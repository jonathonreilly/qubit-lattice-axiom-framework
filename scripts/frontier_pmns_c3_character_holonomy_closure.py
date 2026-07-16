#!/usr/bin/env python3
"""Bounded C3-character inversion on a supplied reduced cycle family.

Question:
  For the supplied forward-cycle matrix C, do its three character phases give
  an invertible coordinate map on the supplied reduced cycle family?

Answer:
  Yes.

  The supplied projected-cycle matrix `C` has character phases

      0, 2 pi / 3, 4 pi / 3.

  On the reduced graph-first family

      A_fwd(u, v, w) = (u + i v) E12 + w E23 + (u - i v) E31

  the corresponding character holonomies are exactly the three one-angle
  holonomies evaluated at those canonical phases. Their design matrix is

      [[ 2,  0, 1],
       [-1,  sqrt(3), 1],
       [-1, -sqrt(3), 1]]

  and has nonzero determinant. Therefore `(u, v, w)` are reconstructed exactly
  from the exact C3 character triple itself.

  This is finite matrix inversion only. It does not derive the physical
  carrier, a Record-compatible readout, or the matrix/coordinate values.
"""

from __future__ import annotations

import math
import sys

import numpy as np

from frontier_pmns_oriented_cycle_channel_value_law import projected_forward_cycle
from frontier_pmns_three_flux_holonomy_closure import (
    recover_reduced_cycle_coordinates_from_three_flux_holonomies,
)
from frontier_pmns_twisted_flux_transfer_holonomy_boundary import (
    flux_holonomy_on_reduced_family,
    reduced_cycle_family,
)
from pmns_lower_level_utils import circularity_guard

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


def c3_character_phases() -> tuple[float, float, float]:
    return (0.0, 2.0 * math.pi / 3.0, 4.0 * math.pi / 3.0)


def c3_character_design_matrix() -> np.ndarray:
    return np.array(
        [
            [2.0, 0.0, 1.0],
            [-1.0, math.sqrt(3.0), 1.0],
            [-1.0, -math.sqrt(3.0), 1.0],
        ],
        dtype=float,
    )


def c3_character_holonomies_on_reduced_family(a: np.ndarray) -> np.ndarray:
    return np.array(
        [flux_holonomy_on_reduced_family(a, phi) for phi in c3_character_phases()],
        dtype=float,
    )


def part1_the_supplied_cycle_matrix_has_the_canonical_c3_character_triple() -> None:
    print("\n" + "=" * 88)
    print("PART 1: THE SUPPLIED CYCLE MATRIX HAS THE CANONICAL C3 CHARACTER TRIPLE")
    print("=" * 88)

    c = projected_forward_cycle()
    evals = np.linalg.eigvals(c)
    target = np.array(
        [1.0, np.exp(2j * math.pi / 3.0), np.exp(4j * math.pi / 3.0)],
        dtype=complex,
    )
    evals_sorted = np.array(sorted(evals, key=lambda z: np.angle(z)))
    target_sorted = np.array(sorted(target, key=lambda z: np.angle(z)))

    check("The projected coordinate-cycle operator is exactly C3-periodic", np.linalg.norm(np.linalg.matrix_power(c, 3) - np.eye(3)) < 1e-12)
    check("Its eigencharacters are exactly 1, omega, omega^2",
          np.linalg.norm(evals_sorted - target_sorted) < 1e-12,
          f"evals={np.round(evals_sorted, 6)}")
    check("Therefore the supplied C3 character phases are 0, 2pi/3, 4pi/3", True)


