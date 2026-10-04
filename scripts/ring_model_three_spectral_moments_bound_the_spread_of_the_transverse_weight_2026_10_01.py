#!/usr/bin/env python3
"""Three spectral moments bound how the spectral weight spreads: sharp tail, hole and gap inequalities, applied to the 8^3 ring estimates.

Let mu be a positive finite measure on (0, inf) with moments m_j = int omega^j dmu, j = -1, 0, 1 (the landed ring-component moments
are m1 = 2 u s^2, m_-1 = chi/2, m0 = S). Put R = m0/sqrt(m1 m_-1) in (0, 1], omega_g = sqrt(m1/m_-1), x = omega/omega_g, p = mu/m0.
Exact facts checked here:
 (I)   E_p[x] = E_p[1/x] = 1/R, hence E_p[cosh ln x - 1] = 1/R - 1.
 (T1)  ratio window: p(x outside [1/lam, lam]) <= (1/R - 1)/(cosh ln lam - 1) = 2(1 - R)/(R(lam + 1/lam - 2)), lam > 1 (Markov on
       cosh ln x - 1); sharp as a supremum approached by outer three-atom measures; boundary atoms on {1/lam, 1, lam} with weights (q/2, 1 - q, q/2),
       q = (1/R - 1)/(cosh ln lam - 1), whenever q <= 1.
 (H)   hole: if mu has no weight in the open window omega_g (1 - d, 1 + d), 0 < d < 1, then R <= 1 - d^2/2 (E_p of
       (x - 1 + d)(x - 1 - d)/x >= 0); equality for two atoms at omega_g (1 -+ d).
 (G)   gap: if mu = mu1 + mu2 with m0 fractions 1 - eps, eps and every frequency ratio between the parts outside (1/r, r), then
       R^-2 - 1 >= eps (1 - eps)(r + 1/r - 2) (Cauchy-Schwarz within parts, t + 1/t >= r + 1/r across); equality for two atoms.
Checks: exact rational arithmetic for the identities and the extremal measures; random positive measures for validity (floating
point); the application uses the landed 8^3 forward-walking S = 0.4084 +- 0.0144 and the ceiling sqrt(m1 m_-1) = 0.4243 (an estimated
statement: R is a Monte Carlo estimate). Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import math
import random
import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 120
RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def moments(w, om):
    w, om = np.asarray(w, float), np.asarray(om, float)
    return (w / om).sum(), w.sum(), (w * om).sum()


# ---------------------------------------------------------------- (I) identities, exact (sympy rational measures with omega_g rational)
rng = random.Random(7)
okI = True
for _ in range(40):
    n = rng.randint(2, 6)
    w = [Fr(rng.randint(1, 9), rng.randint(1, 9)) for _ in range(n)]
    om = [Fr(rng.randint(1, 30), rng.randint(1, 10)) for _ in range(n)]
    mm1 = sum(a / b for a, b in zip(w, om)); m0 = sum(w); m1 = sum(a * b for a, b in zip(w, om))
    og = sp.sqrt(sp.Rational(m1) / sp.Rational(mm1)); Rr = sp.Rational(m0) / sp.sqrt(sp.Rational(m1) * sp.Rational(mm1))
    Ex = sum(sp.Rational(a) * sp.Rational(b) / og for a, b in zip(w, om)) / sp.Rational(m0)
    Exi = sum(sp.Rational(a) * og / sp.Rational(b) for a, b in zip(w, om)) / sp.Rational(m0)
    okI &= sp.simplify(Ex - 1 / Rr) == 0 and sp.simplify(Exi - 1 / Rr) == 0
check("(I) for 40 random rational measures, E_p[omega/omega_g] = E_p[omega_g/omega] = 1/R exactly (sympy), so E_p[cosh ln x - 1] = 1/R - 1", okI)

# ---------------------------------------------------------------- (T1) ratio window: exact sharpness, random validity
ok_sharp = True
rows = []
for Rq, lam in ((Fr(9, 10), Fr(2)), (Fr(24, 25), Fr(3)), (Fr(99, 100), Fr(3, 2)), (Fr(4, 5), Fr(5))):
    c = 1 / Rq; ch = (lam + 1 / lam) / 2
    q = (c - 1) / (ch - 1)
    if q > 1:
        continue
    w = [q / 2, 1 - q, q / 2]; om = [1 / lam, Fr(1), lam]
    mm1 = sum(a / b for a, b in zip(w, om)); m0 = sum(w); m1 = sum(a * b for a, b in zip(w, om))
    ok_sharp &= (m1 == mm1) and (m0 * m0 / (m1 * mm1) == Rq * Rq)        # omega_g = 1 and R exactly as set
    bound = (c - 1) / (ch - 1)
    ok_sharp &= (w[0] + w[2]) == bound
    assert sum(a for a, x in zip(w, om) if x < 1/lam or x > lam) == 0
    previous = Fr(0)
    for eps in (Fr(1, 10), Fr(1, 100), Fr(1, 1000)):
        outer = lam + eps
        qouter = (c - 1) / ((outer + 1/outer)/2 - 1)
        wo, xo = [qouter/2, 1-qouter, qouter/2], [1/outer, Fr(1), outer]
        ok_sharp &= 0 <= qouter <= 1 and sum(a*x for a,x in zip(wo,xo)) == c and sum(a/x for a,x in zip(wo,xo)) == c
        outside = sum(a for a,x in zip(wo,xo) if x < 1/lam or x > lam)
        ok_sharp &= outside == qouter and previous < qouter < bound
        previous = qouter
    rows.append(f"R = {Rq}, lam = {lam}: boundary mass {w[0]+w[2]} has closed-window outside mass zero; outer sequence approaches bound {bound}")
nrng = np.random.default_rng(11)
viol, ntest, worst = 0, 0, 0.0
for _ in range(20000):
    n = nrng.integers(2, 9)
    w = nrng.random(n) ** 3; om = np.exp(nrng.normal(0, nrng.uniform(0.05, 1.5), n))
    mm1, m0, m1 = moments(w, om); R = m0 / math.sqrt(m1 * mm1); og = math.sqrt(m1 / mm1)
    for lam in (1.2, 1.5, 2.0, 3.0, 10.0):
        b = 2 * (1 - R) / (R * (lam + 1 / lam - 2))
        if b >= 1:
            continue
        out = w[(om < og / lam) | (om > og * lam)].sum() / m0
        ntest += 1; viol += out > b * (1 + 1e-12); worst = max(worst, out / b)
check("(T1) ratio window: the fraction of S weight outside [omega_g/lam, lam omega_g] is at most 2(1 - R)/(R(lam + 1/lam - 2)); "
      "sharp as a supremum approached by outer three-atom rational measures; closed-window boundary countercontrol; no violation in random positive measures", ok_sharp and viol == 0,
      "; ".join(rows) + f"; random: {ntest} tests, {viol} violations, largest ratio to the bound {worst:.4f}")

# ---------------------------------------------------------------- (H) hole theorem
ok_h = True
for d in (Fr(1, 10), Fr(3, 10), Fr(1, 2)):
    a, b = 1 - d, 1 + d
    wa, wb = a / (2 - d), b / (2 + d)            # two atoms at 1 -+ d with omega_g = 1
    mm1 = wa / a + wb / b; m0 = wa + wb; m1 = wa * a + wb * b
    ok_h &= (m1 == mm1) and (m0 * m0 / (m1 * mm1) == (1 - d * d / 2) ** 2)
viol_h, nh = 0, 0
for _ in range(20000):
    n = nrng.integers(2, 9)
    w = nrng.random(n); om = np.exp(nrng.normal(0, 0.6, n))
    mm1, m0, m1 = moments(w, om); R = m0 / math.sqrt(m1 * mm1); og = math.sqrt(m1 / mm1)
    x = om / og
    d = float(np.min(np.abs(x - 1)))             # the largest open window about omega_g with no weight
    if 0 < d < 1:
        nh += 1; viol_h += R > 1 - d * d / 2 + 1e-12
check("(H) hole: no weight in omega_g (1 - d, 1 + d) forces R <= 1 - d^2/2; equality exactly for two atoms at omega_g (1 -+ d) "
      "(rational check at d = 1/10, 3/10, 1/2); no violation in random measures", ok_h and viol_h == 0, f"random: {nh} tests, {viol_h} violations")

# ---------------------------------------------------------------- (G) gap theorem
ok_g = True
for eps, r in ((Fr(1, 10), Fr(3)), (Fr(1, 4), Fr(2)), (Fr(1, 100), Fr(10))):
    w = [1 - eps, eps]; om = [Fr(1), r]
    mm1 = sum(a / b for a, b in zip(w, om)); m0 = sum(w); m1 = sum(a * b for a, b in zip(w, om))
    ok_g &= (m1 * mm1 / (m0 * m0)) - 1 == eps * (1 - eps) * (r + 1 / r - 2)
viol_g, ng = 0, 0
for _ in range(20000):
    n1, n2 = nrng.integers(1, 5), nrng.integers(1, 5)
    om1 = np.exp(nrng.normal(0, 0.3, n1)); r = math.exp(nrng.uniform(0.05, 2.5))
    om2 = om1.max() * r * np.exp(np.abs(nrng.normal(0, 0.5, n2)))      # every ratio across the parts >= r
    w1, w2 = nrng.random(n1), nrng.random(n2)
    mm1, m0, m1 = moments(np.r_[w1, w2], np.r_[om1, om2])
    eps = w2.sum() / m0
    ng += 1; viol_g += (m1 * mm1 / m0 ** 2 - 1) < eps * (1 - eps) * (r + 1 / r - 2) * (1 - 1e-12)
check("(G) gap: two parts with m0 fractions 1 - eps, eps and all cross ratios outside (1/r, r) satisfy R^-2 - 1 >= eps(1 - eps)(r + 1/r - 2); "
      "equality exactly for two atoms (rational check); no violation in random split measures", ok_g and viol_g == 0, f"random: {ng} tests, {viol_g} violations")

# ---------------------------------------------------------------- application: landed 8^3 estimates at k = pi/4
S, Se, CEIL = 0.4084, 0.0144, 0.4243
rows = []
for R in (S / CEIL, (S - Se) / CEIL):
    tail = {lam: 2 * (1 - R) / (R * (lam + 1 / lam - 2)) for lam in (1.5, 2.0, 3.0)}
    K = R ** -2 - 1
    emax = {r: (1 - math.sqrt(max(0.0, 1 - 4 * K / (r + 1 / r - 2)))) / 2 if 4 * K < r + 1 / r - 2 else 0.5 for r in (2, 3, 10)}
    rows.append(f"R = {R:.3f}: outside a factor 1.5 / 2 / 3 at most {tail[1.5]:.3f} / {tail[2.0]:.3f} / {tail[3.0]:.3f}; a hole of half-width "
                f"{math.sqrt(2 * (1 - R)):.3f} about omega_g is allowed; a minority band with every cross ratio to its complement outside the ratio window 2 / 3 / 10 carries at most "
                f"{emax[2]:.3f} / {emax[3]:.3f} / {emax[10]:.4f} of S")
check("application to the landed 8^3 estimates at k = pi/4 (forward-walking S = 0.4084 +- 0.0144, ceiling sqrt(m1 m_-1) = 0.4243, "
      "omega_g = sqrt(m1/m_-1) = 1.042 s): estimated bounds at R and at R minus one standard error (reported)", True,
      "; ".join(rows) + f"; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")

raise SystemExit(0 if all(RESULTS) else 1)
