#!/usr/bin/env python3
"""J:attack-b:PR8153 — same E(k)=0 test on zero vs nonzero torus modes.

G2/G5: infrared bound uses 1/E(k) for k!=0. Same test: E(k)=sum_i 2(1-cos k_i)
vanishes iff k=0. HIT if a nonzero mode has E=0 or the zero mode has E!=0.
"""
from __future__ import annotations

import math
from itertools import product


def E(k):
    return sum(2 * (1 - math.cos(ki)) for ki in k)


def main():
    hits = []
    L = 4
    for n in product(range(L), repeat=3):
        k = tuple(2 * math.pi * ni / L for ni in n)
        e = E(k)
        zero = n == (0, 0, 0)
        if zero and e > 1e-12:
            hits.append(f"HIT: E(0)={e} != 0")
            print(hits[-1])
        if (not zero) and e <= 1e-12:
            hits.append(f"HIT: E=0 at nonzero mode {n}")
            print(hits[-1])
    print(f"4^3 modes: E(0)=0 and E>0 off zero (checked {L**3})")
    if hits:
        print("SUMMARY: E(k)=0 test does not separate zero from nonzero modes")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — the same E(k)=0 test "
        "holds only at the zero mode of the 4^3 torus, so 1/E(k) is defined "
        "exactly on the nonzero modes used by G2/G5"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
