import sys, os, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, sys.argv[1])
from fractions import Fraction as Fr
from itertools import combinations
import supervisor_control_block33_ssdp as ssdp
m = importlib.import_module("admissibility_rule_six_axis_formation_threshold_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_2026_09_17")
def optimal_set(eta, p):
    capped = {z: (v if m.level(z) <= m.level(p) else 0) for z, v in eta.items()}
    val, seeds, tree = ssdp.single_seed_min(capped, p, Fr(1), want_tree=True)
    return val, set(tree)
for name, Z in (("Z_A", m.Z_A), ("Z_B", m.Z_B)):
    root, (A_, B_, L_), marks = Z
    sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
    eta = m.run_automaton(sites, {z: 1 for z in marks}); ones, npred, kind = m.kinds(eta)
    print(f"== {name}: root {root} (tight); its 1-predecessors and their optimal rooted sets")
    sets = {}
    for p in npred[root]:
        val, N = optimal_set(eta, p); E = sum(1 for z in N if kind[z] == "proc"); A = sum(1 for z in N if kind[z] == "amp")
        sets[p] = N; print(f"   pred {p}: v = {val}, set size {len(N)} (E={E}, A={A})")
    for p1, p2 in combinations(npred[root], 2):
        O = sets[p1] & sets[p2]; EO = sum(1 for z in O if kind[z] == "proc"); AO = sum(1 for z in O if kind[z] == "amp")
        U = sets[p1] | sets[p2] | {root}; EU = sum(1 for z in U if kind[z] == "proc"); AU = sum(1 for z in U if kind[z] == "amp")
        print(f"   pair {p1},{p2}: overlap {len(O)} nodes (E_O={EO}, A_O={AO}, E_O-A_O={EO-AO}); union with root: E-A = {EU-AU}")
