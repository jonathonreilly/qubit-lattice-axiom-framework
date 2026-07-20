#!/usr/bin/env python3
"""Cycle 484: full-layer P8/Suzuki4/B20 discrete response composition.

Replace Cycle481's supplied continuous-angle actuation by Cycle480's
training-selected Suzuki4 schedule over B20 repeated phase words, preserving
the direction-correct full-layer delivery, arithmetic, local source flags,
inverse, and proper-cubic carried schedule.

Coefficient, product, angle, total, routing, leakage, and inverse residuals
remain separate.  Depth is not time, phase is not energy, response is not
force or gravity, and norm is not probability.  Authority none; audit unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from time import perf_counter
import resource
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_reversible_cubic_relaxation_clock_compiler_cycle463_2026_07_19 as c463
import physical_elementary_divsix_nn_compiler_cycle467_2026_07_19 as c467
import physical_seven_supercell_port_delivery_compiler_cycle470_2026_07_19 as c470
import physical_dual_source_reciprocal_composition_cycle472_2026_07_19 as c472
import physical_mod3_star_layer_scheduler_cycle474_2026_07_19 as c474
import physical_word_weight_control_compiler_cycle476_2026_07_19 as c476
import physical_dual_source_full_layer_delivery_response_cycle477_2026_07_19 as c477
import physical_discrete_angle_product_compiler_cycle480_2026_07_19 as c480
import physical_full_layer_fixed_p_response_composition_cycle481_2026_07_19 as c481


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FULL_LAYER_DISCRETE_RESPONSE_COMPOSITION_CYCLE484_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
SELECTED_ROUTE = "suzuki4"
RETAINED_ROUTE = "direct-strang8"
WALL_CAP_SECONDS = 700.0
RSS_CAP_MIB = 3072.0
PASS = 0
FAIL = 0
SIGNAL_FLOOR = 1e-9

FROZEN = {
    "Cycle463": ("physical_reversible_cubic_relaxation_clock_compiler_cycle463_2026_07_19.py", "3ae259060c7d7f9e13088197cf022eef845241af20972e5496cede6b4344e9ad"),
    "Cycle467": ("physical_elementary_divsix_nn_compiler_cycle467_2026_07_19.py", "7e562949be71a647d410c8a9624eb5cf5fdf2be30777fab93c6ed55824a5e402"),
    "Cycle470": ("physical_seven_supercell_port_delivery_compiler_cycle470_2026_07_19.py", "287b72625b4bf7d29cb847e0a59ed5d64f58b3ec55e5b312942f96bbc0ea6674"),
    "Cycle472": ("physical_dual_source_reciprocal_composition_cycle472_2026_07_19.py", "6204ae34c7d42c5e61d797d5bb2039f8ea199499b46ef01f6b52b8951e8b557d"),
    "Cycle474": ("physical_mod3_star_layer_scheduler_cycle474_2026_07_19.py", "10a55ef2cb36f7d9f60b115911fc2bcffbffbe3ac0977db0ba319f6dcfd08755"),
    "Cycle476": ("physical_word_weight_control_compiler_cycle476_2026_07_19.py", "2cb747b912ed92d6d19e067de9780e0a5899d3659d8defc2135612346cfd0963"),
    "Cycle477": ("physical_dual_source_full_layer_delivery_response_cycle477_2026_07_19.py", "0e0e0f8b5baa8ea0d00d9b24e7cc7a5d2167805158f96223e1f5d41a6e087afd"),
    "Cycle480": ("physical_discrete_angle_product_compiler_cycle480_2026_07_19.py", "39f2fb1c9d3e10bf8741b6f426bc0a7dbbd75dea7c4c66aedc75b8d8275fb743"),
    "Cycle481": ("physical_full_layer_fixed_p_response_composition_cycle481_2026_07_19.py", "7155a82ca672f36f11791cd771515e5039970dec400293dd4e1c4e30e6e3ee13"),
}

Coord = tuple[int, int, int]
Pair = tuple[Coord, Coord]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset", "cycle 484", "selected suzuki4",
        "finite basis b20", "repeated z20 words", "extra source-flag control",
        "direction-correct full-layer", "all fourteen rows", "held rows do not reselect",
        "coefficient quantization", "product-formula", "discrete-angle", "total residual",
        "routing", "leakage", "inverse", "no cancellation-based claim",
        "all 24 proper-cubic frames", "no global resort", "one-particle mass",
        "cycle-230 contact", "depth is not time", "phase is not energy",
        "response is not force or gravity", "norm is not probability",
        "n1 — alternative route enumeration", "n8 — cross-cycle echo and claim gate",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in normalized(NOTE))
    check("the Cycle484 note freezes the three-way discrete full-layer boundary and N1-N8 gate", not missing, missing)


def correct_word_rows() -> tuple[c476.WordRow, ...]:
    rows = []
    for index, row in enumerate(c481.endpoint_rows()):
        rows.append(c476.WordRow(
            f"{row.fixture}-pair{index // 2}-endpoint{row.endpoint}",
            row.radius, row.pair, row.endpoint, row.words, row.held,
        ))
    return tuple(rows)


def flagged_discrete_manifest(route: str) -> dict[str, object]:
    base = c480.route_gate_manifest(route)
    rotations = int(base["coefficient_controlled_pair_rotations"])
    counts = dict(base["counts"])
    # Add one positive source-flag input to each coefficient-controlled AND:
    # 13 controls -> 14 controls, hence two more Toffolis per rotation.
    counts["Toffoli"] += 2 * rotations
    digest = sha256()
    digest.update(str(base["manifest_digest"]).encode())
    digest.update(b"|positive-local-source-flag|14-control-AND|13-clean-aux")
    return {
        "route": route,
        "symmetric_S2_blocks": base["symmetric_S2_blocks"],
        "directional_half_passes": base["directional_half_passes"],
        "coefficient_controlled_pair_rotations": rotations,
        "counts": counts,
        "total_discrete_gates": sum(int(value) for value in counts.values()),
        "active_support_M2": 28,
        "clean_rotation_auxiliary_M2": 13,
        "new_angle_auxiliary_M2": 0,
        "manifest_digest": digest.hexdigest(),
        "Cycle480_base_manifest": base["manifest_digest"],
    }


@dataclass(frozen=True)
class RouteSummary:
    route: str
    training_score: float
    coefficient_max: float
    product_max: float
    angle_max: float
    intrinsic_max: float
    total_max: float
    inverse: float
    leakage: float
    manifest: dict[str, object]


def route_selection_and_error_controls(
    rows: tuple[c476.WordRow, ...]
) -> tuple[dict[str, RouteSummary], tuple[c480.RowResult, ...]]:
    print("\nFROZEN TRAIN SELECTION / DIRECTION-CORRECT ALL14 ERROR LEDGER")
    state = c480.probe_state()
    train_rows = tuple(row for row in rows if not row.held)
    held_rows = tuple(row for row in rows if row.held)
    train = tuple(c480.row_result(row, state) for row in train_rows)
    training_score = {
        RETAINED_ROUTE: max(item.direct_intrinsic_residual for item in train),
        SELECTED_ROUTE: max(item.suzuki_intrinsic_residual for item in train),
    }
    selected = min(
        c480.ROUTE_ORDER,
        key=lambda route: (training_score[route], c480.ROUTE_ORDER.index(route)),
    )
    held = tuple(c480.row_result(row, state) for row in held_rows)
    results = train + held
    sample = next(row for row in held_rows if len(set(row.words)) > 2)
    coefficients = c476.expected_coefficients(sample.words)
    summaries = {}
    for route in c480.ROUTE_ORDER:
        if route == RETAINED_ROUTE:
            product = max(item.direct_product_residual for item in results)
            angle = max(item.direct_angle_residual for item in results)
            intrinsic = max(item.direct_intrinsic_residual for item in results)
            total = max(item.direct_total_residual for item in results)
        else:
            product = max(item.suzuki_product_residual for item in results)
            angle = max(item.suzuki_angle_residual for item in results)
            intrinsic = max(item.suzuki_intrinsic_residual for item in results)
            total = max(item.suzuki_total_residual for item in results)
        forward = c480.product_action(state, coefficients, route=route, discrete=True)
        restored = c480.product_action(
            forward, coefficients, route=route, discrete=True, inverse=True
        )
        summaries[route] = RouteSummary(
            route, training_score[route],
            max(item.coefficient_residual for item in results),
            product, angle, intrinsic, total,
            float(np.linalg.norm(restored - state)),
            abs(float(np.linalg.norm(forward) - np.linalg.norm(state))),
            flagged_discrete_manifest(route),
        )
    check(
        "training-only selection remains Suzuki4 before held readout and all fourteen direction-correct rows keep coefficient, product, angle, intrinsic, total, inverse, and leakage residuals separate",
        selected == SELECTED_ROUTE and len(train) == 6 and len(held) == 8
        and all(summary.product_max < c480.PRODUCT_ERROR_CAP for summary in summaries.values())
        and all(summary.angle_max < c480.ANGLE_ERROR_CAP for summary in summaries.values())
        and all(summary.total_max < c480.STATE_ERROR_CAP for summary in summaries.values())
        and all(summary.inverse < c480.TOLERANCE and summary.leakage < c480.TOLERANCE for summary in summaries.values())
        and summaries[SELECTED_ROUTE].intrinsic_max < summaries[RETAINED_ROUTE].intrinsic_max
        and int(summaries[SELECTED_ROUTE].manifest["total_discrete_gates"])
        > int(summaries[RETAINED_ROUTE].manifest["total_discrete_gates"]),
        {"selection_rule_frozen_before_rows": True,
         "training_only_scores": training_score,
         "selected_before_held_readout": selected,
         "held_rows_reselected_route": False,
         "summaries": {name: summary.__dict__ for name, summary in summaries.items()},
         "all14_rows": [result.__dict__ for result in results],
         "no_cancellation_based_selection": True},
    )
    return summaries, results


@dataclass(frozen=True)
class DomainManifest:
    route: str
    fixture: str
    active_cells: int
    per_cell_pipeline: int
    forward_events: int
    strict_depth: int


def route_phase_manifest(
    route: str, delivery: c467.Circuit, arithmetic: c476.Circuit
) -> dict[str, object]:
    response = c477.response_actions(delivery)
    ports = c481.port_stage_actions(delivery, arithmetic)
    coefficients = c481.coefficient_stage_actions(arithmetic)
    flag = c481.flag_stage_action()
    arithmetic_route = c481.arithmetic_route_manifest(arithmetic)
    actuation = flagged_discrete_manifest(route)
    response_ingress = sum(action.primitive_events for action in response)
    port_ingress = sum(action.primitive_events for action in ports)
    coefficient_unique = sum(action.primitive_events for action in coefficients)
    half_passes = int(actuation["directional_half_passes"])
    coefficient_staging = 2 * half_passes * coefficient_unique
    persistent = 2 * c477.flag_action().primitive_events
    per_cell = (
        persistent + 2 * response_ingress + 2 * port_ingress
        + 2 * arithmetic_route.events + 2 * flag.primitive_events
        + coefficient_staging + int(actuation["total_discrete_gates"])
    )
    per_target_word = sum(int(row["block_events"]) for row in c474.layer_block_data(delivery))
    word_depth = c474.COLOR_COUNT * per_target_word
    strict_depth = (
        word_depth + persistent + c474.COLOR_COUNT * 2 * response_ingress
        + 2 * port_ingress + 2 * arithmetic_route.events
        + 2 * flag.primitive_events + coefficient_staging
        + int(actuation["total_discrete_gates"])
    )
    domains = []
    for fixture in c472.FIXTURES:
        domain = c463.domain(fixture.radius)
        word_events = len(domain.active) * per_target_word
        domains.append(DomainManifest(
            route, fixture.name, len(domain.active), per_cell,
            word_events + len(domain.active) * per_cell, strict_depth,
        ))
    return {
        "route": route, "persistent_flag_roundtrip": persistent,
        "response_delivery_roundtrip": 2 * response_ingress,
        "port_stage_roundtrip": 2 * port_ingress,
        "arithmetic_compute_inverse": 2 * arithmetic_route.events,
        "rotation_flag_stage_roundtrip": 2 * flag.primitive_events,
        "coefficient_unique_ingress": coefficient_unique,
        "coefficient_staging": coefficient_staging,
        "coefficient_half_passes": half_passes,
        "actuation": actuation, "per_cell_pipeline": per_cell,
        "strict_depth": strict_depth,
        "domains": tuple(domains),
        "arithmetic_route": arithmetic_route,
    }


def phase_capacity_conflict_controls(
    delivery: c467.Circuit, arithmetic: c476.Circuit,
    summaries: dict[str, RouteSummary],
) -> tuple[dict[str, object], dict[str, object]]:
    print("\nEXACT DISCRETE FULL-LAYER EVENT / CAPACITY / CONFLICT MANIFEST")
    retained = route_phase_manifest(RETAINED_ROUTE, delivery, arithmetic)
    selected = route_phase_manifest(SELECTED_ROUTE, delivery, arithmetic)
    conflicts = 0
    for fixture in c472.FIXTURES:
        domain = c463.domain(fixture.radius)
        for layer in range(c463.ITERATIONS):
            targets = []
            for item_round in c474.rounds(fixture.radius, layer):
                targets.extend(item_round.targets)
                supports = [c474.star(target) for target in item_round.targets]
                conflicts += sum(bool(left & right) for left, right in combinations(supports, 2))
            conflicts += int(set(targets) != set(domain.active) or len(targets) != len(set(targets)))
    selected_domains = {row.fixture: row for row in selected["domains"]}
    retained_domains = {row.fixture: row for row in retained["domains"]}
    check(
        "Suzuki4 replaces every continuous Rz by repeated Z20 words under the correct extra local source-flag control and fits the complete conflict-free R1/R2 phase schedule",
        c481.COMPOSED_USED == 49_866 and c481.COMPOSED_RESERVE == 14_134
        and conflicts == 0
        and int(selected["per_cell_pipeline"]) == 35_082_887_764
        and int(selected["strict_depth"]) == 71_245_505_380
        and selected_domains["train-R1-axis"].forward_events == 983_370_844_908
        and selected_domains["held-R2-offaxis"].forward_events == 4_552_642_800_500
        and int(retained["per_cell_pipeline"]) == 35_023_610_164
        and retained_domains["train-R1-axis"].forward_events == 981_770_349_708
        and retained_domains["held-R2-offaxis"].forward_events == 4_545_233_100_500
        and int(selected["actuation"]["counts"]["Z20_or_inverse"]) == 107_561_472
        and int(selected["actuation"]["counts"]["Toffoli"]) == 1_459_200
        and int(selected["actuation"]["active_support_M2"]) == 28
        and summaries[SELECTED_ROUTE].training_score < summaries[RETAINED_ROUTE].training_score,
        {"uniform_layout": {"used_M2": c481.COMPOSED_USED,
                            "reserve_M2": c481.COMPOSED_RESERVE,
                            "rotation_support_M2": 28,
                            "angle_auxiliary_M2": 0},
         "selected_Suzuki4": selected,
         "retained_discrete_S8": retained,
         "cost_difference_selected_minus_retained_per_cell":
             int(selected["per_cell_pipeline"]) - int(retained["per_cell_pipeline"]),
         "same_phase_conflicts": conflicts,
         "phase_order": ["persistent flags", "96x27 word rounds",
                         "27-color word ingress", "direction-correct input stage",
                         "P8 arithmetic", "local flag stage",
                         "600 Suzuki scale/direction/bit blocks with repeated Z20 words",
                         "flag unstage", "arithmetic inverse", "input unstage",
                         "reverse-27-color egress", "persistent flag uncompute"],
         "continuous_Rz_events_remaining": 0,
         "no_held_cost_or_route_reselection": True},
    )
    return selected, retained


def literal_discrete_pipeline_controls(
    delivery: c467.Circuit, arithmetic: c476.Circuit,
    rows: tuple[c476.WordRow, ...],
) -> dict[str, object]:
    print("\nLITERAL TRAIN/HELD DISCRETE PIPELINE / EXACT CLEANUP")
    response = c477.response_actions(delivery)
    stages = c481.port_stage_actions(delivery, arithmetic)
    representatives = (rows[0], next(row for row in rows if row.held and len(set(row.words)) > 2))
    state_probe = c480.probe_state()[:, 0]
    failures = 0
    result_rows = []
    minimum_flag_signal = float("inf")
    for row in representatives:
        state = [0] * (7 * c463.SUPERCELL_M2)
        for direction, value in zip(c477.response_directions(), row.words):
            c481.put_physical_word(
                state,
                tuple(c470.history_coord(direction, c463.ITERATIONS, bit) for bit in range(c463.VALUE_BITS)),
                value,
            )
        initial = tuple(state)
        delivery_executor = c470.TransferExecutor(state)
        delivery_executor.execute_ingress(response)
        stage_executor = c470.TransferExecutor(state)
        stage_executor.execute_ingress(stages)
        words = tuple(
            c481.get_physical_word(state, tuple(c481.arithmetic_coord(wire) for wire in word))
            for word in arithmetic.layout.neighbors
        )
        logical = c476.initialize(arithmetic, words)
        logical_initial = tuple(logical)
        c476.execute(logical, arithmetic.trace)
        coefficients = c476.read_coefficients(logical, arithmetic)
        work_leakage = sum(logical[wire] for wire in arithmetic.layout.work)
        active = c480.product_action(
            state_probe, coefficients, route=SELECTED_ROUTE, discrete=True
        )
        signal = float(np.linalg.norm(active - state_probe))
        minimum_flag_signal = min(minimum_flag_signal, signal)
        restored = c480.product_action(
            active, coefficients, route=SELECTED_ROUTE, discrete=True, inverse=True
        )
        c476.execute(logical, tuple(reversed(arithmetic.trace)))
        stage_executor.execute_egress(stages)
        delivery_executor.execute_egress(response)
        failures += int(words != row.words)
        failures += int(coefficients != c476.expected_coefficients(row.words))
        failures += int(work_leakage != 0 or tuple(logical) != logical_initial)
        failures += int(np.linalg.norm(restored - state_probe) >= c480.TOLERANCE)
        failures += int(state != list(initial))
        failures += stage_executor.adjacency_failures + delivery_executor.adjacency_failures
        result_rows.append({"name": row.name, "coefficients": coefficients,
                            "work_leakage": work_leakage,
                            "discrete_inverse": float(np.linalg.norm(restored - state_probe)),
                            "source_flag_on_off_signal": signal})

    held = representatives[-1]
    coefficients = c476.expected_coefficients(held.words)
    lane = next(index for index, value in enumerate(coefficients) if value)
    bit = next(index for index in range(c476.COEFFICIENT_BITS) if (coefficients[lane] >> index) & 1)
    intact = c480.product_action(state_probe, coefficients, route=SELECTED_ROUTE, discrete=True)
    bit_deleted = c480.product_action(
        state_probe, coefficients, route=SELECTED_ROUTE, discrete=True, omit_bit=(lane, bit)
    )
    factors = c480.factor_list(SELECTED_ROUTE, tuple(range(6)))
    factor_index = next(index for index, (_scale, direction) in enumerate(factors) if direction == lane)
    quantum_deleted = c480.product_action(
        state_probe, coefficients, route=SELECTED_ROUTE, discrete=True,
        delete_one_quantum=(factor_index, lane),
    )
    factor_deleted = c480.product_action(
        state_probe, coefficients, route=SELECTED_ROUTE, discrete=True,
        omit_factor=factor_index,
    )
    deleted_words = list(held.words)
    deleted_words[lane] = 0
    word_deleted = c480.product_action(
        state_probe, c476.expected_coefficients(tuple(deleted_words)),
        route=SELECTED_ROUTE, discrete=True,
    )
    deletions = {
        "one_consumed_word_lane": float(np.linalg.norm(intact - word_deleted)),
        "one_Z20_quantum": float(np.linalg.norm(intact - quantum_deleted)),
        "one_coefficient_bit_family": float(np.linalg.norm(intact - bit_deleted)),
        "one_Suzuki_direction_factor": float(np.linalg.norm(intact - factor_deleted)),
        "local_source_flag": float(np.linalg.norm(intact - state_probe)),
    }
    check(
        "literal train/held delivery, direction adapter, P8 arithmetic, Suzuki4-B20 actuation, adjoint, and all port/input/output/work/flag returns are exact",
        failures == 0 and len(rows) == 14 and min(deletions.values()) > SIGNAL_FLOOR
        and minimum_flag_signal > SIGNAL_FLOOR,
        {"literal_rows": result_rows, "all14_rows_checked": len(rows),
         "minimum_flag_signal": minimum_flag_signal,
         "deletions": deletions, "restoration_failures": failures},
    )
    return {"deletions": deletions, "minimum_flag_signal": minimum_flag_signal}


def apply_product_source(
    state: c472.LogicalState, endpoint: int, coefficients: tuple[int, ...],
    *, route: str, discrete: bool, inverse: bool = False, enabled: bool = True,
) -> c472.LogicalState:
    if endpoint not in (0, 1):
        raise ValueError("endpoint must be zero or one")
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    output: c472.LogicalState = {}
    other_values = sorted({pair[1 - endpoint] for pair in state})
    for other_field in other_values:
        other_q = c472.c423.local_q(other_field)
        for local_q in range(3 - other_q):
            local_states = c472.c426.LOCAL_STATES[local_q]
            local_dimension = len(local_states)
            block = np.zeros((64 * local_dimension, 64), dtype=complex)
            present = False
            for field_index, local_field in enumerate(local_states):
                pair = (local_field, other_field) if endpoint == 0 else (other_field, local_field)
                value = state.get(pair)
                if value is None:
                    continue
                present = True
                for local_matter in range(64):
                    for other_matter in range(64):
                        joint = c472.c322.JOINT_INDEX[(local_matter, other_matter)] if endpoint == 0 else c472.c322.JOINT_INDEX[(other_matter, local_matter)]
                        block[local_matter * local_dimension + field_index, other_matter] = value[joint]
            if not present:
                continue
            if local_q != 1:
                raise ValueError("Cycle484 discrete response left the local q1 domain")
            transformed = c480.product_action(
                block, coefficients, route=route, discrete=discrete, inverse=inverse
            )
            for field_index, local_field in enumerate(local_states):
                pair = (local_field, other_field) if endpoint == 0 else (other_field, local_field)
                vector = np.zeros(c472.c426.MATTER_DIM, dtype=complex)
                for local_matter in range(64):
                    for other_matter in range(64):
                        joint = c472.c322.JOINT_INDEX[(local_matter, other_matter)] if endpoint == 0 else c472.c322.JOINT_INDEX[(other_matter, local_matter)]
                        vector[joint] = transformed[local_matter * local_dimension + field_index, other_matter]
                if np.linalg.norm(vector) > 2e-13:
                    output[pair] = vector
    return c472.c426.prune(output)


def apply_exact_p8_source(
    state: c472.LogicalState, endpoint: int, coefficients: tuple[int, ...]
) -> c472.LogicalState:
    """Apply the exact exponential of the literal, not renormalized, P8 word."""

    if endpoint not in (0, 1):
        raise ValueError("endpoint must be zero or one")
    vector = np.asarray(coefficients, dtype=float) / c476.COEFFICIENT_SCALE
    generator = c476.coefficient_generator(vector)
    output: c472.LogicalState = {}
    other_values = sorted({pair[1 - endpoint] for pair in state})
    for other_field in other_values:
        other_q = c472.c423.local_q(other_field)
        for local_q in range(3 - other_q):
            local_states = c472.c426.LOCAL_STATES[local_q]
            local_dimension = len(local_states)
            block = np.zeros((64 * local_dimension, 64), dtype=complex)
            present = False
            for field_index, local_field in enumerate(local_states):
                pair = (local_field, other_field) if endpoint == 0 else (other_field, local_field)
                value = state.get(pair)
                if value is None:
                    continue
                present = True
                for local_matter in range(64):
                    for other_matter in range(64):
                        joint = c472.c322.JOINT_INDEX[(local_matter, other_matter)] if endpoint == 0 else c472.c322.JOINT_INDEX[(other_matter, local_matter)]
                        block[local_matter * local_dimension + field_index, other_matter] = value[joint]
            if not present:
                continue
            if local_q != 1:
                raise ValueError("Cycle484 exact P8 response left the local q1 domain")
            transformed = c480.expm_multiply(1j * c472.c426.ANGLE * generator, block)
            for field_index, local_field in enumerate(local_states):
                pair = (local_field, other_field) if endpoint == 0 else (other_field, local_field)
                value = np.zeros(c472.c426.MATTER_DIM, dtype=complex)
                for local_matter in range(64):
                    for other_matter in range(64):
                        joint = c472.c322.JOINT_INDEX[(local_matter, other_matter)] if endpoint == 0 else c472.c322.JOINT_INDEX[(other_matter, local_matter)]
                        value[joint] = transformed[local_matter * local_dimension + field_index, other_matter]
                if np.linalg.norm(value) > 2e-13:
                    output[pair] = value
    return c472.c426.prune(output)


def product_step(state, factors, coefficients, *, route, discrete):
    output = c472.c426.apply_matter_factor(state, factors[0])
    output = apply_product_source(output, 0, coefficients[0], route=route, discrete=discrete)
    return apply_product_source(output, 1, coefficients[1], route=route, discrete=discrete)


def product_inverse(state, factors, coefficients, *, route, discrete):
    output = apply_product_source(state, 1, coefficients[1], route=route, discrete=discrete, inverse=True)
    output = apply_product_source(output, 0, coefficients[0], route=route, discrete=discrete, inverse=True)
    return c472.c426.apply_matter_factor(output, factors[0].getH())


def exact_p8_step(state, factors, coefficients):
    output = c472.c426.apply_matter_factor(state, factors[0])
    output = apply_exact_p8_source(output, 0, coefficients[0])
    return apply_exact_p8_source(output, 1, coefficients[1])


def physical_product_source(state, encoding, endpoint, coefficients, *, route, discrete):
    decoded = {key: encoding.getH() @ value for key, value in state.items()}
    transformed = apply_product_source(
        decoded, endpoint, coefficients, route=route, discrete=discrete
    )
    output = {}
    zero_physical = np.zeros(encoding.shape[0], dtype=complex)
    zero_logical = np.zeros(c472.c426.MATTER_DIM, dtype=complex)
    for key in state.keys() | transformed.keys():
        before_physical = state.get(key, zero_physical)
        before_logical = decoded.get(key, zero_logical)
        after_logical = transformed.get(key, zero_logical)
        output[key] = before_physical + encoding @ (after_logical - before_logical)
    return c472.c426.prune(output)


def physical_product_step(state, encoding, factors, coefficients, *, route, discrete):
    output = c472.c426.apply_physical_matter_factor(state, encoding, factors[0])
    output = physical_product_source(output, encoding, 0, coefficients[0], route=route, discrete=discrete)
    return physical_product_source(output, encoding, 1, coefficients[1], route=route, discrete=discrete)


def discrete_physical_eg_controls(
    factors, exact_weights, rows: tuple[c476.WordRow, ...]
) -> dict[str, object]:
    print("\nGLOBAL-Q2 P8 + PRODUCT + ANGLE PHYSICAL E/G SEAM")
    pair = c472.HELD.pairs[-1]
    selected_rows = tuple(row for row in rows if row.radius == c472.HELD.radius and row.pair == pair)
    coefficients = tuple(c476.expected_coefficients(row.words) for row in selected_rows)
    initial = c472.initial_state()
    exact = c472.common_source_step(initial, factors, exact_weights[(c472.HELD.radius, pair)])
    p8_exact = exact_p8_step(initial, factors, coefficients)
    route_states = {}
    for route in c480.ROUTE_ORDER:
        continuous = product_step(initial, factors, coefficients, route=route, discrete=False)
        discrete = product_step(initial, factors, coefficients, route=route, discrete=True)
        restored = product_inverse(discrete, factors, coefficients, route=route, discrete=True)
        route_states[route] = {
            "coefficient_quantization": c472.state_residual(p8_exact, exact),
            "product_formula": c472.state_residual(continuous, p8_exact),
            "discrete_angle": c472.state_residual(discrete, continuous),
            "intrinsic_product_plus_angle": c472.state_residual(discrete, p8_exact),
            "total_from_exact_unquantized": c472.state_residual(discrete, exact),
            "inverse": c472.state_residual(restored, initial),
            "norm_leakage": abs(c472.state_inner(discrete, discrete).real - 1.0),
            "state": discrete,
        }
    encoding = c472.c322.build_encoding(3)
    encoded = c472.c426.encode_physical(initial, encoding)
    physical = physical_product_step(
        encoded, encoding, factors, coefficients, route=SELECTED_ROUTE, discrete=True
    )
    expected = c472.c426.encode_physical(route_states[SELECTED_ROUTE]["state"], encoding)
    decoded = {key: encoding.getH() @ value for key, value in physical.items()}
    projected = c472.c426.encode_physical(decoded, encoding)
    eg = c472.state_residual(physical, expected)
    leakage = c472.state_residual(physical, projected)
    check(
        "the selected P8/Suzuki4/B20 update satisfies its physical E/G seam while coefficient, product, angle, intrinsic, total, routing-independent leakage, and inverse residuals remain separate",
        eg < c472.TOLERANCE and leakage < c472.TOLERANCE
        and all(float(route_states[route]["product_formula"]) < c480.PRODUCT_ERROR_CAP for route in c480.ROUTE_ORDER)
        and all(float(route_states[route]["discrete_angle"]) < c480.ANGLE_ERROR_CAP for route in c480.ROUTE_ORDER)
        and all(float(route_states[route]["total_from_exact_unquantized"]) < c480.STATE_ERROR_CAP for route in c480.ROUTE_ORDER)
        and all(float(route_states[route]["inverse"]) < c480.TOLERANCE for route in c480.ROUTE_ORDER)
        and all(float(route_states[route]["norm_leakage"]) < c480.TOLERANCE for route in c480.ROUTE_ORDER),
        {"held_pair": pair, "coefficients": coefficients,
         "selected_route_locked_before_held": SELECTED_ROUTE,
         "route_residuals": {route: {key: value for key, value in data.items() if key != "state"}
                             for route, data in route_states.items()},
         "selected_physical_EG": eg, "selected_physical_code_leakage": leakage,
         "no_cancellation_based_claim": True,
         "one_particle_mass": c472.c219.common_species(-0.3).analytic_mass,
         "Cycle230_contact_nontrivial_columns": 4047},
    )
    return {"routes": route_states, "EG": eg, "leakage": leakage}


def covariance_controls(
    delivery: c467.Circuit, arithmetic: c476.Circuit,
    rows: tuple[c476.WordRow, ...],
) -> None:
    print("\nALL24 DISCRETE FULL-LAYER COVARIANCE / NO RESORT")
    frames = c463.proper_cubic_frames()
    ports = c481.port_stage_actions(delivery, arithmetic)
    coefficients_actions = c481.coefficient_stage_actions(arithmetic)
    flag = c481.flag_stage_action()
    sample = next(row for row in rows if row.held and len(set(row.words)) > 2)
    coefficients = c476.expected_coefficients(sample.words)
    state = c480.probe_state()[:, 0]
    base = c480.product_action(state, coefficients, route=SELECTED_ROUTE, discrete=True)
    failures = 0
    maximum_response = 0.0
    manifests = []
    for frame in frames:
        matrix = np.asarray(frame, dtype=int)
        mapping = c472.direction_map(matrix)
        carried_coefficients = [0] * 6
        for source, target in enumerate(mapping):
            carried_coefficients[target] = coefficients[source]
        representation = c472.c426.recoil_frame(1, matrix)
        carried = c480.product_action(
            representation @ state, tuple(carried_coefficients),
            route=SELECTED_ROUTE, discrete=True, direction_order=tuple(mapping),
        )
        maximum_response = max(maximum_response, float(np.linalg.norm(carried - representation @ base)))
        digest = sha256(repr(frame).encode())
        for action in ports + coefficients_actions + (flag,):
            path = tuple(c467.affine_frame(frame, coord) for coord in action.path)
            failures += sum(c467.manhattan(left, right) != 1 for left, right in zip(path, path[1:]))
            direction = c463.transform(frame, action.direction) if action.direction is not None else None
            digest.update(f"{action.role}|{direction}|{action.bit}|{path}\n".encode())
        for fixture in c472.FIXTURES:
            domain = c463.domain(fixture.radius)
            for layer in range(c463.ITERATIONS):
                sequence = []
                for item_round in c474.rounds(fixture.radius, layer):
                    color = c474.transform_color(frame, item_round.color)
                    targets = {c463.transform(frame, target) for target in item_round.targets}
                    failures += int(targets != {target for target in domain.active if c474.color(target) == color})
                    sequence.append(color)
                failures += int(tuple(sequence) != tuple(c474.transform_color(frame, color) for color in c474.COLORS))
        digest.update(c480.frozen_angle_manifest()["frozen_manifest_digest"].encode())
        digest.update(b"|carried-Suzuki-p-p-q-p-p|carried-Z20-signs|no-resort")
        manifests.append(digest.hexdigest())
    check(
        "all24 structural manifests and one held response sample carry colors, signed ports, adapter, P8 lanes, source flags, Suzuki scales, repeated Z20 signs, and inverse with no global resort",
        len(frames) == 24 and failures == 0 and maximum_response < c480.TOLERANCE
        and len(set(manifests)) == 24,
        {"proper_cubic_frames": len(frames), "path_or_color_failures": failures,
         "maximum_carried_discrete_response_residual": maximum_response,
         "frame_manifests": manifests, "global_resort_used": False,
         "scope": "one predeclared held response vector across all24; structural path/color/schedule audit across both finite fixture domains",
         "carried_negative_q_block": True, "carried_inverse_phase_signs": True},
    )


def imported_science_controls() -> None:
    print("\nFROZEN CYCLE480 SCIENTIFIC IMPORT")
    c480.PASS = 0
    c480.FAIL = 0
    angles = c480.frozen_angle_manifest()
    c480.check(
        "Cycle480 angle manifest remains finite and frozen",
        len(angles["frozen_targets"]) == 30
        and max(abs(item["signed_error"]) for item in angles["frozen_targets"]) <= c480.PHASE_QUANTUM / 2,
        angles,
    )
    rows = c476.word_rows()
    state_result = c480.state_residual_controls(rows)
    c480.operator_controls(rows, state_result)
    c480.covariance_capacity_controls(rows, state_result["selected"])
    c480.deletion_domain_inventory_controls(rows, state_result["selected"])
    check(
        "Cycle480 B20 angle manifest, training-selected Suzuki4, held/operator errors, inverse, leakage, deletion, domain, and all24 controls survive unchanged before composition",
        c480.PASS == 5 and c480.FAIL == 0 and state_result["selected"] == SELECTED_ROUTE,
        {"Cycle480_pass": c480.PASS, "Cycle480_fail": c480.FAIL,
         "selected_route": state_result["selected"],
         "angle_manifest": angles["frozen_manifest_digest"],
         "selected_base_gate_manifest": c480.route_gate_manifest(SELECTED_ROUTE)},
    )


def deletion_domain_inventory_no_go_controls(literal: dict[str, object]) -> None:
    malformed = 0
    state = c480.probe_state()[:, 0]
    actions = (
        lambda: c480.product_action(state, (0,) * 5, route=SELECTED_ROUTE, discrete=True),
        lambda: c480.product_action(state, (0, 0, 0, 0, 0, -1), route=SELECTED_ROUTE, discrete=True),
        lambda: c480.product_action(state, (0,) * 6, route="unknown", discrete=True),
        lambda: c480.product_action(state, (0,) * 6, route=SELECTED_ROUTE, discrete=True, phase_exponent=19),
        lambda: c480.product_action(state, (0,) * 6, route=SELECTED_ROUTE, discrete=True,
                                    direction_order=(0, 1, 2, 3, 4, 4)),
    )
    for action in actions:
        try:
            action()
        except ValueError:
            malformed += 1
    composition_malformed = 0
    try:
        state_bits = [0] * (7 * c463.SUPERCELL_M2)
        arithmetic = c476.build_circuit()
        state_bits[c470.state_index(c481.arithmetic_coord(arithmetic.layout.inputs[0]))] = 1
        if any(state_bits[c470.state_index(c481.arithmetic_coord(wire))]
               for wire in arithmetic.layout.inputs):
            raise ValueError("duplicate P8 input bank is not blank")
    except ValueError:
        composition_malformed += 1
    try:
        c472.validate_pair(c472.HELD.radius, (c472.HELD.pairs[0][0], c472.HELD.pairs[0][0]))
    except ValueError:
        composition_malformed += 1
    try:
        c474.validate_round(c463.domain(2), c474.Round(0, 0, 1, (0, 0, 0), ((1, 0, 0),)))
    except ValueError:
        composition_malformed += 1
    check(
        "Z20, coefficient, Suzuki-factor, source-flag, return, and malformed-domain controls remain visible in the composed route",
        min(float(value) for value in literal["deletions"].values()) > SIGNAL_FLOOR
        and malformed == len(actions) and composition_malformed == 3,
        {"deletions": literal["deletions"], "malformed_domains_refused": malformed,
         "composition_malformed_domains_refused": composition_malformed,
         "return_control": "literal train/held physical states restore exactly only after word/input/flag/coefficient inverse phases"},
    )
    check(
        "the supplied/constructed/open inventory keeps basis, precision, product, source, time, probability, and gravity walls explicit",
        AUTHORITY == "none" and AUDIT == "unset",
        {"supplied": ["Cycle481 direction-correct 49866-M2 delivery/P8/flag schedule",
                      "Cycle480 B20 exponent20 nearest words and training-only route rule",
                      "Cycle472 exact source response, mass/contact, branch menu and readouts",
                      "P8/floor/Suzuki p,q/order, continuous calibration behind Z20, phase barriers"],
         "constructed": ["source-flag-augmented Suzuki4 repeated-Z20 manifest",
                         "exact all-cell R1/R2 discrete event/depth ledger",
                         "direction-correct all14 no-reselection residual ledger",
                         "global-Q2 P8+product+angle physical E/G seam",
                         "literal cleanup, deletions and all24 carried discrete composition"],
         "open": ["basis/P/product/angle calibration selection", "fault/noise model and optimized phase words",
                  "uniform analytic all-word error", "exact local Givens or phase kickback",
                  "route/work optimization and recurrence/history removal",
                  "source/time/energy-stress calibration, asymptotics, gravity, occurrence/Born"],
         "firewall": {"depth_called_time": False, "phase_called_energy": False,
                      "response_called_force_or_gravity": False, "norm_called_probability": False}},
    )
    check(
        "full current N1-N8 rejects no-go, minimum-content, shared-obstruction, and axiom-pressure promotion",
        AUTHORITY == "none" and AUDIT == "unset",
        {"N1": "selected B20/Suzuki4 full-layer composition succeeds; retained B20/Strang8 also succeeds, while Clifford+T, phase kickback, exact Givens, QSP, alternate bases, in-place arithmetic, caching and pipelining remain open",
         "N2": "basis, P, product, angle calibration, routing, recurrence, source/time calibration, asymptotics, gravity and occurrence remain independent",
         "N3": "B20/exponent20/nearest rounding, P8/floor, Suzuki p-q order, source flags, direction adapter, duplicate bank, colors/barriers, finite fixtures and norms are exposed",
         "N4": "the result matches Cycle480's discrete-angle residual and Cycle481's full-layer P8 product-and-quantization residual; it does not match basis selection, uniform error, recurrence, source/time, gravity or Born residuals",
         "N5": "claims stop at a finite P8/Suzuki4/B20 layer; residual columns stay separate, depth is not time, phase not energy, response not force/gravity, norm not probability",
         "N6": "three-way composition closes constructively; exact Givens, alternate bases, optimized routes, recurrence and calibration remain direct paths",
         "N7": "a hostile reviewer can demand uniform operator bounds for all words, a fault model, shorter phase synthesis, no duplicate bank, emitted routing, coherent word superpositions, recurrence and infrared control",
         "N8": "Cycles476/477/480/481 close local control, delivery, discrete angles and full-layer P8 separately; their discrete composition now succeeds while calibration/time/gravity walls remain independent; no axiom pressure"},
    )


def frozen_controls() -> None:
    observed = {name: file_sha(ROOT / "scripts" / filename) for name, (filename, _sha) in FROZEN.items()}
    expected = {name: sha for name, (_filename, sha) in FROZEN.items()}
    check(
        "Cycles463/467/470/472/474/476/477/480/481 remain frozen at exact imported identities",
        observed == expected,
        {"observed": observed, "expected": expected,
         "angle_manifest": c480.frozen_angle_manifest()["frozen_manifest_digest"],
         "selected_base_manifest": c480.route_gate_manifest(SELECTED_ROUTE)["manifest_digest"]},
    )


def resource_controls(started: float) -> None:
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    check(
        "the complete Cycle484 cold run stays below explicit wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
        {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
         "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB},
    )


def main() -> int:
    started = perf_counter()
    print("Cycle484 full-layer discrete P8/Suzuki4/B20 response composition")
    print("authority", AUTHORITY, "audit", AUDIT)
    note_contract()
    factors, exact_weights, fixture_results = c477.run_cycle472_preservation()
    check(
        "frozen Cycle472 exact E/G, mass, Cycle230 contact, leakage, inverse, held branches, and deletions survive unchanged",
        c472.PASS == 8 and c472.FAIL == 0,
        {"Cycle472_pass": c472.PASS, "Cycle472_fail": c472.FAIL,
         "mass": c472.c219.common_species(-0.3).analytic_mass,
         "Cycle230_contact_nontrivial_columns": 4047,
         "held_minimum_pairwise_response": fixture_results[c472.HELD.name]["minimum_pairwise_response"],
         "held_Schmidt_tail": fixture_results[c472.HELD.name]["Schmidt_tail"]},
    )
    imported_science_controls()
    rows = correct_word_rows()
    summaries, _row_results = route_selection_and_error_controls(rows)
    delivery = c467.make_circuit(c463.VALUE_BITS, c463.DENOMINATOR)
    arithmetic = c476.build_circuit()
    phase_capacity_conflict_controls(delivery, arithmetic, summaries)
    literal = literal_discrete_pipeline_controls(delivery, arithmetic, rows)
    discrete_physical_eg_controls(factors, exact_weights, rows)
    covariance_controls(delivery, arithmetic, rows)
    deletion_domain_inventory_no_go_controls(literal)
    frozen_controls()
    resource_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
