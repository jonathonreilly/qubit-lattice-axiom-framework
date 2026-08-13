#!/usr/bin/env python3
"""Exact checks: the three-site cycle is not a unital M_3.

The runner builds the 8x8 0/1 permutation U |q1 q2 q3> = |q2 q3 q1> with
Fraction entries, checks the order-3 unitary identities, identifies C*(U)
with span{I,U,U^2}, and records that 3 does not divide 8. Hostile predicates
U^3 != I, dim C*(U) == 9, and 3 | 8 are evaluated and must fail.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "THREE_SITE_CYCLE_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/THREE_SITE_CYCLE_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


Matrix = tuple[tuple[Fraction, ...], ...]


def identity(n: int) -> Matrix:
    return tuple(
        tuple(Fraction(1 if row == column else 0) for column in range(n))
        for row in range(n)
    )


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return tuple(
        tuple(
            sum((left[row][mid] * right[mid][column] for mid in range(size)), Fraction(0))
            for column in range(size)
        )
        for row in range(size)
    )


def mat_transpose(matrix: Matrix) -> Matrix:
    size = len(matrix)
    return tuple(tuple(matrix[row][column] for row in range(size)) for column in range(size))


def frobenius(left: Matrix, right: Matrix) -> Fraction:
    size = len(left)
    return sum(
        (left[row][column] * right[row][column] for row in range(size) for column in range(size)),
        Fraction(0),
    )


def matrix_rank(rows: list[list[Fraction]]) -> int:
    work = [row[:] for row in rows]
    n_rows = len(work)
    n_cols = len(work[0]) if work else 0
    rank = 0
    column = 0
    for row in range(n_rows):
        pivot_row = None
        while column < n_cols:
            for candidate in range(row, n_rows):
                if work[candidate][column] != 0:
                    pivot_row = candidate
                    break
            if pivot_row is not None:
                break
            column += 1
        if column == n_cols:
            break
        work[row], work[pivot_row] = work[pivot_row], work[row]
        pivot = work[row][column]
        work[row] = [value / pivot for value in work[row]]
        for other in range(n_rows):
            if other == row or work[other][column] == 0:
                continue
            factor = work[other][column]
            work[other] = [value - factor * work[row][index] for index, value in enumerate(work[other])]
        rank += 1
        column += 1
    return rank


def cycle_index(index: int) -> int:
    q1 = (index >> 2) & 1
    q2 = (index >> 1) & 1
    q3 = index & 1
    return (q2 << 2) | (q3 << 1) | q1


def site_cycle_unitary() -> Matrix:
    data = [[Fraction(0) for _ in range(8)] for _ in range(8)]
    for source in range(8):
        data[cycle_index(source)][source] = Fraction(1)
    return tuple(tuple(row) for row in data)


def matrix_units_m3() -> tuple[Matrix, Matrix]:
    e12 = tuple(
        tuple(Fraction(1 if (row, column) == (0, 1) else 0) for column in range(3))
        for row in range(3)
    )
    e21 = tuple(
        tuple(Fraction(1 if (row, column) == (1, 0) else 0) for column in range(3))
        for row in range(3)
    )
    return e12, e21


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

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
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current axiom wording is source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; AUDIT_INPUT_PATHS binds the note and the axiom memo"
    )
    print(
        "measure_boundary: the runner checks exact 0/1 permutation algebra over "
        "Fraction; it does not sample or float"
    )
    print(
        "negative_scope: the site-cycle leftover is not a unital M_3 factor and "
        "is not identified with SU(3) or the Bloch triad"
    )

    identity8 = identity(8)
    unitary = site_cycle_unitary()
    adjoint = mat_transpose(unitary)
    square = mat_mul(unitary, unitary)
    cube = mat_mul(square, unitary)
    u_star_u = mat_mul(adjoint, unitary)

    entries = [unitary[row][column] for row in range(8) for column in range(8)]
    row_sums = [sum(unitary[row], Fraction(0)) for row in range(8)]
    column_sums = [sum((unitary[row][column] for row in range(8)), Fraction(0)) for column in range(8)]
    action_ok = all(
        unitary[cycle_index(source)][source] == 1
        and sum((unitary[row][source] for row in range(8)), Fraction(0)) == 1
        for source in range(8)
    )

    generators = (identity8, unitary, square)
    flattened = [
        [matrix[row][column] for row in range(8) for column in range(8)]
        for matrix in generators
    ]
    generated_rank = matrix_rank(flattened)
    gram = [
        [frobenius(left, right) for right in generators]
        for left in generators
    ]
    gram_det = (
        gram[0][0] * (gram[1][1] * gram[2][2] - gram[1][2] * gram[2][1])
        - gram[0][1] * (gram[1][0] * gram[2][2] - gram[1][2] * gram[2][0])
        + gram[0][2] * (gram[1][0] * gram[2][1] - gram[1][1] * gram[2][0])
    )

    e12, e21 = matrix_units_m3()
    e12_e21 = mat_mul(e12, e21)
    e21_e12 = mat_mul(e21, e12)

    pred_u3_ne_i = cube != identity8
    pred_dim_nine = generated_rank == 9
    pred_three_divides_eight = (8 % 3 == 0)

    checks.check(
        "source-qubit",
        "the axiom memo names the one-site algebra M_2(C)",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom,
    )
    checks.check(
        "source-record",
        "Record locks exactly one admissible local possibility",
        "locks exactly one admissible local possibility" in axiom,
    )
    checks.check(
        "source-lattice",
        "Lattice supplies the cubic lattice Z^3",
        "points of the cubic lattice `Z^3`" in axiom,
    )
    checks.check(
        "u-shape",
        "U is an 8x8 matrix",
        len(unitary) == 8 and all(len(row) == 8 for row in unitary),
    )
    checks.check(
        "u-01-entries",
        "every entry of U is the Fraction 0 or 1",
        all(entry in (Fraction(0), Fraction(1)) for entry in entries),
    )
    checks.check(
        "u-permutation",
        "each row and each column of U sums to 1",
        row_sums == [Fraction(1)] * 8 and column_sums == [Fraction(1)] * 8,
    )
    checks.check(
        "u-cycle-action",
        "U sends |q1 q2 q3> to |q2 q3 q1> on the integer basis 4 q1 + 2 q2 + q3",
        action_ok,
    )
    checks.check(
        "u-unitary",
        "U^* = U^{-1} because U^T U = I_8",
        adjoint == mat_transpose(unitary) and u_star_u == identity8,
    )
    checks.check(
        "u-order-three",
        "U^3 = I_8 and U != I_8",
        cube == identity8 and unitary != identity8,
    )
    checks.check(
        "generators-independent",
        "I, U, U^2 are linearly independent of exact rank 3",
        generated_rank == 3
        and square != identity8
        and square != unitary
        and gram == [
            [Fraction(8), Fraction(2), Fraction(2)],
            [Fraction(2), Fraction(8), Fraction(2)],
            [Fraction(2), Fraction(2), Fraction(8)],
        ]
        and gram_det == Fraction(432),
    )
    checks.check(
        "cstar-commutative",
        "span{I,U,U^2} is commutative because U U^2 = U^2 U = I_8",
        mat_mul(unitary, square) == identity8 and mat_mul(square, unitary) == identity8,
    )
    checks.check(
        "not-unital-m3",
        "C*(U) has dimension 3, not 9, while M_3 is non-commutative of dimension 9",
        generated_rank == 3
        and generated_rank != 9
        and e12_e21 != e21_e12
        and sum(1 for row in range(3) for column in range(3)) == 9,
    )
    checks.check(
        "no-unital-hom",
        "there is no unital *-hom M_3(C) -> M_8(C) because 3 does not divide 8",
        8 % 3 != 0,
    )
    checks.check(
        "mutation-u3-ne-I",
        "predicate U^3 != I fails",
        pred_u3_ne_i is False,
    )
    checks.check(
        "mutation-dim-cstar-9",
        "predicate dim C*(U) == 9 fails",
        pred_dim_nine is False,
    )
    checks.check(
        "mutation-3-divides-8",
        "predicate 3 | 8 fails",
        pred_three_divides_eight is False,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the required leftover and bounded-support status fields",
        all(
            phrase in note
            for phrase in (
                'hypothetical_axiom_status: "three-site-cycle leftover: U cycles three M_2 sites; not adopted as QCD"',
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "type-separation-surface",
        "the note keeps U distinct from the Bloch Ad_R orbit and from ad(su(3))",
        all(
            phrase in normalized_note
            for phrase in (
                "one-site Bloch `Ad_R` orbit (lives in `M_2`, not `M_8`)",
                "adjoint of `su(3)` (non-commutative 8-dimensional Lie algebra)",
                "Do not identify them.",
            )
        ),
    )
    checks.check(
        "leftover-surface",
        "Lattice+Qubit supply H and the displayed cycle; Record does not lock U; leftover not adopted",
        all(
            phrase in normalized_note
            for phrase in (
                "Lattice plus Qubit supply three sites",
                "They do not name QCD, SU(3), or a color axiom",
                "Record does not lock `U`.",
                "leftover displayed map and is not adopted",
            )
        ),
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo is not rewritten with the site-cycle or a color axiom",
        all(
            phrase not in axiom
            for phrase in (
                "|q2 q3 q1",
                "site-cycle",
                "unital M_3",
                "color axiom",
            )
        )
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the declared note-and-axiom string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/THREE_SITE_CYCLE_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    print("per_element: all eight product-basis vectors are checked against the cycle index rule")
    print("per_site: three M_2 sites are cycled as a displayed map; no one-site algebra rewrite is claimed")
    print("per_mode: C*(U)=span{I,U,U^2} is the only generated associative algebra tested")
    print("per_block: the unital M_3 factor and the 3|8 homomorphism obstruction are the negative block")
    print("lattice_wide: checked and not executed — three sites are a local tensor, not a lattice-wide color law")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
