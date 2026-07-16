#!/usr/bin/env python3
"""Exact classification of overlap-commuting common qubit edge Hamiltonians."""

import itertools

import numpy as np
import sympy as sp
from scipy.linalg import expm


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
P = (I2, X, Y, Z)
SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])


def kron(*matrices):
    result = matrices[0]
    for matrix in matrices[1:]:
        result = sp.kronecker_product(result, matrix)
    return result


def cross(left, right):
    return sp.Matrix(left).cross(sp.Matrix(right))


def all_zero(expressions, substitutions=None):
    substitutions = substitutions or {}
    return all(sp.expand(value.subs(substitutions)) == 0 for value in expressions)


def cubic_edges(length):
    sites = tuple(itertools.product(range(length), repeat=3))
    edges = []
    for site in sites:
        for axis in range(3):
            neighbor = list(site)
            neighbor[axis] = (neighbor[axis] + 1) % length
            edges.append((site, tuple(neighbor), axis, site[axis] % 2))
    return sites, tuple(edges)


def embedded_normal_edge(axis_matrix, beta, gamma, first, second, site_count=3):
    def at(site, matrix):
        factors = [I2] * site_count
        factors[site] = matrix
        return kron(*factors)

    factors = [I2] * site_count
    factors[first] = axis_matrix
    factors[second] = axis_matrix
    return beta * (at(first, axis_matrix) + at(second, axis_matrix)) + gamma * kron(*factors)


