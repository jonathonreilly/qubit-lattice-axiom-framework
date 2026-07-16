#!/usr/bin/env python3
"""Cycle 144: bind physical R_B01 completion into recurrent roots.

The direct two-parent recurrent R_B01 root row is removed.  A guarded physical
bridge, twelve-record first-root adapter, and period-four completion sidecar
make the first two recurrent roots descend from the literal 10010001 writer.
Every post-prefix asynchronous history is exhausted; the earlier physical
history is screened exactly for extension-row interference.

Authority: local campaign evidence only.  No foundation, primitive, registry,
policy, audit, queue, commit, push, or PR is changed.
"""

from __future__ import annotations

from pathlib import Path

import guarded_physical_word_to_recurrent_root_history_closure_2026_07_15 as b
import physical_r_b01_safe_prefix_history_probe_2026_07_15 as physical
import prebind_unary_role_history_census_2026_07_15 as history


ROOT_DIR = Path(__file__).resolve().parents[1]
NOTE = ROOT_DIR / "docs" / "work_history" / "repo" / "review_feedback" / "PHYSICAL_R_B01_RECURRENT_ROOT_BIND_CYCLE144_NOTE_2026-07-15.md"
c141 = b.c141
c112 = b.c112
c53 = b.c53
cell = b.cell
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


def final_table():
    table = dict(b.INITIAL_TABLE)
    for local, output in b.ADAPTER_HISTORY_VARIANTS:
        b.add_table_row(table, local, output)
    return table


FINAL_TABLE = final_table()
FINAL_RAW = b.raw_from(FINAL_TABLE)
FACTOR_GRAPH = b.base.compiled_exact_graph(
    b.FACTOR_SOURCE,
    b.FACTOR_OUTPUTS,
    FINAL_RAW,
    b.BIND_IGNORED,
    state_limit=5_000_000,
)


def exact_physical_states():
    return history.reachable_states(
        c112.SOURCE,
        physical.OUTPUTS,
        physical.RAW,
        c112.RAIL_ZERO,
    )


def extension_prehistory_screen(physical_states):
    extension = {
        local: values
        for local, values in FINAL_RAW.items()
        if physical.RAW.get(local) != values
    }
    compiled = c112.compile_conditions(
        c112.SOURCE, physical.OUTPUTS, extension, {}
    )
    projections = {}

    def reachable(mask, desired):
        values = projections.get(mask)
        if values is None:
            values = {state & mask for state in physical_states}
            projections[mask] = values
        return desired in values

    expected = {
        **{site: frozenset((value,)) for site, value in b.FACTOR_OUTPUTS.items()},
        **b.BIND_IGNORED,
        **c112.RAIL_ZERO,
    }
    allowed = []
    physical_targets = []
    invalid = []
    for target, conditions in compiled.conditions.items():
        target_bit = (
            1 << compiled.index[target] if target in compiled.index else 0
        )
        for present, neighbourhood, values in conditions:
            mask = neighbourhood | target_bit
            if not reachable(mask, present):
                continue
            item = (target, present, neighbourhood, values)
            if target in physical.OUTPUTS:
                physical_targets.append(item)
            elif expected.get(target) == values:
                allowed.append(item)
            else:
                invalid.append(item)
    return (
        extension,
        tuple(allowed),
        tuple(physical_targets),
        tuple(invalid),
        len(projections),
    )


def first_root_context():
    records = {**b.base.RECORDS, **b.direct.first_pre_root_records()}
    records.pop(b.ROOT, None)
    for target, output in zip(b.PATH[:-1], b.ROLES[:-1]):
        records[target] = output
    return records


def second_root_context():
    records = {**b.base.RECORDS, **b.direct.first_pre_root_records()}
    records.pop(b.ROOT, None)
    for target, output in zip(b.PATH, b.ROLES):
        records[target] = output
    b.direct.advance_to_second_pre_root(records)
    for target, output in (*b.SIDECAR_TRUNK, *b.SIDECAR_SHELL):
        records[target] = output
    records.pop(b.SECOND_ROOT, None)
    return records


