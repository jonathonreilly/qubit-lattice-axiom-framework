#!/usr/bin/env python3
"""Cycle 365 Route 2: migrating/invariant-fact Record-formation candidate.

This runner states a falsifiable downstream hypothesis; it neither derives a
formation law from the framework axioms nor proposes axiom language.  It uses
the same explicit faithful-close, predecessor-readiness, common-provenance,
fresh-target, and complete 30-bit payload interface as Cycle 364.  Under this
candidate only the output equivalence class is called a conditional Record.
Raw reversible carrier, bond, witness, and payload M2 bits are not Records.

The physical substrate is a finite connected nearest-neighbour M2 strip.  A
lawful recoding touches one source carrier, their intervening bond, and one
fresh target carrier.  It writes an invariant 30-bit/root/episode segment,
clears the source, and writes the target.  Local segment continuity generates
an explicit worldline quotient: old and new carrier facts are one identity,
not two.  A cleared source may be reused by a distinct root, unlike the
Cycle-364 site-tethered candidate.

The possibility of migrating permanence was already left open by the
canonical law-completeness contract; novelty here is the exact bounded local
candidate quotient and its anti-merge, deletion, splice, corruption,
concurrency, and migration discriminators.  Candidate-law selection,
Born/statistics, metric time, renewable unbounded capacity, and full-lattice
completion remain open.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_event_to_append_commit_candidate_cycle326_2026_07_18 as c326
import physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18 as c342
import physical_autonomous_record_payload_faithful_close_nn_route_cycle361_2026_07_18 as c361
import physical_fixed_global_common_fork_record_lineage_nn_route_cycle362_2026_07_18 as c362


Coord = tuple[int, int, int]
Word = tuple[int, ...]
Identity = Coord
RECORD_BITS = c342.RECORD_BITS
INTERFACE_BITS = 4
WIDTH = 40
CONTENT_LANES = tuple(range(RECORD_BITS))
CARRIER_PRESENT_LANE = 30
CARRIER_ROOT_ORIGIN_LANE = 31
CARRIER_ARRIVAL_DIRECTION_LANE = 32
CARRIER_INTERFACE_LANES = (33, 34, 35, 36)
CARRIER_ROOT_SLOT_LANE = 37
CARRIER_ENDPOINT_LANES = (38, 39)
BOND_USED_LANE = 30
BOND_DIRECTION_LANE = 31
BOND_SOURCE_ORIGIN_LANE = 32
BOND_PREDECESSOR_DIRECTION_LANE = 33
BOND_INTERFACE_LANES = (34, 35, 36, 37)
BOND_ROOT_SLOT_LANE = 38
LENGTHS = (3, 6)
TRAIN_SIZES = (6, 12)
HELD_SIZE = 18
SIZES = TRAIN_SIZES + (HELD_SIZE,)
MAX_PREDECESSORS = 2
LOCAL_RADIUS = 1
AUTHORITY = "none"
AUDIT = "unset"
LAW_NAME = "Cycle-365 migrating invariant-fact close-gated formation hypothesis"
RECORD_TYPE = "conditional framework migrating/invariant-fact Record"
CLOSE_SOURCE = "Cycle-361 faithful-close candidate interface"
READINESS_SOURCE = "Cycle-326 fresh/predecessor readiness interface"
PROVENANCE_SOURCE = "Cycle-362 common-fork provenance acceptance interface"
COMPLETENESS_PRIOR = "CANONICAL_LAW_COMPLETENESS_CONTRACT_NOTE_2026-07-13.md"
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


def bit(value: object) -> bool:
    return value in (0, 1) and not isinstance(value, bool) or isinstance(value, bool)


def valid_coord(coord: object) -> bool:
    return (
        isinstance(coord, tuple)
        and len(coord) == 3
        and all(isinstance(item, int) and not isinstance(item, bool) for item in coord)
    )


def distance(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


@dataclass(frozen=True)
class FaithfulCloseInterface:
    site: Coord
    payload: Word
    close_candidate: int
    source: str = CLOSE_SOURCE


@dataclass(frozen=True)
class ReadinessInterface:
    site: Coord
    predecessors: tuple[Coord, ...]
    predecessors_ready: int
    fresh: int
    source: str = READINESS_SOURCE


@dataclass(frozen=True)
class ProvenanceInterface:
    site: Coord
    payload: Word
    predecessors: tuple[Coord, ...]
    accepted: int
    independent_confirmations: int = 1
    source: str = PROVENANCE_SOURCE


@dataclass(frozen=True)
class FormationProposal:
    site: Coord
    payload: Word
    payload_present: Word
    close: FaithfulCloseInterface
    readiness: ReadinessInterface
    provenance: ProvenanceInterface


@dataclass(frozen=True)
class IdentitySeed:
    local_root_slot: int
    source: str = "supplied fresh local root-endpoint slot"


@dataclass(frozen=True)
class Site:
    coord: Coord
    role: str
    cell: int
    lane: int


@dataclass(frozen=True)
class CarrierSites:
    index: int
    sites: tuple[int, ...]


@dataclass(frozen=True)
class BondSites:
    index: int
    sites: tuple[int, ...]


@dataclass(frozen=True)
class Layout:
    fixture: c342.c338.RouteFixture
    size: int
    sites: tuple[Site, ...]
    carriers: tuple[CarrierSites, ...]
    bonds: tuple[BondSites, ...]
    anchors: tuple[Coord, ...]
    frame: tuple[int, ...]


@dataclass(frozen=True)
class BasisState:
    layout: Layout
    bits: tuple[int, ...]


@dataclass(frozen=True)
class CarrierView:
    content: Word
    present: int
    root_origin: int
    arrival_direction: int
    interface: tuple[int, int, int, int]
    root_slot: int
    endpoint_markers: tuple[int, int]


@dataclass(frozen=True)
class BondView:
    content: Word
    used: int
    direction: int
    source_origin: int
    predecessor_direction: int
    interface: tuple[int, int, int, int]
    root_slot: int


@dataclass(frozen=True)
class InvariantFactRecord:
    identity: Identity
    content: Word
    fact_members: tuple[tuple[str, int], ...]
    active_carriers: tuple[int, ...]
    record_type: str = RECORD_TYPE
    law: str = LAW_NAME


@dataclass(frozen=True)
class FormationAnswer:
    state: BasisState
    formed: InvariantFactRecord | None
    status: str
    conditions: tuple[tuple[str, bool], ...]


@dataclass(frozen=True)
class RecodingRequest:
    source: int
    destination: int
    proposal: FormationProposal


@dataclass(frozen=True)
class RecodingAnswer:
    state: BasisState
    status: str
    conditions: tuple[tuple[str, bool], ...]


@dataclass(frozen=True)
class BatchAnswer:
    state: BasisState
    statuses: tuple[str, ...]
    overlaps: tuple[tuple[int, int, str], ...]


def proper_frame(frame: np.ndarray) -> bool:
    matrix = np.asarray(frame, dtype=int)
    return matrix.shape == (3, 3) and any(
        np.array_equal(matrix, item) for item in c362.c353.proper_cubic_frames()
    )


def build_layout(
    fixture: c342.c338.RouteFixture,
    size: int,
    frame: np.ndarray,
) -> Layout:
    if not isinstance(size, int) or isinstance(size, bool) or size < 2:
        raise ValueError("the bounded migrating patch needs at least two carriers")
    if not proper_frame(frame):
        raise ValueError("the migrating patch needs one proper-cubic frame")
    matrix = np.asarray(frame, dtype=int)
    sites: list[Site] = []
    carriers = []
    bonds = []
    for column in range(2 * size - 1):
        role = "carrier" if column % 2 == 0 else "bond"
        cell = column // 2
        installed = []
        for lane in range(WIDTH):
            raw = (column, lane, 0)
            coord = c362.c353.rotated(raw, matrix)
            installed.append(len(sites))
            site_role = (
                "root-endpoint"
                if role == "carrier" and lane in CARRIER_ENDPOINT_LANES
                else role
            )
            sites.append(Site(coord, site_role, cell, lane))
        if role == "carrier":
            carriers.append(CarrierSites(cell, tuple(installed)))
        else:
            bonds.append(BondSites(cell, tuple(installed)))
    anchors = tuple(c362.c353.rotated((index, 0, 0), matrix) for index in range(size))
    if len({item.coord for item in sites}) != len(sites):
        raise RuntimeError("migrating physical M2 coordinates overlap")
    return Layout(
        fixture,
        size,
        tuple(sites),
        tuple(carriers),
        tuple(bonds),
        anchors,
        tuple(int(item) for item in matrix.flat),
    )


def blank_state(layout: Layout) -> BasisState:
    return BasisState(layout, (0,) * len(layout.sites))


def validate_state(state: BasisState) -> None:
    if not isinstance(state, BasisState):
        raise TypeError("the candidate law needs one finite physical BasisState")
    if len(state.bits) != len(state.layout.sites):
        raise ValueError("physical M2 width does not match the installed patch")
    if any(not bit(item) for item in state.bits):
        raise ValueError("physical candidate state must be a binary M2 basis word")


def validate_proposal(layout: Layout, proposal: FormationProposal) -> None:
    if not isinstance(proposal, FormationProposal):
        raise TypeError("formation needs one explicit FormationProposal")
    if proposal.site not in layout.anchors:
        raise ValueError("proposal target is outside the finite carrier patch")
    if (
        not isinstance(proposal.payload, tuple)
        or len(proposal.payload) != RECORD_BITS
        or any(not bit(item) for item in proposal.payload)
        or not isinstance(proposal.payload_present, tuple)
        or len(proposal.payload_present) != RECORD_BITS
        or any(not bit(item) for item in proposal.payload_present)
    ):
        raise ValueError("proposal is outside the complete binary 30-M2 domain")
    if not isinstance(proposal.close, FaithfulCloseInterface):
        raise TypeError("missing explicit Cycle-361 close interface")
    if not isinstance(proposal.readiness, ReadinessInterface):
        raise TypeError("missing explicit Cycle-326 readiness interface")
    if not isinstance(proposal.provenance, ProvenanceInterface):
        raise TypeError("missing explicit Cycle-362 provenance interface")
    if (
        not valid_coord(proposal.close.site)
        or len(proposal.close.payload) != RECORD_BITS
        or any(not bit(item) for item in proposal.close.payload)
        or not bit(proposal.close.close_candidate)
        or proposal.close.source != CLOSE_SOURCE
    ):
        raise ValueError("Cycle-361 close interface is outside its declared domain")
    predecessors = proposal.readiness.predecessors
    if (
        proposal.readiness.site not in layout.anchors
        or not isinstance(predecessors, tuple)
        or len(predecessors) > MAX_PREDECESSORS
        or len(set(predecessors)) != len(predecessors)
        or proposal.site in predecessors
        or any(item not in layout.anchors for item in predecessors)
        or any(distance(proposal.site, item) > LOCAL_RADIUS for item in predecessors)
        or not bit(proposal.readiness.predecessors_ready)
        or not bit(proposal.readiness.fresh)
        or proposal.readiness.source != READINESS_SOURCE
    ):
        raise ValueError("Cycle-326 readiness interface is outside its local domain")
    if (
        not valid_coord(proposal.provenance.site)
        or len(proposal.provenance.payload) != RECORD_BITS
        or any(not bit(item) for item in proposal.provenance.payload)
        or not isinstance(proposal.provenance.predecessors, tuple)
        or len(proposal.provenance.predecessors) > MAX_PREDECESSORS
        or any(item not in layout.anchors for item in proposal.provenance.predecessors)
        or not bit(proposal.provenance.accepted)
        or not isinstance(proposal.provenance.independent_confirmations, int)
        or isinstance(proposal.provenance.independent_confirmations, bool)
        or not 0 <= proposal.provenance.independent_confirmations <= 3
        or proposal.provenance.source != PROVENANCE_SOURCE
    ):
        raise ValueError("Cycle-362 provenance interface is outside its declared domain")


def carrier_view(state: BasisState, index: int) -> CarrierView:
    sites = state.layout.carriers[index].sites
    values = state.bits
    return CarrierView(
        tuple(values[sites[lane]] for lane in CONTENT_LANES),
        values[sites[CARRIER_PRESENT_LANE]],
        values[sites[CARRIER_ROOT_ORIGIN_LANE]],
        values[sites[CARRIER_ARRIVAL_DIRECTION_LANE]],
        tuple(values[sites[lane]] for lane in CARRIER_INTERFACE_LANES),  # type: ignore[arg-type]
        values[sites[CARRIER_ROOT_SLOT_LANE]],
        tuple(values[sites[lane]] for lane in CARRIER_ENDPOINT_LANES),  # type: ignore[arg-type]
    )


def bond_view(state: BasisState, index: int) -> BondView:
    sites = state.layout.bonds[index].sites
    values = state.bits
    return BondView(
        tuple(values[sites[lane]] for lane in CONTENT_LANES),
        values[sites[BOND_USED_LANE]],
        values[sites[BOND_DIRECTION_LANE]],
        values[sites[BOND_SOURCE_ORIGIN_LANE]],
        values[sites[BOND_PREDECESSOR_DIRECTION_LANE]],
        tuple(values[sites[lane]] for lane in BOND_INTERFACE_LANES),  # type: ignore[arg-type]
        values[sites[BOND_ROOT_SLOT_LANE]],
    )


def carrier_blank(state: BasisState, index: int) -> bool:
    sites = state.layout.carriers[index].sites
    return all(state.bits[sites[lane]] == 0 for lane in range(CARRIER_ROOT_SLOT_LANE + 1))


def bond_blank(state: BasisState, index: int) -> bool:
    return all(state.bits[site] == 0 for site in state.layout.bonds[index].sites)


def write_carrier(
    values: list[int],
    carrier: CarrierSites,
    content: Word,
    *,
    root_origin: int,
    arrival_direction: int,
    root_slot: int = 0,
) -> None:
    for lane in range(CARRIER_ROOT_SLOT_LANE + 1):
        values[carrier.sites[lane]] = 0
    for lane, value in enumerate(content):
        values[carrier.sites[lane]] = value
    values[carrier.sites[CARRIER_PRESENT_LANE]] = 1
    values[carrier.sites[CARRIER_ROOT_ORIGIN_LANE]] = root_origin
    values[carrier.sites[CARRIER_ARRIVAL_DIRECTION_LANE]] = arrival_direction
    for lane in CARRIER_INTERFACE_LANES:
        values[carrier.sites[lane]] = 1
    values[carrier.sites[CARRIER_ROOT_SLOT_LANE]] = root_slot


def write_bond(
    values: list[int],
    bond: BondSites,
    content: Word,
    *,
    direction: int,
    source_origin: int,
    predecessor_direction: int,
    root_slot: int,
) -> None:
    for site in bond.sites:
        values[site] = 0
    for lane, value in enumerate(content):
        values[bond.sites[lane]] = value
    values[bond.sites[BOND_USED_LANE]] = 1
    values[bond.sites[BOND_DIRECTION_LANE]] = direction
    values[bond.sites[BOND_SOURCE_ORIGIN_LANE]] = source_origin
    values[bond.sites[BOND_PREDECESSOR_DIRECTION_LANE]] = predecessor_direction
    for lane in BOND_INTERFACE_LANES:
        values[bond.sites[lane]] = 1
    values[bond.sites[BOND_ROOT_SLOT_LANE]] = root_slot


def payload_lawful(layout: Layout, payload: Word) -> bool:
    try:
        record = c342.decode_record_word(payload)
    except (TypeError, ValueError):
        return False
    return (
        record.typed
        and record.permanent
        and c342.cylinder_is_lawful(layout.fixture, record.cylinder)
    )


def proposal(
    layout: Layout,
    target: int,
    payload: Word,
    predecessors: tuple[int, ...] = (),
    *,
    complete: int = 1,
    close: int = 1,
    ready: int = 1,
    provenance: int = 1,
    fresh: int = 1,
    confirmations: int = 1,
) -> FormationProposal:
    site = layout.anchors[target]
    predecessor_sites = tuple(layout.anchors[index] for index in predecessors)
    return FormationProposal(
        site,
        payload,
        (complete,) * RECORD_BITS,
        FaithfulCloseInterface(site, payload, close),
        ReadinessInterface(site, predecessor_sites, ready, fresh),
        ProvenanceInterface(
            site,
            payload,
            predecessor_sites,
            provenance,
            confirmations,
        ),
    )


def proposal_conditions(
    state: BasisState,
    item: FormationProposal,
    *,
    source: int | None,
) -> tuple[tuple[str, bool], ...]:
    validate_state(state)
    validate_proposal(state.layout, item)
    target = state.layout.anchors.index(item.site)
    source_ready = source is None or (
        0 <= source < state.layout.size
        and carrier_view(state, source).present == 1
        and payload_lawful(state.layout, carrier_view(state, source).content)
        and item.readiness.predecessors == (state.layout.anchors[source],)
    )
    complete = all(item.payload_present) and payload_lawful(state.layout, item.payload)
    faithful_close = bool(
        item.close.close_candidate
        and item.close.site == item.site
        and item.close.payload == item.payload
    )
    predecessor_readiness = bool(
        item.readiness.predecessors_ready
        and item.readiness.site == item.site
        and item.readiness.predecessors == item.provenance.predecessors
        and (not item.readiness.predecessors if source is None else source_ready)
    )
    provenance_acceptance = bool(
        item.provenance.accepted
        and item.provenance.site == item.site
        and item.provenance.payload == item.payload
        and item.provenance.predecessors == item.readiness.predecessors
    )
    fresh_site = bool(item.readiness.fresh and carrier_blank(state, target))
    return (
        ("complete_payload", bool(complete)),
        ("faithful_close", faithful_close),
        ("predecessor_readiness", predecessor_readiness),
        ("provenance_acceptance", provenance_acceptance),
        ("fresh_site", fresh_site),
    )


def occupied_fact_nodes(state: BasisState) -> dict[tuple[str, int], Word]:
    nodes: dict[tuple[str, int], Word] = {}
    for index in range(state.layout.size):
        view = carrier_view(state, index)
        if view.present:
            nodes[("carrier", index)] = view.content
    for index in range(state.layout.size - 1):
        view = bond_view(state, index)
        if view.used:
            nodes[("bond", index)] = view.content
    return nodes


def apply_formation(
    state: BasisState,
    item: FormationProposal,
    seed: IdentitySeed,
) -> FormationAnswer:
    conditions = proposal_conditions(state, item, source=None)
    if (
        not isinstance(seed, IdentitySeed)
        or seed.local_root_slot not in (0, 1)
        or isinstance(seed.local_root_slot, bool)
        or seed.source != "supplied fresh local root-endpoint slot"
    ):
        raise ValueError("formation needs one supplied local root-endpoint slot")
    target = state.layout.anchors.index(item.site)
    endpoint_site = state.layout.carriers[target].sites[CARRIER_ENDPOINT_LANES[seed.local_root_slot]]
    all_conditions = conditions + (("root_endpoint_fresh", state.bits[endpoint_site] == 0),)
    failed = tuple(name for name, value in all_conditions if not value)
    if failed:
        return FormationAnswer(state, None, "blocked:" + ",".join(failed), all_conditions)
    values = list(state.bits)
    values[endpoint_site] = 1
    write_carrier(
        values,
        state.layout.carriers[target],
        item.payload,
        root_origin=1,
        arrival_direction=0,
        root_slot=seed.local_root_slot,
    )
    output = replace(state, bits=tuple(values))
    formed = next(value for value in read_candidate_records(output) if target in value.active_carriers)
    return FormationAnswer(output, formed, "formed", all_conditions)


def recoding_support(request: RecodingRequest) -> frozenset[tuple[str, int]]:
    bond = min(request.source, request.destination)
    return frozenset(
        (("carrier", request.source), ("bond", bond), ("carrier", request.destination))
    )


def bond_endpoints(index: int, view: BondView) -> tuple[int, int]:
    return (index, index + 1) if view.direction == 0 else (index + 1, index)


def arrival_history(state: BasisState, carrier: int) -> tuple[int, ...]:
    return tuple(
        index
        for index in range(state.layout.size - 1)
        if bond_view(state, index).used
        and bond_endpoints(index, bond_view(state, index))[1] == carrier
    )


def apply_recoding(state: BasisState, request: RecodingRequest) -> RecodingAnswer:
    validate_state(state)
    if not isinstance(request, RecodingRequest):
        raise TypeError("recoding needs one explicit RecodingRequest")
    if (
        not isinstance(request.source, int)
        or isinstance(request.source, bool)
        or not isinstance(request.destination, int)
        or isinstance(request.destination, bool)
        or not 0 <= request.source < state.layout.size
        or not 0 <= request.destination < state.layout.size
        or abs(request.source - request.destination) != 1
    ):
        raise ValueError("recoding source and target must be adjacent installed carriers")
    conditions = proposal_conditions(state, request.proposal, source=request.source)
    source = carrier_view(state, request.source)
    bond_index = min(request.source, request.destination)
    extra = (
        ("source_present", source.present == 1),
        ("content_preserved", request.proposal.payload == source.content),
        ("bond_fresh", bond_blank(state, bond_index)),
        ("arrival_history_fresh", not arrival_history(state, request.destination)),
    )
    all_conditions = conditions + extra
    failed = tuple(name for name, value in all_conditions if not value)
    if failed:
        return RecodingAnswer(state, "blocked:" + ",".join(failed), all_conditions)
    direction = int(request.source > request.destination)
    values = list(state.bits)
    write_bond(
        values,
        state.layout.bonds[bond_index],
        source.content,
        direction=direction,
        source_origin=source.root_origin,
        predecessor_direction=source.arrival_direction if not source.root_origin else 0,
        root_slot=source.root_slot if source.root_origin else 0,
    )
    for lane in range(CARRIER_ROOT_SLOT_LANE + 1):
        values[state.layout.carriers[request.source].sites[lane]] = 0
    write_carrier(
        values,
        state.layout.carriers[request.destination],
        source.content,
        root_origin=0,
        arrival_direction=direction,
        root_slot=0,
    )
    return RecodingAnswer(replace(state, bits=tuple(values)), "recoded", all_conditions)


def predecessor_bond_index(carrier: int, arrival_direction: int) -> int:
    return carrier - 1 if arrival_direction == 0 else carrier


def matching_predecessor(
    state: BasisState,
    carrier: int,
    arrival_direction: int,
    content: Word,
) -> int | None:
    index = predecessor_bond_index(carrier, arrival_direction)
    if not 0 <= index < state.layout.size - 1:
        return None
    view = bond_view(state, index)
    if (
        view.used
        and bond_endpoints(index, view)[1] == carrier
        and view.content == content
        and all(view.interface)
    ):
        return index
    return None


def continuation_bonds(
    state: BasisState,
    predecessor: int,
    carrier: int,
    content: Word,
) -> tuple[int, ...]:
    found = []
    for index in range(state.layout.size - 1):
        if index == predecessor:
            continue
        view = bond_view(state, index)
        if not view.used or view.source_origin or view.content != content:
            continue
        source, _destination = bond_endpoints(index, view)
        if source != carrier:
            continue
        if predecessor_bond_index(carrier, view.predecessor_direction) == predecessor:
            found.append(index)
    return tuple(found)


def local_constraint_failures(state: BasisState) -> int:
    """Count only bounded carrier, segment, endpoint, and continuity faults."""

    validate_state(state)
    failures = 0
    for index in range(state.layout.size):
        view = carrier_view(state, index)
        sites = state.layout.carriers[index].sites
        if not view.present:
            failures += sum(
                state.bits[sites[lane]] for lane in range(CARRIER_ROOT_SLOT_LANE + 1)
            )
            continue
        failures += int(not payload_lawful(state.layout, view.content))
        failures += sum(1 - value for value in view.interface)
        if view.root_origin:
            failures += int(view.endpoint_markers[view.root_slot] != 1)
            failures += int(view.arrival_direction != 0)
        else:
            failures += int(view.root_slot != 0)
            predecessor = matching_predecessor(
                state,
                index,
                view.arrival_direction,
                view.content,
            )
            failures += int(predecessor is None)

    for index in range(state.layout.size - 1):
        view = bond_view(state, index)
        sites = state.layout.bonds[index].sites
        if not view.used:
            failures += sum(state.bits[site] for site in sites)
            continue
        failures += int(not payload_lawful(state.layout, view.content))
        failures += sum(1 - value for value in view.interface)
        failures += state.bits[sites[39]]
        source, destination = bond_endpoints(index, view)
        if view.source_origin:
            failures += int(view.predecessor_direction != 0)
            failures += int(
                carrier_view(state, source).endpoint_markers[view.root_slot] != 1
            )
        else:
            failures += int(view.root_slot != 0)
            predecessor = matching_predecessor(
                state,
                source,
                view.predecessor_direction,
                view.content,
            )
            failures += int(predecessor is None or predecessor == index)
        arrival = carrier_view(state, destination)
        active_arrival = int(
            arrival.present
            and not arrival.root_origin
            and arrival.arrival_direction == view.direction
            and arrival.content == view.content
        )
        continuations = continuation_bonds(state, index, destination, view.content)
        failures += int(active_arrival + len(continuations) != 1)

    for carrier in range(state.layout.size):
        view = carrier_view(state, carrier)
        for slot, marker in enumerate(view.endpoint_markers):
            attachments = int(
                view.present and view.root_origin and view.root_slot == slot
            )
            for bond in range(state.layout.size - 1):
                segment = bond_view(state, bond)
                if not segment.used or not segment.source_origin:
                    continue
                source, _destination = bond_endpoints(bond, segment)
                attachments += int(source == carrier and segment.root_slot == slot)
            failures += int((marker == 1 and attachments != 1) or (marker == 0 and attachments != 0))
    return failures


def quotient_adjacency(
    state: BasisState,
) -> tuple[
    dict[tuple[str, int], Word | None],
    dict[tuple[str, int], set[tuple[str, int]]],
]:
    nodes: dict[tuple[str, int], Word | None] = {}
    edges: dict[tuple[str, int], set[tuple[str, int]]] = {}

    def add(node: tuple[str, int], content: Word | None) -> None:
        nodes[node] = content
        edges.setdefault(node, set())

    def join(left: tuple[str, int], right: tuple[str, int]) -> None:
        edges[left].add(right)
        edges[right].add(left)

    for carrier in range(state.layout.size):
        view = carrier_view(state, carrier)
        for slot, marker in enumerate(view.endpoint_markers):
            if marker:
                add(("root", 2 * carrier + slot), None)
        if view.present:
            add(("carrier", carrier), view.content)
            if view.root_origin:
                join(("carrier", carrier), ("root", 2 * carrier + view.root_slot))
    for bond in range(state.layout.size - 1):
        view = bond_view(state, bond)
        if not view.used:
            continue
        node = ("bond", bond)
        add(node, view.content)
        source, destination = bond_endpoints(bond, view)
        if view.source_origin:
            join(node, ("root", 2 * source + view.root_slot))
        else:
            predecessor = predecessor_bond_index(source, view.predecessor_direction)
            join(node, ("bond", predecessor))
        arrival = carrier_view(state, destination)
        if (
            arrival.present
            and not arrival.root_origin
            and arrival.arrival_direction == view.direction
            and arrival.content == view.content
        ):
            join(node, ("carrier", destination))
    return nodes, edges


def read_candidate_records(state: BasisState) -> tuple[InvariantFactRecord, ...]:
    """Read quotient classes only after the supplied candidate constraints."""

    if local_constraint_failures(state):
        raise ValueError("physical fact graph is outside the Cycle-365 code space")
    nodes, edges = quotient_adjacency(state)
    unseen = set(nodes)
    output = []
    while unseen:
        start = min(unseen)
        reached = {start}
        frontier = [start]
        while frontier:
            current = frontier.pop()
            for neighbour in edges[current]:
                if neighbour not in reached:
                    reached.add(neighbour)
                    frontier.append(neighbour)
        unseen.difference_update(reached)
        roots = tuple(sorted(node for node in reached if node[0] == "root"))
        contents = {nodes[node] for node in reached if nodes[node] is not None}
        active = tuple(sorted(node[1] for node in reached if node[0] == "carrier"))
        if len(roots) != 1 or len(contents) != 1 or len(active) != 1:
            raise ValueError("candidate quotient lacks one root, content, or active carrier")
        root_index = roots[0][1]
        root_carrier, root_slot = divmod(root_index, 2)
        root_site = state.layout.carriers[root_carrier].sites[
            CARRIER_ENDPOINT_LANES[root_slot]
        ]
        output.append(
            InvariantFactRecord(
                state.layout.sites[root_site].coord,
                next(iter(contents)),
                tuple(sorted(reached)),
                active,
            )
        )
    return tuple(sorted(output, key=lambda item: item.identity))


def overlap_table(requests: tuple[RecodingRequest, ...]) -> tuple[tuple[int, int, str], ...]:
    rows = []
    for left in range(len(requests)):
        for right in range(left + 1, len(requests)):
            if requests[left] == requests[right]:
                rows.append((left, right, "identical-request-unique"))
            elif recoding_support(requests[left]) & recoding_support(requests[right]):
                rows.append((left, right, "shared-support-conflict"))
    return tuple(rows)


def apply_recoding_batch(
    state: BasisState,
    requests: tuple[RecodingRequest, ...],
) -> BatchAnswer:
    validate_state(state)
    if not isinstance(requests, tuple):
        raise TypeError("recoding batch must be a tuple")
    for request in requests:
        if not isinstance(request, RecodingRequest):
            raise TypeError("recoding batch contains a non-request")
    overlaps = overlap_table(requests)
    conflicts = {
        index
        for left, right, kind in overlaps
        if kind == "shared-support-conflict"
        for index in (left, right)
    }
    if conflicts:
        statuses = tuple(
            "overlap-conflict:shared-support" if index in conflicts else "not-applied:atomic-conflict"
            for index in range(len(requests))
        )
        return BatchAnswer(state, statuses, overlaps)
    current = state
    seen: list[RecodingRequest] = []
    statuses = []
    for request in requests:
        if request in seen:
            statuses.append("identical-request-coalesced")
            continue
        answer = apply_recoding(current, request)
        current = answer.state
        statuses.append(answer.status)
        seen.append(request)
    return BatchAnswer(current, tuple(statuses), overlaps)


def words(fixture: c342.c338.RouteFixture, count: int) -> tuple[Word, ...]:
    cylinders = c342.make_cylinder_chain(fixture, endpoint=0, count=count)
    formed = tuple(c342.form_conditional_record(fixture, item) for item in cylinders)
    if any(not item.typed or not item.permanent for item in formed):
        raise RuntimeError("supplied Cycle-342 payload fixture lost its conditional type")
    return tuple(c342.record_word(item) for item in formed)


def rotate_payload(payload: Word, mapping) -> Word:
    record = c342.decode_record_word(payload)
    cylinder = record.cylinder
    rotated = c342.c338.FutureCylinder(
        endpoint=cylinder.endpoint,
        candidate=cylinder.candidate,
        phase=cylinder.phase,
        future_pre=int(mapping[cylinder.future_pre]),
        future_post=int(mapping[cylinder.future_post]),
    )
    return c342.record_word(c342.CylinderRecord(rotated, record.typed, record.permanent))


def connected_nn(layout: Layout) -> bool:
    coordinates = {site.coord for site in layout.sites}
    reached = {layout.sites[0].coord}
    frontier = [layout.sites[0].coord]
    while frontier:
        current = frontier.pop()
        for axis in range(3):
            for delta in (-1, 1):
                neighbour = list(current)
                neighbour[axis] += delta
                candidate = tuple(neighbour)
                if candidate in coordinates and candidate not in reached:
                    reached.add(candidate)
                    frontier.append(candidate)
    return len(reached) == len(coordinates)


def support_diameter(layout: Layout, request: RecodingRequest) -> int:
    indices = tuple(
        site
        for role, index in recoding_support(request)
        for site in (
            layout.carriers[index].sites if role == "carrier" else layout.bonds[index].sites
        )
    )
    return max(
        distance(layout.sites[left].coord, layout.sites[right].coord)
        for left in indices
        for right in indices
    )


def read_rejected(state: BasisState) -> bool:
    try:
        read_candidate_records(state)
    except ValueError:
        return True
    return False


def formation_truth_table_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(3)
    layout = build_layout(fixture, 6, np.eye(3, dtype=int))
    payload = words(fixture, 1)[0]
    empty = blank_state(layout)
    rows = []
    failures = formed = blocked_leakage = 0
    for gates in product((0, 1), repeat=5):
        complete, close, ready, provenance, fresh = gates
        item = proposal(
            layout,
            0,
            payload,
            complete=complete,
            close=close,
            ready=ready,
            provenance=provenance,
            fresh=fresh,
            confirmations=provenance,
        )
        answer = apply_formation(empty, item, IdentitySeed(0))
        expected = all(gates)
        observed = answer.status == "formed"
        failures += int(expected != observed)
        formed += int(observed)
        blocked_leakage += int(not observed and answer.state != empty)
        rows.append((gates, answer.status))
    lawful = apply_formation(empty, proposal(layout, 0, payload), IdentitySeed(0))
    occupied = apply_formation(lawful.state, proposal(layout, 0, payload), IdentitySeed(1))
    detail = {
        "declared_gate_states": len(rows),
        "formed_states": formed,
        "truth_table_failures": failures,
        "blocked_state_leakage": blocked_leakage,
        "condition_order": tuple(name for name, _value in lawful.conditions),
        "occupied_target_status": occupied.status,
        "raw_interface_bits_called_Records": False,
    }
    check(
        "the migrating candidate forms one conditional Record iff every complete/close/predecessor/provenance/fresh predicate holds",
        len(rows) == 32
        and formed == 1
        and failures == blocked_leakage == 0
        and occupied.formed is None
        and "fresh_site" in occupied.status
        and detail["condition_order"] == (
            "complete_payload",
            "faithful_close",
            "predecessor_readiness",
            "provenance_acceptance",
            "fresh_site",
            "root_endpoint_fresh",
        )
        and not detail["raw_interface_bits_called_Records"],
        detail,
    )
    return detail


def worldline_covariance_and_resource_controls() -> dict[str, object]:
    frames = c362.c353.proper_cubic_frames()
    cases = held_cases = 0
    formation_failures = recoding_failures = constraint_failures = 0
    quotient_failures = content_residuals = geometry_failures = 0
    maximum_support = maximum_diameter = 0
    rows = []
    for size in SIZES:
        layout = build_layout(c342.c338.build_fixture(3), size, np.eye(3, dtype=int))
        rows.append(
            {
                "N": size,
                "held": size == HELD_SIZE,
                "M2_sites": len(layout.sites),
                "reusable_carrier_M2": CARRIER_ROOT_SLOT_LANE + 1,
                "root_endpoint_M2": len(CARRIER_ENDPOINT_LANES),
                "bond_M2": WIDTH,
                "formula": "(38 carrier + 2 root-endpoint)N + 40(N-1)",
            }
        )
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        payload = words(fixture, 1)[0]
        for frame in frames:
            for size in SIZES:
                layout = build_layout(fixture, size, frame)
                geometry_failures += int(not connected_nn(layout))
                state = blank_state(layout)
                root_endpoint_coord = layout.sites[
                    layout.carriers[0].sites[CARRIER_ENDPOINT_LANES[0]]
                ].coord
                formed = apply_formation(
                    state,
                    proposal(layout, 0, payload),
                    IdentitySeed(0),
                )
                formation_failures += int(formed.status != "formed")
                state = formed.state
                for destination in range(1, size):
                    request = RecodingRequest(
                        destination - 1,
                        destination,
                        proposal(
                            layout,
                            destination,
                            payload,
                            (destination - 1,),
                        ),
                    )
                    if destination == 1:
                        maximum_support = max(
                            maximum_support,
                            len(recoding_support(request)) * WIDTH,
                        )
                        maximum_diameter = max(
                            maximum_diameter,
                            support_diameter(layout, request),
                        )
                    answer = apply_recoding(state, request)
                    recoding_failures += int(answer.status != "recoded")
                    state = answer.state
                    constraint_failures += local_constraint_failures(state)
                    observed = read_candidate_records(state)
                    quotient_failures += int(
                        len(observed) != 1
                        or observed[0].identity != root_endpoint_coord
                        or observed[0].active_carriers != (destination,)
                        or not carrier_blank(state, destination - 1)
                    )
                    content_residuals += sum(
                        left != right for left, right in zip(observed[0].content, payload)
                    )
                cases += 1
                held_cases += int(length == 6 and size == HELD_SIZE)
    detail = {
        "rows": rows,
        "L_by_N_by_proper_cubic_frame_cases": cases,
        "proper_cubic_frames": len(frames),
        "held_L6_N18_cases": held_cases,
        "Cycle342_payload_frame_action": "supplied upstream; the recoding law transports the bound 30-bit word opaquely",
        "formation_failures": formation_failures,
        "recoding_failures": recoding_failures,
        "local_constraint_failures": constraint_failures,
        "quotient_identity_or_single_read_failures": quotient_failures,
        "all_30_content_bit_residuals": content_residuals,
        "connected_NN_patch_failures": geometry_failures,
        "maximum_recoding_support_M2": maximum_support,
        "maximum_recoding_support_L1_diameter": maximum_diameter,
    }
    check(
        "one exact migrating quotient preserves identity and all 30 bits through bounded local recodings in every proper-cubic frame and held N18",
        len(frames) == 24
        and cases == len(LENGTHS) * len(SIZES) * 24
        and held_cases == 24
        and formation_failures
        == recoding_failures
        == constraint_failures
        == quotient_failures
        == content_residuals
        == geometry_failures
        == 0
        and maximum_support == 3 * WIDTH
        and maximum_diameter == 41
        and all(
            row["M2_sites"] == WIDTH * (2 * row["N"] - 1)
            and row["reusable_carrier_M2"] == 38
            and row["root_endpoint_M2"] == 2
            for row in rows
        ),
        detail,
    )
    return detail


def concurrency_and_overlap_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(3)
    layout = build_layout(fixture, 6, np.eye(3, dtype=int))
    payloads = words(fixture, 2)
    state = blank_state(layout)
    state = apply_formation(state, proposal(layout, 0, payloads[0]), IdentitySeed(0)).state
    state = apply_formation(state, proposal(layout, 4, payloads[1]), IdentitySeed(0)).state
    left = RecodingRequest(0, 1, proposal(layout, 1, payloads[0], (0,)))
    right = RecodingRequest(4, 5, proposal(layout, 5, payloads[1], (4,)))
    lr = apply_recoding(apply_recoding(state, left).state, right).state
    rl = apply_recoding(apply_recoding(state, right).state, left).state
    batch = apply_recoding_batch(state, (left, right))

    single = blank_state(layout)
    single = apply_formation(single, proposal(layout, 0, payloads[0]), IdentitySeed(0)).state
    duplicate = apply_recoding_batch(single, (left, left))
    unique = apply_recoding(single, left)

    conflict_state = blank_state(layout)
    conflict_state = apply_formation(
        conflict_state,
        proposal(layout, 2, payloads[0]),
        IdentitySeed(0),
    ).state
    move_left = RecodingRequest(2, 1, proposal(layout, 1, payloads[0], (2,)))
    move_right = RecodingRequest(2, 3, proposal(layout, 3, payloads[0], (2,)))
    conflict = apply_recoding_batch(conflict_state, (move_left, move_right))
    detail = {
        "disjoint_support": not bool(recoding_support(left) & recoding_support(right)),
        "disjoint_sequential_commutes": lr == rl,
        "disjoint_batch_matches": batch.state == lr,
        "disjoint_batch_statuses": batch.statuses,
        "identical_overlap": duplicate.overlaps,
        "identical_statuses": duplicate.statuses,
        "identical_unique_result": duplicate.state == unique.state,
        "nonidentical_overlap": conflict.overlaps,
        "nonidentical_statuses": conflict.statuses,
        "conflict_state_unchanged": conflict.state == conflict_state,
        "hidden_priority_rule": None,
    }
    check(
        "disjoint recodings commute, identical overlaps coalesce uniquely, and every nonidentical shared-support overlap conflicts atomically",
        detail["disjoint_support"]
        and detail["disjoint_sequential_commutes"]
        and detail["disjoint_batch_matches"]
        and batch.statuses == ("recoded", "recoded")
        and duplicate.overlaps == ((0, 1, "identical-request-unique"),)
        and duplicate.statuses == ("recoded", "identical-request-coalesced")
        and detail["identical_unique_result"]
        and conflict.overlaps == ((0, 1, "shared-support-conflict"),)
        and conflict.statuses == (
            "overlap-conflict:shared-support",
            "overlap-conflict:shared-support",
        )
        and detail["conflict_state_unchanged"]
        and detail["hidden_priority_rule"] is None,
        detail,
    )
    return detail


def migration_and_anti_merge_discriminator_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(3)
    layout = build_layout(fixture, 6, np.eye(3, dtype=int))
    payload = words(fixture, 1)[0]
    initial = apply_formation(
        blank_state(layout),
        proposal(layout, 0, payload),
        IdentitySeed(0),
    ).state
    moved = apply_recoding(
        initial,
        RecodingRequest(0, 1, proposal(layout, 1, payload, (0,))),
    ).state
    moved_records = read_candidate_records(moved)
    reused_answer = apply_formation(
        moved,
        proposal(layout, 0, payload),
        IdentitySeed(1),
    )
    reused = reused_answer.state
    reused_records = read_candidate_records(reused)

    remote = blank_state(layout)
    remote = apply_formation(
        remote,
        proposal(layout, 0, payload),
        IdentitySeed(0),
    ).state
    remote = apply_formation(
        remote,
        proposal(layout, 4, payload),
        IdentitySeed(0),
    ).state
    remote_equal_content_records = read_candidate_records(remote)

    restored_bits = list(moved.bits)
    source_sites = layout.carriers[0].sites
    for lane in range(CARRIER_ROOT_SLOT_LANE + 1):
        restored_bits[source_sites[lane]] = initial.bits[source_sites[lane]]
    duplicated_old = replace(moved, bits=tuple(restored_bits))
    root_endpoint_coords = tuple(
        layout.sites[layout.carriers[0].sites[lane]].coord
        for lane in CARRIER_ENDPOINT_LANES
    )

    detail = {
        "migrating_payload_carrier_cleared": carrier_blank(moved, 0),
        "old_root_endpoint_marker_retained": carrier_view(moved, 0).endpoint_markers == (1, 0),
        "new_carrier_active": carrier_view(moved, 1).present == 1,
        "quotient_records_after_move": len(moved_records),
        "moved_identity": moved_records[0].identity,
        "moved_content_preserved": moved_records[0].content == payload,
        "cleared_old_carrier_reused": reused_answer.status == "formed",
        "equal_content_quotient_records_after_reuse": len(reused_records),
        "physically_distinct_root_endpoints": tuple(item.identity for item in reused_records),
        "remote_equal_content_root_records": len(remote_equal_content_records),
        "remote_equal_content_root_endpoints": tuple(
            item.identity for item in remote_equal_content_records
        ),
        "transported_value_valued_root_key": False,
        "restored_old_carrier_local_failures": local_constraint_failures(duplicated_old),
        "restored_old_carrier_read_rejected": read_rejected(duplicated_old),
        "Cycle364_site_tethered_identity_includes_permanent_site": True,
        "Cycle364_site_tethered_old_carrier_clear_allowed": False,
        "Cycle364_site_tethered_cleared_site_reuse_allowed": False,
        "candidate_law_selected": False,
    }
    check(
        "migration clears and reuses the payload carrier while the local quotient reads one old identity; disconnected equal-content roots never merge",
        detail["migrating_payload_carrier_cleared"]
        and detail["old_root_endpoint_marker_retained"]
        and detail["new_carrier_active"]
        and detail["quotient_records_after_move"] == 1
        and detail["moved_identity"] == root_endpoint_coords[0]
        and detail["moved_content_preserved"]
        and detail["cleared_old_carrier_reused"]
        and detail["equal_content_quotient_records_after_reuse"] == 2
        and detail["physically_distinct_root_endpoints"] == root_endpoint_coords
        and detail["remote_equal_content_root_records"] == 2
        and len(set(detail["remote_equal_content_root_endpoints"])) == 2
        and not detail["transported_value_valued_root_key"]
        and detail["restored_old_carrier_local_failures"] > 0
        and detail["restored_old_carrier_read_rejected"]
        and not detail["Cycle364_site_tethered_old_carrier_clear_allowed"]
        and not detail["Cycle364_site_tethered_cleared_site_reuse_allowed"]
        and not detail["candidate_law_selected"],
        detail,
    )
    return detail


def deletion_splice_corruption_and_domain_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(3)
    layout = build_layout(fixture, 6, np.eye(3, dtype=int))
    payload = words(fixture, 1)[0]
    root = apply_formation(
        blank_state(layout),
        proposal(layout, 0, payload),
        IdentitySeed(0),
    ).state
    deletion_rows = []
    variants = (
        ("complete_payload", proposal(layout, 1, payload, (0,), complete=0)),
        ("faithful_close", proposal(layout, 1, payload, (0,), close=0)),
        ("predecessor_readiness", proposal(layout, 1, payload, (0,), ready=0)),
        (
            "provenance_acceptance",
            proposal(layout, 1, payload, (0,), provenance=0, confirmations=0),
        ),
        ("fresh_site", proposal(layout, 1, payload, (0,), fresh=0)),
    )
    for name, item in variants:
        answer = apply_recoding(root, RecodingRequest(0, 1, item))
        deletion_rows.append(
            {
                "deleted": name,
                "recoded": answer.status == "recoded",
                "state_unchanged": answer.state == root,
                "condition_visible": dict(answer.conditions)[name] is False,
            }
        )

    first = apply_recoding(
        root,
        RecodingRequest(0, 1, proposal(layout, 1, payload, (0,))),
    ).state
    chain = apply_recoding(
        first,
        RecodingRequest(1, 2, proposal(layout, 2, payload, (1,))),
    ).state

    deleted_bits = list(chain.bits)
    for site in layout.bonds[0].sites:
        deleted_bits[site] = 0
    deleted_segment = replace(chain, bits=tuple(deleted_bits))

    marker_deleted_bits = list(chain.bits)
    marker_deleted_bits[layout.carriers[0].sites[CARRIER_ENDPOINT_LANES[0]]] = 0
    deleted_root_marker = replace(chain, bits=tuple(marker_deleted_bits))

    splice_bits = list(chain.bits)
    splice_site = layout.bonds[1].sites[BOND_PREDECESSOR_DIRECTION_LANE]
    splice_bits[splice_site] ^= 1
    spliced_predecessor = replace(chain, bits=tuple(splice_bits))

    active_corruptions = []
    segment_corruptions = []
    for lane in CONTENT_LANES:
        active_bits = list(chain.bits)
        active_bits[layout.carriers[2].sites[lane]] ^= 1
        attacked_active = replace(chain, bits=tuple(active_bits))
        active_corruptions.append(
            (
                lane,
                local_constraint_failures(attacked_active) > 0,
                read_rejected(attacked_active),
            )
        )
        segment_bits = list(chain.bits)
        segment_bits[layout.bonds[1].sites[lane]] ^= 1
        attacked_segment = replace(chain, bits=tuple(segment_bits))
        segment_corruptions.append(
            (
                lane,
                local_constraint_failures(attacked_segment) > 0,
                read_rejected(attacked_segment),
            )
        )

    provenance_splice = proposal(layout, 1, payload, (0,))
    provenance_splice = replace(
        provenance_splice,
        provenance=replace(provenance_splice.provenance, site=layout.anchors[4]),
    )
    provenance_splice_answer = apply_recoding(
        root,
        RecodingRequest(0, 1, provenance_splice),
    )

    invalid_calls = (
        lambda: build_layout(fixture, 1, np.eye(3, dtype=int)),
        lambda: build_layout(fixture, 6, -np.eye(3, dtype=int)),
        lambda: apply_formation(root, proposal(layout, 1, payload), IdentitySeed(True)),
        lambda: apply_formation(
            root,
            replace(proposal(layout, 1, payload), payload=payload[:-1]),
            IdentitySeed(0),
        ),
        lambda: apply_formation(
            root,
            replace(
                proposal(layout, 1, payload),
                close=replace(proposal(layout, 1, payload).close, source="host-close"),
            ),
            IdentitySeed(0),
        ),
        lambda: apply_recoding(
            root,
            RecodingRequest(0, 2, proposal(layout, 2, payload, (0,))),
        ),
        lambda: apply_recoding_batch(root, [  # type: ignore[arg-type]
            RecodingRequest(0, 1, proposal(layout, 1, payload, (0,)))
        ]),
        lambda: local_constraint_failures(replace(root, bits=root.bits[:-1])),
        lambda: local_constraint_failures(
            replace(root, bits=(2,) + root.bits[1:])
        ),
    )
    domain_rejections = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError):
            domain_rejections += 1

    detail = {
        "five_interface_deletions": deletion_rows,
        "segment_deletion_local_failures": local_constraint_failures(deleted_segment),
        "segment_deletion_read_rejected": read_rejected(deleted_segment),
        "root_marker_deletion_local_failures": local_constraint_failures(deleted_root_marker),
        "root_marker_deletion_read_rejected": read_rejected(deleted_root_marker),
        "predecessor_splice_local_failures": local_constraint_failures(spliced_predecessor),
        "predecessor_splice_read_rejected": read_rejected(spliced_predecessor),
        "active_content_bits_attacked": len(active_corruptions),
        "active_content_corruptions_visible": sum(left and right for _lane, left, right in active_corruptions),
        "segment_content_bits_attacked": len(segment_corruptions),
        "segment_content_corruptions_visible": sum(left and right for _lane, left, right in segment_corruptions),
        "provenance_interface_splice_status": provenance_splice_answer.status,
        "provenance_interface_splice_state_unchanged": provenance_splice_answer.state == root,
        "domain_attempts": len(invalid_calls),
        "domain_rejections": domain_rejections,
    }
    check(
        "predicate deletion, segment/root deletion, predecessor/provenance splice, and every carrier/segment content-bit corruption are visible",
        all(
            not row["recoded"] and row["state_unchanged"] and row["condition_visible"]
            for row in deletion_rows
        )
        and detail["segment_deletion_local_failures"] > 0
        and detail["segment_deletion_read_rejected"]
        and detail["root_marker_deletion_local_failures"] > 0
        and detail["root_marker_deletion_read_rejected"]
        and detail["predecessor_splice_local_failures"] > 0
        and detail["predecessor_splice_read_rejected"]
        and detail["active_content_bits_attacked"] == RECORD_BITS
        and detail["active_content_corruptions_visible"] == RECORD_BITS
        and detail["segment_content_bits_attacked"] == RECORD_BITS
        and detail["segment_content_corruptions_visible"] == RECORD_BITS
        and "provenance_acceptance" in detail["provenance_interface_splice_status"]
        and detail["provenance_interface_splice_state_unchanged"]
        and domain_rejections == len(invalid_calls),
        detail,
    )
    return detail


def inventory_and_semantic_controls() -> dict[str, object]:
    inventory = {
        "result": "bounded positive migrating/invariant-fact candidate Record-formation law",
        "hypothesis": LAW_NAME,
        "hypothesis_status": "falsifiable downstream candidate",
        "derived_from_axioms": False,
        "axiom_language_proposed": False,
        "selected_framework_law": False,
        "completeness_prior": COMPLETENESS_PRIOR,
        "prior_already_left_migrating_permanence_open": True,
        "novelty_boundary": "exact bounded local worldline quotient with anti-merge, migration, splice, deletion, corruption, and overlap controls",
        "formed_type": RECORD_TYPE,
        "Record_name_scope": "only a code-valid quotient class output by this explicitly supplied candidate law",
        "raw_reversible_M2_bits_are_Records": False,
        "Cycle361_input": "one target/content-bound faithful-close candidate interface for a complete 30-M2 payload",
        "Cycle362_input": "one target/content/predecessor-bound common-provenance acceptance interface",
        "Cycle326_input": "one explicit predecessor-readiness and fresh-target interface",
        "Cycle342_input": "one supplied lawful typed/permanent 30-M2 content word and L-specific decoder fixture",
        "required_predicates": (
            "complete_payload",
            "faithful_close",
            "predecessor_readiness",
            "provenance_acceptance",
            "fresh_site",
        ),
        "physical_patch": "finite connected-NN strip with 38-M2 reusable carriers, two local endpoint sites per cell, and 40-M2 bonds in one supplied proper-cubic frame",
        "reusable_carrier_M2": CARRIER_ROOT_SLOT_LANE + 1,
        "root_endpoint_M2_per_cell": len(CARRIER_ENDPOINT_LANES),
        "bond_M2": WIDTH,
        "recoding_support_M2": 3 * WIDTH,
        "recoding_support_L1_diameter": 41,
        "quotient_nodes": "occupied carrier facts, immutable directed bond segments, and one-bit local root-endpoint slots",
        "quotient_generators": "root attachment, exact predecessor pointer, and exact final carrier arrival",
        "quotient_identity_readout": "the proper-cubic coordinate of the unique physical root-endpoint node, never a copied label",
        "transported_value_valued_root_or_event_key": False,
        "distinct_equal_content_roots": "different disconnected physical root-endpoint components",
        "old_and_new_carrier_double_read": False,
        "payload_carrier_cleared_on_migration": True,
        "root_endpoint_history_cleared_on_migration": False,
        "cleared_payload_carrier_reusable": True,
        "supplied_root_endpoint_slots_per_carrier": 2,
        "supplied_single_use_bond_segments": True,
        "supplied_single_arrival_history_per_carrier": True,
        "supplied_structure_capacity_is_unbounded": False,
        "physical_gate_compiler": None,
        "universal_event_identity_derived": False,
        "actual_history_sampler": None,
        "Born_weights": None,
        "statistics": None,
        "metric_time": None,
        "interval": None,
        "rate": None,
        "renewable_unbounded_capacity": None,
        "universal_full_lattice_completion": None,
        "candidate_law_selection": None,
        "no_go": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    text = " ".join(__doc__.split()).lower()
    required_text = (
        "falsifiable downstream hypothesis",
        "neither derives",
        "raw reversible carrier",
        "not records",
        "worldline quotient",
        "clears the source",
        "site-tethered candidate",
        "already left open",
        "candidate-law selection",
        "born/statistics",
        "metric time",
        "renewable unbounded capacity",
        "full-lattice completion",
        "authority is none",
        "audit is unset",
    )
    check(
        "the exact quotient and every supplied capacity/interface boundary remain explicit without promoting bits, keys, recodings, or layers to universal identity or time",
        all(item in text for item in required_text)
        and RECORD_BITS == c361.MATCH_BITS == 30
        and c362.PAYLOAD_LANES == tuple(range(2, RECORD_BITS + 2))
        and c326 is not None
        and not inventory["derived_from_axioms"]
        and not inventory["axiom_language_proposed"]
        and not inventory["selected_framework_law"]
        and inventory["prior_already_left_migrating_permanence_open"]
        and not inventory["raw_reversible_M2_bits_are_Records"]
        and not inventory["transported_value_valued_root_or_event_key"]
        and inventory["recoding_support_M2"] == 120
        and inventory["recoding_support_L1_diameter"] == 41
        and inventory["supplied_root_endpoint_slots_per_carrier"] == 2
        and inventory["supplied_single_use_bond_segments"]
        and inventory["supplied_single_arrival_history_per_carrier"]
        and not inventory["supplied_structure_capacity_is_unbounded"]
        and inventory["physical_gate_compiler"] is None
        and not inventory["universal_event_identity_derived"]
        and inventory["actual_history_sampler"] is None
        and inventory["Born_weights"] is inventory["statistics"] is None
        and inventory["metric_time"] is inventory["interval"] is inventory["rate"] is None
        and inventory["renewable_unbounded_capacity"] is None
        and inventory["universal_full_lattice_completion"] is None
        and inventory["candidate_law_selection"] is None
        and inventory["no_go"] is inventory["axiom_pressure"] is None
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 365 ROUTE 2: MIGRATING/INVARIANT-FACT RECORD-FORMATION CANDIDATE")
    print("authority=none; audit=unset; downstream hypothesis; not axiom language")
    truth = formation_truth_table_controls()
    worldline = worldline_covariance_and_resource_controls()
    overlap = concurrency_and_overlap_controls()
    discriminator = migration_and_anti_merge_discriminator_controls()
    attacks = deletion_splice_corruption_and_domain_controls()
    inventory = inventory_and_semantic_controls()
    check(
        "Route 2 is an exact bounded positive migrating candidate with a live site-tethered discriminator, not a selected universal law",
        truth["truth_table_failures"] == 0
        and worldline["local_constraint_failures"] == 0
        and worldline["quotient_identity_or_single_read_failures"] == 0
        and overlap["hidden_priority_rule"] is None
        and discriminator["quotient_records_after_move"] == 1
        and discriminator["equal_content_quotient_records_after_reuse"] == 2
        and attacks["active_content_corruptions_visible"] == RECORD_BITS
        and attacks["segment_content_corruptions_visible"] == RECORD_BITS
        and not inventory["selected_framework_law"],
        {
            "disposition": "bounded positive falsifiable downstream candidate",
            "declared_truth_table_states": truth["declared_gate_states"],
            "sizes": SIZES,
            "proper_cubic_frames": worldline["proper_cubic_frames"],
            "transported_value_valued_root_key": False,
            "candidate_law_selected": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_MIGRATING_INVARIANT_FACT_RECORD_FORMATION_CANDIDATE_OPEN")
        return 1
    print("RESULT PHYSICAL_MIGRATING_INVARIANT_FACT_RECORD_FORMATION_CANDIDATE_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
