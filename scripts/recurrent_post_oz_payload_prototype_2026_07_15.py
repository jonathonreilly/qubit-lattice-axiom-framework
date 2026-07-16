#!/usr/bin/env python3
"""Prototype the smallest generated post-OZ payload on two recurrent cells.

The completed recurrent socket surrounds one open notch site on five sides.
One five-parent row writes the only role absent from the retained Cycle-112
campaign, R_LB, into that site.  The already-retained covariant unary R_LB
row then writes its literal R_C22 output only through the notch's sole open
face.  Two period-adjacent sockets use the identical raw row.

Exploratory only: no foundation, registry, policy, audit, or git authority.
"""

from __future__ import annotations

from collections import Counter

import retained_source_notched_rail_nucleation_cycle141_2026_07_15 as c141


cell = c141.cell
c112 = c141.c112
screen = c141.screen
Coord = c141.Coord


def extended_standard_outputs() -> dict[Coord, str]:
    outputs = c141.standard_outputs()
    old = "B"
    for x, new in zip(range(6, 10), ("C", "D", "A", "B")):
        for yz in cell.PATHS[(old, new)]:
            outputs[cell.site(x, yz)] = cell.CONTENT[(new, yz)]
        for yz in cell.EXTRA_ORDERS[new]:
            outputs[cell.site(x, yz)] = cell.CONTENT[(new, yz)]
        old = new
    outputs[cell.site(9, cell.NOTCH_YZ)] = cell.HELPER_CONTENT
    outputs[cell.site(8, cell.NOTCH_YZ)] = cell.H1
    outputs[cell.site(7, cell.NOTCH_YZ)] = cell.OZ
    return outputs


STANDARD_RAIL_OUTPUTS = extended_standard_outputs()
RAIL_OUTPUTS = {
    c141.transform_site(site): value
    for site, value in STANDARD_RAIL_OUTPUTS.items()
}
STANDARD_RELAYS = (cell.site(3, (-1, 1)), cell.site(7, (-1, 1)))
STANDARD_PAYLOADS = (cell.site(3, (-2, 1)), cell.site(7, (-2, 1)))
STANDARD_TERMINALS = (cell.site(3, (-3, 1)), cell.site(7, (-3, 1)))
RELAYS = tuple(c141.transform_site(site) for site in STANDARD_RELAYS)
PAYLOADS = tuple(c141.transform_site(site) for site in STANDARD_PAYLOADS)
TERMINALS = tuple(c141.transform_site(site) for site in STANDARD_TERMINALS)
RELAY_VALUE = "R_LB"
PAYLOAD_VALUE = "R_C22"
TERMINAL_VALUE = "J1"


RAIL_TERMINAL = {**c141.BASE, **RAIL_OUTPUTS}
RELAY_LOCALS = tuple(
    c112.c53.local_signature(RAIL_TERMINAL, target) for target in RELAYS
)
RELAY_ROW = cell.raw_orbit(RELAY_LOCALS[0], RELAY_VALUE)
WITH_RELAYS = {
    **RAIL_TERMINAL,
    **{target: RELAY_VALUE for target in RELAYS},
}
PAYLOAD_LOCALS = tuple(
    c112.c53.local_signature(WITH_RELAYS, target) for target in PAYLOADS
)
WITH_PAYLOADS = {
    **WITH_RELAYS,
    **{target: PAYLOAD_VALUE for target in PAYLOADS},
}
TERMINAL_LOCALS = tuple(
    c112.c53.local_signature(WITH_PAYLOADS, target)
    for target in TERMINALS
)
FULL_RAW = c141.replacement_probe.merge_raw(
    c141.FULL_RAW,
    RELAY_ROW,
)


OUTPUTS = {
    **RAIL_OUTPUTS,
    **{target: RELAY_VALUE for target in RELAYS},
    **{target: PAYLOAD_VALUE for target in PAYLOADS},
    **{target: TERMINAL_VALUE for target in TERMINALS},
}
NEXT_YZ = cell.PATHS[("B", "C")][0]
IGNORED = {
    c141.transform_site(cell.site(10, NEXT_YZ)):
    frozenset((cell.CONTENT[("C", NEXT_YZ)],))
}


