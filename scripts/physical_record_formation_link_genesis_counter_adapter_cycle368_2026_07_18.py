#!/usr/bin/env python3
"""Cycle 368: conditional Record-formation-to-link-genesis counter adapter.

This runner composes the unselected Cycle-364 immediate site-tethered
formation hypothesis with the Cycle-360 fixed-global local-link counter.  One
atomic adapter call either leaves the common state unchanged or appends the
conditional site/content Record together with one member bit and, for a
non-root append, two equal reciprocal predecessor-link bits.  Link metadata is
therefore written with formation; it is not reconstructed by scanning a
finished Record corpus.

An explicit encoder E maps the common FormationState plus local member/link
metadata into Cycle-360 physical basis inputs.  E retains only Cycle-360's
installed topology, fixed layers, caps, roots, selectors, and packet seed from
its layout scaffold.  It clears and replaces every scaffold Record, member,
and link basis field, and replaces the inert Block record/member descriptors,
from the common state.  A decoder D recovers the same static common state on
the declared linear code space.  The tested intertwiners are

    D E = identity,
    count_360 G_360^N E = sum(local member bits),
    D G_360^N E = identity,
    G_360^{-N} G_360^N E = E.

The result is conditional on Cycle 364 and is an exact bounded adapter plus
physical-counter composition, not a physical gate compiler for formation or
link genesis itself.  Link and count are not Record formation, occurrence,
actuality, interval, rate, proper time, or time.  No obstruction or axiom
pressure is claimed.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from inspect import getsource
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_autonomous_record_link_counter_fixed_global_nn_route_cycle360_2026_07_18 as c360
import physical_site_tethered_close_gated_record_formation_candidate_cycle364_2026_07_18 as c364


Coord = c364.Coord
Word = c364.Word
LENGTHS = (3, 6)
SIZES = (6, 12, 18)
HELD_LENGTH = 6
HELD_SIZE = 18
LINK_WRITE_SOURCE = "Cycle-368 local reciprocal-link/member write interface"
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
    return value in (0, 1)


@dataclass(frozen=True)
class MemberMetadata:
    site: Coord
    member: int


@dataclass(frozen=True)
class ReciprocalLink:
    predecessor: Coord
    member: Coord
    predecessor_to_member: int
    member_to_predecessor: int


@dataclass(frozen=True)
class LinkedFormationState:
    formation: c364.FormationState
    members: tuple[MemberMetadata, ...] = ()
    links: tuple[ReciprocalLink, ...] = ()


@dataclass(frozen=True)
class LinkWriteInterface:
    target: Coord
    payload: Word
    predecessor: Coord | None
    member: int
    predecessor_to_member: int
    member_to_predecessor: int
    source: str = LINK_WRITE_SOURCE


@dataclass(frozen=True)
class AdapterAnswer:
    state: LinkedFormationState
    formed: c364.SiteContentRecord | None
    status: str
    formation_conditions: tuple[tuple[str, bool], ...]
    link_conditions: tuple[tuple[str, bool], ...]


@dataclass(frozen=True)
class CounterEmbedding:
    ordered_sites: tuple[Coord, ...]


def canonical_members(values: tuple[MemberMetadata, ...]) -> tuple[MemberMetadata, ...]:
    return tuple(sorted(values, key=lambda item: item.site))


def canonical_links(values: tuple[ReciprocalLink, ...]) -> tuple[ReciprocalLink, ...]:
    return tuple(sorted(values, key=lambda item: (item.predecessor, item.member)))


def member_map(state: LinkedFormationState) -> dict[Coord, MemberMetadata]:
    return {item.site: item for item in state.members}


def link_map(state: LinkedFormationState) -> dict[tuple[Coord, Coord], ReciprocalLink]:
    return {(item.predecessor, item.member): item for item in state.links}


def validate_linked_state(
    fixture: c364.c342.c338.RouteFixture,
    state: LinkedFormationState,
) -> None:
    if not isinstance(state, LinkedFormationState):
        raise TypeError("adapter needs one LinkedFormationState")
    c364.validate_state(fixture, state.formation)
    if not isinstance(state.members, tuple) or not isinstance(state.links, tuple):
        raise TypeError("member/link metadata must be immutable tuples")
    if state.members != canonical_members(state.members):
        raise ValueError("member metadata is not in canonical site order")
    if state.links != canonical_links(state.links):
        raise ValueError("link metadata is not in canonical endpoint order")
    if len({item.site for item in state.members}) != len(state.members):
        raise ValueError("duplicate member metadata")
    if len({(item.predecessor, item.member) for item in state.links}) != len(state.links):
        raise ValueError("duplicate reciprocal-link metadata")
    records = c364.record_map(state.formation)
    members = member_map(state)
    links = link_map(state)
    if set(members) != set(records):
        raise ValueError("every and only formed Record sites need member metadata")
    for item in state.members:
        if not c364.valid_coord(item.site) or not is_bit(item.member) or item.member != 1:
            raise ValueError("the declared counter code uses one member bit per formed Record")
    for item in state.links:
        if (
            not c364.valid_coord(item.predecessor)
            or not c364.valid_coord(item.member)
            or item.predecessor == item.member
            or c364.distance(item.predecessor, item.member) > c364.LOCAL_RADIUS
            or not is_bit(item.predecessor_to_member)
            or not is_bit(item.member_to_predecessor)
            or item.predecessor_to_member != 1
            or item.member_to_predecessor != 1
            or item.predecessor not in records
            or item.member not in records
        ):
            raise ValueError("reciprocal link is outside the bounded linked-Record code")
    for site, record in records.items():
        if len(record.predecessors) > 1:
            raise ValueError("Cycle-360 adapter declares only the linear Cycle-364 subdomain")
        incoming = tuple(key for key in links if key[1] == site)
        expected = () if not record.predecessors else ((record.predecessors[0], site),)
        if incoming != expected:
            raise ValueError("Record predecessor and simultaneous reciprocal-link metadata disagree")


def validate_link_write(item: LinkWriteInterface) -> None:
    if not isinstance(item, LinkWriteInterface):
        raise TypeError("adapter needs one explicit LinkWriteInterface")
    if (
        not c364.valid_coord(item.target)
        or not isinstance(item.payload, tuple)
        or len(item.payload) != c364.RECORD_BITS
        or any(not is_bit(bit) for bit in item.payload)
        or (item.predecessor is not None and not c364.valid_coord(item.predecessor))
        or not is_bit(item.member)
        or not is_bit(item.predecessor_to_member)
        or not is_bit(item.member_to_predecessor)
        or item.source != LINK_WRITE_SOURCE
    ):
        raise ValueError("link-write interface is outside its basis domain")


def link_condition_table(
    state: LinkedFormationState,
    proposal: c364.FormationProposal,
    write: LinkWriteInterface,
) -> tuple[tuple[str, bool], ...]:
    predecessors = proposal.readiness.predecessors
    expected_predecessor = None if not predecessors else predecessors[0]
    root_bits = write.predecessor_to_member == write.member_to_predecessor == 0
    child_bits = write.predecessor_to_member == write.member_to_predecessor == 1
    return (
        (
            "site_payload_binding",
            write.target == proposal.site and write.payload == proposal.payload,
        ),
        ("member_write", write.member == 1),
        (
            "predecessor_binding",
            len(predecessors) <= 1 and write.predecessor == expected_predecessor,
        ),
        (
            "reciprocal_link_write",
            root_bits if expected_predecessor is None else child_bits,
        ),
        (
            "predecessor_member_present",
            expected_predecessor is None or expected_predecessor in member_map(state),
        ),
    )


def apply_formation_link_genesis(
    fixture: c364.c342.c338.RouteFixture,
    state: LinkedFormationState,
    proposal: c364.FormationProposal,
    write: LinkWriteInterface,
) -> AdapterAnswer:
    """Atomic reference adapter: formation and bounded metadata commit together."""

    validate_linked_state(fixture, state)
    validate_link_write(write)
    formation = c364.apply_candidate_law(fixture, state.formation, proposal)
    link_conditions = link_condition_table(state, proposal, write)
    if formation.formed is None:
        return AdapterAnswer(
            state,
            None,
            "formation-" + formation.status,
            formation.conditions,
            link_conditions,
        )
    failed = tuple(name for name, value in link_conditions if not value)
    if failed:
        return AdapterAnswer(
            state,
            None,
            "link-blocked:" + ",".join(failed),
            formation.conditions,
            link_conditions,
        )
    members = canonical_members(state.members + (MemberMetadata(proposal.site, 1),))
    links = state.links
    if write.predecessor is not None:
        links = canonical_links(
            links
            + (
                ReciprocalLink(
                    write.predecessor,
                    proposal.site,
                    write.predecessor_to_member,
                    write.member_to_predecessor,
                ),
            )
        )
    output = LinkedFormationState(formation.state, members, links)
    validate_linked_state(fixture, output)
    return AdapterAnswer(
        output,
        formation.formed,
        "formed-with-link-metadata",
        formation.conditions,
        link_conditions,
    )


def link_write(
    item: c364.FormationProposal,
    *,
    target: Coord | None = None,
    payload: Word | None = None,
    predecessor: Coord | None | object = "default",
    member: int = 1,
    forward: int | None = None,
    reverse: int | None = None,
) -> LinkWriteInterface:
    predecessors = item.readiness.predecessors
    expected = None if not predecessors else predecessors[0]
    selected = expected if predecessor == "default" else predecessor
    linked = int(expected is not None)
    return LinkWriteInterface(
        item.site if target is None else target,
        item.payload if payload is None else payload,
        selected,  # type: ignore[arg-type]
        member,
        linked if forward is None else forward,
        linked if reverse is None else reverse,
    )


def build_linked_chain(
    fixture: c364.c342.c338.RouteFixture,
    count: int,
) -> tuple[
    LinkedFormationState,
    tuple[LinkedFormationState, ...],
    tuple[c364.FormationProposal, ...],
    tuple[LinkWriteInterface, ...],
]:
    payloads = c364.words(fixture, count)
    state = LinkedFormationState(c364.FormationState())
    states = [state]
    proposals = []
    writes = []
    for index, payload in enumerate(payloads):
        site = (index, 0, 0)
        predecessors: tuple[Coord, ...] = () if index == 0 else ((index - 1, 0, 0),)
        item = c364.proposal(site, payload, predecessors)
        write = link_write(item)
        answer = apply_formation_link_genesis(fixture, state, item, write)
        if answer.status != "formed-with-link-metadata":
            raise RuntimeError(("linked-chain fixture did not form", index, answer))
        state = answer.state
        states.append(state)
        proposals.append(item)
        writes.append(write)
    return state, tuple(states), tuple(proposals), tuple(writes)


def validate_embedding(state: LinkedFormationState, embedding: CounterEmbedding) -> None:
    if not isinstance(embedding, CounterEmbedding) or not isinstance(embedding.ordered_sites, tuple):
        raise TypeError("counter encoding needs one explicit ordered-site embedding")
    if (
        not embedding.ordered_sites
        or len(set(embedding.ordered_sites)) != len(embedding.ordered_sites)
        or any(not c364.valid_coord(site) for site in embedding.ordered_sites)
        or set(embedding.ordered_sites) != set(c364.record_map(state.formation))
    ):
        raise ValueError("counter embedding must name every formed site exactly once")
    links = link_map(state)
    for index, site in enumerate(embedding.ordered_sites):
        record = c364.record_map(state.formation)[site]
        expected = () if index == 0 else (embedding.ordered_sites[index - 1],)
        if record.predecessors != expected:
            raise ValueError("counter embedding order disagrees with local predecessor metadata")
        if index and (expected[0], site) not in links:
            raise ValueError("counter embedding consumes an explicit link; it never derives one")
    if len(state.links) != len(embedding.ordered_sites) - 1:
        raise ValueError("counter embedding needs exactly the declared adjacent links")


def encode_counter_input(
    fixture: c364.c342.c338.RouteFixture,
    state: LinkedFormationState,
    embedding: CounterEmbedding,
    frame: np.ndarray,
) -> c360.MachineState:
    """E: common linked state -> installed Cycle-360 physical basis input."""

    validate_linked_state(fixture, state)
    validate_embedding(state, embedding)
    count = len(embedding.ordered_sites)
    layout, scaffold = c360.build_layout(
        fixture,
        count,
        frame,
        members=(0,) * count,
    )
    values = list(scaffold)
    records = c364.record_map(state.formation)
    members = member_map(state)
    links = link_map(state)
    blocks = tuple(sorted(layout.blocks, key=lambda item: item.index))
    installed = {}
    for block, site in zip(blocks, embedding.ordered_sites):
        for target in block.record_sites:
            values[target] = 0
        for orientation in c360.ORIENTATIONS:
            values[block.member_sites[orientation]] = 0
        content = records[site].content
        for target, value in zip(block.record_sites, content):
            values[target] = value
        for orientation in c360.ORIENTATIONS:
            values[block.member_sites[orientation]] = members[site].member
        decoded = c364.c342.decode_record_word(content)
        installed[block.index] = replace(
            block,
            record=decoded,
            member=members[site].member,
        )
    for bond in layout.bonds:
        for target in bond.bus:
            values[target] = 0
        left = embedding.ordered_sites[bond.index]
        right = embedding.ordered_sites[bond.index + 1]
        supplied = links[(left, right)]
        if supplied.predecessor_to_member != supplied.member_to_predecessor:
            raise ValueError("reciprocal link bits violate their local equality constraint")
        values[bond.bus[0]] = supplied.predecessor_to_member
    layout = replace(
        layout,
        blocks=tuple(installed[block.index] for block in layout.blocks),
    )
    encoded = c360.initial_state(layout, tuple(values))
    if c360.auxiliary_constraint_failures(encoded):
        raise RuntimeError("encoded common state left the Cycle-360 physical code space")
    return encoded


def decode_counter_metadata(
    state: c360.MachineState,
    embedding: CounterEmbedding,
) -> LinkedFormationState:
    """D: recover the static common state using the supplied embedding only."""

    c360.validate_basis_shape(state)
    blocks = tuple(sorted(state.layout.blocks, key=lambda item: item.index))
    if len(blocks) != len(embedding.ordered_sites):
        raise ValueError("decoder embedding has the wrong installed size")
    records = []
    members = []
    for index, (block, site) in enumerate(zip(blocks, embedding.ordered_sites)):
        content = tuple(state.bits[target] for target in block.record_sites)
        decoded = c364.c342.decode_record_word(content)
        if not c364.c342.cylinder_is_lawful(state.layout.fixture, decoded.cylinder):
            raise ValueError("physical Record word is outside the active Cycle-342 fixture")
        predecessors: tuple[Coord, ...] = () if index == 0 else (embedding.ordered_sites[index - 1],)
        records.append(c364.SiteContentRecord(site, content, predecessors))
        member_values = tuple(
            state.bits[block.member_sites[orientation]] for orientation in c360.ORIENTATIONS
        )
        if member_values[0] != member_values[1]:
            raise ValueError("duplicated Cycle-360 member sites violate local equality")
        members.append(MemberMetadata(site, member_values[0]))
    links = []
    for bond in state.layout.bonds:
        if any(state.bits[target] for target in bond.bus[1:]):
            raise ValueError("counter bond workspace is not blank at the decode boundary")
        value = state.bits[bond.bus[0]]
        if value:
            links.append(
                ReciprocalLink(
                    embedding.ordered_sites[bond.index],
                    embedding.ordered_sites[bond.index + 1],
                    value,
                    value,
                )
            )
    output = LinkedFormationState(
        c364.FormationState(c364.canonical(tuple(records))),
        canonical_members(tuple(members)),
        canonical_links(tuple(links)),
    )
    validate_linked_state(state.layout.fixture, output)
    return output


def transform_linked_state(
    state: LinkedFormationState,
    frame: np.ndarray,
    mapping,
) -> LinkedFormationState:
    shift = (0, 0, 0)
    formation = c364.transform_state(state.formation, frame, shift, mapping)
    members = canonical_members(tuple(
        replace(item, site=c364.transform_coord(item.site, frame, shift))
        for item in state.members
    ))
    links = canonical_links(tuple(
        replace(
            item,
            predecessor=c364.transform_coord(item.predecessor, frame, shift),
            member=c364.transform_coord(item.member, frame, shift),
        )
        for item in state.links
    ))
    return LinkedFormationState(formation, members, links)


def transform_link_write(
    item: LinkWriteInterface,
    frame: np.ndarray,
    mapping,
) -> LinkWriteInterface:
    shift = (0, 0, 0)
    return replace(
        item,
        target=c364.transform_coord(item.target, frame, shift),
        payload=c364.rotate_payload(item.payload, mapping),
        predecessor=(
            None
            if item.predecessor is None
            else c364.transform_coord(item.predecessor, frame, shift)
        ),
    )


def formation_link_genesis_controls() -> dict[str, object]:
    rows = []
    failures = preservation_failures = 0
    for length in LENGTHS:
        fixture = c364.c342.c338.build_fixture(length)
        for count in SIZES:
            final, states, proposals, _writes = build_linked_chain(fixture, count)
            for index, (before, after) in enumerate(zip(states, states[1:])):
                expected_links = int(index > 0)
                failures += int(
                    len(after.formation.records) - len(before.formation.records) != 1
                    or len(after.members) - len(before.members) != 1
                    or len(after.links) - len(before.links) != expected_links
                )
                before_records = c364.record_map(before.formation)
                after_records = c364.record_map(after.formation)
                preservation_failures += sum(
                    after_records.get(site) != record for site, record in before_records.items()
                )
                preservation_failures += sum(item not in after.members for item in before.members)
                preservation_failures += sum(item not in after.links for item in before.links)
            failures += int(
                len(final.formation.records) != count
                or len(final.members) != count
                or len(final.links) != count - 1
                or any(len(item.readiness.predecessors) > 1 for item in proposals)
            )
            rows.append(
                {
                    "L": length,
                    "N": count,
                    "held": length == HELD_LENGTH and count == HELD_SIZE,
                    "formed_Records": len(final.formation.records),
                    "member_metadata": len(final.members),
                    "reciprocal_links": len(final.links),
                    "maximum_append_sites": 2,
                    "prior_metadata_residual": preservation_failures,
                }
            )
    check(
        "each lawful Cycle-364 append atomically creates one member and one bounded reciprocal predecessor link while preserving all prior metadata",
        failures == preservation_failures == 0,
        {
            "rows": rows,
            "atomic_delta_failures": failures,
            "prior_Record_member_link_residual": preservation_failures,
            "links_derived_after_formation": False,
        },
    )
    return {"rows": rows, "failures": failures + preservation_failures}


def adapter_counter_intertwiner_controls() -> dict[str, object]:
    frames = c360.c353.proper_cubic_frames()
    cases = held_cases = 0
    adapter_covariance_failures = encoder_roundtrip_failures = 0
    count_failures = inverse_failures = leakage_failures = 0
    record_member_link_leakage = geometry_failures = locality_failures = 0
    for length in LENGTHS:
        fixture = c364.c342.c338.build_fixture(length)
        base_by_size = {
            count: build_linked_chain(fixture, count) for count in SIZES
        }
        base_encoded = {
            count: encode_counter_input(
                fixture,
                base_by_size[count][0],
                CounterEmbedding(tuple((index, 0, 0) for index in range(count))),
                np.eye(3, dtype=int),
            )
            for count in SIZES
        }
        for frame in frames:
            rotated_fixture, mapping, mapping_failures = c364.c342.mapped_fixture(fixture, frame)
            geometry_failures += mapping_failures
            for count in SIZES:
                base_final, base_states, proposals, writes = base_by_size[count]
                prefix = base_states[-2]
                reference = apply_formation_link_genesis(
                    fixture,
                    prefix,
                    proposals[-1],
                    writes[-1],
                )
                transformed_prefix = transform_linked_state(prefix, frame, mapping)
                transformed_proposal = c364.transform_proposal(
                    proposals[-1], frame, (0, 0, 0), mapping
                )
                transformed_write = transform_link_write(writes[-1], frame, mapping)
                observed = apply_formation_link_genesis(
                    rotated_fixture,
                    transformed_prefix,
                    transformed_proposal,
                    transformed_write,
                )
                expected_final = transform_linked_state(reference.state, frame, mapping)
                adapter_covariance_failures += int(
                    observed.status != reference.status or observed.state != expected_final
                )
                order = tuple(
                    c364.transform_coord((index, 0, 0), frame, (0, 0, 0))
                    for index in range(count)
                )
                embedding = CounterEmbedding(order)
                initial = encode_counter_input(
                    rotated_fixture,
                    observed.state,
                    embedding,
                    frame,
                )
                encoder_roundtrip_failures += int(
                    decode_counter_metadata(initial, embedding) != observed.state
                )
                terminal, trace = c360.run_until_done(initial)
                common_count = sum(item.member for item in observed.state.members)
                count_failures += int(
                    c360.done_count(terminal) != common_count or len(trace) != count
                )
                leakage_failures += sum(c360.auxiliary_constraint_failures(item) for item in trace)
                leakage_failures += sum(
                    c360.local_selector_guard_constraint_failures(item) for item in trace
                )
                terminal_common = decode_counter_metadata(terminal, embedding)
                record_member_link_leakage += int(terminal_common != observed.state)
                recovered = terminal
                for _ in trace:
                    recovered = c360.inverse_step(recovered)
                inverse_failures += int(recovered.bits != initial.bits)
                inverse_failures += int(
                    decode_counter_metadata(recovered, embedding) != observed.state
                )
                inverse_failures += int(c360.record_hash(terminal) != c360.record_hash(initial))
                base_layout = base_encoded[count].layout
                geometry_failures += sum(
                    c360.c353.rotated(site.coord, frame) != framed.coord
                    for site, framed in zip(base_layout.sites, initial.layout.sites)
                )
                locality_failures += sum(
                    not c360.support_connected_nn(gate, initial.layout.sites)
                    for layer in initial.layout.layers
                    for gate in layer.gates
                )
                cases += 1
                held_cases += int(length == HELD_LENGTH and count == HELD_SIZE)
    detail = {
        "L_by_N_by_frame_cases": cases,
        "proper_cubic_frames": len(frames),
        "held_L6_N18_cases": held_cases,
        "adapter_covariance_failures": adapter_covariance_failures,
        "encoder_decoder_roundtrip_failures": encoder_roundtrip_failures,
        "count_intertwiner_failures": count_failures,
        "physical_inverse_failures": inverse_failures,
        "counter_auxiliary_or_selector_leakage": leakage_failures,
        "Record_member_link_metadata_leakage": record_member_link_leakage,
        "frame_geometry_or_payload_mapping_failures": geometry_failures,
        "connected_NN_failures": locality_failures,
        "commutative_diagram": (
            "D E = id",
            "count_360 G_360^N E = sum(member)",
            "D G_360^N E = id",
            "G_360^{-N} G_360^N E = E",
        ),
    }
    check(
        "the common formation/link state exactly encodes into and intertwines with the Cycle-360 count in all 24 frames at N6/N12/held-N18",
        cases == len(LENGTHS) * len(SIZES) * 24
        and held_cases == 24
        and adapter_covariance_failures == encoder_roundtrip_failures == 0
        and count_failures == inverse_failures == leakage_failures == 0
        and record_member_link_leakage == geometry_failures == locality_failures == 0,
        detail,
    )
    return detail


def deletion_splice_link_and_domain_controls() -> dict[str, object]:
    fixture = c364.c342.c338.build_fixture(3)
    payloads = c364.words(fixture, 4)
    empty = LinkedFormationState(c364.FormationState())
    root_proposal = c364.proposal((0, 0, 0), payloads[0])
    root_write = link_write(root_proposal)
    root = apply_formation_link_genesis(fixture, empty, root_proposal, root_write)
    child_proposal = c364.proposal((1, 0, 0), payloads[1], ((0, 0, 0),))
    child_write = link_write(child_proposal)
    nominal = apply_formation_link_genesis(
        fixture, root.state, child_proposal, child_write
    )

    missing_formation = apply_formation_link_genesis(
        fixture,
        root.state,
        replace(child_proposal, close=replace(child_proposal.close, close_candidate=0)),
        child_write,
    )
    missing_predecessor = apply_formation_link_genesis(
        fixture, empty, child_proposal, child_write
    )
    attacked = (
        (
            "site_splice",
            link_write(child_proposal, target=(2, 0, 0)),
            "site_payload_binding",
        ),
        (
            "payload_splice",
            link_write(child_proposal, payload=payloads[2]),
            "site_payload_binding",
        ),
        (
            "predecessor_splice",
            link_write(child_proposal, predecessor=(0, 1, 0)),
            "predecessor_binding",
        ),
        ("member_write_deleted", link_write(child_proposal, member=0), "member_write"),
        (
            "forward_link_deleted",
            link_write(child_proposal, forward=0),
            "reciprocal_link_write",
        ),
        (
            "reverse_link_deleted",
            link_write(child_proposal, reverse=0),
            "reciprocal_link_write",
        ),
    )
    attack_rows = []
    for name, write, condition in attacked:
        answer = apply_formation_link_genesis(
            fixture, root.state, child_proposal, write
        )
        attack_rows.append(
            {
                "attack": name,
                "formed": answer.formed is not None,
                "state_unchanged": answer.state == root.state,
                "condition_visible": dict(answer.link_conditions)[condition] is False,
            }
        )

    distinct_site = (0, 1, 0)
    equal_proposal = c364.proposal(distinct_site, payloads[0])
    equal_answer = apply_formation_link_genesis(
        fixture,
        root.state,
        equal_proposal,
        link_write(equal_proposal),
    )

    full, _states, _proposals, _writes = build_linked_chain(fixture, 12)
    embedding = CounterEmbedding(tuple((index, 0, 0) for index in range(12)))
    initial = encode_counter_input(fixture, full, embedding, np.eye(3, dtype=int))
    nominal_terminal, _ = c360.run_until_done(initial)
    missing_physical_link = list(initial.bits)
    missing_physical_link[initial.layout.bonds[5].bus[0]] = 0
    attacked_terminal, _ = c360.run_until_done(
        replace(initial, bits=tuple(missing_physical_link))
    )

    variant_records = list(full.formation.records)
    variant_index = next(
        index for index, record in enumerate(variant_records) if record.site == (1, 0, 0)
    )
    factory_word = variant_records[variant_index].content
    variant_records[variant_index] = replace(
        variant_records[variant_index],
        content=payloads[0],
    )
    variant = replace(
        full,
        formation=c364.FormationState(c364.canonical(tuple(variant_records))),
    )
    variant_initial = encode_counter_input(
        fixture, variant, embedding, np.eye(3, dtype=int)
    )
    variant_block = tuple(
        sorted(variant_initial.layout.blocks, key=lambda item: item.index)
    )[1]
    variant_physical_word = tuple(
        variant_initial.bits[target] for target in variant_block.record_sites
    )
    variant_terminal, _ = c360.run_until_done(variant_initial)

    missing_link_state = replace(full, links=full.links[:-1])
    wrong_embedding = CounterEmbedding(
        embedding.ordered_sites[:5]
        + (embedding.ordered_sites[6], embedding.ordered_sites[5])
        + embedding.ordered_sites[7:]
    )
    invalid_calls = (
        lambda: encode_counter_input(
            fixture, missing_link_state, embedding, np.eye(3, dtype=int)
        ),
        lambda: encode_counter_input(fixture, full, wrong_embedding, np.eye(3, dtype=int)),
        lambda: apply_formation_link_genesis(
            fixture,
            root.state,
            child_proposal,
            replace(child_write, source="host-derived-link"),
        ),
        lambda: apply_formation_link_genesis(
            fixture,
            root.state,
            child_proposal,
            replace(child_write, member=2),
        ),
        lambda: encode_counter_input(
            fixture, full, embedding, -np.eye(3, dtype=int)
        ),
    )
    domain_rejections = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError):
            domain_rejections += 1

    encoder_source = getsource(encode_counter_input)
    detail = {
        "nominal_child_status": nominal.status,
        "missing_formation_status": missing_formation.status,
        "missing_formation_state_unchanged": missing_formation.state == root.state,
        "missing_predecessor_status": missing_predecessor.status,
        "missing_predecessor_state_unchanged": missing_predecessor.state == empty,
        "link_write_attack_rows": attack_rows,
        "equal_content_distinct_site_Records": len(equal_answer.state.formation.records),
        "equal_content_distinct_site_members": len(equal_answer.state.members),
        "nominal_physical_count": c360.done_count(nominal_terminal),
        "physical_link_deletion_count": c360.done_count(attacked_terminal),
        "factory_word_differs_from_common_state_probe": factory_word != payloads[0],
        "encoded_Record_bits_follow_common_state": variant_physical_word == payloads[0],
        "encoded_Block_descriptor_follows_common_state": (
            c364.c342.record_word(variant_block.record) == payloads[0]
        ),
        "common_state_probe_count": c360.done_count(variant_terminal),
        "common_state_probe_is_encoder_authority_not_reachability_claim": True,
        "domain_rejections": domain_rejections,
        "domain_attempts": len(invalid_calls),
        "encoder_reads_supplied_links": "links = link_map(state)" in encoder_source,
        "encoder_derives_links_from_Record_predecessors": "record.predecessors" in encoder_source,
        "host_scan_deriving_links_after_formation": False,
    }
    check(
        "missing formation/predecessor/link writes and splices are atomic and visible; physical link deletion changes count without a host-derived repair",
        nominal.status == "formed-with-link-metadata"
        and missing_formation.formed is None
        and missing_formation.state == root.state
        and missing_predecessor.formed is None
        and missing_predecessor.state == empty
        and all(
            not row["formed"] and row["state_unchanged"] and row["condition_visible"]
            for row in attack_rows
        )
        and len(equal_answer.state.formation.records) == 2
        and len(equal_answer.state.members) == 2
        and c360.done_count(nominal_terminal) == 12
        and c360.done_count(attacked_terminal) != 12
        and detail["factory_word_differs_from_common_state_probe"]
        and detail["encoded_Record_bits_follow_common_state"]
        and detail["encoded_Block_descriptor_follows_common_state"]
        and detail["common_state_probe_count"] == 12
        and detail["common_state_probe_is_encoder_authority_not_reachability_claim"]
        and domain_rejections == len(invalid_calls)
        and detail["encoder_reads_supplied_links"]
        and not detail["encoder_derives_links_from_Record_predecessors"]
        and detail["host_scan_deriving_links_after_formation"] is False,
        detail,
    )
    return detail


def supplied_structure_and_semantic_controls() -> dict[str, object]:
    inventory = {
        "result": "exact bounded conditional formation/link metadata adapter and Cycle-360 counter intertwiner",
        "conditional_on_unselected_Cycle364": True,
        "Cycle364_law_selected": False,
        "common_state": (
            "Cycle-364 fixture-lawful FormationState",
            "one local member bit per formed site",
            "two equal reciprocal bits per predecessor/member bond",
        ),
        "simultaneous_atomic_output": (
            "one conditional site/content Record",
            "one member bit",
            "zero root links or two reciprocal child-link bits",
        ),
        "maximum_append_neighborhood_sites": 2,
        "member_duplication_constraint": "one common member bit maps to equal Cycle-360 A/B member M2 sites",
        "reciprocal_link_constraint": "two common reciprocal bits must agree and map to one bidirectional Cycle-360 bond master",
        "encoder": "E(common linked state, explicit ordered-site embedding, frame) -> Cycle-360 MachineState",
        "decoder": "D reads only the explicit embedding and static Record/member/link physical fields",
        "intertwiners": (
            "D E = identity",
            "count_360 G_360^N E = sum(member)",
            "D G_360^N E = identity",
            "G_360^{-N} G_360^N E = E",
        ),
        "links_derived_by_host_scan_after_formation": False,
        "Cycle360_layout_factory_used_for_topology": True,
        "Cycle360_factory_Record_bits_used_as_input": False,
        "Cycle360_factory_Block_Record_metadata_used_as_input": False,
        "Cycle360_factory_member_bits_used_as_input": False,
        "Cycle360_factory_link_bits_used_as_input": False,
        "supplied_Cycle360_structure": (
            "bounded N-specific physical topology and 156 fixed layers",
            "endpoint caps, roots, selector sector, packet seed, and unary capacity",
            "proper-cubic frame and explicit ordered-site embedding",
        ),
        "physical_formation_and_link_genesis_gate_compiler": None,
        "implementation_incompleteness": "the simultaneous candidate adapter is not yet compiled into autonomous physical gates",
        "shared_substrate_obstruction": False,
        "no_go": None,
        "axiom_pressure": None,
        "link_is_Record_formation": False,
        "count_is_Record_formation": False,
        "link_is_occurrence_or_actuality": False,
        "count_is_interval": False,
        "count_is_rate": False,
        "count_is_time": False,
        "actual_history_sampler": None,
        "Born_weights": None,
        "metric_time": None,
        "interval": None,
        "rate": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    text = " ".join(__doc__.split()).lower()
    required = (
        "unselected cycle-364",
        "not reconstructed by scanning",
        "not a physical gate compiler",
        "link and count are not record formation",
        "no obstruction or axiom pressure",
        "authority is none",
        "audit is unset",
    )
    check(
        "the common-state, scaffold imports, implementation wall, and count-only semantic boundary are explicit",
        all(item in text for item in required)
        and inventory["conditional_on_unselected_Cycle364"]
        and inventory["Cycle364_law_selected"] is False
        and inventory["maximum_append_neighborhood_sites"] == 2
        and inventory["links_derived_by_host_scan_after_formation"] is False
        and inventory["Cycle360_layout_factory_used_for_topology"] is True
        and inventory["Cycle360_factory_Record_bits_used_as_input"] is False
        and inventory["Cycle360_factory_Block_Record_metadata_used_as_input"] is False
        and inventory["Cycle360_factory_member_bits_used_as_input"] is False
        and inventory["Cycle360_factory_link_bits_used_as_input"] is False
        and inventory["physical_formation_and_link_genesis_gate_compiler"] is None
        and inventory["shared_substrate_obstruction"] is False
        and inventory["no_go"] is inventory["axiom_pressure"] is None
        and inventory["link_is_Record_formation"] is False
        and inventory["count_is_Record_formation"] is False
        and inventory["link_is_occurrence_or_actuality"] is False
        and inventory["count_is_interval"] is False
        and inventory["count_is_rate"] is False
        and inventory["count_is_time"] is False
        and inventory["actual_history_sampler"] is None
        and inventory["Born_weights"] is None
        and inventory["metric_time"] is inventory["interval"] is inventory["rate"] is None
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 368: CONDITIONAL FORMATION-TO-LINK-GENESIS CYCLE-360 ADAPTER")
    print("authority=none; audit=unset; conditional on unselected Cycle-364")
    genesis = formation_link_genesis_controls()
    composition = adapter_counter_intertwiner_controls()
    attacks = deletion_splice_link_and_domain_controls()
    inventory = supplied_structure_and_semantic_controls()
    check(
        "Cycle 368 closes the host-certified-chain input at the exact encoder/intertwiner level while retaining the physical genesis compiler as a named implementation wall",
        genesis["failures"] == 0
        and composition["adapter_covariance_failures"] == 0
        and composition["encoder_decoder_roundtrip_failures"] == 0
        and composition["count_intertwiner_failures"] == 0
        and composition["physical_inverse_failures"] == 0
        and attacks["host_scan_deriving_links_after_formation"] is False
        and inventory["physical_formation_and_link_genesis_gate_compiler"] is None
        and inventory["shared_substrate_obstruction"] is False,
        {
            "disposition": "bounded positive exact adapter/physical-counter composition",
            "remaining_wall": "physical autonomous gate compiler for the simultaneous formation/link-genesis update",
            "obstruction": False,
            "sizes": SIZES,
            "proper_cubic_frames": composition["proper_cubic_frames"],
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_RECORD_FORMATION_LINK_GENESIS_COUNTER_ADAPTER_OPEN")
        return 1
    print("RESULT PHYSICAL_RECORD_FORMATION_LINK_GENESIS_COUNTER_ADAPTER_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
