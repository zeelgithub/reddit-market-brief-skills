# Energy

Benchmarks: XLE (sector), XOP (exploration & production), OIH (oilfield
services), AMLP (midstream MLPs). Earnings follow commodity prices, so
always state the oil (WTI, Brent) and natural gas (Henry Hub) prices for
the period, from a dated source.

## Exploration & production (upstream) and integrated majors

| Metric | Where | Read |
|---|---|---|
| Production (boe/d), oil vs gas mix | Release | Growth, and liquids mix (oil earns more per boe) |
| Realized prices vs benchmarks | Release | Differentials and hedging effects |
| Hedging | 10-Q derivatives note | Hedged volumes and prices limit upside and downside |
| Lifting / production cost per boe | Release, 10-K | Low-cost producers survive downturns |
| Breakeven oil price | Company disclosure or analyst estimate (web) | Price needed to fund capex and the base dividend |
| Proved reserves, reserve life (reserves / annual production) | 10-K supplementary oil and gas information | Replacement ratio over 100% keeps the business from shrinking |
| Standardized measure (PV-10-like) | Same 10-K section: `market.py doc <10-K url> --grep "standardized measure"`. Not in SEC's XBRL API for majors (checked COP 2026-09-26) | SEC-price-based value of proved reserves; compare with EV |
| Reinvestment rate | Capex / operating cash flow | Lower means more cash returned; very low can mean underinvestment |
| FCF and shareholder returns | Snapshot | Base + variable dividends and buybacks, often a stated % of FCF |
| Net debt / EBITDA(X) | Snapshot | Under ~1–1.5x comfortable for producers |

Integrated majors add downstream (refining, chemicals) and often LNG;
analyze segments separately (10-Q segment note).

## Midstream (pipelines, storage, processing)

Distributable cash flow (DCF) and coverage (DCF / distributions; ~1.2x+
comfortable), fee-based share of earnings (higher = less commodity risk),
contracted volumes and counterparties, leverage (net debt / EBITDA ~3.5–4.5x
typical), growth projects backlog. MLPs issue K-1 tax forms instead of
1099s. Valuation: EV/EBITDA, distribution/dividend yield, DCF yield.

## Refiners (downstream)

Crack spreads (e.g. the 3-2-1 crack), throughput and utilization, margin
capture vs benchmark crack, turnaround (maintenance) schedule, renewable
diesel economics, product inventories. Very cyclical. Valuation:
EV/EBITDA and P/E on mid-cycle cracks.

## Oilfield services

Rig count (Baker Hughes weekly), frac spread count, pricing, international
vs North America mix, backlog and book-to-bill (offshore), margins.
Valuation: EV/EBITDA, P/E.

## Valuation notes

- P/E looks lowest at commodity peaks; use mid-cycle prices for normalized
  earnings and show sensitivity (FCF at $60 / $75 / $90 oil, for example).
- EV/EBITDA(X), FCF yield, and EV vs PV-10/NAV are standard for producers.

## Drivers to check (web, dated)

OPEC+ decisions, EIA weekly inventories, global demand forecasts (IEA,
EIA), rig counts, geopolitical supply risk, natural gas storage and LNG
export capacity, the futures curve (strip).

## Red flags

Rising decline rates needing more capex to hold production, reserve
write-downs, dividends funded by debt, large hedging losses, shrinking
reserve life.