def sites_from_mask(sites: tuple[Coord, ...], mask: int) -> tuple[Coord, ...]:
    return tuple(site for bit, site in enumerate(sites) if mask >> bit & 1)


def causal_certificates(items, graph):
    index = graph["index"]
    certificates = []
    unresolved = []
    for target, present, neighbourhood, values in items:
        absent = set(neighbourhood) - set(present)
        reasons = []
        for child in present:
            if child not in index:
                continue
            must = graph["mandatory"][child]
            if target in index and must >> index[target] & 1:
                reasons.append(("target-before-present", target, child))
            for missing in absent:
                if missing in index and must >> index[missing] & 1:
                    reasons.append(("absent-before-present", missing, child))
        if reasons:
            certificates.append((target, tuple(sorted(set(reasons)))))
        else:
            unresolved.append((target, present, neighbourhood, values))
    return tuple(certificates), tuple(unresolved)


def corruption_controls():
    stages = (
        ("relay", RAIL_TERMINAL, RELAYS, RELAY_VALUE),
        ("payload", WITH_RELAYS, PAYLOADS, PAYLOAD_VALUE),
        ("terminal", WITH_PAYLOADS, TERMINALS, TERMINAL_VALUE),
    )
    attempts = 0
    survivors = []
    alternate_fronts = []
    descendant_failures = []
    for stage, context, targets, expected in stages:
        for copy_index, target in enumerate(targets):
            parents = tuple(
                c141.add(target, direction)
                for direction, _value in c112.c53.local_signature(context, target)
            )
            for parent in parents:
                correct = context[parent]
                for alternate in (None, *sorted(cell.FULL_ROLES - {correct})):
                    trial = dict(context)
                    if alternate is None:
                        del trial[parent]
                    else:
                        trial[parent] = alternate
                    attempts += 1
                    observed = c141.enabled(trial, FULL_RAW).get(
                        target, frozenset()
                    )
                    if expected in observed:
                        survivors.append((stage, target, parent, alternate))
                    if observed and observed != frozenset((expected,)):
                        alternate_fronts.append(
                            (stage, target, parent, alternate, observed)
                        )

                    # A different valid role may lawfully write a different
                    # record at the mutated target.  Follow that exact local
                    # branch through the remaining declared lineage and
                    # require that it never recreates the intended J1 leaf.
                    branch = dict(trial)
                    if len(observed) == 1:
                        branch[target] = next(iter(observed))
                    downstream = ()
                    if stage == "relay":
                        downstream = (
                            (PAYLOADS[copy_index], PAYLOAD_VALUE),
                            (TERMINALS[copy_index], TERMINAL_VALUE),
                        )
                    elif stage == "payload":
                        downstream = ((TERMINALS[copy_index], TERMINAL_VALUE),)
                    for child, child_expected in downstream:
                        child_observed = c141.enabled(branch, FULL_RAW).get(
                            child, frozenset()
                        )
                        if child_expected in child_observed:
                            descendant_failures.append((
                                stage, target, parent, alternate,
                                child, child_observed,
                            ))
                            break
                        if len(child_observed) == 1:
                            branch[child] = next(iter(child_observed))
                        else:
                            break
    return (
        attempts,
        tuple(survivors),
        tuple(alternate_fronts),
        tuple(descendant_failures),
    )


