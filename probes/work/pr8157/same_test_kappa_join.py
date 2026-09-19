#!/usr/bin/env python3
"""J:attack-b:PR8157 — same kappa test on both sides of beta=5/256.

kappa(beta)=5/(512 beta) for beta>=5/256, 1-128 beta/5 for beta<=5/256.
HIT if the two formulas disagree at the join, or if shells 8j fail on Z^2
while holding on the torus (or conversely) for j < L.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product


def kappa_hi(b):
    return Fraction(5, 512) / b


def kappa_lo(b):
    return 1 - Fraction(128, 5) * b


def dinf_t(y, side):
    def wrap(a):
        a %= side
        return min(a, side - a)

    return max(wrap(y[0]), wrap(y[1]))


def main():
    hits = []
    b0 = Fraction(5, 256)
    hi, lo = kappa_hi(b0), kappa_lo(b0)
    print(f"join beta=5/256: hi={hi} lo={lo}")
    if hi != lo:
        hits.append(f"HIT: kappa formulas disagree at 5/256: {hi} vs {lo}")
        print(hits[-1])
    if hi != Fraction(1, 2):
        hits.append(f"HIT: join value {hi} != 1/2")
        print(hits[-1])

    # shells j=1,2 on Z^2 vs torus 2L=8 (L=4), j<L
    z2 = {}
    for y in product(range(-5, 6), repeat=2):
        j = max(abs(y[0]), abs(y[1]))
        z2[j] = z2.get(j, 0) + 1
    side = 8
    L = 4
    tor = {}
    for y in product(range(side), repeat=2):
        j = dinf_t(y, side)
        tor[j] = tor.get(j, 0) + 1
    for j in (1, 2, 3):
        print(f"shell j={j}: Z^2={z2.get(j)} torus={tor.get(j)} want {8*j}")
        if z2.get(j) != 8 * j:
            hits.append(f"HIT: Z^2 shell j={j} is {z2.get(j)}")
            print(hits[-1])
        if tor.get(j) != 8 * j:
            hits.append(f"HIT: torus shell j={j} is {tor.get(j)}")
            print(hits[-1])
        if z2.get(j) != tor.get(j):
            hits.append(f"HIT: Z^2 vs torus shell j={j} disagree under the same 8j test")
            print(hits[-1])
    if hits:
        print("SUMMARY: kappa join or shell 8j same-test fails")
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note — kappa hi/lo formulas join "
        "at 1/2 at beta=5/256, and the same 8j shell test holds on Z^2 and on the "
        "even-side torus for j<L"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
