#!/usr/bin/env python3
"""J:falsifier:PR8080 — Q_τ(λ) ≥ λ^{-2} for every λ≥δ>0.

Note factorization:
  Q=(3τ-2λ)/τ³ + A(λ-τ)², A=(τ+2δ)/(δ² τ³)
  Q-λ^{-2}=(λ-δ)(λ-τ)²((τ+2δ)λ+δτ)/(δ² τ³ λ²) ≥ 0 for λ≥δ.

Beyond the note: identity in symbols, plus a large Fraction grid
(δ,τ,λ) including δ=1/4 and λ up to 10^4. HIT if residual is nonzero
or a grid point is negative.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

import sympy as sp

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def Q(lam, tau, delta):
    A = (tau + 2 * delta) / (delta ** 2 * tau ** 3)
    return (3 * tau - 2 * lam) / tau ** 3 + A * (lam - tau) ** 2


def claimed_gap(lam, tau, delta):
    return (
        (lam - delta)
        * (lam - tau) ** 2
        * ((tau + 2 * delta) * lam + delta * tau)
        / (delta ** 2 * tau ** 3 * lam ** 2)
    )


def main() -> int:
    lam, tau, delta = sp.symbols("lambda tau delta", positive=True)
    A = (tau + 2 * delta) / (delta ** 2 * tau ** 3)
    Qs = (3 * tau - 2 * lam) / tau ** 3 + A * (lam - tau) ** 2
    gap = claimed_gap(lam, tau, delta)
    residual = sp.together(sp.simplify(Qs - 1 / lam ** 2 - gap))
    print(f"symbolic residual = {residual}")
    if residual != 0:
        hit(f"factorization residual {residual}")

    deltas = [Fraction(1, 4), Fraction(1, 8), Fraction(1, 2), Fraction(1), Fraction(3, 10)]
    taus = [Fraction(1, 5), Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(5), Fraction(16)]
    lams = (
        [Fraction(1, 4), Fraction(1, 3), Fraction(1, 2)]
        + [Fraction(n) for n in range(1, 21)]
        + [Fraction(50), Fraction(100), Fraction(1000), Fraction(10000)]
    )
    n = 0
    for d, t, l in product(deltas, taus, lams):
        if l < d or t <= 0 or d <= 0:
            continue
        n += 1
        val = Q(l, t, d) - 1 / (l * l)
        if val < 0:
            hit(f"Q-1/λ²={val} < 0 at λ={l} τ={t} δ={d}")
            break
        if claimed_gap(l, t, d) != val:
            hit(f"gap mismatch at λ={l} τ={t} δ={d}")
            break
    else:
        print(f"grid {n} points: Q-1/λ² ≥ 0 and matches factorization")

    if HITS:
        print("HIT: " + HITS[0])
        print("SUMMARY: Q_tau falsifier FIRED: " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: Q_tau falsifier did not fire: Q_τ(λ)-λ^{-2} matches the "
        "displayed factorization identically and is nonnegative on a "
        f"{n}-point Fraction grid with λ up to 10^4, beyond the note's checks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
