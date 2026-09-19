#!/usr/bin/env python3
"""J:attack-a:PR8080 — WITNESS REALIZABILITY of the 15 two-link channels.

Note: 'The fifteen two-link channels carry the disjoint...'  On Z^3 a site has
six NN directions; C(6,2)=15 unordered pairs (two-link stars, not triangles).
If that is not the intended graph, the note states no other window/graph
witness. HIT if C(6,2)!=15 or some pair of directions is a lattice triangle.
"""
from __future__ import annotations

from itertools import combinations

STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def main():
    n = len(STEPS)
    pairs = list(combinations(range(n), 2))
    print(f"NN directions={n} unordered pairs={len(pairs)} stated 15")
    hits = []
    if len(pairs) != 15:
        hits.append(f"C({n},2)={len(pairs)} != 15")
    triangles = 0
    for i, j in pairs:
        a, b = STEPS[i], STEPS[j]
        d = sum(abs(a[k] - b[k]) for k in range(3))
        # two directions from the origin form a triangle only if a~b
        if d == 1:
            triangles += 1
            hits.append(f"directions {a},{b} adjacent")
    print(f"two-link stars that are triangles: {triangles}")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: WITNESS REALIZABILITY (PR #8080): " + "; ".join(hits))
    else:
        print(
            "SUMMARY: WITNESS REALIZABILITY (PR #8080): the fifteen two-link "
            "channels match C(6,2) unordered pairs of Z^3 NN directions, each a "
            "2-star not a triangle; pattern has purchase and the witnesses exist as written"
        )


if __name__ == "__main__":
    main()
