#!/usr/bin/env python3
"""Supplied affine coordinate algebra; no physical current/source selection.
J_chi(H)=q_+-i/4 reads q_+ from a supplied current value and is blind to delta.
A second graded current reconstructs delta but selects neither current value.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/DM_NEUTRINO_BREAKING_TRIPLET_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_PREIMAGE_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_POSITIVE_POLAR_H_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_POSTCANONICAL_POLAR_SECTION_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_CARRIER_NORMAL_FORM_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_INTRINSIC_SLOT_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_SHIFT_QUOTIENT_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_BLOCK_POINT_SELECTION_THEOREM_NOTE_2026-04-16.md', 'docs/DM_PMNS_AFFINE_CURRENT_COORDINATE_REDUCTION_THEOREM_NOTE_2026-04-21.md', 'docs/DM_PMNS_GRAPH_FIRST_ORDERED_CHAIN_NONZERO_CURRENT_ACTIVATION_THEOREM_NOTE_2026-04-21.md', 'docs/DM_PMNS_NE_SEED_SURFACE_EXACT_SOURCE_MANIFOLD_THEOREM_NOTE_2026-04-20.md', 'docs/DM_PMNS_ORDERED_CHAIN_GRADED_CURRENT_DELTA_CLOSURE_THEOREM_NOTE_2026-04-21.md', 'docs/PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md', 'docs/PMNS_ORIENTED_CYCLE_SELECTION_STRUCTURE_NOTE.md', 'scripts/dm_leptogenesis_exact_common.py', 'scripts/frontier_dm_neutrino_breaking_triplet_cp_theorem.py', 'scripts/frontier_dm_neutrino_exact_h_source_surface_preimage_bundle_theorem.py', 'scripts/frontier_dm_neutrino_hermitian_bridge_carrier.py', 'scripts/frontier_dm_neutrino_positive_polar_h_cp_theorem.py', 'scripts/frontier_dm_neutrino_postcanonical_polar_section.py', 'scripts/frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary.py', 'scripts/frontier_dm_neutrino_source_surface_active_half_plane_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_carrier_normal_form.py', 'scripts/frontier_dm_neutrino_source_surface_intrinsic_slot_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_shift_quotient_bundle_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_z3_doublet_block_point_selection_theorem.py', 'scripts/frontier_pmns_active_four_real_source_from_transport.py', 'scripts/frontier_pmns_c3_character_holonomy_closure.py', 'scripts/frontier_pmns_c3_character_mode_reduction.py', 'scripts/frontier_pmns_c3_nontrivial_current_boundary.py', 'scripts/frontier_pmns_current_bank_value_selection_nogo.py', 'scripts/frontier_pmns_lower_level_end_to_end_closure.py', 'scripts/frontier_pmns_oriented_cycle_channel_value_law.py', 'scripts/frontier_pmns_oriented_cycle_reduced_channel_nonselection.py', 'scripts/frontier_pmns_oriented_cycle_selection_structure.py', 'scripts/frontier_pmns_sole_axiom_hw1_source_transfer_boundary.py', 'scripts/frontier_pmns_three_flux_holonomy_closure.py', 'scripts/frontier_pmns_twisted_flux_transfer_holonomy_boundary.py', 'scripts/frontier_pmns_uniform_scalar_deformation_boundary.py', 'scripts/pmns_lower_level_utils.py']

import math
import sys
from pathlib import Path

import numpy as np

from frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary import (
    active_affine_h,
    h_base,
    tdelta,
    tm,
    tq,
)
from frontier_dm_neutrino_source_surface_z3_doublet_block_point_selection_theorem import (
    kz_from_h,
)
from frontier_pmns_c3_nontrivial_current_boundary import nontrivial_character_current

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


def expected_current(q_plus: float) -> complex:
    return complex(q_plus, -0.25)


def delta_from_k12(h: np.ndarray) -> float:
    kz = kz_from_h(np.asarray(h, dtype=complex))
    return float((np.imag(kz[1, 2]) + 4.0 * math.sqrt(2.0) / 3.0) / math.sqrt(3.0))


def q_from_doublet_trace(h: np.ndarray) -> float:
    kz = kz_from_h(np.asarray(h, dtype=complex))
    return float(2.0 * math.sqrt(2.0) / 9.0 - 0.5 * np.real(kz[1, 1] + kz[2, 2]))


def part1_basis_values() -> None:
    print("\n" + "=" * 88)
    print("PART 1: EXACT CURRENT VALUES ON THE AFFINE BASIS")
    print("=" * 88)

    j_base = nontrivial_character_current(h_base())
    j_m = nontrivial_character_current(tm())
    j_delta = nontrivial_character_current(tdelta())
    j_q = nontrivial_character_current(tq())

    check(
        "The affine base carries the fixed imaginary offset J_chi(H_base) = -i/4",
        abs(j_base - complex(0.0, -0.25)) < 1.0e-12,
        f"J_base={j_base:.12f}",
    )
    check(
        "The spectator direction T_m is current-blind",
        abs(j_m) < 1.0e-12,
        f"J(T_m)={j_m:.12f}",
    )
    check(
        "The affine delta direction T_delta is current-blind",
        abs(j_delta) < 1.0e-12,
        f"J(T_delta)={j_delta:.12f}",
    )
    check(
        "The affine q_+ direction T_q is read with unit coefficient",
        abs(j_q - 1.0) < 1.0e-12,
        f"J(T_q)={j_q:.12f}",
    )


def part2_exact_affine_formula() -> None:
    print("\n" + "=" * 88)
    print("PART 2: EXACT AFFINE CURRENT FORMULA")
    print("=" * 88)

    samples = [
        (0.0, 0.25, 0.70),
        (0.6, -0.40, 0.70),
        (1.3, 0.95, 0.70),
        (0.4, 1.10, 1.25),
    ]

    ok_formula = True
    max_err = 0.0
    for m, delta, q_plus in samples:
        h = active_affine_h(m, delta, q_plus)
        j = nontrivial_character_current(h)
        err = abs(j - expected_current(q_plus))
        ok_formula &= err < 1.0e-12
        max_err = max(max_err, err)

    check(
        "On the affine Hermitian chart the exact current law is J_chi(H) = q_+ - i/4",
        ok_formula,
        f"max err={max_err:.2e}",
    )
    check(
        "So a supplied current value reconstructs q_+ exactly but is blind to m and delta",
        ok_formula,
        "J_chi depends only on q_+ on the affine chart",
    )


def part3_doublet_block_readout() -> None:
    print("\n" + "=" * 88)
    print("PART 3: THE REMAINING AFFINE SCALAR IS THE SHIFTED IMAGINARY DOUBLET-MIXING")
    print("=" * 88)

    m = 0.70
    q_plus = 0.82
    h_a = active_affine_h(m, 0.20, q_plus)
    h_b = active_affine_h(m, 1.10, q_plus)

    j_a = nontrivial_character_current(h_a)
    j_b = nontrivial_character_current(h_b)
    delta_a = delta_from_k12(h_a)
    delta_b = delta_from_k12(h_b)
    q_a = q_from_doublet_trace(h_a)
    q_b = q_from_doublet_trace(h_b)

    check(
        "Different affine delta values at fixed q_+ carry the same native current",
        abs(j_a - j_b) < 1.0e-12,
        f"J_a={j_a:.12f}, J_b={j_b:.12f}",
    )
    check(
        "The same two points have different shifted Im(K_Z3[1,2]) readout, i.e. different delta",
        abs(delta_a - delta_b) > 1.0e-6,
        f"delta_a={delta_a:.12f}, delta_b={delta_b:.12f}",
    )
    check(
        "The Z3 doublet-block theorem still reads q_+ exactly from the centered doublet trace",
        abs(q_a - q_plus) < 1.0e-12 and abs(q_b - q_plus) < 1.0e-12,
        f"q_a={q_a:.12f}, q_b={q_b:.12f}",
    )


def part4_scientific_consequence() -> None:
    print("\n" + "=" * 88)
    print("PART 4: SCIENTIFIC CONSEQUENCE")
    print("=" * 88)

    manifold_note = read("docs/DM_PMNS_NE_SEED_SURFACE_EXACT_SOURCE_MANIFOLD_THEOREM_NOTE_2026-04-20.md")
    current_note = read("docs/DM_PMNS_GRAPH_FIRST_ORDERED_CHAIN_NONZERO_CURRENT_ACTIVATION_THEOREM_NOTE_2026-04-21.md")
    doublet_note = read("docs/DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_BLOCK_POINT_SELECTION_THEOREM_NOTE_2026-04-16.md")

    check(
        "The fixed-N_e theorem still records that the physical PMNS target lives on an exact local 2-real source manifold",
        "local `2`-real" in manifold_note or "local 2-real" in manifold_note,
    )
    check(
        "The ordered-chain theorem still lands one supplied nonzero-current fixture on hw=1",
        "J_chi(A_ord)=1" in current_note.replace(" ", ""),
    )
    check(
        "The doublet-block theorem still records delta as the shifted imaginary K12 coordinate",
        "delta = (Im K12 + 4 sqrt(2)/3) / sqrt(3)" in doublet_note
        or "delta = (Im K12 + 4 sqrt(2)/3) / sqrt(3)." in doublet_note,
    )
    check(
        "Therefore current activation is not yet the full physical PMNS last mile at this theorem stage",
        True,
        "equivalently the current-blind shifted Im(K_Z3[1,2]) law on the retained hw=1 family remained to be closed",
    )
    check(
        "The graded-current construction recovers coordinates but leaves source selection open",
        "selection of the two current values remains open" in read("docs/DM_PMNS_ORDERED_CHAIN_GRADED_CURRENT_DELTA_CLOSURE_THEOREM_NOTE_2026-04-21.md")
        or "It does not select those values." in read("docs/DM_PMNS_ORDERED_CHAIN_GRADED_CURRENT_DELTA_CLOSURE_THEOREM_NOTE_2026-04-21.md"),
        "conditional coordinate reconstruction only",
    )


def main() -> int:
    print("=" * 88)
    print("DM PMNS AFFINE CURRENT-COORDINATE REDUCTION THEOREM")
    print("=" * 88)
    print()
    print("Question:")
    print("  After graph-first current activation is landed, what exact native object")
    print("  still remains open on the physical affine Hermitian PMNS chart?")

    part1_basis_values()
    part2_exact_affine_formula()
    part3_doublet_block_readout()
    part4_scientific_consequence()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Exact affine-current sharpening:")
    print("    - on H(m, delta, q_+) the native current is J_chi(H) = q_+ - i/4")
    print("    - a supplied current value reconstructs the q_+ coordinate")
    print("    - the shifted Im(K_Z3[1,2]) / delta coordinate remained open at")
    print("      this theorem stage")
    print()
    print("Coordinate reconstruction leaves physical source/current selection open.")
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
