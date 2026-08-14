#!/usr/bin/env python3
"""Exact uniqueness of cube-symmetric linear occupancy decoders on [0,1]^3.

The load-bearing classification row-reduces the full 8-weight invariance
system over Q. No coefficient grid is sampled.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "CUBE_SYMMETRIC_ADDITIVE_SOURCE_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CUBE_SYMMETRIC_ADDITIVE_SOURCE_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Vec3 = tuple[int, int, int]
Mat3 = tuple[tuple[int, ...], ...]
Occupancy = tuple[Fraction, ...]


def vertex_of_index(index: int) -> Vec3:
    return (index & 1, (index >> 1) & 1, (index >> 2) & 1)


def index_of_vertex(vertex: Vec3) -> int:
    return vertex[0] + 2 * vertex[1] + 4 * vertex[2]


VERTICES: tuple[Vec3, ...] = tuple(vertex_of_index(index) for index in range(8))


def proper_signed_permutations() -> tuple[Mat3, ...]:
    """The 24 determinant-+1 signed permutation matrices."""
    matrices: list[Mat3] = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            for row, column in enumerate(perm):
                matrix[row][column] = signs[row]
            inversion_sign = 1
            items = list(perm)
            for left in range(3):
                for right in range(left + 1, 3):
                    if items[left] > items[right]:
                        inversion_sign = -inversion_sign
            if inversion_sign * signs[0] * signs[1] * signs[2] == 1:
                matrices.append(tuple(tuple(row) for row in matrix))
    return tuple(matrices)


ROTATIONS = proper_signed_permutations()


def mat_mul(left: Mat3, right: Mat3) -> Mat3:
    return tuple(
        tuple(
            left[row][0] * right[0][col]
            + left[row][1] * right[1][col]
            + left[row][2] * right[2][col]
            for col in range(3)
        )
        for row in range(3)
    )


def mat_transpose(matrix: Mat3) -> Mat3:
    return tuple(tuple(matrix[row][col] for row in range(3)) for col in range(3))


def rotate_vertex(matrix: Mat3, vertex: Vec3) -> Vec3:
    """Apply x |-> c + P(x - c) with integer 0/1 arithmetic."""
    result = [0, 0, 0]
    for row in range(3):
        for col in range(3):
            entry = matrix[row][col]
            if entry == 1:
                result[row] = vertex[col]
            elif entry == -1:
                result[row] = 1 - vertex[col]
    return (result[0], result[1], result[2])


def rotate_occupancy(matrix: Mat3, occupancy: Occupancy) -> Occupancy:
    """Return o ∘ R^{-1} for R(x) = c + P(x - c)."""
    inverse = mat_transpose(matrix)
    moved = [Fraction(0)] * 8
    for index, vertex in enumerate(VERTICES):
        source = rotate_vertex(inverse, vertex)
        moved[index] = occupancy[index_of_vertex(source)]
    return tuple(moved)


def rho(occupancy: Occupancy) -> Fraction:
    return sum(occupancy, Fraction(0))


def weighted(occupancy: Occupancy, weights: Occupancy) -> Fraction:
    return sum(
        (weight * value for weight, value in zip(weights, occupancy)),
        Fraction(0),
    )


def basis_occupancy(index: int) -> Occupancy:
    return tuple(Fraction(int(item == index)) for item in range(8))


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


def invariance_system() -> list[list[Fraction]]:
    """Stack (P_R^T - I) for the 8-dimensional occupancy action of each R."""
    constraints: list[list[Fraction]] = []
    for matrix in ROTATIONS:
        perm = [[Fraction(0) for _ in range(8)] for _ in range(8)]
        inverse = mat_transpose(matrix)
        for index, vertex in enumerate(VERTICES):
            source = rotate_vertex(inverse, vertex)
            perm[index][index_of_vertex(source)] = Fraction(1)
        # Columns of perm are images of basis vectors under o |-> o ∘ R^{-1}.
        # Invariance: perm^T w = w.
        for row in range(8):
            constraint = [perm[col][row] for col in range(8)]
            constraint[row] -= Fraction(1)
            constraints.append(constraint)
    return constraints


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

    print("external_scientific_inputs: none; exact eight-vertex cube algebra only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact Fraction coefficients; no floating-point inputs")
    print("claim_boundary: bounded algebraic result; no physical identification is asserted")

    identity = (
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
    )
    checks.check(
        "thm1-group-order",
        "exactly 24 distinct proper signed permutation matrices",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24 and identity in ROTATIONS,
    )

    products = {mat_mul(left, right) for left in ROTATIONS for right in ROTATIONS}
    inverses_present = all(mat_mul(matrix, mat_transpose(matrix)) == identity for matrix in ROTATIONS)
    checks.check(
        "thm1-group-laws",
        "the 24 matrices are closed, contain inverses, and include the identity",
        products == set(ROTATIONS) and inverses_present,
    )

    preserves_vertices = all(
        rotate_vertex(matrix, vertex) in VERTICES
        for matrix in ROTATIONS
        for vertex in VERTICES
    )
    checks.check(
        "thm1-preserves-V",
        "every proper cube rotation permutes the eight vertices",
        preserves_vertices,
    )

    origin = (0, 0, 0)
    orbit = {rotate_vertex(matrix, origin) for matrix in ROTATIONS}
    checks.check(
        "thm1-one-orbit",
        "the eight vertices form one orbit under the cube group",
        orbit == set(VERTICES),
    )

    generic = (
        Fraction(1),
        Fraction(0),
        Fraction(1),
        Fraction(0),
        Fraction(0),
        Fraction(1),
        Fraction(1),
        Fraction(0),
    )
    generic_images = [rotate_occupancy(matrix, generic) for matrix in ROTATIONS]
    checks.check(
        "thm4-rho-generic",
        "rho is invariant on (1,0,1,0,0,1,1,0) under every cube rotation",
        all(rho(image) == rho(generic) == Fraction(4) for image in generic_images),
    )

    singles = [basis_occupancy(index) for index in range(8)]
    checks.check(
        "thm2-single-site-rho",
        "every single-site occupancy has rho = 1",
        all(rho(item) == Fraction(1) for item in singles),
    )

    system = invariance_system()
    reduced = row_reduce(system)
    kernel = nullspace(system, 8)
    ones = tuple(Fraction(1) for _ in range(8))
    checks.check(
        "thm3-system-rank",
        "the 8-weight invariance system has exact rank 7",
        len(reduced) == 7,
    )
    checks.check(
        "thm3-kernel-span-rho",
        "the invariance kernel is one-dimensional and spans the vertex sum",
        len(kernel) == 1 and kernel[0] == ones,
    )

    equal_basis_values = all(
        weighted(basis_occupancy(index), ones) == Fraction(1) for index in range(8)
    )
    checks.check(
        "thm2-equal-basis-values",
        "an invariant linear decoder takes the same value on every e_v",
        equal_basis_values,
    )

    mutant_weights = (Fraction(2),) + tuple(Fraction(1) for _ in range(7))
    mutant_fails = any(
        weighted(rotate_occupancy(matrix, singles[0]), mutant_weights)
        != weighted(singles[0], mutant_weights)
        for matrix in ROTATIONS
    )
    checks.check(
        "mutation-double-weight-fails",
        "weighting one vertex by 2 breaks cube-symmetry",
        mutant_fails and weighted(singles[0], mutant_weights) == Fraction(2),
    )

    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE", "we adopt", "Codex", "L_phys")
    checks.check(
        "hygiene-forbidden-substrings",
        "the note avoids the forbidden substrings",
        all(item not in note for item in forbidden),
    )
    checks.check(
        "scope-boundary",
        "the theorem disclaims a physical source law and any axiom edit",
        "No physical source identification" in note
        and "not a fifth extra" in note
        and "no additional axiom is proposed" in note
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
            "docs/CUBE_SYMMETRIC_ADDITIVE_SOURCE_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "claim-type-and-proof-contract",
        "the bounded type and universal proof obligation are source-visible",
        "**Type:** bounded_theorem" in note
        and "row-reduces the complete 8-weight invariance system" in note
        and "### N8" not in note
        and "FAIL / DO NOT SHIP" not in note
        and ("import " + "qcd") not in self_source.lower()
        and ("from " + "qcd") not in self_source.lower(),
    )
    checks.check(
        "live-lattice-quote",
        "the live Lattice sentences are quoted without rewrite",
        "Physical sites are the points of the cubic lattice `Z^3`" in axiom
        and "Physical sites are the points of the cubic lattice `Z^3`" in note
        and "No site is privileged. Sites are distinguished by the supplied lattice"
        in axiom
        and "No site is privileged. Sites are distinguished by the supplied lattice"
        in note
        and "They are not renamed after Lattice." in note,
    )
    checks.check(
        "live-record-quote",
        "the live Record lock and content sentences are quoted without rewrite",
        "When present, a record locks exactly one admissible local possibility."
        in axiom
        and "When present, a record locks exactly one admissible local possibility."
        in note
        and "A readout value is determined by record content" in axiom
        and "A readout value is determined by record content" in note,
    )
    checks.check(
        "qubit-unflipped",
        "the note does not rewrite the live Qubit presentation",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom
        and "changes the Qubit statement" in note
        and "M_2(R)" not in note
        and "we replace Qubit" not in note,
    )

    print("per_element: exact identities cover all eight vertices and all 24 rotations.")
    print("per_site: the theorem is evaluated only on the displayed cube A=[0,1]^3.")
    print("per_mode: linear cube-symmetric decoders are classified; nonlinear maps are out of scope.")
    print("per_block: all 8 rational weights are constrained; the kernel is span_Q{rho}.")
    print(
        "lattice_wide: checked and not executed — the claim asserts no lattice-wide lift."
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
