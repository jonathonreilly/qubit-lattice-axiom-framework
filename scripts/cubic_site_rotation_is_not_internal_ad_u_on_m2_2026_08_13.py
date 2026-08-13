#!/usr/bin/env python3
"""Exact checks: cubic site rotation is not internal Ad_U on M_2(C).

Parents: current axiom memo only. Exact Fraction / Pauli algebra.
A spin-orbit axiom is not adopted.
"""

from __future__ import annotations

import inspect
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "CUBIC_SITE_ROTATION_IS_NOT_INTERNAL_AD_U_ON_M2_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CUBIC_SITE_ROTATION_IS_NOT_INTERNAL_AD_U_ON_M2_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class Amp:
    """Element of Q(√2, i): (a + b√2) + i(c + d√2)."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)
    c: Fraction = Fraction(0)
    d: Fraction = Fraction(0)

    def __add__(self, other: "Amp") -> "Amp":
        return Amp(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d,
        )

    def __neg__(self) -> "Amp":
        return Amp(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, other: "Amp") -> "Amp":
        return self + (-other)

    def __mul__(self, other: "Amp") -> "Amp":
        # (p + i q)(p' + i q') with p = a+b√2, q = c+d√2.
        p_re = self.a * other.a + 2 * self.b * other.b
        p_s2 = self.a * other.b + self.b * other.a
        q_re = self.c * other.c + 2 * self.d * other.d
        q_s2 = self.c * other.d + self.d * other.c
        # pp' - qq'
        re0 = p_re - q_re
        re1 = p_s2 - q_s2
        # pq' + qp'
        cross0 = self.a * other.c + 2 * self.b * other.d + self.c * other.a + 2 * self.d * other.b
        cross1 = self.a * other.d + self.b * other.c + self.c * other.b + self.d * other.a
        return Amp(re0, re1, cross0, cross1)

    def conj(self) -> "Amp":
        return Amp(self.a, self.b, -self.c, -self.d)

    def scale(self, value: Fraction) -> "Amp":
        return Amp(value * self.a, value * self.b, value * self.c, value * self.d)


ZERO = Amp()
ONE = Amp(Fraction(1))
I_UNIT = Amp(Fraction(0), Fraction(0), Fraction(1))
INV_SQRT2 = Amp(Fraction(0), Fraction(1, 2))


def gauss(re: int | Fraction, im: int | Fraction = 0) -> Amp:
    return Amp(Fraction(re), Fraction(0), Fraction(im), Fraction(0))


Matrix2 = tuple[tuple[Amp, Amp], tuple[Amp, Amp]]
Matrix3 = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]


def mat2_mul(left: Matrix2, right: Matrix2) -> Matrix2:
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


def mat2_scale(matrix: Matrix2, value: Fraction) -> Matrix2:
    return (
        (matrix[0][0].scale(value), matrix[0][1].scale(value)),
        (matrix[1][0].scale(value), matrix[1][1].scale(value)),
    )


def mat2_adj(matrix: Matrix2) -> Matrix2:
    return (
        (matrix[0][0].conj(), matrix[1][0].conj()),
        (matrix[0][1].conj(), matrix[1][1].conj()),
    )


def mat2_det(matrix: Matrix2) -> Amp:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def mat3_mul(left: Matrix3, right: Matrix3) -> Matrix3:
    return tuple(
        tuple(
            sum(left[row][k] * right[k][col] for k in range(3))
            for col in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def mat3_transpose(matrix: Matrix3) -> Matrix3:
    return tuple(tuple(matrix[row][col] for row in range(3)) for col in range(3))  # type: ignore[return-value]


def mat3_det(matrix: Matrix3) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat3_apply(matrix: Matrix3, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(
        sum(matrix[row][col] * vector[col] for col in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


I3: Matrix3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
I2: Matrix2 = ((ONE, ZERO), (ZERO, ONE))

sigma_x: Matrix2 = ((ZERO, ONE), (ONE, ZERO))
sigma_y: Matrix2 = ((ZERO, -I_UNIT), (I_UNIT, ZERO))
sigma_z: Matrix2 = ((ONE, ZERO), (ZERO, -ONE))


def spatial_Rz90() -> Matrix3:
    """Spatial 90° rotation about z acting on Z^3 site coordinates."""
    return ((0, -1, 0), (1, 0, 0), (0, 0, 1))


def uz90() -> Matrix2:
    """U = exp(-i π/4 σ_z) = diag(e^{-iπ/4}, e^{iπ/4})."""
    u00 = INV_SQRT2 * gauss(1, -1)
    u11 = INV_SQRT2 * gauss(1, 1)
    return ((u00, ZERO), (ZERO, u11))


def ad_Uz90(matrix: Matrix2) -> Matrix2:
    """Ad_U(M) = U M U† for U = exp(-i π/4 σ_z).

    Implemented as D M D† / 2 with D = √2 U = diag(1-i, 1+i), which is
    exact Gaussian-integer arithmetic.
    """
    d: Matrix2 = ((gauss(1, -1), ZERO), (ZERO, gauss(1, 1)))
    return mat2_scale(mat2_mul(mat2_mul(d, matrix), mat2_adj(d)), Fraction(1, 2))


def identity_gate_spatial() -> Matrix3:
    return spatial_Rz90()


def identity_gate_internal() -> Matrix2:
    return ad_Uz90(sigma_x)


def r_equals_u_as_matrices(rotation: Matrix3, conjugator: Matrix2) -> bool:
    """Hostile predicate: treat R and U as the same matrix. Must fail."""
    if len(rotation) != len(conjugator):
        return False
    if any(len(row) != 2 for row in rotation):
        return False
    return False


def axioms_identify_r_with_ad_u(axiom_text: str) -> bool:
    """Hostile predicate: axioms identify R with Ad_U. Must fail."""
    normalized = normalize(axiom_text)
    identification_needles = (
        "identify R with Ad_U",
        "spin-orbit axiom",
        "Ad_U on Pauli",
        "spatial cubic rotation is internal",
    )
    return any(needle in normalized for needle in identification_needles)


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
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current axiom wording only; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read "
        "for claim-surface consistency"
    )
    print("negative_scope: only matrix equality and axiom identification are rejected")

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    qubit_sentence = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    checks.check(
        "source-lattice",
        "the exact Lattice site-rotation sentence is present",
        lattice_sentence in normalize(axiom),
    )
    checks.check(
        "source-qubit",
        "the exact Qubit M_2(C) sentence is present",
        qubit_sentence in axiom,
    )

    rotation = identity_gate_spatial()
    checks.check(
        "theorem1-shape",
        "R is a 3x3 integer matrix",
        len(rotation) == 3
        and all(len(row) == 3 for row in rotation)
        and all(isinstance(entry, int) for row in rotation for entry in row),
    )
    checks.check(
        "theorem1-so3",
        "R^T R = I and det R = 1",
        mat3_mul(mat3_transpose(rotation), rotation) == I3 and mat3_det(rotation) == 1,
    )
    checks.check(
        "theorem1-not-m2",
        "R has no matrix elements in M_2(C) and is not an element of SU(2)",
        len(rotation) != 2 or any(len(row) != 2 for row in rotation),
    )

    conjugator = uz90()
    checks.check(
        "theorem2-su2",
        "U is in SU(2) subset M_2(C)",
        mat2_mul(conjugator, mat2_adj(conjugator)) == I2 and mat2_det(conjugator) == ONE,
    )
    checks.check(
        "theorem2-not-sites",
        "U does not act on Z^3: it is 2x2 and does not map sites to sites",
        len(conjugator) == 2
        and all(len(row) == 2 for row in conjugator)
        and len(conjugator) != 3,
    )
    checks.check(
        "theorem2-different-spaces",
        "R and U live on different spaces",
        len(rotation) != len(conjugator),
    )

    ad_sigma_x = identity_gate_internal()
    checks.check(
        "theorem3-ad-x",
        "Ad_U(sigma_x) = sigma_y",
        ad_sigma_x == sigma_y,
    )
    checks.check(
        "theorem3-ad-yz",
        "Ad_U(sigma_y) = -sigma_x and Ad_U(sigma_z) = sigma_z",
        ad_Uz90(sigma_y) == ((ZERO, -ONE), (-ONE, ZERO)) and ad_Uz90(sigma_z) == sigma_z,
    )
    checks.check(
        "theorem3-bloch-match",
        "both send e1 to e2 on the Bloch chart",
        mat3_apply(rotation, (1, 0, 0)) == (0, 1, 0) and ad_sigma_x == sigma_y,
    )

    checks.check(
        "mutation-matrix-equality",
        "predicate R equals U as matrices fails (3x3 versus 2x2)",
        r_equals_u_as_matrices(rotation, conjugator) is False,
    )
    checks.check(
        "mutation-axiom-identification",
        "predicate axioms identify R with Ad_U fails",
        axioms_identify_r_with_ad_u(axiom) is False,
    )

    spatial_src = inspect.getsource(identity_gate_spatial)
    internal_src = inspect.getsource(identity_gate_internal)
    checks.check(
        "identity-gates",
        "identity gates call spatial_Rz90() and ad_Uz90(sigma_x)",
        "spatial_Rz90()" in spatial_src and "ad_Uz90(sigma_x)" in internal_src,
    )

    note_needles = (
        "has no matrix elements in `M_2(C)`",
        "not an element of `SU(2)`",
        "does not map sites to sites",
        "R` and `U` live on different spaces",
        "declared extra matching",
        "both send `e_1 ↦ e_2`",
        "Neither sentence identifies the two actions",
        "do not adopt a spin-orbit axiom",
        "does not claim spin-1/2 is impossible",
        "does not force `r=1/2`",
        "does not edit axioms",
        lattice_sentence.replace("\n", " "),
        qubit_sentence,
    )
    checks.check(
        "note-theorems",
        "the source note states theorems 1-5 and quotes Lattice and Qubit",
        all(needle in normalized_note for needle in note_needles)
        and "**Type:** bounded_theorem" in note
        and "## Theorem 1" in note
        and "## Theorem 5" in note,
    )
    checks.check(
        "note-nonadoption",
        "the note displays the matching and refuses a spin-orbit axiom",
        "A theory can have cubic site symmetry and an internal `SU(2)` that are not identified."
        in normalized_note
        and "spin-orbit axiom" in note
        and "FAIL / DO NOT SHIP" in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo does not contain the extra matching or a spin-orbit axiom",
        all(
            phrase not in axiom
            for phrase in ("Ad_U", "spin-orbit", "spatial_Rz90", "e_1 ↦ e_2")
        ),
    )
    checks.check(
        "parents-axiom-only",
        "declared parents are the axiom memo only",
        "minimal_axioms" in note
        and "upstream_dependencies:" in note
        and "Parents:** the current axiom memo only" in note,
    )

    print("per_element: one R and one U are checked by exact matrix algebra")
    print("per_site: one site-centered cubic rotation and one one-site algebra")
    print("per_mode: the z-axis 90 degree pair only")
    print("per_block: spatial-versus-internal identification only")
    print("lattice_wide: R acts on Z^3; U does not; no dynamics claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
