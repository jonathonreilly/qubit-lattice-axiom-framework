#!/usr/bin/env python3
"""J:attack-d:PR8175 — QUANTIFIER SCOPE.

T1.1: M_k(v-e_j)-M_k(v)=1/3-δ_{jk} for every site and directions j,k.
Executed on a box. Check every z in {-2..2}^3 and every j,k in 0,1,2.
Not a re-run of the attack-g period census.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
HITS = []


def tau(z):
    return z[0] + z[1] + z[2]


def M(k, z):
    return Fraction(z[k]) - Fraction(tau(z), 3)


def main():
    for z in product(range(-2, 3), repeat=3):
        for j in range(3):
            w = (z[0] - E[j][0], z[1] - E[j][1], z[2] - E[j][2])
            for k in range(3):
                got = M(k, w) - M(k, z)
                want = Fraction(1, 3) - (1 if j == k else 0)
                if got != want:
                    HITS.append(f"z={z} j={j} k={k}: {got} != {want}")
                    break
            else:
                continue
            break
        else:
            continue
        break
    n = 5 ** 3 * 3 * 3
    print(f"M_k increment on {n} (z,j,k) triples: {'FAIL' if HITS else 'OK'}")
    if HITS:
        print("HIT: " + "; ".join(HITS[:4]))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - M_k(v-e_j)-M_k(v)="
        "1/3-δ_{jk} holds for every z in {-2..2}^3 and every directions j,k"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
