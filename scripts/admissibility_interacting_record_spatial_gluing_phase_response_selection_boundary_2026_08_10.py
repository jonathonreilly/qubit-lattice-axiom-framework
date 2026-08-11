#!/usr/bin/env python3
"""Test interacting Record gluing and the remaining phase-selection boundary.

The bounded witness is a four-site spatial cycle.  Each site carries one null
Record and fifteen actual-edge-labelled Records.  Positive Potts-type factors
couple shared-edge neighbours, while the local geometry score remains the
Block-31 edge score.  A single positive joint law supplies every finite-region
marginal exactly.

The runner also compares two conditional geometry sectors, arbitrary positive
sector multipliers, compact metric reactions, and an unconstrained metric-
response control.  These constructions identify what locality/projectivity
does and does not select; they are not adopted physical laws.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_record_edge_score_rank_one_metric_stress_spatial_projective_curvature_reaction_boundary_2026_08_10 as block31  # noqa: E402


regge = block31.regge

AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_INTERACTING_RECORD_SPATIAL_GLUING_PHASE_RESPONSE_SELECTION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = block31.NOTE_PATH
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_INTERACTING_RECORD_SPATIAL_GLUING_PHASE_RESPONSE_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RECORD_EDGE_SCORE_RANK_ONE_METRIC_STRESS_SPATIAL_PROJECTIVE_CURVATURE_REACTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_record_edge_score_rank_one_metric_stress_spatial_projective_curvature_reaction_boundary_2026_08_10.py",
)

SITES = tuple(range(4))
SPATIAL_EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
PHASE_RHO = (2, 3)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def local_weights(phase: int) -> tuple[int, ...]:
    """Positive class weights invariant under all four-axis permutations."""
    return (5 + 2 * phase,) + tuple(
        2 + phase + sum(direction) for direction in regge.DIRS15
    )


def matching_edges(history: tuple[int, ...]) -> int:
    return sum(history[left] == history[right] for left, right in SPATIAL_EDGES)


def full_integer_law(phase: int) -> tuple[dict[tuple[int, ...], int], int]:
    weights = local_weights(phase)
    rho = PHASE_RHO[phase]
    law: dict[tuple[int, ...], int] = {}
    for history in product(range(16), repeat=4):
        numerator = 1
        for state in history:
            numerator *= weights[state]
        numerator *= rho ** matching_edges(history)
        law[history] = numerator
    return law, sum(law.values())


def all_marginal_numerators(
    full_law: dict[tuple[int, ...], int],
) -> dict[tuple[int, ...], dict[tuple[int, ...], int]]:
    marginals = {
        subset: defaultdict(int)
        for size in range(5)
        for subset in combinations(SITES, size)
    }
    for history, numerator in full_law.items():
        for subset, marginal in marginals.items():
            marginal[tuple(history[site] for site in subset)] += numerator
    return {subset: dict(law) for subset, law in marginals.items()}


def state_label_permutation(axis_permutation: tuple[int, ...]) -> tuple[int, ...]:
    directions = tuple(tuple(item) for item in regge.DIRS15)
    index = {direction: position + 1 for position, direction in enumerate(directions)}
    result = [0]
    for direction in directions:
        transformed = [0, 0, 0, 0]
        for old_axis, bit in enumerate(direction):
            transformed[axis_permutation[old_axis]] = bit
        result.append(index[tuple(transformed)])
    return tuple(result)


def cycle_automorphisms() -> tuple[tuple[int, ...], ...]:
    edge_set = {frozenset(edge) for edge in SPATIAL_EDGES}
    return tuple(
        permutation
        for permutation in permutations(SITES)
        if {
            frozenset((permutation[left], permutation[right]))
            for left, right in SPATIAL_EDGES
        }
        == edge_set
    )


def metric_tensor(coordinate_covector: np.ndarray) -> np.ndarray:
    tensor = np.zeros((4, 4), dtype=float)
    for value, (left, right) in zip(coordinate_covector, regge.HCOMPS):
        if left == right:
            tensor[left, right] = value
        else:
            tensor[left, right] = value / 2.0
            tensor[right, left] = value / 2.0
    return tensor


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    parent = flat(PARENT_PATH)
    registry = PREMISE_REGISTRY_PATH.read_text(encoding="utf-8")

    print("external_scientific_inputs: none; both interacting laws, finite-region marginals, and response controls are repository-local")
    print("analytic_boundary: probability and restriction claims are exact on one four-site cycle; response solves use double precision on the inherited compact carrier")
    print("physical_boundary: the score values, action unit, phase prior, geometry coefficient, boundary-message law, Ward connection, and Lorentzian update remain unselected")

    checks.check(
        "axiom-and-parent-boundary",
        "Admissibility requires neighbour-dependent distributions but does not specify their values, while Block 31 supplies only a noninteracting conditional compiler",
        "determined by, and varies with, the nearest-neighbor conditions" in axioms
        and "distribution's extensional form and values are not specified" in axioms
        and "not a selected gravity law" in parent
        and "spatial product family" in parent
        and all(
            key in registry
            for key in (
                "minimal_axioms",
                "scale_reference_primitive",
                "kinetic_isotropy_primitive",
                "realized_state_primitive",
            )
        ),
    )
    checks.check(
        "note-contract",
        "the note separates interacting finite-parent gluing from lattice-wide law and phase selection and carries N1--N8",
        "interacting finite-parent gluing" in note
        and "boundary message" in note
        and "not a selected gravity phase" in note
        and "n1--n8 status:" in note
        and "no canonical axiom is edited" in note,
    )

    phase_laws = []
    phase_marginals = []
    partition_functions = []
    total_probability_count = set()
    marginal_check_count = set()
    minimum_numerator = None
    normalization_failures = 0
    marginal_failures = 0
    for phase in range(2):
        law, partition = full_integer_law(phase)
        marginals = all_marginal_numerators(law)
        phase_laws.append(law)
        phase_marginals.append(marginals)
        partition_functions.append(partition)
        total_probability_count.add(sum(len(item) for item in marginals.values()))
        minimum_numerator = min(
            min(min(item.values()) for item in marginals.values()),
            minimum_numerator if minimum_numerator is not None else partition,
        )
        normalization_failures += sum(
            sum(item.values()) != partition for item in marginals.values()
        )
        checks_here = 0
        for subset, marginal in marginals.items():
            for position, site in enumerate(subset):
                target_subset = tuple(item for item in subset if item != site)
                target = marginals[target_subset]
                for history, target_numerator in target.items():
                    checks_here += 1
                    source_sum = sum(
                        marginal[
                            history[:position] + (state,) + history[position:]
                        ]
                        for state in range(16)
                    )
                    marginal_failures += int(source_sum != target_numerator)
        marginal_check_count.add(checks_here)

    checks.check(
        "positive-exact-interacting-joint-laws",
        "both supplied four-site laws are strictly positive and normalized on all sixteen Record states",
        minimum_numerator is not None
        and minimum_numerator > 0
        and normalization_failures == 0
        and len(phase_laws) == 2,
        f"partitions={partition_functions}; minimum numerator={minimum_numerator}; normalization failures={normalization_failures}",
    )
    checks.check(
        "exact-interacting-finite-region-projectivity",
        "every subset marginal agrees under every one-site deletion for both interacting geometry sectors",
        total_probability_count == {83521}
        and marginal_check_count == {19652}
        and marginal_failures == 0,
        f"probabilities per phase={total_probability_count}; restrictions per phase={marginal_check_count}; failures={marginal_failures}",
    )

    locality_failures = 0
    neighbour_variations = []
    for phase, law in enumerate(phase_laws):
        weights = local_weights(phase)
        rho = PHASE_RHO[phase]
        for site in SITES:
            neighbours = tuple(
                other
                for edge in SPATIAL_EDGES
                if site in edge
                for other in edge
                if other != site
            )
            opposite = next(
                item for item in SITES if item != site and item not in neighbours
            )
            for context in product(range(16), repeat=3):
                fixed_sites = tuple(item for item in SITES if item != site)
                assignment = dict(zip(fixed_sites, context))
                formula = tuple(
                    weights[state]
                    * rho ** sum(state == assignment[item] for item in neighbours)
                    for state in range(16)
                )
                baseline_history = [assignment.get(item, 0) for item in SITES]
                baseline_history[site] = 0
                baseline = law[tuple(baseline_history)]
                for state in range(1, 16):
                    history = baseline_history.copy()
                    history[site] = state
                    locality_failures += int(
                        law[tuple(history)] * formula[0]
                        != baseline * formula[state]
                    )
                if assignment[opposite] not in (0, 1):
                    continue
        def conditional_zero(left_state: int, right_state: int) -> Fraction:
            denominator = sum(
                weights[state]
                * rho ** ((state == left_state) + (state == right_state))
                for state in range(16)
            )
            return Fraction(
                weights[0] * rho ** ((left_state == 0) + (right_state == 0)),
                denominator,
            )
        neighbour_variations.append(
            abs(conditional_zero(0, 0) - conditional_zero(1, 1))
        )
    checks.check(
        "nearest-neighbour-full-conditionals",
        "each exact full conditional depends only on the two graph neighbours and varies with their Records",
        locality_failures == 0 and min(neighbour_variations) > 0,
        f"factorization failures={locality_failures}; minimum conditional variation={float(min(neighbour_variations)):.6f}",
    )

    adjacent_cross_ratios = []
    induced_cross_ratios = []
    for phase, law in enumerate(phase_laws):
        rho = PHASE_RHO[phase]
        adjacent_cross_ratios.append(
            Fraction(
                law[(0, 0, 0, 0)] * law[(1, 1, 0, 0)],
                law[(0, 1, 0, 0)] * law[(1, 0, 0, 0)],
            )
        )
        opposite = phase_marginals[phase][(0, 2)]
        induced_cross_ratios.append(
            Fraction(
                opposite[(0, 0)] * opposite[(1, 1)],
                opposite[(0, 1)] * opposite[(1, 0)],
            )
        )
        if adjacent_cross_ratios[-1] != rho * rho:
            locality_failures += 1
    checks.check(
        "genuine-shared-edge-interaction",
        "adjacent conditional cross-ratios equal rho squared and are nontrivial in both sectors",
        locality_failures == 0
        and adjacent_cross_ratios == [Fraction(4), Fraction(9)],
        f"adjacent cross-ratios={adjacent_cross_ratios}",
    )
    checks.check(
        "boundary-message-under-restriction",
        "deleting the two intervening sites induces an exact nonproduct correlation between opposite retained sites",
        all(value > 1 for value in induced_cross_ratios),
        "induced opposite-site cross-ratios="
        + ",".join(f"{float(value):.6f}" for value in induced_cross_ratios),
    )

    label_covariance_failures = 0
    for axis_permutation in permutations(range(4)):
        relabel = state_label_permutation(axis_permutation)
        for phase in range(2):
            weights = local_weights(phase)
            label_covariance_failures += sum(
                weights[state] != weights[relabel[state]] for state in range(16)
            )
            label_covariance_failures += sum(
                (left == right) != (relabel[left] == relabel[right])
                for left in range(16)
                for right in range(16)
            )
    automorphisms = cycle_automorphisms()
    checks.check(
        "axis-and-spatial-factor-covariance",
        "local weights and equality couplings commute with all 24 edge-axis relabellings and all cycle automorphisms",
        label_covariance_failures == 0 and len(automorphisms) == 8,
        f"axis failures={label_covariance_failures}; spatial automorphisms={len(automorphisms)}",
    )

    geometry_shift = np.linspace(-0.23, 0.31, 15)
    source_vectors = set()
    null_action_error = 0.0
    action_linearity_error = 0.0
    interaction_action_maximum = 0.0
    for phase, rho in enumerate(PHASE_RHO):
        log_rho = np.log(float(rho))
        for beta in (0.5, 1.0, 2.0):
            for history in phase_laws[phase]:
                counts = tuple(history.count(edge + 1) for edge in range(15))
                source_vectors.add(counts)
                match_count = matching_edges(history)
                action_zero = (len(SPATIAL_EDGES) - match_count) * log_rho
                action_shift = (
                    beta * float(np.dot(counts, geometry_shift)) + action_zero
                )
                action_linearity_error = max(
                    action_linearity_error,
                    abs(action_shift - action_zero - beta * np.dot(counts, geometry_shift)),
                )
                if any(counts):
                    interaction_action_maximum = max(
                        interaction_action_maximum,
                        abs(action_shift - beta * np.dot(counts, geometry_shift)),
                    )
            null_history = (0, 0, 0, 0)
            null_counts = np.asarray(
                [null_history.count(edge + 1) for edge in range(15)],
                dtype=float,
            )
            null_action = (
                beta * float(np.dot(null_counts, geometry_shift))
                + (len(SPATIAL_EDGES) - matching_edges(null_history)) * log_rho
            )
            null_action_error = max(null_action_error, abs(null_action))
    checks.check(
        "null-relative-interacting-source-action",
        "the all-null history is anchored and interaction adds geometry-independent shared-edge action",
        null_action_error == 0.0
        and action_linearity_error < 1.0e-13
        and interaction_action_maximum > 0.0,
        f"source vectors={len(source_vectors)}; linearity={action_linearity_error:.3e}; maximum interaction action={interaction_action_maximum:.6f}",
    )
    checks.check(
        "interaction-preserves-record-source-compiler",
        "the geometry derivative of every interacting history is beta times its actual-edge count source",
        len(source_vectors) == 3876 and action_linearity_error < 1.0e-13,
        f"distinct sources={len(source_vectors)}; derivative identity={action_linearity_error:.3e}",
    )

    metric_map = np.asarray(block31.reaction.exact_metric_map(), dtype=float)
    constituent_errors = []
    constituent_ranks = set()
    aggregate_minimum_eigenvalue = 0.0
    for edge, direction in enumerate(regge.DIRS15):
        tensor = metric_tensor(metric_map.T @ np.eye(15)[:, edge])
        vector = np.asarray(direction, dtype=float)
        expected = np.outer(vector, vector) / (2.0 * np.linalg.norm(vector))
        constituent_errors.append(float(np.linalg.norm(tensor - expected)))
        constituent_ranks.add(int(np.linalg.matrix_rank(tensor, tol=1.0e-10)))
    for counts in source_vectors:
        tensor = metric_tensor(metric_map.T @ np.asarray(counts, dtype=float))
        aggregate_minimum_eigenvalue = min(
            aggregate_minimum_eigenvalue, float(np.min(np.linalg.eigvalsh(tensor)))
        )
    checks.check(
        "positive-metric-stress-under-interacting-gluing",
        "constituent stresses remain rank one and every four-site aggregate stress is positive semidefinite",
        max(constituent_errors) < 1.0e-12
        and constituent_ranks == {1}
        and aggregate_minimum_eigenvalue > -1.0e-11,
        f"constituent error={max(constituent_errors):.3e}; ranks={constituent_ranks}; aggregate minimum={aggregate_minimum_eigenvalue:.3e}",
    )

    law0, law1 = phase_laws
    z0, z1 = partition_functions
    tv_numerator = sum(
        abs(law0[history] * z1 - law1[history] * z0) for history in law0
    )
    phase_tv = Fraction(tv_numerator, 2 * z0 * z1)
    checks.check(
        "record-conditionals-separate-geometry-sectors",
        "the two supplied interacting geometry sectors have distinct positive Record laws",
        phase_tv > 0,
        f"exact conditional total variation={float(phase_tv):.9f}",
    )

    prior_odds = []
    conditional_failures = 0
    for multipliers in ((1, 1), (1, 7)):
        common = multipliers[0] + multipliers[1]
        prior_odds.append(Fraction(multipliers[1], multipliers[0]))
        for phase, (law, partition) in enumerate(
            zip(phase_laws, partition_functions)
        ):
            other_partition = partition_functions[1 - phase]
            sector_mass = multipliers[phase] * z0 * z1
            for numerator in law.values():
                joint_numerator = multipliers[phase] * numerator * other_partition
                conditional_failures += int(
                    joint_numerator * partition
                    != sector_mass * numerator
                )
            conditional_failures += int(
                Fraction(sector_mass, common * z0 * z1)
                != Fraction(multipliers[phase], common)
            )
    checks.check(
        "geometry-phase-prior-nonselection",
        "positive sector multipliers preserve both conditional laws while changing geometry-phase odds",
        conditional_failures == 0 and prior_odds == [Fraction(1), Fraction(7)],
        f"conditional failures={conditional_failures}; phase odds={prior_odds}",
    )

    q0, r20, metric_map, metric_projector, _ = block31.compact_operators()
    source_matrix = np.asarray(sorted(source_vectors), dtype=float).T
    compact_ranks = set()
    metric_response_ranks = set()
    compact_equation = 0.0
    compact_constraint = 0.0
    metric_equation = 0.0
    response_separation = 0.0
    for alpha in block31.lift.ALPHA_WITNESSES:
        repaired = q0 + alpha * r20
        kkt = np.block(
            [
                [repaired, metric_map],
                [metric_map.T, np.zeros((10, 10))],
            ]
        )
        compact_ranks.add(int(np.linalg.matrix_rank(kkt, tol=1.0e-8)))
        for beta in (0.5, 1.0, 2.0):
            sources = beta * source_matrix
            right = np.vstack((-sources, np.zeros((10, sources.shape[1]))))
            compact_solution = np.linalg.solve(kkt, right)
            compact_response = compact_solution[:15]
            compact_multiplier = compact_solution[15:]
            compact_equation = max(
                compact_equation,
                float(
                    np.linalg.norm(
                        repaired @ compact_response
                        + metric_map @ compact_multiplier
                        + sources,
                        2,
                    )
                ),
            )
            compact_constraint = max(
                compact_constraint,
                float(np.linalg.norm(metric_map.T @ compact_response, 2)),
            )
            for gamma in (0.25, 1.0, 4.0):
                metric_operator = repaired + gamma * metric_projector
                metric_response_ranks.add(
                    int(np.linalg.matrix_rank(metric_operator, tol=1.0e-8))
                )
                free_response = np.linalg.solve(metric_operator, -sources)
                metric_equation = max(
                    metric_equation,
                    float(np.linalg.norm(metric_operator @ free_response + sources, 2)),
                )
                response_separation = max(
                    response_separation,
                    float(np.linalg.norm(free_response - compact_response, 2)),
                )
    checks.check(
        "compact-metric-reaction-completion",
        "the inherited metric-only KKT branch solves every interacting-history source at all alpha and beta controls",
        compact_ranks == {25}
        and compact_equation < 1.0e-10
        and compact_constraint < 1.0e-10,
        f"ranks={compact_ranks}; equation={compact_equation:.3e}; constraint={compact_constraint:.3e}",
    )
    checks.check(
        "unconstrained-metric-response-control",
        "a supplied positive metric stiffness gives a distinct full-rank no-reaction response for the same sources",
        metric_response_ranks == {15}
        and metric_equation < 1.0e-10
        and response_separation > 1.0,
        f"ranks={metric_response_ranks}; equation={metric_equation:.3e}; separation={response_separation:.6f}",
    )
    checks.check(
        "structural-properties-do-not-select-response-phase",
        "positivity, locality, covariance, projectivity, source compilation, and solvability admit both compact-reaction and metric-response completions",
        compact_ranks == {25}
        and metric_response_ranks == {15}
        and response_separation > 1.0
        and phase_tv > 0,
    )
    checks.check(
        "coefficient-family-nonselection",
        "the bounded properties persist across beta, rho, phase-prior, alpha, and metric-stiffness controls",
        prior_odds[0] != prior_odds[1]
        and PHASE_RHO[0] != PHASE_RHO[1]
        and len(block31.lift.ALPHA_WITNESSES) == 5
        and compact_ranks == {25}
        and metric_response_ranks == {15},
        "beta=3 controls; rho=2 controls; prior=2 controls; alpha=5 controls; metric stiffness=3 controls",
    )
    checks.check(
        "lattice-wide-ward-and-lorentzian-boundary",
        "one finite parent law does not derive an infinite-lattice boundary-message specification, a complete Ward connection, or Lorentzian dynamics",
        "finite parent" in note
        and "complete stationary ward" in note
        and "lorentzian" in note
        and "not a selected gravity phase" in note,
    )
    checks.check(
        "minimal-law-or-axiom-delta",
        "the remaining autonomy deficit is extensional law selection, boundary-message gluing, geometry-phase dynamics, and causal update rather than another source vector",
        "extensional record law" in note
        and "boundary-message" in note
        and "phase/update law" in note
        and "no fifth ontology axiom is proven necessary" in note,
    )

    print("N5_CERTIFICATE: interaction=two positive four-site shared-edge laws have exact nearest-neighbour full conditionals and nontrivial cross-ratios")
    print("N5_CERTIFICATE: projectivity=each law supplies 83,521 exact subset probabilities and 19,652 one-site restrictions")
    print("N5_CERTIFICATE: boundary=deletion preserves probability but induces opposite-site correlation, so same-form locality needs a boundary message")
    print("N5_CERTIFICATE: response=the same 3,876 sources admit compact reactions and a distinct supplied metric-response control")
    print("N5_CERTIFICATE: axiom_boundary=locality and projectivity do not select beta, rho, phase odds, alpha, response branch, Ward law, or causal update")
    print("per_site: one null plus fifteen actual-edge-labelled Records on each of four spatial-cycle sites")
    print("per_region: every subset of the fixed four-site parent in two interacting geometry sectors")
    print("per_source: all 3,876 distinct four-site count sources at the declared response controls")
    print("lattice_wide: no infinite-volume, arbitrary-overlap, complete-Ward, curved/open, nonlinear, or Lorentzian theorem is claimed")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
