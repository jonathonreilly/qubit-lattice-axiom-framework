import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import supervisor_control_block31_core as core
from fractions import Fraction as F
from collections import Counter
x = (0, 0, 0); random.seed(int(sys.argv[1])); N = int(sys.argv[2])
worst = F(-100); cnt = 0; stats = Counter(); bad_e2_rise0 = 0; bad_e2 = Counter(); worst_cfg = None
for trial in range(N):
    d = random.choice((5, 6, 7, 8, 9, 10, 11, 12, 14)); dens = random.choice((6, 8, 12, 18, 25, 35, 50))
    sites = core.cone(x, d); zeta = {z: 1 for z in sites if random.randrange(100) < dens}
    eta = core.run_automaton(sites, zeta)
    if eta[x] != 1: continue
    ex = core.Explainer(eta, zeta)
    try: nodes, edges, Sn, An, refs, bad = ex.explain(x)
    except AssertionError as e: print("FAIL", e); continue
    for (b, k, a, e, nf, rise, npoles) in ex.log:
        stats[(b, a, e, min(rise, 3))] += 1
        if b >= 1 and e >= 2: bad_e2[(b, a, e, rise)] += 1
        if b >= 1 and e >= 2 and rise <= 0: bad_e2_rise0 += 1
    E = sum(1 for k in edges.values() if k == "arrow"); nS, nA = len(Sn), len(An)
    if nA > 0:
        cnt += 1; r = F(E - 3*(nS-1), nA)
        if r > worst: worst = r; worst_cfg = (d, sorted(zeta), E, nS, nA)
print(f"seed {sys.argv[1]}: {cnt} trees with A; worst ratio {worst} = {float(worst):.3f}; refinements with a bad pole and >= 2 E-arrows: {sum(bad_e2.values())}, of which rise <= 0: {bad_e2_rise0}")
print("  (bad, a, e, rise) for bad refinements with e >= 2:", dict(bad_e2))
tot_bad = sum(v for (b,a,e,r), v in stats.items() if b >= 1); print("  bad refinements total:", tot_bad, "; distribution of (b,a,e,rise capped 3) among them:", {k: v for k, v in sorted(stats.items()) if k[0] >= 1})
if worst_cfg: print("  worst cfg depth", worst_cfg[0], "E,|S|,|A| =", worst_cfg[2:], "zeta:", worst_cfg[1])
