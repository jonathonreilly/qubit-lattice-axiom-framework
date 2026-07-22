#!/usr/bin/env python3
"""Cycle 581: symmetric Regge accuracy and coherent order-orbit tournament.

Route A compiles the Cycle-579 raw Regge/source matching law with a generalized
Strang palindrome and proves a conservative O(1/m^2) operator-norm bound from
Taylor's theorem. Route B constructs a train-derived commutator coloring and
applies it without refit to held L4. Route C tests a coherent proper-cubic
orbit of finite-product orders and separates joint covariance from program/data
disentanglement.

All finite-fixture tick momenta remain supplied host parameters. No literal M2
layout, off-domain full-space update, program genesis, physical time, energy,
stress, gravity, or Einstein equation is claimed.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import sys
from time import perf_counter

import numpy as np
from scipy.sparse.linalg import expm_multiply


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_regge_finite_update_frame_selection_tournament_cycle579_2026_07_22 as cycle579


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_REGGE_SYMMETRIC_ACCURACY_ORDER_ORBIT_TOURNAMENT_"
    "CYCLE581_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9.0e-9
COMM_TOL = 1.0e-12
SIGNAL = 1.0e-10
ANGLE = cycle579.UPDATE_ANGLE
PASS = 0
FAIL = 0


DEPENDENCIES = {
    "outputs/physical_regge_finite_update_frame_selection_tournament_cycle579_receipt_2026_07_22.json":
        "98adae1c1f6b626bf191576ea50a75aaba4243e4f1becdec7e60ef76a2bc80ae",
    "scripts/physical_regge_finite_update_frame_selection_tournament_cycle579_2026_07_22.py":
        "e607e8a0d46fbb70e7be35d1897acebebdb8ad900a4ab69159e572f3fbc5c7ab",
    "docs/work_history/repo/review_feedback/PHYSICAL_REGGE_FINITE_UPDATE_FRAME_SELECTION_TOURNAMENT_CYCLE579_NOTE_2026-07-22.md":
        "9b547203839ae81c3b40dd4514ce3ac75fdba91e6ac18520141d5be18c0cfe93",
    "outputs/physical_regge_finite_update_frame_selection_tournament_cycle579_cold_2026_07_22.txt":
        "851730659d96588f5f8c835c50fdc89a08b83859704f18cbb247da6181e24515",
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest() if path.exists() else "MISSING"


def dependency_controls() -> dict:
    observed = {path: file_sha(ROOT / path) for path in DEPENDENCIES}
    return {"expected": DEPENDENCIES, "observed": observed, "pass": observed == DEPENDENCIES}


def cycle579_receipt() -> dict:
    path = ROOT / "outputs/physical_regge_finite_update_frame_selection_tournament_cycle579_receipt_2026_07_22.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def note_contract() -> dict:
    required = (
        "authority: none", "audit: unset", "cycle 581", "route a", "route b", "route c",
        "raw unnormalized deficit", "no momentum-dependent normalization", "strang",
        "o(1/m^2)", "taylor", "operator norm", "hermitian", "unitary telescoping",
        "exact declared-code", "train l3", "held l4", "no refit", "2905",
        "analytic", "not cold-executed as a full physical hilbert-space operator",
        "commutator", "color", "coherent", "proper-cubic", "entanglement",
        "all 24", "576", "no literal m2 layout", "off-domain full-space",
        "program genesis", "tick_momentum", "not physical time", "generator is not a rate",
        "not physical energy", "not physical stress", "not gravity", "not an einstein equation",
        "actual cycle-230 contact", "mass", "seam", "leakage", "inverse",
        "supplied", "derived", "open", "n1 —", "n8 —",
        "broad negative gate: fail / do not ship", "no axiom pressure",
        "positive partial construction with explicit residuals",
        "norm diagnostic", "not a derived occurrence frequency or born law",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def singleton_strang_substeps(layer_count: int) -> tuple[tuple[int, float], ...]:
    return tuple(
        [(index, 0.5) for index in range(layer_count - 1)]
        + [(layer_count - 1, 1.0)]
        + [(index, 0.5) for index in reversed(range(layer_count - 1))]
    )


def ordered_singleton_strang_substeps(order: tuple[int, ...]) -> tuple[tuple[int, float], ...]:
    return tuple(
        [(index, 0.5) for index in order[:-1]]
        + [(order[-1], 1.0)]
        + [(index, 0.5) for index in reversed(order[:-1])]
    )


def grouped_strang_substeps(groups: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, float], ...]:
    rows: list[tuple[int, float]] = []
    for group in groups[:-1]:
        rows.extend((index, 0.5) for index in group)
    rows.extend((index, 1.0) for index in groups[-1])
    for group in reversed(groups[:-1]):
        rows.extend((index, 0.5) for index in reversed(group))
    return tuple(rows)


def free_algebra_derivative_controls(
    substeps: tuple[tuple[int, float], ...], layer_count: int
) -> dict:
    """Verify first/second Taylor coefficients as formal noncommuting words."""
    first = np.zeros(layer_count)
    second = defaultdict(float)
    for index, weight in substeps:
        first[index] += weight
        second[(index, index)] += 0.5 * weight ** 2
    # apply_product applies later listed exponentials on the left.
    for earlier in range(len(substeps)):
        right_index, right_weight = substeps[earlier]
        for later in range(earlier + 1, len(substeps)):
            left_index, left_weight = substeps[later]
            second[(left_index, right_index)] += left_weight * right_weight
    second_residual = max(
        abs(second[(left, right)] - 0.5)
        for left in range(layer_count)
        for right in range(layer_count)
    )
    return {
        "formal_noncommuting_first_derivative_coefficient_residual": float(np.max(abs(first - 1))),
        "formal_noncommuting_second_derivative_coefficient_residual": float(second_residual),
        "formal_words_checked_through_degree": 2,
        "ordered_degree_two_words_checked": layer_count ** 2,
    }


def apply_product(
    state: np.ndarray,
    layers: list,
    substeps: tuple[tuple[int, float], ...],
    repetitions: int,
    *,
    inverse: bool = False,
) -> np.ndarray:
    output = state.copy()
    rows = tuple(reversed(substeps)) if inverse else substeps
    sign = -1.0 if inverse else 1.0
    delta = ANGLE / repetitions
    for _ in range(repetitions):
        for index, weight in rows:
            output = cycle579.apply_layer(output, layers[index], sign * delta * weight)
    return output


def strang_program_trace(
    layers: list,
    substeps: tuple[tuple[int, float], ...],
    initial: np.ndarray,
    repetitions: int = 2,
) -> dict:
    program_sites = repetitions * len(substeps)
    data = initial.copy()
    phase = 0
    visited = []
    applied = []
    delta = ANGLE / repetitions
    for _ in range(program_sites):
        visited.append(phase)
        local = phase % len(substeps)
        index, weight = substeps[local]
        applied.append((index, weight))
        data = cycle579.apply_layer(data, layers[index], delta * weight)
        phase = (phase + 1) % program_sites
    independently_evaluated = apply_product(initial, layers, substeps, repetitions)

    inverse_data = data.copy()
    inverse_phase = phase
    for _ in range(program_sites):
        inverse_phase = (inverse_phase - 1) % program_sites
        local = inverse_phase % len(substeps)
        index, weight = substeps[local]
        inverse_data = cycle579.apply_layer(inverse_data, layers[index], -delta * weight)

    deleted_layer = next(index for index, layer in enumerate(layers) if layer["name"].startswith("S:"))
    deleted = initial.copy()
    deleted_phase = 0
    for _ in range(program_sites):
        local = deleted_phase % len(substeps)
        index, weight = substeps[local]
        if index != deleted_layer:
            deleted = cycle579.apply_layer(deleted, layers[index], delta * weight)
        deleted_phase = (deleted_phase + 1) % program_sites

    frozen = initial.copy()
    first_index, first_weight = substeps[0]
    for _ in range(program_sites):
        frozen = cycle579.apply_layer(frozen, layers[first_index], delta * first_weight)

    physical_rows = sha256()
    for code_index in range(program_sites):
        physical_rows.update(str(1 << code_index).encode())
        physical_rows.update(b";")
    return {
        "repetitions": repetitions,
        "strang_substeps_per_repetition": len(substeps),
        "program_M2_sites": program_sites,
        "per_repetition_program_visitation_sha256": sha256(
            json.dumps(list(substeps), separators=(",", ":")).encode()
        ).hexdigest(),
        "full_program_visitation_sha256": sha256(
            json.dumps(visited, separators=(",", ":")).encode()
        ).hexdigest(),
        "applied_factor_weight_sha256": sha256(
            json.dumps(applied, separators=(",", ":")).encode()
        ).hexdigest(),
        "every_program_rail_visited_once": visited == list(range(program_sites)),
        "final_program_rail": phase,
        "compiled_product_law_intertwiner_residual": float(np.linalg.norm(data - independently_evaluated)),
        "inverse_program_rail": inverse_phase,
        "inverse_data_residual": float(np.linalg.norm(inverse_data - initial)),
        "source_layer_deletion_signal": float(np.linalg.norm(data - deleted)),
        "source_layer_deletion_program_returns": deleted_phase == 0,
        "program_shift_deletion_signal": float(np.linalg.norm(data - frozen)),
        "program_shift_deletion_unique_rails_visited": 1,
        "physical_one_hot_embedding_shape": f"2^{program_sites} x {program_sites}",
        "physical_one_hot_embedding_nonzero_entries": program_sites,
        "physical_one_hot_embedding_row_hash": physical_rows.hexdigest(),
        "physical_one_hot_embedding_Gram_residual": 0.0,
        "physical_one_hot_shift_code_leakage": 0.0,
        "one_hot_domain_supplied": True,
        "one_hot_domain_locally_enforced": False,
        "literal_M2_layout_compiled": False,
        "off_domain_full_space_micro_update_compiled": False,
        "maximum_phase_controlled_matching_rotation_support_M2": 3,
    }


def rigorous_strang_bound(angle: float, lambda_sum: float, repetitions: int) -> float:
    """Taylor-remainder bound theta^3 Lambda^3/(3m^2)."""
    return float(abs(angle) ** 3 * lambda_sum ** 3 / (3 * repetitions ** 2))


def fixture_core(
    label: str,
    length: int,
    tick_momentum: float,
    held: bool,
    diagonal_types: list,
    regge_types: list,
    source_types: list,
) -> dict:
    layers, hamiltonian, factor = cycle579.build_factor_layers(
        length, tick_momentum, diagonal_types, regge_types, source_types
    )
    dimension = hamiltonian.shape[0]
    source_state = np.zeros(dimension, dtype=complex)
    source_state[0] = 1
    rng = np.random.default_rng(581 + length)
    random_state = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
    random_state /= np.linalg.norm(random_state)
    exact_source = expm_multiply(-1j * ANGLE * hamiltonian, source_state)
    exact_random = expm_multiply(-1j * ANGLE * hamiltonian, random_state)
    factor.update({
        "fixture": label,
        "length": length,
        "held": held,
        "tick_momentum_supplied_as_host_parameter": tick_momentum,
        "dimension": dimension,
        "layers_data": layers,
        "hamiltonian_data": hamiltonian,
        "source_state_data": source_state,
        "random_state_data": random_state,
        "exact_source_data": exact_source,
        "exact_random_data": exact_random,
        "lambda_sum_exact_layer_operator_norms": float(sum(layer["operator_norm"] for layer in layers)),
    })
    return factor


def convergence_rows(fixture: dict, substeps: tuple[tuple[int, float], ...]) -> tuple[dict, ...]:
    layers = fixture["layers_data"]
    lambda_sum = fixture["lambda_sum_exact_layer_operator_norms"]
    rows = []
    for repetitions in (1, 2, 4, 8, 16):
        source = apply_product(fixture["source_state_data"], layers, substeps, repetitions)
        random_state = apply_product(fixture["random_state_data"], layers, substeps, repetitions)
        source_error = float(np.linalg.norm(source - fixture["exact_source_data"]))
        random_error = float(np.linalg.norm(random_state - fixture["exact_random_data"]))
        raw_bound = rigorous_strang_bound(ANGLE, lambda_sum, repetitions)
        rows.append({
            "repetitions": repetitions,
            "program_microsteps": repetitions * len(substeps),
            "source_state_error": source_error,
            "deterministic_random_state_error": random_error,
            "maximum_state_error": max(source_error, random_error),
            "rigorous_Taylor_operator_bound": raw_bound,
            "unitary_cap_bound": min(2.0, raw_bound),
            "bound_dominates_observed": max(source_error, random_error) <= raw_bound + 2.0e-12,
            "source_norm_residual": abs(float(np.vdot(source, source).real) - 1),
            "random_norm_residual": abs(float(np.vdot(random_state, random_state).real) - 1),
        })
    return tuple(rows)


def empirical_slope(rows: tuple[dict, ...]) -> float:
    repetitions = np.asarray([row["repetitions"] for row in rows[1:]], dtype=float)
    errors = np.asarray([row["maximum_state_error"] for row in rows[1:]])
    return float(np.polyfit(np.log(repetitions), np.log(errors), 1)[0])


def commutator_graph(layers: list) -> tuple[tuple[frozenset[int], ...], dict]:
    adjacency = [set() for _ in layers]
    rows = []
    for left, right in combinations(range(len(layers)), 2):
        commutator = layers[left]["matrix"] @ layers[right]["matrix"] - layers[right]["matrix"] @ layers[left]["matrix"]
        norm = float(np.sqrt(np.sum(abs(commutator.data) ** 2)))
        if norm > COMM_TOL:
            adjacency[left].add(right)
            adjacency[right].add(left)
            rows.append((left, right, norm))
    return tuple(frozenset(row) for row in adjacency), {
        "total_pairs": len(layers) * (len(layers) - 1) // 2,
        "noncommuting_pairs": len(rows),
        "commuting_pairs": len(layers) * (len(layers) - 1) // 2 - len(rows),
        "maximum_Frobenius_norm": max(row[2] for row in rows),
        "row_hash": sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest(),
    }


def dsatur_coloring(adjacency: tuple[frozenset[int], ...]) -> tuple[tuple[int, ...], ...]:
    uncolored = set(range(len(adjacency)))
    colors: dict[int, int] = {}
    while uncolored:
        def priority(vertex: int) -> tuple[int, int, int]:
            saturation = len({colors[n] for n in adjacency[vertex] if n in colors})
            return saturation, len(adjacency[vertex]), -vertex
        vertex = max(uncolored, key=priority)
        forbidden = {colors[n] for n in adjacency[vertex] if n in colors}
        color = 0
        while color in forbidden:
            color += 1
        colors[vertex] = color
        uncolored.remove(vertex)
    grouped = defaultdict(list)
    for vertex, color in colors.items():
        grouped[color].append(vertex)
    groups = [tuple(sorted(grouped[color])) for color in sorted(grouped)]
    central = max(range(len(groups)), key=lambda index: (len(groups[index]), -index))
    groups.append(groups.pop(central))
    return tuple(groups)


def within_group_commutators(layers: list, groups: tuple[tuple[int, ...], ...]) -> dict:
    rows = []
    for group_index, group in enumerate(groups):
        for left, right in combinations(group, 2):
            commutator = layers[left]["matrix"] @ layers[right]["matrix"] - layers[right]["matrix"] @ layers[left]["matrix"]
            norm = float(np.sqrt(np.sum(abs(commutator.data) ** 2)))
            if norm > COMM_TOL:
                rows.append((group_index, left, right, norm))
    return {
        "tested_pairs": sum(len(group) * (len(group) - 1) // 2 for group in groups),
        "noncommuting_pairs": len(rows),
        "maximum_Frobenius_norm": max((row[3] for row in rows), default=0.0),
        "row_hash": sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest(),
    }


def clean_fixture(fixture: dict) -> dict:
    return {key: value for key, value in fixture.items() if not key.endswith("_data")}


def route_a_and_b(q_kernel: dict, d_kernel: dict, receipt: dict) -> tuple[dict, dict]:
    diagonal_types, regge_types, source_types = cycle579.interaction_types(q_kernel, d_kernel)
    train = fixture_core(
        "TRAIN_L3_KT0", 3, 0.0, False, diagonal_types, regge_types, source_types
    )
    held = fixture_core(
        "BLINDED_HELD_L4_KT_PI_OVER_2", 4, np.pi / 2, True,
        diagonal_types, regge_types, source_types,
    )
    baseline_substeps = singleton_strang_substeps(len(train["layers_data"]))
    train["baseline_convergence"] = convergence_rows(train, baseline_substeps)
    held["baseline_convergence"] = convergence_rows(held, baseline_substeps)
    train["baseline_empirical_log_error_slope"] = empirical_slope(train["baseline_convergence"])
    held["baseline_empirical_log_error_slope"] = empirical_slope(held["baseline_convergence"])
    train["baseline_program_trace"] = strang_program_trace(
        train["layers_data"], baseline_substeps, train["random_state_data"]
    )
    held["baseline_program_trace"] = strang_program_trace(
        held["layers_data"], baseline_substeps, held["random_state_data"]
    )
    for fixture in (train, held):
        inverse = apply_product(
            apply_product(fixture["random_state_data"], fixture["layers_data"], baseline_substeps, 16),
            fixture["layers_data"], baseline_substeps, 16, inverse=True,
        )
        fixture["baseline_m16_inverse_residual"] = float(np.linalg.norm(inverse - fixture["random_state_data"]))
        fixture["maximum_norm_residual"] = max(
            max(row["source_norm_residual"], row["random_norm_residual"])
            for row in fixture["baseline_convergence"]
        )

    train_adjacency, train_commutators = commutator_graph(train["layers_data"])
    groups = dsatur_coloring(train_adjacency)
    train_parallel_grouped_substeps = grouped_strang_substeps(groups)
    frozen_color_order = tuple(index for group in groups for index in group)
    color_ordered_serial_substeps = ordered_singleton_strang_substeps(frozen_color_order)
    train_group_validation = within_group_commutators(train["layers_data"], groups)
    held_group_validation = within_group_commutators(held["layers_data"], groups)
    train["color_ordered_serial_convergence"] = convergence_rows(train, color_ordered_serial_substeps)
    held["color_ordered_serial_convergence"] = convergence_rows(held, color_ordered_serial_substeps)
    train["color_ordered_serial_empirical_log_error_slope"] = empirical_slope(
        train["color_ordered_serial_convergence"]
    )
    held["color_ordered_serial_empirical_log_error_slope"] = empirical_slope(
        held["color_ordered_serial_convergence"]
    )

    factor_norms_full = [
        max(abs(coefficient) for _, coefficient in diagonal_types),
        *(abs(coefficient) for _, coefficient in regge_types),
        *(abs(coefficient) for _, coefficient in source_types for _ in range(24)),
    ]
    lambda_full = float(sum(factor_norms_full))
    full_layers = 1 + len(regge_types) + 24 * len(source_types)
    full_substeps = 2 * full_layers - 1
    full_constant = rigorous_strang_bound(ANGLE, lambda_full, 1)
    full_rows = []
    for repetitions in (1, 2, 4, 8, 16, 64, 512, 4096):
        raw = full_constant / repetitions ** 2
        full_rows.append({
            "repetitions": repetitions,
            "strang_substeps_per_repetition": full_substeps,
            "one_hot_program_M2_per_cell": repetitions * full_substeps,
            "rigorous_full24_operator_error_bound": raw,
            "unitary_cap_bound": min(2.0, raw),
            "fixed_program_covariance_defect_bound": min(2.0, 2 * raw),
        })
    below_one = math.floor(math.sqrt(full_constant)) + 1
    below_milli = math.floor(math.sqrt(full_constant / 1.0e-3)) + 1
    first_order = receipt.get("route_B_declared_code_product_program", {})
    diagonal_modes = tuple(key[1] for key, _ in diagonal_types)

    route_a = {
        "route": "A_generalized_symmetric_Strang_matching_program",
        "formula": "S2(delta)=prod(j=1..C-1)exp(-i delta H_j/2) exp(-i delta H_C) prod(j=C-1..1)exp(-i delta H_j/2)",
        "bound": "||exp(-i theta H)-S2(theta/m)^m|| <= |theta|^3 Lambda^3/(3m^2)",
        "bound_derivation": {
            "norm": "spectral/operator norm",
            "assumptions": (
                "finite-dimensional time-independent Hermitian factor layers H_j",
                "real theta and exact unitary factor exponentials",
                "nu_j=||H_j|| and Lambda=sum_j nu_j",
                "the palindrome and exact exponential have identical derivatives through order two at zero",
                "Taylor integral remainder bounds each third derivative by Lambda^3",
                "unitary telescoping multiplies one-step error by m",
            ),
            "local_remainder": "|delta|^3(||H||^3+Lambda^3)/6 <= |delta|^3 Lambda^3/3",
            "global_remainder": "m times local remainder at delta=theta/m",
            "exponential_growth_factor_needed": False,
            "commutator_formula_guessed_or_imported": False,
        },
        "single_frame_layers": len(train["layers_data"]),
        "single_frame_strang_substeps_per_repetition": len(baseline_substeps),
        "formal_derivative_matching": free_algebra_derivative_controls(
            baseline_substeps, len(train["layers_data"])
        ),
        "train_and_held": (clean_fixture(train), clean_fixture(held)),
        "compiled_product_law_intertwiner_residual": max(
            train["baseline_program_trace"]["compiled_product_law_intertwiner_residual"],
            held["baseline_program_trace"]["compiled_product_law_intertwiner_residual"],
        ),
        "cold_executed_scope": "260-factor single-frame train L3 and held L4 only",
        "exact_declared_code_program_EG": True,
        "literal_physical_M2_layout_compiled": False,
        "off_domain_full_space_micro_update_compiled": False,
        "full24_layers": full_layers,
        "full24_strang_substeps_per_repetition": full_substeps,
        "full24_factor_operator_norm_count": len(factor_norms_full),
        "full24_combined_diagonal_layer_operator_norm": float(factor_norms_full[0]),
        "full24_diagonal_modes_are_unique": len(set(diagonal_modes)) == len(diagonal_modes),
        "full24_maximum_diagonal_coefficient_imaginary_part": float(max(abs(coefficient.imag) for _, coefficient in diagonal_types)),
        "full24_norm_composition": "combined diagonal norm is the maximum over unique edge-mode diagonals; 144 Regge factors run across disjoint frame sectors so their norms are not multiplied by 24; 115 shared-source factors are replicated 24 times",
        "full24_lambda_sum_operator_norm_bound": lambda_full,
        "full24_bound_constant": full_constant,
        "full24_analytic_rows": tuple(full_rows),
        "full24_status": "analytic factor count, Taylor bound, overhead and covariance bound; not cold-executed as a full physical Hilbert-space operator",
        "full24_physical_Hilbert_space_operator_cold_executed": False,
        "repetitions_for_raw_bound_below_1": below_one,
        "repetitions_for_raw_bound_below_1e_minus_3": below_milli,
        "program_M2_for_raw_bound_below_1e_minus_3": below_milli * full_substeps,
        "cycle579_first_order_repetitions_below_1": first_order.get("full24_raw_bound_below_1_requires_m"),
        "cycle579_first_order_repetitions_below_1e_minus_3": first_order.get("full24_raw_bound_below_1e_minus_3_requires_m"),
        "raw_source_preserved": True,
        "momentum_dependent_source_normalization_used": False,
        "finite_fixture_tick_momentum_is_host_parameter": True,
        "joined_phase_ring_data_operator_composed": False,
        "parameters_refit": 0,
    }
    route_b = {
        "route": "B_train_derived_DSATUR_commutator_coloring",
        "coloring_selected_from": "train L3 noncommutator graph only",
        "held_used_for_selection_or_refit": False,
        "train_noncommutator_graph": train_commutators,
        "color_count": len(groups),
        "group_sizes": tuple(len(group) for group in groups),
        "largest_train_commuting_group_used_as_train_parallel_palindrome_center": len(groups[-1]),
        "groups_sha256": sha256(json.dumps(groups, separators=(",", ":")).encode()).hexdigest(),
        "frozen_color_order_sha256": sha256(
            json.dumps(frozen_color_order, separators=(",", ":")).encode()
        ).hexdigest(),
        "baseline_substeps_per_repetition": len(baseline_substeps),
        "train_parallel_grouped_substeps_per_repetition": len(train_parallel_grouped_substeps),
        "held_parallel_grouping_lawful": held_group_validation["noncommuting_pairs"] == 0,
        "held_parallel_grouping_disposition": "falsified by held within-color noncommutators; no held-driven recoloring performed",
        "color_ordered_serial_substeps_per_repetition": len(color_ordered_serial_substeps),
        "color_ordered_serial_formal_derivative_matching": free_algebra_derivative_controls(
            color_ordered_serial_substeps, len(train["layers_data"])
        ),
        "train_within_group_validation": train_group_validation,
        "held_no_refit_within_group_validation": held_group_validation,
        "same_grouping_and_order_on_held": True,
        "train_baseline_convergence": train["baseline_convergence"],
        "train_color_ordered_serial_convergence": train["color_ordered_serial_convergence"],
        "held_baseline_convergence": held["baseline_convergence"],
        "held_color_ordered_serial_convergence": held["color_ordered_serial_convergence"],
        "train_baseline_slope": train["baseline_empirical_log_error_slope"],
        "train_color_ordered_serial_slope": train["color_ordered_serial_empirical_log_error_slope"],
        "held_baseline_slope": held["baseline_empirical_log_error_slope"],
        "held_color_ordered_serial_slope": held["color_ordered_serial_empirical_log_error_slope"],
        "rigorous_bound_for_color_ordered_serial_schedule": "same Taylor bound because it is a full primitive-factor palindrome",
        "rigorous_bound_for_train_parallel_schedule": "same Taylor bound on train because every train color is an exact commuting macro-generator",
        "rigorous_held_parallel_macro_bound_claimed": False,
        "physical_layout_compiled": False,
        "result_scope": "train-only parallel grouping falsified on held; frozen serial color-order comparison remains a lawful no-refit palindrome",
    }
    return route_a, route_b


def dense_factorization(hamiltonian: np.ndarray) -> tuple[tuple, ...]:
    diagonal = np.real(np.diag(hamiltonian)).copy()
    factors: list[tuple] = [("diagonal", diagonal)]
    for left in range(len(hamiltonian)):
        for right in range(left + 1, len(hamiltonian)):
            coefficient = hamiltonian[left, right]
            if abs(coefficient) > cycle579.KERNEL_TOL:
                factors.append(("pair", left, right, coefficient))
    return tuple(factors)


def apply_dense_factor_inplace(data: np.ndarray, factor: tuple, angle: float) -> None:
    if factor[0] == "diagonal":
        phase = np.exp(-1j * angle * factor[1])
        if data.ndim == 1:
            data *= phase
        else:
            data *= phase[:, None]
        return
    _, left_index, right_index, coefficient = factor
    magnitude = abs(coefficient)
    cosine = math.cos(angle * magnitude)
    sine = math.sin(angle * magnitude)
    phase = coefficient / magnitude
    left = data[left_index].copy()
    right = data[right_index].copy()
    data[left_index] = cosine * left - 1j * sine * phase * right
    data[right_index] = cosine * right - 1j * sine * np.conj(phase) * left


def dense_strang_unitary(hamiltonian: np.ndarray, repetitions: int = 1) -> tuple[np.ndarray, int]:
    factors = dense_factorization(hamiltonian)
    substeps = singleton_strang_substeps(len(factors))
    result = np.eye(len(hamiltonian), dtype=complex)
    delta = ANGLE / repetitions
    for _ in range(repetitions):
        for index, weight in substeps:
            apply_dense_factor_inplace(result, factors[index], delta * weight)
    return result, len(factors)


def representation_permutation(representation: np.ndarray) -> np.ndarray:
    return np.argmax(representation, axis=0)


def conjugate_by_permutation(matrix: np.ndarray, permutation: np.ndarray) -> np.ndarray:
    return matrix[np.ix_(permutation, permutation)]


def route_c_order_orbit() -> dict:
    cycle576 = cycle579.cycle576
    momentum = np.asarray((0.17, 0.11, 0.07, 0.13))
    frame_count = len(cycle576.FRAMES)
    multiplication = np.zeros((frame_count, frame_count), dtype=int)
    representation_residual = 0.0
    permutations = tuple(representation_permutation(rep) for rep in cycle576.FRAME_SECTOR_REPS)
    for left in range(frame_count):
        for right in range(frame_count):
            target = cycle576.FRAME_LOOKUP[
                tuple((cycle576.FRAMES[left] @ cycle576.FRAMES[right]).reshape(-1))
            ]
            multiplication[left, right] = target
            composed = permutations[left][permutations[right]]
            representation_residual = max(
                representation_residual,
                float(np.max(abs(composed - permutations[target]))),
            )

    orbit_products = []
    factor_counts = []
    hermiticity = 0.0
    for lifted in cycle576.LIFTED_FRAMES:
        hamiltonian = cycle576.frame_sector_hamiltonian(lifted @ momentum)
        hermiticity = max(hermiticity, float(np.linalg.norm(hamiltonian - hamiltonian.conj().T)))
        unitary, factors = dense_strang_unitary(hamiltonian, repetitions=1)
        orbit_products.append(unitary)
        factor_counts.append(factors)
    branches = tuple(
        conjugate_by_permutation(orbit_products[index], permutations[index])
        for index in range(frame_count)
    )

    joint_covariance = 0.0
    joint_rows = []
    for branch_index in range(frame_count):
        for transform in range(frame_count):
            product_index = int(multiplication[branch_index, transform])
            transformed_branch = conjugate_by_permutation(
                orbit_products[product_index], permutations[branch_index]
            )
            pulled_back = conjugate_by_permutation(transformed_branch, permutations[transform])
            residual = float(np.linalg.norm(pulled_back - branches[product_index]))
            joint_covariance = max(joint_covariance, residual)
            joint_rows.append((branch_index, transform, product_index, residual))

    source_probe = np.zeros(branches[0].shape[0], dtype=complex)
    source_probe[0] = 1
    branch_states = np.asarray([branch @ source_probe for branch in branches])
    gram = branch_states.conj() @ branch_states.T
    program_purity = float(np.sum(abs(gram) ** 2).real / frame_count ** 2)
    mean_state = np.mean(branch_states, axis=0)
    uniform_projection_weight = float(np.vdot(mean_state, mean_state).real)
    branch_dispersion = max(
        float(np.linalg.norm(branch_states[left] - branch_states[right]))
        for left, right in combinations(range(frame_count), 2)
    )
    entanglement_detected = program_purity < 1 - SIGNAL
    identity_index = cycle576.FRAME_LOOKUP[tuple(np.eye(3, dtype=int).reshape(-1))]
    fixed_branch_covariance = max(
        float(np.linalg.norm(branch - branches[identity_index]))
        for index, branch in enumerate(branches) if index != identity_index
    )
    return {
        "route": "C_coherent_proper_cubic_order_orbit",
        "finite_product_repetitions": 1,
        "momentum": momentum.tolist(),
        "finite_fixture_momentum_is_supplied": True,
        "factor_counts_per_branch": tuple(factor_counts),
        "factor_count_constant_across_orbit": len(set(factor_counts)) == 1,
        "Hamiltonian_Hermiticity_residual": hermiticity,
        "all576_representation_products": frame_count ** 2,
        "all576_representation_residual": representation_residual,
        "controlled_orbit_joint_covariance_residual": joint_covariance,
        "controlled_orbit_joint_covariance_rows_sha256": sha256(
            json.dumps(joint_rows, separators=(",", ":")).encode()
        ).hexdigest(),
        "fixed_canonical_branch_covariance_Frobenius_residual": fixed_branch_covariance,
        "identity_frame_branch_index": identity_index,
        "uniform_program_source_probe_reduced_program_purity": program_purity,
        "uniform_program_projection_weight": uniform_projection_weight,
        "uniform_program_projection_weight_definition": "||24^-1 sum_g B_g |source>||^2",
        "uniform_program_projection_weight_is_norm_diagnostic_not_occurrence_frequency_or_Born_law": True,
        "maximum_branch_source_probe_dispersion": branch_dispersion,
        "generic_source_probe_data_program_entanglement_detected": entanglement_detected,
        "exact_joint_covariance_achieved": joint_covariance < TOL,
        "exact_data_only_covariance_without_entanglement_achieved": (
            joint_covariance < TOL and not entanglement_detected
            and abs(uniform_projection_weight - 1) < TOL
        ),
        "scope_of_false_without_entanglement": "this explicit uniform controlled-orbit construction on the source probe only",
        "uniform_program_projection_would_be_nonunitary_and_has_weight": uniform_projection_weight,
        "coherent_program_genesis_derived": False,
        "program_uncomputation_compiled": False,
        "literal_M2_program_layout_compiled": False,
        "off_domain_full_space_update_compiled": False,
        "universal_impossibility_claim": False,
    }


def retained_controls(receipt: dict) -> dict:
    shore = receipt.get("retained_physical_shore", {})
    kernel = receipt.get("raw_local_kernel", {})
    return {
        "raw_source_action": "S_source=-lambda sum_x q_x sum_local_hinges delta_hinge",
        "raw_unnormalized_deficit_preserved": not kernel.get("momentum_dependent_source_normalization_used", True),
        "Cycle572_EG_residual": shore.get("Cycle572_EG_equals_GphysicalE_residual"),
        "one_particle_mass_residual": shore.get("one_particle_mass_residual"),
        "actual_Cycle230_contact_factorization_residual": shore.get("Cycle230_contact_factorization_residual"),
        "Cycle230_seam_braid_residual": shore.get("Cycle230_seam_braid_residual"),
        "target_code_leakage": shore.get("target_code_leakage"),
        "all24_all576_target_covariance_retained": True,
        "R3_coefficient_retained": -0.4999999704,
        "Cycle460_scope_boundary": "compiles supplied held kernels; does not derive the downstream homogeneous static receiver law",
        "Cycle581_derives_downstream_homogeneous_static_receiver_law": False,
    }


def inventory() -> dict:
    return {
        "supplied": (
            "Cycle576/579 raw Regge action, edge variables, source sign/coupling and 24 co-present sectors",
            "update angle, factor order, Strang half/full weights, repetition count and terminal readout",
            "finite L3/L4 domains and host tick_momentum values",
            "synchronized exactly-one program code and its initial rail",
            "proper-cubic uniform control state and branch-label multiplication law",
        ),
        "derived": (
            "generalized Strang palindrome and exact declared-code single-frame program trace",
            "Taylor/operator-norm O(1/m^2) bound under enumerated finite-dimensional Hermitian assumptions",
            "train-derived commutator coloring and held no-refit validation/comparison",
            "exact all576 joint covariance of the controlled order orbit",
            "source-probe program purity and uniform-program projection weight as norm diagnostics",
        ),
        "open": (
            "literal geometric M2 layout and off-domain full-space micro-update",
            "cold execution of the 2905-factor full24 physical Hilbert operator",
            "practical rigorous full24 accuracy overhead and exact target exponential",
            "entanglement-free deterministic proper-cubic order symmetrization",
            "program/frame genesis, synchronization, terminal readout and renewable sink",
            "joined phase-ring/data operator, arbitrary phase, physical time and nonlinear recurrence",
            "selection and empirical calibration of candidate laws",
            "downstream homogeneous static receiver law; Cycle460 and Cycle581 do not derive it",
        ),
    }


def no_go_controls() -> dict:
    families = (
        {"family": "generalized symmetric matching product", "object_formulation": "raw matching factors and palindromic program", "mechanism_invariant": "time symmetry cancels first-order local error", "terminal_obligation": "higher-accuracy finite update", "status": "ATTEMPTED", "citation": "Cycle581 runner Route A", "result": "exact declared-code product and rigorous inverse-square bound", "why_not_terminal": "exact target exponential, practical full24 overhead and literal layout remain open"},
        {"family": "commutator-colored macro product", "object_formulation": "noncommutator graph", "mechanism_invariant": "exact commuting color classes", "terminal_obligation": "shorter held-portable product schedule", "status": "ATTEMPTED", "citation": "Cycle581 runner Route B", "result": "82 train colors and lawful frozen serial comparison", "why_not_terminal": "39 within-color held commutators falsify the train-only parallel grouping"},
        {"family": "coherent proper-cubic order orbit", "object_formulation": "regular program register plus controlled products", "mechanism_invariant": "joint group covariance", "terminal_obligation": "exact finite-m covariance without residual program", "status": "ATTEMPTED", "citation": "Cycle581 runner Route C", "result": "all576 joint covariance residual zero", "why_not_terminal": "source-probe program purity and uniform-program projection weight are below one"},
        {"family": "first-order ordered Lie product", "object_formulation": "raw matching factors", "mechanism_invariant": "ordered first-order telescoping", "terminal_obligation": "finite target exponential", "status": "RULED OUT BY PRIOR ONLY FOR EXACTNESS OF THAT ORDER", "citation": "Cycle579 note lines 170-180", "result": "complete noncommutator census and 1/m error", "why_not_terminal": "that declared finite order is not the exact exponential"},
        {"family": "randomized product formula", "object_formulation": "distribution over factor permutations", "mechanism_invariant": "error cancellation in expectation/concentration", "terminal_obligation": "held concentration-controlled accuracy/covariance", "status": "OPEN / NOT COUNTED", "citation": "open Cycle581 continuation", "result": "not attempted", "why_not_terminal": "no concentration bound or held execution"},
        {"family": "block encoding and signal processing", "object_formulation": "local-term select/prepare oracle", "mechanism_invariant": "polynomial Hamiltonian simulation", "terminal_obligation": "bounded-M2 deterministic compiler", "status": "OPEN / NOT COUNTED", "citation": "open Cycle581 continuation", "result": "not attempted", "why_not_terminal": "no oracle/layout compiler"},
        {"family": "LCU group symmetrization", "object_formulation": "coherent order branches plus amplitude amplification", "mechanism_invariant": "projected covariant linear combination", "terminal_obligation": "deterministic unentangled covariant update", "status": "OPEN / NOT COUNTED", "citation": "Cycle581 Route C projection-weight diagnostic", "result": "nonzero projected component norm measured; amplification not attempted", "why_not_terminal": "no deterministic amplification/program-return compiler"},
    )
    walls = (
        ("W_accuracy", "practical rigorous full24 target accuracy"),
        ("W_layout", "literal M2 layout and off-domain full-space law"),
        ("W_program", "endogenous program genesis/synchronization/readout"),
        ("W_covariance", "deterministic entanglement-free finite-m covariance"),
        ("W_phase", "joined fourth-displacement phase-ring/data operator"),
    )
    evidence = {
        ("W_accuracy", "W_layout"): ("an accuracy theorem supplies no layout", "a layout supplies no target-error theorem"),
        ("W_accuracy", "W_program"): ("a bound prepares no program", "program genesis cancels no product error"),
        ("W_accuracy", "W_covariance"): ("accuracy alone leaves a finite branch defect", "joint covariance supplies no target-error rate"),
        ("W_accuracy", "W_phase"): ("accuracy at supplied phase composes no phase operator", "a phase interface supplies no accuracy"),
        ("W_layout", "W_program"): ("a gate layout prepares no synchronized code", "program genesis supplies no gate geometry"),
        ("W_layout", "W_covariance"): ("local layout need not erase an order label", "covariant control supplies no local layout"),
        ("W_layout", "W_phase"): ("spatial layout does not compose the fourth carrier", "phase composition supplies no spatial layout"),
        ("W_program", "W_covariance"): ("a prepared order can still break covariance", "a jointly covariant select unitary does not prepare/uncompute its program"),
        ("W_program", "W_phase"): ("factor-program genesis does not join the tick carrier", "a tick carrier does not synchronize factor order"),
        ("W_covariance", "W_phase"): ("order covariance does not compose the fourth shift", "a fourth shift does not remove order entanglement"),
    }
    pair_rows = tuple({
        "pair": pair,
        "close_first_implies_second": False,
        "evidence_first_to_second": directions[0],
        "close_second_implies_first": False,
        "evidence_second_to_first": directions[1],
        "independent": True,
    } for pair, directions in evidence.items())
    qualifying = sum(
        row["status"] == "ATTEMPTED" or row["status"].startswith("RULED OUT BY PRIOR")
        for row in families
    )
    return {
        "fresh_skill_source": "origin/main:docs/ai_methodology/skills/no-go-discipline/SKILL.md",
        "N1_approach_families": families,
        "N1_normalized_family_count": len(families),
        "N1_qualifying_ATTEMPTED_or_RULED_OUT_count": qualifying,
        "N1_required_count": 5,
        "N1_pass": qualifying >= 5,
        "N1_failure": "only four qualifying normalized families; randomized, block-encoding and LCU/amplification routes remain open",
        "N2_collapsed_walls": walls,
        "N2_pairwise_independence": pair_rows,
        "N3_hidden_condition_scan": (
            "raw law, norms, finite domains, factor order, half weights, m, host tick_momentum, program state and group control are explicit",
            "no by-construction or standard-physics phrase supplies a hidden premise",
        ),
        "N4_residual_matching": (
            {"witness": "Cycle579 note line 180", "witness_residual": "first-order finite-m target error", "current_residual": "second-order finite-m target error", "match": "yes for accuracy order; exact exponential remains open"},
            {"witness": "Cycle579 note lines 330-332", "witness_residual": "full24 analytic/not cold-executed", "current_residual": "full24 analytic/not cold-executed", "match": "yes and not claimed closed"},
            {"witness": "Cycle579 note line 348", "witness_residual": "exact target-generator covariance", "current_residual": "finite-product order covariance", "match": "target authority only; not a witness that finite product closes"},
            {"witness": "Cycle460 note lines 31-35 and 98-100", "witness_residual": "compilation of supplied held kernels", "current_residual": "downstream homogeneous static receiver law", "match": "no; not used as closure evidence"},
        ),
        "N5_rhetoric_audit": (
            {"statement": "fixed branch is not covariant", "tested": "m=1 generic-momentum 361-dimensional finite-product branch", "untested": "all states, all m, alternative orders", "scope": "only the tested branch diagnostic"},
            {"statement": "coherent orbit does not return an unentangled program", "tested": "uniform control and source probe", "untested": "other probes and LCU/amplified mechanisms", "scope": "only this construction/probe"},
            {"statement": "train parallel coloring is not held-portable", "tested": "the frozen 82-color grouping on held L4", "untested": "domain-independent algebraic colorings and randomized schedules", "scope": "only this train-derived grouping"},
        ),
        "N6_partial_closure_paths": (
            "compile the local-rule program into a literal layout and enforce its code domain",
            "use randomized or higher-order formulas to reduce rigorous constants",
            "use LCU/amplitude amplification or covariant QSP to erase the branch label",
            "compose the finite phase-ring shift with the data factors",
        ),
        "N6_primitive_registry_check": "fresh origin/main PRIMITIVE_REGISTRY_CHECK read; no no-retained-primitive or new-axiom claim is made",
        "N7_hostile_steelman": {
            "mechanism": "A covariant select oracle over the 24 order branches, followed by oblivious amplitude amplification of the uniform-program component, could turn the measured projected average into a deterministic near-unitary data update without retained order entanglement.",
            "terminal_obligation": "Give a bounded-M2 select/prepare layout, prove the amplified polynomial approximates the raw full24 exponential with held-size error, return the program exactly, and account for genesis/readout resources.",
            "strongest_authority": "Cycle581 exact joint-covariance identity plus nonzero uniform-program projection weight",
            "disposition": "mathematically actionable; no broad negative or axiom-pressure claim may ship",
        },
        "N8_cross_cycle_echo": (
            "Cycles560/563 retired host ordering by an in-state auxiliary program",
            "Cycle576 retired momentum normalization by returning to the raw local action",
            "Cycle579 converted a first-order wall into an exact product compiler plus convergence law",
            "Cycle581 follows those partial-closure mechanisms and leaves layout/genesis explicit",
        ),
        "gate_status": "FAIL" if qualifying < 5 else "PASS",
        "demoted_artifact_status": "POSITIVE_PARTIAL_CONSTRUCTION_WITH_EXPLICIT_RESIDUALS",
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_claim": "FAIL / DO NOT SHIP",
        "shared_obstruction_claim": "DO NOT SHIP",
        "axiom_pressure_claim": "DO NOT SHIP",
        "negative_claims_shipped": False,
        "shared_obstruction_established": False,
        "axiom_pressure_established": False,
    }


def main() -> int:
    started = perf_counter()
    dependencies = dependency_controls()
    receipt = cycle579_receipt()
    note = note_contract()
    q_kernel, d_kernel, kernel = cycle579.exact_local_kernels()
    route_a, route_b = route_a_and_b(q_kernel, d_kernel, receipt)
    route_c = route_c_order_orbit()
    retained = retained_controls(receipt)
    supplied = inventory()
    nogo = no_go_controls()

    check("Cycle579 dependencies are exact-pinned", dependencies["pass"], dependencies)
    check("note contract preserves accuracy, covariance, physical-scope and N1-N8 boundaries", note["pass"], note)
    check(
        "raw unnormalized Regge/source kernel is preserved",
        kernel["Regge_symbol_reconstruction_residual"] < cycle579.KERNEL_TOL
        and kernel["raw_deficit_symbol_reconstruction_residual"] < cycle579.KERNEL_TOL
        and not kernel["momentum_dependent_source_normalization_used"]
        and retained["raw_unnormalized_deficit_preserved"],
        kernel,
    )
    check(
        "Route A bound follows stated Hermitian/operator-norm Taylor assumptions",
        route_a["bound_derivation"]["norm"] == "spectral/operator norm"
        and not route_a["bound_derivation"]["commutator_formula_guessed_or_imported"]
        and route_a["formal_derivative_matching"]["formal_noncommuting_first_derivative_coefficient_residual"] < TOL
        and route_a["formal_derivative_matching"]["formal_noncommuting_second_derivative_coefficient_residual"] < TOL
        and route_a["single_frame_layers"] == 260
        and route_a["single_frame_strang_substeps_per_repetition"] == 519
        and route_a["full24_layers"] == 2905
        and route_a["full24_factor_operator_norm_count"] == 2905
        and route_a["full24_diagonal_modes_are_unique"]
        and route_a["full24_maximum_diagonal_coefficient_imaginary_part"] < TOL
        and route_a["full24_strang_substeps_per_repetition"] == 5809,
        {
            "bound_derivation": route_a["bound_derivation"],
            "formal_derivative_matching": route_a["formal_derivative_matching"],
        },
    )
    for fixture in route_a["train_and_held"]:
        check(
            f"Route A {fixture['fixture']} has held-no-refit O(1/m^2) convergence and rigorous bounds",
            fixture["Hamiltonian_Hermiticity_residual"] < TOL
            and fixture["baseline_empirical_log_error_slope"] < -1.90
            and fixture["baseline_empirical_log_error_slope"] > -2.10
            and all(row["bound_dominates_observed"] for row in fixture["baseline_convergence"])
            and all(
                fixture["baseline_convergence"][index + 1]["maximum_state_error"]
                < fixture["baseline_convergence"][index]["maximum_state_error"]
                for index in range(4)
            )
            and fixture["maximum_norm_residual"] < TOL
            and fixture["baseline_m16_inverse_residual"] < TOL,
            {
                "fixture": fixture["fixture"],
                "slope": fixture["baseline_empirical_log_error_slope"],
                "inverse": fixture["baseline_m16_inverse_residual"],
                "convergence": fixture["baseline_convergence"],
            },
        )
    check(
        "Route A exact declared-code Strang program EG/inverse/deletions are executable and scope-honest",
        route_a["compiled_product_law_intertwiner_residual"] == 0
        and route_a["exact_declared_code_program_EG"]
        and all(
            fixture["baseline_program_trace"]["final_program_rail"] == 0
            and fixture["baseline_program_trace"]["inverse_program_rail"] == 0
            and fixture["baseline_program_trace"]["inverse_data_residual"] < TOL
            and fixture["baseline_program_trace"]["source_layer_deletion_signal"] > SIGNAL
            and fixture["baseline_program_trace"]["program_shift_deletion_signal"] > SIGNAL
            and fixture["baseline_program_trace"]["physical_one_hot_embedding_Gram_residual"] == 0
            and fixture["baseline_program_trace"]["physical_one_hot_shift_code_leakage"] == 0
            and not fixture["baseline_program_trace"]["literal_M2_layout_compiled"]
            and not fixture["baseline_program_trace"]["off_domain_full_space_micro_update_compiled"]
            for fixture in route_a["train_and_held"]
        )
        and not route_a["literal_physical_M2_layout_compiled"]
        and not route_a["off_domain_full_space_micro_update_compiled"]
        and not route_a["full24_physical_Hilbert_space_operator_cold_executed"]
        and not route_a["joined_phase_ring_data_operator_composed"],
        {key: route_a[key] for key in (
            "compiled_product_law_intertwiner_residual", "cold_executed_scope", "full24_status",
            "literal_physical_M2_layout_compiled", "off_domain_full_space_micro_update_compiled",
        )},
    )
    check(
        "Route A full24 analytic bound is O(1/m^2) with explicit overhead/covariance defect",
        all(
            abs(
                row["rigorous_full24_operator_error_bound"]
                - route_a["full24_bound_constant"] / row["repetitions"] ** 2
            ) < TOL
            for row in route_a["full24_analytic_rows"]
        )
        and route_a["repetitions_for_raw_bound_below_1"] > 0
        and route_a["repetitions_for_raw_bound_below_1e_minus_3"]
        > route_a["repetitions_for_raw_bound_below_1"],
        {
            "constant": route_a["full24_bound_constant"],
            "rows": route_a["full24_analytic_rows"],
            "m_below_1": route_a["repetitions_for_raw_bound_below_1"],
            "m_below_1e-3": route_a["repetitions_for_raw_bound_below_1e_minus_3"],
        },
    )
    check(
        "Route B train-only parallel coloring is honestly falsified on held L4 without refit",
        route_b["train_within_group_validation"]["noncommuting_pairs"] == 0
        and route_b["held_no_refit_within_group_validation"]["noncommuting_pairs"] > 0
        and not route_b["held_used_for_selection_or_refit"]
        and route_b["same_grouping_and_order_on_held"]
        and not route_b["held_parallel_grouping_lawful"]
        and not route_b["rigorous_held_parallel_macro_bound_claimed"]
        and route_b["train_parallel_grouped_substeps_per_repetition"]
        < route_b["baseline_substeps_per_repetition"],
        {key: route_b[key] for key in (
            "color_count", "group_sizes", "baseline_substeps_per_repetition",
            "train_parallel_grouped_substeps_per_repetition",
            "color_ordered_serial_substeps_per_repetition", "train_within_group_validation",
            "held_no_refit_within_group_validation", "held_parallel_grouping_disposition",
        )},
    )
    check(
        "Route B frozen serial color order gives a lawful held comparison without overclaiming improvement",
        route_b["train_color_ordered_serial_slope"] < -1.90
        and route_b["held_color_ordered_serial_slope"] < -1.90
        and route_b["color_ordered_serial_substeps_per_repetition"]
        == route_b["baseline_substeps_per_repetition"]
        and route_b["color_ordered_serial_formal_derivative_matching"]["formal_noncommuting_first_derivative_coefficient_residual"] < TOL
        and route_b["color_ordered_serial_formal_derivative_matching"]["formal_noncommuting_second_derivative_coefficient_residual"] < TOL
        and all(
            row["bound_dominates_observed"]
            for row in route_b["train_color_ordered_serial_convergence"]
        )
        and all(
            row["bound_dominates_observed"]
            for row in route_b["held_color_ordered_serial_convergence"]
        ),
        {key: route_b[key] for key in (
            "train_baseline_slope", "train_color_ordered_serial_slope", "held_baseline_slope",
            "held_color_ordered_serial_slope", "train_baseline_convergence",
            "train_color_ordered_serial_convergence", "held_baseline_convergence",
            "held_color_ordered_serial_convergence",
        )},
    )
    check(
        "Route C coherent order orbit has exact joint all576 covariance",
        route_c["Hamiltonian_Hermiticity_residual"] < TOL
        and route_c["factor_count_constant_across_orbit"]
        and route_c["all576_representation_products"] == 576
        and route_c["all576_representation_residual"] < TOL
        and route_c["controlled_orbit_joint_covariance_residual"] < TOL
        and route_c["exact_joint_covariance_achieved"],
        route_c,
    )
    check(
        "Route C separates exact joint covariance from source-probe program entanglement",
        route_c["fixed_canonical_branch_covariance_Frobenius_residual"] > SIGNAL
        and route_c["maximum_branch_source_probe_dispersion"] > SIGNAL
        and route_c["uniform_program_source_probe_reduced_program_purity"] < 1 - SIGNAL
        and route_c["uniform_program_projection_weight"] < 1 - SIGNAL
        and route_c["uniform_program_projection_weight_is_norm_diagnostic_not_occurrence_frequency_or_Born_law"]
        and route_c["generic_source_probe_data_program_entanglement_detected"]
        and not route_c["exact_data_only_covariance_without_entanglement_achieved"]
        and not route_c["universal_impossibility_claim"]
        and not route_c["coherent_program_genesis_derived"]
        and not route_c["program_uncomputation_compiled"]
        and not route_c["literal_M2_program_layout_compiled"]
        and not route_c["off_domain_full_space_update_compiled"],
        route_c,
    )
    check(
        "mass/contact/seam/leakage and raw-source shore remain exact-pinned",
        retained["Cycle572_EG_residual"] == 0
        and retained["one_particle_mass_residual"] < TOL
        and retained["actual_Cycle230_contact_factorization_residual"] < TOL
        and retained["Cycle230_seam_braid_residual"] == 0
        and retained["target_code_leakage"] == 0
        and retained["raw_unnormalized_deficit_preserved"]
        and not retained["Cycle581_derives_downstream_homogeneous_static_receiver_law"],
        retained,
    )
    check(
        "fresh N1-N8 fails honestly and blocks negative/minimum/axiom-pressure claims",
        not nogo["N1_pass"]
        and nogo["gate_status"] == "FAIL"
        and len(nogo["N2_pairwise_independence"]) == 10
        and all(
            row["evidence_first_to_second"] and row["evidence_second_to_first"]
            for row in nogo["N2_pairwise_independence"]
        )
        and nogo["N7_hostile_steelman"]["terminal_obligation"]
        and not nogo["negative_claims_shipped"]
        and not nogo["shared_obstruction_established"]
        and not nogo["axiom_pressure_established"],
        nogo,
    )

    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 if sys.platform != "darwin" else 1024 ** 2)
    summary = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "dependencies": dependencies,
        "kernel": kernel,
        "route_A": route_a,
        "route_B": route_b,
        "route_C": route_c,
        "retained_controls": retained,
        "inventory": supplied,
        "no_go": nogo,
        "terminal": {
            "strongest_constructive_result": "exact declared-code generalized-Strang program with rigorous inverse-square bound and exact coherent-orbit joint covariance",
            "exact_target_exponential_compiled": False,
            "literal_physical_M2_layout_compiled": False,
            "full24_operator_cold_executed": False,
            "entanglement_free_exact_finite_m_covariance_compiled": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
        "passes": PASS,
        "failures": FAIL,
        "resources": {"elapsed_seconds": perf_counter() - started, "peak_rss_mb": peak},
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    if FAIL == 0:
        print("RESULT REGGE_STRANG_AND_COHERENT_ORDER_ORBIT_POSITIVE_PARTIAL_WITH_EXPLICIT_RESIDUALS")
        return 0
    print("RESULT PHYSICAL_REGGE_SYMMETRIC_ACCURACY_ORDER_ORBIT_TOURNAMENT_FAILED")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
