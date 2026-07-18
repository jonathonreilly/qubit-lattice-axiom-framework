#!/usr/bin/env python3
"""Exact positive finite-jet witness-separation certificate.

The load-bearing proof is rational-polynomial algebra: two entire real
functions share every Taylor coefficient through degree five, have exact
positive derivative lower bounds on [0,6], and separate at beta=6.  A separate
composition block uses the sourced one-plaquette variance theorem and compares
independent Bessel/Weyl evaluations at the two positive arguments.

The certificate's domain is the finite jet plus interval-monotonicity surface.
It makes no hierarchy, compact-measure, Wilson-reduction realizability, or
physical full-surface P(6) assertion.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
from typing import TypeAlias

from frontier_gauge_vacuum_plaquette_bridge_support import (
    plaquette_from_bessel,
    plaquette_from_weyl,
)
from frontier_gauge_vacuum_plaquette_mixed_cumulant_audit import (
    beta_eff_beta5_coefficient,
)


Polynomial: TypeAlias = dict[int, Fraction]

PASS_COUNTS = {"THEOREM": 0, "SUPPORT": 0, "CONTROL": 0}
FAIL = 0

BETA_MIN = Fraction(0, 1)
BETA_FRAMEWORK = Fraction(6, 1)
A_EXPECTED = Fraction(1, 26244)
A = beta_eff_beta5_coefficient()
C = Fraction(1, 10_000_000)
EXPECTED_ENDPOINT_SEPARATION = Fraction(729, 156250)

MONOTONICITY_AUTHORITY = (
    "docs/GAUGE_VACUUM_PLAQUETTE_REDUCTION_EXISTENCE_THEOREM_NOTE.md"
)


def normalized(coefficients: Polynomial) -> Polynomial:
    return {
        degree: coefficient
        for degree, coefficient in coefficients.items()
        if coefficient != 0
    }


def witness_polynomials(
    *,
    a: Fraction,
    c: Fraction,
    perturbation_degree: int = 6,
    minus_linear: Fraction = Fraction(1, 1),
    plus_linear: Fraction = Fraction(1, 1),
) -> tuple[Polynomial, Polynomial]:
    minus = normalized({1: minus_linear, 5: a})
    plus = dict(minus)
    plus[1] = plus_linear
    plus[perturbation_degree] = plus.get(perturbation_degree, Fraction(0, 1)) + c
    return normalized(minus), normalized(plus)


def polynomial_degree(coefficients: Polynomial) -> int:
    return max(coefficients, default=-1)


def polynomial_difference(left: Polynomial, right: Polynomial) -> Polynomial:
    degrees = set(left) | set(right)
    return normalized(
        {
            degree: left.get(degree, Fraction(0, 1))
            - right.get(degree, Fraction(0, 1))
            for degree in degrees
        }
    )


def evaluate_exact(coefficients: Polynomial, x: Fraction) -> Fraction:
    return sum(
        (coefficient * x**degree for degree, coefficient in coefficients.items()),
        start=Fraction(0, 1),
    )


def evaluate_float(coefficients: Polynomial, x: float) -> float:
    return sum(float(coefficient) * x**degree for degree, coefficient in coefficients.items())


def derivative(coefficients: Polynomial) -> Polynomial:
    return normalized(
        {
            degree - 1: Fraction(degree, 1) * coefficient
            for degree, coefficient in coefficients.items()
            if degree > 0
        }
    )


def derivative_lower_bound_on_nonnegative_interval(
    coefficients: Polynomial, upper: Fraction
) -> Fraction:
    """Exact coefficient-wise lower bound for p' on [0, upper]."""

    lower = Fraction(0, 1)
    for degree, coefficient in derivative(coefficients).items():
        if degree == 0:
            lower += coefficient
        elif coefficient < 0:
            lower += coefficient * upper**degree
    return lower


def is_entire_real_polynomial(coefficients: Polynomial) -> bool:
    return all(
        isinstance(degree, int)
        and degree >= 0
        and isinstance(coefficient, Fraction)
        for degree, coefficient in coefficients.items()
    )


