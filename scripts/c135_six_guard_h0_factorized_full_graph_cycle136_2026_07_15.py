#!/usr/bin/env python3
"""Cycle 136: exact factorized full graph for the six-image guarded H0.

Direct enumeration would contain 444,969,984 states.  This runner proves the
exact graph product from checked dependency separation: six R_C30 guards see
source records only; the new H0 waits for three causally prior base-variable
parents and two named guards.  An exact second traversal of the Cycle-135 graph
counts the joint parent-present layer consumed by the product.

The complete eight-write factor is still enumerated directly.  The full state
and edge counts are then computed exactly from the executable Cycle-135 graph,
the independent Q6 guard cube, and the conditioned H0 layer.  This is bounded
candidate evidence, not foundation or audit authority.
"""

from __future__ import annotations

from collections import deque
from pathlib import Path

import c132_cage_first_bit_successor_boundary_cycle135_2026_07_15 as c135


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "C135_SIX_GUARD_H0_FACTORIZED_FULL_GRAPH_CYCLE136_NOTE_2026-07-15.md"

c129 = c135.c129
c112 = c135.c112
c59 = c135.c59
c53 = c135.c53

Coord = c135.Coord
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def wrong_value_conditions(compiled, outputs):
    """Expected targets that have any compiled value other than their model."""
    return tuple(sorted(
        (
            target,
            tuple(sorted({
                tuple(sorted(values))
                for _present, _mask, values in conditions
                if values != frozenset((outputs[target],))
            })),
        )
        for target, conditions in compiled.conditions.items()
        if target in outputs
        and any(
            values != frozenset((outputs[target],))
            for _present, _mask, values in conditions
        )
    ))


def wrong_value_condition_details(compiled, outputs):
    """Coordinate-normalized fingerprints retaining every compiled mask."""
    def sites(mask: int):
        return tuple(
            site
            for index, site in enumerate(compiled.sites)
            if mask >> index & 1
        )

    return tuple(sorted(
        (target, sites(present), sites(neighbourhood), tuple(sorted(values)))
        for target, conditions in compiled.conditions.items()
        if target in outputs
        for present, neighbourhood, values in conditions
        if values != frozenset((outputs[target],))
    ))


def condition_details(compiled, targets):
    """Every condition fingerprint, normalized from bit masks to coordinates."""
    def sites(mask: int):
        return tuple(
            site
            for index, site in enumerate(compiled.sites)
            if mask >> index & 1
        )

    return tuple(sorted(
        (target, sites(present), sites(neighbourhood), tuple(sorted(values)))
        for target, conditions in compiled.conditions.items()
        if target in targets
        for present, neighbourhood, values in conditions
    ))


def joint_layer_census(compiled, outputs, ignored, required_sites):
    """Re-enumerate the exact base graph and count a required-present layer."""
    actions = tuple(
        (
            compiled.index.get(target),
            target,
            conditions,
            frozenset((outputs[target],)) if target in outputs else None,
            ignored.get(target),
        )
        for target, conditions in compiled.conditions.items()
    )
    required_mask = sum(1 << compiled.index[site] for site in required_sites)
    queue = deque((0,))
    seen = {0}
    edges = 0
    joint_states = 0
    joint_edges = 0
    terminals = 0
    joint_terminals = 0
    bad: list[object] = []
    next_progress = 1_000_000

    while queue:
        state = queue.popleft()
        is_joint = state & required_mask == required_mask
        legal: list[int] = []
        for index, target, conditions, expected, ignored_value in actions:
            if index is not None and state >> index & 1:
                continue
            for present, neighbourhood, values in conditions:
                if state & neighbourhood != present:
                    continue
                if ignored_value is not None and values == ignored_value:
                    break
                if index is not None and values == expected:
                    legal.append(index)
                    break
                bad.append((state, target, values))
                queue.clear()
                break
            if bad:
                break
        if bad:
            break

        if is_joint:
            joint_states += 1
            joint_edges += len(legal)
        if not legal:
            terminals += 1
            if is_joint:
                joint_terminals += 1
        edges += len(legal)
        for index in legal:
            future = state | 1 << index
            if future not in seen:
                seen.add(future)
                queue.append(future)
        if len(seen) >= next_progress:
            print(
                f"JOINT_PROGRESS states={len(seen)} "
                f"joint={joint_states} joint_edges={joint_edges}",
                flush=True,
            )
            next_progress += 1_000_000

    return (
        len(seen), edges, terminals, joint_states, joint_edges,
        joint_terminals, tuple(bad),
    )


