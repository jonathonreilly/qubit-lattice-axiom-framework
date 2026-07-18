#!/usr/bin/env python3
"""Cycle 132: grow a relocated two-strand cage from the C129 bridge.

The old orientation-13 D2 coordinate is deliberately released from the old
writer layout.  In the Cycle-129 terminal it is an open two-parent corner
between the causally generated OZ and A_0_0 records.  A fresh anchor forms
there, grows two independently forced strands, and closes them through one
fixed R_B00 parent.

All append orderings are exhausted from the exact 264-record source.  This is
a bounded cage/launch seed, not an R_B01 word, writer, or recurrence theorem.
Authority: none.  No foundation, registry, queue, policy, audit, or git state
is edited or selected.
"""

from __future__ import annotations

from pathlib import Path

import r_b01_port_to_role_closed_rail_frame_join_cycle129_2026_07_15 as c129


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "C129_TWO_PARENT_CORNER_RELOCATED_CAGE_SEED_CYCLE132_NOTE_2026-07-15.md"

c124 = c129.c124
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


ANCHOR: Coord = (5, 2, -3)
ANCHOR_OUTPUT = "R_C11"
LOWER_STRAND: Coord = (5, 1, -3)
LOWER_STRAND_OUTPUT = "R_C13"
UPPER_STRAND: Coord = (5, 2, -2)
UPPER_STRAND_OUTPUT = "R_C21"
JOIN: Coord = (5, 1, -2)
JOIN_OUTPUT = "R_C23"

CAGE_GENERATIONS = (
    (ANCHOR, ANCHOR_OUTPUT),
    (LOWER_STRAND, LOWER_STRAND_OUTPUT),
    (UPPER_STRAND, UPPER_STRAND_OUTPUT),
    (JOIN, JOIN_OUTPUT),
)
CAGE_OUTPUTS = dict(CAGE_GENERATIONS)
CAGE_SITES = frozenset(CAGE_OUTPUTS)

OZ: Coord = (5, 3, -3)
OZ_OUTPUT = "OZ"
A00: Coord = (4, 2, -3)
A00_OUTPUT = "A_0_0"
FIXED_R_B00: Coord = (4, 1, -2)


def build_cage(
    role_sequence: tuple[str, str, str, str],
) -> tuple[
    dict[Signature, str],
    dict[Coord, str],
    tuple[Signature, ...],
    tuple[tuple[Coord, ...], ...],
]:
    records = c129.positive_terminal_records()
    table: dict[Signature, str] = {}
    outputs: dict[Coord, str] = {}
    locals_seen: list[Signature] = []
    observed: list[tuple[Coord, ...]] = []
    for (site, _declared_output), output in zip(CAGE_GENERATIONS, role_sequence):
        local = c53.local_signature(records, site)
        canonical = c53.canonical_signature(local)
        prior = table.get(canonical)
        if prior is not None and prior != output:
            raise RuntimeError((canonical, prior, output))
        raw = c59.raw_rule_outputs({canonical: output})
        matches = tuple(sorted(
            target
            for target in c53.open_candidates(records)
            if c53.local_signature(records, target) in raw
        ))
        if matches != (site,):
            raise RuntimeError((site, output, local, matches))
        table[canonical] = output
        outputs[site] = output
        records[site] = output
        locals_seen.append(local)
        observed.append(matches)
    return table, outputs, tuple(locals_seen), tuple(observed)


CAGE_ROLES = (
    ANCHOR_OUTPUT,
    LOWER_STRAND_OUTPUT,
    UPPER_STRAND_OUTPUT,
    JOIN_OUTPUT,
)
CAGE_TABLE, CAGE_OUTPUTS_BUILT, CAGE_LOCALS, OBSERVED = build_cage(CAGE_ROLES)
CAGE_RAW = c59.raw_rule_outputs(CAGE_TABLE)
FULL_RAW = c112.merge_raw(c129.FULL_RAW, CAGE_RAW)
GROWN_OUTPUTS = {**c129.GROWN_OUTPUTS, **CAGE_OUTPUTS}
BASE_TERMINAL = c129.positive_terminal_records()

FACTOR = c112.append_graph(
    source=BASE_TERMINAL,
    outputs=CAGE_OUTPUTS,
    raw=FULL_RAW,
    ignored=c129.IGNORED_NEXT,
)
ALL_FACTOR_MASK = (1 << len(CAGE_OUTPUTS)) - 1

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
        target: raw[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in raw
    }


def cage_enabled(records: dict[Coord, str]):
    return {
        target: values
        for target, values in enabled(records).items()
        if target in CAGE_SITES
    }


