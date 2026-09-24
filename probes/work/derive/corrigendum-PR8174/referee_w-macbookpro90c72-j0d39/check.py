"""Independent confirmation of the PR 8174 corrigendum.

Own six-axis weights and own census. The author's script is not called.
"""
import itertools
import subprocess
import sys
from fractions import Fraction as F

import sympy as sp

FAILS = []
AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def want(label, ok):
    if not ok:
        FAILS.append(label)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


def phi(i, j, w):
    dot = AX[i][0] * AX[j][0] + AX[i][1] * AX[j][1] + AX[i][2] * AX[j][2]
    return w[0] if dot == 1 else w[1] if dot == -1 else w[2]


def K(s, trip, w):
    weights = [phi(v, trip[0], w) * phi(v, trip[1], w) * phi(v, trip[2], w) for v in range(6)]
    total = sum(weights)
    if isinstance(weights[0], sp.Basic):
        return weights[s] / total
    return F(weights[s], total)


def dev(w):
    return (
        1 - K(0, (0, 0, 0), w),
        1 - K(0, (0, 0, 1), w),
        1 - K(0, (0, 0, 2), w),
    )


p, q, r = sp.symbols("p q r", positive=True)
d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
menu = [1 - K(0, trip, (p, q, r)) for trip in ((0, 0, 0), (0, 0, 1), (0, 0, 2))]
ok = all(sp.simplify(x - y) == 0 for x, y in zip(menu, (d1, d2, d3)))
for w in ((1, 2, 1), (5, 2, 4), (3, 1, 2)):
    got = dev(w)
    exp = tuple(sp.together(x.subs({p: w[0], q: w[1], r: w[2]})) for x in (d1, d2, d3))
    ok = ok and all(a == F(b.p, b.q) for a, b in zip(got, exp))
want("A1 the three deviations equal 1 minus the menu conditional, symbolically and at three triples", ok)

g = p ** 2 * r + p * q ** 2 + p * q * r + 2 * p * r ** 2 - q ** 3 - 4 * r ** 3
den2 = (p ** 3 + q ** 3 + 4 * r ** 3) * (p ** 2 * q + p * q ** 2 + 4 * r ** 3)
den3 = (p ** 3 + q ** 3 + 4 * r ** 3) * (p ** 2 + p * r + q ** 2 + q * r + 2 * r ** 2)
e21 = sp.together(d2 - d1 - p ** 2 * (p - q) * (p * q ** 2 + q ** 3 + 4 * r ** 3) / den2)
e31 = sp.together(d3 - d1 - p ** 2 * g / den3)
want("A2 d2-d1 has the sign of p-q and d3-d1 has the sign of g", sp.simplify(e21) == 0 and sp.simplify(e31) == 0)

D = dev((1, 2, 1))
ok = D == (F(12, 13), F(4, 5), F(9, 10)) and g.subs({p: 1, q: 2, r: 1}) == -3
ok = ok and D[0] > max(D[1:]) and D[1] < max(D[1:])
counts = {}
exact = True
for N in (7, 8):
    bad = []
    for P, Q, R in itertools.product(range(1, N + 1), repeat=3):
        d = dev((P, Q, R))
        fails = d[0] > max(d[1], d[2])
        marked = P < Q and (P ** 2 * R + P * Q ** 2 + P * Q * R + 2 * P * R ** 2 - Q ** 3 - 4 * R ** 3) < 0
        exact = exact and fails == marked
        if fails:
            bad.append((P, Q, R))
    counts[N] = len(bad)
    exact = exact and all(Q > P for P, Q, R in bad)
ok = ok and counts == {7: 127, 8: 194} and exact
want("A3 (1,2,1) is 12/13 > 9/10, and the failing triples are exactly 127 and 194, all with q > p", ok)

pts = [(1, 2, 1), (1, 3, 1), (2, 5, 2), (5, 2, 4), (4165, 1, 2), (2085, 1, 1), (8330, 2, 4), (6247, 1, 3)]
ok = True
for w in pts:
    eps = max(dev(w))
    for trip in itertools.product(range(6), repeat=3):
        na = sum(v == 0 for v in trip)
        if na == 3:
            ok = ok and (1 - K(0, trip, w)) == dev(w)[0]
        elif na == 2:
            ok = ok and (1 - K(0, trip, w)) <= eps
want("A4 with eps = max(d1,d2,d3), every two-a triple dissents by at most eps at the tested weights", ok)

used = [
    (4165, 1, 2), (2085, 1, 1), (8330, 2, 4), (6247, 1, 3), (4150, 1, 2),
    (453, 1, 2), (368, 1, 2), (2921, 1, 2), (1464, 1, 1), (5841, 2, 4),
    (4380, 1, 3), (405, 1, 2), (11, 1, 2),
]
ok = all(P >= Q and dev(w)[0] <= max(dev(w)[1:]) for w in used for P, Q, R in [w])
want("A5 every listed certificate, ceiling and stake has p >= q, so d1 <= max(d2,d3)", ok)

note = "docs/ADMISSIBILITY_RULE_SIX_AXIS_FORMATION_THRESHOLD_LIFTED_BY_A_TWO_LEVEL_DOMINATION_SEEDS_AND_AMPLIFIED_NODES_IN_THE_EXPLANATION_TREE_BOUNDED_THEOREM_NOTE_2026-09-16.md"
body = subprocess.run(["git", "show", f"cc7662e1:{note}"], capture_output=True, text=True).stdout.splitlines()
needles = {
    99: "ε₂ = max(d_2, d_3)",
    107: "d_1 ≤ max(d_2, d_3)",
    109: "d_1 ≤ d_3",
    193: "max(d_2, d_3)",
}
ok = all(n <= len(body) and needles[n] in body[n - 1] for n in needles)
want("A5 block 30's note at cc7662e1 still states the two-deviation max on lines 99, 107, 109 and 193", ok)

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: fails at " + FAILS[0])
    sys.exit(1)
print(
    "HIT: confirmed - d1 <= max(d2, d3) holds exactly when p >= q or g >= 0, "
    "with g = p^2 r + p q^2 + p q r + 2 p r^2 - q^3 - 4 r^3. "
    "It fails at (1,2,1), where (d1,d2,d3) = (12/13, 4/5, 9/10), and on 127 triples in {1..7}^3. "
    "The repair eps = max(d1,d2,d3) equals max(d2,d3) whenever p >= q."
)
print(
    "SUMMARY: confirmed the corrigendum. The original coupling fails at (1,2,1) because 12/13 > 9/10. "
    "Every listed weight point of blocks 30-33 has p >= q, so those certificates are unchanged. "
    "Block 30's note at cc7662e1 still writes the two-deviation max."
)
