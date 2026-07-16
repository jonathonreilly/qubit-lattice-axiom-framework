#!/usr/bin/env python3
"""Retarget the proven Cycle-121 writer from R_B00 to R_B01.

Only D7 changes from H0 to H1, making 10010001, and the completion output
changes from R_B00 to R_B01.  All cage geometry and causal ordering remain
the proven Cycle-121 construction.  The full compiler and append graph decide
whether that minimal retarget is safe.

Exploratory only; no foundation, registry, policy, audit, or git authority.
"""

from __future__ import annotations

import r_b00_port_to_zero_source_word_completion_cycle121_2026_07_15 as c121


c119 = c121.c119
c112 = c121.c112
c53 = c121.c53
c59 = c121.c59
H0 = c121.H0
H1 = c121.H1
WORD = (1, 0, 0, 1, 0, 0, 0, 1)
DATA_OUTPUTS = tuple(H1 if bit else H0 for bit in WORD)
DATA_RECORDS = tuple(zip(c121.DATA_SITES, DATA_OUTPUTS))
COMPLETION_OUTPUT = "R_B01"


def build_table():
    records = c119.positive_terminal_records()
    table = {}
    sequence = (
        DATA_RECORDS[0],
        DATA_RECORDS[1],
        (c121.FRONT, c121.FRONT_OUTPUT),
        DATA_RECORDS[2],
        DATA_RECORDS[3],
        DATA_RECORDS[4],
        (c121.TAIL, c121.TAIL_OUTPUT),
        (c121.MID, c121.MID_OUTPUT),
        DATA_RECORDS[5],
    )
    for site, output in sequence:
        c121.add_canonical(table, records, site, output)
        records[site] = output
    inherited_local = c53.local_signature(records, c121.INHERITED)
    inherited_values = c119.FULL_RAW.get(inherited_local)
    records[c121.INHERITED] = c121.INHERITED_OUTPUT
    for site, output in (
        DATA_RECORDS[7],
        DATA_RECORDS[6],
        (c121.JOIN, c121.JOIN_OUTPUT),
    ):
        c121.add_canonical(table, records, site, output)
        records[site] = output
    completion_local = c53.local_signature(records, c121.COMPLETION)
    completion_canonical = c53.canonical_signature(completion_local)
    return table, records, inherited_local, inherited_values, completion_local, completion_canonical


(
    WRITER_TABLE,
    PRE_COMPLETION,
    INHERITED_LOCAL,
    INHERITED_VALUES,
    COMPLETION_LOCAL,
    COMPLETION_CANONICAL,
) = build_table()
WRITER_RAW = c59.raw_rule_outputs(WRITER_TABLE)
COMPLETION_RAW = c59.raw_rule_outputs({COMPLETION_CANONICAL: COMPLETION_OUTPUT})
FULL_RAW = c112.merge_raw(c119.FULL_RAW, WRITER_RAW, COMPLETION_RAW)
OUTPUTS = {
    **dict(DATA_RECORDS),
    **dict(c121.CAGE_RECORDS),
    c121.INHERITED: c121.INHERITED_OUTPUT,
    c121.COMPLETION: COMPLETION_OUTPUT,
}
GROWN_OUTPUTS = {**c119.GROWN_OUTPUTS, **OUTPUTS}
COMPILED = c112.compile_conditions(
    c112.SOURCE, GROWN_OUTPUTS, FULL_RAW, c112.RAIL_ZERO
)


def main() -> None:
    print("WORD", WORD)
    print("INHERITED", INHERITED_LOCAL, INHERITED_VALUES)
    print("COMPLETION_LOCAL", COMPLETION_LOCAL)
    print("TABLE", len(WRITER_TABLE), len(WRITER_RAW), len(COMPLETION_RAW), len(FULL_RAW))
    conflicts = tuple(
        (local, values)
        for local, values in FULL_RAW.items()
        if len(values) != 1
    )
    print("CONFLICTS", len(conflicts), conflicts[:5])
    print("UNEXPECTED", len(COMPILED.unexpected_targets), tuple(sorted(COMPILED.unexpected_targets))[:12])
    wrong = c121.c112.compile_conditions(
        c112.SOURCE, GROWN_OUTPUTS, FULL_RAW, c112.RAIL_ZERO
    )
    if conflicts or COMPILED.unexpected_targets:
        print("RESULT STATIC_RETARGET_REJECTED")
        return
    stats = c112.append_graph(
        c112.SOURCE,
        GROWN_OUTPUTS,
        raw=FULL_RAW,
        ignored=c112.RAIL_ZERO,
        state_limit=2_000_000,
    )
    print(
        "GRAPH", stats.states, stats.edges, stats.terminals,
        stats.terminal_sizes, stats.max_frontier,
        len(stats.bad), len(stats.reached),
    )
    print("BAD", stats.bad[:3])
    print(
        "RESULT",
        "RETARGETED_R_B01_WORD_COMPLETION"
        if stats.terminals == 1
        and not stats.bad
        and len(stats.reached) == len(GROWN_OUTPUTS)
        else "GRAPH_RETARGET_REJECTED",
    )


if __name__ == "__main__":
    main()
