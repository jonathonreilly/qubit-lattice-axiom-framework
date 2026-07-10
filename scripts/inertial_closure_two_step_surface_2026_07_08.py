#!/usr/bin/env python3
"""Uniform-force transport checks on an unwrapped quasimomentum lift.

All tested packets have finite support inside one Brillouin branch, and every
gated time lies before that support reaches a branch seam. Principal-value
momentum after wrapping is outside this runner's claim.
"""

from __future__ import annotations

from itertools import product

import numpy as np
import sympy as sp


MASSES = (0.5, 1.0, 2.0)
G_VALUES = (1.0e-3, 2.0e-3)
TIMES = (0.0, 10.0, 20.0)
PASS_COUNT = 0
FAIL_COUNT = 0


m_s = sp.symbols("m", positive=True, real=True)
p1_s, p2_s, p3_s = sp.symbols("p1 p2 p3", real=True)
E_s = sp.asinh(sp.sqrt(m_s**2 + sp.sin(p1_s) ** 2 + sp.sin(p2_s) ** 2 + sp.sin(p3_s) ** 2))
E3_s = sp.diff(E_s, p3_s)
E33_s = sp.diff(E_s, p3_s, 2)
H33_s = sp.hessian(E33_s, (p1_s, p2_s, p3_s))
E3 = sp.lambdify((m_s, p1_s, p2_s, p3_s), E3_s, "numpy")
E33 = sp.lambdify((m_s, p1_s, p2_s, p3_s), E33_s, "numpy")
H33 = sp.lambdify((m_s, p1_s, p2_s, p3_s), H33_s, "numpy")


def report(name: str, ok: bool, residual: float, detail: str) -> None:
    global PASS_COUNT, FAIL_COUNT
    PASS_COUNT += int(ok)
    FAIL_COUNT += int(not ok)
    print(f"{name}: {'PASS' if ok else 'FAIL'} residual={residual:.3e} {detail}")


def p_star(mass: float) -> float:
    return float(min(np.pi / 4.0, 0.6 * mass))


def compact_packet(mass: float) -> tuple[np.ndarray, np.ndarray]:
    radius = 0.25 * p_star(mass)
    points = np.array(
        [
            (0.0, 0.0, 0.0),
            (radius, 0.0, 0.0),
            (-radius, 0.0, 0.0),
            (0.0, radius, 0.0),
            (0.0, -radius, 0.0),
            (0.0, 0.0, radius),
            (0.0, 0.0, -radius),
        ],
        dtype=float,
    )
    weights = np.array((0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1), dtype=float)
    return points, weights


def inertial_coefficient(mass: float) -> float:
    return float(mass * np.sqrt(1.0 + mass * mass))


def check_unwrapped_lift_and_pre_wrap() -> None:
    worst_mean = 0.0
    minimum_margin = float("inf")
    for mass in MASSES:
        points, weights = compact_packet(mass)
        initial_mean = np.sum(weights[:, None] * points, axis=0)
        for g in G_VALUES:
            for time in TIMES:
                shifted = points.copy()
                shifted[:, 2] -= g * time
                measured = np.sum(weights[:, None] * shifted, axis=0)
                expected = initial_mean - np.array((0.0, 0.0, g * time))
                worst_mean = max(worst_mean, float(np.max(np.abs(measured - expected))))
                margin = np.pi / 2.0 - float(np.max(np.abs(shifted)))
                minimum_margin = min(minimum_margin, margin)
    ok = worst_mean <= 1.0e-14 and minimum_margin > 0.0
    residual = max(worst_mean, max(0.0, -minimum_margin))
    report(
        "CHECK-01 UNWRAPPED-LIFT/PRE-WRAP",
        ok,
        residual,
        f"minimum_branch_seam_margin={minimum_margin:.6e}",
    )


