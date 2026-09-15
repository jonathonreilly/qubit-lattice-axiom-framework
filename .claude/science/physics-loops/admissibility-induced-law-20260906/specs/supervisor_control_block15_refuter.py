"""Refuting pass, block 15 (supervisor seat, disjoint machinery from the runner's checks):
(R1) the criterion by a second implementation that tracks, for each site, its recorded neighbours as a list at formation time
     (no set arithmetic), compared with exact equality on every order of the isolated path, domino and plaquette and on the
     star classes k = 0, 1, 2 (isolated);
(R2) the star's isolated joint law by the tree factorization mu(v) = (1/6) prod_leaves K(v_center, v_leaf) instead of the
     normalized edge product, and the center-first sequential law by hand (the same product), compared with the runner's laws;
(R3) the star in the mixed environment: the center-first law by an order-by-order recursion over the values of the center
     (sum over the center's value of the leaves' independent conditionals), compared with the runner's seq_law;
(R4) the normalizer lemma at (3,1,2) by direct summation with integers for k = 2..8 (beyond the runner's symbolic range).
Run from the pack: the runner is imported from the repository's scripts/ directory."""
import importlib
import random
import sys
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
r15 = importlib.import_module("admissibility_rule_formation_unit_clause_witness_sequential_equals_joint_iff_criterion_2026_09_15")
M = 6
def violates2(U, vO, order):
    Uset = set(U)
    recorded = []
    for x in order:
        rec_inside = 0; rec_total = 0
        for y in r15.nbrs(x):
            if y in recorded:
                rec_inside += 1; rec_total += 1
            elif (y not in Uset) and (y in vO):
                rec_total += 1
        if rec_inside >= 1 and rec_total >= 2:
            return True
        recorded.append(x)
    return False
ok1 = True
for sites in ([(0,0,0),(1,0,0)], [(0,0,0),(1,0,0),(2,0,0)], [(0,0,0),(1,0,0),(1,1,0),(0,1,0)]):
    U, O = r15.make_unit(sites)
    J = r15.joint_law(U, {})
    for order in permutations(U):
        eq = r15.tv(r15.seq_law(U, {}, order), J) == 0
        ok1 = ok1 and (eq == (not violates2(U, {}, order))) and (violates2(U, {}, order) == r15.violates(U, {}, order))
star_U, star_O = r15.make_unit([r15.CENTER] + r15.LEAVES)
Jstar = r15.joint_law(star_U, {})
for k in (0, 1, 2):
    order = r15.LEAVES[:k] + [r15.CENTER] + r15.LEAVES[k:]
    eq = r15.tv(r15.seq_law(star_U, {}, order), Jstar) == 0
    ok1 = ok1 and (eq == (not violates2(star_U, {}, order)))
print("R1 second implementation of the criterion agrees with exact equality on every order of the domino, path, plaquette and the star classes k = 0,1,2:", ok1)
# R2 tree factorization of the star's joint law and the center-first sequential law by hand
tree = {}
for v in product(range(M), repeat=7):
    w = F(1, 6)
    for i in range(1, 7):
        w *= F(r15.PHI[v[i]][v[0]], r15.Z1)
    tree[v] = w
seq0 = r15.seq_law(star_U, {}, [r15.CENTER] + r15.LEAVES)
print("R2 tree factorization equals the runner's joint law and the center-first sequential law on all 6^7 patterns:", all(tree[v] == Jstar[v] for v in tree), all(tree[v] == seq0[v] for v in tree))
# R3 environment star, center-first, by recursion over the center's value
random.seed(3)
vO_mixed = {y: random.randrange(M) for y in star_O}
Je = r15.joint_law(star_U, vO_mixed)
seq_env = r15.seq_law(star_U, vO_mixed, [r15.CENTER] + r15.LEAVES)
rec = {}
for v in product(range(M), repeat=7):
    w = F(1, 6)  # the center has no outside neighbours: its six neighbours are the leaves
    for i, leaf in enumerate(r15.LEAVES, start=1):
        recs = [v[0]] + [vO_mixed[y] for y in r15.nbrs(leaf) if y in vO_mixed]
        w *= r15.cond(tuple(sorted(recs)), v[i])
    rec[v] = w
print("R3 order-by-order recursion equals the runner's center-first environment law on all patterns:", all(rec[v] == seq_env[v] for v in rec), "; TV to the joint law:", r15.tv(rec, Je) > 0)
# R4 lemma by integers for k = 2..8
ok4 = True
for k in range(2, 9):
    same = sum(r15.PHI[s][0] ** k for s in range(M))
    anti = sum(r15.PHI[s][1] * r15.PHI[s][0] ** (k - 1) for s in range(M))
    pred = (3 - 1) * (3 ** (k - 1) - 1 ** (k - 1))
    ok4 = ok4 and (same - anti == pred) and same > anti
print("R4 integer form of the lemma Z_1^k (K_k(b..b) - K_k(-b,b..b)) = (p-q)(p^(k-1) - q^(k-1)) for k = 2..8:", ok4)
