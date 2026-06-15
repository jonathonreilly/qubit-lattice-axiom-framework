#!/usr/bin/env python3
"""Bounded verifier for the stipulated-hypothesis PMNS TM2 algebra lemma."""

from __future__ import annotations

from fractions import Fraction
import math

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    PASS += int(condition)
    FAIL += int(not condition)
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def trimaximal_column_check() -> bool:
    mag = Fraction(1, 3)
    return mag + mag + mag == 1


def theta23_from_mutau_modulus(x: Fraction) -> Fraction:
    """If |U_mu3|^2 = |U_tau3|^2 = x, compute sin^2(theta_23)."""
    denom = x + x
    return x / denom


def tm2_sum_rule(s13_sq: Fraction) -> tuple[Fraction, Fraction]:
    c13_sq = 1 - s13_sq
    s12_sq = Fraction(1, 3) / c13_sq
    return 3 * s12_sq * c13_sq, s12_sq


def lhs_without_cp_phase(s13_sq: Fraction) -> Fraction:
    c13_sq = 1 - s13_sq
    s12_sq = Fraction(1, 3) / c13_sq
    c12_sq = 1 - s12_sq
    return c12_sq + s12_sq * s13_sq


def nonsingular_phase_factor_sq(s13_sq: Fraction) -> Fraction:
    """Square of c12*s12*s13 under the TM2 sum rule."""
    c13_sq = 1 - s13_sq
    s12_sq = Fraction(1, 3) / c13_sq
    c12_sq = 1 - s12_sq
    return c12_sq * s12_sq * s13_sq


def phase_equation_residual_at_degenerate_endpoint(
    s13_sq: Fraction, cos_delta: Fraction
) -> Fraction:
    """Equation (3) residual when the phase multiplier is exactly zero."""
    factor_sq = nonsingular_phase_factor_sq(s13_sq)
    if factor_sq != 0:
        raise ValueError("endpoint residual helper requires c12*s12*s13 = 0")
    phase_multiplier = Fraction(0, 1)
    return lhs_without_cp_phase(s13_sq) - phase_multiplier * cos_delta - Fraction(2, 3)


def implied_cos_delta(s13_sq: float) -> float:
    c13_sq = 1.0 - s13_sq
    s12_sq = (1.0 / 3.0) / c13_sq
    c12_sq = 1.0 - s12_sq
    s13 = math.sqrt(s13_sq)
    s12 = math.sqrt(s12_sq)
    c12 = math.sqrt(c12_sq)
    lhs_no_cos = c12_sq + s12_sq * s13_sq
    target = 2.0 / 3.0
    return (lhs_no_cos - target) / (2.0 * c12 * s12 * s13)


def main() -> int:
    print("=" * 72)
    print("PMNS TM2 RESIDUAL CONSEQUENCE -- STIPULATED-HYPOTHESIS BOUNDED ALGEBRA CHECK")
    print("=" * 72)

    check(
        "trimaximal second column is normalized",
        trimaximal_column_check(),
        "1/3 + 1/3 + 1/3 = 1",
    )

    for x in [Fraction(1, 10), Fraction(3, 10), Fraction(1, 4)]:
        check(
            f"mu-tau modulus residual gives sin^2(theta_23)=1/2 for x={x}",
            theta23_from_mutau_modulus(x) == Fraction(1, 2),
        )

    for s13_sq in [
        Fraction(0, 1),
        Fraction(1, 100),
        Fraction(223, 10000),
        Fraction(1, 20),
        Fraction(1, 10),
    ]:
        lhs, s12_sq = tm2_sum_rule(s13_sq)
        check(
            f"TM2 sum rule holds for sin^2(theta_13)={s13_sq}",
            lhs == 1,
            f"sin^2(theta_12)={s12_sq}",
        )

    for s13_sq in [Fraction(1, 100), Fraction(223, 10000), Fraction(1, 20)]:
        check(
            f"phase-independent part equals 2/3 for sin^2(theta_13)={s13_sq}",
            lhs_without_cp_phase(s13_sq) == Fraction(2, 3),
        )

    for s13_sq in [Fraction(1, 100), Fraction(223, 10000), Fraction(1, 20)]:
        check(
            f"phase divisor is nonzero for sin^2(theta_13)={s13_sq}",
            nonsingular_phase_factor_sq(s13_sq) > 0,
        )

    for s13_sq in [0.01, 0.0223, 0.05]:
        cos_delta = implied_cos_delta(s13_sq)
        check(
            f"cos(delta_CP)=0 follows for sin^2(theta_13)={s13_sq}",
            abs(cos_delta) < 1e-12,
            f"cos(delta_CP)={cos_delta:.3e}",
        )

    endpoint = Fraction(2, 3)
    _lhs, endpoint_s12_sq = tm2_sum_rule(endpoint)
    check(
        "endpoint sin^2(theta_13)=2/3 has c12=0 under TM2",
        endpoint_s12_sq == 1 and nonsingular_phase_factor_sq(endpoint) == 0,
    )
    for cos_delta in [Fraction(-1, 1), Fraction(0, 1), Fraction(1, 1)]:
        check(
            f"endpoint phase equation does not force cos(delta_CP)={cos_delta}",
            phase_equation_residual_at_degenerate_endpoint(endpoint, cos_delta) == 0,
        )

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: stipulated-hypothesis TM2 algebraic consequence FAILED.")
        return 1
    print("VERDICT: stipulated-hypothesis TM2 algebraic consequence holds.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
