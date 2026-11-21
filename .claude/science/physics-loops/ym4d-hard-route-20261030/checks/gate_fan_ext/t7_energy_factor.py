#!/usr/bin/env python3
"""T7, guide only: energy transfer factor of the reflection R on each linear piece."""
import random, sys
import numpy as np
import t1_tree_reflection as t1

def jac(t, ls, S, ac, z, e=1e-5):
    J = np.zeros((len(ac), len(ac)))
    for j, c in enumerate(ac):
        zp, zm = dict(z), dict(z)
        zp[c] += e; zm[c] -= e
        rp, _ = t1.R_map(t, ls, S, zp); rm, _ = t1.R_map(t, ls, S, zm)
        for i, b in enumerate(ac):
            J[i, j] = (rp[b] - rm[b]) / (2 * e)
    return J

random.seed(5)
ts = [t for t in t1.all_trees([1, 2, 3, 4]) if t != "o"]
worst, worstp, by = 0, None, {}
for t in ts:
    ls = t1.leaves(t); ac = sorted(set(t1.nodes(t))); n = len(ls)
    for mask in range(1, 2 ** n - 1):
        S = {i for i in range(n) if mask >> i & 1}
        k = 0; lip = 0
        for _ in range(1500):
            z = {c: random.gauss(0, 1) * 10 ** random.uniform(-1, 1) for c in ac}
            if t1.leaf_of(ls, z) in S:
                continue
            J = jac(t, ls, S, ac, z)
            s = np.linalg.svd(J, compute_uv=False)
            if s[-1] < 1e-9:
                continue
            k = max(k, s[0] ** 2 / abs(np.prod(s)) if len(ac) > 2 else s[0] ** 2 / abs(np.prod(s)))
            lip = max(lip, s[0], 1 / s[-1])
        by[len(ac)] = max(by.get(len(ac), 0), k)
        by[("lip", len(ac))] = max(by.get(("lip", len(ac)), 0), lip)
        if t == (3, (1, "o", "o"), (2, "o", "o")) and mask == 0b1001:
            print("balanced fan, leaves 1 and 4: kappa", round(k, 3), "Euclid Lip", round(lip, 3))
print({str(k): round(v, 3) for k, v in by.items()})
