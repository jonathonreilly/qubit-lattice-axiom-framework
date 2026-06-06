#!/usr/bin/env python3
"""
Executable repair for the first-sector rank-one/factorized-class boundary.

The archived source note named this runner, but the file was absent.  This
version rebuilds the load-bearing checks from current one-hop helpers:

1. construct the completed first-sector vector v_min and sample triple Z_min;
2. construct the positive rank-one transfer T_min with T_min^3 e_0 = v_min;
3. pull T_min back through the Wilson half-slice multiplier M = exp(3 J);
4. prove the unique pullback D_back is not diagonal, so T_min is not itself in
   the diagonal factorized-class subfamily T = M D M;
5. reproduce the positive conjugation-symmetric diagonal-family residual.

It does not retag the audited row.  It restores the missing executable support
needed for re-audit.
"""

from __future__ import annotations

import sys

import numpy as np
from scipy.optimize import minimize

from frontier_gauge_vacuum_plaquette_first_sector_rank_one_transfer_realization_2026_04_19 import (
    completed_sector_data,
    rank_one_transfer_for_vector,
)
from frontier_gauge_vacuum_plaquette_first_three_sample_environment_evaluator_route_2026_04_17 import (
    sample_angle_units,
)
from frontier_gauge_vacuum_plaquette_retained_class_sampling_inversion_2026_04_17 import (
    evaluation_matrix,
)
from frontier_gauge_vacuum_plaquette_spatial_environment_character_measure import (
    BETA,
    build_recurrence_matrix,
    conjugation_swap_matrix,
    matrix_exponential_symmetric,
)


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


def sample_matrix_for(weights: list[tuple[int, int]]) -> np.ndarray:
    angles = [(u1 * np.pi / 16.0, u2 * np.pi / 16.0) for u1, u2 in sample_angle_units().values()]
    return evaluation_matrix(weights, angles)


