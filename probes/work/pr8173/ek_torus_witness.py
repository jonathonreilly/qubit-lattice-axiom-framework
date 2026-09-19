#!/usr/bin/env python3
"""J:attack-a:PR8173 — pattern (a) WITNESS REALIZABILITY.

E(k)=2 sum_j (1-cos k_j) is nonnegative on T_L^3 and vanishes only at k=0,
so G_L(r)=N^{-1} sum_{k!=0} e^{ik.r}/E(k) is well-defined. Do not re-find
the 0.86-0.98 kernel-grid HIT.
"""
from __future__ import annotations

import itertools
import math

HITS = []


def E(n, L):
    return sum(2 * (1 - math.cos(2 * math.pi * nj / L)) for nj in n)


def main():
    for L in (2, 3, 4):
        zeros = []
        negs = []
        for n in itertools.product(range(L), repeat=3):
            val = E(n, L)
            if n == (0, 0, 0):
                if abs(val) > 1e-12:
                    zeros.append((n, val))
            else:
                if val <= 1e-12:
                    zeros.append((n, val))
                if val < -1e-12:
                    negs.append((n, val))
        print(f"L={L}: E(0)={E((0,0,0),L):.2e} nonzero-mode min E={min(E(n,L) for n in itertools.product(range(L),repeat=3) if n!=(0,0,0)):.6f}")
        if zeros:
            HITS.append(f"L={L} unexpected zeros {zeros[:3]}")
        if negs:
            HITS.append(f"L={L} negative E")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (a) WITNESS REALIZABILITY - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - E(k)>=0 on T_L^3 for "
        "L=2,3,4 with kernel only at k=0, so G_L is defined; not a re-find of "
        "the 0.86-0.98 kernel HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
