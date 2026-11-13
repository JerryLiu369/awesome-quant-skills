#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
SKILLS_DIR="${REPO_ROOT}/skills"

TARGET=""
FORCE=0
DRY_RUN=0
LIST_ONLY=0
ITEM=""

usage() {
  cat <<'EOF'
Usage:
  install_skill.sh --list
  install_skill.sh <skill-name|category|all> --target <target> [--force] [--dry-run]

Targets:
  claude          -> ~/.claude/skills
  hermes          -> ~/.hermes/skills
  codex           -> ~/.codex/skills
  opencode        -> ~/.config/opencode/skills
  agents          -> ~/.agents/skills
  custom:<path>   -> <path>

Options:
  --list          List all available mirrored skills
  --target <t>    Destination harness target (required for installation)
  --force         Overwrite existing skill directory if it already exists
  --dry-run       Show what would be copied without modifying files
  -h, --help      Show this help message
EOF
}

die() {
  echo "Error: $*" >&2
  exit 1
}

validate_safe_name() {
  local val="$1"
  if [[ -z "$val" ]]; then
    die "Empty skill or category name."
  fi
  if [[ "$val" == *".."* || "$val" == /* || "$val" == *"\\"* ]]; then
    die "Invalid name (path traversal or absolute path not allowed): $val"
  fi
  if [[ ! "$val" =~ ^[A-Za-z0-9._-]+$ ]]; then
    die "Invalid characters in name '$val'. Allowed: [A-Za-z0-9._-]"
  fi
}

resolve_target_dir() {
  local t="$1"
  case "$t" in
    claude)
      echo "${HOME}/.claude/skills"
      ;;
    hermes)
      echo "${HOME}/.hermes/skills"
      ;;
    codex)
      echo "${HOME}/.codex/skills"
      ;;
    opencode)
      echo "${HOME}/.config/opencode/skills"
      ;;
    agents)
      echo "${HOME}/.agents/skills"
      ;;
    custom:*)
      local custom_path="${t#custom:}"
      if [[ -z "$custom_path" ]]; then
        die "custom:<path> requires a non-empty path."
      fi
      if [[ "$custom_path" == *".."* ]]; then
        die "Path traversal ('..') is not allowed in custom target path: $custom_path"
      fi
      custom_path="${custom_path/#\~/$HOME}"
      echo "$custom_path"
      ;;
    *)
      die "Unknown target '$t'. Expected: claude|hermes|codex|opencode|agents|custom:<path>"
      ;;
  esac
}

list_skills() {
  [[ -d "$SKILLS_DIR" ]] || die "Skills directory not found: $SKILLS_DIR"
  local count=0
  local current_cat=""
  while IFS= read -r skill_file; do
    local rel="${skill_file#${SKILLS_DIR}/}"
    local cat="${rel%%/*}"
    local rest="${rel#*/}"
    local name="${rest%/SKILL.md}"
    if [[ "$cat" != "$current_cat" ]]; then
      echo "[$cat]"
      current_cat="$cat"
    fi
    echo "  - $name  (${cat}/${name})"
    count=$((count + 1))
  done < <(find "$SKILLS_DIR" -mindepth 3 -maxdepth 3 -name "SKILL.md" -type f | sort)
  echo "Total: ${count} skills"
}

install_one_skill() {
  local src_dir="$1"
  local dest_root="$2"
  local skill_name
  skill_name="$(basename "$src_dir")"
  local dest_dir="${dest_root}/${skill_name}"

  if [[ -e "$dest_dir" ]]; then
    if [[ "$FORCE" -eq 0 ]]; then
      echo "[SKIP] ${skill_name} -> ${dest_dir} (already exists; use --force to overwrite)"
      return 0
    fi
    if [[ "$DRY_RUN" -eq 1 ]]; then
      echo "[DRY-RUN] Would overwrite ${dest_dir} from ${src_dir}"
      return 0
    fi
    rm -rf -- "$dest_dir"
  fi

  if [[ "$DRY_RUN" -eq 1 ]]; then
    echo "[DRY-RUN] Would install ${skill_name} -> ${dest_dir}"
  else
    mkdir -p -- "$dest_root"
    cp -R -- "$src_dir" "$dest_dir"
    echo "[OK] Installed ${skill_name} -> ${dest_dir}"
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --list)
      LIST_ONLY=1
      shift
      ;;
    --target)
      [[ $# -ge 2 ]] || die "--target requires an argument."
      TARGET="$2"
      shift 2
      ;;
    --target=*)
      TARGET="${1#--target=}"
      shift
      ;;
    --force)
      FORCE=1
      shift
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    -*)
      die "Unknown option: $1"
      ;;
    *)
      if [[ -n "$ITEM" ]]; then
        die "Unexpected extra argument: $1 (already got '$ITEM')"
      fi
      ITEM="$1"
      shift
      ;;
  esac
done

if [[ "$LIST_ONLY" -eq 1 ]]; then
  list_skills
  exit 0
fi

[[ -n "$ITEM" ]] || { usage >&2; die "Missing <skill-name|category|all>."; }
[[ -n "$TARGET" ]] || { usage >&2; die "Missing --target <target>."; }

validate_safe_name "$ITEM"
DEST_ROOT="$(resolve_target_dir "$TARGET")"

if [[ "$ITEM" == "all" ]]; then
  while IFS= read -r skill_file; do
    install_one_skill "$(dirname "$skill_file")" "$DEST_ROOT"
  done < <(find "$SKILLS_DIR" -mindepth 3 -maxdepth 3 -name "SKILL.md" -type f | sort)
  exit 0
fi

if [[ -d "${SKILLS_DIR}/${ITEM}" ]]; then
  found_in_cat=0
  while IFS= read -r skill_file; do
    install_one_skill "$(dirname "$skill_file")" "$DEST_ROOT"
    found_in_cat=$((found_in_cat + 1))
  done < <(find "${SKILLS_DIR}/${ITEM}" -mindepth 2 -maxdepth 2 -name "SKILL.md" -type f | sort)
  [[ "$found_in_cat" -gt 0 ]] || die "No skills found under category: ${ITEM}"
  exit 0
fi

mapfile -t matches < <(find "$SKILLS_DIR" -mindepth 3 -maxdepth 3 -path "*/${ITEM}/SKILL.md" -type f | sort)
if [[ "${#matches[@]}" -eq 0 ]]; then
  die "Skill or category not found: ${ITEM} (run --list to see available skills)"
elif [[ "${#matches[@]}" -gt 1 ]]; then
  die "Ambiguous skill name '${ITEM}' matched multiple paths: ${matches[*]}"
fi

install_one_skill "$(dirname "${matches[0]}")" "$DEST_ROOT"
