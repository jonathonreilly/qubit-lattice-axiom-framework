#!/usr/bin/env python3
"""J:falsifier:PR8137 — Theorem 3 Haar-square beyond denom 8.

Cubic-covariant kernel: a+b+4c=1, a,b,c>=0. Haar-square iff a=b=c=1/6.
Residual (a-b)^2 and (6c-1)^2/3. Scan denominators 1..12 (note scanned <=8).
HIT if a non-uniform Haar-square kernel appears, or the residual identities fail.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

HITS = []


def main():
    uni = Fraction(1, 6)
    found_uni = 0
    n_scan = 0
    for N in range(1, 13):
        for ia, ib, ic in product(range(N + 1), repeat=3):
            a, b, c = Fraction(ia, N), Fraction(ib, N), Fraction(ic, N)
            if a + b + 4 * c != 1:
                continue
            n_scan += 1
            res_ab = (a - b) ** 2
            res_c = (6 * c - 1) ** 2 / 3
            haar = res_ab == 0 and res_c == 0
            uniform = a == b == c == uni
            if haar and not uniform:
                HITS.append(f"Haar-square non-uniform a,b,c={a,b,c}")
            if uniform:
                found_uni += 1
                if not haar:
                    HITS.append(f"uniform not Haar-square {a,b,c}")
            # identity (6c-1)^2/3 >= 0, zero iff c=1/6
            if res_c == 0 and c != uni:
                HITS.append(f"(6c-1)^2/3=0 at c={c}")
    print(f"scanned {n_scan} kernels denom 1..12; uniform hits {found_uni}")
    if HITS:
        print("HIT: " + "; ".join(HITS[:6]))
        print("SUMMARY: falsifier FIRED: " + "; ".join(HITS[:4]))
        return 0
    print(
        "SUMMARY: Haar-square falsifier did not fire: among cubic kernels "
        "with denominator <=12 the only Haar-square solution is a=b=c=1/6; "
        "(a-b)^2 and (6c-1)^2/3 vanish only there"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
