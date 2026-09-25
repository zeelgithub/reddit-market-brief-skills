# reddit-daily — watchlist

Edit this file to change what `/reddit-daily` covers. The skill reads it
fresh on every run. Anything you say in chat ("just WSB today", "last 48
hours") overrides this file for that one run.

## Subreddits I always want covered

These are always included. The skill also adds other subreddits it finds
active on the same topics that day, and labels them "discovered".

The notes after each subreddit come from research on 2026-09-24:
activity is posts and comments in the last 24 hours, and "early" is how
fast it posted this week's market-moving stories.

### My pages

- r/wallstreetbets: the biggest retail stock discussion (about 20 posts
  and 17,000 comments a day, mostly in the Daily Discussion)
- r/stocks: serious stock discussion and company news (about 10 posts and
  700 comments a day)
- r/DailyStocks: note that it's effectively inactive (210 members; its
  latest 100 posts go back about 5 years). Kept because I asked for it.
  No other "daily stocks" subreddit is active either.
- r/pennystocks: small caps (about 13 posts and 400 comments a day)
- r/options: options trading (about 6 posts and 80 comments a day)
- r/optionstrading: options trading, smaller but busier with posts
  (about 11 posts a day)

### More stock discussion

- r/StockMarket: market news posts with heavy discussion; it had the Fed
  Kashkari inflation story the same day
- r/investing: long-term company and market discussion (about 500
  comments a day)
- r/ValueInvesting: company news plus "is it cheap now?" talk, e.g.
  Berkshire buying Lennar while it fell 40% (about 1,000 comments a day)
- r/stockstobuytoday: "beaten down for no reason / good entry now?"
  threads (about 22 posts and 290 comments a day)
- r/smallstreetbets: WSB-style plays for smaller accounts (about 260
  comments a day)
- r/thetagang: options selling (about 200 comments a day)

### Early and macro news that moves the market

- r/economy: about 60 news links a day (CNBC, CNN, Yahoo Finance); one of
  the first real communities to post the diesel and Kashkari stories
- r/Economics: news links only, with heavy discussion; had the 10-year
  yield and diesel stories within hours
- r/finance: few posts but fast; had the Buffett stepping-down news
  within about 10 minutes
- r/business: company news, e.g. downgrades and deals (about 7 posts and
  190 comments a day)
- r/bonds: Treasury yields, which are a main market driver right now
  (about 16 posts and 1,500 comments a day)
- r/unusual_whales: "BREAKING" headline posts (about 13 a day, 92% links)

### Catalysts and early signals

- r/biotech_stocks: FDA decisions and trial results that make biotech
  stocks spike or drop (about 12 posts a day)
- r/Pennystock: daily pre-market small-cap watchlists
- r/insiderData: insider buying and open-market purchases by company
  executives
- r/Optionmillionaires: "JUST IN" market headlines and options ideas
  (about 18 posts a day)

### Checked and left out

These stay out of the list unless I add them:

- Automated headline feeds (r/MarketFluxHub, r/NowInFinance, r/EverHint,
  r/AutoNewspaper): they post first, but there's no discussion and the
  sources are unknown. /stock-daily covers real news outlets.
- Trading-lifestyle subreddits (r/Daytrading, r/Trading,
  r/FuturesTrading): mostly strategy and psychology, little stock news.
- Meme and portfolio-flex subreddits (r/TheRaceTo10Million,
  r/TheRaceTo1Million): cross-posted spam was seen there.
- Single-stock subreddits (r/Superstonk, and others like it) and
  duplicates (r/Stocks_Picks mirrors r/stockstobuytoday).
- Congress-trade subreddits (r/tradewithcongress,
  r/QuiverQuantitative): /stock-daily already covers Capitol Trades.
- Inactive subreddits (r/StockMarketChat, r/stockbetz, r/EarningsWhisper,
  r/SqueezePlays, r/wallstreetbetsOGs, and others): no posts in days or
  months.

## Discovery topics

Used to find extra subreddits worth adding for that day's run. The skill
also picks up subreddits that are referenced in the day's fetched posts
and comments.

- stock market news
- stock catalysts
- premarket movers
- biotech FDA catalysts
- insider buying
- earnings
- options trading
- penny stocks

## Time window

- **Window:** last 24 hours, counted back from when the run starts.

## Comment depth

One of:

- `full`: every comment Reddit will return. This includes collapsed
  comments, which are fetched one by one, so it's slow on huge threads
  like the WSB Daily Discussion (see SKILL.md for timings).
- `sorts`: every post, plus comments pulled under 6 different sort orders
  (about 2,000 per huge thread; smaller threads are usually complete).
  Much faster.
- `none`: posts only, no comments.

**Comment depth:** sorts

(Chosen 2026-09-24 for speed: about 11 minutes for the 22 subreddits
above, versus about 2 hours for `full`. Every run's Coverage section says what `sorts` left out, mainly
the WSB Daily Discussion. Say "/reddit-daily full" for a one-off complete
run.)

## What I want in the brief

- What's going on today: the main themes, news and market mood per
  subreddit, and across all of them
- Stocks and companies being discussed: every ticker/company that
  actually shows up, with how much it's mentioned, whether people are
  bullish or bearish, and why
- Early news and catalysts: market-moving headlines, which subreddit had
  them first and when, and which stocks they hit
- Dips and run-ups: stocks people say dropped on news (and whether they
  call it a buying chance or a trap), and stocks that ran up (and whether
  people talk about taking profit). Report what people are saying, not
  advice
- Notable posts: DD (due diligence), big gain/loss posts, and breaking
  news posts
- Options activity people mention: strikes, expiries, calls vs puts
- Anything unusual: sudden hype on a small ticker, heavy disagreement,
  or new subreddits showing up in the discussion
