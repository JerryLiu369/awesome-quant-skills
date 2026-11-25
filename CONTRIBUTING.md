# Contributing to Awesome Quant Skills

Thanks for helping keep this a high-signal index of agent skills and tools for quantitative finance.
Not sure where something belongs? Open a [Submit New Entry](https://github.com/JerryLiu369/awesome-quant-skills/issues/new/choose) issue first.

## Inclusion criteria

An entry must be:

- **Agent-usable**: a `SKILL.md`, an MCP server definition, or a documented agent orchestration workflow.
- **Public and maintained**: open GitHub repo, a clear license, not archived, no dead links.
- **Quant-relevant**: data, alpha/factors, portfolio/risk, backtesting/audit, or execution for finance.
- **Honest about finance**: backtest skills show awareness of lookahead bias, split/dividend adjustments, survivorship bias and realistic costs.

Rejected: stale code dumps, broken scrapers, "get-rich-quick" bot spam, repos with live keys or secrets,
and anything that trades real money without a paper-trading default and human approval (see [SECURITY.md](SECURITY.md)).

## Entry format

One line per repo, one category only (never list a repo twice):

```markdown
- [Owner/Repo](https://github.com/Owner/Repo) - Objective one-sentence description of what it does and which harnesses it supports (needs an XYZ API key).
```

- Description: factual, no marketing; end with the auth/cost note in parentheses when a key or paid account is needed.
- Placement: vertical market stack first (China / Crypto / US & Global), universal pipeline stage second; if nothing fits, use `Miscellaneous & Other Skills`. Three related misc entries graduate into their own category.
- Order: alphabetical by `Owner/Repo` (case-insensitive) within each section.
- Mirrored entries also carry a note such as `(mirrored at `skills/<category>/<name>/SKILL.md`)`.

## Both languages are required

Add the entry to **both** `README.md` and `README.zh-CN.md` in the same section, with the same link target.
The Chinese file may translate the description; link counts must stay identical (the validator checks this). When you add or remove an entry, also update the `entries-N` badge and the matching row of the "At a glance" table in both READMEs (also validator-checked).

## Adding a mirrored skill (optional)

1. Copy the upstream `SKILL.md` to `skills/<category>/<name>/SKILL.md`. Frontmatter needs `name` and `description`.
2. Keep (or add) the HTML header with `Imported from: <upstream URL>` and `Source Path:`.
3. Add a row to the table in [NOTICE.md](NOTICE.md): local path, upstream `Owner/Repo`, upstream license. Never relicense to MIT.
4. Reference the path in both READMEs, and bump the mirror count everywhere it appears
   (`README.md`, `README.zh-CN.md`, `llms.txt`).
5. Regenerate the catalog: `python3 scripts/build_catalog.py` (writes `skills/README.md`; never edit it by hand).

## Validate locally

```bash
python3 scripts/build_catalog.py          # regenerate skills/README.md
python3 scripts/build_catalog.py --check  # exit 1 if stale
python3 scripts/validate.py               # all checks must PASS
bash -n scripts/install_skill.sh          # if you touched the installer
```

Python 3.11, standard library only. CI also runs a markdown link check (lychee).

## Pull request

1. Fork and branch.
2. Make the changes above.
3. Title like `Add Owner/Repo to Alpha Generation`; the PR template checklist must be satisfied.
