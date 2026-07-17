#!/usr/bin/env python3
"""Exact checks for the scaled-projector menu forcing and paired boundary note."""

from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md"
PARENT_PATH = ROOT / "docs" / "BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

I2 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
PAULIS = (sx, sy, sz)


def normalize(text):
    return " ".join(text.split())


def matrix_is_zero(matrix):
    return matrix.applyfunc(sp.simplify) == sp.zeros(*matrix.shape)


def exact_eigenvalue_multiset(matrix):
    values = []
    for value, multiplicity in matrix.eigenvals().items():
        values.extend([sp.simplify(value)] * multiplicity)
    return tuple(sorted(values, key=sp.default_sort_key))


def same_multiset(left, right):
    if len(left) != len(right):
        return False
    if len(left) == 2:
        return (
            sp.simplify(left[0] - right[0]) == 0
            and sp.simplify(left[1] - right[1]) == 0
        ) or (
            sp.simplify(left[0] - right[1]) == 0
            and sp.simplify(left[1] - right[0]) == 0
        )
    return tuple(sorted(left, key=sp.default_sort_key)) == tuple(
        sorted(right, key=sp.default_sort_key)
    )


def is_effect(matrix):
    if matrix.shape != (2, 2) or not matrix_is_zero(matrix - matrix.H):
        return False
    return all(
        value.is_real is True
        and value.is_nonnegative is True
        and (sp.Integer(1) - value).is_nonnegative is True
        for value in exact_eigenvalue_multiset(matrix)
    )


def bloch_projector(direction):
    nx, ny, nz = direction
    return (I2 + nx * sx + ny * sy + nz * sz) / 2


def hemisphere_weight(direction):
    nx, ny, nz = (sp.simplify(component) for component in direction)
    for component in (nz, ny, nx):
        if component == 0:
            continue
        if component.is_positive is True:
            return sp.Integer(1)
        if component.is_negative is True:
            return sp.Integer(0)
        raise ValueError("hemisphere sign is not exactly decidable")
    return sp.Integer(0)


def forced_trace_value(samples, target, trace_value=sp.Integer(1)):
    a, d, x, y = sp.symbols("forced_a forced_d forced_x forced_y", real=True)
    sigma = sp.Matrix([[a, x - sp.I * y], [x + sp.I * y, d]])
    equations = [sp.Eq(sp.trace(sigma), trace_value)] + [
        sp.Eq(sp.trace(sigma * bloch_projector(direction)), value)
        for direction, value in samples
    ]
    solution_set = sp.linsolve(equations, (a, d, x, y))
    if solution_set is sp.EmptySet or len(solution_set) != 1:
        return None
    solution = next(iter(solution_set))
    substitutions = dict(zip((a, d, x, y), solution))
    value = sp.simplify(
        sp.trace(sigma * bloch_projector(target)).subs(substitutions)
    )
    if value.free_symbols.intersection({a, d, x, y}):
        return None
    return value


def detects_trace_conflict(samples, target, assigned_value):
    forced = forced_trace_value(samples, target)
    return forced is not None and sp.simplify(forced - assigned_value) != 0


def scaled_projector_parameters(matrix):
    """Return the exact S-branch and recovered parameters, or None."""
    if matrix.shape != (2, 2) or not matrix_is_zero(matrix - matrix.H):
        return None
    eigenvalues = exact_eigenvalue_multiset(matrix)
    c = sp.simplify(sp.trace(matrix))
    if (
        c.is_positive is True
        and (1 - c).is_nonnegative is True
        and same_multiset(eigenvalues, (sp.Integer(0), c))
    ):
        direction = tuple(
            sp.simplify(sp.trace(matrix * pauli) / c) for pauli in PAULIS
        )
        if (
            sp.simplify(sum(component**2 for component in direction) - 1) == 0
            and matrix_is_zero(matrix - c * bloch_projector(direction))
        ):
            return ("projector", c, direction)
    coin_c = sp.simplify(c / 2)
    if (
        coin_c.is_positive is True
        and (1 - coin_c).is_nonnegative is True
        and same_multiset(eigenvalues, (coin_c, coin_c))
        and matrix_is_zero(matrix - coin_c * I2)
    ):
        return ("identity", coin_c, None)
    return None


def valid_scaled_projector_menu(menu):
    return bool(menu) and all(
        scaled_projector_parameters(item) is not None for item in menu
    ) and matrix_is_zero(sum(menu, sp.zeros(2)) - I2)


def unit_sphere_zero(expression, direction):
    """Test a rational identity modulo nx^2+ny^2+nz^2=1."""
    nx, ny, nz = direction
    numerator = sp.together(expression).as_numer_denom()[0]
    relation = nz**2 + nx**2 + ny**2 - 1
    remainder = sp.rem(
        sp.Poly(sp.expand(numerator), nz), sp.Poly(relation, nz)
    ).as_expr()
    return sp.simplify(remainder) == 0


def nonnegative_between(value, variable, lower, upper):
    interval_nonempty = sp.reduce_inequalities(
        [variable > lower, variable < upper], variable
    )
    if interval_nonempty is sp.false or interval_nonempty == False:
        return False
    contradiction = sp.reduce_inequalities(
        [variable > lower, variable < upper, value < 0], variable
    )
    return contradiction is sp.false or contradiction == False


