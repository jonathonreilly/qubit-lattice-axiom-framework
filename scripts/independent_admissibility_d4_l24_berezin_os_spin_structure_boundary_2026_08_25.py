#!/usr/bin/env python3
"""Independent exact checker for the periodic-L24 Berezin OS obstruction.

This file deliberately imports no project runner.  It rebuilds the frozen
radius-one temporal/Clifford block from its definitions and checks the literal
positive-half reflected covariance.  The negative two-generator Berezin norm
is a boundary for the periodic, uniform-reflection spin structure only; no
claim about antiperiodic or seam-transported reflections is made here.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
from sympy.polys.matrices import DomainMatrix


L_TIME = 24
HALF_TIME = 12
FIBER_DIMENSION = 2
HALF_DIMENSION = HALF_TIME * FIBER_DIMENSION
FULL_DIMENSION = L_TIME * FIBER_DIMENSION
MASS = sp.Rational(2, 7)
I = sp.I

SIGMA_X = sp.Matrix(((0, 1), (1, 0)))
SIGMA_Z = sp.diag(1, -1)
SKEW = sp.Matrix(((0, 1), (-1, 0)))
PHASE = sp.diag(1, -I)

EXPECTED_MINOR = sp.Matrix((
    (
        -sp.Rational(147051604814471, 526761374589720),
        -sp.Rational(627723416089, 526761374589720),
    ),
    (
        -sp.Rational(627723416089, 526761374589720),
        sp.Rational(13841287201, 526761374589720),
    ),
))
EXPECTED_WITNESS = -sp.Rational(
    678223072849, 77463616656739800
)
EXPECTED_REDUCED_INERTIA = (2, 2, 20)  # (n_plus, n_minus, n_zero)
EXPECTED_FULL_INERTIA = (16, 16, 160)


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.cancel(value) == 0 for value in left - right
    )


def temporal_matrices() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """Return periodic U, centered D, and the frozen uniform reflection."""
    shift = sp.zeros(L_TIME)
    for time in range(L_TIME):
        shift[(time + 1) % L_TIME, time] = 1
    differential = sp.expand((shift - shift.T) / 2)
    reflection = sp.zeros(L_TIME)
    for time in range(L_TIME):
        reflection[L_TIME - 1 - time, time] = -1
    return shift, differential, reflection


def exact_rank(matrix: sp.MatrixBase) -> int:
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).rank()


def exact_real_symmetric_inertia(
    matrix: sp.MatrixBase,
) -> tuple[int, int, int]:
    """Compute (positive, negative, zero) by exact symmetric congruence.

    A nonzero diagonal supplies a one-dimensional pivot.  If every diagonal
    vanishes but an off-diagonal entry remains, its 2x2 zero-diagonal block is
    hyperbolic and supplies one sign of each kind.  The Schur complement is a
    congruence, so the recursion is an exact Sylvester-law certificate.
    """
    current = sp.Matrix(matrix)
    if not matrix_equal(current, current.T):
        raise ValueError("inertia input is not real symmetric")
    positive = 0
    negative = 0
    zero = 0

    while current.rows:
        size = current.rows
        diagonal_index = next(
            (index for index in range(size) if current[index, index] != 0),
            None,
        )
        if diagonal_index is not None:
            order = [diagonal_index] + [
                index for index in range(size) if index != diagonal_index
            ]
            current = current.extract(order, order)
            pivot = sp.cancel(current[0, 0])
            if pivot > 0:
                positive += 1
            elif pivot < 0:
                negative += 1
            else:  # pragma: no cover - guarded by the exact nonzero search
                raise AssertionError("nonzero pivot simplified to zero")
            if size == 1:
                current = sp.zeros(0)
            else:
                tail = current[1:, 1:]
                column = current[1:, :1]
                current = (tail - column * column.T / pivot).applyfunc(
                    sp.cancel
                )
            continue

        off_diagonal = next((
            (row, column)
            for row in range(size)
            for column in range(row + 1, size)
            if current[row, column] != 0
        ), None)
        if off_diagonal is None:
            zero += size
            break

        first, second = off_diagonal
        order = [first, second] + [
            index for index in range(size)
            if index not in (first, second)
        ]
        current = current.extract(order, order)
        pivot_block = current[:2, :2]
        positive += 1
        negative += 1
        if size == 2:
            current = sp.zeros(0)
        else:
            coupling = current[2:, :2]
            current = (
                current[2:, 2:]
                - coupling * pivot_block.inv() * coupling.T
            ).applyfunc(sp.cancel)

    return positive, negative, zero


@dataclass(frozen=True)
class Fixture:
    shift: sp.Matrix
    differential: sp.Matrix
    time_reflection: sp.Matrix
    complex_action: sp.Matrix
    real_action: sp.Matrix
    reflection: sp.Matrix
    embedding: sp.Matrix
    kernel: sp.Matrix


def build_fixture() -> Fixture:
    shift, differential, time_reflection = temporal_matrices()
    complex_action = sp.expand(
        sp.kronecker_product(
            sp.eye(L_TIME), MASS * sp.eye(2) + I * SIGMA_X
        )
        + sp.kronecker_product(differential, SIGMA_Z)
    )
    full_phase = sp.kronecker_product(sp.eye(L_TIME), PHASE)
    real_action = sp.expand(full_phase.H * complex_action * full_phase)
    reflection = sp.kronecker_product(time_reflection, SIGMA_Z)
    embedding = sp.Matrix.vstack(
        sp.eye(HALF_DIMENSION), sp.zeros(HALF_DIMENSION)
    )
    covariance = real_action.inv(method="DM")
    kernel = sp.simplify(
        embedding.T * reflection * covariance * embedding
    )
    return Fixture(
        shift=shift,
        differential=differential,
        time_reflection=time_reflection,
        complex_action=complex_action,
        real_action=real_action,
        reflection=reflection,
        embedding=embedding,
        kernel=kernel,
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


N5_LINES = (
    "per_element: checked the exact radius-one 2x2 Clifford action, reflected covariance entries, and the disclosed two-generator Berezin principal minor.",
    "per_site: checked the periodic L24 carrier on the positive half t=0,...,11 and used the exact witness sites t=0 and t=6.",
    "per_mode: checked one frozen radius-one Clifford block and its eight-copy full-16 lift; no other radius, source response, or held-out point was evaluated.",
    "per_block: checked action/reflection covariance, degree-one rank and inertia, degree-two Wick determinant, and global-sign, transpose, phase, and common-twist robustness as separate exact blocks.",
    "lattice_wide: checked and not executed -- no antiperiodic or seam-transported spin structure, two-step reconstruction, full event-fiber GNS/CAR identification, CPTP history law, process tensor, gravity law, or TOE closure is tested.",
)


def main() -> int:
    fixture = build_fixture()
    checks = Checks()

    expected_real_action = sp.expand(
        MASS * sp.eye(FULL_DIMENSION)
        + sp.kronecker_product(sp.eye(L_TIME), SKEW)
        + sp.kronecker_product(fixture.differential, SIGMA_Z)
    )
    checks.check(
        "A1",
        "the periodic L24 shift and centered differential are rebuilt exactly",
        matrix_equal(fixture.shift**L_TIME, sp.eye(L_TIME))
        and matrix_equal(fixture.differential.T, -fixture.differential),
    )
    checks.check(
        "A2",
        "the phase-real action is the exact radius-one frozen block",
        matrix_equal(fixture.real_action, expected_real_action)
        and matrix_equal(
            fixture.real_action + fixture.real_action.T,
            2 * MASS * sp.eye(FULL_DIMENSION),
        ),
    )
    checks.check(
        "A3",
        "the uniform reflected action obeys ordinary-transpose self-duality",
        matrix_equal(
            fixture.reflection * fixture.real_action.T
            * fixture.reflection.T,
            fixture.real_action,
        ),
    )

    kernel = fixture.kernel
    witness_indices = (0, 12)
    witness_minor = kernel.extract(witness_indices, witness_indices)
    witness = sp.factor(witness_minor.det())
    reduced_inertia = exact_real_symmetric_inertia(kernel)
    full_inertia = tuple(8 * entry for entry in reduced_inertia)

    checks.check(
        "B1",
        "the literal degree-one reflected covariance is exact real symmetric",
        matrix_equal(kernel, kernel.T) and matrix_equal(kernel, kernel.H),
    )
    checks.check(
        "B2",
        "the disclosed t=0/t=6 principal matrix is reproduced entrywise",
        matrix_equal(witness_minor, EXPECTED_MINOR),
    )
    checks.check(
        "B3",
        "the two-generator Wick determinant is the disclosed strict negative rational",
        witness == EXPECTED_WITNESS
        and witness == -sp.Rational(7**14, 77463616656739800)
        and witness < 0,
    )
    checks.check(
        "B4",
        "the reduced kernel has exact rank four and inertia (2,2,20)",
        exact_rank(kernel) == 4
        and reduced_inertia == EXPECTED_REDUCED_INERTIA,
    )
    checks.check(
        "B5",
        "the eight-copy full-16 lift has rank 32 and inertia (16,16,160)",
        8 * exact_rank(kernel) == 32
        and full_inertia == EXPECTED_FULL_INERTIA,
    )

    negative_kernel = -kernel
    transpose_kernel = kernel.T
    checks.check(
        "C1",
        "a global reflection sign cannot repair the even-degree determinant",
        sp.factor(
            negative_kernel.extract(witness_indices, witness_indices).det()
        ) == witness
        and exact_real_symmetric_inertia(negative_kernel)
        == EXPECTED_REDUCED_INERTIA,
    )
    checks.check(
        "C2",
        "left/right covariance convention transposition leaves the witness fixed",
        matrix_equal(transpose_kernel, kernel)
        and sp.factor(
            transpose_kernel.extract(witness_indices, witness_indices).det()
        ) == witness,
    )

    half_phase = sp.kronecker_product(sp.eye(HALF_TIME), PHASE)
    phased_kernel = sp.expand(half_phase.H * kernel * half_phase)
    checks.check(
        "C3",
        "the complex phase presentation is an exact unitary congruence",
        matrix_equal(half_phase.H * half_phase, sp.eye(HALF_DIMENSION))
        and matrix_equal(
            half_phase * phased_kernel * half_phase.H, kernel
        )
        and matrix_equal(phased_kernel, phased_kernel.H)
        and exact_rank(phased_kernel) == 4
        and sp.factor(
            phased_kernel.extract(witness_indices, witness_indices).det()
        ) == witness,
    )

    # Let q be a common phase multiplying every reflected odd generator,
    # relative to the frozen convention.  At degree p, the OS block scales by
    # q**p.  Among fourth roots of unity, only q=+/-1 keep the nonzero real
    # degree-one kernel Hermitian.  Both have q**2=1, so neither changes the
    # two-generator determinant.  q=+/-i would reverse the degree-two sign but
    # already makes the degree-one form anti-Hermitian and is inadmissible.
    fourth_roots = (sp.Integer(1), -sp.Integer(1), I, -I)
    hermitian_twists = tuple(
        twist for twist in fourth_roots
        if matrix_equal(twist * kernel, (twist * kernel).H)
    )
    checks.check(
        "C4",
        "common fourth-root twists are Hermitian exactly for q=+/-1",
        hermitian_twists == (sp.Integer(1), -sp.Integer(1)),
    )
    checks.check(
        "C5",
        "every Hermitian common twist has q^2=1 and preserves the negative Wick norm",
        all(
            sp.simplify(twist**2) == 1
            and sp.factor((twist * witness_minor).det()) == witness
            for twist in hermitian_twists
        )
        and all(
            not matrix_equal(twist * kernel, (twist * kernel).H)
            for twist in (I, -I)
        ),
    )

    checks.check(
        "D1",
        "the five N5 resolution lines are present exactly once",
        len(N5_LINES) == 5
        and tuple(line.split(":", 1)[0] for line in N5_LINES)
        == ("per_element", "per_site", "per_mode", "per_block", "lattice_wide"),
    )

    for line in N5_LINES:
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
