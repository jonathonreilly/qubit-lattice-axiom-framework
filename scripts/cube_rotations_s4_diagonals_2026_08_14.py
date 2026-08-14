#!/usr/bin/env python3
"""Exact Z checks: det=+1 signed permutation matrices act as S_4 on space diagonals."""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "CUBE_ROTATIONS_S4_DIAGONALS_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CUBE_ROTATIONS_S4_DIAGONALS_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, int, int]
Perm = tuple[int, int, int, int]

I3: Matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
MINUS_I3: Matrix = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))

# Representative vertices, one on each space diagonal.
DIAG_REPS: tuple[Vector, ...] = (
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, 1),
    (1, -1, -1),
)

LATTICE_QUOTE = (
    "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor\n"
    "adjacency, standard translations, and proper cubic rotations about each site."
)
QUBIT_QUOTE = (
    "The full one-site possibility domain has algebraic presentation `M_2(C)`."
)

FORBIDDEN_NOTE_SUBSTRINGS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "exhausted",
    "only route",
    "we adopt",
    "Codex",
    "L_phys",
)


def det3(matrix: Matrix) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][0] * right[0][col]
            + left[row][1] * right[1][col]
            + left[row][2] * right[2][col]
            for col in range(3)
        )
        for row in range(3)
    )


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][col] for row in range(3)) for col in range(3))


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2],
        matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2],
    )


def sign_of_perm(perm: tuple[int, ...]) -> int:
    inversions = 0
    for left in range(len(perm)):
        for right in range(left + 1, len(perm)):
            if perm[left] > perm[right]:
                inversions += 1
    return 1 if inversions % 2 == 0 else -1


def signed_perm_matrix(axis_perm: tuple[int, int, int], signs: tuple[int, int, int]) -> Matrix:
    """Column j is signs[j] * e_{axis_perm[j]}."""
    rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for column, (row, sign) in enumerate(zip(axis_perm, signs)):
        rows[row][column] = sign
    return (tuple(rows[0]), tuple(rows[1]), tuple(rows[2]))


def is_signed_permutation(matrix: Matrix) -> bool:
    for row in matrix:
        if sum(abs(entry) for entry in row) != 1:
            return False
        if any(entry not in (-1, 0, 1) for entry in row):
            return False
    for col in range(3):
        if sum(abs(matrix[row][col]) for row in range(3)) != 1:
            return False
    return True


def enumerate_G() -> tuple[Matrix, ...]:
    elements: list[Matrix] = []
    for axis_perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = signed_perm_matrix(axis_perm, signs)
            if det3(matrix) == 1:
                elements.append(matrix)
    return tuple(elements)


def count_by_sign_rule() -> int:
    count = 0
    for axis_perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if sign_of_perm(axis_perm) * signs[0] * signs[1] * signs[2] == 1:
                count += 1
    return count


def rotation_90_about_x() -> Matrix:
    # e0 -> e0, e1 -> e2, e2 -> -e1
    return ((1, 0, 0), (0, 0, -1), (0, 1, 0))


def rotation_120_about_111() -> Matrix:
    # e0 -> e1 -> e2 -> e0
    return ((0, 0, 1), (1, 0, 0), (0, 1, 0))


def all_vertices() -> tuple[Vector, ...]:
    return tuple(
        (sx, sy, sz)
        for sx, sy, sz in product((-1, 1), repeat=3)
    )


def diagonal_index(vector: Vector) -> int:
    if vector[0] < 0:
        vector = (-vector[0], -vector[1], -vector[2])
    return DIAG_REPS.index(vector)


def phi(matrix: Matrix) -> Perm:
    return tuple(diagonal_index(matvec(matrix, rep)) for rep in DIAG_REPS)


def compose_perm(left: Perm, right: Perm) -> Perm:
    return (left[right[0]], left[right[1]], left[right[2]], left[right[3]])


def identity_perm() -> Perm:
    return (0, 1, 2, 3)


def order_of(matrix: Matrix) -> int:
    current = matrix
    for order in range(1, 9):
        if current == I3:
            return order
        current = matmul(current, matrix)
    return 0


