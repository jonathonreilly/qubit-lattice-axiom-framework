#!/usr/bin/env python3
"""Cycle 187: reachable contact critical pair of two recurrent tubes.

Cycle 84 proved exact Cartesian factorization when two Cycle-80 recurrent
append tubes remain at strict-nearest-neighbour distance two.  This probe
moves two otherwise unchanged tube seeds into disjoint distance-one contact
and exhausts their asynchronous reachable graphs.

The result is bounded and conditional on the supplied pair of tube seeds.  It
is not a cosmological-boundary reachability theorem and has no authority over
foundation, axiom, primitive, registry, policy, queue, or audit surfaces.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import joint_endpoint_bdh_rebind_cycle63_2026_07_14 as c63
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import separated_recurrent_tube_collision_control_cycle84_2026_07_14 as c84


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "REACHABLE_RECURRENT_CONTACT_CRITICAL_PAIR_CYCLE187_NOTE_2026-07-16.md"
)

Coord = tuple[int, int, int]
HORIZONS = (3, 6, 9)
WITNESS_OFFSET: Coord = (0, -1, 4)
PLACEMENT: Coord = (31, -17, 9)

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


def contact_instance(horizon: int, offset: Coord):
    left_source, left_expected = c84.one_tube(horizon)
    right_source = c84.translate(left_source, offset)
    right_expected = c84.translate(left_expected, offset)
    source = {**left_source, **right_source}
    expected = {**left_expected, **right_expected}
    graph = c63.exact_graph(
        source,
        c84.c80.CONSTRUCTION.table,
        expected,
    )
    return source, expected, graph


def contact_offsets() -> tuple[Coord, ...]:
    source, expected = c84.one_tube(3)
    support = set(source) | set(expected)
    result = []
    for dy in range(-6, 7):
        for dz in range(-6, 7):
            if dy == dz == 0:
                continue
            offset = (0, dy, dz)
            shifted = {
                c84.add(site, offset)
                for site in support
            }
            if (
                support.isdisjoint(shifted)
                and c84.minimum_cross_distance(support, shifted) == 1
            ):
                result.append(offset)
    return tuple(result)


CONTACT_OFFSETS = contact_offsets()
CONTACT_GRAPHS = {
    offset: contact_instance(3, offset)
    for offset in CONTACT_OFFSETS
}
WITNESS_INSTANCES = {
    horizon: (
        CONTACT_GRAPHS[WITNESS_OFFSET]
        if horizon == 3
        else contact_instance(horizon, WITNESS_OFFSET)
    )
    for horizon in HORIZONS
}


def records_at_mask(
    source: dict[Coord, str],
    expected: dict[Coord, str],
    graph: c63.ExactGraph,
    mask: int,
) -> dict[Coord, str]:
    records = dict(source)
    records.update({
        site: expected[site]
        for bit, site in enumerate(graph.sites)
        if mask >> bit & 1
    })
    return records


def enabled_writes(
    records: dict[Coord, str],
) -> tuple[tuple[Coord, str, c53.Signature], ...]:
    result = []
    for target in c53.open_candidates(records):
        local = c53.local_signature(records, target)
        output = c84.c80.CONSTRUCTION.table.get(
            c53.canonical_signature(local)
        )
        if output is not None:
            result.append((target, output, local))
    return tuple(sorted(result))


def terminal_record_sets(
    expected: dict[Coord, str],
    graph: c63.ExactGraph,
) -> tuple[frozenset[tuple[Coord, str]], ...]:
    return tuple(
        frozenset(
            (site, expected[site])
            for bit, site in enumerate(graph.sites)
            if mask >> bit & 1
        )
        for mask in graph.terminals
    )


def rotated_witness_counts():
    source, expected, _graph = WITNESS_INSTANCES[3]
    failures = []
    wanted = (144, 952, 1_820, 2, (21, 21), 2, 0)
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        rotated_source = c84.rotate_translate(
            source, rotation, PLACEMENT
        )
        rotated_expected = c84.rotate_translate(
            expected, rotation, PLACEMENT
        )
        graph = c63.exact_graph(
            rotated_source,
            c84.c80.CONSTRUCTION.table,
            rotated_expected,
        )
        observed = (
            graph.conditions,
            len(graph.states),
            graph.edges,
            len(graph.terminals),
            tuple(sorted(mask.bit_count() for mask in graph.terminals)),
            len(graph.parasites),
            len(graph.conflicts),
        )
        if observed != wanted:
            failures.append((rotation_index, observed))
    return tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND PREDECESSOR")
    check("Cycle-187 review note exists", NOTE.is_file())
    check(
        "the consumed recurrent table is the unchanged 51-row Cycle-80 law",
        len(c84.c80.CONSTRUCTION.table) == 51,
        len(c84.c80.CONSTRUCTION.table),
    )

    print("\nALL DISJOINT DISTANCE-ONE PLACEMENTS")
    check(
        "the bounded transverse census contains exactly 28 contact placements",
        len(CONTACT_OFFSETS) == 28
        and WITNESS_OFFSET in CONTACT_OFFSETS,
        CONTACT_OFFSETS,
    )
    terminal_histogram = Counter(
        len(graph.terminals)
        for _source, _expected, graph in CONTACT_GRAPHS.values()
    )
    complete_failures = []
    parasite_histogram = Counter()
    conflict_histogram = Counter()
    for offset, (_source, expected, graph) in CONTACT_GRAPHS.items():
        complete = (1 << len(graph.sites)) - 1
        if complete in graph.states:
            complete_failures.append(offset)
        parasite_histogram[len(graph.parasites)] += 1
        conflict_histogram[len(graph.conflicts)] += 1
    check(
        "no contact placement reaches both complete recurrent tubes",
        not complete_failures,
        complete_failures,
    )
    check(
        "contact yields fourteen open escapes, twelve single terminals, and two split terminals",
        terminal_histogram == Counter({0: 14, 1: 12, 2: 2}),
        terminal_histogram,
    )
    check(
        "all contact placements expose cross-talk without same-site output conflict",
        parasite_histogram == Counter({2: 28})
        and conflict_histogram == Counter({0: 28}),
        (parasite_histogram, conflict_histogram),
    )

    print("\nEXACT REACHABLE CRITICAL PAIR")
    source, expected, graph = WITNESS_INSTANCES[3]
    terminals = tuple(sorted(graph.terminals))
    check(
        "the witness graph has two distinct incomplete maximal histories",
        (
            graph.conditions,
            len(graph.states),
            graph.edges,
            len(terminals),
            tuple(mask.bit_count() for mask in terminals),
            len(graph.parasites),
            len(graph.conflicts),
        ) == (144, 952, 1_820, 2, (21, 21), 2, 0),
        (
            graph.conditions,
            len(graph.states),
            graph.edges,
            len(terminals),
            tuple(mask.bit_count() for mask in terminals),
            graph.parasites,
            graph.conflicts,
        ),
    )
    shared = terminals[0] & terminals[1]
    check(
        "the two terminal histories share one reachable immediate predecessor",
        shared in graph.states
        and shared.bit_count() == 20,
        shared.bit_count(),
    )
    records = records_at_mask(source, expected, graph, shared)
    writes = enabled_writes(records)
    check(
        "the shared predecessor enables exactly two adjacent record writes",
        tuple((site, output) for site, output, _local in writes)
        == (
            ((1, 2, 3), "R_B23"),
            ((1, 2, 4), "R_B30"),
        )
        and c84.manhattan(writes[0][0], writes[1][0]) == 1,
        writes,
    )
    after = []
    for target, output, _local in writes:
        trial = dict(records)
        trial[target] = output
        after.append(enabled_writes(trial))
    check(
        "either adjacent write permanently disables every remaining write",
        after == [(), ()],
        after,
    )
    terminal_sets = terminal_record_sets(expected, graph)
    terminal_differences = frozenset((
        terminal_sets[0] - terminal_sets[1],
        terminal_sets[1] - terminal_sets[0],
    ))
    check(
        "the two permanent terminals differ only by the competing record",
        terminal_differences
        == frozenset({
            frozenset({((1, 2, 3), "R_B23")}),
            frozenset({((1, 2, 4), "R_B30")}),
        }),
        terminal_differences,
    )

    print("\nHORIZON AND COVARIANCE CONTROLS")
    horizon_counts = {}
    horizon_failures = []
    for horizon, (_source, _expected, horizon_graph) in WITNESS_INSTANCES.items():
        observed = (
            horizon_graph.conditions,
            len(horizon_graph.states),
            horizon_graph.edges,
            len(horizon_graph.terminals),
            tuple(
                sorted(mask.bit_count() for mask in horizon_graph.terminals)
            ),
            len(horizon_graph.parasites),
            len(horizon_graph.conflicts),
        )
        horizon_counts[horizon] = observed
        if observed != {
            3: (144, 952, 1_820, 2, (21, 21), 2, 0),
            6: (338, 1_972, 3_758, 2, (21, 21), 2, 0),
            9: (532, 2_992, 5_696, 2, (21, 21), 2, 0),
        }[horizon]:
            horizon_failures.append((horizon, observed))
    check(
        "the same early split survives horizons three, six, and nine",
        not horizon_failures,
        horizon_counts,
    )
    rotation_failures = rotated_witness_counts()
    check(
        "all 24 proper-cubic images preserve the reachable split",
        not rotation_failures,
        rotation_failures[:1],
    )

    print("\nSCOPE")
    normalized = (
        " ".join(NOTE.read_text(encoding="utf-8").lower().split())
        if NOTE.is_file()
        else ""
    )
    required = (
        "supplied two-tube boundary",
        "not a cosmological-boundary reachability theorem",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
        "no axiom addition follows",
    )
    missing = tuple(
        phrase for phrase in required
        if phrase not in normalized
    )
    check(
        "the note carries the bounded reachability and no-go discipline",
        not missing,
        missing,
    )

    print("\nACCOUNTING")
    print("CONTACT_OFFSETS", len(CONTACT_OFFSETS))
    print("TERMINAL_HISTOGRAM", terminal_histogram)
    print("WITNESS_OFFSET", WITNESS_OFFSET)
    print("WITNESS_WRITES", writes)
    print("HORIZON_COUNTS", horizon_counts)
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "REACHABLE_RECURRENT_CONTACT_CRITICAL_PAIR"
        if FAIL == 0
        else "CYCLE187_NEEDS_REPAIR",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
