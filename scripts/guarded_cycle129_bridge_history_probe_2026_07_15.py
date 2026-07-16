#!/usr/bin/env python3
"""History-screen the fresh-shell repair through the old JOINT bridge.

The repair uses a unique A_0_0+OZ seed (J3), its previously absent unary
continuation (two J2 copies), and a two-copy J6 corner row.  The near J6 copy
guards the former unary W3 -> A_2_0 step; the far copies are explicit members
of the same proper-cubic local conditions.  The remaining Cycle-129 geometry
is then rebuilt through JOINT.

Scratch only; no retained or foundation surface changes.
"""

from __future__ import annotations

from collections import Counter, deque
from itertools import combinations

import physical_r_b01_generation3_safe_prefix_scratch_2026_07_15 as prefix
import recurrent_socket_to_cycle129_downstream_interface_probe_2026_07_15 as old


c141 = prefix.c141
c112 = prefix.c112
c53 = prefix.c53
cell = prefix.cell
screen = prefix.payload.screen
SHELL_GROUPS = (
    (((5, 2, -3),), "J6"),
    (((5, 2, -4), (6, 2, -3)), "J2"),
    (((5, 3, -4), (6, 3, -3)), "R_A13"),
)
BRIDGE_GROUPS = (*SHELL_GROUPS, *old.GROUPS[4:14])


def raw_matches(records, raw):
    return tuple(sorted(
        target
        for target in c53.open_candidates(records)
        if c53.local_signature(records, target) in raw
    ))


def build():
    records = dict(prefix.RECORDS)
    table = {}
    observed = []
    outputs = {}
    for sites, output in BRIDGE_GROUPS:
        local = c53.local_signature(records, sites[0])
        canonical = cell.canonical(local)
        prior = table.get(canonical)
        if prior is not None and prior != output:
            raise RuntimeError((sites, canonical, prior, output))
        table[canonical] = output
        raw = cell.raw_orbit(local, output)
        matches = raw_matches(records, raw)
        observed.append((sites, matches, local, output))
        for site in sites:
            if site in records and records[site] != output:
                raise RuntimeError((site, records[site], output))
            records[site] = output
            outputs[site] = output
    extension = c141.replacement_probe.merge_raw(*(
        cell.raw_orbit(signature, output)
        for signature, output in table.items()
    ))
    full_raw = c141.replacement_probe.merge_raw(prefix.FULL_RAW, extension)
    return records, table, extension, full_raw, outputs, tuple(observed)


RECORDS, TABLE, EXTENSION_RAW, FULL_RAW, OUTPUTS, OBSERVED = build()
FACTOR_SOURCE = dict(prefix.RECORDS)
FACTOR_OUTPUTS = {**prefix.payload.OUTPUTS, **OUTPUTS}
COMBINED_OUTPUTS = {
    **prefix.COMBINED_OUTPUTS,
    **OUTPUTS,
}


def compiled_exact_graph(source, outputs, raw, ignored, state_limit=5_000_000):
    """Exact append graph using precompiled six-neighbour mask conditions."""
    compiled = c112.compile_conditions(source, outputs, raw, ignored)
    actions = tuple(
        (compiled.index.get(target), target, conditions)
        for target, conditions in compiled.conditions.items()
    )
    sites = compiled.sites
    all_mask = (1 << len(sites)) - 1
    queue = deque((0,))
    seen = {0}
    edges = 0
    terminals = 0
    bad = []
    max_frontier = 0
    reached_mask = 0
    mandatory = {site: all_mask for site in sites}
    append_seen = Counter()
    diamond_pairs = 0
    diamond_failures = []
    failure = None

    def value_at(state, conditions):
        for present, neighbourhood, values in conditions:
            if state & neighbourhood == present:
                return values
        return None

    while queue:
        state = queue.popleft()
        reached_mask |= state
        legal = []
        wrong = []
        for index, target, conditions in actions:
            if index is not None and state >> index & 1:
                continue
            values = value_at(state, conditions)
            if values is None:
                continue
            if target in ignored and values == ignored[target]:
                continue
            if index is not None and values == frozenset((outputs[target],)):
                legal.append((index, target, conditions))
            else:
                wrong.append((target, values))
        if wrong:
            bad.append((state.bit_count(), tuple(sorted(wrong))))
            failure = ("wrong", state, tuple(sorted(wrong)))
            break
        if state == all_mask:
            terminals += 1
            continue
        if not legal:
            bad.append((state.bit_count(), "dead"))
            failure = ("dead", state)
            break
        max_frontier = max(max_frontier, len(legal))
        for left, right in combinations(legal, 2):
            diamond_pairs += 1
            left_index, left_target, _left_conditions = left
            right_index, right_target, right_conditions = right
            after_left = state | 1 << left_index
            after_right = state | 1 << right_index
            if (
                value_at(after_left, right_conditions)
                != frozenset((outputs[right_target],))
                or value_at(after_right, left[2])
                != frozenset((outputs[left_target],))
            ):
                diamond_failures.append((state.bit_count(), left_target, right_target))
                bad.append((state.bit_count(), "diamond", left_target, right_target))
                failure = (
                    "diamond", state, left_index, left_target,
                    right_index, right_target,
                )
                queue.clear()
                break
        if bad:
            break
        for index, target, _conditions in legal:
            mandatory[target] &= state
            append_seen[target] += 1
            future = state | 1 << index
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)
                if len(seen) > state_limit:
                    bad.append(("state-limit", state_limit))
                    failure = ("state-limit", state_limit)
                    queue.clear()
                    break
    reached = frozenset(
        site for site, bit in compiled.index.items() if reached_mask >> bit & 1
    )
    return {
        "states": len(seen), "edges": edges, "terminals": terminals,
        "bad": tuple(bad), "max_frontier": max_frontier,
        "mandatory": mandatory, "append_seen": append_seen,
        "diamond_pairs": diamond_pairs,
        "diamond_failures": tuple(diamond_failures), "reached": reached,
        "index": compiled.index, "failure": failure,
    }


