#!/usr/bin/env python3
"""Check upstream GitHub repositories listed in README.md for health & status.

Uses Python 3.11+ standard library only (urllib.request + concurrent.futures).
Supports GITHUB_TOKEN env var or `gh auth token` for higher rate limits.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from pathlib import Path

GITHUB_API_BASE = "https://api.github.com"
GITHUB_REPO_RE = re.compile(
    r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)"
)
EXCLUDED_SLUGS = {
    "jerryliu369/awesome-quant-skills",
    "owner/repo",
}


@dataclass
class RepoStatus:
    slug: str
    url: str
    http_status: int | None
    ok: bool
    issue: str | None
    full_name: str | None = None
    archived: bool | None = None
    stars: int | None = None
    pushed_at: str | None = None


def resolve_github_token() -> str | None:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token.strip()
    try:
        proc = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        if proc.returncode == 0 and proc.stdout.strip():
            return proc.stdout.strip()
    except (FileNotFoundError, subprocess.SubprocessError):
        pass
    return None


def extract_repo_slugs(readme_path: Path) -> list[str]:
    text = readme_path.read_text(encoding="utf-8")
    seen: set[str] = set()
    slugs: list[str] = []
    for m in GITHUB_REPO_RE.finditer(text):
        owner, repo = m.group(1), m.group(2)
        if repo.endswith(".git"):
            repo = repo[:-4]
        slug = f"{owner}/{repo}"
        key = slug.lower()
        if key in EXCLUDED_SLUGS or key in seen:
            continue
        seen.add(key)
        slugs.append(slug)
    return slugs


def check_single_repo(slug: str, token: str | None, timeout: float = 15.0) -> RepoStatus:
    api_url = f"{GITHUB_API_BASE}/repos/{slug}"
    html_url = f"https://github.com/{slug}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-quant-skills-check-repos/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(api_url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status_code = resp.status
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code in (404, 410):
            issue = f"HTTP {exc.code} (not found / gone)"
        elif exc.code == 403:
            issue = "HTTP 403 (rate limited or forbidden)"
        else:
            issue = f"HTTP {exc.code}"
        return RepoStatus(
            slug=slug,
            url=html_url,
            http_status=exc.code,
            ok=False,
            issue=issue,
        )
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return RepoStatus(
            slug=slug,
            url=html_url,
            http_status=None,
            ok=False,
            issue=f"Request error: {exc}",
        )

    full_name = data.get("full_name", "")
    archived = bool(data.get("archived", False))
    stars = data.get("stargazers_count")
    pushed_at = data.get("pushed_at")

    issues: list[str] = []
    if full_name and full_name.lower() != slug.lower():
        issues.append(f"renamed/redirected -> {full_name}")
    if archived:
        issues.append("archived=true")

    return RepoStatus(
        slug=slug,
        url=html_url,
        http_status=status_code,
        ok=len(issues) == 0,
        issue="; ".join(issues) if issues else None,
        full_name=full_name or None,
        archived=archived,
        stars=stars,
        pushed_at=pushed_at,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check upstream GitHub repositories in README.md."
    )
    parser.add_argument(
        "--readme",
        default="README.md",
        help="Path to README.md (default: README.md)",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=8,
        help="Concurrent worker threads (default: 8)",
    )
    parser.add_argument(
        "--only-issues",
        action="store_true",
        help="Only output repositories with issues (404/410, renamed, archived, errors)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON report",
    )
    args = parser.parse_args(argv)

    readme_path = Path(args.readme).resolve()
    if not readme_path.is_file():
        print(f"Error: README not found at {readme_path}", file=sys.stderr)
        return 2

    slugs = extract_repo_slugs(readme_path)
    token = resolve_github_token()

    results_by_slug: dict[str, RepoStatus] = {}
    with ThreadPoolExecutor(max_workers=max(1, args.max_workers)) as pool:
        future_map = {
            pool.submit(check_single_repo, slug, token): slug for slug in slugs
        }
        for fut in as_completed(future_map):
            res = fut.result()
            results_by_slug[res.slug] = res

    ordered = [results_by_slug[s] for s in slugs]
    issues_list = [r for r in ordered if not r.ok]
    display_list = issues_list if args.only_issues else ordered

    if args.json:
        payload = {
            "total_checked": len(ordered),
            "issues_count": len(issues_list),
            "authenticated": bool(token),
            "results": [asdict(r) for r in display_list],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        auth_note = "authenticated" if token else "unauthenticated (60 req/hr limit)"
        print(f"Checked {len(ordered)} GitHub repositories ({auth_note}).")
        for r in display_list:
            if r.ok:
                pushed = (r.pushed_at or "")[:10]
                print(
                    f"[OK]    {r.slug:<48} stars={r.stars} pushed={pushed}"
                )
            else:
                print(f"[ISSUE] {r.slug:<48} {r.issue}")
        print(
            f"\nSummary: {len(ordered) - len(issues_list)}/{len(ordered)} healthy, "
            f"{len(issues_list)} issue(s) found."
        )

    return 0 if not issues_list else 1


if __name__ == "__main__":
    sys.exit(main())
