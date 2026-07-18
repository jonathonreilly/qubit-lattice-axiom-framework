#!/usr/bin/env python3
"""Cycle 199: exact first-contact boundary diagnostic.

Move the Cycle-193 R2 dispatcher toward the Cycle-190 hard apparatus from the
Cycle-198 one-open-slab placement.  Distinguish bounding-slab adjacency,
first mixed open-site signature, and first occupied-record contact, then replay
the one-step and first-mixed configurations under the Cycle-197B candidate
table.  This is exploratory source-grade work with no authority.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import common_replacement_base_integration_cycle197b_2026_07_16 as c197b


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "FIRST_CONTACT_BOUNDARY_DIAGNOSTIC_CYCLE199_NOTE_2026-07-16.md"
)
c190 = c197b.c190
c193 = c197b.c193
c53 = c197b.c53
FULL_RAW = c197b.FULL_RAW

Coord = tuple[int, int, int]
BASE_OFFSET = 133
ONE_STEP_OFFSET = 132
FIRST_MIXED_OFFSET = 130
FIRST_CONTACT_OFFSET = 129
HARD_WORD = (1, 0, 1, 0, 1)
R2_CODE = c193.c191.CONTEXT_CODES["R2"]

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


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def shift(records, x_offset: int):
    return {(x + x_offset, y, z): role for (x, y, z), role in records.items()}


def shift_sites(sites, x_offset: int):
    return frozenset((x + x_offset, y, z) for x, y, z in sites)


def contacts(left, right):
    return frozenset(
        (site, add(site, direction))
        for site in left
        for direction in c53.DIRECTIONS
        if add(site, direction) in right
    )


def shell(radius: int):
    return tuple(
        delta
        for delta in product(range(-radius, radius + 1), repeat=3)
        if sum(map(abs, delta)) == radius
    )


def minimum_distance(left, right, limit: int = 10):
    right_set = set(right)
    for distance in range(limit + 1):
        for site in left:
            for delta in shell(distance):
                target = add(site, delta)
                if target in right_set:
                    return distance, site, target
    return None


def mixed_initial_signatures(left_initial, right_initial):
    initial = {**left_initial, **right_initial}
    left_sites = set(left_initial)
    right_sites = set(right_initial)
    result = []
    for target in c53.open_candidates(initial):
        neighbours = tuple(add(target, direction) for direction in c53.DIRECTIONS)
        if (
            any(site in left_sites for site in neighbours)
            and any(site in right_sites for site in neighbours)
        ):
            signature = c53.local_signature(initial, target)
            result.append((target, signature, FULL_RAW.get(signature)))
    return tuple(sorted(result))


def joint_certificate(left, right, x_offset: int):
    initial = {**left[0], **shift(right.initial, x_offset)}
    expected = {**left[1], **shift(right.expected, x_offset)}
    return c190.c171.causal_certificate(initial, expected, left[2])


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    old_190 = c190.FULL_RAW
    old_171 = c190.c171.FULL_RAW
    old_193 = c193.MERGED_RAW
    c190.FULL_RAW = FULL_RAW
    c190.c171.FULL_RAW = FULL_RAW
    c193.MERGED_RAW = FULL_RAW
    try:
        left = c190.apparatus(HARD_WORD)
        right = c193.instance(R2_CODE)
        left_support = frozenset(set(left[0]) | set(left[1]) | set(left[2]))
        right_support = frozenset(set(right.initial) | set(right.expected))

        print("ONE-STEP REQUESTED PLACEMENT")
        one_step_support = shift_sites(right_support, ONE_STEP_OFFSET)
        one_step_contacts = contacts(left_support, one_step_support)
        one_step_distance = minimum_distance(left_support, one_step_support)
        one_step_mixed = mixed_initial_signatures(
            left[0], shift(right.initial, ONE_STEP_OFFSET)
        )
        check(
            "one step closes the slab gap but not the occupied-support gap",
            BASE_OFFSET - ONE_STEP_OFFSET == 1
            and min(site[0] for site in one_step_support)
            - max(site[0] for site in left_support) == 1
            and not one_step_contacts
            and one_step_distance is not None
            and one_step_distance[0] == 4
            and not one_step_mixed,
            {
                "offset": ONE_STEP_OFFSET,
                "contacts": len(one_step_contacts),
                "minimum_distance": one_step_distance,
                "mixed_signatures": one_step_mixed,
            },
        )
        one_step_run = joint_certificate(left, right, ONE_STEP_OFFSET)
        check(
            "the requested one-step configuration is transparently exact",
            one_step_run["ok"]
            and one_step_run["minimum"]["states"] == 6_677
            and one_step_run["edge_checks"]["edges"] == 8_615
            and not one_step_run["unordered"]
            and len(one_step_run["minimum"]["terminal"]) == 10,
            {
                "ok": one_step_run["ok"],
                "states": one_step_run["minimum"]["states"],
                "edges": one_step_run["edge_checks"]["edges"],
            },
        )

        print("FIRST MIXED SIGNATURE")
        distance_profile = {
            offset: minimum_distance(left_support, shift_sites(right_support, offset))[0]
            for offset in (132, 131, 130, 129)
        }
        first_mixed = mixed_initial_signatures(
            left[0], shift(right.initial, FIRST_MIXED_OFFSET)
        )
        check(
            "the exact approach profile is 4, 3, 2, 1 lattice steps",
            distance_profile == {132: 4, 131: 3, 130: 2, 129: 1},
            distance_profile,
        )
        check(
            "offset 130 has one mixed signature and no acting law row",
            first_mixed == ((
                (7, 3, -3),
                (((-1, 0, 0), "R_A13"), ((1, 0, 0), "MARK")),
                None,
            ),),
            first_mixed,
        )
        mixed_run = joint_certificate(left, right, FIRST_MIXED_OFFSET)
        check(
            "the first mixed-signature configuration remains transparently exact",
            mixed_run["ok"]
            and mixed_run["minimum"]["states"] == 6_677
            and mixed_run["edge_checks"]["edges"] == 8_615
            and not mixed_run["unordered"]
            and len(mixed_run["minimum"]["terminal"]) == 10,
            {
                "ok": mixed_run["ok"],
                "states": mixed_run["minimum"]["states"],
                "edges": mixed_run["edge_checks"]["edges"],
            },
        )

        print("FIRST OCCUPIED CONTACT")
        contact_support = shift_sites(right_support, FIRST_CONTACT_OFFSET)
        contact_pairs = contacts(left_support, contact_support)
        check(
            "offset 129 is the first occupied-record contact",
            len(contact_pairs) == 1
            and contact_pairs
            == frozenset((((6, 3, -3), (7, 3, -3)),))
            and left[0][(6, 3, -3)] == "R_A13"
            and shift(right.initial, FIRST_CONTACT_OFFSET)[(7, 3, -3)] == "MARK",
            contact_pairs,
        )

        normalized = (
            " ".join(NOTE.read_text(encoding="utf-8").lower().split())
            if NOTE.is_file()
            else ""
        )
        required = (
            "bounding-slab contact is not occupied-record contact",
            "transparent closure",
            "no existing row acts",
            "not a no-go",
            "draft parking branch",
        )
        missing = tuple(phrase for phrase in required if phrase not in normalized)
        check("the note preserves the diagnostic boundary", not missing, missing)

        print("PASS", PASS, "FAIL", FAIL)
        print(
            "RESULT",
            "FIRST_CONTACT_BOUNDARY_DIAGNOSTIC"
            if FAIL == 0
            else "CYCLE199_OPEN",
        )
        return int(FAIL != 0)
    finally:
        c190.FULL_RAW = old_190
        c190.c171.FULL_RAW = old_171
        c193.MERGED_RAW = old_193


if __name__ == "__main__":
    raise SystemExit(main())
