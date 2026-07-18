#!/usr/bin/env python3
"""Exact-history scratch check for the C124-to-rail grouped bridge."""

from __future__ import annotations

import r_b00_completion_to_r_b01_role_allocator_common_port_cycle124_2026_07_15 as c124


c112 = c124.c112
c105 = c124.c105
c59 = c124.c59
c53 = c124.c53
RAIL = tuple(c105.RAIL_SEQUENCE[:12])
RAIL_OUTPUTS = dict(RAIL)
GROUPS: tuple[tuple[tuple[tuple[int, int, int], ...], str], ...] = (
    (((5, 3, -3),), "OZ"),
    (((4, 3, -3),), "W3"),
    (((4, 2, -3),), "A_0_0"),
    (((3, 2, -3),), "A_1_2"),
    (((4, 3, -4),), "A_2_0"),
    (((4, 2, -4),), "A_3_1"),
    (((3, 2, -4),), "A_3_2"),
    (((2, 2, -4),), "COMPLETE"),
    (((1, 2, -4), (2, 3, -4)), "TY"),
    (((0, 2, -4),), "W4"),
    (((0, 2, -3),), "AUXZ"),
    (((0, 2, -2),), "GU"),
    (((-1, 3, -2),), "R_C01"),
    (((-1, 2, -2),), "JOINT"),
    (((-1, 2, -1),), "T_N0"),
    (((-2, 2, -1),), "Y2"),
)
BRIDGE_OUTPUTS = {site: output for sites, output in GROUPS for site in sites}


def build_table():
    records = {**c124.positive_terminal_records(), **RAIL_OUTPUTS}
    table = {}
    observed = []
    for declared, output in GROUPS:
        canonical = c53.canonical_signature(c53.local_signature(records, declared[0]))
        matches = tuple(sorted(
            site
            for site in c53.open_candidates(records)
            if c53.canonical_signature(c53.local_signature(records, site)) == canonical
        ))
        if matches != tuple(sorted(declared)):
            raise RuntimeError((declared, matches, canonical))
        table[canonical] = output
        records.update({site: output for site in matches})
        observed.append(matches)
    return table, tuple(observed)


def main() -> None:
    table, observed = build_table()
    raw = c59.raw_rule_outputs(table)
    union = c112.merge_raw(c124.FULL_RAW, raw)
    source = c124.positive_terminal_records()
    outputs = {**RAIL_OUTPUTS, **BRIDGE_OUTPUTS}
    ignored = {c105.RAIL_SEQUENCE[12][0]: frozenset((c105.RAIL_SEQUENCE[12][1],))}
    compiled = c112.compile_conditions(source, outputs, union, ignored)
    print(
        "TABLE", len(table), "RAW", len(raw), "UNION", len(union),
        "BRIDGE", len(BRIDGE_OUTPUTS), "OUTPUTS", len(outputs),
        "UNEXPECTED", tuple(sorted(compiled.unexpected_targets)),
    )
    print("GROUPS", observed)
    stats = c112.append_graph(
        source=source,
        outputs=outputs,
        raw=union,
        ignored=ignored,
        state_limit=8_000_000,
    )
    print(
        "GRAPH", stats.states, stats.edges, stats.terminals,
        stats.terminal_sizes, stats.max_frontier, stats.bad,
        tuple(sorted(stats.unexpected_condition_targets)), len(stats.reached),
    )
    print("TERMINAL_STATES", stats.terminal_states[:8])
    print("MISSING", tuple(sorted(set(outputs) - stats.reached)))
    full_outputs = {**c124.GROWN_OUTPUTS, **outputs}
    full_compiled = c112.compile_conditions(c112.SOURCE, full_outputs, union, ignored)
    print("FULL_COMPILED_UNEXPECTED", tuple(sorted(full_compiled.unexpected_targets)))
    full = c112.append_graph(
        source=c112.SOURCE,
        outputs=full_outputs,
        raw=union,
        ignored=ignored,
        state_limit=8_000_000,
    )
    print(
        "FULL_GRAPH", full.states, full.edges, full.terminals,
        full.terminal_sizes, full.max_frontier, full.bad,
        tuple(sorted(full.unexpected_condition_targets)), len(full.reached),
    )


if __name__ == "__main__":
    main()
