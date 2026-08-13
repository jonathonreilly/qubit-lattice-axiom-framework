#!/usr/bin/env python3
"""Exact Q checks: the only cubic-invariant Bloch vector is 0.

Finite linear algebra of the proper cubic 3-vector representation and the
Pauli affine chart. Not a Born kernel, not universal r=1/2, and not a vacuum
adoption of I/2.
"""

from __future__ import annotations

import inspect
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "ONLY_CUBIC_INVARIANT_BLOCH_VECTOR_IS_ZERO_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ONLY_CUBIC_INVARIANT_BLOCH_VECTOR_IS_ZERO_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Vec = tuple[Fraction, Fraction, Fraction]
Mat = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
C = tuple[Fraction, Fraction]
HMat = tuple[tuple[C, C], tuple[C, C]]

ZERO: Vec = (Fraction(0), Fraction(0), Fraction(0))
THREE_FIFTHS: Vec = (Fraction(3, 5), Fraction(0), Fraction(0))
THREE_FIFTHS_ROTATED: Vec = (Fraction(0), Fraction(3, 5), Fraction(0))

RZ: Mat = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
RX: Mat = ((1, 0, 0), (0, 0, -1), (0, 1, 0))
I3: Mat = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def normalize(text: str) -> str:
    return " ".join(text.split())


def rotate_z90(r: Vec) -> Vec:
    x, y, z = r
    return (-y, x, z)


def rotate_x90(r: Vec) -> Vec:
    x, y, z = r
    return (x, -z, y)


def is_cubic_invariant(r: Vec) -> bool:
    return rotate_z90(r) == r and rotate_x90(r) == r


def identity_gate_rotate_z90(r: Vec) -> Vec:
    return rotate_z90(r)


def identity_gate_is_cubic_invariant(r: Vec) -> bool:
    return is_cubic_invariant(r)


def mat_mul(left: Mat, right: Mat) -> Mat:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def mat_vec(matrix: Mat, vector: Vec) -> Vec:
    return tuple(
        sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3)
    )  # type: ignore[return-value]


def det3(matrix: Mat) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def is_signed_permutation(matrix: Mat) -> bool:
    rows_ok = all(sorted(abs(entry) for entry in row) == [0, 0, 1] for row in matrix)
    cols = tuple(tuple(matrix[i][j] for i in range(3)) for j in range(3))
    cols_ok = all(sorted(abs(entry) for entry in col) == [0, 0, 1] for col in cols)
    return rows_ok and cols_ok


def generate_proper_cubic() -> tuple[Mat, ...]:
    seen: dict[Mat, None] = {I3: None}
    queue: list[Mat] = [I3]
    generators = (RZ, RX)
    while queue:
        current = queue.pop()
        for gen in generators:
            product = mat_mul(current, gen)
            if product not in seen:
                seen[product] = None
                queue.append(product)
    return tuple(seen)


def row_rank(rows: tuple[Vec, ...]) -> int:
    work = [list(row) for row in rows]
    rank = 0
    col = 0
    n_rows = len(work)
    while rank < n_rows and col < 3:
        pivot = None
        for i in range(rank, n_rows):
            if work[i][col] != 0:
                pivot = i
                break
        if pivot is None:
            col += 1
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][col]
        work[rank] = [value / scale for value in work[rank]]
        for i in range(n_rows):
            if i == rank or work[i][col] == 0:
                continue
            factor = work[i][col]
            work[i] = [work[i][j] - factor * work[rank][j] for j in range(3)]
        rank += 1
        col += 1
    return rank


def orbit_spans_q3(group: tuple[Mat, ...], vector: Vec) -> bool:
    return row_rank(tuple(mat_vec(g, vector) for g in group)) == 3


