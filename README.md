# Bond Pricing & Risk Metrics

A Python tool to price fixed-income instruments and compute key risk metrics.

## Features
- Theoretical bond pricing via discounted cash flows
- Yield to Maturity (YTM) solver using numerical optimization
- Macaulay Duration, Modified Duration and Convexity
- P&L estimation under interest rate shock scenarios (-200bp to +200bp)
- Price/Yield curve visualization

## Tech Stack
Python · NumPy · SciPy · Matplotlib · Pandas

## Example Output
```
BOND PRICING & RISK METRICS
==================================================
Prix théorique        : 1081.7572 €
Duration Macaulay     : 8.0809 ans
Duration Modifiée     : 7.9225
Convexité             : 75.4725
```

## Rate Shock Scenarios
| Shock (bp) | Exact P&L (€) | Approx P&L (€) |
|-----------|--------------|----------------|
| -200 | +182.21 | +181.07 |
| -100 | +86.75 | +86.61 |
| +100 | -78.89 | -78.76 |
| +200 | -150.69 | -149.66 |

## Author
Paul Carpentier — Master's student in Finance, IESEG School of Management