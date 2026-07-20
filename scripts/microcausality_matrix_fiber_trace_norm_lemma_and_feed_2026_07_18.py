#!/usr/bin/env python3
"""Exact checks for the matrix-fiber trace-norm lemma and activity feed."""

import itertools

import sympy as sp


EXPECTED_LABELS = [
    "pair-trace-norm-identity",
    "three-fiber-degenerate-case",
    "fiber-mode-rotation-car",
    "disjoint-hop-joint-spectrum",
    "onsite-subset-sum-bound",
    "trace-to-operator-envelope",
    "fiber-bilinear-evenness",
    "activity-envelope-formulas",
    "su2-fixed-fiber-values",
    "finite-open-ambient-metrics",
    "zero-activity-branch",
    "uniform-corollary-monotonicity",
]


class CheckRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.labels = []

    def check(self, label, condition):
        ok = bool(condition)
        self.labels.append(label.split()[0])
        if ok:
            self.passed += 1
            print(f"PASS: {label}")
        else:
            self.failed += 1
            print(f"FAIL: {label}")

    def finish(self):
        if self.labels != EXPECTED_LABELS:
            print(
                "FAIL: gate-manifest drift: labels "
                f"{self.labels} != expected {EXPECTED_LABELS}"
            )
            self.failed += 1
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


IDENTITY_2 = sp.eye(2)
ANNIHILATION = sp.Matrix([[0, 1], [0, 0]])
PARITY_Z = sp.Matrix([[1, 0], [0, -1]])


def kron(*matrices):
    result = matrices[0]
    for matrix in matrices[1:]:
        result = sp.Matrix(sp.kronecker_product(result, matrix))
    return result


def annihilation_at(mode, mode_count):
    return kron(
        *(
            [PARITY_Z] * mode
            + [ANNIHILATION]
            + [IDENTITY_2] * (mode_count - mode - 1)
        )
    )


def commutator(left, right):
    return left * right - right * left


def anticommutator(left, right):
    return left * right + right * left


def is_zero(matrix):
    return sp.simplify(matrix) == sp.zeros(*matrix.shape)


def operator_norm(matrix):
    return sp.sqrt(max((matrix.H * matrix).eigenvals()))


