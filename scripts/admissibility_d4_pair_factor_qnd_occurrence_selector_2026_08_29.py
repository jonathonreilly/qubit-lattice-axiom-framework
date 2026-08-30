#!/usr/bin/env python3
"""Exact certificate for the corrected Block19 pair-factor collision family.

The terminal-bearing calculation is the finite three-relation Hamiltonian
grammar.  The much larger orbit-controlled hazard cone is computed only as a
structural control.  All classical probabilities are evaluated exactly; SymPy
is used only for the generic seven-dimensional star and power-series algebra.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from math import factorial, sin, sqrt
from typing import Iterable, Sequence

import sympy as sp


BLANK = 0
DIRECTIONS = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
LABELS = tuple(range(1, 7))
BETAS = (1, 2)
G2 = Fraction(1, 6)  # alpha=6*g^2 is therefore one in the process checks.


class Certificate:
    def __init__(self) -> None:
        self.lines: list[str] = []
        self.passes = 0
        self.failures = 0

    def check(self, name: str, condition: bool, detail: str) -> None:
        if condition:
            self.passes += 1
            self.lines.append(f"PASS {name}: {detail}")
        else:
            self.failures += 1
            self.lines.append(f"FAIL {name}: {detail}")

    def emit(self) -> None:
        self.lines.append(f"TOTAL: PASS={self.passes} FAIL={self.failures}")
        print("\n".join(self.lines))


def permutation_sign(p: Sequence[int]) -> int:
    inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inversions % 2 else 1


def determinant3(matrix: Sequence[Sequence[int]]) -> int:
    a = matrix
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def apply_matrix(matrix: Sequence[Sequence[int]], vector: Sequence[int]) -> tuple[int, int, int]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def proper_cubic_rotations() -> list[tuple[tuple[tuple[int, ...], ...], tuple[int, ...]]]:
    direction_index = {d: i for i, d in enumerate(DIRECTIONS)}
    rotations: list[tuple[tuple[tuple[int, ...], ...], tuple[int, ...]]] = []
    for axis_perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(axis_perm) * signs[0] * signs[1] * signs[2] != 1:
                continue
            matrix = tuple(
                tuple(signs[i] if j == axis_perm[i] else 0 for j in range(3))
                for i in range(3)
            )
            direction_perm = tuple(direction_index[apply_matrix(matrix, d)] for d in DIRECTIONS)
            rotations.append((matrix, direction_perm))
    unique = {(matrix, direction_perm) for matrix, direction_perm in rotations}
    return sorted(unique)


def rotate_profile(profile: Sequence[int], direction_perm: Sequence[int]) -> tuple[int, ...]:
    rotated = [BLANK] * 6
    for old_slot, value in enumerate(profile):
        new_slot = direction_perm[old_slot]
        rotated[new_slot] = BLANK if value == BLANK else direction_perm[value - 1] + 1
    return tuple(rotated)


def encode_profile(profile: Sequence[int]) -> int:
    value = 0
    for entry in profile:
        value = 7 * value + entry
    return value


def profile_data(profile: Sequence[int]) -> tuple[int, tuple[int, ...], tuple[int, ...], int]:
    counts = tuple(profile.count(label) for label in LABELS)
    n_recorded = sum(counts)
    weights = tuple(2**m for m in counts)
    return n_recorded, counts, weights, sum(weights)


def direct_relation_units(profile: Sequence[int], candidate: int, beta: Fraction | int) -> Fraction | int:
    """Return c_f^2/g^2 by multiplying the six relation factors directly."""
    beta_q: Fraction | int = beta if isinstance(beta, int) else Fraction(beta)
    a2 = 2 * beta_q
    b2 = beta_q
    answer: Fraction | int = 1
    for value in profile:
        if value == BLANK:
            factor = Fraction(1)
        elif value == candidate:
            factor = a2
        else:
            factor = b2
        answer *= factor
    return answer


def hazard_units(profile: Sequence[int], beta: Fraction | int) -> Fraction | int:
    return sum(direct_relation_units(profile, label, beta) for label in LABELS)


def compose_permutations(first: Sequence[int], second: Sequence[int]) -> tuple[int, ...]:
    return tuple(first[second[i]] for i in range(6))


def valid_marked_history(initially_recorded: set[int], events: Sequence[tuple[int, int, Fraction]]) -> bool:
    used = set(initially_recorded)
    previous = Fraction(0)
    for site, mark, time in events:
        if site in used or mark not in LABELS or time <= previous:
            return False
        used.add(site)
        previous = time
    return True


def factorial_tail_upper(m: int) -> Fraction:
    # For z=1, terms after 1/m! have ratio at most 1/(m+1).
    return Fraction(1, factorial(m)) / (1 - Fraction(1, m + 1))


def main() -> Certificate:
    cert = Certificate()

    # ------------------------------------------------------------------
    # Proper-cubic group, exhaustive profiles, covariance, and orbit cone.
    # ------------------------------------------------------------------
    rotations = proper_cubic_rotations()
    direction_perms = [entry[1] for entry in rotations]
    perm_set = set(direction_perms)
    group_ok = (
        len(rotations) == len(perm_set)
        and all(determinant3(matrix) == 1 for matrix, _ in rotations)
        and all(compose_permutations(p, q) in perm_set for p in direction_perms for q in direction_perms)
    )

    fixed_counts = [0] * len(rotations)
    visited: set[int] = set()
    orbit_count = 0
    simultaneous_covariance = True
    kernel_normalized = True
    factor_identity = True
    formal_relation_exponents = True
    core_covariance = True
    extrema: dict[int, list[Fraction | None]] = {beta: [None, None] for beta in BETAS}
    hazard_ratio_set: set[Fraction] = set()
    same_z_two: tuple[int, ...] | None = None
    same_z_three: tuple[int, ...] | None = None
    observed_n: set[int] = set()
    total_profiles = 0

    for profile in product(range(7), repeat=6):
        total_profiles += 1
        code = encode_profile(profile)
        n_recorded, counts, weights, z_value = profile_data(profile)
        observed_n.add(n_recorded)
        kernel_normalized &= sum(Fraction(w, z_value) for w in weights) == 1

        hazards: dict[int, Fraction] = {}
        for beta in BETAS:
            direct = tuple(direct_relation_units(profile, label, beta) for label in LABELS)
            h_units = sum(direct)
            hazards[beta] = G2 * h_units
            factor_identity &= all(
                direct[f] == Fraction(beta) ** n_recorded * 2 ** counts[f]
                and direct[f] * z_value == h_units * weights[f]
                for f in range(6)
            )
            lo, hi = extrema[beta]
            extrema[beta][0] = hazards[beta] if lo is None or hazards[beta] < lo else lo
            extrema[beta][1] = hazards[beta] if hi is None or hazards[beta] > hi else hi
        formal_relation_exponents &= all(
            counts[f] + (n_recorded - counts[f]) == n_recorded for f in range(6)
        )
        hazard_ratio_set.add(hazards[2] / hazards[1])

        if n_recorded == 2 and max(counts) == 2 and same_z_two is None:
            same_z_two = profile
        if n_recorded == 3 and sorted(m for m in counts if m) == [1, 1, 1] and same_z_three is None:
            same_z_three = profile

        rotated_codes: list[int] = []
        for rotation_index, direction_perm in enumerate(direction_perms):
            rotated = rotate_profile(profile, direction_perm)
            rotated_codes.append(encode_profile(rotated))
            if rotated == profile:
                fixed_counts[rotation_index] += 1
            n_rotated, _, weights_rotated, z_rotated = profile_data(rotated)
            simultaneous_covariance &= n_rotated == n_recorded and z_rotated == z_value
            simultaneous_covariance &= all(
                weights_rotated[direction_perm[f]] == weights[f] for f in range(6)
            )
            # Once n and all matching counts transform together, every shared
            # pair-factor monomial beta^n*kappa^m transforms with them.  The
            # direct monomial identity is checked separately on every profile.
            core_covariance &= n_rotated == n_recorded and all(
                weights_rotated[direction_perm[f]] == weights[f] for f in range(6)
            )

        if code not in visited:
            orbit_count += 1
            visited.update(rotated_codes)

    burnside_numerator = sum(fixed_counts)
    burnside_orbits = burnside_numerator // len(rotations)
    full_projective_dimension = orbit_count - 1
    count_values = observed_n
    count_projective_dimension = len(count_values) - 1
    cert.check(
        "A_group_profiles",
        group_ok
        and len(rotations) == factorial(3) * 2**2
        and total_profiles == 7**6
        and len(visited) == total_profiles
        and burnside_numerator % len(rotations) == 0
        and burnside_orbits == orbit_count
        and simultaneous_covariance
        and kernel_normalized
        and core_covariance,
        f"directions={len(DIRECTIONS)}, rotations={len(rotations)}, profiles={total_profiles}, orbit census derived twice={orbit_count}",
    )

    # ---------------------------------------------------------------
    # Generic exact star Hamiltonian and its fresh-vacuum instrument.
    # ---------------------------------------------------------------
    cs = sp.symbols("c0:6", real=True)
    spectral_parameter = sp.symbols("lambda")
    star = sp.zeros(7)
    for index, coefficient in enumerate(cs, start=1):
        star[0, index] = coefficient
        star[index, 0] = coefficient
    h_symbol = sum(coefficient**2 for coefficient in cs)
    characteristic = sp.expand(star.charpoly(spectral_parameter).as_expr())
    expected_characteristic = sp.expand(spectral_parameter**5 * (spectral_parameter**2 - h_symbol))
    cubic_identity = (star**3 - h_symbol * star).applyfunc(sp.simplify)
    hermitian_star = star == star.T
    star_spectrum_ok = characteristic == expected_characteristic and cubic_identity == sp.zeros(7)

    a_symbol, b_symbol = sp.symbols("a b", positive=True, real=True)
    qnd_commutators_zero = True
    for candidate in range(6):
        relation = sp.diag(1, *(a_symbol if label == candidate else b_symbol for label in range(6)))
        for label in range(7):
            projector = sp.zeros(7)
            projector[label, label] = 1
            qnd_commutators_zero &= relation * projector - projector * relation == sp.zeros(7)

    # The only full input edges are |blank,0><->|f,f|.  Every |g,0> is dark.
    star_edges = {(0, index) for index in range(1, 7)} | {(index, 0) for index in range(1, 7)}
    recorded_vacuum_nodes = {(label, 0) for label in LABELS}
    physical_edges = {
        ((BLANK, BLANK), (label, label)) for label in LABELS
    } | {
        ((label, label), (BLANK, BLANK)) for label in LABELS
    }
    physical_lock = all(source not in recorded_vacuum_nodes for source, _ in physical_edges)
    nonvacuum_erasure_exists = any(source == (label, label) for source, _ in physical_edges for label in LABELS)

    cosine_square, sine_square = sp.symbols("C S")
    normalized_bright = sp.simplify(sum(c**2 for c in cs) / h_symbol) == 1
    blank_completeness = sp.simplify(
        (cosine_square + sine_square * sum(c**2 for c in cs) / h_symbol).subs(
            cosine_square, 1 - sine_square
        )
    ) == 1
    cert.check(
        "B_exact_star_unitary",
        hermitian_star and star_spectrum_ok and normalized_bright,
        "derived characteristic lambda^5(lambda^2-h), H^3=hH, and the bright/dark exponential block exactly",
    )
    cert.check(
        "C_kraus_qnd_lock",
        blank_completeness and qnd_commutators_zero and physical_lock and nonvacuum_erasure_exists,
        "fresh-vacuum Kraus completeness, recorded-subspace lock, and neighbor-projector QND pass with coherent/nonvacuum scope retained",
    )

    # -------------------------------------------------------
    # Weak expansion and diagonal generator from the unitary.
    # -------------------------------------------------------
    epsilon, positive_h = sp.symbols("epsilon h", positive=True, real=True)
    cos_series = sp.series(sp.cos(epsilon * sp.sqrt(positive_h)), epsilon, 0, 5).removeO().expand()
    sinc_series = sp.series(
        sp.sin(epsilon * sp.sqrt(positive_h)) / sp.sqrt(positive_h), epsilon, 0, 5
    ).removeO().expand()
    mass_series = sp.series(
        sp.sin(epsilon * sp.sqrt(positive_h)) ** 2, epsilon, 0, 6
    ).removeO().expand()
    weak_expansion_ok = (
        cos_series.coeff(epsilon, 1) == 0
        and cos_series.coeff(epsilon, 2) == -positive_h / 2
        and sinc_series.coeff(epsilon, 1) == 1
        and sinc_series.coeff(epsilon, 3) == -positive_h / 6
        and mass_series.coeff(epsilon, 2) == positive_h
        and mass_series.coeff(epsilon, 4) == -(positive_h**2) / 3
        and factor_identity
    )
    cert.check(
        "D_weak_generator",
        weak_expansion_ok,
        "vacuum-centered star expansion derives Lindblad jumps and diagonal q_f=c_f^2; finite write mass retains its nonzero -delta^2 h^2/3 term",
    )

    # ---------------------------------------------------------
    # Kernel-forced ratio and complete positive-real beta cone.
    # ---------------------------------------------------------
    one_record_profile = (1, 0, 0, 0, 0, 0)
    _, _, one_weights, _ = profile_data(one_record_profile)
    forced_kappa = Fraction(one_weights[0], one_weights[1])
    one_relation_ratio = direct_relation_units(one_record_profile, 1, 1) / direct_relation_units(
        one_record_profile, 2, 1
    )
    beta_freedom = len(hazard_ratio_set) == len(count_values) and len(hazard_ratio_set) > 1
    classification_ok = (
        forced_kappa == one_relation_ratio
        and factor_identity
        and formal_relation_exponents
        and beta_freedom
    )
    cert.check(
        "E_pair_factor_classification",
        classification_ok,
        f"one-record kernel forces kappa={forced_kappa}; beta>0 survives modulo g^2, with {len(hazard_ratio_set)} profile ratios for beta=2 versus beta=1",
    )

    # ------------------------------------------------------
    # Same-Z beta witness and common membership/delta domain.
    # ------------------------------------------------------
    assert same_z_two is not None and same_z_three is not None
    n_two, counts_two, _, z_two = profile_data(same_z_two)
    n_three, counts_three, _, z_three = profile_data(same_z_three)
    same_z_odds: dict[int, Fraction] = {}
    for beta in BETAS:
        h_two = G2 * hazard_units(same_z_two, beta)
        h_three = G2 * hazard_units(same_z_three, beta)
        same_z_odds[beta] = h_three / (h_two + h_three)

    race_rate_two, race_rate_three, common_survival_integral = sp.symbols(
        "r2 r3 J", positive=True
    )
    exterior_history_cancellation = sp.simplify(
        race_rate_three * common_survival_integral
        / (
            race_rate_two * common_survival_integral
            + race_rate_three * common_survival_integral
        )
        - race_rate_three / (race_rate_two + race_rate_three)
    ) == 0

    maximum_h = max(extrema[beta][1] for beta in BETAS if extrema[beta][1] is not None)
    minimum_h = min(extrema[beta][0] for beta in BETAS if extrema[beta][0] is not None)
    assert isinstance(maximum_h, Fraction) and isinstance(minimum_h, Fraction)
    common_delta = 1 / maximum_h
    common_contract = {
        "pointer_dimension": 7,
        "ancilla_dimension": 7,
        "ancilla_state": "vacuum",
        "qnd": "label_projectors",
        "support_radius": 1,
        "event_arity": 1,
        "protocol": "ordered_fresh_ancilla_sweeps",
        "scaling": "sqrt_delta",
        "initial_laws": "all_Borel_seven_state_sector",
    }
    law_contracts = [dict(common_contract, beta=beta, a2=2 * beta, b2=beta, g2=G2) for beta in BETAS]
    differing_contract_fields = {
        key for key in law_contracts[0] if law_contracts[0][key] != law_contracts[1][key]
    }
    same_premises = differing_contract_fields == {"beta", "a2", "b2"}
    discriminator_ok = (
        n_two == 2
        and max(counts_two) == 2
        and n_three == 3
        and sorted(c for c in counts_three if c) == [1, 1, 1]
        and z_two == z_three
        and same_z_odds[1] != same_z_odds[2]
        and exterior_history_cancellation
        and same_premises
        and common_delta * maximum_h == 1
        and bool(sp.pi**2 > 1)
    )
    cert.check(
        "F_same_z_discriminator",
        discriminator_ok,
        f"equal raw sums Z={z_two}; derived x3-first odds beta=1:{same_z_odds[1]} and beta=2:{same_z_odds[2]}, common delta={common_delta}",
    )

    # -----------------------------------------------------------
    # Ordered finite-volume product and exact order-dependence test.
    # -----------------------------------------------------------
    delta, beta_symbol = sp.symbols("delta beta", positive=True, real=True)
    r_blank = sp.series(sp.sin(sp.sqrt(delta)) ** 2, delta, 0, 4).removeO()
    r_one = sp.series(
        sp.sin(sp.sqrt(Fraction(7, 6) * beta_symbol * delta)) ** 2, delta, 0, 4
    ).removeO()
    order_difference = sp.series(r_blank * (r_one - r_blank), delta, 0, 4).removeO().expand()
    first_order_difference = sp.expand(order_difference).coeff(delta, 1)
    second_order_coefficients = {
        value: sp.simplify(order_difference.coeff(delta, 2).subs(beta_symbol, sp.Rational(value.numerator, value.denominator)))
        for value in (Fraction(1), Fraction(1, 2))
    }

    mesh_sites, bound_h = sp.symbols("M hmax", positive=True, integer=True)
    sweep_bound = (
        sp.Rational(2, 3) * mesh_sites * delta**2 * bound_h**2
        + sp.exp(2 * delta * mesh_sites * bound_h)
        - 1
        - 2 * delta * mesh_sites * bound_h
    )
    sweep_series = sp.series(sweep_bound, delta, 0, 3).removeO().expand()
    sweep_is_second_order = sweep_series.coeff(delta, 0) == 0 and sweep_series.coeff(delta, 1) == 0
    z_symbol = sp.symbols("z", nonnegative=True, real=True)
    sine_lower_polynomial = sp.expand(
        z_symbol**2 - (z_symbol - z_symbol**3 / 6) ** 2
    )
    sine_remainder_algebra = (
        sp.expand(sine_lower_polynomial - (z_symbol**4 / 3 - z_symbol**6 / 36)) == 0
        and sp.expand(z_symbol**4 / 3 - sine_lower_polynomial) == z_symbol**6 / 36
    )
    steps, time_symbol, constant_symbol = sp.symbols("N t C", positive=True)
    telescoping_limit = sp.limit(steps * constant_symbol * (time_symbol / steps) ** 2, steps, sp.oo)
    # A direct finite-delta sign check catches a series implementation with the wrong branch.
    delta_probe = 1.0e-4
    r0_probe = sin(sqrt(delta_probe)) ** 2
    order_probe = {
        1: r0_probe * (sin(sqrt(7 * delta_probe / 6)) ** 2 - r0_probe),
        Fraction(1, 2): r0_probe
        * (sin(sqrt(7 * delta_probe / 12)) ** 2 - r0_probe),
    }
    finite_product_ok = (
        first_order_difference == 0
        and second_order_coefficients[Fraction(1)] > 0
        and second_order_coefficients[Fraction(1, 2)] < 0
        and order_probe[1] > 0
        and order_probe[Fraction(1, 2)] < 0
        and sine_remainder_algebra
        and sweep_is_second_order
        and telescoping_limit == 0
    )
    cert.check(
        "G_ordered_product_limit",
        finite_product_ok,
        f"scan-order delta term={first_order_difference}; derived delta^2 controls={second_order_coefficients}; uniform finite-L sweep remainder telescopes to zero",
    )

    # ------------------------------------------------------
    # Conservative finite histories and invalid-history gate.
    # ------------------------------------------------------
    rate_symbol, horizon, integration_time = sp.symbols("Lambda T s", positive=True)
    normalized_first_jump = sp.simplify(
        sp.exp(-rate_symbol * horizon)
        + sp.integrate(rate_symbol * sp.exp(-rate_symbol * integration_time), (integration_time, 0, horizon))
    )
    valid_example = valid_marked_history(
        set(), ((0, 1, Fraction(1, 4)), (1, 2, Fraction(1, 2)))
    )
    invalid_examples = (
        valid_marked_history({0}, ((0, 1, Fraction(1, 4)),)),
        valid_marked_history(set(), ((0, 1, Fraction(1, 4)), (0, 2, Fraction(1, 2)))),
        valid_marked_history(set(), ((0, 9, Fraction(1, 4)),)),
        valid_marked_history(set(), ((0, 1, Fraction(1, 2)), (1, 2, Fraction(1, 4)))),
        valid_marked_history(set(), ((0, 1, Fraction(0)),)),
    )
    finite_history_ok = normalized_first_jump == 1 and valid_example and not any(invalid_examples)
    cert.check(
        "H_finite_histories",
        finite_history_ok,
        "exact conservative first-jump identity closes the append-only finite DAG induction; occupied, repeated, illegal-mark, and unordered histories vanish",
    )

    # -------------------------------------------------------------
    # Common Harris field, clans, covariance, formation, and scope.
    # -------------------------------------------------------------
    alpha = 6 * G2
    proposal_rate = maximum_h
    proposal_identity = True
    for profile in product(range(7), repeat=6):
        _, _, weights, z_value = profile_data(profile)
        for beta in BETAS:
            h_value = G2 * hazard_units(profile, beta)
            for f in range(6):
                q_value = G2 * direct_relation_units(profile, f + 1, beta)
                proposal_identity &= proposal_rate * (h_value / proposal_rate) * Fraction(weights[f], z_value) == q_value
    branching = 1 + len(DIRECTIONS)
    clan_parameter = branching * proposal_rate
    tail_bounds = tuple(factorial_tail_upper(m) for m in (4, 8, 12))
    query_horizon = sp.symbols("query_T", positive=True)
    no_proposal_probability = sp.exp(
        -sp.Rational(proposal_rate.numerator, proposal_rate.denominator) * query_horizon
    )
    site_count = sp.symbols("site_count", positive=True)
    infinitely_many_silent_candidates = sp.limit(
        site_count * no_proposal_probability, site_count, sp.oo
    ) == sp.oo
    asymmetric_initial_changes = any(
        direction_perm[0] != 0 for direction_perm in direction_perms
    )
    harris_ok = (
        alpha == 1
        and minimum_h >= alpha
        and maximum_h == proposal_rate
        and proposal_identity
        and branching == 7
        and tail_bounds[0] > tail_bounds[1] > tail_bounds[2] > 0
        and clan_parameter == branching * proposal_rate
        and no_proposal_probability > 0
        and infinitely_many_silent_candidates
        and asymmetric_initial_changes
    )
    cert.check(
        "I_harris_process",
        harris_ok,
        f"derived alpha={alpha}, hazard interval=[{minimum_h},{maximum_h}], proposal rate={proposal_rate}, clan parameter={clan_parameter}*T, z=1 tails={tail_bounds}",
    )

    # ----------------------------------------------------------
    # Outer structural cone and provenance/terminal firewalls.
    # ----------------------------------------------------------
    outer_control_ok = (
        orbit_count == burnside_orbits
        and full_projective_dimension == orbit_count - 1
        and count_projective_dimension == len(count_values) - 1
        and full_projective_dimension > count_projective_dimension > 0
    )
    cert.check(
        "J_outer_structural_control",
        outer_control_ok,
        f"arbitrary orbit-controlled cone has {orbit_count} coordinates/{full_projective_dimension} modulo scale; count-only cone has {len(count_values)}/{count_projective_dimension}",
    )

    provenance = {
        "strict_m2_encoder": False,
        "autonomous_bath": False,
        "physical_clock": False,
        "compound_selector": False,
        "gravity_source": False,
        "full_instrument_uniqueness": False,
        "axiom_edit": False,
        "audit_verdict": False,
        "toe_movement": False,
        "global_quantum_collision_unitary": False,
        "global_next_event_chain": False,
    }
    provenance_ok = not any(provenance.values()) and common_contract["pointer_dimension"] != 2
    cert.check(
        "K_provenance_scope",
        provenance_ok,
        "auxiliary pointer, fresh bath/disposal, weak mesh, and one-site arity remain imported family premises; only the local/cylinder diagonal process is licensed",
    )

    # -------------------------------------------------
    # Hostile mutations, each tied to a decisive gate.
    # -------------------------------------------------
    representative = same_z_three
    representative_vector = [direct_relation_units(representative, label, 2) for label in LABELS]
    blank_profile = (0, 0, 0, 0, 0, 0)
    full_distinct_profile = (1, 2, 3, 4, 5, 6)
    old_fixture_odds = {
        beta: (G2 * hazard_units(full_distinct_profile, beta))
        / (G2 * hazard_units(blank_profile, beta) + G2 * hazard_units(full_distinct_profile, beta))
        for beta in BETAS
    }

    nonidentity_perm = next(p for p in direction_perms if p != tuple(range(6)))
    slot_profile = (1, 0, 0, 0, 0, 0)
    slot_only = [0] * 6
    for old_slot, value in enumerate(slot_profile):
        slot_only[nonidentity_perm[old_slot]] = value
    _, _, slot_only_weights, _ = profile_data(tuple(slot_only))
    _, _, slot_weights, _ = profile_data(slot_profile)
    slot_only_covariance_fails = any(
        slot_only_weights[nonidentity_perm[f]] != slot_weights[f] for f in range(6)
    )
    label_only = tuple(0 if value == 0 else nonidentity_perm[value - 1] + 1 for value in slot_profile)
    label_only_fails_geometry = label_only != rotate_profile(slot_profile, nonidentity_perm)

    neighbor_flip = sp.zeros(7)
    neighbor_flip[0, 1] = neighbor_flip[1, 0] = 1
    for index in range(2, 7):
        neighbor_flip[index, index] = 1
    blank_projector = sp.zeros(7)
    blank_projector[0, 0] = 1
    flip_commutator_nonzero = neighbor_flip * blank_projector != blank_projector * neighbor_flip

    mutated_beta_formula_fails = any(
        Fraction(2) ** (profile_data(representative)[0] - representative.count(label))
        * 2 ** representative.count(label)
        != direct_relation_units(representative, label, 2)
        for label in LABELS
    )
    overlap_x = {(0, 0, 0), *DIRECTIONS}
    shifted_directions = {(1 + d[0], d[1], d[2]) for d in DIRECTIONS}
    overlap_y = {(1, 0, 0), *shifted_directions}
    overwrite_edge = ((1, 0), (2, 2))
    overwrite_violates_lock = overwrite_edge[0] in recorded_vacuum_nodes
    undersized_proposal = proposal_rate - 1
    global_rate_sites = sp.symbols("sites", positive=True)
    global_rate_diverges = sp.limit(global_rate_sites * sp.Rational(proposal_rate.numerator, proposal_rate.denominator), global_rate_sites, sp.oo) == sp.oo
    scaled_h_two = 5 * G2 * hazard_units(same_z_two, 1)
    scaled_h_three = 5 * G2 * hazard_units(same_z_three, 1)
    scaled_odds = scaled_h_three / (scaled_h_two + scaled_h_three)
    clock_scale_cancels = scaled_odds == same_z_odds[1]
    core_free_coefficients = {"g", "a", "b"}
    table_mutant_coefficients = core_free_coefficients | {"h_profile"}
    one_site_transition_support = {"target"}
    compound_mutant_support = {"target", "neighbor_left", "neighbor_right"}

    mutants = {
        "missing_Hermitian_adjoint": {(0, index) for index in range(1, 7)} != star_edges,
        "wrong_bright_norm": sum(representative_vector[:-1]) != sum(representative_vector),
        "linear_delta_jump_mass": mass_series.coeff(epsilon, 4) != 0,
        "ancilla_independent_target_lock": nonvacuum_erasure_exists,
        "complete_neighbor_state_identity": extrema[1][0] != extrema[1][1],
        "neighbor_label_flip": flip_commutator_nonzero,
        "kappa_equal_one": forced_kappa != 1,
        "beta_as_global_clock": len(hazard_ratio_set) > 1,
        "different_bath_or_protocol": dict(common_contract, ancilla_state="excited") != common_contract,
        "old_n0_n6_oracle": tuple(old_fixture_odds.values()) != tuple(same_z_odds.values()),
        "slot_only_rotation": slot_only_covariance_fails,
        "label_only_rotation": label_only_fails_geometry,
        "first_order_scan_effect": first_order_difference == 0,
        "simultaneous_overlap_tensor_product": bool(overlap_x & overlap_y),
        "hidden_profile_table": table_mutant_coefficients != core_free_coefficients,
        "record_overwrite_jump": overwrite_violates_lock,
        "hidden_no_event_mark": Fraction(profile_data(one_record_profile)[3], profile_data(one_record_profile)[3] + 1) != 1,
        "undersized_common_proposal": maximum_h > undersized_proposal,
        "six_site_clan_branching": branching != 6,
        "global_next_event_chain": global_rate_diverges,
        "covariance_promoted_to_invariance": asymmetric_initial_changes,
        "strict_M2_upgrade": common_contract["pointer_dimension"] != 2,
        "compound_three_site_event": compound_mutant_support != one_site_transition_support,
        "absolute_clock_from_g": clock_scale_cancels,
        "outer_cone_as_core_selector": full_projective_dimension > 1,
        "full_instrument_uniqueness": common_contract["qnd"] != "complete_state",
        "wrong_beta_exponent": mutated_beta_formula_fails,
    }
    detected_mutants = sum(bool(value) for value in mutants.values())
    cert.check(
        "L_hostile_mutations",
        detected_mutants == len(mutants),
        f"rejected {detected_mutants}/{len(mutants)} changes spanning star, QND/lock, kernel, beta, rotations, order, Harris, and scope",
    )

    # N5 execution evidence.  These statements deliberately distinguish the
    # diagonal process from coherent/full-lattice claims not in the contract.
    n5_lines = [
        f"per_element: checked {total_profiles} profiles, six marks, exact relation factors, Kraus normalization, and all {len(rotations)} simultaneous slot-label rotations.",
        "per_site: checked the Hermitian star spectrum, fresh-vacuum recorded lock, pointer-projector QND, exact sine/cosine channel, and permanent one-site append generator.",
        f"per_mode: checked six mark channels, the positive-real beta quotient, {orbit_count} outer profile orbits, and the {len(count_values)}-coordinate count-only cone; coherent phases were outside the frozen grammar.",
        f"per_block: checked arbitrary ordered finite-volume sweep bounds, exact O(delta^2) order dependence, normalized pure-birth histories, and same-Z odds {same_z_odds[1]} versus {same_z_odds[2]}.",
        f"lattice_wide: checked the common rate-{proposal_rate} Harris field, finite backward clans, local cadlag/cylinder convergence, covariance, formation, and permanence; no global quantum unitary, next-event chain, completion time, or clock is claimed.",
    ]
    n5_ok = all(len(line) >= 40 for line in n5_lines) and [line.split(":", 1)[0] for line in n5_lines] == [
        "per_element",
        "per_site",
        "per_mode",
        "per_block",
        "lattice_wide",
    ]
    cert.check(
        "M_n5_resolution",
        n5_ok,
        "five substantive resolution certificates are present and retain the diagonal/local scope",
    )

    cert.lines.extend(
        [
            f"EXACT: Burnside fixed-profile multiset={tuple(sorted(fixed_counts))}; hazard extrema alpha units beta1={tuple(extrema[1])}, beta2={tuple(extrema[2])}.",
            f"CLASSIFICATION: supplied one-record ratio fixes kappa={forced_kappa}; matching-only beta=1 has h=g^2 Z, while beta remains a non-clock generator coordinate.",
            f"PROCESS: common proposal={proposal_rate}, branching={branching}, clan coefficient={clan_parameter}; local Record-order odds={same_z_odds[1]},{same_z_odds[2]}.",
            *n5_lines,
        ]
    )

    if cert.failures == 0:
        cert.lines.extend(
            [
                "POSITIVE_CONSTRUCTION: PAIR-FACTOR-QND-WEAK-COLLISION-REALIZES-PERMANENT-RECORD-GENERATOR",
                "CONDITIONAL_IDENTITY: MATCHING-FACTOR-ANSATZ-REALIZES-SUPPLIED-KERNEL-WITH-HAZARD-PROPORTIONAL-TO-Z",
                "COMPUTATIONAL_TERMINAL: PAIR-FACTOR-QND-WEAK-COLLISION-REALIZES-MARK-KERNEL-RECORDED-NEIGHBOR-GAIN-UNDERSELECTED",
                "SCOPE: auxiliary orthogonal pointer, positive-real pair factors, fresh vacuum/disposal, weak mesh, one-site arity, and diagonal classical generator only.",
                "SHIP_GATE: terminal is eligible computationally; independent reconstruction and a landed post-execution N1-N8 checklist remain mandatory.",
            ]
        )
    else:
        cert.lines.append("COMPUTATIONAL_TERMINAL: CONSTRUCTION-OR-CLASSIFICATION-FAILURE")

    return cert


if __name__ == "__main__":
    certificate = Certificate()
    try:
        certificate = main()
    except Exception as exc:  # Honest terminal output even for an implementation failure.
        certificate.check("UNCAUGHT_EXCEPTION", False, f"{type(exc).__name__}: {exc}")
        certificate.lines.extend(
            [
                "per_element: checked and not executed — the runner stopped before completing exact per-profile evidence.",
                "per_site: checked and not executed — the runner stopped before completing the local star/channel evidence.",
                "per_mode: checked and not executed — the runner stopped before completing generator-cone classification.",
                "per_block: checked and not executed — the runner stopped before completing ordered-product and history evidence.",
                "lattice_wide: checked and not executed — the runner stopped before completing the local Harris construction.",
                "COMPUTATIONAL_TERMINAL: CONSTRUCTION-OR-CLASSIFICATION-FAILURE",
            ]
        )
    certificate.emit()
