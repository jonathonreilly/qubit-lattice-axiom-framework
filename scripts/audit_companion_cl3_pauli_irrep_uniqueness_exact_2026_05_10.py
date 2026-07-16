#!/usr/bin/env python3
"""Exact algebra certificate for the Cl(3) Pauli-irrep classification.

The runner constructs the complex Clifford algebra from the defining
relations, rather than starting inside either Pauli representation.  It
certifies:

1. an exact eight-element monomial basis and its complete multiplication table;
2. the ordered volume element omega = gamma_1 gamma_2 gamma_3, its sign,
   centrality, and omega^2 = -1;
3. the complementary central idempotents e_+ = (1 - i omega)/2 and
   e_- = (1 + i omega)/2;
4. two complementary four-dimensional two-sided ideals;
5. explicit algebra isomorphisms from those ideals to M_2(C);
6. the resulting two irreducible complex module classes and the faithfulness
   distinction between the complexification and the original real algebra;
7. the unitary-equivalence refinement under the explicit *-representation
   (Hermitian-generator) hypothesis.

All arithmetic is exact SymPy symbolic arithmetic.  The algebra,
ideal-isomorphism, and module-classification checks are rational/Gaussian-
rational; the conditional unitary control additionally uses exact ``sqrt(2)``.
The default run also executes hostile controls.  ``--inject-failure`` promotes
one hostile fixture to a primary check, so the process must exit nonzero.
"""

from __future__ import annotations

import argparse
import itertools
import sys
from typing import Callable, Sequence

try:
    import sympy as sp
    from sympy import I, Matrix, Rational, eye, simplify, symbols, zeros
except ImportError:
    print("FAIL: sympy is required for exact algebra")
    raise SystemExit(1)


DIM = 8
PASS = 0
FAIL = 0

CANONICAL_MASKS = (0, 1, 2, 4, 3, 5, 6, 7)
BASIS_NAME = {
    0: "1",
    1: "g1",
    2: "g2",
    4: "g3",
    3: "g12",
    5: "g13",
    6: "g23",
    7: "omega",
}


def check(label: str, result: object, detail: str = "") -> bool:
    """Record one computed check."""
    global PASS, FAIL
    ok = bool(result)
    if ok:
        PASS += 1
        status = "PASS (A)"
    else:
        FAIL += 1
        status = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")
    return ok


def section(title: str) -> None:
    print()
    print("-" * 96)
    print(title)
    print("-" * 96)


def blade(mask: int) -> Matrix:
    return Matrix(
        [sp.Integer(1) if row == mask else sp.Integer(0) for row in range(DIM)]
    )


def blade_product(left_mask: int, right_mask: int) -> tuple[int, int]:
    """Return the exact sign and output mask for Euclidean Cl(3,0)."""
    swaps = 0
    for left_bit in range(3):
        if left_mask & (1 << left_bit):
            swaps += sum(
                1
                for right_bit in range(left_bit)
                if right_mask & (1 << right_bit)
            )
    sign = -1 if swaps % 2 else 1
    return sign, left_mask ^ right_mask


PRODUCT_TABLE = [
    [blade_product(left, right) for right in range(DIM)]
    for left in range(DIM)
]


def algebra_product(
    left: Matrix,
    right: Matrix,
    table: Sequence[Sequence[tuple[int, int]]] = PRODUCT_TABLE,
) -> Matrix:
    out = zeros(DIM, 1)
    for left_mask in range(DIM):
        for right_mask in range(DIM):
            sign, out_mask = table[left_mask][right_mask]
            out[out_mask] += sign * left[left_mask] * right[right_mask]
    return out.applyfunc(sp.expand)


def vector_eq(left: Matrix, right: Matrix) -> bool:
    return left.shape == right.shape and all(
        simplify(left[row] - right[row]) == 0 for row in range(left.rows)
    )


def matrix_eq(left: Matrix, right: Matrix) -> bool:
    return left.shape == right.shape and all(
        simplify(left[row, col] - right[row, col]) == 0
        for row in range(left.rows)
        for col in range(left.cols)
    )


def vector_rank(vectors: Sequence[Matrix]) -> int:
    if not vectors:
        return 0
    return Matrix.hstack(*vectors).rank()


