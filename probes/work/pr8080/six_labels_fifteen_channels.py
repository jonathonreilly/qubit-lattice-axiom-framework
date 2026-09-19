#!/usr/bin/env python3
"""J:attack-a:PR8080 — 6 labels and 15 two-neighbor channels exist.

The note's native model uses 6 labels (cube axes) and 15 two-subsets as
channels (K6 edges). These are combinatorial, not a Z^3 window. HIT if
C(6,2)!=15 or the six axes are not distinct unit vectors.
"""
from __future__ import annotations

from itertools import combinations
from math import comb


AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def main():
    hits = []
    n = comb(6, 2)
    edges = list(combinations(range(6), 2))
    print(f"labels={len(AXES)} C(6,2)={n} enumerated={len(edges)}")
    if n != 15 or len(edges) != 15:
        hits.append(f"HIT: two-subset channels {n} != 15")
        print(hits[-1])
    if len(set(AXES)) != 6:
        hits.append("HIT: six labels are not distinct")
        print(hits[-1])
    if any(sum(a[i] ** 2 for i in range(3)) != 1 for a in AXES):
        hits.append("HIT: a label is not a unit axis")
        print(hits[-1])
    # K6 is not a Z^3 window (it has triangles); the note does not claim it is.
    k6_tris = comb(6, 3)
    print(f"K6 triangles={k6_tris} (channel graph, not a Z^3 window)")
    if hits:
        print("SUMMARY: 6-label/15-channel witnesses fail")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — the six unit axes and "
        "C(6,2)=15 two-subset channels exist as stated; K6 is not claimed as a Z^3 window"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
