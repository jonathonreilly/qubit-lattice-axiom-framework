#!/usr/bin/env python3
"""Finite exact-weight sensitivity check for approximate spectral phases.

The inequality is exact for each computed finite Jacobi matrix. The reported
sizes and fitted-phase errors are diagnostics, not an asymptotic claim.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path

import numpy as np
from scipy.linalg import eigh_tridiagonal

ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "scripts" / "postmark_electric_exact_side_fixed_index_kernel_2026_09_24.py"
OUT = Path(__file__).with_name("phase_accuracy_gate_probe.json")
Q_ERROR_TARGET = 0.01
SPINS = (96, 192, 384, 512)


def main() -> None:
    spec = importlib.util.spec_from_file_location("exact_side_phase_gate", RUNNER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    rows = []
    for spin in SPINS:
        lo, hi, diagonal, offdiagonal, _positive = module.finite_spin_matrix(spin)
        eigenvalues, eigenvectors = eigh_tridiagonal(
            diagonal, offdiagonal, eigvals_only=False
        )
        profile, _meta = module.infinite_reference_profile(0.25, radius=24)
        nodes = np.arange(lo, hi + 1)
        eta = np.zeros(nodes.size, dtype=np.complex128)
        for n, value in profile.items():
            eta[n - lo] = value
        coefficients = eigenvectors.T @ eta
        character = np.cos(2 * np.pi * np.remainder(nodes, 3) / 3)
        overlap = eigenvectors.T @ (character[:, None] * eigenvectors)
        pair_weights = np.abs(
            np.conjugate(coefficients[:, None])
            * coefficients[None, :]
            * overlap
        )

        casimir = spin * (spin + 1)
        exact_phase = casimir * eigenvalues / 4.0
        index = np.arange(eigenvalues.size, dtype=float)
        scaled_index = index / (eigenvalues.size - 1)
        fit_coefficients = np.linalg.lstsq(
            np.column_stack((scaled_index**2, scaled_index, np.ones_like(index))),
            exact_phase,
            rcond=None,
        )[0]
        fitted_phase = (
            fit_coefficients[0] * scaled_index**2
            + fit_coefficients[1] * scaled_index
            + fit_coefficients[2]
        )
        phase_error = fitted_phase - exact_phase
        phase_difference_error = np.abs(
            phase_error[None, :] - phase_error[:, None]
        )
        exact_weighted_bound = float(
            np.sum(pair_weights * np.minimum(2.0, phase_difference_error))
        )
        pair_weight_l1 = float(np.sum(pair_weights))
        positive_lag_weight = np.array(
            [float(np.sum(np.diag(pair_weights, k=lag)))
             for lag in range(eigenvalues.size)]
        )
        positive_lag_error_bound = np.array(
            [float(np.sum(np.diag(pair_weights, k=lag)
                          * np.minimum(2.0, np.diag(phase_difference_error, k=lag))))
             for lag in range(eigenvalues.size)]
        )
        dimension = eigenvalues.size
        lag_bins = {
            "diagonal": (0, 0),
            "local_1_to_32": (1, min(32, dimension - 1)),
            "mesoscopic_33_to_D_over_4": (33, max(32, dimension // 4)),
            "macroscopic_above_D_over_4": (dimension // 4 + 1, dimension - 1),
        }
        lag_weight_summary = {}
        for name, (first, last) in lag_bins.items():
            if first > last:
                lag_weight_summary[name] = {"pair_weight_l1": 0.0, "pair_error_bound": 0.0}
                continue
            multiplicity = 1 if name == "diagonal" else 2
            lag_weight_summary[name] = {
                "pair_weight_l1": float(multiplicity * np.sum(positive_lag_weight[first:last + 1])),
                "pair_error_bound": float(multiplicity * np.sum(positive_lag_error_bound[first:last + 1])),
            }
        wrapped_error = np.sort(np.remainder(phase_error, 2.0 * np.pi))
        circular_gaps = np.diff(
            np.concatenate((wrapped_error, wrapped_error[:1] + 2.0 * np.pi))
        )
        circular_radius = float(
            (2.0 * np.pi - np.max(circular_gaps)) / 2.0
        )

        coefficient_norm = float(np.linalg.norm(coefficients))
        normalized_spectral_weight = np.abs(coefficients) ** 2 / coefficient_norm**2
        weighted_phase_mean = np.sum(
            normalized_spectral_weight * np.exp(1j * phase_error)
        )
        weighted_state_distance = float(
            coefficient_norm
            * np.sqrt(max(0.0, 2.0 * (1.0 - abs(weighted_phase_mean))))
        )
        character_operator_norm = float(np.max(np.abs(character)))
        cauchy_pair_weight_envelope = float(
            character_operator_norm
            * coefficient_norm
            * np.sum(np.abs(coefficients))
        )
        if pair_weight_l1 > cauchy_pair_weight_envelope + 1e-10:
            raise ArithmeticError("pair-weight Cauchy envelope failed numerically")
        operator_stability_bound = min(
            2.0 * character_operator_norm * coefficient_norm**2,
            2.0
            * character_operator_norm
            * coefficient_norm
            * weighted_state_distance,
        )
        operator_phase_tolerance = Q_ERROR_TARGET / (
            2.0 * character_operator_norm * coefficient_norm**2
        )

        exact_state = eigenvectors @ (np.exp(1j * exact_phase) * coefficients)
        fitted_state = eigenvectors @ (np.exp(1j * fitted_phase) * coefficients)
        exact_q = np.vdot(exact_state, character * exact_state)
        fitted_q = np.vdot(fitted_state, character * fitted_state)
        actual_q_error = float(abs(exact_q - fitted_q))
        if actual_q_error > exact_weighted_bound + 1e-10:
            raise ArithmeticError("pairwise phase-error bound failed numerically")
        if actual_q_error > operator_stability_bound + 1e-10:
            raise ArithmeticError("operator phase-stability bound failed numerically")
        robust_phase_radius = Q_ERROR_TARGET / (2.0 * pair_weight_l1)
        rows.append(
            {
                "S": spin,
                "dimension": int(eigenvalues.size),
                "pair_weight_l1": pair_weight_l1,
                "pair_weight_cauchy_envelope": cauchy_pair_weight_envelope,
                "pair_weight_over_cauchy_envelope": float(
                    pair_weight_l1 / cauchy_pair_weight_envelope
                ),
                "pair_weight_l1_over_sqrt_S": float(pair_weight_l1 / np.sqrt(spin)),
                "prepared_coefficient_l1": float(np.sum(np.abs(coefficients))),
                "prepared_coefficient_l1_over_sqrt_S": float(
                    np.sum(np.abs(coefficients)) / np.sqrt(spin)
                ),
                "lag_pair_weight_and_error_bound": lag_weight_summary,
                "quadratic_fit_optimal_circular_phase_radius_rad": circular_radius,
                "prepared_state_norm": coefficient_norm,
                "prepared_weighted_phase_state_distance": weighted_state_distance,
                "operator_stability_bound": operator_stability_bound,
                "operator_centered_phase_tolerance_for_q_error_0.01": operator_phase_tolerance,
                "operator_centered_eigenvalue_tolerance_for_q_error_0.01": float(
                    4.0 * operator_phase_tolerance / casimir
                ),
                "exact_weighted_phase_error_bound": exact_weighted_bound,
                "actual_q_fit_error": actual_q_error,
                "both_finite_bound_checks_passed": True,
                "q_exact_real": float(exact_q.real),
                "q_fit_real": float(fitted_q.real),
                "uniform_centered_phase_tolerance_for_q_error_0.01": robust_phase_radius,
                "uniform_centered_eigenvalue_tolerance_for_q_error_0.01": float(
                    4.0 * robust_phase_radius / casimir
                ),
                "scope": "finite float64 diagnostic; uniform stability bound is sufficient, not necessary",
            }
        )

    result = {
        "source_revision": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "exact_side_runner_sha256": hashlib.sha256(RUNNER.read_bytes()).hexdigest(),
        "exact_identity": (
            "q(theta)=sum_jk conj(c_j)c_k V_jk exp(i(theta_k-theta_j)); "
            "for phase errors e_j, |q(theta+e)-q(theta)| <= "
            "sum_jk |c_j c_k V_jk| min(2,|e_k-e_j|)"
        ),
        "uniform_sufficient_condition": (
            "if R=min_a max_j |e_j-a|, then |delta q| <= "
            "min(2,2R) sum_jk |c_j c_k V_jk|"
        ),
        "operator_sufficient_condition": (
            "q is invariant under a common phase; after optimizing that phase, "
            "|delta q| <= 2 ||V|| ||c|| min_a ||(diag(exp(i e_j))-exp(i a)I)c||_2"
        ),
        "rows": rows,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
