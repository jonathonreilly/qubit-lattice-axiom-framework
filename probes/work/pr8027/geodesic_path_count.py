#!/usr/bin/env python3
"""J:attack-a:PR8027 — pattern (a) WITNESS REALIZABILITY.

The note: for displacement (n1,n2,n3) after reflections, all ni>=0,
the number of oriented shortest paths is L!/(n1! n2! n3!), L=n1+n2+n3.
Witnesses exist in Z^3 (bipartite, no NN triangles). HIT if the enumerated
word count differs, or if a shortest path leaves the axis-aligned box.
"""
from __future__ import annotations

from itertools import permutations
from math import factorial

HITS = []


def npaths(n1, n2, n3):
    L = n1 + n2 + n3
    return factorial(L) // (factorial(n1) * factorial(n2) * factorial(n3))


def enumerate_words(n1, n2, n3):
    letters = (0,) * n1 + (1,) * n2 + (2,) * n3
    return set(permutations(letters))


def main():
    # Z^3 NN triangle-free
    nn = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    tri = False
    for a in nn:
        for b in nn:
            if a >= b:
                continue
            if sum(abs(a[i] - b[i]) for i in range(3)) == 1:
                tri = True
    print(f"Z^3 NN triangle? {tri}")
    if tri:
        HITS.append("Z^3 NN triangle")

    for n in [(1, 0, 0), (1, 1, 0), (2, 1, 0), (1, 1, 1), (2, 2, 1), (3, 1, 1)]:
        L = sum(n)
        want = npaths(*n)
        got = len(enumerate_words(*n))
        print(f"n={n} L={L} L!/n!={want} enumerated words={got}")
        if want != got:
            HITS.append(f"{n}: {want} vs {got}")
        # every word stays in the box [0,n1]x[0,n2]x[0,n3]
        e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        for w in enumerate_words(*n):
            x = [0, 0, 0]
            for step in w:
                x[step] += 1
                if x[0] > n[0] or x[1] > n[1] or x[2] > n[2]:
                    HITS.append(f"path left box {n} at {x}")
                    break
            if tuple(x) != n:
                HITS.append(f"word {w} ended at {x} not {n}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print(
            "SUMMARY: attack pattern (a) WITNESS REALIZABILITY on geodesic path "
            "counts - " + "; ".join(HITS)
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - shortest-path witnesses "
        "exist: word counts equal L!/(n1!n2!n3!) on six small displacements, "
        "all stay in the axis-aligned box, and Z^3 NN is triangle-free"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
