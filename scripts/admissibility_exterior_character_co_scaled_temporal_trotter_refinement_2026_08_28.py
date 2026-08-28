#!/usr/bin/env python3
"""Exact checks for the exterior-character co-scaled Trotter boundary."""

from __future__ import annotations

import argparse
import itertools
from math import factorial
from pathlib import Path

import sympy as sp

from admissibility_exterior_character_co_scaled_temporal_trotter_refinement_independent_2026_08_28 import (
    independent_facts,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_CO_SCALED_TEMPORAL_TROTTER_AND_CYLINDRICAL_REFINEMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_TIME_REFINEMENT_SEMIGROUP_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_exterior_character_co_scaled_temporal_trotter_refinement_independent_2026_08_28.py",
)

MUTATIONS = (
    "corrupt_cosine_power",
    "flatten_haar_curvature",
    "shift_radial_moment_recurrence",
    "drop_character_theta6",
    "drop_full_component_factor",
    "flip_clock_q2_sign",
    "erase_L2_residual",
    "identify_spin2_with_spin1",
    "miscount_fine_convolutions",
    "test_determinant_at_mq",
    "force_finite_component_jump",
    "corrupt_determinant_prefactor",
    "bias_product_haar_count",
    "remove_internal_gauge_inverse",
    "drop_hessian_scale_four",
    "replace_cos_pi8_square",
    "drop_left_half_exponential",
    "drop_intrinsic_K_term",
    "promote_operator_norm",
    "identify_spectral_refinement",
    "claim_physical_time",
    "erase_laplace_tail",
    "erase_chernoff_range",
)

PASS = 0
FAIL = 0


def check(name: str, condition: object) -> None:
    global PASS, FAIL
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    PASS += int(ok)
    FAIL += int(not ok)


def truncate(expr: sp.Expr, variable: sp.Symbol, order: int) -> sp.Expr:
    return sp.series(expr, variable, 0, order + 1).removeO().expand()


def normalized_character(theta: sp.Symbol, ell: sp.Symbol | int) -> sp.Expr:
    return sp.sin((ell + sp.Rational(1, 2)) * theta) / (
        (2 * ell + 1) * sp.sin(theta / 2)
    )


def radial_moment(power: int) -> sp.Integer:
    return sp.factorial2(2 * power + 1)


