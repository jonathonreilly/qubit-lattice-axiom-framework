#!/usr/bin/env python3
"""Exact checks for additive Record readout versus a compatible pair action.

The source note proves the Boolean mixed-difference separation, unique
site-plus-edge decomposition, code-symmetric line intersection, and finite
site/edge response theorem. This runner checks exact finite fixtures and binds
the claim to the current source boundaries.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_ISING_ACTION_RECORD_READOUT_PAIR_RESOURCE_RESPONSE_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
ACTION_PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
PAIR_PARENT_PATH = ROOT / "docs" / (
    "PHYSICAL_PAIR_KERNEL_MINIMAL_POSITION_EXTENSION_CYCLE698_NOTE_2026-07-25.md"
)
PRICING_PARENT_PATH = ROOT / "docs" / (
    "SOURCE_ACTION_BRIDGE_PRICING_CYCLE871_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
WEAK_FIELD_PARENT_PATH = ROOT / "docs" / (
    "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_ISING_ACTION_RECORD_READOUT_PAIR_RESOURCE_RESPONSE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/PHYSICAL_PAIR_KERNEL_MINIMAL_POSITION_EXTENSION_CYCLE698_NOTE_2026-07-25.md",
    "docs/SOURCE_ACTION_BRIDGE_PRICING_CYCLE871_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md",
)


Config = tuple[int, ...]
Edge = tuple[int, int]
Vec3 = tuple[int, int, int]


def flip(configuration: Config, site: int) -> Config:
    changed = list(configuration)
    changed[site] = 1 - changed[site]
    return tuple(changed)


def zero_pair(configuration: Config, left: int, right: int) -> Config:
    changed = list(configuration)
    changed[left] = 0
    changed[right] = 0
    return tuple(changed)


def occupation(configuration: Config) -> int:
    return sum(configuration)


def edge_occupation(configuration: Config, edges: tuple[Edge, ...]) -> int:
    return sum(configuration[left] * configuration[right] for left, right in edges)


def additive_readout(
    configuration: Config,
    zero_weights: tuple[Fraction, ...],
    one_weights: tuple[Fraction, ...],
) -> Fraction:
    return sum(
        one_weights[index] if value else zero_weights[index]
        for index, value in enumerate(configuration)
    )


def pair_action(
    configuration: Config,
    edges: tuple[Edge, ...],
    site_coefficient: Fraction,
    edge_coefficient: Fraction,
) -> Fraction:
    return (
        site_coefficient * occupation(configuration)
        + edge_coefficient * edge_occupation(configuration, edges)
    )


def mixed_difference(
    function,
    configuration: Config,
    left: int,
    right: int,
) -> Fraction:
    base = zero_pair(configuration, left, right)
    return (
        function(flip(flip(base, left), right))
        - function(flip(base, left))
        - function(flip(base, right))
        + function(base)
    )


def subset_configuration(site_count: int, subset: tuple[int, ...]) -> Config:
    chosen = set(subset)
    return tuple(1 if site in chosen else 0 for site in range(site_count))


def mobius_coefficient(site_count: int, function, subset: tuple[int, ...]) -> Fraction:
    total = Fraction(0)
    for subset_size in range(len(subset) + 1):
        for chosen in combinations(subset, subset_size):
            sign = -1 if (len(subset) - subset_size) % 2 else 1
            total += sign * function(subset_configuration(site_count, chosen))
    return total


def reconstruct_from_mobius(
    site_count: int,
    coefficients: dict[tuple[int, ...], Fraction],
    configuration: Config,
) -> Fraction:
    occupied = {site for site, value in enumerate(configuration) if value}
    return sum(
        coefficient
        for subset, coefficient in coefficients.items()
        if set(subset).issubset(occupied)
    )


def matrix_rank(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    matrix = [row[:] for row in rows]
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / scale for entry in matrix[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


NEIGHBOR_DIRECTIONS: tuple[Vec3, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def permutation_parity(values: tuple[int, int, int]) -> int:
    inversions = sum(
        values[left] > values[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_cubic_neighbor_permutations() -> tuple[tuple[int, ...], ...]:
    rotations: set[tuple[int, ...]] = set()
    for axes in permutations((0, 1, 2)):
        for signs in product((-1, 1), repeat=3):
            determinant = permutation_parity(axes) * signs[0] * signs[1] * signs[2]
            if determinant != 1:
                continue
            images = []
            for vector in NEIGHBOR_DIRECTIONS:
                transformed = tuple(signs[row] * vector[axes[row]] for row in range(3))
                images.append(NEIGHBOR_DIRECTIONS.index(transformed))
            rotations.add(tuple(images))
    return tuple(sorted(rotations))


def periodic_cubic_graph(size: int) -> tuple[tuple[Vec3, ...], tuple[tuple[Vec3, Vec3], ...]]:
    sites = tuple(product(range(size), repeat=3))
    positive_directions = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    edge_set: set[frozenset[Vec3]] = set()
    for site in sites:
        for direction in positive_directions:
            target = tuple((site[index] + direction[index]) % size for index in range(3))
            edge_set.add(frozenset((site, target)))
    edges = tuple(
        sorted(
            (tuple(sorted(edge)) for edge in edge_set),
            key=repr,
        )
    )
    return sites, edges


def determinant_three(matrix: list[list[Fraction]]) -> Fraction:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def exact_mean_and_covariance(
    weighted_statistics: tuple[tuple[Fraction, tuple[int, ...]], ...]
) -> tuple[tuple[Fraction, ...], tuple[tuple[Fraction, ...], ...]]:
    total = sum((weight for weight, _ in weighted_statistics), Fraction(0))
    dimension = len(weighted_statistics[0][1])
    means = tuple(
        sum(
            (weight * Fraction(statistics[index]) for weight, statistics in weighted_statistics),
            Fraction(0),
        )
        / total
        for index in range(dimension)
    )
    covariance = tuple(
        tuple(
            sum(
                (
                    weight * Fraction(statistics[left] * statistics[right])
                    for weight, statistics in weighted_statistics
                ),
                Fraction(0),
            )
            / total
            - means[left] * means[right]
            for right in range(dimension)
        )
        for left in range(dimension)
    )
    return means, covariance


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    action_parent = ACTION_PARENT_PATH.read_text(encoding="utf-8")
    pair_parent = PAIR_PARENT_PATH.read_text(encoding="utf-8")
    pricing_parent = PRICING_PARENT_PATH.read_text(encoding="utf-8")
    weak_field_parent = WEAK_FIELD_PARENT_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())
    axiom_clean = axiom_flat.replace("`", "")
    action_parent_flat = " ".join(action_parent.split())
    pair_parent_flat = " ".join(pair_parent.split())
    pricing_parent_flat = " ".join(pricing_parent.split())

    print("external_scientific_inputs: none; finite Boolean interaction algebra and exact rational response are proved in-source")
    print("package_local_integrity_reads: current axioms and compatible-action, pair-kernel, source-pricing, and weak-field boundaries are source-bound")
    print("analytic_boundary: arbitrary finite one-body and Boolean-decomposition theorems are proved generally; exact path, cubic, and two-site fixtures are executed")
    print("negative_scope: the fixed binary content-only readout does not equal a nontrivial pair action; enlarged content, pair resources, auxiliary fields, and physical source routes remain live")

    checks.check(
        "source-current-record",
        "content-only scalar readout, finite additivity, and the source/action open gate are present",
        all(
            phrase in axiom_clean
            for phrase in (
                "A readout value is determined by record content alone.",
                "For any finite collection of pairwise-disjoint records, scalar readout I is additive",
                "source/action and physical-observable identification",
            )
        ),
    )
    checks.check(
        "source-compatible-action-parent",
        "the preceding action, code-swap relation, and gravity boundary are present",
        all(
            phrase in action_parent_flat
            for phrase in (
                "A^(sum_i x_i)",
                "A B^3=1",
                "The note does not call that action gravity.",
            )
        ),
    )
    checks.check(
        "source-pair-parent",
        "the pair shape and its open value/sign/range/licensing boundary are present",
        "every pair coefficient exactly zero" in pair_parent_flat
        and "one constant times the number of adjacent record pairs" in pair_parent_flat
        and "Value, sign, range, and licensing remain open" in pair_parent_flat,
    )
    checks.check(
        "source-pricing-parent",
        "the additive action ansatz and nonimplication warning are present",
        "readout-to-action / source-action identification is an OPEN bridge" in pricing_parent_flat
        and "Equal modeled dimension does not establish mutual implication" in pricing_parent_flat,
    )
    checks.check(
        "source-weak-field-parent",
        "the physical weak-field packet preserves full-Einstein and Newton-unit boundaries",
        "This is a bounded weak-field theorem" in weak_field_parent
        and "the full Einstein equations" in weak_field_parent
        and "physical `G_Newton` in SI units" in weak_field_parent,
    )

    site_count = 4
    path_edges: tuple[Edge, ...] = ((0, 1), (1, 2), (2, 3))
    zero_weights = tuple(Fraction(value) for value in (2, -3, 5, 7))
    one_weights = tuple(Fraction(value) for value in (11, 13, -2, 17))
    additive_function = lambda configuration: additive_readout(
        configuration, zero_weights, one_weights
    )
    additive_curls = tuple(
        mixed_difference(additive_function, configuration, left, right)
        for configuration in product((0, 1), repeat=site_count)
        for left, right in combinations(range(site_count), 2)
    )
    checks.check(
        "additive-zero-curl",
        "arbitrary site-dependent two-content additive weights have zero mixed difference on every square",
        additive_curls and all(value == 0 for value in additive_curls),
    )

    site_coefficient = Fraction(11, 7)
    edge_coefficient = Fraction(-5, 3)
    action_function = lambda configuration: pair_action(
        configuration, path_edges, site_coefficient, edge_coefficient
    )
    edge_curls = tuple(
        mixed_difference(action_function, configuration, left, right)
        for configuration in product((0, 1), repeat=site_count)
        for left, right in path_edges
    )
    nonedge_pairs = tuple(
        pair
        for pair in combinations(range(site_count), 2)
        if pair not in path_edges
    )
    nonedge_curls = tuple(
        mixed_difference(action_function, configuration, left, right)
        for configuration in product((0, 1), repeat=site_count)
        for left, right in nonedge_pairs
    )
    checks.check(
        "action-edge-curl",
        "the pair action mixed difference equals its edge coefficient in every environment",
        edge_curls and all(value == edge_coefficient for value in edge_curls),
    )
    checks.check(
        "action-nonedge-curl",
        "the same action has zero mixed difference on every nonedge",
        nonedge_curls and all(value == 0 for value in nonedge_curls),
    )

    content_zero_weight = Fraction(3)
    content_one_weight = Fraction(5)
    one_body_weights = (
        content_zero_weight * content_zero_weight,
        content_one_weight * content_zero_weight,
        content_zero_weight * content_one_weight,
        content_one_weight * content_one_weight,
    )
    one_body_cross_ratio = (
        one_body_weights[3] * one_body_weights[0]
        / (one_body_weights[1] * one_body_weights[2])
    )
    probability_a = Fraction(1, 8)
    probability_b = Fraction(2)
    pair_weights = (
        Fraction(1),
        probability_a,
        probability_a,
        probability_a * probability_a * probability_b,
    )
    pair_cross_ratio = pair_weights[3] * pair_weights[0] / (pair_weights[1] * pair_weights[2])
    checks.check(
        "multiplicative-cross-ratio",
        "one-body content weights give ratio one while the exact compatible edge fixture gives B=2",
        one_body_cross_ratio == 1 and pair_cross_ratio == probability_b == 2,
    )
    checks.check(
        "cross-ratio-mutation-control",
        "removing the pair factor collapses the hostile B=2 witness to the one-body ratio",
        (
            probability_a * probability_a * Fraction(1)
            * pair_weights[0]
            / (pair_weights[1] * pair_weights[2])
        )
        == 1
        and pair_cross_ratio != 1,
    )

    coefficients: dict[tuple[int, ...], Fraction] = {}
    for subset_size in range(site_count + 1):
        for subset in combinations(range(site_count), subset_size):
            coefficients[subset] = mobius_coefficient(site_count, action_function, subset)
    checks.check(
        "mobius-singletons",
        "every singleton Boolean coefficient equals the site coefficient",
        all(coefficients[(site,)] == site_coefficient for site in range(site_count)),
    )
    checks.check(
        "mobius-edges",
        "every nearest-neighbor pair coefficient equals the edge coefficient and every nonedge is zero",
        all(coefficients[edge] == edge_coefficient for edge in path_edges)
        and all(coefficients[pair] == 0 for pair in nonedge_pairs),
    )
    checks.check(
        "mobius-higher-order",
        "all Boolean coefficients of order three and four vanish",
        all(
            coefficient == 0
            for subset, coefficient in coefficients.items()
            if len(subset) >= 3
        ),
    )
    checks.check(
        "mobius-unique-reconstruction",
        "the complete coefficient table reconstructs the action on all sixteen configurations",
        all(
            reconstruct_from_mobius(site_count, coefficients, configuration)
            == action_function(configuration)
            for configuration in product((0, 1), repeat=site_count)
        ),
    )
    three_body_coefficient = Fraction(7, 5)
    mutated_function = lambda configuration: (
        action_function(configuration)
        + three_body_coefficient * configuration[0] * configuration[1] * configuration[2]
    )
    checks.check(
        "higher-order-mutation-control",
        "an injected three-site interaction is detected by its exact third-order coefficient",
        mobius_coefficient(site_count, mutated_function, (0, 1, 2))
        == three_body_coefficient
        and three_body_coefficient != 0,
    )

    feature_rows = [
        [
            Fraction(1),
            Fraction(occupation(configuration)),
            Fraction(edge_occupation(configuration, path_edges)),
        ]
        for configuration in product((0, 1), repeat=site_count)
    ]
    checks.check(
        "site-edge-feature-rank",
        "constant, site count, and edge count are exactly three independent configuration functions",
        matrix_rank(feature_rows) == 3,
    )

    rotations = proper_cubic_neighbor_permutations()
    neighbor_orbit = {
        rotation[NEIGHBOR_DIRECTIONS.index((1, 0, 0))]
        for rotation in rotations
    }
    checks.check(
        "proper-cubic-pair-orbit",
        "all 24 proper rotations act transitively on the six range-one edge directions",
        len(rotations) == 24
        and neighbor_orbit == set(range(6))
        and all(sorted(rotation) == list(range(6)) for rotation in rotations),
    )

    cubic_sites, cubic_edges = periodic_cubic_graph(3)
    degrees = {site: 0 for site in cubic_sites}
    for left, right in cubic_edges:
        degrees[left] += 1
        degrees[right] += 1
    checks.check(
        "six-regular-cubic-fixture",
        "the periodic 3-cube fixture has 27 sites, 81 undirected edges, and degree six",
        len(cubic_sites) == 27
        and len(cubic_edges) == 81
        and set(degrees.values()) == {6},
    )
    sample_sets = (
        frozenset(),
        frozenset((cubic_sites[0],)),
        frozenset(cubic_edges[0]),
        frozenset(cubic_sites[:5]),
        frozenset(site for site in cubic_sites if sum(site) % 2 == 0),
    )

    def cubic_counts(chosen: frozenset[Vec3]) -> tuple[int, int]:
        return len(chosen), sum(left in chosen and right in chosen for left, right in cubic_edges)

    complement_identity = all(
        cubic_counts(frozenset(set(cubic_sites) - set(chosen)))[1]
        == len(cubic_edges) - 6 * cubic_counts(chosen)[0] + cubic_counts(chosen)[1]
        for chosen in sample_sets
    )
    checks.check(
        "code-swap-edge-identity",
        "complementing occupation gives E(1-x)=|E|-6N+E on the exact cubic fixture",
        complement_identity,
    )
    code_edge_coefficient = Fraction(13, 9)
    code_site_coefficient = -3 * code_edge_coefficient
    action_differences = []
    for chosen in sample_sets:
        n_value, e_value = cubic_counts(chosen)
        complement = frozenset(set(cubic_sites) - set(chosen))
        nc_value, ec_value = cubic_counts(complement)
        original = code_site_coefficient * n_value + code_edge_coefficient * e_value
        swapped = code_site_coefficient * nc_value + code_edge_coefficient * ec_value
        action_differences.append(swapped - original)
    checks.check(
        "code-swap-action-line",
        "u=-3v makes the six-regular action code-swap invariant up to one constant",
        len(set(action_differences)) == 1,
    )
    intersection_equations = [
        [Fraction(-3), Fraction(-1)],
        [Fraction(-5), Fraction(-2)],
    ]
    checks.check(
        "one-line-trivial-intersection",
        "singleton and adjacent-pair configurations force the interacting and additive one-scalar lines to meet only at zero",
        matrix_rank(intersection_equations) == 2,
    )

    weighted_statistics = (
        (Fraction(1), (0, 0, 0)),
        (Fraction(1, 8), (1, 0, 0)),
        (Fraction(1, 8), (0, 1, 0)),
        (Fraction(1, 32), (1, 1, 1)),
    )
    means, covariance = exact_mean_and_covariance(weighted_statistics)
    expected_means = (Fraction(5, 41), Fraction(5, 41), Fraction(1, 41))
    expected_numerators = (
        (180, 16, 36),
        (16, 180, 36),
        (36, 36, 40),
    )
    expected_covariance = tuple(
        tuple(Fraction(value, 1681) for value in row) for row in expected_numerators
    )
    checks.check(
        "response-exact-means",
        "the two-site site/edge sufficient statistics have exact mean (5,5,1)/41",
        means == expected_means,
    )
    checks.check(
        "response-exact-covariance",
        "the exact Hessian/covariance matrix has the displayed rational entries",
        covariance == expected_covariance
        and all(covariance[left][right] == covariance[right][left] for left in range(3) for right in range(3)),
    )
    leading_one = covariance[0][0]
    leading_two = covariance[0][0] * covariance[1][1] - covariance[0][1] ** 2
    leading_three = determinant_three([list(row) for row in covariance])
    checks.check(
        "response-positive-definite",
        "all three exact leading principal minors are positive with numerators 180, 32144, and 860672",
        leading_one == Fraction(180, 1681)
        and leading_two == Fraction(32144, 1681**2)
        and leading_three == Fraction(860672, 1681**3)
        and leading_one > 0
        and leading_two > 0
        and leading_three > 0,
    )
    checks.check(
        "response-variance-identity",
        "every tested rational linear combination has nonnegative variance from the covariance form",
        all(
            sum(
                vector[left] * covariance[left][right] * vector[right]
                for left in range(3)
                for right in range(3)
            )
            >= 0
            for vector in product((Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2)), repeat=3)
        ),
    )

    construction_needles = (
        "w_11 w_00/(w_10 w_01)=B",
        "v=-log B",
        "v [E(x)-3 N(x)]",
        "Hess Psi = Cov(T,T)",
        "Pair-resource representation clause",
        "Physical log-law source/action clause",
        "S_phys=s_*[-log pi]+C",
    )
    checks.check(
        "construction-source-surface",
        "the source states the cross-ratio, edge coefficient, line comparison, response, and both candidate clauses",
        all(phrase in note_flat for phrase in construction_needles),
    )
    boundary_needles = (
        "No canonical axiom is edited",
        "the fixed TOE percentages do not move",
        "No interaction no-go, source-action impossibility, axiom inconsistency, or gravity no-go is claimed",
        "This steelman is accepted",
        "hypothetical wording only",
    )
    checks.check(
        "boundary-source-surface",
        "the source preserves governance, percentage, alternative-carrier, steelman, and global-negative limits",
        all(phrase in note_flat for phrase in boundary_needles),
    )
    checks.check(
        "machine-status-contract",
        "the source carries the bounded upstream-support trace contract",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "trace_class: upstream_support",
                "target_claim_id:",
                "target_blocker_text:",
                "source_of_blocker_text: handoff",
                "reachability_to_target: advances",
                "artifact_role: theorem",
                "next_trace_action:",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "pair-resource, log-law action, and source-coordinate wording is absent from the canonical memo",
        all(
            phrase not in axiom
            for phrase in (
                "pair resource",
                "physical statistical source action",
                "edge cross-ratio",
                "site and pair coefficients",
            )
        ),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections, source matching, primitive scan, accepted steelman, and broad-negative rejection are visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "| Source location | Exact residual used | Matches the result? |" in note
        and "The primitive-registry scan used" in note
        and "This steelman is accepted" in note
        and "FAIL / DO NOT SHIP" in note
        and "No interaction no-go, source-action impossibility, axiom inconsistency, or gravity no-go is claimed" in note_flat,
    )

    print("per_element: two Record content weights, one site coefficient, one edge coefficient, and three response coordinates are checked")
    print("per_site: arbitrary site-dependent additive weights have zero pair curl; uniform cubic site terms and code swap are separated")
    print("per_mode: content-only readout, site-plus-edge statistical action, enlarged-content/pair-resource alternatives, and source response are distinct")
    print("per_block: compatible law -> cross-ratio -> unique pair resource -> one-line nonidentity -> covariance response is checked")
    print("lattice_wide: the six-regular periodic cubic identity and all 24 proper rotations are checked; physical source licensing, stress conservation, metric response, gravity, dynamics, and history are not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
