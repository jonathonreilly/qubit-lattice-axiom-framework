#!/usr/bin/env python3
"""Exact checks for fermionic realification and Pfaffian determinant power."""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_"
    "NARROW_THEOREM_NOTE_2026-07-12.md"
)

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail != "" else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print(f"\n{title}\n{'-' * len(title)}")


def pfaffian(matrix: sp.Matrix) -> sp.Expr:
    """Recursive Pfaffian for the small exact matrices used here."""
    size = matrix.rows
    if size == 0:
        return sp.Integer(1)
    if size % 2:
        return sp.Integer(0)
    total = sp.Integer(0)
    for j in range(1, size):
        keep = [index for index in range(size) if index not in (0, j)]
        minor = matrix.extract(keep, keep)
        total += (-1) ** (j + 1) * matrix[0, j] * pfaffian(minor)
    return sp.expand(total)


def fermion_kernel(matrix: sp.Matrix) -> sp.Matrix:
    zeros = sp.zeros(matrix.rows)
    return sp.Matrix.vstack(
        sp.Matrix.hstack(zeros, matrix),
        sp.Matrix.hstack(-matrix.T, zeros),
    )


def realification(matrix: sp.Matrix) -> sp.Matrix:
    real = matrix.applyfunc(sp.re)
    imag = matrix.applyfunc(sp.im)
    return sp.Matrix.vstack(
        sp.Matrix.hstack(real, -imag),
        sp.Matrix.hstack(imag, real),
    )


def grassmann_mul(
    left: dict[int, sp.Expr], right: dict[int, sp.Expr]
) -> dict[int, sp.Expr]:
    """Multiply sparse exterior polynomials in ascending generator order."""
    out: dict[int, sp.Expr] = {}
    for left_mask, left_coeff in left.items():
        for right_mask, right_coeff in right.items():
            if left_mask & right_mask:
                continue
            inversions = 0
            bits = right_mask
            while bits:
                low = bits & -bits
                index = low.bit_length() - 1
                inversions += (left_mask >> (index + 1)).bit_count()
                bits ^= low
            sign = -1 if inversions % 2 else 1
            mask = left_mask | right_mask
            out[mask] = sp.simplify(
                out.get(mask, 0) + sign * left_coeff * right_coeff
            )
    return {mask: coeff for mask, coeff in out.items() if coeff != 0}


def grassmann_quadratic(matrix: sp.Matrix) -> dict[int, sp.Expr]:
    """Return (1/2) Psi^T A_K Psi for Psi=(chibar,chi)."""
    kernel = fermion_kernel(matrix)
    variables = [{1 << index: sp.Integer(1)} for index in range(kernel.rows)]
    out: dict[int, sp.Expr] = {}
    for row in range(kernel.rows):
        for col in range(kernel.cols):
            term = grassmann_mul(variables[row], variables[col])
            for mask, coeff in term.items():
                out[mask] = sp.simplify(
                    out.get(mask, 0)
                    + sp.Rational(1, 2) * kernel[row, col] * coeff
                )
    return {mask: coeff for mask, coeff in out.items() if coeff != 0}


def grassmann_gaussian_top(matrix: sp.Matrix) -> sp.Expr:
    """Top coefficient of exp(-(1/2) Psi^T A_K Psi)."""
    action = {
        mask: -coeff for mask, coeff in grassmann_quadratic(matrix).items()
    }
    exponential: dict[int, sp.Expr] = {0: sp.Integer(1)}
    power: dict[int, sp.Expr] = {0: sp.Integer(1)}
    factorial = sp.Integer(1)
    for degree in range(1, matrix.rows + 1):
        power = grassmann_mul(power, action)
        factorial *= degree
        for mask, coeff in power.items():
            exponential[mask] = sp.simplify(
                exponential.get(mask, 0) + coeff / factorial
            )
    top_mask = (1 << (2 * matrix.rows)) - 1
    return sp.simplify(exponential.get(top_mask, 0))


def exterior_top_jacobian(matrix: sp.Matrix) -> sp.Expr:
    """Coefficient of Xi_1...Xi_m in wedge_i sum_j M_ij Xi_j."""
    product: dict[int, sp.Expr] = {0: sp.Integer(1)}
    for row in range(matrix.rows):
        linear_form = {
            1 << col: matrix[row, col]
            for col in range(matrix.cols)
            if matrix[row, col] != 0
        }
        product = grassmann_mul(product, linear_form)
    return sp.simplify(product.get((1 << matrix.rows) - 1, 0))


