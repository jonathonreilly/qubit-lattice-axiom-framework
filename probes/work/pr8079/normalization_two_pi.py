#!/usr/bin/env python3
"""J:attack-f:PR8079 — NORMALIZATION.

Recompute the note's 2/π in ω5=(2/π)∫Q5, the Haar 1/2 in E[cos²],
M1=6 and M2=42 on a small torus grid, and ∫(42-6t²+t⁴)dt = 42ε-2ε³+ε⁵/5.
HIT if a factor of 2, 1/2, or 2/π is off.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

import sympy as sp

HITS = []


def torus_moments(cvals):
    acc1 = 0
    acc2 = 0
    n = len(cvals)
    N = n**3
    for i, j, k in product(range(n), repeat=3):
        x = 6 - 2 * (cvals[i] + cvals[j] + cvals[k])
        acc1 += x
        acc2 += x * x
    return acc1 / N, acc2 / N, sum(c * c for c in cvals) / n


def main():
    s2 = sp.sqrt(2)
    grids = {
        4: [Fraction(1), Fraction(0), Fraction(-1), Fraction(0)],
        8: [1, s2 / 2, 0, -s2 / 2, -1, -s2 / 2, 0, s2 / 2],
    }
    for n, cvals in grids.items():
        m1, m2, ecos2 = torus_moments(cvals)
        m1, m2, ecos2 = sp.simplify(m1), sp.simplify(m2), sp.simplify(ecos2)
        print(f"T_{n}^3 Haar: EX={m1} EX^2={m2} E cos^2={ecos2}")
        if sp.simplify(m1 - 6) != 0:
            HITS.append(f"n={n} EX={m1} != 6")
        if sp.simplify(m2 - 42) != 0:
            HITS.append(f"n={n} EX^2={m2} != 42")
        if sp.simplify(ecos2 - sp.Rational(1, 2)) != 0:
            HITS.append(f"n={n} E cos^2={ecos2} != 1/2")

    t, a = sp.symbols("t a", positive=True)
    for aval in (1, 4, 9):
        integ = sp.integrate(aval**3 / (aval + t**2), (t, 0, sp.oo))
        lhs = sp.simplify((2 / sp.pi) * integ)
        rhs = sp.Integer(aval) ** sp.Rational(5, 2)
        print(f"(2/π)∫ a^3/(a+t^2) dt at a={aval}: {lhs} vs a^{{5/2}}={rhs}")
        if sp.simplify(lhs - rhs) != 0:
            HITS.append(f"2/π integral fails at a={aval}: {lhs} vs {rhs}")
    # a wrong factor 1/π would miss by 2
    wrong = sp.simplify((1 / sp.pi) * sp.integrate(1 / (1 + t**2), (t, 0, sp.oo)))
    print(f"control: (1/π)∫dt/(1+t^2)={wrong} (would be 1/2, not 1)")
    if sp.simplify(wrong - sp.Rational(1, 2)) != 0:
        HITS.append("control 1/π integral")

    eps = sp.symbols("eps", positive=True)
    L = sp.integrate(42 - 6 * t**2 + t**4, (t, 0, eps))
    stated = 42 * eps - 2 * eps**3 + eps**5 / 5
    print(f"low-piece ∫_0^ε (42-6t^2+t^4)dt = {sp.expand(L)}")
    if sp.expand(L - stated) != 0:
        HITS.append(f"low-piece {L} != {stated}")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - Haar E[cos^2]=1/2 and "
        "(EX,EX^2)=(6,42) on T_4^3 and T_8^3; ω5's 2/π reproduces a^{5/2} at "
        "a=1,4,9; low-piece integral is 42ε-2ε^3+ε^5/5"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
