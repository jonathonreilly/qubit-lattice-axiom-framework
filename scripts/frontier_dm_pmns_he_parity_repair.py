#!/usr/bin/env python3
"""Exact certificate for an abstract explicitly defined Hermitian product.

The historical filename is retained for claim-graph continuity.  The symbols
are six real coordinates and one real phase in an explicitly defined matrix;
this runner does not infer a physical chart, carrier, selector, or phase law.

Modes:
  --mode normal       direct symbolic multiplication and exact identities
  --mode independent  column-outer-product and separate numerical reconstruction
  --mode hostile      recompute and reject seven specified mutations
"""

from __future__ import annotations

import argparse
import cmath
import math
import sys
from itertools import combinations
from typing import TypeAlias

import sympy as sp


PASS = 0
FAIL = 0

ComplexMatrix: TypeAlias = list[list[complex]]


def check(label: str, condition: bool, detail: str = "") -> None:
    """Record one computed theorem check."""
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def section(title: str) -> None:
    print(f"\n{'-' * 82}\n{title}\n{'-' * 82}")


def equivalent(left: sp.Expr, right: sp.Expr = sp.Integer(0)) -> bool:
    """Test an exact identity for the real-symbol expressions used here."""
    residual = sp.expand_complex(sp.simplify(left - right))
    return sp.trigsimp(sp.expand(residual)) == 0


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(equivalent(entry) for entry in matrix)


def direct_symbolic_data() -> dict[str, object]:
    """Build the primary certificate by literal Y Y^dagger multiplication."""
    x1, x2, x3, y1, y2, y3, delta, t = sp.symbols(
        "x1 x2 x3 y1 y2 y3 delta t", real=True
    )
    y_matrix = sp.Matrix(
        [
            [x1, y1, 0],
            [0, x2, y2],
            [y3 * sp.exp(sp.I * delta), 0, x3],
        ]
    )
    h_matrix = y_matrix * y_matrix.conjugate().T
    expected = sp.Matrix(
        [
            [x1**2 + y1**2, x2 * y1, x1 * y3 * sp.exp(-sp.I * delta)],
            [x2 * y1, x2**2 + y2**2, x3 * y2],
            [x1 * y3 * sp.exp(sp.I * delta), x3 * y2, x3**2 + y3**2],
        ]
    )
    return {
        "symbols": (x1, x2, x3, y1, y2, y3, delta, t),
        "Y": y_matrix,
        "H": h_matrix,
        "expected": expected,
    }