def pair_evidence(
    minus: Polynomial, plus: Polynomial, endpoint: Fraction
) -> dict[str, object]:
    difference = polynomial_difference(plus, minus)
    first_difference_degree = min(difference, default=None)
    endpoint_minus = evaluate_exact(minus, endpoint)
    endpoint_plus = evaluate_exact(plus, endpoint)
    endpoint_separation = endpoint_plus - endpoint_minus
    return {
        "difference": difference,
        "first_difference_degree": first_difference_degree,
        "common_jet_through_degree_five": all(
            minus.get(degree, Fraction(0, 1))
            == plus.get(degree, Fraction(0, 1))
            for degree in range(6)
        ),
        "first_difference_is_degree_six": first_difference_degree == 6,
        "minus_derivative_lower_bound": derivative_lower_bound_on_nonnegative_interval(
            minus, endpoint
        ),
        "plus_derivative_lower_bound": derivative_lower_bound_on_nonnegative_interval(
            plus, endpoint
        ),
        "endpoint_minus": endpoint_minus,
        "endpoint_plus": endpoint_plus,
        "endpoint_separation": endpoint_separation,
        "separation_positive": endpoint_separation > 0,
    }


def monotonicity_authority_verified(repo_root: Path) -> bool:
    text = (repo_root / MONOTONICITY_AUTHORITY).read_text(encoding="utf-8")
    needles = (
        "`P_1plaq'(beta) = Var_beta(X)`",
        "`Var_beta(X) > 0`",
        "`P_1plaq(beta)` is strictly increasing on `beta >= 0`",
    )
    return all(needle in text for needle in needles)


def composition_evidence(
    *,
    beta_minus: Fraction,
    beta_plus: Fraction,
    p_minus: float,
    p_plus: float,
    composition_factor: Fraction,
    authority_verified: bool,
) -> dict[str, bool]:
    exact_difference = beta_plus - beta_minus
    positive_domain = beta_minus > 0 and beta_plus > 0
    exact_input_order = (
        composition_factor > 0 and exact_difference == composition_factor
    )
    return {
        "positive_domain": positive_domain,
        "exact_input_order": exact_input_order,
        "theorem_order": authority_verified and positive_domain and exact_input_order,
        "numeric_output_order": p_plus > p_minus,
    }


def check(
    name: str, condition: bool, *, detail: str = "", bucket: str = "THEOREM"
) -> None:
    global FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNTS[bucket] += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


