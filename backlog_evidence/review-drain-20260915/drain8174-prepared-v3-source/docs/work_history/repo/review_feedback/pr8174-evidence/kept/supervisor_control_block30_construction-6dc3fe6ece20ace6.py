"""Control, block 30: the extended explanation tree with amplified nodes, executed exhaustively on the depth-2 cone, on all depth-3
configurations with <= 4 noise sites and on random cones; checks: tree; S-nodes are seeds (0 one-preds), A-nodes have exactly one
1-pred; <= 1 down-arrow per node; forks = |S| - 1; refinements <= |S| - 1 + bad_total; bad_total <= |A|; E <= 3(|S| - 1) + 2|A|."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import supervisor_control_block30_core as core
from itertools import product, combinations
from fractions import Fraction as F
x = (0, 0, 0)
def check(zeta, sites):
    eta = core.run_automaton(sites, zeta)
    if eta[x] != 1: return None
    ex = core.Explainer(eta, zeta)
    nodes, edges, S, A, refs, bad = ex.explain(x)
    ok = core.check_tree(nodes, edges, x, ex)
    downs = {v: 0 for v in nodes}; E = Fk = Am = 0
    for e, kind in edges.items():
        a, b = tuple(e)
        if kind == "fork": Fk += 1; continue
        upper = a if b in core.preds(a) else b; downs[upper] += 1
        if kind == "arrow": E += 1
        else: Am += 1
    nS, nA = len(S), len(A)
    ok = ok and all(z in ex.noise for z in S) and all(z in ex.amp for z in A) and max(downs.values()) <= 1
    ok = ok and {v for v in nodes if downs[v] == 0} == S and Am == nA
    ok = ok and Fk == nS - 1 and refs <= nS - 1 + bad and bad <= nA and E <= 3 * (nS - 1) + 2 * nA
    return ok, nS, nA, E, Fk, bad, refs
random.seed(30)
sites2 = core.cone(x, 2); sites3 = core.cone(x, 3)
configs = [({z: b for z, b in zip(sites2, bits) if b}, sites2) for bits in product((0, 1), repeat=len(sites2))]
for k in range(1, 5):
    for combo in combinations(sites3, k): configs.append(({z: 1 for z in combo}, sites3))
for t in range(1500):
    d = random.choice((3, 4, 5, 6, 7, 8)); dens = random.choice((10, 20, 35, 50))
    s = core.cone(x, d); configs.append(({z: 1 for z in s if random.randrange(100) < dens}, s))
allok = True; n = 0; maxA = 0; worstE = F(0); withA = 0; badsum = 0
for zeta, sites in configs:
    r = check(zeta, sites)
    if r is None: continue
    ok, nS, nA, E, Fk, bad, refs = r; n += 1; allok = allok and ok; maxA = max(maxA, nA); withA += (nA > 0); badsum += bad
    if nS >= 2: worstE = max(worstE, F(E - 2 * nA, nS - 1))
print(f"{n} explained configurations (exhaustive depth-2, depth-3 with <= 4 noise, 1500 random): all checks pass: {allok}; trees with A-nodes: {withA}; max |A| = {maxA}; total bad pairs {badsum}; worst (E - 2|A|)/(|S| - 1) = {worstE} = {float(worstE):.3f} (budget 3)")
