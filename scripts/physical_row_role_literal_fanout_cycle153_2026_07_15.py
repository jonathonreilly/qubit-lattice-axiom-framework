#!/usr/bin/env python3
"""Cycle 153: verify one-row-record to five-literal-bit physical fan-out."""

from __future__ import annotations

from collections import Counter, deque
from itertools import product
from pathlib import Path

import physical_row_role_literal_fanout_probe_2026_07_15 as p


pivot = p.pivot
u = pivot.mult.c150.compact.unified
d = p.d
c53 = p.c53
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "PHYSICAL_ROW_ROLE_LITERAL_FANOUT_CYCLE153_NOTE_2026-07-15.md"
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


def enabled(records):
    return {
        target: p.MERGED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in p.MERGED_RAW
    }


def finite_graph(initial, expected):
    sites = tuple(expected)
    index = {site: bit_index for bit_index, site in enumerate(sites)}
    all_mask = (1 << len(sites)) - 1
    queue = deque((0,))
    seen = {0}
    edges = 0
    terminals = 0
    maximum = 0
    bad = []
    while queue:
        mask = queue.popleft()
        records = dict(initial)
        records.update({
            site: expected[site]
            for site, bit_index in index.items()
            if mask >> bit_index & 1
        })
        actual = enabled(records)
        wrong = {
            site: values
            for site, values in actual.items()
            if site not in expected or values != frozenset((expected[site],))
        }
        if wrong:
            bad.append((mask, wrong))
            continue
        futures = tuple(
            site for site in actual
            if site in index and not (mask >> index[site] & 1)
        )
        maximum = max(maximum, len(futures))
        if mask == all_mask:
            terminals += int(not actual)
            if actual:
                bad.append((mask, actual))
            continue
        if not futures:
            bad.append((mask, "dead"))
            continue
        for site in futures:
            edges += 1
            future = mask | 1 << index[site]
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return len(seen), edges, terminals, maximum, tuple(bad)


def transformed(records, rotation, shift=(137, -139, 149)):
    return c53.transform_records(records, rotation, shift)


def deletion_controls():
    attempts = 0
    failures = []
    for local, output in p.CANONICAL_TABLE.items():
        for index in range(len(local)):
            attempts += 1
            mutated = local[:index] + local[index + 1:]
            if output in p.MERGED_RAW.get(mutated, frozenset()):
                failures.append((local, index, output))
    return attempts, tuple(failures)


def missing_index_controls():
    attempts = 0
    failures = []
    rows = tuple(product((0, 1), repeat=5))
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for row in rows:
            for missing in range(5):
                initial = p.source(row)
                del initial[p.INDEX_SITES[missing]]
                expected = p.outputs(row)
                del expected[p.TARGETS[missing]]
                result = finite_graph(transformed(initial, rotation), transformed(expected, rotation))
                attempts += 1
                if result != (16, 32, 1, 4, ()):
                    failures.append((rotation_index, row, missing, result))
    return attempts, tuple(failures)


def router_graph(g1, g2, measured, rotation=None):
    initial, _case, _updated = pivot.source(g1, g2, measured)
    expected = pivot.expected(g1, g2, measured)
    if rotation is not None:
        shift = (151, -157, 163)
        initial = c53.transform_records(initial, rotation, shift)
        expected = c53.transform_records(expected, rotation, shift)
    return finite_graph(initial, expected)


