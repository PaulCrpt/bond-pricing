import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bond import Bond
from analytics import (macaulay_duration, modified_duration,
                        convexity, ytm_solver, pnl_scenarios)

# ── Paramètres de l'obligation ──────────────────────────────────────────
bond = Bond(
    face_value  = 1000,
    coupon_rate = 0.05,   # 5% coupon
    maturity    = 10,     # 10 ans
    frequency   = 2,      # semestriel
    ytm         = 0.04    # YTM 4%
)

# ── Résultats principaux ─────────────────────────────────────────────────
print("=" * 50)
print("        BOND PRICING & RISK METRICS")
print("=" * 50)
print(f"Prix théorique        : {bond.price():.4f} €")
print(f"Duration Macaulay     : {macaulay_duration(bond):.4f} ans")
print(f"Duration Modifiée     : {modified_duration(bond):.4f}")
print(f"Convexité             : {convexity(bond):.4f}")

# ── YTM Solver ───────────────────────────────────────────────────────────
market_price = 1050
ytm = ytm_solver(bond, market_price)
print(f"\nPrix de marché        : {market_price} €")
print(f"YTM implicite         : {ytm*100:.4f} %")

# ── Scénarios de chocs ───────────────────────────────────────────────────
print("\n── Scénarios de chocs de taux ──")
df = pd.DataFrame(pnl_scenarios(bond))
print(df.to_string(index=False))

# ── Graphique Price/Yield ─────────────────────────────────────────────────
yields = np.linspace(0.001, 0.15, 200)
prices = []
for y in yields:
    bond.ytm = y
    prices.append(bond.price())
bond.ytm = 0.04  # reset

plt.figure(figsize=(10, 5))
plt.plot(yields * 100, prices, color="steelblue", linewidth=2)
plt.axvline(x=4, color="red", linestyle="--", label="YTM initial (4%)")
plt.axhline(y=bond.price(), color="gray", linestyle="--", label=f"Prix ({bond.price():.2f}€)")
plt.title("Relation Prix / Yield")
plt.xlabel("Yield (%)")
plt.ylabel("Prix (€)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("price_yield_curve.png")
plt.show()
print("\nGraphique sauvegardé : price_yield_curve.png")
