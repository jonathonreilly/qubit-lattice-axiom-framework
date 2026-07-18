#!/usr/bin/env python3
"""Cycle 163: verify isolated row muxes and directional common outputs."""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path

import physical_isolated_row_mux_common_output_probe_2026_07_15 as p
import physical_three_row_spacious_isolated_pivot_cycle161_2026_07_15 as c161
import physical_two_port_row_four_fork_cycle158_2026_07_15 as predecessor


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PHYSICAL_ISOLATED_ROW_MUX_COMMON_OUTPUT_CYCLE163_NOTE_2026-07-15.md"
)
ROWS = tuple(product((0, 1), repeat=5))
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


def back_signature(row_role: str):
    records = {(1, 0, 0): row_role, **p.TERMINAL_PATTERN}
    return p.c53.canonical_signature(p.c53.local_signature(records, (0, 0, 0)))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND LAW")
    check("Cycle-163 review note exists", NOTE.is_file())
    prior_gate = p.cell.merge_raw(p.transport.MERGED_RAW, p.GATE_RAW)
    prior_join = p.cell.merge_raw(prior_gate, p.JOIN_RAW)
    check(
        "224 canonical rows add 5,376 disjoint cubic rows",
        len(p.GATE_TABLE) == 160
        and len(p.JOIN_TABLE) == 32
        and len(p.TERMINAL_TABLE) == 32
        and len(p.GATE_RAW) == 3_840
        and len(p.JOIN_RAW) == 768
        and len(p.TERMINAL_RAW) == 768
        and set(p.GATE_RAW).isdisjoint(p.transport.MERGED_RAW)
        and set(p.JOIN_RAW).isdisjoint(prior_gate)
        and set(p.TERMINAL_RAW).isdisjoint(prior_join),
        (len(p.GATE_RAW), len(p.JOIN_RAW), len(p.TERMINAL_RAW)),
    )
    check(
        "the 96,620-row candidate law is deterministic",
        len(p.transport.MERGED_RAW) == 91_244
        and len(p.MERGED_RAW) == 96_620
        and not p.RAW_CONFLICTS
        and all(len(outputs) == 1 for outputs in p.MERGED_RAW.values()),
        len(p.MERGED_RAW),
    )
    direction_failures = [
        role for role in p.ROW_ROLES
        if p.terminal_local(role) == back_signature(role)
    ]
    check(
        "all 32 terminal motifs distinguish forward input from output backfeed",
        not direction_failures,
        direction_failures[:1],
    )

    print("\nMUX AND COMMON OUTPUT")
    check("the complete Cycle-163 mux probe is green", p.main() == 0)

    print("\nCYCLE-161 COMPOSED APPARATUS UNDER THE ENLARGED LAW")
    old_device_law = c161.p.MERGED_RAW
    c161.p.MERGED_RAW = p.MERGED_RAW
    try:
        zero = (0, 0, 0, 0, 0)
        axis = (0, 1, 0, 0, 0)
        probe = (0, 0, 0, 1, 0)
        anchors = (
            (zero, zero, zero),
            (zero, axis, probe),
            (axis, zero, probe),
            (axis, axis, probe),
        )
        case_failures = []
        for args in anchors:
            ok, detail = c161.p.deterministic_run(*args)
            wanted = c161.p.pivot.pivot_rows(*args)[0]
            if not ok or detail[5] != wanted or detail[6] != wanted:
                case_failures.append((args, ok, detail, wanted))
        check(
            "all four physical pivot cases remain exact under the new rows",
            not case_failures,
            case_failures[:1],
        )

        representative = (
            (1, 0, 0, 1, 0),
            (0, 1, 1, 0, 1),
            (1, 1, 0, 1, 0),
        )
        prepared = c161.p.apparatus(*representative)
        rotation_failures = []
        rotation_shapes = Counter()
        for rotation_index, rotation in enumerate(c161.p.c53.ROTATIONS):
            ok, detail = c161.p.execute(prepared, rotation=rotation)
            if ok:
                rotation_shapes[(detail[0], detail[3], detail[4], detail[5], detail[6], detail[7])] += 1
            else:
                rotation_failures.append((rotation_index, detail))
        check(
            "all 24 orientations of the three-row controller remain exact",
            not rotation_failures
            and rotation_shapes
            == {(16_890, 201_035, 16_889, (1, 0), (1, 0), ("L4", "L5")): 24},
            (rotation_shapes, rotation_failures[:1]),
        )
        local_cases, local_failures = c161.p.local_schedule_proof(prepared)
        check(
            "33,806 composed local histories contain no new parasitic write",
            local_cases == 33_806 and not local_failures,
            (local_cases, local_failures[:1]),
        )
    finally:
        c161.p.MERGED_RAW = old_device_law

    print("\nEXHAUSTIVE PREDECESSOR COEXISTENCE")
    old_p_law = predecessor.p.MERGED_RAW
    old_fork_law = predecessor.fork.MERGED_RAW
    old_bind_law = predecessor.bind.MERGED_RAW
    predecessor.p.MERGED_RAW = p.MERGED_RAW
    predecessor.fork.MERGED_RAW = p.MERGED_RAW
    predecessor.bind.MERGED_RAW = p.MERGED_RAW
    try:
        row_failures = []
        for rotation_index, rotation in enumerate(predecessor.c53.ROTATIONS):
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
            "all 1,024 Cycle-156 row-pair schedule proofs survive",
            not bind_failures and bind_cases == {5_006: 1_024},
            (bind_cases, bind_failures[:1]),
        )

        router_failures = []
        router_instances = 0
        for state_id in range(60):
            for basis in predecessor.pivot.algebra.all_bases(state_id):
                for measurement_id in range(15):
                    for outcome_bit in (0, 1):
                        measured = predecessor.pivot.algebra.measurement_row(
                            measurement_id, outcome_bit
                        )
                        result = predecessor.router_graph(*basis, measured)
                        router_instances += 1
                        if result != (10, 13, 1, 2, ()):
                            router_failures.append(
                                (state_id, basis, measurement_id, outcome_bit, result)
                            )
        for rotation_index, rotation in enumerate(predecessor.c53.ROTATIONS):
            for state_id in range(60):
                basis = predecessor.pivot.algebra.STATE_GENERATORS[state_id]
                for measurement_id in range(15):
                    for outcome_bit in (0, 1):
                        measured = predecessor.pivot.algebra.measurement_row(
                            measurement_id, outcome_bit
                        )
                        result = predecessor.router_graph(
                            *basis, measured, rotation=rotation
                        )
                        router_instances += 1
                        if result != (10, 13, 1, 2, ()):
                            router_failures.append(
                                (
                                    rotation_index,
                                    state_id,
                                    measurement_id,
                                    outcome_bit,
                                    result,
                                )
                            )
        check(
            "all 54,000 Cycle-152 router graphs survive",
            router_instances == 54_000 and not router_failures,
            (router_instances, router_failures[:1]),
        )

        unified_failures = []
        unified_instances = 0
        for state_id in range(60):
            for events in product(predecessor.u.EVENTS, repeat=2):
                ok, detail = predecessor.unified_run(state_id, events)
                unified_instances += 1
                if not ok:
                    unified_failures.append((state_id, events, detail))
        check(
            "all 86,640 retained unified histories survive",
            unified_instances == 86_640 and not unified_failures,
            (unified_instances, unified_failures[:1]),
        )
        check(
            "the Cycle-144 terminal retains exactly its two priced fronts",
            predecessor.enabled(predecessor.d.BOUND_TERMINAL)
            == predecessor.d.BOUND_IGNORED,
            predecessor.enabled(predecessor.d.BOUND_TERMINAL),
        )
    finally:
        predecessor.p.MERGED_RAW = old_p_law
        predecessor.fork.MERGED_RAW = old_fork_law
        predecessor.bind.MERGED_RAW = old_bind_law

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "flowed backward into every inactive terminal branch",
        "32 forward and backward signatures are distinct",
        "no new onsite role is introduced",
        "one fixed common output per lane",
        "the output-address gap is closed",
        "no axiom, primitive, registry, policy, or audit edit follows",
        "makes no impossibility or axiom-need claim",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_ISOLATED_ROW_MUX_COMMON_OUTPUT" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
