#!/usr/bin/env python3
"""Cycle 188: proper-cubic transparent contact kernel for recurrent tubes.

Cycle 187 exposed a reachable two-terminal critical pair when two otherwise
lawful Cycle-80 recurrent tubes touch at nearest-neighbour distance one.  This
probe derives the minimum existing-role row delta that preserves every
isolated internal transition on the exact two-tube product domain across all
28 bounded transverse contact placements.

The result is a transparent straight-through contact kernel, not a general
scattering ontology.  It adds no role, priority, clock, sampler, instrument,
foundation, axiom, primitive, registry, policy, audit, commit, push, or PR.
"""

from __future__ import annotations

import hashlib
from collections import Counter
from dataclasses import dataclass
from itertools import product
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import joint_endpoint_bdh_rebind_cycle63_2026_07_14 as c63
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import reachable_recurrent_contact_critical_pair_cycle187_2026_07_16 as c187
import separated_recurrent_tube_collision_control_cycle84_2026_07_14 as c84
import three_phase_recurrent_append_tube_cycle80_2026_07_14 as c80


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "PROPER_CUBIC_RECURRENT_CONTACT_KERNEL_CYCLE188_NOTE_2026-07-16.md"
)
CYCLE80_SCRIPT = ROOT / "scripts/three_phase_recurrent_append_tube_cycle80_2026_07_14.py"
CYCLE84_SCRIPT = ROOT / "scripts/separated_recurrent_tube_collision_control_cycle84_2026_07_14.py"
CYCLE187_SCRIPT = ROOT / "scripts/reachable_recurrent_contact_critical_pair_cycle187_2026_07_16.py"
CYCLE187_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "REACHABLE_RECURRENT_CONTACT_CRITICAL_PAIR_CYCLE187_NOTE_2026-07-16.md"
)

FROZEN_CYCLE80_SCRIPT_SHA = (
    "3cc9de0975458f91aefd648ba91f77b6841339baab2e14619d7cfc44c2a80d2d"
)
FROZEN_CYCLE84_SCRIPT_SHA = (
    "6f0407f34a7ccfa43499c19abf14d119d5c9d3f9d4c857cdbe5b1da354653a67"
)
FROZEN_CYCLE187_SCRIPT_SHA = (
    "13482ac218a06d2b9e7fdac5e38bdc77685cc0095daee7392a60fef39cee6d20"
)
FROZEN_CYCLE187_NOTE_SHA = (
    "72b766e50f09b6260819fabeb6c704950fb629439f27f1498d7b258bf4623c7b"
)

Coord = tuple[int, int, int]
Signature = c53.Signature
Move = tuple[Coord, str]
PLACEMENT: Coord = (41, -29, 17)
HORIZONS = (3, 6, 9)

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


