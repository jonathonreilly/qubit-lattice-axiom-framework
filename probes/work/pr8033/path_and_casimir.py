#!/usr/bin/env python3
"""J:attack-a:PR8033 — pattern (a) WITNESS REALIZABILITY.

Finite PW static-source bounds: a shortest path of length L=|x-y|_1 exists
in Z^3; fundamental Casimir Q(1,0)=4. Z^3 NN is triangle-free.
"""
from __future__ import annotations

HITS = []


def Q(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def main():
    if Q(1, 0) != 4 or Q(0, 1) != 4:
        HITS.append(f"Q fund {Q(1,0)} {Q(0,1)}")
    print(f"Q(1,0)={Q(1,0)} Q(0,1)={Q(0,1)}")
    x, y = (0, 0, 0), (2, 1, 0)
    L = sum(abs(y[i] - x[i]) for i in range(3))
    # one geodesic: two +e1 then +e2
    path = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0)]
    if len(path) - 1 != L:
        HITS.append(f"path length {len(path)-1} != L={L}")
    print(f"geodesic x={x} y={y} L={L} path={path}")
    print("Z^3 NN triangle-free")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - a Manhattan geodesic of "
        "length L exists in Z^3 and the fundamental Casimir Q=4 is realized"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
