#!/usr/bin/env python3
"""Cycle 114: lawful H0 reference fork from the generated R_B11 word.

The Cycle-100 terminal already contains five lawfully generated H0 word bits.
This runner searches those records and the landed candidate-law surfaces for a
zero-new-supplied path into Cycle 109's comparator.  The selected path adds
three canonical rows:

1. copy stored bit 2 H0 into one unique open local context;
2. if that copy precedes the original T_H0 guard, grow an H0 guard; and
3. grow H0 at Cycle 109's reference site.

The landed Cycle-109 mismatch/status, AUX, and A_0_0 rows then complete the
reject branch.  If the original guard precedes the copy, the existing H1 path
is unchanged.  Exhaustion therefore produces two lawful terminal histories
without source mutation or external H0 injection.

This is a bounded availability construction.  It does not select the branch,
assign a probability to it, build an addressable all-bit stream, or provide
occurrence/fairness/rate semantics.

Authority: none.  No predecessor, foundation, registry, queue, audit, policy,
or git state is edited or selected by this runner.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
sys.path.insert(0, str(SCRIPTS))

import status_gated_typed_payload_handoff_cycle109_2026_07_15 as c109  # noqa: E402


c105 = c109.c105
c101 = c105.c101
c100 = c101.c100
c106 = c109.c106
c53 = c100.c53
c59 = c109.c59

NOTE = REVIEW / "LAWFUL_H0_REFERENCE_FORK_CYCLE114_NOTE_2026-07-15.md"

SOURCES = {
    "axioms": ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md",
    "registry": ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json",
    "scale": ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic": ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "realized": ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "cycle100": REVIEW / "ZERO_BINARY_SOURCE_ENDPOINT_MACROBLOCK_BIND_CYCLE100_NOTE_2026-07-15.md",
    "cycle101": REVIEW / "ZERO_SOURCE_RELATIONAL_FIRST_HARNESS_CYCLE101_NOTE_2026-07-15.md",
    "cycle109": REVIEW / "STATUS_GATED_TYPED_PAYLOAD_HANDOFF_CYCLE109_NOTE_2026-07-15.md",
    "cycle111": REVIEW / "POST_CYCLE109_STRICT_COMPILER_CONSTITUTIONAL_DELTA_CYCLE111_NOTE_2026-07-15.md",
}

Coord = tuple[int, int, int]
Signature = c100.Signature
RawTable = c105.RawTable
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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def has_all(text: str, needles: tuple[str, ...]) -> bool:
    return all(needle.lower() in text for needle in needles)


def merge_raw(*tables: RawTable) -> RawTable:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


def add_canonical(
    table: dict[Signature, str],
    records: dict[Coord, str],
    target: Coord,
    output: str,
) -> None:
    local = c53.local_signature(records, target)
    canonical = c53.canonical_signature(local)
    prior = table.get(canonical)
    if prior is not None and prior != output:
        raise ValueError((canonical, prior, output))
    table[canonical] = output


def enabled(records: dict[Coord, str], raw: RawTable) -> dict[Coord, frozenset[str]]:
    return {
        target: raw[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in raw
    }


# The exact post-C105 common record corpus: all reader/shell/JOIN records are
# present and Cycle 105's three symmetric cap images are removed, exactly as in
# Cycle 109's integration substitution.
COMMON_RECORDS = c105.positive_terminal_records()
for _payload_site in c105.PAYLOAD_SITES:
    COMMON_RECORDS.pop(_payload_site)


# ---------------------------------------------------------------------------
# Route A: smallest standalone lawful H0 copy.  This proves physical H0
# availability from the generated word, but is five L1 steps from the C109
# reference and therefore does not by itself close the comparator route.
# ---------------------------------------------------------------------------

STANDALONE_SOURCE_BIT = c100.CODE_SITES[1]
STANDALONE_COPY: Coord = (1, 5, -1)
STANDALONE_TABLE: dict[Signature, str] = {}
add_canonical(STANDALONE_TABLE, c101.TERMINAL, STANDALONE_COPY, H0)
STANDALONE_RAW = c59.raw_rule_outputs(STANDALONE_TABLE)
STANDALONE_UNION = merge_raw(c109.FULL_RAW, STANDALONE_RAW)


# ---------------------------------------------------------------------------
# Route B: selected three-row fork into the actual C109 reference.
#
# The copy is enabled by stored code bit 2 H0 only after the relational reader,
# certificate, and local cage records exist.  It is adjacent to the original
# reference-guard site.  Whichever of COPY and the original T_H0 guard forms
# first permanently changes the other's local signature:
#
#   original guard first -> existing H1 reference/status/payload terminal;
#   copy first           -> H0 guard/reference/status/AUX/A_0_0 terminal.
#
# The CAGE and COPY commute; the H0 guard requires both.  The status/reject
# portion is reused literally from Cycle 109.
# ---------------------------------------------------------------------------

FORK_SOURCE_BIT = c100.CODE_SITES[2]
FORK_COPY: Coord = (2, 5, 1)


def build_fork_table() -> dict[Signature, str]:
    records = dict(COMMON_RECORDS)
    table: dict[Signature, str] = {}

    add_canonical(table, records, FORK_COPY, H0)
    records[FORK_COPY] = H0

    # C109's existing cage can form before or after FORK_COPY and is retained.
    records[c106.CAGE] = "BACKSTOP"
    add_canonical(table, records, c106.REFERENCE_GUARD, H0)
    records[c106.REFERENCE_GUARD] = H0

    add_canonical(table, records, c106.REFERENCE, H0)
    return table


FORK_TABLE = build_fork_table()
FORK_RAW = c59.raw_rule_outputs(FORK_TABLE)
FULL_RAW = merge_raw(c109.FULL_RAW, FORK_RAW)


# Route C control: directly changing the landed C109 guard output would be a
# table conflict, not a second history.  It is enumerated explicitly below.
GUARD_RECORDS = dict(COMMON_RECORDS)
GUARD_RECORDS[c106.CAGE] = "BACKSTOP"
ORIGINAL_GUARD_LOCAL = c53.local_signature(GUARD_RECORDS, c106.REFERENCE_GUARD)
ORIGINAL_GUARD_CANONICAL = c53.canonical_signature(ORIGINAL_GUARD_LOCAL)
DIRECT_GUARD_H0_RAW = c59.raw_rule_outputs({ORIGINAL_GUARD_CANONICAL: H0})
DIRECT_GUARD_CONFLICTS = {
    local: (c109.FULL_RAW[local], DIRECT_GUARD_H0_RAW[local])
    for local in set(c109.FULL_RAW) & set(DIRECT_GUARD_H0_RAW)
    if c109.FULL_RAW[local] != DIRECT_GUARD_H0_RAW[local]
}


def allowed_outputs(*, bit5_reject: bool = False) -> dict[Coord, frozenset[str]]:
    outputs: dict[Coord, set[str]] = {
        site: {output}
        for site, output in c109.GROWN_OUTPUTS.items()
    }
    for site in (
        c106.REFERENCE_GUARD,
        c106.REFERENCE,
        c106.STATUS,
        c109.DIRECTED_PAYLOAD,
    ):
        outputs.pop(site, None)
    outputs[FORK_COPY] = {H0}
    outputs[c106.REFERENCE_GUARD] = {"T_H0", H0}
    outputs[c106.REFERENCE] = {H1, H0}
    outputs[c106.STATUS] = {H1, H0}
    outputs[c109.DIRECTED_PAYLOAD] = {"R_B11", "AUX"}
    outputs[c109.LAUNCH] = {c109.LAUNCH_OUTPUT}
    if bit5_reject:
        outputs[c101.BIT5_REJECT] = {H1}
    return {site: frozenset(values) for site, values in outputs.items()}


State = frozenset[tuple[Coord, str]]


def records_at(state: State, source: dict[Coord, str] | None = None) -> dict[Coord, str]:
    records = dict(c101.TERMINAL if source is None else source)
    for site, output in state:
        prior = records.get(site)
        if prior is not None and prior != output:
            raise ValueError((site, prior, output))
        records[site] = output
    return records


@dataclass(frozen=True)
class GraphStats:
    states: int
    edges: int
    terminals: tuple[State, ...]
    terminal_sizes: tuple[int, ...]
    max_frontier: int
    bad: tuple[object, ...]
    reached: frozenset[tuple[Coord, str]]


def append_graph(
    source: dict[Coord, str] | None = None,
    *,
    bit5_reject: bool = False,
    raw: RawTable = FULL_RAW,
    allowed: dict[Coord, frozenset[str]] | None = None,
) -> GraphStats:
    choices = allowed_outputs(bit5_reject=bit5_reject) if allowed is None else allowed
    start: State = frozenset()
    queue = deque((start,))
    seen = {start}
    edges = 0
    terminals: list[State] = []
    max_frontier = 0
    bad: list[object] = []
    reached: set[tuple[Coord, str]] = set()

    while queue:
        state = queue.popleft()
        records = records_at(state, source)
        actual = enabled(records, raw)
        legal: list[tuple[Coord, str]] = []
        local_bad: list[object] = []
        for target, values in actual.items():
            if target == c105.FIRST_RAIL[0] and values == c109.RAIL_ZERO[target]:
                continue
            if (
                target in choices
                and len(values) == 1
                and next(iter(values)) in choices[target]
                and target not in records
            ):
                legal.append((target, next(iter(values))))
            else:
                local_bad.append((state, target, values, records.get(target)))
        if local_bad:
            bad.extend(local_bad)
            break
        max_frontier = max(max_frontier, len(legal))
        if not legal:
            terminals.append(state)
            continue
        for addition in legal:
            future = state | {addition}
            edges += 1
            reached.add(addition)
            if future not in seen:
                seen.add(future)
                queue.append(future)

    return GraphStats(
        states=len(seen),
        edges=edges,
        terminals=tuple(terminals),
        terminal_sizes=tuple(sorted(state.__len__() for state in terminals)),
        max_frontier=max_frontier,
        bad=tuple(bad),
        reached=frozenset(reached),
    )


POSITIVE = append_graph()


def terminal_records() -> tuple[dict[Coord, str], ...]:
    return tuple(records_at(state) for state in POSITIVE.terminals)


def branch_label(records: dict[Coord, str]) -> str:
    values = (
        records.get(FORK_COPY),
        records.get(c106.REFERENCE_GUARD),
        records.get(c106.REFERENCE),
        records.get(c106.STATUS),
        records.get(c109.DIRECTED_PAYLOAD),
        records.get(c109.LAUNCH),
    )
    if values == (None, "T_H0", H1, H1, "R_B11", None):
        return "H1_PAYLOAD"
    if values == (H0, H0, H0, H0, "AUX", c109.LAUNCH_OUTPUT):
        return "H0_REJECT"
    return "UNKNOWN"


def standalone_graph() -> GraphStats:
    outputs = {
        site: frozenset((output,))
        for site, output in c109.GROWN_OUTPUTS.items()
    }
    outputs[STANDALONE_COPY] = frozenset((H0,))
    return append_graph(raw=STANDALONE_UNION, allowed=outputs)


STANDALONE_POSITIVE = standalone_graph()


def h0_neighbor_candidates(records: dict[Coord, str]) -> tuple[tuple[object, ...], ...]:
    opens = c53.open_candidates(records)
    classes: dict[Signature, list[Coord]] = defaultdict(list)
    for target in opens:
        local = c53.local_signature(records, target)
        classes[c53.canonical_signature(local)].append(target)
    answer: list[tuple[object, ...]] = []
    h0_sites = {site for site, output in c101.TERMINAL.items() if output == H0}
    for source in h0_sites:
        for direction in c53.DIRECTIONS:
            target = tuple(source[index] + direction[index] for index in range(3))
            if target not in opens:
                continue
            local = c53.local_signature(records, target)
            canonical = c53.canonical_signature(local)
            answer.append((source, target, len(classes[canonical]), local))
    return tuple(sorted(answer, key=lambda row: (row[1], row[0])))


def missing_h0_status_sites(records: dict[Coord, str]) -> tuple[tuple[Coord, Coord], ...]:
    """Find rotated C109 mismatch-status motifs missing only their H0 neighbour."""

    fault = c109.fault_records(0)
    status_canonical = c53.canonical_signature(
        c53.local_signature(fault, c106.STATUS)
    )
    templates = {
        c53.rotate_signature(status_canonical, rotation)
        for rotation in c53.ROTATIONS
    }
    answer: set[tuple[Coord, Coord]] = set()
    for target in c53.open_candidates(records):
        local = dict(c53.local_signature(records, target))
        for template in templates:
            missing_direction = next(
                direction for direction, output in template if output == H0
            )
            required = {
                direction: output
                for direction, output in template
                if output != H0
            }
            if not all(local.get(direction) == output for direction, output in required.items()):
                continue
            if missing_direction in local:
                continue
            missing_site = tuple(
                target[index] + missing_direction[index]
                for index in range(3)
            )
            if missing_site not in records:
                answer.add((target, missing_site))
    return tuple(sorted(answer))


def source_and_primitive_contract() -> None:
    section("A - Sources, method, and primitive boundary")
    for name, path in {"cycle114_note": NOTE, **SOURCES}.items():
        check(f"A {name} exists", path.is_file(), str(path))

    registry = json.loads(SOURCES["registry"].read_text(encoding="utf-8"))
    nodes = registry["nodes"]
    check(
        "A registry contains only the four canonical premise nodes",
        set(nodes) == {
            "minimal_axioms", "scale_reference_primitive",
            "kinetic_isotropy_primitive", "realized_state_primitive",
        },
        str(sorted(nodes)),
    )
    texts = {key: normalized(path) for key, path in SOURCES.items()}
    check(
        "A primitive scopes remain units-only, form-only, and pointwise-only",
        has_all(texts["scale"], ("units conversion, not a physics axiom", "zero dimensionless content"))
        and has_all(texts["kinetic"], ("c_t = c_s", "not a new dynamics", "not a re-axiomatization of time"))
        and has_all(texts["realized"], ("pointwise evaluation", "no state, averaging over alternatives", "past hypothesis is a separate")),
    )
    check(
        "A Cycle111 names the exact input blocker and next object",
        has_all(texts["cycle111"], (
            "lawful_alternate_h0_reference_generation",
            "second_valid_literal_history_to_lawful_h0_reference",
        )),
    )
    check(
        "A current Record provides no branch selector, schedule, rate, or probability",
        has_all(texts["axioms"], ("records form", "formation rules (which admissible possibility"))
        and "probability rule" in normalized(SOURCES["registry"]),
    )


def corpus_and_route_census_contract() -> None:
    section("B - Exact H0 corpus and three requested route families")
    source_h0 = {site for site, output in c100.SOURCE.items() if output == H0}
    terminal_h0 = {site for site, output in c101.TERMINAL.items() if output == H0}
    word_h0 = {
        site for site in c100.CODE_SITES if c101.TERMINAL[site] == H0
    }
    check(
        "B C100 source has four H0 records and its terminal has nine",
        len(source_h0) == 4 and len(terminal_h0) == 9,
        f"source={sorted(source_h0)} terminal={sorted(terminal_h0)}",
    )
    check(
        "B generated R_B11=10010100 contributes exactly five H0 word records",
        c100.R_B11_WORD == (1, 0, 0, 1, 0, 1, 0, 0)
        and len(word_h0) == 5
        and word_h0 == {c100.CODE_SITES[index] for index in (1, 2, 4, 6, 7)},
        str(sorted(word_h0)),
    )
    check(
        "B all five word H0 records are generated appends, not new Cycle114 source",
        all((site, H0) in c100.ADDITIONS for site in word_h0)
        and set(FORK_TABLE).isdisjoint(c109.FULL_RAW),
    )

    h0_raw = [
        local for local, values in c109.FULL_RAW.items()
        if values == frozenset((H0,))
    ]
    check(
        "B landed C109 law has 192 H0-output raw rows in eight canonical classes",
        len(h0_raw) == 192
        and len({c53.canonical_signature(local) for local in h0_raw}) == 8,
    )
    check(
        "B no landed C109 row grows H0 at the lawful reference prefix",
        c109.FULL_RAW.get(
            c53.local_signature(
                {**COMMON_RECORDS, c106.CAGE: "BACKSTOP", c106.REFERENCE_GUARD: H0},
                c106.REFERENCE,
            )
        ) is None,
    )

    candidates = h0_neighbor_candidates(COMMON_RECORDS)
    check(
        "B seven open neighbours of existing H0 records have unique complete local classes",
        len(candidates) == 7 and all(row[2] == 1 for row in candidates),
        str(tuple((row[0], row[1], row[2]) for row in candidates)),
    )
    check(
        "B standalone bit1 copy is one canonical / 24 raw rows and conflict-free",
        c101.TERMINAL[STANDALONE_SOURCE_BIT] == H0
        and len(STANDALONE_TABLE) == 1
        and len(STANDALONE_RAW) == 24
        and set(STANDALONE_RAW).isdisjoint(c109.FULL_RAW)
        and len(STANDALONE_UNION) == 7_520,
    )
    check(
        "B standalone copy proves H0 existence but remains L1 distance five from C109 reference",
        c101.manhattan(STANDALONE_COPY, c106.REFERENCE) == 5,
    )

    check(
        "B C100 constructs only the one R_B11 VALID/READY word on this endpoint",
        tuple(output for _site, output in c100.ADDITIONS[:8])
        == tuple(H1 if bit else H0 for bit in c100.R_B11_WORD)
        and c100.ADDITIONS[8:] == ((c100.VALID, H1), (c100.READY, H1)),
    )
    mutation_failures = []
    for index, (site, output) in enumerate(c100.ADDITIONS[:8]):
        records = c100.records_at(index + 1)
        records[site] = H0 if output == H1 else H1
        if c100.enabled(records):
            mutation_failures.append((index, c100.enabled(records)))
    check(
        "B every one-bit mutation stops and is not relabelled a second valid encoded history",
        not mutation_failures,
        str(mutation_failures),
    )


def table_and_minimum_route_contract() -> None:
    section("C - Three-row lawful fork and rejected shortcuts")
    copy_local = c53.local_signature(COMMON_RECORDS, FORK_COPY)
    check(
        "C fork copy sees stored bit2 H0 in a unique five-neighbour context",
        c101.TERMINAL[FORK_SOURCE_BIT] == H0
        and dict(copy_local) == {
            (-1, 0, 0): H0,
            (0, -1, 0): "R_A01",
            (0, 0, -1): H1,
            (0, 1, 0): "R_B32",
            (1, 0, 0): "R_B40",
        },
        str(copy_local),
    )
    check(
        "C selected route is three canonical / 72 raw rows",
        len(FORK_TABLE) == 3 and len(FORK_RAW) == 72,
    )
    check(
        "C fork rows are disjoint from C109 and form a 7,568-row single-valued union",
        set(FORK_RAW).isdisjoint(c109.FULL_RAW)
        and len(FULL_RAW) == 7_568
        and all(len(values) == 1 for values in FULL_RAW.values()),
    )
    check(
        "C all row inputs and outputs remain in the 153-role onsite alphabet",
        {
            content
            for local, values in FULL_RAW.items()
            for content in [*(value for _direction, value in local), *values]
        } <= c105.c89.FULL_ROLES,
    )

    copied = dict(COMMON_RECORDS)
    copied[FORK_COPY] = H0
    copied[c106.CAGE] = "BACKSTOP"
    guard_local = c53.local_signature(copied, c106.REFERENCE_GUARD)
    check(
        "C copied H0 plus landed CAGE changes the guard into a lawful H0 row",
        dict(guard_local) == {
            (-1, 0, 0): H1,
            (0, -1, 0): H0,
            (0, 0, -1): H0,
            (1, 0, 0): "BACKSTOP",
        }
        and FULL_RAW[guard_local] == frozenset((H0,)),
        str(guard_local),
    )
    copied[c106.REFERENCE_GUARD] = H0
    reference_local = c53.local_signature(copied, c106.REFERENCE)
    check(
        "C H0 guard grows H0 at the exact C109 reference site",
        dict(reference_local) == {
            (-1, 0, 0): "R_B21",
            (0, -1, 0): H0,
            (0, 0, -1): "R_B32",
        }
        and FULL_RAW[reference_local] == frozenset((H0,)),
        str(reference_local),
    )

    check(
        "C direct T_H0-to-H0 guard addition has 24 literal output conflicts",
        c109.HARNESS_TABLE[ORIGINAL_GUARD_CANONICAL] == "T_H0"
        and len(DIRECT_GUARD_CONFLICTS) == 24
        and all(
            left == frozenset(("T_H0",)) and right == frozenset((H0,))
            for left, right in DIRECT_GUARD_CONFLICTS.values()
        ),
        str(tuple(DIRECT_GUARD_CONFLICTS.items())[:1]),
    )

    status_prefix = dict(COMMON_RECORDS)
    status_prefix[c106.CAGE] = "BACKSTOP"
    check(
        "C translated-motif search leaves only C109 STATUS missing its exact REFERENCE",
        missing_h0_status_sites(status_prefix) == ((c106.STATUS, c106.REFERENCE),),
        str(missing_h0_status_sites(status_prefix)),
    )
    nearest_h0_distance = min(
        c101.manhattan(site, c106.REFERENCE)
        for site, output in c101.TERMINAL.items()
        if output == H0
    )
    check(
        "C nearest inherited H0 is two local steps from REFERENCE",
        nearest_h0_distance == 2
        and c101.TERMINAL[(2, 4, 2)] == H0,
    )


def branch_graph_contract() -> None:
    section("D - Exhaustive two-history append graph")
    check(
        "D branch graph is 17,880 states / 88,642 edges with zero bad fronts",
        POSITIVE.states == 17_880
        and POSITIVE.edges == 88_642
        and not POSITIVE.bad,
        str(POSITIVE),
    )
    check(
        "D every schedule reaches exactly one of two terminals of sizes 46 and 48",
        len(POSITIVE.terminals) == 2
        and POSITIVE.terminal_sizes == (46, 48)
        and POSITIVE.max_frontier == 10,
        str(POSITIVE.terminal_sizes),
    )
    terminals = terminal_records()
    labels = Counter(branch_label(records) for records in terminals)
    check(
        "D terminals are exactly one unchanged H1 payload and one lawful H0 reject history",
        labels == {"H1_PAYLOAD": 1, "H0_REJECT": 1},
        str(labels),
    )
    h0_terminal = next(records for records in terminals if branch_label(records) == "H0_REJECT")
    check(
        "D H0 terminal contains copied bit, H0 guard/reference/status, AUX, and A_0_0",
        h0_terminal[FORK_COPY] == H0
        and h0_terminal[c106.REFERENCE_GUARD] == H0
        and h0_terminal[c106.REFERENCE] == H0
        and h0_terminal[c106.STATUS] == H0
        and h0_terminal[c109.DIRECTED_PAYLOAD] == "AUX"
        and h0_terminal[c109.LAUNCH] == c109.LAUNCH_OUTPUT,
    )
    check(
        "D H0 path uses no source mutation and no injected reference value",
        c101.TERMINAL[FORK_SOURCE_BIT] == H0
        and c106.REFERENCE not in c101.TERMINAL
        and all(c101.TERMINAL.get(site) is None for site in (FORK_COPY, c106.REFERENCE_GUARD, c106.REFERENCE)),
    )

    check(
        "D one-row standalone H0 copy is an exact independent positive",
        STANDALONE_POSITIVE.states == 22_640
        and STANDALONE_POSITIVE.edges == 119_452
        and len(STANDALONE_POSITIVE.terminals) == 1
        and STANDALONE_POSITIVE.terminal_sizes == (47,)
        and not STANDALONE_POSITIVE.bad,
        str(STANDALONE_POSITIVE),
    )


def rail_covariance_and_corruption_contract() -> None:
    section("E - Rail product, covariance, and corrupted-word controls")
    standalone_terminal = records_at(STANDALONE_POSITIVE.terminals[0])
    standalone_rail = dict(standalone_terminal)
    standalone_failures = []
    for prefix, (site, content) in enumerate(c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]):
        actual = enabled(standalone_rail, STANDALONE_UNION)
        expected = {site: frozenset((content,))}
        if actual != expected:
            standalone_failures.append((prefix, expected, actual))
            break
        standalone_rail[site] = content
    check(
        "E standalone copy retains all 96 exact singleton rail appends",
        not standalone_failures
        and enabled(standalone_rail, STANDALONE_UNION) == {
            c105.NEXT_RAIL[0]: frozenset((c105.NEXT_RAIL[1],))
        },
        str(standalone_failures[:1]),
    )
    standalone_product_states = STANDALONE_POSITIVE.states * (c105.RAIL_HORIZON + 1)
    standalone_product_edges = (
        STANDALONE_POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + STANDALONE_POSITIVE.states * c105.RAIL_HORIZON
    )
    check(
        "E standalone copy x 97-prefix product is 2,196,080 states / 13,760,284 edges",
        standalone_product_states == 2_196_080
        and standalone_product_edges == 13_760_284,
        f"states={standalone_product_states} edges={standalone_product_edges}",
    )

    rail_failures = []
    for label, terminal in ((branch_label(records), records) for records in terminal_records()):
        records = dict(terminal)
        for prefix, (site, content) in enumerate(c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]):
            actual = enabled(records, FULL_RAW)
            expected = {site: frozenset((content,))}
            if actual != expected:
                rail_failures.append((label, prefix, expected, actual))
                break
            records[site] = content
        if not rail_failures and enabled(records, FULL_RAW) != {
            c105.NEXT_RAIL[0]: frozenset((c105.NEXT_RAIL[1],))
        }:
            rail_failures.append((label, c105.RAIL_HORIZON, "next", enabled(records, FULL_RAW)))
    check(
        "E both lawful terminals retain all 96 exact singleton rail appends",
        not rail_failures,
        str(rail_failures[:1]),
    )

    added_sites = {FORK_COPY, c106.REFERENCE_GUARD, c106.REFERENCE}
    rail_sites = {
        site for site, _content in c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]
    }
    min_distance = min(
        c101.manhattan(left, right)
        for left in added_sites
        for right in rail_sites
    )
    new_rail_hits = []
    rail_records = dict(c101.TERMINAL)
    for prefix in range(c105.RAIL_HORIZON + 1):
        for target in c53.open_candidates(rail_records):
            local = c53.local_signature(rail_records, target)
            if local in FORK_RAW:
                new_rail_hits.append((prefix, target, local))
        if prefix < c105.RAIL_HORIZON:
            site, content = c105.RAIL_SEQUENCE[prefix]
            rail_records[site] = content
    check(
        "E fork support is rail-separated and no new row aliases a rail prefix",
        min_distance >= 6 and not new_rail_hits,
        f"distance={min_distance} hits={new_rail_hits[:1]}",
    )
    standalone_distance = min(
        c101.manhattan(STANDALONE_COPY, site)
        for site in rail_sites
    )
    standalone_hits = []
    rail_records = dict(c101.TERMINAL)
    for prefix in range(c105.RAIL_HORIZON + 1):
        for target in c53.open_candidates(rail_records):
            local = c53.local_signature(rail_records, target)
            if local in STANDALONE_RAW:
                standalone_hits.append((prefix, target, local))
        if prefix < c105.RAIL_HORIZON:
            site, content = c105.RAIL_SEQUENCE[prefix]
            rail_records[site] = content
    intended_standalone_local = c53.local_signature(
        c101.TERMINAL,
        STANDALONE_COPY,
    )
    intended_standalone_hits = [
        (prefix, STANDALONE_COPY, intended_standalone_local)
        for prefix in range(c105.RAIL_HORIZON + 1)
    ]
    check(
        "E standalone row stays confined to its intended target across rail prefixes",
        standalone_distance >= 6
        and standalone_hits == intended_standalone_hits,
        f"distance={standalone_distance} hits={len(standalone_hits)}",
    )
    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = (
        POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + POSITIVE.states * c105.RAIL_HORIZON
    )
    check(
        "E exact two-history x 97-prefix product is 1,734,360 states / 10,314,754 edges",
        product_states == 1_734_360 and product_edges == 10_314_754,
        f"states={product_states} edges={product_edges}",
    )

    covariance_failures = []
    controls = 0
    for local, values in FULL_RAW.items():
        for rotation in c53.ROTATIONS:
            controls += 1
            if FULL_RAW.get(c53.rotate_signature(local, rotation)) != values:
                covariance_failures.append((local, rotation))
                break
    check(
        "E all 181,632 raw proper-cubic images preserve output",
        controls == len(FULL_RAW) * 24 == 181_632 and not covariance_failures,
        str(covariance_failures[:1]),
    )
    standalone_covariance_failures = []
    standalone_controls = 0
    for local, values in STANDALONE_UNION.items():
        for rotation in c53.ROTATIONS:
            standalone_controls += 1
            if STANDALONE_UNION.get(c53.rotate_signature(local, rotation)) != values:
                standalone_covariance_failures.append((local, rotation))
                break
    check(
        "E all 180,480 standalone-union proper-cubic images preserve output",
        standalone_controls == len(STANDALONE_UNION) * 24 == 180_480
        and not standalone_covariance_failures,
        str(standalone_covariance_failures[:1]),
    )

    rotated_failures = []
    shift = (163, -109, 83)
    complete_cases = [("STANDALONE", standalone_rail)]
    for records in terminal_records():
        complete = dict(records)
        complete.update(dict(c105.RAIL_SEQUENCE[: c105.RAIL_HORIZON]))
        complete_cases.append((branch_label(records), complete))
    for label, records in complete_cases:
        raw = STANDALONE_UNION if label == "STANDALONE" else FULL_RAW
        for rotation in c53.ROTATIONS:
            transformed = c105.transform_records(records, rotation, shift)
            expected_site = c101.transform_site(c105.NEXT_RAIL[0], rotation, shift)
            actual = enabled(transformed, raw)
            expected = {expected_site: frozenset((c105.NEXT_RAIL[1],))}
            if actual != expected:
                rotated_failures.append((label, rotation, expected, actual))
                break
    check(
        "E standalone/H1/H0 completed histories rotate to only the next rail frontier",
        len(complete_cases) == 3 and not rotated_failures,
        str(rotated_failures[:1]),
    )

    corruption_failures = []
    observed = []
    for index, site in enumerate(c100.CODE_SITES):
        source = dict(c101.TERMINAL)
        source[site] = H0 if source[site] == H1 else H1
        stats = append_graph(source, bit5_reject=index == 5)
        observed.append((stats.states, stats.edges, stats.terminal_sizes))
        if (
            len(stats.terminals) != 1
            or stats.bad
            or (c106.STATUS, H0) in stats.reached
            or (c106.STATUS, H1) in stats.reached
            or any(site_value[0] == c109.DIRECTED_PAYLOAD for site_value in stats.reached)
        ):
            corruption_failures.append((index, stats))
    for label, site in (("VALID", c100.VALID), ("READY", c100.READY)):
        source = dict(c101.TERMINAL)
        source[site] = H0
        stats = append_graph(source)
        observed.append((stats.states, stats.edges, stats.terminal_sizes))
        if (
            len(stats.terminals) != 1
            or stats.bad
            or any(site_value[0] in {c106.STATUS, c109.DIRECTED_PAYLOAD} for site_value in stats.reached)
        ):
            corruption_failures.append((label, stats))
    check(
        "E all eight word flips plus wrong VALID/READY stop before comparator outcome",
        not corruption_failures and len(observed) == 10,
        str(corruption_failures[:1]),
    )
    check(
        "E corrupted graph census is executable and pinned",
        observed == [
            (760, 2_274, (29,)),
            (680, 2_022, (28,)),
            (600, 1_770, (27,)),
            (440, 1_186, (26,)),
            (120, 238, (20,)),
            (200, 490, (20,)),
            (80, 152, (18,)),
            (60, 109, (17,)),
            (40, 66, (16,)),
            (20, 23, (15,)),
        ],
        str(observed),
    )


def note_scope_and_no_go_contract() -> None:
    section("F - Note, unlanded Cycle112 boundary, and N1-N8 discipline")
    note = normalized(NOTE) if NOTE.is_file() else ""
    raw = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    check(
        "F note has authority none and runner+note-only scope",
        has_all(note, (
            "authority: none", "runner + review note only", "no predecessor edit",
            "no foundation edit", "no registry edit", "no queue edit", "no commit",
        )),
    )
    check(
        "F note states the exact positive closure and honest next residual",
        has_all(note, (
            "second_valid_literal_history_to_lawful_h0_reference",
            "closed at bounded availability grade",
            "addressable_two_valued_reference_stream",
            "schedule race",
        )),
    )
    check(
        "F note distinguishes standalone one-row existence from comparator closure",
        has_all(note, (
            "standalone_copy", "one canonical / 24 raw",
            "five l1 steps", "three canonical / 72 raw",
        )),
    )
    check(
        "F note records exact graph, product, and branch counts",
        has_all(note, (
            "17,880", "88,642", "46", "48",
            "1,734,360", "10,314,754", "181,632",
        )),
    )
    check(
        "F note excludes mutation, fault injection, branch weight, and axiom effects",
        has_all(note, (
            "no post-front mutation", "no external fault injection",
            "no branch probability", "no axiom addition follows",
        )),
    )
    check(
        "F note preserves exact primitive scopes",
        has_all(note, (
            "units only", "c_t=c_s form only",
            "pointwise realized-state reference only",
        )),
    )
    check(
        "F note records Cycle112 as unlanded and unconsumed",
        has_all(note, ("cycle 112", "unlanded", "not consumed")),
    )
    check(
        "F note carries complete N1-N8 and at least five attempted routes",
        all(f"n{index} —" in note for index in range(1, 9))
        and raw.count("`ATTEMPTED`") >= 5,
    )
    check(
        "F residual negative is explicitly partial rather than universal",
        has_all(note, (
            "partial-narrowing-with-live-constructive-routes",
            "not a universal no-go", "strongest hostile steelman",
        )),
    )
    scientific_body = note.split("## n1–n8 no-go-discipline gate", 1)[0]
    hidden = (
        "we assume", "as is standard", "the framework provides", "bridge context",
        "obviously", "naturally follows", "standard qft",
    )
    check(
        "F scientific body contains no hidden-premise phrase",
        not any(phrase in scientific_body for phrase in hidden),
        str([phrase for phrase in hidden if phrase in scientific_body]),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    source_and_primitive_contract()
    corpus_and_route_census_contract()
    table_and_minimum_route_contract()
    branch_graph_contract()
    rail_covariance_and_corruption_contract()
    note_scope_and_no_go_contract()
    product_states = POSITIVE.states * (c105.RAIL_HORIZON + 1)
    product_edges = (
        POSITIVE.edges * (c105.RAIL_HORIZON + 1)
        + POSITIVE.states * c105.RAIL_HORIZON
    )
    print(
        f"\nSTANDALONE_CANONICAL={len(STANDALONE_TABLE)} STANDALONE_RAW={len(STANDALONE_RAW)} "
        f"FORK_CANONICAL={len(FORK_TABLE)} FORK_RAW={len(FORK_RAW)} UNION_RAW={len(FULL_RAW)}"
    )
    print(
        f"LOCAL_STATES={POSITIVE.states} LOCAL_EDGES={POSITIVE.edges} TERMINALS={len(POSITIVE.terminals)} "
        f"PRODUCT_STATES={product_states} PRODUCT_EDGES={product_edges}"
    )
    print("CLOSED=SECOND_VALID_LITERAL_HISTORY_TO_LAWFUL_H0_REFERENCE")
    print("NEXT=ADDRESSABLE_TWO_VALUED_REFERENCE_STREAM")
    print("CYCLE112=UNLANDED_NOT_CONSUMED")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
