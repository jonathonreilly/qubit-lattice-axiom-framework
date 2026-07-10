#!/usr/bin/env python3
"""Check exact free formulas and one finite contact-model comparison.

No universal source, WEP, static-class, or mediator conclusion is tested.
"""

from __future__ import annotations

import numpy as np
import sympy as sp

from composite_mass_additivity_binding_defect_2026_07_08 import (
    lowest_pblock_energy,
    near_zero_indices,
    signed_momentum_value,
)


PASS_COUNT = 0
FAIL_COUNT = 0
FIT_RESID_TOL = 1.0e-6


def report(name: str, ok: bool, residual: float, detail: str) -> None:
    global PASS_COUNT, FAIL_COUNT
    PASS_COUNT += int(ok)
    FAIL_COUNT += int(not ok)
    print(f"{name}: {'PASS' if ok else 'FAIL'} residual={residual:.3e} {detail}")


def rest_gap(mass: float) -> float:
    return float(np.arcsinh(mass))


def inertial_coefficient(mass: float) -> float:
    return float(mass * np.sqrt(1.0 + mass * mass))


def source_function(value: float) -> float:
    return float(0.5 * np.sinh(2.0 * value))


def check_conditional_single_formula() -> None:
    x, c = sp.symbols("x c", real=True)
    coefficient = sp.sinh(x) * sp.cosh(x)
    residual = sp.simplify(c * coefficient - c * sp.sinh(2 * x) / 2)
    report(
        "CHECK-01 CONDITIONAL-SINGLE-FORMULA",
        residual == 0,
        0.0 if residual == 0 else 1.0,
        f"symbolic_residual={residual}",
    )


def check_free_composite_formula() -> None:
    x = sp.symbols("x", positive=True, real=True)
    F = lambda z: sp.sinh(2 * z) / 2
    residual = sp.simplify(F(2 * x) / (2 * F(x)) - sp.cosh(2 * x))
    series = sp.series(sp.cosh(2 * x) - 1, x, 0, 6)
    coefficient = sp.expand(series.removeO()).coeff(x, 2)
    ok = residual == 0 and coefficient == 2
    report(
        "CHECK-02 FREE-COMPOSITE-FORMULA",
        ok,
        0.0 if ok else 1.0,
        f"identity_residual={residual} series={series}",
    )


def check_small_parameter_formulas() -> None:
    m, x = sp.symbols("m x", real=True)
    expr_a = 1 - 1 / sp.sqrt(1 + m**2)
    expr_b = sp.sinh(2 * x) / (2 * x) - 1
    expr_c = sp.cosh(2 * x) - 1
    coefficients = (
        sp.expand(sp.series(expr_a, m, 0, 4).removeO()).coeff(m, 2),
        sp.expand(sp.series(expr_b, x, 0, 4).removeO()).coeff(x, 2),
        sp.expand(sp.series(expr_c, x, 0, 4).removeO()).coeff(x, 2),
    )
    expected = (sp.Rational(1, 2), sp.Rational(2, 3), sp.Integer(2))
    ok = coefficients == expected
    report(
        "CHECK-03 SMALL-PARAMETER-FORMULAS",
        ok,
        0.0 if ok else 1.0,
        f"coefficients={coefficients}",
    )


def fitted_curvature_mass(length: int, mass: float, coupling: float) -> tuple[float, float]:
    # Five distinct p^2 values constrain four even-polynomial coefficients.
    # The former radius-3 window had only four distinct p^2 values and therefore
    # interpolated every even input exactly, making its fit residual vacuous.
    indices = near_zero_indices(length, 4)
    momenta = np.array([signed_momentum_value(index, length) for index in indices], dtype=float)
    energies = np.array(
        [lowest_pblock_energy(length, mass, mass, coupling, index) for index in indices],
        dtype=float,
    )
    x2 = momenta * momenta
    design = np.column_stack((np.ones_like(x2), x2, x2**2, x2**3))
    coefficients, *_ = np.linalg.lstsq(design, energies, rcond=None)
    fitted = design @ coefficients
    curvature = 2.0 * float(coefficients[1])
    fitted_mass = float("inf") if curvature == 0.0 else 1.0 / curvature
    residual = float(np.max(np.abs(fitted - energies)))
    return fitted_mass, residual