def check_exact_velocity_acceleration() -> None:
    worst = 0.0
    h = 1.0e-4
    for mass in MASSES:
        points, weights = compact_packet(mass)
        for g in G_VALUES:
            for time in TIMES:
                shifted = points.copy()
                shifted[:, 2] -= g * time
                acceleration = -g * float(np.sum(weights * E33(mass, shifted[:, 0], shifted[:, 1], shifted[:, 2])))
                plus = points.copy()
                minus = points.copy()
                plus[:, 2] -= g * (time + h)
                minus[:, 2] -= g * (time - h)
                v_plus = float(np.sum(weights * E3(mass, plus[:, 0], plus[:, 1], plus[:, 2])))
                v_minus = float(np.sum(weights * E3(mass, minus[:, 0], minus[:, 1], minus[:, 2])))
                finite_difference = (v_plus - v_minus) / (2.0 * h)
                worst = max(worst, abs(finite_difference - acceleration))
    report(
        "CHECK-02 ACCELERATION-IDENTITY",
        worst <= 1.0e-9,
        worst,
        "finite-difference d<velocity>/dt versus -g<E_33>",
    )


def check_rest_derivatives() -> None:
    at_zero = {p1_s: 0, p2_s: 0, p3_s: 0}
    e33_zero = sp.simplify(E33_s.subs(at_zero))
    e3333_zero = sp.simplify(sp.diff(E_s, p3_s, 4).subs(at_zero))
    target_e33 = 1 / (m_s * sp.sqrt(1 + m_s**2))
    target_e3333 = -(3 + 10 * m_s**2 + 4 * m_s**4) / (m_s**3 * (1 + m_s**2) ** sp.Rational(3, 2))
    ok = sp.simplify(e33_zero - target_e33) == 0 and sp.simplify(e3333_zero - target_e3333) == 0
    report(
        "CHECK-03 REST-DERIVATIVES",
        ok,
        0.0 if ok else 1.0,
        f"E33(0)={e33_zero} E3333(0)={e3333_zero}",
    )


def sampled_hessian_sup(mass: float, radius: float) -> float:
    axis = np.linspace(-radius, radius, 7)
    largest = 0.0
    for q in product(axis, repeat=3):
        matrix = np.asarray(H33(mass, *q), dtype=float)
        largest = max(largest, float(np.linalg.norm(matrix, ord=2)))
    return largest


def diagnose_local_curvature_sample() -> None:
    worst_ratio = 0.0
    minimum_pre_wrap_margin = float("inf")
    for mass in MASSES:
        points, weights = compact_packet(mass)
        mi = inertial_coefficient(mass)
        radius = p_star(mass)
        c4 = 0.5 * mi * sampled_hessian_sup(mass, radius)
        sigma2 = float(np.sum(weights * np.sum(points * points, axis=1)))
        for g in G_VALUES:
            for time in TIMES:
                shifted = points.copy()
                shifted[:, 2] -= g * time
                max_norm = float(np.max(np.abs(shifted)))
                minimum_pre_wrap_margin = min(minimum_pre_wrap_margin, radius - max_norm)
                r_value = mi * float(np.sum(weights * E33(mass, shifted[:, 0], shifted[:, 1], shifted[:, 2]))) - 1.0
                bound = c4 * (sigma2 + (g * time) ** 2)
                ratio = abs(r_value) / bound if bound > 0.0 else 0.0
                worst_ratio = max(worst_ratio, ratio)
    print(
        "DIAGNOSTIC-04 SAMPLED-LOCAL-CURVATURE "
        f"worst_abs_r_over_sampled_scale={worst_ratio:.6e} "
        f"minimum_pstar_margin={minimum_pre_wrap_margin:.6e} "
        "sampled_hessian_is_not_a_certified_supremum",
    )


def main() -> int:
    print("UNWRAPPED TWO-STEP QUASIMOMENTUM TRANSPORT")
    check_unwrapped_lift_and_pre_wrap()
    check_exact_velocity_acceleration()
    check_rest_derivatives()
    diagnose_local_curvature_sample()
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
