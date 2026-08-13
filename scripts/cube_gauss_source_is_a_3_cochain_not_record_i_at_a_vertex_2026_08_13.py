#!/usr/bin/env python3
"""Exact Z2 checks: cube Gauss source is a 3-cochain, not vertex Record I.

The runner reconstructs the six unit-cube faces, checks the two-count of each
edge, evaluates bianchi_sum(theta) on every link field, and evaluates
record_I(locks) on vertex lock patterns. Identity gates call those two
functions. The hostile predicate that I=1 equals Gauss rho must fail.
"""

from __future__ import annotations

import ast
import inspect
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "CUBE_GAUSS_SOURCE_IS_A_3_COCHAIN_NOT_RECORD_I_AT_A_VERTEX_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NEWTON_PATH = ROOT / "docs" / "NEWTON_LAW_DERIVED_NOTE.md"

AUDIT_INPUT_PATHS = (
    "docs/CUBE_GAUSS_SOURCE_IS_A_3_COCHAIN_NOT_RECORD_I_AT_A_VERTEX_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/NEWTON_LAW_DERIVED_NOTE.md",
)

FACES: tuple[frozenset[int], ...] = (
    frozenset({0, 5, 1, 4}),   # z=0
    frozenset({2, 7, 3, 6}),   # z=1
    frozenset({0, 9, 2, 8}),   # y=0
    frozenset({1, 11, 3, 10}),  # y=1
    frozenset({4, 10, 6, 8}),  # x=0
    frozenset({5, 11, 7, 9}),  # x=1
)

Lock = str | None
Locks = tuple[Lock, ...]


def normalize(text: str) -> str:
    return " ".join(text.split())


def holonomy(theta: tuple[int, ...], face: frozenset[int]) -> int:
    return sum(theta[edge] for edge in face) % 2


def bianchi_sum(theta: tuple[int, ...]) -> int:
    """Z2 sum of the six face holonomies; this is the forced cube source rho."""
    return sum(holonomy(theta, face) for face in FACES) % 2


def record_I(locks: Locks) -> int:
    """Content-only count of locked vertices."""
    return sum(lock is not None for lock in locks)


def identity_link_field_rho(theta: tuple[int, ...]) -> int:
    """Identity gate for the link-field source. Must call bianchi_sum(theta)."""
    return bianchi_sum(theta)


def identity_vertex_I(locks: Locks) -> int:
    """Identity gate for vertex Record count. Must call record_I(locks)."""
    return record_I(locks)


def predicate_i_one_equals_gauss_rho(theta: tuple[int, ...], locks: Locks) -> bool:
    """Hostile identification: a one-vertex lock equals the cube Gauss source."""
    return identity_vertex_I(locks) == 1 and identity_vertex_I(locks) == identity_link_field_rho(theta)


def edge_face_counts() -> tuple[int, ...]:
    counts = [0] * 12
    for face in FACES:
        for edge in face:
            counts[edge] += 1
    return tuple(counts)


