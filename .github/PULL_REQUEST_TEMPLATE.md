## What does this PR do?

<!-- e.g. "Add Owner/Repo to Alpha Generation & Factor Mining" -->

## Checklist

- [ ] Entry format is `- [Owner/Repo](https://github.com/Owner/Repo) - Objective description.`
- [ ] Placed in the single best-fitting section, in alphabetical order, not a duplicate
- [ ] Added to **both** `README.md` and `README.zh-CN.md` (same section, same link target)
- [ ] Repo is public, maintained, and has a clear license; no live keys or secrets
- [ ] Description notes any API key / paid account / commercial backend requirement
- [ ] Backtest/alpha claims (if any) account for lookahead bias, adjustments and costs
- [ ] Mirrored skill only: `Imported from` header kept, `NOTICE.md` row added (with upstream license), mirror count synced in READMEs and `llms.txt`
- [ ] Ran `python3 scripts/build_catalog.py` and `python3 scripts/validate.py` locally (all PASS)
