#!/usr/bin/env python3
"""J:derive:formation-events-for-amplitudes-of-negative-energy:a2 - worker w-jonathonsmac4f50-jcb3e (claude-opus-5-5).

Definitions (blocks 60, 67, 71; open PRs #8590, #8598, #8603; supplied, not adopted): bodies at rest in a box with held walls;
lengths chi = 1 + sum_x Q_x g_x (g_x the unit-source potential of site x, g = (-Delta)^(-1) with walls at 0), Q_x chi_x = mu_x =
m_x/(8K); ledger = 8K sum Q; rates' operator L = -Delta + diag(Q/chi) on interior sites, walls held; the field exists with
positive rates iff chi > 0 and L is positive definite (block 71 T3(d)); one body: admissible iff Q > -1/(2 g_0) (block 71 T3).
Block 67 T1: one record at y keeps the ledger iff Q' = sum_x Q_x.  Box: the 3^3 interior of a 5^3 box (block 71's 27 sites).
Exact arithmetic: sympy rationals.
"""
import itertools

import sympy as sp

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


n = 3
S = list(itertools.product(range(n), repeat=3))
idx = {s: i for i, s in enumerate(S)}
NBR = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
Lap = sp.zeros(27, 27)                       # -Delta on the interior, walls held at zero
for s in S:
    i = idx[s]
    Lap[i, i] = 6
    for d in NBR:
        t = (s[0] + d[0], s[1] + d[1], s[2] + d[2])
        if t in idx:
            Lap[i, idx[t]] = -1
g = Lap.inv()
gd = [g[i, i] for i in range(27)]
thr = [-1 / (2 * v) for v in gd]


def admissible(Q):
    chi = sp.ones(27, 1) + g * Q
    if min(chi) <= 0:
        return False, chi, None
    L = Lap + sp.diag(*[Q[i] / chi[i] for i in range(27)])
    minors = [L[:k, :k].det() for k in range(1, 28)]
    return all(mm > 0 for mm in minors), chi, L


# ================================================================ A1 a spread negative amplitude below every threshold, with its own field
q = sp.Rational(1, 5)
Q = sp.Matrix([-q] * 27)
ok_field, chi, L = admissible(Q)
sumQ = sum(Q)
ok = ok_field
ok &= all(-q > t for t in thr)                                  # each charge on its own admissible branch
ok &= all(sumQ < t for t in thr)                                # the total below the threshold at EVERY site
N_rates = L.LUsolve(Lap * sp.ones(27, 1)) if L is not None else None   # rates: L N = (boundary term) = -Delta 1 on the interior
check('A1', ok, "EXACT (27 interior sites of a 5^3 box, rational Green function): the amplitude with Q_x = -1/5 at every site "
      "has each charge on its own admissible branch (-1/5 > -1/(2 g_xx)), its own static field exists with positive lengths "
      "and positive definite L = -Delta + Q/chi (all 27 leading minors positive), and its total -27/5 lies below "
      "-1/(2 g_yy) at EVERY site y (the most negative threshold is -952/353 = -2.697 at the corners)",
      f"g_yy from {min(gd)} to {max(gd)}; min chi = {min(chi)}; thresholds from {min(thr)} to {max(thr)}")

# ================================================================ A2 the bound: every record of an admissible negative field has Q_i > -1/(2 g_ii)
# proof in ATTEMPT step 3; here: the lemma's two inequalities on the example, and single records at every site
ok = True
for i in range(27):
    gi = g[:, i]
    val = (gi.T * L * gi)[0]                                    # g_i^T L g_i = g_ii + sum_x (Q_x/chi_x) g_i(x)^2
    ok &= sp.simplify(val - (gd[i] + sum(Q[x] / chi[x] * gi[x] ** 2 for x in range(27)))) == 0
    ok &= chi[i] <= 1 + Q[i] * gd[i]
single = []
for y in range(27):
    Qs = sp.zeros(27, 1)
    Qs[y] = sumQ
    a, _, _ = admissible(Qs)
    single.append(a)
