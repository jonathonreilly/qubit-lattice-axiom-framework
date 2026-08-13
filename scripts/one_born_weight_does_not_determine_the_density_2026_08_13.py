#!/usr/bin/env python3
"""Exact two-density witness: one Born weight does not recover the density.

Identity gates are born(rho, P) and equal_rho(rho0, rho1). Every same-weight
or distinct-density check calls those functions. The mutation predicate
“Tr(ρP) recovers ρ” is required to fail on the displayed pair.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ONE_BORN_WEIGHT_DOES_NOT_DETERMINE_THE_DENSITY_BOUNDED_THEOREM_NOTE_2026-08-13.md"
PARENT_PATH = ROOT / "docs" / "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ONE_BORN_WEIGHT_DOES_NOT_DETERMINE_THE_DENSITY_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def normalize(text: str) -> str:
    return " ".join(text.split())


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def trace(matrix: Matrix) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def det(matrix: Matrix) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def adjoint(matrix: Matrix) -> Matrix:
    return (
        (matrix[0][0], matrix[1][0]),
        (matrix[0][1], matrix[1][1]),
    )


def born(rho: Matrix, projector: Matrix) -> Fraction:
    return trace(matmul(rho, projector))


def equal_rho(rho0: Matrix, rho1: Matrix) -> bool:
    return rho0 == rho1


def density(diagonal: Fraction, off_diagonal: Fraction) -> Matrix:
    return (
        (diagonal, off_diagonal),
        (off_diagonal, Fraction(1) - diagonal),
    )


def recovers_rho(family: tuple[Matrix, ...], projector: Matrix) -> bool:
    """Predicate “Tr(ρP) recovers ρ”: each weight comes from exactly one density."""
    for rho in family:
        matches = [
            other
            for other in family
            if born(other, projector) == born(rho, projector)
        ]
        if len(matches) != 1:
            return False
    return True


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    normalized_parent = normalize(parent)

    print(
        "external_scientific_inputs: axiom wording and the August 9 parent "
        "are source-bound; no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency"
    )

    projector: Matrix = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )
    diagonal = Fraction(3, 5)
    rho0 = density(diagonal, Fraction(0))
    rho1 = density(diagonal, Fraction(1, 5))
    family = (rho0, rho1)

    checks.check(
        "projector-idempotent",
        "P is exactly P squared",
        matmul(projector, projector) == projector,
    )
    checks.check(
        "projector-hermitian",
        "P equals its adjoint",
        adjoint(projector) == projector,
    )
    checks.check(
        "rho0-density",
        "rho0 is Hermitian, trace one, and positive semidefinite",
        adjoint(rho0) == rho0
        and trace(rho0) == 1
        and rho0[0][0] > 0
        and det(rho0) == Fraction(6, 25)
        and det(rho0) >= 0
        and rho0[0][1] * rho0[0][1] <= rho0[0][0] * rho0[1][1],
    )
    checks.check(
        "rho1-density",
        "rho1 is Hermitian, trace one, and positive semidefinite",
        adjoint(rho1) == rho1
        and trace(rho1) == 1
        and rho1[0][0] > 0
        and det(rho1) == Fraction(1, 5)
        and det(rho1) > 0
        and rho1[0][1] * rho1[0][1] <= rho1[0][0] * rho1[1][1],
    )
    checks.check(
        "psd-witness-bound",
        "the off-diagonal of rho1 saturates 1/25 of the 6/25 product bound",
        rho1[0][1] * rho1[0][1] == Fraction(1, 25)
        and rho0[0][0] * rho0[1][1] == Fraction(6, 25),
    )
    checks.check(
        "born-rho0",
        "born(rho0, P) equals 3/5",
        born(rho0, projector) == Fraction(3, 5),
    )
    checks.check(
        "born-rho1",
        "born(rho1, P) equals 3/5",
        born(rho1, projector) == Fraction(3, 5),
    )
    checks.check(
        "same-weight",
        "the two densities share one Born weight on P",
        born(rho0, projector) == born(rho1, projector),
    )
    checks.check(
        "distinct-rho",
        "equal_rho(rho0, rho1) is false because the off-diagonals differ",
        not equal_rho(rho0, rho1) and rho0[0][1] != rho1[0][1],
    )
    checks.check(
        "diagonal-entry",
        "born(rho, P) returns the (0,0) entry for this P",
        born(rho0, projector) == rho0[0][0] and born(rho1, projector) == rho1[0][0],
    )
    checks.check(
        "not-half-trace",
        "the witness diagonal is 3/5, not 1/2",
        diagonal == Fraction(3, 5) and diagonal != Fraction(1, 2),
    )
    checks.check(
        "mutation-recovers",
        "the predicate Tr(rho P) recovers rho fails on {rho0, rho1}",
        recovers_rho(family, projector) is False,
    )

    record_lock = "a record locks exactly one admissible local possibility"
    record_count = "`I` is additive, with `I(empty)=0`"
    admissibility = (
        "the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions"
    )
    checks.check(
        "source-record",
        "the axiom memo names a lock as one possibility and I as an additive count",
        record_lock in normalized_axiom and record_count in axiom,
    )
    checks.check(
        "source-admissibility",
        "the axiom memo names a neighbor-determined possibility distribution",
        admissibility in normalized_axiom,
    )
    checks.check(
        "source-parent",
        "the August 9 parent still states unique density after low-arity grading",
        all(
            phrase in parent
            for phrase in (
                "menu-independent grading",
                "There is a unique density matrix",
                "w(E)=Tr(rho E)",
            )
        ),
    )
    checks.check(
        "note-witness",
        "the note displays Tr(ρ0 P)=Tr(ρ1 P)=3/5 and ρ0 ≠ ρ1",
        "Tr(ρ0 P) = Tr(ρ1 P) = 3/5" in normalized_note
        and "ρ0 ≠ ρ1" in note,
    )
    checks.check(
        "note-reconstruction",
        "the note states that one projector weight does not recover ρ",
        "A single Born weight on one projector does not recover `ρ`" in note
        and "The extra object for a state is the full density (or enough independent weights)"
        in normalized_note,
    )
    checks.check(
        "note-types",
        "the note quotes lock/count and refuses the distribution-to-density identification",
        "a lock is one admissible possibility; `I` is a count" in normalized_note
        and "A lock of a P-outcome is not `ρ0` or `ρ1`" in note
        and "A distribution over possibilities is not a density matrix without an identification"
        in normalized_note,
    )
    checks.check(
        "note-negative-scope",
        "the note keeps Born, August 9, and the axiom surface unmutated",
        "does not claim the Born form is false" in note
        and "does not replace" in note
        and "does not adopt `ρ` as axiom content" in note
        and "two-density witness" in note,
    )
    checks.check(
        "note-no-relaunch",
        "the note does not force r=1/2 and does not launch frame uniqueness",
        "does not force `r=1/2`" in note
        and "does not launch a frame-function uniqueness on all projectors" in note,
    )
    checks.check(
        "note-forbidden-surface",
        "the note has no adoption phrasing and cites no unmerged pull request",
        "we adopt" not in note.lower()
        and "pvmluders" not in note.lower()
        and "pvmselect" not in note.lower()
        and "bloch0" not in note.lower()
        and "nonaffine" not in note.lower()
        and "PR #" not in note
        and "github.com" not in note.lower(),
    )
    checks.check(
        "canonical-nonmutation",
        "the displayed witness matrices are absent from the canonical axiom file",
        all(phrase not in axiom for phrase in ("ρ0", "ρ1", "3/5", "oneweight")),
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "parent-not-overwritten",
        "the parent uniqueness sentence remains in the August 9 file",
        "rho` is unique" in parent or "ρ is unique" in normalized_parent,
    )

    print("per_element: two exact densities and one rank-one projector are checked")
    print("per_site: the underdetermination statement is one-site algebra on M_2(C)")
    print("per_mode: a=3/5 is the only diagonal used; r=1/2 is not forced")
    print("per_block: the rejected block is the predicate that one weight recovers rho")
    print("lattice_wide: checked and not executed — no lattice-wide claim is made")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
