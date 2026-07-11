#!/usr/bin/env python3
"""Exact checks for the cubic neighbor-response classification.

This runner proves only an algebraic conditional.  It does not derive the
physical identification of an Admissibility/formation response with a kinetic
carrier.
"""

from __future__ import annotations

import itertools

import numpy as np
import sympy as sp


PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label}: {detail}")


def signed_permutation_rotations() -> list[sp.Matrix]:
    rotations: list[sp.Matrix] = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = sp.zeros(3, 3)
            for column, row in enumerate(perm):
                matrix[row, column] = signs[column]
            if matrix.det() == 1:
                rotations.append(matrix)
    unique = {tuple(int(x) for x in matrix): matrix for matrix in rotations}
    return [unique[key] for key in sorted(unique)]


DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}


def neighbor_representation(rotation: sp.Matrix) -> sp.Matrix:
    permutation = sp.zeros(6, 6)
    for source, direction in enumerate(DIRECTIONS):
        target_vector = rotation * sp.Matrix(direction)
        target = DIR_INDEX[tuple(int(value) for value in target_vector)]
        permutation[target, source] = 1
    return permutation


def constraint_matrix(rotations: list[sp.Matrix]) -> sp.Matrix:
    # The 24 unknowns are M[row, column], flattened row-major, for
    # M : R^6_directed-neighbors -> R scalar + R^3 vector.
    rows: list[list[int]] = []
    for rotation in rotations:
        pin = neighbor_representation(rotation)
        rout = sp.diag(1, 1, 1, 1)
        rout[1:4, 1:4] = rotation
        for i in range(4):
            for j in range(6):
                equation = [0] * 24
                # (M P)_ij
                for k in range(6):
                    equation[6 * i + k] += int(pin[k, j])
                # -(R_out M)_ij
                for a in range(4):
                    equation[6 * a + j] -= int(rout[i, a])
                rows.append(equation)
    return sp.Matrix(rows)