def axis_cancellation_menu(direction):
    axes = (
        (sp.Integer(1), sp.Integer(0), sp.Integer(0)),
        (sp.Integer(0), sp.Integer(1), sp.Integer(0)),
        (sp.Integer(0), sp.Integer(0), sp.Integer(1)),
    )
    length_one = sp.simplify(sum(abs(component) for component in direction))
    c0 = sp.simplify(2 / (1 + length_one))
    menu = [c0 * bloch_projector(direction)]
    for component, axis in zip(direction, axes):
        if component == 0:
            continue
        if component.is_positive is True:
            sign = sp.Integer(1)
        elif component.is_negative is True:
            sign = sp.Integer(-1)
        else:
            raise ValueError("axis component sign is not exactly decidable")
        opposite_axis = tuple(-sign * entry for entry in axis)
        menu.append(
            sp.simplify(c0 * abs(component))
            * bloch_projector(opposite_axis)
        )
    return tuple(menu)


class CheckRunner:
    def __init__(self):
        self.pass_count = 0
        self.fail_count = 0

    def check(self, gate_id, description, condition):
        passed = bool(condition)
        if passed:
            self.pass_count += 1
        else:
            self.fail_count += 1
        print(f"{'PASS' if passed else 'FAIL'}: {gate_id} {description}")

    def total(self):
        print(f"TOTAL: PASS={self.pass_count} FAIL={self.fail_count}")
        return self.fail_count