ok &= not any(single)
check('A2', ok, "PROVED + EXACT: in any field with all charges <= 0, positive definiteness tested on g_i gives "
      "g_ii + sum_x (Q_x/chi_x) g_i(x)^2 > 0, hence 1 + (Q_i/chi_i) g_ii > 0, and chi_i <= 1 + Q_i g_ii gives "
      "Q_i > -1/(2 g_ii) for EVERY record of an admissible negative field (block 71 T3's bound, now for many bodies); so no "
      "single record of charge -27/5 is admissible at any of the 27 sites (checked directly): the amplitude of A1 has no "
      "ledger-keeping single record - the supervisor's observation holds, and the unit's HIT conditions are not met")

# ================================================================ B1 the best single record, and what the walls see
Kc = sp.symbols('K', positive=True)
ycorner = min(range(27), key=lambda y: thr[y])
bound = thr[ycorner]
jump_min = 8 * Kc * (bound - sumQ)
# clocks: flux of 1 - N into the walls = sum_x P_x with P_x = Q_x N_x (block 67 T3(a)); single record P' = Q'/(1 + 2Q' g_yy)
Qp = sp.symbols("Qp", real=True)
Pp = Qp / (1 + 2 * Qp * gd[ycorner])
lim = sp.limit(Pp, Qp, bound, dir='+')
spread_flux = sum(Q[x] * N_rates[x] for x in range(27))
ok = sp.simplify(jump_min - 8 * Kc * (sp.Rational(27, 5) - sp.Rational(952, 353))) == 0 and lim == -sp.oo
ok &= all(N_rates[x] > 0 for x in range(27))
check('B1', ok, "EXACT: the best single record sits where the threshold is lowest (a corner, -952/353) and must stay above "
      "it, so the ledger RISES by more than 8K(27/5 - 952/353) = 8K x 4771/1765 (about 21.6 K); the walls see the lengths' "
      "monopole jump from sum Q = -27/5 to Q' > -952/353 (block 67 T2(a) with h = 1), and the clocks' flux "
      "P' = Q'/(1 + 2 Q' g_yy) runs to minus infinity as Q' approaches the bound (the zero mode of block 71 T3): the record "
      "that is best for the ledger is singular for the clocks; the spread amplitude itself has positive rates and a finite "
      "clock flux", f"spread amplitude: min rate {min(N_rates)}, clock flux sum P = {spread_flux} = {float(spread_flux):.4f}")

# ================================================================ C1 how many records: n > 2 g_min |sum Q|, attained
nmin_bound = 2 * min(gd) * abs(sumQ)
three = [idx[(0, 0, 2)], idx[(2, 0, 0)], idx[(2, 2, 2)]]
Q3 = sp.zeros(27, 1)
for i in three:
    Q3[i] = sumQ / 3
ok3, chi3, _ = admissible(Q3)
ok = ok3 and nmin_bound > 2 and nmin_bound < 3
check('C1', ok, "PROVED (A2's bound summed) + EXACT: an admissible negative field of n records carries |sum Q| < "
      "sum_i 1/(2 g_ii) <= n/(2 g_min), so keeping the ledger of the amplitude needs n > 2 g_min |sum Q| = "
      f"{float(nmin_bound):.4f}, i.e. at least 3 records; three records of charge -9/5 at three corners, (0,0,2), (2,0,0) and "
      "(2,2,2), ARE admissible (all minors positive): the minimum is exactly 3; in general the count grows like "
      "2 g_min |sum Q|, while a positive amplitude always needs just one",
      f"2 g_min |sum Q| = {nmin_bound}; three-record field min chi = {min(chi3)}")

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print("SUMMARY: PROVED (for the curvature member with held walls, all charges <= 0): every record of an admissible negative "
      "field has Q_i > -1/(2 g_ii) (positive definiteness of -Delta + Q/chi tested on g_i), so a spread negative amplitude "
      "with sum Q below -1/(2 g_yy) at every y - exact example: -1/5 at each of the 27 interior sites of a 5^3 box, own field "
      "admissible - has no ledger-keeping single record; the best single record raises the ledger by more than "
      "8K(|sum Q| - 1/(2 g_min)) and drives the clocks' wall flux to minus infinity at the bound; n > 2 g_min |sum Q| records "
      "are needed and 3 suffice in the example")
