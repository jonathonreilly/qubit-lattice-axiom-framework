#!/usr/bin/env python3
"""Cycle 360: fixed-global autonomous local-link Record-member counter.

This runner replaces Cycle 354's Python active-head scan, neighbour scan, and
state-selected gate templates with one precompiled global layer list for each
installed bounded patch.  Every layer is applied everywhere on every call to
``step(state)``.  Two physical orientation rails remove host neighbour choice:
the B rail moves toward increasing spatial coordinate and the A rail toward
decreasing spatial coordinate.  The supplied root/frame seed chooses the one
initially occupied rail, while both rail circuits always execute.  One
direction-selector M2 per block and a two-M2 nearest-neighbour equality wire
per bond make that choice and the opposite visited guard locally checkable.
The fixed step never consults the selector: a uniform selector/head flip is
the lawful reverse sector.

Head, member, visited, cap/root, reciprocal-link, and carried unary-count M2
sites are literal controls or targets of the fixed reversible gates.  Link
masters fan out locally along each bond and control every packet-lane Fredkin;
local head/member/not-visited controls condition the dimensionless increment.
Auxiliaries uncompute at every rule boundary.  Record-to-link formation,
root/frame, duplicated orientation membership, endpoint caps, finite capacity,
and the observation harness remain supplied.

The output is a dimensionless Record-member count only.  Spatial traversal and
circuit layering are not a clock, evolution axis, interval, rate, or proper
time.  No negative or axiom-pressure claim is made.  Authority is none and
audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
from inspect import getsource, signature
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_autonomous_record_dual_front_rendezvous_nn_route_cycle353_2026_07_18 as c353
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317
import physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18 as c342


Coord = tuple[int, int, int]
Gate = c353.Gate
Layer = c353.Layer
LENGTHS = (3, 6)
SIZES = (6, 12, 18)
HELD_LENGTH = 6
HELD_SIZE = 18
COUNTER_CAPACITY = 18
COUNT_LANES = tuple(range(COUNTER_CAPACITY + 1))
HEAD_Y = 0
COUNT_Y = tuple(2 + value for value in COUNT_LANES)
PACKET_YS = (HEAD_Y,) + COUNT_Y
ORIENTATIONS = ("A", "B")
PACKET_ROLES = ("A", "M", "B")
AUTHORITY = "none"
AUDIT = "unset"
TOL = 1.2e-10
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


@dataclass(frozen=True)
class Site:
    coord: Coord
    cell: int | None
    role: str
    lane: int | None


@dataclass(frozen=True)
class Block:
    index: int
    record: c342.CylinderRecord
    member: int
    selector_site: int
    record_sites: tuple[int, ...]
    packet: dict[str, tuple[int, ...]]
    member_sites: dict[str, int]
    visited_sites: dict[str, int]
    temp_sites: dict[str, int]
    activation_sites: dict[str, tuple[int, ...]]
    cap_sites: dict[str, int]
    root_sites: dict[str, int]
    terminal_sites: dict[str, int]
    done_sites: dict[str, int]


@dataclass(frozen=True)
class Bond:
    index: int
    bus: tuple[int, ...]
    selector_wire: tuple[int, int]


@dataclass(frozen=True)
class Layout:
    fixture: c342.c338.RouteFixture
    count: int
    sites: tuple[Site, ...]
    blocks: tuple[Block, ...]
    bonds: tuple[Bond, ...]
    layers: tuple[Layer, ...]
    frame: tuple[int, ...]
    presentation_reversed: bool


@dataclass(frozen=True)
class MachineState:
    layout: Layout
    bits: tuple[int, ...]


def make_gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    arity = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in arity or len(sites) != arity[kind] or len(set(sites)) != len(sites):
        raise ValueError((kind, sites))
    return Gate(kind, sites, label)


def fredkin_layers(
    prefix: str,
    triples: tuple[tuple[int, int, int, str], ...],
) -> tuple[Layer, Layer, Layer]:
    return (
        Layer(
            prefix + "-a",
            tuple(make_gate("CNOT", (right, left), label + ":a") for control, left, right, label in triples),
        ),
        Layer(
            prefix + "-b",
            tuple(make_gate("TOFFOLI", (control, left, right), label + ":b") for control, left, right, label in triples),
        ),
        Layer(
            prefix + "-c",
            tuple(make_gate("CNOT", (right, left), label + ":c") for control, left, right, label in triples),
        ),
    )


def swap_layers(
    prefix: str,
    pairs: tuple[tuple[int, int, str], ...],
) -> tuple[Layer, Layer, Layer]:
    return (
        Layer(prefix + "-a", tuple(make_gate("CNOT", (left, right), label + ":a") for left, right, label in pairs)),
        Layer(prefix + "-b", tuple(make_gate("CNOT", (right, left), label + ":b") for left, right, label in pairs)),
        Layer(prefix + "-c", tuple(make_gate("CNOT", (left, right), label + ":c") for left, right, label in pairs)),
    )


def base_coord(cell: int, role: str, lane: int | None) -> Coord:
    side_x = {"A": 3 * cell, "M": 3 * cell + 1, "B": 3 * cell + 2}
    if role in PACKET_ROLES and lane in PACKET_YS:
        return (side_x[role], int(lane), 0)
    if role.startswith("record") and lane is not None:
        return (3 * cell + 1, lane, 3)
    if role.startswith("link") and lane is not None:
        return (3 * cell + 2, lane, -1)
    if role == "selector" and lane is None:
        return (3 * cell + 1, -4, 0)
    if role == "selector-wire" and lane in (0, 1):
        return (3 * cell + 2 + lane, -4, 0)
    if ":" not in role:
        raise ValueError((cell, role, lane))
    orientation, name = role.split(":", 1)
    if orientation not in ORIENTATIONS:
        raise ValueError((cell, role, lane))
    x = side_x[orientation]
    fixed = {
        "visited": (0, 1),
        "member": (1, 0),
        "temp": (1, 1),
        "cap": (-1, 0),
        "root": (-2, 1),
        "terminal": (-1, 1),
        "done": (-2, 0),
    }
    if name in fixed and lane is None:
        y, z = fixed[name]
        return (x, y, z)
    if name == "activation" and lane is not None and 0 <= lane < COUNTER_CAPACITY:
        return (x, 2 + lane, 1)
    raise ValueError((cell, role, lane))


def build_layout(
    fixture: c342.c338.RouteFixture,
    count: int,
    frame: np.ndarray,
    *,
    members: tuple[int, ...] | None = None,
    presentation_reversed: bool = False,
) -> tuple[Layout, tuple[int, ...]]:
    if not isinstance(count, int) or isinstance(count, bool) or not 1 <= count <= COUNTER_CAPACITY:
        raise ValueError("Record chain must fit the installed unary capacity")
    members = (1,) * count if members is None else members
    if len(members) != count or any(value not in (0, 1) for value in members):
        raise ValueError("one binary member seed is required per Record")
    matrix = np.asarray(frame, dtype=int)
    if matrix.shape != (3, 3) or round(float(np.linalg.det(matrix))) != 1:
        raise ValueError("layout needs one proper-cubic spatial frame")

    raw_sites: list[tuple[Coord, int | None, str, int | None]] = []
    keys: dict[tuple[object, ...], int] = {}

    def install(key: tuple[object, ...], cell: int | None, role: str, lane: int | None, raw: Coord) -> int:
        if key in keys:
            raise RuntimeError(("duplicate site key", key))
        index = len(raw_sites)
        keys[key] = index
        raw_sites.append((raw, cell, role, lane))
        return index

    records = tuple(
        c342.form_conditional_record(fixture, cylinder)
        for cylinder in c342.make_cylinder_chain(fixture, 0, count)
    )
    blocks: list[Block] = []
    for cell, (record, member) in enumerate(zip(records, members)):
        selector_site = install(
            ("selector", cell),
            cell,
            "selector",
            None,
            base_coord(cell, "selector", None),
        )
        packet = {}
        for role in PACKET_ROLES:
            packet[role] = tuple(
                install(("packet", cell, role, lane), cell, role, lane, base_coord(cell, role, lane))
                for lane in PACKET_YS
            )
        member_sites = {}
        visited_sites = {}
        temp_sites = {}
        activation_sites = {}
        cap_sites = {}
        root_sites = {}
        terminal_sites = {}
        done_sites = {}
        for orientation in ORIENTATIONS:
            for name, target in (
                ("member", member_sites),
                ("visited", visited_sites),
                ("temp", temp_sites),
                ("cap", cap_sites),
                ("root", root_sites),
                ("terminal", terminal_sites),
                ("done", done_sites),
            ):
                role = f"{orientation}:{name}"
                target[orientation] = install(
                    ("aux", cell, orientation, name),
                    cell,
                    role,
                    None,
                    base_coord(cell, role, None),
                )
            activation_sites[orientation] = tuple(
                install(
                    ("activation", cell, orientation, lane),
                    cell,
                    f"{orientation}:activation",
                    lane,
                    base_coord(cell, f"{orientation}:activation", lane),
                )
                for lane in range(COUNTER_CAPACITY)
            )
        record_sites = tuple(
            install(("record", cell, lane), cell, "record", lane, base_coord(cell, "record", lane))
            for lane in range(c342.RECORD_BITS)
        )
        blocks.append(
            Block(
                cell,
                record,
                member,
                selector_site,
                record_sites,
                packet,
                member_sites,
                visited_sites,
                temp_sites,
                activation_sites,
                cap_sites,
                root_sites,
                terminal_sites,
                done_sites,
            )
        )

    bonds = []
    for bond in range(count - 1):
        bus = tuple(
            install(("link", bond, lane), None, "link", lane, base_coord(bond, "link", lane))
            for lane in range(max(PACKET_YS) + 1)
        )
        selector_wire = tuple(
            install(
                ("selector-wire", bond, lane),
                None,
                "selector-wire",
                lane,
                base_coord(bond, "selector-wire", lane),
            )
            for lane in (0, 1)
        )
        bonds.append(Bond(bond, bus, selector_wire))

    transformed_sites = tuple(
        Site(c353.rotated(raw, matrix), cell, role, lane)
        for raw, cell, role, lane in raw_sites
    )
    if len({site.coord for site in transformed_sites}) != len(transformed_sites):
        raise ValueError("the explicit fixed-global M2 geometry overlaps")

    layers: list[Layer] = []
    direction_cells = tuple(
        (block, orientation)
        for block in blocks
        for orientation in ORIENTATIONS
    )

    def local_gate_layer(name: str, maker) -> None:
        layers.append(
            Layer(name, tuple(maker(block, orientation) for block, orientation in direction_cells))
        )

    local_gate_layer(
        "activation-visited-invert",
        lambda block, orientation: make_gate("X", (block.visited_sites[orientation],), f"activation-visited-invert:{orientation}:i{block.index}"),
    )
    local_gate_layer(
        "activation-temp-compute",
        lambda block, orientation: make_gate(
            "TOFFOLI",
            (block.packet[orientation][0], block.member_sites[orientation], block.temp_sites[orientation]),
            f"activation-temp:{orientation}:i{block.index}",
        ),
    )
    local_gate_layer(
        "activation-seed-compute",
        lambda block, orientation: make_gate(
            "TOFFOLI",
            (block.temp_sites[orientation], block.visited_sites[orientation], block.activation_sites[orientation][0]),
            f"activation-seed:{orientation}:i{block.index}",
        ),
    )
    local_gate_layer(
        "activation-temp-uncompute",
        lambda block, orientation: make_gate(
            "TOFFOLI",
            (block.packet[orientation][0], block.member_sites[orientation], block.temp_sites[orientation]),
            f"activation-temp:{orientation}:i{block.index}",
        ),
    )
    local_gate_layer(
        "activation-visited-restore",
        lambda block, orientation: make_gate("X", (block.visited_sites[orientation],), f"activation-visited-restore:{orientation}:i{block.index}"),
    )
    for lane in range(COUNTER_CAPACITY - 1):
        local_gate_layer(
            f"activation-fanout:{lane}",
            lambda block, orientation, lane=lane: make_gate(
                "CNOT",
                (block.activation_sites[orientation][lane], block.activation_sites[orientation][lane + 1]),
                f"activation-fanout:{orientation}:i{block.index}:k{lane}",
            ),
        )
    for counter in reversed(range(COUNTER_CAPACITY)):
        triples = tuple(
            (
                block.activation_sites[orientation][counter],
                block.packet[orientation][counter + 1],
                block.packet[orientation][counter + 2],
                f"count-fredkin:{orientation}:i{block.index}:k{counter}",
            )
            for block, orientation in direction_cells
        )
        layers.extend(fredkin_layers(f"count-fredkin:{counter}", triples))
    for lane in reversed(range(COUNTER_CAPACITY - 1)):
        local_gate_layer(
            f"activation-unfanout:{lane}",
            lambda block, orientation, lane=lane: make_gate(
                "CNOT",
                (block.activation_sites[orientation][lane], block.activation_sites[orientation][lane + 1]),
                f"activation-unfanout:{orientation}:i{block.index}:k{lane}",
            ),
        )
    local_gate_layer(
        "activation-clean-visited-invert",
        lambda block, orientation: make_gate("X", (block.visited_sites[orientation],), f"activation-clean-visited-invert:{orientation}:i{block.index}"),
    )
    local_gate_layer(
        "activation-clean-temp-compute",
        lambda block, orientation: make_gate(
            "TOFFOLI",
            (block.packet[orientation][0], block.member_sites[orientation], block.temp_sites[orientation]),
            f"activation-clean-temp:{orientation}:i{block.index}",
        ),
    )
    local_gate_layer(
        "activation-seed-uncompute",
        lambda block, orientation: make_gate(
            "TOFFOLI",
            (block.temp_sites[orientation], block.visited_sites[orientation], block.activation_sites[orientation][0]),
            f"activation-seed:{orientation}:i{block.index}",
        ),
    )
    local_gate_layer(
        "activation-clean-temp-uncompute",
        lambda block, orientation: make_gate(
            "TOFFOLI",
            (block.packet[orientation][0], block.member_sites[orientation], block.temp_sites[orientation]),
            f"activation-clean-temp:{orientation}:i{block.index}",
        ),
    )
    local_gate_layer(
        "activation-clean-visited-restore",
        lambda block, orientation: make_gate("X", (block.visited_sites[orientation],), f"activation-clean-visited-restore:{orientation}:i{block.index}"),
    )

    local_gate_layer(
        "visited-mark",
        lambda block, orientation: make_gate(
            "CNOT",
            (block.packet[orientation][0], block.visited_sites[orientation]),
            f"visited-mark:{orientation}:i{block.index}",
        ),
    )
    local_gate_layer(
        "terminal-root-invert",
        lambda block, orientation: make_gate("X", (block.root_sites[orientation],), f"terminal-root-invert:{orientation}:i{block.index}"),
    )
    local_gate_layer(
        "terminal-compute",
        lambda block, orientation: make_gate(
            "TOFFOLI",
            (block.packet[orientation][0], block.cap_sites[orientation], block.terminal_sites[orientation]),
            f"terminal-compute:{orientation}:i{block.index}",
        ),
    )
    local_gate_layer(
        "terminal-latch",
        lambda block, orientation: make_gate(
            "TOFFOLI",
            (block.terminal_sites[orientation], block.root_sites[orientation], block.done_sites[orientation]),
            f"terminal-latch:{orientation}:i{block.index}",
        ),
    )
    local_gate_layer(
        "terminal-uncompute",
        lambda block, orientation: make_gate(
            "TOFFOLI",
            (block.packet[orientation][0], block.cap_sites[orientation], block.terminal_sites[orientation]),
            f"terminal-compute:{orientation}:i{block.index}",
        ),
    )
    local_gate_layer(
        "terminal-root-restore",
        lambda block, orientation: make_gate("X", (block.root_sites[orientation],), f"terminal-root-restore:{orientation}:i{block.index}"),
    )

    for lane in range(max(PACKET_YS)):
        layers.append(
            Layer(
                f"link-fanout:{lane}",
                tuple(
                    make_gate(
                        "CNOT",
                        (bond.bus[lane], bond.bus[lane + 1]),
                        f"link-fanout:b{bond.index}:lane{lane}",
                    )
                    for bond in bonds
                ),
            )
        )
    cross_triples = tuple(
        (
            bond.bus[lane],
            blocks[bond.index].packet["B"][PACKET_YS.index(lane)],
            blocks[bond.index + 1].packet["A"][PACKET_YS.index(lane)],
            f"link-cross:b{bond.index}:lane{lane}",
        )
        for bond in bonds
        for lane in PACKET_YS
    )
    layers.extend(fredkin_layers("link-cross", cross_triples))
    for lane in reversed(range(max(PACKET_YS))):
        layers.append(
            Layer(
                f"link-unfanout:{lane}",
                tuple(
                    make_gate(
                        "CNOT",
                        (bond.bus[lane], bond.bus[lane + 1]),
                        f"link-unfanout:b{bond.index}:lane{lane}",
                    )
                    for bond in bonds
                ),
            )
        )

    def onsite_pairs(left_role: str, right_role: str, stage: str):
        return tuple(
            (
                block.packet[left_role][PACKET_YS.index(lane)],
                block.packet[right_role][PACKET_YS.index(lane)],
                f"onsite-{stage}:i{block.index}:lane{lane}",
            )
            for block in blocks
            for lane in PACKET_YS
        )

    for stage, left_role, right_role in (
        ("am1", "A", "M"),
        ("mb", "M", "B"),
        ("am2", "A", "M"),
    ):
        layers.extend(swap_layers(f"onsite-{stage}", onsite_pairs(left_role, right_role, stage)))

    if len(layers) != 156:
        raise RuntimeError(("fixed global layer inventory drifted", len(layers)))

    installed_blocks = tuple(reversed(blocks)) if presentation_reversed else tuple(blocks)
    layout = Layout(
        fixture,
        count,
        transformed_sites,
        installed_blocks,
        tuple(bonds),
        tuple(layers),
        tuple(int(item) for item in matrix.flat),
        presentation_reversed,
    )
    values = [0] * len(transformed_sites)
    for block in blocks:
        for site, bit in zip(block.record_sites, c342.record_word(block.record)):
            values[site] = bit
        for orientation in ORIENTATIONS:
            values[block.member_sites[orientation]] = block.member
    for orientation in ORIENTATIONS:
        for endpoint in (blocks[0], blocks[-1]):
            values[endpoint.cap_sites[orientation]] = 1
    values[blocks[0].root_sites["B"]] = 1
    values[blocks[-1].root_sites["A"]] = 1
    for bond in bonds:
        values[bond.bus[0]] = 1
    return layout, tuple(values)


def initial_state(layout: Layout, static_bits: tuple[int, ...], *, reverse: bool = False) -> MachineState:
    bits = list(static_bits)
    ordered = tuple(sorted(layout.blocks, key=lambda block: block.index))
    block = ordered[-1] if reverse else ordered[0]
    orientation = "A" if reverse else "B"
    inactive_orientation = "B" if reverse else "A"
    selector_value = int(reverse)
    # Selector 0 declares B active/A guarded; selector 1 declares A active/B
    # guarded.  The selector is repeated locally and joined only by two-site
    # NN equality wires.  It is a code-space constraint, not a step input.
    for item in ordered:
        bits[item.selector_site] = selector_value
        bits[item.visited_sites[inactive_orientation]] = 1
    for bond in layout.bonds:
        for site in bond.selector_wire:
            bits[site] = selector_value
    bits[block.packet[orientation][0]] = 1
    bits[block.packet[orientation][1]] = 1
    return MachineState(layout, tuple(bits))


def validate_basis_shape(state: MachineState) -> None:
    if not isinstance(state, MachineState):
        raise TypeError("counter state must be one installed physical basis state")
    if len(state.bits) != len(state.layout.sites):
        raise ValueError("counter state has the wrong installed M2 width")
    if any(bit not in (0, 1) for bit in state.bits):
        raise ValueError("counter state must be an M2 basis word")


def execute_layers(state: MachineState, layers: tuple[Layer, ...]) -> MachineState:
    values = list(state.bits)
    for layer in layers:
        for gate in layer.gates:
            c353.apply_gate(values, gate)
    return replace(state, bits=tuple(values))


def step(state):
    validate_basis_shape(state)
    return execute_layers(state, state.layout.layers)


def inverse_step(state):
    validate_basis_shape(state)
    inverse = tuple(
        Layer(layer.name, tuple(reversed(layer.gates)))
        for layer in reversed(state.layout.layers)
    )
    return execute_layers(state, inverse)


def without_gate(state: MachineState, layer_name: str, label: str) -> MachineState:
    removed = 0
    layers = []
    for layer in state.layout.layers:
        gates = []
        for gate in layer.gates:
            if layer.name == layer_name and gate.label == label:
                removed += 1
            else:
                gates.append(gate)
        layers.append(Layer(layer.name, tuple(gates)))
    if removed != 1:
        raise ValueError((layer_name, label, removed))
    return replace(state, layout=replace(state.layout, layers=tuple(layers)))


def done_count(state: MachineState) -> int | None:
    found = []
    for block in state.layout.blocks:
        for orientation in ORIENTATIONS:
            if state.bits[block.done_sites[orientation]]:
                tokens = []
                for role in ("A", "B"):
                    packet = block.packet[role]
                    if state.bits[packet[0]]:
                        occupied = tuple(
                            index
                            for index, site in enumerate(packet[1:])
                            if state.bits[site]
                        )
                        if len(occupied) == 1:
                            tokens.append(occupied[0])
                if len(tokens) == 1:
                    found.append(tokens[0])
    return found[0] if len(found) == 1 else None


def run_until_done(state: MachineState) -> tuple[MachineState, tuple[MachineState, ...]]:
    current = state
    trace = []
    for _observation_only in range(COUNTER_CAPACITY + 2):
        current = step(current)
        trace.append(current)
        if done_count(current) is not None:
            return current, tuple(trace)
    return current, tuple(trace)


def local_selector_guard_constraint_failures(state: MachineState) -> int:
    """Count bounded selector, head-sector, and inactive-guard violations."""

    failures = 0
    ordered = tuple(sorted(state.layout.blocks, key=lambda block: block.index))
    for bond in state.layout.bonds:
        chain = (
            ordered[bond.index].selector_site,
            *bond.selector_wire,
            ordered[bond.index + 1].selector_site,
        )
        failures += sum(
            state.bits[left] != state.bits[right]
            for left, right in zip(chain, chain[1:])
        )
    for block in ordered:
        selector = state.bits[block.selector_site]
        a_head = state.bits[block.packet["A"][0]]
        b_head = state.bits[block.packet["B"][0]]
        if selector == 0:
            # The existing fixed circuit leaves a DONE-latched B-terminal
            # packet on the returned A rail after its final onsite swap.
            failures += int(a_head != state.bits[block.done_sites["B"]])
            failures += int(b_head == 1 and state.bits[block.done_sites["B"]] == 1)
            failures += state.bits[block.done_sites["A"]]
        else:
            failures += int(b_head != state.bits[block.done_sites["A"]])
            failures += int(a_head == 1 and state.bits[block.done_sites["A"]] == 1)
            failures += state.bits[block.done_sites["B"]]
        inactive = "A" if selector == 0 else "B"
        failures += int(state.bits[block.visited_sites[inactive]] != 1)
    return failures


def auxiliary_constraint_failures(state: MachineState) -> int:
    failures = 0
    heads = 0
    for block in state.layout.blocks:
        for role in ("A", "B"):
            packet = block.packet[role]
            head = state.bits[packet[0]]
            occupied = sum(state.bits[site] for site in packet[1:])
            heads += head
            failures += int((head == 0 and occupied != 0) or (head == 1 and occupied != 1))
        failures += sum(state.bits[site] for site in block.packet["M"])
        for orientation in ORIENTATIONS:
            failures += state.bits[block.temp_sites[orientation]]
            failures += state.bits[block.terminal_sites[orientation]]
            failures += sum(state.bits[site] for site in block.activation_sites[orientation])
            failures += int(state.bits[block.member_sites[orientation]] != block.member)
    failures += int(heads != 1)
    for bond in state.layout.bonds:
        failures += sum(state.bits[site] for site in bond.bus[1:])
    failures += local_selector_guard_constraint_failures(state)
    return failures


def record_hash(state: MachineState) -> str:
    payload = bytes(
        state.bits[site]
        for block in sorted(state.layout.blocks, key=lambda item: item.index)
        for site in block.record_sites
    )
    return sha256(payload).hexdigest()


def support_connected_nn(gate: Gate, sites: tuple[Site, ...]) -> bool:
    coords = tuple(sites[index].coord for index in gate.sites)
    reached = {0}
    while True:
        grown = reached | {
            right
            for left in reached
            for right in range(len(coords))
            if c353.manhattan(coords[left], coords[right]) == 1
        }
        if grown == reached:
            return len(reached) == len(coords)
        reached = grown


def selector_constraint_geometry(layout: Layout) -> tuple[int, int]:
    """Return NN-bond failures and the largest one-cell constraint diameter."""

    ordered = tuple(sorted(layout.blocks, key=lambda block: block.index))
    nn_failures = sum(
        c353.manhattan(layout.sites[left].coord, layout.sites[right].coord) != 1
        for bond in layout.bonds
        for left, right in zip(
            (
                ordered[bond.index].selector_site,
                *bond.selector_wire,
                ordered[bond.index + 1].selector_site,
            ),
            (
                *bond.selector_wire,
                ordered[bond.index + 1].selector_site,
            ),
        )
    )
    cell_diameter = max(
        c353.manhattan(layout.sites[block.selector_site].coord, layout.sites[site].coord)
        for block in ordered
        for site in (
            block.packet["A"][0],
            block.packet["B"][0],
            block.visited_sites["A"],
            block.visited_sites["B"],
            block.done_sites["A"],
            block.done_sites["B"],
        )
    )
    return nn_failures, cell_diameter


def layer_conflicts(layer: Layer) -> int:
    used: set[int] = set()
    conflicts = 0
    for gate in layer.gates:
        conflicts += len(used.intersection(gate.sites))
        used.update(gate.sites)
    return conflicts


def primitive_controls() -> dict[str, int]:
    failures = 0
    for bits in product((0, 1), repeat=3):
        state = list(bits)
        gates = (
            Gate("CNOT", (2, 1), "a"),
            Gate("TOFFOLI", (0, 1, 2), "b"),
            Gate("CNOT", (2, 1), "c"),
        )
        for gate in gates:
            c353.apply_gate(state, gate)
        expected = (bits[0], bits[2] if bits[0] else bits[1], bits[1] if bits[0] else bits[2])
        failures += int(tuple(state) != expected)
        for gate in reversed(gates):
            c353.apply_gate(state, gate)
        failures += int(tuple(state) != bits)
    check(
        "the controlled packet SWAP primitive is exact and self-inverse on its complete basis domain",
        failures == 0,
        {"Fredkin_truth_or_inverse_failures": failures},
    )
    return {"failures": failures}


def fixed_global_geometry_controls() -> dict[str, object]:
    frame = np.eye(3, dtype=int)
    fixture = c342.c338.build_fixture(6)
    rows = []
    failures = 0
    for count in SIZES:
        layout, _bits = build_layout(fixture, count, frame)
        alternate_layout, _alternate_bits = build_layout(
            fixture,
            count,
            frame,
            members=tuple(index % 2 for index in range(count)),
        )
        compiled_signature = tuple(
            (
                layer.name,
                tuple((gate.kind, gate.sites, gate.label) for gate in layer.gates),
            )
            for layer in layout.layers
        )
        alternate_compiled_signature = tuple(
            (
                layer.name,
                tuple((gate.kind, gate.sites, gate.label) for gate in layer.gates),
            )
            for layer in alternate_layout.layers
        )
        control_sites = {
            site
            for layer in layout.layers
            for gate in layer.gates
            for site in gate.sites[:-1]
        }
        required_control_groups = {
            "head": {
                block.packet[orientation][0]
                for block in layout.blocks
                for orientation in ORIENTATIONS
            },
            "link": {bond.bus[0] for bond in layout.bonds},
            "member": {
                block.member_sites[orientation]
                for block in layout.blocks
                for orientation in ORIENTATIONS
            },
            "cap": {
                block.cap_sites[orientation]
                for block in layout.blocks
                for orientation in ORIENTATIONS
            },
            "visited": {
                block.visited_sites[orientation]
                for block in layout.blocks
                for orientation in ORIENTATIONS
            },
            "count": {
                site
                for block in layout.blocks
                for orientation in ORIENTATIONS
                for site in block.packet[orientation][1:]
            },
        }
        missing_control_roles = tuple(
            name
            for name, sites in required_control_groups.items()
            if sites and not sites.intersection(control_sites)
        )
        arity = sum(len(gate.sites) > 3 for layer in layout.layers for gate in layer.gates)
        nn = sum(not support_connected_nn(gate, layout.sites) for layer in layout.layers for gate in layer.gates)
        selector_nn, selector_cell_diameter = selector_constraint_geometry(layout)
        conflicts = sum(layer_conflicts(layer) for layer in layout.layers)
        record_sites = {site for block in layout.blocks for site in block.record_sites}
        record_support_gates = sum(
            bool(record_sites.intersection(gate.sites))
            for layer in layout.layers
            for gate in layer.gates
        )
        row = {
            "N": count,
            "held": count == HELD_SIZE,
            "M2_sites": len(layout.sites),
            "cell_M2": 141,
            "bond_M2": 23,
            "selector_M2_per_cell": 1,
            "selector_wire_M2_per_bond": 2,
            "layers": len(layout.layers),
            "gates": sum(len(layer.gates) for layer in layout.layers),
            "arity_failures": arity,
            "connected_NN_failures": nn,
            "selector_wire_NN_failures": selector_nn,
            "selector_cell_constraint_max_L1": selector_cell_diameter,
            "layer_conflicts": conflicts,
            "coordinate_collisions": len(layout.sites) - len({site.coord for site in layout.sites}),
            "missing_physical_control_roles": missing_control_roles,
            "member_state_layer_signature_residual": int(
                compiled_signature != alternate_compiled_signature
            ),
            "Record_support_gates": record_support_gates,
        }
        failures += arity + nn + selector_nn + conflicts + row["coordinate_collisions"]
        failures += int(selector_cell_diameter > 6)
        failures += int(len(layout.sites) != 141 * count + 23 * (count - 1))
        failures += len(missing_control_roles) + row["member_state_layer_signature_residual"]
        failures += record_support_gates
        rows.append(row)
    source = getsource(step).lower()
    forbidden = (
        "active_block",
        "linked_neighbour",
        "state-selected",
        "target_block",
        "host_index",
        "step_index",
    )
    hits = tuple(token for token in forbidden if token in source)
    check(
        "one fixed 156-layer global rule has constant overhead, connected-NN support, and no layer conflicts or host dispatcher",
        failures == 0
        and tuple(signature(step).parameters) == ("state",)
        and not hits
        and all(row["layers"] == 156 for row in rows),
        {
            "rows": rows,
            "step_parameters": tuple(signature(step).parameters),
            "forbidden_step_source_hits": hits,
            "step_body": source.strip(),
        },
    )
    return {"rows": rows, "failures": failures}


def corpus_frame_inverse_controls() -> dict[str, object]:
    frames = c353.proper_cubic_frames()
    cases = 0
    count_failures = 0
    inverse_failures = 0
    locality_failures = 0
    leakage_failures = 0
    local_selector_guard_failures = 0
    selector_geometry_failures = 0
    held_cases = 0
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        for count in SIZES:
            for frame in frames:
                layout, bits = build_layout(fixture, count, frame)
                initial = initial_state(layout, bits)
                before_hash = record_hash(initial)
                terminal, trace = run_until_done(initial)
                count_failures += int(done_count(terminal) != count or len(trace) != count)
                leakage_failures += sum(auxiliary_constraint_failures(item) for item in trace)
                local_selector_guard_failures += sum(
                    local_selector_guard_constraint_failures(item) for item in trace
                )
                selector_nn, selector_cell_diameter = selector_constraint_geometry(layout)
                selector_geometry_failures += selector_nn + int(selector_cell_diameter > 6)
                locality_failures += sum(
                    not support_connected_nn(gate, layout.sites)
                    for layer in layout.layers
                    for gate in layer.gates
                )
                recovered = terminal
                for _ in range(len(trace)):
                    recovered = inverse_step(recovered)
                inverse_failures += int(recovered.bits != initial.bits)
                inverse_failures += int(record_hash(terminal) != before_hash)
                cases += 1
                held_cases += int(length == HELD_LENGTH and count == HELD_SIZE)
    check(
        "the same fixed rule counts L3/L6 N6/N12/N18 in every proper-cubic frame with exact inverse and zero auxiliary leakage",
        cases == 144
        and held_cases == 24
        and count_failures == inverse_failures == locality_failures == leakage_failures == 0
        and local_selector_guard_failures == 0
        and selector_geometry_failures == 0,
        {
            "L_by_N_by_frame_cases": cases,
            "held_L6_N18_frame_cases": held_cases,
            "count_failures": count_failures,
            "inverse_or_Record_hash_failures": inverse_failures,
            "connected_NN_failures": locality_failures,
            "auxiliary_constraint_failures": leakage_failures,
            "local_selector_guard_constraint_failures": local_selector_guard_failures,
            "proper_cubic_selector_geometry_failures": selector_geometry_failures,
        },
    )
    return {
        "cases": cases,
        "count_failures": count_failures,
        "inverse_failures": inverse_failures,
        "leakage_failures": leakage_failures,
        "local_selector_guard_failures": local_selector_guard_failures,
        "selector_geometry_failures": selector_geometry_failures,
    }


def invariance_alias_member_controls() -> dict[str, object]:
    frame = np.eye(3, dtype=int)
    fixture = c342.c338.build_fixture(6)
    layout, bits = build_layout(fixture, 18, frame)
    forward, _ = run_until_done(initial_state(layout, bits))
    reverse, _ = run_until_done(initial_state(layout, bits, reverse=True))
    presented_layout, presented_bits = build_layout(
        fixture, 18, frame, presentation_reversed=True
    )
    presented, _ = run_until_done(initial_state(presented_layout, presented_bits))
    words = tuple(c342.record_word(block.record) for block in layout.blocks)

    nonmember_layout, nonmember_bits = build_layout(
        fixture, 13, frame, members=(1,) * 12 + (0,)
    )
    member_layout, member_bits = build_layout(fixture, 13, frame, members=(1,) * 13)
    nonmember, _ = run_until_done(initial_state(nonmember_layout, nonmember_bits))
    member, _ = run_until_done(initial_state(member_layout, member_bits))
    detail = {
        "forward_count": done_count(forward),
        "link_reversal_count": done_count(reverse),
        "presentation_reversal_count": done_count(presented),
        "Record_sites": len(words),
        "distinct_Record_words": len(set(words)),
        "period_6_alias_offset": 6,
        "N13_nonmember_count": done_count(nonmember),
        "N13_member_count": done_count(member),
        "Record_hash_preserved": record_hash(forward) == record_hash(initial_state(layout, bits)),
    }
    check(
        "link reversal and presentation order preserve count, period-six aliases remain site-distinct, and local member bits change only count",
        detail["forward_count"] == detail["link_reversal_count"] == detail["presentation_reversal_count"] == 18
        and detail["Record_sites"] == 18
        and detail["distinct_Record_words"] == 6
        and detail["N13_nonmember_count"] == 12
        and detail["N13_member_count"] == 13
        and detail["Record_hash_preserved"],
        detail,
    )
    return detail


def deletion_and_domain_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(6)
    frame = np.eye(3, dtype=int)
    layout, bits = build_layout(fixture, 12, frame)
    initial = initial_state(layout, bits)
    ordered = tuple(sorted(layout.blocks, key=lambda block: block.index))
    nominal, _ = run_until_done(initial)

    link_bits = list(initial.bits)
    link_bits[layout.bonds[5].bus[0]] = 0
    link_terminal, _ = run_until_done(replace(initial, bits=tuple(link_bits)))

    inactive_guard_site = ordered[5].visited_sites["A"]
    guard_deleted_bits = list(initial.bits)
    guard_deleted_bits[inactive_guard_site] = 0
    guard_deleted = replace(initial, bits=tuple(guard_deleted_bits))
    guard_deleted_nominal, _ = run_until_done(guard_deleted)
    guard_and_link_deleted_bits = list(guard_deleted.bits)
    guard_and_link_deleted_bits[layout.bonds[5].bus[0]] = 0
    guard_and_link_deleted, _ = run_until_done(
        replace(guard_deleted, bits=tuple(guard_and_link_deleted_bits))
    )

    selector_fault_bits = list(initial.bits)
    selector_fault_site = ordered[5].selector_site
    selector_fault_bits[selector_fault_site] ^= 1
    selector_fault = replace(initial, bits=tuple(selector_fault_bits))
    reverse_initial = initial_state(layout, bits, reverse=True)

    cap_bits = list(initial.bits)
    cap_bits[ordered[-1].cap_sites["B"]] = 0
    cap_terminal, _ = run_until_done(replace(initial, bits=tuple(cap_bits)))

    member_bits = list(initial.bits)
    for orientation in ORIENTATIONS:
        member_bits[ordered[5].member_sites[orientation]] = 0
    member_terminal, _ = run_until_done(replace(initial, bits=tuple(member_bits)))

    visited_bits = list(initial.bits)
    visited_bits[ordered[5].visited_sites["B"]] = 1
    visited_terminal, _ = run_until_done(replace(initial, bits=tuple(visited_bits)))

    deleted = without_gate(
        initial,
        "count-fredkin:0-b",
        "count-fredkin:B:i0:k0:b",
    )
    deleted_terminal, _ = run_until_done(deleted)

    attacks = {
        "nominal_count": done_count(nominal),
        "link_deletion_count": done_count(link_terminal),
        "inactive_guard_site": inactive_guard_site,
        "selector_fault_site": selector_fault_site,
        "nominal_initial_local_selector_guard_constraint_failures": local_selector_guard_constraint_failures(initial),
        "guard_deleted_initial_constraint_failures": local_selector_guard_constraint_failures(guard_deleted),
        "selector_fault_local_constraint_failures": local_selector_guard_constraint_failures(selector_fault),
        "reverse_sector_local_constraint_failures": local_selector_guard_constraint_failures(reverse_initial),
        "guard_deleted_intact_link_count": done_count(guard_deleted_nominal),
        "guard_protected_link_deletion_count": done_count(link_terminal),
        "guard_deleted_link_deletion_count": done_count(guard_and_link_deleted),
        "guard_deletion_reflection_count_delta": (
            None
            if done_count(guard_and_link_deleted) is None or done_count(link_terminal) is None
            else done_count(guard_and_link_deleted) - done_count(link_terminal)
        ),
        "cap_deletion_count": done_count(cap_terminal),
        "member_bit_5_deleted_count": done_count(member_terminal),
        "visited_bit_5_preseeded_count": done_count(visited_terminal),
        "counter_gate_deletion_count": done_count(deleted_terminal),
    }
    visible = (
        attacks["nominal_count"] == 12
        and attacks["link_deletion_count"] != 12
        and attacks["nominal_initial_local_selector_guard_constraint_failures"] == 0
        and attacks["guard_deleted_initial_constraint_failures"] == 1
        and attacks["selector_fault_local_constraint_failures"] == 3
        and attacks["reverse_sector_local_constraint_failures"] == 0
        and attacks["guard_deleted_intact_link_count"] == 12
        and attacks["guard_protected_link_deletion_count"] == 6
        and attacks["guard_deleted_link_deletion_count"] == 7
        and attacks["guard_deletion_reflection_count_delta"] == 1
        and attacks["cap_deletion_count"] != 12
        and attacks["member_bit_5_deleted_count"] == 11
        and attacks["visited_bit_5_preseeded_count"] == 11
        and attacks["counter_gate_deletion_count"] != 12
    )

    attempts = 0
    rejections = 0

    def rejected(callable_) -> None:
        nonlocal attempts, rejections
        attempts += 1
        try:
            callable_()
        except (ValueError, TypeError):
            rejections += 1

    rejected(lambda: build_layout(fixture, 0, frame))
    rejected(lambda: build_layout(fixture, 19, frame))
    rejected(lambda: build_layout(fixture, True, frame))
    rejected(lambda: build_layout(fixture, 6, frame, members=(1,) * 5))
    rejected(lambda: build_layout(fixture, 6, -np.eye(3, dtype=int)))
    rejected(lambda: step(replace(initial, bits=initial.bits[:-1])))
    malformed = list(initial.bits)
    malformed[0] = 2
    rejected(lambda: step(replace(initial, bits=tuple(malformed))))
    rejected(lambda: step(initial.bits))
    check(
        "local selector/guard/link/cap/member/visited/counter faults are visible and malformed installed domains are rejected",
        visible and attempts == rejections,
        {"attacks": attacks, "domain_attempts": attempts, "domain_rejections": rejections},
    )
    return {"attacks": attacks, "visible": visible, "attempts": attempts, "rejections": rejections}


def inherited_physics_controls() -> dict[str, object]:
    expected_contact = np.diag((np.exp(1j * c317.c311.COUPLING), 1)).astype(complex)
    rows = []
    failures = 0
    for length in LENGTHS:
        fixture = c317.physical_fixture(length)
        projector = fixture.full_encoding @ fixture.full_encoding.conj().T
        row = {
            "L": length,
            "held": length == HELD_LENGTH,
            "two_ray_gram_residual": float(np.linalg.norm(fixture.two_ray_encoding.conj().T @ fixture.two_ray_encoding - c317.I2)),
            "accepted_code_leakage": float(np.linalg.norm((np.eye(projector.shape[0]) - projector) @ fixture.two_ray_encoding)),
            "contact_residual": float(np.linalg.norm(fixture.contact - expected_contact)),
            "contact_intertwiner_residual": float(np.linalg.norm(fixture.physical_contact @ fixture.two_ray_encoding - fixture.two_ray_encoding @ fixture.contact)),
            "constraint_residual": float(np.linalg.norm(fixture.constraint @ fixture.two_ray_encoding - fixture.two_ray_encoding)),
        }
        failures += int(max(value for key, value in row.items() if "residual" in key or "leakage" in key) > TOL)
        rows.append(row)
    species = c317.c311.c219.common_species(-0.3)
    one_particle = c317.c311.exterior_matrix(species.coin, 1)
    mass_residual = abs(c317.c311.c219.rest_mass(species) / species.analytic_mass - 1)
    one_particle_residual = float(np.linalg.norm(one_particle - species.coin))
    failures += int(mass_residual > 3e-12 or one_particle_residual > TOL)
    check(
        "the fixed-global counter is a spectator to the inherited one-particle mass and Cycle-230 seam contact fixtures",
        failures == 0,
        {
            "rows": rows,
            "one_particle_matrix_residual": one_particle_residual,
            "mass_relative_residual": mass_residual,
            "counter_targets_Record_or_matter_sites": False,
        },
    )
    return {"rows": rows, "mass_residual": mass_residual, "failures": failures}


def supplied_structure_and_semantic_controls() -> dict[str, object]:
    inventory = {
        "result": "bounded fixed-global autonomous local-link Record-member counter",
        "fixed_global_layers": 156,
        "state_dependent_host_gate_selection": False,
        "active_head_or_neighbour_scan": False,
        "step_parameters": tuple(signature(step).parameters),
        "step_validates_only_basis_shape_then_fixed_layers": True,
        "supplied_link_formation": "straight reciprocal adjacent Record chain",
        "supplied_link_certificate": "host-checked Cycle342 continuation; autonomous link genesis not derived",
        "supplied_root_and_frame": "endpoint root marker plus A/B orientation rail in one proper-cubic spatial frame",
        "supplied_direction_selector": "one M2 per block; zero declares B active/A guarded and one declares A active/B guarded",
        "supplied_selector_bond_wire": "two persistent M2 per bond join adjacent block selectors by three pairwise NN equalities",
        "selector_M2_per_cell": 1,
        "selector_wire_M2_per_bond": 2,
        "selector_controls_or_targets_fixed_step": False,
        "local_selector_bond_constraint": "each adjacent selector-wire pair agrees; every check has two-site NN support",
        "local_head_selector_constraint": "an in-flight head matches the selector; a returned terminal head requires the same block's selector-declared active DONE latch",
        "terminal_head_convention": "the fixed final onsite swap retains a DONE-latched outbound B(A) terminal packet on A(B)",
        "local_inactive_guard_constraint": "each block's selector-declared opposite visited bit is one",
        "selector_and_guard_constraint_support": "one cell with L1 diameter at most six or one adjacent NN selector-wire pair, independent of chain size",
        "uniform_reverse_sector": "globally flip selectors and bond wires, seed the reverse head, and guard the opposite rail",
        "guard_deletion_control": "one cleared inactive guard bit gives one local violation and shifts the reflected missing-link count by +1",
        "selector_fault_control": "one interior selector flip gives three local violations while the uniform reverse sector gives zero",
        "supplied_members": "duplicated equal local A/B member bits per Record",
        "supplied_caps": "duplicated endpoint cap bits on both orientation rails",
        "supplied_counter_capacity": COUNTER_CAPACITY,
        "N_specific_layout_and_gate_unrolling": True,
        "layer_names_and_depth_N_independent": True,
        "observation_harness": "fixed capacity bound observing local DONE; never changes step layers",
        "counter_value": "dimensionless Record-member count only",
        "traversal_is_time": False,
        "layer_is_time": False,
        "count_is_interval": False,
        "count_is_rate": False,
        "count_is_proper_time": False,
        "time_or_evolution_axis_derived": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the fixed-program repair and every supplied formation/capacity boundary remain explicit with count-only semantics",
        inventory["fixed_global_layers"] == 156
        and not inventory["state_dependent_host_gate_selection"]
        and not inventory["active_head_or_neighbour_scan"]
        and inventory["step_parameters"] == ("state",)
        and inventory["step_validates_only_basis_shape_then_fixed_layers"]
        and inventory["supplied_link_certificate"].endswith("not derived")
        and inventory["supplied_direction_selector"].startswith("one M2 per block")
        and inventory["supplied_selector_bond_wire"].startswith("two persistent M2 per bond")
        and not inventory["selector_controls_or_targets_fixed_step"]
        and inventory["local_selector_bond_constraint"].endswith("two-site NN support")
        and inventory["local_head_selector_constraint"].startswith("an in-flight head")
        and inventory["local_inactive_guard_constraint"].endswith("is one")
        and inventory["guard_deletion_control"].endswith("by +1")
        and inventory["selector_fault_control"].endswith("gives zero")
        and inventory["N_specific_layout_and_gate_unrolling"]
        and inventory["layer_names_and_depth_N_independent"]
        and all(
            inventory[key] is False
            for key in (
                "traversal_is_time",
                "layer_is_time",
                "count_is_interval",
                "count_is_rate",
                "count_is_proper_time",
                "time_or_evolution_axis_derived",
                "shared_obstruction",
                "axiom_pressure",
            )
        )
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def main() -> None:
    primitive_controls()
    fixed_global_geometry_controls()
    corpus = corpus_frame_inverse_controls()
    invariance_alias_member_controls()
    deletions = deletion_and_domain_controls()
    inherited_physics_controls()
    supplied_structure_and_semantic_controls()
    print(
        "RESULT",
        {
            "route": "fixed-global-local-link-counter",
            "strongest_constructive_result": "autonomous_fixed_global_connected_NN_dimensionless_Record_member_count",
            "frame_size_count_failures": corpus["count_failures"],
            "inverse_failures": corpus["inverse_failures"],
            "auxiliary_leakage_failures": corpus["leakage_failures"],
            "local_selector_guard_constraint_failures": corpus[
                "local_selector_guard_failures"
            ],
            "proper_cubic_selector_geometry_failures": corpus[
                "selector_geometry_failures"
            ],
            "guard_deleted_initial_constraint_failures": deletions["attacks"][
                "guard_deleted_initial_constraint_failures"
            ],
            "selector_fault_local_constraint_failures": deletions["attacks"][
                "selector_fault_local_constraint_failures"
            ],
            "reverse_sector_local_constraint_failures": deletions["attacks"][
                "reverse_sector_local_constraint_failures"
            ],
            "guard_deletion_reflection_count_delta": deletions["attacks"][
                "guard_deletion_reflection_count_delta"
            ],
            "state_dependent_host_gate_selection": False,
            "shared_obstruction": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("SUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