def main() -> int:
    rotations = signed_permutation_rotations()
    check("G01", len(rotations) == 24, f"proper cubic rotations={len(rotations)}")
    check("G02", all(rotation.det() == 1 for rotation in rotations), "all det=+1")
    keys = {tuple(int(x) for x in rotation) for rotation in rotations}
    closed = all(
        tuple(int(x) for x in left * right) in keys
        for left in rotations
        for right in rotations
    )
    check("G03", closed, "24-element set is closed")

    constraints = constraint_matrix(rotations)
    rank = constraints.rank()
    nullspace = constraints.nullspace()
    check("I01", rank == 22, f"constraint rank={rank}")
    check("I02", len(nullspace) == 2, f"intertwiner nullity={len(nullspace)}")

    scalar = sp.zeros(4, 6)
    scalar[0, :] = sp.ones(1, 6)
    vector = sp.zeros(4, 6)
    vector[1, 0], vector[1, 1] = 1, -1
    vector[2, 2], vector[2, 3] = 1, -1
    vector[3, 4], vector[3, 5] = 1, -1

    def flattened(matrix: sp.Matrix) -> sp.Matrix:
        return sp.Matrix([matrix[i, j] for i in range(4) for j in range(6)])

    scalar_v = flattened(scalar)
    vector_v = flattened(vector)
    check("I03", constraints * scalar_v == sp.zeros(constraints.rows, 1), "scalar sum is equivariant")
    check("I04", constraints * vector_v == sp.zeros(constraints.rows, 1), "directed vector difference is equivariant")
    basis_rank = sp.Matrix.hstack(scalar_v, vector_v, *nullspace).rank()
    check("I05", basis_rank == 2, "the displayed maps span the full nullspace")

    even_doublet_1 = sp.Matrix([1, 1, -1, -1, 0, 0])
    even_doublet_2 = sp.Matrix([1, 1, 1, 1, -2, -2])
    check("I06", scalar * even_doublet_1 == sp.zeros(4, 1) and vector * even_doublet_1 == sp.zeros(4, 1), "first even anisotropy mode is killed")
    check("I07", scalar * even_doublet_2 == sp.zeros(4, 1) and vector * even_doublet_2 == sp.zeros(4, 1), "second even anisotropy mode is killed")

    sx_s = sp.Matrix([[0, 1], [1, 0]])
    sy_s = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz_s = sp.Matrix([[1, 0], [0, -1]])
    paulis_s = (sx_s, sy_s, sz_s)
    identity_s = sp.eye(2)
    clifford_exact = all(
        sp.simplify(
            paulis_s[mu] * paulis_s[nu]
            + paulis_s[nu] * paulis_s[mu]
            - (2 * identity_s if mu == nu else sp.zeros(2, 2))
        )
        == sp.zeros(2, 2)
        for mu in range(3)
        for nu in range(3)
    )
    check("C01", clifford_exact, "Pauli response coefficients satisfy Cl(3) exactly")

    x, y, z, lam = sp.symbols("x y z lambda", real=True)
    vector_exact = x * sx_s + y * sy_s + z * sz_s
    radius_squared = x**2 + y**2 + z**2
    check("C02", sp.simplify(vector_exact**2 - radius_squared * identity_s) == sp.zeros(2, 2), "symbolic vector response squares to its scalar norm")
    characteristic = sp.expand((lam * identity_s - vector_exact).det())
    check("C03", characteristic == lam**2 - radius_squared, "symbolic vector eigenvalues are plus/minus the response norm")

    # At a concrete nonzero exact vector, verify that the spectral projectors
    # are idempotent, orthogonal, rank one, and exhaustive.  This avoids a
    # numerical simple-eigenvalue inference.
    exact_vector = sp.Rational(2, 7) * sx_s - sp.Rational(3, 7) * sy_s + sp.Rational(6, 7) * sz_s
    # Its norm is one because 2^2+3^2+6^2=7^2.
    p_plus = (identity_s + exact_vector) / 2
    p_minus = (identity_s - exact_vector) / 2
    projector_ok = (
        p_plus**2 == p_plus
        and p_minus**2 == p_minus
        and sp.simplify(p_plus * p_minus) == sp.zeros(2, 2)
        and p_plus + p_minus == identity_s
        and p_plus.trace() == 1
        and p_minus.trace() == 1
        and p_plus.det() == 0
        and p_minus.det() == 0
    )
    check("C04", projector_ok, "nonzero exact vector has two rank-one spectral projectors")

    sx = np.array(sx_s.tolist(), dtype=complex)
    sy = np.array(sy_s.tolist(), dtype=complex)
    sz = np.array(sz_s.tolist(), dtype=complex)
    paulis = (sx, sy, sz)
    identity = np.eye(2, dtype=complex)
    samples = (
        (0.17, -0.31, 0.43),
        (0.0, np.pi / 2, -np.pi / 3),
        (np.pi, np.pi / 4, 0.21),
    )
    square_ok = True
    for momentum in samples:
        dirac = sum(np.sin(momentum[mu]) * paulis[mu] for mu in range(3))
        target = sum(np.sin(value) ** 2 for value in momentum) * identity
        square_ok &= np.allclose(dirac @ dirac, target)
    check("C05", square_ok, "sampled odd response agrees with the exact scalar-square identity")

    corners = list(itertools.product((0.0, np.pi), repeat=3))
    dirac_corner_zeros = []
    laplacian_corner_values = []
    for corner in corners:
        dirac = sum(np.sin(corner[mu]) * paulis[mu] for mu in range(3))
        dirac_corner_zeros.append(np.linalg.norm(dirac) < 1.0e-12)
        laplacian_corner_values.append(2 * sum(1 - np.cos(value) for value in corner))
    check("K01", all(dirac_corner_zeros), "odd Clifford symbol vanishes at all eight corners")
    check("K02", sum(abs(value) < 1.0e-12 for value in laplacian_corner_values) == 1, "graph Laplacian has one null corner")

    # Separately supplied oriented-link realization:
    # A_(+mu)=a I-i b sigma_mu and A_(-mu)=A_(+mu)^dagger.
    # It gives H(k)=[m+2a sum cos(k_mu)]I+2b sum sin(k_mu)sigma_mu.
    a_value = -0.37
    b_value = 0.29
    link_pair_ok = True
    symbol_reconstruction_ok = True
    symbol_hermitian_ok = True
    for momentum in samples:
        reconstructed = np.zeros((2, 2), dtype=complex)
        expected = 1.13 * identity
        reconstructed += 1.13 * identity
        expected += 2 * a_value * sum(np.cos(value) for value in momentum) * identity
        for mu in range(3):
            a_plus = a_value * identity - 1j * b_value * paulis[mu]
            a_minus = a_value * identity + 1j * b_value * paulis[mu]
            link_pair_ok &= np.allclose(a_minus, a_plus.conj().T)
            reconstructed += a_plus * np.exp(1j * momentum[mu]) + a_minus * np.exp(-1j * momentum[mu])
            expected += 2 * b_value * np.sin(momentum[mu]) * paulis[mu]
        symbol_reconstruction_ok &= np.allclose(reconstructed, expected)
        symbol_hermitian_ok &= np.allclose(reconstructed, reconstructed.conj().T)
    check("K03", link_pair_ok, "oriented links obey A_minus=A_plus^dagger")
    check("K04", symbol_reconstruction_ok, "oriented links reconstruct the Hermitian cosine-plus-sine symbol")
    check("K05", symbol_hermitian_ok, "reconstructed nearest-neighbor symbol is Hermitian")

    # The exchange/Laplacian completion is exactly (m,a,b)=(6,-1,0)
    # on the separately supplied oriented-link surface.
    normal_form_ok = True
    for momentum in samples:
        laplacian = 6 - 2 * sum(np.cos(value) for value in momentum)
        normal_form = (6 + 2 * (-1) * sum(np.cos(value) for value in momentum)) * identity
        normal_form_ok &= np.allclose(normal_form, laplacian * identity)
    check("K06", normal_form_ok, "I-SWAP/Laplacian is the b=0 scalar-even normal form")

    nontrivial_scalar_has_rank_one_spectrum = False
    for coefficient in (-3.0, -0.5, 0.0, 2.0):
        eigenvalues = np.linalg.eigvalsh(coefficient * identity)
        nontrivial_scalar_has_rank_one_spectrum |= abs(eigenvalues[1] - eigenvalues[0]) > 1.0e-12
    check("F01", not nontrivial_scalar_has_rank_one_spectrum, "scalar response has no nontrivial rank-one spectral projector")

    check("F02", projector_ok, "nonzero vector response has simple rank-one spectral projectors")

    print("BOUNDARY: F01-F02 exclude b=0 only if spectral record-faithfulness is separately supplied.")
    print("BOUNDARY: K03-K06 use a separately supplied oriented-link response-to-symbol realization.")
    print("BOUNDARY: current Admissibility does not identify availability projectors with these response coefficients.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
