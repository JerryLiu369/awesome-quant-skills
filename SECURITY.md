# Security Policy

This directory lists tools that can **move real money** (CTP, QMT, Alpaca,
Interactive Brokers, Hyperliquid, Jupiter, Coinbase, Binance) next to tools
that consume **untrusted input** (market feeds, SEC/CnInfo filings, Xueqiu and
StockTwits sentiment, LLM-generated formulas). That combination is a
prompt-injection-to-trade risk. These defaults exist to keep that from
happening.

## Safe defaults

1. **Paper first.** Exercise any new execution skill or MCP server against a
   SimNow / paper / testnet account before touching a live account.
2. **Humans approve orders.** Prefer `propose-never-execute` boundaries (see
   `hexonal/vnpy_agentbridge` for the reference pattern) and require explicit
   approval for every live order, especially TWAP/VWAP/iceberg slices that
   execute over time.
3. **Keys never enter prompts.** API keys and secrets go in environment
   variables or your MCP host's secret store — never in agent prompts,
   `SKILL.md` files, committed `config.json`, screenshots, or logs. The
   mirrored `quant-buddy` skill's `config.json` pattern is an upstream
   convention; do not commit a populated copy here.
4. **Untrusted input never auto-trades.** Filings, prices, sentiment scores,
   and news must not trigger orders without a human decision step in between.
   Treat a surprising data value as a data problem first, not a signal.
5. **Least privilege per server.** Run market-data servers and order-routing
   servers with separate credentials; give trading keys the narrowest scope
   the venue allows (e.g. no withdrawals), and use IP allowlists where
   supported.

## Scope notes

- Skills under `skills/` are upstream mirrors (`NOTICE.md`); a vulnerability
  in skill logic should be reported **upstream first**, then mirrored here.
- README directory entries are links, not vendored code — this repo cannot
  patch them, only delist them. A compromised or abandoned upstream gets
  removed from the list.

## Reporting a vulnerability

Please **do not** open a public issue with exploit details or live
credentials. Use GitHub's **private vulnerability reporting** on this
repository (Security tab → Report a vulnerability). Include: affected
skill/server and version or commit, what an attacker can make the agent do,
and minimal reproduction steps with paper/testnet accounts only.