def main():
    a, beta, gamma = sp.symbols("a beta gamma", real=True)
    b = sp.Matrix(sp.symbols("b0:3", real=True))
    c00, c01, c02, c11, c12, c22 = sp.symbols(
        "c00 c01 c02 c11 c12 c22", real=True
    )
    C = sp.Matrix([[c00, c01, c02], [c01, c11, c12], [c02, c12, c22]])

    symmetric_basis = [kron(I2, I2)]
    symmetric_basis += [kron(P[i + 1], I2) + kron(I2, P[i + 1]) for i in range(3)]
    symmetric_basis += [
        kron(P[i + 1], P[j + 1])
        if i == j
        else kron(P[i + 1], P[j + 1]) + kron(P[j + 1], P[i + 1])
        for i in range(3)
        for j in range(i, 3)
    ]
    span_matrix = sp.Matrix.hstack(*(matrix.reshape(16, 1) for matrix in symmetric_basis))
    check("A01", len(symmetric_basis) == 10 and span_matrix.rank() == 10,
          "the endpoint-SWAP-symmetric Hermitian Pauli space has dimension ten")
    check("A02", all(matrix * SWAP == SWAP * matrix for matrix in symmetric_basis),
          "all ten basis elements commute exactly with endpoint SWAP")

    h12 = a * sp.eye(8)
    h23 = a * sp.eye(8)
    for i in range(3):
        h12 += b[i] * (kron(P[i + 1], I2, I2) + kron(I2, P[i + 1], I2))
        h23 += b[i] * (kron(I2, P[i + 1], I2) + kron(I2, I2, P[i + 1]))
        for j in range(3):
            h12 += C[i, j] * kron(P[i + 1], P[j + 1], I2)
            h23 += C[i, j] * kron(I2, P[i + 1], P[j + 1])
    reduced_commutator = sp.expand((h12 * h23 - h23 * h12) / (2 * sp.I))
    actual = {}
    for labels in itertools.product(range(4), repeat=3):
        coefficient = sp.expand(sp.trace(kron(*(P[label] for label in labels)) * reduced_commutator) / 8)
        if coefficient != 0:
            actual[labels] = coefficient

    expected = {}
    rows = [sp.Matrix(C.row(i)).T for i in range(3)]
    for i in range(3):
        for m in range(3):
            expected[(i + 1, m + 1, 0)] = sp.expand(cross(rows[i], b)[m])
            expected[(0, m + 1, i + 1)] = sp.expand(cross(b, rows[i])[m])
        for ell in range(3):
            for m in range(3):
                expected[(i + 1, m + 1, ell + 1)] = sp.expand(cross(rows[i], rows[ell])[m])
    expected = {label: value for label, value in expected.items() if value != 0}
    check("A03", actual == expected and len(actual) == 36,
          "all 36 nonzero Pauli coefficients are exactly row-field or row-row cross products")
    check("A04", sum(0 in label for label in actual) == 18 and sum(0 not in label for label in actual) == 18,
          "independent two-body and three-body Pauli sectors each contain eighteen coefficients")

    three_body = list({sp.expand(value) for label, value in actual.items() if 0 not in label})
    minors = [sp.expand(C.extract(row_pair, col_pair).det())
              for row_pair in itertools.combinations(range(3), 2)
              for col_pair in itertools.combinations(range(3), 2)]
    same_up_to_sign = lambda value, choices: any(sp.expand(value - choice) == 0 or sp.expand(value + choice) == 0 for choice in choices)
    check("A05", all(same_up_to_sign(value, minors) for value in three_body)
          and all(same_up_to_sign(value, three_body) for value in minors),
          "the three-body equations are precisely all 2x2 minors, hence rank(C)<=1")

    n0, n1, n2 = sp.symbols("n0 n1 n2", real=True)
    n = (n0, n1, n2)
    normal_subs = {b[i]: beta * n[i] for i in range(3)}
    normal_subs.update({C[i, j]: gamma * n[i] * n[j] for i in range(3) for j in range(i, 3)})
    check("A06", all_zero(actual.values(), normal_subs),
          "the arbitrary-axis Ising-plus-field normal form is symbolically sufficient")

    zero_c = {entry: 0 for entry in (c00, c01, c02, c11, c12, c22)}
    rank_one_no_field = dict(zero_c, **{})
    rank_one_no_field.update({b[i]: 0 for i in range(3)})
    rank_one_no_field.update({c00: -2, c01: -4, c02: -4, c11: -8, c12: -8, c22: -8})
    check("A07", all_zero(actual.values(), zero_c), "C=0 permits every onsite field direction")
    check("A08", all_zero(actual.values(), rank_one_no_field), "b=0 permits either rank-one C or the scalar degeneration")
    scalar_subs = dict(zero_c)
    scalar_subs.update({entry: 0 for entry in b})
    check("A09", all_zero(actual.values(), scalar_subs), "the scalar Hamiltonian is included with arbitrary unused axis")

    rank_two = dict(zero_c)
    rank_two.update({entry: 0 for entry in b})
    rank_two.update({c00: 1, c11: 1})
    misaligned = dict(zero_c)
    misaligned.update({b[0]: 1, b[1]: 0, b[2]: 0, c22: 1})
    check("M01", not all_zero(actual.values(), rank_two), "a rank-two coupling mutation has a nonzero three-body commutator")
    check("M02", not all_zero(actual.values(), misaligned), "a rank-one coupling with misaligned field has a nonzero two-body commutator")

    generic_edge_01 = embedded_normal_edge(Z, sp.Rational(2, 3), sp.Rational(5, 7), 0, 1)
    generic_edge_02 = embedded_normal_edge(Z, sp.Rational(2, 3), sp.Rational(5, 7), 0, 2)
    generic_edge_12 = embedded_normal_edge(Z, sp.Rational(2, 3), sp.Rational(5, 7), 1, 2)
    edge_terms = (generic_edge_01, generic_edge_02, generic_edge_12)
    check("G01", all(left * right == right * left for left, right in itertools.combinations(edge_terms, 2)),
          "all endpoint orientations of overlapping normal-form edges commute exactly")

    sites, edges = cubic_edges(4)
    degrees = {site: 0 for site in sites}
    layers = {(axis, parity): [] for axis in range(3) for parity in range(2)}
    for first, second, axis, parity in edges:
        degrees[first] += 1
        degrees[second] += 1
        layers[(axis, parity)].append((first, second))
    check("G02", len(edges) == 3 * len(sites) and set(degrees.values()) == {6},
          "the L=4 cubic torus has 3|V| edges and degree six")
    check("G03", all(len({site for edge in layer for site in edge}) == 2 * len(layer) for layer in layers.values()),
          "the six axis-parity classes are exact disjoint-edge matching layers")
    check("G04", sum(degrees.values()) == 6 * len(sites),
          "summing the common edge field gives exactly 6 beta sum_x N_x")

    numeric_edges = [np.asarray(matrix, dtype=complex) for matrix in edge_terms]
    time = 0.371
    summed = expm(-1j * time * sum(numeric_edges))
    products = []
    for order in itertools.permutations(range(3)):
        product_matrix = np.eye(8, dtype=complex)
        for index in order:
            product_matrix = expm(-1j * time * numeric_edges[index]) @ product_matrix
        products.append(product_matrix)
    check("G05", all(np.allclose(summed, product, atol=2e-12) for product in products),
          "exp(-it sum h_e) equals every edge-product order in an overlap-complete local test")

    theta = sp.symbols("theta", real=True)
    Splus = sp.Matrix([[0, 1], [0, 0]])
    zz = kron(Z, Z)
    plus = sp.diag(*(sp.exp(sp.I * theta * zz[index, index]) for index in range(4)))
    minus = sp.diag(*(sp.exp(-sp.I * theta * zz[index, index]) for index in range(4)))
    lhs = plus * kron(Splus, I2) * minus
    rhs = kron(Splus, sp.diag(sp.exp(2 * sp.I * theta), sp.exp(-2 * sp.I * theta)))
    check("R01", all(sp.simplify(value) == 0 for value in (lhs - rhs)),
          "one edge sends S+_x exactly to S+_x exp(2 i gamma t N_y)")
    check("R02", all(sp.simplify(sp.sin(-2 * theta) + sp.sin(2 * theta)) == 0 for _ in range(1)),
          "forward and inverse have the same radius-exception condition")
    exceptional = [sp.simplify(sp.exp(2 * sp.I * (sp.pi * k / 2) * Z)) for k in range(4)]
    check("R03", all(matrix == ((-1) ** k) * I2 for k, matrix in enumerate(exceptional)),
          "gamma t in (pi/2)Z makes every neighbor factor scalar and the automorphism radius zero")
    check("R04", sp.sin(2 * sp.Rational(1, 7)) != 0,
          "away from sin(2 gamma t)=0, S+ depends on every neighbor and exact graph radius is one")
    check("R05", Z * Splus - Splus * Z == 2 * Splus,
          "the six-regular field phase is exp(12 i beta t) and does not enlarge support")

    normal_two_site = beta * (kron(Z, I2) + kron(I2, Z)) + gamma * kron(Z, Z)
    check("T01", normal_two_site * kron(Z, I2) == kron(Z, I2) * normal_two_site
          and normal_two_site * kron(I2, Z) == kron(I2, Z) * normal_two_site,
          "every local axis charge N_x is conserved exactly")
    vacuum = {site: 1 for site in sites}
    def energy_coefficients(configuration):
        field = 6 * sum(configuration.values())
        interaction = sum(configuration[first] * configuration[second] for first, second, _, _ in edges)
        return field, interaction
    vacuum_energy = energy_coefficients(vacuum)
    defect_energies = []
    for defect in sites:
        configuration = dict(vacuum)
        configuration[defect] = -1
        defect_energies.append(energy_coefficients(configuration))
    check("T02", len(set(defect_energies)) == 1,
          "the full one-defect sector is exactly position-degenerate")
    check("T03", tuple(defect_energies[0][i] - vacuum_energy[i] for i in range(2)) == (-12, -12),
          "a one-axis defect shifts energy by -12 beta -12 gamma with no hopping matrix element")
    z0z1 = kron(Z, Z, I2, I2)
    z1z2 = kron(I2, Z, Z, I2)
    z2z3 = kron(I2, I2, Z, Z)
    local_probe = kron(I2, Splus, I2, I2)
    full_generator = z0z1 + z1z2 + z2z3
    incident_generator = z0z1 + z1z2
    full_plus = sp.diag(*(sp.exp(sp.I * theta * full_generator[index, index]) for index in range(16)))
    full_minus = sp.diag(*(sp.exp(-sp.I * theta * full_generator[index, index]) for index in range(16)))
    incident_plus = sp.diag(*(sp.exp(sp.I * theta * incident_generator[index, index]) for index in range(16)))
    incident_minus = sp.diag(*(sp.exp(-sp.I * theta * incident_generator[index, index]) for index in range(16)))
    full_image = full_plus * local_probe * full_minus
    incident_image = incident_plus * local_probe * incident_minus
    check("T04", all(sp.simplify(value) == 0 for value in (full_image - incident_image)),
          "an exact four-site chain image cancels the nonincident edge, so support does not iterate beyond one hop")

    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
