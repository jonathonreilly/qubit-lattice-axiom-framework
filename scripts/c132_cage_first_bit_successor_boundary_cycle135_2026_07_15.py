#!/usr/bin/env python3
"""Cycle 135: construct the first R_B01 bit and bound its nearest successor.

The Cycle-132 cage is rebuilt directly over the exact Cycle-129 predecessor.
One new four-parent row writes a unique physical H1 bit.  Every append order
from the exact source is exhausted.  A swapped H0 output, the direct nearest
H0 successor, the unary alternate successor, and one tested one-row guard
are tested as controls.

Only the first H1 bit is an executable bounded result here.  The guarded
H0 candidate has a clean compiler and factor but no full graph, so no byte,
completion, writer, or recurrence claim follows.  Authority: none.
"""

from __future__ import annotations

from pathlib import Path

import r_b01_port_to_role_closed_rail_frame_join_cycle129_2026_07_15 as c129


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "C132_CAGE_FIRST_BIT_SUCCESSOR_BOUNDARY_CYCLE135_NOTE_2026-07-15.md"
C132_NOTE = REVIEW / "C129_TWO_PARENT_CORNER_RELOCATED_CAGE_SEED_CYCLE132_NOTE_2026-07-15.md"

c112 = c129.c112
c105 = c129.c105
c101 = c129.c101
c59 = c129.c59
c53 = c129.c53

Coord = c129.Coord
Signature = c129.Signature
RawTable = c129.RawTable
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


def raw_rule(records: dict[Coord, str], site: Coord, output: str):
    local = c53.local_signature(records, site)
    canonical = c53.canonical_signature(local)
    return local, c59.raw_rule_outputs({canonical: output})


def targets(records: dict[Coord, str], raw: RawTable) -> tuple[Coord, ...]:
    return tuple(sorted(
        site
        for site in c53.open_candidates(records)
        if c53.local_signature(records, site) in raw
    ))


# Rebuild the exact executable Cycle-132 cage without importing its expensive
# predecessor graph a second time.  The Cycle-135 full graph independently
# includes every cage output and therefore rechecks the complete history.
CAGE_GENERATIONS = (
    ((5, 2, -3), "R_C11"),
    ((5, 1, -3), "R_C13"),
    ((5, 2, -2), "R_C21"),
    ((5, 1, -2), "R_C23"),
)
CAGE_OUTPUTS = dict(CAGE_GENERATIONS)
CAGE_TABLE: dict[Signature, str] = {}
CAGE_LOCALS: list[Signature] = []
CAGE_RECORDS = c129.positive_terminal_records()
for site, output in CAGE_GENERATIONS:
    local = c53.local_signature(CAGE_RECORDS, site)
    canonical = c53.canonical_signature(local)
    row = c59.raw_rule_outputs({canonical: output})
    if targets(CAGE_RECORDS, row) != (site,):
        raise RuntimeError((site, targets(CAGE_RECORDS, row)))
    CAGE_TABLE[canonical] = output
    CAGE_RECORDS[site] = output
    CAGE_LOCALS.append(local)
CAGE_RAW = c59.raw_rule_outputs(CAGE_TABLE)
C132_RAW = c112.merge_raw(c129.FULL_RAW, CAGE_RAW)

BIT: Coord = (5, 0, -2)
BIT_OUTPUT = "H1"
BIT_LOCAL, BIT_RAW = raw_rule(CAGE_RECORDS, BIT, BIT_OUTPUT)
BIT_TARGETS = targets(CAGE_RECORDS, BIT_RAW)
FULL_RAW = c112.merge_raw(C132_RAW, BIT_RAW)
BIT_OUTPUTS = {BIT: BIT_OUTPUT}
GROWN_OUTPUTS = {**c129.GROWN_OUTPUTS, **CAGE_OUTPUTS, **BIT_OUTPUTS}

FACTOR = c112.append_graph(
    source=CAGE_RECORDS,
    outputs=BIT_OUTPUTS,
    raw=FULL_RAW,
    ignored=c129.IGNORED_NEXT,
)
POSITIVE = c112.append_graph(
    source=c112.SOURCE,
    outputs=GROWN_OUTPUTS,
    raw=FULL_RAW,
    ignored=c129.IGNORED_NEXT,
    state_limit=15_000_000,
)
ALL_GROWN_MASK = (1 << len(GROWN_OUTPUTS)) - 1


def positive_terminal_records() -> dict[Coord, str]:
    if POSITIVE.terminal_states != (ALL_GROWN_MASK,):
        raise RuntimeError(POSITIVE.terminal_states)
    return c112.records_at(ALL_GROWN_MASK, c112.SOURCE, GROWN_OUTPUTS)


