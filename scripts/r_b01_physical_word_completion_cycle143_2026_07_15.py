#!/usr/bin/env python3
"""Cycle 143: literal physical R_B01=10010001 word and completion.

The proven Cycle-121 self-caging writer changes only D7 from H0 to H1 and
changes the completion label from R_B00 to R_B01.  Every append schedule is
exhausted; completion is checked against all eight data records; retained
source corruptions, completion-parent mutations, long rail coexistence, and
proper-cubic covariance are tested.

Authority: local campaign evidence only.  No foundation, primitive,
registry, policy, audit, commit, push, or PR is changed.
"""

from __future__ import annotations

from collections import deque
from pathlib import Path

import r_b01_word_retargeted_cycle121_writer_probe_2026_07_15 as w


c121 = w.c121
c119 = w.c119
c112 = w.c112
c105 = c121.c105
c101 = c121.c101
c100 = c121.c100
c53 = w.c53
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "R_B01_PHYSICAL_WORD_COMPLETION_CYCLE143_NOTE_2026-07-15.md"
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


POSITIVE = c112.append_graph(
    c112.SOURCE,
    w.GROWN_OUTPUTS,
    raw=w.FULL_RAW,
    ignored=c112.RAIL_ZERO,
)
ALL_MASK = (1 << len(w.GROWN_OUTPUTS)) - 1


def terminal_records():
    return c112.records_at(ALL_MASK, c112.SOURCE, w.GROWN_OUTPUTS)


def enabled(records, raw=w.FULL_RAW):
    return {
        target: raw[local]
        for target in c53.open_candidates(records)
        if (local := c53.local_signature(records, target)) in raw
    }


def completion_barrier_violations():
    compiled = c112.compile_conditions(
        c112.SOURCE, w.GROWN_OUTPUTS, w.FULL_RAW, c112.RAIL_ZERO
    )
    actions = tuple(
        (compiled.index.get(target), target, conditions)
        for target, conditions in compiled.conditions.items()
    )
    required = sum(1 << compiled.index[site] for site in c121.DATA_SITES)
    completion = 1 << compiled.index[c121.COMPLETION]
    queue = deque((0,))
    seen = {0}
    violations = []
    while queue:
        state = queue.popleft()
        if state & completion and state & required != required:
            violations.append(state)
        legal = []
        for index, target, conditions in actions:
            if index is not None and state >> index & 1:
                continue
            for present, neighbourhood, values in conditions:
                if state & neighbourhood != present:
                    continue
                if target in c112.RAIL_ZERO and values == c112.RAIL_ZERO[target]:
                    break
                if index is not None and values == frozenset((w.GROWN_OUTPUTS[target],)):
                    legal.append(index)
                    break
                raise RuntimeError((state, target, values))
        for index in legal:
            future = state | 1 << index
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return tuple(violations), len(seen)


def completion_parent_controls():
    records = terminal_records()
    records.pop(c121.COMPLETION)
    parents = tuple(
        c53.add(c121.COMPLETION, direction)
        for direction, _value in c53.local_signature(records, c121.COMPLETION)
    )
    attempts = 0
    survivors = []
    alternate_fronts = []
    for parent in parents:
        correct = records[parent]
        for alternate in (None, *sorted(c105.c89.FULL_ROLES - {correct})):
            trial = dict(records)
            if alternate is None:
                del trial[parent]
            else:
                trial[parent] = alternate
            attempts += 1
            observed = enabled(trial).get(c121.COMPLETION, frozenset())
            if w.COMPLETION_OUTPUT in observed:
                survivors.append((parent, alternate, observed))
            elif observed:
                alternate_fronts.append((parent, alternate, observed))
    return attempts, tuple(survivors), tuple(alternate_fronts)


