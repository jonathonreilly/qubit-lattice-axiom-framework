#!/usr/bin/env python3
"""Cycle 105: read status to a generated, role-closed rail spine.

The only initial records are the exact Cycle-100 terminal records consumed by
Cycle 101.  A reverse shell grows from the already-generated Cycle-52 A slice
toward Cycle 101's physical readout.  Its first status/rail join has an exact
three-parent signature: literal OUTPUT, the CERT-derived role-closed type, and
the generated rail-spine tip.  The join then grows a proper-cubic three-image
cap whose onsite content is the literal typed payload R_B11.

Cycle 104's role-closed rail remap needs two integration substitutions before
it can coexist with Cycle 101 beyond the first slice.  C_3_1 -> J2 and
D_1_1 -> J1 remove the R_B31/R_B12 aliases that otherwise wake Cycle 101's
two unary caps.  The repaired union is exhausted through eight rail slices,
all asynchronous reader/spine/rail schedules, all one-bit word corruptions,
and all proper-cubic rotations.

Authority: none.  No foundation, queue, policy, audit, or git mutation follows.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import fragment_safe_role_remap_type_integration_cycle108_2026_07_15 as c108
import live_eight_bit_physical_comparator_cycle89_2026_07_15 as c89
import onsite_alphabet_closed_frame_rail_cycle104_2026_07_15 as c104
import zero_source_relational_first_harness_cycle101_2026_07_15 as c101


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "READ_STATUS_TO_GENERATED_RAIL_SPINE_CYCLE105_NOTE_2026-07-15.md"

Coord = tuple[int, int, int]
Signature = c101.Signature
RawTable = dict[Signature, frozenset[str]]
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def merge_raw(*tables: RawTable) -> RawTable:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


def neighbors(site: Coord) -> frozenset[Coord]:
    return frozenset(c101.add(site, direction) for direction in c101.c100.c53.DIRECTIONS)


def transform_records(
    records: dict[Coord, str],
    rotation: c104.c52.Rotation,
    shift: Coord,
) -> dict[Coord, str]:
    return {
        c101.transform_site(site, rotation, shift): content
        for site, content in records.items()
    }


# ---------------------------------------------------------------------------
# Integrated onsite-alphabet rail repair.
#
# Cycle 104's exact map is retained except for the two output roles that alias
# Cycle 101's only unary fragment rows after later rail slices.  J1 and J2 are
# already-live, unary-inert FULL_ROLES contents.  The 36 B/C/D roles remain
# injective and every A role remains unchanged.
# ---------------------------------------------------------------------------

ROLE_MAP = dict(c108.ROLE_MAP)
REMAPPED_RAW = c108.REMAPPED_RAW
BASE_RAW = c108.INTEGRATED_RAW
RAIL_SEQUENCE = c108.NINE_SLICES
RAIL_HORIZON = c108.HORIZON      # eight complete 12-record slices
FIRST_RAIL = RAIL_SEQUENCE[0]
NEXT_RAIL = RAIL_SEQUENCE[RAIL_HORIZON]


# ---------------------------------------------------------------------------
# Reverse generated-rail shell and literal three-parent join.
#
# The shell starts beside persistent A_3_0 and runs toward the readout.  The
# P2 step has two proper-cubic images; both are physical writes and neither is
# supplied.  NATURAL_TYPE is an inherited remapped-rail write: sole R_B40 at
# Cycle 101 CERT grows R_B21.  The final join literally sees OUTPUT H1,
# NATURAL_TYPE R_B21, and the BTG rail-spine tip.
# ---------------------------------------------------------------------------

NATURAL_TYPE: Coord = (4, 5, 1)
NATURAL_TYPE_OUTPUT = "R_B21"

PRIMARY_SPINE: tuple[Coord, ...] = (
    (0, 0, 3),
    (1, 0, 3),
    (2, 0, 3),
    (2, -1, 3),
    (3, -1, 3),
    (3, -1, 2),
    (3, -1, 1),
    (3, -1, 0),
    (4, -1, 0),
    (4, 0, 0),
    (4, 1, 0),
    (4, 2, 0),
    (4, 3, 0),
    (4, 4, 0),
    (4, 5, 0),
    (4, 6, 0),
)

SPINE_OUTPUTS: tuple[str, ...] = (
    "AUXZ",
    "C_Q",
    "BTP",
    "L3",
    "ARM",
    "W1",
    "AUXY",
    "R_A31",
    "OPEN_B",
    "MARK",
    "P2",
    "OY",
    "TZ",
    "J3",
    "AUX",
    "BTG",
)

P2_SIBLING: Coord = (4, 0, 1)
SPINE_GROUPS: tuple[tuple[Coord, ...], ...] = tuple(
    (site, P2_SIBLING) if index == 10 else (site,)
    for index, site in enumerate(PRIMARY_SPINE)
)

JOIN: Coord = (4, 6, 1)
JOIN_OUTPUT = "JOINT"
PAYLOAD_SITES: tuple[Coord, ...] = ((4, 6, 2), (4, 7, 1), (5, 6, 1))
PAYLOAD_OUTPUT = "R_B11"


def build_bridge_table() -> tuple[dict[Signature, str], tuple[tuple[Coord, ...], ...]]:
    records = dict(c101.TERMINAL)
    records.update(c101.FRAGMENT_OUTPUTS)
    records[NATURAL_TYPE] = NATURAL_TYPE_OUTPUT
    table: dict[Signature, str] = {}
    observed_groups: list[tuple[Coord, ...]] = []

    for primary, output, declared in zip(PRIMARY_SPINE, SPINE_OUTPUTS, SPINE_GROUPS):
        local = c101.c100.c53.local_signature(records, primary)
        canonical = c101.c100.c53.canonical_signature(local)
        prior = table.get(canonical)
        if prior is not None and prior != output:
            raise ValueError((canonical, prior, output))
        matches = tuple(sorted(
            target
            for target in c101.c100.c53.open_candidates(records)
            if c101.c100.c53.canonical_signature(
                c101.c100.c53.local_signature(records, target)
            ) == canonical
        ))
        if matches != tuple(sorted(declared)):
            raise ValueError((primary, declared, matches))
        table[canonical] = output
        observed_groups.append(matches)
        records.update({target: output for target in matches})

    join_local = c101.c100.c53.local_signature(records, JOIN)
    join_canonical = c101.c100.c53.canonical_signature(join_local)
    if join_canonical in table and table[join_canonical] != JOIN_OUTPUT:
        raise ValueError((join_canonical, table[join_canonical], JOIN_OUTPUT))
    table[join_canonical] = JOIN_OUTPUT
    records[JOIN] = JOIN_OUTPUT

    payload_canonical = c101.c100.c53.canonical_signature(
        (((1, 0, 0), JOIN_OUTPUT),)
    )
    matches = tuple(sorted(
        target
        for target in c101.c100.c53.open_candidates(records)
        if c101.c100.c53.canonical_signature(
            c101.c100.c53.local_signature(records, target)
        ) == payload_canonical
    ))
    if matches != tuple(sorted(PAYLOAD_SITES)):
        raise ValueError((PAYLOAD_SITES, matches))
    table[payload_canonical] = PAYLOAD_OUTPUT
    return table, tuple(observed_groups)


BRIDGE_TABLE, OBSERVED_SPINE_GROUPS = build_bridge_table()
BRIDGE_RAW = c59.raw_rule_outputs(BRIDGE_TABLE)
FULL_RAW = merge_raw(BASE_RAW, BRIDGE_RAW)


def enabled(
    records: dict[Coord, str],
    raw: RawTable = FULL_RAW,
) -> dict[Coord, frozenset[str]]:
    return {
        target: raw[local]
        for target in c101.c100.c53.open_candidates(records)
        if (local := c101.c100.c53.local_signature(records, target)) in raw
    }


FRAGMENT_SITES = tuple(sorted(c101.FRAGMENT_OUTPUTS))
FRAGMENT_INDEX = {site: index for index, site in enumerate(FRAGMENT_SITES)}
ALL_FRAGMENT_MASK = (1 << len(FRAGMENT_SITES)) - 1
ALL_PAYLOAD_MASK = (1 << len(PAYLOAD_SITES)) - 1

PositiveState = tuple[int, int, int, int, int, int]
CorruptState = tuple[int, int, int]


def positive_records(state: PositiveState) -> dict[Coord, str]:
    fragment_mask, natural, spine_prefix, sibling, joined, payload_mask = state
    records = dict(c101.TERMINAL)
    for index, site in enumerate(FRAGMENT_SITES):
        if fragment_mask >> index & 1:
            records[site] = c101.FRAGMENT_OUTPUTS[site]
    if natural:
        records[NATURAL_TYPE] = NATURAL_TYPE_OUTPUT
    records.update(dict(zip(PRIMARY_SPINE[:spine_prefix], SPINE_OUTPUTS[:spine_prefix])))
    if sibling:
        records[P2_SIBLING] = SPINE_OUTPUTS[10]
    if joined:
        records[JOIN] = JOIN_OUTPUT
    for index, site in enumerate(PAYLOAD_SITES):
        if payload_mask >> index & 1:
            records[site] = PAYLOAD_OUTPUT
    return records


@dataclass(frozen=True)
class PositiveStats:
    states: int
    edges: int
    terminals: int
    terminal_states: tuple[PositiveState, ...]
    bad: tuple[object, ...]
    premature: tuple[PositiveState, ...]
    join_reached: bool
    payload_reached: bool


def positive_graph() -> PositiveStats:
    start: PositiveState = (0, 0, 0, 0, 0, 0)
    queue = deque((start,))
    seen = {start}
    edges = 0
    terminals: list[PositiveState] = []
    bad: list[object] = []
    premature: list[PositiveState] = []

    while queue:
        state = queue.popleft()
        fragment_mask, natural, spine_prefix, sibling, joined, payload_mask = state
        records = positive_records(state)
        actual = enabled(records)
        legal: list[tuple[str, int]] = []

        for target, values in actual.items():
            if target == FIRST_RAIL[0] and values == frozenset((FIRST_RAIL[1],)):
                continue
            if (
                target in FRAGMENT_INDEX
                and not fragment_mask >> FRAGMENT_INDEX[target] & 1
                and values == frozenset((c101.FRAGMENT_OUTPUTS[target],))
            ):
                legal.append(("fragment", FRAGMENT_INDEX[target]))
            elif (
                not natural
                and target == NATURAL_TYPE
                and values == frozenset((NATURAL_TYPE_OUTPUT,))
            ):
                legal.append(("natural", 0))
            elif (
                spine_prefix < len(PRIMARY_SPINE)
                and target == PRIMARY_SPINE[spine_prefix]
                and values == frozenset((SPINE_OUTPUTS[spine_prefix],))
            ):
                legal.append(("spine", 0))
            elif (
                spine_prefix >= 10
                and not sibling
                and target == P2_SIBLING
                and values == frozenset((SPINE_OUTPUTS[10],))
            ):
                legal.append(("sibling", 0))
            elif not joined and target == JOIN and values == frozenset((JOIN_OUTPUT,)):
                legal.append(("join", 0))
            elif (
                target in PAYLOAD_SITES
                and not payload_mask >> PAYLOAD_SITES.index(target) & 1
                and values == frozenset((PAYLOAD_OUTPUT,))
            ):
                legal.append(("payload", PAYLOAD_SITES.index(target)))
            else:
                bad.append((state, target, values, actual))
                break
        if bad:
            break

        output_present = bool(fragment_mask >> FRAGMENT_INDEX[c101.OUTPUT] & 1)
        if joined and not (
            natural and output_present and spine_prefix == len(PRIMARY_SPINE)
        ):
            premature.append(state)
        if payload_mask and not joined:
            premature.append(state)

        if not legal:
            terminals.append(state)
            continue

        for kind, index in legal:
            future = list(state)
            if kind == "fragment":
                future[0] |= 1 << index
            elif kind == "natural":
                future[1] = 1
            elif kind == "spine":
                future[2] += 1
            elif kind == "sibling":
                future[3] = 1
            elif kind == "join":
                future[4] = 1
            else:
                future[5] |= 1 << index
            next_state = tuple(future)  # type: ignore[assignment]
            edges += 1
            if next_state not in seen:
                seen.add(next_state)
                queue.append(next_state)

    return PositiveStats(
        states=len(seen),
        edges=edges,
        terminals=len(terminals),
        terminal_states=tuple(terminals),
        bad=tuple(bad),
        premature=tuple(premature),
        join_reached=any(state[4] for state in seen),
        payload_reached=any(state[5] for state in seen),
    )


@dataclass(frozen=True)
class CorruptStats:
    states: int
    edges: int
    terminals: int
    terminal_states: tuple[CorruptState, ...]
    bad: tuple[object, ...]
    join_reached: bool
    payload_reached: bool


def corrupt_records(
    source: dict[Coord, str],
    outputs: dict[Coord, str],
    state: CorruptState,
) -> dict[Coord, str]:
    fragment_mask, spine_prefix, sibling = state
    sites = tuple(sorted(outputs))
    records = dict(source)
    for index, site in enumerate(sites):
        if fragment_mask >> index & 1:
            records[site] = outputs[site]
    records.update(dict(zip(PRIMARY_SPINE[:spine_prefix], SPINE_OUTPUTS[:spine_prefix])))
    if sibling:
        records[P2_SIBLING] = SPINE_OUTPUTS[10]
    return records


def corrupt_graph(
    source: dict[Coord, str],
    *,
    allow_bit5_reject: bool = False,
) -> tuple[CorruptStats, dict[Coord, str]]:
    outputs = dict(c101.FRAGMENT_OUTPUTS)
    if allow_bit5_reject:
        outputs[c101.BIT5_REJECT] = c101.H1
    sites = tuple(sorted(outputs))
    site_index = {site: index for index, site in enumerate(sites)}

    start: CorruptState = (0, 0, 0)
    queue = deque((start,))
    seen = {start}
    edges = 0
    terminals: list[CorruptState] = []
    bad: list[object] = []

    while queue:
        state = queue.popleft()
        fragment_mask, spine_prefix, sibling = state
        records = corrupt_records(source, outputs, state)
        actual = enabled(records)
        legal: list[tuple[str, int]] = []

        for target, values in actual.items():
            if target == FIRST_RAIL[0] and values == frozenset((FIRST_RAIL[1],)):
                continue
            if (
                target in site_index
                and not fragment_mask >> site_index[target] & 1
                and values == frozenset((outputs[target],))
            ):
                legal.append(("fragment", site_index[target]))
            elif (
                spine_prefix < len(PRIMARY_SPINE)
                and target == PRIMARY_SPINE[spine_prefix]
                and values == frozenset((SPINE_OUTPUTS[spine_prefix],))
            ):
                legal.append(("spine", 0))
            elif (
                spine_prefix >= 10
                and not sibling
                and target == P2_SIBLING
                and values == frozenset((SPINE_OUTPUTS[10],))
            ):
                legal.append(("sibling", 0))
            else:
                bad.append((state, target, values, actual))
                break
        if bad:
            break

        if not legal:
            terminals.append(state)
            continue
        for kind, index in legal:
            if kind == "fragment":
                future = (fragment_mask | 1 << index, spine_prefix, sibling)
            elif kind == "spine":
                future = (fragment_mask, spine_prefix + 1, sibling)
            else:
                future = (fragment_mask, spine_prefix, 1)
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)

    joined_sites = {JOIN, *PAYLOAD_SITES}
    reached = any(
        joined_sites & set(corrupt_records(source, outputs, state))
        for state in seen
    )
    return (
        CorruptStats(
            states=len(seen),
            edges=edges,
            terminals=len(terminals),
            terminal_states=tuple(terminals),
            bad=tuple(bad),
            join_reached=reached,
            payload_reached=reached,
        ),
        outputs,
    )


POSITIVE = positive_graph()


def positive_terminal_records() -> dict[Coord, str]:
    if len(POSITIVE.terminal_states) != 1:
        raise RuntimeError(POSITIVE)
    return positive_records(POSITIVE.terminal_states[0])


def unary_outputs(raw: RawTable, role: str) -> frozenset[str]:
    return frozenset(
        output
        for local, values in raw.items()
        if len(local) == 1 and local[0][1] == role
        for output in values
    )


def source_map_and_table_contract() -> None:
    section("A - Exact source, integrated role closure, and finite table")
    check("A01 Cycle 105 note exists", NOTE.is_file())
    check(
        "A02 only source is exact 264-record Cycle-100 terminal",
        c101.TERMINAL == c101.c100.records_at(len(c101.c100.ADDITIONS))
        and len(c101.TERMINAL) == 264,
    )
    check(
        "A03 generated A slice and BACKSTOP are already source records",
        len(c101.RAIL_SEED) == 13
        and all(c101.TERMINAL.get(site) == content for site, content in c101.RAIL_SEED.items()),
    )
    changed = {
        role: (c104.ROLE_MAP[role], ROLE_MAP[role])
        for role in ROLE_MAP
        if ROLE_MAP[role] != c104.ROLE_MAP[role]
    }
    check(
        "A04 integrated rail changes exactly C_3_1 and D_1_1 to J2/J1",
        changed == {"C_3_1": ("R_B31", "J2"), "D_1_1": ("R_B12", "J1")},
        str(changed),
    )
    check(
        "A05 all 36 B/C/D mappings remain injective and role-closed",
        set(ROLE_MAP) == c104.PHASE_DOMAIN
        and len(set(ROLE_MAP.values())) == 36
        and set(ROLE_MAP.values()) <= c89.FULL_ROLES,
    )
    check(
        "A06 four unary-hazard codomain roles are absent",
        {"R_LB", "R_LC", "R_B12", "R_B31"}.isdisjoint(ROLE_MAP.values())
        and not unary_outputs(c101.c100.COMBINED_RAW, "J1")
        and not unary_outputs(c101.c100.COMBINED_RAW, "J2"),
    )
    check(
        "A07 repaired rail has 1,080 raw rows disjoint from Cycle 100",
        len(REMAPPED_RAW) == 1_080
        and set(REMAPPED_RAW).isdisjoint(c101.c100.COMBINED_RAW)
        and all(len(values) == 1 for values in REMAPPED_RAW.values()),
    )
    check(
        "A08 Cycle100 + reader + rail is 6,896 single-valued rows",
        len(BASE_RAW) == 6_896 and all(len(values) == 1 for values in BASE_RAW.values()),
    )
    check(
        "A09 bridge contributes 18 canonical and 414 disjoint raw rows",
        len(BRIDGE_TABLE) == 18
        and len(BRIDGE_RAW) == 414
        and set(BRIDGE_RAW).isdisjoint(BASE_RAW),
    )
    table_contents = {
        content for local in FULL_RAW for _direction, content in local
    } | {
        output for values in FULL_RAW.values() for output in values
    }
    check(
        "A10 complete 7,310-row union is single-valued and FULL_ROLES-closed",
        len(FULL_RAW) == 7_310
        and all(len(values) == 1 for values in FULL_RAW.values())
        and table_contents <= c89.FULL_ROLES,
    )


def literal_join_and_payload_contract() -> None:
    section("B - Literal read-status / generated-rail join and first payload")
    grown_spine_sites = {site for group in SPINE_GROUPS for site in group}
    check(
        "B01 zero bridge records are supplied",
        grown_spine_sites.isdisjoint(c101.TERMINAL)
        and NATURAL_TYPE not in c101.TERMINAL
        and JOIN not in c101.TERMINAL
        and set(PAYLOAD_SITES).isdisjoint(c101.TERMINAL),
    )
    check(
        "B02 reverse shell has 17 writes in sixteen generations",
        len(grown_spine_sites) == 17
        and len(SPINE_GROUPS) == 16
        and OBSERVED_SPINE_GROUPS == tuple(tuple(sorted(group)) for group in SPINE_GROUPS),
    )
    first_records = dict(c101.TERMINAL)
    first_signature = c101.c100.c53.local_signature(first_records, PRIMARY_SPINE[0])
    check(
        "B03 first shell write literally consumes persistent A_3_0 plus old H0",
        {content for _direction, content in first_signature} == {"A_3_0", c101.H0}
        and c101.TERMINAL.get((-1, 0, 3)) == "A_3_0",
        str(first_signature),
    )
    natural_records = dict(c101.TERMINAL)
    natural_records.update(c101.FRAGMENT_OUTPUTS)
    natural_signature = c101.c100.c53.local_signature(natural_records, NATURAL_TYPE)
    check(
        "B04 inherited type is exact sole CERT R_B40 -> R_B21",
        natural_signature == (((-1, 0, 0), "R_B40"),)
        and FULL_RAW.get(natural_signature) == frozenset((NATURAL_TYPE_OUTPUT,))
        and c101.CERTIFICATE == (3, 5, 1),
        str(natural_signature),
    )
    before_join = positive_records((
        ALL_FRAGMENT_MASK,
        1,
        len(PRIMARY_SPINE),
        1,
        0,
        0,
    ))
    join_signature = c101.c100.c53.local_signature(before_join, JOIN)
    join_parents = {
        c101.add(JOIN, direction): content
        for direction, content in join_signature
    }
    check(
        "B05 first join literally consumes OUTPUT, CERT-type, and rail-spine tip",
        join_parents == {
            c101.OUTPUT: c101.H1,
            NATURAL_TYPE: NATURAL_TYPE_OUTPUT,
            PRIMARY_SPINE[-1]: "BTG",
        },
        str(join_parents),
    )
    missing_parent_failures = []
    for parent in (c101.OUTPUT, NATURAL_TYPE, PRIMARY_SPINE[-1]):
        records = dict(before_join)
        records.pop(parent)
        if FULL_RAW.get(c101.c100.c53.local_signature(records, JOIN)) is not None:
            missing_parent_failures.append(parent)
    check(
        "B06 removing any one of the three join parents disables the join",
        not missing_parent_failures,
        str(missing_parent_failures),
    )
    joined = dict(before_join)
    joined[JOIN] = JOIN_OUTPUT
    payload_matches = {
        target
        for target, values in enabled(joined).items()
        if values == frozenset((PAYLOAD_OUTPUT,))
    }
    check(
        "B07 join grows exactly three proper-cubic R_B11 payload images",
        payload_matches == set(PAYLOAD_SITES)
        and all(c101.manhattan(left, right) == 2 for index, left in enumerate(PAYLOAD_SITES) for right in PAYLOAD_SITES[index + 1:]),
        str(payload_matches),
    )
    check(
        "B08 payload is literal typed content for the read word",
        PAYLOAD_OUTPUT == "R_B11"
        and c101.c100.R_B11_WORD == (1, 0, 0, 1, 0, 1, 0, 0),
    )
    p2_records = dict(c101.TERMINAL)
    p2_records.update(c101.FRAGMENT_OUTPUTS)
    p2_records[NATURAL_TYPE] = NATURAL_TYPE_OUTPUT
    for group, output in zip(SPINE_GROUPS[:10], SPINE_OUTPUTS[:10]):
        p2_records.update({site: output for site in group})
    p2_front = {
        target
        for target, values in enabled(p2_records).items()
        if values == frozenset((SPINE_OUTPUTS[10],))
    }
    check(
        "B09 P2 cap's two images are simultaneously enabled, grown, and unsupplied",
        p2_front == set(SPINE_GROUPS[10])
        and set(SPINE_GROUPS[10]).isdisjoint(c101.TERMINAL),
        str(p2_front),
    )


def async_and_rail_factor_contract() -> None:
    section("C - Complete reader/spine graph and eight-slice rail product")
    check(
        "C01 exact reader/spine graph has 5,048 states and 21,426 edges",
        POSITIVE.states == 5_048 and POSITIVE.edges == 21_426,
        str(POSITIVE),
    )
    terminal_expected: PositiveState = (
        ALL_FRAGMENT_MASK,
        1,
        len(PRIMARY_SPINE),
        1,
        1,
        ALL_PAYLOAD_MASK,
    )
    check(
        "C02 every reader/spine schedule reaches one complete terminal",
        POSITIVE.terminals == 1
        and POSITIVE.terminal_states == (terminal_expected,)
        and not POSITIVE.bad
        and POSITIVE.join_reached
        and POSITIVE.payload_reached,
        str(POSITIVE.terminal_states),
    )
    check(
        "C03 no join or payload is ever premature",
        not POSITIVE.premature,
        str(POSITIVE.premature[:1]),
    )
    terminal = positive_terminal_records()
    check(
        "C04 completed reader/spine exposes only first repaired rail write",
        enabled(terminal) == {FIRST_RAIL[0]: frozenset((FIRST_RAIL[1],))},
        str(enabled(terminal)),
    )

    trajectory_failures = []
    records = dict(terminal)
    for index, (site, content) in enumerate(RAIL_SEQUENCE[:RAIL_HORIZON]):
        actual = enabled(records)
        expected = {site: frozenset((content,))}
        if actual != expected:
            trajectory_failures.append((index, expected, actual))
            break
        records[site] = content
    check(
        "C05 full terminal grows eight repaired rail slices with singleton fronts",
        not trajectory_failures,
        str(trajectory_failures[:1]),
    )
    check(
        "C06 eight slices expose only exact ninth-slice start",
        enabled(records) == {NEXT_RAIL[0]: frozenset((NEXT_RAIL[1],))},
        str(enabled(records)),
    )

    fb_variable = (
        set(FRAGMENT_SITES)
        | {NATURAL_TYPE, JOIN, P2_SIBLING}
        | set(PRIMARY_SPINE)
        | set(PAYLOAD_SITES)
    )
    rail_sites = {site for site, _content in RAIL_SEQUENCE[:RAIL_HORIZON]}
    common_targets = {
        target
        for left in fb_variable
        for right in rail_sites
        for target in neighbors(left) & neighbors(right)
    }
    min_distance = min(c101.manhattan(left, right) for left in fb_variable for right in rail_sites)
    check(
        "C07 factor fronts share only occupied persistent A_3_0",
        min_distance == 2
        and common_targets == {(-1, 0, 3)}
        and c101.TERMINAL.get((-1, 0, 3)) == "A_3_0",
        f"distance={min_distance} common={common_targets}",
    )
    product_states = POSITIVE.states * (RAIL_HORIZON + 1)
    product_edges = (
        POSITIVE.edges * (RAIL_HORIZON + 1)
        + POSITIVE.states * RAIL_HORIZON
    )
    check(
        "C08 exact locality factor exhausts 489,656 states / 2,562,930 edges",
        product_states == 489_656 and product_edges == 2_562_930,
        f"states={product_states} edges={product_edges}",
    )

    original_raw = merge_raw(c104.MIXED_RAW, c101.FRAGMENT_RAW)
    original_records = dict(c101.TERMINAL)
    original_records.update(c101.FRAGMENT_OUTPUTS)
    original_records[NATURAL_TYPE] = NATURAL_TYPE_OUTPUT
    original_records.update(dict(c104.NINE_SLICES[:16]))
    original_actual = enabled(original_records, original_raw)
    expected_original = {
        c104.NINE_SLICES[16][0]: frozenset((c104.NINE_SLICES[16][1],))
    }
    extras = set(original_actual) - set(expected_original)
    check(
        "C09 unmodified Cycle104 map is executably rejected at prefix 16",
        extras == {(-4, 1, 3), (-3, 1, 4)}
        and all(original_actual[site] == frozenset(("R_B32",)) for site in extras),
        str(original_actual),
    )


CORRUPT_EXPECTED = (
    (760, 2_274),
    (680, 2_022),
    (600, 1_770),
    (440, 1_186),
    (120, 238),
    (200, 490),
    (80, 152),
    (60, 109),
)


def corruption_contract() -> list[tuple[dict[Coord, str], dict[Coord, str], CorruptStats]]:
    section("D - Every literal corruption and handshake error fails closed")
    cases: list[tuple[dict[Coord, str], dict[Coord, str], CorruptStats]] = []
    observed = []
    failures = []
    for index, site in enumerate(c101.c100.CODE_SITES):
        source = dict(c101.TERMINAL)
        source[site] = c101.H0 if source[site] == c101.H1 else c101.H1
        stats, outputs = corrupt_graph(source, allow_bit5_reject=index == 5)
        observed.append((stats.states, stats.edges))
        cases.append((source, outputs, stats))
        if (
            stats.terminals != 1
            or stats.bad
            or stats.join_reached
            or stats.payload_reached
            or len(stats.terminal_states) != 1
            or stats.terminal_states[0][1:] != (14, 1)
        ):
            failures.append((index, stats))
    check(
        "D01 all eight one-bit flips stop before join and payload",
        not failures,
        str(failures[:1]),
    )
    check(
        "D02 exact corrupted graph census is pinned",
        tuple(observed) == CORRUPT_EXPECTED,
        str(observed),
    )

    status_results = []
    for site in (c101.c100.VALID, c101.c100.READY):
        source = dict(c101.TERMINAL)
        source[site] = c101.H0
        stats, outputs = corrupt_graph(source)
        status_results.append((stats.states, stats.edges, stats))
        cases.append((source, outputs, stats))
    check(
        "D03 wrong VALID and READY remain exact fail-closed products",
        [(states, edges) for states, edges, _stats in status_results] == [(40, 66), (20, 23)]
        and all(stats.terminals == 1 and not stats.bad and not stats.join_reached for _states, _edges, stats in status_results),
        str([(states, edges) for states, edges, _stats in status_results]),
    )

    bit5_source, bit5_outputs, bit5_stats = cases[5]
    bit5_terminal = corrupt_records(bit5_source, bit5_outputs, bit5_stats.terminal_states[0])
    check(
        "D04 bit5 reject poison remains explicit and terminal",
        bit5_terminal.get(c101.BIT5_REJECT) == c101.H1,
    )
    rail_failures = []
    for case_index, (source, outputs, stats) in enumerate(cases):
        records = corrupt_records(source, outputs, stats.terminal_states[0])
        for rail_prefix, (site, content) in enumerate(RAIL_SEQUENCE[:RAIL_HORIZON]):
            actual = enabled(records)
            expected = {site: frozenset((content,))}
            if actual != expected:
                rail_failures.append((case_index, rail_prefix, expected, actual))
                break
            records[site] = content
        if not rail_failures and enabled(records) != {
            NEXT_RAIL[0]: frozenset((NEXT_RAIL[1],))
        }:
            rail_failures.append((case_index, RAIL_HORIZON, "next rail", enabled(records)))
    check(
        "D05 all corrupt terminals grow eight exact rail slices without acceptance",
        not rail_failures
        and all(not stats.join_reached and not stats.payload_reached for _source, _outputs, stats in cases),
        str(rail_failures[:1]),
    )
    return cases


def covariance_and_scope_contract(
    corrupt_cases: list[tuple[dict[Coord, str], dict[Coord, str], CorruptStats]],
) -> None:
    section("E - Proper-cubic covariance, old debris, and bounded scope")
    covariance_failures = []
    controls = 0
    for local, values in FULL_RAW.items():
        for rotation in c101.c100.c53.ROTATIONS:
            controls += 1
            actual = FULL_RAW.get(c101.c100.c53.rotate_signature(local, rotation))
            if actual != values:
                covariance_failures.append((local, rotation, values, actual))
    check(
        "E01 all 175,440 raw proper-cubic images preserve output",
        controls == len(FULL_RAW) * 24 == 175_440 and not covariance_failures,
        str(covariance_failures[:1]),
    )

    complete = positive_terminal_records()
    complete.update(dict(RAIL_SEQUENCE[:RAIL_HORIZON]))
    terminal_cases = [("positive", complete, NEXT_RAIL)]
    for index, (source, outputs, stats) in enumerate(corrupt_cases):
        records = corrupt_records(source, outputs, stats.terminal_states[0])
        records.update(dict(RAIL_SEQUENCE[:RAIL_HORIZON]))
        terminal_cases.append((f"corrupt-{index}", records, NEXT_RAIL))

    rotated_failures = []
    shift = (131, -97, 73)
    for label, records, expected_front in terminal_cases:
        for rotation in c101.c100.c53.ROTATIONS:
            transformed = transform_records(records, rotation, shift)
            expected_site = c101.transform_site(expected_front[0], rotation, shift)
            actual = enabled(transformed)
            expected = {expected_site: frozenset((expected_front[1],))}
            if actual != expected:
                rotated_failures.append((label, rotation, expected, actual))
                break
    check(
        "E02 all 264 positive/corrupt terminal rotations expose only next rail",
        len(terminal_cases) == 11 and not rotated_failures,
        str(rotated_failures[:1]),
    )

    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("E03 note pins zero supplied static residue", "zero supplied static residue" in note)
    check("E04 note closes READ_STATUS_TO_GENERATED_RAIL_SPINE", "read_status_to_generated_rail_spine" in note and "closed" in note)
    check("E05 note names the next constructive surface", "typed_payload_cap_to_reusable_harness" in note)
    check("E06 note carries full N1-N8 discipline", all(f"n{index}" in note for index in range(1, 9)))
    check("E07 note makes no complete reusable-harness claim", "does not close the complete reusable harness" in note)
    check("E08 Cycle 105 writes only runner and note", all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    source_map_and_table_contract()
    literal_join_and_payload_contract()
    async_and_rail_factor_contract()
    corrupt_cases = corruption_contract()
    covariance_and_scope_contract(corrupt_cases)
    product_states = POSITIVE.states * (RAIL_HORIZON + 1)
    product_edges = POSITIVE.edges * (RAIL_HORIZON + 1) + POSITIVE.states * RAIL_HORIZON
    print(
        f"\nSOURCE={len(c101.TERMINAL)} SUPPLIED_STATIC=0 "
        f"SPINE_WRITES={sum(map(len, SPINE_GROUPS))} PAYLOAD_WRITES={len(PAYLOAD_SITES)}"
    )
    print(
        f"BASE_RAW={len(BASE_RAW)} BRIDGE_CANONICAL={len(BRIDGE_TABLE)} "
        f"BRIDGE_RAW={len(BRIDGE_RAW)} FULL_RAW={len(FULL_RAW)}"
    )
    print(
        f"FB_STATES={POSITIVE.states} FB_EDGES={POSITIVE.edges} "
        f"PRODUCT_STATES={product_states} PRODUCT_EDGES={product_edges}"
    )
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
