#!/usr/bin/env python3
"""J:attack-g:PR8030 — brute-force the finite disjoint-link claim of section 4 / independent contact proof.

Note (origin/codex/continuum-boundary-block40-20260907):
  Section 4: N=n^3 disjoint elementary xy plaquettes anchored at (2i,2j,2k).
  Independent contact: xy plaquettes based at 3k; four links disjoint from every other
  chosen plaquette because projected unit-square intervals at distinct multiples of 3
  do not overlap in an edge.

Verify literally by enumerating link sets for n=6 (spacing 2) and n=4 (spacing 3).
HIT if any two distinct anchors share a link. Exact integer coordinates.
"""
from __future__ import annotations

import itertools


def xy_plaquette_links(x, y, z):
    """Four oriented edges of the +xy plaquette based at (x,y,z), as frozen undirected links."""
    a = (x, y, z)
    b = (x + 1, y, z)
    c = (x + 1, y + 1, z)
    d = (x, y + 1, z)
    edges = [(a, b), (b, c), (c, d), (d, a)]
    return frozenset(tuple(sorted(e)) for e in edges)


def census(spacing, n):
    anchors = list(itertools.product(range(n), repeat=3))
    links = {}
    for i, j, k in anchors:
        base = (spacing * i, spacing * j, spacing * k)
        links[(i, j, k)] = xy_plaquette_links(*base)
    hits = []
    for a, b in itertools.combinations(anchors, 2):
        inter = links[a] & links[b]
        if inter:
            hits.append((a, b, inter))
    return len(anchors), hits


def main():
    n2, hits2 = census(2, 6)
    n3, hits3 = census(3, 4)
    print(f"spacing2 n=6: {n2} plaquettes, shared-link pairs={len(hits2)}")
    print(f"spacing3 n=4: {n3} plaquettes, shared-link pairs={len(hits3)}")
    if hits2:
        print("HIT: spacing-2 construction has overlapping links", hits2[:3])
    if hits3:
        print("HIT: spacing-3 construction has overlapping links", hits3[:3])
    if not hits2 and not hits3:
        print(
            "SUMMARY: pattern has no purchase on this note — the finite "
            "xy-plaquette link-disjointness claims (anchors 2k on n=6 and 3k on n=4) "
            "hold literally by enumeration of all pairs"
        )
        return 0
    print("SUMMARY: disjoint-link claim fails under brute-force pair enumeration")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
