import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import construction30 as core
random.seed(int(sys.argv[1])); N = int(sys.argv[2])
x = (0, 0, 0); trees = 0; kinds = {"seed": 0, "amp": 0, "proc": 0}; multi3 = 0
for trial in range(N):
    depth = 3 + trial % 7; dens = (10, 20, 35, 50, 65)[trial % 5]
    sites = core.cone(x, depth); zeta = {z: 1 for z in sites if random.randrange(100) < dens}
    eta = core.run_automaton(sites, zeta)
    if eta[x] != 1: continue
    ex = core.Explainer(eta, zeta)
    try: nodes, edges, seeds, amps, nref, bad = ex.explain(x)
    except AssertionError: continue
    trees += 1
    kids = {}
    for e, k in edges.items():
        a, b = tuple(e)
        if k == "fork": continue
        upper = a if b in core.preds(a) else b; lower = b if upper == a else a
        if upper not in ex.amp and upper not in ex.noise:
            kids[lower] = kids.get(lower, 0) + 1
    for u, c in kids.items():
        if c >= 2:
            kinds["amp" if u in ex.amp else "seed" if u in ex.noise else "proc"] += 1
            if c >= 3: multi3 += 1
print(f"seed {sys.argv[1]}: {trees} trees; nodes with >= 2 processed children by kind: {kinds}; with 3: {multi3}")
