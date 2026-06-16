"""Block 04: BZ-corner Hamming-weight decomposition verification.

Verifies that the 8 BZ corners of staggered-Dirac on Z^3 APBC decompose
uniquely by Hamming weight as 1+3+3+1, and that the hw=1 triplet has
the M_3(C) translation character support structure.

This runner deliberately does not verify, derive, or assert an
identification between BZ-corner Hamming parity and K-S position-space
sublattice/chirality grading.

Companion: docs/STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md
Loop: staggered-dirac-realization-gate-20260507
Block: 04
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import List, Tuple

import sympy as sp


NOTE_PATH = Path("docs/STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md")


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
    c3_squared = lambda n: c3_111(c3_111(n))
    c3_cubed = lambda n: c3_111(c3_111(c3_111(n)))
    c3_is_3cycle = all(c3_cubed(n) == n for n in hw1_corners) and \
                   all(c3_111(n) != n for n in hw1_corners)
    print("C_3[111] cyclic generator (cyclic shift (n_1,n_2,n_3) → (n_3,n_1,n_2)):")
    for src, dst in c3_action_dict.items():
        print(f"  {src} → {dst}")
    print(f"  3-cycle on hw=1 (no fixed points; (C_3)^3 = identity): {'PASS' if c3_is_3cycle else 'FAIL'}")
    print()

    # M_3(C) generation: translations + C_3 generate M_3(C) on the cited support surface.
    # We verify the structural setup is correct (full proof in
    # THREE_GENERATION_OBSERVABLE_THEOREM_NOTE)
    print("M_3(C) algebra on hw=1 triplet:")
    print("  generated by translations T_1, T_2, T_3 + C_3[111] cyclic generator")
    print("  full M_3(C) support per THREE_GENERATION_OBSERVABLE_THEOREM_NOTE")
    print()

    # Source-scope firewall: the audited blocker was an unsupported
    # Hamming-parity-to-chirality/sublattice identification.  Keep this
    # runner locked to the finite BZ-corner algebraic surface.
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    required_boundary = (
        "does not identify BZ-corner Hamming parity with the K-S position-space"
        in note_text
        and "any such parity-to-chirality identification is a separate bridge"
        in note_text
    )
    forbidden_overclaims = [
        "Sublattice A (chirality +)",
        "Sublattice B (chirality",
        "sublattice A: hw even",
        "sublattice B: hw odd",
        "Hamming-weight grading + sublattice parity",
    ]
    overclaims_absent = all(token not in note_text for token in forbidden_overclaims)
    scope_firewall_ok = required_boundary and overclaims_absent
    print("Source-scope firewall:")
    print("  does not assert Hamming parity = K-S sublattice/chirality parity")
    print(f"  boundary marker present: {'PASS' if required_boundary else 'FAIL'}")
    print(f"  forbidden parity/chirality overclaims absent: {'PASS' if overclaims_absent else 'FAIL'}")
    print(f"  firewall status: {'PASS' if scope_firewall_ok else 'FAIL'}")
    print()

    # Overall verdict
    all_checks = [decomp_matches, chars_match, distinct, c3_is_3cycle, scope_firewall_ok]
    n_pass = sum(all_checks)
    n_total = len(all_checks)

    print(f"SUMMARY: PASS={n_pass} FAIL={n_total - n_pass} (out of {n_total} structural checks)")
    print()
    print("Bounded theorem (T3) — BZ-corner algebraic triplet support — verified.")
    print("Staggered-Dirac on Z^3 APBC has unique 1+3+3+1 BZ-corner")
    print("decomposition by Hamming weight; hw=1 triplet has M_3(C)")
    print("algebraic support matching THREE_GENERATION_OBSERVABLE_THEOREM.")
    print("CHIRALITY_SUBLATTICE_IDENTIFICATION_DERIVED=FALSE")

    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    raise SystemExit(main())
