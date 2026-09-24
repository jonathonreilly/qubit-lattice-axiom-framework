#!/usr/bin/env python3
"""Check the simple-turning-point Airy scaling for the five-site Jacobi family.

Exact symbolic checks fix the Jordan form, the Airy coefficient, and the
first finite-spin edge shift. Finite products test the scaled one-cell limit
and its Airy ODE propagator. They corroborate, but do not prove, the uniform
Taylor and Euler-product estimates in the paired note.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = (
    "docs/POSTMARK_ELECTRIC_FIVE_SITE_TRANSFER_PHASE_EXPANSION_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/POSTMARK_ELECTRIC_REGULAR_BULK_PHASE_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/POSTMARK_ELECTRIC_SIMPLE_BRAGG_CROSSING_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/POSTMARK_ELECTRIC_SIMPLE_TURNING_POINT_AIRY_SCALE_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-24.md",
)
ROOT = Path(__file__).resolve().parent.parent
OUTPUT = (
    ROOT
    / "outputs"
    / "postmark_moving_index_2026_09_24"
    / "SIMPLE_TURNING_POINT_AIRY_SCALE_TRANSFER_RESULTS.json"
)
SOURCE_BASE_REVISION = "0e6ad8285096ed668816f18caaa6fbbfbd9c50e8"

ELL = (0, 1, 0, 1, 1)
RHO = (0, 0, 0, 1, 0)
PI = (-1, 0, 0, 0, 1)
JORDAN = np.array([[1.0, 1.0], [0.0, 1.0]])
P = np.array([[1.0, 0.1], [1.0, -0.1]])
P_INV = np.linalg.inv(P)


def symbolic_turning_checks() -> dict:
    u, a, lam, z = sp.symbols("u a lam z", real=True)
    one_site = sp.Matrix([[2 * z, 1], [-1, 0]])
    frozen_cell = one_site**5
    jordan_change = sp.Matrix(
        [[1, sp.Rational(1, 10)], [1, -sp.Rational(1, 10)]]
    )
    factored_cell = -frozen_cell
    jordan_at_edge = sp.simplify(
        jordan_change.inv() * factored_cell.subs(z, -1) * jordan_change
    )
    if jordan_at_edge != sp.Matrix([[1, 1], [0, 1]]):
        raise ArithmeticError(("parabolic Jordan form", jordan_at_edge))

    z_u = 1 - lam / (2 * (1 - u**2))
    t5 = 16 * z**5 - 20 * z**3 + 5 * z
    principal_trace = 2 * t5.subs(z, z_u)
    lam_at_a = 4 * (1 - a**2)
    trace_slope = sp.factor(
        sp.diff(-principal_trace, u).subs(u, a).subs(lam, lam_at_a)
    )
    airy_coefficient = 800 * a / lam_at_a
    slope_residual = sp.simplify(trace_slope - airy_coefficient)
    jordan_slope = sp.factor(
        (
            jordan_change.inv()
            * sp.diff(-one_site**5, z)
            * sp.diff(z_u, u)
            * jordan_change
        )[1, 0]
        .subs(z, -1)
        .subs(u, a)
        .subs(lam, lam_at_a)
    )
    jordan_residual = sp.simplify(jordan_slope - airy_coefficient)
    if slope_residual != 0 or jordan_residual != 0:
        raise ArithmeticError(
            ("Airy coefficient", slope_residual, jordan_residual)
        )
    wrong_factor_residual = sp.simplify(
        trace_slope - 400 * a / lam_at_a
    )
    if wrong_factor_residual == 0:
        raise ArithmeticError("factor-of-two Airy coefficient mutation escaped")

    g1 = u * (5 * u * z - 5 * u - 9 * z + 8) / (1 - u**2)
    g1_edge = sp.simplify(g1.subs(z, -1))
    trace_factored_first_order = 10 * g1_edge
    edge_shift = sp.simplify(-trace_factored_first_order / trace_slope)
    expected_shift = sp.simplify(
        -lam_at_a * g1_edge.subs(u, a) / (80 * a)
    )
    shift_residual = sp.simplify(
        (edge_shift - expected_shift).subs(u, a).subs(lam, lam_at_a)
    )
    if shift_residual != 0:
        raise ArithmeticError(
            ("finite-spin edge shift", shift_residual)
        )
    return {
        "factored_cell_at_edge_in_jordan_basis": str(jordan_at_edge),
        "trace_slope_residual": str(slope_residual),
        "jordan_lower_left_slope_residual": str(jordan_residual),
        "airy_coefficient": "800*a/lambda",
        "factor_of_two_mutation_residual": str(wrong_factor_residual),
        "g1_at_edge": str(g1_edge),
        "first_finite_spin_edge_shift": "-lambda*g1(a,-1)/(80*a)",
        "edge_shift_residual": str(shift_residual),
    }


def f(m: int) -> int:
    return m * (m + 1)


def exact_r(S: int, h: int, offset: int) -> float:
    return 1.0 - f(h + offset) / (S * (S + 1))


def frozen_r(u: float, epsilon: float, offset: int) -> float:
    return 1.0 - ((u + offset * epsilon) * (u + (offset + 1) * epsilon)) / (
        1.0 + epsilon
    )


def frozen_cell_transfer(u: float, epsilon: float, lam: float) -> np.ndarray:
    product = np.eye(2, dtype=np.float64)
    for s in range(5):
        left = frozen_r(u, epsilon, ELL[s])
        right = frozen_r(u, epsilon, RHO[s])
        previous = frozen_r(u, epsilon, PI[s])
        offdiag = -math.sqrt(left * right)
        diagonal = left + previous
        transfer = np.array(
            [[(lam - diagonal) / offdiag, -1.0 / offdiag], [offdiag, 0.0]],
            dtype=np.float64,
        )
        product = transfer @ product
    return product


def exact_site_transfer(S: int, h: int, s: int, lam: float) -> np.ndarray:
    left = exact_r(S, h, ELL[s])
    right = exact_r(S, h, RHO[s])
    previous = exact_r(S, h, PI[s])
    offdiag = -math.sqrt(left * right)
    diagonal = left + previous
    return np.array(
        [[(lam - diagonal) / offdiag, -1.0 / offdiag], [offdiag, 0.0]],
        dtype=np.float64,
    )


def exact_cell_transfer(S: int, h: int, lam: float) -> np.ndarray:
    product = np.eye(2, dtype=np.float64)
    for residue in range(5):
        product = exact_site_transfer(S, h, residue, lam) @ product
    return product


def scaled_cell(S: int, h: int, lam: float) -> tuple[np.ndarray, float]:
    a = math.sqrt(1.0 - lam / 4.0)
    w_edge = 1.0 - a * a
    d_edge = np.diag((1.0, w_edge))
    cell = exact_cell_transfer(S, h, lam)
    jordan_cell = -P_INV @ np.linalg.inv(d_edge) @ cell @ d_edge @ P
    q_scale = np.diag((1.0, S ** (1.0 / 3.0)))
    q_scale_inv = np.diag((1.0, S ** (-1.0 / 3.0)))
    return q_scale @ jordan_cell @ q_scale_inv, a


def airy_generator(tau: float, coefficient: float) -> np.ndarray:
    return np.array([[0.0, 1.0], [coefficient * tau, 0.0]], dtype=np.float64)


def rk4_fundamental(
    tau0: float, tau1: float, coefficient: float, steps: int = 12000
) -> np.ndarray:
    if tau1 == tau0:
        return np.eye(2)
    step = (tau1 - tau0) / steps
    state = np.eye(2, dtype=np.float64)
    tau = tau0
    for _ in range(steps):
        a0 = airy_generator(tau, coefficient)
        k1 = a0 @ state
        a1 = airy_generator(tau + step / 2.0, coefficient)
        k2 = a1 @ (state + step * k1 / 2.0)
        k3 = a1 @ (state + step * k2 / 2.0)
        a2 = airy_generator(tau + step, coefficient)
        k4 = a2 @ (state + step * k3)
        state = state + step * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        tau += step
    return state


def finite_scaling_checks() -> dict:
    one_step_rows = []
    product_rows = []
    edge_shift_rows = []
    max_det_error = 0.0
    energy_values = (1.6, 2.4, 3.2)
    spins = (10000, 40000, 160000, 640000)
    sample_tau = (-1.0, -0.5, 0.0, 0.5, 1.0)

    for lam in energy_values:
        a = math.sqrt(1.0 - lam / 4.0)
        coefficient = 800.0 * a / lam
        g1_edge = a * (17.0 - 10.0 * a) / (1.0 - a * a)
        predicted_edge_shift = -lam * g1_edge / (80.0 * a)
        for S in spins:
            delta = S ** (-1.0 / 3.0)
            one_step_error = 0.0
            for tau_target in sample_tau:
                h = round(S * a + tau_target * S ** (1.0 / 3.0))
                tau = (h - S * a) / S ** (1.0 / 3.0)
                step, _ = scaled_cell(S, h, lam)
                max_det_error = max(
                    max_det_error,
                    abs(float(np.linalg.det(step)) - 1.0),
                )
                target = np.eye(2) + delta * airy_generator(tau, coefficient)
                one_step_error = max(
                    one_step_error,
                    float(np.linalg.norm(step - target, ord=np.inf)),
                )
            one_step_rows.append(
                {
                    "lambda": lam,
                    "S": S,
                    "max_euler_step_error": one_step_error,
                    "error_over_step_squared": one_step_error / delta**2,
                }
            )

            R = 0.35
            h0 = math.ceil(S * a - R * S ** (1.0 / 3.0))
            h1 = math.floor(S * a + R * S ** (1.0 / 3.0))
            tau0 = (h0 - S * a) / S ** (1.0 / 3.0)
            tau1 = (h1 - S * a) / S ** (1.0 / 3.0)
            product = np.eye(2)
            for h in range(h0, h1):
                step, _ = scaled_cell(S, h, lam)
                product = step @ product
            airy = rk4_fundamental(tau0, tau1, coefficient)
            error = float(np.linalg.norm(product - airy, ord=np.inf))
            product_rows.append(
                {"lambda": lam, "S": S, "R": R, "propagator_error": error}
            )

            if S >= 960:
                epsilon = 1.0 / S
                left, right = a - 4.0 * epsilon, a + 4.0 * epsilon

                def edge_function(u: float) -> float:
                    return float(np.trace(-frozen_cell_transfer(u, epsilon, lam))) - 2.0

                f_left, f_right = edge_function(left), edge_function(right)
                if not f_left < 0.0 < f_right:
                    raise ArithmeticError(
                        ("frozen edge root is not bracketed", lam, S, f_left, f_right)
                    )
                for _ in range(64):
                    mid = (left + right) / 2.0
                    if edge_function(mid) > 0.0:
                        right = mid
                    else:
                        left = mid
                edge_root = (left + right) / 2.0
                edge_shift_rows.append(
                    {
                        "lambda": lam,
                        "S": S,
                        "S_times_shift": S * (edge_root - a),
                        "predicted_limit": predicted_edge_shift,
                        "absolute_error": abs(
                            S * (edge_root - a) - predicted_edge_shift
                        ),
                    }
                )

    for lam in energy_values:
        a = math.sqrt(1.0 - lam / 4.0)
        h = round(4096 * a)
        matrix = exact_cell_transfer(4096, h, lam)
        if not np.isfinite(matrix).all():
            raise ArithmeticError(("non-finite exact transfer", lam))
        if abs(np.linalg.det(matrix) - 1.0) > 2e-12:
            raise ArithmeticError(("cell determinant", lam, np.linalg.det(matrix)))

    final_by_energy = {}
    for lam in energy_values:
        rows = [row for row in product_rows if row["lambda"] == lam]
        max_scaled_propagator_error = max(
            row["propagator_error"] / row["S"] ** (-1.0 / 3.0)
            for row in rows
        )
        if max_scaled_propagator_error > 200.0:
            raise ArithmeticError(
                ("Airy propagator error envelope", lam, max_scaled_propagator_error)
            )
        shifts = [row for row in edge_shift_rows if row["lambda"] == lam]
        if shifts[-1]["absolute_error"] >= shifts[0]["absolute_error"]:
            raise ArithmeticError(("frozen edge shift convergence", lam, shifts))
        final_by_energy[str(lam)] = {
            "maximum_error_over_S_minus_one_third": max_scaled_propagator_error,
            "first_edge_shift_error": shifts[0]["absolute_error"],
            "last_edge_shift_error": shifts[-1]["absolute_error"],
        }
    if max(row["error_over_step_squared"] for row in one_step_rows) > 3000.0:
        raise ArithmeticError(("one-step Airy expansion", one_step_rows))
    if max_det_error > 2e-10:
        raise ArithmeticError(("scaled determinant", max_det_error))

    return {
        "energies": list(energy_values),
        "spins": list(spins),
        "tau_samples": list(sample_tau),
        "one_step_rows": one_step_rows,
        "propagator_rows": product_rows,
        "frozen_edge_shift_rows": edge_shift_rows,
        "propagator_error_decreases_by_energy": final_by_energy,
        "max_scaled_cell_determinant_error": max_det_error,
        "finite_products_are_diagnostics_only": True,
    }


def main() -> None:
    input_hashes = {}
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        input_hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result = {
        "claim_id": (
            "postmark_electric_simple_turning_point_airy_scale_transfer_2026_09_24"
        ),
        "source_base_revision": SOURCE_BASE_REVISION,
        "runner_sha256": source_hash,
        "input_sha256": input_hashes,
        "read_inventory": {
            "external_scientific_inputs": [],
            "package_integrity_reads": [
                "this runner for its source SHA-256",
                *AUDIT_INPUT_PATHS,
            ],
            "description": (
                "The calculation uses only the exact coefficients and equations "
                "defined in the paired note and its linked transfer notes."
            ),
        },
        "symbolic_checks": symbolic_turning_checks(),
        "finite_checks": finite_scaling_checks(),
        "scope": {
            "proved_by_note": [
                "the parabolic Jordan coefficient and Airy-scale cell limit",
                "the fixed-R inner product convergence to q''=b*tau*q",
                "the match of the inner oscillatory modes to the adjacent "
                "principal-cell basis",
            ],
            "not_proved_by_runner": [
                "uniform analytic remainders",
                "outer WKB error bounds",
                "endpoint conditions, eigenvalue quantization, or prepared readout",
            ],
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
