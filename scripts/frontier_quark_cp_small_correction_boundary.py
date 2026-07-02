#!/usr/bin/env python3
"""
Quark CP small-correction boundary certificate.

Status:
  exact-support boundary for the shipped fitted carrier ratios, plus bounded
  support from a deterministic finite capped-surface scan.

Safe claim:
  The current quark CP-carrier completion should not be described as a small
  perturbative correction to the Schur 1-3 base.  The fitted xi_u and xi_d
  are non-perturbative relative to that base.  A capped parent-slice scan
  also fails to recover the full CKM/J target for common caps R <= 5.

  This does not derive xi_u, xi_d, the comparator targets, or a retained
  quark-mass closure.  It only closes the small-correction interpretation as
  the right reading of the existing bounded completion.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.optimize import differential_evolution

from frontier_quark_cp_carrier_completion import (
    C12_D,
    C12_U,
    C23_D,
    C23_U,
    J_ATLAS,
    R_CT_OBS,
    R_DB,
    R_UC_OBS,
    V_CB_ATLAS,
    V_UB_ATLAS,
    V_US_ATLAS,
    compute_completion_observables,
    solve_completion_surface,
)


AUDIT_TIMEOUT_SEC = 120

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


@dataclass(frozen=True)
class CappedFit:
    cap: float
    rho_u: float
    rho_d: float
    r_uc: float
    r_ct: float
    vus_ratio: float
    vcb_ratio: float
    vub_ratio: float
    j_ratio: float
    max_ckm_or_j_rel_error: float
    objective: float


def base_c13_u(r_uc: float, r_ct: float) -> float:
    return C12_U * C23_U * math.sqrt(r_uc * r_ct)


def base_c13_d() -> float:
    return C12_D * C23_D * math.sqrt(R_DB)


def parent_point_from_capped_coordinates(point: np.ndarray) -> np.ndarray:
    r_uc, r_ct, rho_u, phi_u, rho_d, phi_d = point
    c13_u_base = base_c13_u(r_uc, r_ct)
    c13_d_base = base_c13_d()
    xi_u = rho_u * c13_u_base * complex(math.cos(phi_u), math.sin(phi_u))
    xi_d = rho_d * c13_d_base * complex(math.cos(phi_d), math.sin(phi_d))
    return np.array([r_uc, r_ct, xi_u.real, xi_u.imag, xi_d.real, xi_d.imag], dtype=float)


def capped_objective(point: np.ndarray) -> float:
    try:
        parent_point = parent_point_from_capped_coordinates(point)
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
        ) = compute_completion_observables(parent_point)
    except (ValueError, FloatingPointError):
        return 1.0e20

    r_uc, r_ct = point[:2]
    residuals = np.array(
        [
            (r_uc / R_UC_OBS - 1.0) / 0.01,
            (r_ct / R_CT_OBS - 1.0) / 0.01,
            (vus / V_US_ATLAS - 1.0) / 0.001,
            (vcb / V_CB_ATLAS - 1.0) / 0.001,
            (vub / V_UB_ATLAS - 1.0) / 0.01,
            (jarlskog / J_ATLAS - 1.0) / 0.05,
        ],
        dtype=float,
    )
    return float(np.sum(residuals * residuals))


def solve_capped_surface(cap: float) -> CappedFit:
    bounds = [
        (R_UC_OBS * 0.99, R_UC_OBS * 1.01),
        (R_CT_OBS * 0.99, R_CT_OBS * 1.01),
        (0.0, cap),
        (-math.pi, math.pi),
        (0.0, cap),
        (-math.pi, math.pi),
    ]
    result = differential_evolution(
        capped_objective,
        bounds,
        maxiter=80,
        popsize=12,
        seed=61700 + int(round(100.0 * cap)),
        polish=True,
        tol=1.0e-8,
        workers=1,
    )

    parent_point = parent_point_from_capped_coordinates(result.x)
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
    ) = compute_completion_observables(parent_point)

    ratios = [
        vus / V_US_ATLAS,
        vcb / V_CB_ATLAS,
        vub / V_UB_ATLAS,
        jarlskog / J_ATLAS,
    ]
    max_error = max(abs(ratio - 1.0) for ratio in ratios)
    return CappedFit(
        cap=cap,
        rho_u=float(result.x[2]),
        rho_d=float(result.x[4]),
        r_uc=float(result.x[0]),
        r_ct=float(result.x[1]),
        vus_ratio=float(ratios[0]),
        vcb_ratio=float(ratios[1]),
        vub_ratio=float(ratios[2]),
        j_ratio=float(ratios[3]),
        max_ckm_or_j_rel_error=float(max_error),
        objective=float(result.fun),
    )


def part1_exact_shipped_fit_boundary() -> tuple[float, float, float]:
    print("\n" + "=" * 72)
    print("PART 1: Exact Boundary for the Shipped Completion")
    print("=" * 72)

    result = solve_completion_surface()
    ratio_u = abs(result.xi_u) / result.c13_u_base
    ratio_d = abs(result.xi_d) / result.c13_d_base
    common_cap_required = max(ratio_u, ratio_d)
    xi_u_share_total = abs(result.xi_u) / abs(result.c13_u_total)
    xi_d_share_total = abs(result.xi_d) / abs(result.c13_d_total)

    print(f"\n  xi_u = {result.xi_u.real:+.9f} {result.xi_u.imag:+.9f} i")
    print(f"  xi_d = {result.xi_d.real:+.9f} {result.xi_d.imag:+.9f} i")
    print(f"  c13_u(base) = {result.c13_u_base:.12e}")
    print(f"  c13_d(base) = {result.c13_d_base:.12e}")
    print(f"  |xi_u| / |c13_u(base)| = {ratio_u:.9f}")
    print(f"  |xi_d| / |c13_d(base)| = {ratio_d:.9f}")
    print(f"  common cap R needed to include the shipped pair = {common_cap_required:.9f}")
    print(f"  |xi_u| / |c13_u(total)| = {xi_u_share_total:.9f}")
    print(f"  |xi_d| / |c13_d(total)| = {xi_d_share_total:.9f}")

    check(
        "The shipped up-sector carrier is more than 100 Schur-base units",
        ratio_u > 100.0,
        f"ratio_u = {ratio_u:.6f}",
    )
    check(
        "The shipped down-sector carrier is more than 6 Schur-base units",
        ratio_d > 6.0,
        f"ratio_d = {ratio_d:.6f}",
    )
    check(
        "A common small cap R <= 5 excludes the shipped completion",
        common_cap_required > 100.0,
        f"R_required = {common_cap_required:.6f}",
    )
    check(
        "The added carriers dominate the completed 1-3 coefficients",
        xi_u_share_total > 0.98 and xi_d_share_total > 0.90,
        f"shares = ({xi_u_share_total:.6f}, {xi_d_share_total:.6f})",
    )
    return ratio_u, ratio_d, common_cap_required


def part2_bounded_capped_scan() -> list[CappedFit]:
    print("\n" + "=" * 72)
    print("PART 2: Bounded Capped-Carrier Parent-Slice Scan")
    print("=" * 72)
    print("\n  Scan surface:")
    print("    xi_s = rho_s * c13_s(base) * exp(i phi_s),  0 <= rho_s <= R")
    print("    r_uc and r_ct are allowed to move within +/-1% of the parent comparators.")
    print("    The optimizer is deterministic finite search, not a proof of a global supremum.")

    caps = [1.0, 2.0, 5.0, 10.0, 50.0, 100.0]
    fits = [solve_capped_surface(cap) for cap in caps]

    print("\n  Best-found capped fits:")
    print("    R       rho_u       rho_d       |Vus|/T     |Vcb|/T     |Vub|/T      J/T        max err")
    for fit in fits:
        print(
            f"    {fit.cap:5.1f}"
            f"  {fit.rho_u:10.6f}"
            f"  {fit.rho_d:10.6f}"
            f"  {fit.vus_ratio:10.6f}"
            f"  {fit.vcb_ratio:10.6f}"
            f"  {fit.vub_ratio:10.6f}"
            f"  {fit.j_ratio:10.6f}"
            f"  {fit.max_ckm_or_j_rel_error:10.6f}"
        )

    cap1 = next(fit for fit in fits if fit.cap == 1.0)
    cap2 = next(fit for fit in fits if fit.cap == 2.0)
    cap5 = next(fit for fit in fits if fit.cap == 5.0)
    cap100 = next(fit for fit in fits if fit.cap == 100.0)

    check(
        "All reported capped coordinates obey their declared rho bounds",
        all(fit.rho_u <= fit.cap + 1.0e-7 and fit.rho_d <= fit.cap + 1.0e-7 for fit in fits),
    )
    check(
        "R = 1 perturbative caps recover less than 20% of target J",
        cap1.j_ratio < 0.20,
        f"J/J_target = {cap1.j_ratio:.6f}",
    )
    check(
        "R = 2 caps recover less than 40% of target J",
        cap2.j_ratio < 0.40,
        f"J/J_target = {cap2.j_ratio:.6f}",
    )
    check(
        "R = 5 generous caps still miss target J by more than 35%",
        cap5.j_ratio < 0.65,
        f"J/J_target = {cap5.j_ratio:.6f}",
    )
    check(
        "A near-parent-scale up-sector cap is needed before the scan approaches the target",
        cap100.j_ratio > 0.95 and cap100.max_ckm_or_j_rel_error < 0.03,
        f"R=100 gives J/J_target={cap100.j_ratio:.6f}, max err={cap100.max_ckm_or_j_rel_error:.6f}",
    )
    return fits


def part3_summary(ratio_u: float, ratio_d: float, common_cap_required: float) -> None:
    print("\n" + "=" * 72)
    print("PART 3: Boundary Summary")
    print("=" * 72)
    print("\n  Exact shipped-fit result:")
    print(
        "    the existing xi pair requires sector caps "
        f"rho_u >= {ratio_u:.3f}, rho_d >= {ratio_d:.3f}, "
        f"or a common cap R >= {common_cap_required:.3f}."
    )
    print("\n  Honest interpretation:")
    print("    the quark CP-carrier completion is a bounded non-perturbative")
    print("    carrier ansatz on the parent surface, not a retained small correction.")
    print("\n  Open work unchanged:")
    print("    this runner does not derive xi_u, xi_d, the comparator targets,")
    print("    or a framework-native non-perturbative carrier normalization.")


def main() -> int:
    print("=" * 72)
    print("  FRONTIER: Quark CP Small-Correction Boundary")
    print("=" * 72)

    ratio_u, ratio_d, common_cap_required = part1_exact_shipped_fit_boundary()
    part2_bounded_capped_scan()
    part3_summary(ratio_u, ratio_d, common_cap_required)

    print("\n" + "=" * 72)
    print(f"  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 72)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
