# Core methods (every stock)

The sector file says which of these matter most and adds sector-specific
metrics. Judge every number against three references: the company's own
history, its closest peers, and the sector norm. A number alone says little.

## 1. The business

- What it sells, to whom, and which segment drives profit (10-K segment
  note, not revenue share alone).
- Competitive position: market share, pricing power (gross margin trend),
  switching costs, scale, regulation.
- Customer or product concentration (10-K: customers >10% of revenue).

## 2. Growth

| Metric | How | Read |
|---|---|---|
| Revenue growth | YoY for each quarter, and 3–5 year CAGR | Accelerating or decelerating matters more than the level |
| Organic growth | Excluding acquisitions and FX (from the release) | Separates real demand from M&A |
| EPS growth | Diluted EPS YoY | Check it's not driven only by buybacks or one-offs |
| Guidance | Company outlook vs consensus and vs its last guide | Raised / maintained / cut, and the stock's reaction |

## 3. Profitability

| Metric | Formula | Read |
|---|---|---|
| Gross margin | Gross profit / revenue | Pricing power and cost position; trend matters most |
| Operating margin | Operating income / revenue | Operating leverage: does margin rise with revenue? |
| Net margin | Net income / revenue | Distorted by one-offs; check non-operating gains |
| ROE | Net income / equity | Inflated by leverage and buybacks (tiny or negative equity) |
| ROIC | NOPAT / (debt + equity − cash) | Above the cost of capital (~8–10%) means growth creates value |

## 4. Cash flow and earnings quality

| Metric | Formula | Read |
|---|---|---|
| Free cash flow | Operating cash flow − capex | What's actually available to owners |
| FCF conversion | FCF / net income | Persistently under ~80% needs an explanation (working capital, capex) |
| SBC-adjusted FCF | FCF − stock-based compensation | SBC is a real cost paid in shares; matters most in tech |
| Accruals check | Net income vs operating cash flow | Profits without cash is a warning |
| Working capital | Receivables and inventory growth vs revenue growth | Growing faster than sales can mean channel stuffing or weak demand |
| Non-GAAP gap | Adjusted EPS vs GAAP EPS | A wide, persistent gap ("recurring one-offs") is a red flag |

## 5. Balance sheet and risk

| Metric | Formula | Read |
|---|---|---|
| Net debt / EBITDA | (Debt − cash) / EBITDA | Rough comfort under ~2–3x for most industrials; sector files give norms |
| Interest coverage | Operating income / interest expense | Under ~3x is tight |
| Current ratio | Current assets / current liabilities | Under 1 needs a reason (some models run negative working capital) |
| Debt maturities | 10-K debt note | Large near-term maturities in a high-rate market are a risk |
| Share count | Diluted shares, YoY change | Rising = dilution; falling = buybacks |

Credit ratings and outlooks (S&P, Moody's) are worth a web search for
leveraged companies.

## 6. Capital allocation

Buybacks (at what prices), dividends (payout ratio on FCF, not just EPS),
M&A track record (goodwill impairments later mean overpaying), capex
returns, insider ownership.

## 7. Valuation

Use at least two methods and compare to peers and the company's 5-year range.

| Method | When | Notes |
|---|---|---|
| P/E (TTM and forward) | Profitable, stable earnings | Misleading at cyclical peaks (low P/E at peak earnings) and with one-off gains |
| PEG | Growth companies | P/E ÷ expected EPS growth (%); ~1 is "fair" by convention, a rough screen only |
| EV/EBITDA | Capital-intensive or leveraged businesses; cross-capital-structure comparisons | EBITDA ignores capex; pair with FCF |
| EV/Sales | Unprofitable or early high-growth | Only comparable at similar gross margins |
| P/FCF, FCF yield | Cash-generative businesses | FCF yield vs the 10-year Treasury yield is a useful anchor |
| P/B, P/TBV | Banks, insurers, asset-heavy | Justified P/B rises with ROE |
| Dividend yield, DDM | Utilities, staples, REITs, telecom | Check dividend coverage first |
| Sum of the parts | Conglomerates, multi-segment | Value each segment on its sector's multiple |
| NAV | REITs, miners, E&Ps, BDCs | Price vs net asset value |

### Reverse DCF (what the price assumes)

Solve for the growth the current price implies, instead of guessing growth:
1. Start with TTM FCF per share (or normalized FCF for cyclicals).
2. Discount rate: cost of equity ≈ 10-year Treasury yield (look it up) +
   beta × equity risk premium (~4–5%). State the rate used.
3. Terminal growth 2–3% after 10 years.
4. Find the 10-year FCF growth rate that makes the present value equal the
   price. Then ask whether that growth is plausible given history, market
   size and the sector.

Do it with a short Python calculation and show the inputs. A forward DCF is
the same arithmetic with growth assumed; present it only as a scenario.

## 8. Price action and technicals

From the snapshot: returns vs SPY and the sector ETF (relative strength),
50/200-day moving averages (trend), RSI (above 70 conventionally
overbought, below 30 oversold), distance from the 52-week high/low,
drawdowns, volatility and beta, volume vs average. Note support and
resistance only where there's an obvious prior level. Technicals describe
what the price has done; they don't explain why.

## 9. Sentiment and positioning

- Analysts: rating counts, average/low/high target and dispersion, recent
  upgrades/downgrades and target changes (direction of revisions matters).
- Short interest (% of float, days to cover): high values can mean crowded
  bearish bets or squeeze risk.
- Insiders: open-market buys (Form 4, code P) carry more signal than sales,
  which are often scheduled (10b5-1).
- Options: implied volatility vs history, put/call skew, expected earnings
  move (from web sources).
- Reddit: volume trend, sentiment split, the arguments, positions people
  report. Hype without fundamentals is a risk signal, not a thesis.

## 10. Scenarios (12 months)

For each of bull, base and bear:
1. Assumptions for next-12-month (or next fiscal year) revenue growth and
   margin → EPS or FCF per share.
2. A multiple justified for that scenario (peer range, own history).
3. Implied price = EPS × P/E (or FCF/share ÷ FCF yield, or EBITDA × EV/EBITDA
   − net debt, per share).
4. What would have to happen, and the signals to watch for each.

Base should sit near consensus estimates unless the evidence says otherwise.
Show the analyst target range next to the scenarios. Probability weights are
judgment; label them as such if used.

## Common traps

- TTM vs forward numbers mixed in one comparison.
- Fiscal years that don't match calendar years.
- One-off gains (investment gains, asset sales, tax benefits) inflating net
  income: check operating income and the non-operating line.
- Per-share history across splits (the snapshot adjusts EPS and share
  counts; per-share figures from other sources may not be).
- Multi-class shares and ADRs (ADR ratio, currency) in market cap.
- Cyclicals looking cheapest at peak earnings and most expensive at troughs.
- Survivorship in "it always comes back" arguments.
