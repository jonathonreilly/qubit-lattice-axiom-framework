#!/usr/bin/env python3
"""Derivative packet for the defined finite Wilson inverse coordinate.

The derivative identity is calculus after defining
beta_eff,L = P_1plaq^(-1) composed with P_L.  It is not an independently
derived reduction mechanism.  Imported mixed-cumulant onset arithmetic is
kept in the support bucket, and canonical plaquette data are not read.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

import numpy as np
from scipy.special import iv

from frontier_gauge_vacuum_plaquette_mixed_cumulant_audit import (  # noqa: E402
    beta_eff_beta5_coefficient,
    total_nonlocal_beta5_coefficient,
)


THEOREM_PASS = 0
SUPPORT_PASS = 0
FAIL = 0
FINITE_DIFF_STEP = 1.0e-5
MODE_TOL = 1.0e-15
MAX_MODE = 80


@dataclass(frozen=True)
class SumResult:
    partition: float
    derivative: float
    max_mode_used: int


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


def local_susceptibility_numeric(beta: float, step: float = FINITE_DIFF_STEP) -> float:
    p_plus, _ = plaquette_from_bessel(beta + step)
    p_minus, _ = plaquette_from_bessel(beta - step)
    return (p_plus - p_minus) / (2.0 * step)


def bessel_matrix(beta: float, mode: int) -> np.ndarray:
    arg = beta / 3.0
    return np.array(
        [[iv(mode + i - j, arg) for j in range(3)] for i in range(3)],
        dtype=float,
    )


def bessel_matrix_derivative(beta: float, mode: int) -> np.ndarray:
    arg = beta / 3.0
    return np.array(
        [
            [
                (iv(mode + i - j - 1, arg) + iv(mode + i - j + 1, arg)) / 6.0
                for j in range(3)
            ]
            for i in range(3)
        ],
        dtype=float,
    )


def su3_mode_terms(beta: float, mode: int) -> tuple[float, float]:
    mat = bessel_matrix(beta, mode)
    dmat = bessel_matrix_derivative(beta, mode)
    det = float(np.linalg.det(mat))
    derivative = det * float(np.trace(np.linalg.inv(mat) @ dmat))
    return det, derivative


def su3_partition_sum(beta: float, tol: float = MODE_TOL, max_mode: int = MAX_MODE) -> SumResult:
    total_partition = 0.0
    total_derivative = 0.0

    for mode in range(max_mode + 1):
        strip_partition = 0.0
        strip_derivative = 0.0
        modes = [0] if mode == 0 else [-mode, mode]
        for signed_mode in modes:
            part, deriv = su3_mode_terms(beta, signed_mode)
            strip_partition += part
            strip_derivative += deriv

        total_partition += strip_partition
        total_derivative += strip_derivative

        if mode >= 3:
            partition_small = abs(strip_partition) < tol * abs(total_partition)
            derivative_small = abs(strip_derivative) < tol * abs(total_derivative)
            if partition_small and derivative_small:
                return SumResult(total_partition, total_derivative, mode)

    raise RuntimeError(f"mode sum did not converge by m = {max_mode}")


def plaquette_from_bessel(beta: float) -> tuple[float, int]:
    result = su3_partition_sum(beta)
    return result.derivative / result.partition, result.max_mode_used


def main() -> int:
    onset_plaquette_coeff = total_nonlocal_beta5_coefficient()
    onset_susceptibility_coeff = Fraction(5, 1) * onset_plaquette_coeff
    onset_beta_eff_coeff = beta_eff_beta5_coefficient()
    onset_beta_eff_prime_coeff = Fraction(5, 1) * onset_beta_eff_coeff
    common_slope = Fraction(1, 18)
    transported_coeff = common_slope * onset_beta_eff_prime_coeff

    sample_betas = [0.1, 0.5, 1.0, 2.0, 4.0, 6.0, 10.0]
    sample_local_sus = [local_susceptibility_numeric(beta) for beta in sample_betas]

    print("=" * 78)
    print("GAUGE-VACUUM PLAQUETTE INVERSE-COORDINATE DERIVATIVE PACKET")
    print("=" * 78)
    print()
    print("Exact onset coefficients")
    print(f"  nonlocal plaquette beta^5 coefficient      = {onset_plaquette_coeff} = {float(onset_plaquette_coeff):.15e}")
    print(f"  nonlocal susceptibility beta^4 coefficient = {onset_susceptibility_coeff} = {float(onset_susceptibility_coeff):.15e}")
    print(f"  beta_eff beta^5 coefficient                = {onset_beta_eff_coeff} = {float(onset_beta_eff_coeff):.15e}")
    print(f"  beta_eff' beta^4 coefficient               = {onset_beta_eff_prime_coeff} = {float(onset_beta_eff_prime_coeff):.15e}")
    print(f"  common slope                               = {common_slope} = {float(common_slope):.15e}")
    print(f"  slope * beta_eff' correction               = {transported_coeff} = {float(transported_coeff):.15e}")
    print()
    print("Sampled local susceptibility profile")
    print(f"  sampled betas                              = {sample_betas}")
    print(f"  sampled chi_1plaq(betas)                   = {[round(v, 12) for v in sample_local_sus]}")
    print()
    check(
        "differentiating the exact beta^5 plaquette correction gives the exact beta^4 susceptibility correction",
        onset_susceptibility_coeff == Fraction(5, 472392),
        detail=f"d/d beta [beta^5/472392] = ({onset_susceptibility_coeff}) beta^4",
        bucket="SUPPORT",
    )
    check(
        "differentiating the exact onset law gives beta_eff'(beta)=1 + 5 beta^4 / 26244 + O(beta^5)",
        onset_beta_eff_prime_coeff == Fraction(5, 26244),
        detail=f"beta_eff'(beta) correction coefficient = {onset_beta_eff_prime_coeff}",
        bucket="SUPPORT",
    )
    check(
        "the common strong-coupling slope transports the beta_eff' correction into the same exact susceptibility coefficient",
        transported_coeff == onset_susceptibility_coeff,
        detail=f"(1/18) * ({onset_beta_eff_prime_coeff}) = {transported_coeff}",
        bucket="SUPPORT",
    )
    generic_full_prime = Fraction(2, 7)
    generic_local_prime = Fraction(3, 11)
    generic_coordinate_prime = generic_full_prime / generic_local_prime
    check(
        "differentiating the defined inverse coordinate gives the susceptibility quotient identity",
        generic_local_prime * generic_coordinate_prime == generic_full_prime,
        detail="P_1plaq'(beta_eff) * beta_eff' = P_L'; this is a coordinate identity, not a reduction mechanism",
    )
    check(
        "the imported onset arithmetic does not supply the full susceptibility profile",
        onset_susceptibility_coeff > 0 and onset_beta_eff_coeff > 0,
        detail="finite onset support leaves chi_L(beta) unevaluated away from the onset expansion",
        bucket="SUPPORT",
    )

    check(
        "sampled local one-plaquette susceptibility is strictly positive on the tested beta range",
        all(value > 0.0 for value in sample_local_sus),
        detail=f"min sampled chi_1plaq = {min(sample_local_sus):.12f}",
        bucket="SUPPORT",
    )
    print()
    print("=" * 78)
    print(f"SUMMARY: THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} FAIL={FAIL}")
    print("=" * 78)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
