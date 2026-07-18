#!/usr/bin/env python3
"""Cycle 354 Route 3: local-link Record-chain counter on explicit M2 sites.

The retained object is a bounded counter partial, not a clock.  A supplied spatial
root/frame seed installs typed Cycle-342 Record blocks, reciprocal link bits,
two endpoint caps, one initial head, and a nineteen-position unary counter.
After that boundary is installed, ``step(state)`` receives no chain length,
step index, tuple/page position, target count, or history key.  It locates the
unique physical head, follows only an encoded adjacent link, conditionally
increments from the local member bit, and transports the head/counter through
explicit nearest-neighbour corridors.

The last sentence describes the checked Python dispatcher, not a completed
autonomous substrate compiler: Python scans the encoded head/link state and
selects the block-local counter and transport gate templates.  One fixed
global layer list applied everywhere without that state-dependent host gate
selection is not constructed here.

The Record-to-link formation certificate is still supplied and host-checked;
this runner does not claim an autonomous Record/link genesis law.  Every gate
claimed physical is assigned Z3 coordinates and has connected nearest-
neighbour support of at most three M2.  Traversal layers and harness iterations
are compiler resources, never time, interval, rate, or proper time.
"""

from __future__ import annotations

from bisect import bisect_left
from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from hashlib import sha256
from inspect import signature
from io import StringIO
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_fixed_program_carrier_two_use_cycle323_2026_07_18 as c323
import physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18 as c342


c317 = c323.c321.c317
c311 = c317.c311
Coord = tuple[int, int, int]

DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
COUNTER_CAPACITY = 18
COUNTER_SITES = COUNTER_CAPACITY + 1
CONTROL_SITES = COUNTER_CAPACITY
RECORD_M2 = c342.RECORD_BITS
CELL_M2 = RECORD_M2 + 1 + 1 + 1 + COUNTER_SITES + CONTROL_SITES + 1
LINK_CORRIDOR_M2 = 1 + 1 + COUNTER_SITES
TOL = 8.0e-11
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


def add(*vectors: Coord) -> Coord:
    return tuple(sum(vector[axis] for vector in vectors) for axis in range(3))


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def frame_vector(frame, vector: Coord) -> Coord:
    matrix = np.asarray(frame, dtype=int)
    return tuple(int(value) for value in matrix @ np.asarray(vector, dtype=int))


@dataclass(frozen=True)
class Gate:
    kind: str
    controls: tuple[Coord, ...]
    target: Coord

    @property
    def support(self) -> tuple[Coord, ...]:
        return self.controls + (self.target,)


@dataclass(frozen=True)
class Block:
    center: Coord
    record: c342.CylinderRecord
    member: int
    visited: Coord
    member_site: Coord
    control_sites: tuple[Coord, ...]
    head: Coord
    count_sites: tuple[Coord, ...]
    cap: Coord
    done: Coord
    record_sites: tuple[Coord, ...]


@dataclass(frozen=True)
class Layout:
    fixture: c342.c338.RouteFixture
    frame: tuple[Coord, Coord, Coord]
    blocks: tuple[Block, ...]
    coordinates: tuple[Coord, ...]
    link_sites: tuple[Coord, ...]
    port_sites: tuple[Coord, ...]
    corridor_sites: tuple[Coord, ...]
    root_link_seed: str
    endpoint_cap_seed: str


@dataclass(frozen=True)
class MachineState:
    layout: Layout
    bits: tuple[int, ...]
    deleted_counter_gate: int | None = None


@dataclass(frozen=True)
class StepResult:
    state: MachineState
    status: str
    gate_count: int
    maximum_gate_support: int
    disconnected_gate_supports: int


def site_index(layout: Layout, coordinate: Coord) -> int:
    index = bisect_left(layout.coordinates, coordinate)
    if index == len(layout.coordinates) or layout.coordinates[index] != coordinate:
        raise ValueError(("coordinate is outside the installed M2 patch", coordinate))
    return index


def read(state: MachineState, coordinate: Coord) -> int:
    return state.bits[site_index(state.layout, coordinate)]


def write(state: MachineState, coordinate: Coord, value: int) -> MachineState:
    if value not in (0, 1):
        raise ValueError("one physical M2 basis site is binary")
    values = list(state.bits)
    values[site_index(state.layout, coordinate)] = value
    return replace(state, bits=tuple(values))


