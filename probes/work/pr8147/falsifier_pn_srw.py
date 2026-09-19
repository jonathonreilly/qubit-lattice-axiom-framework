#!/usr/bin/env python3
"""J:falsifier:PR8147 — SRW return P_{2n} closed form vs count, n=0..6.

Not the known T3(ii) u^2 vs 4 sin^2(u/2) HIT.
P_{2n}(0)=6^{-2n} C(2n,n) sum_a C(n,a)^2 C(2(n-a),n-a).
HIT if the two formulas disagree.
"""
from math import comb, factorial

HITS = []


def formula(n):
    s = sum(comb(n, a) ** 2 * comb(2 * (n - a), n - a) for a in range(n + 1))
    return comb(2 * n, n) * s


def triple(n):
    acc = 0
    for a in range(n + 1):
        for b in range(n - a + 1):
            c = n - a - b
            acc += factorial(2 * n) // (
                factorial(a) ** 2 * factorial(b) ** 2 * factorial(c) ** 2
            )
    return acc


def main():
    for n in range(0, 7):
        f, t = formula(n), triple(n)
        print(f"n={n}: formula={f} triple={t} P={f}/6^{2*n}")
        if f != t:
            HITS.append(f"n={n} {f}!={t}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: falsifier FIRED: " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: P_{2n} falsifier did not fire: Vandermonde and triple "
        "counts agree for n=0..6 (not the known T3(ii) u^2 HIT)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
