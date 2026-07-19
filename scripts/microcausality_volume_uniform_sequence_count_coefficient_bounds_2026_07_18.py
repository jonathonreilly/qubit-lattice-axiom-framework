#!/usr/bin/env python3
"""Exact checks for the volume-uniform sequence-count bounds note."""

import itertools

import sympy as sp


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, label, condition):
        ok = bool(condition)
        if ok:
            self.passed += 1
            print(f"PASS: {label}")
        else:
            self.failed += 1
            print(f"FAIL: {label}")

    def finish(self):
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
LOCAL_COORDINATION = 6


def kron(*mats):
    out = mats[0]
    for mat in mats[1:]:
        out = sp.Matrix(sp.kronecker_product(out, mat))
    return out


def com(a, b):
    return a * b - b * a


def is_zero(matrix):
    return sp.simplify(matrix) == sp.zeros(*matrix.shape)


def op_norm_sq(matrix):
    return max((matrix.H * matrix).eigenvals())


def op_norm(matrix):
    return sp.sqrt(op_norm_sq(matrix))


def product_majorant(m_sites, order):
    return sp.prod(
        LOCAL_COORDINATION * (m_sites + step)
        for step in range(order)
    )


def coefficient_majorant(a_norm, b_norm, j_bound, order, sequence_count):
    return (
        2
        * a_norm
        * b_norm
        * (2 * j_bound) ** order
        * sequence_count
    )


def majorant_term(a_norm, b_norm, j_star, time_abs, m_sites, order):
    return (
        2
        * a_norm
        * b_norm
        * (2 * j_star) ** order
        * product_majorant(m_sites, order)
        * sp.Abs(time_abs) ** order
        / sp.factorial(order)
    )


def ratio_majorant(j_star, time_abs, m_sites, order):
    return (
        12
        * j_star
        * sp.Abs(time_abs)
        * sp.Rational(m_sites + order, order + 1)
    )


def sufficient_window(j_star, m_sites, distance):
    if j_star == 0:
        raise ValueError("the positive-coupling window formula excludes J_*=0")
    return sp.Rational(distance + 1, 12 * j_star * (m_sites + distance))


def family_bound_is_finite(values):
    return bool(values) and all(sp.sympify(value).is_finite is True for value in values)


def local_tail_bound(a_norm, b_norm, j_star, time_abs, m_sites, distance):
    if distance < 0:
        raise ValueError("distance must be a finite nonnegative integer")
    if a_norm == 0 or b_norm == 0:
        return sp.Integer(0)
    if j_star == 0 or time_abs == 0:
        return 2 * a_norm * b_norm if distance == 0 else sp.Integer(0)
    ratio = ratio_majorant(j_star, time_abs, m_sites, distance)
    if ratio >= 1:
        raise ValueError("outside the certified local window")
    return sp.simplify(
        majorant_term(
            a_norm,
            b_norm,
            j_star,
            time_abs,
            m_sites,
            distance,
        )
        / (1 - ratio)
    )


