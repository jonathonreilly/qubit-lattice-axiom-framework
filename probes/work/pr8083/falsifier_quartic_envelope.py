#!/usr/bin/env python3
"""J:falsifier:PR8083 — Q_{t,u}(x) ≥ x^{-2} for x ≥ δ=1/4.

Note: P(x)=(x-δ)(x-t)^2(x-u)^2, B=(δ t^2 u^2)^{-1}, A=B(δ^{-1}+2/t+2/u),
Q=(1+P(Ax+B))/x^2, and Q-x^{-2}=P(Ax+B)/x^2 ≥ 0 for x≥δ.

Machinery disjoint from the compact receipt runner: sympy polynomial
identity plus a dense Fraction/float grid. Beyond the note's 15 pairs
from {1,2,4,8,16}: extra (t,u) including 1/2, 3, 5, 32, 64 and x up to
10^4. HIT if Q < x^{-2} at any tested x≥δ.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations_with_replacement

import sympy as sp

DELTA = Fraction(1, 4)
HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def AB(t, u, delta=DELTA):
    B = 1 / (delta * t * t * u * u)
    A = B * (1 / delta + 2 / t + 2 / u)
    return A, B


def Q_minus_invsq(x, t, u, delta=DELTA):
    A, B = AB(t, u, delta)
    P = (x - delta) * (x - t) ** 2 * (x - u) ** 2
    return P * (A * x + B) / (x * x)


def main() -> int:
    x, t, u, d = sp.symbols("x t u delta", positive=True)
    B = 1 / (d * t ** 2 * u ** 2)
    A = B * (1 / d + 2 / t + 2 / u)
    P = (x - d) * (x - t) ** 2 * (x - u) ** 2
    Q = (1 + P * (A * x + B)) / x ** 2
    gap = sp.simplify(Q - 1 / x ** 2 - P * (A * x + B) / x ** 2)
    print(f"symbolic gap (Q-1/x^2 - P(Ax+B)/x^2) = {gap}")
    if gap != 0:
        hit(f"algebraic identity failed: {gap}")

    schedule = list(combinations_with_replacement(
        [Fraction(1), Fraction(2), Fraction(4), Fraction(8), Fraction(16)], 2
    ))
    extra = [
        (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(1, 2), Fraction(2)),
        (Fraction(3), Fraction(5)),
        (Fraction(32), Fraction(64)),
        (Fraction(1, 4), Fraction(1)),
        (Fraction(7), Fraction(11)),
    ]
    xs = (
        [DELTA, DELTA + Fraction(1, 100), Fraction(1, 3), Fraction(1, 2)]
        + [Fraction(n) for n in range(1, 21)]
        + [Fraction(100), Fraction(1000), Fraction(10000)]
    )
    pairs = schedule + extra
    print(f"pairs: {len(schedule)} schedule + {len(extra)} beyond")
    nchk = 0
    for tt, uu in pairs:
        A, B = AB(tt, uu)
        if A <= 0 or B <= 0:
            hit(f"A or B nonpositive at t={tt} u={uu}: A={A} B={B}")
        for xx in xs:
            if xx < DELTA:
                continue
            val = Q_minus_invsq(xx, tt, uu)
            nchk += 1
            if val < 0:
                hit(f"Q-1/x^2={val} < 0 at t={tt} u={uu} x={xx}")
                break
        else:
            continue
        break
    print(f"grid checks: {nchk} all nonnegative")
    # at x=δ the gap is 0
    z = Q_minus_invsq(DELTA, Fraction(1), Fraction(2))
    print(f"at x=δ, t=1,u=2: gap={z} (want 0)")
    if z != 0:
        hit(f"gap at x=δ is {z} != 0")

    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: quartic-envelope falsifier FIRED: " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: quartic-envelope falsifier did not fire: Q_{t,u}(x)-x^{-2}="
        "P(Ax+B)/x^2 identically, nonnegative for x≥1/4 on the 15-pair schedule "
        "and on extra (t,u) including 1/2,3,5,32,64 with x up to 10^4"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
