import sys, ast
sys.path.insert(0, sys.argv[1])
from supervisor_control_block31_core import Explainer, level, preds, check_tree, run_automaton
from fractions import Fraction as F
W = {
 "w5over3": ((3,3,6), [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 5), (0, 1, 0), (0, 1, 2), (0, 1, 3), (0, 2, 1), (0, 2, 2), (0, 2, 3), (0, 2, 5), (0, 2, 6), (0, 3, 1), (0, 3, 2), (0, 3, 5), (0, 3, 6), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 1), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 2), (2, 0, 3), (2, 1, 3), (2, 1, 4), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 2, 5), (2, 3, 1), (2, 3, 5), (2, 3, 6), (3, 0, 0), (3, 2, 2), (3, 3, 1), (3, 3, 2), (3, 3, 5)]),
 "w8over5": ((3,3,4), [(0, 0, 0), (0, 0, 1), (0, 0, 4), (0, 1, 0), (0, 2, 6), (0, 3, 5), (0, 3, 6), (1, 0, 0), (1, 0, 2), (1, 1, 5), (1, 2, 0), (1, 2, 2), (1, 3, 1), (1, 3, 2), (2, 0, 0), (2, 0, 1), (2, 1, 1), (2, 1, 5), (2, 2, 0), (2, 2, 3), (2, 2, 5), (2, 3, 2), (2, 3, 4), (2, 3, 5), (3, 0, 2), (3, 0, 4), (3, 0, 5), (3, 0, 6), (3, 1, 5), (3, 2, 2), (3, 2, 6), (3, 3, 2), (3, 3, 3), (3, 3, 4), (3, 3, 5)]),
}
sites = [(a,b,c) for a in range(4) for b in range(4) for c in range(7)]
for name, (root, zl) in W.items():
    zeta = {z: 1 for z in zl}
    eta = run_automaton(sites, zeta)
    ex = Explainer(eta, zeta)
    nodes, edges, seeds, amps, nref, bad = ex.explain(root)
    E = sum(1 for e, k in edges.items() if k == "arrow"); A = len(amps); Sn = len(seeds); Fk = sum(1 for e, k in edges.items() if k == "fork")
    # minimal noise set actually used by the tree: seeds + amplified nodes of the tree
    used = set(seeds) | set(amps)
    print(f"{name}: root {root}; ones={len(ex.ones)}; tree nodes={len(nodes)} E={E} |A|={A} |S|={Sn} forks={Fk} refinements={nref} bad={bad}; ratio={F(E-3*(Sn-1),A)}; tree_check={check_tree(nodes, edges, root, ex)}; block30 bound {3*(Sn-1)+2*A} ok={E <= 3*(Sn-1)+2*A}; noise marks used by the tree: {len(used)} of {len(zl)}")
    print("   log (bad,kept,a,e,forks,rise,distinct):", ex.log)
    # is the tree reproduced with only the used noise marks? (the rest of zeta only creates 1-sites outside the tree)
    zeta2 = {z: 1 for z in used}
    eta2 = run_automaton(sites, zeta2)
    ex2 = Explainer(eta2, zeta2)
    if root in ex2.ones:
        n2, e2, s2, a2, r2, b2 = ex2.explain(root)
        E2 = sum(1 for e, k in e2.items() if k == "arrow")
        print(f"   with only the tree's own marks: ones={len(ex2.ones)} E={E2} |A|={len(a2)} |S|={len(s2)} ratio={F(E2-3*(len(s2)-1), len(a2)) if a2 else None} check={check_tree(n2, e2, root, ex2)}")
    else:
        print("   with only the tree's own marks the root is 0 (other 1-sites feed the winning pairs)")
    lv = {}
    for v in nodes: lv.setdefault(level(v), []).append(v)
    for l in sorted(lv, reverse=True):
        print(f"   level {l}: " + ", ".join(f"{v}{'S' if v in seeds else 'A' if v in amps else 'P'}" for v in sorted(lv[l])))