GUARD_SITE: Coord = (5, -2, -2)
GUARD_OUTPUT = "R_C30"
GUARD_LOCAL = c53.local_signature(c135.CAGE_RECORDS, GUARD_SITE)
GUARD_CANONICAL = c53.canonical_signature(GUARD_LOCAL)
GUARD_RAW = c59.raw_rule_outputs({GUARD_CANONICAL: GUARD_OUTPUT})
GUARD_TARGETS = tuple(sorted(
    site
    for site in c53.open_candidates(c135.CAGE_RECORDS)
    if c53.local_signature(c135.CAGE_RECORDS, site) in GUARD_RAW
))
GUARD_OUTPUTS = {site: GUARD_OUTPUT for site in GUARD_TARGETS}

H0_SITE: Coord = (5, -1, -2)
H0_OUTPUT = "H0"
H0_BASE_PARENTS = frozenset({
    c135.BIT,
    (4, -1, -2),
    (5, -1, -1),
})
LOCAL_GUARDS = frozenset({(5, -2, -2), (5, -1, -3)})
PREFIX_RECORDS = {
    **c135.CAGE_RECORDS,
    **GUARD_OUTPUTS,
    c135.BIT: c135.BIT_OUTPUT,
}
H0_LOCAL = c53.local_signature(PREFIX_RECORDS, H0_SITE)
H0_CANONICAL = c53.canonical_signature(H0_LOCAL)
H0_RAW = c59.raw_rule_outputs({H0_CANONICAL: H0_OUTPUT})
H0_TARGETS = tuple(sorted(
    site
    for site in c53.open_candidates(PREFIX_RECORDS)
    if c53.local_signature(PREFIX_RECORDS, site) in H0_RAW
))

FULL_RAW = c112.merge_raw(c135.FULL_RAW, GUARD_RAW, H0_RAW)
FACTOR_OUTPUTS = {
    **GUARD_OUTPUTS,
    c135.BIT: c135.BIT_OUTPUT,
    H0_SITE: H0_OUTPUT,
}
GROWN_OUTPUTS = {
    **c135.GROWN_OUTPUTS,
    **GUARD_OUTPUTS,
    H0_SITE: H0_OUTPUT,
}
FACTOR = c112.append_graph(
    source=c135.CAGE_RECORDS,
    outputs=FACTOR_OUTPUTS,
    raw=FULL_RAW,
    ignored=c129.IGNORED_NEXT,
    state_limit=100_000,
)
ALL_FACTOR_MASK = (1 << len(FACTOR_OUTPUTS)) - 1
FULL_COMPILED = c112.compile_conditions(
    c112.SOURCE, GROWN_OUTPUTS, FULL_RAW, c129.IGNORED_NEXT
)
BASE_COMPILED = c112.compile_conditions(
    c112.SOURCE, c135.GROWN_OUTPUTS, c135.FULL_RAW, c129.IGNORED_NEXT
)
BASE_WRONG_VALUES = wrong_value_conditions(BASE_COMPILED, c135.GROWN_OUTPUTS)
FULL_WRONG_VALUES = wrong_value_conditions(FULL_COMPILED, GROWN_OUTPUTS)
BASE_WRONG_DETAILS = wrong_value_condition_details(
    BASE_COMPILED, c135.GROWN_OUTPUTS
)
FULL_WRONG_DETAILS = wrong_value_condition_details(
    FULL_COMPILED, GROWN_OUTPUTS
)
NEW_OUTPUT_SITES = set(GUARD_TARGETS) | {H0_SITE}
NEW_OUTPUT_WRONG_VALUES = tuple(
    item for item in FULL_WRONG_VALUES if item[0] in NEW_OUTPUT_SITES
)
NEW_OUTPUT_WRONG_DETAILS = tuple(
    item for item in FULL_WRONG_DETAILS if item[0] in NEW_OUTPUT_SITES
)

