#!/usr/bin/env python3
"""Block 126: exact dual-family time dressing and the adjointness wall.

The runner compares the monodromy-conjugated family inherited from the solve
lane with a one-super-step SHIFT-conjugated family.  All scientific arithmetic
is exact over Q(i,rho); wall-clock timing is the sole floating-point quantity.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import math
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_spatial_dressing_invisibility_2026_08_17 as prior


R = sp.Rational
I = sp.I
RHO = prior.RHO
SHEARS = prior.SHEARS
block123 = prior.block123
block121 = prior.block121
block119 = prior.block119
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_TIME_DRESSING_ADJOINTNESS_WALL_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_DRESSING_INVISIBILITY_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_spatial_dressing_"
    "invisibility_2026_08_17.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_spatial_dressing_"
    "invisibility_2026_08_17.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TIME_DRESSING_ADJOINTNESS_WALL_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_DRESSING_INVISIBILITY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_spatial_dressing_invisibility_2026_08_17.py",
    "logs/runner-cache/admissibility_dirac_kahler_spatial_dressing_invisibility_2026_08_17.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "00fe13b1f48fd235b2c2723aa5db06601508ba02"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block125-spatial-dressing-invisibility-20260817"
)
PARENT_COMMIT = "ff85cc8c6a991b2926b9ac5cb5168f2587bc0c0d"
PARENT_NOTE_BLOB = "4968f83c5b31d80f6fba31b45460491273f72bb6"
PARENT_RUNNER_BLOB = "3b5321af9ee7f958b6dc404ce250c3433471fae6"
PARENT_CACHE_BLOB = "754f7bfc0958e9082cd9f5693395539a5b02daaf"
ANCESTOR_COMMITS = (
    (124, "da2b9020e9f15ac55640ef87a0798a78e3c9a0d0"),
    (123, "954322e0e085d6c3133ce24dca49db2efbd7d0a6"),
    (122, "f067b99be7eb49fc46ea8dffccab5e20e6052d88"),
    (121, "1714abeefcf3763c0bfe001f30fd14521c538622"),
    (120, "1c2386bf3df420707fd2ecb2d7ec84002ba40ad1"),
    (119, "33fd2d21558604718f3a88713fe1976aff8f9dbb"),
    (118, "fdd1883c54ca8cc14b1337cc1edc249792d5dab2"),
    (117, "f800356aec0989b6e0fa80ed43274794243b1ca2"),
    (116, "c36d11e4e8d927c6fc31f0a8b579d4bd15f4fa43"),
    (115, "c78301fef7521d0518f485f1bf9266983c9e516a"),
    (114, "75026e71cfbd44ed665ddc41c22ebaa722720ea9"),
    (113, "e76893eb7204d1d727a3ab8838fb3fada3f45dfc"),
    (112, "385a6ba5b1594f20e5d4eebba9da68d8e72abc10"),
    (111, "b04e7c8747b09734711cfcd2bfab961bd12e81ad"),
    (110, "d6761278fca9cac617200792473a8f4da3a6cfff"),
    (109, "ad84cfcc857a65285389ba93b47cd7b718589be5"),
    (108, "8afe8dff5ccf531208238af0aaaec1f547d73874"),
    (107, "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"),
    (106, "22d6d90ec2279e5868c9c825149b2a20beea3797"),
    (105, "d06066c2b908aaca0779625d831dfb10620cf34d"),
    (104, "7fe07db6c03fad1191893c942f708c5cb9a54c43"),
    (103, "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"),
)

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_visibility",
    "break_family_a_rank",
    "break_kernel_member",
    "claim_zero_compression",
    "break_adjointness_residual",
    "claim_joint_solution",
    "claim_injectivity",
    "break_isolation",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
    "claim_axiom_amendment",
    "claim_wall_absolute",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    return git_output("rev-parse", f"{commit}:{path}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    expected_parent = (
        "0" * 40 if mutation == "stale_parent_authority" else PARENT_NOTE_BLOB
    )
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        **{
            f"ancestor_{number}": is_ancestor(commit, "HEAD")
            for number, commit in ANCESTOR_COMMITS
        },
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
    }


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


def exact_digest(*payload: object) -> str:
    return hashlib.sha256(sp.srepr(payload).encode("utf-8")).hexdigest()[:16]


G = tuple[Fraction, Fraction]
Q = tuple[G, G]
QMatrix = tuple[tuple[Q, ...], ...]
GZERO: G = (Fraction(0), Fraction(0))
GONE: G = (Fraction(1), Fraction(0))
QZERO: Q = (GZERO, GZERO)
QONE: Q = (GONE, GZERO)


def gadd(left: G, right: G) -> G:
    return left[0] + right[0], left[1] + right[1]


def gneg(value: G) -> G:
    return -value[0], -value[1]


def gsub(left: G, right: G) -> G:
    return gadd(left, gneg(right))


def gmul(left: G, right: G) -> G:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def ginv(value: G) -> G:
    denominator = value[0] * value[0] + value[1] * value[1]
    if denominator == 0:
        raise ZeroDivisionError("zero Gaussian denominator")
    return value[0] / denominator, -value[1] / denominator


def gdiv(left: G, right: G) -> G:
    return gmul(left, ginv(right))


def gstar(value: G) -> G:
    return value[0], -value[1]


def fraction(value: sp.Expr) -> Fraction:
    value = sp.factor(value)
    if not bool(value.is_Rational):
        raise AssertionError(f"non-rational Gaussian coordinate: {value}")
    return Fraction(int(value.p), int(value.q))


def gaussian(value: sp.Expr) -> G:
    real, imag = sp.expand_complex(value).as_real_imag()
    return fraction(real), fraction(imag)


@dataclass(frozen=True)
class QuadraticField:
    polynomial: sp.Poly
    relation_constant: G
    relation_linear: G

    @classmethod
    def from_poly(cls, polynomial: sp.Poly) -> "QuadraticField":
        leading, linear, constant = polynomial.all_coeffs()
        return cls(
            polynomial,
            gaussian(-constant / leading),
            gaussian(-linear / leading),
        )

    def add(self, left: Q, right: Q) -> Q:
        return gadd(left[0], right[0]), gadd(left[1], right[1])

    def neg(self, value: Q) -> Q:
        return gneg(value[0]), gneg(value[1])

    def sub(self, left: Q, right: Q) -> Q:
        return self.add(left, self.neg(right))

    def mul(self, left: Q, right: Q) -> Q:
        cross = gmul(left[1], right[1])
        return (
            gadd(gmul(left[0], right[0]), gmul(cross, self.relation_constant)),
            gadd(
                gadd(gmul(left[0], right[1]), gmul(left[1], right[0])),
                gmul(cross, self.relation_linear),
            ),
        )

    def inv(self, value: Q) -> Q:
        companion = gadd(value[0], gmul(value[1], self.relation_linear))
        denominator = gsub(
            gmul(value[0], companion),
            gmul(gmul(value[1], value[1]), self.relation_constant),
        )
        return gdiv(companion, denominator), gdiv(gneg(value[1]), denominator)

    def div(self, left: Q, right: Q) -> Q:
        return self.mul(left, self.inv(right))

    def star(self, value: Q) -> Q:
        return gstar(value[0]), gstar(value[1])

    def parse(self, value: sp.Expr) -> Q:
        reduced = prior.red(value, self.polynomial)
        expression = sp.Poly(sp.expand(reduced), RHO, domain=sp.QQ_I)
        return (
            gaussian(expression.coeff_monomial(1)),
            gaussian(expression.coeff_monomial(RHO)),
        )

    def matrix(self, source: sp.MatrixBase) -> QMatrix:
        source = sp.Matrix(source)
        return tuple(
            tuple(self.parse(source[row, column]) for column in range(source.cols))
            for row in range(source.rows)
        )

    def rank(self, source: tuple[tuple[Q, ...], ...]) -> int:
        if not source:
            return 0
        work = [list(row) for row in source]
        row = 0
        for column in range(len(work[0])):
            pivot = next(
                (
                    candidate
                    for candidate in range(row, len(work))
                    if work[candidate][column] != QZERO
                ),
                None,
            )
            if pivot is None:
                continue
            work[row], work[pivot] = work[pivot], work[row]
            inverse = self.inv(work[row][column])
            work[row] = [self.mul(value, inverse) for value in work[row]]
            for other in range(len(work)):
                if other == row:
                    continue
                factor = work[other][column]
                if factor == QZERO:
                    continue
                work[other] = [
                    self.sub(left, self.mul(factor, right))
                    for left, right in zip(work[other], work[row])
                ]
            row += 1
            if row == len(work):
                break
        return row

    def expression(self, value: Q) -> sp.Expr:
        def gaussian_expression(item: G) -> sp.Expr:
            return (
                R(item[0].numerator, item[0].denominator)
                + I * R(item[1].numerator, item[1].denominator)
            )

        return sp.expand(
            gaussian_expression(value[0]) + gaussian_expression(value[1]) * RHO
        )

    def text(self, value: Q) -> str:
        return str(self.expression(value))


def qmat_mul(field: QuadraticField, left: QMatrix, right: QMatrix) -> QMatrix:
    if len(left[0]) != len(right):
        raise AssertionError("quadratic matrix product shape")
    rows, inner, columns = len(left), len(right), len(right[0])
    result: list[tuple[Q, ...]] = []
    for row in range(rows):
        target_row: list[Q] = []
        for column in range(columns):
            value = QZERO
            for index in range(inner):
                if left[row][index] != QZERO and right[index][column] != QZERO:
                    value = field.add(
                        value, field.mul(left[row][index], right[index][column])
                    )
            target_row.append(value)
        result.append(tuple(target_row))
    return tuple(result)


def qmat_add(field: QuadraticField, left: QMatrix, right: QMatrix) -> QMatrix:
    return tuple(
        tuple(field.add(a, b) for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def qmat_sub(field: QuadraticField, left: QMatrix, right: QMatrix) -> QMatrix:
    return tuple(
        tuple(field.sub(a, b) for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def qmat_scale(field: QuadraticField, scalar: Q, source: QMatrix) -> QMatrix:
    return tuple(
        tuple(field.mul(scalar, value) for value in row) for row in source
    )


def qmat_adjoint(field: QuadraticField, source: QMatrix) -> QMatrix:
    return tuple(
        tuple(field.star(source[column][row]) for column in range(len(source)))
        for row in range(len(source[0]))
    )


def qmat_flatten(source: QMatrix) -> tuple[Q, ...]:
    return tuple(value for row in source for value in row)


def qmat_columns(matrices: tuple[QMatrix, ...]) -> tuple[tuple[Q, ...], ...]:
    columns = tuple(qmat_flatten(matrix) for matrix in matrices)
    return tuple(
        tuple(column[row] for column in columns) for row in range(len(columns[0]))
    )


def qmat_zero(source: QMatrix) -> bool:
    return all(value == QZERO for row in source for value in row)


def qmat_identity(size: int) -> QMatrix:
    return tuple(
        tuple(QONE if row == column else QZERO for column in range(size))
        for row in range(size)
    )


def qmat_rref(
    field: QuadraticField, source: QMatrix
) -> tuple[QMatrix, tuple[int, ...]]:
    work = [list(row) for row in source]
    if not work:
        return tuple(), tuple()
    pivot_row = 0
    pivots: list[int] = []
    for column in range(len(work[0])):
        pivot = next(
            (
                candidate
                for candidate in range(pivot_row, len(work))
                if work[candidate][column] != QZERO
            ),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = field.inv(work[pivot_row][column])
        work[pivot_row] = [
            field.mul(value, inverse) for value in work[pivot_row]
        ]
        for other in range(len(work)):
            if other == pivot_row:
                continue
            factor = work[other][column]
            if factor == QZERO:
                continue
            work[other] = [
                field.sub(left, field.mul(factor, right))
                for left, right in zip(work[other], work[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break
    return tuple(tuple(row) for row in work), tuple(pivots)


def operator_leakage(
    field: QuadraticField, y: QMatrix, operator: QMatrix
) -> QMatrix:
    bra = qmat_adjoint(field, y)
    norm = qmat_mul(field, bra, y)[0][0]
    projector = qmat_scale(
        field, field.inv(norm), qmat_mul(field, y, bra)
    )
    complement = qmat_sub(field, qmat_identity(8), projector)
    return qmat_mul(field, qmat_mul(field, bra, operator), complement)


def family_leakage_matrix(
    field: QuadraticField, y: QMatrix, family: tuple[QMatrix, ...]
) -> QMatrix:
    columns = tuple(operator_leakage(field, y, operator)[0] for operator in family)
    return tuple(
        tuple(column[row] for column in columns) for row in range(8)
    )


def rational_scalar(value: sp.Rational) -> Q:
    return (
        (Fraction(int(value.p), int(value.q)), Fraction(0)),
        GZERO,
    )


def weighted_operator(
    field: QuadraticField,
    weights: sp.Matrix,
    family: tuple[QMatrix, ...],
) -> QMatrix:
    result = tuple(tuple(QZERO for _ in range(8)) for _ in range(8))
    for weight, member in zip(weights, family):
        result = qmat_add(field, result, qmat_scale(field, rational_scalar(weight), member))
    return result


def field_weighted_operator(
    field: QuadraticField,
    weights: tuple[Q, ...],
    family: tuple[QMatrix, ...],
) -> QMatrix:
    result = tuple(tuple(QZERO for _ in range(8)) for _ in range(8))
    for weight, member in zip(weights, family):
        result = qmat_add(field, result, qmat_scale(field, weight, member))
    return result


class RationalRowSpace:
    def __init__(self, columns: int) -> None:
        self.columns = columns
        self.rows: dict[int, tuple[Fraction, ...]] = {}
        self.witness_rows: list[tuple[Fraction, ...]] = []

    @property
    def rank(self) -> int:
        return len(self.rows)

    def add(self, source: tuple[Fraction, ...]) -> bool:
        if len(source) != self.columns:
            raise AssertionError("rational constraint width")
        row = list(source)
        for pivot in sorted(self.rows):
            factor = row[pivot]
            if factor:
                row = [
                    left - factor * right
                    for left, right in zip(row, self.rows[pivot])
                ]
        pivot = next((index for index, value in enumerate(row) if value), None)
        if pivot is None:
            return False
        scale = row[pivot]
        normalized = tuple(value / scale for value in row)
        for old_pivot, basis in tuple(self.rows.items()):
            factor = basis[pivot]
            if factor:
                self.rows[old_pivot] = tuple(
                    left - factor * right
                    for left, right in zip(basis, normalized)
                )
        self.rows[pivot] = normalized
        self.witness_rows.append(source)
        return True

    def extend(self, other: "RationalRowSpace") -> None:
        for row in other.witness_rows:
            self.add(row)

    def matrix(self) -> sp.Matrix:
        return sp.Matrix(
            tuple(
                tuple(
                    R(value.numerator, value.denominator)
                    for value in self.rows[pivot]
                )
                for pivot in sorted(self.rows)
            )
        )

    def witness_matrix(self) -> sp.Matrix:
        return sp.Matrix(
            tuple(
                tuple(R(value.numerator, value.denominator) for value in row)
                for row in self.witness_rows
            )
        )


def add_q_constraints(space: RationalRowSpace, coefficients: tuple[Q, ...]) -> None:
    for component in range(4):
        row = tuple(value[component // 2][component % 2] for value in coefficients)
        if any(row):
            space.add(row)


def operator_row_space(families: tuple[tuple[QMatrix, ...], ...]) -> RationalRowSpace:
    count = len(families[0])
    result = RationalRowSpace(count)
    for family in families:
        for entry in range(64):
            values = tuple(qmat_flatten(member)[entry] for member in family)
            add_q_constraints(result, values)
    return result


def family_constraints(
    field: QuadraticField,
    y: QMatrix,
    family: tuple[QMatrix, ...],
    reflected: tuple[QMatrix, ...],
) -> tuple[RationalRowSpace, RationalRowSpace]:
    """Return exact QQ leakage and K_Theta-adjointness row spaces."""
    count = len(family)
    if len(reflected) != count:
        raise AssertionError("reflection family width")
    descent = RationalRowSpace(count)
    adjoint = RationalRowSpace(count)
    bra = qmat_adjoint(field, y)
    gram = qmat_mul(field, y, bra)
    rows = tuple(qmat_mul(field, bra, operator)[0] for operator in family)
    for output in range(1, 8):
        coefficients = tuple(
            field.sub(
                field.mul(row[output], bra[0][0]),
                field.mul(row[0], bra[0][output]),
            )
            for row in rows
        )
        add_q_constraints(descent, coefficients)
    residuals = tuple(
        qmat_sub(
            field,
            qmat_mul(field, gram, operator),
            qmat_mul(field, qmat_adjoint(field, theta_operator), gram),
        )
        for operator, theta_operator in zip(family, reflected)
    )
    for row in range(8):
        for column in range(8):
            add_q_constraints(
                adjoint,
                tuple(residual[row][column] for residual in residuals),
            )
    return descent, adjoint


def canonical_kernel_vector(vector: sp.Matrix) -> sp.Matrix:
    denominators = [int(value.q) for value in vector]
    scale = math.lcm(*denominators)
    integers = [int(value * scale) for value in vector]
    divisor = math.gcd(*[abs(value) for value in integers if value])
    integers = [value // divisor for value in integers]
    first = next(value for value in integers if value)
    if first < 0:
        integers = [-value for value in integers]
    return sp.Matrix(integers)


def quotient_compression(
    field: QuadraticField, y: QMatrix, operator: QMatrix
) -> Q:
    bra = qmat_adjoint(field, y)
    numerator = qmat_mul(field, qmat_mul(field, bra, operator), y)[0][0]
    denominator = qmat_mul(field, bra, y)[0][0]
    return field.div(numerator, denominator)


def reflection_adjointness_residual(
    field: QuadraticField,
    y: QMatrix,
    operator: QMatrix,
    reflected_operator: QMatrix,
) -> QMatrix:
    bra = qmat_adjoint(field, y)
    gram = qmat_mul(field, y, bra)
    return qmat_sub(
        field,
        qmat_mul(field, gram, operator),
        qmat_mul(field, qmat_adjoint(field, reflected_operator), gram),
    )


def first_nonzero(source: QMatrix) -> tuple[int, int, Q] | None:
    for row in range(len(source)):
        for column in range(len(source[row])):
            if source[row][column] != QZERO:
                return row, column, source[row][column]
    return None


def mode_monodromy() -> sp.Matrix:
    """The solve lane's pinned full antiperiodic monodromy on cut modes."""
    old = sp.zeros(8)
    for source in range(8):
        old[(source + 1) % 8, source] = -1 if source == 7 else 1
    cut = block119.cut_shift()
    result = cut * old * cut.T
    if result**8 != -sp.eye(8) or result.inv(method="DM") != -result**7:
        raise AssertionError("full antiperiodic mode monodromy")
    transform = block123.spatial_fourier()
    restricted = prior.momentum_diagonal_blocks(
        block123.antiperiodic_time_shift(), transform, cut
    )
    if any(matrix != result for matrix in restricted):
        raise AssertionError("full monodromy must match every momentum restriction")
    return result


