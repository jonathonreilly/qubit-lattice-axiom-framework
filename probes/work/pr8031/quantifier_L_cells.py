#!/usr/bin/env python3
"""J:attack-d:PR8031 — |Lambda|=L^3 for L=1..6 of the finite cubic family."""
from itertools import product


def main():
    hits = []
    for L in range(1, 7):
        n = len(list(product(range(L), repeat=3)))
        print(f"L={L} cells={n}")
        if n != L ** 3:
            hits.append(f"HIT: L={L} cells {n} != {L**3}")
            print(hits[-1])
    if hits:
        print("SUMMARY: L^3 fails inside L=1..6")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — |Lambda|=L^3 holds "
        "for every L=1..6 of the finite cubic family"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
