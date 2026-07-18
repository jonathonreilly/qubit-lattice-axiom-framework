#!/usr/bin/env python3
"""Price the adapter from the retained rectangular rail seed to the notched rail.

The old phase-A rectangle starts the first three writes of the new B slice and
then stops.  Supplying exactly the missing A-lower tail record lets the fixed
notched grammar generate its own A guard, finish a startup partial socket, and
reach the first fully recurrent socket one period later.  The supplied lower
record is therefore an interface price, not a claimed solution.
"""

from __future__ import annotations

from collections import deque

import relational_notched_rail_socket_prototype_2026_07_15 as cell


def old_seed():
    records = {
        cell.site(0, yz): cell.CONTENT[("A", yz)]
        for yz in cell.RECT
    }
    records[cell.site(-1, cell.PORT_A)] = "BACKSTOP"
    return records


def forced_prefix(records):
    answer = []
    state = dict(records)
    while True:
        actual = cell.enabled(state)
        if len(actual) != 1:
            return tuple(answer), actual
        target, values = next(iter(actual.items()))
        value = next(iter(values))
        answer.append((target, value))
        state[target] = value


def adapter_outputs():
    outputs = {
        cell.site(0, cell.GUARD_YZ): cell.CONTENT[("A", cell.GUARD_YZ)]
    }
    old = "A"
    for x, new in zip(range(1, 6), ("B", "C", "D", "A", "B")):
        for yz in cell.PATHS[(old, new)]:
            outputs[cell.site(x, yz)] = cell.CONTENT[(new, yz)]
        for yz in cell.EXTRA_ORDERS[new]:
            outputs[cell.site(x, yz)] = cell.CONTENT[(new, yz)]
        old = new

    # The first A/B pair has no earlier D-root R_B01.  It lawfully writes the
    # helper and H1 but cannot write OZ.  The second A/B pair has the D root
    # produced at x=3 and therefore writes the first complete recurrent port.
    for bx in (1, 5):
        outputs[cell.site(bx, cell.NOTCH_YZ)] = cell.HELPER_CONTENT
        outputs[cell.site(bx - 1, cell.NOTCH_YZ)] = cell.H1
    outputs[cell.site(3, cell.NOTCH_YZ)] = cell.OZ
    first = cell.PATHS[("B", "C")][0]
    ignored = {
        cell.site(6, first): frozenset((cell.CONTENT[("C", first)],))
    }
    return outputs, ignored


def graph(source):
    outputs, ignored = adapter_outputs()
    sites = tuple(sorted(outputs))
    index = {site: bit for bit, site in enumerate(sites)}
    all_mask = (1 << len(sites)) - 1
    queue = deque((0,))
    seen = {0}
    edges = 0
    bad = []
    terminals = 0
    reached_mask = 0
    while queue:
        mask = queue.popleft()
        reached_mask |= mask
        records = dict(source)
        records.update({
            site: outputs[site]
            for site, bit in index.items()
            if mask >> bit & 1
        })
        actual = cell.enabled(records)
        wrong = {
            target: values
            for target, values in actual.items()
            if (
                target in outputs
                and values != frozenset((outputs[target],))
            ) or (
                target not in outputs
                and ignored.get(target) != values
            )
        }
        if wrong:
            bad.append((mask.bit_count(), tuple(sorted(wrong.items()))))
            continue
        if mask == all_mask:
            if actual == ignored:
                terminals += 1
            else:
                bad.append((mask.bit_count(), "terminal", actual))
            continue
        futures = tuple(
            target
            for target in actual
            if target in index and not (mask >> index[target] & 1)
        )
        if not futures:
            bad.append((mask.bit_count(), "dead", actual))
            continue
        for target in futures:
            future = mask | (1 << index[target])
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)
    reached = frozenset(
        site for site, bit in index.items() if reached_mask >> bit & 1
    )
    return len(seen), edges, terminals, tuple(bad), reached


def main() -> None:
    source = old_seed()
    prefix, frontier = forced_prefix(source)
    lower = cell.site(0, cell.LOWER_YZ)
    lower_value = cell.CONTENT[("A", cell.LOWER_YZ)]
    adapted = {**source, lower: lower_value}
    states, edges, terminals, bad, reached = graph(adapted)
    first_complete_oz = cell.site(3, cell.NOTCH_YZ)

    perturbation_failures = []
    attempts = 0
    for alternate in (None, *sorted(cell.FULL_ROLES - {lower_value})):
        trial = dict(source)
        if alternate is not None:
            trial[lower] = alternate
        outcome = graph(trial)
        attempts += 1
        if first_complete_oz in outcome[-1]:
            perturbation_failures.append((alternate, outcome[:4]))

    print("OLD_SEED_RECORDS", len(source))
    print("OLD_SEED_FORCED_PREFIX", len(prefix), prefix)
    print("OLD_SEED_TERMINAL_FRONTIER", frontier)
    print("MISSING_ADAPTER_RECORD", lower, lower_value)
    print("ADAPTED_GRAPH", states, edges, terminals, len(bad), bad[:2])
    print("FIRST_COMPLETE_OZ_REACHED", first_complete_oz in reached)
    print("ADAPTER_PERTURBATIONS", attempts, "FALSE_REACH", len(perturbation_failures), tuple(perturbation_failures[:4]))
    print(
        "RESULT",
        "ONE_RECORD_SEED_ADAPTER_REMAINS_OPEN"
        if (
            len(prefix) == 3
            and not frontier
            and (states, edges, terminals, len(bad)) == (378, 791, 1, 0)
            and first_complete_oz in reached
            and not perturbation_failures
        )
        else "FAIL",
    )


if __name__ == "__main__":
    main()
