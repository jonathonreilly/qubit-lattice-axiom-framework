#!/usr/bin/env python3
"""Cycle 198: disjoint simultaneous Cycle-190/Cycle-193 product probe.

One Cycle-190 hard finite-membership consumer and one Cycle-193 R2 physical
dispatcher are placed in one lattice record configuration under Cycle 197B's
full deterministic law.  Their occupied supports are separated by one open
lattice layer.  The runner certifies exact joint histories, dependency-graph
factorization, projection to both source histories, absence of parasitic
firings, and proper-cubic covariance of the product contract.

This is disjoint simultaneous coexistence, not interaction or quantum
execution.  It adds no local-law row or onsite role and has no authority.
"""

from __future__ import annotations

import hashlib
from collections import defaultdict
from pathlib import Path

import common_replacement_base_integration_cycle197b_2026_07_16 as c197b


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "DISJOINT_MIXED_PRODUCT_COEXISTENCE_CYCLE198_NOTE_2026-07-16.md"
)
CYCLE197B_SCRIPT = (
    ROOT / "scripts/common_replacement_base_integration_cycle197b_2026_07_16.py"
)
CYCLE197B_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COMMON_REPLACEMENT_BASE_INTEGRATION_CYCLE197B_NOTE_2026-07-16.md"
)
FROZEN = {
    CYCLE197B_SCRIPT: "d95a6b33cc86b68adae52a7c8c6e5eaa7ee277e58e845db6b7da2cf873fdfac1",
    CYCLE197B_NOTE: "35134a682f105f177d40d01d6a32d9a008b2791310d53f9dfde0952a97f8f8e0",
}

c190 = c197b.c190
c193 = c197b.c193
c53 = c197b.c53
FULL_RAW = c197b.FULL_RAW

Coord = tuple[int, int, int]
RoleMap = dict[Coord, str]

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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def shifted(records: RoleMap, offset: Coord) -> RoleMap:
    return {add(site, offset): role for site, role in records.items()}


def shifted_sites(sites, offset: Coord) -> frozenset[Coord]:
    return frozenset(add(site, offset) for site in sites)


def shifted_dependencies(dependencies, offset: Coord):
    return {
        add(target, offset): frozenset(add(parent, offset) for parent in parents)
        for target, parents in dependencies.items()
    }


def support(initial, expected, exits=()) -> frozenset[Coord]:
    return frozenset(set(initial) | set(expected) | set(exits))


def bounds(sites: frozenset[Coord]):
    return tuple(
        (min(site[axis] for site in sites), max(site[axis] for site in sites))
        for axis in range(3)
    )


def cross_contacts(left: frozenset[Coord], right: frozenset[Coord]):
    overlaps = left & right
    contacts = {
        (site, add(site, direction))
        for site in left
        for direction in c53.DIRECTIONS
        if add(site, direction) in right
    }
    return overlaps, frozenset(contacts)


def merge_disjoint(left: RoleMap, right: RoleMap) -> RoleMap:
    overlap = set(left) & set(right)
    if overlap:
        raise ValueError(("record-overlap", tuple(sorted(overlap))[:3]))
    return {**left, **right}


def topo_schedule(dependencies, order: str) -> tuple[Coord, ...]:
    children = defaultdict(list)
    pending = {target: len(parents) for target, parents in dependencies.items()}
    for target, parents in dependencies.items():
        for parent in parents:
            children[parent].append(target)
    frontier = {target for target, count in pending.items() if count == 0}
    result = []
    while frontier:
        target = min(frontier) if order == "min" else max(frontier)
        frontier.remove(target)
        result.append(target)
        for child in children[target]:
            pending[child] -= 1
            if pending[child] == 0:
                frontier.add(child)
    if len(result) != len(dependencies):
        raise ValueError(("dependency-cycle", len(result), len(dependencies)))
    return tuple(result)


