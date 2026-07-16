#!/usr/bin/env python3
"""Cycle 166: verify one physical joint conditional stabilizer update."""

from __future__ import annotations

from pathlib import Path

import output_ported_commutator_isolated_pivot_cycle160_2026_07_15 as c160
import physical_three_row_spacious_isolated_pivot_cycle161_2026_07_15 as c161
import physical_row_role_transport_cycle162_2026_07_15 as c162
import physical_isolated_row_mux_common_output_cycle163_2026_07_15 as c163
import physical_transport_bound_commuting_multiplier_cycle164_2026_07_15 as c164
import physical_row_reader_payload_tap_cycle165_2026_07_16 as c165
import physical_joint_stabilizer_update_geometry_probe_2026_07_16 as p


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PHYSICAL_JOINT_STABILIZER_UPDATE_CYCLE166_NOTE_2026-07-16.md"
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


def role_set(raw):
    return {
        role
        for outputs in raw.values()
        for role in outputs
    }


def valid_independent_basis(g1, g2) -> bool:
    return (
        not p.mult.algebra.symplectic(g1, g2)
        and any(g1[:4])
        and any(g2[:4])
        and g1[:4] != g2[:4]
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND LAW")
    check("Cycle-166 review note exists", NOTE.is_file())
    check(
        "the joint law has the exact bounded delta",
        len(p.tap.MERGED_RAW) == 97_388
        and len(p.SPLITTER_TABLE) == 32
        and len(p.SPLITTER_RAW) == 768
        and len(p.INTEGRATED_SELECTOR_TABLE) == 8
        and len(p.INTEGRATED_SELECTOR_RAW) == 192
        and len(p.INTEGRATED_GATE_TABLE) == 160
        and len(p.INTEGRATED_GATE_RAW) == 3_840
        and len(set(p.INTEGRATED_GATE_RAW) & set(p.tap.MERGED_RAW)) == 1_536
        and len(p.MERGED_RAW) == 100_652,
        (
            len(p.SPLITTER_RAW),
            len(p.INTEGRATED_SELECTOR_RAW),
            len(p.INTEGRATED_GATE_RAW),
            len(p.MERGED_RAW),
        ),
    )
    check(
        "the 100,652-row law is deterministic",
        not p.RAW_CONFLICTS
        and all(len(outputs) == 1 for outputs in p.MERGED_RAW.values()),
        len(p.RAW_CONFLICTS),
    )
    new_raw = p.cell.merge_raw(
        p.SPLITTER_RAW,
        p.INTEGRATED_SELECTOR_RAW,
        p.INTEGRATED_GATE_RAW,
    )
    check(
        "the joint repair adds no onsite role",
        role_set(new_raw) <= role_set(p.tap.MERGED_RAW),
        role_set(new_raw) - role_set(p.tap.MERGED_RAW),
    )
    check(
        "all four fixtures use valid independent stabilizer bases and nonidentity measured Paulis",
        set(p.CASE_REPRESENTATIVES) == {(0, 0), (0, 1), (1, 0), (1, 1)}
        and all(
            valid_independent_basis(g1, g2)
            and any(measured[:4])
            and p.pivot.pivot_rows(g1, g2, measured)[0] == case
            and (
                case != (0, 0)
                or measured
                in {
                    g1,
                    g2,
                    p.mult.algebra.multiply_commuting(g1, g2),
                }
            )
            for case, (g1, g2, measured) in p.CASE_REPRESENTATIVES.items()
        ),
        p.CASE_REPRESENTATIVES,
    )

    print("\nJOINT CASE, SCHEDULE, AND DELETION PROOF")
    check("the complete joint probe is green", p.main() == 0)

    print("\nPROPER-CUBIC COVARIANCE")
    rotation_results = []
    for case, rows in p.CASE_REPRESENTATIVES.items():
        for rotation_index, rotation in enumerate(p.c53.ROTATIONS):
            result = p.deterministic_run(*rows, rotation=rotation)
            rotation_results.append((case, rotation_index, result))
            print("ROTATION", case, rotation_index, result)
    check(
        "all four cases close in all 24 proper-cubic images",
        len(rotation_results) == 96
        and all(result[0] for _case, _index, result in rotation_results),
        sum(result[0] for _case, _index, result in rotation_results),
    )

    print("\nPREDECESSOR REGRESSIONS")
    predecessors = (
        ("Cycle 160", c160),
        ("Cycle 161", c161),
        ("Cycle 162", c162),
        ("Cycle 163", c163),
        ("Cycle 164", c164),
        ("Cycle 165", c165),
    )
    for label, module in predecessors:
        check(label + " remains green", module.main() == 0)

    print("\nSCOPE")
    note = (
        " ".join(NOTE.read_text(encoding="utf-8").lower().split())
        if NOTE.is_file()
        else ""
    )
    for phrase in (
        "constructive closure witness",
        "100,652",
        "zero adjacent unordered pairs",
        "twenty direct-parent deletion controls pass",
        "peres–mermin",
        "not yet the preferred candidate for fundamental-law compression",
        "no gravity claim follows",
        "no axiom, primitive, registry, policy, or audit edit follows",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "PHYSICAL_JOINT_STABILIZER_UPDATE" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
