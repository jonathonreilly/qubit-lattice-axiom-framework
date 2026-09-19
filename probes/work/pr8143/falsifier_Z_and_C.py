#!/usr/bin/env python3
"""J:falsifier:PR8143 — Z>=3/4 and |C|=1+5L beyond L=5.

HIT if Z dips below 3/4 on a nonnegative grid or |C|!=1+5L for L=1..30.
"""
from fractions import Fraction

HITS = []


def Z(S):
    return S + (S - 1) ** 2


def seed_C(L):
    T = [(x, 0, 0) for x in range(3 * L)]
    a0 = (-1, 0, 0)
    pj = [(3 * j, -1, 0) for j in range(L)]
    kj = [(3 * j + 2, 1, 0) for j in range(L)]
    return T + [a0] + pj + kj


def main():
    for n in range(0, 41):
        s = Fraction(n, 8)
        z = Z(s)
        if z < Fraction(3, 4):
            HITS.append(f"Z({s})={z}")
    print("Z>=3/4 on S=0..5 step 1/8")
    for L in range(1, 31):
        C = seed_C(L)
        if len(C) != 1 + 5 * L or len(set(C)) != len(C):
            HITS.append(f"|C| L={L}")
    print("|C|=1+5L distinct for L=1..30")
    if HITS:
        print("HIT: " + "; ".join(HITS[:4]))
        print("SUMMARY: falsifier FIRED: " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: Z-and-C falsifier did not fire: Z>=3/4 on the grid and "
        "|C|=1+5L distinct for L=1..30"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
