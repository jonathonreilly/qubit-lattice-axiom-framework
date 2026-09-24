#!/usr/bin/env python3
"""Check the regular-interval adiabatic transfer and overlap phase."""
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
)
ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "outputs" / "postmark_moving_index_2026_09_24" / "REGULAR_BULK_PHASE_TRANSPORT_RESULTS.json"
SOURCE_REVISION = "0e6ad8285096ed668816f18caaa6fbbfbd9c50e8"

ELL = (0, 1, 0, 1, 1)
RHO = (0, 0, 0, 1, 0)
PI = (-1, 0, 0, 0, 1)


def f(m: int) -> int:
    return m * (m + 1)


def berry_formula(w, wprime, cosine, sine, kprime):
    return (wprime * cosine / w + kprime * sine) / (2 * sine)


def symbolic_berry_identity() -> dict:
    w, wprime, cosine, sine, kprime = sp.symbols(
        "w wprime cosine sine kprime", real=True, positive=True
    )
    imag = sp.I
    amp = 1 / sp.sqrt(w * sine)
    lower_amp = sp.sqrt(w / sine)
    r = sp.Matrix([amp * (cosine + imag * sine), -lower_amp])
    dr = sp.Matrix([
        amp * (-sine * kprime + imag * cosine * kprime)
        - sp.Rational(1, 2) * amp
        * (wprime / w + cosine * kprime / sine)
        * (cosine + imag * sine),
        -sp.Rational(1, 2) * lower_amp
        * (wprime / w - cosine * kprime / sine),
    ])
    frame = sp.Matrix.hstack(r, sp.conjugate(r))
    left = frame.inv()[0, :]
    calculated = sp.simplify(sp.im((left * dr)[0]))
    expected = sp.simplify(berry_formula(w, wprime, cosine, sine, kprime))
    residual = sp.simplify(calculated - expected)
    determinant_residual = sp.simplify(frame.det() + 2 * imag)
    checks = {
        "principal_frame_determinant": determinant_residual,
        "berry_connection_formula": residual,
    }
    if any(value != 0 for value in checks.values()):
        raise ArithmeticError(("principal-cell connection identity", checks))
    return {key: str(value) for key, value in checks.items()}


def exact_r(S: int, h: int, a: int) -> float:
    return 1.0 - f(h + a) / (S * (S + 1))


def exact_site_transfer(S: int, h: int, s: int, lam: float) -> np.ndarray:
    left = exact_r(S, h, ELL[s])
    right = exact_r(S, h, RHO[s])
    previous = exact_r(S, h, PI[s])
    offdiag = -math.sqrt(left * right)
    diagonal = left + previous
    return np.array([[(lam - diagonal) / offdiag, -1.0 / offdiag],
                     [offdiag, 0.0]], dtype=np.float64)


def exact_cell_transfer(S: int, h: int, lam: float) -> np.ndarray:
    out = np.eye(2)
    for s in range(5):
        out = exact_site_transfer(S, h, s, lam) @ out
    return out


def local_k(u: float, lam: float) -> float:
    w = 1.0 - u * u
    z = 1.0 - lam / (2.0 * w)
    return math.acos(z)


def nearest_phase(trace: float, k: float) -> float:
    theta = math.acos(max(-1.0, min(1.0, trace / 2.0)))
    candidates = [sign * theta + 2.0 * math.pi * turn
                  for sign in (-1.0, 1.0) for turn in range(-4, 5)]
    return min(candidates, key=lambda phase: abs(phase - 5.0 * k))


def exact_eigenbasis(S: int, h: int, lam: float):
    matrix = exact_cell_transfer(S, h, lam)
    u = h / S
    w = 1.0 - u * u
    k = local_k(u, lam)
    phase = nearest_phase(float(np.trace(matrix)), k)
    upper_right = float(matrix[0, 1])
    flux = upper_right * math.sin(phase)
    if flux <= 0.0:
        raise ArithmeticError(("eigenvector normalization lost positive flux",
                               S, h, k, phase, upper_right, flux))
    eigenvalue = np.exp(1j * phase)
    vector = np.exp(1j * k) * np.array(
        [upper_right, eigenvalue - matrix[0, 0]], dtype=np.complex128
    ) / math.sqrt(flux)
    frame = np.column_stack((vector, vector.conjugate()))
    residual = float(np.linalg.norm(matrix @ vector - eigenvalue * vector,
                                    ord=np.inf))
    return matrix, phase, frame, residual


def connection(u: float, lam: float) -> float:
    w = 1.0 - u * u
    cosine = 1.0 - lam / (2.0 * w)
    k = math.acos(cosine)
    sine = math.sin(k)
    wprime = -2.0 * u
    kprime = -(1.0 - cosine) * wprime / (w * sine)
    return berry_formula(w, wprime, cosine, sine, kprime)


