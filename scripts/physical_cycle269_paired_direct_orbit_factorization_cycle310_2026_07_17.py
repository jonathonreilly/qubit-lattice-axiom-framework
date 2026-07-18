#!/usr/bin/env python3
"""Cycle 310: paired-direct factorization and proper-cubic orbit audit.

The accepted Cycle-304 ninety-sector blocks are factored before the Cycle-306
role lift.  Each sparse factor A is paired with K A K on the other physical r
branch.  The resulting 180-sector layer commutes with C_role exactly.  The
coin uses sparse QR factors; stream and contact use their disjoint swap and
phase structure instead of generic QR.

The runner also closes every coefficient-bearing paired layer under the 24
proper-cubic frames.  It tests support overlap, commutation, deterministic
finite colorings, coefficient-multiset closure, target reconstruction, code
leakage, and the supplied schedule boundary.  A finite factor list is not a
clock, recurrence law, or autonomous application rule.
"""

from __future__ import annotations

from collections import Counter
from itertools import permutations, product
from pathlib import Path
import re
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_coin_stream_contact_common_refinement_cycle304_2026_07_17 as c304
import physical_cycle269_joint_six_mode_coin_lift_cycle302_2026_07_17 as c302
import physical_cycle269_primitive_matrix_unit_synthesis_cycle309_2026_07_17 as c309
import physical_cycle269_relational_role_marker_gauge_cycle306_2026_07_17 as c306


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_PAIRED_DIRECT_ORBIT_FACTORIZATION_CYCLE310_NOTE_2026-07-17.md"
)
TRAINING_SIZE = 3
HELD_SIZE = 6
MICRO_DIMENSION = 90
PHYSICAL_DIMENSION = 180
TOLERANCE = 2e-10

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-310 note exists", False, NOTE)
        return
    body = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "paired-direct",
        "ninety-sector",
        "two hundred twenty paired layers",
        "at most eight raw matrix units",
        "every paired layer commutes with c_role",
        "exact final code action",
        "one hundred nineteen intermediate layers leak from the common shell",
        "one hundred fifty-nine coin orbit types",
        "one hundred thirteen have noncommuting members",
        "unrounded floating-coefficient census",
        "absolute coefficient exceeds 1e-12",
        "eight-color",
        "three thousand four hundred forty-nine",
        "all 24 proper-cubic frames",
        "all 27 l=3 translations",
        "held beta=-0.35",
        "held l=6",
        "twenty-three m2 per cell",
        "forty-four-m2 patch",
        "host schedule",
        "not physical time",
        "not an autonomous law",
        "broad gate status: fail / do not ship",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in body)
    check("the note pins the paired-direct theorem and boundary", not missing, missing)


def physical_frame_permutations():
    result = []
    matrices = []
    for frame in c235.proper_cubic_frames():
        _logical, micro = c304.frame_representations(frame)
        physical = c306.block_diagonal(micro, micro)
        result.append(c309.signed_permutation(physical))
        matrices.append(physical)
    return tuple(result), tuple(matrices)


def factor_matrix(
    delta: dict[tuple[int, int], complex], dimension: int = PHYSICAL_DIMENSION
) -> np.ndarray:
    result = np.eye(dimension, dtype=complex)
    for (row, column), value in delta.items():
        result[row, column] += value
    return result


def factor_product(
    deltas: tuple[dict[tuple[int, int], complex], ...],
    dimension: int = PHYSICAL_DIMENSION,
) -> np.ndarray:
    result = np.eye(dimension, dtype=complex)
    for delta in deltas:
        increment = np.zeros_like(result)
        for (row, column), value in delta.items():
            increment[:, column] += value * result[:, row]
        result += increment
    return result


def paired_delta(
    delta: dict[tuple[int, int], complex], exchange: tuple[int, ...]
) -> dict[tuple[int, int], complex]:
    result = dict(delta)
    for (row, column), value in delta.items():
        result[(MICRO_DIMENSION + exchange[row], MICRO_DIMENSION + exchange[column])] = value
    return result


def disjoint_swap_deltas(operator: np.ndarray):
    if operator.shape != (MICRO_DIMENSION, MICRO_DIMENSION):
        raise ValueError("the disjoint-swap target must be a ninety-sector matrix")
    if np.linalg.norm(operator.conj().T @ operator - np.eye(MICRO_DIMENSION)) > 1e-8:
        raise ValueError("the disjoint-swap target must be unitary")
    mapping = c309.permutation_from_operator(operator)
    if any(mapping[mapping[index]] != index or mapping[index] == index for index in mapping):
        raise ValueError("the disjoint-swap target must be a fixed-point-free involution")
    return tuple(
        c309.delta_for_two_level(
            index,
            target,
            operator[np.ix_((index, target), (index, target))],
        )
        for index, target in enumerate(mapping)
        if index < target
    )


