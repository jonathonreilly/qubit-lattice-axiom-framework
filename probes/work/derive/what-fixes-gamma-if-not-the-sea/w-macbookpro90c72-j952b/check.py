#!/usr/bin/env python3
"""J:derive:what-fixes-gamma-if-not-the-sea:a2 - checks for ATTEMPT.md (same directory). Exact (sympy) unless labelled.

The inventory of pure numbers in blocks 53-78 is in ATTEMPT.md (with sources). Here: (1) the walker's top speed at
w = 1 is exactly 1; (2) every speed of a field whose energy is quadratic in its coefficients is invariant under scaling
all field-energy coefficients (K, alpha, beta_kin) by one factor, while the static coupling gamma = 1/(4K) is not, so
no speed-matching condition fixes gamma or K; (3) gamma = 1/(4K) is an identity of block 60's curvature member at
second order (checked on a ring); (4) the one reading that fixes gamma - the filled sea booked as the field's energy
with the per-site counter-term - gives exactly 12/|c0| (from J:derive:normal-ordering-as-a-rule:a2, #8761; recomputed);
(5) the comparator's map from gamma to the lattice spacing in Planck units (a comparator only).
"""
import sys

import mpmath as mp
import numpy as np
import sympy as sp

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


# ------------------------------------------------------------------ 1. the walker's top speed
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
ks = (k1, k2, k3)
eps = sp.sqrt(sum(sp.sin(k) ** 2 for k in ks))
v2 = sum(sp.diff(eps, k) ** 2 for k in ks)
gap = sp.simplify(1 - v2 - sum(sp.sin(k) ** 4 for k in ks) / eps ** 2)
lim = sp.limit(v2.subs({k2: 0, k3: 0}), k1, 0)
ok("A1", gap == 0 and lim == 1,
   "block 54's walk at w = 1: 1 - |grad eps|^2 = sum sin^4 k / sum sin^2 k >= 0, with |grad eps| -> 1 as k -> 0 along an "
   "axis: the top speed is exactly 1, and the rate unit w = 1 fixes it; it involves no field number")

# ------------------------------------------------------------------ 2. scaling: speeds see only ratios of field numbers
lam, al, bk, K, q, om, cV, cT1, cT2 = sp.symbols("lambda alpha beta_kin K q omega c_V c_T1 c_T2", positive=True)
# any travelling disturbance of a quadratic field energy: potential c_V K q^2 against kinetic (c_T1 alpha + c_T2 beta_kin);
# the decision record's transverse ripples: omega^2 = K q^2 / (4 alpha) (alpha = K/4 puts them at the walker's top speed)
disp_gen = cV * K * q ** 2 / (cT1 * al + cT2 * bk)
disp_T = K * q ** 2 / (4 * al)
scaled = [sp.simplify(d.subs({al: lam * al, bk: lam * bk, K: lam * K}, simultaneous=True) - d) for d in (disp_gen, disp_T)]
gam = 1 / (4 * K)
ok("A2", scaled == [0, 0] and sp.simplify(gam.subs(K, lam * K) - gam / lam) == 0 and sp.solve(sp.Eq(disp_T, q ** 2), al) == [K / 4],
   "every travelling speed of a field energy quadratic in its coefficients is a ratio (omega^2 = c_V K q^2/(c_T1 alpha + "
   "c_T2 beta_kin); the ripples of the decision record, K q^2/(4 alpha)), unchanged by scaling (K, alpha, beta_kin) by one "
   "lambda, while gamma = 1/(4K) -> gamma/lambda: matching the ripples to the walker's top speed fixes alpha = K/4 and "
   "nothing about K or gamma")

# ------------------------------------------------------------------ 3. gamma = 1/(4K): block 60's member on a ring
N = 5
e = sp.Symbol("e")
Kk = sp.Symbol("K", positive=True)
us = sp.symbols(f"u0:{N}")
ls = sp.symbols(f"l0:{N}")
m = [sp.Integer(1) if i == 0 else sp.Integer(0) for i in range(N)]  # a unit body at rest at site 0
lapf = lambda f, i: f[(i + 1) % N] + f[(i - 1) % N] - 2 * f[i]
qf = lambda f, i: sp.Rational(1, 2) * ((f[(i + 1) % N] - f[i]) ** 2 + (f[(i - 1) % N] - f[i]) ** 2)
tt, mu = sp.symbols("t mu")
ledger = sum(e * m[i] * sp.exp(us[i]) + sp.exp(us[i]) * Kk * sp.exp(ls[i]) * (4 * lapf(ls, i) + 2 * qf(ls, i)) for i in range(N))
# first order in a bookkeeping t (u, l, e all O(t)); the unit of rate is held: stationarity under sum du = 0 (multiplier mu)
sub = {**{x: tt * x for x in list(us) + list(ls)}, e: tt * e}
eqs = []
for v in us:
    eqs.append(sp.expand(sp.series(sp.diff(ledger, v).subs(sub, simultaneous=True), tt, 0, 2).removeO()).coeff(tt, 1) - mu)
