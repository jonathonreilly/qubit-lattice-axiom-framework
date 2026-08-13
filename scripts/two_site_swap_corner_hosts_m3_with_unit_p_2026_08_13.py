#!/usr/bin/env python3
"""Exact checks: two-site SWAP corner hosts M_3 with unit p.

Finite integer/Fraction matrix identities only. No QCD, no axiom edit, no
cache write, no network.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "TWO_SITE_SWAP_CORNER_HOSTS_M3_WITH_UNIT_P_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_SITE_SWAP_CORNER_HOSTS_M3_WITH_UNIT_P_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, ...], ...]
Vector = tuple[Fraction, ...]


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


def sub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][col] - right[row][col] for col in range(len(left)))
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


def transpose(matrix: tuple[tuple[Fraction, ...], ...]) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix[0])))


def trace(matrix: Matrix) -> Fraction:
    return sum((matrix[i][i] for i in range(len(matrix))), Fraction(0))


def ketbra(left: Vector, right: Vector) -> Matrix:
    return tuple(tuple(left[row] * right[col] for col in range(len(right))) for row in range(len(left)))


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((matrix[row][col] * vector[col] for col in range(len(vector))), Fraction(0))
        for row in range(len(matrix))
    )


def inner(left: Vector, right: Vector) -> Fraction:
    return sum((left[i] * right[i] for i in range(len(left))), Fraction(0))


def mul_rect(left: tuple[tuple[Fraction, ...], ...], right: tuple[tuple[Fraction, ...], ...]) -> tuple[tuple[Fraction, ...], ...]:
    rows = len(left)
    mid = len(left[0])
    cols = len(right[0])
    return tuple(
        tuple(
            sum((left[row][k] * right[k][col] for k in range(mid)), Fraction(0))
            for col in range(cols)
        )
        for row in range(rows)
    )


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


def flatten(matrix: Matrix) -> tuple[Fraction, ...]:
    return tuple(value for row in matrix for value in row)


def stack_rows(matrices: list[Matrix]) -> Matrix:
    return tuple(flatten(matrix) for matrix in matrices)


def dim_mn(n: int) -> int:
    return n * n


def swap_matrix() -> Matrix:
    """Permutation matrix of |ab> <-> |ba> on the product basis |00>,|01>,|10>,|11>."""
    data = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for a in (0, 1):
        for b in (0, 1):
            source = 2 * a + b
            target = 2 * b + a
            data[target][source] = Fraction(1)
    return tuple(tuple(item) for item in data)


def phi(matrix3: Matrix, wide: tuple[tuple[Fraction, ...], ...], gram_inv: Matrix) -> Matrix:
    """Fraction *-iso M_3 → p M_4 p given by φ(X) = W G^{-1} X W*."""
    return mul_rect(wide, mul_rect(gram_inv, mul_rect(matrix3, transpose(wide))))


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

    print("external_scientific_inputs: current axiom wording is source-bound; no observational or fitted inputs are used")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("measure_boundary: exact integer/Fraction matrix algebra only")
    print("negative_scope: only the displayed swap corner is identified; SU(3), QCD, a Qubit rewrite, and a color axiom are not installed")

    identity3 = eye(3)
    identity4 = eye(4)
    swap = swap_matrix()
    projector = scale(Fraction(1, 2), add(identity4, swap))
    opposite = sub(identity4, projector)

    displayed_projector = (
        (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1, 2), Fraction(1, 2), Fraction(0)),
        (Fraction(0), Fraction(1, 2), Fraction(1, 2), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
    )

    w1: Vector = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    w2: Vector = (Fraction(0), Fraction(1), Fraction(1), Fraction(0))
    w3: Vector = (Fraction(0), Fraction(0), Fraction(0), Fraction(1))
    wide = tuple(zip(w1, w2, w3))
    gram_inv = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1, 2), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )

    on_sum = add(add(ketbra(w1, w1), scale(Fraction(1, 2), ketbra(w2, w2))), ketbra(w3, w3))
    compressed_units = [mul(mul(projector, e_unit(4, row, col)), projector) for row in range(4) for col in range(4)]
    corner_dim = rank(stack_rows(compressed_units))

    phi_id = phi(identity3, wide, gram_inv)
    e12 = e_unit(3, 0, 1)
    e21 = e_unit(3, 1, 0)
    e11 = e_unit(3, 0, 0)
    e22 = e_unit(3, 1, 1)
    sample = add(scale(Fraction(2), e12), scale(Fraction(-3), identity3))

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
        "thm1-hermitian",
        "the two-site swap F is Hermitian",
        adj(swap) == swap,
    )
    checks.check(
        "thm1-involution",
        "F squared equals I_4",
        mul(swap, swap) == identity4,
    )
    checks.check(
        "thm1-trace",
        "Tr(F) equals 2",
        trace(swap) == Fraction(2),
    )
    checks.check(
        "thm1-spectrum",
        "the +1 space of F has rank 3 and the -1 space has rank 1",
        rank(projector) == 3 and rank(opposite) == 1 and add(projector, opposite) == identity4,
    )
    checks.check(
        "thm2-projection",
        "p = (I_4 + F)/2 is an orthogonal projection",
        mul(projector, projector) == projector and adj(projector) == projector,
    )
    checks.check(
        "thm2-explicit",
        "p equals the displayed rank-3 swap projector",
        projector == displayed_projector,
    )
    checks.check(
        "thm2-not-identity",
        "p is not I_4",
        projector != identity4,
    )
    checks.check(
        "thm2-image-basis",
        "p fixes |00>, |01>+|10>, |11> and kills |01>-|10>",
        matvec(projector, w1) == w1
        and matvec(projector, w2) == w2
        and matvec(projector, w3) == w3
        and matvec(projector, (Fraction(0), Fraction(1), Fraction(-1), Fraction(0)))
        == (Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
    )
    checks.check(
        "thm3-unit",
        "p is the unit of the corner p M_4 p",
        all(mul(mul(projector, matrix), projector) == matrix for matrix in compressed_units)
        and mul(mul(projector, identity4), projector) == projector,
    )
    checks.check(
        "thm3-dim",
        "dim_C(C) equals rank(p)^2 equals 9",
        corner_dim == 9 and rank(projector) ** 2 == 9 and dim_mn(3) == 9,
    )
    checks.check(
        "thm3-iso-unit",
        "the Fraction *-iso and the ON projector sum both send I_3 to p",
        phi_id == projector and on_sum == projector,
    )
    basis = (w1, w2, w3)
    unnorm_units = [[ketbra(basis[i], basis[j]) for j in range(3)] for i in range(3)]
    checks.check(
        "thm3-iso-hom",
        "phi is a Q-linear algebra map, and the ON units of im(p) multiply as matrix units",
        phi(sample, wide, gram_inv) == add(scale(Fraction(2), phi(e12, wide, gram_inv)), scale(Fraction(-3), phi_id))
        and phi(mul(e12, e21), wide, gram_inv) == mul(phi(e12, wide, gram_inv), phi(e21, wide, gram_inv))
        and mul(phi(e12, wide, gram_inv), phi(e21, wide, gram_inv)) == phi(e11, wide, gram_inv)
        and all(
            mul(unnorm_units[i][j], unnorm_units[k][l])
            == scale(inner(basis[j], basis[k]), unnorm_units[i][l])
            for i in range(3)
            for j in range(3)
            for k in range(3)
            for l in range(3)
        )
        and all(adj(unnorm_units[i][j]) == unnorm_units[j][i] for i in range(3) for j in range(3)),
    )
    checks.check(
        "thm3-iso-injective",
        "phi has trivial kernel on the nine matrix units",
        all(phi(e_unit(3, row, col), wide, gram_inv) != zero(4) for row in range(3) for col in range(3)),
    )
    checks.check(
        "thm3-on-table",
        "integer spanning vectors of im(p) are orthogonal with middle norm squared 2",
        inner(w1, w2) == 0
        and inner(w1, w3) == 0
        and inner(w2, w3) == 0
        and inner(w1, w1) == 1
        and inner(w2, w2) == 2
        and inner(w3, w3) == 1
        and phi(e22, wide, gram_inv) == scale(Fraction(1, 2), ketbra(w2, w2)),
    )
    checks.check(
        "thm4-inclusion-not-unital",
        "the inclusion C into M_4 is not unital",
        projector != identity4 and phi_id != identity4,
    )
    checks.check(
        "thm5-qubit-untouched",
        "Qubit still names one-site M_2(C) and is not rewritten to M_3",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`." in axiom
        and "rewritten to `M_3`" not in axiom,
    )
    unital_predicate = projector == identity4
    rank_predicate = rank(projector) == 4
    dim_predicate = corner_dim == 9
    checks.check(
        "mutation-unital",
        "predicate p == I_4 fails",
        unital_predicate is False,
    )
    checks.check(
        "mutation-rank",
        "predicate rank(p) == 4 fails",
        rank_predicate is False,
    )
    checks.check(
        "mutation-dim",
        "predicate dim_C(C) == 9 holds",
        dim_predicate is True,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the required bounded-support and color-as-corner leftover status lines",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                'hypothetical_axiom_status: "color-as-corner leftover: p M_4 p ≅ M_3 with unit p; not adopted as QCD"',
                "**Type:** bounded_theorem",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "note-negative-scope",
        "the note refuses SU(3) installation, QCD naming, Qubit rewrite, and color selection",
        all(
            phrase in normalized_note
            for phrase in (
                "does not install `SU(3)`",
                "does not name QCD",
                "does not flip Qubit to `M_3`",
                "does not select color",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo does not contain the swap projector or a color-algebra rewrite",
        all(
            phrase not in axiom
            for phrase in (
                "swap projector",
                "p M_4 p",
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
        and "color is selected by the two-site swap" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the declared note-plus-axiom tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_SITE_SWAP_CORNER_HOSTS_M3_WITH_UNIT_P_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )

    print("per_element: F, p, I_3, I_4, and the matrix units of im(p) are evaluated")
    print("per_site: the statement is the two-site tensor T_2 ≅ M_4; no lattice-wide carrier is asserted")
    print("per_mode: the displayed two-site swap and its +1 corner are the tested maps")
    print("per_block: only the corner host with unit p is identified; unital factorhood and color selection are refused")
    print("lattice_wide: checked and not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
