#!/usr/bin/env python3
"""Exact checks for the onsite-charge common-H strict-QCA dichotomy."""

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


def torus_edges(length):
    sites = tuple(itertools.product(range(length), repeat=3))
    index = {site: i for i, site in enumerate(sites)}
    edges = []
    for site in sites:
        for axis in range(3):
            neighbor = list(site)
            neighbor[axis] = (neighbor[axis] + 1) % length
            edges.append((index[site], index[tuple(neighbor)]))
    return sites, tuple(edges)


def permutation_sign(permutation):
    inversions = sum(permutation[i] > permutation[j]
                     for i in range(len(permutation)) for j in range(i + 1, len(permutation)))
    return -1 if inversions % 2 else 1


def pin_intertwiner(gammas, orthogonal):
    """Numerically solve U gamma_j U^dagger = sum_i O_ij gamma_i."""
    dimension = gammas[0].shape[0]
    equations = []
    for source, gamma in enumerate(gammas):
        target = sum(orthogonal[row, source] * gammas[row] for row in range(len(gammas)))
        equations.append(np.kron(gamma.T, np.eye(dimension)) - np.kron(np.eye(dimension), target))
    stacked = np.vstack(equations)
    _, _, vh = np.linalg.svd(stacked)
    unitary = vh[-1].conj().reshape((dimension, dimension), order="F")
    scale = np.sqrt(np.trace(unitary.conj().T @ unitary).real / dimension)
    return unitary / scale


