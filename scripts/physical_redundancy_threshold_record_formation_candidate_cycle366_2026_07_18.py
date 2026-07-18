#!/usr/bin/env python3
"""Cycle 366 Route 3: exact redundancy-threshold formation candidate.

This runner posits, rather than derives, a falsifiable downstream law.  Three
spatially disjoint non-Record candidates must carry complete content-equal
30-bit payloads, complete 30-bit presence masks, faithful-close acceptance,
and common-event provenance into one fresh predecessor-ready convergence
site.  A fixed bounded NN circuit then forms exactly one site/content Record
at that convergence site.  One or two candidates remain candidates.

The threshold value three and the identification of this convergence event
with one framework Record are explicit supplied law content.  The three
carrier sites are not silently quotient-identified as Records.  The generic
redundancy/objectivity idea is bounded prior art in the June-05 pointer-
non-demolition note; this runner's narrower construction is the exact
Cycle-361 faithful-close / Cycle-362 common-provenance / Cycle-364
fresh-predecessor interface, its threshold discriminator, and its local
Boolean realization.

The Boolean calculation, conditional content write, formation-bit copy, and
workspace cleanup compile into reversible X/CNOT/Toffoli layers.  One final
nonunitary fresh-token consume is the explicitly hypothesized atomic commit;
before it fires the reversible transcript is not decoded as a Record.  This
is a fixed connected-NN Boolean basis-state realization of the candidate law,
not a claim that the framework already admits the commit as an M2 primitive.
``step(state)`` validates only the binary basis shape and never selects gates
from state.  Formation-law selection, threshold justification, renewal,
full-lattice completion, statistics/Born weights, and metric time remain
open.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from inspect import getsource, signature
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_site_tethered_close_gated_record_formation_candidate_cycle364_2026_07_18 as c364
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317
import physical_fixed_global_common_fork_record_lineage_nn_route_cycle362_2026_07_18 as c362


Coord = tuple[int, int, int]
Word = tuple[int, ...]
LENGTHS = (3, 6)
TRAIN_SIZES = (6, 12)
HELD_SIZE = 18
SIZES = TRAIN_SIZES + (HELD_SIZE,)
FORMATION_THRESHOLD = 3
REPLICAS = tuple(range(FORMATION_THRESHOLD))
PAYLOAD_LANES = tuple(range(c364.RECORD_BITS))
PRESENCE_LANES = tuple(range(c364.RECORD_BITS, 2 * c364.RECORD_BITS))
CLOSE_LANE = 2 * c364.RECORD_BITS
PROVENANCE_LANE = CLOSE_LANE + 1
PACKET_LANES = PAYLOAD_LANES + PRESENCE_LANES + (CLOSE_LANE, PROVENANCE_LANE)
PACKET_WIDTH = len(PACKET_LANES)
BUS_LANES = tuple(range(PROVENANCE_LANE))
AUTHORITY = "none"
AUDIT = "unset"
LAW_NAME = "Cycle-366 threshold-three convergence-site formation hypothesis"
RECORD_TYPE = "conditional threshold-three convergence-site Record"
PRIOR_ART_NOTE = (
    "docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_"
    "CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md"
)
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
    event: int
    role: str
    lane: int


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str
    event: int


@dataclass(frozen=True)
class Layer:
    name: str
    gates: tuple[Gate, ...]


@dataclass(frozen=True)
class EventBlock:
    event: int
    target_site: Coord
    predecessors: tuple[Coord, ...]
    replicas: tuple[tuple[int, ...], ...]
    match01: tuple[int, ...]
    match12: tuple[int, ...]
    prefix01: tuple[int, ...]
    prefix12: tuple[int, ...]
    bus: tuple[int, ...]
    output: tuple[int, ...]
    convergence: int
    predecessor_ready: int
    predecessor_prefix: int
    fresh: int
    formed: int


@dataclass(frozen=True)
class Layout:
    count: int
    sites: tuple[Site, ...]
    blocks: tuple[EventBlock, ...]
    layers: tuple[Layer, ...]


@dataclass(frozen=True)
class BasisState:
    layout: Layout
    bits: tuple[int, ...]


@dataclass(frozen=True)
class ReplicaCandidate:
    payload: Word
    payload_present: Word
    close: c364.FaithfulCloseInterface
    provenance: c364.ProvenanceInterface


@dataclass(frozen=True)
class RedundantProposal:
    site: Coord
    payload: Word
    readiness: c364.ReadinessInterface
    replicas: tuple[ReplicaCandidate, ...]


@dataclass(frozen=True)
class Prepared:
    state: BasisState
    admissible: bool
    reasons: tuple[str, ...]
    overlap_status: tuple[str, ...]


@dataclass(frozen=True)
class ThresholdSiteContentRecord:
    site: Coord
    content: Word
    predecessors: tuple[Coord, ...]
    record_type: str = RECORD_TYPE
    law: str = LAW_NAME
    permanent_under_candidate_law: bool = True


def gate(kind: str, sites: tuple[int, ...], label: str, event: int) -> Gate:
    arity = {
        "X": 1,
        "CNOT": 2,
        "TOFFOLI": 3,
        "CONSUME": 2,
    }
    if kind not in arity or len(sites) != arity[kind] or len(set(sites)) != len(sites):
        raise ValueError((kind, sites, label))
    return Gate(kind, sites, label, event)


def build_layout(count: int) -> Layout:
    if not isinstance(count, int) or isinstance(count, bool):
        raise ValueError("installed event count must be an integer")
    if count <= 0:
        raise ValueError("installed event count must be positive")

    sites: list[Site] = []
    blocks: list[EventBlock] = []

    def add(event: int, role: str, lane: int, coord: Coord) -> int:
        sites.append(Site(coord, event, role, lane))
        return len(sites) - 1

    for event in range(count):
        base_y = 8 * event
        replicas = tuple(
            tuple(
                add(event, f"R{replica}", lane, (0, base_y + 2 * replica, lane))
                for lane in PACKET_LANES
            )
            for replica in REPLICAS
        )
        match01 = tuple(
            add(event, "M01", lane, (0, base_y + 1, lane))
            for lane in PACKET_LANES
        )
        match12 = tuple(
            add(event, "M12", lane, (0, base_y + 3, lane))
            for lane in PACKET_LANES
        )
        prefix01 = tuple(
            add(event, "P01", lane, (1, base_y + 1, lane))
            for lane in PACKET_LANES
        )
        prefix12 = tuple(
            add(event, "P12", lane, (1, base_y + 3, lane))
            for lane in PACKET_LANES
        )
        bus = tuple(
            add(event, "BUS", lane, (2, base_y + 2, lane))
            for lane in BUS_LANES
        )
        output = tuple(
            add(event, "OUTPUT", lane, (1, base_y + 2, lane))
            for lane in PAYLOAD_LANES
        )
        convergence = add(
            event,
            "CONVERGENCE",
            PROVENANCE_LANE,
            (1, base_y + 2, PROVENANCE_LANE),
        )
        predecessor_ready = add(
            event,
            "PREDECESSOR_READY",
            PROVENANCE_LANE + 1,
            (1, base_y + 2, PROVENANCE_LANE + 1),
        )
        predecessor_prefix = add(
            event,
            "PREDECESSOR_PREFIX",
            PROVENANCE_LANE,
            (2, base_y + 2, PROVENANCE_LANE),
        )
        fresh = add(
            event,
            "FRESH",
            PROVENANCE_LANE,
            (3, base_y + 2, PROVENANCE_LANE),
        )
        formed = add(
            event,
            "FORMED",
            PROVENANCE_LANE - 1,
            (3, base_y + 2, PROVENANCE_LANE - 1),
        )
        blocks.append(
            EventBlock(
                event,
                sites[formed].coord,
                (),
                replicas,
                match01,
                match12,
                prefix01,
                prefix12,
                bus,
                output,
                convergence,
                predecessor_ready,
                predecessor_prefix,
                fresh,
                formed,
            )
        )

    if len({site.coord for site in sites}) != len(sites):
        raise RuntimeError("threshold-law physical M2 coordinates overlap")

    layers: list[Layer] = []

    def layer(name: str, rows) -> None:
        layers.append(Layer(name, tuple(rows)))

    for name, left_index, right_index, match_name in (
        ("pair01", 0, 1, "match01"),
        ("pair12", 1, 2, "match12"),
    ):
        layer(
            f"payload-match-{name}-left",
            (
                gate(
                    "CNOT",
                    (
                        block.replicas[left_index][lane],
                        getattr(block, match_name)[lane],
                    ),
                    f"payload-match-left:e{block.event}:{name}:lane{lane}",
                    block.event,
                )
                for block in blocks
                for lane in PAYLOAD_LANES
            ),
        )
        layer(
            f"payload-match-{name}-right",
            (
                gate(
                    "CNOT",
                    (
                        block.replicas[right_index][lane],
                        getattr(block, match_name)[lane],
                    ),
                    f"payload-match-right:e{block.event}:{name}:lane{lane}",
                    block.event,
                )
                for block in blocks
                for lane in PAYLOAD_LANES
            ),
        )
        layer(
            f"payload-match-{name}-invert",
            (
                gate(
                    "X",
                    (getattr(block, match_name)[lane],),
                    f"payload-match-invert:e{block.event}:{name}:lane{lane}",
                    block.event,
                )
                for block in blocks
                for lane in PAYLOAD_LANES
            ),
        )
    layer(
        "interface-and-pair01",
        (
            gate("TOFFOLI", (block.replicas[0][lane], block.replicas[1][lane], block.match01[lane]), f"interface-and:e{block.event}:pair01:lane{lane}", block.event)
            for block in blocks
            for lane in PRESENCE_LANES + (CLOSE_LANE, PROVENANCE_LANE)
        ),
    )
    layer(
        "interface-and-pair12",
        (
            gate("TOFFOLI", (block.replicas[1][lane], block.replicas[2][lane], block.match12[lane]), f"interface-and:e{block.event}:pair12:lane{lane}", block.event)
            for block in blocks
            for lane in PRESENCE_LANES + (CLOSE_LANE, PROVENANCE_LANE)
        ),
    )
    layer(
        "prefix-start",
        (
            gate("CNOT", (match[0], prefix[0]), f"prefix-start:e{block.event}:{name}", block.event)
            for block in blocks
            for name, match, prefix in (
                ("pair01", block.match01, block.prefix01),
                ("pair12", block.match12, block.prefix12),
            )
        ),
    )
    for lane_index in PACKET_LANES[1:]:
        layer(
            f"prefix-{lane_index}",
            (
                gate("TOFFOLI", (prefix[lane_index - 1], match[lane_index], prefix[lane_index]), f"prefix:e{block.event}:{name}:lane{lane_index}", block.event)
                for block in blocks
                for name, match, prefix in (
                    ("pair01", block.match01, block.prefix01),
                    ("pair12", block.match12, block.prefix12),
                )
            ),
        )
    layer(
        "pair-convergence",
        (
            gate("TOFFOLI", (block.prefix01[-1], block.prefix12[-1], block.convergence), f"pair-convergence:e{block.event}", block.event)
            for block in blocks
        ),
    )
    layer(
        "predecessor-convergence",
        (
            gate("TOFFOLI", (block.convergence, block.predecessor_ready, block.predecessor_prefix), f"predecessor-convergence:e{block.event}", block.event)
            for block in blocks
        ),
    )
    layer(
        "fresh-convergence",
        (
            gate("TOFFOLI", (block.predecessor_prefix, block.fresh, block.bus[-1]), f"fresh-convergence:e{block.event}", block.event)
            for block in blocks
        ),
    )
    for lane_index in reversed(BUS_LANES[:-1]):
        layer(
            f"acceptance-bus-{lane_index}",
            (
                gate("CNOT", (block.bus[lane_index + 1], block.bus[lane_index]), f"acceptance-bus:e{block.event}:lane{lane_index}", block.event)
                for block in blocks
            ),
        )
    layer(
        "write-once-content",
        (
            gate("TOFFOLI", (block.bus[lane], block.replicas[1][lane], block.output[lane]), f"write-once:e{block.event}:bit{lane}", block.event)
            for block in blocks
            for lane in PAYLOAD_LANES
        ),
    )
    layer(
        "formation-latch",
        (
            gate("CNOT", (block.bus[-1], block.formed), f"formation-latch:e{block.event}", block.event)
            for block in blocks
        ),
    )

    for lane_index in BUS_LANES[:-1]:
        layer(
            f"acceptance-bus-uncompute-{lane_index}",
            (
                gate(
                    "CNOT",
                    (block.bus[lane_index + 1], block.bus[lane_index]),
                    f"acceptance-bus-uncompute:e{block.event}:lane{lane_index}",
                    block.event,
                )
                for block in blocks
            ),
        )
    layer(
        "fresh-convergence-uncompute",
        (
            gate("TOFFOLI", (block.predecessor_prefix, block.fresh, block.bus[-1]), f"fresh-convergence-uncompute:e{block.event}", block.event)
            for block in blocks
        ),
    )
    layer(
        "predecessor-convergence-uncompute",
        (
            gate("TOFFOLI", (block.convergence, block.predecessor_ready, block.predecessor_prefix), f"predecessor-convergence-uncompute:e{block.event}", block.event)
            for block in blocks
        ),
    )
    layer(
        "pair-convergence-uncompute",
        (
            gate("TOFFOLI", (block.prefix01[-1], block.prefix12[-1], block.convergence), f"pair-convergence-uncompute:e{block.event}", block.event)
            for block in blocks
        ),
    )
    for lane_index in reversed(PACKET_LANES[1:]):
        layer(
            f"prefix-uncompute-{lane_index}",
            (
                gate("TOFFOLI", (prefix[lane_index - 1], match[lane_index], prefix[lane_index]), f"prefix-uncompute:e{block.event}:{name}:lane{lane_index}", block.event)
                for block in blocks
                for name, match, prefix in (
                    ("pair01", block.match01, block.prefix01),
                    ("pair12", block.match12, block.prefix12),
                )
            ),
        )
    layer(
        "prefix-start-uncompute",
        (
            gate("CNOT", (match[0], prefix[0]), f"prefix-start-uncompute:e{block.event}:{name}", block.event)
            for block in blocks
            for name, match, prefix in (
                ("pair01", block.match01, block.prefix01),
                ("pair12", block.match12, block.prefix12),
            )
        ),
    )
    layer(
        "interface-and-pair12-uncompute",
        (
            gate("TOFFOLI", (block.replicas[1][lane], block.replicas[2][lane], block.match12[lane]), f"interface-and-uncompute:e{block.event}:pair12:lane{lane}", block.event)
            for block in blocks
            for lane in PRESENCE_LANES + (CLOSE_LANE, PROVENANCE_LANE)
        ),
    )
    layer(
        "interface-and-pair01-uncompute",
        (
            gate("TOFFOLI", (block.replicas[0][lane], block.replicas[1][lane], block.match01[lane]), f"interface-and-uncompute:e{block.event}:pair01:lane{lane}", block.event)
            for block in blocks
            for lane in PRESENCE_LANES + (CLOSE_LANE, PROVENANCE_LANE)
        ),
    )
    for name, left_index, right_index, match_name in (
        ("pair12", 1, 2, "match12"),
        ("pair01", 0, 1, "match01"),
    ):
        layer(
            f"payload-match-{name}-invert-uncompute",
            (
                gate("X", (getattr(block, match_name)[lane],), f"payload-match-invert-uncompute:e{block.event}:{name}:lane{lane}", block.event)
                for block in blocks
                for lane in PAYLOAD_LANES
            ),
        )
        layer(
            f"payload-match-{name}-right-uncompute",
            (
                gate("CNOT", (block.replicas[right_index][lane], getattr(block, match_name)[lane]), f"payload-match-right-uncompute:e{block.event}:{name}:lane{lane}", block.event)
                for block in blocks
                for lane in PAYLOAD_LANES
            ),
        )
        layer(
            f"payload-match-{name}-left-uncompute",
            (
                gate("CNOT", (block.replicas[left_index][lane], getattr(block, match_name)[lane]), f"payload-match-left-uncompute:e{block.event}:{name}:lane{lane}", block.event)
                for block in blocks
                for lane in PAYLOAD_LANES
            ),
        )
    layer(
        "fresh-consume",
        (
            gate("CONSUME", (block.formed, block.fresh), f"fresh-consume:e{block.event}", block.event)
            for block in blocks
        ),
    )

    expected_layers = 269
    if len(layers) != expected_layers:
        raise RuntimeError(("fixed threshold circuit layer drift", len(layers), expected_layers))
    return Layout(count, tuple(sites), tuple(blocks), tuple(layers))


def support_connected_nn(item: Gate, sites: tuple[Site, ...]) -> bool:
    coords = tuple(sites[index].coord for index in item.sites)
    reached = {0}
    while True:
        grown = reached | {
            right
            for left in reached
            for right in range(len(coords))
            if c362.c353.manhattan(coords[left], coords[right]) == 1
        }
        if grown == reached:
            return len(reached) == len(coords)
        reached = grown


def layer_conflicts(layer: Layer) -> int:
    used: set[int] = set()
    conflicts = 0
    for item in layer.gates:
        conflicts += len(used.intersection(item.sites))
        used.update(item.sites)
    return conflicts


def validate_layout(layout: Layout) -> None:
    if len(layout.sites) != len({site.coord for site in layout.sites}):
        raise RuntimeError("layout coordinates overlap")
    for layer in layout.layers:
        if layer_conflicts(layer):
            raise RuntimeError(("layer conflict", layer.name))
        for item in layer.gates:
            if len(item.sites) > 3 or not support_connected_nn(item, layout.sites):
                raise RuntimeError(("nonlocal candidate-law gate", item))


def validate_basis(state: BasisState) -> None:
    if not isinstance(state, BasisState):
        raise TypeError("candidate law requires one BasisState")
    if not isinstance(state.bits, tuple) or len(state.bits) != len(state.layout.sites):
        raise ValueError("physical basis width mismatch")
    if any(bit not in (0, 1) for bit in state.bits):
        raise ValueError("physical basis state is not binary")


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "X":
        bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "TOFFOLI":
        first, second, target = item.sites
        bits[target] ^= bits[first] & bits[second]
    elif item.kind == "CONSUME":
        formed, fresh = item.sites
        if bits[formed]:
            bits[fresh] = 0
    else:
        raise ValueError(item.kind)


def apply_layers(
    state: BasisState,
    layers: tuple[Layer, ...],
    *,
    reverse: bool = False,
) -> BasisState:
    validate_basis(state)
    bits = list(state.bits)
    ordered_layers = reversed(layers) if reverse else layers
    for layer in ordered_layers:
        ordered_gates = reversed(layer.gates) if reverse else layer.gates
        for item in ordered_gates:
            if reverse and item.kind == "CONSUME":
                raise ValueError("the hypothesized nonunitary commit has no inverse")
            apply_gate(bits, item)
    return replace(state, bits=tuple(bits))


def step(state):
    """Apply fixed reversible calculation then the supplied atomic commit."""

    validate_basis(state)
    return apply_layers(state, state.layout.layers)


def validate_replica(replica: ReplicaCandidate) -> None:
    if not isinstance(replica, ReplicaCandidate):
        raise TypeError("replica must carry the explicit candidate interface")
    if (
        not isinstance(replica.payload, tuple)
        or len(replica.payload) != c364.RECORD_BITS
        or any(bit not in (0, 1) for bit in replica.payload)
        or not isinstance(replica.payload_present, tuple)
        or len(replica.payload_present) != c364.RECORD_BITS
        or any(bit not in (0, 1) for bit in replica.payload_present)
    ):
        raise ValueError("replica payload or presence mask is outside the 30-bit domain")
    if not isinstance(replica.close, c364.FaithfulCloseInterface):
        raise TypeError("replica lacks the Cycle-361 close interface")
    if not isinstance(replica.provenance, c364.ProvenanceInterface):
        raise TypeError("replica lacks the Cycle-362 provenance interface")


def validate_proposal(proposal: RedundantProposal) -> None:
    if not isinstance(proposal, RedundantProposal):
        raise TypeError("threshold law requires one RedundantProposal")
    if not c364.valid_coord(proposal.site):
        raise ValueError("proposal target is outside the cubic domain")
    if (
        not isinstance(proposal.payload, tuple)
        or len(proposal.payload) != c364.RECORD_BITS
        or any(bit not in (0, 1) for bit in proposal.payload)
    ):
        raise ValueError("proposal payload is outside the 30-bit domain")
    if not isinstance(proposal.readiness, c364.ReadinessInterface):
        raise TypeError("proposal lacks the Cycle-364 readiness interface")
    predecessors = proposal.readiness.predecessors
    if (
        not c364.valid_coord(proposal.readiness.site)
        or not isinstance(predecessors, tuple)
        or len(predecessors) > c364.MAX_PREDECESSORS
        or len(set(predecessors)) != len(predecessors)
        or proposal.site in predecessors
        or any(not c364.valid_coord(item) for item in predecessors)
        or any(c364.distance(proposal.site, item) > c364.LOCAL_RADIUS for item in predecessors)
        or not c364.bit(proposal.readiness.predecessors_ready)
        or not c364.bit(proposal.readiness.fresh)
        or proposal.readiness.source != c364.READINESS_SOURCE
    ):
        raise ValueError("readiness interface is outside the Cycle-364 local domain")
    if not isinstance(proposal.replicas, tuple) or len(proposal.replicas) > FORMATION_THRESHOLD:
        raise ValueError("candidate multiplicity is outside the explicit threshold-three domain")
    for replica in proposal.replicas:
        validate_replica(replica)
        c364.validate_proposal(
            c364.FormationProposal(
                proposal.site,
                replica.payload,
                replica.payload_present,
                replica.close,
                proposal.readiness,
                replica.provenance,
            )
        )


def interface_replica(base: c364.FormationProposal) -> ReplicaCandidate:
    return ReplicaCandidate(base.payload, base.payload_present, base.close, base.provenance)


def redundant_from_immediate(
    base: c364.FormationProposal,
    count: int | None = None,
) -> RedundantProposal:
    c364.validate_proposal(base)
    multiplicity = (
        base.provenance.independent_confirmations if count is None else count
    )
    if not isinstance(multiplicity, int) or isinstance(multiplicity, bool) or not 0 <= multiplicity <= FORMATION_THRESHOLD:
        raise ValueError("independent candidate multiplicity is outside 0..3")
    return RedundantProposal(
        base.site,
        base.payload,
        base.readiness,
        tuple(interface_replica(base) for _ in range(multiplicity)),
    )


def encode_replica(
    bits: list[int],
    block: EventBlock,
    replica_index: int,
    proposal: RedundantProposal,
    replica: ReplicaCandidate,
) -> None:
    carrier = block.replicas[replica_index]
    for lane, value in zip(PAYLOAD_LANES, replica.payload):
        bits[carrier[lane]] = value
    for lane, value in zip(PRESENCE_LANES, replica.payload_present):
        bits[carrier[lane]] = value
    close_ok = bool(
        replica.close.close_candidate
        and replica.close.site == proposal.site
        and replica.close.payload == replica.payload == proposal.payload
        and replica.close.source == c364.CLOSE_SOURCE
    )
    provenance_ok = bool(
        replica.provenance.accepted
        and replica.provenance.site == proposal.site
        and replica.provenance.payload == replica.payload == proposal.payload
        and replica.provenance.predecessors == proposal.readiness.predecessors
        and replica.provenance.source == c364.PROVENANCE_SOURCE
    )
    bits[carrier[CLOSE_LANE]] = int(close_ok)
    bits[carrier[PROVENANCE_LANE]] = int(provenance_ok)


def prepare(
    layout: Layout,
    assignments: tuple[tuple[int, RedundantProposal], ...],
) -> Prepared:
    if not isinstance(assignments, tuple):
        raise TypeError("assignments must be a tuple")
    bits = [0] * len(layout.sites)
    updated_blocks = list(layout.blocks)
    reasons: list[str] = []
    statuses: list[str] = []
    by_event: dict[int, RedundantProposal] = {}
    for event, proposal in assignments:
        if not isinstance(event, int) or isinstance(event, bool) or not 0 <= event < layout.count:
            reasons.append("event-domain")
            statuses.append("rejected:event-domain")
            continue
        validate_proposal(proposal)
        if proposal.site != layout.blocks[event].target_site:
            reasons.append("target-block-mismatch")
            statuses.append("rejected:target-block-mismatch")
            continue
        if event in by_event:
            if by_event[event] == proposal:
                statuses.append("overlap-identical-coalesced")
            else:
                reasons.append("overlap-conflict:same-target")
                statuses.append("overlap-conflict:same-target")
            continue
        by_event[event] = proposal
        statuses.append("installed")
    if reasons:
        return Prepared(BasisState(layout, tuple(bits)), False, tuple(reasons), tuple(statuses))
    for event, proposal in by_event.items():
        block = layout.blocks[event]
        updated_blocks[event] = replace(
            block,
            predecessors=proposal.readiness.predecessors,
        )
        readiness_ok = bool(
            proposal.readiness.site == proposal.site
            and proposal.readiness.predecessors_ready
            and proposal.readiness.source == c364.READINESS_SOURCE
        )
        fresh_ok = bool(
            proposal.readiness.site == proposal.site
            and proposal.readiness.fresh
            and proposal.readiness.source == c364.READINESS_SOURCE
        )
        bits[block.predecessor_ready] = int(readiness_ok)
        bits[block.fresh] = int(fresh_ok)
        for replica_index, replica in enumerate(proposal.replicas):
            encode_replica(bits, block, replica_index, proposal, replica)
    installed_layout = replace(layout, blocks=tuple(updated_blocks))
    return Prepared(BasisState(installed_layout, tuple(bits)), True, (), tuple(statuses))


def output_word(state: BasisState, block: EventBlock) -> Word:
    return tuple(state.bits[offset] for offset in block.output)


def logical_records(state: BasisState) -> tuple[ThresholdSiteContentRecord, ...]:
    return tuple(
        ThresholdSiteContentRecord(
            block.target_site,
            output_word(state, block),
            block.predecessors,
        )
        for block in state.layout.blocks
        if state.bits[block.formed] and not state.bits[block.fresh]
    )


def workspace_leakage(state: BasisState) -> int:
    return sum(
        state.bits[offset]
        for block in state.layout.blocks
        for offset in (
            block.match01
            + block.match12
            + block.prefix01
            + block.prefix12
            + block.bus
            + (block.convergence, block.predecessor_prefix)
        )
    )


def immutable_input_bits(state: BasisState) -> tuple[int, ...]:
    return tuple(
        state.bits[offset]
        for block in state.layout.blocks
        for offset in tuple(item for replica in block.replicas for item in replica)
        + (block.predecessor_ready,)
    )


def candidate_count(state: BasisState, block: EventBlock) -> int:
    return sum(
        bool(
            state.bits[block.replicas[index][CLOSE_LANE]]
            and state.bits[block.replicas[index][PROVENANCE_LANE]]
            and all(state.bits[block.replicas[index][lane]] for lane in PRESENCE_LANES)
        )
        for index in REPLICAS
    )


def readable_majority(state: BasisState, block: EventBlock) -> Word | None:
    words = [
        tuple(state.bits[block.replicas[index][lane]] for lane in PAYLOAD_LANES)
        for index in REPLICAS
        if all(state.bits[block.replicas[index][lane]] for lane in PRESENCE_LANES)
        and state.bits[block.replicas[index][CLOSE_LANE]]
        and state.bits[block.replicas[index][PROVENANCE_LANE]]
    ]
    if len(words) < 2:
        return None
    return tuple(int(sum(word[bit] for word in words) * 2 >= len(words)) for bit in PAYLOAD_LANES)


def record_words(fixture: c364.c342.c338.RouteFixture, count: int) -> tuple[Word, ...]:
    cylinders = c364.c342.make_cylinder_chain(fixture, endpoint=0, count=count)
    records = tuple(c364.c342.form_conditional_record(fixture, item) for item in cylinders)
    return tuple(c364.c342.record_word(item) for item in records)


def immediate_proposal(block: EventBlock, word: Word, confirmations: int) -> c364.FormationProposal:
    return c364.proposal(block.target_site, word, confirmations=confirmations)


def geometry_and_fixed_rule_controls() -> dict[str, object]:
    frames = c362.c353.proper_cubic_frames()
    rows = []
    failures = 0
    for count in SIZES:
        layout = build_layout(count)
        validate_layout(layout)
        rotated_failures = 0
        for frame in frames:
            framed_sites = tuple(
                replace(site, coord=c362.c353.rotated(site.coord, frame))
                for site in layout.sites
            )
            rotated_failures += sum(
                not support_connected_nn(item, framed_sites)
                for layer in layout.layers
                for item in layer.gates
            )
        row = {
            "N": count,
            "held": count == HELD_SIZE,
            "M2_sites": len(layout.sites),
            "M2_per_convergence_event": len(layout.sites) // count,
            "fixed_layers": len(layout.layers),
            "primitive_gates": sum(len(layer.gates) for layer in layout.layers),
            "maximum_gate_support": max(len(item.sites) for layer in layout.layers for item in layer.gates),
            "connected_NN_failures": sum(
                not support_connected_nn(item, layout.sites)
                for layer in layout.layers
                for item in layer.gates
            ),
            "rotated_connected_NN_failures": rotated_failures,
            "layer_conflicts": sum(layer_conflicts(layer) for layer in layout.layers),
        }
        failures += row["connected_NN_failures"] + row["rotated_connected_NN_failures"] + row["layer_conflicts"]
        failures += int(row["maximum_gate_support"] > 3)
        rows.append(row)
    source = getsource(step).lower()
    forbidden = ("active_event", "candidate_count", "formation_threshold", "if state", "host_index")
    hits = tuple(item for item in forbidden if item in source)
    check(
        "one fixed state-only Boolean realization has constant overhead and connected-NN support in all proper-cubic frames",
        failures == 0
        and len(frames) == 24
        and tuple(signature(step).parameters) == ("state",)
        and not hits
        and len({row["M2_per_convergence_event"] for row in rows}) == 1
        and len({row["fixed_layers"] for row in rows}) == 1,
        {
            "rows": rows,
            "proper_cubic_frames": len(frames),
            "step_parameters": tuple(signature(step).parameters),
            "forbidden_dispatch_hits": hits,
            "state_dependent_gate_selection": False,
            "allowed_reversible_calculation_gates": ("X", "CNOT", "TOFFOLI"),
            "hypothesized_nonunitary_commit_gate": "CONSUME",
            "allowed_physical_M2_gate_compiler_claim": False,
        },
    )
    return {"rows": rows, "failures": failures}


def threshold_truth_and_discriminator_controls() -> dict[str, object]:
    fixture = c364.c342.c338.build_fixture(3)
    layout = build_layout(1)
    word = record_words(fixture, 1)[0]
    rows = []
    failures = 0
    for count in (1, 2, 3):
        base = immediate_proposal(layout.blocks[0], word, count)
        redundant = redundant_from_immediate(base)
        prepared = prepare(layout, ((0, redundant),))
        final = step(prepared.state)
        records = logical_records(final)
        expected = int(count == FORMATION_THRESHOLD)
        failures += int(
            not prepared.admissible
            or len(records) != expected
            or candidate_count(prepared.state, layout.blocks[0]) != count
            or workspace_leakage(final) != 0
            or immutable_input_bits(final) != immutable_input_bits(prepared.state)
        )
        if records:
            failures += int(records[0].content != word or records[0].site != layout.blocks[0].target_site)
        rows.append(
            {
                "independent_close_provenance_candidates": count,
                "formed_convergence_site_Records": len(records),
                "carrier_candidates_typed_as_Records": 0,
                "fresh_after": final.bits[layout.blocks[0].fresh],
                "workspace_leakage": workspace_leakage(final),
            }
        )
    one = immediate_proposal(layout.blocks[0], word, 1)
    immediate = c364.apply_candidate_law(fixture, c364.FormationState(), one)
    threshold = step(prepare(layout, ((0, redundant_from_immediate(one)),)).state)
    discriminator = {
        "same_valid_Cycle364_proposal_confirmations": one.provenance.independent_confirmations,
        "Cycle364_status": immediate.status,
        "Cycle364_formed": immediate.formed is not None,
        "Cycle366_formed": bool(logical_records(threshold)),
    }
    failures += int(
        immediate.status != "formed"
        or immediate.formed is None
        or logical_records(threshold) != ()
    )
    three_base = immediate_proposal(
        layout.blocks[0], word, FORMATION_THRESHOLD
    )
    three = redundant_from_immediate(three_base)
    incomplete_mask = list(three.replicas[2].payload_present)
    incomplete_mask[0] = 0
    closures = {
        "predecessor_not_ready": replace(
            three,
            readiness=replace(three.readiness, predecessors_ready=0),
        ),
        "target_not_fresh": replace(
            three,
            readiness=replace(three.readiness, fresh=0),
        ),
        "one_payload_presence_bit_missing": replace(
            three,
            replicas=three.replicas[:2]
            + (replace(three.replicas[2], payload_present=tuple(incomplete_mask)),),
        ),
    }
    closure_rows = {}
    for name, item in closures.items():
        prepared = prepare(layout, ((0, item),))
        final = step(prepared.state)
        closure_rows[name] = {
            "formed": len(logical_records(final)),
            "workspace_leakage": workspace_leakage(final),
        }
        failures += int(
            not prepared.admissible
            or logical_records(final) != ()
            or workspace_leakage(final) != 0
        )
    check(
        "threshold three is exact and discriminates the immediate site-tethered law on the same one-close proposal",
        failures == 0,
        {
            "explicit_law_parameter_threshold": FORMATION_THRESHOLD,
            "threshold_derived": False,
            "rows": rows,
            "fresh_predecessor_completeness_closures": closure_rows,
            "Cycle364_discriminator": discriminator,
            "three_carriers_are_one_Record_quotient": False,
        },
    )
    return {"rows": rows, "failures": failures}


def reversible_calculation_and_atomic_commit_controls() -> dict[str, object]:
    fixture = c364.c342.c338.build_fixture(3)
    layout = build_layout(1)
    word = record_words(fixture, 1)[0]
    proposal = redundant_from_immediate(
        immediate_proposal(
            layout.blocks[0],
            word,
            FORMATION_THRESHOLD,
        )
    )
    source = prepare(layout, ((0, proposal),)).state
    reversible_layers = layout.layers[:-1]
    commit_layer = (layout.layers[-1],)
    reversible_kinds = {
        item.kind
        for layer in reversible_layers
        for item in layer.gates
    }
    commit_kinds = {
        item.kind
        for layer in commit_layer
        for item in layer.gates
    }
    calculated = apply_layers(source, reversible_layers)
    restored = apply_layers(calculated, reversible_layers, reverse=True)
    committed = apply_layers(calculated, commit_layer)
    inverse_commit_rejections = 0
    try:
        apply_layers(committed, commit_layer, reverse=True)
    except ValueError:
        inverse_commit_rejections += 1
    detail = {
        "reversible_calculation_gate_kinds": tuple(sorted(reversible_kinds)),
        "atomic_commit_gate_kinds": tuple(sorted(commit_kinds)),
        "calculation_workspace_leakage": workspace_leakage(calculated),
        "calculation_formed_bit": calculated.bits[layout.blocks[0].formed],
        "calculation_fresh_bit": calculated.bits[layout.blocks[0].fresh],
        "logical_Records_before_commit": len(logical_records(calculated)),
        "exact_reversible_calculation_inverse": restored == source,
        "logical_Records_after_commit": len(logical_records(committed)),
        "committed_content_residual": sum(
            a != b
            for a, b in zip(output_word(committed, layout.blocks[0]), word)
        ),
        "atomic_commit_inverse_rejections": inverse_commit_rejections,
        "commit_semantics": "CONSUME: if formed=1 set fresh=0; otherwise leave fresh unchanged",
        "commit_admitted_by_existing_framework_law": None,
    }
    check(
        "reversible X/CNOT/Toffoli calculation remains non-Record until the isolated hypothesized nonunitary commit",
        reversible_kinds == {"X", "CNOT", "TOFFOLI"}
        and commit_kinds == {"CONSUME"}
        and detail["calculation_workspace_leakage"] == 0
        and detail["calculation_formed_bit"] == 1
        and detail["calculation_fresh_bit"] == 1
        and detail["logical_Records_before_commit"] == 0
        and detail["exact_reversible_calculation_inverse"]
        and detail["logical_Records_after_commit"] == 1
        and detail["committed_content_residual"] == 0
        and detail["atomic_commit_inverse_rejections"] == 1
        and detail["commit_admitted_by_existing_framework_law"] is None,
        detail,
    )
    return detail


def held_size_and_covariance_controls() -> dict[str, object]:
    frames = c362.c353.proper_cubic_frames()
    rows = []
    cases = held_cases = bit_residual = record_residual = adjacency_failures = 0
    for length in LENGTHS:
        fixture = c364.c342.c338.build_fixture(length)
        for count in SIZES:
            layout = build_layout(count)
            words = record_words(fixture, count)
            assignments = tuple(
                (
                    event,
                    redundant_from_immediate(
                        immediate_proposal(layout.blocks[event], words[event], FORMATION_THRESHOLD)
                    ),
                )
                for event in range(count)
            )
            prepared = prepare(layout, assignments)
            reference = step(prepared.state)
            reference_records = logical_records(reference)
            source_layout = prepared.state.layout
            model_failure = int(
                not prepared.admissible
                or len(reference_records) != count
                or workspace_leakage(reference) != 0
                or any(record.content != word for record, word in zip(reference_records, words))
            )
            rows.append(
                {
                    "L": length,
                    "N": count,
                    "held": length == 6 and count == HELD_SIZE,
                    "formed_logical_Records": len(reference_records),
                    "formation_failures": model_failure,
                    "workspace_leakage": workspace_leakage(reference),
                }
            )
            for frame in frames:
                rotated_sites = tuple(
                    replace(site, coord=c362.c353.rotated(site.coord, frame))
                    for site in source_layout.sites
                )
                rotated_blocks = tuple(
                    replace(
                        block,
                        target_site=c362.c353.rotated(block.target_site, frame),
                        predecessors=tuple(
                            c362.c353.rotated(item, frame)
                            for item in block.predecessors
                        ),
                    )
                    for block in source_layout.blocks
                )
                framed = replace(
                    prepared.state,
                    layout=replace(
                        source_layout,
                        sites=rotated_sites,
                        blocks=rotated_blocks,
                    ),
                )
                framed_final = step(framed)
                cases += 1
                held_cases += int(length == 6 and count == HELD_SIZE)
                bit_residual += sum(a != b for a, b in zip(reference.bits, framed_final.bits))
                framed_records = logical_records(framed_final)
                record_residual += int(
                    tuple(record.content for record in framed_records) != tuple(record.content for record in reference_records)
                    or tuple(record.site for record in framed_records)
                    != tuple(c362.c353.rotated(record.site, frame) for record in reference_records)
                )
                adjacency_failures += sum(
                    not support_connected_nn(item, framed.layout.sites)
                    for layer in framed.layout.layers
                    for item in layer.gates
                )
    failures = sum(row["formation_failures"] for row in rows) + bit_residual + record_residual + adjacency_failures
    check(
        "L3/L6 N6/N12/held-N18 formation is exact and covariant in all 24 proper-cubic frames",
        cases == 144 and held_cases == 24 and failures == 0,
        {
            "rows": rows,
            "L_by_N_by_frame_cases": cases,
            "held_L6_N18_frame_cases": held_cases,
            "state_bit_residual": bit_residual,
            "logical_Record_covariance_residual": record_residual,
            "rotated_adjacency_failures": adjacency_failures,
        },
    )
    return {"rows": rows, "failures": failures}


def fault_and_distinct_event_controls() -> dict[str, object]:
    fixture = c364.c342.c338.build_fixture(6)
    layout = build_layout(2)
    word, alternative = record_words(fixture, 2)
    base0 = immediate_proposal(layout.blocks[0], word, FORMATION_THRESHOLD)
    good = interface_replica(base0)
    nominal_source = prepare(
        layout,
        ((0, redundant_from_immediate(base0)),),
    ).state
    exhaustive_corruption_cases = 0
    exhaustive_corruption_failures = 0
    for replica_index in REPLICAS:
        for bit in PAYLOAD_LANES:
            values = list(nominal_source.bits)
            values[layout.blocks[0].replicas[replica_index][bit]] ^= 1
            source = replace(nominal_source, bits=tuple(values))
            final = step(source)
            exhaustive_corruption_cases += 1
            exhaustive_corruption_failures += int(
                logical_records(final) != ()
                or readable_majority(final, layout.blocks[0]) != word
                or immutable_input_bits(final) != immutable_input_bits(source)
                or workspace_leakage(final) != 0
            )
    exhaustive_deletion_cases = 0
    exhaustive_deletion_failures = 0
    for replica_index in REPLICAS:
        values = list(nominal_source.bits)
        for offset in layout.blocks[0].replicas[replica_index]:
            values[offset] = 0
        source = replace(nominal_source, bits=tuple(values))
        final = step(source)
        exhaustive_deletion_cases += 1
        exhaustive_deletion_failures += int(
            logical_records(final) != ()
            or readable_majority(final, layout.blocks[0]) != word
            or immutable_input_bits(final) != immutable_input_bits(source)
            or workspace_leakage(final) != 0
        )
    corrupted_payload = list(word)
    corrupted_payload[0] ^= 1
    corrupted_word = tuple(corrupted_payload)
    corrupted = replace(
        good,
        payload=corrupted_word,
        close=replace(good.close, payload=corrupted_word),
        provenance=replace(good.provenance, payload=corrupted_word),
    )
    corrupt_proposal = RedundantProposal(base0.site, word, base0.readiness, (good, good, corrupted))
    corrupt_source = prepare(layout, ((0, corrupt_proposal),)).state
    corrupt_final = step(corrupt_source)

    deleted_proposal = RedundantProposal(base0.site, word, base0.readiness, (good, good))
    deleted_source = prepare(layout, ((0, deleted_proposal),)).state
    deleted_final = step(deleted_source)

    base1 = immediate_proposal(layout.blocks[1], word, 1)
    separated = prepare(
        layout,
        (
            (0, RedundantProposal(base0.site, word, base0.readiness, (good, good))),
            (1, redundant_from_immediate(base1)),
        ),
    )
    separated_final = step(separated.state)
    wrong_event_replica = replace(
        good,
        provenance=replace(good.provenance, site=layout.blocks[1].target_site),
    )
    mixed = prepare(
        layout,
        ((0, RedundantProposal(base0.site, word, base0.readiness, (good, good, wrong_event_replica))),),
    )
    mixed_final = step(mixed.state)

    detail = {
        "one_replica_corruption_formed": bool(logical_records(corrupt_final)),
        "one_replica_corruption_majority_content_readable": readable_majority(corrupt_final, layout.blocks[0]) == word,
        "one_replica_corruption_identity_readable": layout.blocks[0].target_site == base0.site,
        "one_replica_deletion_formed": bool(logical_records(deleted_final)),
        "one_replica_deletion_majority_content_readable": readable_majority(deleted_final, layout.blocks[0]) == word,
        "one_replica_deletion_identity_readable": layout.blocks[0].target_site == base0.site,
        "separate_event_equal_content_formed": len(logical_records(separated_final)),
        "mixed_event_equal_content_formed": len(logical_records(mixed_final)),
        "corrupt_input_preserved": immutable_input_bits(corrupt_final) == immutable_input_bits(corrupt_source),
        "deleted_input_preserved": immutable_input_bits(deleted_final) == immutable_input_bits(deleted_source),
        "workspace_leakage": workspace_leakage(corrupt_final) + workspace_leakage(deleted_final) + workspace_leakage(separated_final) + workspace_leakage(mixed_final),
        "all_payload_bit_by_replica_corruption_cases": exhaustive_corruption_cases,
        "all_payload_bit_by_replica_corruption_failures": exhaustive_corruption_failures,
        "each_replica_deletion_cases": exhaustive_deletion_cases,
        "each_replica_deletion_failures": exhaustive_deletion_failures,
        "unused_alternative_word_lawful": c364.payload_lawful(fixture, alternative),
    }
    check(
        "single-replica corruption/deletion is rejected with readable majority content and equal-content distinct events do not merge",
        detail["one_replica_corruption_formed"] is False
        and detail["one_replica_corruption_majority_content_readable"]
        and detail["one_replica_corruption_identity_readable"]
        and detail["one_replica_deletion_formed"] is False
        and detail["one_replica_deletion_majority_content_readable"]
        and detail["one_replica_deletion_identity_readable"]
        and detail["separate_event_equal_content_formed"] == 0
        and detail["mixed_event_equal_content_formed"] == 0
        and detail["corrupt_input_preserved"]
        and detail["deleted_input_preserved"]
        and detail["workspace_leakage"] == 0
        and detail["all_payload_bit_by_replica_corruption_cases"] == 90
        and detail["all_payload_bit_by_replica_corruption_failures"] == 0
        and detail["each_replica_deletion_cases"] == 3
        and detail["each_replica_deletion_failures"] == 0
        and detail["unused_alternative_word_lawful"],
        detail,
    )
    return detail


def overwrite_commutation_and_overlap_controls() -> dict[str, object]:
    fixture = c364.c342.c338.build_fixture(3)
    layout = build_layout(2)
    word, alternative = record_words(fixture, 2)
    proposals = tuple(
        redundant_from_immediate(
            immediate_proposal(layout.blocks[event], word if event == 0 else alternative, FORMATION_THRESHOLD)
        )
        for event in range(2)
    )
    prepared = prepare(layout, tuple(enumerate(proposals)))
    global_final = step(prepared.state)
    first_then_second = apply_layers(
        apply_layers(
            prepared.state,
            tuple(Layer(layer.name, tuple(g for g in layer.gates if g.event == 0)) for layer in layout.layers),
        ),
        tuple(Layer(layer.name, tuple(g for g in layer.gates if g.event == 1)) for layer in layout.layers),
    )
    second_then_first = apply_layers(
        apply_layers(
            prepared.state,
            tuple(Layer(layer.name, tuple(g for g in layer.gates if g.event == 1)) for layer in layout.layers),
        ),
        tuple(Layer(layer.name, tuple(g for g in layer.gates if g.event == 0)) for layer in layout.layers),
    )

    repeated = step(global_final)
    overwritten_bits = list(global_final.bits)
    block = layout.blocks[0]
    for replica in block.replicas:
        for lane, value in zip(PAYLOAD_LANES, alternative):
            overwritten_bits[replica[lane]] = value
    overwrite_source = replace(global_final, bits=tuple(overwritten_bits))
    overwrite_final = step(overwrite_source)

    identical_overlap = prepare(layout, ((0, proposals[0]), (0, proposals[0])))
    conflicting_base = immediate_proposal(
        layout.blocks[0], alternative, FORMATION_THRESHOLD
    )
    conflicting_proposal = redundant_from_immediate(conflicting_base)
    conflicting_overlap = prepare(
        layout,
        ((0, proposals[0]), (0, conflicting_proposal)),
    )
    detail = {
        "disjoint_global_matches_0_then_1": global_final == first_then_second,
        "disjoint_global_matches_1_then_0": global_final == second_then_first,
        "formed_state_is_idempotent": repeated == global_final,
        "overwrite_output_content_residual": sum(
            a != b
            for a, b in zip(output_word(overwrite_final, block), output_word(global_final, block))
        ),
        "overwrite_identity_preserved": logical_records(overwrite_final)[0].site == logical_records(global_final)[0].site,
        "overwrite_formed_flag_preserved": overwrite_final.bits[block.formed] == 1,
        "identical_overlap_admissible": identical_overlap.admissible,
        "identical_overlap_status": identical_overlap.overlap_status,
        "conflicting_overlap_admissible": conflicting_overlap.admissible,
        "conflicting_overlap_reasons": conflicting_overlap.reasons,
        "priority_rule": None,
    }
    check(
        "disjoint formations commute, lawful continuation cannot overwrite, and identical/conflicting overlap has an exact no-priority rule",
        detail["disjoint_global_matches_0_then_1"]
        and detail["disjoint_global_matches_1_then_0"]
        and detail["formed_state_is_idempotent"]
        and detail["overwrite_output_content_residual"] == 0
        and detail["overwrite_identity_preserved"]
        and detail["overwrite_formed_flag_preserved"]
        and detail["identical_overlap_admissible"]
        and detail["identical_overlap_status"] == ("installed", "overlap-identical-coalesced")
        and detail["conflicting_overlap_admissible"] is False
        and detail["conflicting_overlap_reasons"] == ("overlap-conflict:same-target",)
        and detail["priority_rule"] is None,
        detail,
    )
    return detail


def remove_target(layout: Layout, layer_name: str, label: str) -> tuple[tuple[Layer, ...], int]:
    removed = 0
    answer = []
    for layer in layout.layers:
        gates = []
        for item in layer.gates:
            if layer.name == layer_name and item.label == label:
                removed += 1
            else:
                gates.append(item)
        answer.append(Layer(layer.name, tuple(gates)))
    return tuple(answer), removed


def deletion_controls() -> dict[str, object]:
    fixture = c364.c342.c338.build_fixture(6)
    layout = build_layout(1)
    word = record_words(fixture, 1)[0]
    proposal = redundant_from_immediate(immediate_proposal(layout.blocks[0], word, FORMATION_THRESHOLD))
    source = prepare(layout, ((0, proposal),)).state
    ideal = step(source)
    one_bit = word.index(1)
    attacks = (
        ("payload_match", "payload-match-pair01-invert", f"payload-match-invert:e0:pair01:lane{one_bit}"),
        ("presence", "interface-and-pair01", f"interface-and:e0:pair01:lane{PRESENCE_LANES[0]}"),
        ("faithful_close", "interface-and-pair01", f"interface-and:e0:pair01:lane{CLOSE_LANE}"),
        ("common_provenance", "interface-and-pair01", f"interface-and:e0:pair01:lane{PROVENANCE_LANE}"),
        ("convergence", "pair-convergence", "pair-convergence:e0"),
        ("content_write", "write-once-content", f"write-once:e0:bit{one_bit}"),
        ("formation_latch", "formation-latch", "formation-latch:e0"),
        ("cleanup", "fresh-convergence-uncompute", "fresh-convergence-uncompute:e0"),
    )
    rows = []
    failures = 0
    for kind, layer_name, label in attacks:
        layers, removed = remove_target(layout, layer_name, label)
        attacked = apply_layers(source, layers)
        output_residual = sum(a != b for a, b in zip(attacked.bits, ideal.bits))
        records = logical_records(attacked)
        valid_record = bool(
            len(records) == 1
            and records[0].content == word
            and c364.payload_lawful(fixture, records[0].content)
        )
        visible = output_residual > 0 and (not valid_record or workspace_leakage(attacked) > 0)
        failures += int(removed != 1 or not visible)
        rows.append(
            {
                "class": kind,
                "deleted_layer": layer_name,
                "deleted_label": label,
                "removed_gates": removed,
                "output_bit_residual": output_residual,
                "formed_records": len(records),
                "valid_Record": valid_record,
                "workspace_leakage": workspace_leakage(attacked),
                "visible": visible,
            }
        )
    check(
        "payload/presence/close/provenance/convergence/write/latch/cleanup deletions are exactly visible",
        failures == 0,
        {"rows": rows, "deletion_failures": failures},
    )
    return {"rows": rows, "failures": failures}


def lawful_domain_controls() -> dict[str, int]:
    attempts = rejections = 0

    def rejected(callable_) -> None:
        nonlocal attempts, rejections
        attempts += 1
        try:
            callable_()
        except (TypeError, ValueError):
            rejections += 1

    rejected(lambda: build_layout(0))
    rejected(lambda: build_layout(True))
    layout = build_layout(1)
    fixture = c364.c342.c338.build_fixture(3)
    word = record_words(fixture, 1)[0]
    base = immediate_proposal(layout.blocks[0], word, 1)
    state = prepare(layout, ((0, redundant_from_immediate(base)),)).state
    rejected(lambda: step(replace(state, bits=state.bits[:-1])))
    malformed = list(state.bits)
    malformed[0] = 2
    rejected(lambda: step(replace(state, bits=tuple(malformed))))
    rejected(lambda: step(state.bits))
    rejected(lambda: redundant_from_immediate(base, 4))
    bad_replica = replace(interface_replica(base), payload=(0,) * 29)
    rejected(lambda: validate_proposal(RedundantProposal(base.site, word, base.readiness, (bad_replica,))))
    wrong_target = replace(redundant_from_immediate(base), site=(99, 0, 0))
    prepared_wrong = prepare(layout, ((0, wrong_target),))
    attempts += 1
    rejections += int(not prepared_wrong.admissible and prepared_wrong.reasons == ("target-block-mismatch",))
    prepared_event = prepare(layout, ((1, redundant_from_immediate(base)),))
    attempts += 1
    rejections += int(not prepared_event.admissible and prepared_event.reasons == ("event-domain",))
    check(
        "malformed layouts, basis states, multiplicities, payloads, targets, and event assignments are rejected",
        attempts == rejections,
        {"attempts": attempts, "rejections": rejections},
    )
    return {"attempts": attempts, "rejections": rejections}


def inherited_physics_controls() -> dict[str, object]:
    expected_contact = np.diag((np.exp(1j * c317.c311.COUPLING), 1)).astype(complex)
    rows = []
    failures = 0
    for length in LENGTHS:
        fixture = c317.physical_fixture(length)
        projector = fixture.full_encoding @ fixture.full_encoding.conj().T
        row = {
            "L": length,
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
    one_particle_residual = float(np.linalg.norm(one_particle - species.coin))
    mass_residual = abs(c317.c311.c219.rest_mass(species) / species.analytic_mass - 1)
    failures += int(one_particle_residual > TOL or mass_residual > 3e-12)
    check(
        "the threshold-formation sidecar preserves the inherited one-particle mass and Cycle-230 seam contact fixtures",
        failures == 0,
        {
            "rows": rows,
            "one_particle_matrix_residual": one_particle_residual,
            "mass_relative_residual": mass_residual,
        },
    )
    return {"rows": rows, "mass_residual": mass_residual, "failures": failures}


def supplied_structure_and_prior_art_controls() -> dict[str, object]:
    note_text = " ".join(
        (ROOT / PRIOR_ART_NOTE).read_text(encoding="utf-8").lower().split()
    )
    inventory = {
        "candidate_law": LAW_NAME,
        "threshold": FORMATION_THRESHOLD,
        "threshold_derived": False,
        "threshold_justified": False,
        "Record_redundancy_identification_is_supplied_law_content": True,
        "Cycle342_payload_lawfulness_is_supplied_at_interface": True,
        "circuit_derives_Cycle342_payload_lawfulness": False,
        "carrier_candidates_typed_as_Records": False,
        "one_convergence_site_Record_after_threshold": True,
        "supplied": (
            "Cycle-361 faithful-close acceptance per candidate",
            "Cycle-362 common-event provenance acceptance and convergence block",
            "Cycle-364 fresh and predecessor-ready interface",
            "complete 30-bit payload and complete 30-bit presence mask per candidate",
            "three spatially disjoint candidate carriers and blank convergence capacity",
            "fixed reversible X/CNOT/Toffoli calculation schedule and proper-cubic embedding",
            "one hypothesized nonunitary fresh-token consume at the atomic commit boundary",
        ),
        "derived_within_candidate_law": (
            "all-30-bit equality and completeness convergence",
            "one/two dark and exactly-three formation discriminator",
            "reversible conditional convergence-site content write and formation-bit transcript",
            "single-candidate-fault rejection with two-carrier majority readability",
        ),
        "generic_redundancy_objectivity_prior_art": PRIOR_ART_NOTE,
        "prior_art_supplies_quantum_Darwinism_bridge": "quantum-darwinism reading" in note_text,
        "prior_art_says_bridge_is_bounded_input": "explicit bounded inputs" in note_text,
        "novelty_boundary": "exact Cycle-361/362/364 threshold-law interface, discriminators, and bounded NN Boolean realization only",
        "generic_redundancy_as_Record_formation_novelty_claim": False,
        "classification": "fixed connected-NN Boolean basis-state realization of a candidate atomic law",
        "allowed_physical_M2_gate_compiler_claim": False,
        "reversible_calculation_gate_kinds": ("X", "CNOT", "TOFFOLI"),
        "supplied_irreversible_gate_semantics": {
            "CONSUME": "if formed=1 set fresh=0; otherwise leave fresh unchanged",
        },
        "existing_framework_admission_of_CONSUME": None,
        "nonunitary_commit_is_candidate_law_content": True,
        "law_selection": None,
        "Born_or_statistics": None,
        "metric_time": None,
        "threshold_justification": None,
        "renewal": None,
        "full_lattice_completion": None,
        "global_code_precheck": False,
        "state_dependent_host_gate_selection": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "threshold, Record identification, complete interface, prior art, novelty boundary, and open-law inventory are explicit",
        inventory["threshold"] == 3
        and inventory["threshold_derived"] is False
        and inventory["threshold_justified"] is False
        and inventory["Record_redundancy_identification_is_supplied_law_content"]
        and inventory["Cycle342_payload_lawfulness_is_supplied_at_interface"]
        and inventory["circuit_derives_Cycle342_payload_lawfulness"] is False
        and inventory["carrier_candidates_typed_as_Records"] is False
        and inventory["one_convergence_site_Record_after_threshold"]
        and inventory["prior_art_supplies_quantum_Darwinism_bridge"]
        and inventory["prior_art_says_bridge_is_bounded_input"]
        and inventory["generic_redundancy_as_Record_formation_novelty_claim"] is False
        and inventory["allowed_physical_M2_gate_compiler_claim"] is False
        and inventory["reversible_calculation_gate_kinds"] == ("X", "CNOT", "TOFFOLI")
        and set(inventory["supplied_irreversible_gate_semantics"]) == {"CONSUME"}
        and inventory["existing_framework_admission_of_CONSUME"] is None
        and inventory["nonunitary_commit_is_candidate_law_content"]
        and inventory["law_selection"] is None
        and inventory["Born_or_statistics"] is None
        and inventory["metric_time"] is None
        and inventory["threshold_justification"] is None
        and inventory["renewal"] is None
        and inventory["full_lattice_completion"] is None
        and inventory["global_code_precheck"] is False
        and inventory["state_dependent_host_gate_selection"] is False
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def semantic_guard_controls() -> dict[str, object]:
    text = " ".join(__doc__.lower().split())
    required = (
        "posits, rather than derives",
        "one or two candidates remain candidates",
        "explicit supplied law content",
        "not silently quotient-identified as records",
        "bounded prior art",
        "not a claim that the framework already admits",
        "authority is none",
        "audit is unset",
    )
    forbidden = (
        "threshold three is derived",
        "born law derived",
        "metric time derived",
        "axiom pressure",
        "impossibility theorem",
    )
    hits = tuple(item for item in forbidden if item in text)
    check(
        "the wording keeps candidate-law, carrier/Record, prior-art, time, statistics, no-go, and authority boundaries exact",
        all(item in text for item in required) and not hits,
        {"required": required, "forbidden_claim_hits": hits},
    )
    return {"forbidden_claim_hits": hits}


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("=" * 79)
    print("CYCLE 366 ROUTE 3: REDUNDANCY-THRESHOLD RECORD-FORMATION CANDIDATE")
    print("authority=none; audit=unset")
    print("threshold=3 is supplied candidate-law content, not a derivation")
    print("=" * 79)
    geometry_and_fixed_rule_controls()
    threshold_truth_and_discriminator_controls()
    reversible_calculation_and_atomic_commit_controls()
    held_size_and_covariance_controls()
    fault_and_distinct_event_controls()
    overwrite_commutation_and_overlap_controls()
    deletion_controls()
    lawful_domain_controls()
    inherited_physics_controls()
    supplied_structure_and_prior_art_controls()
    semantic_guard_controls()
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT FIXED_CONNECTED_NN_BOOLEAN_REDUNDANCY_THRESHOLD_RECORD_FORMATION_CANDIDATE_OPEN")
        return 1
    print("RESULT FIXED_CONNECTED_NN_BOOLEAN_REDUNDANCY_THRESHOLD_RECORD_FORMATION_CANDIDATE_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
