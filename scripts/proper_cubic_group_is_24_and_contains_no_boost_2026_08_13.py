#!/usr/bin/env python3
"""Exact cubic-point-group and canonical boost-separation checks."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
from typing import TypeAlias


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "PROPER_CUBIC_GROUP_IS_24_AND_CONTAINS_NO_BOOST_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/PROPER_CUBIC_GROUP_IS_24_AND_CONTAINS_NO_BOOST_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Scalar: TypeAlias = int | Fraction
Matrix: TypeAlias = tuple[tuple[Scalar, ...], ...]
Vector3: TypeAlias = tuple[int, int, int]
Matrix3: TypeAlias = tuple[
    tuple[int, int, int],
    tuple[int, int, int],
    tuple[int, int, int],
]


def normalize(text: str) -> str:
    return " ".join(text.split())


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


def _transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][column] for row in range(len(matrix))) for column in range(len(matrix[0])))


def _matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                (left[row][inner] * right[inner][column] for inner in range(len(right))),
                start=0,
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def _matvec(matrix: Matrix3, vector: Vector3) -> Vector3:
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def _diagonal(*entries: Scalar) -> Matrix:
    return tuple(
        tuple(entry if row == column else 0 for column in range(len(entries)))
        for row, entry in enumerate(entries)
    )


def _permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[left] > perm[right]
        for left in range(len(perm))
        for right in range(left + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def _determinant(matrix: Matrix) -> Scalar:
    size = len(matrix)
    return sum(
        (
            _permutation_sign(perm)
            * product_entry(matrix[row][perm[row]] for row in range(size))
            for perm in permutations(range(size))
        ),
        start=0,
    )


def product_entry(entries: object) -> Scalar:
    value: Scalar = 1
    for entry in entries:  # type: ignore[union-attr]
        value *= entry  # type: ignore[operator]
    return value


def _shape3(matrix: object) -> bool:
    return (
        isinstance(matrix, tuple)
        and len(matrix) == 3
        and all(isinstance(row, tuple) and len(row) == 3 for row in matrix)
    )


def is_signed_permutation(matrix: object) -> bool:
    if not _shape3(matrix):
        return False
    rows = matrix  # type: ignore[assignment]
    for row in rows:
        if any(entry not in (-1, 0, 1) for entry in row):
            return False
        if sum(entry != 0 for entry in row) != 1:
            return False
    return all(
        sum(rows[row][column] != 0 for row in range(3)) == 1
        for column in range(3)
    )


def is_proper_cubic(matrix: object) -> bool:
    return is_signed_permutation(matrix) and _determinant(matrix) == 1  # type: ignore[arg-type]


def signed_permutation_matrices() -> tuple[Matrix3, ...]:
    matrices: list[Matrix3] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for column, row in enumerate(perm):
                rows[row][column] = signs[column]
            matrices.append(tuple(tuple(row) for row in rows))  # type: ignore[arg-type]
    return tuple(matrices)


def proper_cubic_matrices() -> tuple[Matrix3, ...]:
    return tuple(
        matrix for matrix in signed_permutation_matrices() if is_proper_cubic(matrix)
    )


def proper_cubic_count() -> int:
    return len(proper_cubic_matrices())


E1: Vector3 = (1, 0, 0)
E2: Vector3 = (0, 1, 0)
E3: Vector3 = (0, 0, 1)
NEIGHBORS = {E1, E2, E3, tuple(-x for x in E1), tuple(-x for x in E2), tuple(-x for x in E3)}

IDENTITY3: Matrix3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
D3 = _diagonal(1, 1, -1)
RY: Matrix3 = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))

ETA2 = _diagonal(Fraction(1), Fraction(-1))
BOOST2: Matrix = (
    (Fraction(5, 3), Fraction(4, 3)),
    (Fraction(4, 3), Fraction(5, 3)),
)

ETA4 = _diagonal(Fraction(1), Fraction(-1), Fraction(-1), Fraction(-1))
BOOST4: Matrix = (
    (Fraction(5, 3), Fraction(4, 3), Fraction(0), Fraction(0)),
    (Fraction(4, 3), Fraction(5, 3), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
)


def maps_neighbor_set(matrix: Matrix3) -> bool:
    return {_matvec(matrix, vector) for vector in NEIGHBORS} == NEIGHBORS


def preserves_form(matrix: Matrix, form: Matrix) -> bool:
    return _matmul(_matmul(_transpose(matrix), form), matrix) == form


def embed_spatial_rotation(matrix: Matrix3) -> Matrix:
    return (
        (1, 0, 0, 0),
        (0, *matrix[0]),
        (0, *matrix[1]),
        (0, *matrix[2]),
    )


def has_time_space_mixing(matrix: Matrix) -> bool:
    return any(matrix[0][index] != 0 or matrix[index][0] != 0 for index in range(1, 4))


def is_nontrivial_boost(matrix: Matrix) -> bool:
    return (
        len(matrix) == 4
        and all(len(row) == 4 for row in matrix)
        and preserves_form(matrix, ETA4)
        and _determinant(matrix) == 1
        and matrix[0][0] > 0
        and has_time_space_mixing(matrix)
    )


N5_LINES = (
    "per_element: all 24 proper-cubic matrices and their canonical spacetime embeddings are checked exactly",
    "per_site: the point action is proved at one arbitrary fixed lattice site and transported by the supplied translations",
    "per_mode: every canonical embedding fixes the displayed time axis, while no momentum or dynamical mode is asserted",
    "per_block: one exact rational boost block is Lorentzian and lies outside the zero-mixing embedded point group",
    "lattice_wide: checked and not executed — no lattice-wide dynamics, continuum limit, or Lorentz restoration is claimed",
)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: only the current minimal-axiom Lattice "
        "sentence is source-bound; no fitted, observational, or literature values are used"
    )
    print(
        "package_local_integrity_reads: the proposed note is read only for claim, "
        "trace, and no-go-discipline consistency"
    )
    print(
        "measure_boundary: exact integer and rational finite-dimensional linear algebra only"
    )
    print(
        "negative_scope: only canonical diag(1,R) embeddings are excluded from "
        "the declared nontrivial time-space-mixing boost class"
    )

    lattice_quote = "standard translations, and proper cubic rotations about each site."
    checks.check(
        "source-lattice",
        "current minimal axioms supply the cubic fixed-site symmetry sentence",
        lattice_quote in normalized_axiom,
    )
    checks.check(
        "source-scope",
        "the note fixes a site, displacement action, and affine action about that site",
        "Fix a site `a in Z^3`" in note
        and "x |-> a + R(x-a)" in note
        and "fixed-site point stabilizer" in normalized_note,
    )

    signed = signed_permutation_matrices()
    signed_set = set(signed)
    group = proper_cubic_matrices()
    group_set = set(group)
    checks.check(
        "signed-census",
        "the signed-permutation enumeration has 48 unique matrices",
        len(signed) == 48 and len(signed_set) == 48,
    )
    checks.check(
        "neighbor-characterization",
        "every enumerated signed permutation preserves the six-neighbor set",
        all(maps_neighbor_set(matrix) for matrix in signed),
    )
    checks.check(
        "proper-count",
        "the determinant-plus-one point group has order 24",
        proper_cubic_count() == 24 and len(group_set) == 24,
    )
    checks.check(
        "group-identity",
        "the identity is in the proper point group",
        IDENTITY3 in group_set,
    )
    checks.check(
        "group-closure",
        "all 24 squared products remain in the group",
        all(_matmul(left, right) in group_set for left in group for right in group),
    )
    checks.check(
        "group-inverses",
        "every transpose is an in-group two-sided inverse",
        all(
            _transpose(matrix) in group_set
            and _matmul(matrix, _transpose(matrix)) == IDENTITY3
            and _matmul(_transpose(matrix), matrix) == IDENTITY3
            for matrix in group
        ),
    )

    checks.check(
        "euclidean-form",
        "every proper cubic matrix satisfies R^T R=I_3",
        all(preserves_form(matrix, IDENTITY3) for matrix in group),
    )
    d3_preservers = tuple(matrix for matrix in group if preserves_form(matrix, D3))
    checks.check(
        "indefinite-intersection",
        "exactly 8 elements preserve diag(1,1,-1) and 16 do not",
        len(d3_preservers) == 8 and len(group) - len(d3_preservers) == 16,
    )
    checks.check(
        "indefinite-witnesses",
        "identity preserves D while the displayed proper y-rotation does not",
        IDENTITY3 in d3_preservers
        and RY in group_set
        and not preserves_form(RY, D3),
    )

    embeddings = tuple(embed_spatial_rotation(matrix) for matrix in group)
    checks.check(
        "embedded-lorentz",
        "all canonical embeddings preserve eta and have determinant one",
        all(preserves_form(matrix, ETA4) and _determinant(matrix) == 1 for matrix in embeddings),
    )
    checks.check(
        "embedded-time-axis",
        "all canonical embeddings fix time and have zero time-space mixing",
        all(matrix[0][0] == 1 and not has_time_space_mixing(matrix) for matrix in embeddings),
    )
    checks.check(
        "universal-no-boost",
        "none of the 24 canonical embeddings is a nontrivial declared boost",
        not any(is_nontrivial_boost(matrix) for matrix in embeddings),
    )

    checks.check(
        "boost2-lorentz",
        "the exact rational 1+1 block preserves diag(1,-1)",
        preserves_form(BOOST2, ETA2),
    )
    checks.check(
        "boost2-proper-time-oriented",
        "the exact rational block has determinant one and positive time component",
        _determinant(BOOST2) == 1 and BOOST2[0][0] == Fraction(5, 3),
    )
    checks.check(
        "boost4-classification",
        "the 3+1 extension is a nontrivial boost under the declared predicate",
        is_nontrivial_boost(BOOST4),
    )
    checks.check(
        "boost-outside-point-group",
        "the exact boost lies outside all zero-mixing canonical embeddings",
        BOOST4 not in set(embeddings),
    )

    required_no_go_sections = tuple(f"### N{index} " for index in range(1, 9))
    checks.check(
        "no-go-packet",
        "the landed note contains the complete N1-N8 discipline record",
        "## No-Go Discipline Gate" in note
        and all(section in note for section in required_no_go_sections)
        and note.count("| ATTEMPTED |") >= 5,
    )
    checks.check(
        "n5-certificate-source",
        "the note carries the exact five forensic resolution lines",
        all(line in note for line in N5_LINES),
    )
    checks.check(
        "trace-contract",
        "the machine trace uses frontier discovery, null target, and a next action",
        "trace_class: frontier_discovery" in note
        and "target_claim_id: null" in note
        and "next_trace_action:" in note,
    )
    checks.check(
        "claim-boundary",
        "the note excludes an embedding-free or dynamical Lorentz no-go",
        "A noncanonical or embedding-free theorem remains open." in normalized_note
        and "It does not claim that Lorentz symmetry cannot emerge" in normalized_note
        and "No spacetime metric or time direction is added" in normalized_note,
    )
    checks.check(
        "claim-type",
        "the source uses the bounded-theorem claim type without authoring an audit verdict",
        "claim_type: bounded_theorem" in note
        and "**Type:** bounded_theorem" in note
        and "independent audit lane only" in normalized_note,
    )

    for line in N5_LINES:
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