def is_topological(sequence, dependencies) -> bool:
    position = {site: index for index, site in enumerate(sequence)}
    return len(position) == len(dependencies) and all(
        position[parent] < position[target]
        for target, parents in dependencies.items()
        for parent in parents
    )


def local_premise(initial, expected, dependencies, target: Coord) -> RoleMap:
    premise = {
        neighbour: initial[neighbour]
        for direction in c53.DIRECTIONS
        if (neighbour := add(target, direction)) in initial
    }
    premise.update({parent: expected[parent] for parent in dependencies[target]})
    return premise


def transformed_site(site: Coord, rotation, shift: Coord) -> Coord:
    return add(c53.matvec(rotation, site), shift)


def covariance_census(initial, expected, exits, dependencies, left_support, right_support):
    local_checks = 0
    local_failures = []
    separation_failures = []
    terminal_failures = []
    premises = {
        target: local_premise(initial, expected, dependencies, target)
        for target in expected
    }
    final = {**initial, **expected}

    for index, rotation in enumerate(c53.ROTATIONS):
        translation = (10_000 + 101 * index, -20_000, 30_000)
        rotated_left = frozenset(
            transformed_site(site, rotation, translation)
            for site in left_support
        )
        rotated_right = frozenset(
            transformed_site(site, rotation, translation)
            for site in right_support
        )
        overlaps, contacts = cross_contacts(rotated_left, rotated_right)
        if overlaps or contacts:
            separation_failures.append((index, len(overlaps), len(contacts)))

        for target, premise in premises.items():
            rotated_target = transformed_site(target, rotation, translation)
            rotated_premise = {
                transformed_site(site, rotation, translation): role
                for site, role in premise.items()
            }
            actual = FULL_RAW.get(
                c53.local_signature(rotated_premise, rotated_target),
                frozenset(),
            )
            local_checks += 1
            if actual != frozenset((expected[target],)):
                local_failures.append((index, target, expected[target], actual))
                if len(local_failures) >= 10:
                    break

        rotated_final = c53.transform_records(final, rotation, translation)
        rotated_exits = c53.transform_records(exits, rotation, translation)
        observed = {
            target: FULL_RAW[signature]
            for target in c53.open_candidates(rotated_final)
            if (
                signature := c53.local_signature(rotated_final, target)
            ) in FULL_RAW
        }
        if observed != rotated_exits:
            terminal_failures.append((
                index,
                len(observed),
                len(rotated_exits),
                tuple(sorted(set(observed) ^ set(rotated_exits)))[:3],
            ))

    return {
        "local_checks": local_checks,
        "local_failures": tuple(local_failures),
        "separation_failures": tuple(separation_failures),
        "terminal_failures": tuple(terminal_failures),
    }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("FROZEN LAW")
    observed = {path: sha256(path) for path in FROZEN}
    check(
        "Cycle 197B remains byte-frozen",
        observed == FROZEN,
        {path.name: digest for path, digest in observed.items()},
    )
    check(
        "the inherited full law is deterministic and unchanged",
        len(FULL_RAW) == 102_398
        and all(len(outputs) == 1 for outputs in FULL_RAW.values()),
        len(FULL_RAW),
    )

    old_190 = c190.FULL_RAW
    old_171 = c190.c171.FULL_RAW
    old_193 = c193.MERGED_RAW
    c190.FULL_RAW = FULL_RAW
    c190.c171.FULL_RAW = FULL_RAW
    c193.MERGED_RAW = FULL_RAW
    try:
        left = c190.apparatus(HARD_WORD)
        left_certificate = c190.c171.causal_certificate(
            left[0], left[1], left[2]
        )
        right = c193.instance(R2_CODE)
        right_min = c193.physical_run(right, "min")
        right_max = c193.physical_run(right, "max")

        left_support = support(left[0], left[1], left[2])
        right_unshifted_support = support(right.initial, right.expected)
        # One open x-layer is the smallest separation guaranteed solely by
        # disjoint axis-aligned support slabs: translated min-x = left max-x+2.
        offset = (
            max(site[0] for site in left_support)
            - min(site[0] for site in right_unshifted_support)
            + 2,
            0,
            0,
        )
        right_initial = shifted(right.initial, offset)
        right_expected = shifted(right.expected, offset)
        right_dependencies = shifted_dependencies(right.dependencies, offset)
        right_support = shifted_sites(right_unshifted_support, offset)

        print("\nSPATIAL PRODUCT")
        overlaps, contacts = cross_contacts(left_support, right_support)
        check(
            "the two complete supports are disjoint with one open lattice layer",
            not overlaps
            and not contacts
            and min(site[0] for site in right_support)
            - max(site[0] for site in left_support) == 2,
            {
                "offset": offset,
                "left_bounds": bounds(left_support),
                "right_bounds": bounds(right_support),
                "overlaps": len(overlaps),
                "contacts": len(contacts),
            },
        )
        initial = merge_disjoint(left[0], right_initial)
        expected = merge_disjoint(left[1], right_expected)
        exits = dict(left[2])
        check(
            "merged initial and expected records are exactly additive and consistent",
            len(initial) == len(left[0]) + len(right.initial)
            and len(expected) == len(left[1]) + len(right.expected)
            and not (set(initial) & set(expected)),
            {
                "initial": len(initial),
                "expected": len(expected),
                "exits": len(exits),
            },
        )

        print("\nSOURCE AND JOINT HISTORIES")
        check(
            "both source apparatuses retain their exact hard histories",
            left_certificate["ok"]
            and left_certificate["minimum"]["states"] == 2_289
            and left_certificate["edge_checks"]["edges"] == 4_232
            and right_min[0]
            and right_max[0]
            and right_min[1]["dynamic"] == 4_388
            and right_max[1]["dynamic"] == 4_388,
            {
                "left_states": left_certificate["minimum"]["states"],
                "left_edges": left_certificate["edge_checks"]["edges"],
                "right_min": right_min,
                "right_max": right_max,
            },
        )
        joint = c190.c171.causal_certificate(initial, expected, exits)
        check(
            "the simultaneous minimum and maximum histories close exactly",
            joint["ok"]
            and joint["minimum"]["states"] == 6_677
            and joint["edge_checks"]["edges"] == 8_615
            and joint["minimum"]["max_frontier"] == 25
            and joint["maximum"]["max_frontier"] == 22
            and not joint["unordered"]
            and len(joint["minimum"]["terminal"]) == 10
            and joint["minimum"]["terminal"] == exits
            and joint["maximum"]["terminal"] == exits,
            {
                "ok": joint["ok"],
                "states": joint["minimum"]["states"],
                "edges": joint["edge_checks"]["edges"],
                "frontiers": (
                    joint["minimum"]["max_frontier"],
                    joint["maximum"]["max_frontier"],
                ),
                "unordered": len(joint["unordered"]),
                "terminal": len(joint["minimum"]["terminal"]),
            },
        )

        wanted_dependencies = {
            **left_certificate["dependencies"],
            **right_dependencies,
        }
        left_targets = set(left[1])
        right_targets = set(right_expected)
        cross_edges = tuple(
            (parent, target)
            for target, parents in joint["dependencies"].items()
            for parent in parents
            if (target in left_targets) != (parent in left_targets)
        )
        check(
            "the joint dependency graph is the exact disjoint source union",
            joint["dependencies"] == wanted_dependencies
            and not cross_edges
            and sum(map(len, left_certificate["dependencies"].values())) == 4_232
            and sum(map(len, right_dependencies.values())) == 4_383,
            {
                "joint_nodes": len(joint["dependencies"]),
                "left_nodes": len(left_certificate["dependencies"]),
                "right_nodes": len(right_dependencies),
                "cross_edges": cross_edges[:3],
            },
        )

        projections = {}
        for order in ("min", "max"):
            joint_order = topo_schedule(joint["dependencies"], order)
            left_projection = tuple(site for site in joint_order if site in left_targets)
            right_projection = tuple(site for site in joint_order if site in right_targets)
            projections[order] = (
                len(left_projection),
                len(right_projection),
                is_topological(left_projection, left_certificate["dependencies"]),
                is_topological(right_projection, right_dependencies),
            )
        check(
            "both joint schedules project to valid complete source histories",
            all(
                values == (2_288, 4_388, True, True)
                for values in projections.values()
            ),
            projections,
        )
        check(
            "full-frontier replay finds no parasitic fire or adjacency alias",
            not joint["edge_checks"]["signature_failures"]
            and not joint["edge_checks"]["deletion_failures"]
            and not joint["unordered"],
            {
                "signature_failures": joint["edge_checks"]["signature_failures"],
                "deletion_failures": joint["edge_checks"]["deletion_failures"],
                "unordered": joint["unordered"],
            },
        )

        print("\nPROPER-CUBIC PRODUCT COVARIANCE")
        covariance = covariance_census(
            initial,
            expected,
            exits,
            joint["dependencies"],
            left_support,
            right_support,
        )
        check(
            "all twenty-four rotations preserve separation and every local write",
            covariance["local_checks"] == 24 * 6_676
            and not covariance["local_failures"]
            and not covariance["separation_failures"]
            and all(c53.determinant(rotation) == 1 for rotation in c53.ROTATIONS),
            {
                "local_checks": covariance["local_checks"],
                "local_failures": covariance["local_failures"][:1],
                "separation_failures": covariance["separation_failures"][:1],
            },
        )
        check(
            "all rotated terminal rescans expose exactly the ten inherited exits",
            not covariance["terminal_failures"],
            covariance["terminal_failures"][:1],
        )

        print("\nPRICE AND SCOPE")
        inherited_roles = c197b.law_roles(FULL_RAW)
        apparatus_roles = set(initial.values()) | set(expected.values())
        check(
            "the spatial product adds zero rows and zero onsite roles",
            len(FULL_RAW) == 102_398
            and apparatus_roles <= inherited_roles,
            {
                "new_rows": 0,
                "new_roles": tuple(sorted(apparatus_roles - inherited_roles)),
            },
        )
        normalized_note = (
            " ".join(NOTE.read_text(encoding="utf-8").lower().split())
            if NOTE.is_file()
            else ""
        )
        required = (
            "disjoint simultaneous coexistence",
            "not interaction",
            "not quantum execution",
            "one open lattice layer",
            "zero new rows and zero onsite roles",
            "no axiom conclusion follows",
            "draft parking branch",
        )
        missing = tuple(phrase for phrase in required if phrase not in normalized_note)
        check(
            "the note preserves the exact bounded scope",
            NOTE.is_file() and not missing,
            missing,
        )

        print("\nACCOUNTING")
        print("OFFSET", offset)
        print("INITIAL_RECORDS", len(initial))
        print("DYNAMIC_RECORDS", len(expected))
        print("JOINT_STATES", joint["minimum"]["states"])
        print("JOINT_EDGES", joint["edge_checks"]["edges"])
        print("ROTATED_LOCAL_CHECKS", covariance["local_checks"])
        print("FULL_RAW_ROWS", len(FULL_RAW))
        print("NEW_ROWS", 0)
        print("NEW_ROLES", ())
        print("PASS", PASS, "FAIL", FAIL)
        print(
            "RESULT",
            "DISJOINT_MIXED_PRODUCT_COEXISTENCE"
            if FAIL == 0
            else "CYCLE198_OPEN",
        )
        return int(FAIL != 0)
    finally:
        c190.FULL_RAW = old_190
        c190.c171.FULL_RAW = old_171
        c193.MERGED_RAW = old_193


if __name__ == "__main__":
    raise SystemExit(main())
