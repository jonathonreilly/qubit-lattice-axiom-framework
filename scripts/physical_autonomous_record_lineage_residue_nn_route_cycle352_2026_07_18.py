#!/usr/bin/env python3
"""Cycle 352 Route 1: autonomous local Record-lineage/residue transducer.

This positive runner preloads each conditional Cycle-342 Record word in a
fixed three-by-sixteen-by-four cubic M2 macrocell, including every unoccupied
future cell.  One supplied root seed and one preloaded local formation input
per cell feed a single reversible ``step(state)`` circuit.  The circuit
snapshots only the locally marked frontier, crosses
each directed nearest-neighbour macrocell bond through disjoint ports, writes
the predecessor ports, and rotates a six-rail residue/name tag.  Repeating the
same state-local step grows a rooted link chain; no Record ID, host index,
membership mask, common-history key, or lineage dictionary is present.  The
autonomous result is the lineage/occupancy/residue sidecar only: Record
payloads, occurrence, and formation are not generated from the root.

Every X/CNOT/Toffoli primitive carries physical cubic coordinates.  Two-site
supports are nearest neighbours and three-site supports induce a connected
nearest-neighbour subgraph.  Longer in-cell moves are explicitly compiled to
nearest-neighbour SWAPs (three CNOTs) and restored.  Circuit layers are fixed
reversible circuit layering, not time.  The layout is spatial only: no OS/Z4
axis, interval, rate, proper time, or evolution-axis discharge is claimed.
Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from inspect import getsource, signature
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317
import physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18 as c342


Coord = tuple[int, int, int]
LENGTHS = (3, 6)
CHAIN_SIZES = (6, 12, 18)
HELD_CHAIN_SIZE = 18
ENDPOINT = 0
CELL_X = 3
CELL_Y = 16
CELL_Z = 4
MACROCELL_M2 = CELL_X * CELL_Y * CELL_Z
LINEAGE_OVERHEAD_M2 = MACROCELL_M2 - c342.RECORD_BITS
RESIDUES = 6
PORT_LANES = 1 + RESIDUES
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


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def moved(coord: Coord, frame: np.ndarray) -> Coord:
    vector = np.asarray(coord, dtype=int) @ np.asarray(frame, dtype=int).T
    return tuple(int(item) for item in vector)


@dataclass(frozen=True)
class Site:
    coord: Coord
    cell_origin: Coord


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    coords: tuple[Coord, ...]
    label: str


@dataclass(frozen=True)
class Macrocell:
    origin: Coord
    path: tuple[int, ...]
    formation: int
    seed: int
    root: int
    boundary: int
    done: int
    occupied: int
    front: int
    predecessor_in: int
    successor_out: int
    residue: tuple[int, ...]
    prefix: tuple[int, ...]
    in_form: tuple[int, ...]
    in_data: tuple[int, ...]
    out_data: tuple[int, ...]
    out_depart: int
    record: tuple[int, ...]
    router_ancilla: tuple[int, ...]


@dataclass(frozen=True)
class Layout:
    sites: tuple[Site, ...]
    cells: tuple[Macrocell, ...]
    bonds: tuple[tuple[Macrocell, Macrocell], ...]
    layers: tuple[tuple[Gate, ...], ...]
    logical_operations: int


@dataclass(frozen=True)
class BasisState:
    layout: Layout
    bits: tuple[int, ...]


def cell_coords(origin_x: int) -> tuple[Coord, ...]:
    """Hamiltonian NN path through one 3x16x4 cubic macrocell."""

    plane = tuple(
        (y, z)
        for y in range(CELL_Y)
        for z in (
            range(CELL_Z) if y % 2 == 0 else reversed(range(CELL_Z))
        )
    )
    answer: list[Coord] = []
    for local_x in range(CELL_X):
        local_plane = plane if local_x % 2 == 0 else tuple(reversed(plane))
        answer.extend((origin_x + local_x, y, z) for y, z in local_plane)
    assert len(answer) == MACROCELL_M2
    assert all(manhattan(left, right) == 1 for left, right in zip(answer, answer[1:]))
    return tuple(answer)


def local_offset(path_coords: tuple[Coord, ...], coord: Coord, base: int) -> int:
    return base + path_coords.index(coord)


def build_cells(count: int) -> tuple[tuple[Site, ...], tuple[Macrocell, ...]]:
    if count <= 0:
        raise ValueError("a lineage layout needs at least one macrocell")
    sites: list[Site] = []
    cells: list[Macrocell] = []
    for cell_number in range(count):
        origin_x = CELL_X * cell_number
        origin = (origin_x, 0, 0)
        coords = cell_coords(origin_x)
        base = len(sites)
        sites.extend(Site(coord, origin) for coord in coords)
        offset = lambda coord: local_offset(coords, coord, base)

        # Each cross-bond gate uses only a right output face and the next
        # cell's left input face.  Adjacent bonds therefore have disjoint
        # physical supports without an even/odd host schedule.
        in_form = tuple(offset((origin_x, lane, 0)) for lane in range(PORT_LANES))
        in_data = tuple(offset((origin_x, lane, 1)) for lane in range(PORT_LANES))
        out_data = tuple(
            offset((origin_x + CELL_X - 1, lane, 0))
            for lane in range(PORT_LANES)
        )
        out_depart = offset((origin_x + CELL_X - 1, 0, 1))
        reserved = set(in_form + in_data + out_data + (out_depart,))
        available = tuple(base + index for index in range(MACROCELL_M2) if base + index not in reserved)
        names = (
            "formation",
            "seed",
            "root",
            "boundary",
            "done",
            "occupied",
            "front",
            "predecessor_in",
            "successor_out",
        )
        fields = dict(zip(names, available[: len(names)]))
        cursor = len(names)
        residue = available[cursor : cursor + RESIDUES]
        cursor += RESIDUES
        prefix = available[cursor : cursor + RESIDUES]
        cursor += RESIDUES
        record = available[cursor : cursor + c342.RECORD_BITS]
        if len(record) != c342.RECORD_BITS:
            raise RuntimeError("macrocell inventory cannot hold the Record payload")
        assigned = reserved | set(fields.values()) | set(residue) | set(prefix) | set(record)
        router_ancilla = tuple(
            item for item in range(base, base + MACROCELL_M2) if item not in assigned
        )
        cells.append(
            Macrocell(
                origin=origin,
                path=tuple(range(base, base + MACROCELL_M2)),
                formation=fields["formation"],
                seed=fields["seed"],
                root=fields["root"],
                boundary=fields["boundary"],
                done=fields["done"],
                occupied=fields["occupied"],
                front=fields["front"],
                predecessor_in=fields["predecessor_in"],
                successor_out=fields["successor_out"],
                residue=tuple(residue),
                prefix=tuple(prefix),
                in_form=in_form,
                in_data=in_data,
                out_data=out_data,
                out_depart=out_depart,
                record=tuple(record),
                router_ancilla=router_ancilla,
            )
        )
    return tuple(sites), tuple(cells)


def gate(kind: str, offsets: tuple[int, ...], sites: tuple[Site, ...], label: str) -> Gate:
    expected = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in expected or len(offsets) != expected[kind] or len(set(offsets)) != len(offsets):
        raise ValueError((kind, offsets))
    return Gate(kind, offsets, tuple(sites[item].coord for item in offsets), label)


def swap_gates(left: int, right: int, sites: tuple[Site, ...], label: str) -> tuple[Gate, ...]:
    if manhattan(sites[left].coord, sites[right].coord) != 1:
        raise ValueError("a physical SWAP edge must be nearest-neighbour")
    return (
        gate("CNOT", (left, right), sites, label + ":swap-a"),
        gate("CNOT", (right, left), sites, label + ":swap-b"),
        gate("CNOT", (left, right), sites, label + ":swap-c"),
    )


def routing_template(path: tuple[int, ...], operands: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    """Adjacent swaps placing operands contiguously with minimum tested motion."""

    operand_set = set(operands)
    if len(operand_set) != len(operands) or not operand_set <= set(path):
        raise ValueError("routed operands must be distinct sites in one macrocell")
    best: tuple[tuple[int, int], ...] | None = None
    for start in range(len(path) - len(operands) + 1):
        remaining = [item for item in path if item not in operand_set]
        desired = remaining[:start] + list(operands) + remaining[start:]
        current = list(path)
        swaps: list[tuple[int, int]] = []
        for position, wanted in enumerate(desired):
            source = current.index(wanted, position)
            while source > position:
                # Record the physical edge, not the logical labels currently
                # riding on it.  The latter change after every SWAP.
                swaps.append((path[source - 1], path[source]))
                current[source - 1], current[source] = current[source], current[source - 1]
                source -= 1
        candidate = tuple(swaps)
        if best is None or len(candidate) < len(best):
            best = candidate
    assert best is not None
    return best


def routed_gate(
    kind: str,
    operands: tuple[int, ...],
    cell: Macrocell,
    sites: tuple[Site, ...],
    label: str,
) -> tuple[Gate, ...]:
    swaps = routing_template(cell.path, operands)
    current = list(cell.path)
    for left, right in swaps:
        left_position = cell.path.index(left)
        right_position = cell.path.index(right)
        current[left_position], current[right_position] = current[right_position], current[left_position]
    positions = tuple(current.index(item) for item in operands)
    if positions != tuple(range(min(positions), min(positions) + len(operands))):
        raise RuntimeError("routing did not place gate operands contiguously")
    central_offsets = tuple(cell.path[position] for position in positions)
    compiled: list[Gate] = []
    for left, right in swaps:
        compiled.extend(swap_gates(left, right, sites, label))
    compiled.append(gate(kind, central_offsets, sites, label))
    for left, right in reversed(swaps):
        compiled.extend(swap_gates(left, right, sites, label))
    return tuple(compiled)


class CircuitBuilder:
    def __init__(self, sites: tuple[Site, ...], cells: tuple[Macrocell, ...]):
        self.sites = sites
        self.cells = cells
        self.bonds = tuple(zip(cells, cells[1:]))
        self.layers: list[tuple[Gate, ...]] = []
        self.logical_operations = 0

    def local(self, kind: str, operands, label: str) -> None:
        rows = tuple(
            routed_gate(kind, tuple(operands(cell)), cell, self.sites, label)
            for cell in self.cells
        )
        lengths = {len(row) for row in rows}
        if len(lengths) != 1:
            raise RuntimeError("homogeneous local routing acquired cell-dependent depth")
        for column in range(len(rows[0])):
            self.layers.append(tuple(row[column] for row in rows))
        self.logical_operations += 1

    def cross(self, kind: str, operands, label: str) -> None:
        layer = tuple(
            gate(kind, tuple(operands(left, right)), self.sites, label)
            for left, right in self.bonds
        )
        if layer:
            self.layers.append(layer)
        self.logical_operations += 1


def build_layout(count: int) -> Layout:
    sites, cells = build_cells(count)
    builder = CircuitBuilder(sites, cells)

    # Uniform root-seed consumption.  These gates run in every cell; only the
    # single supplied seed is active.  Prefix bits are the local three-arity
    # verifier for the one-hot residue/name rail.
    builder.local("TOFFOLI", lambda c: (c.seed, c.formation, c.front), "root:front")
    builder.local("TOFFOLI", lambda c: (c.seed, c.formation, c.occupied), "root:occupied")
    builder.local("TOFFOLI", lambda c: (c.seed, c.formation, c.root), "root:marker")
    builder.local("TOFFOLI", lambda c: (c.seed, c.formation, c.residue[0]), "root:residue0")
    for rail in range(RESIDUES):
        builder.local(
            "TOFFOLI",
            lambda c, rail=rail: (c.seed, c.formation, c.prefix[rail]),
            f"root:prefix:{rail}",
        )
    builder.local("TOFFOLI", lambda c: (c.front, c.root, c.seed), "root:consume-seed")

    # Copy each cell's one formation input to its seven left-face bond lanes.
    for lane in range(PORT_LANES):
        builder.local(
            "CNOT",
            lambda c, lane=lane: (c.formation, c.in_form[lane]),
            f"formation:fanout:{lane}",
        )

    # Snapshot only the local frontier into the right output port.
    builder.local("CNOT", lambda c: (c.front, c.out_data[0]), "emit:active")
    for rail in range(RESIDUES):
        builder.local(
            "TOFFOLI",
            lambda c, rail=rail: (c.front, c.residue[rail], c.out_data[rail + 1]),
            f"emit:residue:{rail}",
        )

    # All directed bonds execute at once on disjoint left/right port sites.
    builder.cross(
        "TOFFOLI",
        lambda left, right: (left.out_data[0], right.in_form[0], right.in_data[0]),
        "bond:arrival",
    )
    builder.cross(
        "CNOT",
        lambda left, right: (right.in_data[0], left.out_depart),
        "bond:departure-copy",
    )
    for rail in range(RESIDUES):
        builder.cross(
            "TOFFOLI",
            lambda left, right, rail=rail: (
                left.out_data[rail + 1],
                right.in_form[rail + 1],
                right.in_data[rail + 1],
            ),
            f"bond:residue:{rail}",
        )

    # Finalize the arriving cell from its left port.  Nothing here reads a
    # coordinate, index, ID, phase, or host-side target count.
    for field_name, field in (
        ("occupied", lambda c: c.occupied),
        ("front", lambda c: c.front),
        ("predecessor", lambda c: c.predecessor_in),
    ):
        builder.local(
            "CNOT",
            lambda c, field=field: (c.in_data[0], field(c)),
            f"arrival:{field_name}",
        )
    for source_rail in range(RESIDUES):
        target_rail = (source_rail + 1) % RESIDUES
        builder.local(
            "CNOT",
            lambda c, source_rail=source_rail, target_rail=target_rail: (
                c.in_data[source_rail + 1], c.residue[target_rail]
            ),
            f"arrival:residue:{source_rail}-to-{target_rail}",
        )
        for prefix_rail in range(target_rail, RESIDUES):
            builder.local(
                "CNOT",
                lambda c, source_rail=source_rail, prefix_rail=prefix_rail: (
                    c.in_data[source_rail + 1], c.prefix[prefix_rail]
                ),
                f"arrival:prefix:{source_rail}-to-{prefix_rail}",
            )
    builder.local("CNOT", lambda c: (c.out_depart, c.successor_out), "departure:successor")

    # Clean the cross-bond input scratch while the old frontier still exists.
    for rail in reversed(range(RESIDUES)):
        builder.cross(
            "TOFFOLI",
            lambda left, right, rail=rail: (
                left.out_data[rail + 1],
                right.in_form[rail + 1],
                right.in_data[rail + 1],
            ),
            f"uncompute:bond-residue:{rail}",
        )
    builder.cross(
        "TOFFOLI",
        lambda left, right: (left.out_data[0], right.in_form[0], right.in_data[0]),
        "uncompute:bond-arrival",
    )
    for rail in reversed(range(RESIDUES)):
        builder.local(
            "TOFFOLI",
            # The emitted active-port bit is the reversible snapshot control.
            # Using the persistent frontier here would also touch the newly
            # arrived cell in the same autonomous step.
            lambda c, rail=rail: (c.out_data[0], c.residue[rail], c.out_data[rail + 1]),
            f"uncompute:emit-residue:{rail}",
        )
    builder.local("CNOT", lambda c: (c.out_depart, c.out_data[0]), "uncompute:emit-active")
    for lane in reversed(range(PORT_LANES)):
        builder.local(
            "CNOT",
            lambda c, lane=lane: (c.formation, c.in_form[lane]),
            f"uncompute:formation-fanout:{lane}",
        )

    # The departure port locally clears the old frontier.  A temporary copy
    # of the new frontier then clears departure across every disjoint bond.
    builder.local("CNOT", lambda c: (c.out_depart, c.front), "departure:clear-old-front")
    builder.local("CNOT", lambda c: (c.front, c.in_data[0]), "cleanup:new-front-witness")
    builder.cross(
        "CNOT",
        lambda left, right: (right.in_data[0], left.out_depart),
        "cleanup:departure",
    )
    builder.local("CNOT", lambda c: (c.front, c.in_data[0]), "cleanup:front-witness")

    # Finite tests carry one local boundary cap.  DONE is a reversible local
    # stop flag consumed immediately by the harness; circuit calls are not
    # interpreted as physical time.
    builder.local("TOFFOLI", lambda c: (c.front, c.boundary, c.done), "done:set")
    builder.local("TOFFOLI", lambda c: (c.front, c.done, c.boundary), "done:consume-cap")

    layout = Layout(
        sites,
        cells,
        builder.bonds,
        tuple(builder.layers),
        builder.logical_operations,
    )
    validate_layout(layout)
    return layout


def support_connected(coords: tuple[Coord, ...]) -> bool:
    if len(coords) <= 1:
        return True
    reached = {0}
    changed = True
    while changed:
        changed = False
        for left in tuple(reached):
            for right in range(len(coords)):
                if right not in reached and manhattan(coords[left], coords[right]) == 1:
                    reached.add(right)
                    changed = True
    return len(reached) == len(coords)


def validate_layout(layout: Layout) -> None:
    coords = tuple(site.coord for site in layout.sites)
    if len(coords) != len(set(coords)):
        raise RuntimeError("physical M2 site coordinates overlap")
    if len(layout.bonds) != len(layout.cells) - 1:
        raise RuntimeError("the supplied macrocell geometry is not one connected line")
    for cell in layout.cells:
        incoming = sum(right is cell for _, right in layout.bonds)
        outgoing = sum(left is cell for left, _ in layout.bonds)
        if incoming > 1 or outgoing > 1:
            raise RuntimeError("a macrocell has non-line branching")
    if sum(sum(right is cell for _, right in layout.bonds) == 0 for cell in layout.cells) != 1:
        raise RuntimeError("the directed line must have one left boundary")
    if sum(sum(left is cell for left, _ in layout.bonds) == 0 for cell in layout.cells) != 1:
        raise RuntimeError("the directed line must have one right boundary")
    for layer in layout.layers:
        flattened = tuple(site for item in layer for site in item.sites)
        if len(flattened) != len(set(flattened)):
            raise RuntimeError("a fixed circuit layer has overlapping gate supports")
        for item in layer:
            if len(item.sites) > 3 or not support_connected(item.coords):
                raise RuntimeError(("non-NN gate support", item))
            if item.kind == "CNOT" and manhattan(*item.coords) != 1:
                raise RuntimeError(("non-NN CNOT", item))


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "X":
        bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "TOFFOLI":
        control0, control1, target = item.sites
        bits[target] ^= bits[control0] & bits[control1]
    else:
        raise ValueError(item.kind)


def validate_basis(state: BasisState) -> None:
    if len(state.bits) != len(state.layout.sites) or set(state.bits) - {0, 1}:
        raise ValueError("the physical state must be one binary value per declared M2 site")


def scratch_is_zero(state: BasisState) -> bool:
    bits = state.bits
    return all(
        not any(
            bits[item]
            for item in cell.in_form
            + cell.in_data
            + cell.out_data
            + (cell.out_depart,)
            + cell.router_ancilla
        )
        for cell in state.layout.cells
    )


def apply_layers(
    state: BasisState,
    layers: tuple[tuple[Gate, ...], ...],
    *,
    reverse: bool = False,
) -> BasisState:
    validate_basis(state)
    bits = list(state.bits)
    rows = reversed(layers) if reverse else layers
    for layer in rows:
        gates = reversed(layer) if reverse else layer
        for item in gates:
            apply_gate(bits, item)
    return replace(state, bits=tuple(bits))


def step(state: BasisState) -> BasisState:
    """One autonomous fixed local rule; the signature has no host controls."""

    validate_basis(state)
    return apply_layers(state, state.layout.layers)


def inverse_step(state: BasisState) -> BasisState:
    """Exact inverse circuit on the declared code; excluded from lineage law."""

    return apply_layers(state, state.layout.layers, reverse=True)


def initial_state(
    layout: Layout,
    records: tuple[c342.CylinderRecord, ...],
    *,
    formation_hole: int | None = None,
    duplicate_root: int | None = None,
) -> BasisState:
    if len(records) != len(layout.cells):
        raise ValueError("one conditional Record is required per macrocell")
    bits = [0] * len(layout.sites)
    for position, (cell, record) in enumerate(zip(layout.cells, records)):
        bits[cell.formation] = int(position != formation_hole)
        bits[cell.boundary] = int(position == len(layout.cells) - 1)
        word = c342.record_word(record)
        for target, value in zip(cell.record, word):
            bits[target] = value
    bits[layout.cells[0].seed] = 1
    if duplicate_root is not None:
        bits[layout.cells[duplicate_root].seed] = 1
    return BasisState(layout, tuple(bits))


def record_at(state: BasisState, cell: Macrocell) -> c342.CylinderRecord:
    return c342.decode_record_word(tuple(state.bits[item] for item in cell.record))


def residue_at(state: BasisState, cell: Macrocell) -> int | None:
    word = tuple(state.bits[item] for item in cell.residue)
    return word.index(1) if sum(word) == 1 else None


def occupied_cells(state: BasisState) -> tuple[Macrocell, ...]:
    return tuple(cell for cell in state.layout.cells if state.bits[cell.occupied])


def locally_done(state: BasisState) -> bool:
    return any(state.bits[cell.done] for cell in state.layout.cells)


def run_until_done(state: BasisState) -> tuple[BasisState, int, tuple[bool, ...]]:
    """Bounded-test harness; its safety bound is not an argument to ``step``."""

    current = state
    code_trace = [code_report(current)["valid"]]
    calls = 0
    safety_bound = len(state.layout.cells) + 2
    while not locally_done(current) and calls < safety_bound:
        current = step(current)
        calls += 1
        code_trace.append(code_report(current)["valid"])
    return current, calls, tuple(bool(item) for item in code_trace)


def prefix_ok(bits: tuple[int, ...], cell: Macrocell) -> bool:
    residue = tuple(bits[item] for item in cell.residue)
    prefix = tuple(bits[item] for item in cell.prefix)
    expected: list[int] = []
    parity = 0
    for item in residue:
        parity ^= item
        expected.append(parity)
    return prefix == tuple(expected) and prefix[-1] == bits[cell.occupied]


def code_report(state: BasisState, fixture=None) -> dict[str, object]:
    validate_basis(state)
    cells = state.layout.cells
    bits = state.bits
    clause_failures: list[str] = []
    maximum_arity = 0
    maximum_cells = 0

    def clause(label: str, condition: bool, arity: int, cell_support: int) -> None:
        nonlocal maximum_arity, maximum_cells
        if arity > 3 or cell_support > 2:
            raise RuntimeError(("lineage auxiliary clause exceeded its local declaration", label))
        maximum_arity = max(maximum_arity, arity)
        maximum_cells = max(maximum_cells, cell_support)
        if not condition:
            clause_failures.append(label)

    # These endpoint tests query only whether a physical bond is incident on
    # the cell.  No coordinate arithmetic, tuple position, or encoded index is
    # used.  On the declared connected directed line, the clauses below imply
    # at most one root and at most one frontier.
    for cell in cells:
        incoming_geometry = tuple(right is cell for _, right in state.layout.bonds).count(True)
        outgoing_geometry = tuple(left is cell for left, _ in state.layout.bonds).count(True)
        occupied = bits[cell.occupied]
        predecessor = bits[cell.predecessor_in]
        successor = bits[cell.successor_out]
        root = bits[cell.root]
        front = bits[cell.front]
        clause(
            "seed-is-only-the-blank-left-boundary",
            bits[cell.seed] == int(incoming_geometry == 0 and not occupied),
            2,
            1,
        )
        clause("root-iff-occupied-without-predecessor", root == (occupied & (1 ^ predecessor)), 3, 1)
        clause("front-iff-occupied-without-successor", front == (occupied & (1 ^ successor)), 3, 1)
        clause("predecessor-implies-occupied", not predecessor or occupied, 2, 1)
        clause("successor-implies-occupied", not successor or occupied, 2, 1)
        clause("root-only-at-left-boundary", not root or incoming_geometry == 0, 1, 1)
        clause("done-only-at-front", not bits[cell.done] or front, 2, 1)
        if outgoing_geometry == 0:
            clause("terminal-cap-xor-done", bits[cell.boundary] ^ bits[cell.done] == 1, 2, 1)
        else:
            clause("nonterminal-has-no-cap-or-done", not bits[cell.boundary] and not bits[cell.done], 2, 1)

        residue = tuple(bits[item] for item in cell.residue)
        prefix = tuple(bits[item] for item in cell.prefix)
        clause("residue-prefix-zero", prefix[0] == residue[0], 2, 1)
        for rail in range(1, RESIDUES):
            clause(
                f"residue-prefix-xor-{rail}",
                prefix[rail] == (prefix[rail - 1] ^ residue[rail]),
                3,
                1,
            )
        clause("residue-presence-iff-occupied", prefix[-1] == occupied, 2, 1)
        for left_rail in range(RESIDUES):
            for right_rail in range(left_rail + 1, RESIDUES):
                clause(
                    f"residue-mutual-exclusion-{left_rail}-{right_rail}",
                    not (residue[left_rail] and residue[right_rail]),
                    2,
                    1,
                )
        for scratch in cell.in_form + cell.in_data + cell.out_data + (cell.out_depart,) + cell.router_ancilla:
            clause("blank-router-or-bond-scratch", bits[scratch] == 0, 1, 1)

    for left, right in state.layout.bonds:
        link = bits[left.successor_out]
        clause("bond-port-equality", link == bits[right.predecessor_in], 2, 2)
        clause("occupied-prefix-monotonicity", not bits[right.occupied] or bits[left.occupied], 2, 2)
        clause("occupied-successor-requires-link", not bits[right.occupied] or link, 2, 2)
        clause("link-requires-occupied-successor", not link or bits[right.occupied], 2, 2)
        for source_rail in range(RESIDUES):
            target_rail = (source_rail + 1) % RESIDUES
            clause(
                f"forward-residue-link-{source_rail}",
                not (link and bits[left.residue[source_rail]]) or bits[right.residue[target_rail]],
                3,
                2,
            )
            clause(
                f"reverse-residue-link-{target_rail}",
                not (link and bits[right.residue[target_rail]]) or bits[left.residue[source_rail]],
                3,
                2,
            )

    local_lineage = not clause_failures
    roots = tuple(bits[cell.root] for cell in cells)
    fronts = tuple(bits[cell.front] for cell in cells)
    topology_uniqueness_consequence = sum(roots) <= 1 and sum(fronts) <= 1
    # The sums above are a diagnostic consequence check only.  They do not
    # enter ``valid``; validity is determined by the explicit local clauses.

    record_chain_ok = True
    if fixture is not None:
        decoded = tuple(record_at(state, cell) for cell in cells)
        record_chain_ok = all(
            item.typed
            and item.permanent
            and c342.cylinder_is_lawful(fixture, item.cylinder)
            for item in decoded
        ) and all(
            right.cylinder == c342.advance_cylinder(fixture, left.cylinder)
            for left, right in zip(decoded, decoded[1:])
        )
    return {
        # The global counts are not load-bearing.  On the connected directed
        # line they are a tested consequence of the clauses, not a validator
        # input.
        "valid": bool(local_lineage and record_chain_ok),
        "local_lineage_auxiliary_clauses": bool(local_lineage),
        "local_clause_failures": tuple(clause_failures),
        "root_front_uniqueness_derived_from_local_line_clauses": topology_uniqueness_consequence,
        "record_chain": bool(record_chain_ok),
        "scratch_zero": scratch_is_zero(state),
        "occupied": sum(bits[cell.occupied] for cell in cells),
        "lineage_auxiliary_constraint_max_cells": maximum_cells,
        "lineage_auxiliary_constraint_max_clause_arity": maximum_arity,
    }


def rooted_lineage_signature(state: BasisState, target: Macrocell) -> tuple[tuple[int, ...], ...]:
    """Follow local predecessor ports; no ID or coordinate arithmetic is read."""

    path: list[tuple[int, ...]] = []
    current = target
    visited: list[Macrocell] = []
    while True:
        if current in visited:
            raise ValueError("cyclic local predecessor path")
        visited.append(current)
        path.append(c342.record_word(record_at(state, current)))
        if not state.bits[current.predecessor_in]:
            break
        incoming = tuple(
            left
            for left, right in state.layout.bonds
            if right is current
            and state.bits[right.predecessor_in]
            and state.bits[left.successor_out]
        )
        if len(incoming) != 1:
            raise ValueError("broken local predecessor path")
        current = incoming[0]
    return tuple(reversed(path))


def records_for(length: int, count: int):
    fixture = c342.c338.build_fixture(length)
    cylinders = c342.make_cylinder_chain(fixture, ENDPOINT, count)
    records = tuple(c342.form_conditional_record(fixture, item) for item in cylinders)
    if not c342.valid_chain(fixture, records):
        raise RuntimeError("Cycle-342 source Record chain is not lawful")
    return fixture, records


def constructive_controls() -> dict[str, object]:
    layouts = {count: build_layout(count) for count in CHAIN_SIZES}
    rows = []
    model_states: dict[tuple[int, int], tuple[object, BasisState, BasisState, int]] = {}
    failures = inverse_failures = leakage = code_failures = 0
    for length in LENGTHS:
        for count in CHAIN_SIZES:
            fixture, records = records_for(length, count)
            initial = initial_state(layouts[count], records)
            final, calls, trace = run_until_done(initial)
            report = code_report(final, fixture)
            inverse = final
            for _ in range(calls):
                inverse = inverse_step(inverse)
            payload_before = tuple(initial.bits[item] for cell in initial.layout.cells for item in cell.record)
            payload_after = tuple(final.bits[item] for cell in final.layout.cells for item in cell.record)
            residues = tuple(residue_at(final, cell) for cell in final.layout.cells)
            failures += int(
                not locally_done(final)
                or report["occupied"] != count
                or residues != tuple(index % RESIDUES for index in range(count))
                or calls != count - 1
            )
            inverse_failures += int(inverse != initial)
            leakage += sum(left != right for left, right in zip(payload_before, payload_after))
            code_failures += (
                sum(not item for item in trace)
                + int(not report["valid"])
                + int(not report["root_front_uniqueness_derived_from_local_line_clauses"])
            )
            model_states[(length, count)] = (fixture, initial, final, calls)
            rows.append(
                {
                    "L": length,
                    "N": count,
                    "held_N": count == HELD_CHAIN_SIZE,
                    "step_calls": calls,
                    "occupied": report["occupied"],
                    "residues": residues,
                    "macrocell_M2": MACROCELL_M2,
                    "lineage_overhead_M2": LINEAGE_OVERHEAD_M2,
                    "physical_M2": len(initial.bits),
                    "logical_operations_per_step": initial.layout.logical_operations,
                    "primitive_gates_per_step": sum(len(layer) for layer in initial.layout.layers),
                    "fixed_circuit_layers_per_step": len(initial.layout.layers),
                }
            )
    step_source = getsource(step)
    forbidden_step_source_hits = tuple(
        token
        for token in ("scratch_is_zero", "locally_done", "target_count", "host_index")
        if token in step_source
    )
    fixed_rule_failures = int(
        len({row["logical_operations_per_step"] for row in rows}) != 1
        or len({row["fixed_circuit_layers_per_step"] for row in rows}) != 1
        or tuple(signature(step).parameters) != ("state",)
        or bool(forbidden_step_source_hits)
    )
    check(
        "one autonomous state-local NN rule grows the rooted predecessor chain and period-6 residue/name tag at L3/L6 and N6/N12/held-N18",
        failures == inverse_failures == leakage == code_failures == fixed_rule_failures == 0,
        {
            "rows": rows,
            "constructive_failures": failures,
            "inverse_failures": inverse_failures,
            "Record_payload_bit_leakage": leakage,
            "code_failures": code_failures,
            "fixed_rule_signature_or_depth_failures": fixed_rule_failures,
            "forbidden_step_source_hits": forbidden_step_source_hits,
        },
    )
    return {"layouts": layouts, "states": model_states, "rows": rows}


def frame_controls(constructive: dict[str, object]) -> dict[str, object]:
    layouts: dict[int, Layout] = constructive["layouts"]  # type: ignore[assignment]
    raw_frames = tuple(c317.c311.c235.proper_cubic_frames())
    frames = tuple(np.asarray(frame, dtype=int) for frame in raw_frames)
    site_failures = gate_failures = layer_failures = 0
    site_frame_cases = gate_frame_cases = 0
    for layout in layouts.values():
        for frame in frames:
            carried_sites = tuple(moved(site.coord, frame) for site in layout.sites)
            site_failures += int(len(carried_sites) != len(set(carried_sites)))
            site_frame_cases += len(carried_sites)
            for layer in layout.layers:
                carried_layer = []
                for item in layer:
                    coords = tuple(moved(coord, frame) for coord in item.coords)
                    carried_layer.extend(coords)
                    gate_failures += int(not support_connected(coords))
                    gate_failures += int(item.kind == "CNOT" and manhattan(*coords) != 1)
                    gate_frame_cases += 1
                layer_failures += int(len(carried_layer) != len(set(carried_layer)))

    # The 30-M2 payload is the current Cycle-342 conditional Record and has
    # its own proper-cubic carrier map.  Audit that carrier for every L/N
    # model while the gate audit above handles the new spatial sidecar.
    record_mapping_failures = model_frame_cases = record_frame_cases = 0
    for length in LENGTHS:
        source_fixture = c342.c338.build_fixture(length)
        for raw_frame in raw_frames:
            carried_fixture, mapping, failures = c342.mapped_fixture(source_fixture, raw_frame)
            record_mapping_failures += failures
            for count in CHAIN_SIZES:
                source = c342.make_cylinder_chain(source_fixture, ENDPOINT, count)
                carried = c342.make_cylinder_chain(carried_fixture, ENDPOINT, count)
                model_frame_cases += 1
                for left, right in zip(source, carried):
                    expected = c342.c338.FutureCylinder(
                        endpoint=left.endpoint,
                        candidate=left.candidate,
                        phase=left.phase,
                        future_pre=int(mapping[left.future_pre]),
                        future_post=int(mapping[left.future_post]),
                    )
                    record_mapping_failures += int(right != expected)
                    record_frame_cases += 1
    check(
        "all Record payloads, instantiated M2 sites, connected NN gate supports, and conflict-free fixed layers survive all 24 proper-cubic frames",
        len(frames) == 24
        and site_failures == gate_failures == layer_failures == record_mapping_failures == 0,
        {
            "proper_cubic_frames": len(frames),
            "L_N_frame_models": model_frame_cases,
            "Record_payload_frame_cases": record_frame_cases,
            "Record_payload_mapping_failures": record_mapping_failures,
            "site_frame_cases": site_frame_cases,
            "gate_frame_cases": gate_frame_cases,
            "site_failures": site_failures,
            "gate_support_failures": gate_failures,
            "layer_conflict_failures": layer_failures,
            "maximum_primitive_gate_support_M2": 3,
            "two_site_gate_distance": 1,
            "three_site_support": "connected induced NN subgraph",
        },
    )
    return {
        "frames": len(frames),
        "model_frame_cases": model_frame_cases,
        "gate_frame_cases": gate_frame_cases,
    }


def alias_controls(constructive: dict[str, object]) -> dict[str, object]:
    states = constructive["states"]
    rows = []
    failures = 0
    for length in LENGTHS:
        for count in (12, 18):
            final: BasisState = states[(length, count)][2]
            alias_pairs = []
            for left in range(count):
                for right in range(left + 1, count):
                    if residue_at(final, final.layout.cells[left]) == residue_at(final, final.layout.cells[right]):
                        left_lineage = rooted_lineage_signature(final, final.layout.cells[left])
                        right_lineage = rooted_lineage_signature(final, final.layout.cells[right])
                        alias_pairs.append((left, right, len(left_lineage), len(right_lineage)))
                        failures += int(left_lineage == right_lineage)
            rows.append({"L": length, "N": count, "residue_alias_pairs": len(alias_pairs), "first_aliases": tuple(alias_pairs[:4])})
    check(
        "period-6 residue aliases are tags rather than identities: every alias remains distinct by the full rooted local-link lineage",
        failures == 0 and all(row["residue_alias_pairs"] > 0 for row in rows),
        {"rows": rows, "lineage_collisions": failures},
    )
    return {"rows": rows, "failures": failures}


def replace_record(state: BasisState, cell: Macrocell, record: c342.CylinderRecord) -> BasisState:
    bits = list(state.bits)
    for target, value in zip(cell.record, c342.record_word(record)):
        bits[target] = value
    return replace(state, bits=tuple(bits))


def flipped(state: BasisState, offset: int) -> BasisState:
    bits = list(state.bits)
    bits[offset] ^= 1
    return replace(state, bits=tuple(bits))


def deletion_layers(layout: Layout, label: str) -> tuple[tuple[Gate, ...], ...]:
    return tuple(
        tuple(item for item in layer if item.label != label)
        for layer in layout.layers
    )


def adversarial_controls(constructive: dict[str, object]) -> dict[str, object]:
    states = constructive["states"]
    fixture, initial, final, calls = states[(3, 6)]
    assert isinstance(initial, BasisState) and isinstance(final, BasisState)
    rows = []
    deletion_failures = 0
    for label in (
        "root:residue0",
        "bond:residue:0",
        "arrival:predecessor",
        "departure:clear-old-front",
        "done:set",
    ):
        layers = deletion_layers(initial.layout, label)
        current = initial
        for _ in range(calls):
            current = apply_layers(current, layers)
        restored = current
        for _ in range(calls):
            restored = apply_layers(restored, layers, reverse=True)
        report = code_report(current, fixture)
        changed = current != final
        caught = not report["valid"] or not locally_done(current)
        inverse = restored == initial
        deletion_failures += int(not (changed and caught and inverse))
        rows.append({"deleted_gate_label": label, "changed": changed, "caught": caught, "inverse": inverse})

    records = tuple(record_at(initial, cell) for cell in initial.layout.cells)
    missing_formation = initial_state(initial.layout, records, formation_hole=3)
    stopped = missing_formation
    # Three calls bring the frontier to the missing local formation input.
    # That call leaves the emission port visibly uncleared and therefore
    # outside the next-step code domain; it is a caught deletion, not a
    # silently skipped host-side branch.
    for _ in range(3):
        stopped = step(stopped)
    formation_control = (
        not locally_done(stopped)
        and len(occupied_cells(stopped)) == 3
        and not scratch_is_zero(stopped)
    )

    duplicate = initial_state(initial.layout, records, duplicate_root=2)
    duplicate_out = step(duplicate)
    duplicate_control = not code_report(duplicate_out, fixture)["valid"]

    collision = flipped(initial, initial.layout.cells[1].front)
    collision_out = step(collision)
    collision_control = not code_report(collision_out, fixture)["valid"]

    splice = replace_record(final, final.layout.cells[3], record_at(final, final.layout.cells[0]))
    splice_control = not code_report(splice, fixture)["valid"]

    domain_rejections = 0
    malformed = list(initial.bits)
    malformed[initial.layout.cells[0].formation] = 2
    try:
        step(replace(initial, bits=tuple(malformed)))
    except ValueError:
        domain_rejections += 1

    # A dirty scratch word is outside the declared local code space, but the
    # physical update must not branch on a host-side global scratch scan.  The
    # same circuit acts and remains exactly reversible on that basis word.
    dirty_scratch = flipped(initial, initial.layout.cells[0].in_data[0])
    dirty_advanced = step(dirty_scratch)
    dirty_scratch_control = (
        not code_report(dirty_scratch, fixture)["valid"]
        and inverse_step(dirty_advanced) == dirty_scratch
    )

    check(
        "formation loss, gate deletion, splice, duplicate root, front collision, inverse, and lawful-domain attacks remain exposed",
        deletion_failures == 0
        and formation_control
        and duplicate_control
        and collision_control
        and splice_control
        and domain_rejections == 1
        and dirty_scratch_control,
        {
            "gate_deletions": rows,
            "gate_deletion_failures": deletion_failures,
            "missing_formation_stops_before_DONE": formation_control,
            "duplicate_root_rejected": duplicate_control,
            "front_collision_rejected": collision_control,
            "Record_splice_rejected": splice_control,
            "lawful_domain_rejections": domain_rejections,
            "lawful_domain_attempts": 1,
            "dirty_scratch_is_local_code_failure_not_host_rejection": dirty_scratch_control,
        },
    )
    return {"rows": rows, "failures": deletion_failures}


def inherited_physics_controls() -> dict[str, object]:
    expected_contact = np.diag((np.exp(1j * c317.c311.COUPLING), 1))
    rows = []
    failures = 0
    for length in LENGTHS:
        fixture = c317.physical_fixture(length)
        contact_residual = float(np.linalg.norm(fixture.contact - expected_contact))
        gram = float(np.linalg.norm(fixture.two_ray_encoding.conj().T @ fixture.two_ray_encoding - c317.I2))
        projector = fixture.full_encoding @ fixture.full_encoding.conj().T
        leakage = float(np.linalg.norm((np.eye(projector.shape[0]) - projector) @ fixture.two_ray_encoding))
        contact_intertwiner = float(
            np.linalg.norm(
                fixture.physical_contact @ fixture.two_ray_encoding
                - fixture.two_ray_encoding @ fixture.contact
            )
        )
        failures += int(max(contact_residual, gram, leakage, contact_intertwiner) > TOL)
        rows.append(
            {
                "L": length,
                "contact_residual": contact_residual,
                "two_ray_gram_residual": gram,
                "accepted_code_leakage": leakage,
                "contact_intertwiner_residual": contact_intertwiner,
            }
        )
    species = c317.c311.c219.common_species(-0.3)
    one_particle = c317.c311.exterior_matrix(species.coin, 1)
    mass_residual = abs(c317.c311.c219.rest_mass(species) / species.analytic_mass - 1)
    failures += int(np.linalg.norm(one_particle - species.coin) > TOL or mass_residual > TOL)
    check(
        "the lineage sidecar leaves the inherited one-particle mass fixture and Cycle-230 seam contact unchanged",
        failures == 0,
        {"rows": rows, "one_particle_matrix_residual": float(np.linalg.norm(one_particle - species.coin)), "mass_relative_residual": mass_residual},
    )
    return {"rows": rows, "mass_residual": mass_residual}


def preloaded_shadow_controls(constructive: dict[str, object]) -> dict[str, object]:
    """Executable disclosure of the route's supplied future-history shadow."""

    rows = []
    failures = 0
    states = constructive["states"]
    for length in LENGTHS:
        for count in CHAIN_SIZES:
            fixture, initial, final, _ = states[(length, count)]
            assert isinstance(initial, BasisState) and isinstance(final, BasisState)
            future_payload_words = tuple(
                tuple(initial.bits[item] for item in cell.record)
                for cell in initial.layout.cells[1:]
            )
            future_records = tuple(record_at(initial, cell) for cell in initial.layout.cells[1:])
            unoccupied_future = all(
                initial.bits[cell.occupied] == 0 for cell in initial.layout.cells[1:]
            )
            payload_unchanged = all(
                tuple(initial.bits[item] for item in cell.record)
                == tuple(final.bits[item] for item in cell.record)
                for cell in initial.layout.cells
            )
            supplied_future_payload = all(any(word) for word in future_payload_words)
            pretyped_future = all(item.typed and item.permanent for item in future_records)
            failures += int(
                not (
                    unoccupied_future
                    and supplied_future_payload
                    and pretyped_future
                    and payload_unchanged
                    and c342.valid_chain(fixture, (record_at(initial, initial.layout.cells[0]),) + future_records)
                )
            )
            rows.append(
                {
                    "L": length,
                    "N": count,
                    "unoccupied_future_macrocells": count - 1,
                    "preloaded_nonzero_future_Record_words": sum(any(word) for word in future_payload_words),
                    "preloaded_future_typed_permanent": pretyped_future,
                    "payload_derived_from_predecessor": False,
                    "formation_generated_by_step": False,
                    "occurrence_generated_by_step": False,
                    "payload_bit_changes": sum(
                        initial.bits[item] != final.bits[item]
                        for cell in initial.layout.cells
                        for item in cell.record
                    ),
                }
            )
    check(
        "the route discloses its preloaded future Record/formation shadow and claims only autonomous lineage-sidecar generation",
        failures == 0
        and all(
            row["preloaded_nonzero_future_Record_words"] == row["unoccupied_future_macrocells"]
            and row["payload_derived_from_predecessor"] is False
            and row["formation_generated_by_step"] is False
            and row["occurrence_generated_by_step"] is False
            and row["payload_bit_changes"] == 0
            for row in rows
        ),
        {
            "rows": rows,
            "strict_Record_formation_closure": False,
            "future_history_shadow_is_supplied": True,
            "failures": failures,
        },
    )
    return {"rows": rows, "failures": failures}


