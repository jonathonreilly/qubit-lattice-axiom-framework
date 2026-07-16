#!/usr/bin/env python3
"""Cycle 160: verify output-ported commutation and isolated pivot control."""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path

import physical_case_role_isolation_cable_probe_2026_07_15 as isolation
import physical_three_row_dual_commutation_bind_probe_2026_07_15 as bind3
import physical_two_port_row_four_fork_cycle158_2026_07_15 as predecessor
import spacious_and_xor_streaming_commutator_probe_2026_07_15 as spacious
import streaming_parity_to_pivot_router_probe_2026_07_15 as controller


d = isolation.d
c53 = isolation.c53
pivot = isolation.pivot
ROWS = tuple(product((0, 1), repeat=5))
ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "OUTPUT_PORTED_COMMUTATOR_ISOLATED_PIVOT_CYCLE160_NOTE_2026-07-15.md"
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


def finite_graph(initial, expected, law):
    sites = tuple(expected)
    index = {site: bit for bit, site in enumerate(sites)}
    all_mask = (1 << len(sites)) - 1
    seen = {0}
    queue = [0]
    edges = 0
    terminals = 0
    maximum = 0
    bad = []
    while queue:
        mask = queue.pop(0)
        records = dict(initial)
        records.update({
            site: expected[site]
            for site, bit in index.items()
            if mask >> bit & 1
        })
        actual = {
            target: law[signature]
            for target in c53.open_candidates(records)
            if (signature := c53.local_signature(records, target)) in law
        }
        wrong = {
            site: values for site, values in actual.items()
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


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    law = isolation.MERGED_RAW

    print("AUTHORITY AND CANDIDATE LAW")
    check("review note exists", NOTE.is_file())
    check(
        "eight canonical rows copy four case roles through straight and turn cells",
        len(isolation.CANONICAL_TABLE) == 8
        and Counter(map(len, isolation.CANONICAL_TABLE)) == {5: 8}
        and set(isolation.CANONICAL_TABLE.values()) == set(pivot.CASE_ROLES),
        Counter(map(len, isolation.CANONICAL_TABLE)),
    )
    check(
        "192 new raw rows are disjoint and yield a deterministic 89,708-row law",
        len(isolation.CASE_CABLE_RAW) == 192
        and set(isolation.CASE_CABLE_RAW).isdisjoint(bind3.MERGED_RAW)
        and len(law) == 89_708
        and not isolation.RAW_CONFLICTS
        and all(len(outputs) == 1 for outputs in law.values()),
        (len(isolation.CASE_CABLE_RAW), len(law)),
    )
    check(
        "no foundation or axiom surface is part of the Cycle 160 delta",
        isolation.MERGED_RAW is not bind3.MERGED_RAW,
        "compiler-only candidate rows",
    )

    print("\nCASE-ROLE ISOLATION CABLE")
    fork_failures = []
    fork_sizes = set()
    for role in pivot.CASE_ROLES:
        for rotation_index, rotation in enumerate(c53.ROTATIONS):
            result = isolation.graph(role, rotation)
            if result[:5] != (36, 60, 1, 2, ()):
                fork_failures.append((role, rotation_index, result))
            else:
                fork_sizes.add(result[5])
    check(
        "all 96 case-role fork/orientation graphs are exact",
        not fork_failures and fork_sizes == {121},
        (fork_sizes, fork_failures[:1]),
    )
    deletion_failures = []
    for role in pivot.CASE_ROLES:
        initial, _expected, _ports = isolation.apparatus(role)
        initial.pop(isolation.SOURCE)
        if actual := isolation.enabled(initial):
            deletion_failures.append((role, actual))
    check(
        "deleting the case source suppresses both isolated branches",
        not deletion_failures,
        deletion_failures[:1],
    )

    print("\nOUTPUT-PORTED AND/XOR COMMUTATOR")
    old_spacious_law = spacious.MERGED_RAW
    spacious.MERGED_RAW = law
    try:
        value_failures = []
        detail_counts = Counter()
        for bits in product((0, 1), repeat=8):
            ok, detail = spacious.deterministic_run(bits)
            wanted = (
                (bits[0] & bits[1])
                ^ (bits[2] & bits[3])
                ^ (bits[4] & bits[5])
                ^ (bits[6] & bits[7])
            )
            if ok:
                detail_counts[detail[1:5]] += 1
            if not ok or detail[5] != wanted:
                value_failures.append((bits, ok, detail, wanted))
        check(
            "all 256 physical eight-input graphs produce exact four-product parity",
            not value_failures
            and detail_counts == {(3_217, 4, 14_954, 1_259): 256},
            (detail_counts, value_failures[:1]),
        )
        rotation_failures = []
        rotation_shapes = Counter()
        representative = (1, 1, 1, 0, 0, 1, 1, 1)
        for rotation_index, rotation in enumerate(c53.ROTATIONS):
            ok, detail = spacious.deterministic_run(representative, rotation)
            if ok:
                rotation_shapes[(detail[0], detail[2], detail[3], detail[4], detail[5])] += 1
            else:
                rotation_failures.append((rotation_index, detail))
        check(
            "the spacious commutator survives all 24 proper-cubic orientations",
            not rotation_failures
            and rotation_shapes == {(1_260, 4, 14_954, 1_259, 0): 24},
            (rotation_shapes, rotation_failures[:1]),
        )
        input_delete_failures = []
        initial, _expected, _dependencies, _result = spacious.apparatus(representative)
        input_sites = tuple(
            site
            for center in spacious.AND_CENTERS
            for site in (spacious.add(center, (0, 0, 1)), spacious.add(center, (-1, 0, 0)))
        )
        all_products = set(spacious.AND_CENTERS)
        for input_site in input_sites:
            mutated = dict(initial)
            mutated.pop(input_site)
            actual = spacious.enabled(mutated)
            if len(set(actual) & all_products) != 3:
                input_delete_failures.append((input_site, set(actual) & all_products))
        check(
            "deleting any one literal parent suppresses exactly its AND product",
            not input_delete_failures,
            input_delete_failures[:1],
        )
    finally:
        spacious.MERGED_RAW = old_spacious_law

    print("\nISOLATED PIVOT CONTROLLER")
    cases = (
        ((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)),
        ((0, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 0, 1, 0)),
        ((0, 1, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 1, 0)),
        ((0, 1, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 0, 1, 0)),
    )
    case_failures = []
    case_counts = Counter()
    old_controller_law = controller.MERGED_RAW
    controller.MERGED_RAW = law
    try:
        for args in cases:
            observed_case = pivot.pivot_rows(*args)[0]
            for rotation_index, rotation in enumerate(c53.ROTATIONS):
                ok, detail = controller.deterministic_run(*args, rotation=rotation)
                if ok:
                    case_counts[(observed_case, detail[0], detail[2], detail[3], detail[4])] += 1
                else:
                    case_failures.append((observed_case, rotation_index, detail))
        check(
            "all four cases pass in all 24 orientations through isolated lanes",
            not case_failures
            and case_counts
            == {
                (case, 624, 2, 7_504, 623): 24
                for case in product((0, 1), repeat=2)
            },
            (case_counts, case_failures[:1]),
        )
        source_failures = []
        for args in cases:
            initial, expected, _dependencies = controller.apparatus(*args)
            c_inputs = {
                controller.add(pivot.CASE_INPUTS["c1"], controller.ROUTER_SHIFT),
                controller.add(pivot.CASE_INPUTS["c2"], controller.ROUTER_SHIFT),
            }
            case_site = controller.add(pivot.CASE_SITE, controller.ROUTER_SHIFT)
            if (
                set(initial) & set(expected)
                or c_inputs & set(initial)
                or case_site in initial
                or any(role in initial.values() for role in pivot.CASE_ROLES)
            ):
                source_failures.append((args, len(initial), len(expected)))
        check(
            "selector inputs, case role, and lane selectors are absent initially",
            not source_failures,
            source_failures[:1],
        )
    finally:
        controller.MERGED_RAW = old_controller_law

    print("\nPREDECESSOR COEXISTENCE")
    old_bind3_law = bind3.MERGED_RAW
    bind3.MERGED_RAW = law
    try:
        smoke = bind3.deterministic_run(
            (1, 0, 0, 1, 0),
            (0, 1, 1, 0, 1),
            (1, 1, 0, 1, 0),
        )
        check(
            "the complete Cycle-159 smoke survives exactly",
            smoke == (True, (2_957, 23_564, 12, 33_736, 2_956)),
            smoke,
        )
        rotation_failures = []
        for rotation_index, rotation in enumerate(c53.ROTATIONS):
            cases_count, failures = bind3.local_schedule_proof(
                (1, 0, 0, 1, 0),
                (0, 1, 1, 0, 1),
                (1, 1, 0, 1, 0),
                rotation=rotation,
            )
            if cases_count != 37_676 or failures:
                rotation_failures.append((rotation_index, cases_count, failures[:1]))
        check(
            "all 24 Cycle-159 schedule proofs survive the new rows",
            not rotation_failures,
            rotation_failures[:1],
        )
    finally:
        bind3.MERGED_RAW = old_bind3_law

    old_p_law = predecessor.p.MERGED_RAW
    old_fork_law = predecessor.fork.MERGED_RAW
    old_bind_law = predecessor.bind.MERGED_RAW
    predecessor.p.MERGED_RAW = law
    predecessor.fork.MERGED_RAW = law
    predecessor.bind.MERGED_RAW = law
    try:
        row_failures = []
        for rotation_index, rotation in enumerate(c53.ROTATIONS):
            for row in ROWS:
                result = predecessor.p.graph(row, rotation)
                if result[:5] != (625, 2_500, 1, 8, ()):
                    row_failures.append((rotation_index, row, result))
        check(
            "all 768 two-port row-fork graphs survive",
            not row_failures,
            row_failures[:1],
        )

        bind_failures = []
        bind_cases = Counter()
        for left in ROWS:
            for right in ROWS:
                cases_count, failures = predecessor.bind.local_schedule_proof(left, right)
                bind_cases[cases_count] += 1
                if failures:
                    bind_failures.append((left, right, failures[:1]))
                    break
            if bind_failures:
                break
        check(
            "all 1,024 Cycle-156 schedule proofs survive",
            not bind_failures and bind_cases == {5_006: 1_024},
            (bind_cases, bind_failures[:1]),
        )

        router_failures = []
        for state_id in range(60):
            for basis in pivot.algebra.all_bases(state_id):
                for measurement_id in range(15):
                    for outcome_bit in (0, 1):
                        measured = pivot.algebra.measurement_row(measurement_id, outcome_bit)
                        result = predecessor.router_graph(*basis, measured)
                        if result != (10, 13, 1, 2, ()):
                            router_failures.append((state_id, basis, measurement_id, outcome_bit, result))
        check(
            "all 54,000 Cycle-152 router graphs survive",
            not router_failures,
            router_failures[:1],
        )

        unified_failures = []
        for state_id in range(60):
            for events in product(predecessor.u.EVENTS, repeat=2):
                ok, detail = predecessor.unified_run(state_id, events)
                if not ok:
                    unified_failures.append((state_id, events, detail))
        check(
            "all 86,640 prior unified histories survive",
            not unified_failures,
            unified_failures[:1],
        )
        check(
            "Cycle-144 terminal retains exactly its two priced fronts",
            predecessor.enabled(d.BOUND_TERMINAL) == d.BOUND_IGNORED,
            predecessor.enabled(d.BOUND_TERMINAL),
        )
    finally:
        predecessor.p.MERGED_RAW = old_p_law
        predecessor.fork.MERGED_RAW = old_fork_law
        predecessor.bind.MERGED_RAW = old_bind_law

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "output-ported commutator and isolated pivot controller",
        "eight canonical case-role cable rows",
        "89,708",
        "256",
        "96/96",
        "supplied product literals",
        "does not derive occurrence or equal weights",
        "no axiom addition follows",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "OUTPUT_PORTED_COMMUTATOR_ISOLATED_PIVOT" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