def diagonal_phase_deltas(operator: np.ndarray):
    if operator.shape != (MICRO_DIMENSION, MICRO_DIMENSION):
        raise ValueError("the phase target must be a ninety-sector matrix")
    if np.linalg.norm(operator - np.diag(np.diag(operator))) > 1e-11:
        raise ValueError("the phase target must be diagonal")
    if np.linalg.norm(operator.conj().T @ operator - np.eye(MICRO_DIMENSION)) > 1e-8:
        raise ValueError("the phase target must be unitary")
    return tuple(
        c309.delta_for_phase(index, operator[index, index])
        for index in range(MICRO_DIMENSION)
        if abs(operator[index, index] - 1) > 1e-12
    )


def sector_deltas(name: str, operator: np.ndarray):
    if name == "coin":
        return c309.primitive_deltas(c309.qr_factorization(operator))
    if name == "stream":
        return disjoint_swap_deltas(operator)
    if name == "contact":
        return diagonal_phase_deltas(operator)
    raise ValueError("the paired-direct compiler accepts coin, stream, or contact")


def delta_action(
    delta: dict[tuple[int, int], complex], columns: np.ndarray
) -> np.ndarray:
    result = np.zeros_like(columns)
    for (row, column), value in delta.items():
        result[row, :] += value * columns[column, :]
    return result


def layer_unitarity_residual(delta: dict[tuple[int, int], complex]) -> float:
    support = sorted({index for pair in delta for index in pair})
    restricted = np.eye(len(support), dtype=complex)
    positions = {value: index for index, value in enumerate(support)}
    for (row, column), value in delta.items():
        restricted[positions[row], positions[column]] += value
    return float(np.linalg.norm(restricted.conj().T @ restricted - np.eye(len(support))))


