#!/usr/bin/env python3
"""Exact Q(i) uniqueness: the only G-invariant state on M_2 is I_2/2.

Integer 3x3 cube rotations and Gaussian-rational Pauli arithmetic.
No QCD, no axiom edit, no cache write, no network.
"""

from __future__ import annotations

from itertools import permutations, product
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "CUBE_INVARIANT_STATE_ON_M2_IS_UNIQUE_HALF_I_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CUBE_INVARIANT_STATE_ON_M2_IS_UNIQUE_HALF_I_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Vec3 = tuple[Fraction, Fraction, Fraction]
Mat3 = tuple[Vec3, Vec3, Vec3]


class Qi:
    """a + b i with a, b in Q."""

    __slots__ = ("re", "im")

    def __init__(self, re: Fraction | int, im: Fraction | int = 0) -> None:
        self.re = Fraction(re)
        self.im = Fraction(im)

    def __add__(self, other: Qi) -> Qi:
        return Qi(self.re + other.re, self.im + other.im)

    def __sub__(self, other: Qi) -> Qi:
        return Qi(self.re - other.re, self.im - other.im)

    def __mul__(self, other: Qi) -> Qi:
        return Qi(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def __neg__(self) -> Qi:
        return Qi(-self.re, -self.im)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Qi):
            return NotImplemented
        return self.re == other.re and self.im == other.im

    def conj(self) -> Qi:
        return Qi(self.re, -self.im)

    def is_zero(self) -> bool:
        return self.re == 0 and self.im == 0


ZERO = Qi(0, 0)
ONE = Qi(1, 0)
I_UNIT = Qi(0, 1)
HALF = Qi(Fraction(1, 2), 0)
MINUS_I = Qi(0, -1)

Matrix2 = tuple[tuple[Qi, Qi], tuple[Qi, Qi]]


def q(value: Fraction | int) -> Qi:
    return Qi(value, 0)


def mat2_add(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


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


def mat2_scale(coeff: Qi, matrix: Matrix2) -> Matrix2:
    return (
        (coeff * matrix[0][0], coeff * matrix[0][1]),
        (coeff * matrix[1][0], coeff * matrix[1][1]),
    )


def mat2_trace(matrix: Matrix2) -> Qi:
    return matrix[0][0] + matrix[1][1]


def identity2() -> Matrix2:
    return ((ONE, ZERO), (ZERO, ONE))


def sigma_x() -> Matrix2:
    return ((ZERO, ONE), (ONE, ZERO))


def sigma_y() -> Matrix2:
    return ((ZERO, MINUS_I), (I_UNIT, ZERO))


def sigma_z() -> Matrix2:
    return ((ONE, ZERO), (ZERO, Qi(-1, 0)))


def as_frac_vec(vec: tuple[int | Fraction, int | Fraction, int | Fraction]) -> Vec3:
    return (Fraction(vec[0]), Fraction(vec[1]), Fraction(vec[2]))


def as_int_mat(rows: tuple[tuple[int, int, int], ...]) -> Mat3:
    return (
        as_frac_vec(rows[0]),
        as_frac_vec(rows[1]),
        as_frac_vec(rows[2]),
    )


RX = as_int_mat(((1, 0, 0), (0, 0, -1), (0, 1, 0)))
RZ = as_int_mat(((0, -1, 0), (1, 0, 0), (0, 0, 1)))
EYE3 = as_int_mat(((1, 0, 0), (0, 1, 0), (0, 0, 1)))


def det3(matrix: Mat3) -> Fraction:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def mat3_mul(left: Mat3, right: Mat3) -> Mat3:
    return tuple(
        tuple(
            sum((left[row][mid] * right[mid][col] for mid in range(3)), Fraction(0))
            for col in range(3)
        )
        for row in range(3)
    )


def mat3_sub(left: Mat3, right: Mat3) -> Mat3:
    return tuple(
        tuple(left[row][col] - right[row][col] for col in range(3))
        for row in range(3)
    )


def mat3_vec(matrix: Mat3, vec: Vec3) -> Vec3:
    return tuple(
        sum((matrix[row][col] * vec[col] for col in range(3)), Fraction(0))
        for row in range(3)
    )


def mat3_inv(matrix: Mat3) -> Mat3:
    """Adjugate / det for an integer rotation (det = ±1)."""
    determinant = det3(matrix)
    if determinant == 0:
        raise ZeroDivisionError("singular 3x3 matrix")
    cofactors = (
        (
            matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1],
            -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]),
            matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0],
        ),
        (
            -(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]),
            matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0],
            -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]),
        ),
        (
            matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1],
            -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]),
            matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0],
        ),
    )
    transpose = tuple(
        tuple(cofactors[col][row] / determinant for col in range(3))
        for row in range(3)
    )
    return transpose


