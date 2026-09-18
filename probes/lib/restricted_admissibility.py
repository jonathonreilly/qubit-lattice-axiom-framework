"""structure of optimal trees (c = 1): per node type, the multiset of children kinds (nodes whose arrow points to it), forks;
and whether optimal cost is preserved under restrictions: (R1) a processed node has at most one processed child; (R2) at most two
children in total at any non-seed node; (R3) an amplified node has no processed child; (R4) no fork at a processed node."""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import csr_matrix, vstack
from mintree import MinTree, run_automaton, level, preds
import family as m

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


# probe: search for realizations where the one-processed-child restriction is NOT admissible at c = 2 (restricted min > 0 while the
# unrestricted min <= 0); argv: seed count A B L
seed, count = int(sys.argv[1]), int(sys.argv[2]); A_, B_, L_ = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
random.seed(seed); sites = [(a, b, cc) for a in range(A_) for b in range(B_) for cc in range(L_)]
n = hits = worst = 0; t0 = time.time()
while n < count:
    zeta = {z: 1 for z in random.sample(sites, random.randint(3, 16))}
    eta = run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if len(ones) < 12 or len(ones) > 70: continue
    root = max(ones, key=level); mt = MinTree(eta, root); r = mt.solve(2.0)
    if r is None: continue
    base = r["E"] - 3 * (r["S"] - 1) - 2 * r["A"]; v = solve_restricted(mt, 2.0, {"R1"}); n += 1
    if base <= 0 and (v is None or v > 1e-9):
        hits += 1; print(f"HIT: restriction not admissible: base {base}, restricted {v}, zeta={sorted(zeta)}", flush=True)
    if v is not None: worst = max(worst, v - base)
print(f"SUMMARY: realizations={n} hits={hits} max_restricted_minus_unrestricted={worst} elapsed={time.time()-t0:.0f}")
