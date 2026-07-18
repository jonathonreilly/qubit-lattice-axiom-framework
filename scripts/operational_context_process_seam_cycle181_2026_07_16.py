#!/usr/bin/env python3
"""Cycle 181: late context-choice / instrument / memory process seam.

This runner consumes the frozen Cycle-177 nine-source/six-context apparatus
only at its exact deterministic record interface.  It attaches an explicit
late-choice protocol graph, then compares normalized continuation laws that
share the same physical source/terminal map.

It does not supply or claim quantum statistics, physical contextuality,
instrument equivalence, a Born rule, or an axiom amendment.
"""

from __future__ import annotations

import hashlib
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path

import all_nine_six_context_shared_ancestry_cycle177_2026_07_16 as c177


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "OPERATIONAL_CONTEXT_PROCESS_SEAM_CYCLE181_NOTE_2026-07-16.md"
)
CYCLE177 = (
    ROOT
    / "scripts/all_nine_six_context_shared_ancestry_cycle177_2026_07_16.py"
)
CYCLE177_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ALL_NINE_SIX_CONTEXT_SHARED_ANCESTRY_CYCLE177_NOTE_2026-07-16.md"
)
FROZEN = {
    CYCLE177: "45af53a19db6879c133ace06536d5a98d2c9b6407419ec6e5e944090601343a5",
    CYCLE177_NOTE: "cffc1111e334f32dbe950c0e1cc0ef2457862a6c05b2e76b01d190d1c987af16",
}

Bit = int
Assignment = tuple[Bit, ...]
Pattern = tuple[Bit, ...]
Kernel = tuple[Fraction, Fraction]
Fingerprint = tuple[Kernel, ...]

ASSIGNMENTS: tuple[Assignment, ...] = tuple(
    product((0, 1), repeat=len(c177.OBSERVABLE_IDS))
)
CONTEXT_LABELS = tuple(label for label, _ids, _sign in c177.EXPECTED_CONTEXTS)
INSTRUMENTS = ("preserve", "refresh")
HALF = Fraction(1, 2)

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


def exact_context_pattern(assignment: Assignment) -> Pattern:
    """Cycle-177's six deterministic context bits in closed GF(2) form."""

    signs = dict(zip(c177.OBSERVABLE_IDS, assignment, strict=True))
    return tuple(
        1 ^ unsigned_sign ^ signs[first] ^ signs[second] ^ signs[third]
        for _label, (first, second, third), unsigned_sign
        in c177.EXPECTED_CONTEXTS
    )


PATTERNS = {
    assignment: exact_context_pattern(assignment)
    for assignment in ASSIGNMENTS
}


@dataclass(frozen=True)
class ProtocolRecord:
    stage: int
    kind: str
    label: object
    content: object
    parents: tuple[object, ...]


@dataclass(frozen=True)
class LateChoiceTranscript:
    assignment: Assignment
    terminal_pattern: Pattern
    context_index: int
    context_label: str
    instrument: str
    outcome: Bit
    records: tuple[ProtocolRecord, ...]


def physical_source_records(assignment: Assignment) -> tuple[ProtocolRecord, ...]:
    sources, _splitters = c177.source_geometry()
    signs = dict(zip(c177.OBSERVABLE_IDS, assignment, strict=True))
    return tuple(
        ProtocolRecord(
            0,
            "physical-source",
            measurement_id,
            signs[measurement_id],
            (sources[measurement_id],),
        )
        for measurement_id in c177.OBSERVABLE_IDS
    )


def terminal_anchors() -> dict[str, tuple[int, int, int]]:
    output_site = c177.fully_ported_plan().output_site
    return {
        label: c177.shifted(output_site, c177.CONTEXT_SHIFTS[label])
        for label in CONTEXT_LABELS
    }


def physical_terminal_records(
    assignment: Assignment,
) -> tuple[ProtocolRecord, ...]:
    anchors = terminal_anchors()
    pattern = PATTERNS[assignment]
    return tuple(
        ProtocolRecord(
            1,
            "physical-context-terminal",
            label,
            bit,
            (anchors[label],),
        )
        for label, bit in zip(CONTEXT_LABELS, pattern, strict=True)
    )


def omission_records(assignment: Assignment) -> tuple[ProtocolRecord, ...]:
    return physical_source_records(assignment) + physical_terminal_records(assignment)


