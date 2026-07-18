#!/usr/bin/env python3
"""Cycle 186: adjacent critical-pair and unique-closure test of the full law.

The current deterministic table is confluent on the campaign's selected
apparatuses.  This probe tests whether confluence follows from the full table
itself on unrestricted record configurations.

Take two adjacent open sites A and B in an otherwise fully recorded lattice.
Each site can have an arity-five exact signature omitting only the other open
site.  Both writes are initially enabled.  The probe exhausts all such
oppositely oriented row pairs and classifies what happens to each event after
the other site's permanent output is added.

The runner has no authority.  It edits no foundation, axiom, primitive,
registry, policy, audit, queue, predecessor, commit, push, or PR surface.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import recurrent_five_literal_lane_worldline_cycle178_2026_07_16 as c178


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FULL_LAW_ADJACENT_CRITICAL_PAIR_ACTUALITY_CYCLE186_NOTE_2026-07-16.md"
)

c53 = c178.c171.c53
LAW = c178.FULL_RAW
EX = (1, 0, 0)
NEG_EX = (-1, 0, 0)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def unique_output(values: frozenset[str]) -> str:
    if len(values) != 1:
        raise ValueError(("nondeterministic-output", values))
    return next(iter(values))


def extend_signature(signature, direction, role):
    if direction in dict(signature):
        raise ValueError(("occupied-direction", direction, signature))
    return tuple(sorted(signature + ((direction, role),)))


def transition_status(signature, direction, neighbor_role, original_output):
    values = LAW.get(extend_signature(signature, direction, neighbor_role))
    if values is None:
        return "ABSENT"
    output = unique_output(values)
    return "SAME" if output == original_output else "CHANGED"


A_ROWS = tuple(
    (signature, unique_output(values))
    for signature, values in LAW.items()
    if len(signature) == 5 and EX not in dict(signature)
)
B_ROWS = tuple(
    (signature, unique_output(values))
    for signature, values in LAW.items()
    if len(signature) == 5 and NEG_EX not in dict(signature)
)
OUTPUTS = tuple(sorted({
    output
    for _signature, output in A_ROWS + B_ROWS
}))


def pair_census():
    b_counts = {}
    b_witness = {}
    for a_output in OUTPUTS:
        counts = Counter()
        for signature, b_output in B_ROWS:
            status = transition_status(
                signature,
                NEG_EX,
                a_output,
                b_output,
            )
            counts[(b_output, status)] += 1
            b_witness.setdefault(
                (a_output, b_output, status),
                (signature, b_output),
            )
        b_counts[a_output] = counts

    categories = Counter()
    witness = None
    for a_signature, a_output in A_ROWS:
        counts = b_counts[a_output]
        for (b_output, b_status), count in counts.items():
            a_status = transition_status(
                a_signature,
                EX,
                b_output,
                a_output,
            )
            categories[(a_status, b_status)] += count
            if (
                witness is None
                and a_status == "ABSENT"
                and b_status == "ABSENT"
            ):
                b_signature, _ = b_witness[
                    (a_output, b_output, b_status)
                ]
                witness = (
                    a_signature,
                    a_output,
                    b_signature,
                    b_output,
                )
    return categories, witness


PAIR_CATEGORIES, WITNESS = pair_census()


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def witness_geometry(witness):
    a_signature, a_output, b_signature, b_output = witness
    a_target = (0, 0, 0)
    b_target = EX
    a_records = {
        add(a_target, direction): role
        for direction, role in a_signature
    }
    b_records = {
        add(b_target, direction): role
        for direction, role in b_signature
    }
    overlap = {
        site: (a_records[site], b_records[site])
        for site in set(a_records) & set(b_records)
    }
    return (
        a_target,
        b_target,
        a_records,
        b_records,
        overlap,
        a_output,
        b_output,
    )


def rotated_witness_failures(witness):
    a_signature, a_output, b_signature, b_output = witness
    failures = []
    for rotation in c53.ROTATIONS:
        rotated_a = c53.rotate_signature(a_signature, rotation)
        rotated_b = c53.rotate_signature(b_signature, rotation)
        direction = c53.matvec(rotation, EX)
        opposite = tuple(-value for value in direction)
        if LAW.get(rotated_a) != frozenset((a_output,)):
            failures.append(("a-base", rotation, LAW.get(rotated_a)))
        if LAW.get(rotated_b) != frozenset((b_output,)):
            failures.append(("b-base", rotation, LAW.get(rotated_b)))
        if LAW.get(extend_signature(rotated_a, direction, b_output)) is not None:
            failures.append((
                "a-after-b",
                rotation,
                LAW.get(extend_signature(rotated_a, direction, b_output)),
            ))
        if LAW.get(extend_signature(rotated_b, opposite, a_output)) is not None:
            failures.append((
                "b-after-a",
                rotation,
                LAW.get(extend_signature(rotated_b, opposite, a_output)),
            ))
    return tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND LAW")
    check("Cycle-186 review note exists", NOTE.is_file())
    check(
        "the consumed law is the deterministic Cycle-178 union",
        len(LAW) == 101_996
        and all(len(values) == 1 for values in LAW.values())
        and not c178.RAW_CONFLICTS,
        (len(LAW), len(c178.RAW_CONFLICTS)),
    )

    print("\nADJACENT ARITY-FIVE DOMAIN")
    check(
        "both orientations expose the expected arity-five row population",
        len(A_ROWS) > 0
        and len(A_ROWS) == len(B_ROWS)
        and set(OUTPUTS) == {
            output
            for _signature, output in A_ROWS
        } == {
            output
            for _signature, output in B_ROWS
        },
        (len(A_ROWS), len(B_ROWS), len(OUTPUTS)),
    )
    check(
        "the pair census covers the full oriented Cartesian product",
        sum(PAIR_CATEGORIES.values()) == len(A_ROWS) * len(B_ROWS),
        (sum(PAIR_CATEGORIES.values()), len(A_ROWS) * len(B_ROWS)),
    )
    check(
        "almost every adjacent arity-five pair mutually disables and none commutes",
        PAIR_CATEGORIES == {
            ("ABSENT", "ABSENT"): 208_395_792,
            ("SAME", "ABSENT"): 1_152,
            ("ABSENT", "SAME"): 1_152,
        },
        PAIR_CATEGORIES,
    )

    print("\nEXACT MUTUAL-DISABLE WITNESS")
    check("one mutual-disable witness exists", WITNESS is not None)
    if WITNESS is None:
        print("SUMMARY")
        print("PASS", PASS, "FAIL", FAIL)
        return 1

    (
        a_target,
        b_target,
        a_records,
        b_records,
        overlap,
        a_output,
        b_output,
    ) = witness_geometry(WITNESS)
    a_signature, _a_output, b_signature, _b_output = WITNESS
    check(
        "the adjacent arity-five supporting records are geometrically disjoint",
        not overlap
        and len(a_records) == 5
        and len(b_records) == 5
        and b_target == add(a_target, EX),
        overlap,
    )
    check(
        "both writes are enabled on the same initial two-hole record state",
        LAW.get(a_signature) == frozenset((a_output,))
        and LAW.get(b_signature) == frozenset((b_output,)),
        (a_output, b_output),
    )
    a_after_b = extend_signature(a_signature, EX, b_output)
    b_after_a = extend_signature(b_signature, NEG_EX, a_output)
    check(
        "writing either permanent record disables the other exact event",
        LAW.get(a_after_b) is None
        and LAW.get(b_after_a) is None,
        (LAW.get(a_after_b), LAW.get(b_after_a)),
    )
    check(
        "the two maximal local completions are distinct permanent configurations",
        (a_target, a_output) != (b_target, b_output)
        and a_target not in a_records
        and b_target not in b_records,
        ((a_target, a_output), (b_target, b_output)),
    )
    rotation_failures = rotated_witness_failures(WITNESS)
    check(
        "all 24 proper-cubic images preserve the mutual-disable critical pair",
        not rotation_failures,
        rotation_failures[:1],
    )

    print("\nSCOPE AND INTERPRETATION")
    note = NOTE.read_text()
    check(
        "the note restricts the result to the unrestricted table domain",
        "not a reachable-state counterexample" in note
        and "unrestricted extensional table domain" in note
        and "N1 — alternative routes" in note
        and "N8 — cross-cycle echo" in note,
    )
    check(
        "the witness separates apparatus confluence from global law confluence",
        PAIR_CATEGORIES[("ABSENT", "ABSENT")] > 0
        and PAIR_CATEGORIES[("SAME", "SAME")] == 0,
    )

    print("\nACCOUNTING")
    print("A_ROWS", len(A_ROWS))
    print("B_ROWS", len(B_ROWS))
    print("OUTPUTS", len(OUTPUTS))
    print("PAIR_CATEGORIES", PAIR_CATEGORIES)
    print("MUTUAL_DISABLE_PAIRS", PAIR_CATEGORIES[("ABSENT", "ABSENT")])
    print("COMMUTING_PAIRS", PAIR_CATEGORIES[("SAME", "SAME")])
    print("WITNESS_A_SIGNATURE", a_signature)
    print("WITNESS_A_OUTPUT", a_output)
    print("WITNESS_B_SIGNATURE", b_signature)
    print("WITNESS_B_OUTPUT", b_output)
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "FULL_LAW_HAS_UNRESTRICTED_NONCONFLUENT_MAXIMAL_RECORD_COMPLETIONS"
        if FAIL == 0
        else "CYCLE186_NEEDS_REPAIR",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
