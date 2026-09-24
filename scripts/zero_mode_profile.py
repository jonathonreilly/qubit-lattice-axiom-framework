#!/usr/bin/env python3
"""Finite-spin legal-hop checks and low-spectrum diagnostics for M_S.

The hop-map checks and zero-mode recurrence are conditional on the supplied
six-site model.  The eigensolver output is diagnostic only.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/zero_mode_profile.py', 'scripts/core_derivation.py', 'scripts/spectral_fixed_time_probe.py')

import collections
import importlib.util
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh_tridiagonal

AUDIT_TIMEOUT_SEC = 3600

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("core", HERE / "core_derivation.py")
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
spec2 = importlib.util.spec_from_file_location("spectral", HERE / "spectral_fixed_time_probe.py")
spectral = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(spectral)

# x=m(m+1) for the two one-hop amplitudes attached to the edge n -> n+1.
POS_LEFT = (0, 1, 0, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2, 3, 3)
POS_RIGHT = (0, 0, 0, 1, 0, 1, 1, 1, 2, 1, 2, 2, 2, 3, 2)
NEG_LEFT = (-1, -2, -1, -2, -2, -2, -3, -2, -3, -3, -3, -4, -3, -4, -4)
NEG_RIGHT = (-1, -1, -1, -2, -1, -2, -2, -2, -3, -2, -3, -3, -3, -4, -3)


def casimir_factor(m: int, C: int) -> int:
    return C - m * (m + 1)


def predicted_x_pair(n: int) -> tuple[int, int]:
    if n >= 0:
        k, r = divmod(n, 15)
        m_left = 3 * k + POS_LEFT[r]
        m_right = 3 * k + POS_RIGHT[r]
        return (m_left * (m_left + 1), m_right * (m_right + 1))
    K = (-n + 14) // 15
    r = n + 15 * K
    return ((3 * K + NEG_LEFT[r]) * (3 * K + NEG_LEFT[r] + 1),
            (3 * K + NEG_RIGHT[r]) * (3 * K + NEG_RIGHT[r] + 1))


def build_hop_edges(spin: int):
    lo, hi = -5 * spin, 5 * spin - 4
    nodes = core.walk_nodes(max(abs(lo), abs(hi)) + 1)
    intermediates: dict[object, list[tuple[int, float, int]]] = collections.defaultdict(list)
    for n in range(lo, hi + 1):
        for q, amp, _edge, m, a in core.all_hops(nodes[n], spin):
            if core.count_empty_A(q) == 1:
                intermediates[q].append((n, amp, m * (m + a)))
    if len(intermediates) != hi - lo:
        raise ArithmeticError((spin, "intermediate row count", len(intermediates), hi - lo))

    edges = {}
    for q, entries in intermediates.items():
        entries.sort(key=lambda row: row[0])
        if len(entries) != 2 or entries[1][0] != entries[0][0] + 1:
            raise ArithmeticError((spin, "non-path hop row", entries))
        n = entries[0][0]
        if n in edges:
            raise ArithmeticError((spin, "duplicate adjacent hop row", n))
        if any(entry[1] == 0.0 for entry in entries):
            raise ArithmeticError((spin, "zero hop coefficient on path edge", n, entries))
        if (entries[0][2], entries[1][2]) != predicted_x_pair(n):
            raise ArithmeticError((spin, "one-hop residue polynomial", n,
                                   (entries[0][2], entries[1][2]), predicted_x_pair(n)))
        edges[n] = entries
    if set(edges) != set(range(lo, hi)):
        raise ArithmeticError((spin, "edge coverage", min(edges), max(edges)))
    return lo, hi, edges


def zero_mode(spin: int):
    lo, hi, edges = build_hop_edges(spin)
    C = spin * (spin + 1)
    h = {0: 1.0}
    for n in range(0, hi):
        left, right = edges[n]
        h[n + 1] = h[n] * abs(left[1] / right[1])
    for n in range(-1, lo - 1, -1):
        left, right = edges[n]
        h[n] = h[n + 1] * abs(right[1] / left[1])

    norm = math.sqrt(sum(value * value for value in h.values()))
    phi = {n: ((-1.0) ** n) * h[n] / norm for n in range(lo, hi + 1)}
    residual = max(abs(left[1] * phi[n] + right[1] * phi[n + 1])
                   for n, (left, right) in edges.items())

    h0 = h[0]
    block_error = 0.0
    C_float = float(C)
    for K in range(1, hi // 15 + 1):
        expected = casimir_factor(3 * K, C) / C_float
        block_error = max(block_error, abs(h[15 * K] / h0 - expected))
    for K in range(1, (-lo) // 15 + 1):
        expected = casimir_factor(3 * K - 1, C) / C_float
        block_error = max(block_error, abs(h[-15 * K] / h0 - expected))

    assert residual < 1e-11 and block_error < 1e-10, (spin,residual,block_error)
    weights = np.asarray([phi[n] * phi[n] for n in range(lo, hi + 1)])
    x = np.asarray([n / (5 * spin) for n in range(lo, hi + 1)])
    delta = 1 / (5 * spin)
    pi_comparison = weights / (delta * (1 - np.abs(x) + delta) ** 2)
    conductance_comparison = []
    for n, (left, right) in edges.items():
        xmid = (n + 0.5) / (5 * spin)
        ymid = 1 - abs(xmid) + delta
        b = abs(left[1] * right[1])
        conductance = b * abs(phi[n]) * abs(phi[n + 1])
        conductance_comparison.append(conductance / (delta * ymid**3))
    cumulative = np.cumsum(weights)
    primitive = lambda z: z - (2 / 3) * z**3 + z**5 / 5
    target_cdf = (15 / 16) * (primitive(x) + 8 / 15)
    vacancy_mode = float(sum(weights[i] for i, n in enumerate(range(lo, hi + 1)) if n % 3 == 0))
    interior = np.abs(x) <= 0.9
    profile_error = float(np.max(np.abs(np.asarray([h[n] / h0 for n in range(lo, hi + 1)])[interior]
                                         - (1 - x[interior] ** 2))))
    return {
        "S": spin,
        "C": C,
        "dimension": hi - lo + 1,
        "intermediate_rows": len(edges),
        "max_zero_mode_row_residual": residual,
        "max_block_product_error": block_error,
        "origin_weight": float(phi[0] ** 2),
        "S_times_origin_weight": float(spin * phi[0] ** 2),
        "pi_edge_comparison_min_max": [float(np.min(pi_comparison)), float(np.max(pi_comparison))],
        "conductance_edge_comparison_min_max": [float(np.min(conductance_comparison)),
                                                float(np.max(conductance_comparison))],
        "profile_max_abs_error_on_abs_x_le_0_9": profile_error,
        "scaled_flux_cdf_sup_error": float(np.max(np.abs(cumulative - target_cdf))),
        "zero_mode_vacancy_probability": vacancy_mode,
    }


def low_spectrum(spin: int, count: int = 13):
    lo, hi, diag, off = spectral.finite_spin_m(spin)
    C = spin * (spin + 1)
    eigvals, eigvecs = eigh_tridiagonal(diag, off, select="i",
                                        select_range=(0, count - 1))
    j = np.arange(count)
    expected = j * (j + 5) / 25
    return {
        "S": spin,
        "C_times_low_eigenvalues": (C * eigvals).tolist(),
        "Gegenbauer_candidate_j_jplus5_over25": expected.tolist(),
        "absolute_errors": np.abs(C * eigvals - expected).tolist(),
        "C_times_origin_spectral_weights": (C * eigvecs[-lo, :] ** 2).tolist(),
    }


def run(spins, spectral_spins):
    results = [zero_mode(S) for S in spins]
    spectrum = [low_spectrum(S) for S in spectral_spins]
    return {
        "status": "The theorem note derives exact one-hop zero-mode identities and an analytic fixed-index form-convergence proof; this runner checks finite-spin hop identities and supplies corroborative spectral diagnostics only.",
        "upstream_model_pr": 8831,
        "upstream_model_head": "b6eb31bedb3134dfacd8f4ab83cb7d96fc6dc953",
        "campaign_science_checkpoint_parent": "d7ba50d4e20a66d995c8fdc4e69254f0536b0108",
        "operator": "M_S=-H2,S=A_S^* A_S and G_S=M_S^2-C M_S",
        "positive_block_identity": "h[15K]/h[0]=(C-(3K)(3K+1))/C",
        "negative_block_identity": "h[-15K]/h[0]=(C-(3K-1)(3K))/C",
        "continuum_zero_mode_density": "(15/16)(1-x^2)^2 dx on [-1,1], x=n/(5S)",
        "rescaled_form_on_smooth_tests": "(1/25) integral rho(x)(1-x^2) |f'(x)|^2 dx, rho=(15/16)(1-x^2)^2",
        "limit_differential_expression": "-(1/25)[(1-x^2)f''-6x f']",
        "fixed_index_spectral_claim_in_note": "C lambda_(S,j) -> j(j+5)/25 for each fixed j, proved there by compactness, recovery, lower semicontinuity, and min-max; this runner does not implement that proof",
        "numerical_low_spectrum_role": "Double-precision values through S=1024 corroborate the analytic fixed-index result only; they do not prove it or establish fixed-time dephasing",
        "zero_mode_results": results,
        "low_spectrum_results": spectrum,
        "limits": "No fixed-laboratory-time readout limit follows. The zero-mode projection at the prepared state is O(1/S); the moving-index spectral tail and off-diagonal phases remain uncontrolled.",
    }


if __name__ == "__main__":
    payload = run(tuple(range(1, 21)) + (32, 64, 128, 256, 512, 1024),
                  (8, 16, 32, 64, 128, 256, 512, 1024))
    out = HERE / "ZERO_MODE_PROFILE_RESULTS.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