def tune_to_energy(length: int, mass: float, target: float) -> tuple[float, float]:
    low, high = 0.0, 1.0
    while lowest_pblock_energy(length, mass, mass, high, 0) > target:
        high *= 2.0
        if high > 64.0:
            raise RuntimeError("failed to bracket finite contact comparator")
    measured = float("nan")
    for _ in range(100):
        middle = 0.5 * (low + high)
        measured = lowest_pblock_energy(length, mass, mass, middle, 0)
        if measured > target:
            low = middle
        else:
            high = middle
    coupling = 0.5 * (low + high)
    measured = lowest_pblock_energy(length, mass, mass, coupling, 0)
    return coupling, measured


def check_finite_same_energy_comparator() -> None:
    length = 64
    masses = (0.5, 0.6)
    target = 0.90 * min(2.0 * rest_gap(mass) for mass in masses)
    rows: list[str] = []
    energies: list[float] = []
    fitted_masses: list[float] = []
    fit_residuals: list[float] = []
    for mass in masses:
        coupling, measured = tune_to_energy(length, mass, target)
        fitted_mass, fit_residual = fitted_curvature_mass(length, mass, coupling)
        energies.append(measured)
        fitted_masses.append(fitted_mass)
        fit_residuals.append(fit_residual)
        rows.append(
            f"m={mass:.1f},U={coupling:.10e},E0={measured:.12e},"
            f"Mcurv={fitted_mass:.12e},fit_resid={fit_residual:.3e}"
        )
    energy_mismatch = abs(energies[0] - energies[1])
    fitted_masses_ok = all(
        np.isfinite(value) and value > 0.0 for value in fitted_masses
    )
    relative_mass_separation = (
        abs(fitted_masses[0] - fitted_masses[1])
        / max(abs(value) for value in fitted_masses)
        if fitted_masses_ok
        else float("nan")
    )
    fit_residuals_ok = all(
        np.isfinite(value) and value <= FIT_RESID_TOL for value in fit_residuals
    )
    max_fit_residual = (
        max(fit_residuals) if all(np.isfinite(value) for value in fit_residuals)
        else float("inf")
    )
    ok = (
        energy_mismatch <= 1.0e-10
        and fitted_masses_ok
        and fit_residuals_ok
        and np.isfinite(relative_mass_separation)
        and relative_mass_separation >= 0.05
    )
    residual = max(
        energy_mismatch if np.isfinite(energy_mismatch) else float("inf"),
        0.0 if fitted_masses_ok else float("inf"),
        max(0.0, max_fit_residual - FIT_RESID_TOL)
        if np.isfinite(max_fit_residual)
        else float("inf"),
        max(0.0, 0.05 - relative_mass_separation)
        if np.isfinite(relative_mass_separation)
        else float("inf"),
    )
    report(
        "CHECK-04 FINITE-SAME-ENERGY-COMPARATOR",
        ok,
        residual,
        f"L={length} target={target:.12e} relative_mass_separation={relative_mass_separation:.6e} "
        f"max_fit_residual={max_fit_residual:.3e} fit_residual_tolerance={FIT_RESID_TOL:.1e} "
        f"fitted_masses_positive_finite={str(fitted_masses_ok).lower()} rows=["
        + "; ".join(rows)
        + "]",
    )


def main() -> int:
    print("FREE SOURCE-FUNCTION FORMULAS AND FINITE CONTACT COMPARATOR")
    check_conditional_single_formula()
    check_free_composite_formula()
    check_small_parameter_formulas()
    check_finite_same_energy_comparator()
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
