#!/usr/bin/env python3
"""Compact exact certificate for the Cl(3) Pauli-irrep theorem."""

from __future__ import annotations

from cl3_pauli_irrep_exact_support_2026_05_10 import *

AUDIT_INPUT_PATHS = (
    "scripts/cl3_pauli_irrep_exact_support_2026_05_10.py",
    "scripts/cl3_pauli_irrep_faithful_direct_sum_n7_independent_2026_07_17.py",
)

def main() -> int:
    args = parse_args()
    set_verbose(args.verbose)
    active_table = (
        WORD_PRODUCT_TABLE if args.mode == "independent" else PRODUCT_TABLE
    )
    set_active_table(active_table)
    construction = "word-insertion" if args.mode == "independent" else "bit-inversion"
    print("CL3_PAULI_IRREP_EXACT_CERTIFICATE arithmetic=Gaussian-rational")
    print(f"mode={args.mode} table={construction}")
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
    section("Part A: eight-dimensional algebra from the defining relations")
    print_multiplication_table(active_table)
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
    for element_mask, gamma_mask in itertools.product(
        CANONICAL_MASKS, (1, 2, 4)
    ):
        for left_mask, right_mask in (
            (element_mask, gamma_mask),
            (gamma_mask, element_mask),
        ):
            expected_sign, expected_mask = WORD_PRODUCT_TABLE[left_mask][right_mask]
            generator_closure.append(
                vector_eq(
                    algebra_product(
                        basis_by_mask[left_mask],
                        basis_by_mask[right_mask],
                    ),
                    expected_sign * basis_by_mask[expected_mask],
                )
            )
    check(
        "A4 left/right generator products match the independent canonical-word reducer",
        sum(int(result) for result in generator_closure) == len(generator_closure),
        f"{sum(int(result) for result in generator_closure)}/"
        f"{len(generator_closure)} products",
    )
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
    normalization_witness = Matrix([[0, 2 * I], [2, 0]])
    normalization_gram = adjoint(normalization_witness) * normalization_witness
    normalization_scalar = simplify(normalization_gram.trace() / 2)
    normalized_witness = normalization_witness / sp.sqrt(normalization_scalar)
    witness_images = [
        normalization_witness * sigma * normalization_witness.inv()
        for sigma in pauli
    ]
    normalized_witness_images = [
        normalized_witness * sigma * normalized_witness.inv()
        for sigma in pauli
    ]
    check(
        "F2 computed scalar Gram normalizes a nontrivial exact intertwiner by sqrt(c), not c",
        normalization_scalar.is_positive is True
        and matrix_eq(
            normalization_gram,
            normalization_scalar * identity_2,
        )
        and matrix_eq(
            adjoint(normalized_witness) * normalized_witness,
            identity_2,
        )
        and all(
            matrix_eq(left, right)
            for left, right in zip(witness_images, normalized_witness_images)
        )
        and not matrix_eq(
            adjoint(normalization_witness / normalization_scalar)
            * (normalization_witness / normalization_scalar),
            identity_2,
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
    wrong_table = [list(row) for row in active_table]
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
    complex_minus_map = Matrix.hstack(
        *[matrix_coordinates(images_minus[mask]) for mask in CANONICAL_MASKS]
    )
    complex_minus_kernel = [
        sum(
            (
                coordinate[column] * basis_by_mask[mask]
                for column, mask in enumerate(CANONICAL_MASKS)
            ),
            zero,
        )
        for coordinate in complex_minus_map.nullspace()
    ]
    real_plus_map = Matrix.hstack(
        *[real_matrix_coordinates(images_plus[mask]) for mask in CANONICAL_MASKS]
    )
    real_minus_map = Matrix.hstack(
        *[real_matrix_coordinates(images_minus[mask]) for mask in CANONICAL_MASKS]
    )
    combined_complex_map = Matrix.vstack(complex_plus_map, complex_minus_map)
    combined_actions = [
        sp.diag(images_plus[mask], images_minus[mask])
        for mask in CANONICAL_MASKS
    ]
    first_chirality_subspace = [
        Matrix([1, 0, 0, 0]),
        Matrix([0, 1, 0, 0]),
    ]
    second_chirality_subspace = [
        Matrix([0, 0, 1, 0]),
        Matrix([0, 0, 0, 1]),
    ]
    combined_module_reducible = all(
        in_span(action * vector, subspace)
        for action in combined_actions
        for subspace in (first_chirality_subspace, second_chirality_subspace)
        for vector in subspace
    ) and all(
        0 < vector_rank(subspace) < 4
        for subspace in (first_chirality_subspace, second_chirality_subspace)
    )
    plus_kernel_dimension = len(complex_plus_kernel)
    minus_kernel_dimension = len(complex_minus_kernel)
    plus_real_rank = real_plus_map.rank()
    minus_real_rank = real_minus_map.rank()
    plus_ideal_dimension = vector_rank(plus_generators)
    minus_ideal_dimension = vector_rank(minus_generators)
    combined_map_rank = combined_complex_map.rank()
    pauli_hermitian = all(matrix_eq(sigma, adjoint(sigma)) for sigma in pauli)
    nonunitary_boundary_witness = (
        all(nonunitary_clifford_results)
        and any(
            not matrix_eq(image, adjoint(image))
            for image in nonunitary_images
        )
        and not matrix_eq(
            nonunitary_gram,
            (nonunitary_gram.trace() / 2) * identity_2,
        )
    )
    hermitian_refinement_closes = (
        pauli_hermitian
        and len(gram_commutant) == 1
        and same_span(gram_commutant, [Matrix([1, 0, 0, 1])])
        and matrix_eq(
            adjoint(normalized_witness) * normalized_witness,
            identity_2,
        )
    )
    boundaries_scoped = (
        plus_kernel_dimension == minus_kernel_dimension == 4
        and pauli_hermitian
        and nonunitary_boundary_witness
        and combined_map_rank == DIM
        and combined_module_reducible
        and hermitian_refinement_closes
    )
    routes = (
        NoGoRoute(
            route_id="complex-kernel-solve",
            route_class="algebraic_rearrangement",
            mechanism="algebraic full-basis kernel solve for both complex actions",
            attempt="solve both action maps and opposite-ideal kernels",
            outcome="both exact maps have rank four and opposite-ideal kernel dimension four",
            honesty_marker="ATTEMPTED",
            closed=(
                complex_plus_map.rank() == complex_minus_map.rank() == 4
                and plus_kernel_dimension == minus_kernel_dimension == 4
                and same_span(complex_plus_kernel, minus_generators)
                and same_span(complex_minus_kernel, plus_generators)
            ),
        ),
        NoGoRoute(
            route_id="central-character-separation",
            route_class="symmetry_or_representation",
            mechanism="representation central-character and commutant separation",
            attempt="solve central actions and cross-character intertwiners",
            outcome="a simple module selects one central character and the opposite-character intertwiner space is zero",
            honesty_marker="ATTEMPTED",
            closed=(
                central_action_pairs
                == {
                    (sp.Integer(1), sp.Integer(0)),
                    (sp.Integer(0), sp.Integer(1)),
                }
                and chirality_matrix.rank() == 4
                and chirality_matrix.nullspace() == []
            ),
        ),
        NoGoRoute(
            route_id="finite-simple-counterexamples",
            route_class="numerical_or_finite_case",
            mechanism="finite exact compute of scalar and doubled module candidates",
            attempt="test scalar and doubled-module candidates exactly",
            outcome="the scalar system is inconsistent and the four-dimensional doubled module is reducible",
            honesty_marker="ATTEMPTED",
            closed=(
                one_d_inconsistent
                and doubled_invariant
                and doubled_commutes
                and vector_rank(doubled_submodule) == 2
            ),
        ),
        NoGoRoute(
            route_id="faithful-direct-sum-carrier",
            route_class="alternate_carrier_or_sector",
            mechanism="alternate module carrier rho_plus direct-sum rho_minus",
            attempt="stack both maps and test rank plus reducibility",
            outcome="the stacked carrier is faithful only because it contains both invariant chirality summands and is reducible",
            honesty_marker="ATTEMPTED",
            closed=combined_map_rank == DIM and combined_module_reducible,
        ),
        NoGoRoute(
            route_id="gram-normalization",
            route_class="normalization_or_units",
            mechanism="normalization of the intertwiner Gram matrix under Hermitian generators",
            attempt="solve the Gram commutant and diagonal similarity",
            outcome="Hermitian images force scalar normalization while the bare non-Hermitian similarity keeps a nonscalar Gram matrix",
            honesty_marker="ATTEMPTED",
            closed=hermitian_refinement_closes and nonunitary_boundary_witness,
        ),
    )
    prior_witness_count = sum(
        route.honesty_marker == "RULED OUT BY PRIOR" for route in routes
    )
    resolution_kwargs = {
        "plus_kernel_dimension": plus_kernel_dimension,
        "minus_kernel_dimension": minus_kernel_dimension,
        "plus_real_rank": plus_real_rank,
        "minus_real_rank": minus_real_rank,
        "central_action_count": len(central_action_pairs),
        "plus_ideal_dimension": plus_ideal_dimension,
        "minus_ideal_dimension": minus_ideal_dimension,
        "combined_map_rank": combined_map_rank,
    }
    resolutions = make_resolution_records(**resolution_kwargs)
    missing_resolution = tuple(
        record
        for record in resolutions
        if record.resolution_class != "per_mode"
    )
    stale_resolution = (
        replace(
            resolutions[0],
            certificate=(
                ("plus_kernel_dimension", 0),
                ("minus_kernel_dimension", 0),
            ),
        ),
        *resolutions[1:],
    )
    reordered_resolution = (
        resolutions[0],
        resolutions[2],
        resolutions[1],
        *resolutions[3:],
    )
    false_resolution = (
        *resolutions[:-1],
        replace(
            resolutions[-1],
            disposition="PROVED",
            description=(
                "lattice_wide: a false fixture promotes the untested, excluded "
                "resolution to a proved lattice-wide negative statement."
            ),
        ),
    )
    resolution_mutation_rejections = {
        "missing-resolution-evidence": not resolution_records_valid(missing_resolution),
        "stale-resolution-evidence": not resolution_records_valid(stale_resolution),
        "reordered-resolution-evidence": not resolution_records_valid(
            reordered_resolution
        ),
        "false-resolution-evidence": not resolution_records_valid(false_resolution),
    }
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
        **resolution_mutation_rejections,
    }
    local_echo_controls_closed = sum(
        hostile_results[name]
        for name in ("quotient-only-idempotents", "unitary-without-hermitian")
    )
    emit_development_no_go_evidence(
        routes=routes,
        resolutions=resolutions,
        boundaries_scoped=boundaries_scoped,
        prior_witness_count=prior_witness_count,
        combined_map_rank=combined_map_rank,
        combined_module_reducible=combined_module_reducible,
        hermitian_refinement_closes=hermitian_refinement_closes,
        standard_complex_kernel_dimension=plus_kernel_dimension,
        local_echo_controls_closed=local_echo_controls_closed,
    )
    section("Part H: hostile controls")
    resolution_fixture_names = set(resolution_mutation_rejections)
    for hostile_name, rejected in hostile_results.items():
        if (
            hostile_name in resolution_fixture_names
            and args.mode not in {"hostile", "intentional-failure"}
        ):
            continue
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
    section("Summary")
    print("CERTIFIED split=M2(C)+M2(C) irreps=2 dimensions=2,2")
    print("CERTIFIED real_ranks=8,8 complex_kernel_dimensions=4,4")
    pass_count, fail_count = counts()
    print("=" * 72)
    print(f"TOTAL: PASS={pass_count}, FAIL={fail_count}")
    print("=" * 72)
    return 0 if fail_count == 0 else 1
if __name__ == "__main__":
    raise SystemExit(main())
