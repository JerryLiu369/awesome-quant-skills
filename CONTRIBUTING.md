# Contributing to Awesome Quant Skills

Thank you for contributing! We aim to maintain a high-signal index of agent skills and tools for quantitative finance.

## Submission Guidelines

1. **Format**: Follow the standard format:
   ```markdown
   - [Owner/Repo](https://github.com/Owner/Repo) - Short, objective description of the skill and its supported agent harnesses.
   ```
2. **Quality Standards**:
   - The repository must contain concrete agent skills (`SKILL.md`), MCP definitions, or clear agent orchestration workflows.
   - Do not submit stale code dumps, broken scrapers, or get-rich-quick trading bot spam.
   - Financial accuracy: backtest skills should demonstrate awareness of lookahead bias, split adjustments, and realistic transaction costs.
3. **Placement**: Put the entry in the single most fitting category (vertical market stack first, pipeline stage second); don't list the same repo twice. Ordering within a section doesn't matter.
4. **Uncategorized Skills & Rule of Three**: If a skill does not fit neatly into an existing pipeline stage or market stack, place it under `Miscellaneous & Other Skills`. When 3 or more related skills accumulate under a distinct theme, they will graduate into an independent category.

## Pull Request Process

1. Fork the repository.
2. Add your entry to `README.md`.
3. For mirrored skills under `skills/`: keep the `Imported from` header with the upstream URL, and add the matching row (local path, upstream, license) to `NOTICE.md` (CI checks every mirrored skill is listed there).
4. Submit a PR with a clear title (e.g., `Add Owner/Repo to Alpha Generation`).
