#!/usr/bin/env python3
"""Exact checks for the binary/ternary scaled-projector frame-lift note.

The runner verifies the finite algebra around the one-ancilla compression and
an exact degree-nine polynomial hostile test.  It does not finitely prove the
standard dimension-three frame-function theorem; that theorem is a named
mathematical input in the note.
"""

from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
GLEASON_PATH = ROOT / "docs" / "GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md"
PRIOR_PATH = ROOT / "docs" / "BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md"

AUDIT_INPUT_PATHS = (
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md",
    "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
)

I2 = sp.eye(2)
I3 = sp.eye(3)
SQRT3 = sp.sqrt(3)
OMEGA = sp.exp(2 * sp.pi * sp.I / 3).expand(complex=True)
MODULUS = 1_000_003


def normalize(text):
    return " ".join(text.split())


def matrix_zero(value):
    return value.applyfunc(sp.simplify) == sp.zeros(*value.shape)


def top_effect(column):
    top = column[:2, :]
    return sp.simplify(top * top.H)


def quaternion_rotation(q):
    q0, q1, q2, q3 = q
    scale = sum(value * value for value in q)
    numerators = (
        (q0*q0 + q1*q1 - q2*q2 - q3*q3, 2*(q1*q2 - q0*q3), 2*(q1*q3 + q0*q2)),
        (2*(q1*q2 + q0*q3), q0*q0 - q1*q1 + q2*q2 - q3*q3, 2*(q2*q3 - q0*q1)),
        (2*(q1*q3 - q0*q2), 2*(q2*q3 + q0*q1), q0*q0 - q1*q1 - q2*q2 + q3*q3),
    )
    return tuple(
        tuple(Fraction(entry, scale) for entry in row)
        for row in numerators
    )


def rational_rotations(count):
    seen = set()
    rotations = []
    for q in product(range(-4, 5), repeat=4):
        if q == (0, 0, 0, 0):
            continue
        rotation = quaternion_rotation(q)
        if rotation in seen:
            continue
        seen.add(rotation)
        rotations.append(rotation)
        if len(rotations) == count:
            return rotations
    raise RuntimeError("insufficient deterministic rational rotations")


def mat_vec(rotation, vector):
    return tuple(
        sum(rotation[i][j] * vector[j] for j in range(3))
        for i in range(3)
    )


def odd_sphere_basis(max_degree):
    basis = []
    for i in range(max_degree + 1):
        for j in range(max_degree + 1 - i):
            for k in (0, 1):
                degree = i + j + k
                if degree <= max_degree and degree % 2 == 1:
                    basis.append((i, j, k))
    return tuple(basis)


def monomial(vector, powers):
    value = Fraction(1)
    for coordinate, power in zip(vector, powers):
        value *= coordinate ** power
    return value


def modulo(value, prime):
    return (value.numerator % prime) * pow(value.denominator % prime, prime - 2, prime) % prime


