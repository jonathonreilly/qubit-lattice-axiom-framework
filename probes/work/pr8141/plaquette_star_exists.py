#!/usr/bin/env python3
"""J:attack-a:PR8141 — pattern (a) WITNESS REALIZABILITY.

Plaquette 4-cycle and star (center + 6 NN) exist in Z^3; Z^3 is bipartite
so the plaquette is not a triangle.
"""
from __future__ import annotations

HITS = []


def nn(a, b):
    return sum(abs(a[i] - b[i]) for i in range(3)) == 1


def main():
    plaq = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    cyc = all(nn(plaq[i], plaq[(i + 1) % 4]) for i in range(4))
    diag = nn(plaq[0], plaq[2])
    print(f"plaquette 4-cycle NN? {cyc} has diagonal NN? {diag}")
    if not cyc or diag:
        HITS.append("plaquette")
    c = (0, 0, 0)
    star = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    if not all(nn(c, s) for s in star) or len(star) != 6:
        HITS.append("star")
    print(f"star 6 NN of origin: {star}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the plaquette is a "
        "4-cycle without diagonals and the 6-neighbour star exists in Z^3"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
