#!/usr/bin/env python3
"""Historical diagonal-label CP-carrier optimizer with spectrum firewall.

Status:
  bounded numerical CKM+CP match on a diagonal-parameter ansatz

Safe claim:
  The minimal Schur-NNI surface still does not close the CKM CP area; that
  no-go remains in frontier_quark_mass_ratio_full_solve.py.

  If one adds one independent complex 1-3 coordinate in each quark sector,
  the optimizer can match the CKM/J comparators while placing two diagonal
  input labels near observed up-sector mass-ratio comparators.

  The diagonal labels are not the completed matrices' singular-value mass
  ratios.  This runner now checks that mismatch explicitly.  The exact
  spectrum and weak-basis obstruction is verified independently by
  frontier_quark_cp_carrier_spectrum_basis_obstruction.py.

  This is historical bounded fit context, not a physical full-quark closure or
  a derivation of xi_u and xi_d.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass

import numpy as np
from scipy.optimize import differential_evolution, minimize

from frontier_quark_mass_ratio_full_solve import (
    C12_D,
    C12_U,
    C23_D,
    C23_U,
    J_ATLAS,
    R_CT_OBS,
    R_DB,
    R_SB,
    R_UC_OBS,
    V_CB_ATLAS,
    V_UB_ATLAS,
    V_US_ATLAS,
    solve_magnitude_surface,
)


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def wrap_to_pi(angle: float) -> float:
    return ((angle + math.pi) % (2.0 * math.pi)) - math.pi


@dataclass(frozen=True)
class CompletionSolve:
    r_uc: float
    r_ct: float
    xi_u: complex
    xi_d: complex
    c13_u_base: float
    c13_d_base: float
    c13_u_total: complex
    c13_d_total: complex
    vus: float
    vcb: float
    vub: float
    jarlskog: float
    det_phase: float
    objective: float


def build_nni_with_complex_13(
    m1: float,
    m2: float,
    m3: float,
    c12: float,
    c23: float,
    c13_complex: complex,
) -> np.ndarray:
    matrix = np.zeros((3, 3), dtype=complex)
    matrix[0, 0] = m1
    matrix[1, 1] = m2
    matrix[2, 2] = m3
    matrix[0, 1] = c12 * math.sqrt(m1 * m2)
    matrix[1, 0] = np.conj(matrix[0, 1])
    matrix[1, 2] = c23 * math.sqrt(m2 * m3)
    matrix[2, 1] = np.conj(matrix[1, 2])
    matrix[0, 2] = c13_complex * math.sqrt(m1 * m3)
    matrix[2, 0] = np.conj(matrix[0, 2])
    return matrix


def diag_hermitian_square(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    h = matrix @ matrix.conj().T
    eigvals, eigvecs = np.linalg.eigh(h)
    order = np.argsort(eigvals)
    return eigvals[order], eigvecs[:, order]


def compute_completion_observables(
    point: np.ndarray,
) -> tuple[float, float, complex, complex, complex, complex, float, float, float, float, float]:
    r_uc, r_ct, xi_u_re, xi_u_im, xi_d_re, xi_d_im = point
    if r_uc <= 0.0 or r_ct <= 0.0 or r_uc * r_ct >= 1.0:
        raise ValueError("invalid mass-ratio point")

    m_u = r_uc * r_ct
    m_c = r_ct
    m_t = 1.0

    m_d = R_DB
    m_s = R_SB
    m_b = 1.0

    c13_u_base = C12_U * C23_U * math.sqrt(m_u / m_t)
    c13_d_base = C12_D * C23_D * math.sqrt(m_d / m_b)
    xi_u = complex(xi_u_re, xi_u_im)
    xi_d = complex(xi_d_re, xi_d_im)
    c13_u_total = c13_u_base + xi_u
    c13_d_total = c13_d_base + xi_d

    m_u_matrix = build_nni_with_complex_13(m_u, m_c, m_t, C12_U, C23_U, c13_u_total)
    m_d_matrix = build_nni_with_complex_13(m_d, m_s, m_b, C12_D, C23_D, c13_d_total)

    _, u_u = diag_hermitian_square(m_u_matrix)
    _, u_d = diag_hermitian_square(m_d_matrix)
    v = u_u.conj().T @ u_d

    vus = abs(v[0, 1])
    vcb = abs(v[1, 2])
    vub = abs(v[0, 2])
    jarlskog = abs(np.imag(v[0, 1] * v[1, 2] * np.conj(v[0, 2]) * np.conj(v[1, 1])))

    det_prod = np.linalg.det(m_u_matrix) * np.linalg.det(m_d_matrix)
    det_phase = abs(wrap_to_pi(cmath.phase(det_prod)))

    return (
        c13_u_base,
        c13_d_base,
        xi_u,
        xi_d,
        c13_u_total,
        c13_d_total,
        vus,
        vcb,
        vub,
        jarlskog,
        det_phase,
    )


def completion_objective(point: np.ndarray) -> float:
    try:
        (
            _c13_u_base,
            _c13_d_base,
            _xi_u,
            _xi_d,
            _c13_u_total,
            _c13_d_total,
            vus,
            vcb,
            vub,
            jarlskog,
            _det_phase,
        ) = compute_completion_observables(point)
    except ValueError:
        return 1.0e12

    r_uc, r_ct = point[:2]
    residuals = np.array(
        [
            (r_uc - R_UC_OBS) / 1.0e-4,
            (r_ct - R_CT_OBS) / 1.0e-4,
            (vus - V_US_ATLAS) / 1.0e-4,
            (vcb - V_CB_ATLAS) / 1.0e-4,
            (vub - V_UB_ATLAS) / 1.0e-4,
            (jarlskog - J_ATLAS) / 2.0e-6,
        ],
        dtype=float,
    )
    return float(np.sum(residuals**2))


def solve_completion_surface() -> CompletionSolve:
    bounds = [
        (5.0e-4, 5.0e-3),
        (4.0e-3, 2.0e-2),
        (-0.5, 0.5),
        (-0.5, 0.5),
        (-0.5, 0.5),
        (-0.5, 0.5),
    ]

    global_result = differential_evolution(
        completion_objective,
        bounds,
        maxiter=120,
        popsize=20,
        seed=13,
        polish=False,
    )

    seeds = [
        global_result.x,
        np.array([R_UC_OBS, R_CT_OBS, 0.34, -0.06, 0.08, 0.11], dtype=float),
        np.array([R_UC_OBS, R_CT_OBS, 0.10, 0.10, 0.05, -0.10], dtype=float),
    ]

    best_x: np.ndarray | None = None
    best_fun: float | None = None
    for seed in seeds:
        result = minimize(
            completion_objective,
            seed,
            method="L-BFGS-B",
            bounds=bounds,
            options={"maxiter": 1000},
        )
        if best_fun is None or result.fun < best_fun:
            best_x = result.x
            best_fun = float(result.fun)

    assert best_x is not None and best_fun is not None

    (
        c13_u_base,
        c13_d_base,
        xi_u,
        xi_d,
        c13_u_total,
        c13_d_total,
        vus,
        vcb,
        vub,
        jarlskog,
        det_phase,
    ) = compute_completion_observables(best_x)

    return CompletionSolve(
        r_uc=float(best_x[0]),
        r_ct=float(best_x[1]),
        xi_u=xi_u,
        xi_d=xi_d,
        c13_u_base=c13_u_base,
        c13_d_base=c13_d_base,
        c13_u_total=c13_u_total,
        c13_d_total=c13_d_total,
        vus=vus,
        vcb=vcb,
        vub=vub,
        jarlskog=jarlskog,
        det_phase=det_phase,
        objective=best_fun,
    )


def part1_anchor() -> tuple[float, float]:
    print("\n" + "=" * 72)
    print("PART 1: Minimal-Surface Anchor")
    print("=" * 72)

    anchor = solve_magnitude_surface()
    anchor_ratio = anchor.jarlskog / J_ATLAS

    print(f"\n  minimal-surface m_u/m_c = {anchor.r_uc:.6e}")
    print(f"  minimal-surface m_c/m_t = {anchor.r_ct:.6e}")
    print(f"  minimal-surface |V_us|  = {anchor.vus:.6f}")
    print(f"  minimal-surface |V_cb|  = {anchor.vcb:.6f}")
    print(f"  minimal-surface |V_ub|  = {anchor.vub:.6f}")
    print(f"  minimal-surface J       = {anchor.jarlskog:.6e}")
    print(f"  minimal-surface J/J_atlas = {anchor_ratio:.6f}")

    check(
        "The minimal Schur-NNI anchor still under-produces J by more than 5x",
        J_ATLAS / anchor.jarlskog > 5.0,
        f"factor = {J_ATLAS / anchor.jarlskog:.2f}",
    )
    return anchor.jarlskog, anchor_ratio


def part2_completion(result: CompletionSolve, anchor_j: float) -> None:
    print("\n" + "=" * 72)
    print("PART 2: Historical Complex 1-3 Coordinate Fit And Spectrum Firewall")
    print("=" * 72)

    dev_uc = (result.r_uc / R_UC_OBS - 1.0) * 100.0
    dev_ct = (result.r_ct / R_CT_OBS - 1.0) * 100.0
    xi_u_mag = abs(result.xi_u)
    xi_d_mag = abs(result.xi_d)
    xi_u_phase = math.degrees(cmath.phase(result.xi_u))
    xi_d_phase = math.degrees(cmath.phase(result.xi_d))

    print("\n  Solved diagonal input labels (not physical singular-value ratios):")
    print(f"    r_uc(label) = {result.r_uc:.6e}  (comparator: {R_UC_OBS:.6e}, dev: {dev_uc:+.2f}%)")
    print(f"    r_ct(label) = {result.r_ct:.6e}  (comparator: {R_CT_OBS:.6e}, dev: {dev_ct:+.2f}%)")
    print()
    print("  Added complex carriers:")
    print(f"    xi_u = {result.xi_u.real:+.6f} {result.xi_u.imag:+.6f} i")
    print(f"      |xi_u| = {xi_u_mag:.6f}, phase = {xi_u_phase:.3f} deg")
    print(f"    xi_d = {result.xi_d.real:+.6f} {result.xi_d.imag:+.6f} i")
    print(f"      |xi_d| = {xi_d_mag:.6f}, phase = {xi_d_phase:.3f} deg")
    print()
    print("  Schur base vs completed 1-3 coefficients:")
    print(f"    c13_u(base)  = {result.c13_u_base:.6e}")
    print(f"    c13_u(total) = {result.c13_u_total.real:+.6f} {result.c13_u_total.imag:+.6f} i")
    print(f"    c13_d(base)  = {result.c13_d_base:.6e}")
    print(f"    c13_d(total) = {result.c13_d_total.real:+.6f} {result.c13_d_total.imag:+.6f} i")
    print()
    print("  Completed CKM surface:")
    print(f"    |V_us| = {result.vus:.9f}")
    print(f"    |V_cb| = {result.vcb:.9f}")
    print(f"    |V_ub| = {result.vub:.9f}")
    print(f"    J      = {result.jarlskog:.9e}")
    print(f"    arg det(M_u M_d) = {result.det_phase:.3e} rad")
    print(f"    objective score  = {result.objective:.6f}")
    print(f"    J improvement over anchor = {result.jarlskog / anchor_j:.3f}x")

    up_matrix = build_nni_with_complex_13(
        result.r_uc * result.r_ct,
        result.r_ct,
        1.0,
        C12_U,
        C23_U,
        result.c13_u_total,
    )
    up_singular = np.sort(np.linalg.svd(up_matrix, compute_uv=False))
    physical_r_uc = float(up_singular[0] / up_singular[1])
    physical_r_ct = float(up_singular[1] / up_singular[2])
    print()
    print("  Physical singular-spectrum diagnostic:")
    print(f"    sigma_u/sigma_c = {physical_r_uc:.9e}")
    print(f"    sigma_c/sigma_t = {physical_r_ct:.9e}")

    check(
        "Physical sigma_u/sigma_c is not the fitted diagonal-label ratio",
        abs(physical_r_uc / R_UC_OBS - 1.0) > 0.01,
        f"ratio to comparator = {physical_r_uc / R_UC_OBS:.6f}",
    )
    check(
        "Physical sigma_c/sigma_t is not the fitted diagonal-label ratio",
        abs(physical_r_ct / R_CT_OBS - 1.0) > 0.01,
        f"ratio to comparator = {physical_r_ct / R_CT_OBS:.6f}",
    )
    check(
        "Coordinate fit matches |V_us| within 0.01%",
        abs(result.vus / V_US_ATLAS - 1.0) < 1.0e-4,
        f"ratio = {result.vus / V_US_ATLAS:.8f}",
    )
    check(
        "Coordinate fit matches |V_cb| within 0.05%",
        abs(result.vcb / V_CB_ATLAS - 1.0) < 5.0e-4,
        f"ratio = {result.vcb / V_CB_ATLAS:.8f}",
    )
    check(
        "Coordinate fit matches |V_ub| within 0.2%",
        abs(result.vub / V_UB_ATLAS - 1.0) < 2.0e-3,
        f"ratio = {result.vub / V_UB_ATLAS:.8f}",
    )
    check(
        "Coordinate fit matches J within 1%",
        abs(result.jarlskog / J_ATLAS - 1.0) < 0.01,
        f"ratio = {result.jarlskog / J_ATLAS:.8f}",
    )
    check(
        "The Hermitian fit has positive determinant product and zero phase mod 2pi",
        result.det_phase < 1.0e-10,
        f"arg det(M_u M_d) = {result.det_phase:.3e}",
    )
    check(
        "The fitted complex coordinates are genuinely nonzero",
        abs(result.xi_u) > 1.0e-3 and abs(result.xi_d) > 1.0e-3,
        f"|xi_u| = {abs(result.xi_u):.3e}, |xi_d| = {abs(result.xi_d):.3e}",
    )
    check(
        "The fitted ansatz lifts J by more than a factor of 6 over the anchor",
        result.jarlskog / anchor_j > 6.0,
        f"lift = {result.jarlskog / anchor_j:.3f}x",
    )
    check(
        "The added carrier is not a perturbative tweak of the Schur base",
        abs(result.xi_u) / result.c13_u_base > 10.0 and abs(result.xi_d) / result.c13_d_base > 5.0,
        f"ratios = ({abs(result.xi_u) / result.c13_u_base:.2f}, {abs(result.xi_d) / result.c13_d_base:.2f})",
    )


def part3_summary(result: CompletionSolve) -> None:
    print("\n" + "=" * 72)
    print("PART 3: Summary")
    print("=" * 72)

    print("\n  Honest endpoint:")
    print("    complex 1-3 coordinates can fit the CKM/J comparator surface together")
    print("    with diagonal labels placed near mass-ratio comparators, but the completed")
    print("    matrices do not reproduce those physical singular-value mass ratios")
    print()
    print("  Honest caveat:")
    print("    the added carrier dominates the bare Schur 1-3 term, especially in the up sector,")
    print("    so this is neither a small retained correction nor a full-quark completion")


def main() -> int:
    print("=" * 72)
    print("  FRONTIER: Historical Quark CP-Carrier Diagonal-Label Fit")
    print("=" * 72)

    anchor_j, _anchor_ratio = part1_anchor()
    completion = solve_completion_surface()
    part2_completion(completion, anchor_j)
    part3_summary(completion)

    print("\n" + "=" * 72)
    print(f"  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 72)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
