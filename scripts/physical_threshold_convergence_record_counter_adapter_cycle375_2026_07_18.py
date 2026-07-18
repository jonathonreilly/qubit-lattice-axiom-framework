#!/usr/bin/env python3
"""Cycle 375: post-CONSUME Cycle-366 Record -> Cycle-360 counter adapter.

Only post-CONSUME Cycle-366 logical Records can become counter members.  The
three threshold carriers, reversible formed transcript, fresh token, and
workspace are absent from the common state.  Member, order, and reciprocal-
link metadata are explicit supplied inputs keyed to the installed convergence
blocks; links are never reconstructed from a scan of Record predecessor data.

On the declared nonempty linear code space the exact maps and intertwiners are

    E : ThresholdLinkedState x explicit embedding x frame -> MachineState,
    D E = identity,
    count_360 G_360^N E = sum(member),
    D G_360^N E = identity,
    G_360^{-N} G_360^N E = E.

Cycle 360 is unchanged.  Cycle 366, threshold three, and its nonunitary
CONSUME are supplied and unselected; CONSUME admission is absent.  The
reversible threshold calculation does not create links or members and is not
an admitted physical commit compiler.  The output is a dimensionless member
count, not an interval, rate, clock, or time.  Autonomous link/member genesis
and a physical commit compiler remain incompleteness, not an obstruction.
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
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_THRESHOLD_CONVERGENCE_RECORD_COUNTER_ADAPTER_"
    "CYCLE375_NOTE_2026-07-18.md"
)

import physical_autonomous_record_link_counter_fixed_global_nn_route_cycle360_2026_07_18 as c360
import physical_redundancy_threshold_record_formation_candidate_cycle366_2026_07_18 as c366


Coord = c366.Coord
Word = c366.Word
LENGTHS = (3, 6)
TRAIN_SIZES = (6, 12)
HELD_SIZE = 18
SIZES = TRAIN_SIZES + (HELD_SIZE,)
METADATA_SOURCE = "Cycle-375 supplied convergence-block member/order/reciprocal-link metadata"
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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> dict[str, object]:
    if not NOTE.exists():
        check("the Cycle-375 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "only post-consume logical records count",
        "candidates, the reversible formed transcript, and the fresh bit are not members",
        "one/two/three carriers",
        "0/0/1",
        "d e = identity",
        "all 24 proper-cubic frames",
        "train sizes n=6 and n=12",
        "held-out size n=18",
        "links and order are supplied metadata",
        "never reconstructed from a record scan",
        "consume admission by existing framework law: none",
        "autonomous link/member genesis: none",
        "physical commit compiler: none",
        "dimensionless",
        "shared substrate obstruction: none established",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the post-CONSUME member code, explicit links/order, exact maps, and semantic residuals",
        not missing,
        missing,
    )
    return {"missing": missing}


def valid_coord(site: Coord) -> bool:
    return (
        isinstance(site, tuple)
        and len(site) == 3
        and all(isinstance(value, int) and not isinstance(value, bool) for value in site)
    )


@dataclass(frozen=True)
class MemberMetadata:
    site: Coord
    member: int
    source: str = METADATA_SOURCE


@dataclass(frozen=True)
class ReciprocalLink:
    predecessor: Coord
    member: Coord
    predecessor_to_member: int
    member_to_predecessor: int
    source: str = METADATA_SOURCE


@dataclass(frozen=True)
class CounterEmbedding:
    ordered_sites: tuple[Coord, ...]
    source: str = METADATA_SOURCE


@dataclass(frozen=True)
class SuppliedMetadata:
    embedding: CounterEmbedding
    members: tuple[MemberMetadata, ...]
    links: tuple[ReciprocalLink, ...]
    source: str = METADATA_SOURCE


@dataclass(frozen=True)
class ThresholdLinkedState:
    records: tuple[c366.ThresholdSiteContentRecord, ...]
    members: tuple[MemberMetadata, ...]
    links: tuple[ReciprocalLink, ...]


def supplied_metadata(layout: c366.Layout) -> SuppliedMetadata:
    """Supply block order and links from the installed layout, not Records."""

    sites = tuple(block.target_site for block in layout.blocks)
    return SuppliedMetadata(
        CounterEmbedding(sites),
        tuple(MemberMetadata(site, 1) for site in sites),
        tuple(
            ReciprocalLink(left, right, 1, 1)
            for left, right in zip(sites, sites[1:])
        ),
    )


def member_map(common: ThresholdLinkedState) -> dict[Coord, MemberMetadata]:
    return {item.site: item for item in common.members}


def link_map(common: ThresholdLinkedState) -> dict[tuple[Coord, Coord], ReciprocalLink]:
    return {(item.predecessor, item.member): item for item in common.links}


def validate_metadata(metadata: SuppliedMetadata) -> None:
    if not isinstance(metadata, SuppliedMetadata):
        raise TypeError("common-state extraction requires explicit SuppliedMetadata")
    if metadata.source != METADATA_SOURCE or metadata.embedding.source != METADATA_SOURCE:
        raise ValueError("metadata source is outside the declared supplied interface")
    sites = metadata.embedding.ordered_sites
    if (
        not isinstance(sites, tuple)
        or not sites
        or len(set(sites)) != len(sites)
        or any(not valid_coord(site) for site in sites)
        or len(metadata.members) != len(sites)
        or len(metadata.links) != len(sites) - 1
    ):
        raise ValueError("supplied order/member/link metadata has the wrong finite domain")
    for site, member in zip(sites, metadata.members):
        if member != MemberMetadata(site, 1):
            raise ValueError("supplied member metadata is not exact")
    for left, right, link in zip(sites, sites[1:], metadata.links):
        if link != ReciprocalLink(left, right, 1, 1):
            raise ValueError("supplied reciprocal-link metadata is not exact")


def validate_common_state(
    fixture: c366.c364.c342.c338.RouteFixture,
    common: ThresholdLinkedState,
    embedding: CounterEmbedding,
) -> None:
    if not isinstance(common, ThresholdLinkedState):
        raise TypeError("counter encoder requires one ThresholdLinkedState")
    if not isinstance(embedding, CounterEmbedding) or embedding.source != METADATA_SOURCE:
        raise TypeError("counter encoder requires one explicit supplied embedding")
    if not common.records or len(common.records) not in range(1, c360.COUNTER_CAPACITY + 1):
        raise ValueError("common state is outside Cycle-360's installed nonempty capacity")
    sites = tuple(record.site for record in common.records)
    if embedding.ordered_sites != sites or len(set(sites)) != len(sites):
        raise ValueError("embedding must preserve every post-CONSUME Record site exactly once")
    if len(common.members) != len(sites) or len(common.links) != len(sites) - 1:
        raise ValueError("every Record needs one member and every adjacent order pair one link")
    members = member_map(common)
    links = link_map(common)
    if set(members) != set(sites) or len(members) != len(common.members):
        raise ValueError("member metadata aliases or misses a post-CONSUME Record")
    expected_links = tuple(zip(sites, sites[1:]))
    if tuple((item.predecessor, item.member) for item in common.links) != expected_links:
        raise ValueError("explicit reciprocal links disagree with the supplied order")
    for record in common.records:
        decoded = c366.c364.c342.decode_record_word(record.content)
        if (
            not isinstance(record, c366.ThresholdSiteContentRecord)
            or not valid_coord(record.site)
            or record.predecessors != ()
            or record.record_type != c366.RECORD_TYPE
            or record.law != c366.LAW_NAME
            or not record.permanent_under_candidate_law
            or not decoded.typed
            or not decoded.permanent
            or not c366.c364.c342.cylinder_is_lawful(fixture, decoded.cylinder)
        ):
            raise ValueError("common Record is outside the Cycle-366 post-CONSUME code")
        member = members[record.site]
        if member.member != 1 or member.source != METADATA_SOURCE:
            raise ValueError("only explicit member-one metadata enters the count code")
    for link in common.links:
        if (
            link.predecessor_to_member != 1
            or link.member_to_predecessor != 1
            or link.source != METADATA_SOURCE
            or (link.predecessor, link.member) not in links
        ):
            raise ValueError("reciprocal link violates the supplied equality code")
    if not c366.c364.c342.valid_chain(
        fixture,
        tuple(c366.c364.c342.decode_record_word(record.content) for record in common.records),
    ):
        raise ValueError("post-CONSUME Record payloads are not a lawful Cycle-360 chain")


def extract_postconsume_common(
    fixture: c366.c364.c342.c338.RouteFixture,
    physical: c366.BasisState,
    metadata: SuppliedMetadata,
) -> ThresholdLinkedState:
    """Use supplied order/links; logical_records supplies membership eligibility only."""

    c366.validate_basis(physical)
    validate_metadata(metadata)
    if c366.workspace_leakage(physical) != 0:
        raise ValueError("threshold workspace must be clean at extraction")
    logical = {record.site: record for record in c366.logical_records(physical)}
    order = metadata.embedding.ordered_sites
    if set(logical) != set(order):
        raise ValueError("only and every supplied ordered site must be post-CONSUME logical")
    common = ThresholdLinkedState(
        tuple(logical[site] for site in order),
        metadata.members,
        metadata.links,
    )
    validate_common_state(fixture, common, metadata.embedding)
    return common


def encode_counter_input(
    fixture: c366.c364.c342.c338.RouteFixture,
    common: ThresholdLinkedState,
    embedding: CounterEmbedding,
    frame: np.ndarray,
) -> c360.MachineState:
    """E: exact common-state encoder into the unchanged Cycle-360 machine."""

    validate_common_state(fixture, common, embedding)
    size = len(embedding.ordered_sites)
    layout, scaffold = c360.build_layout(
        fixture, size, frame, members=(0,) * size
    )
    values = list(scaffold)
    members = member_map(common)
    links = link_map(common)
    blocks = tuple(sorted(layout.blocks, key=lambda item: item.index))
    installed = {}
    for block, record in zip(blocks, common.records):
        for target in block.record_sites:
            values[target] = 0
        for orientation in c360.ORIENTATIONS:
            values[block.member_sites[orientation]] = 0
        for target, value in zip(block.record_sites, record.content):
            values[target] = value
        for orientation in c360.ORIENTATIONS:
            values[block.member_sites[orientation]] = members[record.site].member
        installed[block.index] = replace(
            block,
            record=c366.c364.c342.decode_record_word(record.content),
            member=members[record.site].member,
        )
    for bond in layout.bonds:
        for target in bond.bus:
            values[target] = 0
        left = embedding.ordered_sites[bond.index]
        right = embedding.ordered_sites[bond.index + 1]
        supplied = links[(left, right)]
        if supplied.predecessor_to_member != supplied.member_to_predecessor:
            raise ValueError("reciprocal link equality failed")
        values[bond.bus[0]] = supplied.predecessor_to_member
    layout = replace(
        layout,
        blocks=tuple(installed[block.index] for block in layout.blocks),
    )
    encoded = c360.initial_state(layout, tuple(values))
    if c360.auxiliary_constraint_failures(encoded):
        raise RuntimeError("E left the Cycle-360 initial code space")
    return encoded


def decode_counter_metadata(
    state: c360.MachineState,
    embedding: CounterEmbedding,
) -> ThresholdLinkedState:
    """D: read static fields using only the supplied embedding."""

    c360.validate_basis_shape(state)
    blocks = tuple(sorted(state.layout.blocks, key=lambda item: item.index))
    if len(blocks) != len(embedding.ordered_sites):
        raise ValueError("decoder embedding has the wrong installed size")
    records = []
    members = []
    for block, site in zip(blocks, embedding.ordered_sites):
        content = tuple(state.bits[target] for target in block.record_sites)
        decoded = c366.c364.c342.decode_record_word(content)
        if not c366.c364.c342.cylinder_is_lawful(state.layout.fixture, decoded.cylinder):
            raise ValueError("decoded Record payload is outside the active fixture")
        records.append(c366.ThresholdSiteContentRecord(site, content, ()))
        duplicated = tuple(
            state.bits[block.member_sites[orientation]]
            for orientation in c360.ORIENTATIONS
        )
        if duplicated != (1, 1):
            raise ValueError("duplicated physical member fields left the common code")
        members.append(MemberMetadata(site, 1))
    links = []
    for bond in state.layout.bonds:
        if any(state.bits[target] for target in bond.bus[1:]):
            raise ValueError("counter bond workspace is not blank at D")
        value = state.bits[bond.bus[0]]
        if value != 1:
            raise ValueError("physical reciprocal-link master is absent")
        links.append(
            ReciprocalLink(
                embedding.ordered_sites[bond.index],
                embedding.ordered_sites[bond.index + 1],
                value,
                value,
            )
        )
    common = ThresholdLinkedState(tuple(records), tuple(members), tuple(links))
    validate_common_state(state.layout.fixture, common, embedding)
    return common


def build_physical_source(
    fixture: c366.c364.c342.c338.RouteFixture,
    size: int,
    multiplicity: int = c366.FORMATION_THRESHOLD,
) -> tuple[c366.BasisState, c366.BasisState, c366.BasisState]:
    if size not in SIZES and size != 1:
        raise ValueError("threshold fixture is outside the declared finite domain")
    layout = c366.build_layout(size)
    words = c366.record_words(fixture, size)
    assignments = tuple(
        (
            event,
            c366.redundant_from_immediate(
                c366.immediate_proposal(layout.blocks[event], words[event], multiplicity),
                multiplicity,
            ),
        )
        for event in range(size)
    )
    prepared = c366.prepare(layout, assignments)
    if not prepared.admissible:
        raise RuntimeError(("threshold fixture rejected", prepared.reasons))
    calculated = c366.apply_layers(prepared.state, prepared.state.layout.layers[:-1])
    committed = c366.apply_layers(calculated, (prepared.state.layout.layers[-1],))
    return prepared.state, calculated, committed


def transform_basis_source(
    source: c366.BasisState,
    frame: np.ndarray,
    mapping,
) -> c366.BasisState:
    sites = tuple(
        replace(site, coord=c366.c362.c353.rotated(site.coord, frame))
        for site in source.layout.sites
    )
    blocks = tuple(
        replace(
            block,
            target_site=c366.c362.c353.rotated(block.target_site, frame),
            predecessors=tuple(c366.c362.c353.rotated(site, frame) for site in block.predecessors),
        )
        for block in source.layout.blocks
    )
    bits = list(source.bits)
    for block in source.layout.blocks:
        for replica in block.replicas:
            payload = tuple(source.bits[replica[lane]] for lane in c366.PAYLOAD_LANES)
            rotated = c366.c364.rotate_payload(payload, mapping)
            for lane, value in zip(c366.PAYLOAD_LANES, rotated):
                bits[replica[lane]] = value
    return c366.BasisState(replace(source.layout, sites=sites, blocks=blocks), tuple(bits))


def transform_common(
    common: ThresholdLinkedState,
    frame: np.ndarray,
    mapping,
) -> tuple[ThresholdLinkedState, CounterEmbedding]:
    rotate = lambda site: c366.c362.c353.rotated(site, frame)
    records = tuple(
        replace(
            record,
            site=rotate(record.site),
            content=c366.c364.rotate_payload(record.content, mapping),
            predecessors=tuple(rotate(site) for site in record.predecessors),
        )
        for record in common.records
    )
    members = tuple(replace(item, site=rotate(item.site)) for item in common.members)
    links = tuple(
        replace(item, predecessor=rotate(item.predecessor), member=rotate(item.member))
        for item in common.links
    )
    embedding = CounterEmbedding(tuple(record.site for record in records))
    return ThresholdLinkedState(records, members, links), embedding


def carrier_threshold_count_discriminator_controls() -> dict[str, object]:
    fixture = c366.c364.c342.c338.build_fixture(3)
    rows = []
    failures = 0
    for multiplicity in (1, 2, 3):
        prepared, calculated, committed = build_physical_source(fixture, 1, multiplicity)
        precommit = c366.logical_records(calculated)
        postcommit = c366.logical_records(committed)
        member_count = len(postcommit)
        expected = int(multiplicity == c366.FORMATION_THRESHOLD)
        failures += int(
            len(precommit) != 0
            or len(postcommit) != expected
            or member_count != expected
            or c366.workspace_leakage(calculated) != 0
            or c366.workspace_leakage(committed) != 0
        )
        rows.append(
            {
                "precommit_carriers": multiplicity,
                "precommit_logical_Records": len(precommit),
                "post_CONSUME_logical_Records": len(postcommit),
                "dimensionless_member_count": member_count,
                "Cycle360_machine_installed": False,
            }
        )
    executable_hits = {
        "metadata": "logical_records" in getsource(supplied_metadata),
        "E_predecessor_scan": "record.predecessors" in getsource(encode_counter_input),
        "E_logical_Record_scan": "logical_records" in getsource(encode_counter_input),
    }
    detail = {
        "rows": rows,
        "discriminator": "one/two/three carriers -> dimensionless count 0/0/1",
        "discriminator_surface": "exact common-state member functional; unchanged Cycle360 campaign domain begins at N6",
        "three_carriers_are_three_members": False,
        "reversible_formed_transcript_is_member": False,
        "fresh_bit_is_member": False,
        "metadata_or_E_host_derivation_hits": executable_hits,
        "Cycle366_step_parameters": tuple(signature(c366.step).parameters),
        "E_parameters": tuple(signature(encode_counter_input).parameters),
        "CONSUME_admission_by_existing_framework_law": None,
    }
    check(
        "one/two/three carriers map to dimensionless count 0/0/1; only the post-CONSUME logical Record is a member",
        failures == 0
        and tuple(row["dimensionless_member_count"] for row in rows) == (0, 0, 1)
        and not any(executable_hits.values())
        and detail["Cycle366_step_parameters"] == ("state",)
        and detail["E_parameters"] == ("fixture", "common", "embedding", "frame")
        and detail["CONSUME_admission_by_existing_framework_law"] is None,
        detail,
    )
    return {"failures": failures + sum(executable_hits.values()), **detail}


def exact_adapter_counter_frame_controls() -> dict[str, object]:
    frames = c360.c353.proper_cubic_frames()
    cases = held_cases = 0
    threshold_failures = common_covariance_failures = 0
    roundtrip_failures = count_failures = inverse_failures = 0
    leakage_failures = static_leakage = geometry_failures = locality_failures = 0
    rows = []
    for length in LENGTHS:
        fixture = c366.c364.c342.c338.build_fixture(length)
        base = {}
        for size in SIZES:
            prepared, calculated, committed = build_physical_source(fixture, size)
            metadata = supplied_metadata(committed.layout)
            common = extract_postconsume_common(fixture, committed, metadata)
            base[size] = (prepared, common)
        for size in SIZES:
            prepared, base_common = base[size]
            base_initial = encode_counter_input(
                fixture,
                base_common,
                CounterEmbedding(tuple(record.site for record in base_common.records)),
                np.eye(3, dtype=int),
            )
            for frame in frames:
                rotated_fixture, mapping, mapping_failures = c366.c364.c342.mapped_fixture(fixture, frame)
                geometry_failures += mapping_failures
                framed_source = transform_basis_source(prepared, frame, mapping)
                calculated = c366.apply_layers(framed_source, framed_source.layout.layers[:-1])
                committed = c366.apply_layers(calculated, (framed_source.layout.layers[-1],))
                metadata = supplied_metadata(committed.layout)
                common = extract_postconsume_common(rotated_fixture, committed, metadata)
                expected_common, expected_embedding = transform_common(base_common, frame, mapping)
                common_covariance_failures += int(
                    common != expected_common or metadata.embedding != expected_embedding
                )
                initial = encode_counter_input(
                    rotated_fixture, common, metadata.embedding, frame
                )
                roundtrip_failures += int(
                    decode_counter_metadata(initial, metadata.embedding) != common
                )
                terminal, trace = c360.run_until_done(initial)
                common_count = sum(item.member for item in common.members)
                count_failures += int(
                    c360.done_count(terminal) != common_count or len(trace) != size
                )
                leakage_failures += sum(c360.auxiliary_constraint_failures(item) for item in trace)
                leakage_failures += sum(
                    c360.local_selector_guard_constraint_failures(item) for item in trace
                )
                terminal_common = decode_counter_metadata(terminal, metadata.embedding)
                static_leakage += int(terminal_common != common)
                recovered = terminal
                for _ in trace:
                    recovered = c360.inverse_step(recovered)
                inverse_failures += int(recovered.bits != initial.bits)
                inverse_failures += int(
                    decode_counter_metadata(recovered, metadata.embedding) != common
                )
                inverse_failures += int(c360.record_hash(terminal) != c360.record_hash(initial))
                threshold_failures += int(
                    c366.logical_records(calculated) != ()
                    or len(c366.logical_records(committed)) != size
                    or c366.workspace_leakage(committed) != 0
                )
                geometry_failures += sum(
                    c360.c353.rotated(base_site.coord, frame) != framed_site.coord
                    for base_site, framed_site in zip(base_initial.layout.sites, initial.layout.sites)
                )
                locality_failures += sum(
                    not c360.support_connected_nn(gate, initial.layout.sites)
                    for layer in initial.layout.layers
                    for gate in layer.gates
                )
                cases += 1
                held_cases += int(length == 6 and size == HELD_SIZE)
            rows.append(
                {
                    "L": length,
                    "N": size,
                    "train": size in TRAIN_SIZES,
                    "held": length == 6 and size == HELD_SIZE,
                    "Cycle360_M2_sites": len(base_initial.layout.sites),
                    "Cycle360_fixed_layers": len(base_initial.layout.layers),
                }
            )
    failures = (
        threshold_failures
        + common_covariance_failures
        + roundtrip_failures
        + count_failures
        + inverse_failures
        + leakage_failures
        + static_leakage
        + geometry_failures
        + locality_failures
    )
    detail = {
        "rows": rows,
        "L_by_N_by_frame_cases": cases,
        "proper_cubic_frames": len(frames),
        "held_L6_N18_frame_cases": held_cases,
        "threshold_or_commit_failures": threshold_failures,
        "common_state_covariance_failures": common_covariance_failures,
        "D_E_roundtrip_failures": roundtrip_failures,
        "count_intertwiner_failures": count_failures,
        "physical_inverse_failures": inverse_failures,
        "counter_auxiliary_or_selector_leakage": leakage_failures,
        "Record_member_link_static_leakage": static_leakage,
        "frame_geometry_or_payload_mapping_failures": geometry_failures,
        "connected_NN_failures": locality_failures,
        "intertwiners": (
            "D E = identity",
            "count_360 G_360^N E = sum(member)",
            "D G_360^N E = identity",
            "G_360^{-N} G_360^N E = E",
        ),
    }
    check(
        "the explicit post-CONSUME common state exactly intertwines with unchanged Cycle 360 at L3/L6 N6/N12/held-N18 in all 24 frames",
        cases == len(LENGTHS) * len(SIZES) * 24
        and held_cases == 24
        and failures == 0,
        detail,
    )
    return {"failures": failures, **detail}


def deletion_corruption_domain_controls() -> dict[str, object]:
    fixture = c366.c364.c342.c338.build_fixture(3)
    frame = np.eye(3, dtype=int)
    prepared, calculated, committed = build_physical_source(fixture, 12)
    metadata = supplied_metadata(committed.layout)
    common = extract_postconsume_common(fixture, committed, metadata)
    initial = encode_counter_input(fixture, common, metadata.embedding, frame)
    nominal, _trace = c360.run_until_done(initial)

    deleted_commit_layer = c366.Layer(
        calculated.layout.layers[-1].name,
        calculated.layout.layers[-1].gates[1:],
    )
    commit_deleted = c366.apply_layers(calculated, (deleted_commit_layer,))
    commit_deleted_records = c366.logical_records(commit_deleted)

    corrupted_bits = list(prepared.bits)
    corrupted_bits[prepared.layout.blocks[0].replicas[2][0]] ^= 1
    corrupted = c366.step(replace(prepared, bits=tuple(corrupted_bits)))
    corrupted_records = c366.logical_records(corrupted)

    missing_physical_link = list(initial.bits)
    missing_physical_link[initial.layout.bonds[5].bus[0]] = 0
    link_deleted_terminal, _ = c360.run_until_done(
        replace(initial, bits=tuple(missing_physical_link))
    )
    counter_deleted = c360.without_gate(
        initial,
        "count-fredkin:0-b",
        "count-fredkin:B:i0:k0:b",
    )
    counter_deleted_terminal, _ = c360.run_until_done(counter_deleted)

    bad_link_direction = replace(
        common.links[0], member_to_predecessor=0
    )
    wrong_order = CounterEmbedding(
        metadata.embedding.ordered_sites[:5]
        + (metadata.embedding.ordered_sites[6], metadata.embedding.ordered_sites[5])
        + metadata.embedding.ordered_sites[7:]
    )
    invalid_calls = (
        lambda: extract_postconsume_common(fixture, calculated, metadata),
        lambda: extract_postconsume_common(fixture, commit_deleted, metadata),
        lambda: extract_postconsume_common(fixture, corrupted, metadata),
        lambda: validate_common_state(
            fixture, replace(common, members=common.members[:-1]), metadata.embedding
        ),
        lambda: validate_common_state(
            fixture, replace(common, links=common.links[:-1]), metadata.embedding
        ),
        lambda: validate_common_state(
            fixture,
            replace(common, links=(bad_link_direction,) + common.links[1:]),
            metadata.embedding,
        ),
        lambda: encode_counter_input(fixture, common, wrong_order, frame),
        lambda: encode_counter_input(fixture, common, metadata.embedding, -frame),
        lambda: validate_metadata(replace(metadata, source="host-derived-scan")),
        lambda: decode_counter_metadata(
            replace(initial, bits=initial.bits[:-1]), metadata.embedding
        ),
    )
    rejections = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError):
            rejections += 1

    common_fields = set(ThresholdLinkedState.__dataclass_fields__)
    detail = {
        "nominal_dimensionless_count": c360.done_count(nominal),
        "single_CONSUME_gate_deletion_postconsume_Records": len(commit_deleted_records),
        "single_carrier_corruption_postconsume_Records": len(corrupted_records),
        "physical_link_deletion_count": c360.done_count(link_deleted_terminal),
        "physical_counter_gate_deletion_count": c360.done_count(counter_deleted_terminal),
        "domain_rejections": rejections,
        "domain_attempts": len(invalid_calls),
        "Record_hash_preserved": c360.record_hash(nominal) == c360.record_hash(initial),
        "common_state_fields": tuple(sorted(common_fields)),
        "candidate_or_transcript_or_fresh_fields_in_common_state": bool(
            common_fields.intersection({"replicas", "candidates", "bits", "formed", "fresh", "workspace"})
        ),
        "encoder_reads_explicit_links": "links = link_map(common)" in getsource(encode_counter_input),
        "encoder_scans_Record_predecessors": "record.predecessors" in getsource(encode_counter_input),
        "counter_step_parameters": tuple(signature(c360.step).parameters),
    }
    check(
        "commit/carrier/link/counter deletion and domain attacks are visible without Record-scan repair or common-state leakage",
        detail["nominal_dimensionless_count"] == 12
        and detail["single_CONSUME_gate_deletion_postconsume_Records"] == 11
        and detail["single_carrier_corruption_postconsume_Records"] == 11
        and detail["physical_link_deletion_count"] != 12
        and detail["physical_counter_gate_deletion_count"] != 12
        and rejections == len(invalid_calls)
        and detail["Record_hash_preserved"]
        and not detail["candidate_or_transcript_or_fresh_fields_in_common_state"]
        and detail["encoder_reads_explicit_links"]
        and not detail["encoder_scans_Record_predecessors"]
        and detail["counter_step_parameters"] == ("state",),
        detail,
    )
    return detail


def supplied_structure_and_semantic_controls() -> dict[str, object]:
    inventory = {
        "result": "bounded positive conditional Cycle-366 post-CONSUME Record to unchanged Cycle-360 counter adapter",
        "common_state": "post-CONSUME convergence Records plus supplied member/order/reciprocal-link metadata",
        "members": "one explicit member-one bit per post-CONSUME logical Record",
        "links_and_order": "explicit supplied convergence-block metadata, never inferred from Record predecessor fields",
        "source_link_geometry": "supplied abstract adjacency between convergence blocks",
        "counter_link_geometry": "Cycle-360 bounded connected-NN physical bond masters",
        "embedding": "supplied map from ordered convergence sites to Cycle-360 cells",
        "three_carriers_are_members": False,
        "reversible_formed_transcript_is_member": False,
        "fresh_bit_is_member": False,
        "Cycle366_threshold": c366.FORMATION_THRESHOLD,
        "threshold_derived": False,
        "Cycle366_selected": False,
        "CONSUME_selected": False,
        "CONSUME_admission_by_existing_framework_law": None,
        "reversible_threshold_calculation": "inherited exact fixed connected-NN Boolean basis-state calculation",
        "reversible_threshold_calculation_is_physical_commit_compiler": False,
        "autonomous_link_member_genesis": None,
        "physical_commit_compiler": None,
        "Cycle360_changed": False,
        "Cycle360_fixed_layers": 156,
        "Cycle360_capacity": c360.COUNTER_CAPACITY,
        "Cycle360_supplied_structure": (
            "bounded N-specific topology, caps, roots, selectors, guards, packet seed, unary capacity",
            "explicit proper-cubic frame and ordered-site embedding",
        ),
        "counter_output": "dimensionless post-CONSUME Record-member count",
        "count_is_interval": False,
        "count_is_rate": False,
        "count_is_time": False,
        "counter_layers_are_time": False,
        "actual_history_sampler": None,
        "Born_weights": None,
        "implementation_incompleteness": (
            "CONSUME admission/physical commit and autonomous link/member/order genesis remain open"
        ),
        "shared_substrate_obstruction": None,
        "no_go": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "all threshold, commit, metadata, embedding, counter, and semantic imports remain explicit without selecting Cycle 366",
        inventory["three_carriers_are_members"] is False
        and inventory["reversible_formed_transcript_is_member"] is False
        and inventory["fresh_bit_is_member"] is False
        and inventory["Cycle366_threshold"] == 3
        and inventory["threshold_derived"] is False
        and inventory["Cycle366_selected"] is False
        and inventory["CONSUME_selected"] is False
        and inventory["CONSUME_admission_by_existing_framework_law"] is None
        and inventory["reversible_threshold_calculation_is_physical_commit_compiler"] is False
        and inventory["autonomous_link_member_genesis"] is None
        and inventory["physical_commit_compiler"] is None
        and inventory["Cycle360_changed"] is False
        and inventory["Cycle360_fixed_layers"] == 156
        and inventory["Cycle360_capacity"] == 18
        and inventory["count_is_interval"] is False
        and inventory["count_is_rate"] is False
        and inventory["count_is_time"] is False
        and inventory["counter_layers_are_time"] is False
        and inventory["actual_history_sampler"] is None
        and inventory["Born_weights"] is None
        and inventory["shared_substrate_obstruction"] is None
        and inventory["no_go"] is inventory["axiom_pressure"] is None
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 375: POST-CONSUME THRESHOLD RECORD -> UNCHANGED CYCLE-360 COUNTER")
    print("authority=none; audit=unset; Cycle366/threshold/CONSUME unselected")
    note = note_contract()
    discriminator = carrier_threshold_count_discriminator_controls()
    frames = exact_adapter_counter_frame_controls()
    attacks = deletion_corruption_domain_controls()
    inventory = supplied_structure_and_semantic_controls()
    check(
        "Cycle 375 gives an exact bounded symmetric Record-count adapter while retaining physical commit and autonomous metadata genesis as named incompleteness",
        not note["missing"]
        and discriminator["failures"] == 0
        and frames["failures"] == 0
        and attacks["domain_rejections"] == attacks["domain_attempts"]
        and inventory["CONSUME_admission_by_existing_framework_law"] is None
        and inventory["autonomous_link_member_genesis"] is None
        and inventory["physical_commit_compiler"] is None
        and inventory["shared_substrate_obstruction"] is None,
        {
            "disposition": "bounded positive exact post-CONSUME common-state/counter adapter",
            "strongest_positive": "only post-CONSUME Cycle366 Records intertwine exactly with unchanged Cycle360 member count",
            "open_physical_residual": "CONSUME admission/commit compiler and autonomous member/link/order genesis",
            "selected_Cycle366": None,
            "shared_obstruction": None,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_THRESHOLD_CONVERGENCE_RECORD_COUNTER_ADAPTER_OPEN")
        return 1
    print("RESULT PHYSICAL_THRESHOLD_CONVERGENCE_RECORD_COUNTER_ADAPTER_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
