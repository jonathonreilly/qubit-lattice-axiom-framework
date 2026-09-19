#!/usr/bin/env python3
"""J:falsifier:PR8142 — X1: both K2 mixed-difference ratios =1 only if p=q=r.

Falsifier bullet: both K2 ratios of X1 equal to 1 at some nonconstant triple.
Beyond the note's (3,1,2),(5,2,4): integer grid 1≤q,r≤p≤12 and extra
rationals. HIT if both ratios are 1 off the constant ray.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def ratios(p, q, r):
    # closed forms from the six-axis product rule (orbit p,q,r)
    r1 = ((p ** 2 + q ** 2 + 4 * r ** 2) / (2 * (p * q + 2 * r ** 2))) ** 2
    r2 = ((p ** 2 + q ** 2 + 4 * r ** 2) / (2 * r * (p + q + r))) ** 2
    return r1, r2


def main() -> int:
    n = 0
    for p, q, r in product(range(1, 13), repeat=3):
        n += 1
        a, b = ratios(Fraction(p), Fraction(q), Fraction(r))
        const = p == q == r
        if a == 1 and b == 1 and not const:
            hit(f"both K2 ratios=1 at nonconstant ({p},{q},{r})")
            break
        if b == 1 and not const:
            hit(f"ratio2=1 at nonconstant ({p},{q},{r})")
            break
    else:
        print(f"integer grid 1..12^3: {n} triples, both ratios=1 only on p=q=r")
    extra = [
        (Fraction(3), Fraction(1), Fraction(2)),
        (Fraction(5), Fraction(2), Fraction(4)),
        (Fraction(7), Fraction(3), Fraction(5)),
        (Fraction(37, 10), Fraction(1), Fraction(2)),
        (Fraction(11), Fraction(10), Fraction(10)),
        (Fraction(100), Fraction(1), Fraction(1)),
    ]
    for trip in extra:
        a, b = ratios(*trip)
        const = trip[0] == trip[1] == trip[2]
        print(f"  {trip}: ratio1={a} ratio2={b}")
        if a == 1 and b == 1 and not const:
            hit(f"both=1 at {trip}")
    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: X1 K2-ratio falsifier FIRED: " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: X1 K2-ratio falsifier did not fire: both mixed-difference "
        "ratios equal 1 only on p=q=r, on the 12^3 integer grid and extra "
        "rationals beyond the note's two declared triples"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
