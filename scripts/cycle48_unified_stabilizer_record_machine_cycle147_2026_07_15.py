#!/usr/bin/env python3
"""Cycle 147: unified finite stabilizer record machine.

Authority: local campaign evidence only.  Conditional state updates are
compiled; measurement occurrence and weights are not derived.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path

import cycle48_unified_clifford_luders_machine_probe_2026_07_15 as u


m = u.measure
t = u.t
d = u.d
bind = m.bind
c53 = u.c53
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "CYCLE48_UNIFIED_STABILIZER_RECORD_MACHINE_CYCLE147_NOTE_2026-07-15.md"
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


def prep_word(value: int) -> d.Word:
    return tuple((value >> shift) & 1 for shift in range(5, -1, -1))  # type: ignore[return-value]


def measurement_port_source(word: d.Word, measurement_id: int, outcome_bit: int):
    records = d.local_source(word)
    assert records.pop(bind.PORT) == d.CAGE_ROLE
    records[bind.FRAME] = d.CAGE_ROLE
    records[bind.GATE_SITES[0]] = m.MEASUREMENT_ROLE[measurement_id]
    records[bind.GATE_SITES[1]] = d.bit_role(outcome_bit)
    records[bind.GATE_SITES[2]] = d.CAGE_ROLE
    records[bind.NEXT_FRAME] = d.CAGE_ROLE
    core = set(records) | set(d.CHAIN) | {bind.PORT, bind.NEXT_PORT}
    interface = {
        bind.CURRENT, bind.PORT, bind.NEXT_PORT, bind.FRAME,
        bind.NEXT_FRAME, *bind.GATE_SITES,
    }
    shell = {
        c53.add(site, direction)
        for site in interface
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in core
    }
    records.update({site: d.CAGE_ROLE for site in shell})
    return records


def transform(records, rotation):
    return c53.transform_records(records, rotation, d.SHIFT)


def enabled(records):
    return {
        target: u.MERGED_RAW[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in u.MERGED_RAW
    }


def prep_measurement_run(prep_id: int, measurement_id: int, outcome_bit: int, rotation):
    word = prep_word(prep_id)
    source = transform(measurement_port_source(word, measurement_id, outcome_bit), rotation)
    local_expected = d.local_outputs(word)
    if prep_id < 60:
        local_expected[bind.PORT] = m.update_output(prep_id, measurement_id, outcome_bit)
    expected = transform(local_expected, rotation)
    records = dict(source)
    order = (*d.CHAIN, *((bind.PORT,) if prep_id < 60 else ()))
    for step, local_target in enumerate(order):
        target = next(iter(transform({local_target: "x"}, rotation)))
        actual = enabled(records)
        wanted = {target: frozenset((expected[target],))}
        if actual != wanted:
            return False, ("front", step, actual, wanted, len(source))
        records[target] = expected[target]
    actual = enabled(records)
    if actual:
        return False, ("terminal", actual, len(source))
    return True, (len(order) + 1, len(order), len(source))


def parent_deletions():
    attempts = 0
    failures = []
    for state_id in range(60):
        for measurement_id in range(15):
            for outcome_bit in (0, 1):
                local = m.update_local(state_id, measurement_id, outcome_bit)
                intended = m.update_output(state_id, measurement_id, outcome_bit)
                for index in range(len(local)):
                    attempts += 1
                    mutated = local[:index] + local[index + 1:]
                    observed = u.MERGED_RAW.get(mutated, frozenset())
                    if intended in observed:
                        failures.append((state_id, measurement_id, outcome_bit, index, observed))
    return attempts, tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND CONDITIONAL ALGEBRA")
    check("review note exists", NOTE.is_file())
    counts = Counter(probability for probability, _target in m.BRANCH.values())
    check(
        "Cycle-48 branch table has exact 0/half/1 census",
        len(m.BRANCH) == 1_800
        and counts == {Fraction(0): 180, Fraction(1, 2): 1_440, Fraction(1): 180},
        counts,
    )
    check(
        "every nonzero branch has an exact sixty-state target",
        all(probability == 0 or target in range(60) for probability, target in m.BRANCH.values()),
    )
    check(
        "fifteen physical measurement roles are injective and outside state IDs",
        len(m.MEASUREMENT_ROLE) == len(m.ROLE_MEASUREMENT) == 15
        and not (set(m.MEASUREMENT_ROLE.values()) & set(t.ROLE_STATE)),
    )

    print("\nCONDITIONAL UPDATE GRAMMAR")
    check(
        "1,800 five-parent rows compile all Pauli outcome updates",
        len(m.CANONICAL_TABLE) == 1_800
        and Counter(map(len, m.CANONICAL_TABLE)) == {5: 1_800},
        Counter(map(len, m.CANONICAL_TABLE)),
    )
    check(
        "43,200 covariant update rows are single-valued",
        len(m.UPDATE_RAW) == 43_200
        and all(len(values) == 1 for values in m.UPDATE_RAW.values()),
    )
    check(
        "bound+decoder+Clifford+measurement union is conflict-free",
        len(u.MERGED_RAW) == 67_580
        and not m.RAW_CONFLICTS
        and all(len(values) == 1 for values in u.MERGED_RAW.values()),
        len(u.MERGED_RAW),
    )
    check(
        "zero-weight transcripts write reject; nonzero transcripts write exact target state",
        all(
            m.update_output(state_id, measurement_id, outcome_bit)
            == (t.REJECT_ROLE if target is None else t.STATE_ROLE[target])
            for (state_id, measurement_id, outcome_bit), (_probability, target) in m.BRANCH.items()
        ),
    )

    print("\nUNIFIED TWO-EVENT TAPE")
    failures = []
    states = edges = 0
    sizes = set()
    for state_id in range(60):
        for pair in product(u.EVENTS, repeat=2):
            ok, detail = u.run(state_id, pair)
            if not ok:
                failures.append((state_id, pair, detail))
            else:
                local_states, local_edges, source_size = detail
                states += local_states
                edges += local_edges
                sizes.add(source_size)
    check(
        "all 86,640 Clifford/measurement event pairs are exact",
        not failures and states == 250_800 and edges == 164_160 and sizes == {42},
        (states, edges, sizes, failures[:1]),
    )
    check(
        "one 38-event alphabet mixes eight Clifford and thirty outcome records",
        len(u.EVENTS) == 38
        and len(u.CLIFFORD_EVENTS) == 8
        and len(u.MEASUREMENT_EVENTS) == 30,
    )
    check(
        "reject outputs terminate while every nonzero output is reusable",
        all(
            len(u.apparatus(state_id, pair)[1])
            == (1 if u.event_output(state_id, pair[0])[1] is None else 2)
            for state_id in range(60)
            for pair in product(u.EVENTS, repeat=2)
        ),
    )

    print("\nPREPARATION-TO-MEASUREMENT BIND")
    check(
        "Cycle-144 terminal keeps exactly its two priced fronts",
        enabled(d.BOUND_TERMINAL) == d.BOUND_IGNORED,
        enabled(d.BOUND_TERMINAL),
    )
    failures = []
    states = edges = 0
    sizes = set()
    for rotation_index, rotation in enumerate(c53.ROTATIONS):
        for prep_id in range(64):
            for measurement_id in range(15):
                for outcome_bit in (0, 1):
                    ok, detail = prep_measurement_run(
                        prep_id, measurement_id, outcome_bit, rotation
                    )
                    if not ok:
                        failures.append((rotation_index, prep_id, measurement_id, outcome_bit, detail))
                    else:
                        local_states, local_edges, source_size = detail
                        states += local_states
                        edges += local_edges
                        sizes.add(source_size)
    check(
        "all 46,080 rotated preparation/measurement histories are exact",
        not failures and sizes == {69},
        (states, edges, sizes, failures[:1]),
    )
    valid_instances = 24 * 60 * 30
    invalid_instances = 24 * 4 * 30
    check(
        "integrated graph census is six writes for rejects and seven for valid preparations",
        states == valid_instances * 8 + invalid_instances * 7
        and edges == valid_instances * 7 + invalid_instances * 6,
        (states, edges),
    )
    attempts, deletion_failures = parent_deletions()
    check(
        "deleting any conditional-update parent suppresses that update",
        attempts == 9_000 and not deletion_failures,
        (attempts, deletion_failures[:1]),
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "unified conditional stabilizer record machine",
        "outcome occurrence is not derived",
        "weights remain an explicit conditional import",
        "compiled truth table is not a selected natural law",
        "no axiom addition follows",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "UNIFIED_CONDITIONAL_STABILIZER_RECORD_MACHINE" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
