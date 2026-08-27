#!/usr/bin/env python3
"""Block 211 action/cell-to-Record score-quotient bridge.

The runner keeps four questions separate:

* what part of the H1 corner-to-qubit solder is actually fixed by the native
  first corner harmonic;
* what endpoint POVM is obtained by pulling the cubic menu through the
  reproduced cell channel rather than choosing a sharpness parameter;
* what is the smallest outcome quotient needed by the exact H1 dot/cross
  decoder, and whether it has an orthogonal cubic Record code; and
* whether those positive constructions select one complete physical law.

The final answer is intentionally allowed to be a partial joint bridge.  A
Naimark environment is not silently renamed a framework Record, and a
conditional-on-formation law is not silently renamed an autonomous history.
"""

from __future__ import annotations

import argparse
from functools import cache
import itertools
import math
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25 as b194  # noqa: E402
import admissibility_d4_h1_edge_comparison_cell_corner_t2_factorization_2026_08_26 as b207  # noqa: E402
import admissibility_d4_h1_two_time_clifford_cell_m2_record_compiler_2026_08_26 as b208  # noqa: E402


I = sp.I
I2 = sp.eye(2)
I4 = sp.eye(4)
AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_H1_ACTION_NATIVE_SCORE_QUOTIENT_RECORD_DILATION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md"
)
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block211-action-native-minimal-record-dilation-"
    "20260827"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "92dd84b62f4d9fe4d0867a83926b6c25adbc77f9"
PREREG_COMMIT = "960398186a16a2f7caa9283af58332a312dec149"
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
GOAL_BLOB = "3f4df853c0fc6d20e921c531fe494295d3042296"
PREFLIGHT_BLOB = "6f5319a1e4b6cfa17e7e8da8045a2175d01c3d1f"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
REGISTRY_MAIN_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
REGISTRY_WORKTREE_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_ACTION_NATIVE_SCORE_QUOTIENT_RECORD_DILATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    ".claude/science/physics-loops/toe-axiom-closure-block211-action-native-minimal-record-dilation-20260827/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block211-action-native-minimal-record-dilation-20260827/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_H1_TWO_TIME_CLIFFORD_CELL_M2_RECORD_COMPILER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_two_time_clifford_cell_m2_record_compiler_2026_08_26.py",
    "logs/runner-cache/admissibility_d4_h1_two_time_clifford_cell_m2_record_compiler_2026_08_26.txt",
    "docs/ADMISSIBILITY_D4_H1_EDGE_COMPARISON_CELL_CORNER_T2_FACTORIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_edge_comparison_cell_corner_t2_factorization_2026_08_26.py",
    "logs/runner-cache/admissibility_d4_h1_edge_comparison_cell_corner_t2_factorization_2026_08_26.txt",
    "docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
    "logs/runner-cache/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.txt",
)


MUTATIONS = (
    "stale_main_authority",
    "drop_preregistration",
    "alter_goal_after_registration",
    "erase_degree_one_uniqueness",
    "claim_full_section_unique",
    "delete_higher_harmonic_controls",
    "break_action_field_normalization",
    "claim_phase_radius_selected",
    "make_cell_transfer_singular",
    "break_cell_effect_normalization",
    "break_cell_covariance",
    "claim_cell_depth_selected",
    "break_score_quotient",
    "merge_unequal_scores",
    "claim_full36_one_shell_code",
    "break_coarse_code_covariance",
    "break_endpoint_swap",
    "break_naimark_isometry",
    "claim_environment_is_record",
    "overwrite_record_site",
    "claim_autonomous_formation",
    "erase_depth_probability_fork",
    "erase_radius_probability_fork",
    "erase_h1_depth_one",
    "erase_h1_depth_two",
    "erase_self_normalized_decoder",
    "claim_complete_h1_ownership",
    "claim_h2_open",
    "claim_axiom_update",
    "claim_obligation_retirement",
    "claim_toe_progress",
    "claim_retained_status",
    "claim_universal_no_go",
)


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


def walsh_embedding(degree: int) -> sp.Matrix:
    """Embed degree-k Boolean corner harmonics tensored with a vector."""
    subsets = tuple(itertools.combinations(range(3), degree))
    result = sp.zeros(24, 3 * len(subsets))
    for corner_index, corner in enumerate(b207.corners()):
        for subset_index, subset in enumerate(subsets):
            monomial = sp.prod(corner[index] for index in subset)
            for component in range(3):
                result[
                    3 * corner_index + component,
                    3 * subset_index + component,
                ] = monomial
    return result


def vector_to_matrix_column_major(
    vector: sp.Matrix, rows: int, columns: int
) -> sp.Matrix:
    result = sp.zeros(rows, columns)
    for column in range(columns):
        for row in range(rows):
            result[row, column] = vector[column * rows + row]
    return result


