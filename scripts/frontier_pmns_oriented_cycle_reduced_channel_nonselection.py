#!/usr/bin/env python3
"""Algebraic nonselection check on the supplied reduced cycle family.

Question:
  On an explicitly supplied graph-first-symmetric reduced-cycle family, does
  residual symmetry, coordinate extraction, and a target-constructed fixture
  select a unique point?

Answer:
  The supplied coordinate map does not select a point. It only extracts the
  coordinates of whichever matrix is supplied.

  The exact reduced family is

      A_fwd(u, v, w) = (u + i v) E12 + w E23 + (u - i v) E31

  and every point of that 3-real family:

    - satisfies the graph-first residual antiunitary symmetry
    - has its coordinates extracted by the bounded algebraic cycle lemma
    - can be round-tripped through a target-constructed response fixture as a
      consistency check

  The fixture round trip is not independent physical realization evidence and
  is not used as a carrier, readout, or value-selection theorem.
"""

from __future__ import annotations

import sys

import numpy as np

from frontier_pmns_oriented_cycle_channel_value_law import oriented_cycle_coeffs_from_block
from frontier_pmns_oriented_cycle_selection_structure import P23
from pmns_lower_level_utils import (
    I3,
    active_response_columns_from_sector_operator,
    derive_active_block_from_response_columns,
    sector_operator_fixture_from_effective_block,
    support_mask,
)

np.set_printoptions(precision=6, suppress=True, linewidth=140)

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


def e(i: int, j: int) -> np.ndarray:
    out = np.zeros((3, 3), dtype=complex)
    out[i, j] = 1.0
    return out


E12 = e(0, 1)
E23 = e(1, 2)
E31 = e(2, 0)
TARGET_SUPPORT = (np.abs(I3 + E12 + E23 + E31) > 0).astype(int)


def residual_swap_conjugate(a: np.ndarray) -> np.ndarray:
    return P23 @ a.conj().T @ P23


def reduced_cycle_block(u: float, v: float, w: float) -> np.ndarray:
    return (u + 1j * v) * E12 + w * E23 + (u - 1j * v) * E31


def reduced_cycle_coordinates(a: np.ndarray) -> np.ndarray:
    coeffs = oriented_cycle_coeffs_from_block(a)
    return np.array([np.real(coeffs[0]), np.imag(coeffs[0]), np.real(coeffs[1])], dtype=float)


def active_block_with_reduced_cycle(u: float, v: float, w: float, xbar: float = 1.0) -> np.ndarray:
    return xbar * I3 + reduced_cycle_block(u, v, w)


def part1_the_graph_first_symmetric_family_is_exactly_three_real_dimensional() -> None:
    print("\n" + "=" * 88)
    print("PART 1: THE GRAPH-FIRST-SYMMETRIC FAMILY IS EXACTLY 3-REAL DIMENSIONAL")
    print("=" * 88)

    u, v, w = 0.41, 0.32, 0.28
    a = reduced_cycle_block(u, v, w)
    coeffs = oriented_cycle_coeffs_from_block(a)
    coords = reduced_cycle_coordinates(a)

    check("The reduced graph-first cycle block is fixed by the residual antiunitary symmetry",
          np.linalg.norm(residual_swap_conjugate(a) - a) < 1e-12,
          f"error={np.linalg.norm(residual_swap_conjugate(a) - a):.2e}")
    check("Its exact oriented-cycle coefficients are (u+iv, w, u-iv)",
          np.linalg.norm(coeffs - np.array([u + 1j * v, w, u - 1j * v], dtype=complex)) < 1e-12,
          f"coeffs={np.round(coeffs, 6)}")
    check("The bounded algebraic extractor recovers the reduced real coordinates exactly",
          np.linalg.norm(coords - np.array([u, v, w], dtype=float)) < 1e-12,
          f"coords={np.round(coords, 6)}")


