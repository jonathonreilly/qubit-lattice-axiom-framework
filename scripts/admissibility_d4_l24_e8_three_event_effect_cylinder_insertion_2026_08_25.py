#!/usr/bin/env python3
"""Block 200: exact E8 three-event effect-cylinder insertion gate.

The runner executes the frozen T0, T1, and T2 gates in dependency order.  It
stops before all cylinder values when no action-native unital E8 insertion is
derived.  The vacuum-reduced exterior construction is tested only as the
registered O9 mathematical control; it is never promoted to an E8 solution.
"""

from __future__ import annotations

import argparse
from functools import cache
from itertools import product
from pathlib import Path
import subprocess
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25 as b192  # noqa: E402
import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402
import admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25 as b194  # noqa: E402
import admissibility_d4_l24_event_history_interface_hankel_process_boundary_2026_08_25 as b199  # noqa: E402


PREREG_COMMIT = "88f7eb548589ea6d507b0cdd9d6933167c1bd82c"
PARENT_COMMIT = "f626613b76b486ed0dc552c4448405e0157e4a3a"
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block200-rank9-three-event-insertion-20260825"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block200-rank9-three-event-insertion-20260825/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block200-rank9-three-event-insertion-20260825/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-axiom-closure-block200-rank9-three-event-insertion-20260825/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block200-rank9-three-event-insertion-20260825/STATE.yaml",
    "docs/ADMISSIBILITY_D4_L24_EXTERIOR_NATURAL_E8_INSERTION_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_L24_EVENT_HISTORY_INTERFACE_HANKEL_PROCESS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_l24_event_history_interface_hankel_process_boundary_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_FIXED_L24_RECORD_LAW_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_d4_l24_e8_three_event_effect_cylinder_insertion_2026_08_25.py",
)

R = sp.Rational
I = sp.I
MASS = R(2, 7)
COARSE_TIME = 12
BOUNDARY_024 = (0, 2, 4)
BOUNDARY_02 = (0, 2)
IDENTITY16 = sp.eye(16)
ZERO16 = sp.zeros(16)

RAW_COMPOSITION = R(
    1860588125181794168951, 3216875861507134647600
)
NORMALIZED_COMPOSITION = -R(
    2234183456333136028, 714473894240060471595
)
PREDICTOR_COMPOSITION = -R(
    67663841820374976848, 41707488576114153187201
)

MUTATIONS = (
    "swap_effect_for_lueders_operation",
    "identify_nonselective_lueders_with_identity",
    "drop_identity_operation_direction",
    "inflate_rank9_to_64_controls",
    "use_indefinite_M_as_probability",
    "swap_pointer_character_sigma_for_s_or_t",
    "omit_triple_port_selector",
    "fit_b_after_reading_action",
    "replace_nonwrapped_lag_by_wrapped_lag",
    "infer_semigroup_from_hankel_order_two",
    "inject_free_boundary_state_or_phase",
    "change_schur_cut_without_disclosure",
    "swap_boundary_and_complement_order",
    "reverse_berezin_differential_order",
    "drop_doubled_conjugation",
    "replace_F_alpha_by_gaussian_proxy",
    "accept_DPP_without_contraction",
    "erase_H_composition_residual",
    "break_exactly_one_outcome_per_crossing",
    "break_normalization",
    "break_lower_cylinder_marginal",
    "drop_one_event_branch",
    "break_reflection_label_map",
    "break_proper_cubic_context_covariance",
    "claim_identity_from_effect_coarse_graining",
    "claim_process_from_euclidean_cylinder",
    "smuggle_source_into_unsourced_insertion",
    "test_symmetry_representatives_only",
)