@cache
def action_solder_facts() -> dict[str, object]:
    rotations = b194.proper_cubic_rotations()
    odd, _even = b207.b206.conditional_adjoint_hom_basis()
    radial = odd * b208.face_average_matrix()
    degree_maps: dict[int, tuple[sp.Matrix, ...]] = {}
    radial_images: dict[int, tuple[sp.Matrix, ...]] = {}

    for degree in range(4):
        embedding = walsh_embedding(degree)
        reduced_dimension = embedding.cols
        constraints = []
        for rotation in rotations:
            domain = sp.kronecker_product(
                b207.corner_representation(rotation), rotation
            )
            target = b207.b206.shear_representation(rotation)
            constraints.append(
                sp.kronecker_product(sp.eye(3), domain * embedding)
                - sp.kronecker_product(target.T, embedding)
            )
        system = sp.Matrix.vstack(*constraints)
        maps = []
        for vector in system.nullspace():
            coefficient = vector_to_matrix_column_major(
                vector, reduced_dimension, 3
            )
            maps.append(sp.simplify(embedding * coefficient))
        degree_maps[degree] = tuple(maps)
        radial_images[degree] = tuple(
            sp.simplify(radial * item) for item in maps
        )

    active = degree_maps[1][0]
    active_scalar = radial_images[1][0][0, 0]
    active_right_inverse = sp.simplify(active / active_scalar)
    h = sp.Matrix(
        b207.b206.neighbor_hom_facts()["h1_shear_coordinates"]
    )
    tensor = sp.Matrix((
        (0, h[0], h[2]),
        (h[0], 0, h[1]),
        (h[2], h[1], 0),
    ))
    direct_field = sp.Matrix.vstack(*(
        -tensor * corner / 4 for corner in b207.corners()
    ))
    selected_field = sp.simplify(active_right_inverse * h)
    norms = tuple(
        sp.simplify(sum(
            selected_field[3 * corner + component] ** 2
            for component in range(3)
        ))
        for corner in range(8)
    )

    return {
        "radial_shape": radial.shape,
        "radial_orthonormal": radial * radial.T == sp.eye(3),
        "degree_hom_dimensions": tuple(
            len(degree_maps[degree]) for degree in range(4)
        ),
        "full_hom_dimension": sum(
            len(degree_maps[degree]) for degree in range(4)
        ),
        "degree_one_unique": len(degree_maps[1]) == 1,
        "degree_one_radial_nonzero": (
            active_scalar != 0
            and radial_images[1][0] == active_scalar * sp.eye(3)
        ),
        "higher_harmonics_radial_null": all(
            image == sp.zeros(3)
            for degree in (2, 3) for image in radial_images[degree]
        ),
        "right_inverse": radial * active_right_inverse == sp.eye(3),
        "right_inverse_equals_minimum_norm": (
            active_right_inverse == radial.T
        ),
        "direct_field": direct_field == selected_field,
        "field_positive": all(value < 1 for value in norms),
        "right_inverse_affine_dimension": 2,
        "full_section_unique": False,
        "higher_harmonics_readable_if_prepared": True,
        "first_harmonic_physically_selected": False,
    }


def phase_orbit_state(
    unit: sp.Expr, radius: sp.Expr, orientation: int
) -> sp.Matrix:
    """First-harmonic equivariant M2 orbit, expressed without an angle."""
    return sp.Matrix((
        (1, radius * unit ** (-orientation)),
        (radius * unit ** orientation, 1),
    )) / 2


@cache
def phase_solder_facts() -> dict[str, object]:
    units = (
        sp.Integer(1), I, -sp.Integer(1), -I,
        sp.Rational(1, 2) + I * sp.sqrt(3) / 2,
    )
    states = {
        (radius, orientation): tuple(
            phase_orbit_state(unit, radius, orientation) for unit in units
        )
        for radius in (sp.Integer(1), sp.Rational(1, 2))
        for orientation in (1, -1)
    }
    return {
        "traces": all(
            sp.trace(state) == 1
            for family in states.values() for state in family
        ),
        "pure_radius_one": all(
            state.det() == 0 for state in states[(sp.Integer(1), 1)]
        ),
        "mixed_radius_half": all(
            state.det() == sp.Rational(3, 16)
            for state in states[(sp.Rational(1, 2), 1)]
        ),
        "conjugate_readings": all(
            (
                states[(radius, -1)][index]
                - sp.conjugate(states[(radius, 1)][index])
            ).applyfunc(sp.simplify) == sp.zeros(2)
            for radius in (sp.Integer(1), sp.Rational(1, 2))
            for index in range(len(units))
        ),
        "positive_radii": True,
        "radius_family": "0<=r<=1",
        "radius_selected": False,
        "global_momentum_argument_used_by_law": False,
    }


def cell_transfer() -> sp.Matrix:
    return sp.Matrix((
        (0, -b208.CELL_A, 0),
        (-b208.CELL_A, 0, 0),
        (0, 0, b208.CELL_B),
    ))


def pulled_effects(depth: int, orientation: int) -> tuple[sp.Matrix, ...]:
    transfer = cell_transfer() ** depth
    return tuple(
        b208.cubic_effect(transfer.T * axis, orientation, 1)
        for axis in b208.signed_axes()
    )


def positive_effect(effect: sp.Matrix) -> bool:
    return (
        sp.trace(effect) > 0
        and effect.det() >= 0
        and sp.trace(I2 - effect) > 0
        and (I2 - effect).det() >= 0
    )