def main():
    checks = CheckRunner()

    bond = {1: kron(SX, SX, I2), 2: kron(I2, SZ, SZ)}
    hamiltonian = bond[1] + bond[2]
    site_a = kron(SZ, I2, I2)
    probe_x3 = kron(I2, I2, SX)
    probe_y3 = kron(I2, I2, SY)
    probe_z3 = kron(I2, I2, SZ)
    probes = (probe_x3, probe_y3, probe_z3)

    def nested(sequence, operator):
        for label in reversed(sequence):
            operator = com(bond[label], operator)
        return operator

    def adjoint_power(order):
        operator = site_a
        for _ in range(order):
            operator = com(hamiltonian, operator)
        return operator

    # W1 -- ordered sequence expansion.
    for order in (2, 3):
        sequence_sum = sum(
            (
                nested(sequence, site_a)
                for sequence in itertools.product((1, 2), repeat=order)
            ),
            sp.zeros(8),
        )
        checks.check(
            f"W1-k{order} ordered sequence sum equals the nested adjoint",
            is_zero(adjoint_power(order) - sequence_sum),
        )

    # W2 -- dead sequences, below-cone recovery, and the disconnected case.
    checks.check(
        "W2a inner-miss sequences vanish exactly",
        is_zero(nested((1, 2), site_a))
        and is_zero(nested((2, 2), site_a)),
    )
    bond4_12 = kron(SX, SX, I2, I2)
    bond4_34 = kron(I2, I2, SZ, SZ)
    site4_a = kron(SZ, I2, I2, I2)
    checks.check(
        "W2b a later bond missing the current support kills the word",
        is_zero(com(bond4_34, com(bond4_12, site4_a))),
    )
    checks.check(
        "W2c every length-one word is below the distance-two cone",
        all(
            is_zero(com(nested((label,), site_a), probe))
            for label in (1, 2)
            for probe in probes
        ),
    )
    disconnected_h = bond[1]
    disconnected_terms = []
    operator = site_a
    for _ in range(9):
        disconnected_terms.append(operator)
        operator = com(disconnected_h, operator)
    checks.check(
        "W2d a disconnected far site remains silent through order eight",
        all(is_zero(com(term, probe)) for term in disconnected_terms for probe in probes),
    )

    # W3 -- local incidence count, N_0, product, recurrence, and actual words.
    unit_vectors = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

    def incident_bonds(sites):
        bonds = set()
        for site in sites:
            for vector in unit_vectors:
                plus = tuple(a + b for a, b in zip(site, vector))
                minus = tuple(a - b for a, b in zip(site, vector))
                bonds.add(tuple(sorted((site, plus))))
                bonds.add(tuple(sorted((minus, site))))
        return bonds

    single = incident_bonds([(0, 0, 0)])
    pair = incident_bonds([(0, 0, 0), (1, 0, 0)])
    triple = incident_bonds([(0, 0, 0), (1, 0, 0), (2, 0, 0)])
    checks.check(
        "W3a exact incidence counts obey the local 6s bound",
        len(single) == 6
        and len(pair) == 11
        and len(triple) == 16
        and len(single) <= 6
        and len(pair) <= 12
        and len(triple) <= 18,
    )
    checks.check(
        "W3b N_0 and independent product-majorant values are exact",
        product_majorant(1, 0) == 1
        and product_majorant(1, 1) == 6
        and product_majorant(1, 2) == 72
        and product_majorant(1, 3) == 1296
        and product_majorant(2, 2) == 216,
    )
    checks.check(
        "W3c the product majorant satisfies bar_N_{k+1}=6(m+k)bar_N_k",
        all(
            product_majorant(m_sites, order + 1)
            == 6 * (m_sites + order) * product_majorant(m_sites, order)
            for m_sites in range(1, 5)
            for order in range(6)
        ),
    )
    surviving = {
        order: sum(
            not is_zero(nested(sequence, site_a))
            for sequence in itertools.product((1, 2), repeat=order)
        )
        for order in range(1, 5)
    }
    checks.check(
        "W3d exact survivor counts lie below the product majorant",
        surviving == {1: 1, 2: 2, 3: 2, 4: 4}
        and all(
            surviving[order] <= product_majorant(1, order)
            for order in surviving
        ),
    )

    # W4 -- exact coefficients, actual-count bound, and reach/retreat/re-arrival.
    ad1 = adjoint_power(1)
    ad2 = adjoint_power(2)
    ad3 = adjoint_power(3)
    ad4 = adjoint_power(4)
    expected_yxi = kron(SY, SX, I2)
    expected_yyz = kron(SY, SY, SZ)
    checks.check(
        "W4a exact adjoints through order four match the Pauli-word derivation",
        ad1 == -2 * sp.I * expected_yxi
        and ad2 == 4 * site_a + 4 * expected_yyz
        and ad3 == -16 * sp.I * expected_yxi
        and ad4 == 32 * site_a + 32 * expected_yyz,
    )
    coefficient_norm = op_norm(com(ad2, probe_x3))
    actual_count_bound = coefficient_majorant(1, 1, 1, 2, surviving[2])
    product_count_bound = coefficient_majorant(
        1,
        1,
        1,
        2,
        product_majorant(1, 2),
    )
    checks.check(
        "W4b the k=2 coefficient obeys actual- and product-count bounds",
        coefficient_norm == 8
        and actual_count_bound == 16
        and product_count_bound == 576
        and coefficient_norm <= actual_count_bound <= product_count_bound,
    )
    checks.check(
        "W4c order two reaches X3 and Y3 while Z3 stays silent",
        not is_zero(com(ad2, probe_x3))
        and not is_zero(com(ad2, probe_y3))
        and is_zero(com(ad2, probe_z3)),
    )
    order3_terms = [
        nested(sequence, site_a)
        for sequence in itertools.product((1, 2), repeat=3)
    ]
    checks.check(
        "W4d every order-three word and their sum are silent for all far probes",
        all(is_zero(com(term, probe)) for term in order3_terms for probe in probes)
        and all(is_zero(com(ad3, probe)) for probe in probes),
    )
    checks.check(
        "W4e order four re-arrives at X3 and Y3 while Z3 stays silent",
        not is_zero(com(ad4, probe_x3))
        and not is_zero(com(ad4, probe_y3))
        and is_zero(com(ad4, probe_z3)),
    )

    # W5 -- independent ratio, window, family, tail, and boundary checks.
    m_sym, k_sym = sp.symbols("m_sym k_sym", positive=True)
    monotonicity = sp.expand(
        (m_sym + k_sym) * (k_sym + 2)
        - (m_sym + k_sym + 1) * (k_sym + 1)
    )
    checks.check(
        "W5a ratio monotonicity reduces exactly to m-1",
        sp.simplify(monotonicity - (m_sym - 1)) == 0,
    )
    j_value = sp.Rational(2, 3)
    time_value = sp.Rational(3, 40)
    checks.check(
        "W5b consecutive product-majorant terms have the stated ratio",
        all(
            sp.simplify(
                majorant_term(1, 1, j_value, time_value, m_sites, order + 1)
                / majorant_term(1, 1, j_value, time_value, m_sites, order)
                - ratio_majorant(j_value, time_value, m_sites, order)
            )
            == 0
            for m_sites in range(1, 5)
            for order in range(5)
        ),
    )
    checks.check(
        "W5c an independent ratio instance fixes the coefficient 12",
        ratio_majorant(2, sp.Rational(1, 120), 3, 4) == sp.Rational(7, 25),
    )
    window = sufficient_window(1, 1, 2)
    half_window = window / 2
    checks.check(
        "W5d the sufficient window has constant 12 and half-window ratio one-half",
        window == sp.Rational(1, 12)
        and half_window == sp.Rational(1, 24)
        and ratio_majorant(1, half_window, 1, 2) == sp.Rational(1, 2),
    )
    ratio = ratio_majorant(1, half_window, 1, 2)
    partial_tail = sum(
        majorant_term(1, 1, 1, half_window, 1, order)
        for order in range(2, 13)
    )
    closed_bound = local_tail_bound(1, 1, 1, half_window, 1, 2)
    checks.check(
        "W5e exact partial tail is below bar_a_d/(1-r_*)",
        ratio == sp.Rational(1, 2)
        and closed_bound == 1
        and partial_tail < closed_bound
        and all(
            ratio_majorant(1, half_window, 1, order) <= ratio
            for order in range(2, 13)
        ),
    )
    checks.check(
        "W5f family-level uniformity requires a finite J_*",
        family_bound_is_finite([sp.Rational(1, 3), 2, 5])
        and not family_bound_is_finite([1, sp.oo])
        and not family_bound_is_finite([]),
    )
    checks.check(
        "W5g d=0, zero-norm, zero-time, and zero-coupling cases are separate",
        local_tail_bound(1, 1, 1, 0, 1, 0) == 2
        and local_tail_bound(1, 1, 1, 0, 1, 2) == 0
        and local_tail_bound(1, 1, 0, 5, 1, 0) == 2
        and local_tail_bound(1, 1, 0, 5, 1, 2) == 0
        and local_tail_bound(0, 1, 1, sp.Rational(1, 100), 1, 2) == 0,
    )
    checks.check(
        "W5h a zero sequence count forces every recurrence majorant afterward to zero",
        all(6 * (m_sites + order) * 0 == 0 for m_sites in range(1, 5) for order in range(6)),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