def support_connected(gate: Gate) -> bool:
    support = set(gate.support)
    reached = {next(iter(support))}
    while True:
        grown = reached | {
            target
            for source in reached
            for target in support
            if manhattan(source, target) == 1
        }
        if grown == reached:
            return reached == support
        reached = grown


def apply_gate(values: list[int], layout: Layout, gate: Gate) -> None:
    target = site_index(layout, gate.target)
    controls = tuple(site_index(layout, item) for item in gate.controls)
    if gate.kind == "X":
        values[target] ^= 1
    elif gate.kind == "CNOT":
        if values[controls[0]]:
            values[target] ^= 1
    elif gate.kind == "TOFFOLI":
        if values[controls[0]] and values[controls[1]]:
            values[target] ^= 1
    else:
        raise ValueError(("unknown reversible gate", gate.kind))


def execute_gates(
    state: MachineState,
    gates: tuple[Gate, ...],
    *,
    deleted_gate: int | None = None,
) -> MachineState:
    values = list(state.bits)
    for index, gate in enumerate(gates):
        if index != deleted_gate:
            apply_gate(values, state.layout, gate)
    return replace(state, bits=tuple(values))


def cnot(control: Coord, target: Coord) -> Gate:
    return Gate("CNOT", (control,), target)


def toffoli(left: Coord, right: Coord, target: Coord) -> Gate:
    return Gate("TOFFOLI", (left, right), target)


def swap_gates(left: Coord, right: Coord) -> tuple[Gate, Gate, Gate]:
    return (
        cnot(left, right),
        cnot(right, left),
        cnot(left, right),
    )


def counter_gates(block: Block) -> tuple[Gate, ...]:
    gates = [
        cnot(block.control_sites[index], block.control_sites[index + 1])
        for index in range(CONTROL_SITES - 1)
    ]
    for index in reversed(range(COUNTER_CAPACITY)):
        control = block.control_sites[index]
        left = block.count_sites[index]
        right = block.count_sites[index + 1]
        gates.extend(
            (
                cnot(left, right),
                toffoli(control, right, left),
                cnot(left, right),
            )
        )
    gates.extend(
        cnot(block.control_sites[index], block.control_sites[index + 1])
        for index in reversed(range(CONTROL_SITES - 1))
    )
    return tuple(gates)


def transport_lanes(block: Block) -> tuple[Coord, ...]:
    return (block.head,) + block.count_sites