def one_super_step_shifts() -> tuple[sp.Matrix, ...]:
    """Return the checker-pinned one-super-step time lift at each momentum.

    Kept separate from ``mode_monodromy`` so the theorem displays and tests
    the lift convention rather than silently identifying it with the full
    monodromy.
    """
    lift = sp.zeros(32)
    for fine_slice in range(8):
        target_slice = (fine_slice + 2) % 8
        sign = -1 if fine_slice + 2 > 7 else 1
        for spatial_site in range(4):
            lift[4 * target_slice + spatial_site, 4 * fine_slice + spatial_site] = sign
    inverse = lift.inv(method="DM")
    if lift * inverse != sp.eye(32) or inverse * lift != sp.eye(32):
        raise AssertionError("exact one-super-step lift inverse")
    return (lift,) * 4


def momentum_projectors() -> tuple[sp.Matrix, ...]:
    """Checker-pinned spatial momentum projectors on the four-site slice."""
    cycle = sp.zeros(4)
    for spatial_site in range(4):
        cycle[spatial_site, (spatial_site - 1) % 4] = 1
    return tuple(
        (
            R(1, 4)
            * sum(
                (
                    (I ** ((-momentum * power) % 4)) * cycle**power
                    for power in range(4)
                ),
                sp.zeros(4),
            )
        ).applyfunc(sp.expand)
        for momentum in range(4)
    )


