# Financials

Benchmarks: XLF (sector), KBE (banks), KRE (regional banks), KIE
(insurance). For banks and insurers, **EV, EBITDA, free cash flow and
current ratio don't apply**: deposits, float and loan flows are the
business. Value them on book value and returns.

XBRL tag names vary by filer; find them with `market.py tags <T> --grep <word>`.
Present for JPM (checked 2026-09-26): `InterestIncomeExpenseNet`,
`NoninterestIncome`, `NoninterestExpense`, `ProvisionForLoanLeaseAndOtherLosses`,
`Deposits`. Loan totals are usually under `FinancingReceivable...` tags or
only in the earnings release and supplement; ratios (NIM, CET1, efficiency,
charge-offs) come from the release.

## Banks

| Metric | Formula / where | Read |
|---|---|---|
| Net interest income (NII) and growth | XBRL, release | Core revenue |
| Net interest margin (NIM) | NII / average earning assets (release) | Direction matters: rate cuts and deposit costs move it |
| Deposit growth and cost | Release | Deposit beta = how much of rate moves passes to depositors |
| Noninterest-bearing deposits share | Release | Cheap funding; falling share raises costs |
| Loan growth and mix | Release, 10-Q | Commercial real estate (especially office) exposure is a watch item |
| Efficiency ratio | Noninterest expense / revenue | Lower is better; under ~55–60% is good for many banks |
| Provision for credit losses | XBRL | Rising provisions lead charge-offs |
| Net charge-offs (% of loans) | Release | Realized losses |
| Nonperforming assets / loans | Release | Early credit stress |
| Allowance / loans | Release | Reserve cushion |
| CET1 ratio | Release | Capital vs regulatory minimum plus buffers; drives buyback capacity |
| ROA, ROE, ROTCE | Snapshot / release | ROA ~1%+ and ROTCE mid-teens+ are strong |
| Tangible book value per share | (Equity − goodwill − intangibles) / shares | Growth over time is the value creation |
| Unrealized securities losses (AOCI, HTM) | 10-Q securities note | Hidden capital hits if assets must be sold |
| Uninsured deposits % | 10-K/10-Q | Run risk (2023 regional bank failures) |
| Loan-to-deposit ratio | Loans / deposits | Liquidity |

Valuation: P/TBV vs ROTCE (higher sustainable ROTCE justifies a higher
P/TBV), P/E, dividend yield and buybacks (capital return).

## Insurance

**Property & casualty:**
- Combined ratio = loss ratio + expense ratio; under 100% means an
  underwriting profit.
- Prior-year reserve development (favorable or adverse): adverse
  development means past profits were overstated.
- Premium growth and pricing (rate increases), catastrophe losses vs
  budget, investment income and portfolio yield, book value per share growth.

**Life and annuities:** spread income, sales, lapse rates, capital ratios
(RBC), sensitivity to rates and credit, reinsurance deals, alternative-
asset exposure.

**Brokers:** organic revenue growth, margins, M&A.

Valuation: P/B vs ROE, P/E, dividend yield. Berkshire-style conglomerates:
sum of the parts (insurance float and investments plus operating businesses).

## Asset managers, brokers and exchanges

Asset managers: AUM, net flows (organic growth), fee rate, mix
(passive vs active vs alternatives), performance fees. Brokers: client
assets, net new assets, trading activity, net interest revenue on client
cash (rate sensitive). Exchanges: trading volumes, recurring data/index
revenue share. Valuation: P/E, EV/EBITDA for asset-light models.

## Payments and fintech

Total payment volume (TPV), take rate (revenue / TPV), transaction margin,
active accounts, cross-border share, credit losses where the company lends.
Valuation: P/E, EV/EBITDA, EV/Sales for high growth.

## Consumer finance and BDCs

Consumer lenders: loan growth, yield, net charge-offs, delinquencies (30+
days), funding cost. BDCs: NAV per share trend, net investment income vs
dividend (coverage), non-accruals (% of portfolio at cost and fair value),
leverage; valuation price / NAV.

## Sector drivers

Rate path and yield curve shape, credit cycle (unemployment, delinquencies),
regulation and capital rules, stress-test results, deposit flows,
catastrophe season for P&C.
