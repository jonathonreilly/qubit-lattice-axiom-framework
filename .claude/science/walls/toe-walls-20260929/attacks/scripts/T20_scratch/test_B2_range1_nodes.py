"""Caveat probe for Test B: range |v|_inf<=1 covariant laws for the three non-full actions. Do isolated linear
nodes exist away from Gamma (anisotropic, non-symmetric points)?"""
import numpy as np
from test_B_covariant import build, hop_set, combo, component_rank, find_nodes, report_nodes, dvec
V = hop_set(1)
for kind in ("trivial", "sign", "axis", "full"):
    basis, _ = build(kind, V)
    print(f"{kind}: dim {len(basis)}")
    for trial in range(4):
        C, A = combo(basis)
        r, _ = component_rank(C, A, 200)
        nodes = find_nodes(C, A, 80) if r == 3 else []
        rows = report_nodes(C, A, nodes)
        iso = [x for x in rows if x[1][-1] > 1e-6]
        conds = [x[1][0] / x[1][-1] for x in iso]
        print(f"   member {trial}: r={r}; isolated rank-3 nodes found: {len(iso)}; cond numbers: {np.round(conds[:6],2)}")