def same_span(left: Sequence[Matrix], right: Sequence[Matrix]) -> bool:
    left_rank = vector_rank(left)
    right_rank = vector_rank(right)
    combined_rank = vector_rank([*left, *right])
    return left_rank == right_rank == combined_rank


def in_span(vector: Matrix, spanning_vectors: Sequence[Matrix]) -> bool:
    rank = vector_rank(spanning_vectors)
    return vector_rank([*spanning_vectors, vector]) == rank


def matrix_coordinates(matrix: Matrix) -> Matrix:
    return Matrix(
        [matrix[row, col] for row in range(matrix.rows) for col in range(matrix.cols)]
    )


def real_matrix_coordinates(matrix: Matrix) -> Matrix:
    coordinates: list[sp.Expr] = []
    for row in range(matrix.rows):
        for col in range(matrix.cols):
            coordinates.extend(
                [sp.expand_complex(matrix[row, col]).as_real_imag()[0],
                 sp.expand_complex(matrix[row, col]).as_real_imag()[1]]
            )
    return Matrix(coordinates)


def representation_images(sign: int, pauli: Sequence[Matrix]) -> list[Matrix]:
    """Images of all ordered blades under gamma_i -> sign sigma_i."""
    images: list[Matrix] = []
    for mask in range(DIM):
        image = eye(2)
        for bit in range(3):
            if mask & (1 << bit):
                image = image * (sign * pauli[bit])
        images.append(image.applyfunc(sp.expand))
    return images


def representation_of_vector(vector: Matrix, images: Sequence[Matrix]) -> Matrix:
    image = zeros(2, 2)
    for mask in range(DIM):
        image += vector[mask] * images[mask]
    return image.applyfunc(sp.expand)


def homomorphism_ok(
    images: Sequence[Matrix],
    table: Sequence[Sequence[tuple[int, int]]] = PRODUCT_TABLE,
) -> bool:
    basis = [blade(mask) for mask in range(DIM)]
    for left_mask, right_mask in itertools.product(range(DIM), repeat=2):
        product = algebra_product(
            basis[left_mask],
            basis[right_mask],
            table,
        )
        if not matrix_eq(
            representation_of_vector(product, images),
            images[left_mask] * images[right_mask],
        ):
            return False
    return True


def table_relations_ok(
    table: Sequence[Sequence[tuple[int, int]]],
    gammas: Sequence[Matrix],
    one: Matrix,
) -> bool:
    zero = zeros(DIM, 1)
    for i, gamma_i in enumerate(gammas):
        for j, gamma_j in enumerate(gammas):
            anticommutator = algebra_product(
                gamma_i, gamma_j, table
            ) + algebra_product(gamma_j, gamma_i, table)
            expected = 2 * one if i == j else zero
            if not vector_eq(anticommutator, expected):
                return False
    return True


def idempotent_axioms_ok(
    e_plus: Matrix,
    e_minus: Matrix,
    basis: Sequence[Matrix],
    one: Matrix,
) -> bool:
    zero = zeros(DIM, 1)
    algebra_identities = (
        vector_eq(e_plus + e_minus, one),
        vector_eq(algebra_product(e_plus, e_minus), zero),
        vector_eq(algebra_product(e_minus, e_plus), zero),
        vector_eq(algebra_product(e_plus, e_plus), e_plus),
        vector_eq(algebra_product(e_minus, e_minus), e_minus),
    )
    centrality = all(
        vector_eq(
            algebra_product(e, element),
            algebra_product(element, e),
        )
        for e in (e_plus, e_minus)
        for element in basis
    )
    return all(algebra_identities) and centrality


def labelled_idempotents_ok(
    e_plus: Matrix,
    e_minus: Matrix,
    basis: Sequence[Matrix],
    one: Matrix,
    omega: Matrix,
    images_plus: Sequence[Matrix],
    images_minus: Sequence[Matrix],
) -> bool:
    zero_2 = zeros(2, 2)
    identity_2 = eye(2)
    return (
        idempotent_axioms_ok(e_plus, e_minus, basis, one)
        and vector_eq(algebra_product(omega, e_plus), I * e_plus)
        and vector_eq(algebra_product(omega, e_minus), -I * e_minus)
        and matrix_eq(representation_of_vector(e_plus, images_plus), identity_2)
        and matrix_eq(representation_of_vector(e_minus, images_plus), zero_2)
        and matrix_eq(representation_of_vector(e_plus, images_minus), zero_2)
        and matrix_eq(representation_of_vector(e_minus, images_minus), identity_2)
    )


