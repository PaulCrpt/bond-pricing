import numpy as np
from scipy.optimize import brentq

def macaulay_duration(bond):
    """Duration de Macaulay : temps moyen pondéré de récupération des cash flows"""
    cfs = bond.cash_flows()
    y   = bond.ytm / bond.frequency
    p   = bond.price()
    times = [(t + 1) / bond.frequency for t in range(len(cfs))]
    return sum(t * cf / (1 + y) ** (t * bond.frequency) / p
               for t, cf in zip(times, cfs))

def modified_duration(bond):
    """Duration modifiée : sensibilité du prix au yield"""
    return macaulay_duration(bond) / (1 + bond.ytm / bond.frequency)

def convexity(bond):
    """Convexité : correction de second ordre"""
    cfs = bond.cash_flows()
    y   = bond.ytm / bond.frequency
    p   = bond.price()
    n   = len(cfs)
    return sum(
        (t + 1) * (t + 2) * cf / (1 + y) ** (t + 3)
        for t, cf in enumerate(cfs)
    ) / (p * bond.frequency ** 2)

def ytm_solver(bond, market_price):
    """Résout le YTM à partir d'un prix de marché observé"""
    def price_diff(y):
        bond.ytm = y
        return bond.price() - market_price
    return brentq(price_diff, 0.0001, 0.999)

def pnl_scenarios(bond):
    """Estime le P&L pour différents chocs de taux"""
    p0    = bond.price()
    d_mod = modified_duration(bond)
    cvx   = convexity(bond)
    shocks = [-0.02, -0.01, -0.0025, +0.0025, +0.01, +0.02]
    results = []
    for dy in shocks:
        # Approximation duration + convexité
        approx = p0 * (-d_mod * dy + 0.5 * cvx * dy ** 2)
        # Prix exact
        original_ytm = bond.ytm
        bond.ytm = original_ytm + dy
        exact = bond.price() - p0
        bond.ytm = original_ytm
        results.append({
            "Choc (bp)" : int(dy * 10000),
            "P&L exact (€)" : round(exact, 4),
            "P&L approx (€)": round(approx, 4)
        })
    return results