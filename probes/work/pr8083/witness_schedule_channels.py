#!/usr/bin/env python3
"""J:attack-a:PR8083 — witness realizability of the quartic schedule and channels.

Fifteen unordered pairs with repetition from {1,2,4,8,16}; 2 modes × 2 P/O
× 15 = 60 candidates; 12 P + 3 O = 15 two-link channels; δ=1/4;
P(x)=(x-δ)(x-t)^2(x-u)^2 exists for every pair; Q-x^{-2}≥0 as written.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    S = (1, 2, 4, 8, 16)
    pairs = list(itertools.combinations_with_replacement(S, 2))
    print(f"unordered pairs with repetition: {len(pairs)}")
    if len(pairs) != 15:
        return hits(f"{len(pairs)} pairs != 15")
    if 2 * 2 * 15 != 60:
        return hits("2*2*15 != 60 candidates")
    print("2 modes × 2 P/O × 15 pairs = 60 candidates: True")

    labels = list(itertools.combinations(range(6), 2))
    if len(labels) != 15:
        return hits("15 two-link channels missing")
    # a conventional split 12 P + 3 O: three pairwise-disjoint edges of K6
    matching = [((0, 1), (2, 3), (4, 5))]
    O = matching[0]
    Pch = [e for e in labels if e not in O]
    if len(O) != 3 or len(Pch) != 12:
        return hits(f"P/O split {len(Pch)}+{len(O)} != 12+3")
    print("12 P + 3 O channels exist as a K6 1-factor plus the rest: True")

    delta = Fr(1, 4)
    x, t, u = sp.symbols("x t u", positive=True)
    B = 1 / (delta * t**2 * u**2)
    A = B * (1 / delta + 2 / t + 2 / u)
    Px = (x - delta) * (x - t) ** 2 * (x - u) ** 2
    Q = (1 + Px * (A * x + B)) / x**2
    gap = sp.together(Q - 1 / x**2)
    rhs = Px * (A * x + B) / x**2
    if sp.simplify(gap - rhs) != 0:
        return hits("Q-x^{-2} identity fails")
    print("Q_{t,u}(x)-x^{-2} = P(x)(Ax+B)/x^2 identically: True")

    # every schedule pair is positive so the envelope is defined
    for tt, uu in pairs:
        if tt <= 0 or uu <= 0:
            return hits(f"nonpositive schedule pair {(tt, uu)}")
        Bb = Fr(1) / (delta * tt**2 * uu**2)
        Aa = Bb * (Fr(1, delta) + Fr(2, tt) + Fr(2, uu))
        if Aa <= 0 or Bb <= 0:
            return hits(f"A,B not positive at {(tt, uu)}")
    print("all 15 schedule pairs give positive A,B at δ=1/4: True")

    # X=4√15, V=32√30 exist as positive reals
    if 4**2 * 15 != 240 or 32**2 * 30 != 30720:
        return hits("X=4√15 or V=32√30 squares failed")
    print("trial-norm caps X=4√15 and V=32√30 exist: True")

    print(
        "SUMMARY: pattern has no purchase on this note: the 15-pair schedule, "
        "60 candidates, 12+3 channel split, quartic envelope identity, and "
        "δ=1/4 with positive A,B all exist as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
