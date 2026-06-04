#!/usr/bin/env python3
"""Exact finite-dimensional checks for the tensor-composition no-go.

The runner proves only a narrow no-go: faithful commuting local M_2(C) copies
do not, by locality alone, force the full composite to be the generated
ordinary tensor product. A duplicate global sector M_4(C) oplus M_4(C)
satisfies operational locality but is not locally tomographic.
"""

from __future__ import annotations

import sympy as sp
from sympy import I, Matrix, eye, zeros


RESULTS: list[tuple[str, bool]] = []


def check(label: str, ok: bool) -> None:
    RESULTS.append((label, bool(ok)))


def kron(a: Matrix, b: Matrix) -> Matrix:
    rows_a, cols_a = a.shape
    rows_b, cols_b = b.shape
    out = zeros(rows_a * rows_b, cols_a * cols_b)
    for i in range(rows_a):
        for j in range(cols_a):
            for k in range(rows_b):
                for l in range(cols_b):
                    out[i * rows_b + k, j * cols_b + l] = a[i, j] * b[k, l]
    return out


def direct_sum(a: Matrix, b: Matrix) -> Matrix:
    return Matrix.diag(a, b)


def flatten_rank(mats: list[Matrix]) -> int:
    return Matrix.hstack(*[mat.reshape(mat.rows * mat.cols, 1) for mat in mats]).rank()


def self_adjoint_dim_complex(n: int) -> int:
    return n * n


def self_adjoint_dim_real(n: int) -> int:
    return n * (n + 1) // 2


def matrix_units(n: int) -> list[Matrix]:
    units: list[Matrix] = []
    for i in range(n):
        for j in range(n):
            m = zeros(n, n)
            m[i, j] = 1
            units.append(m)
    return units


def main() -> int:
    sigma0 = eye(2)
    sigma1 = Matrix([[0, 1], [1, 0]])
    sigma2 = Matrix([[0, -I], [I, 0]])
    sigma3 = Matrix([[1, 0], [0, -1]])
    pauli = [sigma0, sigma1, sigma2, sigma3]

    ordinary_products = [kron(a, b) for a in pauli for b in pauli]
    check(
        "N1 ordinary generated complex tensor product is locally tomographic: 16 = 4*4",
        flatten_rank(ordinary_products) == 16
        and self_adjoint_dim_complex(4)
        == self_adjoint_dim_complex(2) * self_adjoint_dim_complex(2),
    )

    duplicate_a = [direct_sum(kron(a, sigma0), kron(a, sigma0)) for a in pauli]
    duplicate_b = [direct_sum(kron(sigma0, b), kron(sigma0, b)) for b in pauli]

    check(
        "N2 local M2(C) embeddings are faithful: each local image has rank 4",
        flatten_rank(duplicate_a) == 4 and flatten_rank(duplicate_b) == 4,
    )

    commute = all(
        sp.simplify(a * b - b * a) == zeros(8, 8)
        for a in duplicate_a
        for b in duplicate_b
    )
    check("N3 operational locality holds: the two local images commute", commute)

    duplicate_products = [
        direct_sum(kron(a, b), kron(a, b))
        for a in pauli
        for b in pauli
    ]
    product_rank = flatten_rank(duplicate_products)
    full_direct_sum_basis = [
        direct_sum(unit, zeros(4, 4)) for unit in matrix_units(4)
    ] + [
        direct_sum(zeros(4, 4), unit) for unit in matrix_units(4)
    ]
    full_rank = flatten_rank(full_direct_sum_basis)
    check(
        "N4 local products span only diagonal M4(C): rank 16, full M4(C) oplus M4(C) rank 32",
        product_rank == 16 and full_rank == 32 and product_rank != full_rank,
    )

    sector_z = direct_sum(eye(4), -eye(4))
    span_with_z_rank = flatten_rank(duplicate_products + [sector_z])
    z_commutes = all(
        sp.simplify(sector_z * product - product * sector_z) == zeros(8, 8)
        for product in duplicate_products
    )
    check(
        "N5 central sector observable I4 oplus -I4 commutes with local products but is outside their span",
        z_commutes and span_with_z_rank == product_rank + 1,
    )

    check(
        "N6 NO-GO: same local complex qubits plus locality do not force generation/local tomography",
        commute
        and flatten_rank(duplicate_a) == 4
        and flatten_rank(duplicate_b) == 4
        and product_rank == 16
        and full_rank == 32
        and span_with_z_rank == 17,
    )

    check(
        "N7 rebit comparator: real tensor product is not locally tomographic, 3*3 = 9 != 10",
        self_adjoint_dim_real(2) ** 2 == 9
        and self_adjoint_dim_real(4) == 10
        and self_adjoint_dim_real(2) ** 2 != self_adjoint_dim_real(4),
    )

    left_i = kron(I * sigma0, sigma0)
    right_i = kron(sigma0, I * sigma0)
    global_i = I * eye(4)
    check(
        "N8 ordinary complex tensor product has shared scalar i",
        sp.simplify(left_i - global_i) == zeros(4, 4)
        and sp.simplify(right_i - global_i) == zeros(4, 4),
    )

    passed = sum(1 for _, ok in RESULTS if ok)
    failed = len(RESULTS) - passed
    for label, ok in RESULTS:
        print(("PASS" if ok else "FAIL") + " - " + label)
    print()
    print(f"{passed} PASS, {failed} FAIL")
    print(
        "Narrow no-go verified: operational locality with faithful local "
        "M_2(C) copies does not by itself force the ordinary generated "
        "tensor product or local tomography. A local-tomography/no-extra-"
        "global generation premise is the exact residual."
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