def volume_convention_ok(
    candidate: Matrix,
    ordered_volume: Matrix,
    images_plus: Sequence[Matrix],
    images_minus: Sequence[Matrix],
) -> bool:
    identity_2 = eye(2)
    return (
        vector_eq(candidate, ordered_volume)
        and matrix_eq(representation_of_vector(candidate, images_plus), I * identity_2)
        and matrix_eq(
            representation_of_vector(candidate, images_minus),
            -I * identity_2,
        )
    )


def basis_certificate_ok(
    candidate_basis: Sequence[Matrix],
    images_plus: Sequence[Matrix],
    images_minus: Sequence[Matrix],
) -> bool:
    if len(candidate_basis) != DIM or vector_rank(candidate_basis) != DIM:
        return False
    joint_columns = [
        Matrix.vstack(
            matrix_coordinates(representation_of_vector(element, images_plus)),
            matrix_coordinates(representation_of_vector(element, images_minus)),
        )
        for element in candidate_basis
    ]
    return Matrix.hstack(*joint_columns).rank() == DIM


def ideal_basis(idempotent: Matrix, basis: Sequence[Matrix]) -> list[Matrix]:
    return Matrix.hstack(
        *[algebra_product(element, idempotent) for element in basis]
    ).columnspace()


def ideal_homomorphism_ok(
    ideal_generators: Sequence[Matrix],
    images: Sequence[Matrix],
) -> bool:
    for left, right in itertools.product(ideal_generators, repeat=2):
        if not matrix_eq(
            representation_of_vector(algebra_product(left, right), images),
            representation_of_vector(left, images)
            * representation_of_vector(right, images),
        ):
            return False
    return True


