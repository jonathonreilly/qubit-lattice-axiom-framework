#!/usr/bin/env python3
"""Finite test of fixed and macroscopic spectral-lag cancellation.

Unlike the broad all-lag Abel probe, this tests a changed estimate: for selected
fixed and macroscopic lags h it records the unweighted phase-prefix
discrepancy, the actual prepared/character weighted sum, its summation-by-parts
envelope, and the remaining contribution from all untested lags. Float64 data
are diagnostic only; no asymptotic conclusion is inferred.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
from scipy.linalg import eigh_tridiagonal

ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "scripts/postmark_electric_exact_side_fixed_index_kernel_2026_09_24.py"
OUT = Path(__file__).with_name("selected_lag_phase_cancellation_probe.json")
LAGS = (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1536,
        2048, 2560, 3840, 5000)


def load_runner():
    spec = importlib.util.spec_from_file_location("exact_side", RUNNER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def wrap(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


def run(spin: int, radius: int, module):
    lo, hi, diagonal, offdiagonal, _ = module.finite_spin_matrix(spin)
    lam, vectors = eigh_tridiagonal(diagonal, offdiagonal, eigvals_only=False)
    nodes = np.arange(lo, hi + 1, dtype=np.int64)
    C = spin * (spin + 1)
    profile, profile_meta = module.infinite_reference_profile(0.25, radius=radius)
    core = np.fromiter(profile.keys(), dtype=np.int64)
    values = np.fromiter(profile.values(), dtype=np.complex128)
    coeff = vectors[core - lo, :].T @ values
    observable = np.cos(2 * np.pi * np.remainder(nodes, 3) / 3)

    diagonal_v = np.einsum("i,ij,ij->j", observable, vectors, vectors,
                           optimize=False)
    diagonal_term = np.sum(np.abs(coeff) ** 2 * diagonal_v)
    evolved = vectors @ (np.exp(0.25j * C * lam) * coeff)
    q_direct = np.vdot(evolved, observable * evolved)

    rows = []
    selected_sum = 0j
    for h in LAGS:
        if h >= len(lam):
            continue
        v_lag = np.einsum("i,ij,ij->j", observable,
                          vectors[:, :-h], vectors[:, h:], optimize=False)
        if spin <= 8:
            v_dense = vectors.T @ (observable[:, None] * vectors)
            check = float(np.max(np.abs(v_lag - np.diag(v_dense, k=h))))
        else:
            check = None
        weights = np.conjugate(coeff[:-h]) * coeff[h:] * v_lag
        phase = 0.25 * C * (lam[h:] - lam[:-h])
        oscillation = np.exp(1j * phase)
        actual = np.sum(weights * oscillation)
        selected_sum += actual
        phase_prefix = np.cumsum(oscillation)
        scaled_weights = len(lam) * weights
        variation = float(abs(scaled_weights[-1]) +
                          np.sum(np.abs(np.diff(scaled_weights))))
        abel_bound = variation * float(np.max(np.abs(phase_prefix))) / len(lam)
        weighted_prefix = np.cumsum(weights * oscillation)
        phase_increment = wrap(np.diff(phase))
        near = np.abs(phase_increment) < 0.01
        near_weight = (float(np.sum(np.abs(weights[:-1][near])))
                       if len(weights) > 1 else 0.0)
        rows.append({
            "lag": h,
            "pairs": len(weights),
            "phase_prefix_max": float(np.max(np.abs(phase_prefix))),
            "phase_prefix_over_sqrt_pairs": float(
                np.max(np.abs(phase_prefix)) / np.sqrt(len(weights))),
            "weighted_pair_l1": float(np.sum(np.abs(weights))),
            "weighted_sum_abs": float(abs(actual)),
            "weighted_prefix_max_abs": float(np.max(np.abs(weighted_prefix))),
            "scaled_weight_total_variation": variation,
            "abel_bound": abel_bound,
            "near_alias_increment_count_at_0_01": int(np.count_nonzero(near)),
            "near_alias_weight_l1_at_0_01": near_weight,
            "dense_overlap_check_error_when_S_le_8": check,
        })

    low_lag_approx = diagonal_term + 2 * np.real(selected_sum)
    return {
        "S": spin,
        "dimension": len(lam),
        "profile_radius": radius,
        "profile_tail_bound": module.cauchy_profile_tail_bound(0.25, radius),
        "profile_construction": profile_meta["independent_method"],
        "q_real_direct": float(q_direct.real),
        "q_imag_direct": float(q_direct.imag),
        "diagonal_term_real": float(np.real(diagonal_term)),
        "selected_lag_sum_real": float(2 * np.real(selected_sum)),
        "remainder_after_selected_lags_real_diagnostic": float(
            q_direct.real - low_lag_approx),
        "fixed_lags": rows,
        "scope": "finite float64/complex128 profile-scalar diagnostic; no uniform lag bound or asymptotic claim",
    }


def main():
    module = load_runner()
    spins = (8, 96, 192, 384, 512)
    result = {
        "source_revision": "5171af01191cc2db9d5bad0f8eca2185114ebbe3",
        "input_sha256": {
            "exact_side_runner": hashlib.sha256(RUNNER.read_bytes()).hexdigest(),
            "exact_side_note": hashlib.sha256((ROOT / "docs/POSTMARK_ELECTRIC_EXACT_SIDE_FIXED_INDEX_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-24.md").read_bytes()).hexdigest(),
            "five_site_note": hashlib.sha256((ROOT / "docs/POSTMARK_ELECTRIC_FIVE_SITE_INTER_FIBER_PHASE_BOUNDED_THEOREM_NOTE_2026-09-24.md").read_bytes()).hexdigest(),
            "probe": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "lag_phase": "Phi[S,h,j]=C/4*(lambda[j+h]-lambda[j]); lambda are exact finite-spin eigenvalues of N_S",
        "weight": "conj(c[j])*c[j+h]*<phi_j, cos(2*pi*n/3) phi_(j+h)> with c the radius-R limiting prepared profile projected onto the finite eigenbasis",
        "selected_fixed_and_macroscopic_lags": list(LAGS),
        "rows": [run(S, 24, module) for S in spins],
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
