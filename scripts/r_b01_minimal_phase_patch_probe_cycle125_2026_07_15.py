#!/usr/bin/env python3
"""Cycle 125: test the smallest local patch of the R_B01 writer reuse failure.

The probe uses proper-cubic orientation 20 of the Cycle-121 writer at the
Cycle-124 R_B01 port.  It moves D5 before D4 so D5 is an H0-site guard and
changes the final join role to R_C01.  This repairs the intended-order local
conflicts, then deliberately subjects the resulting table to full subset and
asynchronous checks.

The bounded result is negative: the translated tail has an empty local
signature, the candidate creates broad unary aliases, and the exact graph is
bad at the source.  This is not a no-go against other writers.

Authority: none.  No foundation, registry, queue, policy, audit, or git state
is edited or selected by this runner.
"""

from __future__ import annotations

from pathlib import Path

import r_b00_completion_to_r_b01_role_allocator_common_port_cycle124_2026_07_15 as c124


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "R_B01_MINIMAL_PHASE_PATCH_PROBE_CYCLE125_NOTE_2026-07-15.md"

c121 = c124.c121
c119 = c124.c119
c112 = c124.c112
c105 = c124.c105
c101 = c124.c101
c53 = c124.c53
c59 = c124.c59

Coord = c124.Coord
Signature = c124.Signature
H0 = c124.H0
H1 = c124.H1
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


def add_canonical(
    table: dict[Signature, str],
    records: dict[Coord, str],
    site: Coord,
    output: str,
) -> None:
    local = c53.local_signature(records, site)
    canonical = c53.canonical_signature(local)
    prior = table.get(canonical)
    if prior is not None and prior != output:
        raise ValueError((canonical, prior, output))
    table[canonical] = output


ROTATION_INDEX = 20
ROTATION = c53.ROTATIONS[ROTATION_INDEX]
OLD_PORT = c119.PORT
NEW_PORT = c124.PORT
ROTATED_OLD_PORT = c53.matvec(ROTATION, OLD_PORT)
SHIFT = tuple(
    NEW_PORT[index] - ROTATED_OLD_PORT[index]
    for index in range(3)
)


def transform(site: Coord) -> Coord:
    return c101.transform_site(site, ROTATION, SHIFT)


DATA_WORD = (1, 0, 0, 1, 0, 0, 0, 1)
DATA_OUTPUTS = tuple(H1 if bit else H0 for bit in DATA_WORD)
DATA_RECORDS = tuple(
    (transform(site), output)
    for site, output in zip(c121.DATA_SITES, DATA_OUTPUTS)
)

FRONT = transform(c121.FRONT)
TAIL = transform(c121.TAIL)
MID = transform(c121.MID)
JOIN = transform(c121.JOIN)
INHERITED = transform(c121.INHERITED)
COMPLETION = transform(c121.COMPLETION)
JOIN_OUTPUT = "R_C01"
COMPLETION_OUTPUT = "R_B01"

# D5 moves before D4.  It therefore sits beside D4 before both H0 branches
# can expose the live two-perpendicular-H0 -> H1 orbit.  This is the smallest
# intended-order guard repair tested here.
EARLY_ROWS = (
    DATA_RECORDS[0],
    DATA_RECORDS[1],
    (FRONT, c121.FRONT_OUTPUT),
    DATA_RECORDS[2],
    DATA_RECORDS[3],
    (TAIL, c121.TAIL_OUTPUT),
    (MID, c121.MID_OUTPUT),
    DATA_RECORDS[5],
)
LATE_ROWS = (
    DATA_RECORDS[4],
    DATA_RECORDS[7],
    DATA_RECORDS[6],
    (JOIN, JOIN_OUTPUT),
    (COMPLETION, COMPLETION_OUTPUT),
)


def build_candidate() -> tuple[dict[Signature, str], dict[Coord, str], Signature, frozenset[str] | None]:
    records = c124.positive_terminal_records()
    table: dict[Signature, str] = {}
    outputs: dict[Coord, str] = {}
    for site, output in EARLY_ROWS:
        add_canonical(table, records, site, output)
        records[site] = output
        outputs[site] = output

    inherited_local = c53.local_signature(records, INHERITED)
    partial_raw = c59.raw_rule_outputs(table)
    inherited_values = c112.merge_raw(c124.FULL_RAW, partial_raw).get(
        inherited_local
    )
    if inherited_values != frozenset((c121.INHERITED_OUTPUT,)):
        raise RuntimeError((INHERITED, inherited_local, inherited_values))
    records[INHERITED] = c121.INHERITED_OUTPUT
    outputs[INHERITED] = c121.INHERITED_OUTPUT

    for site, output in LATE_ROWS:
        add_canonical(table, records, site, output)
        records[site] = output
        outputs[site] = output
    return table, outputs, inherited_local, inherited_values


CANDIDATE_TABLE, EXTENSION_OUTPUTS, INHERITED_LOCAL, INHERITED_VALUES = build_candidate()
CANDIDATE_RAW = c59.raw_rule_outputs(CANDIDATE_TABLE)
FULL_RAW = c112.merge_raw(c124.FULL_RAW, CANDIDATE_RAW)
GROWN_OUTPUTS = {
    **c124.GROWN_OUTPUTS,
    **EXTENSION_OUTPUTS,
}
POSITIVE = c112.append_graph(
    source=c112.SOURCE,
    outputs=GROWN_OUTPUTS,
    raw=FULL_RAW,
)


