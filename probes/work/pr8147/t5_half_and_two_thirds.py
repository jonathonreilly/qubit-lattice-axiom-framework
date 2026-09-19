#!/usr/bin/env python3
"""J:attack-f:PR8147 — NORMALIZATION of T5 1/2 and 2/3.

Do not re-find the known T3(ii) u^2 vs 4 sin²(u/2) HIT.

T5: zonal log-prod expansion has κ=f'(1)/(2 f(1)); per-component variance
f(1)/(3 f'(1)), equal to 2/3 for Born f(t)=(1+t)/2; block 07 formation has
g=1/2. Also T1: at g=1 (w=1/3) the directed kernel G sums to 1 on each
level (probability kernel). Exact Fraction/sympy.
"""
from __future__ import annotations

from fractions import Fraction
from math import factorial

import sympy as sp

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def main() -> int:
    t = sp.symbols("t")
    f = (1 + t) / 2
    fp = sp.diff(f, t)
    kap = sp.simplify(fp.subs(t, 1) / (2 * f.subs(t, 1)))
    var = sp.simplify(f.subs(t, 1) / (3 * fp.subs(t, 1)))
    print(f"Born f=(1+t)/2: κ=f'(1)/(2f(1))={kap}  var=f(1)/(3f'(1))={var}")
    if var != sp.Rational(2, 3):
        hit(f"Born variance {var} != 2/3")
    if kap != sp.Rational(1, 4):
        # the note states the formula, not the value 1/4; still record
        print(f"  κ={kap} (formula as written)")
    # without the 2 in κ: f'/f = 1/2, a common swap
    kap_wrong = sp.simplify(fp.subs(t, 1) / f.subs(t, 1))
    print(f"  without the 1/2 in κ one would get {kap_wrong}")

    # g = 3w; massless formation is g=1 so w=1/3; static Laplacian formation g=1/2 so w=1/6
    w_massless = Fraction(1, 3)
    w_static = Fraction(1, 6)
    print(f"g=3w: massless w={w_massless} g={3*w_massless}; static-Laplacian w={w_static} g={3*w_static}")
    if 3 * w_static != Fraction(1, 2):
        hit(f"3*(1/6) != 1/2")

    # T1 probability kernel at g=1: sum_{d1+d2+d3=n} n!/(d1!d2!d3!) / 3^n = 1
    print("== T1 G sums to 1 at w=1/3, n=1..8 ==")
    for n in range(0, 9):
        s = Fraction(0)
        for d1 in range(n + 1):
            for d2 in range(n - d1 + 1):
                d3 = n - d1 - d2
                s += Fraction(factorial(n), factorial(d1) * factorial(d2) * factorial(d3) * 3 ** n)
        print(f"  n={n} sum G={s}")
        if s != 1:
            hit(f"n={n} directed-kernel sum {s} != 1 (g=1 normalization)")

    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: NORMALIZATION (PR #8147): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: NORMALIZATION (PR #8147): T5 Born variance f(1)/(3f'(1))=2/3 "
        "and κ=f'(1)/(2f(1))=1/4; g=3w gives g=1/2 at w=1/6; T1 directed kernel "
        "sums to 1 at w=1/3 for n=0..8; pattern has purchase (known T3(ii) "
        "u^2 vs 4sin²(u/2) not re-claimed)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