def main():
    runner = CheckRunner()

    # Group D - domain and parameter recovery
    nx, ny, nz = sp.symbols("nx ny nz", real=True)
    direction = (nx, ny, nz)
    c = sp.symbols("c", positive=True)
    symbolic_projector = bloch_projector(direction)
    scaled_projector = c * symbolic_projector
    projector_idempotence = all(
        unit_sphere_zero(entry, direction)
        for entry in symbolic_projector**2 - symbolic_projector
    )
    traceless_part = scaled_projector - sp.trace(scaled_projector) * I2 / 2
    recovered_coefficients = tuple(
        sp.simplify(sp.trace(traceless_part * pauli) / 2) for pauli in PAULIS
    )
    runner.check(
        "D1",
        "trace and traceless coefficients recover c and c*n/2",
        projector_idempotence
        and matrix_is_zero(symbolic_projector - symbolic_projector.H)
        and sp.simplify(sp.trace(scaled_projector) - c) == 0
        and all(
            sp.simplify(actual - c * component / 2) == 0
            for actual, component in zip(recovered_coefficients, direction)
        ),
    )

    cp = sp.symbols("c_prime", positive=True)
    spectral_parameter = sp.symbols("spectral_parameter")
    projector_characteristic = sp.det(
        spectral_parameter * I2 - scaled_projector
    )
    coin_characteristic = sp.det(spectral_parameter * I2 - cp * I2)
    projector_spectrum_certificate = unit_sphere_zero(
        projector_characteristic - spectral_parameter * (spectral_parameter - c),
        direction,
    )
    spectral_collision_solution = sp.solve(
        [sp.Eq(cp, 0), sp.Eq(cp, c)], (cp, c), dict=True
    )
    runner.check(
        "D2-types",
        "rank-one and identity rays have incompatible exact eigenvalue multisets",
        projector_spectrum_certificate
        and sp.simplify(coin_characteristic - (spectral_parameter - cp) ** 2)
        == 0
        and c.is_positive is True
        and cp.is_positive is True
        and spectral_collision_solution == [],
    )

    npx, npy, npz = sp.symbols("npx npy npz", real=True)
    prime_direction = (npx, npy, npz)
    scaled_projector_prime = cp * bloch_projector(prime_direction)
    trace_difference = sp.simplify(
        sp.trace(scaled_projector - scaled_projector_prime)
    )
    pauli_differences = tuple(
        sp.simplify(sp.trace((scaled_projector - scaled_projector_prime) * pauli))
        for pauli in PAULIS
    )
    direction_after_trace = tuple(
        sp.simplify(value.subs(cp, c) / c) for value in pauli_differences
    )
    runner.check(
        "D2-projectors",
        "equal nonzero scaled projectors force equal scale and direction",
        trace_difference == c - cp
        and direction_after_trace
        == tuple(
            component - prime_component
            for component, prime_component in zip(direction, prime_direction)
        ),
    )

    # Group T1 - exact menu characterization
    c1, c2, c3, d = sp.symbols("c1 c2 c3 d", real=True)
    direction_symbols = sp.symbols("n1x n1y n1z n2x n2y n2z n3x n3y n3z", real=True)
    directions = tuple(
        tuple(direction_symbols[3 * index : 3 * index + 3]) for index in range(3)
    )
    coefficients = (c1, c2, c3)
    generic_sum = sum(
        (coefficient * bloch_projector(item_direction)
         for coefficient, item_direction in zip(coefficients, directions)),
        d * I2,
    )
    residual = generic_sum - I2
    scalar_condition = sp.simplify(sum(coefficients) / 2 + d - 1)
    vector_conditions = tuple(
        sp.simplify(
            sum(
                coefficient * item_direction[axis]
                for coefficient, item_direction in zip(coefficients, directions)
            )
        )
        for axis in range(3)
    )
    residual_from_conditions = scalar_condition * I2 + sum(
        (vector_conditions[index] * PAULIS[index] / 2 for index in range(3)),
        sp.zeros(2),
    )
    recovered_conditions = (sp.trace(residual) / 2,) + tuple(
        sp.trace(residual * pauli) for pauli in PAULIS
    )
    runner.check(
        "T1a",
        "generic three-ray plus one-coin residual vanishes iff scalar and vector conditions do",
        matrix_is_zero(residual - residual_from_conditions)
        and all(
            sp.simplify(actual - expected) == 0
            for actual, expected in zip(
                recovered_conditions, (scalar_condition,) + vector_conditions
            )
        ),
    )

    minus_direction = tuple(-component for component in direction)
    projective_menu_sum = bloch_projector(direction) + bloch_projector(minus_direction)
    runner.check(
        "T1b-projective",
        "symbolic antipodal projective menu sums to identity",
        projector_idempotence and matrix_is_zero(projective_menu_sum - I2),
    )

    coin_c = sp.symbols("coin_c", real=True)
    coin_interval = sp.reduce_inequalities(
        [coin_c > 0, coin_c < 1], coin_c
    )
    runner.check(
        "T1b-coin",
        "symbolic two-outcome identity coin sums to identity",
        coin_interval is not sp.false
        and coin_interval != False
        and matrix_is_zero(coin_c * I2 + (1 - coin_c) * I2 - I2),
    )

    split_l, split_m, split_r = sp.symbols(
        "split_l split_m split_r", positive=True
    )
    split_sum = (
        split_l * bloch_projector(direction)
        + split_m * bloch_projector(direction)
        + split_r * bloch_projector(direction)
        + bloch_projector(minus_direction)
    )
    runner.check(
        "T1b-split",
        "symbolic same-direction split menu sums to identity under l+m+r=1",
        matrix_is_zero(split_sum.subs(split_r, 1 - split_l - split_m) - I2),
    )

    coplanar_directions = (
        (sp.Integer(1), sp.Integer(0), sp.Integer(0)),
        (-sp.Rational(1, 2), sp.sqrt(3) / 2, sp.Integer(0)),
        (-sp.Rational(1, 2), -sp.sqrt(3) / 2, sp.Integer(0)),
    )
    coplanar_menu = tuple(
        sp.Rational(2, 3) * bloch_projector(item_direction)
        for item_direction in coplanar_directions
    )
    runner.check(
        "T1b-coplanar",
        "exact three-element coplanar scaled-projector menu sums to identity",
        all(
            sp.simplify(sum(component**2 for component in item_direction) - 1) == 0
            for item_direction in coplanar_directions
        )
        and valid_scaled_projector_menu(coplanar_menu),
    )

    px, py, pz = sp.symbols("px py pz", positive=True)
    positive_direction = (px, py, pz)
    positive_length = px + py + pz
    positive_c0 = sp.simplify(2 / (1 + positive_length))
    generic_axis_sum = (
        positive_c0 * bloch_projector(positive_direction)
        + positive_c0 * px * bloch_projector((-1, 0, 0))
        + positive_c0 * py * bloch_projector((0, -1, 0))
        + positive_c0 * pz * bloch_projector((0, 0, -1))
    )
    pair_sum = px * py + px * pz + py * pz
    c0_upper_certificate = sp.simplify(2 * pair_sum / (1 + positive_length) ** 2)
    coefficient_upper_certificates = tuple(
        sp.simplify(
            (
                sum(other**2 for other in positive_direction if other != component)
                / (1 + component)
                + sum(other for other in positive_direction if other != component)
            )
            / (1 + positive_length)
        )
        for component in positive_direction
    )
    runner.check(
        "T1c-generic",
        "generic positive-octant axis cancellation is a menu with coefficients in (0,1]",
        matrix_is_zero(generic_axis_sum - I2)
        and positive_c0.is_positive is True
        and all((positive_c0 * component).is_positive is True for component in positive_direction)
        and c0_upper_certificate.is_positive is True
        and unit_sphere_zero(1 - positive_c0 - c0_upper_certificate, positive_direction)
        and all(
            certificate.is_positive is True
            and unit_sphere_zero(
                1 - positive_c0 * component - certificate,
                positive_direction,
            )
            for component, certificate in zip(
                positive_direction, coefficient_upper_certificates
            )
        ),
    )

    octant_signs = (
        (1, 1, 1),
        (1, 1, -1),
        (1, -1, 1),
        (1, -1, -1),
        (-1, 1, 1),
        (-1, 1, -1),
        (-1, -1, 1),
        (-1, -1, -1),
    )
    for index, signs in enumerate(octant_signs, start=1):
        octant_direction = tuple(
            sign * component
            for sign, component in zip(
                signs, (sp.Rational(3, 7), sp.Rational(6, 7), sp.Rational(2, 7))
            )
        )
        octant_menu = axis_cancellation_menu(octant_direction)
        runner.check(
            f"T1c-octant-{index}",
            "rational octant witness is an exact axis-cancellation menu",
            sp.simplify(sum(component**2 for component in octant_direction) - 1) == 0
            and valid_scaled_projector_menu(octant_menu),
        )

    zero_component_direction = (
        sp.Rational(3, 5), sp.Integer(0), -sp.Rational(4, 5)
    )
    zero_component_menu = axis_cancellation_menu(zero_component_direction)
    runner.check(
        "T1c-zero-component",
        "zero-component axis menu omits the zero-weight element and sums exactly",
        len(zero_component_menu) == 3
        and valid_scaled_projector_menu(zero_component_menu),
    )

    e_z = (sp.Integer(0), sp.Integer(0), sp.Integer(1))
    axis_menu = axis_cancellation_menu(e_z)
    runner.check(
        "T1c-axis",
        "axis cancellation degenerates to the antipodal projective menu",
        len(axis_menu) == 2
        and valid_scaled_projector_menu(axis_menu)
        and all(
            matrix_is_zero(actual - expected)
            for actual, expected in zip(
                axis_menu, (bloch_projector(e_z), bloch_projector((0, 0, -1)))
            )
        ),
    )

    reject_direction = (
        sp.Rational(3, 7), sp.Rational(6, 7), sp.Rational(2, 7)
    )
    full_axis_menu = axis_cancellation_menu(reject_direction)
    dropped_axis_menu = full_axis_menu[:-1]
    runner.check(
        "T1d",
        "menu checker rejects an axis family with a vector-cancelling element dropped",
        all(scaled_projector_parameters(item) is not None for item in dropped_axis_menu)
        and not matrix_is_zero(sum(dropped_axis_menu, sp.zeros(2)) - I2)
        and not valid_scaled_projector_menu(dropped_axis_menu),
    )

    unsharp_effect = sp.diag(sp.Rational(1, 2), sp.Rational(1, 4))
    runner.check(
        "T1e",
        "effect with two distinct nonzero eigenvalues is outside S",
        is_effect(unsharp_effect)
        and exact_eigenvalue_multiset(unsharp_effect)
        == (sp.Rational(1, 4), sp.Rational(1, 2))
        and scaled_projector_parameters(unsharp_effect) is None,
    )

    # Group T2 - forcing on the scaled-projector family
    h_l, h_m, h_lm, h_r, g_minus = sp.symbols(
        "h_l h_m h_lm h_r g_minus", real=True
    )
    ray_solution = sp.solve(
        [
            sp.Eq(h_l + h_m + h_r + g_minus, 1),
            sp.Eq(h_lm + h_r + g_minus, 1),
        ],
        (h_lm, g_minus),
        dict=True,
    )
    split_first = (
        split_l * bloch_projector(direction)
        + split_m * bloch_projector(direction)
        + (1 - split_l - split_m) * bloch_projector(direction)
        + bloch_projector(minus_direction)
    )
    split_regrouped = (
        (split_l + split_m) * bloch_projector(direction)
        + (1 - split_l - split_m) * bloch_projector(direction)
        + bloch_projector(minus_direction)
    )
    runner.check(
        "T2a",
        "two valid split-menu normalizations eliminate to ray additivity",
        projector_idempotence
        and matrix_is_zero(split_first - I2)
        and matrix_is_zero(split_regrouped - I2)
        and len(ray_solution) == 1
        and sp.simplify(ray_solution[0][h_lm] - h_l - h_m) == 0,
    )

    h_one, h_half, h_third, h_two_thirds, h_remainder = sp.symbols(
        "h_one h_half h_third h_two_thirds h_remainder", real=True
    )
    half_solution = sp.solve(
        [
            sp.Eq(2 * h_half + h_remainder, 1),
            sp.Eq(h_one + h_remainder, 1),
        ],
        (h_half, h_remainder),
        dict=True,
    )
    thirds_solution = sp.solve(
        [
            sp.Eq(3 * h_third + h_remainder, 1),
            sp.Eq(h_one + h_remainder, 1),
            sp.Eq(h_two_thirds, 2 * h_third),
        ],
        (h_third, h_two_thirds, h_remainder),
        dict=True,
    )
    runner.check(
        "T2b-rational",
        "ray additivity gives exact homogeneity at one-half and two-thirds",
        len(half_solution) == 1
        and len(thirds_solution) == 1
        and sp.simplify(half_solution[0][h_half] - h_one / 2) == 0
        and sp.simplify(
            thirds_solution[0][h_two_thirds] - 2 * h_one / 3
        )
        == 0,
    )

    h_lower, h_upper = sp.symbols("h_lower h_upper", real=True)
    h_increment = sp.symbols("h_increment", nonnegative=True)
    monotone_solution = sp.solve(
        [sp.Eq(h_upper, h_lower + h_increment)], h_upper, dict=True
    )
    monotone_difference = sp.simplify(
        (h_upper - h_lower).subs(monotone_solution[0])
    )
    runner.check(
        "T2b-monotone",
        "nonnegative ray increments force monotonicity",
        monotone_difference == h_increment
        and monotone_difference.is_nonnegative is True,
    )

    t = sp.symbols("t", real=True)
    q1 = sp.Rational(1, 2)
    q2 = sp.Rational(2, 3)
    squeeze_interval_ok = nonnegative_between(t - q1, t, q1, q2) and nonnegative_between(
        q2 - t, t, q1, q2
    )
    h_t, h_base = sp.symbols("h_t h_base", real=True)
    lower_weight, upper_weight = sp.symbols(
        "lower_weight upper_weight", nonnegative=True
    )
    squeeze_solution = sp.solve(
        [
            sp.Eq(h_t, q1 * h_base + lower_weight),
            sp.Eq(q2 * h_base, h_t + upper_weight),
        ],
        (h_base, h_t),
        dict=True,
    )
    squeeze_lower_residual = sp.simplify(
        (h_t - q1 * h_base).subs(squeeze_solution[0])
    )
    squeeze_upper_residual = sp.simplify(
        (q2 * h_base - h_t).subs(squeeze_solution[0])
    )
    runner.check(
        "T2b-squeeze",
        "hardened nonempty-interval guard and formal squeeze hold between one-half and two-thirds",
        squeeze_interval_ok
        and squeeze_lower_residual == lower_weight
        and squeeze_upper_residual == upper_weight
        and squeeze_lower_residual.is_nonnegative is True
        and squeeze_upper_residual.is_nonnegative is True,
    )

    toy_small = sp.Rational(1, 4) * bloch_projector(e_z)
    toy_large = sp.Rational(1, 2) * bloch_projector(e_z)
    toy_weights = {
        "small": sp.Rational(3, 4),
        "large": sp.Rational(1, 4),
    }
    runner.check(
        "T2b-rejector",
        "checker detects a non-monotone toy assignment on one ray",
        scaled_projector_parameters(toy_small) is not None
        and scaled_projector_parameters(toy_large - toy_small) is not None
        and (toy_weights["large"] - toy_weights["small"]).is_negative is True,
    )

    g_n, g_n_complement = sp.symbols("g_n g_n_complement", real=True)
    complement_solution = sp.solve(
        [sp.Eq(g_n + g_n_complement, 1)], g_n_complement, dict=True
    )
    runner.check(
        "T2c",
        "projective-menu normalization formally gives the complement identity",
        matrix_is_zero(projective_menu_sum - I2)
        and len(complement_solution) == 1
        and sp.simplify(complement_solution[0][g_n_complement] - (1 - g_n))
        == 0,
    )

    g_xp, g_xm, g_yp, g_ym, g_zp, g_zm = sp.symbols(
        "g_xp g_xm g_yp g_ym g_zp g_zm", real=True
    )
    axis_g = sp.symbols("axis_g", real=True)
    axis_affinity_solution = sp.solve(
        [
            sp.Eq(g_xp + g_xm, 1),
            sp.Eq(g_yp + g_ym, 1),
            sp.Eq(g_zp + g_zm, 1),
            sp.Eq(
                positive_c0 * axis_g
                + positive_c0 * px * g_xm
                + positive_c0 * py * g_ym
                + positive_c0 * pz * g_zm,
                1,
            ),
        ],
        (axis_g, g_xm, g_ym, g_zm),
        dict=True,
    )
    s_axes = (2 * g_xp - 1, 2 * g_yp - 1, 2 * g_zp - 1)
    positive_affine_target = sp.simplify(
        (1 + sum(component * s_axis for component, s_axis in zip(positive_direction, s_axes)))
        / 2
    )
    runner.check(
        "T2d-generic",
        "complements and the symbolic positive-octant axis menu eliminate to Bloch affinity",
        len(axis_affinity_solution) == 1
        and sp.simplify(
            axis_affinity_solution[0][axis_g] - positive_affine_target
        )
        == 0,
    )

    axis_value_by_sign = (
        (g_xp, g_xm),
        (g_yp, g_ym),
        (g_zp, g_zm),
    )
    complement_substitutions = {g_xm: 1 - g_xp, g_ym: 1 - g_yp, g_zm: 1 - g_zp}

    def axis_menu_forced_value(witness_direction):
        witness_length = sp.simplify(
            sum(abs(component) for component in witness_direction)
        )
        witness_c0 = sp.simplify(2 / (1 + witness_length))
        normalization_left = witness_c0 * axis_g
        for component, (positive_value, negative_value) in zip(
            witness_direction, axis_value_by_sign
        ):
            if component == 0:
                continue
            if component.is_positive is True:
                opposite_value = negative_value
            elif component.is_negative is True:
                opposite_value = positive_value
            else:
                raise ValueError("axis component sign is not exactly decidable")
            normalization_left += witness_c0 * abs(component) * opposite_value
        solved = sp.solve(
            [sp.Eq(normalization_left.subs(complement_substitutions), 1)],
            axis_g,
            dict=True,
        )
        if len(solved) != 1:
            return None
        return sp.simplify(solved[0][axis_g])

    for index, signs in enumerate(octant_signs, start=1):
        octant_direction = tuple(
            sign * component
            for sign, component in zip(
                signs, (sp.Rational(3, 7), sp.Rational(6, 7), sp.Rational(2, 7))
            )
        )
        forced_value = axis_menu_forced_value(octant_direction)
        affine_target = sp.simplify(
            (1 + sum(component * s_axis for component, s_axis in zip(octant_direction, s_axes)))
            / 2
        )
        runner.check(
            f"T2d-octant-{index}",
            "rational octant axis normalization gives the same affine value",
            forced_value is not None
            and sp.simplify(forced_value - affine_target) == 0,
        )

    zero_forced_value = axis_menu_forced_value(zero_component_direction)
    zero_affine_target = sp.simplify(
        (1 + sum(component * s_axis for component, s_axis in zip(zero_component_direction, s_axes)))
        / 2
    )
    runner.check(
        "T2d-zero-component",
        "zero-component axis normalization gives the same affine value",
        zero_forced_value is not None
        and sp.simplify(zero_forced_value - zero_affine_target) == 0,
    )

    f_c, f_cp, f_sum, f_remainder = sp.symbols(
        "f_c f_cp f_sum f_remainder", real=True
    )
    coin_additivity_solution = sp.solve(
        [
            sp.Eq(f_c + f_cp + f_remainder, 1),
            sp.Eq(f_sum + f_remainder, 1),
        ],
        (f_sum, f_remainder),
        dict=True,
    )
    runner.check(
        "T2e-additivity",
        "two coin-menu normalizations eliminate to identity-ray additivity",
        len(coin_additivity_solution) == 1
        and sp.simplify(coin_additivity_solution[0][f_sum] - f_c - f_cp) == 0,
    )

    rational_numerator = sp.symbols("rational_numerator", positive=True, integer=True)
    rational_denominator = sp.symbols(
        "rational_denominator", positive=True, integer=True
    )
    f_unit_fraction, f_rational = sp.symbols(
        "f_unit_fraction f_rational", real=True
    )
    rational_value_solution = sp.solve(
        [
            sp.Eq(rational_denominator * f_unit_fraction, 1),
            sp.Eq(f_rational, rational_numerator * f_unit_fraction),
        ],
        (f_unit_fraction, f_rational),
        dict=True,
    )
    runner.check(
        "T2e-rational",
        "coin additivity and f(1)=1 give f(p/r)=p/r",
        len(rational_value_solution) == 1
        and sp.simplify(
            rational_value_solution[0][f_rational]
            - rational_numerator / rational_denominator
        )
        == 0,
    )

    f_t, f_base = sp.symbols("f_t f_base", real=True)
    f_lower_weight, f_upper_weight = sp.symbols(
        "f_lower_weight f_upper_weight", nonnegative=True
    )
    coin_squeeze_solution = sp.solve(
        [
            sp.Eq(f_t, q1 * f_base + f_lower_weight),
            sp.Eq(q2 * f_base, f_t + f_upper_weight),
        ],
        (f_base, f_t),
        dict=True,
    )
    coin_lower_residual = sp.simplify(
        (f_t - q1 * f_base).subs(coin_squeeze_solution[0])
    )
    coin_upper_residual = sp.simplify(
        (q2 * f_base - f_t).subs(coin_squeeze_solution[0])
    )
    runner.check(
        "T2e-squeeze",
        "coin continuity uses the same hardened rational-squeeze scaffolding",
        squeeze_interval_ok
        and nonnegative_between(t - q1, t, q1, q2)
        and nonnegative_between(q2 - t, t, q1, q2)
        and coin_lower_residual == f_lower_weight
        and coin_upper_residual == f_upper_weight
        and coin_lower_residual.is_nonnegative is True
        and coin_upper_residual.is_nonnegative is True,
    )

    s_x, s_y, s_z = sp.symbols("s_x s_y s_z", real=True)
    s_length = sp.symbols("s_length", positive=True)
    s_squared = s_x**2 + s_y**2 + s_z**2
    negative_s_direction = (-s_x / s_length, -s_y / s_length, -s_z / s_length)
    g_at_negative_s = sp.simplify(
        (1 + sum(component * s_axis for component, s_axis in zip(
            negative_s_direction, (s_x, s_y, s_z)
        )))
        / 2
    )
    g_at_negative_s_on_radius = sp.simplify(
        g_at_negative_s.subs(s_z**2, s_length**2 - s_x**2 - s_y**2)
    )
    g_minimum = sp.symbols("g_minimum", nonnegative=True)
    norm_solution = sp.solve(
        [sp.Eq(g_minimum, g_at_negative_s_on_radius)], s_length, dict=True
    )
    norm_margin = sp.simplify(
        (1 - s_length).subs(norm_solution[0])
    )
    sigma_state = (I2 + s_x * sx + s_y * sy + s_z * sz) / 2
    state_spectral_parameter = sp.symbols("state_spectral_parameter")
    state_characteristic = sp.det(state_spectral_parameter * I2 - sigma_state)
    target_characteristic = (
        state_spectral_parameter - (1 - s_length) / 2
    ) * (
        state_spectral_parameter - (1 + s_length) / 2
    )
    state_char_numerator = sp.together(
        state_characteristic - target_characteristic
    ).as_numer_denom()[0]
    state_char_remainder = sp.rem(
        sp.Poly(sp.expand(state_char_numerator), s_z),
        sp.Poly(s_z**2 + s_x**2 + s_y**2 - s_length**2, s_z),
    ).as_expr()
    lower_state_eigenvalue = (1 - s_length) / 2
    upper_state_eigenvalue = (1 + s_length) / 2
    runner.check(
        "T2f-state",
        "the antipodal minimum forces norm at most one and sigma is a density matrix",
        g_at_negative_s_on_radius == (1 - s_length) / 2
        and len(norm_solution) == 1
        and norm_margin == 2 * g_minimum
        and norm_margin.is_nonnegative is True
        and sp.trace(sigma_state) == 1
        and sp.simplify(state_char_remainder) == 0
        and sp.simplify(
            lower_state_eigenvalue.subs(norm_solution[0]) - g_minimum
        )
        == 0
        and upper_state_eigenvalue.is_positive is True,
    )

    representation_scale = sp.symbols("representation_scale", positive=True)
    representation_direction = (nx, ny, nz)
    affine_value = sp.simplify(
        (1 + nx * s_x + ny * s_y + nz * s_z) / 2
    )
    runner.check(
        "T2f-representation",
        "sigma represents every symbolic scaled projector and identity multiple",
        sp.simplify(
            sp.trace(
                sigma_state
                * representation_scale
                * bloch_projector(representation_direction)
            )
            - representation_scale * affine_value
        )
        == 0
        and sp.simplify(
            sp.trace(sigma_state * representation_scale * I2)
            - representation_scale
        )
        == 0,
    )

    delta_a, delta_d, delta_x, delta_y = sp.symbols(
        "delta_a delta_d delta_x delta_y", real=True
    )
    hermitian_difference = sp.Matrix(
        [
            [delta_a, delta_x - sp.I * delta_y],
            [delta_x + sp.I * delta_y, delta_d],
        ]
    )
    uniqueness_solution = sp.solve(
        [
            sp.Eq(sp.trace(hermitian_difference * observable), 0)
            for observable in (
                bloch_projector((1, 0, 0)),
                bloch_projector((0, 1, 0)),
                bloch_projector((0, 0, 1)),
                I2,
            )
        ],
        (delta_a, delta_d, delta_x, delta_y),
        dict=True,
    )
    runner.check(
        "T2f-uniqueness",
        "four trace values determine a Hermitian M2 representative uniquely",
        uniqueness_solution
        == [{delta_a: 0, delta_d: 0, delta_x: 0, delta_y: 0}],
    )

    # Group T3 - paired-menu boundary
    pair_g1, pair_g1c, pair_g2, pair_g2c = sp.symbols(
        "pair_g1 pair_g1c pair_g2 pair_g2c", real=True
    )
    pair_l1, pair_l2, pair_d = sp.symbols(
        "pair_l1 pair_l2 pair_d", real=True
    )
    paired_weight_sum = (
        pair_l1 * (pair_g1 + pair_g1c)
        + pair_l2 * (pair_g2 + pair_g2c)
        + pair_d
    )
    paired_solution = sp.solve(
        [
            sp.Eq(pair_g1 + pair_g1c, 1),
            sp.Eq(pair_g2 + pair_g2c, 1),
            sp.Eq(pair_l1 + pair_l2 + pair_d, 1),
        ],
        (pair_g1c, pair_g2c, pair_d),
        dict=True,
    )
    paired_normalization_ok = (
        len(paired_solution) == 1
        and sp.simplify(paired_weight_sum.subs(paired_solution[0]) - 1) == 0
    )
    runner.check(
        "T3a",
        "two-pair plus one-coin rogue normalization reduces to the T1 scalar condition",
        paired_normalization_ok,
    )

    e_x = (sp.Integer(1), sp.Integer(0), sp.Integer(0))
    inv_sqrt2 = sp.sqrt(2) / 2
    u_direction = (inv_sqrt2, sp.Integer(0), -inv_sqrt2)
    hemisphere_values_ok = (
        hemisphere_weight(e_x) == 1
        and hemisphere_weight(e_z) == 1
        and hemisphere_weight(u_direction) == 0
        and hemisphere_weight(tuple(-component for component in e_x)) == 0
        and hemisphere_weight(tuple(-component for component in e_z)) == 0
        and hemisphere_weight(u_direction)
        + hemisphere_weight(tuple(-component for component in u_direction))
        == 1
    )
    runner.check(
        "T3b-hemisphere",
        "lexicographic hemisphere rogue has the required tie-aware values",
        hemisphere_values_ok,
    )

    rogue_samples = ((e_x, sp.Integer(1)), (e_z, sp.Integer(1)))
    rogue_forced_u = forced_trace_value(rogue_samples, u_direction)
    rogue_conflict_ok = (
        rogue_forced_u == sp.Rational(1, 2)
        and detects_trace_conflict(
            rogue_samples, u_direction, hemisphere_weight(u_direction)
        )
    )
    runner.check(
        "T3b-conflict",
        "normalization and two rogue values force trace value one-half at u",
        rogue_conflict_ok,
    )

    def affine_z_weight(item_direction):
        return sp.simplify((1 + item_direction[2]) / 2)

    affine_samples = (
        (e_x, affine_z_weight(e_x)),
        (e_z, affine_z_weight(e_z)),
    )
    affine_forced_u = forced_trace_value(affine_samples, u_direction)
    affine_sigma = (I2 + sz) / 2
    affine_control_ok = (
        affine_forced_u == affine_z_weight(u_direction)
        and not detects_trace_conflict(
            affine_samples, u_direction, affine_z_weight(u_direction)
        )
        and all(
            sp.simplify(
                sp.trace(affine_sigma * bloch_projector(item_direction))
                - affine_z_weight(item_direction)
            )
            == 0
            for item_direction in (e_x, e_z, u_direction)
        )
    )
    runner.check(
        "T3b-control",
        "affine Bloch control remains consistent and is not falsely detected",
        affine_control_ok,
    )

    split_direction = e_z
    split_antipode = tuple(-component for component in split_direction)
    split_weights_side = (
        sp.Rational(1, 5),
        sp.Rational(1, 4),
        1 - sp.Rational(1, 5) - sp.Rational(1, 4),
    )
    split_weights_antipode = (sp.Integer(1),)
    exact_split_menu = tuple(
        weight * bloch_projector(split_direction)
        for weight in split_weights_side
    ) + tuple(
        weight * bloch_projector(split_antipode)
        for weight in split_weights_antipode
    )
    split_unpaired = (
        valid_scaled_projector_menu(exact_split_menu)
        and tuple(sorted(split_weights_side, key=sp.default_sort_key))
        != tuple(sorted(split_weights_antipode, key=sp.default_sort_key))
    )
    runner.check(
        "T3c-split",
        "exact split witness has no equal-weight antipodal perfect matching",
        split_unpaired,
    )

    positive_octant_direction = (
        sp.Rational(3, 7), sp.Rational(6, 7), sp.Rational(2, 7)
    )
    positive_octant_axis_directions = (
        positive_octant_direction,
        (-sp.Integer(1), sp.Integer(0), sp.Integer(0)),
        (sp.Integer(0), -sp.Integer(1), sp.Integer(0)),
        (sp.Integer(0), sp.Integer(0), -sp.Integer(1)),
    )
    pair_dots = tuple(
        sp.simplify(
            sum(left_component * right_component for left_component, right_component in zip(left, right))
        )
        for left_index, left in enumerate(positive_octant_axis_directions)
        for right in positive_octant_axis_directions[left_index + 1 :]
    )
    axis_unpaired = (
        valid_scaled_projector_menu(axis_cancellation_menu(positive_octant_direction))
        and len(pair_dots) == 6
        and all(sp.simplify(dot + 1) != 0 for dot in pair_dots)
    )
    runner.check(
        "T3c-axis",
        "positive-octant axis menu has four pairwise non-antipodal directions",
        axis_unpaired,
    )

    cubic_nz = sp.symbols("cubic_nz", real=True)
    cubic_weight = (1 + cubic_nz**3) / 2
    cubic_complement = sp.simplify(
        cubic_weight + (1 + (-cubic_nz) ** 3) / 2 - 1
    )
    cubic_lower_bound = sp.reduce_inequalities(
        [cubic_nz >= -1, cubic_nz <= 1, cubic_weight < 0], cubic_nz
    )
    cubic_upper_bound = sp.reduce_inequalities(
        [cubic_nz >= -1, cubic_nz <= 1, cubic_weight > 1], cubic_nz
    )
    runner.check(
        "T3a-ind-complement",
        "cubic witness obeys the complement law and stays inside [0,1]",
        cubic_complement == 0
        and (cubic_lower_bound is sp.false or cubic_lower_bound == False)
        and (cubic_upper_bound is sp.false or cubic_upper_bound == False),
    )

    cubic_axis_values = tuple(
        sp.simplify((1 + sp.Integer(axis_direction[2]) ** 3) / sp.Integer(2))
        for axis_direction in ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    )
    cubic_s = tuple(2 * value - 1 for value in cubic_axis_values)
    cubic_m = (sp.sqrt(3) / 2, sp.Integer(0), sp.Rational(1, 2))
    cubic_trace_candidate = sp.simplify(
        (1 + sum(component * s_component for component, s_component in zip(cubic_m, cubic_s)))
        / 2
    )
    cubic_witness_value = sp.simplify((1 + cubic_m[2] ** 3) / 2)
    runner.check(
        "T3a-ind-nontrace",
        "cubic witness refutes its unique trace-form candidate at an exact direction",
        cubic_axis_values == (sp.Rational(1, 2), sp.Rational(1, 2), sp.Integer(1))
        and cubic_s == (0, 0, 1)
        and sp.simplify(sum(component**2 for component in cubic_m) - 1) == 0
        and cubic_trace_candidate == sp.Rational(3, 4)
        and cubic_witness_value == sp.Rational(9, 16)
        and sp.simplify(cubic_trace_candidate - cubic_witness_value) != 0,
    )

    cubic_pair_direction = cubic_m
    cubic_pair_weight = sp.Rational(2, 5)
    cubic_pair_sum = sp.simplify(
        cubic_pair_weight * ((1 + cubic_pair_direction[2] ** 3) / 2)
        + cubic_pair_weight * ((1 + (-cubic_pair_direction[2]) ** 3) / 2)
        + (1 - cubic_pair_weight)
    )
    runner.check(
        "T3a-ind-paired",
        "cubic witness normalizes an exact paired menu with a coin",
        cubic_pair_sum == 1,
    )

    runner.check(
        "T3d-corollary",
        "corollary: paired rogue survives, so forcing uses split and axis-cancellation schemas",
        paired_normalization_ok
        and hemisphere_values_ok
        and rogue_conflict_ok
        and affine_control_ok
        and split_unpaired
        and axis_unpaired,
    )

    # Group N - exact document needle checks
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    parent_text = PARENT_PATH.read_text(encoding="utf-8")
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8")
    note_normalized = normalize(note_text)
    parent_normalized = normalize(parent_text)
    axiom_normalized = normalize(axiom_text)

    runner.check(
        "N1",
        "axiom memo pins record readability to record content alone",
        "Only records are readable. A readout value is determined by record content alone."
        in axiom_normalized,
    )

    runner.check(
        "N2",
        "parent note names intermediate classical mixtures as untested",
        "classical mixtures of projective menus and other intermediate families"
        in parent_normalized,
    )

    runner.check(
        "N3",
        "parent note pins the menu-grade hypothesis surface as underived",
        "Whether the physical registration supplies menus at projective grade, at effect grade, at neither, or at some intermediate family is underived and is not decided here."
        in parent_normalized,
    )

    runner.check(
        "N4-claim",
        "source note pins its exact claim identifier",
        "claim_id: born_form_scaled_projector_menu_family_sitewise_forcing_and_paired_menu_boundary_bounded_theorem_note_2026-07-17"
        in note_text,
    )

    runner.check(
        "N4-labels",
        "source note contains both scaled-projector hypothesis labels",
        "**(F1)" in note_text and "**(F2)" in note_text,
    )

    runner.check(
        "N4-no-bridge",
        "source note pins the no-literature-bridge-input scope",
        "no literature bridge input" in note_normalized,
    )

    runner.check(
        "N4-paired",
        "source note states that the paired subfamily does not force",
        "The paired subfamily does not force" in note_normalized,
    )

    failures = runner.total()
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
