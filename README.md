# reddit-market-brief-skills

Two Claude Code skills I use for a quick daily read on the market:

- **`/reddit-daily`**: what the stock subreddits are talking about today:
  tickers, sentiment, early news, catalysts, dips and run-ups.
- **`/stock-daily`**: market news since the last close, plus recent
  politician stock buys from [Capitol Trades](https://www.capitoltrades.com/trades).

Open Claude Code in this folder, type one of the commands, and the brief
shows up in the chat. The standing settings (which subreddits, which news
topics) live in files, so there's nothing to retype each day.

## Setup

1. Install the Python packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and add your Composio API key (from
   [dashboard.composio.dev](https://dashboard.composio.dev)).
3. Run `/reddit-daily` once. If Reddit isn't connected yet, Claude gives
   you a link to approve it in your browser.

`/stock-daily` doesn't need any of that. It uses web search plus the
Claude desktop app's built-in browser (Capitol Trades blocks plain
requests, so a real browser is needed).

## Changing what gets covered

| To change | Edit |
|---|---|
| Subreddits, time window, comment depth, what the brief includes | `.claude/skills/reddit-daily/watchlist.md` |
| News topics, preferred outlets, Capitol Trades filters, tickers to watch | `.claude/skills/stock-daily/sources.md` |

For a one-off change, just say it after the command, e.g.
`/reddit-daily just r/pennystocks, last 48 hours`. The files stay as they are.

## How it works

`reddit-daily` runs `scripts/collect.py`, which pulls every post from the
window across the watchlist, fetches the comments, and builds a digest.
Claude reads the digest and writes the brief. Raw data goes to your temp
folder, not the project, and is deleted after a week.

With the default `sorts` depth, a run over the 22 watchlist subreddits
takes about 11 minutes. Everything comes back essentially complete except
the WSB Daily Discussion thread, which is too big to expand in one pass.
`/reddit-daily full` gets it all but takes around 2 hours. Every brief ends
with a coverage section that says exactly what was missed.

## Layout

```
.claude/skills/
  reddit-daily/   SKILL.md, watchlist.md, scripts/collect.py
  stock-daily/    SKILL.md, sources.md
lib/reddit_session.py   Composio session helper (connection, tool calls, retries)
CLAUDE.md               project rules Claude follows
```

## Notes

- Reddit content is treated as untrusted text. Claude summarizes it but
  never follows instructions found in posts or comments.
- None of this is financial advice. It reports what people and news
  sources are saying.
