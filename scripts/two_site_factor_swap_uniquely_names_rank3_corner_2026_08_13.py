#!/usr/bin/env python3
"""Exact checks for the two-site factor-swap and its rank-3 projector.

The load-bearing classification row-reduces the full 16-real-coordinate
space of complex-Hermitian 4x4 matrices. No coefficient grid is sampled.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_SITE_FACTOR_SWAP_UNIQUELY_NAMES_RANK3_CORNER_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_SITE_FACTOR_SWAP_UNIQUELY_NAMES_RANK3_CORNER_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, ...], ...]
HermitianPair = tuple[Matrix, Matrix]


def zero(n: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(n)) for _ in range(n))


def eye(n: int) -> Matrix:
    return tuple(
        tuple(Fraction(int(row == col)) for col in range(n)) for row in range(n)
    )


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][col] + right[row][col] for col in range(len(left)))
        for row in range(len(left))
    )


def scale(scalar: Fraction, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(scalar * matrix[row][col] for col in range(len(matrix)))
        for row in range(len(matrix))
    )


def mul(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return tuple(
        tuple(
            sum(
                (left[row][mid] * right[mid][col] for mid in range(size)),
                Fraction(0),
            )
            for col in range(size)
        )
        for row in range(size)
    )


def adj_real(matrix: Matrix) -> Matrix:
    size = len(matrix)
    return tuple(tuple(matrix[col][row] for col in range(size)) for row in range(size))


def trace(matrix: Matrix) -> Fraction:
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def rank(matrix: Matrix) -> int:
    return len(row_reduce([list(row) for row in matrix]))


def kron(left: Matrix, right: Matrix) -> Matrix:
    a, b = len(left), len(right)
    return tuple(
        tuple(
            left[i // b][j // b] * right[i % b][j % b]
            for j in range(a * b)
        )
        for i in range(a * b)
    )


def e_unit(n: int, row: int, col: int) -> Matrix:
    data = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    data[row][col] = Fraction(1)
    return tuple(tuple(item) for item in data)


def factor_swap() -> Matrix:
    return (
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    )


def apply_to_basis(matrix: Matrix, index: int) -> tuple[Fraction, ...]:
    return tuple(matrix[row][index] for row in range(len(matrix)))


def row_reduce(rows: list[list[Fraction]]) -> list[list[Fraction]]:
    """Return nonzero rows of the exact reduced row-echelon form."""
    if not rows:
        return []
    n_rows = len(rows)
    n_cols = len(rows[0])
    mat = [list(row) for row in rows]
    pivot_row = 0
    for col in range(n_cols):
        pivot = next(
            (row for row in range(pivot_row, n_rows) if mat[row][col] != 0),
            None,
        )
        if pivot is None:
            continue
        mat[pivot_row], mat[pivot] = mat[pivot], mat[pivot_row]
        pivot_value = mat[pivot_row][col]
        mat[pivot_row] = [entry / pivot_value for entry in mat[pivot_row]]
        for row in range(n_rows):
            if row == pivot_row or mat[row][col] == 0:
                continue
            factor = mat[row][col]
            mat[row] = [
                mat[row][j] - factor * mat[pivot_row][j] for j in range(n_cols)
            ]
        pivot_row += 1
        if pivot_row == n_rows:
            break
    return [row for row in mat if any(entry != 0 for entry in row)]


def nullspace(rows: list[list[Fraction]], n_cols: int) -> list[tuple[Fraction, ...]]:
    """Exact basis for the nullspace of a rational coefficient matrix."""
    reduced = row_reduce(rows)
    pivots: dict[int, list[Fraction]] = {}
    for row in reduced:
        pivot = next(index for index, value in enumerate(row) if value != 0)
        pivots[pivot] = row
    free_columns = [column for column in range(n_cols) if column not in pivots]
    basis: list[tuple[Fraction, ...]] = []
    for free in free_columns:
        vector = [Fraction(0)] * n_cols
        vector[free] = Fraction(1)
        for pivot, row in pivots.items():
            vector[pivot] = -row[free]
        basis.append(tuple(vector))
    return basis


def complex_hermitian_basis() -> list[HermitianPair]:
    """A 16-real-coordinate basis represented as (real part, imaginary part)."""
    z4 = zero(4)
    basis: list[HermitianPair] = []
    for index in range(4):
        basis.append((e_unit(4, index, index), z4))
    for row in range(4):
        for col in range(row + 1, 4):
            symmetric = add(e_unit(4, row, col), e_unit(4, col, row))
            antisymmetric = add(
                e_unit(4, row, col), scale(Fraction(-1), e_unit(4, col, row))
            )
            basis.append((symmetric, z4))
            basis.append((z4, antisymmetric))
    return basis


def combine_hermitian(
    coordinates: tuple[Fraction, ...], basis: list[HermitianPair]
) -> HermitianPair:
    real = zero(4)
    imaginary = zero(4)
    for coefficient, (basis_real, basis_imaginary) in zip(coordinates, basis):
        real = add(real, scale(coefficient, basis_real))
        imaginary = add(imaginary, scale(coefficient, basis_imaginary))
    return real, imaginary


def hermitian_intertwining_kernel() -> tuple[int, list[HermitianPair]]:
    """Solve the two intertwining relations on every complex-Hermitian U."""
    i2 = eye(2)
    generators = (e_unit(2, 0, 0), e_unit(2, 0, 1))
    basis = complex_hermitian_basis()
    constraints: list[list[Fraction]] = []

    for generator in generators:
        left_operator = kron(generator, i2)
        right_operator = kron(i2, generator)
        residuals: list[HermitianPair] = []
        for basis_real, basis_imaginary in basis:
            residual_real = add(
                mul(basis_real, left_operator),
                scale(Fraction(-1), mul(right_operator, basis_real)),
            )
            residual_imaginary = add(
                mul(basis_imaginary, left_operator),
                scale(Fraction(-1), mul(right_operator, basis_imaginary)),
            )
            residuals.append((residual_real, residual_imaginary))

        for component in (0, 1):
            for row in range(4):
                for col in range(4):
                    constraints.append(
                        [residual[component][row][col] for residual in residuals]
                    )

    reduced_rank = len(row_reduce(constraints))
    coordinate_basis = nullspace(constraints, len(basis))
    return reduced_rank, [combine_hermitian(vector, basis) for vector in coordinate_basis]


def is_nonzero_real_multiple(matrix_pair: HermitianPair, target: Matrix) -> bool:
    """Whether a complex matrix pair is a nonzero real multiple of target."""
    real, imaginary = matrix_pair
    if imaginary != zero(4):
        return False
    scalar: Fraction | None = None
    for row in range(4):
        for col in range(4):
            if target[row][col] != 0:
                candidate = real[row][col] / target[row][col]
                scalar = candidate if scalar is None else scalar
                if candidate != scalar:
                    return False
            elif real[row][col] != 0:
                return False
    return scalar is not None and scalar != 0


def implements_generators(matrix: Matrix) -> bool:
    i2 = eye(2)
    for generator in (e_unit(2, 0, 0), e_unit(2, 0, 1)):
        left = kron(generator, i2)
        right = kron(i2, generator)
        if mul(matrix, left) != mul(right, matrix):
            return False
    return True


def polynomial_multiply(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    """Multiply coefficient tuples ordered from constant term upward."""
    product = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            product[left_degree + right_degree] += (
                left_coefficient * right_coefficient
            )
    return tuple(product)


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

    print("external_scientific_inputs: none; exact two-site matrix algebra only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact Fraction coefficients; no floating-point inputs")
    print("claim_boundary: bounded algebraic result; no physical identification is asserted")

    f = factor_swap()
    minus_f = scale(Fraction(-1), f)
    twice_f = scale(Fraction(2), f)
    i4 = eye(4)
    i2 = eye(2)
    p_plus = scale(Fraction(1, 2), add(i4, f))
    p_minus = scale(Fraction(1, 2), add(i4, minus_f))

    checks.check("thm1-hermitian", "F^* = F", adj_real(f) == f)
    checks.check("thm1-involution", "F^2 = I_4", mul(f, f) == i4)
    checks.check("thm1-trace", "Tr(F) = 2", trace(f) == Fraction(2))

    matrix_units = tuple(e_unit(2, row, col) for row in range(2) for col in range(2))
    factor_exchange = all(
        mul(mul(f, kron(unit, i2)), f) == kron(i2, unit)
        and mul(mul(f, kron(i2, unit)), f) == kron(unit, i2)
        for unit in matrix_units
    )
    checks.check(
        "thm2-ad-exchanges",
        "Ad_F exchanges both factors on all four matrix units",
        factor_exchange,
    )

    images = {
        0: (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        1: (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
        2: (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        3: (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    }
    checks.check(
        "thm3-basis-images",
        "the four product-basis images are exactly the factor-swap columns",
        all(apply_to_basis(f, index) == images[index] for index in range(4)),
    )

    kernel_rank, kernel_basis = hermitian_intertwining_kernel()
    checks.check(
        "thm4-hermitian-system-rank",
        "the 16-real-coordinate intertwining system has exact rank 15",
        kernel_rank == 15,
    )
    checks.check(
        "thm4-hermitian-kernel",
        "the full complex-Hermitian kernel is one-dimensional and spans F",
        len(kernel_basis) == 1 and is_nonzero_real_multiple(kernel_basis[0], f),
    )
    checks.check(
        "thm4-both-signs-implement",
        "both F and -F satisfy the two generator intertwining equations",
        implements_generators(f) and implements_generators(minus_f),
    )
    checks.check(
        "thm4-scalar-involution-roots",
        "t^2-1 factors exactly as (t-1)(t+1), so its real roots are +/-1",
        mul(f, f) == i4
        and polynomial_multiply(
            (Fraction(-1), Fraction(1)),
            (Fraction(1), Fraction(1)),
        )
        == (Fraction(-1), Fraction(0), Fraction(1)),
    )
    checks.check(
        "mutation-two-f-involution-fails",
        "the non-root scalar mutation U=2F does not satisfy U^2=I",
        mul(twice_f, twice_f) != i4,
    )
    checks.check(
        "mutation-f-eq-minus-f-fails",
        "F and -F are distinguished by exact trace",
        f != minus_f and trace(f) == -trace(minus_f),
    )

    checks.check(
        "thm5-pplus-proj",
        "p_+^2 = p_+ = p_+^*",
        mul(p_plus, p_plus) == p_plus and adj_real(p_plus) == p_plus,
    )
    checks.check(
        "thm5-pminus-proj",
        "p_-^2 = p_- = p_-^*",
        mul(p_minus, p_minus) == p_minus and adj_real(p_minus) == p_minus,
    )
    checks.check("thm5-rank-pplus", "rank(p_+) = 3", rank(p_plus) == 3)
    checks.check("thm5-rank-pminus", "rank(p_-) = 1", rank(p_minus) == 1)
    checks.check(
        "thm5-complementary",
        "p_+ + p_- = I_4 and p_+ p_- = 0",
        add(p_plus, p_minus) == i4 and mul(p_plus, p_minus) == zero(4),
    )
    checks.check(
        "mutation-rank-pplus-eq-1-fails",
        "the rank-1 mutation is rejected",
        rank(p_plus) != 1,
    )
    checks.check(
        "mutation-pplus-eq-i4-fails",
        "the full-unit mutation is rejected",
        p_plus != i4,
    )

    checks.check(
        "scope-boundary",
        "the theorem disclaims a physical interpretation and any axiom edit",
        "No physical two-site composition rule" in note
        and "no additional\naxiom is proposed" in note
        and "These are scope boundaries, not impossibility" in note,
    )
    checks.check(
        "machine-status-contract",
        "bounded status, frontier trace, and next action are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "trace_class: frontier_discovery" in note
        and 'next_trace_action: "independent audit of the bounded algebraic claim"'
        in note,
    )
    checks.check(
        "import-boundary-contract",
        "the supplied host and absent physical bridge are disclosed",
        "## Inputs And Import Boundary" in note
        and "Explicit theorem-domain condition" in note
        and "External empirical or literature inputs:** none" in note
        and "Open physical bridge" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_SITE_FACTOR_SWAP_UNIQUELY_NAMES_RANK3_CORNER_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "claim-type-and-proof-contract",
        "the bounded type and universal proof obligation are source-visible",
        "**Type:** bounded_theorem" in note
        and "all 16 real coordinates" in note
        and "rank 15 and nullspace" in note
        and "not merely rational matrices or\na finite coefficient grid" in note
        and "### N8" not in note
        and "FAIL / DO NOT SHIP" not in note
        and ("import " + "qcd") not in self_source.lower()
        and ("from " + "qcd") not in self_source.lower(),
    )
    checks.check(
        "live-record-unread",
        "the live Record unread sentence is quoted without rewrite",
        "A site with no record cannot be read." in axiom
        and "A site with no record cannot be read." in note,
    )

    print(
        "per_element: exact identities cover F, -F, p_+, p_-, and all four matrix units."
    )
    print(
        "per_site: the theorem is evaluated only on the supplied two-site host H=C^2 tensor C^2."
    )
    print(
        "per_mode: both swap eigenspaces and their complementary spectral projectors are resolved exactly."
    )
    print(
        "per_block: all 16 real coordinates of a complex-Hermitian 4x4 matrix are constrained; the kernel is span_R{F}."
    )
    print(
        "lattice_wide: checked and not executed — the claim asserts no multi-site or lattice-wide lift."
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