def integrate_connection(lo: float, hi: float) -> float:
    nodes, weights = np.polynomial.legendre.leggauss(192)
    midpoint = (lo + hi) / 2.0
    halfwidth = (hi - lo) / 2.0
    return halfwidth * sum(
        weight * connection(midpoint + halfwidth * node, LAMBDA)
        for node, weight in zip(nodes, weights)
    )


def wrap_phase(value: float) -> float:
    return math.atan2(math.sin(value), math.cos(value))


LAMBDA = 2.0 * (1.0 - math.cos(1.0))


def finite_interval_checks() -> dict:
    rows = []
    max_basis_det_error = 0.0
    max_eigenvector_residual = 0.0
    max_overlap_form_error = 0.0

    for S in (120, 240, 480, 960):
        h0 = -round(0.10 * S)
        h1 = round(0.30 * S)
        data = {
            h: exact_eigenbasis(S, h, LAMBDA)
            for h in range(h0, h1 + 1)
        }
        product = np.eye(2)
        phase_product = 0.0
        overlap_phase = 0.0
        overlap_magnitude = 1.0
        min_bulk_gap = 1.0

        for h in range(h0, h1):
            matrix, phase, frame, eigen_residual = data[h]
            next_frame = data[h + 1][2]
            moving_overlap = np.linalg.solve(next_frame, frame)
            beta = moving_overlap[0, 0]
            gamma = moving_overlap[0, 1]
            min_bulk_gap = min(min_bulk_gap, abs(math.sin(phase)))
            max_basis_det_error = max(
                max_basis_det_error, abs(np.linalg.det(frame) + 2j)
            )
            max_eigenvector_residual = max(max_eigenvector_residual,
                                            eigen_residual)
            max_overlap_form_error = max(
                max_overlap_form_error,
                abs(abs(beta) ** 2 - abs(gamma) ** 2 - 1.0),
            )
            product = matrix @ product
            phase_product += phase
            overlap_phase += float(np.angle(beta))
            overlap_magnitude *= abs(beta)

        lo = h0 / S
        hi = h1 / S
        berry_integral = integrate_connection(lo, hi)
        phase_frame = data[h0][2]
        end_frame = data[h1][2]
        eta = overlap_magnitude * np.exp(
            1j * (phase_product + overlap_phase)
        )
        diagonal_approximation = (
            end_frame
            @ np.diag((eta, eta.conjugate()))
            @ np.linalg.inv(phase_frame)
        )
        product_error = float(np.linalg.norm(
            product - diagonal_approximation, ord=np.inf
        ))

        phase_without_g2 = 0.0
        for h in range(h0, h1):
            u = h / S
            w = 1.0 - u * u
            k = local_k(u, LAMBDA)
            z = math.cos(k)
            g1 = u * (5*u*z - 5*u - 9*z + 8) / w
            phase_without_g2 += 5.0*k + g1/(S*math.sin(k))
        phase_asymptotic_error = wrap_phase(
            phase_product + overlap_phase
            - phase_without_g2 + berry_integral
        )

        rows.append({
            "S": S,
            "cells": h1 - h0,
            "u_interval": [lo, hi],
            "min_abs_sin_local_phase": min_bulk_gap,
            "basis_det_error": max_basis_det_error,
            "max_eigenvector_residual": max_eigenvector_residual,
            "max_su11_overlap_identity_error": max_overlap_form_error,
            "diagonal_product_magnitude": overlap_magnitude,
            "product_diagonal_approximation_error": product_error,
            "product_error_times_S": S * product_error,
            "discrete_overlap_phase": overlap_phase,
            "negative_connection_integral": -berry_integral,
            "overlap_phase_connection_residual": wrap_phase(
                overlap_phase + berry_integral
            ),
            "accumulated_phase_asymptotic_residual": phase_asymptotic_error,
        })

    return {
        "finite_sample_count": len(rows),
        "energy_lambda": LAMBDA,
        "regular_interval_targets": [-0.10, 0.30],
        "scope": "finite float64 corroboration only; no rate constant is inferred from these samples",
        "sample_rows": rows,
    }


def source_hashes() -> dict:
    return {
        rel: hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        for rel in AUDIT_INPUT_PATHS
    }


def main() -> None:
    result = {
        "actual_current_surface_status": "conditional-support",
        "target_claim_type": "bounded_theorem",
        "source_revision": SOURCE_REVISION,
        "source_sha256": source_hashes(),
        "numpy": np.__version__,
        "sympy": sp.__version__,
        "symbolic_connection_checks": symbolic_berry_identity(),
        "finite_interval_checks": finite_interval_checks(),
        "scope_limit": "macroscopic product only on compact nonturning and non-Bragg intervals; no layer matching, global quantization, or prepared-readout estimate",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