def key(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.canonical_signature(c53.local_signature(records, target))


def table_output(
    table: dict[Signature, str],
    records: dict[Coord, str],
    target: Coord,
) -> str | None:
    return table.get(key(records, target))


def enabled_writes(
    table: dict[Signature, str],
    records: dict[Coord, str],
) -> tuple[Move, ...]:
    result = []
    for target in c53.open_candidates(records):
        output = table_output(table, records, target)
        if output is not None:
            result.append((target, output))
    return tuple(sorted(result))


SINGLE_SOURCE, SINGLE_ALLOWED = c84.one_tube(3)
SINGLE_GRAPH = c63.exact_graph(
    SINGLE_SOURCE,
    c80.CONSTRUCTION.table,
    SINGLE_ALLOWED,
)
SINGLE_INDEX = {
    site: index
    for index, site in enumerate(SINGLE_GRAPH.sites)
}


def single_records(mask: int) -> dict[Coord, str]:
    records = dict(SINGLE_SOURCE)
    records.update({
        site: SINGLE_ALLOWED[site]
        for bit, site in enumerate(SINGLE_GRAPH.sites)
        if mask >> bit & 1
    })
    return records


SINGLE_RECORDS = {
    mask: single_records(mask)
    for mask in SINGLE_GRAPH.states
}


def internal_moves(mask: int) -> tuple[Move, ...]:
    return tuple(
        (target, output)
        for target, output in enabled_writes(
            c80.CONSTRUCTION.table,
            SINGLE_RECORDS[mask],
        )
        if (
            target in SINGLE_ALLOWED
            and SINGLE_ALLOWED[target] == output
            and not mask >> SINGLE_INDEX[target] & 1
        )
    )


SINGLE_MOVES = {
    mask: internal_moves(mask)
    for mask in SINGLE_GRAPH.states
}


@dataclass(frozen=True)
class CriticalPair:
    offset: Coord
    left_mask: int
    right_mask: int
    left: Move
    right: Move


@dataclass(frozen=True)
class ContactCensus:
    kernel: dict[Signature, str]
    critical_pairs: tuple[CriticalPair, ...]
    required_uses: int
    conflicts: tuple[object, ...]


def contact_records(
    offset: Coord,
    left_mask: int,
    right_mask: int,
) -> dict[Coord, str]:
    return {
        **SINGLE_RECORDS[left_mask],
        **c84.translate(SINGLE_RECORDS[right_mask], offset),
    }


def derive_contact_census() -> ContactCensus:
    kernel: dict[Signature, str] = {}
    critical_pairs = []
    conflicts = []
    required_uses = 0
    for offset in c187.CONTACT_OFFSETS:
        for left_mask, right_mask in product(
            SINGLE_GRAPH.states,
            repeat=2,
        ):
            records = contact_records(offset, left_mask, right_mask)
            left_moves = SINGLE_MOVES[left_mask]
            right_moves = SINGLE_MOVES[right_mask]
            for side, moves in ((0, left_moves), (1, right_moves)):
                for target, output in moves:
                    contact_target = (
                        target
                        if side == 0
                        else c84.add(target, offset)
                    )
                    signature = key(records, contact_target)
                    prior = c80.CONSTRUCTION.table.get(
                        signature,
                        kernel.get(signature),
                    )
                    if prior is not None and prior != output:
                        conflicts.append(
                            (
                                offset,
                                left_mask,
                                right_mask,
                                side,
                                contact_target,
                                prior,
                                output,
                                signature,
                            )
                        )
                    if signature not in c80.CONSTRUCTION.table:
                        required_uses += 1
                        kernel[signature] = output
            if len(left_moves) == len(right_moves) == 1:
                left = left_moves[0]
                right = (
                    c84.add(right_moves[0][0], offset),
                    right_moves[0][1],
                )
                if c84.manhattan(left[0], right[0]) == 1:
                    critical_pairs.append(
                        CriticalPair(
                            offset,
                            left_mask,
                            right_mask,
                            left,
                            right,
                        )
                    )
    return ContactCensus(
        kernel,
        tuple(critical_pairs),
        required_uses,
        tuple(conflicts),
    )


CONTACT_CENSUS = derive_contact_census()
CONTACT_KERNEL = CONTACT_CENSUS.kernel
CONTACT_TABLE = {
    **c80.CONSTRUCTION.table,
    **CONTACT_KERNEL,
}
BASE_RAW = c59.raw_rule_outputs(c80.CONSTRUCTION.table)
KERNEL_RAW = c59.raw_rule_outputs(CONTACT_KERNEL)
CONTACT_RAW = c59.raw_rule_outputs(CONTACT_TABLE)


def contact_boundary(
    horizon: int,
    offset: Coord,
) -> tuple[dict[Coord, str], dict[Coord, str]]:
    source, allowed = c84.one_tube(horizon)
    return (
        {**source, **c84.translate(source, offset)},
        {**allowed, **c84.translate(allowed, offset)},
    )


def critical_pair_controls():
    failures = []
    late_counts: Counter[Signature] = Counter()
    late_examples: dict[
        Signature,
        tuple[dict[Coord, str], Coord, str],
    ] = {}
    placement_counts: Counter[Coord] = Counter()
    for pair in CONTACT_CENSUS.critical_pairs:
        records = contact_records(
            pair.offset,
            pair.left_mask,
            pair.right_mask,
        )
        left_target, left_output = pair.left
        right_target, right_output = pair.right
        placement_counts[pair.offset] += 1
        if (
            table_output(
                CONTACT_TABLE,
                records,
                left_target,
            )
            != left_output
            or table_output(
                CONTACT_TABLE,
                records,
                right_target,
            )
            != right_output
        ):
            failures.append(("prestate", pair))
            continue

        left_first = dict(records)
        left_first[left_target] = left_output
        right_late = key(left_first, right_target)
        late_counts[right_late] += 1
        late_examples.setdefault(
            right_late,
            (left_first, right_target, right_output),
        )

        right_first = dict(records)
        right_first[right_target] = right_output
        left_late = key(right_first, left_target)
        late_counts[left_late] += 1
        late_examples.setdefault(
            left_late,
            (right_first, left_target, left_output),
        )

        if (
            table_output(
                CONTACT_TABLE,
                left_first,
                right_target,
            )
            != right_output
            or table_output(
                CONTACT_TABLE,
                right_first,
                left_target,
            )
            != left_output
        ):
            failures.append(("late-arm", pair))
            continue

        left_then_right = dict(left_first)
        left_then_right[right_target] = right_output
        right_then_left = dict(right_first)
        right_then_left[left_target] = left_output
        if left_then_right != right_then_left:
            failures.append(("join", pair))

    deletion_failures = []
    for signature, example in late_examples.items():
        records, target, output = example
        reduced = dict(CONTACT_TABLE)
        removed = reduced.pop(signature, None)
        if (
            removed != output
            or table_output(reduced, records, target) is not None
        ):
            deletion_failures.append(
                (signature, removed, output)
            )
    return (
        tuple(failures),
        late_counts,
        late_examples,
        placement_counts,
        tuple(deletion_failures),
    )


def witness_controls():
    source, expected, graph = c187.WITNESS_INSTANCES[3]
    terminals = tuple(sorted(graph.terminals))
    shared = terminals[0] & terminals[1]
    records = c187.records_at_mask(source, expected, graph, shared)
    writes = enabled_writes(c80.CONSTRUCTION.table, records)
    local_rows = {}
    for first, second in ((writes[0], writes[1]), (writes[1], writes[0])):
        trial = dict(records)
        trial[first[0]] = first[1]
        local_rows[key(trial, second[0])] = second[1]
    local_table = {
        **c80.CONSTRUCTION.table,
        **local_rows,
    }
    local_graph = c63.exact_graph(
        source,
        local_table,
        expected,
    )
    repaired_graph = c63.exact_graph(
        source,
        CONTACT_TABLE,
        expected,
    )

    batch = dict(records)
    for target, output in writes:
        batch[target] = output
    batch_mask = terminals[0] | terminals[1]
    return {
        "source": source,
        "expected": expected,
        "base_graph": graph,
        "shared": shared,
        "records": records,
        "writes": writes,
        "local_rows": local_rows,
        "local_graph": local_graph,
        "repaired_graph": repaired_graph,
        "batch": batch,
        "batch_mask": batch_mask,
        "batch_enabled": enabled_writes(
            c80.CONSTRUCTION.table,
            batch,
        ),
    }


def all_contact_graph_controls():
    shape_histogram = Counter()
    failures = []
    factor_failures = []
    cartesian = frozenset(
        product(SINGLE_GRAPH.states, repeat=2)
    )
    for offset in c187.CONTACT_OFFSETS:
        source, expected = contact_boundary(3, offset)
        graph = c63.exact_graph(
            source,
            CONTACT_TABLE,
            expected,
        )
        complete = (1 << len(graph.sites)) - 1
        observed = (
            graph.conditions,
            len(graph.states),
            graph.edges,
            len(graph.terminals),
            complete in graph.states,
            len(graph.parasites),
            len(graph.conflicts),
        )
        shape_histogram[observed] += 1
        if (
            len(graph.states) != 2_704
            or graph.edges != 5_408
            or graph.terminals
            or complete not in graph.states
            or graph.parasites
            != c84.expected_parasites(3, offset)
            or graph.conflicts
        ):
            failures.append(
                (offset, observed, graph.parasites)
            )

        right_source = c84.translate(SINGLE_SOURCE, offset)
        right_allowed = c84.translate(SINGLE_ALLOWED, offset)
        right_graph = c63.exact_graph(
            right_source,
            c80.CONSTRUCTION.table,
            right_allowed,
        )
        projected = c84.projected_state_pairs(
            graph,
            SINGLE_GRAPH,
            right_graph,
        )
        if projected != cartesian:
            factor_failures.append(
                (
                    offset,
                    len(projected),
                    len(cartesian),
                )
            )
    return (
        shape_histogram,
        tuple(failures),
        tuple(factor_failures),
    )


def horizon_controls():
    observed = {}
    failures = []
    expected_conditions = {3: 162, 6: 374, 9: 586}
    for horizon in HORIZONS:
        source, allowed = c84.one_tube(horizon)
        isolated_base = c63.exact_graph(
            source,
            c80.CONSTRUCTION.table,
            allowed,
        )
        isolated_contact = c63.exact_graph(
            source,
            CONTACT_TABLE,
            allowed,
        )
        joint_source, joint_allowed = contact_boundary(
            horizon,
            c187.WITNESS_OFFSET,
        )
        joint = c63.exact_graph(
            joint_source,
            CONTACT_TABLE,
            joint_allowed,
        )
        complete = (1 << len(joint.sites)) - 1
        item = (
            isolated_base.conditions,
            len(isolated_base.states),
            isolated_base.edges,
            joint.conditions,
            len(joint.states),
            joint.edges,
            len(joint.terminals),
            complete in joint.states,
            len(joint.parasites),
            len(joint.conflicts),
        )
        observed[horizon] = item
        if (
            isolated_contact != isolated_base
            or joint.conditions != expected_conditions[horizon]
            or len(joint.states)
            != len(isolated_base.states) ** 2
            or joint.edges
            != 2 * len(isolated_base.states) ** 2
            or joint.terminals
            or complete not in joint.states
            or len(joint.parasites) != 2
            or joint.conflicts
        ):
            failures.append((horizon, item))
    return observed, tuple(failures)


def separation_controls():
    failures = []
    attempts = 0
    for offset in c84.OFFSETS:
        for horizon in c84.HORIZONS:
            source, allowed = c84.one_tube(horizon)
            joint_source = {
                **source,
                **c84.translate(source, offset),
            }
            joint_allowed = {
                **allowed,
                **c84.translate(allowed, offset),
            }
            base_graph = c63.exact_graph(
                joint_source,
                c80.CONSTRUCTION.table,
                joint_allowed,
            )
            contact_graph = c63.exact_graph(
                joint_source,
                CONTACT_TABLE,
                joint_allowed,
            )
            attempts += 1
            if contact_graph != base_graph:
                failures.append(
                    (
                        offset,
                        horizon,
                        (
                            base_graph.conditions,
                            len(base_graph.states),
                            base_graph.edges,
                        ),
                        (
                            contact_graph.conditions,
                            len(contact_graph.states),
                            contact_graph.edges,
                        ),
                    )
                )
    return attempts, tuple(failures)


def rotation_controls():
    source, expected = contact_boundary(
        3,
        c187.WITNESS_OFFSET,
    )
    wanted_parasites = dict(
        c84.expected_parasites(
            3,
            c187.WITNESS_OFFSET,
        )
    )
    failures = []
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        rotated_source = c84.rotate_translate(
            source,
            rotation,
            PLACEMENT,
        )
        rotated_expected = c84.rotate_translate(
            expected,
            rotation,
            PLACEMENT,
        )
        rotated_parasites = frozenset(
            c84.rotate_translate(
                wanted_parasites,
                rotation,
                PLACEMENT,
            ).items()
        )
        graph = c63.exact_graph(
            rotated_source,
            CONTACT_TABLE,
            rotated_expected,
        )
        complete = (1 << len(graph.sites)) - 1
        observed = (
            graph.conditions,
            len(graph.states),
            graph.edges,
            len(graph.terminals),
            complete in graph.states,
            len(graph.parasites),
            len(graph.conflicts),
        )
        if (
            observed
            != (162, 2_704, 5_408, 0, True, 2, 0)
            or graph.parasites != rotated_parasites
        ):
            failures.append(
                (
                    rotation_index,
                    observed,
                    graph.parasites,
                    rotated_parasites,
                )
            )
    return tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND PREDECESSOR")
    check(
        "Cycle 80, Cycle 84, and Cycle 187 frozen hashes match",
        sha256(CYCLE80_SCRIPT) == FROZEN_CYCLE80_SCRIPT_SHA
        and sha256(CYCLE84_SCRIPT) == FROZEN_CYCLE84_SCRIPT_SHA
        and sha256(CYCLE187_SCRIPT) == FROZEN_CYCLE187_SCRIPT_SHA
        and sha256(CYCLE187_NOTE) == FROZEN_CYCLE187_NOTE_SHA,
        (
            sha256(CYCLE80_SCRIPT),
            sha256(CYCLE84_SCRIPT),
            sha256(CYCLE187_SCRIPT),
            sha256(CYCLE187_NOTE),
        ),
    )
    check(
        "the predecessor census is the exact 28-placement witness domain",
        len(c187.CONTACT_OFFSETS) == 28
        and c187.WITNESS_OFFSET in c187.CONTACT_OFFSETS,
        c187.CONTACT_OFFSETS,
    )

    print("\nMINIMUM TRANSPARENT CONTACT PRICE")
    recurrence_roles = (
        frozenset(c80.CONSTRUCTION.table.values())
        | frozenset(
            role
            for signature in c80.CONSTRUCTION.table
            for _direction, role in signature
        )
    )
    kernel_roles = (
        frozenset(CONTACT_KERNEL.values())
        | frozenset(
            role
            for signature in CONTACT_KERNEL
            for _direction, role in signature
        )
    )
    check(
        "the product-domain census derives 162 existing-role canonical rows",
        len(CONTACT_KERNEL) == 162
        and not CONTACT_CENSUS.conflicts
        and kernel_roles <= recurrence_roles,
        (
            len(CONTACT_KERNEL),
            CONTACT_CENSUS.required_uses,
            len(CONTACT_CENSUS.conflicts),
            len(kernel_roles - recurrence_roles),
        ),
    )
    check(
        "the proper-cubic price is 3,888 new raw rows and a conflict-free 213-row union",
        len(c80.CONSTRUCTION.table) == 51
        and len(BASE_RAW) == 1_170
        and len(KERNEL_RAW) == 3_888
        and not (set(BASE_RAW) & set(KERNEL_RAW))
        and len(CONTACT_TABLE) == 213
        and len(CONTACT_RAW) == 5_058
        and all(len(outputs) == 1 for outputs in CONTACT_RAW.values()),
        (
            len(c80.CONSTRUCTION.table),
            len(CONTACT_KERNEL),
            len(BASE_RAW),
            len(KERNEL_RAW),
            len(CONTACT_RAW),
        ),
    )

    print("\nLOCAL CONTACT CRITICAL PAIRS")
    (
        pair_failures,
        late_counts,
        late_examples,
        placement_counts,
        deletion_failures,
    ) = critical_pair_controls()
    check(
        "all 162 reachable adjacent contact pairs close to the same record map",
        len(CONTACT_CENSUS.critical_pairs) == 162
        and not pair_failures,
        (
            len(CONTACT_CENSUS.critical_pairs),
            Counter(placement_counts.values()),
            pair_failures[:2],
        ),
    )
    check(
        "the kernel is exactly the missing late-arm set",
        set(late_counts) == set(CONTACT_KERNEL)
        and Counter(late_counts.values()) == Counter({2: 162})
        and len(late_examples) == 162,
        (
            len(late_counts),
            Counter(late_counts.values()),
            len(late_examples),
        ),
    )
    check(
        "deleting any one kernel row reopens a displayed critical-pair arm",
        len(late_examples) == len(CONTACT_KERNEL)
        and not deletion_failures,
        deletion_failures[:2],
    )

    print("\nEXACT CYCLE-187 WITNESS")
    witness = witness_controls()
    local_graph = witness["local_graph"]
    repaired_graph = witness["repaired_graph"]
    repaired_complete = (1 << len(repaired_graph.sites)) - 1
    check(
        "two existing-role rows are the minimum local diamond completion",
        len(witness["local_rows"]) == 2
        and set(witness["local_rows"]) <= set(CONTACT_KERNEL)
        and (
            local_graph.conditions,
            len(local_graph.states),
            local_graph.edges,
            len(local_graph.terminals),
            tuple(mask.bit_count() for mask in local_graph.terminals),
            len(local_graph.parasites),
            len(local_graph.conflicts),
        )
        == (146, 953, 1_822, 1, (22,), 2, 0),
        (
            witness["local_rows"],
            local_graph.conditions,
            len(local_graph.states),
            local_graph.edges,
            tuple(mask.bit_count() for mask in local_graph.terminals),
        ),
    )
    check(
        "the full kernel carries that witness to both complete recurrent tubes",
        (
            repaired_graph.conditions,
            len(repaired_graph.states),
            repaired_graph.edges,
            len(repaired_graph.terminals),
            repaired_complete in repaired_graph.states,
            len(repaired_graph.parasites),
            len(repaired_graph.conflicts),
        )
        == (162, 2_704, 5_408, 0, True, 2, 0),
        (
            repaired_graph.conditions,
            len(repaired_graph.states),
            repaired_graph.edges,
            len(repaired_graph.terminals),
            repaired_complete in repaired_graph.states,
            repaired_graph.parasites,
            repaired_graph.conflicts,
        ),
    )
    check(
        "synchronous pre-state batching is a distinct third terminal semantics",
        witness["shared"].bit_count() == 20
        and len(witness["writes"]) == 2
        and witness["batch_mask"].bit_count() == 22
        and witness["batch_mask"]
        not in witness["base_graph"].states
        and not witness["batch_enabled"]
        and witness["batch_mask"] in repaired_graph.states,
        (
            witness["shared"].bit_count(),
            witness["writes"],
            witness["batch_mask"].bit_count(),
            witness["batch_enabled"],
        ),
    )

    print("\nALL 28 CONTACT PLACEMENTS")
    (
        shape_histogram,
        contact_failures,
        factor_failures,
    ) = all_contact_graph_controls()
    check(
        "all 28 placements reach both complete tubes with only intended exits",
        not contact_failures
        and shape_histogram
        == Counter({
            (150, 2_704, 5_408, 0, True, 2, 0): 10,
            (156, 2_704, 5_408, 0, True, 2, 0): 10,
            (162, 2_704, 5_408, 0, True, 2, 0): 8,
        }),
        (shape_histogram, contact_failures[:2]),
    )
    check(
        "every contact graph projects to the exact two-lineage Cartesian product",
        not factor_failures,
        factor_failures[:2],
    )

    print("\nRECURRENCE AND SEPARATION COMPOSITION")
    horizon_counts, horizon_failures = horizon_controls()
    check(
        "the witness remains the exact recurrent product through horizons 3, 6, and 9",
        not horizon_failures,
        horizon_counts,
    )
    separation_attempts, separation_failures = separation_controls()
    check(
        "the kernel leaves all six strict-separation controls byte-for-byte unchanged",
        separation_attempts == 6
        and not separation_failures,
        (separation_attempts, separation_failures[:1]),
    )

    print("\nPROPER-CUBIC COVARIANCE")
    rotation_failures = rotation_controls()
    check(
        "all 24 proper-cubic images preserve complete two-lineage contact",
        not rotation_failures,
        rotation_failures[:1],
    )

    print("\nSCOPE")
    normalized = (
        " ".join(NOTE.read_text(encoding="utf-8").lower().split())
        if NOTE.is_file()
        else ""
    )
    required = (
        "transparent straight-through compatibility class",
        "minimum is scoped",
        "synchronous pre-state batching",
        "no global clock",
        "no coordinate priority",
        "no host-selected branch",
        "no axiom addition follows",
        "no foundation, axiom, primitive, registry, policy, or audit edit",
    )
    missing = tuple(
        phrase
        for phrase in required
        if phrase not in normalized
    )
    check(
        "the note states the compatibility and occurrence-semantics boundaries",
        not missing,
        missing,
    )

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "PROPER_CUBIC_RECURRENT_CONTACT_KERNEL"
        if FAIL == 0
        else "CYCLE188_NEEDS_REPAIR",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
