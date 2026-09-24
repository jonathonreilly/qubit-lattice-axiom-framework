#!/usr/bin/env python3
"""Finite-spin census of one-index and fixed-lag aliases in the exact q_S sum.

This diagnostic keeps the exact prepared-profile coefficients and cosine-
character overlaps. It separates (i) individual spectral-index phase slopes
alpha_j = C (lambda_{j+1}-lambda_j)/4 modulo 2 pi from (ii) the fixed-lag
phase increment alpha_{j+h}-alpha_j modulo 2 pi. The second is the discrete
derivative governing cancellation within a fixed lag. Float64 only; no
asymptotic or interval claim is made.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
from scipy.linalg import eigh_tridiagonal

ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "scripts" / "postmark_electric_exact_side_fixed_index_kernel_2026_09_24.py"
OUT = Path(__file__).with_name("phase_alias_overlap_census.json")
THRESHOLDS = (0.01, 0.03, 0.1)
LAG_EDGES = (0.0, 0.125, 0.25, 0.5, 0.75, 1.0000000001)


def load_runner():
    spec = importlib.util.spec_from_file_location("exact_side_alias", RUNNER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def wrap(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


def zero_stat():
    return {"pairs": 0, "weight_l1": 0.0, "signed_real": 0.0,
            "signed_imag": 0.0, "sum_lag_abs": 0.0}


def run(spin: int, module):
    lo, hi, diag, offdiag, _ = module.finite_spin_matrix(spin)
    lam, vectors = eigh_tridiagonal(diag, offdiag, eigvals_only=False)
    profile, profile_info = module.infinite_reference_profile(0.25, radius=24)
    nodes = np.arange(lo, hi + 1)
    eta = np.zeros(len(nodes), dtype=np.complex128)
    for n, value in profile.items():
        eta[n - lo] = value
    coeff = vectors.T @ eta
    char = np.cos(2 * np.pi * np.remainder(nodes, 3) / 3)
    V = vectors.T @ (char[:, None] * vectors)
    D = len(lam)
    C = spin * (spin + 1)

    # q_S in the profile reduction has phases exp(i C lambda_j/4); the
    # finite N_S^2 evolution is already encoded in eta_inf(t) and coeff.
    theta = C * lam / 4.0
    alpha = np.diff(theta)
    alpha_residual = wrap(alpha)
    alpha_alias_index = np.rint(alpha / (2 * np.pi)).astype(np.int64)
    out = {
        "S": spin,
        "dimension": D,
        "profile_core_radius": 24,
        "profile_tail_bound": module.cauchy_profile_tail_bound(0.25, 24),
        "profile_construction": profile_info["independent_method"],
        "individual_phase_slope": {
            "raw_min": float(np.min(alpha)),
            "raw_max": float(np.max(alpha)),
            "alias_index_min": int(np.min(alpha_alias_index)),
            "alias_index_max": int(np.max(alpha_alias_index)),
            "distinct_alias_indices": int(np.unique(alpha_alias_index).size),
            "prepared_mode_mass_by_threshold": {},
        },
        "fixed_lag_increment_aliases": {},
        "q_real_direct": None,
        "q_real_from_lags": None,
        "q_reconstruction_error": None,
        "scope": "finite-spin float64/complex128 census; no interval or asymptotic claim",
    }
    for eps in THRESHOLDS:
        mask = np.abs(alpha_residual) < eps
        mode_mass = float(np.sum(np.abs(coeff[:-1][mask]) ** 2))
        out["individual_phase_slope"]["prepared_mode_mass_by_threshold"][str(eps)] = {
            "resonant_gap_count": int(np.count_nonzero(mask)),
            "prepared_mass_on_left_mode": mode_mass,
        }

    edges = np.array(LAG_EDGES, dtype=float)
    lag_bins = [{"lag_fraction": [float(edges[b]), float(min(edges[b + 1], 1.0))],
                 "lags": 0,
                 "fixed_lag_resonance": {str(e): zero_stat() for e in THRESHOLDS},
                 "individual_slope_classes": {
                     str(e): {k: zero_stat() for k in ("both", "left_only", "right_only", "neither")}
                     for e in THRESHOLDS},
                 } for b in range(len(edges) - 1)]
    total = {str(e): {
        "fixed_lag_resonance": zero_stat(),
        "individual_slope_classes": {
            k: zero_stat() for k in ("both", "left_only", "right_only", "neither")},
    } for e in THRESHOLDS}
    endpoint = {"pairs": 0, "weight_l1": 0.0, "signed_real": 0.0,
                "signed_imag": 0.0}
    lag_sum = 0j
    diagonal = np.sum(np.abs(coeff) ** 2 * np.diag(V))
    direct_state = vectors @ (np.exp(1j * theta) * coeff)
    direct_q = np.vdot(direct_state, char * direct_state)

    for h in range(1, D):
        # The last pair has no forward adjacent phase increment at its right
        # endpoint. Keep it in q reconstruction and report it separately.
        valid = D - h - 1
        j = np.arange(valid)
        all_w = np.conjugate(coeff[:-h]) * coeff[h:] * np.diag(V, k=h)
        all_ph = theta[np.arange(D - h) + h] - theta[np.arange(D - h)]
        all_terms = all_w * np.exp(1j * all_ph)
        w = all_w[:valid]
        ph = all_ph[:valid]
        terms = all_terms[:valid]
        lag_sum += np.sum(terms)
        if len(all_w) > valid:
            tail_term = all_terms[valid]
            endpoint["pairs"] += 1
            endpoint["weight_l1"] += float(abs(all_w[valid]))
            endpoint["signed_real"] += float(tail_term.real)
            endpoint["signed_imag"] += float(tail_term.imag)
        b = min(int(np.searchsorted(edges, h / D, side="right") - 1), len(lag_bins) - 1)
        lag_bins[b]["lags"] += 1
        rj = alpha_residual[j]
        rk = alpha_residual[j + h]
        lag_residual = wrap(alpha[j + h] - alpha[j])
        for eps in THRESHOLDS:
            key = str(eps)
            lag_mask = np.abs(lag_residual) < eps
            classes = {
                "both": (np.abs(rj) < eps) & (np.abs(rk) < eps),
                "left_only": (np.abs(rj) < eps) & (np.abs(rk) >= eps),
                "right_only": (np.abs(rj) >= eps) & (np.abs(rk) < eps),
                "neither": (np.abs(rj) >= eps) & (np.abs(rk) >= eps),
            }
            for dest in (total[key]["fixed_lag_resonance"], lag_bins[b]["fixed_lag_resonance"][key]):
                z = np.sum(terms[lag_mask])
                dest["pairs"] += int(np.count_nonzero(lag_mask))
                dest["weight_l1"] += float(np.sum(np.abs(w[lag_mask])))
                dest["signed_real"] += float(z.real)
                dest["signed_imag"] += float(z.imag)
                dest["sum_lag_abs"] += float(abs(z))
            for cname, mask in classes.items():
                for dest in (total[key]["individual_slope_classes"][cname],
                             lag_bins[b]["individual_slope_classes"][key][cname]):
                    z = np.sum(terms[mask])
                    dest["pairs"] += int(np.count_nonzero(mask))
                    dest["weight_l1"] += float(np.sum(np.abs(w[mask])))
                    dest["signed_real"] += float(z.real)
                    dest["signed_imag"] += float(z.imag)
                    dest["sum_lag_abs"] += float(abs(z))
        if h % 512 == 0:
            print(f"S={spin} completed_lag={h}/{D-1}", flush=True)

    # Restore separately tracked terminal pairs in the exact lag sum.
    q_from_lags = diagonal + 2 * np.real(lag_sum + endpoint["signed_real"] + 1j * endpoint["signed_imag"])
    out["q_real_direct"] = float(direct_q.real)
    out["q_real_from_lags"] = float(q_from_lags)
    out["q_reconstruction_error"] = float(abs(direct_q.real - q_from_lags))
    out["fixed_lag_increment_aliases"] = {
        "definition": "wrap(alpha[j+h]-alpha[j]); this is the discrete derivative of the lag-h phase in j",
        "thresholds": total,
        "lag_fraction_bins": lag_bins,
        "unclassified_terminal_pair_per_lag": endpoint,
    }
    return out


def main():
    module = load_runner()
    rows = []
    for spin in (96, 192, 384, 512):
        rows.append(run(spin, module))
    result = {
        "source_revision": "5171af01191cc2db9d5bad0f8eca2185114ebbe3",
        "input_sha256": {
            "exact_side_runner": hashlib.sha256(RUNNER.read_bytes()).hexdigest(),
            "this_diagnostic": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "phase_convention": "For q_S, theta_j=C*lambda_j/4 multiplies the prepared-profile spectral coefficient c_j. The exp(-i*N_S^2/4) factor belongs to the prepared profile eta_inf, not to this conjugation phase.",
        "alias_conventions": {
            "individual": "alpha_j=theta_(j+1)-theta_j; alias if alpha_j is within epsilon of 2*pi*integer",
            "fixed_lag": "alpha_(j+h)-alpha_j; alias if this lag-phase derivative is within epsilon of 2*pi*integer",
            "warning": "The two conditions are different. These bins are descriptive diagnostics, not estimates of the omitted complement.",
        },
        "rows": rows,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
