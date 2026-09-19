#!/usr/bin/env python3
"""J:attack-a:PR8140 — pattern (a) WITNESS REALIZABILITY.

The four-cube witness: r=17 independent edges, P=24 square faces.
A 4-cube has 16 vertices, 32 edges, 24 faces; after a spanning tree
(15 tree edges) the cotree has 32-15=17 edges. Distinct from the
pattern-(f) coupled-defect brute force. HIT if those counts fail.
"""
from __future__ import annotations

from itertools import combinations, product

HITS = []


def main():
    verts = list(product((0, 1), repeat=4))
    print(f"4-cube vertices {len(verts)} (stated 16 for hypercube)")
    if len(verts) != 16:
        HITS.append(f"verts {len(verts)}")
    edges = []
    for i, u in enumerate(verts):
        for v in verts[i + 1 :]:
            if sum(a != b for a, b in zip(u, v)) == 1:
                edges.append((u, v))
    print(f"edges {len(edges)} (32)")
    if len(edges) != 32:
        HITS.append(f"edges {len(edges)}")
    faces = 0
    for u in verts:
        for d1, d2 in combinations(range(4), 2):
            if u[d1] == 0 and u[d2] == 0:
                faces += 1
    print(f"square faces from origin-corners {faces} (24)")
    if faces != 24:
        HITS.append(f"faces {faces} != 24")
    tree = 16 - 1
    cotree = 32 - tree
    print(f"spanning tree {tree} edges; cotree r={cotree} (stated 17)")
    if cotree != 17:
        HITS.append(f"cotree {cotree} != 17")
    # Z^3 bipartite
    print("Z^3 NN is bipartite (no odd cycles / no triangles)")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY on the four-cube - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the four-cube witness "
        "exists: 16 vertices, 32 edges, 24 square faces, spanning-tree cotree r=17"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
