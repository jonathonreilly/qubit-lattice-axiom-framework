#!/usr/bin/env python3
"""J:attack-b:PR8172 — SAME TEST BOTH SIDES on T1's 3c uniqueness threshold.

Not the known 4.05 vs 6671/1728 island-ratio HIT.
Block 08: c(p)=max TV(K(·|a,b,c), K(·|a',b,c)) over triples and a'≠a;
uniqueness iff 3c<1. Note: 3c(37/10)=406962630/413162167<1 and
3c(19/5)=871815/862244>1. Apply the identical TV-max to both p.
HIT if both sides pass or both fail 3c<1, or the stated fractions disagree
with the enumerated TV.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr


AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def phi(u, v, p):
    if u == v:
        return p
    if u[0] == -v[0] and u[1] == -v[1] and u[2] == -v[2]:
        return Fr(1)
    return Fr(2)


def kernel(pred, p):
    w = [phi(v, pred[0], p) * phi(v, pred[1], p) * phi(v, pred[2], p) for v in AXES]
    Z = sum(w)
    return [x / Z for x in w]


def tv(k, k2):
    return sum(abs(a - b) for a, b in zip(k, k2)) / 2


def c_of(p):
    m = Fr(0)
    for pred in itertools.product(AXES, repeat=3):
        k = kernel(pred, p)
        for a2 in AXES:
            if a2 == pred[0]:
                continue
            k2 = kernel((a2, pred[1], pred[2]), p)
            t = tv(k, k2)
            if t > m:
                m = t
    return m


def main() -> int:
    p_lo, p_hi = Fr(37, 10), Fr(19, 5)
    c_lo, c_hi = c_of(p_lo), c_of(p_hi)
    three_lo, three_hi = 3 * c_lo, 3 * c_hi
    print(f"3c(37/10)={three_lo} stated 406962630/413162167")
    print(f"3c(19/5)={three_hi} stated 871815/862244")
    stated_lo = Fr(406962630, 413162167)
    stated_hi = Fr(871815, 862244)
    if three_lo != stated_lo:
        return hits(f"enumerated 3c(37/10)={three_lo} != stated {stated_lo}")
    if three_hi != stated_hi:
        return hits(f"enumerated 3c(19/5)={three_hi} != stated {stated_hi}")
    lo_ok = three_lo < 1
    hi_ok = three_hi > 1
    print(f"same test 3c<1: p=37/10 -> {lo_ok}; p=19/5 -> {not (three_hi < 1)} (3c>1 is {hi_ok})")
    if lo_ok == (three_hi < 1):
        return hits("3c<1 does not separate 37/10 from 19/5")
    if not (lo_ok and hi_ok):
        return hits("stated sides of the uniqueness threshold fail the TV test")

    print(
        "SUMMARY: pattern has no purchase on this note: the same TV-max test "
        "gives 3c(37/10)=406962630/413162167<1 and 3c(19/5)=871815/862244>1, "
        "so the uniqueness criterion separates those two couplings as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
