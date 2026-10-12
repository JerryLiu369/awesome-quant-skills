# Third-Party Notices

This repository's own curation work — `README.md`, `data/catalog.json`,
`.github/workflows/`, and `CONTRIBUTING.md` — is released under the
[MIT License](LICENSE) (Copyright 2026 JerryLiu369).

Files under [`skills/`](skills/) are **mirrored from upstream projects** and
**retain their original licenses**. They are NOT relicensed to MIT by this
project. The HTML comment header in each `SKILL.md` records its
`Imported from` source and original `Source Path`.

## Scope and redistribution rules

1. Where the upstream project declares a license (e.g. in its repo `LICENSE`
   file or in the `SKILL.md` frontmatter), that license governs the mirrored
   file. In particular, files marked `GPL-3.0-only` / `GPL-3.0` below remain
   under the GNU General Public License v3.0 and are distributed under those
   terms.
2. Where no license marker was copied into the mirrored `SKILL.md`, the file
   remains the property of its upstream authors — consult the upstream
   repository before commercial redistribution. Do not assume MIT.
3. Mirrors in this repo are `SKILL.md`-only excerpts. Companion code the skill
   may reference (`scripts/`, `workflows/`, `references/`, bundled configs)
   generally still lives upstream. For runnable use, fetch the full upstream
   project (see `upstream` links in `data/catalog.json`).

## Mirrored skills and known licenses

| Skill (local path) | Upstream | License status in this repo |
|---|---|---|
| `skills/alpha-factors/alpha-zoo/SKILL.md` | HKUDS/Vibe-Trading | Retains upstream license — see source |
| `skills/alpha-factors/breadth-chart-analyst/SKILL.md` | tradermonty/claude-trading-skills | Retains upstream license — see source |
| `skills/alpha-factors/canslim-screener/SKILL.md` | tradermonty/claude-trading-skills | Retains upstream license — see source |
| `skills/alpha-factors/factor-mining-pandaai/SKILL.md` | quantskills/skill-factor-mining-pandaai | **GPL-3.0-only** (declared in-file) |
| `skills/backtesting-audit/backtest-review/SKILL.md` | saksham10arora-dotcom/quant-skills | Retains upstream license — see source |
| `skills/backtesting-audit/backtesting-bias-avoidance/SKILL.md` | quantskills/skill-backtesting-bias-avoidance | **GPL-3.0-only** (declared in-file) |
| `skills/backtesting-audit/data-quality-audit/SKILL.md` | saksham10arora-dotcom/quant-skills | Retains upstream license — see source |
| `skills/backtesting-audit/paper-repro/SKILL.md` | saksham10arora-dotcom/quant-skills | Retains upstream license — see source |
| `skills/backtesting-audit/pine-backtester/SKILL.md` | TradersPost/pinescript-agents | Retains upstream license — see source |
| `skills/backtesting-audit/stats-test-picker/SKILL.md` | saksham10arora-dotcom/quant-skills | Retains upstream license — see source |
| `skills/backtesting-audit/vectorbt-backtest/SKILL.md` | marketcalls/vectorbt-backtesting-skills | Retains upstream license — see source |
| `skills/backtesting-audit/vectorbt-optimize/SKILL.md` | marketcalls/vectorbt-backtesting-skills | Retains upstream license — see source |
| `skills/china-markets/akquant/SKILL.md` | lzwme/finance-quant-skills | Retains upstream license — see source |
| `skills/china-markets/ashare-pre-st-filter/SKILL.md` | HKUDS/Vibe-Trading | Retains upstream license — see source |
| `skills/china-markets/cninfo-disclosure/SKILL.md` | rollysys/use_cninfo | Retains upstream license — see source |
| `skills/china-markets/ctp-api/SKILL.md` | algoderiv/agent-skills | Retains upstream license — see source |
| `skills/china-markets/ptrade-strategy-writing/SKILL.md` | xxbbzy/ptrade-agent-skills | Retains upstream license — see source |
| `skills/china-markets/quant-buddy/SKILL.md` | pseudo-longinus/quant-buddy-skills | Retains upstream license — see source; requires commercial `quant-buddy` API backend |
| `skills/china-markets/ssquant-futures/SKILL.md` | quantskills/agent-ssquant | **GPL-3.0** (declared in-file) |
| `skills/china-markets/tdxquant/SKILL.md` | lingfan/tdxquant-mcp | Retains upstream license — see source |
| `skills/china-markets/tqsdk-trading/SKILL.md` | shinnytech/tqsdk-python | Retains upstream license — see source |
| `skills/china-markets/wencai-screener/SKILL.md` | raidery/quant-skills | Retains upstream license — see source |
| `skills/crypto-web3/defillama-data/SKILL.md` | DefiLlama/defillama-skills | Retains upstream license — see source |
| `skills/crypto-web3/defillama-flows/SKILL.md` | DefiLlama/defillama-skills | Retains upstream license — see source |
| `skills/crypto-web3/defillama-yields/SKILL.md` | DefiLlama/defillama-skills | Retains upstream license — see source |
| `skills/crypto-web3/perp-funding-basis/SKILL.md` | HKUDS/Vibe-Trading | Retains upstream license — see source |
| `skills/crypto-web3/pine-debugger/SKILL.md` | TradersPost/pinescript-agents | Retains upstream license — see source |
| `skills/crypto-web3/pine-developer/SKILL.md` | TradersPost/pinescript-agents | Retains upstream license — see source |
| `skills/global-equities/edgar-financials/SKILL.md` | dgunning/edgartools | Retains upstream license — see source |
| `skills/global-equities/llmquant-equities/SKILL.md` | LLMQuant/skills | Retains upstream license — see source |
| `skills/global-equities/llmquant-macro/SKILL.md` | LLMQuant/skills | Retains upstream license — see source |
| `skills/portfolio-risk/llmquant-risk/SKILL.md` | LLMQuant/skills | Retains upstream license — see source |
| `skills/portfolio-risk/openquant-trading/SKILL.md` | mitchellbernstein/openquant | Retains upstream license — see source |

If you are an upstream author and want your skill's license recorded
precisely here (or removed from the mirror), please open an issue or PR —
the `Imported from` header plus this table is the intended attribution chain.
New mirrored-skill PRs must record the upstream license in
`data/catalog.json` (`license` field) and keep this table in sync.