def main() -> int:
    print("RAIL_OUTPUTS", len(RAIL_OUTPUTS))
    print("RELAYS", RELAYS)
    print("PAYLOADS", PAYLOADS)
    print("TERMINALS", TERMINALS)
    print("RELAY_LOCALS", RELAY_LOCALS)
    print("PAYLOAD_LOCALS", PAYLOAD_LOCALS)
    print("TERMINAL_LOCALS", TERMINAL_LOCALS)
    print("ROW_SIZES", len(RELAY_ROW), len(FULL_RAW))
    print("INHERITED_PAYLOAD_ROW", c141.FULL_RAW.get(PAYLOAD_LOCALS[0]))
    print("INHERITED_TERMINAL_ROW", c141.FULL_RAW.get(TERMINAL_LOCALS[0]))
    print("SINGLE_VALUED", all(len(values) == 1 for values in FULL_RAW.values()))
    print("RELAY_SAME", RELAY_LOCALS[0] == RELAY_LOCALS[1])
    print("PAYLOAD_SAME", PAYLOAD_LOCALS[0] == PAYLOAD_LOCALS[1])

    graph = c141.exact_graph(
        c141.BASE,
        OUTPUTS,
        FULL_RAW,
        IGNORED,
        diamonds=True,
    )
    print("GRAPH", {
        key: graph[key]
        for key in (
            "states", "edges", "terminals", "max_frontier",
            "diamond_pairs",
        )
    })
    print("BAD", graph["bad"][:3])
    print("DIAMOND_FAILURES", graph["diamond_failures"][:3])
    print("REACHED", len(graph["reached"]), len(OUTPUTS))

    compiled = c112.compile_conditions(
        c141.BASE,
        OUTPUTS,
        FULL_RAW,
        IGNORED,
    )
    wrong = screen.wrong_value_details(compiled, OUTPUTS, IGNORED)
    print("UNEXPECTED", tuple(sorted(compiled.unexpected_targets))[:5], len(compiled.unexpected_targets))
    print("WRONG", wrong[:3], len(wrong))

    wrong_certificates, wrong_unresolved = causal_certificates(wrong, graph)
    unexpected_items = tuple(
        (
            target,
            sites_from_mask(compiled.sites, present),
            sites_from_mask(compiled.sites, neighbourhood),
            tuple(sorted(values)),
        )
        for target in sorted(compiled.unexpected_targets)
        for present, neighbourhood, values in compiled.conditions[target]
    )
    unexpected_certificates, unexpected_unresolved = causal_certificates(
        unexpected_items, graph
    )
    print(
        "CAUSAL_CERTIFICATES",
        len(wrong_certificates), len(wrong_unresolved),
        len(unexpected_certificates), len(unexpected_unresolved),
    )
    if wrong_unresolved:
        print("WRONG_UNRESOLVED", wrong_unresolved[:3])
    if unexpected_unresolved:
        print("UNEXPECTED_UNRESOLVED", unexpected_unresolved[:3])

    (
        attempts,
        survivors,
        alternate_fronts,
        descendant_failures,
    ) = corruption_controls()
    print(
        "CORRUPTION",
        attempts,
        len(survivors), survivors[:3],
        len(alternate_fronts), alternate_fronts[:3],
        len(descendant_failures), descendant_failures[:3],
    )

    success = (
        RELAY_LOCALS[0] == RELAY_LOCALS[1]
        and len(RELAY_LOCALS[0]) == 5
        and PAYLOAD_LOCALS[0] == PAYLOAD_LOCALS[1]
        and len(PAYLOAD_LOCALS[0]) == 1
        and TERMINAL_LOCALS[0] == TERMINAL_LOCALS[1]
        and len(TERMINAL_LOCALS[0]) == 1
        and len(RELAY_ROW) == 24
        and c141.FULL_RAW.get(PAYLOAD_LOCALS[0])
        == frozenset((PAYLOAD_VALUE,))
        and c141.FULL_RAW.get(TERMINAL_LOCALS[0])
        == frozenset((TERMINAL_VALUE,))
        and all(len(values) == 1 for values in FULL_RAW.values())
        and graph["terminals"] == 1
        and not graph["bad"]
        and not graph["diamond_failures"]
        and len(graph["reached"]) == len(OUTPUTS)
        and len(compiled.unexpected_targets) == 8
        and len(wrong_certificates) == len(wrong)
        and not wrong_unresolved
        and len(unexpected_certificates) == len(unexpected_items)
        and not unexpected_unresolved
        and attempts == 2_142
        and not survivors
        and not descendant_failures
    )
    print("RESULT", "TWO_RECURRENT_INHERITED_PAYLOADS" if success else "FAIL")
    return int(not success)


if __name__ == "__main__":
    raise SystemExit(main())
