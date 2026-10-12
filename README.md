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
- [Meta-Tools & Scaffolding](#-meta-tools--scaffolding)
- [Contributing](#-contributing)

---

## 🌐 Vertical Market Stacks

*Full-lifecycle skills engineered for specific regional regulations, session rhythms, or market microstructure.*

### China A-Shares & Domestic Futures
- [algoderiv/agent-skills](https://github.com/algoderiv/agent-skills) - Claude Code skills for Chinese quantitative derivatives and CTP 6.7.8 API integration (`skills/ctp-api/SKILL.md`), order execution, and position management alongside TqSdk.
- [itsadrianxv/quant-strategy-builder-skill](https://github.com/itsadrianxv/quant-strategy-builder-skill) - Modular skill suite for Claude Code, Codex, and OpenClaw supporting domestic futures (`implement-cn-futures-strategy`) and A-share/ETF execution constraints (`implement-cn-equity-etf-strategy`).
- [jwangkun/claude-for-financial-services-cn](https://github.com/jwangkun/claude-for-financial-services-cn) - Comprehensive collection of 63 Claude Skills adapted for Chinese financial institutions alongside bundled MCP servers (`akshare-mcp`, `ifind-mcp`, `wind-mcp`).
- [lzwme/finance-quant-skills](https://github.com/lzwme/finance-quant-skills) - Agent skills tailored for A-share quantitative trading, market analysis, and rule checking.
- [quantskills/agent-ssquant](https://github.com/quantskills/agent-ssquant) - Futures quantitative agent workflow with Anthropic-compatible `skills/ssquant/SKILL.md` to gate CTP/SimNow runtime execution.
- [shinnytech/tqsdk-python](https://github.com/shinnytech/tqsdk-python) - Official Tianqin Quant SDK featuring an embedded agent skill (`tqsdk-trading-and-data/SKILL.md`) for CTP futures/options event loops and margin execution.

### Crypto & Web3 Markets
- [brandononchain/opentrade](https://github.com/brandononchain/opentrade) - Agent skills supporting 24/7 crypto microstructure, Pine Script v6 strategy synthesis, and high-frequency trading heuristics.
- [DefiLlama/defillama-skills](https://github.com/DefiLlama/defillama-skills) - Official agent skills (`yield-strategies`, `defi-data`, `flows-and-events`) connecting agents to DefiLlama for protocol TVL, DEX volumes, yields, and token unlocks.
- [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) - Multi-asset trading agent framework with native `SKILL.md` packaging and `perp-funding-basis` skills for perpetual funding rate cash-and-carry basis arbitrage.
- [mirror29/openfinclaw-cli](https://github.com/mirror29/openfinclaw-cli) - Plug-and-play crypto research, backtest, and paper-trade skill integrations for multi-agent environments.
- [vooi-app/mcp](https://github.com/vooi-app/mcp) - Unified perpetual futures MCP server connecting AI agents to Hyperliquid, Lighter, Aster, and Kinetiq for cross-venue funding rate spread arbitrage.

### US & Global Equities
- [LLMQuant/skills](https://github.com/LLMQuant/skills) - Standardized repository of 18 modular agent skills (`llmquant-equities`, `llmquant-macro`, `llmquant-risk`) compatible with Claude Code, Codex, and Hermes Agent.
- [pseudo-longinus/quant-buddy-skills](https://github.com/pseudo-longinus/quant-buddy-skills) - Full infrastructure skills covering US/HK equities, macro indicators, and multi-asset screening for LLM agents.
- [zen-tradings/retail-skills-us](https://github.com/zen-tradings/retail-skills-us) - Skills tailored for US equity rule enforcement, tax-loss harvesting, and retail algorithmic setups.

---

## ⚙️ Universal Quant Pipeline

*Modular skills aligned with each chronological stage of the quantitative investment lifecycle.*

### 1. Data Ingestion & Market Feeds
*Retrieval, cleaning, split-adjustment, and cross-source alignment.*
- [dgunning/edgartools](https://github.com/dgunning/edgartools) - SEC EDGAR toolkit providing a native MCP server (`edgartools-mcp`) and Claude Code skills for extracting 10-K, 10-Q, 8-K, and Form 4 insider filings into typed data.
- [elsejj/mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock) - Dedicated A-share MCP server providing tiered endpoints for quotes, financial fundamentals, and technical indicators backed by the `msd` database.
- [guangxiangdebizi/FinanceMCP](https://github.com/guangxiangdebizi/FinanceMCP) - Multi-market financial MCP server providing 19 tools integrating Tushare Pro for quotes, financial statements, and macro indicators.
- [hypier/tradingview-quantitative-skills](https://github.com/hypier/tradingview-quantitative-skills) - Technical pattern recognition, market scanning, and TradingView feed integration skills.
- [quantskills/quantskills](https://github.com/quantskills/quantskills) - Panoramic ecosystem navigation and standard data retrieval workflows for financial agents.
- [raidery/quant-skills](https://github.com/raidery/quant-skills) - Quant skill pack featuring `wencai/SKILL.md` for natural-language stock screening via `pywencai`.
- [zwldarren/akshare-one-mcp](https://github.com/zwldarren/akshare-one-mcp) - FastMCP server built on `akshare-one` exposing Chinese equity quotes, K-lines, and financials with multi-source fallback.

### 2. Alpha Generation & Factor Mining
*Hypothesis testing, formulaic alpha derivation, and research document processing.*
- [Abel-ai-lab/predict-anything](https://github.com/Abel-ai-lab/predict-anything) - Causal market analysis, alpha discovery, and predictive market structure extraction skills.
- [CTAAgents/quant-skills](https://github.com/CTAAgents/quant-skills) - AI-driven Commodity Trading Advisor (CTA) skills leveraging genetic programming for factor discovery.
- [Howard-Jerry/quant-agent-skills](https://github.com/Howard-Jerry/quant-agent-skills) - 8,000-line orchestration skill for concept thematic analysis, industry supply chain mapping, and factor screening.
- [minihellboy/factorminer](https://github.com/minihellboy/factorminer) - Quantitative alpha discovery engine with LLM-guided symbolic search, typed DSL execution, and native MCP server support.
- [quantskills/skill-factor-mining-pandaai](https://github.com/quantskills/skill-factor-mining-pandaai) - Academic paper factor extraction and structured financial analysis skills.
- [VernonOY/replicalpha](https://github.com/VernonOY/replicalpha) - Quant research reproduction agent extracting factors from research PDFs into executable Python code with Red Team validation.

### 3. Portfolio & Risk Allocation
*Capital allocation, position sizing, risk parity, and dynamic rebalancing.*
- [agiprolabs/claude-trading-skills](https://github.com/agiprolabs/claude-trading-skills) - 68 trading skills featuring Kelly criterion position sizing, regime detection, and slippage modeling.
- [ElmatadorZ/Money-Atlas-Intelligence-OS](https://github.com/ElmatadorZ/Money-Atlas-Intelligence-OS) - Smart Money Concepts (SMC) market structure and asset allocation guidance skill.
- [jackson-video-resources/markov-hedge-fund-method](https://github.com/jackson-video-resources/markov-hedge-fund-method) - Markov regime detection skill for dynamic portfolio risk-on/risk-off regime switching.
- [mitchellbernstein/openquant](https://github.com/mitchellbernstein/openquant) - Open-source quant operating system providing an MCP server and Hermes/Claude Agent Skills for VaR risk assessment and signal generation.

### 4. Backtesting & Safety Auditing
*Simulation, lookahead bias prevention, data-leakage auditing, and return attribution.*
- [bmouler/lookahead-lint](https://github.com/bmouler/lookahead-lint) - AST-based static analyzer for quantitative code that agents run to flag lookahead bias, future target leakage (`.shift(-1)`), and premature scaler fitting.
- [ml4t/skills](https://github.com/ml4t/skills) - Machine Learning for Algorithmic Trading skills enforcing leakage-safe feature engineering, purged cross-validation boundaries, and rigorous backtest auditing.
- [quantskills/skill-backtesting-bias-avoidance](https://github.com/quantskills/skill-backtesting-bias-avoidance) - Dedicated `SKILL.md` auditing backtests for lookahead bias, survivorship bias, CSCV Probability of Backtest Overfitting (PBO), and Deflated Sharpe Ratio (DSR).
- [saksham10arora-dotcom/quant-skills](https://github.com/saksham10arora-dotcom/quant-skills) - Specialized skills for backtest code review, lookahead bias audits, statistical test validation, and paper reproduction across Claude Code / OpenCode / Codex.

### 5. Execution & Order Routing
*Order execution algorithms (TWAP/VWAP), slippage management, and broker integration.*
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

### Broker & Exchange Gateways
- [alpacahq/alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server) - Official Alpaca MCP server exposing market data and live/paper trading tools for equities, ETFs, crypto, and options.
- [rcontesti/IB_MCP](https://github.com/rcontesti/IB_MCP) - Model Context Protocol server interfacing with Interactive Brokers' official Web API to monitor liquidity and submit institutional-grade orders.

---

## 🏗️ Skill-Native Quant Frameworks

*Autonomous multi-agent quantitative platforms designed around composable skills.*
- [AI4Finance-Foundation/FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) - Open-source multi-agent platform orchestrating specialized roles (Market Analyst, 10-K Financial Analyst, Quantitative Trader, Risk Manager) for equity research.
- [microsoft/RD-Agent](https://github.com/microsoft/RD-Agent) - Autonomous R&D multi-agent framework by Microsoft Research automating hypothesis generation, factor implementation, and backtesting against Microsoft Qlib.
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) - Institutional trading desk multi-agent framework built with LangGraph where specialized LLM roles collaborate in structured debate and risk cycles.
- [tohnee/investagent](https://github.com/tohnee/investagent) - Multi-agent investment research framework combining industry chain analysis, Buffett valuation filters, and QuantDinger backtesting.
- [yiyan-yixing/quant-trading-skills](https://github.com/yiyan-yixing/quant-trading-skills) - 11-role collaborative quant agent framework featuring 20 core skills, 3-tier memory, and adversarial challenge protocols.

---

## 🛠️ Meta-Tools & Scaffolding

*Skills and utilities that assist quants in strategy scaffolding, syntax translation, and validation.*
- [BoyceFong/quant-skill-build](https://github.com/BoyceFong/quant-skill-build) - Skill authoring and scaffolding builder optimized for Codex and quantitative prompt authoring.
- [LuxAlgo/PineTS](https://github.com/LuxAlgo/PineTS) - Open-source TypeScript transpiler and headless runtime for Pine Script v5/v6 with `AGENTS.md` and `pinets-cli` tool support.
- [marketcalls/vectorbt-backtesting-skills](https://github.com/marketcalls/vectorbt-backtesting-skills) - Modular suite of agentic coding skills scaffolding VectorBT strategy development, hyperparameter tuning, and tearsheet evaluation.
- [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) - Collection of 70+ domain-specific trading skills for AI coding agents covering market breadth, technical screening, and trade journaling.
- [TradersPost/pinescript-agents](https://github.com/TradersPost/pinescript-agents) - Claude Code skills (`pine-developer`, `pine-debugger`, `pine-backtester`) engineered to generate and debug TradingView Pine Script v6 strategies.

---

## 🤝 Contributing

We welcome community contributions! Please review our quality gates before submitting a Pull Request:

1. **Agent-Centric**: Must be directly invocable by an LLM Agent via `SKILL.md`, CLI prompt, or MCP tool.
2. **Methodological Rigor**: Backtesting and factor skills must adhere to sound quantitative principles (e.g., lookahead bias prevention, post-split price adjustments `close * adj_factor`).
3. **No Hallucinated Tooling**: Scripts and endpoints referenced in the skill must be verifiable and reproducible.

See [CONTRIBUTING.md](CONTRIBUTING.md) for submission details.

---

## 📄 License

This repository is released under the [MIT License](LICENSE).
