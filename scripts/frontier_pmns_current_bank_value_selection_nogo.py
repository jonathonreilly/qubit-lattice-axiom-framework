#!/usr/bin/env python3
"""Checked-mechanism boundary for PMNS reduced-cycle value selection.

Question:
  After the sole-axiom free-point theorem, the scalar deformation boundaries,
  the graph-first selector reduction, and the oriented-cycle coordinate map,
  do the mechanisms checked here select a unique reduced-cycle value?

Answer:
  No.

  The runner verifies:

    1. the sole axiom `Cl(3)` on `Z^3` gives only the trivial free response
       profiles on the retained lepton triplets
    2. the admitted local scalar routes stay diagonal/scalar and are rejected
       by the retained one-sided PMNS closure stack
    3. graph-first residual symmetry restricts an explicitly supplied
       candidate block to a reduced oriented forward-cycle family
    4. a bounded algebraic lemma extracts coordinates from a supplied block
    5. target-constructed response fixtures round-trip supplied reduced blocks,
       but are consistency-only rather than independent physical evidence

  None of those checked mechanisms selects a unique reduced-cycle value. This
  is not an exhaustive inventory theorem for every framework route.
"""

from __future__ import annotations

import sys

import numpy as np

from frontier_pmns_lower_level_end_to_end_closure import close_from_lower_level_observables
from frontier_pmns_oriented_cycle_channel_value_law import oriented_cycle_coeffs_from_block
from frontier_pmns_oriented_cycle_reduced_channel_nonselection import (
    active_block_with_reduced_cycle,
    reduced_cycle_coordinates,
    residual_swap_conjugate,
)
from frontier_pmns_uniform_scalar_deformation_boundary import scalar_triplet_block
from pmns_lower_level_utils import (
    I3,
    active_response_columns_from_sector_operator,
    circularity_guard,
    derive_active_block_from_response_columns,
    passive_response_columns_from_sector_operator,
    sector_operator_fixture_from_effective_block,
    support_mask,
)

np.set_printoptions(precision=6, suppress=True, linewidth=140)

PASS_COUNT = 0
FAIL_COUNT = 0
TARGET_SUPPORT = (np.abs(np.eye(3, dtype=complex) + np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)) > 0).astype(int)


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


def expect_raises(fn, exc_type) -> tuple[bool, str]:
    try:
        fn()
    except exc_type as e:  # noqa: PERF203
        return True, str(e)
    except Exception as e:  # noqa: BLE001
        return False, f"wrong exception {type(e).__name__}: {e}"
    return False, "no exception"


def part1_free_and_scalar_routes_are_too_small() -> None:
    print("\n" + "=" * 88)
    print("PART 1: FREE AND SCALAR ROUTES ARE TOO SMALL")
    print("=" * 88)

    lam_act = 0.31
    lam_pass = 0.27

    free_active_cols = active_response_columns_from_sector_operator(I3, lam_act)[1]
    free_passive_cols = passive_response_columns_from_sector_operator(I3, lam_pass)[1]
    ok_free, detail_free = expect_raises(
        lambda: close_from_lower_level_observables(free_active_cols, free_passive_cols, lam_act, lam_pass),
        ValueError,
    )
    check("The sole-axiom free response profiles are rejected by the retained PMNS closure stack", ok_free, detail_free)
    check("The free point carries no nontrivial active support", np.array_equal(support_mask(np.column_stack(free_active_cols)), np.eye(3, dtype=int)))

    diagonal_active = np.diag([1.21, 0.94, 1.08]).astype(complex)
    scalar_passive = scalar_triplet_block(1.13)
    scalar_active_cols = active_response_columns_from_sector_operator(diagonal_active, lam_act)[1]
    scalar_passive_cols = passive_response_columns_from_sector_operator(scalar_passive, lam_pass)[1]
    _kernel_diag, diag_block = derive_active_block_from_response_columns(scalar_active_cols, lam_act)
    ok_diag, detail_diag = expect_raises(
        lambda: close_from_lower_level_observables(scalar_active_cols, scalar_passive_cols, lam_act, lam_pass),
        ValueError,
    )
    check("A retained local-scalar diagonal triplet block stays diagonal on the active response chain",
          np.array_equal(support_mask(diag_block), np.eye(3, dtype=int)))
    check("The retained PMNS closure stack rejects the diagonal/scalar route as well", ok_diag, detail_diag)