def enabled(records: dict[Coord, str], raw: RawTable = FULL_RAW):
    return {
        site: raw[local]
        for site in c53.open_candidates(records)
        if (local := c53.local_signature(records, site)) in raw
    }


# Wrong-bit control: the terminal-only factor cannot distinguish the swapped
# output, but the complete history exposes one unintended H1 target.
WRONG_LOCAL, WRONG_RAW = raw_rule(CAGE_RECORDS, BIT, "H0")
WRONG_UNION = c112.merge_raw(C132_RAW, WRONG_RAW)
WRONG_OUTPUTS = {BIT: "H0"}
WRONG_GROWN = {**c129.GROWN_OUTPUTS, **CAGE_OUTPUTS, **WRONG_OUTPUTS}
WRONG_COMPILED = c112.compile_conditions(
    c112.SOURCE, WRONG_GROWN, WRONG_UNION, c129.IGNORED_NEXT
)
WRONG_FACTOR = c112.append_graph(
    source=CAGE_RECORDS,
    outputs=WRONG_OUTPUTS,
    raw=WRONG_UNION,
    ignored=c129.IGNORED_NEXT,
)


# Nearest-successor controls after the executable H1 bit.
BIT_RECORDS = {**CAGE_RECORDS, BIT: BIT_OUTPUT}
DIRECT_SUCCESSOR: Coord = (5, -1, -2)
DIRECT_LOCAL, DIRECT_RAW = raw_rule(BIT_RECORDS, DIRECT_SUCCESSOR, "H0")
DIRECT_TARGETS = targets(BIT_RECORDS, DIRECT_RAW)
DIRECT_UNION = c112.merge_raw(FULL_RAW, DIRECT_RAW)
DIRECT_OUTPUTS = {BIT: BIT_OUTPUT, **{site: "H0" for site in DIRECT_TARGETS}}
DIRECT_GROWN = {**c129.GROWN_OUTPUTS, **CAGE_OUTPUTS, **DIRECT_OUTPUTS}
DIRECT_COMPILED = c112.compile_conditions(
    c112.SOURCE, DIRECT_GROWN, DIRECT_UNION, c129.IGNORED_NEXT
)
DIRECT_FACTOR = c112.append_graph(
    source=CAGE_RECORDS,
    outputs=DIRECT_OUTPUTS,
    raw=DIRECT_UNION,
    ignored=c129.IGNORED_NEXT,
)

UNARY_SUCCESSOR: Coord = (6, 0, -2)
UNARY_LOCAL, UNARY_RAW = raw_rule(BIT_RECORDS, UNARY_SUCCESSOR, "H0")
UNARY_TARGETS = targets(BIT_RECORDS, UNARY_RAW)


# Tested D1-neighbour guard.  Both supported coordinates share one
# L4+L6 canonical row, whose full orbit has six physical records.  Modeling
# all six makes the intended H0 unique and gives a clean compiler/factor, but
# no full graph is claimed or run here.
GUARD_SITE: Coord = (5, -2, -2)
GUARD_OUTPUT = "R_C30"
GUARD_LOCAL, GUARD_RAW = raw_rule(CAGE_RECORDS, GUARD_SITE, GUARD_OUTPUT)
GUARD_TARGETS = targets(CAGE_RECORDS, GUARD_RAW)
GUARD_RECORDS = {**CAGE_RECORDS, **{site: GUARD_OUTPUT for site in GUARD_TARGETS}}
GUARDED_BIT_RECORDS = {**GUARD_RECORDS, BIT: BIT_OUTPUT}
GUARDED_H0_LOCAL, GUARDED_H0_RAW = raw_rule(
    GUARDED_BIT_RECORDS, DIRECT_SUCCESSOR, "H0"
)
GUARDED_H0_TARGETS = targets(GUARDED_BIT_RECORDS, GUARDED_H0_RAW)
GUARD_CANDIDATE_RAW = c112.merge_raw(FULL_RAW, GUARD_RAW, GUARDED_H0_RAW)
GUARD_CANDIDATE_OUTPUTS = {
    **{site: GUARD_OUTPUT for site in GUARD_TARGETS},
    BIT: BIT_OUTPUT,
    DIRECT_SUCCESSOR: "H0",
}
GUARD_CANDIDATE_GROWN = {
    **c129.GROWN_OUTPUTS,
    **CAGE_OUTPUTS,
    **GUARD_CANDIDATE_OUTPUTS,
}
GUARD_COMPILED = c112.compile_conditions(
    c112.SOURCE,
    GUARD_CANDIDATE_GROWN,
    GUARD_CANDIDATE_RAW,
    c129.IGNORED_NEXT,
)
GUARD_FACTOR = c112.append_graph(
    source=CAGE_RECORDS,
    outputs=GUARD_CANDIDATE_OUTPUTS,
    raw=GUARD_CANDIDATE_RAW,
    ignored=c129.IGNORED_NEXT,
    state_limit=100_000,
)


