#!/usr/bin/env python3
"""Check the regular-arc five-site transfer phase through S^-2.

The symbolic checks derive the coefficient convolution from the exact
five-site Jacobi entries. Finite-spin products corroborate the local
expansion and the exact regrouping into three shifted five-site cells. This
runner does not prove global quantization, slow transport, or a readout limit.
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
)
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUTPUT = ROOT / "outputs" / "postmark_moving_index_2026_09_24" / "FIVE_SITE_TRANSFER_PHASE_EXPANSION_RESULTS.json"
SOURCE_REVISION = "0e6ad8285096ed668816f18caaa6fbbfbd9c50e8"

ELL = (0, 1, 0, 1, 1)
RHO = (0, 0, 0, 1, 0)
PI = (-1, 0, 0, 0, 1)


def f(m: int) -> int:
    return m * (m + 1)


def p5_polynomial(u, z):
    return (
        160*u**4*z**5 - 320*u**4*z**4 + 100*u**4*z**3 + 120*u**4*z**2 - 60*u**4*z
        - 720*u**3*z**5 + 1232*u**3*z**4 - 188*u**3*z**3 - 516*u**3*z**2
        + 183*u**3*z + 9*u**3
        + 832*u**2*z**5 - 1168*u**2*z**4 - 84*u**2*z**3 + 556*u**2*z**2
        - 102*u**2*z - 25*u**2
        - 144*u*z**5 + 128*u*z**4 + 108*u*z**3 - 96*u*z**2 - 9*u*z + 8*u
        + 64*z**5 - 64*z**4 - 48*z**3 + 48*z**2 + 4*z - 4
    )


def alpha(u, a):
    return u**2 - u * (2*a + 1)


def beta(u, a):
    return -a * (a + 1) + u * (2*a + 1) - u**2


def symbolic_expansion() -> dict:
    u, z, eps = sp.symbols("u z eps", real=True)
    w = 1 - u**2
    A = sp.Matrix([[2*z, 1], [-1, 0]])
    p0, p1, p2 = sp.eye(2), sp.zeros(2), sp.zeros(2)

    for s in range(5):
        r_left = 1 - (u + ELL[s]*eps) * (u + (ELL[s] + 1)*eps) / (1 + eps)
        r_right = 1 - (u + RHO[s]*eps) * (u + (RHO[s] + 1)*eps) / (1 + eps)
        r_previous = 1 - (u + PI[s]*eps) * (u + (PI[s] + 1)*eps) / (1 + eps)
        for a, exact_r in ((ELL[s], r_left), (RHO[s], r_right), (PI[s], r_previous)):
            expected_r = w + alpha(u, a)*eps + beta(u, a)*eps**2
            if sp.series(exact_r - expected_r, eps, 0, 3).removeO() != 0:
                raise ArithmeticError(("Casimir coefficient expansion", s, a))

        b = (alpha(u, ELL[s]) + alpha(u, RHO[s])) / 2
        c = ((beta(u, ELL[s]) + beta(u, RHO[s])) / 2
             - (alpha(u, ELL[s]) - alpha(u, RHO[s]))**2 / (8*w))
        d1 = alpha(u, ELL[s]) + alpha(u, PI[s])
        d2 = beta(u, ELL[s]) + beta(u, PI[s])
        link_square_residual = sp.series(
            (w + b*eps + c*eps**2)**2 - r_left*r_right, eps, 0, 3
        ).removeO()
        if sp.factor(link_square_residual) != 0:
            raise ArithmeticError(("square-root link expansion", s, link_square_residual))

        B = sp.Matrix([
            [d1/w - 2*z*b/w, -b/w],
            [-b/w, 0],
        ])
        C = sp.Matrix([
            [d2/w - d1*b/w**2 - 2*z*c/w + 2*z*b**2/w**2,
             -c/w + b**2/w**2],
            [-c/w, 0],
        ])

        # Left multiplication appends the next site transfer: after s=4 this
        # is M_4 M_3 M_2 M_1 M_0, matching the recurrence convention.
        p0, p1, p2 = A*p0, A*p1 + B*p0, A*p2 + B*p1 + C*p0

    tau0 = sp.factor(sp.trace(p0))
    tau1 = sp.factor(sp.trace(p1))
    tau2 = sp.factor(sp.trace(p2))
    t5 = 16*z**5 - 20*z**3 + 5*z
    u4 = 16*z**4 - 12*z**2 + 1
    g1 = u * (5*u*z - 5*u - 9*z + 8) / w
    expected_p5 = p5_polynomial(u, z)
    g2 = sp.factor(-(tau2/2 + t5*g1**2/(2*(1-z**2))) / u4)
    aa, dd, ll = sp.symbols("a d lambda", nonzero=True)
    transfer = sp.Matrix([[(ll-dd)/aa, -1/aa], [aa, 0]])
    checks = {
        "frozen_trace": sp.factor(tau0 - 2*t5),
        "first_order_trace": sp.factor(tau1 + 2*u4*g1),
        "second_order_trace": sp.factor(tau2 - 2*expected_p5/w**2),
        "frozen_cell_determinant": sp.factor(A.det() - 1),
        "exact_site_transfer_determinant": sp.factor(transfer.det() - 1),
        "first_order_phase_inversion": sp.factor(-2*u4*g1 - tau1),
        "second_order_phase_inversion": sp.factor(
            -2*u4*g2 - t5*g1**2/(1-z**2) - tau2),
    }
    if any(value != 0 for value in checks.values()):
        raise ArithmeticError(("five-site trace coefficient", checks))

    return {
        "symbolic_checks": {key: str(value) for key, value in checks.items()},
        "tau0": str(tau0),
        "tau1": str(tau1),
        "tau2": str(tau2),
        "P5": str(sp.expand(expected_p5)),
        "g1": str(sp.factor(g1)),
        "g2_definition": "-(tau2/2 + T5(z)*g1^2/(2*(1-z^2)))/U4(z)",
        "uniformity_domain": "u in a compact subset of (-1,1); k in a compact set with |sin(5*k)| bounded below by a positive constant",
        "proof_role": "exact symbolic coefficient identity; compactness/Taylor and implicit-function arguments establish the uniform O(S^-3) statement in the note",
    }


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


def asymptotic_traces(u: float, z: float) -> tuple[float, float, float]:
    w = 1.0 - u*u
    t5 = 16*z**5 - 20*z**3 + 5*z
    u4 = 16*z**4 - 12*z**2 + 1
    g1 = u * (5*u*z - 5*u - 9*z + 8) / w
    P5 = float(p5_polynomial(u, z))
    return 2*t5, -2*u4*g1, 2*P5/(w*w)


def finite_transfer_checks() -> dict:
    trace_rows = []
    max_det_error = 0.0
    max_group_error = 0.0
    max_trace_scaled_remainder = 0.0
    max_phase_scaled_remainder = 0.0
    kappas = []

    for S in (60, 120, 240, 480):
        for u_target in (-0.60, -0.20, 0.0, 0.35, 0.65):
            h = round(S*u_target)
            u = h/S
            w = 1.0 - u*u
            for k in (0.10, 0.20, 0.50):
                z = math.cos(k)
                lam = 2*w*(1-z)
                exact = exact_cell_transfer(S, h, lam)
                tau = float(np.trace(exact))
                tau0, tau1, tau2 = asymptotic_traces(u, z)
                scaled_trace_remainder = S**3 * abs(tau - tau0 - tau1/S - tau2/S**2)
                kappa = abs(math.sin(5*k))
                if not (-2.0 < tau < 2.0):
                    raise ArithmeticError(("regular-arc transfer left elliptic regime", S, h, k, tau))
                phi_exact = math.acos(tau/2.0)
                U4 = 16*z**4 - 12*z**2 + 1
                g1 = u*(5*u*z - 5*u - 9*z + 8)/w
                g2 = -(tau2/2 + (16*z**5 - 20*z**3 + 5*z)*g1**2/(2*(1-z*z)))/U4
                phi_approx = 5*k + g1/(S*math.sin(k)) + g2/(S**2*math.sin(k))
                scaled_phase_remainder = S**3 * abs(phi_exact - phi_approx)
                max_trace_scaled_remainder = max(max_trace_scaled_remainder,
                                                  scaled_trace_remainder)
                max_phase_scaled_remainder = max(max_phase_scaled_remainder,
                                                  scaled_phase_remainder)
                kappas.append(kappa)
                trace_rows.append({
                    "S": S, "h": h, "u": u, "k": k,
                    "abs_sin_5k": kappa,
                    "trace_error_times_S3": scaled_trace_remainder,
                    "phase_error_times_S3": scaled_phase_remainder,
                    "trace_error": scaled_trace_remainder/S**3,
                    "phase_error": scaled_phase_remainder/S**3,
                })
                for s in range(5):
                    T = exact_site_transfer(S, h, s, lam)
                    max_det_error = max(max_det_error, abs(np.linalg.det(T)-1.0))

        # Verify exact regrouping of the actual varying-coefficient 15-site
        # product. The same lambda is used in all three consecutive cells.
        for h in (-round(0.40*S), -round(0.10*S), 0, round(0.30*S)):
            u = h/S
            lam = 2*(1-u*u)*(1-math.cos(0.20))
            m0 = exact_cell_transfer(S, h, lam)
            m1 = exact_cell_transfer(S, h+1, lam)
            m2 = exact_cell_transfer(S, h+2, lam)
            grouped = m2 @ m1 @ m0
            direct = np.eye(2)
            for cell in range(3):
                for s in range(5):
                    direct = exact_site_transfer(S, h+cell, s, lam) @ direct
            error = float(np.linalg.norm(direct-grouped, ord=np.inf))
            max_group_error = max(max_group_error, error)

    if max_det_error > 2e-12 or max_group_error > 2e-11:
        raise ArithmeticError(("exact transfer identities", max_det_error, max_group_error))
    # A wrong/missing second coefficient leaves an O(S^-2) residual, so the
    # 240-to-480 error ratio is near 4 instead of 8 at this held-out sentinel.
    # The exact values are intentionally included in the result, not promoted
    # to a uniform bound; the analytic compactness argument proves that part.
    sentinels = {
        (row["S"], row["k"]): row
        for row in trace_rows if row["h"] == round(0.65*row["S"])
    }
    trace240 = sentinels[(240, 0.10)]
    trace480 = sentinels[(480, 0.10)]
    trace_order_ratio = trace240["trace_error"] / trace480["trace_error"]
    phase_order_ratio = trace240["phase_error"] / trace480["phase_error"]
    if not (6.0 <= trace_order_ratio <= 10.0):
        raise ArithmeticError(("trace remainder fails cubic-order sentinel",
                               trace_order_ratio, trace240, trace480))
    if not (6.0 <= phase_order_ratio <= 10.0):
        raise ArithmeticError(("phase remainder fails cubic-order sentinel",
                               phase_order_ratio, trace240, trace480))
    return {
        "sample_count": len(trace_rows),
        "min_abs_sin_5k": min(kappas),
        "max_abs_det_minus_one": max_det_error,
        "max_15_site_grouping_inf_norm_error": max_group_error,
        "max_trace_remainder_times_S3": max_trace_scaled_remainder,
        "max_phase_remainder_times_S3": max_phase_scaled_remainder,
        "held_out_order_sentinel": {
            "S_values": [240, 480],
            "u_target": 0.65,
            "k": 0.10,
            "trace_error_ratio": trace_order_ratio,
            "phase_error_ratio": phase_order_ratio,
            "accepted_range": [6.0, 10.0],
            "role": "finite-difference discriminator for a missing/wrong S^-2 coefficient; not a proof of uniformity",
        },
        "sample_rows": trace_rows,
        "scope": "finite float64 corroboration only; the uniform remainder follows from the analytic compactness argument in the note",
        "15_site_identity": "M15(h)=M5(h+2) @ M5(h+1) @ M5(h), with the three actual shifted cells",
    }


def source_hashes() -> dict:
    return {
        rel: hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
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
        "transfer_definition": "T_n=[[ (lambda-d_n)/a_n, -1/a_n ],[a_n,0]], det(T_n)=1",
        "symbolic_expansion": symbolic_expansion(),
        "finite_transfer_checks": finite_transfer_checks(),
        "scope_limit": "local frozen five-site eigenphase on regular compact bulk arcs; no slow transport, global quantization, or phase-correlated readout estimate",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
