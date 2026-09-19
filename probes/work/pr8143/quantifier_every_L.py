#!/usr/bin/env python3
"""J:attack-d:PR8143 — QUANTIFIER SCOPE.

The note claims |C|=1+5L and sequence length 3L for every L, Z=S+(S-1)^2≥3/4
for every S, and λ=a/[a+(a-1)^2]∈[0,1] for every a≥0. The geometry census
was executed at L=5. Check L=1..20 and a rational S,a grid.
"""
from __future__ import annotations

from fractions import Fraction

HITS = []


def seed(L):
    T = [(x, 0, 0) for x in range(3 * L)]
    a0 = (-1, 0, 0)
    pj = [(3 * j, -1, 0) for j in range(L)]
    kj = [(3 * j + 2, 1, 0) for j in range(L)]
    C = T + [a0] + pj + kj
    seq = []
    for j in range(L):
        seq.extend([(3 * j, 0, 0), (3 * j + 1, 0, 0), (3 * j + 2, 0, 0)])
    return C, seq


def Z(S):
    return S + (S - 1) ** 2


def lam(a):
    return a / (a + (a - 1) ** 2)


def main():
    for L in range(1, 21):
        C, seq = seed(L)
        if len(C) != 1 + 5 * L:
            HITS.append(f"|C|={len(C)} != 1+5L at L={L}")
        if len(set(C)) != len(C):
            HITS.append(f"duplicate C at L={L}")
        if len(seq) != 3 * L:
            HITS.append(f"|seq|={len(seq)} != 3L at L={L}")
        if len(set(seq)) != 3 * L:
            HITS.append(f"seq not 3L distinct at L={L}")
    print("L=1..20: |C|=1+5L and |seq|=3L distinct")

    samples = [Fraction(n, 8) for n in range(0, 33)]
    for s in samples:
        z = Z(s)
        if z < Fraction(3, 4):
            HITS.append(f"Z({s})={z}<3/4")
    print("Z>=3/4 on S=0..4 step 1/8")
    for a in samples:
        if a < 0:
            continue
        den = a + (a - 1) ** 2
        if den <= 0:
            HITS.append(f"λ denom {den} at a={a}")
            continue
        lv = lam(a)
        if lv < 0 or lv > 1:
            HITS.append(f"λ({a})={lv} not in [0,1]")
    print("λ in [0,1] on a=0..4 step 1/8")

    if HITS:
        print("HIT: " + "; ".join(HITS[:6]))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS[:4]))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - |C|=1+5L and the 3L "
        "sequence hold for every L=1..20; Z≥3/4 and λ∈[0,1] hold on the "
        "tested nonnegative grid (beyond the executed L=5 census)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
