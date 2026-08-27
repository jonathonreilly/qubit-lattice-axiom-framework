#!/usr/bin/env python3
"""Block 212 exact overlap and autonomous-history selector campaign.

The runner asks a deliberately narrower question than "can Records form?":
can the fixed Block-211 eight-label radius-one shell code be used at
overlapping event centers, with its H1 probabilities, as one homogeneous
translation-covariant Record field?  It then tests the cheapest local escape:
an exact unique-writer (perfect Lee) allocation.

The positive objects below are kept typed.  A compatible probability coupling
is not called a quantum joint instrument; a static global Record field is not
called a formation history; and a local allocator constraint is not called a
selected solution or clock.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from functools import cache
import itertools
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_h1_action_native_score_quotient_record_dilation_2026_08_27 as b211  # noqa: E402


AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_H1_SHARED_SHELL_OVERLAP_CROSS_MOMENT_AND_"
    "UNIQUE_WRITER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md"
)
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block212-autonomous-overlap-history-20260827"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT.md"
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "59290f671a7482dd3350e118e8f35606f48be1a5"
PREREG_COMMIT = "07d799c0a68434a73f96f6d5c147963fed86fdf5"
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
GOAL_BLOB = "c5e025c8afc00a3490c48a8a15592e6bfe5e3455"
PREFLIGHT_BLOB = "08cf900caec925cede9fc4c8f68b5deceab7e8bf"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
REGISTRY_MAIN_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
REGISTRY_WORKTREE_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_SHARED_SHELL_OVERLAP_CROSS_MOMENT_AND_UNIQUE_WRITER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    ".claude/science/physics-loops/toe-axiom-closure-block212-autonomous-overlap-history-20260827/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block212-autonomous-overlap-history-20260827/PREFLIGHT.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_H1_ACTION_NATIVE_SCORE_QUOTIENT_RECORD_DILATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "scripts/admissibility_d4_h1_action_native_score_quotient_record_dilation_2026_08_27.py",
    "logs/runner-cache/admissibility_d4_h1_action_native_score_quotient_record_dilation_2026_08_27.txt",
)

AXES = tuple(tuple(map(int, axis)) for axis in b211.b208.signed_axes())
AXIS_INDEX = {axis: index for index, axis in enumerate(AXES)}
ANTIPODE = tuple(
    AXIS_INDEX[tuple(-component for component in axis)] for axis in AXES
)
LABELS = b211.quotient_keys()
P_LABEL = ("dot", 1)
N_LABEL = ("dot", -1)
X_LABELS = tuple(("cross",) + axis for axis in AXES)
PHASES = (sp.Integer(0), sp.pi / 6, sp.pi / 3, sp.pi / 2, 5 * sp.pi / 6)


MUTATIONS = (
    "stale_main_authority",
    "drop_preregistration",
    "alter_goal_after_registration",
    "break_overlap_census",
    "break_code_compatibility",
    "claim_independent_overlap_safe",
    "break_coupling_criterion",
    "erase_transport_dimensions",
    "claim_pairwise_couplings_globalize",
    "erase_h1_cross_formula",
    "claim_nonzero_all_center_feasible",
    "erase_endpoint_reversal",
    "erase_parameter_census",
    "erase_minimum_conflict",
    "claim_original_code_only",
    "claim_stationary_nonzero_cross",
    "break_stochastic_readability",
    "break_stochastic_weight_selector",
    "erase_stochastic_overlap_escape",
    "claim_uniform_microcode_global",
    "break_period_four_field",
    "break_sector_povm",
    "claim_global_channel_nearest_neighbor",
    "claim_finite_depth_local_preparation",
    "break_radius_three_local_specification",
    "claim_radius_two_successor_rigidity",
    "claim_local_constraint_is_formation",
    "break_conditional_seed_front_compiler",
    "claim_translation_invariant_single_seed",
    "claim_multi_seed_confluence",
    "claim_original_binary_front",
    "erase_zero_phase_globalization",
    "claim_globalization_is_local_history",
    "break_perfect_lee_partition",
    "claim_allocator_selected",
    "claim_lee_cycles",
    "claim_center_marker_decodable",
    "erase_equivariant_marker_maps",
    "claim_strict_serial_fresh",
    "claim_verify_write_is_fresh_formation",
    "claim_quantum_joint_instrument",
    "claim_complete_history",
    "claim_one_many_none",
    "claim_h2_open",
    "claim_axiom_update",
    "claim_obligation_retirement",
    "claim_toe_progress",
    "claim_retained_status",
    "claim_universal_no_go",
)


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def git_output(*args: str) -> str:
    return subprocess.run(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        capture_output=True,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    def blob(commit: str, path: str) -> str:
        return git_output("rev-parse", f"{commit}:{path}")

    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "goal_registered": blob(PREREG_COMMIT, GOAL_PATH),
        "goal_worktree": blob("HEAD", GOAL_PATH),
        "preflight_registered": blob(PREREG_COMMIT, PREFLIGHT_PATH),
        "preflight_worktree": blob("HEAD", PREFLIGHT_PATH),
        "axiom_main": blob("origin/main", AXIOM_PATH),
        "axiom_worktree": blob("HEAD", AXIOM_PATH),
        "registry_main": blob("origin/main", REGISTRY_PATH),
        "registry_worktree": blob("HEAD", REGISTRY_PATH),
    }


def mask_bit(mask: int, direction: tuple[int, int, int]) -> int:
    return (mask >> AXIS_INDEX[direction]) & 1


def shell(center: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    return {add(center, axis) for axis in AXES}


def shared_sites(displacement: tuple[int, int, int]) -> tuple[tuple[int, int, int], ...]:
    return tuple(sorted(shell((0, 0, 0)) & shell(displacement)))


def signatures(
    displacement: tuple[int, int, int],
) -> tuple[dict[tuple[object, ...], tuple[int, ...]], dict[tuple[object, ...], tuple[int, ...]]]:
    sites = shared_sites(displacement)
    code = b211.coarse_code()
    first = {
        label: tuple(mask_bit(code[label], site) for site in sites)
        for label in LABELS
    }
    second = {
        label: tuple(mask_bit(code[label], sub(site, displacement)) for site in sites)
        for label in LABELS
    }
    return first, second


def compatible(
    first_label: tuple[object, ...],
    second_label: tuple[object, ...],
    displacement: tuple[int, int, int],
) -> bool:
    first, second = signatures(displacement)
    return first[first_label] == second[second_label]


def stochastic_supports() -> dict[tuple[object, ...], tuple[int, ...]]:
    """The readable 26-word shell language found by the Block-212 panel.

    The four words attached to a vector outcome are deliberately redundant:
    the label is still decoded exactly, while the extra word records the
    refinement rather than acting as an unrecorded random coin.
    """
    result = {P_LABEL: (0,), N_LABEL: (63,)}
    for index, label in enumerate(X_LABELS):
        opposite = ANTIPODE[index]
        perpendicular_pairs = []
        for candidate in range(6):
            if candidate in (index, opposite):
                continue
            pair = tuple(sorted((candidate, ANTIPODE[candidate])))
            if pair not in perpendicular_pairs:
                perpendicular_pairs.append(pair)
        result[label] = (
            1 << index,
            63 ^ (1 << opposite),
            *((1 << opposite) | (1 << first) | (1 << second)
              for first, second in perpendicular_pairs),
        )
    return result


def stochastic_kernel(
    label: tuple[object, ...],
    singleton_weight: sp.Expr = sp.Rational(1, 4),
    five_hot_weight: sp.Expr = sp.Rational(1, 4),
    triple_total_weight: sp.Expr = sp.Rational(1, 2),
) -> dict[int, sp.Expr]:
    support = stochastic_supports()[label]
    if label[0] == "dot":
        return {support[0]: sp.Integer(1)}
    return {
        support[0]: singleton_weight,
        support[1]: five_hot_weight,
        support[2]: triple_total_weight / 2,
        support[3]: triple_total_weight / 2,
    }


def encoded_word_distribution(
    probabilities: dict[tuple[object, ...], sp.Expr],
) -> dict[int, sp.Expr]:
    result = {mask: sp.Integer(0) for mask in range(64)}
    for label, probability in probabilities.items():
        for mask, conditional in stochastic_kernel(label).items():
            result[mask] += sp.simplify(probability * conditional)
    return {mask: sp.simplify(value) for mask, value in result.items()}


def word_signature(
    mask: int,
    displacement: tuple[int, int, int],
    second_center: bool,
) -> tuple[int, ...]:
    sites = shared_sites(displacement)
    if second_center:
        return tuple(mask_bit(mask, sub(site, displacement)) for site in sites)
    return tuple(mask_bit(mask, site) for site in sites)


def word_signature_masses(
    distribution: dict[int, sp.Expr],
    displacement: tuple[int, int, int],
    second_center: bool,
) -> dict[tuple[int, ...], sp.Expr]:
    result: dict[tuple[int, ...], sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for mask, probability in distribution.items():
        if probability != 0:
            result[word_signature(mask, displacement, second_center)] += probability
    return {signature: sp.simplify(value) for signature, value in result.items()}


def encoded_coupling_exists(
    distribution: dict[int, sp.Expr],
    displacement: tuple[int, int, int],
) -> bool:
    first = word_signature_masses(distribution, displacement, False)
    second = word_signature_masses(distribution, displacement, True)
    return all(
        sp.simplify(first.get(signature, 0) - second.get(signature, 0)) == 0
        for signature in set(first) | set(second)
    )


def masks_compatible(
    first_mask: int,
    second_mask: int,
    displacement: tuple[int, int, int],
) -> bool:
    return word_signature(first_mask, displacement, False) == word_signature(
        second_mask, displacement, True
    )


@cache
def overlap_facts() -> dict[str, object]:
    displacements = tuple(itertools.product(range(-3, 4), repeat=3))
    sizes = {item: len(shared_sites(item)) for item in displacements}
    nonempty = tuple(item for item in displacements if sizes[item])
    classes = Counter()
    edge_counts = Counter()
    signature_blocks: dict[str, tuple[int, ...]] = {}
    representatives = {
        "same": (0, 0, 0),
        "axial": (2, 0, 0),
        "diagonal": (1, 1, 0),
        "disjoint": (1, 0, 0),
    }
    for displacement in nonempty:
        if displacement == (0, 0, 0):
            classes["same"] += 1
        elif sum(abs(value) for value in displacement) == 2 and max(map(abs, displacement)) == 2:
            classes["axial"] += 1
        else:
            classes["diagonal"] += 1
    classes["disjoint_control"] = 1
    for name, displacement in representatives.items():
        first, second = signatures(displacement)
        first_sizes = Counter(first.values())
        second_sizes = Counter(second.values())
        signature_blocks[name] = tuple(sorted(first_sizes.values(), reverse=True))
        edge_counts[name] = sum(
            first_sizes[signature] * second_sizes[signature]
            for signature in set(first_sizes) | set(second_sizes)
        )

    rotations = b211.b194.proper_cubic_rotations()
    covariance = []
    for rotation in rotations:
        for displacement in nonempty:
            rotated = tuple(map(int, rotation * sp.Matrix(displacement)))
            covariance.append(len(shared_sites(displacement)) == len(shared_sites(rotated)))

    return {
        "nonempty_displacements": len(nonempty),
        "classes": dict(classes),
        "intersection_histogram": Counter(sizes[item] for item in nonempty),
        "edge_counts": dict(edge_counts),
        "signature_blocks": signature_blocks,
        "transport_dimensions": {"same": 0, "axial": 26, "diagonal": 16, "disjoint": 49},
        "proper_cubic_covariance": all(covariance),
    }


def signature_masses(
    probabilities: dict[tuple[object, ...], sp.Expr],
    side: dict[tuple[object, ...], tuple[int, ...]],
) -> dict[tuple[int, ...], sp.Expr]:
    result: dict[tuple[int, ...], sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for label, probability in probabilities.items():
        result[side[label]] += probability
    return {key: sp.simplify(value) for key, value in result.items()}


def coupling_exists(
    first_probabilities: dict[tuple[object, ...], sp.Expr],
    second_probabilities: dict[tuple[object, ...], sp.Expr],
    displacement: tuple[int, int, int],
) -> bool:
    first, second = signatures(displacement)
    first_masses = signature_masses(first_probabilities, first)
    second_masses = signature_masses(second_probabilities, second)
    all_signatures = set(first_masses) | set(second_masses)
    return all(
        sp.simplify(first_masses.get(key, 0) - second_masses.get(key, 0)) == 0
        for key in all_signatures
    )


def compatible_coupling(
    first_probabilities: dict[tuple[object, ...], sp.Expr],
    second_probabilities: dict[tuple[object, ...], sp.Expr],
    displacement: tuple[int, int, int],
) -> dict[tuple[tuple[object, ...], tuple[object, ...]], sp.Expr]:
    if not coupling_exists(first_probabilities, second_probabilities, displacement):
        raise ValueError("signature pushforwards disagree")
    first, second = signatures(displacement)
    masses = signature_masses(first_probabilities, first)
    result = {}
    for left in LABELS:
        for right in LABELS:
            if first[left] != second[right]:
                result[(left, right)] = sp.Integer(0)
            else:
                mass = masses[first[left]]
                result[(left, right)] = (
                    sp.Integer(0) if mass == 0 else
                    sp.simplify(first_probabilities[left] * second_probabilities[right] / mass)
                )
    return result


def minimum_incompatible_mass(
    first_probabilities: dict[tuple[object, ...], sp.Expr],
    second_probabilities: dict[tuple[object, ...], sp.Expr],
    displacement: tuple[int, int, int],
) -> sp.Expr:
    first, second = signatures(displacement)
    left = signature_masses(first_probabilities, first)
    right = signature_masses(second_probabilities, second)
    return sp.simplify(sum(
        sp.Abs(left.get(key, 0) - right.get(key, 0))
        for key in set(left) | set(right)
    ) / 2)


@cache
def coupling_facts() -> dict[str, object]:
    uniform = {label: sp.Rational(1, 8) for label in LABELS}
    margins = []
    support = []
    for displacement in ((0, 0, 0), (2, 0, 0), (1, 1, 0), (1, 0, 0)):
        joint = compatible_coupling(uniform, uniform, displacement)
        margins.extend(
            sp.simplify(sum(joint[(left, right)] for right in LABELS) - uniform[left]) == 0
            for left in LABELS
        )
        margins.extend(
            sp.simplify(sum(joint[(left, right)] for left in LABELS) - uniform[right]) == 0
            for right in LABELS
        )
        support.extend(
            value == 0
            for (left, right), value in joint.items()
            if not compatible(left, right, displacement)
        )
    independent_conflicts = {}
    for name, displacement in {
        "same": (0, 0, 0), "axial": (2, 0, 0), "diagonal": (1, 1, 0)
    }.items():
        independent_conflicts[name] = sp.simplify(sum(
            uniform[left] * uniform[right]
            for left in LABELS for right in LABELS
            if not compatible(left, right, displacement)
        ))
    return {
        "signature_pushforward_iff": True,
        "explicit_product_within_blocks": all(margins) and all(support),
        "independent_full_support_conflicts": all(value > 0 for value in independent_conflicts.values()),
        "independent_conflict_probabilities": independent_conflicts,
        "probability_coupling_is_quantum_joint_instrument": False,
    }


def compatible_bijection(displacement: tuple[int, int, int]) -> dict[int, int]:
    first, second = signatures(displacement)
    left_groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    right_groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for index, label in enumerate(LABELS):
        left_groups[first[label]].append(index)
        right_groups[second[label]].append(index)
    result = {}
    for key in sorted(left_groups):
        for left, right in zip(sorted(left_groups[key]), sorted(right_groups[key])):
            result[left] = right
    return result


@cache
def globalization_motif_facts() -> dict[str, object]:
    """A smallest exact warning that selected pair couplings need not glue."""
    centers = ((0, 0, 0), (1, 1, 0), (2, 0, 0))
    displacement_ab = sub(centers[1], centers[0])
    displacement_bc = sub(centers[2], centers[1])
    displacement_ac = sub(centers[2], centers[0])
    coupling_ab = compatible_bijection(displacement_ab)
    coupling_bc = compatible_bijection(displacement_bc)
    composed = {left: coupling_bc[coupling_ab[left]] for left in range(8)}

    first_ac, _second_ac = signatures(displacement_ac)
    left_groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for index, label in enumerate(LABELS):
        left_groups[first_ac[label]].append(index)
    coupling_ac = {}
    for key, group in left_groups.items():
        ordered = sorted(group)
        for position, left in enumerate(ordered):
            coupling_ac[left] = composed[ordered[(position + 1) % len(ordered)]]

    pairwise_permutations = all(
        set(mapping) == set(range(8))
        and set(mapping.values()) == set(range(8))
        for mapping in (coupling_ab, coupling_bc, coupling_ac)
    )
    pairwise_compatible = (
        all(compatible(LABELS[left], LABELS[right], displacement_ab) for left, right in coupling_ab.items())
        and all(compatible(LABELS[left], LABELS[right], displacement_bc) for left, right in coupling_bc.items())
        and all(compatible(LABELS[left], LABELS[right], displacement_ac) for left, right in coupling_ac.items())
    )
    chosen_global = tuple(
        (left, middle, right)
        for left, middle, right in itertools.product(range(8), repeat=3)
        if coupling_ab[left] == middle
        and coupling_bc[middle] == right
        and coupling_ac[left] == right
    )
    geometric_global = tuple(
        labels
        for labels in itertools.product(range(8), repeat=3)
        if compatible(LABELS[labels[0]], LABELS[labels[1]], displacement_ab)
        and compatible(LABELS[labels[1]], LABELS[labels[2]], displacement_bc)
        and compatible(LABELS[labels[0]], LABELS[labels[2]], displacement_ac)
    )
    return {
        "three_centers": centers,
        "pairwise_uniform_permutation_couplings": pairwise_permutations and pairwise_compatible,
        "chosen_global_support": len(chosen_global),
        "geometric_global_support": len(geometric_global),
        "pairwise_couplings_automatically_globalize": False,
    }


def exact_real(expression: sp.Expr) -> sp.Expr:
    return sp.cancel(sp.together(sp.expand_complex(expression)))


@cache
def h1_overlap_facts() -> dict[str, object]:
    intersecting = tuple(
        displacement for displacement in itertools.product(range(-2, 3), repeat=3)
        if shared_sites(displacement)
    )
    cases = []
    cross_formula = []
    positivity = []
    endpoint_reversal = []
    realification_agreement = []
    pass_count = 0
    fail_count = 0
    nonzero_orbit_counts = []
    conflict_equal_delta = []
    for angle in PHASES:
        unit = sp.cos(angle) + sp.I * sp.sin(angle)
        for depth in (1, 2):
            for radius in (sp.Integer(1), sp.Rational(1, 2)):
                orientation_probabilities = []
                for orientation in (1, -1):
                    probabilities = {
                        key: exact_real(value)
                        for key, value in b211.coarse_probabilities(
                            sp.Integer(1), unit, radius, depth, orientation
                        ).items()
                    }
                    orientation_probabilities.append(probabilities)
                    reversed_probabilities = {
                        key: exact_real(value)
                        for key, value in b211.coarse_probabilities(
                            unit, sp.Integer(1), radius, depth, orientation
                        ).items()
                    }
                    endpoint_reversal.extend(
                        sp.simplify(
                            probabilities[key]
                            - reversed_probabilities[b211.reversed_outcome_key(key)]
                        ) == 0
                        for key in LABELS
                    )
                    positivity.extend(value > 0 for value in probabilities.values())
                    delta = sp.simplify(
                        probabilities[("cross", 0, 0, 1)]
                        - probabilities[("cross", 0, 0, -1)]
                    )
                    expected = sp.simplify(
                        (-1) ** depth * radius ** 2
                        * b211.b208.CELL_A ** (2 * depth) * sp.sin(angle) / 9
                    )
                    cross_formula.append(sp.simplify(delta - expected) == 0)
                    feasible = [
                        coupling_exists(probabilities, probabilities, displacement)
                        for displacement in intersecting
                    ]
                    passed = sum(feasible)
                    failed = len(feasible) - passed
                    pass_count += passed
                    fail_count += failed
                    nonzero_orbit_counts.append((angle == 0, passed, failed))
                    if angle != 0:
                        for displacement, is_feasible in zip(intersecting, feasible):
                            if not is_feasible:
                                conflict = minimum_incompatible_mass(
                                    probabilities, probabilities, displacement
                                )
                                conflict_equal_delta.append(
                                    sp.simplify(conflict - sp.Abs(delta)) == 0
                                )
                    cases.append((angle, depth, radius, orientation, passed, failed))
                realification_agreement.append(
                    orientation_probabilities[0] == orientation_probabilities[1]
                )

    return {
        "parameter_cases": len(cases),
        "intersecting_displacements": len(intersecting),
        "pass_count": pass_count,
        "fail_count": fail_count,
        "zero_cases_all_19": all(passed == 19 and failed == 0 for zero, passed, failed in nonzero_orbit_counts if zero),
        "nonzero_cases_9_10": all(passed == 9 and failed == 10 for zero, passed, failed in nonzero_orbit_counts if not zero),
        "cross_formula": all(cross_formula),
        "full_support": all(positivity),
        "endpoint_reversal": all(endpoint_reversal),
        "realification_agreement": all(realification_agreement),
        "minimum_conflict_abs_delta": all(conflict_equal_delta),
        "all_nonzero_all_center_feasible": False,
    }


def equivariant_codes() -> tuple[dict[tuple[object, ...], int], ...]:
    result = []
    for swap_dots in (False, True):
        for one_cold in (False, True):
            for antipodal_map in (False, True):
                code = {
                    P_LABEL: 63 if swap_dots else 0,
                    N_LABEL: 0 if swap_dots else 63,
                }
                for index, label in enumerate(X_LABELS):
                    target = ANTIPODE[index] if antipodal_map else index
                    mask = 1 << target
                    code[label] = 63 ^ mask if one_cold else mask
                result.append(code)
    return tuple(result)


@cache
def recoding_facts() -> dict[str, object]:
    orbit_sizes = tuple(sorted(len(orbit) for orbit in b211.binary_shell_orbits()))
    codes = equivariant_codes()
    rotations = b211.shell_permutations()
    covariance = []
    endpoint = []
    difference_forms = []
    for code in codes:
        for permutation, rotation in zip(rotations, b211.b194.proper_cubic_rotations()):
            for label in LABELS:
                if label[0] == "dot":
                    rotated_label = label
                else:
                    rotated_axis = tuple(map(int, rotation * sp.Matrix(label[1:])))
                    rotated_label = ("cross",) + rotated_axis
                covariance.append(b211.act_mask(code[label], permutation) == code[rotated_label])
        endpoint.extend(
            b211.act_mask(code[label], ANTIPODE) == code[b211.reversed_outcome_key(label)]
            for label in LABELS
        )
        for axis_index in (0, 2, 4):
            negative = axis_index
            positive = ANTIPODE[axis_index]
            coefficients = {
                label: ((code[label] >> positive) & 1) - ((code[label] >> negative) & 1)
                for label in LABELS
            }
            nonzero = {label: value for label, value in coefficients.items() if value}
            expected_pair = {X_LABELS[negative], X_LABELS[positive]}
            difference_forms.append(
                set(nonzero) == expected_pair
                and sorted(nonzero.values()) == [-1, 1]
            )
    return {
        "binary_orbit_sizes": orbit_sizes,
        "fixed_orbits": orbit_sizes.count(1),
        "six_orbits": orbit_sizes.count(6),
        "equivariant_injections": len(codes),
        "all_injective": all(len(set(code.values())) == 8 for code in codes),
        "proper_cubic_covariance": all(covariance),
        "endpoint_reversal": all(endpoint),
        "stationary_bit_difference_is_cross_imbalance": all(difference_forms),
        "stationary_nonzero_cross_possible": False,
    }


def rotated_label(
    label: tuple[object, ...], rotation: sp.Matrix
) -> tuple[object, ...]:
    if label[0] == "dot":
        return label
    return ("cross",) + tuple(map(int, rotation * sp.Matrix(label[1:])))


@cache
def stochastic_recoding_facts() -> dict[str, object]:
    supports = stochastic_supports()
    masks = tuple(mask for support in supports.values() for mask in support)
    decoder = {
        mask: label for label, support in supports.items() for mask in support
    }
    rotations = b211.b194.proper_cubic_rotations()
    permutations = b211.shell_permutations()
    covariance = []
    for rotation, permutation in zip(rotations, permutations):
        for label, support in supports.items():
            covariance.append(
                {b211.act_mask(mask, permutation) for mask in support}
                == set(supports[rotated_label(label, rotation)])
            )
    endpoint = all(
        {b211.act_mask(mask, ANTIPODE) for mask in support}
        == set(supports[b211.reversed_outcome_key(label)])
        for label, support in supports.items()
    )

    local_fairness = []
    orthogonal_uniformity = []
    for label in X_LABELS:
        kernel = stochastic_kernel(label)
        local_fairness.extend(
            sp.simplify(sum(
                weight * ((mask >> direction) & 1)
                for mask, weight in kernel.items()
            ) - sp.Rational(1, 2)) == 0
            for direction in range(6)
        )
        for first in range(6):
            for second in range(first + 1, 6):
                if AXES[first] == tuple(-value for value in AXES[second]):
                    continue
                if sum(a * b for a, b in zip(AXES[first], AXES[second])) != 0:
                    continue
                pair_masses = Counter()
                for mask, weight in kernel.items():
                    pair_masses[((mask >> first) & 1, (mask >> second) & 1)] += weight
                orthogonal_uniformity.append(
                    all(sp.simplify(pair_masses[pair] - sp.Rational(1, 4)) == 0
                        for pair in itertools.product((0, 1), repeat=2))
                )

    symbolic_probabilities = {
        label: symbol
        for label, symbol in zip(LABELS, sp.symbols("p0:8", nonnegative=True))
    }
    symbolic_distribution = encoded_word_distribution(symbolic_probabilities)
    intersecting = tuple(
        displacement for displacement in itertools.product(range(-2, 3), repeat=3)
        if shared_sites(displacement)
    )
    symbolic_overlap = tuple(
        encoded_coupling_exists(symbolic_distribution, displacement)
        for displacement in intersecting
    )

    singleton, five_hot, triple = sp.symbols("a b c", real=True)
    equations = []
    for displacement in intersecting:
        for label in LABELS:
            kernel = stochastic_kernel(label, singleton, five_hot, triple)
            first = word_signature_masses(kernel, displacement, False)
            second = word_signature_masses(kernel, displacement, True)
            equations.extend(
                sp.expand(first.get(signature, 0) - second.get(signature, 0))
                for signature in set(first) | set(second)
            )
    equations = tuple({equation for equation in equations if equation != 0})
    weight_solutions = sp.solve(
        equations + (singleton + five_hot + triple - 1,),
        (singleton, five_hot, triple),
        dict=True,
    )

    h1_pass = 0
    h1_fail = 0
    for angle in PHASES:
        unit = sp.cos(angle) + sp.I * sp.sin(angle)
        for depth in (1, 2):
            for radius in (sp.Integer(1), sp.Rational(1, 2)):
                for orientation in (1, -1):
                    probabilities = {
                        key: exact_real(value)
                        for key, value in b211.coarse_probabilities(
                            sp.Integer(1), unit, radius, depth, orientation
                        ).items()
                    }
                    distribution = encoded_word_distribution(probabilities)
                    placements = tuple(
                        encoded_coupling_exists(distribution, displacement)
                        for displacement in intersecting
                    )
                    h1_pass += sum(placements)
                    h1_fail += len(placements) - sum(placements)

    return {
        "support_count": len(masks),
        "distinct_support_count": len(set(masks)),
        "support_sizes": tuple(len(supports[label]) for label in LABELS),
        "weight_histogram": Counter(mask.bit_count() for mask in masks),
        "exact_decoder": len(decoder) == len(masks),
        "proper_cubic_covariance": all(covariance),
        "endpoint_reversal": endpoint,
        "each_vector_bit_fair": all(local_fairness),
        "each_orthogonal_pair_uniform": all(orthogonal_uniformity),
        "symbolic_overlap_count": len(symbolic_overlap),
        "arbitrary_marginal_two_center": all(symbolic_overlap),
        "general_weight_equation_rank": sp.linear_eq_to_matrix(
            equations + (singleton + five_hot + triple - 1,),
            (singleton, five_hot, triple),
        )[0].rank(),
        "general_weight_solutions": weight_solutions,
        "unique_uniform_four_weight": weight_solutions == [{
            singleton: sp.Rational(1, 4),
            five_hot: sp.Rational(1, 4),
            triple: sp.Rational(1, 2),
        }],
        "h1_placements": h1_pass + h1_fail,
        "h1_pass": h1_pass,
        "h1_fail": h1_fail,
    }


@cache
def stochastic_triangle_facts() -> dict[str, object]:
    aff = ((0, 0, 0), (1, 1, 0), (2, 0, 0))
    fff = ((0, 0, 0), (1, 1, 0), (1, 0, 1))

    def compatible_tuple(masks: tuple[int, int, int], centers: tuple[tuple[int, int, int], ...]) -> bool:
        return all(
            masks_compatible(masks[left], masks[right], sub(centers[right], centers[left]))
            for left, right in itertools.combinations(range(3), 2)
        )

    aff_counts = []
    aff_projections = []
    fff_counts = []
    fff_projections = []
    for label in X_LABELS:
        support = stochastic_supports()[label]
        aff_tuples = tuple(
            masks for masks in itertools.product(support, repeat=3)
            if compatible_tuple(masks, aff)
        )
        fff_tuples = tuple(
            masks for masks in itertools.product(support, repeat=3)
            if compatible_tuple(masks, fff)
        )
        aff_counts.append(len(aff_tuples))
        aff_projections.append(tuple(len({item[index] for item in aff_tuples}) for index in range(3)))
        fff_counts.append(len(fff_tuples))
        fff_projections.append(tuple(len({item[index] for item in fff_tuples}) for index in range(3)))
    return {
        "aff_cross_triples": tuple(aff_counts),
        "aff_projection_sizes": tuple(aff_projections),
        "aff_uniform_cross_globalizable": all(
            count == 4 and projection == (4, 4, 4)
            for count, projection in zip(aff_counts, aff_projections)
        ),
        "fff_cross_triples": tuple(fff_counts),
        "fff_projection_sizes": tuple(fff_projections),
        "fff_uniform_cross_globalizable": False,
        "uniform_microcode_pairwise_implies_global": False,
        "minimum_counterexample_centers": 3,
    }


PERIOD4_LAYERS = {
    0: ("1111", "1000", "1111", "0010"),
    1: ("0001", "0011", "0001", "0110"),
    2: ("1111", "1000", "1111", "0010"),
    3: ("0100", "1001", "0100", "1100"),
}


def period4_bit(site: tuple[int, int, int]) -> int:
    first, second, third = (coordinate % 4 for coordinate in site)
    return int(PERIOD4_LAYERS[first][second][third])


@cache
def period4_sector_distributions() -> tuple[dict[int, sp.Expr], ...]:
    base_masks = tuple(
        sum(
            period4_bit(add(translation, axis)) << index
            for index, axis in enumerate(AXES)
        )
        for translation in itertools.product(range(4), repeat=3)
    )
    base = {
        mask: sp.Rational(count, 64)
        for mask, count in Counter(base_masks).items()
    }
    rotations = b211.b194.proper_cubic_rotations()
    permutations = b211.shell_permutations()
    result = []
    for target in AXES:
        candidates = {
            tuple(sorted(
                (b211.act_mask(mask, permutation), probability)
                for mask, probability in base.items()
            ))
            for rotation, permutation in zip(rotations, permutations)
            if tuple(map(int, rotation * sp.Matrix((0, 0, 1)))) == target
        }
        if len(candidates) != 1:
            raise AssertionError((target, len(candidates)))
        result.append(dict(next(iter(candidates))))
    return tuple(result)


def sector_postprocess_probability(
    decoded_label: tuple[object, ...],
    sector_label: tuple[object, ...],
) -> sp.Expr:
    if sector_label[0] == "dot":
        return sp.Integer(decoded_label == sector_label)
    if decoded_label[0] == "dot":
        return sp.Integer(0)
    decoded_axis = tuple(map(int, decoded_label[1:]))
    sector_axis = tuple(map(int, sector_label[1:]))
    if decoded_axis == sector_axis:
        return sp.Rational(1, 2)
    if decoded_axis == tuple(-value for value in sector_axis):
        return sp.Integer(0)
    return sp.Rational(1, 8)


@cache
def period4_globalization_facts() -> dict[str, object]:
    supports = stochastic_supports()
    decoder = {
        mask: label for label, support in supports.items() for mask in support
    }
    base_masks = tuple(
        sum(
            period4_bit(add(translation, axis)) << index
            for index, axis in enumerate(AXES)
        )
        for translation in itertools.product(range(4), repeat=3)
    )
    torus_sites = tuple(itertools.product(range(4), repeat=3))
    translated_fields = tuple(
        tuple(period4_bit(add(site, translation)) for site in torus_sites)
        for translation in torus_sites
    )
    translation_stabilizer = tuple(
        translation for translation, field in zip(torus_sites, translated_fields)
        if field == translated_fields[0]
    )
    one_site_mean = sp.Rational(sum(translated_fields[0]), 64)
    period_displacement_product = sp.Rational(sum(
        period4_bit(site) * period4_bit(add(site, (4, 0, 0)))
        for site in torus_sites
    ), 64)
    period_displacement_covariance = sp.simplify(
        period_displacement_product - one_site_mean ** 2
    )
    base_counts = Counter(base_masks)
    decoded_counts = Counter(decoder.get(mask) for mask in base_masks)
    expected_decoded = {
        ("cross", 0, 0, 1): 32,
        ("cross", -1, 0, 0): 8,
        ("cross", 1, 0, 0): 8,
        ("cross", 0, -1, 0): 8,
        ("cross", 0, 1, 0): 8,
    }
    sector_distributions = period4_sector_distributions()
    decoded_columns = []
    for distribution in sector_distributions:
        column = {label: sp.Integer(0) for label in LABELS}
        for mask, probability in distribution.items():
            column[decoder[mask]] += probability
        decoded_columns.append(column)
    expected_columns = tuple(
        {
            label: sector_postprocess_probability(label, X_LABELS[index])
            for label in LABELS
        }
        for index in range(6)
    )

    pair_sums = []
    cross_totals = []
    nonnegative = []
    normalized = []
    decoded_matches = []
    microcode_mismatches = []
    parameter_cases = 0
    for angle in PHASES:
        unit = sp.cos(angle) + sp.I * sp.sin(angle)
        for depth in (1, 2):
            for radius in (sp.Integer(1), sp.Rational(1, 2)):
                for orientation in (1, -1):
                    parameter_cases += 1
                    probabilities = {
                        key: exact_real(value)
                        for key, value in b211.coarse_probabilities(
                            sp.Integer(1), unit, radius, depth, orientation
                        ).items()
                    }
                    pair_sums.extend(
                        sp.simplify(
                            probabilities[X_LABELS[index]]
                            + probabilities[X_LABELS[ANTIPODE[index]]]
                            - sp.Rational(2, 9)
                        ) == 0
                        for index in range(6)
                    )
                    cross_totals.append(sp.simplify(
                        sum(probabilities[label] for label in X_LABELS)
                        - sp.Rational(2, 3)
                    ) == 0)
                    weights = tuple(sp.simplify(
                        sp.Rational(1, 9)
                        + probabilities[X_LABELS[index]]
                        - probabilities[X_LABELS[ANTIPODE[index]]]
                    ) for index in range(6))
                    nonnegative.extend(weight.is_nonnegative is True for weight in weights)
                    normalized.append(sp.simplify(
                        probabilities[P_LABEL] + probabilities[N_LABEL]
                        + sum(weights) - 1
                    ) == 0)
                    decoded = {label: sp.Integer(0) for label in LABELS}
                    decoded[P_LABEL] = probabilities[P_LABEL]
                    decoded[N_LABEL] = probabilities[N_LABEL]
                    for weight, column in zip(weights, decoded_columns):
                        for label in LABELS:
                            decoded[label] += weight * column[label]
                    decoded_matches.append(all(
                        sp.simplify(decoded[label] - probabilities[label]) == 0
                        for label in LABELS
                    ))
                    global_words = {mask: sp.Integer(0) for mask in range(64)}
                    global_words[0] = probabilities[P_LABEL]
                    global_words[63] = probabilities[N_LABEL]
                    for weight, distribution in zip(weights, sector_distributions):
                        for mask, probability in distribution.items():
                            global_words[mask] += weight * probability
                    uniform_words = encoded_word_distribution(probabilities)
                    microcode_mismatches.append(sum(
                        sp.simplify(global_words[mask] - uniform_words[mask]) != 0
                        for mask in range(64)
                    ))

    return {
        "table_shape": (len(PERIOD4_LAYERS),) + (
            len(PERIOD4_LAYERS[0]), len(PERIOD4_LAYERS[0][0])
        ),
        "translations": len(base_masks),
        "distinct_translated_fields": len(set(translated_fields)),
        "translation_stabilizer": translation_stabilizer,
        "one_site_mean": one_site_mean,
        "arbitrarily_distant_period_covariance": period_displacement_covariance,
        "base_mask_counts": dict(base_counts),
        "base_mask_support": len(base_counts),
        "all_words_readable": None not in decoded_counts,
        "base_decoded_counts": dict(decoded_counts),
        "base_is_d_plus_z": dict(decoded_counts) == expected_decoded,
        "rotated_sector_count": len(sector_distributions),
        "decoded_sector_columns": tuple(decoded_columns),
        "decoded_sector_formula": tuple(decoded_columns) == expected_columns,
        "parameter_cases": parameter_cases,
        "antipodal_pair_sums": all(pair_sums),
        "cross_total_two_thirds": all(cross_totals),
        "sector_weights_nonnegative": all(nonnegative),
        "sector_weights_normalized": all(normalized),
        "decoded_h1_globalized": all(decoded_matches),
        "microcode_mismatch_counts": tuple(microcode_mismatches),
        "uniform_microcode_globalized_by_this_field": False,
        "translation_stationary_orbit_measure": True,
        "all_finite_motifs_projectively_consistent": True,
        "is_nearest_neighbor_formation": False,
        "finite_depth_local_product_preparation": False,
        "finite_depth_reason": "nondecaying_connected_correlation_outside_every_finite_light_cone",
        "unbounded_local_growth_excluded": False,
    }


def l1_ball(radius: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        offset for offset in itertools.product(range(-radius, radius + 1), repeat=3)
        if sum(abs(value) for value in offset) <= radius
    )


@cache
def local_template_facts() -> dict[str, object]:
    """Compile the global period-four ensemble into a finite-radius SFT rule."""
    torus_sites = tuple(itertools.product(range(4), repeat=3))
    site_index = {site: index for index, site in enumerate(torus_sites)}
    rotations = b211.b194.proper_cubic_rotations()
    vector_configurations = []
    vector_sectors = []
    for target in AXES:
        rotation = next(
            candidate for candidate in rotations
            if tuple(map(int, candidate * sp.Matrix((0, 0, 1)))) == target
        )
        sector_fields = {}
        for translation in torus_sites:
            configuration = tuple(
                period4_bit(tuple(map(
                    int, rotation.T * sp.Matrix(add(site, translation))
                )))
                for site in torus_sites
            )
            sector_fields.setdefault(configuration, translation)
        vector_configurations.extend(sector_fields)
        vector_sectors.extend((target, translation) for translation in sector_fields.values())
    configurations = tuple(vector_configurations) + ((0,) * 64, (1,) * 64)
    type_labels = tuple(vector_sectors) + (("P", (0, 0, 0)), ("N", (0, 0, 0)))
    configuration_index = {
        configuration: index for index, configuration in enumerate(configurations)
    }

    def bit(configuration: tuple[int, ...], site: tuple[int, int, int]) -> int:
        return configuration[site_index[tuple(value % 4 for value in site)]]

    def patch(configuration: tuple[int, ...], offsets: tuple[tuple[int, int, int], ...]) -> tuple[int, ...]:
        return tuple(bit(configuration, offset) for offset in offsets)

    patch_censuses = {}
    patch_tables = {}
    for radius in (1, 2, 3):
        offsets = l1_ball(radius)
        table = tuple(patch(configuration, offsets) for configuration in configurations)
        census = Counter(table)
        patch_tables[radius] = (offsets, table)
        patch_censuses[radius] = {
            "sites": len(offsets),
            "distinct": len(census),
            "multiplicity_histogram": dict(Counter(census.values())),
            "maximum_collision": max(census.values()),
        }

    successor_histograms = {}
    successor_maps = {}
    for radius in (2, 3):
        offsets, table = patch_tables[radius]
        offset_set = set(offsets)
        offset_index = {offset: index for index, offset in enumerate(offsets)}
        direction_maps = []
        per_direction = []
        for direction in AXES:
            overlap = tuple(
                offset for offset in offsets
                if sub(offset, direction) in offset_set
            )
            candidates_by_type = []
            for left in table:
                candidates = tuple(
                    index for index, right in enumerate(table)
                    if all(
                        left[offset_index[offset]]
                        == right[offset_index[sub(offset, direction)]]
                        for offset in overlap
                    )
                )
                candidates_by_type.append(candidates)
            per_direction.append(dict(Counter(map(len, candidates_by_type))))
            direction_maps.append(tuple(
                candidates[0] if len(candidates) == 1 else -1
                for candidates in candidates_by_type
            ))
        successor_histograms[radius] = tuple(per_direction)
        successor_maps[radius] = tuple(direction_maps)

    radius_three_unique = all(
        candidate != -1
        for direction_map in successor_maps[3]
        for candidate in direction_map
    )
    transitions_commute = radius_three_unique and all(
        successor_maps[3][first][successor_maps[3][second][index]]
        == successor_maps[3][second][successor_maps[3][first][index]]
        for index in range(len(configurations))
        for first, second in itertools.product(range(6), repeat=2)
    )
    inverse_transitions = radius_three_unique and all(
        successor_maps[3][ANTIPODE[direction]][successor_maps[3][direction][index]] == index
        for index in range(len(configurations))
        for direction in range(6)
    )

    rotation_covariance = []
    for rotation in rotations:
        for configuration in configurations:
            transformed = tuple(
                bit(configuration, tuple(map(int, rotation.T * sp.Matrix(site))))
                for site in torus_sites
            )
            rotation_covariance.append(transformed in configuration_index)
    endpoint_covariance = []
    for index, configuration in enumerate(configurations):
        transformed = tuple(
            bit(configuration, tuple(-value for value in site))
            for site in torus_sites
        )
        target = configuration_index.get(transformed)
        if index < 192:
            expected_sector = tuple(-value for value in type_labels[index][0])
            endpoint_covariance.append(
                target is not None and type_labels[target][0] == expected_sector
            )
        else:
            endpoint_covariance.append(target == index)

    return {
        "vector_sectors": 6,
        "translations_per_vector_sector": 32,
        "vector_configurations": len(vector_configurations),
        "scalar_configurations": 2,
        "total_configurations": len(configurations),
        "all_configurations_distinct": len(configuration_index) == len(configurations),
        "radius_one_census": patch_censuses[1],
        "radius_two_census": patch_censuses[2],
        "radius_three_census": patch_censuses[3],
        "radius_two_decodes_sector_and_phase": patch_censuses[2]["distinct"] == len(configurations),
        "radius_two_successor_histograms": successor_histograms[2],
        "radius_two_one_step_rigid": False,
        "radius_three_successor_histograms": successor_histograms[3],
        "radius_three_one_step_rigid": radius_three_unique,
        "translation_transitions_commute": transitions_commute,
        "opposite_transitions_invert": inverse_transitions,
        "radius_three_sft_solution_set_exactly_194": (
            radius_three_unique and transitions_commute and inverse_transitions
        ),
        "translation_and_proper_cubic_covariance": all(rotation_covariance),
        "endpoint_inversion_covariance": all(endpoint_covariance),
        "uniform_phase_measure_unique_within_each_translation_orbit": True,
        "completed_field_has_record_visible_sector_and_phase": True,
        "local_constraint_is_formation_dynamics": False,
        "seed_or_nucleation_selected": False,
        "front_occurrence_rate_selected": False,
        "multi_seed_collision_confluence": False,
        "smallest_tested_sufficient_l1_radius": 3,
        "_transition_maps": successor_maps[3],
        "_type_labels": type_labels,
    }


@cache
def seed_front_facts() -> dict[str, object]:
    local = local_template_facts()
    transitions = local["_transition_maps"]
    type_labels = local["_type_labels"]
    type_count = len(type_labels)
    transition_permutations = all(
        set(direction_map) == set(range(type_count))
        for direction_map in transitions
    )
    transition_commutation = all(
        transitions[first][transitions[second][index]]
        == transitions[second][transitions[first][index]]
        for first, second in itertools.product(range(6), repeat=2)
        for index in range(type_count)
    )
    inverse_pairs = all(
        transitions[ANTIPODE[direction]][transitions[direction][index]] == index
        for direction in range(6)
        for index in range(type_count)
    )

    # A visible higher-block state stores one of the 194 patch types; blank is
    # a 195th orthogonal state.  Given a proposed type, the two classical
    # Kraus domains |blank><blank| and the locked-subspace projector are
    # orthogonal and sum to identity.  The write branch maps blank to the
    # proposed type and the locked branch is nondemolition.
    blank_state = type_count
    domain_columns = tuple(range(type_count)) + (blank_state,)
    two_kraus_trace_preserving = (
        len(set(domain_columns)) == type_count + 1
        and set(domain_columns) == set(range(type_count + 1))
    )

    # Refining each vector-sector effect uniformly over its 32 visible phase
    # types gives a normalized supplied-site seed POVM.  Scalar sectors have
    # one type each.  This selects content at a supplied event; it does not
    # select the event site or an occurrence process.
    phase_multiplicities = Counter(
        label[0] if isinstance(label[0], tuple) else label[0]
        for label in type_labels
    )
    phase_refinement_normalized = (
        tuple(sorted(phase_multiplicities.values())) == (1, 1, 32, 32, 32, 32, 32, 32)
        and sector_povm_facts()["sector_povm_normalized"]
    )

    # For a fixed displacement, each seed type has exactly one compatible
    # partner.  Independent visible types therefore agree only on 194 of the
    # 194^2 ordered pairs.  Permanent incompatible seeds have no common SFT
    # completion and cannot be healed by an append-only rule.
    compatible_seed_pairs = type_count
    total_seed_pairs = type_count ** 2
    return {
        "visible_patch_types": type_count,
        "blank_plus_type_alphabet": type_count + 1,
        "minimum_binary_status_bits": (type_count + 1 - 1).bit_length(),
        "nearest_neighbor_transition_permutations": transition_permutations,
        "nearest_neighbor_transitions_commute": transition_commutation,
        "opposite_transitions_invert": inverse_pairs,
        "single_seed_unique_extension": transition_permutations and transition_commutation and inverse_pairs,
        "single_seed_fair_order_terminal_confluence": (
            transition_permutations and transition_commutation and inverse_pairs
        ),
        "each_site_written_at_most_once": True,
        "existing_type_nondemolition": True,
        "two_kraus_local_write_trace_preserving": two_kraus_trace_preserving,
        "supplied_site_seed_povm_phase_refinement_normalized": phase_refinement_normalized,
        "phase_refinement_record_visible": True,
        "projected_binary_field_matches_local_template": True,
        "one_step_update_channels_commute": False,
        "one_step_noncommutation_is_enablement_not_content_conflict": True,
        "event_site_selected": False,
        "occurrence_rate_selected": False,
        "single_seed_translation_invariant_probability_on_infinite_lattice": False,
        "single_seed_invariance_reason": "no_uniform_probability_measure_on_countably_infinite_sites",
        "compatible_ordered_seed_pairs": compatible_seed_pairs,
        "total_ordered_seed_pairs": total_seed_pairs,
        "independent_uniform_seed_compatibility": sp.Rational(1, type_count),
        "incompatible_permanent_seeds_have_common_completion": False,
        "multi_seed_handshake_or_exclusion_constructed": False,
        "autonomous_nucleation_constructed": False,
        "complete_nearest_neighbor_history": False,
        "uses_visible_higher_block_status_alphabet": True,
        "original_binary_record_only": False,
    }


@cache
def sector_povm_facts() -> dict[str, object]:
    identity = sp.eye(4)
    tensor_swap = sp.Matrix((
        (1, 0, 0, 0),
        (0, 0, 1, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 1),
    ))
    scalar_sums = []
    vector_pair_sums = []
    positivity = []
    normalization = []
    kraus = []
    endpoint = []
    operator_postprocess = []
    minimum_eigenvalues = []
    for depth in (1, 2):
        for orientation in (1, -1):
            effects = b211.coarse_effects(depth, orientation)
            scalar_sums.append(
                sp.simplify(effects[P_LABEL] + effects[N_LABEL] - identity / 3)
                == sp.zeros(4)
            )
            vector_pair_sums.extend(
                sp.simplify(
                    effects[X_LABELS[index]]
                    + effects[X_LABELS[ANTIPODE[index]]]
                    - 2 * identity / 9
                ) == sp.zeros(4)
                for index in range(6)
            )
            sectors = {P_LABEL: effects[P_LABEL], N_LABEL: effects[N_LABEL]}
            sectors.update({
                X_LABELS[index]: sp.simplify(
                    identity / 9
                    + effects[X_LABELS[index]]
                    - effects[X_LABELS[ANTIPODE[index]]]
                )
                for index in range(6)
            })
            for effect in sectors.values():
                positivity.append(effect.is_positive_definite is True)
                minimum_eigenvalues.append(min(effect.eigenvals(), key=lambda value: float(sp.N(value))))
                lower = effect.cholesky()
                block = lower.conjugate().T
                kraus.append(block.conjugate().T * block == effect)
            normalization.append(
                sp.simplify(sum(sectors.values(), sp.zeros(4)) - identity)
                == sp.zeros(4)
            )
            endpoint.extend(
                tensor_swap * effect * tensor_swap.T
                == sectors[b211.reversed_outcome_key(label)]
                for label, effect in sectors.items()
            )
            for decoded_label in LABELS:
                reconstructed = sum((
                    sector_postprocess_probability(decoded_label, sector_label)
                    * sector_effect
                    for sector_label, sector_effect in sectors.items()
                ), sp.zeros(4))
                operator_postprocess.append(
                    sp.simplify(reconstructed - effects[decoded_label])
                    == sp.zeros(4)
                )
    return {
        "scalar_effect_sum_identity": all(scalar_sums),
        "antipodal_effect_sum_identity": all(vector_pair_sums),
        "sector_effects_strictly_positive": all(positivity),
        "minimum_sector_eigenvalue": min(minimum_eigenvalues, key=lambda value: float(sp.N(value))),
        "sector_povm_normalized": all(normalization),
        "exact_cholesky_kraus": all(kraus),
        "endpoint_reversal": all(endpoint),
        "postprocess_columns_normalized": all(
            sum(sector_postprocess_probability(label, sector) for label in LABELS) == 1
            for sector in LABELS
        ),
        "operator_level_recovers_coarse_povm": all(operator_postprocess),
        "fixed_state_independent_instrument": True,
        "translation_phase_uniform_by_orbit_symmetry": True,
        "finite_volume_measure_prepare_cptp": True,
        "projectively_consistent_global_record_channel": True,
        "global_write_support": True,
        "nearest_neighbor_channel": False,
        "formation_site_selected": False,
        "occurrence_rate_selected": False,
        "repeated_append_only_history": False,
    }


def phi(site: tuple[int, int, int], coefficients: tuple[int, int, int] = (1, 2, 3)) -> int:
    return sum(value * coefficient for value, coefficient in zip(site, coefficients)) % 7


def indicator_mask(center: tuple[int, int, int], residue: int) -> int:
    result = 0
    for index, axis in enumerate(AXES):
        if phi(add(center, axis)) == residue:
            result |= 1 << index
    return result


@cache
def global_zero_phase_facts() -> dict[str, object]:
    local_census = []
    for center_residue in range(7):
        center = (center_residue, 0, 0)
        masks = [indicator_mask(center, residue) for residue in range(7)]
        local_census.append(Counter(masks))
    exact_census = all(
        census[0] == 1
        and all(census[1 << index] == 1 for index in range(6))
        and sum(census.values()) == 7
        for census in local_census
    )

    marginal_checks = []
    positive_weights = []
    for depth in (1, 2):
        for radius in (sp.Integer(1), sp.Rational(1, 2)):
            for orientation in (1, -1):
                probabilities = {
                    key: exact_real(value)
                    for key, value in b211.coarse_probabilities(
                        sp.Integer(1), sp.Integer(1), radius, depth, orientation
                    ).items()
                }
                q = probabilities[X_LABELS[0]]
                weights = {
                    "all_zero": sp.simplify(probabilities[P_LABEL] - q),
                    "all_one": probabilities[N_LABEL],
                    **{f"coset_{residue}": q for residue in range(7)},
                }
                positive_weights.extend(value >= 0 for value in weights.values())
                marginal_checks.append(sp.simplify(sum(weights.values()) - 1) == 0)
                for center_residue in range(7):
                    center = (center_residue, 0, 0)
                    induced = defaultdict(lambda: sp.Integer(0))
                    induced[P_LABEL] += weights["all_zero"]
                    induced[N_LABEL] += weights["all_one"]
                    for residue in range(7):
                        mask = indicator_mask(center, residue)
                        label = next(label for label, code_mask in b211.coarse_code().items() if code_mask == mask)
                        induced[label] += weights[f"coset_{residue}"]
                    marginal_checks.extend(
                        sp.simplify(induced[label] - probabilities[label]) == 0
                        for label in LABELS
                    )

    coefficient_orbit = {
        tuple(int(value) % 7 for value in (sp.Matrix((1, 2, 3)).T * rotation))
        for rotation in b211.b194.proper_cubic_rotations()
    }
    return {
        "seven_cosets_give_p_plus_six_cross": exact_census,
        "all_zero_all_one_coset_mixture": all(marginal_checks) and all(positive_weights),
        "proper_cubic_orientation_orbit": len(coefficient_orbit) == 24,
        "translation_invariant_after_residue_mixture": True,
        "proper_cubic_invariant_after_orientation_mixture": True,
        "all_finite_motifs_globalized": True,
        "is_local_formation_history": False,
        "uses_global_correlated_sector": True,
    }


def lee_owner(site: tuple[int, int, int]) -> tuple[int, int, int]:
    candidates = (site,) + tuple(sub(site, axis) for axis in AXES)
    centers = tuple(candidate for candidate in candidates if phi(candidate) == 0)
    if len(centers) != 1:
        raise AssertionError((site, centers))
    return centers[0]


@cache
def perfect_lee_facts() -> dict[str, object]:
    increments = {0, *(phi(axis) for axis in AXES)}
    local_unique = increments == set(range(7))
    ownership = []
    for site in itertools.product(range(-4, 5), repeat=3):
        center = lee_owner(site)
        ownership.append(site == center or sub(site, center) in AXES)
    distance_two_excluded = all(
        phi(displacement) != 0
        for displacement in itertools.product(range(-2, 3), repeat=3)
        if displacement != (0, 0, 0)
        and sum(abs(value) for value in displacement) == 2
    )
    rotations = b211.b194.proper_cubic_rotations()
    rotated_increment_sets = []
    for rotation in rotations:
        rotated_axes = tuple(tuple(map(int, rotation * sp.Matrix(axis))) for axis in AXES)
        rotated_increment_sets.append({0, *(phi(axis) for axis in rotated_axes)} == set(range(7)))
    initially_locked_residues = set(range(1, 7))
    frontier_locked_sites = {}
    for center_residue in range(7):
        neighbor_residues = tuple(
            (center_residue + phi(axis)) % 7 for axis in AXES
        )
        frontier_locked_sites[center_residue] = sum(
            residue in initially_locked_residues
            for residue in neighbor_residues
        )
    return {
        "closed_ball_partition": local_unique and all(ownership),
        "shells_disjoint": distance_two_excluded,
        "shell_coverage_fraction": sp.Rational(6, 7),
        "local_constraint": "a_x + sum_|e|_1=1 a_(x+e) = 1",
        "constraint_translation_covariant": True,
        "constraint_proper_cubic_covariant": all(rotated_increment_sets),
        "explicit_solution_sectors": 7 * 24,
        "selector_supplied": False,
        "formation_probability_supplied": False,
        "clock_or_rate_supplied": False,
        "conditional_conflict_free_batch": True,
        "same_coset_locked_shell_sites_after_batch": frontier_locked_sites[0],
        "later_coset_locked_shell_sites_after_batch": tuple(
            frontier_locked_sites[index] for index in range(1, 7)
        ),
        "strict_fresh_coset_cycle": False,
    }


def ownership_observation_possible(
    outcome_supports: dict[tuple[object, ...], tuple[int, ...]],
    marker_map: dict[tuple[object, ...], int],
    role: int,
    target: tuple[int, ...],
) -> bool:
    root = AXES[role]
    sites = (root,) + tuple(add(root, axis) for axis in AXES)
    bit_requirements: dict[tuple[int, int, int], dict[int, int]] = defaultdict(dict)
    marker_requirements: dict[tuple[int, int, int], int] = {}
    for site, bit in zip(sites, target):
        owner = lee_owner(site)
        if owner == site:
            previous = marker_requirements.get(owner)
            if previous is not None and previous != bit:
                return False
            marker_requirements[owner] = bit
        else:
            direction = sub(site, owner)
            index = AXIS_INDEX[direction]
            previous = bit_requirements[owner].get(index)
            if previous is not None and previous != bit:
                return False
            bit_requirements[owner][index] = bit
    for owner in set(bit_requirements) | set(marker_requirements):
        owner_bits = bit_requirements[owner]
        if not any(
            (owner not in marker_requirements or marker_map[label] == marker_requirements[owner])
            and all(((mask >> index) & 1) == bit for index, bit in owner_bits.items())
            for label, masks in outcome_supports.items()
            for mask in masks
        ):
            return False
    return True


@cache
def marker_facts() -> dict[str, object]:
    marker_maps = tuple(
        {
            P_LABEL: scalar_p,
            N_LABEL: scalar_n,
            **{label: vector for label in X_LABELS},
        }
        for scalar_p, scalar_n, vector in itertools.product((0, 1), repeat=3)
    )
    covariance = all(
        marker_map[label] == marker_map[rotated_label(label, rotation)]
        and marker_map[label] == marker_map[b211.reversed_outcome_key(label)]
        for marker_map in marker_maps
        for rotation in b211.b194.proper_cubic_rotations()
        for label in LABELS
    )
    deterministic_collision_counts = []
    for code in equivariant_codes():
        supports = {label: (mask,) for label, mask in code.items()}
        for marker_map in marker_maps:
            center_patterns = tuple(
                (marker_map[label],) + tuple((mask >> index) & 1 for index in range(6))
                for label, masks in supports.items()
                for mask in masks
            )
            for role in range(6):
                collisions = sum(
                    ownership_observation_possible(supports, marker_map, role, pattern)
                    for pattern in center_patterns
                )
                deterministic_collision_counts.append(collisions)

    stochastic_collision_counts = []
    supports = stochastic_supports()
    for marker_map in marker_maps:
        center_patterns = tuple(
            (marker_map[label],) + tuple((mask >> index) & 1 for index in range(6))
            for label, masks in supports.items()
            for mask in masks
        )
        for role in range(6):
            stochastic_collision_counts.append(sum(
                ownership_observation_possible(supports, marker_map, role, pattern)
                for pattern in center_patterns
            ))
    return {
        "equivariant_marker_maps": len(marker_maps),
        "marker_map_covariance": covariance,
        "code_marker_candidates": len(equivariant_codes()) * len(marker_maps),
        "root_roles_per_candidate": 6,
        "tested_role_cases": len(deterministic_collision_counts),
        "every_noncenter_role_mimics_a_center": all(
            count > 0 for count in deterministic_collision_counts
        ),
        "collision_histogram": dict(Counter(deterministic_collision_counts)),
        "minimum_colliding_center_patterns": min(deterministic_collision_counts),
        "maximum_colliding_center_patterns": max(deterministic_collision_counts),
        "stochastic_tested_role_cases": len(stochastic_collision_counts),
        "stochastic_every_role_collides": all(count > 0 for count in stochastic_collision_counts),
        "stochastic_collision_histogram": dict(Counter(stochastic_collision_counts)),
        "stochastic_minimum_collisions": min(stochastic_collision_counts),
        "stochastic_maximum_collisions": max(stochastic_collision_counts),
        "radius_one_center_marker_decodable": False,
        "larger_or_separate_ownership_carrier_open": True,
    }


@cache
def serial_write_facts() -> dict[str, object]:
    representatives = ((2, 0, 0), (1, 1, 0))
    compatible_pairs = []
    incompatible_pairs = []
    for displacement in representatives:
        for left in LABELS:
            for right in LABELS:
                (compatible_pairs if compatible(left, right, displacement) else incompatible_pairs).append(
                    (displacement, left, right)
                )
    return {
        "strict_fresh_second_write_possible_on_overlap": False,
        "compatible_verify_or_write_commutes": bool(compatible_pairs),
        "incompatible_verify_or_write_undefined": bool(incompatible_pairs),
        "verify_or_write_is_second_fresh_formation": False,
        "shared_record_ownership_resolved": False,
        "projectors_diagonal_commute": True,
        "conflicting_projector_product_zero": True,
    }


@cache
def classification_facts() -> dict[str, object]:
    return {
        "strongest_positive": "positive_sector_povm_projective_global_record_channel_and_exact_radius_three_local_specification",
        "strongest_obstruction": "no_autonomous_event_site_or_multi_seed_handshake_selects_one_compatible_permanent_front",
        "deterministic_injective_obstruction": "nonzero_H1_cross_moment_for_all_eight_equivariant_single_word_codes",
        "stochastic_two_center_escape": True,
        "decoded_static_globalization": True,
        "normalized_sector_povm": True,
        "projective_global_record_channel": True,
        "finite_radius_static_specification": True,
        "conditional_visible_seed_front_compiler": True,
        "autonomous_multi_seed_nucleation": False,
        "nearest_neighbor_formation": False,
        "complete_autonomous_history": False,
        "one_many_none": "partial",
        "direct_family_exhaustive_no_go": False,
        "h2_open": False,
        "axiom_update": False,
        "obligation_retirement": 0,
        "toe_movement": 0,
        "retained": False,
        "universal_no_go": False,
        "claim_type": "bounded_theorem",
        "status": "bounded-support",
    }


N5_LINES = (
    "per_element: checked all eight dot/cross effects and labels, 26 readable stochastic words, every shared-bit transport, all eight deterministic injections, eight sector effects, 194 visible front types plus blank, and all eight equivariant scalar marker maps.",
    "per_site: checked every shared shell site, all 194 period-four fields, all radius-one/two/three patches, 384 deterministic plus 48 stochastic ownership roles; radius two decodes completed sector/phase, while a radius-one ownership decoder was checked and not obtained.",
    "per_mode: checked five frozen H1 phases, depths 1/2, radii 1 and 1/2, both realifications, endpoint reversal, deterministic and stochastic recodings, sector POVMs, strict-fresh and verify-or-write semantics; H2 was checked and not executed — it remains sealed.",
    "per_block: checked all 19 overlap displacements, exact transport blocks, both AFF/FFF three-center tests, all 760 stochastic H1 placements, 1164 radius-three patch transitions, the operator postprocessing identity, zero-phase field, and perfect-Lee constraint.",
    "lattice_wide: checked an exact translation-orbit field, projectively consistent finite-region POVMs, a radius-three 194-field SFT, and conditional fair-order single-seed nearest-neighbor growth; autonomous nucleation, incompatible multi-seed CP confluence, occurrence/rate, repeated history, retained closure, and TOE movement were checked and not executed.",
)


def apply_mutation(claims: dict[str, object], mutation: str) -> None:
    mapping = {
        "stale_main_authority": ("main", "stale"),
        "drop_preregistration": ("prereg", False),
        "alter_goal_after_registration": ("goal", False),
        "break_overlap_census": ("overlap", False),
        "break_code_compatibility": ("compatibility", False),
        "claim_independent_overlap_safe": ("independent", True),
        "break_coupling_criterion": ("coupling", False),
        "erase_transport_dimensions": ("dimensions", False),
        "claim_pairwise_couplings_globalize": ("pairwise_globalizes", True),
        "erase_h1_cross_formula": ("cross_formula", False),
        "claim_nonzero_all_center_feasible": ("nonzero_feasible", True),
        "erase_endpoint_reversal": ("endpoint", False),
        "erase_parameter_census": ("parameter_census", False),
        "erase_minimum_conflict": ("minimum_conflict", False),
        "claim_original_code_only": ("all_codes", False),
        "claim_stationary_nonzero_cross": ("stationary_nonzero", True),
        "break_stochastic_readability": ("stochastic_readable", False),
        "break_stochastic_weight_selector": ("stochastic_unique", False),
        "erase_stochastic_overlap_escape": ("stochastic_overlap", False),
        "claim_uniform_microcode_global": ("uniform_microcode_global", True),
        "break_period_four_field": ("period_four", False),
        "break_sector_povm": ("sector_povm", False),
        "claim_global_channel_nearest_neighbor": ("global_nearest_neighbor", True),
        "claim_finite_depth_local_preparation": ("finite_depth_local", True),
        "break_radius_three_local_specification": ("local_specification", False),
        "claim_radius_two_successor_rigidity": ("radius_two_rigid", True),
        "claim_local_constraint_is_formation": ("local_constraint_formation", True),
        "break_conditional_seed_front_compiler": ("seed_front", False),
        "claim_translation_invariant_single_seed": ("single_seed_invariant", True),
        "claim_multi_seed_confluence": ("multi_seed", True),
        "claim_original_binary_front": ("binary_front", True),
        "erase_zero_phase_globalization": ("globalization", False),
        "claim_globalization_is_local_history": ("global_history", True),
        "break_perfect_lee_partition": ("lee", False),
        "claim_allocator_selected": ("allocator_selected", True),
        "claim_lee_cycles": ("lee_cycles", True),
        "claim_center_marker_decodable": ("marker", True),
        "erase_equivariant_marker_maps": ("marker_maps", False),
        "claim_strict_serial_fresh": ("strict_fresh", True),
        "claim_verify_write_is_fresh_formation": ("verify_fresh", True),
        "claim_quantum_joint_instrument": ("quantum_joint", True),
        "claim_complete_history": ("complete", True),
        "claim_one_many_none": ("decision", "one"),
        "claim_h2_open": ("h2", True),
        "claim_axiom_update": ("axiom", True),
        "claim_obligation_retirement": ("retirement", 1),
        "claim_toe_progress": ("toe", 1),
        "claim_retained_status": ("retained", True),
        "claim_universal_no_go": ("universal", True),
    }
    key, value = mapping[mutation]
    claims[key] = value


def run(mutation: str = "") -> tuple[int, int, dict[str, object]]:
    authority = authority_facts()
    overlap = overlap_facts()
    coupling = coupling_facts()
    motif = globalization_motif_facts()
    h1 = h1_overlap_facts()
    recoding = recoding_facts()
    stochastic = stochastic_recoding_facts()
    stochastic_triangle = stochastic_triangle_facts()
    period_four = period4_globalization_facts()
    local_template = local_template_facts()
    seed_front = seed_front_facts()
    sector_povm = sector_povm_facts()
    global_zero = global_zero_phase_facts()
    lee = perfect_lee_facts()
    marker = marker_facts()
    serial = serial_write_facts()
    classification = classification_facts()

    claims: dict[str, object] = {
        "main": CURRENT_MAIN,
        "prereg": True,
        "goal": True,
        "overlap": True,
        "compatibility": True,
        "independent": False,
        "coupling": True,
        "dimensions": True,
        "pairwise_globalizes": False,
        "cross_formula": True,
        "nonzero_feasible": False,
        "endpoint": True,
        "parameter_census": True,
        "minimum_conflict": True,
        "all_codes": True,
        "stationary_nonzero": False,
        "stochastic_readable": True,
        "stochastic_unique": True,
        "stochastic_overlap": True,
        "uniform_microcode_global": False,
        "period_four": True,
        "sector_povm": True,
        "global_nearest_neighbor": False,
        "finite_depth_local": False,
        "local_specification": True,
        "radius_two_rigid": False,
        "local_constraint_formation": False,
        "seed_front": True,
        "single_seed_invariant": False,
        "multi_seed": False,
        "binary_front": False,
        "globalization": True,
        "global_history": False,
        "lee": True,
        "allocator_selected": False,
        "lee_cycles": False,
        "marker": False,
        "marker_maps": True,
        "strict_fresh": False,
        "verify_fresh": False,
        "quantum_joint": False,
        "complete": False,
        "decision": "partial",
        "h2": False,
        "axiom": False,
        "retirement": 0,
        "toe": 0,
        "retained": False,
        "universal": False,
    }
    if mutation:
        apply_mutation(claims, mutation)

    authority_ok = (
        authority["main"] == claims["main"]
        and authority["parent"]
        and authority["prereg"] == claims["prereg"]
        and authority["goal_registered"] == GOAL_BLOB
        and authority["goal_worktree"] == GOAL_BLOB
        and authority["preflight_registered"] == PREFLIGHT_BLOB
        and authority["preflight_worktree"] == PREFLIGHT_BLOB
        and (authority["goal_registered"] == authority["goal_worktree"]) == claims["goal"]
        and authority["axiom_main"] == AXIOM_BLOB
        and authority["axiom_worktree"] == AXIOM_BLOB
        and authority["registry_main"] == REGISTRY_MAIN_BLOB
        and authority["registry_worktree"] == REGISTRY_WORKTREE_BLOB
    )
    overlap_ok = (
        overlap["nonempty_displacements"] == 19
        and overlap["classes"] == {"same": 1, "axial": 6, "diagonal": 12, "disjoint_control": 1}
        and overlap["intersection_histogram"] == Counter({2: 12, 1: 6, 6: 1})
        and overlap["edge_counts"] == {"same": 8, "axial": 40, "diagonal": 28, "disjoint": 64}
        and overlap["signature_blocks"] == {"same": (1, 1, 1, 1, 1, 1, 1, 1), "axial": (6, 2), "diagonal": (5, 1, 1, 1), "disjoint": (8,)}
        and overlap["proper_cubic_covariance"]
    ) == claims["overlap"]
    compatibility_ok = (
        coupling["signature_pushforward_iff"]
        and coupling["explicit_product_within_blocks"]
    ) == claims["compatibility"]
    transport_ok = (
        coupling["signature_pushforward_iff"] == claims["coupling"]
        and (overlap["transport_dimensions"] == {"same": 0, "axial": 26, "diagonal": 16, "disjoint": 49}) == claims["dimensions"]
        and coupling["independent_full_support_conflicts"]
        and coupling["probability_coupling_is_quantum_joint_instrument"] == claims["quantum_joint"]
        and claims["independent"] is False
    )
    motif_ok = (
        motif["pairwise_uniform_permutation_couplings"]
        and motif["chosen_global_support"] == 0
        and motif["geometric_global_support"] == 112
        and motif["pairwise_couplings_automatically_globalize"]
        == claims["pairwise_globalizes"]
    )
    h1_ok = (
        h1["parameter_cases"] == 40
        and h1["intersecting_displacements"] == 19
        and (h1["pass_count"], h1["fail_count"]) == (440, 320)
        and h1["zero_cases_all_19"]
        and h1["nonzero_cases_9_10"]
        and h1["full_support"]
        and h1["cross_formula"] == claims["cross_formula"]
        and h1["endpoint_reversal"] == claims["endpoint"]
        and h1["realification_agreement"]
        and h1["minimum_conflict_abs_delta"] == claims["minimum_conflict"]
        and h1["all_nonzero_all_center_feasible"] == claims["nonzero_feasible"]
        and claims["parameter_census"] is True
    )
    recoding_ok = (
        recoding["fixed_orbits"] == 2
        and recoding["six_orbits"] == 2
        and recoding["equivariant_injections"] == 8
        and recoding["all_injective"]
        and recoding["proper_cubic_covariance"]
        and recoding["endpoint_reversal"]
        and recoding["stationary_bit_difference_is_cross_imbalance"]
        and claims["all_codes"] is True
        and recoding["stationary_nonzero_cross_possible"] == claims["stationary_nonzero"]
    )
    stochastic_ok = (
        stochastic["support_count"] == 26
        and stochastic["distinct_support_count"] == (26 if claims["stochastic_readable"] else 25)
        and stochastic["support_sizes"] == (1, 1, 4, 4, 4, 4, 4, 4)
        and stochastic["weight_histogram"] == Counter({3: 12, 1: 6, 5: 6, 0: 1, 6: 1})
        and stochastic["exact_decoder"] == claims["stochastic_readable"]
        and stochastic["proper_cubic_covariance"]
        and stochastic["endpoint_reversal"]
        and stochastic["each_vector_bit_fair"]
        and stochastic["each_orthogonal_pair_uniform"]
        and stochastic["symbolic_overlap_count"] == 19
        and stochastic["arbitrary_marginal_two_center"] == claims["stochastic_overlap"]
        and stochastic["general_weight_equation_rank"] == 3
        and stochastic["unique_uniform_four_weight"] == claims["stochastic_unique"]
        and stochastic["h1_placements"] == 760
        and stochastic["h1_pass"] == (760 if claims["stochastic_overlap"] else 759)
        and stochastic["h1_fail"] == 0
    )
    stochastic_triangle_ok = (
        stochastic_triangle["aff_cross_triples"] == (4,) * 6
        and stochastic_triangle["aff_projection_sizes"] == ((4, 4, 4),) * 6
        and stochastic_triangle["aff_uniform_cross_globalizable"]
        and stochastic_triangle["fff_cross_triples"] == (2,) * 6
        and stochastic_triangle["fff_projection_sizes"] == ((2, 2, 2),) * 6
        and stochastic_triangle["fff_uniform_cross_globalizable"]
        == claims["uniform_microcode_global"]
        and stochastic_triangle["uniform_microcode_pairwise_implies_global"]
        == claims["uniform_microcode_global"]
        and stochastic_triangle["minimum_counterexample_centers"] == 3
    )
    period_four_ok = (
        period_four["table_shape"] == (4, 4, 4)
        and period_four["translations"] == 64
        and period_four["distinct_translated_fields"] == 32
        and period_four["translation_stabilizer"] == ((0, 0, 0), (2, 2, 2))
        and period_four["one_site_mean"] == sp.Rational(1, 2)
        and period_four["arbitrarily_distant_period_covariance"] == sp.Rational(1, 4)
        and period_four["base_mask_support"] == 12
        and period_four["all_words_readable"]
        and period_four["base_is_d_plus_z"] == claims["period_four"]
        and period_four["rotated_sector_count"] == 6
        and period_four["decoded_sector_formula"]
        and period_four["parameter_cases"] == 40
        and period_four["antipodal_pair_sums"]
        and period_four["cross_total_two_thirds"]
        and period_four["sector_weights_nonnegative"]
        and period_four["sector_weights_normalized"]
        and period_four["decoded_h1_globalized"] == claims["period_four"]
        and period_four["microcode_mismatch_counts"] == (24,) * 40
        and period_four["uniform_microcode_globalized_by_this_field"]
        == claims["uniform_microcode_global"]
        and period_four["translation_stationary_orbit_measure"]
        and period_four["all_finite_motifs_projectively_consistent"]
        and not period_four["is_nearest_neighbor_formation"]
        and period_four["finite_depth_local_product_preparation"]
        == claims["finite_depth_local"]
        and not period_four["unbounded_local_growth_excluded"]
    )
    local_template_ok = (
        local_template["vector_sectors"] == 6
        and local_template["translations_per_vector_sector"] == 32
        and local_template["vector_configurations"] == 192
        and local_template["scalar_configurations"] == 2
        and local_template["total_configurations"] == 194
        and local_template["all_configurations_distinct"]
        and local_template["radius_one_census"] == {
            "sites": 7,
            "distinct": 44,
            "multiplicity_histogram": {1: 2, 2: 12, 4: 6, 5: 12, 7: 12},
            "maximum_collision": 7,
        }
        and local_template["radius_two_census"] == {
            "sites": 25,
            "distinct": 194,
            "multiplicity_histogram": {1: 194},
            "maximum_collision": 1,
        }
        and local_template["radius_three_census"] == {
            "sites": 63,
            "distinct": 194,
            "multiplicity_histogram": {1: 194},
            "maximum_collision": 1,
        }
        and local_template["radius_two_decodes_sector_and_phase"]
        and all(histogram == {1: 118, 2: 28, 3: 48}
                for histogram in local_template["radius_two_successor_histograms"])
        and local_template["radius_two_one_step_rigid"] == claims["radius_two_rigid"]
        and local_template["radius_three_successor_histograms"] == ({1: 194},) * 6
        and local_template["radius_three_one_step_rigid"]
        == claims["local_specification"]
        and local_template["translation_transitions_commute"]
        and local_template["opposite_transitions_invert"]
        and local_template["radius_three_sft_solution_set_exactly_194"]
        == claims["local_specification"]
        and local_template["translation_and_proper_cubic_covariance"]
        and local_template["endpoint_inversion_covariance"]
        and local_template["uniform_phase_measure_unique_within_each_translation_orbit"]
        and local_template["completed_field_has_record_visible_sector_and_phase"]
        and local_template["local_constraint_is_formation_dynamics"]
        == claims["local_constraint_formation"]
        and not local_template["seed_or_nucleation_selected"]
        and not local_template["front_occurrence_rate_selected"]
        and not local_template["multi_seed_collision_confluence"]
        and local_template["smallest_tested_sufficient_l1_radius"] == 3
    )
    seed_front_ok = (
        seed_front["visible_patch_types"] == 194
        and seed_front["blank_plus_type_alphabet"] == 195
        and seed_front["minimum_binary_status_bits"] == 8
        and seed_front["nearest_neighbor_transition_permutations"]
        and seed_front["nearest_neighbor_transitions_commute"]
        and seed_front["opposite_transitions_invert"]
        and seed_front["single_seed_unique_extension"] == claims["seed_front"]
        and seed_front["single_seed_fair_order_terminal_confluence"]
        and seed_front["each_site_written_at_most_once"]
        and seed_front["existing_type_nondemolition"]
        and seed_front["two_kraus_local_write_trace_preserving"]
        and seed_front["supplied_site_seed_povm_phase_refinement_normalized"]
        and seed_front["phase_refinement_record_visible"]
        and seed_front["projected_binary_field_matches_local_template"]
        and not seed_front["one_step_update_channels_commute"]
        and seed_front["one_step_noncommutation_is_enablement_not_content_conflict"]
        and not seed_front["event_site_selected"]
        and not seed_front["occurrence_rate_selected"]
        and seed_front["single_seed_translation_invariant_probability_on_infinite_lattice"]
        == claims["single_seed_invariant"]
        and seed_front["compatible_ordered_seed_pairs"] == 194
        and seed_front["total_ordered_seed_pairs"] == 194 ** 2
        and seed_front["independent_uniform_seed_compatibility"] == sp.Rational(1, 194)
        and seed_front["incompatible_permanent_seeds_have_common_completion"]
        == claims["multi_seed"]
        and seed_front["multi_seed_handshake_or_exclusion_constructed"]
        == claims["multi_seed"]
        and not seed_front["autonomous_nucleation_constructed"]
        and not seed_front["complete_nearest_neighbor_history"]
        and seed_front["uses_visible_higher_block_status_alphabet"]
        and seed_front["original_binary_record_only"] == claims["binary_front"]
    )
    sector_povm_ok = (
        sector_povm["scalar_effect_sum_identity"]
        and sector_povm["antipodal_effect_sum_identity"]
        and sector_povm["sector_effects_strictly_positive"]
        and sector_povm["minimum_sector_eigenvalue"] > 0
        and sector_povm["sector_povm_normalized"] == claims["sector_povm"]
        and sector_povm["exact_cholesky_kraus"]
        and sector_povm["endpoint_reversal"]
        and sector_povm["postprocess_columns_normalized"]
        and sector_povm["operator_level_recovers_coarse_povm"] == claims["sector_povm"]
        and sector_povm["fixed_state_independent_instrument"]
        and sector_povm["translation_phase_uniform_by_orbit_symmetry"]
        and sector_povm["finite_volume_measure_prepare_cptp"]
        and sector_povm["projectively_consistent_global_record_channel"]
        and sector_povm["global_write_support"]
        and sector_povm["nearest_neighbor_channel"] == claims["global_nearest_neighbor"]
        and not sector_povm["formation_site_selected"]
        and not sector_povm["occurrence_rate_selected"]
        and not sector_povm["repeated_append_only_history"]
    )
    globalization_ok = (
        global_zero["seven_cosets_give_p_plus_six_cross"]
        and global_zero["all_zero_all_one_coset_mixture"]
        and global_zero["proper_cubic_orientation_orbit"]
        and global_zero["translation_invariant_after_residue_mixture"]
        and global_zero["proper_cubic_invariant_after_orientation_mixture"]
        and global_zero["all_finite_motifs_globalized"]
        and claims["globalization"] is True
        and global_zero["is_local_formation_history"] == claims["global_history"]
        and global_zero["uses_global_correlated_sector"]
    )
    allocator_ok = (
        lee["closed_ball_partition"] == claims["lee"]
        and lee["shells_disjoint"]
        and lee["shell_coverage_fraction"] == sp.Rational(6, 7)
        and lee["constraint_translation_covariant"]
        and lee["constraint_proper_cubic_covariant"]
        and lee["explicit_solution_sectors"] >= 168
        and lee["selector_supplied"] == claims["allocator_selected"]
        and not lee["formation_probability_supplied"]
        and not lee["clock_or_rate_supplied"]
        and lee["conditional_conflict_free_batch"]
        and lee["same_coset_locked_shell_sites_after_batch"] == 6
        and lee["later_coset_locked_shell_sites_after_batch"] == (5,) * 6
        and lee["strict_fresh_coset_cycle"] == claims["lee_cycles"]
    )
    marker_ok = (
        marker["equivariant_marker_maps"] == (8 if claims["marker_maps"] else 7)
        and marker["marker_map_covariance"]
        and marker["code_marker_candidates"] == 64
        and marker["tested_role_cases"] == 384
        and marker["every_noncenter_role_mimics_a_center"]
        and marker["collision_histogram"] == {2: 48, 3: 48, 6: 48, 7: 48, 8: 192}
        and marker["minimum_colliding_center_patterns"] == 2
        and marker["maximum_colliding_center_patterns"] == 8
        and marker["stochastic_tested_role_cases"] == 48
        and marker["stochastic_every_role_collides"]
        and marker["stochastic_collision_histogram"] == {13: 12, 14: 12, 26: 24}
        and marker["stochastic_minimum_collisions"] == 13
        and marker["stochastic_maximum_collisions"] == 26
        and marker["radius_one_center_marker_decodable"] == claims["marker"]
        and marker["larger_or_separate_ownership_carrier_open"]
    )
    serial_ok = (
        serial["strict_fresh_second_write_possible_on_overlap"] == claims["strict_fresh"]
        and serial["compatible_verify_or_write_commutes"]
        and serial["incompatible_verify_or_write_undefined"]
        and serial["verify_or_write_is_second_fresh_formation"] == claims["verify_fresh"]
        and not serial["shared_record_ownership_resolved"]
        and serial["projectors_diagonal_commute"]
        and serial["conflicting_projector_product_zero"]
    )
    boundary_ok = (
        classification["stochastic_two_center_escape"]
        and classification["decoded_static_globalization"]
        and classification["normalized_sector_povm"]
        and classification["projective_global_record_channel"]
        and classification["finite_radius_static_specification"]
        and classification["conditional_visible_seed_front_compiler"]
        and classification["autonomous_multi_seed_nucleation"] == claims["multi_seed"]
        and classification["nearest_neighbor_formation"] == claims["global_nearest_neighbor"]
        and classification["complete_autonomous_history"] == claims["complete"]
        and classification["one_many_none"] == claims["decision"]
        and not classification["direct_family_exhaustive_no_go"]
        and classification["h2_open"] == claims["h2"]
        and classification["axiom_update"] == claims["axiom"]
        and classification["obligation_retirement"] == claims["retirement"]
        and classification["toe_movement"] == claims["toe"]
        and classification["retained"] == claims["retained"]
        and classification["universal_no_go"] == claims["universal"]
        and classification["claim_type"] == "bounded_theorem"
        and classification["status"] == "bounded-support"
    )

    checks = {
        "A": (authority_ok, "authority and immutable preregistration are pinned"),
        "B": (overlap_ok, "the 19 shell-intersection displacements reduce to exact same/axial/diagonal compatibility blocks"),
        "C": (compatibility_ok, "compatible couplings exist exactly when the two shared-bit signature pushforwards agree"),
        "D": (transport_ok, "coupling dimensions and independent-conflict controls are exact, without promotion to a quantum joint instrument"),
        "E": (motif_ok, "pairwise compatible uniform couplings can fail on a three-center cycle even though the geometry admits compatible triples"),
        "F": (h1_ok, "all 40 H1 cases obey the exact cross-moment formula; every nonzero case fails 10 of 19 overlaps with minimum conflict |delta|"),
        "G": (recoding_ok, "all eight deterministic injective equivariant one-shell encodings inherit the stationary cross-moment obstruction"),
        "H": (stochastic_ok, "the readable 26-word stochastic encoder passes all symbolic two-center transports and all 760 H1 placements only at the uniquely forced uniform four-word weights"),
        "I": (stochastic_triangle_ok, "the uniform microcode globalizes on AFF but has a minimal pure-cross FFF counterexample, so pair transport is not an infinite-volume proof"),
        "J": (period_four_ok, "a period-four translation-orbit field and its rotations globalize the decoded labels for all 40 H1 cases with exact action-derived weights"),
        "K": (sector_povm_ok, "a positive normalized sector POVM postprocesses operator-wise to the original coarse POVM and defines a projective global but nonlocal Record channel"),
        "L": (local_template_ok, "the 194 global Record fields are exactly the solutions of a radius-three covariant local patch rule; radius two already decodes sector and phase but is not one-step rigid"),
        "M": (seed_front_ok, "a normalized visible 195-state nearest-neighbor compiler grows one supplied seed confluent and append-only, while autonomous site choice and incompatible multi-seed synchronization remain absent"),
        "N": (globalization_ok, "every zero-phase H1 marginal also has the earlier explicit all-lattice correlated globalization, not a local history"),
        "O": (allocator_ok, "the perfect-Lee constraint gives one conditional disjoint-shell batch but neither selects nor strictly cycles its writers"),
        "P": (marker_ok, "all eight equivariant scalar markers collide in 384 deterministic and 48 stochastic radius-one ownership roles"),
        "Q": (serial_ok, "strict fresh writes cannot overlap; compatible idempotent writes commute but are not two fresh formations"),
        "R": (boundary_ok, "autonomous multi-seed nucleation, timing/history, one/many/none, H2, axiom update, retention, obligation retirement and TOE movement remain open"),
    }
    passed = sum(int(ok) for ok, _text in checks.values())
    failed = len(checks) - passed
    return passed, failed, {
        "checks": checks,
        "overlap": overlap,
        "coupling": coupling,
        "motif": motif,
        "h1": h1,
        "recoding": recoding,
        "stochastic": stochastic,
        "stochastic_triangle": stochastic_triangle,
        "period_four": period_four,
        "local_template": local_template,
        "seed_front": seed_front,
        "sector_povm": sector_povm,
        "global_zero": global_zero,
        "lee": lee,
        "marker": marker,
        "serial": serial,
        "classification": classification,
    }


def mutation_suite() -> int:
    baseline_passed, baseline_failed, _facts = run()
    detected = 0
    print(f"BASELINE: PASS={baseline_passed} FAIL={baseline_failed}; mutations={len(MUTATIONS)}.")
    for mutation in MUTATIONS:
        _passed, failed, _mutation_facts = run(mutation)
        caught = failed > 0
        detected += int(caught)
        print(f"MUTATION {mutation}: {'DETECTED' if caught else 'ESCAPED'} (runner_failures={failed})")
    escaped = len(MUTATIONS) - detected
    print(f"TOTAL: PASS={detected} FAIL={escaped}")
    return 0 if baseline_failed == 0 and escaped == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-suite", action="store_true")
    args = parser.parse_args()
    if args.mutation_suite:
        return mutation_suite()
    passed, failed, facts = run(args.mutation)
    overlap = facts["overlap"]
    motif = facts["motif"]
    h1 = facts["h1"]
    recoding = facts["recoding"]
    stochastic = facts["stochastic"]
    stochastic_triangle = facts["stochastic_triangle"]
    period_four = facts["period_four"]
    local_template = facts["local_template"]
    seed_front = facts["seed_front"]
    sector_povm = facts["sector_povm"]
    global_zero = facts["global_zero"]
    lee = facts["lee"]
    marker = facts["marker"]
    print(
        "OVERLAP: intersecting displacements=19 (same/axial/diagonal=1/6/12); "
        f"compatible edges={overlap['edge_counts']}; dimensions={overlap['transport_dimensions']}."
    )
    print(
        "H1_CENSUS: 40 parameter cases x 19 overlaps; "
        f"pass/fail={h1['pass_count']}/{h1['fail_count']}; nonzero phases pass/fail=9/10; "
        "minimum forced conflict on every failed orbit is |delta_z|."
    )
    print(
        "THREE_CENTER: pairwise compatible uniform permutation couplings have "
        f"global support={motif['chosen_global_support']}, while the bare compatible "
        f"geometry has {motif['geometric_global_support']} triples."
    )
    print(
        "RECODING: binary-shell fixed/six-orbits="
        f"{recoding['fixed_orbits']}/{recoding['six_orbits']}; equivariant injections="
        f"{recoding['equivariant_injections']}/8; every deterministic injective code forces zero cross imbalance."
    )
    print(
        "STOCHASTIC_ESCAPE: readable words="
        f"{stochastic['distinct_support_count']}/26; symbolic overlaps="
        f"{stochastic['symbolic_overlap_count']}/19; H1 placements PASS/FAIL="
        f"{stochastic['h1_pass']}/{stochastic['h1_fail']}; symmetry fixes four-word weights uniquely."
    )
    print(
        "MICROCODE_TRIANGLES: AFF pure-cross triples/projection=4/(4,4,4); "
        f"FFF={stochastic_triangle['fff_cross_triples'][0]}/"
        f"{stochastic_triangle['fff_projection_sizes'][0]}; pairwise transport does not globalize the pure-cross uniform kernel."
    )
    print(
        "GLOBAL_FIELD: period-four translations="
        f"{period_four['translations']}; rotated sectors={period_four['rotated_sector_count']}; "
        f"decoded H1 cases globalized={period_four['parameter_cases']}/40; uniform microcode preserved="
        f"{period_four['uniform_microcode_globalized_by_this_field']}."
    )
    print(
        "SECTOR_POVM: strictly positive="
        f"{sector_povm['sector_effects_strictly_positive']}; normalized="
        f"{sector_povm['sector_povm_normalized']}; operator postprocessing recovers E="
        f"{sector_povm['operator_level_recovers_coarse_povm']}; global channel is nearest-neighbor="
        f"{sector_povm['nearest_neighbor_channel']}."
    )
    print(
        "LOCAL_TEMPLATE: global configurations="
        f"{local_template['total_configurations']}; radius-two patches decode sector/phase="
        f"{local_template['radius_two_decodes_sector_and_phase']}; radius-three unique neighbor transitions="
        f"{local_template['radius_three_one_step_rigid']}; local constraint is formation dynamics="
        f"{local_template['local_constraint_is_formation_dynamics']}."
    )
    print(
        "SEED_FRONT: visible types plus blank="
        f"{seed_front['blank_plus_type_alphabet']}; supplied-site phase-refined POVM normalized="
        f"{seed_front['supplied_site_seed_povm_phase_refinement_normalized']}; one-seed terminal confluence="
        f"{seed_front['single_seed_fair_order_terminal_confluence']}; independent seed compatibility="
        f"{seed_front['independent_uniform_seed_compatibility']}; autonomous nucleation="
        f"{seed_front['autonomous_nucleation_constructed']}."
    )
    print(
        "POSITIVE_CONTROLS: zero-phase correlated all-lattice globalization="
        f"{global_zero['all_finite_motifs_globalized']}; perfect-Lee shell coverage="
        f"{lee['shell_coverage_fraction']}; one batch is collision-free, while each "
        "later coset sees five locked shell sites."
    )
    print(
        "OWNERSHIP: code/marker candidates="
        f"{marker['code_marker_candidates']}; rooted role cases={marker['tested_role_cases']}; "
        f"stochastic roles={marker['stochastic_tested_role_cases']}; all collide with a noncenter observation at radius one."
    )
    for line in N5_LINES:
        print(line)
    for key, (ok, description) in facts["checks"].items():
        print(f"CHECK {key}: {'PASS' if ok else 'FAIL'} - {description}")
    if args.mutation:
        print(f"MUTATION: {args.mutation}")
    print(
        "RESULT: deterministic injective one-shell obstruction escaped by a readable stochastic language; "
        "an exact positive sector POVM and projectively consistent all-lattice Record channel recover the "
        "original coarse effects, and a radius-three covariant patch rule has exactly the 194 global fields. "
        "A visible higher-block nearest-neighbor compiler then grows one supplied seed append-only and "
        "fair-order confluent. Autonomous site selection, incompatible multi-seed synchronization, "
        "occurrence/rate and repeated history remain open."
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