def late_choice_transcript(
    assignment: Assignment,
    context_index: int,
    instrument: str,
) -> LateChoiceTranscript:
    if instrument not in INSTRUMENTS:
        raise ValueError(("unknown-instrument", instrument))
    label = CONTEXT_LABELS[context_index]
    pattern = PATTERNS[assignment]
    outcome = pattern[context_index]
    base = omission_records(assignment)
    terminal_keys = tuple(
        ("physical-context-terminal", terminal_label)
        for terminal_label in CONTEXT_LABELS
    )
    ready = ProtocolRecord(
        2,
        "terminal-ready",
        "six-context-apparatus",
        1,
        terminal_keys,
    )
    choice = ProtocolRecord(
        3,
        "context-choice",
        label,
        1,
        (("terminal-ready", "six-context-apparatus"),),
    )
    instrument_record = ProtocolRecord(
        4,
        "instrument",
        instrument,
        1,
        (("context-choice", label),),
    )
    outcome_record = ProtocolRecord(
        4,
        "selected-outcome",
        label,
        outcome,
        (
            ("physical-context-terminal", label),
            ("context-choice", label),
            ("instrument", instrument),
        ),
    )
    return LateChoiceTranscript(
        assignment=assignment,
        terminal_pattern=pattern,
        context_index=context_index,
        context_label=label,
        instrument=instrument,
        outcome=outcome,
        records=base + (ready, choice, instrument_record, outcome_record),
    )


def immediate_visible(transcript: LateChoiceTranscript) -> tuple[str, Bit]:
    """The deliberately instrument-blind current readout."""

    return transcript.context_label, transcript.outcome


def forgotten_display(transcript: LateChoiceTranscript) -> tuple[object, ...]:
    """A decoder that hides the selected outcome but not physical intervention."""

    return tuple(
        (record.kind, record.label, record.content)
        for record in transcript.records
        if record.kind != "selected-outcome"
    )


def future_kernel(
    assignment: Assignment,
    next_context_index: int,
    instrument: str,
) -> Kernel:
    """One-step continuation over a fresh downstream apparatus region."""

    if instrument == "preserve":
        bit = PATTERNS[assignment][next_context_index]
        return (Fraction(1 - bit), Fraction(bit))
    if instrument == "refresh":
        return (HALF, HALF)
    raise ValueError(("unknown-instrument", instrument))


def future_fingerprint(
    assignment: Assignment,
    instrument: str,
) -> Fingerprint:
    return tuple(
        future_kernel(assignment, context_index, instrument)
        for context_index in range(len(CONTEXT_LABELS))
    )


def grouped_fingerprint_counts(decoder) -> dict[object, int]:
    fibres: dict[object, set[Fingerprint]] = defaultdict(set)
    for assignment in ASSIGNMENTS:
        for context_index in range(len(CONTEXT_LABELS)):
            for instrument in INSTRUMENTS:
                transcript = late_choice_transcript(
                    assignment,
                    context_index,
                    instrument,
                )
                fibres[decoder(transcript)].add(
                    future_fingerprint(assignment, instrument)
                )
    return {
        fibre: len(fingerprints)
        for fibre, fingerprints in fibres.items()
    }


def frozen_output_table(first_context: int, second_context: int) -> dict[tuple[Bit, Bit], Fraction]:
    counts: Counter[tuple[Bit, Bit]] = Counter(
        (
            PATTERNS[assignment][first_context],
            PATTERNS[assignment][second_context],
        )
        for assignment in ASSIGNMENTS
    )
    return {
        outcomes: Fraction(counts[outcomes], len(ASSIGNMENTS))
        for outcomes in product((0, 1), repeat=2)
    }


def iid_output_table(_first_context: int, _second_context: int) -> dict[tuple[Bit, Bit], Fraction]:
    return {
        outcomes: Fraction(1, 4)
        for outcomes in product((0, 1), repeat=2)
    }


def sticky_output_table(first_context: int, second_context: int) -> dict[tuple[Bit, Bit], Fraction]:
    frozen = frozen_output_table(first_context, second_context)
    iid = iid_output_table(first_context, second_context)
    return {
        outcomes: HALF * frozen[outcomes] + HALF * iid[outcomes]
        for outcomes in product((0, 1), repeat=2)
    }


def equality_probability(table: dict[tuple[Bit, Bit], Fraction]) -> Fraction:
    return table[(0, 0)] + table[(1, 1)]