for v in ls:
    eqs.append(sp.expand(sp.series(sp.diff(ledger, v).subs(sub, simultaneous=True), tt, 0, 2).removeO()).coeff(tt, 1))
sol = sp.solve(eqs + [sum(us), sum(ls)], list(us) + list(ls) + [mu], dict=True)
ring_ok = bool(sol)
if ring_ok:
    s0 = sol[0]
    ring_ok = all(sp.simplify(lapf([s0[x] for x in us], i) - (1 / (4 * Kk)) * (e * m[i] - e / N)) == 0 for i in range(N))
ok("A3", ring_ok,
   "block 60's curvature member K l (4 lap l + 2 q) per tick, a unit body at rest on a ring of 5, stationary to first order "
   "in its energy with the unit of rate held by the mean: lap u = (1/(4K)) (e - mean e), i.e. block 55's law with gamma = "
   "1/(4K): an identity of the member, fixing neither")

# ------------------------------------------------------------------ 4. the sea reading's value (FLOAT momentum sums)
def c0_mid(L):
    n = (np.arange(L) + 0.5) * 2 * np.pi / L
    KY, KZ = np.meshgrid(n, n, indexing="ij")
    s2 = np.sin(KY) ** 2 + np.sin(KZ) ** 2
    return -sum(np.sqrt(np.sin(kx) ** 2 + s2).sum() for kx in n) / L ** 3


c0s = [c0_mid(L) for L in (64, 128, 256)]
c0 = c0s[2] + (c0s[2] - c0s[1]) / 15
gam_site = 12 / abs(c0)
ok("A4", abs(c0 + 1.193801121) < 2e-9,
   f"the filled sea booked as the field's energy, with the per-site counter-term c0 sum w: gamma = 12/|c0| = "
   f"{gam_site:.6f} exactly in terms of c0 = -<|sin k|> = {c0:.9f} (#8761), in block 56's member (half bending); with "
   "the equally admissible per-bond counter-term the long-wavelength stiffness is exactly 0 and no gamma is induced; the "
   "sea gives the clock stiffness a u.u term that the curvature member does not have, so it fixes no K")

# ------------------------------------------------------------------ 5. comparator only: lattice spacing in Planck units
mp.mp.dps = 20
g0 = mp.sqrt(6) / (32 * mp.pi ** 3) * mp.gamma(mp.mpf(1) / 24) * mp.gamma(mp.mpf(5) / 24) * mp.gamma(mp.mpf(7) / 24) * mp.gamma(mp.mpf(11) / 24)
rows = []
for name, gv in (("12/|c0|", gam_site), ("10.51 (block 76)", 10.51)):
    rows.append(f"gamma = {name}: a = sqrt(4 pi/gamma) l_P = {np.sqrt(4 * np.pi / gv):.4f} l_P, saturation 12/(gamma g0) = "
                f"{12 / (gv * float(g0)):.4f}")
ok("A5", abs(float(g0) - 1.516386059151978) < 1e-12,
   "comparator (not adopted): with packets falling at -grad u and Newton's lap Phi = 4 pi G rho, block 55's lap u = gamma e "
   "reads gamma = 4 pi G in lattice units (hbar = c = a = 1), so a/l_P = sqrt(4 pi/gamma); for the curvature member "
   "gamma = 1/(4K) gives a/l_P = sqrt(16 pi K), of order one iff K ~ 1/(16 pi) = 0.0199: " + "; ".join(rows))

print(f"SUMMARY: {'PARTIAL' if not FAILS else 'PARTIAL (failed checks: ' + ', '.join(FAILS) + ')'} no supplied clause "
      "other than the sea reading fixes gamma or K: A, B, C give one pure number gamma; gamma = 1/(4K) is an identity of "
      "the curvature member; alpha = K/4 (ripples at the walker's top speed) and every other speed condition fix only "
      "ratios, being invariant under scaling all field-energy numbers, which moves gamma = 1/(4K); the sea with the "
      f"per-site counter-term fixes gamma = 12/|c0| = {gam_site:.4f} in the half-bending member only (#8761); comparator: "
      f"a = {np.sqrt(4 * np.pi / gam_site):.3f} l_P; the unit's HIT condition is not met")
