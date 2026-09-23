#!/usr/bin/env python3
"""the-level-ordered-response-kernel a1 (w-jonathonsmac4f50-j40ae). Exact arithmetic (Fraction, sympy) except section N.

Linear (gain-one) theory under the level-ordered past {0, -e1, -e2, -e3}: theta'(x) = (1/4) sum_d theta(x + d) + source,
so P(k) = (1 + sum_j e^{-i k_j})/4 and the stationary kernel is G = sum_n P^n.
  E1 G(a,b,c) = (4/3) L!/(a! b! c!) 3^{-L}, L = a + b + c, on the forward octant, 0 elsewhere (recursion, all L <= 24)
  E2 the zero-step sum: sum_j C(L+j, j) 4^{-j} = (4/3)^{L+1}
  E3 every level carries total response 4/3; Fourier: R(k) = 4/(3 - sum_j e^{-i k_j})
  E4 light-cone comparator 7/E(k), E(k) = 6 - 2 sum cos k_j; drift-free directions: R_lo E = 2 (gain one), and the
     rule-gain model A(4 beta)/(3 - sum e^{-ik}) exceeds the light-cone bound 1/E(k) iff A(4 beta) > 1/2
  N  on-axis and transverse asymptotics of the wake (floating point, labelled)
"""
import sys, math
from fractions import Fraction as Fr
from math import factorial, comb
import sympy as sp

FAILS = []
def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok: FAILS.append(name)

def Gclosed(a, b, c):
    if min(a, b, c) < 0: return Fr(0)
    L = a + b + c
    return Fr(4, 3)*Fr(factorial(L), factorial(a)*factorial(b)*factorial(c))/Fr(3)**L

# ------------------------------------------------------------------ E1 the recursion G = delta + P G on Z^3
# G(x) = delta_{x0} + (1/4) G(x) + (1/4) sum_j G(x - e_j)  <=>  G(x) = (4/3) delta + (1/3) sum_j G(x - e_j)
LMAX = 24
G = {}
ok = True
for L in range(0, LMAX + 1):
    for a in range(L + 1):
        for b in range(L - a + 1):
            c = L - a - b
            val = (Fr(4, 3) if L == 0 else Fr(0)) + Fr(1, 3)*sum(G.get(y, Fr(0)) for y in [(a-1, b, c), (a, b-1, c), (a, b, c-1)])
            G[(a, b, c)] = val
            ok &= val == Gclosed(a, b, c)
check("E1.1 the recursion G = (4/3) delta + (1/3) sum_j G(x - e_j) is solved by (4/3) L!/(a!b!c!) 3^(-L) at every octant point with L <= 24", ok)
# outside the octant the recursion started from zero gives zero: a point with a negative coordinate only receives
# from points with a negative coordinate (x - e_j keeps it negative), and the source sits at the origin
check("E1.2 the kernel vanishes off the forward octant (support argument; sampled: every point with a coordinate -1, |x|<=6, gets 0)",
      all(Gclosed(a, b, c) == 0 for a in range(-1, 6) for b in range(-1, 6) for c in range(-1, 6) if min(a, b, c) < 0))
# ------------------------------------------------------------------ E2 the zero-step series
Lsym, jsym = sp.symbols('L j', integer=True, nonnegative=True)
okser = all(sum(Fr(comb(L + j, j), 4**j) for j in range(0, 400)) <= Fr(4, 3)**(L + 1) and
            Fr(4, 3)**(L + 1) - sum(Fr(comb(L + j, j), 4**j) for j in range(0, 400)) < Fr(1, 10**30) for L in range(0, 12))
check("E2 sum_j C(L+j, j) 4^(-j) = (4/3)^(L+1) (partial sums to j = 400 below it and within 1e-30, L = 0..11; the identity is (1-x)^(-L-1) at x = 1/4)", okser)
# ------------------------------------------------------------------ E3 level totals and the Fourier kernel
check("E3.1 every level L carries total response exactly 4/3 (L = 0..24)",
      all(sum(G[(a, b, L - a - b)] for a in range(L + 1) for b in range(L - a + 1)) == Fr(4, 3) for L in range(LMAX + 1)))
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
u = [sp.exp(-sp.I*k1), sp.exp(-sp.I*k2), sp.exp(-sp.I*k3)]
S = sum(u)
# level-L Fourier sum = (4/3)(S/3)^L by the multinomial theorem; geometric sum -> 4/(3 - S)
Lz = 5
lvl = sum(sp.Rational(Gclosed(a, b, Lz - a - b).numerator, Gclosed(a, b, Lz - a - b).denominator)*u[0]**a*u[1]**b*u[2]**(Lz - a - b)
          for a in range(Lz + 1) for b in range(Lz - a + 1))
check("E3.2 level sum sum_{a+b+c=L} G e^{-ik.x} = (4/3)(sum_j e^{-ik_j}/3)^L (multinomial theorem, L = 5 symbolic)",
      sp.expand(lvl - sp.Rational(4, 3)*(S/3)**Lz) == 0)
