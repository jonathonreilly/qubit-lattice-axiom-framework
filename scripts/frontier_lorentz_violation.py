#!/usr/bin/env python3
"""Compact certificate for the supplied nearest-neighbor cubic symbol.

The only scientific input is the selected spatial kinetic symbol

    K_a(p) = sum_i (4/a^2) sin^2(a p_i/2).

The runner verifies four audit-targeted consequences:

1. its exact Taylor coefficient is ``-a^2/12`` at quartic order;
2. ``sum_i n_i^4`` has normalized cubic-harmonic coefficient
   ``4*sqrt(pi)/15``;
3. the symbol is invariant under all 48 signed permutations in ``O_h`` but a
   fixed proper rotation outside ``O_h`` changes it; and
4. the approved scale-reference conversion ``a^{-1}=M_Pl`` gives the stated
   natural-unit coefficient at one GeV.

This is a class-A algebraic certificate conditional on the supplied symbol.
It does not select an action, derive a relativistic carrier, establish physical
Lorentz violation or CPT, perform SME matching, or test experiment.

The source and stdout are deliberately compact enough to appear in full in
the restricted audit packet (40,000 source characters and 20,000 stdout
characters as of 2026-07-29).
"""

from __future__ import annotations

import itertools
import math
import sys
from collections.abc import Callable

import numpy as np
import sympy as sp


TOL = 1.0e-12
PLANCK_LENGTH_M = 1.616255e-35
HBAR_C_GEV_M = 1.973269804e-16
PLANCK_ENERGY_GEV = 1.220890e19

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str) -> bool:
    """Record and print one executed assertion."""
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    print(f"[{status}] {name}")
    print(f"       {detail}")
    return condition


def section(title: str) -> None:
    print(f"\n{title}\n{'-' * len(title)}")


def signed_permutations() -> tuple[np.ndarray, ...]:
    """Construct the full 48-element signed-permutation representation."""
    elements: list[np.ndarray] = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=np.int64)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            elements.append(matrix)
    return tuple(elements)


def matrix_key(matrix: np.ndarray) -> tuple[int, ...]:
    return tuple(int(entry) for entry in matrix.reshape(-1))


def integer_det3(matrix: np.ndarray) -> int:
    a, b, c = (int(value) for value in matrix[0])
    d, e, f = (int(value) for value in matrix[1])
    g, h, i = (int(value) for value in matrix[2])
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def kinetic_symbol(momentum: np.ndarray, spacing: float) -> float:
    momentum = np.asarray(momentum, dtype=float)
    return float(np.sum((4.0 / spacing**2) * np.sin(spacing * momentum / 2.0) ** 2))


def quartic_direction(direction: np.ndarray) -> float:
    unit = np.asarray(direction, dtype=float)
    unit = unit / np.linalg.norm(unit)
    return float(np.sum(unit**4))


def verify_o_h() -> bool:
    """Verify exact group structure, invariance, and an outside-group control."""
    before = FAIL_COUNT
    section("A. Full O_h action and negative control")

    group = signed_permutations()
    keys = {matrix_key(matrix) for matrix in group}
    identity = np.eye(3, dtype=np.int64)
    determinants = [integer_det3(matrix) for matrix in group]

    check(
        "O_h has 48 distinct signed-permutation matrices",
        len(group) == len(keys) == 48,
        f"constructed={len(group)}, distinct={len(keys)} = 3!*2^3",
    )
    check(
        "O_h has 24 proper and 24 improper elements",
        determinants.count(1) == determinants.count(-1) == 24,
        f"det(+1)={determinants.count(1)}, det(-1)={determinants.count(-1)}",
    )
    check(
        "O_h is closed and contains every inverse",
        all(matrix_key(left @ right) in keys for left in group for right in group)
        and all(matrix_key(matrix.T) in keys for matrix in group)
        and all(np.array_equal(matrix @ matrix.T, identity) for matrix in group),
        "all 48^2 products close and R^-1=R^T is present",
    )

    spacing = 0.731
    momenta = (
        np.array([0.127, -1.937, 2.619]) / spacing,
        np.array([math.pi * (1.0 - 2.0**-20), -2.4, 0.25]) / spacing,
        np.array([math.sqrt(2.0), -math.sqrt(3.0), math.pi / 5.0]) / spacing,
    )
    directions = (
        np.array([1.0, 0.0, 0.0]),
        np.array([1.0, 1.0, 1.0]),
        np.array([1.0, 2.0, 3.0]),
        np.array([math.sqrt(2.0), -math.pi, math.e]),
    )
    kinetic_residual = max(
        abs(kinetic_symbol(matrix @ p, spacing) - kinetic_symbol(p, spacing))
        for matrix in group
        for p in momenta
    )
    quartic_residual = max(
        abs(quartic_direction(matrix @ n) - quartic_direction(n))
        for matrix in group
        for n in directions
    )
    check(
        "the supplied finite-a symbol is invariant under all of O_h",
        kinetic_residual < TOL,
        f"max |K_a(Rp)-K_a(p)|={kinetic_residual:.3e} over 48x{len(momenta)} actions",
    )
    check(
        "sum_i n_i^4 is invariant under all of O_h",
        quartic_residual < TOL,
        f"max quartic residual={quartic_residual:.3e} over 48x{len(directions)} actions",
    )

    angle = math.pi / 7.0
    rotation = np.array(
        [
            [math.cos(angle), -math.sin(angle), 0.0],
            [math.sin(angle), math.cos(angle), 0.0],
            [0.0, 0.0, 1.0],
        ]
    )
    momentum = np.array([2.3, 0.4, -1.1]) / spacing
    distance_to_group = min(float(np.linalg.norm(rotation - matrix)) for matrix in group)
    norm_residual = abs(float(np.linalg.norm(rotation @ momentum) - np.linalg.norm(momentum)))
    symbol_delta = abs(kinetic_symbol(rotation @ momentum, spacing) - kinetic_symbol(momentum, spacing))
    check(
        "R_z(pi/7) is a proper rotation outside O_h and changes the symbol",
        abs(float(np.linalg.det(rotation)) - 1.0) < TOL
        and norm_residual < TOL
        and distance_to_group > 1.0e-3
        and symbol_delta > 1.0e-3,
        "det(R)=%.15f, norm residual=%.3e, distance(O_h)=%.3e, |K(Rp)-K(p)|=%.6f"
        % (float(np.linalg.det(rotation)), norm_residual, distance_to_group, symbol_delta),
    )
    return FAIL_COUNT == before


