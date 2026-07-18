#!/usr/bin/env python3
"""Finite connected-hierarchy projection theorem for the Wilson plaquette.

The analytic proof in the source note establishes the universal finite
common-source identity. This runner provides finite exact illustrations of the
source algebra and independently checks the corrected shell-summed three-point
onset by two exact symbolic routes.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import sys

import sympy as sp

sys.path.insert(0, "scripts")

from frontier_gauge_vacuum_plaquette_mixed_cumulant_audit import (  # noqa: E402
    beta_eff_beta5_coefficient,
    total_nonlocal_beta5_coefficient,
)


THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0

EXPECTED_PLAQUETTE_DIFFERENCE = Fraction(1, 472392)
EXPECTED_BETA_EFF_SHIFT = Fraction(1, 26244)
LOCAL_ONE_PLAQUETTE_SLOPE = Fraction(1, 18)
EXPECTED_THREE_POINT_DIFFERENCE = Fraction(5, 118098)

MUTATIONS = (
    "none",
    "omit-local-baseline",
    "wrong-derivative-order",
    "wrong-beta-eff-coefficient",
    "wrong-source-shift",
)


def check(name: str, condition: bool, detail: str = "", bucket: str = "THEOREM") -> None:
    global THEOREM_PASS, SUPPORT_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        if bucket == "SUPPORT":
            SUPPORT_PASS += 1
        else:
            THEOREM_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


def beta_derivative_of_monomial(alpha: tuple[int, ...]) -> Counter[tuple[int, ...]]:
    """Derivative after the uniform shift y_r = beta + J_r."""
    out: Counter[tuple[int, ...]] = Counter()
    for idx, power in enumerate(alpha):
        if power == 0:
            continue
        reduced = list(alpha)
        reduced[idx] -= 1
        out[tuple(reduced)] += power
    return out


def source_derivative_of_monomial(alpha: tuple[int, ...], idx: int) -> Counter[tuple[int, ...]]:
    out: Counter[tuple[int, ...]] = Counter()
    power = alpha[idx]
    if power == 0:
        return out
    reduced = list(alpha)
    reduced[idx] -= 1
    out[tuple(reduced)] += power
    return out


def source_indices(size: int, mutation: str) -> range:
    if mutation == "wrong-source-shift":
        return range(size - 1)
    return range(size)


def sum_source_derivatives(alpha: tuple[int, ...], mutation: str) -> Counter[tuple[int, ...]]:
    out: Counter[tuple[int, ...]] = Counter()
    for idx in source_indices(len(alpha), mutation):
        out += source_derivative_of_monomial(alpha, idx)
    return out


def second_level_identity(
    alpha: tuple[int, ...], fixed_idx: int, mutation: str
) -> tuple[Counter[tuple[int, ...]], Counter[tuple[int, ...]]]:
    left: Counter[tuple[int, ...]] = Counter()
    for reduced_alpha, coeff in source_derivative_of_monomial(alpha, fixed_idx).items():
        left += Counter(
            {
                monomial: coeff * value
                for monomial, value in beta_derivative_of_monomial(reduced_alpha).items()
            }
        )

    right: Counter[tuple[int, ...]] = Counter()
    for idx in source_indices(len(alpha), mutation):
        for reduced_alpha, coeff in source_derivative_of_monomial(alpha, idx).items():
            right += Counter(
                {
                    monomial: coeff * value
                    for monomial, value in source_derivative_of_monomial(
                        reduced_alpha, fixed_idx
                    ).items()
                }
            )
    return left, right


def as_sympy(value: Fraction) -> sp.Rational:
    return sp.Rational(value.numerator, value.denominator)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mutation",
        choices=MUTATIONS,
        default="none",
        help="hostile mutation used to verify that a load-bearing check fails",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    mutation = args.mutation

    illustration_basis = [
        (0, 0, 0),
        (1, 0, 0),
        (0, 0, 2),
        (2, 1, 0),
        (1, 1, 1),
        (3, 2, 1),
        (4, 0, 2),
    ]
    first_identity_ok = all(
        beta_derivative_of_monomial(alpha) == sum_source_derivatives(alpha, mutation)
        for alpha in illustration_basis
    )
    second_identity_ok = all(
        second_level_identity(alpha, fixed_idx, mutation)[0]
        == second_level_identity(alpha, fixed_idx, mutation)[1]
        for alpha in illustration_basis
        for fixed_idx in range(len(alpha))
    )

    supplied_plaquette_difference = total_nonlocal_beta5_coefficient()
    supplied_beta_eff_shift = beta_eff_beta5_coefficient()
    derivative_order = 1 if mutation == "wrong-derivative-order" else 2
    route_beta_eff_shift = (
        Fraction(1, 26245)
        if mutation == "wrong-beta-eff-coefficient"
        else supplied_beta_eff_shift
    )

    beta = sp.symbols("beta")
    route1_polynomial = as_sympy(supplied_plaquette_difference) * beta**5
    route1_derivative = sp.diff(route1_polynomial, beta, derivative_order)
    route1_beta3_coefficient = sp.expand(route1_derivative).coeff(beta, 3)

    c1, c2, c3, c4, c5, c6 = sp.symbols("c1 c2 c3 c4 c5 c6")
    local_series = sum(
        coefficient * beta**power
        for power, coefficient in enumerate((c1, c2, c3, c4, c5, c6), start=1)
    )
    beta_eff_series = beta + as_sympy(route_beta_eff_shift) * beta**5
    transported_series = sp.expand(local_series.subs(beta, beta_eff_series))
    transported_derivative = sp.diff(transported_series, beta, derivative_order)
    local_baseline = sp.diff(local_series, beta, derivative_order)
    if mutation == "omit-local-baseline":
        route2_difference = transported_derivative
    else:
        route2_difference = transported_derivative - local_baseline
    route2_beta3_coefficient = sp.expand(route2_difference).coeff(beta, 3)
    route2_generic_expected = 20 * as_sympy(route_beta_eff_shift) * c1
    route2_at_local_slope = sp.simplify(
        route2_beta3_coefficient.subs(c1, as_sympy(LOCAL_ONE_PLAQUETTE_SLOPE))
    )

    shell_two, shell_three, local_chi, local_chi_prime = sp.symbols(
        "S2 S3 chi_1plaq chi_1plaq_prime", nonzero=True
    )
    beta_eff_prime = shell_two / local_chi
    beta_eff_second = (
        shell_three / local_chi
        - (local_chi_prime / local_chi) * beta_eff_prime**2
    )
    first_transport_residual = sp.simplify(local_chi * beta_eff_prime - shell_two)
    second_transport_residual = sp.simplify(
        local_chi * beta_eff_second
        + local_chi_prime * beta_eff_prime**2
        - shell_three
    )

    expected_three_point = as_sympy(EXPECTED_THREE_POINT_DIFFERENCE)

    print("=" * 78)
    print("GAUGE-VACUUM PLAQUETTE FINITE CONNECTED-HIERARCHY PROJECTION THEOREM")
    print("=" * 78)
    print()
    print(f"Hostile mutation                         = {mutation}")
    print()
    print("Finite source-shift illustrations")
    print(f"  monomial illustration basis            = {illustration_basis}")
    print(f"  common-source identity illustrated     = {first_identity_ok}")
    print(f"  next hierarchy level illustrated       = {second_identity_ok}")
    print()
    print("Exact supplied onset data")
    print(f"  P_L - P_1plaq beta^5 coefficient       = {supplied_plaquette_difference}")
    print(f"  beta_eff beta^5 coefficient            = {route_beta_eff_shift}")
    print(f"  chi_1plaq(0)                           = {LOCAL_ONE_PLAQUETTE_SLOPE}")
    print(f"  derivative order used                  = {derivative_order}")
    print()
    print("Independent exact routes to the corrected beta^3 coefficient")
    print(f"  route 1 coefficient                    = {route1_beta3_coefficient}")
    print(f"  route 2 generic coefficient            = {route2_beta3_coefficient}")
    print(f"  route 2 at chi_1plaq(0)=1/18           = {route2_at_local_slope}")
    print(f"  expected full-minus-local coefficient  = {expected_three_point}")
    print()

    check(
        "the finite common-source identity is illustrated exactly on the stated monomials",
        first_identity_ok,
        detail="finite illustration only; the note proves the universal identity by the multivariable chain rule",
        bucket="SUPPORT",
    )
    check(
        "the next hierarchy level is illustrated exactly on the same finite basis",
        second_identity_ok,
        detail="finite illustration after one fixed source derivative",
        bucket="SUPPORT",
    )
    check(
        "the supplied full-minus-one-plaquette onset coefficient is source-bound exactly",
        supplied_plaquette_difference == EXPECTED_PLAQUETTE_DIFFERENCE,
        detail=f"P_L - P_1plaq = ({supplied_plaquette_difference}) beta^5 + O(beta^6)",
        bucket="SUPPORT",
    )
    check(
        "the beta_eff route uses the exact supplied beta^5 coefficient",
        route_beta_eff_shift == EXPECTED_BETA_EFF_SHIFT,
        detail=f"beta_eff - beta = ({route_beta_eff_shift}) beta^5 + O(beta^6)",
        bucket="SUPPORT",
    )
    check(
        "the first beta_eff derivative transport formula reconstructs the shell-summed two-point projection",
        first_transport_residual == 0,
        detail="chi_1plaq(beta_eff) * beta_eff' = sum_r C_2(p_0,r)",
    )
    check(
        "the second beta_eff derivative transport formula reconstructs the shell-summed three-point projection",
        second_transport_residual == 0,
        detail="chi_1plaq * beta_eff'' + chi_1plaq' * (beta_eff')^2 = sum_(r,s) C_3(p_0,r,s)",
    )
    check(
        "twice differentiating the supplied plaquette difference gives 5/118098 at order beta^3",
        route1_beta3_coefficient == expected_three_point,
        detail=f"d^2/d beta^2 [beta^5/472392] has beta^3 coefficient {route1_beta3_coefficient}",
    )
    check(
        "generic one-plaquette composition leaves only 20 * chi_1plaq(0) * a at order beta^3 after baseline subtraction",
        sp.simplify(route2_beta3_coefficient - route2_generic_expected) == 0,
        detail=f"generic coefficient = {route2_beta3_coefficient}; c2 through c6 cancel",
    )
    check(
        "the beta_eff composition route gives the same corrected full-minus-local coefficient",
        route2_at_local_slope == expected_three_point,
        detail=f"20 * (1/18) * ({route_beta_eff_shift}) = {route2_at_local_slope}",
    )
    check(
        "both exact routes agree on the coefficient in sum C_3 minus the local chi_1plaq' baseline",
        route1_beta3_coefficient == route2_at_local_slope == expected_three_point,
        detail="sum_(r,s) C_3 - chi_1plaq' = (5/118098) beta^3 + O(beta^4)",
    )

    print()
    print("=" * 78)
    print(f"SUMMARY: THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
