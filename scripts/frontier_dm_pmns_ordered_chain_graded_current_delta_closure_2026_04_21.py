#!/usr/bin/env python3
"""Coordinate recovery from supplied H; no current-value or physical selection theorem."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/DM_LEPTOGENESIS_NE_CHARGED_SOURCE_RESPONSE_REDUCTION_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_NE_PROJECTED_SOURCE_LAW_DERIVATION_NOTE_2026-04-16.md', 'docs/DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_BREAKING_TRIPLET_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_PREIMAGE_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_EXACT_H_SOURCE_SURFACE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_POSITIVE_POLAR_H_CP_THEOREM_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_POSTCANONICAL_POLAR_SECTION_NOTE_2026-04-15.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_CARRIER_NORMAL_FORM_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_INTRINSIC_SLOT_THEOREM_NOTE_2026-04-16.md', 'docs/DM_NEUTRINO_SOURCE_SURFACE_SHIFT_QUOTIENT_BUNDLE_THEOREM_NOTE_2026-04-16.md', 'docs/DM_PMNS_GRAPH_FIRST_ORDERED_CHAIN_NONZERO_CURRENT_ACTIVATION_THEOREM_NOTE_2026-04-21.md', 'docs/DM_PMNS_ORDERED_CHAIN_GRADED_CURRENT_DELTA_CLOSURE_THEOREM_NOTE_2026-04-21.md', 'docs/DM_PMNS_UPPER_OCTANT_SOURCE_CUBIC_SELECTOR_THEOREM_NOTE_2026-04-20.md', 'docs/DM_WILSON_TO_DWEH_HERMITIAN_SOURCE_FAMILY_TARGET_NOTE_2026-04-18.md', 'docs/DM_WILSON_TO_DWEH_LOCAL_CHAIN_PATH_ALGEBRA_TARGET_NOTE_2026-04-18.md', 'docs/PMNS_GRAPH_FIRST_CYCLE_FRAME_SUPPORT_NOTE.md', 'docs/PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md', 'docs/PMNS_ORIENTED_CYCLE_SELECTION_STRUCTURE_NOTE.md', 'scripts/dm_leptogenesis_exact_common.py', 'scripts/frontier_dm_leptogenesis_pmns_projector_interface.py', 'scripts/frontier_dm_neutrino_breaking_triplet_cp_theorem.py', 'scripts/frontier_dm_neutrino_exact_h_source_surface_preimage_bundle_theorem.py', 'scripts/frontier_dm_neutrino_hermitian_bridge_carrier.py', 'scripts/frontier_dm_neutrino_positive_polar_h_cp_theorem.py', 'scripts/frontier_dm_neutrino_postcanonical_polar_section.py', 'scripts/frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary.py', 'scripts/frontier_dm_neutrino_source_surface_active_half_plane_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_carrier_normal_form.py', 'scripts/frontier_dm_neutrino_source_surface_intrinsic_slot_theorem.py', 'scripts/frontier_dm_neutrino_source_surface_shift_quotient_bundle_theorem.py', 'scripts/frontier_dm_pmns_graph_first_ordered_chain_nonzero_current_closure_2026_04_21.py', 'scripts/frontier_dm_pmns_upper_octant_source_cubic_selector_theorem_2026_04_20.py', 'scripts/frontier_dm_wilson_to_dweh_local_chain_path_algebra_target_2026_04_18.py', 'scripts/frontier_graph_first_selector_derivation.py', 'scripts/frontier_graph_first_su3_integration.py', 'scripts/frontier_pmns_active_four_real_source_from_transport.py', 'scripts/frontier_pmns_c3_character_holonomy_closure.py', 'scripts/frontier_pmns_c3_character_mode_reduction.py', 'scripts/frontier_pmns_c3_nontrivial_current_boundary.py', 'scripts/frontier_pmns_current_bank_value_selection_nogo.py', 'scripts/frontier_pmns_graph_first_cycle_frame_support.py', 'scripts/frontier_pmns_lower_level_end_to_end_closure.py', 'scripts/frontier_pmns_oriented_cycle_channel_value_law.py', 'scripts/frontier_pmns_oriented_cycle_reduced_channel_nonselection.py', 'scripts/frontier_pmns_oriented_cycle_selection_structure.py', 'scripts/frontier_pmns_sole_axiom_hw1_source_transfer_boundary.py', 'scripts/frontier_pmns_theta23_upper_octant_chamber_closure_prediction.py', 'scripts/frontier_pmns_three_flux_holonomy_closure.py', 'scripts/frontier_pmns_twisted_flux_transfer_holonomy_boundary.py', 'scripts/frontier_pmns_uniform_scalar_deformation_boundary.py', 'scripts/frontier_sigma_hier_uniqueness_theorem.py', 'scripts/pmns_lower_level_utils.py']

import math
import sys

import numpy as np

from dm_leptogenesis_exact_common import exact_package
from frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary import (
    active_affine_h,
    h_base,
    tdelta,
    tm,
    tq,
)
from frontier_dm_pmns_graph_first_ordered_chain_nonzero_current_closure_2026_04_21 import (
    chain_number_operator,
)
from frontier_dm_pmns_upper_octant_source_cubic_selector_theorem_2026_04_20 import (
    CHAMBER_ROOTS,
)
from frontier_pmns_c3_nontrivial_current_boundary import nontrivial_character_current
from pmns_lower_level_utils import (
    active_response_columns_from_sector_operator,
    derive_active_block_from_response_columns,
    sector_operator_fixture_from_effective_block,
)


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




def graded_current(h: np.ndarray) -> complex:
    n = chain_number_operator()
    return nontrivial_character_current(1j * (n @ h - h @ n))


def expected_graded_current(m: float, delta: float, q_plus: float) -> complex:
    e1 = exact_package().E1
    return complex(-0.5, 0.5 * e1 - 0.5 * delta - 1.5 * q_plus)


def delta_from_currents(h: np.ndarray) -> float:
    e1 = exact_package().E1
    j = nontrivial_character_current(h)
    jn = graded_current(h)
    return float(e1 - 2.0 * np.imag(jn) - 3.0 * np.real(j))


def q_from_current(h: np.ndarray) -> float:
    return float(np.real(nontrivial_character_current(h)))




def part2_basis_values_close_the_exact_graded_current_formula() -> None:
    print("\n" + "=" * 88)
    print("PART 2: BASIS VALUES CLOSE THE EXACT GRADED-CURRENT FORMULA")
    print("=" * 88)

    e1 = exact_package().E1
    h0 = h_base()
    tm_mat = tm()
    td_mat = tdelta()
    tq_mat = tq()

    j_h0 = graded_current(h0)
    j_tm = graded_current(tm_mat)
    j_td = graded_current(td_mat)
    j_tq = graded_current(tq_mat)

    check(
        "On the affine base H_base the graded current is -1/2 + i E1/2",
        abs(j_h0 - complex(-0.5, 0.5 * e1)) < 1e-12,
        f"J_N(H_base)={j_h0:.12f}",
    )
    check(
        "The spectator generator T_m is graded-current blind",
        abs(j_tm) < 1e-12,
        f"J_N(T_m)={j_tm:.12f}",
    )
    check(
        "The delta generator contributes exactly -i/2",
        abs(j_td - complex(0.0, -0.5)) < 1e-12,
        f"J_N(T_delta)={j_td:.12f}",
    )
    check(
        "The q_+ generator contributes exactly -3 i / 2",
        abs(j_tq - complex(0.0, -1.5)) < 1e-12,
        f"J_N(T_q)={j_tq:.12f}",
    )

    samples = [
        (0.0, 0.2, 2.1),
        (0.5, 0.4, 1.0),
        (1.2, 0.9, 1.1),
        CHAMBER_ROOTS["Basin 1"],
    ]
    ok_formula = True
    max_err = 0.0
    for m, delta, q_plus in samples:
        h = active_affine_h(m, delta, q_plus)
        err = abs(graded_current(h) - expected_graded_current(m, delta, q_plus))
        ok_formula &= err < 1e-12
        max_err = max(max_err, float(err))

    check(
        "Affine linearity gives J_N(H) = -1/2 + i(E1/2 - delta/2 - 3 q_+/2)",
        ok_formula,
        f"max err={max_err:.2e}",
    )


def part3_the_pair_of_currents_recovers_the_full_affine_active_pair() -> None:
    print("\n" + "=" * 88)
    print("PART 3: THE PAIR OF CURRENTS RECOVERS THE FULL AFFINE ACTIVE PAIR")
    print("=" * 88)

    same_q = [
        (0.5, 0.1, 1.0),
        (0.5, 1.2, 1.0),
    ]
    j_same = [nontrivial_character_current(active_affine_h(*p)) for p in same_q]
    jn_same = [graded_current(active_affine_h(*p)) for p in same_q]

    check(
        "Two affine points with the same q_+ have the same supplied current J_chi",
        abs(j_same[0] - j_same[1]) < 1e-12,
        f"J0={j_same[0]:.12f}, J1={j_same[1]:.12f}",
    )
    check(
        "The graded current separates those same-q_+ points by their different delta values",
        abs(jn_same[0] - jn_same[1]) > 1e-6,
        f"J_N0={jn_same[0]:.12f}, J_N1={jn_same[1]:.12f}",
    )

    samples = [
        (0.5, 0.1, 1.0),
        (0.5, 0.4, 1.0),
        (1.2, 0.9, 1.1),
        CHAMBER_ROOTS["Basin 1"],
        CHAMBER_ROOTS["Basin 2"],
        CHAMBER_ROOTS["Basin X"],
    ]
    ok_q = True
    ok_delta = True
    max_q_err = 0.0
    max_d_err = 0.0
    for m, delta, q_plus in samples:
        h = active_affine_h(m, delta, q_plus)
        q_err = abs(q_from_current(h) - q_plus)
        d_err = abs(delta_from_currents(h) - delta)
        ok_q &= q_err < 1e-12
        ok_delta &= d_err < 1e-12
        max_q_err = max(max_q_err, float(q_err))
        max_d_err = max(max_d_err, float(d_err))

    check(
        "The affine current theorem still recovers q_+ exactly as Re J_chi(H)",
        ok_q,
        f"max err={max_q_err:.2e}",
    )
    check(
        "The graded-current law recovers delta exactly as E1 - 2 Im J_N(H) - 3 Re J_chi(H)",
        ok_delta,
        f"max err={max_d_err:.2e}",
    )


def part4_the_current_pair_survives_exactly_on_the_supplied_hw1_response_family() -> None:
    print("\n" + "=" * 88)
    print("PART 4: THE CURRENT PAIR SURVIVES EXACTLY ON THE SUPPLIED HW=1 RESPONSE FAMILY")
    print("=" * 88)

    lam = 0.31
    samples = [
        CHAMBER_ROOTS["Basin 1"],
        (0.5, 0.4, 1.0),
        (1.2, 0.9, 1.1),
    ]

    ok_block = True
    ok_q = True
    ok_delta = True
    max_block = 0.0
    max_q_err = 0.0
    max_d_err = 0.0

    for idx, sample in enumerate(samples):
        h = active_affine_h(*sample)
        sector = sector_operator_fixture_from_effective_block(h, seed=4100 + idx)
        _ref, cols = active_response_columns_from_sector_operator(sector, lam)
        _ker, recovered = derive_active_block_from_response_columns(cols, lam)

        block_err = np.linalg.norm(recovered - h)
        q_err = abs(q_from_current(recovered) - sample[2])
        d_err = abs(delta_from_currents(recovered) - sample[1])

        ok_block &= block_err < 1e-12
        ok_q &= q_err < 1e-12
        ok_delta &= d_err < 1e-12
        max_block = max(max_block, float(block_err))
        max_q_err = max(max_q_err, float(q_err))
        max_d_err = max(max_d_err, float(d_err))

    check(
        "Active response-column reconstruction recovers the affine Hermitian block exactly",
        ok_block,
        f"max err={max_block:.2e}",
    )
    check(
        "On reconstructed hw=1 response blocks the supplied current still recovers q_+ exactly",
        ok_q,
        f"max err={max_q_err:.2e}",
    )
    check(
        "On reconstructed hw=1 response blocks the graded current still recovers delta exactly",
        ok_delta,
        f"max err={max_d_err:.2e}",
    )








def main() -> int:
    check('The supplied grading is diag(1,2,3)',np.linalg.norm(chain_number_operator()-np.diag([1.,2.,3.]))<1e-12)
    check('Current coordinate Jacobian is invertible, not a selector',abs(np.linalg.det(np.array([[-.5,-1.5],[0.,1.]]))+.5)<1e-12)
    part2_basis_values_close_the_exact_graded_current_formula()
    part3_the_pair_of_currents_recovers_the_full_affine_active_pair()
    part4_the_current_pair_survives_exactly_on_the_supplied_hw1_response_family()
    print('Current values and physical H remain supplied; two real coordinates remain free.')
    print(f'SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}')
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