def verify_taylor_coefficient() -> bool:
    """Extract the low-momentum coefficients from the supplied symbol exactly."""
    before = FAIL_COUNT
    section("B. Exact Taylor coefficient")

    momentum, spacing = sp.symbols("p a", real=True, nonzero=True)
    one_axis_symbol = 4 * sp.sin(spacing * momentum / 2) ** 2 / spacing**2
    series = sp.series(one_axis_symbol, momentum, 0, 8).removeO().expand()
    quadratic = sp.simplify(series.coeff(momentum, 2))
    quartic = sp.simplify(series.coeff(momentum, 4))
    sextic = sp.simplify(series.coeff(momentum, 6))

    check(
        "symbolic series has coefficients 1, -a^2/12, +a^4/360",
        quadratic == 1 and quartic == -spacing**2 / 12 and sextic == spacing**4 / 360,
        f"series={series}; coeff(p^4)={quartic}",
    )

    spacing_num = 0.37
    momentum_num = np.array([0.19, -0.31, 0.47])
    exact = kinetic_symbol(momentum_num, spacing_num)
    through_p4 = float(
        np.sum(momentum_num**2 - spacing_num**2 * momentum_num**4 / 12.0)
    )
    through_p6 = float(
        np.sum(
            momentum_num**2
            - spacing_num**2 * momentum_num**4 / 12.0
            + spacing_num**4 * momentum_num**6 / 360.0
        )
    )
    residual_p4 = abs(exact - through_p4)
    residual_p6 = abs(exact - through_p6)
    check(
        "independent numeric residual falls at the predicted next order",
        residual_p6 < residual_p4 and residual_p6 < 1.0e-9,
        f"|exact-p4|={residual_p4:.3e}, |exact-p6|={residual_p6:.3e}",
    )
    return FAIL_COUNT == before


def sphere_inner(
    left: sp.Expr,
    right: sp.Expr,
    theta: sp.Symbol,
    phi: sp.Symbol,
) -> sp.Expr:
    return sp.simplify(
        sp.integrate(
            sp.integrate(left * sp.conjugate(right) * sp.sin(theta), (phi, 0, 2 * sp.pi)),
            (theta, 0, sp.pi),
        )
    )


