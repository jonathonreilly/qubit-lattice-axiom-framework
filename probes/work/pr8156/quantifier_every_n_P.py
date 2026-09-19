#!/usr/bin/env python3
"""J:attack-d:PR8156 — QUANTIFIER SCOPE.

V2 claims P_{2n}(0,0) ≤ (36/11)^{3/2}/(4 π^{3/2} n^{3/2}) + 2 e^{-4n/(3π²)}
for every n≥1 (executed symbolically; Vandermonde to n=12). Check the
closed form vs the bound for n=1..20, and 1-cos u ≥ 11u²/24 on |u|≤1.
Not the N=1000 75/100–76/100 certificate.
"""
from __future__ import annotations

from math import comb

import mpmath as mp

HITS = []
mp.mp.dps = 40


def P(n):
    s = sum(comb(n, a) ** 2 * comb(2 * (n - a), n - a) for a in range(n + 1))
    return mp.mpf(comb(2 * n, n) * s) / mp.power(6, 2 * n)


def bound(n):
    pi = mp.pi
    return (mp.mpf(36) / 11) ** mp.mpf("1.5") / (
        4 * pi ** mp.mpf("1.5") * mp.power(n, mp.mpf("1.5"))
    ) + 2 * mp.e ** (-4 * n / (3 * pi * pi))


def main():
    for n in range(1, 21):
        lhs, rhs = P(n), bound(n)
        print(f"n={n}: P={lhs} bound={rhs} ok={lhs <= rhs}")
        if lhs > rhs + mp.mpf("1e-20"):
            HITS.append(f"P_{{2n}}>{n} bound at n={n}")

    # 1-cos u ≥ 11 u²/24 on |u|≤1
    for k in range(0, 101):
        u = mp.mpf(k) / 100
        lhs = 1 - mp.cos(u)
        rhs = 11 * u * u / 24
        if lhs + mp.mpf("1e-20") < rhs:
            HITS.append(f"1-cos u < 11u^2/24 at u={u}")
            break
    print("1-cos u ≥ 11u²/24 on k/100 in [0,1]: True" if not any("11u" in h for h in HITS) else "failed")

    # 1-cos u ≥ 2u²/π² on [0,π]
    pi = mp.pi
    for k in range(0, 101):
        u = k * pi / 100
        lhs = 1 - mp.cos(u)
        rhs = 2 * u * u / (pi * pi)
        if lhs + mp.mpf("1e-20") < rhs:
            HITS.append(f"1-cos u < 2u^2/π² at u={u}")
            break
    print("1-cos u ≥ 2u²/π² on [0,π]: checked")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - V2's P_{2n} bound "
        "holds for every n=1..20 and 1-cos u ≥ 11u²/24 on |u|≤1 and ≥ 2u²/π² "
        "on [0,π] (not the N=1000 75/100–76/100 certificate)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
