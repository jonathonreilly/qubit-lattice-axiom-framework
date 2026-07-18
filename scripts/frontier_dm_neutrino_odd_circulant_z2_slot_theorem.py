#!/usr/bin/env python3
"""Exact positive finite-matrix Hermitian-circulant parity theorem.

The runner constructs the full Hermitian commutant independently, checks its
exact basis and coefficient extraction, verifies the parity representation and
entry identity, and executes hostile mutations through the same validators.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    from sympy import (
        I as SYM_I,
        Matrix,
        Rational,
        conjugate,
        eye,
        im,
        re as sym_re,
        simplify,
        sqrt,
        symbols,
        zeros,
    )
except ImportError:
    print("FAIL: sympy is required for exact finite-matrix algebra")
    sys.exit(1)


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "DM_NEUTRINO_ODD_CIRCULANT_Z2_SLOT_THEOREM_NOTE_2026-04-15.md"
)

PASS_COUNT = 0
FAIL_COUNT = 0
MUTATION_KILLS = 0
MUTATION_TOTAL = 0

I3 = eye(3)
S = Matrix(
    [
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
    ]
)
S2 = S * S
P23 = Matrix(
    [
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
    ]
)
BASIS = (I3, S + S2, SYM_I * (S - S2))


def check(name: str, condition: object, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    status = "PASS" if ok else "FAIL"
    message = f"  [{status}] {name}"
    if detail:
        message += f"  ({detail})"
    print(message)
    return ok


def mutation_check(name: str, killed: object) -> bool:
    global MUTATION_KILLS, MUTATION_TOTAL
    MUTATION_TOTAL += 1
    if bool(killed):
        MUTATION_KILLS += 1
    return check(f"Hostile mutation killed: {name}", killed)


def exit_code_for(fail_count: int) -> int:
    return 1 if fail_count else 0


def is_zero_matrix(matrix: Matrix) -> bool:
    return matrix.applyfunc(simplify) == zeros(*matrix.shape)


def hs_inner(left: Matrix, right: Matrix):
    return simplify((left.H * right).trace())


def hs_gram(basis: tuple[Matrix, ...] = BASIS) -> Matrix:
    return Matrix([[hs_inner(left, right) for right in basis] for left in basis])


def extract_coefficients(
    matrix: Matrix, basis: tuple[Matrix, ...] = BASIS
) -> Matrix:
    gram = hs_gram(basis)
    rhs = Matrix([hs_inner(element, matrix) for element in basis])
    return gram.inv() * rhs


def reconstruct(
    coefficients: Matrix, basis: tuple[Matrix, ...] = BASIS
) -> Matrix:
    result = zeros(3, 3)
    for coefficient, element in zip(coefficients, basis):
        result += coefficient * element
    return result.applyfunc(simplify)


def raw_hermitian_circulant(d, c_even, c_odd) -> Matrix:
    """Build the matrix independently from its first-row entry."""
    z = c_even + SYM_I * c_odd
    return Matrix(
        [
            [d, z, conjugate(z)],
            [conjugate(z), d, z],
            [z, conjugate(z), d],
        ]
    ).applyfunc(simplify)


def matrix_from_coefficients(d, c_even, c_odd) -> Matrix:
    return (d * BASIS[0] + c_even * BASIS[1] + c_odd * BASIS[2]).applyfunc(
        simplify
    )


def hermitian_from_coordinates(coordinates: list[int]) -> Matrix:
    return Matrix(
        [
            [
                coordinates[0],
                coordinates[3] + SYM_I * coordinates[4],
                coordinates[5] + SYM_I * coordinates[6],
            ],
            [
                coordinates[3] - SYM_I * coordinates[4],
                coordinates[1],
                coordinates[7] + SYM_I * coordinates[8],
            ],
            [
                coordinates[5] - SYM_I * coordinates[6],
                coordinates[7] - SYM_I * coordinates[8],
                coordinates[2],
            ],
        ]
    )


def hermitian_coordinates(matrix: Matrix) -> Matrix:
    return Matrix(
        [
            sym_re(matrix[0, 0]),
            sym_re(matrix[1, 1]),
            sym_re(matrix[2, 2]),
            sym_re(matrix[0, 1]),
            im(matrix[0, 1]),
            sym_re(matrix[0, 2]),
            im(matrix[0, 2]),
            sym_re(matrix[1, 2]),
            im(matrix[1, 2]),
        ]
    ).applyfunc(simplify)


def commutant_constraint_matrix(shift: Matrix) -> Matrix:
    columns: list[Matrix] = []
    for coordinate_index in range(9):
        coordinates = [0] * 9
        coordinates[coordinate_index] = 1
        hermitian = hermitian_from_coordinates(coordinates)
        commutator = hermitian * shift - shift * hermitian
        entries = list(commutator)
        columns.append(
            Matrix(
                [simplify(sym_re(value)) for value in entries]
                + [simplify(im(value)) for value in entries]
            )
        )
    return Matrix.hstack(*columns)


def validate_supplied_shift(candidate: Matrix) -> bool:
    return (
        candidate == S
        and candidate**3 == I3
        and candidate.H == candidate**2
    )


def validate_commutant_member(matrix: Matrix, shift: Matrix = S) -> bool:
    return is_zero_matrix(matrix - matrix.H) and is_zero_matrix(
        matrix * shift - shift * matrix
    )


def validate_commutant_basis(
    shift: Matrix = S, basis: tuple[Matrix, ...] = BASIS
) -> tuple[bool, int, int, int]:
    constraint = commutant_constraint_matrix(shift)
    nullity = 9 - constraint.rank()
    coordinate_columns = Matrix.hstack(
        *[hermitian_coordinates(element) for element in basis]
    )
    basis_rank = coordinate_columns.rank()
    every_member = all(validate_commutant_member(element, shift) for element in basis)
    spans = nullity == len(basis) and basis_rank == len(basis)
    return every_member and spans, constraint.rank(), nullity, basis_rank


def parity_representation(
    basis: tuple[Matrix, ...] = BASIS, exchange: Matrix = P23
) -> Matrix:
    columns = []
    for element in basis:
        reflected = exchange * element * exchange.H
        columns.append(extract_coefficients(reflected, basis))
    return Matrix.hstack(*columns).applyfunc(simplify)


def validate_parity_signature(expected: tuple[int, int, int]) -> bool:
    return parity_representation() == Matrix.diag(*expected)


def parity_multiplicities(representation: Matrix) -> tuple[int, int]:
    even = len((representation - eye(3)).nullspace())
    odd = len((representation + eye(3)).nullspace())
    return even, odd


def validate_extraction_denominators(denominators: tuple[int, int, int]) -> bool:
    gram = hs_gram()
    diagonal = tuple(gram[index, index] for index in range(3))
    off_diagonal_zero = all(
        gram[row, column] == 0
        for row in range(3)
        for column in range(3)
        if row != column
    )
    return diagonal == denominators and off_diagonal_zero


SIGNED_ZERO_SAMPLES = (
    (Rational(5, 2), Rational(5, 4), Rational(3, 4)),
    (-1, -2, 3),
    (0, Rational(9, 2), Rational(-1, 2)),
    (3, 0, 2),
    (7, Rational(-3, 2), 0),
    (0, 0, 0),
)


def coordinate_identity_holds(
    samples: tuple[tuple[object, object, object], ...], factor: int = 2
) -> bool:
    for d, c_even, c_odd in samples:
        matrix = raw_hermitian_circulant(d, c_even, c_odd)
        direct = simplify(im(matrix[0, 1] * matrix[0, 1]))
        if simplify(direct - factor * c_even * c_odd) != 0:
            return False
    return True


def exact_basis_change() -> Matrix:
    return Matrix(
        [
            [1 / sqrt(2), 1 / sqrt(2), 0],
            [-1 / sqrt(2), 1 / sqrt(2), 0],
            [0, 0, 1],
        ]
    )


def raw_coordinate_polynomial(matrix: Matrix):
    return simplify(im(matrix[0, 1] * matrix[0, 1]))


def raw_coordinate_is_basis_invariant(matrix: Matrix, unitary: Matrix) -> bool:
    transformed = (unitary * matrix * unitary.H).applyfunc(simplify)
    return simplify(
        raw_coordinate_polynomial(transformed) - raw_coordinate_polynomial(matrix)
    ) == 0


def part1_full_hermitian_commutant() -> None:
    print("\n" + "=" * 92)
    print("PART 1: EXACT FULL HERMITIAN COMMUTANT")
    print("=" * 92)

    valid, constraint_rank, nullity, basis_rank = validate_commutant_basis()
    check(
        "The supplied cyclic shift convention is exact",
        validate_supplied_shift(S) and S2 == S**2,
    )
    check(
        "Independent nine-real-coordinate constraints have rank six",
        constraint_rank == 6 and nullity == 3,
        f"rank={constraint_rank}, nullity={nullity}",
    )
    check(
        "I, S+S^2, and i(S-S^2) are independent Hermitian commutant elements",
        basis_rank == 3 and all(validate_commutant_member(element) for element in BASIS),
        f"basis rank={basis_rank}",
    )
    check(
        "The displayed basis spans the full Hermitian commutant",
        valid,
        f"commutant dimension={nullity}, basis rank={basis_rank}",
    )


def part2_gram_extraction_and_parity() -> None:
    print("\n" + "=" * 92)
    print("PART 2: EXACT GRAM MATRIX, EXTRACTION, AND PARITY REPRESENTATION")
    print("=" * 92)

    d, c_even, c_odd = symbols("d c_even c_odd", real=True)
    symbolic_matrix = matrix_from_coefficients(d, c_even, c_odd)
    representation = parity_representation()
    multiplicities = parity_multiplicities(representation)

    check(
        "P23 exchanges S and S^2",
        P23 * S * P23 == S2 and P23 * S2 * P23 == S,
    )
    check(
        "The Hilbert-Schmidt Gram matrix is diag(3,6,6)",
        hs_gram() == Matrix.diag(3, 6, 6),
        f"G={hs_gram()}",
    )
    check(
        "Hilbert-Schmidt extraction recovers the symbolic coefficient triple",
        extract_coefficients(symbolic_matrix) == Matrix([d, c_even, c_odd]),
    )
    check(
        "The independently extracted parity representation is diag(+1,+1,-1)",
        representation == Matrix.diag(1, 1, -1),
        f"R={representation}",
    )
    check(
        "The exact parity multiplicities are two even and one odd",
        multiplicities == (2, 1),
        f"multiplicities={multiplicities}",
    )


def part3_signed_and_zero_extraction_cases() -> None:
    print("\n" + "=" * 92)
    print("PART 3: EXACT SIGNED AND ZERO COEFFICIENT CASES")
    print("=" * 92)

    for index, (d, c_even, c_odd) in enumerate(SIGNED_ZERO_SAMPLES):
        matrix = raw_hermitian_circulant(d, c_even, c_odd)
        expected = Matrix([d, c_even, c_odd])
        extracted = extract_coefficients(matrix)
        check(
            f"Case {index}: extraction and reconstruction recover all coefficients",
            extracted == expected and reconstruct(extracted) == matrix,
            f"expected={tuple(expected)}, extracted={tuple(extracted)}",
        )

    probe = raw_hermitian_circulant(0, Rational(3, 2), Rational(-1, 4))
    check(
        "The supplied entry convention has K_01 = c_even + i c_odd",
        probe[0, 1] == Rational(3, 2) - SYM_I / 4
        and probe[0, 2] == Rational(3, 2) + SYM_I / 4,
        f"K_01={probe[0, 1]}, K_02={probe[0, 2]}",
    )


def part4_exact_coordinate_polynomial() -> None:
    print("\n" + "=" * 92)
    print("PART 4: EXACT COORDINATE POLYNOMIAL")
    print("=" * 92)

    d, c_even, c_odd = symbols("d c_even c_odd", real=True)
    symbolic_matrix = matrix_from_coefficients(d, c_even, c_odd)
    reflected = P23 * symbolic_matrix * P23
    direct = raw_coordinate_polynomial(symbolic_matrix)
    reflected_direct = raw_coordinate_polynomial(reflected)

    check(
        "Actual symbolic entry multiplication gives 2 c_even c_odd",
        simplify(direct - 2 * c_even * c_odd) == 0,
        f"A_01={direct}",
    )
    check(
        "P23 changes the exact coordinate polynomial by one minus sign",
        simplify(reflected_direct + direct) == 0,
        f"A_01(PKP)={reflected_direct}",
    )

    for index, sample in enumerate(SIGNED_ZERO_SAMPLES):
        check(
            f"Case {index}: actual matrix multiplication matches the coordinate identity",
            coordinate_identity_holds((sample,)),
            f"coefficients={sample}",
        )


def part5_exact_basis_transformation() -> None:
    print("\n" + "=" * 92)
    print("PART 5: EXACT SIMULTANEOUS BASIS TRANSFORMATION")
    print("=" * 92)

    unitary = exact_basis_change()
    d, c_even, c_odd = symbols("d c_even c_odd", real=True)
    symbolic_matrix = matrix_from_coefficients(d, c_even, c_odd)
    transformed_basis = tuple(
        (unitary * element * unitary.H).applyfunc(simplify) for element in BASIS
    )
    transformed_matrix = (unitary * symbolic_matrix * unitary.H).applyfunc(simplify)
    transformed_exchange = (unitary * P23 * unitary.H).applyfunc(simplify)
    transformed_representation = parity_representation(
        transformed_basis, transformed_exchange
    )

    check("The chosen basis transformation is exactly unitary", unitary * unitary.H == I3)
    check(
        "Simultaneous conjugation preserves the symbolic coefficient triple",
        extract_coefficients(transformed_matrix, transformed_basis)
        == Matrix([d, c_even, c_odd]),
    )
    check(
        "Simultaneous conjugation preserves parity multiplicities",
        transformed_representation == Matrix.diag(1, 1, -1)
        and parity_multiplicities(transformed_representation) == (2, 1),
    )

    probe = raw_hermitian_circulant(
        Rational(7, 4), Rational(-4, 5), Rational(7, 20)
    )
    transformed_probe = (unitary * probe * unitary.H).applyfunc(simplify)
    original_value = raw_coordinate_polynomial(probe)
    transformed_value = raw_coordinate_polynomial(transformed_probe)
    check(
        "The raw 01-entry polynomial changes under this basis transformation",
        original_value != transformed_value,
        f"original={original_value}, transformed={transformed_value}",
    )


def part6_theorem_surface_consistency() -> None:
    print("\n" + "=" * 92)
    print("PART 6: POSITIVE THEOREM-SURFACE CONSISTENCY")
    print("=" * 92)

    note = NOTE_PATH.read_text(encoding="utf-8")
    required = (
        "**Claim type:** positive_theorem",
        "## Typed theorem surface",
        "**Input.** The displayed finite matrices",
        "**Output.** The exact Hermitian commutant",
        "G = diag(3,6,6)",
        "`(2 even, 1 odd)`",
        "`c_odd` is the unique odd coordinate",
        "A_01(K) := Im[(K_01)^2] = 2 c_even c_odd",
        "The coefficient triple and parity multiplicities are therefore",
        "The raw polynomial `Im[(K'_01)^2]` is coordinate-dependent",
    )
    stale_terms = (
        "physical",
        "leptogenesis",
        "heavy-neutrino",
        "right-Gram",
        "activation",
        "decay asymmetry",
        "kinetics",
        "washout",
        "transport",
        "missing_bridge_theorem",
        "does not",
        "no-go",
        "exclusion",
        "carrier bridge",
        "readout bridge",
    )
    missing = [phrase for phrase in required if phrase not in note]
    leaked = [
        phrase
        for phrase in stale_terms
        if re.search(rf"(?<![A-Za-z]){re.escape(phrase)}(?![A-Za-z])", note, re.I)
    ]

    check(
        "The note declares every finite-matrix input and theorem output",
        not missing,
        f"missing count={len(missing)}",
    )
    check(
        "The theorem surface contains only its positive finite-matrix content",
        not leaked,
        f"stale-term count={len(leaked)}",
    )
    check(
        "Exit policy maps every positive failure count to a nonzero exit",
        exit_code_for(0) == 0
        and exit_code_for(1) != 0
        and exit_code_for(7) != 0,
    )


def part7_hostile_mutations() -> None:
    print("\n" + "=" * 92)
    print("PART 7: HOSTILE MUTATIONS THROUGH LOAD-BEARING VALIDATORS")
    print("=" * 92)

    noncirculant_hermitian = Matrix.diag(1, 2, 3)
    mutation_check(
        "noncirculant Hermitian member",
        not validate_commutant_member(noncirculant_hermitian),
    )
    mutation_check(
        "wrong even/odd parity assignment",
        not validate_parity_signature((1, -1, 1)),
    )
    mutation_check(
        "reversed overall sign in the coordinate identity",
        not coordinate_identity_holds(SIGNED_ZERO_SAMPLES, factor=-2),
    )

    unitary = exact_basis_change()
    probe = raw_hermitian_circulant(
        Rational(7, 4), Rational(-4, 5), Rational(7, 20)
    )
    mutation_check(
        "raw-entry basis-invariance assertion",
        not raw_coordinate_is_basis_invariant(probe, unitary),
    )
    mutation_check(
        "altered coefficient-extraction denominator",
        not validate_extraction_denominators((3, 3, 6)),
    )
    mutation_check(
        "reversed cyclic-shift convention",
        not validate_supplied_shift(S2),
    )


def main() -> int:
    print("=" * 92)
    print("SUPPLIED 3x3 HERMITIAN-CIRCULANT / P23 EVEN-ODD ALGEBRA THEOREM")
    print("=" * 92)
    print()
    print("Typed surface:")
    print("  input  = displayed finite matrices, basis, indices, and trace pairing")
    print("  output = exact commutant, extraction, parity, and coordinate identity")

    part1_full_hermitian_commutant()
    part2_gram_extraction_and_parity()
    part3_signed_and_zero_extraction_cases()
    part4_exact_coordinate_polynomial()
    part5_exact_basis_transformation()
    part6_theorem_surface_consistency()
    part7_hostile_mutations()

    print("\n" + "=" * 92)
    print("RESULT")
    print("=" * 92)
    print("  Positive finite-matrix theorem:")
    print("    - the Hermitian commutant is exactly three-real-dimensional")
    print("    - its parity multiplicities are exactly two even and one odd")
    print("    - Hilbert-Schmidt extraction returns (d, c_even, c_odd)")
    print("    - in the displayed basis Im[(K_01)^2] = 2 c_even c_odd")
    print("    - simultaneous conjugation preserves coefficients and parity")
    print("    - the raw 01-entry polynomial is coordinate-dependent")
    print()
    print(f"MUTATION KILLS={MUTATION_KILLS}/{MUTATION_TOTAL}")
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return exit_code_for(FAIL_COUNT)


if __name__ == "__main__":
    sys.exit(main())
