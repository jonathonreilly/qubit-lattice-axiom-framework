#!/usr/bin/env python3
"""Cycle 142: two generated post-OZ payload lineages under one local rule.

Cycle 141 derives the recurrent notched rail from the retained Cycle-112
source.  Extending that rail by one period exposes two consecutive complete
OZ sockets.  Their identical five-wall contexts consume one new canonical
row, writing R_LB into each notch.  Two literal retained unary rows then grow
R_LB -> R_C22 -> J1 through the sole open face.

The runner exhausts the factor's asynchronous histories, proves its exact
product with the retained Cycle-112 core, certifies all static aliases as
causally unreachable, checks every proper-cubic orientation, and mutates
every direct parent through deletion and every alternate onsite role.

Authority: local exploratory evidence only.  No foundation, primitive,
registry, policy, audit, queue, commit, push, or PR is changed.
"""

from __future__ import annotations

from collections import Counter

import recurrent_post_oz_payload_prototype_2026_07_15 as p


c141 = p.c141
c112 = p.c112
cell = p.cell
screen = p.screen
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


def manhattan(left: p.Coord, right: p.Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("CONSTRUCTION")
    expected_relay_roles = {"W3", "OZ", "R_C23", "GY", "GU"}
    check(
        "two translated sockets expose the identical five-parent context",
        p.RELAY_LOCALS[0] == p.RELAY_LOCALS[1]
        and {value for _direction, value in p.RELAY_LOCALS[0]}
        == expected_relay_roles,
        p.RELAY_LOCALS,
    )
    retained_values = set(c112.SOURCE.values()) | set(c112.GROWN_OUTPUTS.values()) | set(p.RAIL_OUTPUTS.values())
    check(
        "R_LB is the sole onsite role absent from the retained physical corpus",
        cell.FULL_ROLES - retained_values == {p.RELAY_VALUE},
        tuple(sorted(cell.FULL_ROLES - retained_values)),
    )
    check(
        "the payload consumes exactly one new canonical / 24 raw rows",
        len(p.RELAY_ROW) == 24
        and p.RELAY_LOCALS[0] not in c141.FULL_RAW
        and len(p.FULL_RAW) == len(c141.FULL_RAW) + 24 == 8_360,
        (len(p.RELAY_ROW), len(p.FULL_RAW)),
    )
    check(
        "both continuation steps are literal retained unary rows",
        p.PAYLOAD_LOCALS[0] == p.PAYLOAD_LOCALS[1]
        and p.TERMINAL_LOCALS[0] == p.TERMINAL_LOCALS[1]
        and c141.FULL_RAW.get(p.PAYLOAD_LOCALS[0])
        == frozenset((p.PAYLOAD_VALUE,))
        and c141.FULL_RAW.get(p.TERMINAL_LOCALS[0])
        == frozenset((p.TERMINAL_VALUE,)),
        (p.PAYLOAD_LOCALS[0], p.TERMINAL_LOCALS[0]),
    )
    check(
        "the 8,360-row union is single-valued",
        all(len(values) == 1 for values in p.FULL_RAW.values()),
    )
    branches = tuple(zip(p.RELAYS, p.PAYLOADS, p.TERMINALS))
    cross_distance = min(
        manhattan(left, right)
        for left in branches[0]
        for right in branches[1]
    )
    check(
        "each branch is a three-record line and adjacent-period branches do not cross-contact",
        all(
            manhattan(relay, payload) == manhattan(payload, terminal) == 1
            and manhattan(relay, terminal) == 2
            for relay, payload, terminal in branches
        )
        and cross_distance == 4,
        (branches, cross_distance),
    )

    print("\nEXACT FACTOR")
    graph = c141.exact_graph(
        c141.BASE,
        p.OUTPUTS,
        p.FULL_RAW,
        p.IGNORED,
        diamonds=True,
    )
    check(
        "all 139 writes reach one complete schedule-independent terminal",
        (
            graph["states"], graph["edges"], graph["terminals"],
            len(graph["bad"]), len(graph["reached"]),
        ) == (2_240, 6_245, 1, 0, 139),
        (
            graph["states"], graph["edges"], graph["terminals"],
            graph["bad"][:2], len(graph["reached"]),
        ),
    )
    check(
        "every co-enabled append pair commutes",
        graph["diamond_pairs"] == 6_374
        and not graph["diamond_failures"],
        (graph["diamond_pairs"], graph["diamond_failures"][:2]),
    )
    check(
        "both R_LB/R_C22/J1 lineages occur in the unique terminal",
        all(site in graph["reached"] for branch in branches for site in branch),
    )

    print("\nSTATIC SCREEN AND CAUSAL FIREWALL")
    compiled = c112.compile_conditions(
        c141.BASE,
        p.OUTPUTS,
        p.FULL_RAW,
        p.IGNORED,
    )
    wrong = screen.wrong_value_details(compiled, p.OUTPUTS, p.IGNORED)
    wrong_certificates, wrong_unresolved = p.causal_certificates(wrong, graph)
    unexpected_items = tuple(
        (
            target,
            p.sites_from_mask(compiled.sites, present),
            p.sites_from_mask(compiled.sites, neighbourhood),
            tuple(sorted(values)),
        )
        for target in sorted(compiled.unexpected_targets)
        for present, neighbourhood, values in compiled.conditions[target]
    )
    unexpected_certificates, unexpected_unresolved = p.causal_certificates(
        unexpected_items, graph
    )
    check(
        "all 116 static wrong-value conditions carry causal contradictions",
        len(wrong) == len(wrong_certificates) == 116
        and not wrong_unresolved,
        (len(wrong), len(wrong_certificates), len(wrong_unresolved)),
    )
    check(
        "all eight static side aliases carry causal contradictions",
        len(compiled.unexpected_targets) == len(unexpected_items)
        == len(unexpected_certificates) == 8
        and not unexpected_unresolved,
        (
            len(compiled.unexpected_targets), len(unexpected_items),
            len(unexpected_certificates), len(unexpected_unresolved),
        ),
    )

    combined_outputs = {**c112.GROWN_OUTPUTS, **p.OUTPUTS}
    combined = c112.compile_conditions(
        c112.SOURCE,
        combined_outputs,
        p.FULL_RAW,
        p.IGNORED,
    )
    base = c112.compile_conditions(
        c112.SOURCE,
        c112.GROWN_OUTPUTS,
        c141.REPLACEMENT_RAW,
        c112.RAIL_ZERO,
    )
    combined_wrong = set(
        screen.wrong_value_details(combined, combined_outputs, p.IGNORED)
    )
    base_wrong = set(
        screen.wrong_value_details(base, c112.GROWN_OUTPUTS, c112.RAIL_ZERO)
    )
    combined_core_wrong = {
        item for item in combined_wrong if item[0] in c112.GROWN_OUTPUTS
    }
    check(
        "payload integration adds no core wrong-value fingerprint",
        not (combined_core_wrong - base_wrong),
        tuple(sorted(combined_core_wrong - base_wrong))[:2],
    )
    check(
        "factor conditions are invariant across core completion",
        c141.coordinate_fingerprints(combined, set(p.OUTPUTS))
        == c141.coordinate_fingerprints(compiled, set(p.OUTPUTS)),
    )
    cross_contacts = tuple(sorted(
        (new_site, old_site)
        for new_site in p.OUTPUTS
        for direction in cell.c52.DIRECTIONS
        if (old_site := c141.add(new_site, direction)) in c112.GROWN_OUTPUTS
    ))
    check(
        "the factor has no nearest-neighbour contact with the retained core",
        not cross_contacts,
        cross_contacts[:2],
    )

    print("\nEXACT CORE PRODUCT")
    core_states, core_edges = 73_656, 430_754
    product_states = core_states * graph["states"]
    product_edges = (
        core_edges * graph["states"]
        + core_states * graph["edges"]
    )
    check(
        "full asynchronous product state census",
        product_states == 164_989_440,
        product_states,
    )
    check(
        "full asynchronous product edge census",
        product_edges == 1_424_870_680,
        product_edges,
    )

    print("\nCOVARIANCE AND CORRUPTION")
    raw_failures = []
    raw_controls = 0
    for local, values in p.FULL_RAW.items():
        for rotation in cell.c52.ROTATIONS:
            raw_controls += 1
            if p.FULL_RAW.get(cell.c52.rotate_signature(local, rotation)) != values:
                raw_failures.append((local, rotation))
                break
    check(
        "all 200,640 proper-cubic raw images preserve output",
        raw_controls == len(p.FULL_RAW) * 24 == 200_640
        and not raw_failures,
        raw_failures[:2],
    )

    rotated = []
    shift = (29, -31, 37)
    for rotation in cell.c52.ROTATIONS:
        outcome = c141.exact_graph(
            c141.transform_records(c141.BASE, rotation, shift),
            c141.transform_records(p.OUTPUTS, rotation, shift),
            p.FULL_RAW,
            c141.transform_values(p.IGNORED, rotation, shift),
        )
        rotated.append((
            outcome["states"], outcome["edges"], outcome["terminals"],
            len(outcome["bad"]), len(outcome["reached"]),
        ))
    check(
        "all 24 orientations have the same exact factor graph",
        Counter(rotated) == {(2_240, 6_245, 1, 0, 139): 24},
        Counter(rotated),
    )

    attempts, survivors, alternate_fronts, descendant_failures = (
        p.corruption_controls()
    )
    check(
        "all 2,142 direct parent mutations suppress the intended stage",
        attempts == 2_142 and not survivors,
        (attempts, survivors[:2]),
    )
    check(
        "alternate typed fronts never recreate the intended J1 lineage",
        len(alternate_fronts) == 72 and not descendant_failures,
        (len(alternate_fronts), descendant_failures[:2]),
    )

    print("\nACCOUNTING")
    print("NEW_CANONICAL", 1)
    print("NEW_RAW", len(p.RELAY_ROW))
    print("UNION_RAW", len(p.FULL_RAW))
    print("FACTOR_OUTPUTS", len(p.OUTPUTS))
    print("FACTOR_STATES", graph["states"])
    print("FACTOR_EDGES", graph["edges"])
    print("PRODUCT_STATES", product_states)
    print("PRODUCT_EDGES", product_edges)
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "TWO_RECURRENT_POST_OZ_PAYLOADS" if FAIL == 0 else "FAIL",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
