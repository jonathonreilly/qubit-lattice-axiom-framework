#!/usr/bin/env python3
"""Exact integer checks for the proper cubic group of 24 matrices.

The runner enumerates 3x3 signed-permutation matrices, counts the det=+1
subset through proper_cubic_count(), and rejects the 1+1 boost prototype
through is_proper_cubic(). Identity gates must call those two functions.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "PROPER_CUBIC_GROUP_IS_24_AND_CONTAINS_NO_BOOST_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"

AUDIT_INPUT_PATHS = (
    "docs/PROPER_CUBIC_GROUP_IS_24_AND_CONTAINS_NO_BOOST_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
)

Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]


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


def _shape_ok(matrix: object) -> bool:
    if not isinstance(matrix, tuple) or len(matrix) != 3:
        return False
    return all(isinstance(row, tuple) and len(row) == 3 for row in matrix)


def _det3(matrix: Matrix) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def _matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def _transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def _is_signed_permutation(matrix: object) -> bool:
    if not _shape_ok(matrix):
        return False
    rows = matrix  # type: ignore[assignment]
    for row in rows:
        if any(entry not in (-1, 0, 1) for entry in row):
            return False
        if sum(entry != 0 for entry in row) != 1:
            return False
    for column in range(3):
        if sum(rows[row][column] != 0 for row in range(3)) != 1:
            return False
    return True


def is_proper_cubic(matrix: object) -> bool:
    """True iff matrix is a 3x3 monomial signed-permutation matrix with det=+1."""
    if not _is_signed_permutation(matrix):
        return False
    return _det3(matrix) == 1  # type: ignore[arg-type]


def signed_permutation_matrices() -> tuple[Matrix, ...]:
    matrices: list[Matrix] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for column, row in enumerate(perm):
                rows[row][column] = signs[column]
            matrices.append(tuple(tuple(entry) for entry in rows))  # type: ignore[arg-type]
    return tuple(matrices)


def proper_cubic_matrices() -> tuple[Matrix, ...]:
    return tuple(matrix for matrix in signed_permutation_matrices() if is_proper_cubic(matrix))


def proper_cubic_count() -> int:
    return sum(1 for matrix in signed_permutation_matrices() if is_proper_cubic(matrix))


def identity_count_gate() -> bool:
    """Identity gate: order is read from proper_cubic_count()."""
    return proper_cubic_count() == 24


def identity_membership_gate(matrix: object) -> bool:
    """Identity gate: membership is read from is_proper_cubic(M)."""
    return is_proper_cubic(matrix)


IDENTITY: Matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
BOOST_L = ((2, 1), (1, 2))
EMBEDDED_BOOST: Matrix = ((2, 1, 0), (1, 2, 0), (0, 0, 1))
ROT90_Z: Matrix = ((0, -1, 0), (1, 0, 0), (0, 0, 1))


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    normalized_parent = normalize(parent)

    print(
        "external_scientific_inputs: current axiom wording and the kinetic-isotropy "
        "primitive are source-bound; no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency"
    )
    print(
        "measure_boundary: the runner checks exact integer 3x3 algebra; it does "
        "not install a Wick parameter or a (3,1) form"
    )
    print(
        "negative_scope: only |G|!=24 and membership of diag(L,1) are rejected; "
        "Lorentz closure remains live"
    )

    lattice_quote = "standard translations, and proper cubic rotations about each site."
    checks.check(
        "source-lattice",
        "the axiom memo names translations and proper cubic rotations",
        lattice_quote in normalized_axiom,
    )
    checks.check(
        "source-kinetic-tick",
        "kinetic isotropy supplies the Euclidean equality c_t = c_s",
        "c_t = c_s" in parent,
    )
    checks.check(
        "source-kinetic-not-lorentz",
        "kinetic isotropy leaves full Lorentz restoration as a separate claim",
        "full Lorentz restoration remain separate" in normalized_parent,
    )
    checks.check(
        "source-note-quotes",
        "the note quotes Lattice and states one Euclidean tick, not a Lorentz theorem",
        lattice_quote in normalized_note
        and "one Euclidean tick" in normalized_note
        and "c_t = c_s" in note
        and "not a Lorentz theorem" in normalized_note,
    )

    signed = signed_permutation_matrices()
    unique_signed = set(signed)
    checks.check(
        "signed-permutation-census",
        "there are exactly 3! x 2^3 = 48 signed-permutation matrices",
        len(signed) == 48 and len(unique_signed) == 48,
    )

    group = proper_cubic_matrices()
    count = proper_cubic_count()
    checks.check(
        "identity-count-gate",
        "identity gate calls proper_cubic_count() and obtains 24",
        identity_count_gate() and count == 24 and len(group) == 24,
    )
    checks.check(
        "proper-det",
        "every counted matrix has det=+1 and passes is_proper_cubic",
        all(_det3(matrix) == 1 and is_proper_cubic(matrix) for matrix in group),
    )
    half = sum(1 for matrix in signed if _det3(matrix) == 1)
    checks.check(
        "half-split",
        "exactly half of the 48 signed-permutation matrices have det=+1",
        half == 24 and 2 * half == len(signed),
    )

    euclidean_ok = all(_matmul(_transpose(matrix), matrix) == IDENTITY for matrix in group)
    checks.check(
        "euclidean-form",
        "every R in G satisfies R^T R = I_3",
        euclidean_ok,
    )

    sample = (1, 0, 0)
    preserved = True
    for matrix in group:
        image = tuple(sum(matrix[i][j] * sample[j] for j in range(3)) for i in range(3))
        if sum(value * value for value in image) != 1:
            preserved = False
            break
    checks.check(
        "euclidean-quadratic",
        "x |-> R x preserves x1^2+x2^2+x3^2 on the first basis vector",
        preserved,
    )
    checks.check(
        "not-minkowski-3",
        "the note distinguishes diag(1,1,1) from diag(1,1,-1)",
        "diag(1,1,1)" in note and "diag(1,1,-1)" in note,
    )

    checks.check(
        "identity-membership-gate",
        "identity gate calls is_proper_cubic on I_3 and a proper rotation",
        identity_membership_gate(IDENTITY)
        and identity_membership_gate(ROT90_Z)
        and is_proper_cubic(IDENTITY)
        and is_proper_cubic(ROT90_Z),
    )

    boost_plane = BOOST_L[0][0] ** 2 + BOOST_L[1][0] ** 2
    checks.check(
        "boost-prototype-not-cubic",
        "L is 2x2, has entry 2, and does not preserve x^2+y^2",
        len(BOOST_L) == 2
        and len(BOOST_L[0]) == 2
        and BOOST_L[0][0] == 2
        and 2 not in (-1, 1)
        and boost_plane == 5
        and not is_proper_cubic(BOOST_L),
    )
    first_row_nonzeros = sum(entry != 0 for entry in EMBEDDED_BOOST[0])
    embedded_is_cubic = is_proper_cubic(EMBEDDED_BOOST)
    checks.check(
        "embedded-boost-not-cubic",
        "diag(L,1) has two nonzeros in the first row and fails is_proper_cubic",
        EMBEDDED_BOOST[0][1] == 1
        and first_row_nonzeros == 2
        and identity_membership_gate(EMBEDDED_BOOST) is False
        and embedded_is_cubic is False,
    )

    order_neq_24 = proper_cubic_count() != 24
    checks.check(
        "mutation-order",
        "predicate |G|!=24 fails",
        order_neq_24 is False,
    )
    checks.check(
        "mutation-embedded-boost",
        "predicate diag(L,1) is a proper cubic matrix fails",
        embedded_is_cubic is False,
    )

    checks.check(
        "extra-object-displayed",
        "a fourth direction and a (3,1) form are displayed and not adopted",
        "fourth direction" in normalized_note
        and "(3,1) form" in normalized_note
        and "not adopted" in normalized_note,
    )
    checks.check(
        "boundary-phrases",
        "the note does not claim Lorentz impossibility, a=1, G=SO(3), or axiom adoption",
        "we adopt" not in normalized_note.lower()
        and "new axiom" not in normalized_note
        and "Codex" not in note
        and "does not install `a = 1`" in normalized_note
        and "does not say that the cubic 24 is `SO(3)`" in normalized_note
        and "does not claim that Lorentz closure is impossible" in normalized_note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo is not edited by this block",
        lattice_quote in axiom and "diag(L, 1)" not in axiom,
    )

    print("per_element: all 48 signed-permutation matrices and the 24 det=+1 subset are counted exactly")
    print("per_site: named symmetry is the Lattice site rotation; no composite carrier is asserted")
    print("per_mode: Euclidean q_E is checked; the (3,1) form is displayed only")
    print("per_block: the boost prototype and its 3D embedding are the only rejected block")
    print("lattice_wide: checked and not executed — no lattice-wide dynamics or Lorentz no-go is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
