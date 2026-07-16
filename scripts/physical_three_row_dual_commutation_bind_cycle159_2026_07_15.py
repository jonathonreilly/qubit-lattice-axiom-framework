#!/usr/bin/env python3
"""Cycle 159: verify one measured row feeding two physical commutators."""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path

import physical_three_row_dual_commutation_bind_probe_2026_07_15 as p
import physical_two_port_row_four_fork_cycle158_2026_07_15 as prior


d = p.d
c53 = p.c53
comm = p.comm
ROWS = tuple(product((0, 1), repeat=5))
ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PHYSICAL_THREE_ROW_DUAL_COMMUTATION_BIND_CYCLE159_NOTE_2026-07-15.md"
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


def manhattan(left, right):
    return sum(abs(a - b) for a, b in zip(left, right))


def shifted_sites(sites, shift):
    return {p.add(site, shift) for site in sites}


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND LAW")
    check("review note exists", NOTE.is_file())
    check(
        "Cycle 159 adds no transition row",
        p.MERGED_RAW is p.twoport.MERGED_RAW and len(p.MERGED_RAW) == 89_516,
        len(p.MERGED_RAW),
    )
    check(
        "retained merged law remains deterministic",
        not p.twoport.RAW_CONFLICTS
        and all(len(outputs) == 1 for outputs in p.MERGED_RAW.values()),
        len(p.MERGED_RAW),
    )

    print("\nGEOMETRY AND SUPPLIED CONTENT")
    paths = {
        **{("generator", *key): path for key, path in p.GENERATOR_PATHS.items()},
        **{("internal", *key): path for key, path in p.MEASURED_INTERNAL_PATHS.items()},
        **{("continuation", *key): path for key, path in p.MEASURED_CONTINUATIONS.items()},
    }
    occurrences = Counter(site for path in paths.values() for site in path)
    locality_failures = [
        (key, left, right)
        for key, path in paths.items()
        for left, right in zip(path, path[1:])
        if manhattan(left, right) != 1
    ]
    check(
        "24 paths are nearest-neighbor with only 12 intended junction overlaps",
        len(paths) == 24
        and sum(map(len, paths.values())) == 2_958
        and len(occurrences) == 2_946
        and Counter(occurrences.values()) == {1: 2_934, 2: 12}
        and not locality_failures,
        (len(paths), sum(map(len, paths.values())), len(occurrences), locality_failures[:1]),
    )
    scaffold, terminal_ports = p.routing_scaffold()
    calculated_ports = {
        p.add(path[-1], p.sub(path[-1], path[-2]))
        for path in paths.values()
    }
    required_comm_ports = {
        p.add(term, center) for center in p.COMM_CENTERS for term in comm.TERMS
    }
    check(
        "one joint guide assignment closes all paths at the exact ports",
        terminal_ports == calculated_ports
        and required_comm_ports <= set(terminal_ports)
        and set(scaffold.values()) <= {p.FRAME, p.cable.GUIDE_ROLE},
        (len(scaffold), len(terminal_ports), len(required_comm_ports)),
    )

    g1 = (1, 0, 0, 1, 0)
    g2 = (0, 1, 1, 0, 1)
    measured = (1, 1, 0, 1, 0)
    initial, expected, dependencies = p.apparatus(g1, g2, measured)
    roles = Counter(initial.values())
    check(
        "only three row roles plus operator/guide/frame records are supplied",
        not (set(initial) & set(expected))
        and d.H0 not in initial.values()
        and d.H1 not in initial.values()
        and roles[p.ported.five.ROW_ROLE[g1]] == 1
        and roles[p.ported.five.ROW_ROLE[g2]] == 1
        and roles[p.twoport.five.ROW_ROLE[measured]] == 1,
        (len(initial), len(expected), len(dependencies)),
    )
    smoke_ok, smoke_detail = p.deterministic_run(g1, g2, measured)
    check(
        "one complete exact-frontier schedule produces both commutation records",
        smoke_ok and smoke_detail == (2_957, 23_564, 12, 33_736, 2_956),
        smoke_detail,
    )

    print("\nEXHAUSTIVE VALUES AND SCHEDULES")
    distribution = Counter()
    value_failures = []
    for measured_row in ROWS:
        for left in ROWS:
            left_value = comm.alu.bit(
                comm.alu.compact.algebra.symplectic(left, measured_row)
            )
            for right in ROWS:
                right_value = comm.alu.bit(
                    comm.alu.compact.algebra.symplectic(right, measured_row)
                )
                distribution[(left_value, right_value)] += 1
                if left_value not in (d.H0, d.H1) or right_value not in (d.H0, d.H1):
                    value_failures.append((left, right, measured_row))
    check(
        "all 32,768 row triples have the exact two-selector truth distribution",
        not value_failures
        and distribution
        == {
            (d.H0, d.H0): 9_728,
            (d.H0, d.H1): 7_680,
            (d.H1, d.H0): 7_680,
            (d.H1, d.H1): 7_680,
        },
        distribution,
    )
    center_sites = tuple(p.add(comm.CENTER, center) for center in p.COMM_CENTERS)
    anchor_failures = []
    anchors = (
        ((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)),
        ((1, 1, 1, 1, 1), (1, 1, 1, 1, 1), (1, 1, 1, 1, 1)),
        (g1, g2, measured),
        (g2, g1, measured),
        (measured, g1, g2),
        (measured, g2, g1),
    )
    for left, right, measured_row in anchors:
        outputs, _deps = p.expected_graph(left, right, measured_row)
        wanted = tuple(
            comm.alu.bit(comm.alu.compact.algebra.symplectic(row, measured_row))
            for row in (left, right)
        )
        got = tuple(outputs[site] for site in center_sites)
        if got != wanted:
            anchor_failures.append((left, right, measured_row, got, wanted))
    check(
        "the physical dependency graph places both exact algebraic answers",
        not anchor_failures,
        anchor_failures[:1],
    )
    cases, schedule_failures = p.local_schedule_proof(g1, g2, measured)
    check(
        "37,676 realizable local histories contain no wrong or parasitic write",
        cases == 37_676 and not schedule_failures,
        (cases, schedule_failures[:1]),
    )
    rotation_failures = []
    rotation_cases = Counter()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        cases, failures = p.local_schedule_proof(g1, g2, measured, rotation=rotation)
        rotation_cases[cases] += 1
        if failures:
            rotation_failures.append((rotation_index, cases, failures[:1]))
    check(
        "the composed all-schedule proof survives all 24 proper-cubic orientations",
        not rotation_failures and rotation_cases == {37_676: 24},
        (rotation_cases, rotation_failures[:1]),
    )

    print("\nCAUSAL CONTROLS")
    g1_starts = shifted_sites(p.ported.TARGETS, p.GENERATOR_CENTERS[0])
    g2_starts = shifted_sites(p.ported.TARGETS, p.GENERATOR_CENTERS[1])
    measured_starts = shifted_sites(p.twoport.TARGETS, p.MEASURED_CENTER)
    full_frontier = p.enabled(initial)
    without_g1 = dict(initial)
    without_g1.pop(p.GENERATOR_CENTERS[0])
    without_g2 = dict(initial)
    without_g2.pop(p.GENERATOR_CENTERS[1])
    without_measured = dict(initial)
    without_measured.pop(p.MEASURED_CENTER)
    check(
        "the initial frontier contains exactly the twelve row-bit writes",
        set(full_frontier) == g1_starts | g2_starts | measured_starts,
        len(full_frontier),
    )
    check(
        "deleting either generator suppresses exactly its four first writes",
        set(p.enabled(without_g1)) == g2_starts | measured_starts
        and set(p.enabled(without_g2)) == g1_starts | measured_starts,
    )
    check(
        "deleting the measured row suppresses exactly its shared four first writes",
        set(p.enabled(without_measured)) == g1_starts | g2_starts,
        p.enabled(without_measured),
    )
    shared_failures = []
    for bit_index in range(4):
        source = p.add(p.twoport.TARGETS[bit_index], p.MEASURED_CENTER)
        children = {
            p.MEASURED_INTERNAL_PATHS[(branch, bit_index)][-1]
            for branch in range(2)
        }
        if any(dependencies[child] != frozenset((source,)) for child in children):
            shared_failures.append((bit_index, source, children))
    check(
        "each measured bit is one record with two causal children",
        not shared_failures,
        shared_failures[:1],
    )
    dependency_failures = []
    for center in p.COMM_CENTERS:
        center_site = p.add(comm.CENTER, center)
        terms = frozenset(p.add(term, center) for term in comm.TERMS)
        if dependencies[center_site] != terms:
            dependency_failures.append((center_site, dependencies[center_site], terms))
        for term, geometry in zip(comm.TERMS, comm.PARENT_GEOMETRY, strict=True):
            target = p.add(term, center)
            parents = frozenset(
                (p.add(geometry["left"], center), p.add(geometry["right"], center))
            )
            if dependencies[target] != parents:
                dependency_failures.append((target, dependencies[target], parents))
    check(
        "both parity records depend on four two-parent products",
        not dependency_failures,
        dependency_failures[:1],
    )

    print("\nPREDECESSOR COEXISTENCE")
    prior_result = prior.main()
    check(
        "the complete Cycle-158 predecessor suite remains green",
        prior_result == 0,
        prior_result,
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "one measured row to two physical commutation records",
        "no transition row is added",
        "32,768",
        "37,676",
        "supplied guide/frame harness",
        "does not derive occurrence or equal weights",
        "no axiom addition follows",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_THREE_ROW_DUAL_COMMUTATION_BIND" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
