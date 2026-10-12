# Awesome Quant Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> A curated directory of **Agent Skills**, **Quant MCP Servers**, and **Skill-Native Systems** for Quantitative Finance, Systematic Research, and Algorithmic Trading across **Claude Code**, **OpenCode**, **Codex**, and **Hermes**.

Unlike legacy quant lists cluttered with abandoned libraries, this directory focuses strictly on **autonomous agent capabilities**: machine-executable `SKILL.md` workflows, Model Context Protocol (MCP) tooling, and deterministic quantitative reasoning.

---

## 📌 Scope & Inclusion Standards

Entries are strictly organized across operational tiers:

1. **Native Agent Skills (80% Focus)**: Portable `SKILL.md` specifications, prompts, and orchestration recipes usable in modern coding agents (Claude Code, OpenCode, Codex, Hermes) without proprietary daemon lock-in.
2. **Quant MCP Servers (15%)**: Model Context Protocol servers exposing standardized financial tools (market feeds, order routing, statistical testing).
3. **Skill-Native Systems (5%)**: Open-source quant agent frameworks that expose modular, plug-and-play skill architectures.

---

## 📦 Embedded Skills Library

This repository doubles as a **quant skill pack**: 33 `SKILL.md` files mirrored directly inside [`skills/`](skills/), ready to copy into your agent harness (`~/.claude/skills/`, `~/.agents/skills/`, or Hermes). Two caveats: mirrors are `SKILL.md`-only excerpts — helper scripts and reference docs stay upstream (see each file's `Imported from` header) — and most but not all are permissively licensed: three are GPL-family and one (`quant-buddy`) needs a commercial API backend. Check per-skill licenses in [NOTICE.md](NOTICE.md) and [`data/catalog.json`](data/catalog.json) before redistributing.

- **China A-Shares & Futures**: CTP API, PTrade, TqSdk, TDX, MiniQMT, Wencai, CnInfo, AKQuant.
- **Alpha & Factors**: Paper-derived factor mining, Alpha Zoo, CANSLIM screeners.
- **Backtesting & Auditing**: Lookahead bias avoidance, PBO overfitting checks, VectorBT, Purged CV.
- **Crypto & Web3**: Pine Script developer/debugger/backtester, DefiLlama yields & flows, Perp funding basis.
- **Global Equities & Risk**: EDGAR 10-K extraction, LLMQuant equities & macro, OpenQuant VaR risk.

*Full machine-readable registry available at [`data/catalog.json`](data/catalog.json).*

---

## 📑 Table of Contents

- [Vertical Market Stacks](#-vertical-market-stacks)
  - [China A-Shares & Domestic Futures](#china-a-shares--domestic-futures)
  - [Crypto & Web3 Markets](#crypto--web3-markets)
  - [US & Global Equities](#us--global-equities)
- [Universal Quant Pipeline](#-universal-quant-pipeline)
  - [1. Data Ingestion & Market Feeds](#1-data-ingestion--market-feeds)
  - [2. Alpha Generation & Factor Mining](#2-alpha-generation--factor-mining)
  - [3. Portfolio & Risk Allocation](#3-portfolio--risk-allocation)
  - [4. Backtesting & Safety Auditing](#4-backtesting--safety-auditing)
  - [5. Execution & Order Routing](#5-execution--order-routing)
- [Quant MCP Servers](#-quant-mcp-servers)
  - [Market Feeds & Fundamentals](#market-feeds--fundamentals)
  - [Broker & Exchange Gateways](#broker--exchange-gateways)
- [Skill-Native Quant Frameworks](#-skill-native-quant-frameworks)
- [Miscellaneous & Other Skills](#-miscellaneous--other-skills)
- [Contributing](#-contributing)

---

## 🌐 Vertical Market Stacks

*Full-lifecycle skills engineered for specific regional regulations, session rhythms, or market microstructure.*

### China A-Shares & Domestic Futures
- [algoderiv/agent-skills](https://github.com/algoderiv/agent-skills) - Claude Code skills for Chinese quantitative derivatives and CTP 6.7.8 API integration (`skills/ctp-api/SKILL.md`), order execution, and position management alongside TqSdk.
- [hexonal/vnpy_agentbridge](https://github.com/hexonal/vnpy_agentbridge) - FastMCP bridge and IntentEngine running in the VeighNa (vnpy) `MainEngine` process enforcing a "propose-never-execute" boundary with human and `vnpy_riskmanager` approval gating.
- [itsadrianxv/quant-strategy-builder-skill](https://github.com/itsadrianxv/quant-strategy-builder-skill) - Modular skill suite for Claude Code, Codex, and OpenClaw supporting domestic futures (`implement-cn-futures-strategy`) and A-share/ETF execution constraints (`implement-cn-equity-etf-strategy`).
- [juju-w/qmt-mcp](https://github.com/juju-w/qmt-mcp) - Streamable HTTP MCP server running `xtquant` (miniQMT) in Docker/Wine or native Windows for ticker search, historical K-lines, and portfolio inspection.
- [jwangkun/claude-for-financial-services-cn](https://github.com/jwangkun/claude-for-financial-services-cn) - Comprehensive collection of 63 Claude Skills adapted for Chinese financial institutions alongside bundled MCP servers (`akshare-mcp`, `ifind-mcp`, `wind-mcp`).
- [lingfan/tdxquant-mcp](https://github.com/lingfan/tdxquant-mcp) - Model Context Protocol server and native `skills/tdxquant-mcp/SKILL.md` skill for TdxQuant / TongDaXin across Cursor, Claude Code, and Hermes.
- [lzwme/finance-quant-skills](https://github.com/lzwme/finance-quant-skills) - Agent skills tailored for A-share quantitative trading, market analysis, and rule checking.
- [quantskills/agent-ssquant](https://github.com/quantskills/agent-ssquant) - Futures quantitative agent workflow with Anthropic-compatible `skills/ssquant/SKILL.md` to gate CTP/SimNow runtime execution.
- [rollysys/use_cninfo](https://github.com/rollysys/use_cninfo) - Specialized CLI and Claude Code `SKILL.md` skill querying official A-share statutory disclosures on CnInfo and extracting full-text Markdown via PyMuPDF.
- [sencloud/futures_mcp](https://github.com/sencloud/futures_mcp) - Domestic commodity and financial futures MCP server combining AKShare market data feeds, multi-indicator technical analysis, and DeepSeek analytical integration.
- [shinnytech/tqsdk-python](https://github.com/shinnytech/tqsdk-python) - Official Tianqin Quant SDK featuring an embedded agent skill (`tqsdk-trading-and-data/SKILL.md`) for CTP futures/options event loops and margin execution.
- [xxbbzy/ptrade-agent-skills](https://github.com/xxbbzy/ptrade-agent-skills) - Dedicated `SKILL.md` skill suite (`skills/ptrade-strategy-writing`) for Claude Code and Codex with static AST checkers to write and inspect PTrade institutional trading algorithms.

### Crypto & Web3 Markets
- [AlgoVaultLabs/crypto-quant-signal-mcp](https://github.com/AlgoVaultLabs/crypto-quant-signal-mcp) - Multi-venue derivatives intelligence MCP server with 20 pre-built Anthropic agent skills scanning cross-venue funding rate arbitrage across 7 perpetual exchanges.
- [brandononchain/opentrade](https://github.com/brandononchain/opentrade) - Agent skills supporting 24/7 crypto microstructure, Pine Script v6 strategy synthesis, and high-frequency trading heuristics.
- [DefiLlama/defillama-skills](https://github.com/DefiLlama/defillama-skills) - Official agent skills (`yield-strategies`, `defi-data`, `flows-and-events`) connecting agents to DefiLlama for protocol TVL, DEX volumes, yields, and token unlocks.
- [dex-original/okx-agent-trade-kit](https://github.com/dex-original/okx-agent-trade-kit) - AI agent trading kit and MCP server (`okx-trade-mcp`) providing 145 tools across 11 modules for spot and derivatives algorithmic order execution.
- [edkdev/hyperliquid-mcp](https://github.com/edkdev/hyperliquid-mcp) - Python MCP server for Hyperliquid perpetual DEX with EIP-712 order signing, atomic bracket orders (entry + TP + SL), and funding rate streams.
- [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Multi-asset trading agent framework with native `SKILL.md` packaging and `perp-funding-basis` skills for perpetual funding rate cash-and-carry basis arbitrage.
- [kukapay/crypto-liquidations-mcp](https://github.com/kukapay/crypto-liquidations-mcp) - FastMCP streaming server streaming Binance Futures liquidation cascades and order size distributions for market stress detection.
- [kukapay/jupiter-mcp](https://github.com/kukapay/jupiter-mcp) - Dedicated MCP server executing Solana DEX token swaps via Jupiter Ultra API with quote generation, slippage tolerance, and priority fee controls.
- [mirror29/openfinclaw-cli](https://github.com/mirror29/openfinclaw-cli) - Plug-and-play crypto research, backtest, and paper-trade skill integrations for multi-agent environments.
- [sendaifun/solana-agent-kit](https://github.com/sendaifun/solana-agent-kit) - Foundational open-source toolkit connecting AI agents to Solana protocols with 60+ actions (Jupiter, Raydium, Orca, Meteora, Drift).
- [vooi-app/mcp](https://github.com/vooi-app/mcp) - Unified perpetual futures MCP server connecting AI agents to Hyperliquid, Lighter, Aster, and Kinetiq for cross-venue funding rate spread arbitrage.

### US & Global Equities
- [daniel3303/Equibles](https://github.com/daniel3303/Equibles) - Self-hosted financial terminal MCP server providing 62+ agent tools across SEC EDGAR, 13F ownership, congressional disclosures, and FRED data.
- [jsconiers/capitol-trades-mcp](https://github.com/jsconiers/capitol-trades-mcp) - FastMCP server providing 23 specialized tools to track US congressional stock trades from Capitol Trades without API keys.
- [LLMQuant/skills](https://github.com/LLMQuant/skills) - Standardized repository of 18 modular agent skills (`llmquant-equities`, `llmquant-macro`, `llmquant-risk`) compatible with Claude Code, Codex, and Hermes Agent.
- [pseudo-longinus/quant-buddy-skills](https://github.com/pseudo-longinus/quant-buddy-skills) - Full infrastructure skills covering US/HK equities, macro indicators, and multi-asset screening for LLM agents.
- [simonlin1212/global-stock-data](https://github.com/simonlin1212/global-stock-data) - Zero-auth market data skill for Claude Code / Codex with 50+ endpoints covering CBOE options Greeks, 0DTE flow, and policy rates from 38 central banks.
- [stocktwits/stocktwits-mcp](https://github.com/stocktwits/stocktwits-mcp) - Official StockTwits MCP server exposing zero-auth tools to stream retail investor sentiment scores, trending tickers, and social volume momentum.
- [zen-tradings/retail-skills-us](https://github.com/zen-tradings/retail-skills-us) - Skills tailored for US equity rule enforcement, tax-loss harvesting, and retail algorithmic setups.

---

## ⚙️ Universal Quant Pipeline

*Modular skills aligned with each chronological stage of the quantitative investment lifecycle.*

### 1. Data Ingestion & Market Feeds
*Retrieval, cleaning, split-adjustment, and cross-source alignment.*
- [27dream/mcp-eastmoney](https://github.com/27dream/mcp-eastmoney) - Zero-configuration MCP server for Claude Code and Cursor providing direct access to EastMoney push APIs without API keys.
- [CNQQC/xueqiu-mcp](https://github.com/CNQQC/xueqiu-mcp) - MCP server with 29 tools providing structured Xueqiu market data, capital flows, and community sentiment formatted as clean Markdown tables.
- [dgunning/edgartools](https://github.com/dgunning/edgartools) - SEC EDGAR toolkit providing a native MCP server (`edgartools-mcp`) and Claude Code skills for extracting 10-K, 10-Q, 8-K, and Form 4 insider filings into typed data.
- [elsejj/mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock) - Dedicated A-share MCP server providing tiered endpoints for quotes, financial fundamentals, and technical indicators backed by the `msd` database.
- [erwanjun/tushare-mcp-server](https://github.com/erwanjun/tushare-mcp-server) - Production MCP server wrapping 173 Tushare Pro endpoints across A-shares, futures, options, indices, and macro metrics.
- [guangxiangdebizi/FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP) - Multi-market financial MCP server providing 19 tools integrating Tushare Pro for quotes, financial statements, and macro indicators.
- [hypier/tradingview-quantitative-skills](https://github.com/hypier/tradingview-quantitative-skills) - Technical pattern recognition, market scanning, and TradingView feed integration skills.
- [kylefu8/tradingview-akshare-mcp](https://github.com/kylefu8/tradingview-akshare-mcp) - Technical analysis MCP server built on AKShare and TradingView indicators with multi-source fallback.
- [lefterisloukas/edgar-crawler](https://github.com/lefterisloukas/edgar-crawler) - Academic SEC EDGAR extraction engine (WWW 2025) converting 10-K, 10-Q, and 8-K reports into clean, item-segmented JSON structures.
- [quantskills/quantskills](https://github.com/quantskills/quantskills) - Panoramic ecosystem navigation and standard data retrieval workflows for financial agents.
- [raidery/quant-skills](https://github.com/raidery/quant-skills) - Quant skill pack featuring `wencai/SKILL.md` for natural-language stock screening via `pywencai`.
- [stefanoamorelli/fred-mcp-server](https://github.com/stefanoamorelli/fred-mcp-server) - Dedicated Model Context Protocol server delivering universal access to over 800,000 Federal Reserve Economic Data (FRED®) time series.
- [stefanoamorelli/sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp) - High-precision MCP server connecting AI coding assistants directly to SEC EDGAR filings (10-K, 10-Q, 8-K), parsed XBRL statements, and Form 4 insider transactions.
- [zwldarren/akshare-one-mcp](https://github.com/zwldarren/akshare-one-mcp) - FastMCP server built on `akshare-one` exposing Chinese equity quotes, K-lines, and financials with multi-source fallback.

### 2. Alpha Generation & Factor Mining
*Hypothesis testing, formulaic alpha derivation, and research document processing.*
- [Abel-ai-lab/predict-anything](https://github.com/Abel-ai-lab/predict-anything) - Causal market analysis, alpha discovery, and predictive market structure extraction skills.
- [CTAAgents/quant-skills](https://github.com/CTAAgents/quant-skills) - AI-driven Commodity Trading Advisor (CTA) skills leveraging genetic programming for factor discovery.
- [Howard-Jerry/quant-agent-skills](https://github.com/Howard-Jerry/quant-agent-skills) - 8,000-line orchestration skill for concept thematic analysis, industry supply chain mapping, and factor screening.
- [minihellboy/factorminer](https://github.com/minihellboy/factorminer) - Quantitative alpha discovery engine with LLM-guided symbolic search, typed DSL execution, and native MCP server support.
- [noahnan-max/governed-dcf-skill](https://github.com/noahnan-max/governed-dcf-skill) - Portable, governed agent skill (`SKILL.md`) for Codex providing auditable multi-scenario FCFF valuation, reverse DCF, and WACC sensitivity matrices.
- [quantskills/skill-factor-mining-pandaai](https://github.com/quantskills/skill-factor-mining-pandaai) - Academic paper factor extraction and structured financial analysis skills.
- [stockvaluation-io/stockvaluation_io](https://github.com/stockvaluation-io/stockvaluation_io) - Local-first MCP DCF valuation engine decoupling qualitative thesis generation from deterministic Damodaran-style valuation math.
- [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) - Collection of 70+ domain-specific trading skills for AI coding agents covering market breadth analysis, technical screening, and trade journaling.
- [TradersPost/pinescript-agents](https://github.com/TradersPost/pinescript-agents) - Claude Code skills (`pine-developer`, `pine-debugger`, `pine-backtester`) engineered to generate TradingView Pine Script v6 strategies with automated broker alert webhooks.
- [VernonOY/replicalpha](https://github.com/VernonOY/replicalpha) - Quant research reproduction agent extracting factors from research PDFs into executable Python code with Red Team validation.

### 3. Portfolio & Risk Allocation
*Capital allocation, position sizing, risk parity, and dynamic rebalancing.*
- [agiprolabs/claude-trading-skills](https://github.com/agiprolabs/claude-trading-skills) - 68 trading skills featuring Kelly criterion position sizing, regime detection, and slippage modeling.
- [dcajasn/Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) - Quantitative strategic asset allocation library supporting 24+ convex risk measures (CVaR, CDaR, EVaR) and nested clustered optimization (HRP, HERC, HER2).
- [ElmatadorZ/Money-Atlas-Intelligence-OS](https://github.com/ElmatadorZ/Money-Atlas-Intelligence-OS) - Smart Money Concepts (SMC) market structure and asset allocation guidance skill.
- [jackson-video-resources/markov-hedge-fund-method](https://github.com/jackson-video-resources/markov-hedge-fund-method) - Markov regime detection skill for dynamic portfolio risk-on/risk-off regime switching.
- [mitchellbernstein/openquant](https://github.com/mitchellbernstein/openquant) - Open-source quant operating system providing an MCP server and Hermes/Claude Agent Skills for VaR risk assessment and signal generation.
- [PyPortfolio/PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt) - Production-grade portfolio optimization implementing Mean-Variance Efficient Frontier, Black-Litterman allocation, and Hierarchical Risk Parity (HRP).

### 4. Backtesting & Safety Auditing
*Simulation, lookahead bias prevention, data-leakage auditing, and return attribution.*
- [bettyguo/agent-backtest-lab](https://github.com/bettyguo/agent-backtest-lab) - Statistical-rigor audit harness designed specifically for LLM trading-agent frameworks to prevent lookahead leakage, prompt-bias self-deception, and PBO overfitting.
- [bmouler/lookahead-lint](https://github.com/bmouler/lookahead-lint) - AST-based static analyzer for quantitative code that agents run to flag lookahead bias, future target leakage (`.shift(-1)`), and premature scaler fitting.
- [eslazarev/purged-cross-validation](https://github.com/eslazarev/purged-cross-validation) - Scikit-learn-compatible package implementing López de Prado's Purged K-Fold and Combinatorial Purged Cross-Validation (CPCV) to eliminate time-series leakage.
- [LuxAlgo/PineTS](https://github.com/LuxAlgo/PineTS) - Open-source TypeScript transpiler and headless runtime for Pine Script v5/v6 with `AGENTS.md` and `pinets-cli` tool support for local strategy simulation and backtesting.
- [marketcalls/vectorbt-backtesting-skills](https://github.com/marketcalls/vectorbt-backtesting-skills) - Modular suite of agentic coding skills scaffolding VectorBT strategy development, hyperparameter tuning, and tearsheet evaluation.
- [ml4t/skills](https://github.com/ml4t/skills) - Machine Learning for Algorithmic Trading skills enforcing leakage-safe feature engineering, purged cross-validation boundaries, and rigorous backtest auditing.
- [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) - Production Rust-native algorithmic trading engine with deterministic event-driven backtesting and in-repo `AGENTS.md` and `CLAUDE.md` operational rules.
- [PyneSys/pynecore](https://github.com/PyneSys/pynecore) - Pine Script-compatible Python runtime and AST transpiler running TradingView indicators and strategies in native Python for offline backtesting and bar-by-bar verification.
- [QuantConnect/Lean](https://github.com/QuantConnect/Lean) - Institutional-grade algorithmic trading and backtesting engine (Python/C#) supporting multi-asset modeling, tick-level granularity, and LEAN CLI agent synthesis.
- [quantskills/skill-backtesting-bias-avoidance](https://github.com/quantskills/skill-backtesting-bias-avoidance) - Dedicated `SKILL.md` auditing backtests for lookahead bias, survivorship bias, CSCV Probability of Backtest Overfitting (PBO), and Deflated Sharpe Ratio (DSR).
- [ranaroussi/quantstats](https://github.com/ranaroussi/quantstats) - Portfolio analytics library calculating Sharpe, Sortino, Calmar, and VaR to generate interactive HTML tearsheets for agent backtest evaluation.
- [saksham10arora-dotcom/quant-skills](https://github.com/saksham10arora-dotcom/quant-skills) - Specialized skills for backtest code review, lookahead bias audits, statistical test validation, and paper reproduction across Claude Code / OpenCode / Codex.
- [stefan-jansen/pyfolio-reloaded](https://github.com/stefan-jansen/pyfolio-reloaded) - Maintained pyfolio risk analytics framework generating tearsheets covering return attribution and Bayesian out-of-sample performance analysis.
- [stefan-jansen/zipline-reloaded](https://github.com/stefan-jansen/zipline-reloaded) - Maintained modern fork of Zipline backtesting engine delivering agent-ready Pipeline APIs for cross-sectional factor simulations.

### 5. Execution & Order Routing
*Order execution algorithms (TWAP/VWAP), slippage management, and broker integration.*
- [anbotolabs/anboto-agent-kit](https://github.com/anbotolabs/anboto-agent-kit) - Institutional execution desk toolkit and MCP (`@anboto/mcp`) with native Claude Skill (`anboto-trading`) deploying TWAP, VWAP, POV, and Iceberg algorithms across 14 venues.
- [SMU-Rainflow/ctp-mcp](https://github.com/SMU-Rainflow/ctp-mcp) - MCP server built on `vnpy_ctp` exposing CTP tick streaming, limit/market order placement, and cancellation to coding agents.
- [Synpath-ai/synpath](https://github.com/Synpath-ai/synpath) - Python/Rust smart order routing (SOR) and advanced execution algorithms (TWAP, iceberg, pegged orders) for prediction and financial venues.
- [TradeRouter/trade-router-mcp](https://github.com/TradeRouter/trade-router-mcp) - Algorithmic execution MCP server exposing TWAP slicing, DCA, and multi-DEX routing with MEV protection.

---

## 🔌 Quant MCP Servers

*Standardized Model Context Protocol servers providing raw computational and data APIs to quant agents.*

### Market Feeds & Fundamentals
- [Alex2Yang97/yahoo-finance-mcp](https://github.com/Alex2Yang97/yahoo-finance-mcp) - Production-ready Yahoo Finance MCP server exposing historical OHLCV candles, option chains, fundamental ratios, and corporate actions.
- [bidouilles/mcp-tradingview-server](https://github.com/bidouilles/mcp-tradingview-server) - FastMCP server providing direct tool access to TradingView technical indicators (RSI, MACD, EMAs) and OHLCV candlestick feeds.
- [doggybee/mcp-server-ccxt](https://github.com/doggybee/mcp-server-ccxt) - Model Context Protocol server exposing unified CCXT trading and market data tools across 20+ cryptocurrency exchanges.
- [eliasfire617/crypto-market-data-mcp](https://github.com/eliasfire617/crypto-market-data-mcp) - CCXT market data MCP server across 100+ exchanges with open interest and perpetual funding rate comparison tools.
- [financial-datasets/mcp-server](https://github.com/financial-datasets/mcp-server) - Dedicated MCP server providing structured 10-K/10-Q financial statements and prices tailored for LLM tool consumption.
- [lazy-dinosaur/ccxt-mcp](https://github.com/lazy-dinosaur/ccxt-mcp) - Standardized Model Context Protocol server bridging CCXT across 100+ cryptocurrency exchanges with post-trade quantitative heuristics.
- [openbq-org/OpenBB](https://github.com/openbq-org/OpenBB) - Core OpenBB platform featuring `openbb-mcp-server`, exposing 100+ multi-asset financial data providers as standardized MCP tools with bundled `SKILL.md` guides.

### Broker & Exchange Gateways
- [alpacahq/alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server) - Official Alpaca MCP server exposing market data and live/paper trading tools for equities, ETFs, crypto, and options.
- [AnalyticAce/binance-mcp-server](https://github.com/AnalyticAce/binance-mcp-server) - Production MCP server exposing Binance spot and futures APIs with order book analysis and position tracking.
- [rcontesti/IB_MCP](https://github.com/rcontesti/IB_MCP) - Model Context Protocol server interfacing with Interactive Brokers' official Web API to monitor liquidity and submit institutional-grade orders.
- [visusnet/coinbase-mcp-server](https://github.com/visusnet/coinbase-mcp-server) - MCP server and native Claude Skill (`coinbase-trading`) integrating Coinbase Advanced Trading API for autonomous trade execution.

---

## 🏗️ Skill-Native Quant Frameworks

*Autonomous multi-agent quantitative platforms designed around composable skills.*
- [AI4Finance-Foundation/FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) - Open-source multi-agent platform orchestrating specialized roles (Market Analyst, 10-K Financial Analyst, Quantitative Trader, Risk Manager) for equity research.
- [microsoft/RD-Agent](https://github.com/microsoft/RD-Agent) - Autonomous R&D multi-agent framework by Microsoft Research automating hypothesis generation, factor implementation, and backtesting against Microsoft Qlib.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) - Institutional trading desk multi-agent framework built with LangGraph where specialized LLM roles collaborate in structured debate and risk cycles.
- [tohnee/investagent](https://github.com/tohnee/investagent) - Multi-agent investment research framework combining industry chain analysis, Buffett valuation filters, and QuantDinger backtesting.
- [yiyan-yixing/quant-trading-skills](https://github.com/yiyan-yixing/quant-trading-skills) - 11-role collaborative quant agent framework featuring 20 core skills, 3-tier memory, and adversarial challenge protocols.

---

## 🧪 Miscellaneous & Other Skills

*A staging ground for emerging, experimental, or cross-cutting skills that do not fit neatly into the categories above. When 3+ related skills accumulate here, they will graduate into their own dedicated category.*

- [BoyceFong/quant-skill-build](https://github.com/BoyceFong/quant-skill-build) - Skill authoring and scaffolding builder optimized for Codex and quantitative prompt authoring.

---

## 🤝 Contributing

We welcome community contributions! Please review our quality gates before submitting a Pull Request:

1. **Agent-Centric**: Must be directly invocable by an LLM Agent via `SKILL.md`, CLI prompt, or MCP tool.
2. **Methodological Rigor**: Backtesting and factor skills must adhere to sound quantitative principles (e.g., lookahead bias prevention, post-split price adjustments `close * adj_factor`).
3. **No Hallucinated Tooling**: Scripts and endpoints referenced in the skill must be verifiable and reproducible.

See [CONTRIBUTING.md](CONTRIBUTING.md) for submission details.

---

## ⚠️ Disclaimer

This project is for research and educational purposes only. Nothing here constitutes investment advice, an offer, or a solicitation to buy or sell any security or derivative.

Many skills and MCP servers listed here can route real orders (CTP, QMT, Alpaca, IB, Hyperliquid, Jupiter, Coinbase, etc.). Default to paper trading and human approval:

- Read-only first, then `propose-never-execute` where supported.
- Never put live API keys or secrets in agent prompts or committed `config.json`.
- Market data, filings, and social sentiment are untrusted inputs. Do not wire them directly to auto-execution.

You are solely responsible for compliance, risk control, and any losses.

---

## 📄 License

This repository's own curation (`README.md`, `data/`, `.github/`, `CONTRIBUTING.md`) is released under the [MIT License](LICENSE).

Skills under [`skills/`](skills/) are mirrored from upstream projects and **retain their original licenses** (see [NOTICE.md](NOTICE.md) and the `Imported from` header in each `SKILL.md`). Some mirrored skills are GPL-3.0 family — redistribution of those files follows their upstream terms, not MIT.