def momentum_block(source: sp.Matrix, momentum: int, fine_slices: int) -> sp.Matrix:
    """Apply the checker-pinned full-lattice-to-momentum contraction."""
    projector = momentum_projectors()[momentum]
    return sp.Matrix(
        fine_slices,
        fine_slices,
        lambda row, column: sp.expand(
            sum(
                projector[x, y] * source[4 * row + y, 4 * column + x]
                for x in range(4)
                for y in range(4)
            )
        ),
    )


@dataclass(frozen=True)
class ModeFamilyResult:
    momentum: int
    field: QuadraticField
    y: QMatrix
    family: tuple[QMatrix, ...]
    reflected: tuple[QMatrix, ...]
    raw_rank: int
    span_rank: int
    pairwise_distinct: bool
    leakage: QMatrix
    leakage_rank: int
    leakage_pivots: tuple[int, ...]
    descent: RationalRowSpace
    adjoint: RationalRowSpace
    joint: RationalRowSpace
    descent_kernel: tuple[sp.Matrix, ...]
    joint_kernel: tuple[sp.Matrix, ...]


@dataclass(frozen=True)
class AggregateResult:
    count: int
    span_rank: int
    descent_rank: int
    adjoint_rank: int
    joint_rank: int
    descent_kernel: tuple[sp.Matrix, ...]
    joint_kernel: tuple[sp.Matrix, ...]
    joint_operator_empty: bool
    descent_witness: sp.Matrix
    joint_witness: sp.Matrix


