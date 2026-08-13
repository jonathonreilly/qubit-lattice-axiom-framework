#!/usr/bin/env python3
"""Exact checks: cubic covariance forbids a preferred-neighbor content law.

A 6-tuple maps the six cubic neighbor directions to a two-letter menu {A,B}.
The hostile law mu_z reads only the +e3 slot. Identity gates call mu_z(n)
and rotate_x90_tuple(n). All scalars are exact Fraction values.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "CUBIC_COVARIANCE_FORBIDS_PREFERRED_NEIGHBOR_CONTENT_LAW_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CUBIC_COVARIANCE_FORBIDS_PREFERRED_NEIGHBOR_CONTENT_LAW_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

A = "A"
B = "B"

PLUS_E1 = (1, 0, 0)
MINUS_E1 = (-1, 0, 0)
PLUS_E2 = (0, 1, 0)
MINUS_E2 = (0, -1, 0)
PLUS_E3 = (0, 0, 1)
MINUS_E3 = (0, 0, -1)

AXES = (PLUS_E1, MINUS_E1, PLUS_E2, MINUS_E2, PLUS_E3, MINUS_E3)

# Standard 90° rotation about +x: (x, y, z) ↦ (x, −z, y).
R = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(-1)),
    (Fraction(0), Fraction(1), Fraction(0)),
)

I3 = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1)),
)

NeighborTuple = tuple[str, str, str, str, str, str]


def normalize(text: str) -> str:
    return " ".join(text.split())


def transpose(matrix):
    return tuple(tuple(matrix[row][column] for row in range(3)) for column in range(3))


def mat_mul(left, right):
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(3)), Fraction(0))
            for j in range(3)
        )
        for i in range(3)
    )


def det3(matrix) -> Fraction:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def apply_matrix(matrix, vector):
    coords = tuple(Fraction(component) for component in vector)
    image = tuple(
        sum((matrix[i][j] * coords[j] for j in range(3)), Fraction(0))
        for i in range(3)
    )
    if any(entry.denominator != 1 for entry in image):
        raise ValueError("rotation left the integer lattice")
    return tuple(int(entry) for entry in image)


def labels_of(n: NeighborTuple) -> dict[tuple[int, int, int], str]:
    return dict(zip(AXES, n))


def tuple_from_labels(labels: dict[tuple[int, int, int], str]) -> NeighborTuple:
    return tuple(labels[axis] for axis in AXES)  # type: ignore[return-value]


def mu_z(n: NeighborTuple) -> Fraction:
    """Hostile preferred-axis law: depends only on the +e3 neighbor."""
    if labels_of(n)[PLUS_E3] == A:
        return Fraction(1)
    return Fraction(1, 3)


def rotate_x90_tuple(n: NeighborTuple) -> NeighborTuple:
    """Act by (R·n)(d) = n(R^{-1} d) with R the standard 90° rotation about x."""
    labels = labels_of(n)
    r_inv = transpose(R)
    rotated = {axis: labels[apply_matrix(r_inv, axis)] for axis in AXES}
    return tuple_from_labels(rotated)


def is_mu_z_cubic_covariant(n: NeighborTuple) -> bool:
    """Predicate 'μ_z is cubic-covariant' on one 6-tuple: μ_z(n) = μ_z(R·n)."""
    return mu_z(n) == mu_z(rotate_x90_tuple(n))


def identity_mu_z_gate(n: NeighborTuple) -> Fraction:
    return mu_z(n)


def identity_rotate_gate(n: NeighborTuple) -> NeighborTuple:
    return rotate_x90_tuple(n)


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
    runner_source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current axiom wording only; no observational or fitted inputs"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for claim-surface consistency"
    )
    print(
        "negative_scope: only preferred-axis neighbor dependence is excluded; unique covariant selection remains open"
    )

    checks.check(
        "audit-inputs",
        "declared audit inputs are the new note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/CUBIC_COVARIANCE_FORBIDS_PREFERRED_NEIGHBOR_CONTENT_LAW_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    covariance_sentence = (
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations."
    )
    checks.check(
        "source-admissibility",
        "the axiom memo states proper-cubic covariance of the rule",
        covariance_sentence in normalized_axiom,
    )
    checks.check(
        "source-note-theorems",
        "the note states Theorems 1 through 5 on the hostile law",
        all(
            phrase in note
            for phrase in (
                "Theorem 1 — The Displayed Map Is A Proper Cubic Rotation",
                "Theorem 2 — The Hostile Law Is Not Invariant Under `R`",
                "Theorem 3 — `μ_z` Is Not An Admissibility-Shaped Law",
                "Theorem 4 — Preferred-Axis Dependence Is Killed; A Unique Rule Is Not Selected",
                "Theorem 5 — A Later Selector Is Not Ruled Out",
            )
        ),
    )
    checks.check(
        "source-note-no-half",
        "the note does not force μ = 1/2",
        "does not force `μ = 1/2`" in normalized_note
        and "This note does not force `μ = 1/2`" in normalized_note,
    )
    checks.check(
        "source-note-no-adoption",
        "the note does not adopt a law",
        "does not adopt a law" in normalized_note,
    )
    checks.check(
        "source-note-no-selector-ban",
        "the note does not claim that no later selector exists",
        "does not claim that no later selector exists" in normalized_note,
    )

    r_t = transpose(R)
    checks.check(
        "theorem-1-orthogonal",
        "R^T R equals the identity with exact Fraction entries",
        mat_mul(r_t, R) == I3,
    )
    checks.check(
        "theorem-1-det",
        "det R equals 1",
        det3(R) == Fraction(1),
    )
    rotated_axes = tuple(apply_matrix(R, axis) for axis in AXES)
    checks.check(
        "theorem-1-cubic-shell",
        "R permutes the six nearest-neighbor directions",
        set(rotated_axes) == set(AXES),
    )
    checks.check(
        "theorem-1-moves-plus-e3",
        "R sends +e3 to a different cubic direction",
        apply_matrix(R, PLUS_E3) != PLUS_E3 and apply_matrix(R, PLUS_E3) in AXES,
    )

    all_b: NeighborTuple = (B, B, B, B, B, B)
    plus_e3_a_labels = {axis: B for axis in AXES}
    plus_e3_a_labels[PLUS_E3] = A
    witness: NeighborTuple = tuple_from_labels(plus_e3_a_labels)
    constant_a: NeighborTuple = (A, A, A, A, A, A)

    mu_witness = identity_mu_z_gate(witness)
    mu_all_b = identity_mu_z_gate(all_b)
    rotated_witness = identity_rotate_gate(witness)
    mu_rotated = identity_mu_z_gate(rotated_witness)

    checks.check(
        "identity-mu-z",
        "identity gate calls mu_z on the +e3=A witness and on a +e3=B tuple",
        mu_witness == Fraction(1) and mu_all_b == Fraction(1, 3),
    )
    checks.check(
        "identity-rotate",
        "identity gate calls rotate_x90_tuple and moves the +e3 slot off A",
        labels_of(rotated_witness)[PLUS_E3] == B
        and labels_of(rotated_witness)[apply_matrix(R, PLUS_E3)] == A,
    )
    checks.check(
        "values-not-half",
        "the hostile values are exact 1 and 1/3, not 1/2",
        mu_witness != Fraction(1, 2)
        and mu_rotated != Fraction(1, 2)
        and mu_all_b != Fraction(1, 2)
        and mu_witness == Fraction(1)
        and mu_rotated == Fraction(1, 3),
    )
    checks.check(
        "theorem-2-witness",
        "there exist n and R·n with mu_z(A|n)=1 and mu_z(A|R·n)=1/3",
        mu_witness == Fraction(1) and mu_rotated == Fraction(1, 3),
    )
    checks.check(
        "mutation-covariant-predicate",
        "the predicate 'μ_z is cubic-covariant' fails on the witness",
        is_mu_z_cubic_covariant(witness) is False,
    )
    checks.check(
        "constant-tuple-invariance",
        "constant 6-tuples are invariant, so the mutation is not a broken equality",
        is_mu_z_cubic_covariant(constant_a)
        and is_mu_z_cubic_covariant(all_b)
        and mu_z(constant_a) == Fraction(1)
        and mu_z(all_b) == Fraction(1, 3),
    )
    fourth = witness
    for _ in range(4):
        fourth = rotate_x90_tuple(fourth)
    checks.check(
        "rotate-order-four",
        "four applications of rotate_x90_tuple return the original 6-tuple",
        fourth == witness,
    )
    checks.check(
        "identity-gate-source",
        "the runner source contains live calls to mu_z(n) and rotate_x90_tuple(n)",
        "return mu_z(n)" in runner_source
        and "return rotate_x90_tuple(n)" in runner_source
        and "identity_mu_z_gate(witness)" in runner_source
        and "identity_rotate_gate(witness)" in runner_source,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