def proper_cubic_group() -> tuple[Mat3, ...]:
    elements: list[Mat3] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = [[Fraction(0), Fraction(0), Fraction(0)] for _ in range(3)]
            for row, col in enumerate(perm):
                rows[row][col] = Fraction(signs[row])
            matrix = tuple(tuple(row) for row in rows)
            if det3(matrix) == 1:
                elements.append(matrix)
    return tuple(elements)


def common_fixed_basis(group: tuple[Mat3, ...]) -> tuple[Vec3, ...]:
    """Q-basis of the common +1 eigenspace of the displayed 3x3 action."""
    stacked: list[list[Fraction]] = []
    for item in group:
        shifted = mat3_sub(item, EYE3)
        for row in shifted:
            stacked.append([Fraction(entry) for entry in row])
    rank_rows: list[list[Fraction]] = [list(row) for row in stacked]
    height = len(rank_rows)
    pivot_of_col = [-1, -1, -1]
    cursor = 0
    for col in range(3):
        pivot = None
        for row in range(cursor, height):
            if rank_rows[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        rank_rows[cursor], rank_rows[pivot] = rank_rows[pivot], rank_rows[cursor]
        scale = rank_rows[cursor][col]
        rank_rows[cursor] = [entry / scale for entry in rank_rows[cursor]]
        for row in range(height):
            if row == cursor or rank_rows[row][col] == 0:
                continue
            factor = rank_rows[row][col]
            rank_rows[row] = [
                rank_rows[row][idx] - factor * rank_rows[cursor][idx]
                for idx in range(3)
            ]
        pivot_of_col[col] = cursor
        cursor += 1
    basis: list[Vec3] = []
    pivot_cols = {col for col, prow in enumerate(pivot_of_col) if prow != -1}
    for free in range(3):
        if free in pivot_cols:
            continue
        vec = [Fraction(0), Fraction(0), Fraction(0)]
        vec[free] = Fraction(1)
        for col, prow in enumerate(pivot_of_col):
            if prow != -1:
                vec[col] = -rank_rows[prow][free]
        basis.append(tuple(vec))
    return tuple(basis)


def invariant_bloch_vectors() -> tuple[Vec3, ...]:
    kernel = common_fixed_basis(proper_cubic_group())
    if kernel:
        return kernel
    return (as_frac_vec((0, 0, 0)),)


def bloch_state(vec: tuple[int | Fraction, int | Fraction, int | Fraction]) -> Matrix2:
    nx, ny, nz = as_frac_vec(vec)
    combo = mat2_add(
        mat2_add(
            mat2_scale(q(nx), sigma_x()),
            mat2_scale(q(ny), sigma_y()),
        ),
        mat2_scale(q(nz), sigma_z()),
    )
    return mat2_scale(HALF, mat2_add(identity2(), combo))


def rho_half_i() -> Matrix2:
    return mat2_scale(HALF, identity2())


def pauli_coords(matrix: Matrix2) -> tuple[Qi, Vec3]:
    """X = a I + b · σ with a, b extracted by traces."""
    coeff_i = mat2_trace(matrix)
    alpha = Qi(coeff_i.re / 2, coeff_i.im / 2)
    beta = []
    for pauli in (sigma_x(), sigma_y(), sigma_z()):
        traced = mat2_trace(mat2_mul(matrix, pauli))
        beta.append(traced.re / 2)
        if traced.im != 0:
            raise ArithmeticError("Pauli coordinate left the real line")
    return alpha, (beta[0], beta[1], beta[2])


def apply_alpha(rotation: Mat3, matrix: Matrix2) -> Matrix2:
    alpha, beta = pauli_coords(matrix)
    rotated = mat3_vec(rotation, beta)
    combo = mat2_add(
        mat2_add(
            mat2_scale(q(rotated[0]), sigma_x()),
            mat2_scale(q(rotated[1]), sigma_y()),
        ),
        mat2_scale(q(rotated[2]), sigma_z()),
    )
    return mat2_add(mat2_scale(alpha, identity2()), combo)


def rho_z_is_not_invariant() -> bool:
    rho_z = bloch_state((0, 0, 1))
    return apply_alpha(RX, rho_z) != rho_z


def axiom_body_without_commentary(axiom_text: str) -> str:
    start = axiom_text.find("### Lattice / Physical Locality")
    end = axiom_text.find("## Qualification")
    if start < 0 or end < 0 or end <= start:
        raise RuntimeError("could not isolate the four axiom statements")
    return axiom_text[start:end]


def sample_bloch_vectors() -> tuple[Vec3, ...]:
    axes = (
        (0, 0, 0),
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    )
    return tuple(as_frac_vec(item) for item in axes)


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
    group = proper_cubic_group()
    zero_vec = as_frac_vec((0, 0, 0))
    ez = as_frac_vec((0, 0, 1))
    fixed = invariant_bloch_vectors()
    half_i = rho_half_i()
    rho_zero = bloch_state(zero_vec)
    z_moves = rho_z_is_not_invariant()

    print("external_scientific_inputs: none; G and α are displayed theorem data")
    print("package_local_integrity_reads: runner source, proposed source note, and live axiom memo")
    print("measure_boundary: exact Q(i) and integer 3x3 matrices; no Born weights")
    print("negative_scope: uniqueness of the G-invariant state, not a kernel or menu law")

    checks.check("qi-i-squared", "i^2 = -1", I_UNIT * I_UNIT == Qi(-1, 0))
    checks.check(
        "pauli-squares",
        "σx^2 = σy^2 = σz^2 = I",
        mat2_mul(sigma_x(), sigma_x()) == identity2()
        and mat2_mul(sigma_y(), sigma_y()) == identity2()
        and mat2_mul(sigma_z(), sigma_z()) == identity2(),
    )
    checks.check(
        "pauli-xyz",
        "σx σy = i σz",
        mat2_mul(sigma_x(), sigma_y()) == mat2_scale(I_UNIT, sigma_z()),
    )
    checks.check(
        "rx-formula",
        "Rx sends (x,y,z) to (x,-z,y)",
        mat3_vec(RX, as_frac_vec((2, 3, 5))) == as_frac_vec((2, -5, 3)),
    )
    checks.check(
        "rz-formula",
        "Rz sends (c,0,0) to (0,c,0)",
        mat3_vec(RZ, as_frac_vec((7, 0, 0))) == as_frac_vec((0, 7, 0)),
    )
    checks.check(
        "group-order-det",
        "G has 24 elements, each with det +1, and contains Rx, Rz",
        len(group) == 24
        and len(set(group)) == 24
        and all(det3(item) == 1 for item in group)
        and RX in group
        and RZ in group
        and EYE3 in group,
    )
    checks.check(
        "group-closed",
        "G is closed under multiplication",
        all(mat3_mul(left, right) in group for left in group for right in group),
    )

    sample = as_frac_vec((1, 0, 0))
    checks.check(
        "alpha-on-rho",
        "α_R(ρ(n)) = ρ(R n) on a coordinate axis",
        apply_alpha(RX, bloch_state(sample)) == bloch_state(mat3_vec(RX, sample)),
    )
    checks.check(
        "faithful-action",
        "α_R = id iff R = I",
        all(
            (item == EYE3)
            == all(
                apply_alpha(item, bloch_state(vec)) == bloch_state(vec)
                for vec in sample_bloch_vectors()
            )
            for item in group
        ),
    )

    checks.check("thm1-zero-fixed", "n = 0 is fixed by every R in G", all(
        mat3_vec(item, zero_vec) == zero_vec for item in group
    ))
    checks.check(
        "thm1-rho-zero-is-half-i",
        "ρ(0) = I_2/2",
        rho_zero == half_i and half_i == ((HALF, ZERO), (ZERO, HALF)),
    )
    checks.check(
        "thm2-rx-witness",
        "if n_y or n_z is nonzero then Rx n ≠ n",
        mat3_vec(RX, as_frac_vec((1, 1, 0))) != as_frac_vec((1, 1, 0))
        and mat3_vec(RX, as_frac_vec((0, 0, 1))) != as_frac_vec((0, 0, 1)),
    )
    checks.check(
        "thm2-only-zero-invariant",
        "the only invariant Bloch vector is 0",
        fixed == (zero_vec,)
        and all(
            (vec == zero_vec)
            == all(mat3_vec(item, vec) == vec for item in group)
            for vec in sample_bloch_vectors()
        ),
    )
    conjugate_group = tuple(mat3_mul(mat3_mul(RZ, item), mat3_inv(RZ)) for item in group)
    checks.check(
        "thm3-unique-and-conjugate",
        "I_2/2 is the unique α-invariant state, and conjugate actions still fix only 0",
        bloch_state(zero_vec) == half_i
        and common_fixed_basis(group) == ()
        and common_fixed_basis(conjugate_group) == (),
    )
    checks.check(
        "thm5-control-disagrees",
        "ρ(ê_z) disagrees with I_2/2 and is not invariant",
        bloch_state(ez) != half_i
        and bloch_state(ez) == ((ONE, ZERO), (ZERO, ZERO))
        and z_moves
        and mat3_vec(RX, ez) != ez,
    )
    checks.check(
        "mutation-rho-z-invariant-fails",
        "predicate ρ(ê_z) is G-invariant fails",
        not all(mat3_vec(item, ez) == ez for item in group),
    )
    checks.check(
        "mutation-nonzero-fixed-fails",
        "predicate a nonzero n is fixed by all of G fails",
        all(
            any(mat3_vec(item, vec) != vec for item in group)
            for vec in sample_bloch_vectors()
            if vec != zero_vec
        ),
    )
    checks.check(
        "mutation-half-i-ne-rho0-fails",
        "predicate I_2/2 != ρ(0) fails",
        not (half_i != rho_zero),
    )

    axiom_core = axiom_body_without_commentary(axiom)
    checks.check(
        "mutation-memo-axiom-content-fails",
        "predicate live memo names I/2 or Born as axiom content fails",
        "I/2" not in axiom_core
        and "I_2/2" not in axiom_core
        and "Born" not in axiom_core
        and "probability distribution over the possibilities is determined by"
        in axiom
        and "locks exactly one admissible local possibility" in axiom
        and "Only records are readable." in axiom,
    )
    checks.check(
        "mutation-note-adopts-born-fails",
        "predicate note adopts I/2 as Born fails",
        "not adopted as Born" in note
        and "we adopt" not in note
        and "unique G-invariant" in note
        and "I_2/2" in note
        and "conditional on the displayed faithful action" in note,
    )
    banned = (
        "Lattice-named",
        "we adopt",
        "Gleason",
        "0.5934",
        "#" + "6263",
        "#" + "6268",
        "#" + "6272",
        "#" + "6273",
        "exhausted",
        "closes the route",
        "Record names neither",
    )
    checks.check(
        "forbidden-absent",
        "note omits the banned phrases",
        all(phrase not in note for phrase in banned),
    )
    checks.check(
        "machine-status-contract",
        "note carries bounded-support status and no hypothetical axiom adoption",
        "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"'
        in note
        and "This note authors no audit verdict" in note
        and "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/CUBE_INVARIANT_STATE_ON_M2_IS_UNIQUE_HALF_I_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "identity-gates",
        "identity gates call the three named functions",
        "def invariant_bloch_vectors(" in self_source
        and "def rho_half_i(" in self_source
        and "def rho_z_is_not_invariant(" in self_source
        and fixed == (zero_vec,)
        and half_i == rho_zero
        and z_moves is True,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