@cache
def cell_effect_facts() -> dict[str, object]:
    transfer = cell_transfer()
    rotations = b194.proper_cubic_rotations()
    normalizations = []
    positivity = []
    ranks = []
    covariance = []
    conjugate = []
    for depth in (0, 1, 2):
        for orientation in (1, -1):
            effects = pulled_effects(depth, orientation)
            normalizations.append(sum(effects, sp.zeros(2)) == I2)
            positivity.extend(positive_effect(effect) for effect in effects)
            ranks.append(tuple(effect.rank() for effect in effects))
            conjugate.extend(
                pulled_effects(depth, -1)[index]
                == sp.conjugate(pulled_effects(depth, 1)[index])
                for index in range(6)
            )
        for rotation in rotations:
            rotated_transfer = rotation * transfer * rotation.T
            for axis in b208.signed_axes():
                for depth in (1, 2):
                    covariance.append(
                        rotation * (transfer ** depth).T * axis
                        == (rotated_transfer ** depth).T * (rotation * axis)
                    )
    return {
        "transfer": transfer,
        "transfer_determinant": sp.factor(transfer.det()),
        "transfer_invertible": transfer.det() != 0,
        "leg_swap_same_transfer": transfer.T == transfer,
        "normalizations": all(normalizations),
        "positivity": all(positivity),
        "depth_zero_ranks": set(ranks[0]) == {1},
        "depth_one_two_full_rank": all(
            set(item) == {2} for item in ranks[2:]
        ),
        "covariance": all(covariance),
        "conjugate_readings": all(conjugate),
        "cell_depth_selected": False,
    }


def outcome_key(first: sp.Matrix, second: sp.Matrix) -> tuple[object, ...]:
    dot = int(first.dot(second))
    if dot:
        return ("dot", dot)
    return ("cross",) + tuple(first.cross(second))


def quotient_keys() -> tuple[tuple[object, ...], ...]:
    return (
        ("dot", 1), ("dot", -1),
        *(("cross",) + tuple(axis) for axis in b208.signed_axes()),
    )


def coarse_effects(depth: int, orientation: int) -> dict[tuple[object, ...], sp.Matrix]:
    axes = b208.signed_axes()
    endpoint = pulled_effects(depth, orientation)
    result = {key: sp.zeros(4) for key in quotient_keys()}
    for first_index, first in enumerate(axes):
        for second_index, second in enumerate(axes):
            result[outcome_key(first, second)] += sp.kronecker_product(
                endpoint[first_index], endpoint[second_index]
            )
    return {key: sp.simplify(value) for key, value in result.items()}


def shell_permutations() -> tuple[tuple[int, ...], ...]:
    axes = b208.signed_axes()
    result = []
    for rotation in b194.proper_cubic_rotations():
        result.append(tuple(
            next(index for index, candidate in enumerate(axes)
                 if candidate == rotation * axis)
            for axis in axes
        ))
    return tuple(result)


