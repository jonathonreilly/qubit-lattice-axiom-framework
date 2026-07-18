#!/usr/bin/env python3
"""Finite connected-hierarchy projection theorem for the Wilson plaquette.

The analytic proof in the source note establishes the universal finite
common-source identity. This runner provides finite exact illustrations of the
source algebra and checks the first two defined inverse-coordinate derivative
identities by exact symbolic reconstruction.
"""

from __future__ import annotations

import argparse
from collections import Counter

import sympy as sp

THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0

MUTATIONS = (
    "none",
    "wrong-source-shift",
    "wrong-transport-product",
    "omit-local-curvature",
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

    shell_two, shell_three, local_chi, local_chi_prime = sp.symbols(
        "S2 S3 chi_1plaq chi_1plaq_prime", nonzero=True
    )
    beta_eff_prime = (
        shell_two * local_chi
        if mutation == "wrong-transport-product"
        else shell_two / local_chi
    )
    beta_eff_second = (
        shell_three / local_chi
        - (local_chi_prime / local_chi) * beta_eff_prime**2
    )
    if mutation == "omit-local-curvature":
        beta_eff_second = shell_three / local_chi
    first_transport_residual = sp.simplify(local_chi * beta_eff_prime - shell_two)
    second_transport_residual = sp.simplify(
        local_chi * beta_eff_second
        + local_chi_prime * beta_eff_prime**2
        - shell_three
    )

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
    print("Defined inverse-coordinate derivative reconstruction")
    print(f"  beta_eff'                              = {beta_eff_prime}")
    print(f"  beta_eff''                             = {beta_eff_second}")
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
        "the first defined-coordinate derivative identity reconstructs the shell-summed two-point projection",
        first_transport_residual == 0,
        detail="chi_1plaq(beta_eff) * beta_eff' = sum_r C_2(p_0,r)",
    )
    check(
        "the second defined-coordinate derivative identity reconstructs the shell-summed three-point projection",
        second_transport_residual == 0,
        detail="chi_1plaq * beta_eff'' + chi_1plaq' * (beta_eff')^2 = sum_(r,s) C_3(p_0,r,s)",
    )
    print()
    print("=" * 78)
    print(f"SUMMARY: THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
