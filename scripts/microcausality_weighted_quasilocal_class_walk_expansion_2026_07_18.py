#!/usr/bin/env python3
"""Exact checks for the supplied weighted quasilocal-class LR bound."""

import itertools

import sympy as sp


EXPECTED_LABELS = [
    "l1-sphere-count",
    "ambient-chain-diameter",
    "bond-incidence-ladder",
    "site-weighted-activity",
    "meeting-row-bound",
    "peeling-power",
    "exhaustive-chain-peeling",
    "duhamel-resummation",
    "decay-sign-rejector",
    "bond-envelope",
    "pair-activity-closed-form",
    "pair-activity-values",
    "even-car-locality",
    "tensor-support-reduction",
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


def diameter(support):
    return max(support) - min(support)


def main():
    checks = CheckRunner()

    def sphere_count(radius):
        return sum(
            1
            for point in itertools.product(
                range(-radius, radius + 1), repeat=3
            )
            if sum(abs(coordinate) for coordinate in point) == radius
        )

    sphere_values = [sphere_count(radius) for radius in range(1, 5)]
    checks.check(
        "l1-sphere-count exact 4r^2+2 values at r=1..4",
        sphere_values == [6, 18, 38, 66]
        and all(
            sphere_count(radius) == 4 * radius * radius + 2
            for radius in range(1, 5)
        ),
    )

    sites = tuple(range(5))
    supports = [
        frozenset(combo)
        for size in range(1, len(sites) + 1)
        for combo in itertools.combinations(sites, size)
    ]
    chains = [(support,) for support in supports if 0 in support]
    reach_ok = True
    attained = False
    for length in (1, 2, 3):
        if length > 1:
            chains = [
                chain + (next_support,)
                for chain in chains
                for next_support in supports
                if chain[-1] & next_support
            ]
        for chain in chains:
            if 4 not in chain[-1]:
                continue
            diameter_sum = sum(diameter(support) for support in chain)
            reach_ok &= diameter_sum >= 4
            attained |= diameter_sum == 4
    checks.check(
        "ambient-chain-diameter all subset chains obey sum diameters>=distance, attained",
        reach_ok
        and attained
        and diameter(frozenset((0, 4))) == 4,
    )

    axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

    def add(left, right):
        return tuple(a + b for a, b in zip(left, right))

    def incident(site):
        bonds = set()
        for axis in axes:
            for sign in (-1, 1):
                step = tuple(sign * component for component in axis)
                bonds.add(frozenset((site, add(site, step))))
        return bonds

    reference_bond = frozenset(((0, 0, 0), (1, 0, 0)))
    union_count = sum(len(incident(site)) for site in reference_bond)
    meeting_bonds = set().union(*(incident(site) for site in reference_bond))
    checks.check(
        "bond-incidence-ladder union=12 distinct=11 nonself=10",
        union_count == 12
        and len(meeting_bonds) == 11
        and len(meeting_bonds - {reference_bond}) == 10,
    )

    exponential_base = sp.Rational(3, 2)
    activity_family = [
        (frozenset((0, 2)), sp.Rational(1, 3)),
        (frozenset((0, 1, 2)), sp.Rational(1, 4)),
    ]

    def plain_weight(entry):
        support, norm = entry
        return norm * exponential_base ** diameter(support)

    def starred_weight(entry):
        support, _ = entry
        return len(support) * plain_weight(entry)

    starred_rows = {
        site: sum(
            starred_weight(entry)
            for entry in activity_family
            if site in entry[0]
        )
        for site in sites[:3]
    }
    missing_size_row = sum(
        plain_weight(entry)
        for entry in activity_family
        if 0 in entry[0]
    )
    wrong_sign_row = sum(
        len(support) * norm * exponential_base ** (-diameter(support))
        for support, norm in activity_family
        if 0 in support
    )
    checks.check(
        "site-weighted-activity exact size and positive-diameter factors reject omissions",
        starred_rows == {
            0: sp.Rational(51, 16),
            1: sp.Rational(27, 16),
            2: sp.Rational(51, 16),
        }
        and missing_size_row == sp.Rational(21, 16)
        and wrong_sign_row == sp.Rational(17, 27)
        and missing_size_row != starred_rows[0]
        and wrong_sign_row != starred_rows[0],
    )

    kappa_activity = max(starred_rows.values())
    meeting_rows_ok = all(
        sum(
            starred_weight(entry)
            for entry in activity_family
            if support & entry[0]
        )
        <= len(support) * kappa_activity
        for support in supports
    )
    checks.check(
        "meeting-row-bound exact finite family obeys sum meeting wstar<=size*kappa",
        meeting_rows_ok
        and kappa_activity == sp.Rational(51, 16),
    )

    def peeling_majorant(initial_activity, row_activity, length):
        return initial_activity * row_activity ** (length - 1)

    exact_peeling_value = peeling_majorant(
        sp.Rational(5, 4), sp.Rational(3, 2), 3
    )
    wrong_power_value = sp.Rational(5, 4) * sp.Rational(3, 2) ** 3
    checks.check(
        "peeling-power exact nX*kappa^(k-1) value rejects kappa^k",
        exact_peeling_value == sp.Rational(45, 16)
        and wrong_power_value == sp.Rational(135, 32)
        and exact_peeling_value != wrong_power_value,
    )

    exhaustive_family = []
    for support in supports:
        norm = sp.Rational(1, 3) ** diameter(support) * sp.Rational(
            1, 2
        ) ** len(support)
        exhaustive_family.append((support, norm))
    exhaustive_base = sp.Rational(5, 4)

    def exhaustive_plain(entry):
        support, norm = entry
        return norm * exhaustive_base ** diameter(support)

    def exhaustive_starred(entry):
        support, _ = entry
        return len(support) * exhaustive_plain(entry)

    exhaustive_kappa = max(
        sum(
            exhaustive_starred(entry)
            for entry in exhaustive_family
            if site in entry[0]
        )
        for site in sites
    )
    exhaustive_nx = sum(
        exhaustive_starred(entry)
        for entry in exhaustive_family
        if 0 in entry[0]
    )
    weighted_chains = [
        (entry,) for entry in exhaustive_family if 0 in entry[0]
    ]
    exhaustive_ok = True
    strict_witnesses = 0
    for length in (1, 2, 3):
        if length > 1:
            weighted_chains = [
                chain + (next_entry,)
                for chain in weighted_chains
                for next_entry in exhaustive_family
                if chain[-1][0] & next_entry[0]
            ]
        exact_sum = sum(
            sp.prod(exhaustive_plain(entry) for entry in chain)
            for chain in weighted_chains
            if 4 in chain[-1][0]
        )
        correct_bound = peeling_majorant(
            exhaustive_nx, exhaustive_kappa, length
        )
        exhaustive_ok &= exact_sum <= correct_bound
        strict_witnesses += int(bool(exact_sum < correct_bound))
    checks.check(
        "exhaustive-chain-peeling all 31 supports and lengths 1..3 satisfy the bound",
        exhaustive_ok
        and strict_witnesses == 3
        and len(exhaustive_family) == 31,
    )

    kappa, time, norm_a, norm_b, initial_activity = sp.symbols(
        "kappa time norm_a norm_b initial_activity", positive=True
    )
    order = sp.Symbol("order", integer=True, positive=True)
    order_term = (
        2 ** (order + 1)
        * norm_a
        * norm_b
        * initial_activity
        * kappa ** (order - 1)
        * time**order
        / sp.factorial(order)
    )
    summed_order_terms = sp.Sum(order_term, (order, 1, sp.oo)).doit()
    theorem_tail = (
        2
        * norm_a
        * norm_b
        * initial_activity
        / kappa
        * (sp.exp(2 * kappa * time) - 1)
    )
    half_prefactor_tail = theorem_tail / 2
    wrong_sign_tail = (
        2
        * norm_a
        * norm_b
        * initial_activity
        / kappa
        * (sp.exp(-2 * kappa * time) - 1)
    )
    correct_slope = sp.diff(theorem_tail, time).subs(time, 0)
    checks.check(
        "duhamel-resummation exact order series, slope, and prefactor/sign rejectors",
        sp.simplify(summed_order_terms - theorem_tail) == 0
        and sp.simplify(correct_slope - 4 * norm_a * norm_b * initial_activity)
        == 0
        and sp.simplify(summed_order_terms - half_prefactor_tail) != 0
        and sp.diff(wrong_sign_tail, time).subs(time, 0)
        == -4 * norm_a * norm_b * initial_activity,
    )

    decay_correct_near = exponential_base ** (-2)
    decay_correct_far = exponential_base ** (-5)
    decay_wrong_near = exponential_base**2
    decay_wrong_far = exponential_base**5
    checks.check(
        "decay-sign-rejector negative exponent decreases with distance while positive grows",
        0 < decay_correct_far < decay_correct_near < 1
        and 1 < decay_wrong_near < decay_wrong_far,
    )

    coupling, exp_mu = sp.symbols("coupling exp_mu", positive=True)
    saturated_star = sum(
        2 * coupling * exp_mu for _ in incident((0, 0, 0))
    )
    checks.check(
        "bond-envelope six incident size-two bonds give 12Jemu and rate ratio 6/5",
        sp.simplify(saturated_star - 12 * coupling * exp_mu) == 0
        and sp.Rational(2 * 12, 20) == sp.Rational(6, 5),
    )

    rho = sp.Symbol("rho", positive=True)
    sphere_generating_sum = (
        4 * rho * (1 + rho) / (1 - rho) ** 3
        + 2 * rho / (1 - rho)
    )
    expected_sphere_sum = 2 * rho * (3 + rho**2) / (1 - rho) ** 3
    kappa_3d = 2 * sphere_generating_sum
    expected_kappa_3d = 4 * rho * (3 + rho**2) / (1 - rho) ** 3
    kappa_1d = 4 * rho / (1 - rho)
    missing_size_kappa_3d = expected_kappa_3d / 2
    checks.check(
        "pair-activity-closed-form sphere sum and size-two factor reject half-value",
        sp.simplify(sphere_generating_sum - expected_sphere_sum) == 0
        and sp.simplify(kappa_3d - expected_kappa_3d) == 0
        and sp.simplify(kappa_3d - missing_size_kappa_3d) != 0
        and sp.simplify(kappa_1d - 2 * rho * 2 / (1 - rho)) == 0,
    )

    checks.check(
        "pair-activity-values exact 3D values 14,684 and 1D value 4",
        sp.simplify(expected_kappa_3d.subs(rho, sp.Rational(1, 3))) == 14
        and sp.simplify(expected_kappa_3d.subs(rho, sp.Rational(3, 4)))
        == 684
        and sp.simplify(kappa_1d.subs(rho, sp.Rational(1, 2))) == 4
        and sp.simplify(missing_size_kappa_3d.subs(rho, sp.Rational(1, 3)))
        == 7,
    )

    identity_2 = sp.eye(2)
    annihilation = sp.Matrix([[0, 1], [0, 0]])
    parity_z = sp.Matrix([[1, 0], [0, -1]])

    def kron(*matrices):
        result = matrices[0]
        for matrix in matrices[1:]:
            result = sp.Matrix(sp.kronecker_product(result, matrix))
        return result

    def annihilation_at(site, site_count=4):
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

    car = [annihilation_at(site) for site in range(4)]
    car_dagger = [operator.H for operator in car]
    long_pair = car_dagger[0] * car[3] + car_dagger[3] * car[0]
    nearest_pair = car_dagger[0] * car[1] + car_dagger[1] * car[0]
    middle_pair = car_dagger[1] * car[2] + car_dagger[2] * car[1]
    density_0 = car_dagger[0] * car[0]
    density_1 = car_dagger[1] * car[1]
    car_hamiltonian = long_pair + nearest_pair + middle_pair
    checks.check(
        "even-car-locality distant even term commutes off support and reduction is exact",
        is_zero(long_pair - long_pair.H)
        and is_zero(commutator(long_pair, car[1]))
        and is_zero(commutator(long_pair, car_dagger[1]))
        and is_zero(commutator(long_pair, density_1))
        and is_zero(commutator(middle_pair, density_0))
        and is_zero(
            commutator(car_hamiltonian, density_0)
            - commutator(long_pair, density_0)
            - commutator(nearest_pair, density_0)
        )
        and not is_zero(commutator(long_pair, density_0)),
    )

    pauli_x = sp.Matrix([[0, 1], [1, 0]])
    pauli_z = sp.Matrix([[1, 0], [0, -1]])
    three_site_term = kron(pauli_x, pauli_x, pauli_x, identity_2)
    far_bond = kron(identity_2, identity_2, pauli_z, pauli_z)
    observable_1 = kron(pauli_z, identity_2, identity_2, identity_2)
    observable_4 = kron(identity_2, identity_2, identity_2, pauli_x)
    tensor_hamiltonian = three_site_term + far_bond
    checks.check(
        "tensor-support-reduction mixed three-site and bond terms obey exact locality",
        is_zero(commutator(far_bond, observable_1))
        and is_zero(
            commutator(tensor_hamiltonian, observable_1)
            - commutator(three_site_term, observable_1)
        )
        and not is_zero(commutator(three_site_term, observable_1))
        and is_zero(commutator(three_site_term, observable_4)),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
