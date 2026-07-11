#!/usr/bin/env python3
"""Exact endpoint-kernel and affine-remainder theorem checks.

This runner has no physical boundary values, target Yukawa value, fitted
profile, or profile-family search. It checks the load-bearing mathematics for
the scalar transport class

    y' = c y (-d y^2 + G(s) + e q(s)),   c,d,e > 0.

The physical identification of this scalar equation with an interacting
lattice bridge is deliberately outside the claim checked here.
"""

from __future__ import annotations

import sys
from math import exp, sqrt

import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp


PASS = 0
FAIL = 0


def check(tag: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"[{status}] {tag}: {detail}")


def affine_projection(function, left: float, right: float) -> tuple[float, float]:
    """Return slope/intercept of the continuous L2 affine projection."""
    g11 = (right**3 - left**3) / 3.0
    g12 = (right**2 - left**2) / 2.0
    g22 = right - left
    rhs = np.array(
        [
            quad(lambda s: s * function(s), left, right, epsabs=1e-13)[0],
            quad(function, left, right, epsabs=1e-13)[0],
        ]
    )
    return tuple(np.linalg.solve(np.array([[g11, g12], [g12, g22]]), rhs))


def main() -> int:
    print("Exact endpoint-kernel and affine-remainder theorem")
    print("No physical constants or target values are proof inputs.\n")

    # Symbolic derivation for the nonlinear scalar transport class.
    c, d, e, y = sp.symbols("c d e y", positive=True, finite=True)
    gauge, q = sp.symbols("G q", nonnegative=True, finite=True)
    flow = c * y * (-d * y**2 + gauge + e * q)
    flow_y = sp.diff(flow, y)
    flow_q = sp.diff(flow, q)

    # For K(s)=F_q(s) exp(int_s^T F_y du), total differentiation along
    # y'=F gives d(log K)/ds = d(log F_q)/ds - F_y.
    log_kernel_prime = sp.simplify(sp.diff(sp.log(flow_q), y) * flow - flow_y)
    expected_log_kernel_prime = 2 * c * d * y**2
    check(
        "symbolic-first-log-derivative",
        sp.simplify(log_kernel_prime - expected_log_kernel_prime) == 0,
        f"K'/K = {log_kernel_prime}",
    )

    kernel_second_ratio = sp.simplify(
        sp.diff(log_kernel_prime, y) * flow + log_kernel_prime**2
    )
    expected_second_ratio = 4 * c**2 * d * y**2 * (gauge + e * q)
    check(
        "symbolic-second-derivative",
        sp.simplify(kernel_second_ratio - expected_second_ratio) == 0,
        f"K''/K = {kernel_second_ratio}",
    )
    check(
        "positive-monotone-convex-signs",
        flow_q.is_positive
        and expected_log_kernel_prime.is_positive
        and expected_second_ratio.is_nonnegative,
        "F_q>0, K'/K>0, and K''/K>=0 for c,d,e,y>0 and G,q>=0",
    )
    check(
        "zero-source-convexity-boundary",
        sp.simplify(expected_second_ratio.subs({gauge: 0, q: 0})) == 0,
        "G=q=0 gives K''=0 without violating convexity",
    )

    # Nonlinear cubic source-map check: compare the variational derivative to
    # central finite differences and verify a quadratic Frechet remainder.
    toy_c, toy_d, toy_e = 0.13, 0.8, 1.2
    toy_terminal, toy_y0 = 1.1, 0.7

    def toy_gauge(s: float) -> float:
        return 0.4 + 0.05 * s

    def toy_source(s: float) -> float:
        return 0.3 + 0.02 * np.cos(s)

    def toy_direction(s: float) -> float:
        return 1.0 + s

    def toy_flow(s: float, y_value: float, q_value: float) -> float:
        return toy_c * y_value * (
            -toy_d * y_value**2 + toy_gauge(s) + toy_e * q_value
        )

    variational_solution = solve_ivp(
        lambda s, state: [
            toy_flow(s, state[0], toy_source(s)),
            toy_c
            * (-3.0 * toy_d * state[0] ** 2 + toy_gauge(s) + toy_e * toy_source(s))
            * state[1]
            + toy_c * toy_e * state[0] * toy_direction(s),
        ],
        (0.0, toy_terminal),
        [toy_y0, 0.0],
        rtol=2e-12,
        atol=2e-14,
        max_step=0.01,
    )
    if not variational_solution.success:
        raise RuntimeError(variational_solution.message)
    toy_base_endpoint = float(variational_solution.y[0, -1])
    toy_derivative = float(variational_solution.y[1, -1])

    def toy_endpoint(epsilon_value: float) -> float:
        solution_ivp = solve_ivp(
            lambda s, state: [
                toy_flow(
                    s,
                    state[0],
                    toy_source(s) + epsilon_value * toy_direction(s),
                )
            ],
            (0.0, toy_terminal),
            [toy_y0],
            rtol=2e-12,
            atol=2e-14,
            max_step=0.01,
        )
        if not solution_ivp.success:
            raise RuntimeError(solution_ivp.message)
        return float(solution_ivp.y[0, -1])

    toy_epsilon = 1.0e-3
    toy_central_difference = (
        toy_endpoint(toy_epsilon) - toy_endpoint(-toy_epsilon)
    ) / (2.0 * toy_epsilon)
    toy_relative_error = abs(toy_central_difference - toy_derivative) / abs(
        toy_derivative
    )
    remainder_large = abs(
        toy_endpoint(toy_epsilon)
        - toy_base_endpoint
        - toy_epsilon * toy_derivative
    )
    remainder_small = abs(
        toy_endpoint(toy_epsilon / 2.0)
        - toy_base_endpoint
        - (toy_epsilon / 2.0) * toy_derivative
    )
    remainder_ratio = remainder_large / remainder_small
    check(
        "nonlinear-cubic-frechet-derivative",
        toy_relative_error < 1e-7,
        f"central-difference relative error={toy_relative_error:.3e}",
    )
    check(
        "nonlinear-cubic-quadratic-remainder",
        3.8 < remainder_ratio < 4.2,
        f"remainder ratio under epsilon halving={remainder_ratio:.6f}",
    )

    # Exact affine-projection and interpolation-remainder algebra.
    x, h = sp.symbols("x h", real=True, positive=True)
    chord_square_integral = sp.integrate(x**2 * (h - x) ** 2, (x, 0, h))
    check(
        "sharp-chord-integral",
        sp.simplify(chord_square_integral - h**5 / 30) == 0,
        "integral_0^h x^2(h-x)^2 dx = h^5/30",
    )

    # Independent exact example: project x^2 onto span{1,x} on [0,1].
    slope, intercept = sp.symbols("slope intercept")
    residual = x**2 - slope * x - intercept
    solution = sp.solve(
        [sp.integrate(residual, (x, 0, 1)), sp.integrate(x * residual, (x, 0, 1))],
        (slope, intercept),
        dict=True,
    )[0]
    residual = sp.expand(residual.subs(solution))
    residual_norm_sq = sp.integrate(residual**2, (x, 0, 1))
    check(
        "exact-l2-projection-example",
        solution[slope] == 1
        and solution[intercept] == -sp.Rational(1, 6)
        and residual_norm_sq == sp.Rational(1, 180),
        f"Pi_1[x^2]=x-1/6 and ||x^2-Pi_1[x^2]||_2^2={residual_norm_sq}",
    )
    check(
        "projection-orthogonality-example",
        sp.integrate(residual, (x, 0, 1)) == 0
        and sp.integrate(x * residual, (x, 0, 1)) == 0,
        "residual is orthogonal to both affine basis functions",
    )
    check(
        "curvature-bound-example",
        residual_norm_sq <= sp.Rational(1, 30),
        "||R||_2 <= ||K''||_infinity/sqrt(120) for K=x^2 on [0,1]",
    )

    # A finite-difference falsifier for the adjoint sign.  This is a
    # dimensionless linear transport example, not a physical calibration.
    a = 0.7
    source = 1.3
    terminal = 1.1

    def profile(s: float) -> float:
        return 1.0 + s

    def endpoint(epsilon: float) -> float:
        solution_ivp = solve_ivp(
            lambda s, z: [a * z[0] + source * epsilon * profile(s)],
            (0.0, terminal),
            [0.4],
            rtol=2e-12,
            atol=2e-14,
            max_step=0.01,
        )
        if not solution_ivp.success:
            raise RuntimeError(solution_ivp.message)
        return float(solution_ivp.y[0, -1])

    epsilon = 1e-5
    finite_difference = (endpoint(epsilon) - endpoint(-epsilon)) / (2 * epsilon)
    correct_adjoint = quad(
        lambda s: source * exp(a * (terminal - s)) * profile(s),
        0.0,
        terminal,
        epsabs=1e-13,
    )[0]
    wrong_sign_adjoint = quad(
        lambda s: source * exp(-a * (terminal - s)) * profile(s),
        0.0,
        terminal,
        epsabs=1e-13,
    )[0]
    correct_relative_error = abs(correct_adjoint - finite_difference) / abs(finite_difference)
    wrong_relative_error = abs(wrong_sign_adjoint - finite_difference) / abs(finite_difference)
    check(
        "positive-adjoint-sign-finite-difference",
        correct_relative_error < 1e-8,
        f"relative error={correct_relative_error:.3e}",
    )
    check(
        "negative-control-wrong-adjoint-sign",
        wrong_relative_error > 0.1,
        f"wrong-sign relative error={wrong_relative_error:.3e}",
    )

    # Continuous L2 projection, operator-norm witness, and curvature bound on
    # the same independent exponential kernel.
    kernel = lambda s: source * exp(a * (terminal - s))
    proj_slope, proj_intercept = affine_projection(kernel, 0.0, terminal)
    remainder = lambda s: kernel(s) - (proj_slope * s + proj_intercept)
    moment_0 = quad(remainder, 0.0, terminal, epsabs=1e-13)[0]
    moment_1 = quad(lambda s: s * remainder(s), 0.0, terminal, epsabs=1e-13)[0]
    remainder_norm = sqrt(quad(lambda s: remainder(s) ** 2, 0.0, terminal)[0])
    witness_action = quad(
        lambda s: remainder(s) * remainder(s) / remainder_norm,
        0.0,
        terminal,
    )[0]
    curvature_sup = a**2 * kernel(0.0)
    curvature_bound = curvature_sup * terminal ** 2.5 / sqrt(120.0)
    check(
        "continuous-projection-orthogonality",
        abs(moment_0) < 1e-11 and abs(moment_1) < 1e-11,
        f"moments=({moment_0:.3e}, {moment_1:.3e})",
    )
    check(
        "riesz-operator-norm-witness",
        abs(witness_action - remainder_norm) < 1e-11,
        f"witness action={witness_action:.12e}, ||R||_2={remainder_norm:.12e}",
    )
    check(
        "affine-curvature-remainder-bound",
        remainder_norm <= curvature_bound,
        f"||R||_2={remainder_norm:.6e} <= {curvature_bound:.6e}",
    )

    # Coordinate-density check.  For s=h(1-x), the endpoint kernel density
    # with respect to dx is h K(s(x)); omitting h changes the functional.
    response_s = quad(lambda s: kernel(s) * profile(s), 0.0, terminal)[0]
    response_x = quad(
        lambda x_value: terminal
        * kernel(terminal * (1.0 - x_value))
        * profile(terminal * (1.0 - x_value)),
        0.0,
        1.0,
    )[0]
    response_x_missing_jacobian = response_x / terminal
    check(
        "coordinate-kernel-jacobian",
        abs(response_s - response_x) < 1e-11,
        f"ds response={response_s:.12e}, dx response={response_x:.12e}",
    )
    check(
        "negative-control-missing-jacobian",
        abs(response_x_missing_jacobian - response_s) > 0.05 * abs(response_s),
        "omitting ds/dx changes the endpoint functional",
    )

    print(f"\nFINAL TALLY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
