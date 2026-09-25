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

ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "scripts" / "postmark_electric_exact_side_fixed_index_kernel_2026_09_24.py"
OUT = Path(__file__).with_name("full_lag_scale_decomposition.json")


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
    D = len(lam)
    C = spin * (spin + 1)
    evolved = vectors @ (np.exp(0.25j * C * lam) * coeff)
    direct_q = np.vdot(evolved, cos_character * evolved)
    diag_term = np.sum(np.abs(coeff) ** 2 * np.diag(character))

    edges = np.array([0.0, 0.125, 0.25, 0.5, 0.75, 1.0000000001])
    bins = [{"lag_fraction": [float(edges[b]), float(min(edges[b + 1], 1.0))],
             "signed_lag_sum_real": 0.0, "signed_lag_sum_imag": 0.0,
             "sum_lag_abs": 0.0, "max_lag_abs": 0.0,
             "pair_weight_l1": 0.0, "abel_bound_sum": 0.0,
             "near_alias_weight_l1_at_0_01": 0.0, "lags": 0}
            for b in range(len(edges) - 1)]
    near_counts = {"0.01": 0, "0.03": 0, "0.1": 0}
    near_weight = {key: 0.0 for key in near_counts}
    abel_sum = 0.0
    total_offdiag_l1 = 0.0
    actual_lag_sum = 0.0 + 0.0j
    max_variation = 0.0
    max_prefix_sum = 0.0
    for h in range(1, D):
        j = np.arange(D - h)
        w = np.conjugate(coeff[:-h]) * coeff[h:] * np.diag(character, k=h)
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
        b = min(int(np.searchsorted(edges, h / D, side="right") - 1),
                len(bins) - 1)
        bins[b]["signed_lag_sum_real"] += float(np.real(actual))
        bins[b]["signed_lag_sum_imag"] += float(np.imag(actual))
        bins[b]["sum_lag_abs"] += float(abs(actual))
        bins[b]["max_lag_abs"] = max(bins[b]["max_lag_abs"], float(abs(actual)))
        bins[b]["pair_weight_l1"] += pair_l1
        bins[b]["abel_bound_sum"] += bound
        bins[b]["lags"] += 1
        for key in near_counts:
            threshold = float(key)
            mask = np.abs(inc) < threshold
            near_counts[key] += int(np.count_nonzero(mask))
            if len(w) > 1:
                near_l1 = float(np.sum(np.abs(w[:-1][mask])))
                near_weight[key] += near_l1
                if key == "0.01":
                    bins[b]["near_alias_weight_l1_at_0_01"] += near_l1

    spectral_q = diag_term + 2 * np.real(actual_lag_sum)
    direct_err = abs(float(np.real(direct_q)) - float(np.real(spectral_q)))
    return {
        "S": spin, "dimension": D, "profile_core_radius": core_radius,
        "profile_tail_bound": module.cauchy_profile_tail_bound(0.25, core_radius),
        "profile_construction": profile_info["independent_method"],
        "q_real_direct": float(np.real(direct_q)), "q_imag_direct": float(np.imag(direct_q)),
        "spectral_vs_direct_real_error": float(direct_err),
        "diagonal_term_real": float(np.real(diag_term)),
        "offdiagonal_reconstruction_error": float(direct_err),
        "sum_actual_positive_lag_abs": float(abs(actual_lag_sum)),
        "total_offdiagonal_weight_l1": total_offdiag_l1,
        "total_abel_bound_positive_lags": abel_sum,
        "max_lag_scaled_weight_variation": max_variation,
        "max_lag_phase_prefix": max_prefix_sum,
        "near_alias_increment_counts": near_counts,
        "near_alias_weight_l1": near_weight,
        "lag_fraction_bins": bins,
        "scope": "finite-spin float64/complex128 all-lag scale diagnostic; not interval certified and not an asymptotic estimate",
    }


def main():
    module = load_runner()
    rows = [run(S, 24, module) for S in (96, 192, 384, 512)]
    result = {
        "source_revision": "5171af01191cc2db9d5bad0f8eca2185114ebbe3",
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