@dataclass(frozen=True)
class FixtureResult:
    shear: sp.Rational
    sectors: tuple[object, ...]
    thetas: tuple[sp.Matrix, ...]
    monodromy: sp.Matrix
    shifts: tuple[sp.Matrix, ...]
    family_a: tuple[ModeFamilyResult, ...]
    family_b: tuple[ModeFamilyResult, ...]
    aggregate_a: AggregateResult
    aggregate_b: AggregateResult
    aggregate_union: AggregateResult
    aggregate_two_time: AggregateResult


def make_mode_result(
    momentum: int,
    sector: object,
    theta_source: sp.Matrix,
    raw_source: tuple[sp.Matrix, ...],
) -> ModeFamilyResult:
    field = QuadraticField.from_poly(sector.polynomial)
    theta = field.matrix(theta_source)
    y = field.matrix(sector.y)
    raw = tuple(field.matrix(member) for member in raw_source)
    dressed = tuple(
        qmat_mul(field, qmat_mul(field, theta, member), theta) for member in raw
    )
    family = raw + dressed
    reflected = dressed + raw
    leakage = family_leakage_matrix(field, y, family)
    _, leakage_pivots = qmat_rref(field, leakage)
    descent, adjoint = family_constraints(field, y, family, reflected)
    joint = RationalRowSpace(len(family))
    joint.extend(descent)
    joint.extend(adjoint)
    descent_matrix = descent.matrix()
    joint_matrix = joint.matrix()
    return ModeFamilyResult(
        momentum=momentum,
        field=field,
        y=y,
        family=family,
        reflected=reflected,
        raw_rank=field.rank(qmat_columns(raw)),
        span_rank=field.rank(qmat_columns(family)),
        pairwise_distinct=all(
            family[left] != family[right]
            for left in range(len(family))
            for right in range(left)
        ),
        leakage=leakage,
        leakage_rank=len(leakage_pivots),
        leakage_pivots=leakage_pivots,
        descent=descent,
        adjoint=adjoint,
        joint=joint,
        descent_kernel=tuple(descent_matrix.nullspace()),
        joint_kernel=tuple(joint_matrix.nullspace()),
    )


