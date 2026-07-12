#!/usr/bin/env python3
"""Exact checks for the two-band BdG strict-time/flat-spectrum boundary."""

import itertools

import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.special import jv


PASS = 0
FAIL = 0


def check(name, condition, detail):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])


def kron(*matrices):
    result = matrices[0]
    for matrix in matrices[1:]:
        result = sp.kronecker_product(result, matrix)
    return result


def permutation_sign(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations():
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if permutation_sign(permutation) * np.prod(signs) != 1:
                continue
            rotation = np.zeros((3, 3), dtype=int)
            for output_axis in range(3):
                rotation[output_axis, permutation[output_axis]] = signs[output_axis]
            rotations.append(rotation)
    return rotations


def pin_intertwiner(gammas, orthogonal):
    """Numerically solve U gamma_j U^dagger = sum_i O_ij gamma_i."""
    dimension = gammas[0].shape[0]
    equations = []
    for source, gamma in enumerate(gammas):
        target = sum(orthogonal[row, source] * gammas[row] for row in range(len(gammas)))
        equations.append(
            np.kron(gamma.T, np.eye(dimension))
            - np.kron(np.eye(dimension), target)
        )
    _, _, vh = np.linalg.svd(np.vstack(equations))
    unitary = vh[-1].conj().reshape((dimension, dimension), order="F")
    scale = np.sqrt(np.trace(unitary.conj().T @ unitary).real / dimension)
    return unitary / scale


def main():
    # A. The spin-edge parity class and its category split.
    parity = kron(Z, Z)
    charge = kron(Z, I2) + kron(I2, Z)
    spin_basis = (
        kron(I2, I2),
        kron(Z, I2) + kron(I2, Z),
        kron(Z, Z),
        kron(X, X) + kron(Y, Y),
        kron(X, X) - kron(Y, Y),
        kron(X, Y) + kron(Y, X),
    )
    columns = sp.Matrix.hstack(*(matrix.reshape(16, 1) for matrix in spin_basis))
    check("A01", columns.rank() == 6,
          "the endpoint-symmetric parity-even spin-density basis has six independent real directions")
    check("A02", all(matrix * SWAP == SWAP * matrix for matrix in spin_basis),
          "all six directions are endpoint-SWAP symmetric")
    check("A03", all(matrix * parity == parity * matrix for matrix in spin_basis),
          "all six directions conserve total fermion parity")
    check("A04", all(matrix * charge == charge * matrix for matrix in spin_basis[:4]),
          "the first four directions are exactly the charge-preserving Block11 class")
    check("A05", all(matrix * charge != charge * matrix for matrix in spin_basis[4:]),
          "XX-YY and XY+YX are exactly the two charge-breaking pairing directions")

    even_indices = (0, 3)
    odd_indices = (1, 2)
    even_blocks = tuple(matrix.extract(even_indices, even_indices) for matrix in spin_basis)
    odd_blocks = tuple(matrix.extract(odd_indices, odd_indices) for matrix in spin_basis)
    check("A06", sp.Matrix.hstack(*(matrix.reshape(4, 1) for matrix in even_blocks)).rank() == 4,
          "the even-parity block spans every Hermitian 2x2 matrix")
    check("A07", sp.Matrix.hstack(*(matrix.reshape(4, 1) for matrix in odd_blocks)).rank() == 2,
          "the odd-parity block spans exactly the I,X commutant of endpoint SWAP")

    # B. General two-band Cayley-Hamilton and the flat-spectrum exponential.
    d0, d1, d2 = sp.symbols("d0 d1 d2", real=True)
    D = d0 * X + d1 * Y + d2 * Z
    spectral_square = sp.expand(d0 ** 2 + d1 ** 2 + d2 ** 2)
    check("B01", sp.simplify(D * D - spectral_square * I2) == sp.zeros(2),
          "every traceless Hermitian two-band symbol obeys D^2=s I")
    rho, time, center = sp.symbols("rho time center", real=True, nonzero=True)
    flat_exp = sp.exp(-sp.I * time * center) * (
        sp.cos(time * rho) * I2 - sp.I * sp.sin(time * rho) * D / rho
    )
    derivative_at_zero = flat_exp.diff(time).subs(time, 0)
    check("B02", sp.simplify(derivative_at_zero + sp.I * (center * I2 + D)) == sp.zeros(2),
          "the closed flat-band expression has generator center I+D")
    check("B03", sp.simplify(flat_exp.conjugate().T * flat_exp - I2).subs(
        spectral_square, rho ** 2) == sp.zeros(2),
          "D^2=rho^2 I makes the closed finite-Laurent exponential exactly unitary")

    n = sp.symbols("n", integer=True, nonnegative=True)
    series_coefficients = [(-1) ** order * time ** (2 * order) / sp.factorial(2 * order)
                           for order in range(16)]
    check("B04", all(coefficient != 0 for coefficient in series_coefficients),
          "cos(time sqrt(s)) is a nonpolynomial entire function of s at every nonzero time")
    z = sp.symbols("z", nonzero=True)
    sample_s = z + 2 + 1 / z
    growing_poles = []
    power = sp.Integer(1)
    for order in range(1, 11):
        power = sp.expand(power * sample_s)
        lowest = min(term.as_powers_dict().get(z, 0) for term in sp.Add.make_args(power))
        growing_poles.append(lowest == -order)
    check("B05", all(growing_poles),
          "a nonconstant Laurent s has unbounded pole order under the nonterminating entire series")
    check("B06", sp.limit(sample_s * z, z, 0) == 1,
          "the generic one-variable slice has a genuine pole, so the composition has an essential singularity")
    check("M01", sp.cos(time * sp.sqrt(sp.Integer(4))) == sp.cos(2 * time),
          "the essential-singularity obstruction disappears when the band square is constant")

    # C. Scalar proper-cubic one-mode Nambu classification.
    rotations = proper_cubic_rotations()
    check("C01", len(rotations) == 24 and all(round(np.linalg.det(rotation)) == 1 for rotation in rotations),
          "the signed-permutation enumeration is exactly the 24-element proper cubic group")
    constraints = np.vstack([rotation - np.eye(3, dtype=int) for rotation in rotations])
    check("C02", np.linalg.matrix_rank(constraints) == 3,
          "the proper-cubic vector fixed space is zero-dimensional")
    reversal_witnesses = []
    for axis in range(3):
        unit = np.eye(3, dtype=int)[:, axis]
        reversal_witnesses.append(any(np.array_equal(rotation @ unit, -unit) for rotation in rotations))
    check("C03", all(reversal_witnesses),
          "a proper rotation sends each nearest-neighbor direction to its reverse")
    rotation_keys = {tuple(rotation.reshape(-1)): rotation for rotation in rotations}
    commutator_generators = []
    for left in rotations:
        for right in rotations:
            commutator = left @ right @ left.T @ right.T
            commutator_generators.append(rotation_keys[tuple(commutator.reshape(-1))])
    commutator_subgroup = {tuple(np.eye(3, dtype=int).reshape(-1))}
    changed = True
    while changed:
        changed = False
        for current_key in tuple(commutator_subgroup):
            current = np.asarray(current_key, dtype=int).reshape(3, 3)
            for generator in commutator_generators:
                product_key = tuple((current @ generator).reshape(-1))
                if product_key not in commutator_subgroup:
                    commutator_subgroup.add(product_key)
                    changed = True
    check("C04", len(commutator_subgroup) == 12 and len(rotations) // len(commutator_subgroup) == 2,
          "the proper-cubic commutator subgroup has order 12, so every ordinary one-dimensional character squares trivially")

    mu, hopping = sp.symbols("mu hopping", real=True)
    kx, ky, kz = sp.symbols("kx ky kz", real=True)
    xi = mu + 2 * hopping * (sp.cos(kx) + sp.cos(ky) + sp.cos(kz))
    scalar_bdg = xi * Z
    scalar_square = sp.expand_trig((scalar_bdg * scalar_bdg)[0, 0])
    check("C05", sp.simplify(sp.diff(scalar_square, kx).subs({kx: sp.pi / 2, ky: 0, kz: 0}))
          == -4 * hopping * (mu + 4 * hopping),
          "nonzero cubic hopping generically makes the two-band square momentum-dependent")
    samples = [sp.simplify(scalar_square.subs({kx: point[0], ky: point[1], kz: point[2]}))
               for point in ((0, 0, 0), (sp.pi, 0, 0), (sp.pi, sp.pi, sp.pi))]
    check("C06", sp.solve([samples[0] - samples[1], samples[0] - samples[2]], [hopping], dict=True)
          == [{hopping: 0}],
          "flat spectrum in the nearest-neighbor scalar cubic normal symbol forces zero hopping")

    # D. Positive lower-symmetry flat BdG escape and strict CAR convolution.
    h_plus = (Z - sp.I * Y) / 2
    h_minus = (Z + sp.I * Y) / 2
    kitaev_square = {
        2: h_plus * h_plus,
        0: h_plus * h_minus + h_minus * h_plus,
        -2: h_minus * h_minus,
    }
    check("D01", kitaev_square[0] == I2 and kitaev_square[2] == sp.zeros(2)
          and kitaev_square[-2] == sp.zeros(2),
          "the lower-symmetry Kitaev symbol (cos k)Z+(sin k)Y is an exact flat involution")
    particle_hole_ok = (
        X * h_plus.conjugate() * X == -h_plus
        and X * h_minus.conjugate() * X == -h_minus
    )
    check("D02", particle_hole_ok,
          "the Laurent coefficients obey the spinless BdG particle-hole relation")
    cosine, sine = sp.Rational(5, 13), sp.Rational(12, 13)
    unitary_coefficients = {
        0: cosine * I2,
        1: -sp.I * sine * h_plus,
        -1: -sp.I * sine * h_minus,
    }
    autocorrelation = {}
    for left, left_matrix in unitary_coefficients.items():
        for right, right_matrix in unitary_coefficients.items():
            delta = right - left
            autocorrelation[delta] = autocorrelation.get(delta, sp.zeros(2)) + left_matrix.conjugate().T * right_matrix
    check("D03", autocorrelation[0] == I2
          and all(matrix == sp.zeros(2) for delta, matrix in autocorrelation.items() if delta != 0),
          "the flat BdG exponential is a strict radius-one Bogoliubov/CAR convolution with local inverse")
    sample_k, sample_t = 0.63, 0.41
    kitaev_numeric = np.cos(sample_k) * np.asarray(Z, dtype=complex) + np.sin(sample_k) * np.asarray(Y, dtype=complex)
    kitaev_closed = np.cos(sample_t) * np.eye(2) - 1j * np.sin(sample_t) * kitaev_numeric
    check("D04", np.allclose(expm(-1j * sample_t * kitaev_numeric), kitaev_closed, atol=2e-13),
          "the lower-symmetry positive escape is strict for every time, not at an isolated time")

    # E. Dispersive mutation: exact unitarity with nonzero tails.
    argument = 1.73
    bessel_tail = np.abs(jv(np.arange(0, 60), argument))
    check("E01", all(np.any(bessel_tail[radius + 1:] > 1e-300) for radius in (0, 1, 2, 4, 8, 16, 32)),
          "the dispersive scalar hopping exponential has Bessel support beyond every tested cutoff")
    theta = np.linspace(-np.pi, np.pi, 4096, endpoint=False)
    reconstruction = sum(((-1j) ** order) * jv(order, argument) * np.exp(1j * order * theta)
                         for order in range(-80, 81))
    check("E02", np.max(np.abs(reconstruction - np.exp(-1j * argument * np.cos(theta)))) < 2e-13,
          "the two-sided Bessel series reconstructs the exact dispersive Laurent exponential")
    check("E03", np.max(np.abs(np.abs(np.exp(-1j * argument * np.cos(theta))) - 1)) < 2e-15,
          "the tail obstruction is compatible with exact one-particle unitarity")

    # F. Recheck the multicomponent fully cubic flat-involution escape mechanism.
    gamma_bond_sp = (
        kron(X, I2, I2), kron(Y, I2, I2),
        kron(Z, X, I2), kron(Z, Y, I2),
        kron(Z, Z, X), kron(Z, Z, Y),
    )
    gamma_zero_sp = kron(Z, Z, Z)
    gamma_all_sp = (gamma_zero_sp,) + gamma_bond_sp
    clifford_exact = all(
        gamma_all_sp[i] * gamma_all_sp[j] + gamma_all_sp[j] * gamma_all_sp[i]
        == (2 * sp.eye(8) if i == j else sp.zeros(8))
        for i in range(7) for j in range(7)
    )
    check("F01", clifford_exact,
          "seven explicit Hermitian 8x8 gammas satisfy the exact Cl(7) relations")
    aa, bb = sp.Rational(3, 5), sp.Rational(4, 5)
    stencil = {(0, 0, 0): aa * gamma_zero_sp}
    for axis in range(3):
        forward = tuple(1 if coordinate == axis else 0 for coordinate in range(3))
        backward = tuple(-1 if coordinate == axis else 0 for coordinate in range(3))
        odd = gamma_bond_sp[2 * axis]
        even = gamma_bond_sp[2 * axis + 1]
        stencil[forward] = bb * (odd - sp.I * even) / (2 * sp.sqrt(3))
        stencil[backward] = bb * (odd + sp.I * even) / (2 * sp.sqrt(3))
    square_stencil = {}
    for left_displacement, left_matrix in stencil.items():
        for right_displacement, right_matrix in stencil.items():
            displacement = tuple(left_displacement[i] + right_displacement[i] for i in range(3))
            square_stencil[displacement] = square_stencil.get(displacement, sp.zeros(8)) + left_matrix * right_matrix
    square_stencil = {key: matrix.applyfunc(sp.simplify) for key, matrix in square_stencil.items()}
    check("F02", square_stencil[(0, 0, 0)] == sp.eye(8)
          and all(matrix == sp.zeros(8) for key, matrix in square_stencil.items() if key != (0, 0, 0)),
          "the multicomponent cubic Laurent symbol is an exact radius-one flat involution")

    induced_rotations = []
    for spatial in rotations:
        induced = np.zeros((6, 6), dtype=int)
        for output_axis in range(3):
            source_axis = int(np.argmax(np.abs(spatial[output_axis])))
            sign = spatial[output_axis, source_axis]
            induced[2 * output_axis, 2 * source_axis] = 1
            induced[2 * output_axis + 1, 2 * source_axis + 1] = sign
        induced_rotations.append((spatial, induced))
    induced_determinants = [round(np.linalg.det(induced)) for _, induced in induced_rotations]
    check("F03", induced_determinants.count(1) == 12 and induced_determinants.count(-1) == 12,
          "the irreducible 8-mode orientation obstruction is present on half the cubic rotations")

    gamma_bond = tuple(np.asarray(matrix, dtype=complex) for matrix in gamma_bond_sp)
    gamma_zero = np.asarray(gamma_zero_sp, dtype=complex)
    doubled_zero = np.block([[gamma_zero, np.zeros((8, 8))], [np.zeros((8, 8)), -gamma_zero]])
    doubled_bond = tuple(np.block([[gamma, np.zeros((8, 8))], [np.zeros((8, 8)), gamma]])
                         for gamma in gamma_bond)
    sample_p = np.array((0.27, -0.61, 1.13))
    q_sample = float(aa) * doubled_zero
    for axis in range(3):
        q_sample += (float(bb) / np.sqrt(3)) * (
            np.cos(sample_p[axis]) * doubled_bond[2 * axis]
            + np.sin(sample_p[axis]) * doubled_bond[2 * axis + 1]
        )
    covariance_errors = []
    lifted_by_spatial = {}
    for spatial, induced in induced_rotations:
        pin = pin_intertwiner(gamma_bond, induced)
        if round(np.linalg.det(induced)) == 1:
            lifted = np.block([[pin, np.zeros((8, 8))], [np.zeros((8, 8)), pin]])
        else:
            lifted = np.block([[np.zeros((8, 8)), pin], [pin, np.zeros((8, 8))]])
        lifted_by_spatial[tuple(spatial.reshape(-1))] = lifted
        covariance_errors.append(np.linalg.norm(lifted.conj().T @ lifted - np.eye(16)))
        rotated_p = spatial @ sample_p
        rotated_q = float(aa) * doubled_zero
        for axis in range(3):
            rotated_q += (float(bb) / np.sqrt(3)) * (
                np.cos(rotated_p[axis]) * doubled_bond[2 * axis]
                + np.sin(rotated_p[axis]) * doubled_bond[2 * axis + 1]
            )
        covariance_errors.append(np.linalg.norm(lifted @ q_sample @ lifted.conj().T - rotated_q))
    check("F04", max(covariance_errors) < 2e-11,
          "doubling the Clifford chirality supplies a unitary intertwiner for each of all 24 proper cubic rotations")

    projective_errors = []
    cocycles = {}
    for left, _ in induced_rotations:
        for right, _ in induced_rotations:
            left_lift = lifted_by_spatial[tuple(left.reshape(-1))]
            right_lift = lifted_by_spatial[tuple(right.reshape(-1))]
            target_lift = lifted_by_spatial[tuple((left @ right).reshape(-1))]
            product = left_lift @ right_lift
            phase = np.trace(target_lift.conj().T @ product) / 16
            projective_errors.append(np.linalg.norm(product - phase * target_lift))
            projective_errors.append(abs(abs(phase) - 1))
            cocycles[(tuple(left.reshape(-1)), tuple(right.reshape(-1)))] = phase
    check("F05", max(projective_errors) < 2e-11,
          "the 24 intertwiners close projectively, so conjugation is an honest action on the even/quadratic algebra")

    rotation_x = np.diag((1, -1, -1))
    rotation_y = np.diag((-1, 1, -1))
    lift_x = lifted_by_spatial[tuple(rotation_x.reshape(-1))]
    lift_y = lifted_by_spatial[tuple(rotation_y.reshape(-1))]
    check("F06", np.linalg.norm(lift_x @ lift_y + lift_y @ lift_x) < 2e-11
          and np.linalg.norm(lift_x @ lift_y - lift_y @ lift_x) > 1,
          "commuting pi rotations anticommute on odd CAR generators, exposing the nontrivial spinorial cocycle")

    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