def normalized_table(table: dict[tuple[Bit, Bit], Fraction]) -> bool:
    return (
        set(table) == set(product((0, 1), repeat=2))
        and all(weight >= 0 for weight in table.values())
        and sum(table.values(), Fraction()) == 1
    )


def source_transition_normalization() -> tuple[bool, object]:
    sample = ASSIGNMENTS[137]
    iid_sum = sum(
        (Fraction(1, len(ASSIGNMENTS)) for _candidate in ASSIGNMENTS),
        Fraction(),
    )
    frozen_sum = sum(
        (
            Fraction(int(candidate == sample))
            for candidate in ASSIGNMENTS
        ),
        Fraction(),
    )
    sticky_sum = sum(
        (
            HALF * int(candidate == sample)
            + Fraction(1, 2 * len(ASSIGNMENTS))
            for candidate in ASSIGNMENTS
        ),
        Fraction(),
    )
    sticky_min = min(
        HALF * int(candidate == sample)
        + Fraction(1, 2 * len(ASSIGNMENTS))
        for candidate in ASSIGNMENTS
    )
    return (
        iid_sum == frozen_sum == sticky_sum == 1 and sticky_min > 0,
        {
            "iid": iid_sum,
            "frozen": frozen_sum,
            "sticky": sticky_sum,
            "sticky_min": sticky_min,
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("FROZEN PHYSICAL INTERFACE")
    observed_hashes = {path: sha256(path) for path in FROZEN}
    check(
        "Cycle 177 runner and note remain frozen",
        observed_hashes == FROZEN,
        {path.name: value for path, value in observed_hashes.items()},
    )
    semantic_failures = []
    for assignment in ASSIGNMENTS:
        _semantics, reference = c177.assignment_semantics(assignment)
        if PATTERNS[assignment] != reference:
            semantic_failures.append((assignment, PATTERNS[assignment], reference))
            if len(semantic_failures) >= 5:
                break
    pattern_counts = Counter(PATTERNS.values())
    hamming_histogram = Counter(sum(pattern) for pattern in PATTERNS.values())
    check(
        "closed GF(2) form exactly reproduces all 512 Cycle-177 terminal vectors",
        not semantic_failures
        and len(pattern_counts) == 32
        and set(pattern_counts.values()) == {16}
        and hamming_histogram == Counter({1: 96, 3: 320, 5: 96}),
        {
            "failures": semantic_failures,
            "patterns": len(pattern_counts),
            "multiplicity": sorted(set(pattern_counts.values())),
            "histogram": hamming_histogram,
        },
    )
    anchors = terminal_anchors()
    check(
        "the protocol attachment uses the six exact physical terminal anchors",
        anchors
        == {
            "R1": (0, -10_000, -1),
            "R2": (0, -6_000, -1),
            "R3": (0, -2_000, -1),
            "C1": (0, 2_000, -1),
            "C2": (0, 6_000, -1),
            "C3": (0, 10_000, -1),
        },
        anchors,
    )

    print("\nEXPLICIT LATE CONTEXT-CHOICE RECORDS")
    transcripts = tuple(
        late_choice_transcript(assignment, context_index, "preserve")
        for assignment in ASSIGNMENTS
        for context_index in range(len(CONTEXT_LABELS))
    )
    check(
        "all 512 x 6 late choices copy exactly one already-formed terminal record",
        len(transcripts) == 3_072
        and all(
            transcript.outcome
            == transcript.terminal_pattern[transcript.context_index]
            for transcript in transcripts
        ),
        len(transcripts),
    )
    check(
        "choice and selected-outcome records are strictly later than all six terminals",
        all(
            max(
                record.stage
                for record in transcript.records
                if record.kind == "physical-context-terminal"
            )
            < min(
                record.stage
                for record in transcript.records
                if record.kind in {"context-choice", "selected-outcome"}
            )
            for transcript in transcripts
        ),
        "terminal stage 1; choice stage 3; selected outcome stage 4",
    )
    no_retro_failures = []
    for assignment in ASSIGNMENTS:
        patterns = {
            late_choice_transcript(assignment, context_index, "preserve").terminal_pattern
            for context_index in range(len(CONTEXT_LABELS))
        }
        if patterns != {PATTERNS[assignment]}:
            no_retro_failures.append((assignment, patterns))
    check(
        "late choice never changes the pre-existing six-terminal vector",
        not no_retro_failures,
        no_retro_failures[:5],
    )

    print("\nOMISSION VERSUS MEASURE-AND-FORGET")
    omission_failures = []
    future_separations = 0
    for assignment in ASSIGNMENTS:
        omitted = omission_records(assignment)
        for context_index in range(len(CONTEXT_LABELS)):
            measured = late_choice_transcript(
                assignment,
                context_index,
                "refresh",
            )
            if not set(omitted) < set(measured.records):
                omission_failures.append((assignment, context_index))
            if any(
                record.kind == "selected-outcome"
                for record in measured.records
            ) and all(
                item[0] != "selected-outcome"
                for item in forgotten_display(measured)
            ):
                pass
            else:
                omission_failures.append(("forget-decoder", assignment, context_index))
            if future_kernel(assignment, context_index, "preserve") != future_kernel(
                assignment,
                context_index,
                "refresh",
            ):
                future_separations += 1
    check(
        "omission is not record deletion after an intervention",
        not omission_failures and future_separations == 3_072,
        {
            "failures": omission_failures[:5],
            "future_separations": future_separations,
        },
    )
    passive = late_choice_transcript(ASSIGNMENTS[0], 0, "preserve")
    disturbing = late_choice_transcript(ASSIGNMENTS[0], 0, "refresh")
    check(
        "measure-and-forget need not disturb, but its physical protocol record remains",
        immediate_visible(passive) == immediate_visible(disturbing)
        and forgotten_display(passive) != forgotten_display(disturbing)
        and set(omission_records(ASSIGNMENTS[0])) < set(passive.records),
        {
            "omitted_records": len(omission_records(ASSIGNMENTS[0])),
            "passive_records": len(passive.records),
            "refresh_records": len(disturbing.records),
        },
    )

    print("\nSAME IMMEDIATE OUTCOME / DIFFERENT FUTURE")
    same_immediate = 0
    different_future = 0
    for assignment in ASSIGNMENTS:
        for context_index in range(len(CONTEXT_LABELS)):
            preserve = late_choice_transcript(
                assignment,
                context_index,
                "preserve",
            )
            refresh = late_choice_transcript(
                assignment,
                context_index,
                "refresh",
            )
            same_immediate += int(
                immediate_visible(preserve) == immediate_visible(refresh)
            )
            different_future += int(
                future_fingerprint(assignment, "preserve")
                != future_fingerprint(assignment, "refresh")
            )
    check(
        "preserve and refresh instruments agree now and disagree on continuation",
        same_immediate == different_future == 3_072,
        {
            "same_immediate": same_immediate,
            "different_future": different_future,
        },
    )

    print("\nNORMALIZED MEMORY COMPARATORS")
    source_normalized, source_detail = source_transition_normalization()
    check(
        "IID, frozen, and full-support sticky source transitions normalize exactly",
        source_normalized,
        source_detail,
    )
    one_shot = {
        context_index: Fraction(
            sum(PATTERNS[assignment][context_index] for assignment in ASSIGNMENTS),
            len(ASSIGNMENTS),
        )
        for context_index in range(len(CONTEXT_LABELS))
    }
    check(
        "all six one-shot context marginals are exactly one half",
        set(one_shot.values()) == {HALF},
        dict(zip(CONTEXT_LABELS, one_shot.values(), strict=True)),
    )
    memory_failures = []
    equality = {}
    for first_context in range(len(CONTEXT_LABELS)):
        for second_context in range(len(CONTEXT_LABELS)):
            tables = {
                "iid": iid_output_table(first_context, second_context),
                "frozen": frozen_output_table(first_context, second_context),
                "sticky": sticky_output_table(first_context, second_context),
            }
            if not all(normalized_table(table) for table in tables.values()):
                memory_failures.append(("normalization", first_context, second_context, tables))
            equality[(first_context, second_context)] = {
                label: equality_probability(table)
                for label, table in tables.items()
            }
            wanted = (
                {"iid": HALF, "frozen": Fraction(1), "sticky": Fraction(3, 4)}
                if first_context == second_context
                else {"iid": HALF, "frozen": HALF, "sticky": HALF}
            )
            if equality[(first_context, second_context)] != wanted:
                memory_failures.append(
                    (
                        "equality",
                        first_context,
                        second_context,
                        equality[(first_context, second_context)],
                        wanted,
                    )
                )
            if any(weight <= 0 for weight in tables["sticky"].values()):
                memory_failures.append(("sticky-support", first_context, second_context))
    check(
        "same one-shot marginals coexist with distinct exact repeated-context laws",
        not memory_failures,
        {
            "same_context": equality[(0, 0)],
            "different_context": equality[(0, 1)],
            "failures": memory_failures[:5],
        },
    )

    print("\nRECORD-FIBRE STRONG LUMPABILITY")
    outcome_only = grouped_fingerprint_counts(
        lambda transcript: immediate_visible(transcript)
    )
    instrument_blind = grouped_fingerprint_counts(
        lambda transcript: (
            transcript.terminal_pattern,
            transcript.context_label,
            transcript.outcome,
        )
    )
    instrument_visible_pattern_hidden = grouped_fingerprint_counts(
        lambda transcript: (
            transcript.context_label,
            transcript.outcome,
            transcript.instrument,
        )
    )
    complete_operational = grouped_fingerprint_counts(
        lambda transcript: (
            transcript.terminal_pattern,
            transcript.context_label,
            transcript.outcome,
            transcript.instrument,
        )
    )
    check(
        "outcome-only and instrument-blind record fibres are not future-lumpable",
        max(outcome_only.values()) > 1
        and max(instrument_blind.values()) > 1,
        {
            "outcome_only_max": max(outcome_only.values()),
            "instrument_blind_max": max(instrument_blind.values()),
        },
    )
    preserve_hidden_counts = grouped_fingerprint_counts(
        lambda transcript: (
            transcript.context_label,
            transcript.outcome,
            transcript.instrument,
        )
        if transcript.instrument == "preserve"
        else (
            "separate-refresh",
            transcript.assignment,
            transcript.context_label,
        )
    )
    check(
        "instrument labels alone do not replace the preparation/terminal record class",
        max(instrument_visible_pattern_hidden.values()) > 1
        and max(preserve_hidden_counts.values()) > 1,
        {
            "all_instruments_max": max(instrument_visible_pattern_hidden.values()),
            "preserve_max": max(preserve_hidden_counts.values()),
        },
    )
    check(
        "context + instrument + full six-terminal pattern is strongly lumpable",
        set(complete_operational.values()) == {1},
        {
            "fibres": len(complete_operational),
            "max_fingerprints": max(complete_operational.values()),
        },
    )
    check(
        "the six-context operational preparation quotient has 32 classes, not 512",
        len(pattern_counts) == 32
        and set(pattern_counts.values()) == {16},
        {
            "classes": len(pattern_counts),
            "raw_assignments_per_class": sorted(set(pattern_counts.values())),
            "source-sensitive-classes": len(ASSIGNMENTS),
        },
    )

    print("\nSCOPE AND IMPORT FIREWALL")
    note_text = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    normalized = " ".join(note_text.lower().split())
    required = (
        "all six terminal records exist before the late choice",
        "classical record lookup",
        "not a physical contextuality result",
        "not a quantum-statistics derivation",
        "normalized process/history functional remains imported",
        "prepared-state or boundary interface remains imported",
        "identity containment remains imported",
        "instrument transition remains imported",
        "actuality and frequency remain imported",
        "no axiom conclusion follows",
        "## n1",
        "## n2",
        "## n3",
        "## n4",
        "## n5",
        "## n6",
        "## n7",
        "## n8",
    )
    missing = tuple(phrase for phrase in required if phrase not in normalized)
    check(
        "the Cycle-181 note preserves the operational and constitutional firewall",
        not missing,
        missing,
    )

    print("\nACCOUNTING")
    print("ASSIGNMENTS", len(ASSIGNMENTS))
    print("PATTERNS", len(pattern_counts), sorted(set(pattern_counts.values())))
    print("LATE_TRANSCRIPTS", len(transcripts))
    print("ONE_SHOT", one_shot)
    print("MEMORY_SAME_CONTEXT", equality[(0, 0)])
    print("MEMORY_DIFFERENT_CONTEXT", equality[(0, 1)])
    print(
        "LUMPABILITY",
        {
            "outcome_only_max": max(outcome_only.values()),
            "instrument_blind_max": max(instrument_blind.values()),
            "instrument_visible_pattern_hidden_max": max(
                instrument_visible_pattern_hidden.values()
            ),
            "complete_max": max(complete_operational.values()),
        },
    )
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE181_OPERATIONAL_PROCESS_SEAM_CLASSIFIED"
        if FAIL == 0
        else "CYCLE181_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
