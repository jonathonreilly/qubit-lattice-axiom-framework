#!/usr/bin/env python3
"""J:attack-f:PR8080 — NORMALIZATION.

TV 1/2 on 15 two-link channels; C(6,2)=15. Haar/channel counts.
"""
from fractions import Fraction
from math import comb

HITS = []


def tv(mu, nu):
    return Fraction(1, 2) * sum(abs(a - b) for a, b in zip(mu, nu))


def main():
    n = comb(6, 2)
    print(f"C(6,2)={n}")
    if n != 15:
        HITS.append(f"C(6,2)={n}")
    e0 = [Fraction(1)] + [0] * 14
    e1 = [0, Fraction(1)] + [0] * 13
    print(f"TV 15-simplex point masses {tv(e0, e1)}")
    if tv(e0, e1) != 1:
        HITS.append("TV")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - C(6,2)=15 two-link "
        "channels and TV 1/2 on that simplex"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
