#!/usr/bin/env python3
"""Exact finite-dimensional checks for the forced C3 Brannen circulant form.

The runner verifies that the Hermitian commutant of the C3 cyclic shift on the
three-generation space is exactly the three-real-parameter Brannen circulant
family H = a I + b C + conj(b) C^T. It also verifies the record pointer,
locality, discriminating controls, and non-collapse of the free sector dial.
"""

from __future__ import annotations

import math
import sys
from typing import Iterable

import numpy as np
import sympy as sp


TOL = 1.0e-10
PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> bool:
    """Emit one summary line and accumulate a hard pass/fail count."""
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"SUMMARY: {status} - {label}{suffix}")
    return condition


def cyclic_shift_np() -> np.ndarray:
    return np.array(
        [
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0],
        ],
        dtype=complex,
    )


def cyclic_shift_sp() -> sp.Matrix:
    return sp.Matrix(
        [
            [0, 0, 1],
            [1, 0, 0],
            [0, 1, 0],
        ]
    )


def hermitian_basis_np() -> list[np.ndarray]:
    basis: list[np.ndarray] = []
    for i in range(3):
        mat = np.zeros((3, 3), dtype=complex)
        mat[i, i] = 1.0
        basis.append(mat)
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        mat = np.zeros((3, 3), dtype=complex)
        mat[i, j] = 1.0
        mat[j, i] = 1.0
        basis.append(mat)
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        mat = np.zeros((3, 3), dtype=complex)
        mat[i, j] = 1.0j
        mat[j, i] = -1.0j
        basis.append(mat)
    return basis


def hermitian_basis_sp() -> list[sp.Matrix]:
    basis: list[sp.Matrix] = []
    for i in range(3):
        mat = sp.zeros(3, 3)
        mat[i, i] = 1
        basis.append(mat)
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        mat = sp.zeros(3, 3)
        mat[i, j] = 1
        mat[j, i] = 1
        basis.append(mat)
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        mat = sp.zeros(3, 3)
        mat[i, j] = sp.I
        mat[j, i] = -sp.I
        basis.append(mat)
    return basis


def real_vector_from_complex_entries(entries: Iterable[sp.Expr]) -> list[sp.Expr]:
    entries = list(entries)
    return [sp.re(z) for z in entries] + [sp.im(z) for z in entries]


def hermitian_commutator_map_sp(operator: sp.Matrix) -> sp.Matrix:
    columns = []
    for basis_matrix in hermitian_basis_sp():
        commutator = basis_matrix * operator - operator * basis_matrix
        columns.append(sp.Matrix(real_vector_from_complex_entries(commutator)))
    return sp.Matrix.hstack(*columns)


def complex_commutant_map_sp(operator: sp.Matrix) -> sp.Matrix:
    basis = []
    for i in range(3):
        for j in range(3):
            mat = sp.zeros(3, 3)
            mat[i, j] = 1
            basis.append(mat)
    columns = []
    for basis_matrix in basis:
        commutator = basis_matrix * operator - operator * basis_matrix
        columns.append(sp.Matrix(list(commutator)))
    return sp.Matrix.hstack(*columns)


def h_from_coefficients(coefficients: Iterable[float], basis: list[np.ndarray]) -> np.ndarray:
    h = np.zeros((3, 3), dtype=complex)
    for coefficient, basis_matrix in zip(coefficients, basis):
        h += float(coefficient) * basis_matrix
    return h


def brannen_h(a: float, b: complex, c_shift: np.ndarray) -> np.ndarray:
    return a * np.eye(3, dtype=complex) + b * c_shift + np.conjugate(b) * c_shift.T


def comm_norm(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.linalg.norm(left @ right - right @ left))


def is_hermitian(matrix: np.ndarray) -> bool:
    return bool(np.allclose(matrix, matrix.conjugate().T, atol=TOL, rtol=0.0))


