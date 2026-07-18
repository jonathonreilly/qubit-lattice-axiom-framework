#!/usr/bin/env python3
"""Cycle 45 exact complete-history and counterfactual-law reconstruction probes."""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import product
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "COMPLETE_HISTORY_RECONSTRUCTION_CYCLE45_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
CYCLE42 = REVIEW / "REALIZED_HISTORY_EXACT_LAW_IDENTIFIABILITY_CYCLE42_NOTE_2026-07-14.md"
UNIQUE_EXTENSION = REVIEW / "DETERMINISTIC_UNIQUE_EXTENSION_RECORD_SECTOR_NOTE_2026-07-14.md"
FREQUENCY = REVIEW / "CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md"
ACTUALITY = REVIEW / "STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md"
ADAPTIVE = REVIEW / "ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md"
MOVING = REVIEW / "MOVING_LOGICAL_APPARATUS_APPEND_FRONT_CYCLE34_NOTE_2026-07-14.md"
GLOBAL_PROCESS = REVIEW / "GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md"

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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    text = text.replace("**", "")
    text = text.replace("`", "")
    return " ".join(text.split())


def markdown_subsection(text: str, number: int) -> str:
    lowered = text.lower()
    start_marker = f"### n{number} —"
    end_marker = f"### n{number + 1} —" if number < 8 else "## bottom line"
    start = lowered.index(start_marker)
    end = lowered.index(end_marker, start)
    return lowered[start:end]


@dataclass(frozen=True)
class EventRecord:
    event_id: str
    parent_id: str | None
    before: str
    protocol: str
    outcome: int
    after: str


def reconstruct_chain(records: tuple[EventRecord, ...]) -> tuple[EventRecord, ...]:
    """Reconstruct a unique finite history from certified predecessor headers."""
    if not records:
        raise ValueError("empty corpus")
    by_id = {record.event_id: record for record in records}
    if len(by_id) != len(records):
        raise ValueError("duplicate event id")
    roots = [record for record in records if record.parent_id is None]
    if len(roots) != 1:
        raise ValueError("corpus needs one genesis")

    child_of: dict[str, EventRecord] = {}
    for record in records:
        if record.parent_id is None:
            continue
        if record.parent_id not in by_id:
            raise ValueError("missing parent")
        if record.parent_id in child_of:
            raise ValueError("forked history")
        child_of[record.parent_id] = record

    ordered = [roots[0]]
    seen = {roots[0].event_id}
    while ordered[-1].event_id in child_of:
        child = child_of[ordered[-1].event_id]
        if child.event_id in seen:
            raise ValueError("causal cycle")
        if ordered[-1].after != child.before:
            raise ValueError("state-transition mismatch")
        ordered.append(child)
        seen.add(child.event_id)
    if len(ordered) != len(records):
        raise ValueError("disconnected corpus")
    return tuple(ordered)


