"""structure of optimal trees (c = 1): per node type, the multiset of children kinds (nodes whose arrow points to it), forks;
and whether optimal cost is preserved under restrictions: (R1) a processed node has at most one processed child; (R2) at most two
children in total at any non-seed node; (R3) an amplified node has no processed child; (R4) no fork at a processed node."""
import sys, os, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, sys.argv[1])
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import csr_matrix, vstack
from supervisor_control_block33_mintree import MinTree, run_automaton, level, preds
import importlib
m = importlib.import_module("admissibility_rule_six_axis_formation_threshold_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_2026_09_17")

def solve_restricted(mt, c, restr):
    cost = np.zeros(mt.nvar)
    for z in mt.V: cost[mt.idx[z]] = {"proc": 1.0, "amp": -c, "seed": -3.0}[mt.kind[z]]
    cons = [LinearConstraint(mt.A, mt.lo, mt.hi)]
    rows = []; his = []
    for u in mt.V:
        kids = [(k, z) for k, (z, uu) in enumerate(mt.arrows) if uu == u]
        if "R1" in restr and mt.kind[u] == "proc":
            co = np.zeros(mt.nvar)
            for k, z in kids:
                if mt.kind[z] == "proc": co[mt.off_a + k] = 1
            if co.any(): rows.append(co); his.append(1)
        if "R2" in restr and mt.kind[u] != "seed":
            co = np.zeros(mt.nvar)
            for k, z in kids: co[mt.off_a + k] = 1
            if co.any(): rows.append(co); his.append(2)
        if "R3" in restr and mt.kind[u] == "amp":
            co = np.zeros(mt.nvar)
            for k, z in kids:
                if mt.kind[z] == "proc": co[mt.off_a + k] = 1
            if co.any(): rows.append(co); his.append(0)
        if "R4" in restr and mt.kind[u] == "proc":
            co = np.zeros(mt.nvar)
            for k, (a, b) in enumerate(mt.forks):
                if u in (a, b): co[mt.off_f + k] = 1
            if co.any(): rows.append(co); his.append(0)
    if rows:
        cons.append(LinearConstraint(csr_matrix(np.array(rows)), -np.inf, np.array(his, dtype=float)))
    res = milp(cost, constraints=cons, integrality=mt.integrality, bounds=mt.bounds, options={"disp": False, "time_limit": 60})
    if res.status != 0: return None
    xv = res.x
    nodes = [z for z in mt.V if xv[mt.idx[z]] > 0.5]
    E = sum(1 for z in nodes if mt.kind[z] == "proc"); A = sum(1 for z in nodes if mt.kind[z] == "amp"); Sn = sum(1 for z in nodes if mt.kind[z] == "seed")
    return E - 3 * (Sn - 1) - c * A

random.seed(35)
cases = []
for name, Z in (("Z_A", m.Z_A), ("Z_B", m.Z_B), ("W1", m.W1), ("W2", m.W2)):
    root, (A_, B_, L_), marks = Z
    st = [(a, b, cc) for a in range(A_) for b in range(B_) for cc in range(L_)]
    cases.append((name, run_automaton(st, {z: 1 for z in marks}), root))
sites = [(a, b, cc) for a in range(4) for b in range(4) for cc in range(7)]
n = 0
while n < 120:
    zeta = {z: 1 for z in random.sample(sites, random.randint(3, 14))}
    eta = run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if len(ones) < 12 or len(ones) > 60: continue
    cases.append((f"rand{n}", eta, max(ones, key=level))); n += 1
patt = {}; forkpatt = {}; loss = {r: 0 for r in ("R1", "R2", "R3", "R4")}; tested = 0; t0 = time.time()
for name, eta, root in cases:
    mt = MinTree(eta, root); r = mt.solve(1.0)
    if r is None: continue
    tested += 1
    kids = {}
    for (z, u) in r["arrows"]: kids.setdefault(u, []).append(mt.kind[z])
    fk = {}
    for (a, b) in r["forks"]:
        fk[a] = fk.get(a, 0) + 1; fk[b] = fk.get(b, 0) + 1
    for u in r["nodes"]:
        key = (mt.kind[u], tuple(sorted(kids.get(u, []))))
        patt[key] = patt.get(key, 0) + 1
        fkey = (mt.kind[u], fk.get(u, 0)); forkpatt[fkey] = forkpatt.get(fkey, 0) + 1
    base = r["E"] - 3 * (r["S"] - 1) - r["A"]
    for rr in loss:
        v = solve_restricted(mt, 1.0, {rr})
        if v is None or v > base + 1e-9: loss[rr] += 1
print(f"{tested} realizations in {time.time()-t0:.0f}s")
print("children patterns (node kind, sorted kinds of nodes whose arrow points to it) -> count:")
for k in sorted(patt, key=lambda kv: (kv[0], len(kv[1]), kv[1])): print("   ", k, patt[k])
print("fork incidence (kind, #forks at node):", sorted(forkpatt.items()))
print("realizations where the restriction raises the minimum cost:", loss)
