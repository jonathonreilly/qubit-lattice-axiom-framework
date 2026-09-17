import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import supervisor_control_block30_core as core
from itertools import product, combinations
from fractions import Fraction as F
x = (0,0,0); random.seed(31); worst = F(-10); cnt = 0; hist = {}
sites2 = core.cone(x, 2); configs = [({z: b for z, b in zip(sites2, bits) if b}, sites2) for bits in product((0,1), repeat=len(sites2))]
for t in range(2500):
    d = random.choice((4,5,6,7,8,9,10)); dens = random.choice((10,20,35,50)); s = core.cone(x, d); configs.append(({z: 1 for z in s if random.randrange(100) < dens}, s))
for zeta, sites in configs:
    eta = core.run_automaton(sites, zeta)
    if eta[x] != 1: continue
    ex = core.Explainer(eta, zeta); nodes, edges, S, A, refs, bad = ex.explain(x)
    E = sum(1 for k in edges.values() if k == "arrow"); nS, nA = len(S), len(A)
    if nA > 0:
        cnt += 1; excess = E - 3*(nS - 1); worst = max(worst, F(excess, nA)); hist[nA] = max(hist.get(nA, F(-10)), F(excess, nA))
print(f"trees with A-nodes: {cnt}; worst (E - 3(|S|-1))/|A| = {worst} = {float(worst):.3f} (the proved budget allows 2); by |A|: { {k: float(v) for k, v in sorted(hist.items())} }")