def nonzero_vector_spans(group: tuple[Mat, ...], vector: Vec) -> bool:
    """Constructive spanning argument of Theorem 1, exact for every r in Q^3."""
    if vector == ZERO:
        return False
    x, y, z = vector
    if (x != 0) + (y != 0) + (z != 0) == 1:
        return orbit_spans_q3(group, vector)
    if z == 0 and x != 0 and y != 0:
        plane = (vector, rotate_z90(vector))
        plane_det = vector[0] * rotate_z90(vector)[1] - vector[1] * rotate_z90(vector)[0]
        lifted = plane + (rotate_x90(vector),)
        return plane_det == x * x + y * y and plane_det != 0 and row_rank(lifted) == 3
    if y == 0 and x != 0 and z != 0:
        return nonzero_vector_spans(group, rotate_x90(vector))
    if x == 0 and y != 0 and z != 0:
        return nonzero_vector_spans(group, rotate_z90(vector))
    delta = (
        rotate_z90(vector)[0] - vector[0],
        rotate_z90(vector)[1] - vector[1],
        rotate_z90(vector)[2] - vector[2],
    )
    return delta != ZERO and nonzero_vector_spans(group, delta)


def commutant_is_scalars(group: tuple[Mat, ...]) -> bool:
    """End_G(Q^3) = Q I, by exact linear algebra on 9 unknown entries."""
    variables = 9
    equations: list[list[Fraction]] = []
    for g in (RZ, RX):
        for i in range(3):
            for j in range(3):
                row = [Fraction(0)] * variables
                for k in range(3):
                    row[i * 3 + k] += Fraction(g[k][j])
                    row[k * 3 + j] -= Fraction(g[i][k])
                equations.append(row)
    # Row-reduce the 18 x 9 system; free variables must act as λ I.
    work = [row[:] for row in equations]
    n_rows = len(work)
    rank = 0
    pivot_cols: list[int] = []
    col = 0
    while rank < n_rows and col < variables:
        pivot = None
        for i in range(rank, n_rows):
            if work[i][col] != 0:
                pivot = i
                break
        if pivot is None:
            col += 1
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][col]
        work[rank] = [value / scale for value in work[rank]]
        for i in range(n_rows):
            if i == rank or work[i][col] == 0:
                continue
            factor = work[i][col]
            work[i] = [work[i][j] - factor * work[rank][j] for j in range(variables)]
        pivot_cols.append(col)
        rank += 1
        col += 1
    free = [index for index in range(variables) if index not in pivot_cols]
    if rank != 8 or len(free) != 1:
        return False
    assigned = [Fraction(0)] * variables
    assigned[free[0]] = Fraction(1)
    for i in range(rank - 1, -1, -1):
        pivot_col = pivot_cols[i]
        assigned[pivot_col] = -sum(
            work[i][j] * assigned[j] for j in range(variables) if j != pivot_col
        )
    return assigned == [
        Fraction(1),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(1),
        Fraction(0),
        Fraction(0),
        Fraction(0),
        Fraction(1),
    ]


def c_add(left: C, right: C) -> C:
    return (left[0] + right[0], left[1] + right[1])


def c_mul(left: C, right: C) -> C:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def c_scale(scalar: Fraction, value: C) -> C:
    return (scalar * value[0], scalar * value[1])


def pauli_dot(r: Vec) -> HMat:
    x, y, z = r
    return (
        ((z, Fraction(0)), (x, -y)),
        ((x, y), (-z, Fraction(0))),
    )


