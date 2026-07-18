#!/usr/bin/env python3
"""Cycle 84: exact collision-free separation control for Cycle 80 tubes.

This is a positive finite control, not a collision-resolution no-go.  It
checks that two copies of the three-phase recurrent append tube factor as the
Cartesian product of their one-tube asynchronous graphs whenever every site
in one occupied support is at least two lattice steps from the other.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import joint_endpoint_bdh_rebind_cycle63_2026_07_14 as c63
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import three_phase_recurrent_append_tube_cycle80_2026_07_14 as c80


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "SEPARATED_RECURRENT_TUBE_COLLISION_CONTROL_CYCLE84_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
OFFSETS = ((0, 6, 0), (0, 0, 5))
HORIZONS = (3, 6, 9)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def translate(records: dict[Coord, str], offset: Coord) -> dict[Coord, str]:
    return {add(site, offset): content for site, content in records.items()}


def rotate_translate(
    records: dict[Coord, str],
    rotation: tuple[tuple[int, int, int], ...],
    offset: Coord,
) -> dict[Coord, str]:
    return {
        add(c53.matvec(rotation, site), offset): content
        for site, content in records.items()
    }


def one_tube(horizon: int) -> tuple[dict[Coord, str], dict[Coord, str]]:
    source = {
        **c80.layer(0, "A"),
        (-1, *c80.LAUNCH["A"]): "Z0",
    }
    allowed: dict[Coord, str] = {}
    for x in range(1, horizon + 1):
        allowed.update(c80.layer(x, c80.PHASES[x % 3]))
    return source, allowed


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def minimum_cross_distance(
    left: set[Coord], right: set[Coord]
) -> int:
    return min(manhattan(a, b) for a in left for b in right)


def projected_state_pairs(
    joint: c63.ExactGraph,
    left: c63.ExactGraph,
    right: c63.ExactGraph,
) -> frozenset[tuple[int, int]]:
    joint_index = {site: index for index, site in enumerate(joint.sites)}

    def project(mask: int, sites: tuple[Coord, ...], shift: Coord) -> int:
        result = 0
        for bit, site in enumerate(sites):
            joint_site = add(site, shift)
            if mask & (1 << joint_index[joint_site]):
                result |= 1 << bit
        return result

    zero = (0, 0, 0)
    return frozenset(
        (project(mask, left.sites, zero), project(mask, right.sites, zero))
        for mask in joint.states
    )


def expected_parasites(horizon: int, offset: Coord) -> frozenset[tuple[Coord, str]]:
    phase = c80.PHASES[(horizon + 1) % 3]
    site = (horizon + 1, *c80.SEED[phase])
    output = c80.role(phase, *c80.SEED[phase])
    return frozenset({(site, output), (add(site, offset), output)})


def exact_factorization_controls() -> None:
    for offset in OFFSETS:
        for horizon in HORIZONS:
            source, allowed = one_tube(horizon)
            shifted_source = translate(source, offset)
            shifted_allowed = translate(allowed, offset)
            left_support = set(source) | set(allowed)
            right_support = set(shifted_source) | set(shifted_allowed)
            tag = f"{offset}/h{horizon}"

            check(
                f"B {tag} supports are disjoint at strict-NN distance two",
                left_support.isdisjoint(right_support)
                and minimum_cross_distance(left_support, right_support) == 2,
            )

            single = c63.exact_graph(source, c80.CONSTRUCTION.table, allowed)
            shifted = c63.exact_graph(
                shifted_source, c80.CONSTRUCTION.table, shifted_allowed
            )
            joint = c63.exact_graph(
                source | shifted_source,
                c80.CONSTRUCTION.table,
                allowed | shifted_allowed,
            )
            state_pairs = projected_state_pairs(joint, single, shifted)
            cartesian = frozenset(product(single.states, shifted.states))

            check(
                f"B {tag} condition set is the disjoint union",
                joint.conditions == single.conditions + shifted.conditions,
                str((joint.conditions, single.conditions, shifted.conditions)),
            )
            check(
                f"B {tag} reachable graph is the exact Cartesian product",
                state_pairs == cartesian
                and len(joint.states) == len(single.states) * len(shifted.states),
                str((len(joint.states), len(cartesian))),
            )
            check(
                f"B {tag} append-edge count factorizes",
                joint.edges
                == single.edges * len(shifted.states)
                + shifted.edges * len(single.states),
                str((joint.edges, single.edges, shifted.edges)),
            )
            check(
                f"B {tag} exposes exactly the two next seeds",
                joint.parasites == expected_parasites(horizon, offset),
                str(sorted(joint.parasites)),
            )
            check(
                f"B {tag} has no conflict or hidden dead terminal",
                not joint.conflicts and not joint.terminals,
                str((joint.conflicts, joint.terminals)),
            )


def proper_cubic_control() -> None:
    source, allowed = one_tube(3)
    offset = OFFSETS[0]
    double_source = source | translate(source, offset)
    double_allowed = allowed | translate(allowed, offset)
    expected = (144, 2_704, 5_408, 0, 2)
    failures = []
    placement = (31, -17, 9)
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        graph = c63.exact_graph(
            rotate_translate(double_source, rotation, placement),
            c80.CONSTRUCTION.table,
            rotate_translate(double_allowed, rotation, placement),
        )
        observed = (
            graph.conditions,
            len(graph.states),
            graph.edges,
            len(graph.conflicts),
            len(graph.parasites),
        )
        if observed != expected or graph.terminals:
            failures.append((rotation_index, observed, graph.terminals))
    check(
        "C01 all 24 proper-cubic images preserve the product graph",
        not failures,
        str(failures[:1]),
    )


def scope_contract() -> None:
    text = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    check("D01 note exists and carries no authority", NOTE.is_file() and "authority: none" in text)
    check("D02 note identifies a positive separation control", "positive separation control" in text)
    check("D03 note does not claim adjacent collision resolution", "does not resolve adjacent collisions" in text)
    check("D04 note denies an axiom consequence", "no axiom addition follows" in text)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    check("A01 Cycle-80 recurrent table remains 51 rows", len(c80.CONSTRUCTION.table) == 51)
    check("A02 two independent transverse offsets are declared", len(OFFSETS) == 2)
    exact_factorization_controls()
    proper_cubic_control()
    scope_contract()
    print("\nOFFSETS=2 HORIZONS=3 ROTATIONS=24")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
