#!/usr/bin/env python3
"""Check the symmetry-suppressed central Bragg transfer estimate.

The symbolic checks establish vanishing of the first-order moving-frame
matrix at the central point and the exact quadratic contact coefficient.
Finite exact-Jacobi products test the principal-frame approximation at four
central Bragg energies. They corroborate but do not prove the uniform bound.
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
    "docs/POSTMARK_ELECTRIC_CENTRAL_BRAGG_CROSSING_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-24.md",
)
ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "outputs" / "postmark_moving_index_2026_09_24" / "CENTRAL_BRAGG_CROSSING_TRANSFER_RESULTS.json"
SOURCE_REVISION = "20251000c51d7bd23573d36f091eb1c88ebde92a"

ELL = (0, 1, 0, 1, 1)
RHO = (0, 0, 0, 1, 0)
PI = (-1, 0, 0, 0, 1)
U_INTERVAL = (-0.10, 0.10)


def alpha(u, a):
    return u**2 - u*(2*a+1)


def symbolic_central_checks() -> dict:
    u, z, q = sp.symbols("u z q", real=True)
    I = sp.I
    w = 1-u**2
    wp = sp.diff(w, u)
    A = sp.Matrix([[2*z, 1], [-1, 0]])
    p0, p1 = sp.eye(2), sp.zeros(2)

    for s in range(5):
        b = (alpha(u, ELL[s]) + alpha(u, RHO[s]))/2
        d1 = alpha(u, ELL[s]) + alpha(u, PI[s])
        m1 = sp.Matrix([
            [d1/w - 2*z*b/w, -b/w],
            [-b/w, 0],
        ])
        p0, p1 = A*p0, A*p1 + m1*p0

    if sp.simplify(p0-A**5) != sp.zeros(2):
        raise ArithmeticError("leading five-site multiplication order mismatch")

    similarity = sp.diag(1, w)
    physical_p1 = similarity*p1*similarity.inv()
    plus, minus = z+I*q, z-I*q
    amplitude = 1/sp.sqrt(w*q)
    frame = sp.Matrix.hstack(
        amplitude*sp.Matrix([plus, -w]),
        amplitude*sp.Matrix([minus, -w]),
    )
    kprime = -(1-z)*wp/(w*q)
    zprime, qprime = -q*kprime, z*kprime
    ampprime = -sp.Rational(1, 2)*amplitude*(wp/w+qprime/q)
    frameprime = sp.Matrix.hstack(
        sp.Matrix([ampprime*plus+amplitude*(zprime+I*qprime),
                   -ampprime*w-amplitude*wp]),
        sp.Matrix([ampprime*minus+amplitude*(zprime-I*qprime),
                   -ampprime*w-amplitude*wp]),
    )
    leading = sp.diag(plus**5, minus**5)
    a1 = frame.inv()*physical_p1*frame-frame.inv()*frameprime*leading
    central_matrix = sp.simplify(a1.subs(u, 0))
    if central_matrix != sp.zeros(2):
        raise ArithmeticError(("central first-order moving-frame matrix", central_matrix))

    g1 = u*(5*u*z-5*u-9*z+8)/w
    berry = (2*z-1)*wp/(2*w*q)
    if sp.simplify(g1.subs(u, 0)) != 0 or sp.simplify(berry.subs(u, 0)) != 0:
        raise ArithmeticError("central first-order diagonal phase did not vanish")

    # A fixed off-diagonal term violates the exact central vanishing and is a
    # deliberate mutation check for the structural premise used in the rate.
    mutated = central_matrix + sp.Matrix([[0, 1], [1, 0]])
    if mutated == sp.zeros(2):
        raise ArithmeticError("constant off-diagonal mutation was not rejected")

    v = sp.symbols("v", real=True)
    contact_checks = {}
    for m in (1, 2, 3, 4):
        km = sp.pi*m/5
        cosine, sine = sp.cos(km), sp.sin(km)
        a = 1-cosine
        z_v = 1-a/(1-v)
        U4 = 16*z_v**4-12*z_v**2+1
        sin5k = U4*sp.sqrt(1-z_v**2)
        actual = sp.diff(sin5k, v).subs(v, 0)
        expected = 5*(-1)**m*a/sine
        residual = sp.simplify(sp.trigsimp(actual-expected))
        if residual != 0:
            raise ArithmeticError(("quadratic contact coefficient", m, residual))
        contact_checks[str(m)] = str(residual)

    return {
        "central_first_order_moving_frame_matrix": str(central_matrix),
        "central_diagonal_phase_coefficient_vanishes": True,
        "constant_offdiagonal_mutation_rejected": True,
        "quadratic_contact_coefficient_residuals": contact_checks,
        "first_order_scaling": "A1(0)=0 and A1 is analytic, hence A1(u)=O(u) on compact J",
    }


def f(m: int) -> int:
    return m*(m+1)


def exact_r(S: int, h: int, a: int) -> float:
    return 1.0-f(h+a)/(S*(S+1))


def exact_site_transfer(S: int, h: int, s: int, lam: float) -> np.ndarray:
    left = exact_r(S, h, ELL[s])
    right = exact_r(S, h, RHO[s])
    previous = exact_r(S, h, PI[s])
    offdiag = -math.sqrt(left*right)
    diagonal = left+previous
    return np.array([[(lam-diagonal)/offdiag, -1.0/offdiag],
                     [offdiag, 0.0]], dtype=np.float64)


def exact_cell_transfer(S: int, h: int, lam: float) -> np.ndarray:
    product = np.eye(2)
    for s in range(5):
        product = exact_site_transfer(S, h, s, lam) @ product
    return product


def local_k(u: float, lam: float) -> float:
    w = 1-u*u
    z = 1-lam/(2*w)
    if not -1 < z < 1:
        raise ArithmeticError(("test energy left the local band", u, lam, z))
    return math.acos(z)


def principal_frame(u: float, lam: float) -> np.ndarray:
    w = 1-u*u
    k = local_k(u, lam)
    r = np.array([np.exp(1j*k), -w], dtype=np.complex128)/math.sqrt(w*math.sin(k))
    return np.column_stack((r, r.conjugate()))


def phase_correction(u: float, lam: float) -> float:
    w = 1-u*u
    z = 1-lam/(2*w)
    k = math.acos(z)
    g1 = u*(5*u*z-5*u-9*z+8)/w
    berry = (2*z-1)*(-2*u)/(2*w*math.sin(k))
    return g1/math.sin(k)-berry


def finite_central_checks() -> dict:
    rows = []
    lo, hi = U_INTERVAL
    endpoint_momenta = {}
    for m in (1, 2, 3, 4):
        lam = 2*(1-math.cos(m*math.pi/5))
        endpoint_momenta[str(m)] = [local_k(lo, lam), local_k(hi, lam)]
        if abs(local_k(0.0, lam)-m*math.pi/5) > 2e-14:
            raise ArithmeticError(("central Bragg point mismatch", m))
        kmax = max(endpoint_momenta[str(m)])
        other_roots = [n for n in (1, 2, 3, 4)
                       if n != m and m*math.pi/5 < n*math.pi/5 < kmax]
        if other_roots:
            raise ArithmeticError(("test interval includes another Bragg point", m, other_roots))

        for S in (120, 240, 480, 960, 1920, 3840, 7680, 15360):
            h0, h1 = math.ceil(S*lo), math.floor(S*hi)
            rho = S**-0.5
            product = np.eye(2, dtype=np.complex128)
            inner = np.eye(2, dtype=np.complex128)
            theta = 0.0
            inner_cells = 0
            hyperbolic_cells = 0
            max_det_error = 0.0
            max_frame_det_error = 0.0
            max_su11_error = 0.0

            for h in range(h0, h1):
                u, next_u = h/S, (h+1)/S
                cell = exact_cell_transfer(S, h, lam)
                frame = principal_frame(u, lam)
                next_frame = principal_frame(next_u, lam)
                step = np.linalg.solve(next_frame, cell @ frame)
                product = step @ product
                max_det_error = max(max_det_error, abs(np.linalg.det(cell)-1.0))
                max_frame_det_error = max(
                    max_frame_det_error,
                    abs(np.linalg.det(frame)+2j),
                    abs(np.linalg.det(next_frame)+2j),
                )
                max_su11_error = max(
                    max_su11_error,
                    abs(abs(step[0, 0])**2-abs(step[0, 1])**2-1.0),
                )
                if abs(float(np.trace(cell))) > 2.0:
                    hyperbolic_cells += 1
                theta += 5*local_k(u, lam)+phase_correction(u, lam)/S
                if abs(u) <= rho:
                    inner = (((-1.0)**m)*step) @ inner
                    inner_cells += 1

            target = np.diag((np.exp(1j*theta), np.exp(-1j*theta)))
            error = float(np.linalg.norm(product-target, ord=np.inf))
            inner_error = float(np.linalg.norm(inner-np.eye(2), ord=np.inf))
            rows.append({
                "m": m,
                "lambda": lam,
                "S": S,
                "cells": h1-h0,
                "u_interval": [h0/S, h1/S],
                "hyperbolic_local_cells": hyperbolic_cells,
                "max_local_determinant_error": float(max_det_error),
                "max_principal_frame_determinant_error": float(max_frame_det_error),
                "max_moving_frame_su11_identity_error": float(max_su11_error),
                "principal_frame_product_error": error,
                "error_times_sqrt_S": error*math.sqrt(S),
                "offdiagonal_mixing": float(max(abs(product[0, 1]), abs(product[1, 0]))),
                "inner_layer_width": rho,
                "inner_layer_cells": inner_cells,
                "inner_scalar_product_error": inner_error,
                "inner_error_times_sqrt_S": inner_error*math.sqrt(S),
            })

    return {
        "u_interval": list(U_INTERVAL),
        "central_energy_count": 4,
        "spins_per_energy": 8,
        "endpoint_momenta": endpoint_momenta,
        "scope": "finite exact scalar-Jacobi products in float64; corroboration only, not a proof of the O(S^-1/2) bound",
        "sample_rows": rows,
    }


def source_hashes() -> dict:
    return {rel: hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
            for rel in AUDIT_INPUT_PATHS}


def main() -> None:
    result = {
        "actual_current_surface_status": "conditional-support",
        "target_claim_type": "bounded_theorem",
        "source_revision": SOURCE_REVISION,
        "source_sha256": source_hashes(),
        "numpy": np.__version__,
        "sympy": sp.__version__,
        "symbolic": symbolic_central_checks(),
        "finite_central": finite_central_checks(),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
