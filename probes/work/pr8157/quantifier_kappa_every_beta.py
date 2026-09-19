#!/usr/bin/env python3
"""J:attack-d:PR8157 — QUANTIFIER SCOPE.

P3 claims, for every β>0, the exponent
  γ − 16 β γ² cosh γ  ≥  κ(β)
with γ=min(1, 5/(256β)) and cosh 1 ≤ 8/5, so
  γ − 16 β γ² (8/5)  =  κ(β)
identically on each branch. Also Σ_{j=1}^R 8j/(1+j)² ≤ 8 H_R for every R≥1
(P2 shell/harmonic bound). HIT if either identity fails at a value in range.
"""
from __future__ import annotations

from fractions import Fraction

JOIN = Fraction(5, 256)
HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def kappa(beta: Fraction) -> Fraction:
    if beta >= JOIN:
        return Fraction(5, 512) / beta
    return 1 - Fraction(128, 5) * beta


def gamma(beta: Fraction) -> Fraction:
    return min(Fraction(1), Fraction(5, 256) / beta)


def exp_lb(beta: Fraction) -> Fraction:
    g = gamma(beta)
    return g - 16 * beta * g * g * Fraction(8, 5)


def main() -> int:
    print("== exponent identity γ-16βγ²(8/5) = κ(β) on both branches ==")
    # algebraic: β ≥ 5/256, γ=5/(256β)
    b = Fraction(5, 256)  # dummy; identity in b
    # check the closed form
    # γ = 5/(256 β); 16 β γ² (8/5) = 5/(512 β); γ - that = 5/(512 β)
    from sympy import Integer, Rational, simplify, symbols

    beta = symbols("beta", positive=True)
    g = Rational(5, 256) / beta
    lhs = simplify(g - 16 * beta * g ** 2 * Rational(8, 5))
    rhs = Rational(5, 512) / beta
    print(f"  large-β branch: {lhs} vs {rhs} equal={simplify(lhs - rhs)==0}")
    if simplify(lhs - rhs) != 0:
        hit(f"large-β exponent identity failed: {lhs} != {rhs}")
    g1 = Integer(1)
    lhs1 = simplify(g1 - 16 * beta * g1 ** 2 * Rational(8, 5))
    rhs1 = 1 - Rational(128, 5) * beta
    print(f"  small-β branch: {lhs1} vs {rhs1} equal={simplify(lhs1 - rhs1)==0}")
    if simplify(lhs1 - rhs1) != 0:
        hit(f"small-β exponent identity failed: {lhs1} != {rhs1}")
    # numeric Fraction grid
    grid = (
        [JOIN / n for n in (8, 4, 2, 1)]
        + [JOIN * n for n in (1, 2, 4, 8, 16)]
        + [Fraction(1, n) for n in (1, 2, 5, 10, 20, 100, 1000)]
        + [Fraction(n, 256) for n in range(1, 30)]
    )
    for b in grid:
        if b <= 0:
            continue
        a, k = exp_lb(b), kappa(b)
        ok = a == k
        if not ok:
            hit(f"β={b}: exp_lb={a} != κ={k}")
            break
    else:
        print(f"  Fraction grid ({len(grid)} points): exp_lb = κ")

    print("== P2 Σ_j 8j/(1+j)² ≤ 8 H_R for every R=1..80 ==")
    H = Fraction(0)
    S = Fraction(0)
    worst = None
    for R in range(1, 81):
        H += Fraction(1, R)
        S += 8 * Fraction(R, (1 + R) ** 2)
        slack = 8 * H - S
        if slack < 0:
            hit(f"R={R}: Σ 8j/(1+j)²={S} > 8 H_R={8*H}")
            break
        if worst is None or slack < worst[0]:
            worst = (slack, R)
    else:
        print(f"  R=1..80 holds; tightest slack {worst[0]} at R={worst[1]}")

    # κ≥1/2 on the small branch, including the join
    if kappa(JOIN) != Fraction(1, 2):
        hit(f"κ(5/256)={kappa(JOIN)} != 1/2")
    if kappa(JOIN / 2) < Fraction(1, 2):
        hit(f"κ(join/2)={kappa(JOIN/2)} < 1/2")
    print(f"  κ(join)={kappa(JOIN)} κ(join/2)={kappa(JOIN/2)} ≥ 1/2")

    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: QUANTIFIER SCOPE (PR #8157): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: QUANTIFIER SCOPE (PR #8157): γ−16βγ²(8/5)=κ(β) identically "
        "on both branches (every β>0); Σ_{j=1}^R 8j/(1+j)² ≤ 8 H_R for R=1..80; "
        "κ(5/256)=1/2; pattern has purchase and the inequalities hold in-range"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