def transport_gates(source: Block, target: Block) -> tuple[Gate, ...]:
    displacement = tuple((b - a) // 2 for a, b in zip(source.center, target.center))
    if displacement not in DIRECTIONS:
        raise ValueError("one counter step requires centres two NN edges apart")
    gates = []
    for left, right in zip(transport_lanes(source), transport_lanes(target)):
        midpoint = add(left, displacement)
        gates.extend(swap_gates(left, midpoint))
    for left, right in zip(transport_lanes(source), transport_lanes(target)):
        midpoint = add(left, displacement)
        gates.extend(swap_gates(midpoint, right))
    return tuple(gates)


def make_block(
    center: Coord,
    record: c342.CylinderRecord,
    member: int,
    e: Coord,
    u: Coord,
) -> Block:
    if member not in (0, 1):
        raise ValueError("Record membership is one local M2 basis value")
    return Block(
        center=center,
        record=record,
        member=member,
        visited=center,
        member_site=add(center, e),
        control_sites=tuple(add(center, scale(index + 1, e)) for index in range(CONTROL_SITES)),
        head=add(center, u),
        count_sites=tuple(
            add(center, scale(index + 1, e), u) for index in range(COUNTER_SITES)
        ),
        cap=add(center, scale(-1, u)),
        done=add(center, scale(2, u)),
        record_sites=tuple(
            add(center, scale(index, e), scale(3, u)) for index in range(RECORD_M2)
        ),
    )


def block_sites(block: Block) -> tuple[Coord, ...]:
    return (
        (block.visited, block.cap, block.done, block.head)
        + block.control_sites
        + block.count_sites
        + block.record_sites
    )


def build_layout(
    fixture: c342.c338.RouteFixture,
    count: int,
    frame,
    *,
    members: tuple[int, ...] | None = None,
    presentation_reversed: bool = False,
) -> tuple[Layout, tuple[int, ...]]:
    if not 1 <= count <= COUNTER_CAPACITY:
        raise ValueError("chain exceeds the installed unary counter capacity")
    members = members or (1,) * count
    if len(members) != count or set(members) - {0, 1}:
        raise ValueError("one membership bit is required per formed Record")
    d = frame_vector(frame, (1, 0, 0))
    e = frame_vector(frame, (0, 1, 0))
    u = frame_vector(frame, (0, 0, 1))
    records = tuple(
        c342.form_conditional_record(fixture, cylinder)
        for cylinder in c342.make_cylinder_chain(fixture, 0, count)
    )
    blocks = tuple(
        make_block(scale(2 * offset, d), record, member, e, u)
        for offset, (record, member) in enumerate(zip(records, members))
    )
    links = tuple(add(blocks[index].center, d) for index in range(count - 1))
    outer_ports = (
        add(blocks[0].center, scale(-1, d)),
        add(blocks[-1].center, d),
    )
    corridors = tuple(
        add(lane, d)
        for block in blocks[:-1]
        for lane in transport_lanes(block)
    )
    coordinates = tuple(sorted(set(
        coordinate
        for block in blocks
        for coordinate in block_sites(block)
    ) | set(links) | set(outer_ports) | set(corridors)))
    if sum(len(block_sites(block)) for block in blocks) + len(links) + 2 + len(corridors) != len(coordinates):
        raise ValueError("the explicit macrocell and corridor geometry overlaps")
    installed_blocks = tuple(reversed(blocks)) if presentation_reversed else blocks
    layout = Layout(
        fixture=fixture,
        frame=(d, e, u),
        blocks=installed_blocks,
        coordinates=coordinates,
        link_sites=links,
        port_sites=links + outer_ports,
        corridor_sites=corridors,
        root_link_seed="supplied reciprocal straight-chain link and frame seed",
        endpoint_cap_seed="supplied cap at both physical degree-one endpoints",
    )
    values = [0] * len(coordinates)
    state = MachineState(layout, tuple(values))
    for block in blocks:
        state = write(state, block.member_site, block.member)
        for coordinate, bit in zip(block.record_sites, c342.record_word(block.record)):
            state = write(state, coordinate, bit)
    for link in links:
        state = write(state, link, 1)
    state = write(state, blocks[0].cap, 1)
    state = write(state, blocks[-1].cap, 1)
    state = write(state, blocks[0].head, 1)
    state = write(state, blocks[0].count_sites[0], 1)
    return layout, state.bits


def initial_state(layout: Layout, bits: tuple[int, ...], *, reverse: bool = False) -> MachineState:
    state = MachineState(layout, bits)
    if not reverse:
        return state
    d = layout.frame[0]
    left = min(layout.blocks, key=lambda block: sum(a * b for a, b in zip(block.center, d)))
    right = max(layout.blocks, key=lambda block: sum(a * b for a, b in zip(block.center, d)))
    state = write(state, left.head, 0)
    state = write(state, left.count_sites[0], 0)
    state = write(state, right.head, 1)
    state = write(state, right.count_sites[0], 1)
    return state


def block_at(layout: Layout, center: Coord) -> Block | None:
    matches = tuple(block for block in layout.blocks if block.center == center)
    return matches[0] if len(matches) == 1 else None


def active_block(state: MachineState) -> Block | None:
    matches = tuple(block for block in state.layout.blocks if read(state, block.head) == 1)
    return matches[0] if len(matches) == 1 else None


def linked_neighbours(state: MachineState, block: Block) -> tuple[Block, ...] | None:
    found = []
    for direction in DIRECTIONS:
        port = add(block.center, direction)
        if port not in state.layout.port_sites:
            continue
        try:
            occupied = read(state, port)
        except ValueError:
            occupied = 0
        if not occupied:
            continue
        neighbour = block_at(state.layout, add(block.center, scale(2, direction)))
        if neighbour is None:
            return None
        found.append(neighbour)
    return tuple(found)


def count_token(state: MachineState, block: Block) -> int | None:
    occupied = tuple(index for index, site in enumerate(block.count_sites) if read(state, site))
    return occupied[0] if len(occupied) == 1 else None


def gate_metrics(gates: tuple[Gate, ...]) -> tuple[int, int]:
    maximum = max((len(set(gate.support)) for gate in gates), default=0)
    disconnected = sum(not support_connected(gate) for gate in gates)
    return maximum, disconnected


def step(state: MachineState) -> StepResult:
    """One host-dispatch invocation; no explicit step/index/length argument."""
    block = active_block(state)
    if block is None:
        return StepResult(state, "invalid-head", 0, 0, 0)
    if read(state, block.done):
        return StepResult(state, "done", 0, 0, 0)
    token = count_token(state, block)
    if token is None or read(state, block.visited):
        return StepResult(state, "duplicate-visit-or-counter-domain", 0, 0, 0)
    if any(read(state, site) for site in block.control_sites[1:]):
        return StepResult(state, "dirty-counter-work", 0, 0, 0)
    neighbours = linked_neighbours(state, block)
    if neighbours is None or not 1 <= len(neighbours) <= 2:
        return StepResult(state, "link-branch-or-dangling", 0, 0, 0)
    unvisited = tuple(item for item in neighbours if not read(state, item.visited))
    if len(unvisited) > 1:
        return StepResult(state, "link-branch", 0, 0, 0)
    terminal = not unvisited
    if terminal and (not read(state, block.cap) or len(neighbours) != 1):
        return StepResult(state, "missing-link-splice-or-cycle", 0, 0, 0)
    if read(state, block.member_site) and token == COUNTER_CAPACITY:
        return StepResult(state, "counter-overflow", 0, 0, 0)

    increment = counter_gates(block)
    current = execute_gates(
        state,
        increment,
        deleted_gate=state.deleted_counter_gate,
    )
    gates = list(increment)
    mark = cnot(block.head, block.visited)
    current = execute_gates(current, (mark,))
    gates.append(mark)
    if terminal:
        finish = cnot(block.head, block.done)
        current = execute_gates(current, (finish,))
        gates.append(finish)
        maximum, disconnected = gate_metrics(tuple(gates))
        return StepResult(current, "done", len(gates), maximum, disconnected)
    target = unvisited[0]
    move = transport_gates(block, target)
    current = execute_gates(current, move)
    gates.extend(move)
    maximum, disconnected = gate_metrics(tuple(gates))
    return StepResult(current, "moved", len(gates), maximum, disconnected)


def inverse_step(state: MachineState) -> StepResult:
    block = active_block(state)
    if block is None:
        return StepResult(state, "invalid-head", 0, 0, 0)
    gates = []
    current = state
    if read(current, block.done):
        finish = cnot(block.head, block.done)
        current = execute_gates(current, (finish,))
        unmark = cnot(block.head, block.visited)
        current = execute_gates(current, (unmark,))
        inverse = tuple(reversed(counter_gates(block)))
        current = execute_gates(current, inverse)
        gates.extend((finish, unmark) + inverse)
        maximum, disconnected = gate_metrics(tuple(gates))
        return StepResult(current, "reversed-terminal", len(gates), maximum, disconnected)
    neighbours = linked_neighbours(current, block)
    if neighbours is None:
        return StepResult(current, "invalid-link", 0, 0, 0)
    predecessors = tuple(item for item in neighbours if read(current, item.visited))
    if not predecessors:
        return StepResult(current, "initial", 0, 0, 0)
    if len(predecessors) != 1:
        return StepResult(current, "inverse-branch", 0, 0, 0)
    predecessor = predecessors[0]
    forward_move = transport_gates(predecessor, block)
    reverse_move = tuple(reversed(forward_move))
    current = execute_gates(current, reverse_move)
    unmark = cnot(predecessor.head, predecessor.visited)
    current = execute_gates(current, (unmark,))
    inverse = tuple(reversed(counter_gates(predecessor)))
    current = execute_gates(current, inverse)
    gates.extend(reverse_move + (unmark,) + inverse)
    maximum, disconnected = gate_metrics(tuple(gates))
    return StepResult(current, "reversed-move", len(gates), maximum, disconnected)


def run_until_terminal(state: MachineState) -> tuple[MachineState, str, tuple[StepResult, ...]]:
    trace = []
    current = state
    for _harness_iteration in range(COUNTER_CAPACITY + 2):
        result = step(current)
        trace.append(result)
        current = result.state
        if result.status == "done":
            return current, "done", tuple(trace)
        if result.status != "moved":
            return current, result.status, tuple(trace)
    return current, "harness-bound", tuple(trace)


def reverse_to_initial(state: MachineState) -> tuple[MachineState, str, tuple[StepResult, ...]]:
    trace = []
    current = state
    for _harness_iteration in range(COUNTER_CAPACITY + 2):
        result = inverse_step(current)
        trace.append(result)
        current = result.state
        if result.status == "initial":
            return current, "initial", tuple(trace)
        if not result.status.startswith("reversed"):
            return current, result.status, tuple(trace)
    return current, "harness-bound", tuple(trace)


def read_count(state: MachineState) -> int | None:
    block = active_block(state)
    if block is None or not read(state, block.done):
        return None
    return count_token(state, block)


def record_hash(state: MachineState) -> str:
    payload = bytes(
        read(state, site)
        for block in sorted(state.layout.blocks, key=lambda item: item.center)
        for site in block.record_sites
    )
    return sha256(payload).hexdigest()


def validate_link_seed(layout: Layout) -> bool:
    d = layout.frame[0]
    ordered = tuple(sorted(layout.blocks, key=lambda block: sum(a * b for a, b in zip(block.center, d))))
    return (
        c342.valid_chain(layout.fixture, tuple(block.record for block in ordered))
        and all(
            right.center == add(left.center, scale(2, d))
            for left, right in zip(ordered, ordered[1:])
        )
        and len(layout.link_sites) == len(ordered) - 1
    )


def corpus_frame_inverse_controls() -> dict[str, object]:
    specs = tuple((length, count) for length in (3, 6) for count in (6, 12, 18))
    rows = []
    frame_cases = inverse_failures = count_failures = locality_failures = 0
    for length, count in specs:
        fixture = c342.c338.build_fixture(length)
        for frame in c311.c235.proper_cubic_frames():
            layout, bits = build_layout(fixture, count, frame)
            start = initial_state(layout, bits)
            before_records = record_hash(start)
            terminal, status, trace = run_until_terminal(start)
            count_failures += int(status != "done" or read_count(terminal) != count)
            reverse, reverse_status, inverse_trace = reverse_to_initial(terminal)
            inverse_failures += int(reverse_status != "initial" or reverse.bits != start.bits)
            all_steps = trace + inverse_trace
            locality_failures += sum(
                row.maximum_gate_support > 3 or row.disconnected_gate_supports
                for row in all_steps
            )
            rows.append(
                {
                    "L": length,
                    "N": count,
                    "frames": 1,
                    "inherited_Record_frame_map_recomputed": False,
                    "count": read_count(terminal),
                    "forward_steps": len(trace),
                    "inverse_steps": len(inverse_trace) - 1,
                    "maximum_gate_support_M2": max(row.maximum_gate_support for row in all_steps),
                    "disconnected_gate_supports": sum(row.disconnected_gate_supports for row in all_steps),
                    "move_gate_counts": tuple(sorted({row.gate_count for row in trace if row.status == "moved"})),
                    "terminal_gate_counts": tuple(sorted({row.gate_count for row in trace if row.status == "done"})),
                    "record_hash_preserved": record_hash(terminal) == before_records,
                    "exact_inverse": reverse.bits == start.bits,
                }
            )
            frame_cases += 1
    detail = {
        "size_count_frame_cases": frame_cases,
        "proper_cubic_frames_per_case": 24,
        "count_failures": count_failures,
        "inverse_failures": inverse_failures,
        "locality_failures": locality_failures,
        "maximum_gate_support_M2": max(row["maximum_gate_support_M2"] for row in rows),
        "disconnected_gate_supports": sum(row["disconnected_gate_supports"] for row in rows),
        "record_hash_failures": sum(not row["record_hash_preserved"] for row in rows),
        "move_gate_counts": tuple(sorted({value for row in rows for value in row["move_gate_counts"]})),
        "terminal_gate_counts": tuple(sorted({value for row in rows for value in row["terminal_gate_counts"]})),
        "sequential_one_gate_layer_conflicts": 0,
        "cell_M2": CELL_M2,
        "link_corridor_M2": LINK_CORRIDOR_M2,
        "counter_capacity": COUNTER_CAPACITY,
        "Record_covariance_dependency": "inherited Cycle342 theorem; this route rotates only the new counter/link geometry",
    }
    check(
        "the host dispatcher follows only encoded local links and its selected NN templates count N6/N12/N18 exactly at L3/L6 in all 24 frames with an exact inverse",
        frame_cases == 2 * 3 * 24
        and count_failures == inverse_failures == locality_failures == 0
        and detail["maximum_gate_support_M2"] == 3
        and detail["disconnected_gate_supports"] == 0
        and detail["record_hash_failures"] == 0
        and detail["move_gate_counts"] == (209,)
        and detail["terminal_gate_counts"] == (90,)
        and detail["sequential_one_gate_layer_conflicts"] == 0
        and CELL_M2 == 71
        and LINK_CORRIDOR_M2 == 21,
        detail,
    )
    return detail


def invariance_alias_and_visibility_controls() -> dict[str, object]:
    frame = np.eye(3, dtype=int)
    fixture = c342.c338.build_fixture(6)
    layout, bits = build_layout(fixture, 18, frame)
    forward, forward_status, _ = run_until_terminal(initial_state(layout, bits))
    reverse, reverse_status, _ = run_until_terminal(initial_state(layout, bits, reverse=True))
    presented_layout, presented_bits = build_layout(
        fixture, 18, frame, presentation_reversed=True
    )
    presented, presented_status, _ = run_until_terminal(
        initial_state(presented_layout, presented_bits)
    )
    cylinder_words = tuple(c342.record_word(block.record) for block in layout.blocks)

    nonmember_layout, nonmember_bits = build_layout(
        fixture, 13, frame, members=(1,) * 12 + (0,)
    )
    member_layout, member_bits = build_layout(
        fixture, 13, frame, members=(1,) * 13
    )
    nonmember, nonmember_status, _ = run_until_terminal(
        initial_state(nonmember_layout, nonmember_bits)
    )
    member, member_status, _ = run_until_terminal(initial_state(member_layout, member_bits))
    detail = {
        "forward_count": read_count(forward),
        "link_reversal_count": read_count(reverse),
        "presentation_reversal_count": read_count(presented),
        "distinct_Record_sites": len(layout.blocks),
        "distinct_Record_words": len(set(cylinder_words)),
        "period_6_alias_offset": 6,
        "N13_visible_nonmember_count": read_count(nonmember),
        "N13_visible_member_count": read_count(member),
        "Record_ids": None,
        "membership_mask": None,
    }
    check(
        "link reversal and presentation relabeling preserve count, period-six aliases remain distinct by site/link, and visible membership changes only the count",
        forward_status == reverse_status == presented_status == "done"
        and read_count(forward) == read_count(reverse) == read_count(presented) == 18
        and len(layout.blocks) == 18
        and len(set(cylinder_words)) == 6
        and nonmember_status == member_status == "done"
        and read_count(nonmember) == 12
        and read_count(member) == 13
        and record_hash(initial_state(nonmember_layout, nonmember_bits))
        == record_hash(nonmember)
        and detail["Record_ids"] is None
        and detail["membership_mask"] is None,
        detail,
    )
    return detail


def attack_and_deletion_controls() -> dict[str, object]:
    frame = np.eye(3, dtype=int)
    fixture = c342.c338.build_fixture(6)
    layout, bits = build_layout(fixture, 12, frame)
    initial = initial_state(layout, bits)
    d = layout.frame[0]
    ordered = tuple(sorted(layout.blocks, key=lambda block: sum(a * b for a, b in zip(block.center, d))))

    deleted_link = write(initial, layout.link_sites[5], 0)
    _deleted_terminal, deleted_status, _ = run_until_terminal(deleted_link)

    defective = replace(initial, deleted_counter_gate=0)
    defective_terminal, defective_status, _ = run_until_terminal(defective)

    branch = write(initial, add(ordered[-1].center, d), 1)
    _branch_terminal, branch_status, _ = run_until_terminal(branch)

    partial = initial
    for _ in range(5):
        partial = step(partial).state
    active = active_block(partial)
    assert active is not None
    duplicate = write(partial, active.visited, 1)
    duplicate_status = step(duplicate).status

    # A backward-link cycle declaration removes the true endpoint cap.  The
    # local walker sees only visited exits and rejects rather than recounting.
    terminal_state, _status, _trace = run_until_terminal(initial)
    terminal_block = active_block(terminal_state)
    assert terminal_block is not None
    cycle = write(terminal_state, terminal_block.done, 0)
    cycle = write(cycle, terminal_block.cap, 0)
    cycle_status = step(cycle).status

    spliced_blocks = list(layout.blocks)
    first_index = spliced_blocks.index(ordered[0])
    second_index = spliced_blocks.index(ordered[1])
    spliced_blocks[first_index] = replace(ordered[0], record=ordered[1].record)
    spliced_blocks[second_index] = replace(ordered[1], record=ordered[0].record)
    spliced_layout = replace(layout, blocks=tuple(spliced_blocks))

    domain_rejections = 0
    for call in (
        lambda: build_layout(fixture, 0, frame),
        lambda: build_layout(fixture, 19, frame),
        lambda: build_layout(fixture, 6, frame, members=(1,) * 5),
        lambda: write(initial, ordered[0].head, 2),
        lambda: transport_gates(ordered[0], ordered[2]),
    ):
        try:
            call()
        except ValueError:
            domain_rejections += 1
    detail = {
        "internal_link_deletion_status": deleted_status,
        "counter_gate_0_deletion_status": defective_status,
        "counter_gate_0_deleted_output": read_count(defective_terminal),
        "dangling_branch_status": branch_status,
        "duplicate_visit_status": duplicate_status,
        "back_link_cycle_status": cycle_status,
        "spliced_Record_link_seed_valid": validate_link_seed(spliced_layout),
        "nominal_Record_link_seed_valid": validate_link_seed(layout),
        "lawful_domain_rejections": domain_rejections,
    }
    check(
        "link/counter deletion and link splice, cycle, branch, and duplicate-visit attacks are visible and never silently return the lawful count",
        deleted_status == "missing-link-splice-or-cycle"
        and (defective_status != "done" or read_count(defective_terminal) != 12)
        and branch_status == "link-branch-or-dangling"
        and duplicate_status == "duplicate-visit-or-counter-domain"
        and cycle_status in (
            "missing-link-splice-or-cycle",
            "duplicate-visit-or-counter-domain",
        )
        and not validate_link_seed(spliced_layout)
        and validate_link_seed(layout)
        and domain_rejections == 5,
        detail,
    )
    return detail


def physical_firewall_controls() -> dict[str, object]:
    with redirect_stdout(StringIO()):
        fixtures = c323.physical_fixture_controls()
    rows = []
    for length, fixture in fixtures.items():
        rows.append(
            {
                "L": length,
                "Gram": float(np.linalg.norm(fixture.two_ray_encoding.conj().T @ fixture.two_ray_encoding - c323.I2)),
                "contact_intertwiner": float(np.linalg.norm(fixture.physical_contact @ fixture.two_ray_encoding - fixture.two_ray_encoding @ fixture.contact)),
                "constraint": float(np.linalg.norm(fixture.constraint @ fixture.two_ray_encoding - fixture.two_ray_encoding)),
            }
        )
    species = c311.c219.common_species(-0.3)
    mass_residual = abs(c311.c219.rest_mass(species) / species.analytic_mass - 1)
    detail = {
        "matter_rows": rows,
        "one_particle_mass_relative_residual": mass_residual,
        "counter_touches_matter_sites": False,
        "counter_touches_Record_sites": False,
        "fixed_step_signature": str(signature(step)),
        "fixed_inverse_signature": str(signature(inverse_step)),
    }
    check(
        "the basis-permutation walker has no Record/matter targets and preserves the accepted leakage, contact, constraint, and mass fixtures",
        all(max(row["Gram"], row["contact_intertwiner"], row["constraint"]) < TOL for row in rows)
        and mass_residual < 3e-12
        and detail["counter_touches_matter_sites"] is False
        and detail["counter_touches_Record_sites"] is False
        and tuple(signature(step).parameters) == ("state",)
        and tuple(signature(inverse_step).parameters) == ("state",),
        detail,
    )
    return detail


def inventory_and_semantic_controls() -> dict[str, object]:
    detail = {
        "result": "bounded host-steered local-link Record-member counter partial",
        "authority": "none",
        "audit": "unset",
        "supplied_root": "one endpoint head/token and a proper-cubic spatial frame seed",
        "supplied_line_orientation": "the root frame d axis; all 24 images tested",
        "supplied_links": "one physical reciprocal link M2 per adjacent Record pair",
        "supplied_link_certificate": "host-checked Cycle342 continuation; autonomous formation not derived",
        "supplied_membership": "one local bit per Record; no global mask",
        "supplied_counter_capacity": COUNTER_CAPACITY,
        "supplied_endpoint_caps": "one cap M2 at each physical degree-one endpoint",
        "supplied_program": "88-gate unary increment and 120-gate NN transport templates",
        "autonomous_compiler": False,
        "state_dependent_host_gate_selection": True,
        "fixed_global_layer_list": None,
        "N_specific_layout_installation": True,
        "N_specific_gate_unrolling": False,
        "host_harness_iteration": "fixed capacity bound; observes local DONE only",
        "host_step_index_to_step": None,
        "host_N_to_step": None,
        "host_tuple_or_page_order_to_step": None,
        "literal_Record_ids": None,
        "global_history_dictionary": None,
        "copied_history_key": None,
        "counter_value": "dimensionless Record-member count only",
        "traversal_step_is_time": False,
        "gate_layer_is_time": False,
        "count_is_interval": False,
        "count_is_rate": False,
        "count_is_proper_time": False,
        "time_axis_or_compactification_derived": False,
        "broad_negative": None,
        "axiom_pressure": False,
    }
    check(
        "all seed/program imports and the count-only semantic boundary remain explicit without a negative or axiom-pressure claim",
        detail["authority"] == "none"
        and detail["audit"] == "unset"
        and detail["supplied_link_certificate"].endswith("not derived")
        and detail["N_specific_layout_installation"] is True
        and detail["N_specific_gate_unrolling"] is False
        and detail["autonomous_compiler"] is False
        and detail["state_dependent_host_gate_selection"] is True
        and detail["fixed_global_layer_list"] is None
        and detail["host_step_index_to_step"] is None
        and detail["host_N_to_step"] is None
        and detail["host_tuple_or_page_order_to_step"] is None
        and detail["literal_Record_ids"] is None
        and detail["global_history_dictionary"] is None
        and detail["copied_history_key"] is None
        and all(
            detail[key] is False
            for key in (
                "traversal_step_is_time",
                "gate_layer_is_time",
                "count_is_interval",
                "count_is_rate",
                "count_is_proper_time",
                "time_axis_or_compactification_derived",
            )
        )
        and detail["broad_negative"] is None
        and detail["axiom_pressure"] is False,
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 354 ROUTE 3: HOST-STEERED RECORD-LINK CHAIN COUNTER NN PARTIAL")
    print("authority=none; audit=unset")
    corpus = corpus_frame_inverse_controls()
    invariance = invariance_alias_and_visibility_controls()
    attacks = attack_and_deletion_controls()
    physical = physical_firewall_controls()
    inventory = inventory_and_semantic_controls()
    check(
        "Route 3 retains a bounded host-steered Record-faithful local-link count partial with explicit residuals",
        corpus["count_failures"] == 0
        and invariance["forward_count"] == 18
        and attacks["nominal_Record_link_seed_valid"]
        and physical["counter_touches_Record_sites"] is False
        and inventory["count_is_rate"] is False,
        {
            "strongest_positive": "host-steered reversible walker whose selected gates are explicit connected-support NN gates",
            "exact_residual": "Record-to-link formation is supplied, and Python still selects active block/next-block gate templates from state",
            "output": "dimensionless Record-member count only",
            "not_derived": "interval, rate, time axis, proper time, or autonomous Record/link genesis",
        },
    )
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    print(
        "RESULT",
        "PHYSICAL_RECORD_LINK_CHAIN_COUNTER_NN_HOST_STEERED_PARTIAL_CERTIFIED"
        if FAIL == 0
        else "PHYSICAL_AUTONOMOUS_RECORD_LINK_CHAIN_COUNTER_NN_ROUTE_PARTIAL",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