def contract() -> None:
    section("A - Exact intended-order patch")
    check("A01 Cycle 125 note exists", NOTE.is_file())
    check(
        "A02 orientation 20 maps old port exactly onto fresh R_B01 port",
        transform(OLD_PORT) == NEW_PORT,
        f"old={OLD_PORT} new={NEW_PORT} mapped={transform(OLD_PORT)}",
    )
    check(
        "A03 all fourteen transformed extension sites are initially open",
        len(EXTENSION_OUTPUTS) == 14
        and set(EXTENSION_OUTPUTS).isdisjoint(c124.positive_terminal_records()),
    )
    decoded = tuple(
        1 if EXTENSION_OUTPUTS[transform(site)] == H1 else 0
        for site in c121.DATA_SITES
    )
    check(
        "A04 intended records decode literal R_B01=10010001",
        decoded == DATA_WORD,
        str(decoded),
    )
    check(
        "A05 early D5 is present before D4 and inherited H1 still fires",
        EARLY_ROWS[-1] == DATA_RECORDS[5]
        and INHERITED_VALUES == frozenset((c121.INHERITED_OUTPUT,)),
        f"X={INHERITED_LOCAL}->{INHERITED_VALUES}",
    )
    check(
        "A06 R_C01 phase label removes the old R_B00 completion collision",
        c53.local_signature(
            {
                **c124.positive_terminal_records(),
                **EXTENSION_OUTPUTS,
            },
            COMPLETION,
        )
        in CANDIDATE_RAW
        and CANDIDATE_RAW[
            c53.local_signature(
                {
                    **c124.positive_terminal_records(),
                    **EXTENSION_OUTPUTS,
                },
                COMPLETION,
            )
        ]
        == frozenset((COMPLETION_OUTPUT,)),
    )

    section("B - Full-table and subset failure")
    check(
        "B01 thirteen explicit rows quotient to twelve canonical / 159 raw",
        len(CANDIDATE_TABLE) == 12
        and len(CANDIDATE_RAW) == 159,
        f"canonical={len(CANDIDATE_TABLE)} raw={len(CANDIDATE_RAW)}",
    )
    check(
        "B02 8,903-row union is single-valued",
        len(FULL_RAW) == 8_903
        and all(len(values) == 1 for values in FULL_RAW.values()),
    )
    check(
        "B03 translated tail creates the empty local rule -> R_B41",
        CANDIDATE_RAW.get(()) == frozenset((c121.TAIL_OUTPUT,)),
        str(CANDIDATE_RAW.get(())),
    )
    unary = {
        local: values
        for local, values in CANDIDATE_RAW.items()
        if len(local) == 1
    }
    check(
        "B04 candidate also contributes thirty unary raw signatures",
        len(unary) == 30,
        str(list(unary.items())[:1]),
    )
    check(
        "B05 full subset compilation exposes 130 unexpected targets",
        len(POSITIVE.unexpected_condition_targets) == 130,
        str(sorted(POSITIVE.unexpected_condition_targets)[:1]),
    )
    check(
        "B06 asynchronous graph is bad at source before any candidate write",
        POSITIVE.states == 1
        and POSITIVE.edges == 0
        and POSITIVE.terminals == 0
        and POSITIVE.reached == frozenset()
        and len(POSITIVE.bad) == 1
        and POSITIVE.bad[0][0] == 0
        and POSITIVE.bad[0][2] == frozenset((c121.TAIL_OUTPUT,)),
        str(POSITIVE.bad[:1]),
    )
    check(
        "B07 intended R_B01 completion is unreachable",
        COMPLETION not in POSITIVE.reached,
    )


def scope_contract() -> None:
    section("C - Scope and no-go-discipline boundary")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check(
        "C01 note names exact bounded negative",
        "r_b01_minimal_phase_patch_probe" in note,
    )
    check(
        "C02 note names exact next repair target",
        "rail-attached provenance cage" in note,
    )
    check(
        "C03 note carries refreshed N1-N8 discipline",
        all(f"n{index}" in note for index in range(1, 9)),
    )
    check(
        "C04 note denies broad writer or recurrence no-go",
        "not a no-go against an r_b01 writer" in note
        and "not a no-go against recurrence" in note,
    )
    check("C05 note makes no axiom addition", "no axiom addition follows" in note)
    check(
        "C06 Cycle 125 writes only runner and review note",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    contract()
    scope_contract()
    print(
        f"\nCANDIDATE_CANONICAL={len(CANDIDATE_TABLE)} "
        f"CANDIDATE_RAW={len(CANDIDATE_RAW)} UNION_RAW={len(FULL_RAW)}"
    )
    print(
        f"UNEXPECTED={len(POSITIVE.unexpected_condition_targets)} "
        f"STATES={POSITIVE.states} EDGES={POSITIVE.edges}"
    )
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT=R_B01_MINIMAL_PHASE_PATCH_BOUNDED_NEGATIVE"
        if FAIL == 0
        else "RESULT=FAIL"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
