"""4-loop MS-bar alpha_s and quark-mass running with flavour thresholds (own implementation).

a = alpha_s/pi ;  da/dlnmu^2 = -sum_i beta_i a^(i+2) ;  dlnm/dlnmu^2 = -sum_i gamma_i a^(i+1)
beta: van Ritbergen-Vermaseren-Larin 1997; gamma: Vermaseren-Larin-van Ritbergen 1997, Chetyrkin 1997.
Thresholds at mu = m_h(m_h), 2-loop decoupling constants (11/72, 89/432) optional.
"""
import numpy as np
from scipy.integrate import solve_ivp

z3, z4, z5 = 1.2020569031595942, np.pi**4/90, 1.0369277551433699


def beta(nf):
    b0 = (11 - 2*nf/3)/4
    b1 = (102 - 38*nf/3)/16
    b2 = (2857/2 - 5033*nf/18 + 325*nf**2/54)/64
    b3 = (149753/6 + 3564*z3 - (1078361/162 + 6508*z3/27)*nf
          + (50065/162 + 6472*z3/81)*nf**2 + 1093*nf**3/729)/256
    return b0, b1, b2, b3


def gamma(nf):
    g0 = 1.0
    g1 = (202/3 - 20*nf/9)/16
    g2 = (1249 + (-2216/27 - 160*z3/3)*nf - 140*nf**2/81)/64
    g3 = (4603055/162 + 135680*z3/27 - 8800*z5
          + (-91723/27 - 34192*z3/9 + 880*z4 + 18400*z5/9)*nf
          + (5242/243 + 800*z3/9 - 160*z4/3)*nf**2
          + (-332/243 + 64*z3/27)*nf**3)/256
    return g0, g1, g2, g3


def _rhs(t, y, nf, loops):
    a = y[0]
    b = beta(nf); g = gamma(nf)
    da = -sum(b[i]*a**(i+2) for i in range(loops))
    dl = -sum(g[i]*a**(i+1) for i in range(loops))
    return [da, dl]


def run_fixed(a0, lnm0, mu0, mu1, nf, loops=4):
    if mu0 == mu1:
        return a0, lnm0
    s = solve_ivp(_rhs, [np.log(mu0**2), np.log(mu1**2)], [a0, lnm0], args=(nf, loops),
                  rtol=1e-11, atol=1e-14, method='DOP853')
    return s.y[0, -1], s.y[1, -1]


class QCD:
    def __init__(self, asMZ=0.1180, mc=1.27, mb=4.18, mt=163.0, MZ=91.1876,
                 loops=4, match2=True):
        self.th = [mc, mb, mt]
        self.MZ, self.asMZ, self.loops, self.match2 = MZ, asMZ, loops, match2

    def nf_mid(self, lo, hi):
        mid = np.sqrt(lo*hi)
        return 3 + sum(mid > t for t in self.th)

    def evolve(self, a, lnm, mu0, mu1):
        """evolve (a, ln m) from mu0 to mu1 through thresholds. lnm may be a float; the
        mass is a *light* quark relative to every threshold crossed EXCEPT its own:
        for the heavy quark's own mass used below its threshold we simply keep running
        it with nf of the effective theory (RunDec convention)."""
        if mu1 == mu0:
            return a, lnm
        up = mu1 > mu0
        pts = sorted([t for t in self.th if min(mu0, mu1) < t < max(mu0, mu1)], reverse=not up)
        cur = mu0
        for t in pts + [mu1]:
            lo, hi = (cur, t) if up else (t, cur)
            nf = self.nf_mid(lo, hi)
            a, lnm = run_fixed(a, lnm, cur, t, nf, self.loops)
            cur = t
            if t != mu1 and self.match2:
                c2, cm = 11/72, 89/432
                if up:   # nf-1 -> nf :  a^(nf) = a^(nl)/(1+c2 a^2), m^(nf)=m^(nl)/(1+cm a^2)
                    a = a/(1 + c2*a**2)
                    lnm = lnm - np.log(1 + cm*a**2)
                else:
                    a = a*(1 + c2*a**2)
                    lnm = lnm + np.log(1 + cm*a**2)
        return a, lnm

    def alpha_s(self, mu):
        a, _ = self.evolve(self.asMZ/np.pi, 0.0, self.MZ, mu)
        return a*np.pi

    def mass(self, m0, mu0, mu):
        """m(mu) from m(mu0)=m0 using the alpha_s trajectory anchored at MZ."""
        a0 = self.alpha_s(mu0)/np.pi
        a, l = self.evolve(a0, np.log(m0), mu0, mu)
        return float(np.exp(l))


if __name__ == "__main__":
    q = QCD()
    for mu in (1.27, 2.0, 4.18, 91.19, 163., 1000.):
        print(f"alpha_s({mu:8.2f}) = {q.alpha_s(mu):.5f}")
