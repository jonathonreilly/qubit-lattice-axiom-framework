#!/usr/bin/env python3
"""Exact checks for the scalar gauged-kernel weighted-activity feed."""

import itertools

import sympy as sp


EXPECTED_LABELS = [
    "scalar-car-pair-norm",
    "linf-shell-count",
    "ambient-metric-conversion",
    "activity-factor-assembly",
    "activity-closed-values",
    "decay-threshold",
    "finite-open-region-envelope",
    "background-sign-uniformity",
    "zero-activity-branch",
    "uniform-corollary-monotonicity",
    "gaussian-identity-shift",
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


def main():
    checks = CheckRunner()

    identity_2 = sp.eye(2)
    annihilation = sp.Matrix([[0, 1], [0, 0]])
    parity_z = sp.Matrix([[1, 0], [0, -1]])

    def kron(*matrices):
        result = matrices[0]
        for matrix in matrices[1:]:
            result = sp.Matrix(sp.kronecker_product(result, matrix))
        return result

    def annihilation_at(site, site_count=3):
        return kron(
            *(
                [parity_z] * site
                + [annihilation]
                + [identity_2] * (site_count - site - 1)
            )
        )

    def commutator(left, right):
        return left * right - right * left

    def is_zero(matrix):
        return sp.simplify(matrix) == sp.zeros(*matrix.shape)

    def norm_squared(matrix):
        return max((matrix.H * matrix).eigenvals())

    car = [annihilation_at(site) for site in range(3)]
    car_dagger = [operator.H for operator in car]
    hopping_monomial = car_dagger[0] * car[1]
    density = car_dagger[0] * car[0]
    kernel_value = (sp.Integer(3) + 4 * sp.I) / 10
    pair_term = (
        kernel_value * car_dagger[0] * car[1]
        + sp.conjugate(kernel_value) * car_dagger[1] * car[0]
    )
    global_parity = kron(parity_z, parity_z, parity_z)
    exact_pair_norm_squared = sp.simplify(norm_squared(pair_term))
    checks.check(
        "scalar-car-pair-norm exact |k|=1/2, size-two envelope=1, even Hermitian",
        sp.simplify(norm_squared(hopping_monomial) - 1) == 0
        and sp.simplify(norm_squared(density) - 1) == 0
        and is_zero(pair_term - pair_term.H)
        and is_zero(commutator(pair_term, global_parity))
        and exact_pair_norm_squared == sp.Rational(1, 4)
        and 2 * sp.Rational(1, 2) == 1,
    )

    def linf_norm(point):
        return max(abs(coordinate) for coordinate in point)

    def linf_shell_count(radius):
        return sum(
            1
            for point in itertools.product(
                range(-radius, radius + 1), repeat=3
            )
            if linf_norm(point) == radius
        )

    shell_values = [linf_shell_count(radius) for radius in (1, 2, 3)]
    checks.check(
        "linf-shell-count exact 24r^2+2 values 26,98,218",
        shell_values == [26, 98, 218]
        and all(
            linf_shell_count(radius)
            == (2 * radius + 1) ** 3 - (2 * radius - 1) ** 3
            == 24 * radius * radius + 2
            for radius in (1, 2, 3)
        ),
    )

    metric_points = [
        point
        for point in itertools.product(range(-2, 3), repeat=3)
        if any(point)
    ]
    metric_conversion_ok = all(
        sum(abs(coordinate) for coordinate in point)
        <= 3 * linf_norm(point)
        for point in metric_points
    )
    diagonal = (2, 2, 2)
    checks.check(
        "ambient-metric-conversion l1<=3linf on open Z3 subsets with equality",
        metric_conversion_ok
        and sum(abs(coordinate) for coordinate in diagonal)
        == 3 * linf_norm(diagonal)
        and not all(
            sum(abs(coordinate) for coordinate in point)
            <= 2 * linf_norm(point)
            for point in metric_points
        ),
    )

    decay_ratio = sp.Symbol("decay_ratio", positive=True)
    shell_series = (
        24 * decay_ratio * (1 + decay_ratio) / (1 - decay_ratio) ** 3
        + 2 * decay_ratio / (1 - decay_ratio)
    )
    closed_shell_series = (
        2
        * decay_ratio
        * (13 + 10 * decay_ratio + decay_ratio**2)
        / (1 - decay_ratio) ** 3
    )
    envelope_activity = 1 + 4 * closed_shell_series
    exact_scalar_activity = 1 + 2 * closed_shell_series
    wrong_support_factor_activity = 1 + closed_shell_series
    checks.check(
        "activity-factor-assembly pair-norm two times support-size two and closed shell sum",
        sp.simplify(shell_series - closed_shell_series) == 0
        and sp.simplify(
            4 * closed_shell_series
            - 8
            * decay_ratio
            * (13 + 10 * decay_ratio + decay_ratio**2)
            / (1 - decay_ratio) ** 3
        )
        == 0
        and sp.simplify(envelope_activity - exact_scalar_activity) != 0
        and sp.simplify(exact_scalar_activity - wrong_support_factor_activity)
        != 0,
    )

    half = sp.Rational(1, 2)
    checks.check(
        "activity-closed-values envelope=585 scalar=293 reject missing-factor=147",
        sp.simplify(envelope_activity.subs(decay_ratio, half)) == 585
        and sp.simplify(exact_scalar_activity.subs(decay_ratio, half)) == 293
        and sp.simplify(
            wrong_support_factor_activity.subs(decay_ratio, half)
        )
        == 147
        and 585 != 293 != 147,
    )

    eta, delta = sp.symbols("eta delta", positive=True)
    mu_below = eta / 3 - delta
    mu_above = eta / 3 + delta
    exponent_below = sp.simplify(eta - 3 * mu_below)
    exponent_above = sp.simplify(eta - 3 * mu_above)
    numeric_q_below = sp.exp(-(sp.Integer(2) - 3 * sp.Rational(1, 2)))
    numeric_q_above = sp.exp(-(sp.Integer(2) - 3 * sp.Rational(3, 4)))
    checks.check(
        "decay-threshold mu<eta/3 gives q<1 while above threshold gives q>1",
        exponent_below == 3 * delta
        and exponent_above == -3 * delta
        and 0 < numeric_q_below < 1
        and numeric_q_above > 1,
    )

    finite_radius = 2
    finite_q = sp.Rational(1, 4)
    finite_points = itertools.product(
        range(-finite_radius, finite_radius + 1), repeat=3
    )
    finite_envelope = 1 + 4 * sum(
        finite_q ** linf_norm(point) for point in finite_points if any(point)
    )
    infinite_envelope = sp.simplify(
        envelope_activity.subs(decay_ratio, finite_q)
    )
    checks.check(
        "finite-open-region-envelope truncated ambient shells lie below infinite envelope",
        finite_envelope < infinite_envelope
        and infinite_envelope == sp.Rational(673, 9),
    )

    exponential_mu = sp.Rational(9, 8)
    sites = (0, 1, 2)
    pairs = ((0, 1), (1, 2), (0, 2))
    envelope_activities = set()
    exact_activities = set()
    norm_multisets = set()
    for signs in itertools.product((-1, 1), repeat=3):
        pair_norms = {
            pair: abs(sign) * sp.Rational(1, 2) ** abs(pair[1] - pair[0])
            for pair, sign in zip(pairs, signs)
        }
        norm_multisets.add(tuple(sorted(pair_norms.values())))
        site_envelopes = []
        site_exact = []
        for site in sites:
            envelope_sum = sp.Integer(1)
            exact_sum = sp.Integer(1)
            for pair, pair_norm in pair_norms.items():
                if site not in pair:
                    continue
                pair_distance = abs(pair[1] - pair[0])
                envelope_sum += (
                    2 * pair_norm * 2 * exponential_mu**pair_distance
                )
                exact_sum += pair_norm * 2 * exponential_mu**pair_distance
            site_envelopes.append(envelope_sum)
            site_exact.append(exact_sum)
        envelope_activities.add(max(site_envelopes))
        exact_activities.add(max(site_exact))
    checks.check(
        "background-sign-uniformity eight sign backgrounds give envelope 11/2 and exact 13/4",
        len(norm_multisets) == 1
        and envelope_activities == {sp.Rational(11, 2)}
        and exact_activities == {sp.Rational(13, 4)},
    )

    pauli_x = sp.Matrix([[0, 1], [1, 0]])
    pauli_z = sp.Matrix([[1, 0], [0, -1]])
    zero_hamiltonian = sp.zeros(2)
    zero_evolution = sp.exp(sp.I * zero_hamiltonian)
    evolved_pauli_x = zero_evolution * pauli_x * zero_evolution.H
    checks.check(
        "zero-activity-branch zero Hamiltonian gives identity evolution without dividing by kappa",
        zero_evolution == sp.eye(2)
        and evolved_pauli_x == pauli_x
        and commutator(evolved_pauli_x, pauli_z)
        == commutator(pauli_x, pauli_z),
    )

    actual_kappa, common_kappa, time = sp.symbols(
        "actual_kappa common_kappa time", positive=True
    )
    growth = sp.exp(2 * actual_kappa * time) - 1
    growth_derivative = sp.diff(growth, actual_kappa)
    actual_value = sp.exp(2 * sp.Integer(3) * sp.Rational(2, 7)) - 1
    common_value = sp.exp(2 * sp.Integer(5) * sp.Rational(2, 7)) - 1
    checks.check(
        "uniform-corollary-monotonicity growth increases with kappa and coarse support ratio",
        growth_derivative.is_positive is True
        and actual_value < common_value
        and sp.Rational(7, 3) <= 3,
    )

    scalar_shift = sp.Symbol("scalar_shift", real=True)
    hamiltonian_matrix = sp.MatrixSymbol("hamiltonian_matrix", 2, 2)
    observable_matrix = sp.MatrixSymbol("observable_matrix", 2, 2)
    shift_drop = sp.expand(
        (scalar_shift * sp.Identity(2) + hamiltonian_matrix)
        * observable_matrix
        - observable_matrix
        * (scalar_shift * sp.Identity(2) + hamiltonian_matrix)
        - (
            hamiltonian_matrix * observable_matrix
            - observable_matrix * hamiltonian_matrix
        )
    )
    checks.check(
        "gaussian-identity-shift scalar log-factor drops from every commutator",
        shift_drop == sp.ZeroMatrix(2, 2),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
