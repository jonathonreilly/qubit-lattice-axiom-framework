#!/usr/bin/env python3
"""Price the exact boundary between renewed OZ launch and Cycle-129 bridge reuse.

The recurrent cell renews the exact Cycle-129 launch row.  This probe asks the
strictly stronger question: does the rest of the old 16-generation bridge run
from that socket without silently importing the old word/cage surroundings?

This is a local interface diagnostic only.  It selects no law and changes no
foundation, registry, policy, audit, or git state.
"""

from __future__ import annotations

import relational_notched_rail_socket_prototype_2026_07_15 as cell


Coord = tuple[int, int, int]
Signature = tuple[tuple[Coord, str], ...]


GROUPS: tuple[tuple[tuple[Coord, ...], str], ...] = (
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

LOCALS: tuple[Signature, ...] = (
    (((0, 0, 1), "H1"), ((0, 1, 0), "R_B01")),
    (((-1, 0, 0), "T_H3"), ((0, 0, 1), "H0"), ((0, 1, 0), "R_A01"), ((1, 0, 0), "OZ")),
    (((0, -1, 0), "L6"), ((0, 0, 1), "T_H3"), ((0, 1, 0), "W3")),
    (((-1, 0, 0), "L9"), ((0, -1, 0), "L7"), ((0, 0, 1), "H0"), ((0, 1, 0), "T_H3"), ((1, 0, 0), "A_0_0")),
    (((0, 0, 1), "W3"),),
    (((0, 0, 1), "A_0_0"), ((0, 1, 0), "A_2_0")),
    (((0, 0, 1), "A_1_2"), ((1, 0, 0), "A_3_1")),
    (((0, -1, 0), "L7"), ((0, 0, 1), "L9"), ((1, 0, 0), "A_3_2")),
    (((0, 0, 1), "L10"), ((1, 0, 0), "COMPLETE")),
    (((0, -1, 0), "GY"), ((1, 0, 0), "TY")),
    (((0, -1, 0), "YG0"), ((0, 0, -1), "W4"), ((1, 0, 0), "L10")),
    (((0, -1, 0), "Y2"), ((0, 0, -1), "AUXZ"), ((0, 0, 1), "W3"), ((0, 1, 0), "T_N0"), ((1, 0, 0), "L11")),
    (((0, 0, 1), "W1"), ((1, 0, 0), "T_N0")),
    (((0, 1, 0), "R_C01"), ((1, 0, 0), "GU")),
    (((0, 0, -1), "JOINT"), ((0, 0, 1), "A_0_2"), ((0, 1, 0), "W1"), ((1, 0, 0), "W3")),
    (((0, 0, 1), "B_0_2"), ((1, 0, 0), "T_N0")),
)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def transform(rotation, offset: Coord, position: Coord) -> Coord:
    return add(cell.c52.matvec(rotation, position), offset)


def main() -> None:
    launch_target = cell.EXEMPLAR_SOCKET[-1]
    launch_local = cell.SOCKET_ADDITIONS[-1][2]
    rotations = tuple(
        rotation
        for rotation in cell.c52.ROTATIONS
        if cell.c52.rotate_signature(LOCALS[0], rotation) == launch_local
    )
    print("EXACT_LABELED_LAUNCH_ROTATIONS", len(rotations))
    if len(rotations) != 1:
        print("RESULT", "FAIL")
        return
    rotation = rotations[0]
    source_launch = GROUPS[0][0][0]
    rotated_launch = cell.c52.matvec(rotation, source_launch)
    offset = tuple(a - b for a, b in zip(launch_target, rotated_launch))
    tr = lambda position: transform(rotation, offset, position)

    outputs, sockets, _ignored = cell.expected_outputs()
    records = {**cell.seed_records(), **outputs}
    for socket in sockets:
        records.pop(socket[-1])

    matches = []
    first_mismatch = None
    bridge_positions = {
        tr(site): output
        for sites, output in GROUPS
        for site in sites
    }
    prior = {}
    support = {}
    support_conflicts = []
    for generation, ((declared, output), required) in enumerate(zip(GROUPS, LOCALS)):
        target = tr(declared[0])
        expected = tuple(sorted(
            (cell.c52.matvec(rotation, direction), value)
            for direction, value in required
        ))
        actual = cell.local_signature(records, target)
        matches.append(actual == expected)
        if actual != expected and first_mismatch is None:
            first_mismatch = (generation, target, expected, actual)

        for direction, value in required:
            parent = add(target, cell.c52.matvec(rotation, direction))
            if prior.get(parent) == value:
                continue
            if parent in records:
                if records[parent] != value:
                    support_conflicts.append((
                        generation, parent, value, records[parent]
                    ))
            elif parent in bridge_positions:
                if parent not in prior:
                    support_conflicts.append((
                        generation, parent, value,
                        "FUTURE_" + bridge_positions[parent],
                    ))
            else:
                previous = support.get(parent)
                if previous is not None and previous != value:
                    support_conflicts.append((
                        generation, parent, value, "SUPPORT_" + previous
                    ))
                support[parent] = value

        for site in declared:
            physical = tr(site)
            records[physical] = output
            prior[physical] = output

    bridge_rows = {
        cell.canonical(required): output
        for (_sites, output), required in zip(GROUPS, LOCALS)
    }
    row_conflicts = tuple(sorted(
        (signature, cell.ROWS[signature], output)
        for signature, output in bridge_rows.items()
        if signature in cell.ROWS and cell.ROWS[signature] != output
    ))

    print("ROW_DOMAIN_CONFLICTS", len(row_conflicts), row_conflicts[:2])
    print("GENERATION_SIGNATURE_MATCHES", sum(matches), "OF", len(matches), tuple(matches))
    print("FIRST_DOWNSTREAM_MISMATCH", first_mismatch)
    print("EXTERNAL_SUPPORT_RECORDS", len(support), tuple(sorted(support.items())))
    print("OCCUPIED_SUPPORT_CONFLICTS", len(support_conflicts), tuple(support_conflicts))
    print(
        "RESULT",
        "EXACT_LAUNCH_RENEWS_BUT_CYCLE129_DOWNSTREAM_CONTEXT_DOES_NOT",
    )


if __name__ == "__main__":
    main()
