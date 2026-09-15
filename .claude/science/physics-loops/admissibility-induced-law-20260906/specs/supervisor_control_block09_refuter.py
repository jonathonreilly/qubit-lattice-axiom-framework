"""Refuting pass, block 09 (supervisor, disjoint machinery).
R1: the dependence witness recomputed from block 08's product form on the 3x3x3 box (the conditional of the center (1,1,1)
    given all other sites, as a ratio of product-form values — no K_3-grouping formula), at (3,1,2), all sites +x except x+e1-e2.
R2: the (+++)/(---) pair witness recomputed the same way on the 3x3x3 box with the reflected predecessor structure.
R3: the joint law J on the 2x2 column: both marginals of J equal pi (consistency), and TV(J, J^T) recomputed from the
    orbit-lifted pi with the reversed transfer P*(v,w) = pi(w)P(w,v)/pi(v) (stochasticity of P* checked).
"""
from fractions import Fraction as F
from itertools import product
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[5] / "scripts"))
import importlib
r08 = importlib.import_module("admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_2026_09_15")
r09 = importlib.import_module("admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_2026_09_15")
M = 6
rule = r08.Rule((3, 1, 2))
sites = r08.box_sites((3, 3, 3))
center = (1, 1, 1)

def preds_signed(x, kappa):
    out = []
    for j in range(3):
        y = list(x); y[j] -= kappa[j]
        if all(0 <= c <= 2 for c in y):
            out.append(tuple(y))
    return out

def product_form(v: dict, kappa) -> F:
    w = F(1, M) if True else None
    # origin of the class: the corner site with no predecessors gets 1/6; every other site: prod K / K_k
    w = F(1)
    for x in sites:
        A = preds_signed(x, kappa)
        if not A:
            w *= F(1, M)
            continue
        for y in A:
            w *= rule.K[v[y]][v[x]]
        if len(A) == 2:
            w /= rule.K2[(v[A[0]], v[A[1]])]
        elif len(A) == 3:
            w /= rule.K3[(v[A[0]], v[A[1]], v[A[2]])]
    return w

def center_conditional(v: dict, kappa):
    ws = []
    for s in range(M):
        vv = dict(v); vv[center] = s
        ws.append(product_form(vv, kappa))
    Z = sum(ws)
    return [x / Z for x in ws]

# R1
base = {x: 0 for x in sites}
c0 = center_conditional(base, (1, 1, 1))
best = F(0)
for val in range(M):
    v = dict(base); v[(2, 0, 1)] = val  # x + e1 - e2 with x = (1,1,1)
    best = max(best, r08.tv(c0, center_conditional(v, (1, 1, 1))))
print("R1 dependence witness via the 3x3x3 product form:", best, "== runner literal:", best == r09.DEP_WITNESS_312)
# R2
offsets = {(0,1): (2,0,1), (0,2): (2,1,0), (1,0): (0,2,1), (1,2): (1,2,0), (2,0): (0,1,2), (2,1): (1,0,2)}  # x + e_i - e_j
vals = {(0,1): 0, (0,2): 0, (1,0): 2, (1,2): 1, (2,0): 2, (2,1): 1}  # the runner's witness (+x,+x,+y,-x,+y,-x) on sorted offsets? recompute by search below
best2 = F(0)
keys = sorted(offsets)
for assign in product(range(M), repeat=6):
    v = dict(base)
    for k, a in zip(keys, assign):
        v[offsets[k]] = a
    d = r08.tv(center_conditional(v, (1, 1, 1)), center_conditional(v, (-1, -1, -1)))
    if d > best2: best2 = d
print("R2 pair witness via the 3x3x3 product forms (search over 6^6):", best2, "== runner literal:", best2 == r09.PAIR_WITNESS_312)
# R3
states, pi = r09.stationary_plane_law(rule, (1, 1, 1))
P = {}
row_ok = True
for w in states:
    rs = F(0)
    for v in states:
        P[(w, v)] = r09.plane_transfer_class(rule, (1, 1, 1), w, v)
        rs += P[(w, v)]
    row_ok = row_ok and rs == 1
m1 = {v: sum(pi[w] * P[(w, v)] for w in states) for v in states}
marg_ok = all(m1[v] == pi[v] for v in states)
Pstar_rows_ok = all(sum(pi[w] * P[(w, v)] / pi[v] for w in states) == 1 for v in states)
tvd = sum(abs(pi[w] * P[(w, v)] - pi[v] * P[(v, w)]) for w in states for v in states) / 2
print("R3 rows of P sum to one:", row_ok, "; pi P = pi:", marg_ok, "; P* stochastic:", Pstar_rows_ok, "; TV(J,J^T) over ordered pairs /2 =", r08.dec(tvd), "== runner:", tvd == r09.irreversibility(rule, (1,1,1), states, pi))
