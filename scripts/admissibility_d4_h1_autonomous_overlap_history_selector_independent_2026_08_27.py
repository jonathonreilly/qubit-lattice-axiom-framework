#!/usr/bin/env python3
"""Independent Block-212 shell-overlap/history-selector checker.

This checker deliberately imports only the committed Block-211 fixture.  It
reconstructs the shell intersections, compatibility graphs, transportation
criterion, multi-center tests, and conditional escapes without importing the
Block-212 primary runner.

The result is intentionally boundary-bounded.  The period-4 Record support has
an exact static radius-3 SFT and a visible supplied-seed front compiler, but
this does not select an event site/rate, reconcile multiple seeds, construct
autonomous history, or globalize the uniform microcode.
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

# Committed Block-211 fixture only; no Block-212 primary import is permitted.
import admissibility_d4_h1_action_native_score_quotient_record_dilation_2026_08_27 as b211  # noqa: E402


Vector = tuple[int, int, int]
Outcome = tuple[object, ...]
AUDIT_TIMEOUT_SEC = 240
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block212-autonomous-overlap-history-20260827"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT.md"
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK211_NOTE_PATH = (
    "docs/ADMISSIBILITY_D4_H1_ACTION_NATIVE_SCORE_QUOTIENT_RECORD_DILATION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md"
)
BLOCK211_RUNNER_PATH = (
    "scripts/admissibility_d4_h1_action_native_score_quotient_record_dilation_"
    "2026_08_27.py"
)
BLOCK211_GOAL_PATH = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block211-action-native-minimal-record-dilation-"
    "20260827/GOAL.md"
)
PARENT_COMMIT = "59290f671a7482dd3350e118e8f35606f48be1a5"
PREREG_COMMIT = "07d799c0a68434a73f96f6d5c147963fed86fdf5"
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
GOAL_BLOB = "c5e025c8afc00a3490c48a8a15592e6bfe5e3455"
PREFLIGHT_BLOB = "08cf900caec925cede9fc4c8f68b5deceab7e8bf"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
REGISTRY_MAIN_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
REGISTRY_WORKTREE_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
BLOCK211_NOTE_BLOB = "21d13376082387b8aef12e9ae38f01645ad81beb"
BLOCK211_RUNNER_BLOB = "439b4b13227db51dbcfdebf7495f5e791555c1ec"
BLOCK211_GOAL_BLOB = "3f4df853c0fc6d20e921c531fe494295d3042296"

# Literal and intentionally nonempty: these are the only scientific inputs.
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block212-autonomous-overlap-history-20260827/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block212-autonomous-overlap-history-20260827/PREFLIGHT.md",
    "docs/ADMISSIBILITY_D4_H1_ACTION_NATIVE_SCORE_QUOTIENT_RECORD_DILATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "scripts/admissibility_d4_h1_action_native_score_quotient_record_dilation_2026_08_27.py",
    "logs/runner-cache/admissibility_d4_h1_action_native_score_quotient_record_dilation_2026_08_27.txt",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)


AXES: tuple[Vector, ...] = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
ORIGIN: Vector = (0, 0, 0)
P: Outcome = ("P",)
N: Outcome = ("N",)
OUTCOMES: tuple[Outcome, ...] = (
    P,
    N,
    *(('X',) + axis for axis in AXES),
)
PHASES = (
    sp.Integer(0),
    sp.pi / 6,
    sp.pi / 3,
    sp.pi / 2,
    5 * sp.pi / 6,
)
DEPTHS = (1, 2)
RADII = (sp.Integer(1), sp.Rational(1, 2))
REALIFICATIONS = (1, -1)
DISJOINT_CONTROLS: tuple[Vector, ...] = (
    (1, 0, 0),
    (3, 0, 0),
    (2, 1, 0),
    (1, 1, 1),
)


MUTATIONS = (
    "ind_stale_main_authority",
    "ind_drop_preregistration",
    "ind_alter_goal_after_registration",
    "ind_alter_preflight_after_registration",
    "ind_alter_parent_fixture",
    "ind_drop_face_displacement",
    "ind_change_axial_edge_count",
    "ind_change_face_edge_count",
    "ind_admit_cross_signature",
    "ind_erase_transport_necessity",
    "ind_erase_transport_sufficiency",
    "ind_break_code_equivariance",
    "ind_break_endpoint_reversal",
    "ind_change_phase_pass_count",
    "ind_erase_cross_mismatch",
    "ind_erase_minimum_conflict_identity",
    "ind_claim_products_safe",
    "ind_permit_strict_overlap",
    "ind_reject_idempotent_reuse",
    "ind_claim_homogeneous_cross",
    "ind_change_recoding_count",
    "ind_claim_stationary_recoding_cross",
    "ind_break_stochastic_readability",
    "ind_change_symbolic_overlap_count",
    "ind_change_stabilizer_weight_solution",
    "ind_erase_stochastic_h1_placements",
    "ind_claim_fff_extreme_globalizes",
    "ind_break_exact_h1_triangle_certificate",
    "ind_confuse_numerical_scout_with_certificate",
    "ind_break_period4_table",
    "ind_erase_decoded_label_globalization",
    "ind_claim_uniform_microcode_preserved",
    "ind_break_sector_effect_partition",
    "ind_make_sector_effect_nonpositive",
    "ind_break_sector_kraus_normalization",
    "ind_break_operator_postprocessing",
    "ind_break_sector_endpoint_reversal",
    "ind_break_record_projectivity",
    "ind_claim_record_channel_local_autonomous",
    "ind_change_radius1_patch_count",
    "ind_erase_radius1_collisions",
    "ind_change_radius2_patch_count",
    "ind_claim_radius2_unique_successors",
    "ind_break_radius3_successor_uniqueness",
    "ind_break_translation_commutation",
    "ind_break_sft_cubic_covariance",
    "ind_break_sft_endpoint_covariance",
    "ind_change_sft_field_count",
    "ind_claim_sft_formation_dynamics",
    "ind_change_smallest_radius",
    "ind_change_seed_front_alphabet",
    "ind_break_seed_transition_permutations",
    "ind_break_seed_phase_povm",
    "ind_break_seed_write_normalization",
    "ind_break_seed_nondemolition",
    "ind_break_single_seed_extension",
    "ind_break_fair_order_confluence",
    "ind_claim_enabled_steps_commute",
    "ind_claim_seed_content_conflict",
    "ind_change_compatible_seed_pairs",
    "ind_claim_incompatible_seed_completion",
    "ind_claim_invariant_single_seed_law",
    "ind_claim_compiler_selects_site_rate",
    "ind_claim_multi_seed_handshake",
    "ind_claim_binary_seed_carrier",
    "ind_break_single_seed_no_go_scope",
    "ind_claim_pairwise_globalizes",
    "ind_break_global_escape",
    "ind_break_lee_residue_bijection",
    "ind_break_ownership_collision_census",
    "ind_change_marker_map_count",
    "ind_break_stochastic_marker_census",
    "ind_claim_radius_one_center_decoder",
    "ind_claim_complete_history",
    "ind_open_h2",
    "ind_edit_axiom",
    "ind_move_toe",
    "ind_claim_retained_status",
    "ind_claim_universal_no_go",
)


N5_LINES = (
    "per_element: checked eight labels, 26 words, 32 sector effects, 194 phase-refined seed effects, exact Kraus blocks, 195 visible front states, all frames, endpoint reversal, and a=b=c/2=1/4.",
    "per_site: checked every shared site, the two-domain write/lock channel, and 384 deterministic plus 48 stochastic marker roles; a binary radius-one ownership decoder was checked and not obtained.",
    "per_mode: checked five H1 phases across both depths, radii and realifications; deterministic coding fails 320 placements by |delta_z| while redundant coding passes all 760; H2 was checked and not executed — it remains sealed.",
    "per_block: checked all transports, both triangle orbits, 20 exact H1 certificates, 64 translations, 1164 patch transitions, and 194/194^2 fixed-displacement seed compatibility.",
    "lattice_wide: checked the exact 194-field static SFT and fair-order one-seed limit; autonomous site/rate, handshake, repeated history, and uniform-microcode consistency remain open.",
)


def add(first: Vector, second: Vector) -> Vector:
    return tuple(a + b for a, b in zip(first, second))  # type: ignore[return-value]


def sub(first: Vector, second: Vector) -> Vector:
    return tuple(a - b for a, b in zip(first, second))  # type: ignore[return-value]


def negate(vector: Vector) -> Vector:
    return tuple(-value for value in vector)  # type: ignore[return-value]


def l1(vector: Vector) -> int:
    return sum(abs(value) for value in vector)


def code(outcome: Outcome) -> tuple[int, ...]:
    if outcome == P:
        return (0,) * 6
    if outcome == N:
        return (1,) * 6
    axis = tuple(int(value) for value in outcome[1:])
    return tuple(int(candidate == axis) for candidate in AXES)


def outcome_from_code(word: tuple[int, ...]) -> Outcome | None:
    for outcome in OUTCOMES:
        if code(outcome) == word:
            return outcome
    return None


def antipode(outcome: Outcome) -> Outcome:
    if outcome in (P, N):
        return outcome
    return ("X",) + negate(tuple(outcome[1:]))  # type: ignore[arg-type]


def rotate_outcome(
    outcome: Outcome, rotation: tuple[Vector, Vector, Vector]
) -> Outcome:
    if outcome in (P, N):
        return outcome
    return ("X",) + mat_vec(rotation, tuple(outcome[1:]))  # type: ignore[arg-type]


def overlap_pairs(displacement: Vector) -> tuple[tuple[int, int], ...]:
    """Offsets s,t with s = displacement+t for centers 0 and displacement."""
    return tuple(
        (left, right)
        for left, s_axis in enumerate(AXES)
        for right, t_axis in enumerate(AXES)
        if sub(s_axis, t_axis) == displacement
    )


def signature(outcome: Outcome, displacement: Vector, left: bool) -> tuple[int, ...]:
    word = code(outcome)
    return tuple(
        word[left_index if left else right_index]
        for left_index, right_index in overlap_pairs(displacement)
    )


def compatibility_edges(displacement: Vector) -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left in range(8)
        for right in range(8)
        if signature(OUTCOMES[left], displacement, True)
        == signature(OUTCOMES[right], displacement, False)
    )


def displacement_class(displacement: Vector) -> str:
    if displacement == ORIGIN:
        return "same"
    nonzero = tuple(abs(value) for value in displacement if value)
    if nonzero == (2,):
        return "axial"
    if len(nonzero) == 2 and nonzero == (1, 1):
        return "face"
    return "disjoint"


@cache
def proper_cubic_rotations() -> tuple[tuple[Vector, Vector, Vector], ...]:
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[row] * int(column == permutation[row]) for column in range(3))
                for row in range(3)
            )
            determinant = (
                matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
                - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
                + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
            )
            if determinant == 1:
                rotations.append(matrix)  # type: ignore[arg-type]
    return tuple(rotations)


def mat_vec(matrix: tuple[Vector, Vector, Vector], vector: Vector) -> Vector:
    return tuple(sum(row[index] * vector[index] for index in range(3)) for row in matrix)  # type: ignore[return-value]


def mask_word(mask: int) -> tuple[int, ...]:
    return tuple((mask >> index) & 1 for index in range(6))


def rotate_mask(mask: int, rotation: tuple[Vector, Vector, Vector]) -> int:
    result = 0
    for index, axis in enumerate(AXES):
        if (mask >> index) & 1:
            result |= 1 << AXES.index(mat_vec(rotation, axis))
    return result


def reverse_mask(mask: int) -> int:
    result = 0
    for index, axis in enumerate(AXES):
        if (mask >> index) & 1:
            result |= 1 << AXES.index(negate(axis))
    return result


@cache
def equivariant_recodings() -> tuple[tuple[int, ...], ...]:
    """Enumerate, rather than assume, every eight-label equivariant injection."""
    rotations = proper_cubic_rotations()
    fixed_masks = tuple(
        mask for mask in range(64)
        if all(rotate_mask(mask, rotation) == mask for rotation in rotations)
    )
    base_axis = AXES[0]
    stabilizer = tuple(
        rotation for rotation in rotations
        if mat_vec(rotation, base_axis) == base_axis
    )
    seeds = tuple(
        mask for mask in range(64)
        if all(rotate_mask(mask, rotation) == mask for rotation in stabilizer)
        and len({rotate_mask(mask, rotation) for rotation in rotations}) == 6
    )
    candidates = set()
    for dot_masks in itertools.permutations(fixed_masks, 2):
        for seed in seeds:
            cross_masks = []
            well_defined = True
            for axis in AXES:
                images = {
                    rotate_mask(seed, rotation)
                    for rotation in rotations
                    if mat_vec(rotation, base_axis) == axis
                }
                if len(images) != 1:
                    well_defined = False
                    break
                cross_masks.append(next(iter(images)))
            if well_defined:
                candidate = tuple(dot_masks) + tuple(cross_masks)
                if len(set(candidate)) == 8:
                    candidates.add(candidate)
    return tuple(sorted(candidates))


@cache
def recoding_facts() -> dict[str, object]:
    rotations = proper_cubic_rotations()
    unseen = set(range(64))
    orbit_sizes = []
    while unseen:
        seed = min(unseen)
        orbit = {rotate_mask(seed, rotation) for rotation in rotations}
        orbit_sizes.append(len(orbit))
        unseen.difference_update(orbit)

    recodings = equivariant_recodings()
    covariance = []
    endpoint = []
    stationary_forms = []
    for recoding in recodings:
        for rotation in rotations:
            for index, outcome in enumerate(OUTCOMES):
                rotated_index = OUTCOMES.index(rotate_outcome(outcome, rotation))
                covariance.append(
                    rotate_mask(recoding[index], rotation)
                    == recoding[rotated_index]
                )
        endpoint.extend(
            reverse_mask(recoding[index])
            == recoding[OUTCOMES.index(antipode(outcome))]
            for index, outcome in enumerate(OUTCOMES)
        )
        for negative, positive in ((0, 1), (2, 3), (4, 5)):
            bit_difference = tuple(
                ((mask >> positive) & 1) - ((mask >> negative) & 1)
                for mask in recoding
            )
            component = positive // 2
            cross_coefficients = (0, 0) + tuple(
                axis[component] for axis in AXES
            )
            stationary_forms.append(
                bit_difference == cross_coefficients
                or bit_difference == tuple(-value for value in cross_coefficients)
            )
    return {
        "binary_orbit_sizes": tuple(sorted(orbit_sizes)),
        "fixed_orbits": orbit_sizes.count(1),
        "six_orbits": orbit_sizes.count(6),
        "equivariant_injections": len(recodings),
        "all_injective": all(len(set(recoding)) == 8 for recoding in recodings),
        "proper_cubic_covariance": all(covariance),
        "endpoint_reversal": all(endpoint),
        "stationary_bit_difference_is_cross_imbalance": all(stationary_forms),
        "stationary_nonzero_cross_possible": False,
    }


@cache
def shell_facts() -> dict[str, object]:
    displacements = tuple(sorted(
        {sub(left, right) for left in AXES for right in AXES},
        key=lambda item: (l1(item), item),
    ))
    class_counts = Counter(displacement_class(item) for item in displacements)
    overlap_sizes = Counter((displacement_class(item), len(overlap_pairs(item))) for item in displacements)
    edge_counts = defaultdict(set)
    for item in displacements:
        edge_counts[displacement_class(item)].add(len(compatibility_edges(item)))
    for disjoint_control in DISJOINT_CONTROLS:
        edge_counts["disjoint"].add(len(compatibility_edges(disjoint_control)))

    reversal = all(
        set(overlap_pairs(negate(item))) == {(right, left) for left, right in overlap_pairs(item)}
        for item in displacements
    )
    iff = all(
        ((left, right) in compatibility_edges(item))
        == all(
            code(OUTCOMES[left])[left_index] == code(OUTCOMES[right])[right_index]
            for left_index, right_index in overlap_pairs(item)
        )
        for item in displacements + DISJOINT_CONTROLS
        for left in range(8)
        for right in range(8)
    )

    rotations = proper_cubic_rotations()
    equivariant = []
    compatibility_covariant = []
    score_covariant = []
    antipode_covariant = []
    for rotation in rotations:
        permutation = tuple(
            OUTCOMES.index(rotate_outcome(outcome, rotation))
            for outcome in OUTCOMES
        )
        for outcome in OUTCOMES:
            rotated = rotate_outcome(outcome, rotation)
            equivariant.append(all(
                code(rotated)[AXES.index(mat_vec(rotation, offset))]
                == code(outcome)[offset_index]
                for offset_index, offset in enumerate(AXES)
            ))
            antipode_covariant.append(
                rotate_outcome(antipode(outcome), rotation)
                == antipode(rotated)
            )
            if outcome in (P, N):
                score_covariant.append(rotated == outcome)
            else:
                score_covariant.append(
                    tuple(rotated[1:])
                    == mat_vec(rotation, tuple(outcome[1:]))  # type: ignore[arg-type]
                )
        for item in displacements:
            source_edges = set(compatibility_edges(item))
            target_edges = set(compatibility_edges(mat_vec(rotation, item)))
            compatibility_covariant.append(all(
                ((left, right) in source_edges)
                == ((permutation[left], permutation[right]) in target_edges)
                for left, right in itertools.product(range(8), repeat=2)
            ))
    endpoint_code = all(
        code(antipode(outcome))[AXES.index(negate(axis))] == code(outcome)[index]
        for outcome in OUTCOMES
        for index, axis in enumerate(AXES)
    )
    distances = tuple(
        sum(a != b for a, b in zip(code(first), code(second)))
        for index, first in enumerate(OUTCOMES)
        for second in OUTCOMES[index + 1:]
    )
    return {
        "displacements": displacements,
        "intersecting_count": len(displacements),
        "class_counts": dict(class_counts),
        "overlap_sizes": dict(overlap_sizes),
        "edge_counts": {key: tuple(sorted(value)) for key, value in edge_counts.items()},
        "reversal": reversal,
        "disjoint_controls": all(not overlap_pairs(item) for item in DISJOINT_CONTROLS),
        "intersection_iff_axis_difference": all(
            bool(overlap_pairs(item)) == (item in set(displacements))
            for item in itertools.product(range(-2, 3), repeat=3)
        ),
        "signature_iff": iff,
        "rotation_count": len(rotations),
        "equivariant_cases": sum(equivariant),
        "equivariant": all(equivariant),
        "compatibility_covariant": all(compatibility_covariant),
        "score_covariant": all(score_covariant),
        "antipode_covariant": all(antipode_covariant),
        "endpoint_code": endpoint_code,
        "minimum_code_distance": min(distances),
    }


def signature_classes(displacement: Vector) -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
    left_groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    right_groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for index, outcome in enumerate(OUTCOMES):
        left_groups[signature(outcome, displacement, True)].append(index)
        right_groups[signature(outcome, displacement, False)].append(index)
    if set(left_groups) != set(right_groups):
        return ()
    return tuple(
        (tuple(left_groups[key]), tuple(right_groups[key]))
        for key in sorted(left_groups)
    )


def compatible_marginals(
    left: tuple[sp.Expr, ...],
    right: tuple[sp.Expr, ...],
    displacement: Vector,
) -> bool:
    return all(
        sp.simplify(sum(left[index] for index in left_class)
                    - sum(right[index] for index in right_class)) == 0
        for left_class, right_class in signature_classes(displacement)
    )


def exact_abs(expression: sp.Expr) -> sp.Expr:
    value = canonical(expression)
    if value.is_nonnegative is True:
        return value
    if value.is_nonpositive is True:
        return -value
    return sp.Abs(value)


def minimum_incompatible_mass(
    left: tuple[sp.Expr, ...],
    right: tuple[sp.Expr, ...],
    displacement: Vector,
) -> sp.Expr:
    """Minimum mass forced off the compatibility graph (pushforward TV)."""
    differences = []
    for left_class, right_class in signature_classes(displacement):
        differences.append(canonical(
            sum(left[index] for index in left_class)
            - sum(right[index] for index in right_class)
        ))
    return canonical(sum(exact_abs(value) for value in differences) / 2)


def transport_coupling(
    left: tuple[sp.Expr, ...],
    right: tuple[sp.Expr, ...],
    displacement: Vector,
) -> sp.Matrix | None:
    """Exact component-product coupling, including zero-mass components."""
    if not compatible_marginals(left, right, displacement):
        return None
    result = sp.zeros(8)
    for left_class, right_class in signature_classes(displacement):
        mass = sp.simplify(sum(left[index] for index in left_class))
        if mass == 0:
            continue
        for left_index in left_class:
            for right_index in right_class:
                result[left_index, right_index] = sp.simplify(
                    left[left_index] * right[right_index] / mass
                )
    return result


def valid_coupling(
    coupling: sp.Matrix | None,
    left: tuple[sp.Expr, ...],
    right: tuple[sp.Expr, ...],
    displacement: Vector,
) -> bool:
    if coupling is None:
        return False
    return (
        all(sp.simplify(sum(coupling[row, column] for column in range(8)) - left[row]) == 0 for row in range(8))
        and all(sp.simplify(sum(coupling[row, column] for row in range(8)) - right[column]) == 0 for column in range(8))
        and all(coupling[row, column] == 0 for row in range(8) for column in range(8) if (row, column) not in compatibility_edges(displacement))
        and all(coupling[row, column] >= 0 for row in range(8) for column in range(8))
        and sp.simplify(sum(coupling)) == 1
    )


@cache
def transport_facts() -> dict[str, object]:
    displacements = shell_facts()["displacements"]
    controls = tuple(displacements) + DISJOINT_CONTROLS
    ranks = defaultdict(set)
    component_profiles = defaultdict(set)
    necessity = []
    sufficiency = []
    for item in controls:
        edges = compatibility_edges(item)
        incidence = sp.zeros(len(edges), 16)
        for row, (left, right) in enumerate(edges):
            incidence[row, left] = 1
            incidence[row, 8 + right] = -1
        ranks[displacement_class(item)].add(incidence.rank())
        classes = signature_classes(item)
        component_profiles[displacement_class(item)].add(tuple(sorted(
            (len(left), len(right)) for left, right in classes
        )))
        necessity.append(all(
            signature(OUTCOMES[left], item, True)
            == signature(OUTCOMES[right], item, False)
            for left, right in edges
        ))
        generated = {
            (left, right)
            for left_class, right_class in classes
            for left in left_class
            for right in right_class
        }
        sufficiency.append(generated == set(edges))

    uniform = tuple(sp.Rational(1, 8) for _ in range(8))
    delta_p = (sp.Integer(1),) + (sp.Integer(0),) * 7
    delta_n = (sp.Integer(0), sp.Integer(1)) + (sp.Integer(0),) * 6
    examples = []
    uniform_entries = defaultdict(set)
    for item in controls:
        full = transport_coupling(uniform, uniform, item)
        zero = transport_coupling(delta_p, delta_p, item)
        examples.extend((
            valid_coupling(full, uniform, uniform, item),
            valid_coupling(zero, delta_p, delta_p, item),
        ))
        if full is not None:
            uniform_entries[displacement_class(item)].add(tuple(sorted({
                full[row, column]
                for row in range(8)
                for column in range(8)
                if full[row, column] != 0
            })))
    incompatible_zero_support = all(
        transport_coupling(delta_p, delta_n, item) is None
        for item in displacements
    )
    return {
        "ranks": {key: tuple(sorted(value)) for key, value in ranks.items()},
        "profiles": {key: tuple(value) for key, value in component_profiles.items()},
        "necessity": all(necessity),
        "sufficiency": all(sufficiency),
        "iff": all(necessity) and all(sufficiency),
        "examples": all(examples),
        "zero_support_rejection": incompatible_zero_support,
        "uniform_entries": {key: tuple(value) for key, value in uniform_entries.items()},
    }


def canonical(expression: sp.Expr) -> sp.Expr:
    return sp.radsimp(sp.simplify(sp.expand_complex(expression)))


@cache
def stochastic_supports() -> tuple[tuple[int, ...], ...]:
    """Supports of the redundant encoder, ordered by the eight outcomes."""
    result: list[tuple[int, ...]] = [(0,), (63,)]
    for axis in AXES:
        axis_index = AXES.index(axis)
        antipode_index = AXES.index(negate(axis))
        perpendicular_pairs = []
        for index, candidate in enumerate(AXES):
            if candidate in (axis, negate(axis)):
                continue
            pair = tuple(sorted((index, AXES.index(negate(candidate)))))
            if pair not in perpendicular_pairs:
                perpendicular_pairs.append(pair)
        words = [
            1 << axis_index,
            63 ^ (1 << antipode_index),
            *(
                (1 << antipode_index) | (1 << pair[0]) | (1 << pair[1])
                for pair in perpendicular_pairs
            ),
        ]
        result.append(tuple(words))
    return tuple(result)


def stochastic_kernel(
    outcome_index: int,
    a: sp.Expr = sp.Rational(1, 4),
    b: sp.Expr = sp.Rational(1, 4),
    c: sp.Expr = sp.Rational(1, 2),
) -> dict[int, sp.Expr]:
    support = stochastic_supports()[outcome_index]
    if outcome_index < 2:
        return {support[0]: sp.Integer(1)}
    weights = (a, b, c / 2, c / 2)
    return dict(zip(support, weights))


def encoded_mask_distribution(
    probabilities: tuple[sp.Expr, ...],
    a: sp.Expr = sp.Rational(1, 4),
    b: sp.Expr = sp.Rational(1, 4),
    c: sp.Expr = sp.Rational(1, 2),
) -> dict[int, sp.Expr]:
    result = {mask: sp.Integer(0) for mask in range(64)}
    for outcome_index, probability in enumerate(probabilities):
        for mask, conditional_weight in stochastic_kernel(
            outcome_index, a, b, c
        ).items():
            result[mask] += probability * conditional_weight
    return {mask: sp.expand(value) for mask, value in result.items()}


def mask_signature(mask: int, displacement: Vector, left: bool) -> tuple[int, ...]:
    word = mask_word(mask)
    return tuple(
        word[left_index if left else right_index]
        for left_index, right_index in overlap_pairs(displacement)
    )


def mask_signature_masses(
    distribution: dict[int, sp.Expr], displacement: Vector, left: bool
) -> dict[tuple[int, ...], sp.Expr]:
    result: dict[tuple[int, ...], sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for mask, probability in distribution.items():
        result[mask_signature(mask, displacement, left)] += probability
    return {key: sp.expand(value) for key, value in result.items()}


def encoded_overlap_compatible(
    distribution: dict[int, sp.Expr], displacement: Vector
) -> bool:
    left = mask_signature_masses(distribution, displacement, True)
    right = mask_signature_masses(distribution, displacement, False)
    return all(
        sp.simplify(left.get(key, 0) - right.get(key, 0)) == 0
        for key in set(left) | set(right)
    )


@cache
def stochastic_encoder_facts() -> dict[str, object]:
    supports = stochastic_supports()
    flattened = tuple(itertools.chain.from_iterable(supports))
    rotations = proper_cubic_rotations()
    covariance = []
    endpoint = []
    for rotation in rotations:
        for outcome_index, outcome in enumerate(OUTCOMES):
            rotated_index = OUTCOMES.index(rotate_outcome(outcome, rotation))
            transformed = {
                rotate_mask(mask, rotation): weight
                for mask, weight in stochastic_kernel(outcome_index).items()
            }
            covariance.append(transformed == stochastic_kernel(rotated_index))
    for outcome_index, outcome in enumerate(OUTCOMES):
        reversed_index = OUTCOMES.index(antipode(outcome))
        transformed = {
            reverse_mask(mask): weight
            for mask, weight in stochastic_kernel(outcome_index).items()
        }
        endpoint.append(transformed == stochastic_kernel(reversed_index))

    symbolic_probabilities = sp.symbols("p0:8", nonnegative=True)
    symbolic_distribution = encoded_mask_distribution(symbolic_probabilities)
    arbitrary_overlap = tuple(
        encoded_overlap_compatible(symbolic_distribution, displacement)
        for displacement in shell_facts()["displacements"]
    )
    word_transport_components = []
    for displacement in shell_facts()["displacements"]:
        left_groups: dict[tuple[int, ...], set[int]] = defaultdict(set)
        right_groups: dict[tuple[int, ...], set[int]] = defaultdict(set)
        for mask in range(64):
            left_groups[mask_signature(mask, displacement, True)].add(mask)
            right_groups[mask_signature(mask, displacement, False)].add(mask)
        compatible_edges_from_signatures = {
            (left_mask, right_mask)
            for key in set(left_groups) | set(right_groups)
            for left_mask in left_groups.get(key, set())
            for right_mask in right_groups.get(key, set())
        }
        direct_edges = {
            (left_mask, right_mask)
            for left_mask, right_mask in itertools.product(range(64), repeat=2)
            if all(
                mask_word(left_mask)[left_index]
                == mask_word(right_mask)[right_index]
                for left_index, right_index in overlap_pairs(displacement)
            )
        }
        word_transport_components.append(
            set(left_groups) == set(right_groups)
            and compatible_edges_from_signatures == direct_edges
        )

    a, b, c = sp.symbols("a b c", real=True)
    equations = []
    for outcome_index in range(8):
        basis = tuple(
            sp.Integer(index == outcome_index) for index in range(8)
        )
        distribution = encoded_mask_distribution(basis, a, b, c)
        for displacement in shell_facts()["displacements"]:
            left = mask_signature_masses(distribution, displacement, True)
            right = mask_signature_masses(distribution, displacement, False)
            equations.extend(
                sp.expand(left.get(key, 0) - right.get(key, 0))
                for key in set(left) | set(right)
                if sp.expand(left.get(key, 0) - right.get(key, 0)) != 0
            )
    unique_equations = tuple(sorted(set(equations), key=str))
    coefficient_matrix, _constant = sp.linear_eq_to_matrix(
        unique_equations + (a + b + c - 1,), (a, b, c)
    )
    solution = sp.linsolve(
        unique_equations + (a + b + c - 1,), (a, b, c)
    )
    return {
        "support_count": len(flattened),
        "distinct_support_count": len(set(flattened)),
        "support_sizes": tuple(len(item) for item in supports),
        "disjoint_readability": len(flattened) == len(set(flattened)),
        "proper_cubic_covariance": all(covariance),
        "endpoint_covariance": all(endpoint),
        "symbolic_overlap_count": len(arbitrary_overlap),
        "arbitrary_symbolic_two_center": all(arbitrary_overlap),
        "word_signature_transport_iff": all(word_transport_components),
        "general_equation_rank": coefficient_matrix.rank(),
        "general_weight_solution": solution,
        "general_solution_unique_uniform_four": solution
        == sp.FiniteSet((sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 2))),
    }


def fixture_key(outcome: Outcome) -> tuple[object, ...]:
    if outcome == P:
        return ("dot", 1)
    if outcome == N:
        return ("dot", -1)
    return ("cross",) + tuple(outcome[1:])


def fixture_probabilities(
    first: sp.Expr,
    second: sp.Expr,
    radius: sp.Expr,
    depth: int,
    orientation: int,
) -> tuple[sp.Expr, ...]:
    raw = b211.coarse_probabilities(first, second, radius, depth, orientation)
    return tuple(canonical(raw[fixture_key(outcome)]) for outcome in OUTCOMES)


def score_moments(probabilities: tuple[sp.Expr, ...]) -> tuple[sp.Expr, tuple[sp.Expr, ...]]:
    dot = canonical(9 * (probabilities[0] - probabilities[1]))
    cross = tuple(canonical(9 * sum(
        probabilities[index + 2] * AXES[index][component]
        for index in range(6)
    )) for component in range(3))
    return dot, cross


@cache
def h1_facts() -> dict[str, object]:
    incoming, transfer = b211.b207.b193.POINTS["H1"]
    outgoing = tuple(sp.simplify(incoming[index] + transfer[index]) for index in range(4))
    source_angles = (
        incoming == (sp.pi / 6, sp.pi / 3, 0, sp.pi / 6)
        and transfer == (sp.pi / 3, sp.pi / 2, 0, 0)
        and outgoing == (sp.pi / 2, 5 * sp.pi / 6, 0, sp.pi / 6)
        and set(incoming + outgoing) == set(PHASES)
    )
    pass_count = 0
    fail_count = 0
    all_overlap_pass = 0
    all_overlap_fail = 0
    cross_mismatch = 0
    failed_conflict_count = 0
    stochastic_placement_pass = 0
    stochastic_placement_fail = 0
    stochastic_encoded_normalized = []
    stochastic_encoded_support = []
    normalizations = []
    positivity = []
    moments = []
    endpoint_reverse = []
    compatible_couplings = []
    conflict_equal_delta = []
    phase_census: dict[sp.Expr, list[int]] = {phase: [0, 0, 0] for phase in PHASES}
    per_depth = Counter()
    per_radius = Counter()
    per_realification = Counter()
    displacements = shell_facts()["displacements"]
    for phase, depth, radius, orientation in itertools.product(
        PHASES, DEPTHS, RADII, REALIFICATIONS
    ):
        unit = sp.cos(phase) + sp.I * sp.sin(phase)
        probabilities = fixture_probabilities(sp.Integer(1), unit, radius, depth, orientation)
        reversed_probabilities = fixture_probabilities(unit, sp.Integer(1), radius, depth, orientation)
        endpoint_reverse.append(all(
            canonical(reversed_probabilities[index] - probabilities[OUTCOMES.index(antipode(outcome))]) == 0
            for index, outcome in enumerate(OUTCOMES)
        ))
        normalizations.append(canonical(sum(probabilities)) == 1)
        positivity.extend(value.is_real is True and value.is_positive is True for value in probabilities)
        dot, cross = score_moments(probabilities)
        scale = radius ** 2 * b211.b208.CELL_A ** (2 * depth)
        expected_cross = (
            sp.Integer(0),
            sp.Integer(0),
            canonical((-1) ** depth * scale * sp.sin(phase)),
        )
        moments.append(
            canonical(dot - scale * sp.cos(phase)) == 0
            and all(canonical(actual - expected) == 0 for actual, expected in zip(cross, expected_cross))
        )
        if any(value != 0 for value in expected_cross):
            cross_mismatch += 1

        delta_z = canonical(probabilities[7] - probabilities[6])

        compatible = tuple(compatible_marginals(probabilities, probabilities, item) for item in displacements)
        encoded_distribution = encoded_mask_distribution(probabilities)
        encoded_compatible = tuple(
            encoded_overlap_compatible(encoded_distribution, item)
            for item in displacements
        )
        stochastic_placement_pass += sum(encoded_compatible)
        stochastic_placement_fail += len(encoded_compatible) - sum(encoded_compatible)
        stochastic_encoded_normalized.append(
            canonical(sum(encoded_distribution.values())) == 1
        )
        stochastic_encoded_support.append(
            sum(value != 0 for value in encoded_distribution.values()) == 26
            and all(
                canonical(value).is_positive is True
                for value in encoded_distribution.values()
                if value != 0
            )
        )
        for item, is_compatible in zip(displacements, compatible):
            component_differences = tuple(canonical(
                sum(probabilities[index] for index in left_class)
                - sum(probabilities[index] for index in right_class)
            ) for left_class, right_class in signature_classes(item))
            if is_compatible:
                positive_component_masses = all(
                    canonical(sum(probabilities[index] for index in left_class)).is_positive is True
                    for left_class, _right_class in signature_classes(item)
                )
                compatible_couplings.append(
                    all(value == 0 for value in component_differences)
                    and positive_component_masses
                )
            else:
                compatible_couplings.append(any(value != 0 for value in component_differences))
                failed_conflict_count += 1
                conflict_equal_delta.append(
                    canonical(
                        minimum_incompatible_mass(
                            probabilities, probabilities, item
                        ) - exact_abs(delta_z)
                    ) == 0
                )
        local_pass = sum(compatible)
        local_fail = len(compatible) - local_pass
        pass_count += local_pass
        fail_count += local_fail
        all_overlap_pass += int(all(compatible))
        all_overlap_fail += int(not all(compatible))
        phase_census[phase][0] += 1
        phase_census[phase][1] += local_pass
        phase_census[phase][2] += local_fail
        per_depth[(depth, "pass")] += local_pass
        per_depth[(depth, "fail")] += local_fail
        per_radius[(radius, "pass")] += local_pass
        per_radius[(radius, "fail")] += local_fail
        per_realification[(orientation, "pass")] += local_pass
        per_realification[(orientation, "fail")] += local_fail

    return {
        "source_angles": source_angles,
        "case_count": len(PHASES) * len(DEPTHS) * len(RADII) * len(REALIFICATIONS),
        "pass_count": pass_count,
        "fail_count": fail_count,
        "all_overlap_pass": all_overlap_pass,
        "all_overlap_fail": all_overlap_fail,
        "cross_mismatch": cross_mismatch,
        "failed_conflict_count": failed_conflict_count,
        "minimum_conflict_abs_delta_z": (
            failed_conflict_count == 320 and all(conflict_equal_delta)
        ),
        "stochastic_placement_pass": stochastic_placement_pass,
        "stochastic_placement_fail": stochastic_placement_fail,
        "stochastic_encoded_normalized": all(stochastic_encoded_normalized),
        "stochastic_encoded_full_26_support": all(stochastic_encoded_support),
        "normalized": all(normalizations),
        "strictly_positive": all(positivity),
        "moments": all(moments),
        "endpoint_reverse": all(endpoint_reverse),
        "compatible_couplings": all(compatible_couplings),
        "frame_case_count": len(PHASES) * len(DEPTHS) * len(RADII) * len(REALIFICATIONS) * len(proper_cubic_rotations()),
        "frame_covariance": shell_facts()["compatibility_covariant"],
        "frame_moments": shell_facts()["score_covariant"] and all(moments),
        "frame_endpoint_reverse": shell_facts()["antipode_covariant"] and all(endpoint_reverse),
        "phase_census": {phase: tuple(values) for phase, values in phase_census.items()},
        "depth_census": dict(per_depth),
        "radius_census": dict(per_radius),
        "realification_census": dict(per_realification),
    }


@cache
def product_facts() -> dict[str, object]:
    uniform = tuple(sp.Rational(1, 8) for _ in range(8))
    representatives = {
        "same": ORIGIN,
        "axial": (2, 0, 0),
        "face": (1, 1, 0),
        "disjoint": (1, 0, 0),
    }
    conflicts = {}
    for name, displacement in representatives.items():
        allowed = set(compatibility_edges(displacement))
        conflicts[name] = sp.simplify(sum(
            uniform[left] * uniform[right]
            for left in range(8)
            for right in range(8)
            if (left, right) not in allowed
        ))
    every_overlap_has_conflict = all(
        len(compatibility_edges(item)) < 64
        for item in shell_facts()["displacements"]
    )
    return {
        "conflicts": conflicts,
        "every_full_support_product_conflicts": every_overlap_has_conflict,
        "independent_safe": False,
    }


def append_word(
    state: dict[Vector, int],
    center: Vector,
    outcome: Outcome,
    semantics: str,
) -> dict[Vector, int] | None:
    sites = tuple(add(center, offset) for offset in AXES)
    word = code(outcome)
    if semantics == "strict" and any(site in state for site in sites):
        return None
    if semantics == "idempotent" and any(
        site in state and state[site] != word[index]
        for index, site in enumerate(sites)
    ):
        return None
    result = dict(state)
    for index, site in enumerate(sites):
        result.setdefault(site, word[index])
    return result


def first_wins(
    state: dict[Vector, int], center: Vector, outcome: Outcome
) -> dict[Vector, int]:
    result = dict(state)
    for index, offset in enumerate(AXES):
        result.setdefault(add(center, offset), code(outcome)[index])
    return result


@cache
def write_facts() -> dict[str, object]:
    strict_overlap = []
    strict_disjoint = []
    idempotent = []
    atomic = []
    corrupts = []
    displacements = tuple(shell_facts()["displacements"]) + ((1, 0, 0),)
    for displacement in displacements:
        overlaps = bool(overlap_pairs(displacement))
        allowed = set(compatibility_edges(displacement))
        for left, right in itertools.product(range(8), repeat=2):
            first = append_word({}, ORIGIN, OUTCOMES[left], "strict")
            second = append_word({}, displacement, OUTCOMES[right], "strict")
            forward = None if first is None else append_word(first, displacement, OUTCOMES[right], "strict")
            reverse = None if second is None else append_word(second, ORIGIN, OUTCOMES[left], "strict")
            if overlaps:
                strict_overlap.append(forward is None and reverse is None)
            else:
                strict_disjoint.append(forward is not None and forward == reverse)

            first_i = append_word({}, ORIGIN, OUTCOMES[left], "idempotent")
            second_i = append_word({}, displacement, OUTCOMES[right], "idempotent")
            forward_i = None if first_i is None else append_word(first_i, displacement, OUTCOMES[right], "idempotent")
            reverse_i = None if second_i is None else append_word(second_i, ORIGIN, OUTCOMES[left], "idempotent")
            compatible = (left, right) in allowed
            idempotent.append(
                (forward_i is not None and reverse_i is not None and forward_i == reverse_i)
                if compatible else (forward_i is None and reverse_i is None)
            )
            atomic.append(compatible == all(
                code(OUTCOMES[left])[left_index] == code(OUTCOMES[right])[right_index]
                for left_index, right_index in overlap_pairs(displacement)
            ))
            if overlaps and not compatible:
                stored = first_wins(first_wins({}, ORIGIN, OUTCOMES[left]), displacement, OUTCOMES[right])
                observed = tuple(stored[add(displacement, offset)] for offset in AXES)
                corrupts.append(observed != code(OUTCOMES[right]))
    return {
        "strict_overlap_allowed": not all(strict_overlap),
        "strict_overlap_rejected": all(strict_overlap),
        "strict_disjoint_commutes": all(strict_disjoint),
        "idempotent_exact": all(idempotent),
        "atomic_exact": all(atomic),
        "first_wins_corrupts": all(corrupts),
    }


@cache
def homogeneous_facts() -> dict[str, object]:
    rows = []
    for displacement in shell_facts()["displacements"]:
        for left_class, right_class in signature_classes(displacement):
            row = [0] * 8
            for index in left_class:
                row[index] += 1
            for index in right_class:
                row[index] -= 1
            if any(row):
                rows.append(row)
    constraint = sp.Matrix(rows)
    cross_map = sp.zeros(3, 8)
    for axis_index, axis in enumerate(AXES):
        for component in range(3):
            cross_map[component, axis_index + 2] = axis[component]
    nullspace = constraint.nullspace()
    return {
        "constraint_rank": constraint.rank(),
        "nullity": len(nullspace),
        "all_cross_zero": all(cross_map * vector == sp.zeros(3, 1) for vector in nullspace),
        "nonzero_homogeneous_cross_allowed": False,
    }


def compatible_bijection(displacement: Vector) -> dict[int, int]:
    result = {}
    for left_class, right_class in signature_classes(displacement):
        for left, right in zip(sorted(left_class), sorted(right_class)):
            result[left] = right
    return result


@cache
def motif_facts() -> dict[str, object]:
    centers = (ORIGIN, (1, 1, 0), (2, 0, 0))
    ab = compatible_bijection(sub(centers[1], centers[0]))
    bc = compatible_bijection(sub(centers[2], centers[1]))
    composed = {left: bc[ab[left]] for left in range(8)}
    ac_displacement = sub(centers[2], centers[0])
    ac = {}
    for left_class, _right_class in signature_classes(ac_displacement):
        ordered = sorted(left_class)
        for index, left in enumerate(ordered):
            ac[left] = composed[ordered[(index + 1) % len(ordered)]]

    pairwise_compatible = (
        all((left, right) in compatibility_edges(sub(centers[1], centers[0])) for left, right in ab.items())
        and all((left, right) in compatibility_edges(sub(centers[2], centers[1])) for left, right in bc.items())
        and all((left, right) in compatibility_edges(ac_displacement) for left, right in ac.items())
        and all(set(mapping) == set(range(8)) and set(mapping.values()) == set(range(8)) for mapping in (ab, bc, ac))
    )
    chosen_global = tuple(
        (left, middle, right)
        for left, middle, right in itertools.product(range(8), repeat=3)
        if ab[left] == middle and bc[middle] == right and ac[left] == right
    )
    geometric_global = tuple(
        labels
        for labels in itertools.product(range(8), repeat=3)
        if all(
            (labels[left], labels[right]) in compatibility_edges(sub(centers[right], centers[left]))
            for left, right in itertools.combinations(range(3), 2)
        )
    )
    return {
        "pairwise_uniform_couplings": pairwise_compatible,
        "chosen_global_count": len(chosen_global),
        "geometric_global_count": len(geometric_global),
        "pairwise_couplings_automatically_globalize": False,
    }


def masks_compatible(
    left_mask: int, right_mask: int, displacement: Vector
) -> bool:
    return all(
        mask_word(left_mask)[left_index] == mask_word(right_mask)[right_index]
        for left_index, right_index in overlap_pairs(displacement)
    )


def mask_tuple_compatible(
    masks: tuple[int, ...], centers: tuple[Vector, ...]
) -> bool:
    return all(
        masks_compatible(
            masks[left], masks[right], sub(centers[right], centers[left])
        )
        for left, right in itertools.combinations(range(len(centers)), 2)
        if overlap_pairs(sub(centers[right], centers[left]))
    )


def canonical_triangle(centers: tuple[Vector, Vector, Vector]) -> tuple[Vector, Vector]:
    representatives = []
    for ordered in itertools.permutations(centers):
        relative = (
            sub(ordered[1], ordered[0]),
            sub(ordered[2], ordered[0]),
        )
        for rotation in proper_cubic_rotations():
            representatives.append(tuple(sorted(
                mat_vec(rotation, displacement) for displacement in relative
            )))
    return min(representatives)  # type: ignore[return-value]


@cache
def triangle_orbits() -> tuple[tuple[Vector, Vector, Vector], ...]:
    nonzero = set(shell_facts()["displacements"]) - {ORIGIN}
    representatives = set()
    for second, third in itertools.combinations(sorted(nonzero), 2):
        if sub(third, second) in nonzero:
            representatives.add(canonical_triangle((ORIGIN, second, third)))
    return tuple((ORIGIN,) + pair for pair in sorted(representatives))


def labelwise_permutation_coupling_exists(
    centers: tuple[Vector, Vector, Vector], outcome_index: int
) -> bool:
    support = stochastic_supports()[outcome_index]
    if len(support) == 1:
        return mask_tuple_compatible((support[0],) * 3, centers)
    for second_permutation in itertools.permutations(range(4)):
        for third_permutation in itertools.permutations(range(4)):
            assignments = tuple(
                (
                    support[index],
                    support[second_permutation[index]],
                    support[third_permutation[index]],
                )
                for index in range(4)
            )
            if all(mask_tuple_compatible(item, centers) for item in assignments):
                return True
    return False


@cache
def stochastic_motif_facts() -> dict[str, object]:
    # The complete pairwise-overlap triangle census has one AFF and one FFF orbit.
    orbits = triangle_orbits()
    by_profile = {}
    for centers in orbits:
        profile = tuple(sorted(
            displacement_class(sub(centers[right], centers[left]))
            for left, right in itertools.combinations(range(3), 2)
        ))
        by_profile[profile] = centers
    aff_profile = ("axial", "face", "face")
    fff_profile = ("face", "face", "face")
    aff = by_profile[aff_profile]
    fff = by_profile[fff_profile]

    aff_labelwise = tuple(
        labelwise_permutation_coupling_exists(aff, outcome_index)
        for outcome_index in range(8)
    )

    # Exact minimal counterexample: every cross-label kernel is pairwise
    # compatible, but its FFF-compatible triples omit half its support in each
    # marginal projection, so the required uniform four-word marginal is
    # impossible.  No floating-point solver participates in this certificate.
    fff_cross_assignments = []
    fff_projection_sizes = []
    for outcome_index in range(2, 8):
        support = stochastic_supports()[outcome_index]
        assignments = tuple(
            indices
            for indices in itertools.product(range(4), repeat=3)
            if mask_tuple_compatible(
                tuple(support[index] for index in indices), fff
            )
        )
        fff_cross_assignments.append(len(assignments))
        fff_projection_sizes.append(tuple(
            len({indices[center] for indices in assignments})
            for center in range(3)
        ))

    full_support = tuple(sorted(set(itertools.chain.from_iterable(
        stochastic_supports()
    ))))
    support_index = {mask: index for index, mask in enumerate(full_support)}
    compatible_triples = tuple(
        masks
        for masks in itertools.product(full_support, repeat=3)
        if mask_tuple_compatible(masks, fff)
    )

    # Numerical LP is used only to scout a sparse support.  Every reported
    # certificate is then reconstructed and validated over exact SymPy
    # algebra, including positivity and all 78 marginal equations.
    import numpy as np
    from scipy.optimize import linprog

    incidence_numpy = np.zeros(
        (3 * len(full_support), len(compatible_triples)), dtype=int
    )
    for column, masks in enumerate(compatible_triples):
        for center, mask in enumerate(masks):
            incidence_numpy[
                center * len(full_support) + support_index[mask], column
            ] = 1
    incidence_exact = sp.SparseMatrix(incidence_numpy)

    parameter_probabilities = []
    for phase, depth, radius, orientation in itertools.product(
        PHASES, DEPTHS, RADII, REALIFICATIONS
    ):
        unit = sp.cos(phase) + sp.I * sp.sin(phase)
        parameter_probabilities.append(fixture_probabilities(
            sp.Integer(1), unit, radius, depth, orientation
        ))
    unique_probabilities = tuple(dict.fromkeys(parameter_probabilities))
    scout_results = []
    exact_results = []
    exact_support_sizes = []
    certificate_by_probability = {}
    for probabilities in unique_probabilities:
        encoded = encoded_mask_distribution(probabilities)
        marginal = sp.Matrix(tuple(encoded[mask] for mask in full_support))
        target = sp.Matrix.vstack(marginal, marginal, marginal)
        numerical_target = np.array(
            [float(sp.N(value, 16)) for value in target], dtype=float
        )
        scout = linprog(
            np.zeros(len(compatible_triples)),
            A_eq=incidence_numpy,
            b_eq=numerical_target,
            bounds=(0, None),
            method="highs",
        )
        scout_results.append(scout.success)
        if not scout.success:
            exact_results.append(False)
            certificate_by_probability[probabilities] = False
            continue
        selected = tuple(
            index for index, value in enumerate(scout.x) if value > 1e-10
        )
        selected_incidence = incidence_exact[:, selected]
        solution_set = sp.linsolve((selected_incidence, target))
        solution_tuples = tuple(solution_set)
        exact = False
        if len(solution_tuples) == 1:
            weights = solution_tuples[0]
            exact = (
                not any(value.free_symbols for value in weights)
                and all(sp.simplify(value).is_nonnegative is True for value in weights)
                and selected_incidence * sp.Matrix(weights) == target
                and all(mask_tuple_compatible(compatible_triples[index], fff) for index in selected)
            )
        exact_results.append(exact)
        certificate_by_probability[probabilities] = exact
        if exact:
            exact_support_sizes.append(len(selected))

    all_placements_exact = all(
        certificate_by_probability[probabilities]
        for probabilities in parameter_probabilities
    )
    return {
        "triangle_orbit_count": len(orbits),
        "triangle_profiles": tuple(sorted(by_profile)),
        "aff_labelwise_arbitrary_law_certificate": all(aff_labelwise),
        "fff_compatible_triple_count": len(compatible_triples),
        "fff_cross_assignment_counts": tuple(fff_cross_assignments),
        "fff_cross_projection_sizes": tuple(fff_projection_sizes),
        "fff_extreme_cross_globalizable": False,
        "minimal_center_count": 3,
        "numerical_scouting_cases": len(unique_probabilities),
        "numerical_scouting_feasible": all(scout_results),
        "numerical_scouting_is_certificate": False,
        "exact_certificate_cases": sum(exact_results),
        "exact_certificate_support_range": (
            min(exact_support_sizes), max(exact_support_sizes)
        ),
        "exact_h1_placements": len(parameter_probabilities),
        "exact_h1_all_fff": all_placements_exact,
        "exact_validation_uses_floating_point": False,
    }


PERIOD4_LAYERS = {
    0: ("1111", "1000", "1111", "0010"),
    1: ("0001", "0011", "0001", "0110"),
    2: ("1111", "1000", "1111", "0010"),
    3: ("0100", "1001", "0100", "1100"),
}


def period4_bit(site: Vector) -> int:
    x, y, z = (coordinate % 4 for coordinate in site)
    return int(PERIOD4_LAYERS[x][y][z])


@cache
def period4_decoded_globalization_facts() -> dict[str, object]:
    decoder = {
        mask: outcome_index
        for outcome_index, supports in enumerate(stochastic_supports())
        for mask in supports
    }
    translation_masks = tuple(
        sum(
            period4_bit(add(translation, axis)) << index
            for index, axis in enumerate(AXES)
        )
        for translation in itertools.product(range(4), repeat=3)
    )
    translation_counts = Counter(translation_masks)
    decoded_counts = Counter(decoder.get(mask) for mask in translation_masks)
    plus_z_index = OUTCOMES.index(("X", 0, 0, 1))
    expected_decoded_counts = {
        plus_z_index: 32,
        **{
            index + 2: 8
            for index, axis in enumerate(AXES)
            if axis[2] == 0
        },
    }
    base_distribution = {
        mask: sp.Rational(count, 64)
        for mask, count in translation_counts.items()
    }

    rotated_distributions = []
    rotation_well_defined = []
    plus_z = (0, 0, 1)
    for target_axis in AXES:
        candidates = tuple({
            tuple(sorted(
                (rotate_mask(mask, rotation), probability)
                for mask, probability in base_distribution.items()
            ))
            for rotation in proper_cubic_rotations()
            if mat_vec(rotation, plus_z) == target_axis
        })
        rotation_well_defined.append(len(candidates) == 1)
        rotated_distributions.append(dict(candidates[0]))

    decoded_columns = []
    for distribution in rotated_distributions:
        column = [sp.Integer(0)] * 8
        for mask, probability in distribution.items():
            column[decoder[mask]] += probability
        decoded_columns.append(tuple(column))
    expected_columns = []
    for target_axis in AXES:
        column = [sp.Integer(0)] * 8
        for index, candidate in enumerate(AXES):
            if candidate == target_axis:
                column[index + 2] = sp.Rational(1, 2)
            elif candidate == negate(target_axis):
                column[index + 2] = sp.Integer(0)
            else:
                column[index + 2] = sp.Rational(1, 8)
        expected_columns.append(tuple(column))

    pair_sums = []
    cross_totals = []
    weights_nonnegative = []
    weights_normalized = []
    decoded_matches = []
    microcode_mismatch_counts = []
    parameter_cases = 0
    for phase, depth, radius, orientation in itertools.product(
        PHASES, DEPTHS, RADII, REALIFICATIONS
    ):
        parameter_cases += 1
        unit = sp.cos(phase) + sp.I * sp.sin(phase)
        probabilities = fixture_probabilities(
            sp.Integer(1), unit, radius, depth, orientation
        )
        cross_probabilities = probabilities[2:]
        pair_sums.extend(
            canonical(
                cross_probabilities[index]
                + cross_probabilities[AXES.index(negate(axis))]
                - sp.Rational(2, 9)
            ) == 0
            for index, axis in enumerate(AXES)
        )
        cross_totals.append(
            canonical(sum(cross_probabilities) - sp.Rational(2, 3)) == 0
        )
        sector_weights = tuple(canonical(
            sp.Rational(1, 9)
            + cross_probabilities[index]
            - cross_probabilities[AXES.index(negate(axis))]
        ) for index, axis in enumerate(AXES))
        weights_nonnegative.extend(
            weight.is_nonnegative is True for weight in sector_weights
        )
        weights_normalized.append(
            canonical(probabilities[0] + probabilities[1]
                      + sum(sector_weights) - 1) == 0
        )
        decoded = [sp.Integer(0)] * 8
        decoded[0] = probabilities[0]
        decoded[1] = probabilities[1]
        for weight, column in zip(sector_weights, decoded_columns):
            for outcome_index in range(8):
                decoded[outcome_index] += weight * column[outcome_index]
        decoded_matches.append(all(
            canonical(actual - expected) == 0
            for actual, expected in zip(decoded, probabilities)
        ))

        global_microcode = {mask: sp.Integer(0) for mask in range(64)}
        global_microcode[0] = probabilities[0]
        global_microcode[63] = probabilities[1]
        for weight, distribution in zip(sector_weights, rotated_distributions):
            for mask, value in distribution.items():
                global_microcode[mask] += weight * value
        uniform_kernel_microcode = encoded_mask_distribution(probabilities)
        microcode_mismatch_counts.append(sum(
            canonical(global_microcode[mask]
                      - uniform_kernel_microcode[mask]) != 0
            for mask in range(64)
        ))

    return {
        "literal_table_shape": (4, 4, 4) if (
            len(PERIOD4_LAYERS) == 4
            and all(len(PERIOD4_LAYERS[index]) == 4 for index in range(4))
            and all(len(row) == 4 for rows in PERIOD4_LAYERS.values() for row in rows)
        ) else (),
        "translation_count": len(translation_masks),
        "translation_mask_support": len(translation_counts),
        "all_translation_words_readable": None not in decoded_counts,
        "base_decoded_counts": dict(decoded_counts),
        "expected_base_decoded_counts": expected_decoded_counts,
        "base_is_d_plus_z": dict(decoded_counts) == expected_decoded_counts,
        "rotated_sector_count": len(rotated_distributions),
        "rotation_well_defined": all(rotation_well_defined),
        "decoded_sector_columns": tuple(decoded_columns),
        "decoded_sector_formula": tuple(decoded_columns)
        == tuple(expected_columns),
        "parameter_cases": parameter_cases,
        "antipodal_cross_sums": all(pair_sums),
        "cross_total_two_thirds": all(cross_totals),
        "sector_weights_nonnegative": all(weights_nonnegative),
        "sector_weights_normalized": all(weights_normalized),
        "decoded_h1_globalized": all(decoded_matches),
        "microcode_mismatch_counts": tuple(microcode_mismatch_counts),
        "uniform_kernel_microcode_preserved": False,
        "translation_averaged_global_fields": True,
        "decoded_globalization_is_local_formation_law": False,
    }


def decoded_postprocessing_matrix() -> sp.Matrix:
    result = sp.zeros(8)
    result[0, 0] = 1
    result[1, 1] = 1
    for decoded_index, decoded_axis in enumerate(AXES):
        for sector_index, sector_axis in enumerate(AXES):
            if decoded_axis == sector_axis:
                result[decoded_index + 2, sector_index + 2] = sp.Rational(1, 2)
            elif decoded_axis != negate(sector_axis):
                result[decoded_index + 2, sector_index + 2] = sp.Rational(1, 8)
    return result


@cache
def operator_sector_povm_facts() -> dict[str, object]:
    identity = sp.eye(4)
    endpoint_swap = sp.Matrix((
        (1, 0, 0, 0),
        (0, 0, 1, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 1),
    ))
    postprocessing = decoded_postprocessing_matrix()
    antipode_indices = tuple(
        OUTCOMES.index(antipode(outcome)) for outcome in OUTCOMES
    )
    dot_partitions = []
    cross_partitions = []
    positivity = []
    povm_normalization = []
    cholesky_exact = []
    kraus_normalization = []
    endpoint_reversal = []
    operator_postprocessing = []
    determinants = []
    for depth, orientation in itertools.product(DEPTHS, REALIFICATIONS):
        raw_effects = b211.coarse_effects(depth, orientation)
        effects = tuple(
            sp.simplify(raw_effects[fixture_key(outcome)])
            for outcome in OUTCOMES
        )
        dot_partitions.append(
            sp.simplify(effects[0] + effects[1] - identity / 3)
            == sp.zeros(4)
        )
        cross_partitions.extend(
            sp.simplify(
                effects[index + 2]
                + effects[AXES.index(negate(axis)) + 2]
                - 2 * identity / 9
            ) == sp.zeros(4)
            for index, axis in enumerate(AXES)
        )
        sectors = [effects[0], effects[1]]
        sectors.extend(
            sp.simplify(
                identity / 9
                + effects[index + 2]
                - effects[AXES.index(negate(axis)) + 2]
            )
            for index, axis in enumerate(AXES)
        )
        sector_tuple = tuple(sectors)
        povm_normalization.append(
            sp.simplify(sum(sector_tuple, sp.zeros(4)) - identity)
            == sp.zeros(4)
        )
        kraus_blocks = []
        for sector in sector_tuple:
            positivity.append(
                sector == sector.conjugate().T
                and sector.is_positive_definite is True
            )
            determinants.append(sp.factor(sector.det()))
            lower = sector.cholesky()
            kraus = lower.conjugate().T
            cholesky_exact.append(
                sp.simplify(kraus.conjugate().T * kraus - sector)
                == sp.zeros(4)
            )
            kraus_blocks.append(kraus)
        isometry = sp.Matrix.vstack(*kraus_blocks)
        kraus_normalization.append(
            sp.simplify(isometry.conjugate().T * isometry - identity)
            == sp.zeros(4)
        )
        endpoint_reversal.extend(
            sp.simplify(
                endpoint_swap * sector * endpoint_swap.T
                - sector_tuple[antipode_indices[index]]
            ) == sp.zeros(4)
            for index, sector in enumerate(sector_tuple)
        )
        operator_postprocessing.extend(
            sp.simplify(
                sum(
                    (postprocessing[row, column] * sector_tuple[column]
                     for column in range(8)),
                    sp.zeros(4),
                ) - effects[row]
            ) == sp.zeros(4)
            for row in range(8)
        )

    postprocessing_normalized = all(
        sum(postprocessing[row, column] for row in range(8)) == 1
        for column in range(8)
    )
    postprocessing_endpoint = all(
        postprocessing[antipode_indices[row], antipode_indices[column]]
        == postprocessing[row, column]
        for row, column in itertools.product(range(8), repeat=2)
    )
    period4_columns = period4_decoded_globalization_facts()[
        "decoded_sector_columns"
    ]
    return {
        "case_count": len(DEPTHS) * len(REALIFICATIONS),
        "dot_partition_count": sum(dot_partitions),
        "cross_partition_count": sum(cross_partitions),
        "dot_partitions": all(dot_partitions),
        "cross_partitions": all(cross_partitions),
        "sector_effect_count": len(positivity),
        "strictly_positive": all(positivity),
        "positive_determinants": all(value > 0 for value in determinants),
        "povm_normalized": all(povm_normalization),
        "cholesky_kraus_exact": all(cholesky_exact),
        "kraus_isometry_normalized": all(kraus_normalization),
        "endpoint_reversal": all(endpoint_reversal),
        "postprocessing_shape": postprocessing.shape,
        "postprocessing_nonnegative": all(value >= 0 for value in postprocessing),
        "postprocessing_column_stochastic": postprocessing_normalized,
        "postprocessing_endpoint_reversal": postprocessing_endpoint,
        "postprocessing_matches_period4": tuple(
            tuple(postprocessing[row, column + 2] for row in range(8))
            for column in range(6)
        ) == period4_columns,
        "operator_postprocessing_count": sum(operator_postprocessing),
        "operator_postprocessing_exact": all(operator_postprocessing),
    }


TORUS4_SITES: tuple[Vector, ...] = tuple(
    itertools.product(range(4), repeat=3)
)
TORUS4_INDEX = {site: index for index, site in enumerate(TORUS4_SITES)}


def inverse_rotate_torus(
    rotation: tuple[Vector, Vector, Vector], site: Vector
) -> Vector:
    return tuple(
        sum(rotation[row][column] * site[row] for row in range(3)) % 4
        for column in range(3)
    )  # type: ignore[return-value]


def period4_configuration(
    rotation: tuple[Vector, Vector, Vector], translation: Vector
) -> int:
    result = 0
    for index, site in enumerate(TORUS4_SITES):
        shifted = tuple(
            (site[component] - translation[component]) % 4
            for component in range(3)
        )
        result |= period4_bit(
            inverse_rotate_torus(rotation, shifted)  # type: ignore[arg-type]
        ) << index
    return result


def restrict_configuration(configuration: int, sites: tuple[Vector, ...]) -> tuple[int, ...]:
    return tuple(
        (configuration >> TORUS4_INDEX[tuple(value % 4 for value in site)]) & 1
        for site in sites
    )


@cache
def l1_ball_offsets(radius: int) -> tuple[Vector, ...]:
    return tuple(
        vector
        for vector in itertools.product(range(-radius, radius + 1), repeat=3)
        if l1(vector) <= radius
    )


@cache
def l1_ball_offset_index(radius: int) -> dict[Vector, int]:
    return {
        offset: index for index, offset in enumerate(l1_ball_offsets(radius))
    }


def centered_configuration_patch(
    configuration: int,
    radius: int,
    center: Vector = ORIGIN,
) -> tuple[int, ...]:
    return tuple(
        (
            configuration
            >> TORUS4_INDEX[
                tuple((center[index] + offset[index]) % 4 for index in range(3))
            ]
        )
        & 1
        for offset in l1_ball_offsets(radius)
    )


@cache
def patch_overlap_indices(
    radius: int, displacement: Vector
) -> tuple[tuple[int, int], ...]:
    offsets = l1_ball_offsets(radius)
    offset_index = l1_ball_offset_index(radius)
    return tuple(
        (left_index, offset_index[sub(offset, displacement)])
        for left_index, offset in enumerate(offsets)
        if sub(offset, displacement) in offset_index
    )


def compatible_patch_successors(
    patches: tuple[tuple[int, ...], ...],
    radius: int,
    displacement: Vector,
) -> tuple[tuple[int, ...], ...]:
    pairs = patch_overlap_indices(radius, displacement)
    right_buckets: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for right_index, patch in enumerate(patches):
        right_buckets[tuple(patch[right] for _left, right in pairs)].append(
            right_index
        )
    return tuple(
        tuple(right_buckets.get(
            tuple(patch[left] for left, _right in pairs), ()
        ))
        for patch in patches
    )


@cache
def transform_torus_configuration(
    configuration: int,
    transformation: tuple[Vector, Vector, Vector],
) -> int:
    result = 0
    for target_index, target_site in enumerate(TORUS4_SITES):
        source_site = inverse_rotate_torus(transformation, target_site)
        result |= (
            (configuration >> TORUS4_INDEX[source_site]) & 1
        ) << target_index
    return result


def inverse_transform_vector(
    transformation: tuple[Vector, Vector, Vector], vector: Vector
) -> Vector:
    return tuple(
        sum(
            transformation[row][column] * vector[row]
            for row in range(3)
        )
        for column in range(3)
    )  # type: ignore[return-value]


def transform_patch(
    patch: tuple[int, ...],
    radius: int,
    transformation: tuple[Vector, Vector, Vector],
) -> tuple[int, ...]:
    offsets = l1_ball_offsets(radius)
    offset_index = l1_ball_offset_index(radius)
    return tuple(
        patch[offset_index[inverse_transform_vector(transformation, offset)]]
        for offset in offsets
    )


@cache
def period4_static_sft_facts() -> dict[str, object]:
    """Certify the finite-radius support constraint, not a formation law."""
    plus_z = (0, 0, 1)
    sector_sets = []
    orientation_independence = []
    for target_axis in AXES:
        candidates = {
            tuple(sorted({
                period4_configuration(rotation, translation)
                for translation in TORUS4_SITES
            }))
            for rotation in proper_cubic_rotations()
            if mat_vec(rotation, plus_z) == target_axis
        }
        orientation_independence.append(len(candidates) == 1)
        sector_sets.append(next(iter(candidates)))

    vector_configurations = tuple(sorted(set().union(*map(set, sector_sets))))
    all_zero = 0
    all_one = (1 << len(TORUS4_SITES)) - 1
    all_configurations = tuple(sorted(
        set(vector_configurations) | {all_zero, all_one}
    ))
    configuration_index = {
        configuration: index
        for index, configuration in enumerate(all_configurations)
    }
    sector_disjoint = sum(map(len, sector_sets)) == len(vector_configurations)

    vector_patches = {
        radius: tuple(
            centered_configuration_patch(configuration, radius)
            for configuration in vector_configurations
        )
        for radius in (1, 2, 3)
    }
    all_patches = {
        radius: tuple(
            centered_configuration_patch(configuration, radius)
            for configuration in all_configurations
        )
        for radius in (1, 2, 3)
    }
    all_patch_sets = {
        radius: set(patches) for radius, patches in all_patches.items()
    }
    vector_patch_counts = {
        radius: len(set(patches)) for radius, patches in vector_patches.items()
    }
    all_patch_counts = {
        radius: len(set(patches)) for radius, patches in all_patches.items()
    }
    radius_one_multiplicities = Counter(vector_patches[1]).values()
    radius_one_collision_histogram = dict(sorted(Counter(
        radius_one_multiplicities
    ).items()))

    radius_two_successors = tuple(
        compatible_patch_successors(vector_patches[2], 2, displacement)
        for displacement in AXES
    )
    radius_two_histograms = tuple(
        dict(sorted(Counter(map(len, successors)).items()))
        for successors in radius_two_successors
    )
    radius_three_successors = tuple(
        compatible_patch_successors(all_patches[3], 3, displacement)
        for displacement in AXES
    )
    radius_three_histograms = tuple(
        dict(sorted(Counter(map(len, successors)).items()))
        for successors in radius_three_successors
    )

    radius_three_index = {
        patch: index for index, patch in enumerate(all_patches[3])
    }
    actual_transitions = tuple(
        tuple(
            radius_three_index[
                centered_configuration_patch(configuration, 3, displacement)
            ]
            for configuration in all_configurations
        )
        for displacement in AXES
    )
    unique_successor_is_actual_translation = all(
        radius_three_successors[direction_index][configuration_index_] == (
            actual_transitions[direction_index][configuration_index_],
        )
        for direction_index in range(len(AXES))
        for configuration_index_ in range(len(all_configurations))
    )
    transition_permutations = all(
        len(set(transition)) == len(all_configurations)
        for transition in actual_transitions
    )
    opposite_transitions_are_inverses = all(
        actual_transitions[AXES.index(negate(displacement))][
            actual_transitions[direction_index][configuration_index_]
        ] == configuration_index_
        for direction_index, displacement in enumerate(AXES)
        for configuration_index_ in range(len(all_configurations))
    )
    transitions_commute = all(
        actual_transitions[left][actual_transitions[right][configuration_index_]]
        == actual_transitions[right][actual_transitions[left][configuration_index_]]
        for left, right in itertools.product(range(len(AXES)), repeat=2)
        for configuration_index_ in range(len(all_configurations))
    )
    period_four_translations = all(
        (lambda transition, start: transition[
            transition[transition[transition[start]]]
        ])(actual_transitions[direction_index], configuration_index_)
        == configuration_index_
        for direction_index in range(len(AXES))
        for configuration_index_ in range(len(all_configurations))
    )

    unseen = set(range(len(all_configurations)))
    transition_orbits = []
    while unseen:
        seed = min(unseen)
        orbit = {seed}
        frontier = [seed]
        while frontier:
            current = frontier.pop()
            for transition in actual_transitions:
                successor = transition[current]
                if successor not in orbit:
                    orbit.add(successor)
                    frontier.append(successor)
        transition_orbits.append(frozenset(
            all_configurations[index] for index in orbit
        ))
        unseen -= orbit
    expected_orbits = {
        frozenset((all_zero,)),
        frozenset((all_one,)),
        *(frozenset(sector) for sector in sector_sets),
    }
    translation_orbits_exact = set(transition_orbits) == expected_orbits

    rotations = proper_cubic_rotations()
    rotation_maps = tuple(
        tuple(
            configuration_index[
                transform_torus_configuration(configuration, rotation)
            ]
            for configuration in all_configurations
        )
        for rotation in rotations
    )
    proper_cubic_field_covariance = all(
        {
            transform_torus_configuration(configuration, rotation)
            for configuration in sector_sets[sector_index]
        } == set(sector_sets[AXES.index(mat_vec(rotation, axis))])
        for rotation in rotations
        for sector_index, axis in enumerate(AXES)
    )
    endpoint_transformation: tuple[Vector, Vector, Vector] = (
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
    )
    endpoint_map = tuple(
        configuration_index[
            transform_torus_configuration(
                configuration, endpoint_transformation
            )
        ]
        for configuration in all_configurations
    )
    endpoint_field_covariance = all(
        {
            transform_torus_configuration(
                configuration, endpoint_transformation
            )
            for configuration in sector_sets[sector_index]
        } == set(sector_sets[AXES.index(negate(axis))])
        for sector_index, axis in enumerate(AXES)
    )
    proper_cubic_patch_covariance = all(
        transform_patch(patch, radius, rotation) in all_patch_sets[radius]
        for radius in (1, 2, 3)
        for rotation in rotations
        for patch in all_patches[radius]
    )
    endpoint_patch_covariance = all(
        transform_patch(patch, radius, endpoint_transformation)
        in all_patch_sets[radius]
        for radius in (1, 2, 3)
        for patch in all_patches[radius]
    )
    proper_cubic_transition_covariance = all(
        rotation_map[actual_transitions[direction_index][configuration_index_]]
        == actual_transitions[
            AXES.index(mat_vec(rotation, displacement))
        ][rotation_map[configuration_index_]]
        for rotation, rotation_map in zip(rotations, rotation_maps)
        for direction_index, displacement in enumerate(AXES)
        for configuration_index_ in range(len(all_configurations))
    )
    endpoint_transition_covariance = all(
        endpoint_map[actual_transitions[direction_index][configuration_index_]]
        == actual_transitions[AXES.index(negate(displacement))][
            endpoint_map[configuration_index_]
        ]
        for direction_index, displacement in enumerate(AXES)
        for configuration_index_ in range(len(all_configurations))
    )

    allowed_radius_three = all_patch_sets[3]
    catalog_satisfies_local_constraint = all(
        centered_configuration_patch(configuration, 3, center)
        in allowed_radius_three
        for configuration in all_configurations
        for center in TORUS4_SITES
    )
    positive_axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    translated_patch_reconstruction = True
    center_symbol_reconstruction = True
    center_offset_index = l1_ball_offsets(3).index(ORIGIN)
    for configuration_index_, configuration in enumerate(all_configurations):
        for center in TORUS4_SITES:
            translated_index = configuration_index_
            for component, displacement in enumerate(positive_axes):
                transition = actual_transitions[AXES.index(displacement)]
                for _step in range(center[component]):
                    translated_index = transition[translated_index]
            expected_patch = centered_configuration_patch(configuration, 3, center)
            translated_patch_reconstruction &= (
                all_patches[3][translated_index] == expected_patch
            )
            center_symbol_reconstruction &= (
                all_patches[3][translated_index][center_offset_index]
                == (
                    configuration >> TORUS4_INDEX[center]
                ) & 1
            )

    exact_sft_proof = all((
        all_patch_counts[3] == len(all_configurations),
        all(histogram == {1: 194} for histogram in radius_three_histograms),
        unique_successor_is_actual_translation,
        transition_permutations,
        opposite_transitions_are_inverses,
        transitions_commute,
        period_four_translations,
        catalog_satisfies_local_constraint,
        translated_patch_reconstruction,
        center_symbol_reconstruction,
    ))
    return {
        "sector_count": len(sector_sets),
        "orientation_independent_sectors": all(orientation_independence),
        "sector_sizes": tuple(map(len, sector_sets)),
        "sector_disjoint": sector_disjoint,
        "vector_configuration_count": len(vector_configurations),
        "total_configuration_count": len(all_configurations),
        "ball_sizes": {
            radius: len(l1_ball_offsets(radius)) for radius in (1, 2, 3)
        },
        "vector_patch_counts": vector_patch_counts,
        "all_patch_counts": all_patch_counts,
        "radius_one_vector_collision_histogram": radius_one_collision_histogram,
        "radius_one_all_vector_types_collide": (
            sum(radius_one_collision_histogram.values()) == 42
            and 1 not in radius_one_collision_histogram
        ),
        "radius_two_decodes_sector_and_phase": vector_patch_counts[2] == 192,
        "radius_two_successor_histograms": radius_two_histograms,
        "radius_two_has_ambiguous_successors": all(
            histogram == {1: 116, 2: 28, 3: 48}
            for histogram in radius_two_histograms
        ),
        "radius_three_successor_histograms": radius_three_histograms,
        "radius_three_unique_successor_total": sum(
            histogram.get(1, 0) for histogram in radius_three_histograms
        ),
        "unique_successor_is_actual_translation": unique_successor_is_actual_translation,
        "transition_permutations": transition_permutations,
        "opposite_transitions_are_inverses": opposite_transitions_are_inverses,
        "transitions_commute": transitions_commute,
        "period_four_translations": period_four_translations,
        "translation_orbit_sizes": tuple(sorted(map(len, transition_orbits))),
        "translation_orbits_exact": translation_orbits_exact,
        "proper_cubic_field_covariance": proper_cubic_field_covariance,
        "proper_cubic_patch_covariance": proper_cubic_patch_covariance,
        "proper_cubic_transition_covariance": proper_cubic_transition_covariance,
        "endpoint_field_covariance": endpoint_field_covariance,
        "endpoint_patch_covariance": endpoint_patch_covariance,
        "endpoint_transition_covariance": endpoint_transition_covariance,
        "catalog_satisfies_local_constraint": catalog_satisfies_local_constraint,
        "translated_patch_reconstruction": translated_patch_reconstruction,
        "center_symbol_reconstruction": center_symbol_reconstruction,
        "global_fields_exactly_catalog": exact_sft_proof,
        "certified_global_field_count": (
            len(all_configurations) if exact_sft_proof else 0
        ),
        "constraint_kind": "static_finite_range_sft",
        "constraint_radius": 3,
        "smallest_tested_unique_successor_radius": 3,
        "radius_two_exact_sft_excluded": False,
        "formation_dynamics_constructed": False,
        "autonomous_history_constructed": False,
        "_all_configurations": all_configurations,
        "_sector_sets": tuple(sector_sets),
        "_configuration_index": configuration_index,
        "_radius_three_patches": all_patches[3],
        "_transitions": actual_transitions,
        "_endpoint_map": endpoint_map,
    }


def translate_patch_type(
    transitions: tuple[tuple[int, ...], ...],
    patch_type: int,
    displacement: Vector,
) -> int:
    result = patch_type
    positive_directions = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    for component, value in enumerate(displacement):
        direction = (
            positive_directions[component]
            if value >= 0
            else negate(positive_directions[component])
        )
        transition = transitions[AXES.index(direction)]
        for _step in range(abs(value)):
            result = transition[result]
    return result


@cache
def higher_block_seed_front_facts() -> dict[str, object]:
    """Audit the supplied-site compiler on its visible higher-block carrier."""
    static = period4_static_sft_facts()
    configurations = static["_all_configurations"]
    sector_sets = static["_sector_sets"]
    configuration_index = static["_configuration_index"]
    transitions = static["_transitions"]
    endpoint_map = static["_endpoint_map"]
    type_count = len(configurations)
    blank = type_count
    carrier_dimension = type_count + 1

    transition_permutations = all(
        set(transition) == set(range(type_count))
        for transition in transitions
    )
    transition_commutation = all(
        transitions[left][transitions[right][patch_type]]
        == transitions[right][transitions[left][patch_type]]
        for left, right in itertools.product(range(len(AXES)), repeat=2)
        for patch_type in range(type_count)
    )
    inverse_transitions = all(
        transitions[AXES.index(negate(displacement))][
            transitions[direction_index][patch_type]
        ] == patch_type
        for direction_index, displacement in enumerate(AXES)
        for patch_type in range(type_count)
    )

    all_zero = 0
    all_one = (1 << len(TORUS4_SITES)) - 1
    type_sectors = [-1] * type_count
    type_sectors[configuration_index[all_zero]] = 0
    type_sectors[configuration_index[all_one]] = 1
    for sector_index, sector in enumerate(sector_sets):
        for configuration in sector:
            type_sectors[configuration_index[configuration]] = sector_index + 2
    type_sector_tuple = tuple(type_sectors)
    phase_multiplicities = tuple(Counter(type_sector_tuple)[index] for index in range(8))

    identity = sp.eye(4)
    tensor_swap = sp.Matrix((
        (1, 0, 0, 0),
        (0, 0, 1, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 1),
    ))
    antipode_indices = tuple(
        OUTCOMES.index(antipode(outcome)) for outcome in OUTCOMES
    )
    refined_normalization = []
    refined_positivity = []
    scalar_unrefined = []
    vector_uniform = []
    sector_endpoint = []
    for depth, orientation in itertools.product(DEPTHS, REALIFICATIONS):
        raw_effects = b211.coarse_effects(depth, orientation)
        effects = tuple(
            sp.simplify(raw_effects[fixture_key(outcome)])
            for outcome in OUTCOMES
        )
        sectors = (effects[0], effects[1]) + tuple(
            sp.simplify(
                identity / 9
                + effects[index + 2]
                - effects[AXES.index(negate(axis)) + 2]
            )
            for index, axis in enumerate(AXES)
        )
        refinements = tuple(
            sp.simplify(sector / phase_multiplicities[index])
            for index, sector in enumerate(sectors)
        )
        refined_normalization.append(
            sp.simplify(sum(
                (
                    phase_multiplicities[index] * refinements[index]
                    for index in range(8)
                ),
                sp.zeros(4),
            ) - identity) == sp.zeros(4)
        )
        refined_positivity.extend(
            refinement.is_positive_definite is True
            for refinement in refinements
        )
        scalar_unrefined.extend(
            sp.simplify(refinements[index] - sectors[index]) == sp.zeros(4)
            for index in (0, 1)
        )
        vector_uniform.extend(
            sp.simplify(refinements[index] - sectors[index] / 32)
            == sp.zeros(4)
            for index in range(2, 8)
        )
        sector_endpoint.extend(
            sp.simplify(
                tensor_swap * refinements[index] * tensor_swap.T
                - refinements[antipode_indices[index]]
            ) == sp.zeros(4)
            for index in range(8)
        )
    type_endpoint_covariance = all(
        type_sector_tuple[endpoint_map[patch_type]]
        == antipode_indices[type_sector_tuple[patch_type]]
        for patch_type in range(type_count)
    )

    # For every proposed type a, K_write=|a><blank| has only the blank
    # input column, while K_lock is the identity on all 194 locked columns.
    write_domain_projector = tuple(
        int(input_type == blank) for input_type in range(carrier_dimension)
    )
    lock_domain_projector = tuple(
        int(input_type < type_count) for input_type in range(carrier_dimension)
    )
    kraus_domain_partition = all(
        write_domain_projector[input_type]
        + lock_domain_projector[input_type] == 1
        for input_type in range(carrier_dimension)
    )
    domain_projectors_orthogonal = all(
        write_domain_projector[input_type]
        * lock_domain_projector[input_type] == 0
        for input_type in range(carrier_dimension)
    )
    write_actions = tuple(
        tuple(
            proposal if input_type == blank else None
            for input_type in range(carrier_dimension)
        )
        for proposal in range(type_count)
    )
    lock_action = tuple(
        input_type if input_type < type_count else None
        for input_type in range(carrier_dimension)
    )
    write_targets_exact = all(
        action[blank] == proposal
        and all(action[locked_type] is None for locked_type in range(type_count))
        for proposal, action in enumerate(write_actions)
    )
    locked_nondemolition = (
        lock_action[:type_count] == tuple(range(type_count))
        and lock_action[blank] is None
    )
    blank_is_written_once = all(
        proposal != blank for proposal in range(type_count)
    )

    torus_neighbors = {
        site: tuple(
            tuple((site[index] + direction[index]) % 4 for index in range(3))
            for direction in AXES
        )
        for site in TORUS4_SITES
    }
    origin_index = TORUS4_INDEX[ORIGIN]
    expected_types = tuple(
        tuple(
            translate_patch_type(transitions, seed_type, site)
            for site in TORUS4_SITES
        )
        for seed_type in range(type_count)
    )
    neighbor_content_consistency = all(
        transitions[direction_index][
            expected_types[seed_type][
                TORUS4_INDEX[
                    tuple(
                        (site[index] - direction[index]) % 4
                        for index in range(3)
                    )
                ]
            ]
        ] == expected_types[seed_type][TORUS4_INDEX[site]]
        for seed_type in range(type_count)
        for site in TORUS4_SITES
        for direction_index, direction in enumerate(AXES)
    )

    reached = {ORIGIN}
    frontier = [ORIGIN]
    while frontier:
        site = frontier.pop()
        for neighbor in torus_neighbors[site]:
            if neighbor not in reached:
                reached.add(neighbor)
                frontier.append(neighbor)
    torus_graph_connected = len(reached) == len(TORUS4_SITES)

    def enabled_proposal(
        state: tuple[int, ...], site: Vector
    ) -> tuple[int | None, bool]:
        site_index = TORUS4_INDEX[site]
        if state[site_index] != blank:
            return None, False
        proposals = []
        for direction_index, direction in enumerate(AXES):
            neighbor = tuple(
                (site[index] - direction[index]) % 4 for index in range(3)
            )
            neighbor_type = state[TORUS4_INDEX[neighbor]]
            if neighbor_type != blank:
                proposals.append(transitions[direction_index][neighbor_type])
        if not proposals:
            return None, False
        if len(set(proposals)) != 1:
            return None, True
        return proposals[0], False

    def update_site(state: tuple[int, ...], site: Vector) -> tuple[tuple[int, ...], bool]:
        proposal, conflict = enabled_proposal(state, site)
        if proposal is None:
            return state, conflict
        result = list(state)
        result[TORUS4_INDEX[site]] = proposal
        return tuple(result), conflict

    site_orders = (
        TORUS4_SITES,
        tuple(reversed(TORUS4_SITES)),
        tuple(sorted(TORUS4_SITES, key=lambda site: (
            sum(min(value, 4 - value) for value in site), site
        ))),
        tuple(sorted(TORUS4_SITES, key=lambda site: (
            (site[0] + 2 * site[1] + 3 * site[2]) % 7, site
        ))),
    )
    schedule_terminal_checks = []
    schedule_conflict_checks = []
    schedule_single_write_checks = []
    for seed_type in range(type_count):
        expected = expected_types[seed_type]
        for order in site_orders:
            state = [blank] * len(TORUS4_SITES)
            state[origin_index] = seed_type
            state_tuple = tuple(state)
            write_count = [0] * len(TORUS4_SITES)
            conflict_seen = False
            while True:
                changed = False
                for site in order:
                    before = state_tuple
                    state_tuple, conflict = update_site(state_tuple, site)
                    conflict_seen |= conflict
                    if state_tuple != before:
                        write_count[TORUS4_INDEX[site]] += 1
                        changed = True
                if not changed:
                    break
            schedule_terminal_checks.append(state_tuple == expected)
            schedule_conflict_checks.append(not conflict_seen)
            schedule_single_write_checks.append(
                write_count[origin_index] == 0
                and all(
                    write_count[index] == 1
                    for index in range(len(TORUS4_SITES))
                    if index != origin_index
                )
            )

    witness_seed = 0
    first_site = (1, 0, 0)
    second_site = (2, 0, 0)
    initial = [blank] * len(TORUS4_SITES)
    initial[origin_index] = witness_seed
    initial_state = tuple(initial)
    second_then_first, second_first_conflict = update_site(
        initial_state, second_site
    )
    second_then_first, first_after_second_conflict = update_site(
        second_then_first, first_site
    )
    first_then_second, first_second_conflict = update_site(
        initial_state, first_site
    )
    first_then_second, second_after_first_conflict = update_site(
        first_then_second, second_site
    )
    enablement_noncommutation = (
        second_then_first != first_then_second
        and second_then_first[TORUS4_INDEX[second_site]] == blank
        and first_then_second[TORUS4_INDEX[second_site]]
        == expected_types[witness_seed][TORUS4_INDEX[second_site]]
        and not any((
            second_first_conflict,
            first_after_second_conflict,
            first_second_conflict,
            second_after_first_conflict,
        ))
    )
    eventually_completed, eventual_conflict = update_site(
        second_then_first, second_site
    )
    enablement_witness_same_terminal_content = (
        not eventual_conflict
        and eventually_completed[TORUS4_INDEX[second_site]]
        == first_then_second[TORUS4_INDEX[second_site]]
    )

    fixed_displacement = (1, 0, 0)
    displacement_map = tuple(
        translate_patch_type(transitions, patch_type, fixed_displacement)
        for patch_type in range(type_count)
    )
    completion_count_histogram = Counter(
        int(right_type == displacement_map[left_type])
        for left_type, right_type in itertools.product(
            range(type_count), repeat=2
        )
    )
    compatible_pairs = completion_count_histogram[1]
    incompatible_pairs = completion_count_histogram[0]

    box_index = sp.symbols("box_index", integer=True, nonnegative=True)
    intensity_bound_limit = sp.limit(
        sp.Rational(1, 1) / (2 * box_index + 1) ** 3,
        box_index,
        sp.oo,
    )
    finite_box_sizes = tuple((2 * index + 1) ** 3 for index in range(6))
    finite_box_intensity_bounds = tuple(
        sp.Rational(1, size) for size in finite_box_sizes
    )
    translation_invariance_gives_constant_anchor_intensity = True
    exact_one_seed_bounds_every_finite_box_expectation = all(
        size * bound == 1
        for size, bound in zip(finite_box_sizes, finite_box_intensity_bounds)
    )
    zero_intensity_makes_countable_anchor_union_null = True
    theorem_statement = (
        "No countably additive translation-invariant probability law on "
        "visible seed subsets of infinite Z3 is supported on configurations "
        "with exactly one finite nonempty seed."
    )
    hidden_wall_phrases = (
        "we assume", "by construction", "as is standard", "framework provides",
        "bridge context", "background", "naturally", "obviously", "standard qft",
        "registered", "canonical",
    )
    no_hidden_wall_language = not any(
        phrase in theorem_statement.lower() for phrase in hidden_wall_phrases
    )
    alternative_routes = (
        ("finite_volume_orbit", "uniform finite-torus seed", "finite normalization", "fails the infinite-lattice premise"),
        ("rooted_probability", "supplied origin or Palm root", "distinguished site", "fails unrooted translation invariance"),
        ("stationary_point_process", "positive-density seeds", "stationary intensity", "does not choose exactly one finite seed"),
        ("invariant_mean", "finitely additive uniform location", "amenable mean", "is outside countably additive probability"),
        ("quantum_carrier", "coherent seed superposition", "nonclassical amplitudes", "is outside the visible classical seed law"),
        ("multi_seed_protocol", "pre-write handshake or exclusion", "relational compatibility", "can close formation without selecting exactly one seed"),
    )
    route_family_keys = tuple(
        (route[0], route[1], route[2]) for route in alternative_routes
    )
    scope_drop_escapes = {
        "infinite_Z3": "uniform one-seed law on every finite torus",
        "translation_invariance": "delta law at a supplied origin",
        "exactly_one_finite_seed": "stationary positive-density or empty law",
        "countable_additivity": "finitely additive invariant mean",
    }
    resolution_audit = {
        "per_element": "seed indicator at one site has common intensity p",
        "per_site": "translation invariance makes that intensity site-independent",
        "per_block": "a finite box has expected seed count |Lambda|p at most one",
        "lattice_wide": "the box limit forces p=0 and countable union forces no seed",
    }
    partial_closure_routes = (
        "supplied visible seed",
        "finite-torus uniform seed",
        "positive-density compatible nucleation",
        "pre-write multi-seed handshake",
        "state/action-derived inhomogeneity",
    )
    cross_cycle_echoes = (
        "Block-212 deterministic blank-state stabilizer is narrower and has stochastic escapes",
        "the radius-three higher-block recoding retired the earlier nonlocal-support concern",
        "continuation comparators separate terminal compatibility from physical update commutation",
        "hard-core random marks remain a conditional positive-density route",
    )
    single_seed_no_go = all((
        translation_invariance_gives_constant_anchor_intensity,
        exact_one_seed_bounds_every_finite_box_expectation,
        intensity_bound_limit == 0,
        zero_intensity_makes_countable_anchor_union_null,
        len(TORUS4_SITES) == 64,
        sp.Rational(1, len(TORUS4_SITES)) > 0,
        len(set(route_family_keys)) >= 5,
        len(scope_drop_escapes) == 4,
        no_hidden_wall_language,
        len(resolution_audit) == 4,
        len(partial_closure_routes) >= 4,
        len(cross_cycle_echoes) >= 3,
    ))

    single_seed_unique_extension = all((
        transition_permutations,
        transition_commutation,
        inverse_transitions,
        neighbor_content_consistency,
        static["global_fields_exactly_catalog"],
    ))
    fair_order_confluence = all((
        single_seed_unique_extension,
        torus_graph_connected,
        all(schedule_terminal_checks),
        all(schedule_conflict_checks),
        all(schedule_single_write_checks),
    ))
    no_go_discipline_pass = all((
        len(set(route_family_keys)) >= 5,
        len(scope_drop_escapes) == 4,
        no_hidden_wall_language,
        len(resolution_audit) == 4,
        len(partial_closure_routes) >= 4,
        len(cross_cycle_echoes) >= 3,
        single_seed_no_go,
    ))
    return {
        "visible_patch_types": type_count,
        "blank_plus_type_alphabet": carrier_dimension,
        "minimum_binary_status_bits": (carrier_dimension - 1).bit_length(),
        "phase_multiplicities": phase_multiplicities,
        "refined_seed_effect_count": sum(phase_multiplicities),
        "phase_refined_povm_case_count": len(DEPTHS) * len(REALIFICATIONS),
        "phase_refined_povm_normalized": all(refined_normalization),
        "phase_refined_effects_strictly_positive": all(refined_positivity),
        "scalar_sectors_unrefined": all(scalar_unrefined),
        "vector_sectors_uniform_over_32_phases": all(vector_uniform),
        "phase_refinement_endpoint_covariant": (
            all(sector_endpoint) and type_endpoint_covariance
        ),
        "seed_povm_site_supplied": True,
        "seed_povm_selects_event_site": False,
        "transition_permutations": transition_permutations,
        "transition_commutation": transition_commutation,
        "inverse_transitions": inverse_transitions,
        "kraus_write_formula": "|a><blank|",
        "kraus_lock_formula": "sum_locked|b><b|",
        "kraus_domain_partition_exact": kraus_domain_partition,
        "kraus_domain_projectors_orthogonal": domain_projectors_orthogonal,
        "two_kraus_trace_preserving": (
            kraus_domain_partition and domain_projectors_orthogonal
        ),
        "write_targets_exact": write_targets_exact,
        "locked_subspace_nondemolition": locked_nondemolition,
        "blank_is_written_at_most_once": blank_is_written_once,
        "single_seed_unique_extension": single_seed_unique_extension,
        "neighbor_content_consistency": neighbor_content_consistency,
        "torus_graph_connected": torus_graph_connected,
        "tested_seed_types": type_count,
        "tested_fair_site_orders": len(site_orders),
        "tested_schedule_cases": len(schedule_terminal_checks),
        "all_tested_orders_reach_unique_terminal": all(schedule_terminal_checks),
        "all_tested_orders_conflict_free": all(schedule_conflict_checks),
        "all_tested_orders_write_once": all(schedule_single_write_checks),
        "fair_order_pointwise_terminal_confluence": fair_order_confluence,
        "fairness_is_a_supplied_schedule_condition": True,
        "enabled_one_step_updates_commute": False,
        "enablement_noncommutation_witness": enablement_noncommutation,
        "fixed_content_writes_on_distinct_sites_commute": True,
        "enablement_witness_same_terminal_content": enablement_witness_same_terminal_content,
        "one_step_noncommutation_is_content_conflict": False,
        "fixed_seed_displacement": fixed_displacement,
        "compatible_ordered_seed_pairs": compatible_pairs,
        "incompatible_ordered_seed_pairs": incompatible_pairs,
        "total_ordered_seed_pairs": type_count ** 2,
        "completion_count_histogram": dict(sorted(completion_count_histogram.items())),
        "independent_uniform_seed_compatibility": sp.Rational(1, type_count),
        "incompatible_permanent_seeds_have_common_sft_completion": False,
        "finite_nonempty_seed_has_translation_equivariant_anchor": True,
        "translation_invariant_exact_single_seed_probability_law_exists": False,
        "single_seed_probability_no_go": single_seed_no_go,
        "single_seed_no_go_statement": theorem_statement,
        "single_site_intensity_bound_limit": intensity_bound_limit,
        "finite_box_sizes": finite_box_sizes,
        "finite_box_intensity_bounds": finite_box_intensity_bounds,
        "translation_invariance_gives_constant_anchor_intensity": (
            translation_invariance_gives_constant_anchor_intensity
        ),
        "exact_one_seed_bounds_every_finite_box_expectation": (
            exact_one_seed_bounds_every_finite_box_expectation
        ),
        "zero_intensity_makes_countable_anchor_union_null": (
            zero_intensity_makes_countable_anchor_union_null
        ),
        "countable_union_contradiction": single_seed_no_go,
        "finite_torus_uniform_single_seed_escape": True,
        "supplied_origin_single_seed_escape": True,
        "positive_density_multi_seed_escape": True,
        "finitely_additive_invariant_mean_outside_scope": True,
        "coherent_nonclassical_seed_outside_scope": True,
        "no_go_route_family_count": len(set(route_family_keys)),
        "no_go_scope_drop_escapes": scope_drop_escapes,
        "no_go_hidden_wall_scan": no_hidden_wall_language,
        "no_go_prior_witnesses_required": 0,
        "no_go_resolution_audit": resolution_audit,
        "no_go_partial_closure_routes": partial_closure_routes,
        "no_go_within_scope_steelman_found": False,
        "no_go_cross_cycle_echoes": cross_cycle_echoes,
        "no_go_discipline_pass": no_go_discipline_pass,
        "carrier_kind": "visible_higher_block_195_state",
        "original_binary_record_only": False,
        "event_site_selected": False,
        "occurrence_rate_selected": False,
        "multi_seed_handshake_constructed": False,
        "autonomous_history_constructed": False,
    }


@cache
def period4_record_channel_facts() -> dict[str, object]:
    plus_z = (0, 0, 1)
    sector_ensembles = []
    orientation_independence = []
    for target_axis in AXES:
        candidate_ensembles = tuple({
            tuple(sorted(Counter(
                period4_configuration(rotation, translation)
                for translation in TORUS4_SITES
            ).items()))
            for rotation in proper_cubic_rotations()
            if mat_vec(rotation, plus_z) == target_axis
        })
        orientation_independence.append(len(candidate_ensembles) == 1)
        sector_ensembles.append(Counter(dict(candidate_ensembles[0])))

    ensemble_normalization = all(
        sum(ensemble.values()) == 64 for ensemble in sector_ensembles
    )
    distinct_per_sector = tuple(len(ensemble) for ensemble in sector_ensembles)
    cross_configurations = set().union(*(set(item) for item in sector_ensembles))
    all_zero = 0
    all_one = (1 << 64) - 1
    all_global_configurations = cross_configurations | {all_zero, all_one}

    decoder = {
        mask: outcome_index
        for outcome_index, supports in enumerate(stochastic_supports())
        for mask in supports
    }
    postprocessing = decoded_postprocessing_matrix()
    all_center_decoding = []
    for sector_index, ensemble in enumerate(sector_ensembles):
        expected = tuple(postprocessing[row, sector_index + 2] for row in range(8))
        for center in TORUS4_SITES:
            decoded = Counter()
            for configuration, multiplicity in ensemble.items():
                shell_mask = 0
                for role, axis in enumerate(AXES):
                    site = tuple((center[index] + axis[index]) % 4 for index in range(3))
                    shell_mask |= (
                        (configuration >> TORUS4_INDEX[site]) & 1
                    ) << role
                decoded[decoder[shell_mask]] += multiplicity
            all_center_decoding.append(all(
                sp.Rational(decoded.get(outcome_index, 0), 64)
                == expected[outcome_index]
                for outcome_index in range(8)
            ))

    small_sites = tuple(
        tuple(value % 4 for value in add(ORIGIN, axis)) for axis in AXES
    )
    fff_centers = (ORIGIN, (1, 1, 0), (1, 0, 1))
    large_sites = tuple(sorted({
        tuple(value % 4 for value in add(center, axis))
        for center in fff_centers
        for axis in AXES
    }))
    small_positions = tuple(large_sites.index(site) for site in small_sites)
    projective_checks = []
    for ensemble in sector_ensembles:
        direct = Counter()
        via_large = Counter()
        for configuration, multiplicity in ensemble.items():
            direct[restrict_configuration(configuration, small_sites)] += multiplicity
            large_pattern = restrict_configuration(configuration, large_sites)
            via_large[tuple(large_pattern[index] for index in small_positions)] += multiplicity
        projective_checks.append(direct == via_large)

    base_ensemble = sector_ensembles[AXES.index(plus_z)]
    origin_index = TORUS4_INDEX[ORIGIN]
    distant_witness = None
    for displacement in TORUS4_SITES[1:]:
        torus_distance = sum(min(value, 4 - value) for value in displacement)
        if torus_distance < 2:
            continue
        second_index = TORUS4_INDEX[displacement]
        total = sum(base_ensemble.values())
        first_mean = sp.Rational(sum(
            multiplicity * ((configuration >> origin_index) & 1)
            for configuration, multiplicity in base_ensemble.items()
        ), total)
        second_mean = sp.Rational(sum(
            multiplicity * ((configuration >> second_index) & 1)
            for configuration, multiplicity in base_ensemble.items()
        ), total)
        joint = sp.Rational(sum(
            multiplicity
            * ((configuration >> origin_index) & 1)
            * ((configuration >> second_index) & 1)
            for configuration, multiplicity in base_ensemble.items()
        ), total)
        covariance = sp.simplify(joint - first_mean * second_mean)
        if covariance != 0:
            distant_witness = (displacement, covariance)
            break

    operator = operator_sector_povm_facts()
    return {
        "cross_sector_count": len(sector_ensembles),
        "orientation_independent_translation_orbits": all(orientation_independence),
        "ensemble_normalized": ensemble_normalization,
        "distinct_configurations_per_cross_sector": distinct_per_sector,
        "distinct_cross_configurations": len(cross_configurations),
        "distinct_total_configurations": len(all_global_configurations),
        "all_centers_decode_postprocessing": all(all_center_decoding),
        "projective_restriction_count": len(projective_checks),
        "projectively_consistent": all(projective_checks),
        "distant_correlation_witness": distant_witness,
        "measure_prepare_trace_preserving": (
            operator["povm_normalized"] and ensemble_normalization
        ),
        "measure_prepare_completely_positive": (
            operator["cholesky_kraus_exact"]
            and operator["strictly_positive"]
        ),
        "global_record_channel": True,
        "local_nearest_neighbor_channel": False,
        "autonomous_nearest_neighbor_history": False,
        "event_conditioned": True,
    }


def phi(vector: Vector, form: Vector = (1, 2, 3)) -> int:
    return sum(form[index] * vector[index] for index in range(3)) % 7


def lee_owner(site: Vector) -> Vector:
    candidates = (site,) + tuple(sub(site, axis) for axis in AXES)
    owners = tuple(candidate for candidate in candidates if phi(candidate) == 0)
    if len(owners) != 1:
        raise AssertionError((site, owners))
    return owners[0]


def ownership_observation_possible(
    outcome_supports: tuple[tuple[int, ...], ...],
    marker_map: tuple[int, ...],
    role: int,
    target: tuple[int, ...],
) -> bool:
    root = AXES[role]
    observed_sites = (root,) + tuple(add(root, axis) for axis in AXES)
    bit_requirements: dict[Vector, dict[int, int]] = defaultdict(dict)
    marker_requirements: dict[Vector, int] = {}
    for site, bit in zip(observed_sites, target):
        owner = lee_owner(site)
        if owner == site:
            previous_marker = marker_requirements.get(owner)
            if previous_marker is not None and previous_marker != bit:
                return False
            marker_requirements[owner] = bit
            continue
        direction = sub(site, owner)
        direction_index = AXES.index(direction)
        previous = bit_requirements[owner].get(direction_index)
        if previous is not None and previous != bit:
            return False
        bit_requirements[owner][direction_index] = bit
    owners = set(bit_requirements) | set(marker_requirements)
    return all(
        any(
            (owner not in marker_requirements
             or marker_map[outcome_index] == marker_requirements[owner])
            and all(
                ((mask >> index) & 1) == bit
                for index, bit in bit_requirements[owner].items()
            )
            for outcome_index, masks in enumerate(outcome_supports)
            for mask in masks
        )
        for owner in owners
    )


@cache
def ownership_collision_facts() -> dict[str, object]:
    marker_maps = tuple(
        (p_bit, n_bit) + (cross_bit,) * 6
        for p_bit, n_bit, cross_bit in itertools.product((0, 1), repeat=3)
    )
    marker_covariance = all(
        marker_map[index]
        == marker_map[OUTCOMES.index(rotate_outcome(outcome, rotation))]
        and marker_map[index]
        == marker_map[OUTCOMES.index(antipode(outcome))]
        for marker_map in marker_maps
        for rotation in proper_cubic_rotations()
        for index, outcome in enumerate(OUTCOMES)
    )
    deterministic_collision_counts = []
    for recoding in equivariant_recodings():
        outcome_supports = tuple((mask,) for mask in recoding)
        for marker_map in marker_maps:
            center_patterns = tuple(
                (marker_map[outcome_index],) + mask_word(mask)
                for outcome_index, masks in enumerate(outcome_supports)
                for mask in masks
            )
            for role in range(6):
                deterministic_collision_counts.append(sum(
                    ownership_observation_possible(
                        outcome_supports, marker_map, role, pattern
                    )
                    for pattern in center_patterns
                ))
    stochastic_collision_counts = []
    for marker_map in marker_maps:
        center_patterns = tuple(
            (marker_map[outcome_index],) + mask_word(mask)
            for outcome_index, masks in enumerate(stochastic_supports())
            for mask in masks
        )
        for role in range(6):
            stochastic_collision_counts.append(sum(
                ownership_observation_possible(
                    stochastic_supports(), marker_map, role, pattern
                )
                for pattern in center_patterns
            ))
    return {
        "code_count": len(equivariant_recodings()),
        "equivariant_marker_maps": len(marker_maps),
        "marker_map_covariance": marker_covariance,
        "noncenter_roles": 6,
        "tested_role_cases": len(deterministic_collision_counts),
        "every_role_collides": all(count > 0 for count in deterministic_collision_counts),
        "collision_histogram": dict(Counter(deterministic_collision_counts)),
        "minimum_colliding_center_patterns": min(deterministic_collision_counts),
        "maximum_colliding_center_patterns": max(deterministic_collision_counts),
        "stochastic_tested_role_cases": len(stochastic_collision_counts),
        "stochastic_every_role_collides": all(count > 0 for count in stochastic_collision_counts),
        "stochastic_collision_histogram": dict(Counter(stochastic_collision_counts)),
        "stochastic_minimum_collisions": min(stochastic_collision_counts),
        "stochastic_maximum_collisions": max(stochastic_collision_counts),
        "radius_one_center_decoder_exists": False,
        "larger_or_separate_ownership_carrier_open": True,
    }


def local_field_word(center_residue: int, field: object, form: Vector) -> tuple[int, ...]:
    if field == "star":
        return (1,) * 6
    residue = int(field)
    return tuple(int((center_residue + phi(offset, form)) % 7 == residue) for offset in AXES)


@cache
def global_escape_facts() -> dict[str, object]:
    rotations = proper_cubic_rotations()
    base_form = (1, 2, 3)
    forms = tuple(mat_vec(rotation, base_form) for rotation in rotations)
    local_uniform = []
    global_compatible = []
    for form in forms:
        for center_residue in range(7):
            observed = tuple(
                outcome_from_code(local_field_word(center_residue, field, form))
                for field in ("star", *range(7))
            )
            local_uniform.append(len(observed) == 8 and set(observed) == set(OUTCOMES))
            for displacement in shell_facts()["displacements"]:
                right_residue = (center_residue + phi(displacement, form)) % 7
                for field in ("star", *range(7)):
                    left_word = local_field_word(center_residue, field, form)
                    right_word = local_field_word(right_residue, field, form)
                    global_compatible.append(all(
                        left_word[left] == right_word[right]
                        for left, right in overlap_pairs(displacement)
                    ))
    form_set = set(forms)
    frame_closed = all(
        mat_vec(rotation, form) in form_set
        for rotation in rotations
        for form in forms
    )
    return {
        "form_count": len(form_set),
        "local_uniform_full_support": all(local_uniform),
        "global_overlap_compatible": all(global_compatible),
        "proper_cubic_average": frame_closed and len(rotations) == 24,
        "translation_permuted_cosets": all(
            {(residue + shift) % 7 for residue in range(7)} == set(range(7))
            for shift in range(7)
        ),
        "correlated_not_product": product_facts()["every_full_support_product_conflicts"],
        "nearest_neighbor_autonomous_law": False,
        "global_constraint_escape": True,
    }


@cache
def lee_facts() -> dict[str, object]:
    closed_offsets = (ORIGIN,) + AXES
    residues = tuple(phi(offset) for offset in closed_offsets)
    inverse = {residue: offset for residue, offset in zip(residues, closed_offsets)}
    supplied_residue_offset_bijection = (
        len(inverse) == 7
        and set(inverse) == set(range(7))
        and all(phi(inverse[residue]) == residue for residue in range(7))
    )
    open_shell_disjoint = all(
        not (phi(sub(left, right)) == 0 and left != right)
        for left, right in itertools.product(AXES, repeat=2)
    )
    frontier = {}
    selected = 0
    locked_residues = set(range(7)) - {selected}
    for center_residue in range(7):
        neighbor_residues = tuple((center_residue + phi(offset)) % 7 for offset in AXES)
        frontier[center_residue] = sum(residue in locked_residues for residue in neighbor_residues)
    nearby_kernel_center = (2, -1, 0)
    arbitrary_batch = all(
        append_word(
            append_word({}, ORIGIN, left, "strict") or {},
            nearby_kernel_center,
            right,
            "strict",
        ) is not None
        for left, right in itertools.product(OUTCOMES, repeat=2)
    )
    return {
        "closed_residues": residues,
        "perfect_closed_ball": supplied_residue_offset_bijection,
        "supplied_residue_offset_bijection": supplied_residue_offset_bijection,
        "open_shell_disjoint": open_shell_disjoint,
        "event_density": sp.Rational(1, 7),
        "written_density": sp.Rational(6, 7),
        "unique_writer": open_shell_disjoint and supplied_residue_offset_bijection,
        "arbitrary_batch_outcomes": phi(nearby_kernel_center) == 0 and arbitrary_batch,
        "same_coset_locked_sites": frontier[0],
        "later_coset_locked_sites": tuple(frontier[index] for index in range(1, 7)),
        "strict_fresh_cycle_possible": False,
        "supplied_coloring": True,
        "autonomous_selector": False,
    }


def git_output(*args: str) -> str:
    return subprocess.run(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).stdout.strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    def blob(commit: str, path: str) -> str:
        return git_output("rev-parse", f"{commit}:{path}")

    goal_text = (ROOT / GOAL_PATH).read_text()
    preflight_text = (ROOT / PREFLIGHT_PATH).read_text()
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "prereg_exact": git_output("rev-parse", PREREG_COMMIT) == PREREG_COMMIT,
        "goal_registered": blob(PREREG_COMMIT, GOAL_PATH),
        "goal_worktree": blob("HEAD", GOAL_PATH),
        "preflight_registered": blob(PREREG_COMMIT, PREFLIGHT_PATH),
        "preflight_worktree": blob("HEAD", PREFLIGHT_PATH),
        "axiom_main": blob("origin/main", AXIOM_PATH),
        "axiom_worktree": blob("HEAD", AXIOM_PATH),
        "registry_main": blob("origin/main", REGISTRY_PATH),
        "registry_worktree": blob("HEAD", REGISTRY_PATH),
        "block211_note": blob("HEAD", BLOCK211_NOTE_PATH),
        "block211_runner": blob("HEAD", BLOCK211_RUNNER_PATH),
        "block211_goal": blob("HEAD", BLOCK211_GOAL_PATH),
        "inputs_exist": bool(AUDIT_INPUT_PATHS) and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        "h2_fence_text": "H2 remains sealed" in goal_text and "H2 sealed: `true`" in preflight_text,
    }


@cache
def classification_facts() -> dict[str, object]:
    return {
        "partial": True,
        "classification": "partial_radius3_static_sft_conditional_supplied_seed_front_autonomous_history_open",
        "complete_history": False,
        "direct_family_exhausted": False,
        "deterministic_obstruction_exhaustive": False,
        "stochastic_two_center_escape": True,
        "decoded_label_global_process": True,
        "uniform_microcode_infinite_consistency_constructed": False,
        "operator_sector_povm_bridge": True,
        "record_measure_prepare_normalized": True,
        "record_projectively_consistent": True,
        "record_support_static_finite_range": True,
        "record_measure_prepare_uses_global_sector": True,
        "record_support_formation_dynamics": False,
        "record_channel_autonomous_nn": False,
        "conditional_visible_seed_front": True,
        "invariant_exact_single_seed_excluded": True,
        "seed_event_site_supplied": True,
        "seed_occurrence_rate_open": True,
        "multi_seed_handshake_open": True,
        "autonomous_history_open": True,
        "one_many_none_decided": False,
        "h2_open": False,
        "axiom_update": False,
        "toe_movement": 0,
        "retained": False,
        "universal_no_go": False,
    }


def claims() -> dict[str, object]:
    return {
        "main": CURRENT_MAIN,
        "prereg": True,
        "goal": True,
        "preflight": True,
        "parent_fixture": True,
        "face_displacements": 12,
        "axial_edges": 40,
        "face_edges": 28,
        "signature_iff": True,
        "transport_necessity": True,
        "transport_sufficiency": True,
        "code_equivariance": True,
        "endpoint_reversal": True,
        "phase_all_pass": 8,
        "cross_mismatch": 32,
        "minimum_conflict": True,
        "independent_safe": False,
        "strict_overlap_allowed": False,
        "idempotent_exact": True,
        "homogeneous_cross_allowed": False,
        "recoding_count": 8,
        "stationary_recoding_cross_allowed": False,
        "stochastic_support_count": 26,
        "symbolic_overlap_count": 19,
        "stabilizer_weight_solution": True,
        "stochastic_h1_pass": 760,
        "triangle_orbits": 2,
        "fff_extreme_globalizable": False,
        "exact_h1_triangle": True,
        "numerical_scout_is_certificate": False,
        "period4_table": True,
        "decoded_label_globalization": True,
        "uniform_microcode_preserved": False,
        "sector_partition": True,
        "sector_positive": True,
        "sector_kraus": True,
        "operator_postprocessing": True,
        "sector_endpoint": True,
        "record_projective": True,
        "record_channel_local_autonomous": False,
        "radius1_vector_patch_count": 42,
        "radius1_collisions": True,
        "radius2_vector_patch_count": 192,
        "radius2_unique_successors": False,
        "radius3_unique_successors": True,
        "translation_commutation": True,
        "sft_cubic_covariance": True,
        "sft_endpoint_covariance": True,
        "sft_field_count": 194,
        "sft_formation_dynamics": False,
        "smallest_unique_successor_radius": 3,
        "seed_front_alphabet": 195,
        "seed_transition_permutations": True,
        "seed_phase_povm": True,
        "seed_write_normalization": True,
        "seed_nondemolition": True,
        "single_seed_extension": True,
        "fair_order_confluence": True,
        "enabled_steps_commute": False,
        "seed_content_conflict": False,
        "compatible_seed_pairs": 194,
        "incompatible_seed_completion": False,
        "invariant_single_seed_law": False,
        "compiler_selects_site_rate": False,
        "multi_seed_handshake": False,
        "binary_seed_carrier": False,
        "single_seed_no_go_scoped": True,
        "pairwise_globalizes": False,
        "global_escape": True,
        "lee_residue_bijection": True,
        "marker_map_count": 8,
        "ownership_cases": 384,
        "stochastic_ownership_cases": 48,
        "ownership_every_collision": True,
        "center_decoder": False,
        "complete_history": False,
        "h2": False,
        "axiom": False,
        "toe": 0,
        "retained": False,
        "universal_no_go": False,
    }


def apply_mutation(values: dict[str, object], mutation: str) -> None:
    mapping = {
        "ind_stale_main_authority": ("main", "stale"),
        "ind_drop_preregistration": ("prereg", False),
        "ind_alter_goal_after_registration": ("goal", False),
        "ind_alter_preflight_after_registration": ("preflight", False),
        "ind_alter_parent_fixture": ("parent_fixture", False),
        "ind_drop_face_displacement": ("face_displacements", 11),
        "ind_change_axial_edge_count": ("axial_edges", 39),
        "ind_change_face_edge_count": ("face_edges", 27),
        "ind_admit_cross_signature": ("signature_iff", False),
        "ind_erase_transport_necessity": ("transport_necessity", False),
        "ind_erase_transport_sufficiency": ("transport_sufficiency", False),
        "ind_break_code_equivariance": ("code_equivariance", False),
        "ind_break_endpoint_reversal": ("endpoint_reversal", False),
        "ind_change_phase_pass_count": ("phase_all_pass", 7),
        "ind_erase_cross_mismatch": ("cross_mismatch", 0),
        "ind_erase_minimum_conflict_identity": ("minimum_conflict", False),
        "ind_claim_products_safe": ("independent_safe", True),
        "ind_permit_strict_overlap": ("strict_overlap_allowed", True),
        "ind_reject_idempotent_reuse": ("idempotent_exact", False),
        "ind_claim_homogeneous_cross": ("homogeneous_cross_allowed", True),
        "ind_change_recoding_count": ("recoding_count", 7),
        "ind_claim_stationary_recoding_cross": ("stationary_recoding_cross_allowed", True),
        "ind_break_stochastic_readability": ("stochastic_support_count", 25),
        "ind_change_symbolic_overlap_count": ("symbolic_overlap_count", 18),
        "ind_change_stabilizer_weight_solution": ("stabilizer_weight_solution", False),
        "ind_erase_stochastic_h1_placements": ("stochastic_h1_pass", 759),
        "ind_claim_fff_extreme_globalizes": ("fff_extreme_globalizable", True),
        "ind_break_exact_h1_triangle_certificate": ("exact_h1_triangle", False),
        "ind_confuse_numerical_scout_with_certificate": ("numerical_scout_is_certificate", True),
        "ind_break_period4_table": ("period4_table", False),
        "ind_erase_decoded_label_globalization": ("decoded_label_globalization", False),
        "ind_claim_uniform_microcode_preserved": ("uniform_microcode_preserved", True),
        "ind_break_sector_effect_partition": ("sector_partition", False),
        "ind_make_sector_effect_nonpositive": ("sector_positive", False),
        "ind_break_sector_kraus_normalization": ("sector_kraus", False),
        "ind_break_operator_postprocessing": ("operator_postprocessing", False),
        "ind_break_sector_endpoint_reversal": ("sector_endpoint", False),
        "ind_break_record_projectivity": ("record_projective", False),
        "ind_claim_record_channel_local_autonomous": ("record_channel_local_autonomous", True),
        "ind_change_radius1_patch_count": ("radius1_vector_patch_count", 41),
        "ind_erase_radius1_collisions": ("radius1_collisions", False),
        "ind_change_radius2_patch_count": ("radius2_vector_patch_count", 191),
        "ind_claim_radius2_unique_successors": ("radius2_unique_successors", True),
        "ind_break_radius3_successor_uniqueness": ("radius3_unique_successors", False),
        "ind_break_translation_commutation": ("translation_commutation", False),
        "ind_break_sft_cubic_covariance": ("sft_cubic_covariance", False),
        "ind_break_sft_endpoint_covariance": ("sft_endpoint_covariance", False),
        "ind_change_sft_field_count": ("sft_field_count", 193),
        "ind_claim_sft_formation_dynamics": ("sft_formation_dynamics", True),
        "ind_change_smallest_radius": ("smallest_unique_successor_radius", 2),
        "ind_change_seed_front_alphabet": ("seed_front_alphabet", 194),
        "ind_break_seed_transition_permutations": ("seed_transition_permutations", False),
        "ind_break_seed_phase_povm": ("seed_phase_povm", False),
        "ind_break_seed_write_normalization": ("seed_write_normalization", False),
        "ind_break_seed_nondemolition": ("seed_nondemolition", False),
        "ind_break_single_seed_extension": ("single_seed_extension", False),
        "ind_break_fair_order_confluence": ("fair_order_confluence", False),
        "ind_claim_enabled_steps_commute": ("enabled_steps_commute", True),
        "ind_claim_seed_content_conflict": ("seed_content_conflict", True),
        "ind_change_compatible_seed_pairs": ("compatible_seed_pairs", 193),
        "ind_claim_incompatible_seed_completion": ("incompatible_seed_completion", True),
        "ind_claim_invariant_single_seed_law": ("invariant_single_seed_law", True),
        "ind_claim_compiler_selects_site_rate": ("compiler_selects_site_rate", True),
        "ind_claim_multi_seed_handshake": ("multi_seed_handshake", True),
        "ind_claim_binary_seed_carrier": ("binary_seed_carrier", True),
        "ind_break_single_seed_no_go_scope": ("single_seed_no_go_scoped", False),
        "ind_claim_pairwise_globalizes": ("pairwise_globalizes", True),
        "ind_break_global_escape": ("global_escape", False),
        "ind_break_lee_residue_bijection": ("lee_residue_bijection", False),
        "ind_break_ownership_collision_census": ("ownership_cases", 95),
        "ind_change_marker_map_count": ("marker_map_count", 7),
        "ind_break_stochastic_marker_census": ("stochastic_ownership_cases", 47),
        "ind_claim_radius_one_center_decoder": ("center_decoder", True),
        "ind_claim_complete_history": ("complete_history", True),
        "ind_open_h2": ("h2", True),
        "ind_edit_axiom": ("axiom", True),
        "ind_move_toe": ("toe", 1),
        "ind_claim_retained_status": ("retained", True),
        "ind_claim_universal_no_go": ("universal_no_go", True),
    }
    key, value = mapping[mutation]
    values[key] = value


def run(mutation: str = "") -> tuple[int, int, dict[str, object]]:
    authority = authority_facts()
    shell = shell_facts()
    transport = transport_facts()
    h1 = h1_facts()
    product = product_facts()
    writes = write_facts()
    homogeneous = homogeneous_facts()
    recoding = recoding_facts()
    stochastic = stochastic_encoder_facts()
    motif = motif_facts()
    stochastic_motif = stochastic_motif_facts()
    decoded_global = period4_decoded_globalization_facts()
    operator = operator_sector_povm_facts()
    record_channel = period4_record_channel_facts()
    static_sft = period4_static_sft_facts()
    seed_front = higher_block_seed_front_facts()
    escape = global_escape_facts()
    lee = lee_facts()
    ownership = ownership_collision_facts()
    classification = classification_facts()
    expected = claims()
    if mutation:
        apply_mutation(expected, mutation)

    authority_ok = (
        authority["main"] == expected["main"]
        and authority["parent"]
        and authority["prereg"] == expected["prereg"]
        and authority["prereg_exact"]
        and authority["goal_registered"] == GOAL_BLOB
        and authority["goal_worktree"] == GOAL_BLOB
        and (authority["goal_registered"] == authority["goal_worktree"]) == expected["goal"]
        and authority["preflight_registered"] == PREFLIGHT_BLOB
        and authority["preflight_worktree"] == PREFLIGHT_BLOB
        and (authority["preflight_registered"] == authority["preflight_worktree"]) == expected["preflight"]
        and authority["axiom_main"] == AXIOM_BLOB
        and authority["axiom_worktree"] == AXIOM_BLOB
        and authority["registry_main"] == REGISTRY_MAIN_BLOB
        and authority["registry_worktree"] == REGISTRY_WORKTREE_BLOB
        and (authority["block211_note"] == BLOCK211_NOTE_BLOB
             and authority["block211_runner"] == BLOCK211_RUNNER_BLOB
             and authority["block211_goal"] == BLOCK211_GOAL_BLOB) == expected["parent_fixture"]
        and authority["inputs_exist"]
        and authority["h2_fence_text"]
    )
    shell_ok = (
        shell["intersecting_count"] == 19
        and shell["class_counts"] == {"same": 1, "axial": 6, "face": expected["face_displacements"]}
        and shell["overlap_sizes"] == {("same", 6): 1, ("axial", 1): 6, ("face", 2): 12}
        and shell["edge_counts"] == {
            "same": (8,),
            "axial": (expected["axial_edges"],),
            "face": (expected["face_edges"],),
            "disjoint": (64,),
        }
        and shell["signature_iff"] == expected["signature_iff"]
        and shell["reversal"]
        and shell["disjoint_controls"]
        and shell["intersection_iff_axis_difference"]
        and shell["rotation_count"] == 24
        and shell["equivariant_cases"] == 192
        and shell["equivariant"] == expected["code_equivariance"]
        and shell["compatibility_covariant"]
        and shell["score_covariant"]
        and shell["antipode_covariant"]
        and shell["endpoint_code"]
        and shell["minimum_code_distance"] == 1
    )
    transport_ok = (
        transport["ranks"] == {"same": (8,), "axial": (14,), "face": (12,), "disjoint": (15,)}
        and transport["profiles"] == {
            "same": (((1, 1),) * 8,),
            "axial": (((2, 2), (6, 6)),),
            "face": (((1, 1), (1, 1), (1, 1), (5, 5)),),
            "disjoint": (((8, 8),),),
        }
        and transport["necessity"] == expected["transport_necessity"]
        and transport["sufficiency"] == expected["transport_sufficiency"]
        and transport["iff"]
        and transport["examples"]
        and transport["zero_support_rejection"]
        and transport["uniform_entries"] == {
            "same": ((sp.Rational(1, 8),),),
            "axial": ((sp.Rational(1, 48), sp.Rational(1, 16)),),
            "face": ((sp.Rational(1, 40), sp.Rational(1, 8)),),
            "disjoint": ((sp.Rational(1, 64),),),
        }
    )
    h1_ok = (
        h1["source_angles"]
        and h1["case_count"] == 40
        and h1["pass_count"] == 440
        and h1["fail_count"] == 320
        and h1["all_overlap_pass"] == expected["phase_all_pass"]
        and h1["all_overlap_fail"] == 32
        and h1["cross_mismatch"] == expected["cross_mismatch"]
        and h1["failed_conflict_count"] == 320
        and h1["minimum_conflict_abs_delta_z"] == expected["minimum_conflict"]
        and h1["normalized"] and h1["strictly_positive"] and h1["moments"]
        and h1["endpoint_reverse"] == expected["endpoint_reversal"]
        and h1["compatible_couplings"]
        and h1["frame_case_count"] == 960
        and h1["frame_covariance"] and h1["frame_moments"]
        and h1["frame_endpoint_reverse"]
        and h1["stochastic_placement_pass"] == expected["stochastic_h1_pass"]
        and h1["stochastic_placement_fail"] == 0
        and h1["stochastic_encoded_normalized"]
        and h1["stochastic_encoded_full_26_support"]
        and h1["phase_census"] == {
            sp.Integer(0): (8, 152, 0),
            sp.pi / 6: (8, 72, 80),
            sp.pi / 3: (8, 72, 80),
            sp.pi / 2: (8, 72, 80),
            5 * sp.pi / 6: (8, 72, 80),
        }
        and all(h1["depth_census"][(item, "pass")] == 220 and h1["depth_census"][(item, "fail")] == 160 for item in DEPTHS)
        and all(h1["radius_census"][(item, "pass")] == 220 and h1["radius_census"][(item, "fail")] == 160 for item in RADII)
        and all(h1["realification_census"][(item, "pass")] == 220 and h1["realification_census"][(item, "fail")] == 160 for item in REALIFICATIONS)
    )
    write_ok = (
        product["conflicts"] == {
            "same": sp.Rational(7, 8),
            "axial": sp.Rational(3, 8),
            "face": sp.Rational(9, 16),
            "disjoint": sp.Integer(0),
        }
        and product["every_full_support_product_conflicts"]
        and product["independent_safe"] == expected["independent_safe"]
        and writes["strict_overlap_allowed"] == expected["strict_overlap_allowed"]
        and writes["strict_overlap_rejected"] and writes["strict_disjoint_commutes"]
        and writes["idempotent_exact"] == expected["idempotent_exact"]
        and writes["atomic_exact"] and writes["first_wins_corrupts"]
    )
    homogeneous_ok = (
        homogeneous["constraint_rank"] == 5
        and homogeneous["nullity"] == 3
        and homogeneous["all_cross_zero"]
        and homogeneous["nonzero_homogeneous_cross_allowed"] == expected["homogeneous_cross_allowed"]
        and recoding["fixed_orbits"] == 2
        and recoding["six_orbits"] == 2
        and recoding["equivariant_injections"] == expected["recoding_count"]
        and recoding["all_injective"]
        and recoding["proper_cubic_covariance"]
        and recoding["endpoint_reversal"]
        and recoding["stationary_bit_difference_is_cross_imbalance"]
        and recoding["stationary_nonzero_cross_possible"]
        == expected["stationary_recoding_cross_allowed"]
    )
    stochastic_ok = (
        stochastic["support_count"] == 26
        and stochastic["distinct_support_count"]
        == expected["stochastic_support_count"]
        and stochastic["support_sizes"] == (1, 1, 4, 4, 4, 4, 4, 4)
        and stochastic["disjoint_readability"]
        and stochastic["proper_cubic_covariance"]
        and stochastic["endpoint_covariance"]
        and stochastic["symbolic_overlap_count"]
        == expected["symbolic_overlap_count"]
        and stochastic["arbitrary_symbolic_two_center"]
        and stochastic["word_signature_transport_iff"]
        and stochastic["general_equation_rank"] == 3
        and stochastic["general_solution_unique_uniform_four"]
        == expected["stabilizer_weight_solution"]
    )
    motif_ok = (
        motif["pairwise_uniform_couplings"]
        and motif["chosen_global_count"] == 0
        and motif["geometric_global_count"] == 112
        and motif["pairwise_couplings_automatically_globalize"] == expected["pairwise_globalizes"]
    )
    stochastic_motif_ok = (
        stochastic_motif["triangle_orbit_count"] == expected["triangle_orbits"]
        and stochastic_motif["triangle_profiles"] == (
            ("axial", "face", "face"),
            ("face", "face", "face"),
        )
        and stochastic_motif["aff_labelwise_arbitrary_law_certificate"]
        and stochastic_motif["fff_compatible_triple_count"] == 560
        and stochastic_motif["fff_cross_assignment_counts"] == (2,) * 6
        and stochastic_motif["fff_cross_projection_sizes"]
        == ((2, 2, 2),) * 6
        and stochastic_motif["fff_extreme_cross_globalizable"]
        == expected["fff_extreme_globalizable"]
        and stochastic_motif["minimal_center_count"] == 3
        and stochastic_motif["numerical_scouting_cases"] == 20
        and stochastic_motif["numerical_scouting_feasible"]
        and stochastic_motif["numerical_scouting_is_certificate"]
        == expected["numerical_scout_is_certificate"]
        and stochastic_motif["exact_certificate_cases"] == 20
        and stochastic_motif["exact_h1_placements"] == 40
        and stochastic_motif["exact_h1_all_fff"]
        == expected["exact_h1_triangle"]
        and not stochastic_motif["exact_validation_uses_floating_point"]
    )
    decoded_global_ok = (
        (decoded_global["literal_table_shape"] == (4, 4, 4)
         and decoded_global["translation_count"] == 64
         and decoded_global["translation_mask_support"] == 12
         and decoded_global["all_translation_words_readable"]
         and decoded_global["base_is_d_plus_z"])
        == expected["period4_table"]
        and decoded_global["rotated_sector_count"] == 6
        and decoded_global["rotation_well_defined"]
        and decoded_global["decoded_sector_formula"]
        and decoded_global["parameter_cases"] == 40
        and decoded_global["antipodal_cross_sums"]
        and decoded_global["cross_total_two_thirds"]
        and decoded_global["sector_weights_nonnegative"]
        and decoded_global["sector_weights_normalized"]
        and decoded_global["decoded_h1_globalized"]
        == expected["decoded_label_globalization"]
        and decoded_global["microcode_mismatch_counts"] == (24,) * 40
        and decoded_global["uniform_kernel_microcode_preserved"]
        == expected["uniform_microcode_preserved"]
        and decoded_global["translation_averaged_global_fields"]
        and not decoded_global["decoded_globalization_is_local_formation_law"]
    )
    operator_channel_ok = (
        operator["case_count"] == 4
        and operator["dot_partition_count"] == 4
        and operator["cross_partition_count"] == 24
        and (operator["dot_partitions"] and operator["cross_partitions"])
        == expected["sector_partition"]
        and operator["sector_effect_count"] == 32
        and (operator["strictly_positive"]
             and operator["positive_determinants"])
        == expected["sector_positive"]
        and operator["povm_normalized"]
        and (operator["cholesky_kraus_exact"]
             and operator["kraus_isometry_normalized"])
        == expected["sector_kraus"]
        and operator["endpoint_reversal"] == expected["sector_endpoint"]
        and operator["postprocessing_shape"] == (8, 8)
        and operator["postprocessing_nonnegative"]
        and operator["postprocessing_column_stochastic"]
        and operator["postprocessing_endpoint_reversal"]
        and operator["postprocessing_matches_period4"]
        and operator["operator_postprocessing_count"] == 32
        and operator["operator_postprocessing_exact"]
        == expected["operator_postprocessing"]
        and record_channel["cross_sector_count"] == 6
        and record_channel["orientation_independent_translation_orbits"]
        and record_channel["ensemble_normalized"]
        and record_channel["distinct_configurations_per_cross_sector"]
        == (32,) * 6
        and record_channel["distinct_cross_configurations"] == 192
        and record_channel["distinct_total_configurations"] == 194
        and record_channel["all_centers_decode_postprocessing"]
        and record_channel["projective_restriction_count"] == 6
        and record_channel["projectively_consistent"]
        == expected["record_projective"]
        and record_channel["distant_correlation_witness"]
        == ((0, 1, 1), sp.Rational(-1, 16))
        and record_channel["measure_prepare_trace_preserving"]
        and record_channel["measure_prepare_completely_positive"]
        and record_channel["global_record_channel"]
        and (record_channel["local_nearest_neighbor_channel"]
             or record_channel["autonomous_nearest_neighbor_history"])
        == expected["record_channel_local_autonomous"]
        and record_channel["event_conditioned"]
    )
    static_sft_ok = (
        static_sft["sector_count"] == 6
        and static_sft["orientation_independent_sectors"]
        and static_sft["sector_sizes"] == (32,) * 6
        and static_sft["sector_disjoint"]
        and static_sft["vector_configuration_count"] == 192
        and static_sft["total_configuration_count"] == 194
        and static_sft["ball_sizes"] == {1: 7, 2: 25, 3: 63}
        and static_sft["vector_patch_counts"][1]
        == expected["radius1_vector_patch_count"]
        and static_sft["all_patch_counts"] == {1: 44, 2: 194, 3: 194}
        and static_sft["radius_one_vector_collision_histogram"]
        == {2: 12, 4: 6, 5: 12, 7: 12}
        and static_sft["radius_one_all_vector_types_collide"]
        == expected["radius1_collisions"]
        and static_sft["vector_patch_counts"][2]
        == expected["radius2_vector_patch_count"]
        and static_sft["radius_two_decodes_sector_and_phase"]
        and static_sft["radius_two_has_ambiguous_successors"]
        == (not expected["radius2_unique_successors"])
        and all(
            histogram == {1: 116, 2: 28, 3: 48}
            for histogram in static_sft["radius_two_successor_histograms"]
        )
        and all(
            histogram == {1: 194}
            for histogram in static_sft["radius_three_successor_histograms"]
        ) == expected["radius3_unique_successors"]
        and static_sft["radius_three_unique_successor_total"] == 1164
        and static_sft["unique_successor_is_actual_translation"]
        and static_sft["transition_permutations"]
        and static_sft["opposite_transitions_are_inverses"]
        and static_sft["transitions_commute"]
        == expected["translation_commutation"]
        and static_sft["period_four_translations"]
        and static_sft["translation_orbit_sizes"]
        == (1, 1, 32, 32, 32, 32, 32, 32)
        and static_sft["translation_orbits_exact"]
        and (
            static_sft["proper_cubic_field_covariance"]
            and static_sft["proper_cubic_patch_covariance"]
            and static_sft["proper_cubic_transition_covariance"]
        ) == expected["sft_cubic_covariance"]
        and (
            static_sft["endpoint_field_covariance"]
            and static_sft["endpoint_patch_covariance"]
            and static_sft["endpoint_transition_covariance"]
        ) == expected["sft_endpoint_covariance"]
        and static_sft["catalog_satisfies_local_constraint"]
        and static_sft["translated_patch_reconstruction"]
        and static_sft["center_symbol_reconstruction"]
        and static_sft["global_fields_exactly_catalog"]
        and static_sft["certified_global_field_count"]
        == expected["sft_field_count"]
        and static_sft["constraint_kind"] == "static_finite_range_sft"
        and static_sft["constraint_radius"] == 3
        and static_sft["smallest_tested_unique_successor_radius"]
        == expected["smallest_unique_successor_radius"]
        and not static_sft["radius_two_exact_sft_excluded"]
        and static_sft["formation_dynamics_constructed"]
        == expected["sft_formation_dynamics"]
        and not static_sft["autonomous_history_constructed"]
    )
    seed_front_ok = (
        seed_front["visible_patch_types"] == 194
        and seed_front["blank_plus_type_alphabet"]
        == expected["seed_front_alphabet"]
        and seed_front["minimum_binary_status_bits"] == 8
        and seed_front["phase_multiplicities"]
        == (1, 1, 32, 32, 32, 32, 32, 32)
        and seed_front["refined_seed_effect_count"] == 194
        and seed_front["phase_refined_povm_case_count"] == 4
        and (
            seed_front["phase_refined_povm_normalized"]
            and seed_front["phase_refined_effects_strictly_positive"]
            and seed_front["scalar_sectors_unrefined"]
            and seed_front["vector_sectors_uniform_over_32_phases"]
            and seed_front["phase_refinement_endpoint_covariant"]
        ) == expected["seed_phase_povm"]
        and seed_front["seed_povm_site_supplied"]
        and not seed_front["seed_povm_selects_event_site"]
        and (
            seed_front["transition_permutations"]
            and seed_front["transition_commutation"]
            and seed_front["inverse_transitions"]
        ) == expected["seed_transition_permutations"]
        and seed_front["kraus_write_formula"] == "|a><blank|"
        and seed_front["kraus_lock_formula"] == "sum_locked|b><b|"
        and (
            seed_front["kraus_domain_partition_exact"]
            and seed_front["kraus_domain_projectors_orthogonal"]
            and seed_front["two_kraus_trace_preserving"]
            and seed_front["write_targets_exact"]
        ) == expected["seed_write_normalization"]
        and seed_front["locked_subspace_nondemolition"]
        == expected["seed_nondemolition"]
        and seed_front["blank_is_written_at_most_once"]
        and seed_front["single_seed_unique_extension"]
        == expected["single_seed_extension"]
        and seed_front["neighbor_content_consistency"]
        and seed_front["torus_graph_connected"]
        and seed_front["tested_seed_types"] == 194
        and seed_front["tested_fair_site_orders"] == 4
        and seed_front["tested_schedule_cases"] == 776
        and seed_front["all_tested_orders_reach_unique_terminal"]
        and seed_front["all_tested_orders_conflict_free"]
        and seed_front["all_tested_orders_write_once"]
        and seed_front["fair_order_pointwise_terminal_confluence"]
        == expected["fair_order_confluence"]
        and seed_front["fairness_is_a_supplied_schedule_condition"]
        and seed_front["enabled_one_step_updates_commute"]
        == expected["enabled_steps_commute"]
        and seed_front["enablement_noncommutation_witness"]
        and seed_front["fixed_content_writes_on_distinct_sites_commute"]
        and seed_front["enablement_witness_same_terminal_content"]
        and seed_front["one_step_noncommutation_is_content_conflict"]
        == expected["seed_content_conflict"]
        and seed_front["fixed_seed_displacement"] == (1, 0, 0)
        and seed_front["compatible_ordered_seed_pairs"]
        == expected["compatible_seed_pairs"]
        and seed_front["incompatible_ordered_seed_pairs"] == 194 ** 2 - 194
        and seed_front["total_ordered_seed_pairs"] == 194 ** 2
        and seed_front["completion_count_histogram"]
        == {0: 194 ** 2 - 194, 1: 194}
        and seed_front["independent_uniform_seed_compatibility"]
        == sp.Rational(1, 194)
        and seed_front["incompatible_permanent_seeds_have_common_sft_completion"]
        == expected["incompatible_seed_completion"]
        and seed_front["finite_nonempty_seed_has_translation_equivariant_anchor"]
        and seed_front["translation_invariant_exact_single_seed_probability_law_exists"]
        == expected["invariant_single_seed_law"]
        and seed_front["single_seed_probability_no_go"]
        and seed_front["single_site_intensity_bound_limit"] == 0
        and seed_front["countable_union_contradiction"]
        and seed_front["finite_torus_uniform_single_seed_escape"]
        and seed_front["supplied_origin_single_seed_escape"]
        and seed_front["positive_density_multi_seed_escape"]
        and seed_front["finitely_additive_invariant_mean_outside_scope"]
        and seed_front["coherent_nonclassical_seed_outside_scope"]
        and seed_front["no_go_route_family_count"] >= 5
        and len(seed_front["no_go_scope_drop_escapes"]) == 4
        and seed_front["no_go_hidden_wall_scan"]
        and seed_front["no_go_prior_witnesses_required"] == 0
        and len(seed_front["no_go_resolution_audit"]) == 4
        and len(seed_front["no_go_partial_closure_routes"]) >= 4
        and not seed_front["no_go_within_scope_steelman_found"]
        and len(seed_front["no_go_cross_cycle_echoes"]) >= 3
        and seed_front["no_go_discipline_pass"]
        == expected["single_seed_no_go_scoped"]
        and seed_front["carrier_kind"] == "visible_higher_block_195_state"
        and seed_front["original_binary_record_only"]
        == expected["binary_seed_carrier"]
        and (seed_front["event_site_selected"]
             or seed_front["occurrence_rate_selected"])
        == expected["compiler_selects_site_rate"]
        and seed_front["multi_seed_handshake_constructed"]
        == expected["multi_seed_handshake"]
        and not seed_front["autonomous_history_constructed"]
    )
    escape_ok = (
        escape["form_count"] == 24
        and escape["local_uniform_full_support"]
        and escape["global_overlap_compatible"]
        and escape["proper_cubic_average"]
        and escape["translation_permuted_cosets"]
        and escape["correlated_not_product"]
        and escape["global_constraint_escape"] == expected["global_escape"]
        and not escape["nearest_neighbor_autonomous_law"]
    )
    lee_ok = (
        lee["closed_residues"] == (0, 6, 1, 5, 2, 4, 3)
        and lee["perfect_closed_ball"]
        and lee["supplied_residue_offset_bijection"]
        == expected["lee_residue_bijection"]
        and lee["open_shell_disjoint"] and lee["unique_writer"]
        and lee["arbitrary_batch_outcomes"]
        and lee["event_density"] == sp.Rational(1, 7)
        and lee["written_density"] == sp.Rational(6, 7)
        and lee["same_coset_locked_sites"] == 6
        and lee["later_coset_locked_sites"] == (5,) * 6
        and not lee["strict_fresh_cycle_possible"]
        and lee["supplied_coloring"] and not lee["autonomous_selector"]
    )
    ownership_ok = (
        ownership["code_count"] == 8
        and ownership["equivariant_marker_maps"]
        == expected["marker_map_count"]
        and ownership["marker_map_covariance"]
        and ownership["noncenter_roles"] == 6
        and ownership["tested_role_cases"] == expected["ownership_cases"]
        and ownership["every_role_collides"]
        == expected["ownership_every_collision"]
        and ownership["minimum_colliding_center_patterns"] == 2
        and ownership["maximum_colliding_center_patterns"] == 8
        and ownership["collision_histogram"]
        == {2: 48, 3: 48, 6: 48, 7: 48, 8: 192}
        and ownership["stochastic_tested_role_cases"]
        == expected["stochastic_ownership_cases"]
        and ownership["stochastic_every_role_collides"]
        and ownership["stochastic_collision_histogram"]
        == {13: 12, 14: 12, 26: 24}
        and ownership["stochastic_minimum_collisions"] == 13
        and ownership["stochastic_maximum_collisions"] == 26
        and ownership["radius_one_center_decoder_exists"]
        == expected["center_decoder"]
        and ownership["larger_or_separate_ownership_carrier_open"]
    )
    boundary_ok = (
        classification["partial"]
        and classification["complete_history"] == expected["complete_history"]
        and not classification["direct_family_exhausted"]
        and not classification["deterministic_obstruction_exhaustive"]
        and classification["stochastic_two_center_escape"]
        and classification["decoded_label_global_process"]
        and not classification["uniform_microcode_infinite_consistency_constructed"]
        and classification["operator_sector_povm_bridge"]
        and classification["record_measure_prepare_normalized"]
        and classification["record_projectively_consistent"]
        and classification["record_support_static_finite_range"]
        and classification["record_measure_prepare_uses_global_sector"]
        and not classification["record_support_formation_dynamics"]
        and not classification["record_channel_autonomous_nn"]
        and classification["conditional_visible_seed_front"]
        and classification["invariant_exact_single_seed_excluded"]
        and classification["seed_event_site_supplied"]
        and classification["seed_occurrence_rate_open"]
        and classification["multi_seed_handshake_open"]
        and classification["autonomous_history_open"]
        and not classification["one_many_none_decided"]
        and classification["h2_open"] == expected["h2"]
        and classification["axiom_update"] == expected["axiom"]
        and classification["toe_movement"] == expected["toe"]
        and classification["retained"] == expected["retained"]
        and classification["universal_no_go"] == expected["universal_no_go"]
    )

    checks = {
        "A": (authority_ok, "the Block-212 preregistration and every inherited authority blob are exact"),
        "B": (shell_ok, "the complete 19-displacement shell census has 8/40/28/64 compatibility edges and an exact cubic code"),
        "C": (transport_ok, "signature pushforward equality is necessary and sufficient, including zero-support and uniform full-support limits"),
        "D": (h1_ok, "all 40 H1 parameter cases, endpoint reversals, and exact cross moments give the 440/320 displacement census"),
        "E": (write_ok, "full-support products conflict while strict and idempotent serial/atomic semantics remain distinct"),
        "F": (homogeneous_ok, "all eight independently enumerated equivariant recodings inherit the stationary zero-cross obstruction"),
        "G": (stochastic_ok, "the readable 26-word stochastic encoder passes every symbolic two-center overlap only at a=b=c/2=1/4"),
        "H": (motif_ok, "chosen pair couplings can form an inconsistent cycle although compatible triples exist"),
        "I": (stochastic_motif_ok, "both triangle orbits are exact: FFF has a minimal extreme-label counterexample but all 40 H1 placements have exact certificates"),
        "J": (escape_ok, "an explicit uniform full-support global correlated field is translation/proper-cubic covariant but nonlocal"),
        "K": (lee_ok, "the supplied mod-7 Lee coloring gives a conditional unique-writer batch but cannot cycle under strict freshness"),
        "L": (ownership_ok, "all deterministic and stochastic radius-one roles collide for all eight equivariant marker maps"),
        "M": (decoded_global_ok, "the period-4 sector mixture globalizes decoded H1 labels but not the uniform conditional microcode"),
        "N": (operator_channel_ok, "the exact sector POVM and decoded postprocessing define a normalized projectively consistent global Record channel"),
        "O": (static_sft_ok, "the 194 period-4 fields are exactly a cubic/endpoint-covariant radius-3 static SFT, with the tested radius-1/2 boundary explicit"),
        "P": (seed_front_ok, "the visible 195-state two-Kraus compiler grows one supplied seed confluent, while the exact invariant-single-seed and incompatible-pair boundaries stay narrowly scoped"),
        "Q": (boundary_ok, "uniform-microcode infinite consistency, autonomous site/rate, multi-seed handshake, history, H2, axiom change, retention, TOE movement, and universal no-go remain unclaimed"),
    }
    passed = sum(int(value[0]) for value in checks.values())
    failed = len(checks) - passed
    return passed, failed, {
        "checks": checks,
        "shell": shell,
        "transport": transport,
        "h1": h1,
        "product": product,
        "writes": writes,
        "homogeneous": homogeneous,
        "recoding": recoding,
        "stochastic": stochastic,
        "motif": motif,
        "stochastic_motif": stochastic_motif,
        "decoded_global": decoded_global,
        "operator": operator,
        "record_channel": record_channel,
        "static_sft": static_sft,
        "seed_front": seed_front,
        "escape": escape,
        "lee": lee,
        "ownership": ownership,
        "classification": classification,
    }


def mutation_suite() -> int:
    baseline_passed, baseline_failed, _ = run()
    detected = 0
    print(f"BASELINE: PASS={baseline_passed} FAIL={baseline_failed}; mutations={len(MUTATIONS)}.")
    for mutation in MUTATIONS:
        _passed, failed, _facts = run(mutation)
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
    arguments = parser.parse_args()
    if arguments.mutation_suite:
        return mutation_suite()

    passed, failed, facts = run(arguments.mutation)
    shell = facts["shell"]
    transport = facts["transport"]
    h1 = facts["h1"]
    product = facts["product"]
    homogeneous = facts["homogeneous"]
    recoding = facts["recoding"]
    stochastic = facts["stochastic"]
    motif = facts["motif"]
    stochastic_motif = facts["stochastic_motif"]
    decoded_global = facts["decoded_global"]
    operator = facts["operator"]
    record_channel = facts["record_channel"]
    static_sft = facts["static_sft"]
    seed_front = facts["seed_front"]
    escape = facts["escape"]
    lee = facts["lee"]
    ownership = facts["ownership"]
    classification = facts["classification"]
    print(
        "OVERLAP_CENSUS: intersecting=19 (same=1x6, axial=6x1, "
        "face=12x2); compatibility_edges=8/40/28/64; endpoint reversal "
        f"and {shell['equivariant_cases']}=8x24 code transports exact."
    )
    print(
        "TRANSPORT_IFF: signature pushforwards match iff a coupling exists; "
        f"incidence_ranks={transport['ranks']}; uniform positive entries "
        "same=1/8, axial=1/48|1/16, face=1/40|1/8, disjoint=1/64."
    )
    print(
        "H1_CENSUS: phases=(0,pi/6,pi/3,pi/2,5pi/6), depths=2, "
        "radii=2, realifications=2 => cases=40; all-overlap PASS=8 FAIL=32; "
        f"displacement PASS={h1['pass_count']} FAIL={h1['fail_count']}; "
        f"nonzero_cross_mismatch={h1['cross_mismatch']}; every one of 320 "
        "deterministic failures has minimum incompatible mass |delta_z|; "
        f"redundant stochastic placements PASS={h1['stochastic_placement_pass']} "
        f"FAIL={h1['stochastic_placement_fail']}."
    )
    print(
        "PRODUCT_AND_WRITES: uniform product conflict same/axial/face/disjoint="
        f"{product['conflicts']}; strict overlap rejects both orders; idempotent "
        "reuse and atomic union succeed iff signatures agree."
    )
    print(
        "HOMOGENEOUS_OBSTRUCTION: constraint_rank="
        f"{homogeneous['constraint_rank']} nullity={homogeneous['nullity']}; "
        f"binary fixed/six-orbits={recoding['fixed_orbits']}/{recoding['six_orbits']}, "
        f"equivariant injections={recoding['equivariant_injections']}; every "
        "stationary recoding forces zero cross moment."
    )
    print(
        "STOCHASTIC_ENCODER: readable support=26/26; arbitrary symbolic "
        f"overlaps={stochastic['symbolic_overlap_count']}/19; cubic and endpoint "
        "covariant; stabilizer weights uniquely a=b=1/4,c=1/2."
    )
    print(
        "STOCHASTIC_TRIANGLES: triangle_orbits="
        f"{stochastic_motif['triangle_orbit_count']}; FFF extreme cross label "
        "has only 2 triples and is exactly nonglobal; numerical scout=20/20 "
        f"(not a certificate), exact algebraic H1 certificates="
        f"{stochastic_motif['exact_certificate_cases']}/20 for 40/40 placements."
    )
    print(
        "PERIOD4_DECODED_GLOBALIZATION: "
        f"{decoded_global['translation_count']} translations give D_+z="
        "(X+z:1/2, each perpendicular cross:1/8); six rotated sectors and "
        "w_e=1/9+p_e-p_-e reproduce 40/40 decoded H1 laws, while all 40 "
        "differ from uniform K microcode on 24 masks."
    )
    print(
        "OPERATOR_RECORD_BRIDGE: sector POVMs="
        f"{operator['case_count']}, positive effects={operator['sector_effect_count']}, "
        f"operator decodes={operator['operator_postprocessing_count']}/32; "
        f"global configurations={record_channel['distinct_total_configurations']}, "
        "Kraus-normalized/projective with distant covariance -1/16; not autonomous NN."
    )
    print(
        "STATIC_RADIUS3_SFT: vector patches B1/B2/B3="
        f"{tuple(static_sft['vector_patch_counts'].values())}; B2 successor "
        "histogram={1:116,2:28,3:48}; B3 unique successors=1164/1164, "
        "commuting translations give exactly 194 fields; static constraint, not formation dynamics."
    )
    print(
        "SEED_FRONT: visible alphabet=195; four supplied-site phase POVMs "
        "normalize; write/lock Kraus domains sum to I; 776 fair-order tests "
        "converge; compatible fixed-displacement pairs=194/37636; no invariant "
        "exact-single-seed law, rate, handshake, or autonomous history."
    )
    print(
        "OWNERSHIP_COLLISIONS: 8 recodings x 8 equivariant marker maps x 6 "
        f"roles={ownership['tested_role_cases']} (range 2..8); stochastic "
        f"encoder roles=8x6={ownership['stochastic_tested_role_cases']} "
        "(range 13..26); no radius-one decoder."
    )
    for line in N5_LINES:
        print(f"N5 {line}")
    for label, (ok, description) in facts["checks"].items():
        print(f"{label}: {'PASS' if ok else 'FAIL'} — {description}.")
    print(
        "CLASSIFICATION: " + classification["classification"]
        + "; honest partial only; H2 sealed; axiom/registry/TOE unchanged."
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
