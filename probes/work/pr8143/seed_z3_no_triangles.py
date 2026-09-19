#!/usr/bin/env python3
"""J:attack-a:PR8143 — seed geometry in Z^3 is triangle-free (independent of generator sim).

Section 3: T={(x,0,0): x=0..3L-1}, a0=(-1,0,0), p_j=(3j,-1,0), k_j=(3j+2,1,0),
|C|=1+5L. HIT if sites collide, |C|!=1+5L, or the nn graph on C has a triangle.
"""
from __future__ import annotations

from itertools import combinations


def nn(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) == 1


def seed(L):
    T = [(x, 0, 0) for x in range(3 * L)]
    a0 = (-1, 0, 0)
    pj = [(3 * j, -1, 0) for j in range(L)]
    kj = [(3 * j + 2, 1, 0) for j in range(L)]
    C = T + [a0] + pj + kj
    return C


def main():
    hits = []
    for L in range(1, 9):
        C = seed(L)
        n = len(C)
        nd = len(set(C))
        want = 1 + 5 * L
        tris = [
            t
            for t in combinations(C, 3)
            if nn(t[0], t[1]) and nn(t[1], t[2]) and nn(t[2], t[0])
        ]
        print(f"L={L}: |C|={n} distinct={nd} want={want} triangles={len(tris)}")
        if n != want or nd != want:
            hits.append(f"HIT: L={L} |C|={n} distinct={nd} != {want}")
            print(hits[-1])
        if tris:
            hits.append(f"HIT: L={L} seed graph has a triangle {tris[0]}")
            print(hits[-1])
    if hits:
        print("SUMMARY: seed C is not a triangle-free Z^3 point set of size 1+5L")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — the section-3 seed "
        "C=T∪{a0}∪{p_j}∪{k_j} has |C|=1+5L distinct Z^3 sites and a triangle-free "
        "nn graph for L=1..8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
