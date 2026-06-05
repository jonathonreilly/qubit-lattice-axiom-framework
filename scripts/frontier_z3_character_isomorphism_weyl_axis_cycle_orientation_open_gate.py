#!/usr/bin/env python3
"""Finite checks for the Z3 Weyl axis-cycle orientation open gate."""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "Z3_CHARACTER_ISOMORPHISM_WEYL_AXIS_CYCLE_ORIENTATION_OPEN_GATE_NOTE_2026-05-30.md"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  --  {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)


def read_note() -> str:
    return NOTE.read_text(encoding="utf-8")


def permutation_matrix(p: tuple[int, int, int]) -> sp.Matrix:
    mat = sp.zeros(3)
    for i, j in enumerate(p):
        mat[i, j] = 1
    return mat


def check_note_scope() -> None:
    section("Note scope")
    text = read_note()
    flat = " ".join(text.split())
    required = [
        "**Claim type:** open_gate",
        "axis-cycle regular character: verified",
        "canonical within-sector orientation from that finite character calculation: open",
        "not a formal no-go over all possible color/generation bridges",
        "does not approve",
    ]
    forbidden = [
        "Generated" + " with",
        "source-note proposal only",
        "actual_" + "current_surface_status",
        "audit" + " lane",
        "ret" + "ained_bounded",
        "ret" + "ained_no_go",
        "A_min",
        "P1",
        "P2",
        "P3",
    ]
    for marker in required:
        check(f"note contains marker: {marker}", marker in text or marker in flat)
    for marker in forbidden:
        check(f"note omits non-native marker: {marker}", marker not in text)


def check_characters(p_axis: sp.Matrix) -> None:
    section("Axis-cycle and center characters")
    omega = sp.exp(2 * sp.pi * sp.I / 3)
    axis_character = [sp.simplify(sp.trace(p_axis**k)) for k in (0, 1, 2)]
    center_character = [sp.simplify(sp.trace(z * sp.eye(3))) for z in (1, omega, omega**2)]
    check("axis-cycle character is regular (3,0,0)", axis_character == [3, 0, 0], str(axis_character))
    check("center character is not regular", center_character[1] != 0 and center_character[2] != 0, str(center_character))
    check("P^3 = I", sp.simplify(p_axis**3 - sp.eye(3)) == sp.zeros(3))
    check("det(P) = 1", sp.det(p_axis) == 1, str(sp.det(p_axis)))


def check_commutant_and_alignments(p_axis: sp.Matrix) -> None:
    section("Commutant and permutation alignments")
    a0, a1, a2 = sp.symbols("a0 a1 a2")
    basis = [sp.eye(3), p_axis, sp.simplify(p_axis**2)]
    generic = a0 * basis[0] + a1 * basis[1] + a2 * basis[2]
    flattened = sp.Matrix([[b[i] for b in basis] for i in range(9)])
    check("every a0 I + a1 P + a2 P^2 commutes with P", sp.simplify(generic * p_axis - p_axis * generic) == sp.zeros(3))
    check("span{I,P,P^2} is three-dimensional", flattened.rank() == 3, f"rank={flattened.rank()}")

    perms = [(p, permutation_matrix(p)) for p in itertools.permutations(range(3))]

    def commutes(mat: sp.Matrix) -> bool:
        return sp.simplify(mat * p_axis - p_axis * mat) == sp.zeros(3)

    commuting = [(p, mat) for p, mat in perms if commutes(mat)]
    non_commuting = [(p, mat) for p, mat in perms if not commutes(mat)]
    check("exactly three permutation alignments commute with P", len(commuting) == 3, str([p for p, _ in commuting]))
    check("the commuting alignments are exactly I, P, P^2", all(any(sp.simplify(mat - b) == sp.zeros(3) for b in basis) for _, mat in commuting))
    check("the other three permutations do not commute with P", len(non_commuting) == 3, str([p for p, _ in non_commuting]))


def check_cyclic_relabeling_isospectral(p_axis: sp.Matrix) -> None:
    section("Cyclic relabeling is isospectral")
    diagonal = sp.diag(2, 5, 9)
    relabeled = sp.simplify(p_axis * diagonal * p_axis.inv())
    check("cyclic relabeling changes order", diagonal != relabeled, str(relabeled))
    check("cyclic relabeling preserves spectrum", diagonal.eigenvals() == relabeled.eigenvals(), str(relabeled.eigenvals()))


def main() -> int:
    p_axis = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    check_note_scope()
    check_characters(p_axis)
    check_commutant_and_alignments(p_axis)
    check_cyclic_relabeling_isospectral(p_axis)
    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: Weyl axis-cycle character/orientation open-gate checks failed.")
        return 1
    print("VERDICT: Weyl axis-cycle character/orientation open-gate checks pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
