#!/usr/bin/env python3
"""Cycle 95: two physical AUX-gated candidate handoffs.

Cycle 93's selected-reference mismatch writes AUX.  Here AUX starts a physical
nearest-neighbour transport.  The 48 H0/H1 candidate records are encoded onto
an already-live two-content tag rail, carried around an open midpoint, decoded
back to H0/H1, and compared physically with the immutable original.  Exact
transport writes ALL and starts the next comparator; an injected unequal copy
writes one AUX and cannot start it.

Two handoffs are composed before a third comparator selects.  Every candidate
bit, status, tag, token, decision, and gate is a lattice record.  Initial
candidate/reference words, writer programs, and finite cages remain supplied.

Authority: none.  No foundation, registry, queue, audit, or git state follows.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import live_directional_program_writer_cycle90_2026_07_15 as c90
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import total_status_serial_reject_selector_cycle93_2026_07_15 as c93


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "AUX_GATED_CANDIDATE_TRANSPORT_CYCLE95_NOTE_2026-07-15.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
Program = tuple[int, ...]
Word = c90.Word
H0 = "H0"
H1 = "H1"
ALL = "ALL"
AUX = "AUX"

# All mechanism contents are already in Cycle 89's 153-role live alphabet.
TAG_FAMILIES: dict[str, tuple[str, str]] = {
    "A": ("AUXY", "AUXZ"),
    "B": ("OY", "OZ"),
    # The C rail lies directly beside the still-open decoded H rail.  Old GU/M
    # one-neighbour rows can write there before the handoff reaches it.  These
    # two already-live, formerly input-unused roles keep the open decode rail
    # genuinely quiet until its endpoint token/previous decoded bit arrives.
    "C": ("A_3_1", "A_3_2"),
    "D": ("BTG", "BTP"),
    "E": ("TY", "TZ"),
}
COPY_GUARD = "T_G1"
DEC_GUARD_Y = "T_H0"
DEC_GUARD_ZP = "T_H1"
DEC_GUARD_ZM = "T_H2"
SMALL_GUARD = "T_H3"
# Cycle 93's alternating H0/H1 status cage aliases unequal, not-yet-reached
# candidate/reference positions to an old four-neighbour H1 row.  BACKSTOP is
# already a live physical role but is absent from every Cycle 93 input
# signature.  The same marker on both transverse sides therefore gives the
# total-status recurrence its own caged local family without encoding a
# direction or a bit value in the cage.
STATUS_GUARD = "BACKSTOP"
# A naked reuse of an old travelling role inherits old one- and two-neighbour
# propagation rows and can branch into every open transverse neighbour.  The
# A_* contents below are already live roles but absent from Cycle 93's input
# alphabet.  Each cable phase gets its own content, while a finite LAUNCH_A
# shell makes it an explicit one-cell NN cable rather than an asserted edge.
TOKEN_GUARD = "LAUNCH_A"
LAUNCH_ROLES = {
    "h0": ("A_0_0", "A_0_1"),
    "h1": ("A_1_0", "A_1_2"),
}
TRANSITION_ROLES = ("A_2_0", "A_2_1")
BRIDGE_ROLE = "A_2_2"
VALIDATION_TURN = "JOINT"
ACCEPT_CARRIER = "A_3_0"

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def bit_content(bit: int) -> str:
    return H1 if bit else H0


def tag_content(bit: int, family: str) -> str:
    return TAG_FAMILIES[family][bit]


def bit_of(content: str) -> int:
    assert content in (H0, H1)
    return int(content == H1)


def put(records: dict[Coord, str], site: Coord, content: str) -> None:
    prior = records.get(site)
    if prior is not None and prior != content:
        raise ValueError(f"source collision at {site}: {prior}/{content}")
    records[site] = content


def rail_site(index: int, center: tuple[int, int]) -> Coord:
    y, z = center
    return (index, y, z)


def transform_reverse(site: Coord, layer: int) -> Coord:
    """Proper half-turn about y, then translate x by 47 and z by layer."""

    x, y, z = site
    return (47 - x, y, layer - z)


def transformed_reverse(records: dict[Coord, str], layer: int) -> dict[Coord, str]:
    return {transform_reverse(site, layer): content for site, content in records.items()}


@dataclass(frozen=True)
class Node:
    name: str
    site: Coord
    output: str
    parents: frozenset[str]
    phase: str


@dataclass(frozen=True)
class Protocol:
    source: dict[Coord, str]
    nodes: tuple[Node, ...]
    candidate_local: Signature
    reference_locals: tuple[Signature, Signature, Signature]

    @property
    def by_name(self) -> dict[str, Node]:
        return {node.name: node for node in self.nodes}


@dataclass(frozen=True)
class FrontierResult:
    ok: bool
    states: int
    max_frontier: int
    detail: str


@dataclass(frozen=True)
class FaultResult:
    ok: bool
    states: int
    injected: int
    new_aux: int
    detail: str


class Builder:
    def __init__(self) -> None:
        self.source: dict[Coord, str] = {}
        self.nodes: list[Node] = []
        self.names: set[str] = set()

    def supply(self, site: Coord, content: str) -> None:
        put(self.source, site, content)

    def node(self, name: str, site: Coord, output: str, parents: tuple[str, ...] | list[str], phase: str) -> str:
        if name in self.names:
            raise ValueError(f"duplicate node {name}")
        if site in self.source or any(prior.site == site for prior in self.nodes):
            raise ValueError(f"occupied node site {name} {site}")
        unknown = set(parents) - self.names
        if unknown:
            raise ValueError(f"unknown parents {name}: {unknown}")
        self.names.add(name)
        self.nodes.append(Node(name, site, output, frozenset(parents), phase))
        return name


PROGRAM_ITEMS = tuple(c90.ROW_PROGRAMS.items())


def selection_positions(layer: int, reverse: bool) -> dict[str, object]:
    order = tuple(range(47, -1, -1)) if reverse else tuple(range(48))
    start_x = 48 if reverse else -1
    decision_x = -1 if reverse else 48
    return {
        "order": order,
        "start": (start_x, 1, layer),
        "decision": (decision_x, 1, layer),
        "writer_first": (decision_x + (-1 if reverse else 1), 1, layer),
    }


def supply_selection_cell(
    builder: Builder,
    layer: int,
    reference: Program,
    output_word: Word,
    *,
    reverse: bool,
) -> None:
    for index, bit in enumerate(reference):
        builder.supply((index, 2, layer), bit_content(bit))
        builder.supply((index, 1, layer - 1), STATUS_GUARD)
        builder.supply((index, 1, layer + 1), STATUS_GUARD)

    positions = selection_positions(layer, reverse)
    decision = positions["decision"]  # type: ignore[assignment]
    dx, dy, dz = decision
    if layer != -2:
        builder.supply((dx, dy + 1, dz), DEC_GUARD_Y)
    if reverse:
        if layer == -4:
            builder.supply((dx, dy, dz - 1), DEC_GUARD_ZP)
        if layer != -2:
            builder.supply((dx, dy, dz + 1), DEC_GUARD_ZM)
        writer = transformed_reverse(
            c90.output_harness(output_word, port=False, shift_x=49), layer
        )
    else:
        builder.supply((dx, dy, dz + 1), DEC_GUARD_ZP)
        if layer == -4:
            builder.supply((dx, dy, dz - 1), DEC_GUARD_ZM)
        writer = {
            (x, y, z + layer): content
            for (x, y, z), content in c90.output_harness(
                output_word, port=False, shift_x=49
            ).items()
        }
    for site, content in writer.items():
        builder.supply(site, content)


def writer_additions(output_word: Word, layer: int, reverse: bool) -> tuple[tuple[Coord, str], ...]:
    additions = c90.output_additions(output_word, 49)
    if reverse:
        return tuple((transform_reverse(site, layer), content) for site, content in additions)
    return tuple(((x, y, z + layer), content) for (x, y, z), content in additions)


def supply_copy_scaffold(builder: Builder) -> None:
    # A single guide rail cages every tagged intermediate.  It is supplied;
    # the tag/data rails themselves remain open and are grown.
    for z in (0, -1, -2, -3, -4):
        for index in range(48):
            builder.supply((index, -2, z), COPY_GUARD)

    # Validation targets use the tagged detour below and the already-supplied
    # selection cage above.  Their outside turns are now grown physical
    # records, so no decision site is prefilled by a synthetic end guard.


def cumulative_status(candidate: Program, reference: Program, order: tuple[int, ...]) -> tuple[str, ...]:
    equal = True
    result = []
    for index in order:
        equal = equal and candidate[index] == reference[index]
        result.append(H1 if equal else H0)
    return tuple(result)


def add_selection(
    builder: Builder,
    prefix: str,
    layer: int,
    candidate: Program,
    reference: Program,
    *,
    reverse: bool,
    start_parent: str | None,
) -> tuple[str, str]:
    positions = selection_positions(layer, reverse)
    order: tuple[int, ...] = positions["order"]  # type: ignore[assignment]
    statuses = cumulative_status(candidate, reference, order)
    previous = start_parent
    for offset, (index, output) in enumerate(zip(order, statuses)):
        name = f"{prefix}_status_{offset:02d}"
        parents = () if previous is None else (previous,)
        previous = builder.node(name, (index, 1, layer), output, parents, f"{prefix}_compare")
    decision_output = ALL if candidate == reference else AUX
    decision = builder.node(
        f"{prefix}_decision",
        positions["decision"],  # type: ignore[arg-type]
        decision_output,
        (previous,),  # type: ignore[arg-type]
        f"{prefix}_decision",
    )
    return previous, decision  # type: ignore[return-value]


def add_launch(
    builder: Builder,
    prefix: str,
    layer: int,
    decision: str,
    *,
    reverse_selection: bool,
    second_handoff: bool,
) -> tuple[str, Coord]:
    edge_x = -1 if reverse_selection else 48
    launch_roles = LAUNCH_ROLES[prefix]
    if second_handoff:
        # The first handoff's immutable endpoint token occupies D-y.  The
        # shortest open strict-NN route around that trail has eleven steps in
        # the transverse plane and reaches the next tagged rail from y=-2.
        yz_path = (
            (2, layer), (2, layer - 1), (2, layer - 2), (2, layer - 3),
            (1, layer - 3), (0, layer - 3), (-1, layer - 3),
            (-2, layer - 3), (-2, layer - 2), (-2, layer - 1),
            (-1, layer - 1),
        )
        previous = decision
        final_site = (edge_x, yz_path[-1][0], yz_path[-1][1])
        for index, (y, z) in enumerate(yz_path):
            previous = builder.node(
                f"{prefix}_launch_{index:02d}", (edge_x, y, z), launch_roles[index % 2],
                (previous,), f"{prefix}_launch"
            )
        return previous, final_site

    # Both selected-reference mismatches leave D toward -y.  The second
    # handoff uses the explicit trail-avoiding route above.
    first = builder.node(
        f"{prefix}_launch_0", (edge_x, 0, layer), launch_roles[0],
        (decision,), f"{prefix}_launch"
    )
    second = builder.node(
        f"{prefix}_launch_1", (edge_x, -1, layer), launch_roles[1],
        (first,), f"{prefix}_launch"
    )
    return second, (edge_x, -1, layer)


def add_sweep(
    builder: Builder,
    prefix: str,
    source_center: tuple[int, int],
    target_center: tuple[int, int],
    bits: Program,
    *,
    tagged_source: bool,
    tagged_target: bool,
    target_family: str | None,
    reverse: bool,
    first_token: str | None,
) -> tuple[str, tuple[str, ...]]:
    order = tuple(range(47, -1, -1)) if reverse else tuple(range(48))
    previous = first_token
    names = []
    for offset, index in enumerate(order):
        name = f"{prefix}_{offset:02d}"
        output = (
            tag_content(bits[index], target_family)  # type: ignore[arg-type]
            if tagged_target else bit_content(bits[index])
        )
        parents = () if previous is None else (previous,)
        previous = builder.node(
            name, rail_site(index, target_center), output, parents, prefix
        )
        names.append(previous)
    return previous, tuple(names)  # type: ignore[return-value]


def add_transition(
    builder: Builder,
    prefix: str,
    source_center: tuple[int, int],
    target_center: tuple[int, int],
    completed: str,
    *,
    completed_at: int,
) -> str:
    turn_content, endpoint_content = TRANSITION_ROLES
    outside_x = -1 if completed_at == 0 else 48
    guard_x = outside_x - 1 if outside_x < 0 else outside_x + 1
    for guard_site in (
        rail_site(guard_x, source_center),
        rail_site(guard_x, target_center),
    ):
        if guard_site not in builder.source and all(node.site != guard_site for node in builder.nodes):
            builder.supply(guard_site, SMALL_GUARD)
    turn = builder.node(
        f"{prefix}_turn", rail_site(outside_x, source_center), turn_content,
        (completed,), prefix
    )
    return builder.node(
        f"{prefix}_token", rail_site(outside_x, target_center), endpoint_content,
        (turn,), prefix
    )


def add_validation(
    builder: Builder,
    prefix: str,
    original_center: tuple[int, int],
    copied_center: tuple[int, int],
    tag_center: tuple[int, int],
    candidate: Program,
    final_sweep_names: tuple[str, ...],
    final_done: str,
    *,
    layer_mid: int,
    reverse: bool,
    remote_next: bool,
) -> tuple[str, str]:
    start_x = 48 if reverse else -1
    decision_x = -1 if reverse else 48
    order = tuple(range(47, -1, -1)) if reverse else tuple(range(48))
    copied_layer = copied_center[1]
    turn = builder.node(
        f"{prefix}_validation_turn", (start_x, 0, copied_layer),
        VALIDATION_TURN, (final_done,), f"{prefix}_validate_turn"
    )
    start = builder.node(
        f"{prefix}_validation_start", (start_x, 0, layer_mid), H1,
        (turn,), f"{prefix}_validate"
    )
    previous = start
    status_names = []
    for offset, index in enumerate(order):
        name = f"{prefix}_validation_{index:02d}"
        parents = (previous, final_sweep_names[index])
        previous = builder.node(
            name, (index, 0, layer_mid), H1, parents,
            f"{prefix}_validate"
        )
        status_names.append(previous)
    decision = builder.node(
        f"{prefix}_validation_decision", (decision_x, 0, layer_mid), ALL,
        (previous,), f"{prefix}_validate_decision"
    )
    bridge = builder.node(
        f"{prefix}_accept_bridge", (decision_x, 1, layer_mid), BRIDGE_ROLE,
        (decision,), f"{prefix}_accept"
    )

    if remote_next:
        # Cell 0 validates right-to-left, while cell 1 must start at the far
        # right.  Carry acceptance across the open midpoint between the two
        # supplied reference rails.  Every step is a physical NN record.
        previous = builder.node(
            f"{prefix}_accept_up", (decision_x, 2, layer_mid),
            ACCEPT_CARRIER, (bridge,), f"{prefix}_accept_carry"
        )
        for index in range(48):
            previous = builder.node(
                f"{prefix}_accept_{index:02d}", (index, 2, layer_mid),
                ACCEPT_CARRIER, (previous,), f"{prefix}_accept_carry"
            )
        previous = builder.node(
            f"{prefix}_accept_turn", (48, 2, layer_mid),
            ACCEPT_CARRIER, (previous,), f"{prefix}_accept_carry"
        )
        previous = builder.node(
            f"{prefix}_accept_down", (48, 1, layer_mid),
            ACCEPT_CARRIER, (previous,), f"{prefix}_accept_carry"
        )
        next_site = (48, 1, copied_layer)
        next_parent = previous
    else:
        next_site = (decision_x, 1, copied_layer)
        next_parent = bridge

    next_start = builder.node(
        f"{prefix}_next_start", next_site, H1,
        (next_parent,), f"{prefix}_accept"
    )
    return decision, next_start


def cage_token_nodes(builder: Builder) -> None:
    """Occupy every unused neighbour of every grown cable/bridge site.

    Node neighbours are left open because they are the intended predecessor,
    successor, or data target.  Existing supplied records are likewise kept.
    Every other transverse opening is physically closed by the same live
    marker.  This is finite supplied apparatus, not a graph-side inhibition.
    """

    node_sites = {node.site for node in builder.nodes}
    token_contents = (
        {content for pair in LAUNCH_ROLES.values() for content in pair}
        | set(TRANSITION_ROLES)
        | {BRIDGE_ROLE, VALIDATION_TURN, ACCEPT_CARRIER}
    )
    token_sites = {node.site for node in builder.nodes if node.output in token_contents}
    for token_site in token_sites:
        for direction in c53.DIRECTIONS:
            neighbour = add(token_site, direction)
            if neighbour in node_sites or neighbour in builder.source:
                continue
            builder.supply(neighbour, TOKEN_GUARD)


def build_protocol(candidate_index: int) -> Protocol:
    candidate_local, candidate = PROGRAM_ITEMS[candidate_index]
    reference_items = (
        PROGRAM_ITEMS[(candidate_index + 1) % len(PROGRAM_ITEMS)],
        PROGRAM_ITEMS[(candidate_index + 2) % len(PROGRAM_ITEMS)],
        PROGRAM_ITEMS[candidate_index],
    )
    builder = Builder()
    for index, bit in enumerate(candidate):
        builder.supply((index, 0, 0), bit_content(bit))
    builder.supply((-1, 1, 0), H1)

    for cell_index, (local, reference) in enumerate(reference_items):
        output = c90.c89.LIVE_TABLE[local]
        output_word = c90.c89.ROLE_TO_WORD[output]
        supply_selection_cell(
            builder, -2 * cell_index, reference, output_word,
            reverse=cell_index == 1,
        )
    supply_copy_scaffold(builder)

    _last, decision0 = add_selection(
        builder, "c0", 0, candidate, reference_items[0][1],
        reverse=False, start_parent=None,
    )
    launch0, _ = add_launch(
        builder, "h0", 0, decision0,
        reverse_selection=False, second_handoff=False,
    )
    side0_done, _ = add_sweep(
        builder, "h0_side0", (0, 0), (-1, 0), candidate,
        tagged_source=False, tagged_target=True, reverse=True,
        target_family="A", first_token=launch0,
    )
    token = add_transition(
        builder, "h0_to_mid", (-1, 0), (-1, -1), side0_done,
        completed_at=0,
    )
    mid0_done, _ = add_sweep(
        builder, "h0_mid", (-1, 0), (-1, -1), candidate,
        tagged_source=True, tagged_target=True, reverse=False,
        target_family="B", first_token=token,
    )
    token = add_transition(
        builder, "h0_to_side1", (-1, -1), (-1, -2), mid0_done,
        completed_at=47,
    )
    side1_done, _ = add_sweep(
        builder, "h0_side1", (-1, -1), (-1, -2), candidate,
        tagged_source=True, tagged_target=True, reverse=True,
        target_family="C", first_token=token,
    )
    token = add_transition(
        builder, "h0_to_c1", (-1, -2), (0, -2), side1_done,
        completed_at=0,
    )
    c1_done, c1_names = add_sweep(
        builder, "h0_c1", (-1, -2), (0, -2), candidate,
        tagged_source=True, tagged_target=False, reverse=False,
        target_family=None, first_token=token,
    )
    _v0, start1 = add_validation(
        builder, "h0", (0, 0), (0, -2), (-1, -1), candidate,
        c1_names, c1_done, layer_mid=-1, reverse=True, remote_next=True,
    )

    _last, decision1 = add_selection(
        builder, "c1", -2, candidate, reference_items[1][1],
        reverse=True, start_parent=start1,
    )
    launch1, _ = add_launch(
        builder, "h1", -2, decision1,
        reverse_selection=True, second_handoff=True,
    )
    mid1_done, _ = add_sweep(
        builder, "h1_mid", (-1, -2), (-1, -3), candidate,
        tagged_source=True, tagged_target=True, reverse=False,
        target_family="D", first_token=launch1,
    )
    token = add_transition(
        builder, "h1_to_side2", (-1, -3), (-1, -4), mid1_done,
        completed_at=47,
    )
    side2_done, _ = add_sweep(
        builder, "h1_side2", (-1, -3), (-1, -4), candidate,
        tagged_source=True, tagged_target=True, reverse=True,
        target_family="E", first_token=token,
    )
    token = add_transition(
        builder, "h1_to_c2", (-1, -4), (0, -4), side2_done,
        completed_at=0,
    )
    c2_done, c2_names = add_sweep(
        builder, "h1_c2", (-1, -4), (0, -4), candidate,
        tagged_source=True, tagged_target=False, reverse=False,
        target_family=None, first_token=token,
    )
    _v1, start2 = add_validation(
        builder, "h1", (0, -2), (0, -4), (-1, -3), candidate,
        c2_names, c2_done, layer_mid=-3, reverse=True, remote_next=False,
    )

    _last, decision2 = add_selection(
        builder, "c2", -4, candidate, reference_items[2][1],
        reverse=False, start_parent=start2,
    )
    final_local = reference_items[2][0]
    final_output = c90.c89.LIVE_TABLE[final_local]
    output_word = c90.c89.ROLE_TO_WORD[final_output]
    previous = decision2
    for step, (site, output) in enumerate(writer_additions(output_word, -4, False)):
        previous = builder.node(
            f"c2_writer_{step:02d}", site, output, (previous,), "c2_writer"
        )

    cage_token_nodes(builder)

    return Protocol(
        dict(builder.source), tuple(builder.nodes), candidate_local,
        tuple(local for local, _program in reference_items),
    )


def topological_records(protocol: Protocol) -> tuple[dict[Coord, str], tuple[Node, ...]]:
    records = dict(protocol.source)
    ordered: list[Node] = []
    completed: set[str] = set()
    remaining = list(protocol.nodes)
    while remaining:
        progress = False
        for index, node in enumerate(remaining):
            if node.parents <= completed:
                put(records, node.site, node.output)
                ordered.append(node)
                completed.add(node.name)
                remaining.pop(index)
                progress = True
                break
        if not progress:
            raise RuntimeError("protocol graph contains a cycle")
    return records, tuple(ordered)


def raw_signature(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.local_signature(records, target)


def add_compiled_row(table: dict[Signature, str], local: Signature, output: str) -> None:
    canonical = c53.canonical_signature(local)
    prior = table.get(canonical)
    if prior is not None and prior != output:
        raise ValueError(f"compiled canonical conflict {prior}/{output}: {canonical}")
    table[canonical] = output


def add_row_unless_base(
    table: dict[Signature, str], records: dict[Coord, str], site: Coord,
    output: str,
) -> None:
    local = raw_signature(records, site)
    base = c93.COMBINED_RAW.get(local)
    if base is None or base != frozenset((output,)):
        add_compiled_row(table, local, output)


def compile_fault_validation_case(
    table: dict[Signature, str], prefix: str, faults: frozenset[int],
) -> None:
    """Compile only the detector response to an externally corrupted copy.

    The wrong H record is deliberately injected at an otherwise correctly
    enabled decode site; no row is learned for making the wrong record.  All
    subsequently learned rows are ordinary physical turn/status/AUX records.
    """

    protocol = build_protocol(0)
    records = dict(protocol.source)
    copy_phase = "h0_c1" if prefix == "h0" else "h1_c2"
    original_z = 0 if prefix == "h0" else -2
    copied_z = -2 if prefix == "h0" else -4
    equal = True

    for node in protocol.nodes:
        output = node.output
        if node.phase == copy_phase and node.site[0] in faults:
            output = H0 if node.output == H1 else H1

        is_status = (
            node.phase == f"{prefix}_validate"
            and node.name != f"{prefix}_validation_start"
        )
        is_detector = (
            node.phase == f"{prefix}_validate_turn"
            or node.name == f"{prefix}_validation_start"
            or is_status
            or node.name == f"{prefix}_validation_decision"
        )
        if is_status:
            index = node.site[0]
            equal = equal and (
                records[(index, 0, original_z)]
                == records[(index, 0, copied_z)]
            )
            output = H1 if equal else H0
        elif node.name == f"{prefix}_validation_decision":
            output = ALL if equal else AUX

        if is_detector:
            add_row_unless_base(table, records, node.site, output)
        put(records, node.site, output)
        if node.name == f"{prefix}_validation_decision":
            break


def compile_protocols() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    for candidate_index in range(len(PROGRAM_ITEMS)):
        protocol = build_protocol(candidate_index)
        records = dict(protocol.source)
        completed: set[str] = set()
        remaining = list(protocol.nodes)
        while remaining:
            node = next(item for item in remaining if item.parents <= completed)
            local = raw_signature(records, node.site)
            base = c93.COMBINED_RAW.get(local)
            if base is None or base != frozenset((node.output,)):
                add_compiled_row(table, local, node.output)
            put(records, node.site, node.output)
            completed.add(node.name)
            remaining.remove(node)

    # Every bit position is attacked once, plus the all-bits-corrupt mixed
    # case.  These add the absorbing-H0 and terminal-AUX detector rows; they do
    # not add a mechanism capable of producing a corrupted transported bit.
    fault_masks = tuple(frozenset((index,)) for index in range(48)) + (
        frozenset(range(48)),
    )
    for prefix in ("h0", "h1"):
        for faults in fault_masks:
            compile_fault_validation_case(table, prefix, faults)
    return table


NEW_TABLE = compile_protocols()
NEW_RAW = c59.raw_rule_outputs(NEW_TABLE)


def merge_raw() -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in (c93.COMBINED_RAW, NEW_RAW):
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


COMBINED_RAW = merge_raw()


def assignments(records: dict[Coord, str]) -> dict[Coord, str]:
    result: dict[Coord, str] = {}
    for target in c53.open_candidates(records):
        local = raw_signature(records, target)
        if local not in COMBINED_RAW:
            continue
        values = COMBINED_RAW[local]
        result[target] = next(iter(values)) if len(values) == 1 else "CONFLICT"
    return result


def enabled_nodes(protocol: Protocol, completed: frozenset[str]) -> dict[Coord, str]:
    return {
        node.site: node.output
        for node in protocol.nodes
        if node.name not in completed and node.parents <= completed
    }


def assignment_value(records: dict[Coord, str], target: Coord) -> str | None:
    if target in records:
        return None
    values = COMBINED_RAW.get(raw_signature(records, target))
    if values is None:
        return None
    return next(iter(values)) if len(values) == 1 else "CONFLICT"


def update_local_frontier(
    actual: dict[Coord, str], records: dict[Coord, str], written: Coord,
) -> None:
    """Exact incremental update: one NN write changes only six open sites."""

    actual.pop(written, None)
    for direction in c53.DIRECTIONS:
        target = add(written, direction)
        value = assignment_value(records, target)
        if value is None:
            actual.pop(target, None)
        else:
            actual[target] = value


def verify_protocol_frontiers(protocol: Protocol) -> FrontierResult:
    records = dict(protocol.source)
    actual = assignments(records)
    maximum = len(actual)
    for step, node in enumerate(protocol.nodes):
        expected = {node.site: node.output}
        if actual != expected:
            extras = sorted(set(actual) - set(expected))[:4]
            missing = sorted(set(expected) - set(actual))[:4]
            return FrontierResult(
                False, step + 1, maximum,
                f"{node.name}: extras={extras} missing={missing} "
                f"actual={actual.get(node.site)} expected={node.output}",
            )
        put(records, node.site, node.output)
        update_local_frontier(actual, records, node.site)
        maximum = max(maximum, len(actual))
    if actual:
        return FrontierResult(False, len(protocol.nodes) + 1, maximum, f"terminal={actual}")
    return FrontierResult(True, len(protocol.nodes) + 1, maximum, "")


def verify_fault_case(
    protocol: Protocol, prefix: str, faults: frozenset[int],
) -> FaultResult:
    """Inject wrong decoded H records, then demand detector AUX and silence."""

    records = dict(protocol.source)
    actual = assignments(records)
    copy_phase = "h0_c1" if prefix == "h0" else "h1_c2"
    original_z = 0 if prefix == "h0" else -2
    copied_z = -2 if prefix == "h0" else -4
    equal = True
    injected = 0
    after_injection_aux = 0

    for step, node in enumerate(protocol.nodes):
        output = node.output
        inject = node.phase == copy_phase and node.site[0] in faults
        is_status = (
            node.phase == f"{prefix}_validate"
            and node.name != f"{prefix}_validation_start"
        )
        if is_status:
            index = node.site[0]
            equal = equal and (
                records[(index, 0, original_z)]
                == records[(index, 0, copied_z)]
            )
            output = H1 if equal else H0
        elif node.name == f"{prefix}_validation_decision":
            output = ALL if equal else AUX

        # The perturbed site must first be the unique correctly enabled law
        # output.  Only then is the opposite record externally injected.
        law_output = node.output if inject else output
        expected = {node.site: law_output}
        if actual != expected:
            return FaultResult(
                False, step + 1, injected, after_injection_aux,
                f"{node.name}: actual={actual} expected={expected}",
            )
        if inject:
            output = H0 if node.output == H1 else H1
            injected += 1
        if injected and output == AUX:
            after_injection_aux += 1
        put(records, node.site, output)
        update_local_frontier(actual, records, node.site)

        if node.name == f"{prefix}_validation_decision":
            ok = (
                not equal and not actual and injected == len(faults)
                and after_injection_aux == 1
            )
            detail = "" if ok else (
                f"equal={equal} terminal={actual} injected={injected}/{len(faults)} aux={after_injection_aux}"
            )
            return FaultResult(ok, step + 2, injected, after_injection_aux, detail)
    return FaultResult(False, len(protocol.nodes), injected, after_injection_aux, "decision not reached")


def rotate_protocol(protocol: Protocol, rotation: c53.Rotation) -> Protocol:
    return Protocol(
        {c53.matvec(rotation, site): content for site, content in protocol.source.items()},
        tuple(
            Node(
                node.name, c53.matvec(rotation, node.site), node.output,
                node.parents, node.phase,
            )
            for node in protocol.nodes
        ),
        protocol.candidate_local,
        protocol.reference_locals,
    )


def physical_transport_ok(protocol: Protocol) -> bool:
    """Every carried bit is read from a physically adjacent prior rail."""

    specifications = {
        "h0_side0": ((0, 0), (-1, 0), None, "A"),
        "h0_mid": ((-1, 0), (-1, -1), "A", "B"),
        "h0_side1": ((-1, -1), (-1, -2), "B", "C"),
        "h0_c1": ((-1, -2), (0, -2), "C", None),
        "h1_mid": ((-1, -2), (-1, -3), "C", "D"),
        "h1_side2": ((-1, -3), (-1, -4), "D", "E"),
        "h1_c2": ((-1, -4), (0, -4), "E", None),
    }
    records = dict(protocol.source)
    for node in protocol.nodes:
        if node.phase in specifications:
            source_center, target_center, source_family, target_family = specifications[node.phase]
            index = node.site[0]
            source = rail_site(index, source_center)
            if sum(abs(a - b) for a, b in zip(source, node.site)) != 1:
                return False
            source_content = records.get(source)
            if source_content is None:
                return False
            if source_family is None:
                bit = bit_of(source_content)
            else:
                if source_content not in TAG_FAMILIES[source_family]:
                    return False
                bit = TAG_FAMILIES[source_family].index(source_content)
            expected = bit_content(bit) if target_family is None else tag_content(bit, target_family)
            if node.output != expected or node.site != rail_site(index, target_center):
                return False
            local = raw_signature(records, node.site)
            delta = tuple(a - b for a, b in zip(source, node.site))
            if (delta, source_content) not in local:
                return False
        put(records, node.site, node.output)
    return True


def exact_orders_ok(protocol: Protocol) -> bool:
    expected = {
        "c0_compare": tuple(range(48)),
        "h0_side0": tuple(range(47, -1, -1)),
        "h0_mid": tuple(range(48)),
        "h0_side1": tuple(range(47, -1, -1)),
        "h0_c1": tuple(range(48)),
        "c1_compare": tuple(range(47, -1, -1)),
        "h1_mid": tuple(range(48)),
        "h1_side2": tuple(range(47, -1, -1)),
        "h1_c2": tuple(range(48)),
        "c2_compare": tuple(range(48)),
    }
    for phase, order in expected.items():
        if tuple(node.site[0] for node in protocol.nodes if node.phase == phase) != order:
            return False
    for prefix in ("h0", "h1"):
        statuses = tuple(
            node.site[0] for node in protocol.nodes
            if node.phase == f"{prefix}_validate"
            and node.name != f"{prefix}_validation_start"
        )
        if statuses != tuple(range(47, -1, -1)):
            return False
    accept_word = tuple(
        node.site[0] for node in protocol.nodes
        if node.phase == "h0_accept_carry"
        and node.name.startswith("h0_accept_") and node.name[-2:].isdigit()
    )
    return accept_word == tuple(range(48))


def parent_edges_are_nn(protocol: Protocol) -> bool:
    by_name = protocol.by_name
    return all(
        sum(abs(a - b) for a, b in zip(by_name[parent].site, node.site)) == 1
        for node in protocol.nodes for parent in node.parents
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    mechanism_roles = (
        {content for family in TAG_FAMILIES.values() for content in family}
        | {content for pair in LAUNCH_ROLES.values() for content in pair}
        | set(TRANSITION_ROLES)
        | {
            BRIDGE_ROLE, VALIDATION_TURN, ACCEPT_CARRIER, COPY_GUARD,
            DEC_GUARD_Y, DEC_GUARD_ZP, DEC_GUARD_ZM, SMALL_GUARD,
            STATUS_GUARD, TOKEN_GUARD, ALL, AUX,
        }
    )
    protocols = tuple(build_protocol(index) for index in range(len(PROGRAM_ITEMS)))
    sample = protocols[0]
    overlap = set(NEW_RAW) & set(c93.COMBINED_RAW)

    section("A - Law integration and finite apparatus")
    check("A01 mechanism roles belong to the live alphabet", mechanism_roles <= c90.c89.FULL_ROLES)
    check("A02 protocol bank contains all 236 selected programs", len(protocols) == 236)
    check("A03 every protocol is finite and acyclic", all(
        len(topological_records(protocol)[1]) == len(protocol.nodes)
        for protocol in protocols
    ))
    check("A04 supplied/grown counts are explicit and constant", all(
        len(protocol.source) == 943 and len(protocol.nodes) == 680
        for protocol in protocols
    ), "943 supplied / 680 grown")
    check("A05 every supplied and grown content is live", all(
        set(protocol.source.values()) | {node.output for node in protocol.nodes}
        <= c90.c89.FULL_ROLES
        for protocol in protocols
    ))
    check("A06 new table is finite and nonempty", bool(NEW_TABLE), f"{len(NEW_TABLE)} canonical / {len(NEW_RAW)} raw")
    check("A07 Cycle95 raw rows are disjoint from Cycle93", not overlap, str(len(overlap)))
    check("A08 mixed Cycle93+95 union is single-valued", all(
        len(values) == 1 for values in COMBINED_RAW.values()
    ), str(len(COMBINED_RAW)))
    check("A09 every canonical row has all proper-cubic raw images", all(
        NEW_RAW.get(c53.rotate_signature(local, rotation)) == frozenset((output,))
        for local, output in NEW_TABLE.items() for rotation in c53.ROTATIONS
    ))

    section("B - Physical geometry, order, and no symbolic bypass")
    check("B01 all causal parent edges are strict nearest neighbours", all(parent_edges_are_nn(p) for p in protocols))
    check("B02 construction order is one append-only causal chain", all(
        not p.nodes[0].parents
        and all(p.nodes[index - 1].name in p.nodes[index].parents for index in range(1, len(p.nodes)))
        for p in protocols
    ))
    check("B03 exact compare/transport/validation bit orders hold", all(exact_orders_ok(p) for p in protocols))
    check("B04 every carried bit reads a physically adjacent prior bit/tag", all(
        physical_transport_ok(protocol) for protocol in protocols
    ))
    check("B05 sources and grown sites are pairwise disjoint", all(
        not (set(p.source) & {node.site for node in p.nodes})
        and len({node.site for node in p.nodes}) == len(p.nodes)
        for p in protocols
    ))
    check("B06 first two references mismatch and final reference equals candidate", all(
        PROGRAM_ITEMS[index][1] != PROGRAM_ITEMS[(index + 1) % 236][1]
        and PROGRAM_ITEMS[index][1] != PROGRAM_ITEMS[(index + 2) % 236][1]
        and protocols[index].reference_locals[2] == protocols[index].candidate_local
        for index in range(236)
    ))
    check("B07 selector decisions are AUX, AUX, then ALL", all(
        p.by_name["c0_decision"].output == AUX
        and p.by_name["c1_decision"].output == AUX
        and p.by_name["c2_decision"].output == ALL
        for p in protocols
    ))
    check("B08 both validation decisions are ALL on exact copies", all(
        p.by_name["h0_validation_decision"].output == ALL
        and p.by_name["h1_validation_decision"].output == ALL
        for p in protocols
    ))
    check("B09 AUX is the immediate physical parent of each transport launch", all(
        p.by_name["c0_decision"].name in p.by_name["h0_launch_0"].parents
        and p.by_name["c1_decision"].name in p.by_name["h1_launch_00"].parents
        for p in protocols
    ))
    check("B10 ALL immediately enters a physical accept chain before the next comparator", all(
        p.by_name["h0_validation_decision"].name in p.by_name["h0_accept_bridge"].parents
        and p.by_name["h1_validation_decision"].name in p.by_name["h1_accept_bridge"].parents
        and p.by_name["h0_next_start"].name in p.by_name["c1_status_00"].parents
        and p.by_name["h1_next_start"].name in p.by_name["c2_status_00"].parents
        for p in protocols
    ))

    section("C - All-236 exact live frontiers and append-only trails")
    success_results = tuple(verify_protocol_frontiers(p) for p in protocols)
    success_states = sum(result.states for result in success_results)
    check("C01 every one of 236 protocols has its exact live frontier", all(
        result.ok for result in success_results
    ), f"{success_states} states")
    check("C02 asynchronous scheduler has one enabled record per nonterminal", all(
        result.max_frontier == 1 for result in success_results
    ))
    check("C03 parasite census is zero extras/missing/conflicts", all(
        not result.detail for result in success_results
    ))

    terminal_ok = True
    writer_ok = True
    append_only_ok = True
    for index, protocol in enumerate(protocols):
        terminal, ordered = topological_records(protocol)
        candidate_local, candidate = PROGRAM_ITEMS[index]
        terminal_ok = terminal_ok and all(
            terminal[(bit_index, 0, layer)] == bit_content(candidate[bit_index])
            for layer in (0, -2, -4) for bit_index in range(48)
        )
        append_only_ok = append_only_ok and (
            len(terminal) == len(protocol.source) + len(protocol.nodes)
            and all(terminal[node.site] == node.output for node in ordered)
        )
        output = c90.c89.LIVE_TABLE[candidate_local]
        word = c90.c89.ROLE_TO_WORD[output]
        expected_writer = writer_additions(word, -4, False)
        actual_writer = tuple(
            (node.site, node.output) for node in protocol.nodes
            if node.phase == "c2_writer"
        )
        writer_ok = writer_ok and actual_writer == expected_writer
    check("C04 both handoffs preserve all 48 physical bits for all236", terminal_ok)
    check("C05 every source and grown record remains in the terminal trail", append_only_ok)
    check("C06 third ALL writes the exact selected 17-record output", writer_ok)
    check("C07 transported rails contain 22,656 checked bit records", 236 * 48 * 2 == 22656 and terminal_ok)

    section("D - Corruption detector: one new AUX and no advance")
    single_faults = tuple(
        verify_fault_case(sample, prefix, frozenset((index,)))
        for prefix in ("h0", "h1") for index in range(48)
    )
    mixed_masks = (frozenset(range(48)), frozenset((0, 7, 23, 47)))
    mixed_faults = tuple(
        verify_fault_case(sample, prefix, mask)
        for prefix in ("h0", "h1") for mask in mixed_masks
    )
    all_program_faults = tuple(
        verify_fault_case(protocol, prefix, frozenset((47,)))
        for protocol in protocols for prefix in ("h0", "h1")
    )
    fault_results = single_faults + mixed_faults + all_program_faults
    check("D01 every bit position is attacked in both handoffs", all(
        result.ok for result in single_faults
    ), "96 single-bit cases")
    check("D02 all-bit and separated mixed corruptions are absorbed", all(
        result.ok for result in mixed_faults
    ), "4 mixed cases")
    check("D03 all236 terminal-bit corruptions stop in both handoffs", all(
        result.ok for result in all_program_faults
    ), "472 program/handoff cases")
    check("D04 each perturbation occurs at a correctly enabled law site", all(
        result.injected > 0 for result in fault_results
    ))
    check("D05 each corrupted validation grows exactly one new AUX", all(
        result.new_aux == 1 for result in fault_results
    ))
    check("D06 every AUX detector terminal has an empty live frontier", all(
        not result.detail for result in fault_results
    ), f"{sum(result.states for result in fault_results)} states")
    check("D07 no corruption case teaches the law to make its wrong bit", all(
        result.ok for result in fault_results
    ), "each injected site was uniquely enabled with the opposite, correct law output")

    section("E - All 24 cubic images and mixed-law parasite controls")
    rotated = tuple(
        verify_protocol_frontiers(rotate_protocol(sample, rotation))
        for rotation in c53.ROTATIONS
    )
    check("E01 proper cubic group has exactly 24 images", len(c53.ROTATIONS) == len(set(c53.ROTATIONS)) == 24)
    check("E02 every full rotated protocol has the exact frontier", all(
        result.ok for result in rotated
    ), f"{sum(result.states for result in rotated)} rotated states")
    check("E03 every rotated nonterminal frontier remains singleton", all(
        result.max_frontier == 1 for result in rotated
    ))
    check("E04 Cycle93+95 mixed roles create no live parasite", not overlap and all(
        result.ok for result in success_results + rotated
    ))
    check("E05 corrected BACKSTOP status cage is absent from Cycle93 inputs", all(
        STATUS_GUARD not in {content for _direction, content in local}
        for local in c93.COMBINED_RAW
    ))
    check("E06 phase-tagged cable roles are absent from Cycle93 inputs", all(
        content not in {value for local in c93.COMBINED_RAW for _direction, value in local}
        for content in ({value for pair in LAUNCH_ROLES.values() for value in pair} | set(TRANSITION_ROLES))
    ))

    section("F - Scope and authority")
    check("F01 supplied state is explicitly counted", len(sample.source) == 943, str(Counter(sample.source.values())))
    grown_phases = Counter(node.phase for node in sample.nodes)
    check("F02 grown state is explicitly phase-counted", sum(grown_phases.values()) == 680, str(grown_phases))
    source_lines = Path(__file__).read_text().splitlines()
    check("F03 no Cycle94 module is imported", all(
        "cycle94" not in line.lower()
        for line in source_lines
        if line.startswith("import ") or line.startswith("from ")
    ))
    check("F04 runner claims no foundation, queue, audit, or git authority", "Authority: none." in (__doc__ or ""))
    note_text = NOTE.read_text() if NOTE.exists() else ""
    check("F05 companion Cycle95 note exists", bool(note_text))
    check("F06 note contains the complete written N1-N8 gate", all(
        f"### N{index}" in note_text for index in range(1, 9)
    ) and "Gate outcome:" in note_text)

    print(f"\nNEW_CANONICAL={len(NEW_TABLE)} NEW_RAW={len(NEW_RAW)} OVERLAP={len(overlap)} UNION={len(COMBINED_RAW)}")
    print(
        f"PROGRAMS={len(protocols)} SUCCESS_STATES={success_states} "
        f"CUBIC_STATES={sum(result.states for result in rotated)}"
    )
    print(f"FAULT_CASES={len(fault_results)} FAULT_STATES={sum(result.states for result in fault_results)}")
    print(f"SUPPLIED={len(sample.source)} GROWN={len(sample.nodes)}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
