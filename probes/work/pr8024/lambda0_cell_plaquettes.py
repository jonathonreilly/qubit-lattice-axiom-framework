#!/usr/bin/env python3
"""J:attack-a:PR8024 — WITNESS REALIZABILITY of Lambda0 cells and plaquettes.

Note: at x in Z^3, three positively oriented outgoing links x->x+e_i;
Lambda0={0,e1,e2,e3}; three plaquettes i<j (4-cycles, not triangles);
Z^3 bipartite. Not the known Casimir-floor HIT (C(1,0)=8/3 vs 4).
"""
from __future__ import annotations

from itertools import combinations

E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def add(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def main():
    hits = []
    origin = (0, 0, 0)
    Lambda0 = (origin,) + E
    print(f"Lambda0={Lambda0} n={len(set(Lambda0))}")
    if len(set(Lambda0)) != 4:
        hits.append("Lambda0 not 4 distinct sites")

    # three plaquettes: vertices 0, e_i, e_j, e_i+e_j
    for i, j in combinations(range(3), 2):
        verts = [origin, E[i], E[j], add(E[i], E[j])]
        if len(set(verts)) != 4:
            hits.append(f"plaquette {i}{j} not 4 vertices")
        # 4-cycle edges of length 1
        edges = [
            (origin, E[i]), (origin, E[j]),
            (E[i], add(E[i], E[j])), (E[j], add(E[i], E[j])),
        ]
        for u, v in edges:
            d = sum(abs(u[k] - v[k]) for k in range(3))
            if d != 1:
                hits.append(f"plaquette {i}{j} edge {u}-{v} l1={d}")
        # fourth vertex not in Lambda0
        fourth = add(E[i], E[j])
        if fourth in Lambda0:
            hits.append(f"fourth vertex {fourth} in Lambda0")
        print(f"plaquette {i}<{j}: verts={verts} 4-cycle edges ok, fourth={fourth} not a tail cell")

    # no triangle of NN edges in Lambda0: Lambda0 is a 3-star (origin plus 3)
    # the three e_i are pairwise at l1=2
    for i, j in combinations(range(3), 2):
        d = sum(abs(E[i][k] - E[j][k]) for k in range(3))
        if d == 1:
            hits.append("e_i adjacent to e_j (triangle)")
    print("Lambda0 is K_{1,3} (no triangles)")

    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: WITNESS REALIZABILITY (PR #8024): " + "; ".join(hits))
    else:
        print(
            "SUMMARY: WITNESS REALIZABILITY (PR #8024): Lambda0={0,e1,e2,e3} is four "
            "sites with three outgoing links and three 4-cycle plaquettes whose fourth "
            "vertices lie outside the tail cell; no triangles; pattern has purchase "
            "and the witnesses exist as written"
        )


if __name__ == "__main__":
    main()