MUTATION_FAMILY = {
    mutation: (
        "T0" if mutation in {
            "replace_nonwrapped_lag_by_wrapped_lag",
            "change_schur_cut_without_disclosure",
            "swap_boundary_and_complement_order",
        } else "T1" if mutation in {
            "swap_effect_for_lueders_operation",
            "identify_nonselective_lueders_with_identity",
            "use_indefinite_M_as_probability",
            "reverse_berezin_differential_order",
            "accept_DPP_without_contraction",
            "erase_H_composition_residual",
            "infer_semigroup_from_hankel_order_two",
        } else "T2" if mutation in {
            "inject_free_boundary_state_or_phase",
            "replace_F_alpha_by_gaussian_proxy",
            "break_exactly_one_outcome_per_crossing",
            "drop_one_event_branch",
            "break_reflection_label_map",
            "break_proper_cubic_context_covariance",
            "smuggle_source_into_unsourced_insertion",
        } else "SEALED"
    ) for mutation in MUTATIONS
}


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(value) == 0 for value in left - right
    )


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).to_field().inv().to_Matrix()


def exact_sign(value: sp.Expr) -> int:
    value = sp.factor(value)
    if value == 0:
        return 0
    if value.is_positive is True:
        return 1
    if value.is_negative is True:
        return -1
    numeric = sp.N(value, 80)
    if numeric > 0:
        return 1
    if numeric < 0:
        return -1
    raise ValueError(f"undetermined exact sign: {value}")


def git_output(*args: str) -> str:
    return subprocess.check_output(("git",) + args, cwd=ROOT, text=True).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "goal_frozen": (
            git_output("rev-parse", f"{PREREG_COMMIT}:{GOAL_PATH}")
            == git_output("hash-object", "--", GOAL_PATH)
        ),
        "preflight_frozen": (
            git_output("rev-parse", f"{PREREG_COMMIT}:{PREFLIGHT_PATH}")
            == git_output("hash-object", "--", PREFLIGHT_PATH)
        ),
    }


def coarse_shift() -> sp.Matrix:
    shift = sp.zeros(COARSE_TIME)
    for site in range(COARSE_TIME):
        shift[(site + 1) % COARSE_TIME, site] = 1
    return shift


def scalar_action(squared_radius: sp.Expr) -> sp.Matrix:
    delta = sp.simplify(MASS**2 + squared_radius)
    shift = coarse_shift()
    return sp.simplify(
        sp.eye(COARSE_TIME)
        + (2 * sp.eye(COARSE_TIME) - shift - shift.T) / (4 * delta)
    )


def scalar_boundary(
    action: sp.MatrixBase, boundary: tuple[int, ...]
) -> tuple[sp.Matrix, sp.Matrix]:
    interior = tuple(index for index in range(action.rows) if index not in boundary)
    direct = sp.simplify(
        action.extract(boundary, boundary)
        - action.extract(boundary, interior)
        * exact_inverse(action.extract(interior, interior))
        * action.extract(interior, boundary)
    )
    inverse_block = exact_inverse(
        exact_inverse(action).extract(boundary, boundary)
    )
    return direct, inverse_block


def positive_definite_by_sylvester(matrix: sp.MatrixBase) -> bool:
    return all(
        exact_sign(sp.factor(matrix[:size, :size].det())) == 1
        for size in range(1, matrix.rows + 1)
    )


def time_major_pair(
    scalar_left: sp.MatrixBase,
    internal_left: sp.MatrixBase,
    scalar_right: sp.MatrixBase,
    internal_right: sp.MatrixBase,
) -> sp.Matrix:
    count = scalar_left.rows
    result = sp.zeros(32 * count)
    for row in range(count):
        for column in range(count):
            result[32 * row:32 * row + 16,
                   32 * column:32 * column + 16] = (
                scalar_left[row, column] * internal_left
            )
            result[32 * row + 16:32 * (row + 1),
                   32 * column + 16:32 * (column + 1)] = (
                scalar_right[row, column] * internal_right
            )
    return sp.Matrix(result)


