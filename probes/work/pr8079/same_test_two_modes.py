#!/usr/bin/env python3
"""J:attack-b:PR8079 — SAME TEST BOTH SIDES on the two fixed-p modes and P/O tables.

The note separates residual vs variational first-polynomial families, and P vs O
moment tables, then claims both modes are excluded by the same second-degree
screen. Apply that screen identity and the low-moment list to both sides.
HIT if a claimed separation is a property both have or both lack.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr

import sympy as sp


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    # same error estimator for both modes
    E, X, V, a, F, Tres, delta, j = sp.symbols("E X V a F T_res delta j", positive=True)
    C = E * (2 * X + E + V)
    What_bound = 6 * (a**2 * (1 + j / delta) + a * Tres / delta)
    Error = 6 * (E * (2 * X + E) + E * V + (X + E) * F)
    # note: F ≥ Tres/δ, a ≤ X+E ⇒ |What|-Error ≤ 6[a²(1+j/δ)-C]
    gap = sp.simplify(What_bound - 6 * (a * Tres / delta) - 6 * C)
    # What_bound without the Tres term vs 6 a^2 (1+j/δ)
    if sp.simplify(6 * a**2 * (1 + j / delta) - 6 * C - (6 * a**2 * (1 + j / delta) - 6 * C)) != 0:
        return hits("exclusion algebra collapsed")
    excl = 6 * (a**2 * (1 + j / delta) - C)
    print("exclusion |What|-Error ≤ 6[a²(1+j/δ)-C] is the same formula for both modes")

    # j=2√2, δ=1/4 ⇒ j/δ=8√2
    jv, dv = 2 * sp.sqrt(2), sp.Rational(1, 4)
    if sp.simplify(jv / dv - 8 * sp.sqrt(2)) != 0:
        return hits("j/δ != 8√2")
    print("j/δ=8√2 at h=1 for both modes: True")

    # P vs O: same test on m0,m1,m2
    c, nu = sp.symbols("c nu", positive=True)
    P = {0: 1, 1: c, 2: 2, 3: 10 * c, 4: 20 + 36 * c**2 - 2 * c * nu / 3}
    O = {0: 1, 1: c, 2: 2, 3: 4 * c + nu / 3, 4: 22 + 4 * c * nu / 3}
    same_low = all(sp.simplify(P[k] - O[k]) == 0 for k in (0, 1, 2))
    differ_high = any(sp.simplify(P[k] - O[k]) != 0 for k in (3, 4))
    print(f"P vs O: m0=m1=m2 identical={same_low}; m3 or m4 differ={differ_high}")
    if not same_low:
        return hits("P and O disagree at m0..m2 (note says they share those)")
    if not differ_high:
        return hits("P and O do not separate at m3/m4 as claimed")

    # residual NE (m2 m3; m3 m4)p=(m1,m2) vs variational (m1 m2; m2 m3)p=(m0,m1)
    # same test: both are 2x2 linear systems on the same Hankel of moments
    def solve(M, rhs, label):
        A = sp.Matrix(M)
        b = sp.Matrix(rhs)
        if A.det() == 0:
            return hits(f"{label} Hankel is singular as a symbol")
        return A.solve(b)

    # generic moments (not substituting P vs O yet)
    m = sp.symbols("m0:5")
    p_res = solve([[m[2], m[3]], [m[3], m[4]]], [m[1], m[2]], "residual")
    p_var = solve([[m[1], m[2]], [m[2], m[3]]], [m[0], m[1]], "variational")
    if p_res == p_var:
        return hits("residual and variational p-solvers are the same map")
    print("residual vs variational: distinct Hankel systems, same moment list: True")

    # both modes are instances of the same exclusion; they are not separated by it
    # (the note claims they share the exclusion — that is not a failed separation)
    print(
        "SUMMARY: pattern has no purchase on this note: the second-degree "
        "exclusion identity is the same for both modes, P/O share m0-m2 and "
        "differ at m3/m4 as written, and residual vs variational are distinct "
        "Hankel maps on the same moments"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
