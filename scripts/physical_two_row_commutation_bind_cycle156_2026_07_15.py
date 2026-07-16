#!/usr/bin/env python3
"""Cycle 156: verify two physical row records through one commutation bit."""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path

import physical_two_row_commutation_bind_probe_2026_07_15 as p


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
    / "PHYSICAL_TWO_ROW_COMMUTATION_BIND_CYCLE156_NOTE_2026-07-15.md"
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
        "Cycle 156 adds no transition row",
        p.MERGED_RAW is p.ported.MERGED_RAW,
        len(p.MERGED_RAW),
    )
    check(
        "retained merged law is deterministic",
        not p.ported.RAW_CONFLICTS
        and all(len(outputs) == 1 for outputs in p.MERGED_RAW.values()),
        len(p.MERGED_RAW),
    )
    check(
        "four-bit spatial permutations are exact",
        sorted(p.LEFT_SPATIAL_BITS) == sorted(p.RIGHT_SPATIAL_BITS) == list(range(4))
        and {
            bit: p.LEFT_TERM_BY_BIT[bit]
            for bit in p.LEFT_SPATIAL_BITS
        } == p.LEFT_TERM_BY_BIT
        and {
            bit: p.RIGHT_TERM_BY_BIT[bit]
            for bit in p.RIGHT_SPATIAL_BITS
        } == p.RIGHT_TERM_BY_BIT,
        (p.LEFT_SPATIAL_BITS, p.RIGHT_SPATIAL_BITS),
    )

    print("\nGEOMETRY AND SUPPLIED CONTENT")
    path_sites = [site for path in p.PATHS.values() for site in path]
    path_failures = []
    for key, path in p.PATHS.items():
        side, bit_index = key
        term_index = (
            p.LEFT_TERM_BY_BIT[bit_index]
            if side == "left"
            else p.RIGHT_TERM_BY_BIT[bit_index]
        )
        geometry = comm.PARENT_GEOMETRY[term_index]
        input_site = geometry[side]
        terminal = p.add(path[-1], p.sub(path[-1], path[-2]))
        if (
            path[-1] != input_site
            or terminal != comm.TERMS[term_index]
            or any(manhattan(a, b) != 1 for a, b in zip(path, path[1:]))
        ):
            path_failures.append((key, path[-2:], input_site, terminal))
    check(
        "eight cable paths are local, disjoint, and reach their exact AND inputs",
        len(path_sites) == len(set(path_sites)) == 404 and not path_failures,
        (len(path_sites), len(set(path_sites)), path_failures[:1]),
    )
    scaffold, terminal_ports = p.routing_scaffold()
    check(
        "joint guide assignment closes all eight paths",
        terminal_ports == frozenset(comm.TERMS)
        and set(scaffold.values()) <= {p.FRAME, p.cable.GUIDE_ROLE},
        (len(scaffold), terminal_ports),
    )

    smoke_left = (0, 1, 0, 1, 0)
    smoke_right = (1, 0, 1, 0, 1)
    initial, expected, dependencies = p.apparatus(smoke_left, smoke_right)
    check(
        "only row/index/operator/guide/frame records are initially supplied",
        not (set(expected) & set(initial))
        and d.H0 not in initial.values()
        and d.H1 not in initial.values()
        and Counter(initial.values())[p.ported.five.ROW_ROLE[smoke_left]] == 1
        and Counter(initial.values())[p.ported.five.ROW_ROLE[smoke_right]] == 1,
        (len(initial), len(expected), len(dependencies)),
    )
    smoke_ok, smoke_detail = p.deterministic_run(smoke_left, smoke_right)
    check(
        "one complete causal schedule reaches only the physical commutation bit",
        smoke_ok and smoke_detail == (410, 1_872, 8, 4_540, 409),
        smoke_detail,
    )

    print("\nEXHAUSTIVE VALUES AND SCHEDULES")
    pair_failures = []
    case_counts = Counter()
    output_counts = Counter()
    for left in ROWS:
        for right in ROWS:
            cases, failures = p.local_schedule_proof(left, right)
            case_counts[cases] += 1
            output_counts[
                comm.alu.bit(comm.alu.compact.algebra.symplectic(left, right))
            ] += 1
            if failures:
                pair_failures.append((left, right, cases, failures[:1]))
                if len(pair_failures) >= 20:
                    break
        if len(pair_failures) >= 20:
            break
    check(
        "all 1,024 row pairs pass the local all-schedule proof",
        not pair_failures and case_counts == {5_006: 1_024},
        (case_counts, pair_failures[:1]),
    )
    check(
        "the final record has the exact symplectic truth distribution",
        output_counts == {d.H0: 544, d.H1: 480},
        output_counts,
    )
    check(
        "5,126,144 realizable local histories contain no parasitic write",
        sum(cases * count for cases, count in case_counts.items()) == 5_126_144,
        sum(cases * count for cases, count in case_counts.items()),
    )

    rotation_failures = []
    rotation_cases = Counter()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        cases, failures = p.local_schedule_proof(
            smoke_left, smoke_right, rotation=rotation
        )
        rotation_cases[cases] += 1
        if failures:
            rotation_failures.append((rotation_index, cases, failures[:1]))
    check(
        "the composed proof survives all 24 proper-cubic orientations",
        not rotation_failures and rotation_cases == {5_006: 24},
        (rotation_cases, rotation_failures[:1]),
    )

    print("\nCAUSAL CONTROLS")
    left_starts = shifted_sites(p.ported.TARGETS, p.LEFT_CENTER)
    right_starts = shifted_sites(p.ported.TARGETS, p.RIGHT_CENTER)
    without_left = dict(initial)
    without_left.pop(p.LEFT_CENTER)
    without_right = dict(initial)
    without_right.pop(p.RIGHT_CENTER)
    left_deleted_frontier = p.enabled(without_left)
    right_deleted_frontier = p.enabled(without_right)
    check(
        "deleting the left row suppresses exactly its four first writes",
        set(left_deleted_frontier) == right_starts
        and not (set(left_deleted_frontier) & left_starts),
        left_deleted_frontier,
    )
    check(
        "deleting the right row suppresses exactly its four first writes",
        set(right_deleted_frontier) == left_starts
        and not (set(right_deleted_frontier) & right_starts),
        right_deleted_frontier,
    )
    check(
        "the parity record depends on four products and every product on two cables",
        dependencies[comm.CENTER] == frozenset(comm.TERMS)
        and all(
            dependencies[term]
            == frozenset((geometry["left"], geometry["right"]))
            for term, geometry in zip(comm.TERMS, comm.PARENT_GEOMETRY)
        ),
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "two row records to one physical commutation record",
        "no transition row is added",
        "5,126,144",
        "supplied guide/frame harness",
        "does not derive occurrence or equal weights",
        "no axiom addition follows",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_TWO_ROW_COMMUTATION_BIND" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
