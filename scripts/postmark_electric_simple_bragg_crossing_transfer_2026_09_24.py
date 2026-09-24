#!/usr/bin/env python3
"""Check the moving-frame phase identity and one simple Bragg crossing.

Exact symbolic algebra checks the first-order diagonal phase coefficient.
Finite exact-Jacobi products test the smooth principal-frame approximation
through one interior 5k=pi crossing. The finite products are diagnostics;
the uniform rate is established only by the shrinking-layer and outer-gap
argument in the paired theorem note.
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
)
ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "outputs" / "postmark_moving_index_2026_09_24" / "SIMPLE_BRAGG_CROSSING_TRANSFER_RESULTS.json"
SOURCE_REVISION = "20251000c51d7bd23573d36f091eb1c88ebde92a"

ELL = (0, 1, 0, 1, 1)
RHO = (0, 0, 0, 1, 0)
PI = (-1, 0, 0, 0, 1)
U_B_TARGET = 0.75
LAMBDA = 2.0 * (1.0 - U_B_TARGET**2) * (1.0 - math.cos(math.pi / 5.0))
U_B = U_B_TARGET
INTERVAL_HALF_WIDTH = 0.12


def alpha(u, a):
    return u**2 - u * (2 * a + 1)


def beta(u, a):
    return -a * (a + 1) + u * (2 * a + 1) - u**2


def symbolic_phase_identity() -> dict:
    """Derive -i A1_11/lambda_+ = g1/sin(k)-B modulo sin(k)^2+cos(k)^2=1."""
    u, z, q = sp.symbols("u z q", real=True)
    I = sp.I
    w = 1 - u**2
    wp = sp.diff(w, u)
    eps = sp.symbols("eps", real=True)
    A = sp.Matrix([[2*z, 1], [-1, 0]])
    p0, p1 = sp.eye(2), sp.zeros(2)

    for s in range(5):
        b = (alpha(u, ELL[s]) + alpha(u, RHO[s])) / 2
        d1 = alpha(u, ELL[s]) + alpha(u, PI[s])
        m1 = sp.Matrix([
            [d1/w - 2*z*b/w, -b/w],
            [-b/w, 0],
        ])
        p0, p1 = A*p0, A*p1 + m1*p0

    if sp.simplify(p0 - A**5) != sp.zeros(2):
        raise ArithmeticError("leading cell multiplication order mismatch")
    similarity = sp.diag(1, w)
    physical_p1 = similarity*p1*similarity.inv()

    plus = z + I*q
    minus = z - I*q
    amplitude = 1 / sp.sqrt(w*q)
    frame = sp.Matrix.hstack(
        amplitude * sp.Matrix([plus, -w]),
        amplitude * sp.Matrix([minus, -w]),
    )
    # Differentiate at fixed lambda: z'= (1-z)w'/w and k'=-z'/q.
    kprime = -(1-z)*wp/(w*q)
    zprime = -q*kprime
    qprime = z*kprime
    ampprime = -sp.Rational(1, 2)*amplitude*(wp/w + qprime/q)
    plusprime = zprime + I*qprime
    minusprime = zprime - I*qprime
    rplusprime = sp.Matrix([
        ampprime*plus + amplitude*plusprime,
        -ampprime*w - amplitude*wp,
    ])
    rminusprime = sp.Matrix([
        ampprime*minus + amplitude*minusprime,
        -ampprime*w - amplitude*wp,
    ])
    frameprime = sp.Matrix.hstack(rplusprime, rminusprime)

    leading_eigenvalue = plus**5
    leading_frame = sp.diag(leading_eigenvalue, minus**5)
    a1 = frame.inv()*physical_p1*frame - frame.inv()*frameprime*leading_frame
    g1 = u*(5*u*z - 5*u - 9*z + 8)/w
    berry = (2*z - 1)*wp/(2*w*q)
    identity = -I*a1[0, 0]/leading_eigenvalue - (g1/q - berry)
    wrong_berry_sign = -I*a1[0, 0]/leading_eigenvalue - (g1/q + berry)

    # Clear radicals, then reduce the numerator in the quadratic field q^2=1-z^2.
    residual = sp.cancel(sp.together(identity))
    numerator = residual.as_numer_denom()[0]
    numerator = sp.expand(numerator)
    polynomial = sp.Poly(numerator, q, domain="EX")
    relation = sp.Poly(q**2 + z**2 - 1, q, domain="EX")
    reduced = sp.rem(polynomial, relation).as_expr()
    reduced = sp.factor(sp.cancel(reduced))
    if reduced != 0:
        raise ArithmeticError(("moving-frame first-order phase identity", reduced))

    wrong_residual = sp.cancel(sp.together(wrong_berry_sign))
    wrong_numerator = sp.expand(wrong_residual.as_numer_denom()[0])
    wrong_remainder = sp.rem(sp.Poly(wrong_numerator, q, domain="EX"), relation).as_expr()
    wrong_remainder = sp.factor(sp.cancel(wrong_remainder))
    if wrong_remainder == 0:
        raise ArithmeticError("opposite connection sign was not rejected")

    shifted_g1 = -I*a1[0, 0]/leading_eigenvalue - ((g1 + 1)/q - berry)
    shifted_residual = sp.cancel(sp.together(shifted_g1))
    shifted_numerator = sp.expand(shifted_residual.as_numer_denom()[0])
    shifted_remainder = sp.rem(sp.Poly(shifted_numerator, q, domain="EX"), relation).as_expr()
    shifted_remainder = sp.factor(sp.cancel(shifted_remainder))
    if shifted_remainder == 0:
        raise ArithmeticError("additive g1 mutation was not rejected")

    determinant = sp.factor(frame.det())
    det_residual = sp.factor(sp.together(determinant + 2*I))
    det_num = sp.Poly(sp.expand(det_residual.as_numer_denom()[0]), q, domain="EX")
    det_reduced = sp.factor(sp.cancel(sp.rem(det_num, relation).as_expr()))
    if det_reduced != 0:
        raise ArithmeticError(("principal-frame determinant", det_reduced))

    return {
        "moving_frame_phase_identity_mod_sine_square_plus_cosine_square": str(reduced),
        "principal_frame_determinant_residual": str(det_reduced),
        "opposite_connection_sign_mutation_rejected": str(wrong_remainder),
        "additive_g1_mutation_rejected": str(shifted_remainder),
        "identity": "-i*(A1[0,0]/exp(5ik)) = g1/sin(k) - B, with lambda held fixed while differentiating u",
    }


def f(m: int) -> int:
    return m * (m + 1)


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


def local_k(u: float) -> float:
    w = 1.0 - u*u
    z = 1.0 - LAMBDA/(2.0*w)
    if not -1.0 < z < 1.0:
        raise ArithmeticError(("test interval left local elliptic band", u, z))
    return math.acos(z)


def principal_frame(u: float) -> np.ndarray:
    w = 1.0 - u*u
    k = local_k(u)
    sine = math.sin(k)
    vector = np.array([np.exp(1j*k), -w], dtype=np.complex128) / math.sqrt(w*sine)
    return np.column_stack((vector, vector.conjugate()))


def phase_correction(u: float) -> tuple[float, float, float]:
    w = 1.0 - u*u
    z = 1.0 - LAMBDA/(2.0*w)
    k = math.acos(z)
    sine = math.sin(k)
    wprime = -2.0*u
    g1 = u*(5.0*u*z - 5.0*u - 9.0*z + 8.0)/w
    berry = (2.0*z - 1.0)*wprime/(2.0*w*sine)
    return g1/sine - berry, g1/sine, berry


def wrap_phase(x: float) -> float:
    return math.atan2(math.sin(x), math.cos(x))


def finite_crossing_checks() -> dict:
    lo = U_B - INTERVAL_HALF_WIDTH
    hi = U_B + INTERVAL_HALF_WIDTH
    endpoint_ks = [local_k(lo), local_k(hi)]
    if not (0.0 < min(endpoint_ks) <= max(endpoint_ks) < math.pi):
        raise ArithmeticError(("test interval reaches a band edge", endpoint_ks))
    if abs(local_k(U_B) - math.pi/5.0) > 2e-14:
        raise ArithmeticError("selected test point is not on 5k=pi")

    rows = []
    for S in (120, 240, 480, 960, 1920, 3840, 7680, 15360):
        h0 = math.ceil(S*lo)
        h1 = math.floor(S*hi)
        moving_product = np.eye(2, dtype=np.complex128)
        theta = 0.0
        max_cell_det_error = 0.0
        max_frame_det_error = 0.0
        max_moving_su11_error = 0.0
        hyperbolic_cells = 0
        n_inner = 0
        rho = (1.0/S)**(2.0/3.0)
        inner_product = np.eye(2, dtype=np.complex128)

        for h in range(h0, h1):
            u = h/S
            next_u = (h+1)/S
            cell = exact_cell_transfer(S, h, LAMBDA)
            frame = principal_frame(u)
            next_frame = principal_frame(next_u)
            step = np.linalg.solve(next_frame, cell @ frame)
            moving_product = step @ moving_product
            det_error = abs(np.linalg.det(cell)-1.0)
            max_cell_det_error = max(max_cell_det_error, float(det_error))
            frame_det_error = max(
                abs(np.linalg.det(frame)+2j),
                abs(np.linalg.det(next_frame)+2j),
            )
            max_frame_det_error = max(max_frame_det_error, float(frame_det_error))
            su11_error = abs(abs(step[0, 0])**2 - abs(step[0, 1])**2 - 1.0)
            max_moving_su11_error = max(max_moving_su11_error, float(su11_error))
            trace = float(np.trace(cell))
            if abs(trace) > 2.0:
                hyperbolic_cells += 1

            local_k_value = local_k(u)
            correction, _, _ = phase_correction(u)
            theta += 5.0*local_k_value + correction/S

            if abs(u-U_B) <= rho:
                sigma = -1.0  # exp(i*5*k_B) for the selected m=1 crossing.
                inner_product = (sigma*step) @ inner_product
                n_inner += 1

        target = np.diag((np.exp(1j*theta), np.exp(-1j*theta)))
        product_error = float(np.linalg.norm(moving_product-target, ord=np.inf))
        predicted_order = S**(-1.0/3.0)
        inner_error = float(np.linalg.norm(inner_product-np.eye(2), ord=np.inf))
        rows.append({
            "S": S,
            "cells": h1-h0,
            "u_interval": [h0/S, h1/S],
            "crossing_u": U_B,
            "crossing_phase": math.pi,
            "min_endpoint_k": min(endpoint_ks),
            "max_endpoint_k": max(endpoint_ks),
            "hyperbolic_local_cells": hyperbolic_cells,
            "max_local_determinant_error": max_cell_det_error,
            "max_principal_frame_determinant_error": max_frame_det_error,
            "max_moving_frame_su11_identity_error": max_moving_su11_error,
            "principal_frame_product_error": product_error,
            "error_times_S_1_3": product_error/predicted_order,
            "off_diagonal_mixing": float(max(abs(moving_product[0, 1]), abs(moving_product[1, 0]))),
            "principal_phase_residual": wrap_phase(float(np.angle(moving_product[0, 0]))-theta),
            "inner_layer_width": rho,
            "inner_layer_cells": n_inner,
            "inner_scalar_product_error": inner_error,
            "inner_error_times_S_1_3": inner_error/predicted_order,
        })

    return {
        "energy_lambda": LAMBDA,
        "bragg_root_u": U_B,
        "bragg_index_m": 1,
        "test_interval": [lo, hi],
        "endpoint_local_momenta": endpoint_ks,
        "finite_sample_count": len(rows),
        "scope": "exact scalar-Jacobi finite products in float64; corroboration only, not proof of the uniform O(S^-1/3) rate",
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
        "symbolic": symbolic_phase_identity(),
        "finite_crossing": finite_crossing_checks(),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
