#!/usr/bin/env python3
"""J:attack-d:PR8030 — xy-plaquette link disjointness at extra n.

Note executed n=6 spacing 2 and n=4 spacing 3. Quantifier: also n=2,3
spacing 2 and n=2,3 spacing 3. HIT if two anchors share a link.
"""
from __future__ import annotations

import itertools


def xy_plaquette_links(x, y, z):
    a, b, c, d = (x, y, z), (x + 1, y, z), (x + 1, y + 1, z), (x, y + 1, z)
    edges = [(a, b), (b, c), (c, d), (d, a)]
    return frozenset(tuple(sorted(e)) for e in edges)


def census(spacing, n):
    anchors = list(itertools.product(range(n), repeat=3))
    links = {}
    for i, j, k in anchors:
        links[(i, j, k)] = xy_plaquette_links(spacing * i, spacing * j, spacing * k)
    hits = []
    for a, b in itertools.combinations(anchors, 2):
        inter = links[a] & links[b]
        if inter:
            hits.append((a, b, inter))
    return len(anchors), hits


def main():
    bad = []
    for spacing, n in ((2, 2), (2, 3), (2, 6), (3, 2), (3, 3), (3, 4)):
        nanc, hits = census(spacing, n)
        print(f"spacing={spacing} n={n}: plaquettes={nanc} shared-pairs={len(hits)}")
        if hits:
            bad.append((spacing, n, hits[:2]))
            print("HIT: overlapping links", spacing, n, hits[:2])
    if bad:
        print("SUMMARY: disjoint-link claim fails at extra n inside the stated range")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — xy-plaquette link "
        "disjointness holds at extra n=2,3 as well as the executed n=6 "
        "spacing-2 and n=4 spacing-3"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