def corpus_history_reconstruction() -> None:
    section("B - Permanent-corpus to complete-history reconstruction")
    ordered = (
        EventRecord("e0", None, "s0", "prepare-00", 0, "s1"),
        EventRecord("e1", "e0", "s1", "probe-left", 1, "s2"),
        EventRecord("e2", "e1", "s2", "probe-right", 0, "s3"),
        EventRecord("e3", "e2", "s3", "close", 1, "s4"),
    )
    scrambled = (ordered[2], ordered[0], ordered[3], ordered[1])
    recovered = reconstruct_chain(scrambled)
    check("B scrambled permanent corpus reconstructs one ordered history", recovered == ordered)
    check("B reconstructed history has one genesis", sum(r.parent_id is None for r in recovered) == 1)
    check("B every adjacent state is consistent", all(a.after == b.before for a, b in zip(recovered, recovered[1:])))
    check("B all protocols and outcomes survive ordering", tuple((r.protocol, r.outcome) for r in recovered) == tuple((r.protocol, r.outcome) for r in ordered))
    check("B reconstruction does not use input-list order", tuple(r.event_id for r in scrambled) != tuple(r.event_id for r in recovered))

    gap = tuple(record for record in ordered if record.event_id != "e2")
    try:
        reconstruct_chain(gap)
        gap_rejected = False
    except ValueError:
        gap_rejected = True
    check("B missing-parent corpus is rejected", gap_rejected)

    fork = ordered + (EventRecord("e1b", "e0", "s1", "probe-up", 0, "sx"),)
    try:
        reconstruct_chain(fork)
        fork_rejected = False
    except ValueError:
        fork_rejected = True
    check("B forked corpus is rejected", fork_rejected)

    inconsistent = tuple(
        replace(record, before="wrong") if record.event_id == "e2" else record
        for record in ordered
    )
    try:
        reconstruct_chain(inconsistent)
        mismatch_rejected = False
    except ValueError:
        mismatch_rejected = True
    check("B state-inconsistent corpus is rejected", mismatch_rejected)

    unordered_multiset = sorted((0, 1))
    check("B bare outcome multiset admits two orders", sorted((0, 1)) == unordered_multiset and sorted((1, 0)) == unordered_multiset and (0, 1) != (1, 0))


CONTEXTS = tuple(product((0, 1), repeat=3))
RULE_110 = {
    (1, 1, 1): 0,
    (1, 1, 0): 1,
    (1, 0, 1): 1,
    (1, 0, 0): 0,
    (0, 1, 1): 1,
    (0, 1, 0): 1,
    (0, 0, 1): 1,
    (0, 0, 0): 0,
}


def global_ring_update(configuration: tuple[int, ...], table: dict[tuple[int, int, int], int]) -> tuple[int, ...]:
    size = len(configuration)
    return tuple(
        table[(configuration[(index - 1) % size], configuration[index], configuration[(index + 1) % size])]
        for index in range(size)
    )


def reconstruct_deterministic_table(rows: tuple[tuple[tuple[int, int, int], int], ...]) -> dict[tuple[int, int, int], int]:
    table: dict[tuple[int, int, int], int] = {}
    for context, outcome in rows:
        if context in table and table[context] != outcome:
            raise ValueError("inconsistent response row")
        table[context] = outcome
    if set(table) != set(CONTEXTS):
        raise ValueError("incomplete context domain")
    return table


def deterministic_unique_extension() -> None:
    section("C - Deterministic universal-context unique extension")
    rows = tuple((context, RULE_110[context]) for context in CONTEXTS)
    shuffled = tuple(rows[index] for index in (6, 0, 4, 2, 7, 1, 5, 3))
    reconstructed = reconstruct_deterministic_table(shuffled)
    check("C universal corpus covers every radius-one binary context", set(reconstructed) == set(CONTEXTS))
    check("C deterministic response rows reconstruct Rule 110 exactly", reconstructed == RULE_110)

    configurations = tuple(product((0, 1), repeat=4))
    check(
        "C reconstructed local table fixes every four-site ring counterfactual",
        all(global_ring_update(config, reconstructed) == global_ring_update(config, RULE_110) for config in configurations),
    )
    check("C global extension covers all sixteen four-site configurations", len(configurations) == 16)

    changed = dict(RULE_110)
    changed[(1, 1, 1)] = 1
    check("C universal corpus separates a one-row rival", any(reconstructed[c] != changed[c] for c in CONTEXTS))

    partial_rows = tuple(row for row in rows if row[0] != (1, 1, 1))
    partial_signature = dict(partial_rows)
    check("C partial corpus leaves a rival extension", all(partial_signature[c] == changed[c] for c in partial_signature) and changed[(1, 1, 1)] != RULE_110[(1, 1, 1)])
    try:
        reconstruct_deterministic_table(partial_rows)
        missing_rejected = False
    except ValueError:
        missing_rejected = True
    check("C reconstruction rejects a missing counterfactual row", missing_rejected)


