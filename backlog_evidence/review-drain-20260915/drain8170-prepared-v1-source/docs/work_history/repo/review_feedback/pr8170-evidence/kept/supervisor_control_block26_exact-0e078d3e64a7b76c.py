"""Control (exact parts) for block 26: (1) vMF moments on S^2: E[w] = A(k) = coth k - 1/k, E[w^2] = 1 - 2A/k; the Langevin bound
A(k) <= k/3 via sinh^2 k >= k^2 + k^4/3.  (2) The level walk's return sum P_k = sum_y p_k(y)^2 exactly (k <= 300) and the explicit
two-sided bounds 3 sqrt3/(4 pi k) - 1/k^2 - (5/(2k)) e^{-k/4} <= P_k <= 3 sqrt3/(4 pi k) + 27/k^2 + e^{-sqrt k/7}; k P_k for larger k by
quadrature.  (3) The spin-wave exponent gamma(beta) = (3 sqrt3/(4 pi)) A(3 beta)/(3 beta)."""
import sympy as sp
from fractions import Fraction as F
from math import comb, factorial, sqrt, pi, exp, cos
k, w = sp.symbols("kappa w", positive=True)
Z = sp.integrate(sp.exp(k * w), (w, -1, 1))
Ew = sp.simplify(sp.integrate(w * sp.exp(k * w), (w, -1, 1)) / Z)
Ew2 = sp.simplify(sp.integrate(w**2 * sp.exp(k * w), (w, -1, 1)) / Z)
A = sp.coth(k) - 1 / k
print("(1) E[w] - A =", sp.simplify((Ew - A).rewrite(sp.exp)), "; E[w^2] - (1 - 2A/k) =", sp.simplify((Ew2 - (1 - 2 * A / k)).rewrite(sp.exp)))
# Langevin bound: A'(k) = 1/k^2 - 1/sinh^2 k <= 1/(3 + k^2) since sinh^2 k >= k^2 + k^4/3: series of sinh^2 = (cosh 2k - 1)/2 = sum_{n>=1} (2k)^{2n}/(2 (2n)!)
ser = sp.series(sp.sinh(k)**2 - k**2 - k**4 / 3, k, 0, 12).removeO()
print("(1) sinh^2 k - k^2 - k^4/3 series (all coefficients >= 0):", ser, "; A' == 1/k^2 - 1/sinh^2:", sp.simplify(sp.diff(A, k) - (1 / k**2 - 1 / sp.sinh(k)**2)) == 0)
# (2) P_k exact
def Pk(kk):
    tot = 0
    for a in range(kk + 1):
        for b in range(kk + 1 - a):
            c = kk - a - b
            m = factorial(kk) // (factorial(a) * factorial(b) * factorial(c))
            tot += m * m
    return F(tot, 9 ** kk)
c0 = 3 * sqrt(3) / (4 * pi)
ok = True; worst_lo = 0; worst_hi = 0
for kk in range(1, 301):
    p = float(Pk(kk))
    lo = c0 / kk - 1 / kk**2 - (5 / (2 * kk)) * exp(-kk / 4); hi = c0 / kk + 27 / kk**2 + exp(-sqrt(kk) / 7)
    ok = ok and lo <= p <= hi
    worst_lo = max(worst_lo, (c0 / kk - p) * kk * kk); worst_hi = max(worst_hi, (p - c0 / kk) * kk * kk)
print(f"(2) two-sided bounds hold for k <= 300: {ok}; k^2 (c0/k - P_k) max = {worst_lo:.3f}; k^2 (P_k - c0/k) max = {worst_hi:.3f}; k P_k at 300 = {300*float(Pk(300)):.5f} vs c0 = {c0:.5f}")
# quadrature for larger k
import numpy as np
n = 4096; th = np.linspace(-np.pi, np.pi, n, endpoint=False)
T1, T2 = np.meshgrid(th, th, indexing="ij")
u = (3 + 2 * np.cos(T1) + 2 * np.cos(T2) + 2 * np.cos(T1 - T2)) / 9
for kk in (300, 1000, 3000, 10000):
    print(f"(2) quadrature k P_k at k={kk}: {kk * (u**kk).mean():.5f}")
def Afun(x): return 1 / np.tanh(x) - 1 / x
for beta in (3, 6, 12, 24, 48):
    g = c0 * Afun(3 * beta) / (3 * beta)
    print(f"(3) gamma_lin(beta={beta}) = {g:.5f}  (A(3beta) = {Afun(3*beta):.5f}; sqrt3/(4 pi beta) = {sqrt(3)/(4*pi*beta):.5f})")
