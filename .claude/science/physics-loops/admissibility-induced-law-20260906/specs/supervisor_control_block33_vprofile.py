import sys, importlib
sys.path.insert(0, sys.argv[1])
from fractions import Fraction as Fr
m = importlib.import_module("admissibility_rule_six_axis_formation_threshold_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_2026_09_17")
for name, Z in (("Z_A", m.Z_A), ("Z_B", m.Z_B)):
    root, (A_, B_, L_), marks = Z
    sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
    eta = m.run_automaton(sites, {z: 1 for z in marks}); ones, npred, kind = m.kinds(eta)
    comp = m.component(eta, root)
    v = {}
    for z in sorted(comp, key=m.level):
        v[z] = m.single_seed_min_capped(eta, z, Fr(1), m.level(z))[0]
    lv = {}
    for z in comp: lv.setdefault(m.level(z), []).append(z)
    print(f"== {name}: rooted values by level (kind, v); seed at (0,0,0)")
    for l in sorted(lv, reverse=True):
        print(f"  level {l:2d}: " + "  ".join(f"{z}{kind[z][0]}:{v[z]}" for z in sorted(lv[l])))
    # for each processed node: v(z) - (1 + min pred v)  (0 = path-tight, negative = merge/harvest helped)
    slack = {}
    for z in comp:
        if kind[z] == "proc":
            s = v[z] - (1 + min(v[u] for u in npred[z]))
            slack[s] = slack.get(s, 0) + 1
    print("  processed nodes: v(z) - (1 + min_u v(u)) distribution:", sorted(slack.items()))
