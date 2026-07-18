#!/usr/bin/env python3
"""Cycle 120: two generated candidates, one formed selector, one literal port.

Cycle 117 grows two distinct neighbouring source records, D0=H1 and D1=H0.
This runner adds a self-caged address race.  The two lawful histories write
different contents at one selector-relay site.  Each selector content enables
only the carrier adjacent to its selected source, and both carriers terminate
at the same physical port, which records the selected literal H value.

All earlier rows remain live.  No record is supplied at the selector, carrier,
or port.  The exact multi-output asynchronous graph is exhausted from Cycle
100's 264-record source.

Authority: none.  No foundation, registry, queue, policy, audit, or git state
is edited or selected by this runner.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from itertools import product
import json
from pathlib import Path

import r_b10_port_to_zero_source_word_completion_cycle117_2026_07_15 as c117


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "CANDIDATE_SELECTED_COMMON_REFERENCE_PORT_CYCLE120_NOTE_2026-07-15.md"

c115 = c117.c115
c112 = c117.c112
c109 = c117.c109
c105 = c117.c105
c101 = c117.c101
c100 = c117.c100
c53 = c117.c53
c59 = c117.c59

Coord = c117.Coord
Signature = c117.Signature
RawTable = c117.RawTable
H0 = c117.H0
H1 = c117.H1
PASS = 0
FAIL = 0

SOURCES = {
    "axioms": ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md",
    "registry": ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json",
    "scale": ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic": ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized": ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "cycle112": REVIEW / "EIGHT_BIT_STATUS_COMPLETION_FRONT_CYCLE112_NOTE_2026-07-15.md",
    "cycle115": REVIEW / "FIRST_AUTONOMOUS_SUCCESSOR_ROLE_PORT_CYCLE115_NOTE_2026-07-15.md",
    "cycle116": REVIEW / "POST_CYCLE115_ADDRESS_SEMANTICS_AUDIT_CYCLE116_NOTE_2026-07-15.md",
    "cycle117": REVIEW / "R_B10_PORT_TO_ZERO_SOURCE_WORD_COMPLETION_CYCLE117_NOTE_2026-07-15.md",
    "cycle118": REVIEW / "FIXED_TWO_VALUE_SERIAL_READ_PATH_CYCLE118_NOTE_2026-07-15.md",
    "primitive_check": ROOT / "docs" / "ai_methodology" / "skills" / "PRIMITIVE_REGISTRY_CHECK.md",
    "no_go": ROOT / "docs" / "ai_methodology" / "skills" / "no-go-discipline" / "SKILL.md",
}


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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def has_all(text: str, needles: tuple[str, ...]) -> bool:
    return all(needle.lower() in text for needle in needles)


def add_canonical(
    table: dict[Signature, str],
    records: dict[Coord, str],
    site: Coord,
    output: str,
) -> None:
    local = c53.local_signature(records, site)
    canonical = c53.canonical_signature(local)
    prior = table.get(canonical)
    if prior is not None and prior != output:
        raise ValueError((site, canonical, prior, output))
    table[canonical] = output


# ---------------------------------------------------------------------------
# Exact relational geometry.
#
# D0 and D1 are generated Cycle-117 data records.  The zero-side guard is a
# three-record contextual lineage.  The one-side guard is one contextual
# record.  ADDRESS_ONE and SELECTOR are adjacent: SELECTOR can record the zero
# token first, blocking ADDRESS_ONE, or ADDRESS_ONE can form first and change
# SELECTOR's exact local signature to the one token.
#
# SELECTOR_GUARD has one forced proper-cubic image.  ADDRESS_ONE blocks that
# image in the one branch; the image forms in the zero branch.  This balances
# both complete histories at ten new records without supplying either one.
# ---------------------------------------------------------------------------

SOURCE_ONE: Coord = c117.DATA_SITES[0]       # (5,2,1)=H1
SOURCE_ZERO: Coord = c117.DATA_SITES[1]      # (5,1,0)=H0

ONE_GUARD: Coord = (5, 2, 2)
ZERO_PRE_GUARD: Coord = (4, -1, 1)
ZERO_MID_GUARD: Coord = (5, -1, 1)
ZERO_GUARD: Coord = (5, 0, 1)
SELECTOR_GUARD: Coord = (6, 0, 1)
SELECTOR_GUARD_IMAGE: Coord = (5, 0, 2)
ADDRESS_ONE: Coord = (5, 1, 2)
SELECTOR: Coord = (5, 1, 1)
SELECTOR_RELAY: Coord = (6, 1, 1)
CARRIER_ONE: Coord = (6, 2, 1)
CARRIER_ZERO: Coord = (6, 1, 0)
COMMON_PORT: Coord = (6, 2, 0)

ONE_GUARD_OUTPUT = "R_C20"
ZERO_PRE_GUARD_OUTPUT = "R_C10"
ZERO_MID_GUARD_OUTPUT = "R_C11"
ZERO_GUARD_OUTPUT = "B1"
SELECTOR_GUARD_OUTPUT = "COMPLETE"
ADDRESS_ONE_OUTPUT = "R_C30"
SELECTOR_ONE_TOKEN = "R_C41"
SELECTOR_ZERO_TOKEN = "R_C40"
SELECTOR_ONE = "R_C01"
SELECTOR_ZERO = "R_C00"
CARRIER_ONE_OUTPUT = "B_1_2"
CARRIER_ZERO_OUTPUT = "B_0_2"
PORT_ONE_OUTPUT = H1
PORT_ZERO_OUTPUT = H0


def build_mux_table() -> dict[Signature, str]:
    terminal = c117.positive_terminal_records()
    table: dict[Signature, str] = {}

    add_canonical(table, terminal, ONE_GUARD, ONE_GUARD_OUTPUT)

    zero_guards = dict(terminal)
    add_canonical(table, zero_guards, ZERO_PRE_GUARD, ZERO_PRE_GUARD_OUTPUT)
    zero_guards[ZERO_PRE_GUARD] = ZERO_PRE_GUARD_OUTPUT
    add_canonical(table, zero_guards, ZERO_MID_GUARD, ZERO_MID_GUARD_OUTPUT)
    zero_guards[ZERO_MID_GUARD] = ZERO_MID_GUARD_OUTPUT
    add_canonical(table, zero_guards, ZERO_GUARD, ZERO_GUARD_OUTPUT)
    zero_guards[ZERO_GUARD] = ZERO_GUARD_OUTPUT
    add_canonical(
        table,
        zero_guards,
        SELECTOR_GUARD,
        SELECTOR_GUARD_OUTPUT,
    )

    one_address = dict(terminal)
    one_address[ONE_GUARD] = ONE_GUARD_OUTPUT
    add_canonical(table, one_address, ADDRESS_ONE, ADDRESS_ONE_OUTPUT)
    one_address[ADDRESS_ONE] = ADDRESS_ONE_OUTPUT
    one_address.update({
        ZERO_PRE_GUARD: ZERO_PRE_GUARD_OUTPUT,
        ZERO_MID_GUARD: ZERO_MID_GUARD_OUTPUT,
        ZERO_GUARD: ZERO_GUARD_OUTPUT,
        SELECTOR_GUARD: SELECTOR_GUARD_OUTPUT,
    })
    add_canonical(table, one_address, SELECTOR, SELECTOR_ONE_TOKEN)

    zero_address = dict(terminal)
    zero_address.update({
        ZERO_PRE_GUARD: ZERO_PRE_GUARD_OUTPUT,
        ZERO_MID_GUARD: ZERO_MID_GUARD_OUTPUT,
        ZERO_GUARD: ZERO_GUARD_OUTPUT,
        SELECTOR_GUARD: SELECTOR_GUARD_OUTPUT,
    })
    add_canonical(table, zero_address, SELECTOR, SELECTOR_ZERO_TOKEN)

    branch_one = dict(terminal)
    branch_one.update({
        ONE_GUARD: ONE_GUARD_OUTPUT,
        ZERO_PRE_GUARD: ZERO_PRE_GUARD_OUTPUT,
        ZERO_MID_GUARD: ZERO_MID_GUARD_OUTPUT,
        ZERO_GUARD: ZERO_GUARD_OUTPUT,
        SELECTOR_GUARD: SELECTOR_GUARD_OUTPUT,
        ADDRESS_ONE: ADDRESS_ONE_OUTPUT,
        SELECTOR: SELECTOR_ONE_TOKEN,
    })
    add_canonical(table, branch_one, SELECTOR_RELAY, SELECTOR_ONE)
    branch_one[SELECTOR_RELAY] = SELECTOR_ONE
    add_canonical(table, branch_one, CARRIER_ONE, CARRIER_ONE_OUTPUT)
    branch_one[CARRIER_ONE] = CARRIER_ONE_OUTPUT
    add_canonical(table, branch_one, COMMON_PORT, PORT_ONE_OUTPUT)

    branch_zero = dict(terminal)
    branch_zero.update({
        ONE_GUARD: ONE_GUARD_OUTPUT,
        ZERO_PRE_GUARD: ZERO_PRE_GUARD_OUTPUT,
        ZERO_MID_GUARD: ZERO_MID_GUARD_OUTPUT,
        ZERO_GUARD: ZERO_GUARD_OUTPUT,
        SELECTOR_GUARD: SELECTOR_GUARD_OUTPUT,
        SELECTOR: SELECTOR_ZERO_TOKEN,
    })
    add_canonical(table, branch_zero, SELECTOR_RELAY, SELECTOR_ZERO)
    branch_zero[SELECTOR_RELAY] = SELECTOR_ZERO
    add_canonical(table, branch_zero, CARRIER_ZERO, CARRIER_ZERO_OUTPUT)
    branch_zero[CARRIER_ZERO] = CARRIER_ZERO_OUTPUT
    add_canonical(table, branch_zero, COMMON_PORT, PORT_ZERO_OUTPUT)
    return table


MUX_TABLE = build_mux_table()
MUX_RAW = c59.raw_rule_outputs(MUX_TABLE)
FULL_RAW = c112.merge_raw(c117.FULL_RAW, MUX_RAW)

EXTENSION_ALLOWED: dict[Coord, frozenset[str]] = {
    ONE_GUARD: frozenset((ONE_GUARD_OUTPUT,)),
    ZERO_PRE_GUARD: frozenset((ZERO_PRE_GUARD_OUTPUT,)),
    ZERO_MID_GUARD: frozenset((ZERO_MID_GUARD_OUTPUT,)),
    ZERO_GUARD: frozenset((ZERO_GUARD_OUTPUT,)),
    SELECTOR_GUARD: frozenset((SELECTOR_GUARD_OUTPUT,)),
    SELECTOR_GUARD_IMAGE: frozenset((SELECTOR_GUARD_OUTPUT,)),
    ADDRESS_ONE: frozenset((ADDRESS_ONE_OUTPUT,)),
    SELECTOR: frozenset((SELECTOR_ZERO_TOKEN, SELECTOR_ONE_TOKEN)),
    SELECTOR_RELAY: frozenset((SELECTOR_ZERO, SELECTOR_ONE)),
    CARRIER_ONE: frozenset((CARRIER_ONE_OUTPUT,)),
    CARRIER_ZERO: frozenset((CARRIER_ZERO_OUTPUT,)),
    COMMON_PORT: frozenset((PORT_ZERO_OUTPUT, PORT_ONE_OUTPUT)),
}


def allowed_with(base: dict[Coord, str]) -> dict[Coord, frozenset[str]]:
    answer = {
        site: frozenset((output,))
        for site, output in base.items()
    }
    answer.update(EXTENSION_ALLOWED)
    return answer


POSITIVE_ALLOWED = allowed_with(c117.GROWN_OUTPUTS)


# ---------------------------------------------------------------------------
# Exact multi-output compiler and asynchronous graph.
# ---------------------------------------------------------------------------

Condition = tuple[int, int, frozenset[str]]


@dataclass(frozen=True)
class MultiGraph:
    states: int
    edges: int
    terminals: tuple[int, ...]
    terminal_sizes: tuple[int, ...]
    max_frontier: int
    bad: tuple[object, ...]
    unexpected: frozenset[Coord]
    violations: tuple[object, ...]
    actions: tuple[tuple[Coord, str], ...]
    action_edges: tuple[int, ...]


def multi_append_graph(
    source: dict[Coord, str],
    allowed: dict[Coord, frozenset[str]],
    raw: RawTable = FULL_RAW,
    ignored: dict[Coord, frozenset[str]] = c112.RAIL_ZERO,
    state_limit: int = 5_000_000,
) -> MultiGraph:
    actions = tuple(sorted(
        (site, output)
        for site, outputs in allowed.items()
        for output in outputs
    ))
    index = {action: position for position, action in enumerate(actions)}
    groups = {
        site: sum(1 << index[(site, output)] for output in outputs)
        for site, outputs in allowed.items()
    }

    universe: set[Coord] = set()
    for site in set(source) | set(allowed):
        for direction in c53.DIRECTIONS:
            universe.add(c53.add(site, direction))
    universe.difference_update(source)

    conditions: dict[Coord, tuple[Condition, ...]] = {}
    for target in universe:
        fixed: list[tuple[Coord, str]] = []
        variable: list[tuple[Coord, tuple[tuple[int, str], ...]]] = []
        for direction in c53.DIRECTIONS:
            neighbour = c53.add(target, direction)
            if neighbour in source:
                fixed.append((direction, source[neighbour]))
            elif neighbour in allowed:
                variable.append((
                    direction,
                    tuple(
                        (index[(neighbour, output)], output)
                        for output in allowed[neighbour]
                    ),
                ))

        neighbourhood_mask = 0
        for _direction, options in variable:
            for action_index, _output in options:
                neighbourhood_mask |= 1 << action_index

        local_conditions: set[Condition] = set()
        choices = [((None, None),) + options for _direction, options in variable]
        for selected in product(*choices):
            parts = list(fixed)
            present_mask = 0
            for (direction, _options), (action_index, output) in zip(variable, selected):
                if action_index is not None:
                    parts.append((direction, output))
                    present_mask |= 1 << action_index
            values = raw.get(tuple(sorted(parts)))
            if values is not None:
                local_conditions.add((present_mask, neighbourhood_mask, values))
        if local_conditions:
            conditions[target] = tuple(local_conditions)

    unexpected = frozenset(set(conditions) - set(allowed) - set(ignored))
    compiled = []
    for target, target_conditions in conditions.items():
        compiled.append((
            target,
            groups.get(target, 0),
            {
                output: index[(target, output)]
                for output in allowed.get(target, ())
            },
            target_conditions,
        ))

    required = {
        "port1": {
            (ONE_GUARD, ONE_GUARD_OUTPUT),
            (ZERO_PRE_GUARD, ZERO_PRE_GUARD_OUTPUT),
            (ZERO_MID_GUARD, ZERO_MID_GUARD_OUTPUT),
            (ZERO_GUARD, ZERO_GUARD_OUTPUT),
            (SELECTOR_GUARD, SELECTOR_GUARD_OUTPUT),
            (ADDRESS_ONE, ADDRESS_ONE_OUTPUT),
            (SELECTOR, SELECTOR_ONE_TOKEN),
            (SELECTOR_RELAY, SELECTOR_ONE),
            (CARRIER_ONE, CARRIER_ONE_OUTPUT),
            (SOURCE_ONE, H1),
        },
        "port0": {
            (ZERO_PRE_GUARD, ZERO_PRE_GUARD_OUTPUT),
            (ZERO_MID_GUARD, ZERO_MID_GUARD_OUTPUT),
            (ZERO_GUARD, ZERO_GUARD_OUTPUT),
            (SELECTOR_GUARD, SELECTOR_GUARD_OUTPUT),
            (SELECTOR, SELECTOR_ZERO_TOKEN),
            (SELECTOR_RELAY, SELECTOR_ZERO),
            (CARRIER_ZERO, CARRIER_ZERO_OUTPUT),
            (SOURCE_ZERO, H0),
        },
    }

    def required_mask(items: set[tuple[Coord, str]]) -> int:
        answer = 0
        for action in items:
            site, output = action
            if source.get(site) == output:
                continue
            answer |= 1 << index[action]
        return answer

    required_masks = {
        key: required_mask(items)
        for key, items in required.items()
    }
    port1_bit = 1 << index[(COMMON_PORT, PORT_ONE_OUTPUT)]
    port0_bit = 1 << index[(COMMON_PORT, PORT_ZERO_OUTPUT)]
    address_one_bit = 1 << index[(ADDRESS_ONE, ADDRESS_ONE_OUTPUT)]

    queue = deque((0,))
    seen = {0}
    edges = 0
    terminals: list[int] = []
    max_frontier = 0
    bad: list[object] = []
    violations: list[object] = []
    action_edges = [0] * len(actions)

    while queue:
        state = queue.popleft()
        if (
            state & port1_bit
            and state & required_masks["port1"] != required_masks["port1"]
        ):
            violations.append(("port1-before-provenance", state))
        if state & port0_bit:
            if state & required_masks["port0"] != required_masks["port0"]:
                violations.append(("port0-before-provenance", state))
            if state & address_one_bit:
                violations.append(("port0-with-address-one", state))

        legal: list[int] = []
        for target, target_group, output_index, target_conditions in compiled:
            if target_group and state & target_group:
                continue
            for present_mask, neighbourhood_mask, values in target_conditions:
                if state & neighbourhood_mask != present_mask:
                    continue
                if target in ignored and values == ignored[target]:
                    break
                if len(values) == 1 and (output := next(iter(values))) in output_index:
                    legal.append(output_index[output])
                    break
                bad.append((state, target, values))
                queue.clear()
                break
            if bad:
                break
        if bad:
            break

        max_frontier = max(max_frontier, len(legal))
        if not legal:
            terminals.append(state)
            continue
        for action_index in legal:
            future = state | 1 << action_index
            edges += 1
            action_edges[action_index] += 1
            if future not in seen:
                seen.add(future)
                if len(seen) > state_limit:
                    bad.append(("state-limit", state_limit))
                    queue.clear()
                    break
                queue.append(future)

    return MultiGraph(
        states=len(seen),
        edges=edges,
        terminals=tuple(terminals),
        terminal_sizes=tuple(sorted({state.bit_count() for state in terminals})),
        max_frontier=max_frontier,
        bad=tuple(bad),
        unexpected=unexpected,
        violations=tuple(violations),
        actions=actions,
        action_edges=tuple(action_edges),
    )


POSITIVE = multi_append_graph(c112.SOURCE, POSITIVE_ALLOWED)


def records_at(
    state: int,
    source: dict[Coord, str] = c112.SOURCE,
    actions: tuple[tuple[Coord, str], ...] = POSITIVE.actions,
) -> dict[Coord, str]:
    records = dict(source)
    for index, (site, output) in enumerate(actions):
        if state >> index & 1:
            prior = records.get(site)
            if prior is not None and prior != output:
                raise RuntimeError((site, prior, output))
            records[site] = output
    return records


def enabled(records: dict[Coord, str], raw: RawTable = FULL_RAW) -> dict[Coord, frozenset[str]]:
    return {
        target: raw[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in raw
    }


def terminal_class(state: int) -> tuple[str | None, str | None]:
    records = records_at(state)
    return records.get(SELECTOR_RELAY), records.get(COMMON_PORT)


def append_rail(records: dict[Coord, str]) -> tuple[dict[Coord, str], tuple[object, ...]]:
    answer = dict(records)
    failures: list[object] = []
    for prefix, (site, output) in enumerate(
        c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]
    ):
        actual = enabled(answer)
        expected = {site: frozenset((output,))}
        if actual != expected:
            failures.append((prefix, expected, actual))
            break
        answer[site] = output
    if not failures and enabled(answer) != {
        c105.NEXT_RAIL[0]: frozenset((c105.NEXT_RAIL[1],))
    }:
        failures.append((c105.RAIL_HORIZON, enabled(answer)))
    return answer, tuple(failures)


# ---------------------------------------------------------------------------
# Contracts.
# ---------------------------------------------------------------------------

def source_and_primitive_contract() -> None:
    section("A - Exact predecessor and primitive scopes")
    for name, path in {"cycle120_note": NOTE, **SOURCES}.items():
        check(f"A {name} exists", path.is_file(), str(path))

    registry = json.loads(SOURCES["registry"].read_text(encoding="utf-8"))
    nodes = registry["nodes"]
    check(
        "A registered primitive paths are consumed literally",
        ROOT / nodes["scale_reference_primitive"]["current_path"] == SOURCES["scale"]
        and ROOT / nodes["kinetic_isotropy_primitive"]["current_path"] == SOURCES["kinetic"]
        and ROOT / nodes["realized_state_primitive"]["current_path"] == SOURCES["realized"],
    )
    texts = {key: normalized(path) for key, path in SOURCES.items()}
    check(
        "A scale primitive is units-only and supplies no selector/readout bridge",
        has_all(texts["scale"], ("units conversion", "no mass ratio", "selector", "readout bridge")),
    )
    check(
        "A kinetic primitive is c_t=c_s form-only and supplies no selector/readout",
        has_all(texts["kinetic"], ("c_t = c_s", "no mass ratio", "selector", "readout bridge")),
    )
    check(
        "A realized-state primitive is pointwise-only and supplies no selection/weight",
        has_all(texts["realized"], ("pointwise", "not a state-selection rule", "no averaging", "probability rule")),
    )
    check(
        "A Cycle116 and Cycle118 name the exact I3 residual",
        "candidate_selected_common_reference_port" in texts["cycle116"]
        and "i3: candidate-selected value at one common logical port" in texts["cycle118"],
    )
    check(
        "A predecessors retain exact green finite surfaces",
        c112.POSITIVE.states == 73_656
        and c115.POSITIVE.states == 74_264
        and c117.POSITIVE.states == 76_056
        and not c112.POSITIVE.bad
        and not c115.POSITIVE.bad
        and not c117.POSITIVE.bad,
    )


def table_and_geometry_contract() -> None:
    section("B - Two generated candidates, self-caged selector, common port")
    terminal = c117.positive_terminal_records()
    check(
        "B D0=H1 and D1=H0 are distinct generated records, not supplied source",
        SOURCE_ONE == c117.DATA_SITES[0]
        and SOURCE_ZERO == c117.DATA_SITES[1]
        and c117.GROWN_OUTPUTS[SOURCE_ONE] == H1
        and c117.GROWN_OUTPUTS[SOURCE_ZERO] == H0
        and {SOURCE_ONE, SOURCE_ZERO}.isdisjoint(c112.SOURCE),
    )
    check(
        "B extension preserves every predecessor and source record",
        set(EXTENSION_ALLOWED).isdisjoint(c117.GROWN_OUTPUTS)
        and set(EXTENSION_ALLOWED).isdisjoint(c112.SOURCE),
    )
    check(
        "B table is 14 canonical / 318 raw rows disjoint from Cycle117",
        len(MUX_TABLE) == 14
        and len(MUX_RAW) == 318
        and set(MUX_RAW).isdisjoint(c117.FULL_RAW),
        f"canonical={len(MUX_TABLE)} raw={len(MUX_RAW)}",
    )
    check(
        "B complete 8,630-row union is single-valued and alphabet-closed",
        len(FULL_RAW) == 8_630
        and all(len(values) == 1 for values in FULL_RAW.values())
        and {
            content
            for local, values in FULL_RAW.items()
            for content in [
                *(value for _direction, value in local),
                *values,
            ]
        } <= c105.c89.FULL_ROLES,
    )

    zero_guard_records = dict(terminal)
    zero_guard_records.update({
        ZERO_PRE_GUARD: ZERO_PRE_GUARD_OUTPUT,
        ZERO_MID_GUARD: ZERO_MID_GUARD_OUTPUT,
        ZERO_GUARD: ZERO_GUARD_OUTPUT,
    })
    forced_guard_images = {
        target
        for target, values in enabled(zero_guard_records, MUX_RAW).items()
        if values == frozenset((SELECTOR_GUARD_OUTPUT,))
    }
    check(
        "B B1 self-cage has exactly two lawful COMPLETE images",
        forced_guard_images == {SELECTOR_GUARD, SELECTOR_GUARD_IMAGE},
        str(forced_guard_images),
    )

    one_records = dict(terminal)
    one_records.update({
        ONE_GUARD: ONE_GUARD_OUTPUT,
        ZERO_PRE_GUARD: ZERO_PRE_GUARD_OUTPUT,
        ZERO_MID_GUARD: ZERO_MID_GUARD_OUTPUT,
        ZERO_GUARD: ZERO_GUARD_OUTPUT,
        SELECTOR_GUARD: SELECTOR_GUARD_OUTPUT,
        ADDRESS_ONE: ADDRESS_ONE_OUTPUT,
        SELECTOR: SELECTOR_ONE_TOKEN,
    })
    zero_records = dict(terminal)
    zero_records.update({
        ZERO_PRE_GUARD: ZERO_PRE_GUARD_OUTPUT,
        ZERO_MID_GUARD: ZERO_MID_GUARD_OUTPUT,
        ZERO_GUARD: ZERO_GUARD_OUTPUT,
        SELECTOR_GUARD: SELECTOR_GUARD_OUTPUT,
        SELECTOR: SELECTOR_ZERO_TOKEN,
    })
    one_selector_local = c53.local_signature(one_records, SELECTOR_RELAY)
    zero_selector_local = c53.local_signature(zero_records, SELECTOR_RELAY)
    check(
        "B one literal selector relay accepts either branch token plus COMPLETE cage",
        one_selector_local
        == (((-1, 0, 0), SELECTOR_ONE_TOKEN), ((0, -1, 0), SELECTOR_GUARD_OUTPUT))
        and zero_selector_local
        == (((-1, 0, 0), SELECTOR_ZERO_TOKEN), ((0, -1, 0), SELECTOR_GUARD_OUTPUT)),
        f"one={one_selector_local} zero={zero_selector_local}",
    )
    check(
        "B selector contents are distinct and port coordinate is literally common",
        SELECTOR_ONE != SELECTOR_ZERO
        and PORT_ONE_OUTPUT != PORT_ZERO_OUTPUT
        and len(EXTENSION_ALLOWED[COMMON_PORT]) == 2,
    )

    one_records[SELECTOR_RELAY] = SELECTOR_ONE
    zero_records[SELECTOR_RELAY] = SELECTOR_ZERO
    one_carrier_local = c53.local_signature(one_records, CARRIER_ONE)
    zero_carrier_local = c53.local_signature(zero_records, CARRIER_ZERO)
    check(
        "B each selected carrier consumes selector content plus its own source value",
        one_carrier_local
        == (((-1, 0, 0), H1), ((0, -1, 0), SELECTOR_ONE))
        and zero_carrier_local
        == (((-1, 0, 0), H0), ((0, 0, 1), SELECTOR_ZERO)),
        f"one={one_carrier_local} zero={zero_carrier_local}",
    )
    one_records[CARRIER_ONE] = CARRIER_ONE_OUTPUT
    zero_records[CARRIER_ZERO] = CARRIER_ZERO_OUTPUT
    one_port_local = c53.local_signature(one_records, COMMON_PORT)
    zero_port_local = c53.local_signature(zero_records, COMMON_PORT)
    check(
        "B both carriers decode at one exact port to literal selected H1/H0",
        one_port_local
        == (((-1, 0, 0), "TZ"), ((0, 0, 1), CARRIER_ONE_OUTPUT))
        and zero_port_local
        == (((-1, 0, 0), "TZ"), ((0, -1, 0), CARRIER_ZERO_OUTPUT))
        and FULL_RAW[one_port_local] == frozenset((H1,))
        and FULL_RAW[zero_port_local] == frozenset((H0,)),
        f"one={one_port_local} zero={zero_port_local}",
    )


def graph_contract() -> None:
    section("C - Every asynchronous history and selector provenance")
    check(
        "C action corpus is 82 inherited plus 15 alternative-aware actions",
        len(c117.GROWN_OUTPUTS) == 82
        and len(POSITIVE.actions) == 97,
        f"actions={len(POSITIVE.actions)}",
    )
    check(
        "C compiler finds zero unexpected target and zero bad transition",
        not POSITIVE.unexpected and not POSITIVE.bad,
        f"unexpected={POSITIVE.unexpected} bad={POSITIVE.bad[:1]}",
    )
    check(
        "C exact graph is 133,270 states / 790,154 edges / two 92-write terminals",
        POSITIVE.states == 133_270
        and POSITIVE.edges == 790_154
        and len(POSITIVE.terminals) == 2
        and POSITIVE.terminal_sizes == (92,)
        and POSITIVE.max_frontier == 11,
        f"states={POSITIVE.states} edges={POSITIVE.edges} terminals={len(POSITIVE.terminals)} sizes={POSITIVE.terminal_sizes}",
    )
    check(
        "C no reachable port precedes selector, carrier, source, or guard provenance",
        not POSITIVE.violations,
        str(POSITIVE.violations[:1]),
    )
    classes = Counter(terminal_class(state) for state in POSITIVE.terminals)
    check(
        "C terminal classes are exactly selector-zero/H0 and selector-one/H1",
        classes == {(SELECTOR_ZERO, H0): 1, (SELECTOR_ONE, H1): 1},
        str(classes),
    )

    terminals = [records_at(state) for state in POSITIVE.terminals]
    zero_terminal = next(records for records in terminals if records[COMMON_PORT] == H0)
    one_terminal = next(records for records in terminals if records[COMMON_PORT] == H1)
    check(
        "C zero branch contains guard image and excludes one-address record",
        zero_terminal.get(SELECTOR_GUARD_IMAGE) == SELECTOR_GUARD_OUTPUT
        and ADDRESS_ONE not in zero_terminal,
    )
    check(
        "C one branch contains one-address record and blocks guard image",
        one_terminal.get(ADDRESS_ONE) == ADDRESS_ONE_OUTPUT
        and SELECTOR_GUARD_IMAGE not in one_terminal,
    )
    check(
        "C both candidate source records survive unchanged in both terminals",
        all(
            records[SOURCE_ONE] == H1 and records[SOURCE_ZERO] == H0
            for records in terminals
        ),
    )
    check(
        "C both complete branches expose only the inherited repaired-rail front",
        all(enabled(records) == c112.RAIL_ZERO for records in terminals),
        str([enabled(records) for records in terminals]),
    )


def rail_and_covariance_contract() -> None:
    section("D - Rail product, late rail, and proper-cubic covariance")
    terminal_records = [records_at(state) for state in POSITIVE.terminals]
    rail_failures = []
    rail_completed = []
    for branch, records in enumerate(terminal_records):
        completed, failures = append_rail(records)
        rail_completed.append(completed)
        if failures:
            rail_failures.append((branch, failures[0]))
    check(
        "D both selector branches retain all 96 exact singleton rail appends",
        not rail_failures,
        str(rail_failures[:1]),
    )

    rail_only = dict(c112.SOURCE)
    alias_hits = []
    for prefix in range(c105.RAIL_HORIZON + 1):
        for target in c53.open_candidates(rail_only):
            local = c53.local_signature(rail_only, target)
            if local in MUX_RAW and local not in c117.FULL_RAW:
                alias_hits.append((prefix, target, local))
        if prefix < c105.RAIL_HORIZON:
            site, output = c105.RAIL_SEQUENCE[prefix]
            rail_only[site] = output
    rail_sites = {
        site for site, _output in c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]
    }
    distance = min(
        c101.manhattan(left, right)
        for left in EXTENSION_ALLOWED
        for right in rail_sites
    )
    check(
        "D mux support is distance seven from rail with zero 97-prefix aliases",
        distance == 7 and not alias_hits,
        f"distance={distance} aliases={alias_hits[:1]}",
    )

    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = (
        POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + POSITIVE.states * c105.RAIL_HORIZON
    )
    check(
        "D exact rail locality product is 12,927,190 states / 89,438,858 edges",
        product_states == 12_927_190 and product_edges == 89_438_858,
        f"states={product_states} edges={product_edges}",
    )

    long_rail = c105.c108.c104.rail_sequence(102, c105.ROLE_MAP)
    late_failures = []
    late_sizes = []
    for branch, records in enumerate(terminal_records):
        late = dict(records)
        for prefix, (site, output) in enumerate(long_rail[: 101 * 12]):
            actual = enabled(late)
            expected = {site: frozenset((output,))}
            if actual != expected:
                late_failures.append((branch, prefix, expected, actual))
                break
            late[site] = output
        late_sizes.append(len(late))
        if not late_failures:
            next_site, next_output = long_rail[101 * 12]
            if enabled(late) != {next_site: frozenset((next_output,))}:
                late_failures.append((branch, "next", enabled(late)))
    check(
        "D both branches grow 101 complete late slices / 1,212 records",
        not late_failures and late_sizes == [1_568, 1_568],
        f"sizes={late_sizes} failures={late_failures[:1]}",
    )

    covariance_failures = []
    controls = 0
    for local, values in FULL_RAW.items():
        for rotation in c53.ROTATIONS:
            controls += 1
            actual = FULL_RAW.get(c53.rotate_signature(local, rotation))
            if actual != values:
                covariance_failures.append((local, rotation, values, actual))
                break
    check(
        "D all 207,120 full-law proper-cubic images preserve output",
        controls == len(FULL_RAW) * 24 == 207_120
        and not covariance_failures,
        str(covariance_failures[:1]),
    )

    shift = (211, -127, 103)
    rotated_failures = []
    rotated_controls = 0
    for branch, records in enumerate(terminal_records):
        for rotation in c53.ROTATIONS:
            rotated_controls += 1
            transformed = c105.transform_records(records, rotation, shift)
            next_site = c101.transform_site(c105.FIRST_RAIL[0], rotation, shift)
            expected = {next_site: frozenset((c105.FIRST_RAIL[1],))}
            actual = enabled(transformed)
            if actual != expected:
                rotated_failures.append((branch, rotation, expected, actual))
                break
    check(
        "D all 48 rotated branch terminals expose only the rotated rail front",
        rotated_controls == 48 and not rotated_failures,
        str(rotated_failures[:1]),
    )


def corruption_contract() -> None:
    section("E - Wrong word, VALID/READY, and typed-H0 controls")
    expected = [
        (1_350, 4_578, 1, (31,), 6),
        (1_150, 3_822, 1, (30,), 6),
        (950, 3_066, 1, (29,), 6),
        (650, 1_882, 1, (28,), 5),
        (150, 317, 1, (21,), 3),
        (250, 645, 1, (21,), 4),
        (100, 203, 1, (19,), 3),
        (75, 146, 1, (18,), 3),
        (50, 89, 1, (17,), 3),
        (25, 32, 1, (16,), 2),
    ]
    observed = []
    failures = []

    def inspect(label: str, graph: MultiGraph) -> None:
        observed.append((
            graph.states,
            graph.edges,
            len(graph.terminals),
            graph.terminal_sizes,
            graph.max_frontier,
        ))
        action_index = {action: index for index, action in enumerate(graph.actions)}
        port_actions = [
            action_index[(COMMON_PORT, output)]
            for output in (H0, H1)
        ]
        port_terminal = any(
            any(state >> index & 1 for index in port_actions)
            for state in graph.terminals
        )
        if (
            graph.bad
            or graph.unexpected
            or graph.violations
            or port_terminal
        ):
            failures.append((label, graph, port_terminal))

    for index, site in enumerate(c100.CODE_SITES):
        source = dict(c112.SOURCE)
        source[site] = H0 if source[site] == H1 else H1
        outputs = dict(c117.GROWN_OUTPUTS)
        if index == 5:
            outputs[c101.BIT5_REJECT] = H1
        inspect(
            f"bit-{index}",
            multi_append_graph(source, allowed_with(outputs)),
        )

    for label, site in (("valid", c100.VALID), ("ready", c100.READY)):
        source = dict(c112.SOURCE)
        source[site] = H0
        inspect(
            label,
            multi_append_graph(source, POSITIVE_ALLOWED),
        )

    check(
        "E all eight one-bit flips plus wrong VALID/READY reach no common port",
        not failures,
        str(failures[:1]),
    )
    check(
        "E all ten corrupted multi-graphs retain their exact census",
        observed == expected,
        str(observed),
    )

    fault_source = c109.fault_records(3)
    fault_outputs = {
        site: output
        for site, output in {
            **c112.EXTENSION_OUTPUTS,
            **c115.SUCCESSOR_OUTPUTS,
            **c117.EXTENSION_OUTPUTS,
        }.items()
        if site not in fault_source
    }
    fault_outputs[c112.GUARD_SPINE[1]] = H1
    fault_outputs[c112.GUARD_SPINE[2]] = H1
    fault = multi_append_graph(
        fault_source,
        allowed_with(fault_outputs),
    )
    fault_index = {action: index for index, action in enumerate(fault.actions)}
    fault_has_port = any(
        any(
            state >> fault_index[(COMMON_PORT, output)] & 1
            for output in (H0, H1)
        )
        for state in fault.terminals
    )
    check(
        "E typed-H0 alternate exhausts to two partial terminals and no port",
        fault.states == 88
        and fault.edges == 238
        and len(fault.terminals) == 2
        and fault.terminal_sizes == (7, 8)
        and fault.max_frontier == 5
        and not fault.bad
        and not fault.unexpected
        and not fault.violations
        and not fault_has_port,
        f"states={fault.states} edges={fault.edges} sizes={fault.terminal_sizes} bad={fault.bad[:1]}",
    )


def note_and_scope_contract() -> None:
    section("F - Bounded meaning, constitutional firewall, and N1-N8")
    note = normalized(NOTE)
    check(
        "F note names exact I3 closure and one literal common port",
        has_all(note, (
            "candidate_selected_common_reference_port",
            "one literal common port",
            "selector-zero/h0",
            "selector-one/h1",
        )),
    )
    check(
        "F note states schedule-realized selector and conditional confluence",
        has_all(note, (
            "schedule-realized",
            "conditional on the formed selector",
            "does not supply an occurrence probability",
        )),
    )
    check(
        "F note preserves source-first read chronology and rejects later locking",
        has_all(note, (
            "source records form and lock first",
            "reading neither forms nor finishes locking",
        )),
    )
    check(
        "F note leaves 236-bank, external setting, law selection, and rates open",
        has_all(note, (
            "236-program association",
            "externally settable",
            "exact-law selection",
            "rate",
        )),
    )
    check(
        "F constitutional delta is zero and no axiom addition follows",
        has_all(note, (
            "constitutional delta is zero",
            "no axiom addition follows",
            "candidate exact-law content",
        )),
    )
    check(
        "F all N1-N8 no-go-discipline sections are visible",
        all(f"n{index}" in note for index in range(1, 9))
        and "status: pass for the bounded positive" in note,
    )


def main() -> int:
    source_and_primitive_contract()
    table_and_geometry_contract()
    graph_contract()
    rail_and_covariance_contract()
    corruption_contract()
    note_and_scope_contract()

    section("Summary")
    print(f"PASS={PASS} FAIL={FAIL}")
    print(f"MUX_CANONICAL={len(MUX_TABLE)} MUX_RAW={len(MUX_RAW)} FULL_RAW={len(FULL_RAW)}")
    print(f"STATES={POSITIVE.states} EDGES={POSITIVE.edges} TERMINALS={len(POSITIVE.terminals)}")
    print("TERMINAL_CLASSES=R_C00:H0,R_C01:H1")
    print("CLOSED=CANDIDATE_SELECTED_COMMON_REFERENCE_PORT")
    print("PORT=(6,2,0) SOURCE_ZERO=(5,1,0) SOURCE_ONE=(5,2,1)")
    print("CONSTITUTIONAL_DELTA=ZERO")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
