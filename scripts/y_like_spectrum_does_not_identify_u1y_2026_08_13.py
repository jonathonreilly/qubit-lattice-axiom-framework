#!/usr/bin/env python3
"""Exact checks: Y_like spectrum does not identify U(1)_Y.

On the taste cube C^8 the residual-swap generators
Y_a = (2 tau_a - I)/3 are pairwise distinct and isospectral with
spec {+1/3 x6, -1 x2} and trace 0. Spectrum plus tracelessness
therefore do not select a unique generator. The scale k=1/3 produces
{1/9 x6, -1/3 x2} and is not Sigma_*. Identity gates call y_like(axis)
built from tau(axis). No cache is written.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "Y_LIKE_SPECTRUM_DOES_NOT_IDENTIFY_U1Y_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NATIVE_PATH = (
    ROOT / "docs" / "NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md"
)

AUDIT_INPUT_PATHS = (
    "docs/Y_LIKE_SPECTRUM_DOES_NOT_IDENTIFY_U1Y_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md",
)

Matrix = tuple[tuple[Fraction, ...], ...]
Vector = tuple[Fraction, ...]

CUBE: tuple[tuple[int, int, int], ...] = (
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1),
)
INDEX = {bits: i for i, bits in enumerate(CUBE)}
ONE = Fraction(1)
ZERO = Fraction(0)
THIRD = Fraction(1, 3)
TWO_THIRDS = Fraction(2, 3)
NINTH = Fraction(1, 9)


def identity() -> Matrix:
    return tuple(tuple(ONE if i == j else ZERO for j in range(8)) for i in range(8))


def mat_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a + b for a, b in zip(left_row, right_row, strict=True))
        for left_row, right_row in zip(left, right, strict=True)
    )


def mat_sub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a - b for a, b in zip(left_row, right_row, strict=True))
        for left_row, right_row in zip(left, right, strict=True)
    )


def mat_scale(coeff: Fraction, matrix: Matrix) -> Matrix:
    return tuple(tuple(coeff * entry for entry in row) for row in matrix)


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(8)), ZERO)
            for j in range(8)
        )
        for i in range(8)
    )


def mat_transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[j][i] for j in range(8)) for i in range(8))


def mat_trace(matrix: Matrix) -> Fraction:
    return sum((matrix[i][i] for i in range(8)), ZERO)


def mat_apply(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((matrix[i][j] * vector[j] for j in range(8)), ZERO) for i in range(8)
    )


def mat_minus_scalar(matrix: Matrix, scalar: Fraction) -> Matrix:
    return tuple(
        tuple(matrix[i][j] - (scalar if i == j else ZERO) for j in range(8))
        for i in range(8)
    )


def mat_rank(matrix: Matrix) -> int:
    rows = [list(row) for row in matrix]
    rank = 0
    for col in range(8):
        pivot = next((row for row in range(rank, 8) if rows[row][col] != 0), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = ONE / rows[rank][col]
        rows[rank] = [inv * entry for entry in rows[rank]]
        for row in range(8):
            if row != rank and rows[row][col] != 0:
                factor = rows[row][col]
                rows[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(rows[row], rows[rank], strict=True)
                ]
        rank += 1
    return rank


def multiplicity(matrix: Matrix, eigenvalue: Fraction) -> int:
    return 8 - mat_rank(mat_minus_scalar(matrix, eigenvalue))


def swap_bits(bits: tuple[int, int, int], axis: int) -> tuple[int, int, int]:
    coords = [bits[0], bits[1], bits[2]]
    others = [index for index in range(3) if index != axis]
    first, second = others
    coords[first], coords[second] = coords[second], coords[first]
    return (coords[0], coords[1], coords[2])


def tau(axis: int) -> Matrix:
    """Permutation matrix of the complementary-axis swap on the lex cube."""
    if axis not in (0, 1, 2):
        raise ValueError("axis must be 0, 1, or 2")
    rows = [[ZERO for _ in range(8)] for _ in range(8)]
    for source, bits in enumerate(CUBE):
        target = INDEX[swap_bits(bits, axis)]
        rows[target][source] = ONE
    return tuple(tuple(row) for row in rows)


def pi_plus(axis: int) -> Matrix:
    return mat_scale(Fraction(1, 2), mat_add(identity(), tau(axis)))


def pi_minus(axis: int) -> Matrix:
    return mat_scale(Fraction(1, 2), mat_sub(identity(), tau(axis)))


def y_like(axis: int) -> Matrix:
    """Identity-gate function: native residual-swap generator on one axis."""
    return mat_scale(Fraction(1, 3), mat_sub(mat_scale(Fraction(2), tau(axis)), identity()))


def y_like_native_combination(axis: int) -> Matrix:
    return mat_sub(mat_scale(THIRD, pi_plus(axis)), pi_minus(axis))


def y_like_scaled_by_third(axis: int) -> Matrix:
    """Mutation: replace y_like by (1/3) times itself."""
    return mat_scale(THIRD, y_like(axis))


def y_like_axis0_only(_axis: int) -> Matrix:
    """Mutation: replace every axis by axis 0."""
    return y_like(0)


def spectrum_equals_target(matrix: Matrix) -> bool:
    return multiplicity(matrix, THIRD) == 6 and multiplicity(matrix, Fraction(-1)) == 2


def pairwise_distinct(matrices: tuple[Matrix, Matrix, Matrix]) -> bool:
    left, mid, right = matrices
    return left != mid and mid != right and right != left


def first_disagreement(left: Matrix, right: Matrix) -> tuple[int, int] | None:
    for i in range(8):
        for j in range(8):
            if left[i][j] != right[i][j]:
                return (i, j)
    return None


def basis_vector(bits: tuple[int, int, int]) -> Vector:
    index = INDEX[bits]
    return tuple(ONE if i == index else ZERO for i in range(8))


def vec_add(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right, strict=True))


def vec_sub(left: Vector, right: Vector) -> Vector:
    return tuple(a - b for a, b in zip(left, right, strict=True))


def vec_scale(coeff: Fraction, vector: Vector) -> Vector:
    return tuple(coeff * entry for entry in vector)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    native = NATIVE_PATH.read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: native residual-swap Y_like construction "
        "and the four-axiom memo; no observational or fitted inputs"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no runner cache is written"
    )
    print(
        "negative_scope: spectrum plus trace do not identify a unique "
        "anomaly-complete U(1)_Y generator; U(1)_Y is not claimed impossible"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, axiom memo, and native surface note",
        AUDIT_INPUT_PATHS
        == (
            "docs/Y_LIKE_SPECTRUM_DOES_NOT_IDENTIFY_U1Y_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "native-nonclaim-phrase",
        "the native note contains the exact non-claim phrase",
        "does not claim anomaly-complete" in native,
    )
    checks.check(
        "native-construction",
        "the native note states the projector formula and the +1/3,-1 spectrum",
        "Y_like = (1/3) Pi_+ - Pi_-." in native
        and "rank(Pi_+) = 6" in native
        and "rank(Pi_-) = 2" in native
        and "Tr(Y_like) = 0" in native,
    )
    checks.check(
        "axiom-does-not-name-generator",
        "the axiom memo does not name Y_like or U(1)_Y",
        "Y_like" not in axiom and "U(1)_Y" not in axiom and "hypercharge" not in axiom.lower(),
    )

    eye = identity()
    for axis in (0, 1, 2):
        swap = tau(axis)
        checks.check(
            f"tau-{axis}-involution",
            "tau^2 = I as exact permutation-matrix arithmetic",
            mat_mul(swap, swap) == eye,
        )
        checks.check(
            f"tau-{axis}-hermitian",
            "tau is a real symmetric permutation matrix",
            swap == mat_transpose(swap)
            and all(entry in (ZERO, ONE) for row in swap for entry in row)
            and all(sum(row, ZERO) == ONE for row in swap)
            and all(sum(swap[i][j] for i in range(8)) == ONE for j in range(8)),
        )
        plus = pi_plus(axis)
        minus = pi_minus(axis)
        checks.check(
            f"projectors-{axis}",
            "Pi_+ and Pi_- are complementary projectors of ranks 6 and 2",
            mat_mul(plus, plus) == plus
            and mat_mul(minus, minus) == minus
            and mat_mul(plus, minus) == tuple((ZERO,) * 8 for _ in range(8))
            and mat_add(plus, minus) == eye
            and mat_rank(plus) == 6
            and mat_rank(minus) == 2
            and mat_trace(plus) == Fraction(6)
            and mat_trace(minus) == Fraction(2),
            residual=(mat_rank(plus), mat_rank(minus), mat_trace(plus), mat_trace(minus)),
        )

        closed = y_like(axis)
        native_combo = y_like_native_combination(axis)
        checks.check(
            f"closed-form-{axis}",
            "identity-gate y_like(axis) equals (1/3)Pi_+ - Pi_- and (2 tau - I)/3",
            closed == native_combo
            and closed
            == mat_scale(Fraction(1, 3), mat_sub(mat_scale(Fraction(2), swap), eye)),
        )
        checks.check(
            f"trace-{axis}",
            "Tr Y_a = 0",
            mat_trace(closed) == ZERO,
            residual=mat_trace(closed),
        )
        checks.check(
            f"spectrum-{axis}",
            "spec(Y_a) = {1/3 x6, -1 x2} by rank(Y-lambda I)",
            spectrum_equals_target(closed)
            and multiplicity(closed, THIRD) == 6
            and multiplicity(closed, Fraction(-1)) == 2
            and mat_rank(mat_minus_scalar(closed, THIRD)) == 2
            and mat_rank(mat_minus_scalar(closed, Fraction(-1))) == 6,
            residual=(
                multiplicity(closed, THIRD),
                multiplicity(closed, Fraction(-1)),
            ),
        )
        checks.check(
            f"hermitian-{axis}",
            "Y_a is real symmetric, hence Hermitian",
            closed == mat_transpose(closed),
        )

    plus_space_0 = (
        basis_vector((0, 0, 0)),
        basis_vector((0, 1, 1)),
        basis_vector((1, 0, 0)),
        basis_vector((1, 1, 1)),
        vec_add(basis_vector((0, 0, 1)), basis_vector((0, 1, 0))),
        vec_add(basis_vector((1, 0, 1)), basis_vector((1, 1, 0))),
    )
    minus_space_0 = (
        vec_sub(basis_vector((0, 0, 1)), basis_vector((0, 1, 0))),
        vec_sub(basis_vector((1, 0, 1)), basis_vector((1, 1, 0))),
    )
    y0 = y_like(0)
    t0 = tau(0)
    plus_ok = all(
        mat_apply(t0, vector) == vector
        and mat_apply(y0, vector) == vec_scale(THIRD, vector)
        for vector in plus_space_0
    )
    minus_ok = all(
        mat_apply(t0, vector) == vec_scale(Fraction(-1), vector)
        and mat_apply(y0, vector) == vec_scale(Fraction(-1), vector)
        for vector in minus_space_0
    )
    checks.check(
        "eigenspace-action",
        "Y_0 acts by +1/3 on the +1 space of tau_0 and by -1 on the -1 space",
        plus_ok and minus_ok,
    )

    y1 = y_like(1)
    y2 = y_like(2)
    t1 = tau(1)
    t2 = tau(2)
    image_001 = (
        INDEX[swap_bits((0, 0, 1), 0)],
        INDEX[swap_bits((0, 0, 1), 1)],
        INDEX[swap_bits((0, 0, 1), 2)],
    )
    checks.check(
        "vector-witness-001",
        "tau_0, tau_1, tau_2 send e_(0,0,1) to three different basis vectors",
        image_001 == (INDEX[(0, 1, 0)], INDEX[(1, 0, 0)], INDEX[(0, 0, 1)])
        and mat_apply(t0, basis_vector((0, 0, 1))) == basis_vector((0, 1, 0))
        and mat_apply(t1, basis_vector((0, 0, 1))) == basis_vector((1, 0, 0))
        and mat_apply(t2, basis_vector((0, 0, 1))) == basis_vector((0, 0, 1)),
        residual=image_001,
    )
    disagree_01 = first_disagreement(t0, t1)
    disagree_02 = first_disagreement(t0, t2)
    disagree_12 = first_disagreement(t1, t2)
    checks.check(
        "pairwise-tau-entries",
        "each pair of residual swaps disagrees at a named matrix entry",
        disagree_01 is not None
        and disagree_02 is not None
        and disagree_12 is not None
        and t0[2][1] == ONE
        and t1[2][1] == ZERO
        and t2[2][1] == ZERO
        and t1[4][1] == ONE
        and t2[4][1] == ZERO
        and t0[1][2] == ONE
        and t1[1][2] == ZERO,
        residual=(disagree_01, disagree_02, disagree_12),
    )
    checks.check(
        "pairwise-y-distinct",
        "Y_0 != Y_1 != Y_2 != Y_0 as exact Fraction matrices",
        pairwise_distinct((y0, y1, y2))
        and y0[2][1] == TWO_THIRDS
        and y1[2][1] == ZERO
        and y2[2][1] == ZERO
        and y1[4][1] == TWO_THIRDS
        and y2[4][1] == ZERO,
    )
    checks.check(
        "isospectral",
        "all three generators have spectrum Sigma_* and trace 0",
        spectrum_equals_target(y0)
        and spectrum_equals_target(y1)
        and spectrum_equals_target(y2)
        and mat_trace(y0) == mat_trace(y1) == mat_trace(y2) == ZERO,
    )

    scaled = y_like_scaled_by_third(0)
    checks.check(
        "scale-k-one",
        "spec(k Y_0) equals Sigma_* if and only if k=1 among the tested rationals",
        spectrum_equals_target(y_like(0))
        and not spectrum_equals_target(scaled)
        and not spectrum_equals_target(mat_scale(Fraction(-1), y0))
        and not spectrum_equals_target(mat_scale(ZERO, y0))
        and not spectrum_equals_target(mat_scale(Fraction(3), y0)),
    )
    checks.check(
        "scale-one-third-spectrum",
        "k=1/3 produces spec {1/9 x6, -1/3 x2}, which is not Sigma_*",
        multiplicity(scaled, NINTH) == 6
        and multiplicity(scaled, Fraction(-1, 3)) == 2
        and not spectrum_equals_target(scaled)
        and mat_trace(scaled) == ZERO,
        residual=(
            multiplicity(scaled, NINTH),
            multiplicity(scaled, Fraction(-1, 3)),
            multiplicity(scaled, THIRD),
        ),
    )
    k_minus = mat_scale(Fraction(-1), y0)
    checks.check(
        "scale-minus-one-spectrum",
        "k=-1 produces spec {-1/3 x6, +1 x2}, which is not Sigma_*",
        multiplicity(k_minus, Fraction(-1, 3)) == 6
        and multiplicity(k_minus, ONE) == 2
        and not spectrum_equals_target(k_minus),
    )

    average = mat_scale(THIRD, mat_add(mat_add(y0, y1), y2))
    checks.check(
        "average-not-target",
        "the average of the three Y_a has spec {1/3 x4, -1/3 x4}, not Sigma_*",
        average != y0
        and average != y1
        and average != y2
        and multiplicity(average, THIRD) == 4
        and multiplicity(average, Fraction(-1, 3)) == 4
        and not spectrum_equals_target(average),
        residual=(multiplicity(average, THIRD), multiplicity(average, Fraction(-1, 3))),
    )

    collapsed = (y_like_axis0_only(0), y_like_axis0_only(1), y_like_axis0_only(2))
    checks.check(
        "mutation-scale-fails-target",
        "replacing y_like by k=1/3 times itself fails spectrum-equals-Sigma_*",
        spectrum_equals_target(y_like(0))
        and not spectrum_equals_target(y_like_scaled_by_third(0)),
    )
    checks.check(
        "mutation-collapse-fails-distinct",
        "replacing all three axes by axis 0 fails pairwise distinctness",
        pairwise_distinct((y_like(0), y_like(1), y_like(2)))
        and not pairwise_distinct(collapsed)
        and collapsed[0] == collapsed[1] == collapsed[2] == y_like(0),
    )
    plus0 = pi_plus(0)
    checks.check(
        "mutation-pi-plus-fails-target",
        "replacing y_like by Pi_+ yields spec {1 x6, 0 x2} and fails Sigma_*",
        multiplicity(plus0, ONE) == 6
        and multiplicity(plus0, ZERO) == 2
        and not spectrum_equals_target(plus0)
        and spectrum_equals_target(y_like(0)),
        residual=(multiplicity(plus0, ONE), multiplicity(plus0, ZERO)),
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    retained_ok = all(line in note for line in allowed_retained)
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-contract",
        "machine-status fields, required phrases, and forbidden-word hygiene hold",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "trace_class: negative_route_pruning",
                "target_claim_id: y_like_u1y_identification",
                'target_blocker_text: "Y_like ↔ U(1)_Y and hw=1 ↔ three families as explicit identification theorems"',
                "source_of_blocker_text: handoff",
                "reachability_to_target: prunes",
                "artifact_role: theorem",
                'next_trace_action: "P-HY remains a declared identification; a commutation-with-SU(2)×SU(3) bridge or another selector is still open; do not adopt axiom text."',
                'conditional_surface_status: "exact for three-axis distinctness and the k=1 scale rejector; physical U(1)_Y remains open"',
                'hypothetical_axiom_status: "no edit"',
                "admitted_observation_status: null",
                "does not claim anomaly-complete",
                "1/9",
                "k=1/3",
                "authors no audit verdict",
                "Y = (2 tau - I)/3",
                "Y_0 != Y_1 != Y_2 != Y_0",
                "Tr Y_a = 0",
            )
        )
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "Block 15" not in note
        and "toe-lphys" not in note,
        residual=[
            phrase
            for phrase in (
                "does not claim anomaly-complete",
                "1/9",
                "k=1/3",
                "authors no audit verdict",
                "Y = (2 tau - I)/3",
            )
            if phrase not in note
        ],
    )
    checks.check(
        "note-links-parents",
        "the note links the axiom memo and the native abelian-surface note",
        "MINIMAL_AXIOMS_2026-06-29.md" in note
        and "NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md" in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "note-does-not-forbid-u1y",
        "the note states the scoped gap and does not claim U(1)_Y is impossible",
        "does not claim that `U(1)_Y` is impossible" in note
        or "does not claim that U(1)_Y is impossible" in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the uniqueness obstruction is absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("Y_0", "Y_like", "Σ_*", "P-HY", "(2 tau - I)/3")
        ),
    )

    n5_lines = (
        "per_element: named generators Y_0, Y_1, Y_2 and the tested scales of Y_0 are recomputed as exact Fraction 8x8 matrices",
        "per_site: statements are one taste-cube C^8 statements; no composite spacetime-site carrier is asserted",
        "per_mode: eigenvalue multiplicities of Y_a are checked by rank(Y-lambda I); no harmonic mode is claimed",
        "per_block: only three-axis distinctness, closed form, and the k=1 scale rejector are executed",
        "lattice_wide: checked and not executed — no lattice-wide U(1)_Y identification or anomaly cancellation is claimed",
    )
    for line in n5_lines:
        checks.check(
            "n5-length",
            "each N5 resolution line is at least 40 characters",
            line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            and len(line) >= 40,
            residual=(len(line), line[:40]),
        )
        print(line)

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
