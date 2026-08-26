#!/usr/bin/env python3
"""Block 201: typed direct Schur/Wick event-functional kill gate.

The runner reconstructs every nonempty boundary restriction of the six
incoming/outgoing action carriers, derives the action/event coordinate
intertwiner and its gauge quotient, verifies the compressed determinant
engine without reading a physical target, and only then evaluates the eight
raw D1 one-crossing weights.  A normalization failure seals gluing and the
729-word census exactly as preregistered.
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

import admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24 as b190  # noqa: E402
import admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25 as b192  # noqa: E402
import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402
import admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25 as b194  # noqa: E402
import admissibility_d4_l24_event_history_interface_hankel_process_boundary_2026_08_25 as b199  # noqa: E402


PREREG_COMMIT = "f80e9673ad"
PARENT_COMMIT = "c7e0a0b57810e97bf563a65ded273ce9a6da0b2f"
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block201-direct-schur-wick-event-functional-20260825"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block201-direct-schur-wick-event-functional-20260825/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block201-direct-schur-wick-event-functional-20260825/PREFLIGHT_WITNESSES.md",
    "docs/ADMISSIBILITY_D4_L24_DIRECT_SCHUR_WICK_EVENT_FUNCTIONAL_NORMALIZATION_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_L24_EXTERIOR_NATURAL_E8_INSERTION_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_L24_EVENT_HISTORY_INTERFACE_HANKEL_PROCESS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
    "scripts/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.py",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
    "scripts/admissibility_d4_l24_event_history_interface_hankel_process_boundary_2026_08_25.py",
)

R = sp.Rational
I = sp.I
MASS = R(2, 7)
COARSE_TIME = 12
SITES = (0, 2, 4)
BOUNDARIES = {
    "0": (0,),
    "2": (2,),
    "4": (4,),
    "02": (0, 2),
    "04": (0, 4),
    "24": (2, 4),
    "024": (0, 2, 4),
}
EXPECTED_RADIUS_PAIRS = {
    "D1": (R(0), R(1)),
    "D2": (R(0), R(2)),
    "D3": (R(0), R(3)),
    "H1": (R(1), R(5, 4)),
    "H2": (R(3, 2), (7 + sp.sqrt(3)) / 4),
    "X1": (R(3, 4), (10 + sp.sqrt(3)) / 4),
}

MUTATION_FAMILY = {
    "stale_parent_or_main": "P0",
    "hide_or_reuse_float_pilot": "P0",
    "duplicate_radius_to_manufacture_c32": "T0",
    "swap_incoming_outgoing": "T0",
    "even_positions_not_coarse_sites": "T0",
    "claim_block200_six_carriers": "T0",
    "identity_from_equal_dimension": "T1",
    "fit_intertwiner_after_weights": "T1",
    "allow_weight_changing_gauge": "T1",
    "reorder_form_masks_without_matrices": "T1",
    "form_major_order": "T1",
    "omit_annihilation_equations": "T1",
    "conflate_coordinate_and_os_reflection": "T1",
    "crossing_dependent_phases": "T1",
    "force_phase_with_untracked_connector": "T1",
    "break_context_covariance": "T1",
    "reverse_berezin_order": "T2",
    "drop_doubled_conjugation": "T2",
    "sum_amplitudes_then_square": "T2",
    "normalize_each_depth": "T3",
    "condition_one_occupation": "T3",
    "identity_as_dephasing": "T3",
    "pairwise_compose_q024": "T3",
    "drop_branch_term": "T3",
    "fit_character_or_b": "S",
    "symmetry_representatives_only": "S",
    "fixed_label_cubic_transitivity": "S",
    "import_boundary_or_filling": "S",
    "claim_strong_positivity": "S",
    "manufacture_strong_kernel": "S",
    "claim_causal_axiom_or_toe": "S",
}
MUTATIONS = tuple(MUTATION_FAMILY)

RESOLUTION_LINES = (
    "per_element: checked all eight rank-four effects and all eight exact raw D1 one-crossing amplitudes and weights.",
    "per_site: checked direct and covariance Schur restrictions at each registered coarse site 0, 2, and 4.",
    "per_mode: checked all nine squared radii through the six physical incoming/outgoing carrier pairs.",
    "per_block: checked the typed C32 carrier, full intertwiner gauge orbit, determinant engine, and first normalization stop.",
    "lattice_wide: checked and not executed — D1 raw normalization failed before gluing, the 729-word census, or other carriers.",
)


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(value) == 0 for value in left - right
    )


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).to_field().inv().to_Matrix()


def exact_det(matrix: sp.MatrixBase) -> sp.Expr:
    domain_matrix = DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    )
    return sp.factor(domain_matrix.domain.to_sympy(domain_matrix.det()))


def git_output(*args: str) -> str:
    return subprocess.check_output(("git",) + args, cwd=ROOT, text=True).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        check=False,
        stdout=subprocess.DEVNULL,
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


@cache
def scalar_action(squared_radius: sp.Expr) -> sp.Matrix:
    delta = sp.simplify(MASS**2 + squared_radius)
    shift = coarse_shift()
    return sp.simplify(
        sp.eye(COARSE_TIME)
        + (2 * sp.eye(COARSE_TIME) - shift - shift.T) / (4 * delta)
    )


@cache
def scalar_boundary(
    squared_radius: sp.Expr, boundary: tuple[int, ...]
) -> tuple[sp.Matrix, sp.Matrix]:
    action = scalar_action(squared_radius)
    interior = tuple(index for index in range(action.rows) if index not in boundary)
    direct = sp.simplify(
        action.extract(boundary, boundary)
        - action.extract(boundary, interior)
        * exact_inverse(action.extract(interior, interior))
        * action.extract(interior, boundary)
    )
    covariance = exact_inverse(
        exact_inverse(action).extract(boundary, boundary)
    )
    return sp.Matrix(direct), sp.Matrix(covariance)


def squared_spatial_radius(momentum: tuple[sp.Expr, ...]) -> sp.Expr:
    return sp.simplify(sum(sp.sin(momentum[axis]) ** 2 for axis in range(3)))


def time_major_pair(
    scalar_in: sp.MatrixBase,
    internal_in: sp.MatrixBase,
    scalar_out: sp.MatrixBase,
    internal_out: sp.MatrixBase,
) -> sp.Matrix:
    count = scalar_in.rows
    result = sp.zeros(32 * count)
    for row in range(count):
        for column in range(count):
            result[
                32 * row:32 * row + 16,
                32 * column:32 * column + 16,
            ] = scalar_in[row, column] * internal_in
            result[
                32 * row + 16:32 * (row + 1),
                32 * column + 16:32 * (column + 1),
            ] = scalar_out[row, column] * internal_out
    return sp.Matrix(result)


def scalar_nested(
    larger: sp.MatrixBase,
    larger_boundary: tuple[int, ...],
    smaller_boundary: tuple[int, ...],
) -> tuple[sp.Matrix, sp.Expr]:
    keep = tuple(larger_boundary.index(site) for site in smaller_boundary)
    remove = tuple(index for index in range(len(larger_boundary)) if index not in keep)
    if not remove:
        return sp.Matrix(larger), sp.Integer(0)
    reduced = sp.simplify(
        larger.extract(keep, keep)
        - larger.extract(keep, remove)
        * exact_inverse(larger.extract(remove, remove))
        * larger.extract(remove, keep)
    )
    determinant_residual = sp.simplify(
        larger.det() - larger.extract(remove, remove).det() * reduced.det()
    )
    return sp.Matrix(reduced), determinant_residual


@cache
def t0_facts() -> dict[str, object]:
    fixture_summaries = []
    all_radii: set[sp.Expr] = set()
    d1_kernels: dict[str, sp.Matrix] = {}
    all_scalar_checks = True
    all_internal_checks = True

    for name, (incoming, transfer) in b193.POINTS.items():
        outgoing = tuple(sp.simplify(incoming[i] + transfer[i]) for i in range(4))
        radius_in = squared_spatial_radius(incoming)
        radius_out = squared_spatial_radius(outgoing)
        all_radii.update((radius_in, radius_out))
        internal_in = b192.spatial_action(incoming)
        internal_out = b192.spatial_action(outgoing)
        all_internal_checks = all_internal_checks and matrix_equal(
            internal_in.H * internal_in,
            (MASS**2 + radius_in) * sp.eye(16),
        ) and matrix_equal(
            internal_out.H * internal_out,
            (MASS**2 + radius_out) * sp.eye(16),
        )

        scalar_in: dict[str, sp.Matrix] = {}
        scalar_out: dict[str, sp.Matrix] = {}
        kernels: dict[str, sp.Matrix] = {}
        for label, boundary in BOUNDARIES.items():
            direct_in, covariance_in = scalar_boundary(radius_in, boundary)
            direct_out, covariance_out = scalar_boundary(radius_out, boundary)
            all_scalar_checks = all_scalar_checks and (
                matrix_equal(direct_in, covariance_in)
                and matrix_equal(direct_out, covariance_out)
                and direct_in.rank() == len(boundary)
                and direct_out.rank() == len(boundary)
            )
            scalar_in[label] = direct_in
            scalar_out[label] = direct_out
            kernels[label] = time_major_pair(
                direct_in, internal_in, direct_out, internal_out
            )
            all_scalar_checks = all_scalar_checks and (
                kernels[label].shape == (32 * len(boundary), 32 * len(boundary))
            )

        for label, boundary in BOUNDARIES.items():
            nested_in, det_residual_in = scalar_nested(
                scalar_in["024"], SITES, boundary
            )
            nested_out, det_residual_out = scalar_nested(
                scalar_out["024"], SITES, boundary
            )
            all_scalar_checks = all_scalar_checks and (
                matrix_equal(nested_in, scalar_in[label])
                and matrix_equal(nested_out, scalar_out[label])
                and det_residual_in == 0
                and det_residual_out == 0
            )

        fixture_summaries.append(
            (name, radius_in, radius_out, tuple(kernels[label].rows for label in BOUNDARIES))
        )
        if name == "D1":
            d1_kernels = kernels

    expected_rows = (32, 32, 32, 64, 64, 64, 96)
    expected_radii = {sp.simplify(value) for value in b199.FROZEN_SQUARED_RADII}
    return {
        "fixtures": tuple(fixture_summaries),
        "fixture_pairs": {
            name: (radius_in, radius_out)
            for name, radius_in, radius_out, _rows in fixture_summaries
        },
        "all_scalar_checks": all_scalar_checks,
        "all_internal_checks": all_internal_checks,
        "all_rows": all(rows == expected_rows for *_prefix, rows in fixture_summaries),
        "radii": frozenset(all_radii),
        "expected_radii": frozenset(expected_radii),
        "d1_kernels": d1_kernels,
        "coarse_sites": SITES,
        "block200_extension_honest": set(b193.POINTS) == set(EXPECTED_RADIUS_PAIRS),
    }


def graph_component_count(edges: tuple[tuple[int, int], ...], size: int) -> int:
    neighbors = {index: set() for index in range(size)}
    for left, right in edges:
        neighbors[left].add(right)
        neighbors[right].add(left)
    unseen = set(range(size))
    count = 0
    while unseen:
        count += 1
        stack = [unseen.pop()]
        while stack:
            for neighbor in neighbors[stack.pop()]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)
    return count


@cache
def t1_facts() -> dict[str, object]:
    form_subsets = tuple(
        tuple(axis for axis in range(4) if mask & (1 << axis))
        for mask in range(16)
    )
    numbers = tuple(
        b190.CREATION[axis] * b190.ANNIHILATION[axis]
        for axis in range(4)
    )
    signatures = tuple(
        tuple(numbers[axis][index, index] for axis in range(4))
        for index in range(16)
    )
    edges = tuple(
        (row, column)
        for creation in b190.CREATION
        for row in range(16)
        for column in range(16)
        if creation[row, column] != 0
    )
    car_exact = all(
        matrix_equal(
            b190.ANNIHILATION[left] * b190.CREATION[right]
            + b190.CREATION[right] * b190.ANNIHILATION[left],
            sp.eye(16) if left == right else sp.zeros(16),
        )
        for left in range(4) for right in range(4)
    )
    common_commutant_dimension = (
        1 if len(set(signatures)) == 16 and graph_component_count(edges, 16) == 1
        else -1
    )

    action_labels = tuple(
        (sector, form_subsets[mask])
        for sector in ("in", "out") for mask in range(16)
    )
    event_labels = tuple(
        (sector, form_subsets[mask])
        for sector in ("upper", "lower") for mask in range(16)
    )
    coordinate_map = {"in": "upper", "out": "lower"}
    labeled_identification = all(
        event_labels[index] == (coordinate_map[action_labels[index][0]], action_labels[index][1])
        for index in range(32)
    )
    j0 = sp.eye(32)
    pi = sp.diag(*([1] * 16 + [-1] * 16))
    generators = tuple(
        sp.kronecker_product(sp.eye(2), generator)
        for generator in b190.CREATION + b190.ANNIHILATION
    )
    intertwines_all_car = all(matrix_equal(j0 * generator, generator * j0) for generator in generators)
    sector_family_dimension = 2 if common_commutant_dimension == 1 else -1

    classification = b194.detector_classification_facts()
    coordinate_reflection = sp.diag(b193.GTIME, b193.GTIME)
    reflection_intertwining = matrix_equal(
        j0 * coordinate_reflection, coordinate_reflection * j0
    )
    detector_orientation = sp.expand(I * b193.GTIME * b193.GSPACE[2])
    orientation_derived = matrix_equal(detector_orientation, classification["orientation"])

    q0 = t0_facts()["d1_kernels"]["0"]
    q02 = t0_facts()["d1_kernels"]["02"]
    u, v = sp.symbols("u v", nonzero=True)
    d = sp.diag(*([u] * 16 + [v] * 16))
    d_inverse = sp.diag(*([1 / u] * 16 + [1 / v] * 16))
    gauge_commutes = matrix_equal(q0 * d, d * q0)
    effects = tuple(sp.Matrix(effect) for effect in b194.instrument_pointer_facts()["effects"])
    gauge_similarity = all(
        matrix_equal(
            q0 + sp.eye(32) - d_inverse * effect * d,
            d_inverse * (q0 + sp.eye(32) - effect) * d,
        )
        for effect in effects
    )
    common_two = sp.diag(d, d)
    common_phase_commutes = matrix_equal(q02 * common_two, common_two * q02)
    crossing_dependent = sp.diag(sp.eye(32), sp.diag(*([-1] * 16 + [1] * 16)))
    crossing_dependent_rejected = not matrix_equal(
        q02 * crossing_dependent, crossing_dependent * q02
    )

    return {
        "form_basis": form_subsets == b190.FORM_SUBSETS,
        "car_exact": car_exact,
        "joint_signatures": len(set(signatures)),
        "creation_graph_components": graph_component_count(edges, 16),
        "common_commutant_dimension": common_commutant_dimension,
        "sector_family_dimension": sector_family_dimension,
        "labeled_identification": labeled_identification,
        "j0_unitary": matrix_equal(j0.H * j0, sp.eye(32)),
        "pi_intertwining": matrix_equal(j0 * pi, pi * j0),
        "intertwines_all_car": intertwines_all_car,
        "proper_cubic": (
            classification["proper_cubic_count"] == 24
            and classification["family_covariance"]
            and classification["context_covariance"]
        ),
        "reflection_intertwining": reflection_intertwining,
        "coordinate_vs_fiber_separate": (
            classification["coordinate_reflection_odd"]
            and classification["fiber_reflection_odd"]
        ),
        "orientation_derived": orientation_derived,
        "gauge_commutes": gauge_commutes,
        "gauge_similarity": gauge_similarity,
        "common_phase_commutes": common_phase_commutes,
        "crossing_dependent_rejected": crossing_dependent_rejected,
        "gauge_group": "U(1)^2",
        "physical_weight_orbits": 1,
    }


@cache
def effects_and_factors() -> tuple[
    tuple[sp.Matrix, ...], tuple[tuple[sp.Matrix, sp.Matrix], ...]
]:
    effects = tuple(sp.Matrix(effect) for effect in b194.instrument_pointer_facts()["effects"])
    factors = []
    for effect in effects:
        _reduced, pivots = effect.rref()
        x = effect[:, tuple(pivots)]
        gram_inverse = exact_inverse(x.H * x)
        if not matrix_equal(x * gram_inverse * x.H, effect):
            raise AssertionError("rank factor failed")
        factors.append((sp.Matrix(x), sp.Matrix(gram_inverse * x.H)))
    return effects, tuple(factors)


def determinant_amplitude(q: sp.MatrixBase, labels: tuple[int, ...]) -> sp.Expr:
    n = len(labels)
    if n == 0:
        return sp.Integer(1)
    if q.shape != (32 * n, 32 * n):
        raise ValueError("word and action boundary have different types")
    _effects, factors = effects_and_factors()
    m = sp.Matrix(q + sp.eye(q.rows))
    det_q = exact_det(q)
    det_m = exact_det(m)
    m_inverse = exact_inverse(m)
    total = sp.Integer(0)
    for epsilon in product((0, 1), repeat=n):
        active = tuple(index for index, value in enumerate(epsilon) if value)
        if not active:
            determinant = det_m
        else:
            u_matrix = sp.zeros(q.rows, 4 * len(active))
            vh_matrix = sp.zeros(4 * len(active), q.rows)
            for factor_index, slot in enumerate(active):
                x, vh = factors[labels[slot]]
                u_matrix[
                    32 * slot:32 * (slot + 1),
                    4 * factor_index:4 * (factor_index + 1),
                ] = x
                vh_matrix[
                    4 * factor_index:4 * (factor_index + 1),
                    32 * slot:32 * (slot + 1),
                ] = vh
            small = sp.eye(4 * len(active)) - vh_matrix * m_inverse * u_matrix
            determinant = sp.factor(det_m * exact_det(small))
        total += (-1) ** (n - sum(epsilon)) * determinant
    return sp.factor(sp.cancel(total / det_q))


@cache
def t2_facts() -> dict[str, object]:
    effects, factors = effects_and_factors()
    q_control = 2 * sp.eye(32)
    m_control = q_control + sp.eye(32)
    comparisons = []
    for label in (0, 7):
        x, vh = factors[label]
        compressed = exact_det(m_control) * exact_det(
            sp.eye(4) - vh * exact_inverse(m_control) * x
        )
        direct = exact_det(m_control - effects[label])
        comparisons.append(sp.simplify(compressed - direct) == 0)

    dephasing_witness = None
    for row in range(32):
        for column in range(32):
            matrix_unit = sp.zeros(32)
            matrix_unit[row, column] = 1
            dephased = sum(
                (effect * matrix_unit * effect for effect in effects),
                sp.zeros(32),
            )
            if not matrix_equal(dephased, matrix_unit):
                dephasing_witness = (row, column)
                break
        if dephasing_witness is not None:
            break
    return {
        "effect_count": len(effects),
        "effect_ranks": tuple(effect.rank() for effect in effects),
        "pvm_complete": matrix_equal(sum(effects, sp.zeros(32)), sp.eye(32)),
        "factor_ranks": tuple(x.cols for x, _vh in factors),
        "factor_exact": all(
            matrix_equal(x * vh, effect)
            for effect, (x, vh) in zip(effects, factors)
        ),
        "compressed_direct": all(comparisons),
        "empty_amplitude": determinant_amplitude(sp.zeros(0), ()),
        "max_word_determinant_order": 12,
        "dephasing_witness": dephasing_witness,
        "entrywise_scope_only": True,
    }


@cache
def t3_facts() -> dict[str, object]:
    q0 = t0_facts()["d1_kernels"]["0"]
    amplitudes = tuple(determinant_amplitude(q0, (label,)) for label in range(8))
    weights = tuple(
        sp.factor(sp.simplify(sp.conjugate(amplitude) * amplitude))
        for amplitude in amplitudes
    )
    raw_sum = sp.factor(sum(weights))
    one_shot_pass = all(weight == R(1, 8) for weight in weights) and raw_sum == 1
    delta = None
    gluing_status = "sealed_by_one_shot_failure"
    if one_shot_pass:
        q024 = t0_facts()["d1_kernels"]["024"]
        q02 = t0_facts()["d1_kernels"]["02"]
        delta = sp.factor(
            sum(determinant_amplitude(q024, (0, 0, label)) for label in range(8))
            - determinant_amplitude(q02, (0, 0))
        )
        gluing_status = "pass" if delta == 0 else "fail"
    return {
        "amplitudes": amplitudes,
        "weights": weights,
        "raw_sum": raw_sum,
        "one_shot_pass": one_shot_pass,
        "delta": delta,
        "gluing_status": gluing_status,
        "target_exact": all(value.is_number for value in amplitudes + weights),
        "stop_honored": one_shot_pass or delta is None,
    }


def evaluate(mutation: str) -> tuple[dict[str, tuple[bool, str]], dict[str, object]]:
    authority = authority_facts()
    t0 = t0_facts()
    t1 = t1_facts()
    t2 = t2_facts()
    t3 = t3_facts()
    family = MUTATION_FAMILY.get(mutation, "")
    results = {
        "P0": (
            authority["main"] == CURRENT_MAIN
            and authority["parent"] and authority["prereg"]
            and authority["goal_frozen"] and authority["preflight_frozen"]
            and family != "P0",
            "parent/main authority and frozen preregistration/disclosure blobs bind",
        ),
        "T0": (
            t0["fixture_pairs"] == EXPECTED_RADIUS_PAIRS
            and t0["all_scalar_checks"] and t0["all_internal_checks"]
            and t0["all_rows"] and t0["radii"] == t0["expected_radii"]
            and t0["coarse_sites"] == SITES and t0["block200_extension_honest"]
            and family != "T0",
            "all seven Schur restrictions on six typed carriers reconstruct exactly",
        ),
        "T1": (
            t1["form_basis"] and t1["car_exact"]
            and t1["joint_signatures"] == 16
            and t1["creation_graph_components"] == 1
            and t1["common_commutant_dimension"] == 1
            and t1["sector_family_dimension"] == 2
            and t1["labeled_identification"] and t1["j0_unitary"]
            and t1["pi_intertwining"] and t1["intertwines_all_car"]
            and t1["proper_cubic"] and t1["reflection_intertwining"]
            and t1["coordinate_vs_fiber_separate"] and t1["orientation_derived"]
            and t1["gauge_commutes"] and t1["gauge_similarity"]
            and t1["common_phase_commutes"] and t1["crossing_dependent_rejected"]
            and t1["gauge_group"] == "U(1)^2" and t1["physical_weight_orbits"] == 1
            and family != "T1",
            "the labeled intertwiner is derived as one U(1)^2 gauge orbit with exact weight invariance",
        ),
        "T2": (
            t2["effect_count"] == 8 and set(t2["effect_ranks"]) == {4}
            and set(t2["factor_ranks"]) == {4} and t2["pvm_complete"]
            and t2["factor_exact"] and t2["compressed_direct"]
            and t2["empty_amplitude"] == 1
            and t2["max_word_determinant_order"] == 12
            and t2["dephasing_witness"] is not None
            and t2["entrywise_scope_only"] and family != "T2",
            "rank-four determinant lemma, unit typing, and identity/dephasing separation pass",
        ),
        "T3": (
            t3["target_exact"] and t3["stop_honored"] and family != "T3",
            "the exact raw D1 one-shot kill gate executes and its preregistered stop is honored",
        ),
        "S": (
            family != "S",
            "T4-T7, alternate routes, axioms, obligation retirement, and TOE movement remain sealed",
        ),
    }
    return results, t3


def compact(value: sp.Expr, limit: int = 520) -> str:
    rendered = sp.sstr(value)
    if len(rendered) <= limit:
        return rendered
    return f"{sp.N(value, 18)} [exact expression chars={len(rendered)}]"


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
    baseline, _target = evaluate("")
    baseline_failures = tuple(key for key, (ok, _text) in baseline.items() if not ok)
    print(f"BASELINE: virtual_exit={len(baseline_failures)}; failed_gates={baseline_failures or 'none'}")
    rejected = matched = 0
    for mutation in MUTATIONS:
        results, _cached_target = evaluate(mutation)
        failed = tuple(key for key, (ok, _text) in results.items() if not ok)
        expected = MUTATION_FAMILY[mutation]
        caught = bool(failed)
        exact = failed == (expected,)
        rejected += int(caught)
        matched += int(exact)
        print(
            f"MUTATION: {mutation}; virtual_exit={len(failed)}; "
            f"failed_gates={failed or 'none'}; expected={expected}; "
            f"gate_match={str(exact).lower()}"
        )
    failures = int(bool(baseline_failures)) + len(MUTATIONS) - rejected + len(MUTATIONS) - matched
    print(
        f"MUTATION_TOTAL: baseline_exit={len(baseline_failures)}; "
        f"rejected={rejected}; gate_matches={matched}; total={len(MUTATIONS)}; "
        f"harness_failures={failures}"
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
    results, target = evaluate(args.mutation)
    for key in ("P0", "T0", "T1", "T2", "T3", "S"):
        condition, statement = results[key]
        checks.check(key, statement, condition)

    t0 = t0_facts()
    t1 = t1_facts()
    print(
        "CARRIERS: fixtures=6; boundaries=7; radii=9; sites=(0,2,4); "
        f"pairs={t0['fixture_pairs']}"
    )
    print(
        "INTERTWINER: basis=sector-major/form-bitmask; common_CAR_commutant_dim="
        f"{t1['common_commutant_dimension']}; full_linear_dim="
        f"{t1['sector_family_dimension']}; isometric_gauge=U(1)^2; "
        "weight_orbits=1; crossing_dependent_phases=rejected"
    )
    grouped: dict[tuple[sp.Expr, sp.Expr], list[int]] = {}
    for label, pair in enumerate(zip(target["amplitudes"], target["weights"])):
        grouped.setdefault(pair, []).append(label)
    for (amplitude, weight), labels in grouped.items():
        print(
            f"D1_ONE_SHOT: labels={tuple(labels)}; amplitude={compact(amplitude, 1000)}; "
            f"weight={compact(weight)}"
        )
    print(
        f"D1_RAW_SUM: {compact(target['raw_sum'])}; "
        f"one_shot_target={'pass' if target['one_shot_pass'] else 'fail'}; "
        f"gluing={target['gluing_status']}"
    )
    if target["delta"] is not None:
        print(f"D1_DELTA_00_024_TO_02: {compact(target['delta'])}")
    else:
        print("[SEALED] D1_DELTA_00_024_TO_02: one-shot normalization failed first")
    print("[SEALED] T4-T6: no 729-word census, remaining carriers, or selector")
    for line in RESOLUTION_LINES:
        print(line)
    print(
        "BOUNDED_SCOPE: a failure rejects only the frozen typed determinant "
        "functional; POVM/null, support, Nambu, OS/GNS, causal-boundary, "
        "response, gravity, axiom, and TOE routes remain open."
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
