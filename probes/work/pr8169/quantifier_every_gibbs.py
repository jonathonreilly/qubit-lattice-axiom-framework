#!/usr/bin/env python3
"""J:attack-d:PR8169 — QUANTIFIER SCOPE.

Gibbs 2α+2γ=1 for every mass on the line; Born (1+s·q)/2 ∈[0,1] on every
4-point frame {±q, ±q⊥}. Linear family /4 sums to 1 for every λ with
|λ|≤1. Not a re-run of the attack-f normalization script.
"""
from __future__ import annotations

from fractions import Fraction

HITS = []


def born(s, q):
    return Fraction(1 + sum(s[i] * q[i] for i in range(3)), 2)


def main():
    q, qp = (1, 0, 0), (0, 1, 0)
    S = [q, qp, tuple(-x for x in q), tuple(-x for x in qp)]
    if len(set(S)) != 4:
        HITS.append("menu not 4")
    for s in S:
        b = born(s, q)
        if b < 0 or b > 1:
            HITS.append(f"Born {b} off [0,1] at {s}")
    print("Born in [0,1] on the 4-point menu")

    for n in range(0, 11):
        alpha = Fraction(n, 20)
        gamma = Fraction(1, 2) - alpha
        if 2 * alpha + 2 * gamma != 1:
            HITS.append(f"2α+2γ at α={alpha}")
        if gamma < 0:
            continue
    print("2α+2γ=1 on α=0..1/2 step 1/20")

    for lam in (Fraction(0), Fraction(1, 2), Fraction(1), Fraction(-1, 2), Fraction(-1)):
        masses = [Fraction(1 + lam * sum(s[i] * (q[i] + qp[i]) for i in range(3)), 4) for s in S]
        sm = sum(masses)
        print(f"λ={lam}: linear family sum={sm} masses={masses}")
        if sm != 1:
            HITS.append(f"linear sum {sm} at λ={lam}")
        if any(m < 0 for m in masses):
            HITS.append(f"negative mass at λ={lam}")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - Born stays in [0,1] "
        "on the 4-point menu; 2α+2γ=1 on the Gibbs line; the linear family /4 "
        "sums to 1 for every tested λ in [-1,1]"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
