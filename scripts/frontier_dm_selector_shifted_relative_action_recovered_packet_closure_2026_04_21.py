#!/usr/bin/env python3
"""Supplied five-lift shifted-relative-action numerical diagnostic.

The scalar, seed, shift list, sixty-point grid and one far-shift point are
stipulated. Floating minimizer/sign checks apply only to those fixtures;
no continuum, asymptotic, physical selector or global closure is established.
Documentary text observations and unscored narration supply no proof authority.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/DM_ABCC_EXACT_TARGET_SURFACE_SOURCE_CUBIC_CLOSURE_THEOREM_NOTE_2026-04-21.md', 'docs/DM_LEPTOGENESIS_NE_PROJECTED_SOURCE_TRIPLET_SIGN_THEOREM_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_CP_BRIDGE_BOUNDARY_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_BREAKING_TRIPLET_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_PREIMAGE_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_POSITIVE_POLAR_H_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_POSTCANONICAL_POLAR_SECTION_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_AMPLITUDE_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_BANK_Z3_DOUBLET_BLOCK_SELECTION_OBSTRUCTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ATOMIC_WITNESS_VOLUME_SELECTOR_NONREALIZATION_NOTE_2026-04-18.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_CARRIER_NORMAL_FORM_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_INTRINSIC_SLOT_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_SHIFT_QUOTIENT_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_BLOCK_POINT_SELECTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md', 'docs/DM_SELECTOR_RELATIVE_ACTION_RECOVERED_BRANCH_SEPARATION_SUPPORT_THEOREM_NOTE_2026-04-21.md', 'docs/DM_SELECTOR_RELATIVE_ACTION_RECOVERED_PROJECTION_SUPPORT_THEOREM_NOTE_2026-04-21.md', 'docs/DM_SELECTOR_SHIFTED_DOUBLET_IMAG_SIGN_SUPPORT_THEOREM_NOTE_2026-04-21.md', 'docs/DM_SELECTOR_SHIFTED_RELATIVE_ACTION_RECOVERED_PACKET_CLOSURE_THEOREM_NOTE_2026-04-21.md', 'docs/DM_SELECTOR_THRESHOLD_STABILIZATION_SUPPORT_THEOREM_NOTE_2026-04-21.md', 'docs/SCALAR_SELECTOR_REMAINING_OPEN_IMPORTS_2026-04-20.md', 'scripts/dm_leptogenesis_exact_common.py', 'scripts/dm_selector_branch_support.py', 'scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py', 'scripts/frontier_dm_leptogenesis_ne_charged_source_response_reduction.py', 'scripts/frontier_dm_leptogenesis_ne_projected_source_law_derivation.py', 'scripts/frontier_dm_leptogenesis_ne_projected_source_triplet_sign_theorem.py', 'scripts/frontier_dm_leptogenesis_pmns_active_projector_reduction.py', 'scripts/frontier_dm_leptogenesis_pmns_cp_bridge_boundary.py', 'scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py', 'scripts/frontier_dm_leptogenesis_pmns_projector_interface.py', 'scripts/frontier_dm_neutrino_breaking_triplet_cp_theorem.py', 'scripts/frontier_dm_neutrino_exact_h_source_surface_preimage_bundle_theorem.py', 'scripts/frontier_dm_neutrino_hermitian_bridge_carrier.py', 'scripts/frontier_dm_neutrino_positive_polar_h_cp_theorem.py', 'scripts/frontier_dm_neutrino_postcanonical_polar_section.py', 'scripts/frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary.py', 'scripts/frontier_dm_neutrino_source_surface_active_half_plane_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_atomic_witness_volume_selector_nonrealization.py', 'scripts/frontier_dm_neutrino_source_surface_carrier_normal_form.py', 'scripts/frontier_dm_neutrino_source_surface_intrinsic_slot_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_shift_quotient_bundle_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_z3_doublet_block_point_selection_theorem.py', 'scripts/frontier_dm_selector_first_shoulder_exit_threshold_support_2026_04_21.py', 'scripts/frontier_dm_selector_relative_action_recovered_branch_separation_support_2026_04_21.py', 'scripts/frontier_dm_selector_relative_action_recovered_projection_support_2026_04_21.py', 'scripts/frontier_dm_selector_shifted_doublet_imag_sign_support_2026_04_21.py']

import sys
from pathlib import Path

import numpy as np

from dm_selector_branch_support import SHIFT_OFFSETS, recovered_bank
from frontier_dm_leptogenesis_pmns_observable_relative_action_law import H_SEED
from frontier_dm_selector_shifted_doublet_imag_sign_support_2026_04_21 import (
    imag12_from_h,
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


def flat(text: str) -> str:
    return " ".join(text.split())


def unique_argmin(values: np.ndarray) -> tuple[int, float]:
    vals = np.asarray(values, dtype=float)
    order = np.argsort(vals)
    return int(order[0]), float(vals[order[1]] - vals[order[0]])


def shifted_relative_action_to_seed(h: np.ndarray, mu: float) -> float:
    a_seed = np.asarray(H_SEED, dtype=complex) + float(mu) * np.eye(3, dtype=complex)
    a = np.asarray(h, dtype=complex) + float(mu) * np.eye(3, dtype=complex)
    m = np.linalg.inv(a_seed) @ a
    sign, logdet = np.linalg.slogdet(m)
    if abs(sign) < 1.0e-12:
        raise ValueError("shifted relative-action matrix left the positive branch")
    return float(np.real(np.trace(m) - logdet - 3.0))


def dense_shift_grid(mu_floor: float) -> np.ndarray:
    return np.concatenate(
        [
            np.linspace(mu_floor + 1.0e-6, mu_floor + 0.1, 20),
            np.linspace(mu_floor + 0.1, mu_floor + 2.0, 20),
            np.linspace(mu_floor + 2.0, mu_floor + 20.0, 20),
        ]
    )


def main() -> int:
    print("=" * 88)
    print("SUPPLIED SHIFTED-RELATIVE-ACTION FINITE PACKET DIAGNOSTIC")
    print("=" * 88)

    rel_note = read("docs/DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md")
    proj_note = read("docs/DM_SELECTOR_RELATIVE_ACTION_RECOVERED_PROJECTION_SUPPORT_THEOREM_NOTE_2026-04-21.md")
    sign_note = read("docs/DM_SELECTOR_SHIFTED_DOUBLET_IMAG_SIGN_SUPPORT_THEOREM_NOTE_2026-04-21.md")
    exact_target = read("docs/DM_ABCC_EXACT_TARGET_SURFACE_SOURCE_CUBIC_CLOSURE_THEOREM_NOTE_2026-04-21.md")

    _lifts, hs_bank, repairs_bank, _targets = recovered_bank()
    mu_floor = float(np.max(repairs_bank))
    imag_bank = np.array([imag12_from_h(h) for h in hs_bank], dtype=float)

    print("\n" + "=" * 88)
    print("PART 1: STIPULATED SCALAR AND SUPPLIED POSITIVE WINDOWS")
    print("=" * 88)

    check('DOCUMENTARY text observation only: The original selector note still records the exact scalar observable-relative-action grammar', 'exact relative bosonic action' in flat(rel_note) and 'S_rel(H_e || H_seed)' in rel_note and ('log det(H_seed^{-1} H_e) - 3' in rel_note))
    check(
        "One common positivity threshold mu_floor exists on the recovered bank",
        mu_floor > 0.0,
        f"mu_floor = {mu_floor:.15f}",
    )
    print("  [INFO] The shifted scalar functional is stipulated; its physical selection is not derived.")

    print("\n" + "=" * 88)
    print("PART 2: EVERY AUDITED COMMON POSITIVE SHIFT PICKS THE SAME PREFERRED LIFT")
    print("=" * 88)

    audited = []
    for offset in SHIFT_OFFSETS:
        mu = mu_floor + float(offset)
        vals = np.array([shifted_relative_action_to_seed(h, mu) for h in hs_bank], dtype=float)
        idx, margin = unique_argmin(vals)
        audited.append((mu, idx, margin))

    audited_ok = all(idx == 0 and margin > 1.0e-9 for _mu, idx, margin in audited)
    audited_margin = min(margin for _mu, _idx, margin in audited)
    check(
        "Across the full audited shift family, the shifted relative action uniquely minimizes at recovered lift 0",
        audited_ok,
        f"worst audited margin = {audited_margin:.12f}",
    )
    check(
        "At the first audited shift above positivity, lift 0 is already unique",
        audited[0][1] == 0 and audited[0][2] > 1.0e-9,
        f"(mu, margin)=({audited[0][0]:.15f}, {audited[0][2]:.12f})",
    )
    check(
        "At the largest audited shift, lift 0 is still unique",
        audited[-1][1] == 0 and audited[-1][2] > 1.0e-9,
        f"(mu, margin)=({audited[-1][0]:.15f}, {audited[-1][2]:.12f})",
    )

    print("\n" + "=" * 88)
    print("PART 3: SIXTY SUPPLIED GRID POINTS AND ONE LARGE-SHIFT POINT")
    print("=" * 88)

    worst_mu = None
    worst_margin = float("inf")
    dense_ok = True
    for mu in dense_shift_grid(mu_floor):
        vals = np.array([shifted_relative_action_to_seed(h, float(mu)) for h in hs_bank], dtype=float)
        idx, margin = unique_argmin(vals)
        if idx != 0 or margin <= 1.0e-9:
            dense_ok = False
        if margin < worst_margin:
            worst_mu = float(mu)
            worst_margin = float(margin)

    check(
        "At the sixty supplied grid points, the same unique finite-bank minimizer is observed",
        dense_ok,
        f"worst dense margin = {worst_margin:.12f} at mu = {worst_mu:.15f}",
    )
    large_mu = mu_floor + 1.0e6
    large_vals = np.array([shifted_relative_action_to_seed(h, large_mu) for h in hs_bank], dtype=float)
    large_idx, large_margin = unique_argmin(large_vals)
    check(
        "At the single supplied mu_floor+1e6 point, lift 0 is the finite-bank minimizer",
        large_idx == 0 and large_margin > 1.0e-18,
        f"(large_mu, margin)=({large_mu:.1f}, {large_margin:.12e})",
    )

    print("\n" + "=" * 88)
    print("PART 4: SUPPLIED SCALAR MINIMIZER AND FINITE DOUBLEt SIGN COMPARISON")
    print("=" * 88)

    positive_idx = np.where(imag_bank > 0.0)[0]
    check('DOCUMENTARY text observation only: The earlier packet note still records that only recovered lift 0 lies on the positive side of Im(K_Z3[1,2]) = 0', 'lift `0`: `Im(K_Z3[1,2]) > 0`' in sign_note and 'lifts `1,2,3,4`: `Im(K_Z3[1,2]) < 0`' in sign_note)
    check(
        "Exactly one recovered lift has positive shifted-imaginary doublet mixing",
        len(positive_idx) == 1 and int(positive_idx[0]) == 0,
        f"Im(K12)_bank = {np.round(imag_bank, 12)}",
    )
    check(
        "So the same shifted relative-action law and the odd doublet-sign packet select the same preferred lift",
        audited_ok and dense_ok and len(positive_idx) == 1 and int(positive_idx[0]) == 0,
        "same recovered lift 0",
    )

    print("\n" + "=" * 88)
    print("PART 5: SCIENTIFIC CONSEQUENCE")
    print("=" * 88)

    check('DOCUMENTARY text observation only: The projection note still records that the exact internal selector already has the same preferred recovered image', 'exact observable-relative-action law' in flat(proj_note) and 'preferred recovered lift `0`' in flat(proj_note))
    check(
        "The supplied scalar functional selects lift0 in the finite tested packet",
        audited_ok and dense_ok and len(positive_idx) == 1 and int(positive_idx[0]) == 0,
        "packet-local closure only",
    )
    check('DOCUMENTARY text observation only: The companion finite table keeps physical selection and completeness open', 'It neither derives that selector nor removes physical branch-choice obligations.' in flat(exact_target) or 'This is conditional on a separate positivity selector.' in flat(exact_target), 'pure target-free global sign/source-chart derivation remains outside this theorem alone')

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("Finite supplied-bank comparisons only: SHIFT_OFFSETS, sixty grid points and one far point.")
    print("No continuum/asymptotic theorem, physical selector or exhaustive closure follows.")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