def unified_run(state_id, events):
    source, expected = u.apparatus(state_id, events)
    records = dict(source)
    for target, output in expected.items():
        actual = enabled(records)
        wanted = {target: frozenset((output,))}
        if actual != wanted:
            return False, (actual, wanted)
        records[target] = output
    return (not enabled(records), enabled(records))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND INTERFACE")
    check("review note exists", NOTE.is_file())
    check(
        "Cycle-152 router law remains exact and conflict-free",
        len(pivot.MERGED_RAW) == 82_316 and not pivot.RAW_CONFLICTS,
        len(pivot.MERGED_RAW),
    )
    check(
        "one source role spans exactly all 32 signed Pauli rows",
        len(p.five.ROW_ROLE) == len(p.five.ROLE_ROW) == 32,
    )
    check(
        "five distinct established roles name the five literal positions",
        len(p.INDEX_ROLES) == len(set(p.INDEX_ROLES)) == 5
        and not (set(p.INDEX_ROLES) & set(p.five.ROLE_ROW))
        and not (set(p.INDEX_ROLES) & {d.H0, d.H1, p.FRAME}),
        p.INDEX_ROLES,
    )

    print("\nLOCAL FANOUT LAW")
    check(
        "160 six-parent rows cover 32 rows by five bit positions",
        len(p.CANONICAL_TABLE) == 160
        and Counter(map(len, p.CANONICAL_TABLE)) == {6: 160},
        Counter(map(len, p.CANONICAL_TABLE)),
    )
    check(
        "every canonical output is the indexed literal bit",
        all(
            p.CANONICAL_TABLE[p.local(row, bit_index)] == p.bit(row[bit_index])
            for row in product((0, 1), repeat=5)
            for bit_index in range(5)
        ),
    )
    check(
        "960 proper-cubic rows are disjoint from the Cycle-152 law",
        len(p.FANOUT_RAW) == 960
        and set(p.FANOUT_RAW).isdisjoint(pivot.MERGED_RAW),
        (len(p.FANOUT_RAW), len(pivot.MERGED_RAW)),
    )
    check(
        "fanout merges into 83,276 rows without conflict",
        len(p.MERGED_RAW) == 83_276
        and not p.RAW_CONFLICTS
        and all(len(values) == 1 for values in p.MERGED_RAW.values()),
        len(p.MERGED_RAW),
    )
    check(
        "apparatus supplies one row record and no literal input bits",
        all(
            Counter(p.source(row).values())[p.five.ROW_ROLE[row]] == 1
            and d.H0 not in p.source(row).values()
            and d.H1 not in p.source(row).values()
            and len(p.source(row)) == 57
            for row in product((0, 1), repeat=5)
        ),
    )
    deletion_attempts, deletion_failures = deletion_controls()
    check(
        "deleting any direct fanout parent suppresses its intended bit",
        deletion_attempts == 960 and not deletion_failures,
        (deletion_attempts, deletion_failures[:1]),
    )

    print("\nALL ROWS, SCHEDULES, AND ROTATIONS")
    graph_failures = []
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for row in product((0, 1), repeat=5):
            result = p.graph(row, rotation)
            if result != (32, 80, 1, 5, ()):
                graph_failures.append((rotation_index, row, result))
    check(
        "all 768 fanout graphs realize the full five-write causal cube",
        not graph_failures,
        graph_failures[:1],
    )
    missing_attempts, missing_failures = missing_index_controls()
    check(
        "deleting any index token removes only that bit across all rotations",
        missing_attempts == 3_840 and not missing_failures,
        (missing_attempts, missing_failures[:1]),
    )
    source_delete_failures = []
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        initial = p.source((0, 0, 0, 0, 0))
        del initial[p.SOURCE]
        result = finite_graph(transformed(initial, rotation), {})
        if result != (1, 0, 1, 0, ()):
            source_delete_failures.append((rotation_index, result))
    check(
        "deleting the sole row source suppresses every bit in every orientation",
        not source_delete_failures,
        source_delete_failures[:1],
    )

    print("\nPREDECESSOR COEXISTENCE")
    router_failures = []
    for state_id in range(60):
        for basis in p.pivot.algebra.all_bases(state_id):
            for measurement_id in range(15):
                for outcome_bit in (0, 1):
                    measured = p.pivot.algebra.measurement_row(measurement_id, outcome_bit)
                    result = router_graph(*basis, measured)
                    if result != (10, 13, 1, 2, ()):
                        router_failures.append((state_id, basis, measurement_id, outcome_bit, result))
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for state_id in range(60):
            basis = p.pivot.algebra.STATE_GENERATORS[state_id]
            for measurement_id in range(15):
                for outcome_bit in (0, 1):
                    measured = p.pivot.algebra.measurement_row(measurement_id, outcome_bit)
                    result = router_graph(*basis, measured, rotation)
                    if result != (10, 13, 1, 2, ()):
                        router_failures.append((rotation_index, state_id, measurement_id, outcome_bit, result))
    check(
        "all 54,000 Cycle-152 router graphs survive the fanout rows",
        not router_failures,
        router_failures[:1],
    )
    mixed_failures = []
    for state_id in range(60):
        for events in product(u.EVENTS, repeat=2):
            ok, detail = unified_run(state_id, events)
            if not ok:
                mixed_failures.append((state_id, events, detail))
    check(
        "fanout rows preserve all 86,640 prior unified histories",
        not mixed_failures,
        mixed_failures[:1],
    )
    check(
        "Cycle-144 terminal retains exactly its two priced fronts",
        enabled(d.BOUND_TERMINAL) == d.BOUND_IGNORED,
        enabled(d.BOUND_TERMINAL),
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "one row record to five literal bits",
        "no literal input bits",
        "representation mismatch",
        "bit transport and duplicate use remain open",
        "finite role-level adapter",
        "does not derive occurrence or equal weights",
        "no axiom addition follows",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_ROW_ROLE_LITERAL_FANOUT" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
