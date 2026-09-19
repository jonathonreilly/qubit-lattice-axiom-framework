#!/usr/bin/env python3
"""J:attack-d:PR8033 — quantifier scope: cell counts L^3 for L=1..8.

Finite-volume family on Lambda={0,...,L-1}^3 has L^3 cells. HIT if the
count fails at a size in the executed range L=1..8.
"""
from __future__ import annotations

from itertools import product


def main():
    hits = []
    for L in range(1, 9):
        n = len(list(product(range(L), repeat=3)))
        print(f"L={L}: cells={n} want {L**3}")
        if n != L ** 3:
            hits.append(f"HIT: L={L} cells {n} != {L**3}")
            print(hits[-1])
    if hits:
        print("SUMMARY: L^3 cell count fails inside L=1..8")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — |Lambda|=L^3 holds "
        "for every L=1..8 of the finite cubic family"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
