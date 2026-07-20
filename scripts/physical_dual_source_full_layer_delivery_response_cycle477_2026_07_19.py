#!/usr/bin/env python3
"""Cycle 477: dual-source full-layer delivery/response-interface compiler.

Compose Cycle 470 word transport with Cycle 472's two active source vertices.
Cycle 474 colors both the complete dual-source relaxation and an unconditional
final-word delivery interface at every active cell.  Only two local Q1 flags
activate the supplied Cycle-472 word-to-weight/weighted-response semantics.
Cycle 476's fixed-P q1 arithmetic/control compiler is available separately but
is not composed into this event manifest.
Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
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


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DUAL_SOURCE_FULL_LAYER_DELIVERY_RESPONSE_CYCLE477_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
B = c463.VALUE_BITS
ZERO = (0, 0, 0)
ENDPOINT_M2 = 36
ENDPOINT_START = c470.USED_PER_ACTIVE_SUPERCELL
SOURCE_CELL_USED = ENDPOINT_START + ENDPOINT_M2
SOURCE_CELL_RESERVE = c463.SUPERCELL_M2 - SOURCE_CELL_USED
FROZEN_C467_SHA = "7e562949be71a647d410c8a9624eb5cf5fdf2be30777fab93c6ed55824a5e402"
FROZEN_C470_SHA = "287b72625b4bf7d29cb847e0a59ed5d64f58b3ec55e5b312942f96bbc0ea6674"
FROZEN_C472_SHA = "6204ae34c7d42c5e61d797d5bb2039f8ea199499b46ef01f6b52b8951e8b557d"
FROZEN_C474_SHA = "10a55ef2cb36f7d9f60b115911fc2bcffbffbe3ac0977db0ba319f6dcfd08755"
FROZEN_C476_SHA = "2cb747b912ed92d6d19e067de9780e0a5899d3659d8defc2135612346cfd0963"
FROZEN_C467_ROUTE = "4d6f058d95cc32538f3a15b6fd0eb620f7708371e6276298d063ba44078d1457"
FROZEN_C470_LITERAL = "4b3c532fe2507e72c529e32a396d7288e28042a493492f55eff9dc6f906a7502"
WALL_CAP_SECONDS = 300.0
RSS_CAP_MIB = 2048.0
PASS = 0
FAIL = 0

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
    value = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        value = value.replace(marker, "")
    return " ".join(value.split())


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset", "cycle 477",
        "full-layer delivery interface", "two active source vertices",
        "primitive word-to-weight synthesis is not claimed",
        "all 24 proper-cubic frames", "held response", "source endpoint support",
        "mass and cycle-230 contact", "e g_coarse = g_physical e",
        "event manifest is not full primitive response execution",
        "iteration count, color round, and schedule depth are not time",
        "not probability", "not energy, force, lapse, metric, backreaction, or gravity",
        "n1 — alternative route enumeration", "n8 — cross-cycle echo and claim gate",
        "no axiom pressure",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle477 note freezes the full-layer delivery/response boundary and N1-N8 gate", not missing, missing)


def response_directions() -> tuple[Coord, ...]:
    return tuple(tuple(int(value) for value in direction) for direction in c472.DIRECTIONS)


def port_lane(direction: Coord) -> int:
    return c470.DIRECTIONS.index(direction)


def response_actions(circuit: c467.Circuit) -> tuple[c470.Action, ...]:
    output = []
    for direction in response_directions():
        lane = port_lane(direction)
        for bit in range(B):
            path = c470.manhattan_path(
                c470.history_coord(direction, c463.ITERATIONS, bit),
                c470.compact_coord(circuit.layout.neighbor[lane][bit]),
                c470.axis_order(direction),
            )
            output.append(c470.Action(
                "remote_cnot", "final-neighbor-word->response-port", direction, bit, path
            ))
    return tuple(output)


def flag_action() -> c470.Action:
    reservoir = c467.path_coordinate(ENDPOINT_START)
    flag = c470.source_storage_coord()
    return c470.Action(
        "remote_cnot", "local-reservoir->persistent-source-flag", None, 0,
        c470.manhattan_path(reservoir, flag, c470.axis_order(None)),
    )


def dual_colored_history(radius: int, pair: Pair, *, reverse: bool = False,
                         history: tuple[tuple[int, ...], ...] | None = None,
                         delete_source: int | None = None) -> tuple[tuple[int, ...], ...]:
    c472.validate_pair(radius, pair)
    item = c463.domain(radius)
    source = c472.source_bits(radius, pair, delete_source)
    output = (
        [list(layer) for layer in history]
        if history is not None else [[0 for _ in item.active] for _ in range(c463.ITERATIONS + 1)]
    )
    layer_order = reversed(range(c463.ITERATIONS)) if reverse else range(c463.ITERATIONS)
    for layer in layer_order:
        layer_rounds = tuple(reversed(c474.rounds(radius, layer))) if reverse else c474.rounds(radius, layer)
        for item_round in layer_rounds:
            c474.validate_round(item, item_round)
            targets = reversed(item_round.targets) if reverse else item_round.targets
            for target in targets:
                previous = output[item_round.read_layer]
                neighbors = tuple(
                    previous[item.active_index[coord]] if coord in item.active_index else 0
                    for coord in c463.six_neighbors(target)
                )
                value = c463.local_quotient(neighbors, source[item.active_index[target]])
                index = item.active_index[target]
                if reverse:
                    if output[item_round.write_layer][index] != value:
                        raise ValueError("inverse history leaves the dual-source code")
                    output[item_round.write_layer][index] = 0
                else:
                    if output[item_round.write_layer][index] != 0:
                        raise ValueError("dual-source target is not blank")
                    output[item_round.write_layer][index] = value
    return tuple(tuple(layer) for layer in output)


@dataclass(frozen=True)
class ManifestRow:
    fixture: str
    pair: Pair
    word_events: int
    response_delivery_events: int
    flag_route_events: int
    compiled_forward_events: int
    compiled_parallel_depth: int
    source_colors: tuple[c474.Color, c474.Color]
    source_response_rounds: int
    digest: str


def full_layer_manifest_controls(circuit: c467.Circuit) -> tuple[ManifestRow, ...]:
    block_data = c474.layer_block_data(circuit)
    response = response_actions(circuit)
    response_ingress_events = sum(action.primitive_events for action in response)
    response_roundtrip = 2 * response_ingress_events
    flag = flag_action()
    rows = []
    failures = 0
    for fixture in c472.FIXTURES:
        item = c463.domain(fixture.radius)
        word_events = len(item.active) * sum(int(row["block_events"]) for row in block_data)
        word_depth = c474.COLOR_COUNT * sum(int(row["block_events"]) for row in block_data)
        response_events = len(item.active) * response_roundtrip
        flag_events = 2 * len(item.active) * flag.primitive_events
        # All cell-local flag routes can run together.  Response word routes use 27 colors.
        compiled_depth = word_depth + c474.COLOR_COUNT * response_roundtrip + 2 * flag.primitive_events
        for pair in fixture.pairs:
            history = dual_colored_history(fixture.radius, pair)
            baseline = c472.relax_history(fixture.radius, pair)
            restored = dual_colored_history(fixture.radius, pair, reverse=True, history=history)
            failures += int(history != baseline)
            failures += int(any(value for layer in restored for value in layer))
            source_colors = tuple(c474.color(coord) for coord in pair)
            source_rounds = len(set(source_colors))
            for layer in range(c463.ITERATIONS):
                targets = []
                for item_round in c474.rounds(fixture.radius, layer):
                    targets.extend(item_round.targets)
                    supports = [c474.star(target) for target in item_round.targets]
                    failures += sum(bool(left & right) for left, right in combinations(supports, 2))
                failures += int(set(targets) != set(item.active) or len(targets) != len(set(targets)))
            digest = sha256()
            digest.update(f"{fixture.name}|{pair}|{source_colors}|".encode())
            for datum in block_data:
                digest.update(f"{datum['layer']}|{datum['block_manifest']}\n".encode())
            digest.update(c470.action_digest(response).encode())
            digest.update(c470.action_digest((flag,)).encode())
            row = ManifestRow(
                fixture.name, pair, word_events, response_events, flag_events,
                word_events + response_events + flag_events,
                compiled_depth, source_colors, source_rounds, digest.hexdigest(),
            )
            rows.append(row)
    check(
        "full-layer Cycle474 schedules reproduce every dual-source Cycle472 word history and exact inverse with conflict-free Cycle470 block support",
        failures == 0 and len(rows) == 7
        and response_ingress_events == 571_968 and flag.primitive_events == 193,
        {"branches": [row.__dict__ for row in rows],
         "history_or_conflict_failures": failures,
         "response_actions_per_cell": len(response),
         "response_ingress_events_per_cell": response_ingress_events,
         "response_roundtrip_events_per_cell": response_roundtrip,
         "response_action_digest": c470.action_digest(response),
         "flag_path_distance": flag.distance, "flag_events_per_compute": flag.primitive_events,
         "flag_action_digest": c470.action_digest((flag,)),
         "opaque_response_vertices_per_branch": 2,
         "primitive_word_to_weight_or_vertex_events_in_counts": 0},
    )
    return tuple(rows)


def put_word(state: list[int], coords: tuple[Coord, ...], value: int) -> None:
    for bit, coord in enumerate(coords):
        state[c470.state_index(coord)] = (value >> bit) & 1


def get_word(state: list[int], coords: tuple[Coord, ...]) -> int:
    return sum(state[c470.state_index(coord)] << bit for bit, coord in enumerate(coords))


def delivered_weights(words: tuple[int, ...]) -> np.ndarray:
    total = sum(words)
    if total == 0:
        return np.full(6, 1 / 6, dtype=float)
    return np.asarray([float(Fraction(value, total)) for value in words], dtype=float)


def literal_delivery_controls(circuit: c467.Circuit, factors,
                              weight_rows) -> dict[str, object]:
    actions = response_actions(circuit)
    rows = []
    failures = 0
    route_deletion_residuals = []
    return_deletion_witnesses = 0
    for fixture in c472.FIXTURES:
        item = c463.domain(fixture.radius)
        for pair in fixture.pairs:
            history = c472.relax_history(fixture.radius, pair)
            final = history[-1]
            expected_pair_weights = weight_rows[(fixture.radius, pair)]
            observed_weights = []
            for endpoint, source_coord in enumerate(pair):
                words = tuple(
                    final[item.active_index[tuple(np.asarray(source_coord) + np.asarray(direction))]]
                    if tuple(np.asarray(source_coord) + np.asarray(direction)) in item.active_index else 0
                    for direction in response_directions()
                )
                state = [0] * (7 * c463.SUPERCELL_M2)
                for direction, value in zip(response_directions(), words):
                    put_word(
                        state,
                        tuple(c470.history_coord(direction, c463.ITERATIONS, bit) for bit in range(B)),
                        value,
                    )
                initial = tuple(state)
                executor = c470.TransferExecutor(state)
                executor.execute_ingress(actions)
                delivered = tuple(
                    get_word(
                        state,
                        tuple(c470.compact_coord(circuit.layout.neighbor[port_lane(direction)][bit]) for bit in range(B)),
                    )
                    for direction in response_directions()
                )
                weights = delivered_weights(delivered)
                observed_weights.append(weights)
                failures += int(delivered != words)
                failures += int(float(np.max(abs(weights - expected_pair_weights[endpoint]))) > c472.TOLERANCE)
                port_occupancy = sum(
                    state[c470.state_index(c470.compact_coord(wire))]
                    for lane in circuit.layout.neighbor for wire in lane
                )
                return_deletion_witnesses += int(port_occupancy > 0)
                executor.execute_egress(actions)
                failures += int(state != list(initial))
                failures += int(executor.adjacency_failures != 0)
            intact = c472.common_source_step(c472.initial_state(), factors, tuple(observed_weights))
            changed_weights = [value.copy() for value in observed_weights]
            source_words = tuple(
                final[item.active_index[tuple(np.asarray(pair[0]) + np.asarray(direction))]]
                if tuple(np.asarray(pair[0]) + np.asarray(direction)) in item.active_index else 0
                for direction in response_directions()
            )
            nonzero = next(index for index, value in enumerate(source_words) if value)
            deleted_words = tuple(0 if index == nonzero else value for index, value in enumerate(source_words))
            changed_weights[0] = delivered_weights(deleted_words)
            deleted_state = c472.common_source_step(c472.initial_state(), factors, tuple(changed_weights))
            route_deletion_residuals.append(c472.state_residual(intact, deleted_state))
            rows.append({
                "fixture": fixture.name, "pair": pair,
                "weight_residual": max(float(np.max(abs(observed_weights[index] - expected_pair_weights[index]))) for index in (0, 1)),
                "route_deletion_residual": route_deletion_residuals[-1],
            })
    flag = flag_action()
    flag_state = [0] * (7 * c463.SUPERCELL_M2)
    flag_state[c470.state_index(c467.path_coordinate(ENDPOINT_START))] = 1
    flag_initial = tuple(flag_state)
    flag_executor = c470.TransferExecutor(flag_state)
    flag_executor.execute_action(flag)
    flag_after_compute = flag_state[c470.state_index(c470.source_storage_coord())]
    flag_executor.execute_action(flag)
    flag_restored = flag_state == list(flag_initial)
    check(
        "every train/held source endpoint literally receives and returns all six final words with exact Cycle472 weights and visible route deletion",
        failures == 0 and len(rows) == 7 and return_deletion_witnesses == 14
        and min(route_deletion_residuals) > c472.SIGNAL_FLOOR
        and flag_after_compute == 1 and flag_restored and flag_executor.adjacency_failures == 0,
        {"rows": rows, "literal_source_endpoints": 14,
         "route_or_restoration_failures": failures,
         "populated_port_return_deletion_witnesses": return_deletion_witnesses,
         "minimum_consumed_word_route_deletion_residual": min(route_deletion_residuals),
         "flag_after_compute": flag_after_compute, "flag_inverse_restored": flag_restored,
         "response_ingress_events_per_endpoint": sum(action.primitive_events for action in actions),
         "response_roundtrip_events_per_endpoint": 2 * sum(action.primitive_events for action in actions)},
    )
    return {"rows": rows, "minimum_route_deletion": min(route_deletion_residuals)}


def run_cycle472_preservation() -> tuple[object, dict, dict]:
    print("\nFROZEN CYCLE472 PRESERVATION RUN")
    c472.PASS = 0
    c472.FAIL = 0
    started = perf_counter()
    factors = c472.c315.logical_update_controls(c472.c322.LABELS)[:3]
    weights = c472.word_generation_controls()
    c472.operator_and_covariance_controls(weights)
    fixture_results = c472.response_controls(factors, weights)
    c472.physical_eg_controls(factors, weights)
    c472.deletions_and_seam_controls(factors, weights)
    c472.mass_contact_and_routing_controls(started)
    c472.domain_inventory_no_go_controls(started)
    species = c472.c219.common_species(-0.3)
    mass_residual = abs(c472.c219.rest_mass(species) - species.analytic_mass)
    check(
        "Cycle472 E/G, mass, contact, leakage, inverse, held response, and source/response deletions survive unchanged",
        # Cycle472 has eight scientific controls here; its ninth main-run
        # control is the Cycle472 note contract, which is intentionally not
        # re-run as a substitute for a preservation test.
        c472.PASS == 8 and c472.FAIL == 0 and mass_residual < 2e-12
        and fixture_results[c472.HELD.name]["minimum_pairwise_response"] > c472.BRANCH_FLOOR
        and fixture_results[c472.HELD.name]["Schmidt_tail"] > c472.SIGNAL_FLOOR,
        {"Cycle472_pass": c472.PASS, "Cycle472_fail": c472.FAIL,
         "mass": species.analytic_mass, "mass_residual": mass_residual,
         "Cycle230_contact_nontrivial_columns": 4047,
         "physical_EG_leakage_inverse_cap": c472.TOLERANCE,
         "held_word_response_residual_cap": c472.WORD_THRESHOLD,
         "held_minimum_pairwise_response": fixture_results[c472.HELD.name]["minimum_pairwise_response"],
         "held_Schmidt_tail": fixture_results[c472.HELD.name]["Schmidt_tail"],
         "held_Schmidt_rank": fixture_results[c472.HELD.name]["Schmidt_rank"]},
    )
    return factors, weights, fixture_results


def capacity_and_conflict_controls(rows: tuple[ManifestRow, ...]) -> None:
    response_roundtrip = 2 * sum(action.primitive_events for action in response_actions(
        c467.make_circuit(B, c463.DENOMINATOR)
    ))
    results = []
    failures = 0
    for fixture in c472.FIXTURES:
        item = c463.domain(fixture.radius)
        maximum_parallel = max(len(item_round.targets) for item_round in c474.rounds(fixture.radius, 0))
        for item_round in c474.rounds(fixture.radius, 0):
            supports = [c474.star(target) for target in item_round.targets]
            failures += sum(bool(left & right) for left, right in combinations(supports, 2))
        branch = next(row for row in rows if row.fixture == fixture.name)
        results.append({
            "fixture": fixture.name, "active_cells": len(item.active),
            "per_active_cell_used_M2": SOURCE_CELL_USED,
            "per_active_cell_reserve_M2": SOURCE_CELL_RESERVE,
            "domain_capacity_M2": item.physical_m2,
            "maximum_parallel_stars": maximum_parallel,
            "maximum_simultaneous_support_M2": maximum_parallel * 7 * c463.SUPERCELL_M2,
            "response_roundtrip_per_cell": response_roundtrip,
            "compiled_forward_events": branch.compiled_forward_events,
            "compiled_parallel_depth": branch.compiled_parallel_depth,
        })
    check(
        "uniform endpoint banks, full-layer word/response delivery, flag paths, ports, and colored stars fit with zero simultaneous conflict",
        failures == 0 and SOURCE_CELL_USED == 46_407 and SOURCE_CELL_RESERVE == 17_593
        and [row["maximum_parallel_stars"] for row in results] == [1, 8],
        {"rows": results, "simultaneous_M2_path_port_endpoint_conflicts": failures,
         "endpoint_bank": {"matter_M2": 29, "hard_core_source_star_M2": 7,
                           "reservoir_index": ENDPOINT_START,
                           "persistent_flag_index": c470.SOURCE_STORAGE},
         "response_factor_events_counted": False,
         "primitive_word_to_weight_events_counted": False},
    )


def transform_pair(frame: c463.Frame, pair: Pair) -> Pair:
    return tuple(c463.transform(frame, coord) for coord in pair)  # type: ignore[return-value]


def covariance_controls(circuit: c467.Circuit, rows: tuple[ManifestRow, ...]) -> None:
    frames = c463.proper_cubic_frames()
    response = response_actions(circuit)
    flag = flag_action()
    failures = 0
    manifests = []
    for frame in frames:
        digest = sha256()
        digest.update(repr(frame).encode())
        carried_response_directions = []
        for action in response:
            carried_direction = c463.transform(frame, action.direction) if action.direction is not None else None
            carried_response_directions.append(carried_direction)
            carried_path = tuple(c470.transform_global(frame, coord) for coord in action.path)
            failures += sum(c467.manhattan(left, right) != 1 for left, right in zip(carried_path, carried_path[1:]))
            digest.update(f"{action.role}|{carried_direction}|{action.bit}|{carried_path}\n".encode())
        failures += int(set(carried_response_directions) != {
            c463.transform(frame, direction) for direction in response_directions()
        })
        carried_flag_path = tuple(c470.transform_global(frame, coord) for coord in flag.path)
        failures += sum(c467.manhattan(left, right) != 1 for left, right in zip(carried_flag_path, carried_flag_path[1:]))
        for fixture in c472.FIXTURES:
            item = c463.domain(fixture.radius)
            for pair in fixture.pairs:
                carried_pair = transform_pair(frame, pair)
                failures += int(any(coord not in item.active_index for coord in carried_pair))
                source_colors = tuple(c474.transform_color(frame, c474.color(coord)) for coord in pair)
                failures += int(source_colors != tuple(c474.color(coord) for coord in carried_pair))
                for layer in range(c463.ITERATIONS):
                    carried_sequence = []
                    for item_round in c474.rounds(fixture.radius, layer):
                        carried_color = c474.transform_color(frame, item_round.color)
                        carried_targets = tuple(c463.transform(frame, target) for target in item_round.targets)
                        carried_sequence.append(carried_color)
                        failures += int(set(carried_targets) != {
                            target for target in item.active if c474.color(target) == carried_color
                        })
                    failures += int(tuple(carried_sequence) != tuple(c474.transform_color(frame, value) for value in c474.COLORS))
                branch = next(row for row in rows if row.fixture == fixture.name and row.pair == pair)
                digest.update(f"{fixture.name}|{carried_pair}|{source_colors}|{branch.digest}|no-resort\n".encode())
        manifests.append(digest.hexdigest())
    check(
        "all 24 proper-cubic frames carry full-layer colors, source flags/endpoints, final-word paths/ports, and both response vertices without global re-sorting",
        len(frames) == 24 and failures == 0 and len(set(manifests)) == 24,
        {"frames": len(frames), "carried_failures": failures,
         "frame_manifests": manifests, "global_resort_used": False,
         "carried_objects": "source pair, source colors, endpoint bank, flag path, word directions, face paths, ports, complete reference round sequence"},
    )


def deletion_domain_and_inventory_controls(circuit: c467.Circuit, factors, weights,
                                           delivery_results: dict[str, object]) -> None:
    pair = c472.HELD.pairs[-1]
    history = dual_colored_history(c472.HELD.radius, pair)
    deleted_history = dual_colored_history(c472.HELD.radius, pair, delete_source=0)
    source_route_changes = history != deleted_history
    nonblank_refused = False
    try:
        state = [0] * (7 * c463.SUPERCELL_M2)
        wire = circuit.layout.neighbor[0][0]
        state[c470.state_index(c470.compact_coord(wire))] = 1
        c470.validate_blank_compact(state, circuit)
    except ValueError:
        nonblank_refused = True
    duplicate_source_refused = False
    try:
        c472.validate_pair(c472.HELD.radius, (pair[0], pair[0]))
    except ValueError:
        duplicate_source_refused = True
    malformed_round_refused = False
    try:
        item = c463.domain(c472.HELD.radius)
        bad = c474.Round(0, 0, 1, (0, 0, 0), ((1, 0, 0),))
        c474.validate_round(item, bad)
    except ValueError:
        malformed_round_refused = True
    response_deletion = []
    intact = c472.common_source_step(c472.initial_state(), factors, weights[(c472.HELD.radius, pair)])
    for endpoint in (0, 1):
        enabled = (endpoint != 0, endpoint != 1)
        response_deletion.append(c472.state_residual(
            intact,
            c472.common_source_step(c472.initial_state(), factors, weights[(c472.HELD.radius, pair)], enabled=enabled),
        ))
    check(
        "source-route, consumed-word route, response vertex, return, color, port, and pair deletions are exposed",
        source_route_changes and float(delivery_results["minimum_route_deletion"]) > c472.SIGNAL_FLOOR
        and min(response_deletion) > c472.SIGNAL_FLOOR
        and nonblank_refused and duplicate_source_refused and malformed_round_refused,
        {"source_route_changes_word_history": source_route_changes,
         "minimum_consumed_word_route_deletion": delivery_results["minimum_route_deletion"],
         "response_vertex_deletions": response_deletion,
         "return_deletion": "14 literal endpoint runs retain populated ports until inverse egress",
         "nonblank_port_refused": nonblank_refused,
         "duplicate_source_refused": duplicate_source_refused,
         "malformed_color_round_refused": malformed_round_refused},
    )
    check(
        "the supplied/constructed/open inventory keeps response synthesis, time, source, probability, and gravity walls explicit",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "supplied": ["Cycle463 finite retained word law", "Cycle467 arithmetic",
                         "Cycle470 occupied-path transport", "Cycle472 Q2 source/weight/vertex law",
                         "Cycle474 27-color order", "uniform 36-M2 endpoint banks"],
            "constructed": ["dual-source colored histories/inverse", "uniform source-flag paths",
                             "full-layer final-word delivery/return", "literal delivery at all14 active endpoints",
                             "capacity/conflict/event manifests", "all24 carried composition"],
            "available_separately": ["Cycle476 fixed-P=8 q1 word-to-weight NCT",
                                     "Cycle476 eight-step symmetric bit-controlled response product"],
            "open": ["Cycle476/Cycle477 augmented-block whole-layer composition",
                     "source-flag conditioning and discrete onsite-angle synthesis",
                     "q>1 or exact-exponential response", "autonomous response-law selection",
                     "history removal and optimized scheduling",
                     "source calibration, physical time, asymptotics, geometry, occurrence"],
            "scope": "full-layer delivery interface with two active response vertices; not a fully primitive full-layer response",
            "event_manifest_is_not_full_primitive_response_execution": True,
            "primitive_word_to_weight_synthesis_is_not_claimed": True,
            "not_claimed": ["probability", "time", "energy", "force", "lapse", "metric", "backreaction", "gravity"],
        },
    )


def frozen_and_no_go_controls() -> None:
    paths = {
        "Cycle467": ROOT / "scripts/physical_elementary_divsix_nn_compiler_cycle467_2026_07_19.py",
        "Cycle470": ROOT / "scripts/physical_seven_supercell_port_delivery_compiler_cycle470_2026_07_19.py",
        "Cycle472": ROOT / "scripts/physical_dual_source_reciprocal_composition_cycle472_2026_07_19.py",
        "Cycle474": ROOT / "scripts/physical_mod3_star_layer_scheduler_cycle474_2026_07_19.py",
        "Cycle476": ROOT / "scripts/physical_word_weight_control_compiler_cycle476_2026_07_19.py",
    }
    observed = {name: file_sha(path) for name, path in paths.items()}
    expected = {"Cycle467": FROZEN_C467_SHA, "Cycle470": FROZEN_C470_SHA,
                "Cycle472": FROZEN_C472_SHA, "Cycle474": FROZEN_C474_SHA,
                "Cycle476": FROZEN_C476_SHA}
    check(
        "Cycles467/470/472/474/476 remain frozen at their exact compiler identities",
        observed == expected,
        {"observed": observed, "expected": expected,
         "Cycle467_route": FROZEN_C467_ROUTE, "Cycle470_literal_manifest": FROZEN_C470_LITERAL},
    )
    check(
        "full N1-N8 rejects no-go, minimum-content, and axiom-pressure promotion",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "N1": "full-layer unconditional delivery succeeds; selected-star, flag-controlled Fredkin routing, cached faces, packet networks, Cycle476 fixed-P composition, exact small-block simulation, and discrete-angle synthesis remain alternatives",
            "N2": "delivery, word-to-weight synthesis, response-law selection, history, source calibration, time, asymptotics, occurrence, and gravity remain independent",
            "N3": "uniform blank endpoint banks, two Q1 occupations, retained histories, 27 colors, opaque weight/vertex factors, pair menus, and boundaries are exposed",
            "N4": "this witness matches Cycle472's named Cycle470/whole-layer delivery residual; Cycle476 separately matches fixed-P q1 weight/control, while their augmented composition, P2, source/time, and gravity residuals remain",
            "N5": "claims stop at a finite full-layer delivery interface and branchwise two-vertex response preservation; no primitive-response, probability, force, or gravity rhetoric",
            "N6": "delivery and Cycle476 fixed-P q1 weight/control close separately; augmented-block composition, discrete angles, exact or q>1 response, and autonomous conditional vertices remain direct routes",
            "N7": "a reviewer can demand primitive normalization/root/exponential, fewer redundant inactive deliveries, recurrent matter transport, calibration, and infrared control",
            "N8": "Cycle472's transport residual and Cycle476's fixed-P q1 control residual close on separate interfaces; augmented composition, angle/source/time/gravity walls remain; no axiom pressure",
        },
    )


def resource_controls(started: float) -> None:
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    check(
        "the complete Cycle477 run stays below explicit wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
        {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
         "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB},
    )


def main() -> int:
    started = perf_counter()
    print("Cycle477 physical dual-source full-layer delivery/response interface")
    print("authority", AUTHORITY, "audit", AUDIT)
    note_contract()
    factors, weights, _fixture_results = run_cycle472_preservation()
    circuit = c467.make_circuit(B, c463.DENOMINATOR)
    rows = full_layer_manifest_controls(circuit)
    delivery_results = literal_delivery_controls(circuit, factors, weights)
    capacity_and_conflict_controls(rows)
    covariance_controls(circuit, rows)
    deletion_domain_and_inventory_controls(circuit, factors, weights, delivery_results)
    frozen_and_no_go_controls()
    resource_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
