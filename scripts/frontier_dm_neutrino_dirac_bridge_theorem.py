#!/usr/bin/env python3
"""Exact finite-matrix certificate for the DM-neutrino bridge algebra.

The certified result is deliberately conditional and algebraic. Given the
displayed Hermitian Euclidean Cl(4) generators on C^16 and real coefficients,
the runner checks the M(phi) square and grading identities, the bare
Xi_5 = -gamma_5 classification, and a finite bit-basis return lemma.

It does not select a physical Dirac/Yukawa carrier, derive a selector,
identify the constructed grading with physical chirality, or close a
normalization law.
"""

from __future__ import annotations

import itertools
import sys

import sympy as sp


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    """Record one decisive exact gate."""
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return condition


def is_zero(matrix: sp.Matrix) -> bool:
    """Return whether every expanded entry is exactly zero."""
    return bool(matrix.applyfunc(sp.expand).is_zero_matrix)


def commutes(left: sp.Matrix, right: sp.Matrix) -> bool:
    return is_zero(left * right - right * left)


def anticommutes(left: sp.Matrix, right: sp.Matrix) -> bool:
    return is_zero(left * right + right * left)


def frobenius_squared(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(matrix.conjugate().T * matrix))


def kron4(
    first: sp.Matrix,
    second: sp.Matrix,
    third: sp.Matrix,
    fourth: sp.Matrix,
) -> sp.Matrix:
    return sp.Matrix(sp.kronecker_product(first, second, third, fourth))


I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
I16 = sp.eye(16)

G0 = kron4(SZ, SZ, SZ, SX)
G1 = kron4(SX, I2, I2, I2)
G2 = kron4(SZ, SX, I2, I2)
G3 = kron4(SZ, SZ, SX, I2)
GENERATORS = [G0, G1, G2, G3]
SPATIAL_GENERATORS = [G1, G2, G3]

GAMMA_5 = G0 * G1 * G2 * G3
XI_5 = G1 * G2 * G3 * G0
P_L = (I16 + GAMMA_5) / 2
P_R = (I16 - GAMMA_5) / 2

SPATIAL_STATES = [
    (first, second, third)
    for first in range(2)
    for second in range(2)
    for third in range(2)
]
FULL_STATES = [
    (first, second, third, fourth)
    for first, second, third in SPATIAL_STATES
    for fourth in range(2)
]
INDEX = {state: index for index, state in enumerate(FULL_STATES)}

O0 = [(0, 0, 0)]
T1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
T2 = [(1, 1, 0), (1, 0, 1), (0, 1, 1)]
O3 = [(1, 1, 1)]


def projector(spatial_states: list[tuple[int, int, int]]) -> sp.Matrix:
    result = sp.zeros(16)
    for fourth in (0, 1):
        for spatial_state in spatial_states:
            index = INDEX[spatial_state + (fourth,)]
            result[index, index] = 1
    return result


def restricted_basis(spatial_states: list[tuple[int, int, int]]) -> sp.Matrix:
    columns = []
    for fourth in (0, 1):
        for spatial_state in spatial_states:
            column = sp.zeros(16, 1)
            column[INDEX[spatial_state + (fourth,)], 0] = 1
            columns.append(column)
    return sp.Matrix.hstack(*columns)


def grading_census(
    generators: list[sp.Matrix],
    grading: sp.Matrix,
) -> tuple[int, int]:
    """Count even products that commute and odd products that anticommute."""
    dimension = generators[0].rows
    even = 0
    odd = 0
    for size in range(len(generators) + 1):
        for subset in itertools.combinations(range(len(generators)), size):
            product = sp.eye(dimension)
            for index in subset:
                product *= generators[index]
            if size % 2 == 0:
                even += int(commutes(product, grading))
            else:
                odd += int(anticommutes(product, grading))
    return even, odd


def standard_four_by_four_generators() -> list[sp.Matrix]:
    """A separate exact Hermitian Euclidean Cl(4) realization."""
    sigma_1 = sp.Matrix([[0, 1], [1, 0]])
    sigma_2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sigma_3 = sp.Matrix([[1, 0], [0, -1]])
    identity = sp.eye(2)
    return [
        sp.Matrix(sp.kronecker_product(sigma_2, identity)),
        sp.Matrix(sp.kronecker_product(sigma_1, sigma_1)),
        sp.Matrix(sp.kronecker_product(sigma_1, sigma_2)),
        sp.Matrix(sp.kronecker_product(sigma_1, sigma_3)),
    ]


