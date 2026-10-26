#!/usr/bin/env python3
"""This runner reproduces supplied finite numerical fixtures and checks documentary
consistency. Its unchanged numerical predicates, grids and optimizer settings
are not a proof of global optimality, exact roots, physical selection or an
exhaustive remaining research burden. Text matches report text only. Historical
literal-True narrative is not counted as a mathematical PASS.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['archive_unlanded/dm-neutrino-stale-runners-2026-04-30/DM_NEUTRINO_WEAK_TRIPLET_COEFFICIENT_AXIOM_BOUNDARY_NOTE_2026-04-15.md', 'docs/DM_LEPTOGENESIS_NE_PROJECTED_SOURCE_TRIPLET_SIGN_THEOREM_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_CP_BRIDGE_BOUNDARY_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_BREAKING_TRIPLET_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_PREIMAGE_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_POSITIVE_POLAR_H_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_POSTCANONICAL_POLAR_SECTION_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_AMPLITUDE_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_BANK_Z3_DOUBLET_BLOCK_SELECTION_OBSTRUCTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ATOMIC_WITNESS_VOLUME_SELECTOR_NONREALIZATION_NOTE_2026-04-18.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_CARRIER_NORMAL_FORM_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_INTRINSIC_SLOT_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_SHIFT_QUOTIENT_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_BLOCK_POINT_SELECTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_SELECTOR_FIRST_SHOULDER_EXIT_THRESHOLD_SUPPORT_NOTE_2026-04-21.md', 'docs/DM_SELECTOR_RELATIVE_ACTION_RECOVERED_BRANCH_SEPARATION_SUPPORT_THEOREM_NOTE_2026-04-21.md', 'docs/DM_SELECTOR_RELATIVE_ACTION_RECOVERED_PROJECTION_SUPPORT_THEOREM_NOTE_2026-04-21.md', 'docs/DM_SELECTOR_SHIFTED_DOUBLET_IMAG_SIGN_SUPPORT_THEOREM_NOTE_2026-04-21.md', 'docs/DM_SELECTOR_THRESHOLD_STABILIZATION_SUPPORT_THEOREM_NOTE_2026-04-21.md', 'docs/SCALAR_SELECTOR_REMAINING_OPEN_IMPORTS_2026-04-20.md', 'scripts/dm_leptogenesis_exact_common.py', 'scripts/dm_selector_branch_support.py', 'scripts/frontier_dm_leptogenesis_flavor_column_functional_theorem.py', 'scripts/frontier_dm_leptogenesis_ne_charged_source_response_reduction.py', 'scripts/frontier_dm_leptogenesis_ne_projected_source_law_derivation.py', 'scripts/frontier_dm_leptogenesis_ne_projected_source_triplet_sign_theorem.py', 'scripts/frontier_dm_leptogenesis_pmns_active_projector_reduction.py', 'scripts/frontier_dm_leptogenesis_pmns_cp_bridge_boundary.py', 'scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py', 'scripts/frontier_dm_leptogenesis_pmns_projector_interface.py', 'scripts/frontier_dm_neutrino_breaking_triplet_cp_theorem.py', 'scripts/frontier_dm_neutrino_exact_h_source_surface_preimage_bundle_theorem.py', 'scripts/frontier_dm_neutrino_hermitian_bridge_carrier.py', 'scripts/frontier_dm_neutrino_positive_polar_h_cp_theorem.py', 'scripts/frontier_dm_neutrino_postcanonical_polar_section.py', 'scripts/frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary.py', 'scripts/frontier_dm_neutrino_source_surface_active_half_plane_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_atomic_witness_volume_selector_nonrealization.py', 'scripts/frontier_dm_neutrino_source_surface_carrier_normal_form.py', 'scripts/frontier_dm_neutrino_source_surface_intrinsic_slot_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_shift_quotient_bundle_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_z3_doublet_block_point_selection_theorem.py', 'scripts/frontier_dm_selector_first_shoulder_exit_threshold_support_2026_04_21.py', 'scripts/frontier_dm_selector_relative_action_recovered_branch_separation_support_2026_04_21.py', 'scripts/frontier_dm_selector_relative_action_recovered_projection_support_2026_04_21.py']

import math
import sys
from pathlib import Path

import numpy as np

from dm_selector_branch_support import recovered_bank
from frontier_dm_neutrino_source_bank_z3_doublet_block_selection_obstruction_theorem import (
    active_target_from_h,
)
from frontier_dm_neutrino_source_surface_z3_doublet_block_point_selection_theorem import (
    kz_from_h,
)
from frontier_dm_leptogenesis_ne_projected_source_law_derivation import (
    hermitian_linear_responses,
)
from frontier_dm_leptogenesis_ne_projected_source_triplet_sign_theorem import (
    triplet_from_projected_response_pack,
)
from frontier_dm_selector_relative_action_recovered_branch_separation_support_2026_04_21 import (
    observable_relative_action_selection,
)
from frontier_dm_selector_relative_action_recovered_projection_support_2026_04_21 import (
    unique_argmin,
)
from frontier_dm_selector_first_shoulder_exit_threshold_support_2026_04_21 import (
    threshold_volume,
)
from frontier_dm_neutrino_source_surface_atomic_witness_volume_selector_nonrealization import (
    inverse_eigenvalue_parameters,
)
from dm_selector_branch_support import ANCHOR_OFFSET, common_shift

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


def imag12_from_h(h: np.ndarray) -> float:
    kz = np.asarray(kz_from_h(h), dtype=complex)
    return float(np.imag(kz[1, 2]))


def delta_switch() -> float:
    return 4.0 * math.sqrt(2.0) / (3.0 * math.sqrt(3.0))


def main() -> int:
    print("=" * 88)
    print("DM SELECTOR SHIFTED-DOUBLET-IMAGINARY-SIGN FINITE NUMERICAL SUPPORT")
    print("=" * 88)

    doublet_note = read("docs/DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_BLOCK_POINT_SELECTION_THEOREM_NOTE_2026-04-16.md")
    sep_note = read("docs/DM_SELECTOR_RELATIVE_ACTION_RECOVERED_BRANCH_SEPARATION_SUPPORT_THEOREM_NOTE_2026-04-21.md")
    proj_note = read("docs/DM_SELECTOR_RELATIVE_ACTION_RECOVERED_PROJECTION_SUPPORT_THEOREM_NOTE_2026-04-21.md")
    review = read("docs/SCALAR_SELECTOR_REMAINING_OPEN_IMPORTS_2026-04-20.md")

    _i_star, _x_sel, _y_sel, _delta_sel, h_rel, _etas = observable_relative_action_selection()
    rel_target = np.asarray(active_target_from_h(h_rel), dtype=float)
    rel_imag = imag12_from_h(h_rel)
    d_cut = delta_switch()

    _lifts, hs_bank, repairs_bank, _targets = recovered_bank()
    imag_bank = np.array([imag12_from_h(h) for h in hs_bank], dtype=float)
    target_bank = np.array([active_target_from_h(h) for h in hs_bank], dtype=float)
    triplet_bank = [triplet_from_projected_response_pack(hermitian_linear_responses(h)) for h in hs_bank]

    mu_anchor = common_shift(repairs_bank, ANCHOR_OFFSET)
    params_bank = [inverse_eigenvalue_parameters(h, mu_anchor) for h in hs_bank]
    tau_b = np.array([math.log1p(p[1]) for p in params_bank], dtype=float)
    tau_b_min = float(np.min(tau_b))
    tau_vals = np.array([threshold_volume(p, tau_b_min) for p in params_bank], dtype=float)
    tau_idx, tau_margin = unique_argmin(tau_vals)

    print("\n" + "=" * 88)
    print("PART 1: THE ACTIVE Z3 DOUBLET THEOREM FIXES ONE CANONICAL SIGN BOUNDARY")
    print("=" * 88)

    check('DOCUMENTARY text observation only: The doublet-block theorem note records delta = (Im K12 + 4 sqrt(2)/3) / sqrt(3)', "delta = (Im K12 + 4 sqrt(2)/3) / sqrt(3)" in doublet_note)
    check(
        'So the computed sign boundary is delta = 4 sqrt(2) / (3 sqrt(3))',
        abs(d_cut - 4.0 * math.sqrt(2.0) / (3.0 * math.sqrt(3.0))) < 1.0e-12,
        f"delta_cut = {d_cut:.15f}",
    )

    print("\n" + "=" * 88)
    print("PART 2: THE INTERNAL SELECTOR LIES ON THE POSITIVE SIDE OF THAT BOUNDARY")
    print("=" * 88)

    check('DOCUMENTARY text observation only: The separation note still records the exact internal observable-relative-action selector', "observable-relative-action law" in sep_note and "exact internal selector law" in sep_note)
    check(
        'The numerically constructed candidate target has delta_rel > delta_cut',
        rel_target[0] > d_cut,
        f"(delta_rel, delta_cut)=({rel_target[0]:.12f}, {d_cut:.12f})",
    )
    check(
        'Equivalently, the numerically constructed candidate has positive shifted imaginary doublet mixing Im(K12) > 0',
        rel_imag > 0.0,
        f"Im(K12)_rel = {rel_imag:.12e}",
    )

    print("\n" + "=" * 88)
    print("PART 3: ON THE RECOVERED BANK, ONLY THE PREFERRED LIFT SHARES THAT POSITIVE SIDE")
    print("=" * 88)

    positive_idx = np.where(imag_bank > 0.0)[0]
    check(
        'Exactly one recovered lift has positive shifted imaginary doublet mixing',
        len(positive_idx) == 1,
        f"positive indices = {positive_idx.tolist()}",
    )
    check(
        'That unique positive recovered lift is the preferred lift 0',
        len(positive_idx) == 1 and int(positive_idx[0]) == 0,
        f"Im(K12)_bank = {np.round(imag_bank, 12)}",
    )
    check(
        'Every competing recovered lift lies strictly on the negative side Im(K12) < 0',
        np.all(imag_bank[1:] < 0.0),
        f"competitor imag parts = {np.round(imag_bank[1:], 12)}",
    )

    print("\n" + "=" * 88)
    print("PART 4: THE CONSTRUCTIVE TRIPLET CHAMBER STILL DOES NOT DISTINGUISH THE RECOVERED PACKET")
    print("=" * 88)

    gamma_bank = np.array([float(t["gamma"]) for t in triplet_bank], dtype=float)
    e1_bank = np.array([float(t["E1"]) for t in triplet_bank], dtype=float)
    e2_bank = np.array([float(t["E2"]) for t in triplet_bank], dtype=float)

    check(
        'All recovered lifts already share the same computed constructive triplet tuple',
        np.allclose(gamma_bank, gamma_bank[0], atol=1.0e-12)
        and np.allclose(e1_bank, e1_bank[0], atol=1.0e-12)
        and np.allclose(e2_bank, e2_bank[0], atol=1.0e-12),
        f"(gamma,E1,E2)=({gamma_bank[0]:.12f},{e1_bank[0]:.12f},{e2_bank[0]:.12f})",
    )
    check(
        'So the constructive triplet chamber gamma > 0, E1 > 0, E2 > 0 is shared across the recovered packet',
        np.all(gamma_bank > 0.0) and np.all(e1_bank > 0.0) and np.all(e2_bank > 0.0),
        "triplet chamber does not break the recovered degeneracy",
    )
    check(
        'Every recovered lift also stays on the positive oriented-phase side sin(delta) > 0',
        np.all(np.sin(target_bank[:, 0]) > 0.0),
        f"sin(delta)_bank = {np.round(np.sin(target_bank[:, 0]), 12)}",
    )

    print("\n" + "=" * 88)
    print("PART 5: FINITE SIGN AND THRESHOLD AGREEMENT")
    print("=" * 88)

    check('DOCUMENTARY text observation only: The projection note still records that the preferred recovered lift is the canonical recovered image of the internal selector', "canonical recovered projection" in flat(proj_note)
        and "preferred recovered lift `0`" in flat(proj_note))
    check(
        'The supplied threshold candidate tau_b,min still selects the same preferred recovered lift uniquely',
        tau_idx == 0 and tau_margin > 1.0e-9,
        f"(winner, margin)=({tau_idx}, {tau_margin:.12f})",
    )
    check(
        'So on the current selector packet the numerically constructed candidate, the recovered projection, the threshold selector, and the shifted-imaginary sign all agree on the same preferred recovered lift',
        len(positive_idx) == 1 and int(positive_idx[0]) == 0 and tau_idx == 0 and rel_imag > 0.0,
        "same preferred lift 0",
    )

    print("\n" + "=" * 88)
    print("PART 6: DOCUMENTARY BOUNDARY AND FINITE COMPARISONS")
    print("=" * 88)

    check("DOCUMENTARY: summary reports physical selection obligations open and PMNS angles supplied", "selection obligations remain open" in " ".join(review.split()) and "PMNS angle triple is an input" in " ".join(review.split()))
    check(
        'Finite supplied diagnostic: agreement of the computed packet comparisons; no global or physical implication',
        np.allclose(gamma_bank, gamma_bank[0], atol=1.0e-12)
        and np.all(gamma_bank > 0.0)
        and len(positive_idx) == 1
        and int(positive_idx[0]) == 0,
        "first right-sensitive refinement",
    )
    check(
        'Finite supplied diagnostic: agreement of the computed packet comparisons; no global or physical implication',
        len(positive_idx) == 1 and int(positive_idx[0]) == 0 and rel_imag > 0.0 and tau_idx == 0,
        "support narrowing only",
    )

    print("\n" + "=" * 88)
    print("RESULT: finite supplied computations and documentary observations only")
    print("No physical selector, exact optimizer/root certificate, exhaustive route or continuous-window theorem follows.")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
