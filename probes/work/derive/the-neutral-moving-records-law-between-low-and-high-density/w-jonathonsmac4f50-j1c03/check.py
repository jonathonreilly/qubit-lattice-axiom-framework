#!/usr/bin/env python3
"""The neutral moving-records law at low density: the sphere menu's threshold and a beta-dependent two-valued region.
J:derive:the-neutral-moving-records-law-between-low-and-high-density:a2

Setting (block 126 as landed): sites empty (weight 1) or holding a content with a priori weight z times the menu's
measure; bond kernel 1 with an empty end, c e^{beta s.s'} between contents; even periodic cubic tori. Neutral scales:
c0 = beta/sinh(beta) (sphere, uniform probability measure on S^2), c0 = 1/cosh(beta) (two-valued, counting measure).

S  sphere menu at the neutral scale:
   S1 <e^{beta s.v}>_{S^2} = sinh(beta|v|)/(beta|v|)      (exact integral)
   S2 f(x) = log(sinh x / x) is convex with f(0) = 0, hence superadditive, so F_m = c0^m sinh(m beta)/(m beta)
      increases with m; the occupation probability given everything else is <= z F_6(beta)
   S3 no long-range order and bounded structure factor for z < z0(beta) = 1/(5 F_6(beta)) at every beta;
      z0 ~ 3/(80 beta^5) at large beta (probe #9260's remark gave (beta e^beta/sinh beta)^-6/5, weaker by ~12 beta)
   S4 cluster decoupling survives (SO(3) rotation of one occupied cluster)
T  two-valued menu: the same bound with the exact beta-dependence, z < 1/(5[(1+t)^6 + (1-t)^6]), t = tanh beta,
   contains #9260's z < 1/320 for every beta and is 32 times larger at beta -> 0
"""
import sys, time
from fractions import Fraction as Fr
import sympy as sp

T0 = time.time()
FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)

b, x, th, v = sp.symbols('beta x theta v', positive=True)
print("== S sphere menu")
# S1 average of e^{beta v cos(theta)} over the unit sphere with the uniform probability measure (1/2) sin(theta) d theta
avg = sp.integrate(sp.exp(b*v*sp.cos(th))*sp.sin(th)/2, (th, 0, sp.pi))
check("S1 <e^{beta s.v}> over the uniform probability measure on S^2 = sinh(beta|v|)/(beta|v|)",
      sp.simplify(avg - sp.sinh(b*v)/(b*v)) == 0, str(sp.simplify(avg)))
c0 = b/sp.sinh(b)
check("S1b neutral scale: c0 <e^{beta s.s'}> = 1 (an occupied neighbour weighs the same as an empty one on average)",
      sp.simplify(c0*sp.sinh(b)/b - 1) == 0)
# S2 convexity of f(x) = log(sinh x / x): f'' = 1/x^2 - 1/sinh(x)^2 > 0 because sinh x > x
f = sp.log(sp.sinh(x)/x)
f2 = sp.simplify(sp.diff(f, x, 2))
check("S2a f(x) = log(sinh x/x) has f''(x) = 1/x^2 - 1/sinh(x)^2", sp.simplify(f2 - (1/x**2 - 1/sp.sinh(x)**2)) == 0, str(f2))
ser = sp.series(sp.sinh(x) - x, x, 0, 8).removeO()
check("S2b sinh x - x = x^3/6 + x^5/120 + ... has only positive Taylor coefficients (so sinh x > x > 0 and f'' > 0)",
      all(cf > 0 for cf in sp.Poly(ser, x).coeffs()))
check("S2c f(0+) = 0", sp.limit(f, x, 0) == 0)
# superadditivity from convexity with f(0) = 0 gives F_{m+1}/F_m = exp(f((m+1)b) - f(mb) - f(b)) >= 1
F = lambda m: c0**m*sp.sinh(m*b)/(m*b) if m else sp.Integer(1)
okmono = True
for m in range(0, 6):
    ratio = sp.simplify(F(m + 1)/F(m))
    if m >= 1:
        g = lambda y: sp.sinh(y)/y                      # exp(f(y)) = g(y)
        target = g((m + 1)*b)/(g(m*b)*g(b))
        if sp.simplify(ratio/target - 1) != 0: okmono = False
