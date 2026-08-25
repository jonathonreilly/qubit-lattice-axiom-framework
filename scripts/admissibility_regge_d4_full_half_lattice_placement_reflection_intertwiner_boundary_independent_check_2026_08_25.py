#!/usr/bin/env python3
"""Independent exact checker for the Block 196 singleton-grade Ward gate.

This file does not import the primary Block 196 runner.  It reconstructs the
frozen row-face coefficient systems directly from the raw D4 incidence
formula, checks all 15 directions and four singleton grades over ``QQ``, and
verifies the support-independent mixed-edge corner contradiction.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import subprocess

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PREREG_COMMIT = "3241d452c580f7a09597c3e40070ab95669507bd"
PREREG_GOAL = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block196-regge-d4-placement-reflection-20260825/"
    "GOAL.md"
)
ZERO = (0, 0, 0, 0)
AXES = tuple(range(4))
UNITS = tuple(
    tuple(int(axis == slot) for slot in AXES)
    for axis in AXES
)
COMPONENTS = tuple((axis, axis) for axis in AXES) + tuple(
    combinations(AXES, 2)
)
DIRS15 = tuple(
    direction
    for direction in product((0, 1), repeat=4)
    if any(direction)
)


@dataclass
class Reporter:
    passed: int = 0
    failed: int = 0

    def check(self, name: str, condition: bool, detail: str) -> None:
        status = "PASS" if bool(condition) else "FAIL"
        self.passed += int(bool(condition))
        self.failed += int(not bool(condition))
        print(f"{status} {name}: {detail}")

    def total(self) -> None:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        stderr=subprocess.DEVNULL,
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


def add_exp(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


def sub_exp(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(a - b for a, b in zip(left, right))


def row_face(direction: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    """Vertices s<=d of the preregistered positive-direction row face."""
    return tuple(
        product(*(((0, 1) if value else (0,)) for value in direction))
    )


def coefficient_system(
    direction: tuple[int, ...], grade: int
) -> tuple[sp.SparseMatrix, sp.SparseMatrix, tuple[tuple[int, tuple[int, ...]], ...]]:
    """Build one exact rational singleton-grade coefficient system.

    Diagonal tensor variables have been invertibly rescaled by 2,
    off-diagonal variables by sqrt(2), and the target by sqrt(|d|).  These
    changes preserve rank and consistency and leave only 0,+1,-1 entries.
    """
    support = row_face(direction)
    unknowns = tuple(
        (component, shift)
        for component in COMPONENTS
        for shift in support
    )
    entries: dict[tuple[tuple[int, tuple[int, ...]], int], int] = {}
    target: dict[tuple[int, tuple[int, ...]], int] = {}

    def insert(
        row: tuple[int, tuple[int, ...]], column: int, value: int
    ) -> None:
        entries[row, column] = entries.get((row, column), 0) + value

    for column, (component, shift) in enumerate(unknowns):
        left, right = component
        if left == right:
            # (1-z_left^-1) on the diagonal D4 tensor slot.
            insert((left, shift), column, 1)
            insert((left, sub_exp(shift, UNITS[left])), column, -1)
            continue

        # (z_right-1) in gauge column left, and conversely.
        insert((left, add_exp(shift, UNITS[right])), column, 1)
        insert((left, shift), column, -1)
        insert((right, add_exp(shift, UNITS[left])), column, 1)
        insert((right, shift), column, -1)

    if direction[grade]:
        target[grade, direction] = 1
        target[grade, ZERO] = -1

    row_labels = tuple(
        sorted({row for row, _column in entries} | set(target))
    )
    row_index = {row: index for index, row in enumerate(row_labels)}
    matrix = sp.MutableSparseMatrix(
        len(row_labels),
        len(unknowns),
        {
            (row_index[row], column): value
            for (row, column), value in entries.items()
            if value
        },
    )
    rhs = sp.MutableSparseMatrix(
        len(row_labels),
        1,
        {
            (row_index[row], 0): value
            for row, value in target.items()
            if value
        },
    )
    return matrix, rhs, row_labels


def expected_case(
    weight: int, active: bool
) -> tuple[int, int, int, int]:
    """Return variables, coefficient rows, rank, and augmented rank."""
    if weight == 1:
        return (20, 36, 20, 20)
    if weight == 2:
        return (40, 64, 40, 41 if active else 40)
    if weight == 3:
        return (80, 112, 80, 81 if active else 80)
    if weight == 4:
        return (160, 192, 158, 159)
    raise AssertionError(f"unexpected direction weight {weight}")


def corner_certificate(
    matrix: sp.SparseMatrix,
    rhs: sp.SparseMatrix,
    row_labels: tuple[tuple[int, tuple[int, ...]], ...],
) -> tuple[bool, sp.Expr]:
    """Return the 16-term d=1100,g=0 left-null certificate."""
    left, right = 0, 1
    spectators = (2, 3)
    weights: dict[tuple[int, tuple[int, ...]], int] = {
        (left, sub_exp(ZERO, UNITS[left])): 1,
        (left, ZERO): 1,
        (left, UNITS[left]): 1,
        (left, add_exp(UNITS[right], UNITS[right])): -1,
        (right, sub_exp(ZERO, UNITS[right])): -1,
        (right, ZERO): -1,
        (right, UNITS[right]): -1,
        (right, add_exp(UNITS[left], UNITS[left])): 1,
    }
    for spectator in spectators:
        weights[left, UNITS[spectator]] = 1
        weights[left, add_exp(UNITS[left], UNITS[spectator])] = 1
        weights[right, UNITS[spectator]] = -1
        weights[right, add_exp(UNITS[right], UNITS[spectator])] = -1

    vector = sp.Matrix(
        1,
        len(row_labels),
        lambda _row, column: weights.get(row_labels[column], 0),
    )
    annihilates = vector * matrix == sp.zeros(1, matrix.cols)
    return bool(annihilates), sp.simplify((vector * rhs)[0])


def analytic_corner() -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    """Reconstruct the two regular-Laurent boundary values exactly."""
    z0, z1 = sp.symbols("z0 z1")
    branch_from_column_zero = sp.cancel(
        ((z1 - 1) / sp.sqrt(2)) / (sp.sqrt(2) * (z1 - 1))
    )
    branch_from_column_one = sp.cancel(
        sp.Integer(0) / (sp.sqrt(2) * (z0 - 1))
    )
    return (
        branch_from_column_zero,
        branch_from_column_one,
        sp.limit(branch_from_column_zero, z1, 1),
        sp.limit(branch_from_column_one, z0, 1),
    )


def main() -> int:
    reporter = Reporter()
    try:
        resolved = git_output("rev-parse", f"{PREREG_COMMIT}^{{commit}}")
        goal = git_output("show", f"{PREREG_COMMIT}:{PREREG_GOAL}")
        prereg_markers = (
            "exactly 3200 coefficients",
            "four 800-variable systems",
            "M^(g) Gamma_D=G_R E_gg",
            "No fallback support",
        )
        reporter.check(
            "PREREG_BIND",
            resolved == PREREG_COMMIT
            and is_ancestor(PREREG_COMMIT)
            and all(marker in goal for marker in prereg_markers),
            f"commit={resolved[:12]}; ancestor={is_ancestor(PREREG_COMMIT)}",
        )

        observed: dict[
            tuple[int, bool], set[tuple[int, int, int, int]]
        ] = {}
        counts: dict[tuple[int, bool], int] = {}
        grade_rank = [0] * 4
        grade_inconsistent = [0] * 4
        inconsistent = 0
        witness_data = None

        for direction in DIRS15:
            weight = sum(direction)
            for grade in AXES:
                active = bool(direction[grade])
                matrix, rhs, row_labels = coefficient_system(direction, grade)
                rank = matrix.rank()
                augmented = matrix.row_join(rhs).rank()
                datum = (matrix.cols, matrix.rows, rank, augmented)
                key = (weight, active)
                observed.setdefault(key, set()).add(datum)
                counts[key] = counts.get(key, 0) + 1
                grade_rank[grade] += rank
                grade_inconsistent[grade] += int(augmented != rank)
                inconsistent += int(augmented != rank)
                if direction == (1, 1, 0, 0) and grade == 0:
                    witness_data = (matrix, rhs, row_labels, rank, augmented)

        expected_counts = {
            (1, False): 12,
            (1, True): 4,
            (2, False): 12,
            (2, True): 12,
            (3, False): 4,
            (3, True): 12,
            (4, True): 4,
        }
        table_ok = counts == expected_counts
        for key, count in sorted(counts.items()):
            expected = expected_case(*key)
            values = observed[key]
            table_ok = table_ok and values == {expected}
            print(
                "DATA RANK_ORBIT "
                f"weight={key[0]} active={key[1]} count={count} "
                f"observed={sorted(values)}"
            )
        reporter.check(
            "EXACT_60_CASE_CENSUS",
            len(DIRS15) == 15
            and sum(counts.values()) == 60
            and table_ok,
            f"directions={len(DIRS15)}; cases={sum(counts.values())}",
        )
        reporter.check(
            "FOUR_GRADE_GLOBAL_RANKS",
            grade_rank == [798] * 4
            and grade_inconsistent == [7] * 4
            and inconsistent == 28,
            "rank_by_grade="
            f"{grade_rank}; inconsistent_by_grade={grade_inconsistent}; "
            f"total_inconsistent={inconsistent}",
        )

        if witness_data is None:
            raise AssertionError("d=1100,g=0 witness was not constructed")
        matrix, rhs, row_labels, rank, augmented = witness_data
        annihilates, target_value = corner_certificate(
            matrix, rhs, row_labels
        )
        reporter.check(
            "LEFT_NULL_WITNESS",
            rank == 40
            and augmented == 41
            and annihilates
            and target_value == -1,
            "d=1100,g=0: rank=40 augmented=41; "
            f"y^T A=0, y^T b={target_value} after exact target rescaling",
        )

        branch_zero, branch_one, corner_zero, corner_one = analytic_corner()
        reporter.check(
            "REGULAR_LAURENT_CORNER_CONTRADICTION",
            branch_zero == sp.Rational(1, 2)
            and branch_one == 0
            and corner_zero == sp.Rational(1, 2)
            and corner_one == 0
            and corner_zero != corner_one,
            "M_01(1,z1)=1/2 while M_01(z0,1)=0; "
            f"common-corner limits={corner_zero}/{corner_one}",
        )
    except Exception as exc:  # Fail closed and preserve the TOTAL line.
        reporter.check(
            "UNCAUGHT_EXCEPTION",
            False,
            f"{type(exc).__name__}: {exc}",
        )

    reporter.total()
    return 1 if reporter.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