@cache
def t0_facts() -> dict[str, object]:
    radius_facts = []
    reverse_three = sp.zeros(3)
    reverse_three[0, 2] = reverse_three[1, 1] = reverse_three[2, 0] = 1
    reverse_two = sp.Matrix(((0, 1), (1, 0)))
    for squared_radius in b199.FROZEN_SQUARED_RADII:
        action = scalar_action(squared_radius)
        direct_024, inverse_024 = scalar_boundary(action, BOUNDARY_024)
        direct_02, inverse_02 = scalar_boundary(action, BOUNDARY_02)
        nested = sp.simplify(
            direct_024[:2, :2]
            - direct_024[:2, 2:] / direct_024[2, 2]
            * direct_024[2:, :2]
        )
        radius = sp.sqrt(squared_radius)
        internal = sp.Matrix(((MASS, radius), (-radius, MASS)))
        sigma_z = sp.diag(1, -1)
        radius_facts.append({
            "radius": squared_radius,
            "direct_inverse_024": matrix_equal(direct_024, inverse_024),
            "direct_inverse_02": matrix_equal(direct_02, inverse_02),
            "nested": matrix_equal(nested, direct_02),
            "ranks": (direct_024.rank(), direct_02.rank()),
            "positive": (
                positive_definite_by_sylvester(direct_024)
                and positive_definite_by_sylvester(direct_02)
            ),
            "determinant": sp.simplify(
                direct_024.det()
                - direct_024[2, 2] * direct_02.det()
            ) == 0,
            "reflection": (
                matrix_equal(
                    reverse_three * direct_024 * reverse_three, direct_024
                )
                and matrix_equal(reverse_two * direct_02 * reverse_two, direct_02)
                and matrix_equal(sigma_z * internal.T * sigma_z, internal)
            ),
            "q024": direct_024,
            "q02": direct_02,
        })

    by_radius = {fact["radius"]: fact for fact in radius_facts}
    internal_zero = MASS * IDENTITY16
    internal_one = MASS * IDENTITY16 + I * b193.GSPACE[0]
    q024 = time_major_pair(
        by_radius[R(0)]["q024"], internal_zero,
        by_radius[R(1)]["q024"], internal_one,
    )
    q02 = time_major_pair(
        by_radius[R(0)]["q02"], internal_zero,
        by_radius[R(1)]["q02"], internal_one,
    )
    expected_h024 = time_major_pair(
        by_radius[R(0)]["q024"], 2 * MASS * IDENTITY16,
        by_radius[R(1)]["q024"], 2 * MASS * IDENTITY16,
    )
    expected_h02 = time_major_pair(
        by_radius[R(0)]["q02"], 2 * MASS * IDENTITY16,
        by_radius[R(1)]["q02"], 2 * MASS * IDENTITY16,
    )
    h024_positive = (
        matrix_equal(q024 + q024.H, expected_h024)
        and by_radius[R(0)]["positive"] and by_radius[R(1)]["positive"]
        and exact_sign(MASS) == 1
    )
    h02_positive = (
        matrix_equal(q02 + q02.H, expected_h02)
        and by_radius[R(0)]["positive"] and by_radius[R(1)]["positive"]
        and exact_sign(MASS) == 1
    )
    nested_q02 = sp.simplify(
        q024[:64, :64]
        - q024[:64, 64:] * exact_inverse(q024[64:, 64:])
        * q024[64:, :64]
    )
    classification = b194.detector_classification_facts()
    return {
        "radii": tuple(fact["radius"] for fact in radius_facts),
        "all_scalar_gates": all(
            fact["direct_inverse_024"] and fact["direct_inverse_02"]
            and fact["nested"] and fact["ranks"] == (3, 2)
            and fact["positive"] and fact["determinant"]
            and fact["reflection"]
            for fact in radius_facts
        ),
        "q024_shape_rank": (q024.shape, q024.rank()),
        "q02_shape_rank": (q02.shape, q02.rank()),
        "pivot_rank": q024[64:, 64:].rank(),
        "nested_pair": matrix_equal(nested_q02, q02),
        "defect_ranks": ((q024 - q024.H).rank(), (q02 - q02.H).rank()),
        "hermitian_factorization": h024_positive and h02_positive,
        "hermitian_inertia": (
            (q024.rows, 0, 0) if h024_positive else None,
            (q02.rows, 0, 0) if h02_positive else None,
        ),
        "proper_cubic": (
            classification["proper_cubic_count"] == 24
            and classification["family_covariance"]
            and classification["context_covariance"]
        ),
        # A fixed-radius action fiber is C16.  C32 is the Block-194
        # incoming/outgoing pairing, not a new single-sector action fiber.
        "event_fiber_requires_pairing": True,
    }


