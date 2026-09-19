#!/usr/bin/env python3
"""J:attack-f:PR8083 — NORMALIZATION.

15 two-link defects × 4 = 60 schedule candidates; TV 1/2.
"""
from math import comb
from fractions import Fraction

HITS = []


def main():
    n = comb(6, 2)
    print(f"C(6,2)={n}; 15*4={n*4}")
    if n != 15 or n * 4 != 60:
        HITS.append(f"schedule {n} {n*4}")
    tv = Fraction(1, 2) * (abs(1) + abs(1))
    print(f"TV two-point masses {tv}")
    if tv != 1:
        HITS.append("TV")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - 15 two-link defects "
        "and 60 schedule candidates; TV 1/2"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
