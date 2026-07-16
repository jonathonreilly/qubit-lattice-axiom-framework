#!/usr/bin/env python3
"""Find parent roles with no reachable unary opening before the byte bind.

Terminal-only absence missed a transient J3 opening in the proven physical
writer.  This census exhausts the 249,192 physical-prefix states and the
2,240 recurrent-payload states, then evaluates every covariant unary local
condition against those exact reachable masks.  A role is clean only when no
open target ever has that role as its sole written neighbour in either factor.

Scratch only; no retained or foundation surface changes.
"""

from __future__ import annotations

from collections import deque

import physical_r_b01_safe_prefix_history_probe_2026_07_15 as physical


p = physical.p
c112 = physical.c112
c141 = physical.c141
cell = p.cell
payload = p.payload


def reachable_states(source, outputs, raw, ignored, state_limit=1_000_000):
    compiled = c112.compile_conditions(source, outputs, raw, ignored)
    actions = tuple(
        (compiled.index.get(target), target, conditions)
        for target, conditions in compiled.conditions.items()
    )
    queue = deque((0,))
    seen = {0}
    bad = []
    edges = 0
    terminals = []
    while queue:
        state = queue.popleft()
        legal = []
        for index, target, conditions in actions:
            if index is not None and state >> index & 1:
                continue
            for present, neighbourhood, values in conditions:
                if state & neighbourhood != present:
                    continue
                if target in ignored and values == ignored[target]:
                    break
                if index is not None and values == frozenset((outputs[target],)):
                    legal.append(index)
                    break
                bad.append((state, target, values))
                break
            if bad:
                break
        if bad:
            break
        if not legal:
            terminals.append(state)
        for index in legal:
            future = state | 1 << index
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)
                if len(seen) > state_limit:
                    bad.append(("state-limit", state_limit))
                    queue.clear()
                    break
    return compiled, frozenset(seen), edges, tuple(terminals), tuple(bad)


def unary_table():
    table = {}
    for role in cell.FULL_ROLES:
        canonical = cell.canonical((((1, 0, 0), role),))
        for signature in cell.raw_orbit(canonical, role):
            prior = table.get(signature)
            if prior is not None and prior != frozenset((role,)):
                raise RuntimeError((signature, prior, role))
            table[signature] = frozenset((role,))
    return table


UNARY_RAW = unary_table()


def reachable_unary_events(source, outputs, states):
    compiled = c112.compile_conditions(source, outputs, UNARY_RAW, {})
    projections = {}

    def reachable(mask, desired):
        values = projections.get(mask)
        if values is None:
            values = {state & mask for state in states}
            projections[mask] = values
        return desired in values

    events = []
    for target, conditions in compiled.conditions.items():
        target_bit = (
            1 << compiled.index[target] if target in compiled.index else 0
        )
        for present, neighbourhood, values in conditions:
            if len(values) != 1:
                raise RuntimeError((target, values))
            role = next(iter(values))
            mask = neighbourhood | target_bit
            if reachable(mask, present):
                events.append((
                    role,
                    target,
                    outputs.get(target),
                    present,
                    neighbourhood,
                ))
    return tuple(events), len(projections)


def main():
    physical_graph = reachable_states(
        c112.SOURCE,
        physical.OUTPUTS,
        physical.RAW,
        c112.RAIL_ZERO,
    )
    p_compiled, p_states, p_edges, p_terminals, p_bad = physical_graph
    print(
        "PHYSICAL_GRAPH", len(p_states), p_edges, len(p_terminals),
        tuple(sorted({state.bit_count() for state in p_terminals})), p_bad,
    )
    recurrent_graph = reachable_states(
        c141.BASE,
        payload.OUTPUTS,
        payload.FULL_RAW,
        payload.IGNORED,
    )
    r_compiled, r_states, r_edges, r_terminals, r_bad = recurrent_graph
    print(
        "RECURRENT_GRAPH", len(r_states), r_edges, len(r_terminals),
        tuple(sorted({state.bit_count() for state in r_terminals})), r_bad,
    )

    physical_events, physical_projections = reachable_unary_events(
        c112.SOURCE, physical.OUTPUTS, p_states
    )
    recurrent_events, recurrent_projections = reachable_unary_events(
        c141.BASE, payload.OUTPUTS, r_states
    )
    physical_roles = {item[0] for item in physical_events}
    recurrent_roles = {item[0] for item in recurrent_events}
    clean = tuple(sorted(
        cell.FULL_ROLES - physical_roles - recurrent_roles
    ))
    print(
        "EVENTS", len(physical_events), len(recurrent_events),
        "PROJECTIONS", physical_projections, recurrent_projections,
    )
    print("PHYSICAL_EVENT_ROLES", len(physical_roles), tuple(sorted(physical_roles)))
    print("RECURRENT_EVENT_ROLES", len(recurrent_roles), tuple(sorted(recurrent_roles)))
    print("CLEAN_ROLES", len(clean), clean)
    for role in ("J3", "J6", "R_A13", "R_C13", "R_C40"):
        samples = tuple(
            item for item in (*physical_events, *recurrent_events)
            if item[0] == role
        )[:5]
        print("ROLE", role, "EVENTS", samples)
    success = (
        len(p_states) == 249_192
        and len(p_terminals) == 1
        and not p_bad
        and len(r_states) == 2_240
        and len(r_terminals) == 1
        and not r_bad
        and "J3" not in clean
        and bool(clean)
    )
    print("RESULT", "EXACT_PREBIND_UNARY_CLEAN_ROLES" if success else "UNARY_CENSUS_REJECTED")


if __name__ == "__main__":
    main()