def main() -> int:
    print("DM-NEUTRINO BRIDGE ALGEBRA: exact conditional finite-matrix certificate")

    phi_1, phi_2, phi_3 = sp.symbols(
        "phi_1 phi_2 phi_3",
        real=True,
    )
    coefficients = [phi_1, phi_2, phi_3]
    matrix_family = sum(
        (coefficient * generator for coefficient, generator in zip(
            coefficients,
            SPATIAL_GENERATORS,
        )),
        sp.zeros(16),
    )
    coefficient_norm_squared = sum(coefficient**2 for coefficient in coefficients)

    print()
    print("== Exact displayed Clifford algebra ==")
    check(
        "displayed generators are Hermitian involutions",
        all(
            is_zero(generator - generator.conjugate().T)
            and is_zero(generator * generator - I16)
            for generator in GENERATORS
        ),
        "eight exact identities",
    )
    check(
        "all ordered Clifford anticommutators have the required value",
        all(
            is_zero(
                GENERATORS[left] * GENERATORS[right]
                + GENERATORS[right] * GENERATORS[left]
                - 2 * int(left == right) * I16
            )
            for left in range(4)
            for right in range(4)
        ),
        "sixteen ordered pairs",
    )
    check(
        "constructed grading is a Hermitian traceless involution",
        is_zero(GAMMA_5 - GAMMA_5.conjugate().T)
        and is_zero(GAMMA_5 * GAMMA_5 - I16)
        and sp.trace(GAMMA_5) == 0,
    )
    check(
        "real-coefficient M(phi) is Hermitian",
        is_zero(matrix_family - matrix_family.conjugate().T),
        "phi_1, phi_2, phi_3 are explicitly declared real",
    )
    check(
        "M(phi)^2 equals the coefficient norm squared times identity",
        is_zero(
            matrix_family * matrix_family
            - coefficient_norm_squared * I16
        ),
    )
    check(
        "M(phi) anticommutes with the constructed grading",
        anticommutes(matrix_family, GAMMA_5),
    )
    check(
        "both grading-diagonal blocks of M(phi) vanish",
        is_zero(P_L * matrix_family * P_L)
        and is_zero(P_R * matrix_family * P_R),
    )
    check(
        "axis substitution M(e_i) returns the corresponding generator",
        all(
            is_zero(
                matrix_family.subs({
                    phi_1: int(index == 0),
                    phi_2: int(index == 1),
                    phi_3: int(index == 2),
                })
                - SPATIAL_GENERATORS[index]
            )
            for index in range(3)
        ),
    )

    print()
    print("== Wrong-object rejectors ==")
    check(
        "a doubled coefficient norm is rejected",
        not is_zero(
            matrix_family * matrix_family
            - 2 * coefficient_norm_squared * I16
        ),
    )
    substituted_family = phi_1 * G1 + phi_2 * G2 + phi_3 * XI_5
    check(
        "replacing G_3 by Xi_5 breaks grading oddness",
        not anticommutes(substituted_family, GAMMA_5),
    )
    check(
        "an imaginary coefficient makes i G_1 non-Hermitian",
        not is_zero(sp.I * G1 - (sp.I * G1).conjugate().T),
    )
    truncated_family = phi_1 * G1 + phi_2 * G2
    check(
        "dropping the phi_3 term breaks the stated square",
        not is_zero(
            truncated_family * truncated_family
            - coefficient_norm_squared * I16
        ),
    )

    print()
    print("== Bare Xi_5 grading classification and explicit boundary ==")
    check(
        "Xi_5 equals minus the constructed grading",
        is_zero(XI_5 + GAMMA_5),
        "sign from three generator transpositions",
    )
    ordering_signs = []
    for ordering in itertools.permutations(range(4)):
        product = sp.eye(16)
        for index in ordering:
            product *= GENERATORS[index]
        if is_zero(product - GAMMA_5):
            ordering_signs.append(1)
        elif is_zero(product + GAMMA_5):
            ordering_signs.append(-1)
        else:
            ordering_signs.append(0)
    check(
        "all generator orderings equal plus or minus the grading",
        ordering_signs.count(1) == 12
        and ordering_signs.count(-1) == 12
        and 0 not in ordering_signs,
        "24 orderings: 12 plus and 12 minus",
    )
    check(
        "bare Xi_5 has zero grading-off-diagonal blocks",
        is_zero(P_L * XI_5 * P_R)
        and is_zero(P_R * XI_5 * P_L),
    )
    check(
        "G_1 has zero grading-diagonal blocks and full cross-block rank",
        is_zero(P_L * G1 * P_L)
        and is_zero(P_R * G1 * P_R)
        and (P_R * G1 * P_L).rank() == 8,
        "rank(P_R G_1 P_L) = 8",
    )
    xi_weights = (
        frobenius_squared(P_L * XI_5 * P_L),
        frobenius_squared(P_L * XI_5 * P_R),
        frobenius_squared(P_R * XI_5 * P_L),
        frobenius_squared(P_R * XI_5 * P_R),
    )
    generator_weights = (
        frobenius_squared(P_L * G1 * P_L),
        frobenius_squared(P_L * G1 * P_R),
        frobenius_squared(P_R * G1 * P_L),
        frobenius_squared(P_R * G1 * P_R),
    )
    check(
        "the exact squared Frobenius block weights are separated",
        xi_weights == (8, 0, 0, 8)
        and generator_weights == (0, 8, 8, 0),
        "LL/LR/RL/RR: Xi_5 8/0/0/8; G_1 0/8/8/0",
    )
    full_generator_off_diagonal = P_L * G1 * P_R + P_R * G1 * P_L
    check(
        "one-direction and full off-diagonal norms are distinguished",
        frobenius_squared(P_R * G1 * P_L) == 8
        and frobenius_squared(full_generator_off_diagonal) == 16,
        "norms are sqrt(8) and 4",
    )
    composite = sp.I * G1 * XI_5
    check(
        "the composite i G_1 Xi_5 is a Hermitian grading-odd involution",
        is_zero(composite - composite.conjugate().T)
        and anticommutes(composite, GAMMA_5)
        and is_zero(composite * composite - I16),
        "explicitly prevents a bare-Xi_5 no-go overreach",
    )

    print()
    print("== Separate four-dimensional representation replay ==")
    four_generators = standard_four_by_four_generators()
    I4 = sp.eye(4)
    four_grading = (
        four_generators[0]
        * four_generators[1]
        * four_generators[2]
        * four_generators[3]
    )
    four_xi = (
        four_generators[1]
        * four_generators[2]
        * four_generators[3]
        * four_generators[0]
    )
    check(
        "the separate representation obeys the same Clifford relations",
        all(
            is_zero(
                four_generators[left] * four_generators[right]
                + four_generators[right] * four_generators[left]
                - 2 * int(left == right) * I4
            )
            for left in range(4)
            for right in range(4)
        ),
    )
    even_count, odd_count = grading_census(
        four_generators,
        four_grading,
    )
    check(
        "the separate representation repeats Xi_5 and grading census",
        is_zero(four_xi + four_grading)
        and (even_count, odd_count) == (8, 8),
        "eight even products commute; eight odd products anticommute",
    )

    print()
    print("== Exact finite bit-basis return ==")
    projector_o0 = projector(O0)
    projector_t1 = projector(T1)
    projector_t2 = projector(T2)
    projector_o3 = projector(O3)
    basis_t1 = restricted_basis(T1)
    one_step = basis_t1.T * projector_t1 * G1 * projector_t1 * basis_t1
    two_step = (
        basis_t1.T
        * projector_t1
        * G1
        * (projector_o0 + projector_t2)
        * G1
        * projector_t1
        * basis_t1
    )
    two_step_with_o3 = (
        basis_t1.T
        * projector_t1
        * G1
        * (projector_o0 + projector_t2 + projector_o3)
        * G1
        * projector_t1
        * basis_t1
    )
    check(
        "the T_1 bit-basis block has no one-step self-return",
        is_zero(one_step),
    )
    check(
        "the two-step return through O_0 plus T_2 is identity",
        is_zero(two_step - sp.eye(6)),
    )
    check(
        "adding O_3 does not change the first closed return",
        is_zero(two_step_with_o3 - two_step),
    )

    print()
    print("BOUNDARY: no selector, physical carrier, Yukawa/action, chirality-")
    print("  realization, generation, weak-axis, or normalization claim is made.")
    print("BOUNDARY: no negative route-exhaustion or composite-carrier no-go is made.")
    print()
    print(f"RESULT: {PASS_COUNT} PASS, {FAIL_COUNT} FAIL")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
