#!/usr/bin/env python3
"""Supplied-premise interval-composition theorem for the DM thermal layer.

Framework convention:
  "axiom" means only the single framework axiom Cl(3) on Z^3.

Corrigendum 2026-09-30 (Sommerfeld argument):
  The shared thermal helper used S = pi z / (1 - exp(-pi z)) with z = alpha / v
  for the RELATIVE speed v of the weight v^2 exp(-x_f v^2 / 4).  The radial
  Schroedinger equation gives 2 pi z.  With the corrected kernel both endpoint
  images lie ABOVE the comparator ratio, so the previously reported target
  bracketing and certified one-scalar root (sigma = 0.14508) do not exist.
  Parts 2 and 3 below now certify that absence.  See
  scripts/dm_sommerfeld_kernel_radial_schrodinger_verification.py.

Purpose:
  Verify the visible interval arithmetic and endpoint disjointness, and certify
  the target position relative to the endpoint images and the absence (or
  presence) of a one-scalar root, after the upstream/helper packet
  supplies:

    1. continuum integral representation,
    2. monotonicity in the selected coupling,
    3. positive-series / tail enclosures,
    4. the 64:1 same-surface channel-weight bridge,
    5. the live-DM plaquette / eta-omega constants,
    6. the packet-completeness / selector premise.

Scope:
  - current-bank selector closure still fails;
  - the runner-grade gain is a certified supplied-premise interval theorem;
  - this runner does not derive the live-DM premise packet from framework
    primitives.
"""

from __future__ import annotations


# The audit-lane cache policy reads this declaration before refreshing stdout.
# Keep the ceiling at the repair target so regressions to slow thermal
# summation surface as compute breakage instead of claiming a long-run budget.
AUDIT_TIMEOUT_SEC = 60

import sys
from pathlib import Path
import json

from dm_full_closure_minimal_reduced_cycle_extension_map_common import omega_b_from_eta
from dm_full_closure_same_surface_thermal_support_common import (
    ALPHA_HI,
    ALPHA_LO,
    OMEGA_DM_OBS,
    certified_same_surface_ratio_bounds,
    certified_sigma_interval,
    converged_same_surface_ratio,
)
from dm_leptogenesis_exact_common import ETA_OBS

PASS_COUNT = 0
FAIL_COUNT = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17.md"
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"

# Root coupling reported by the archived half-argument (pi) kernel, superseded
# by the 2026-09-30 corrigendum (sigma = 0.145077095756643 on the family).
ARCHIVED_PI_FORM_ROOT_ALPHA = 0.090899546858439

CURRENT_ONE_HOP_AUTHORITIES = {
    "dm_full_closure_same_surface_thermal_integral_representation_theorem_note_2026-04-16": "retained_bounded",
    "dm_full_closure_same_surface_thermal_monotonicity_theorem_note_2026-04-17": "retained_bounded",
    "dm_full_closure_same_surface_thermal_series_tail_support_note_2026-04-17": "retained_bounded",
    "dm_full_closure_64_to_1_channel_weight_bridge_narrow_theorem_note_2026-06-02": "retained_bounded",
}


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def part0_source_scope_boundary() -> None:
    print("\n" + "=" * 88)
    print("PART 0: SOURCE-NOTE SCOPE BOUNDARY")
    print("=" * 88)
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "**Claim type:** open_gate / conditional-support interval-composition certificate",
        "**Type:** conditional / support",
        "2026-06-12 audit firewall: supplied-premise support only",
        "supplied-premise boundary",
        "This row does not derive",
        "premise packet from framework primitives",
        "Open upstream gaps registered",
    ]
    forbidden = [
        "source-note proposal only",
        "actual_" + "current_surface_status",
        "bare_" + "ret" + "ained",
        "**Claim type:** bounded support note",
        "**Claim type:** bounded_theorem",
    ]
    for phrase in required:
        check(f"source contains required boundary phrase: {phrase}", phrase in text)
    for phrase in forbidden:
        check(f"source omits forbidden control phrase: {phrase}", phrase not in text)

    check(
        "source records the 2026-06-07 current-authority reduction",
        "2026-06-07 Current Authority Reduction" in text,
    )
    check(
        "source carries the 2026-09-30 Sommerfeld-argument corrigendum",
        "Corrigendum (2026-09-30)" in text,
    )
    check(
        "source no longer treats the 64:1 bridge as an open gap",
        "The 64:1 channel-weight bridge is no longer an open parent import" in text,
    )
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    for claim_id, expected_status in CURRENT_ONE_HOP_AUTHORITIES.items():
        row = ledger.get(claim_id, {})
        check(
            f"one-hop authority is audited_clean/{expected_status}: {claim_id}",
            row.get("audit_status") == "audited_clean"
            and row.get("effective_status") == expected_status,
            f"audit_status={row.get('audit_status')} effective_status={row.get('effective_status')}",
        )


