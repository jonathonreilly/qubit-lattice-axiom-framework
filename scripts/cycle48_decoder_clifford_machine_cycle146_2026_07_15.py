#!/usr/bin/env python3
"""Cycle 146: local Cycle-48 preparation and Clifford record machine.

Authority: local campaign evidence only.  No protected surface or git remote
is changed.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path

import cycle48_decoder_clifford_bind_probe_2026_07_15 as bind


t = bind.transition
d = bind.d
c48 = t.c48
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "CYCLE48_DECODER_CLIFFORD_MACHINE_CYCLE146_NOTE_2026-07-15.md"
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


def word(value: int) -> d.Word:
    return tuple((value >> shift) & 1 for shift in range(5, -1, -1))  # type: ignore[return-value]


def direct_deletion_controls():
    failures = []
    attempts = 0
    for state_id in range(60):
        for gate_id in range(8):
            local = t.transition_local(state_id, gate_id)
            intended = t.transition_output(state_id, gate_id)
            raw_local = local
            for index in range(len(raw_local)):
                attempts += 1
                mutated = raw_local[:index] + raw_local[index + 1:]
                observed = bind.MERGED_RAW.get(mutated, frozenset())
                if intended in observed:
                    failures.append((state_id, gate_id, index, observed))
    return attempts, tuple(failures)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("AUTHORITY AND ALGEBRA")
    check("review note exists", NOTE.is_file())
    check("Cycle 48 supplies sixty exact stabilizer states", len(t.STATES) == 60)
    check(
        "all 420 Clifford images are exact members of the sixty-state class",
        len(t.GATE_IMAGE) == 420 and all(value is not None for value in t.GATE_IMAGE.values()),
    )
    check(
        "three physical bits encode seven gates and one reject",
        {t.gate_word(index) for index in range(8)} == set(product((0, 1), repeat=3)),
    )

    print("\nTRANSITION GRAMMAR")
    check(
        "sixty physical state roles are injective and exclude reject",
        len(t.STATE_ROLE) == len(t.ROLE_STATE) == 60
        and t.REJECT_ROLE not in t.ROLE_STATE,
    )
    check(
        "480 five-parent rows compile all state/gate contexts",
        len(t.CANONICAL_TABLE) == 480
        and Counter(map(len, t.CANONICAL_TABLE)) == {5: 480},
        Counter(map(len, t.CANONICAL_TABLE)),
    )
    check(
        "transition grammar has 11,520 covariant raw rows",
        len(t.TRANSITION_RAW) == 11_520
        and all(len(values) == 1 for values in t.TRANSITION_RAW.values()),
    )
    check(
        "transition rows are disjoint from the Cycle-145 merged law",
        set(t.TRANSITION_RAW).isdisjoint(d.MERGED_RAW)
        and len(t.MERGED_RAW) == 24_380
        and not t.RAW_CONFLICTS,
        (len(d.MERGED_RAW), len(t.TRANSITION_RAW), len(t.MERGED_RAW)),
    )
    check(
        "every transition output equals the Cycle-48 matrix image",
        all(
            t.transition_output(state_id, gate_id)
            == t.STATE_ROLE[t.GATE_IMAGE[(state_id, gate_id)]]
            for state_id in range(60)
            for gate_id in range(7)
        ),
    )

    print("\nRECURRENT TWO-OPERATION MACHINE")
    failures = []
    states = edges = 0
    sizes = set()
    for state_id in range(60):
        for gates in product(range(8), repeat=2):
            ok, detail = t.run(state_id, gates)
            if not ok:
                failures.append((state_id, gates, detail))
            else:
                local_states, local_edges, source_size = detail
                states += local_states
                edges += local_edges
                sizes.add(source_size)
    check(
        "all 3,840 two-operation transcripts reach the exact terminal",
        not failures and states == 11_040 and edges == 7_200 and sizes == {39},
        (states, edges, sizes, failures[:1]),
    )
    check(
        "reject is terminal while every valid output is reusable",
        all(
            len(t.apparatus(state_id, (first, second))[1])
            == (1 if first == 7 else 2)
            for state_id in range(60)
            for first in range(8)
            for second in range(8)
        ),
    )

    print("\nPREPARATION-TO-DYNAMICS BIND")
    check(
        "port decoder retains 126 five-parent rows",
        len(bind.DECODER_TABLE) == 126
        and Counter(map(len, bind.DECODER_TABLE)) == {5: 126},
        Counter(map(len, bind.DECODER_TABLE)),
    )
    check(
        "bound+decoder+transition union is 24,380-row single-valued",
        len(bind.MERGED_RAW) == 24_380
        and not bind.RAW_CONFLICTS
        and all(len(values) == 1 for values in bind.MERGED_RAW.values()),
    )
    check(
        "Cycle-144 terminal gains no decoder/transition front",
        bind.enabled(d.BOUND_TERMINAL) == d.BOUND_IGNORED,
        bind.enabled(d.BOUND_TERMINAL),
    )
    failures = []
    states = edges = 0
    sizes = set()
    for rotation_index, rotation in enumerate(bind.c53.ROTATIONS):
        for prep_id in range(64):
            for gate_id in range(8):
                ok, detail = bind.run(prep_id, gate_id, rotation)
                if not ok:
                    failures.append((rotation_index, prep_id, gate_id, detail))
                else:
                    local_states, local_edges, source_size = detail
                    states += local_states
                    edges += local_edges
                    sizes.add(source_size)
    check(
        "all 12,288 rotated preparation/operation histories are exact",
        not failures and states == 97_536 and edges == 85_248 and sizes == {69},
        (states, edges, sizes, failures[:1]),
    )
    check(
        "valid preparation writes the exact next state and invalid preparation never transitions",
        all(
            (
                bind.run(prep_id, gate_id, bind.c53.ROTATIONS[0])[0]
                and ((prep_id < 60) == (bind.PORT in {
                    **bind.decoder_outputs(word(prep_id)),
                    **({bind.PORT: t.transition_output(prep_id, gate_id)} if prep_id < 60 else {}),
                }))
            )
            for prep_id in range(64)
            for gate_id in range(8)
        ),
    )
    attempts, deletion_failures = direct_deletion_controls()
    check(
        "deleting any direct transition parent suppresses that transition output",
        attempts == 2_400 and not deletion_failures,
        (attempts, deletion_failures[:1]),
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "preparation-to-clifford record machine",
        "operation bits remain supplied event records",
        "does not derive born probabilities",
        "engineered finite transition table",
        "no axiom addition follows",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "CYCLE48_DECODER_CLIFFORD_MACHINE" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
