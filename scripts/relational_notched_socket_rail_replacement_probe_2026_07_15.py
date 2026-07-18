#!/usr/bin/env python3
"""Test the notched recurrent cell as a replacement for the old rail law."""

from __future__ import annotations

import post_cycle131_outward_adapter_search_scratch as live
import relational_notched_rail_socket_prototype_2026_07_15 as cell
import relational_periodic_socket_emitter_search_scratch_2026_07_15 as details


def subtract_raw(table, removed):
    answer = {}
    for signature, values in table.items():
        remaining = values - removed.get(signature, frozenset())
        if remaining:
            answer[signature] = remaining
    return answer


def merge_raw(*tables):
    answer = {}
    for table in tables:
        for signature, values in table.items():
            answer[signature] = answer.get(signature, frozenset()) | values
    return answer


def main() -> None:
    c112 = live.c112
    old_rail = live.c105.REMAPPED_RAW
    core = subtract_raw(c112.FULL_RAW, old_rail)
    replacement = merge_raw(core, cell.RAW)
    core_input_roles = frozenset(
        value
        for signature in core
        for _direction, value in signature
    )
    extra_candidates = (
        cell.FULL_ROLES
        - cell.RECT_CONTENTS
        - {cell.H0, cell.H1, cell.OZ, "R_B01", "BACKSTOP"}
    )
    inert_roles = tuple(sorted(extra_candidates - core_input_roles))
    conflicts = tuple(sorted(
        (signature, values)
        for signature, values in replacement.items()
        if len(values) != 1
    ))
    print(
        "RAW_COUNTS",
        "C112", len(c112.FULL_RAW),
        "OLD_RAIL", len(old_rail),
        "CORE", len(core),
        "CELL", len(cell.RAW),
        "REPLACEMENT", len(replacement),
    )
    print("CONFLICTS", len(conflicts))
    print("CORE_INPUT_ROLES", len(core_input_roles))
    print("EXTRA_CANDIDATES", len(extra_candidates))
    print("INERT_ROLES", len(inert_roles), inert_roles)
    for item in conflicts[:80]:
        print("CONFLICT", item)
    if conflicts:
        return

    # First require the non-rail compiler corpus to remain internally valid.
    core_compiled = c112.compile_conditions(
        c112.SOURCE,
        c112.GROWN_OUTPUTS,
        core,
        {},
    )
    core_wrong = details.wrong_value_details(core_compiled, c112.GROWN_OUTPUTS, {})
    print("CORE_UNEXPECTED", tuple(sorted(core_compiled.unexpected_targets)))
    print("CORE_WRONG", len(core_wrong), core_wrong[:40])
    core_graph = c112.append_graph(
        source=c112.SOURCE,
        outputs=c112.GROWN_OUTPUTS,
        raw=core,
        ignored={},
        state_limit=8_000_000,
    )
    print(
        "CORE_GRAPH",
        core_graph.states,
        core_graph.edges,
        core_graph.terminals,
        core_graph.terminal_sizes,
        core_graph.max_frontier,
        core_graph.bad,
        tuple(sorted(core_graph.unexpected_condition_targets)),
        len(core_graph.reached),
    )
    replacement_core_compiled = c112.compile_conditions(
        c112.SOURCE,
        c112.GROWN_OUTPUTS,
        replacement,
        c112.RAIL_ZERO,
    )
    replacement_core_wrong = details.wrong_value_details(
        replacement_core_compiled, c112.GROWN_OUTPUTS, c112.RAIL_ZERO
    )
    print(
        "CORE_REPLACEMENT_UNEXPECTED",
        tuple(sorted(replacement_core_compiled.unexpected_targets)),
    )
    print(
        "CORE_REPLACEMENT_WRONG_DELTA",
        len(set(replacement_core_wrong) - set(core_wrong)),
        tuple(sorted(set(replacement_core_wrong) - set(core_wrong)))[:80],
    )
    replacement_core_graph = c112.append_graph(
        source=c112.SOURCE,
        outputs=c112.GROWN_OUTPUTS,
        raw=replacement,
        ignored=c112.RAIL_ZERO,
        state_limit=8_000_000,
    )
    print(
        "CORE_REPLACEMENT_GRAPH",
        replacement_core_graph.states,
        replacement_core_graph.edges,
        replacement_core_graph.terminals,
        replacement_core_graph.terminal_sizes,
        replacement_core_graph.max_frontier,
        replacement_core_graph.bad,
        tuple(sorted(replacement_core_graph.unexpected_condition_targets)),
        len(replacement_core_graph.reached),
    )

    # Then run the recurrent cell under every retained non-rail rule.
    original_raw = cell.RAW
    cell.RAW = replacement
    identity = next(
        rotation
        for rotation in cell.c52.ROTATIONS
        if cell.c52.matvec(rotation, (2, 3, 5)) == (2, 3, 5)
    )
    graph = cell.graph(identity)
    cell.RAW = original_raw
    print("CELL_GRAPH", {
        key: value for key, value in graph.items() if key not in {"bad", "sockets"}
    })
    print("CELL_GRAPH_BAD", graph["bad"][:20])

    # Pre-graph all-subsets screen for the cell alone under the replacement.
    outputs, _sockets, ignored0 = cell.expected_outputs()
    ignored = {site: frozenset((value,)) for site, value in ignored0.items()}
    cell_only_compiled = c112.compile_conditions(
        cell.seed_records(), outputs, original_raw, ignored
    )
    cell_only_wrong = details.wrong_value_details(
        cell_only_compiled, outputs, ignored
    )
    compiled = c112.compile_conditions(cell.seed_records(), outputs, replacement, ignored)
    wrong = details.wrong_value_details(compiled, outputs, ignored)
    wrong_delta = tuple(sorted(set(wrong) - set(cell_only_wrong)))
    print("CELL_COMPILED", len(compiled.conditions))
    print(
        "CELL_ONLY_UNEXPECTED",
        tuple(sorted(cell_only_compiled.unexpected_targets)),
    )
    print("CELL_ONLY_WRONG", len(cell_only_wrong))
    print("CELL_UNEXPECTED", tuple(sorted(compiled.unexpected_targets)))
    print("CELL_WRONG", len(wrong))
    print("CELL_WRONG_DELTA", len(wrong_delta))
    for item in wrong_delta[:160]:
        print("CELL_WRONG_DELTA_DETAIL", item)


if __name__ == "__main__":
    main()