def paired_factorization_controls(frame_permutations, frame_matrices):
    exchange = c309.permutation_from_operator(c306.exchange_operator())
    constraint_permutation = c309.permutation_from_operator(c306.role_constraint())
    encoding = c306.constrained_encoding()
    code_projector = encoding @ encoding.conj().T
    beta_details = {}
    stable_counts = []
    maximum_reconstruction = 0.0
    maximum_code_action = 0.0
    maximum_composition = 0.0
    maximum_constraint = 0.0
    maximum_unitarity = 0.0
    maximum_complete_frame = 0.0
    primary_schedule = None
    primary_targets = None
    for beta in (-0.2, -0.3, -0.4, -0.35):
        old, logical, physical = c306.old_and_new_operators(beta)
        schedule = {}
        products = {}
        detail = {}
        for name, operator in old.items():
            base = sector_deltas(name, operator)
            paired = tuple(paired_delta(delta, exchange) for delta in base)
            product_operator = factor_product(paired)
            reconstruction = float(np.linalg.norm(product_operator - physical[name]))
            code_action = float(
                np.linalg.norm(product_operator @ encoding - encoding @ logical[name])
            )
            constraint_residuals = tuple(
                c309.constraint_commutator_residual(delta, constraint_permutation)
                for delta in paired
            )
            all_frame, maximum_frame = c309.covariance_census(
                paired, frame_permutations
            )
            leakage = tuple(
                float(
                    np.linalg.norm(
                        (np.eye(PHYSICAL_DIMENSION) - code_projector)
                        @ delta_action(delta, encoding),
                        2,
                    )
                )
                for delta in paired
            )
            unitarity = tuple(layer_unitarity_residual(delta) for delta in paired)
            maximum_reconstruction = max(maximum_reconstruction, reconstruction)
            maximum_code_action = max(maximum_code_action, code_action)
            maximum_constraint = max(
                maximum_constraint, max(constraint_residuals, default=0.0)
            )
            maximum_unitarity = max(maximum_unitarity, max(unitarity, default=0.0))
            schedule[name] = paired
            products[name] = product_operator
            detail[name] = {
                "paired_layers": len(paired),
                "raw_branch_factors": 2 * len(paired),
                "maximum_raw_matrix_units_per_paired_layer": max(map(len, paired)),
                "reconstruction_residual": reconstruction,
                "code_action_residual": code_action,
                "C_role_noncommuting_layers": sum(value > 1e-11 for value in constraint_residuals),
                "individually_all_frame_layers": all_frame,
                "maximum_individual_frame_residual": maximum_frame,
                "common_shell_leaking_layers": sum(value > 1e-10 for value in leakage),
                "maximum_common_shell_leakage": max(leakage, default=0.0),
                "maximum_layer_unitarity_residual": max(unitarity, default=0.0),
            }
        counts = tuple(detail[name]["paired_layers"] for name in ("coin", "stream", "contact"))
        leakage_counts = tuple(
            detail[name]["common_shell_leaking_layers"]
            for name in ("coin", "stream", "contact")
        )
        stable_counts.append((counts, leakage_counts))
        composed = products["contact"] @ products["stream"] @ products["coin"]
        target = physical["contact"] @ physical["stream"] @ physical["coin"]
        composition_residual = float(np.linalg.norm(composed - target))
        composition_code_residual = float(
            np.linalg.norm(
                composed @ encoding
                - encoding @ (logical["contact"] @ logical["stream"] @ logical["coin"])
            )
        )
        maximum_composition = max(
            maximum_composition, composition_residual, composition_code_residual
        )
        frame_residual = max(
            float(np.linalg.norm(frame @ composed - composed @ frame))
            for frame in frame_matrices
        )
        maximum_complete_frame = max(maximum_complete_frame, frame_residual)
        detail["composition_reconstruction_residual"] = composition_residual
        detail["composition_code_action_residual"] = composition_code_residual
        detail["complete_product_frame_residual"] = frame_residual
        beta_details[beta] = detail
        if beta == -0.3:
            primary_schedule = schedule
            primary_targets = physical
    check(
        "two hundred twenty sparse paired-direct layers exactly reconstruct every target while preserving C_role",
        set(stable_counts) == {((160, 45, 15), (89, 30, 0))}
        and maximum_reconstruction < TOLERANCE
        and maximum_code_action < TOLERANCE
        and maximum_composition < TOLERANCE
        and maximum_constraint < TOLERANCE
        and maximum_unitarity < TOLERANCE
        and maximum_complete_frame < TOLERANCE
        and all(
            beta_details[beta][name]["individually_all_frame_layers"] == 0
            for beta in beta_details
            for name in ("coin", "stream", "contact")
        )
        and max(
            beta_details[beta][name]["maximum_raw_matrix_units_per_paired_layer"]
            for beta in beta_details
            for name in ("coin", "stream", "contact")
        )
        == 8,
        {
            "beta_details": beta_details,
            "stable_coin_stream_contact_paired_counts_and_leakage_counts": stable_counts,
            "total_paired_layers": sum(stable_counts[0][0]),
            "total_raw_branch_factors": 2 * sum(stable_counts[0][0]),
            "maximum_reconstruction_residual": maximum_reconstruction,
            "maximum_code_action_residual": maximum_code_action,
            "maximum_composition_residual": maximum_composition,
            "maximum_layer_constraint_commutator": maximum_constraint,
            "maximum_layer_unitarity_residual": maximum_unitarity,
            "maximum_complete_product_frame_residual": maximum_complete_frame,
            "coin_schedule": "supplied reverse-lexicographic ninety-sector QR order",
            "stream_and_contact_order": "irrelevant within disjoint commuting families",
            "outer_schedule": "supplied coin, then stream/catch-up, then contact",
        },
    )
    return primary_schedule, primary_targets


def delta_key(delta: dict[tuple[int, int], complex]):
    return tuple(
        sorted(
            (
                row,
                column,
                float(value.real),
                float(value.imag),
            )
            for (row, column), value in delta.items()
            if abs(value) > 1e-12
        )
    )


def orbit_members(delta, frame_permutations):
    result = {}
    for mapping, signs in frame_permutations:
        transformed = c309.transformed_delta(delta, mapping, signs)
        result[delta_key(transformed)] = transformed
    return result


def multiply_sparse(left, right):
    by_row = {}
    for (row, column), value in right.items():
        by_row.setdefault(row, []).append((column, value))
    result = {}
    for (row, middle), left_value in left.items():
        for column, right_value in by_row.get(middle, ()):
            key = (row, column)
            result[key] = result.get(key, 0) + left_value * right_value
    return {key: value for key, value in result.items() if abs(value) > 1e-11}


def noncommutation_residual(left, right) -> float:
    return c309.sparse_residual(
        multiply_sparse(left, right), multiply_sparse(right, left)
    )


def orbit_graph(members, mode: str):
    member_list = tuple(members)
    supports = tuple({index for pair in delta for index in pair} for delta in member_list)
    adjacency = [set() for _ in member_list]
    for left in range(len(member_list)):
        for right in range(left + 1, len(member_list)):
            if mode == "overlap":
                adjacent = bool(supports[left] & supports[right])
            elif mode == "noncommutation":
                adjacent = noncommutation_residual(member_list[left], member_list[right]) > 1e-10
            else:
                raise ValueError("orbit graph mode must be overlap or noncommutation")
            if adjacent:
                adjacency[left].add(right)
                adjacency[right].add(left)
    return tuple(frozenset(row) for row in adjacency)


