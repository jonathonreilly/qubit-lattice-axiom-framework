#!/usr/bin/env python3
"""Exact integer checks: one 3-qubit C^8 can carry Y_0; cubic cancel is extra.

The runner constructs H = (C^2)^{otimes 3} congruent to C^8, the stipulated
projectors Pi_+, Pi_-, and Y_0 = Pi_+ - 3 Pi_-, then computes exact integer
traces. It reconstructs 6 - 54 = -48 from the spectrum and from the matrix
cube. Complementary cancellation is checked only on the extra-supplied
direct sum H oplus H. Hostile predicates Tr(Y_0^3)==0 and dim(H oplus H)==8
must fail. No observational inputs are used.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / (
    "docs/"
    "THREE_QUBIT_C8_CARRIES_Y0_CUBIC_CANCEL_STILL_EXTRA_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/THREE_QUBIT_C8_CARRIES_Y0_CUBIC_CANCEL_STILL_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


Matrix = tuple[tuple[int, ...], ...]


def zero(n: int) -> list[list[int]]:
    return [[0 for _ in range(n)] for _ in range(n)]


def identity(n: int) -> Matrix:
    matrix = zero(n)
    for i in range(n):
        matrix[i][i] = 1
    return tuple(tuple(row) for row in matrix)


def diag_from_values(values: tuple[int, ...]) -> Matrix:
    matrix = zero(len(values))
    for i, value in enumerate(values):
        matrix[i][i] = value
    return tuple(tuple(row) for row in matrix)


def add(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(n)) for i in range(n)
    )


def scale(value: int, matrix: Matrix) -> Matrix:
    n = len(matrix)
    return tuple(
        tuple(value * matrix[i][j] for j in range(n)) for i in range(n)
    )


def mul(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(n)) for j in range(n)
        )
        for i in range(n)
    )


def trace(matrix: Matrix) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def rank_diagonal(matrix: Matrix) -> int:
    return sum(1 for i in range(len(matrix)) if matrix[i][i] != 0)


def kronecker(left: Matrix, right: Matrix) -> Matrix:
    a, b = len(left), len(right)
    out = zero(a * b)
    for i in range(a):
        for j in range(a):
            for k in range(b):
                for el in range(b):
                    out[i * b + k][j * b + el] = left[i][j] * right[k][el]
    return tuple(tuple(row) for row in out)


def block_diag(left: Matrix, right: Matrix) -> Matrix:
    a, b = len(left), len(right)
    out = zero(a + b)
    for i in range(a):
        for j in range(a):
            out[i][j] = left[i][j]
    for i in range(b):
        for j in range(b):
            out[a + i][a + j] = right[i][j]
    return tuple(tuple(row) for row in out)


def spectrum_of_diagonal(matrix: Matrix) -> tuple[int, ...]:
    return tuple(matrix[i][i] for i in range(len(matrix)))


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
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current axiom wording is source-bound; "
        "no observational or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; parents on origin/main are the axiom memo only"
    )
    print(
        "measure_boundary: exact integer traces and dimensions only; "
        "6-54=-48 is reconstructed from the spectrum and from the matrix cube"
    )
    print(
        "negative_scope: one 3-qubit Hilbert is not a cubic-cancel; "
        "no charge naming and no generation axiom"
    )

    qubit_sentence = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    checks.check(
        "source-qubit",
        "the current Qubit wording names one-site M_2(C)",
        qubit_sentence in axiom,
    )
    checks.check(
        "source-no-y0",
        "the axiom memo does not name Y_0",
        "Y_0" not in axiom,
    )
    checks.check(
        "source-no-second-c8",
        "the axiom memo does not name a second C^8",
        "C^8" not in axiom and "C^8" not in axiom.replace("\\", ""),
    )

    one_qubit = identity(2)
    three_qubit = kronecker(one_qubit, kronecker(one_qubit, one_qubit))
    dim_h = len(three_qubit)
    checks.check(
        "dim-H",
        "dim H = 2^3 = 8",
        dim_h == 8 and dim_h == 2**3 and three_qubit == identity(8),
    )

    pi_plus = diag_from_values((1, 1, 1, 1, 1, 1, 0, 0))
    pi_minus = diag_from_values((0, 0, 0, 0, 0, 0, 1, 1))
    checks.check(
        "pi-plus-projector",
        "Pi_+ is a rank-6 projector",
        mul(pi_plus, pi_plus) == pi_plus
        and rank_diagonal(pi_plus) == 6
        and trace(pi_plus) == 6,
    )
    checks.check(
        "pi-minus-projector",
        "Pi_- is a rank-2 projector",
        mul(pi_minus, pi_minus) == pi_minus
        and rank_diagonal(pi_minus) == 2
        and trace(pi_minus) == 2,
    )
    checks.check(
        "pi-complement",
        "Pi_+ and Pi_- are complementary orthogonal projectors on C^8",
        mul(pi_plus, pi_minus) == diag_from_values((0,) * 8)
        and add(pi_plus, pi_minus) == identity(8),
    )

    y0 = add(pi_plus, scale(-3, pi_minus))
    stipulated = diag_from_values((1, 1, 1, 1, 1, 1, -3, -3))
    checks.check(
        "y0-definition",
        "Y_0 = Pi_+ - 3 Pi_- equals diag(I_6, -3 I_2)",
        y0 == stipulated,
    )

    plus_mult = spectrum_of_diagonal(y0).count(1)
    minus_mult = spectrum_of_diagonal(y0).count(-3)
    one_cubed = plus_mult * (1**3)
    minus_three_cubed = minus_mult * ((-3) ** 3)
    reconstructed = one_cubed + minus_three_cubed
    y0_cubed = mul(mul(y0, y0), y0)
    tr_y0_cubed = trace(y0_cubed)
    checks.check(
        "spectrum-multiplicities",
        "Y_0 has six +1 eigenvalues and two -3 eigenvalues",
        plus_mult == 6 and minus_mult == 2,
    )
    checks.check(
        "reconstruct-6-minus-54",
        "6(1)^3 + 2(-3)^3 reconstructs as 6-54=-48",
        one_cubed == 6
        and minus_three_cubed == -54
        and reconstructed == 6 - 54
        and (6 - 54) == -48,
    )
    checks.check(
        "tr-y0-cubed",
        "matrix Tr(Y_0^3) equals the reconstructed integer -48",
        tr_y0_cubed == reconstructed and tr_y0_cubed == -48,
    )
    checks.check(
        "tr-y0-cubed-nonzero",
        "Tr(Y_0^3) != 0",
        tr_y0_cubed != 0,
    )
    mutation_tr_zero = tr_y0_cubed == 0
    checks.check(
        "mutation-tr-y0-cubed-zero",
        "hostile predicate Tr(Y_0^3)==0 fails",
        mutation_tr_zero is False,
    )

    y_oplus = block_diag(y0, scale(-1, y0))
    dim_oplus = len(y_oplus)
    tr_y_oplus_cubed = trace(mul(mul(y_oplus, y_oplus), y_oplus))
    minus_y0_cubed_trace = trace(mul(mul(scale(-1, y0), scale(-1, y0)), scale(-1, y0)))
    checks.check(
        "dim-oplus",
        "dim(H oplus H) = 16",
        dim_oplus == 16 and dim_oplus == dim_h + dim_h,
    )
    mutation_dim_eight = dim_oplus == 8
    checks.check(
        "mutation-dim-oplus-eight",
        "hostile predicate dim(H oplus H)==8 fails",
        mutation_dim_eight is False,
    )
    checks.check(
        "tr-y-oplus-cubed",
        "Tr(Y_oplus^3) = -48 + 48 = 0",
        minus_y0_cubed_trace == 48
        and tr_y0_cubed + minus_y0_cubed_trace == 0
        and tr_y_oplus_cubed == 0,
    )

    checks.check(
        "note-theorem-1",
        "the note states dim H = 8 and Tr(Y_0^3) = 6-54=-48 != 0",
        "dim H = 8" in normalized_note
        and "6 − 54 = −48" in note
        and "Tr(Y_0^3) = −48 ≠ 0" in note,
    )
    checks.check(
        "note-theorem-2",
        "the note states the complementary cancel on H oplus H at dimension 16",
        "Y_⊕ = Y_0 ⊕ (−Y_0)" in note
        and "Tr(Y_⊕^3) = −48 + 48 = 0" in note
        and "dim(H ⊕ H) = 16" in note,
    )
    checks.check(
        "note-theorem-3",
        "the note states that one 3-qubit Hilbert does not force Tr(Y^3)=0",
        "does not supply the complementary copy or force" in normalized_note
        and "The cancel is an extra matching." in normalized_note
        and "not supplied by having one 3-qubit Hilbert" in note,
    )
    checks.check(
        "note-theorem-4",
        "the note quotes Qubit M_2(C) and refuses a generation axiom",
        qubit_sentence in note
        and "Neither `Y_0` nor a second `C^8` is named" in note
        and "does not adopt a generation axiom" in normalized_note,
    )
    checks.check(
        "note-no-charge-naming",
        "the note does not perform U(1)_Y or PDG identification",
        "U(1)_Y" not in note and "PDG" not in note,
    )
    checks.check(
        "note-independence",
        "the note is independent of the dim-16-vs-C^2 and Hilbert-vs-M_3 holes",
        "independent of the comparison of dimension 16 with one-site" in normalized_note
        and "independent of the comparison of a Hilbert space with `M_3`" in normalized_note,
    )
    checks.check(
        "note-status",
        "machine status is bounded-support",
        "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the new note and the axiom memo only",
        AUDIT_INPUT_PATHS
        == (
            "docs/THREE_QUBIT_C8_CARRIES_Y0_CUBIC_CANCEL_STILL_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
