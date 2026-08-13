#!/usr/bin/env python3
"""Exact integer traces: second C^8 with -Y_0 cancels the cubic and is extra.

Identity gates call cubic_Y0() and cubic_Yplus(). Those functions compute
traces from constructed integer matrices. They do not return a stored target.
"""

from __future__ import annotations

import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/SECOND_C8_WITH_MINUS_Y0_CANCELS_CUBIC_AND_IS_EXTRA_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
PARENT_REL = (
    "docs/LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_"
    "NARROW_THEOREM_NOTE_2026-05-02.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/SECOND_C8_WITH_MINUS_Y0_CANCELS_CUBIC_AND_IS_EXTRA_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_"
    "NARROW_THEOREM_NOTE_2026-05-02.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def diag(values: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    n = len(values)
    return tuple(tuple(values[i] if i == j else 0 for j in range(n)) for i in range(n))


def mat_add(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    n = len(left)
    return tuple(tuple(left[i][j] + right[i][j] for j in range(n)) for i in range(n))


def mat_scale(
    scalar: int,
    matrix: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    n = len(matrix)
    return tuple(tuple(scalar * matrix[i][j] for j in range(n)) for i in range(n))


def matmul(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    n = len(left)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(n)) for j in range(n))
        for i in range(n)
    )


def mat_pow3(matrix: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    return matmul(matmul(matrix, matrix), matrix)


def trace(matrix: tuple[tuple[int, ...], ...]) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def rank_diag_projector(matrix: tuple[tuple[int, ...], ...]) -> int:
    return sum(1 for i in range(len(matrix)) if matrix[i][i] != 0)


def direct_sum(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    n = len(left)
    m = len(right)
    size = n + m
    rows = []
    for i in range(size):
        row = []
        for j in range(size):
            if i < n and j < n:
                row.append(left[i][j])
            elif i >= n and j >= n:
                row.append(right[i - n][j - n])
            else:
                row.append(0)
        rows.append(tuple(row))
    return tuple(rows)


def spectrum(matrix: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(matrix[i][i] for i in range(len(matrix)))


def pi_plus() -> tuple[tuple[int, ...], ...]:
    return diag((1, 1, 1, 1, 1, 1, 0, 0))


def pi_minus() -> tuple[tuple[int, ...], ...]:
    return diag((0, 0, 0, 0, 0, 0, 1, 1))


def Y_0() -> tuple[tuple[int, ...], ...]:
    return mat_add(pi_plus(), mat_scale(-3, pi_minus()))


def minus_Y_0() -> tuple[tuple[int, ...], ...]:
    return mat_scale(-1, Y_0())


def Y_plus() -> tuple[tuple[int, ...], ...]:
    return direct_sum(Y_0(), minus_Y_0())


def reconstructed_cubic_Y0() -> int:
    return 6 * (1**3) + 2 * ((-3) ** 3)


def cubic_Y0() -> int:
    return trace(mat_pow3(Y_0()))


def cubic_Yplus() -> int:
    return trace(mat_pow3(Y_plus()))


def dim_H() -> int:
    return len(Y_plus())


def onesite_qubit_dim() -> int:
    return 2


def predicate_single_block_cubic_vanishes() -> bool:
    return cubic_Y0() == 0


def predicate_onesite_M2_contains_Yplus() -> bool:
    return dim_H() <= onesite_qubit_dim()


def opposite_spectrum_length() -> int:
    return len(tuple(-value for value in spectrum(Y_0())))


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


def identity_gates_call_required_functions(source: str) -> bool:
    tree = ast.parse(source)
    required = {"cubic_Y0", "cubic_Yplus"}
    seen: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if isinstance(func, ast.Name) and func.id in required:
            seen.add(func.id)
    return seen == required


def audit_paths_literal(source: str) -> tuple[str, ...] | None:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue
        if node.targets[0].id != "AUDIT_INPUT_PATHS":
            continue
        if not isinstance(node.value, ast.Tuple):
            return None
        paths: list[str] = []
        for elt in node.value.elts:
            if not isinstance(elt, ast.Constant) or not isinstance(elt.value, str):
                return None
            paths.append(elt.value)
        return tuple(paths)
    return None


def main() -> int:
    checks = Checks()
    source = Path(__file__).read_text(encoding="utf-8")
    note = (ROOT / NOTE_REL).read_text(encoding="utf-8")
    parent = (ROOT / PARENT_REL).read_text(encoding="utf-8")
    axiom = (ROOT / AXIOM_REL).read_text(encoding="utf-8")
    note_n = normalize(note)
    parent_n = normalize(parent)
    axiom_n = normalize(axiom)

    plus = pi_plus()
    minus = pi_minus()
    y0 = Y_0()
    yplus = Y_plus()
    rebuilt = reconstructed_cubic_Y0()

    checks.check(
        "source-parent-ratio",
        "May 2 parent states the 1 : (-3) multiplicity ratio",
        "1 : (−3)" in parent or "1 : (-3)" in parent,
    )
    checks.check(
        "source-parent-no-sm-y",
        "May 2 parent keeps SM hypercharge identification out of scope",
        "identification with Standard Model hypercharge Y" in parent
        and "out of scope" in parent_n,
    )
    checks.check(
        "source-qubit-m2",
        "Qubit one-site domain is M_2(C) and names neither second C^8 nor Y_oplus",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom
        and "Y_⊕" not in axiom
        and "Y_oplus" not in axiom_n
        and "second C^8" not in axiom,
    )
    checks.check(
        "source-note-theorems",
        "note states the five theorems and the extra-object bound",
        all(
            phrase in note
            for phrase in (
                "Tr(Y_0^3) = −48 ≠ 0",
                "The complementary block cancels the cubic",
                "dim H = 16 > 2 = dim C^2",
                "complementary 8-carrier with opposite",
                "Do not identify `Y_⊕` with Standard Model hypercharge",
            )
        ),
    )
    checks.check(
        "source-note-negative-scope",
        "note adopts no generation axiom and does not close P-HY",
        "does not adopt that operator as an axiom" in note_n
        and "does not call the pair two generations" in note_n
        and "Do not claim that physical hypercharge (P-HY) is closed" in note
        and "Do not import PDG" in note_n
        and "phyanom" not in note
        and "c8carrier" not in note
        and "ranksplit" not in note,
    )
    checks.check(
        "projectors",
        "Pi_+ and Pi_- are complementary rank-(6,2) projectors on C^8",
        plus == matmul(plus, plus)
        and minus == matmul(minus, minus)
        and matmul(plus, minus) == diag((0,) * 8)
        and mat_add(plus, minus) == diag((1,) * 8)
        and rank_diag_projector(plus) == 6
        and rank_diag_projector(minus) == 2,
    )
    checks.check(
        "first-block-ratio",
        "Y_0 keeps the parent (6,2) spectrum 1 x6 and -3 x2",
        spectrum(y0) == (1, 1, 1, 1, 1, 1, -3, -3)
        and y0 == mat_add(plus, mat_scale(-3, minus))
        and trace(y0) == 0,
    )
    checks.check(
        "identity-cubic-Y0",
        "Tr(Y_0^3) equals reconstructed 6*(1)^3 + 2*(-3)^3",
        cubic_Y0() == rebuilt and rebuilt == 6 - 54 and cubic_Y0() != 0,
    )
    checks.check(
        "identity-cubic-Yplus",
        "Tr(Y_oplus^3) vanishes by the complementary block",
        cubic_Yplus() == 0
        and cubic_Yplus() == cubic_Y0() + trace(mat_pow3(minus_Y_0()))
        and spectrum(yplus)
        == (1, 1, 1, 1, 1, 1, -3, -3, -1, -1, -1, -1, -1, -1, 3, 3),
    )
    checks.check(
        "dim-extra",
        "dim H = 16 exceeds one-site C^2 and one C^8",
        dim_H() == 16 and dim_H() > onesite_qubit_dim() and dim_H() > 8,
    )
    checks.check(
        "minimality-opposite-octet",
        "opposite spectrum of Y_0 occupies eight eigenvalues",
        opposite_spectrum_length() == 8
        and tuple(-value for value in spectrum(y0)[:8]) == spectrum(yplus)[8:],
    )
    checks.check(
        "mutation-cubic-zero",
        "predicate Tr(Y_0^3)=0 fails because the cubic is 6-54",
        predicate_single_block_cubic_vanishes() is False and cubic_Y0() == 6 - 54,
    )
    checks.check(
        "mutation-m2-contains-yplus",
        "predicate one-site M_2 contains Y_oplus fails (dim 16 vs 2)",
        predicate_onesite_M2_contains_Yplus() is False
        and dim_H() == 16
        and onesite_qubit_dim() == 2,
    )
    checks.check(
        "identity-gates-call-cubics",
        "identity gates call cubic_Y0() and cubic_Yplus()",
        identity_gates_call_required_functions(source),
    )
    literal = audit_paths_literal(source)
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the new note, the May 2 note, and the axiom memo",
        literal == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            NOTE_REL,
            PARENT_REL,
            AXIOM_REL,
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
