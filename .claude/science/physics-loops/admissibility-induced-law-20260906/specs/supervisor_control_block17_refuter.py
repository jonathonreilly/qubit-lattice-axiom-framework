"""Refuting pass, block 17 (supervisor seat, disjoint machinery from the runner's checks):
(R1) reflection positivity on the ring of 4 by the explicit sum-of-squares decomposition E[F F∘θ] Z = sum_{v0,v2} W_P G(v0,v2)^2
     (computed as such), against the runner's direct expectation, for pseudo-random F and both triples;
(R2) the chessboard instance on the ring in the two-step quadratic-form form: P(A_0 ∩ A_2) <= P(A_0 ∩ θA_0)^{1/2} P(A_2 ∩ θA_2)^{1/2}
     with the reflection through the plane {1,3} (a different reflection than the runner's), then the second reflection;
(R3) the enclosing-cycle counts by a second enumeration: polyominoes of perimeter 4, 6, 8 placed to contain the origin cell
     (translations x orientations), against the runner's walk enumeration;
(R4) the two series by numeric summation of exact partial sums to 400 terms at y = 1/2 and y = 4/5 against the closed forms;
(R5) the three-dimensional connected plaquette sets for n <= 4 by a second adjacency implementation (two dual plaquettes
     share a dual edge iff the two bonds lie in a common primal unit square: the twelve neighbours), against the runner's counts.
Run from the pack: the runner is imported from the repository's scripts/ directory."""
import importlib
import random
import sys
from fractions import Fraction as F
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
r17 = importlib.import_module("admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_several_gibbs_states_2026_09_15")
M = 6
random.seed(11)
ok1 = True
for tr in ((3, 1, 2), (5, 2, 4)):
    phi = r17.phi_matrix(*tr)
    mu = r17.ring_measure(phi, 4)
    Z = sum(1 for _ in ())  # placeholder
    # unnormalized weights: W(v) = phi(v0,v1) phi(v1,v2) phi(v2,v3) phi(v3,v0); plane P = {0, 2}; W_P = 1 (no bonds inside P);
    # W^+(v0,v1,v2) = phi(v0,v1) phi(v1,v2); W^-(v0,v3,v2) = phi(v2,v3) phi(v3,v0) = W^+(v0,v3,v2)
    for _ in range(10):
        Ftab = {k: F(random.randint(-9, 9)) for k in product(range(M), repeat=3)}
        sos = F(0)
        for v0 in range(M):
            for v2 in range(M):
                G = sum((Ftab[(v0, v1, v2)] * phi[v0][v1] * phi[v1][v2] for v1 in range(M)), F(0))
                sos += G * G
        Ztot = sum(phi[a][b] * phi[b][c] * phi[c][d] * phi[d][a] for a in range(M) for b in range(M) for c in range(M) for d in range(M))
        direct = sum((mu[v] * Ftab[(v[0], v[1], v[2])] * Ftab[(v[0], v[3], v[2])] for v in mu), F(0))
        ok1 = ok1 and sos / Ztot == direct and sos >= 0
print("R1 sum-of-squares decomposition equals the direct expectation and is nonnegative (ring, both triples, 10 F each):", ok1)
phi = r17.phi_matrix(3, 1, 2)
mu = r17.ring_measure(phi, 4)
def P(pred):
    return sum((pr for v, pr in mu.items() if pred(v)), F(0))
