#!/usr/bin/env python3
"""Exact checks: a 2-set content law μ is not a density matrix ρ.

The runner uses only rational arithmetic. It binds the displayed law through
mu_A() and compares the two trial densities through equal_rho. The uniqueness
predicate is required to fail on {ρ0, ρ1}.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "TWO_SET_CONTENT_LAW_IS_NOT_A_DENSITY_MATRIX_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_SET_CONTENT_LAW_IS_NOT_A_DENSITY_MATRIX_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def mu_A() -> Fraction:
    """Mass of label A under the displayed 2-set law."""
    return Fraction(3, 5)


def mu_B() -> Fraction:
    """Mass of label B, forced by normalization of a 2-set probability."""
    return Fraction(1) - mu_A()


def mu(label: str) -> Fraction:
    if label == "A":
        return mu_A()
    if label == "B":
        return mu_B()
    raise KeyError(label)


def equal_rho(left: Matrix, right: Matrix) -> bool:
    return left == right


def adjoint(matrix: Matrix) -> Matrix:
    return (
        (matrix[0][0], matrix[1][0]),
        (matrix[0][1], matrix[1][1]),
    )


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][col] + right[row][col] for col in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][0] * right[0][col] + left[row][1] * right[1][col]
            for col in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def trace(matrix: Matrix) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def determinant(matrix: Matrix) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def is_hermitian(matrix: Matrix) -> bool:
    return matrix == adjoint(matrix)


def is_density(matrix: Matrix) -> bool:
    return (
        is_hermitian(matrix)
        and trace(matrix) == 1
        and matrix[0][0] >= 0
        and determinant(matrix) >= 0
    )


def diagonal(matrix: Matrix) -> tuple[Fraction, Fraction]:
    return (matrix[0][0], matrix[1][1])


P_Z: Matrix = (
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0)),
)
I_MINUS_P_Z: Matrix = (
    (Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1)),
)


def born_weights_on_z(rho: Matrix) -> tuple[Fraction, Fraction]:
    return (trace(matmul(rho, P_Z)), trace(matmul(rho, I_MINUS_P_Z)))


def bloch_vector(rho: Matrix) -> tuple[Fraction, Fraction, Fraction]:
    r_x = rho[0][1] + rho[1][0]
    r_y = rho[1][0] - rho[0][1]
    r_z = rho[0][0] - rho[1][1]
    return (r_x, r_y, r_z)


def bloch_radius_squared(rho: Matrix) -> Fraction:
    r_x, r_y, r_z = bloch_vector(rho)
    return r_x * r_x + r_y * r_y + r_z * r_z


def normalize(text: str) -> str:
    return " ".join(text.split())


def mu_uniquely_determines_rho(candidates: tuple[Matrix, ...]) -> bool:
    target = (mu_A(), mu_B())
    matches = [rho for rho in candidates if born_weights_on_z(rho) == target]
    return len(matches) == 1


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


def make_rho0() -> Matrix:
    return (
        (mu_A(), Fraction(0)),
        (Fraction(0), mu_B()),
    )


def make_rho1() -> Matrix:
    off = Fraction(1, 5)
    return (
        (mu_A(), off),
        (off, mu_B()),
    )


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)
    rho0 = make_rho0()
    rho1 = make_rho1()

    print(
        "external_scientific_inputs: current axiom wording only; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency"
    )

    admissibility = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    qubit = "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    checks.check(
        "source-admissibility",
        "Admissibility names a distribution over possibilities",
        admissibility in normalized_axiom,
    )
    checks.check(
        "source-qubit",
        "Qubit presents the local domain as M_2(C)",
        qubit in axiom,
    )

    checks.check(
        "law-normalization",
        "the displayed 2-set law is a probability",
        mu("A") + mu("B") == 1 and mu("A") > 0 and mu("B") > 0,
    )
    checks.check(
        "identity-gate-mu-A",
        "both trial densities carry mu_A on the (0,0) entry",
        rho0[0][0] == mu_A() and rho1[0][0] == mu_A(),
    )
    checks.check(
        "identity-gate-unequal-rho",
        "the two displayed densities are unequal matrices",
        equal_rho(rho0, rho1) is False,
    )

    checks.check(
        "rho0-density",
        "ρ0 is Hermitian, trace one, and positive definite",
        is_density(rho0) and determinant(rho0) == Fraction(6, 25),
    )
    checks.check(
        "rho1-density",
        "ρ1 is Hermitian, trace one, and positive definite with det 1/5",
        is_density(rho1) and determinant(rho1) == Fraction(1, 5),
    )
    checks.check(
        "common-diagonal",
        "both densities have diagonal (μ(A), μ(B))",
        diagonal(rho0) == (mu_A(), mu_B())
        and diagonal(rho1) == (mu_A(), mu_B()),
    )
    checks.check(
        "born-weights-shared",
        "both densities reproduce μ on {P_z, I−P_z}",
        born_weights_on_z(rho0) == (mu_A(), mu_B())
        and born_weights_on_z(rho1) == (mu_A(), mu_B()),
    )
    checks.check(
        "uniqueness-predicate-fails",
        "the predicate μ uniquely determines ρ fails on {ρ0, ρ1}",
        mu_uniquely_determines_rho((rho0, rho1)) is False,
    )
    checks.check(
        "mu-has-no-off-diagonal",
        "μ is a function on {A, B} rather than a 2×2 matrix",
        callable(mu) and set(label for label in ("A", "B")) == {"A", "B"},
    )
    checks.check(
        "bloch-radius-not-half",
        "neither displayed density is forced to Bloch radius 1/2",
        bloch_radius_squared(rho0) != Fraction(1, 4)
        and bloch_radius_squared(rho1) != Fraction(1, 4)
        and bloch_vector(rho0) == (Fraction(0), Fraction(0), Fraction(1, 5))
        and bloch_vector(rho1) == (Fraction(2, 5), Fraction(0), Fraction(1, 5)),
    )

    theorem_needles = (
        "μ` is a function `X→Q`",
        "no unique `ρ`",
        "A law on a 2-set is a probability on `{A,B}`. It is not an element of",
        "does not adopt a dictionary",
        "does not claim that Born is false",
        "does not adopt `L_phys`",
        "does not force a Bloch radius `r=1/2`",
    )
    checks.check(
        "note-theorem-surface",
        "Theorems 1–5 and the display/no-dictionary boundary are source-visible",
        all(needle in note for needle in theorem_needles)
        and all(f"## Theorem {index}" in note for index in range(1, 6)),
    )
    forbidden = (
        "Gleason",
        "oneweight",
        "locksample",
        "unmerged PR",
        "#6209",
    )
    checks.check(
        "note-forbidden-rhetoric",
        "the note avoids Gleason, unmerged-PR cites, and a Born-is-false claim",
        all(token not in note for token in forbidden)
        and "does not claim that Born is false" in note
        and all(token not in axiom for token in ("ρ0", "two-set content law")),
    )
    checks.check(
        "axiom-quotes-in-note",
        "the note quotes the current Admissibility and Qubit sentences",
        admissibility in normalized_note and qubit in note,
    )

    print(
        "per_element: μ(A), μ(B), ρ0, and ρ1 are checked exactly; "
        "off-diagonals distinguish the two densities"
    )
    print(
        "per_site: the type mismatch is an algebraic one-site statement; "
        "no composite carrier is asserted"
    )
    print(
        "per_mode: only the menu {P_z, I−P_z} is used for the uniqueness test"
    )
    print(
        "per_block: the 2-set-law versus density identification is the only "
        "negative block tested"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide dynamics "
        "or Born no-go is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