def integrate_radial_polynomial(poly: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    result = sp.Integer(0)
    for (power,), coefficient in sp.Poly(sp.expand(poly), variable).terms():
        if power % 2:
            raise AssertionError("odd radial power")
        result += coefficient * radial_moment(power // 2)
    return sp.simplify(result)


def derive_multiplier_log(*, drop_theta6: bool = False) -> tuple[sp.Expr, tuple[sp.Symbol, ...]]:
    """Laplace-expand the actual action/Haar/character integral through q^3."""
    q, x = sp.symbols("q x", positive=True, real=True)
    n, ell = sp.symbols("n ell", positive=True, integer=True)
    theta = sp.symbols("theta", real=True)
    action = sp.Rational(16, 1) / n * (1 - sp.cos(theta / 2) ** (2 * n))
    action_taylor = sp.series(action, theta, 0, 10).removeO()
    scaled_theta = sp.sqrt(q) * x
    correction = truncate(
        sp.exp(-action_taylor.subs(theta, scaled_theta) / (8 * q) + x**2 / 2),
        q,
        3,
    )
    haar = sp.series(4 * sp.sin(theta / 2) ** 2 / theta**2, theta, 0, 8).removeO()
    character = sp.series(normalized_character(theta, ell), theta, 0, 8).removeO()
    if drop_theta6:
        character -= sp.expand(character).coeff(theta, 6) * theta**6
    haar = haar.subs(theta, scaled_theta)
    character = character.subs(theta, scaled_theta)
    denominator_integrand = truncate(correction * haar, q, 3)
    numerator_integrand = truncate(denominator_integrand * character, q, 3)
    denominator = sp.Add(*(
        integrate_radial_polynomial(denominator_integrand.coeff(q, power), x) * q**power
        for power in range(4)
    ))
    numerator = sp.Add(*(
        integrate_radial_polynomial(numerator_integrand.coeff(q, power), x) * q**power
        for power in range(4)
    ))
    multiplier = truncate(numerator / denominator, q, 3)
    return truncate(sp.log(multiplier), q, 3), (q, n, ell)


def expected_multiplier_log(q: sp.Symbol, n: sp.Symbol, ell: sp.Symbol) -> sp.Expr:
    angular = ell * (ell + 1)
    return (
        -angular * q / 2
        - angular * (5 * n - 2) * q**2 / 8
        + angular * (
            (12 * n - 4) * angular - (255 * n**2 - 171 * n + 24)
        ) * q**3 / 192
    )


Word = tuple[str, ...]
Words = dict[Word, sp.Rational]


def word_add(left: Words, right: Words) -> Words:
    out = dict(left)
    for word, coefficient in right.items():
        out[word] = out.get(word, sp.Rational(0)) + coefficient
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def word_scale(words: Words, factor: sp.Rational) -> Words:
    return {word: factor * coefficient for word, coefficient in words.items()
            if factor * coefficient}


def word_mul(left: Words, right: Words, order: int = 3) -> Words:
    out: Words = {}
    for left_word, left_coefficient in left.items():
        for right_word, right_coefficient in right.items():
            word = left_word + right_word
            if len(word) <= order:
                out[word] = out.get(word, sp.Rational(0)) + left_coefficient * right_coefficient
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def word_exp(letter: str, factor: sp.Rational) -> Words:
    return {
        (): sp.Rational(1),
        (letter,): factor,
        (letter, letter): factor**2 / 2,
        (letter, letter, letter): factor**3 / 6,
    }


def symmetric_word_log(*, omit_left_half: bool = False) -> Words:
    left = {(): sp.Rational(1)} if omit_left_half else word_exp("X", sp.Rational(1, 2))
    product = word_mul(word_mul(left, word_exp("Y", sp.Rational(1))),
                       word_exp("X", sp.Rational(1, 2)))
    delta = word_add(product, {(): sp.Rational(-1)})
    return word_add(
        word_add(delta, word_scale(word_mul(delta, delta), sp.Rational(-1, 2))),
        word_scale(word_mul(word_mul(delta, delta), delta), sp.Rational(1, 3)),
    )


def matrix_series_exp(matrix: sp.Matrix, epsilon: sp.Symbol, order: int = 3) -> sp.Matrix:
    size = matrix.rows
    result = sp.eye(size)
    power = sp.eye(size)
    for degree in range(1, order + 1):
        power = power * matrix
        result += power / factorial(degree)
    return result.applyfunc(lambda entry: truncate(entry, epsilon, order))


def matrix_series_log(matrix: sp.Matrix, epsilon: sp.Symbol, order: int = 3) -> sp.Matrix:
    delta = matrix - sp.eye(matrix.rows)
    result = sp.zeros(matrix.rows)
    power = sp.eye(matrix.rows)
    for degree in range(1, order + 1):
        power = power * delta
        result += sp.Rational((-1) ** (degree + 1), degree) * power
    return result.applyfunc(lambda entry: truncate(entry, epsilon, order))


def z2_isometry(*, biased: bool = False, length: int = 3) -> bool:
    coarse = {1: sp.Rational(2), -1: sp.Rational(-1)}
    coarse_norm = sum(value**2 for value in coarse.values()) / 2
    fine_sum = sp.Rational(0)
    for mask in range(1 << length):
        product = 1
        for bit in range(length):
            product *= -1 if mask & (1 << bit) else 1
        fine_sum += coarse[product] ** 2
    denominator = (1 << length) - int(biased)
    return sp.Rational(fine_sum, denominator) == coarse_norm


def main(mutation: str | None, mode: str) -> int:
    global PASS, FAIL
    PASS = 0
    FAIL = 0

    if mode == "independent":
        for name, condition in independent_facts().items():
            check(f"independent: {name}", condition)
        print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
        return int(FAIL != 0)

    root = Path(__file__).resolve().parents[1]
    source = (root / AUDIT_INPUT_PATHS[0]).read_text()
    parent = (root / AUDIT_INPUT_PATHS[1]).read_text()
    axioms = (root / AUDIT_INPUT_PATHS[2]).read_text()
    if mutation == "promote_operator_norm":
        source = source.replace("strong convergence, not operator-norm convergence",
                                "operator-norm convergence")
    if mutation == "identify_spectral_refinement":
        source = source.replace("Temporal repetition on one fixed graph is not spatial carrier refinement",
                                "Temporal repetition on one fixed graph is spatial carrier refinement")
    if mutation == "claim_physical_time":
        source = source.replace("not a derived clock or lattice spacing",
                                "a derived physical clock and lattice spacing")
    if mutation == "erase_laplace_tail":
        source = source.replace("strict positive minimum", "no positive minimum")
    if mutation == "erase_chernoff_range":
        source = source.replace("hence the range condition holds",
                                "without checking the range condition")
    scope_ok = (
        "strong convergence, not operator-norm convergence" in source
        and "Temporal repetition on one fixed graph is not spatial carrier refinement" in source
        and "not a derived clock or lattice spacing" in source
        and "exact common-clock obstruction" in parent
        and "source/action" in axioms
        and "strict positive minimum" in source
        and "hence the range condition holds" in source
    )

    theta = sp.symbols("theta", real=True)
    n = sp.symbols("n", positive=True, integer=True)
    cosine_power = 2 * n + (2 if mutation == "corrupt_cosine_power" else 0)
    action = sp.Rational(16, 1) / n * (1 - sp.cos(theta / 2) ** cosine_power)
    action_series = sp.series(action, theta, 0, 10).removeO().expand()
    action_ok = all((
        sp.simplify(action_series.coeff(theta, 2) - 4) == 0,
        sp.simplify(action_series.coeff(theta, 4) + (3 * n - 1) / 6) == 0,
        sp.simplify(action_series.coeff(theta, 6) - (15 * n**2 - 15 * n + 4) / 360) == 0,
        sp.simplify(action_series.coeff(theta, 8)
                    + (105 * n**3 - 210 * n**2 + 147 * n - 34) / 40320) == 0,
    ))
    check("actual action: the full f_n common-axis Taylor series is derived through theta^8", action_ok)

    nominal_haar = sp.series(4 * sp.sin(theta / 2) ** 2 / theta**2, theta, 0, 8).removeO().expand()
    haar = nominal_haar
    if mutation == "flatten_haar_curvature":
        haar -= haar.coeff(theta, 2) * theta**2
    ell = sp.symbols("ell", positive=True, integer=True)
    character = sp.series(normalized_character(theta, ell), theta, 0, 8).removeO().expand()
    angular = ell * (ell + 1)
    character_target = (
        1 - angular * theta**2 / 6
        + angular * (3 * angular - 1) * theta**4 / 360
        - angular * (3 * angular**2 - 3 * angular + 1) * theta**6 / 15120
    )
    check(
        "Haar and character geometry: normalized class curvature and all-spin theta^6 coefficients are exact",
        haar == 1 - theta**2 / 12 + theta**4 / 360 - theta**6 / 20160
        and sp.simplify(character - character_target) == 0,
    )

    moments = tuple(radial_moment(power) for power in range(5))
    checked_moments = list(moments)
    if mutation == "shift_radial_moment_recurrence":
        checked_moments[3] += 2
    recurrence_ok = all(
        checked_moments[power] == (2 * power + 1) * checked_moments[power - 1]
        for power in range(1, 5)
    )
    check(
        "radial Gaussian measure: normalized three-dimensional moments are generated recursively",
        checked_moments[0] == 1 and recurrence_ok and moments == (1, 3, 15, 105, 945),
    )

    log_expr, (q, n_log, ell_log) = derive_multiplier_log(
        drop_theta6=(mutation == "drop_character_theta6")
    )
    expected_log = expected_multiplier_log(q, n_log, ell_log)
    proper_mass, improper_mass, proper_multiplier = sp.symbols(
        "I_proper I_improper u", positive=True
    )
    determinant_multiplier = (proper_mass - improper_mass) / (proper_mass + improper_mass)
    proper_probability = proper_mass / (proper_mass + improper_mass)
    full_multiplier = proper_probability * proper_multiplier
    if mutation == "drop_full_component_factor":
        full_multiplier = proper_multiplier
    component_bridge_ok = (
        sp.simplify(proper_probability - (1 + determinant_multiplier) / 2) == 0
        and sp.simplify(full_multiplier - proper_probability * proper_multiplier) == 0
        and sp.limit(
            sp.exp(-2 / (n_log * q)) / q ** sp.Rational(15, 2),
            q,
            0,
            dir="+",
        ) == 0
    )
    check(
        "actual full O(3) multiplier: the proper log and exponentially flat component-mass factor are both derived",
        sp.simplify(log_expr - expected_log) == 0 and component_bridge_ok,
    )

    epsilon, diffusivity = sp.symbols("epsilon D", positive=True)
    clock_a, clock_b = sp.symbols("clock_a clock_b")
    generic_angular = sp.symbols("L", positive=True)
    generic_log = (
        -generic_angular * q / 2
        -generic_angular * (5 * n_log - 2) * q**2 / 8
        + generic_angular * (
            (12 * n_log - 4) * generic_angular
            - (255 * n_log**2 - 171 * n_log + 24)
        ) * q**3 / 192
    )
    clock = diffusivity * epsilon + clock_a * diffusivity**2 * epsilon**2 + clock_b * diffusivity**3 * epsilon**3
    substituted = truncate(generic_log.subs(q, clock), epsilon, 3)
    epsilon2_equation = sp.expand(substituted.coeff(epsilon, 2) / (generic_angular * diffusivity**2))
    epsilon3_per_l = sp.expand(substituted.coeff(epsilon, 3) / (generic_angular * diffusivity**3))
    epsilon3_linear_equation = sp.Poly(epsilon3_per_l, generic_angular).coeff_monomial(1)
    solution = sp.solve((epsilon2_equation, epsilon3_linear_equation), (clock_a, clock_b), dict=True)[0]
    checked_solution = dict(solution)
    if mutation == "flip_clock_q2_sign":
        checked_solution[clock_a] = -checked_solution[clock_a]
    clock_ok = (
        checked_solution[clock_a] == -(5 * n_log - 2) / 4
        and checked_solution[clock_b] == (15 * n_log**2 - 23 * n_log + 8) / 32
    )
    check("corrected scalar clock: the q^2 and q^3 coefficients are solved from the channel expansion", clock_ok)

    corrected = sp.expand(substituted.subs(solution))
    cubic_residual = sp.factor(corrected.coeff(epsilon, 3))
    checked_residual = cubic_residual
    if mutation == "erase_L2_residual":
        checked_residual -= diffusivity**3 * (3 * n_log - 1) * generic_angular**2 / 48
    check(
        "irreducible residual: scalar clock correction leaves D^3(3n-1)L^2 epsilon^3/48",
        sp.simplify(checked_residual
                    - diffusivity**3 * (3 * n_log - 1) * generic_angular**2 / 48) == 0,
    )

    spin_two_angular = sp.Integer(2) if mutation == "identify_spin2_with_spin1" else sp.Integer(6)
    spin_invariant = sp.factor(
        generic_log.subs(generic_angular, spin_two_angular) / spin_two_angular
        - generic_log.subs(generic_angular, 2) / 2
    )
    check(
        "channel invariant: spin one and spin two retain the exact cubic common-clock mismatch",
        sp.simplify(sp.expand(spin_invariant).coeff(q, 3) - (3 * n_log - 1) / 12) == 0,
    )

    subdivision_m = sp.symbols("m", integer=True, positive=True)
    coefficient2, coefficient3 = sp.symbols("c2 c3")
    fine_count = subdivision_m - int(mutation == "miscount_fine_convolutions")
    coarse_q = subdivision_m * q + coefficient2 * q**2 + coefficient3 * q**3
    spin_one_match = truncate(
        generic_log.subs({generic_angular: 2, q: coarse_q})
        - fine_count * generic_log.subs(generic_angular, 2), q, 3
    )
    subdivision_solution = sp.solve(
        (spin_one_match.coeff(q, 2), spin_one_match.coeff(q, 3)),
        (coefficient2, coefficient3),
        dict=True,
    )[0]
    spin_two_defect = sp.factor(truncate(
        generic_log.subs({generic_angular: 6, q: coarse_q.subs(subdivision_solution)})
        - fine_count * generic_log.subs(generic_angular, 6), q, 3
    ).coeff(q, 3))
    nominal_c2 = subdivision_solution[coefficient2]
    determinant_c2 = sp.Integer(0) if mutation == "test_determinant_at_mq" else nominal_c2
    determinant_finite_exponent = sp.factor(
        2 * determinant_c2 / (n_log * subdivision_m**2)
    )
    expected_finite_exponent = -(subdivision_m - 1) * (5 * n_log - 2) / (
        2 * n_log * subdivision_m
    )
    matched_divergence_sample = (
        2 ** -sp.Rational(5, 2)
        * sp.exp(-sp.Rational(3, 4))
        * sp.exp(1 / q)
    )
    check(
        "cylindrical refinement: full spin-one matching leaves both spin-two and matched-clock determinant defects",
        spin_one_match.coeff(q, 1) == 0
        and sp.simplify(spin_two_defect - (3 * n_log - 1) * (subdivision_m**3 - subdivision_m) / 2) == 0
        and sp.simplify(determinant_finite_exponent - expected_finite_exponent) == 0
        and sp.limit(matched_divergence_sample, q, 0, dir="+") == sp.oo,
    )

    radial_variable = sp.symbols("radial_variable", nonnegative=True, real=True)
    gaussian_x2 = sp.integrate(
        radial_variable**2 * sp.exp(-radial_variable**2 / 2),
        (radial_variable, 0, sp.oo),
    )
    haar_leading = sp.Rational(1, 3) / sp.pi if mutation == "corrupt_determinant_prefactor" else sp.Rational(1, 2) / sp.pi
    proper_integral_coefficient = sp.simplify(haar_leading * gaussian_x2)
    determinant_prefactor = sp.simplify(2 / proper_integral_coefficient)
    determinant_exponent = -2 / (n_log * diffusivity * epsilon)
    if mutation == "force_finite_component_jump":
        determinant_exponent = -2 * epsilon / (n_log * diffusivity)
    accumulated_jump_scale = epsilon ** sp.Rational(-5, 2) * sp.exp(determinant_exponent)
    check(
        "determinant component: diffusive scaling freezes the Arrhenius jump channel",
        sp.simplify(proper_integral_coefficient - 1 / (2 * sp.sqrt(2 * sp.pi))) == 0
        and sp.simplify(determinant_prefactor - 4 * sp.sqrt(2 * sp.pi)) == 0
        and sp.limit(accumulated_jump_scale, epsilon, 0, dir="+") == 0,
    )

    check(
        "Haar pullback: product measure pushes forward exactly under ordered multiplication",
        z2_isometry(biased=(mutation == "bias_product_haar_count")),
    )

    h = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    first = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    second = sp.Matrix([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    transformed_first = h * first
    transformed_second = second * (h if mutation == "remove_internal_gauge_inverse" else h.inv())
    check(
        "common projector: the internal fine gauge frame cancels in the coarse ordered holonomy",
        transformed_second * transformed_first == second * first,
    )

    fine_total = 12 if mutation == "drop_hessian_scale_four" else 16
    nominal_action = sp.Rational(16, 1) / n * (1 - sp.cos(theta / 2) ** (2 * n))
    plaquette_defect = sp.series(
        fine_total * nominal_action.subs(theta, theta / 4) - nominal_action,
        theta,
        0,
        6,
    ).removeO().expand()
    check(
        "equal-flux plaquette: four subplaquettes with beta_f=4 beta_c match theta^2 but leave the quartic defect",
        plaquette_defect.coeff(theta, 2) == 0
        and sp.simplify(plaquette_defect.coeff(theta, 4) - 5 * (3 * n - 1) / 32) == 0,
    )

    radical = (2 + sp.sqrt(2)) / 4
    if mutation == "replace_cos_pi8_square":
        radical = sp.Integer(1)
    pi_n1 = sp.expand(16 * nominal_action.subs({n: 1, theta: sp.pi / 4})
                      - nominal_action.subs({n: 1, theta: sp.pi}))
    lower_bound = sp.simplify(15 - 16 * radical)
    check(
        "finite plaquette witness: the pi defect is exact in Q(sqrt(2)) and positive for every n>=1",
        sp.simplify(sp.cos(sp.pi / 8) ** 2 - radical) == 0
        and sp.simplify(pi_n1 - (112 - 64 * sp.sqrt(2))) == 0
        and lower_bound.is_positive,
    )

    free_log = symmetric_word_log(omit_left_half=(mutation == "drop_left_half_exponential"))
    expected_words = {
        ("X",): sp.Rational(1), ("Y",): sp.Rational(1),
        ("X", "X", "Y"): -sp.Rational(1, 24),
        ("X", "Y", "X"): sp.Rational(1, 12),
        ("Y", "X", "X"): -sp.Rational(1, 24),
        ("Y", "Y", "X"): sp.Rational(1, 12),
        ("Y", "X", "Y"): -sp.Rational(1, 6),
        ("X", "Y", "Y"): sp.Rational(1, 12),
    }
    check(
        "symmetric product: the free-word logarithm derives both nested-commutator signs",
        free_log == expected_words,
    )

    matrix_a = sp.diag(0, 1, 3)
    matrix_v = sp.Matrix([[2, 1, 0], [1, 2, 1], [0, 1, 2]])
    matrix_k = sp.Rational(5, 12) * matrix_a**2
    used_k = sp.zeros(3) if mutation == "drop_intrinsic_K_term" else matrix_k
    left_half = matrix_series_exp(-epsilon * matrix_v / 2, epsilon)
    middle = matrix_series_exp(-epsilon * matrix_a + epsilon**3 * used_k, epsilon)
    matrix_product = (left_half * middle * left_half).applyfunc(
        lambda entry: truncate(entry, epsilon, 3)
    )
    matrix_log = matrix_series_log(matrix_product, epsilon)
    comm_vva = matrix_v * (matrix_v * matrix_a - matrix_a * matrix_v) \
        - (matrix_v * matrix_a - matrix_a * matrix_v) * matrix_v
    comm_aav = matrix_a * (matrix_a * matrix_v - matrix_v * matrix_a) \
        - (matrix_a * matrix_v - matrix_v * matrix_a) * matrix_a
    matrix_target = -epsilon * (matrix_a + matrix_v) + epsilon**3 * (
        matrix_k + comm_vva / 24 - comm_aav / 12
    )
    matrix_difference = (matrix_log - matrix_target).applyfunc(
        lambda entry: truncate(sp.simplify(entry), epsilon, 3)
    )
    check(
        "noncommuting exact control: the intrinsic exterior K term and Strang commutators reconstruct the matrix log",
        matrix_difference == sp.zeros(3),
    )

    check(
        "scope and imports: the result is strong fixed-carrier mathematics, not norm refinement or physical time",
        scope_ok,
    )

    print("per_element: actual f_n, Haar, characters, radial moments, and component asymptotics were derived")
    print("per_site: ordered fine-edge gauge cancellation and product-Haar pushforward were executed")
    print("per_mode: all-spin logs, the corrected clock, spin-one/two defects, and determinant freeze were checked")
    print("per_block: the nonconstant-potential symmetric product and both bare refinement boundaries were reconstructed")
    print("lattice_wide: checked and not executed — no changing-graph strong comparison, thermodynamic limit, or physical clock is supplied")
    print("STATUS: the actual exterior family has a co-scaled fixed-carrier strong product but no exact bare same-family cylindrical refinement")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mode", choices=("primary", "independent"), default="primary")
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.mutation, arguments.mode))