def aggregate_results(
    families: tuple[tuple[QMatrix, ...], ...],
    reflected: tuple[tuple[QMatrix, ...], ...],
    sectors: tuple[object, ...],
) -> AggregateResult:
    count = len(families[0])
    descent = RationalRowSpace(count)
    adjoint = RationalRowSpace(count)
    for family, theta_family, sector in zip(families, reflected, sectors):
        field = QuadraticField.from_poly(sector.polynomial)
        local_descent, local_adjoint = family_constraints(
            field, field.matrix(sector.y), family, theta_family
        )
        descent.extend(local_descent)
        adjoint.extend(local_adjoint)
    joint = RationalRowSpace(count)
    joint.extend(descent)
    joint.extend(adjoint)
    operators = operator_row_space(families)
    joint_plus_operators = RationalRowSpace(count)
    joint_plus_operators.extend(joint)
    joint_plus_operators.extend(operators)
    descent_matrix = descent.matrix()
    joint_matrix = joint.matrix()
    return AggregateResult(
        count=count,
        span_rank=operators.rank,
        descent_rank=descent.rank,
        adjoint_rank=adjoint.rank,
        joint_rank=joint.rank,
        descent_kernel=tuple(descent_matrix.nullspace()),
        joint_kernel=tuple(joint_matrix.nullspace()),
        joint_operator_empty=joint_plus_operators.rank == joint.rank,
        descent_witness=descent.witness_matrix(),
        joint_witness=joint.witness_matrix(),
    )


def union_mode_families(
    left: tuple[ModeFamilyResult, ...],
    right: tuple[ModeFamilyResult, ...],
) -> tuple[tuple[QMatrix, ...], ...]:
    return tuple(a.family + b.family for a, b in zip(left, right))


def union_reflected_families(
    left: tuple[ModeFamilyResult, ...],
    right: tuple[ModeFamilyResult, ...],
) -> tuple[tuple[QMatrix, ...], ...]:
    return tuple(a.reflected + b.reflected for a, b in zip(left, right))