def part2_target_constructed_response_round_trip_is_consistency_only() -> None:
    print("\n" + "=" * 88)
    print("PART 2: TARGET-CONSTRUCTED RESPONSE ROUND TRIP IS CONSISTENCY-ONLY")
    print("=" * 88)

    lam = 0.31
    u, v, w = 0.37, -0.19, 0.24
    target = active_block_with_reduced_cycle(u, v, w, xbar=1.08)
    sector = sector_operator_fixture_from_effective_block(target, seed=5831)
    _block, columns = active_response_columns_from_sector_operator(sector, lam)
    _kernel, recovered = derive_active_block_from_response_columns(columns, lam)
    coeffs = oriented_cycle_coeffs_from_block(recovered)

    check("The target-constructed response fixture round-trips to the supplied block",
          np.linalg.norm(recovered - target) < 1e-12,
          f"error={np.linalg.norm(recovered - target):.2e}")
    check("The round-tripped block stays on the specified diagonal-plus-forward-cycle support",
          np.array_equal(support_mask(recovered), TARGET_SUPPORT))
    check("Algebraic extraction after the round trip returns the supplied coordinates",
          np.linalg.norm(coeffs - np.array([u - 0.19j, 0.24, u + 0.19j], dtype=complex)) < 1e-12,
          f"coeffs={np.round(coeffs, 6)}")
    print("  [INFO] The fixture was constructed from the target block; this is not")
    print("  [INFO] independent physical carrier or Record-readout evidence.")


def part3_checked_constraints_do_not_select_a_unique_reduced_channel_point() -> None:
    print("\n" + "=" * 88)
    print("PART 3: THE CHECKED CONSTRAINTS DO NOT SELECT A UNIQUE REDUCED-CHANNEL POINT")
    print("=" * 88)

    a = active_block_with_reduced_cycle(0.41, 0.32, 0.28, xbar=1.0)
    b = active_block_with_reduced_cycle(0.29, -0.17, 0.34, xbar=1.0)
    ca = reduced_cycle_coordinates(a)
    cb = reduced_cycle_coordinates(b)

    check("Two distinct reduced-channel points satisfy the same residual antiunitary symmetry",
          np.linalg.norm(residual_swap_conjugate(a) - a) < 1e-12
          and np.linalg.norm(residual_swap_conjugate(b) - b) < 1e-12
          and np.linalg.norm(a - b) > 1e-6,
          f"|A-B|={np.linalg.norm(a - b):.6f}")
    check("They are separated by the algebraic coordinate map rather than collapsed by it",
          np.linalg.norm(ca - cb) > 1e-6,
          f"|Δcoords|={np.linalg.norm(ca - cb):.6f}")
    print("  [INFO] Coordinate extraction is not value selection.")
    print("  [INFO] The physical carrier, readout, and matrix-selection bridges remain open.")


def main() -> int:
    print("=" * 88)
    print("PMNS ORIENTED CYCLE REDUCED-CHANNEL NONSELECTION")
    print("=" * 88)
    print()
    print("Question:")
    print("  On an explicitly supplied graph-first-symmetric reduced-cycle family,")
    print("  do the checked residual, coordinate, and fixture mechanisms select")
    print("  a unique point?")

    part1_the_graph_first_symmetric_family_is_exactly_three_real_dimensional()
    part2_target_constructed_response_round_trip_is_consistency_only()
    part3_checked_constraints_do_not_select_a_unique_reduced_channel_point()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Bounded algebraic checks on the supplied reduced-cycle family:")
    print("    - the graph-first-symmetric supplied family is exactly 3-real dimensional")
    print("    - supplied coordinates are extracted exactly by the cycle-coordinate lemma")
    print("    - the target-constructed response fixture is consistency-only")
    print("    - coordinate extraction does not select a unique reduced-channel value")
    print()
    print("  A retained carrier, Record-compatible readout, and A/value-selection")
    print("  theorem remain separate open bridges.")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