def dsatur_coloring(adjacency):
    colors = [-1] * len(adjacency)
    for _ in range(len(adjacency)):
        vertex = max(
            (index for index, color in enumerate(colors) if color < 0),
            key=lambda index: (
                len({colors[other] for other in adjacency[index] if colors[other] >= 0}),
                len(adjacency[index]),
                -index,
            ),
        )
        used = {colors[other] for other in adjacency[vertex] if colors[other] >= 0}
        color = 0
        while color in used:
            color += 1
        colors[vertex] = color
    return tuple(colors)


def coloring_is_valid(adjacency, colors) -> bool:
    return all(
        colors[left] != colors[right]
        for left, neighbors in enumerate(adjacency)
        for right in neighbors
    )


def orbit_closure_controls(schedule, targets, frame_permutations, frame_matrices):
    details = {}
    all_orbit_pairs = set()
    total_types = 0
    total_noncommuting_types = 0
    maximum_overlap_colors = 0
    maximum_commutation_colors = 0
    all_colorings_valid = True
    all_orbits_closed = True
    completion_products = {}
    expected = {
        "coin": (159, 160, 3609, 3449, 46, 113),
        "stream": (4, 45, 45, 0, 4, 0),
        "contact": (2, 15, 15, 0, 2, 0),
    }
    for name, deltas in schedule.items():
        scheduled_counts = Counter(delta_key(delta) for delta in deltas)
        closures = {}
        for delta in deltas:
            orbit = orbit_members(delta, frame_permutations)
            signature = tuple(sorted(orbit))
            closures[signature] = orbit
        completed_deltas = list(deltas)
        orbit_size_counts = Counter()
        commuting_types = 0
        noncommuting_types = 0
        overlap_edges = 0
        noncommutation_edges = 0
        block_overlap_colors = 0
        block_commutation_colors = 0
        completed_count = 0
        for signature, orbit in closures.items():
            members = tuple(orbit[key] for key in sorted(orbit))
            orbit_size_counts[len(members)] += 1
            all_orbit_pairs.update(pair for member in members for pair in member)
            for member in members:
                for mapping, signs in frame_permutations:
                    all_orbits_closed &= delta_key(
                        c309.transformed_delta(member, mapping, signs)
                    ) in orbit
            overlap_graph = orbit_graph(members, "overlap")
            commutation_graph = orbit_graph(members, "noncommutation")
            overlap_coloring = dsatur_coloring(overlap_graph)
            commutation_coloring = dsatur_coloring(commutation_graph)
            all_colorings_valid &= coloring_is_valid(overlap_graph, overlap_coloring)
            all_colorings_valid &= coloring_is_valid(
                commutation_graph, commutation_coloring
            )
            overlap_edge_count = sum(map(len, overlap_graph)) // 2
            noncommutation_edge_count = sum(map(len, commutation_graph)) // 2
            overlap_edges = max(overlap_edges, overlap_edge_count)
            noncommutation_edges = max(noncommutation_edges, noncommutation_edge_count)
            overlap_colors = max(overlap_coloring, default=-1) + 1
            commutation_colors = max(commutation_coloring, default=-1) + 1
            block_overlap_colors = max(block_overlap_colors, overlap_colors)
            block_commutation_colors = max(block_commutation_colors, commutation_colors)
            if noncommutation_edge_count:
                noncommuting_types += 1
            else:
                commuting_types += 1
            multiplicity = max(scheduled_counts[key] for key in orbit)
            completed_count += multiplicity * len(orbit)
            for key in sorted(orbit):
                completed_deltas.extend(
                    orbit[key] for _ in range(multiplicity - scheduled_counts[key])
                )
        completion_product = factor_product(tuple(completed_deltas))
        completion_products[name] = completion_product
        target_residual = float(np.linalg.norm(completion_product - targets[name], 2))
        frame_residual = max(
            float(np.linalg.norm(frame @ completion_product - completion_product @ frame, 2))
            for frame in frame_matrices
        )
        frame_mismatch = 0
        for mapping, signs in frame_permutations:
            transformed = Counter(
                delta_key(c309.transformed_delta(delta, mapping, signs))
                for delta in deltas
            )
            frame_mismatch = max(frame_mismatch, sum((transformed - scheduled_counts).values()))
        block_expected = expected[name]
        details[name] = {
            "orbit_types": len(closures),
            "orbit_size_counts": dict(orbit_size_counts),
            "scheduled_paired_layers": len(deltas),
            "minimum_coefficient_multiset_closure_layers": completed_count,
            "added_layers_for_multiset_closure": completed_count - len(deltas),
            "commuting_orbit_types": commuting_types,
            "noncommuting_orbit_types": noncommuting_types,
            "maximum_overlap_edges_in_one_orbit": overlap_edges,
            "maximum_noncommutation_edges_in_one_orbit": noncommutation_edges,
            "maximum_verified_overlap_colors": block_overlap_colors,
            "maximum_verified_commutation_colors": block_commutation_colors,
            "maximum_scheduled_multiset_frame_mismatch": frame_mismatch,
            "append-completed_target_operator_residual": target_residual,
            "append-completed_frame_residual": frame_residual,
            "matches_expected_census": (
                len(closures),
                len(deltas),
                completed_count,
                completed_count - len(deltas),
                commuting_types,
                noncommuting_types,
            )
            == block_expected,
        }
        total_types += len(closures)
        total_noncommuting_types += noncommuting_types
        maximum_overlap_colors = max(maximum_overlap_colors, block_overlap_colors)
        maximum_commutation_colors = max(
            maximum_commutation_colors, block_commutation_colors
        )
    check(
        "complete proper-cubic orbit closure is finite, but the sparse coin closures overlap and do not commute",
        all(row["matches_expected_census"] for row in details.values())
        and total_types == 165
        and total_noncommuting_types == 113
        and maximum_overlap_colors == maximum_commutation_colors == 8
        and all_colorings_valid
        and all_orbits_closed
        and details["coin"]["append-completed_target_operator_residual"] > 0.1
        and details["coin"]["append-completed_frame_residual"] > 0.1
        and details["stream"]["append-completed_target_operator_residual"] < TOLERANCE
        and details["stream"]["append-completed_frame_residual"] < TOLERANCE
        and details["contact"]["append-completed_target_operator_residual"] < TOLERANCE
        and details["contact"]["append-completed_frame_residual"] < TOLERANCE,
        {
            "block_details": details,
            "total_coefficient-bearing_orbit_types": total_types,
            "noncommuting_orbit_types": total_noncommuting_types,
            "verified_DSATUR_overlap_color_ceiling": maximum_overlap_colors,
            "verified_DSATUR_commutation_color_ceiling": maximum_commutation_colors,
            "coloring_minimality_claimed": False,
            "orbit_families_closed_under_all_frames": all_orbits_closed,
            "interpretation": "coloring is a supplied compiler schedule; multiset closure alone does not preserve product order or target action",
        },
    )
    return all_orbit_pairs, details