def part1_current_bank_certified_bounds() -> tuple[float, float, float, float, float]:
    print("\n" + "=" * 88)
    print("PART 1: CERTIFIED CURRENT-BANK THERMAL ENVELOPES")
    print("=" * 88)

    r_lo_lo, r_lo_hi, att_lo, rep_lo = certified_same_surface_ratio_bounds(ALPHA_LO)
    r_hi_lo, r_hi_hi, att_hi, rep_hi = certified_same_surface_ratio_bounds(ALPHA_HI)
    omega_b = float(omega_b_from_eta(ETA_OBS))

    check(
        "The lower current-bank endpoint has a certified narrow thermal ratio enclosure",
        r_lo_hi - r_lo_lo < 1.0e-9,
        f"R_lo=[{r_lo_lo:.12f}, {r_lo_hi:.12f}], width={r_lo_hi-r_lo_lo:.3e}",
    )
    check(
        "The upper current-bank endpoint has a certified narrow thermal ratio enclosure",
        r_hi_hi - r_hi_lo < 1.0e-9,
        f"R_hi=[{r_hi_lo:.12f}, {r_hi_hi:.12f}], width={r_hi_hi-r_hi_lo:.3e}",
    )
    check(
        "The current-bank endpoint enclosures are rigorously disjoint",
        r_lo_hi < r_hi_lo,
        f"R_lo_hi={r_lo_hi:.12f}, R_hi_lo={r_hi_lo:.12f}",
    )

    print()
    print(f"  alpha_lo = {ALPHA_LO:.15f}  ->  R in [{r_lo_lo:.12f}, {r_lo_hi:.12f}]")
    print(f"  alpha_hi = {ALPHA_HI:.15f}  ->  R in [{r_hi_lo:.12f}, {r_hi_hi:.12f}]")
    print(f"  trunc_lo = (N_att={att_lo}, N_rep={rep_lo})")
    print(f"  trunc_hi = (N_att={att_hi}, N_rep={rep_hi})")
    print(f"  Omega_b  = {omega_b:.12f}")
    return omega_b, r_lo_lo, r_lo_hi, r_hi_lo, r_hi_hi


def part2_current_bank_global_image(omega_b: float, r_lo_lo: float, r_lo_hi: float, r_hi_lo: float, r_hi_hi: float) -> float:
    print("\n" + "=" * 88)
    print("PART 2: GLOBAL CURRENT-BANK IMAGE BY EXACT MONOTONICITY")
    print("=" * 88)

    target_ratio = OMEGA_DM_OBS / omega_b
    omega_dm_lo_lo = r_lo_lo * omega_b
    omega_dm_lo_hi = r_lo_hi * omega_b
    omega_dm_hi_lo = r_hi_lo * omega_b
    omega_dm_hi_hi = r_hi_hi * omega_b

    check(
        "Exact monotonicity plus certified endpoint bounds gives a rigorous current-bank image interval",
        omega_dm_lo_hi < omega_dm_hi_lo,
        f"Omega_DM in [[{omega_dm_lo_lo:.12f}, {omega_dm_lo_hi:.12f}], [{omega_dm_hi_lo:.12f}, {omega_dm_hi_hi:.12f}]]",
    )
    check(
        "The observed DM target lies BELOW both exact endpoint images (corrected kernel): the current bank overshoots it and forces no selector",
        OMEGA_DM_OBS < omega_dm_lo_lo < omega_dm_hi_lo,
        f"Omega_DM_target={OMEGA_DM_OBS:.12f} < Omega_DM(alpha_lo) lower bound={omega_dm_lo_lo:.12f}",
    )
    check(
        "The same statement on the ratio scale is rigorous",
        target_ratio < r_lo_lo < r_hi_lo,
        f"R_target={target_ratio:.12f} < R_lo lower bound={r_lo_lo:.12f}",
    )

    print()
    print(f"  current-bank Omega_DM lower endpoint = [{omega_dm_lo_lo:.12f}, {omega_dm_lo_hi:.12f}]")
    print(f"  current-bank Omega_DM upper endpoint = [{omega_dm_hi_lo:.12f}, {omega_dm_hi_hi:.12f}]")
    print(f"  Omega_DM target                     = {OMEGA_DM_OBS:.12f}")
    return target_ratio


