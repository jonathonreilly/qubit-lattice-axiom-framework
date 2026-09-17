"""the hard inductive case: processed z all of whose 1-predecessors u have rooted minimum v(u) = 0 (seeds or tight processed nodes).
Print v(z), the kinds of the preds, and the optimal rooted tree of z (nodes by level, seeds/forks)."""
import sys, os, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, sys.argv[1])
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from supervisor_control_block33_mintree import MinTree, run_automaton, level, preds
import importlib
m = importlib.import_module("admissibility_rule_six_axis_formation_threshold_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_2026_09_17")

def rooted(eta, z, c=1.0):
    mt2 = MinTree(eta, z)
    cost = np.zeros(mt2.nvar)
    for w in mt2.V: cost[mt2.idx[w]] = {"proc": 1.0, "amp": -c, "seed": -3.0}[mt2.kind[w]]
    ub = mt2.bounds.ub.copy(); lb = mt2.bounds.lb.copy()
    for w in mt2.V:
        if level(w) > level(z): ub[mt2.idx[w]] = 0
    res = milp(cost, constraints=[LinearConstraint(mt2.A, mt2.lo, mt2.hi)], integrality=mt2.integrality, bounds=Bounds(lb, ub), options={"disp": False, "time_limit": 60})
    if res.status != 0: return None, None
    xv = res.x
    nodes = [w for w in mt2.V if xv[mt2.idx[w]] > 0.5]
    arrows = [(a, b) for k, (a, b) in enumerate(mt2.arrows) if xv[mt2.off_a + k] > 0.5]
    forks = [(a, b) for k, (a, b) in enumerate(mt2.forks) if xv[mt2.off_f + k] > 0.5]
    E = sum(1 for w in nodes if mt2.kind[w] == "proc"); A = sum(1 for w in nodes if mt2.kind[w] == "amp"); Sn = sum(1 for w in nodes if mt2.kind[w] == "seed")
    return E - 3 * (Sn - 1) - A, dict(nodes=nodes, arrows=arrows, forks=forks, E=E, A=A, S=Sn, kind=mt2.kind)

random.seed(34)
sites = [(a, b, c) for a in range(4) for b in range(4) for c in range(7)]
cases = []
for name, Z in (("Z_A", m.Z_A), ("Z_B", m.Z_B), ("W1", m.W1)):
    root, (A_, B_, L_), marks = Z
    st = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
    cases.append((name, run_automaton(st, {z: 1 for z in marks})))
n = 0
while n < 80:
    zeta = {z: 1 for z in random.sample(sites, random.randint(3, 14))}
    eta = run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if len(ones) < 12 or len(ones) > 60: continue
    cases.append((f"rand{n}", eta)); n += 1
hard = 0; shown = 0; kinds_hist = {}; mech = {}
for name, eta in cases:
    ones, npred, kind = m.kinds(eta)
    vcache = {}
    def v(z):
        if z not in vcache:
            vcache[z] = rooted(eta, z)
        return vcache[z]
    for z in sorted(ones, key=level):
        if kind[z] != "proc": continue
        ps = npred[z]
        if all(kind[u] == "seed" or (kind[u] == "proc" and v(u)[0] == 0) for u in ps):
            hard += 1
            vz, T = v(z)
            key = tuple(sorted(kind[u] for u in ps)); kinds_hist[key] = kinds_hist.get(key, 0) + 1
            # mechanism: which preds are in the tree, forks used, seeds used
            inT = [u for u in ps if u in T["nodes"]]
            mk = (vz, len(inT), T["S"], len(T["forks"]))
            mech[mk] = mech.get(mk, 0) + 1
            if shown < 6 and key != ("seed", "seed") and key != ("seed", "seed", "seed"):
                shown += 1
                lv = {}
                for w in T["nodes"]: lv.setdefault(level(w), []).append(w)
                print(f"{name}: z={z} preds={[(u, kind[u], v(u)[0]) for u in ps]} -> v(z)={vz} tree (E,A,S,F)=({T['E']},{T['A']},{T['S']},{len(T['forks'])}); forks={T['forks']}")
                for l in sorted(lv, reverse=True):
                    print("     level", l, ", ".join(f"{w}{kind[w][0]}" for w in sorted(lv[l])))
print(f"hard cases (processed z with all 1-preds seeds or tight): {hard}; pred-kind patterns: {kinds_hist}")
print("mechanism (v(z), #preds in tree, seeds, forks):", sorted(mech.items()))
