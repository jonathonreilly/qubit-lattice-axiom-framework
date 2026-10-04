#!/usr/bin/env python3
"""Converged thermal selector support on the one-scalar same-surface DM family.

Framework convention:
  "axiom" means only the single framework axiom Cl(3) on Z^3.

Corrigendum 2026-09-30 (Sommerfeld argument):
  The shared thermal helper used S = pi z / (1 - exp(-pi z)), z = alpha / v_rel,
  half the argument the radial Schroedinger equation gives (2 pi z).  The
  archived result of this runner (a unique interior selector sigma = 0.145077,
  alpha = 0.0908995, R = 5.447934) belonged to the half-argument kernel.  With
  the corrected kernel both endpoint images exceed the comparator ratio, so the
  family has NO crossing and the 9/62 clue has no referent.  The checks below
  certify that.  See scripts/dm_sommerfeld_kernel_radial_schrodinger_verification.py.

Purpose:
  Replace the unstable coarse-grid retained thermal runner with a corrected
  high-precision continuum same-surface evaluation on the admitted DM-side
  family, and report whether the family reaches the comparator.

Scope:
  This is support, not theorem-grade closure. It stabilizes the admitted-family
  numerics and shows that the coarse thermal discretization is not what
  separates the family from the comparator.
"""

from __future__ import annotations

# Explicit bounded execution cap; scientific content is unchanged by this metadata.
AUDIT_TIMEOUT_SEC = 120

import sys

from dm_full_closure_minimal_reduced_cycle_extension_map_common import (
    R_BASE_EXACT,
    omega_b_from_eta,
    retained_structural_dm_ratio,
)
from dm_full_closure_same_surface_thermal_support_common import (
    ALPHA_HI,
    ALPHA_LO,
    OMEGA_DM_OBS,
    alpha_sigma,
    converged_comparator_pin,
    converged_same_surface_ratio,
    converged_sigma_root,
)
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


def main() -> int:
    print("=" * 88)
    print("DM FULL CLOSURE SAME-SURFACE CONVERGED THERMAL SELECTOR SUPPORT")
    print("=" * 88)

    omega_b = float(omega_b_from_eta(ETA_OBS))
    r_target = OMEGA_DM_OBS / omega_b
    sigma_struct = float(1.0 / (2.0 * R_BASE_EXACT))
    r_conv_lo = converged_same_surface_ratio(ALPHA_LO)
    r_conv_hi = converged_same_surface_ratio(ALPHA_HI)
    r_coarse_lo = retained_structural_dm_ratio(ALPHA_LO)
    r_coarse_hi = retained_structural_dm_ratio(ALPHA_HI)

    print("\n" + "=" * 88)
    print("PART 1: THE ADMITTED DM FAMILY HAS NO CLOSURE CROSSING (CORRECTED KERNEL)")
    print("=" * 88)
    try:
        converged_sigma_root(omega_b)
        no_root = False
        detail = "a root was returned"
    except ValueError as exc:
        no_root = True
        detail = str(exc)
    check(
        "The converged same-surface kernel has no crossing on sigma in [0,1]: the root is not bracketed",
        no_root,
        detail,
        cls="D",
    )
    check(
        "Both converged endpoint images exceed the comparator ratio",
        r_conv_lo > r_target and r_conv_hi > r_target,
        f"R(alpha_lo)={r_conv_lo:.9f}, R(alpha_hi)={r_conv_hi:.9f}, R_target={r_target:.9f}",
        cls="D",
    )

    print("\n" + "=" * 88)
    print("PART 2: THE COARSE THERMAL GRID IS NOT THE ISSUE, AND THE 9/62 CLUE HAS NO REFERENT")
    print("=" * 88)
    check(
        "The coarse retained grid and the converged evaluator agree at both endpoints far inside the gap to the comparator",
        abs(r_coarse_lo - r_conv_lo) < 1.0e-4 and abs(r_coarse_hi - r_conv_hi) < 1.0e-4,
        f"coarse-converged: alpha_lo {r_coarse_lo - r_conv_lo:+.3e}, alpha_hi {r_coarse_hi - r_conv_hi:+.3e}",
    )
    r_struct = converged_same_surface_ratio(alpha_sigma(sigma_struct))
    check(
        "The converged ratio at the 9/62 point misses the comparator by far more than the archived 9/62 residual",
        abs(r_struct - r_target) > 1.0,
        f"R(sigma=9/62)={r_struct:.9f}, R_target={r_target:.9f}",
    )

    alpha_pin, r_pin = converged_comparator_pin(omega_b)
    print()
    print(f"  R_target          = {r_target:.12f}")
    print(f"  R(alpha_lo) coarse= {r_coarse_lo:.12f}")
    print(f"  R(alpha_lo) conv  = {r_conv_lo:.12f}")
    print(f"  R(alpha_hi) coarse= {r_coarse_hi:.12f}")
    print(f"  R(alpha_hi) conv  = {r_conv_hi:.12f}")
    print(f"  sigma_9/62        = {sigma_struct:.15f}")
    print(f"  R(sigma=9/62)     = {r_struct:.12f}")
    print(f"  comparator pin    = alpha {alpha_pin:.15f} (outside the family, sigma < 0; R = {r_pin:.12f})")

    print("\n" + "=" * 88)
    print("BOTTOM LINE")
    print("=" * 88)
    print("  Honest status:")
    print("    - with the corrected 2 pi kernel the one-scalar same-surface family does NOT")
    print("      reach the comparator: both endpoint images exceed it")
    print("    - the archived unique interior selector and the 9/62 near-coincidence belonged")
    print("      to the half-argument kernel and are superseded")
    print("    - a coupling near the comparator pin above would be a fitted value")
    print("      outside the family, not a selector")
    print("    - current-bank selector closure is still open")

    print("\n" + "=" * 88)
    print(f"SUMMARY: classified_pass={PASS_COUNT} fail={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