def print_multiplication_table() -> None:
    print("Exact multiplication table (rows multiply columns):")
    header = "         " + " ".join(f"{BASIS_NAME[m]:>7}" for m in CANONICAL_MASKS)
    print(header)
    for left_mask in CANONICAL_MASKS:
        entries = []
        for right_mask in CANONICAL_MASKS:
            sign, out_mask = PRODUCT_TABLE[left_mask][right_mask]
            prefix = "-" if sign == -1 else ""
            entries.append(f"{prefix}{BASIS_NAME[out_mask]}")
        print(
            f"{BASIS_NAME[left_mask]:>7} "
            + " ".join(f"{entry:>7}" for entry in entries)
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inject-failure",
        choices=(
            "wrong-volume-sign",
            "swapped-idempotents",
            "malformed-idempotents",
            "incomplete-basis",
            "wrong-clifford-relation",
            "non-homomorphic-map",
        ),
        help="Promote one hostile fixture to a primary check; exit must be nonzero.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    print("=" * 96)
    print("Exact abstract-algebra certificate for")
    print("CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10")
    print("Arithmetic: exact SymPy symbolic; algebra core Gaussian-rational; no floats")
    print("=" * 96)

    basis_by_mask = [blade(mask) for mask in range(DIM)]
    basis = [basis_by_mask[mask] for mask in CANONICAL_MASKS]
    one = basis_by_mask[0]
    gamma_1, gamma_2, gamma_3 = (
        basis_by_mask[1],
        basis_by_mask[2],
        basis_by_mask[4],
    )
    gammas = [gamma_1, gamma_2, gamma_3]
    zero = zeros(DIM, 1)

    sigma_1 = Matrix([[0, 1], [1, 0]])
    sigma_2 = Matrix([[0, -I], [I, 0]])
    sigma_3 = Matrix([[1, 0], [0, -1]])
    pauli = [sigma_1, sigma_2, sigma_3]
    identity_2 = eye(2)
    zero_2 = zeros(2, 2)

    images_plus = representation_images(1, pauli)
    images_minus = representation_images(-1, pauli)

    # ------------------------------------------------------------------ A
    section("Part A: eight-dimensional algebra from the defining relations")
    print_multiplication_table()

    associativity_results = []
    for left, middle, right in itertools.product(basis, repeat=3):
        associativity_results.append(
            vector_eq(
                algebra_product(algebra_product(left, middle), right),
                algebra_product(left, algebra_product(middle, right)),
            )
        )
    check(
        "A1 complete 8^3 basis associativity table",
        sum(int(result) for result in associativity_results)
        == len(associativity_results),
        f"{sum(int(result) for result in associativity_results)}/"
        f"{len(associativity_results)} products",
    )

    clifford_results = []
    for i, gamma_i in enumerate(gammas):
        for j, gamma_j in enumerate(gammas):
            anticommutator = algebra_product(
                gamma_i, gamma_j
            ) + algebra_product(gamma_j, gamma_i)
            expected = 2 * one if i == j else zero
            clifford_results.append(vector_eq(anticommutator, expected))
    check(
        "A2 all defining Clifford relations hold in the abstract table",
        sum(int(result) for result in clifford_results) == len(clifford_results),
        f"{sum(int(result) for result in clifford_results)}/"
        f"{len(clifford_results)} relations",
    )

    generated_blades = [
        one,
        gamma_1,
        gamma_2,
        gamma_3,
        algebra_product(gamma_1, gamma_2),
        algebra_product(gamma_1, gamma_3),
        algebra_product(gamma_2, gamma_3),
        algebra_product(algebra_product(gamma_1, gamma_2), gamma_3),
    ]
    check(
        "A3 ordered generator monomials give the complete canonical basis",
        all(vector_eq(left, right) for left, right in zip(generated_blades, basis))
        and vector_rank(generated_blades) == DIM,
        f"rank={vector_rank(generated_blades)}",
    )

    joint_columns = [
        Matrix.vstack(
            matrix_coordinates(images_plus[mask]),
            matrix_coordinates(images_minus[mask]),
        )
        for mask in CANONICAL_MASKS
    ]
    joint_matrix = Matrix.hstack(*joint_columns)
    check(
        "A4 joint Pauli map has full complex rank 8",
        joint_matrix.rank() == DIM and simplify(joint_matrix.det()) != 0,
        f"rank={joint_matrix.rank()}, det={simplify(joint_matrix.det())}",
    )

    check(
        "A5 rho_+ respects all 64 abstract basis products",
        homomorphism_ok(images_plus),
    )
    check(
        "A6 rho_- respects all 64 abstract basis products",
        homomorphism_ok(images_minus),
    )

    # ------------------------------------------------------------------ B
    section("Part B: ordered volume element and central idempotents")
    ordered_volume = algebra_product(
        algebra_product(gamma_1, gamma_2),
        gamma_3,
    )
    omega = basis_by_mask[7]
    check(
        "B1 omega is the ordered product gamma_1 gamma_2 gamma_3",
        vector_eq(ordered_volume, omega),
    )
    check(
        "B2 omega^2 = -1 in the abstract algebra",
        vector_eq(algebra_product(omega, omega), -one),
    )
    omega_central_results = [
        vector_eq(
            algebra_product(omega, element),
            algebra_product(element, omega),
        )
        for element in basis
    ]
    check(
        "B3 omega commutes with the complete eight-element basis",
        sum(int(result) for result in omega_central_results)
        == len(omega_central_results),
        f"{sum(int(result) for result in omega_central_results)}/"
        f"{len(omega_central_results)} commutators",
    )
    check(
        "B4 ordered sign convention gives rho_+(omega)=+iI and rho_-(omega)=-iI",
        volume_convention_ok(
            omega,
            ordered_volume,
            images_plus,
            images_minus,
        ),
    )

    e_plus = Rational(1, 2) * (one - I * omega)
    e_minus = Rational(1, 2) * (one + I * omega)
    check(
        "B5 e_+=(1-i omega)/2 and e_-=(1+i omega)/2 are central orthogonal idempotents",
        idempotent_axioms_ok(e_plus, e_minus, basis, one),
    )
    check(
        "B6 idempotent labels match omega e_+=+i e_+ and omega e_-=-i e_-",
        labelled_idempotents_ok(
            e_plus,
            e_minus,
            basis,
            one,
            omega,
            images_plus,
            images_minus,
        ),
    )

    # ------------------------------------------------------------------ C
    section("Part C: complementary four-dimensional two-sided ideals")
    plus_generators = [
        algebra_product(element, e_plus)
        for element in (one, gamma_1, gamma_2, gamma_3)
    ]
    minus_generators = [
        algebra_product(element, e_minus)
        for element in (one, gamma_1, gamma_2, gamma_3)
    ]
    plus_full = ideal_basis(e_plus, basis)
    minus_full = ideal_basis(e_minus, basis)

    check(
        "C1 A e_+ is four-dimensional with basis {e_+,g1e_+,g2e_+,g3e_+}",
        vector_rank(plus_generators) == 4
        and same_span(plus_generators, plus_full),
        f"chosen rank={vector_rank(plus_generators)}, ideal rank={vector_rank(plus_full)}",
    )
    check(
        "C2 A e_- is four-dimensional with basis {e_-,g1e_-,g2e_-,g3e_-}",
        vector_rank(minus_generators) == 4
        and same_span(minus_generators, minus_full),
        f"chosen rank={vector_rank(minus_generators)}, ideal rank={vector_rank(minus_full)}",
    )

    reduction_results = []
    for sign, idempotent in ((1, e_plus), (-1, e_minus)):
        e, g1e, g2e, g3e = [
            algebra_product(element, idempotent)
            for element in (one, gamma_1, gamma_2, gamma_3)
        ]
        reduction_results.extend(
            [
                vector_eq(algebra_product(omega, idempotent), sign * I * e),
                vector_eq(
                    algebra_product(basis_by_mask[3], idempotent),
                    sign * I * g3e,
                ),
                vector_eq(
                    algebra_product(basis_by_mask[5], idempotent),
                    -sign * I * g2e,
                ),
                vector_eq(
                    algebra_product(basis_by_mask[6], idempotent),
                    sign * I * g1e,
                ),
            ]
        )
    check(
        "C3 bivectors and omega reduce to the four stated ideal basis vectors",
        sum(int(result) for result in reduction_results) == len(reduction_results),
        f"{sum(int(result) for result in reduction_results)}/"
        f"{len(reduction_results)} reductions",
    )

    two_sided_results = []
    for ideal_generators in (plus_generators, minus_generators):
        for algebra_element, ideal_element in itertools.product(
            basis, ideal_generators
        ):
            two_sided_results.extend(
                [
                    in_span(
                        algebra_product(algebra_element, ideal_element),
                        ideal_generators,
                    ),
                    in_span(
                        algebra_product(ideal_element, algebra_element),
                        ideal_generators,
                    ),
                ]
            )
    check(
        "C4 exhaustive left/right closure of both ideals",
        sum(int(result) for result in two_sided_results) == len(two_sided_results),
        f"{sum(int(result) for result in two_sided_results)}/"
        f"{len(two_sided_results)} products",
    )

    cross_results = [
        vector_eq(algebra_product(left, right), zero)
        for left, right in itertools.product(plus_generators, minus_generators)
    ] + [
        vector_eq(algebra_product(left, right), zero)
        for left, right in itertools.product(minus_generators, plus_generators)
    ]
    combined_rank = vector_rank([*plus_generators, *minus_generators])
    check(
        "C5 A e_+ and A e_- annihilate each other and form an 8-dimensional direct sum",
        sum(int(result) for result in cross_results) == len(cross_results)
        and combined_rank == DIM,
        f"cross products={sum(int(result) for result in cross_results)}/"
        f"{len(cross_results)}, combined rank={combined_rank}",
    )

    # ------------------------------------------------------------------ D
    section("Part D: explicit ideal isomorphisms to M_2(C)")
    for sign, label, idempotent, ideal_generators, images in (
        (1, "+", e_plus, plus_generators, images_plus),
        (-1, "-", e_minus, minus_generators, images_minus),
    ):
        expected_images = [identity_2, *(sign * sigma for sigma in pauli)]
        actual_images = [
            representation_of_vector(element, images)
            for element in ideal_generators
        ]
        check(
            f"D1{label} Phi_{label}(e_{label},g1e_{label},g2e_{label},g3e_{label}) "
            f"= (I,{label}sigma1,{label}sigma2,{label}sigma3)",
            all(
                matrix_eq(actual, expected)
                for actual, expected in zip(actual_images, expected_images)
            ),
        )
        image_matrix = Matrix.hstack(
            *[matrix_coordinates(image) for image in actual_images]
        )
        check(
            f"D2{label} Phi_{label} is surjective onto the four-dimensional M_2(C)",
            image_matrix.rank() == 4,
            f"image rank={image_matrix.rank()}",
        )
        check(
            f"D3{label} Phi_{label} has zero kernel on its four-dimensional domain",
            vector_rank(ideal_generators) == 4 and image_matrix.nullspace() == [],
            f"domain rank={vector_rank(ideal_generators)}, kernel dim="
            f"{len(image_matrix.nullspace())}",
        )
        check(
            f"D4{label} Phi_{label} preserves all 16 products of the ideal basis",
            ideal_homomorphism_ok(ideal_generators, images),
        )
        check(
            f"D5{label} Phi_{label} sends the ideal unit e_{label} to I_2",
            matrix_eq(
                representation_of_vector(idempotent, images),
                identity_2,
            ),
        )

    matrix_units = {
        (0, 0): Matrix([[1, 0], [0, 0]]),
        (0, 1): Matrix([[0, 1], [0, 0]]),
        (1, 0): Matrix([[0, 0], [1, 0]]),
        (1, 1): Matrix([[0, 0], [0, 1]]),
    }
    matrix_unit_results = []
    for a, b, c, d in itertools.product(range(2), repeat=4):
        expected = matrix_units[(a, d)] if b == c else zero_2
        matrix_unit_results.append(
            matrix_eq(
                matrix_units[(a, b)] * matrix_units[(c, d)],
                expected,
            )
        )
    check(
        "D6 all matrix-unit identities E_ab E_cd = delta_bc E_ad hold",
        sum(int(result) for result in matrix_unit_results)
        == len(matrix_unit_results),
        f"{sum(int(result) for result in matrix_unit_results)}/"
        f"{len(matrix_unit_results)} products",
    )

    x11, x12, x21, x22 = symbols("x11 x12 x21 x22")
    generic_matrix = Matrix([[x11, x12], [x21, x22]])
    coefficients = {
        (0, 0): x11,
        (0, 1): x12,
        (1, 0): x21,
        (1, 1): x22,
    }
    isolation_results = []
    for p, a, b, q in itertools.product(range(2), repeat=4):
        isolation_results.append(
            matrix_eq(
                matrix_units[(p, a)] * generic_matrix * matrix_units[(b, q)],
                coefficients[(a, b)] * matrix_units[(p, q)],
            )
        )
    check(
        "D7 any nonzero two-sided ideal of M_2(C) contains every matrix unit",
        sum(int(result) for result in isolation_results) == len(isolation_results),
        f"{sum(int(result) for result in isolation_results)}/"
        f"{len(isolation_results)} coefficient-isolation identities",
    )

    # ------------------------------------------------------------------ E
    section("Part E: representation classification and faithfulness boundary")
    for sign, label, images, opposite_ideal in (
        (1, "+", images_plus, minus_generators),
        (-1, "-", images_minus, plus_generators),
    ):
        complex_map = Matrix.hstack(
            *[matrix_coordinates(images[mask]) for mask in CANONICAL_MASKS]
        )
        kernel_coordinates = complex_map.nullspace()
        kernel = [
            sum(
                (
                    coordinate[column] * basis_by_mask[mask]
                    for column, mask in enumerate(CANONICAL_MASKS)
                ),
                zeros(DIM, 1),
            )
            for coordinate in kernel_coordinates
        ]
        check(
            f"E1{label} complexified rho_{label} has rank 4 and kernel dimension 4",
            complex_map.rank() == 4
            and len(kernel) == 4
            and same_span(kernel, opposite_ideal),
            f"rank={complex_map.rank()}, kernel dim={len(kernel)}",
        )

        real_map = Matrix.hstack(
            *[real_matrix_coordinates(images[mask]) for mask in CANONICAL_MASKS]
        )
        check(
            f"E2{label} restriction of rho_{label} to real Cl(3,0) is faithful",
            real_map.rank() == DIM,
            f"real rank={real_map.rank()}",
        )

    lambda_plus, lambda_minus = symbols("lambda_plus lambda_minus")
    central_action_solutions = sp.solve(
        [
            lambda_plus**2 - lambda_plus,
            lambda_minus**2 - lambda_minus,
            lambda_plus + lambda_minus - 1,
            lambda_plus * lambda_minus,
        ],
        [lambda_plus, lambda_minus],
        dict=True,
    )
    central_action_pairs = {
        (
            simplify(solution[lambda_plus]),
            simplify(solution[lambda_minus]),
        )
        for solution in central_action_solutions
    }
    check(
        "E3 complementary central idempotents have only scalar action pairs (1,0) and (0,1)",
        central_action_pairs
        == {
            (sp.Integer(1), sp.Integer(0)),
            (sp.Integer(0), sp.Integer(1)),
        },
        f"solutions={sorted(central_action_pairs, key=str)}",
    )

    commutator_columns = []
    for candidate_unit in (
        matrix_units[(0, 0)],
        matrix_units[(0, 1)],
        matrix_units[(1, 0)],
        matrix_units[(1, 1)],
    ):
        column_entries: list[sp.Expr] = []
        for algebra_unit in matrix_units.values():
            column_entries.extend(
                list(matrix_coordinates(candidate_unit * algebra_unit - algebra_unit * candidate_unit))
            )
        commutator_columns.append(Matrix(column_entries))
    commutant_constraint = Matrix.hstack(*commutator_columns)
    commutant = commutant_constraint.nullspace()
    check(
        "E4 the commutant of the natural M_2(C) module is exactly C I_2",
        len(commutant) == 1
        and same_span(
            commutant,
            [Matrix([1, 0, 0, 1])],
        ),
        f"commutant dimension={len(commutant)}",
    )

    standard_action_results = []
    e1 = Matrix([1, 0])
    e2 = Matrix([0, 1])
    for target in (e1, e2):
        for source in (e1, e2):
            source_index = 0 if source == e1 else 1
            target_index = 0 if target == e1 else 1
            standard_action_results.append(
                matrix_eq(
                    matrix_units[(target_index, source_index)] * source,
                    target,
                )
            )
    check(
        "E5 matrix units generate C^2 from every nonzero coordinate direction",
        sum(int(result) for result in standard_action_results)
        == len(standard_action_results),
        f"{sum(int(result) for result in standard_action_results)}/"
        f"{len(standard_action_results)} actions",
    )

    e11 = matrix_units[(0, 0)]
    e12 = matrix_units[(0, 1)]
    e21 = matrix_units[(1, 0)]
    module_inverse_results = [
        matrix_eq(e11 + e21 * e12, identity_2),
        matrix_eq(e11 * e11, e11),
        matrix_eq(e12 * e11, zero_2),
        matrix_eq(e11 * e21 * e11, zero_2),
        matrix_eq(e12 * e21 * e11, e11),
    ]
    check(
        "E6 the matrix-unit F/G maps are inverse on every unital M_2(C)-module",
        sum(int(result) for result in module_inverse_results)
        == len(module_inverse_results),
        f"{sum(int(result) for result in module_inverse_results)}/"
        f"{len(module_inverse_results)} universal identities",
    )

    f_operators = (e11, e21)
    module_linearity_results = []
    for a, b, source_index in itertools.product(range(2), repeat=3):
        left = matrix_units[(a, b)] * f_operators[source_index] * e11
        right = f_operators[a] * e11 if b == source_index else zero_2
        module_linearity_results.append(matrix_eq(left, right))
    check(
        "E7 F(e_j tensor w) is M_2(C)-linear for arbitrary w in E_11 V",
        sum(int(result) for result in module_linearity_results)
        == len(module_linearity_results),
        f"{sum(int(result) for result in module_linearity_results)}/"
        f"{len(module_linearity_results)} matrix-unit actions",
    )

    check(
        "E8 rho_+ and rho_- are inequivalent because omega has eigenvalues +i and -i",
        not matrix_eq(
            representation_of_vector(omega, images_plus),
            representation_of_vector(omega, images_minus),
        ),
    )

    # ------------------------------------------------------------------ F
    section("Part F: conditional unitary refinement for *-representations")
    adjoint = lambda matrix: matrix.conjugate().T

    hadamard = Rational(1, 1) / sp.sqrt(2) * Matrix([[1, 1], [1, -1]])
    scaled_hadamard = 3 * hadamard
    scaled_images = [
        scaled_hadamard * sigma * scaled_hadamard.inv() for sigma in pauli
    ]
    scaled_gram = adjoint(scaled_hadamard) * scaled_hadamard
    check(
        "F1 scaled-unitary intertwiner preserves Hermitian generators",
        all(matrix_eq(image, adjoint(image)) for image in scaled_images),
    )
    check(
        "F2 its Gram matrix is the positive scalar 9 I and lies in the commutant",
        matrix_eq(scaled_gram, 9 * identity_2)
        and all(
            matrix_eq(scaled_gram * sigma, sigma * scaled_gram)
            for sigma in pauli
        ),
    )

    nonunitary = Matrix([[2, 0], [0, 1]])
    nonunitary_images = [
        nonunitary * sigma * nonunitary.inv() for sigma in pauli
    ]
    nonunitary_clifford_results = []
    for i, image_i in enumerate(nonunitary_images):
        for j, image_j in enumerate(nonunitary_images):
            expected = 2 * identity_2 if i == j else zero_2
            nonunitary_clifford_results.append(
                matrix_eq(image_i * image_j + image_j * image_i, expected)
            )
    nonunitary_gram = adjoint(nonunitary) * nonunitary
    check(
        "F3 nonunitary similarity still preserves all Clifford relations",
        sum(int(result) for result in nonunitary_clifford_results)
        == len(nonunitary_clifford_results),
        f"{sum(int(result) for result in nonunitary_clifford_results)}/"
        f"{len(nonunitary_clifford_results)} relations",
    )
    check(
        "F4 nonunitary similarity leaves the *-representation class",
        any(
            not matrix_eq(image, adjoint(image))
            for image in nonunitary_images
        )
        and not matrix_eq(
            nonunitary_gram,
            (nonunitary_gram.trace() / 2) * identity_2,
        ),
        f"T^dagger T={nonunitary_gram.tolist()}",
    )

    # ------------------------------------------------------------------ H
    section("Part H: hostile controls")
    wrong_volume = -omega
    swapped_plus, swapped_minus = e_minus, e_plus
    malformed_plus = Rational(1, 3) * (one - I * omega)
    malformed_minus = one - malformed_plus
    incomplete_basis = basis[:-1]

    wrong_table = [list(row) for row in PRODUCT_TABLE]
    wrong_table[1][1] = (-1, 0)

    bad_images = list(images_plus)
    bad_images[3] = -bad_images[3]

    hostile_predicates: dict[str, Callable[[], bool]] = {
        "wrong-volume-sign": lambda: volume_convention_ok(
            wrong_volume,
            ordered_volume,
            images_plus,
            images_minus,
        ),
        "swapped-idempotents": lambda: labelled_idempotents_ok(
            swapped_plus,
            swapped_minus,
            basis,
            one,
            omega,
            images_plus,
            images_minus,
        ),
        "malformed-idempotents": lambda: idempotent_axioms_ok(
            malformed_plus,
            malformed_minus,
            basis,
            one,
        ),
        "incomplete-basis": lambda: basis_certificate_ok(
            incomplete_basis,
            images_plus,
            images_minus,
        ),
        "wrong-clifford-relation": lambda: table_relations_ok(
            wrong_table,
            gammas,
            one,
        ),
        "non-homomorphic-map": lambda: homomorphism_ok(bad_images),
    }

    for hostile_name, predicate in hostile_predicates.items():
        check(
            f"H reject hostile fixture: {hostile_name}",
            not predicate(),
        )

    if args.inject_failure:
        check(
            f"INTENTIONAL FAILURE fixture promoted: {args.inject_failure}",
            hostile_predicates[args.inject_failure](),
            detail="this run must exit nonzero",
        )

    # ---------------------------------------------------------------- summary
    section("Summary")
    print("  Certified from the defining relations:")
    print("    A_C has the exact basis {1,g1,g2,g3,g12,g13,g23,omega}.")
    print("    omega=g1 g2 g3 is central, omega^2=-1, and fixes the idempotent labels.")
    print("    A_C=A_C e_+ direct-sum A_C e_-, with both ideals four-dimensional.")
    print("    Phi_+: A_C e_+ -> M_2(C) and Phi_-: A_C e_- -> M_2(C) are isomorphisms.")
    print("    Therefore A_C has exactly two simple summands and two irreducible module classes.")
    print("    The two complexified irreps kill opposite ideals; their real Cl(3,0)")
    print("    restrictions are faithful. No lattice carrier or physical selection is inferred.")
    print()
    print("=" * 96)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 96)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
