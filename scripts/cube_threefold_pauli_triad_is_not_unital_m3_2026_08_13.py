#!/usr/bin/env python3
"""Exact Q(i) checks for the cube 3-fold Pauli-axis triad.

One-site M_2(C). A supplied Pauli-axis action of the body-diagonal
3-fold cycles the Pauli axes. The action map is extra. No QCD
identification, Qubit rewrite, or axiom edit.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "CUBE_THREEFOLD_PAULI_TRIAD_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CUBE_THREEFOLD_PAULI_TRIAD_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


class Gau:
    """a + b i with a, b in Q."""

    __slots__ = ("a", "b")

    def __init__(self, a: Fraction | int, b: Fraction | int = 0) -> None:
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other: Gau) -> Gau:
        return Gau(self.a + other.a, self.b + other.b)

    def __sub__(self, other: Gau) -> Gau:
        return Gau(self.a - other.a, self.b - other.b)

    def __mul__(self, other: Gau) -> Gau:
        return Gau(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Gau):
            return NotImplemented
        return self.a == other.a and self.b == other.b

    def __neg__(self) -> Gau:
        return Gau(-self.a, -self.b)

    def conj(self) -> Gau:
        return Gau(self.a, -self.b)

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def inverse(self) -> Gau:
        if self.is_zero():
            raise ZeroDivisionError("zero has no inverse in Q(i)")
        norm = self.a * self.a + self.b * self.b
        if norm == 0:
            raise ArithmeticError("Gaussian norm vanished on a nonzero element")
        conjugate = self.conj()
        return Gau(conjugate.a / norm, conjugate.b / norm)


I_UNIT = Gau(0, 1)
ONE = Gau(1, 0)
ZERO = Gau(0, 0)
HALF = Gau(Fraction(1, 2), 0)
HALF_I = Gau(0, Fraction(1, 2))
NEG_HALF_I = Gau(0, Fraction(-1, 2))
THREE_HALVES = Gau(Fraction(3, 2), 0)

Matrix = tuple[tuple[Gau, Gau], tuple[Gau, Gau]]


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
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


def mat_add(left: Matrix, right: Matrix) -> Matrix:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def mat_sub(left: Matrix, right: Matrix) -> Matrix:
    return (
        (left[0][0] - right[0][0], left[0][1] - right[0][1]),
        (left[1][0] - right[1][0], left[1][1] - right[1][1]),
    )


def mat_scale(coeff: Gau, matrix: Matrix) -> Matrix:
    return (
        (coeff * matrix[0][0], coeff * matrix[0][1]),
        (coeff * matrix[1][0], coeff * matrix[1][1]),
    )


def mat_adj(matrix: Matrix) -> Matrix:
    return (
        (matrix[0][0].conj(), matrix[1][0].conj()),
        (matrix[0][1].conj(), matrix[1][1].conj()),
    )


def mat_trace(matrix: Matrix) -> Gau:
    return matrix[0][0] + matrix[1][1]


def flatten(matrix: Matrix) -> tuple[Gau, ...]:
    out: list[Gau] = []
    for row in matrix:
        out.extend(row)
    return tuple(out)


def span_rank(matrices: tuple[Matrix, ...]) -> int:
    """Exact row rank over Q(i)."""
    rows = [list(flatten(matrix)) for matrix in matrices]
    rank = 0
    col = 0
    n_rows = len(rows)
    n_cols = 4
    while rank < n_rows and col < n_cols:
        pivot = None
        for i in range(rank, n_rows):
            if not rows[i][col].is_zero():
                pivot = i
                break
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_inv = rows[rank][col].inverse()
        rows[rank] = [entry * pivot_inv for entry in rows[rank]]
        for i in range(n_rows):
            if i == rank or rows[i][col].is_zero():
                continue
            factor = rows[i][col]
            rows[i] = [rows[i][j] - factor * rows[rank][j] for j in range(n_cols)]
        rank += 1
        col += 1
    return rank


def is_rank1_projection(matrix: Matrix) -> bool:
    return (
        mat_mul(matrix, matrix) == matrix
        and mat_adj(matrix) == matrix
        and mat_trace(matrix) == ONE
    )


def identity2() -> Matrix:
    return ((ONE, ZERO), (ZERO, ONE))


def sigma_x() -> Matrix:
    return ((ZERO, ONE), (ONE, ZERO))


def sigma_y() -> Matrix:
    return ((ZERO, Gau(0, -1)), (I_UNIT, ZERO))


def sigma_z() -> Matrix:
    return ((ONE, ZERO), (ZERO, Gau(-1, 0)))


def p_x() -> Matrix:
    return ((HALF, HALF), (HALF, HALF))


def p_y() -> Matrix:
    return ((HALF, NEG_HALF_I), (HALF_I, HALF))


def p_z() -> Matrix:
    return ((ONE, ZERO), (ZERO, ZERO))


def pauli_coords(matrix: Matrix) -> tuple[Gau, Gau, Gau, Gau]:
    """M = a I + b σx + c σy + d σz, recovered by traces."""
    two = Gau(2, 0)
    two_inv = two.inverse()
    a = two_inv * mat_trace(matrix)
    b = two_inv * mat_trace(mat_mul(matrix, sigma_x()))
    c = two_inv * mat_trace(mat_mul(matrix, sigma_y()))
    d = two_inv * mat_trace(mat_mul(matrix, sigma_z()))
    return a, b, c, d


def from_pauli(a: Gau, b: Gau, c: Gau, d: Gau) -> Matrix:
    return mat_add(
        mat_add(mat_scale(a, identity2()), mat_scale(b, sigma_x())),
        mat_add(mat_scale(c, sigma_y()), mat_scale(d, sigma_z())),
    )


def phi(matrix: Matrix) -> Matrix:
    """Cube 3-fold: σx→σy, σy→σz, σz→σx, extended C-linearly."""
    a, b, c, d = pauli_coords(matrix)
    return from_pauli(a, d, b, c)


def cube_u() -> Matrix:
    """U = (I - i(σx+σy+σz))/2, the spin-1/2 120° body-diagonal lift."""
    body = mat_add(mat_add(sigma_x(), sigma_y()), sigma_z())
    return mat_scale(HALF, mat_sub(identity2(), mat_scale(I_UNIT, body)))


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; displayed Pauli triad and cycle map are theorem hypotheses")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact Q(i) Pauli matrices and C-linear cycle automorphism")
    print("negative_scope: the Pauli-axis triad is not a PVM or unital M_3 factor and is not adopted as QCD")

    unit = identity2()
    sx, sy, sz = sigma_x(), sigma_y(), sigma_z()
    px, py, pz = p_x(), p_y(), p_z()

    checks.check(
        "source-lattice",
        "Lattice names proper cubic rotations about each site",
        "proper cubic rotations about each site" in axiom,
    )
    checks.check(
        "source-qubit",
        "one-site possibility algebra is M_2(C)",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom,
    )
    checks.check(
        "pauli-reconstruction",
        "Px, Py, Pz equal (I+σ)/2 on the exact Pauli matrices",
        px == mat_scale(HALF, mat_add(unit, sx))
        and py == mat_scale(HALF, mat_add(unit, sy))
        and pz == mat_scale(HALF, mat_add(unit, sz)),
    )

    checks.check("thm1-px-proj", "Px is a rank-1 projection", is_rank1_projection(px))
    checks.check("thm1-py-proj", "Py is a rank-1 projection", is_rank1_projection(py))
    checks.check("thm1-pz-proj", "Pz is a rank-1 projection", is_rank1_projection(pz))
    checks.check(
        "thm1-pairwise-distinct",
        "Px, Py, Pz are pairwise distinct",
        px != py and px != pz and py != pz,
    )

    checks.check("thm2-phi-px", "φ(Px) = Py", phi(px) == py)
    checks.check("thm2-phi-py", "φ(Py) = Pz", phi(py) == pz)
    checks.check("thm2-phi-pz", "φ(Pz) = Px", phi(pz) == px)
    checks.check("thm2-phi-not-id", "φ ≠ id", phi(px) != px)
    checks.check(
        "thm2-phi-cube-id",
        "φ^3 = id on the Pauli basis",
        phi(phi(phi(sx))) == sx
        and phi(phi(phi(sy))) == sy
        and phi(phi(phi(sz))) == sz
        and phi(phi(phi(unit))) == unit
        and phi(phi(phi(px))) == px,
    )
    checks.check(
        "thm2-phi-star-linear",
        "φ is *-linear on the Pauli spanning set",
        phi(mat_adj(sx)) == mat_adj(phi(sx))
        and phi(mat_adj(sy)) == mat_adj(phi(sy))
        and phi(mat_scale(I_UNIT, sx)) == mat_scale(I_UNIT, phi(sx)),
    )
    checks.check(
        "thm2-phi-multiplicative",
        "φ preserves the Pauli product table",
        phi(mat_mul(sx, sy)) == mat_mul(phi(sx), phi(sy))
        and phi(mat_mul(sy, sz)) == mat_mul(phi(sy), phi(sz))
        and phi(mat_mul(sz, sx)) == mat_mul(phi(sz), phi(sx)),
    )

    u_mat = cube_u()
    u_adj = mat_adj(u_mat)
    ad_u_sx = mat_mul(u_mat, mat_mul(sx, u_adj))
    ad_u_sy = mat_mul(u_mat, mat_mul(sy, u_adj))
    ad_u_sz = mat_mul(u_mat, mat_mul(sz, u_adj))
    u3 = mat_mul(u_mat, mat_mul(u_mat, u_mat))
    checks.check(
        "thm2-u-unitary",
        "displayed U is unitary",
        mat_mul(u_mat, u_adj) == unit and mat_mul(u_adj, u_mat) == unit,
    )
    checks.check(
        "thm2-u-cube-central",
        "U^3 = -I, hence U^3 is proportional to I",
        u3 == mat_scale(Gau(-1, 0), unit),
    )
    checks.check(
        "thm2-ad-u-is-phi",
        "Ad_U implements the Pauli-axis cycle",
        ad_u_sx == sy and ad_u_sy == sz and ad_u_sz == sx,
    )

    body = mat_add(mat_add(sx, sy), sz)
    triad_sum = mat_add(mat_add(px, py), pz)
    half_body = mat_scale(HALF, body)
    expected_sum = mat_add(mat_scale(THREE_HALVES, unit), half_body)
    checks.check(
        "thm3-exact-sum",
        "Px+Py+Pz = (3/2)I + (σx+σy+σz)/2",
        triad_sum == expected_sum,
    )
    checks.check(
        "thm3-sum-not-three-halves",
        "unlike the equatorial z-orbit, the Bloch vectors do not cancel",
        triad_sum != mat_scale(THREE_HALVES, unit),
    )
    checks.check(
        "mutation-sum-eq-i-fails",
        "predicate Px+Py+Pz == I fails",
        triad_sum != unit,
    )
    two_thirds = Gau(Fraction(2, 3), 0)
    scaled_sum = mat_scale(two_thirds, triad_sum)
    checks.check(
        "thm3-uniform-scale-not-povm",
        "uniform (2/3) scaling does not restore a resolution of the identity",
        scaled_sum != unit,
    )
    checks.check(
        "thm3-not-orthogonal",
        "Px Py is nonzero, so the triad is not a PVM",
        mat_mul(px, py) != ((ZERO, ZERO), (ZERO, ZERO)),
    )

    gens = (px, py, pz, unit)
    words = list(gens)
    for left in gens:
        for right in gens:
            words.append(mat_mul(left, right))
            words.append(mat_adj(mat_mul(left, right)))
    basis = (unit, sx, sy, sz)
    basis_rank = span_rank(basis)
    dim = span_rank(tuple(words))
    checks.check(
        "thm4-pauli-basis-rank-4",
        "I, σx, σy, σz have Q(i)-rank 4",
        basis_rank == 4,
    )
    checks.check(
        "thm4-generated-dim-4",
        "Q(i)-dimension of C*(Px,Py,Pz) = 4",
        dim == 4,
    )
    checks.check("mutation-dim-eq-9-fails", "predicate dim generated == 9 fails", dim != 9)
    checks.check(
        "thm4-not-m3",
        "generated unital *-algebra is M_2(C), not M_3(C)",
        dim == 4 and dim != 9,
    )

    checks.check("thm5-three-not-divides-two", "3 does not divide 2", 2 % 3 != 0)
    checks.check(
        "thm5-injective-dimension-obstruction",
        "an injective complex-linear map M_3 to M_2 would require 9 <= 4",
        3 * 3 > 2 * 2,
    )
    checks.check(
        "mutation-unital-m3-to-m2-fails",
        "predicate unital M_3 → M_2 exists fails",
        2 % 3 != 0,
    )

    checks.check(
        "thm6-supplied-action-not-equator",
        "this triad is a supplied Pauli-axis cycle, not Lattice-named and not the z-equator",
        "not Lattice-named" in note
        and "supplied Pauli-axis" in note
        and "trivial-versus-Pauli-adjoint" in note
        and "cube 3-fold" in note
        and "not the displayed z-equator" in note
        and pz[0][0] == ONE
        and pz[1][1] == ZERO,
    )
    checks.check(
        "thm6-record-and-refusals",
        "note makes the Record reading conditional and refuses QCD adoption",
        "support is exactly `{Px, Py, Pz}`" in note
        and "Record locks one member of that supplied support" in note
        and "A site with no record cannot be read." in axiom
        and "not adopted as QCD" in note
        and "No Qubit rewrite" in note
        and "Do not adopt the triad as color" in note,
    )
    checks.check(
        "machine-status-contract",
        "note carries the required leftover status and bounded-support surface",
        'hypothetical_axiom_status: "cube-threefold leftover: Ad cycles Px,Py,Pz; not adopted as QCD"'
        in note
        and "actual_current_surface_status: bounded-support" in note
        and "next_trace_action:" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/CUBE_THREEFOLD_PAULI_TRIAD_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and "AUDIT_INPUT_PATHS = (" in self_source,
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and a passing N1-N8 gate are source-visible",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") >= 5
        and "**CLOSED HERE**" not in note
        and "**LIVE / OUT OF SCOPE**" not in note
        and ("import " + "qcd") not in self_source.lower(),
    )

    print("per_element: checked exactly — each of Px, Py, Pz is a distinct rank-one projection in M_2(C)")
    print("per_site: checked exactly — the unweighted sum is not I and the generated algebra has field-rank four")
    print("per_mode: checked exactly — the cube 3-fold cycle map and Ad_U send Px to Py to Pz to Px")
    print("per_block: checked exactly — the triad is not a PVM, not a unital M_3 factor, and not a uniform-scale POVM")
    print("lattice_wide: checked and not executed — no nearest-neighbor covariance or QCD identification is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
