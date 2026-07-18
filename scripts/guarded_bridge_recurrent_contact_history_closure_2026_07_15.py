#!/usr/bin/env python3
"""Close exact schedule variants at the guarded bridge/recurrent contact.

The fresh-shell bridge and recurrent rail first touch at adjacent JOINT and
T_H3 records.  Whenever the exact compiled graph exposes a noncommuting pair,
add only the two observed enlarged local conditions with their already-fixed
outputs, then rerun the entire post-prefix graph.  Wrong writes, raw conflicts,
dead states, or an unbounded variant cascade reject the route.

Scratch only; no retained or foundation surface changes.
"""

from __future__ import annotations

import guarded_cycle129_bridge_history_probe_2026_07_15 as base


c141 = base.c141
c53 = base.c53
cell = base.cell


def raw_from(table):
    extension = c141.replacement_probe.merge_raw(*(
        cell.raw_orbit(signature, output)
        for signature, output in table.items()
    ))
    return c141.replacement_probe.merge_raw(base.prefix.FULL_RAW, extension)


def records_at(state, index):
    records = dict(base.FACTOR_SOURCE)
    records.update({
        site: base.FACTOR_OUTPUTS[site]
        for site, bit in index.items()
        if state >> bit & 1
    })
    return records


def add_variant(table, records, target):
    output = base.FACTOR_OUTPUTS[target]
    local = c53.local_signature(records, target)
    if not local:
        return False, ("empty", target)
    canonical = cell.canonical(local)
    inherited = base.prefix.FULL_RAW.get(local)
    if inherited is not None and inherited != frozenset((output,)):
        return False, ("base-conflict", target, local, inherited, output)
    prior = table.get(canonical)
    if prior is not None and prior != output:
        return False, ("table-conflict", target, canonical, prior, output)
    if prior == output or inherited == frozenset((output,)):
        return False, ("already-present", target, local, output)
    table[canonical] = output
    return True, (target, output, local)


def main():
    table = dict(base.TABLE)
    added = []
    for iteration in range(24):
        raw = raw_from(table)
        conflicts = tuple(
            (local, values) for local, values in raw.items() if len(values) != 1
        )
        if conflicts:
            print("CONFLICT", conflicts[:3])
            break
        graph = base.compiled_exact_graph(
            base.FACTOR_SOURCE,
            base.FACTOR_OUTPUTS,
            raw,
            base.prefix.payload.IGNORED,
            state_limit=5_000_000,
        )
        print(
            "ITER", iteration, "ROWS", len(table), "RAW", len(raw),
            "GRAPH", graph["states"], graph["edges"], graph["terminals"],
            graph["max_frontier"], "BAD", graph["bad"][:2],
            "REACHED", len(graph["reached"]),
        )
        if not graph["bad"]:
            print("ADDED", added)
            print("RESULT GUARDED_BRIDGE_RECURRENT_HISTORY_CLOSED")
            return
        failure = graph["failure"]
        if failure is None or failure[0] != "diamond":
            if failure and len(failure) > 1 and isinstance(failure[1], int):
                records = records_at(failure[1], graph["index"])
                print("FAILURE_LOCALS")
                for target in base.FACTOR_OUTPUTS:
                    bit = graph["index"][target]
                    if not (failure[1] >> bit & 1):
                        local = c53.local_signature(records, target)
                        if local:
                            print(target, base.FACTOR_OUTPUTS[target], local, raw.get(local))
            break
        _, state, left_index, left_target, right_index, right_target = failure
        records = records_at(state, graph["index"])
        repairs = []
        for written_index, written_target, target in (
            (left_index, left_target, right_target),
            (right_index, right_target, left_target),
        ):
            after = {**records, written_target: base.FACTOR_OUTPUTS[written_target]}
            okay, detail = add_variant(table, after, target)
            print("DIAMOND_VARIANT", written_target, "THEN", target, okay, detail)
            if okay:
                repairs.append(detail)
            elif detail[0] != "already-present":
                print("ADDED", added)
                print("RESULT HISTORY_CLOSURE_REJECTED")
                return
        if not repairs:
            print("NO_NEW_REPAIR")
            break
        added.extend(repairs)
    print("ADDED", added)
    print("RESULT HISTORY_CLOSURE_REJECTED")


if __name__ == "__main__":
    main()