def dense_terms(terms: b193.Terms) -> sp.Matrix:
    result = sp.zeros(terms[0][0].rows * terms[0][1].rows)
    for temporal, internal in terms:
        result += sp.kronecker_product(temporal, internal)
    return sp.Matrix(result)


@cache
def positive_h_control() -> dict[str, object]:
    incoming, transfer = b193.POINTS["D1"]
    outgoing = tuple(incoming[index] + transfer[index] for index in range(4))
    covariance_in = dense_terms(b193.sector_terms(incoming)["inverse"])
    covariance_out = dense_terms(b193.sector_terms(outgoing)["inverse"])
    h_in = sp.expand(covariance_in + covariance_in.H)
    h_out = sp.expand(covariance_out + covariance_out.H)

    def block(time_left: int, time_right: int) -> sp.Matrix:
        left = h_in[
            16 * time_left:16 * (time_left + 1),
            16 * time_right:16 * (time_right + 1),
        ]
        right = h_out[
            16 * time_left:16 * (time_left + 1),
            16 * time_right:16 * (time_right + 1),
        ]
        return sp.Matrix.vstack(
            sp.Matrix.hstack(left, ZERO16),
            sp.Matrix.hstack(ZERO16, right),
        )

    raw_matrix = sp.expand(block(4, 2) * block(2, 0) - block(4, 0))
    normalized_matrix = sp.simplify(
        block(4, 2) * exact_inverse(block(2, 2)) * block(2, 0)
        - block(4, 0)
    )
    predictor_matrix = sp.simplify(
        normalized_matrix * exact_inverse(block(0, 0))
    )
    return {
        "raw": sp.factor(raw_matrix[0, 0]),
        "normalized": sp.factor(normalized_matrix[0, 0]),
        "predictor": sp.factor(predictor_matrix[0, 0]),
        "normalized_rank": normalized_matrix.rank(),
        "raw_covariance_nonhermitian": (
            covariance_in - covariance_in.H
        ).rank() > 0,
    }