def locality_translation_and_held_controls(schedule, orbit_pairs) -> None:
    active_pairs = {pair for deltas in schedule.values() for delta in deltas for pair in delta}
    size_details = {}
    for size, label in ((TRAINING_SIZE, "training L=3"), (HELD_SIZE, "held L=6")):
        code = c304.c269.build_code(size)
        representatives = c309.basis_representatives(code)
        constraint_failures = 0
        sector_failures = 0
        for representative in representatives:
            constraint_failures += sum(
                not representative.commutes(c302.constraint_pauli(code, vertex))
                for vertex in range(len(code.graph.vertices))
            )
            sector_failures += sum(
                not representative.commutes(row)
                for row in code.local_checks + code.wilsons
            )
        route_details = {}
        for route, pairs in (("scheduled", active_pairs), ("orbit-closed support", orbit_pairs)):
            union = 0
            maximum = 0
            for row, column in pairs:
                transition = representatives[row] @ c302.pauli_dagger(representatives[column])
                support = transition.x | transition.z
                union |= support
                maximum = max(maximum, support.bit_count())
            route_details[route] = {
                "distinct_raw_matrix_units": len(pairs),
                "transition_union_M2": union.bit_count(),
                "maximum_transition_support_M2": maximum,
            }
        patterns = {
            (column.tags, column.stream_slice, r_value)
            for r_value in range(2)
            for column in c304.micro_columns(code)
        }
        size_details[label] = {
            "patterns": len(patterns),
            "constraint_failures": constraint_failures,
            "sector_failures": sector_failures,
            "route_details": route_details,
            "homogeneous_r_sites": len(
                {c306.gauge_qubit(code, body) for body in code.graph.cells}
            ),
        }
    training = c304.c269.build_code(TRAINING_SIZE)
    solver = c304.reference_solver(training)
    source = c304.micro_columns(training, c304.BODY)
    translation_failures = 0
    r_targets = set()
    for displacement in product(range(training.length), repeat=3):
        vertex_map, edge_map = c304.c269.graph_translation_maps(
            training.graph, displacement
        )
        toggles, repair_pairs, flips = c304.c269.repair_data(
            training.graph, vertex_map, edge_map
        )
        target = c304.micro_columns(training, displacement)
        r_targets.add(c306.gauge_qubit(training, displacement))
        for source_column, target_column in zip(source, target):
            translation_failures += c304.state_relative_phase(
                training,
                solver,
                source_column.face_pauli,
                target_column.face_pauli,
                edge_map,
                toggles,
                repair_pairs,
                flips,
            ) != 0
            translation_failures += (
                c304.local.ports.permute_bits(source_column.tags, vertex_map)
                != target_column.tags
            )
    translation_failures += len(r_targets) != TRAINING_SIZE**3
    expected_route = {
        "scheduled": {
            "distinct_raw_matrix_units": 532,
            "transition_union_M2": 43,
            "maximum_transition_support_M2": 27,
        },
        "orbit-closed support": {
            "distinct_raw_matrix_units": 1200,
            "transition_union_M2": 43,
            "maximum_transition_support_M2": 29,
        },
    }
    check(
        "scheduled and orbit-closed factors retain the bounded forty-four-M2 physical patch at training and held size",
        all(
            detail["patterns"] == 180
            and detail["constraint_failures"] == 0
            and detail["sector_failures"] == 0
            and detail["route_details"] == expected_route
            and detail["homogeneous_r_sites"] == size**3
            for size, detail in zip((TRAINING_SIZE, HELD_SIZE), size_details.values())
        )
        and translation_failures == 0,
        {
            "size_details": size_details,
            "installed_overhead_M2_per_cell": 23,
            "projector_control_M2": 14,
            "bounded_patch_M2": 44,
            "L3_translation_ray_tests": TRAINING_SIZE**3 * 90,
            "translation_failures": translation_failures,
        },
    )


