#!/usr/bin/env python3
"""Cycle 101: zero-source relational first-harness fragment.

The exact Cycle-100 terminal is the only record boundary.  A typed relational
surface sweep reads READY, VALID, and all eight literal R_B11 bits; two finite
proper-cubic caps turn the sweep without choosing an axis externally.  The
sweep then grows one literal-dependent reference, one compare certificate, and
one output bit.  No candidate, reference, comparator, writer, cage, or rail
record is supplied.

The already-generated Cycle-52 A slice is also recognized in the endpoint.
Its first B slice grows concurrently under the full mixed table.  The two
fronts are exhausted as one asynchronous product; a causal join between the
read status and that reusable rail remains open.

Authority: none.  No foundation, queue, audit, or git state follows.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import self_extending_frame_cage_rail_cycle52_2026_07_14 as c52
import zero_binary_source_endpoint_macroblock_bind_cycle100_2026_07_15 as c100


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "ZERO_SOURCE_RELATIONAL_FIRST_HARNESS_CYCLE101_NOTE_2026-07-15.md"

Coord = tuple[int, int, int]
Signature = c100.Signature
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
H0 = "H0"
H1 = "H1"
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


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def transform_site(site: Coord, rotation: Matrix, shift: Coord) -> Coord:
    return add(c100.c53.matvec(rotation, site), shift)


def transform_records(
    records: dict[Coord, str], rotation: Matrix, shift: Coord
) -> dict[Coord, str]:
    return {
        transform_site(site, rotation, shift): content
        for site, content in records.items()
    }


def merge_raw(
    *tables: dict[Signature, frozenset[str]],
) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


TERMINAL = c100.records_at(len(c100.ADDITIONS))


# ---------------------------------------------------------------------------
# Compact relational surface reader.
#
# Each group is one concurrent generation.  The two multi-site caps are not a
# host-selected fanout: proper-cubic covariance makes every listed image live.
# Unique existing 153-role contents retain phase/address without a new carrier.
# ---------------------------------------------------------------------------

Group = tuple[tuple[Coord, str], ...]

FRAGMENT_GROUPS: tuple[Group, ...] = (
    (((3, 3, 3), "R_B00"),),                  # READY tap
    (((3, 4, 3), "R_B01"),),                  # VALID tap
    (((2, 4, 3), "R_B02"),),                  # bit 7
    (((1, 4, 3), "R_B10"),),                  # bit 6
    (((1, 5, 3), "R_B11"),),                  # bit 5
    (((0, 5, 3), "R_B12"),),                  # bit 4
    (                                           # three-image corner cap
        ((-1, 5, 3), "R_B13"),
        ((0, 6, 3), "R_B13"),
        ((0, 5, 4), "R_B13"),
    ),
    (((0, 6, 2), "R_B20"),),                  # bit-4 transverse bind
    (                                           # caged equal H1 pair
        ((0, 6, 1), "R_B21"),                  # bit 3
        ((1, 6, 2), "R_B21"),                  # bit 5 control image
    ),
    (((1, 6, 1), "R_B23"),),                  # bit 2
    (((1, 6, 0), "R_B30"),),                  # bit 1
    (((2, 6, 0), "R_B31"),),                  # bit 0
    (                                           # four-site comparator cage
        ((3, 6, 0), "R_B32"),
        ((2, 7, 0), "R_B32"),
        ((2, 6, 1), "R_B32"),
        ((2, 6, -1), "R_B32"),
    ),
    (((3, 5, 0), "R_B33"),),                  # literal-dependent reference
    (((3, 5, 1), "R_B40"),),                  # compare/write certificate
    (((3, 6, 1), H1),),                        # first physical output bit
)

FRAGMENT_OUTPUTS: dict[Coord, str] = {
    site: content
    for group in FRAGMENT_GROUPS
    for site, content in group
}
FRAGMENT_SITES = frozenset(FRAGMENT_OUTPUTS)
REFERENCE: Coord = (3, 5, 0)
CERTIFICATE: Coord = (3, 5, 1)
OUTPUT: Coord = (3, 6, 1)
BIT5_REJECT: Coord = (2, 5, 2)


def build_fragment_table() -> tuple[dict[Signature, str], dict[Coord, frozenset[Coord]]]:
    records = dict(TERMINAL)
    table: dict[Signature, str] = {}
    consumed_terminal: dict[Coord, set[Coord]] = defaultdict(set)
    for group in FRAGMENT_GROUPS:
        assert set(site for site, _content in group).isdisjoint(records)
        staged: list[tuple[Signature, str]] = []
        for target, output in group:
            local = c100.c53.local_signature(records, target)
            canonical = c100.c53.canonical_signature(local)
            prior = table.get(canonical)
            if prior is not None and prior != output:
                raise ValueError((canonical, prior, output))
            staged.append((canonical, output))
            for direction, _content in local:
                neighbor = add(target, direction)
                if neighbor in TERMINAL:
                    consumed_terminal[neighbor].add(target)
        for canonical, output in staged:
            table[canonical] = output
        records.update(dict(group))
    return table, {
        site: frozenset(targets)
        for site, targets in consumed_terminal.items()
    }


FRAGMENT_TABLE, CONSUMED_TERMINAL = build_fragment_table()
FRAGMENT_RAW = c59.raw_rule_outputs(FRAGMENT_TABLE)
BASE_RAW = merge_raw(c100.COMBINED_RAW, c52.RULE_OUTPUTS)
COMBINED_RAW = merge_raw(BASE_RAW, FRAGMENT_RAW)
FRAGMENT_ONLY_RAW = merge_raw(c100.COMBINED_RAW, FRAGMENT_RAW)


def enabled(
    records: dict[Coord, str],
    table: dict[Signature, frozenset[str]] = COMBINED_RAW,
) -> dict[Coord, frozenset[str]]:
    return {
        target: table[local]
        for target in c100.c53.open_candidates(records)
        if (local := c100.c53.local_signature(records, target)) in table
    }


# ---------------------------------------------------------------------------
# The generated endpoint already contains a proper-cubic image of Cycle 52's
# complete A slice and BACKSTOP.  Its first B slice is a zero-source reusable
# frame front.  Freeze after that slice while retaining the exact next C seed.
# ---------------------------------------------------------------------------

RAIL_ROTATION: Matrix = ((-1, 0, 0), (0, 0, 1), (0, 1, 0))
RAIL_SHIFT: Coord = (-1, 0, 0)


def rail_transform(site: Coord) -> Coord:
    return transform_site(site, RAIL_ROTATION, RAIL_SHIFT)


RAIL_SEED = transform_records(c52.seed_records(), RAIL_ROTATION, RAIL_SHIFT)
RAIL_TWO_LAYERS = tuple(
    (rail_transform(site), content)
    for site, content in c52.bounded_sequence(2)
)
RAIL_B = RAIL_TWO_LAYERS[:12]
NEXT_C = RAIL_TWO_LAYERS[12]
RAIL_B_OUTPUTS = dict(RAIL_B)
RAIL_B_SITES = frozenset(RAIL_B_OUTPUTS)


@dataclass(frozen=True)
class GraphStats:
    states: int
    edges: int
    terminals: int
    terminal_sizes: tuple[int, ...]
    output_reached: bool
    reject_terminal: bool
    bad: tuple[object, ...]


def fragment_graph(
    source: dict[Coord, str],
    *,
    allow_bit5_reject: bool = False,
) -> GraphStats:
    outputs = dict(FRAGMENT_OUTPUTS)
    if allow_bit5_reject:
        outputs[BIT5_REJECT] = H1
    allowed_sites = frozenset(outputs)
    queue = deque((frozenset(),))
    seen = {frozenset()}
    edges = 0
    terminals: list[frozenset[Coord]] = []
    bad: list[object] = []
    rail_front = {RAIL_B[0][0]: frozenset((RAIL_B[0][1],))}

    while queue:
        state = queue.popleft()
        records = dict(source)
        records.update({site: outputs[site] for site in state})
        actual = enabled(records)
        if actual.get(RAIL_B[0][0]) == rail_front[RAIL_B[0][0]]:
            actual.pop(RAIL_B[0][0])
        wrong = {
            site: values
            for site, values in actual.items()
            if site not in allowed_sites
            or values != frozenset((outputs[site],))
        }
        if wrong:
            bad.append((state, wrong))
            break
        if not actual:
            terminals.append(state)
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
        output_reached=any(OUTPUT in state for state in seen),
        reject_terminal=bool(terminals) and all(BIT5_REJECT in state for state in terminals),
        bad=tuple(bad),
    )


@dataclass(frozen=True)
class ProductStats:
    states: int
    edges: int
    terminals: int
    terminal_frontiers: tuple[tuple[tuple[Coord, frozenset[str]], ...], ...]
    bad: tuple[object, ...]


def product_graph() -> ProductStats:
    queue = deque(((frozenset(), 0),))
    seen = {(frozenset(), 0)}
    edges = 0
    terminals: list[tuple[tuple[Coord, frozenset[str]], ...]] = []
    bad: list[object] = []

    while queue:
        fragment_state, rail_count = queue.popleft()
        records = dict(TERMINAL)
        records.update({
            site: FRAGMENT_OUTPUTS[site]
            for site in fragment_state
        })
        records.update(dict(RAIL_B[:rail_count]))
        actual = enabled(records)
        rail_front = RAIL_B[rail_count] if rail_count < 12 else NEXT_C
        allowed = {
            site: frozenset((FRAGMENT_OUTPUTS[site],))
            for site in FRAGMENT_SITES - fragment_state
        }
        allowed[rail_front[0]] = frozenset((rail_front[1],))
        wrong = {
            site: values
            for site, values in actual.items()
            if allowed.get(site) != values
        }
        if wrong:
            bad.append((fragment_state, rail_count, wrong))
            break
        if len(fragment_state) == len(FRAGMENT_SITES) and rail_count == 12:
            terminals.append(tuple(sorted(actual.items())))
            continue
        legal = [
            site
            for site in actual
            if site in FRAGMENT_SITES
            or (rail_count < 12 and site == RAIL_B[rail_count][0])
        ]
        if not legal:
            bad.append((fragment_state, rail_count, "dead"))
            break
        for site in legal:
            if site in FRAGMENT_SITES:
                future = (fragment_state | {site}, rail_count)
            else:
                future = (fragment_state, rail_count + 1)
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)

    return ProductStats(
        states=len(seen),
        edges=edges,
        terminals=len(terminals),
        terminal_frontiers=tuple(sorted(set(terminals))),
        bad=tuple(bad),
    )


POSITIVE = fragment_graph(TERMINAL)
PRODUCT = product_graph()


def source_and_table_contract() -> None:
    section("A - Exact Cycle-100 terminal, generated rail, and mixed table")
    check("A01 Cycle 101 note exists", NOTE.is_file())
    check("A02 source is exactly the 264-record Cycle-100 terminal", TERMINAL == c100.records_at(10) and len(TERMINAL) == 264)
    check("A03 no fragment or first-B-rail record is supplied", FRAGMENT_SITES.isdisjoint(TERMINAL) and RAIL_B_SITES.isdisjoint(TERMINAL))
    check("A04 complete Cycle-52 A slice and BACKSTOP are already generated", len(RAIL_SEED) == 13 and all(TERMINAL.get(site) == content for site, content in RAIL_SEED.items()))
    check("A05 Cycle-100 plus Cycle-52 base has exactly 6,524 raw rows", len(BASE_RAW) == 6_524 and all(len(values) == 1 for values in BASE_RAW.values()))
    check("A06 relational fragment has 17 canonical and 372 raw rows", len(FRAGMENT_TABLE) == 17 and len(FRAGMENT_RAW) == 372)
    check("A07 fragment raw rows are disjoint from the complete base", set(FRAGMENT_RAW).isdisjoint(BASE_RAW))
    check("A08 complete mixed union has 6,896 single-valued raw rows", len(COMBINED_RAW) == 6_896 and all(len(values) == 1 for values in COMBINED_RAW.values()))
    check("A09 initial mixed frontier is exactly reader START plus rail START", enabled(TERMINAL) == {FRAGMENT_GROUPS[0][0][0]: frozenset((FRAGMENT_GROUPS[0][0][1],)), RAIL_B[0][0]: frozenset((RAIL_B[0][1],))}, str(enabled(TERMINAL)))


def literal_read_and_fragment_contract() -> None:
    section("B - Literal eight-bit read and zero-source first harness fragment")
    check("B01 fragment grows exactly 22 records in sixteen generations", len(FRAGMENT_SITES) == 22 and len(FRAGMENT_GROUPS) == 16)
    consumed_word = {
        site for site in c100.CODE_SITES if site in CONSUMED_TERMINAL
    }
    check("B02 every literal R_B11 bit is consumed by a grown exact signature", consumed_word == set(c100.CODE_SITES), str(consumed_word))
    check("B03 READY and VALID are both physically consumed before the word sweep", c100.READY in CONSUMED_TERMINAL and c100.VALID in CONSUMED_TERMINAL)
    check("B04 the stored literal remains exactly R_B11=10010100", tuple(1 if TERMINAL[site] == H1 else 0 for site in c100.CODE_SITES) == c100.R_B11_WORD == (1, 0, 0, 1, 0, 1, 0, 0))

    reference_signature = c100.c53.local_signature({**TERMINAL, **{site: content for group in FRAGMENT_GROUPS[:13] for site, content in group}}, REFERENCE)
    check("B05 grown reference sees literal bit0, old R_A10, and typed cage status", len(reference_signature) == 3 and {content for _direction, content in reference_signature} == {H1, "R_A10", "R_B32"}, str(reference_signature))
    certificate_records = dict(TERMINAL)
    certificate_records.update({site: content for group in FRAGMENT_GROUPS[:14] for site, content in group})
    certificate_signature = c100.c53.local_signature(certificate_records, CERTIFICATE)
    check("B06 compare certificate sees the grown reference and old R_A00 frame", len(certificate_signature) == 2 and {content for _direction, content in certificate_signature} == {"R_B33", "R_A00"})
    output_records = dict(certificate_records)
    output_records[CERTIFICATE] = FRAGMENT_OUTPUTS[CERTIFICATE]
    output_signature = c100.c53.local_signature(output_records, OUTPUT)
    check("B07 first write sees certificate plus two grown cage/status records", len(output_signature) == 3 and {content for _direction, content in output_signature} == {"R_B40", "R_B32"})
    wrong_reference = dict(certificate_records)
    wrong_reference[c100.CODE_SITES[0]] = H0
    check("B08 wrong literal bit0 cannot form the reference", COMBINED_RAW.get(c100.c53.local_signature(wrong_reference, REFERENCE)) is None)

    check("B09 full fragment graph has exactly 182 states and 538 edges", POSITIVE.states == 182 and POSITIVE.edges == 538, str(POSITIVE))
    check("B10 every asynchronous schedule reaches one complete 22-record terminal", POSITIVE.terminals == 1 and POSITIVE.terminal_sizes == (22,) and POSITIVE.output_reached and not POSITIVE.bad, str(POSITIVE))
    full = dict(TERMINAL)
    full.update(FRAGMENT_OUTPUTS)
    check("B11 complete old-debris fragment is quiet without the independent rail law", enabled(full, FRAGMENT_ONLY_RAW) == {}, str(enabled(full, FRAGMENT_ONLY_RAW)))


def wrong_word_contract() -> None:
    section("C - All one-bit stored-word corruptions fail closed")
    observed = []
    failures = []
    for index, site in enumerate(c100.CODE_SITES):
        source = dict(TERMINAL)
        source[site] = H0 if source[site] == H1 else H1
        stats = fragment_graph(source, allow_bit5_reject=index == 5)
        observed.append((stats.states, stats.edges, stats.terminal_sizes))
        if stats.output_reached or stats.bad or stats.terminals != 1:
            failures.append((index, stats))
        if index == 5 and not stats.reject_terminal:
            failures.append((index, "missing reject poison"))
    expected = [
        (38, 70, (14,)),
        (34, 62, (13,)),
        (30, 54, (12,)),
        (22, 34, (11,)),
        (6, 5, (5,)),
        (10, 13, (5,)),
        (4, 3, (3,)),
        (3, 2, (2,)),
    ]
    check("C01 all eight corruptions exhaust to one stopped graph with no output", not failures, str(failures[:1]))
    check("C02 exact corrupt-state/edge/terminal-size census is pinned", observed == expected, str(observed))

    valid_source = dict(TERMINAL)
    valid_source[c100.VALID] = H0
    ready_source = dict(TERMINAL)
    ready_source[c100.READY] = H0
    valid_stats = fragment_graph(valid_source)
    ready_stats = fragment_graph(ready_source)
    check("C03 wrong VALID stops after READY tap", valid_stats.states == 2 and valid_stats.edges == 1 and valid_stats.terminal_sizes == (1,) and not valid_stats.output_reached)
    check("C04 wrong READY stops before every fragment append", ready_stats.states == 1 and ready_stats.edges == 0 and ready_stats.terminal_sizes == (0,) and not ready_stats.output_reached)
    check("C05 bit5's history-mixed base row is an explicit one-record reject poison", BIT5_REJECT not in FRAGMENT_SITES and c100.COMBINED_RAW.get(c100.c53.local_signature({**TERMINAL, c100.CODE_SITES[5]: H0}, BIT5_REJECT)) == frozenset((H1,)))


def concurrency_covariance_and_scope_contract() -> None:
    section("D - Generated rail product, covariance, old debris, and scope")
    min_distance = min(manhattan(left, right) for left in FRAGMENT_SITES for right in RAIL_B_SITES)
    check("D01 fragment and generated B rail are noninteracting at minimum L1 four", min_distance == 4, str(min_distance))
    check("D02 exact mixed asynchronous product has 2,366 states and 9,178 edges", PRODUCT.states == 2_366 and PRODUCT.edges == 9_178, str(PRODUCT))
    expected_terminal = (((NEXT_C[0], frozenset((NEXT_C[1],))),),)
    check("D03 product has one terminal prefix exposing only exact next C-rail start", PRODUCT.terminals == 1 and PRODUCT.terminal_frontiers == expected_terminal and not PRODUCT.bad, str(PRODUCT))

    covariance_failures = []
    covariance_controls = 0
    for signature, values in COMBINED_RAW.items():
        for rotation in c100.c53.ROTATIONS:
            covariance_controls += 1
            actual = COMBINED_RAW.get(c100.c53.rotate_signature(signature, rotation))
            if actual != values:
                covariance_failures.append((signature, rotation, values, actual))
    check("D04 all 165,504 proper-cubic raw images preserve output", covariance_controls == 6_896 * 24 and not covariance_failures, str(covariance_failures[:1]))

    terminal_records = dict(TERMINAL)
    terminal_records.update(FRAGMENT_OUTPUTS)
    terminal_records.update(RAIL_B_OUTPUTS)
    rotated_failures = []
    shift = (83, -61, 47)
    for rotation in c100.c53.ROTATIONS:
        records = transform_records(terminal_records, rotation, shift)
        actual = enabled(records)
        expected_site = transform_site(NEXT_C[0], rotation, shift)
        if actual != {expected_site: frozenset((NEXT_C[1],))}:
            rotated_failures.append((rotation, actual))
    check("D05 all 24 rotated complete old-debris prefixes expose only next rail", not rotated_failures, str(rotated_failures[:1]))

    note = NOTE.read_text(encoding="utf-8").lower()
    check("D06 note pins zero supplied static residue", "zero supplied static residue" in note)
    check("D07 note names the exact next rail-join spine", "read_status_to_generated_rail_spine" in note)
    check("D08 note does not claim a complete reusable harness", "does not close the complete reusable harness" in note)
    check("D09 note contains the full N1-N8 gate", all(f"n{index}" in note for index in range(1, 9)))
    check("D10 Cycle 101 writes only its runner and review note", all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    source_and_table_contract()
    literal_read_and_fragment_contract()
    wrong_word_contract()
    concurrency_covariance_and_scope_contract()
    print(f"\nC100_TERMINAL={len(TERMINAL)} SUPPLIED_STATIC=0 FRAGMENT_GROWN={len(FRAGMENT_SITES)} RAIL_B_GROWN={len(RAIL_B)}")
    print(f"FRAGMENT_CANONICAL={len(FRAGMENT_TABLE)} FRAGMENT_RAW={len(FRAGMENT_RAW)} UNION_RAW={len(COMBINED_RAW)}")
    print(f"FRAGMENT_STATES={POSITIVE.states} PRODUCT_STATES={PRODUCT.states} PRODUCT_EDGES={PRODUCT.edges}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
