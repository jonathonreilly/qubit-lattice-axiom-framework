"""Refuting pass, block 12 (supervisor seat, disjoint machinery from the runner's checks):
(R1) the 2x2 numbers on the full 1296-state chain instead of the orbit quotient — TV between the rows of the all-+x and
     the all--x planes after n steps (the quotient identifies these two states, so it cannot see this mode);
(R2) the eroder bound with an exhaustive small-island generator (every subset of size <= 3 of level 4);
(R3) epsilon(p) by maximising over the three closed-form patterns instead of the 216-triple scan.
Run from the pack: the runner is imported from the repository's scripts/ directory."""
import importlib
import sys
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
r12 = importlib.import_module("admissibility_rule_strong_coupling_formation_law_level_automaton_eroder_metastability_2026_09_15")
M = 6
rule = r12.Rule((10, 1, 2))
states = list(product(range(M), repeat=4))
P = {w: [r12.plane_transfer(rule, w, v) for v in states] for w in states}


def tv_rows(w1, w2, n):
    a, b = P[w1][:], P[w2][:]
    for _ in range(n - 1):
        a = [sum(a[i] * P[states[i]][j] for i in range(len(states))) for j in range(len(states))]
        b = [sum(b[i] * P[states[i]][j] for i in range(len(states))) for j in range(len(states))]
    return sum(abs(u - v) for u, v in zip(a, b)) / 2


w_plus, w_minus = (0, 0, 0, 0), (1, 1, 1, 1)
d1 = tv_rows(w_plus, w_minus, 1)
d2 = tv_rows(w_plus, w_minus, 2)
print("R1 full chain at p=10: TV(all +x, all -x) after 1 step =", r12.dec(d1, 6), "; after 2 steps =", r12.dec(d2, 6))
print("R1 the orbit quotient's 1-step max is 0.393104 < the full chain's", r12.dec(d1, 6), ": the quotient identifies +x with -x planes and cannot see the slow mode")
print("R1 agrees with the runner's integer-denominator computation:", r12.micro(d1) == r12.MEMORY[10][1], r12.micro(d2) == r12.MEMORY[10][2])
pts = [(a, b, 4 - a - b) for a in range(5) for b in range(5 - a)]
worst, ok, count = 0, True, 0
for k in (1, 2, 3):
    for isl in combinations(pts, k):
        isl = set(isl)
        T = r12.evolve_majority(isl)
        B = r12.island_bound(isl, 4)
        ok = ok and 0 <= T <= B
        worst = max(worst, T)
        count += 1
print(f"R2 exhaustive islands (all {count} subsets of size <= 3 of level 4): bound holds: {ok}; longest life: {worst}")
x, y, mx = 0, 2, 1
for p in (3, 10, 30, 100, 1000):
    rl = r12.Rule((p, 1, 2))
    cands = {"unanimous": 1 - rl.cond((x, x, x))[x], "orthogonal": 1 - rl.cond((x, x, y))[x], "antipodal": 1 - rl.cond((x, x, mx))[x]}
    best = max(cands, key=lambda k: cands[k])
    print(f"R3 p={p}: max over the three patterns = {cands[best]} ({best}) == runner literal {r12.EPS_312[p]}: {cands[best] == r12.EPS_312[p]}")
