#!/usr/bin/env python3
"""Cycle 152: exhaustive check of the physical four-case pivot router."""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path

import physical_four_case_pivot_router_probe_2026_07_15 as p


c150 = p.mult.c150
u = c150.compact.unified
d = p.d
c53 = p.c53
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "PHYSICAL_FOUR_CASE_PIVOT_ROUTER_CYCLE152_NOTE_2026-07-15.md"
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


def wrong_selector_controls():
    attempts = 0
    failures = []
    for case, selected in p.LANE_OUTPUT.items():
        for correct in selected:
            branch = p.SELECTOR_BRANCH[correct]
            for wrong in p.SELECTOR_ROLES:
                if wrong == correct:
                    continue
                for row_role in p.five.ROLE_ROW:
                    attempts += 1
                    local = p.copy_local(branch, wrong, row_role, case)
                    if local in p.MERGED_RAW:
                        failures.append((case, branch, correct, wrong, row_role, p.MERGED_RAW[local]))
    return attempts, tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND PREDECESSOR")
    check("review note exists", NOTE.is_file())
    check(
        "Cycle-151 commutation and multiplication law remains conflict-free",
        len(p.mult.MERGED_RAW) == 77_420 and not p.mult.RAW_CONFLICTS,
        len(p.mult.MERGED_RAW),
    )
    check(
        "router uses the established 32-role signed-row alphabet",
        len(p.five.ROW_ROLE) == len(p.five.ROLE_ROW) == 32,
    )

    print("\nFOUR-CASE CONTROLLER")
    check(
        "four case rows encode every commutation-bit pair",
        len(p.CASE_TABLE) == 4 and set(p.CASE_ROLE) == set(product((0, 1), repeat=2)),
        p.CASE_ROLE,
    )
    check(
        "eight lane rows select exactly two outputs per case",
        len(p.LANE_TABLE) == 8
        and set(p.LANE_OUTPUT) == set(product((0, 1), repeat=2))
        and all(len(outputs) == 2 for outputs in p.LANE_OUTPUT.values()),
        p.LANE_OUTPUT,
    )
    check(
        "five selector roles cover the two first-row and three second-row sources",
        len(p.SELECTOR_ROLES) == len(p.SELECTOR_BRANCH) == 5
        and set(p.SELECTOR_BRANCH.values()) == set(p.BRANCHES),
        p.SELECTOR_BRANCH,
    )
    check(
        "one shared existing marker role types every branch socket",
        p.ROUTER_MARKER in d.PREFIX_ROLES
        and set(p.BRANCH_MARK_POS) == set(p.BRANCHES),
        (p.ROUTER_MARKER, len(set(p.BRANCH_MARK_POS.values()))),
    )

    print("\nLAW MERGE")
    check(
        "192 physical row-copy contexts cover all selected rows",
        len(p.COPY_TABLE) == 192 and set(p.COPY_TABLE.values()) == set(p.five.ROLE_ROW),
        Counter(map(len, p.COPY_TABLE)),
    )
    check(
        "204 canonical router rows expand to 4,896 proper-cubic rows",
        len(p.CANONICAL_TABLE) == 204 and len(p.ROUTER_RAW) == 4_896,
        (len(p.CANONICAL_TABLE), len(p.ROUTER_RAW)),
    )
    check(
        "router merges into 82,316 rows without conflict",
        len(p.MERGED_RAW) == 82_316
        and not p.RAW_CONFLICTS
        and all(len(values) == 1 for values in p.MERGED_RAW.values()),
        (len(p.mult.MERGED_RAW), len(p.ROUTER_RAW), len(p.MERGED_RAW)),
    )
    attempts, selector_failures = wrong_selector_controls()
    check(
        "all wrong selectors remain inert at every typed branch socket",
        attempts == 1_024 and not selector_failures,
        (attempts, selector_failures[:1]),
    )
    deletion_attempts, deletion_failures = deletion_controls()
    check(
        "deleting any direct router parent suppresses its intended output",
        deletion_attempts == 1_004 and not deletion_failures,
        (deletion_attempts, deletion_failures[:1]),
    )

    print("\nEXHAUSTIVE CAUSAL GRAPHS")
    identity_failures = []
    identity_cases = Counter()
    for state_id in range(60):
        for basis in p.algebra.all_bases(state_id):
            for measurement_id in range(15):
                for outcome_bit in (0, 1):
                    measured = p.algebra.measurement_row(measurement_id, outcome_bit)
                    case, _updated = p.pivot_rows(*basis, measured)
                    identity_cases[case] += 1
                    result = p.graph(*basis, measured)
                    if result != (10, 13, 1, 2, ()):
                        identity_failures.append((state_id, basis, measurement_id, outcome_bit, result))
    check(
        "all 10,800 bases/outcomes have the exact finite causal graph",
        not identity_failures and sum(identity_cases.values()) == 10_800,
        (identity_cases, identity_failures[:1]),
    )

    rotation_failures = []
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for state_id in range(60):
            basis = p.algebra.STATE_GENERATORS[state_id]
            for measurement_id in range(15):
                for outcome_bit in (0, 1):
                    measured = p.algebra.measurement_row(measurement_id, outcome_bit)
                    result = p.graph(*basis, measured, rotation)
                    if result != (10, 13, 1, 2, ()):
                        rotation_failures.append((rotation_index, state_id, measurement_id, outcome_bit, result))
    check(
        "all 43,200 rotated canonical-basis graphs are exact",
        not rotation_failures,
        rotation_failures[:1],
    )
    check(
        "combined graph census is 54,000 with all four pivot cases present",
        not identity_failures
        and not rotation_failures
        and set(identity_cases) == set(product((0, 1), repeat=2)),
        10_800 + 43_200,
    )

    print("\nMIXED-DEVICE CLOSURE")
    mixed_failures = []
    for state_id in range(60):
        for events in product(u.EVENTS, repeat=2):
            ok, detail = unified_run(state_id, events)
            if not ok:
                mixed_failures.append((state_id, events, detail))
    check(
        "router rows preserve all 86,640 prior unified histories",
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
        "physical four-case pivot router",
        "supplied commutation bits",
        "supplied product row",
        "case-dependent output sites",
        "deterministic membership remains open",
        "does not derive occurrence or equal weights",
        "no axiom addition follows",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_FOUR_CASE_PIVOT_ROUTER" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
