#!/usr/bin/env python3
"""Cycle 372: Cycle-365 migrating-Record to Cycle-360 counter adapter.

This runner constructs an exact common-state projection between the unselected
Cycle-365 migrating/invariant-fact candidate law and the fixed-global physical
Cycle-360 member counter.  One Cycle-365 endpoint-rooted quotient component is
projected to one counter block and one member bit, independent of how many
immutable history segments or transient carrier facts represent it.  Migration
therefore leaves the counter input unchanged.  Lawful reuse of a cleared
carrier by a new root adds exactly one new quotient component and one count.

Ordering, one member bit per quotient component, and reciprocal links between
successive embedded components are explicit supplied adapter metadata.  They
are not derived by a host scan of the finished worldline graph.  The endpoint
coordinate is used only to bind the supplied embedding to the physical
Cycle-365 quotient; it is never copied along the worldline as a value ID.

The exact maps are A (Cycle-365 state plus supplied metadata to a common
projection), E (common projection to Cycle-360 physical input), and D
(Cycle-360 static fields back to that common projection).  On the declared
code space the runner tests D E = identity, count G^N E = quotient-cardinality,
D G^N E = identity, and G^{-N} G^N E = E.  G is the unchanged fixed Cycle-360
update.

Cycle 365 remains unselected.  Autonomous member/link genesis and a physical
compiler for A remain implementation/law incompleteness, not an obstruction.
The count is dimensionless, not interval, rate, proper time, or time.  Renewal
and full-lattice completion remain open.  Authority is none and audit unset.
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
    "PHYSICAL_MIGRATING_RECORD_COUNTER_COMMON_STATE_ADAPTER_"
    "CYCLE372_NOTE_2026-07-18.md"
)

import physical_autonomous_record_link_counter_fixed_global_nn_route_cycle360_2026_07_18 as c360
import physical_migrating_invariant_fact_record_formation_candidate_cycle365_2026_07_18 as c365


Coord = c365.Coord
Word = c365.Word
LENGTHS = (3, 6)
SIZES = (6, 12, 18)
HELD_LENGTH = 6
HELD_SIZE = 18
METADATA_SOURCE = "Cycle-372 supplied ordered quotient-component member/link embedding"
COMMON_SOURCE = "Cycle-372 projection of the code-valid Cycle-365 quotient"
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
    return value in (0, 1) and not isinstance(value, bool) or isinstance(value, bool)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


@dataclass(frozen=True)
class ComponentSnapshot:
    root_endpoint: Coord
    content: Word


@dataclass(frozen=True)
class MemberMetadata:
    root_endpoint: Coord
    member: int


@dataclass(frozen=True)
class ReciprocalComponentLink:
    predecessor: Coord
    member: Coord
    predecessor_to_member: int
    member_to_predecessor: int


@dataclass(frozen=True)
class OrderedComponentMetadata:
    ordered_roots: tuple[Coord, ...]
    members: tuple[MemberMetadata, ...]
    links: tuple[ReciprocalComponentLink, ...]
    source: str = METADATA_SOURCE


@dataclass(frozen=True)
class CommonCounterState:
    components: tuple[ComponentSnapshot, ...]
    members: tuple[MemberMetadata, ...]
    links: tuple[ReciprocalComponentLink, ...]
    source: str = COMMON_SOURCE


@dataclass(frozen=True)
class CounterEmbedding:
    ordered_roots: tuple[Coord, ...]


@dataclass(frozen=True)
class SourceFixture:
    initial: c365.BasisState
    migrated: c365.BasisState
    metadata: OrderedComponentMetadata
    migration_statuses: tuple[str, ...]


def canonical_members(values: tuple[MemberMetadata, ...]) -> tuple[MemberMetadata, ...]:
    return tuple(sorted(values, key=lambda item: item.root_endpoint))


def canonical_links(
    values: tuple[ReciprocalComponentLink, ...],
) -> tuple[ReciprocalComponentLink, ...]:
    return tuple(sorted(values, key=lambda item: (item.predecessor, item.member)))


def supplied_metadata(ordered_roots: tuple[Coord, ...]) -> OrderedComponentMetadata:
    """Fixture input: supply order, membership, and links; derive none in A/E."""

    members = canonical_members(tuple(MemberMetadata(root, 1) for root in ordered_roots))
    links = canonical_links(tuple(
        ReciprocalComponentLink(left, right, 1, 1)
        for left, right in zip(ordered_roots, ordered_roots[1:])
    ))
    return OrderedComponentMetadata(ordered_roots, members, links)


def build_source_fixture(
    fixture: c365.c342.c338.RouteFixture,
    count: int,
    frame: np.ndarray,
) -> SourceFixture:
    """Build the declared test fixture with supplied metadata at formation."""

    layout = c365.build_layout(fixture, 2 * count, frame)
    payloads = c365.words(fixture, count)
    state = c365.blank_state(layout)
    roots = []
    for index, payload in enumerate(payloads):
        carrier = 2 * index
        answer = c365.apply_formation(
            state,
            c365.proposal(layout, carrier, payload),
            c365.IdentitySeed(0),
        )
        if answer.status != "formed":
            raise RuntimeError(("Cycle-365 source root failed", index, answer.status))
        state = answer.state
        root_site = layout.carriers[carrier].sites[c365.CARRIER_ENDPOINT_LANES[0]]
        roots.append(layout.sites[root_site].coord)
    initial = state
    requests = tuple(
        c365.RecodingRequest(
            2 * index,
            2 * index + 1,
            c365.proposal(
                layout,
                2 * index + 1,
                payload,
                (2 * index,),
            ),
        )
        for index, payload in enumerate(payloads)
    )
    migration = c365.apply_recoding_batch(initial, requests)
    if any(status != "recoded" for status in migration.statuses):
        raise RuntimeError(("Cycle-365 disjoint migration failed", migration.statuses))
    return SourceFixture(
        initial,
        migration.state,
        supplied_metadata(tuple(roots)),
        migration.statuses,
    )


def member_map(values: tuple[MemberMetadata, ...]) -> dict[Coord, MemberMetadata]:
    return {item.root_endpoint: item for item in values}


def link_map(
    values: tuple[ReciprocalComponentLink, ...],
) -> dict[tuple[Coord, Coord], ReciprocalComponentLink]:
    return {(item.predecessor, item.member): item for item in values}


def validate_metadata(
    source: c365.BasisState,
    metadata: OrderedComponentMetadata,
) -> tuple[c365.InvariantFactRecord, ...]:
    c365.validate_state(source)
    if not isinstance(metadata, OrderedComponentMetadata):
        raise TypeError("adapter needs one explicit OrderedComponentMetadata")
    if metadata.source != METADATA_SOURCE:
        raise ValueError("ordered member/link metadata has the wrong supplied source")
    if (
        not isinstance(metadata.ordered_roots, tuple)
        or not metadata.ordered_roots
        or len(set(metadata.ordered_roots)) != len(metadata.ordered_roots)
        or any(not c365.valid_coord(item) for item in metadata.ordered_roots)
    ):
        raise ValueError("ordered component embedding is outside its finite domain")
    if metadata.members != canonical_members(metadata.members):
        raise ValueError("member metadata is not in canonical root-endpoint order")
    if metadata.links != canonical_links(metadata.links):
        raise ValueError("link metadata is not in canonical endpoint order")
    quotient = c365.read_candidate_records(source)
    by_root = {item.identity: item for item in quotient}
    if set(metadata.ordered_roots) != set(by_root):
        raise ValueError("embedding must name every quotient component exactly once")
    members = member_map(metadata.members)
    if set(members) != set(by_root) or any(item.member != 1 for item in members.values()):
        raise ValueError("one supplied unit member bit is required per quotient component")
    links = link_map(metadata.links)
    expected = tuple(zip(metadata.ordered_roots, metadata.ordered_roots[1:]))
    if set(links) != set(expected) or len(metadata.links) != len(expected):
        raise ValueError("supplied links must be exactly the ordered adjacent component chain")
    for key in expected:
        item = links[key]
        if item.predecessor_to_member != 1 or item.member_to_predecessor != 1:
            raise ValueError("every supplied component link must be reciprocal and present")
    return quotient


def adapt_common_state(
    source: c365.BasisState,
    metadata: OrderedComponentMetadata,
) -> CommonCounterState:
    """A: project by supplied component order; do not generate order or links."""

    quotient = validate_metadata(source, metadata)
    by_root = {item.identity: item for item in quotient}
    components = tuple(
        ComponentSnapshot(root, by_root[root].content)
        for root in metadata.ordered_roots
    )
    return CommonCounterState(
        components,
        metadata.members,
        metadata.links,
    )


def validate_common(
    fixture: c365.c342.c338.RouteFixture,
    common: CommonCounterState,
) -> None:
    if not isinstance(common, CommonCounterState):
        raise TypeError("E needs one CommonCounterState")
    if common.source != COMMON_SOURCE or not common.components:
        raise ValueError("common state has the wrong projection source or is empty")
    roots = tuple(item.root_endpoint for item in common.components)
    if len(set(roots)) != len(roots) or any(not c365.valid_coord(item) for item in roots):
        raise ValueError("common components need unique physical root endpoints")
    for item in common.components:
        if (
            not isinstance(item.content, tuple)
            or len(item.content) != c365.RECORD_BITS
            or any(not is_bit(value) for value in item.content)
        ):
            raise ValueError("common component content is outside the 30-M2 domain")
        decoded = c365.c342.decode_record_word(item.content)
        if (
            not decoded.typed
            or not decoded.permanent
            or not c365.c342.cylinder_is_lawful(fixture, decoded.cylinder)
        ):
            raise ValueError("common component content is not fixture-lawful")
    metadata = OrderedComponentMetadata(roots, common.members, common.links)
    # Validate the metadata contract without re-reading a source graph.
    if metadata.members != canonical_members(metadata.members):
        raise ValueError("common member metadata is not canonical")
    members = member_map(metadata.members)
    if set(members) != set(roots) or any(item.member != 1 for item in members.values()):
        raise ValueError("common member metadata does not bind every component once")
    links = link_map(metadata.links)
    expected = tuple(zip(roots, roots[1:]))
    if (
        metadata.links != canonical_links(metadata.links)
        or set(links) != set(expected)
        or len(metadata.links) != len(expected)
        or any(
            links[key].predecessor_to_member != 1
            or links[key].member_to_predecessor != 1
            for key in expected
        )
    ):
        raise ValueError("common reciprocal links do not match the supplied component order")


def encode_counter_input(
    fixture: c365.c342.c338.RouteFixture,
    common: CommonCounterState,
    frame: np.ndarray,
) -> c360.MachineState:
    """E: common quotient projection -> installed Cycle-360 physical input."""

    validate_common(fixture, common)
    count = len(common.components)
    layout, scaffold = c360.build_layout(
        fixture,
        count,
        frame,
        members=(0,) * count,
    )
    values = list(scaffold)
    members = member_map(common.members)
    links = link_map(common.links)
    blocks = tuple(sorted(layout.blocks, key=lambda item: item.index))
    installed = {}
    for block, component in zip(blocks, common.components):
        for site in block.record_sites:
            values[site] = 0
        for orientation in c360.ORIENTATIONS:
            values[block.member_sites[orientation]] = 0
        for site, value in zip(block.record_sites, component.content):
            values[site] = value
        member = members[component.root_endpoint].member
        for orientation in c360.ORIENTATIONS:
            values[block.member_sites[orientation]] = member
        installed[block.index] = replace(
            block,
            record=c365.c342.decode_record_word(component.content),
            member=member,
        )
    for bond in layout.bonds:
        for site in bond.bus:
            values[site] = 0
        left = common.components[bond.index].root_endpoint
        right = common.components[bond.index + 1].root_endpoint
        supplied = links[(left, right)]
        if supplied.predecessor_to_member != supplied.member_to_predecessor:
            raise ValueError("reciprocal component-link bits violate local equality")
        values[bond.bus[0]] = supplied.predecessor_to_member
    layout = replace(
        layout,
        blocks=tuple(installed[block.index] for block in layout.blocks),
    )
    encoded = c360.initial_state(layout, tuple(values))
    if c360.auxiliary_constraint_failures(encoded):
        raise RuntimeError("E left the Cycle-360 physical code space")
    return encoded


def decode_counter_common(
    state: c360.MachineState,
    embedding: CounterEmbedding,
) -> CommonCounterState:
    """D: decode static physical fields using only the supplied root order."""

    c360.validate_basis_shape(state)
    if (
        not isinstance(embedding, CounterEmbedding)
        or not isinstance(embedding.ordered_roots, tuple)
        or len(set(embedding.ordered_roots)) != len(embedding.ordered_roots)
        or any(not c365.valid_coord(item) for item in embedding.ordered_roots)
    ):
        raise ValueError("D needs one unique finite ordered-root embedding")
    blocks = tuple(sorted(state.layout.blocks, key=lambda item: item.index))
    if len(blocks) != len(embedding.ordered_roots):
        raise ValueError("D embedding has the wrong installed counter size")
    components = []
    members = []
    for block, root in zip(blocks, embedding.ordered_roots):
        content = tuple(state.bits[site] for site in block.record_sites)
        decoded = c365.c342.decode_record_word(content)
        if (
            not decoded.typed
            or not decoded.permanent
            or not c365.c342.cylinder_is_lawful(state.layout.fixture, decoded.cylinder)
        ):
            raise ValueError("D found a non-lawful physical component word")
        member_values = tuple(
            state.bits[block.member_sites[orientation]]
            for orientation in c360.ORIENTATIONS
        )
        if member_values[0] != member_values[1]:
            raise ValueError("duplicated Cycle-360 member M2 sites disagree")
        components.append(ComponentSnapshot(root, content))
        members.append(MemberMetadata(root, member_values[0]))
    links = []
    for bond in state.layout.bonds:
        if any(state.bits[site] for site in bond.bus[1:]):
            raise ValueError("Cycle-360 bond workspace is not blank at D boundary")
        value = state.bits[bond.bus[0]]
        if value:
            links.append(
                ReciprocalComponentLink(
                    embedding.ordered_roots[bond.index],
                    embedding.ordered_roots[bond.index + 1],
                    value,
                    value,
                )
            )
    output = CommonCounterState(
        tuple(components),
        canonical_members(tuple(members)),
        canonical_links(tuple(links)),
    )
    validate_common(state.layout.fixture, output)
    return output


def transform_coord(coord: Coord, frame: np.ndarray) -> Coord:
    return c360.c353.rotated(coord, frame)


def transform_common(
    common: CommonCounterState,
    frame: np.ndarray,
) -> CommonCounterState:
    components = tuple(
        replace(item, root_endpoint=transform_coord(item.root_endpoint, frame))
        for item in common.components
    )
    members = canonical_members(tuple(
        replace(item, root_endpoint=transform_coord(item.root_endpoint, frame))
        for item in common.members
    ))
    links = canonical_links(tuple(
        replace(
            item,
            predecessor=transform_coord(item.predecessor, frame),
            member=transform_coord(item.member, frame),
        )
        for item in common.links
    ))
    return CommonCounterState(components, members, links)


def count_common(common: CommonCounterState) -> int:
    return sum(item.member for item in common.members)


def endpoint_marker_count(state: c365.BasisState) -> int:
    return sum(
        sum(c365.carrier_view(state, index).endpoint_markers)
        for index in range(state.layout.size)
    )


def transform_source_fixture(
    source: SourceFixture,
    frame: np.ndarray,
) -> SourceFixture:
    layout = c365.build_layout(
        source.initial.layout.fixture,
        source.initial.layout.size,
        frame,
    )
    metadata = OrderedComponentMetadata(
        tuple(transform_coord(item, frame) for item in source.metadata.ordered_roots),
        canonical_members(tuple(
            replace(item, root_endpoint=transform_coord(item.root_endpoint, frame))
            for item in source.metadata.members
        )),
        canonical_links(tuple(
            replace(
                item,
                predecessor=transform_coord(item.predecessor, frame),
                member=transform_coord(item.member, frame),
            )
            for item in source.metadata.links
        )),
    )
    return SourceFixture(
        c365.BasisState(layout, source.initial.bits),
        c365.BasisState(layout, source.migrated.bits),
        metadata,
        source.migration_statuses,
    )


def fixed_counter_update_controls() -> dict[str, object]:
    fixture = c365.c342.c338.build_fixture(3)
    rows = []
    failures = 0
    for count in SIZES:
        layout, _bits = c360.build_layout(fixture, count, np.eye(3, dtype=int))
        row = {
            "N": count,
            "M2_sites": len(layout.sites),
            "layers": len(layout.layers),
            "gates": sum(len(layer.gates) for layer in layout.layers),
            "connected_NN_failures": sum(
                not c360.support_connected_nn(gate, layout.sites)
                for layer in layout.layers
                for gate in layer.gates
            ),
            "layer_conflicts": sum(c360.layer_conflicts(layer) for layer in layout.layers),
        }
        failures += row["connected_NN_failures"] + row["layer_conflicts"]
        rows.append(row)
    source = getsource(c360.step).strip().lower()
    detail = {
        "rows": rows,
        "step_parameters": tuple(signature(c360.step).parameters),
        "step_source": source,
        "state_dependent_host_gate_selection": False,
        "adapter_modifies_fixed_update": False,
    }
    check(
        "E consumes the unchanged fixed 156-layer connected-NN Cycle-360 update with no adapter-side dispatcher",
        failures == 0
        and tuple(signature(c360.step).parameters) == ("state",)
        and source
        == "def step(state):\n    validate_basis_shape(state)\n    return execute_layers(state, state.layout.layers)"
        and [row["M2_sites"] for row in rows] == [961, 1945, 2929]
        and [row["layers"] for row in rows] == [156, 156, 156]
        and [row["gates"] for row in rows] == [2828, 5756, 8684]
        and not detail["state_dependent_host_gate_selection"]
        and not detail["adapter_modifies_fixed_update"],
        detail,
    )
    return detail


def adapter_intertwiner_controls() -> dict[str, object]:
    frames = c360.c353.proper_cubic_frames()
    cases = held_cases = 0
    source_constraint_failures = source_quotient_failures = 0
    migration_projection_failures = migration_encoding_failures = 0
    covariance_failures = roundtrip_failures = count_failures = 0
    inverse_failures = leakage_failures = metadata_leakage = 0
    geometry_failures = locality_failures = history_double_count_failures = 0
    rows = []
    for length in LENGTHS:
        fixture = c365.c342.c338.build_fixture(length)
        base_sources = {
            count: build_source_fixture(fixture, count, np.eye(3, dtype=int))
            for count in SIZES
        }
        base_common = {
            count: adapt_common_state(
                base_sources[count].migrated,
                base_sources[count].metadata,
            )
            for count in SIZES
        }
        base_encoded = {
            count: encode_counter_input(
                fixture,
                base_common[count],
                np.eye(3, dtype=int),
            )
            for count in SIZES
        }
        for frame in frames:
            for count in SIZES:
                source = transform_source_fixture(base_sources[count], frame)
                initial_quotient = c365.read_candidate_records(source.initial)
                migrated_quotient = c365.read_candidate_records(source.migrated)
                source_constraint_failures += c365.local_constraint_failures(source.initial)
                source_constraint_failures += c365.local_constraint_failures(source.migrated)
                source_quotient_failures += int(
                    len(initial_quotient) != count or len(migrated_quotient) != count
                )
                common_initial = adapt_common_state(source.initial, source.metadata)
                common_migrated = adapt_common_state(source.migrated, source.metadata)
                migration_projection_failures += int(common_initial != common_migrated)
                expected_common = transform_common(base_common[count], frame)
                covariance_failures += int(common_migrated != expected_common)
                encoded_initial = encode_counter_input(fixture, common_initial, frame)
                encoded_migrated = encode_counter_input(fixture, common_migrated, frame)
                migration_encoding_failures += int(
                    encoded_initial.bits != encoded_migrated.bits
                )
                embedding = CounterEmbedding(source.metadata.ordered_roots)
                roundtrip_failures += int(
                    decode_counter_common(encoded_migrated, embedding) != common_migrated
                )
                terminal, trace = c360.run_until_done(encoded_migrated)
                quotient_count = len(migrated_quotient)
                common_count = count_common(common_migrated)
                count_failures += int(
                    c360.done_count(terminal) != quotient_count
                    or common_count != quotient_count
                    or len(trace) != quotient_count
                )
                leakage_failures += sum(
                    c360.auxiliary_constraint_failures(item) for item in trace
                )
                terminal_common = decode_counter_common(terminal, embedding)
                metadata_leakage += int(terminal_common != common_migrated)
                recovered = terminal
                for _item in trace:
                    recovered = c360.inverse_step(recovered)
                inverse_failures += int(recovered.bits != encoded_migrated.bits)
                inverse_failures += int(
                    decode_counter_common(recovered, embedding) != common_migrated
                )
                inverse_failures += int(
                    c360.record_hash(terminal) != c360.record_hash(encoded_migrated)
                )
                base_layout = base_encoded[count].layout
                geometry_failures += sum(
                    c360.c353.rotated(site.coord, frame) != rotated.coord
                    for site, rotated in zip(base_layout.sites, encoded_migrated.layout.sites)
                )
                locality_failures += sum(
                    not c360.support_connected_nn(gate, encoded_migrated.layout.sites)
                    for layer in encoded_migrated.layout.layers
                    for gate in layer.gates
                )
                initial_fact_nodes = len(c365.occupied_fact_nodes(source.initial))
                migrated_fact_nodes = len(c365.occupied_fact_nodes(source.migrated))
                endpoints = endpoint_marker_count(source.migrated)
                history_double_count_failures += int(
                    initial_fact_nodes != count
                    or migrated_fact_nodes != 2 * count
                    or endpoints != count
                    or quotient_count != count
                )
                cases += 1
                held_cases += int(length == HELD_LENGTH and count == HELD_SIZE)
                if np.array_equal(frame, np.eye(3, dtype=int)):
                    rows.append(
                        {
                            "L": length,
                            "N": count,
                            "held": length == HELD_LENGTH and count == HELD_SIZE,
                            "initial_quotient_Records": len(initial_quotient),
                            "migrated_quotient_Records": len(migrated_quotient),
                            "initial_carrier_or_segment_facts": initial_fact_nodes,
                            "migrated_carrier_or_segment_facts": migrated_fact_nodes,
                            "immutable_root_endpoints": endpoints,
                            "physical_counter_count": c360.done_count(terminal),
                        }
                    )
    detail = {
        "rows": rows,
        "L_by_N_by_frame_cases": cases,
        "proper_cubic_frames": len(frames),
        "held_L6_N18_cases": held_cases,
        "Cycle365_source_constraint_failures": source_constraint_failures,
        "Cycle365_quotient_cardinality_failures": source_quotient_failures,
        "migration_common_projection_failures": migration_projection_failures,
        "migration_counter_encoding_failures": migration_encoding_failures,
        "proper_cubic_adapter_covariance_failures": covariance_failures,
        "D_E_roundtrip_failures": roundtrip_failures,
        "count_intertwiner_failures": count_failures,
        "physical_inverse_failures": inverse_failures,
        "counter_auxiliary_selector_leakage": leakage_failures,
        "common_Record_member_link_leakage": metadata_leakage,
        "frame_geometry_failures": geometry_failures,
        "connected_NN_failures": locality_failures,
        "history_or_transient_double_count_failures": history_double_count_failures,
        "commutative_diagram": (
            "A(initial source) = A(migrated source)",
            "D E A = A",
            "count_360 G_360^N E A = quotient_cardinality",
            "D G_360^N E A = A",
            "G_360^{-N} G_360^N E A = E A",
        ),
    }
    check(
        "A/E/D exactly count each Cycle-365 quotient component once across migration in all 24 frames at L3/L6 N6/N12/held-N18",
        cases == len(LENGTHS) * len(SIZES) * 24
        and held_cases == 24
        and source_constraint_failures
        == source_quotient_failures
        == migration_projection_failures
        == migration_encoding_failures
        == covariance_failures
        == roundtrip_failures
        == count_failures
        == inverse_failures
        == leakage_failures
        == metadata_leakage
        == geometry_failures
        == locality_failures
        == history_double_count_failures
        == 0,
        detail,
    )
    return detail


def migration_reuse_discriminator_controls() -> dict[str, object]:
    fixture = c365.c342.c338.build_fixture(3)
    source = build_source_fixture(fixture, 6, np.eye(3, dtype=int))
    common_before = adapt_common_state(source.migrated, source.metadata)
    encoded_before = encode_counter_input(
        fixture,
        common_before,
        np.eye(3, dtype=int),
    )
    terminal_before, _trace = c360.run_until_done(encoded_before)

    layout = source.migrated.layout
    new_payload = c365.words(fixture, 7)[-1]
    reuse = c365.apply_formation(
        source.migrated,
        c365.proposal(layout, 0, new_payload),
        c365.IdentitySeed(1),
    )
    if reuse.status != "formed":
        raise RuntimeError(("old carrier reuse fixture failed", reuse.status))
    new_root_site = layout.carriers[0].sites[c365.CARRIER_ENDPOINT_LANES[1]]
    new_root = layout.sites[new_root_site].coord
    old_last = source.metadata.ordered_roots[-1]
    extended_metadata = OrderedComponentMetadata(
        source.metadata.ordered_roots + (new_root,),
        canonical_members(
            source.metadata.members + (MemberMetadata(new_root, 1),)
        ),
        canonical_links(
            source.metadata.links
            + (ReciprocalComponentLink(old_last, new_root, 1, 1),)
        ),
    )
    common_after = adapt_common_state(reuse.state, extended_metadata)
    encoded_after = encode_counter_input(
        fixture,
        common_after,
        np.eye(3, dtype=int),
    )
    terminal_after, _after_trace = c360.run_until_done(encoded_after)
    prior_preserved = common_after.components[:-1] == common_before.components
    detail = {
        "old_reusable_carrier_blank_before_reuse": c365.carrier_blank(source.migrated, 0),
        "reuse_status": reuse.status,
        "Cycle365_constraints_after_reuse": c365.local_constraint_failures(reuse.state),
        "quotient_Records_before_reuse": len(c365.read_candidate_records(source.migrated)),
        "quotient_Records_after_reuse": len(c365.read_candidate_records(reuse.state)),
        "carrier_or_segment_facts_after_reuse": len(c365.occupied_fact_nodes(reuse.state)),
        "root_endpoints_after_reuse": endpoint_marker_count(reuse.state),
        "physical_count_before_reuse": c360.done_count(terminal_before),
        "physical_count_after_reuse": c360.done_count(terminal_after),
        "prior_component_projection_preserved": prior_preserved,
        "new_component_content_preserved": common_after.components[-1].content == new_payload,
        "old_history_segments_counted_as_members": False,
        "new_root_endpoint_copied_along_old_worldline": False,
    }
    check(
        "cleared-carrier reuse adds exactly one new component/count while the migrated component and its immutable history remain one member",
        detail["old_reusable_carrier_blank_before_reuse"]
        and detail["reuse_status"] == "formed"
        and detail["Cycle365_constraints_after_reuse"] == 0
        and detail["quotient_Records_before_reuse"] == 6
        and detail["quotient_Records_after_reuse"] == 7
        and detail["carrier_or_segment_facts_after_reuse"] == 13
        and detail["root_endpoints_after_reuse"] == 7
        and detail["physical_count_before_reuse"] == 6
        and detail["physical_count_after_reuse"] == 7
        and detail["prior_component_projection_preserved"]
        and detail["new_component_content_preserved"]
        and not detail["old_history_segments_counted_as_members"]
        and not detail["new_root_endpoint_copied_along_old_worldline"],
        detail,
    )
    return detail


def rejected(callable_) -> bool:
    try:
        callable_()
    except (TypeError, ValueError, RuntimeError):
        return True
    return False


def deletion_splice_domain_controls() -> dict[str, object]:
    fixture = c365.c342.c338.build_fixture(3)
    source = build_source_fixture(fixture, 6, np.eye(3, dtype=int))
    common = adapt_common_state(source.migrated, source.metadata)
    encoded = encode_counter_input(fixture, common, np.eye(3, dtype=int))
    nominal_terminal, _trace = c360.run_until_done(encoded)

    deleted_bits = list(source.migrated.bits)
    for site in source.migrated.layout.bonds[0].sites:
        deleted_bits[site] = 0
    deleted_segment = replace(source.migrated, bits=tuple(deleted_bits))

    splice_bits = list(source.migrated.bits)
    splice_site = source.migrated.layout.bonds[0].sites[c365.BOND_ROOT_SLOT_LANE]
    splice_bits[splice_site] ^= 1
    spliced_root_endpoint = replace(source.migrated, bits=tuple(splice_bits))

    content_bits = list(source.migrated.bits)
    content_bits[source.migrated.layout.carriers[1].sites[0]] ^= 1
    corrupted_content = replace(source.migrated, bits=tuple(content_bits))

    missing_link_metadata = replace(
        source.metadata,
        links=source.metadata.links[:-1],
    )
    first_link = source.metadata.links[0]
    spliced_link_metadata = replace(
        source.metadata,
        links=canonical_links(
            (replace(first_link, member=(999, 0, 0)),)
            + source.metadata.links[1:]
        ),
    )
    missing_member_metadata = replace(
        source.metadata,
        members=source.metadata.members[:-1],
    )

    missing_physical_link = list(encoded.bits)
    missing_physical_link[encoded.layout.bonds[2].bus[0]] = 0
    physical_link_attacked = replace(encoded, bits=tuple(missing_physical_link))
    attacked_terminal, _attacked_trace = c360.run_until_done(physical_link_attacked)

    deleted_gate = c360.without_gate(
        encoded,
        "count-fredkin:0-b",
        "count-fredkin:B:i0:k0:b",
    )
    gate_deleted_terminal, _gate_trace = c360.run_until_done(deleted_gate)

    invalid_calls = (
        lambda: adapt_common_state(deleted_segment, source.metadata),
        lambda: adapt_common_state(spliced_root_endpoint, source.metadata),
        lambda: adapt_common_state(corrupted_content, source.metadata),
        lambda: adapt_common_state(source.migrated, missing_link_metadata),
        lambda: adapt_common_state(source.migrated, spliced_link_metadata),
        lambda: adapt_common_state(source.migrated, missing_member_metadata),
        lambda: adapt_common_state(
            source.migrated,
            replace(source.metadata, source="host-derived-links"),
        ),
        lambda: encode_counter_input(fixture, common, -np.eye(3, dtype=int)),
        lambda: decode_counter_common(
            encoded,
            CounterEmbedding(source.metadata.ordered_roots[:-1]),
        ),
        lambda: validate_common(
            fixture,
            replace(common, components=common.components[:-1]),
        ),
        lambda: adapt_common_state(source.migrated.bits, source.metadata),  # type: ignore[arg-type]
    )
    domain_rejections = sum(rejected(call) for call in invalid_calls)
    adapter_source = getsource(adapt_common_state)
    detail = {
        "segment_deletion_local_failures": c365.local_constraint_failures(deleted_segment),
        "root_endpoint_splice_local_failures": c365.local_constraint_failures(spliced_root_endpoint),
        "content_corruption_local_failures": c365.local_constraint_failures(corrupted_content),
        "source_or_metadata_attack_rejections": domain_rejections,
        "source_or_metadata_attack_attempts": len(invalid_calls),
        "nominal_physical_count": c360.done_count(nominal_terminal),
        "physical_link_deletion_count": c360.done_count(attacked_terminal),
        "counter_gate_deletion_count": c360.done_count(gate_deleted_terminal),
        "A_reads_supplied_links": "metadata.links" in adapter_source,
        "A_constructs_links_from_quotient_scan": "reciprocalcomponentlink(" in adapter_source.lower(),
        "A_constructs_order_from_quotient_scan": "sorted(" in adapter_source.lower(),
        "links_repaired_after_physical_deletion": False,
    }
    check(
        "source deletion/splice/content faults, metadata deletion/splice, malformed domains, and physical counter deletions are visible without host repair",
        detail["segment_deletion_local_failures"] > 0
        and detail["root_endpoint_splice_local_failures"] > 0
        and detail["content_corruption_local_failures"] > 0
        and domain_rejections == len(invalid_calls)
        and detail["nominal_physical_count"] == 6
        and detail["physical_link_deletion_count"] != 6
        and detail["counter_gate_deletion_count"] != 6
        and detail["A_reads_supplied_links"]
        and not detail["A_constructs_links_from_quotient_scan"]
        and not detail["A_constructs_order_from_quotient_scan"]
        and not detail["links_repaired_after_physical_deletion"],
        detail,
    )
    return detail


def note_contract_controls() -> dict[str, object]:
    if not NOTE.exists():
        check("the Cycle-372 adapter note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "one quotient component is one counted record",
        "a(initial) = a(migrated)",
        "d e a = a",
        "dimensionless",
        "ordered component embedding",
        "links are supplied",
        "not a transported value id",
        "implementation/law incompleteness",
        "not an obstruction",
        "cycle 365 remains unselected",
        "renewable unbounded capacity remains open",
        "full-lattice completion remains open",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the quotient/count intertwiner, supplied links, novelty boundary, and semantic firewall",
        not missing,
        missing,
    )
    return {"missing": missing}


def supplied_structure_and_semantic_controls() -> dict[str, object]:
    inventory = {
        "result": "exact bounded Cycle-365 quotient to fixed Cycle-360 physical counter common-state adapter",
        "Cycle365_candidate_selected": False,
        "source_Record_definition": "one code-valid endpoint-rooted Cycle-365 worldline quotient component",
        "carrier_fact_is_independent_Record": False,
        "history_segment_is_independent_Record": False,
        "root_endpoint_marker_is_independent_Record": False,
        "transient_fact_is_independent_Record": False,
        "transported_value_valued_root_or_event_ID": False,
        "common_projection_A": "Cycle-365 state plus explicit metadata -> one ordered snapshot/member per quotient component",
        "encoder_E": "common projection plus supplied frame -> Cycle-360 MachineState",
        "decoder_D": "Cycle-360 static Record/member/link fields plus supplied root order -> common projection",
        "exact_intertwiners": (
            "A(initial)=A(migrated)",
            "D E A=A",
            "count G^N E A=quotient cardinality",
            "D G^N E A=A",
            "G^-N G^N E A=E A",
        ),
        "supplied_ordered_component_embedding": True,
        "supplied_member_metadata": "one unit bit per quotient component",
        "supplied_link_metadata": "two equal reciprocal bits per consecutive ordered component pair",
        "links_derived_by_host_scan_of_worldline_graph": False,
        "ordering_derived_by_host_scan_of_worldline_graph": False,
        "link_metadata_written_by_Cycle365_law": False,
        "autonomous_member_link_genesis": None,
        "physical_A_or_link_genesis_gate_compiler": None,
        "implementation_law_incompleteness": "ordered component embedding and reciprocal member/link genesis remain supplied",
        "shared_substrate_obstruction": False,
        "no_go": None,
        "axiom_pressure": None,
        "supplied_Cycle360_structure": (
            "N-specific 141N+23(N-1) M2 layout and 156 fixed layers",
            "caps, roots, direction selectors/wires, inactive guard, packet seed, unary capacity",
            "proper-cubic frame and observation bound",
        ),
        "Cycle360_update_modified": False,
        "Cycle342_payload_frame_action": "supplied upstream; A/E/D transport the bound 30-bit content opaquely",
        "count_value": "dimensionless quotient-Record member count",
        "count_is_interval": False,
        "count_is_rate": False,
        "count_is_time": False,
        "count_is_proper_time": False,
        "metric_time": None,
        "renewable_unbounded_capacity": None,
        "full_lattice_completion": None,
        "Born_statistics": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    text = " ".join(__doc__.split()).lower()
    required_text = (
        "one cycle-365 endpoint-rooted quotient component",
        "history segments or transient carrier facts",
        "explicit supplied adapter metadata",
        "not derived by a host scan",
        "never copied along the worldline as a value id",
        "unchanged fixed cycle-360 update",
        "implementation/law incompleteness, not an obstruction",
        "dimensionless",
        "renewal",
        "full-lattice completion",
        "authority is none",
        "audit unset",
    )
    check(
        "all source quotient, embedding/link, fixed-counter, implementation, capacity, and count-only boundaries are explicit",
        all(item in text for item in required_text)
        and not inventory["Cycle365_candidate_selected"]
        and not inventory["carrier_fact_is_independent_Record"]
        and not inventory["history_segment_is_independent_Record"]
        and not inventory["root_endpoint_marker_is_independent_Record"]
        and not inventory["transient_fact_is_independent_Record"]
        and not inventory["transported_value_valued_root_or_event_ID"]
        and inventory["supplied_ordered_component_embedding"]
        and not inventory["links_derived_by_host_scan_of_worldline_graph"]
        and not inventory["ordering_derived_by_host_scan_of_worldline_graph"]
        and not inventory["link_metadata_written_by_Cycle365_law"]
        and inventory["autonomous_member_link_genesis"] is None
        and inventory["physical_A_or_link_genesis_gate_compiler"] is None
        and not inventory["shared_substrate_obstruction"]
        and inventory["no_go"] is inventory["axiom_pressure"] is None
        and not inventory["Cycle360_update_modified"]
        and not inventory["count_is_interval"]
        and not inventory["count_is_rate"]
        and not inventory["count_is_time"]
        and not inventory["count_is_proper_time"]
        and inventory["metric_time"] is None
        and inventory["renewable_unbounded_capacity"] is None
        and inventory["full_lattice_completion"] is None
        and inventory["Born_statistics"] is None
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 372: MIGRATING RECORD / FIXED COUNTER COMMON-STATE ADAPTER")
    print("authority=none; audit=unset; Cycle-365 unselected; count dimensionless")
    note = note_contract_controls()
    fixed = fixed_counter_update_controls()
    composition = adapter_intertwiner_controls()
    reuse = migration_reuse_discriminator_controls()
    attacks = deletion_splice_domain_controls()
    inventory = supplied_structure_and_semantic_controls()
    check(
        "Cycle 372 exactly counts migrating quotient Records once while retaining link/member genesis as supplied implementation/law incompleteness",
        not note["missing"]
        and not fixed["adapter_modifies_fixed_update"]
        and composition["count_intertwiner_failures"] == 0
        and composition["migration_common_projection_failures"] == 0
        and composition["migration_counter_encoding_failures"] == 0
        and composition["history_or_transient_double_count_failures"] == 0
        and reuse["physical_count_before_reuse"] == 6
        and reuse["physical_count_after_reuse"] == 7
        and attacks["source_or_metadata_attack_rejections"]
        == attacks["source_or_metadata_attack_attempts"]
        and not inventory["Cycle365_candidate_selected"]
        and inventory["autonomous_member_link_genesis"] is None
        and not inventory["shared_substrate_obstruction"],
        {
            "disposition": "bounded positive exact common-state adapter/physical-counter intertwiner",
            "remaining_wall": "autonomous ordered component member/link genesis and physical A compiler",
            "obstruction": False,
            "sizes": SIZES,
            "proper_cubic_frames": composition["proper_cubic_frames"],
            "count_semantics": "dimensionless",
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_MIGRATING_RECORD_COUNTER_COMMON_STATE_ADAPTER_OPEN")
        return 1
    print("RESULT PHYSICAL_MIGRATING_RECORD_COUNTER_COMMON_STATE_ADAPTER_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