def deterministic_response(law: str, step: int, action: int) -> int:
    if law == "L0":
        return 0
    if law == "L1":
        return 0 if step == 0 else action
    if law == "L2":
        return 1 if step == 0 else 1 - action
    raise ValueError(law)


def adaptive_signature(law: str) -> tuple[tuple[int, int], ...]:
    first_action = 0
    first_outcome = deterministic_response(law, 0, first_action)
    second_action = 1 if first_outcome == 0 else 0
    second_outcome = deterministic_response(law, 1, second_action)
    return ((first_action, first_outcome), (second_action, second_outcome))


def fixed_signature(law: str) -> tuple[int, int]:
    return (
        deterministic_response(law, 0, 0),
        deterministic_response(law, 1, 0),
    )


def adaptive_self_testing() -> None:
    section("D - Finite adaptive self-testing signature")
    laws = ("L0", "L1", "L2")
    adaptive = {law: adaptive_signature(law) for law in laws}
    fixed = {law: fixed_signature(law) for law in laws}
    check("D one adaptive protocol has one signature per candidate", set(adaptive) == set(laws))
    check("D adaptive signatures are pairwise distinct", len(set(adaptive.values())) == len(laws), str(adaptive))
    check("D fixed nonadaptive protocol leaves L0 and L1 identical", fixed["L0"] == fixed["L1"])
    check("D adaptivity separates the fixed-protocol collision", adaptive["L0"] != adaptive["L1"])
    check("D second action genuinely depends on first record", adaptive["L0"][1][0] != adaptive["L2"][1][0])

    actual_signature = adaptive["L1"]
    compatible = tuple(law for law, signature in adaptive.items() if signature == actual_signature)
    check("D exact self-testing corpus identifies one law class member", compatible == ("L1",))


MARKOV_CONTEXTS = tuple(product((0, 1), repeat=2))
MARKOV_ACTIONS = (0, 1)


def exact_markov_kernel() -> dict[tuple[tuple[int, int], int], tuple[Fraction, Fraction]]:
    kernel: dict[tuple[tuple[int, int], int], tuple[Fraction, Fraction]] = {}
    for context in MARKOV_CONTEXTS:
        context_index = 2 * context[0] + context[1]
        for action in MARKOV_ACTIONS:
            ones = 1 + context_index + 2 * action
            kernel[(context, action)] = (Fraction(8 - ones, 8), Fraction(ones, 8))
    return kernel


def reconstruct_markov_kernel(limit_counts: dict[tuple[tuple[int, int], int], tuple[int, int]]) -> dict[tuple[tuple[int, int], int], tuple[Fraction, Fraction]]:
    expected_rows = {(context, action) for context in MARKOV_CONTEXTS for action in MARKOV_ACTIONS}
    if set(limit_counts) != expected_rows:
        raise ValueError("incomplete process-tomography rows")
    return {
        row: tuple(Fraction(count, sum(counts)) for count in counts)
        for row, counts in limit_counts.items()
    }


def adaptive_process_distribution(
    kernel: dict[tuple[tuple[int, int], int], tuple[Fraction, Fraction]],
    horizon: int,
) -> dict[tuple[tuple[int, int], ...], Fraction]:
    frontier: dict[tuple[tuple[int, int], tuple[tuple[int, int], ...]], Fraction] = {
        ((0, 0), ()): Fraction(1)
    }
    for step in range(horizon):
        next_frontier: dict[tuple[tuple[int, int], tuple[tuple[int, int], ...]], Fraction] = {}
        for (context, transcript), weight in frontier.items():
            action = context[0] ^ context[1] ^ (step % 2)
            for outcome, probability in enumerate(kernel[(context, action)]):
                new_context = (context[1], outcome)
                new_transcript = transcript + ((action, outcome),)
                key = (new_context, new_transcript)
                next_frontier[key] = next_frontier.get(key, Fraction(0)) + weight * probability
        frontier = next_frontier
    return {transcript: weight for (_, transcript), weight in frontier.items()}


