#!/usr/bin/env python3
"""Exact checks: the M_3 corner pad in M_4 is not a unital color algebra.

Finite integer/Fraction matrix identities only. No QCD, no axiom edit, no
cache write, no network.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "M3_CORNER_IN_M4_IS_NOT_UNITAL_COLOR_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/M3_CORNER_IN_M4_IS_NOT_UNITAL_COLOR_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, ...], ...]


def normalize(text: str) -> str:
    return " ".join(text.split())


def zero(n: int) -> Matrix:
    return tuple(tuple(Fraction(0) for _ in range(n)) for _ in range(n))


def eye(n: int) -> Matrix:
    return tuple(tuple(Fraction(int(row == col)) for col in range(n)) for row in range(n))


def e_unit(n: int, row: int, col: int) -> Matrix:
    data = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    data[row][col] = Fraction(1)
    return tuple(tuple(item) for item in data)


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][col] + right[row][col] for col in range(len(left)))
        for row in range(len(left))
    )


def scale(scalar: Fraction, matrix: Matrix) -> Matrix:
    return tuple(tuple(scalar * matrix[row][col] for col in range(len(matrix))) for row in range(len(matrix)))


def mul(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return tuple(
        tuple(
            sum((left[row][mid] * right[mid][col] for mid in range(size)), Fraction(0))
            for col in range(size)
        )
        for row in range(size)
    )


def adj(matrix: Matrix) -> Matrix:
    size = len(matrix)
    return tuple(tuple(matrix[col][row] for col in range(size)) for row in range(size))


def iota(matrix: Matrix) -> Matrix:
    if len(matrix) != 3:
        raise ValueError("iota is defined on 3x3 matrices")
    data = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for row in range(3):
        for col in range(3):
            data[row][col] = matrix[row][col]
    return tuple(tuple(item) for item in data)


def rank(matrix: Matrix) -> int:
    """Exact row rank over Q by Gaussian elimination."""
    rows = [list(row) for row in matrix]
    height = len(rows)
    width = len(rows[0]) if rows else 0
    lead = 0
    computed = 0
    for r in range(height):
        if lead >= width:
            return computed
        i = r
        while rows[i][lead] == 0:
            i += 1
            if i == height:
                i = r
                lead += 1
                if lead == width:
                    return computed
        rows[i], rows[r] = rows[r], rows[i]
        pivot = rows[r][lead]
        rows[r] = [value / pivot for value in rows[r]]
        for i in range(height):
            if i == r:
                continue
            factor = rows[i][lead]
            rows[i] = [rows[i][c] - factor * rows[r][c] for c in range(width)]
        computed += 1
        lead += 1
    return computed


def dim_mn(n: int) -> int:
    return n * n


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

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
    normalized_axiom = normalize(axiom)

    print("external_scientific_inputs: current axiom wording is source-bound; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("measure_boundary: exact integer/Fraction matrix algebra only")
    print("negative_scope: only the displayed non-unital corner pad is rejected; SU(3), QCD, and a color axiom are not installed")

    identity3 = eye(3)
    identity4 = eye(4)
    e12 = e_unit(3, 0, 1)
    e21 = e_unit(3, 1, 0)
    e11 = e_unit(3, 0, 0)
    sample = add(scale(Fraction(2), e12), scale(Fraction(-3), identity3))

    padded_identity = iota(identity3)
    padded_e12 = iota(e12)
    padded_e21 = iota(e21)
    padded_sample = iota(sample)
    projection = padded_identity
    opposite = tuple(
        tuple(identity4[row][col] - projection[row][col] for col in range(4))
        for row in range(4)
    )

    checks.check(
        "source-qubit",
        "the axiom memo names the full one-site possibility domain M_2(C)",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`." in axiom,
    )
    checks.check(
        "dim-two-site",
        "T_2 = M_2 ⊗ M_2 has complex dimension 16, matching M_4",
        dim_mn(2) * dim_mn(2) == 16 and dim_mn(4) == 16,
    )
    checks.check(
        "dim-m3",
        "M_3 has complex dimension 9",
        dim_mn(3) == 9,
    )
    checks.check(
        "thm1-linear",
        "iota is Q-linear on a two-term combination of E_12 and I_3",
        padded_sample == add(scale(Fraction(2), padded_e12), scale(Fraction(-3), padded_identity)),
    )
    checks.check(
        "thm1-star",
        "iota preserves the adjoint on E_12 and I_3",
        iota(adj(e12)) == adj(padded_e12) and iota(adj(identity3)) == adj(padded_identity),
    )
    checks.check(
        "thm1-multiplicative",
        "iota(E_12 E_21) equals iota(E_12) iota(E_21) and recovers iota(E_11)",
        iota(mul(e12, e21)) == mul(padded_e12, padded_e21) and mul(padded_e12, padded_e21) == iota(e11),
    )
    checks.check(
        "thm1-injective",
        "iota has trivial kernel on the nine matrix units",
        all(iota(e_unit(3, row, col)) != zero(4) for row in range(3) for col in range(3)),
    )
    checks.check(
        "thm1-e12",
        "iota(E_12) is the 4x4 matrix unit in position (1,2)",
        padded_e12 == e_unit(4, 0, 1),
    )
    checks.check(
        "thm1-identity-image",
        "iota(I_3) is the projection P = diag(1,1,1,0)",
        projection == tuple(
            tuple(Fraction(int(row == col and row < 3)) for col in range(4))
            for row in range(4)
        ),
    )
    checks.check(
        "thm2-not-unital",
        "iota(I_3) is not I_4, so the pad is not a unital *-homomorphism",
        padded_identity != identity4,
    )
    checks.check(
        "thm3-rank",
        "rank(iota(I_3)) is 3 and rank(I_4) is 4",
        rank(padded_identity) == 3 and rank(identity4) == 4,
    )
    checks.check(
        "thm3-projection",
        "P is a projection with complementary rank 1",
        mul(projection, projection) == projection
        and adj(projection) == projection
        and rank(opposite) == 1
        and add(projection, opposite) == identity4,
    )
    unital_predicate = padded_identity == identity4
    rank_predicate = rank(padded_identity) == 4
    checks.check(
        "mutation-unital",
        "predicate iota(I_3) == I_4 fails",
        unital_predicate is False,
    )
    checks.check(
        "mutation-rank",
        "predicate rank(iota(I_3)) == 4 fails",
        rank_predicate is False,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the required bounded-support and C2 leftover status lines",
        all(
            phrase in note
            for phrase in (
                'actual_current_surface_status: bounded-support',
                'hypothetical_axiom_status: "C2 tensor composite leftover: non-unital corner is not the color algebra; not adopted"',
                "**Type:** bounded_theorem",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "note-negative-scope",
        "the note refuses SU(3) installation, QCD naming, and color-axiom adoption",
        all(
            phrase in normalized_note
            for phrase in (
                "does not install `SU(3)`",
                "does not name QCD",
                "does not adopt a color axiom",
                "wrong type for “color is a composite of qubits.”",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo does not contain the pad or a color-algebra rewrite",
        all(
            phrase not in axiom
            for phrase in (
                "iota",
                "diag(X, 0)",
                "color algebra",
                "SU(3)",
                "QCD",
            )
        ),
    )
    checks.check(
        "no-go-gate",
        "N1-N8 and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the declared note-plus-axiom tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/M3_CORNER_IN_M4_IS_NOT_UNITAL_COLOR_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    print("per_element: I_3, I_4, E_12, E_21, and E_11 are evaluated under iota")
    print("per_site: the statement is the two-site tensor T_2 ≅ M_4; no lattice-wide carrier is asserted")
    print("per_mode: the displayed top-left pad is the tested map")
    print("per_block: only unit-algebra identification via the cheap pad is rejected")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
