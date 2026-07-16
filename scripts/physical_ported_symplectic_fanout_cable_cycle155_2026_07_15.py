#!/usr/bin/env python3
"""Cycle 155: verify ported four-bit row fanout and cable attachment."""

from __future__ import annotations

from collections import Counter, deque
from itertools import product
from pathlib import Path

import physical_ported_fanout_cable_bind_probe_2026_07_15 as bind


p = bind.ported
cable = p.cable
terminal = p.terminal
pivot = terminal.pivot
u = pivot.mult.c150.compact.unified
d = p.d
c53 = p.c53
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "PHYSICAL_PORTED_SYMPLECTIC_FANOUT_CABLE_CYCLE155_NOTE_2026-07-15.md"
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


def transformed(records, rotation, shift):
    return c53.transform_records(records, rotation, shift)


def terminal_fanout_graph(row, rotation=None):
    initial = terminal.source(row)
    expected = terminal.outputs(row)
    if rotation is not None:
        shift = (251, -257, 263)
        initial = transformed(initial, rotation, shift)
        expected = transformed(expected, rotation, shift)
    return finite_graph(initial, expected)


def router_graph(g1, g2, measured, rotation=None):
    initial, _case, _updated = pivot.source(g1, g2, measured)
    expected = pivot.expected(g1, g2, measured)
    if rotation is not None:
        shift = (269, -271, 277)
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

    print("AUTHORITY AND INTERFACE")
    check("review note exists", NOTE.is_file())
    check(
        "Cycle-154 cable law remains exact and conflict-free",
        len(cable.MERGED_RAW) == 83_372 and not cable.RAW_CONFLICTS,
        len(cable.MERGED_RAW),
    )
    check(
        "four output targets expose only x0,x1,z0,z1",
        len(p.TARGETS) == len(p.PORTS) == len(p.INDEX_ROLES) == 4
        and all(p.PORTS[index] == bind.scale(2, p.TARGETS[index]) for index in range(4)),
        (p.TARGETS, p.PORTS),
    )

    print("\nPORTED FANOUT LAW")
    check(
        "128 five-parent rows cover 32 rows by four symplectic bits",
        len(p.CANONICAL_TABLE) == 128
        and Counter(map(len, p.CANONICAL_TABLE)) == {5: 128},
        Counter(map(len, p.CANONICAL_TABLE)),
    )
    check(
        "every output is the exact indexed row bit and phase is not consumed",
        all(
            p.CANONICAL_TABLE[p.local(row, bit_index)] == p.bit(row[bit_index])
            for row in product((0, 1), repeat=5)
            for bit_index in range(4)
        ),
    )
    check(
        "3,072 ported rows are disjoint from Cycle 154",
        len(p.PORTED_RAW) == 3_072 and set(p.PORTED_RAW).isdisjoint(cable.MERGED_RAW),
        len(p.PORTED_RAW),
    )
    check(
        "ported fanout merges into 86,444 rows without conflict",
        len(p.MERGED_RAW) == 86_444
        and not p.RAW_CONFLICTS
        and all(len(values) == 1 for values in p.MERGED_RAW.values()),
        len(p.MERGED_RAW),
    )
    deletion_attempts, deletion_failures = deletion_controls()
    check(
        "deleting any direct fanout parent suppresses its intended bit",
        deletion_attempts == 640 and not deletion_failures,
        (deletion_attempts, deletion_failures[:1]),
    )

    print("\nOPEN PORTS AND CABLE BIND")
    ported_failures = []
    star_failures = []
    source_sizes = set()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for row in product((0, 1), repeat=5):
            ported_result = p.graph(row, rotation)
            if ported_result != (16, 32, 1, 4, ()):
                ported_failures.append((rotation_index, row, ported_result))
            star_result = bind.graph(row, rotation)
            if star_result != (625, 2_000, 1, 4, ()):
                star_failures.append((rotation_index, row, star_result))
            else:
                source_sizes.add(len(bind.apparatus(row)[0]))
    check("all 768 ported four-bit causal cubes are exact", not ported_failures, ported_failures[:1])
    check(
        "all 768 fanout-plus-four-cable causal products are exact",
        not star_failures and source_sizes == {193},
        (source_sizes, star_failures[:1]),
    )
    check(
        "one row record and no literal inputs drive sixteen physical writes",
        all(
            len(bind.apparatus(row)[1]) == 16
            and d.H0 not in bind.apparatus(row)[0].values()
            and d.H1 not in bind.apparatus(row)[0].values()
            and Counter(bind.apparatus(row)[0].values())[p.five.ROW_ROLE[row]] == 1
            for row in product((0, 1), repeat=5)
        ),
    )
    endpoint_failures = []
    for row in product((0, 1), repeat=5):
        _source, expected, terminal_ports, paths = bind.apparatus(row)
        for bit_index, path in enumerate(paths):
            if expected[path[-1]] != p.bit(row[bit_index]) or path[-1] in terminal_ports:
                endpoint_failures.append((row, bit_index, path[-1], expected[path[-1]], terminal_ports))
    check("every cable endpoint retains its indexed symplectic bit", not endpoint_failures, endpoint_failures[:1])

    print("\nPREDECESSOR COEXISTENCE")
    cable_failures = []
    for name, path in cable.PATHS.items():
        for value in (d.H0, d.H1):
            for rotation_index, rotation in enumerate(c53.ROTATIONS):
                initial, expected, _port = cable.apparatus(value, path)
                shift = (281, -283, 293)
                result = finite_graph(transformed(initial, rotation, shift), transformed(expected, rotation, shift))
                wanted = (1, 0, 1, 0, ()) if not expected else None
                # A cable is a single chain, not a Boolean cube; replay it directly.
                records = transformed(initial, rotation, shift)
                moved_expected = transformed(expected, rotation, shift)
                for step, (target, output) in enumerate(moved_expected.items()):
                    actual = enabled(records)
                    if actual != {target: frozenset((output,))}:
                        cable_failures.append((name, value, rotation_index, step, actual, target, output, result, wanted))
                        break
                    records[target] = output
                else:
                    if enabled(records):
                        cable_failures.append((name, value, rotation_index, "terminal", enabled(records)))
    check("all 192 Cycle-154 cable histories survive ported rows", not cable_failures, cable_failures[:1])

    terminal_failures = []
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for row in product((0, 1), repeat=5):
            result = terminal_fanout_graph(row, rotation)
            if result != (32, 80, 1, 5, ()):
                terminal_failures.append((rotation_index, row, result))
    check("all 768 Cycle-153 terminal fanout graphs survive ported rows", not terminal_failures, terminal_failures[:1])

    router_failures = []
    for state_id in range(60):
        for basis in pivot.algebra.all_bases(state_id):
            for measurement_id in range(15):
                for outcome_bit in (0, 1):
                    measured = pivot.algebra.measurement_row(measurement_id, outcome_bit)
                    result = router_graph(*basis, measured)
                    if result != (10, 13, 1, 2, ()):
                        router_failures.append((state_id, basis, measurement_id, outcome_bit, result))
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for state_id in range(60):
            basis = pivot.algebra.STATE_GENERATORS[state_id]
            for measurement_id in range(15):
                for outcome_bit in (0, 1):
                    measured = pivot.algebra.measurement_row(measurement_id, outcome_bit)
                    result = router_graph(*basis, measured, rotation)
                    if result != (10, 13, 1, 2, ()):
                        router_failures.append((rotation_index, state_id, measurement_id, outcome_bit, result))
    check("all 54,000 Cycle-152 router graphs survive ported rows", not router_failures, router_failures[:1])

    mixed_failures = []
    for state_id in range(60):
        for events in product(u.EVENTS, repeat=2):
            ok, detail = unified_run(state_id, events)
            if not ok:
                mixed_failures.append((state_id, events, detail))
    check("ported rows preserve all 86,640 prior unified histories", not mixed_failures, mixed_failures[:1])
    check(
        "Cycle-144 terminal retains exactly its two priced fronts",
        enabled(d.BOUND_TERMINAL) == d.BOUND_IGNORED,
        enabled(d.BOUND_TERMINAL),
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "ported symplectic row fanout",
        "four transport-ready bits",
        "phase bit remains in the row record",
        "core-first, cage-once",
        "does not derive occurrence or equal weights",
        "no axiom addition follows",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_PORTED_SYMPLECTIC_FANOUT_CABLE" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