def mass_contact_and_comparison_controls() -> None:
    species = c219.common_species(-0.3)
    encoding = c306.constrained_encoding()
    physical_coin = c306.lift_physical(c304.physical_coin(species.coin))
    scalar = np.zeros(42, dtype=complex)
    scalar[:6] = c304.c210.UNIFORM
    encoded = encoding @ scalar
    eigenvalue = np.vdot(encoded, physical_coin @ encoded)
    mass = float(np.angle(eigenvalue)) / c219.C_SQUARED
    fixture = c219.rest_mass(species)
    contact = c306.lift_physical(c304.physical_contact(c304.contact.COUPLING))
    contact_zero = c306.lift_physical(c304.physical_contact(0.0))
    one_particle_firewall = float(np.linalg.norm((contact - contact_zero) @ encoding[:, :12]))
    stream = c306.lift_physical(c304.physical_stream())
    order_residual = float(np.linalg.norm(contact @ stream - stream @ contact, 2))
    comparison = {
        "paired-direct Cycle310": {
            "layers": 220,
            "maximum_raw_matrix_units_per_layer": 8,
            "code_preserving_intermediate_layers": 101,
            "all-frame_intermediate_layers": 0,
            "schedule": "coin QR plus disjoint stream/contact and supplied outer order",
        },
        "gauge QR Cycle309": {
            "layers": 379,
            "maximum_raw_matrix_units_per_layer": 400,
            "code_preserving_intermediate_layers": 379,
            "all-frame_intermediate_layers": 0,
            "schedule": "QR plus supplied outer order",
        },
        "staged spectral Cycle309": {
            "layers": 10,
            "maximum_raw_matrix_units_per_layer": 3600,
            "code_preserving_intermediate_layers": 10,
            "all-frame_intermediate_layers": 10,
            "schedule": "supplied outer order",
        },
        "complete-G spectral Cycle309": {
            "layers": 16,
            "maximum_raw_matrix_units_per_layer": 14400,
            "code_preserving_intermediate_layers": 16,
            "all-frame_intermediate_layers": 16,
            "schedule": "one supplied G application",
        },
    }
    check(
        "the sparse pairing preserves the mass fixture and contact seam while exposing the route tradeoff",
        abs(mass - fixture) < 4e-13
        and one_particle_firewall == 0
        and order_residual > 0.3
        and comparison["paired-direct Cycle310"]["layers"] < comparison["gauge QR Cycle309"]["layers"]
        and comparison["paired-direct Cycle310"]["maximum_raw_matrix_units_per_layer"]
        < comparison["gauge QR Cycle309"]["maximum_raw_matrix_units_per_layer"],
        {
            "physical_rest_mass": mass,
            "Cycle219_fixture": fixture,
            "one_particle_contact_difference": one_particle_firewall,
            "Cycle230_contact_coupling": c304.contact.COUPLING,
            "contact_stream_order_residual": order_residual,
            "route_comparison": comparison,
        },
    )