# Full-history role-selection control.  The first attractive role assignment
# gives LOWER_STRAND the live unary role R_C12.  Its multi-parent row is new,
# but old unary-R_C12 rows then fire at two unintended shell sites.  The bad
# candidate is compiled only; it is never inherited by FULL_RAW.
REJECTED_ROLES = ("R_C11", "R_C12", "R_C13", "R_C21")
(
    REJECTED_TABLE,
    REJECTED_OUTPUTS,
    REJECTED_LOCALS,
    REJECTED_OBSERVED,
) = build_cage(REJECTED_ROLES)
REJECTED_RAW = c59.raw_rule_outputs(REJECTED_TABLE)
REJECTED_UNION = c112.merge_raw(c129.FULL_RAW, REJECTED_RAW)
REJECTED_GROWN_OUTPUTS = {**c129.GROWN_OUTPUTS, **REJECTED_OUTPUTS}
REJECTED_COMPILED = c112.compile_conditions(
    c112.SOURCE,
    REJECTED_GROWN_OUTPUTS,
    REJECTED_UNION,
    c129.IGNORED_NEXT,
)


def table_contract() -> None:
    section("A - C129 two-parent corner and relocated two-strand cage")
    check("A01 Cycle 132 review note exists", NOTE.is_file())
    check(
        "A02 C129 predecessor has the executable full-history census",
        c129.POSITIVE.states == 6_541_456
        and c129.POSITIVE.edges == 51_107_588
        and c129.POSITIVE.terminals == 1
        and c129.POSITIVE.terminal_states == (c129.ALL_GROWN_MASK,)
        and len(c129.POSITIVE.reached) == 130
        and not c129.POSITIVE.bad,
    )
    check(
        "A03 old D2 coordinate is open and sees exactly OZ plus A_0_0",
        ANCHOR not in BASE_TERMINAL
        and CAGE_LOCALS[0]
        == (((-1, 0, 0), A00_OUTPUT), ((0, 1, 0), OZ_OUTPUT)),
        str(CAGE_LOCALS[0]),
    )
    check(
        "A04 anchor row is causally downstream of two generated C129 parents",
        BASE_TERMINAL.get(OZ) == OZ_OUTPUT
        and BASE_TERMINAL.get(A00) == A00_OUTPUT
        and OZ in c129.BRIDGE_OUTPUTS
        and A00 in c129.BRIDGE_OUTPUTS
        and {OZ, A00} <= c129.POSITIVE.reached
        and {OZ, A00}.isdisjoint(c112.SOURCE),
    )
    check(
        "A05 lower strand requires anchor plus the two L6 supports",
        tuple(value for _direction, value in CAGE_LOCALS[1])
        == ("L6", "L6", ANCHOR_OUTPUT),
        str(CAGE_LOCALS[1]),
    )
    check(
        "A06 upper strand requires anchor plus T_H3 and two H1 supports",
        set(value for _direction, value in CAGE_LOCALS[2])
        == {"T_H3", "H1", ANCHOR_OUTPUT}
        and len(CAGE_LOCALS[2]) == 4,
        str(CAGE_LOCALS[2]),
    )
    check(
        "A07 join requires fixed R_B00 and both distinct strands",
        set(value for _direction, value in CAGE_LOCALS[3])
        == {"R_B00", LOWER_STRAND_OUTPUT, UPPER_STRAND_OUTPUT}
        and len(CAGE_LOCALS[3]) == 3,
        str(CAGE_LOCALS[3]),
    )
    check(
        "A08 four canonical rows have 96 proper-cubic raw images",
        len(CAGE_TABLE) == 4
        and len(CAGE_RAW) == 96
        and all(len(values) == 1 for values in CAGE_RAW.values()),
        f"canonical={len(CAGE_TABLE)} raw={len(CAGE_RAW)}",
    )
    check(
        "A09 all four rows have one exact terminal target",
        OBSERVED == ((ANCHOR,), (LOWER_STRAND,), (UPPER_STRAND,), (JOIN,))
        and CAGE_OUTPUTS_BUILT == CAGE_OUTPUTS,
        str(OBSERVED),
    )
    check(
        "A10 new raw domain is disjoint and 9,206-row union single-valued",
        not (set(CAGE_RAW) & set(c129.FULL_RAW))
        and len(FULL_RAW) == 9_206
        and all(len(values) == 1 for values in FULL_RAW.values()),
    )


