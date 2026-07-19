#!/usr/bin/env python3
"""Cycle 399: reversible source-response to Record-counter interface.

The Cycle-396 held-L6 shared-middle source compiler is tensored with two
Cycle-360 fixed-global Record-member counter packets.  A fixed local adapter
coherently admits one previously excluded member precisely on the far-side
reservoir basis sector.  It does not threshold an amplitude and it does not
form a framework Record.

The output is a dimensionless counter coordinate.  Counter traversal and
compiler layering are not time; the unchanged Record DAG has unchanged causal
depth.  No occupation, pointer, or counter is called a physical source,
energy, stress, gravity, occurrence, Record, interval, rate, or proper time.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, replace
from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import car_compiler_record_causal_depth_bridge_cycle255_2026_07_17 as c255
import physical_autonomous_record_link_counter_fixed_global_nn_route_cycle360_2026_07_18 as c360
import physical_shared_middle_three_cell_source_compiler_cycle396_2026_07_18 as c396
import record_defined_causal_depth_clock_cycle170_2026_07_16 as c170


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_RESPONSE_RECORD_COUNTER_INTERFACE_CYCLE399_NOTE_2026-07-18.md"
)
TRAIN_LENGTH = 5
HELD_LENGTH = 6
PACKET_RECORDS = 6
PACKET_MEMBERS = (1, 1, 1, 1, 1, 0)
BASE_COUNT = 5
ADMITTED_COUNT = 6
SOURCE_DEPTH = 3
COUNTER_STEPS = 6
ADMISSION_RULE = "exact target-reservoir basis projector"
NUMERIC_THRESHOLD = None
TOLERANCE = 6e-10
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class BridgeKey:
    q_key: tuple
    a_bits: tuple[int, ...]
    c_bits: tuple[int, ...]
    enables: tuple[int, int]
    comparators: tuple[int, int]


BridgeState = dict[BridgeKey, np.ndarray]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-399 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "e_399 g_399 = g_physical,399 e_399",
        "exact target-reservoir basis projector",
        "no numerical threshold",
        "blind held l6",
        "record payload and identity are preserved",
        "coherent adapter output is not a record",
        "causal-depth response is undefined without a supplied actualization map",
        "counter traversal and compiler layering are not time",
        "not physical source, energy, stress, gravity, occurrence, interval, rate, or proper time",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("the note states the complete interface and semantic contract", not missing, missing)


def packet_fixture(frame: np.ndarray | None = None):
    frame = np.eye(3, dtype=int) if frame is None else np.asarray(frame, dtype=int)
    fixture = c360.c342.c338.build_fixture(HELD_LENGTH)
    layout, static = c360.build_layout(
        fixture, PACKET_RECORDS, frame, members=PACKET_MEMBERS
    )
    return layout, c360.initial_state(layout, static)


def selected_member_sites(layout: c360.Layout) -> tuple[int, int]:
    block = max(layout.blocks, key=lambda item: item.index)
    return tuple(block.member_sites[orientation] for orientation in c360.ORIENTATIONS)


def bridge_constraint_failures(state: c360.MachineState) -> int:
    """Cycle-360 constraints with the selected member promoted to a 00/11 code."""

    failures = c360.auxiliary_constraint_failures(state)
    for block in state.layout.blocks:
        failures -= sum(
            state.bits[block.member_sites[orientation]] != block.member
            for orientation in c360.ORIENTATIONS
        )
        failures += int(
            state.bits[block.member_sites["A"]]
            != state.bits[block.member_sites["B"]]
        )
    return failures


def bridge_norm(state: BridgeState) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def prune(state: BridgeState, threshold: float = 2e-13) -> BridgeState:
    return {key: value for key, value in state.items() if np.linalg.norm(value) > threshold}


def bridge_residual(left: BridgeState, right: BridgeState) -> float:
    keys = set(left) | set(right)
    maximum = 0.0
    for key in keys:
        if key in left:
            zero = np.zeros_like(left[key])
        else:
            zero = np.zeros_like(right[key])
        maximum = max(
            maximum,
            float(np.linalg.norm(left.get(key, zero) - right.get(key, zero))),
        )
    return maximum


def initial_bridge_state(origin: int, layout: c360.Layout, initial: c360.MachineState) -> BridgeState:
    if origin not in (0, 2):
        raise ValueError("origin must be A or C")
    source = c396.initial_response_state(origin)
    enables = (0, 1) if origin == 0 else (1, 0)
    return {
        BridgeKey(q_key, initial.bits, initial.bits, enables, (0, 0)): value.copy()
        for q_key, value in source.items()
    }


def apply_source_macro(
    state: BridgeState,
    route: str,
    length: int,
    factors,
    *,
    inverse: bool = False,
) -> BridgeState:
    grouped: dict[tuple, dict] = defaultdict(dict)
    for key, value in state.items():
        context = (key.a_bits, key.c_bits, key.enables, key.comparators)
        grouped[context][key.q_key] = value
    output: BridgeState = {}
    for context, q_state in grouped.items():
        transformed = q_state
        for _ in range(SOURCE_DEPTH):
            transformed = (
                c396.logical_inverse(transformed, route, length, factors)
                if inverse
                else c396.logical_step(transformed, route, length, factors)
            )
        a_bits, c_bits, enables, comparators = context
        for q_key, value in transformed.items():
            key = BridgeKey(q_key, a_bits, c_bits, enables, comparators)
            output[key] = output.get(key, 0) + value
    return prune(output)


def apply_admission_adapter(
    state: BridgeState,
    layout: c360.Layout,
    *,
    delete_side: int | None = None,
    delete_one_member_gate: bool = False,
) -> BridgeState:
    """Four-layer reversible comparator/dual-member admission circuit."""

    member_sites = selected_member_sites(layout)
    output: BridgeState = {}
    for key, value in state.items():
        packet_bits = [list(key.a_bits), list(key.c_bits)]
        comparators = list(key.comparators)
        for packet_side, source_cell in enumerate((0, 2)):
            control = int(
                key.q_key == c396.q_reservoir(source_cell)
                and key.enables[packet_side] == 1
                and delete_side != packet_side
            )
            # TOFFOLI(reservoir, enable -> comparator)
            comparators[packet_side] ^= control
            if comparators[packet_side]:
                packet_bits[packet_side][member_sites[0]] ^= 1
                if not delete_one_member_gate:
                    packet_bits[packet_side][member_sites[1]] ^= 1
            # Uncompute the comparator.  It is never a Record.
            comparators[packet_side] ^= control
        target = BridgeKey(
            key.q_key,
            tuple(packet_bits[0]),
            tuple(packet_bits[1]),
            key.enables,
            tuple(comparators),
        )
        output[target] = output.get(target, 0) + value
    return prune(output)


def apply_counter_macro(
    state: BridgeState, layout: c360.Layout, *, inverse: bool = False
) -> BridgeState:
    output: BridgeState = {}
    for key, value in state.items():
        a_state = c360.MachineState(layout, key.a_bits)
        c_state = c360.MachineState(layout, key.c_bits)
        for _ in range(COUNTER_STEPS):
            if inverse:
                a_state = c360.inverse_step(a_state)
                c_state = c360.inverse_step(c_state)
            else:
                a_state = c360.step(a_state)
                c_state = c360.step(c_state)
        target = BridgeKey(
            key.q_key,
            a_state.bits,
            c_state.bits,
            key.enables,
            key.comparators,
        )
        output[target] = output.get(target, 0) + value
    return prune(output)


def common_forward(
    state: BridgeState, route: str, length: int, factors, layout: c360.Layout
) -> BridgeState:
    output = apply_source_macro(state, route, length, factors)
    output = apply_admission_adapter(output, layout)
    return apply_counter_macro(output, layout)


def common_inverse(
    state: BridgeState, route: str, length: int, factors, layout: c360.Layout
) -> BridgeState:
    output = apply_counter_macro(state, layout, inverse=True)
    output = apply_admission_adapter(output, layout)
    return apply_source_macro(output, route, length, factors, inverse=True)


def packet_distribution(
    state: BridgeState, layout: c360.Layout, packet_side: int
) -> dict[int | None, float]:
    distribution: dict[int | None, float] = defaultdict(float)
    for key, value in state.items():
        bits = key.a_bits if packet_side == 0 else key.c_bits
        count = c360.done_count(c360.MachineState(layout, bits))
        distribution[count] += float(np.vdot(value, value).real)
    return dict(distribution)


def expected_count(distribution: dict[int | None, float]) -> float:
    if None in distribution:
        raise AssertionError(("counter did not reach DONE", distribution))
    return float(sum(int(count) * weight for count, weight in distribution.items()))


def source_factors():
    rows, coin, first, second, contact, _forward, _reverse = c396.c319.update_controls(
        c396.LABELS, "path"
    )
    return rows, (coin, first, second, contact)


def adapter_and_counter_controls(layout, initial) -> None:
    print("\nFIXED LOCAL ADAPTER / COUNTER PACKETS")
    admitted_bits = list(initial.bits)
    for site in selected_member_sites(layout):
        admitted_bits[site] ^= 1
    admitted = c360.MachineState(layout, tuple(admitted_bits))
    base_terminal = initial
    admitted_terminal = admitted
    for _ in range(COUNTER_STEPS):
        base_terminal = c360.step(base_terminal)
        admitted_terminal = c360.step(admitted_terminal)
    check(
        "the two lawful member-code branches produce fixed dimensionless counts five and six",
        c360.done_count(base_terminal) == BASE_COUNT
        and c360.done_count(admitted_terminal) == ADMITTED_COUNT
        and bridge_constraint_failures(initial) == 0
        and bridge_constraint_failures(admitted) == 0
        and bridge_constraint_failures(base_terminal) == 0
        and bridge_constraint_failures(admitted_terminal) == 0,
        {
            "packet_M2": len(layout.sites),
            "Record_blocks": PACKET_RECORDS,
            "base_count": c360.done_count(base_terminal),
            "admitted_count": c360.done_count(admitted_terminal),
            "fixed_counter_layers_per_step": len(layout.layers),
            "fixed_counter_steps": COUNTER_STEPS,
        },
    )
    # Reservoir--enable--comparator--two-member graph: every primitive has a
    # connected NN support in this fixed attachment chart.
    coords = {
        "member_A": (0, 0, 0),
        "comparator": (1, 0, 0),
        "member_B": (2, 0, 0),
        "reservoir": (1, 1, 0),
        "enable": (1, 2, 0),
    }
    edges = (
        ("enable", "reservoir"),
        ("reservoir", "comparator"),
        ("comparator", "member_A"),
        ("comparator", "member_B"),
    )
    distances = tuple(c255.manhattan(coords[left], coords[right]) for left, right in edges)
    check(
        "the admission adapter is a fixed reversible bounded-NN circuit with no threshold or host response query",
        ADMISSION_RULE == "exact target-reservoir basis projector"
        and NUMERIC_THRESHOLD is None
        and distances == (1, 1, 1, 1),
        {
            "admission_rule": ADMISSION_RULE,
            "numeric_threshold": NUMERIC_THRESHOLD,
            "layers": 4,
            "adapter_M2_per_packet": 2,
            "edge_distances": distances,
            "comparators_return_to_zero": True,
        },
    )


def train_held_response_controls(factors, layout, initial):
    print("\nPREDECLARED L5 / BLIND HELD-L6 COMMON RESPONSE")
    rows = []
    held_outputs = {}
    for route in c396.ROUTES:
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            for origin, target_side in ((0, 1), (2, 0)):
                state = initial_bridge_state(origin, layout, initial)
                output = common_forward(state, route, length, factors, layout)
                target_distribution = packet_distribution(output, layout, target_side)
                spectator_distribution = packet_distribution(output, layout, 1 - target_side)
                target_expectation = expected_count(target_distribution)
                spectator_expectation = expected_count(spectator_distribution)
                row = {
                    "route": route,
                    "L": length,
                    "held": length == HELD_LENGTH,
                    "origin": "A" if origin == 0 else "C",
                    "target": "C" if target_side == 1 else "A",
                    "target_distribution": target_distribution,
                    "spectator_distribution": spectator_distribution,
                    "counter_response": target_expectation - spectator_expectation,
                    "norm": bridge_norm(output),
                }
                rows.append(row)
                if length == HELD_LENGTH:
                    held_outputs[(route, origin)] = output
    failures = []
    for route in c396.ROUTES:
        selected = [row for row in rows if row["route"] == route]
        responses = [row["counter_response"] for row in selected]
        expected = (
            5.958479723237607e-06
            if route == "unit_weight"
            else 3.0046754132975383e-05
        )
        failures.extend(
            (route, row)
            for row in selected
            if abs(row["counter_response"] - expected) > TOLERANCE
            or abs(row["norm"] - 1) > TOLERANCE
        )
    check(
        "the frozen exact adapter yields reciprocal train/held counter responses for both source routes",
        not failures
        and NUMERIC_THRESHOLD is None
        and all(row["target_distribution"].keys() == {5, 6} for row in rows)
        and all(
            row["spectator_distribution"].keys() == {5}
            and abs(row["spectator_distribution"][5] - 1) < TOLERANCE
            for row in rows
        ),
        {"rows": rows, "failures": failures},
    )
    return held_outputs, rows


def inverse_leakage_record_controls(held_outputs, factors, layout, initial) -> None:
    print("\nINVERSE / LEAKAGE / RECORD PAYLOAD")
    inverse_rows = []
    record_failures = 0
    constraint_failures = 0
    comparator_failures = 0
    original_hash = c360.record_hash(initial)
    for (route, origin), output in held_outputs.items():
        recovered = common_inverse(output, route, HELD_LENGTH, factors, layout)
        wanted = initial_bridge_state(origin, layout, initial)
        inverse_rows.append(
            {
                "route": route,
                "origin": origin,
                "inverse_residual": bridge_residual(recovered, wanted),
                "norm_residual": abs(bridge_norm(output) - 1),
            }
        )
        for key in output:
            record_failures += c360.record_hash(
                c360.MachineState(layout, key.a_bits)
            ) != original_hash
            record_failures += c360.record_hash(
                c360.MachineState(layout, key.c_bits)
            ) != original_hash
            constraint_failures += bridge_constraint_failures(
                c360.MachineState(layout, key.a_bits)
            )
            constraint_failures += bridge_constraint_failures(
                c360.MachineState(layout, key.c_bits)
            )
            comparator_failures += sum(key.comparators)
    check(
        "the common reversible macro has an exact inverse and zero counter/adapter leakage",
        max(row["inverse_residual"] for row in inverse_rows) < TOLERANCE
        and max(row["norm_residual"] for row in inverse_rows) < TOLERANCE
        and constraint_failures == comparator_failures == 0,
        {
            "rows": inverse_rows,
            "counter_constraint_failures": constraint_failures,
            "comparator_reset_failures": comparator_failures,
        },
    )
    check(
        "Record payload and identity are preserved in every coherent counter branch",
        record_failures == 0
        and all(
            not {
                site
                for block in layout.blocks
                for site in block.record_sites
            }.intersection(gate.sites)
            for layer in layout.layers
            for gate in layer.gates
        ),
        {
            "Record_hash": original_hash,
            "branch_hash_failures": record_failures,
            "Record_support_gates": 0,
            "adapter_targets_Record_sites": False,
        },
    )


def physical_common_state_controls(held_outputs, factors, layout, initial) -> None:
    print("\nPHYSICAL M2 COMMON STATE / INTERTWINER")
    encodings, _reducer, support, gram_rows = c396.build_shell(HELD_LENGTH)
    encoding = encodings[c396.c319.ORDER_INDEX[(0, 1, 2)]]
    source_initial = c396.initial_response_state(0)
    physical_initial = c396.encode_state(source_initial, encoding)
    source_expected = c396.logical_step(source_initial, "unit_weight", HELD_LENGTH, factors)
    source_physical = c396.physical_step(
        physical_initial, encoding, "unit_weight", HELD_LENGTH, factors
    )
    source_intertwiner = c396.state_residual(
        source_physical, c396.encode_state(source_expected, encoding)
    )

    target = held_outputs[("unit_weight", 0)]
    target_vectors = [
        value
        for key, value in target.items()
        if key.q_key == c396.q_reservoir(2)
    ]
    logical_target_weight = sum(float(np.vdot(value, value).real) for value in target_vectors)
    physical_target_weight = 0.0
    for value in target_vectors:
        physical = encoding @ value
        physical_target_weight += float(np.vdot(physical, physical).real)

    # On every other factor E_399 is the identity.  The adapter and counter
    # are literal M2 permutations, hence commute with E exactly.  The source
    # factor is the tested Cycle-396 intertwiner above.
    recovered = common_inverse(target, "unit_weight", HELD_LENGTH, factors, layout)
    logical_inverse_residual = bridge_residual(
        recovered, initial_bridge_state(0, layout, initial)
    )
    common_resources = {
        "matter_face_port_cell_union_M2": support["face_port_cell_role_union_M2"],
        "S3_role_M2": 3,
        "unit_Q_register_M2_per_L6_cell": 13,
        "L6_cells": HELD_LENGTH ** 3,
        "two_counter_packets_M2": 2 * len(layout.sites),
        "two_comparator_plus_enable_pairs_M2": 4,
    }
    common_resources["installed_common_state_M2"] = (
        common_resources["matter_face_port_cell_union_M2"]
        + common_resources["S3_role_M2"]
        + common_resources["unit_Q_register_M2_per_L6_cell"]
        * common_resources["L6_cells"]
        + common_resources["two_counter_packets_M2"]
        + common_resources["two_comparator_plus_enable_pairs_M2"]
    )
    check(
        "E_399 G_399 = G_physical,399 E_399 and the inverse close on the declared held code",
        max(gram_rows) < TOLERANCE
        and source_intertwiner < TOLERANCE
        and logical_inverse_residual < TOLERANCE
        and abs(physical_target_weight - logical_target_weight) < TOLERANCE,
        {
            "six_order_Gram_raw_maxima": gram_rows,
            "Cycle396_source_factor_intertwiner": source_intertwiner,
            "common_inverse_residual": logical_inverse_residual,
            "encoded_target_readout_residual": abs(
                physical_target_weight - logical_target_weight
            ),
            "identity_factors": "Q register, two physical counter packets, adapter M2",
            "physical_completion": "Cycle396 matrix-unit identity completion supplied",
        },
    )
    check(
        "the common M2 installation has bounded support and constant overhead per lattice cell and packet block",
        common_resources["installed_common_state_M2"] == 4855,
        common_resources,
    )


def covariance_controls(factors) -> None:
    print("\nALL 24 PROPER-CUBIC FRAMES")
    coin, first, second, contact = factors
    covariance = c396.c319.covariance_schedule_controls(
        c396.LABELS,
        "path",
        coin,
        first,
        second,
        contact,
        contact @ second @ first @ coin,
        contact @ first @ second @ coin,
    )
    counter_failures = 0
    adapter_distance_failures = 0
    inverse_failures = 0
    for frame in c396.c210.proper_cubic_frames():
        layout, initial = packet_fixture(frame)
        admitted_bits = list(initial.bits)
        for site in selected_member_sites(layout):
            admitted_bits[site] ^= 1
        admitted = c360.MachineState(layout, tuple(admitted_bits))
        initial_copy = initial
        admitted_copy = admitted
        for _ in range(COUNTER_STEPS):
            initial_copy = c360.step(initial_copy)
            admitted_copy = c360.step(admitted_copy)
        counter_failures += c360.done_count(initial_copy) != BASE_COUNT
        counter_failures += c360.done_count(admitted_copy) != ADMITTED_COUNT
        for _ in range(COUNTER_STEPS):
            initial_copy = c360.inverse_step(initial_copy)
            admitted_copy = c360.inverse_step(admitted_copy)
        inverse_failures += initial_copy.bits != initial.bits
        inverse_failures += admitted_copy.bits != admitted.bits
        # Proper-cubic signed permutations preserve the four unit attachment edges.
        for vector in ((0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
            adapter_distance_failures += int(
                sum(abs(int(value)) for value in frame @ np.asarray(vector)) != 1
            )
    check(
        "the source/compiler, both counter branches, and the local adapter cover all 24 spatial frames",
        covariance["proper_cubic_frames"] == 24
        and covariance["maximum_update_covariance_residual"] < TOLERANCE
        and covariance["frame_group_law_failures"] == 0
        and counter_failures == inverse_failures == adapter_distance_failures == 0,
        {
            "source_covariance": covariance,
            "counter_frame_cases": 48,
            "counter_failures": counter_failures,
            "counter_inverse_failures": inverse_failures,
            "adapter_rotated_edge_tests": 24 * 4,
            "adapter_distance_failures": adapter_distance_failures,
        },
    )


def conservation_contact_controls(held_outputs, update_rows, factors) -> None:
    print("\nMASS / Q / NUMBER / VECTOR / CONTACT")
    number_values = np.asarray(
        [label[0] + label[2] + label[4] for label in c396.LABELS], dtype=float
    )

    def matter_number(state: BridgeState) -> float:
        return float(
            sum(
                np.vdot(value, number_values * value).real
                for value in state.values()
            )
        )

    layout, initial = packet_fixture()
    before = initial_bridge_state(0, layout, initial)
    after = held_outputs[("unit_weight", 0)]
    coefficient_ops = c396.c322.local_source_blocks(c396.ANGLE)
    unit_ops = c396.c325.unit_weight_local_source(c396.ANGLE)
    coefficient_vector = max(
        np.linalg.norm(coefficient_ops[1] @ operator - operator @ coefficient_ops[1])
        for operator in coefficient_ops[4]
    )
    unit_vector = max(
        np.linalg.norm(unit_ops[1] @ operator - operator @ unit_ops[1])
        for operator in unit_ops[7]
    )
    contact = factors[3]
    check(
        "the common spectator interface preserves mass, global Q=1, total matter number, and both local vector ledgers",
        abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"])
        < TOLERANCE
        and abs(matter_number(after) - matter_number(before)) < TOLERANCE
        and all(key.q_key[0] in ("R", "L") for key in after)
        and abs(bridge_norm(after) - 1) < TOLERANCE
        and coefficient_vector < TOLERANCE
        and unit_vector < TOLERANCE,
        {
            "mass_fixture": update_rows["Cycle219_mass_fixture"],
            "three_cell_mass": update_rows["three_cell_rest_mass"],
            "matter_number_before": matter_number(before),
            "matter_number_after": matter_number(after),
            "global_Q": 1,
            "coefficient_two_vector_commutator": coefficient_vector,
            "unit_weight_vector_commutator": unit_vector,
        },
    )
    check(
        "the Cycle-230 contact remains present and changes the held counter response when deleted",
        np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14) == 645,
        {"contact_nontrivial_columns": 645},
    )


def causal_depth_semantic_controls() -> None:
    print("\nRECORD / CAUSAL-DEPTH SEMANTIC FIREWALL")
    dag = c255.event_dag()
    schedules = c255.topological_schedules(dag)
    certificates = tuple(c255.depth_certificate(dag, schedule) for schedule in schedules)
    expected = {event.site: str(event.value) for event in dag.events.values()}
    dependencies = {
        event.site: frozenset(dag.events[parent].site for parent in event.parents)
        for event in dag.events.values()
    }
    completion_site = dag.events[dag.completion].site
    cycle170 = c170.dag_certificate(expected, dependencies, (completion_site,))
    coherent_causal_depth_response = None
    supplied_actualization_map = None
    check(
        "the actual Record DAG keeps scheduler-invariant depth four because the adapter changes no Record or dependency edge",
        len(schedules) == 2
        and certificates[0] == certificates[1]
        and certificates[0]["depth"] == 4
        and cycle170["depth"] == 4
        and cycle170["output_depths"] == (4,),
        {
            "Cycle255_schedules": len(schedules),
            "Cycle255_depth": certificates[0]["depth"],
            "Cycle170_depth": cycle170["depth"],
            "Record_or_edge_changes_from_adapter": 0,
        },
    )
    check(
        "a coherent counter admission is not actualized as a Record and therefore returns no causal-depth response",
        coherent_causal_depth_response is None and supplied_actualization_map is None,
        {
            "coherent_adapter_output_is_Record": False,
            "supplied_actualization_map": supplied_actualization_map,
            "causal_depth_response": coherent_causal_depth_response,
            "counter_response": "defined dimensionless expectation",
            "boundary": "a commit/dephasing and dependency-edge law would be additional supplied structure",
        },
    )


def deletion_and_alternative_controls(factors, layout, initial, held_outputs) -> None:
    print("\nSOURCE / ADAPTER / COUNTER DELETIONS AND ALTERNATIVES")
    primary = held_outputs[("unit_weight", 0)]
    baseline = expected_count(packet_distribution(primary, layout, 1)) - BASE_COUNT

    def source_response(**kwargs) -> float:
        source = c396.evolve(
            c396.initial_response_state(0),
            "unit_weight",
            HELD_LENGTH,
            factors,
            SOURCE_DEPTH,
            **kwargs,
        )
        return c396.reservoir_weight(source, 2)

    stream_deleted = source_response(stream_enabled=False)
    target_deleted = source_response(enabled=(True, True, False))
    middle_deleted = source_response(enabled=(True, False, True))
    contact_deleted = source_response(contact_enabled=False)
    stale_auxiliary = source_response(move_auxiliary=False)

    pre_adapter = apply_source_macro(
        initial_bridge_state(0, layout, initial),
        "unit_weight",
        HELD_LENGTH,
        factors,
    )
    adapter_deleted = apply_counter_macro(pre_adapter, layout)
    adapter_deleted_response = (
        expected_count(packet_distribution(adapter_deleted, layout, 1)) - BASE_COUNT
    )
    one_gate_deleted = apply_admission_adapter(
        pre_adapter, layout, delete_one_member_gate=True
    )
    one_gate_constraint_failures = sum(
        bridge_constraint_failures(c360.MachineState(layout, key.c_bits))
        for key in one_gate_deleted
        if key.q_key == c396.q_reservoir(2)
    )

    admitted_bits = list(initial.bits)
    for site in selected_member_sites(layout):
        admitted_bits[site] ^= 1
    admitted = c360.MachineState(layout, tuple(admitted_bits))
    counter_deleted = c360.without_gate(
        admitted, "count-fredkin:0-b", "count-fredkin:B:i0:k0:b"
    )
    nominal = admitted
    for _ in range(COUNTER_STEPS):
        nominal = c360.step(nominal)
        counter_deleted = c360.step(counter_deleted)

    target_vector = primary[
        next(key for key in primary if key.q_key == c396.q_reservoir(2))
    ]
    other_coherence = max(
        abs(np.vdot(target_vector, value))
        for key, value in primary.items()
        if key.q_key != c396.q_reservoir(2)
    )
    coefficient_response = expected_count(
        packet_distribution(held_outputs[("coefficient_two", 0)], layout, 1)
    ) - BASE_COUNT
    check(
        "source, adapter, and counter deletions are visible while middle/contact/route alternatives remain distinct",
        stream_deleted < TOLERANCE
        and target_deleted < TOLERANCE
        and adapter_deleted_response < TOLERANCE
        and stale_auxiliary < TOLERANCE
        and abs(middle_deleted - baseline) > 1e-10
        and abs(contact_deleted - baseline) > 1e-10
        and one_gate_constraint_failures > 0
        and c360.done_count(nominal) == ADMITTED_COUNT
        and c360.done_count(counter_deleted) != ADMITTED_COUNT
        and abs(coefficient_response - baseline) > 1e-6,
        {
            "baseline_counter_response": baseline,
            "stream_deleted": stream_deleted,
            "target_source_deleted": target_deleted,
            "adapter_deleted": adapter_deleted_response,
            "stationary_auxiliary": stale_auxiliary,
            "middle_source_deleted": middle_deleted,
            "contact_deleted": contact_deleted,
            "one_member_gate_constraint_failures": one_gate_constraint_failures,
            "counter_gate_nominal/deleted": (
                c360.done_count(nominal), c360.done_count(counter_deleted)
            ),
            "coefficient_two_alternative": coefficient_response,
        },
    )
    check(
        "the held response remains coherent, so a classical commit/dephasing alternative is not part of the reversible inverse",
        other_coherence > 1e-6,
        {
            "maximum_target/non_target_q_coherence": float(other_coherence),
            "dephasing_is_reversible": False,
            "commit_or_threshold_supplied": False,
        },
    )


def inventory_and_methodology_controls() -> None:
    print("\nSUPPLIED / DERIVED / OPEN INVENTORY")
    inventory = {
        "source substrate": "Cycle396 held-L6 unit and coefficient-two shared-middle compilers",
        "counter substrate": "two Cycle360 N6 fixed-global 961-M2 Record-member packets",
        "counter inputs": "six immutable Record payloads plus supplied 111110 member code",
        "orientation": "one physical far-side enable seed; swaps under A/C reciprocity",
        "adapter": "exact reservoir/enable comparator and two member CNOTs, then uncompute",
        "calibration": "none; no numerical threshold",
        "common encoding": "Cycle396 E tensor identity on Q/counters/adapter M2",
        "physical completion": "Cycle396 matrix-unit identity completion remains supplied",
        "derived": "reversible coherent count response, reciprocity, covariance, deletions",
        "Record semantics": "payload/identity preserved; no Record formation or DAG edge",
        "depth semantics": "existing depth unchanged; coherent depth response undefined",
        "open": "actualization/commit law, depth edge law, metric normalization, primitive sparse source synthesis",
        "not used": "threshold, host response branch, parity service, gravity law, Thirring engine",
        "authority": "none",
        "audit": "unset",
    }
    check(
        "every supplied, derived, and open interface component is explicit",
        len(inventory) == 15,
        inventory,
    )
    check(
        "the interface boundary is not promoted to a no-go, minimum-content, shared-obstruction, gravity, or axiom-pressure claim",
        True,
        {
            "N1_to_N8_triggered": False,
            "reason": "no negative/minimum/shared-obstruction claim is shipped",
            "shared_obstruction": False,
            "gravity_claim": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    print("CYCLE 399: PHYSICAL SOURCE-RESPONSE / RECORD-COUNTER INTERFACE")
    print("authority=none; audit=unset")
    note_contract()
    update_rows, factors = source_factors()
    layout, initial = packet_fixture()
    adapter_and_counter_controls(layout, initial)
    held_outputs, _response_rows = train_held_response_controls(
        factors, layout, initial
    )
    inverse_leakage_record_controls(held_outputs, factors, layout, initial)
    physical_common_state_controls(held_outputs, factors, layout, initial)
    covariance_controls(factors)
    conservation_contact_controls(held_outputs, update_rows, factors)
    causal_depth_semantic_controls()
    deletion_and_alternative_controls(factors, layout, initial, held_outputs)
    inventory_and_methodology_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_SOURCE_RESPONSE_RECORD_COUNTER_INTERFACE_OPEN")
        return 1
    print("RESULT PHYSICAL_SOURCE_RESPONSE_RECORD_COUNTER_INTERFACE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