def main():
    c, r, g, J = sp.symbols("c r g J", real=True)
    charge = kron(Z, I2) + kron(I2, Z)
    basis = (
        kron(I2, I2),
        kron(Z, I2) + kron(I2, Z),
        kron(Z, Z),
        kron(X, X) + kron(Y, Y),
    )
    columns = sp.Matrix.hstack(*(matrix.reshape(16, 1) for matrix in basis))
    check("A01", columns.rank() == 4,
          "the four normal-form operators are linearly independent")
    check("A02", all(matrix * SWAP == SWAP * matrix for matrix in basis),
          "all four operators are exactly endpoint-SWAP symmetric")
    check("A03", all(matrix * charge == charge * matrix for matrix in basis),
          "all four operators exactly conserve the supplied onsite charge")

    h = c * basis[0] + r * basis[1] + g * basis[2] + J * basis[3]
    one_block = h.extract([1, 2], [1, 2])
    check("A04", one_block == sp.Matrix([[c - g, 2 * J], [2 * J, c - g]]),
          "the charge-zero block is exactly (c-g)I+2J X")
    check("A05", h[0, 0] == c + 2 * r + g and h[3, 3] == c - 2 * r + g,
          "the one-dimensional charge sectors have the stated endpoint energies")

    e00, e11, a, b = sp.symbols("e00 e11 a b", real=True)
    general = sp.diag(e00, 0, 0, e11)
    general[1, 1] = a
    general[2, 2] = a
    general[1, 2] = b
    general[2, 1] = b
    substitutions = {
        c: (e00 + e11 + 2 * a) / 4,
        r: (e00 - e11) / 4,
        g: (e00 + e11 - 2 * a) / 4,
        J: b / 2,
    }
    check("A06", all(sp.simplify(value) == 0 for value in (h.subs(substitutions) - general)),
          "every Hermitian charge-block and SWAP-symmetric matrix reconstructs uniquely")
    mutation = kron(X, I2) + kron(I2, X)
    check("M01", mutation * SWAP == SWAP * mutation and mutation * charge != charge * mutation,
          "an endpoint-symmetric charge-breaking mutation is rejected by the theorem class")

    sites, edges = torus_edges(4)
    adjacency = sp.zeros(len(sites))
    degrees = [0] * len(sites)
    for first, second in edges:
        adjacency[first, second] += 1
        adjacency[second, first] += 1
        degrees[first] += 1
        degrees[second] += 1
    check("K01", len(edges) == 3 * len(sites) and set(degrees) == {6},
          "the cubic torus has 3|V| undirected edges and degree six")
    relative = -12 * (r + g) * sp.eye(len(sites)) + 2 * J * adjacency
    check("K02", relative[0, 0] == -12 * (r + g)
          and set(relative[0, j] for j in range(1, len(sites))) <= {0, 2 * J},
          "the one-particle restriction is E1 I+2J A with E1=-12(r+g)")
    # Independent assembly of the one-particle generator directly from the edge
    # density block entries -- vacuum-relative diagonal shift per incident edge
    # plus the off-diagonal hopping -- with no use of the asserted E1 formula.
    vacuum_edge_diag = h[0, 0]
    one_excited_edge_diag = h[1, 1]
    hopping_entry = h[1, 2]
    k_from_blocks = sp.zeros(len(sites))
    for site_index in range(len(sites)):
        k_from_blocks[site_index, site_index] = (
            degrees[site_index] * (one_excited_edge_diag - vacuum_edge_diag)
        )
    for first, second in edges:
        k_from_blocks[first, second] += hopping_entry
        k_from_blocks[second, first] += hopping_entry
    check("K02b", sp.simplify(k_from_blocks - relative) == sp.zeros(len(sites)),
          "the one-particle generator assembled from the edge-density blocks equals E1 I+2J A")

    momenta = [2 * np.pi * n / 4 for n in range(4)]
    numeric_adjacency = np.asarray(adjacency, dtype=float)
    adjacency_spectrum = np.sort(np.linalg.eigvalsh(numeric_adjacency))
    bloch_spectrum = np.sort([
        2 * sum(np.cos(k) for k in ks)
        for ks in itertools.product(momenta, repeat=3)
    ])
    check("K03", np.allclose(adjacency_spectrum, bloch_spectrum, atol=2e-12),
          "finite-torus diagonalization matches 2 sum_mu cos(k_mu)")
    h12 = kron(h, I2)
    h23 = kron(I2, h)
    overlap_commutator = h12 * h23 - h23 * h12
    check("K04", overlap_commutator[4, 1] == 4 * J ** 2
          and overlap_commutator[1, 4] == -4 * J ** 2,
          "the three-site outer-hop overlap commutator has exact entries +/-4J^2")

    phi = sp.eye(4) - SWAP
    phi_expected = sp.Rational(1, 2) * basis[0] - sp.Rational(1, 2) * basis[2] - sp.Rational(1, 2) * basis[3]
    check("C01", phi == phi_expected,
          "I-SWAP has exact coefficients (c,r,g,J)=(1/2,0,-1/2,-1/2)")
    phi_block = phi.extract([1, 2], [1, 2])
    check("C02", phi_block == sp.Matrix([[1, -1], [-1, 1]]),
          "the I-SWAP edge restricts to the two-site graph Laplacian")
    laplacian = 6 * sp.eye(len(sites)) - adjacency
    phi_relative = relative.subs({r: 0, g: -sp.Rational(1, 2), J: -sp.Rational(1, 2)})
    check("C03", phi_relative == laplacian,
          "the cubic I-SWAP one-particle generator is exactly 6I-A")

    z, tau, hop = sp.symbols("z tau hop", nonzero=True)
    slice_exponent = -sp.I * 2 * hop * tau * (z + 1 / z)
    check("L01", sp.limit(slice_exponent * z, z, 0) == -2 * sp.I * hop * tau,
          "the exponent has a nonzero z^-1 principal coefficient when Jt is nonzero")
    w = sp.symbols("w", positive=True)
    at_infinity = sp.expand(slice_exponent.subs(z, 1 / w))
    check("L02", sp.limit(at_infinity * w, w, 0) == -2 * sp.I * hop * tau,
          "after z=1/w the exponent has a nonzero w^-1 coefficient at infinity")
    negative_tail = [sp.expand((-2 * sp.I * hop * tau) ** n / sp.factorial(n)) for n in range(1, 13)]
    check("L03", all(value != 0 for value in negative_tail),
          "exp(-2iJt/z) has certified nonzero z^-n coefficients through every symbolic test order")
    finite_mutation = sp.exp(slice_exponent.subs(hop, 0))
    check("M02", finite_mutation == 1,
          "the essential-singularity obstruction disappears exactly on the J=0 mutation")

    for argument in (0.7, 1.9, 4.2):
        orders = np.arange(0, 45)
        coefficients = np.abs(jv(orders, argument))
        tail_nonzero = all(np.any(coefficients[R + 1:] > 1e-300) for R in (0, 1, 2, 4, 8, 16, 24))
        check(f"B{argument}", tail_nonzero,
              f"Bessel coefficients at argument {argument} survive beyond every tested cutoff")
    argument = 2.3
    theta = np.linspace(-np.pi, np.pi, 4096, endpoint=False)
    reconstruction = sum(((-1j) ** n) * jv(n, argument) * np.exp(1j * n * theta)
                         for n in range(-80, 81))
    check("B04", np.max(np.abs(reconstruction - np.exp(-1j * argument * np.cos(theta)))) < 2e-13,
          "the two-sided Bessel generating series reconstructs the Laurent exponential")
    threshold_ok = True
    for argument in (0.7, 1.9, 4.2, 11.0):
        # Fixed threshold from the closed-form bound, not incremented until it holds.
        threshold_order = int(np.ceil(argument ** 2 / (4 * np.log(2))))
        for n in range(threshold_order, threshold_order + 24):
            closed_form_bound = np.exp(argument ** 2 / (4 * (n + 1))) - 1
            # Exact relative tail sum_{m>=1} (x^2/4)^m n!/(m!(n+m)!), computed
            # term by term and therefore independent of the closed-form bound.
            actual_relative_tail = 0.0
            term = 1.0
            for m in range(1, 400):
                term *= (argument ** 2 / 4) / (m * (n + m))
                actual_relative_tail += term
                if term < 1e-18:
                    break
            # (i) the closed form really bounds the exact tail; (ii) that bound is
            # below one at and above the threshold, so the leading term dominates;
            # (iii) hence J_n(x) is nonzero.
            threshold_ok &= actual_relative_tail <= closed_form_bound + 1e-12
            threshold_ok &= closed_form_bound < 1.0
            threshold_ok &= abs(jv(n, argument)) > 0
    check("B05", threshold_ok,
          "the exact relative Bessel tail stays below exp[x^2/(4(n+1))]-1<1 for n>=x^2/(4 log 2), so leading-term dominance certifies eventual nonzero support")

    length = 18
    ring_adjacency = np.zeros((length, length), dtype=complex)
    for x in range(length):
        ring_adjacency[x, (x + 1) % length] = 1
        ring_adjacency[(x + 1) % length, x] = 1
    time = 0.37
    hopping = 0.8
    propagator = expm(-1j * time * 2 * hopping * ring_adjacency)
    distances = np.array([min(x, length - x) for x in range(length)])
    check("Q01", all(np.any(np.abs(propagator[distances > radius, 0]) > 1e-14) for radius in (0, 1, 2, 3, 4, 5)),
          "a large-torus sample has exact-flow leakage beyond every tested local radius")
    check("Q02", np.allclose(propagator.conj().T @ propagator, np.eye(length), atol=2e-12),
          "the leaking one-particle evolution remains unitary")

    theta_symbol = sp.symbols("theta", real=True)
    Sminus = sp.Matrix([[0, 0], [1, 0]])
    zz = kron(Z, Z)
    plus = sp.diag(*(sp.exp(sp.I * theta_symbol * zz[i, i]) for i in range(4)))
    minus = sp.diag(*(sp.exp(-sp.I * theta_symbol * zz[i, i]) for i in range(4)))
    image = plus * kron(Sminus, I2) * minus
    expected = kron(Sminus, sp.diag(sp.exp(-2 * sp.I * theta_symbol), sp.exp(2 * sp.I * theta_symbol)))
    check("R01", all(sp.simplify(value) == 0 for value in (image - expected)),
          "the J=0 interaction sends a ladder operator to one neighbor factor")
    exceptional = [sp.simplify(sp.exp(-2 * sp.I * (sp.pi * n / 2) * Z)) for n in range(4)]
    check("R02", all(matrix == ((-1) ** n) * I2 for n, matrix in enumerate(exceptional)),
          "gt in (pi/2)Z gives radius zero in the commuting branch")
    # Radius-one iff sin(2gt)!=0, tested at both scalar (sin=0) and non-scalar
    # (sin!=0) times: the neighbor factor exp(-2i gt Z) is proportional to I iff
    # its two diagonal phases agree, i.e. iff sin(2gt)=0.
    radius_one_iff_ok = True
    gt_values = (
        [sp.pi * k / 2 for k in range(4)]
        + [sp.Rational(j, 5) for j in range(1, 6)]
        + [sp.pi / 3, sp.pi / 6]
    )
    for gt_value in gt_values:
        neighbor_factor = sp.diag(sp.exp(-2 * sp.I * gt_value), sp.exp(2 * sp.I * gt_value))
        factor_is_scalar = sp.simplify(neighbor_factor[0, 0] - neighbor_factor[1, 1]) == 0
        sine_is_zero = sp.simplify(sp.sin(2 * gt_value)) == 0
        radius_one_iff_ok &= factor_is_scalar == sine_is_zero
    check("R03", radius_one_iff_ok,
          "the commuting-branch neighbor factor is scalar iff sin(2gt)=0, so exact radius is one iff sin(2gt)!=0")

    # Positive escape outside the headline one-qubit/U(1) class.
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
    check("E01", clifford_exact,
          "seven explicit Hermitian 8x8 gammas satisfy the exact Cl(7) relations")

    aa, bb = sp.symbols("aa bb", real=True)
    stencil = {(0, 0, 0): aa * gamma_zero_sp}
    for axis in range(3):
        forward = [0, 0, 0]
        forward[axis] = 1
        backward = [0, 0, 0]
        backward[axis] = -1
        odd = gamma_bond_sp[2 * axis]
        even = gamma_bond_sp[2 * axis + 1]
        stencil[tuple(forward)] = bb * (odd - sp.I * even) / (2 * sp.sqrt(3))
        stencil[tuple(backward)] = bb * (odd + sp.I * even) / (2 * sp.sqrt(3))
    square_stencil = {}
    for left_displacement, left_matrix in stencil.items():
        for right_displacement, right_matrix in stencil.items():
            displacement = tuple(left_displacement[i] + right_displacement[i] for i in range(3))
            square_stencil[displacement] = square_stencil.get(displacement, sp.zeros(8)) + left_matrix * right_matrix
    square_stencil = {key: matrix.applyfunc(sp.simplify) for key, matrix in square_stencil.items()}
    check("E02", square_stencil[(0, 0, 0)] == (aa ** 2 + bb ** 2) * sp.eye(8)
          and all(matrix == sp.zeros(8) for key, matrix in square_stencil.items() if key != (0, 0, 0)),
          "the flat symbol q has exact Laurent identity q^2=(a^2+b^2)I")

    onsite = aa * gamma_zero_sp
    first_bond = stencil[(1, 0, 0)]
    commutator = (onsite * first_bond - first_bond * onsite).applyfunc(sp.simplify)
    check("E03", commutator != sp.zeros(8),
          "for ab nonzero the onsite and nearest-neighbor pieces do not commute")

    gamma_bond = tuple(np.asarray(matrix, dtype=complex) for matrix in gamma_bond_sp)
    gamma_zero = np.asarray(gamma_zero_sp, dtype=complex)
    sample_a, sample_b, sample_t = 0.6, 0.8, 0.371
    sample_p = (0.27, -0.61, 1.13)
    q_sample = sample_a * gamma_zero
    for axis in range(3):
        q_sample += (sample_b / np.sqrt(3)) * (
            np.cos(sample_p[axis]) * gamma_bond[2 * axis]
            + np.sin(sample_p[axis]) * gamma_bond[2 * axis + 1]
        )
    closed_exp = np.cos(sample_t) * np.eye(8) - 1j * np.sin(sample_t) * q_sample
    check("E04", np.allclose(expm(-1j * sample_t * q_sample), closed_exp, atol=2e-12),
          "exp(-itq)=cos(t)I-i sin(t)q, giving radius at most one for all t and exact one at this sample")

    volume = gamma_zero_sp
    for gamma in gamma_bond_sp:
        volume *= gamma
    volume_scalar = volume[0, 0]
    check("E05", volume == volume_scalar * sp.eye(8) and volume_scalar != 0,
          "the irreducible 8-mode Cl(7) volume element is a nonzero central scalar")

    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if permutation_sign(permutation) * np.prod(signs) != 1:
                continue
            spatial = np.zeros((3, 3), dtype=int)
            induced = np.zeros((6, 6), dtype=int)
            for output_axis in range(3):
                source_axis = permutation[output_axis]
                spatial[output_axis, source_axis] = signs[output_axis]
                induced[2 * output_axis, 2 * source_axis] = 1
                induced[2 * output_axis + 1, 2 * source_axis + 1] = signs[output_axis]
            rotations.append((spatial, induced))
    determinants = [round(np.linalg.det(induced)) for _, induced in rotations]
    check("E06", len(rotations) == 24 and determinants.count(1) == 12 and determinants.count(-1) == 12,
          "all 24 proper cubic rotations induce twelve even and twelve odd signed-pair maps")
    check("E07", any(det == -1 for det in determinants) and volume_scalar != -volume_scalar,
          "the odd signed-pair maps cannot fix Gamma0 in one irreducible 8-mode Cl(7) carrier")

    doubled_zero = np.block([[gamma_zero, np.zeros((8, 8))], [np.zeros((8, 8)), -gamma_zero]])
    doubled_bond = tuple(np.block([[gamma, np.zeros((8, 8))], [np.zeros((8, 8)), gamma]])
                         for gamma in gamma_bond)
    covariance_errors = []
    unitarity_errors = []
    doubled_q_sample = sample_a * doubled_zero
    for axis in range(3):
        doubled_q_sample += (sample_b / np.sqrt(3)) * (
            np.cos(sample_p[axis]) * doubled_bond[2 * axis]
            + np.sin(sample_p[axis]) * doubled_bond[2 * axis + 1]
        )
    for spatial, induced in rotations:
        pin = pin_intertwiner(gamma_bond, induced)
        if round(np.linalg.det(induced)) == 1:
            lifted = np.block([[pin, np.zeros((8, 8))], [np.zeros((8, 8)), pin]])
        else:
            lifted = np.block([[np.zeros((8, 8)), pin], [pin, np.zeros((8, 8))]])
        unitarity_errors.append(np.linalg.norm(lifted.conj().T @ lifted - np.eye(16)))
        covariance_errors.append(np.linalg.norm(lifted @ doubled_zero @ lifted.conj().T - doubled_zero))
        for source, gamma in enumerate(doubled_bond):
            target = sum(induced[row, source] * doubled_bond[row] for row in range(6))
            covariance_errors.append(np.linalg.norm(lifted @ gamma @ lifted.conj().T - target))
        rotated_p = spatial @ np.asarray(sample_p)
        rotated_q = sample_a * doubled_zero
        for axis in range(3):
            rotated_q += (sample_b / np.sqrt(3)) * (
                np.cos(rotated_p[axis]) * doubled_bond[2 * axis]
                + np.sin(rotated_p[axis]) * doubled_bond[2 * axis + 1]
            )
        covariance_errors.append(np.linalg.norm(lifted @ doubled_q_sample @ lifted.conj().T - rotated_q))
    check("E08", max(unitarity_errors) < 2e-12,
          "the doubled-carrier Pin intertwiners are unitary for all 24 rotations")
    check("E09", max(covariance_errors) < 2e-11,
          "the 16-mode doubled-chirality repair is covariant for all 24 proper cubic rotations")

    doubled_zero_exact = sp.diag(gamma_zero_sp, -gamma_zero_sp)
    doubled_bond_exact = tuple(sp.diag(gamma, gamma) for gamma in gamma_bond_sp)
    flat_coefficients = {(0, 0, 0): sp.Rational(3, 5) * doubled_zero_exact}
    for axis in range(3):
        forward = tuple(1 if coordinate == axis else 0 for coordinate in range(3))
        backward = tuple(-1 if coordinate == axis else 0 for coordinate in range(3))
        odd = doubled_bond_exact[2 * axis]
        even = doubled_bond_exact[2 * axis + 1]
        flat_coefficients[forward] = sp.Rational(2, 5) * (odd - sp.I * even) / sp.sqrt(3)
        flat_coefficients[backward] = sp.Rational(2, 5) * (odd + sp.I * even) / sp.sqrt(3)
    hermitian_coefficients = all(
        flat_coefficients[tuple(-entry for entry in displacement)]
        == matrix.conjugate().T
        for displacement, matrix in flat_coefficients.items()
    )
    check("E10", hermitian_coefficients,
          "the doubled 16-mode Laurent coefficients define a Hermitian finite-range quadratic CAR Hamiltonian")

    cosine, sine = sp.Rational(5, 13), sp.Rational(12, 13)
    unitary_coefficients = {
        displacement: (-sp.I * sine * matrix)
        for displacement, matrix in flat_coefficients.items()
    }
    unitary_coefficients[(0, 0, 0)] += cosine * sp.eye(16)
    autocorrelation = {}
    for left_displacement, left_matrix in unitary_coefficients.items():
        for right_displacement, right_matrix in unitary_coefficients.items():
            delta = tuple(right_displacement[i] - left_displacement[i] for i in range(3))
            autocorrelation[delta] = autocorrelation.get(delta, sp.zeros(16)) + left_matrix.conjugate().T * right_matrix
    autocorrelation = {key: matrix.applyfunc(sp.simplify) for key, matrix in autocorrelation.items()}
    car_unitary = autocorrelation[(0, 0, 0)] == sp.eye(16) and all(
        matrix == sp.zeros(16) for key, matrix in autocorrelation.items() if key != (0, 0, 0)
    )
    check("E11", car_unitary and 2 ** 16 == 65536,
          "the radius-one coefficient convolution preserves CAR with inverse at the same radius; local Fock dimension is 2^16")

    two_mode_annihilators = (kron(Sminus, I2), kron(Z, Sminus))
    bilinear_identity = True
    for creator_index, annihilator_index, probe_index in itertools.product(range(2), repeat=3):
        bilinear = two_mode_annihilators[creator_index].conjugate().T * two_mode_annihilators[annihilator_index]
        commutator_value = bilinear * two_mode_annihilators[probe_index] - two_mode_annihilators[probe_index] * bilinear
        expected_value = (-two_mode_annihilators[annihilator_index]
                          if creator_index == probe_index else sp.zeros(4))
        bilinear_identity &= commutator_value == expected_value
    representative_bond = flat_coefficients[(1, 0, 0)]
    transposition_is_load_bearing = representative_bond.T != representative_bond
    check("E12", bilinear_identity and transposition_is_load_bearing,
          "the exact CAR bilinear commutator fixes the transposed coefficient in H_flat and generates the displayed U_t derivative")

    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