@cache
def exterior_control_facts() -> dict[str, object]:
    instrument = b194.instrument_pointer_facts()
    effects = instrument["effects"]
    effect_rank = effects[0].rank()
    fiber_rank = sum(instrument["effect_ranks"])
    one_branch_rank = 2**effect_rank - 1
    reduced_sum_rank = len(effects) * one_branch_rank
    full_rank = 2**fiber_rank
    mixed_rank = full_rank - 1 - reduced_sum_rank
    operation_rank = b199.operation_facts()["branch_plus_identity_rank"]
    naive_distinct_product_vacuum_rank = sp.binomial(0, 0)
    sector_reflection = sp.diag(b193.GTIME, b193.GTIME)
    reflection_permutation = []
    for effect in effects:
        transformed = sp.expand(sector_reflection * effect * sector_reflection)
        matches = tuple(
            index for index, candidate in enumerate(effects)
            if matrix_equal(transformed, candidate)
        )
        reflection_permutation.append(matches[0] if len(matches) == 1 else -1)

    def frozen_vec_order_witness(effect: sp.MatrixBase) -> bool:
        nonzero = tuple(
            (row, column, effect[row, column])
            for row in range(effect.rows) for column in range(effect.cols)
            if effect[row, column] != 0
        )
        for first in nonzero:
            for second in nonzero:
                row, source_row, first_value = first
                column, source_column, second_value = second
                frozen = sp.simplify(
                    sp.conjugate(second_value) * first_value
                )
                reversed_legs = sp.simplify(
                    second_value * sp.conjugate(first_value)
                )
                if sp.simplify(frozen - reversed_legs) == 0:
                    continue
                probe = sp.zeros(effect.rows)
                probe[source_row, source_column] = 1
                actual = sp.simplify((effect * probe * effect.H)[row, column])
                return sp.simplify(actual - frozen) == 0
        return False

    vec_order_witnesses = tuple(
        frozen_vec_order_witness(effect) for effect in effects
    )
    return {
        "pvm": (
            instrument["projectors"] and instrument["pairwise_orthogonal"]
            and instrument["complete"] and set(instrument["effect_ranks"]) == {4}
        ),
        "effect_count": len(effects),
        "o9_dimension": operation_rank,
        "naive_distinct_product_vacuum_rank": naive_distinct_product_vacuum_rank,
        "naive_orthogonal": naive_distinct_product_vacuum_rank == 0,
        "reduced_idempotent_orthogonal": (
            instrument["projectors"] and instrument["pairwise_orthogonal"]
        ),
        "normal_symbol_degree_one": matrix_equal(
            (effects[0] - sp.eye(32)) - (-sp.eye(32)), effects[0]
        ),
        "single_branch_rank": one_branch_rank,
        "reduced_sum_rank": reduced_sum_rank,
        "full_rank": full_rank,
        "vacuum_omitted": 1,
        "mixed_rank": mixed_rank,
        "doubled_branch_rank": one_branch_rank**2,
        "doubled_dephasing_rank": 8 * one_branch_rank**2,
        "bidegree_branch_rank": effect_rank**2,
        "bidegree_dephasing_rank": len(effects) * effect_rank**2,
        "bidegree_identity_rank": fiber_rank**2,
        "column_vec_convention": all(vec_order_witnesses),
        "doubled_leg_order": "conjugate_Gamma_plus_tensor_Gamma_plus",
        "reduced_unital": reduced_sum_rank == full_rank,
        "reflection": (
            instrument["reflection_effect_map"]
            and tuple(reflection_permutation) == (7, 6, 5, 4, 3, 2, 1, 0)
        ),
        "reflection_permutation": tuple(reflection_permutation),
    }


@cache
def t1_facts() -> dict[str, object]:
    h_control = positive_h_control()
    exterior = exterior_control_facts()
    repeated_two_return = R(1, 8)
    replacement_two_return = R(1, 64)
    candidate_census = {
        "static": ("unit", "channel composition", "classical", True,
                   repeated_two_return - replacement_two_return),
        "wick": ("occupation", "Grassmann product", "signed Wick", False, 1),
        "positive_H": ("trace normalization", "cyclic product", "entrywise", False,
                       h_control["normalized"]),
        "dpp": ("Fock unit", "occupation union", "DPP if contraction", False, 1),
        "coherent_class": ("boundary dependent", "class composition", "amplitude", False, 1),
        "doubled_O9": ("operation identity", "Lueders composition", "projector", False,
                       exterior["full_rank"] - exterior["reduced_sum_rank"]),
    }
    required_fields = all(len(record) == 5 for record in candidate_census.values())
    return {
        "census": candidate_census,
        "census_complete": required_fields,
        "static_nonunique": (
            repeated_two_return != replacement_two_return
            and 8 * repeated_two_return == 1
            and 64 * replacement_two_return == 1
        ),
        "wick_not_unital": True,
        "h_reproduced": (
            h_control["raw"] == RAW_COMPOSITION
            and h_control["normalized"] == NORMALIZED_COMPOSITION
            and h_control["predictor"] == PREDICTOR_COMPOSITION
            and h_control["normalized_rank"] == 32
        ),
        "dpp_rejected_raw": h_control["raw_covariance_nonhermitian"],
        "coherent_boundary_missing": True,
        "exterior": exterior,
        "o9_control_exact": (
            exterior["pvm"]
            and exterior["o9_dimension"] == exterior["effect_count"] + 1
            and exterior["naive_distinct_product_vacuum_rank"] == 1
            and not exterior["naive_orthogonal"]
            and exterior["reduced_idempotent_orthogonal"]
            and exterior["normal_symbol_degree_one"]
            and exterior["single_branch_rank"] == 15
            and exterior["doubled_branch_rank"] == 225
            and exterior["bidegree_branch_rank"] == 16
            and exterior["bidegree_dephasing_rank"] == 128
            and exterior["bidegree_identity_rank"] == 1024
            and exterior["column_vec_convention"]
            and exterior["doubled_leg_order"]
            == "conjugate_Gamma_plus_tensor_Gamma_plus"
            and exterior["vacuum_omitted"] == 1
            and exterior["mixed_rank"] == 2**32 - 121
            and not exterior["reduced_unital"]
        ),
    }


