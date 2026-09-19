#!/usr/bin/env python3
"""J:attack-d:PR8024 — QUANTIFIER SCOPE on whole-group 3(L-1)^3 for every L>=1.

Note: for Lambda={0,...,L-1}^3 the whole-group rule retains 3(L-1)^3
plaquettes. Executed L=1,2,3 in the checker. HIT if some L>=1 in 1..12
disagrees. Not the known Casimir-floor HIT.
"""
from __future__ import annotations

from itertools import product

E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def in_box(x, L):
    return all(0 <= x[i] < L for i in range(3))


def add(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def whole_group(L):
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


def main():
    hits = []
    for L in range(1, 9):
        wg = whole_group(L)
        st = 3 * (L - 1) ** 3
        print(f"L={L} whole-group={wg} stated={st}")
        if wg != st:
            hits.append(f"L={L} {wg}!={st}")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: QUANTIFIER SCOPE (PR #8024): " + "; ".join(hits))
    else:
        print(
            "SUMMARY: QUANTIFIER SCOPE on whole-group 3(L-1)^3 (PR #8024): holds "
            "for every L=1..8 (beyond the checker's L=1,2,3); no in-range failure; "
            "the independent-of-Lambda gap itself is not a finite identity to break"
        )


if __name__ == "__main__":
    main()
