# reddit-market-brief-skills

A daily market brief from Reddit, the news, and Congress trades, from one
command.

Market-moving talk is spread across dozens of subreddits and news sites,
and reading it yourself takes hours. This project reads it for you and
gives you a single summary of what people are talking about, what broke
early, and what politicians are buying.

It's built as three [Claude Code](https://claude.com/claude-code) skills.
A skill is a set of saved instructions Claude Code runs when you type its
command. Open Claude Code in this folder, type a command, and the brief
shows up in the chat.

## `/reddit-daily`

Reads the last 24 hours of posts and comments across 22 subreddits:

| Group | Subreddits |
|---|---|
| Core stock talk | r/wallstreetbets, r/stocks, r/DailyStocks, r/pennystocks, r/options, r/optionstrading |
| More discussion | r/StockMarket, r/investing, r/ValueInvesting, r/stockstobuytoday, r/smallstreetbets, r/thetagang |
| Early and macro news | r/economy, r/Economics, r/finance, r/business, r/bonds, r/unusual_whales |
| Catalysts and signals | r/biotech_stocks, r/Pennystock, r/insiderData, r/Optionmillionaires |

The brief covers early news and catalysts, dips and run-ups, the
most-discussed stocks with sentiment, and a per-subreddit rundown. There's
no fixed stock list: any ticker or company that comes up gets picked up.

A run takes about 11 minutes. Everything is read except part of WSB's
Daily Discussion thread; `/reddit-daily full` gets that too (about 2
hours). Each brief ends with what was and wasn't read.

## `/stock-daily`

- Market news since the last close: indices, the Fed, earnings and big
  movers, with sources.
- Stock buys by members of Congress published on
  [Capitol Trades](https://www.capitoltrades.com/trades) in the last 7 days.

## `/stock-analysis`

Ask about one stock or ETF ("analyze NVDA", "is SPY a good ETF", "what is
Reddit saying about GME") and get a full, sourced analysis:

- performance vs the S&P 500 and the stock's sector, and the price trend
- fundamentals scored with the metrics that fit its sector (software,
  chips, banks, REITs, oil, biotech, ETFs, penny stocks and more)
- valuation vs peers and its own history
- news, earnings and upcoming catalysts
- Wall Street ratings and price targets
- every Reddit post about it in the last 7 days, with full comment trees
- bull vs bear case and 12-month scenarios with the math shown

It reports the buy/sell calls analysts and Reddit users make, with their
reasons; it doesn't tell you what to do.

## How it works

- **`/reddit-daily`**: a Python script (`scripts/collect.py`) pulls the
  posts and comments through [Composio](https://composio.dev), a service
  that connects to your Reddit account. It stays within Reddit's rate
  limits and builds a digest, then Claude reads the digest and writes the
  brief.
- **`/stock-daily`**: Claude searches the web for the day's news and reads
  Capitol Trades in a browser.
- **`/stock-analysis`**: a Python script (`scripts/market.py`) pulls prices
  and analyst data from Google Finance and Yahoo, and reported financials
  from SEC filings. The Reddit script reads every post about the ticker.
  Claude picks the sector's method file (`references/sectors/`), searches
  the web for news, and writes the analysis.
- Your standing choices (subreddits, news topics, filters) live in two
  settings files, so you never retype them.

## Setup

You'll need the Claude desktop app (for Claude Code), Python 3, and a
Composio account.

1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and add your Composio API key from
   [dashboard.composio.dev](https://dashboard.composio.dev). For
   `/stock-analysis`, also set `SEC_USER_AGENT` to your name and email
   (`Jane Doe jane@example.com`); SEC requires a contact.
3. Run `/reddit-daily`. If Reddit isn't connected yet, you'll get a link
   to approve it.

`/stock-daily` needs none of this, but it does need the Claude desktop
app's built-in browser, because Capitol Trades blocks plain requests.

## Customizing

- Subreddits, time window, depth: `.claude/skills/reddit-daily/watchlist.md`
  (`/stock-analysis` uses the same subreddit list)
- Analysis methods per sector: `.claude/skills/stock-analysis/references/`
- News topics, trade filters: `.claude/skills/stock-daily/sources.md`

For a one-off change, add it after the command:
`/reddit-daily just r/pennystocks, last 48 hours`.

Not financial advice. It reports what people and news sources are saying.