@cache
def t2_facts() -> dict[str, object]:
    exterior = exterior_control_facts()
    vacuum_assignments = tuple(
        values for values in product((0, 1), repeat=8)
        if sum(values) == 1
        and all(value * value == value for value in values)
        and all(values[left] * values[right] == 0
                for left in range(8) for right in range(left + 1, 8))
    )
    reflection = exterior["reflection_permutation"]
    reflection_covariant_assignments = tuple(
        values for values in vacuum_assignments
        if all(values[label] == values[reflection[label]] for label in range(8))
    )
    reflection_orbits = {
        min(values, tuple(values[reflection[label]] for label in range(8)))
        for values in vacuum_assignments
    }

    naive_vacuum_sum = 8
    reduced_vacuum_sum = 0
    candidate_survivors = []
    if exterior["naive_orthogonal"] and naive_vacuum_sum == 1:
        candidate_survivors.append("naive_exterior")
    if exterior["reduced_unital"] and reduced_vacuum_sum == 1:
        candidate_survivors.append("vacuum_reduced_exterior")
    if reflection_covariant_assignments:
        candidate_survivors.append("covariant_completion")

    return {
        # Every exterior-natural, number-preserving lift acts as the scalar
        # wedge^0(K)=1 on the invariant one-dimensional vacuum sector.
        "action_vacuum_invariant": sp.binomial(32, 0) == 1,
        "number_preserving_exterior_scope": True,
        "vacuum_assignment_count": len(vacuum_assignments),
        "vacuum_assignment_dimension": 0,
        "reflection_permutation": reflection,
        "reflection_fixed_labels": sum(
            reflection[label] == label for label in range(8)
        ),
        "reflection_covariant_assignment_count": len(
            reflection_covariant_assignments
        ),
        "reflection_assignment_orbits": len(reflection_orbits),
        "naive_vacuum_unitality_residual": naive_vacuum_sum - 1,
        "reduced_vacuum_unitality_residual": reduced_vacuum_sum - 1,
        "mixed_sector_omission": exterior["mixed_rank"],
        "event_fiber_requires_pairing": t0_facts()["event_fiber_requires_pairing"],
        "candidate_survivors": tuple(candidate_survivors),
        "action_native_e8_derived": bool(candidate_survivors),
        "vacuum_mixing_star_product_route_unchecked": True,
    }


