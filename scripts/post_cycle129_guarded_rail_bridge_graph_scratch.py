#!/usr/bin/env python3
"""Exact factor/full-history scratch for a two-parent guarded C129 bridge."""

from __future__ import annotations

import post_cycle124_rail_attached_head_cycle122_graph_scratch as old


c124 = old.c124
c112 = old.c112
c105 = old.c105
c59 = old.c59
c53 = old.c53
RAIL = old.RAIL
RAIL_OUTPUTS = old.RAIL_OUTPUTS
GROUPS = (
    *old.GROUPS[:12],
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
    locals_seen = []
    for declared, output in GROUPS:
        local = c53.local_signature(records, declared[0])
        canonical = c53.canonical_signature(local)
        matches = tuple(sorted(
            site
            for site in c53.open_candidates(records)
            if c53.canonical_signature(c53.local_signature(records, site)) == canonical
        ))
        if matches != tuple(sorted(declared)):
            raise RuntimeError((declared, matches, local, canonical))
        prior = table.get(canonical)
        if prior is not None and prior != output:
            raise RuntimeError((canonical, prior, output))
        table[canonical] = output
        records.update({site: output for site in matches})
        observed.append(matches)
        locals_seen.append(local)
    return table, tuple(observed), tuple(locals_seen)


def summarize(label, source, outputs, union, ignored):
    compiled = c112.compile_conditions(source, outputs, union, ignored)
    print(label, "COMPILED", len(compiled.conditions), tuple(sorted(compiled.unexpected_targets)))
    stats = c112.append_graph(
        source=source,
        outputs=outputs,
        raw=union,
        ignored=ignored,
        state_limit=8_000_000,
    )
    print(
        label,
        "GRAPH",
        stats.states,
        stats.edges,
        stats.terminals,
        stats.terminal_sizes,
        stats.max_frontier,
        stats.bad,
        tuple(sorted(stats.unexpected_condition_targets)),
        len(stats.reached),
    )
    return stats


def main() -> None:
    table, observed, locals_seen = build_table()
    raw = c59.raw_rule_outputs(table)
    union = c112.merge_raw(c124.FULL_RAW, raw)
    print(
        "TABLE",
        len(table),
        "RAW",
        len(raw),
        "UNION",
        len(union),
        "SINGLE",
        all(len(values) == 1 for values in union.values()),
        "BRIDGE",
        len(BRIDGE_OUTPUTS),
    )
    print("GROUPS", observed)
    print("GUARD_LOCAL", locals_seen[12], "JOINT_LOCAL", locals_seen[13])
    outputs = {**RAIL_OUTPUTS, **BRIDGE_OUTPUTS}
    ignored = {c105.RAIL_SEQUENCE[12][0]: frozenset((c105.RAIL_SEQUENCE[12][1],))}
    summarize("FACTOR", c124.positive_terminal_records(), outputs, union, ignored)
    full_outputs = {**c124.GROWN_OUTPUTS, **outputs}
    summarize("FULL", c112.SOURCE, full_outputs, union, ignored)


if __name__ == "__main__":
    main()
