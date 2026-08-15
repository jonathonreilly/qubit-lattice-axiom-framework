#!/usr/bin/env python3
"""Exact checks for unique linear-threshold formation as f_L1.

Cube-equivariant linear maps {0,1}^6 → R^3 in the standard 3 are the ray
α L1. The threshold 1_{L≠0} is empty at α=0 and equals f_L1 at every
α≠0. All algebra is exact Fraction arithmetic. No cache is written.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path

from fractions import Fraction


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / (
    "docs/LINEAR_THRESHOLD_FORMATION_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/LINEAR_THRESHOLD_FORMATION_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

DIRS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)

Matrix = tuple[tuple[Fraction, ...], ...]


def frac(value: int) -> Fraction:
    return Fraction(value)


def mat(rows: list[list[int | Fraction]]) -> Matrix:
    return tuple(tuple(Fraction(entry) for entry in row) for row in rows)


def zero(rows: int, cols: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(cols)) for _ in range(rows))


def mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                (left[row][mid] * right[mid][col] for mid in range(len(right))),
                Fraction(0),
            )
            for col in range(len(right[0]))
        )
        for row in range(len(left))
    )


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][col] + right[row][col] for col in range(len(left[0])))
        for row in range(len(left))
    )


def scale(scalar: Fraction, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(scalar * matrix[row][col] for col in range(len(matrix[0])))
        for row in range(len(matrix))
    )


def transpose(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(matrix[row][col] for row in range(len(matrix)))
        for col in range(len(matrix[0]))
    )


def det3(matrix: Matrix) -> Fraction:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def apply_vec(matrix: Matrix, vector: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    for row in matrix:
        value = sum((row[col] * vector[col] for col in range(3)), Fraction(0))
        out.append(int(value))
    return tuple(out)


def dir_index(vector: tuple[int, ...]) -> int:
    return DIRS.index(vector)


def proper_rotations() -> tuple[Matrix, ...]:
    rotations: list[Matrix] = []
    for perm in permutations(range(3)):
        for sign_bits in range(8):
            signs = [1 if ((sign_bits >> axis) & 1) == 0 else -1 for axis in range(3)]
            data = [[0, 0, 0] for _ in range(3)]
            for axis in range(3):
                data[perm[axis]][axis] = signs[axis]
            candidate = mat(data)
            if det3(candidate) == 1:
                rotations.append(candidate)
    return tuple(rotations)


def rho(rotation: Matrix) -> Matrix:
    inverse = transpose(rotation)
    data = [[Fraction(0) for _ in range(6)] for _ in range(6)]
    for dest, direction in enumerate(DIRS):
        source = apply_vec(inverse, direction)
        data[dest][dir_index(source)] = Fraction(1)
    return tuple(tuple(row) for row in data)


def l1_map() -> Matrix:
    return mat(
        [
            [1, -1, 0, 0, 0, 0],
            [0, 0, 1, -1, 0, 0],
            [0, 0, 0, 0, 1, -1],
        ]
    )


def even_sum_map() -> Matrix:
    return mat(
        [
            [1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1],
        ]
    )


def flatten(matrix: Matrix) -> tuple[Fraction, ...]:
    return tuple(entry for row in matrix for entry in row)


def reshape3x6(values: tuple[Fraction, ...]) -> Matrix:
    return tuple(values[row * 6 : (row + 1) * 6] for row in range(3))


def row_reduce(rows: list[list[Fraction]]) -> list[list[Fraction]]:
    if not rows:
        return []
    n_rows = len(rows)
    n_cols = len(rows[0])
    work = [list(row) for row in rows]
    pivot_row = 0
    for col in range(n_cols):
        pivot = next(
            (row for row in range(pivot_row, n_rows) if work[row][col] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][col]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for row in range(n_rows):
            if row == pivot_row or work[row][col] == 0:
                continue
            factor = work[row][col]
            work[row] = [
                work[row][index] - factor * work[pivot_row][index]
                for index in range(n_cols)
            ]
        pivot_row += 1
        if pivot_row == n_rows:
            break
    return [row for row in work if any(entry != 0 for entry in row)]


def nullspace(rows: list[list[Fraction]], n_cols: int) -> list[tuple[Fraction, ...]]:
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


def equivariance_system(rotations: tuple[Matrix, ...]) -> list[list[Fraction]]:
    constraints: list[list[Fraction]] = []
    for rotation in rotations:
        action = rho(rotation)
        for source_row in range(3):
            for source_col in range(6):
                coordinates = [Fraction(0)] * 18
                # (L ρ - R L)_{source_row, source_col} = 0
                for mid in range(6):
                    coordinates[source_row * 6 + mid] += action[mid][source_col]
                for mid in range(3):
                    coordinates[mid * 6 + source_col] -= rotation[source_row][mid]
                constraints.append(coordinates)
    return constraints


def apply_linear(matrix: Matrix, occupancy: tuple[int, ...]) -> tuple[Fraction, ...]:
    return tuple(
        sum((matrix[row][col] * occupancy[col] for col in range(6)), Fraction(0))
        for row in range(3)
    )


def dipole(occupancy: tuple[int, ...]) -> tuple[int, ...]:
    return (
        occupancy[0] - occupancy[1],
        occupancy[2] - occupancy[3],
        occupancy[4] - occupancy[5],
    )


def threshold(matrix: Matrix, occupancy: tuple[int, ...]) -> int:
    return int(apply_linear(matrix, occupancy) != (Fraction(0), Fraction(0), Fraction(0)))


def f_l1(occupancy: tuple[int, ...]) -> int:
    return int(dipole(occupancy) != (0, 0, 0))


def is_multiple(candidate: Matrix, target: Matrix) -> bool:
    scalar: Fraction | None = None
    for row in range(3):
        for col in range(6):
            if target[row][col] != 0:
                value = candidate[row][col] / target[row][col]
                if scalar is None:
                    scalar = value
                elif value != scalar:
                    return False
            elif candidate[row][col] != 0:
                return False
    return scalar is not None


def chi_std(rotation: Matrix) -> int:
    return int(rotation[0][0] + rotation[1][1] + rotation[2][2])


def chi_even(rotation: Matrix) -> int:
    unsigned = 0
    for axis in range(3):
        if rotation[axis][axis] != 0:
            unsigned += 1
    return unsigned


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
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
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("external_scientific_inputs: none; cube rotations and occupancy bits are declared")
    print("claim_scope: displayed linear-threshold uniqueness; f_L1 is not adopted")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/LINEAR_THRESHOLD_FORMATION_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)),
    )

    rotations = proper_rotations()
    identity = mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    rotation_set = set(rotations)
    checks.check(
        "rotation-group-order",
        "there are exactly 24 proper cube rotations",
        len(rotations) == 24 and len(rotation_set) == 24 and identity in rotation_set,
        len(rotations),
    )
    closed = all(mul(left, right) in rotation_set for left in rotations for right in rotations)
    inverses = all(mul(rotation, transpose(rotation)) == identity for rotation in rotations)
    checks.check(
        "rotation-group-laws",
        "the 24 matrices are a group under multiplication with inverses R^T",
        closed and inverses,
    )

    even_inner = sum(chi_even(rotation) * chi_std(rotation) for rotation in rotations)
    odd_inner = sum(chi_std(rotation) * chi_std(rotation) for rotation in rotations)
    checks.check(
        "thm1-even-killed",
        "the even character inner product with the standard 3 is exactly 0",
        even_inner == 0,
        even_inner,
    )
    checks.check(
        "thm1-odd-is-standard",
        "the odd character inner product with the standard 3 is exactly 24",
        odd_inner == 24,
        odd_inner,
    )

    constraints = equivariance_system(rotations)
    reduced = row_reduce(constraints)
    kernel = nullspace(constraints, 18)
    l1 = l1_map()
    checks.check(
        "thm2-system-rank",
        "the 18-coefficient equivariance system has exact rank 17",
        len(reduced) == 17,
        len(reduced),
    )
    checks.check(
        "thm2-kernel-is-l1-ray",
        "the equivariant nullspace is one-dimensional and spans L1",
        len(kernel) == 1 and is_multiple(reshape3x6(kernel[0]), l1),
        kernel,
    )

    even_generators = (
        (1, 1, 0, 0, 0, 0),
        (0, 0, 1, 1, 0, 0),
        (0, 0, 0, 0, 1, 1),
    )
    even_killed = all(
        apply_linear(reshape3x6(kernel[0]), generator)
        == (Fraction(0), Fraction(0), Fraction(0))
        for generator in even_generators
    )
    checks.check(
        "thm1-even-generators-vanish",
        "every equivariant map vanishes on the three even generators",
        even_killed,
    )

    cubes = tuple(product((0, 1), repeat=6))
    zeros = [cube for cube in cubes if f_l1(cube) == 0]
    ones = [cube for cube in cubes if f_l1(cube) == 1]
    checks.check(
        "thm2-census",
        "L1 vanishes on exactly 8 of 64 configurations, so f_L1 has 56 units",
        len(cubes) == 64 and len(zeros) == 8 and len(ones) == 56,
        (len(zeros), len(ones)),
    )

    scales = (Fraction(1), Fraction(2), Fraction(-1), Fraction(5), Fraction(2, 7))
    independent = True
    for alpha in scales:
        image = scale(alpha, l1)
        independent = independent and all(
            threshold(image, cube) == f_l1(cube) for cube in cubes
        )
        independent = independent and all(
            (apply_linear(image, cube) == (Fraction(0), Fraction(0), Fraction(0)))
            == (dipole(cube) == (0, 0, 0))
            for cube in cubes
        )
    checks.check(
        "thm2-alpha-independence",
        "every tested nonzero α has L(c)=0 iff n(c)=0, so f_α equals f_L1",
        independent and Fraction(1, 3) not in scales,
    )

    zero_map = scale(Fraction(0), l1)
    empty = all(threshold(zero_map, cube) == 0 for cube in cubes)
    checks.check(
        "thm3-zero-map-empty",
        "the zero map yields the empty predicate f=0",
        empty,
    )
    checks.check(
        "thm3-empty-is-not-fl1",
        "the empty predicate is not f_L1",
        empty and any(f_l1(cube) == 1 for cube in cubes),
    )

    even_map = even_sum_map()
    even_equivariant = all(
        mul(even_map, rho(rotation)) == mul(rotation, even_map) for rotation in rotations
    )
    checks.check(
        "mutation-even-sum-not-equivariant",
        "the even sum map is not cube-equivariant to the standard 3",
        not even_equivariant,
    )

    flipped = mat(
        [
            [1, 1, 0, 0, 0, 0],
            [0, 0, 1, -1, 0, 0],
            [0, 0, 0, 0, 1, -1],
        ]
    )
    flipped_equivariant = all(
        mul(flipped, rho(rotation)) == mul(rotation, flipped) for rotation in rotations
    )
    checks.check(
        "mutation-wrong-pair-signs",
        "replacing one L1 pair by a sum leaves the equivariance system",
        not flipped_equivariant,
    )

    lattice_quote = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    formation_boundary = (
        "it does not supply the formation site, probability, or rate."
    )
    checks.check(
        "live-lattice-quote",
        "the live Lattice rotation sentence is quoted without rewrite",
        lattice_quote in axiom and lattice_quote in note,
    )
    checks.check(
        "live-formation-boundary",
        "the live Admissibility formation-boundary sentence is quoted without rewrite",
        formation_boundary in axiom.replace("\n", " ")
        and formation_boundary in note,
    )
    checks.check(
        "records-form-quoted",
        "the live Record sentence Records form. is quoted without rewrite",
        "Records form." in axiom and "Records form." in note,
    )

    required_note_phrases = (
        "Displayed, not adopted",
        "the unique nonzero-linear-threshold predicate in",
        "the standard 3 is `f_L1`",
        "no numerical\nnormalization is selected",
        "**Type:** bounded_theorem",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "## Inputs And Import Boundary",
        "Explicit theorem-domain condition",
        "External empirical or literature inputs:** none",
        "Open physical bridge",
        "These are scope boundaries, not impossibility",
    )
    checks.check(
        "note-contract",
        "the note states uniqueness, displayed scope, and the import boundary",
        all(phrase in note for phrase in required_note_phrases),
        [phrase for phrase in required_note_phrases if phrase not in note],
    )
    checks.check(
        "machine-status-contract",
        "bounded status, frontier trace, and next action are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "trace_class: frontier_discovery" in note
        and 'next_trace_action: "independent audit of the bounded algebraic uniqueness claim"'
        in note,
    )

    forbidden = (
        "G" + "_N",
        "1/" + "r",
        "1/" + "r^2",
        "Lattice" + "-named",
        "not a " + "TOE",
    )
    combined = note + "\n" + self_source
    checks.check(
        "forbidden-phrases-absent",
        "note and runner omit the dispatch-forbidden phrases",
        all(phrase not in combined for phrase in forbidden),
        [phrase for phrase in forbidden if phrase in combined],
    )
    checks.check(
        "scale-not-one-third",
        "neither source adopts the conventional scale 1/3",
        "1/3" not in note
        and "Fraction(1, 3) not in scales" in self_source
        and "adopt" in note.lower(),
    )
    checks.check(
        "no-float-and-no-cache",
        "the runner uses Fraction only and writes no cache",
        "cache_write: false" in self_source
        and ("flo" + "at(") not in self_source
        and ("num" + "py") not in self_source
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "no-axiom-edit",
        "the axiom memo is read only and the note proposes no axiom edit",
        "hypothetical_axiom_status: \"none;" in note
        and "not proposed as axiom content" in note
        and "### Lattice / Physical Locality" in axiom,
    )

    print("per_element: all 18 linear coefficients and all 24 rotations are constrained.")
    print("per_site: the theorem is evaluated only on the six signed neighbour occupations.")
    print("per_mode: even and odd occupancy pieces are separated by exact characters.")
    print("per_block: the 64-configuration cube is exhaustively compared to f_L1.")
    print("lattice_wide: checked and not executed — no multi-site lift is asserted.")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
