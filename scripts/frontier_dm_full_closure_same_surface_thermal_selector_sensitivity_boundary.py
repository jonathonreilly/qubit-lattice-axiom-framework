#!/usr/bin/env python3
"""Sensitivity boundary for same-surface DM selector claims from the retained thermal kernel.

Framework convention:
  "axiom" means only the single framework axiom Cl(3) on Z^3.

Corrigendum 2026-09-30 (Sommerfeld argument):
  This runner's local Sommerfeld helper used pi * zeta, half the argument the
  radial Schroedinger equation gives (2 pi * zeta, zeta = alpha / v_rel).  The
  archived roots quoted below (sigma_2000 = 0.145161, sigma_4000 = 0.145600,
  sigma_8000 = 0.145585, sigma_16000 = 0.145581) belonged to the half-argument
  kernel.  With the corrected kernel there is no root on sigma in [0, 1] at any
  quadrature resolution, so the 9/62 clue has no referent; the checks below
  certify that and that quadrature is not what separates the family from the
  comparator.  See scripts/dm_sommerfeld_kernel_radial_schrodinger_verification.py.

Purpose:
  Test whether the apparent structural collapse clue

      sigma ~= 1 / (2 R_base) = 9/62

  is robust on the retained same-surface DM kernel, or whether it is an
  artifact of the current coarse thermal averaging implementation.

Answer:
  It is not robust enough to support a selector claim on the current branch.
  With the corrected kernel the family does not reach the comparator at all.
"""

from __future__ import annotations

import sys

import numpy as np

from dm_full_closure_minimal_reduced_cycle_extension_map_common import (
    R_BASE_EXACT,
    SOMMERFELD_ARGUMENT_FACTOR,
    omega_b_from_eta,
    retained_structural_dm_ratio,
)
from dm_full_closure_same_surface_thermal_support_common import ALPHA_HI, ALPHA_LO, OMEGA_DM_OBS
from dm_leptogenesis_exact_common import ETA_OBS

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", cls: str = "C") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{cls}] {status}: {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def sommerfeld(alpha_eff: float, v: float) -> float:
    zeta = alpha_eff / v
    if abs(zeta) < 1.0e-15:
        return 1.0
    y = SOMMERFELD_ARGUMENT_FACTOR * zeta
    if -y > 700.0:
        return 0.0
    return float(y / (1.0 - np.exp(-y)))


def thermal_avg(alpha_eff: float, x_f: float, attractive: bool, npts: int, vmin: float = 0.001, vmax: float = 2.0) -> float:
    v = np.linspace(vmin, vmax, npts)
    weight = v**2 * np.exp(-x_f * v**2 / 4.0)
    sign = 1.0 if attractive else -1.0
    vals = np.array([sommerfeld(sign * alpha_eff, float(v_i)) for v_i in v], dtype=float)
    return float(np.trapezoid(vals * weight, v) / np.trapezoid(weight, v))


def refined_ratio(alpha_s: float, npts: int, vmin: float = 0.001, vmax: float = 2.0) -> float:
    c2_su3 = 4.0 / 3.0
    alpha_1 = c2_su3 * alpha_s
    alpha_8 = (1.0 / 6.0) * alpha_s
    s_1 = thermal_avg(alpha_1, 25.0, attractive=True, npts=npts, vmin=vmin, vmax=vmax)
    s_8 = thermal_avg(alpha_8, 25.0, attractive=False, npts=npts, vmin=vmin, vmax=vmax)
    w_1 = (1.0 / 9.0) * c2_su3**2
    w_8 = (8.0 / 9.0) * (1.0 / 6.0) ** 2
    s_vis = (w_1 * s_1 + w_8 * s_8) / (w_1 + w_8)
    return float(R_BASE_EXACT * s_vis)


def main() -> int:
    print("=" * 88)
    print("DM FULL CLOSURE SAME-SURFACE THERMAL SELECTOR SENSITIVITY BOUNDARY")
    print("=" * 88)

    omega_b = float(omega_b_from_eta(ETA_OBS))
    r_target = OMEGA_DM_OBS / omega_b
    sigma_struct = float(1.0 / (2.0 * R_BASE_EXACT))
    npts_list = (2000, 4000, 8000, 16000)

    print("\n" + "=" * 88)
    print("PART 1: BASELINE ON THE COARSE RETAINED GRID (CORRECTED KERNEL)")
    print("=" * 88)
    r_coarse_lo = retained_structural_dm_ratio(ALPHA_LO)
    r_coarse_hi = retained_structural_dm_ratio(ALPHA_HI)
    check(
        "The coarse retained runner has no crossing on the family: both endpoint images exceed the comparator ratio",
        r_coarse_lo > r_target and r_coarse_hi > r_target,
        f"R(alpha_lo)={r_coarse_lo:.9f}, R(alpha_hi)={r_coarse_hi:.9f}, R_target={r_target:.9f}",
    )

    print("\n" + "=" * 88)
    print("PART 2: QUADRATURE REFINEMENT MOVES THE ENDPOINT IMAGES FAR LESS THAN THEIR GAP TO THE COMPARATOR")
    print("=" * 88)
    r_lo = {n: refined_ratio(ALPHA_LO, n) for n in npts_list}
    r_hi = {n: refined_ratio(ALPHA_HI, n) for n in npts_list}
    spread_lo = max(r_lo.values()) - min(r_lo.values())
    spread_hi = max(r_hi.values()) - min(r_hi.values())
    check(
        "At every refinement the family still lies entirely above the comparator: no root at any resolution",
        all(v > r_target for v in r_lo.values()) and all(v > r_target for v in r_hi.values()),
        f"min R(alpha_lo)={min(r_lo.values()):.9f}, min R(alpha_hi)={min(r_hi.values()):.9f}, R_target={r_target:.9f}",
    )
    check(
        "The refinement spread of the endpoint images is negligible next to their gap to the comparator",
        max(spread_lo, spread_hi) < 1.0e-3 * (min(r_lo.values()) - r_target),
        f"spread(alpha_lo)={spread_lo:.3e}, spread(alpha_hi)={spread_hi:.3e}, gap={min(r_lo.values()) - r_target:.6f}",
    )

    print()
    for n in npts_list:
        print(f"  npts={n:6d}  R(alpha_lo)={r_lo[n]:.12f}  R(alpha_hi)={r_hi[n]:.12f}")
    print(f"  R_target = {r_target:.12f}")
    print(f"  sigma_9/62 = {sigma_struct:.15f}  (no root exists on sigma in [0,1], so the clue has no referent)")

    print("\n" + "=" * 88)
    print("BOTTOM LINE")
    print("=" * 88)
    print("  Honest status:")
    print("    - with the corrected 2 pi kernel the family does not reach the comparator at")
    print("      any quadrature resolution, so there is no selector root to compare with 9/62")
    print("    - the archived apparent 9/62 match and its instability belonged to the")
    print("      half-argument kernel and are superseded")
    print("    - so 9/62 must not be promoted as a DM selector law on the current branch")
    print("    - the exact rational/group skeleton is unaffected; the thermal layer must be")
    print("      re-derived before any selector collapse is attempted")

    print("\n" + "=" * 88)
    print(f"SUMMARY: classified_pass={PASS_COUNT} fail={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
