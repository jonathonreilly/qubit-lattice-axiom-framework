#!/usr/bin/env python3
"""J:attack-g:PR8156 — brute-force V1's closed-walk count, literally.

Note (PR #8156): P_{2n}(0,0) = 6^{-2n} C(2n,n) sum_a C(n,a)^2 C(2(n-a), n-a)
and #{closed walks of length 2n} = sum_{a+b+c=n} (2n)! / (a! a! b! b! c! c!).
V1 says the closed-walk count was executed by enumeration for n <= 3.
This script enumerates all 6^{2n} walks for n = 0..4 and compares both formulas
exactly (integers / Fraction). Pattern: PROOF STEP BY BRUTE FORCE, one step (V1).
"""
from __future__ import annotations

from fractions import Fraction as Fr
from itertools import product
from math import comb, factorial


def formula_count(n: int) -> int:
    """C(2n,n) * sum_a C(n,a)^2 C(2(n-a), n-a)."""
    s = sum(comb(n, a) ** 2 * comb(2 * (n - a), n - a) for a in range(n + 1))
    return comb(2 * n, n) * s


def triple_count(n: int) -> int:
    """sum_{a+b+c=n} (2n)! / (a!^2 b!^2 c!^2)."""
    acc = 0
    for a in range(n + 1):
        for b in range(n - a + 1):
            c = n - a - b
            acc += factorial(2 * n) // (
                factorial(a) ** 2 * factorial(b) ** 2 * factorial(c) ** 2
            )
    return acc


def enumerate_closed(n: int) -> int:
    """Number of length-2n walks on Z^3 with steps +-e_i that return to 0."""
    dirs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    closed = 0
    L = 2 * n
    for steps in product(range(6), repeat=L):
        x = y = z = 0
        for s in steps:
            dx, dy, dz = dirs[s]
            x += dx
            y += dy
            z += dz
        if x == y == z == 0:
            closed += 1
    return closed


def main() -> int:
    hits = []
    print("V1 closed-walk count: enumeration vs C(2n,n) sum_a C(n,a)^2 C(2(n-a),n-a) vs sum_{a+b+c=n} (2n)!/(a!^2 b!^2 c!^2)")
    for n in range(0, 5):
        f = formula_count(n)
        t = triple_count(n)
        if f != t:
            hits.append(
                f"HIT: V1's two closed-form counts disagree at n={n}: Vandermonde {f} vs triple {t}"
            )
        if n <= 4:
            e = enumerate_closed(n)
            print(f"  n={n}: enum={e}  Vandermonde={f}  triple={t}  6^{2*n}={6**(2*n)}")
            if e != f:
                hits.append(
                    f"HIT: V1 closed-walk formula fails enumeration at n={n}: enum {e} vs formula {f}"
                )
        P = Fr(f, 6 ** (2 * n))
        print(f"       P_{{{2*n}}}(0,0) = {P}")
    # odd length cannot close: length 1 and 3
    for L in (1, 3):
        dirs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
        closed = 0
        for steps in product(range(6), repeat=L):
            x = y = z = 0
            for s in steps:
                dx, dy, dz = dirs[s]
                x += dx
                y += dy
                z += dz
            if x == y == z == 0:
                closed += 1
        print(f"  odd length {L}: closed={closed} (V1: 0)")
        if closed != 0:
            hits.append(f"HIT: V1 says odd walks cannot close; length {L} has {closed} closed walks")
    if hits:
        for h in hits:
            print(h)
        print("SUMMARY: V1 closed-walk identity fails brute-force enumeration")
    else:
        print(
            "SUMMARY: PROOF STEP BY BRUTE FORCE on V1 (PR #8156): closed-walk count "
            "matches enumeration at n=0..4 (6^{8}=1679616 walks at n=4) and both "
            "Vandermonde and triple formulas; odd lengths 1,3 have zero closed walks; "
            "pattern has purchase and the step holds as written"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