def finite_order_process_tomography() -> None:
    section("E - Exact finite-order Markov/process tomography")
    kernel = exact_markov_kernel()
    limit_counts = {
        row: (int(probabilities[0] * 8), int(probabilities[1] * 8))
        for row, probabilities in kernel.items()
    }
    reconstructed = reconstruct_markov_kernel(limit_counts)
    check("E all eight context-action rows are certified", len(limit_counts) == 8)
    check("E every exact row normalizes", all(sum(row) == 1 for row in reconstructed.values()))
    check("E exact limiting conditional rows reconstruct the kernel", reconstructed == kernel)

    original_process = adaptive_process_distribution(kernel, 3)
    reconstructed_process = adaptive_process_distribution(reconstructed, 3)
    check("E reconstructed kernel fixes every depth-three adaptive transcript", reconstructed_process == original_process)
    check("E depth-three adaptive process normalizes exactly", sum(original_process.values()) == 1)
    check("E depth-three process has all eight binary outcome transcripts", len(original_process) == 8)
    check("E every displayed transcript has positive rational weight", all(weight > 0 and isinstance(weight, Fraction) for weight in original_process.values()))

    omitted = ((1, 1), 1)
    partial = {row: counts for row, counts in limit_counts.items() if row != omitted}
    rival = dict(kernel)
    rival[omitted] = (Fraction(3, 8), Fraction(5, 8))
    check("E missing row admits a distinct compatible kernel", all(kernel[row] == rival[row] for row in partial) and kernel[omitted] != rival[omitted])
    try:
        reconstruct_markov_kernel(partial)
        omitted_rejected = False
    except ValueError:
        omitted_rejected = True
    check("E tomography rejects incomplete row coverage", omitted_rejected)


def generate_dovetail_corpus(length: int, initial_phase: int = 0) -> tuple[EventRecord, ...]:
    records: list[EventRecord] = []
    phase = initial_phase % len(CONTEXTS)
    parent: str | None = None
    for index in range(length):
        context = CONTEXTS[phase]
        event_id = f"d{index}"
        next_phase = (phase + 1) % len(CONTEXTS)
        records.append(
            EventRecord(
                event_id,
                parent,
                f"phase-{phase}",
                "query-" + "".join(map(str, context)),
                RULE_110[context],
                f"phase-{next_phase}",
            )
        )
        parent = event_id
        phase = next_phase
    return tuple(records)


def law_owned_one_outcome() -> None:
    section("F - Law-owned one-outcome universal corpus")
    corpus = generate_dovetail_corpus(16, initial_phase=0)
    repeated = generate_dovetail_corpus(16, initial_phase=0)
    check("F supplied law and phase generate one exact corpus", corpus == repeated)
    check("F every event has one binary outcome", all(record.outcome in (0, 1) for record in corpus))
    check("F every later event has the prior event as parent", all(record.parent_id == f"d{index - 1}" for index, record in enumerate(corpus) if index > 0))
    check("F every finite prefix preserves all earlier records", all(corpus[:n] == tuple(list(corpus[: n + 1])[:n]) for n in range(1, len(corpus))))
    check("F predecessor headers reconstruct the law-generated history", reconstruct_chain(tuple(reversed(corpus))) == corpus)

    first_cycle = corpus[: len(CONTEXTS)]
    decoded_rows = tuple(
        (
            tuple(int(bit) for bit in record.protocol.removeprefix("query-")),
            record.outcome,
        )
        for record in first_cycle
    )
    check("F one dovetail cycle covers every local context", {context for context, _ in decoded_rows} == set(CONTEXTS))
    check("F the generated history reconstructs the full local law", reconstruct_deterministic_table(decoded_rows) == RULE_110)

    other_boundary = generate_dovetail_corpus(16, initial_phase=1)
    check("F a different supplied phase changes the particular history", corpus != other_boundary)
    other_rows = tuple(
        (
            tuple(int(bit) for bit in record.protocol.removeprefix("query-")),
            record.outcome,
        )
        for record in other_boundary[: len(CONTEXTS)]
    )
    check("F boundary change leaves the reconstructed law invariant", reconstruct_deterministic_table(other_rows) == RULE_110)
    check("F deterministic generator extends to every requested finite length", len(generate_dovetail_corpus(64)) == 64)