def positive_contract() -> None:
    section("A - Exact first physical 1 bit")
    check("A01 Cycle 135 note and Cycle 132 predecessor note exist", NOTE.is_file() and C132_NOTE.is_file())
    check(
        "A02 rebuilt Cycle-132 cage is four canonical / 96 raw rows",
        len(CAGE_TABLE) == 4 and len(CAGE_RAW) == 96 and len(C132_RAW) == 9_206,
    )
    check(
        "A03 first bit has exact four-parent cage-plus-fixed local",
        BIT_LOCAL
        == (
            ((-1, 0, 0), "R_B10"),
            ((0, 0, -1), "L6"),
            ((0, 0, 1), "H1"),
            ((0, 1, 0), "R_C23"),
        ),
        str(BIT_LOCAL),
    )
    check(
        "A04 H1 row is 24 raw images with one exact terminal target",
        len(BIT_RAW) == 24 and BIT_TARGETS == (BIT,),
        str(BIT_TARGETS),
    )
    check(
        "A05 new row is disjoint and complete union has 9,230 rows",
        not (set(BIT_RAW) & set(C132_RAW))
        and len(FULL_RAW) == 9_230
        and all(len(values) == 1 for values in FULL_RAW.values()),
    )
    full_compiled = c112.compile_conditions(
        c112.SOURCE, GROWN_OUTPUTS, FULL_RAW, c129.IGNORED_NEXT
    )
    check(
        "A06 full compiler has 136 targets and zero unexpected",
        len(GROWN_OUTPUTS) == 135
        and len(full_compiled.conditions) == 136
        and not full_compiled.unexpected_targets,
    )
    check(
        "A07 isolated bit factor is two states / one edge / one terminal",
        FACTOR.states == 2
        and FACTOR.edges == 1
        and FACTOR.terminals == 1
        and FACTOR.terminal_sizes == (1,)
        and not FACTOR.bad
        and not FACTOR.unexpected_condition_targets,
    )
    check(
        "A08 every full history reaches one complete 135-write terminal",
        POSITIVE.states == 6_936_208
        and POSITIVE.edges == 53_907_076
        and POSITIVE.terminals == 1
        and POSITIVE.terminal_states == (ALL_GROWN_MASK,)
        and POSITIVE.terminal_sizes == (135,)
        and POSITIVE.max_frontier == 14
        and not POSITIVE.bad
        and not POSITIVE.unexpected_condition_targets
        and len(POSITIVE.reached) == 135,
        f"states={POSITIVE.states} edges={POSITIVE.edges}",
    )


def causal_and_wrong_bit_contract() -> None:
    section("B - Parent deletion and wrong-bit controls")
    parents = ((4, 0, -2), (5, 0, -3), (5, 0, -1), (5, 1, -2))
    deletion_failures = []
    for parent in parents:
        records = dict(CAGE_RECORDS)
        records.pop(parent)
        if BIT in enabled(records):
            deletion_failures.append(parent)
    check("B01 deleting any one of four parents disables H1", not deletion_failures, str(deletion_failures))
    check(
        "B02 swapped H0 row looks clean only in terminal factor",
        WRONG_FACTOR.states == 2
        and WRONG_FACTOR.edges == 1
        and WRONG_FACTOR.terminals == 1
        and not WRONG_FACTOR.bad,
    )
    check(
        "B03 swapped-H0 one-output corpus exposes one extra named target",
        WRONG_COMPILED.unexpected_targets == frozenset(((5, -1, -2),)),
        str(tuple(sorted(WRONG_COMPILED.unexpected_targets))),
    )
    check(
        "B04 extra target carries an inherited H1 output",
        any(
            values == frozenset(("H1",))
            for _present, _mask, values in WRONG_COMPILED.conditions[(5, -1, -2)]
        ),
    )