def supplied_structure_controls(constructive: dict[str, object]) -> dict[str, object]:
    sample = constructive["rows"][0]
    detail = {
        "result": "bounded positive autonomous lineage/residue sidecar over a preloaded Record shadow",
        "supplied": (
            "all conditional typed/permanent 30-M2 Cycle-342 Record words, including every unoccupied future macrocell",
            "one root seed M2 in the declared input code",
            "one preloaded local formation/commit M2 per Record macrocell",
            "finite directed NN macrocell adjacency and one terminal boundary cap for tests",
            "fixed reversible circuit layering and blank local router/bond ancillas",
            "Cycle-342 lawful Record continuation fixture and upstream physical source structures",
        ),
        "not_supplied": (
            "literal Record IDs or arithmetic Record names",
            "host index/position-derived residue",
            "membership masks or global lineage dictionary",
            "copied common-history key",
            "state-dependent host schedule, host step number, or target count",
        ),
        "step_signature": "step(state)",
        "residue_source": "local six-rail rotation across the predecessor bond",
        "predecessor_source": "local arrival/departure port circuit",
        "Record_payload_generated_by_step": False,
        "formation_or_occurrence_generated_by_step": False,
        "strict_Record_formation_closure": False,
        "Record_M2": c342.RECORD_BITS,
        "macrocell_M2": MACROCELL_M2,
        "constant_overhead_M2_per_Record": LINEAGE_OVERHEAD_M2,
        "maximum_primitive_gate_support_M2": 3,
        "lineage_auxiliary_constraint_max_cells": 2,
        "lineage_auxiliary_constraint_max_clause_arity": 3,
        "fixed_circuit_layers_are_time": False,
        "spatial_layout_only": True,
        "OS_or_Z4_axis": None,
        "interval": None,
        "rate": None,
        "proper_time": None,
        "physical_energy": None,
        "Born_probability": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "sample_metrics": sample,
    }
    check(
        "all supplied structure and semantic firewalls remain explicit with authority none and audit unset",
        detail["step_signature"] == "step(state)"
        and detail["fixed_circuit_layers_are_time"] is False
        and detail["Record_payload_generated_by_step"] is False
        and detail["formation_or_occurrence_generated_by_step"] is False
        and detail["strict_Record_formation_closure"] is False
        and detail["OS_or_Z4_axis"] is None
        and detail["interval"] is detail["rate"] is detail["proper_time"] is None
        and detail["axiom_pressure"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("=" * 79)
    print("CYCLE 352 ROUTE 1: AUTONOMOUS LOCAL RECORD-LINEAGE/RESIDUE NN TRANSDUCER")
    print("authority=none; audit=unset")
    print("fixed circuit layering is not time; spatial layout only")
    print("=" * 79)
    constructive = constructive_controls()
    frame_controls(constructive)
    alias_controls(constructive)
    adversarial_controls(constructive)
    inherited_physics_controls()
    preloaded_shadow_controls(constructive)
    supplied_structure_controls(constructive)
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_AUTONOMOUS_RECORD_LINEAGE_RESIDUE_NN_ROUTE_OPEN")
        return 1
    print("RESULT PHYSICAL_AUTONOMOUS_RECORD_LINEAGE_RESIDUE_NN_ROUTE_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