def part2_graph_first_restricts_a_supplied_candidate_family() -> None:
    print("\n" + "=" * 88)
    print("PART 2: GRAPH-FIRST RESTRICTS A SUPPLIED CANDIDATE FAMILY")
    print("=" * 88)

    u, v, w = 0.41, 0.32, 0.28
    block = active_block_with_reduced_cycle(u, v, w, xbar=1.0)
    coords = reduced_cycle_coordinates(block)

    check("The graph-first residual antiunitary symmetry fixes the reduced oriented-cycle block",
          np.linalg.norm(residual_swap_conjugate(block) - block) < 1e-12,
          f"error={np.linalg.norm(residual_swap_conjugate(block) - block):.2e}")
    check("The reduced oriented-cycle coordinates are read exactly as (u,v,w)",
          np.linalg.norm(coords - np.array([u, v, w], dtype=float)) < 1e-12,
          f"coords={np.round(coords, 6)}")
    check("The supplied candidate block has the specified diagonal-plus-forward-cycle support",
          np.array_equal(support_mask(block), TARGET_SUPPORT))


def part3_target_constructed_round_trips_do_not_select_a_value() -> None:
    print("\n" + "=" * 88)
    print("PART 3: TARGET-CONSTRUCTED FIXTURES ARE CONSISTENCY-ONLY")
    print("=" * 88)

    lam = 0.31
    a = active_block_with_reduced_cycle(0.41, 0.32, 0.28, xbar=1.0)
    b = active_block_with_reduced_cycle(0.29, -0.17, 0.34, xbar=1.0)

    sector_a = sector_operator_fixture_from_effective_block(a, seed=4101)
    sector_b = sector_operator_fixture_from_effective_block(b, seed=4102)
    _ref_a, cols_a = active_response_columns_from_sector_operator(sector_a, lam)
    _ref_b, cols_b = active_response_columns_from_sector_operator(sector_b, lam)
    _ker_a, rec_a = derive_active_block_from_response_columns(cols_a, lam)
    _ker_b, rec_b = derive_active_block_from_response_columns(cols_b, lam)
    coeffs_a = oriented_cycle_coeffs_from_block(rec_a)
    coeffs_b = oriented_cycle_coeffs_from_block(rec_b)
    coords_a = reduced_cycle_coordinates(rec_a)
    coords_b = reduced_cycle_coordinates(rec_b)

    check("Two target-constructed fixtures round-trip two distinct supplied reduced-channel points",
          np.linalg.norm(rec_a - a) < 1e-12 and np.linalg.norm(rec_b - b) < 1e-12 and np.linalg.norm(a - b) > 1e-6,
          f"|A-B|={np.linalg.norm(a - b):.6f}")
    check("The bounded algebraic coordinate map separates the round-tripped blocks",
          np.linalg.norm(coeffs_a - coeffs_b) > 1e-6 and np.linalg.norm(coords_a - coords_b) > 1e-6,
          f"|Δcoords|={np.linalg.norm(coords_a - coords_b):.6f}")
    check("Both round-tripped blocks satisfy the same graph-first residual antiunitary symmetry",
          np.linalg.norm(residual_swap_conjugate(rec_a) - rec_a) < 1e-12
          and np.linalg.norm(residual_swap_conjugate(rec_b) - rec_b) < 1e-12)
    print("  [INFO] These fixtures were constructed from the supplied targets and are consistency-only.")
    print("  [INFO] They do not establish a physical carrier, readout, or value-selection law.")


def part4_circularity_guard() -> None:
    print("\n" + "=" * 88)
    print("PART 4: CIRCULARITY GUARD")
    print("=" * 88)

    ok_active, bad_active = circularity_guard(active_response_columns_from_sector_operator, {"x", "y", "delta", "tau", "q"})
    ok_cycle, bad_cycle = circularity_guard(oriented_cycle_coeffs_from_block, {"u", "v", "w", "sigma"})
    check("The lower-level active response derivation does not take PMNS-side value targets as inputs", ok_active, f"bad={bad_active}")
    check("The algebraic coordinate extractor does not take reduced-channel coordinate names as inputs", ok_cycle, f"bad={bad_cycle}")


def main() -> int:
    print("=" * 88)
    print("PMNS CURRENT BANK VALUE-SELECTION NO-GO")
    print("=" * 88)
    print()
    print("Question:")
    print("  Do the checked free, scalar, residual-symmetry, coordinate, and")
    print("  target-constructed-fixture mechanisms select a unique value?")

    part1_free_and_scalar_routes_are_too_small()
    part2_graph_first_restricts_a_supplied_candidate_family()
    part3_target_constructed_round_trips_do_not_select_a_value()
    part4_circularity_guard()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Checked-mechanism boundary:")
    print("    - the checked free response profile is rejected")
    print("    - the checked scalar deformation route stays too small")
    print("    - graph-first residual symmetry restricts a supplied candidate")
    print("      block to the reduced oriented forward-cycle family")
    print("    - target-constructed response fixtures round-trip supplied reduced")
    print("      blocks as consistency checks only")
    print("    - none of these checked mechanisms selects a unique value")
    print()
    print("  This is not an exhaustive route inventory. A physical carrier,")
    print("  Record-compatible readout, block-construction law, and numerical")
    print("  selector remain separate open bridges.")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
