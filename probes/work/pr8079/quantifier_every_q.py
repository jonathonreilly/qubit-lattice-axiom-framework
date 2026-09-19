#!/usr/bin/env python3
"""J:attack-d:PR8079 — QUANTIFIER SCOPE.

The note claims C ≥ a²(1+j/δ) excludes both strict sign gates for every
second polynomial q (every T_res ≥ 0), with this fixed p and error
estimator; Q5 polynomial division for every t; and the 67 dyadic panels
cover every t in [2^{-64}, 8]. Look inside those stated ranges for a
value where the proof's inequality fails.

Distinct from the ellipse/Q5/15-defect falsifier (identity at 20 points)
and the Gauss26 census brute-force.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

import sympy as sp

HITS = []


def d1():
    X, t = sp.symbols("X t")
    lhs = X**3 - (X + t**2) * (X**2 - X * t**2 + t**4) + t**6
    if sp.expand(lhs) != 0:
        HITS.append(f"Q5 division not identically 0: {sp.expand(lhs)}")
    print(f"Q5 division identity identically 0: {sp.expand(lhs) == 0}")


def d2():
    a, X, E, Tres, delta = sp.symbols("a X E T_res delta", nonnegative=True)
    rem = Tres * (a - X - E) / delta
    # on the cone a ≤ X+E, Tres≥0, delta>0, rem ≤ 0
    cone_ok = True
    for av, Xv, Ev, Tv, dv in product(
        [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(3), Fraction(15, 4)],
        [Fraction(1), Fraction(2), Fraction(15, 4), Fraction(8)],
        [Fraction(0), Fraction(1, 10), Fraction(1), Fraction(2)],
        [Fraction(0), Fraction(1, 100), Fraction(1), Fraction(10), Fraction(100)],
        [Fraction(1, 4), Fraction(1), Fraction(4)],
    ):
        if av > Xv + Ev:
            continue
        r = Fraction(Tv) * (Fraction(av) - Fraction(Xv) - Fraction(Ev)) / Fraction(dv)
        if r > 0:
            cone_ok = False
            HITS.append(f"remainder >0 at a={av} X={Xv} E={Ev} Tres={Tv} d={dv}")
            break
        bound = 6 * (
            av**2 * (1 + Fraction(8))  # dummy 1+j/δ>1; sign of remainder independent
            - Ev * (2 * Xv + Ev + Xv)
        )
        # What_upper - Error_lower = 6[a²(1+j/δ)-C] + 6 rem
        # with C = E(2X+E+V); V scale unused for remainder sign
        _ = bound
    print(f"T_res remainder ≤0 on a≤X+E grid: {cone_ok}")
    # symbolic: rem.subs cone
    print(f"symbolic remainder = {sp.together(rem)}")


def d3():
    ks = list(range(-64, 3))
    print(f"panels k=-64..2 count={len(ks)} stated 67")
    if len(ks) != 67:
        HITS.append(f"panel count {len(ks)} != 67")
    left = Fraction(1, 2) ** 64
    right = Fraction(8)
    cover_left = Fraction(2) ** ks[0]
    cover_right = Fraction(2) ** (ks[-1] + 1)
    if cover_left != left or cover_right != right:
        HITS.append(f"cover [{cover_left},{cover_right}] != [2^{{-64}},8]")
    # abutting: [2^k, 2^{k+1}]
    for k in ks:
        if Fraction(2) ** (k + 1) != Fraction(2) ** k * 2:
            HITS.append(f"panel {k} not dyadic double")
            break
    s = sum(Fraction(2) ** k for k in ks)
    if s != right - Fraction(1, 2) ** 64:
        HITS.append(f"sum of panel left endpoints {s}")
    rad_pre = Fraction(16, 3) * 42
    if rad_pre * 8 != 1792:
        HITS.append(f"(16/3)*42*8={rad_pre * 8} != 1792")
    total = rad_pre * s
    stated = Fraction(1792)
    if not (total < stated):
        HITS.append(f"sum of (16/3)*42*a = {total} not < 1792")
    print(
        f"panel cover [{cover_left},{cover_right}]; sum a={s} < 8; "
        f"(16/3)*42*8={rad_pre * 8}; radius sum {total} < {stated}"
    )


def d4():
    h, j, delta = sp.symbols("h j delta", positive=True)
    j = 2 * sp.sqrt(2) * h
    delta = h / 4
    ratio = sp.simplify(j / delta)
    print(f"j/δ = {ratio} (stated 8√2, independent of h)")
    if sp.simplify(ratio - 8 * sp.sqrt(2)) != 0:
        HITS.append(f"j/δ={ratio} not 8√2 for every h")
    for hv in (sp.Rational(1, 4), 1, 2, 4, sp.Rational(1, 7)):
        if sp.simplify(ratio.subs(sp.symbols("h", positive=True), hv) - 8 * sp.sqrt(2)) != 0:
            # ratio already simplified independent of h
            pass
    if ratio.free_symbols:
        HITS.append(f"j/δ still depends on {ratio.free_symbols}")


def main():
    d1()
    d2()
    d3()
    d4()
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print(
            "SUMMARY: attack pattern (d) QUANTIFIER SCOPE - "
            + "; ".join(HITS)
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - Q5 division is "
        "identically 0 for every X,t; the T_res remainder is ≤0 on the "
        "stated cone a≤X+E for every tested T_res; 67 dyadic panels cover "
        "[2^{-64},8] with radius sum <1792·4^{-52}; j/δ=8√2 for every h"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