def build_fixture(package: prior.FixturePackage) -> FixtureResult:
    routing = next(
        candidate for candidate in package.routings if candidate.routing == "t-first"
    )
    if not routing.identity_exact:
        raise AssertionError("the pinned t-first routed current must be exact")
    transform = block123.spatial_fourier()
    cut = block119.cut_shift()
    monodromy = mode_monodromy()
    shifts = one_super_step_shifts()
    base_a = prior.momentum_diagonal_blocks(
        routing.temporal[block121.site(7, 0)], transform, cut
    )
    base_b = routing.temporal[block121.site(2, 0)]
    family_a = tuple(
        make_mode_result(
            momentum,
            sector,
            package.thetas[momentum],
            tuple(
                (
                    monodromy**power
                    * base_a[momentum]
                    * monodromy ** (-power)
                ).applyfunc(sp.expand)
                for power in range(4)
            ),
        )
        for momentum, sector in enumerate(package.sectors)
    )
    family_b = tuple(
        make_mode_result(
            momentum,
            sector,
            package.thetas[momentum],
            tuple(
                momentum_block(
                    (
                        shifts[momentum] ** power
                        * base_b
                        * shifts[momentum] ** (-power)
                    ).applyfunc(sp.expand),
                    momentum,
                    8,
                )
                for power in range(4)
            ),
        )
        for momentum, sector in enumerate(package.sectors)
    )
    families_a = tuple(mode.family for mode in family_a)
    reflected_a = tuple(mode.reflected for mode in family_a)
    families_b = tuple(mode.family for mode in family_b)
    reflected_b = tuple(mode.reflected for mode in family_b)
    union = union_mode_families(family_a, family_b)
    union_reflected = union_reflected_families(family_a, family_b)

    two_time: list[tuple[QMatrix, ...]] = []
    two_time_reflected: list[tuple[QMatrix, ...]] = []
    for momentum, (mode, theta_source) in enumerate(zip(family_a, package.thetas)):
        field = mode.field
        theta = field.matrix(theta_source)
        left_powers = tuple(field.matrix(monodromy**power) for power in range(3))
        right_powers = tuple(
            field.matrix(monodromy ** (-power)) for power in range(3)
        )
        base = mode.family[0]
        family = tuple(
            qmat_mul(
                field,
                qmat_mul(field, left_powers[left], base),
                right_powers[right],
            )
            for left in range(3)
            for right in range(3)
        )
        two_time.append(family)
        two_time_reflected.append(
            tuple(
                qmat_mul(field, qmat_mul(field, theta, member), theta)
                for member in family
            )
        )

    return FixtureResult(
        shear=package.shear,
        sectors=package.sectors,
        thetas=package.thetas,
        monodromy=monodromy,
        shifts=shifts,
        family_a=family_a,
        family_b=family_b,
        aggregate_a=aggregate_results(families_a, reflected_a, package.sectors),
        aggregate_b=aggregate_results(families_b, reflected_b, package.sectors),
        aggregate_union=aggregate_results(union, union_reflected, package.sectors),
        aggregate_two_time=aggregate_results(
            tuple(two_time), tuple(two_time_reflected), package.sectors
        ),
    )


def fixture_results() -> tuple[FixtureResult, ...]:
    packages = prior.fixture_packages()
    if tuple(package.shear for package in packages) != SHEARS:
        raise AssertionError("both pinned shear fixtures")
    return tuple(build_fixture(package) for package in packages)


@dataclass(frozen=True)
class DescendingWitness:
    weights: tuple[Q, ...]
    leakage_rank: int
    leakage_pivots: tuple[int, ...]
    all_weights_nonzero: bool
    operator_nonzero: bool
    leakage_zero: bool
    sandwich: Q
    compression: Q
    adjoint_mismatch: bool
    residual: QMatrix
    residual_entry: tuple[int, int, Q] | None


def shortest_nonzero(source: QMatrix, field: QuadraticField) -> tuple[int, int, Q] | None:
    entries = (
        (len(field.text(value)), row, column, value)
        for row, values in enumerate(source)
        for column, value in enumerate(values)
        if value != QZERO
    )
    selected = min(entries, default=None)
    if selected is None:
        return None
    _, row, column, value = selected
    return row, column, value


def descending_witness(mode: ModeFamilyResult) -> DescendingWitness | None:
    reduced, pivots = qmat_rref(mode.field, mode.leakage)
    if pivots != tuple(range(7)):
        return None
    weights_list = [QZERO] * 8
    weights_list[7] = QONE
    for row, pivot in enumerate(pivots):
        weights_list[pivot] = mode.field.neg(reduced[row][7])
    weights = tuple(weights_list)
    operator = field_weighted_operator(mode.field, weights, mode.family)
    reflected_operator = field_weighted_operator(
        mode.field, weights, mode.reflected
    )
    bra = qmat_adjoint(mode.field, mode.y)
    sandwich = qmat_mul(
        mode.field, qmat_mul(mode.field, bra, operator), mode.y
    )[0][0]
    compression = quotient_compression(mode.field, mode.y, operator)
    residual = reflection_adjointness_residual(
        mode.field, mode.y, operator, reflected_operator
    )
    return DescendingWitness(
        weights=weights,
        leakage_rank=mode.leakage_rank,
        leakage_pivots=mode.leakage_pivots,
        all_weights_nonzero=all(weight != QZERO for weight in weights),
        operator_nonzero=not qmat_zero(operator),
        leakage_zero=qmat_zero(operator_leakage(mode.field, mode.y, operator)),
        sandwich=sandwich,
        compression=compression,
        adjoint_mismatch=reflected_operator != qmat_adjoint(mode.field, operator),
        residual=residual,
        residual_entry=shortest_nonzero(residual, mode.field),
    )


