#!/usr/bin/env python3
"""Cycle 141: derive the notched recurrent rail from the retained source.

Two source-conditioned, strict-nearest-neighbour rows write the missing lower
tail and its guard.  The existing notched rail grammar then reaches its first
complete recurrent OZ socket.  The full Cycle-112 compiler and the nucleation
factor are proved to form an exact asynchronous product.

This campaign runner has no authority.  It changes no foundation, registry,
policy, audit, or git state.
"""

from __future__ import annotations

from collections import Counter, deque
from itertools import combinations

import eight_bit_status_completion_front_cycle112_2026_07_15 as c112
import generated_endpoint_autonomous_frame_rail_cycle102_2026_07_15 as c102
import post_cycle131_outward_adapter_search_scratch as live
import relational_notched_rail_socket_prototype_2026_07_15 as cell
import relational_notched_socket_rail_replacement_probe_2026_07_15 as replacement_probe
import relational_periodic_socket_emitter_search_scratch_2026_07_15 as screen


Coord = tuple[int, int, int]
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


def transform_site(position: Coord) -> Coord:
    return add(cell.c52.matvec(c102.SEED_ROTATION, position), c102.SEED_SHIFT)


def transform_records(records: dict[Coord, str], rotation, shift: Coord):
    return {
        add(cell.c52.matvec(rotation, site), shift): value
        for site, value in records.items()
    }


def transform_values(records, rotation, shift: Coord):
    return {
        add(cell.c52.matvec(rotation, site), shift): values
        for site, values in records.items()
    }


OLD_RAIL_RAW = live.c105.REMAPPED_RAW
CORE_RAW = replacement_probe.subtract_raw(c112.FULL_RAW, OLD_RAIL_RAW)
REPLACEMENT_RAW = replacement_probe.merge_raw(CORE_RAW, cell.RAW)

LOWER = transform_site(cell.site(0, cell.LOWER_YZ))
GUARD = transform_site(cell.site(0, cell.GUARD_YZ))
LOWER_VALUE = cell.CONTENT[("A", cell.LOWER_YZ)]
GUARD_VALUE = cell.CONTENT[("A", cell.GUARD_YZ)]
LOWER_LOCAL = c112.c53.local_signature(c112.SOURCE, LOWER)
LOWER_ROW = cell.raw_orbit(LOWER_LOCAL, LOWER_VALUE)
LOWER_CONTEXT = {**c112.SOURCE, LOWER: LOWER_VALUE}
GUARD_LOCAL = c112.c53.local_signature(LOWER_CONTEXT, GUARD)
GUARD_ROW = cell.raw_orbit(GUARD_LOCAL, GUARD_VALUE)
FULL_RAW = replacement_probe.merge_raw(REPLACEMENT_RAW, LOWER_ROW, GUARD_ROW)


def standard_outputs() -> dict[Coord, str]:
    outputs = {
        cell.site(0, cell.LOWER_YZ): LOWER_VALUE,
        cell.site(0, cell.GUARD_YZ): GUARD_VALUE,
    }
    old = "A"
    for x, new in zip(range(1, 6), ("B", "C", "D", "A", "B")):
        for yz in cell.PATHS[(old, new)]:
            outputs[cell.site(x, yz)] = cell.CONTENT[(new, yz)]
        for yz in cell.EXTRA_ORDERS[new]:
            outputs[cell.site(x, yz)] = cell.CONTENT[(new, yz)]
        old = new

    # The actual retained source has a permanent W5 beside the startup H1
    # target.  It blocks that non-load-bearing partial socket.  The startup
    # helper remains a modeled output; the first complete socket is at x=3.
    outputs[cell.site(1, cell.NOTCH_YZ)] = cell.HELPER_CONTENT
    outputs[cell.site(5, cell.NOTCH_YZ)] = cell.HELPER_CONTENT
    outputs[cell.site(4, cell.NOTCH_YZ)] = cell.H1
    outputs[cell.site(3, cell.NOTCH_YZ)] = cell.OZ
    return outputs