def source_and_classification_contract() -> None:
    section("A - Source, primitive, and classification contract")
    sources = (
        NOTE,
        AXIOMS,
        REALIZED,
        CYCLE42,
        UNIQUE_EXTENSION,
        FREQUENCY,
        ACTUALITY,
        ADAPTIVE,
        MOVING,
        GLOBAL_PROCESS,
    )
    for path in sources:
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    realized = normalized(REALIZED)
    cycle42 = normalized(CYCLE42)
    unique = normalized(UNIQUE_EXTENSION)
    frequency = normalized(FREQUENCY)
    actuality = normalized(ACTUALITY)
    adaptive = normalized(ADAPTIVE)
    moving = normalized(MOVING)

    check("A note is authority-free", "authority: none" in note)
    check("A note disclaims foundation edits", "does not amend an axiom" in note)
    check("A note disclaims audit authority", "issue an audit verdict" in note)
    check("A note carries fresh N1-N8", all(f"n{i} —" in note for i in range(1, 9)))
    check("A live state remains record configurations", "a state is a configuration of records" in axioms)
    check("A Admissibility remains non-dynamics", "admissibility is not a dynamics axiom" in axioms)
    check("A realized primitive remains pointwise", "derivations may evaluate at the realized state, pointwise" in realized)
    check("A realized primitive supplies no state", "it does not supply a state, state-selection rule" in realized)
    check("A Cycle 42 leaves separating complete-H route live", "a separating complete-h theorem remains a live zero-edit route" in cycle42)
    check("A unique extension distinguishes law from boundary", "unique continuation still contains the choice" in unique)
    check("A frequency source names the component-mean condition", "component-mean condition" in frequency)
    check("A actuality source names four history routes", all(phrase in actuality for phrase in ("uniquely derived from the law and boundary", "law-owned one-outcome dynamics", "reconstructed from records", "contingent world-history data")))
    check("A adaptive source is finite-protocol exact", "finite adaptive protocol tree" in adaptive)
    check("A moving-front source supplies unique predecessors", "the new record has the unique predecessor" in moving)

    required = (
        "corpus-chain reconstruction theorem",
        "deterministic universal-context theorem",
        "adaptive separating-signature theorem",
        "finite-order process-tomography theorem",
        "law-owned one-outcome recursion theorem",
        "reconstruction implication is exact without a new axiom",
        "not selection of l* by the foundation",
        "the pointwise s_* primitive is neither enlarged nor used as h",
        "no live axiom, primitive, registry, audit, or policy surface is changed",
        "broad history-nonidentifiability claim remains demoted",
    )
    for phrase in required:
        check(f"A note contains: {phrase}", phrase in note)