def hostile_control(
    name: str, evidence: dict[str, object], failed_key: str, detail: str
) -> None:
    killed = not bool(evidence[failed_key])
    check(name, killed, detail=detail, bucket="CONTROL")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    minus, plus = witness_polynomials(a=A, c=C)
    evidence = pair_evidence(minus, plus, BETA_FRAMEWORK)

    endpoint_minus = evidence["endpoint_minus"]
    endpoint_plus = evidence["endpoint_plus"]
    endpoint_separation = evidence["endpoint_separation"]
    assert isinstance(endpoint_minus, Fraction)
    assert isinstance(endpoint_plus, Fraction)
    assert isinstance(endpoint_separation, Fraction)

    beta_minus_float = evaluate_float(minus, float(BETA_FRAMEWORK))
    beta_plus_float = evaluate_float(plus, float(BETA_FRAMEWORK))
    float_separation = beta_plus_float - beta_minus_float

    p_minus, mode_minus = plaquette_from_bessel(float(endpoint_minus))
    p_plus, mode_plus = plaquette_from_bessel(float(endpoint_plus))
    p_minus_weyl = plaquette_from_weyl(float(endpoint_minus))
    p_plus_weyl = plaquette_from_weyl(float(endpoint_plus))

    authority_verified = monotonicity_authority_verified(repo_root)
    composition = composition_evidence(
        beta_minus=endpoint_minus,
        beta_plus=endpoint_plus,
        p_minus=p_minus,
        p_plus=p_plus,
        composition_factor=endpoint_separation,
        authority_verified=authority_verified,
    )

    print("=" * 78)
    print("GAUGE-VACUUM PLAQUETTE FINITE-JET WITNESS SEPARATION")
    print("=" * 78)
    print()
    print("Typed exact inputs")
    print(f"  a (mixed-cumulant Fraction helper)   = {A}")
    print(f"  interval                             = [{BETA_MIN}, {BETA_FRAMEWORK}]")
    print(f"  c (rational construction choice)    = {C}")
    print(f"  local monotonicity authority         = {MONOTONICITY_AUTHORITY}")
    print()
    print("Rational-polynomial construction")
    print("  f_-(beta)                            = beta + a beta^5")
    print("  f_+(beta)                            = beta + a beta^5 + c beta^6")
    print(f"  first differing degree              = {evidence['first_difference_degree']}")
    print(f"  exact difference polynomial         = {evidence['difference']}")
    print()
    print("Exact interval and endpoint certificate")
    print(f"  derivative lower bound for f_-      = {evidence['minus_derivative_lower_bound']}")
    print(f"  derivative lower bound for f_+      = {evidence['plus_derivative_lower_bound']}")
    print(f"  f_-(6)                               = {endpoint_minus} = {float(endpoint_minus):.15f}")
    print(f"  f_+(6)                               = {endpoint_plus} = {float(endpoint_plus):.15f}")
    print(
        "  exact separation                    = "
        f"{endpoint_separation} = {float(endpoint_separation):.15f}"
    )
    print(f"  floating-evaluation separation      = {float_separation:.15f}")
    print(f"  f_-'(6)                              = {evaluate_exact(derivative(minus), BETA_FRAMEWORK)}")
    print(f"  f_+'(6)                              = {evaluate_exact(derivative(plus), BETA_FRAMEWORK)}")
    print()
    print("Separate local one-plaquette composition")
    print("  exact theorem                        = P_1plaq'(x) = Var_x(X) > 0")
    print(f"  authority needles verified          = {authority_verified}")
    print(
        f"  P_1plaq(f_-(6)) Bessel              = {p_minus:.15f} "
        f"(mode cutoff m={mode_minus})"
    )
    print(f"  P_1plaq(f_-(6)) Weyl                = {p_minus_weyl:.15f}")
    print(
        f"  P_1plaq(f_+(6)) Bessel              = {p_plus:.15f} "
        f"(mode cutoff m={mode_plus})"
    )
    print(f"  P_1plaq(f_+(6)) Weyl                = {p_plus_weyl:.15f}")
    print(f"  local-block separation              = {p_plus - p_minus:.15f}")
    print()

    check(
        "typed inputs are the exact positive rationals and interval endpoint declared by the theorem",
        A == A_EXPECTED
        and A > 0
        and C == Fraction(1, 10_000_000)
        and C > 0
        and BETA_MIN == 0
        and BETA_FRAMEWORK == 6,
        detail=f"a={A}, c={C}, interval=[{BETA_MIN},{BETA_FRAMEWORK}]",
    )
    check(
        "both witnesses are entire real functions represented as exact rational polynomials",
        is_entire_real_polynomial(minus)
        and is_entire_real_polynomial(plus)
        and polynomial_degree(minus) == 5
        and polynomial_degree(plus) == 6,
        detail=f"degrees=({polynomial_degree(minus)},{polynomial_degree(plus)})",
    )
    check(
        "exact coefficient calculation gives a common Taylor jet through degree five and first difference at degree six",
        bool(evidence["common_jet_through_degree_five"])
        and bool(evidence["first_difference_is_degree_six"])
        and evidence["difference"] == {6: C},
        detail=f"difference coefficients={evidence['difference']}",
    )
    check(
        "the minus witness has an exact strictly positive derivative lower bound on [0,6]",
        evidence["minus_derivative_lower_bound"] == 1,
        detail="coefficient-wise analytic lower bound = 1",
    )
    check(
        "the plus witness has an exact strictly positive derivative lower bound on [0,6]",
        evidence["plus_derivative_lower_bound"] == 1,
        detail="coefficient-wise analytic lower bound = 1",
    )
    check(
        "exact Fraction evaluation gives the required positive beta=6 separation",
        endpoint_separation
        == C * BETA_FRAMEWORK**6
        == EXPECTED_ENDPOINT_SEPARATION
        and bool(evidence["separation_positive"]),
        detail=f"delta={endpoint_separation}=0.0046656 exactly",
    )
    check(
        "strict increase of the sourced local one-plaquette block preserves the exact input order",
        composition["theorem_order"],
        detail=(
            f"0 < {endpoint_minus} < {endpoint_plus}; "
            "P_1plaq'(x)=Var_x(X)>0 on the displayed positive arguments"
        ),
    )

    check(
        "direct floating polynomial evaluation agrees with the exact endpoint separation",
        abs(float_separation - float(endpoint_separation)) < 2.0e-15,
        detail=(
            f"float delta={float_separation:.15f}, "
            f"exact delta={float(endpoint_separation):.15f}"
        ),
        bucket="SUPPORT",
    )
    check(
        "Bessel and Weyl local-block evaluations agree and retain strict output order",
        composition["numeric_output_order"]
        and abs(p_minus - p_minus_weyl) < 1.0e-12
        and abs(p_plus - p_plus_weyl) < 1.0e-12,
        detail=(
            f"Bessel-Weyl deltas=({abs(p_minus-p_minus_weyl):.3e},"
            f"{abs(p_plus-p_plus_weyl):.3e}); output delta={p_plus-p_minus:.15f}"
        ),
        bucket="SUPPORT",
    )

    degree_five_minus, degree_five_plus = witness_polynomials(
        a=A, c=C, perturbation_degree=5
    )
    degree_five_evidence = pair_evidence(
        degree_five_minus, degree_five_plus, BETA_FRAMEWORK
    )
    hostile_control(
        "degree-five perturbation is rejected by the common-jet validator",
        degree_five_evidence,
        "common_jet_through_degree_five",
        f"mutated difference={degree_five_evidence['difference']}",
    )

    zero_minus, zero_plus = witness_polynomials(a=A, c=Fraction(0, 1))
    zero_evidence = pair_evidence(zero_minus, zero_plus, BETA_FRAMEWORK)
    hostile_control(
        "c=0 mutation is rejected by the exact separation validator",
        zero_evidence,
        "separation_positive",
        f"mutated separation={zero_evidence['endpoint_separation']}",
    )

    sign_minus, sign_plus = witness_polynomials(
        a=A, c=C, plus_linear=Fraction(-1, 1)
    )
    sign_evidence = pair_evidence(sign_minus, sign_plus, BETA_FRAMEWORK)
    derivative_mutation = {
        "interval_derivative_positive": sign_evidence[
            "plus_derivative_lower_bound"
        ]
        > 0
    }
    hostile_control(
        "negative-linear-sign mutation is rejected by the interval derivative validator",
        derivative_mutation,
        "interval_derivative_positive",
        f"mutated exact lower bound={sign_evidence['plus_derivative_lower_bound']}",
    )

    swapped_composition = composition_evidence(
        beta_minus=endpoint_minus,
        beta_plus=endpoint_plus,
        p_minus=p_plus,
        p_plus=p_minus,
        composition_factor=endpoint_separation,
        authority_verified=authority_verified,
    )
    hostile_control(
        "swapped local plaquette values are rejected by the strict-output-order validator",
        swapped_composition,
        "numeric_output_order",
        f"mutated output delta={p_minus-p_plus:.15f}",
    )

    missing_factor_composition = composition_evidence(
        beta_minus=endpoint_minus,
        beta_plus=endpoint_plus,
        p_minus=p_minus,
        p_plus=p_plus,
        composition_factor=Fraction(0, 1),
        authority_verified=authority_verified,
    )
    hostile_control(
        "missing composition factor is rejected by the exact input-order validator",
        missing_factor_composition,
        "exact_input_order",
        "mutated composition factor=0",
    )

    print()
    print("=" * 78)
    print(
        "SUMMARY: "
        f"THEOREM PASS={PASS_COUNTS['THEOREM']} "
        f"SUPPORT={PASS_COUNTS['SUPPORT']} "
        f"CONTROL PASS={PASS_COUNTS['CONTROL']} FAIL={FAIL}"
    )
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
