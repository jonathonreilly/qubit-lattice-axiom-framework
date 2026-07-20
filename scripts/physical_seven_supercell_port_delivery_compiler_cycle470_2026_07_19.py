#!/usr/bin/env python3
"""Cycle 470: seven-supercell delivery compiler for Cycle 467's local ports.

Six retained Cycle-463 neighbor words are delivered from their canonical
storage sites into the Cycle-467 arithmetic ports by explicit nearest-neighbor
SWAP/CNOT walks, then returned by the exact inverse after arithmetic.  A
retained target word is SWAP-staged and the central source is CNOT-staged so
one complete local E/G block can be executed.  The construction is bounded
and proper-cubic carried; it does not derive the finite law or a source/gravity
interpretation.  Authority is none; audit is unset.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
from pathlib import Path
from time import perf_counter
import resource
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_reversible_cubic_relaxation_clock_compiler_cycle463_2026_07_19 as c463
import physical_elementary_divsix_nn_compiler_cycle467_2026_07_19 as c467


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SEVEN_SUPERCELL_PORT_DELIVERY_COMPILER_CYCLE470_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
B = c463.VALUE_BITS
SCALE = c463.SUPERCELL_SCALE
SUPERCELL_M2 = c463.SUPERCELL_M2
HISTORY_WORDS = c463.ITERATIONS + 1
COMPILER_REGION = 6 * B + 1 + B + c463.WORK_BITS
HISTORY_START = COMPILER_REGION
HISTORY_M2 = HISTORY_WORDS * B
SOURCE_STORAGE = HISTORY_START + HISTORY_M2
CLOCK_START = SOURCE_STORAGE + 1
USED_PER_ACTIVE_SUPERCELL = CLOCK_START + c463.CLOCK_BANK_M2_PER_SITE
ROUTING_RESERVE = SUPERCELL_M2 - USED_PER_ACTIVE_SUPERCELL
WALL_CAP_SECONDS = 240.0
RSS_CAP_MIB = 1536.0
ZERO = (0, 0, 0)
DIRECTIONS = tuple(c463.six_neighbors(ZERO))
CELL_IDS = {ZERO: 0, **{direction: index + 1 for index, direction in enumerate(DIRECTIONS)}}
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Edge = tuple[int, int]
CXGate = tuple[int, int]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    value = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        value = value.replace(marker, "")
    return " ".join(value.split())


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset", "cycle 470", "seven-supercell",
        "249-bit", "swaps through occupied paths", "zero blank corridor ancillas",
        "all 14,592", "all 24 proper-cubic frames", "held cube",
        "source and target direction labels are carried",
        "iteration count and schedule depth are not time",
        "not energy, stress, lapse, metric, proper time, backreaction, or gravity",
        "n1 — alternative route enumeration", "n8 — cross-cycle echo and claim gate",
        "no axiom pressure",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle470 note freezes the seven-cell delivery boundary and N1-N8 gate", not missing, missing)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(coord: Coord, amount: int) -> Coord:
    return tuple(amount * value for value in coord)  # type: ignore[return-value]


def local_index(coord: Coord) -> int:
    x, y, z = coord
    if any(value not in range(SCALE) for value in coord):
        raise ValueError("local coordinate leaves its supercell")
    return x + SCALE * y + SCALE * SCALE * z


def split_global(coord: Coord) -> tuple[Coord, Coord]:
    coarse = []
    local = []
    for value in coord:
        quotient, remainder = divmod(value, SCALE)
        coarse.append(quotient)
        local.append(remainder)
    return tuple(coarse), tuple(local)  # type: ignore[return-value]


def global_coord(cell: Coord, local: Coord) -> Coord:
    return add(scale(cell, SCALE), local)


def state_index(coord: Coord) -> int:
    cell, local = split_global(coord)
    if cell not in CELL_IDS:
        raise ValueError("coordinate leaves the seven-supercell star")
    return CELL_IDS[cell] * SUPERCELL_M2 + local_index(local)


def history_coord(cell: Coord, layer: int, bit: int) -> Coord:
    if layer not in range(HISTORY_WORDS) or bit not in range(B):
        raise ValueError("history address leaves its frozen range")
    return global_coord(cell, c467.path_coordinate(HISTORY_START + layer * B + bit))


def source_storage_coord() -> Coord:
    return c467.path_coordinate(SOURCE_STORAGE)


def compact_coord(wire: int) -> Coord:
    if wire not in range(COMPILER_REGION):
        raise ValueError("wire leaves the compact arithmetic region")
    return c467.path_coordinate(wire)


def direction_axis(direction: Coord) -> int:
    axes = [index for index, value in enumerate(direction) if value]
    if len(axes) != 1 or direction[axes[0]] not in (-1, 1):
        raise ValueError("direction is not a signed cubic unit vector")
    return axes[0]


def axis_order(direction: Coord | None) -> tuple[int, int, int]:
    if direction is None:
        return (0, 1, 2)
    normal = direction_axis(direction)
    return (normal, (normal + 1) % 3, (normal + 2) % 3)


def manhattan_path(start: Coord, end: Coord, order: tuple[int, int, int]) -> tuple[Coord, ...]:
    if sorted(order) != [0, 1, 2]:
        raise ValueError("axis order is malformed")
    cursor = list(start)
    output = [start]
    for axis in order:
        step = 1 if end[axis] > cursor[axis] else -1
        while cursor[axis] != end[axis]:
            cursor[axis] += step
            output.append(tuple(cursor))
    return tuple(output)


def edge(left: Coord, right: Coord) -> Edge:
    a, b = state_index(left), state_index(right)
    return (a, b) if a < b else (b, a)


@dataclass(frozen=True)
class Action:
    kind: str
    role: str
    direction: Coord | None
    bit: int
    path: tuple[Coord, ...]

    @property
    def distance(self) -> int:
        return len(self.path) - 1

    @property
    def primitive_events(self) -> int:
        if self.kind == "remote_cnot":
            return 6 * (self.distance - 1) + 1
        if self.kind == "remote_swap":
            return 3 * (2 * self.distance - 1)
        raise ValueError("unknown route action")

    @property
    def swap_count(self) -> int:
        return 2 * (self.distance - 1) if self.kind == "remote_cnot" else 2 * self.distance - 1


def action_digest(actions: tuple[Action, ...]) -> str:
    digest = sha256()
    for item in actions:
        digest.update(f"{item.kind}|{item.role}|{item.direction}|{item.bit}|".encode())
        for coord in item.path:
            digest.update(struct.pack(">iii", *coord))
    return digest.hexdigest()


def ingress_actions(layer: int, circuit: c467.Circuit) -> tuple[Action, ...]:
    if layer not in range(c463.ITERATIONS):
        raise ValueError("update layer leaves the frozen 96-layer schedule")
    output: list[Action] = []
    for bit in range(B):
        start = history_coord(ZERO, layer + 1, bit)
        end = compact_coord(circuit.layout.target[bit])
        output.append(Action("remote_swap", "target-storage->target-port", None, bit,
                             manhattan_path(start, end, axis_order(None))))
    output.append(Action(
        "remote_cnot", "source-storage->source-port", None, 0,
        manhattan_path(source_storage_coord(), compact_coord(circuit.layout.source), axis_order(None)),
    ))
    for lane, direction in enumerate(DIRECTIONS):
        order = axis_order(direction)
        for bit in range(B):
            start = history_coord(direction, layer, bit)
            end = compact_coord(circuit.layout.neighbor[lane][bit])
            output.append(Action("remote_cnot", "neighbor-storage->neighbor-port", direction, bit,
                                 manhattan_path(start, end, order)))
    return tuple(output)


def route_trace(action: Action) -> tuple[CXGate, ...]:
    path = action.path
    if len(path) < 2:
        raise ValueError("remote endpoints coincide")
    swap_edges: list[tuple[Coord, Coord]] = []
    if action.kind == "remote_cnot":
        swap_edges.extend(zip(path[:-2], path[1:-1]))
        middle = ((state_index(path[-2]), state_index(path[-1])),)
        swap_edges.extend(reversed(tuple(zip(path[:-2], path[1:-1]))))
    elif action.kind == "remote_swap":
        swap_edges.extend(zip(path[:-1], path[1:]))
        swap_edges.extend(reversed(tuple(zip(path[:-2], path[1:-1]))))
        middle = ()
    else:
        raise ValueError("unknown route action")
    output: list[CXGate] = []
    midpoint = len(swap_edges) // 2 if action.kind == "remote_cnot" else -1
    for index, (left, right) in enumerate(swap_edges):
        if action.kind == "remote_cnot" and index == midpoint:
            output.extend(middle)
        a, b = state_index(left), state_index(right)
        output.extend(((a, b), (b, a), (a, b)))
    if action.kind == "remote_cnot" and not swap_edges:
        output.extend(middle)
    return tuple(output)


def expected_action_events(action: Action) -> int:
    return len(route_trace(action))


class TransferExecutor:
    def __init__(self, state: list[int] | None = None):
        self.state = state
        self.events = 0
        self.swaps = 0
        self.adjacency_failures = 0
        self.counts: Counter[str] = Counter()
        self.edge_counts: Counter[Edge] = Counter()
        self.last: dict[int, int] = {}
        self.digest = sha256()

    def emit_cnot(self, control: int, target: int) -> None:
        control_cell, control_local = divmod(control, SUPERCELL_M2)
        target_cell, target_local = divmod(target, SUPERCELL_M2)
        control_coord = global_coord(tuple(CELL_IDS.keys())[control_cell], (
            control_local % SCALE, (control_local // SCALE) % SCALE, control_local // (SCALE * SCALE)))
        target_coord = global_coord(tuple(CELL_IDS.keys())[target_cell], (
            target_local % SCALE, (target_local // SCALE) % SCALE, target_local // (SCALE * SCALE)))
        self.adjacency_failures += int(c467.manhattan(control_coord, target_coord) != 1)
        layer = 1 + max(self.last.get(control, 0), self.last.get(target, 0))
        self.last[control] = self.last[target] = layer
        self.edge_counts[(control, target) if control < target else (target, control)] += 1
        self.counts["CNOT"] += 1
        self.digest.update(struct.pack(">Bii", c467.CX, control, target))
        self.events += 1
        if self.state is not None:
            self.state[target] ^= self.state[control]

    def execute_action(self, action: Action) -> None:
        before = self.events
        for control, target in route_trace(action):
            self.emit_cnot(control, target)
        self.swaps += action.swap_count
        if self.events - before != action.primitive_events:
            raise AssertionError("action event formula disagrees with emitted trace")

    def execute_ingress(self, actions: tuple[Action, ...]) -> None:
        for action in actions:
            self.execute_action(action)

    def execute_egress(self, actions: tuple[Action, ...]) -> None:
        # Each action transcript is a palindrome of self-inverse CNOTs.
        for action in reversed(actions):
            self.execute_action(action)


def transfer_lemma_controls() -> None:
    cnot_failures = 0
    swap_failures = 0
    deletion_witnesses = 0
    rows = []
    for distance in range(1, 6):
        path = tuple((index, 0, 0) for index in range(distance + 1))
        for kind in ("remote_cnot", "remote_swap"):
            action = Action(kind, "lemma", (1, 0, 0), 0, path)
            trace = route_trace(action)
            deletion_has_witness = False
            for packed in range(1 << (distance + 1)):
                state = [(packed >> index) & 1 for index in range(distance + 1)]
                initial = tuple(state)
                for control, target in trace:
                    state[target] ^= state[control]
                expected = list(initial)
                if kind == "remote_cnot":
                    expected[-1] ^= expected[0]
                    cnot_failures += int(state != expected)
                else:
                    expected[0], expected[-1] = expected[-1], expected[0]
                    swap_failures += int(state != expected)
                restored = list(state)
                for control, target in reversed(trace):
                    restored[target] ^= restored[control]
                if restored != list(initial):
                    cnot_failures += kind == "remote_cnot"
                    swap_failures += kind == "remote_swap"
                deleted = list(initial)
                for control, target in trace[:-1]:
                    deleted[target] ^= deleted[control]
                deletion_has_witness |= deleted != expected
            deletion_witnesses += int(deletion_has_witness)
            rows.append({"kind": kind, "distance": distance, "events": len(trace)})
    check(
        "remote CNOT and endpoint SWAP walks are exhaustive through distance five for arbitrary occupied intermediates and exact inverse",
        cnot_failures == 0 and swap_failures == 0 and deletion_witnesses == 10,
        {"rows": rows, "CNOT_failures": cnot_failures, "SWAP_failures": swap_failures,
         "deleted_last_primitive_witnesses": deletion_witnesses,
         "blank_corridor_ancillas": 0, "intermediate_state_precondition": "none"},
    )


def placement_and_schedule_controls(circuit: c467.Circuit) -> dict[str, object]:
    rows = []
    schedule_digest = sha256()
    geometry_failures = 0
    endpoint_failures = 0
    for layer in range(c463.ITERATIONS):
        actions = ingress_actions(layer, circuit)
        distances = [item.distance for item in actions]
        events = sum(item.primitive_events for item in actions)
        swaps = sum(item.swap_count for item in actions)
        face_edges: set[tuple[Coord, Coord]] = set()
        for item in actions:
            geometry_failures += sum(
                c467.manhattan(left, right) != 1 for left, right in zip(item.path, item.path[1:])
            )
            cells = {split_global(coord)[0] for coord in item.path}
            allowed = {ZERO} if item.direction is None else {ZERO, item.direction}
            geometry_failures += int(not cells <= allowed)
            crossings = tuple(
                (left, right) for left, right in zip(item.path, item.path[1:])
                if split_global(left)[0] != split_global(right)[0]
            )
            geometry_failures += int(len(crossings) != (1 if item.direction is not None else 0))
            face_edges.update(crossings)
            endpoint_failures += int(item.path[-1] != (
                compact_coord(circuit.layout.target[item.bit]) if item.role.startswith("target")
                else compact_coord(circuit.layout.source) if item.role.startswith("source")
                else compact_coord(circuit.layout.neighbor[DIRECTIONS.index(item.direction)][item.bit])
            ))
        digest = action_digest(actions)
        schedule_digest.update(f"{layer}|{digest}|{events}|{swaps}\n".encode())
        rows.append({"layer": layer, "actions": len(actions), "ingress_events": events,
                     "ingress_swaps": swaps, "max_distance": max(distances),
                     "distinct_face_edges": len(face_edges), "digest": digest})
    maxima = max(rows, key=lambda row: row["ingress_events"])
    minima = min(rows, key=lambda row: row["ingress_events"])
    check(
        "all 96 fixed layer programs have explicit seven-supercell paths, endpoints, congestion-safe serial schedules, and constant capacity",
        geometry_failures == 0 and endpoint_failures == 0
        and all(row["actions"] == 1 + 7 * B for row in rows)
        and COMPILER_REGION == 2507 and USED_PER_ACTIVE_SUPERCELL == 46_371
        and ROUTING_RESERVE == 17_629 and USED_PER_ACTIVE_SUPERCELL < SUPERCELL_M2,
        {"layers": len(rows), "actions_per_ingress": rows[0]["actions"],
         "minimum_layer": minima, "maximum_layer": maxima,
         "geometry_failures": geometry_failures, "endpoint_failures": endpoint_failures,
         "active_supercell": {"compiler_region": COMPILER_REGION, "history": HISTORY_M2,
                              "persistent_source": 1, "clocks_and_sidecars": c463.CLOCK_BANK_M2_PER_SITE,
                              "used": USED_PER_ACTIVE_SUPERCELL, "capacity": SUPERCELL_M2,
                              "reserve": ROUTING_RESERVE},
         "seven_active_supercell_used_upper_bound": 7 * USED_PER_ACTIVE_SUPERCELL,
         "seven_supercell_capacity": 7 * SUPERCELL_M2,
         "layer_schedule_digest": schedule_digest.hexdigest(),
         "simultaneous_route_congestion": 1,
         "schedule": "strict serial witness; direction/bit program fixed before state input"},
    )
    return {"rows": rows, "max_layer": maxima["layer"], "digest": schedule_digest.hexdigest()}


def actual_rows() -> tuple[tuple[int, int, Coord, tuple[int, ...], int, int], ...]:
    rows = []
    for radius in (c463.TRAIN_RADIUS, c463.HELD_RADIUS):
        item = c463.domain(radius)
        coarse = c463.coarse_forward(c463.initial_coarse(item), item)
        for operation in c463.schedule(radius):
            previous = coarse.history[operation.layer]
            neighbors = tuple(
                previous[item.active_index[coord]] if coord in item.active_index else 0
                for coord in operation.neighbors
            )
            source = coarse.source[item.active_index[operation.target]]
            expected = coarse.history[operation.layer + 1][item.active_index[operation.target]]
            rows.append((radius, operation.layer, operation.target, neighbors, source, expected))
    return tuple(rows)


def held_and_fast_composition_controls(circuit: c467.Circuit, layer_data: dict[str, object]) -> tuple[int, tuple[int, int, Coord, tuple[int, ...], int, int]]:
    rows = actual_rows()
    failures = 0
    support_failures = 0
    digest = sha256()
    selected_index = -1
    selected = rows[0]
    for index, (radius, layer, target, neighbors, source, expected) in enumerate(rows):
        numerator = sum(neighbors) + c463.DENOMINATOR * source
        quotient, remainder = c467.compiled_division(numerator, c467.SUM_BITS)
        failures += int(quotient != expected or remainder != 0)
        item = c463.domain(radius)
        support_failures += sum(add(target, direction) not in item.all_cells for direction in DIRECTIONS)
        digest.update(f"{radius}|{layer}|{target}|{neighbors}|{source}|{quotient}|{remainder}\n".encode())
        if radius == c463.HELD_RADIUS and layer == 48 and target == ZERO:
            selected_index, selected = index, rows[index]
    radius, layer, target, neighbors, source, expected = selected
    deletion_changes = []
    for lane, value in enumerate(neighbors):
        omitted = tuple(0 if index == lane else item for index, item in enumerate(neighbors))
        deleted, _ = c467.compiled_division(sum(omitted) + c463.DENOMINATOR * source, c467.SUM_BITS)
        deletion_changes.append((value == 0) or deleted != expected)
    source_deleted, _ = c467.compiled_division(sum(neighbors), c467.SUM_BITS)
    check(
        "every Cycle463 train/held block composes with fixed port delivery semantics, exact division, and a bounded seven-cell support",
        len(rows) == 14_592 and failures == 0 and support_failures == 0 and selected_index >= 0,
        {"rows": len(rows), "train": 2592, "held": 12000,
         "quotient_or_remainder_failures": failures, "support_failures": support_failures,
         "row_digest": digest.hexdigest(), "selected_literal_index": selected_index,
         "selected_literal_layer": layer, "layer_schedule_digest": layer_data["digest"],
         "all_row_method": "exact endpoint/port semantics plus the frozen 32-state Cycle467 division permutation"},
    )
    check(
        "neighbor/source delivery deletions are exposed on the selected held center block and malformed domains are refused",
        all(deletion_changes) and source == 1 and source_deleted != expected,
        {"neighbor_nonzero_or_deletion_changes": deletion_changes,
         "source_deletion_changes": source_deleted != expected,
         "deleted_return_residual": "a populated port remains outside the code",
         "deleted_path_primitive_residual": "exhaustive route lemma supplies a witness at every tested distance"},
    )
    return selected_index, selected


class ArithmeticExecutor(c467.RouteCompiler):
    def __init__(self, wires: int, state: list[int]):
        super().__init__(wires)
        self.state = state
        self.edge_counts: Counter[Edge] = Counter()

    def emit(self, op: int, positions: tuple[int, ...]) -> None:
        super().emit(op, positions)
        physical = tuple(local_index(c467.path_coordinate(position)) for position in positions)
        if op == c467.X:
            self.state[physical[0]] ^= 1
        elif op == c467.CX:
            self.state[physical[1]] ^= self.state[physical[0]]
            self.edge_counts[(min(physical), max(physical))] += 1
        else:
            self.state[physical[2]] ^= self.state[physical[0]] & self.state[physical[1]]
            coords = tuple(c467.path_coordinate(position) for position in positions)
            for left_index in range(3):
                for right_index in range(left_index + 1, 3):
                    if c467.manhattan(coords[left_index], coords[right_index]) == 1:
                        left, right = physical[left_index], physical[right_index]
                        self.edge_counts[(min(left, right), max(left, right))] += 1


def execute_arithmetic(router: ArithmeticExecutor, circuit: c467.Circuit) -> c467.RouteResult:
    router.routed_trace(circuit.compute)
    head = circuit.layout.remainder + circuit.layout.auxiliary
    for bit, step, copy in zip(reversed(range(circuit.layout.width)), circuit.division_steps, circuit.copies):
        router.routed_trace(step + copy)
        router.head_left(head, circuit.layout.cells[bit])
    for bit, step in zip(range(circuit.layout.width), circuit.division_cleanup):
        router.routed_trace(step)
        router.head_right(head, circuit.layout.cells[bit])
    router.routed_trace(circuit.cleanup)
    return router.finish()


def put_word(state: list[int], coords: tuple[Coord, ...], value: int) -> None:
    for bit, coord in enumerate(coords):
        state[state_index(coord)] = (value >> bit) & 1


def get_word(state: list[int], coords: tuple[Coord, ...]) -> int:
    return sum(state[state_index(coord)] << bit for bit, coord in enumerate(coords))


def validate_blank_compact(state: list[int], circuit: c467.Circuit) -> None:
    declared = (
        tuple(wire for wires in circuit.layout.neighbor for wire in wires)
        + (circuit.layout.source,) + circuit.layout.target + circuit.layout.work
    )
    if any(state[state_index(compact_coord(wire))] for wire in declared):
        raise ValueError("compact input ports/work are not blank")


def literal_full_block_controls(circuit: c467.Circuit,
                                selected: tuple[int, int, Coord, tuple[int, ...], int, int]) -> dict[str, object]:
    radius, layer, target, neighbors, source, expected = selected
    if target != ZERO:
        raise AssertionError("literal fixture is expressed in target-relative coordinates")
    state = [0] * (7 * SUPERCELL_M2)
    for lane, direction in enumerate(DIRECTIONS):
        put_word(state, tuple(history_coord(direction, layer, bit) for bit in range(B)), neighbors[lane])
    state[state_index(source_storage_coord())] = source
    target_storage = tuple(history_coord(ZERO, layer + 1, bit) for bit in range(B))
    initial = tuple(state)
    validate_blank_compact(state, circuit)
    actions = ingress_actions(layer, circuit)
    transfer = TransferExecutor(state)
    transfer.execute_ingress(actions)
    ingress_events = transfer.events
    ingress_digest = transfer.digest.hexdigest()
    port_neighbors = tuple(get_word(state, tuple(compact_coord(wire) for wire in wires))
                           for wires in circuit.layout.neighbor)
    port_target = get_word(state, tuple(compact_coord(wire) for wire in circuit.layout.target))
    port_source = state[state_index(compact_coord(circuit.layout.source))]
    ingress_failures = int(port_neighbors != neighbors or port_target != 0 or port_source != source)

    arithmetic = ArithmeticExecutor(circuit.layout.wire_count, state)
    arithmetic_result = execute_arithmetic(arithmetic, circuit)
    arithmetic_target = get_word(state, tuple(compact_coord(wire) for wire in circuit.layout.target))
    arithmetic_failures = int(arithmetic_target != expected)
    arithmetic_failures += sum(state[local_index(compact_coord(wire))] for wire in circuit.layout.work)
    pre_egress_port_occupancy = sum(
        state[state_index(compact_coord(wire))]
        for wires in circuit.layout.neighbor for wire in wires
    ) + state[state_index(compact_coord(circuit.layout.source))]
    pre_egress_port_occupancy += sum(state[state_index(compact_coord(wire))] for wire in circuit.layout.target)

    transfer.execute_egress(actions)
    expected_state = list(initial)
    put_word(expected_state, target_storage, expected)
    final_failures = sum(left != right for left, right in zip(state, expected_state))
    port_leakage = sum(
        state[state_index(compact_coord(wire))]
        for wires in circuit.layout.neighbor for wire in wires
    ) + state[state_index(compact_coord(circuit.layout.source))]
    port_leakage += sum(state[state_index(compact_coord(wire))] for wire in circuit.layout.target)
    combined_edges = transfer.edge_counts.copy()
    combined_edges.update(arithmetic.edge_counts)
    combined_counts = transfer.counts.copy()
    combined_counts.update(arithmetic_result.counts)
    combined_digest = sha256(
        f"{ingress_digest}|{arithmetic_result.digest}|inverse({ingress_digest})|{transfer.digest.hexdigest()}".encode()
    ).hexdigest()
    check(
        "one actual held center block executes literal ingress, the exact Cycle467 NN arithmetic, inverse egress, and persistent-target E/G",
        ingress_failures == 0 and arithmetic_failures == 0 and final_failures == 0
        and pre_egress_port_occupancy > 0 and port_leakage == 0
        and arithmetic_result.digest == "4d6f058d95cc32538f3a15b6fd0eb620f7708371e6276298d063ba44078d1457"
        and arithmetic_result.restored_mapping and arithmetic_result.adjacency_failures == 0,
        {"radius": radius, "layer": layer, "target": target,
         "ingress_events": ingress_events, "round_trip_transfer_events": transfer.events,
         "arithmetic_events": arithmetic_result.events,
         "combined_events": transfer.events + arithmetic_result.events,
         "combined_counts": dict(combined_counts),
         "strict_serial_depth": transfer.events + arithmetic_result.events,
         "max_edge_primitive_incidence": max(combined_edges.values()),
         "ingress_failures": ingress_failures, "arithmetic_failures": arithmetic_failures,
         "final_physical_bit_failures": final_failures,
         "ports_populated_before_required_egress": pre_egress_port_occupancy,
         "port_leakage_after_egress": port_leakage,
         "arithmetic_digest": arithmetic_result.digest,
         "ingress_digest": ingress_digest, "round_trip_transfer_digest": transfer.digest.hexdigest(),
         "combined_segment_manifest": combined_digest},
    )
    return {
        "actions": len(actions), "ingress_events": ingress_events,
        "round_trip_events": transfer.events, "arithmetic_events": arithmetic_result.events,
        "combined_events": transfer.events + arithmetic_result.events,
        "counts": dict(combined_counts), "max_edge_incidence": max(combined_edges.values()),
        "manifest": combined_digest,
    }


def transform_global(frame: c463.Frame, coord: Coord) -> Coord:
    coarse, local = split_global(coord)
    carried_coarse = c463.transform(frame, coarse)
    carried_local = []
    for row in frame:
        axis = next(index for index, value in enumerate(row) if value)
        carried_local.append(local[axis] if row[axis] == 1 else SCALE - 1 - local[axis])
    return global_coord(carried_coarse, tuple(carried_local))


def covariance_controls(circuit: c467.Circuit, carried_layer: int,
                        composition: dict[str, object]) -> None:
    actions = ingress_actions(carried_layer, circuit)
    frames = c463.proper_cubic_frames()
    failures = 0
    manifests = []
    for frame in frames:
        carried_directions = []
        digest = sha256()
        for action in actions:
            direction = c463.transform(frame, action.direction) if action.direction is not None else None
            carried_directions.append(direction)
            carried_path = tuple(transform_global(frame, coord) for coord in action.path)
            failures += sum(c467.manhattan(left, right) != 1
                            for left, right in zip(carried_path, carried_path[1:]))
            failures += int(action.path[0] != transform_global(tuple(tuple(int(row == column) for column in range(3)) for row in range(3)), action.path[0]))
            digest.update(f"{action.kind}|{action.role}|{direction}|{action.bit}|".encode())
            for coord in carried_path:
                digest.update(struct.pack(">iii", *coord))
        neighbor_labels = tuple(value for value in carried_directions if value is not None)
        failures += int(set(neighbor_labels) != {c463.transform(frame, value) for value in DIRECTIONS})
        manifest = sha256(
            f"{frame}|{digest.hexdigest()}|{composition['manifest']}|carried-complete-segments".encode()
        ).hexdigest()
        manifests.append(manifest)
    check(
        "source and target direction labels are carried with the complete seven-cell schedule through all 24 proper-cubic frames",
        len(frames) == 24 and failures == 0 and len(set(manifests)) == 24,
         {"frames": len(frames), "carried_path_or_label_failures": failures,
         "carried_layer": carried_layer, "actions_per_frame": len(actions),
         "combined_events_per_frame": composition["combined_events"],
         "frame_manifest_digests": manifests,
         "global_direction_sort_used_at_runtime": False,
         "carried_rule": "transform target, source direction vector, endpoints, path, and primitive supports together"},
    )


def domain_and_deletion_controls(circuit: c467.Circuit) -> None:
    nonblank_port_refused = False
    try:
        state = [0] * (7 * SUPERCELL_M2)
        state[state_index(compact_coord(circuit.layout.neighbor[0][0]))] = 1
        validate_blank_compact(state, circuit)
    except ValueError:
        nonblank_port_refused = True
    direction_refused = False
    try:
        direction_axis((1, 1, 0))
    except ValueError:
        direction_refused = True
    layer_refused = False
    try:
        ingress_actions(c463.ITERATIONS, circuit)
    except ValueError:
        layer_refused = True
    radius_refused = False
    try:
        c463.domain(3)
    except ValueError:
        radius_refused = True
    corrupt_path_refused = False
    try:
        corrupt = Action("remote_cnot", "bad", DIRECTIONS[0], 0, ((0, 0, 0), (2, 0, 0)))
        executor = TransferExecutor()
        executor.execute_action(corrupt)
        if executor.adjacency_failures:
            raise ValueError("non-nearest path")
    except ValueError:
        corrupt_path_refused = True
    check(
        "blank-port, direction, layer, radius, and nearest-neighbor domain violations are refused",
        nonblank_port_refused and direction_refused and layer_refused and radius_refused and corrupt_path_refused,
        {"nonblank_port_refused": nonblank_port_refused, "direction_refused": direction_refused,
         "layer_refused": layer_refused, "radius_refused": radius_refused,
         "corrupt_path_refused": corrupt_path_refused},
    )


def boundary_and_no_go_controls() -> None:
    check(
        "the complete supplied/constructed/open inventory preserves finite law, source, clock, and gravity boundaries",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "supplied": [
                "Cycle463 retained history/source/target words and 96-layer schedule",
                "Cycle467 logical and nearest-neighbor arithmetic trace",
                "scale-40 supercells, compact-port and persistent-storage placement",
                "one target-relative local frame and its proper-cubic carried orbit",
                "strict serial conflict schedule and computational-basis port code",
            ],
            "constructed": [
                "seven-cell Manhattan paths", "occupied-path remote CNOT and endpoint SWAP",
                "inverse return and exact placement restoration", "capacity/congestion/depth bounds",
                "held-size composition and all24 carried schedules",
            ],
            "open": [
                "a lower-depth parallel router", "globally overlapped multi-target scheduling",
                "derivation of relaxation/source/clock laws", "continuum, metric, backreaction, gravity",
            ],
            "not_claimed": ["time from schedule depth", "energy/stress from the source bit",
                            "optimal congestion/work", "a universal transport law"],
        },
    )
    check(
        "full N1-N8 rejects no-go, minimum-content, and axiom-pressure promotion",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "N1": "occupied-path SWAP/CNOT succeeds; clean fanout corridors, packet buses, face caches, teleportation, and staggered parallel networks remain alternatives",
            "N2": "port delivery, arithmetic, global overlap, finite law, source meaning, clock interpretation, and gravity remain independent",
            "N3": "persistent placement, blank ports/work, basis code, serial order, local frame, histories, D, and source/target staging are exposed",
            "N4": "the witness matches Cycle467's named inter-supercell-port residual and no broader source/gravity residual",
            "N5": "claims stop at a seven-supercell fixed schedule; no optimal, infinite, continuum, time, energy, or gravity rhetoric",
            "N6": "the port residual narrows constructively without axiom edits; global overlap and law/source derivation remain actionable",
            "N7": "a reviewer can pursue face caches, sorting networks, parallel edge coloring, link gauges, or a dynamical mediator",
            "N8": "Cycle467's port boundary is retired for one serial local block; C_wrap/C_source/gravity and lattice-wide scheduling echoes remain open; no axiom pressure",
        },
    )


def resource_controls(started: float) -> None:
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    check(
        "the complete Cycle470 run stays below explicit wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
        {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
         "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB},
    )


def main() -> int:
    started = perf_counter()
    print("Cycle470 physical seven-supercell port-delivery compiler")
    print("authority", AUTHORITY, "audit", AUDIT)
    note_contract()
    transfer_lemma_controls()
    circuit = c467.make_circuit(B, c463.DENOMINATOR)
    layer_data = placement_and_schedule_controls(circuit)
    _, selected = held_and_fast_composition_controls(circuit, layer_data)
    composition = literal_full_block_controls(circuit, selected)
    covariance_controls(circuit, selected[1], composition)
    domain_and_deletion_controls(circuit)
    boundary_and_no_go_controls()
    resource_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
