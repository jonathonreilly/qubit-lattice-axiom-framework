#!/usr/bin/env python3
"""Exhaust onsite-role corruptions of the recurrent notched socket parents."""

from __future__ import annotations

import relational_notched_rail_socket_prototype_2026_07_15 as cell


def identity_rotation():
    return next(
        rotation
        for rotation in cell.c52.ROTATIONS
        if cell.c52.matvec(rotation, (2, 3, 5)) == (2, 3, 5)
    )


def main() -> None:
    expected, sockets, _ignored = cell.expected_outputs()
    rail = cell.seed_records()
    rail.update(expected)
    for socket in sockets:
        _q, _blocker, _a_guard, _root, _b_guard, helper, h1, launch = socket
        rail.pop(helper)
        rail.pop(h1)
        rail.pop(launch)

    attempts = 0
    false_positive_failures = []
    diagnostic_alternates = []
    for socket_index, socket in enumerate(sockets):
        q, blocker, a_guard, root, b_guard, helper, h1, launch = socket
        stages = (
            (
                "helper",
                dict(rail),
                helper,
                (("root", root), ("b_guard", b_guard)),
            ),
            (
                "h1",
                {**rail, helper: cell.HELPER_CONTENT},
                h1,
                (("blocker", blocker), ("a_guard", a_guard), ("helper", helper)),
            ),
            (
                "oz",
                {**rail, helper: cell.HELPER_CONTENT, h1: cell.H1},
                launch,
                (("q", q), ("h1", h1)),
            ),
        )
        for stage, context, target, parents in stages:
            for label, parent in parents:
                correct = context[parent]
                deleted = dict(context)
                deleted.pop(parent)
                attempts += 1
                deleted_values = cell.enabled(deleted).get(target, frozenset())
                expected_value = {
                    "helper": cell.HELPER_CONTENT,
                    "h1": cell.H1,
                    "oz": cell.OZ,
                }[stage]
                if expected_value in deleted_values:
                    false_positive_failures.append((
                        socket_index,
                        stage,
                        label,
                        "DELETED",
                        deleted_values,
                    ))
                elif deleted_values:
                    diagnostic_alternates.append((
                        socket_index,
                        stage,
                        label,
                        "DELETED",
                        deleted_values,
                    ))
                for alternate in sorted(cell.FULL_ROLES - {correct}):
                    trial = dict(context)
                    trial[parent] = alternate
                    actual = cell.enabled(trial)
                    attempts += 1
                    actual_values = actual.get(target, frozenset())
                    if expected_value in actual_values:
                        false_positive_failures.append((
                            socket_index,
                            stage,
                            label,
                            alternate,
                            actual_values,
                        ))
                    elif actual_values:
                        diagnostic_alternates.append((
                            socket_index,
                            stage,
                            label,
                            alternate,
                            actual_values,
                        ))

    identity = identity_rotation()
    initial_q = cell.site(-1, cell.ROOT_YZ)
    next_q = cell.site(3, cell.ROOT_YZ)
    seed = cell.seed_records()
    recurrence_attempts = 0
    recurrence_failures = []
    deleted_seed = dict(seed)
    deleted_seed.pop(initial_q)
    deleted_result = cell.graph(
        identity,
        last_x=3,
        base_records=deleted_seed,
        include_reached=True,
    )
    recurrence_attempts += 1
    if next_q in deleted_result["reached"]:
        recurrence_failures.append(("DELETED", deleted_result["states"]))
    for alternate in sorted(cell.FULL_ROLES - {seed[initial_q]}):
        corrupt_seed = dict(seed)
        corrupt_seed[initial_q] = alternate
        result = cell.graph(
            identity,
            last_x=3,
            base_records=corrupt_seed,
            include_reached=True,
        )
        recurrence_attempts += 1
        if next_q in result["reached"]:
            recurrence_failures.append((alternate, result["states"], result["bad"][:2]))

    print("DIRECT_ATTEMPTS", attempts)
    print(
        "DIRECT_FALSE_POSITIVE_FAILURES",
        len(false_positive_failures),
        tuple(false_positive_failures[:80]),
    )
    print(
        "DIRECT_DIAGNOSTIC_ALTERNATES",
        len(diagnostic_alternates),
        tuple(diagnostic_alternates[:80]),
    )
    print("RECURRENCE_ATTEMPTS", recurrence_attempts)
    print("RECURRENCE_FAILURES", len(recurrence_failures), tuple(recurrence_failures[:80]))


if __name__ == "__main__":
    main()