def graph_contract() -> None:
    section("B - Exact factor and full-history append graphs")
    factor_compiled = c112.compile_conditions(
        BASE_TERMINAL,
        CAGE_OUTPUTS,
        FULL_RAW,
        c129.IGNORED_NEXT,
    )
    full_compiled = c112.compile_conditions(
        c112.SOURCE,
        GROWN_OUTPUTS,
        FULL_RAW,
        c129.IGNORED_NEXT,
    )
    check(
        "B01 factor compiler has five targets and zero unexpected",
        len(factor_compiled.conditions) == 5
        and not factor_compiled.unexpected_targets,
        f"conditions={len(factor_compiled.conditions)}",
    )
    check(
        "B02 cage factor is six states / six edges / one four-write terminal",
        FACTOR.states == 6
        and FACTOR.edges == 6
        and FACTOR.terminals == 1
        and FACTOR.terminal_states == (ALL_FACTOR_MASK,)
        and FACTOR.terminal_sizes == (4,)
        and FACTOR.max_frontier == 2
        and not FACTOR.bad
        and not FACTOR.unexpected_condition_targets
        and len(FACTOR.reached) == 4,
        f"states={FACTOR.states} edges={FACTOR.edges} max={FACTOR.max_frontier}",
    )
    check(
        "B03 full compiler has 135 targets and zero unexpected",
        len(GROWN_OUTPUTS) == 134
        and len(full_compiled.conditions) == 135
        and not full_compiled.unexpected_targets,
        f"outputs={len(GROWN_OUTPUTS)} conditions={len(full_compiled.conditions)}",
    )
    check(
        "B04 every full history reaches one complete 134-write terminal",
        POSITIVE.states == 6_870_416
        and POSITIVE.edges == 53_451_460
        and POSITIVE.terminals == 1
        and POSITIVE.terminal_states == (ALL_GROWN_MASK,)
        and POSITIVE.terminal_sizes == (134,)
        and POSITIVE.max_frontier == 14
        and not POSITIVE.bad
        and not POSITIVE.unexpected_condition_targets
        and len(POSITIVE.reached) == 134,
        f"states={POSITIVE.states} edges={POSITIVE.edges} terminals={POSITIVE.terminals} max={POSITIVE.max_frontier}",
    )
    check(
        "B05 complete cage leaves only the next ordered rail record",
        enabled(positive_terminal_records())
        == {c129.NEXT_RAIL[0]: frozenset((c129.NEXT_RAIL[1],))},
        str(enabled(positive_terminal_records())),
    )


def causal_contract() -> None:
    section("C - Causal prerequisites and rejected-role control")
    check(
        "C01 terminal enables anchor first and neither strand nor join",
        cage_enabled(BASE_TERMINAL)
        == {ANCHOR: frozenset((ANCHOR_OUTPUT,))},
        str(cage_enabled(BASE_TERMINAL)),
    )
    after_anchor = {**BASE_TERMINAL, ANCHOR: ANCHOR_OUTPUT}
    check(
        "C02 anchor enables both strands and still not join",
        cage_enabled(after_anchor)
        == {
            LOWER_STRAND: frozenset((LOWER_STRAND_OUTPUT,)),
            UPPER_STRAND: frozenset((UPPER_STRAND_OUTPUT,)),
        },
        str(cage_enabled(after_anchor)),
    )
    after_lower = {**after_anchor, LOWER_STRAND: LOWER_STRAND_OUTPUT}
    after_upper = {**after_anchor, UPPER_STRAND: UPPER_STRAND_OUTPUT}
    check(
        "C03 either single strand leaves only the other strand enabled",
        cage_enabled(after_lower)
        == {UPPER_STRAND: frozenset((UPPER_STRAND_OUTPUT,))}
        and cage_enabled(after_upper)
        == {LOWER_STRAND: frozenset((LOWER_STRAND_OUTPUT,))},
    )
    after_both = {
        **after_anchor,
        LOWER_STRAND: LOWER_STRAND_OUTPUT,
        UPPER_STRAND: UPPER_STRAND_OUTPUT,
    }
    check(
        "C04 join becomes available only after both strands",
        cage_enabled(after_both) == {JOIN: frozenset((JOIN_OUTPUT,))},
        str(cage_enabled(after_both)),
    )
    without_oz = dict(BASE_TERMINAL)
    without_oz.pop(OZ)
    without_a00 = dict(BASE_TERMINAL)
    without_a00.pop(A00)
    check(
        "C05 either missing C129 parent prevents the anchor",
        ANCHOR not in enabled(without_oz)
        and ANCHOR not in enabled(without_a00),
    )
    check(
        "C06 rejected R_C12 strand role has two exact unexpected targets",
        REJECTED_COMPILED.unexpected_targets
        == frozenset(((5, 1, -4), (6, 1, -3))),
        str(tuple(sorted(REJECTED_COMPILED.unexpected_targets))),
    )
    check(
        "C07 both rejected targets would write A_2_1 from unary R_C12",
        all(
            any(values == frozenset(("A_2_1",)) for _present, _mask, values in REJECTED_COMPILED.conditions[target])
            for target in REJECTED_COMPILED.unexpected_targets
        ),
    )
    check(
        "C08 selected R_C13 strand role has no inherited unary input row",
        not any(
            len(local) == 1 and local[0][1] == LOWER_STRAND_OUTPUT
            for local in c129.FULL_RAW
        ),
    )


