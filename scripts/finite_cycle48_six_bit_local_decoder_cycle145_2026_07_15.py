#!/usr/bin/env python3
"""Cycle 145: compile Cycle 48's finite decoder into strict local records.

The preparation word is supplied only as six literal permanent H0/H1 records.
A covariant six-write prefix chain maps all sixty valid Cycle-48 words to
distinct physical state-ID roles and the four unused words to disjoint reject
roles.  The rows are merged with Cycle 144 and exhaustively screened.

Authority: local campaign evidence only.  No foundation, axiom, primitive,
registry, policy, queue, audit, commit, push, or PR is changed.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path

import cycle48_six_bit_local_decoder_compilation_probe_2026_07_15 as p
import record_derived_coherent_carrier_decoder_cycle48_2026_07_14 as c48


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "FINITE_CYCLE48_SIX_BIT_LOCAL_DECODER_CYCLE145_NOTE_2026-07-15.md"
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


def word(value: int) -> p.Word:
    return tuple((value >> shift) & 1 for shift in range(5, -1, -1))  # type: ignore[return-value]


def nonboundary_enabled(records):
    return {
        target: values
        for target, values in p.enabled(records).items()
        if p.BOUND_IGNORED.get(target) != values
    }


def deletion_controls():
    failures = []
    attempts = 0
    rotation = p.c53.ROTATIONS[0]
    for value in range(64):
        bits = word(value)
        outputs = p.transform(p.local_outputs(bits), rotation)
        for missing in range(6):
            attempts += 1
            source = p.local_source(bits)
            del source[p.DATA[missing]]
            records = {**p.BOUND_TERMINAL, **p.transform(source, rotation)}
            for index in range(missing):
                actual = nonboundary_enabled(records)
                site = next(iter(p.transform({p.CHAIN[index]: "x"}, rotation)))
                expected = {site: frozenset((outputs[site],))}
                if actual != expected:
                    failures.append((value, missing, index, actual, expected))
                    break
                records[site] = outputs[site]
            else:
                if nonboundary_enabled(records):
                    failures.append((value, missing, "did-not-stall", nonboundary_enabled(records)))
                final = next(iter(p.transform({p.CHAIN[-1]: "x"}, rotation)))
                if final in records:
                    failures.append((value, missing, "final-present", records[final]))
    return attempts, tuple(failures)


def direct_parent_mutations():
    attempts = 0
    survivors = []
    alternate_fronts = []
    for prefix in p.PREFIXES:
        index = len(prefix) - 1
        bits: p.Word = tuple(prefix + (0,) * (6 - len(prefix)))  # type: ignore[assignment]
        records = p.local_source(bits)
        records.update({
            p.CHAIN[prior]: p.PREFIX_ROLE[prefix[: prior + 1]]
            for prior in range(index)
        })
        target = p.CHAIN[index]
        intended = p.PREFIX_ROLE[prefix]
        local = p.c53.local_signature(records, target)
        parents = tuple(p.c53.add(target, direction) for direction, _value in local)
        for parent in parents:
            correct = records[parent]
            for alternate in (None, *sorted(p.cell.FULL_ROLES - {correct})):
                attempts += 1
                trial = dict(records)
                if alternate is None:
                    del trial[parent]
                else:
                    trial[parent] = alternate
                observed = p.MERGED_RAW.get(
                    p.c53.local_signature(trial, target), frozenset()
                )
                if intended in observed:
                    survivors.append((prefix, parent, alternate, observed))
                elif observed:
                    alternate_fronts.append((prefix, parent, alternate, observed))
    return attempts, tuple(survivors), tuple(alternate_fronts)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND INPUT CLASS")
    check("review note exists", NOTE.is_file())
    check(
        "Cycle 48 accepts exactly codes 0 through 59",
        all(c48.decode_six(word(value)) == (value if value < 60 else None) for value in range(64)),
    )
    check(
        "runner is outside protected constitutional surfaces",
        "review_feedback" in str(NOTE) and "MINIMAL_AXIOMS" not in str(NOTE),
    )

    print("\nLOCAL COMPILATION")
    arities = Counter(map(len, p.CANONICAL_TABLE))
    check(
        "153-role alphabet partitions into 27 reserved and 126 prefix roles",
        len(p.cell.FULL_ROLES) == 153
        and len(p.RESERVED_ROLES) == 27
        and len(p.PREFIX_ROLES) == len(p.PREFIXES) == 126,
        (len(p.cell.FULL_ROLES), len(p.RESERVED_ROLES), len(p.PREFIX_ROLES)),
    )
    check(
        "all nonempty six-bit prefixes have one injective physical role",
        len(p.PREFIX_ROLE) == len(p.ROLE_PREFIX) == 126
        and all(p.ROLE_PREFIX[p.PREFIX_ROLE[prefix]] == prefix for prefix in p.PREFIXES),
    )
    check(
        "finite apparatus is six literal bits, one start, and 43 quiet cage records",
        len(p.DATA) == 6
        and len(p.CAGE_SITES) == 43
        and len(p.local_source(word(0))) == 50,
        (len(p.DATA), len(p.CAGE_SITES), len(p.local_source(word(0)))),
    )
    check(
        "126 canonical rows have only five- or six-parent radius-one inputs",
        len(p.CANONICAL_TABLE) == 126
        and arities == {5: 62, 6: 64}
        and all(
            direction in p.c53.DIRECTIONS
            for local in p.CANONICAL_TABLE
            for direction, _value in local
        ),
        arities,
    )
    check(
        "3,024 decoder rows are disjoint from the 9,836-row bound law",
        len(p.DECODER_RAW) == 3_024
        and set(p.DECODER_RAW).isdisjoint(p.bound.FINAL_RAW)
        and len(p.MERGED_RAW) == 12_860,
        (len(p.DECODER_RAW), len(p.bound.FINAL_RAW), len(p.MERGED_RAW)),
    )
    check(
        "merged law is single-valued and alphabet-closed",
        not p.RAW_CONFLICTS
        and all(len(values) == 1 for values in p.MERGED_RAW.values())
        and {
            value
            for local, outputs in p.MERGED_RAW.items()
            for value in (*[item for _direction, item in local], *outputs)
        } <= p.cell.FULL_ROLES,
    )
    check(
        "MARK cage has no unary continuation in the merged law",
        not any(len(local) == 1 and local[0][1] == p.CAGE_ROLE for local in p.MERGED_RAW),
    )

    print("\nALL WORDS, SCHEDULES, AND ROTATIONS")
    failures = []
    states = edges = 0
    for rotation_index, rotation in enumerate(p.c53.ROTATIONS):
        for value in range(64):
            ok, detail = p.exact_instance(word(value), rotation)
            if not ok:
                failures.append((rotation_index, value, detail))
            else:
                local_states, local_edges = detail
                states += local_states
                edges += local_edges
    check(
        "all 1,536 rotated word histories are exact six-write chains",
        not failures and states == 10_752 and edges == 9_216,
        (states, edges, failures[:1]),
    )
    valid_roles = {p.PREFIX_ROLE[word(value)] for value in range(60)}
    reject_roles = {p.PREFIX_ROLE[word(value)] for value in range(60, 64)}
    check(
        "sixty state IDs and four reject IDs are pairwise disjoint",
        len(valid_roles) == 60 and len(reject_roles) == 4 and not (valid_roles & reject_roles),
        (len(valid_roles), len(reject_roles)),
    )
    check(
        "every physical final role replays the exact Cycle-48 decoder result",
        all(
            c48.decode_six(p.ROLE_PREFIX[p.PREFIX_ROLE[word(value)]])
            == (value if value < 60 else None)
            for value in range(64)
        ),
    )
    check(
        "decoder and bound terminal are strictly separated while sharing one law",
        min(
            sum(abs(a - b) for a, b in zip(left, right))
            for left in p.BOUND_TERMINAL
            for right in p.transform(p.local_source(word(0)), p.c53.ROTATIONS[0])
        ) > 1,
    )

    print("\nCORRUPTION AND PARENT NECESSITY")
    deletion_attempts, deletion_failures = deletion_controls()
    check(
        "deleting any literal bit stalls before the missing position",
        deletion_attempts == 384 and not deletion_failures,
        (deletion_attempts, deletion_failures[:1]),
    )
    flip_failures = []
    for value in range(64):
        original = word(value)
        for index in range(6):
            changed = list(original)
            changed[index] ^= 1
            changed_word: p.Word = tuple(changed)  # type: ignore[assignment]
            ok, detail = p.exact_instance(changed_word, p.c53.ROTATIONS[0])
            if not ok or p.PREFIX_ROLE[changed_word] == p.PREFIX_ROLE[original]:
                flip_failures.append((value, index, detail))
    check(
        "flipping any bit yields the distinct changed-word ID",
        not flip_failures,
        flip_failures[:1],
    )
    attempts, survivors, alternate_fronts = direct_parent_mutations()
    check(
        "all direct-parent deletion/value mutations suppress the intended write",
        attempts == (62 * 5 + 64 * 6) * 153 and not survivors,
        (attempts, survivors[:1], len(alternate_fronts)),
    )

    print("\nSCOPE")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split()) if NOTE.is_file() else ""
    for phrase in (
        "finite_cycle48_local_decoder",
        "six literal permanent h0/h1 records",
        "not generated from the recurrent archive",
        "born–lüders weights remain conditional",
        "no axiom addition follows",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
    ):
        check("note contains: " + phrase, phrase in note)

    print("\nTOTAL")
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "FINITE_CYCLE48_LOCAL_DECODER" if FAIL == 0 else "FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