def part3_admitted_family_certified_root(omega_b: float, target_ratio: float, r_lo_lo: float) -> None:
    print("\n" + "=" * 88)
    print("PART 3: NO ROOT ON THE ONE-SCALAR SAME-SURFACE FAMILY (CORRECTED KERNEL)")
    print("=" * 88)

    try:
        certified_sigma_interval(omega_b)
        no_certified_root = False
    except ValueError as exc:
        no_certified_root = True
        detail = str(exc)
    else:
        detail = "a certified sigma interval was returned"

    check(
        "No certified root interval exists on sigma in [0,1]: the helper cannot bracket the target",
        no_certified_root,
        detail,
    )
    check(
        "Exact monotonicity: R(sigma) >= R(sigma=0) > R_target for every sigma in [0,1], so the family has no crossing",
        r_lo_lo > target_ratio,
        f"R(sigma=0) lower bound={r_lo_lo:.12f}, R_target={target_ratio:.12f}",
    )

    alpha_half = ARCHIVED_PI_FORM_ROOT_ALPHA / 2.0
    ratio_half = converged_same_surface_ratio(alpha_half)
    check(
        "The corrected ratio at half the archived (pi-form) root coupling reproduces the comparator, as S_pi(alpha) = S_2pi(alpha/2) requires",
        abs(ratio_half - target_ratio) < 1.0e-9,
        f"R_corrected(alpha={alpha_half:.15f})={ratio_half:.12f}, R_target={target_ratio:.12f}",
    )
    check(
        "That comparator-reproducing coupling lies outside the admitted family (sigma < 0): a fitted value, not a selector",
        alpha_half < ALPHA_LO,
        f"alpha={alpha_half:.15f} < alpha_lo={ALPHA_LO:.15f}",
    )

    print()
    print(f"  comparator-reproducing alpha = {alpha_half:.15f}  (R = {ratio_half:.12f}); diagnostic only")
    print(f"  admitted family              alpha in [{ALPHA_LO:.15f}, {ALPHA_HI:.15f}]")


def main() -> int:
    print("=" * 88)
    print("DM SAME-SURFACE THERMAL SUPPLIED-PREMISE INTERVAL THEOREM")
    print("=" * 88)

    part0_source_scope_boundary()
    omega_b, r_lo_lo, r_lo_hi, r_hi_lo, r_hi_hi = part1_current_bank_certified_bounds()
    target_ratio = part2_current_bank_global_image(omega_b, r_lo_lo, r_lo_hi, r_hi_lo, r_hi_hi)
    part3_admitted_family_certified_root(omega_b, target_ratio, r_lo_lo)

    print("\n" + "=" * 88)
    print("BOTTOM LINE")
    print("=" * 88)
    print("  Given the supplied upstream/helper packet and the corrected Sommerfeld")
    print("  argument (2 pi alpha / v_rel), the local interval composition certifies:")
    print("    - current-bank endpoint images are bracketed and disjoint")
    print("    - the comparator target lies BELOW both endpoint images")
    print("    - the one-scalar same-surface family has NO root on sigma in [0,1]")
    print("  The archived target bracketing and unique root interval came from the")
    print("  half-argument (pi) kernel and are superseded.")
    print("  What still remains open is the source derivation of the live-DM")
    print("  constants and packet-completeness / selector premises.")

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