def main() -> int:
    print("Fermionic realification and Pfaffian determinant power")
    print("=" * 64)

    section("Part A: block-Pfaffian identity")
    k1 = sp.Symbol("k1")
    kernel1 = fermion_kernel(sp.Matrix([[k1]]))
    check("rank-1 kernel is antisymmetric", kernel1.T == -kernel1)
    check("rank-1 Pfaffian has determinant power one", pfaffian(kernel1) == k1)

    a, b, c, d = sp.symbols("a b c d")
    matrix2 = sp.Matrix([[a, b], [c, d]])
    kernel2 = fermion_kernel(matrix2)
    sign2 = (-1) ** (2 * 1 // 2)
    check("rank-2 kernel is antisymmetric", kernel2.T == -kernel2)
    check(
        "generic rank-2 block Pfaffian identity",
        sp.simplify(pfaffian(kernel2) - sign2 * matrix2.det()) == 0,
    )

    entries3 = sp.symbols("q00:03 q10:13 q20:23")
    matrix3 = sp.Matrix(3, 3, entries3)
    kernel3 = fermion_kernel(matrix3)
    sign3 = (-1) ** (3 * 2 // 2)
    check("rank-3 kernel is antisymmetric", kernel3.T == -kernel3)
    check(
        "generic rank-3 block Pfaffian identity",
        sp.simplify(pfaffian(kernel3) - sign3 * matrix3.det()) == 0,
    )

    section("Part B: quadratic form and coordinate covariance")
    expected_quadratic = {
        (1 << i) | (1 << (2 + j)): matrix2[i, j]
        for i in range(2)
        for j in range(2)
    }
    check(
        "exterior-algebra quadratic is chibar K chi",
        grassmann_quadratic(matrix2) == expected_quadratic,
    )

    p, q, r, s = sp.symbols("p q r s")
    transform = sp.Matrix([[p, q], [r, s]])
    congruent = transform.T * kernel1 * transform
    check(
        "Pfaffian congruence carries det(M)",
        sp.simplify(pfaffian(congruent) - transform.det() * pfaffian(kernel1)) == 0,
    )
    check(
        "exterior top form independently gives det(M)",
        sp.simplify(exterior_top_jacobian(transform) - transform.det()) == 0,
    )
    check(
        "inverse top-form Jacobian cancels congruence factor",
        sp.simplify(pfaffian(congruent) / transform.det() - pfaffian(kernel1)) == 0,
    )

    for rank, matrix in ((1, sp.Matrix([[k1]])), (2, matrix2), (3, matrix3)):
        orientation = (-1) ** (rank * (rank + 1) // 2)
        gaussian_top = grassmann_gaussian_top(matrix)
        check(
            f"rank-{rank} negative-exponent Gaussian top sign",
            sp.simplify(gaussian_top - orientation * matrix.det()) == 0,
        )
        check(
            f"rank-{rank} oriented Gaussian equals det(K)",
            sp.simplify(orientation * gaussian_top - matrix.det()) == 0,
        )

    section("Part C: conjugate sector and ordinary realification")
    u, v = sp.symbols("u v", real=True)
    z = u + sp.I * v
    complex_scalar = sp.Matrix([[z]])
    conjugate_scalar = sp.conjugate(complex_scalar)
    paired_kernel = sp.diag(
        fermion_kernel(complex_scalar), fermion_kernel(conjugate_scalar)
    )
    single_pf = pfaffian(fermion_kernel(complex_scalar))
    conjugate_pf = pfaffian(fermion_kernel(conjugate_scalar))
    paired_pf = pfaffian(paired_kernel)
    modulus_square = sp.expand(z * sp.conjugate(z))
    check("single-sector Pfaffian equals z", sp.simplify(single_pf - z) == 0)
    check(
        "conjugate-sector Pfaffian equals conjugate(z)",
        sp.simplify(conjugate_pf - sp.conjugate(z)) == 0,
    )
    check(
        "direct-sum Pfaffian is the product of sector Pfaffians",
        sp.simplify(paired_pf - single_pf * conjugate_pf) == 0,
    )
    check("paired Pfaffian is modulus square", sp.simplify(paired_pf - modulus_square) == 0)
    check(
        "ordinary realification determinant matches paired sectors",
        sp.simplify(realification(complex_scalar).det() - paired_pf) == 0,
    )
    x0, x1, x2, x3, y0, y1, y2, y3 = sp.symbols(
        "x0 x1 x2 x3 y0 y1 y2 y3", real=True
    )
    complex_matrix2 = sp.Matrix(
        [[x0 + sp.I * y0, x1 + sp.I * y1],
         [x2 + sp.I * y2, x3 + sp.I * y3]]
    )
    check(
        "generic rank-2 realification is the conjugate determinant product",
        sp.simplify(
            realification(complex_matrix2).det()
            - complex_matrix2.det() * sp.conjugate(complex_matrix2.det())
        )
        == 0,
    )
    paired_kernel2 = sp.diag(
        fermion_kernel(complex_matrix2),
        fermion_kernel(sp.conjugate(complex_matrix2)),
    )
    check(
        "generic rank-2 conjugate direct sum has no residual sign",
        sp.simplify(
            pfaffian(paired_kernel2)
            - complex_matrix2.det() * sp.conjugate(complex_matrix2.det())
        )
        == 0,
    )
    check("single sector retains complex phase", sp.simplify(sp.im(single_pf) - v) == 0)
    check("paired sectors cancel complex phase", sp.simplify(sp.im(paired_pf)) == 0)

    generic_realification = realification(
        sp.Matrix([[u + sp.I * v, 2], [3 * sp.I, 1 - sp.I]])
    )
    check(
        "ordinary realification need not be antisymmetric",
        generic_realification.T != -generic_realification,
    )

    singular = sp.Matrix([[1 + sp.I, 2], [2 + 2 * sp.I, 4]])
    check("singular complex determinant vanishes", singular.det() == 0)
    check("singular block Pfaffian vanishes", pfaffian(fermion_kernel(singular)) == 0)
    check("singular realification determinant vanishes", realification(singular).det() == 0)

    section("Scope guards")
    note = NOTE.read_text(encoding="utf-8")
    check(
        "source states determinant-power preservation under coordinate change",
        "coordinate change cannot alter the determinant\npower" in note,
    )
    check(
        "source limits the theorem to a supplied algebraic domain",
        "The theorem domain is a supplied Grassmann action" in note,
    )
    check(
        "source leaves registered r outside the theorem domain",
        "grain, registered `r`, `delta`, and R-eta readout lies outside" in note,
    )

    print("\n" + "=" * 64)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