def successor_contract() -> None:
    section("C - Exact nearest-successor boundary")
    check(
        "C01 direct H0 successor has exactly two terminal images",
        DIRECT_TARGETS == ((5, -1, -2), (5, 1, 1)),
        str(DIRECT_TARGETS),
    )
    check(
        "C02 two-image corpus exposes two additional full-history targets",
        DIRECT_COMPILED.unexpected_targets
        == frozenset(((5, 0, 1), (5, 1, -1))),
        str(tuple(sorted(DIRECT_COMPILED.unexpected_targets))),
    )
    check(
        "C03 terminal-only direct factor is misleadingly clean",
        DIRECT_FACTOR.states == 6
        and DIRECT_FACTOR.edges == 7
        and DIRECT_FACTOR.terminals == 1
        and DIRECT_FACTOR.terminal_sizes == (3,)
        and not DIRECT_FACTOR.bad,
    )
    check(
        "C04 unary alternate successor has eleven terminal images",
        UNARY_LOCAL == (((-1, 0, 0), "H1"),)
        and len(UNARY_TARGETS) == 11
        and UNARY_SUCCESSOR in UNARY_TARGETS,
        str(UNARY_TARGETS),
    )
    check(
        "C05 tested guard row has six explicit physical images",
        GUARD_LOCAL == (((-1, 0, 0), "L4"), ((0, 0, 1), "L6"))
        and len(GUARD_TARGETS) == 6,
        str(GUARD_TARGETS),
    )
    check(
        "C06 six-record guard makes intended H0 terminal target unique",
        GUARDED_H0_TARGETS == (DIRECT_SUCCESSOR,),
        str(GUARDED_H0_TARGETS),
    )
    check(
        "C07 guarded candidate compiler and factor are clean but bounded",
        len(GUARD_CANDIDATE_GROWN) == 142
        and len(GUARD_COMPILED.conditions) == 143
        and not GUARD_COMPILED.unexpected_targets
        and GUARD_FACTOR.states == 144
        and GUARD_FACTOR.edges == 496
        and GUARD_FACTOR.terminals == 1
        and GUARD_FACTOR.terminal_sizes == (8,)
        and GUARD_FACTOR.max_frontier == 7
        and not GUARD_FACTOR.bad,
        f"factor={GUARD_FACTOR.states}/{GUARD_FACTOR.edges}",
    )


def renewal_and_scope_contract() -> None:
    section("D - Renewal, covariance, and exact scope")
    records = positive_terminal_records()
    failures = []
    for prefix, (site, output) in enumerate(c105.RAIL_SEQUENCE[12:96], 12):
        actual = enabled(records)
        expected = {site: frozenset((output,))}
        if actual != expected:
            failures.append((prefix, expected, actual))
            break
        records[site] = output
    check(
        "D01 eight rail slices remain singleton fronts after first bit",
        not failures
        and enabled(records)
        == {c105.RAIL_SEQUENCE[96][0]: frozenset((c105.RAIL_SEQUENCE[96][1],))},
        str(failures[:1]),
    )
    covariance_failures = []
    controls = 0
    for local, values in FULL_RAW.items():
        for rotation in c53.ROTATIONS:
            controls += 1
            if FULL_RAW.get(c53.rotate_signature(local, rotation)) != values:
                covariance_failures.append((local, rotation))
                break
    check(
        "D02 all 221,520 proper-cubic raw images preserve output",
        controls == len(FULL_RAW) * 24 == 221_520 and not covariance_failures,
    )
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("D03 note names c132_cage_first_bit_successor_boundary", "c132_cage_first_bit_successor_boundary" in note)
    check("D04 note carries refreshed N1-N8 discipline", all(f"n{i}" in note for i in range(1, 9)))
    check(
        "D05 note denies byte/writer/completion claims",
        "not an eight-bit word" in note
        and "not an r_b01 writer" in note
        and "no completion record" in note,
    )
    check("D06 note makes no axiom addition", "no axiom addition follows" in note)
    check(
        "D07 Cycle 135 writes runner and review note only",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    positive_contract()
    causal_and_wrong_bit_contract()
    successor_contract()
    renewal_and_scope_contract()
    print(
        f"\nBIT_RAW={len(BIT_RAW)} UNION_RAW={len(FULL_RAW)} "
        f"FULL={POSITIVE.states}/{POSITIVE.edges}"
    )
    print(
        f"DIRECT_IMAGES={len(DIRECT_TARGETS)} UNARY_IMAGES={len(UNARY_TARGETS)} "
        f"GUARD_IMAGES={len(GUARD_TARGETS)} GUARD_FACTOR={GUARD_FACTOR.states}/{GUARD_FACTOR.edges}"
    )
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT=C132_CAGE_FIRST_BIT_POSITIVE_NEAREST_SUCCESSOR_BOUNDED"
        if FAIL == 0
        else "RESULT=FAIL"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
