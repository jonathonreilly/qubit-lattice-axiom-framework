#!/usr/bin/env python3
"""Exact local-symbol algebra and finite-spin checks for the 15-cell Jacobi wall.

The symbolic calculation is conditional on the supplied integer-spin hop map.
It identifies local cell bands and their first subprincipal resonant coupling;
it does not propagate the actual initial state or prove a fixed-time limit.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 3600

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("zero_mode", HERE / "zero_mode_profile.py")
zero_mode = importlib.util.module_from_spec(spec)
spec.loader.exec_module(zero_mode)
spec2 = importlib.util.spec_from_file_location("spectral", HERE / "spectral_fixed_time_probe.py")
spectral = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(spectral)

SIDES = {
    "+": (zero_mode.POS_LEFT, zero_mode.POS_RIGHT, -3),
    "-": (zero_mode.NEG_LEFT, zero_mode.NEG_RIGHT, +3),
}


def alpha(offset: int, u):
    """First 1/S coefficient of R_(uS+offset)/C, C=S(S+1)."""
    return u**2 - u * (2 * offset + 1)


def cell_coefficients(side: str, u):
    left, right, wrap = SIDES[side]
    offdiag = [(alpha(left[r], u) + alpha(right[r], u)) / 2
               for r in range(15)]
    previous_right = [right[(r - 1) % 15] for r in range(15)]
    previous_right[0] = right[14] + wrap
    diagonal = [alpha(left[r], u) + alpha(previous_right[r], u)
                for r in range(15)]
    return diagonal, offdiag


def band_matrix_element(diagonal, offdiag, theta, ell, ell_prime):
    q = (theta + 2 * sp.pi * ell) / 15
    q_prime = (theta + 2 * sp.pi * ell_prime) / 15
    # Matrix element <v_q|N|v_q'> for v_q[r]=exp(i*q*r)/sqrt(15).
    total = sum(
        sp.exp(sp.I * (q_prime - q) * r)
        * (diagonal[r] - offdiag[r] * (sp.exp(sp.I * q_prime) + sp.exp(-sp.I * q)))
        for r in range(15)
    ) / 15
    return sp.simplify(sp.expand_complex(total))


def projected_crossing(side: str, theta, ell: int, ell_prime: int):
    u = sp.symbols("u", real=True)
    diagonal, offdiag = cell_coefficients(side, u)
    matrix = sp.Matrix([
        [band_matrix_element(diagonal, offdiag, theta, ell, ell),
         band_matrix_element(diagonal, offdiag, theta, ell, ell_prime)],
        [band_matrix_element(diagonal, offdiag, theta, ell_prime, ell),
         band_matrix_element(diagonal, offdiag, theta, ell_prime, ell_prime)],
    ]).applyfunc(sp.simplify)
    return u, matrix


def verify_symbolic_resonances():
    u = sp.symbols("u", real=True)
    expected = {
        ("+", 0): sp.Matrix([
            [u * (3 * u - 11), 2 * u * (1 + sp.sqrt(3) * sp.I) / 5],
            [2 * u * (1 - sp.sqrt(3) * sp.I) / 5, u * (3 * u - 11)],
        ]),
        ("-", 0): sp.Matrix([
            [u * (3 * u + 11), 2 * u * (-1 - sp.sqrt(3) * sp.I) / 5],
            [2 * u * (-1 + sp.sqrt(3) * sp.I) / 5, u * (3 * u + 11)],
        ]),
        ("+", 1): sp.Matrix([
            [u * (5 * u - 17) / 5, 2 * u * (3 - sp.sqrt(3) * sp.I) / 15],
            [2 * u * (3 + sp.sqrt(3) * sp.I) / 15, u * (5 * u - 17) / 5],
        ]),
        ("-", 1): sp.Matrix([
            [u * (5 * u + 17) / 5, -2 * u * (3 - sp.sqrt(3) * sp.I) / 15],
            [-2 * u * (3 + sp.sqrt(3) * sp.I) / 15, u * (5 * u + 17) / 5],
        ]),
    }
    cases = (("+", 0, 5, 10), ("-", 0, 5, 10),
             ("+", 1, 12, 2), ("-", 1, 12, 2))
    results = []
    for side, zone, ell, ell_prime in cases:
        theta = sp.Integer(0) if zone == 0 else sp.pi
        _, matrix = projected_crossing(side, theta, ell, ell_prime)
        target = expected[(side, zone)]
        if any(sp.simplify(matrix[r, c] - target[r, c]) != 0
               for r in range(2) for c in range(2)):
            raise ArithmeticError((side, zone, matrix, target))
        coupling = sp.simplify(sp.Abs(matrix[0, 1]))
        gap_coefficient = sp.simplify(2 * coupling)
        results.append({
            "side": side,
            "reduced_zone_boundary": "theta=0" if zone == 0 else "theta=pi",
            "bands": [ell, ell_prime],
            "projected_first_order_matrix": [
                [str(matrix[r, c]) for c in range(2)] for r in range(2)
            ],
            "coupling_magnitude": str(coupling),
            "local_eigenvalue_gap_coefficient_before_1_over_S": str(gap_coefficient),
        })
    return results


def verify_principal_bands():
    maximum_error = 0.0
    samples = 0
    for u in (0.13, 0.41, 0.77):
        w = 1 - u * u
        for theta in (0.0, 0.37, 1.9, np.pi, 5.4):
            matrix = np.zeros((15, 15), dtype=complex)
            matrix[np.diag_indices(15)] = 2 * w
            for r in range(14):
                matrix[r, r + 1] = matrix[r + 1, r] = -w
            matrix[0, 14] = -w * np.exp(-1j * theta)
            matrix[14, 0] = -w * np.exp(1j * theta)
            q = (theta + 2 * np.pi * np.arange(15)) / 15
            expected = np.sort(2 * w - 2 * w * np.cos(q))
            error = float(np.max(np.abs(np.linalg.eigvalsh(matrix) - expected)))
            maximum_error = max(maximum_error, error)
            samples += 1
    if maximum_error > 2e-12:
        raise ArithmeticError(("principal Bloch bands", maximum_error))
    return {"samples": samples, "maximum_eigenvalue_error": maximum_error}


def verify_finite_spin_expansion():
    rows = []
    global_max = 0.0
    spins = (64, 128, 256, 512, 1024)
    for spin in spins:
        lo, hi, diagonal, offdiag = spectral.finite_spin_m(spin)
        h = 1 / spin
        side_maxima = {}
        for side, (left, right, wrap) in SIDES.items():
            cell = round(0.43 * spin / 3)
            u = 3 * cell / spin
            previous_right = [right[(r - 1) % 15] for r in range(15)]
            previous_right[0] = right[14] + wrap
            max_residual = 0.0
            for r in range(15):
                n = 15 * cell + r if side == "+" else -15 * cell + r
                if n < lo or n >= hi:
                    continue
                b1 = (alpha(left[r], u) + alpha(right[r], u)) / 2
                d1 = alpha(left[r], u) + alpha(previous_right[r], u)
                index = n - lo
                w = 1 - u * u
                residuals = (
                    spin * spin * (diagonal[index] - (2 * w + h * d1)),
                    spin * spin * (offdiag[index] - (w + h * b1)),
                )
                max_residual = max(max_residual, *(abs(x) for x in residuals))
            if max_residual > 100:
                raise ArithmeticError((spin, side, "1/S cell expansion", max_residual))
            side_maxima[side] = max_residual
            global_max = max(global_max, max_residual)
        rows.append({"S": spin, "max_S2_scaled_remainder_by_side": side_maxima})
    return {"spins": rows, "global_max_S2_scaled_remainder": global_max}


def main():
    resonances = verify_symbolic_resonances()
    w = sp.symbols("w", real=True)
    x, q = sp.symbols("x q", real=True)
    gap = 2 * sp.sqrt(3) * (1 - x * x) * sp.sin(q + sp.pi / 3)
    dx = sp.diff(gap, x)
    dq = sp.diff(gap, q) / 15
    hessian_q = sp.hessian(gap, (x, q))
    hessian = sp.Matrix([
        [hessian_q[0, 0], hessian_q[0, 1] / 15],
        [hessian_q[1, 0] / 15, hessian_q[1, 1] / 225],
    ])
    stationary_det = sp.simplify(hessian.subs({x: 0, q: sp.pi / 6}).det())
    if sp.simplify(dx.subs({x: 0, q: sp.pi / 6})) != 0:
        raise ArithmeticError("principal stationary x derivative")
    if sp.simplify(dq.subs({x: 0, q: sp.pi / 6})) != 0:
        raise ArithmeticError("principal stationary Bloch derivative")
    if stationary_det != sp.Rational(8, 75):
        raise ArithmeticError(("principal stationary Hessian", stationary_det))

    output = {
        "claim_status": "conditional local-cell symbol theorem; no full propagator asymptotic is claimed",
        "source_revision": "1c9a243e9b393520183bb06600dec3da9182371a",
        "source_note": "docs/FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md",
        "source_note_sha256": "d235b264783de82bd563d17c217c0b3bc22718638223106215ae43edfd7dbb23",
        "operator": "N_S=J M_S J with M_S=A_S^* A_S and J|n>=(-1)^n|n>",
        "cell_coordinates": "positive n=15k+r uses u=3k/S; negative n=-15K+r uses u=3K/S; r=0,...,14",
        "casimir_factor": "R_m/C with R_m=C-m(m+1), C=S(S+1)",
        "exact_scalar_expansion": "R_(uS+a)/C = (1-u^2) + S^-1*(u^2-u*(2a+1)) - S^-2*(u-a)*(u-a-1)/(1+S^-1)",
        "principal_cell_symbol": "2*(1-u^2)-2*(1-u^2)*cos(q)",
        "folded_bands": "nu_l(u,theta)=2*(1-u^2)-2*(1-u^2)*cos((theta+2*pi*l)/15), l=0,...,14",
        "mod3_character": "V|n>=exp(2*pi*i*n/3)|n>; in a 15-cell it maps band l to l+5 modulo 15",
        "principal_mod3_band_gap": "2*sqrt(3)*(1-u^2)*sin(q_l+pi/3)",
        "principal_phase_stationary_set": "the only interior critical points in signed x are x=0 and q=pi/6 or 7*pi/6; their Hessian determinant is 8/75, but x=0 is the positive/negative cell seam and outer subprincipal expansions do not give its inner matching",
        "first_subprincipal_arrays": {
            "positive_diagonal": "d1_r=alpha(L_r^+)+alpha(R_(r-1)^+), with R_(-1)^+=R_14^+-3",
            "negative_diagonal": "d1_r=alpha(L_r^-)+alpha(R_(r-1)^-), with R_(-1)^-=R_14^-+3",
            "both_offdiagonal": "b1_r=(alpha(L_r)+alpha(R_r))/2",
            "alpha": "alpha(a)=u^2-u*(2a+1); N_S has offdiagonal -b1/S",
        },
        "mod3_resonant_crossings": resonances,
        "finite_spin_coefficient_expansion_check": verify_finite_spin_expansion(),
        "principal_bloch_matrix_check": verify_principal_bands(),
        "phase_scale": "the local avoided-crossing gap is kappa(u)/S+O(S^-2); under exp(-it*(N_S^2-C*N_S)) its phase splitting is t*kappa(u)*S+O(1) for fixed u>0",
        "limits": "The subprincipal resonance cannot be discarded at fixed laboratory time. This local frozen-cell calculation is not a full-operator gap theorem, WKB estimate, initial-state propagation result, or fixed-time limit. The central layer u=O(1/S), boundaries u near 1, electric tails, and H4/output/domain comparison remain open.",
    }
    target = HERE / "MOVING_INDEX_CELL_SYMBOL_RESULTS.json"
    target.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