def generated_subgroup(seed_a: Matrix, seed_b: Matrix) -> set[Matrix]:
    seen: set[Matrix] = {I3}
    frontier = [I3]
    while frontier:
        current = frontier.pop()
        for generator in (seed_a, seed_b):
            product = matmul(current, generator)
            if product not in seen:
                seen.add(product)
                frontier.append(product)
    return seen


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

    print("external_scientific_inputs: none; exact integer signed-permutation algebra only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact Z coefficients; no floating-point inputs")
    print("claim_boundary: constructed isomorphism G -> S_4; no axiom edit is asserted")

    group = enumerate_G()
    group_set = set(group)
    formula_count = count_by_sign_rule()
    s4_size = sum(1 for _ in permutations(range(4)))

    checks.check("thm1-order", "|G| = 24 by enumeration", len(group) == 24)
    checks.check(
        "thm1-distinct",
        "the 24 enumerated matrices are distinct",
        len(group_set) == 24,
    )
    checks.check(
        "thm1-sign-rule",
        "3! axis permutations times 4 admissible sign patterns equal 24",
        formula_count == 24 and formula_count == len(group),
    )
    checks.check(
        "thm1-s4-count",
        "|S_4| = 24 by enumerating permutations of four labels",
        s4_size == 24,
    )
    checks.check(
        "thm1-membership",
        "every enumerated matrix is a det=+1 signed permutation with R^T R = I",
        all(
            is_signed_permutation(matrix)
            and det3(matrix) == 1
            and matmul(transpose(matrix), matrix) == I3
            for matrix in group
        ),
    )
    checks.check(
        "mutation-minus-i-not-in-G",
        "-I has det=-1 and is absent from G",
        det3(MINUS_I3) == -1 and MINUS_I3 not in group_set,
    )

    vertices = all_vertices()
    assigned = tuple(diagonal_index(vertex) for vertex in vertices)
    checks.check(
        "diag-partition",
        "the eight vertices partition into the four listed space diagonals",
        len(vertices) == 8
        and set(assigned) == {0, 1, 2, 3}
        and all(assigned.count(index) == 2 for index in range(4)),
    )

    rot90 = rotation_90_about_x()
    rot120 = rotation_120_about_111()
    checks.check(
        "gen-in-G",
        "the 90-about-x and 120-about-(1,1,1) matrices lie in G",
        rot90 in group_set and rot120 in group_set,
    )
    checks.check(
        "gen-orders",
        "those generators have orders 4 and 3",
        order_of(rot90) == 4 and order_of(rot120) == 3,
    )
    checks.check(
        "gen-generate",
        "the pair generates all 24 elements of G",
        generated_subgroup(rot90, rot120) == group_set,
    )

    phi_values = {matrix: phi(matrix) for matrix in group}
    identity_image = phi(I3)
    kernel = tuple(
        matrix for matrix, image in phi_values.items() if image == identity_perm()
    )
    image = set(phi_values.values())

    checks.check("phi-id", "phi(I) is the identity permutation", identity_image == identity_perm())
    checks.check(
        "thm3-ker",
        "ker phi = {I}",
        kernel == (I3,) and I3 in group_set,
    )
    checks.check(
        "thm4-surjective",
        "im phi has 24 distinct permutations, hence equals S_4",
        len(image) == 24 and len(image) == s4_size,
    )

    product_90_120 = matmul(rot90, rot120)
    product_120_90 = matmul(rot120, rot90)
    checks.check(
        "thm2-gen-pair",
        "phi is multiplicative on the generating pair",
        phi(product_90_120) == compose_perm(phi(rot90), phi(rot120))
        and phi(product_120_90) == compose_perm(phi(rot120), phi(rot90)),
    )
    checks.check(
        "thm2-all-pairs",
        "phi(RS)=phi(R) o phi(S) for every pair in G",
        all(
            phi(matmul(left, right)) == compose_perm(phi_values[left], phi_values[right])
            for left in group
            for right in group
        ),
    )

    note_unquoted = "\n".join(
        line[2:] if line.startswith("> ") else line for line in note.splitlines()
    )
    forbidden_hits = tuple(
        item for item in FORBIDDEN_NOTE_SUBSTRINGS if item in note
    )
    checks.check(
        "note-forbidden-substrings",
        "the note contains none of the dispatch-forbidden substrings",
        forbidden_hits == (),
    )
    checks.check(
        "live-lattice-quote",
        "the live Lattice proper-cubic-rotations sentence is quoted without rewrite",
        LATTICE_QUOTE in axiom and LATTICE_QUOTE in note_unquoted,
    )
    checks.check(
        "live-qubit-unflipped",
        "the live Qubit M_2(C) sentence is quoted without rewrite",
        QUBIT_QUOTE in axiom and QUBIT_QUOTE in note,
    )
    checks.check(
        "scope-boundary",
        "the note disclaims Aut(M_2) adoption, axiom text, and inverse-square",
        "no Aut(`M_2`)" in note
        and "No axiom text" in note
        and "No inverse-square" in note
        and "Qubit remains" in note
        and "M_2(C)" in note,
    )
    checks.check(
        "machine-status-contract",
        "bounded-support status and not-proposed axiom status are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "hypothetical_axiom_status: \"not proposed\"" in note
        and "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/CUBE_ROTATIONS_S4_DIAGONALS_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "parents-axiom-only",
        "the note names the live axiom memo as its only parent",
        "**Parents:** the live axiom memo" in note
        and "MINIMAL_AXIOMS_2026-06-29.md" in note,
    )

    print("per_element: each of the 24 matrices is tested for membership, kernel, and image.")
    print("per_site: not executed — the claim is the onsite rotation group, not a multi-site law.")
    print("per_mode: the four space diagonals are the only labels of phi.")
    print("per_block: multiplicativity is checked on the generating pair and on all 24x24 products.")
    print("lattice_wide: checked and not executed — no lattice-wide lift is asserted.")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
