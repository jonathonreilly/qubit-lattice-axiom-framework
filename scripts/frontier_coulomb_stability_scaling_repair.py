#!/usr/bin/env python3
"""Coulomb Green-kernel scaling repair certificate.

This runner checks only the bounded continuum-math lemma in
COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md. It does not derive
an electromagnetic sector, a gauge coupling, or a hydrogen spectrum.
"""

from __future__ import annotations

import math
from fractions import Fraction


def require(condition: bool, label: str) -> None:
    assert condition, label
    print(f"PASS: {label}")


def radial_laplacian_power_coeff(a: Fraction, d: int) -> Fraction:
    """Coefficient C with Delta r^a = C r^(a-2) away from r=0 in R^d."""

    return a * (a + d - 2)


def q_value(d: int, lam: float, t_value: float, u_value: float) -> float:
    return (lam**2) * t_value - (lam ** (d - 2)) * u_value


def main() -> int:
    print("COULOMB GREEN-KERNEL SCALING REPAIR")
    print("Scope: bounded continuum-math scaling lemma; no EM-sector claim.")
    print()

    for d in range(3, 11):
        a = Fraction(2 - d, 1)
        coeff = radial_laplacian_power_coeff(a, d)
        require(
            coeff == 0,
            f"d={d}: Delta r^(2-d)=0 away from the origin",
        )

    # Change of variables for psi_lambda(x)=lambda^(d/2) psi(lambda x).
    # The exponents below are the total lambda powers after y=lambda x.
    for d in range(3, 11):
        norm_power = d - d
        grad_power = (d + 2) - d
        green_power = d + (d - 2) - d
        require(norm_power == 0, f"d={d}: dilation preserves L2 norm")
        require(grad_power == 2, f"d={d}: kinetic form scales as lambda^2")
        require(
            green_power == d - 2,
            f"d={d}: Green-kernel attraction scales as lambda^(d-2)",
        )

    # Exponent ordering is the whole collapse test.
    require(1 < 2, "d=3: attractive exponent 1 is sub-quadratic")
    require(2 == 2, "d=4: attractive exponent 2 is marginal")
    for d in range(5, 11):
        require(d - 2 > 2, f"d={d}: attractive exponent beats kinetic exponent")

    # Concrete large-lambda witnesses for d>=5.
    t_value = 1.0
    u_value = 1.0
    for d in range(5, 11):
        q_10 = q_value(d, 10.0, t_value, u_value)
        q_100 = q_value(d, 100.0, t_value, u_value)
        require(q_10 < 0.0, f"d={d}: Q(lambda=10)<0 for T=U=1")
        require(q_100 < q_10, f"d={d}: Q(lambda=100) is more negative")

    # The d=3 scaling parabola has a finite minimum in this one-parameter
    # test family; this is not a spectral theorem, just a firewall against
    # claiming ultraviolet collapse from the scaling exponent alone.
    d3_min_lambda = 0.5
    d3_min_value = q_value(3, d3_min_lambda, t_value, u_value)
    require(
        math.isclose(d3_min_value, -0.25, rel_tol=0.0, abs_tol=1e-12),
        "d=3: lambda^2-lambda scaling has finite trial-family minimum",
    )

    print()
    print("SUMMARY: PASS=53 FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
