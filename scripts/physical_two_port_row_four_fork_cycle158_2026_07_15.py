#!/usr/bin/env python3
"""Cycle 158: verify a two-port four-bit row reader and predecessor coexistence."""

from __future__ import annotations

from collections import Counter, deque
from itertools import product
from pathlib import Path

import physical_literal_bit_fork_probe_2026_07_15 as fork
import physical_two_port_row_four_fork_probe_2026_07_15 as p
import physical_two_row_commutation_bind_probe_2026_07_15 as bind


ported = p.ported
pivot = ported.terminal.pivot
u = pivot.mult.c150.compact.unified
d = p.d
c53 = p.c53
ROWS = tuple(product((0, 1), repeat=5))
ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PHYSICAL_TWO_PORT_ROW_FOUR_FORK_CYCLE158_NOTE_2026-07-15.md"
)
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


def enabled(records, law=None):
    law = p.MERGED_RAW if law is None else law
    return {
        target: law[signature]
        for target in c53.open_candidates(records)
        if (signature := c53.local_signature(records, target)) in law
    }


def finite_graph(initial, expected, law=None):
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
        actual = enabled(records, law)
        wrong = {
            site: values
            for site, values in actual.items()
            if site not in expected or values != frozenset((expected[site],))
        }
        if wrong:
            bad.append((mask, wrong))
            continue
        futures = tuple(
            site
            for site in actual
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


def deletion_controls():
    attempts = 0
    failures = []
    for signature, output in p.CANONICAL_TABLE.items():
        for index in range(len(signature)):
            attempts += 1
            mutated = signature[:index] + signature[index + 1:]
            if output in p.MERGED_RAW.get(mutated, frozenset()):
                failures.append((signature, index, output))
    return attempts, tuple(failures)


def transformed(records, rotation, shift):
    return c53.transform_records(records, rotation, shift)


def router_graph(g1, g2, measured, rotation=None):
    initial, _case, _updated = pivot.source(g1, g2, measured)
    expected = pivot.expected(g1, g2, measured)
    if rotation is not None:
        shift = (389, -397, 401)
        initial = transformed(initial, rotation, shift)
        expected = transformed(expected, rotation, shift)
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

    print("AUTHORITY AND LAW")
    check("review note exists", NOTE.is_file())
    check(
        "128 four-parent rows cover 32 rows by four symplectic positions",
        len(p.CANONICAL_TABLE) == 128
        and Counter(map(len, p.CANONICAL_TABLE)) == {4: 128},
        Counter(map(len, p.CANONICAL_TABLE)),
    )
    check(
        "every canonical output is the exact indexed row bit",
        all(
            p.CANONICAL_TABLE[p.local(row, bit_index)]
            == p.bit(row[bit_index])
            for row in ROWS
            for bit_index in range(4)
        ),
    )
    check(
        "3,072 two-port rows are disjoint from the Cycle-155 law",
        len(p.TWO_PORT_RAW) == 3_072
        and set(p.TWO_PORT_RAW).isdisjoint(ported.MERGED_RAW),
        len(p.TWO_PORT_RAW),
    )
    check(
        "the enlarged 89,516-row law is deterministic",
        len(p.MERGED_RAW) == 89_516
        and not p.RAW_CONFLICTS
        and all(len(outputs) == 1 for outputs in p.MERGED_RAW.values()),
        len(p.MERGED_RAW),
    )
    deletion_attempts, deletion_failures = deletion_controls()
    check(
        "deleting any direct two-port parent suppresses its intended bit",
        deletion_attempts == 512 and not deletion_failures,
        (deletion_attempts, deletion_failures[:1]),
    )

    print("\nTWO-PORT FOUR-FORK")
    graph_failures = []
    source_sizes = set()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for row in ROWS:
            result = p.graph(row, rotation)
            if result[:5] != (625, 2_500, 1, 8, ()):
                graph_failures.append((rotation_index, row, result))
            else:
                source_sizes.add(result[5])
    check(
        "all 768 row-orientation four-fork graphs are exact",
        not graph_failures and source_sizes == {97},
        (source_sizes, graph_failures[:1]),
    )
    endpoint_failures = []
    for row in ROWS:
        initial, expected, ports = p.apparatus(row)
        if (
            len(expected) != 12
            or len(ports) != 8
            or set(ports) & (set(initial) | set(expected))
            or d.H0 in initial.values()
            or d.H1 in initial.values()
            or Counter(initial.values())[p.five.ROW_ROLE[row]] != 1
        ):
            endpoint_failures.append((row, len(initial), expected, ports))
    check(
        "one row and no supplied bits drive eight fresh endpoints",
        not endpoint_failures,
        endpoint_failures[:1],
    )
    source_delete_failures = []
    for row in ROWS:
        initial, _expected, _ports = p.apparatus(row)
        initial.pop(p.SOURCE)
        actual = enabled(initial)
        if actual:
            source_delete_failures.append((row, actual))
    check(
        "deleting the row source suppresses all derived bits",
        not source_delete_failures,
        source_delete_failures[:1],
    )

    print("\nPREDECESSOR COEXISTENCE")
    old_ported_failures = []
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        shift = (409, -419, 421)
        for row in ROWS:
            initial = transformed(ported.source(row), rotation, shift)
            expected = transformed(ported.outputs(row), rotation, shift)
            result = finite_graph(initial, expected)
            if result != (16, 32, 1, 4, ()):
                old_ported_failures.append((rotation_index, row, result))
    check(
        "all 768 one-port row fanout graphs survive the two-port rows",
        not old_ported_failures,
        old_ported_failures[:1],
    )

    fork_failures = []
    old_fork_law = fork.MERGED_RAW
    fork.MERGED_RAW = p.MERGED_RAW
    try:
        for value in (d.H0, d.H1):
            for rotation_index, rotation in enumerate(c53.ROTATIONS):
                result = fork.graph(value, rotation)
                if result[:5] != (16, 24, 1, 2, ()):
                    fork_failures.append((value, rotation_index, result))
    finally:
        fork.MERGED_RAW = old_fork_law
    check(
        "all 48 supplied-bit fork graphs survive the two-port rows",
        not fork_failures,
        fork_failures[:1],
    )

    bind_failures = []
    bind_cases = Counter()
    old_bind_law = bind.MERGED_RAW
    bind.MERGED_RAW = p.MERGED_RAW
    try:
        for left in ROWS:
            for right in ROWS:
                cases, failures = bind.local_schedule_proof(left, right)
                bind_cases[cases] += 1
                if failures:
                    bind_failures.append((left, right, cases, failures[:1]))
                    if len(bind_failures) >= 20:
                        break
            if len(bind_failures) >= 20:
                break
    finally:
        bind.MERGED_RAW = old_bind_law
    check(
        "all 1,024 Cycle-156 row-pair schedule proofs survive",
        not bind_failures and bind_cases == {5_006: 1_024},
        (bind_cases, bind_failures[:1]),
    )

    router_failures = []
    for state_id in range(60):
        for basis in pivot.algebra.all_bases(state_id):
            for measurement_id in range(15):
                for outcome_bit in (0, 1):
                    measured = pivot.algebra.measurement_row(
                        measurement_id, outcome_bit
                    )
                    result = router_graph(*basis, measured)
                    if result != (10, 13, 1, 2, ()):
                        router_failures.append(
                            (state_id, basis, measurement_id, outcome_bit, result)
                        )
    check(
        "all 54,000 Cycle-152 router graphs survive the two-port rows",
        not router_failures,
        router_failures[:1],
    )

    unified_failures = []
    for state_id in range(60):
        for events in product(u.EVENTS, repeat=2):
            ok, detail = unified_run(state_id, events)
            if not ok:
                unified_failures.append((state_id, events, detail))
    check(
        "the enlarged law preserves all 86,640 prior unified histories",
        not unified_failures,
        unified_failures[:1],
    )
    check(
        "Cycle-144 terminal retains exactly its two priced fronts",
        enabled(d.BOUND_TERMINAL) == d.BOUND_IGNORED,
        enabled(d.BOUND_TERMINAL),
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "physical two-port row four-fork",
        "four recorded parents",
        "89,516",
        "no no-go is shipped",
        "compiler content",
        "does not derive occurrence or equal weights",
        "no axiom addition follows",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_TWO_PORT_ROW_FOUR_FORK" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
