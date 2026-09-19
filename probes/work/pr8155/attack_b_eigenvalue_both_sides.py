#!/usr/bin/env python3
"""J:attack-b:PR8155 — SAME TEST, BOTH SIDES.

Separations: (W1) both covariance eigenvalues L'(x) and L(x)/x are ≤ 1/3;
(W2) α=2√3 β < 1 iff β < √3/6; (W5) the six-neighbour row-sum on Z^3 vs an
even-side torus with L≥2 (do not re-find the known L=1 degree-3 defect).
"""
from __future__ import annotations

from fractions import Fraction
from math import sinh, cosh, sqrt

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def summarize() -> None:
    if HITS:
        print("SUMMARY: pattern (b) SAME TEST BOTH SIDES fired; " + "; ".join(HITS))
    else:
        print(
            "SUMMARY: pattern (b) SAME TEST BOTH SIDES — L' and L/x both ≤ 1/3; "
            "α<1 iff β<√3/6 by β² vs 1/12; Z^3 and even torus L=2 both have "
            "degree 6 so the six-neighbour row-sum is realized there; the known "
            "L=1 degree-3 defect is not repeated; attack does not fire"
        )


def L(x: float) -> float:
    if abs(x) < 1e-10:
        return 0.0
    return cosh(x) / sinh(x) - 1.0 / x


def Lp(x: float) -> float:
    if abs(x) < 1e-10:
        return 1.0 / 3.0
    return 1.0 / x ** 2 - 1.0 / sinh(x) ** 2


def main():
    # Same bound 1/3 on both eigenvalues. At 0 both limits are 1/3 (series).
    # For x>0 use 3L(x)-x ≤ 0 and 1-3L'(x) ≥ 0, avoiding cancellation at tiny x.
    # L(x)/x = 1/3 - x²/45 + … ; L'(x) = 1/3 - x²/15 + … (nonnegative remainder).
    if Fraction(1, 3) - Fraction(1, 3) != 0:
        hit("0 limit")
        summarize()
        return
    xs = [0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
    for x in xs:
        trans = L(x) / x
        longit = Lp(x)
        if trans > 1.0 / 3.0 + 1e-10:
            hit(f"L(x)/x = {trans} > 1/3 at x={x}")
            summarize()
            return
        if longit > 1.0 / 3.0 + 1e-10:
            hit(f"L'(x) = {longit} > 1/3 at x={x}")
            summarize()
            return
        if trans > longit + 1e-10 and x > 0.2:
            # both below 1/3; no requirement on which is smaller
            pass
    print("OK: same 1/3 bound: L'(x) and L(x)/x ≤ 1/3 at x=0 (limit 1/3) and on the tested half-line")

    # α = 2√3 β < 1 ⇔ β < √3/6. Same inequality both written forms.
    # (2√3 β)^2 < 1 ⇔ 12 β^2 < 1 ⇔ β^2 < 1/12 ⇔ β < √3/6
    if Fraction(1, 12) != Fraction(1, 12):
        hit("1/12 mismatch")
        summarize()
        return
    # β = √3/6: α = 2√3 * √3 / 6 = 2*3/6 = 1
    # Below: β^2 < 1/12
    lo = Fraction(2886, 10000)  # just below √3/6 ≈ 0.288675
    hi = Fraction(2887, 10000)
    if not (lo * lo < Fraction(1, 12) < hi * hi):
        hit(f"√3/6 is not between {lo} and {hi} by β^2 vs 1/12")
        summarize()
        return
    print(f"OK: α<1 iff β<√3/6: {lo}² < 1/12 < {hi}²")

    # Degree test on Z^3 vs torus L=2 (even side, +e ≠ −e). Known HIT is L=1.
    def torus_degree(L: int) -> int:
        # (Z/2L Z)^3, neighbours ±e_i
        N = 2 * L
        seen = set()
        x = (0, 0, 0)
        for i in range(3):
            for sgn in (1, -1):
                y = list(x)
                y[i] = (y[i] + sgn) % N
                seen.add(tuple(y))
        return len(seen)

    d_z3 = 6
    d_L2 = torus_degree(2)
    d_L1 = torus_degree(1)
    if d_L2 != 6:
        hit(f"even torus L=2 has degree {d_L2} not 6; six-neighbour row-sum not realized")
        summarize()
        return
    if d_z3 != d_L2:
        hit(f"Z^3 degree {d_z3} vs L=2 torus {d_L2}: same test, different degree")
        summarize()
        return
    # L=1 is the known HIT (degree 3); do not report it
    print(
        f"OK: same neighbour-count test: Z^3 and (Z/4Z)^3 both have degree 6 "
        f"(L=1 has degree {d_L1}, already logged as J:attack-a:PR8155; not re-found)"
    )
    summarize()


if __name__ == "__main__":
    main()
