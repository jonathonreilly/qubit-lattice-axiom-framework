"""Exp 1: the rooted minimum v(z) = min cost over trees containing z with all nodes at levels <= level(z) (integer program with a level cap),
for every 1-site z of many realizations; is v(z) <= 0 always, and <= -1 at amplified nodes?
Exp 2: a greedy rule R1 (amplified-first downward paths + full harvest of amplified nodes) scored against the exact minimum."""
import sys, os, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, sys.argv[1])
import numpy as np
from fractions import Fraction as Fr
from scipy.optimize import milp, LinearConstraint
from scipy.sparse import csr_matrix
from supervisor_control_block33_mintree import MinTree, run_automaton, level, preds
import importlib
m = importlib.import_module("admissibility_rule_six_axis_formation_threshold_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_2026_09_17")

def rooted_min(mt, z, c=1.0):
    """min cost over trees containing z (as root of the ILP) with nodes only at levels <= level(z)."""
    mt2 = MinTree(mt.eta, z)
    cost = np.zeros(mt2.nvar)
    for w in mt2.V:
        cost[mt2.idx[w]] = {"proc": 1.0, "amp": -c, "seed": -3.0}[mt2.kind[w]]
    # cap: nodes above level(z) excluded
    ub = mt2.bounds.ub.copy(); lb = mt2.bounds.lb.copy()
    for w in mt2.V:
        if level(w) > level(z): ub[mt2.idx[w]] = 0
    from scipy.optimize import Bounds
    res = milp(cost, constraints=[LinearConstraint(mt2.A, mt2.lo, mt2.hi)], integrality=mt2.integrality, bounds=Bounds(lb, ub), options={"disp": False, "time_limit": 60})
    if res.status != 0: return None
    xv = res.x
    nodes = [w for w in mt2.V if xv[mt2.idx[w]] > 0.5]
    E = sum(1 for w in nodes if mt2.kind[w] == "proc"); A = sum(1 for w in nodes if mt2.kind[w] == "amp"); Sn = sum(1 for w in nodes if mt2.kind[w] == "seed")
    return E - 3 * (Sn - 1) - A, (E, A, Sn)

def rule_R1(eta, root):
    """downward paths from the root choosing preds by preference amplified > seed > processed (lexicographic ties); then harvest every
    amplified node whose single predecessor is in the tree, repeatedly; forks: none (single-seed only); returns cost or None."""
    ones, npred, kind = m.kinds(eta)
    N = {root}; frontier = [root]
    while frontier:
        z = frontier.pop()
        if kind[z] == "seed": continue
        ps = npred[z]
        pref = sorted(ps, key=lambda u: ({"amp": 0, "seed": 1, "proc": 2}[kind[u]], u))
        u = pref[0]
        if u not in N: N.add(u); frontier.append(u)
    changed = True
    while changed:
        changed = False
        for a in ones:
            if kind[a] == "amp" and a not in N and npred[a][0] in N:
                N.add(a); changed = True
    seeds = [w for w in N if kind[w] == "seed"]
    if len(seeds) != 1: return None, None
    E = sum(1 for w in N if kind[w] == "proc"); A = sum(1 for w in N if kind[w] == "amp")
    return E - A, (E, A)

random.seed(33)
cases = []
for name, Z in (("Z_A", m.Z_A), ("Z_B", m.Z_B), ("W1", m.W1)):
    root, (A_, B_, L_), marks = Z
    sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
    cases.append((name, run_automaton(sites, {z: 1 for z in marks})))
sites = [(a, b, c) for a in range(4) for b in range(4) for c in range(7)]
n = 0
while n < 60:
    zeta = {z: 1 for z in random.sample(sites, random.randint(3, 12))}
    eta = run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if len(ones) < 15 or len(ones) > 60: continue
    cases.append((f"rand{n}", eta)); n += 1
worst_proc = worst_amp = Fr(-100); viol = 0; R1_fail = 0; R1_tested = 0; t0 = time.time(); zc = 0
hist = {}
for name, eta in cases:
    ones, npred, kind = m.kinds(eta)
    mt = MinTree(eta, max(ones, key=level))
    for z in ones:
        if kind[z] == "seed": continue
        r = rooted_min(mt, z)
        if r is None: continue
        v, cnt = r; zc += 1
        key = (kind[z], v); hist[key] = hist.get(key, 0) + 1
        if kind[z] == "amp": worst_amp = max(worst_amp, v)
        else: worst_proc = max(worst_proc, v)
        if (kind[z] == "amp" and v > -1) or (kind[z] == "proc" and v > 0):
            viol += 1
            if viol <= 5: print(f"  rooted violation: {name} z={z} kind={kind[z]} v={v} counts={cnt}")
    # R1 on the top root
    root = max(ones, key=level)
    rc, cnt = rule_R1(eta, root)
    if rc is not None:
        R1_tested += 1
        if rc > 0:
            R1_fail += 1
            if R1_fail <= 5: print(f"  R1 fails on {name}: cost {rc} counts {cnt}; exact min: {mt.solve(1.0)['cost']}")
print(f"{len(cases)} realizations, {zc} rooted sites in {time.time()-t0:.0f}s: max rooted v over processed = {worst_proc}, over amplified = {worst_amp}; violations of (proc <= 0, amp <= -1): {viol}")
print("distribution (kind, v):", sorted(hist.items(), key=lambda kv: (kv[0][0], kv[0][1])))
print(f"R1 (single-seed cases): tested {R1_tested}, cost > 0 in {R1_fail}")
