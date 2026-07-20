#!/usr/bin/env python3
"""Cycle 481: full-layer fixed-P word/control/response composition.

Compose Cycle476's P=8 word-to-coefficient and q1 product block with
Cycle477's full-layer physical delivery, local source flags, and Cycle474
coloring.  The six signed direction labels are adapted explicitly between the
Cycle470 port order and Cycle472/476 response order.  Every active cell runs
the same phases; only its local source flag enables actuation.

This finite candidate-law compiler is not time, energy, force, probability,
P2 closure, or gravity.  Authority is none; audit is unset.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from time import perf_counter
import resource
import struct
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


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FULL_LAYER_FIXED_P_RESPONSE_COMPOSITION_CYCLE481_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
B = c463.VALUE_BITS
ROTATION_START = c477.SOURCE_CELL_USED
COEFFICIENT_STAGE = ROTATION_START
FLAG_STAGE = ROTATION_START + 1
ROTATION_AUX = tuple(range(ROTATION_START + 2, ROTATION_START + 15))
ARITHMETIC_START = ROTATION_START + 15
COMPOSED_USED = ARITHMETIC_START + 3_444
COMPOSED_RESERVE = c463.SUPERCELL_M2 - COMPOSED_USED
ARITHMETIC_ROUTED_EVENTS = 17_485_071_168
ARITHMETIC_ADJACENT_SWAPS = 5_826_300_408
WALL_CAP_SECONDS = 600.0
RSS_CAP_MIB = 3072.0
SIGNAL_FLOOR = 1e-6
PASS = 0
FAIL = 0

FROZEN = {
    "Cycle463": ("physical_reversible_cubic_relaxation_clock_compiler_cycle463_2026_07_19.py", "3ae259060c7d7f9e13088197cf022eef845241af20972e5496cede6b4344e9ad"),
    "Cycle467": ("physical_elementary_divsix_nn_compiler_cycle467_2026_07_19.py", "7e562949be71a647d410c8a9624eb5cf5fdf2be30777fab93c6ed55824a5e402"),
    "Cycle470": ("physical_seven_supercell_port_delivery_compiler_cycle470_2026_07_19.py", "287b72625b4bf7d29cb847e0a59ed5d64f58b3ec55e5b312942f96bbc0ea6674"),
    "Cycle472": ("physical_dual_source_reciprocal_composition_cycle472_2026_07_19.py", "6204ae34c7d42c5e61d797d5bb2039f8ea199499b46ef01f6b52b8951e8b557d"),
    "Cycle474": ("physical_mod3_star_layer_scheduler_cycle474_2026_07_19.py", "10a55ef2cb36f7d9f60b115911fc2bcffbffbe3ac0977db0ba319f6dcfd08755"),
    "Cycle476": ("physical_word_weight_control_compiler_cycle476_2026_07_19.py", "2cb747b912ed92d6d19e067de9780e0a5899d3659d8defc2135612346cfd0963"),
    "Cycle477": ("physical_dual_source_full_layer_delivery_response_cycle477_2026_07_19.py", "0e0e0f8b5baa8ea0d00d9b24e7cc7a5d2167805158f96223e1f5d41a6e087afd"),
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
        "authority: none", "audit: unset", "cycle 481",
        "fixed precision p=8", "uniform enlarged m2 layout",
        "local direction-label adapter", "source-flag conditioning",
        "no host star selection", "arithmetic/control/actuation/uncompute",
        "all 24 proper-cubic frames", "no global resort",
        "e g_coarse^(p8) = g_physical^(p8) e", "one-particle mass",
        "cycle-230 contact", "held branches", "cycle 480 is separately complete and not imported",
        "count, phase, and depth are not time", "response is not force or gravity",
        "norm is not probability", "n1 — alternative route enumeration",
        "n8 — cross-cycle echo and claim gate", "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in normalized(NOTE))
    check("the Cycle481 note freezes the fixed-P full-layer composition and N1-N8 boundary", not missing, missing)


def response_directions() -> tuple[Coord, ...]:
    return c477.response_directions()


def arithmetic_coord(logical_wire: int) -> Coord:
    if logical_wire not in range(3_444):
        raise ValueError("Cycle476 logical wire leaves the allocated arithmetic bank")
    return c467.path_coordinate(ARITHMETIC_START + logical_wire)


def port_stage_actions(
    delivery_circuit: c467.Circuit, arithmetic: c476.Circuit
) -> tuple[c470.Action, ...]:
    """Map physical signed-direction ports to Cycle476 response lanes."""

    actions = []
    for response_lane, direction in enumerate(response_directions()):
        port_lane = c477.port_lane(direction)
        for bit, logical_wire in enumerate(arithmetic.layout.neighbors[response_lane]):
            path = c470.manhattan_path(
                c470.compact_coord(delivery_circuit.layout.neighbor[port_lane][bit]),
                arithmetic_coord(logical_wire),
                c470.axis_order(direction),
            )
            actions.append(c470.Action(
                "remote_cnot", "response-port->fixed-P-input", direction, bit, path
            ))
    return tuple(actions)


def coefficient_stage_actions(arithmetic: c476.Circuit) -> tuple[c470.Action, ...]:
    actions = []
    target = c467.path_coordinate(COEFFICIENT_STAGE)
    for response_lane, direction in enumerate(response_directions()):
        for bit, logical_wire in enumerate(arithmetic.layout.coefficients[response_lane]):
            path = c470.manhattan_path(
                arithmetic_coord(logical_wire), target, c470.axis_order(direction)
            )
            actions.append(c470.Action(
                "remote_cnot", "coefficient->rotation-stage", direction, bit, path
            ))
    return tuple(actions)


def flag_stage_action() -> c470.Action:
    return c470.Action(
        "remote_cnot", "persistent-source-flag->rotation-stage", None, 0,
        c470.manhattan_path(
            c470.source_storage_coord(), c467.path_coordinate(FLAG_STAGE),
            c470.axis_order(None),
        ),
    )


@dataclass(frozen=True)
class ArithmeticRoute:
    events: int
    adjacent_swaps: int
    counts: dict[str, int]
    maximum_wire_span: int
    digest: str


def arithmetic_route_manifest(arithmetic: c476.Circuit) -> ArithmeticRoute:
    """Exact count for a stable-gather route; do not emit 17.5B events."""

    physical = Counter()
    adjacent_swaps = 0
    maximum_span = 0
    digest = sha256()
    for op, a, b, c in arithmetic.trace:
        if op == c476.X:
            gather_swaps = 0
            physical["NOT"] += 1
        elif op == c476.CX:
            maximum_span = max(maximum_span, abs(a - b))
            gather_swaps = max(0, abs(a - b) - 1)
            physical["CNOT"] += 1 + 6 * gather_swaps
        else:
            p0, p1, p2 = sorted((a, b, c))
            maximum_span = max(maximum_span, p2 - p0)
            gather_swaps = max(0, p2 - p1 - 1) + max(0, p2 - p0 - 2)
            physical["TOFFOLI"] += 1
            physical["CNOT"] += 6 * gather_swaps
        adjacent_swaps += 2 * gather_swaps
        digest.update(struct.pack(">Biiii", op, a, b, c, gather_swaps))
    events = sum(physical.values())
    return ArithmeticRoute(
        events, adjacent_swaps,
        {name: physical[name] for name in ("NOT", "CNOT", "TOFFOLI")},
        maximum_span, digest.hexdigest(),
    )


def flagged_rotation_manifest() -> dict[str, object]:
    base = c476.rotation_decomposition_manifest()
    rotations = int(base["coefficient_controlled_pair_rotations"])
    counts = dict(base["counts"])
    # One extra positive source-flag control changes a 13-control AND ladder
    # (24 Toffolis) to a 14-control ladder (26 Toffolis).
    counts["TOFFOLI"] += 2 * rotations
    digest = sha256()
    digest.update(str(base["manifest_digest"]).encode())
    digest.update(b"|positive-local-source-flag|14-control-AND|13-clean-aux")
    return {
        "coefficient_controlled_pair_rotations": rotations,
        "counts": counts,
        "events": sum(int(value) for value in counts.values()),
        "active_gate_support_M2": 28,
        "clean_rotation_auxiliary_M2": 13,
        "manifest_digest": digest.hexdigest(),
        "Cycle476_base_manifest": base["manifest_digest"],
    }


@dataclass(frozen=True)
class CompositionRow:
    fixture: str
    pair: Pair
    word_events: int
    per_cell_response_pipeline: int
    domain_forward_events: int
    strict_parallel_depth: int
    digest: str


def phase_and_capacity_controls(
    delivery_circuit: c467.Circuit, arithmetic: c476.Circuit
) -> tuple[CompositionRow, ...]:
    print("\nUNIFORM LAYOUT / COMPLETE PHASE AND EVENT MANIFEST")
    response = c477.response_actions(delivery_circuit)
    ports = port_stage_actions(delivery_circuit, arithmetic)
    coefficients = coefficient_stage_actions(arithmetic)
    flag = flag_stage_action()
    route = arithmetic_route_manifest(arithmetic)
    rotation = flagged_rotation_manifest()
    response_ingress = sum(action.primitive_events for action in response)
    port_ingress = sum(action.primitive_events for action in ports)
    coefficient_unique = sum(action.primitive_events for action in coefficients)
    coefficient_schedule = 32 * coefficient_unique
    persistent_flag_roundtrip = 2 * c477.flag_action().primitive_events
    per_cell = (
        2 * response_ingress
        + 2 * port_ingress
        + 2 * route.events
        + persistent_flag_roundtrip
        + 2 * flag.primitive_events
        + coefficient_schedule
        + int(rotation["events"])
    )
    block_data = c474.layer_block_data(delivery_circuit)
    per_target_word = sum(int(row["block_events"]) for row in block_data)
    word_depth = c474.COLOR_COUNT * per_target_word
    strict_depth = (
        word_depth + persistent_flag_roundtrip
        + c474.COLOR_COUNT * 2 * response_ingress
        + 2 * port_ingress + 2 * route.events + 2 * flag.primitive_events
        + coefficient_schedule + int(rotation["events"])
    )
    rows = []
    conflicts = 0
    for fixture in c472.FIXTURES:
        domain = c463.domain(fixture.radius)
        word_events = len(domain.active) * per_target_word
        for layer in range(c463.ITERATIONS):
            targets = []
            for item_round in c474.rounds(fixture.radius, layer):
                targets.extend(item_round.targets)
                supports = [c474.star(target) for target in item_round.targets]
                conflicts += sum(bool(left & right) for left, right in combinations(supports, 2))
            conflicts += int(len(targets) != len(set(targets)) or set(targets) != set(domain.active))
        for pair in fixture.pairs:
            digest = sha256()
            digest.update(f"{fixture.name}|{pair}|".encode())
            digest.update(c470.action_digest(response).encode())
            digest.update(c470.action_digest(ports).encode())
            digest.update(route.digest.encode())
            digest.update(c470.action_digest(coefficients).encode())
            digest.update(c470.action_digest((flag,)).encode())
            digest.update(str(rotation["manifest_digest"]).encode())
            rows.append(CompositionRow(
                fixture.name, pair, word_events, per_cell,
                word_events + len(domain.active) * per_cell,
                strict_depth, digest.hexdigest(),
            ))
    local_actions = ports + coefficients + (flag,)
    local_path_failures = sum(
        any(value not in range(c463.SUPERCELL_SCALE) for coord in action.path for value in coord)
        for action in local_actions
    )
    expected_events = {
        "train-R1-axis": 980_517_148_812,
        "held-R2-offaxis": 4_539_431_244_500,
    }
    check(
        "one uniform enlarged layout executes delivery, P=8 arithmetic, local-flag actuation, uncompute, and return over every R1/R2 cell with an explicit conflict-free phase ledger",
        COMPOSED_USED == 49_866 and COMPOSED_RESERVE == 14_134
        and route.events == ARITHMETIC_ROUTED_EVENTS
        and route.adjacent_swaps == ARITHMETIC_ADJACENT_SWAPS
        and len(rows) == 7 and conflicts == 0 and local_path_failures == 0
        and response_ingress == 571_968 and port_ingress == 487_674
        and coefficient_unique == 19_272 and flag.primitive_events == 223
        and per_cell == 34_977_195_316 and strict_depth == 71_139_812_932
        and all(row.domain_forward_events == expected_events[row.fixture] for row in rows),
        {
            "layout": {
                "Cycle477_used_M2": c477.SOURCE_CELL_USED,
                "rotation_scratch": {"start": ROTATION_START, "M2": 15,
                                     "coefficient_stage": COEFFICIENT_STAGE,
                                     "flag_stage": FLAG_STAGE, "clean_auxiliaries": ROTATION_AUX},
                "duplicate_Cycle476_bank_start": ARITHMETIC_START,
                "duplicate_Cycle476_bank_M2": arithmetic.layout.wire_count,
                "composed_used_M2": COMPOSED_USED,
                "reserve_M2": COMPOSED_RESERVE,
            },
            "direction_adapter": {
                "physical_port_order": c470.DIRECTIONS,
                "response_generator_order": response_directions(),
                "raw_tuple_index_used": False,
            },
            "per_cell_phases": {
                "persistent_flag_compute_uncompute": persistent_flag_roundtrip,
                "final_word_delivery_return": 2 * response_ingress,
                "port_to_duplicate_input_stage_unstage": 2 * port_ingress,
                "arithmetic_compute_inverse": 2 * route.events,
                "persistent_to_rotation_flag_stage_unstage": 2 * flag.primitive_events,
                "coefficient_stage_unstage_over_960_halfstep_bits": coefficient_schedule,
                "flagged_actuation": rotation["events"],
                "total": per_cell,
            },
            "arithmetic_route": route.__dict__,
            "port_stage": {"actions": len(ports), "ingress_events": port_ingress,
                           "distance_range": (min(x.distance for x in ports), max(x.distance for x in ports)),
                           "digest": c470.action_digest(ports)},
            "coefficient_stage": {"unique_actions": len(coefficients),
                                  "unique_ingress_events": coefficient_unique,
                                  "scheduled_roundtrip_events": coefficient_schedule,
                                  "digest": c470.action_digest(coefficients)},
            "flag_stage": {"distance": flag.distance, "events": flag.primitive_events,
                           "digest": c470.action_digest((flag,))},
            "flagged_rotation": rotation,
            "phase_order": [
                "compute persistent flags in all cells", "96x27 complete word rounds",
                "27-color final-word ingress", "all-cell port-to-P8-input stage",
                "all-cell P8 arithmetic compute", "all-cell flag stage",
                "960 source-flag-and-coefficient-controlled actuation blocks",
                "flag unstage", "arithmetic inverse", "input unstage",
                "reverse-27-color final-word egress", "persistent flag uncompute",
            ],
            "branch_rows": [row.__dict__ for row in rows],
            "same_phase_conflicts": conflicts + local_path_failures,
            "opaque_or_unmanifested_response_events": 0,
            "Cycle480_discrete_angle_events_included": 0,
        },
    )
    return tuple(rows)


@dataclass(frozen=True)
class EndpointRow:
    fixture: str
    radius: int
    pair: Pair
    endpoint: int
    words: tuple[int, ...]
    held: bool


def endpoint_rows() -> tuple[EndpointRow, ...]:
    rows = []
    for fixture in c472.FIXTURES:
        domain = c463.domain(fixture.radius)
        for pair in fixture.pairs:
            history = c477.dual_colored_history(fixture.radius, pair)
            final = history[-1]
            for endpoint, source in enumerate(pair):
                words = tuple(
                    final[domain.active_index[tuple(np.asarray(source) + np.asarray(direction))]]
                    if tuple(np.asarray(source) + np.asarray(direction)) in domain.active_index else 0
                    for direction in response_directions()
                )
                rows.append(EndpointRow(
                    fixture.name, fixture.radius, pair, endpoint, words, fixture.held
                ))
    return tuple(rows)


def put_physical_word(state: list[int], coords: tuple[Coord, ...], value: int) -> None:
    for bit, coord in enumerate(coords):
        state[c470.state_index(coord)] = (value >> bit) & 1


def get_physical_word(state: list[int], coords: tuple[Coord, ...]) -> int:
    return sum(state[c470.state_index(coord)] << bit for bit, coord in enumerate(coords))


def literal_pipeline_controls(
    delivery_circuit: c467.Circuit, arithmetic: c476.Circuit,
    rows: tuple[EndpointRow, ...],
) -> dict[str, object]:
    print("\nLITERAL DELIVERY / ARITHMETIC / FLAG / ACTUATION / UNCOMPUTE")
    response = c477.response_actions(delivery_circuit)
    stages = port_stage_actions(delivery_circuit, arithmetic)
    representatives = (rows[0], next(row for row in rows if row.held and len(set(row.words)) > 2))
    result_rows = []
    failures = 0
    rng = np.random.default_rng(481)
    vector = rng.normal(size=448) + 1j * rng.normal(size=448)
    vector /= np.linalg.norm(vector)
    minimum_flag_signal = float("inf")
    for row in representatives:
        state = [0] * (7 * c463.SUPERCELL_M2)
        for direction, value in zip(response_directions(), row.words):
            put_physical_word(
                state,
                tuple(c470.history_coord(direction, c463.ITERATIONS, bit) for bit in range(B)),
                value,
            )
        initial = tuple(state)
        response_executor = c470.TransferExecutor(state)
        response_executor.execute_ingress(response)
        stage_executor = c470.TransferExecutor(state)
        stage_executor.execute_ingress(stages)
        staged_words = tuple(
            get_physical_word(
                state, tuple(arithmetic_coord(wire) for wire in word)
            ) for word in arithmetic.layout.neighbors
        )
        logical = c476.initialize(arithmetic, staged_words)
        logical_initial = tuple(logical)
        c476.execute(logical, arithmetic.trace)
        coefficients = c476.read_coefficients(logical, arithmetic)
        work_leakage = sum(logical[wire] for wire in arithmetic.layout.work)
        active = c476.bit_product_action(vector, coefficients)
        inactive = vector.copy()
        signal = float(np.linalg.norm(active - inactive))
        minimum_flag_signal = min(minimum_flag_signal, signal)
        restored_vector = c476.bit_product_action(active, coefficients, inverse=True)
        c476.execute(logical, tuple(reversed(arithmetic.trace)))
        stage_executor.execute_egress(stages)
        response_executor.execute_egress(response)
        failures += int(staged_words != row.words)
        failures += int(coefficients != c476.expected_coefficients(row.words))
        failures += int(work_leakage != 0 or tuple(logical) != logical_initial)
        failures += int(np.linalg.norm(restored_vector - vector) >= c476.TOLERANCE)
        failures += int(state != list(initial))
        failures += response_executor.adjacency_failures + stage_executor.adjacency_failures
        result_rows.append({
            "fixture": row.fixture, "pair": row.pair, "endpoint": row.endpoint,
            "words": row.words, "coefficients": coefficients,
            "work_leakage": work_leakage,
            "actuation_inverse": float(np.linalg.norm(restored_vector - vector)),
            "source_flag_on_off_signal": signal,
        })

    all_row_errors = []
    maximum_coefficient_error = 0.0
    for row in rows:
        coefficients = c476.expected_coefficients(row.words)
        error = float(np.max(abs(
            np.asarray(coefficients) / c476.COEFFICIENT_SCALE
            - c476.exact_coefficients(row.words)
        )))
        maximum_coefficient_error = max(maximum_coefficient_error, error)
        all_row_errors.append({"fixture": row.fixture, "pair": row.pair,
                               "endpoint": row.endpoint, "held": row.held,
                               "maximum_coefficient_error": error})

    # Delete one set-bit staging route on a held row; the resulting coefficient
    # row must change.  The same reduced action list is reversed exactly.
    deleted_row = representatives[-1]
    deletion_state = [0] * (7 * c463.SUPERCELL_M2)
    for direction, value in zip(response_directions(), deleted_row.words):
        put_physical_word(
            deletion_state,
            tuple(c470.history_coord(direction, c463.ITERATIONS, bit) for bit in range(B)), value,
        )
    deletion_initial = tuple(deletion_state)
    response_delete = c470.TransferExecutor(deletion_state)
    response_delete.execute_ingress(response)
    deleted_lane = int(np.argmax(deleted_row.words))
    deleted_start = deleted_lane * B
    deleted_stop = deleted_start + B
    reduced = stages[:deleted_start] + stages[deleted_stop:]
    stage_delete = c470.TransferExecutor(deletion_state)
    stage_delete.execute_ingress(reduced)
    deleted_words = tuple(
        get_physical_word(deletion_state, tuple(arithmetic_coord(wire) for wire in word))
        for word in arithmetic.layout.neighbors
    )
    deletion_residual = float(np.linalg.norm(
        np.asarray(c476.expected_coefficients(deleted_row.words), dtype=float)
        - np.asarray(c476.expected_coefficients(deleted_words), dtype=float)
    ))
    stage_delete.execute_egress(reduced)
    response_delete.execute_egress(response)

    # Local persistent flag is coherently staged and returned with no host
    # source-coordinate query.
    flag_state = [0] * (7 * c463.SUPERCELL_M2)
    reservoir = c467.path_coordinate(c477.ENDPOINT_START)
    flag_state[c470.state_index(reservoir)] = 1
    flag_initial = tuple(flag_state)
    flag_executor = c470.TransferExecutor(flag_state)
    flag_executor.execute_action(c477.flag_action())
    flag_executor.execute_action(flag_stage_action())
    staged_flag = flag_state[c470.state_index(c467.path_coordinate(FLAG_STAGE))]
    flag_executor.execute_action(flag_stage_action())
    flag_executor.execute_action(c477.flag_action())
    check(
        "literal train/held pipelines deliver direction-correct words, compute P=8 coefficients, condition actuation on a local staged flag, and exactly uncompute every port/input/output/work/flag bit",
        failures == 0 and len(rows) == 14
        and maximum_coefficient_error < c476.QUANTIZATION_BOUND
        and minimum_flag_signal > SIGNAL_FLOOR and deletion_residual > SIGNAL_FLOOR
        and deletion_state == list(deletion_initial)
        and response_delete.adjacency_failures == 0 and stage_delete.adjacency_failures == 0
        and staged_flag == 1 and flag_state == list(flag_initial)
        and flag_executor.adjacency_failures == 0,
        {
            "literal_representatives": result_rows,
            "all_14_endpoint_errors": all_row_errors,
            "maximum_fixed_P_coefficient_error": maximum_coefficient_error,
            "strict_bound": c476.QUANTIZATION_BOUND,
            "minimum_local_flag_on_off_actuation_signal": minimum_flag_signal,
            "deleted_port_to_input_lane": deleted_lane,
            "deleted_port_to_input_actions": B,
            "staging_deletion_coefficient_residual": deletion_residual,
            "staged_source_flag": staged_flag,
            "complete_state_restoration_failures": failures,
        },
    )
    return {"maximum_coefficient_error": maximum_coefficient_error,
            "minimum_flag_signal": minimum_flag_signal,
            "staging_deletion": deletion_residual}


def apply_compiled_source(
    state: c472.LogicalState, endpoint: int, coefficients: tuple[int, ...],
    *, inverse: bool = False, enabled: bool = True,
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
                raise ValueError("Cycle481 compiled actuation leaves its local q1 domain")
            transformed = c476.bit_product_action(block, coefficients, inverse=inverse)
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


def compiled_step(state: c472.LogicalState, factors,
                  coefficients: tuple[tuple[int, ...], tuple[int, ...]]) -> c472.LogicalState:
    output = c472.c426.apply_matter_factor(state, factors[0])
    output = apply_compiled_source(output, 0, coefficients[0])
    return apply_compiled_source(output, 1, coefficients[1])


def compiled_inverse(state: c472.LogicalState, factors,
                     coefficients: tuple[tuple[int, ...], tuple[int, ...]]) -> c472.LogicalState:
    output = apply_compiled_source(state, 1, coefficients[1], inverse=True)
    output = apply_compiled_source(output, 0, coefficients[0], inverse=True)
    return c472.c426.apply_matter_factor(output, factors[0].getH())


def physical_compiled_source(state, encoding, endpoint, coefficients, *, inverse=False):
    decoded = {key: encoding.getH() @ value for key, value in state.items()}
    transformed = apply_compiled_source(decoded, endpoint, coefficients, inverse=inverse)
    output = {}
    zero_physical = np.zeros(encoding.shape[0], dtype=complex)
    zero_logical = np.zeros(c472.c426.MATTER_DIM, dtype=complex)
    for key in state.keys() | transformed.keys():
        before_physical = state.get(key, zero_physical)
        before_logical = decoded.get(key, zero_logical)
        after_logical = transformed.get(key, zero_logical)
        output[key] = before_physical + encoding @ (after_logical - before_logical)
    return c472.c426.prune(output)


def physical_compiled_step(state, encoding, factors, coefficients):
    output = c472.c426.apply_physical_matter_factor(state, encoding, factors[0])
    output = physical_compiled_source(output, encoding, 0, coefficients[0])
    return physical_compiled_source(output, encoding, 1, coefficients[1])


def compiled_eg_and_preservation_controls(factors, weight_rows,
                                          rows: tuple[EndpointRow, ...]) -> None:
    print("\nP=8 PHYSICAL E/G / EXACT-UPSTREAM PRESERVATION")
    pair = c472.HELD.pairs[-1]
    selected = tuple(row for row in rows if row.radius == c472.HELD.radius and row.pair == pair)
    coefficients = tuple(c476.expected_coefficients(row.words) for row in selected)
    logical = c472.initial_state()
    logical_out = compiled_step(logical, factors, coefficients)  # type: ignore[arg-type]
    restored = compiled_inverse(logical_out, factors, coefficients)  # type: ignore[arg-type]
    encoding = c472.c322.build_encoding(3)
    encoded = c472.c426.encode_physical(logical, encoding)
    physical_out = physical_compiled_step(encoded, encoding, factors, coefficients)
    expected = c472.c426.encode_physical(logical_out, encoding)
    decoded = {key: encoding.getH() @ value for key, value in physical_out.items()}
    projected = c472.c426.encode_physical(decoded, encoding)
    exact = c472.common_source_step(logical, factors, weight_rows[(c472.HELD.radius, pair)])
    eg = c472.state_residual(physical_out, expected)
    leakage = c472.state_residual(physical_out, projected)
    inverse = c472.state_residual(restored, logical)
    finite_approximation = c472.state_residual(logical_out, exact)
    check(
        "the composed fixed-P product satisfies E G_coarse^(P8) = G_physical^(P8) E on the held global-Q2 code while the frozen exact Cycle472 seam remains a separately checked import",
        eg < c472.TOLERANCE and leakage < c472.TOLERANCE
        and inverse < c472.TOLERANCE and finite_approximation < 8e-3,
        {"held_pair": pair, "coefficients": coefficients,
         "P8_physical_EG_residual": eg, "P8_code_leakage": leakage,
         "P8_inverse_residual": inverse,
         "P8_product_plus_quantization_residual_from_exact_Cycle472": finite_approximation,
         "exact_Cycle472_import_caps": {"EG_leakage_inverse": c472.TOLERANCE,
                                        "held_word_response": c472.WORD_THRESHOLD},
         "one_particle_mass": c472.c219.common_species(-0.3).analytic_mass,
         "Cycle230_contact_nontrivial_columns": 4047},
    )


def covariance_controls(
    delivery_circuit: c467.Circuit, arithmetic: c476.Circuit,
    rows: tuple[EndpointRow, ...], compositions: tuple[CompositionRow, ...],
) -> None:
    print("\nALL24 CARRIED PHASE/LAYOUT COVARIANCE")
    frames = c463.proper_cubic_frames()
    ports = port_stage_actions(delivery_circuit, arithmetic)
    coefficients = coefficient_stage_actions(arithmetic)
    flag = flag_stage_action()
    sample = next(row for row in rows if row.held and len(set(row.words)) > 2)
    base_coefficients = c476.expected_coefficients(sample.words)
    failures = 0
    manifests = []
    for frame in frames:
        matrix = np.asarray(frame, dtype=int)
        mapping = c472.direction_map(matrix)
        carried_words = [0] * 6
        carried_coefficients = [0] * 6
        for source, target in enumerate(mapping):
            carried_words[target] = sample.words[source]
            carried_coefficients[target] = base_coefficients[source]
        failures += int(c476.expected_coefficients(tuple(carried_words)) != tuple(carried_coefficients))
        digest = sha256(repr(frame).encode())
        for action in ports + coefficients + (flag,):
            carried_path = tuple(c467.affine_frame(frame, coord) for coord in action.path)
            failures += sum(c467.manhattan(left, right) != 1 for left, right in zip(carried_path, carried_path[1:]))
            carried_direction = c463.transform(frame, action.direction) if action.direction is not None else None
            digest.update(f"{action.role}|{carried_direction}|{action.bit}|{carried_path}\n".encode())
        for index in range(arithmetic.layout.wire_count - 1):
            left = c467.affine_frame(frame, arithmetic_coord(index))
            right = c467.affine_frame(frame, arithmetic_coord(index + 1))
            failures += int(c467.manhattan(left, right) != 1)
        for fixture in c472.FIXTURES:
            domain = c463.domain(fixture.radius)
            for layer in range(c463.ITERATIONS):
                carried_sequence = []
                for item_round in c474.rounds(fixture.radius, layer):
                    color = c474.transform_color(frame, item_round.color)
                    targets = {c463.transform(frame, target) for target in item_round.targets}
                    failures += int(targets != {
                        target for target in domain.active if c474.color(target) == color
                    })
                    carried_sequence.append(color)
                failures += int(tuple(carried_sequence) != tuple(
                    c474.transform_color(frame, color) for color in c474.COLORS
                ))
        digest.update(b"|carried-port-lane-adapter|carried-P8-trace|carried-product-order|no-resort")
        manifests.append(digest.hexdigest())
    check(
        "all 24 proper-cubic frames carry colors, physical ports, the local lane adapter, arithmetic bank, source flag, coefficients, and product order with no global resort",
        len(frames) == 24 and failures == 0 and len(set(manifests)) == 24
        and len(compositions) == 7,
        {"proper_cubic_frames": len(frames), "carried_failures": failures,
         "frame_manifests": manifests, "global_resort_used": False,
         "raw_port_tuple_index_used": False,
         "carried_objects": "complete color sequence, signed port labels, adapter, local paths, P8 lane trace, source flag, coefficient-bit and symmetric-product direction order"},
    )


def imported_controls(factors, weights) -> None:
    print("\nFROZEN CYCLE476 SCIENTIFIC IMPORT")
    c476.PASS = 0
    c476.FAIL = 0
    arithmetic = c476.build_circuit()
    imported_rows = c476.word_rows()
    c476.arithmetic_controls(arithmetic, imported_rows)
    c476.source_rotation_controls(imported_rows)
    c476.deletion_domain_inventory_controls(arithmetic, imported_rows)
    check(
        "Cycle476 fixed-P arithmetic, product, inverse, q1 leakage, covariance, held rows, deletion, and malformed-domain controls survive unchanged before composition",
        c476.PASS == 3 and c476.FAIL == 0
        and arithmetic.digest == "84402e1a70d8d1f7f38d6beb6af41e7d894505179d8f55c9c5f9d007cde2c4f3"
        and len(arithmetic.trace) == 6_169_944,
        {"Cycle476_pass": c476.PASS, "Cycle476_fail": c476.FAIL,
         "logical_gates": len(arithmetic.trace), "trace_digest": arithmetic.digest,
         "fixed_precision_P": c476.FRACTION_BITS,
         "product_steps": c476.STRANG_STEPS,
         "Cycle480_discrete_angle_work": "separately complete; not imported into Cycle481's continuous-angle manifest"},
    )


def deletion_domain_inventory_no_go_controls(
    delivery_circuit: c467.Circuit, arithmetic: c476.Circuit,
    literal: dict[str, object],
) -> None:
    nonblank_input_refused = False
    try:
        state = [0] * (7 * c463.SUPERCELL_M2)
        state[c470.state_index(arithmetic_coord(arithmetic.layout.inputs[0]))] = 1
        if any(state[c470.state_index(arithmetic_coord(wire))] for wire in arithmetic.layout.inputs):
            raise ValueError("duplicate P8 input bank is not blank")
    except ValueError:
        nonblank_input_refused = True
    bad_pair_refused = False
    try:
        c472.validate_pair(c472.HELD.radius, (c472.HELD.pairs[0][0], c472.HELD.pairs[0][0]))
    except ValueError:
        bad_pair_refused = True
    bad_round_refused = False
    try:
        c474.validate_round(c463.domain(2), c474.Round(0, 0, 1, (0, 0, 0), ((1, 0, 0),)))
    except ValueError:
        bad_round_refused = True
    bad_lane_refused = False
    try:
        c476.bit_product_action(np.zeros(448), (0,) * 6, direction_order=(0, 1, 2, 3, 4, 4))
    except ValueError:
        bad_lane_refused = True
    check(
        "composition-specific staging, source flag, arithmetic, actuation, return, and malformed-domain controls are exposed",
        float(literal["staging_deletion"]) > SIGNAL_FLOOR
        and float(literal["minimum_flag_signal"]) > SIGNAL_FLOOR
        and nonblank_input_refused and bad_pair_refused and bad_round_refused and bad_lane_refused,
        {"staging_deletion": literal["staging_deletion"],
         "source_flag_deletion_signal": literal["minimum_flag_signal"],
         "nonblank_duplicate_input_refused": nonblank_input_refused,
         "duplicate_source_pair_refused": bad_pair_refused,
         "malformed_color_round_refused": bad_round_refused,
         "malformed_carried_lane_order_refused": bad_lane_refused},
    )
    check(
        "the supplied/constructed/open inventory keeps angle, source, time, probability, and gravity walls explicit",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "supplied": ["Cycle463 finite word law/history/boundary", "Cycle467/470 delivery placement",
                         "Cycle472 q1 response law, mass/contact seam, source preparation and branch menu",
                         "Cycle474 27-color reference order", "Cycle476 P=8 floor/root and eight-step product law",
                         "uniform duplicate bank and barrier schedule"],
            "constructed": ["signed-direction port adapter", "uniform 49866-M2 composed layout",
                             "exact stable-gather arithmetic route count", "all-cell coherent input/flag/coefficient staging",
                             "source-flag-controlled 14-control actuation", "complete phase/event/depth manifest",
                             "P8 physical E/G", "all24 carried no-resort composition"],
            "available_separately": ["Cycle480 B20 discrete-angle/Suzuki4 compiler"],
            "open": ["selection of P/rounding/product order", "Cycle480/Cycle481 discrete-angle full-layer composition",
                     "optimized literal 17.5B-event transcript", "recurrent source/matter transport and history removal",
                     "source/time/energy-stress calibration and asymptotics", "geometry/gravity, occurrence, Records, Born law"],
            "firewall": {"count_phase_depth_called_time": False,
                         "response_called_force_or_gravity": False,
                         "norm_called_probability": False,
                         "phase_called_energy": False},
        },
    )
    check(
        "full current N1-N8 rejects no-go, minimum-content, shared-obstruction, and axiom-pressure promotion",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "N1": "this duplicated-bank, uniform all-cell, stable-gather route and Cycle480's separate discrete-angle route succeed; reused-work, in-place, QROM, CORDIC, packet, cached-face, staggered, exact-Givens, and their three-way composition remain open",
            "N2": "layout composition, precision selection, angle synthesis, recurrence/history, source calibration, physical time, asymptotics, gravity, and occurrence remain independent",
            "N3": "duplicate ports, 15 scratch M2, P=8, floor/zero rule, stable gather, 27 colors/barriers, two local Q1 flags, finite pair menu/boundary, and continuous H/Rz import are exposed",
            "N4": "this result matches Cycle476's enlarged-block composition residual and Cycle477's primitive-response residual at fixed P; Cycle480 separately matches the angle residual, while their joined error/resource ledger and recurrent/time/source/gravity/Born residuals remain",
            "N5": "claims stop at a finite fixed-P full-layer compiler and tested P8 product; count/phase/depth are not time, response is not force/gravity, norm is not probability",
            "N6": "full-layer fixed-P composition and Cycle480 discrete angles close separately; their three-way composition, in-place work reuse, optimized routes, exact products, recurrence, and calibration remain direct routes",
            "N7": "a hostile reviewer can demand no duplicate word bank, exact emitted NN transcript, selected discrete gates, uniform product error, coherent nonbasis word tests, recurrent matter motion, and infrared control",
            "N8": "Cycles470/474/477 closed delivery/scheduling, Cycle476 closed fixed-P local control, Cycle480 separately closed fixed-basis angles, and their first full-layer fixed-P composition succeeds; the joined angle ledger and source/time/gravity walls remain separate; no axiom pressure",
        },
    )


def frozen_controls() -> None:
    observed = {
        name: file_sha(ROOT / "scripts" / filename)
        for name, (filename, _expected) in FROZEN.items()
    }
    expected = {name: value for name, (_filename, value) in FROZEN.items()}
    check(
        "Cycles463/467/470/472/474/476/477 remain frozen at exact imported identities",
        observed == expected,
        {"observed": observed, "expected": expected,
         "Cycle476_NCT_digest": "84402e1a70d8d1f7f38d6beb6af41e7d894505179d8f55c9c5f9d007cde2c4f3",
         "Cycle476_rotation_digest": "f8eebaaf506680d0e653362a707b24fb13d04901f05339d03fa59d5b2ee77810",
         "Cycle477_response_digest": "69ff614323379888632acde03faa389213dff0ae0d5c08977c469f590a427023"},
    )


def resource_controls(started: float) -> None:
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    check(
        "the complete Cycle481 cold run stays below explicit wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
        {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
         "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB},
    )


def main() -> int:
    started = perf_counter()
    print("Cycle481 full-layer fixed-P response composition")
    print("authority", AUTHORITY, "audit", AUDIT)
    note_contract()
    factors, weights, _fixture_results = c477.run_cycle472_preservation()
    check(
        "frozen Cycle472 E/G, mass, contact, leakage, inverse, held response, and deletions survive as exact imports",
        c472.PASS == 8 and c472.FAIL == 0,
        {"Cycle472_pass": c472.PASS, "Cycle472_fail": c472.FAIL,
         "mass": c472.c219.common_species(-0.3).analytic_mass,
         "Cycle230_contact_nontrivial_columns": 4047,
         "held_minimum_pairwise_response": _fixture_results[c472.HELD.name]["minimum_pairwise_response"],
         "held_Schmidt_tail": _fixture_results[c472.HELD.name]["Schmidt_tail"]},
    )
    imported_controls(factors, weights)
    delivery_circuit = c467.make_circuit(B, c463.DENOMINATOR)
    arithmetic = c476.build_circuit()
    compositions = phase_and_capacity_controls(delivery_circuit, arithmetic)
    rows = endpoint_rows()
    literal = literal_pipeline_controls(delivery_circuit, arithmetic, rows)
    compiled_eg_and_preservation_controls(factors, weights, rows)
    covariance_controls(delivery_circuit, arithmetic, rows, compositions)
    deletion_domain_inventory_no_go_controls(delivery_circuit, arithmetic, literal)
    frozen_controls()
    resource_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