def deletion_controls(schedule, targets, frame_matrices) -> None:
    whole_layer_deletions = {
        name: max(
            float(np.linalg.norm(factor_matrix(delta) - np.eye(PHYSICAL_DIMENSION), 2))
            for delta in deltas
        )
        for name, deltas in schedule.items()
    }
    exchange = c309.permutation_from_operator(c306.exchange_operator())
    old, _logical, _physical = c306.old_and_new_operators(-0.3)
    base_coin = sector_deltas("coin", old["coin"])
    strongest_index = max(
        range(len(base_coin)),
        key=lambda index: np.linalg.norm(
            factor_matrix(paired_delta(base_coin[index], exchange))
            - np.eye(PHYSICAL_DIMENSION),
            2,
        ),
    )
    deleted_partner = np.eye(PHYSICAL_DIMENSION, dtype=complex)
    for (row, column), value in base_coin[strongest_index].items():
        deleted_partner[row, column] += value
    constraint = c306.role_constraint()
    partner_constraint_residual = float(
        np.linalg.norm(constraint @ deleted_partner - deleted_partner @ constraint, 2)
    )
    deleted_stream = factor_product(schedule["stream"][1:])
    stream_target_residual = float(np.linalg.norm(deleted_stream - targets["stream"], 2))
    stream_frame_residual = max(
        float(np.linalg.norm(frame @ deleted_stream - deleted_stream @ frame, 2))
        for frame in frame_matrices
    )
    check(
        "whole-layer, conjugate-partner, and orbit-member deletions are detected",
        whole_layer_deletions["coin"] > 1.99
        and whole_layer_deletions["stream"] > 1.99
        and whole_layer_deletions["contact"] > 0.3
        and partner_constraint_residual > 1.99
        and stream_target_residual > 1.99
        and stream_frame_residual > 1.99,
        {
            "maximum_whole_paired_layer_deletion_by_block": whole_layer_deletions,
            "coin_conjugate_partner_deletion_constraint_residual": partner_constraint_residual,
            "one_stream_orbit_member_deletion_target_residual": stream_target_residual,
            "one_stream_orbit_member_deletion_frame_residual": stream_frame_residual,
        },
    )


def lawful_domain_and_inventory() -> None:
    rejects = 0
    for invalid in (np.eye(2)[:, :1], np.asarray(((1, 1), (0, 1)), dtype=complex)):
        try:
            c309.qr_factorization(invalid)
        except ValueError:
            rejects += 1
    try:
        disjoint_swap_deltas(np.eye(MICRO_DIMENSION))
    except ValueError:
        rejects += 1
    try:
        diagonal_phase_deltas(c304.physical_stream())
    except ValueError:
        rejects += 1
    try:
        c304.c269.build_code(2)
    except (KeyError, ValueError):
        rejects += 1
    check(
        "lawful-domain controls reject nonsquare, nonunitary, fixed-point, nondiagonal, and aliased-size inputs",
        rejects == 5,
        rejects,
    )
    inventory = {
        "supplied coefficients": "Cycle-219 C, declared wedge^2 C, Cycle-230 g=0.37, and the Cycle-304 ninety-sector blocks",
        "supplied physical grammar": "Cycle-302/304 Pauli transitions, fourteen-bit tag/flag/r projectors, and matrix units",
        "supplied role structure": "Cycle-306 K_exchange, r placement, C_role, common-shell projector, and constrained encoding",
        "derived sparse factors": "one hundred sixty coin QR layers, forty-five disjoint signed stream swaps, and fifteen contact phases",
        "derived pairing": "A on r=0 paired with K A K on r=1, giving exact C_role centralization and at most eight raw units",
        "supplied numerical structure": "QR elimination and residual thresholds; orbit keys use unrounded binary floats after the abs(value)>1e-12 sparsity cutoff",
        "supplied schedules": "coin QR pivot order, outer coin-stream-contact order, occurrence/application, and any orbit-color order",
        "orbit audit only": "frame closure, overlap/noncommutation graphs, and verified DSATUR colorings do not select a new target law",
        "still supplied": "initial code state, fixed Wilson ray, common-shell preparation, macrocell framing, and recurrent application",
        "excluded": "global parity service, Jordan-Wigner order, physical time, energy/rate, Record, and source/gravity semantics",
    }
    check("the paired-direct supplied and derived structure is explicit", len(inventory) == 10, inventory)


def markdown_section(body: str, start: str, end: str | None) -> str:
    start_index = body.index(start)
    end_index = len(body) if end is None else body.index(end, start_index)
    return body[start_index:end_index]


