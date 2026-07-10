#!/usr/bin/env python3
"""Check only the free two-step rest-gap and curvature algebra.

The supplied input is
E(p) = asinh(sqrt(m^2 + sum_j sin(p_j)^2)), m > 0.
No physical-species, projection, persistence, source, or audit claim is tested.
"""

from __future__ import annotations

from itertools import product

import numpy as np
import sympy as sp


MASSES = (0.05, 0.1, 0.2, 0.5, 1.0, 2.0)
PASS_COUNT = 0
FAIL_COUNT = 0


def report(name: str, ok: bool, residual: float, detail: str) -> None:
    global PASS_COUNT, FAIL_COUNT
    PASS_COUNT += int(ok)
    FAIL_COUNT += int(not ok)
    print(f"{name}: {'PASS' if ok else 'FAIL'} residual={residual:.3e} {detail}")


def energy(m: float, p: tuple[float, float, float]) -> float:
    return float(np.arcsinh(np.sqrt(m * m + sum(np.sin(x) ** 2 for x in p))))


def inertial_coefficient(m: float) -> float:
    return float(m * np.sqrt(1.0 + m * m))


def check_rest_gap() -> None:
    grid = np.linspace(-np.pi, np.pi, 33)
    worst = 0.0
    for m in MASSES:
        measured = min(energy(m, tuple(float(x) for x in p)) for p in product(grid, repeat=3))
        worst = max(worst, abs(measured - float(np.arcsinh(m))))
    report("CHECK-01 REST-GAP", worst <= 1.0e-12, worst, "grid includes all sin(p_j)=0 corners")


def check_curvature() -> None:
    m, q = sp.symbols("m q", positive=True, real=True)
    expr = sp.asinh(sp.sqrt(m**2 + sp.sin(q) ** 2))
    exact = sp.simplify(sp.diff(expr, q, 2).subs(q, 0))
    target = 1 / (m * sp.sqrt(1 + m**2))
    symbolic_ok = sp.simplify(exact - target) == 0

    worst_numeric = 0.0
    for mass in MASSES:
        target_value = 1.0 / inertial_coefficient(mass)
        estimates = []
        for h in (2.0**-k for k in range(5, 12)):
            coarse = (energy(mass, (0.0, 0.0, h)) - 2.0 * energy(mass, (0.0, 0.0, 0.0))
                      + energy(mass, (0.0, 0.0, -h))) / h**2
            fine_h = h / 2.0
            fine = (energy(mass, (0.0, 0.0, fine_h)) - 2.0 * energy(mass, (0.0, 0.0, 0.0))
                    + energy(mass, (0.0, 0.0, -fine_h))) / fine_h**2
            estimates.append((4.0 * fine - coarse) / 3.0)
        worst_numeric = max(worst_numeric, min(abs(value - target_value) for value in estimates))
    residual = max(worst_numeric, 0.0 if symbolic_ok else 1.0)
    report("CHECK-02 CURVATURE", symbolic_ok and worst_numeric <= 1.0e-7, residual, f"exact={exact}")


def check_hyperbolic_relation() -> None:
    m = sp.symbols("m", positive=True, real=True)
    gap = sp.asinh(m)
    coefficient = m * sp.sqrt(1 + m**2)
    exact_residual = sp.simplify(coefficient - sp.expand_trig(sp.sinh(2 * gap) / 2))
    series = sp.series(coefficient / gap, m, 0, 5)
    coefficient_m2 = sp.expand(series.removeO()).coeff(m, 2)
    symbolic_ok = exact_residual == 0 and coefficient_m2 == sp.Rational(2, 3)

    worst_numeric = 0.0
    for mass in MASSES:
        gap_value = float(np.arcsinh(mass))
        worst_numeric = max(
            worst_numeric,
            abs(inertial_coefficient(mass) - 0.5 * float(np.sinh(2.0 * gap_value))),
        )
    residual = max(worst_numeric, 0.0 if symbolic_ok else 1.0)
    report(
        "CHECK-03 HYPERBOLIC-RELATION",
        symbolic_ok and worst_numeric <= 1.0e-12,
        residual,
        f"exact_residual={exact_residual} series={series}",
    )


def main() -> int:
    print("FREE TWO-STEP REST-GAP AND CURVATURE ALGEBRA")
    check_rest_gap()
    check_curvature()
    check_hyperbolic_relation()
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
