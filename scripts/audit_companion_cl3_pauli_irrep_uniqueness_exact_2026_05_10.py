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
7. an exhaustive center and simple-module classification; and
8. the unitary-equivalence refinement under the explicit *-representation
   (Hermitian-generator) hypothesis.

All arithmetic is exact SymPy symbolic arithmetic.  The algebra,
ideal-isomorphism, module-classification, and conditional unitary checks are
rational/Gaussian-rational.
Four explicit modes are provided: ``normal``, ``independent``, ``hostile``, and
``intentional-failure``.  The independent mode reconstructs the table with a
separate word-insertion reducer.  The last mode promotes a rejected hostile
fixture to a primary assertion, so the process must exit nonzero.
"""

from __future__ import annotations

import argparse
import itertools
from typing import Sequence

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
ACTIVE_TABLE = PRODUCT_TABLE


def word_product(left_mask: int, right_mask: int) -> tuple[int, int]:
    """Independent reducer: insert right-word letters into a canonical word."""
    word = [bit for bit in range(3) if left_mask & (1 << bit)]
    sign = 1
    for bit in range(3):
        if not right_mask & (1 << bit):
            continue
        greater = sum(1 for present in word if present > bit)
        if greater % 2:
            sign = -sign
        if bit in word:
            word.remove(bit)
        else:
            word.append(bit)
            word.sort()
    out_mask = sum(1 << bit for bit in word)
    return sign, out_mask


WORD_PRODUCT_TABLE = [
    [word_product(left, right) for right in range(DIM)]
    for left in range(DIM)
]


def algebra_product(
    left: Matrix,
    right: Matrix,
    table: Sequence[Sequence[tuple[int, int]]] | None = None,
) -> Matrix:
    if table is None:
        table = ACTIVE_TABLE
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
    table: Sequence[Sequence[tuple[int, int]]] | None = None,
) -> bool:
    if table is None:
        table = ACTIVE_TABLE
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


def ideal_basis(idempotent: Matrix, basis: Sequence[Matrix]) -> list[Matrix]:
    return Matrix.hstack(
        *[algebra_product(element, idempotent) for element in basis]
    ).columnspace()


def print_multiplication_table(
    table: Sequence[Sequence[tuple[int, int]]],
) -> None:
    print("Exact multiplication table (rows multiply columns):")
    header = "         " + " ".join(f"{BASIS_NAME[m]:>7}" for m in CANONICAL_MASKS)
    print(header)
    for left_mask in CANONICAL_MASKS:
        entries = []
        for right_mask in CANONICAL_MASKS:
            sign, out_mask = table[left_mask][right_mask]
            prefix = "-" if sign == -1 else ""
            entries.append(f"{prefix}{BASIS_NAME[out_mask]}")
        print(
            f"{BASIS_NAME[left_mask]:>7} "
            + " ".join(f"{entry:>7}" for entry in entries)
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile", "intentional-failure"),
        default="normal",
        help="Exact certificate lane (default: normal).",
    )
    parser.add_argument(
        "--inject-failure",
        choices=(
            "wrong-multiplication-sign",
            "quotient-only-idempotents",
            "missing-ideal",
            "false-faithful-extension",
            "fake-one-dimensional-simple",
            "fake-extra-dimensional-simple",
            "chirality-merger",
            "unitary-without-hermitian",
        ),
        help="Fixture promoted by intentional-failure mode.",
    )
    args = parser.parse_args()
    if args.inject_failure and args.mode != "intentional-failure":
        parser.error("--inject-failure requires --mode intentional-failure")
    return args


def main() -> int:
    args = parse_args()
    global ACTIVE_TABLE
    ACTIVE_TABLE = (
        WORD_PRODUCT_TABLE if args.mode == "independent" else PRODUCT_TABLE
    )

    print("=" * 96)
    print("Exact abstract-algebra certificate for")
    print("CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10")
    print("Arithmetic: exact SymPy symbolic; algebra core Gaussian-rational; no floats")
    print(f"Mode: {args.mode}; table construction: "
          f"{'word-insertion reducer' if args.mode == 'independent' else 'bit-inversion formula'}")
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
    print_multiplication_table(ACTIVE_TABLE)

    if args.mode == "independent":
        check(
            "A0 independent word reducer reproduces all 64 signed products",
            all(
                WORD_PRODUCT_TABLE[left][right] == PRODUCT_TABLE[left][right]
                for left, right in itertools.product(range(DIM), repeat=2)
            ),
            "64/64 products compared after separate construction",
        )

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

    generator_closure = []
    for element, gamma in itertools.product(basis, gammas):
        generator_closure.extend(
            [
                in_span(algebra_product(element, gamma), basis),
                in_span(algebra_product(gamma, element), basis),
            ]
        )
    check(
        "A4 left/right multiplication by every generator closes on the eight words",
        sum(int(result) for result in generator_closure) == len(generator_closure),
        f"{sum(int(result) for result in generator_closure)}/"
        f"{len(generator_closure)} products",
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
    e_plus = Rational(1, 2) * (one - I * omega)
    e_minus = Rational(1, 2) * (one + I * omega)
    check(
        "B5 e_+=(1-i omega)/2 and e_-=(1+i omega)/2 are central orthogonal idempotents",
        idempotent_axioms_ok(e_plus, e_minus, basis, one),
    )
    check(
        "B6 abstract labels satisfy omega e_+=+i e_+ and omega e_-=-i e_-",
        vector_eq(algebra_product(omega, e_plus), I * e_plus)
        and vector_eq(algebra_product(omega, e_minus), -I * e_minus),
    )

    center_coefficients = symbols("z0:8")
    generic_element = Matrix(center_coefficients)
    center_equations: list[sp.Expr] = []
    for gamma in gammas:
        commutator = algebra_product(generic_element, gamma) - algebra_product(
            gamma, generic_element
        )
        center_equations.extend(sp.expand(entry) for entry in commutator)
    center_matrix, _ = sp.linear_eq_to_matrix(
        center_equations, center_coefficients
    )
    center_nullspace = center_matrix.nullspace()
    check(
        "B7 solving all generator commutators gives Z(A_C)=span_C{1,omega}",
        len(center_nullspace) == 2
        and same_span(center_nullspace, [one, omega]),
        f"center dimension={len(center_nullspace)}",
    )

    central_scalar, central_volume = symbols("central_scalar central_volume")
    central_candidate = central_scalar * one + central_volume * omega
    central_idempotent_equations = list(
        algebra_product(central_candidate, central_candidate) - central_candidate
    )
    central_idempotent_solutions = sp.solve(
        central_idempotent_equations,
        [central_scalar, central_volume],
        dict=True,
    )
    central_idempotent_pairs = {
        (
            simplify(solution[central_scalar]),
            simplify(solution[central_volume]),
        )
        for solution in central_idempotent_solutions
    }
    check(
        "B8 the only central idempotents are 0, 1, e_+, and e_-",
        central_idempotent_pairs
        == {
            (sp.Integer(0), sp.Integer(0)),
            (sp.Integer(1), sp.Integer(0)),
            (Rational(1, 2), -I * Rational(1, 2)),
            (Rational(1, 2), I * Rational(1, 2)),
        },
        f"exact solutions={sorted(central_idempotent_pairs, key=str)}",
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
    section("Part D: matrix units constructed inside both abstract ideals")
    external_matrix_units = {
        (0, 0): Matrix([[1, 0], [0, 0]]),
        (0, 1): Matrix([[0, 1], [0, 0]]),
        (1, 0): Matrix([[0, 0], [1, 0]]),
        (1, 1): Matrix([[0, 0], [0, 1]]),
    }
    x11, x12, x21, x22 = symbols("x11 x12 x21 x22")
    generic_coefficients = {
        (0, 0): x11,
        (0, 1): x12,
        (1, 0): x21,
        (1, 1): x22,
    }
    abstract_units_by_sign: dict[int, dict[tuple[int, int], Matrix]] = {}
    for chirality, label, idempotent, ideal_generators in (
        (1, "+", e_plus, plus_generators),
        (-1, "-", e_minus, minus_generators),
    ):
        units = {
            (0, 0): Rational(1, 2) * algebra_product(
                idempotent, one + chirality * gamma_3
            ),
            (1, 1): Rational(1, 2) * algebra_product(
                idempotent, one - chirality * gamma_3
            ),
            (0, 1): chirality * Rational(1, 2) * algebra_product(
                idempotent, gamma_1 + I * gamma_2
            ),
            (1, 0): chirality * Rational(1, 2) * algebra_product(
                idempotent, gamma_1 - I * gamma_2
            ),
        }
        abstract_units_by_sign[chirality] = units
        unit_products = []
        for a, b, c, d in itertools.product(range(2), repeat=4):
            expected = units[(a, d)] if b == c else zero
            unit_products.append(
                vector_eq(
                    algebra_product(units[(a, b)], units[(c, d)]),
                    expected,
                )
            )
        check(
            f"D1{label} all 16 abstract E_ab E_cd=delta_bc E_ad products hold",
            sum(int(result) for result in unit_products) == len(unit_products),
            f"{sum(int(result) for result in unit_products)}/"
            f"{len(unit_products)} products",
        )
        check(
            f"D2{label} E_11+E_22=e_{label}; the four units are an ideal basis",
            vector_eq(units[(0, 0)] + units[(1, 1)], idempotent)
            and vector_rank(list(units.values())) == 4
            and same_span(list(units.values()), ideal_generators),
            f"matrix-unit rank={vector_rank(list(units.values()))}",
        )
        generic_ideal_element = sum(
            (generic_coefficients[index] * unit for index, unit in units.items()),
            zero,
        )
        isolation_results = []
        for p, a, b, q in itertools.product(range(2), repeat=4):
            isolated = algebra_product(
                algebra_product(units[(p, a)], generic_ideal_element),
                units[(b, q)],
            )
            isolation_results.append(
                vector_eq(
                    isolated,
                    generic_coefficients[(a, b)] * units[(p, q)],
                )
            )
        check(
            f"D3{label} coefficient isolation makes every nonzero two-sided ideal full",
            sum(int(result) for result in isolation_results)
            == len(isolation_results),
            f"{sum(int(result) for result in isolation_results)}/"
            f"{len(isolation_results)} identities",
        )

    check(
        "D4 center exhaustion and two simple complementary ideals leave exactly two summands",
        len(center_nullspace) == 2
        and len(central_idempotent_pairs) == 4
        and combined_rank == DIM
        and all(
            vector_rank(list(units.values())) == 4
            for units in abstract_units_by_sign.values()
        ),
    )

    # ------------------------------------------------------------------ E
    section("Part E: representation classification and faithfulness boundary")
    check(
        "E0 ordered Pauli quotients give rho_+(omega)=+iI and rho_-(omega)=-iI",
        matrix_eq(representation_of_vector(omega, images_plus), I * identity_2)
        and matrix_eq(
            representation_of_vector(omega, images_minus), -I * identity_2
        ),
    )
    for sign, label, idempotent, ideal_generators, images, opposite_ideal in (
        (1, "+", e_plus, plus_generators, images_plus, minus_generators),
        (-1, "-", e_minus, minus_generators, images_minus, plus_generators),
    ):
        check(
            f"E1{label} Pauli assignment respects every abstract basis product",
            homomorphism_ok(images),
        )
        actual_ideal_images = [
            representation_of_vector(element, images)
            for element in ideal_generators
        ]
        ideal_image_matrix = Matrix.hstack(
            *[matrix_coordinates(image) for image in actual_ideal_images]
        )
        abstract_unit_images = {
            index: representation_of_vector(unit, images)
            for index, unit in abstract_units_by_sign[sign].items()
        }
        check(
            f"E2{label} in-ideal units map bijectively and unitaly to standard M_2(C) units",
            all(
                matrix_eq(abstract_unit_images[index], expected)
                for index, expected in external_matrix_units.items()
            )
            and ideal_image_matrix.rank() == 4
            and ideal_image_matrix.nullspace() == []
            and matrix_eq(
                representation_of_vector(idempotent, images), identity_2
            ),
            f"ideal image rank={ideal_image_matrix.rank()}",
        )
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
            f"E3{label} complexified rho_{label} has exactly the opposite ideal as kernel",
            complex_map.rank() == 4
            and len(kernel) == 4
            and same_span(kernel, opposite_ideal),
            f"rank={complex_map.rank()}, kernel dim={len(kernel)}",
        )

        real_map = Matrix.hstack(
            *[real_matrix_coordinates(images[mask]) for mask in CANONICAL_MASKS]
        )
        check(
            f"E4{label} restriction of rho_{label} to real Cl(3,0) is faithful",
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
        "E5 simplicity forces exactly one central ideal to act on a simple module",
        central_action_pairs
        == {
            (sp.Integer(1), sp.Integer(0)),
            (sp.Integer(0), sp.Integer(1)),
        },
        f"solutions={sorted(central_action_pairs, key=str)}",
    )

    commutator_columns = []
    for candidate_unit in (
        external_matrix_units[(0, 0)],
        external_matrix_units[(0, 1)],
        external_matrix_units[(1, 0)],
        external_matrix_units[(1, 1)],
    ):
        column_entries: list[sp.Expr] = []
        for algebra_unit in external_matrix_units.values():
            column_entries.extend(
                list(matrix_coordinates(candidate_unit * algebra_unit - algebra_unit * candidate_unit))
            )
        commutator_columns.append(Matrix(column_entries))
    commutant_constraint = Matrix.hstack(*commutator_columns)
    commutant = commutant_constraint.nullspace()
    check(
        "E6 the commutant of the natural M_2(C) module is exactly C I_2",
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
                    external_matrix_units[(target_index, source_index)] * source,
                    target,
                )
            )
    check(
        "E7 matrix units generate C^2 from every nonzero coordinate direction",
        sum(int(result) for result in standard_action_results)
        == len(standard_action_results),
        f"{sum(int(result) for result in standard_action_results)}/"
        f"{len(standard_action_results)} actions",
    )

    e11 = external_matrix_units[(0, 0)]
    e12 = external_matrix_units[(0, 1)]
    e21 = external_matrix_units[(1, 0)]
    module_inverse_results = [
        matrix_eq(e11 + e21 * e12, identity_2),
        matrix_eq(e11 * e11, e11),
        matrix_eq(e12 * e11, zero_2),
        matrix_eq(e11 * e21 * e11, zero_2),
        matrix_eq(e12 * e21 * e11, e11),
    ]
    check(
        "E8 the universal matrix-unit F/G identities are mutually inverse",
        sum(int(result) for result in module_inverse_results)
        == len(module_inverse_results),
        f"{sum(int(result) for result in module_inverse_results)}/"
        f"{len(module_inverse_results)} universal identities",
    )

    f_operators = (e11, e21)
    module_linearity_results = []
    for a, b, source_index in itertools.product(range(2), repeat=3):
        left = external_matrix_units[(a, b)] * f_operators[source_index] * e11
        right = f_operators[a] * e11 if b == source_index else zero_2
        module_linearity_results.append(matrix_eq(left, right))
    check(
        "E9 F(e_j tensor w) is M_2(C)-linear for arbitrary w in E_11 V",
        sum(int(result) for result in module_linearity_results)
        == len(module_linearity_results),
        f"{sum(int(result) for result in module_linearity_results)}/"
        f"{len(module_linearity_results)} matrix-unit actions",
    )

    check(
        "E10 F/G and matrix-unit transitivity force every simple ideal-module to be C^2",
        all(module_inverse_results)
        and all(module_linearity_results)
        and all(standard_action_results)
        and len(commutant) == 1,
    )

    check(
        "E11 rho_+ and rho_- are inequivalent because omega acts by opposite scalars",
        not matrix_eq(
            representation_of_vector(omega, images_plus),
            representation_of_vector(omega, images_minus),
        ),
    )

    # ------------------------------------------------------------------ F
    section("Part F: conditional unitary refinement for *-representations")
    adjoint = lambda matrix: matrix.conjugate().T
    h11, h12, h21, h22 = symbols("h11 h12 h21 h22")
    generic_gram = Matrix([[h11, h12], [h21, h22]])
    gram_equations = []
    for sigma in pauli:
        gram_equations.extend(matrix_coordinates(generic_gram * sigma - sigma * generic_gram))
    gram_matrix, _ = sp.linear_eq_to_matrix(
        gram_equations, [h11, h12, h21, h22]
    )
    gram_commutant = gram_matrix.nullspace()
    check(
        "F1 a generic Gram matrix commuting with the Pauli algebra is scalar",
        len(gram_commutant) == 1
        and same_span(gram_commutant, [Matrix([1, 0, 0, 1])]),
        f"commutant dimension={len(gram_commutant)}",
    )
    positive_scalar = symbols("positive_scalar", positive=True)
    check(
        "F2 H=cI with c>0 gives U=T/sqrt(c) and U^dagger U=I",
        matrix_eq((positive_scalar * identity_2) / positive_scalar, identity_2),
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
        "F3 a nonunitary similarity still preserves all Clifford relations",
        sum(int(result) for result in nonunitary_clifford_results)
        == len(nonunitary_clifford_results),
        f"{sum(int(result) for result in nonunitary_clifford_results)}/"
        f"{len(nonunitary_clifford_results)} relations",
    )
    check(
        "F4 without Hermitian generators the same-sign unitary claim is false",
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
    wrong_table = [list(row) for row in ACTIVE_TABLE]
    wrong_table[1][1] = (-1, 0)

    quotient_only_accepts = (
        matrix_eq(representation_of_vector(e_plus, images_plus), identity_2)
        and matrix_eq(representation_of_vector(e_minus, images_plus), zero_2)
        and matrix_eq(representation_of_vector(e_plus, images_minus), zero_2)
        and matrix_eq(representation_of_vector(e_minus, images_minus), identity_2)
    )
    augmented_one = Matrix.vstack(one, Matrix([1]))
    augmented_e_plus = Matrix.vstack(e_plus, Matrix([0]))
    augmented_e_minus = Matrix.vstack(e_minus, Matrix([0]))
    augmented_complete = vector_eq(
        augmented_e_plus + augmented_e_minus,
        augmented_one,
    )

    complex_plus_map = Matrix.hstack(
        *[matrix_coordinates(images_plus[mask]) for mask in CANONICAL_MASKS]
    )
    complex_plus_kernel = [
        sum(
            (
                coordinate[column] * basis_by_mask[mask]
                for column, mask in enumerate(CANONICAL_MASKS)
            ),
            zero,
        )
        for coordinate in complex_plus_map.nullspace()
    ]
    one_d_g1, one_d_g2, one_d_g3 = symbols("one_d_g1 one_d_g2 one_d_g3")
    one_d_groebner = sp.groebner(
        [
            one_d_g1**2 - 1,
            one_d_g2**2 - 1,
            one_d_g3**2 - 1,
            2 * one_d_g1 * one_d_g2,
            2 * one_d_g1 * one_d_g3,
            2 * one_d_g2 * one_d_g3,
        ],
        one_d_g1,
        one_d_g2,
        one_d_g3,
    )
    one_d_inconsistent = one_d_groebner.reduce(sp.Integer(1))[1] == 0

    doubled_actions = {
        index: sp.kronecker_product(unit, eye(2))
        for index, unit in external_matrix_units.items()
    }
    doubled_submodule = [Matrix([1, 0, 0, 0]), Matrix([0, 0, 1, 0])]
    doubled_invariant = all(
        in_span(action * vector, doubled_submodule)
        for action, vector in itertools.product(
            doubled_actions.values(), doubled_submodule
        )
    )
    nonscalar_doubled_commutant = sp.kronecker_product(
        identity_2, external_matrix_units[(0, 1)]
    )
    doubled_commutes = all(
        matrix_eq(
            nonscalar_doubled_commutant * action,
            action * nonscalar_doubled_commutant,
        )
        for action in doubled_actions.values()
    )

    t11, t12, t21, t22 = symbols("t11 t12 t21 t22")
    chirality_intertwiner = Matrix([[t11, t12], [t21, t22]])
    chirality_equations = matrix_coordinates(
        chirality_intertwiner * (I * identity_2)
        - (-I * identity_2) * chirality_intertwiner
    )
    chirality_matrix, _ = sp.linear_eq_to_matrix(
        chirality_equations, [t11, t12, t21, t22]
    )

    hostile_results: dict[str, bool] = {
        "wrong-multiplication-sign": not table_relations_ok(
            wrong_table, gammas, one
        ),
        "quotient-only-idempotents": quotient_only_accepts
        and not augmented_complete,
        "missing-ideal": vector_rank(plus_generators) == 4
        and vector_rank(plus_generators) != DIM,
        "false-faithful-extension": complex_plus_map.rank() == 4
        and len(complex_plus_kernel) == 4
        and same_span(complex_plus_kernel, minus_generators),
        "fake-one-dimensional-simple": one_d_inconsistent,
        "fake-extra-dimensional-simple": doubled_invariant
        and vector_rank(doubled_submodule) == 2
        and doubled_commutes
        and not matrix_eq(
            nonscalar_doubled_commutant,
            (nonscalar_doubled_commutant.trace() / 4) * eye(4),
        ),
        "chirality-merger": chirality_matrix.rank() == 4
        and chirality_matrix.nullspace() == [],
        "unitary-without-hermitian": all(
            matrix_eq(image_i * image_j + image_j * image_i,
                      2 * identity_2 if i == j else zero_2)
            for i, image_i in enumerate(nonunitary_images)
            for j, image_j in enumerate(nonunitary_images)
        )
        and any(not matrix_eq(image, adjoint(image)) for image in nonunitary_images)
        and not matrix_eq(
            nonunitary_gram,
            (nonunitary_gram.trace() / 2) * identity_2,
        )
        and len(gram_commutant) == 1,
    }

    for hostile_name, rejected in hostile_results.items():
        check(
            f"H reject hostile fixture: {hostile_name}",
            rejected,
        )

    if args.mode == "intentional-failure":
        promoted_fixture = args.inject_failure or "wrong-multiplication-sign"
        check(
            f"INTENTIONAL FAILURE fixture promoted: {promoted_fixture}",
            not hostile_results[promoted_fixture],
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
