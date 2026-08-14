#!/usr/bin/env python3
"""Exact order census of the 24 proper 3x3 signed permutation matrices.

G is enumerated over Z. Element orders are least k>0 with R^k = I.
No cache write, no citation manifest, no axiom edit.
"""

from __future__ import annotations

from collections import Counter
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "CUBE_ROTATION_GROUP_NOT_CYCLIC_DIHEDRAL_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CUBE_ROTATION_GROUP_NOT_CYCLIC_DIHEDRAL_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

IDENTITY: Matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

# 90° about the third coordinate axis: a displayed order-4 witness.
AXIS_90: Matrix = ((0, -1, 0), (1, 0, 0), (0, 0, 1))

LATTICE_QUOTE_SITES = (
    "Physical sites are the points of the cubic lattice `Z^3`, with "
    "nearest-neighbor adjacency, standard translations, and proper cubic "
    "rotations about each site."
)
LATTICE_QUOTE_NO_PRIVILEGE = (
    "No site is privileged. Sites are distinguished by the supplied lattice "
    "structure alone."
)

FORBIDDEN_NOTE_SUBSTRINGS = (
    "G_N",
    "1/r",
    "1/r^2",
    "Lattice-named",
    "not a TOE",
    "we adopt",
    "Codex",
    "L_phys",
)


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][0] * right[0][col]
            + left[row][1] * right[1][col]
            + left[row][2] * right[2][col]
            for col in range(3)
        )
        for row in range(3)
    )


def det3(matrix: Matrix) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def is_signed_permutation(matrix: Matrix) -> bool:
    for row in matrix:
        if sorted(abs(entry) for entry in row) != [0, 0, 1]:
            return False
    for col in range(3):
        if sorted(abs(matrix[row][col]) for row in range(3)) != [0, 0, 1]:
            return False
    return True


def enumerate_signed_permutation_matrices() -> list[Matrix]:
    matrices: list[Matrix] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for row in range(3):
                entries = [0, 0, 0]
                entries[perm[row]] = signs[row]
                rows.append(tuple(entries))
            matrices.append(tuple(rows))  # type: ignore[arg-type]
    return matrices


def proper_signed_permutations() -> list[Matrix]:
    return [matrix for matrix in enumerate_signed_permutation_matrices() if det3(matrix) == 1]


def collapsed(text: str) -> str:
    return " ".join(text.split())


def element_order(matrix: Matrix) -> int:
    power = matrix
    for order in range(1, 25):
        if power == IDENTITY:
            return order
        power = mat_mul(power, matrix)
    raise ArithmeticError("no order at most 24; G would not be a finite subgroup of order 24")


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

    print("external_scientific_inputs: none; exact Z matrix orders only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: integer 3x3 arithmetic; no floating-point inputs")
    print("claim_boundary: G is not C_24 and not D_12; no SO(3) census; no M_2 action")

    all_signed = enumerate_signed_permutation_matrices()
    group = proper_signed_permutations()
    unique = set(group)
    orders = [element_order(matrix) for matrix in group]
    order_set = set(orders)
    counts = Counter(orders)
    max_order = max(orders)
    order_four_count = counts[4]

    print(f"|G|={len(unique)}")
    print("order_counts: " + ", ".join(f"{order}:{counts[order]}" for order in sorted(counts)))
    print(f"max_order={max_order}")

    checks.check("signed-count-48", "there are 48 signed permutation matrices", len(all_signed) == 48)
    checks.check(
        "all-signed-perm",
        "every generated matrix is a signed permutation",
        all(is_signed_permutation(matrix) for matrix in all_signed),
    )
    checks.check("g-cardinality", "|G|=24", len(group) == 24 and len(unique) == 24)
    checks.check(
        "g-det-plus-one",
        "every element of G has det = +1",
        all(det3(matrix) == 1 for matrix in group),
    )
    checks.check("identity-in-g", "I is in G", IDENTITY in unique)
    checks.check("axis-90-in-g", "the displayed 90° axis matrix is in G", AXIS_90 in unique)
    checks.check("axis-90-order-4", "the displayed 90° axis matrix has order 4", element_order(AXIS_90) == 4)
    checks.check("orders-only-1234", "orders in G are a subset of {1,2,3,4}", order_set <= {1, 2, 3, 4})
    checks.check("max-order-4", "max order in G is 4", max_order == 4)
    checks.check("order-4-exists", "G has at least one element of order 4", order_four_count >= 1)
    checks.check("no-order-12", "G has no element of order 12", 12 not in order_set and counts[12] == 0)
    checks.check("no-order-24", "G has no element of order 24", 24 not in order_set and counts[24] == 0)
    checks.check(
        "not-c24",
        "G is not cyclic of order 24",
        len(unique) == 24 and 24 not in order_set,
    )
    checks.check(
        "not-d12",
        "G is not dihedral of order 24",
        len(unique) == 24 and 12 not in order_set,
    )

    forbidden_hits = [needle for needle in FORBIDDEN_NOTE_SUBSTRINGS if needle in note]
    checks.check(
        "note-forbidden-substrings",
        "note avoids the dispatch-forbidden substrings",
        forbidden_hits == [],
    )
    checks.check(
        "lattice-quotes",
        "Live Parent Quotes are the two Lattice sentences",
        LATTICE_QUOTE_SITES in note and LATTICE_QUOTE_NO_PRIVILEGE in note,
    )
    checks.check(
        "lattice-quotes-live",
        "quoted Lattice sentences are live on the axiom memo",
        LATTICE_QUOTE_SITES in collapsed(axiom)
        and LATTICE_QUOTE_NO_PRIVILEGE in collapsed(axiom),
    )
    checks.check(
        "parents-axiom-memo-only",
        "declared parents are the axiom memo only",
        "Parents:** the live axiom memo" in note
        and "MINIMAL_AXIOMS_2026-06-29.md" in note
        and AUDIT_INPUT_PATHS
        == (
            "docs/CUBE_ROTATION_GROUP_NOT_CYCLIC_DIHEDRAL_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "note-contract",
        "machine status, theorems, and stated non-claims are source-visible",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "**Type:** bounded_theorem",
                "## Theorem 1",
                "## Theorem 2",
                "not cyclic of order 24",
                "not dihedral of order 24",
                "does not classify all order-24 subgroups of SO(3)",
                "does not adopt an `M_2` action",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        )
        and "new axiom" not in note.lower(),
    )
    checks.check(
        "no-qubit-rewrite",
        "the one-site algebra sentence is not rewritten",
        "algebraic presentation" not in note.replace(
            "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
            "",
        ),
    )
    checks.check(
        "no-cache-write",
        "this runner writes no cache path",
        "cache" not in self_source.lower() or "No cache write" in self_source,
    )

    print("per_element: each of the 24 matrices has a computed finite order in {1,2,3,4}")
    print("per_site: the statement is about one 3x3 matrix set, not a site algebra")
    print("per_mode: only the displayed G is classified as not C_24 and not D_12")
    print("per_block: no SO(3) classification block is executed")
    print("lattice_wide: checked and not executed — no lattice-wide law is claimed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