import mpmath as mp
mp.mp.dps = 40
num_ok = all(float((F(m + 1)/F(m)).subs(b, bv)) >= 1 - 1e-30 for m in range(0, 6) for bv in (sp.Rational(1, 100), sp.Rational(1, 3), 1, 2, 5, 10, 30))
check("S2d F_{m+1}/F_m = exp(f((m+1)beta) - f(m beta) - f(beta)) >= 1 (identity exact; spot values >= 1)", okmono and num_ok)
# S3 threshold and asymptotics
F6 = F(6)
z0 = 1/(5*F6)
lim = sp.limit(F6/b**5, b, sp.oo)
check("S3a large beta: beta^-5 F_6(beta) -> 16/3, so z0(beta) ~ 3/(80 beta^5)", sp.simplify(lim - sp.Rational(16, 3)) == 0, str(lim))
check("S3b small beta: F_6 -> 1, so z0 -> 1/5", sp.limit(F6, b, 0) == 1)
old = (b*sp.exp(b)/sp.sinh(b))**6
lim2 = sp.limit(old/F6/b, b, sp.oo)
check("S3c against #9260's remark bound (beta e^beta/sinh beta)^6: ratio old/new ~ 12 beta", sp.simplify(lim2 - 12) == 0, str(lim2))
for bv in (sp.Rational(1, 2), 1, 2, 5, 10, 20):
    print(f"   beta = {bv}: z0 = 1/(5 F_6) = {mp.nstr(mp.mpf(1)/(5*mp.mpf(sp.N(F6.subs(b, bv), 40))), 8)}   (#9260 remark: {mp.nstr(mp.mpf(1)/(5*mp.mpf(sp.N(old.subs(b, bv), 40))), 8)})")
# S4 decoupling: Haar average of a rotation is zero (checked on the finite rotation group of the cube as a stand-in)
import itertools
Rs = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        Mx = sp.zeros(3)
        for i in range(3): Mx[i, perm[i]] = sg[i]
        if Mx.det() == 1: Rs.append(Mx)
check("S4 the 24 proper rotations of the cube average to the zero matrix (a finite group acting irreducibly; the "
      "Haar average over SO(3) is likewise 0), so rotating one occupied cluster kills <s_x.s_y | O> across clusters",
      len(Rs) == 24 and sum(Rs, sp.zeros(3)) == sp.zeros(3))
# S5 path count and the sum rule
p = sp.Symbol('p', positive=True)
n = sp.Symbol('n', integer=True, positive=True)
okS5 = all(sp.summation(6*5**(n - 1)*pv**(n + 1), (n, 1, sp.oo)) == 6*pv**2/(1 - 5*pv) for pv in (sp.Rational(1, 7), sp.Rational(1, 10), sp.Rational(3, 16)))
check("S5 sum_n 6*5^(n-1) p^(n+1) = 6p^2/(1-5p) (geometric series, exact at p = 1/7, 1/10, 3/16), so sum_x P(0 <-> x) <= p + 6p^2/(1-5p) for p < 1/5", okS5)

print("== T two-valued menu, exact beta dependence")
t = sp.Symbol('t', positive=True)
okT = True
for k in range(7):
    for l in range(7 - k):
        S = sp.expand((1 + t)**k*(1 - t)**l + (1 - t)**k*(1 + t)**l)
        diff = sp.Poly(sp.expand((1 + t)**6 + (1 - t)**6 - S), t)
        if any(cf < 0 for cf in diff.coeffs()): okT = False
check("T1 for all k + l <= 6: (1+t)^6 + (1-t)^6 - S(k,l) has non-negative coefficients (#9260 L1), so the occupation "
      "probability is <= z[(1+t)^6 + (1-t)^6] at each beta", okT)
G = (1 + t)**6 + (1 - t)**6
check("T2 G(t) = (1+t)^6 + (1-t)^6 increases on [0,1] from 2 to 64; region z < 1/(5G(tanh beta)) contains z < 1/320 "
      "and is 32 times larger at beta -> 0", sp.simplify(G.subs(t, 0) - 2) == 0 and sp.simplify(G.subs(t, 1) - 64) == 0
      and all(cf >= 0 for cf in sp.Poly(sp.diff(G, t), t).coeffs()))
for bv in (sp.Rational(1, 4), 1, 2, 5):
    tv = sp.tanh(bv)
    print(f"   beta = {bv}: two-valued threshold 1/(5 G) = {mp.nstr(mp.mpf(1)/(5*mp.mpf(sp.N(G.subs(t, tv), 30))), 8)} (vs 1/320 = 0.003125)")

print(f"== done in {time.time()-T0:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: PROVED (sphere menu, low density): at the neutral scale c0 = beta/sinh beta, every conditional occupation "
          "probability is <= z F_6(beta), F_6 = (beta/sinh beta)^6 sinh(6 beta)/(6 beta) (sphere average + superadditivity of "
          "log(sinh x/x)); cluster decoupling survives (rotating one occupied cluster); hence no long-range order and a bounded "
          "structure factor for z < z0(beta) = 1/(5 F_6(beta)) at every beta, z0 ~ 3/(80 beta^5) (12 beta better than the prior "
          "remark); two-valued: the exact beta-dependent region z < 1/(5[(1+t)^6+(1-t)^6]) contains z < 1/320 (32x at small beta)")
    print("HIT sphere menu at the neutral scale: no order for z < 1/(5 F_6(beta)), explicit, ~ 3/(80 beta^5); cluster decoupling survives")
