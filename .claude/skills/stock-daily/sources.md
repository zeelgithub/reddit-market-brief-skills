# stock-daily — what to fetch

Edit this file to change what `/stock-daily` covers. The skill reads it
fresh on every run; nothing here is cached anywhere else.

## Time window

- **News window:** since the previous US market close (4:00pm ET on the
  last trading day). On a Monday or after a holiday, that reaches back
  over the weekend/holiday.
- **Politician trades window:** filings *published* in the last 7 days.
  Anything published since the previous run day is tagged **NEW**.
  (Filings lag the actual trade by up to 45 days — "published" is when it
  became public, which is what makes it news.)

## Market news — what to cover

Cover all of these, every run. The news sections come from web search, so
discover what actually happened; this is a checklist, not a keyword list.

- Index moves and futures: S&P 500, Nasdaq, Dow, Russell 2000, VIX
- Macro and Fed: rates, yields, CPI/PCE/jobs data, Fed speakers, the day's
  economic calendar
- Earnings: who reported since the last close, who reports today
  (before open / after close), notable beats and misses
- Biggest movers: large pre-market/after-hours gainers and losers, and why
- Company-specific headlines: M&A, guidance changes, FDA decisions,
  lawsuits, analyst upgrades and downgrades
- Sector and commodity moves: oil, gold, crypto, and the sector leaders
  and laggards

## Preferred news outlets

Prefer these when searching, but don't limit to them — use whatever
reputable source actually has the story:

- Reuters, AP, CNBC, Bloomberg, MarketWatch, Wall Street Journal,
  Yahoo Finance, Barron's, Financial Times, Investopedia (for calendars)

## Politician trades — Capitol Trades

- **Site:** https://www.capitoltrades.com/trades
- **Trade types:** buys (`txType=buy`). Also summarize sells in a short
  separate list, because a sell by the same politician can matter.
- **Chambers/parties:** all (House + Senate, every party)
- **Asset types:** all. Call out stock trades with a ticker first; list
  bonds, T-bills, municipal and private funds separately and briefly.

## My tickers (optional)

Tickers I always want mentioned if they show up anywhere in the news or
the Capitol Trades filings. This is **not** a filter: the report still
covers everything else. Leave it empty if you don't want it.

-