def function_calls(name: str) -> set[str]:
    source = inspect.getsource(globals()[name])
    tree = ast.parse(source)
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            names.add(node.func.id)
    return names


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
    newton = NEWTON_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)
    normalized_newton = normalize(newton)

    print(
        "external_scientific_inputs: axiom Record wording and the Newton "
        "source-linearity non-claim are source-bound; no observational inputs"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency against AUDIT_INPUT_PATHS"
    )

    checks.check(
        "audit-inputs",
        "declared inputs are the new note, the axiom memo, and the Newton note",
        AUDIT_INPUT_PATHS
        == (
            "docs/CUBE_GAUSS_SOURCE_IS_A_3_COCHAIN_NOT_RECORD_I_AT_A_VERTEX_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/NEWTON_LAW_DERIVED_NOTE.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and NEWTON_PATH.is_file(),
    )
    checks.check(
        "face-reconstruction",
        "six faces, each a 4-edge set, cover twelve edges",
        len(FACES) == 6 and all(len(face) == 4 for face in FACES) and set().union(*FACES) == set(range(12)),
    )
    checks.check(
        "two-count",
        "each edge lies in exactly two faces",
        edge_face_counts() == (2,) * 12,
    )

    zero_field = (0,) * 12
    one_edge = (1,) + (0,) * 11
    all_ones = (1,) * 12
    all_rho_zero = all(identity_link_field_rho(theta) == 0 for theta in product((0, 1), repeat=12))
    checks.check(
        "identity-bianchi-zero",
        "identity_link_field_rho calls bianchi_sum and returns 0 on sample fields",
        "bianchi_sum" in function_calls("identity_link_field_rho")
        and identity_link_field_rho(zero_field) == 0
        and identity_link_field_rho(one_edge) == 0
        and identity_link_field_rho(all_ones) == 0,
    )
    checks.check(
        "theorem-1-all-fields",
        "bianchi_sum(theta) is 0 for every Z2 link field, so forced rho is 0",
        all_rho_zero and bianchi_sum(one_edge) == 0,
    )

    unlocked: Locks = (None,) * 8
    one_lock: Locks = ("A",) + (None,) * 7
    other_one_lock: Locks = (None,) * 3 + ("B",) + (None,) * 4
    full_lock: Locks = ("A", "B", "A", "B", "A", "B", "A", "B")
    checks.check(
        "identity-record-I",
        "identity_vertex_I calls record_I and counts the lock domain",
        "record_I" in function_calls("identity_vertex_I")
        and identity_vertex_I(unlocked) == 0
        and identity_vertex_I(one_lock) == 1
        and identity_vertex_I(other_one_lock) == 1
        and identity_vertex_I(full_lock) == 8,
    )
    checks.check(
        "theorem-2-type-split",
        "I=1 exists and is not the forced cube source rho=0",
        record_I(one_lock) == 1 and bianchi_sum(zero_field) == 0 and record_I(one_lock) != bianchi_sum(zero_field),
    )
    checks.check(
        "mutation-i-equals-rho",
        "the predicate I=1 equals Gauss rho fails",
        predicate_i_one_equals_gauss_rho(zero_field, one_lock) is False
        and predicate_i_one_equals_gauss_rho(one_edge, other_one_lock) is False
        and record_I(one_lock) == 1,
    )
    checks.check(
        "source-record",
        "Record I is quoted as content-only additive readout",
        "A readout value is determined by record content alone." in normalized_axiom
        and "scalar readout `I` is additive, with `I(empty)=0`." in normalized_axiom
        and "`I` is a content-only count of locks" in normalized_note
        and "does not name a 3-cochain on cubes" in normalized_note
        and "The extra object for a lattice Gauss source is `ρ` on 3-cells." in note,
    )
    checks.check(
        "source-newton-nonclaim",
        "Newton is cited only as a source-linearity non-claim",
        "source-linearity" in normalized_newton
        and "Newton's law as an unconditional framework output" in newton
        and "source-linearity non-claim" in normalized_note
        and "does not install Newton" in normalized_note
        and "does not identify `I` with mass" in note,
    )
    checks.check(
        "display-not-adopt",
        "rho is displayed and not adopted",
        "Display `ρ`; do not adopt it." in note
        and "we adopt" not in note.lower(),
    )
    checks.check(
        "theorem-5-scope",
        "two-count is not a new Bianchi theorem and 4D color is not claimed",
        "not a new Bianchi theorem beyond the two-count" in normalized_note
        and "Do not claim 4D color." in note
        and "SU(3)" not in note
        and "cubebianchi" not in note.lower()
        and "unittable" not in note.lower(),
    )
    forbidden = ("G" + "_N", "1" + "/r", "L" + "_phys")
    runner_text = Path(__file__).read_text(encoding="utf-8")
    checks.check(
        "forbidden-tokens",
        "note stays off coupling, inverse-distance, and physical-length tokens",
        all(token not in note for token in forbidden)
        and all(token not in runner_text for token in forbidden),
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note,
    )

    print("per_element: twelve edges and six faces are reconstructed; every Z2 link field is summed")
    print("per_site: Record I is a vertex lock-domain count on the eight cube vertices")
    print("per_block: the only negative block is the I=1 versus rho=0 type split")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