def main():
    checks = CheckRunner()

    mode_count = 4
    car = [annihilation_at(mode, mode_count) for mode in range(mode_count)]
    car_dagger = [operator.H for operator in car]

    def pair_term(fiber_matrix):
        directed = sp.zeros(2**mode_count, 2**mode_count)
        for left_fiber in range(2):
            for right_fiber in range(2):
                directed += (
                    fiber_matrix[left_fiber, right_fiber]
                    * car_dagger[left_fiber]
                    * car[2 + right_fiber]
                )
        return directed + directed.H

    pair_instances = [
        sp.Matrix([[1, 0], [0, 0]]),
        sp.Matrix([[0, 1], [0, 0]]),
        sp.Matrix([[1, 1], [0, 0]]),
        sp.eye(2),
        sp.Matrix([[1, 0], [0, 2]]),
        sp.Matrix([[1, 1], [1, -1]]),
        sp.Matrix([[2, 1], [0, 1]]),
        sp.Matrix([[sp.I, 1], [0, 2]]),
    ]
    pair_values_match = all(
        sp.simplify(
            operator_norm(pair_term(matrix))
            - sum(matrix.singular_values())
        )
        == 0
        for matrix in pair_instances
    )
    nonnormal_value = sp.simplify(
        operator_norm(pair_term(pair_instances[6]))
    )
    identity_value = sp.simplify(operator_norm(pair_term(sp.eye(2))))
    checks.check(
        "pair-trace-norm-identity eight matrices including complex and nonnormal cases",
        pair_values_match
        and nonnormal_value == sp.sqrt(10)
        and identity_value == 2
        and max(sp.eye(2).singular_values()) == 1,
    )

    six_modes = 6
    car6 = [annihilation_at(mode, six_modes) for mode in range(six_modes)]
    car6_dagger = [operator.H for operator in car6]
    singular_values = [sp.Integer(2), sp.Integer(2), sp.Rational(1, 2)]
    diagonal_pair_sum = sp.zeros(2**six_modes, 2**six_modes)
    for index, singular_value in enumerate(singular_values):
        diagonal_pair_sum += singular_value * (
            car6_dagger[2 * index] * car6[2 * index + 1]
            + car6_dagger[2 * index + 1] * car6[2 * index]
        )
    witness = sp.zeros(2**six_modes, 1)
    for choice_bits in range(8):
        basis_index = 0
        for index in range(3):
            occupy_first = (choice_bits >> index) & 1
            mode = 2 * index if occupy_first else 2 * index + 1
            basis_index |= 1 << (six_modes - 1 - mode)
        witness[basis_index] = 1
    target_eigenvalue = sum(singular_values)
    individual_norms_match = all(
        sp.simplify(
            operator_norm(
                singular_value
                * (
                    car6_dagger[2 * index] * car6[2 * index + 1]
                    + car6_dagger[2 * index + 1] * car6[2 * index]
                )
            )
            - singular_value
        )
        == 0
        for index, singular_value in enumerate(singular_values)
    )
    checks.check(
        "three-fiber-degenerate-case explicit eigenvector attains trace norm 9/2",
        sp.simplify(
            diagonal_pair_sum * witness - target_eigenvalue * witness
        )
        == sp.zeros(2**six_modes, 1)
        and individual_norms_match
        and target_eigenvalue == sp.Rational(9, 2),
    )

    real_rotation = sp.Rational(1, 5) * sp.Matrix([[3, 4], [-4, 3]])
    rotated_1 = real_rotation[0, 0] * car[0] + real_rotation[0, 1] * car[1]
    rotated_2 = real_rotation[1, 0] * car[0] + real_rotation[1, 1] * car[1]
    complex_rotation = sp.Matrix(
        [
            [sp.Rational(3, 5), 4 * sp.I / 5],
            [sp.Rational(4, 5), -3 * sp.I / 5],
        ]
    )
    complex_1 = (
        sp.conjugate(complex_rotation[0, 0]) * car[0]
        + sp.conjugate(complex_rotation[1, 0]) * car[1]
    )
    complex_2 = (
        sp.conjugate(complex_rotation[0, 1]) * car[0]
        + sp.conjugate(complex_rotation[1, 1]) * car[1]
    )
    real_car_ok = (
        is_zero(anticommutator(rotated_1, rotated_2))
        and is_zero(
            anticommutator(rotated_1, rotated_1.H) - sp.eye(2**mode_count)
        )
        and is_zero(
            anticommutator(rotated_2, rotated_2.H) - sp.eye(2**mode_count)
        )
        and is_zero(anticommutator(rotated_1, rotated_2.H))
    )
    complex_car_ok = (
        is_zero(complex_rotation.H * complex_rotation - sp.eye(2))
        and is_zero(anticommutator(complex_1, complex_2))
        and is_zero(
            anticommutator(complex_1, complex_1.H) - sp.eye(2**mode_count)
        )
        and is_zero(
            anticommutator(complex_2, complex_2.H) - sp.eye(2**mode_count)
        )
        and is_zero(anticommutator(complex_1, complex_2.H))
    )
    checks.check(
        "fiber-mode-rotation-car real and complex unitary rotations preserve CAR",
        real_car_ok and complex_car_ok,
    )

    first_hop = car_dagger[0] * car[2] + car_dagger[2] * car[0]
    second_hop = car_dagger[1] * car[3] + car_dagger[3] * car[1]
    first_spectrum = set(first_hop.eigenvals().keys())
    joint_spectrum = set((first_hop + 2 * second_hop).eigenvals().keys())
    expected_joint_spectrum = {
        left + right
        for left in (-1, 0, 1)
        for right in (-2, 0, 2)
    }
    checks.check(
        "disjoint-hop-joint-spectrum commuting spectra add and norm is 3",
        is_zero(commutator(first_hop, second_hop))
        and first_spectrum == {-1, 0, 1}
        and joint_spectrum == expected_joint_spectrum
        and operator_norm(first_hop + 2 * second_hop) == 3,
    )

    site_mode_count = 2
    site_car = [
        annihilation_at(mode, site_mode_count) for mode in range(site_mode_count)
    ]
    site_car_dagger = [operator.H for operator in site_car]

    def onsite_term(fiber_matrix):
        result = sp.zeros(2**site_mode_count, 2**site_mode_count)
        for left_fiber in range(2):
            for right_fiber in range(2):
                result += (
                    fiber_matrix[left_fiber, right_fiber]
                    * site_car_dagger[left_fiber]
                    * site_car[right_fiber]
                )
        return result

    strict_matrix = sp.diag(1, -1)
    saturated_matrix = sp.diag(1, 2)
    checks.check(
        "onsite-subset-sum-bound strict diag(1,-1) and saturated diag(1,2)",
        operator_norm(onsite_term(strict_matrix)) == 1
        and sum(strict_matrix.singular_values()) == 2
        and operator_norm(onsite_term(saturated_matrix)) == 3
        and sum(saturated_matrix.singular_values()) == 3,
    )

    nonnormal_singular_values = pair_instances[6].singular_values()
    identity_singular_values = sp.eye(2).singular_values()
    checks.check(
        "trace-to-operator-envelope S1<=n_f*op with identity attainment",
        sp.simplify(
            sum(nonnormal_singular_values)
            - 2 * max(nonnormal_singular_values)
        ).is_nonpositive
        is True
        and sum(identity_singular_values) == 2
        and max(identity_singular_values) == 1
        and sum(identity_singular_values) == 2 * max(identity_singular_values),
    )

    parity_4 = kron(PARITY_Z, PARITY_Z, PARITY_Z, PARITY_Z)
    parity_2 = kron(PARITY_Z, PARITY_Z)
    checks.check(
        "fiber-bilinear-evenness pair and onsite terms commute with parity",
        is_zero(commutator(pair_term(pair_instances[6]), parity_4))
        and is_zero(commutator(pair_term(pair_instances[7]), parity_4))
        and is_zero(commutator(onsite_term(strict_matrix), parity_2)),
    )

    decay_ratio = sp.Symbol("decay_ratio", positive=True)
    fiber_dimension = sp.Symbol("fiber_dimension", positive=True, integer=True)
    shell_series = (
        2
        * decay_ratio
        * (13 + 10 * decay_ratio + decay_ratio**2)
        / (1 - decay_ratio) ** 3
    )
    direct_envelope = fiber_dimension * (1 + 2 * shell_series)
    coarse_envelope = fiber_dimension * (1 + 4 * shell_series)
    missing_support_factor = fiber_dimension * (1 + shell_series)
    half = sp.Rational(1, 2)
    checks.check(
        "activity-envelope-formulas direct 293nf, coarse 585nf, missing-factor rejected",
        sp.simplify(direct_envelope.subs(decay_ratio, half))
        == 293 * fiber_dimension
        and sp.simplify(coarse_envelope.subs(decay_ratio, half))
        == 585 * fiber_dimension
        and sp.simplify(missing_support_factor.subs(decay_ratio, half))
        == 147 * fiber_dimension
        and direct_envelope.subs(
            {decay_ratio: half, fiber_dimension: 2}
        )
        < coarse_envelope.subs(
            {decay_ratio: half, fiber_dimension: 2}
        ),
    )

    checks.check(
        "su2-fixed-fiber-values n_f=2 gives direct 586K and coarse 1170K",
        direct_envelope.subs(
            {decay_ratio: half, fiber_dimension: 2}
        )
        == 586
        and coarse_envelope.subs(
            {decay_ratio: half, fiber_dimension: 2}
        )
        == 1170
        and direct_envelope.subs(
            {decay_ratio: half, fiber_dimension: 1}
        )
        == 293,
    )

    def linf_norm(point):
        return max(abs(coordinate) for coordinate in point)

    def shell_count(radius):
        return sum(
            1
            for point in itertools.product(
                range(-radius, radius + 1), repeat=3
            )
            if linf_norm(point) == radius
        )

    ambient_points = [
        point
        for point in itertools.product(range(-2, 3), repeat=3)
        if any(point)
    ]
    checks.check(
        "finite-open-ambient-metrics shells and sharp l1<=3linf conversion",
        [shell_count(radius) for radius in (1, 2, 3)] == [26, 98, 218]
        and all(
            sum(abs(coordinate) for coordinate in point)
            <= 3 * linf_norm(point)
            for point in ambient_points
        )
        and sum(abs(coordinate) for coordinate in (2, 2, 2))
        == 3 * linf_norm((2, 2, 2)),
    )

    pauli_x = sp.Matrix([[0, 1], [1, 0]])
    pauli_z = sp.Matrix([[1, 0], [0, -1]])
    zero_hamiltonian = sp.zeros(2)
    zero_evolution = sp.exp(sp.I * zero_hamiltonian)
    checks.check(
        "zero-activity-branch identity evolution avoids the activity quotient",
        zero_evolution == sp.eye(2)
        and zero_evolution * pauli_x * zero_evolution.H == pauli_x
        and commutator(pauli_x, pauli_z)
        == commutator(
            zero_evolution * pauli_x * zero_evolution.H, pauli_z
        ),
    )

    activity, time = sp.symbols("activity time", positive=True)
    growth = sp.exp(2 * activity * time) - 1
    checks.check(
        "uniform-corollary-monotonicity growth increases with activity and direct<=coarse",
        sp.diff(growth, activity).is_positive is True
        and sp.exp(2 * 293 * sp.Rational(1, 100)) - 1
        < sp.exp(2 * 585 * sp.Rational(1, 100)) - 1
        and sp.Rational(7, 3) <= 3,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
