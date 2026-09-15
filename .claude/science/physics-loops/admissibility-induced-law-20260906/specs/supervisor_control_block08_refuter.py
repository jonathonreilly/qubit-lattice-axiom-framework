"""Refuting pass (supervisor, disjoint machinery), block 08.
R1: the 2x2 transfer's TV at (3,1,2) by a different route — the cube law's marginal on the plane x1 = 1 (integer-weighted
    enumeration over 6^8, independent of the fraction transfer code) against the 2D law; the identity Q2a says the marginal is mu P.
R2: c_3 at (3,1,2) by the integer phi formulation and the TV identity sum of positive parts (not the fraction kernels).
R3: the stationary 2x2 law by power iteration of the orbit quotient (40 steps) vs the exact solve: row of Q^40 vs pi.
R4: the influence bound's path count on the cube: N(000,111) = 6 by explicit path enumeration.
R5: the third difference identity for a genuinely pair-additive F (control): ratio 1.
"""
from fractions import Fraction as F
from itertools import product, permutations
from math import lcm
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[5] / "scripts"))
import importlib
run = importlib.import_module("admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_2026_09_15")

M = 6
rule = run.Rule((3, 1, 2))
# R1
sites = run.box_sites((2, 2, 2)); idx = {s: i for i, s in enumerate(sites)}
phi, Z2, Z3 = rule.phi, rule.Z2, rule.Z3
l2 = 1
for v in Z2.values(): l2 = lcm(l2, v)
l3 = 1
for v in Z3.values(): l3 = lcm(l3, v)
L = M * rule.Z1 ** 3 * l2 ** 3 * l3
edges = [(idx[y], idx[x]) for x in sites for y in run.preds(x)]
two = [(idx[run.preds(x)[0]], idx[run.preds(x)[1]]) for x in sites if len(run.preds(x)) == 2]
three = [(idx[run.preds(x)[0]], idx[run.preds(x)[1]], idx[run.preds(x)[2]]) for x in sites if len(run.preds(x)) == 3]
plane1 = [idx[(1, 0, 0)], idx[(1, 0, 1)], idx[(1, 1, 0)], idx[(1, 1, 1)]]  # (x2,x3) = 00, 01, 10, 11
marg = {}
for v in product(range(M), repeat=8):
    num = 1
    for a, b in edges: num *= phi[v[b]][v[a]]
    den = M * rule.Z1 ** 3
    for a, b in two: den *= Z2[(v[a], v[b])]
    for a, b, c in three: den *= Z3[(v[a], v[b], v[c])]
    key = tuple(v[i] for i in plane1)
    marg[key] = marg.get(key, 0) + num * (L // den)
mu = run.mu_2x2(rule)
tvd = sum(abs(F(marg.get(k, 0), L) - mu[k]) for k in mu) / 2
print("R1 TV(cube marginal on plane 1, mu_2D) =", tvd, "== note literal:", tvd == F(356696849, 806187919680))
# R2
def cond_int(rec):
    k = len(rec)
    w = [1] * M
    for a in rec:
        w = [w[s] * phi[s][a] for s in range(M)]
    Z = sum(w)
    return [F(x, Z) for x in w]
best = F(0)
for rec in product(range(M), repeat=3):
    base = cond_int(rec)
    for i in range(3):
        for a2 in range(M):
            if a2 == rec[i]: continue
            r2 = list(rec); r2[i] = a2
            other = cond_int(tuple(r2))
            d = sum(max(x - y, 0) for x, y in zip(base, other))  # TV as the sum of positive parts
            best = max(best, d)
print("R2 c_3 by positive parts / integer phi =", best, "== 27/110:", best == F(27, 110))
# R3
states, orbit_of, reps, sizes = run.orbits_2x2()
n = len(reps)
Q = [[F(0)] * n for _ in range(n)]
for o, w in enumerate(reps):
    for v in states:
        Q[o][orbit_of[v]] += run.plane_transfer(rule, w, v)
pi_exact = run.solve_stationary(Q)
row = [F(1) if j == 0 else F(0) for j in range(n)]
for _ in range(40):
    row = [sum(row[k] * Q[k][j] for k in range(n)) for j in range(n)]
gap = max(abs(a - b) for a, b in zip(row, pi_exact))
print("R3 power iteration (40 steps) vs exact solve: max |diff| < 10^-12:", gap < F(1, 10**12), "(gap numerator digits", len(str(gap.numerator)), "denominator digits", len(str(gap.denominator)), ")")
# R4
def paths(z, x):
    if z == x: return 1
    return sum(paths(tuple(z[i] + (1 if j == i else 0) for i in range(3)), x) for j in range(3) if z[j] < x[j])
print("R4 N(000,111) =", paths((0, 0, 0), (1, 1, 1)), "(expected 6)")
# R5
g = {(a, b): F(phi[a][b], 7) for a in range(M) for b in range(M)}
Fpa = lambda a, b, c: g[(a, b)] + g[(b, c)] + g[(a, c)]
x, y, z = 0, 2, 4
alt = Fpa(x,x,x) - Fpa(y,x,x) - Fpa(x,y,x) + Fpa(y,y,x) - Fpa(x,x,z) + Fpa(y,x,z) + Fpa(x,y,z) - Fpa(y,y,z)
print("R5 alternating sum of a pair-additive F =", alt, "(expected 0)")