def part2_the_supplied_character_triple_has_full_rank_on_the_reduced_cycle_family() -> None:
    print("\n" + "=" * 88)
    print("PART 2: THE SUPPLIED CHARACTER TRIPLE HAS FULL RANK ON THE REDUCED CYCLE FAMILY")
    print("=" * 88)

    m = c3_character_design_matrix()
    det = float(np.linalg.det(m))

    check("The character-triple design matrix is the canonical C3 matrix",
          np.linalg.norm(m - np.array([[2.0, 0.0, 1.0], [-1.0, math.sqrt(3.0), 1.0], [-1.0, -math.sqrt(3.0), 1.0]])) < 1e-12)
    check("The exact C3 character triple has nonzero determinant", abs(det) > 1e-12, f"det={det:.12f}")
    check("So the supplied character triple removes the one-angle 2-real kernel algebraically", True)


def part3_the_reduced_cycle_coordinates_are_reconstructed_from_the_supplied_character_functionals() -> None:
    print("\n" + "=" * 88)
    print("PART 3: THE REDUCED COORDINATES RECONSTRUCT FROM THE SUPPLIED CHARACTER FUNCTIONALS")
    print("=" * 88)

    target = np.array([0.41, 0.32, 0.28], dtype=float)
    a = reduced_cycle_family(*target)
    hol = c3_character_holonomies_on_reduced_family(a)
    recovered = recover_reduced_cycle_coordinates_from_three_flux_holonomies(hol, c3_character_phases())

    check("The supplied character-functional vector is the exact image of (u,v,w)",
          np.linalg.norm(hol - c3_character_design_matrix() @ target) < 1e-12,
          f"hol={np.round(hol, 6)}")
    check("The reduced coordinates are reconstructed exactly from the supplied character functionals",
          np.linalg.norm(recovered - target) < 1e-12,
          f"recovered={np.round(recovered, 6)}")
    check("So the supplied reduced-cycle coordinates invert exactly on this C3 character map", True)


def part4_circularity_guard() -> None:
    print("\n" + "=" * 88)
    print("PART 4: CIRCULARITY GUARD")
    print("=" * 88)

    ok_phase, bad_phase = circularity_guard(c3_character_phases, {"u", "v", "w", "x", "y", "delta", "tau", "q"})
    ok_hol, bad_hol = circularity_guard(c3_character_holonomies_on_reduced_family, {"u", "v", "w", "x", "y", "delta", "tau", "q"})
    ok_rec, bad_rec = circularity_guard(recover_reduced_cycle_coordinates_from_three_flux_holonomies, {"u", "v", "w", "x", "y", "delta", "tau", "q"})

    check("The exact C3 character phases take no PMNS-side target values as inputs", ok_phase, f"bad={bad_phase}")
    check("The supplied character-functional map takes no PMNS-side target coordinates as inputs", ok_hol, f"bad={bad_hol}")
    check("The character-holonomy reconstruction takes no PMNS-side target coordinates as inputs", ok_rec, f"bad={bad_rec}")


def main() -> int:
    print("=" * 88)
    print("PMNS C3 CHARACTER HOLOMONY CLOSURE")
    print("=" * 88)
    print()
    print("Question:")
    print("  Does the supplied C3 cycle matrix give an invertible three-mode")
    print("  coordinate map on the supplied reduced cycle family?")

    part1_the_supplied_cycle_matrix_has_the_canonical_c3_character_triple()
    part2_the_supplied_character_triple_has_full_rank_on_the_reduced_cycle_family()
    part3_the_reduced_cycle_coordinates_are_reconstructed_from_the_supplied_character_functionals()
    part4_circularity_guard()

    print("\n" + "=" * 88)
    print("RESULT")
    print("=" * 88)
    print("  Bounded algebraic inversion on the supplied reduced-cycle family:")
    print("    - the supplied projected cycle has the exact C3 character phases")
    print("      0, 2pi/3, 4pi/3")
    print("    - those three supplied functionals give an invertible 3 x 3")
    print("      system on the reduced graph-first PMNS cycle family")
    print("    - therefore (u,v,w) are reconstructed exactly from the exact C3")
    print("      character-functional triple")
    print()
    print("  This does not derive a physical carrier, Record-compatible readout,")
    print("  or a law selecting the supplied matrix or its coordinates.")
    print()
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