STANDARD_OUTPUTS = standard_outputs()
OUTPUTS = {transform_site(site): value for site, value in STANDARD_OUTPUTS.items()}
NEXT_YZ = cell.PATHS[("B", "C")][0]
IGNORED = {
    transform_site(cell.site(6, NEXT_YZ)):
    frozenset((cell.CONTENT[("C", NEXT_YZ)],))
}
BASE = c112.positive_terminal_records()


def enabled(records, raw=FULL_RAW):
    return {
        target: raw[local]
        for target in c112.c53.open_candidates(records)
        if (local := c112.c53.local_signature(records, target)) in raw
    }


def exact_graph(source, outputs, raw, ignored, *, diamonds=False):
    sites = tuple(sorted(outputs))
    index = {site: bit for bit, site in enumerate(sites)}
    all_mask = (1 << len(sites)) - 1
    queue = deque((0,))
    seen = {0}
    edges = 0
    bad = []
    terminals = 0
    max_frontier = 0
    mandatory = {site: all_mask for site in sites}
    append_seen = Counter()
    diamond_pairs = 0
    diamond_failures = []
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
        actual = {
            target: raw[local]
            for target in c112.c53.open_candidates(records)
            if (local := c112.c53.local_signature(records, target)) in raw
        }
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
        futures = tuple(sorted(
            target
            for target, values in actual.items()
            if target in index
            and not (mask >> index[target] & 1)
            and values == frozenset((outputs[target],))
        ))
        max_frontier = max(max_frontier, len(futures))
        if not futures:
            bad.append((mask.bit_count(), "dead", actual))
            continue
        if diamonds:
            for left, right in combinations(futures, 2):
                diamond_pairs += 1
                after_left = {**records, left: outputs[left]}
                after_right = {**records, right: outputs[right]}
                left_enabled = {
                    target: raw[local]
                    for target in c112.c53.open_candidates(after_left)
                    if (local := c112.c53.local_signature(after_left, target)) in raw
                }
                right_enabled = {
                    target: raw[local]
                    for target in c112.c53.open_candidates(after_right)
                    if (local := c112.c53.local_signature(after_right, target)) in raw
                }
                if (
                    left_enabled.get(right) != frozenset((outputs[right],))
                    or right_enabled.get(left) != frozenset((outputs[left],))
                ):
                    diamond_failures.append((mask.bit_count(), left, right))
        for target in futures:
            mandatory[target] &= mask
            append_seen[target] += 1
            future = mask | (1 << index[target])
            edges += 1
            if future not in seen:
                seen.add(future)
                queue.append(future)
    reached = frozenset(
        site for site, bit in index.items() if reached_mask >> bit & 1
    )
    return {
        "states": len(seen),
        "edges": edges,
        "terminals": terminals,
        "bad": tuple(bad),
        "max_frontier": max_frontier,
        "mandatory": mandatory,
        "append_seen": append_seen,
        "diamond_pairs": diamond_pairs,
        "diamond_failures": tuple(diamond_failures),
        "reached": reached,
        "index": index,
    }


FACTOR = exact_graph(BASE, OUTPUTS, FULL_RAW, IGNORED, diamonds=True)


def coordinate_fingerprints(compiled, targets):
    def sites(mask: int):
        return tuple(
            site
            for bit, site in enumerate(compiled.sites)
            if mask >> bit & 1
        )

    return frozenset(
        (target, sites(present), sites(neighbourhood), tuple(sorted(values)))
        for target, conditions in compiled.conditions.items()
        if target in targets
        for present, neighbourhood, values in conditions
    )


def causal_certificates(wrong):
    index = FACTOR["index"]
    certificates = []
    unresolved = []
    for target, present, neighbourhood, values in wrong:
        absent = set(neighbourhood) - set(present)
        reasons = []
        for child in present:
            if child not in index:
                continue
            must = FACTOR["mandatory"][child]
            if target in index and must >> index[target] & 1:
                reasons.append(("target-before-present", target, child))
            for missing in absent:
                if missing in index and must >> index[missing] & 1:
                    reasons.append(("absent-before-present", missing, child))
        if reasons:
            certificates.append((target, present, values, tuple(sorted(set(reasons)))))
        else:
            unresolved.append((target, present, neighbourhood, values))
    return tuple(certificates), tuple(unresolved)