def diagonal_family_search(
    multiplier: np.ndarray,
    sample_matrix: np.ndarray,
    target_vector: np.ndarray,
    target_samples: np.ndarray,
) -> dict[str, object]:
    e0 = np.zeros(len(target_vector), dtype=float)
    e0[0] = 1.0

    def propagate(params: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        d00, d10, d11 = params
        diag = np.diag([d00, d10, d10, d11])
        transfer = multiplier @ diag @ multiplier
        vector = np.linalg.matrix_power(transfer, 3) @ e0
        samples = np.real_if_close(sample_matrix @ vector).real
        return vector, samples

    def objective(log_params: np.ndarray) -> float:
        vector, _samples = propagate(np.exp(log_params))
        delta = vector - target_vector
        return float(np.dot(delta, delta))

    starts = [
        (0.255192351889, 8.06e-12, 2.05e-11),
        (0.25519235, 1.0e-10, 1.0e-10),
        (0.35, 1.0e-18, 1.0e-18),
        (0.10, 0.01, 0.01),
        (0.50, 0.02, 1.0e-4),
        (1.0e-3, 1.0e-3, 1.0e-3),
    ]
    best = None
    for start in starts:
        result = minimize(
            objective,
            np.log(np.maximum(np.asarray(start, dtype=float), 1.0e-18)),
            method="L-BFGS-B",
            bounds=[(-40.0, 5.0), (-40.0, 5.0), (-40.0, 5.0)],
            options={"maxiter": 1000, "ftol": 1.0e-15, "gtol": 1.0e-12},
        )
        if best is None or float(result.fun) < float(best.fun):
            best = result

    assert best is not None
    params = np.exp(best.x)
    vector, samples = propagate(params)
    vector_gap = float(np.linalg.norm(vector - target_vector))
    sample_gap = float(np.linalg.norm(samples - target_samples))
    return {
        "params": params,
        "vector": vector,
        "samples": samples,
        "vector_gap": vector_gap,
        "sample_gap": sample_gap,
        "objective": float(best.fun),
        "success": bool(best.success),
        "message": str(best.message),
    }


def main() -> int:
    print("=" * 112)
    print("GAUGE-VACUUM PLAQUETTE FIRST-SECTOR RANK-ONE FACTORIZED-CLASS BOUNDARY")
    print("=" * 112)
    print()
    print("Question:")
    print("  Does the exact positive rank-one realization of Z_min also come from the")
    print("  diagonal Wilson factorized-class subfamily T = exp(3J) D exp(3J)?")

    v_min_old_order, z_min = completed_sector_data()
    jmat, weights, index = build_recurrence_matrix(1)
    retained_order = [(0, 0), (1, 0), (0, 1), (1, 1)]
    old_index = {w: i for i, w in enumerate(retained_order)}
    v_min = np.array([v_min_old_order[old_index[w]] for w in weights], dtype=float)

    multiplier = matrix_exponential_symmetric(jmat, BETA / 2.0)
    sample_mat = sample_matrix_for(weights)
    z_eval = np.real_if_close(sample_mat @ v_min).real

    t_min = rank_one_transfer_for_vector(v_min)
    e0 = np.zeros(len(v_min), dtype=float)
    e0[0] = 1.0
    propagated = np.linalg.matrix_power(t_min, 3) @ e0

    d_back = np.linalg.solve(multiplier, np.linalg.solve(multiplier, t_min).T).T
    reconstruction = multiplier @ d_back @ multiplier
    offdiag = d_back - np.diag(np.diag(d_back))
    offdiag_frob = float(np.linalg.norm(offdiag))
    offdiag_op = float(np.linalg.norm(offdiag, 2))
    diag_vals = np.diag(d_back)
    swap = conjugation_swap_matrix(weights, index)

    search = diagonal_family_search(multiplier, sample_mat, v_min, z_min)
    best_params = np.asarray(search["params"], dtype=float)
    best_vector = np.asarray(search["vector"], dtype=float)
    best_samples = np.asarray(search["samples"], dtype=float)

    z_gap = float(np.linalg.norm(z_eval - z_min))
    prop_gap = float(np.linalg.norm(propagated - v_min))
    recon_gap = float(np.linalg.norm(reconstruction - t_min))
    multiplier_det = float(np.linalg.det(multiplier))
    dback_swap_gap = float(np.linalg.norm(swap @ d_back - d_back @ swap))
    dback_sym_gap = float(np.linalg.norm(d_back - d_back.T))

    print()
    print(f"  recurrence weights                         = {weights}")
    print(f"  v_min                                      = {np.round(v_min, 12).tolist()}")
    print(f"  Z_min                                      = {np.round(z_min, 12).tolist()}")
    print(f"  E_3 v_min                                  = {np.round(z_eval, 12).tolist()}")
    print(f"  det(exp(3J))                               = {multiplier_det:.12e}")
    print(f"  diag(D_back)                               = {np.round(diag_vals, 12).tolist()}")
    print(f"  ||offdiag(D_back)||_F / ||.||_2            = {offdiag_frob:.12f} / {offdiag_op:.12f}")
    print(f"  D_back symmetry / conjugation gaps         = {dback_sym_gap:.3e} / {dback_swap_gap:.3e}")
    print(f"  best positive diagonal params              = {np.round(best_params, 12).tolist()}")
    print(f"  best diagonal vector                       = {np.round(best_vector, 12).tolist()}")
    print(f"  best diagonal samples                      = {np.round(best_samples, 12).tolist()}")
    print(f"  best vector/sample residuals               = {search['vector_gap']:.12f} / {search['sample_gap']:.12f}")
    print()

    check(
        "The completed four-weight vector evaluates to the current completed sample triple Z_min",
        z_gap < 1.0e-12,
        f"||E_3 v_min - Z_min||={z_gap:.3e}",
    )
    check(
        "The explicit positive rank-one transfer T_min propagates e_0 to v_min at depth three",
        prop_gap < 1.0e-12 and float(np.min(np.linalg.eigvalsh(t_min))) > -1.0e-12,
        f"||T_min^3 e_0-v_min||={prop_gap:.3e}",
    )
    check(
        "The Wilson half-slice multiplier is invertible, so D_back = M^-1 T_min M^-1 is the unique pullback",
        abs(multiplier_det) > 1.0e-6 and recon_gap < 1.0e-12,
        f"(detM,recon_gap)=({multiplier_det:.3e},{recon_gap:.3e})",
    )
    check(
        "The unique pullback is self-adjoint and conjugation-symmetric but not diagonal",
        dback_sym_gap < 1.0e-12
        and dback_swap_gap < 1.0e-12
        and offdiag_frob > 0.20
        and abs(offdiag_frob - 0.250338180104) < 5.0e-10,
        f"offdiag_frob={offdiag_frob:.12f}",
    )
    check(
        "The positive conjugation-symmetric diagonal-family search reproduces the archived boundary residual for v_min",
        float(search["vector_gap"]) > 0.13
        and float(search["vector_gap"]) < 0.14
        and abs(float(best_params[0]) - 0.25519235) < 1.0e-6
        and best_params[1] >= 0.0
        and best_params[2] >= 0.0,
        f"best=({best_params[0]:.12e},{best_params[1]:.12e},{best_params[2]:.12e}), gap={search['vector_gap']:.12f}",
    )
    check(
        "The same best diagonal family point still misses the three-sample target, so the boundary is executable",
        float(search["sample_gap"]) > 0.22 and float(search["sample_gap"]) < 0.24,
        f"sample_gap={search['sample_gap']:.12f}",
    )

    print("\n" + "=" * 112)
    print("RESULT")
    print("=" * 112)
    print("  Executable boundary restored:")
    print("    - T_min is an exact positive rank-one transfer realization of Z_min")
    print("    - the unique Wilson half-slice pullback of T_min is not diagonal")
    print("    - therefore that rank-one realization is not in the diagonal")
    print("      factorized-class subfamily T = exp(3J) D exp(3J)")
    print("    - the historical positive diagonal search residual is reproduced")
    print("    - this runner restores the missing executable artifact for re-audit")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