def no_go_discipline_contract() -> None:
    section("G - Fresh N1-N8 no-go-discipline contract")
    raw = NOTE.read_text(encoding="utf-8")
    parts = {number: markdown_subsection(raw, number) for number in range(1, 9)}
    compact = {number: " ".join(part.split()) for number, part in parts.items()}

    n1_rows = [line.lower() for line in parts[1].splitlines() if line.startswith("|")]
    attempted_rows = [line for line in n1_rows if "| attempted |" in line]
    check("G N1 marks at least five routes ATTEMPTED", len(attempted_rows) >= 5, f"count={len(attempted_rows)}")
    for route in (
        "causal-header corpus reconstruction",
        "deterministic universal-context extension",
        "adaptive finite-class self-test",
        "finite-order process tomography",
        "law-owned one-outcome recursion",
    ):
        check(f"G N1 includes route: {route}", route in parts[1])
    check("G N1 leaves direct foundation uniqueness open", "direct foundation uniqueness | open" in parts[1])

    for wall in ("w_c", "w_d", "w_s", "w_x"):
        check(f"G N2 names {wall}", wall in parts[2])
    for pair in (
        "`w_c`, `w_d`",
        "`w_c`, `w_s`",
        "`w_c`, `w_x`",
        "`w_d`, `w_s`",
        "`w_d`, `w_x`",
        "`w_s`, `w_x`",
    ):
        check(f"G N2 tests pair {pair}", pair in parts[2])
    check("G N2 collapses to four conditions", "collapsed set is {w_c,w_d,w_s,w_x}" in parts[2].replace("`", ""))

    for trigger in (
        "approved",
        "complete corpus",
        "by construction",
        "self-testing",
        "law-owned",
        "exact frequencies",
        "canonical",
    ):
        check(f"G N3 classifies trigger: {trigger}", trigger in parts[3])
    check("G N3 reports zero hidden conditions", "unresolved hidden conditions: 0" in parts[3].replace("*", ""))

    for source in (
        CYCLE42.name.lower(),
        FREQUENCY.name.lower(),
        UNIQUE_EXTENSION.name.lower(),
        ADAPTIVE.name.lower(),
        MOVING.name.lower(),
    ):
        check(f"G N4 maps source: {source}", source in parts[4])
    check("G N4 drops direction-mismatched evidence", "positive comparator only; not negative evidence" in parts[4])

    for resolution in (
        "unordered finite record multiset",
        "certified finite causal chain",
        "finite deterministic local-law domain",
        "finite adaptive candidate class",
        "known finite-order stochastic class",
        "countably complete physical protocol category",
        "unrestricted law space",
    ):
        check(f"G N5 scopes resolution: {resolution}", resolution in parts[5])
    check("G N5 leaves two high-resolution routes open", parts[5].count("not tested / open") >= 2)
    check("G N5 forbids the broad no-go", "no universal history-nonidentifiability theorem is licensed" in parts[5])

    for path in (
        "approved realized-state primitive",
        "causal-header reconstruction",
        "deterministic universal corpus",
        "adaptive separating family",
        "finite-order process tomography",
        "law-owned one-outcome recursion",
        "direct foundation uniqueness",
    ):
        check(f"G N6 contains path: {path}", path in parts[6])
    check("G N6 keeps primitive pointwise", "closes only pointwise evaluation at a supplied s_*" in parts[6].replace("`", ""))
    check("G N6 authorizes no new axiom", "none of these theorem routes entails a new axiom sentence" in compact[6])

    for phrase in (
        "hostile steelman:",
        "outcome:",
        "broad negative is defeated",
        "narrow missing-certificate boundary survives",
    ):
        check(f"G N7 contains: {phrase}", phrase in compact[7].replace("*", ""))

    for source in (
        CYCLE42.name.lower(),
        ACTUALITY.name.lower(),
        FREQUENCY.name.lower(),
        MOVING.name.lower(),
        GLOBAL_PROCESS.name.lower(),
    ):
        check(f"G N8 cites: {source}", source in parts[8])
    n8_plain = compact[8].replace("*", "").replace("`", "")
    check("G N8 records prescribed searches", "prescribed docs phrase scan" in n8_plain and "no_go_ledger.md walk" in n8_plain)
    check("G gate passes only narrow boundary", "gate result: pass for the narrow missing-certificate/nonseparating-signature boundary" in n8_plain)


def main() -> int:
    source_and_classification_contract()
    corpus_history_reconstruction()
    deterministic_unique_extension()
    adaptive_self_testing()
    finite_order_process_tomography()
    law_owned_one_outcome()
    no_go_discipline_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: certified causal records reconstruct H; a separating "
        "deterministic universal corpus reconstructs its declared full law "
        "class; stochastic closure still needs exact pointwise response limits"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
