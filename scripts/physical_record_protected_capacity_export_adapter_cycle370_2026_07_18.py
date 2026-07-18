#!/usr/bin/env python3
"""Cycle 370: conditional Record-to-protected-capacity physical adapter.

This runner composes the unselected Cycle-364 formation hypothesis and its
Cycle-368 member/link metadata with the exact Cycle-335 append/export
permutations.  The common state contains an immutable source bank of
conditional Records and separate protected carrier replicas.  A carrier is
not a Record.  On the declared binary code space, a reversible nearest-
neighbor blank-bus copy stages one carrier from an already formed source
Record while every source lane remains fixed at every primitive boundary;
exact nearest-neighbor swaps append, translate, export, or exchange that
carrier with one explicitly supplied external boundary-refresh blank.

For ingress, append, export, and one external boundary refresh the runner tests

    E G_common = G_physical E,
    D E = identity,
    G_physical^{-1} G_physical E = E.

Protected occupancy is the Cycle-335 repetition triple 000/111.  Site,
content, predecessor, member, and reciprocal-link fields are carried without
reinterpretation.  Every physical primitive touches two adjacent M2 sites.
No reversible carrier copy is called a Record, no blank is created, Cycle 364
is not selected, and the realized-state reference supplies no content.
Ingress copies only declared computational-basis Record/metadata fields into
blank M2 carriers; it makes no arbitrary-state quantum-cloning claim.
Indefinite autonomous renewal is not built; that is a law/implementation
incompleteness, not an obstruction.  A supplied blank exchange is not called
renewal.  No no-go, minimum-content, or axiom-pressure claim is made.
Authority is none and audit is unset.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, replace
from pathlib import Path
import sys
from typing import Iterable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECORD_PROTECTED_CAPACITY_EXPORT_ADAPTER_CYCLE370_NOTE_2026-07-18.md"
)

import protected_recurrent_actual_history_selection_cycle335_2026_07_18 as c335
import physical_record_formation_link_genesis_counter_adapter_cycle368_2026_07_18 as c368


c364 = c368.c364
Coord = c364.Coord
Word = c364.Word
LENGTHS = (3, 6)
TRAIN_CASES = ((3, 6), (3, 12))
HELD_CASE = (6, 18)
CASES = TRAIN_CASES + (HELD_CASE,)
COORD_BITS = 7
COORD_OFFSET = 1 << (COORD_BITS - 1)
COORD_MIN = -COORD_OFFSET
COORD_MAX = COORD_OFFSET - 1
OCCUPANCY_BITS = 3
FIELD_BITS = 3 * COORD_BITS + c364.RECORD_BITS + 1 + 3 * COORD_BITS + 3
CARRIER_BITS = OCCUPANCY_BITS + FIELD_BITS
AUTHORITY = "none"
AUDIT = "unset"
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


def is_bit(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value in (0, 1)


@dataclass(frozen=True)
class CarrierReplica:
    """A protected movable replica; this value is deliberately not a Record."""

    record: c364.SiteContentRecord
    member: int
    predecessor_to_member: int
    member_to_predecessor: int


@dataclass(frozen=True)
class CapacityCommonState:
    """Common source/replica state for one bounded protected patch."""

    source: c368.LinkedFormationState
    ordered_sites: tuple[Coord, ...]
    external: CarrierReplica | None
    exported: CarrierReplica | None
    slots: tuple[CarrierReplica | None, ...]
    incoming: CarrierReplica | None


@dataclass(frozen=True)
class PhysicalPatch:
    """Binary M2 basis state on one connected framed nearest-neighbor tape."""

    fixture: object
    source_count: int
    length: int
    bits: tuple[int, ...]
    coords: tuple[Coord, ...]


Gate = tuple[str, int, int]


def integer_bits(value: int, width: int) -> tuple[int, ...]:
    if not isinstance(value, int) or isinstance(value, bool) or not 0 <= value < (1 << width):
        raise ValueError("integer is outside the fixed binary codec")
    return tuple((value >> shift) & 1 for shift in reversed(range(width)))


def bits_integer(bits: tuple[int, ...]) -> int:
    if any(not is_bit(value) for value in bits):
        raise ValueError("codec input is not binary")
    value = 0
    for item in bits:
        value = (value << 1) | item
    return value


def coordinate_bits(coord: Coord) -> tuple[int, ...]:
    if not c364.valid_coord(coord) or any(not COORD_MIN <= value <= COORD_MAX for value in coord):
        raise ValueError("Record coordinate is outside the declared signed seven-bit adapter domain")
    return tuple(
        bit
        for value in coord
        for bit in integer_bits(value + COORD_OFFSET, COORD_BITS)
    )


def bits_coordinate(bits: tuple[int, ...]) -> Coord:
    if len(bits) != 3 * COORD_BITS:
        raise ValueError("coordinate codec has the wrong width")
    values = tuple(
        bits_integer(bits[index * COORD_BITS : (index + 1) * COORD_BITS]) - COORD_OFFSET
        for index in range(3)
    )
    if not c364.valid_coord(values):
        raise ValueError("decoded coordinate left the cubic integer domain")
    return values  # type: ignore[return-value]


def envelope_map(state: c368.LinkedFormationState) -> dict[Coord, CarrierReplica]:
    records = c364.record_map(state.formation)
    members = c368.member_map(state)
    links = c368.link_map(state)
    output = {}
    for site, record in records.items():
        if record.predecessors:
            link = links[(record.predecessors[0], site)]
            forward = link.predecessor_to_member
            reverse = link.member_to_predecessor
        else:
            forward = reverse = 0
        output[site] = CarrierReplica(record, members[site].member, forward, reverse)
    return output


def validate_replica(fixture: object, replica: CarrierReplica) -> None:
    if not isinstance(replica, CarrierReplica):
        raise TypeError("protected carrier contains a non-replica value")
    c364.validate_record(replica.record)
    if not c364.payload_lawful(fixture, replica.record.content):
        raise ValueError("carrier content is not a fixture-lawful Cycle-342 word")
    linked = int(bool(replica.record.predecessors))
    if (
        len(replica.record.predecessors) > 1
        or not is_bit(replica.member)
        or replica.member != 1
        or not is_bit(replica.predecessor_to_member)
        or not is_bit(replica.member_to_predecessor)
        or replica.predecessor_to_member != linked
        or replica.member_to_predecessor != linked
    ):
        raise ValueError("carrier member/reciprocal-link metadata left the Cycle-368 code")
    coordinate_bits(replica.record.site)
    if replica.record.predecessors:
        coordinate_bits(replica.record.predecessors[0])


def validate_common(fixture: object, state: CapacityCommonState) -> None:
    if not isinstance(state, CapacityCommonState):
        raise TypeError("adapter requires one CapacityCommonState")
    c368.validate_linked_state(fixture, state.source)
    embedding = c368.CounterEmbedding(state.ordered_sites)
    c368.validate_embedding(state.source, embedding)
    if not isinstance(state.slots, tuple) or len(state.slots) not in LENGTHS:
        raise ValueError("protected capacity length must be trained L=3 or held L=6")
    allowed = envelope_map(state.source)
    for replica in (state.external, state.exported, *state.slots, state.incoming):
        if replica is None:
            continue
        validate_replica(fixture, replica)
        if allowed.get(replica.record.site) != replica:
            raise ValueError("carrier identity/content/link metadata is spliced from the source bank")


def encode_replica(fixture: object, replica: CarrierReplica | None) -> tuple[int, ...]:
    if replica is None:
        return (0,) * CARRIER_BITS
    validate_replica(fixture, replica)
    record = replica.record
    predecessor = record.predecessors[0] if record.predecessors else None
    fields = (
        coordinate_bits(record.site)
        + tuple(record.content)
        + (int(predecessor is not None),)
        + ((0,) * (3 * COORD_BITS) if predecessor is None else coordinate_bits(predecessor))
        + (replica.member, replica.predecessor_to_member, replica.member_to_predecessor)
    )
    if len(fields) != FIELD_BITS:
        raise RuntimeError("carrier field-width invariant failed")
    return (1, 1, 1) + fields


def decode_replica(fixture: object, bits: tuple[int, ...]) -> CarrierReplica | None:
    if len(bits) != CARRIER_BITS or any(not is_bit(value) for value in bits):
        raise ValueError("physical carrier is outside its binary width")
    protected = bits[:OCCUPANCY_BITS]
    fields = bits[OCCUPANCY_BITS:]
    if protected == (0, 0, 0):
        if any(fields):
            raise ValueError("blank protected occupancy carries leaked payload")
        return None
    if protected != (1, 1, 1):
        raise ValueError("protected occupancy repetition constraint failed")
    cursor = 0
    site = bits_coordinate(fields[cursor : cursor + 3 * COORD_BITS])
    cursor += 3 * COORD_BITS
    content = tuple(fields[cursor : cursor + c364.RECORD_BITS])
    cursor += c364.RECORD_BITS
    predecessor_present = fields[cursor]
    cursor += 1
    predecessor_field = tuple(fields[cursor : cursor + 3 * COORD_BITS])
    cursor += 3 * COORD_BITS
    if predecessor_present:
        predecessors = (bits_coordinate(predecessor_field),)
    else:
        if any(predecessor_field):
            raise ValueError("root replica leaks a predecessor coordinate")
        predecessors = ()
    member, forward, reverse = fields[cursor : cursor + 3]
    replica = CarrierReplica(
        c364.SiteContentRecord(site, content, predecessors),
        member,
        forward,
        reverse,
    )
    validate_replica(fixture, replica)
    return replica


def make_blank_common(
    fixture: object,
    source: c368.LinkedFormationState,
    ordered_sites: tuple[Coord, ...],
    length: int,
) -> CapacityCommonState:
    state = CapacityCommonState(source, ordered_sites, None, None, (None,) * length, None)
    validate_common(fixture, state)
    return state


def stage_common(fixture: object, state: CapacityCommonState, source_index: int) -> CapacityCommonState:
    validate_common(fixture, state)
    if state.incoming is not None or not 0 <= source_index < len(state.ordered_sites):
        raise ValueError("ingress needs one source index and one blank incoming carrier")
    replica = envelope_map(state.source)[state.ordered_sites[source_index]]
    output = replace(state, incoming=replica)
    validate_common(fixture, output)
    return output


def unstage_common(fixture: object, state: CapacityCommonState, source_index: int) -> CapacityCommonState:
    validate_common(fixture, state)
    if not 0 <= source_index < len(state.ordered_sites):
        raise ValueError("inverse ingress source index is outside the bank")
    replica = envelope_map(state.source)[state.ordered_sites[source_index]]
    if state.incoming != replica:
        raise ValueError("inverse ingress needs the matching staged carrier")
    output = replace(state, incoming=None)
    validate_common(fixture, output)
    return output


def append_common(fixture: object, state: CapacityCommonState, phase: int) -> CapacityCommonState:
    validate_common(fixture, state)
    if not 0 <= phase < len(state.slots):
        raise ValueError("append phase is outside the finite protected window")
    if state.incoming is None or state.slots[phase] is not None:
        raise ValueError("append needs one carrier replica and one fresh protected slot")
    slots = list(state.slots)
    slots[phase], incoming = state.incoming, slots[phase]
    output = replace(state, slots=tuple(slots), incoming=incoming)
    validate_common(fixture, output)
    return output


def export_common(fixture: object, state: CapacityCommonState) -> CapacityCommonState:
    validate_common(fixture, state)
    if state.exported is not None:
        raise ValueError("moving export requires one explicitly blank export boundary")
    output = replace(
        state,
        exported=state.slots[0],
        slots=state.slots[1:] + (state.incoming,),
        incoming=state.exported,
    )
    validate_common(fixture, output)
    return output


def refresh_common(fixture: object, state: CapacityCommonState) -> CapacityCommonState:
    validate_common(fixture, state)
    if state.external is not None or state.exported is None:
        raise ValueError("boundary refresh needs one supplied external blank and one occupied export")
    output = replace(state, external=state.exported, exported=state.external)
    validate_common(fixture, output)
    return output


def capacity_blocks(state: CapacityCommonState) -> tuple[CarrierReplica | None, ...]:
    return (
        (state.incoming,)
        + tuple(reversed(state.slots))
        + (state.exported, state.external)
    )


def source_bit_end(source_count: int) -> int:
    return source_count * CARRIER_BITS


def bus_bit_end(source_count: int) -> int:
    return 2 * source_count * CARRIER_BITS


def capacity_block_start(source_count: int) -> int:
    return 2 * source_count


def connected_coordinate_graph(coords: tuple[Coord, ...]) -> bool:
    if not coords or len(set(coords)) != len(coords):
        return False
    remaining = set(coords)
    frontier = [remaining.pop()]
    while frontier:
        current = frontier.pop()
        for axis in range(3):
            for delta in (-1, 1):
                candidate = list(current)
                candidate[axis] += delta
                neighbour = tuple(candidate)
                if neighbour in remaining:
                    remaining.remove(neighbour)
                    frontier.append(neighbour)
    return not remaining


def proper_frame(frame: np.ndarray) -> bool:
    return any(
        np.array_equal(frame, candidate)
        for candidate in c368.c360.c353.proper_cubic_frames()
    )


def encode_physical(
    fixture: object,
    state: CapacityCommonState,
    frame: np.ndarray,
) -> PhysicalPatch:
    """E: fixed source bank, blank NN bus grid, and movable capacity tape."""

    validate_common(fixture, state)
    if not isinstance(frame, np.ndarray) or frame.shape != (3, 3) or not proper_frame(frame):
        raise ValueError("physical tape requires one of the 24 proper-cubic frames")
    count = len(state.ordered_sites)
    source = envelope_map(state.source)
    source_bits = tuple(
        bit
        for site in state.ordered_sites
        for bit in encode_replica(fixture, source[site])
    )
    bus_bits = (0,) * (count * CARRIER_BITS)
    movable_bits = tuple(
        bit
        for block in capacity_blocks(state)
        for bit in encode_replica(fixture, block)
    )
    bits = source_bits + bus_bits + movable_bits

    def rotated(raw: Coord) -> Coord:
        return tuple(int(value) for value in frame @ np.array(raw, dtype=int))

    source_coords = tuple(
        rotated((source_index, lane, 1))
        for source_index in range(count)
        for lane in range(CARRIER_BITS)
    )
    bus_coords = tuple(
        rotated((source_index, lane, 0))
        for source_index in range(count)
        for lane in range(CARRIER_BITS)
    )
    capacity_coords = tuple(
        rotated(
            (
                count,
                lane if block % 2 == 0 else CARRIER_BITS - 1 - lane,
                -block,
            )
        )
        for block in range(len(state.slots) + 3)
        for lane in range(CARRIER_BITS)
    )
    coords = source_coords + bus_coords + capacity_coords
    if not connected_coordinate_graph(coords):
        raise RuntimeError("source/bus/capacity M2 layout is not one connected patch")
    return PhysicalPatch(fixture, len(state.ordered_sites), len(state.slots), bits, coords)


def decode_physical(state: PhysicalPatch) -> CapacityCommonState:
    """D: exact endpoint decoder; static scaffold metadata supplies no payload."""

    if (
        not isinstance(state, PhysicalPatch)
        or state.source_count < 1
        or state.length not in LENGTHS
        or len(state.bits) != (2 * state.source_count + state.length + 3) * CARRIER_BITS
        or len(state.coords) != len(state.bits)
        or any(not is_bit(value) for value in state.bits)
        or any(not c364.valid_coord(coord) for coord in state.coords)
        or not connected_coordinate_graph(state.coords)
    ):
        raise ValueError("physical state is outside the connected binary patch domain")
    source_end = source_bit_end(state.source_count)
    bus_end = bus_bit_end(state.source_count)
    if any(state.bits[source_end:bus_end]):
        raise ValueError("nearest-neighbor ingress bus is not blank at the decode boundary")
    source_blocks = tuple(
        decode_replica(state.fixture, state.bits[index : index + CARRIER_BITS])
        for index in range(0, source_end, CARRIER_BITS)
    )
    if any(item is None for item in source_blocks):
        raise ValueError("immutable source bank contains a blank carrier")
    source_replicas = tuple(item for item in source_blocks if item is not None)
    records = c364.FormationState(c364.canonical(tuple(item.record for item in source_replicas)))
    members = c368.canonical_members(tuple(
        c368.MemberMetadata(item.record.site, item.member) for item in source_replicas
    ))
    links = c368.canonical_links(tuple(
        c368.ReciprocalLink(
            item.record.predecessors[0],
            item.record.site,
            item.predecessor_to_member,
            item.member_to_predecessor,
        )
        for item in source_replicas
        if item.record.predecessors
    ))
    source = c368.LinkedFormationState(records, members, links)
    ordered_sites = tuple(item.record.site for item in source_replicas)
    blocks = tuple(
        decode_replica(state.fixture, state.bits[index : index + CARRIER_BITS])
        for index in range(bus_end, len(state.bits), CARRIER_BITS)
    )
    cursor = 0
    incoming = blocks[cursor]
    cursor += 1
    slots = tuple(reversed(blocks[cursor : cursor + state.length]))
    cursor += state.length
    exported, external = blocks[cursor : cursor + 2]
    output = CapacityCommonState(source, ordered_sites, external, exported, slots, incoming)
    validate_common(state.fixture, output)
    return output


def adjacent_block_swap_schedule(left_block: int) -> tuple[Gate, ...]:
    start = left_block * CARRIER_BITS
    gates = []
    for _ in range(CARRIER_BITS):
        gates.extend(
            ("swap", target, target + 1)
            for target in range(start, start + 2 * CARRIER_BITS - 1)
        )
    return tuple(gates)


def block_transposition_macros(left_block: int, right_block: int) -> tuple[int, ...]:
    if not 0 <= left_block < right_block:
        raise ValueError("block transposition needs ordered distinct endpoints")
    return (
        tuple(range(left_block, right_block))
        + tuple(reversed(range(left_block, right_block - 1)))
    )


def stage_schedule(source_block: int, source_count: int) -> tuple[Gate, ...]:
    """Remote basis CNOT through a blank bus; source lanes are controls only."""

    if not 0 <= source_block < source_count:
        raise ValueError("source carrier is outside the fixed source bank")
    gates = []
    for lane in range(CARRIER_BITS):
        source = source_block * CARRIER_BITS + lane
        bus = tuple(
            (source_count + index) * CARRIER_BITS + lane
            for index in range(source_block, source_count)
        )
        target = 2 * source_count * CARRIER_BITS + lane
        gates.append(("cx", source, bus[0]))
        gates.extend(("cx", left, right) for left, right in zip(bus, bus[1:]))
        gates.append(("cx", bus[-1], target))
        gates.extend(("cx", left, right) for left, right in reversed(tuple(zip(bus, bus[1:]))))
        gates.append(("cx", source, bus[0]))
    return tuple(gates)


def execute_schedule(
    state: PhysicalPatch,
    gates: Iterable[Gate],
) -> tuple[PhysicalPatch, dict[str, int]]:
    """Execute and audit every primitive boundary for fixed-source invariance."""

    gate_tuple = tuple(gates)
    values = list(state.bits)
    source_end = source_bit_end(state.source_count)
    bus_end = bus_bit_end(state.source_count)
    initial_source = tuple(values[:source_end])
    nonzero_bus = {
        index for index in range(source_end, bus_end) if values[index]
    }
    source_mutations = source_target_gates = bus_cross_lane_leakage = support_failures = 0
    binary_failures = 0
    maximum_nonzero_bus = len(nonzero_bus)
    for kind, left, right in gate_tuple:
        if (
            kind not in ("swap", "cx")
            or not 0 <= left < len(values)
            or not 0 <= right < len(values)
            or c364.distance(state.coords[left], state.coords[right]) != 1
        ):
            support_failures += 1
            raise ValueError("physical gate is not a connected nearest-neighbor M2 primitive")
        if kind == "swap":
            source_target_gates += int(left < source_end or right < source_end)
            values[left], values[right] = values[right], values[left]
        else:
            source_target_gates += int(right < source_end)
            values[right] ^= values[left]
        for index in (left, right):
            if index < source_end and values[index] != initial_source[index]:
                source_mutations += 1
            if source_end <= index < bus_end:
                if values[index]:
                    nonzero_bus.add(index)
                else:
                    nonzero_bus.discard(index)
        active_lanes = {
            (index - source_end) % CARRIER_BITS for index in nonzero_bus
        }
        bus_cross_lane_leakage += int(len(active_lanes) > 1)
        maximum_nonzero_bus = max(maximum_nonzero_bus, len(nonzero_bus))
        binary_failures += int(values[left] not in (0, 1) or values[right] not in (0, 1))
    output = replace(state, bits=tuple(values))
    detail = {
        "primitive_boundaries_audited": len(gate_tuple),
        "source_lane_mutations": source_mutations,
        "source_target_gates": source_target_gates,
        "bus_cross_lane_leakage": bus_cross_lane_leakage,
        "bus_endpoint_nonzero_M2": len(nonzero_bus),
        "maximum_transient_nonzero_bus_M2": maximum_nonzero_bus,
        "support_failures": support_failures,
        "binary_failures": binary_failures,
    }
    return output, detail


def apply_schedule(state: PhysicalPatch, gates: Iterable[Gate]) -> PhysicalPatch:
    output, audit = execute_schedule(state, gates)
    if (
        audit["source_lane_mutations"]
        or audit["source_target_gates"]
        or audit["bus_cross_lane_leakage"]
        or audit["support_failures"]
        or audit["binary_failures"]
    ):
        raise RuntimeError(("primitive trace violated source/bus code", audit))
    return output


def apply_macros(state: PhysicalPatch, macros: tuple[int, ...]) -> PhysicalPatch:
    output = state
    for left_block in macros:
        output = apply_schedule(output, adjacent_block_swap_schedule(left_block))
    return output


def macro_gate_sequence(macros: tuple[int, ...]) -> tuple[Gate, ...]:
    return tuple(
        gate
        for left_block in macros
        for gate in adjacent_block_swap_schedule(left_block)
    )


def physical_stage(state: PhysicalPatch, source_index: int) -> tuple[PhysicalPatch, tuple[Gate, ...]]:
    common = decode_physical(state)
    expected = stage_common(state.fixture, common, source_index)
    gates = stage_schedule(source_index, state.source_count)
    output = apply_schedule(state, gates)
    if decode_physical(output) != expected:
        raise RuntimeError("physical ingress left the exact common endpoint")
    return output, gates


def physical_append(state: PhysicalPatch, phase: int) -> tuple[PhysicalPatch, tuple[int, ...]]:
    common = decode_physical(state)
    expected = append_common(state.fixture, common, phase)
    incoming = capacity_block_start(state.source_count)
    target = incoming + 1 + (state.length - 1 - phase)
    macros = block_transposition_macros(incoming, target)
    output = apply_macros(state, macros)
    if decode_physical(output) != expected:
        raise RuntimeError("physical append left the exact common endpoint")
    return output, macros


def physical_export(state: PhysicalPatch) -> tuple[PhysicalPatch, tuple[int, ...]]:
    common = decode_physical(state)
    expected = export_common(state.fixture, common)
    incoming = capacity_block_start(state.source_count)
    exported = incoming + state.length + 1
    macros = tuple(reversed(range(incoming, exported)))
    output = apply_macros(state, macros)
    if decode_physical(output) != expected:
        raise RuntimeError("physical export left the exact common endpoint")
    return output, macros


def physical_refresh(state: PhysicalPatch) -> tuple[PhysicalPatch, tuple[int, ...]]:
    common = decode_physical(state)
    expected = refresh_common(state.fixture, common)
    exported = capacity_block_start(state.source_count) + state.length + 1
    macros = (exported,)
    output = apply_macros(state, macros)
    if decode_physical(output) != expected:
        raise RuntimeError("physical boundary refresh left the exact common endpoint")
    return output, macros


def inverse_gates(state: PhysicalPatch, gates: tuple[Gate, ...]) -> PhysicalPatch:
    return apply_schedule(state, reversed(gates))


def inverse_macros(state: PhysicalPatch, macros: tuple[int, ...]) -> PhysicalPatch:
    return apply_macros(state, tuple(reversed(macros)))


def occupancy(replica: CarrierReplica | None) -> tuple[int, int, int]:
    return (0, 0, 0) if replica is None else (1, 1, 1)


def export_projection(state: CapacityCommonState) -> c335.ExportState:
    return c335.ExportState(
        occupancy(state.incoming),
        tuple(occupancy(item) for item in state.slots),
        occupancy(state.exported),
    )


def append_projection(
    state: CapacityCommonState,
) -> tuple[tuple[tuple[int, int, int], ...], tuple[int, int, int]]:
    return tuple(occupancy(item) for item in state.slots), occupancy(state.incoming)


def resource_ledger(state: CapacityCommonState) -> dict[str, object]:
    movable = (state.external, state.exported, *state.slots, state.incoming)
    identities = Counter(
        item.record.site
        for item in movable
        if item is not None
    )
    return {
        "source_Records": len(state.source.formation.records),
        "movable_carriers": len(movable),
        "occupied_replicas": sum(item is not None for item in movable),
        "blank_carriers": sum(item is None for item in movable),
        "identity_site_multiset": tuple(sorted(identities.items())),
    }


def transform_common(
    state: CapacityCommonState,
    frame: np.ndarray,
    mapping: object,
) -> CapacityCommonState:
    transformed_source = c368.transform_linked_state(state.source, frame, mapping)
    transformed = envelope_map(transformed_source)

    def carrier(item: CarrierReplica | None) -> CarrierReplica | None:
        if item is None:
            return None
        site = c364.transform_coord(item.record.site, frame, (0, 0, 0))
        return transformed[site]

    output = CapacityCommonState(
        transformed_source,
        tuple(c364.transform_coord(site, frame, (0, 0, 0)) for site in state.ordered_sites),
        carrier(state.external),
        carrier(state.exported),
        tuple(carrier(item) for item in state.slots),
        carrier(state.incoming),
    )
    return output


def physical_intertwiner_controls() -> dict[str, object]:
    frames = c368.c360.c353.proper_cubic_frames()
    cases = held_cases = 0
    mapping_failures = roundtrip_failures = intertwiner_failures = 0
    inverse_failures = leakage_failures = locality_failures = 0
    primitive_boundaries = source_trace_failures = bus_trace_failures = 0
    gate_counts = Counter()
    for length, count in CASES:
        fixture = c364.c342.c338.build_fixture(length)
        source, _states, _proposals, _writes = c368.build_linked_chain(fixture, count)
        order = tuple((index, 0, 0) for index in range(count))
        base_blank = make_blank_common(fixture, source, order, length)
        replicas = envelope_map(source)
        base_full = replace(
            base_blank,
            slots=tuple(replicas[order[index]] for index in range(length)),
            incoming=replicas[order[length]],
        )
        for frame in frames:
            rotated_fixture, mapping, failures = c364.c342.mapped_fixture(fixture, frame)
            mapping_failures += failures
            blank = transform_common(base_blank, frame, mapping)
            full = transform_common(base_full, frame, mapping)

            encoded_blank = encode_physical(rotated_fixture, blank, frame)
            roundtrip_failures += int(decode_physical(encoded_blank) != blank)

            staged = stage_common(rotated_fixture, blank, count - 1)
            physical_staged, ingress_gates = physical_stage(encoded_blank, count - 1)
            audited_stage, ingress_audit = execute_schedule(encoded_blank, ingress_gates)
            intertwiner_failures += int(audited_stage != physical_staged)
            primitive_boundaries += ingress_audit["primitive_boundaries_audited"]
            source_trace_failures += (
                ingress_audit["source_lane_mutations"]
                + ingress_audit["source_target_gates"]
            )
            bus_trace_failures += (
                ingress_audit["bus_cross_lane_leakage"]
                + ingress_audit["bus_endpoint_nonzero_M2"]
            )
            intertwiner_failures += int(
                physical_staged != encode_physical(rotated_fixture, staged, frame)
            )
            recovered = inverse_gates(physical_staged, ingress_gates)
            inverse_failures += int(recovered != encoded_blank)

            appended = append_common(rotated_fixture, staged, length - 1)
            physical_appended, append_macros = physical_append(physical_staged, length - 1)
            _audited_append, append_audit = execute_schedule(
                physical_staged, macro_gate_sequence(append_macros)
            )
            primitive_boundaries += append_audit["primitive_boundaries_audited"]
            source_trace_failures += (
                append_audit["source_lane_mutations"]
                + append_audit["source_target_gates"]
            )
            bus_trace_failures += (
                append_audit["bus_cross_lane_leakage"]
                + append_audit["bus_endpoint_nonzero_M2"]
            )
            intertwiner_failures += int(
                physical_appended != encode_physical(rotated_fixture, appended, frame)
            )
            projected_append = c335.append_step(
                append_projection(staged)[0],
                length - 1,
                append_projection(staged)[1],
            )
            intertwiner_failures += int(append_projection(appended) != projected_append)
            inverse_failures += int(
                inverse_macros(physical_appended, append_macros) != physical_staged
            )

            encoded_full = encode_physical(rotated_fixture, full, frame)
            exported = export_common(rotated_fixture, full)
            physical_exported, export_macros = physical_export(encoded_full)
            _audited_export, export_audit = execute_schedule(
                encoded_full, macro_gate_sequence(export_macros)
            )
            primitive_boundaries += export_audit["primitive_boundaries_audited"]
            source_trace_failures += (
                export_audit["source_lane_mutations"]
                + export_audit["source_target_gates"]
            )
            bus_trace_failures += (
                export_audit["bus_cross_lane_leakage"]
                + export_audit["bus_endpoint_nonzero_M2"]
            )
            intertwiner_failures += int(
                physical_exported != encode_physical(rotated_fixture, exported, frame)
            )
            inverse_failures += int(
                inverse_macros(physical_exported, export_macros) != encoded_full
            )
            projected = c335.export_step(export_projection(full))
            intertwiner_failures += int(export_projection(exported) != projected)

            refreshed = refresh_common(rotated_fixture, exported)
            physical_refreshed, refresh_macros = physical_refresh(physical_exported)
            _audited_refresh, refresh_audit = execute_schedule(
                physical_exported, macro_gate_sequence(refresh_macros)
            )
            primitive_boundaries += refresh_audit["primitive_boundaries_audited"]
            source_trace_failures += (
                refresh_audit["source_lane_mutations"]
                + refresh_audit["source_target_gates"]
            )
            bus_trace_failures += (
                refresh_audit["bus_cross_lane_leakage"]
                + refresh_audit["bus_endpoint_nonzero_M2"]
            )
            intertwiner_failures += int(
                physical_refreshed != encode_physical(rotated_fixture, refreshed, frame)
            )
            inverse_failures += int(
                inverse_macros(physical_refreshed, refresh_macros) != physical_exported
            )

            endpoints = (
                physical_staged,
                physical_appended,
                physical_exported,
                physical_refreshed,
            )
            for endpoint in endpoints:
                try:
                    decoded = decode_physical(endpoint)
                    leakage_failures += int(decoded.source != blank.source)
                    leakage_failures += int(any(not is_bit(value) for value in endpoint.bits))
                except (TypeError, ValueError):
                    leakage_failures += 1
            locality_failures += sum(
                c364.distance(encoded_blank.coords[left], encoded_blank.coords[right]) != 1
                for _kind, left, right in ingress_gates
            )
            gate_counts["ingress_M2_gates"] += len(ingress_gates)
            gate_counts["append_carrier_swaps"] += len(append_macros)
            gate_counts["export_carrier_swaps"] += len(export_macros)
            gate_counts["external_refresh_carrier_swaps"] += len(refresh_macros)
            cases += 1
            held_cases += int((length, count) == HELD_CASE)
    detail = {
        "L_by_N_by_frame_cases": cases,
        "train_cases": TRAIN_CASES,
        "held_case": HELD_CASE,
        "held_L6_N18_frame_cases": held_cases,
        "proper_cubic_frames": len(frames),
        "payload_mapping_failures": mapping_failures,
        "encoder_decoder_roundtrip_failures": roundtrip_failures,
        "E_G_common_equals_G_physical_E_failures": intertwiner_failures,
        "exact_inverse_failures": inverse_failures,
        "code_or_source_leakage_failures": leakage_failures,
        "connected_NN_failures": locality_failures,
        "primitive_gate_boundaries_audited": primitive_boundaries,
        "source_lane_trace_failures": source_trace_failures,
        "bus_trace_or_endpoint_leakage": bus_trace_failures,
        "carrier_width_M2": CARRIER_BITS,
        "held_patch_M2": (2 * HELD_CASE[1] + HELD_CASE[0] + 3) * CARRIER_BITS,
        "maximum_primitive_support_M2": 2,
        "accumulated_gate_counts": dict(gate_counts),
    }
    check(
        "ingress, append, export, and one supplied external-blank refresh exactly intertwine on a connected NN M2 tape in all 24 frames",
        len(frames) == 24
        and cases == len(CASES) * len(frames)
        and held_cases == len(frames)
        and mapping_failures == roundtrip_failures == 0
        and intertwiner_failures == inverse_failures == 0
        and leakage_failures == locality_failures == 0
        and primitive_boundaries > 0
        and source_trace_failures == bus_trace_failures == 0
        and CARRIER_BITS == 79,
        detail,
    )
    return detail


def trajectory_controls() -> dict[str, object]:
    rows = []
    failures = 0
    for length, count in ((3, 6), (6, 18)):
        fixture = c364.c342.c338.build_fixture(length)
        source, _states, _proposals, _writes = c368.build_linked_chain(fixture, count)
        order = tuple((index, 0, 0) for index in range(count))
        common = make_blank_common(fixture, source, order, length)
        target = envelope_map(source)[order[-1]]
        physical = encode_physical(fixture, common, np.eye(3, dtype=int))
        common = stage_common(fixture, common, count - 1)
        physical, ingress_gates = physical_stage(physical, count - 1)
        staged_physical = physical
        occupancy_history = [resource_ledger(common)["occupied_replicas"]]
        identity_residual = 0
        export_macros = []
        for _step in range(length + 1):
            before_projection = export_projection(common)
            common = export_common(fixture, common)
            physical, macros = physical_export(physical)
            export_macros.append(macros)
            failures += int(decode_physical(physical) != common)
            failures += int(
                export_projection(common) != c335.export_step(before_projection)
            )
            occupancy_history.append(resource_ledger(common)["occupied_replicas"])
            for carrier in (common.exported, *common.slots, common.incoming):
                if carrier is not None:
                    identity_residual += int(carrier != target)
        source_after = envelope_map(common.source)[order[-1]]
        failures += int(common.exported != target or source_after != target)
        recovered = physical
        for macros in reversed(export_macros):
            recovered = inverse_macros(recovered, macros)
        failures += int(recovered != staged_physical)
        recovered = inverse_gates(recovered, ingress_gates)
        blank = make_blank_common(fixture, source, order, length)
        failures += int(recovered != encode_physical(fixture, blank, np.eye(3, dtype=int)))
        rows.append(
            {
                "L": length,
                "source_N": count,
                "held": length == 6,
                "steps_from_ingress_to_export": length + 1,
                "occupancy_history": tuple(occupancy_history),
                "site_content_member_link_residual": identity_residual,
                "source_Record_unchanged": source_after == target,
                "exported_replica_matches_source": common.exported == target,
                "full_inverse_residual": int(
                    recovered != encode_physical(fixture, blank, np.eye(3, dtype=int))
                ),
            }
        )
    check(
        "one newly staged carrier enters, crosses every protected slot, and exports with exact site/content/member/link identity while its source Record remains immutable",
        failures == 0
        and all(
            row["occupancy_history"] == (1,) * (row["L"] + 2)
            and row["site_content_member_link_residual"] == 0
            and row["source_Record_unchanged"]
            and row["exported_replica_matches_source"]
            and row["full_inverse_residual"] == 0
            for row in rows
        ),
        rows,
    )
    return {"rows": rows, "failures": failures}


def exhaustion_and_one_supplied_boundary_refresh_controls() -> dict[str, object]:
    rows = []
    failures = 0
    for length, count in ((3, 6), (6, 18)):
        fixture = c364.c342.c338.build_fixture(length)
        source, _states, _proposals, _writes = c368.build_linked_chain(fixture, count)
        order = tuple((index, 0, 0) for index in range(count))
        common = make_blank_common(fixture, source, order, length)
        physical = encode_physical(fixture, common, np.eye(3, dtype=int))
        ledger = [("initial_supplied_capacity", resource_ledger(common))]
        for phase in range(length):
            common = stage_common(fixture, common, phase)
            physical, _ = physical_stage(physical, phase)
            staged_blanks = resource_ledger(common)["blank_carriers"]
            common = append_common(fixture, common, phase)
            physical, _ = physical_append(physical, phase)
            failures += int(resource_ledger(common)["blank_carriers"] != staged_blanks)
        ledger.append(("finite_window_full", resource_ledger(common)))

        common = stage_common(fixture, common, length)
        physical, _ = physical_stage(physical, length)
        ledger.append(("first_over_capacity_replica_staged", resource_ledger(common)))
        logical_rejected = physical_rejected = False
        try:
            append_common(fixture, common, 0)
        except ValueError:
            logical_rejected = True
        try:
            physical_append(physical, 0)
        except ValueError:
            physical_rejected = True

        before_export = resource_ledger(common)
        common = export_common(fixture, common)
        physical, _ = physical_export(physical)
        after_export = resource_ledger(common)
        ledger.append(("existing_export_blank_relocated", after_export))
        blank_export_delta = after_export["blank_carriers"] - before_export["blank_carriers"]

        before_refresh = resource_ledger(common)
        common = refresh_common(fixture, common)
        physical, _ = physical_refresh(physical)
        after_refresh = resource_ledger(common)
        ledger.append(("supplied_external_blank_exchanged", after_refresh))
        refresh_blank_delta = after_refresh["blank_carriers"] - before_refresh["blank_carriers"]

        common = stage_common(fixture, common, length + 1)
        physical, _ = physical_stage(physical, length + 1)
        after_second_stage = resource_ledger(common)
        ledger.append(("next_replica_consumes_incoming_blank", after_second_stage))
        common = export_common(fixture, common)
        physical, _ = physical_export(physical)
        ledger.append(("one_external_refresh_then_next_export_complete", resource_ledger(common)))
        second_refresh_rejected = False
        try:
            refresh_common(fixture, common)
        except ValueError:
            second_refresh_rejected = True

        decoded = decode_physical(physical)
        failures += int(decoded != common)
        failures += int(not logical_rejected or not physical_rejected)
        failures += int(blank_export_delta != 0 or refresh_blank_delta != 0)
        failures += int(
            after_second_stage["blank_carriers"]
            != after_refresh["blank_carriers"] - 1
        )
        failures += int(not second_refresh_rejected)
        rows.append(
            {
                "L": length,
                "source_N": count,
                "held": length == 6,
                "first_over_capacity_append_rejected": logical_rejected and physical_rejected,
                "export_blank_net_creation": blank_export_delta,
                "external_refresh_net_blank_creation": refresh_blank_delta,
                "next_replica_blank_consumption": (
                    after_refresh["blank_carriers"] - after_second_stage["blank_carriers"]
                ),
                "second_refresh_without_another_supplied_blank_rejected": second_refresh_rejected,
                "ledger": ledger,
            }
        )
    check(
        "the first exhaustion boundary rejects append; export and one external-blank refresh proceed with zero net blank creation",
        failures == 0
        and all(
            row["first_over_capacity_append_rejected"]
            and row["export_blank_net_creation"] == 0
            and row["external_refresh_net_blank_creation"] == 0
            and row["next_replica_blank_consumption"] == 1
            and row["second_refresh_without_another_supplied_blank_rejected"]
            for row in rows
        ),
        rows,
    )
    return {"rows": rows, "failures": failures}


def deletion_splice_domain_and_leakage_controls() -> dict[str, object]:
    fixture = c364.c342.c338.build_fixture(3)
    source, _states, _proposals, _writes = c368.build_linked_chain(fixture, 6)
    order = tuple((index, 0, 0) for index in range(6))
    replicas = envelope_map(source)
    blank = make_blank_common(fixture, source, order, 3)
    physical_blank = encode_physical(fixture, blank, np.eye(3, dtype=int))
    expected_staged = stage_common(fixture, blank, 5)
    ingress_gates = stage_schedule(5, 6)
    first_cx = next(index for index, gate in enumerate(ingress_gates) if gate[0] == "cx")
    deleted_ingress = ingress_gates[:first_cx] + ingress_gates[first_cx + 1 :]
    ingress_deletion_detected = False
    try:
        decode_physical(apply_schedule(physical_blank, deleted_ingress))
    except (ValueError, RuntimeError):
        ingress_deletion_detected = True

    long_bus_gates = stage_schedule(0, 6)
    bus_start = source_bit_end(6)
    bus_end = bus_bit_end(6)
    deleted_bus_index = next(
        index
        for index, (_kind, left, right) in enumerate(long_bus_gates)
        if bus_start <= left < bus_end and bus_start <= right < bus_end
    )
    deleted_bus_gates = (
        long_bus_gates[:deleted_bus_index] + long_bus_gates[deleted_bus_index + 1 :]
    )
    bus_deletion_visible = False
    attacked_bus, attacked_bus_audit = execute_schedule(physical_blank, deleted_bus_gates)
    try:
        decoded_bus = decode_physical(attacked_bus)
        bus_deletion_visible = decoded_bus != stage_common(fixture, blank, 0)
    except ValueError:
        bus_deletion_visible = True
    nominal_bus, nominal_bus_audit = execute_schedule(physical_blank, long_bus_gates)

    full = replace(
        blank,
        slots=tuple(replicas[order[index]] for index in range(3)),
        incoming=replicas[order[3]],
    )
    physical_full = encode_physical(fixture, full, np.eye(3, dtype=int))
    nominal_export, export_macros = physical_export(physical_full)
    export_deletion_survivors = 0
    for deleted in range(len(export_macros)):
        attacked = apply_macros(
            physical_full,
            export_macros[:deleted] + export_macros[deleted + 1 :],
        )
        export_deletion_survivors += int(attacked == nominal_export)

    append_state = replace(
        blank,
        slots=(None, replicas[order[1]], replicas[order[2]]),
        incoming=replicas[order[3]],
    )
    physical_append_input = encode_physical(fixture, append_state, np.eye(3, dtype=int))
    nominal_append, append_macros = physical_append(physical_append_input, 0)
    append_deletion_survivors = 0
    for deleted in range(len(append_macros)):
        attacked = apply_macros(
            physical_append_input,
            append_macros[:deleted] + append_macros[deleted + 1 :],
        )
        append_deletion_survivors += int(attacked == nominal_append)

    staged_physical, complete_ingress = physical_stage(physical_blank, 5)
    inverse_failures = int(inverse_gates(staged_physical, complete_ingress) != physical_blank)
    inverse_failures += int(inverse_macros(nominal_export, export_macros) != physical_full)
    inverse_failures += int(
        inverse_macros(nominal_append, append_macros) != physical_append_input
    )

    corrupted_bits = list(physical_full.bits)
    corrupted_bits[0] ^= 1
    protected_fault_rejected = False
    try:
        decode_physical(replace(physical_full, bits=tuple(corrupted_bits)))
    except ValueError:
        protected_fault_rejected = True

    wrong_replica = replace(replicas[order[3]], member=0)
    invalid_calls = (
        lambda: validate_common(fixture, replace(blank, incoming=wrong_replica)),
        lambda: stage_common(fixture, expected_staged, 4),
        lambda: append_common(fixture, full, 0),
        lambda: export_common(fixture, replace(full, exported=replicas[order[4]])),
        lambda: refresh_common(fixture, full),
        lambda: encode_physical(fixture, blank, -np.eye(3, dtype=int)),
        lambda: decode_physical(replace(physical_full, bits=physical_full.bits[:-1])),
        lambda: decode_physical(replace(physical_full, coords=physical_full.coords[:-1])),
        lambda: coordinate_bits((64, 0, 0)),
        lambda: validate_common(fixture, replace(blank, ordered_sites=tuple(reversed(order)))),
    )
    domain_rejections = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError):
            domain_rejections += 1

    source_splice = stage_common(fixture, blank, 4)
    splice_visible = source_splice.incoming != expected_staged.incoming
    leakage_failures = 0
    for endpoint in (staged_physical, nominal_export, nominal_append):
        decoded = decode_physical(endpoint)
        leakage_failures += int(decoded.source != source)
        leakage_failures += int(any(not is_bit(value) for value in endpoint.bits))
    detail = {
        "ingress_occupancy_CNOT_deletion_rejected": ingress_deletion_detected,
        "internal_bus_CNOT_deletion_visible": bus_deletion_visible,
        "deleted_bus_endpoint_nonzero_M2": attacked_bus_audit["bus_endpoint_nonzero_M2"],
        "nominal_bus_source_lane_mutations": nominal_bus_audit["source_lane_mutations"],
        "nominal_bus_source_target_gates": nominal_bus_audit["source_target_gates"],
        "nominal_bus_endpoint_nonzero_M2": nominal_bus_audit["bus_endpoint_nonzero_M2"],
        "nominal_bus_target_correct": decode_physical(nominal_bus) == stage_common(fixture, blank, 0),
        "export_carrier_swap_deletions": len(export_macros),
        "export_deletion_lawful_survivors": export_deletion_survivors,
        "append_carrier_swap_deletions": len(append_macros),
        "append_deletion_lawful_survivors": append_deletion_survivors,
        "protected_single_replica_fault_rejected": protected_fault_rejected,
        "source_identity_splice_visible": splice_visible,
        "domain_rejections": domain_rejections,
        "domain_attempts": len(invalid_calls),
        "inverse_failures": inverse_failures,
        "source_or_binary_leakage_failures": leakage_failures,
    }
    check(
        "ingress/append/export deletions, identity splicing, protected faults, malformed domains, leakage, and exact inverses are controlled",
        ingress_deletion_detected
        and bus_deletion_visible
        and attacked_bus_audit["bus_endpoint_nonzero_M2"] > 0
        and nominal_bus_audit["source_lane_mutations"] == 0
        and nominal_bus_audit["source_target_gates"] == 0
        and nominal_bus_audit["bus_endpoint_nonzero_M2"] == 0
        and decode_physical(nominal_bus) == stage_common(fixture, blank, 0)
        and export_deletion_survivors == append_deletion_survivors == 0
        and protected_fault_rejected
        and splice_visible
        and domain_rejections == len(invalid_calls)
        and inverse_failures == leakage_failures == 0,
        detail,
    )
    return detail


def note_contract_controls() -> dict[str, object]:
    if not NOTE.exists():
        check("the Cycle-370 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    text = " ".join(
        NOTE.read_text(encoding="utf-8").lower().replace("`", "").split()
    )
    required = (
        "authority: none",
        "audit: unset",
        "cycle 364 remains an unselected",
        "carrier replica is not called a record",
        "no arbitrary-state quantum-cloning claim",
        "source bank is immutable at every primitive gate boundary",
        "every source lane is a cnot control only",
        "bus is uncomputed to blank",
        "primitive gate boundaries audited",
        "internal bus-cnot deletion survivors",
        "boundary refresh, not renewal",
        "net blank creation 0",
        "indefinite autonomous renewal is not built",
        "law/implementation incompleteness, not an obstruction",
        "all 24 proper-cubic frames",
        "trained (l=3,n=6) and (l=3,n=12)",
        "held (l=6,n=18)",
        "maximum primitive support",
        "the realized-state reference supplies no content",
        "no recurrence, physical layer, gate count, append phase, or export count is time",
        "no blank count is promoted to energy, stress, active source, or gravity",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the exact finite result, external-refresh boundary, and semantic firewall",
        not missing,
        missing,
    )
    return {"missing": missing}


def inventory_and_semantic_controls() -> dict[str, object]:
    inventory = {
        "result": "exact bounded common-state and connected-NN M2 protected-capacity adapter",
        "conditional_on_unselected_Cycle364": True,
        "Cycle364_selected_framework_law": False,
        "source_Record": "immutable conditional Cycle-364 site/content Record with Cycle-368 metadata",
        "movable_value": "protected carrier replica, not a Record",
        "ingress": "reversible basis-copy CNOT schedule through an explicit blank NN bus into one supplied blank carrier",
        "ingress_domain": "declared computational-basis Record/metadata codewords with a blank M2 target",
        "arbitrary_state_quantum_cloning_claim": False,
        "source_Record_lanes_are_CNOT_controls_only": True,
        "source_Record_lane_target_gates": 0,
        "bus_endpoint_leakage": 0,
        "protected_occupancy": "Cycle-335 000/111 repetition triple",
        "carried_fields": (
            "signed bounded source site",
            "complete 30-M2 content word",
            "optional predecessor site",
            "member bit",
            "two reciprocal-link bits",
        ),
        "encoder": "E(common source plus replicas, frame) to connected M2 tape",
        "decoder": "D recovers source and every replica exactly on the endpoint code space",
        "intertwiners": (
            "E G_ingress_common = G_ingress_physical E",
            "E G_append_common = G_append_physical E",
            "E G_export_common = G_export_physical E",
            "E G_refresh_common = G_refresh_physical E",
            "D E = identity",
            "G_physical_inverse G_physical E = E",
        ),
        "physical_embedding": "connected source-bank/blank-bus/capacity-tape patch in every proper-cubic frame",
        "carrier_width_M2": CARRIER_BITS,
        "maximum_primitive_support_M2": 2,
        "source_plus_bus_overhead": "158 M2 per source Record, constant per source",
        "movable_carrier_overhead": "79 M2 per movable carrier",
        "held_patch_M2": (2 * HELD_CASE[1] + HELD_CASE[0] + 3) * CARRIER_BITS,
        "supplied_structure": (
            "unselected Cycle-364 formation hypothesis and fixture",
            "Cycle-368 simultaneous member/link metadata and ordered linear embedding",
            "seven-bit signed coordinate codec domain",
            "finite L=3 or L=6 capacity and physical tape layout",
            "one 79-M2 blank nearest-neighbor bus column per source Record",
            "append phase, export boundary, fixed gate schedules, and proper-cubic frame",
            "one initial export blank, one external boundary-refresh blank, and blank ingress carriers",
            "choice of which already formed source Record is copied",
        ),
        "realized_state_reference_supplies_content": False,
        "copy_is_Record": False,
        "pointer_or_carrier_is_Record": False,
        "blank_capacity_created": False,
        "supplied_external_refresh_is_autonomous_renewal": False,
        "indefinite_autonomous_renewal": None,
        "law_or_implementation_incompleteness": "additional external sectors/blanks and an autonomous renewal law are not built",
        "shared_substrate_obstruction": False,
        "no_go": None,
        "minimum_content_claim": None,
        "axiom_pressure": None,
        "recurrence_or_layer_or_count_is_time": False,
        "source_energy_or_gravity_promotion": None,
        "actual_history_sampler": None,
        "Born_weights": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    text = " ".join(__doc__.split()).lower()
    required = (
        "unselected cycle-364",
        "carrier is not a record",
        "no blank is created",
        "realized-state reference supplies no content",
        "law/implementation incompleteness",
        "not an obstruction",
        "no no-go, minimum-content, or axiom-pressure claim",
        "authority is none",
        "audit is unset",
    )
    check(
        "the supplied structure, conditional status, resource boundary, and semantic firewall are explicit",
        all(item in text for item in required)
        and inventory["conditional_on_unselected_Cycle364"]
        and inventory["Cycle364_selected_framework_law"] is False
        and inventory["copy_is_Record"] is False
        and inventory["arbitrary_state_quantum_cloning_claim"] is False
        and inventory["source_Record_lanes_are_CNOT_controls_only"]
        and inventory["source_Record_lane_target_gates"] == 0
        and inventory["bus_endpoint_leakage"] == 0
        and inventory["pointer_or_carrier_is_Record"] is False
        and inventory["blank_capacity_created"] is False
        and inventory["supplied_external_refresh_is_autonomous_renewal"] is False
        and inventory["indefinite_autonomous_renewal"] is None
        and inventory["shared_substrate_obstruction"] is False
        and inventory["no_go"] is inventory["minimum_content_claim"] is None
        and inventory["axiom_pressure"] is None
        and inventory["recurrence_or_layer_or_count_is_time"] is False
        and inventory["source_energy_or_gravity_promotion"] is None
        and inventory["actual_history_sampler"] is inventory["Born_weights"] is None
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 370: CONDITIONAL RECORD / PROTECTED-CAPACITY PHYSICAL ADAPTER")
    print("authority=none; audit=unset; Cycle-364 unselected; carrier copy is not a Record")
    intertwiners = physical_intertwiner_controls()
    trajectory = trajectory_controls()
    boundary = exhaustion_and_one_supplied_boundary_refresh_controls()
    attacks = deletion_splice_domain_and_leakage_controls()
    note = note_contract_controls()
    inventory = inventory_and_semantic_controls()
    check(
        "Cycle 370 gives a bounded physical Record-to-capacity adapter through one supplied boundary refresh without promoting it to a selected or autonomously renewable law",
        intertwiners["E_G_common_equals_G_physical_E_failures"] == 0
        and trajectory["failures"] == 0
        and boundary["failures"] == 0
        and attacks["inverse_failures"] == 0
        and not note["missing"]
        and inventory["Cycle364_selected_framework_law"] is False
        and inventory["indefinite_autonomous_renewal"] is None
        and inventory["shared_substrate_obstruction"] is False,
        {
            "disposition": "bounded positive exact common-state/physical-capacity composition",
            "train_cases": TRAIN_CASES,
            "held_case": HELD_CASE,
            "proper_cubic_frames": intertwiners["proper_cubic_frames"],
            "supplied_boundary_refresh": "one external blank exchanged exactly; net blank creation zero",
            "indefinite_autonomous_renewal": "not built; law/implementation incompleteness",
            "obstruction": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_RECORD_PROTECTED_CAPACITY_EXPORT_ADAPTER_OPEN")
        return 1
    print("RESULT PHYSICAL_RECORD_PROTECTED_CAPACITY_EXPORT_ADAPTER_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
