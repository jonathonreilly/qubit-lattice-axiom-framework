#!/usr/bin/env python3
"""Cycle 154: verify the straight/turn physical literal-bit cable."""

from __future__ import annotations

from collections import Counter, deque
from itertools import product
from pathlib import Path

import physical_literal_bit_cable_probe_2026_07_15 as p


fanout = p.fanout
pivot = fanout.pivot
u = pivot.mult.c150.compact.unified
d = p.d
c53 = p.c53
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "PHYSICAL_LITERAL_BIT_CABLE_CYCLE154_NOTE_2026-07-15.md"
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


def fanout_graph(row, rotation=None):
    initial = fanout.source(row)
    expected = fanout.outputs(row)
    if rotation is not None:
        shift = (181, -191, 193)
        initial = transformed(initial, rotation, shift)
        expected = transformed(expected, rotation, shift)
    return finite_graph(initial, expected)


def router_graph(g1, g2, measured, rotation=None):
    initial, _case, _updated = pivot.source(g1, g2, measured)
    expected = pivot.expected(g1, g2, measured)
    if rotation is not None:
        shift = (197, -199, 211)
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

    print("AUTHORITY AND PREDECESSOR")
    check("review note exists", NOTE.is_file())
    check(
        "Cycle-153 fanout law remains exact and conflict-free",
        len(fanout.MERGED_RAW) == 83_276 and not fanout.RAW_CONFLICTS,
        len(fanout.MERGED_RAW),
    )
    check(
        "one established non-bit role types every cable guide",
        p.GUIDE_ROLE in d.PREFIX_ROLES
        and p.GUIDE_ROLE not in {d.H0, d.H1, p.FRAME},
        p.GUIDE_ROLE,
    )

    print("\nMINIMAL CABLE LAW")
    check(
        "four five-parent rows are exactly bit by straight-or-turn",
        len(p.CANONICAL_TABLE) == 4
        and Counter(map(len, p.CANONICAL_TABLE)) == {5: 4}
        and set(p.CANONICAL_TABLE.values()) == {d.H0, d.H1},
        Counter(map(len, p.CANONICAL_TABLE)),
    )
    check(
        "straight and turn signatures are geometrically distinct for both bits",
        all(
            p.canonical_local(value, "straight") != p.canonical_local(value, "turn")
            for value in (d.H0, d.H1)
        ),
    )
    check(
        "96 proper-cubic cable rows are disjoint from Cycle 153",
        len(p.CABLE_RAW) == 96 and set(p.CABLE_RAW).isdisjoint(fanout.MERGED_RAW),
        len(p.CABLE_RAW),
    )
    check(
        "cable merges into 83,372 rows without conflict",
        len(p.MERGED_RAW) == 83_372
        and not p.RAW_CONFLICTS
        and all(len(values) == 1 for values in p.MERGED_RAW.values()),
        len(p.MERGED_RAW),
    )
    deletion_attempts, deletion_failures = deletion_controls()
    check(
        "deleting any direct cable parent suppresses its intended copy",
        deletion_attempts == 20 and not deletion_failures,
        (deletion_attempts, deletion_failures[:1]),
    )

    print("\nPATHS, TURNS, AND CORRUPTION")
    path_failures = []
    instance_count = 0
    guide_counts = {}
    for name, path in p.PATHS.items():
        for value in (d.H0, d.H1):
            source, expected, terminal_port = p.apparatus(value, path)
            guide_counts.setdefault(name, set()).add(Counter(source.values())[p.GUIDE_ROLE])
            if terminal_port in source or terminal_port in expected:
                path_failures.append((name, value, "terminal-port-not-open"))
            for rotation_index, rotation in enumerate(c53.ROTATIONS):
                result = p.graph(value, path, rotation)
                instance_count += 1
                if result[:3] != (len(path), len(path) - 1, ()):
                    path_failures.append((name, value, rotation_index, result))
    check(
        "all 192 straight/turn/three-axis histories are exact",
        instance_count == 192 and not path_failures,
        (instance_count, guide_counts, path_failures[:1]),
    )
    check(
        "every cable cell sees a guide while compatible corner cells may share one",
        guide_counts == {
            "straight": {4},
            "one_turn": {3},
            "two_turn": {3},
            "three_axis": {4},
        },
        guide_counts,
    )
    guide_delete_failures = []
    attempts = 0
    for name, path in p.PATHS.items():
        for value in (d.H0, d.H1):
            source, expected, _port = p.apparatus(value, path)
            for guide_site in tuple(site for site, role in source.items() if role == p.GUIDE_ROLE):
                attempts += 1
                trial = dict(source)
                del trial[guide_site]
                records = dict(trial)
                progressed = 0
                while True:
                    actual = enabled(records)
                    wanted = {
                        site: values for site, values in actual.items()
                        if site in expected and site not in records
                    }
                    if len(wanted) != 1:
                        break
                    site, values = next(iter(wanted.items()))
                    if values != frozenset((expected[site],)):
                        break
                    records[site] = expected[site]
                    progressed += 1
                if progressed >= len(expected) or enabled(records):
                    guide_delete_failures.append((name, value, guide_site, progressed, enabled(records)))
    check(
        "deleting any path guide forces a strict preterminal stall",
        attempts == 28 and not guide_delete_failures,
        (attempts, guide_delete_failures[:1]),
    )

    print("\nPREDECESSOR COEXISTENCE")
    fanout_failures = []
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for row in product((0, 1), repeat=5):
            result = fanout_graph(row, rotation)
            if result != (32, 80, 1, 5, ()):
                fanout_failures.append((rotation_index, row, result))
    check("all 768 Cycle-153 fanout graphs survive cable rows", not fanout_failures, fanout_failures[:1])

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
    check("all 54,000 Cycle-152 router graphs survive cable rows", not router_failures, router_failures[:1])

    mixed_failures = []
    for state_id in range(60):
        for events in product(u.EVENTS, repeat=2):
            ok, detail = unified_run(state_id, events)
            if not ok:
                mixed_failures.append((state_id, events, detail))
    check("cable rows preserve all 86,640 prior unified histories", not mixed_failures, mixed_failures[:1])
    check(
        "Cycle-144 terminal retains exactly its two priced fronts",
        enabled(d.BOUND_TERMINAL) == d.BOUND_IGNORED,
        enabled(d.BOUND_TERMINAL),
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "physical literal-bit cable",
        "straight and covariant turn cells",
        "path compiler",
        "transport primitive",
        "does not choose a fundamental law",
        "does not derive occurrence or equal weights",
        "no axiom addition follows",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_LITERAL_BIT_CABLE" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