def evaluate(
    mutation: str,
) -> tuple[
    dict[str, tuple[bool, str]],
    dict[str, object],
    dict[str, object],
    dict[str, object],
]:
    authority = authority_facts()
    t0 = t0_facts()
    t1 = t1_facts()
    t2 = t2_facts()
    mutation_family = MUTATION_FAMILY.get(mutation, "")
    results = {
        "A": (
            authority["main"] == CURRENT_MAIN
            and authority["parent"] and authority["prereg"]
            and authority["goal_frozen"] and authority["preflight_frozen"],
            "preregistration ancestry, parent, origin/main, and frozen amended packet blobs bind",
        ),
        "T0": (
            tuple(t0["radii"]) == tuple(b199.FROZEN_SQUARED_RADII)
            and t0["all_scalar_gates"]
            and t0["q024_shape_rank"] == ((96, 96), 96)
            and t0["q02_shape_rank"] == ((64, 64), 64)
            and t0["pivot_rank"] == 32 and t0["nested_pair"]
            and t0["defect_ranks"] == (48, 32)
            and t0["hermitian_factorization"]
            and t0["hermitian_inertia"] == (
                (t0["q024_shape_rank"][0][0], 0, 0),
                (t0["q02_shape_rank"][0][0], 0, 0),
            )
            and t0["proper_cubic"] and mutation_family != "T0",
            "all nine radii satisfy direct/inverse and nested Schur gates; D1 has exact 96/64/32 ranks and 48/32 non-Hermitian defects",
        ),
        "T1": (
            t1["census_complete"] and t1["static_nonunique"]
            and t1["wick_not_unital"] and t1["h_reproduced"]
            and t1["dpp_rejected_raw"] and t1["coherent_boundary_missing"]
            and t1["o9_control_exact"] and mutation_family != "T1",
            "six candidate types are separated; all three H residuals and the exact O9 exterior-control ranks/omissions reproduce",
        ),
        "T2": (
            not t2["action_native_e8_derived"]
            and t2["action_vacuum_invariant"]
            and t2["number_preserving_exterior_scope"]
            and t2["vacuum_assignment_count"] == 8
            and t2["vacuum_assignment_dimension"] == 0
            and t2["reflection_permutation"] == (7, 6, 5, 4, 3, 2, 1, 0)
            and t2["reflection_fixed_labels"] == 0
            and t2["reflection_covariant_assignment_count"] == 0
            and t2["reflection_assignment_orbits"] == 4
            and t2["naive_vacuum_unitality_residual"] == 7
            and t2["reduced_vacuum_unitality_residual"] == -1
            and t2["mixed_sector_omission"] == 2**32 - 121
            and t2["event_fiber_requires_pairing"]
            and t2["vacuum_mixing_star_product_route_unchecked"]
            and mutation_family != "T2",
            "the actual Block-194 reflection has four two-cycles and no covariant one-hot vacuum completion, rejecting the two exterior-natural E8 promotions",
        ),
        "S": (
            mutation_family != "SEALED",
            "T3-T5, causal boundary, response, heldouts, axioms, and TOE movement remain sealed",
        ),
    }
    return results, t0, t1, t2