def normal_checks() -> int:
    """Prove the finite matrix theorem by direct exact computation."""
    data = direct_symbolic_data()
    x1, x2, x3, y1, y2, y3, delta, t = data["symbols"]
    y_matrix = data["Y"]
    h_matrix = data["H"]
    expected = data["expected"]
    assert isinstance(y_matrix, sp.MatrixBase)
    assert isinstance(h_matrix, sp.MatrixBase)
    assert isinstance(expected, sp.MatrixBase)

    print("Abstract Hermitian-product conjugation-parity theorem for an explicit matrix family")
    section("Direct product, order, and conjugation")
    check("direct Y Y^dagger multiplication gives all displayed entries", matrix_zero(h_matrix - expected))
    check("the computed product is Hermitian", matrix_zero(h_matrix - h_matrix.conjugate().T))
    check(
        "sign reversal is entrywise conjugation",
        matrix_zero(h_matrix.subs(delta, -delta) - h_matrix.conjugate()),
    )
    phase_independent = ((0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2))
    check(
        "the seven phase-independent entries are individually even",
        all(equivalent(h_matrix[i, j].subs(delta, -delta), h_matrix[i, j]) for i, j in phase_independent),
    )
    phase_sensitive_coordinates = {
        x1: sp.Rational(2, 3),
        y3: sp.Rational(5, 7),
    }
    sample_phase = sp.Rational(2, 5)
    check(
        "the two phase-sensitive entries are conjugation-paired, not generically entrywise even",
        equivalent(h_matrix[0, 2].subs(delta, -delta), h_matrix[2, 0])
        and equivalent(h_matrix[2, 0].subs(delta, -delta), h_matrix[0, 2])
        and not equivalent(
            h_matrix[0, 2].subs(phase_sensitive_coordinates).subs(delta, -sample_phase),
            h_matrix[0, 2].subs(phase_sensitive_coordinates).subs(delta, sample_phase),
        ),
    )
    alternate_order = y_matrix.conjugate().T * y_matrix
    check(
        "Y^dagger Y is generically distinct from the certified Y Y^dagger product",
        not matrix_zero(h_matrix - alternate_order),
    )

    section("Positive semidefiniteness")
    a_diag = x1**2 + y1**2
    b_diag = x2**2 + y2**2
    c_diag = x3**2 + y3**2
    one_by_one = (a_diag, b_diag, c_diag)
    for index, expression in enumerate(one_by_one, start=1):
        check(
            f"principal minor ({index}) is the displayed sum of real squares",
            equivalent(h_matrix[index - 1, index - 1], expression),
        )

    two_by_two_targets = {
        (0, 1): x1**2 * x2**2 + x1**2 * y2**2 + y1**2 * y2**2,
        (0, 2): x1**2 * x3**2 + y1**2 * x3**2 + y1**2 * y3**2,
        (1, 2): x2**2 * x3**2 + x2**2 * y3**2 + y2**2 * y3**2,
    }
    for indices, target in two_by_two_targets.items():
        minor = h_matrix.extract(indices, indices).det()
        check(f"principal minor {indices} is a sum of real squares", equivalent(minor, target))

    a_product = x1 * x2 * x3
    b_product = y1 * y2 * y3
    determinant_sos = (a_product + b_product * sp.cos(delta)) ** 2 + (
        b_product * sp.sin(delta)
    ) ** 2
    check("det(H) is the displayed sum of two real squares", equivalent(h_matrix.det(), determinant_sos))
    check("det(H) equals |det(Y)|^2", equivalent(h_matrix.det(), y_matrix.det() * sp.conjugate(y_matrix.det())))

    u1, u2, u3, v1, v2, v3 = sp.symbols("u1 u2 u3 v1 v2 v3", real=True)
    vector = sp.Matrix([u1 + sp.I * v1, u2 + sp.I * v2, u3 + sp.I * v3])
    quadratic = (vector.conjugate().T * h_matrix * vector)[0]
    pulled_back = y_matrix.conjugate().T * vector
    norm_square = sum(sp.conjugate(entry) * entry for entry in pulled_back)
    check("v^dagger H v equals ||Y^dagger v||_2^2 exactly", equivalent(quadratic, norm_square))

    section("Characteristic data and invariant readouts")
    p = x2 * y1
    q = x1 * y3
    r = x3 * y2
    c1 = a_diag + b_diag + c_diag
    c2 = a_diag * b_diag + a_diag * c_diag + b_diag * c_diag - p**2 - q**2 - r**2
    c3 = a_product**2 + b_product**2 + 2 * a_product * b_product * sp.cos(delta)
    coefficients = h_matrix.charpoly(t).all_coeffs()
    targets = (sp.Integer(1), -c1, c2, -c3)
    for index, (actual, target) in enumerate(zip(coefficients, targets, strict=True)):
        check(f"characteristic coefficient {index} has the derived closed form", equivalent(actual, target))

    check("trace has the derived closed form", equivalent(sp.trace(h_matrix), c1))
    check("determinant has the derived cosine form", equivalent(h_matrix.det(), c3))
    check("trace is even under sign reversal", equivalent(sp.trace(h_matrix.subs(delta, -delta)), sp.trace(h_matrix)))
    check("determinant is even under sign reversal", equivalent(h_matrix.det().subs(delta, -delta), h_matrix.det()))
    for power in (2, 3, 4):
        check(
            f"trace power k={power} is even under sign reversal",
            equivalent(sp.trace(h_matrix.subs(delta, -delta) ** power), sp.trace(h_matrix**power)),
        )
    frobenius_sq = sum(sp.conjugate(h_matrix[i, j]) * h_matrix[i, j] for i in range(3) for j in range(3))
    check("Frobenius norm squared equals tr(H^2)", equivalent(frobenius_sq, sp.trace(h_matrix**2)))
    check("Frobenius norm squared is even", equivalent(frobenius_sq.subs(delta, -delta), frobenius_sq))
    check(
        "sign reversal preserves the full characteristic polynomial",
        all(equivalent(a.subs(delta, -delta), a) for a in coefficients),
    )

    print(f"\nSUMMARY: MODE=normal PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


def independent_symbolic_checks() -> None:
    """Reconstruct the matrix as a sum of column outer products."""
    a1, a2, a3, b1, b2, b3, theta, z = sp.symbols(
        "a1 a2 a3 b1 b2 b3 theta z", real=True
    )
    columns = (
        (a1, 0, b3 * sp.exp(sp.I * theta)),
        (b1, a2, 0),
        (0, b2, a3),
    )
    reconstructed = sp.Matrix(
        3,
        3,
        lambda row, column: sum(
            carrier[row] * sp.conjugate(carrier[column]) for carrier in columns
        ),
    )
    independently_expected = (
        (a1**2 + b1**2, a2 * b1, a1 * b3 * sp.exp(-sp.I * theta)),
        (a2 * b1, a2**2 + b2**2, a3 * b2),
        (a1 * b3 * sp.exp(sp.I * theta), a3 * b2, a3**2 + b3**2),
    )
    for row in range(3):
        for column in range(3):
            check(
                f"outer-product reconstruction entry ({row + 1},{column + 1})",
                equivalent(reconstructed[row, column], independently_expected[row][column]),
            )
    check("outer-product reconstruction is Hermitian", matrix_zero(reconstructed - reconstructed.conjugate().T))
    check(
        "outer-product reconstruction has sign-flip conjugation parity",
        matrix_zero(reconstructed.subs(theta, -theta) - reconstructed.conjugate()),
    )

    d0, d1, d2 = reconstructed[0, 0], reconstructed[1, 1], reconstructed[2, 2]
    manual_c1 = d0 + d1 + d2
    manual_c2 = (
        d0 * d1
        + d0 * d2
        + d1 * d2
        - reconstructed[0, 1] * reconstructed[1, 0]
        - reconstructed[0, 2] * reconstructed[2, 0]
        - reconstructed[1, 2] * reconstructed[2, 1]
    )
    manual_c3 = determinant_3x3_symbolic(reconstructed)
    for index, coefficient in enumerate((manual_c1, manual_c2, manual_c3), start=1):
        check(
            f"manual characteristic invariant c{index} is even",
            equivalent(coefficient.subs(theta, -theta), coefficient),
        )
    polynomial = z**3 - manual_c1 * z**2 + manual_c2 * z - manual_c3
    check("manual characteristic polynomial is preserved", equivalent(polynomial.subs(theta, -theta), polynomial))


def determinant_3x3_symbolic(matrix: sp.MatrixBase) -> sp.Expr:
    return (
        matrix[0, 0] * (matrix[1, 1] * matrix[2, 2] - matrix[1, 2] * matrix[2, 1])
        - matrix[0, 1] * (matrix[1, 0] * matrix[2, 2] - matrix[1, 2] * matrix[2, 0])
        + matrix[0, 2] * (matrix[1, 0] * matrix[2, 1] - matrix[1, 1] * matrix[2, 0])
    )


def outer_product_sum(columns: tuple[tuple[complex, complex, complex], ...]) -> ComplexMatrix:
    return [
        [sum(column[i] * column[j].conjugate() for column in columns) for j in range(3)]
        for i in range(3)
    ]


def independent_numeric_h(
    x_values: tuple[complex, complex, complex],
    y_values: tuple[complex, complex, complex],
    delta: float,
) -> ComplexMatrix:
    x1, x2, x3 = x_values
    y1, y2, y3 = y_values
    columns = (
        (x1, 0j, y3 * cmath.exp(1j * delta)),
        (y1, x2, 0j),
        (0j, y2, x3),
    )
    return outer_product_sum(columns)


def numeric_det(matrix: ComplexMatrix) -> complex:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def numeric_char_coefficients(matrix: ComplexMatrix) -> tuple[complex, complex, complex, complex]:
    diagonal = (matrix[0][0], matrix[1][1], matrix[2][2])
    c1 = sum(diagonal)
    c2 = (
        diagonal[0] * diagonal[1]
        + diagonal[0] * diagonal[2]
        + diagonal[1] * diagonal[2]
        - matrix[0][1] * matrix[1][0]
        - matrix[0][2] * matrix[2][0]
        - matrix[1][2] * matrix[2][1]
    )
    c3 = numeric_det(matrix)
    return (1 + 0j, -c1, c2, -c3)


def max_difference(left: ComplexMatrix, right: ComplexMatrix) -> float:
    return max(abs(left[i][j] - right[i][j]) for i in range(3) for j in range(3))


def conjugate_numeric(matrix: ComplexMatrix) -> ComplexMatrix:
    return [[entry.conjugate() for entry in row] for row in matrix]


def numeric_principal_minors(matrix: ComplexMatrix) -> tuple[complex, ...]:
    minors: list[complex] = [matrix[i][i] for i in range(3)]
    for i, j in combinations(range(3), 2):
        minors.append(matrix[i][i] * matrix[j][j] - matrix[i][j] * matrix[j][i])
    minors.append(numeric_det(matrix))
    return tuple(minors)


def independent_numeric_checks() -> None:
    samples = (
        ("generic-positive", (0.4, 0.6, 0.7), (0.2, 0.3, 0.5), 0.37),
        ("mixed-sign", (1.0, -0.2, 0.9), (0.8, 0.1, -0.4), 1.2),
        ("second-mixed-sign", (-0.5, 0.25, 0.75), (0.6, -0.3, 0.2), -0.9),
        ("all-zero", (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), 0.61),
        ("rank-deficient", (1.0, 1.0, 1.0), (1.0, 1.0, 1.0), math.pi),
    )
    for sample_name, x_values, y_values, delta in samples:
        h_pos = independent_numeric_h(x_values, y_values, delta)
        h_neg = independent_numeric_h(x_values, y_values, -delta)
        check(
            f"numeric {sample_name} sample sign-flip conjugation",
            max_difference(h_neg, conjugate_numeric(h_pos)) < 1e-12,
        )
        check(
            f"numeric {sample_name} sample Hermiticity",
            max_difference(h_pos, conjugate_numeric([list(row) for row in zip(*h_pos)])) < 1e-12,
        )
        det_y = (
            x_values[0] * x_values[1] * x_values[2]
            + y_values[0] * y_values[1] * y_values[2] * cmath.exp(1j * delta)
        )
        check(
            f"numeric {sample_name} sample determinant equals |det(Y)|^2",
            abs(numeric_det(h_pos) - abs(det_y) ** 2) < 1e-10,
        )
        coeff_pos = numeric_char_coefficients(h_pos)
        coeff_neg = numeric_char_coefficients(h_neg)
        check(
            f"numeric {sample_name} sample characteristic coefficients are even",
            max(abs(a - b) for a, b in zip(coeff_pos, coeff_neg, strict=True)) < 1e-10,
        )
        minors = numeric_principal_minors(h_pos)
        check(
            f"numeric {sample_name} sample all principal minors are nonnegative real",
            all(abs(value.imag) < 1e-10 and value.real >= -1e-10 for value in minors),
        )


def independent_checks() -> int:
    """Run the independently coded symbolic and numerical reconstructions."""
    print("Abstract matrix-family theorem: independent reconstruction")
    section("Column outer products and manual characteristic polynomial")
    independent_symbolic_checks()
    section("Independent numerical and principal-minor route")
    independent_numeric_checks()
    print(f"\nSUMMARY: MODE=independent PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


def hostile_reference_and_symbols() -> tuple[sp.Matrix, tuple[sp.Symbol, ...]]:
    c1, c2, c3, d1, d2, d3, phi = sp.symbols("c1 c2 c3 d1 d2 d3 phi", real=True)
    matrix = sp.Matrix(
        [[c1, d1, 0], [0, c2, d2], [d3 * sp.exp(sp.I * phi), 0, c3]]
    )
    return matrix, (c1, c2, c3, d1, d2, d3, phi)


def hostile_checks() -> int:
    """Recompute and reject every requested mutation."""
    print("Abstract matrix-family theorem: hostile mutation controls")
    section("Mutated products and premises")
    y_matrix, symbols = hostile_reference_and_symbols()
    c1, c2, c3, d1, d2, d3, phi = symbols
    reference = y_matrix * y_matrix.conjugate().T

    wrong_sign_y = sp.Matrix(
        [[c1, d1, 0], [0, c2, d2], [d3 * sp.exp(-sp.I * phi), 0, c3]]
    )
    check(
        "reject wrong phase sign",
        not matrix_zero(wrong_sign_y * wrong_sign_y.conjugate().T - reference),
    )

    moved_phase_y = sp.Matrix(
        [[c1, d1, 0], [0, c2, d2], [d3, 0, c3 * sp.exp(sp.I * phi)]]
    )
    check(
        "reject phase moved to a different matrix entry",
        not matrix_zero(moved_phase_y * moved_phase_y.conjugate().T - reference),
    )
    check(
        "reject transpose without conjugation in the adjoint",
        not matrix_zero(y_matrix * y_matrix.T - reference),
    )
    check(
        "reject Y^dagger Y substituted for Y Y^dagger",
        not matrix_zero(y_matrix.conjugate().T * y_matrix - reference),
    )

    complex_x = (1.0 + 0.7j, 0.8 + 0j, -0.4 + 0j)
    real_y = (0.5 + 0j, -0.3 + 0j, 0.9 + 0j)
    complex_pos = independent_numeric_h(complex_x, real_y, 0.43)
    complex_neg = independent_numeric_h(complex_x, real_y, -0.43)
    check(
        "reject complex-coordinate mutation that breaks the real-premise parity",
        max_difference(complex_neg, conjugate_numeric(complex_pos)) > 1e-6,
    )

    substitution = {c1: 0.7, c2: -0.4, c3: 0.9, d1: 0.2, d2: 0.6, d3: -0.5, phi: 0.37}
    h_pos = reference.subs(substitution).evalf()
    h_neg = reference.subs({**substitution, phi: -0.37}).evalf()
    check(
        "reject false entrywise-evenness of the phase-sensitive entries",
        not matrix_zero(h_neg - h_pos),
    )

    diag = (reference[0, 0], reference[1, 1], reference[2, 2])
    correct_c2 = (
        diag[0] * diag[1]
        + diag[0] * diag[2]
        + diag[1] * diag[2]
        - reference[0, 1] * reference[1, 0]
        - reference[0, 2] * reference[2, 0]
        - reference[1, 2] * reference[2, 1]
    )
    wrong_c2 = correct_c2 + reference[0, 2] * reference[2, 0]
    true_coefficient = reference.charpoly().all_coeffs()[2]
    check(
        "reject wrong characteristic coefficient missing the (1,3) product",
        equivalent(true_coefficient, correct_c2) and not equivalent(true_coefficient, wrong_c2),
    )

    print(f"\nSUMMARY: MODE=hostile PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile"),
        default="normal",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.mode == "normal":
        return normal_checks()
    if args.mode == "independent":
        return independent_checks()
    return hostile_checks()


if __name__ == "__main__":
    sys.exit(main())