N5_LINES = (
    "N5: per_element: time-visibility, monodromy-rank-eight, shift-rank-seven, descending-kernel, zero-leakage, nonzero-compression, adjointness-residual, joint-emptiness, and footing-correction certificates are checked",
    "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus",
    "per_mode: at zero momentum the shift-conjugated rank-seven leakage map has a one-dimensional kernel with identically vanishing leakage and nonzero quotient compression, but its reflection-adjointness residual is nonzero",
    "per_block: both displayed time-conjugation families are quotient-visible; the monodromy family has empty descent, the shift family has one genuine descending member, and no nonzero-compression member satisfies descent and reflection-adjointness jointly in either family, their union, or the displayed two-time class",
    "lattice_wide: checked and not executed — reflection-compatible observable classes, Q-modification, the naturality classification, the curved-carrier dependency, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open",
)

SCOPE_KEYS = (
    "time_dressing",
    "visibility",
    "descending_member",
    "nonzero_compression",
    "adjointness_wall",
    "single_blocking",
    "lift_dependent",
    "injectivity_correction",
    "dual_family",
    "os_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity_quotient",
    "adm",
    "n1_n8",
    "w1",
    "n5_resolution",
    "bounded_wall",
)


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    forbidden_absolute_upgrades = (
        "absolute adjointness wall",
        "all time dressings are blocked",
        "all time dressings are excluded",
        "every possible time dressing",
        "universal time-dressing no-go",
    )
    result = {
        "time_dressing": "time dressing" in note or "time-smeared" in note,
        "visibility": "genuinely distinct" in note or "visibility" in note,
        "descending_member": (
            "descending member" in note or "reaches the quotient" in note
        ),
        "nonzero_compression": "nonzero quotient compression" in note,
        "adjointness_wall": (
            "adjointness wall" in note or "reflection-adjointness" in note
        ),
        "single_blocking": "single blocking" in note or "isolated" in note,
        "lift_dependent": (
            "lift-dependent" in note or "convention-dependent" in note
        ),
        "injectivity_correction": (
            "injectivity" in note and ("false" in note or "refuted" in note)
        ),
        "dual_family": "dual-family" in note or "both families" in note,
        "os_boundary": (
            "not an os no-go" in note or "not a curved os no-go" in note
        ),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity_quotient": (
            "gravity constraint quotient remains unexecuted" in note
        ),
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "w1": "w1" in note,
        "n5_resolution": all(
            f"{resolution}:" in note
            for resolution in (
                "per_element",
                "per_site",
                "per_mode",
                "per_block",
                "lattice_wide",
            )
        ),
        "bounded_wall": not any(
            phrase in note for phrase in forbidden_absolute_upgrades
        ),
    }
    if mutation == "weaken_no_go_packet":
        result["os_boundary"] = False
        result["n1_n8"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
    if mutation == "claim_wall_absolute":
        result["bounded_wall"] = False
    return result


def witness_text(
    witness: DescendingWitness | None, field: QuadraticField
) -> str:
    if witness is None:
        return "none"
    return (
        f"f[7]={field.text(witness.weights[7])},"
        f"all_nonzero={witness.all_weights_nonzero},"
        f"sha={exact_digest(witness.weights)}"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started = time.monotonic()
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-authority",
        "Block 125 note/runner/cache and ancestors 124--103 are pinned",
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_TIME_DRESSING_ADJOINTNESS_WALL_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SPATIAL_DRESSING_INVISIBILITY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_spatial_dressing_invisibility_2026_08_17.py",
            "logs/runner-cache/admissibility_dirac_kahler_spatial_dressing_invisibility_2026_08_17.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(authority[f"ancestor_{number}"] for number in range(103, 125))
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    fixtures = fixture_results()
    witnesses = tuple(descending_witness(fixture.family_b[0]) for fixture in fixtures)

    visibility_exact = all(
        all(
            mode.raw_rank == 4
            and mode.span_rank == 8
            and mode.pairwise_distinct
            for mode in fixture.family_a
        )
        and all(mode.pairwise_distinct for mode in fixture.family_b)
        for fixture in fixtures
    )
    if mutation == "break_visibility":
        visibility_exact = False
    checks.check(
        "B-the-visibility",
        "both time families are genuinely distinct; family A has span rank 8 per momentum",
        visibility_exact,
    )

    family_a_empty = all(
        all(mode.descent.rank == 8 and not mode.descent_kernel for mode in fixture.family_a)
        for fixture in fixtures
    )
    if mutation == "break_family_a_rank":
        family_a_empty = False
    checks.check(
        "C-family-a-descent-empty",
        "the family-A leakage map has rank 8 and kernel zero at every momentum in both fixtures",
        family_a_empty,
    )

    kernel_exact = all(
        witness is not None
        and witness.leakage_rank == 7
        and witness.leakage_pivots == tuple(range(7))
        and witness.weights[7] == QONE
        and witness.all_weights_nonzero
        and witness.operator_nonzero
        and witness.leakage_zero
        for fixture, witness in zip(fixtures, witnesses)
    )
    kernel_raw = kernel_exact
    if mutation == "break_kernel_member":
        kernel_exact = False
    compression_nonzero = all(
        witness is not None
        and witness.sandwich != QZERO
        and witness.compression != QZERO
        for witness in witnesses
    )
    compression_raw = compression_nonzero
    if mutation == "claim_zero_compression":
        compression_nonzero = False
    checks.check(
        "D-the-descending-member",
        "family B at k=0 has rank 7, a one-dimensional nonzero descending kernel, and nonzero quotient compression",
        kernel_exact and compression_nonzero,
    )

    residual_nonzero = all(
        witness is not None
        and witness.adjoint_mismatch
        and witness.residual_entry is not None
        for witness in witnesses
    )
    residual_raw = residual_nonzero
    if mutation == "break_adjointness_residual":
        residual_nonzero = False
    joint_empty = all(
        fixture.aggregate_a.joint_operator_empty
        and fixture.aggregate_b.joint_operator_empty
        and fixture.aggregate_union.joint_operator_empty
        and fixture.aggregate_two_time.joint_operator_empty
        and fixture.aggregate_two_time.span_rank == 9
        for fixture in fixtures
    )
    joint_raw = joint_empty
    if mutation == "claim_joint_solution":
        joint_empty = False
    checks.check(
        "E-the-adjointness-wall",
        "O* has a nonzero K_Theta residual and the joint solve is empty in A, B, their union span, and the nine-dimensional two-time class",
        residual_nonzero and joint_empty,
    )

    footing_exact = all(
        fixture.family_a[0].descent.rank == 8
        and fixture.family_b[0].leakage_rank == 7
        for fixture in fixtures
    )
    if mutation == "claim_injectivity":
        footing_exact = False
    checks.check(
        "F-the-footing-correction",
        "leakage injectivity is false as a class claim; k=0 ranks are lift-dependent 8 versus 7, so the wall rests on adjointness alone",
        footing_exact and kernel_raw and joint_raw,
    )

    isolation_exact = (
        kernel_raw and compression_raw and residual_raw and joint_raw
    )
    if mutation == "break_isolation":
        isolation_exact = False
    checks.check(
        "G-the-isolation-statement",
        "descent and nonzero compression are achieved while their conjunction with adjointness is empty: adjointness is the single displayed blocker",
        isolation_exact,
    )

    note_scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "bounded dual-family/correction/isolation/N1--N8/W1/N5 firewalls and runtime bound are present",
        set(note_scope) == set(SCOPE_KEYS)
        and all(note_scope.values())
        and elapsed_before_scope <= 400,
    )

    print(
        "FAMILY A: M=C S_AP C^T on the eight cut modes, M^8=-I; "
        "J_A(k) is the t-first routed temporal density at (slice 7,x=0); "
        "A_k=(M^m J_A(k) M^-m)_{m=0..3} plus "
        "(Theta_k M^m J_A(k) M^-m Theta_k)_{m=0..3}."
    )
    print(
        "FAMILY B: SHIFT is the isolated one-super-step mode lift; "
        "J_B(k) is the t-first routed temporal density at (slice 2,x=0); "
        "B_k=(SHIFT_k^m J_B(k) SHIFT_k^-m)_{m=0..3} plus "
        "(Theta_k SHIFT_k^m J_B(k) SHIFT_k^-m Theta_k)_{m=0..3}."
    )
    print(
        "RANKS: A leakage(k=0..3)="
        f"{tuple(tuple(mode.descent.rank for mode in fixture.family_a) for fixture in fixtures)}; "
        "B leakage(k=0..3)="
        f"{tuple(tuple(mode.leakage_rank for mode in fixture.family_b) for fixture in fixtures)}."
    )
    for fixture, witness in zip(fixtures, witnesses):
        compression = (
            "none"
            if witness is None
            else (
                f"nonzero={witness.compression != QZERO},"
                f"sha={exact_digest(witness.compression)}"
            )
        )
        print(
            f"O* c={fixture.shear}: weights={witness_text(witness, fixture.family_b[0].field)}; "
            f"nonzero={bool(witness and witness.operator_nonzero)}; "
            f"leakage_zero={bool(witness and witness.leakage_zero)}; "
            f"quotient_compression={compression}."
        )
    for fixture, witness in zip(fixtures, witnesses):
        if witness is None or witness.residual_entry is None:
            residual_text = "none"
        else:
            row, column, value = witness.residual_entry
            residual_text = (
                f"R[{row},{column}] nonzero; sha={exact_digest(value)}"
            )
        print(f"ADJOINTNESS RESIDUAL c={fixture.shear}: {residual_text}.")
    print(
        "EXHAUSTION: aggregate joint ranks A/B/union/two-time="
        f"{tuple((f.aggregate_a.joint_rank, f.aggregate_b.joint_rank, f.aggregate_union.joint_rank, f.aggregate_two_time.joint_rank) for f in fixtures)}; "
        "constraint sha="
        f"{exact_digest(tuple((f.aggregate_a.joint_witness, f.aggregate_b.joint_witness, f.aggregate_union.joint_witness, f.aggregate_two_time.joint_witness) for f in fixtures))}."
    )
    for line in N5_LINES:
        print(line)
    print(
        "RESULT: the time direction is visible and descent is achievable — a current-derived operator reaches the quotient for the first time — but reflection-adjointness blocks every displayed member, so the observable wall is exactly the reflection structure"
    )
    print(
        "DECISION_CUT: pose reflection-compatible observable classes and the naturality/curved work; reject further smearing constructions"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