def rank_mod_prime(rows, prime):
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (index for index in range(pivot_row, row_count) if matrix[index][column] % prime),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column] % prime, prime - 2, prime)
        matrix[pivot_row] = [(entry * inverse) % prime for entry in matrix[pivot_row]]
        pivot_values = matrix[pivot_row]
        for index in range(row_count):
            if index == pivot_row:
                continue
            factor = matrix[index][column] % prime
            if factor:
                matrix[index] = [
                    (left - factor * right) % prime
                    for left, right in zip(matrix[index], pivot_values)
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def polynomial_mode_certificate():
    basis = odd_sphere_basis(9)
    rotations = rational_rotations(1000)
    singleton_radius = Fraction(3, 4)
    pair_radius = Fraction(5, 8)
    singleton = (Fraction(0), Fraction(0), Fraction(1))
    pair_plus = (Fraction(4, 5), Fraction(0), Fraction(-3, 5))
    pair_minus = (Fraction(-4, 5), Fraction(0), Fraction(-3, 5))
    rows = []
    linear_kernel = True
    for rotation in rotations:
        n = mat_vec(rotation, singleton)
        plus = mat_vec(rotation, pair_plus)
        minus = mat_vec(rotation, pair_minus)
        linear_kernel = linear_kernel and all(
            singleton_radius*n[index]
            + pair_radius*(plus[index] + minus[index]) == 0
            for index in range(3)
        )
        rational_row = [monomial(n, power) for power in basis]
        rational_row.extend(
            monomial(plus, power) + monomial(minus, power)
            for power in basis
        )
        rows.append(tuple(modulo(value, MODULUS) for value in rational_row))
    rank = rank_mod_prime(rows, MODULUS)
    return len(basis), len(rows[0]), rank, linear_kernel


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, label, statement, condition):
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self):
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main():
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    gleason = GLEASON_PATH.read_text(encoding="utf-8")
    prior = PRIOR_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: canonical axiom wording, the landed frame-theorem record, and the landed open-question note are read only for source and boundary gates")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency; the cache envelope separately binds this runner and every declared input")
    print("standard_theorem_boundary: the dimension-three frame-function theorem is named and not represented as finitely recomputed")

    checks.check(
        "source-admissibility",
        "the canonical source says the local distribution is nearest-neighbor determined and varying",
        "the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions" in normalize(axiom),
    )
    checks.check(
        "source-frame",
        "the named theorem record states the dimension-at-least-three frame representation",
        "dim H ≥ 3" in gleason and "every frame function" in gleason,
    )
    checks.check(
        "source-frontier",
        "the landed comparison explicitly records the scaled ternary question",
        "prove ternary scaled-projector sufficiency or find a rogue" in prior,
    )
    checks.check(
        "surface-status",
        "the note keeps conditional support, hypothetical axiom wording, and independent audit explicit",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: conditional-support",
                "hypothetical_axiom_status:",
                "Independent audit remains required",
                "no canonical axiom edit",
            )
        ),
    )

    # A basis containing the pure ancilla compresses to a binary menu plus zero.
    standard_basis = I3
    standard_effects = tuple(top_effect(standard_basis[:, index]) for index in range(3))
    checks.check(
        "zero-to-binary",
        "the standard qutrit basis compresses to two qubit projectors and one zero effect",
        standard_effects == (
            sp.Matrix([[1, 0], [0, 0]]),
            sp.Matrix([[0, 0], [0, 1]]),
            sp.zeros(2),
        ),
    )
    checks.check(
        "zero-to-binary-sum",
        "dropping the zero leaves an exact binary resolution of the qubit identity",
        matrix_zero(standard_effects[0] + standard_effects[1] - I2),
    )

    # The Fourier basis compresses to an equal-weight ternary rank-one menu.
    fourier = sp.Matrix(
        [
            [1, 1, 1],
            [1, OMEGA, OMEGA**2],
            [1, OMEGA**2, OMEGA],
        ]
    ) / SQRT3
    fourier_effects = tuple(top_effect(fourier[:, index]) for index in range(3))
    checks.check(
        "fourier-unitary",
        "the exact Fourier columns form an orthonormal qutrit basis",
        matrix_zero(fourier.H * fourier - I3),
    )
    checks.check(
        "fourier-compression",
        "the three compressed Fourier effects sum exactly to the qubit identity",
        matrix_zero(sum(fourier_effects, sp.zeros(2)) - I2),
    )
    checks.check(
        "fourier-scaled-rank-one",
        "each compressed Fourier effect has trace two-thirds and determinant zero",
        all(
            sp.simplify(sp.trace(effect) - sp.Rational(2, 3)) == 0
            and sp.simplify(effect.det()) == 0
            for effect in fourier_effects
        ),
    )

    # A second exact rational basis guards against a Fourier-only identity.
    rational_rotation = sp.Matrix(
        [[sp.Rational(1, 3), -sp.Rational(2, 3), sp.Rational(2, 3)],
         [sp.Rational(2, 3), sp.Rational(2, 3), sp.Rational(1, 3)],
         [-sp.Rational(2, 3), sp.Rational(1, 3), sp.Rational(2, 3)]]
    )
    rational_effects = tuple(top_effect(rational_rotation[:, index]) for index in range(3))
    checks.check(
        "rational-unitary",
        "the independent rational columns form an exact orthonormal basis",
        matrix_zero(rational_rotation.T * rational_rotation - I3),
    )
    checks.check(
        "rational-compression",
        "the independent rational compression is a three-member scaled rank-one resolution",
        matrix_zero(sum(rational_effects, sp.zeros(2)) - I2)
        and all(effect != sp.zeros(2) and sp.simplify(effect.det()) == 0 for effect in rational_effects),
    )

    # Exact cubic hostile control on a genuine equal-weight trine.
    nz_values = (sp.Integer(1), -sp.Rational(1, 2), -sp.Rational(1, 2))
    cubic_weights = tuple(sp.Rational(1, 3) * (1 + value**3) for value in nz_values)
    checks.check(
        "cubic-hostile-control",
        "the smooth binary cubic grading gives exact trine sum five-fourths rather than one",
        sp.simplify(sum(cubic_weights) - sp.Rational(5, 4)) == 0,
    )

    # Positivity makes a zero diagonal expectation delete the ancilla block.
    b11, b12, b13, b21, b22, b23, b31, b32, b33 = sp.symbols(
        "b11 b12 b13 b21 b22 b23 b31 b32 b33", complex=True
    )
    B = sp.Matrix([[b11, b12, b13], [b21, b22, b23], [b31, b32, b33]])
    R = B.H * B
    last_expectation = sp.expand(R[2, 2])
    checks.check(
        "ancilla-positive-factor",
        "the ancilla expectation is exactly the squared norm of the last factor column",
        sp.simplify(
            last_expectation
            - (sp.conjugate(b13)*b13 + sp.conjugate(b23)*b23 + sp.conjugate(b33)*b33)
        ) == 0,
    )

    basis_count, column_count, rank, linear_kernel = polynomial_mode_certificate()
    checks.check(
        "polynomial-basis",
        "the odd sphere-polynomial normal form through degree nine has fifty-five coefficients per radius",
        basis_count == 55 and column_count == 110,
    )
    checks.check(
        "polynomial-born-kernel",
        "the three independent radius-weighted linear Born modes lie in the exact ternary kernel",
        linear_kernel,
    )
    checks.check(
        "polynomial-rank",
        "one exact rational ternary orbit leaves only the three linear Born modes through degree nine",
        rank == 107,
    )

    print("per_element: exact scaled rank-one compression, zero-effect handling, trace, determinant, and cubic-weight identities are checked element by element")
    print("per_site: one complete M_2(C) site and its one-dimensional qutrit dilation are checked; no multi-site carrier is asserted")
    print("per_mode: odd sphere-polynomial sections through degree nine are checked by exact modular rank; the general frame theorem is named, not executed")
    print("per_block: this single theorem block checks the compression, hostile control, source boundaries, and conditional claim surface together")
    print("lattice_wide: checked and not executed — the theorem is one-site conditional mathematics and makes no lattice-wide registration claim")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