def verify_normalized_harmonic() -> bool:
    """Derive the normalized K_4 projection and pointwise identity exactly."""
    before = FAIL_COUNT
    section("C. Normalized cubic-harmonic projection")

    theta, phi = sp.symbols("theta phi", real=True)
    cosine = sp.cos(theta)
    sine = sp.sin(theta)
    f4 = sine**4 * (sp.cos(phi) ** 4 + sp.sin(phi) ** 4) + cosine**4

    # This is exactly Y_40 + sqrt(5/14)(Y_44 + Y_4,-4) in the normalized
    # Condon-Shortley complex basis. The combination is real.
    k4 = (
        3 * (35 * cosine**4 - 30 * cosine**2 + 3)
        + 15 * sine**4 * sp.cos(4 * phi)
    ) / (16 * sp.sqrt(sp.pi))
    coefficient = 4 * sp.sqrt(sp.pi) / 15
    pointwise_residual = sp.trigsimp(sp.expand_trig(f4 - sp.Rational(3, 5) - coefficient * k4))
    pointwise_residual = sp.simplify(pointwise_residual)

    check(
        "normalized harmonic identity holds pointwise",
        pointwise_residual == 0,
        "trigsimp(sum_i n_i^4 - 3/5 - (4*sqrt(pi)/15)K_4)="
        f"{pointwise_residual}",
    )

    norm = sphere_inner(k4, k4, theta, phi)
    overlap = sphere_inner(f4, k4, theta, phi)
    projection = sp.simplify(overlap / norm)
    check(
        "exact normalized projection is 4*sqrt(pi)/15",
        norm == sp.Rational(12, 7)
        and overlap == 16 * sp.sqrt(sp.pi) / 35
        and sp.simplify(projection - coefficient) == 0,
        f"<K_4|K_4>={norm}, <f|K_4>={overlap}, ratio={projection}",
    )

    old_residual = sp.simplify(
        (sp.Rational(4, 5) - coefficient) * k4.subs({theta: 0, phi: 0})
    )
    check(
        "discarded coefficient 4/5 fails in the normalized convention",
        old_residual != 0,
        f"axis residual(old-correct)={old_residual}",
    )

    axis = sp.simplify(f4.subs({theta: 0, phi: 0}))
    diagonal_theta = sp.acos(1 / sp.sqrt(3))
    diagonal = sp.simplify(f4.subs({theta: diagonal_theta, phi: sp.pi / 4}))
    check(
        "directional anisotropy is exactly a factor of three",
        axis == 1 and diagonal == sp.Rational(1, 3) and axis / diagonal == 3,
        f"f4([100])={axis}, f4([111])={diagonal}, ratio={axis / diagonal}",
    )
    return FAIL_COUNT == before


def verify_unit_conversion() -> bool:
    """Recheck the scale-reference illustration with an explicit unit map."""
    before = FAIL_COUNT
    section("D. Approved scale-reference unit conversion")

    # Since 1 GeV^-1 = hbar*c = 1.973269804e-16 m, divide a length in metres
    # by hbar*c to express it in GeV^-1.
    spacing_gev_inverse = PLANCK_LENGTH_M / HBAR_C_GEV_M
    reciprocal_energy = 1.0 / spacing_gev_inverse
    coefficient_gev_inverse2 = spacing_gev_inverse**2 / 12.0
    coefficient_from_energy = 1.0 / (12.0 * PLANCK_ENERGY_GEV**2)
    relative_reciprocal_error = abs(reciprocal_energy / PLANCK_ENERGY_GEV - 1.0)
    relative_coefficient_error = abs(coefficient_gev_inverse2 / coefficient_from_energy - 1.0)

    check(
        "metres to GeV^-1 conversion reproduces the Planck energy reciprocal",
        relative_reciprocal_error < 2.0e-6,
        "a=%.10e GeV^-1, 1/a=%.10e GeV, relative difference=%.3e"
        % (spacing_gev_inverse, reciprocal_energy, relative_reciprocal_error),
    )
    check(
        "a^2/12 gives the one-GeV fractional scale 5.6e-40",
        relative_coefficient_error < 4.0e-6
        and math.isclose(coefficient_gev_inverse2, 5.6e-40, rel_tol=2.0e-3),
        "a^2/12=%.10e GeV^-2; 1/(12 E_Pl^2)=%.10e GeV^-2; relative difference=%.3e"
        % (coefficient_gev_inverse2, coefficient_from_energy, relative_coefficient_error),
    )
    return FAIL_COUNT == before


def main() -> int:
    print("FIXED-ACTION CUBIC-ANISOTROPY CERTIFICATE")
    print("Conditional algebra for the supplied symbol; no physical Lorentz/CPT/SME claim")
    print("=" * 78)

    gates: tuple[tuple[str, Callable[[], bool]], ...] = (
        ("Full O_h action certificate", verify_o_h),
        ("Taylor coefficient check", verify_taylor_coefficient),
        ("Cubic-harmonic identity check", verify_normalized_harmonic),
        ("Unit conversion check", verify_unit_conversion),
    )
    results = [(name, gate()) for name, gate in gates]

    section("Scope boundary")
    print("Verified only for K_a(p)=sum_i (4/a^2) sin^2(a p_i/2).")
    print("Not derived: action selection, carrier/continuum meaning, CPT, SME response,")
    print("or experimental consistency. The scale reference is a units primitive only.")

    section("EXPERIMENT COMPLETE")
    for name, passed in results:
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    print(f"Executed assertions: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("CLAIM_BOUNDARY=conditional_algebraic_diagnostic_for_supplied_symbol")

    return 0 if FAIL_COUNT == 0 and all(passed for _, passed in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