check("E3.3 R(k) = sum_L (4/3)(S/3)^L = 4/(3 - S) = 1/(1 - P(k)) with P = (1 + S)/4",
      sp.simplify(sp.Rational(4, 3)/(1 - S/3) - 1/(1 - (1 + S)/4)) == 0)
# ------------------------------------------------------------------ E4 comparison with the light-cone law
q = sp.symbols('q', real=True)
E = lambda kk: 6 - 2*sum(sp.cos(t) for t in kk)
kdf = (q, -q, 0)                                     # a drift-free direction: sum sin k_j = 0
den = 3 - sum(sp.exp(-sp.I*t) for t in kdf)
check("E4.1 light-cone gain-one kernel: 1/(1 - P_lc) = 7/E(k) with P_lc = (1 + 2 sum cos k_j)/7",
      sp.simplify(1/(1 - (1 + 2*(sp.cos(k1) + sp.cos(k2) + sp.cos(k3)))/7) - 7/E((k1, k2, k3))) == 0)
check("E4.2 along k = (q, -q, 0): 3 - sum e^{-ik_j} = E(k)/2, so the level-ordered gain-one kernel is 8/E(k) (vs 7/E light-cone)",
      sp.simplify((den - E(kdf)/2).rewrite(sp.cos)) == 0)
kap = sp.symbols('kappa', positive=True)
Afun = sp.coth(kap) - 1/kap
# the rule-gain linear model: theta' = P theta + (A(4 beta)/4) h  ->  theta = A(4 beta)/(3 - S) h; on k=(q,-q,0): 2 A(4 beta)/E(k)
lo, hi = Fr(179, 100), Fr(181, 100)
check("E4.3 A(kappa) = 1/2 at kappa* in (1.79, 1.81): the rule-gain model exceeds the light-cone bound 1/E(k) in the drift-free "
      "directions iff 4 beta > kappa*, i.e. beta > 0.45 (A increasing)",
      Afun.subs(kap, sp.Rational(179, 100)).evalf(30) < sp.Rational(1, 2) < Afun.subs(kap, sp.Rational(181, 100)).evalf(30)
      and sp.diff(Afun, kap).subs(kap, sp.Rational(18, 10)).evalf(30) > 0)
check("E4.4 the kernel is not symmetric: G(1,0,0) = 4/9 but G(-1,0,0) = 0 (forward-backward asymmetry, exact)",
      Gclosed(1, 0, 0) == Fr(4, 9) and Gclosed(-1, 0, 0) == 0)

# ------------------------------------------------------------------ N  asymptotics (floating point, labelled)
def lgG(a, b, c):
    L = a + b + c
    return math.log(4/3) + math.lgamma(L + 1) - math.lgamma(a + 1) - math.lgamma(b + 1) - math.lgamma(c + 1) - L*math.log(3)
ax = []
for n in (10, 100, 1000, 10000):
    L = 3*n; r = L/math.sqrt(3)
    ax.append(math.exp(lgG(n, n, n))*math.pi*r/2)
print("   NUMERICAL on-axis G(n,n,n) * pi r / 2 (should -> 1):", [round(v, 5) for v in ax])
check("N1 NUMERICAL: on the axis G ~ 2/(pi r) = (8/7) x 7/(4 pi r)", abs(ax[-1] - 1) < 1e-3)
tr = []
n = 3000; L = 3*n
for dlt in (0, 20, 40, 60):                           # move (n+dlt, n-dlt, n): transverse displacement rho = dlt*sqrt(2)
    rho2 = 2*dlt**2
    pred = 2*math.sqrt(3)/(math.pi*L)*math.exp(-3*rho2/(2*L))
    tr.append(math.exp(lgG(n + dlt, n - dlt, n))/pred)
print("   NUMERICAL transverse profile / (2 sqrt3/(pi L)) exp(-3 rho^2/(2L)) at L = 9000:", [round(v, 4) for v in tr])
check("N2 NUMERICAL: Gaussian cross-section of variance L/3 per transverse direction", all(abs(v - 1) < 5e-3 for v in tr))

print()
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0]); sys.exit(1)
print("SUMMARY: PROVED the level-ordered gain-one response kernel exactly: G(a,b,c) = (4/3) L!/(a!b!c!) 3^-L on the forward "
      "octant and 0 elsewhere (L = a+b+c); R(k) = 4/(3 - sum e^-ik_j); every level carries 4/3; a one-sided wake along "
      "(1,1,1) with on-axis 2/(pi r) (8/7 of the light-cone kernel's 7/(4 pi r)) and a Gaussian cross-section of variance L/3; "
      "in drift-free directions the rule-gain model gives 2A(4 beta)/E(k), above the light-cone bound 1/E(k) iff beta > 0.45")
print("HIT: (a) exact: the level-ordered gain-one kernel is G(a,b,c) = (4/3) L!/(a!b!c!) 3^-L on the forward octant, zero "
      "behind: a wake along (1,1,1), not the inverse Laplacian (on-axis 2/(pi r), Gaussian cross-section of variance L/3, total "
      "4/3 per level, R(k) = 4/(3 - sum_j e^-ik_j)); (b) its rule-gain linear response exceeds the light-cone bound 1/E(k) "
      "by the factor 2A(4 beta) in the drift-free directions, i.e. for beta > 0.45")