BASE_NONPARENT_DETAILS = condition_details(
    BASE_COMPILED, set(c135.GROWN_OUTPUTS) - H0_BASE_PARENTS
)
FULL_NONPARENT_DETAILS = condition_details(
    FULL_COMPILED, set(c135.GROWN_OUTPUTS) - H0_BASE_PARENTS
)
BASE_PARENT_DETAILS = condition_details(BASE_COMPILED, H0_BASE_PARENTS)
FULL_PARENT_DETAILS = condition_details(FULL_COMPILED, H0_BASE_PARENTS)
FULL_PARENT_H0_ABSENT_PROJECTED = tuple(sorted(
    (
        target,
        present,
        tuple(site for site in neighbourhood if site != H0_SITE),
        values,
    )
    for target, present, neighbourhood, values in FULL_PARENT_DETAILS
    if H0_SITE not in present
))
FULL_PARENT_H0_PRESENT = tuple(
    item for item in FULL_PARENT_DETAILS if H0_SITE in item[1]
)
BASE_IGNORED_DETAILS = condition_details(BASE_COMPILED, set(c129.IGNORED_NEXT))
FULL_IGNORED_DETAILS = condition_details(FULL_COMPILED, set(c129.IGNORED_NEXT))
H0_CONDITION_DETAILS = condition_details(FULL_COMPILED, {H0_SITE})


def completion_violations() -> tuple[int, ...]:
    compiled = c112.compile_conditions(
        c135.CAGE_RECORDS, FACTOR_OUTPUTS, FULL_RAW, c129.IGNORED_NEXT
    )
    actions = tuple(
        (compiled.index.get(target), target, conditions)
        for target, conditions in compiled.conditions.items()
    )
    h0_bit = 1 << compiled.index[H0_SITE]
    required_sites = {
        c135.BIT,
        (5, -2, -2),
        (5, -1, -3),
    }
    required_mask = sum(1 << compiled.index[site] for site in required_sites)
    queue = deque((0,))
    seen = {0}
    violations: list[int] = []
    while queue:
        state = queue.popleft()
        if state & h0_bit and state & required_mask != required_mask:
            violations.append(state)
        legal: list[int] = []
        for index, target, conditions in actions:
            if index is not None and state >> index & 1:
                continue
            for present, neighbourhood, values in conditions:
                if state & neighbourhood != present:
                    continue
                if target in c129.IGNORED_NEXT and values == c129.IGNORED_NEXT[target]:
                    break
                if index is not None and values == frozenset((FACTOR_OUTPUTS[target],)):
                    legal.append(index)
                    break
                raise RuntimeError((state, target, values))
        for index in legal:
            future = state | 1 << index
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return tuple(violations)


# Exact graph product.  H0 can exist only in the exact Cycle-135 layer where
# all three old variable parents are present.  Count that layer and its induced
# old edges by an independent traversal; do not infer it by subtraction.
BASE_STATES = c135.POSITIVE.states
BASE_EDGES = c135.POSITIVE.edges
BASE_TERMINALS = c135.POSITIVE.terminals
JOINT_CENSUS = joint_layer_census(
    BASE_COMPILED,
    c135.GROWN_OUTPUTS,
    c129.IGNORED_NEXT,
    H0_BASE_PARENTS,
)
(
    JOINT_BASE_STATES,
    JOINT_BASE_EDGES,
    JOINT_BASE_TERMINALS,
    JOINT_STATES,
    JOINT_EDGES,
    JOINT_TERMINALS,
    JOINT_BAD,
) = JOINT_CENSUS

GUARD_SUBSETS = 1 << len(GUARD_TARGETS)
GUARD_CUBE_EDGES = len(GUARD_TARGETS) * (1 << (len(GUARD_TARGETS) - 1))
H0_ELIGIBLE_GUARD_SUBSETS = 1 << (len(GUARD_TARGETS) - 2)
H0_LAYER_GUARD_EDGES = (len(GUARD_TARGETS) - 2) * (
    1 << (len(GUARD_TARGETS) - 3)
)

FACTORIZED_STATES = (
    GUARD_SUBSETS * BASE_STATES
    + H0_ELIGIBLE_GUARD_SUBSETS * JOINT_STATES
)
FACTORIZED_EDGES = (
    GUARD_SUBSETS * BASE_EDGES
    + GUARD_CUBE_EDGES * BASE_STATES
    + H0_ELIGIBLE_GUARD_SUBSETS * JOINT_STATES
    + H0_ELIGIBLE_GUARD_SUBSETS * JOINT_EDGES
    + H0_LAYER_GUARD_EDGES * JOINT_STATES
)
FACTORIZED_TERMINALS = BASE_TERMINALS