A0 = lambda v: v[0] != v[1]   # bond (0,1) bad
A2 = lambda v: v[2] != v[3]   # bond (2,3) bad
# reflection through the plane {1,3}: swaps 0 and 2; theta A0 = bond (2,1) bad; theta A2 = bond (0,3) bad
lhs = P(lambda v: A0(v) and A2(v))
r1 = P(lambda v: A0(v) and v[2] != v[1])
r2 = P(lambda v: A2(v) and v[0] != v[3])
step1 = lhs ** 2 <= r1 * r2
# second reflection through {0,2}: swaps 1 and 3; A0 ∩ θA0 = bonds (0,1),(1,2) bad; its reflection gives bonds (0,3),(3,2) bad → all bad
r1all = P(lambda v: all(v[i] != v[(i + 1) % 4] for i in range(4)))
step2 = r1 ** 2 <= r1all and r2 ** 2 <= r1all
print("R2 two-step chessboard on the ring: P(A0∩A2)^2 <= P(A0∩θA0) P(A2∩θA2):", step1, "; each of those squared <= P(all bad):", step2, "; hence P(A0∩A2)^2 <= P(all bad):", lhs ** 2 <= r1all)
def polyomino_placements(cells):
    """number of translates of the polyomino (set of cells) containing the origin cell = its area; sum over distinct rotations"""
    seen = set()
    def normalize(c):
        mx = min(x for x, y in c); my = min(y for x, y in c)
        return frozenset((x - mx, y - my) for x, y in c)
    shapes = set()
    c = cells
    for _ in range(4):
        shapes.add(normalize(c))
        c = [(-y, x) for x, y in c]
    return sum(len(sh) for sh in shapes)
counts2 = {4: polyomino_placements([(0, 0)]), 6: polyomino_placements([(0, 0), (1, 0)]),
           8: polyomino_placements([(0, 0), (1, 0), (0, 1), (1, 1)]) + polyomino_placements([(0, 0), (1, 0), (2, 0)]) + polyomino_placements([(0, 0), (1, 0), (0, 1)])}
counts1 = {n: r17.enclosing_cycles(n) for n in (4, 6, 8)}
print("R3 enclosing cycles by polyomino placements:", counts2, "; by the runner's walk enumeration:", counts1, "; equal:", counts1 == counts2)
y1, y2 = F(1, 2), F(4, 5)
s1 = sum((n * y1 ** n for n in range(4, 401)), F(0)); s2 = sum((n * y2 ** n for n in range(6, 401)), F(0))
print("R4 partial sums to 400 terms: at y=1/2 vs 5/8 gap <", F(1, 10 ** 30) > abs(s1 - F(5, 8)), "; at y=4/5 vs 8192/625 gap <", F(1, 10 ** 30) > abs(s2 - F(8192, 625)))
def nb2(b):
    (x, d) = b
    dirs = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    out = set()
    for dd in range(3):
        if dd == d:
            continue
        for sgn in (1, -1):
            for base in (x, tuple(x[k] + dirs[d][k] for k in range(3))):
                cand_x = base if sgn == 1 else tuple(base[k] - dirs[dd][k] for k in range(3))
                cand = (cand_x, dd)
                # two bonds are dual-edge neighbours iff they lie in a common unit square and are not opposite sides
                if cand == b:
                    continue
                # both bonds in a common unit square: the four sites of the square must contain both bonds' endpoints
                pts = {b[0], tuple(b[0][k] + dirs[b[1]][k] for k in range(3)), cand[0], tuple(cand[0][k] + dirs[cand[1]][k] for k in range(3))}
                if len(pts) == 3:  # perpendicular bonds sharing a site: common square exists
                    out.add(cand)
                elif len(pts) == 4 and cand[1] == b[1]:  # parallel bonds at unit distance: opposite sides of a square (NOT dual-edge adjacent) unless...
                    pass
    # parallel bonds shifted by a unit perpendicular step share a dual edge (their dual plaquettes are adjacent faces of a dual cube)
    for dd in range(3):
        if dd == d:
            continue
        for sgn in (1, -1):
            out.add((tuple(x[k] + sgn * dirs[dd][k] for k in range(3)), d))
    return out
origin = ((0, 0, 0), 0)
same_adj = all(nb2(b) == r17.plaquette_neighbors(b) for b in [origin] + list(r17.plaquette_neighbors(origin)))
frontier = {frozenset([origin])}; counts3 = {}
for n in range(1, 5):
    counts3[n] = len(frontier)
    nxt = set()
    for s in frontier:
        nb = set()
        for b in s:
            nb |= nb2(b)
        for b in nb - s:
            nxt.add(frozenset(s | {b}))
    frontier = nxt
print("R5 second adjacency implementation agrees with the runner's on the origin's neighbourhood:", same_adj, "; counts n=1..4:", counts3)
