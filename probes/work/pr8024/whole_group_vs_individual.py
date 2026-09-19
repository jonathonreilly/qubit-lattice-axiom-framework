#!/usr/bin/env python3
"""J:attack-b:PR8024 — SAME TEST, BOTH SIDES: whole-group vs individual plaquettes.

Note: whole-group on Lambda={0..L-1}^3 retains 3(L-1)^3 plaquettes, not every
individually supported plaquette. Identical test: count plaquettes under both
rules. Not the known Casimir-floor HIT.
"""
from __future__ import annotations

from itertools import product

E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def in_box(x, L):
    return all(0 <= x[i] < L for i in range(3))


def add(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def whole_group(L):
    # cells x in Lambda with all three outgoing plaquettes using vertices in box
    n = 0
    for x in product(range(L), repeat=3):
        ok = True
        for i in range(3):
            for j in range(i + 1, 3):
                verts = [x, add(x, E[i]), add(x, E[j]), add(add(x, E[i]), E[j])]
                if not all(in_box(v, L) for v in verts):
                    ok = False
        if ok:
            n += 3
    return n


def individual(L):
    # every oriented i<j plaquette whose 4 vertices lie in Lambda
    n = 0
    for x in product(range(L), repeat=3):
        for i in range(3):
            for j in range(i + 1, 3):
                verts = [x, add(x, E[i]), add(x, E[j]), add(add(x, E[i]), E[j])]
                if all(in_box(v, L) for v in verts):
                    n += 1
    return n


def main():
    hits = []
    for L in range(1, 6):
        wg, ind = whole_group(L), individual(L)
        stated = 3 * (L - 1) ** 3
        print(f"L={L} whole-group={wg} stated={stated} individual={ind} differ={wg!=ind}")
        if wg != stated:
            hits.append(f"L={L} whole-group {wg} != 3(L-1)^3={stated}")
        if L >= 2 and wg == ind:
            hits.append(f"L={L} whole-group equals individual ({wg}); does not separate")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: SAME TEST BOTH SIDES (PR #8024): " + "; ".join(hits[:3]))
    else:
        print(
            "SUMMARY: SAME TEST BOTH SIDES on whole-group vs individual plaquettes "
            "(PR #8024): for L=2..5 the identical 4-vertex-in-box count finds "
            "whole-group=3(L-1)^3 strictly below the individual total; the "
            "separation holds as written"
        )


if __name__ == "__main__":
    main()
