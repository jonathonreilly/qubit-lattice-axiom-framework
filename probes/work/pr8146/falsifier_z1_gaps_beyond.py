#!/usr/bin/env python3
"""J:falsifier:PR8146 — D3: |p-q|<Z1 and |p+q-2r|<Z1 for positive triples.

Z1=p+q+4r. Falsifier: a positive triple with |p-q|≥Z1 or |p+q-2r|≥Z1.
Beyond the note: integer grid 1..30 and extra rationals. Do not re-find
the known 2:1 majority iff HIT at (5,2,4).
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def main() -> int:
    n = 0
    for p, q, r in product(range(1, 31), repeat=3):
        n += 1
        Z1 = p + q + 4 * r
        if abs(p - q) >= Z1 or abs(p + q - 2 * r) >= Z1:
            hit(f"D3 fails at ({p},{q},{r}): Z1={Z1}")
            break
    else:
        print(f"integer grid 1..30^3: {n} triples, D3 holds")
    extra = [
        (Fraction(3), Fraction(1), Fraction(2)),
        (Fraction(5), Fraction(2), Fraction(4)),
        (Fraction(100), Fraction(1), Fraction(1)),
        (Fraction(1), Fraction(100), Fraction(1)),
        (Fraction(1, 10), Fraction(1, 10), Fraction(1, 10)),
    ]
    for p, q, r in extra:
        Z1 = p + q + 4 * r
        ok = abs(p - q) < Z1 and abs(p + q - 2 * r) < Z1
        print(f"  {(p, q, r)} Z1={Z1} D3={ok}")
        if not ok:
            hit(f"D3 fails at extra {(p, q, r)}")
    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: D3 Z1-gap falsifier FIRED: " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: D3 Z1-gap falsifier did not fire: |p-q|<Z1 and |p+q-2r|<Z1 "
        "on the 30^3 positive integer grid and extra rationals (known 2:1 "
        "majority HIT at (5,2,4) not re-claimed)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