def main():
    mismatches = tuple(
        (index, declared, matches, local, output)
        for index, (declared, matches, local, output) in enumerate(OBSERVED)
        if tuple(sorted(declared)) != matches
    )
    print("CONSTRUCTION")
    print("GROUPS", len(BRIDGE_GROUPS), "OUTPUTS", len(OUTPUTS))
    print("TABLE", len(TABLE), "EXTENSION_RAW", len(EXTENSION_RAW), "FULL_RAW", len(FULL_RAW))
    print("MISMATCHES", len(mismatches), mismatches[:3])
    print("MULTI", sum(len(values) != 1 for values in FULL_RAW.values()))
    for index, item in enumerate(OBSERVED[:4]):
        print("REPAIR", index, item)

    print("\nCONDITIONAL FACTOR")
    graph = compiled_exact_graph(
        FACTOR_SOURCE,
        FACTOR_OUTPUTS,
        FULL_RAW,
        prefix.payload.IGNORED,
    )
    print("GRAPH", {
        key: graph[key] for key in (
            "states", "edges", "terminals", "max_frontier", "diamond_pairs"
        )
    })
    print("BAD", graph["bad"][:3], "REACHED", len(graph["reached"]))
    print("DIAMOND_FAILURES", graph["diamond_failures"][:3])

    print("\nWHOLE-HISTORY STATIC SCREEN")
    compiled = c112.compile_conditions(
        c112.SOURCE,
        COMBINED_OUTPUTS,
        FULL_RAW,
        prefix.payload.IGNORED,
    )
    wrong = set(screen.wrong_value_details(
        compiled, COMBINED_OUTPUTS, prefix.payload.IGNORED
    ))
    baseline = c112.compile_conditions(
        c112.SOURCE,
        prefix.COMBINED_OUTPUTS,
        prefix.FULL_RAW,
        prefix.payload.IGNORED,
    )
    baseline_wrong = set(screen.wrong_value_details(
        baseline, prefix.COMBINED_OUTPUTS, prefix.payload.IGNORED
    ))
    new_wrong = tuple(sorted(wrong - baseline_wrong))
    new_unexpected = tuple(sorted(
        set(compiled.unexpected_targets) - set(baseline.unexpected_targets)
    ))
    print("UNEXPECTED", len(compiled.unexpected_targets), "NEW", new_unexpected)
    print("WRONG", len(wrong), "NEW", len(new_wrong), new_wrong[:5])

    reachability = c112.append_graph(
        c112.SOURCE,
        COMBINED_OUTPUTS,
        raw=FULL_RAW,
        ignored=prefix.payload.IGNORED,
        state_limit=2_000_000,
    )
    print(
        "WHOLE_GRAPH",
        reachability.states, reachability.edges, reachability.terminals,
        reachability.max_frontier, reachability.bad[:2],
        len(reachability.reached),
    )

    terminal = {**c112.SOURCE, **COMBINED_OUTPUTS}
    enabled = c141.enabled(terminal, FULL_RAW)
    print("TERMINAL_ENABLED", enabled)
    success = (
        not mismatches
        and all(len(values) == 1 for values in FULL_RAW.values())
        and graph["terminals"] == 1
        and not graph["bad"]
        and not graph["diamond_failures"]
        and len(graph["reached"]) == len(FACTOR_OUTPUTS)
        and not new_unexpected
        and not new_wrong
        and not reachability.bad
        and enabled == prefix.payload.IGNORED
    )
    print("RESULT", "FRESH_SHELL_GUARDED_BYTE_TO_JOINT" if success else "GUARDED_HISTORY_REJECTED")


if __name__ == "__main__":
    main()