def root_parent_mutations(target, records):
    local = c53.local_signature(records, target)
    parents = tuple(c53.add(target, direction) for direction, _value in local)
    attempts = 0
    survivors = []
    alternate_fronts = []
    for parent in parents:
        correct = records[parent]
        for alternate in (None, *sorted(cell.FULL_ROLES - {correct})):
            trial = dict(records)
            if alternate is None:
                del trial[parent]
            else:
                trial[parent] = alternate
            attempts += 1
            mutated = c53.local_signature(trial, target)
            observed = FINAL_RAW.get(mutated, frozenset())
            if "R_B01" in observed:
                survivors.append((parent, alternate, observed))
            elif observed:
                alternate_fronts.append((parent, alternate, observed))
    return local, attempts, tuple(survivors), tuple(alternate_fronts)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CONSTRUCTION")
    check("review note exists", NOTE.is_file())
    check(
        "direct two-parent recurrent root orbit is absent",
        len(b.direct.DIRECT_ROOT_ROW) == 24
        and not (set(FINAL_RAW) & set(b.direct.DIRECT_ROOT_ROW)),
        len(b.direct.DIRECT_ROOT_ROW),
    )
    check(
        "32 canonical additions compile to a 9,836-row single-valued law",
        len(FINAL_TABLE) == 32
        and len(FINAL_RAW) == 9_836
        and all(len(values) == 1 for values in FINAL_RAW.values()),
        (len(FINAL_TABLE), len(FINAL_RAW)),
    )
    collisions = tuple(sorted(
        (site, b.base.FACTOR_OUTPUTS[site], b.ADAPTER_OUTPUTS[site])
        for site in set(b.base.FACTOR_OUTPUTS) & set(b.ADAPTER_OUTPUTS)
        if b.base.FACTOR_OUTPUTS[site] != b.ADAPTER_OUTPUTS[site]
    ))
    check(
        "adapter and recurrent outputs have no wrong-value collision",
        not collisions and len(b.FACTOR_OUTPUTS) == 172,
        collisions,
    )

    print("\nEXACT POST-PREFIX GRAPH")
    check(
        "all 172 writes reach one schedule-independent terminal",
        FACTOR_GRAPH["states"] == 68_736
        and FACTOR_GRAPH["edges"] == 330_024
        and FACTOR_GRAPH["terminals"] == 1
        and FACTOR_GRAPH["max_frontier"] == 9
        and not FACTOR_GRAPH["bad"]
        and not FACTOR_GRAPH["diamond_failures"]
        and len(FACTOR_GRAPH["reached"]) == 172,
        (
            FACTOR_GRAPH["states"], FACTOR_GRAPH["edges"],
            FACTOR_GRAPH["max_frontier"], FACTOR_GRAPH["diamond_pairs"],
        ),
    )
    terminal = {**b.FACTOR_SOURCE, **b.FACTOR_OUTPUTS}
    check(
        "terminal exposes only next rail and next sidecar fronts",
        c141.enabled(terminal, FINAL_RAW) == b.BIND_IGNORED
        and set(b.BIND_IGNORED) == {(-11, 1, 2), (-9, -1, 0)},
        c141.enabled(terminal, FINAL_RAW),
    )

    first_required = (
        (5, 2, -3),
        b.JOINT,
        *b.PATH[:-1],
    )
    first_mandatory = FACTOR_GRAPH["mandatory"][b.ROOT]
    second_required = (
        b.ROOT,
        *(site for site, _output in b.SIDECAR_TRUNK),
        b.SIDECAR_SHELL[0][0],
    )
    second_mandatory = FACTOR_GRAPH["mandatory"][b.SECOND_ROOT]
    check(
        "first root requires physical seed, JOINT, and every adapter record",
        all(
            first_mandatory >> FACTOR_GRAPH["index"][site] & 1
            for site in first_required
        ),
        first_required,
    )
    check(
        "second root requires first root and the carried sidecar",
        all(
            second_mandatory >> FACTOR_GRAPH["index"][site] & 1
            for site in second_required
        ),
        second_required,
    )

    first_records = first_root_context()
    second_records = second_root_context()
    first_local = c53.local_signature(first_records, b.ROOT)
    second_local = c53.local_signature(second_records, b.SECOND_ROOT)
    check(
        "both roots consume the same three-parent guarded local row",
        first_local == second_local
        and len(first_local) == 3
        and FINAL_RAW.get(first_local) == frozenset(("R_B01",)),
        (first_local, second_local),
    )

    print("\nPHYSICAL PREHISTORY FIREWALL")
    p_compiled, p_states, p_edges, p_terminals, p_bad = exact_physical_states()
    data_mask = sum(
        1 << p_compiled.index[site] for site in b.base.prefix.word.c121.DATA_SITES
    )
    completion_bit = 1 << p_compiled.index[b.base.prefix.word.c121.COMPLETION]
    completion_descended_prefix = set(b.base.prefix.PREFIX_OUTPUTS) - {
        b.base.prefix.ALLOCATOR
    }
    prefix_mask = sum(
        1 << p_compiled.index[site] for site in completion_descended_prefix
    )
    completion_violations = tuple(
        state for state in p_states
        if state & completion_bit and state & data_mask != data_mask
    )
    prefix_violations = tuple(
        state for state in p_states
        if state & prefix_mask and not state & completion_bit
    )
    early_prefix_sites = {
        site
        for state in p_states
        if not state & completion_bit
        for site in b.base.prefix.PREFIX_OUTPUTS
        if state >> p_compiled.index[site] & 1
    }
    check(
        "249,192 physical histories preserve byte, port, and launch barriers",
        len(p_states) == 249_192
        and p_edges == 1_596_534
        and len(p_terminals) == 1
        and not p_bad
        and not completion_violations
        and not prefix_violations
        and early_prefix_sites == {b.base.prefix.ALLOCATOR},
        (
            len(p_states), p_edges, completion_violations[:1],
            prefix_violations[:1], early_prefix_sites,
        ),
    )
    extension, allowed, physical_targets, invalid, projections = (
        extension_prehistory_screen(p_states)
    )
    check(
        "extension rows cannot rewrite a physical-prefix target",
        not physical_targets,
        physical_targets[:3],
    )
    check(
        "every reachable prehistory extension front is declared and typed",
        not invalid and bool(allowed),
        (len(extension), len(allowed), projections, invalid[:3]),
    )

    print("\nMUTATION AND COVARIANCE CONTROLS")
    first_local, first_attempts, first_survivors, first_alternates = (
        root_parent_mutations(b.ROOT, first_records)
    )
    second_local, second_attempts, second_survivors, second_alternates = (
        root_parent_mutations(b.SECOND_ROOT, second_records)
    )
    check(
        "all 918 direct root-parent mutations suppress R_B01",
        first_attempts == second_attempts == 459
        and not first_survivors and not second_survivors,
        (first_survivors[:2], second_survivors[:2]),
    )
    check(
        "alternate typed fronts never contain the intended root value",
        all("R_B01" not in values for _p, _a, values in (*first_alternates, *second_alternates)),
        (len(first_alternates), len(second_alternates)),
    )
    covariance_failures = []
    covariance_checks = 0
    for local, values in FINAL_RAW.items():
        for rotation in c53.ROTATIONS:
            covariance_checks += 1
            if FINAL_RAW.get(c53.rotate_signature(local, rotation)) != values:
                covariance_failures.append((local, rotation))
                break
    check(
        "all 236,064 proper-cubic raw images preserve output",
        covariance_checks == 236_064 and not covariance_failures,
        covariance_failures[:2],
    )
    note = NOTE.read_text() if NOTE.is_file() else ""
    check(
        "review note carries N1-N8 discipline and no axiom edit",
        all(f"### N{index}" in note for index in range(1, 9))
        and "No axiom addition follows" in note,
    )

    print("\nACCOUNTING")
    print("PHYSICAL_STATES", len(p_states))
    print("FACTOR_STATES", FACTOR_GRAPH["states"])
    print("FACTOR_EDGES", FACTOR_GRAPH["edges"])
    print("FINAL_RAW", len(FINAL_RAW))
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "PHYSICAL_R_B01_RECURRENT_ROOT_BIND"
        if FAIL == 0 else "CYCLE144_REJECTED",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
