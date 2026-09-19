#!/usr/bin/env python3
"""J:falsifier:PR8030 — disjoint xy-plaquette links beyond executed n.

Section 4: N=n^3 disjoint elementary xy plaquettes at (spacing*i, spacing*j,
spacing*k). Executed n=6 spacing 2 and n=4 spacing 3. Beyond: n=8 spacing 2
and n=6,7 spacing 3. HIT if two distinct anchors share a link.
"""
from __future__ import annotations

from itertools import combinations, product

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def xy_links(x, y, z):
    a, b, c, d = (x, y, z), (x + 1, y, z), (x + 1, y + 1, z), (x, y + 1, z)
    return frozenset(tuple(sorted(e)) for e in ((a, b), (b, c), (c, d), (d, a)))


def main() -> int:
    for spacing, n in ((2, 8), (3, 6), (3, 7)):
        anchors = list(product(range(n), repeat=3))
        links = {a: xy_links(spacing * a[0], spacing * a[1], spacing * a[2]) for a in anchors}
        shared = 0
        for a, b in combinations(anchors, 2):
            if links[a] & links[b]:
                shared += 1
                if shared <= 2:
                    hit(f"spacing={spacing} n={n} {a} shares with {b}")
        print(f"spacing={spacing} n={n}: {len(anchors)} plaquettes, shared-pairs={shared}")
    if HITS:
        print("SUMMARY: disjoint-plaquette falsifier FIRED - " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: xy-plaquette links remain pairwise disjoint for n=8 spacing 2 "
        "and n=6,7 spacing 3 (beyond executed n=6/4); falsifier does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