def rail_and_covariance_contract() -> None:
    section("D - Continued rail renewal and proper-cubic covariance")
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
        "D01 remaining 84 writes through eight slices stay singleton fronts",
        not failures
        and enabled(records)
        == {c105.RAIL_SEQUENCE[96][0]: frozenset((c105.RAIL_SEQUENCE[96][1],))},
        str(failures[:1]),
    )

    long_rail = c105.c108.c104.rail_sequence(102, c105.ROLE_MAP)
    late = positive_terminal_records()
    late_failures = []
    for prefix in range(12, 101 * 12):
        site, output = long_rail[prefix]
        actual = enabled(late)
        expected = {site: frozenset((output,))}
        if actual != expected:
            late_failures.append((prefix, expected, actual))
            break
        late[site] = output
    next_site, next_output = long_rail[101 * 12]
    check(
        "D02 late control reaches 101 slices with 1,598 terminal records",
        not late_failures
        and len(late) == 1_598
        and enabled(late) == {next_site: frozenset((next_output,))},
        str(late_failures[:1]),
    )

    covariance_failures = []
    controls = 0
    for local, values in FULL_RAW.items():
        for rotation in c53.ROTATIONS:
            controls += 1
            if FULL_RAW.get(c53.rotate_signature(local, rotation)) != values:
                covariance_failures.append((local, rotation, values))
                break
    check(
        "D03 all 220,944 proper-cubic raw-image checks preserve output",
        controls == len(FULL_RAW) * 24 == 220_944
        and not covariance_failures,
        str(covariance_failures[:1]),
    )

    shift = (211, -149, 127)
    rotated_failures = []
    for rotation in c53.ROTATIONS:
        transformed = c105.transform_records(records, rotation, shift)
        rotated_next = c101.transform_site(c105.RAIL_SEQUENCE[96][0], rotation, shift)
        expected = {rotated_next: frozenset((c105.RAIL_SEQUENCE[96][1],))}
        if enabled(transformed) != expected:
            rotated_failures.append((rotation, expected, enabled(transformed)))
            break
    check(
        "D04 every rotated completed history exposes only rotated next rail",
        not rotated_failures,
        str(rotated_failures[:1]),
    )


def scope_contract() -> None:
    section("E - Exact bounded scope and N1-N8 discipline")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check(
        "E01 note names exact bounded campaign construction",
        "c129_two_parent_corner_relocated_cage_seed" in note,
    )
    check(
        "E02 note preserves cage/launch-seed scope",
        "cage/launch seed" in note,
    )
    check(
        "E03 note denies word, writer, and recurrence claims",
        "not an r_b01 word" in note
        and "not an r_b01 writer" in note
        and "not a recurrence theorem" in note,
    )
    check(
        "E04 note carries refreshed N1-N8 discipline",
        all(f"n{index}" in note for index in range(1, 9)),
    )
    check(
        "E05 note names rejected R_C12 role without inheriting it",
        "rejected r_c12" in note,
    )
    check(
        "E06 note makes no axiom addition",
        "no axiom addition follows" in note,
    )
    check(
        "E07 Cycle 132 writes runner and review note only",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    table_contract()
    graph_contract()
    causal_contract()
    rail_and_covariance_contract()
    scope_contract()
    print(
        f"\nCAGE_CANONICAL={len(CAGE_TABLE)} CAGE_RAW={len(CAGE_RAW)} "
        f"UNION_RAW={len(FULL_RAW)} OUTPUTS={len(GROWN_OUTPUTS)}"
    )
    print(
        f"FACTOR={FACTOR.states}/{FACTOR.edges} "
        f"FULL={POSITIVE.states}/{POSITIVE.edges} "
        f"REJECTED_UNEXPECTED={len(REJECTED_COMPILED.unexpected_targets)}"
    )
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT=C129_TWO_PARENT_CORNER_RELOCATED_CAGE_SEED"
        if FAIL == 0
        else "RESULT=FAIL"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
