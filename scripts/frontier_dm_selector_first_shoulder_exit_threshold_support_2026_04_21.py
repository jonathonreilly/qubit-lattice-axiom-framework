#!/usr/bin/env python3
"""Finite supplied-bank first-middle-breakpoint diagnostic.

The unchanged numerical comparisons evaluate supplied fixtures at one breakpoint.
They neither certify a whole stabilization interval nor select a physical law.
Documentary matches report text only; canonicality/burden narration is unscored.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['archive_unlanded/dm-neutrino-stale-runners-2026-04-30/DM_NEUTRINO_WEAK_TRIPLET_COEFFICIENT_AXIOM_BOUNDARY_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_BREAKING_TRIPLET_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_PREIMAGE_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_POSITIVE_POLAR_H_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_POSTCANONICAL_POLAR_SECTION_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_AMPLITUDE_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_BANK_Z3_DOUBLET_BLOCK_SELECTION_OBSTRUCTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ATOMIC_WITNESS_VOLUME_SELECTOR_NONREALIZATION_NOTE_2026-04-18.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_CARRIER_NORMAL_FORM_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_INTRINSIC_SLOT_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_SHIFT_QUOTIENT_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_BLOCK_POINT_SELECTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md', 'docs/DM_SELECTOR_THRESHOLD_STABILIZATION_SUPPORT_THEOREM_NOTE_2026-04-21.md', 'scripts/dm_leptogenesis_exact_common.py', 'scripts/dm_selector_branch_support.py', 'scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py', 'scripts/frontier_dm_leptogenesis_ne_charged_source_response_reduction.py', 'scripts/frontier_dm_leptogenesis_pmns_projector_interface.py', 'scripts/frontier_dm_neutrino_breaking_triplet_cp_theorem.py', 'scripts/frontier_dm_neutrino_exact_h_source_surface_preimage_bundle_theorem.py', 'scripts/frontier_dm_neutrino_hermitian_bridge_carrier.py', 'scripts/frontier_dm_neutrino_positive_polar_h_cp_theorem.py', 'scripts/frontier_dm_neutrino_postcanonical_polar_section.py', 'scripts/frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary.py', 'scripts/frontier_dm_neutrino_source_surface_active_half_plane_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_atomic_witness_volume_selector_nonrealization.py', 'scripts/frontier_dm_neutrino_source_surface_carrier_normal_form.py', 'scripts/frontier_dm_neutrino_source_surface_intrinsic_slot_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_shift_quotient_bundle_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_z3_doublet_block_point_selection_theorem.py']

import math
import sys
from pathlib import Path

import numpy as np

from dm_selector_branch_support import (
    ANCHOR_OFFSET,
    PREFERRED_RECOVERED_LIFT,
    common_shift,
    recovered_bank,
)
from frontier_dm_neutrino_source_surface_atomic_witness_volume_selector_nonrealization import (
    inverse_eigenvalue_parameters,
    witness_volume_from_atomic_field,
)

ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0


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


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def threshold_volume(params: tuple[float, float, float], tau: float) -> float:
    return witness_volume_from_atomic_field(params, float(tau))


def main() -> int:
    print("=" * 88)
    print("SUPPLIED-BANK FIRST-MIDDLE-BREAKPOINT DIAGNOSTIC")
    print("=" * 88)

    lifts, hs_bank, repairs_bank, _targets = recovered_bank()
    mu_bank = common_shift(repairs_bank, ANCHOR_OFFSET)
    params_bank = [inverse_eigenvalue_parameters(h, mu_bank) for h in hs_bank]

    tau_b = np.array([math.log1p(p[1]) for p in params_bank], dtype=float)
    tau_a = np.array([math.log1p(p[0]) for p in params_bank], dtype=float)
    tau_star = 0.1316375782215522
    tau_b_min = float(np.min(tau_b))
    tau_b_argmin = int(np.argmin(tau_b))
    tau_zero_next = float(np.min(tau_a[1:]))

    vals_bmin = np.array([threshold_volume(p, tau_b_min) for p in params_bank], dtype=float)
    winner_bmin = int(np.argmin(vals_bmin))

    note = read("docs/DM_SELECTOR_THRESHOLD_STABILIZATION_SUPPORT_THEOREM_NOTE_2026-04-21.md")
    nonrealization = read("docs/DM_NEUTRINO_SOURCE_SURFACE_ATOMIC_WITNESS_VOLUME_SELECTOR_NONREALIZATION_NOTE_2026-04-18.md")

    print("\n" + "=" * 88)
    print("PART 1: THE EARLIEST MIDDLE-BRANCH BREAKPOINT IS UNIQUE")
    print("=" * 88)

    check(
        "The preferred recovered lift is still lift 0 on the current selector branch",
        np.linalg.norm(np.asarray(lifts[0], dtype=float) - PREFERRED_RECOVERED_LIFT) < 1.0e-12,
        f"preferred lift = {np.round(lifts[0], 12)}",
    )
    check(
        "Each recovered lift has an intrinsic middle-branch threshold tau_b = log(1+b)",
        np.all(np.isfinite(tau_b)) and np.all(tau_b > 0.0),
        f"tau_b = {np.round(tau_b, 12)}",
    )
    check(
        "The earliest middle-branch threshold is unique and belongs to the preferred recovered lift",
        tau_b_argmin == 0 and tau_b[0] + 1.0e-12 < np.min(tau_b[1:]),
        f"(tau_b_min, next) = ({tau_b[0]:.15f}, {np.min(tau_b[1:]):.15f})",
    )

    print("\n" + "=" * 88)
    print("PART 2: COMPARISON TO SUPPLIED NUMERICAL ENDPOINTS")
    print("=" * 88)

    check('DOCUMENTARY only: parent records supplied onset; no whole-window certificate inferred', 'tau_star' in note and '0.131637578221552' in note)
    check(
        "The earliest middle-branch threshold lies strictly above tau_star",
        tau_b_min > tau_star,
        f"(tau_b_min - tau_star) = {tau_b_min - tau_star:.15f}",
    )
    check(
        "The earliest middle-branch threshold also lies strictly below the next zero-volume tie",
        tau_b_min < tau_zero_next,
        f"(tau_b_min, tau_zero_next)=({tau_b_min:.15f},{tau_zero_next:.15f})",
    )

    print("\n" + "=" * 88)
    print("PART 3: THAT BREAKPOINT ALREADY SELECTS THE PREFERRED LIFT")
    print("=" * 88)

    check(
        "At this supplied breakpoint, lift 0 has the smallest evaluated field on the supplied bank",
        winner_bmin == 0 and np.all(vals_bmin[0] + 1.0e-12 < vals_bmin[1:]),
        f"vals(tau_b,min) = {np.round(vals_bmin, 12)}",
    )
    print("  [INFO] Historical canonicality/remaining-burden inference withdrawn; no physical selector conclusion.")

    print("\n" + "=" * 88)
    print("PART 4: SCIENTIFIC CONSEQUENCE")
    print("=" * 88)

    check('DOCUMENTARY only: nonrealization text records open intrinsic threshold law', 'intrinsic threshold law' in nonrealization and 'tau = 0.13' in nonrealization and ('tau = 0.14' in nonrealization))
    print("  [INFO] Historical canonicality/remaining-burden inference withdrawn; no physical selector conclusion.")
    print("  [INFO] Historical canonicality/remaining-burden inference withdrawn; no physical selector conclusion.")

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  On the supplied bank, the earliest evaluated middle breakpoint belongs to lift 0.")
    print("  Its field value is smallest among these five supplied entries.")
    print("  Comparison with supplied numerical endpoints is not a whole-window certificate.")
    print("  Physical threshold selection and exhaustive remaining-route claims are open.")
    print()
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
