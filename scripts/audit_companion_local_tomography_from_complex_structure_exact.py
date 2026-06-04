#!/usr/bin/env python3
"""Exact finite-dimensional checks for the conditional local-tomography note.

The runner proves only this conditional fact: under the ordinary shared-scalar
complex tensor product M_2(C) tensor_C M_2(C) ~= M_4(C), two complex qubits are
locally tomographic by self-adjoint dimension count. It does not derive the
composition rule from the framework axioms.
"""

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


def self_adjoint_dim_complex(n: int) -> int:
    return n * n


def complex_dim_matrix_algebra(n: int) -> int:
    return n * n


def self_adjoint_dim_real(n: int) -> int:
    return n * (n + 1) // 2


def main() -> int:
    sigma0 = eye(2)
    sigma1 = Matrix([[0, 1], [1, 0]])
    sigma2 = Matrix([[0, -I], [I, 0]])
    sigma3 = Matrix([[1, 0], [0, -1]])

    check(
        "M1 dim_R(M_n(C)_sa) = n^2 = dim_C(M_n(C)) for n=2,3,4",
        all(
            self_adjoint_dim_complex(n) == complex_dim_matrix_algebra(n)
            for n in (2, 3, 4)
        ),
    )

    a, b, c, d, e, f, g, h = sp.symbols("a b c d e f g h", real=True)
    matrix = Matrix([[a + I * b, c + I * d], [e + I * f, g + I * h]])
    h1 = (matrix + matrix.conjugate().T) / 2
    h2 = (matrix - matrix.conjugate().T) / (2 * I)
    check(
        "M1b M = H1 + i H2 with H1,H2 self-adjoint",
        sp.simplify(matrix - (h1 + I * h2)) == zeros(2, 2)
        and sp.simplify(h1 - h1.conjugate().T) == zeros(2, 2)
        and sp.simplify(h2 - h2.conjugate().T) == zeros(2, 2),
    )

    check(
        "M2 ordinary complex two-qubit tensor product has local-tomography dimension 16 = 4*4",
        self_adjoint_dim_complex(4)
        == self_adjoint_dim_complex(2) * self_adjoint_dim_complex(2),
    )

    check(
        "M3 ordinary real rebit tensor product fails local tomography: 9 != 10",
        self_adjoint_dim_real(2) ** 2 == 9 and self_adjoint_dim_real(4) == 10,
    )

    left_i = kron(I * sigma0, sigma0)
    right_i = kron(sigma0, I * sigma0)
    global_i = I * eye(4)
    check(
        "M4 shared scalar i: (iI2) tensor I2 = I2 tensor (iI2) = iI4",
        sp.simplify(left_i - global_i) == zeros(4, 4)
        and sp.simplify(right_i - global_i) == zeros(4, 4),
    )

    pauli_basis = [sigma0, sigma1, sigma2, sigma3]
    products = [kron(x, y) for x in pauli_basis for y in pauli_basis]
    flattened = Matrix.hstack(*[product.reshape(16, 1) for product in products])
    check(
        "M5 Pauli products span M_4(C): 16 products, rank 16",
        flattened.rank() == 16,
    )

    check(
        "M6 sigma1 sigma2 sigma3 = i I2",
        sp.simplify(sigma1 * sigma2 * sigma3 - I * sigma0) == zeros(2, 2),
    )

    passed = sum(1 for _, ok in RESULTS if ok)
    failed = len(RESULTS) - passed
    for label, ok in RESULTS:
        print(("PASS" if ok else "FAIL") + " - " + label)
    print()
    print(f"{passed} PASS, {failed} FAIL")
    print(
        "Conditional result: ordinary shared-scalar complex matrix tensor "
        "products are locally tomographic by dimension count. The runner does "
        "not derive the composition premise from Lattice, Quantum, or Record."
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
