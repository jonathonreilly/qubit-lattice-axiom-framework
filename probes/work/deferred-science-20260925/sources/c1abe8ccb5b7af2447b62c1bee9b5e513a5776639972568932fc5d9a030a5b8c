#!/usr/bin/env python3
"""Exploratory finite-spin test of the exact weighted lag/alias criterion.

This computes the finite-core scalar q_{S,R}, its actual lag contributions,
the Abel total-variation bound, and the weight carried by near-alias increments.
All values use float64/complex128 eigensolvers and are diagnostics only; they
do not enclose an asymptotic limit or a theorem.
"""
from __future__ import annotations

import importlib.util
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.linalg import eigh_tridiagonal

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "scripts" / "postmark_electric_exact_side_fixed_index_kernel_2026_09_24.py"
OUT = Path(__file__).with_name("WEIGHTED_ALIAS_DIAGNOSTIC.json")


def load_runner():
    spec = importlib.util.spec_from_file_location("exact_side", RUNNER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def wrap(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


def run(spin: int, core_radius: int, module):
    lo, hi, diag, offdiag, _ = module.finite_spin_matrix(spin)
    lam, vectors = eigh_tridiagonal(diag, offdiag, eigvals_only=False)
    profile, profile_info = module.infinite_reference_profile(0.25, radius=core_radius)
    nodes = np.arange(lo, hi + 1)
    eta = np.zeros(len(nodes), dtype=np.complex128)
    for n, value in profile.items():
        eta[n - lo] = value
    coeff = vectors.T @ eta
    cos_character = np.cos(2 * np.pi * np.remainder(nodes, 3) / 3)
    character = vectors.T @ (cos_character[:, None] * vectors)
    weights = np.conjugate(coeff)[:, None] * coeff[None, :] * character
    D = len(lam)
    C = spin * (spin + 1)
    phases = np.exp(0.25j * C * (lam[None, :] - lam[:, None]))
    q = np.sum(weights * phases)
    diag_term = np.sum(np.diag(weights))
    evolved = vectors @ (np.exp(0.25j * C * lam) * coeff)
    direct_q = np.vdot(evolved, cos_character * evolved)

    lag_rows = []
    abel_sum = 0.0
    near_counts = {"0.01": 0, "0.03": 0, "0.1": 0}
    near_weight = {key: 0.0 for key in near_counts}
    total_offdiag_l1 = 0.0
    actual_lag_sum = 0.0 + 0.0j
    max_variation = 0.0
    max_prefix_sum = 0.0
    for h in range(1, D):
        j = np.arange(D - h)
        w = weights[j, j + h]
        ph = 0.25 * C * (lam[j + h] - lam[j])
        inc = wrap(np.diff(ph))
        A = D * w
        variation = float(abs(A[-1]) + np.sum(np.abs(np.diff(A))))
        prefix = np.cumsum(np.exp(1j * ph))
        discrepancy = float(np.max(np.abs(prefix)))
        bound = variation * discrepancy / D
        actual = np.sum(w * np.exp(1j * ph))
        actual_lag_sum += actual
        abel_sum += bound
        max_variation = max(max_variation, variation)
        max_prefix_sum = max(max_prefix_sum, discrepancy)
        pair_l1 = float(np.sum(np.abs(w)))
        total_offdiag_l1 += pair_l1
        row = {"lag": h, "pairs": len(j), "scaled_weight_variation": variation,
               "max_phase_prefix": discrepancy, "abel_bound": bound,
               "actual_lag_abs": float(abs(actual)), "pair_weight_l1": pair_l1}
        lag_rows.append(row)
        for key in near_counts:
            threshold = float(key)
            mask = np.abs(inc) < threshold
            near_counts[key] += int(np.count_nonzero(mask))
            if len(w) > 1:
                near_weight[key] += float(np.sum(np.abs(w[:-1][mask])))

    direct_err = abs((np.real(diag_term) + 2 * np.real(actual_lag_sum)) - np.real(q))
    return {
        "S": spin, "dimension": D, "profile_core_radius": core_radius,
        "profile_tail_bound": module.cauchy_profile_tail_bound(0.25, core_radius),
        "profile_construction": profile_info["independent_method"],
        "q_real": float(np.real(q)), "q_imag": float(np.imag(q)),
        "spectral_vs_direct_q_error": float(abs(q - direct_q)),
        "diagonal_term_real": float(np.real(diag_term)),
        "offdiagonal_reconstruction_error": float(direct_err),
        "sum_actual_positive_lag_abs": float(abs(actual_lag_sum)),
        "total_offdiagonal_weight_l1": total_offdiag_l1,
        "total_abel_bound_positive_lags": abel_sum,
        "max_lag_scaled_weight_variation": max_variation,
        "max_lag_phase_prefix": max_prefix_sum,
        "near_alias_increment_counts": near_counts,
        "near_alias_weight_l1": near_weight,
        "scope": "finite-spin float64/complex128 diagnostic; not interval certified and not an asymptotic estimate",
        "selected_lags": [
            lag_rows[i] for i in sorted({0, len(lag_rows)//4,
                                         len(lag_rows)//2, 3*len(lag_rows)//4,
                                         len(lag_rows)-1})
        ],
    }


def main():
    module = load_runner()
    rows = [run(S, 24, module) for S in (24, 48, 96)]
    result = {
        "source_revision": "0e6ad8285096ed668816f18caaa6fbbfbd9c50e8",
        "input_sha256": {
            "exact_side_runner": hashlib.sha256(RUNNER.read_bytes()).hexdigest(),
            "exact_side_note": hashlib.sha256((ROOT / "docs/POSTMARK_ELECTRIC_EXACT_SIDE_FIXED_INDEX_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-24.md").read_bytes()).hexdigest(),
            "five_site_note": hashlib.sha256((ROOT / "docs/POSTMARK_ELECTRIC_FIVE_SITE_INTER_FIBER_PHASE_BOUNDED_THEOREM_NOTE_2026-09-24.md").read_bytes()).hexdigest(),
            "this_diagnostic": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "observable": "The real cos(2*pi*n/3) component of the period-three character; the positive-lag sum is paired with its Hermitian conjugate.",
        "criterion": "For each lag h, |sum_j W_{j,j+h} exp(i Phi_{S,h}(j))| <= D^{-1} Var(D W) max_prefix |sum exp(i Phi)|.",
        "alias_definition": "near alias means wrapped first difference of the actual lag phase Phi is within the stated threshold of 0 modulo 2pi.",
        "rows": rows,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
