# Small caps, penny stocks, pre-revenue, OTC, IPOs and SPACs

Use alongside the sector file when market cap is under about $2B, the stock
trades under $5 or over the counter, the company has little or no revenue,
it listed recently, or Reddit hype is driving it. The main risks here are
running out of money, dilution, and manipulation, so check those first.

## Survival and dilution

| Check | How | Read |
|---|---|---|
| Cash runway | (Cash + short-term investments) / quarterly operating cash burn | Under ~12 months means a raise is likely soon |
| Share count trend | Snapshot diluted shares, quarter by quarter | Rapid growth = ongoing dilution |
| Financing filings | Profile: S-1, S-3 (shelf), 424B5 (offering), 8-K | An active shelf or ATM means stock can be sold into any rally |
| Warrants and convertibles | 10-Q equity and debt notes | Convertibles with variable conversion prices ("toxic") create constant selling pressure |
| Reverse splits | Snapshot split history (ratios below 1) | Repeated reverse splits usually follow sustained dilution |
| Going-concern warning | 10-K/10-Q (`market.py doc <url> --grep "going concern"`) | Auditor or management doubt about surviving 12 months |
| Listing compliance | 8-K item 3.01 | Nasdaq/NYSE deficiency notices (e.g. under $1 bid for 30 days) |
| Auditor | 10-K | Small or recently changed auditors deserve attention |

## Trading and manipulation signals

- Float and short interest (% of float, days to cover, borrow fee) from web
  sources; low float plus high short interest drives squeezes both ways.
- Volume spikes without filings or news behind them.
- Paid promotions, newsletter pumps, sudden social-media volume, press
  releases heavy on partnerships with no disclosed financial terms.
- Reverse mergers, frequent name or business-model changes, related-party
  transactions (10-K related party note).
- OTC tier (OTCQX, OTCQB, Pink) and whether the company files with the SEC
  at all.

## Recent IPOs and SPACs

Lock-up expiry dates (insider selling), SPAC redemption rate at the merger,
sponsor promote and warrants, projections made during the deal vs actuals.

## Valuation

Market cap vs cash (EV near or below zero means the market doubts the cash
will last or be used well), EV/Sales for early revenue, milestone-based
(value only if a specific event happens). Present outcomes as binary where
they are.

## Reddit angle

Compare the Reddit mention trend (mentions digest, "Mentions by day") with
filings and news: a mention spike with no fundamental news is a hype
signal. Report it as such, alongside the survival and dilution checks.