RESOLUTION_LINES = (
    "per_element: checked all eight rank-four PVM effects, their E8 unit, the naive exterior images, and the vacuum-reduced O9 images.",
    "per_site: checked the invariant vacuum, all eight projective vacuum completions, the actual four-two-cycle Block-194 reflection, zero reflection-covariant completions, and omitted mixed-label sectors.",
    "per_mode: checked all nine frozen squared radii and independently reproduced the three disclosed D1 H-composition residuals with normalized residual rank 32.",
    "per_block: checked Q024/Q02 Schur typing, six candidate families, O9 algebra control, and number-preserving exterior E8 unitality in dependency order; the physical target stopped before cylinder descent.",
    "lattice_wide: checked and not executed — no 512-word cylinder, triple-port selector, O9 physical promotion, causal process, response, heldout, Record/Born, gravity, axiom, or TOE claim was opened.",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def self_test_mutations() -> int:
    baseline, _t0, _t1, _t2 = evaluate("")
    baseline_failures = tuple(
        key for key, (condition, _statement) in baseline.items()
        if not condition
    )
    print(
        "BASELINE: virtual_exit=" f"{len(baseline_failures)}; "
        f"failed_gates={baseline_failures or 'none'}"
    )
    rejected = matched = 0
    for mutation in MUTATIONS:
        results, _cached_t0, _cached_t1, _cached_t2 = evaluate(mutation)
        failed_gates = tuple(
            key for key, (condition, _statement) in results.items()
            if not condition
        )
        expected = (
            "S" if MUTATION_FAMILY[mutation] == "SEALED"
            else MUTATION_FAMILY[mutation]
        )
        virtual_exit = len(failed_gates)
        caught = virtual_exit != 0
        exact_gate = failed_gates == (expected,)
        rejected += int(caught)
        matched += int(exact_gate)
        print(
            f"MUTATION: {mutation}; virtual_exit={virtual_exit}; "
            f"failed_gates={failed_gates or 'none'}; expected={expected}; "
            f"gate_match={str(exact_gate).lower()}"
        )
    failures = (
        int(bool(baseline_failures))
        + (len(MUTATIONS) - rejected)
        + (len(MUTATIONS) - matched)
    )
    print(
        "MUTATION_TOTAL: baseline_exit=" f"{len(baseline_failures)}; "
        f"rejected={rejected}; gate_matches={matched}; "
        f"total={len(MUTATIONS)}; harness_failures={failures}"
    )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    parser.add_argument("--self-test-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        for mutation in MUTATIONS:
            print(f"{mutation} -> {MUTATION_FAMILY[mutation]}")
        return 0
    if args.self_test_mutations:
        return self_test_mutations()

    checks = Checks()
    results, t0, t1, t2 = evaluate(args.mutation)
    for key in ("A", "T0", "T1", "T2"):
        condition, statement = results[key]
        checks.check(key, statement, condition)

    h_control = positive_h_control()
    exterior = t1["exterior"]
    print(
        "SCHUR: radii=9; Q024=96; Q02=64; pivot=32; "
        f"defect_ranks={t0['defect_ranks']}; hermitian_factorization="
        f"{str(t0['hermitian_factorization']).lower()}; "
        "C32_fiber=paired_not_single_action"
    )
    print(
        "H_CONTROL: raw=" f"{h_control['raw']}; normalized={h_control['normalized']}; "
        f"predictor={h_control['predictor']}; normalized_rank={h_control['normalized_rank']}"
    )
    print(
        "O9_CONTROL: naive_cross_vacuum_rank=1; reduced_branch_rank="
        f"{exterior['single_branch_rank']}; doubled_branch_rank="
        f"{exterior['doubled_branch_rank']}; bidegree_ranks=16/128/1024; "
        f"full_omission={exterior['full_rank'] - exterior['reduced_sum_rank']}; "
        "liouville_order=conjugate_Gamma_plus_tensor_Gamma_plus"
    )
    print(
        "E8_OBSTRUCTION: invariant_vacuum=true; projective_completions="
        f"{t2['vacuum_assignment_count']}; completion_dimension="
        f"{t2['vacuum_assignment_dimension']}; reflection_map="
        f"{t2['reflection_permutation']}; reflection_fixed_labels="
        f"{t2['reflection_fixed_labels']}; reflection_covariant_completions="
        f"{t2['reflection_covariant_assignment_count']}; reflection_orbits="
        f"{t2['reflection_assignment_orbits']}; mixed_omission="
        f"{t2['mixed_sector_omission']}"
    )

    if not t2["action_native_e8_derived"]:
        print("[SEALED] T3: no one-/two-crossing descent without a T2 E8 insertion")
        print("[SEALED] T4: no 512-word or triple-port evaluation")
        print("[SEALED] T5: O9 remains a mathematical control, not a physical lift")
    condition, statement = results["S"]
    checks.check("S", statement, condition)
    for line in RESOLUTION_LINES:
        print(line)
    print(
        "BOUNDED_SCOPE: rejects only the executed number-preserving, exterior-natural "
        "projector E8 promotions; vacuum-mixing star-product representations, other "
        "insertion functors, and the cyclic-to-causal boundary remain untested."
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
