"""Fairness check for kill_R2: a finite-range (moral-graph) parent DOES exist for a fixed-order formation law.
Range needed = the moral graph (parents, children, co-parents of children)."""
import itertools, numpy as np
from kill_R2_formation_law import *

def moral_blankets(n, nbrs, order):
    pos = {x: k for k, x in enumerate(order)}
    parents = {x: [y for y in nbrs[x] if pos[y] < pos[x]] for x in range(n)}
    bl = {x: set(parents[x]) for x in range(n)}
    for c in range(n):
        for p in parents[c]:
            bl[p].add(c)
            for q in parents[c]:
                if q != p: bl[p].add(q)
    return {x: sorted(bl[x]) for x in range(n)}

def defect_with_blanket(mu, blank, n):
    worst = 0.0
    for x in range(n):
        full = cond_given_rest(mu, x)
        others = [a for a in range(n) if a != x and a not in blank[x]]
        m = mu.sum(axis=tuple(others), keepdims=True) if others else mu
        nn_cond = m / m.sum(axis=x, keepdims=True)
        worst = max(worst, np.abs(full - nn_cond).max())
    return worst

def nn_range(n, nbrs, blank):
    ext = []
    for x in range(n):
        extra = [y for y in blank[x] if y not in nbrs[x]]
        ext.append(extra)
    return ext

for tag, n, edges, od in [("cycle4", 4, [(0,1),(1,2),(2,3),(3,0)], (0,1,2,3)),
                          ("cube8", 8, cube_edges if 'cube_edges' in globals() else None, (0,3,5,6,1,2,4,7))]:
    nbrs = build(n, edges)
    mu = joint_formation(n, nbrs, od)
    bl = moral_blankets(n, nbrs, od)
    print(tag, "order", od, "moral-blanket Markov defect", f"{defect_with_blanket(mu, bl, n):.2e}",
          "| sites needing non-nearest-neighbour projector support:", sum(1 for e in nn_range(n, nbrs, bl) if e), "of", n)
