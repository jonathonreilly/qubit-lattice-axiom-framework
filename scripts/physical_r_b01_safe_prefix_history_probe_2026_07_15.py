#!/usr/bin/env python3
"""Exhaust the physical R_B01 writer plus its six-record safe bridge prefix.

This isolates the word/writer and allocator/port/OZ/W3/A_0_0/A_1_2 rows from
the independent recurrent rail.  It tests whether the intended-order prefix
used by the guard searches is itself valid under every asynchronous history.

Scratch only; no retained or foundation surface changes.
"""

from __future__ import annotations

import physical_r_b01_generation3_safe_prefix_scratch_2026_07_15 as p


w = p.word
c112 = p.c112
c141 = p.c141
OUTPUTS = {**w.GROWN_OUTPUTS, **p.PREFIX_OUTPUTS}
RAW = c141.replacement_probe.merge_raw(w.FULL_RAW, p.NEW_RAW)


def main():
    compiled = c112.compile_conditions(
        c112.SOURCE, OUTPUTS, RAW, c112.RAIL_ZERO
    )
    print(
        "STATIC", len(OUTPUTS), len(RAW),
        sum(len(values) != 1 for values in RAW.values()),
        len(compiled.unexpected_targets),
        tuple(sorted(compiled.unexpected_targets))[:12],
    )
    graph = c112.append_graph(
        c112.SOURCE,
        OUTPUTS,
        raw=RAW,
        ignored=c112.RAIL_ZERO,
        state_limit=5_000_000,
    )
    print(
        "GRAPH", graph.states, graph.edges, graph.terminals,
        graph.terminal_sizes, graph.max_frontier,
        len(graph.bad), graph.bad[:3], len(graph.reached),
    )
    success = (
        all(len(values) == 1 for values in RAW.values())
        and not compiled.unexpected_targets
        and graph.terminals == 1
        and not graph.bad
        and len(graph.reached) == len(OUTPUTS)
    )
    print("RESULT", "PHYSICAL_R_B01_SAFE_PREFIX_HISTORY" if success else "SAFE_PREFIX_REJECTED")


if __name__ == "__main__":
    main()
