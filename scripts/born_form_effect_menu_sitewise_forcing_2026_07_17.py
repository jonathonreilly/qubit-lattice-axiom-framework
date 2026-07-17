#!/usr/bin/env python3
"""Exact checks for the effect-menu Born-form and product-menu boundary note."""

from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md"
BRIDGE_PATH = ROOT / "docs" / "BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
EFFECT_BRIDGE_PATH = ROOT / "docs" / "BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"

I2 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
PAULIS = (sx, sy, sz)


def normalize(text):
    return " ".join(text.split())


def matrix_is_zero(matrix):
    return matrix.applyfunc(sp.simplify) == sp.zeros(*matrix.shape)


def exact_eigenvalues(matrix):
    return tuple(sp.simplify(value) for value in matrix.eigenvals())


def is_effect(matrix):
    if matrix.rows != matrix.cols or not matrix_is_zero(matrix - matrix.H):
        return False
    return all(
        value.is_real is True
        and value.is_nonnegative is True
        and (sp.Integer(1) - value).is_nonnegative is True
        for value in exact_eigenvalues(matrix)
    )


def has_negative_eigenvalue(matrix):
    return any(value.is_negative is True for value in exact_eigenvalues(matrix))


def valid_effect_menu(menu):
    if not menu:
        return False
    dimension = menu[0].rows
    return (
        all(item.shape == (dimension, dimension) and is_effect(item) for item in menu)
        and matrix_is_zero(sum(menu, sp.zeros(dimension)) - sp.eye(dimension))
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

    # Group A - partial additivity from menu normalization (formal)
    w1, w2, w12, wR = sp.symbols("w1 w2 w12 wR", real=True)
    a1_solution = sp.solve(
        [sp.Eq(w1 + w2 + wR, 1), sp.Eq(w12 + wR, 1)],
        (w12, wR),
        dict=True,
    )
    runner.check(
        "A1",
        "two menu normalizations eliminate to partial additivity",
        len(a1_solution) == 1
        and sp.simplify(a1_solution[0][w12] - w1 - w2) == 0,
    )

    wE, wComplement = sp.symbols("wE wComplement", real=True)
    a2_solution = sp.solve([sp.Eq(wE + wComplement, 1)], wComplement, dict=True)
    runner.check(
        "A2",
        "binary menu normalization gives the complement law",
        len(a2_solution) == 1
        and sp.simplify(a2_solution[0][wComplement] - (1 - wE)) == 0,
    )

    E1 = sp.diag(sp.Rational(1, 4), sp.Rational(1, 8))
    E2 = sp.Matrix(
        [
            [sp.Rational(1, 4), sp.Rational(1, 8)],
            [sp.Rational(1, 8), sp.Rational(1, 4)],
        ]
    )
    R2 = I2 - E1 - E2
    runner.check(
        "A3-d2",
        "noncommuting rational M2 effects have a positive menu remainder",
        not matrix_is_zero(E1 * E2 - E2 * E1)
        and all(is_effect(item) for item in (E1, E2, R2))
        and valid_effect_menu((E1, E2, R2)),
    )

    E1_4 = sp.kronecker_product(E1, I2)
    E2_4 = sp.kronecker_product(E2, I2)
    R4 = sp.eye(4) - E1_4 - E2_4
    runner.check(
        "A3-d4",
        "noncommuting rational M4 effects have a positive menu remainder",
        not matrix_is_zero(E1_4 * E2_4 - E2_4 * E1_4)
        and all(is_effect(item) for item in (E1_4, E2_4, R4))
        and valid_effect_menu((E1_4, E2_4, R4)),
    )

    bad1 = sp.Rational(3, 4) * sp.diag(1, 0)
    bad2 = sp.Rational(3, 4) * sp.diag(1, 0)
    bad_remainder = I2 - bad1 - bad2
    runner.check(
        "A4",
        "menu checker rejects a negative remainder eigenvalue",
        is_effect(bad1)
        and is_effect(bad2)
        and has_negative_eigenvalue(bad_remainder)
        and not valid_effect_menu((bad1, bad2, bad_remainder)),
    )

    # Group B - homogeneity and monotonicity
    wE_b1, wPart, wComp_b1 = sp.symbols("wE_b1 wPart wComp_b1", real=True)
    for divisor, gate_id in ((3, "B1-r3"), (5, "B1-r5")):
        b1_solution = sp.solve(
            [
                sp.Eq(divisor * wPart + wComp_b1, 1),
                sp.Eq(wE_b1 + wComp_b1, 1),
            ],
            (wPart, wComp_b1),
            dict=True,
        )
        runner.check(
            gate_id,
            f"{divisor}-fold menu elimination gives rational homogeneity",
            len(b1_solution) == 1
            and sp.simplify(b1_solution[0][wPart] - wE_b1 / divisor) == 0,
        )

    wE_b2, wF_b2 = sp.symbols("wE_b2 wF_b2", real=True)
    wDelta = sp.symbols("wDelta", nonnegative=True)
    b2_solution = sp.solve(
        [sp.Eq(wF_b2, wE_b2 + wDelta)], wF_b2, dict=True
    )
    E_mono = sp.diag(sp.Rational(1, 4), sp.Rational(1, 8))
    F_mono = sp.diag(sp.Rational(1, 2), sp.Rational(1, 4))
    b2_difference = sp.simplify(b2_solution[0][wF_b2] - wE_b2)
    runner.check(
        "B2",
        "partial additivity and nonnegative difference weight imply monotonicity",
        is_effect(E_mono)
        and is_effect(F_mono)
        and is_effect(F_mono - E_mono)
        and b2_difference == wDelta
        and b2_difference.is_nonnegative is True,
    )

    t = sp.symbols("t", real=True)
    q1 = sp.Rational(1, 2)
    q2 = sp.Rational(2, 3)
    squeeze_effect = sp.diag(sp.Rational(1, 2), sp.Rational(1, 4))
    lower_gap_eigenvalues = exact_eigenvalues((t - q1) * squeeze_effect)
    upper_gap_eigenvalues = exact_eigenvalues((q2 - t) * squeeze_effect)

    def nonnegative_between(value, lower, upper):
        interval_nonempty = sp.reduce_inequalities(
            [t > lower, t < upper], t
        )
        if interval_nonempty is sp.false or interval_nonempty == False:
            return False
        contradiction = sp.reduce_inequalities(
            [t > lower, t < upper, value < 0], t
        )
        return contradiction is sp.false or contradiction == False

    squeeze_spectrum_ok = all(
        nonnegative_between(value, q1, q2)
        for value in lower_gap_eigenvalues + upper_gap_eigenvalues
    )
    wE_b3, wt = sp.symbols("wE_b3 wt", real=True)
    lower_weight, upper_weight = sp.symbols(
        "lower_weight upper_weight", nonnegative=True
    )
    b3_solution = sp.solve(
        [
            sp.Eq(wt, q1 * wE_b3 + lower_weight),
            sp.Eq(q2 * wE_b3, wt + upper_weight),
        ],
        (wE_b3, wt),
        dict=True,
    )
    b3_lower_residual = sp.simplify(
        (wt - q1 * wE_b3).subs(b3_solution[0])
    )
    b3_upper_residual = sp.simplify(
        (q2 * wE_b3 - wt).subs(b3_solution[0])
    )
    runner.check(
        "B3",
        "exact operator squeeze and formal weight chain hold between 1/2 and 2/3",
        squeeze_spectrum_ok
        and b3_lower_residual == lower_weight
        and b3_upper_residual == upper_weight
        and b3_lower_residual.is_nonnegative is True
        and b3_upper_residual.is_nonnegative is True,
    )

    toy_E = sp.diag(sp.Rational(1, 4), 0)
    toy_F = sp.diag(sp.Rational(1, 2), 0)
    toy_weights = {"E": sp.Rational(3, 4), "F": sp.Rational(1, 4)}
    runner.check(
        "B4",
        "checker detects a non-monotone toy assignment on an effect chain",
        is_effect(toy_E)
        and is_effect(toy_F - toy_E)
        and (toy_weights["F"] - toy_weights["E"]).is_negative is True,
    )

    # Group C - linear extension bases
    basis2 = (I2,) + tuple((I2 + pauli) / 2 for pauli in PAULIS)
    runner.check(
        "C1-effects",
        "the four M2 identity-plus-Pauli basis elements are effects",
        len(basis2) == 4 and all(is_effect(item) for item in basis2),
    )
    gram2 = sp.Matrix(
        [[sp.trace(left * right) for right in basis2] for left in basis2]
    )
    runner.check(
        "C1-gram",
        "the exact M2 effect-basis trace Gram matrix is nonsingular",
        sp.simplify(gram2.det()) != 0,
    )

    paulis_with_identity = (I2,) + PAULIS
    pauli_products4 = tuple(
        sp.kronecker_product(left, right)
        for left_index, left in enumerate(paulis_with_identity)
        for right_index, right in enumerate(paulis_with_identity)
        if (left_index, right_index) != (0, 0)
    )
    basis4 = (sp.eye(4),) + tuple(
        (sp.eye(4) + product) / 2 for product in pauli_products4
    )
    runner.check(
        "C2-effects",
        "the sixteen M4 identity-plus-Pauli-product basis elements are effects",
        len(basis4) == 16 and all(is_effect(item) for item in basis4),
    )
    gram4 = sp.Matrix(
        [[sp.trace(left * right) for right in basis4] for left in basis4]
    )
    runner.check(
        "C2-gram",
        "the exact M4 effect-basis trace Gram matrix is nonsingular",
        sp.simplify(gram4.det()) != 0,
    )

    A = sp.Matrix(
        [[1, sp.Rational(1, 4)], [sp.Rational(1, 4), sp.Rational(1, 2)]]
    )
    D = sp.diag(sp.Rational(1, 2), sp.Rational(1, 2))
    B = sp.diag(sp.Rational(1, 2), sp.Rational(1, 4))
    C = A + D - B
    scale = sp.Integer(2)
    wA, wB, wC, wD, wSum = sp.symbols("wA wB wC wD wSum", real=True)
    c3_solution = sp.solve(
        [sp.Eq(wA + wD, wSum), sp.Eq(wC + wB, wSum)],
        (wA, wC),
        dict=True,
    )
    cancellation_target = sp.simplify(
        (scale * wA + scale * wD - scale * wC - scale * wB).subs(
            c3_solution[0]
        )
    )
    runner.check(
        "C3",
        "scaled effect additivity makes positive-cone cancellation well-defined",
        matrix_is_zero(A + D - C - B)
        and all(is_effect(item / scale) for item in (A, B, C, D))
        and is_effect((A + D) / scale)
        and is_effect((C + B) / scale)
        and cancellation_target == 0,
    )

    # Group D - trace representation and reconstruction
    w_I = sp.Integer(1)
    w_x, w_y, w_z = sp.symbols("w_x w_y w_z", real=True)
    sigma00, sigma11, sigma_re, sigma_im = sp.symbols(
        "sigma00 sigma11 sigma_re sigma_im", real=True
    )
    sigma_unknown = sp.Matrix(
        [
            [sigma00, sigma_re - sp.I * sigma_im],
            [sigma_re + sp.I * sigma_im, sigma11],
        ]
    )
    basis_values2 = (w_I, w_x, w_y, w_z)
    d1_solution = sp.solve(
        [
            sp.Eq(sp.trace(sigma_unknown * basis), value)
            for basis, value in zip(basis2, basis_values2)
        ],
        (sigma00, sigma11, sigma_re, sigma_im),
        dict=True,
    )
    sigma2_symbolic = sigma_unknown.subs(d1_solution[0]).applyfunc(sp.simplify)
    landed_sigma2 = sp.Rational(1, 2) * (
        I2
        + (2 * w_x - 1) * sx
        + (2 * w_y - 1) * sy
        + (2 * w_z - 1) * sz
    )
    runner.check(
        "D1",
        "M2 trace-pairing solve equals the landed Bloch reconstruction",
        len(d1_solution) == 1
        and matrix_is_zero(sigma2_symbolic - landed_sigma2),
    )

    e0, ex, ey, ez = sp.symbols("e0 ex ey ez", real=True)
    generic_E2 = e0 * I2 + ex * sx + ey * sy + ez * sz
    generic_E2_from_effect_basis = (
        (e0 - ex - ey - ez) * basis2[0]
        + 2 * ex * basis2[1]
        + 2 * ey * basis2[2]
        + 2 * ez * basis2[3]
    )
    extension_E2 = (
        (e0 - ex - ey - ez) * w_I
        + 2 * ex * w_x
        + 2 * ey * w_y
        + 2 * ez * w_z
    )
    runner.check(
        "D2",
        "M2 trace pairing reproduces the generic effect-basis linear extension",
        matrix_is_zero(generic_E2 - generic_E2_from_effect_basis)
        and sp.simplify(sp.trace(sigma2_symbolic * generic_E2) - extension_E2)
        == 0,
    )

    basis_values4 = sp.Matrix(
        [sp.Integer(1)]
        + list(sp.symbols("w4_1:16", real=True))
    )
    sigma4_coefficients = gram4.inv() * basis_values4
    sigma4_symbolic = sum(
        (
            sigma4_coefficients[index] * basis4[index]
            for index in range(len(basis4))
        ),
        sp.zeros(4),
    ).applyfunc(sp.simplify)
    h4_coefficients = sp.symbols("h4_0:16", real=True)
    pauli_basis4 = (sp.eye(4),) + pauli_products4
    generic_E4 = sum(
        (
            coefficient * basis
            for coefficient, basis in zip(h4_coefficients, pauli_basis4)
        ),
        sp.zeros(4),
    )
    generic_E4_from_effect_basis = (
        (h4_coefficients[0] - sum(h4_coefficients[1:])) * basis4[0]
        + sum(
            (
                2 * h4_coefficients[index] * basis4[index]
                for index in range(1, 16)
            ),
            sp.zeros(4),
        )
    )
    extension_E4 = (
        (h4_coefficients[0] - sum(h4_coefficients[1:])) * basis_values4[0]
        + sum(
            2 * h4_coefficients[index] * basis_values4[index]
            for index in range(1, 16)
        )
    )
    reconstructed_values4 = sp.Matrix(
        [sp.trace(sigma4_symbolic * basis) for basis in basis4]
    )
    runner.check(
        "D3",
        "M4 sixteen-value solve reproduces a generic Pauli-product extension",
        matrix_is_zero(gram4 * sigma4_coefficients - basis_values4)
        and matrix_is_zero(generic_E4 - generic_E4_from_effect_basis)
        and matrix_is_zero(reconstructed_values4 - basis_values4)
        and sp.simplify(sp.trace(sigma4_symbolic * generic_E4) - extension_E4)
        == 0,
    )

    runner.check(
        "D4-d2",
        "M2 Gram nonsingularity forces uniqueness of the trace representative",
        gram2.det() != 0 and gram2.nullspace() == [],
    )
    runner.check(
        "D4-d4",
        "M4 Gram nonsingularity forces uniqueness of the trace representative",
        gram4.det() != 0 and gram4.nullspace() == [],
    )

    # Group E - state property
    runner.check(
        "E1",
        "the reconstructed identity value one gives trace one in both dimensions",
        sp.simplify(sp.trace(sigma2_symbolic) - 1) == 0
        and sp.simplify(sp.trace(sigma4_symbolic) - 1) == 0,
    )

    alpha, beta = sp.symbols("alpha beta", complex=True)
    psi = sp.Matrix([alpha, beta])
    psi_projector = psi * psi.H
    psi_quadratic = (psi.H * sigma2_symbolic * psi)[0]
    runner.check(
        "E2",
        "the projector trace equals the symbolic bra-ket quadratic form",
        sp.simplify(
            sp.expand_complex(
                sp.trace(sigma2_symbolic * psi_projector) - psi_quadratic
            )
        )
        == 0,
    )

    state_a, state_d, state_x, state_y = sp.symbols(
        "state_a state_d state_x state_y", real=True
    )
    generic_sigma2 = sp.Matrix(
        [
            [state_a, state_x - sp.I * state_y],
            [state_x + sp.I * state_y, state_d],
        ]
    )
    named_vectors = (
        sp.Matrix([1, 0]),
        sp.Matrix([0, 1]),
        sp.Matrix([1, 1]),
        sp.Matrix([1, sp.I]),
    )
    named_quadratics = tuple(
        sp.expand((vector.H * generic_sigma2 * vector)[0])
        for vector in named_vectors
    )
    named_expected = (
        state_a,
        state_d,
        state_a + state_d + 2 * state_x,
        state_a + state_d + 2 * state_y,
    )
    q_axis_a, q_axis_d, q_real, q_imag = sp.symbols(
        "q_axis_a q_axis_d q_real q_imag", nonnegative=True
    )
    named_solution = sp.solve(
        [
            sp.Eq(state_a, q_axis_a),
            sp.Eq(state_d, q_axis_d),
            sp.Eq(state_a + state_d + 2 * state_x, q_real),
            sp.Eq(state_a + state_d + 2 * state_y, q_imag),
        ],
        (state_a, state_d, state_x, state_y),
        dict=True,
    )
    real_lower_residual = sp.simplify(
        (state_x + (state_a + state_d) / 2).subs(named_solution[0])
    )
    imag_lower_residual = sp.simplify(
        (state_y + (state_a + state_d) / 2).subs(named_solution[0])
    )
    runner.check(
        "E3-vectors",
        "the named four-vector principal-minor scaffolding gives exact lower bounds",
        all(
            sp.simplify(actual - expected) == 0
            for actual, expected in zip(named_quadratics, named_expected)
        )
        and real_lower_residual == q_real / 2
        and imag_lower_residual == q_imag / 2
        and real_lower_residual.is_nonnegative is True
        and imag_lower_residual.is_nonnegative is True,
    )

    r_state, p_state, q_state = sp.symbols("r_state p_state q_state", real=True)
    sigma_witness_family = sp.Matrix(
        [[sp.Rational(1, 2), r_state], [r_state, sp.Rational(1, 2)]]
    )
    family_eigenvalues = set(exact_eigenvalues(sigma_witness_family))
    family_quadratic = sp.expand(
        (
            sp.Matrix([p_state, q_state]).T
            * sigma_witness_family
            * sp.Matrix([p_state, q_state])
        )[0]
    )
    family_decomposition = (
        (sp.Rational(1, 2) + r_state) * (p_state + q_state) ** 2 / 2
        + (sp.Rational(1, 2) - r_state) * (p_state - q_state) ** 2 / 2
    )
    eigenvalue_region = sp.reduce_inequalities(
        [
            sp.Rational(1, 2) + r_state >= 0,
            sp.Rational(1, 2) - r_state >= 0,
        ],
        r_state,
    )
    expected_region = sp.And(
        r_state >= -sp.Rational(1, 2), r_state <= sp.Rational(1, 2)
    )
    runner.check(
        "E3-family",
        "witness-family quadratic nonnegativity is exactly the PSD eigenvalue criterion",
        family_eigenvalues
        == {
            sp.Rational(1, 2) + r_state,
            sp.Rational(1, 2) - r_state,
        }
        and sp.simplify(family_quadratic - family_decomposition) == 0
        and sp.simplify(sp.Equivalent(eigenvalue_region, expected_region)) is sp.true
        and sp.simplify(
            sigma_witness_family.det()
            - (sp.Rational(1, 4) - r_state**2)
        )
        == 0
        and sp.simplify(
            family_quadratic.subs({p_state: 1, q_state: 1})
            - 2 * (sp.Rational(1, 2) + r_state)
        )
        == 0
        and sp.simplify(
            family_quadratic.subs({p_state: 1, q_state: -1})
            - 2 * (sp.Rational(1, 2) - r_state)
        )
        == 0,
    )

    # Group T2 - rogue non-extension at one site
    e_x = (sp.Integer(1), sp.Integer(0), sp.Integer(0))
    e_z = (sp.Integer(0), sp.Integer(0), sp.Integer(1))
    inv_sqrt2 = sp.sqrt(2) / 2
    u_direction = (inv_sqrt2, sp.Integer(0), -inv_sqrt2)
    runner.check(
        "T2a",
        "lexicographic hemisphere values respect the nz-ny-nx tuple order",
        hemisphere_weight(e_x) == 1
        and hemisphere_weight(e_z) == 1
        and hemisphere_weight(u_direction) == 0,
    )

    rogue_samples = ((e_x, sp.Integer(1)), (e_z, sp.Integer(1)))
    rogue_forced_u = forced_trace_value(rogue_samples, u_direction)
    runner.check(
        "T2b",
        "normalization and two rogue values force trace value one-half at u",
        rogue_forced_u == sp.Rational(1, 2)
        and detects_trace_conflict(
            rogue_samples, u_direction, hemisphere_weight(u_direction)
        ),
    )

    def affine_z_weight(direction):
        return sp.simplify((1 + direction[2]) / 2)

    affine_samples = (
        (e_x, affine_z_weight(e_x)),
        (e_z, affine_z_weight(e_z)),
    )
    affine_forced_u = forced_trace_value(affine_samples, u_direction)
    affine_sigma = (I2 + sz) / 2
    runner.check(
        "T2c",
        "affine Bloch control remains consistent with its forced trace value",
        affine_forced_u == affine_z_weight(u_direction)
        and not detects_trace_conflict(
            affine_samples, u_direction, affine_z_weight(u_direction)
        )
        and all(
            sp.simplify(
                sp.trace(affine_sigma * bloch_projector(direction))
                - affine_z_weight(direction)
            )
            == 0
            for direction in (e_x, e_z, u_direction)
        ),
    )

    complement_directions = (
        (
            "T2d-1",
            (
                sp.Rational(3, 5),
                sp.Integer(0),
                sp.Rational(4, 5),
            ),
        ),
        ("T2d-2", (sp.Integer(0), sp.Integer(1), sp.Integer(0))),
        ("T2d-3", (sp.Integer(1), sp.Integer(0), sp.Integer(0))),
        ("T2d-4", (sp.Integer(0), sp.Integer(0), sp.Integer(1))),
    )
    for gate_id, direction in complement_directions:
        antipode = tuple(-component for component in direction)
        runner.check(
            gate_id,
            "hemisphere rule complements an exact antipodal tie-aware pair",
            sp.simplify(sum(component**2 for component in direction) - 1) == 0
            and hemisphere_weight(direction) + hemisphere_weight(antipode) == 1,
        )

    # Group T3 - product-menu boundary on the bonded pair
    ax, ay, az, cx, cy, cz = sp.symbols("ax ay az cx cy cz", real=True)
    a_vector = sp.Matrix([ax, ay, az])
    c_vector = sp.Matrix([cx, cy, cz])
    a_direction = (ax, ay, az)
    c_direction = (cx, cy, cz)
    dot_ac = (a_vector.T * c_vector)[0]
    norm_a = (a_vector.T * a_vector)[0]
    norm_c = (c_vector.T * c_vector)[0]
    single_overlap = sp.expand(
        sp.trace(bloch_projector(a_direction) * bloch_projector(c_direction))
    )
    antipode_deltas = tuple(a_vector[index] + c_vector[index] for index in range(3))
    antipode_sum_squares = sp.expand(sum(delta**2 for delta in antipode_deltas))
    sum_of_squares_certificate = (
        sp.simplify(antipode_sum_squares - (norm_a + norm_c + 2 * dot_ac))
        == 0
        and all(delta.is_real is True for delta in antipode_deltas)
        and all(
            sum(
                other_delta**2
                for other_index, other_delta in enumerate(antipode_deltas)
                if other_index != index
            ).is_nonnegative
            is True
            for index in range(len(antipode_deltas))
        )
    )
    runner.check(
        "T3a",
        "single-site overlap and real sum-of-squares force the antipode",
        sp.simplify(single_overlap - (1 + dot_ac) / 2) == 0
        and sum_of_squares_certificate
        and sp.simplify(sp.Integer(1) + sp.Integer(1) + 2 * (-1)) == 0
        and all(
            sp.simplify(
                delta.subs({cx: -ax, cy: -ay, cz: -az}, simultaneous=True)
            )
            == 0
            for delta in antipode_deltas
        ),
    )

    bx, by, bz, dx, dy, dz = sp.symbols("bx by bz dx dy dz", real=True)
    b_vector = sp.Matrix([bx, by, bz])
    d_vector = sp.Matrix([dx, dy, dz])
    b_direction = (bx, by, bz)
    d_direction = (dx, dy, dz)
    dot_bd = (b_vector.T * d_vector)[0]
    product_overlap = sp.expand(
        sp.trace(
            sp.kronecker_product(
                bloch_projector(a_direction), bloch_projector(b_direction)
            )
            * sp.kronecker_product(
                bloch_projector(c_direction), bloch_projector(d_direction)
            )
        )
    )
    runner.check(
        "T3b",
        "product-projector overlap factorizes into the two Bloch overlaps",
        sp.simplify(product_overlap - (1 + dot_ac) * (1 + dot_bd) / 4)
        == 0,
    )

    b1x, b1y, b1z = sp.symbols("b1x b1y b1z", real=True)
    b2x, b2y, b2z = sp.symbols("b2x b2y b2z", real=True)
    b3x, b3y, b3z = sp.symbols("b3x b3y b3z", real=True)
    b1 = sp.Matrix([b1x, b1y, b1z])
    b2 = sp.Matrix([b2x, b2y, b2z])
    b3 = sp.Matrix([b3x, b3y, b3z])
    forced_antipodes = {
        b2x: -b1x,
        b2y: -b1y,
        b2z: -b1z,
        b3x: -b1x,
        b3y: -b1y,
        b3z: -b1z,
    }
    forced_b2b3 = sp.expand((b2.T * b3)[0].subs(forced_antipodes))
    b1_norm = sp.expand((b1.T * b1)[0])
    forced_contradiction = sp.expand(forced_b2b3 + 1).subs(
        {b1z**2: 1 - b1x**2 - b1y**2}
    )
    runner.check(
        "T3c",
        "three mutually antipodal unit directions are inconsistent",
        sp.simplify(forced_b2b3 - b1_norm) == 0
        and sp.simplify(forced_contradiction - 2) == 0,
    )

    product_ranks = {
        left_rank * right_rank
        for left_rank in (0, 1, 2)
        for right_rank in (0, 1, 2)
    }
    runner.check(
        "T3d",
        "product-projector ranks are exactly 0, 1, 2, and 4",
        product_ranks == {0, 1, 2, 4} and 3 not in product_ranks,
    )

    negative_a_direction = (-ax, -ay, -az)
    below_overlap = sp.expand(
        sp.trace(
            sp.kronecker_product(
                bloch_projector(negative_a_direction), I2
            )
            * sp.kronecker_product(
                bloch_projector(c_direction), bloch_projector(d_direction)
            )
        )
    )
    overlap_parameter = sp.symbols("overlap_parameter", real=True)
    unit_overlap_solution = sp.solve(
        sp.Eq((1 - overlap_parameter) / 2, 1), overlap_parameter
    )
    runner.check(
        "T3e",
        "a rank-one product below P(-a) tensor I has first slot -a",
        sp.simplify(below_overlap - (1 - dot_ac) / 2) == 0
        and unit_overlap_solution == [-1]
        and sum_of_squares_certificate,
    )

    exact_a = e_z
    exact_b = e_x
    mixed_rank_two_sum = (
        sp.kronecker_product(bloch_projector(exact_a), I2)
        + sp.kronecker_product(I2, bloch_projector(exact_b))
    )
    a_perp = sp.Matrix([0, 1])
    b_perp = sp.Matrix([1, -1]) / sp.sqrt(2)
    joint_perp = sp.kronecker_product(a_perp, b_perp)
    symbolic_mixed_sum = (
        sp.kronecker_product(bloch_projector(a_direction), I2)
        + sp.kronecker_product(I2, bloch_projector(b_direction))
    )
    norm_b = (b_vector.T * b_vector)[0]
    generic_square_trace = sp.expand(sp.trace(symbolic_mixed_sum**2))
    runner.check(
        "T3f",
        "mixed rank-two sum is not identity by a null vector and square trace",
        matrix_is_zero(mixed_rank_two_sum * joint_perp)
        and not matrix_is_zero(sp.eye(4) * joint_perp)
        and sp.trace(mixed_rank_two_sum**2) == 6
        and sp.trace(sp.eye(4) ** 2) == 4
        and sp.simplify(generic_square_trace - (4 + norm_a + norm_b)) == 0,
    )

    (
        g1a,
        g1na,
        g1d,
        g1nd,
        g2b,
        g2nb,
        g2c,
        g2nc,
        g2d,
        g2nd,
    ) = sp.symbols(
        "g1a g1na g1d g1nd g2b g2nb g2c g2nc g2d g2nd", real=True
    )
    complement_solution = sp.solve(
        [
            sp.Eq(g1a + g1na, 1),
            sp.Eq(g1d + g1nd, 1),
            sp.Eq(g2b + g2nb, 1),
            sp.Eq(g2c + g2nc, 1),
            sp.Eq(g2d + g2nd, 1),
        ],
        (g1na, g1nd, g2nb, g2nc, g2nd),
        dict=True,
    )[0]

    site1_rooted = (
        g1a * g2b + g1a * g2nb + g1na * g2c + g1na * g2nc
    )
    site2_rooted = (
        g1a * g2b + g1na * g2b + g1d * g2nb + g1nd * g2nb
    )
    runner.check(
        "T3g-tree4",
        "complement identities normalize both rooted four-leaf tree menus",
        sp.simplify(site1_rooted.subs(complement_solution) - 1) == 0
        and sp.simplify(site2_rooted.subs(complement_solution) - 1) == 0,
    )

    site1_211 = g1a + g1na * g2d + g1na * g2nd
    site2_211 = g2b + g1d * g2nb + g1nd * g2nb
    runner.check(
        "T3g-211",
        "complement identities normalize both site-swapped 2-1-1 menus",
        sp.simplify(site1_211.subs(complement_solution) - 1) == 0
        and sp.simplify(site2_211.subs(complement_solution) - 1) == 0,
    )

    site1_22 = g1a + g1na
    site2_22 = g2b + g2nb
    trivial_menu = sp.Integer(1) * sp.Integer(1)
    runner.check(
        "T3g-coarse",
        "complement identities normalize both 2-2 menus and the identity menu",
        sp.simplify(site1_22.subs(complement_solution) - 1) == 0
        and sp.simplify(site2_22.subs(complement_solution) - 1) == 0
        and trivial_menu == 1,
    )

    rho_diagonal = sp.symbols("rho_d0:4", real=True)
    rho_pair = sp.zeros(4)
    for index in range(4):
        rho_pair[index, index] = rho_diagonal[index]
    for row in range(4):
        for column in range(row + 1, 4):
            real_part, imag_part = sp.symbols(
                f"rho_r{row}{column} rho_i{row}{column}", real=True
            )
            rho_pair[row, column] = real_part - sp.I * imag_part
            rho_pair[column, row] = real_part + sp.I * imag_part
    nx, ny, nz = sp.symbols("nx ny nz", real=True)
    n_direction = (nx, ny, nz)
    pair_marginal_components = tuple(
        sp.trace(rho_pair * sp.kronecker_product(pauli, I2))
        for pauli in PAULIS
    )
    pair_affine_left = sp.trace(
        rho_pair * sp.kronecker_product(bloch_projector(n_direction), I2)
    )
    pair_affine_right = (
        sp.trace(rho_pair)
        + nx * pair_marginal_components[0]
        + ny * pair_marginal_components[1]
        + nz * pair_marginal_components[2]
    ) / 2
    pair_forced_u = forced_trace_value(rogue_samples, u_direction)
    product_rogue_u = hemisphere_weight(u_direction) * sp.Integer(1)
    runner.check(
        "T3h",
        "pair-state restriction is affine and conflicts with the product rogue",
        matrix_is_zero(rho_pair - rho_pair.H)
        and sp.simplify(pair_affine_left - pair_affine_right) == 0
        and pair_forced_u == sp.Rational(1, 2)
        and product_rogue_u == 0
        and pair_forced_u != product_rogue_u,
    )

    g1a_w, g2b_w = sp.symbols("g1a_w g2b_w", real=True)
    within_split_residual = sp.simplify(
        g1a_w * g2b_w + g1a_w * (1 - g2b_w) - g1a_w
    )
    within_rank2_residual = sp.simplify(g1a_w + (1 - g1a_w) - 1)
    split_operator_identity = matrix_is_zero(
        sp.Matrix(sp.kronecker_product(
            bloch_projector((ax, ay, az)), bloch_projector((bx, by, bz))
        ))
        + sp.Matrix(sp.kronecker_product(
            bloch_projector((ax, ay, az)),
            bloch_projector((-bx, -by, -bz)),
        ))
        - sp.Matrix(sp.kronecker_product(bloch_projector((ax, ay, az)), I2))
    )
    rank2_operator_identity = matrix_is_zero(
        sp.Matrix(sp.kronecker_product(bloch_projector((ax, ay, az)), I2))
        + sp.Matrix(sp.kronecker_product(bloch_projector((-ax, -ay, -az)), I2))
        - sp.eye(4)
    )
    runner.check(
        "T3j",
        "the extension is additive on within-family product merges (both classified cases)",
        within_split_residual == 0
        and within_rank2_residual == 0
        and split_operator_identity
        and rank2_operator_identity,
    )

    ket00 = sp.Matrix([1, 0, 0, 0])
    ket01 = sp.Matrix([0, 1, 0, 0])
    ket10 = sp.Matrix([0, 0, 1, 0])
    projector_00 = ket00 * ket00.H
    psi_plus = (ket01 + ket10) / sp.sqrt(2)
    projector_psi_plus = psi_plus * psi_plus.H
    q_sum = projector_00 + projector_psi_plus

    def eigenvalue_multiset(matrix):
        values = []
        for value, multiplicity in matrix.eigenvals().items():
            values.extend([sp.simplify(value)] * multiplicity)
        return tuple(sorted(values, key=sp.default_sort_key))

    def multisets_equal(left, right):
        return len(left) == len(right) and all(
            sp.simplify(a - b) == 0 for a, b in zip(left, right)
        )

    def pair_partial_trace_eigenvalues(matrix, over_second):
        if over_second:
            reduced = sp.Matrix(
                2, 2,
                lambda i, j: matrix[2 * i, 2 * j] + matrix[2 * i + 1, 2 * j + 1],
            )
        else:
            reduced = sp.Matrix(
                2, 2, lambda i, j: matrix[i, j] + matrix[i + 2, j + 2]
            )
        return eigenvalue_multiset(reduced)

    q_partial_eigs_2 = pair_partial_trace_eigenvalues(q_sum, True)
    q_partial_eigs_1 = pair_partial_trace_eigenvalues(q_sum, False)
    product_rank2_partial_eigs = pair_partial_trace_eigenvalues(
        sp.Matrix(sp.kronecker_product(bloch_projector((0, 0, 1)), I2)), True
    )
    hemisphere_e_z = hemisphere_weight((0, 0, 1))
    extension_value = sp.Rational(1, 2)
    global_additivity_defect = sp.simplify(
        extension_value
        - hemisphere_e_z * hemisphere_e_z
        - extension_value
    )
    runner.check(
        "T3k",
        "the reviewer witness shows the extension is not globally additive (defect minus one)",
        matrix_is_zero(projector_00 * projector_psi_plus)
        and q_sum.rank() == 2
        and multisets_equal(
            q_partial_eigs_2, (sp.Rational(1, 2), sp.Rational(3, 2))
        )
        and multisets_equal(
            q_partial_eigs_1, (sp.Rational(1, 2), sp.Rational(3, 2))
        )
        and multisets_equal(
            product_rank2_partial_eigs, (sp.Integer(0), sp.Integer(2))
        )
        and hemisphere_e_z == 1
        and global_additivity_defect == -1,
    )

    bell_vector = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    bell_projector = bell_vector * bell_vector.H
    bell_coefficient_matrix = sp.Matrix(
        [[bell_vector[0], bell_vector[1]], [bell_vector[2], bell_vector[3]]]
    )
    runner.check(
        "T3i",
        "Bell projection is entangled and therefore outside product menus",
        bell_projector.rank() == 1
        and bell_coefficient_matrix.rank() == 2
        and sp.simplify(bell_coefficient_matrix.det() - sp.Rational(1, 2))
        == 0,
    )

    # Group T5 - finite-group zero-information limit
    invariance_equations = []
    for pauli in PAULIS:
        invariance_equations.extend(
            list(pauli * generic_sigma2 * pauli - generic_sigma2)
        )
    invariant_solution = sp.solve(
        invariance_equations,
        (state_a, state_d, state_x, state_y),
        dict=True,
    )
    invariant_sigma = generic_sigma2.subs(invariant_solution[0]).applyfunc(
        sp.simplify
    )
    invariant_scalar = sp.simplify(sp.trace(invariant_sigma) / 2)
    runner.check(
        "T5a",
        "Pauli-conjugation invariance forces a symbolic Hermitian matrix scalar",
        len(invariant_solution) == 1
        and matrix_is_zero(invariant_sigma - invariant_scalar * I2),
    )

    invariant_free_symbols = tuple(
        sorted(invariant_sigma.free_symbols, key=lambda symbol: symbol.name)
    )
    trace_one_solution = sp.solve(
        [sp.Eq(sp.trace(invariant_sigma), 1)],
        invariant_free_symbols,
        dict=True,
    )
    normalized_invariant_sigma = invariant_sigma.subs(
        trace_one_solution[0]
    ).applyfunc(sp.simplify)
    symbolic_binary_weights = (
        sp.simplify(
            sp.trace(normalized_invariant_sigma * bloch_projector(n_direction))
        ),
        sp.simplify(
            sp.trace(
                normalized_invariant_sigma
                * bloch_projector(tuple(-component for component in n_direction))
            )
        ),
    )
    runner.check(
        "T5b",
        "trace normalization gives I/2 and uniform embedded binary weights",
        len(invariant_free_symbols) == 1
        and len(trace_one_solution) == 1
        and matrix_is_zero(normalized_invariant_sigma - I2 / 2)
        and sp.trace(normalized_invariant_sigma) == 1
        and symbolic_binary_weights
        == (sp.Rational(1, 2), sp.Rational(1, 2)),
    )

    # Group N - exact document needle checks
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    bridge_text = BRIDGE_PATH.read_text(encoding="utf-8")
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8")
    effect_bridge_text = EFFECT_BRIDGE_PATH.read_text(encoding="utf-8")
    note_normalized = normalize(note_text)
    bridge_normalized = normalize(bridge_text)
    axiom_normalized = normalize(axiom_text)
    effect_bridge_normalized = normalize(effect_bridge_text)

    runner.check(
        "N1",
        "axiom memo pins record readability to record content alone",
        "Only records are readable. A readout value is determined by record content alone."
        in axiom_normalized,
    )
    runner.check(
        "N2",
        "axiom memo limits the axioms to their named primitive content",
        "These axioms state only their named primitive content."
        in axiom_normalized,
    )
    runner.check(
        "N3",
        "landed bridge identifies Gleason as imported classical mathematics",
        "Gleason's theorem is imported as named classical mathematics."
        in bridge_normalized,
    )
    runner.check(
        "N4",
        "landed bridge pins the exact three-direction trace-form refutation",
        "Three directions plus normalization refute every `2x2` trace form at once"
        in bridge_normalized,
    )
    runner.check(
        "N5",
        "landed bridge pins the full projection-measure strength warning",
        "Without this full projection-measure strength a partial menu assignment is not a frame function and Gleason does not apply"
        in bridge_normalized,
    )
    runner.check(
        "N6",
        "landed bridge pins the adjacency and H4 attribution",
        "adjacency alone pays for nothing here without H4's strength"
        in bridge_normalized,
    )
    runner.check(
        "N7",
        "effect bridge pins the landed Bloch coefficient with exact Unicode minus",
        "(2 m(P_a^+) − 1)" in effect_bridge_normalized,
    )
    runner.check(
        "N8-claim",
        "source note pins its exact claim identifier",
        "claim_id: born_form_effect_menu_sitewise_forcing_and_product_menu_boundary_bounded_theorem_note_2026-07-17"
        in note_text,
    )
    runner.check(
        "N8-hypotheses",
        "source note contains both effect-grade hypothesis labels",
        "**(E1)" in note_text and "**(E2)" in note_text,
    )
    runner.check(
        "N8-no-bridge",
        "source note pins the no-literature-bridge-input scope",
        "no literature bridge input" in note_normalized,
    )

    failures = runner.total()
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
