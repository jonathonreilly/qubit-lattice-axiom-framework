#!/usr/bin/env python3
"""J:attack-a:PR8149 — WITNESS REALIZABILITY of the star, plaquette, and 18-site hull.

Note: isolated star = a site and its six neighbours; isolated plaquette C4;
16 path orders + 8 diagonal-first = 24 = 4!; outside neighbours of the star
(the environment) are the 18 sites at graph distance 2 adjacent to some leaf.
Z^3 bipartite: star and plaquette have no triangles.

Not the known HIT (sigma-equivariant 216 envs / product of D).
"""
from __future__ import annotations

from itertools import permutations, product

STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def add(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def main():
    hits = []
    o = (0, 0, 0)
    leaves = [add(o, s) for s in STEPS]
    star = [o] + leaves
    if len(set(star)) != 7:
        hits.append("star not 7 distinct sites")
    # no triangle: leaves are pairwise non-adjacent
    leafset = set(leaves)
    leaf_edges = 0
    for a in leaves:
        for s in STEPS:
            if add(a, s) in leafset:
                leaf_edges += 1
    leaf_edges //= 2
    print(f"star sites=7 leaf-leaf NN edges={leaf_edges} (stated 0; bipartite)")
    if leaf_edges != 0:
        hits.append(f"star has {leaf_edges} leaf-leaf edges (triangle/C4?)")

    # 18 outside sites: neighbors of leaves except origin and except other leaves
    outside = set()
    for a in leaves:
        for s in STEPS:
            y = add(a, s)
            if y != o and y not in leafset:
                outside.add(y)
    print(f"star outside sites {len(outside)} stated 18")
    if len(outside) != 18:
        hits.append(f"outside {len(outside)} != 18")

    # plaquette C4 in the e1-e2 plane
    pla = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)]
    edges = {frozenset(p) for p in (
        ((0, 0, 0), (1, 0, 0)), ((0, 0, 0), (0, 1, 0)),
        ((1, 0, 0), (1, 1, 0)), ((0, 1, 0), (1, 1, 0)),
    )}
    # opposite pairs (diagonals)
    diags = {frozenset(((0, 0, 0), (1, 1, 0))), frozenset(((1, 0, 0), (0, 1, 0)))}
    verts = pla
    n_path = n_diag = 0
    for order in permutations(verts):
        first2 = frozenset(order[:2])
        if first2 in diags:
            n_diag += 1
        elif first2 in edges:
            n_path += 1
        else:
            hits.append("order first2 neither edge nor diagonal")
    print(f"plaquette orders path-start={n_path} diagonal-first={n_diag} total={n_path+n_diag}")
    if n_path != 16 or n_diag != 8:
        hits.append(f"path/diag orders {n_path}/{n_diag} != 16/8")

    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: WITNESS REALIZABILITY (PR #8149): " + "; ".join(hits))
    else:
        print(
            "SUMMARY: WITNESS REALIZABILITY (PR #8149): isolated star is 7 sites "
            "with 0 leaf-leaf edges and 18 outside environment sites; plaquette C4 "
            "has 16 path-start and 8 diagonal-first orders; pattern has purchase "
            "and the witnesses exist as written"
        )


if __name__ == "__main__":
    main()