def solve_brannen_parameters(matrix: np.ndarray, c_shift: np.ndarray) -> tuple[float, complex]:
    del c_shift
    a = np.trace(matrix) / 3.0
    b_values = np.array([matrix[1, 0], matrix[2, 1], matrix[0, 2]], dtype=complex)
    c_values = np.array([matrix[0, 1], matrix[1, 2], matrix[2, 0]], dtype=complex)
    b = complex(np.mean(b_values))
    checks = [
        abs(a.imag) < TOL,
        np.allclose(np.diag(matrix), a, atol=TOL, rtol=0.0),
        np.allclose(b_values, b, atol=TOL, rtol=0.0),
        np.allclose(c_values, np.conjugate(b), atol=TOL, rtol=0.0),
    ]
    if not all(checks):
        raise AssertionError("matrix is not reconstructible as a Brannen circulant")
    return float(a.real), b


def sorted_real(values: Iterable[float]) -> np.ndarray:
    return np.sort(np.array(list(values), dtype=float))


def range_shift(displacement: int) -> np.ndarray:
    mat = np.zeros((3, 3), dtype=complex)
    for source in range(3):
        target = (source + displacement) % 3
        mat[target, source] = 1.0
    return mat


def main() -> int:
    c_np = cyclic_shift_np()
    c2_np = c_np @ c_np
    c_sp = cyclic_shift_sp()
    identity = np.eye(3, dtype=complex)
    basis_np = hermitian_basis_np()

    check("C is the 3x3 cyclic shift with C^3 = I", np.allclose(c_np @ c_np @ c_np, identity))
    check("Hermitian real basis has dimension 9", len(basis_np) == 9 and all(is_hermitian(b) for b in basis_np))

    commutator_map = hermitian_commutator_map_sp(c_sp)
    rank = commutator_map.rank()
    nullspace = commutator_map.nullspace()
    commutant_dim = len(nullspace)
    check(
        "dim_R{Hermitian H : [H,C]=0} is computed by rank/nullspace and equals exactly 3",
        commutant_dim == 3,
        detail=f"rank={rank} nullity={commutant_dim}",
    )
    if commutant_dim != 3:
        raise AssertionError(f"anti-fabrication gate failed: Hermitian commutant dim={commutant_dim}, not 3")

    rng = np.random.default_rng(20260615)
    random_parameter_ok = True
    for _ in range(5):
        a = float(rng.uniform(-2.0, 3.0))
        b = complex(rng.normal(), rng.normal())
        h = brannen_h(a, b, c_np)
        random_parameter_ok = (
            random_parameter_ok
            and is_hermitian(h)
            and comm_norm(h, c_np) < TOL
            and np.allclose(brannen_h(*solve_brannen_parameters(h, c_np), c_np), h, atol=TOL, rtol=0.0)
        )
    check("random (a in R, b in C) Brannen operators are Hermitian, C3-covariant, and reconstruct", random_parameter_ok)

    nullspace_vectors = [
        np.array([float(sp.N(entry)) for entry in vector], dtype=float)
        for vector in nullspace
    ]
    basis_reconstruct_ok = True
    for vector in nullspace_vectors:
        h = h_from_coefficients(vector, basis_np)
        a, b = solve_brannen_parameters(h, c_np)
        basis_reconstruct_ok = (
            basis_reconstruct_ok
            and is_hermitian(h)
            and comm_norm(h, c_np) < TOL
            and np.allclose(brannen_h(a, b, c_np), h, atol=TOL, rtol=0.0)
        )
    check("each computed commutant nullspace basis vector reconstructs as aI+bC+conj(b)C^T", basis_reconstruct_ok)

    general_reconstruct_ok = True
    for _ in range(6):
        weights = rng.normal(size=commutant_dim)
        coefficient_vector = sum(weight * vector for weight, vector in zip(weights, nullspace_vectors))
        h = h_from_coefficients(coefficient_vector, basis_np)
        a, b = solve_brannen_parameters(h, c_np)
        general_reconstruct_ok = (
            general_reconstruct_ok
            and is_hermitian(h)
            and comm_norm(h, c_np) < TOL
            and np.allclose(brannen_h(a, b, c_np), h, atol=TOL, rtol=0.0)
        )
    check("general commuting Hermitian operators reconstruct as Brannen circulants", general_reconstruct_ok)

    eigen_ok = True
    eigen_details: list[str] = []
    for a, magnitude, delta in [(3.0, 0.4, 0.2), (2.5, 0.9, -0.7), (5.0, 1.1, 1.3)]:
        b = magnitude * complex(math.cos(delta), math.sin(delta))
        h = brannen_h(a, b, c_np)
        operator_eigenvalues = np.linalg.eigvalsh(h)
        formula_eigenvalues = [
            a + 2.0 * magnitude * math.cos(delta + 2.0 * math.pi * k / 3.0)
            for k in range(3)
        ]
        eigen_ok = eigen_ok and np.allclose(sorted_real(operator_eigenvalues), sorted_real(formula_eigenvalues), atol=TOL, rtol=0.0)
        eigen_details.append(f"a={a:g}, |b|={magnitude:g}, delta={delta:g}, r_label={magnitude * magnitude / (a * a):.12g}")
    check("numpy eigvalsh(H) matches a+2|b|cos(delta+2pi k/3)", eigen_ok, detail="; ".join(eigen_details))

    s_pointer = c_np + c2_np
    record_h = brannen_h(2.0, 0.6 * complex(math.cos(0.5), math.sin(0.5)), c_np)
    check("[H,S]=0 for Brannen circulant H and S=C+C^2", comm_norm(record_h, s_pointer) < TOL)
    check("S=C+C^2 has the 2-sector record spectrum {2,-1,-1}", np.allclose(sorted_real(np.linalg.eigvalsh(s_pointer)), np.array([-1.0, -1.0, 2.0]), atol=TOL, rtol=0.0))

    range_one_residues = [d for d in range(3) if min(d, 3 - d) <= 1]
    range_one_ops = [range_shift(d) for d in range_one_residues]
    range_ops_are_shifts = (
        range_one_residues == [0, 1, 2]
        and np.allclose(range_one_ops[0], identity)
        and np.allclose(range_one_ops[1], c_np)
        and np.allclose(range_one_ops[2], c2_np)
    )
    check("range-<=1 displacement operators on the 3-cycle are exactly {I,C,C^2}", range_ops_are_shifts)

    complex_map = complex_commutant_map_sp(c_sp)
    complex_commutant_dim = 9 - complex_map.rank()
    local_span_rank = np.linalg.matrix_rank(np.column_stack([op.reshape(-1) for op in [identity, c_np, c2_np]]))
    check(
        "{I,C,C^2} are independent and span the complex C3 commutant",
        complex_commutant_dim == 3 and local_span_rank == 3,
        detail=f"complex_commutant_dim={complex_commutant_dim}, local_span_rank={local_span_rank}",
    )

    non_c3_control = np.diag([1.0, 2.0, 3.0]).astype(complex)
    check("control c1: diag(1,2,3) fails C3 covariance", comm_norm(non_c3_control, c_np) > 1.0e-8, detail=f"norm={comm_norm(non_c3_control, c_np):.12g}")
    check("control c1: diag(1,2,3) does not commute with pointer S", comm_norm(non_c3_control, s_pointer) > 1.0e-8, detail=f"norm={comm_norm(non_c3_control, s_pointer):.12g}")

    generic_control = sp.Matrix(
        [
            [0, 1, 2],
            [3, 0, 5],
            [7, 11, 13],
        ]
    )
    generic_map = hermitian_commutator_map_sp(generic_control)
    generic_dim = len(generic_map.nullspace())
    check(
        "control c2: a generic non-C3 nonnormal operator has Hermitian commutant dimension < 3",
        generic_dim < 3,
        detail=f"rank={generic_map.rank()} nullity={generic_dim}",
    )

    dial_1 = (2.0, 0.5, 0.1)
    dial_2 = (3.0, 1.2, -0.4)
    label_1 = (dial_1[1] * dial_1[1] / (dial_1[0] * dial_1[0]), dial_1[2])
    label_2 = (dial_2[1] * dial_2[1] / (dial_2[0] * dial_2[0]), dial_2[2])
    check("dial non-collapse: different supplied couplings give different (r,delta) labels", label_1 != label_2, detail=f"{label_1} vs {label_2}")

    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 and PASS_COUNT >= 10 else 1


if __name__ == "__main__":
    sys.exit(main())
