# ETFs

An ETF's outlook is the outlook of what it holds, plus fund-specific
costs and risks. Get holdings and fund data from the issuer's fund page
(fact sheet, holdings file) via web search; the snapshot gives price,
performance, and Google's stats (no SEC fundamentals for ETFs).

## Fund facts

| Item | Where | Read |
|---|---|---|
| Index / strategy and methodology | Issuer page, prospectus | What exactly it owns and how it's weighted (cap, equal, factor, active) |
| Expense ratio | Issuer page (Google's profile sometimes quotes it) | Compare with ETFs tracking the same exposure |
| AUM and average volume | Issuer page, snapshot | Small, thin funds have wider spreads and closure risk |
| Bid-ask spread | Issuer page or quote | Trading cost |
| Premium / discount to NAV | Issuer page | Persistent gaps in illiquid or international funds |
| Tracking difference | Fund total return vs index return | Cost beyond the expense ratio |
| Holdings count, top-10 weight, sector and country weights | Holdings file | Concentration risk |
| Distribution yield, SEC 30-day yield, frequency | Issuer page | Income; for bond funds use SEC yield / yield to maturity |
| Capital gains distributions | Issuer page | Tax efficiency |

## Performance

From the snapshot: total returns vs SPY and vs its own benchmark or
category peers (1/3/5/10 years), volatility, max drawdown. Compare with the
cheapest fund offering the same exposure.

## Analysis of the underlying

- Weighted P/E, earnings growth and dividend yield of the holdings (issuer
  pages often publish these); compare with the S&P 500.
- The biggest holdings drive results: summarize their state (run
  `market.py quote` or `snapshot` on the top holdings when they dominate).
- Apply the sector file for sector ETFs (XLK → technology.md, XLE →
  energy.md, etc.).

## Structure-specific risks

- **Leveraged and inverse ETFs:** reset daily; over longer periods returns
  drift from 2x/3x of the index (volatility decay). Meant for short holding
  periods; say so plainly.
- **Options-income / covered-call ETFs:** high distributions but capped
  upside; part of the payout can be return of capital; compare total return,
  not yield.
- **Bond ETFs:** duration (rate sensitivity), credit quality, yield to
  maturity, average maturity.
- **Commodity ETFs:** usually hold futures; roll costs (contango) cause
  drift from spot; some issue K-1 tax forms.
- **Single-stock and crypto ETFs:** fees, structure (spot vs futures),
  concentration.
- **Thematic ETFs:** concentration, high fees, and hype-driven launches near
  tops.
- **Currency-hedged vs unhedged** international funds.

## Scenarios

Bull/base/bear for the ETF = scenarios for its holdings' earnings and
multiple (weighted), or for rates and credit spreads for bond funds, minus
fees.
