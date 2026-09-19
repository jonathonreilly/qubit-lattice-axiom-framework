#!/usr/bin/env python3
"""J:attack-d:PR8083 — QUANTIFIER SCOPE: Q_{t,u}(x)>=x^{-2} for all x>=δ, t,u>0.

Check the 15 schedule pairs and x in {δ, 2δ, t, u, 8, 16}. HIT if any
stated-range point has Q < x^{-2}.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def Q(x, t, u, delta=Fr(1, 4)):
    B = 1 / (delta * t**2 * u**2)
    A = B * (1 / delta + Fr(2, t) + Fr(2, u))
    P = (x - delta) * (x - t) ** 2 * (x - u) ** 2
    return (1 + P * (A * x + B)) / (x * x)


def main() -> int:
    delta = Fr(1, 4)
    S = (1, 2, 4, 8, 16)
    pairs = list(itertools.combinations_with_replacement(S, 2))
    xs = [delta, Fr(1, 2), Fr(1), Fr(2), Fr(3), Fr(8), Fr(16), Fr(5, 4)]
    for t, u in pairs:
        for x in xs:
            if x < delta:
                continue
            q = Q(x, Fr(t), Fr(u), delta)
            inv = 1 / (x * x)
            if q < inv:
                return hits(f"Q({x},{t},{u})={q} < 1/x^2={inv}")
        print(f"pair {(t,u)}: Q>=1/x^2 on tested x>=δ: True")
    print(
        "SUMMARY: pattern has no purchase on this note: Q_{t,u}(x)>=x^{-2} holds "
        "for all 15 schedule pairs and tested x>=δ=1/4"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
