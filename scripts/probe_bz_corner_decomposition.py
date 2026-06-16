"""Block 04: BZ-corner Hamming-weight decomposition verification.

Verifies that the 8 BZ corners of staggered-Dirac on Z^3 APBC decompose
uniquely by Hamming weight as 1+3+3+1, and that the hw=1 triplet has
the M_3(C) translation character support structure.

Companion: docs/STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md
Loop: staggered-dirac-realization-gate-20260507
Block: 04
"""
from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from pathlib import Path
from typing import List, Tuple

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md"


def enumerate_bz_corners() -> List[Tuple[int, int, int]]:
    """Enumerate all 8 BZ corners of staggered fermion on Z^3 APBC.

    Each corner is labeled by binary (n_1, n_2, n_3) with k_μ = n_μ · π.
    """
    return [(n1, n2, n3) for n1 in (0, 1) for n2 in (0, 1) for n3 in (0, 1)]


def hamming_weight(n: Tuple[int, int, int]) -> int:
    """Hamming weight: number of 1s in the binary corner label."""
    return sum(n)


def translation_character(n: Tuple[int, int, int], direction: int) -> int:
    """Character of lattice translation T_μ on BZ corner n.

    T_μ acts as exp(i k_μ) = (−1)^{n_μ} on corner with k_μ = n_μ · π.
    """
    n1, n2, n3 = n
    if direction == 1:
        return (-1) ** n1
    elif direction == 2:
        return (-1) ** n2
    elif direction == 3:
        return (-1) ** n3
    else:
        raise ValueError("direction must be 1, 2, or 3")


def diagonal_translation_matrix(hw1_corners: list[Tuple[int, int, int]], direction: int) -> sp.Matrix:
    return sp.diag(*[translation_character(n, direction) for n in hw1_corners])


def projector_from_characters(translations: list[sp.Matrix], chars: tuple[int, int, int]) -> sp.Matrix:
    eye = sp.eye(3)
    out = eye
    for sign, translation in zip(chars, translations):
        out *= (eye + sign * translation) / 2
    return sp.simplify(out)


def cycle_matrix(hw1_corners: list[Tuple[int, int, int]]) -> sp.Matrix:
    """Matrix of the C_3[111] corner cycle restricted to hw=1."""

    index = {corner: i for i, corner in enumerate(hw1_corners)}

    def c3_111(n: Tuple[int, int, int]) -> Tuple[int, int, int]:
        return (n[2], n[0], n[1])

    out = sp.zeros(3, 3)
    for src, corner in enumerate(hw1_corners):
        dst = index[c3_111(corner)]
        out[dst, src] = 1
    return out


def matrix_unit(i: int, j: int) -> sp.Matrix:
    out = sp.zeros(3, 3)
    out[i, j] = 1
    return out


def span_dimension(mats: list[sp.Matrix]) -> int:
    """Dimension of the complex linear span of 3x3 matrices."""

    cols = [sp.Matrix(9, 1, list(mat)) for mat in mats]
    return sp.Matrix.hstack(*cols).rank()


