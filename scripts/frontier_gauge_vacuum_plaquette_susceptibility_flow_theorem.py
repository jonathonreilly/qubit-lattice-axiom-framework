#!/usr/bin/env python3
"""Derivative packet for the defined finite Wilson inverse coordinate.

The derivative identity is calculus after defining
beta_eff,L = P_1plaq^(-1) composed with P_L.  It is not an independently
derived reduction mechanism.  Canonical plaquette and mixed-cumulant data are
not read.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

import numpy as np
from scipy.special import iv

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


def independent_polynomial_derivative_model(
    beta: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    """Differentiate an independently expanded exact composition.

    local(x)=x+x^3, coordinate(beta)=beta+beta^2, and
    full(beta)=beta+beta^2+beta^3+3 beta^4+3 beta^5+beta^6.
    """

    coordinate = beta + beta**2
    local_prime = 1 + 3 * coordinate**2
    coordinate_prime = 1 + 2 * beta
    expanded_full_prime = (
        1
        + 2 * beta
        + 3 * beta**2
        + 12 * beta**3
        + 15 * beta**4
        + 6 * beta**5
    )
    return expanded_full_prime, local_prime, coordinate_prime


def main() -> int:
    sample_betas = [0.1, 0.5, 1.0, 2.0, 4.0, 6.0, 10.0]
    sample_local_sus = [local_susceptibility_numeric(beta) for beta in sample_betas]

    print("=" * 78)
    print("GAUGE-VACUUM PLAQUETTE INVERSE-COORDINATE DERIVATIVE PACKET")
    print("=" * 78)
    print()
    print("Sampled local susceptibility profile")
    print(f"  sampled betas                              = {sample_betas}")
    print(f"  sampled chi_1plaq(betas)                   = {[round(v, 12) for v in sample_local_sus]}")
    print()
    model_beta = Fraction(2, 5)
    full_prime, local_prime, coordinate_prime = independent_polynomial_derivative_model(
        model_beta
    )
    check(
        "an independently expanded exact composition gives the susceptibility quotient identity",
        full_prime == local_prime * coordinate_prime
        and full_prime / local_prime == coordinate_prime,
        detail=(
            "local(x)=x+x^3 and coordinate(beta)=beta+beta^2; "
            f"at beta={model_beta}, full'={full_prime}, local'={local_prime}, "
            f"coordinate'={coordinate_prime}"
        ),
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