BASE_TERMINAL_RECORDS = c135.positive_terminal_records()
PRE_H0_TERMINAL_RECORDS = {**BASE_TERMINAL_RECORDS, **GUARD_OUTPUTS}
FINAL_TERMINAL_RECORDS = {
    **PRE_H0_TERMINAL_RECORDS,
    H0_SITE: H0_OUTPUT,
}


def enabled_nonignored(records):
    enabled = {}
    for target in c53.open_candidates(records):
        values = FULL_RAW.get(c53.local_signature(records, target))
        if values is None:
            continue
        if target in c129.IGNORED_NEXT and values == c129.IGNORED_NEXT[target]:
            continue
        enabled[target] = values
    return enabled


# Wrong-output fork.  Replacing H0 with H1 is also compiler/factor clean, so
# this probe establishes formation and order but does not select bit value 0.
WRONG_H1_RAW = c59.raw_rule_outputs({H0_CANONICAL: "H1"})
WRONG_H1_UNION = c112.merge_raw(c135.FULL_RAW, GUARD_RAW, WRONG_H1_RAW)
WRONG_H1_OUTPUTS = {**GUARD_OUTPUTS, c135.BIT: c135.BIT_OUTPUT, H0_SITE: "H1"}
WRONG_H1_GROWN = {**c135.GROWN_OUTPUTS, **GUARD_OUTPUTS, H0_SITE: "H1"}
WRONG_H1_COMPILED = c112.compile_conditions(
    c112.SOURCE, WRONG_H1_GROWN, WRONG_H1_UNION, c129.IGNORED_NEXT
)
WRONG_H1_WRONG_VALUES = wrong_value_conditions(
    WRONG_H1_COMPILED, WRONG_H1_GROWN
)
WRONG_H1_WRONG_DETAILS = wrong_value_condition_details(
    WRONG_H1_COMPILED, WRONG_H1_GROWN
)
WRONG_H1_NEW_WRONG_VALUES = tuple(
    item
    for item in WRONG_H1_WRONG_VALUES
    if item[0] in NEW_OUTPUT_SITES | {c135.BIT}
)
WRONG_H1_FACTOR = c112.append_graph(
    source=c135.CAGE_RECORDS,
    outputs=WRONG_H1_OUTPUTS,
    raw=WRONG_H1_UNION,
    ignored=c129.IGNORED_NEXT,
    state_limit=100_000,
)


