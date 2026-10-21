#!/usr/bin/env python3
"""Finite supplied basin/current controls; physical source selection remains open."""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
from frontier_dm_abcc_exact_target_surface_source_cubic_closure_2026_04_21 import basin_data
from frontier_pmns_c3_nontrivial_current_boundary import nontrivial_character_current
from frontier_pmns_oriented_cycle_reduced_channel_nonselection import active_block_with_reduced_cycle
from frontier_pmns_sole_axiom_hw1_source_transfer_boundary import sole_axiom_hw1_source_transfer_pack
from frontier_pmns_uniform_scalar_deformation_boundary import scalar_triplet_block
from pmns_lower_level_utils import I3, active_response_columns_from_sector_operator, derive_active_block_from_response_columns
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
 "docs/DM_ABCC_EXACT_TARGET_SURFACE_SOURCE_CUBIC_CLOSURE_THEOREM_NOTE_2026-04-21.md",
 "docs/DM_PMNS_ORDERED_CHAIN_GRADED_CURRENT_DELTA_CLOSURE_THEOREM_NOTE_2026-04-21.md",
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

def part3_on_the_reduced_family_jchi_is_exactly_the_nontrivial_value_datum() -> None:
    print('\n' + '=' * 88)
    print('PART 3: ON THE REDUCED FAMILY J_chi IS EXACTLY THE SUPPLIED NONTRIVIAL CURRENT')
    print('=' * 88)
    a = active_block_with_reduced_cycle(0.41, 0.32, 0.28, xbar=1.0)
    b = active_block_with_reduced_cycle(0.29, -0.17, 0.34, xbar=1.0)
    j_a = nontrivial_character_current(a)
    j_b = nontrivial_character_current(b)
    check('The native current reproduces the first reduced nontrivial mode exactly', abs(j_a.real - 0.41) < 1e-12 and abs(j_a.imag - 0.32) < 1e-12, f'J_a={j_a:.6f}')
    check('These two supplied points carry distinct J_chi currents', abs(j_a - j_b) > 1e-06, f'J_a={j_a:.6f}, J_b={j_b:.6f}')

def part4_the_current_retained_bank_still_sets_jchi_to_zero() -> None:
    print('\n' + '=' * 88)
    print('PART 4: THREE SUPPLIED FIXTURES HAVE ZERO CURRENT')
    print('=' * 88)
    free_current = nontrivial_character_current(I3)
    lam = 0.31
    pack = sole_axiom_hw1_source_transfer_pack(lam, 0.27)
    source_block = derive_active_block_from_response_columns(pack['active_columns'], lam)[1]
    source_current = nontrivial_character_current(source_block)
    scalar_block = scalar_triplet_block(1.13)
    scalar_cols = active_response_columns_from_sector_operator(scalar_block, lam)[1]
    scalar_active = derive_active_block_from_response_columns(scalar_cols, lam)[1]
    scalar_current = nontrivial_character_current(scalar_active)
    check('The free route has J_chi = 0', abs(free_current) < 1e-12, f'J_chi={free_current:.6f}')
    check('The supplied hw=1 source/transfer fixture has J_chi = 0', abs(source_current) < 1e-12, f'J_chi={source_current:.6f}')
    check('The supplied scalar fixture has J_chi = 0', abs(scalar_current) < 1e-12, f'J_chi={scalar_current:.6f}')

def part1_finite_basin_table():
    data = basin_data()
    inside = {name for name, row in data.items() if row['margin'] >= 0}
    check('Supplied table has chamber members 1,2,X', inside == {'Basin 1','Basin 2','Basin X'})
    check('Imposed positive cubic selects Basin 1 among these rows',
          data['Basin 1']['I_src'] > 0 and data['Basin 2']['I_src'] < 0 and data['Basin X']['I_src'] < 0)
    check('These three rows have the displayed determinant signs',
          data['Basin 1']['Delta_src'] > 0 and data['Basin 2']['Delta_src'] < 0 and data['Basin X']['Delta_src'] < 0)
    check('N and P preserve counterexamples to unrestricted sign equivalence',
          data['Basin N']['I_src']*data['Basin N']['Delta_src'] < 0 and
          data['Basin P']['I_src']*data['Basin P']['Delta_src'] < 0)

def part2_current_coordinates():
    # Independent supplied coordinate directions, not physical target selection.
    j0 = nontrivial_character_current(active_block_with_reduced_cycle(0,0,.28,xbar=1.0))
    ju = nontrivial_character_current(active_block_with_reduced_cycle(1,0,.28,xbar=1.0))
    jv = nontrivial_character_current(active_block_with_reduced_cycle(0,1,.28,xbar=1.0))
    jac = np.array([[(ju-j0).real,(jv-j0).real],[(ju-j0).imag,(jv-j0).imag]])
    check('Supplied real and imaginary current coordinates have identity Jacobian',np.linalg.norm(jac-np.eye(2))<1e-12)
    jw = nontrivial_character_current(active_block_with_reduced_cycle(0,0,1.28,xbar=1.0))
    check('Current does not recover the independent trivial-mode coordinate',abs(jw-j0)<1e-12)

def documentary_boundaries():
    cubic = (ROOT/AUDIT_INPUT_PATHS[0]).read_text(encoding='utf-8')
    graded = (ROOT/AUDIT_INPUT_PATHS[1]).read_text(encoding='utf-8')
    check('Documentary: cubic source explicitly limits its result to a finite table',
          'It neither derives that selector nor removes physical branch-choice obligations.' in cubic)
    check('Documentary: graded-current source distinguishes coordinate recovery from selection',
          'selection of the two current values remains open' in graded)

def main():
    print('Finite supplied basin/current controls; no physical last-mile closure')
    part1_finite_basin_table()
    part2_current_coordinates()
    part3_on_the_reduced_family_jchi_is_exactly_the_nontrivial_value_datum()
    part4_the_current_retained_bank_still_sets_jchi_to_zero()
    documentary_boundaries()
    print('Open: chamber selection, complete solution census, positivity law, physical current values and source-manifold bridge.')
    print(f'SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}')
    return 1 if FAIL_COUNT else 0
if __name__ == '__main__':
    sys.exit(main())
