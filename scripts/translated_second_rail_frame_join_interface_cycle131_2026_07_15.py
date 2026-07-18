#!/usr/bin/env python3
"""Cycle 131: exact interface test for a translated second Cycle-129 bridge.

This runner asks only whether the executable campaign 16-row grammar can be translated and
applied literally at its terminal Y2/T_N0+B_0_2 interface.  It does not search
adapter rows or phase relabelings and therefore asserts no recurrence no-go.
"""

from __future__ import annotations

from pathlib import Path

import r_b01_port_to_role_closed_rail_frame_join_cycle129_2026_07_15 as c129


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "TRANSLATED_SECOND_RAIL_FRAME_JOIN_INTERFACE_CYCLE131_NOTE_2026-07-15.md"

c53 = c129.c53
PASS = 0
FAIL = 0

LAUNCH_TARGET = c129.GROUPS[0][0][0]
LAUNCH_LOCAL = c129.GROUP_LOCALS[0]
LAUNCH_CANONICAL = c53.canonical_signature(LAUNCH_LOCAL)
LAUNCH_ROLES = frozenset(value for _direction, value in LAUNCH_LOCAL)

CONTACT = c129.CONTACT
HEAD_PHASE = c129.HEAD_PHASE
FRAME_PARENT = c129.FRAME_PARENT
SECOND_SLOT = (-1, 2, 0)


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


TERMINAL = c129.positive_terminal_records()
COMMON_NEIGHBORS = tuple(sorted(
    set(c53.add(HEAD_PHASE, direction) for direction in c53.DIRECTIONS)
    & set(c53.add(FRAME_PARENT, direction) for direction in c53.DIRECTIONS)
))
OPEN_COMMON = tuple(site for site in COMMON_NEIGHBORS if site not in TERMINAL)
INTERFACE_ROLES = frozenset((TERMINAL[HEAD_PHASE], TERMINAL[FRAME_PARENT]))

# Hypothetically clear the second common neighbour only to price the type and
# context mismatch.  This is a read-only diagnostic, not an allowed deletion.
HYPOTHETICAL = dict(TERMINAL)
HYPOTHETICAL.pop(SECOND_SLOT)
SECOND_LOCAL = c53.local_signature(HYPOTHETICAL, SECOND_SLOT)
SECOND_CANONICAL = c53.canonical_signature(SECOND_LOCAL)

ALL_LAUNCH_MATCHES = tuple(sorted(
    site
    for site in c53.open_candidates(TERMINAL)
    if c53.canonical_signature(c53.local_signature(TERMINAL, site))
    == LAUNCH_CANONICAL
))


def interface_contract() -> None:
    section("A - Launch type versus terminal interface type")
    check("A01 Cycle 131 note exists", NOTE.is_file())
    check(
        "A02 campaign grammar launches from the exact H1 + R_B01 pair",
        LAUNCH_ROLES == frozenset(("H1", "R_B01"))
        and len(LAUNCH_LOCAL) == 2,
        str(LAUNCH_LOCAL),
    )
    check(
        "A03 terminal interface is exactly Y2 joined from T_N0 + B_0_2",
        TERMINAL[CONTACT] == "Y2"
        and INTERFACE_ROLES == frozenset(("T_N0", "B_0_2")),
        f"contact={TERMINAL[CONTACT]} roles={INTERFACE_ROLES}",
    )
    check(
        "A04 parent-role sets are disjoint and require two substitutions",
        not (LAUNCH_ROLES & INTERFACE_ROLES)
        and len(LAUNCH_ROLES - INTERFACE_ROLES) == 2,
        f"launch={LAUNCH_ROLES} terminal={INTERFACE_ROLES}",
    )
    check(
        "A05 no proper-cubic rotation can repair a content-label mismatch",
        all(
            c53.rotate_signature(LAUNCH_CANONICAL, rotation)
            != SECOND_CANONICAL
            for rotation in c53.ROTATIONS
        ),
        f"launch={LAUNCH_CANONICAL} second={SECOND_CANONICAL}",
    )


def occupancy_and_row_contract() -> None:
    section("B - Common-neighbour occupancy and literal row reuse")
    check(
        "B01 T_N0 and B_0_2 have exactly the two expected common neighbours",
        COMMON_NEIGHBORS == (CONTACT, SECOND_SLOT),
        str(COMMON_NEIGHBORS),
    )
    check(
        "B02 both common neighbours are permanently occupied",
        not OPEN_COMMON
        and TERMINAL[CONTACT] == "Y2"
        and TERMINAL[SECOND_SLOT] == "A_0_2",
        f"open={OPEN_COMMON} contents={(TERMINAL[CONTACT], TERMINAL[SECOND_SLOT])}",
    )
    check(
        "B03 completed terminal has zero open match for launch canonical",
        not ALL_LAUNCH_MATCHES,
        str(ALL_LAUNCH_MATCHES),
    )
    check(
        "B04 hypothetical cleared slot is not an existing Cycle-129 bridge row",
        SECOND_LOCAL not in c129.BRIDGE_RAW,
        f"local={SECOND_LOCAL} values={c129.BRIDGE_RAW.get(SECOND_LOCAL)}",
    )
    check(
        "B05 complete Cycle-129 law still exposes only ordered rail renewal",
        c129.enabled(TERMINAL)
        == {c129.NEXT_RAIL[0]: frozenset((c129.NEXT_RAIL[1],))},
        str(c129.enabled(TERMINAL)),
    )


def scope_contract() -> None:
    section("C - Bounded negative and live repair routes")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check(
        "C01 note names literal translated same-grammar scope",
        "literal translated same-grammar application" in note,
    )
    check(
        "C02 note keeps adapter and phase-relabel routes live",
        "adapter" in note and "phase relabel" in note,
    )
    check(
        "C03 note carries complete N1-N8 discipline",
        all(f"n{index}" in note for index in range(1, 9)),
    )
    check(
        "C04 note denies recurrence no-go and axiom addition",
        "not a recurrence no-go" in note and "no axiom addition follows" in note,
    )
    check(
        "C05 Cycle 131 writes only runner and review note",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    interface_contract()
    occupancy_and_row_contract()
    scope_contract()
    print(f"\nLAUNCH_CANONICAL={LAUNCH_CANONICAL}")
    print(f"SECOND_CANONICAL={SECOND_CANONICAL}")
    print(f"ROLE_SUBSTITUTIONS={len(LAUNCH_ROLES - INTERFACE_ROLES)} OPEN_SLOTS={len(OPEN_COMMON)}")
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT=EXACT_TRANSLATED_SECOND_INTERFACE_MISMATCH"
        if FAIL == 0
        else "RESULT=FAIL"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