def source_corruption_controls():
    new_sites = set(w.OUTPUTS)
    censuses = []
    failures = []
    for index, site in enumerate(c100.CODE_SITES):
        source = dict(c112.SOURCE)
        source[site] = c121.H0 if source[site] == c121.H1 else c121.H1
        outputs = dict(w.GROWN_OUTPUTS)
        if index == 5:
            outputs[c101.BIT5_REJECT] = c121.H1
        stats = c112.append_graph(source, outputs, raw=w.FULL_RAW)
        reached = new_sites & stats.reached
        censuses.append((stats.states, stats.edges, stats.terminal_sizes))
        if stats.terminals != 1 or stats.bad or reached:
            failures.append(("bit", index, reached, stats.bad[:1]))
    for label, site in (("valid", c100.VALID), ("ready", c100.READY)):
        source = dict(c112.SOURCE)
        source[site] = c121.H0
        stats = c112.append_graph(source, w.GROWN_OUTPUTS, raw=w.FULL_RAW)
        reached = new_sites & stats.reached
        censuses.append((stats.states, stats.edges, stats.terminal_sizes))
        if stats.terminals != 1 or stats.bad or reached:
            failures.append((label, reached, stats.bad[:1]))
    return tuple(censuses), tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("PHYSICAL WORD")
    check("review note exists", NOTE.is_file())
    check(
        "eight data records are literal R_B01=10010001",
        w.WORD == (1, 0, 0, 1, 0, 0, 0, 1)
        and c105.c89.ROLE_TO_WORD["R_B01"] == w.WORD
        and c105.c89.WORD_TO_ROLE[w.WORD] == "R_B01",
        w.WORD,
    )
    check(
        "writer remains twelve canonical / 288 raw rows",
        len(w.WRITER_TABLE) == 12 and len(w.WRITER_RAW) == 288,
        (len(w.WRITER_TABLE), len(w.WRITER_RAW)),
    )
    check(
        "completion is one canonical / 24 raw rows",
        len(w.COMPLETION_RAW) == 24
        and not (set(w.WRITER_RAW) & set(w.COMPLETION_RAW)),
        len(w.COMPLETION_RAW),
    )
    check(
        "8,696-row union is single-valued and alphabet-closed",
        len(w.FULL_RAW) == 8_696
        and all(len(values) == 1 for values in w.FULL_RAW.values())
        and {
            value
            for local, values in w.FULL_RAW.items()
            for value in [*(item for _direction, item in local), *values]
        } <= c105.c89.FULL_ROLES,
    )
    check(
        "D7 and completion are the only semantic retargets from Cycle 121",
        {
            site
            for site in w.OUTPUTS
            if w.OUTPUTS[site] != {
                **dict(c121.DATA_RECORDS),
                **dict(c121.CAGE_RECORDS),
                c121.INHERITED: c121.INHERITED_OUTPUT,
                c121.COMPLETION: c121.COMPLETION_OUTPUT,
            }[site]
        } == {c121.DATA_SITES[7], c121.COMPLETION},
    )

    print("\nEXACT HISTORY")
    check(
        "all schedules reach one complete 99-write terminal",
        POSITIVE.states == 247_144
        and POSITIVE.edges == 1_586_166
        and POSITIVE.terminals == 1
        and POSITIVE.terminal_states == (ALL_MASK,)
        and POSITIVE.terminal_sizes == (99,)
        and POSITIVE.max_frontier == 12
        and not POSITIVE.bad
        and not POSITIVE.unexpected_condition_targets
        and len(POSITIVE.reached) == 99,
        (POSITIVE.states, POSITIVE.edges, POSITIVE.max_frontier),
    )
    violations, barrier_states = completion_barrier_violations()
    check(
        "R_B01 completion never precedes any physical bit",
        barrier_states == POSITIVE.states and not violations,
        (barrier_states, violations[:2]),
    )
    terminal = terminal_records()
    check(
        "terminal decodes the word and carries R_B01 completion",
        tuple(1 if terminal[site] == c121.H1 else 0 for site in c121.DATA_SITES)
        == w.WORD
        and terminal[c121.COMPLETION] == "R_B01"
        and enabled(terminal) == c112.RAIL_ZERO,
    )

    print("\nCORRUPTION AND COVARIANCE")
    attempts, survivors, alternate_fronts = completion_parent_controls()
    check(
        "all 459 completion-parent mutations suppress R_B01 completion",
        attempts == 459 and not survivors,
        (attempts, survivors[:2]),
    )
    check(
        "alternate valid roles are typed alternate fronts, not false R_B01",
        all("R_B01" not in values for _parent, _role, values in alternate_fronts),
        len(alternate_fronts),
    )
    censuses, corruption_failures = source_corruption_controls()
    check(
        "eight source-bit flips plus wrong VALID/READY reach no new writer record",
        len(censuses) == 10 and not corruption_failures,
        corruption_failures[:2],
    )
    covariance_failures = []
    controls = 0
    for local, values in w.FULL_RAW.items():
        for rotation in c53.ROTATIONS:
            controls += 1
            if w.FULL_RAW.get(c53.rotate_signature(local, rotation)) != values:
                covariance_failures.append((local, rotation))
                break
    check(
        "all 208,704 proper-cubic raw images preserve output",
        controls == 208_704 and not covariance_failures,
        covariance_failures[:2],
    )
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("note carries N1-N8 discipline", all(f"n{i}" in note for i in range(1, 9)))
    check("note makes no axiom addition", "no axiom addition follows" in note)

    print("\nACCOUNTING")
    print("WORD", "".join(map(str, w.WORD)))
    print("WRITER_CANONICAL", len(w.WRITER_TABLE))
    print("WRITER_RAW", len(w.WRITER_RAW))
    print("COMPLETION_RAW", len(w.COMPLETION_RAW))
    print("STATES", POSITIVE.states)
    print("EDGES", POSITIVE.edges)
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "R_B01_PHYSICAL_WORD_AND_COMPLETION" if FAIL == 0 else "FAIL")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
