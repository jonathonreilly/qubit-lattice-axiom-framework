#!/usr/bin/env python3
"""
Finite check packet for the Bertrand stable-orbit upper-bound support note.

This runner verifies the in-packet continuum Green-kernel bridge used by
docs/BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md:

  * for every checked integer d >= 3, the radial kernel r^(2-d) is harmonic
    away from the source under the d-dimensional radial Laplacian;
  * the normalized kernel G_d(r)=1/((d-2) S_{d-1}) r^(2-d) has unit flux;
  * the attractive potential has the shape -k/r^(d-2), with constants
    absorbed into k;
  * the circular-orbit effective-potential algebra gives stable d=3,
    marginal d=4, and unstable d>=5.

No observational values, fitted selectors, or new axioms are used.
"""
from __future__ import annotations

import math


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name, condition, detail=""):
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"[{status}] {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)


def sphere_area(d):
    """Area of S^{d-1} embedded in R^d."""
    return 2.0 * math.pi ** (d / 2.0) / math.gamma(d / 2.0)


def radial_laplacian_power_exponent(d, q):
    """Delta r^q = q(q+d-2) r^(q-2) away from r=0."""
    return q * (q + d - 2)


def green_coeff(d):
    return 1.0 / ((d - 2) * sphere_area(d))


def green_kernel(d, r):
    return green_coeff(d) * r ** (2 - d)


def minus_radial_derivative_green(d, r):
    # -d/dr [c r^(2-d)] = c(d-2) r^(1-d)
    return green_coeff(d) * (d - 2) * r ** (1 - d)


def second_derivative_at_circular_orbit(d, k=2.3, m=1.7, r=1.4):
    # V_eff = -k r^(2-d) + L^2/(2 m r^2).
    # Circularity gives L^2 = m k (d-2) r^(4-d).
    L2 = m * k * (d - 2) * r ** (4 - d)
    direct = -k * (d - 2) * (d - 1) * r ** (-d) + 3.0 * L2 / (m * r ** 4)
    reduced = k * (d - 2) * (4 - d) * r ** (-d)
    return direct, reduced


def main():
    print("Bertrand stable-orbit Green-kernel bridge")
    print("=" * 52)

    dims = list(range(3, 13))

    max_laplace_coeff = max(abs(radial_laplacian_power_exponent(d, 2 - d)) for d in dims)
    check(
        "r^(2-d) is radial-harmonic away from the source for checked d>=3",
        max_laplace_coeff < 1e-14,
        f"max coefficient q(q+d-2) = {max_laplace_coeff:.1e}",
    )

    max_flux_err = 0.0
    flux_ok = True
    for d in dims:
        for r in (0.4, 1.0, 3.7):
            flux = minus_radial_derivative_green(d, r) * sphere_area(d) * r ** (d - 1)
            max_flux_err = max(max_flux_err, abs(flux - 1.0))
            flux_ok = flux_ok and math.isclose(flux, 1.0, rel_tol=0.0, abs_tol=1e-13)
    check(
        "G_d(r)=1/((d-2)S_{d-1}) r^(2-d) has unit outward -grad flux",
        flux_ok,
        f"max flux residual = {max_flux_err:.1e}",
    )

    max_shape_err = 0.0
    for d in dims:
        k = 5.0
        # Constants from the Green normalization can be absorbed into k; the
        # shape must be exactly r^(2-d).
        for r in (0.5, 2.0):
            V_shape = -k * r ** (2 - d)
            V_from_green = -(k / green_coeff(d)) * green_kernel(d, r)
            max_shape_err = max(max_shape_err, abs(V_shape - V_from_green))
    check(
        "Attractive Green potential has shape V(r)=-k/r^(d-2) for all checked d",
        max_shape_err < 1e-12,
        f"max shape residual = {max_shape_err:.1e}",
    )

    max_second_err = 0.0
    second_ok = True
    signs = {}
    for d in dims:
        direct, reduced = second_derivative_at_circular_orbit(d)
        max_second_err = max(max_second_err, abs(direct - reduced))
        second_ok = second_ok and math.isclose(direct, reduced, rel_tol=0.0, abs_tol=1e-14)
        signs[d] = 1 if reduced > 0 else (-1 if reduced < 0 else 0)
    check(
        "Effective-potential second derivative reduces to k(d-2)(4-d)/r_c^d",
        second_ok,
        f"max direct-vs-reduced residual = {max_second_err:.1e}",
    )

    check("d=3 circular orbit is stable", signs[3] == 1, f"sign={signs[3]}")
    check("d=4 circular orbit is marginal", signs[4] == 0, f"sign={signs[4]}")
    check(
        "all checked integer d>=5 circular orbits are unstable",
        all(signs[d] == -1 for d in range(5, 13)),
        "signs=" + ",".join(f"{d}:{signs[d]}" for d in range(5, 13)),
    )

    check(
        "Bridge scope excludes d=1 and d=2 logarithmic/one-dimensional cases",
        all(d >= 3 for d in dims),
        f"checked dims={dims[0]}..{dims[-1]}",
    )

    print("=" * 52)
    print(f"SCORECARD: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
