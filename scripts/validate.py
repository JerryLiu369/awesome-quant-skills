#!/usr/bin/env python3
"""Repository integrity validator for awesome-quant-skills.

Uses Python 3.11+ standard library only (no third-party dependencies).
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

REQUIRED_ROOT_FILES = [
    "LICENSE",
    "NOTICE.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "README.md",
    "README.zh-CN.md",
    "llms.txt",
]

SELF_REPO_SLUG = "jerryliu369/awesome-quant-skills"
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
GITHUB_LINK_RE = re.compile(r"\]\(https://github\.com/")
GITHUB_REPO_RE = re.compile(
    r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)"
)
TOC_ANCHOR_RE = re.compile(r"\[[^\]]+\]\(#([^)]+)\)")


@dataclass
class CheckResult:
    name: str
    passed: bool
    details: list[str]


def github_heading_slug(heading_text: str) -> str:
    """Convert a Markdown heading into a GitHub-compatible anchor slug."""
    text = heading_text.strip()
    # Strip inline markdown links [label](url) -> label
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Strip inline code backticks and emphasis markers
    text = text.replace("`", "")
    text = text.lower()
    # Keep Unicode word characters (letters, digits, CJK, underscores), spaces, and hyphens.
    # GitHub strips punctuation (including '.', '&', '/', etc.) and emojis, then maps spaces to '-'.
    cleaned_chars: list[str] = []
    for ch in text:
        if ch == " " or ch == "-" or ch == "_" or ch.isalnum():
            cleaned_chars.append(ch)
    slug = "".join(cleaned_chars).replace(" ", "-")
    return slug


def extract_headings(markdown_text: str) -> tuple[list[tuple[int, str, str]], dict[str, int]]:
    """Extract headings outside fenced code blocks and return (headings, level_counts)."""
    headings: list[tuple[int, str, str]] = []
    level_counts: dict[str, int] = {"h1": 0, "h2": 0, "h3": 0, "h4": 0}
    seen_slugs: dict[str, int] = {}
    in_fence = False

    for line in markdown_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.+?)\s*#*$", line)
        if not m:
            continue
        level = len(m.group(1))
        raw_title = m.group(2).strip()
        if f"h{level}" in level_counts:
            level_counts[f"h{level}"] += 1
        base_slug = github_heading_slug(raw_title)
        if base_slug in seen_slugs:
            seen_slugs[base_slug] += 1
            unique_slug = f"{base_slug}-{seen_slugs[base_slug]}"
        else:
            seen_slugs[base_slug] = 0
            unique_slug = base_slug
        headings.append((level, raw_title, unique_slug))

    return headings, level_counts


def extract_external_repo_slugs(markdown_text: str) -> list[str]:
    """Extract external owner/repo slugs from directory entries / GitHub links."""
    slugs: list[str] = []
    for line in markdown_text.splitlines():
        # Focus on list-item directory entries or general GitHub repo links
        for m in GITHUB_REPO_RE.finditer(line):
            owner, repo = m.group(1), m.group(2)
            # Strip trailing .git if present
            if repo.endswith(".git"):
                repo = repo[:-4]
            slug = f"{owner}/{repo}"
            if slug.lower() == SELF_REPO_SLUG:
                continue
            # Ignore template placeholder
            if slug.lower() == "owner/repo":
                continue
            slugs.append(slug)
    return slugs


def run_validations(
    root: Path, allow_unreferenced_mirrors: bool = False
) -> list[CheckResult]:
    results: list[CheckResult] = []

    # 1. Required root files
    missing_root = [f for f in REQUIRED_ROOT_FILES if not (root / f).is_file()]
    results.append(
        CheckResult(
            name="required_root_files",
            passed=len(missing_root) == 0,
            details=(
                [f"All {len(REQUIRED_ROOT_FILES)} required root files present."]
                if not missing_root
                else [f"Missing required root file: {f}" for f in missing_root]
            ),
        )
    )

    # Read core docs if present
    def read_text(rel: str) -> str:
        p = root / rel
        return p.read_text(encoding="utf-8") if p.is_file() else ""

    notices_text = read_text("NOTICE.md")
    readme_en = read_text("README.md")
    readme_zh = read_text("README.zh-CN.md")
    llms_txt = read_text("llms.txt")

    # 2. Discover and validate SKILL.md files
    skill_paths = sorted(
        {
            Path(p).as_posix()
            for p in (
                glob.glob("skills/*/SKILL.md", root_dir=root)
                + glob.glob("skills/*/*/SKILL.md", root_dir=root)
            )
        }
    )

    skill_errors: list[str] = []
    if not skill_paths:
        skill_errors.append("No mirrored skills found under skills/")
    else:
        for rel_path in skill_paths:
            full_path = root / rel_path
            if full_path.stat().st_size == 0:
                skill_errors.append(f"Empty file: {rel_path}")
                continue
            text = full_path.read_text(encoding="utf-8", errors="replace")
            fm_match = re.search(r"^---\s*\n(.*?)---", text, re.S | re.M)
            fm = fm_match.group(1) if fm_match else ""
            if "name:" not in fm or "description:" not in fm:
                skill_errors.append(
                    f"Invalid SKILL.md frontmatter (needs name: + description:): {rel_path}"
                )
            if "Imported from:" not in text:
                skill_errors.append(f"Missing 'Imported from:' header: {rel_path}")
            if rel_path not in notices_text:
                skill_errors.append(f"Skill not listed in NOTICE.md: {rel_path}")

    results.append(
        CheckResult(
            name="skill_files_validation",
            passed=len(skill_errors) == 0,
            details=(
                [f"Validated {len(skill_paths)} mirrored SKILL.md files."]
                if not skill_errors
                else skill_errors
            ),
        )
    )

    # 3. Mirror count accuracy in README.md, README.zh-CN.md, llms.txt
    mirror_count = len(skill_paths)
    count_pattern = re.compile(rf"(?<!\d){mirror_count}(?!\d)")
    count_errors: list[str] = []
    for doc_name, doc_text in [
        ("README.md", readme_en),
        ("README.zh-CN.md", readme_zh),
        ("llms.txt", llms_txt),
    ]:
        if not count_pattern.search(doc_text):
            count_errors.append(
                f"Mirror count {mirror_count} missing from {doc_name}"
            )
    results.append(
        CheckResult(
            name="mirror_count_sync",
            passed=len(count_errors) == 0,
            details=(
                [f"Mirror count ({mirror_count}) present in README.md, README.zh-CN.md, and llms.txt."]
                if not count_errors
                else count_errors
            ),
        )
    )

    # 4. Heading hierarchy consistency (H2/H3 counts) between README.md and README.zh-CN.md
    en_headings, en_counts = extract_headings(readme_en)
    zh_headings, zh_counts = extract_headings(readme_zh)
    heading_errors: list[str] = []
    for lvl in ("h2", "h3"):
        if en_counts[lvl] != zh_counts[lvl]:
            heading_errors.append(
                f"{lvl.upper()} count mismatch: README.md={en_counts[lvl]}, README.zh-CN.md={zh_counts[lvl]}"
            )
    results.append(
        CheckResult(
            name="readme_heading_hierarchy",
            passed=len(heading_errors) == 0,
            details=(
                [
                    f"H2 ({en_counts['h2']}) and H3 ({en_counts['h3']}) counts match between README.md and README.zh-CN.md."
                ]
                if not heading_errors
                else heading_errors
            ),
        )
    )

    # 5. GitHub directory entry count parity
    en_gh_count = len(GITHUB_LINK_RE.findall(readme_en))
    zh_gh_count = len(GITHUB_LINK_RE.findall(readme_zh))
    results.append(
        CheckResult(
            name="readme_entry_count_parity",
            passed=en_gh_count == zh_gh_count,
            details=(
                [f"GitHub link count matches ({en_gh_count}) in both READMEs."]
                if en_gh_count == zh_gh_count
                else [
                    f"EN/ZH GitHub directory entry count mismatch: README.md={en_gh_count}, README.zh-CN.md={zh_gh_count}"
                ]
            ),
        )
    )

    # 6. Duplicate external owner/repo slugs
    dup_errors: list[str] = []
    for doc_name, doc_text in [("README.md", readme_en), ("README.zh-CN.md", readme_zh)]:
        seen: dict[str, str] = {}
        for slug in extract_external_repo_slugs(doc_text):
            key = slug.lower()
            if key in seen:
                dup_errors.append(
                    f"Duplicate repo slug in {doc_name}: {slug} (first seen as {seen[key]})"
                )
            else:
                seen[key] = slug
    results.append(
        CheckResult(
            name="no_duplicate_repos",
            passed=len(dup_errors) == 0,
            details=(
                ["No duplicate external owner/repo slugs in README.md or README.zh-CN.md."]
                if not dup_errors
                else dup_errors
            ),
        )
    )

    # 7. TOC and internal #anchor resolution
    anchor_errors: list[str] = []
    for doc_name, doc_text, headings in [
        ("README.md", readme_en, en_headings),
        ("README.zh-CN.md", readme_zh, zh_headings),
    ]:
        valid_slugs = {slug for _, _, slug in headings}
        in_fence = False
        for lineno, line in enumerate(doc_text.splitlines(), start=1):
            stripped = line.strip()
            if stripped.startswith("```") or stripped.startswith("~~~"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for m in TOC_ANCHOR_RE.finditer(line):
                anchor = m.group(1)
                if anchor not in valid_slugs:
                    anchor_errors.append(
                        f"{doc_name}:{lineno}: unresolved anchor '#{anchor}'"
                    )
    results.append(
        CheckResult(
            name="toc_anchor_resolution",
            passed=len(anchor_errors) == 0,
            details=(
                ["All internal #anchor links resolve to valid heading slugs."]
                if not anchor_errors
                else anchor_errors
            ),
        )
    )

    # 8. No Chinese characters in README.md body (except language-switch line)
    cjk_errors: list[str] = []
    for lineno, line in enumerate(readme_en.splitlines(), start=1):
        if "[中文](README.zh-CN.md)" in line:
            continue
        if CJK_RE.search(line):
            cjk_errors.append(
                f"README.md:{lineno}: unexpected CJK characters outside language-switch line: {line.strip()[:80]}"
            )
    results.append(
        CheckResult(
            name="english_readme_no_cjk",
            passed=len(cjk_errors) == 0,
            details=(
                ["README.md contains no CJK characters outside the language-switch line."]
                if not cjk_errors
                else cjk_errors
            ),
        )
    )

    # 9. Every local mirrored SKILL.md referenced in both README.md and README.zh-CN.md
    unref_errors: list[str] = []
    for rel_path in skill_paths:
        if rel_path not in readme_en:
            unref_errors.append(f"Unreferenced mirror in README.md: {rel_path}")
        if rel_path not in readme_zh:
            unref_errors.append(f"Unreferenced mirror in README.zh-CN.md: {rel_path}")
    passed_unref = len(unref_errors) == 0 or allow_unreferenced_mirrors
    if unref_errors and allow_unreferenced_mirrors:
        details = [
            f"Allowed {len(unref_errors)} unreferenced mirror notices via --allow-unreferenced-mirrors."
        ]
    elif not unref_errors:
        details = [f"All {len(skill_paths)} mirrored SKILL.md paths are referenced in both READMEs."]
    else:
        details = unref_errors
    results.append(
        CheckResult(
            name="mirrors_referenced_in_readmes",
            passed=passed_unref,
            details=details,
        )
    )

    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate awesome-quant-skills repository structure and metadata."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root directory (default: current directory)",
    )
    parser.add_argument(
        "--allow-unreferenced-mirrors",
        action="store_true",
        help="Do not fail if local skills/<cat>/<name>/SKILL.md paths are not explicitly mentioned in READMEs",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output machine-readable JSON summary",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    results = run_validations(
        root=root,
        allow_unreferenced_mirrors=args.allow_unreferenced_mirrors,
    )
    all_passed = all(r.passed for r in results)

    if args.json:
        payload = {
            "passed": all_passed,
            "checks": [asdict(r) for r in results],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for r in results:
            status = "PASS" if r.passed else "FAIL"
            print(f"[{status}] {r.name}")
            for detail in r.details:
                print(f"       - {detail}")
        passed_count = sum(1 for r in results if r.passed)
        print(
            f"\nSummary: {passed_count}/{len(results)} checks passed. "
            f"Overall: {'PASS' if all_passed else 'FAIL'}"
        )

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
