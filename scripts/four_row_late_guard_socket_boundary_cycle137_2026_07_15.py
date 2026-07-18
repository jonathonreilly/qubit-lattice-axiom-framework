#!/usr/bin/env python3
"""Cycle 137: exact boundary for one declared four-row socket family."""

from __future__ import annotations

from pathlib import Path

import post_cycle134_four_row_socket_search_scratch as search


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "FOUR_ROW_LATE_GUARD_SOCKET_BOUNDARY_CYCLE137_NOTE_2026-07-15.md"
SEARCH = ROOT / "scripts" / "post_cycle134_four_row_socket_search_scratch.py"

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


CENTERS, FRESH_ROLES, CENSUS, SURVIVORS = search.run_search()


EXPECTED_CENTERS = (
    (-2, 1, -1),
    (-2, 2, -2),
    (-2, 3, -1),
    (-1, 1, -2),
    (1, 2, -1),
)
EXPECTED_FRESH = (
    "R_C11",
    "R_C12",
    "R_C13",
    "R_C21",
    "R_C22",
    "R_C23",
    "R_C30",
    "R_C32",
    "R_C33",
    "R_C41",
    "R_LB",
)
EXPECTED_CENSUS = {
    "arm1_rows": 17_584,
    "arm2_rows": 13_492,
    "centers": 5,
    "direction_pairs": 26_256,
    "duplicate_sequences": 6_108,
    "factor_unexpected": 2_153,
    "factor_wrong_value": 2_810,
    "fresh_roles": 11,
    "full_unexpected": 3_147,
    "full_wrong_value": 3_770,
    "guard_attempts": 55,
    "guard_rows": 55,
    "helper_attempts": 2_420,
    "helper_rows": 2_188,
    "helper_target_contexts": 242,
    "open_geometries": 10_522,
    "role_assignments": 21_044,
    "socket_geometries": 3_770,
}


def interface_contract() -> None:
    section("A - Exact late interface and declared fresh roles")
    check("A01 Cycle 137 note exists", NOTE.is_file())
    check("A02 executable search module exists", SEARCH.is_file())
    check(
        "A03 exact five radius-three late centers are enumerated",
        CENTERS == EXPECTED_CENTERS,
        str(CENTERS),
    )
    check(
        "A04 every center has at least two parents including a Y2-valued record",
        all(
            len(search.s.c53.local_signature(search.TERMINAL, center)) >= 2
            and "Y2"
            in {
                value
                for _direction, value
                in search.s.c53.local_signature(search.TERMINAL, center)
            }
            for center in CENTERS
        ),
    )
    check(
        "A05 eleven roles are alphabet-closed and terminal-absent",
        FRESH_ROLES == EXPECTED_FRESH
        and not (set(FRESH_ROLES) & set(search.TERMINAL.values()))
        and set(FRESH_ROLES) <= search.s.c105.c89.FULL_ROLES,
        str(FRESH_ROLES),
    )


def census_contract() -> None:
    section("B - Complete declared-family census")
    check(
        "B01 complete census equals frozen Cycle-137 counts",
        CENSUS == EXPECTED_CENSUS,
        str(CENSUS),
    )
    check(
        "B02 all 55 late-guard role attempts are raw-compatible",
        CENSUS["guard_attempts"] == CENSUS["guard_rows"] == 55,
    )
    check(
        "B03 helper layer exhausts 242 contexts and 2,420 role attempts",
        CENSUS["helper_target_contexts"] == 242
        and CENSUS["helper_attempts"] == 2_420
        and CENSUS["helper_rows"] == 2_188,
    )
    check(
        "B04 orthogonal arms exhaust 26,256 pairs / 21,044 assignments",
        CENSUS["direction_pairs"] == 26_256
        and CENSUS["open_geometries"] == 10_522
        and CENSUS["role_assignments"] == 21_044,
    )
    check(
        "B05 all physical coimages leave 3,770 distinct socket geometries",
        CENSUS["arm1_rows"] == 17_584
        and CENSUS["arm2_rows"] == 13_492
        and CENSUS["duplicate_sequences"] == 6_108
        and CENSUS["socket_geometries"] == 3_770,
    )


def failure_contract() -> None:
    section("C - Expected-target and unexpected-target boundary")
    check(
        "C01 every socket geometry has a full-source wrong-value condition",
        CENSUS["full_wrong_value"]
        == CENSUS["socket_geometries"]
        == 3_770,
    )
    check(
        "C02 3,147 also expose a full-source unexpected target",
        CENSUS["full_unexpected"] == 3_147,
    )
    check(
        "C03 factor-scope failures overlap at 2,153 unexpected / 2,810 wrong",
        CENSUS["factor_unexpected"] == 2_153
        and CENSUS["factor_wrong_value"] == 2_810,
    )
    check(
        "C04 zero candidate reaches the schedule-graph gate",
        not SURVIVORS and "screen_survivors" not in CENSUS,
        str(SURVIVORS),
    )


def scope_contract() -> None:
    section("D - Exact scope and constitutional boundary")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check(
        "D01 note names four-row late-guard socket boundary",
        "four-row late-guard socket boundary" in note,
    )
    check(
        "D02 note declares radius-three/radius-four/radius-six envelope",
        "radius three" in note
        and "radius four" in note
        and "radius six" in note,
    )
    check(
        "D03 note keeps five-row, terminal-emitted, and bridge-redesign routes live",
        "five-row" in note
        and "terminal-emitted" in note
        and "bridge redesign" in note,
    )
    check(
        "D04 note carries complete N1-N8 discipline",
        all(f"n{index}" in note for index in range(1, 9)),
    )
    check(
        "D05 note denies four-row/global no-go, minimality, and axiom addition",
        "not a four-row no-go" in note
        and "not a socket no-go" in note
        and "no minimality follows" in note
        and "no axiom addition follows" in note,
    )
    check(
        "D06 Cycle 137 campaign surfaces are runner, search module, and review note",
        all(
            path.parent in (ROOT / "scripts", REVIEW)
            for path in (Path(__file__), SEARCH, NOTE)
        ),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    interface_contract()
    census_contract()
    failure_contract()
    scope_contract()
    print(
        f"\nSOCKET_GEOMETRIES={CENSUS['socket_geometries']} "
        f"FULL_WRONG={CENSUS['full_wrong_value']} "
        f"SCREEN_SURVIVORS={len(SURVIVORS)}"
    )
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT=FOUR_ROW_LATE_GUARD_SOCKET_BOUNDARY"
        if FAIL == 0
        else "RESULT=FAIL"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