def direct_corruption_controls():
    stages = (
        ("lower", dict(c112.SOURCE), LOWER, LOWER_VALUE),
        ("guard", {**c112.SOURCE, LOWER: LOWER_VALUE}, GUARD, GUARD_VALUE),
    )
    attempts = 0
    failures = []
    same_value_fallbacks = []
    wrong_outputs = []
    for stage, context, target, expected in stages:
        parents = tuple(
            add(target, direction) for direction, _value in c112.c53.local_signature(context, target)
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
                observed = enabled(trial).get(target, frozenset())
                if observed and observed != frozenset((expected,)):
                    wrong_outputs.append((stage, parent, alternate, observed))
                if expected in observed:
                    signature = c112.c53.local_signature(trial, target)
                    fallback = (
                        stage == "guard"
                        and parent == add(GUARD, (1, 0, 0))
                        and alternate is None
                        and cell.RAW.get(signature) == frozenset((expected,))
                        and signature not in GUARD_ROW
                    )
                    if fallback:
                        same_value_fallbacks.append(
                            (stage, parent, alternate, signature)
                        )
                    else:
                        failures.append((stage, parent, alternate, signature))
    return (
        attempts,
        tuple(failures),
        tuple(same_value_fallbacks),
        tuple(wrong_outputs),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("SOURCE-CONDITIONED ROWS")
    check(
        "lower row has the exact three independent source parents",
        tuple(value for _direction, value in LOWER_LOCAL) == ("A_0_2", "W1", "W3"),
        LOWER_LOCAL,
    )
    check(
        "guard row absorbs the exact retained W4 neighbour",
        tuple(value for _direction, value in GUARD_LOCAL) == ("A_0_1", "T_H3", "W4"),
        GUARD_LOCAL,
    )
    check("each adapter row has 24 proper-cubic images", len(LOWER_ROW) == len(GUARD_ROW) == 24)
    check("adapter signatures are new to the replacement grammar", LOWER_LOCAL not in REPLACEMENT_RAW and GUARD_LOCAL not in REPLACEMENT_RAW)
    check("full 8336-row raw union is single-valued", len(FULL_RAW) == 8336 and all(len(v) == 1 for v in FULL_RAW.values()), len(FULL_RAW))

    print("\nFACTOR GRAPH")
    check("actual source contributes no output site", not (set(OUTPUTS) & set(BASE)))
    check("nucleation has 75 generated records", len(OUTPUTS) == 75, len(OUTPUTS))
    check(
        "exact factor census",
        (FACTOR["states"], FACTOR["edges"], FACTOR["terminals"], len(FACTOR["bad"]))
        == (260, 499, 1, 0),
        (FACTOR["states"], FACTOR["edges"], FACTOR["terminals"], FACTOR["bad"][:2]),
    )
    check("factor reaches every declared output", len(FACTOR["reached"]) == len(OUTPUTS), len(FACTOR["reached"]))
    first_oz = transform_site(cell.site(3, cell.NOTCH_YZ))
    check("factor reaches the first complete recurrent OZ", first_oz in FACTOR["reached"], first_oz)
    check(
        "all co-enabled factor actions commute",
        FACTOR["diamond_pairs"] > 0 and not FACTOR["diamond_failures"],
        (FACTOR["diamond_pairs"], FACTOR["diamond_failures"][:2]),
    )

    print("\nSTATIC SCREEN AND CAUSAL FIREWALL")
    factor_compiled = c112.compile_conditions(BASE, OUTPUTS, FULL_RAW, IGNORED)
    factor_wrong = screen.wrong_value_details(factor_compiled, OUTPUTS, IGNORED)
    certificates, unresolved = causal_certificates(factor_wrong)
    check("factor compiler has no unexpected target", not factor_compiled.unexpected_targets, tuple(sorted(factor_compiled.unexpected_targets)))
    check("all 48 static wrong warnings are explicit", len(factor_wrong) == 48, len(factor_wrong))
    check("every static warning has a causal contradiction", len(certificates) == 48 and not unresolved, (len(certificates), len(unresolved)))

    combined_outputs = {**c112.GROWN_OUTPUTS, **OUTPUTS}
    combined_compiled = c112.compile_conditions(c112.SOURCE, combined_outputs, FULL_RAW, IGNORED)
    combined_wrong = set(screen.wrong_value_details(combined_compiled, combined_outputs, IGNORED))
    base_compiled = c112.compile_conditions(
        c112.SOURCE, c112.GROWN_OUTPUTS, REPLACEMENT_RAW, c112.RAIL_ZERO
    )
    base_wrong = set(screen.wrong_value_details(
        base_compiled, c112.GROWN_OUTPUTS, c112.RAIL_ZERO
    ))
    combined_core_wrong = {item for item in combined_wrong if item[0] in c112.GROWN_OUTPUTS}
    check("combined compiler has no unexpected target", not combined_compiled.unexpected_targets, tuple(sorted(combined_compiled.unexpected_targets)))
    check("adapter adds no core wrong-value fingerprint", not (combined_core_wrong - base_wrong), tuple(sorted(combined_core_wrong - base_wrong))[:2])
    check(
        "new-output conditions are invariant across core completion",
        coordinate_fingerprints(combined_compiled, set(OUTPUTS))
        == coordinate_fingerprints(factor_compiled, set(OUTPUTS)),
    )
    cross_adjacency = tuple(sorted(
        (new_site, old_site)
        for new_site in OUTPUTS
        for direction in cell.c52.DIRECTIONS
        if (old_site := add(new_site, direction)) in c112.GROWN_OUTPUTS
    ))
    check("new and core outputs have no nearest-neighbour contact", not cross_adjacency, cross_adjacency[:2])

    print("\nEXACT PRODUCT")
    core_states, core_edges = 73_656, 430_754
    product_states = core_states * FACTOR["states"]
    product_edges = core_edges * FACTOR["states"] + core_states * FACTOR["edges"]
    check("product state census", product_states == 19_150_560, product_states)
    check("product edge census", product_edges == 148_750_384, product_edges)

    print("\nCOVARIANCE AND CORRUPTION")
    rotated = []
    for rotation in cell.c52.ROTATIONS:
        shift0 = (17, -19, 23)
        outcome = exact_graph(
            transform_records(BASE, rotation, shift0),
            transform_records(OUTPUTS, rotation, shift0),
            FULL_RAW,
            transform_values(IGNORED, rotation, shift0),
        )
        rotated.append((
            outcome["states"], outcome["edges"], outcome["terminals"],
            len(outcome["bad"]), len(outcome["reached"]),
        ))
    check(
        "all 24 proper-cubic factors have the same exact graph",
        len(rotated) == 24 and set(rotated) == {(260, 499, 1, 0, 75)},
        Counter(rotated),
    )
    (
        attempts,
        corruption_failures,
        same_value_fallbacks,
        corruption_wrong_outputs,
    ) = direct_corruption_controls()
    check(
        "917 direct parent corruptions suppress the intended adapter output",
        attempts == 918
        and len(same_value_fallbacks) == 1
        and not corruption_failures,
        (attempts, same_value_fallbacks, corruption_failures[:3]),
    )
    check(
        "the sole survivor is the pre-existing two-parent guard fallback",
        same_value_fallbacks == ((
            "guard",
            add(GUARD, (1, 0, 0)),
            None,
            (((0, 0, 1), "A_0_1"), ((0, 1, 0), "T_H3")),
        ),),
        same_value_fallbacks,
    )
    check(
        "no direct parent corruption selects a wrong target value",
        not corruption_wrong_outputs,
        corruption_wrong_outputs[:3],
    )

    print("\nACCOUNTING")
    print("CORE_RAW", len(CORE_RAW))
    print("RECURRENT_RAW", len(cell.RAW))
    print("ADAPTER_RAW", len(LOWER_ROW) + len(GUARD_ROW))
    print("FULL_RAW", len(FULL_RAW))
    print("NUCLEATION_OUTPUTS", len(OUTPUTS))
    print("PRODUCT_STATES", product_states)
    print("PRODUCT_EDGES", product_edges)
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "RETAINED_SOURCE_NOTCHED_RAIL_NUCLEATION"
        if FAIL == 0 else "FAIL",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
