#!/usr/bin/env python3
"""Referee for J:derive:strong-field-turning-by-a-clump:a2.

The radial index, the capture threshold and the Lambert series are re-derived
with sympy and mpmath. The author's script is not called.
"""
import sys

import mpmath as mp
import sympy as sp

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


A, r, b, x, y, beta, eps = sp.symbols("A r b x y beta eps", positive=True)
f = r * sp.exp(A / r)
fp = sp.simplify(sp.diff(f, r))
ok("C1", sp.simplify(fp - sp.exp(A / r) * (1 - A / r)) == 0 and sp.simplify(f.subs(r, A) - sp.E * A) == 0,
   "f(r)=r e^{A/r} has f'(r)=e^{A/r}(1-A/r), so its minimum is f(A)=e A")

# circular ray: |v|=w=e^{-1}, centripetal |v|^2/A equals w^2 |grad u|
wA = sp.exp(-1)
cent = wA ** 2 / A
# u=-A/r, |grad u|=A/r^2, at r=A is 1/A; w^2=e^{-2}
law = sp.exp(-2) / A
ok("C2", sp.simplify(cent - law) == 0,
   "on r=A the law's acceleration e^{-2}/A equals the centripetal acceleration of |v|=1/e")

# substitution: beta dx / sqrt(e^{2x}-beta^2 x^2) = dy/((1-x) sqrt(1-y^2)) when y=beta x e^{-x}
yy = beta * x * sp.exp(-x)
rad = sp.sqrt(sp.exp(2 * x) - beta ** 2 * x ** 2)
lhs = sp.simplify(beta / rad)
dydx = sp.diff(yy, x)
rhs_per_dx = sp.simplify(dydx / ((1 - x) * sp.sqrt(1 - yy ** 2)))
ok("S1", sp.simplify(lhs - rhs_per_dx) == 0,
   "y = beta x e^{-x} turns the Bouguer integral into dy/((1-x) sqrt(1-y^2)); x=-W0(-y/beta)")

def c_n(n):
    return sp.sqrt(sp.pi) * n ** n * sp.gamma(sp.Rational(n + 1, 2)) / (sp.factorial(n) * sp.gamma(sp.Rational(n, 2) + 1))

want = {
    1: 2,
    2: sp.pi,
    3: 6,
    4: 4 * sp.pi,
    5: sp.Rational(250, 9),
    6: 81 * sp.pi / 4,
}
series_ok = all(sp.simplify(c_n(n) - val) == 0 for n, val in want.items())
# beta integral I_n = int_0^1 y^n / sqrt(1-y^2) dy = (sqrt(pi)/2) Gamma((n+1)/2)/Gamma(n/2+1)
t = sp.symbols("t", positive=True)
moments_ok = True
for n in range(0, 7):
    exact = sp.integrate(sp.sin(t) ** n, (t, 0, sp.pi / 2))  # y=sin t
    formula = sp.sqrt(sp.pi) / 2 * sp.gamma(sp.Rational(n + 1, 2)) / sp.gamma(sp.Rational(n, 2) + 1)
    moments_ok &= sp.simplify(exact - formula) == 0
# 2 I_n * n^n / n! = c_n
link_ok = all(sp.simplify(2 * (sp.sqrt(sp.pi) / 2 * sp.gamma(sp.Rational(n + 1, 2)) / sp.gamma(sp.Rational(n, 2) + 1))
                          * n ** n / sp.factorial(n) - c_n(n)) == 0 for n in range(1, 7))
ok("S2", series_ok and moments_ok and link_ok,
   "c_n = 2, pi, 6, 4 pi, 250/9, 81 pi/4 for n=1..6, and c_n = 2 n^n I_n / n! with the beta moments")

# radius: n c_n e^{-n} -> 1, checked at large n in high precision; the series radius is 1/e
mp.mp.dps = 30
def c_mp(n):
    return mp.sqrt(mp.pi) * mp.power(n, n) * mp.gamma((n + 1) / 2) / (mp.factorial(n) * mp.gamma(n / 2 + 1))

ratios = [n * c_mp(n) * mp.exp(-n) for n in (20, 40, 80)]
ok("K1", all(abs(z - 1) < mp.mpf("0.02") for z in ratios) and abs(ratios[-1] - 1) < abs(ratios[0] - 1),
   f"n c_n e^{{-n}} = {mp.nstr(ratios[0], 6)}, {mp.nstr(ratios[1], 6)}, {mp.nstr(ratios[2], 6)}, approaching 1, so the radius is 1/e")

# integral versus the series at eps=1/5 < 1/e
eps_v = mp.mpf(1) / 5

def integrand(yy):
    return 1 / ((1 + mp.lambertw(-yy * eps_v)) * mp.sqrt(1 - yy ** 2))

chi_int = 2 * mp.quad(integrand, [0, 1]) - mp.pi
chi_ser = sum(c_mp(n) * eps_v ** n for n in range(1, 50))
ok("N1", abs(chi_int - chi_ser) < mp.mpf("1e-10"),
   f"at A/b=1/5 the Lambert integral is {mp.nstr(chi_int, 12)} and the series is {mp.nstr(chi_ser, 12)}")

# threshold constant from the series, and the singular integral's log
# C = sum (c_n e^{-n} - 1/n). Partial sum plus the tail ~ -1/(2n) from 1 - n c_n e^{-n} ~ 1/(3n) or similar;
# compare two cutoffs.
def partial_C(N):
    return sum(c_mp(n) * mp.exp(-n) - 1 / mp.mpf(n) for n in range(1, N + 1))

C200, C400 = partial_C(200), partial_C(400)
ok("K2", abs(C400 - C200) < mp.mpf("1e-3") and abs(C400 + mp.mpf("0.4658175633")) < mp.mpf("2e-3"),
   f"sum (c_n e^{{-n}} - 1/n) is {mp.nstr(C400, 8)} at 400 terms (quoted -0.46581756)")

if FAILS:
    print("SUMMARY: fails at step " + ", ".join(FAILS) + " - independent check disagreed")
    sys.exit(1)
print("SUMMARY: confirmed - for u=-A/r the critical impact parameter is e A, and above it the turn is the Lambert series 2A/b + pi(A/b)^2 + 6(A/b)^3 + ...")
print("HIT: confirmed - f(r)=r e^{A/r} is minimized at r=A with value e A, so a ray is captured iff b<eA and the circle r=A is a ray; for b>eA, chi = 2 int_0^1 dy/((1+W0(-y A/b)) sqrt(1-y^2)) - pi = sum c_n (A/b)^n with c_n = sqrt(pi) n^n Gamma((n+1)/2)/(n! Gamma(n/2+1)), whose first terms are 2, pi, 6, 4 pi, and whose radius is exactly 1/e.")