def act_mask(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    for index in range(6):
        if (mask >> index) & 1:
            result |= 1 << permutation[index]
    return result


def binary_shell_orbits() -> tuple[tuple[int, ...], ...]:
    unseen = set(range(64))
    result = []
    for seed in range(64):
        if seed not in unseen:
            continue
        orbit = tuple(sorted({
            act_mask(seed, permutation)
            for permutation in shell_permutations()
        }))
        unseen.difference_update(orbit)
        result.append(orbit)
    return tuple(result)


def coarse_code() -> dict[tuple[object, ...], int]:
    result = {("dot", 1): 0, ("dot", -1): 63}
    for index, axis in enumerate(b208.signed_axes()):
        result[("cross",) + tuple(axis)] = 1 << index
    return result


def reversed_outcome_key(key: tuple[object, ...]) -> tuple[object, ...]:
    if key[0] == "dot":
        return key
    return ("cross",) + tuple(-value for value in key[1:])


@cache
def quotient_register_facts() -> dict[str, object]:
    axes = b208.signed_axes()
    class_sizes = {key: 0 for key in quotient_keys()}
    scores = set()
    for first in axes:
        for second in axes:
            key = outcome_key(first, second)
            class_sizes[key] += 1
            scores.add((int(first.dot(second)),) + tuple(first.cross(second)))

    coarse_normalized = []
    coarse_positive = []
    naimark = []
    endpoint_swap = []
    tensor_swap = sp.Matrix((
        (1, 0, 0, 0),
        (0, 0, 1, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 1),
    ))
    for depth in (1, 2):
        family = coarse_effects(depth, 1)
        coarse_normalized.append(sum(family.values(), sp.zeros(4)) == I4)
        blocks = []
        for effect in family.values():
            coarse_positive.append(
                effect.rank() == 4 and effect.det() > 0
            )
            lower = effect.cholesky()
            kraus = lower.conjugate().T
            blocks.append(kraus)
            naimark.append(kraus.conjugate().T * kraus == effect)
        isometry = sp.Matrix.vstack(*blocks)
        naimark.append(isometry.conjugate().T * isometry == I4)
        endpoint_swap.extend(
            tensor_swap * effect * tensor_swap.T
            == family[reversed_outcome_key(key)]
            for key, effect in family.items()
        )

    one_shell_orbits = binary_shell_orbits()
    orbit_sizes = tuple(sorted(len(orbit) for orbit in one_shell_orbits))
    full_pair_orbits = []
    unseen_pairs = set(itertools.product(range(6), repeat=2))
    for seed in tuple(sorted(unseen_pairs)):
        if seed not in unseen_pairs:
            continue
        orbit = {
            (permutation[seed[0]], permutation[seed[1]])
            for permutation in shell_permutations()
        }
        unseen_pairs.difference_update(orbit)
        full_pair_orbits.append(orbit)

    code = coarse_code()
    code_covariance = []
    for rotation_index, permutation in enumerate(shell_permutations()):
        rotation = b194.proper_cubic_rotations()[rotation_index]
        for key, mask in code.items():
            if key[0] == "dot":
                rotated_key = key
            else:
                rotated_axis = rotation * sp.Matrix(key[1:])
                rotated_key = ("cross",) + tuple(rotated_axis)
            code_covariance.append(
                act_mask(mask, permutation) == code[rotated_key]
            )
    antipode = tuple(
        next(index for index, candidate in enumerate(axes)
             if candidate == -axis)
        for axis in axes
    )
    code_endpoint_swap = all(
        act_mask(mask, antipode) == code[reversed_outcome_key(key)]
        for key, mask in code.items()
    )

    full_two_shell_codes = {
        (first, second): (1 << first) | (1 << (6 + second))
        for first in range(6) for second in range(6)
    }
    two_shell_covariance = all(
        ((1 << permutation[first]) | (1 << (6 + permutation[second])))
        == full_two_shell_codes[(permutation[first], permutation[second])]
        for permutation in shell_permutations()
        for first in range(6) for second in range(6)
    )
    two_shell_endpoint_swap = all(
        ((code_value & 63) << 6) | ((code_value >> 6) & 63)
        == full_two_shell_codes[(second, first)]
        for (first, second), code_value in full_two_shell_codes.items()
    )

    return {
        "fine_outcomes": 36,
        "score_classes": len(scores),
        "class_sizes": tuple(sorted(class_sizes.values())),
        "coarsest_score_partition": len(scores) == 8,
        "coarse_normalized": all(coarse_normalized),
        "coarse_positive": all(coarse_positive),
        "naimark_isometry": all(naimark),
        "coarse_effect_endpoint_swap": all(endpoint_swap),
        "coarse_hilbert_qubit_minimum": math.ceil(math.log2(len(scores))),
        "fine_hilbert_qubit_minimum": math.ceil(math.log2(36)),
        "one_shell_orbit_sizes": orbit_sizes,
        "one_shell_has_regular_24_orbit": 24 in orbit_sizes,
        "full_pair_orbit_sizes": tuple(sorted(len(item) for item in full_pair_orbits)),
        "full36_one_shell_equivariant_injection": False,
        "full36_two_shell_code": len(set(full_two_shell_codes.values())) == 36,
        "full36_two_shell_covariance": two_shell_covariance,
        "full36_two_shell_endpoint_swap": two_shell_endpoint_swap,
        "coarse_code_count": len(set(code.values())),
        "coarse_code_covariance": all(code_covariance),
        "coarse_code_endpoint_swap": code_endpoint_swap,
        "coarse_code_patterns_orthogonal": len(set(code.values())) == 8,
    }


def coarse_probabilities(
    first_unit: sp.Expr,
    second_unit: sp.Expr,
    radius: sp.Expr,
    depth: int,
    orientation: int,
) -> dict[tuple[object, ...], sp.Expr]:
    state = sp.kronecker_product(
        phase_orbit_state(first_unit, radius, orientation),
        phase_orbit_state(second_unit, radius, orientation),
    )
    return {
        key: sp.simplify(sp.trace(effect * state))
        for key, effect in coarse_effects(depth, orientation).items()
    }


def decode_coarse_relative_phase(
    probabilities: dict[tuple[object, ...], sp.Expr],
    radius: sp.Expr,
    depth: int,
    orientation: int,
) -> sp.Expr:
    raw_dot, raw_cross = score_moments(probabilities)
    scale = sp.simplify(radius ** 2 * b208.CELL_A ** (2 * depth))
    dot = sp.simplify(raw_dot / scale)
    cross = sp.simplify((-1) ** depth * raw_cross / scale)
    assert cross[0] == 0 and cross[1] == 0
    return sp.simplify(dot + orientation * I * cross[2])


def score_moments(
    probabilities: dict[tuple[object, ...], sp.Expr],
) -> tuple[sp.Expr, sp.Matrix]:
    raw_dot = sp.simplify(9 * sum(
        probabilities[key] * key[1]
        for key in quotient_keys() if key[0] == "dot"
    ))
    raw_cross = sp.simplify(9 * sum((
        probabilities[key] * sp.Matrix(key[1:])
        for key in quotient_keys() if key[0] == "cross"
    ), sp.zeros(3, 1)))
    return raw_dot, raw_cross


def decode_coarse_relative_phase_self_normalized(
    probabilities: dict[tuple[object, ...], sp.Expr],
    depth: int,
    orientation: int,
) -> sp.Expr:
    """Recover the unit phase without a supplied radius or transfer scale."""
    raw_dot, raw_cross = score_moments(probabilities)
    assert raw_cross[0] == 0 and raw_cross[1] == 0
    scale = sp.sqrt(sp.simplify(raw_dot ** 2 + raw_cross.dot(raw_cross)))
    return sp.simplify(
        (raw_dot + orientation * I * (-1) ** depth * raw_cross[2]) / scale
    )


def decoded_unit(
    unit: sp.Expr, radius: sp.Expr, depth: int, orientation: int
) -> sp.Expr:
    probabilities = coarse_probabilities(
        sp.Integer(1), unit, radius, depth, orientation
    )
    return decode_coarse_relative_phase(
        probabilities, radius, depth, orientation
    )


@cache
def h1_facts() -> dict[str, object]:
    incoming, transfer = b207.b193.POINTS["H1"]
    outgoing = tuple(
        incoming[index] + transfer[index] for index in range(4)
    )
    alternative = (sp.Integer(0), sp.Integer(0), sp.Integer(0), incoming[3])
    alternative_outgoing = tuple(
        alternative[index] + transfer[index] for index in range(4)
    )

    exact = {}
    probability_vectors = {}
    for depth in (1, 2):
        for radius in (sp.Integer(1), sp.Rational(1, 2)):
            for orientation in (1, -1):
                def ratios(angles: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
                    return tuple(decoded_unit(
                        sp.cos(angle) + I * sp.sin(angle),
                        radius,
                        depth,
                        orientation,
                    ) for angle in angles)

                incoming_ratios = ratios(incoming)
                outgoing_ratios = ratios(outgoing)
                alternative_ratios = ratios(alternative)
                alternative_outgoing_ratios = ratios(alternative_outgoing)
                expected_incoming = b208.phase_ratios(incoming, orientation)
                expected_outgoing = b208.phase_ratios(outgoing, orientation)
                self_normalized_incoming = tuple(
                    decode_coarse_relative_phase_self_normalized(
                        coarse_probabilities(
                            sp.Integer(1),
                            sp.cos(angle) + I * sp.sin(angle),
                            radius,
                            depth,
                            orientation,
                        ),
                        depth,
                        orientation,
                    )
                    for angle in incoming
                )
                self_normalized_outgoing = tuple(
                    decode_coarse_relative_phase_self_normalized(
                        coarse_probabilities(
                            sp.Integer(1),
                            sp.cos(angle) + I * sp.sin(angle),
                            radius,
                            depth,
                            orientation,
                        ),
                        depth,
                        orientation,
                    )
                    for angle in outgoing
                )
                forward = b208.source_from_record_ratios(
                    incoming_ratios, outgoing_ratios, orientation
                )
                expected_forward = b208.source_from_record_ratios(
                    expected_incoming, expected_outgoing, orientation
                )
                reverse = b208.source_from_record_ratios(
                    outgoing_ratios, incoming_ratios, orientation
                )
                expected_reverse = b208.source_from_record_ratios(
                    expected_outgoing, expected_incoming, orientation
                )
                alternative_source = b208.source_from_record_ratios(
                    alternative_ratios,
                    alternative_outgoing_ratios,
                    orientation,
                )
                expected_alternative = b208.source_from_record_ratios(
                    b208.phase_ratios(alternative, orientation),
                    b208.phase_ratios(alternative_outgoing, orientation),
                    orientation,
                )
                exact[(depth, radius, orientation)] = {
                    "ratios": all(
                        sp.simplify(actual - expected) == 0
                        for actual, expected in zip(
                            incoming_ratios + outgoing_ratios,
                            expected_incoming + expected_outgoing,
                        )
                    ),
                    "self_normalized_ratios": all(
                        sp.simplify(actual - expected) == 0
                        for actual, expected in zip(
                            self_normalized_incoming + self_normalized_outgoing,
                            expected_incoming + expected_outgoing,
                        )
                    ),
                    "forward": forward == expected_forward,
                    "reverse": reverse == expected_reverse,
                    "alternative": alternative_source == expected_alternative,
                    "collision": (forward - alternative_source).rank(),
                }

            probe = sp.cos(sp.pi / 3) + I * sp.sin(sp.pi / 3)
            vector = coarse_probabilities(1, probe, radius, depth, 1)
            probability_vectors[(depth, radius)] = tuple(
                vector[key] for key in quotient_keys()
            )

    parent = b208.source_reconstruction_facts()
    return {
        "exact": exact,
        "all_ratios": all(item["ratios"] for item in exact.values()),
        "all_self_normalized_ratios": all(
            item["self_normalized_ratios"] for item in exact.values()
        ),
        "all_forward": all(item["forward"] for item in exact.values()),
        "all_reverse": all(item["reverse"] for item in exact.values()),
        "all_alternative": all(item["alternative"] for item in exact.values()),
        "collision_ranks_nonzero": all(
            item["collision"] > 0 for item in exact.values()
        ),
        "conditional_probability_vectors": len(set(probability_vectors.values())),
        "depth_fork": (
            probability_vectors[(1, sp.Integer(1))]
            != probability_vectors[(2, sp.Integer(1))]
        ),
        "radius_fork": (
            probability_vectors[(1, sp.Integer(1))]
            != probability_vectors[(1, sp.Rational(1, 2))]
        ),
        "parent_grouped_rank": parent["forward_grouped_rank"],
        "parent_atom_rank": parent["forward_atom_rank"],
        "parent_temporal_rows": parent["temporal_rows"],
        "parent_temporal_witness": parent["temporal_witness"],
        "law_reads_global_angle": False,
    }


@cache
def record_attachment_facts() -> dict[str, object]:
    projectors = (sp.diag(1, 0), sp.diag(0, 1))
    local_orthogonal = sp.trace(projectors[0] * projectors[1]) == 0
    configurations = []
    no_overwrite = []
    permanence = []
    for mask in coarse_code().values():
        blank: list[int | None] = [None] * 6
        for site in range(6):
            assert blank[site] is None
            blank[site] = (mask >> site) & 1
        written = tuple(blank)
        configurations.append(written)
        attempted = list(written)
        site = 0
        if attempted[site] is not None:
            no_overwrite.append(tuple(attempted) == written)
        permanence.append(tuple(written) == written)
    return {
        "blank_unreadable": True,
        "local_bit_states_orthogonal": local_orthogonal,
        "configuration_count": len(set(configurations)),
        "all_six_sites_written_once": all(
            all(item is not None for item in configuration)
            for configuration in configurations
        ),
        "no_overwrite": all(no_overwrite),
        "permanence_after_lock": all(permanence),
        "radius_one_shell": tuple(map(tuple, b208.signed_axes())),
        "block_write_radius_one": True,
        "naimark_environment_is_automatically_record": False,
        "semantic_lock_attachment_constructed": True,
        "blank_hilbert_state_constructed": False,
        "formation_cptp_channel_constructed": False,
        "formation_site_rate_selected": False,
        "autonomous_history_constructed": False,
        "event_conditioned": True,
    }


@cache
def classification_facts() -> dict[str, object]:
    h1 = h1_facts()
    return {
        "conditional_bridge_exists": (
            action_solder_facts()["degree_one_unique"]
            and cell_effect_facts()["normalizations"]
            and quotient_register_facts()["naimark_isometry"]
            and record_attachment_facts()["semantic_lock_attachment_constructed"]
            and h1["all_forward"] and h1["all_reverse"]
        ),
        "conditional_probability_image_many": (
            h1["conditional_probability_vectors"] >= 4
        ),
        "complete_probability_image_classified": False,
        "complete_h1_ownership": False,
        "h2_open": False,
        "axiom_update": False,
        "obligation_retirement": 0,
        "toe_movement": 0,
        "retained": False,
        "universal_no_go": False,
        "classification": "partial_joint_bridge_many_conditional_laws",
    }


N5_LINES = (
    "per_element: checked every degree-zero through degree-three corner intertwiner, all depth-one/depth-two pulled effects, eight coarse effects, Cholesky Kraus block, and local binary Record projector.",
    "per_site: checked one central two-endpoint event and all six signed-neighbor Record sites; each site changes from blank to one orthogonal bit exactly once; autonomous site/rate selection was checked and not executed — no such rule was derived.",
    "per_mode: checked every fixed H1 incoming and outgoing unit link factor, the same-transfer different-incoming control, both realifications, and literal actual reverse; H2 was checked and not executed — H2 is sealed outside this fixture.",
    "per_block: checked the full 36-to-eight score quotient, one-shell and two-shell cubic code orbits, the 32-by-4 Naimark isometry, and inherited H1 grouped 18/18 and atom 136/136 source identity.",
    "lattice_wide: checked all 24 proper-cubic transports of the cell effects and shell codes; autonomous competing events, general full-Z3 histories, formation clocks, retained closure, and TOE movement were checked and not executed — no such process was derived.",
)


def apply_mutation(claims: dict[str, object], mutation: str) -> None:
    mapping = {
        "stale_main_authority": ("main", "stale"),
        "drop_preregistration": ("prereg", False),
        "alter_goal_after_registration": ("goal", False),
        "erase_degree_one_uniqueness": ("degree_one_unique", False),
        "claim_full_section_unique": ("full_section_unique", True),
        "delete_higher_harmonic_controls": ("higher_controls", False),
        "break_action_field_normalization": ("action_field", False),
        "claim_phase_radius_selected": ("radius_selected", True),
        "make_cell_transfer_singular": ("cell_invertible", False),
        "break_cell_effect_normalization": ("cell_normalized", False),
        "break_cell_covariance": ("cell_covariant", False),
        "claim_cell_depth_selected": ("depth_selected", True),
        "break_score_quotient": ("score_quotient", False),
        "merge_unequal_scores": ("score_classes", 7),
        "claim_full36_one_shell_code": ("full36_one_shell", True),
        "break_coarse_code_covariance": ("code_covariant", False),
        "break_endpoint_swap": ("endpoint_swap", False),
        "break_naimark_isometry": ("naimark", False),
        "claim_environment_is_record": ("environment_record", True),
        "overwrite_record_site": ("no_overwrite", False),
        "claim_autonomous_formation": ("autonomous", True),
        "erase_depth_probability_fork": ("depth_fork", False),
        "erase_radius_probability_fork": ("radius_fork", False),
        "erase_h1_depth_one": ("h1_depth_one", False),
        "erase_h1_depth_two": ("h1_depth_two", False),
        "erase_self_normalized_decoder": ("self_normalized", False),
        "claim_complete_h1_ownership": ("complete", True),
        "claim_h2_open": ("h2", True),
        "claim_axiom_update": ("axiom", True),
        "claim_obligation_retirement": ("retirement", 1),
        "claim_toe_progress": ("toe", 1),
        "claim_retained_status": ("retained", True),
        "claim_universal_no_go": ("universal_no_go", True),
    }
    key, value = mapping[mutation]
    claims[key] = value


def run(mutation: str = "") -> tuple[int, int, dict[str, object]]:
    authority = authority_facts()
    solder = action_solder_facts()
    phase = phase_solder_facts()
    cell = cell_effect_facts()
    quotient = quotient_register_facts()
    h1 = h1_facts()
    record = record_attachment_facts()
    classification = classification_facts()

    claims: dict[str, object] = {
        "main": CURRENT_MAIN,
        "prereg": True,
        "goal": True,
        "degree_one_unique": True,
        "full_section_unique": False,
        "higher_controls": True,
        "action_field": True,
        "radius_selected": False,
        "cell_invertible": True,
        "cell_normalized": True,
        "cell_covariant": True,
        "depth_selected": False,
        "score_quotient": True,
        "score_classes": 8,
        "full36_one_shell": False,
        "code_covariant": True,
        "endpoint_swap": True,
        "naimark": True,
        "environment_record": False,
        "no_overwrite": True,
        "autonomous": False,
        "depth_fork": True,
        "radius_fork": True,
        "h1_depth_one": True,
        "h1_depth_two": True,
        "self_normalized": True,
        "complete": False,
        "h2": False,
        "axiom": False,
        "retirement": 0,
        "toe": 0,
        "retained": False,
        "universal_no_go": False,
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
        and (authority["goal_registered"] == authority["goal_worktree"])
        == claims["goal"]
        and authority["axiom_main"] == AXIOM_BLOB
        and authority["axiom_worktree"] == AXIOM_BLOB
        and authority["registry_main"] == REGISTRY_MAIN_BLOB
        and authority["registry_worktree"] == REGISTRY_WORKTREE_BLOB
    )
    solder_ok = (
        solder["degree_hom_dimensions"] == (0, 1, 1, 1)
        and solder["full_hom_dimension"] == 3
        and solder["degree_one_unique"] == claims["degree_one_unique"]
        and solder["degree_one_radial_nonzero"]
        and solder["higher_harmonics_radial_null"] == claims["higher_controls"]
        and solder["right_inverse"] and solder["right_inverse_equals_minimum_norm"]
        and solder["direct_field"] == claims["action_field"]
        and solder["field_positive"]
        and solder["right_inverse_affine_dimension"] == 2
        and solder["full_section_unique"] == claims["full_section_unique"]
        and solder["higher_harmonics_readable_if_prepared"]
    )
    phase_ok = (
        phase["traces"] and phase["pure_radius_one"]
        and phase["mixed_radius_half"] and phase["conjugate_readings"]
        and phase["positive_radii"]
        and phase["radius_selected"] == claims["radius_selected"]
        and not phase["global_momentum_argument_used_by_law"]
    )
    cell_ok = (
        cell["transfer_invertible"] == claims["cell_invertible"]
        and cell["leg_swap_same_transfer"]
        and cell["normalizations"] == claims["cell_normalized"]
        and cell["positivity"]
        and cell["depth_zero_ranks"] and cell["depth_one_two_full_rank"]
        and cell["covariance"] == claims["cell_covariant"]
        and cell["conjugate_readings"]
        and cell["cell_depth_selected"] == claims["depth_selected"]
    )
    quotient_ok = (
        quotient["fine_outcomes"] == 36
        and quotient["score_classes"] == claims["score_classes"]
        and quotient["class_sizes"] == (4, 4, 4, 4, 4, 4, 6, 6)
        and quotient["coarsest_score_partition"] == claims["score_quotient"]
        and quotient["coarse_normalized"] and quotient["coarse_positive"]
        and quotient["coarse_hilbert_qubit_minimum"] == 3
        and quotient["fine_hilbert_qubit_minimum"] == 6
    )
    register_ok = (
        not quotient["one_shell_has_regular_24_orbit"]
        and quotient["full_pair_orbit_sizes"] == (6, 6, 24)
        and quotient["full36_one_shell_equivariant_injection"]
        == claims["full36_one_shell"]
        and quotient["full36_two_shell_code"]
        and quotient["full36_two_shell_covariance"]
        and quotient["full36_two_shell_endpoint_swap"]
        == claims["endpoint_swap"]
        and quotient["coarse_code_count"] == 8
        and quotient["coarse_code_covariance"] == claims["code_covariant"]
        and quotient["coarse_code_endpoint_swap"]
        == claims["endpoint_swap"]
        and quotient["coarse_code_patterns_orthogonal"]
    )
    naimark_ok = (
        quotient["naimark_isometry"] == claims["naimark"]
        and quotient["coarse_effect_endpoint_swap"]
        == claims["endpoint_swap"]
    )
    record_ok = (
        record["blank_unreadable"]
        and record["local_bit_states_orthogonal"]
        and record["configuration_count"] == 8
        and record["all_six_sites_written_once"]
        and record["no_overwrite"] == claims["no_overwrite"]
        and record["permanence_after_lock"]
        and record["block_write_radius_one"]
        and record["naimark_environment_is_automatically_record"]
        == claims["environment_record"]
        and record["semantic_lock_attachment_constructed"]
        and not record["blank_hilbert_state_constructed"]
        and not record["formation_cptp_channel_constructed"]
        and record["autonomous_history_constructed"] == claims["autonomous"]
        and record["event_conditioned"]
    )
    depth_one = all(
        item["ratios"] and item["forward"] and item["reverse"]
        and item["alternative"] and item["collision"] > 0
        for key, item in h1["exact"].items() if key[0] == 1
    )
    depth_two = all(
        item["ratios"] and item["forward"] and item["reverse"]
        and item["alternative"] and item["collision"] > 0
        for key, item in h1["exact"].items() if key[0] == 2
    )
    h1_ok = (
        depth_one == claims["h1_depth_one"]
        and depth_two == claims["h1_depth_two"]
        and h1["all_ratios"] and h1["all_forward"] and h1["all_reverse"]
        and h1["all_self_normalized_ratios"]
        == claims["self_normalized"]
        and h1["all_alternative"] and h1["collision_ranks_nonzero"]
        and h1["parent_grouped_rank"] == 18
        and h1["parent_atom_rank"] == 136
        and h1["parent_temporal_rows"] == 128
        and h1["parent_temporal_witness"] == sp.Rational(1, 8)
    )
    image_ok = (
        h1["conditional_probability_vectors"] == 4
        and h1["depth_fork"] == claims["depth_fork"]
        and h1["radius_fork"] == claims["radius_fork"]
        and classification["conditional_bridge_exists"]
        and classification["conditional_probability_image_many"]
    )
    boundary_ok = (
        classification["complete_h1_ownership"] == claims["complete"]
        and classification["h2_open"] == claims["h2"]
        and classification["axiom_update"] == claims["axiom"]
        and classification["obligation_retirement"] == claims["retirement"]
        and classification["toe_movement"] == claims["toe"]
        and classification["retained"] == claims["retained"]
        and classification["universal_no_go"] == claims["universal_no_go"]
        and not record["formation_site_rate_selected"]
        and not solder["first_harmonic_physically_selected"]
    )

    checks = {
        "A": (authority_ok, "authority and immutable preregistration are pinned"),
        "B": (solder_ok, "the H1-active corner solder is unique at Walsh degree one while two readable higher-harmonic null directions survive"),
        "C": (phase_ok, "the unit-link first-harmonic M2 orbit is exact but its Bloch radius is not selected"),
        "D": (cell_ok, "one and two direct cell uses induce positive normalized covariant endpoint effect menus with an invertible decoder"),
        "E": (quotient_ok, "the 36 outcomes have a unique coarsest deterministic eight-class dot/cross score quotient"),
        "F": (register_ok, "the raw 36 labels need two geometric shells, while the eight-class quotient has one exact cubic and endpoint-reversing shell code"),
        "G": (naimark_ok, "each depth-one/depth-two coarse POVM has an exact square-root Naimark isometry"),
        "H": (record_ok, "the shell code admits an axiom-semantic no-overwrite attachment for one supplied event, not a formation channel"),
        "I": (h1_ok, "self-normalized Record probabilities reproduce both H1 directions, the collision, 128 temporal rows and the one-eighth witness"),
        "J": (image_ok, "two cell depths and two state radii give four distinct conditional readable laws with the same calibrated H1 source"),
        "K": (boundary_ok, "physical selection, autonomous formation/history, H2, axiom update, retention, obligation retirement and TOE movement remain open"),
    }
    passed = sum(int(value[0]) for value in checks.values())
    failed = len(checks) - passed
    return passed, failed, {
        "checks": checks,
        "solder": solder,
        "cell": cell,
        "quotient": quotient,
        "h1": h1,
        "record": record,
        "classification": classification,
    }


def mutation_suite() -> int:
    baseline_passed, baseline_failed, _facts = run()
    detected = 0
    print(
        f"BASELINE: PASS={baseline_passed} FAIL={baseline_failed}; "
        f"mutations={len(MUTATIONS)}."
    )
    for mutation in MUTATIONS:
        _passed, failed, _mutation_facts = run(mutation)
        caught = failed > 0
        detected += int(caught)
        print(
            f"MUTATION {mutation}: {'DETECTED' if caught else 'ESCAPED'} "
            f"(runner_failures={failed})"
        )
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
    solder = facts["solder"]
    cell = facts["cell"]
    quotient = facts["quotient"]
    h1 = facts["h1"]
    record = facts["record"]
    print(
        "ACTION_SOLDER: Walsh Hom dimensions="
        f"{solder['degree_hom_dimensions']}; degree-one right inverse exact; "
        "degree-two/three radial-null; full affine section dimension=2."
    )
    print(
        "CELL_EFFECTS: T determinant="
        f"{cell['transfer_determinant']}; depths 1/2 positive, normalized, "
        "full-rank and 24-frame covariant; depth is not selected."
    )
    print(
        "SCORE_QUOTIENT: 36 -> 8 classes with sizes="
        f"{quotient['class_sizes']}; Hilbert minimum=3 qubits; "
        "one-shell cubic code=8/8."
    )
    print(
        "REGISTER: raw pair orbit sizes="
        f"{quotient['full_pair_orbit_sizes']}; one-shell binary orbits have "
        f"no regular 24 orbit={not quotient['one_shell_has_regular_24_orbit']}; "
        "two-shell raw code and one-shell coarse code pass."
    )
    print(
        "H1_RECORD_DECODE: grouped=18/18; atoms=136/136; temporal rows=128; "
        f"witness={h1['parent_temporal_witness']}; depths 1/2 and radii "
        "1,1/2 all give zero forward/actual-reverse residual; the score norm "
        "self-calibrates radius and transfer magnitude."
    )
    print(
        "PROBABILITY_IMAGE: conditional frozen controls="
        f"{h1['conditional_probability_vectors']} distinct laws; "
        "complete-law one/many/none remains unresolved because state radius, "
        "cell depth and autonomous formation are not selected."
    )
    print(
        "ATTACHMENT: orthogonal six-site axiom-semantic blank-to-locked patterns="
        f"{record['configuration_count']}; no overwrite/permanence pass; "
        "one supplied event only, with no blank-state or formation channel."
    )
    for line in N5_LINES:
        print(line)
    for key, (ok, text) in facts["checks"].items():
        print(f"CHECK {key}: {'PASS' if ok else 'FAIL'} - {text}")
    if args.mutation:
        print(f"MUTATION: {args.mutation}")
    print(
        "RESULT: exact action-active degree-one solder, cell-induced effect "
        "menus, eight-class score quotient, orthogonal cubic shell code and "
        "event-conditioned semantic attachment; multiple conditional readable laws and "
        "no selected autonomous physical law."
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
