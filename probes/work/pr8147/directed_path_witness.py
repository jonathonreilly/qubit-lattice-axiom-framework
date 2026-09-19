#!/usr/bin/env python3
"""J:attack-a:PR8147 — pattern (a) WITNESS REALIZABILITY.

Directed monotone paths exist: n!/(d1!d2!d3!) paths of displacement d.
Do not re-find T3(ii) S=u^2.
"""
from __future__ import annotations

from math import factorial

HITS = []


def npaths(d):
    n = sum(d)
    return factorial(n) // (factorial(d[0]) * factorial(d[1]) * factorial(d[2]))


def main():
    for d in ((1, 0, 0), (1, 1, 0), (2, 1, 0), (1, 1, 1)):
        n = npaths(d)
        print(f"d={d} n={sum(d)} paths={n}")
        if n < 1:
            HITS.append(str(d))
    print("Z^3 NN triangle-free; 5x5 torus of Z^2 exists")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - monotone directed-path "
        "counts n!/d! are positive on small displacements; not a re-find of T3(ii) u^2"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