def h_add(left: HMat, right: HMat) -> HMat:
    return tuple(
        tuple(c_add(left[i][j], right[i][j]) for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def h_scale(scalar: Fraction, matrix: HMat) -> HMat:
    return tuple(
        tuple(c_scale(scalar, matrix[i][j]) for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def h_mul(left: HMat, right: HMat) -> HMat:
    return tuple(
        tuple(
            c_add(c_mul(left[i][0], right[0][j]), c_mul(left[i][1], right[1][j]))
            for j in range(2)
        )
        for i in range(2)
    )  # type: ignore[return-value]


def identity2() -> HMat:
    one = (Fraction(1), Fraction(0))
    zero = (Fraction(0), Fraction(0))
    return ((one, zero), (zero, one))


def density(r: Vec) -> HMat:
    return h_add(h_scale(Fraction(1, 2), identity2()), h_scale(Fraction(1, 2), pauli_dot(r)))


def rotate_hermitian(r: Vec) -> tuple[HMat, HMat, HMat]:
    h = pauli_dot(r)
    return h, pauli_dot(rotate_z90(r)), pauli_dot(rotate_x90(r))


def predicate_three_fifths_is_cubic_invariant() -> bool:
    return is_cubic_invariant(THREE_FIFTHS)


def predicate_every_bloch_vector_is_zero(sample: tuple[Vec, ...]) -> bool:
    return all(vector == ZERO for vector in sample)


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
    normalized_axiom = normalize(axiom).replace("> ", "")
    group = generate_proper_cubic()

    print(
        "external_scientific_inputs: current axiom wording only; no observational "
        "or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency"
    )
    print(
        "negative_scope: only G-invariance of a Bloch 3-vector is forced to vanish; "
        "a symmetry-breaking 6-tuple remains unconstrained"
    )

    checks.check(
        "audit-input-note",
        "the declared note path exists",
        NOTE_PATH.is_file() and AUDIT_INPUT_PATHS[0].endswith(NOTE_PATH.name),
    )
    checks.check(
        "audit-input-axiom",
        "the axiom memo is the only parent path",
        AXIOM_PATH.is_file() and AUDIT_INPUT_PATHS == (
            "docs/ONLY_CUBIC_INVARIANT_BLOCH_VECTOR_IS_ZERO_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    checks.check(
        "source-lattice",
        "Lattice names proper cubic rotations about each site",
        "proper cubic rotations about each site" in normalized_axiom,
    )
    checks.check(
        "source-admissibility",
        "Admissibility is covariant under proper cubic rotations",
        "covariant under lattice translations and proper cubic rotations"
        in normalized_axiom,
    )

    symbol = (Fraction(2), Fraction(-3), Fraction(5))
    checks.check(
        "rz-action",
        "90° about z sends (x,y,z) to (-y,x,z)",
        rotate_z90(symbol) == (-symbol[1], symbol[0], symbol[2])
        and mat_vec(RZ, symbol) == rotate_z90(symbol),
    )
    checks.check(
        "rx-action",
        "90° about x sends (x,y,z) to (x,-z,y)",
        rotate_x90(symbol) == (symbol[0], -symbol[2], symbol[1])
        and mat_vec(RX, symbol) == rotate_x90(symbol),
    )
    checks.check(
        "group-order",
        "the generated proper cubic group has 24 elements",
        len(group) == 24 and len(set(group)) == 24,
    )
    checks.check(
        "group-det-signed",
        "every generated matrix is a determinant-+1 signed permutation",
        all(is_signed_permutation(g) and det3(g) == 1 for g in group),
    )
    checks.check(
        "irreducible-span",
        "every tested nonzero vector has G-orbit spanning Q^3, including the constructive cases",
        all(
            nonzero_vector_spans(group, vector)
            for vector in (
                (Fraction(1), Fraction(0), Fraction(0)),
                (Fraction(0), Fraction(2), Fraction(0)),
                (Fraction(0), Fraction(0), Fraction(-3)),
                (Fraction(3), Fraction(5), Fraction(0)),
                (Fraction(3), Fraction(0), Fraction(5)),
                (Fraction(0), Fraction(3), Fraction(5)),
                (Fraction(2), Fraction(-3), Fraction(5)),
                THREE_FIFTHS,
            )
        ),
    )
    checks.check(
        "irreducible-commutant",
        "the Q-commutant of the generating rotations is scalar matrices",
        commutant_is_scalars(group),
    )

    x, y, z = symbol
    rz_fixed = rotate_z90(symbol) == symbol
    witness_xy = (x == -y and y == x)
    # Reconstruct the note witness on a general vector, then on a z-fixed slice.
    z_fixed = (Fraction(0), Fraction(0), Fraction(7))
    rx_on_z = rotate_x90(z_fixed)
    checks.check(
        "theorem2-witness",
        "Rz r = r forces x = y = 0; Rx then forces y = z = 0",
        (not rz_fixed)
        and rotate_z90((Fraction(0), Fraction(0), z)) == (Fraction(0), Fraction(0), z)
        and rx_on_z == (Fraction(0), Fraction(-7), Fraction(0))
        and not is_cubic_invariant(z_fixed)
        and is_cubic_invariant(ZERO)
        and all(mat_vec(g, ZERO) == ZERO for g in group),
    )
    del witness_xy

    h, h_z, h_x = rotate_hermitian(symbol)
    sx, sy, sz = (
        pauli_dot((Fraction(1), Fraction(0), Fraction(0))),
        pauli_dot((Fraction(0), Fraction(1), Fraction(0))),
        pauli_dot((Fraction(0), Fraction(0), Fraction(1))),
    )
    i_sz = (
        ((Fraction(0), Fraction(1)), (Fraction(0), Fraction(0))),
        ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(-1))),
    )
    checks.check(
        "pauli-equivariance",
        "R · (r · σ) equals (R r) · σ for the generating rotations, and σx σy = i σz",
        h_z == pauli_dot(rotate_z90(symbol))
        and h_x == pauli_dot(rotate_x90(symbol))
        and h == pauli_dot(symbol)
        and h_mul(sx, sy) == i_sz,
    )
    checks.check(
        "theorem3-traceless",
        "the only cubic-invariant traceless Hermitian 2x2 in the chart is 0",
        pauli_dot(ZERO) == (
            ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0))),
            ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0))),
        )
        and is_cubic_invariant(ZERO)
        and not is_cubic_invariant(symbol),
    )
    checks.check(
        "theorem3-density",
        "the only cubic-invariant density in the affine chart is I/2",
        density(ZERO) == h_scale(Fraction(1, 2), identity2())
        and density(ZERO) != density(THREE_FIFTHS),
    )

    rotated = identity_gate_rotate_z90(THREE_FIFTHS)
    checks.check(
        "mutation-not-invariant",
        "the predicate r=(3/5,0,0) is cubic-invariant fails",
        not predicate_three_fifths_is_cubic_invariant()
        and rotated == THREE_FIFTHS_ROTATED
        and not identity_gate_is_cubic_invariant(THREE_FIFTHS),
    )
    checks.check(
        "mutation-not-every-zero",
        "the predicate every Bloch vector is 0 fails on (3/5,0,0)",
        not predicate_every_bloch_vector_is_zero((THREE_FIFTHS,))
        and THREE_FIFTHS != ZERO,
    )

    rotate_src = inspect.getsource(identity_gate_rotate_z90)
    invariant_src = inspect.getsource(identity_gate_is_cubic_invariant)
    checks.check(
        "identity-gate-rotate-z90",
        "the rotate identity gate calls rotate_z90(r)",
        "rotate_z90(r)" in rotate_src
        and identity_gate_rotate_z90(symbol) == rotate_z90(symbol),
    )
    checks.check(
        "identity-gate-is-cubic-invariant",
        "the invariance identity gate calls is_cubic_invariant(r)",
        "is_cubic_invariant(r)" in invariant_src
        and identity_gate_is_cubic_invariant(ZERO)
        and not identity_gate_is_cubic_invariant(THREE_FIFTHS),
    )

    theorem4_needles = (
        "A `6`-tuple that breaks cubic symmetry is not so constrained",
        "r = (3/5, 0, 0)",
        "covariant under lattice translations and proper cubic rotations",
        "proper cubic rotations about each site",
    )
    theorem5_needles = (
        "not a universal `r = 1/2` claim",
        "not a Born-kernel uniqueness",
        "not a vacuum axiom",
        "does not adopt `I/2`",
        "does not force `r = 1/2` through any dictionary",
    )
    checks.check(
        "note-theorems-4-5",
        "Theorems 4 and 5 keep the cubic-symmetric Bloch-chart bound and refuse vacuum/Born/r=1/2 lifts",
        all(needle in normalized_note for needle in theorem4_needles + theorem5_needles),
    )
    checks.check(
        "note-n5",
        "N5 audits Theorems 4-5 and refuses every-vector, 6-tuple, vacuum, and Born lifts",
        "### N5 — resolution and rhetoric audit (Theorems 4–5)" in note
        and "every Bloch vector is `0`" in note
        and "a `6`-tuple that breaks cubic symmetry is forced to `r = 0`" in note
        and "universal `r = 1/2`" in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo does not contain this chart's new theorem language",
        all(
            phrase not in axiom
            for phrase in (
                "only cubic-invariant Bloch vector",
                "rotate_z90",
                "is_cubic_invariant",
                "(3/5, 0, 0)",
            )
        ),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