def epsilon_corner_shift(n: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """Momentum-space action of position-space epsilon(x)=(-1)^(x1+x2+x3).

    Multiplication by epsilon shifts momentum by pi(1,1,1), so on binary
    BZ-corner labels it complements every bit.
    """

    return tuple(1 - bit for bit in n)


def main() -> int:
    print("=" * 72)
    print("Block 04 — BZ-Corner Decomposition Verification")
    print("Loop: staggered-dirac-realization-gate-20260507")
    print("Companion: docs/STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md")
    print("=" * 72)
    print()

    corners = enumerate_bz_corners()
    print(f"Total BZ corners: {len(corners)} (= 2^3 on staggered Z^3 APBC)")
    print()

    # Group by Hamming weight
    by_hw = defaultdict(list)
    for n in corners:
        by_hw[hamming_weight(n)].append(n)

    print("Hamming-weight decomposition:")
    for hw in sorted(by_hw.keys()):
        corners_at_hw = by_hw[hw]
        print(f"  hw={hw}: {len(corners_at_hw)} corner(s) → {corners_at_hw}")

    expected_decomp = {0: 1, 1: 3, 2: 3, 3: 1}
    actual_decomp = {hw: len(by_hw[hw]) for hw in sorted(by_hw.keys())}
    decomp_matches = expected_decomp == actual_decomp

    print()
    print(f"Expected: 1+3+3+1 = 8")
    print(f"Actual:   {'+'.join(str(actual_decomp[hw]) for hw in sorted(actual_decomp.keys()))} = {sum(actual_decomp.values())}")
    print(f"  {'PASS' if decomp_matches else 'FAIL'}")
    print()

    # hw=1 triplet translation characters
    hw1_corners = by_hw[1]
    print("hw=1 triplet translation characters (T_1, T_2, T_3):")
    print()
    print(f"{'corner':>15} {'T_1':>5} {'T_2':>5} {'T_3':>5}")
    char_matrix = []
    for n in hw1_corners:
        chars = tuple(translation_character(n, μ) for μ in (1, 2, 3))
        char_matrix.append(chars)
        print(f"{str(n):>15} {chars[0]:>5} {chars[1]:>5} {chars[2]:>5}")
    print()

    # Verify the diag(-1, +1, +1) etc structure (order-agnostic)
    expected_chars_set = {
        (-1, 1, 1),   # T_1 = −1, T_2 = +1, T_3 = +1
        (1, -1, 1),   # T_1 = +1, T_2 = −1, T_3 = +1
        (1, 1, -1),   # T_1 = +1, T_2 = +1, T_3 = −1
    }
    chars_match = set(char_matrix) == expected_chars_set
    print(f"Expected (as set): {{(−1,+1,+1), (+1,−1,+1), (+1,+1,−1)}}")
    print(f"   (matches THREE_GENERATION_OBSERVABLE_THEOREM_NOTE support surface, order-agnostic)")
    print(f"  {'PASS' if chars_match else 'FAIL'}")
    print()

    # Distinct joint characters check
    joint_chars = set(char_matrix)
    distinct = len(joint_chars) == 3
    print(f"Joint characters distinct: {len(joint_chars)} unique tuples (expected 3)")
    print(f"  {'PASS' if distinct else 'FAIL'}")
    print()

    # C_3[111] cyclic generator: order-agnostic 3-cycle on hw=1 corners
    # Define the C_3 action as cyclic shift of indices: (n_1, n_2, n_3) → (n_3, n_1, n_2)
    def c3_111(n: Tuple[int, int, int]) -> Tuple[int, int, int]:
        return (n[2], n[0], n[1])
    c3_action_dict = {n: c3_111(n) for n in hw1_corners}
    # Apply C_3 three times — should return to identity
    c3_cubed = lambda n: c3_111(c3_111(c3_111(n)))
    c3_is_3cycle = all(c3_cubed(n) == n for n in hw1_corners) and \
                   all(c3_111(n) != n for n in hw1_corners)
    print("C_3[111] cyclic generator (cyclic shift (n_1,n_2,n_3) → (n_3,n_1,n_2)):")
    for src, dst in c3_action_dict.items():
        print(f"  {src} → {dst}")
    print(f"  3-cycle on hw=1 (no fixed points; (C_3)^3 = identity): {'PASS' if c3_is_3cycle else 'FAIL'}")
    print()

    # M_3(C) generation is checked directly here, not imported from the
    # parent support note.  The parent is a parallel citation for the same
    # finite algebra.
    print("M_3(C) algebra on hw=1 triplet (native finite check):")
    translations = [diagonal_translation_matrix(hw1_corners, μ) for μ in (1, 2, 3)]
    projectors = [
        projector_from_characters(translations, tuple(translation_character(n, μ) for μ in (1, 2, 3)))
        for n in hw1_corners
    ]
    C3 = cycle_matrix(hw1_corners)
    C3_powers = [sp.eye(3), C3, C3 ** 2]

    projector_idempotent = all(P * P == P for P in projectors)
    projector_orthogonal = all(
        projectors[i] * projectors[j] == sp.zeros(3, 3)
        for i in range(3)
        for j in range(3)
        if i != j
    )
    projector_rank1 = all(P.rank() == 1 for P in projectors)
    projectors_resolve_identity = sum(projectors, sp.zeros(3, 3)) == sp.eye(3)
    print(f"  translation-character projectors idempotent: {'PASS' if projector_idempotent else 'FAIL'}")
    print(f"  translation-character projectors orthogonal:  {'PASS' if projector_orthogonal else 'FAIL'}")
    print(f"  translation-character projectors rank one:    {'PASS' if projector_rank1 else 'FAIL'}")
    print(f"  projectors resolve I_3:                       {'PASS' if projectors_resolve_identity else 'FAIL'}")

    matrix_units = []
    recovered_units = []
    for i in range(3):
        for j in range(3):
            target = matrix_unit(i, j)
            candidates = [projectors[i] * C_power * projectors[j] for C_power in C3_powers]
            matrix_units.append(target)
            recovered_units.append(any(candidate == target for candidate in candidates))
    all_matrix_units_recovered = all(recovered_units)
    generated_span = []
    for left in projectors:
        for C_power in C3_powers:
            for right in projectors:
                generated_span.append(left * C_power * right)
    generated_dimension = span_dimension(generated_span)
    full_m3_generated = generated_dimension == 9 and all_matrix_units_recovered
    print(f"  all nine matrix units P_i C3^k P_j recovered: {'PASS' if all_matrix_units_recovered else 'FAIL'}")
    print(f"  generated algebra span dimension: {generated_dimension} (expected 9)")
    print(f"  translations + C3[111] generate M_3(C):        {'PASS' if full_m3_generated else 'FAIL'}")
    print()

    # No-proper-quotient boundary: D_3 projectors force invariant subspaces to
    # coordinate subsets, and the three-cycle has no nonempty proper invariant
    # subset on {0,1,2}.
    print("No-proper-subspace / quotient check on hw=1:")
    c3_index_action = {}
    for src, corner in enumerate(hw1_corners):
        c3_index_action[src] = hw1_corners.index(c3_111(corner))
    nontrivial_subsets = [
        set(combo)
        for r in (1, 2)
        for combo in combinations(range(3), r)
    ]
    invariant_subsets = [
        subset
        for subset in nontrivial_subsets
        if {c3_index_action[i] for i in subset} == subset
    ]
    no_proper_subspace = invariant_subsets == []
    print(f"  D_3-invariant candidates checked: {len(nontrivial_subsets)}")
    print(f"  nonempty proper candidates also C3-invariant: {invariant_subsets}")
    print(f"  no proper nonzero subspace preserves D_3 and C3: {'PASS' if no_proper_subspace else 'FAIL'}")
    print()

    # Correct boundary for the post-audit blocker: position-space staggered
    # epsilon is not a diagonal Hamming-parity/chirality label on the BZ-corner
    # basis.  It shifts k by pi(1,1,1), i.e. complements all three corner bits.
    print("Position-space epsilon boundary on BZ-corner labels:")
    epsilon_pairs = {n: epsilon_corner_shift(n) for n in corners}
    for src, dst in sorted(epsilon_pairs.items()):
        print(f"  epsilon: {src} -> {dst} (hw {hamming_weight(src)} -> {hamming_weight(dst)})")
    epsilon_involution = all(epsilon_corner_shift(epsilon_corner_shift(n)) == n for n in corners)
    epsilon_flips_hw_parity = all(
        hamming_weight(epsilon_corner_shift(n)) % 2 != hamming_weight(n) % 2
        for n in corners
    )
    hw1_maps_to_hw2 = all(hamming_weight(epsilon_corner_shift(n)) == 2 for n in hw1_corners)
    hamming_parity_balanced = (
        sum(len(by_hw[hw]) for hw in (0, 2)) == 4
        and sum(len(by_hw[hw]) for hw in (1, 3)) == 4
    )
    print(f"  epsilon complement action is involutive:         {'PASS' if epsilon_involution else 'FAIL'}")
    print(f"  epsilon flips Hamming parity in d=3:             {'PASS' if epsilon_flips_hw_parity else 'FAIL'}")
    print(f"  epsilon maps hw=1 triplet to hw=2 triplet:       {'PASS' if hw1_maps_to_hw2 else 'FAIL'}")
    print(f"  Hamming even/odd counts are balanced 4+4:        {'PASS' if hamming_parity_balanced else 'FAIL'}")
    print("  Boundary: no diagonal sublattice/chirality identification is claimed here.")
    print()

    # Source-scope firewall: the post-audit defect was an unsupported
    # Hamming-parity-to-chirality/sublattice identification. Keep the note
    # locked to the finite BZ-corner algebraic surface.
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    required_boundary = (
        "BZ-corner Hamming parity with the K-S" in note_text
        and "parity-to-chirality identification is a separate bridge" in note_text
    )
    forbidden_overclaims = [
        "Sublattice A (chirality +)",
        "Sublattice B (chirality",
        "sublattice A: hw even",
        "sublattice B: hw odd",
        "Hamming-weight grading + sublattice parity",
    ]
    overclaims_absent = all(token not in note_text for token in forbidden_overclaims)
    source_scope_firewall_ok = required_boundary and overclaims_absent
    print("Source-scope firewall:")
    print("  does not assert Hamming parity = K-S sublattice/chirality parity")
    print(f"  boundary marker present: {'PASS' if required_boundary else 'FAIL'}")
    print(f"  forbidden parity/chirality overclaims absent: {'PASS' if overclaims_absent else 'FAIL'}")
    print(f"  firewall status: {'PASS' if source_scope_firewall_ok else 'FAIL'}")
    print()

    # Overall verdict
    all_checks = [
        decomp_matches,
        chars_match,
        distinct,
        c3_is_3cycle,
        projector_idempotent,
        projector_orthogonal,
        projector_rank1,
        projectors_resolve_identity,
        all_matrix_units_recovered,
        full_m3_generated,
        no_proper_subspace,
        epsilon_involution,
        epsilon_flips_hw_parity,
        hw1_maps_to_hw2,
        hamming_parity_balanced,
        source_scope_firewall_ok,
    ]
    n_pass = sum(all_checks)
    n_total = len(all_checks)

    print(f"SUMMARY: PASS={n_pass} FAIL={n_total - n_pass} (out of {n_total} structural checks)")
    print()
    print("Bounded theorem (T3) — BZ-corner algebraic triplet support — verified.")
    print("Staggered-Dirac on Z^3 APBC has unique 1+3+3+1 BZ-corner")
    print("decomposition by Hamming weight; hw=1 triplet has M_3(C)")
    print("algebraic support and no-proper-subspace closure. Epsilon/chirality")
    print("is fenced off: position-space epsilon complements BZ-corner bits.")
    print("CHIRALITY_SUBLATTICE_IDENTIFICATION_DERIVED=FALSE")

    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    raise SystemExit(main())
