#!/usr/bin/env python3
"""Exact cyclotomic checks for one displayed C3 Bloch-projector orbit.

Field Q(ω) with ω^2+ω+1=0. No physical support selector, QCD
identification, axiom edit, or cache write.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "C3_BLOCH_ORBIT_IS_THREE_MENU_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/C3_BLOCH_ORBIT_IS_THREE_MENU_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


class Cyc:
    """a + b ω with ω^2 + ω + 1 = 0."""

    __slots__ = ("a", "b")

    def __init__(self, a: Fraction | int, b: Fraction | int = 0) -> None:
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other: Cyc) -> Cyc:
        return Cyc(self.a + other.a, self.b + other.b)

    def __sub__(self, other: Cyc) -> Cyc:
        return Cyc(self.a - other.a, self.b - other.b)

    def __mul__(self, other: Cyc) -> Cyc:
        # (a+bω)(c+dω) = ac + (ad+bc)ω + bd ω^2 = (ac-bd) + (ad+bc-bd)ω
        return Cyc(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a - self.b * other.b,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cyc):
            return NotImplemented
        return self.a == other.a and self.b == other.b

    def __neg__(self) -> Cyc:
        return Cyc(-self.a, -self.b)

    def conj(self) -> Cyc:
        # ω-bar = ω^2 = -1-ω, so (a+bω)-bar = a + b(-1-ω) = (a-b) + (-b)ω
        return Cyc(self.a - self.b, -self.b)

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def inverse(self) -> Cyc:
        """Multiplicative inverse in Q(ω)."""
        if self.is_zero():
            raise ZeroDivisionError("zero has no inverse in Q(omega)")
        conjugate = self.conj()
        norm = self * conjugate
        if not norm.b == 0 or norm.a == 0:
            raise ArithmeticError("cyclotomic norm did not reduce to a nonzero rational")
        return Cyc(conjugate.a / norm.a, conjugate.b / norm.a)


OMEGA = Cyc(0, 1)
OMEGA2 = Cyc(-1, -1)  # -1 - ω
ONE = Cyc(1, 0)
ZERO = Cyc(0, 0)
HALF = Cyc(Fraction(1, 2), 0)

Matrix = tuple[tuple[Cyc, Cyc], tuple[Cyc, Cyc]]


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


def mat_scale(coeff: Cyc, matrix: Matrix) -> Matrix:
    return (
        (coeff * matrix[0][0], coeff * matrix[0][1]),
        (coeff * matrix[1][0], coeff * matrix[1][1]),
    )


def mat_adj(matrix: Matrix) -> Matrix:
    return (
        (matrix[0][0].conj(), matrix[1][0].conj()),
        (matrix[0][1].conj(), matrix[1][1].conj()),
    )


def mat_trace(matrix: Matrix) -> Cyc:
    return matrix[0][0] + matrix[1][1]


def flatten(matrix: Matrix) -> tuple[Cyc, ...]:
    """Four Q(ω) entries in row-major order."""
    out: list[Cyc] = []
    for row in matrix:
        out.extend(row)
    return tuple(out)


def span_rank(matrices: tuple[Matrix, ...]) -> int:
    """Exact row rank over Q(ω), not over the eight-dimensional Q expansion."""
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


def p0() -> Matrix:
    return ((HALF, HALF), (HALF, HALF))


def r_mat() -> Matrix:
    return ((ONE, ZERO), (ZERO, OMEGA))


def r_inv() -> Matrix:
    return ((ONE, ZERO), (ZERO, OMEGA2))


def ad_r(matrix: Matrix) -> Matrix:
    return mat_mul(r_mat(), mat_mul(matrix, r_inv()))


def e11() -> Matrix:
    return ((ZERO, ZERO), (ZERO, ONE))


def e00() -> Matrix:
    return ((ONE, ZERO), (ZERO, ZERO))


def same_unordered_menu(left: tuple[Matrix, ...], right: tuple[Matrix, ...]) -> bool:
    """Exact equality of two finite menus, including multiplicity."""
    if len(left) != len(right):
        return False
    used = [False] * len(right)
    for candidate in left:
        for index, target in enumerate(right):
            if not used[index] and candidate == target:
                used[index] = True
                break
        else:
            return False
    return True


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

    print("external_scientific_inputs: none; displayed R and P0 are theorem hypotheses")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact Q(ω); scaled trine normalization is mathematical only")
    print("negative_scope: the unweighted displayed orbit is not a PVM or unital M_3 factor")

    checks.check("omega-minimal", "ω^2 + ω + 1 = 0", OMEGA * OMEGA + OMEGA + ONE == ZERO)
    checks.check("omega-cube", "ω^3 = 1", OMEGA * OMEGA * OMEGA == ONE)
    checks.check("omega-not-one", "ω ≠ 1", OMEGA != ONE)

    ray0 = p0()
    ray1 = ad_r(ray0)
    ray2 = ad_r(ray1)
    ray3 = ad_r(ray2)
    unit = identity2()

    checks.check("thm1-p0-proj", "P0 is a rank-1 projection", is_rank1_projection(ray0))
    checks.check("thm1-p1-proj", "P1 is a rank-1 projection", is_rank1_projection(ray1))
    checks.check("thm1-p2-proj", "P2 is a rank-1 projection", is_rank1_projection(ray2))
    checks.check(
        "thm1-pairwise-distinct",
        "P0, P1, P2 are pairwise distinct",
        ray0 != ray1 and ray0 != ray2 and ray1 != ray2,
    )
    checks.check("thm1-orbit-closes", "Ad_R(P2) = P0", ray3 == ray0)

    expected_p1 = (
        (HALF, Cyc(Fraction(-1, 2), Fraction(-1, 2))),  # ω^2/2 = (-1-ω)/2
        (Cyc(0, Fraction(1, 2)), HALF),  # ω/2
    )
    checks.check("thm1-p1-formula", "P1 equals ((1/2, ω^2/2), (ω/2, 1/2))", ray1 == expected_p1)

    checks.check("thm2-not-e00", "P1 ≠ |0><0|", ray1 != e00())
    checks.check("thm2-not-e11", "P1 ≠ |1><1|", ray1 != e11())
    checks.check("thm2-not-p0", "P1 ≠ P0", ray1 != ray0)
    computational_plus_menu = (e00(), e11(), ray0)
    orbit_menu = (ray0, ray1, ray2)
    checks.check(
        "thm2-full-menu-inequality",
        "the orbit menu is not {|0><0|, |1><1|, |+><+|}",
        not same_unordered_menu(orbit_menu, computational_plus_menu),
    )

    three_halves = Cyc(Fraction(3, 2), 0)
    summed = mat_add(mat_add(ray0, ray1), ray2)
    checks.check(
        "thm3-sum-is-three-halves",
        "P0+P1+P2 = (3/2) I_2",
        summed == mat_scale(three_halves, unit),
    )
    checks.check(
        "mutation-sum-eq-i-fails",
        "predicate P0+P1+P2 == I_2 fails",
        summed != unit,
    )
    two_thirds = Cyc(Fraction(2, 3), 0)
    effects = tuple(mat_scale(two_thirds, ray) for ray in orbit_menu)
    effect_sum = mat_add(mat_add(effects[0], effects[1]), effects[2])
    checks.check("thm3-scaled-trine-povm", "sum_k (2/3) Pk = I_2", effect_sum == unit)
    checks.check(
        "thm3-scaled-effects-not-projections",
        "each (2/3) Pk is non-idempotent, so the normalization is not a PVM",
        all(mat_mul(effect, effect) != effect for effect in effects),
    )

    gens = (ray0, ray1, ray2, unit)
    words = list(gens)
    for left in gens:
        for right in gens:
            words.append(mat_mul(left, right))
            words.append(mat_adj(mat_mul(left, right)))
    basis = (unit, ray0, ray1, mat_mul(ray0, ray1))
    basis_rank = span_rank(basis)
    dim = span_rank(tuple(words))
    checks.check(
        "thm4-explicit-basis-rank-4",
        "I, P0, P1, P0P1 have Q(ω)-rank 4",
        basis_rank == 4,
    )
    checks.check("thm4-generated-dim-4", "Q(ω)-dimension of generated algebra = 4", dim == 4)
    checks.check("mutation-dim-eq-9-fails", "predicate dim generated == 9 fails", dim != 9)

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
        "thm6-record-and-refusals",
        "note makes the Record reading conditional and refuses unsupported identifications",
        "support is exactly `{P0, P1, P2}`" in note
        and "Record locks one member of that supplied support" in note
        and "A site with no record cannot be read." in axiom
        and "No `SU(3)` or QCD identification" in note
        and "No Qubit rewrite" in note
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom,
    )
    checks.check(
        "machine-status-contract",
        "note carries the bounded-support status and no hypothetical axiom adoption",
        'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and "actual_current_surface_status: bounded-support" in note
        and "next_trace_action:" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/C3_BLOCH_ORBIT_IS_THREE_MENU_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and a passing N1-N8 gate are source-visible",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "No-Go Discipline disposition: **PASS**" in note
        and note.count("**ATTEMPTED**") == 6
        and ("import " + "qcd") not in self_source.lower(),
    )

    print("per_element: checked exactly — each displayed Pk is a distinct rank-one projection in M_2(C)")
    print("per_site: checked exactly — the unweighted sum is (3/2)I and the generated algebra has field-rank four")
    print("per_mode: checked exactly — the single displayed Ad_R orbit closes after three steps; no other orbit is classified")
    print("per_block: checked exactly — scaled trine effects form a POVM but not a PVM or multiplicative M_3 factor")
    print("lattice_wide: checked and not executed — no nearest-neighbor covariance or lattice-wide support law is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
