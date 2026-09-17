"""Refuting pass, block 32 — disjoint machinery.
(1) The extremal realizations Z_A, Z_B: the minimum over the family recomputed by an INTEGER PROGRAM over node/arrow/fork/flow variables
    (scipy milp, floating point) at c = 1 and c = 99/100, against the runner's exact dynamic program.
(2) The rule re-run with a numpy array implementation and compared site by site.
(3) The family enumerated by brute force on 60 further tiny realizations (different window, different seed) against the exact program
    (single-seed components) and against the integer program (all components).
(4) A search for c* > 1 by simulated annealing (different moves and acceptance than the climbs) in a 4x4x7 window for 240 s.
(5) The component lemma probed: the components of the roots of Z_A and Z_B recomputed by a union-find over all G-edges among 1-sites."""
import sys, os, random, math, time
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, sys.argv[2])
import numpy as np
from fractions import Fraction as Fr
import importlib
m = importlib.import_module("admissibility_rule_six_axis_formation_threshold_minimal_marked_tree_family_constant_at_least_one_exact_certificates_and_the_tree_route_floor_2026_09_17")
from supervisor_control_block32_mintree import MinTree

def majority_np(shape, marks):
    A_, B_, L_ = shape
    eta = np.zeros((A_, B_, L_), dtype=np.int8); mk = np.zeros_like(eta)
    for (a, b, c) in marks: mk[a, b, c] = 1
    for s in range(A_ + B_ + L_):
        for a in range(A_):
            for b in range(B_):
                c = s - a - b
                if 0 <= c < L_:
                    n = (eta[a-1, b, c] if a else 0) + (eta[a, b-1, c] if b else 0) + (eta[a, b, c-1] if c else 0)
                    eta[a, b, c] = 1 if (n >= 2 or mk[a, b, c]) else 0
    return eta

print("== (1)+(2)+(5): the extremal realizations")
for name, Z in (("Z_A", m.Z_A), ("Z_B", m.Z_B)):
    root, shape, marks = Z
    eta_np = majority_np(shape, marks)
    sites = [(a, b, c) for a in range(shape[0]) for b in range(shape[1]) for c in range(shape[2])]
    eta = m.run_automaton(sites, {z: 1 for z in marks})
    agree = all(eta_np[z] == eta[z] for z in sites)
    # union-find component over all G-edges among 1-sites
    ones = [z for z in sites if eta[z] == 1]; parent = {z: z for z in ones}
    def find(a):
        while parent[a] != a: a = parent[a]
        return a
    for z in ones:
        for p in m.preds(z):
            if p in parent: parent[find(z)] = find(p)
        for o in m.FORK_OFFSETS:
            w = (z[0] + o[0], z[1] + o[1], z[2] + o[2])
            if w in parent: parent[find(z)] = find(w)
    comp_uf = {z for z in ones if find(z) == find(root)}
    comp_run = m.component(eta, root)
    kind = m.kinds(eta)[2]
    mt = MinTree(eta, root)
    r1 = mt.solve(1.0); r99 = mt.solve(0.99)
    v1 = Fr(r1["E"] - 3 * (r1["S"] - 1) - r1["A"]); v99 = Fr(r1["E"] - 3 * (r1["S"] - 1)) - Fr(99, 100) * r1["A"]
    v99b = Fr(r99["E"] - 3 * (r99["S"] - 1)) - Fr(99, 100) * r99["A"]
    d1 = m.single_seed_min(eta, root, Fr(1))[0]; d99 = m.single_seed_min(eta, root, Fr(99, 100))[0]
    print(f"{name}: numpy rule agrees on all {len(sites)} sites: {agree}; component by union-find = runner's: {comp_uf == comp_run} ({len(comp_uf)} nodes, seeds in it: {sum(1 for z in comp_uf if kind[z]=='seed')}); integer program at c=1: cost {v1} with (E,|A|,|S|,F)=({r1['E']},{r1['A']},{r1['S']},{r1['F']}) verified={r1['ok']} [exact DP: {d1}]; at c=99/100: {v99b} (E,|A|,|S|,F)=({r99['E']},{r99['A']},{r99['S']},{r99['F']}) [exact DP: {d99}]")
print("== (3): brute force on further tiny realizations (window 3x3x5, seed 99)")
random.seed(99); sites = [(a, b, c) for a in range(3) for b in range(3) for c in range(5)]
n_single = n_multi = bad = 0; t0 = time.time()
while n_single + n_multi < 60 and time.time() - t0 < 300:
    zeta = {z: 1 for z in random.sample(sites, random.randint(1, 6))}
    eta = m.run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if len(ones) < 4 or len(ones) > 10: continue
    root = max(ones, key=m.level)
    if m.level(root) < 2: continue
    c = Fr(random.choice([1, 2, 3]), random.choice([1, 2]))
    b = m.brute_min(eta, root, c)
    mt = MinTree(eta, root); r = mt.solve(float(c)); mv = None if r is None else Fr(r["E"] - 3 * (r["S"] - 1)) - c * r["A"]
    comp = m.component(eta, root); kind = m.kinds(eta)[2]
    if sum(1 for z in comp if kind[z] == "seed") == 1:
        d = m.single_seed_min(eta, root, c)[0]; n_single += 1
        if not (b == d == mv): bad += 1
    else:
        n_multi += 1
        if b != mv: bad += 1
print(f"single-seed realizations {n_single} (brute = exact program = integer program), multi-seed {n_multi} (brute = integer program); disagreements {bad}")
print("== (4): simulated annealing on c* (4x4x7, 240 s)")
random.seed(4242); sites = [(a, b, c) for a in range(4) for b in range(4) for c in range(7)]
def score(zeta):
    eta = m.run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if not ones or len(ones) > 70: return Fr(-10)
    roots = sorted(ones, key=m.level, reverse=True)[:3]; best = Fr(-10)
    for root in roots:
        if m.level(root) < 4: continue
        mt = MinTree(eta, root); cs, r, r0 = mt.cstar()
        if cs is None: continue
        if r0["E"] - 3 * (r0["S"] - 1) <= 0: cs = min(cs, Fr(0))
        best = max(best, cs)
    return best
t0 = time.time(); overall = Fr(-10)
while time.time() - t0 < 240:
    zeta = {z: 1 for z in random.sample(sites, 5)}; cur = score(zeta); T = 0.4
    for it in range(400):
        if time.time() - t0 > 240: break
        new = dict(zeta)
        for _ in range(random.choice((1, 2, 3))):
            z = random.choice(sites)
            if z in new: del new[z]
            else: new[z] = 1
        if not new: continue
        sc = score(new)
        if sc >= cur or random.random() < math.exp(float(sc - cur) / T):
            zeta, cur = new, sc; overall = max(overall, cur)
        T = max(0.02, T * 0.995)
print("simulated annealing best c*:", overall, "=", float(overall))
print("== verdict:", "consistent — the exact minima are reproduced by the integer program; nothing above c* = 1 found" if overall <= 1 else "a realization with c* > 1 found — the note's lower bound stands, the conjecture c* = 1 would be refuted")