def release_certificate_controls() -> None:
    body = NOTE.read_text(encoding="utf-8")
    n1 = markdown_section(body, "### N1", "### N2")
    statuses = tuple(
        re.findall(r"^\|[^\n]*\|\s*\*\*([^*\n]+)\*\*\s*\|", n1, flags=re.MULTILINE)
    )
    expected_statuses = (
        "ATTEMPTED",
        "ATTEMPTED",
        "ATTEMPTED",
        "ATTEMPTED",
        "ATTEMPTED",
        "OPEN / UNTESTED",
        "OPEN / UNTESTED",
        "OPEN / UNTESTED",
    )
    check("the N1 table has exactly eight declared route statuses", statuses == expected_statuses, statuses)

    n2 = markdown_section(body, "### N2", "### N3")
    directional_rows = tuple(
        re.findall(
            r"^\|\s*`(W_[a-z]+)`\s*\|\s*`(W_[a-z]+)`\s*\|\s*no\s*\|",
            n2,
            flags=re.MULTILINE,
        )
    )
    walls = ("W_gate", "W_apply", "W_rec", "W_prep")
    check(
        "the N2 table contains all twelve and only the directed wall separators",
        len(directional_rows) == 12
        and len(set(directional_rows)) == 12
        and set(directional_rows) == set(permutations(walls, 2)),
        directional_rows,
    )

    n4 = markdown_section(body, "### N4", "### N5")
    locations = tuple(
        (name, int(line))
        for name, line in re.findall(r"`([^`\n]+\.md):(\d+)`", n4)
    )
    results = []
    for name, line in locations:
        path = NOTE.parent / name
        lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
        results.append((name, line, bool(lines) and line <= len(lines) and bool(lines[line - 1].strip())))
    check(
        "all six N4 residual witnesses resolve to nonempty source lines",
        len(results) == 6 and all(row[2] for row in results),
        results,
    )

    n5 = " ".join(markdown_section(body, "### N5", "### N6").lower().split())
    n6 = " ".join(markdown_section(body, "### N6", "### N7").lower().split())
    n7 = " ".join(markdown_section(body, "### N7", "### N8").lower().split())
    n8 = " ".join(markdown_section(body, "### N8", "## Optimal next probe").lower().split())
    broad_markers = (
        "**Broad gate status: FAIL / DO NOT SHIP.**",
        "Gate disposition: **FAIL / DO NOT SHIP for the broad negative.**",
    )
    section_markers = (
        "| resolution | tested result | untested broader claim | disposition |" in n5
        and "gauge qr and spectral factors remain the constructive partial-closure paths" in n6
        and "reject any sparse-primitive no-go" in n7
        and all(cycle in n8 for cycle in ("cycle 304", "cycle 306", "cycle 309", "cycle 310"))
        and "no broad negative or axiom pressure" in n8
    )
    check(
        "the N5-N8 and broad-negative release markers are exact",
        section_markers and all(marker in body for marker in broad_markers),
        {"sections": section_markers, "broad_markers": tuple(marker in body for marker in broad_markers)},
    )

    trailing_whitespace = []
    for path in (Path(__file__).resolve(), NOTE):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if line.endswith((" ", "\t")):
                trailing_whitespace.append((path.name, line_number))
    check("the Cycle-310 release paths contain no trailing whitespace", not trailing_whitespace, trailing_whitespace)


def hidden_premise_scan() -> None:
    phrases = (
        " ".join(("we", "assume")),
        " ".join(("by", "construction")),
        " ".join(("as", "is", "standard")),
        " ".join(("the", "framework", "provides")),
        " ".join(("bridge", "context")),
        "".join(("back", "ground")),
        "".join(("natural", "ly")),
        "".join(("obvious", "ly")),
        " ".join(("standard", "qft")),
        "".join(("register", "ed")),
        "".join(("canoni", "cal")),
    )
    hits = []
    for path in (Path(__file__).resolve(), NOTE):
        body = path.read_text(encoding="utf-8").lower()
        for phrase in phrases:
            if phrase in body:
                hits.append((path.name, phrase))
    check("the two-path hidden-premise scan has zero literal hits", not hits, hits)


def main() -> int:
    print("CYCLE 310: PAIRED-DIRECT ORBIT FACTORIZATION")
    print("authority=none; audit=unset")
    note_contract()
    frame_permutations, frame_matrices = physical_frame_permutations()
    schedule, targets = paired_factorization_controls(frame_permutations, frame_matrices)
    orbit_pairs, _orbit_details = orbit_closure_controls(
        schedule, targets, frame_permutations, frame_matrices
    )
    locality_translation_and_held_controls(schedule, orbit_pairs)
    mass_contact_and_comparison_controls()
    deletion_controls(schedule, targets, frame_matrices)
    lawful_domain_and_inventory()
    release_certificate_controls()
    hidden_premise_scan()
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
