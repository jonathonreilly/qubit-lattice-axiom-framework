#!/usr/bin/env python3
"""Cycle 106: first self-grown selector payload, literal bit-0 instance.

Extract the exact first-bit dependency cone from Cycle 95, then replace that
supplied mini-apparatus with records grown from the Cycle-100 terminal, the
Cycle-101 literal reader, and the fragment-safe Cycle-108 frame rail.  The
positive construction is the fixed literal bit-0=H1 instance.  H0 at the new
reference site is used only as an explicit fault-injection control; it is not
a reachable branch and carries no probability interpretation.

Authority: none.  This runner writes nothing and changes no foundation,
registry, queue, policy, selected law, audit state, or git state.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

import aux_gated_candidate_transport_cycle95_2026_07_15 as c95
import four_open_reservation_comb_cycle59_2026_07_14 as c59
import fragment_safe_role_remap_type_integration_cycle108_2026_07_15 as c108
import live_eight_bit_physical_comparator_cycle89_2026_07_15 as c89
import read_status_to_generated_rail_spine_cycle105_2026_07_15 as c105
import zero_binary_source_endpoint_macroblock_bind_cycle100_2026_07_15 as c100
import zero_source_relational_first_harness_cycle101_2026_07_15 as c101


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "FIRST_SELF_GROWN_SELECTOR_PAYLOAD_BIT0_CYCLE106_NOTE_2026-07-15.md"

Coord = c100.Coord
Signature = c100.Signature
H0 = "H0"
H1 = "H1"
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


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def merge_raw(
    *tables: dict[Signature, frozenset[str]],
) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


def transform_site(site: Coord, rotation: c100.c53.Matrix, shift: Coord) -> Coord:
    return add(c100.c53.matvec(rotation, site), shift)


def transform_records(
    records: dict[Coord, str],
    rotation: c100.c53.Matrix,
    shift: Coord,
) -> dict[Coord, str]:
    return {
        transform_site(site, rotation, shift): content
        for site, content in records.items()
    }


# ---------------------------------------------------------------------------
# Exact Cycle-95 first-bit dependency cone.  Coordinates are translated to a
# small standalone cell, but the literal Cycle-95 mixed law is unchanged.
# ---------------------------------------------------------------------------

C95_STATUS: Coord = (0, 0, 0)
C95_DECISION: Coord = (1, 0, 0)
C95_LAUNCH: Coord = (1, -1, 0)

C95_MINI: tuple[tuple[Coord, str, str], ...] = (
    ((0, -1, 0), H1, "candidate"),
    ((0, 1, 0), H0, "reference"),
    ((-1, 0, 0), H1, "previous"),
    ((0, 0, -1), "BACKSTOP", "cage-minus"),
    ((0, 0, 1), "BACKSTOP", "cage-plus"),
    ((1, 1, 0), "T_H0", "decision-y"),
    ((1, 0, 1), "T_H1", "decision-z"),
    ((2, -1, 0), H0, "token-y"),
    ((1, -1, 1), "LAUNCH_A", "token-z"),
)


def c95_enabled(records: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    return {
        target: c95.COMBINED_RAW[local]
        for target in c100.c53.open_candidates(records)
        if (local := c100.c53.local_signature(records, target))
        in c95.COMBINED_RAW
    }


def c95_subset_wins(stage: int) -> tuple[int, tuple[tuple[str, ...], ...]]:
    """Return the minimum source count and every minimum exact subset."""

    for size in range(len(C95_MINI) + 1):
        wins: list[tuple[str, ...]] = []
        for subset in combinations(C95_MINI, size):
            records = {site: content for site, content, _name in subset}
            reference = C95_MINI[1][0]
            if reference not in records:
                continue
            correct = dict(records)
            correct[reference] = H1
            exact_compare = (
                c95_enabled(records) == {C95_STATUS: frozenset((H0,))}
                and c95_enabled(correct) == {C95_STATUS: frozenset((H1,))}
            )
            if not exact_compare:
                continue
            if stage >= 2:
                records[C95_STATUS] = H0
                if c95_enabled(records) != {
                    C95_DECISION: frozenset(("AUX",))
                }:
                    continue
            if stage >= 3:
                records[C95_DECISION] = "AUX"
                if c95_enabled(records) != {
                    C95_LAUNCH: frozenset(("A_0_0",))
                }:
                    continue
            wins.append(tuple(name for _site, _content, name in subset))
        if wins:
            return size, tuple(wins)
    raise AssertionError("finite Cycle-95 subset search found no witness")


# ---------------------------------------------------------------------------
# Cycle-106 grown payload.  TYPE is inherited from Cycle 108's CERT -> R_B21
# row.  Two arm records cage JOIN against corrupt-reader aliases.  A separate
# T_H0 guard cages the reference against the natural R_B21/R_B32 rail pair.
# ---------------------------------------------------------------------------

TYPE: Coord = c108.TYPE_SITE
TYPE_CONTENT = c108.TYPE_CONTENT
TYPE_ARM: Coord = (4, 5, 0)
JOIN_GUARD: Coord = (4, 6, 0)
JOIN: Coord = (4, 6, 1)
CAGE: Coord = (3, 5, 2)
REFERENCE_GUARD: Coord = c101.BIT5_REJECT
REFERENCE: Coord = (2, 6, 2)
STATUS: Coord = (3, 6, 2)
REJECT: Coord = (4, 6, 2)
LAUNCH: Coord = (4, 5, 2)

CORRECT_NEW: tuple[tuple[Coord, str], ...] = (
    (TYPE_ARM, "T_H2"),
    (JOIN_GUARD, "T_H3"),
    (JOIN, "JOINT"),
    (CAGE, "BACKSTOP"),
    (REFERENCE_GUARD, "T_H0"),
    (REFERENCE, H1),
    (STATUS, H1),
)

WRONG_CONTROL: tuple[tuple[Coord, str], ...] = (
    (STATUS, H0),
    (REJECT, "AUX"),
    (LAUNCH, "A_0_0"),
)


def add_canonical(
    table: dict[Signature, str],
    records: dict[Coord, str],
    site: Coord,
    output: str,
) -> None:
    local = c100.c53.local_signature(records, site)
    canonical = c100.c53.canonical_signature(local)
    prior = table.get(canonical)
    if prior is not None and prior != output:
        raise ValueError((canonical, prior, output))
    table[canonical] = output


def build_payload_table() -> dict[Signature, str]:
    table: dict[Signature, str] = {}
    records = dict(c101.TERMINAL)
    records.update(c101.FRAGMENT_OUTPUTS)
    records[TYPE] = TYPE_CONTENT
    for site, output in CORRECT_NEW:
        add_canonical(table, records, site, output)
        records[site] = output

    wrong = dict(c101.TERMINAL)
    wrong.update(c101.FRAGMENT_OUTPUTS)
    wrong.update({TYPE: TYPE_CONTENT})
    wrong.update(dict(CORRECT_NEW[:-1]))
    wrong[REFERENCE] = H0
    for site, output in WRONG_CONTROL:
        add_canonical(table, wrong, site, output)
        wrong[site] = output
    return table


PAYLOAD_TABLE = build_payload_table()
PAYLOAD_RAW = c59.raw_rule_outputs(PAYLOAD_TABLE)
COMBINED_RAW = merge_raw(c108.INTEGRATED_RAW, PAYLOAD_RAW)
C105_UNION_RAW = merge_raw(c105.FULL_RAW, PAYLOAD_RAW)

CORRECT_OUTPUTS: dict[Coord, str] = {
    **c101.FRAGMENT_OUTPUTS,
    TYPE: TYPE_CONTENT,
    **dict(CORRECT_NEW),
}
CORRECT_SITES = frozenset(CORRECT_OUTPUTS)
PAYLOAD_SITES = frozenset((TYPE,)) | frozenset(site for site, _ in CORRECT_NEW) | {
    REJECT,
    LAUNCH,
}
RAIL_SITES = frozenset(site for site, _content in c108.NINE_SLICES[: c108.HORIZON])


def enabled(
    records: dict[Coord, str],
    table: dict[Signature, frozenset[str]] = COMBINED_RAW,
) -> dict[Coord, frozenset[str]]:
    return {
        target: table[local]
        for target in c100.c53.open_candidates(records)
        if (local := c100.c53.local_signature(records, target)) in table
    }


RAIL_ZERO = {
    c108.NINE_SLICES[0][0]: frozenset((c108.NINE_SLICES[0][1],))
}


def without_front(
    actual: dict[Coord, frozenset[str]],
    front: dict[Coord, frozenset[str]],
) -> dict[Coord, frozenset[str]]:
    result = dict(actual)
    for site, values in front.items():
        if result.get(site) == values:
            result.pop(site)
    return result


@dataclass(frozen=True)
class GraphStats:
    states: int
    edges: int
    terminals: int
    terminal_sizes: tuple[int, ...]
    max_front: int
    premature_reject: bool
    bad: tuple[object, ...]


def correct_local_graph() -> GraphStats:
    """All literal-reader, TYPE, arm, reference, and status schedules."""

    queue = deque((frozenset(),))
    seen = {frozenset()}
    edges = 0
    terminals: list[frozenset[Coord]] = []
    max_front = 0
    premature_reject = False
    bad: list[object] = []

    while queue:
        state = queue.popleft()
        records = dict(c101.TERMINAL)
        records.update({site: CORRECT_OUTPUTS[site] for site in state})
        actual = without_front(enabled(records), RAIL_ZERO)
        allowed = {
            site: frozenset((CORRECT_OUTPUTS[site],))
            for site in CORRECT_SITES - state
        }
        wrong = {
            site: values
            for site, values in actual.items()
            if allowed.get(site) != values
        }
        if wrong:
            bad.append((state, wrong))
            break
        if REJECT in actual or LAUNCH in actual:
            premature_reject = True
        max_front = max(max_front, len(actual))
        if state == CORRECT_SITES:
            terminals.append(state)
            continue
        if not actual:
            bad.append((state, "dead"))
            break
        for site in actual:
            future = state | {site}
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)

    return GraphStats(
        states=len(seen),
        edges=edges,
        terminals=len(terminals),
        terminal_sizes=tuple(sorted({len(state) for state in terminals})),
        max_front=max_front,
        premature_reject=premature_reject,
        bad=tuple(bad),
    )


CORRECT_GRAPH = correct_local_graph()


def rail_payload_crossfire() -> tuple[tuple[object, ...], ...]:
    failures: list[tuple[object, ...]] = []
    for prefix in range(c108.HORIZON + 1):
        records = dict(c101.TERMINAL)
        records.update(dict(c108.NINE_SLICES[:prefix]))
        for target in c100.c53.open_candidates(records):
            local = c100.c53.local_signature(records, target)
            if local in PAYLOAD_RAW:
                failures.append((prefix, target, PAYLOAD_RAW[local], local))
    return tuple(failures)


RAIL_CROSSFIRE = rail_payload_crossfire()


def wrong_control_failures() -> tuple[tuple[object, ...], ...]:
    """Inject H0 only after the lawful H1 reference frontier exists."""

    failures: list[tuple[object, ...]] = []
    complete = dict(CORRECT_OUTPUTS)
    for prefix in range(c108.HORIZON + 1):
        records = dict(c101.TERMINAL)
        records.update(complete)
        records.update(dict(c108.NINE_SLICES[:prefix]))
        records[REFERENCE] = H0
        records.pop(STATUS)
        rail_site, rail_content = c108.NINE_SLICES[prefix]
        rail_front = {rail_site: frozenset((rail_content,))}
        stages = (
            (STATUS, H0, {**rail_front, STATUS: frozenset((H0,))}),
            (REJECT, "AUX", {**rail_front, REJECT: frozenset(("AUX",))}),
            (LAUNCH, "A_0_0", {**rail_front, LAUNCH: frozenset(("A_0_0",))}),
        )
        for stage, (site, output, expected) in enumerate(stages):
            actual = enabled(records)
            if actual != expected:
                failures.append((prefix, stage, expected, actual))
                break
            records[site] = output
        if failures:
            break
        if enabled(records) != rail_front:
            failures.append((prefix, 3, rail_front, enabled(records)))
            break
    return tuple(failures)


WRONG_FAILURES = wrong_control_failures()


@dataclass(frozen=True)
class CorruptionStats:
    states: int
    edges: int
    terminals: int
    terminal_sizes: tuple[int, ...]
    candidate_reached: bool
    payload_reached: tuple[Coord, ...]
    bit5_poison: bool
    bad: tuple[object, ...]


def corruption_graph(index: int) -> CorruptionStats:
    source = dict(c101.TERMINAL)
    site = c100.CODE_SITES[index]
    source[site] = H0 if source[site] == H1 else H1
    outputs = dict(CORRECT_OUTPUTS)
    if index == 5:
        # REFERENCE_GUARD is deliberately the inherited bit-5 reject site.
        outputs[c101.BIT5_REJECT] = H1
    allowed_sites = frozenset(outputs)
    queue = deque((frozenset(),))
    seen = {frozenset()}
    edges = 0
    terminals: list[frozenset[Coord]] = []
    reached: set[Coord] = set()
    bad: list[object] = []

    while queue:
        state = queue.popleft()
        records = dict(source)
        records.update({site: outputs[site] for site in state})
        actual = without_front(enabled(records), RAIL_ZERO)
        wrong = {
            target: values
            for target, values in actual.items()
            if target not in allowed_sites
            or values != frozenset((outputs[target],))
        }
        if wrong:
            bad.append((state, wrong))
            break
        reached.update(state)
        if not actual:
            terminals.append(state)
        for target in actual:
            future = state | {target}
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)

    payload_reached = tuple(sorted((PAYLOAD_SITES & reached) - {c101.BIT5_REJECT}))
    return CorruptionStats(
        states=len(seen),
        edges=edges,
        terminals=len(terminals),
        terminal_sizes=tuple(sorted({len(state) for state in terminals})),
        candidate_reached=c101.OUTPUT in reached,
        payload_reached=payload_reached,
        bit5_poison=index == 5 and c101.BIT5_REJECT in reached,
        bad=tuple(bad),
    )


CORRUPTIONS = tuple(corruption_graph(index) for index in range(8))


def wrong_role_scan() -> tuple[
    dict[str, int], tuple[tuple[object, ...], ...], frozenset[str]
]:
    """Immediate typed-fault census at GUARD, REFERENCE, and STATUS."""

    base = dict(c101.TERMINAL)
    base.update(CORRECT_OUTPUTS)
    base.update(dict(c108.NINE_SLICES[: c108.HORIZON]))
    rail_site, rail_content = c108.NINE_SLICES[c108.HORIZON]
    rail_front = {rail_site: frozenset((rail_content,))}
    side_counts: Counter[str] = Counter()
    unsafe: list[tuple[object, ...]] = []

    cases = (
        ("guard", REFERENCE_GUARD, (REFERENCE, STATUS)),
        ("reference", REFERENCE, (STATUS,)),
        ("status", STATUS, ()),
    )
    for label, site, removed in cases:
        for role in sorted(c89.FULL_ROLES):
            records = dict(base)
            for target in removed:
                records.pop(target, None)
            records[site] = role
            actual = enabled(records)
            expected = dict(rail_front)
            if label == "guard" and role == "T_H0":
                expected[REFERENCE] = frozenset((H1,))
            if label == "reference" and role in {H0, H1}:
                expected[STATUS] = frozenset((role,))
            if label == "status" and role == H0:
                expected[REJECT] = frozenset(("AUX",))

            extras = {
                target: values
                for target, values in actual.items()
                if expected.get(target) != values
            }
            if extras:
                side_counts[label] += 1
            illegal_decision = (
                (REJECT in actual and not (label == "status" and role == H0))
                or LAUNCH in actual
                or any(
                    "AUX" in values or "A_0_0" in values
                    for target, values in actual.items()
                    if target not in {REJECT, LAUNCH}
                )
            )
            if illegal_decision:
                unsafe.append((label, role, actual))

    unary_roles = frozenset(
        role
        for role in c89.FULL_ROLES
        if any(
            len(local) == 1 and local[0][1] == role
            for local in c108.INTEGRATED_RAW
        )
    )
    return dict(side_counts), tuple(unsafe), unary_roles


ROLE_SIDE_COUNTS, ROLE_UNSAFE, UNARY_ROLES = wrong_role_scan()


def c95_dependency_contract() -> None:
    section("A - Exact Cycle-95 first-bit source dependency")
    check("A01 Cycle 95's complete apparatus has 943 supplied records",
          len(c95.build_protocol(0).source) == 943)
    minima = tuple(c95_subset_wins(stage) for stage in (1, 2, 3))
    check("A02 exact compare kernel is the unique five-record subset",
          minima[0] == (5, (("candidate", "reference", "previous", "cage-minus", "cage-plus"),)),
          str(minima[0]))
    check("A03 exact AUX certificate is the unique seven-record subset",
          minima[1][0] == 7 and len(minima[1][1]) == 1
          and set(minima[1][1][0]) == {name for _s, _c, name in C95_MINI[:7]},
          str(minima[1]))
    check("A04 exact first launch is the unique nine-record subset",
          minima[2][0] == 9 and len(minima[2][1]) == 1
          and set(minima[2][1][0]) == {name for _s, _c, name in C95_MINI},
          str(minima[2]))
    full = {site: content for site, content, _name in C95_MINI}
    deletion_failures = []
    for deleted in full:
        records = {site: content for site, content in full.items() if site != deleted}
        if c95_enabled(records) != {C95_STATUS: frozenset((H0,))}:
            continue
        records[C95_STATUS] = H0
        if c95_enabled(records) != {C95_DECISION: frozenset(("AUX",))}:
            continue
        records[C95_DECISION] = "AUX"
        if c95_enabled(records) == {C95_LAUNCH: frozenset(("A_0_0",))}:
            deletion_failures.append(deleted)
    check("A05 deleting any one of the nine records breaks the full cone",
          not deletion_failures, str(deletion_failures))
    overlap = set(c95.COMBINED_RAW) & set(c108.INTEGRATED_RAW)
    conflicts = {
        local for local in overlap
        if c95.COMBINED_RAW[local] != c108.INTEGRATED_RAW[local]
    }
    check("A06 Cycle 95's whole law is not silently merged into Cycle 108",
          len(overlap) == 5_240 and len(conflicts) == 6
          and all(local[0][1] == "R_LA" for local in conflicts),
          str((len(overlap), len(conflicts))))


def grown_payload_contract() -> None:
    section("B - Zero-added-source literal bit-0 payload and exact table")
    check("B01 source boundary is exactly the inherited 264-record Cycle-100 terminal",
          c101.TERMINAL == c100.records_at(10) and len(c101.TERMINAL) == 264)
    check("B02 candidate, reference, arm, cage, status, reject, and launch start open",
          set(CORRECT_OUTPUTS) | {REJECT, LAUNCH} > c101.FRAGMENT_SITES
          and (set(CORRECT_OUTPUTS) | {REJECT, LAUNCH}).isdisjoint(c101.TERMINAL))
    check("B03 bit-0 candidate is the grown Cycle-101 H1 output",
          c101.FRAGMENT_OUTPUTS[c101.OUTPUT] == H1
          and c101.OUTPUT in CORRECT_SITES)
    check("B04 TYPE is inherited CERT-to-R_B21 growth, not a new row",
          TYPE == (4, 5, 1) and TYPE_CONTENT == "R_B21"
          and c108.REMAPPED_RAW.get((((-1, 0, 0), "R_B40"),)) == {TYPE_CONTENT})
    check("B05 ten canonical rows compile to 240 disjoint cubic images",
          len(PAYLOAD_TABLE) == 10 and len(PAYLOAD_RAW) == 240
          and set(PAYLOAD_RAW).isdisjoint(c108.INTEGRATED_RAW))
    check("B06 exact union has 7,136 single-valued raw inputs",
          len(COMBINED_RAW) == 7_136
          and all(len(values) == 1 for values in COMBINED_RAW.values()))
    contents = {
        content
        for local, values in COMBINED_RAW.items()
        for _direction, content in local
    } | {output for values in COMBINED_RAW.values() for output in values}
    check("B07 complete table remains inside the 153-role onsite alphabet",
          contents <= c89.FULL_ROLES)
    check("B08 reference guard occupies the inherited bit-5 poison site",
          REFERENCE_GUARD == c101.BIT5_REJECT
          and dict(CORRECT_NEW)[REFERENCE_GUARD] == "T_H0")


def schedule_rail_and_fault_contract() -> None:
    section("C - All correct schedules, eight rail slices, and H0 control")
    check("C01 correct local graph has 982 states and 3,850 edges",
          CORRECT_GRAPH.states == 982 and CORRECT_GRAPH.edges == 3_850,
          str(CORRECT_GRAPH))
    check("C02 every schedule reaches one complete 30-record grown terminal",
          CORRECT_GRAPH.terminals == 1
          and CORRECT_GRAPH.terminal_sizes == (len(CORRECT_SITES),)
          and len(CORRECT_SITES) == 30
          and not CORRECT_GRAPH.bad,
          str(CORRECT_GRAPH))
    check("C03 no correct schedule exposes AUX or launch",
          not CORRECT_GRAPH.premature_reject)
    check("C04 local maximum frontier is seven",
          CORRECT_GRAPH.max_front == 7)
    min_payload_rail = min(
        manhattan(payload, rail)
        for payload in PAYLOAD_SITES
        for rail in RAIL_SITES
    )
    check("C05 payload and eight-slice rail supports are separated by L1 seven",
          min_payload_rail == 7, str(min_payload_rail))
    check("C06 no payload row fires in any of 97 rail prefixes",
          not RAIL_CROSSFIRE, str(RAIL_CROSSFIRE[:1]))
    product_states = CORRECT_GRAPH.states * (c108.HORIZON + 1)
    product_edges = (
        CORRECT_GRAPH.edges * (c108.HORIZON + 1)
        + CORRECT_GRAPH.states * c108.HORIZON
    )
    check("C07 exact separated async product has 95,254 states and 467,722 edges",
          product_states == 95_254 and product_edges == 467_722,
          str((product_states, product_edges)))
    check("C08 H0 fault control is exact at all 97 rail prefixes and four stages",
          not WRONG_FAILURES, str(WRONG_FAILURES[:1]))


def corruption_and_type_contract() -> None:
    section("D - Word corruptions and all live typed substitutions")
    observed = tuple(
        (stats.states, stats.edges, stats.terminal_sizes)
        for stats in CORRUPTIONS
    )
    expected = (
        (38, 70, (14,)),
        (34, 62, (13,)),
        (30, 54, (12,)),
        (22, 34, (11,)),
        (6, 5, (5,)),
        (10, 13, (5,)),
        (4, 3, (3,)),
        (3, 2, (2,)),
    )
    check("D01 all eight one-bit word corruptions retain the exact stopped census",
          observed == expected, str(observed))
    check("D02 no word corruption reaches candidate or any payload record",
          all(not stats.candidate_reached and not stats.payload_reached
              for stats in CORRUPTIONS),
          str(tuple(stats.payload_reached for stats in CORRUPTIONS)))
    check("D03 bit 5 alone writes the inherited poison at the guard coordinate",
          tuple(stats.bit5_poison for stats in CORRUPTIONS)
          == (False, False, False, False, False, True, False, False))
    check("D04 every corruption graph is single-terminal and parasite-free",
          all(stats.terminals == 1 and not stats.bad for stats in CORRUPTIONS))
    check("D05 all 459 GUARD/REFERENCE/STATUS role substitutions are screened",
          len(c89.FULL_ROLES) * 3 == 459
          and ROLE_SIDE_COUNTS == {"reference": 19, "status": 19},
          str(ROLE_SIDE_COUNTS))
    check("D06 the 19 side-front roles are exactly the inherited unary-input roles",
          len(UNARY_ROLES) == 19
          and {"R_B12", "R_B31", "R_B40", "R_LA"} <= UNARY_ROLES)
    check("D07 no typed substitution exposes an illicit AUX or launch",
          not ROLE_UNSAFE, str(ROLE_UNSAFE[:1]))


def covariance_and_scope_contract() -> None:
    section("E - Proper-cubic covariance, scope, and documentation")
    raw_failures = []
    raw_controls = 0
    for local, values in COMBINED_RAW.items():
        for rotation in c100.c53.ROTATIONS:
            raw_controls += 1
            if COMBINED_RAW.get(c100.c53.rotate_signature(local, rotation)) != values:
                raw_failures.append((local, rotation, values))
                break
        if raw_failures:
            break
    check("E01 all 171,264 raw proper-cubic images preserve output",
          raw_controls == 7_136 * 24 and not raw_failures,
          str(raw_failures[:1]))

    correct = dict(c101.TERMINAL)
    correct.update(CORRECT_OUTPUTS)
    correct.update(dict(c108.NINE_SLICES[: c108.HORIZON]))
    wrong = dict(correct)
    wrong[REFERENCE] = H0
    wrong.pop(STATUS)
    stage_records = [dict(correct), dict(wrong)]
    wrong[STATUS] = H0
    stage_records.append(dict(wrong))
    wrong[REJECT] = "AUX"
    stage_records.append(dict(wrong))
    wrong[LAUNCH] = "A_0_0"
    stage_records.append(dict(wrong))
    shift = (83, -61, 47)
    rotation_failures = []
    for rotation in c100.c53.ROTATIONS:
        rail_site = transform_site(c108.NINE_SLICES[c108.HORIZON][0], rotation, shift)
        rail_content = c108.NINE_SLICES[c108.HORIZON][1]
        expected_fronts = (
            {rail_site: frozenset((rail_content,))},
            {
                rail_site: frozenset((rail_content,)),
                transform_site(STATUS, rotation, shift): frozenset((H0,)),
            },
            {
                rail_site: frozenset((rail_content,)),
                transform_site(REJECT, rotation, shift): frozenset(("AUX",)),
            },
            {
                rail_site: frozenset((rail_content,)),
                transform_site(LAUNCH, rotation, shift): frozenset(("A_0_0",)),
            },
            {rail_site: frozenset((rail_content,))},
        )
        for index, (records, expected) in enumerate(zip(stage_records, expected_fronts)):
            actual = enabled(transform_records(records, rotation, shift))
            if actual != expected:
                rotation_failures.append((rotation, index, expected, actual))
                break
        if rotation_failures:
            break
    check("E02 all 24 rotations preserve correct and four H0-control frontiers",
          not rotation_failures, str(rotation_failures[:1]))

    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("E03 note says literal bit-0 instance and types H0 as fault injection",
          "literal bit-0 instance" in note and "fault injection" in note
          and "not a reachable" in note)
    check("E04 note pins inherited boundary versus zero added payload source",
          "264-record inherited generated boundary" in note
          and "zero added payload/harness source records" in note)
    check("E05 note withholds full-selector and probability claims",
          "does not establish a full selector" in note
          and "no probability claim" in note)
    check("E06 note contains the full N1-N8 gate",
          all(f"n{index}" in note for index in range(1, 9)))
    check("E07 note makes no foundation or axiom edit",
          "no foundation edit" in note and "no axiom addition" in note)
    check("E08 Cycle 106 writes only this runner and its review note",
          all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)))


def c105_integration_open_contract() -> None:
    section("F - Literal Cycle-105 integration remains open")
    c105_spine = dict(zip(c105.PRIMARY_SPINE, c105.SPINE_OUTPUTS))
    check("F01 Cycle 105 occupies both Cycle-106 arm coordinates differently",
          c105_spine.get(TYPE_ARM) == "AUX"
          and c105_spine.get(JOIN_GUARD) == "BTG"
          and dict(CORRECT_NEW)[TYPE_ARM] == "T_H2"
          and dict(CORRECT_NEW)[JOIN_GUARD] == "T_H3")
    check("F02 both constructions place the same JOINT at the join coordinate",
          c105.JOIN == JOIN and c105.JOIN_OUTPUT == dict(CORRECT_NEW)[JOIN])
    reject_signature = (((0, 0, -1), "JOINT"),)
    check("F03 Cycle 105's unary JOINT cap targets the Cycle-106 reject site",
          c105.FULL_RAW.get(reject_signature) == {"R_B11"}
          and REJECT in c105.PAYLOAD_SITES)
    check("F04 raw tables merge without hiding the state-level race",
          not (set(c105.FULL_RAW) & set(PAYLOAD_RAW))
          and len(C105_UNION_RAW) == 7_550
          and all(len(values) == 1 for values in C105_UNION_RAW.values()))

    capped = dict(c101.TERMINAL)
    capped.update(c101.FRAGMENT_OUTPUTS)
    capped.update({
        TYPE: TYPE_CONTENT,
        TYPE_ARM: "AUX",
        JOIN_GUARD: "BTG",
        JOIN: "JOINT",
        CAGE: "BACKSTOP",
        REFERENCE_GUARD: "T_H0",
        REFERENCE: H1,
        REJECT: "R_B11",
    })
    capped_status = c100.c53.local_signature(capped, STATUS)
    check("F05 a pre-status C105 cap changes the exact status signature",
          {content for _direction, content in capped_status}
          == {H1, "BACKSTOP", "R_B11"}
          and C105_UNION_RAW.get(capped_status) is None,
          str(capped_status))

    note = NOTE.read_text(encoding="utf-8").lower()
    check("F06 note marks C105_INTEGRATION_OPEN and withholds post-C105 closure",
          "c105_integration_open" in note
          and "does not advance after cycle 105" in note)
    check("F07 note retains a concrete status-gated integration route",
          "joint + status" in note and "status-gated" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    c95_dependency_contract()
    grown_payload_contract()
    schedule_rail_and_fault_contract()
    corruption_and_type_contract()
    covariance_and_scope_contract()
    c105_integration_open_contract()
    print(
        f"\nC95_MINIMA=5/7/9 INHERITED_BOUNDARY={len(c101.TERMINAL)} "
        f"GROWN_CORRECT={len(CORRECT_SITES)} PAYLOAD_CANONICAL={len(PAYLOAD_TABLE)}"
    )
    print(
        f"PAYLOAD_RAW={len(PAYLOAD_RAW)} UNION_RAW={len(COMBINED_RAW)} "
        f"LOCAL_STATES={CORRECT_GRAPH.states} PRODUCT_STATES={CORRECT_GRAPH.states * 97}"
    )
    print("RESULT=FIRST_SELF_GROWN_SELECTOR_PAYLOAD_LITERAL_BIT0_INSTANCE")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
