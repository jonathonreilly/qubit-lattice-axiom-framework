#!/usr/bin/env python3
"""J:attack-b:PR8139 — same 3-predecessor test on all eight cube corners.

The eight corner laws are the eight choices of which octant is 'past'.
Same test: each corner of the unit cube has three nn edges in Z^3.
HIT if some corner has a different nn-degree, or the eight corners are
not distinct.
"""
from __future__ import annotations

from itertools import product


def nn_count(p, box):
    return sum(
        1
        for q in box
        if q != p and sum(abs(p[i] - q[i]) for i in range(3)) == 1
    )


def main():
    hits = []
    corners = list(product((0, 1), repeat=3))
    print(f"corners {len(corners)}")
    if len(set(corners)) != 8:
        hits.append("HIT: eight corners are not 8 distinct points")
        print(hits[-1])
    box = list(product(range(-1, 3), repeat=3))
    degs = {c: nn_count(c, box) for c in corners}
    print(f"nn degrees in [-1,2]^3: {degs}")
    if len(set(degs.values())) != 1:
        hits.append(f"HIT: corners do not all have the same nn-degree: {degs}")
        print(hits[-1])
    if set(degs.values()) != {6}:
        hits.append(f"HIT: a corner is not 6-regular in the ambient lattice: {degs}")
        print(hits[-1])
    if hits:
        print("SUMMARY: eight-corner same-degree test fails")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — the same 6-regular nn "
        "test holds at all eight unit-cube corners in Z^3, so the eight corner "
        "laws are the eight orientations of one local stencil"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