def contract() -> None:
    section("A - Six-image guard and unique H0 local")
    check("A01 Cycle 136 note exists", NOTE.is_file())
    check(
        "A02 tested guard local is L4+L6 with six explicit images",
        GUARD_LOCAL == (((-1, 0, 0), "L4"), ((0, 0, 1), "L6"))
        and GUARD_TARGETS
        == (
            (1, -5, -3), (1, -2, -6), (2, -5, -2),
            (2, -1, -6), (5, -2, -2), (5, -1, -3),
        ),
        str(GUARD_TARGETS),
    )
    check(
        "A03 H0 requires three prior base-variable parents and two guards",
        H0_LOCAL
        == (
            ((-1, 0, 0), "H1"),
            ((0, -1, 0), "R_C30"),
            ((0, 0, -1), "R_C30"),
            ((0, 0, 1), "H0"),
            ((0, 1, 0), "H1"),
        ),
        str(H0_LOCAL),
    )
    check("A04 guarded H0 has one exact terminal target", H0_TARGETS == (H0_SITE,))
    check(
        "A05 union has 9,278 single-valued rows and zero unexpected targets",
        len(FULL_RAW) == 9_278
        and all(len(values) == 1 for values in FULL_RAW.values())
        and len(GROWN_OUTPUTS) == 142
        and len(FULL_COMPILED.conditions) == 143
        and not FULL_COMPILED.unexpected_targets,
    )
    check(
        "A06 new guard/H0 targets have zero expected-target wrong-value aliases",
        not NEW_OUTPUT_WRONG_VALUES and not NEW_OUTPUT_WRONG_DETAILS,
        str(NEW_OUTPUT_WRONG_DETAILS),
    )
    exact_h0_parents = tuple(sorted(H0_BASE_PARENTS | LOCAL_GUARDS))
    check(
        "A07 H0 has one exact all-five-parent compiled condition",
        H0_CONDITION_DETAILS
        == ((
            H0_SITE,
            exact_h0_parents,
            exact_h0_parents,
            (H0_OUTPUT,),
        ),),
        str(H0_CONDITION_DETAILS),
    )

    section("B - Enumerated factor and completion barrier")
    check(
        "B01 complete factor is 144 states / 496 edges / one terminal",
        FACTOR.states == 144
        and FACTOR.edges == 496
        and FACTOR.terminals == 1
        and FACTOR.terminal_states == (ALL_FACTOR_MASK,)
        and FACTOR.terminal_sizes == (8,)
        and FACTOR.max_frontier == 7
        and not FACTOR.bad
        and not FACTOR.unexpected_condition_targets,
    )
    check("B02 H0 never precedes H1 or either local guard", not completion_violations())
    final_prefix = {**c135.CAGE_RECORDS, **FACTOR_OUTPUTS}
    deletion_failures = []
    for parent in (c135.BIT, (5, -2, -2), (5, -1, -3), (4, -1, -2), (5, -1, -1)):
        records = dict(final_prefix)
        records.pop(parent)
        local = c53.local_signature(records, H0_SITE)
        if local in FULL_RAW and FULL_RAW[local] == frozenset((H0_OUTPUT,)):
            deletion_failures.append(parent)
    check("B03 deleting any H0 parent disables H0", not deletion_failures, str(deletion_failures))

    section("C - Exact factorized full-graph census")
    base_variable_sites = set(c135.GROWN_OUTPUTS)
    guard_neighbour_failures = []
    for guard in GUARD_TARGETS:
        variable_neighbours = {
            c53.add(guard, direction)
            for direction in c53.DIRECTIONS
        } & base_variable_sites
        if variable_neighbours:
            guard_neighbour_failures.append((guard, variable_neighbours))
    guard_adjacencies = []
    for index, guard in enumerate(GUARD_TARGETS):
        neighbours = {
            c53.add(guard, direction) for direction in c53.DIRECTIONS
        }
        for other in GUARD_TARGETS[index + 1:]:
            if other in neighbours:
                guard_adjacencies.append((guard, other))
    check(
        "C01 guards see source only and are pairwise nonadjacent",
        not guard_neighbour_failures and not guard_adjacencies,
        f"base={guard_neighbour_failures} pairs={guard_adjacencies}",
    )
    h0_variable_neighbours = {
        c53.add(H0_SITE, direction) for direction in c53.DIRECTIONS
    } & (base_variable_sites | set(GUARD_TARGETS))
    required_h0_variable_neighbours = H0_BASE_PARENTS | LOCAL_GUARDS
    nonlocal_guards = set(GUARD_TARGETS) - LOCAL_GUARDS
    check(
        "C02 H0 sees exactly three old parents and two local guards",
        h0_variable_neighbours == required_h0_variable_neighbours
        and len(nonlocal_guards) == 4
        and not (h0_variable_neighbours & nonlocal_guards),
        str(h0_variable_neighbours),
    )
    check(
        "C03 all old nonparent condition fingerprints are exactly preserved",
        len(BASE_NONPARENT_DETAILS) == 181
        and FULL_NONPARENT_DETAILS == BASE_NONPARENT_DETAILS,
        f"base={len(BASE_NONPARENT_DETAILS)} full={len(FULL_NONPARENT_DETAILS)}",
    )
    check(
        "C04 parent conditions are the exact H0-absent base conditions",
        len(BASE_PARENT_DETAILS) == 3
        and len(FULL_PARENT_DETAILS) == 3
        and FULL_PARENT_H0_ABSENT_PROJECTED == BASE_PARENT_DETAILS
        and not FULL_PARENT_H0_PRESENT
        and all(
            H0_SITE in neighbourhood
            for _target, _present, neighbourhood, _values
            in FULL_PARENT_DETAILS
        ),
    )
    ignored_values_safe = all(
        values == tuple(sorted(c129.IGNORED_NEXT[target]))
        for target, _present, _neighbourhood, values in FULL_IGNORED_DETAILS
    )
    check(
        "C05 ignored-target condition and value are unchanged",
        len(BASE_IGNORED_DETAILS) == 1
        and FULL_IGNORED_DETAILS == BASE_IGNORED_DETAILS
        and ignored_values_safe,
        str(FULL_IGNORED_DETAILS),
    )
    inherited_wrong_targets = {target for target, _values in FULL_WRONG_VALUES}
    check(
        "C06 all 40 wrong-condition fingerprints are exactly inherited",
        len(FULL_WRONG_VALUES) == 24
        and FULL_WRONG_VALUES == BASE_WRONG_VALUES
        and len(FULL_WRONG_DETAILS) == 40
        and FULL_WRONG_DETAILS == BASE_WRONG_DETAILS
        and inherited_wrong_targets <= base_variable_sites
        and c135.BIT not in inherited_wrong_targets
        and not (inherited_wrong_targets & NEW_OUTPUT_SITES),
        f"summaries={len(FULL_WRONG_VALUES)} details={len(FULL_WRONG_DETAILS)}",
    )
    check(
        "C07 independent traversal gives exact three-parent joint layer",
        not c135.POSITIVE.bad
        and not c135.POSITIVE.unexpected_condition_targets
        and JOINT_BASE_STATES == BASE_STATES == 6_936_208
        and JOINT_BASE_EDGES == BASE_EDGES == 53_907_076
        and JOINT_BASE_TERMINALS == BASE_TERMINALS == 1
        and JOINT_STATES == 65_792
        and JOINT_EDGES == 389_824
        and JOINT_TERMINALS == 1
        and not JOINT_BAD,
        f"joint={JOINT_STATES}/{JOINT_EDGES}",
    )
    check(
        "C08 exact factorized graph has 444,969,984 states",
        FACTORIZED_STATES == 444_969_984,
        str(FACTORIZED_STATES),
    )
    check(
        "C09 exact factorized graph has 4,791,200,000 edges",
        FACTORIZED_EDGES == 4_791_200_000,
        str(FACTORIZED_EDGES),
    )
    missing_guard_failures = []
    for guard in GUARD_TARGETS:
        records = {
            **BASE_TERMINAL_RECORDS,
            **{
                site: output
                for site, output in GUARD_OUTPUTS.items()
                if site != guard
            },
        }
        if FULL_RAW.get(c53.local_signature(records, guard)) != frozenset((GUARD_OUTPUT,)):
            missing_guard_failures.append(guard)
    pre_h0_enabled = enabled_nonignored(PRE_H0_TERMINAL_RECORDS)
    final_enabled = enabled_nonignored(FINAL_TERMINAL_RECORDS)
    check(
        "C10 every incomplete product terminal has a guard or H0 enabled",
        not missing_guard_failures
        and pre_h0_enabled == {H0_SITE: frozenset((H0_OUTPUT,))},
        f"guards={missing_guard_failures} pre_h0={pre_h0_enabled}",
    )
    check(
        "C11 product has one all-142-output terminal and no final action",
        BASE_TERMINALS == 1
        and FACTORIZED_TERMINALS == 1
        and FACTOR.terminals == 1
        and len(GROWN_OUTPUTS) == 142
        and not final_enabled,
        str(final_enabled),
    )

    section("D - Output fork and bounded scope")
    check(
        "D01 swapped guarded H1 is unexpected-target-clean and factor-clean only",
        not WRONG_H1_COMPILED.unexpected_targets
        and WRONG_H1_FACTOR.states == 144
        and WRONG_H1_FACTOR.edges == 496
        and WRONG_H1_FACTOR.terminals == 1
        and not WRONG_H1_FACTOR.bad,
    )
    check(
        "D02 replacement H1 adds one BIT expected-target wrong-value alias",
        len(WRONG_H1_WRONG_VALUES) == 25
        and len(WRONG_H1_WRONG_DETAILS) == 41
        and WRONG_H1_NEW_WRONG_VALUES
        == (
            (c135.BIT, (("H0",),)),
        ),
        str(WRONG_H1_NEW_WRONG_VALUES),
    )
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("D03 note names factorized rather than enumerated full graph", "factorized full graph" in note and "not directly enumerated" in note)
    check("D04 note preserves unresolved H0/H1 output fork", "output fork remains open" in note and "expected-target wrong-value" in note)
    check("D05 note denies byte/writer claims", "not an eight-bit word" in note and "not an r_b01 writer" in note)
    check("D06 note carries N1-N8", all(f"n{i}" in note for i in range(1, 9)))
    check("D07 note makes no axiom addition", "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    contract()
    print(
        f"\nFACTOR={FACTOR.states}/{FACTOR.edges} "
        f"FULL_FACTORIZED={FACTORIZED_STATES}/{FACTORIZED_EDGES} "
        f"OUTPUTS={len(GROWN_OUTPUTS)}"
    )
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT=C135_SIX_GUARD_H0_FACTORIZED_FULL_GRAPH"
        if FAIL == 0 else "RESULT=FAIL"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
