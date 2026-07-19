#!/usr/bin/env python3
"""Exact checks for the outcome-threshold and mixed-projective forcing note."""

from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md"
SCALED_PARENT_PATH = ROOT / "docs" / "BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md"
EFFECT_PARENT_PATH = ROOT / "docs" / "BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md"
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


def scaled_projector_parameters(matrix):
    """Return the exact scaled-family branch and parameters, or None."""
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
    return (
        bool(menu)
        and all(scaled_projector_parameters(item) is not None for item in menu)
        and matrix_is_zero(sum(menu, sp.zeros(2)) - I2)
    )


def bloch_projector(direction):
    nx, ny, nz = direction
    return (I2 + nx * sx + ny * sy + nz * sz) / 2


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


def witness_f(value):
    value = sp.sympify(value)
    return sp.cancel(value**3 / (value**3 + (1 - value) ** 3))


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


def normalization_violation(values):
    return sp.simplify(sum(values, sp.Integer(0)) - 1) != 0


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

    # Group F - exact witness function
    t = sp.symbols("t", real=True)
    complement_residual = sp.factor(witness_f(t) + witness_f(1 - t) - 1)
    runner.check(
        "F1-complement",
        "f(t)+f(1-t)=1 identically",
        complement_residual == 0,
    )
    runner.check(
        "F1-endpoints",
        "f has the exact endpoint values zero and one",
        witness_f(0) == 0 and witness_f(1) == 1,
    )

    denominator = sp.expand(t**3 + (1 - t) ** 3)
    denominator_certificate = 3 * (t - sp.Rational(1, 2)) ** 2 + sp.Rational(1, 4)
    runner.check(
        "F2-identity",
        "the cubic denominator has the completed-square form",
        sp.expand(denominator - denominator_certificate) == 0,
    )
    runner.check(
        "F2-lower-bound",
        "the completed-square denominator is at least one-quarter",
        sp.simplify(denominator_certificate - sp.Rational(1, 4)).is_nonnegative
        is True,
    )
    witness_derivative = sp.diff(witness_f(t), t)
    derivative_certificate = 3 * t**2 * (1 - t) ** 2 / denominator**2
    runner.check(
        "F2-smooth-monotone",
        "the exact derivative is nonnegative wherever the positive denominator is used",
        sp.factor(witness_derivative - derivative_certificate) == 0,
    )

    exact_f_values = tuple(
        witness_f(value)
        for value in (
            sp.Rational(1, 4),
            sp.Rational(1, 2),
            sp.Rational(5, 8),
            sp.Rational(3, 4),
        )
    )
    runner.check(
        "F3",
        "f has all four specified exact rational values",
        exact_f_values
        == (
            sp.Rational(1, 28),
            sp.Rational(1, 2),
            sp.Rational(125, 152),
            sp.Rational(27, 28),
        ),
    )

    # Group T1 - binary-menu boundary
    nx, ny, nz = sp.symbols("nx ny nz", real=True)
    direction = (nx, ny, nz)
    sigma0 = (I2 + sp.Rational(1, 2) * sz) / 2
    projector_trace = sp.simplify(sp.trace(sigma0 * bloch_projector(direction)))
    runner.check(
        "T1a",
        "sigma0 gives Tr(sigma0 P(n))=(2+nz)/4 symbolically",
        projector_trace == (2 + nz) / 4,
    )

    ea, ed, ex, ey = sp.symbols("ea ed ex ey", real=True)
    symbolic_effect = sp.Matrix(
        [[ea, ex - sp.I * ey], [ex + sp.I * ey, ed]]
    )
    trace_effect = sp.simplify(sp.trace(sigma0 * symbolic_effect))
    trace_complement = sp.simplify(sp.trace(sigma0 * (I2 - symbolic_effect)))
    runner.check(
        "T1b-trace",
        "a symbolic Hermitian effect and its complement have complementary traces",
        matrix_is_zero(symbolic_effect - symbolic_effect.H)
        and sp.trace(sigma0) == 1
        and sp.simplify(trace_complement - (1 - trace_effect)) == 0,
    )
    runner.check(
        "T1b-compose",
        "the f-complement law formally composes with the trace complement",
        sp.factor(witness_f(trace_effect) + witness_f(trace_complement) - 1) == 0,
    )

    endpoint_zero = witness_f(projector_trace.subs(nz, 0))
    endpoint_one = witness_f(projector_trace.subs(nz, 1))
    affine_midpoint_prediction = sp.simplify((endpoint_zero + endpoint_one) / 2)
    actual_midpoint = witness_f(projector_trace.subs(nz, sp.Rational(1, 2)))
    runner.check(
        "T1c-values",
        "the endpoint values predict 41/56 while the midpoint is 125/152",
        endpoint_zero == sp.Rational(1, 2)
        and endpoint_one == sp.Rational(27, 28)
        and affine_midpoint_prediction == sp.Rational(41, 56)
        and actual_midpoint == sp.Rational(125, 152),
    )
    runner.check(
        "T1c-cross-product",
        "exact cross multiplication detects the three-point non-affinity",
        41 * 152 != 125 * 56
        and sp.simplify(affine_midpoint_prediction - actual_midpoint) != 0,
    )

    ternary_menu = (
        sp.Rational(1, 4) * I2,
        sp.Rational(1, 4) * I2,
        sp.Rational(1, 2) * I2,
    )
    ternary_witness_values = tuple(
        witness_f(sp.trace(sigma0 * effect)) for effect in ternary_menu
    )
    runner.check(
        "T1d",
        "the exact ternary menu sums to I but the witness weights sum to 4/7",
        matrix_is_zero(sum(ternary_menu, sp.zeros(2)) - I2)
        and ternary_witness_values
        == (sp.Rational(1, 28), sp.Rational(1, 28), sp.Rational(1, 2))
        and sum(ternary_witness_values) == sp.Rational(4, 7)
        and normalization_violation(ternary_witness_values),
    )

    affine_binary_values = (
        trace_effect,
        trace_complement,
    )
    affine_ternary_values = tuple(sp.trace(sigma0 * effect) for effect in ternary_menu)
    runner.check(
        "T1e-control",
        "the affine trace control passes binary and ternary normalization without a flag",
        not normalization_violation(affine_binary_values)
        and not normalization_violation(affine_ternary_values)
        and sum(affine_ternary_values) == 1,
    )

    # Group T2 - the ternary threshold
    w1, w2, w12, w_remainder = sp.symbols(
        "w1 w2 w12 w_remainder", real=True
    )
    additivity_solution = sp.solve(
        [
            sp.Eq(w1 + w2 + w_remainder, 1),
            sp.Eq(w12 + w_remainder, 1),
        ],
        (w12, w_remainder),
        dict=True,
    )
    runner.check(
        "T2a",
        "TERNARY MENU IS THE ONLY NEW INPUT: it and the binary regrouping eliminate to additivity",
        len(additivity_solution) == 1
        and sp.simplify(additivity_solution[0][w12] - w1 - w2) == 0,
    )

    e_z = (sp.Integer(0), sp.Integer(0), sp.Integer(1))
    e_x = (sp.Integer(1), sp.Integer(0), sp.Integer(0))
    effect1 = sp.Rational(1, 4) * bloch_projector(e_z)
    effect2 = sp.Rational(1, 4) * bloch_projector(e_x)
    effect_sum = effect1 + effect2
    effect_remainder = I2 - effect_sum
    runner.check(
        "T2b-cone",
        "the rational noncommuting pair and its sum/remainder stay in the effect cone",
        is_effect(effect1)
        and is_effect(effect2)
        and is_effect(effect_sum)
        and is_effect(effect_remainder)
        and not matrix_is_zero(effect1 * effect2 - effect2 * effect1),
    )
    runner.check(
        "T2b-menus",
        "the noncommuting witness realizes the ternary and binary regrouped menus exactly",
        matrix_is_zero(effect1 + effect2 + effect_remainder - I2)
        and matrix_is_zero(effect_sum + effect_remainder - I2),
    )

    # Group T3 - mixed-projective forcing
    split_l, split_m, split_r = sp.symbols(
        "split_l split_m split_r", positive=True
    )
    minus_direction = tuple(-component for component in direction)
    split_menu_sum = (
        split_l * bloch_projector(direction)
        + split_m * bloch_projector(direction)
        + split_r * bloch_projector(direction)
        + bloch_projector(minus_direction)
    )
    runner.check(
        "T3a",
        "one component with a split plus outcome gives the symbolic split menu",
        matrix_is_zero(
            split_menu_sum.subs(split_r, 1 - split_l - split_m) - I2
        )
        and sp.simplify(
            (split_l + split_m + split_r).subs(
                split_r, 1 - split_l - split_m
            )
            - 1
        )
        == 0,
    )

    a1, a2 = sp.symbols("a1 a2", real=True)
    g1, g2, w_a = sp.symbols("g1 g2 w_a", real=True)
    merge2_equation = sp.Eq(
        w_a + a1 * (1 - g1) + a2 * (1 - g2) + (1 - a1 - a2),
        1,
    )
    merge2_solution = sp.solve([merge2_equation], w_a, dict=True)
    n1_symbols = sp.symbols("n1x n1y n1z", real=True)
    n2_symbols = sp.symbols("n2x n2y n2z", real=True)
    merge2_element = (
        a1 * bloch_projector(n1_symbols)
        + a2 * bloch_projector(n2_symbols)
    )
    merge2_presentation_sum = (
        merge2_element
        + a1 * bloch_projector(tuple(-entry for entry in n1_symbols))
        + a2 * bloch_projector(tuple(-entry for entry in n2_symbols))
        + (1 - a1 - a2) * I2
    )
    runner.check(
        "T3b-two-direction",
        "the two-direction merge presentation normalizes and eliminates to its matching sum",
        matrix_is_zero(merge2_presentation_sum - I2)
        and len(merge2_solution) == 1
        and sp.simplify(merge2_solution[0][w_a] - a1 * g1 - a2 * g2)
        == 0,
    )

    a3, g3 = sp.symbols("a3 g3", real=True)
    merge3_equation = sp.Eq(
        w_a
        + a1 * (1 - g1)
        + a2 * (1 - g2)
        + a3 * (1 - g3)
        + (1 - a1 - a2 - a3),
        1,
    )
    merge3_solution = sp.solve([merge3_equation], w_a, dict=True)
    n3_symbols = sp.symbols("n3x n3y n3z", real=True)
    merge3_presentation_sum = merge2_presentation_sum - (1 - a1 - a2) * I2
    merge3_presentation_sum += (
        a3 * bloch_projector(n3_symbols)
        + a3 * bloch_projector(tuple(-entry for entry in n3_symbols))
        + (1 - a1 - a2 - a3) * I2
    )
    runner.check(
        "T3b-three-direction",
        "the three-direction merge presentation obeys the same finite-family lemma",
        matrix_is_zero(merge3_presentation_sum - I2)
        and len(merge3_solution) == 1
        and sp.simplify(
            merge3_solution[0][w_a] - a1 * g1 - a2 * g2 - a3 * g3
        )
        == 0,
    )

    px, py, pz = sp.symbols("px py pz", positive=True)
    positive_direction = (px, py, pz)
    positive_length = px + py + pz
    positive_c0 = sp.simplify(2 / (1 + positive_length))
    positive_halved_axis = (
        positive_c0 * bloch_projector(positive_direction) / 2
        + positive_c0 * px * bloch_projector((-1, 0, 0)) / 2
        + positive_c0 * py * bloch_projector((0, -1, 0)) / 2
        + positive_c0 * pz * bloch_projector((0, 0, -1)) / 2
    )
    positive_projector_ok = all(
        unit_sphere_zero(entry, positive_direction)
        for entry in (
            bloch_projector(positive_direction) ** 2
            - bloch_projector(positive_direction)
        )
    )
    runner.check(
        "T3c-axis-symbolic",
        "the positive-octant halved axis decomposition equals I/2 with mass one",
        positive_projector_ok
        and matrix_is_zero(positive_halved_axis - I2 / 2)
        and sp.simplify(positive_c0 * (1 + positive_length) / 2 - 1)
        == 0,
    )

    mx, my, mz = sp.symbols("mx my mz", real=True)
    m_direction = (mx, my, mz)
    symbolic_antipodal_half = (
        bloch_projector(m_direction) / 2
        + bloch_projector(tuple(-entry for entry in m_direction)) / 2
    )
    symbolic_m_projector_ok = all(
        unit_sphere_zero(entry, m_direction)
        for entry in bloch_projector(m_direction) ** 2 - bloch_projector(m_direction)
    )
    runner.check(
        "T3c-antipodal-symbolic",
        "the symbolic antipodal decomposition equals I/2 with mass one",
        symbolic_m_projector_ok
        and matrix_is_zero(symbolic_antipodal_half - I2 / 2)
        and sp.Rational(1, 2) + sp.Rational(1, 2) == 1,
    )

    other_octant_direction = (
        sp.Rational(3, 7), -sp.Rational(6, 7), sp.Rational(2, 7)
    )
    other_octant_menu = axis_cancellation_menu(other_octant_direction)
    other_octant_halved = tuple(item / 2 for item in other_octant_menu)
    runner.check(
        "T3c-axis-octant",
        "an exact mixed-sign rational axis decomposition equals I/2 with mass one",
        sp.simplify(
            sum(component**2 for component in other_octant_direction) - 1
        )
        == 0
        and all(is_effect(item) for item in other_octant_halved)
        and matrix_is_zero(sum(other_octant_halved, sp.zeros(2)) - I2 / 2)
        and sp.simplify(
            sum(sp.trace(item) for item in other_octant_halved) - 1
        )
        == 0,
    )

    rational_m = (sp.Rational(3, 5), sp.Integer(0), sp.Rational(4, 5))
    rational_antipodal_half = (
        bloch_projector(rational_m) / 2
        + bloch_projector(tuple(-entry for entry in rational_m)) / 2
    )
    runner.check(
        "T3c-antipodal-witness",
        "the rational antipodal comparison is the same I/2 with mass one",
        sp.simplify(sum(component**2 for component in rational_m) - 1) == 0
        and matrix_is_zero(rational_antipodal_half - I2 / 2)
        and sp.simplify(sp.trace(rational_antipodal_half) - 1) == 0,
    )

    g_n, g_xp, g_xm, g_yp, g_ym, g_zp, g_zm = sp.symbols(
        "g_n g_xp g_xm g_yp g_ym g_zp g_zm", real=True
    )
    positive_affinity_solution = sp.solve(
        [
            sp.Eq(g_xp + g_xm, 1),
            sp.Eq(g_yp + g_ym, 1),
            sp.Eq(g_zp + g_zm, 1),
            sp.Eq(
                positive_c0 * g_n / 2
                + positive_c0 * px * g_xm / 2
                + positive_c0 * py * g_ym / 2
                + positive_c0 * pz * g_zm / 2,
                sp.Rational(1, 2),
            ),
        ],
        (g_n, g_xm, g_ym, g_zm),
        dict=True,
    )
    s_axes = (2 * g_xp - 1, 2 * g_yp - 1, 2 * g_zp - 1)
    positive_affine_target = sp.simplify(
        (
            1
            + sum(
                component * s_axis
                for component, s_axis in zip(positive_direction, s_axes)
            )
        )
        / 2
    )
    runner.check(
        "T3d-positive",
        "the merge equation and complements eliminate to positive-octant affinity",
        len(positive_affinity_solution) == 1
        and sp.simplify(
            positive_affinity_solution[0][g_n] - positive_affine_target
        )
        == 0,
    )

    axis_values = ((g_xp, g_xm), (g_yp, g_ym), (g_zp, g_zm))
    complement_substitutions = {
        g_xm: 1 - g_xp,
        g_ym: 1 - g_yp,
        g_zm: 1 - g_zp,
    }
    other_length = sp.simplify(
        sum(abs(component) for component in other_octant_direction)
    )
    other_c0 = sp.simplify(2 / (1 + other_length))
    other_affinity_left = other_c0 * g_n / 2
    for component, (positive_value, negative_value) in zip(
        other_octant_direction, axis_values
    ):
        if component.is_positive is True:
            opposite_value = negative_value
        elif component.is_negative is True:
            opposite_value = positive_value
        else:
            raise ValueError("rational witness has an undecidable component sign")
        other_affinity_left += other_c0 * abs(component) * opposite_value / 2
    other_affinity_solution = sp.solve(
        [
            sp.Eq(
                other_affinity_left.subs(complement_substitutions),
                sp.Rational(1, 2),
            )
        ],
        g_n,
        dict=True,
    )
    other_affine_target = sp.simplify(
        (
            1
            + sum(
                component * s_axis
                for component, s_axis in zip(other_octant_direction, s_axes)
            )
        )
        / 2
    )
    runner.check(
        "T3d-other-octant",
        "explicit sign branches give the same affinity in a mixed-sign octant",
        len(other_affinity_solution) == 1
        and sp.simplify(other_affinity_solution[0][g_n] - other_affine_target)
        == 0,
    )

    s_x, s_y, s_z = sp.symbols("s_x s_y s_z", real=True)
    sigma = (I2 + s_x * sx + s_y * sy + s_z * sz) / 2
    merged_trace = sp.simplify(sp.trace(sigma * merge2_element))
    merged_target = sp.simplify(
        a1
        * (
            1
            + n1_symbols[0] * s_x
            + n1_symbols[1] * s_y
            + n1_symbols[2] * s_z
        )
        / 2
        + a2
        * (
            1
            + n2_symbols[0] * s_x
            + n2_symbols[1] * s_y
            + n2_symbols[2] * s_z
        )
        / 2
    )
    runner.check(
        "T3e",
        "the trace form on a merged element is the matching sum of affine values",
        sp.simplify(merged_trace - merged_target) == 0,
    )

    rho_a, rho_d, rho_x, rho_y = sp.symbols(
        "rho_a rho_d rho_x rho_y", real=True
    )
    generic_state = sp.Matrix(
        [[rho_a, rho_x - sp.I * rho_y], [rho_x + sp.I * rho_y, rho_d]]
    )
    coin_trace_value = sp.simplify(
        sp.trace(generic_state * sp.Rational(1, 4) * I2).subs(
            rho_d, 1 - rho_a
        )
    )
    runner.check(
        "T1f-coin-refutation",
        "every normalized trace form gives 1/4 on the quarter coin while the witness gives 1/28",
        coin_trace_value == sp.Rational(1, 4)
        and witness_f(sp.Rational(1, 4)) == sp.Rational(1, 28)
        and sp.Rational(1, 28) != sp.Rational(1, 4),
    )

    finite_dimension = sp.symbols("finite_dimension", integer=True, positive=True)
    uniform_state_entry = 1 / finite_dimension
    quarter_coin_trace_all_d = sp.simplify(
        finite_dimension * uniform_state_entry * sp.Rational(1, 4)
    )
    quarter_coin_complement_trace_all_d = sp.simplify(
        finite_dimension * uniform_state_entry * sp.Rational(3, 4)
    )
    runner.check(
        "T1g-all-finite-d",
        "the normalized uniform-state schema gives the same binary witness and coin refutation in arbitrary finite dimension",
        quarter_coin_trace_all_d == sp.Rational(1, 4)
        and quarter_coin_complement_trace_all_d == sp.Rational(3, 4)
        and witness_f(quarter_coin_trace_all_d)
        + witness_f(quarter_coin_complement_trace_all_d)
        == 1
        and witness_f(quarter_coin_trace_all_d) == sp.Rational(1, 28)
        and quarter_coin_trace_all_d != witness_f(quarter_coin_trace_all_d),
    )

    heavy_a, heavy_b = sp.Rational(4, 5), sp.Rational(3, 5)
    heavy_element = heavy_a * bloch_projector(e_z) + heavy_b * bloch_projector(
        tuple(-entry for entry in e_z)
    )
    heavy_menu = (
        heavy_element,
        (1 - heavy_a) * bloch_projector(e_z),
        (1 - heavy_b) * bloch_projector(tuple(-entry for entry in e_z)),
    )
    g_heavy, w_heavy = sp.symbols("g_heavy w_heavy", real=True)
    heavy_solution = sp.solve(
        [
            sp.Eq(
                w_heavy
                + (1 - heavy_a) * g_heavy
                + (1 - heavy_b) * (1 - g_heavy),
                1,
            )
        ],
        w_heavy,
        dict=True,
    )
    heavy_matching_sum = sp.simplify(
        heavy_a * g_heavy + heavy_b * (1 - g_heavy)
    )
    s_z_only = sp.symbols("s_z_only", real=True)
    sigma_z_only = (I2 + s_z_only * sz) / 2
    heavy_trace = sp.simplify(sp.trace(sigma_z_only * heavy_element))
    heavy_affine = sp.simplify(
        heavy_a * (1 + s_z_only) / 2 + heavy_b * (1 - s_z_only) / 2
    )
    runner.check(
        "T3f-heavy-element",
        "a trace-exceeding-one merged element takes its matching sum by the separate-outcomes route",
        sp.simplify(sp.trace(heavy_element) - sp.Rational(7, 5)) == 0
        and matrix_is_zero(sum(heavy_menu, sp.zeros(2)) - I2)
        and len(heavy_solution) == 1
        and sp.simplify(heavy_solution[0][w_heavy] - heavy_matching_sum) == 0
        and sp.simplify(
            heavy_matching_sum.subs(g_heavy, (1 + s_z_only) / 2)
            - heavy_trace
        )
        == 0
        and sp.simplify(heavy_trace - heavy_affine) == 0,
    )

    # Group T4 - incomparability
    merged_element = (
        sp.Rational(1, 2) * bloch_projector(e_z)
        + sp.Rational(1, 2) * bloch_projector(e_x)
    )
    merged_eigenvalues = exact_eigenvalue_multiset(merged_element)
    expected_merged_eigenvalues = (
        (2 - sp.sqrt(2)) / 4,
        (2 + sp.sqrt(2)) / 4,
    )
    runner.check(
        "T4a-spectrum",
        "the merged two-direction element has the two exact distinct nonzero eigenvalues",
        same_multiset(merged_eigenvalues, expected_merged_eigenvalues)
        and all(value.is_positive is True for value in merged_eigenvalues)
        and sp.simplify(merged_eigenvalues[0] - merged_eigenvalues[1]) != 0,
    )
    runner.check(
        "T4a-membership",
        "the merged spectrum matches neither a rank-one scaled ray nor an identity ray",
        scaled_projector_parameters(merged_element) is None
        and not same_multiset(
            merged_eigenvalues, (sp.Integer(0), sp.trace(merged_element))
        )
        and not same_multiset(
            merged_eigenvalues,
            (sp.trace(merged_element) / 2, sp.trace(merged_element) / 2),
        ),
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
        "T4b-menu",
        "the exact coplanar scaled-projector menu sums to identity",
        all(
            sp.simplify(sum(component**2 for component in item_direction) - 1)
            == 0
            for item_direction in coplanar_directions
        )
        and valid_scaled_projector_menu(coplanar_menu),
    )
    coplanar_dots = tuple(
        sp.simplify(sum(x * y for x, y in zip(left, right)))
        for left_index, left in enumerate(coplanar_directions)
        for right in coplanar_directions[left_index + 1 :]
    )
    runner.check(
        "T4b-dots",
        "all coplanar directions have dot product minus one-half, never antipodal",
        coplanar_dots
        == (
            -sp.Rational(1, 2),
            -sp.Rational(1, 2),
            -sp.Rational(1, 2),
        )
        and all(dot != -1 for dot in coplanar_dots),
    )

    nonparallel_direction = (
        sp.Rational(4, 5), sp.Integer(0), sp.Rational(3, 5)
    )
    rank_one_piece_difference = (
        bloch_projector(e_z)
        - sp.Rational(1, 2) * bloch_projector(nonparallel_direction)
    )
    rank_one_piece_eigenvalues = exact_eigenvalue_multiset(
        rank_one_piece_difference
    )
    runner.check(
        "T4c-projector-piece",
        "an exact nonparallel positive projector piece creates a negative eigenvalue",
        sp.simplify(sum(component**2 for component in nonparallel_direction) - 1)
        == 0
        and sum(x * y for x, y in zip(e_z, nonparallel_direction))
        == sp.Rational(3, 5)
        and same_multiset(
            rank_one_piece_eigenvalues,
            ((5 - sp.sqrt(65)) / 20, (5 + sp.sqrt(65)) / 20),
        )
        and any(value.is_negative is True for value in rank_one_piece_eigenvalues),
    )

    target_scale, piece_scale, direction_dot = sp.symbols(
        "target_scale piece_scale direction_dot", positive=True
    )
    support_difference_determinant = sp.expand(
        ((target_scale - piece_scale) / 2) ** 2
        - (
            target_scale**2
            + piece_scale**2
            - 2 * target_scale * piece_scale * direction_dot
        )
        / 4
    )
    runner.check(
        "T4c-support-determinant",
        "the general rank-one support determinant is -c*p*(1-n dot m)/2",
        sp.factor(
            support_difference_determinant
            + target_scale * piece_scale * (1 - direction_dot) / 2
        )
        == 0,
    )

    positive_piece = sp.symbols("positive_piece", positive=True)
    identity_piece_difference = bloch_projector(e_z) - positive_piece * I2
    identity_piece_eigenvalues = exact_eigenvalue_multiset(
        identity_piece_difference
    )
    runner.check(
        "T4c-identity-piece",
        "every positive identity piece leaves a negative eigenvalue below a rank-one projector",
        same_multiset(
            identity_piece_eigenvalues,
            (-positive_piece, 1 - positive_piece),
        )
        and (-positive_piece).is_negative is True,
    )

    coin_into_rank_one = (
        sp.Rational(2, 3) * bloch_projector(coplanar_directions[0])
        - sp.Rational(1, 10) * I2
    )
    runner.check(
        "T4d",
        "the exact coplanar rank-one element cannot receive a positive coin piece",
        same_multiset(
            exact_eigenvalue_multiset(coin_into_rank_one),
            (-sp.Rational(1, 10), sp.Rational(17, 30)),
        )
        and any(
            value.is_negative is True
            for value in exact_eigenvalue_multiset(coin_into_rank_one)
        ),
    )

    # Group T5 - binary menus within the scaled family
    scaled_c = sp.symbols("scaled_c", real=True)
    spectral_parameter = sp.symbols("spectral_parameter", real=True)
    scaled_complement = I2 - scaled_c * bloch_projector(direction)
    scaled_complement_characteristic = sp.det(
        spectral_parameter * I2 - scaled_complement
    )
    scaled_complement_target = (
        spectral_parameter - (1 - scaled_c)
    ) * (spectral_parameter - 1)
    runner.check(
        "T5a-spectrum",
        "I-cP(n) has the symbolic eigenvalue multiset {1-c,1}",
        all(
            unit_sphere_zero(entry, direction)
            for entry in bloch_projector(direction) ** 2
            - bloch_projector(direction)
        )
        and unit_sphere_zero(
            scaled_complement_characteristic - scaled_complement_target,
            direction,
        ),
    )

    scaled_prime = sp.symbols("scaled_prime", real=True)
    rank_one_direct_solution = sp.solve(
        [sp.Eq(1 - scaled_c, 0), sp.Eq(1, scaled_prime)],
        (scaled_c, scaled_prime),
        dict=True,
    )
    rank_one_crossed_solution = sp.solve(
        [sp.Eq(1 - scaled_c, scaled_prime), sp.Eq(1, 0)],
        (scaled_c, scaled_prime),
        dict=True,
    )
    runner.check(
        "T5a-rank-one-match",
        "solve-based matching to {c-prime,0} forces c=1",
        rank_one_direct_solution == [{scaled_c: 1, scaled_prime: 1}]
        and rank_one_crossed_solution == [],
    )

    identity_match_solution = sp.solve(
        [sp.Eq(1 - scaled_c, scaled_prime), sp.Eq(1, scaled_prime)],
        (scaled_c, scaled_prime),
        dict=True,
    )
    runner.check(
        "T5a-identity-match",
        "solve-based matching to {c-prime,c-prime} only gives c=0, outside (0,1)",
        identity_match_solution == [{scaled_c: 0, scaled_prime: 1}]
        and not (sp.Integer(0) < identity_match_solution[0][scaled_c] < 1),
    )

    coin_variable = sp.symbols("coin_variable", real=True)
    rational_coin = sp.Rational(2, 5)
    rational_coin_complement = I2 - rational_coin * I2
    runner.check(
        "T5b",
        "coin complements stay on the identity ray and pass the scaled-family test",
        matrix_is_zero(
            I2 - coin_variable * I2 - (1 - coin_variable) * I2
        )
        and nonnegative_between(1 - coin_variable, coin_variable, 0, 1)
        and scaled_projector_parameters(rational_coin_complement)
        == ("identity", 1 - rational_coin, None),
    )

    smooth_direction_z = sp.symbols("smooth_direction_z", real=True)
    smooth_scaled_rogue = (1 + smooth_direction_z**3) / 2
    runner.check(
        "T5c-smooth-rogue",
        "the smooth cubic directional grading obeys complements but contradicts its axis-fitted trace candidate",
        sp.factor(
            smooth_scaled_rogue
            + smooth_scaled_rogue.subs(smooth_direction_z, -smooth_direction_z)
            - 1
        )
        == 0
        and smooth_scaled_rogue.subs(smooth_direction_z, 1) == 1
        and smooth_scaled_rogue.subs(smooth_direction_z, 0) == sp.Rational(1, 2)
        and smooth_scaled_rogue.subs(
            smooth_direction_z, sp.Rational(1, 2)
        )
        == sp.Rational(9, 16)
        and sp.Rational(9, 16) != sp.Rational(3, 4),
    )

    # Group N - normalized-whitespace document needles
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    scaled_parent_text = SCALED_PARENT_PATH.read_text(encoding="utf-8")
    effect_parent_text = EFFECT_PARENT_PATH.read_text(encoding="utf-8")
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8")
    note_normalized = normalize(note_text)
    scaled_parent_normalized = normalize(scaled_parent_text)
    effect_parent_normalized = normalize(effect_parent_text)
    axiom_normalized = normalize(axiom_text)

    runner.check(
        "N1",
        "the axiom memo pins readable values to record content alone",
        "Only records are readable. A readout value is determined by record content alone."
        in axiom_normalized,
    )
    runner.check(
        "N2",
        "the effect-grade parent pins its current dimension-generic finite-effect theorem",
        "This proof is dimension-generic and imports no representation theorem."
        in effect_parent_normalized,
    )
    runner.check(
        "N3",
        "the scaled-projector parent states the paired-subfamily boundary",
        "The paired subfamily does not force" in scaled_parent_normalized,
    )
    runner.check(
        "N4-claim",
        "the source note pins its exact claim identifier",
        "claim_id: born_form_menu_outcome_threshold_and_mixed_projective_forcing_bounded_theorem_note_2026-07-17"
        in note_text,
    )
    runner.check(
        "N4-labels",
        "the source note uses scientific names for all three conditional menu surfaces and narrows the scaled claim",
        "**Binary effect-partition normalization.**" in note_text
        and "**Ternary effect-partition normalization.**" in note_text
        and "**Finite mixed-projective partition normalization.**" in note_text
        and "No ternary scaled-projector sufficiency or exact scaled outcome-count threshold is proved here."
        in note_normalized,
    )
    runner.check(
        "N4-threshold",
        "the source note states the exact three-outcome threshold",
        "exact maximum-arity threshold is three" in note_normalized,
    )

    failures = runner.total()
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
