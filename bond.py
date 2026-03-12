import numpy as np

class Bond:
    def __init__(self, face_value, coupon_rate, maturity, frequency, ytm):
        """
        face_value  : valeur nominale (ex: 1000)
        coupon_rate : taux coupon annuel (ex: 0.05 pour 5%)
        maturity    : maturité en années (ex: 10)
        frequency   : fréquence des coupons par an (1=annuel, 2=semestriel)
        ytm         : yield to maturity (ex: 0.04 pour 4%)
        """
        self.face_value  = face_value
        self.coupon_rate = coupon_rate
        self.maturity    = maturity
        self.frequency   = frequency
        self.ytm         = ytm

    def cash_flows(self):
        """Génère la liste des cash flows de l'obligation"""
        n      = int(self.maturity * self.frequency)
        coupon = self.face_value * self.coupon_rate / self.frequency
        cfs    = [coupon] * n
        cfs[-1] += self.face_value  # remboursement du nominal à maturité
        return cfs

    def price(self):
        """Calcule le prix théorique par actualisation des cash flows"""
        cfs = self.cash_flows()
        y   = self.ytm / self.frequency
        return sum(cf / (1 + y) ** (t + 1) for t, cf in enumerate(cfs))