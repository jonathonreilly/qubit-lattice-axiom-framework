#!/usr/bin/env python3
"""Cycle 455: physical precommit-ratchet corpus/count bridge.

Compose independent actual Cycle-452 ratchets into a finite protected corpus.
The reversible counter is controlled by copied local decoder fragments, never
by a host-supplied outcome word.  This finite candidate corpus is not a Record,
an occurrence, realized history, probability, or a Born/frequency theorem.
Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_precommit_local_ratchet_dilation_cycle452_2026_07_19 as c452


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_PRECOMMIT_RATCHET_CORPUS_COUNT_BRIDGE_CYCLE455_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TRAIN_WORD = (1, 0, 1)
HELD_WORD = (1, 0, 1, 0, 0, 1)
MAX_TRIALS = len(HELD_WORD)
ID_BITS = 3
ORDER_BITS = 3
PROGRAM_BITS = len(c452.ROUTE_NAMES)
FRAGMENT_BITS = 3
ENTRY_BITS = ID_BITS + ORDER_BITS + PROGRAM_BITS + FRAGMENT_BITS
PASS = 0
FAIL = 0

Word = tuple[int, ...]
Coord = tuple[int, int, int]


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    output = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return output


_cursor = [MAX_TRIALS * c452.TOTAL_M2]
SOURCE_IDENTITIES = tuple(take(_cursor, ID_BITS) for _ in range(MAX_TRIALS))
SOURCE_ORDERS = tuple(take(_cursor, ORDER_BITS) for _ in range(MAX_TRIALS))
CORPUS_IDENTITIES = tuple(take(_cursor, ID_BITS) for _ in range(MAX_TRIALS))
CORPUS_ORDERS = tuple(take(_cursor, ORDER_BITS) for _ in range(MAX_TRIALS))
CORPUS_PROGRAMS = tuple(take(_cursor, PROGRAM_BITS) for _ in range(MAX_TRIALS))
CORPUS_FRAGMENTS = tuple(take(_cursor, FRAGMENT_BITS) for _ in range(MAX_TRIALS))
COUNT_UNARY = take(_cursor, MAX_TRIALS + 1)
VISIBLE_SITES = tuple(
    index
    for trial in range(MAX_TRIALS)
    for field in (
        CORPUS_IDENTITIES[trial],
        CORPUS_ORDERS[trial],
        CORPUS_PROGRAMS[trial],
        CORPUS_FRAGMENTS[trial],
    )
    for index in field
) + COUNT_UNARY
CORPUS_SITES = VISIBLE_SITES[: -(MAX_TRIALS + 1)]
RESET_SINK = take(_cursor, len(VISIBLE_SITES))
TOTAL_M2 = _cursor[0]


@dataclass(frozen=True)
class State:
    bits: Word
    trials: int
    calls: int


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class CorpusEntry:
    identity: int
    order: int
    program: str
    fragments: Word


@dataclass(frozen=True)
class CorpusReadout:
    entries: tuple[CorpusEntry, ...]
    candidate_word: Word
    committed_count: int
    finite_count_ratio: Fraction
    sha256: str


@dataclass(frozen=True)
class Trace:
    logical_gates: int
    nearest_neighbor_primitives: int
    maximum_support: int
    connected_failures: int
    sha256: str


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    value = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        value = value.replace(marker, "")
    return " ".join(value.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "physical precommit-ratchet corpus/count bridge",
        "independent actual cycle-452 ratchets",
        "101001",
        "computed reversibly from copied local decoder fragments",
        "finite candidate corpus is not an actual realized history",
        "count ratio is not probability",
        "all 24 proper-cubic frames",
        "n1 — alternative route enumeration",
        "n8 — claim-gate result",
        "broad negative claim: fail",
        "no axiom pressure",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle455 note freezes the candidate-history firewall and N1-N8 gate", not missing, missing)


def is_word(value: object, width: int) -> bool:
    return (
        isinstance(value, tuple)
        and len(value) == width
        and all(
            isinstance(bit, int)
            and not isinstance(bit, bool)
            and bit in (0, 1)
            for bit in value
        )
    )


def binary(value: int, width: int) -> Word:
    if value not in range(1 << width):
        raise ValueError("integer does not fit the declared M2 field")
    return tuple((value >> shift) & 1 for shift in reversed(range(width)))


def integer(word: Word) -> int:
    if not is_word(word, len(word)):
        raise ValueError("nonbinary integer field")
    value = 0
    for bit in word:
        value = 2 * value + bit
    return value


def selected(bits: Word | list[int], sites: tuple[int, ...]) -> Word:
    return tuple(bits[index] for index in sites)


def replace_selected(bits: list[int], sites: tuple[int, ...], values: Word) -> None:
    if len(sites) != len(values):
        raise ValueError("field width mismatch")
    for site, value in zip(sites, values):
        bits[site] = value


def trial_sites(trial: int) -> tuple[int, ...]:
    start = trial * c452.TOTAL_M2
    return tuple(range(start, start + c452.TOTAL_M2))


def shifted(sites: tuple[int, ...], trial: int) -> tuple[int, ...]:
    offset = trial * c452.TOTAL_M2
    return tuple(offset + site for site in sites)


def route_program(name: str) -> Word:
    if name not in c452.c449.PROGRAMS:
        raise ValueError("unknown Cycle449 law program")
    return c452.c449.PROGRAMS[name]


def route_ready_packets(case_name: str, program: str):
    stimulus = "three_agree" if program == "threshold3" else "single"
    return c452.c449.packet_sets(case_name)[stimulus]


def route_dark_packets(case_name: str, program: str):
    if program == "threshold3":
        return c452.c449.packet_sets(case_name)["single"]
    return c452.actual_unready_packets(case_name)


def validate_state(state: State, *, initial: bool = False) -> None:
    if not isinstance(state, State) or not is_word(state.bits, TOTAL_M2):
        raise ValueError("Cycle455 state is outside its binary M2 domain")
    expected_calls = c452.TRAIN_CALLS if state.trials == len(TRAIN_WORD) else c452.HELD_CALLS
    if state.trials not in (len(TRAIN_WORD), len(HELD_WORD)) or state.calls != expected_calls:
        raise ValueError("state leaves the frozen train/held domain")
    for trial in range(state.trials):
        c452.validate_state(c452.State(selected(state.bits, trial_sites(trial))))
    if any(state.bits[index] for trial in range(state.trials, MAX_TRIALS) for index in trial_sites(trial)):
        raise ValueError("inactive independent-ratchet blocks must remain blank")
    if initial:
        for trial in range(state.trials):
            block = c452.State(selected(state.bits, trial_sites(trial)))
            c452.validate_state(block, initial=True, calls=state.calls)
            if selected(state.bits, SOURCE_IDENTITIES[trial]) != binary(trial + 1, ID_BITS):
                raise ValueError("trial identity source is malformed")
            if selected(state.bits, SOURCE_ORDERS[trial]) != binary(trial, ORDER_BITS):
                raise ValueError("trial order source is malformed")
        inactive_headers = tuple(
            index
            for trial in range(state.trials, MAX_TRIALS)
            for index in SOURCE_IDENTITIES[trial] + SOURCE_ORDERS[trial]
        )
        if any(
            state.bits[index]
            for index in inactive_headers + CORPUS_SITES + COUNT_UNARY[1:] + RESET_SINK
        ):
            raise ValueError("inactive headers, corpus, count tail, and reset sink must enter blank")
        if state.bits[COUNT_UNARY[0]] != 1:
            raise ValueError("unary counter resource must start at zero")


def prepare_sequence(case_name: str, program: str, word: Word) -> State:
    if case_name not in ("train_L3", "held_L6"):
        raise ValueError("unknown Cycle443 train/held fixture")
    if word not in (TRAIN_WORD, HELD_WORD):
        raise ValueError("candidate word is outside the frozen train/held set")
    calls = c452.TRAIN_CALLS if word == TRAIN_WORD else c452.HELD_CALLS
    if (case_name, len(word)) not in (("train_L3", 3), ("held_L6", 6)):
        raise ValueError("fixture and candidate-word size do not match")
    program_word = route_program(program)
    bits = [0] * TOTAL_M2
    for trial, desired in enumerate(word):
        packets = (
            route_ready_packets(case_name, program)
            if desired
            else route_dark_packets(case_name, program)
        )
        block = c452.prepare_joined(packets, program_word, calls=calls)
        replace_selected(bits, trial_sites(trial), block.bits)
        replace_selected(bits, SOURCE_IDENTITIES[trial], binary(trial + 1, ID_BITS))
        replace_selected(bits, SOURCE_ORDERS[trial], binary(trial, ORDER_BITS))
    bits[COUNT_UNARY[0]] = 1
    state = State(tuple(bits), len(word), calls)
    validate_state(state, initial=True)
    return state


def gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    arities = {"CNOT": 2, "FREDKIN": 3, "SWAP": 2}
    if kind not in arities or len(sites) != arities[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed Cycle455 gate")
    if any(site not in range(TOTAL_M2) for site in sites):
        raise ValueError("Cycle455 gate leaves the finite block")
    return Gate(kind, sites, label)


@lru_cache(maxsize=None)
def corpus_schedule(trials: int) -> tuple[Gate, ...]:
    if trials not in (len(TRAIN_WORD), len(HELD_WORD)):
        raise ValueError("corpus schedule leaves the frozen sizes")
    gates: list[Gate] = []
    for trial in range(trials):
        for lane, (source, target) in enumerate(zip(SOURCE_IDENTITIES[trial], CORPUS_IDENTITIES[trial])):
            gates.append(gate("CNOT", (source, target), f"trial{trial}:identity:{lane}"))
        for lane, (source, target) in enumerate(zip(SOURCE_ORDERS[trial], CORPUS_ORDERS[trial])):
            gates.append(gate("CNOT", (source, target), f"trial{trial}:order:{lane}"))
        for lane, (source, target) in enumerate(
            zip(shifted(c452.c449.PROGRAM, trial), CORPUS_PROGRAMS[trial])
        ):
            gates.append(gate("CNOT", (source, target), f"trial{trial}:program:{lane}"))
        for lane, (source, target) in enumerate(
            zip(shifted(c452.DECODER_FRAGMENTS, trial), CORPUS_FRAGMENTS[trial])
        ):
            gates.append(gate("CNOT", (source, target), f"trial{trial}:decoder:{lane}"))
        control = CORPUS_FRAGMENTS[trial][0]
        for count in reversed(range(trials)):
            gates.append(
                gate(
                    "FREDKIN",
                    (control, COUNT_UNARY[count], COUNT_UNARY[count + 1]),
                    f"trial{trial}:count:{count}",
                )
            )
    return tuple(gates)


@lru_cache(maxsize=1)
def reset_schedule() -> tuple[Gate, ...]:
    return tuple(
        gate("SWAP", (source, sink), f"reset:{lane}")
        for lane, (source, sink) in enumerate(zip(VISIBLE_SITES, RESET_SINK))
    )


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "FREDKIN":
        control, left, right = item.sites
        if bits[control]:
            bits[left], bits[right] = bits[right], bits[left]
    elif item.kind == "SWAP":
        left, right = item.sites
        bits[left], bits[right] = bits[right], bits[left]
    else:
        raise ValueError("unknown Cycle455 gate")


def apply_schedule(
    state: State,
    schedule: tuple[Gate, ...],
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> State:
    validate_state(state)
    bits = list(state.bits)
    order = reversed(schedule) if reverse else schedule
    for item in order:
        if item.label != delete_label:
            apply_gate(bits, item)
    output = replace(state, bits=tuple(bits))
    validate_state(output)
    return output


def replace_trial(state: State, trial: int, block: c452.State) -> State:
    bits = list(state.bits)
    replace_selected(bits, trial_sites(trial), block.bits)
    return replace(state, bits=tuple(bits))


def forward_trial(
    block: c452.State,
    calls: int,
    *,
    delete_label: str | None = None,
) -> c452.State:
    if delete_label is None:
        return c452.joined_forward(block, calls)
    precommit = c452.c449.apply_logical(c452.c449.BasisState(block.bits[: c452.c449.TOTAL_M2]))
    start = c452.replace_precommit(block, precommit)
    return c452.apply_cells(start, calls, delete_label=delete_label)


def joined_forward(
    state: State,
    *,
    delete_corpus_label: str | None = None,
    delete_ratchet: tuple[int, str] | None = None,
) -> State:
    validate_state(state, initial=True)
    output = state
    for trial in range(state.trials):
        block = c452.State(selected(output.bits, trial_sites(trial)))
        deletion = delete_ratchet[1] if delete_ratchet and delete_ratchet[0] == trial else None
        output = replace_trial(output, trial, forward_trial(block, state.calls, delete_label=deletion))
    return apply_schedule(output, corpus_schedule(state.trials), delete_label=delete_corpus_label)


def joined_inverse(state: State) -> State:
    output = apply_schedule(state, corpus_schedule(state.trials), reverse=True)
    for trial in reversed(range(state.trials)):
        block = c452.State(selected(output.bits, trial_sites(trial)))
        output = replace_trial(output, trial, c452.joined_inverse(block, state.calls))
    validate_state(output, initial=True)
    return output


def coarse_candidate_word(initial: State) -> Word:
    outputs = []
    for trial in range(initial.trials):
        block = c452.State(selected(initial.bits, trial_sites(trial)))
        precommit_input = c452.c449.BasisState(block.bits[: c452.c449.TOTAL_M2])
        program = selected(precommit_input.bits, c452.c449.PROGRAM)
        packets = tuple(
            c452.c449.CandidatePacket(
                selected(precommit_input.bits, c452.c449.CANDIDATE[bank]),
                selected(precommit_input.bits, c452.c449.ADMISSION[bank]),
                f"decoded physical bank {bank}",
            )
            for bank in range(3)
        )
        view = c452.c449.coarse_view(packets, program, precommit_input.bits[c452.c449.MIGRATION_TOKEN])
        outputs.append(int(c452.route_from_view(view) is not None))
    return tuple(outputs)


def expected_visible(initial: State) -> Word:
    word = coarse_candidate_word(initial)
    bits = [0] * TOTAL_M2
    for trial, outcome in enumerate(word):
        replace_selected(bits, CORPUS_IDENTITIES[trial], binary(trial + 1, ID_BITS))
        replace_selected(bits, CORPUS_ORDERS[trial], binary(trial, ORDER_BITS))
        program = selected(initial.bits, shifted(c452.c449.PROGRAM, trial))
        replace_selected(bits, CORPUS_PROGRAMS[trial], program)
        replace_selected(bits, CORPUS_FRAGMENTS[trial], (outcome,) * 3)
    bits[COUNT_UNARY[sum(word)]] = 1
    return selected(tuple(bits), VISIBLE_SITES)


def program_name(word: Word) -> str | None:
    return next((name for name, value in c452.c449.PROGRAMS.items() if value == word), None)


def decode_corpus(state: State) -> CorpusReadout | None:
    validate_state(state)
    entries: list[CorpusEntry] = []
    program_words: list[Word] = []
    candidate: list[int] = []
    for trial in range(state.trials):
        identity_word = selected(state.bits, CORPUS_IDENTITIES[trial])
        order_word = selected(state.bits, CORPUS_ORDERS[trial])
        program_word = selected(state.bits, CORPUS_PROGRAMS[trial])
        fragments = selected(state.bits, CORPUS_FRAGMENTS[trial])
        name = program_name(program_word)
        if (
            integer(identity_word) != trial + 1
            or integer(order_word) != trial
            or name is None
            or fragments not in ((0, 0, 0), (1, 1, 1))
        ):
            return None
        program_words.append(program_word)
        candidate.append(fragments[0])
        entries.append(CorpusEntry(trial + 1, trial, name, fragments))
    if len(set(program_words)) != 1:
        return None
    count_word = selected(state.bits, COUNT_UNARY[: state.trials + 1])
    if sum(count_word) != 1 or any(state.bits[index] for index in COUNT_UNARY[state.trials + 1 :]):
        return None
    count = count_word.index(1)
    if count != sum(candidate):
        return None
    signature = tuple(
        bit
        for entry in entries
        for bit in binary(entry.identity, ID_BITS)
        + binary(entry.order, ORDER_BITS)
        + route_program(entry.program)
        + entry.fragments
    ) + count_word
    return CorpusReadout(
        tuple(entries),
        tuple(candidate),
        count,
        Fraction(count, state.trials),
        sha256(bytes(signature)).hexdigest(),
    )


def require_blank_reset_sink(state: State) -> None:
    validate_state(state)
    if any(state.bits[index] for index in RESET_SINK):
        raise ValueError("corpus reset sink must enter blank")


def apply_reset(
    state: State,
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> State:
    if not reverse:
        require_blank_reset_sink(state)
    return apply_schedule(state, reset_schedule(), reverse=reverse, delete_label=delete_label)


def reset_trials_to_their_sinks(state: State, *, reverse: bool = False) -> State:
    output = state
    for trial in range(state.trials):
        block = c452.State(selected(output.bits, trial_sites(trial)))
        output = replace_trial(output, trial, c452.apply_reset(block, reverse=reverse))
    return output


@lru_cache(maxsize=None)
def route_for_gate(item: Gate) -> tuple[tuple[int, int], ...]:
    labels = list(range(TOTAL_M2))
    targets = tuple(range(TOTAL_M2 - len(item.sites), TOTAL_M2))
    swaps: list[tuple[int, int]] = []
    for desired, target in zip(reversed(item.sites), reversed(targets)):
        position = labels.index(desired)
        if position > target:
            raise RuntimeError("Cycle455 right-edge routing invariant failed")
        while position < target:
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            swaps.append((position, position + 1))
            position += 1
    if tuple(labels[index] for index in targets) != item.sites:
        raise RuntimeError("Cycle455 routed operand order is not exact")
    return tuple(swaps)


def apply_nearest_neighbor(state: State, schedule: tuple[Gate, ...]) -> State:
    validate_state(state)
    bits = list(state.bits)
    for item in schedule:
        swaps = route_for_gate(item)
        for left, right in swaps:
            bits[left], bits[right] = bits[right], bits[left]
        width = len(item.sites)
        apply_gate(bits, Gate(item.kind, tuple(range(TOTAL_M2 - width, TOTAL_M2)), item.label))
        for left, right in reversed(swaps):
            bits[left], bits[right] = bits[right], bits[left]
    return replace(state, bits=tuple(bits))


@lru_cache(maxsize=None)
def compiled_trace(trials: int) -> Trace:
    digest = sha256()
    primitives = 0
    maximum_support = 0
    failures = 0
    for item in corpus_schedule(trials):
        swaps = route_for_gate(item)
        for left, right in swaps:
            for name in ("CNOT", "CNOT", "CNOT"):
                digest.update(f"{name}:{left},{right}\n".encode())
                primitives += 1
                maximum_support = max(maximum_support, 2)
                failures += int(right != left + 1)
        support = tuple(range(TOTAL_M2 - len(item.sites), TOTAL_M2))
        digest.update(f"{item.kind}:{','.join(map(str, support))}\n".encode())
        primitives += 1
        maximum_support = max(maximum_support, len(support))
        failures += int(any(right != left + 1 for left, right in zip(support, support[1:])))
        for left, right in reversed(swaps):
            for name in ("CNOT", "CNOT", "CNOT"):
                digest.update(f"{name}:{left},{right}\n".encode())
                primitives += 1
                maximum_support = max(maximum_support, 2)
                failures += int(right != left + 1)
    return Trace(len(corpus_schedule(trials)), primitives, maximum_support, failures, digest.hexdigest())


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                frames.append(matrix)
    return tuple(frames)


def connected(coords: tuple[Coord, ...]) -> bool:
    return all(
        sum(abs(left[axis] - right[axis]) for axis in range(3)) == 1
        for left, right in zip(coords, coords[1:])
    )


def exact_bridge_controls() -> dict[str, object]:
    print("\nINDEPENDENT ACTUAL RATCHETS / E455-G455 / INVERSE")
    rows = []
    held_reference: State | None = None
    for case_name, word in (("train_L3", TRAIN_WORD), ("held_L6", HELD_WORD)):
        for program in c452.ROUTE_NAMES:
            initial = prepare_sequence(case_name, program, word)
            physical = joined_forward(initial)
            decoded = decode_corpus(physical)
            recovered = joined_inverse(physical)
            coarse = coarse_candidate_word(initial)
            row = {
                "case": case_name,
                "program": program,
                "independent_blocks": len({trial_sites(i) for i in range(initial.trials)}) == initial.trials,
                "physical_word": None if decoded is None else decoded.candidate_word,
                "coarse_word": coarse,
                "E455G_equals_GphysicalE455": selected(physical.bits, VISIBLE_SITES) == expected_visible(initial),
                "inverse_exact": recovered == initial,
                "count": None if decoded is None else decoded.committed_count,
                "ratio": None if decoded is None else str(decoded.finite_count_ratio),
                "program_retained": all(
                    selected(physical.bits, shifted(c452.c449.PROGRAM, trial)) == route_program(program)
                    and selected(physical.bits, CORPUS_PROGRAMS[trial]) == route_program(program)
                    for trial in range(initial.trials)
                ),
                "local_fragments": tuple(
                    selected(physical.bits, shifted(c452.DECODER_FRAGMENTS, trial))
                    for trial in range(initial.trials)
                ),
                "work_leakage": sum(
                    c452.c449.work_leakage(
                        c452.c449.BasisState(selected(physical.bits, trial_sites(trial))[: c452.c449.TOTAL_M2])
                    )
                    + physical.bits[trial * c452.TOTAL_M2 + c452.PREFIX_WORK]
                    for trial in range(initial.trials)
                ),
            }
            rows.append(row)
            if case_name == "held_L6" and program == "immediate":
                held_reference = physical
    passed = all(
        row["independent_blocks"]
        and row["physical_word"] == row["coarse_word"]
        and row["physical_word"] in (TRAIN_WORD, HELD_WORD)
        and row["E455G_equals_GphysicalE455"]
        and row["inverse_exact"]
        and row["program_retained"]
        and row["work_leakage"] == 0
        and row["count"] == sum(row["physical_word"])
        for row in rows
    )
    check(
        "three Cycle449 programs produce the train/held corpus and reversible count from independent actual Cycle452 fragments",
        passed,
        rows,
    )
    assert held_reference is not None
    return {"rows": rows, "held_reference": held_reference}


def dark_and_refusal_controls() -> None:
    print("\nDARK / REFUSAL / FIXTURE CONTROLS")
    rows = []
    for program in c452.ROUTE_NAMES:
        initial = prepare_sequence("train_L3", program, TRAIN_WORD)
        # Replace every trial with the route-specific actual dark preparation.
        bits = list(initial.bits)
        for trial in range(initial.trials):
            block = c452.prepare_joined(
                route_dark_packets("train_L3", program),
                route_program(program),
                calls=c452.TRAIN_CALLS,
            )
            replace_selected(bits, trial_sites(trial), block.bits)
        dark_initial = replace(initial, bits=tuple(bits))
        dark = joined_forward(dark_initial)
        view = decode_corpus(dark)
        rows.append((program, None if view is None else view.candidate_word, None if view is None else view.finite_count_ratio))
    refusals = 0
    malformed_calls = (
        lambda: prepare_sequence("held_L6", "immediate", TRAIN_WORD),
        lambda: prepare_sequence("train_L3", "unknown", TRAIN_WORD),
        lambda: prepare_sequence("train_L3", "immediate", (1, 2, 1)),
    )
    for operation in malformed_calls:
        try:
            operation()
        except ValueError:
            refusals += 1
    valid = prepare_sequence("train_L3", "immediate", TRAIN_WORD)
    bits = list(valid.bits)
    bits[SOURCE_IDENTITIES[0][2]] = 0
    try:
        validate_state(replace(valid, bits=tuple(bits)), initial=True)
    except ValueError:
        refusals += 1
    check(
        "route-specific dark fixtures yield a protected 000 corpus while malformed word/program/header domains refuse",
        all(word == (0, 0, 0) and ratio == Fraction(0, 1) for _, word, ratio in rows)
        and refusals == 4,
        {"dark_rows": rows, "lawful_domain_refusals": refusals},
    )


def deletion_controls() -> None:
    print("\nIDENTITY / ORDER / PROGRAM / DECODER / RESOURCE DELETIONS")
    initial = prepare_sequence("held_L6", "immediate", HELD_WORD)
    baseline = joined_forward(initial)
    baseline_view = decode_corpus(baseline)
    deletions = {
        "trial_identity": joined_forward(initial, delete_corpus_label="trial0:identity:2"),
        "trial_order": joined_forward(initial, delete_corpus_label="trial1:order:2"),
        "program": joined_forward(initial, delete_corpus_label="trial0:program:0"),
        "decoder_fragment": joined_forward(initial, delete_corpus_label="trial0:decoder:1"),
        "counter_resource": joined_forward(initial, delete_corpus_label="trial0:count:0"),
    }
    resource_bits = list(initial.bits)
    resource_site = c452.c449.ADMISSION[0][0]
    resource_bits[resource_site] = 0
    resource_deleted_initial = replace(initial, bits=tuple(resource_bits))
    ratchet_deleted = joined_forward(resource_deleted_initial)
    ratchet_deleted_view = decode_corpus(ratchet_deleted)
    check(
        "trial identity/order/program/decoder/count deletions refuse the corpus; one ratchet-resource deletion changes the exact frozen fixture",
        baseline_view is not None
        and baseline_view.candidate_word == HELD_WORD
        and all(decode_corpus(state) is None for state in deletions.values())
        and ratchet_deleted_view is not None
        and ratchet_deleted_view.candidate_word != HELD_WORD
        and ratchet_deleted_view.candidate_word == (0,) + HELD_WORD[1:],
        {
            "baseline": baseline_view,
            "metadata_decoder_deletions_refused": {name: decode_corpus(state) for name, state in deletions.items()},
            "first_ratchet_admission_resource_site_deleted": resource_site,
            "ratchet_resource_deleted_view": ratchet_deleted_view,
        },
    )


def reset_and_sink_controls(reference: State) -> None:
    print("\nRESET / EXPLICIT SINK ACCOUNTING")
    before = decode_corpus(reference)
    reset_sources = reset_trials_to_their_sinks(reference)
    after_source_reset = decode_corpus(reset_sources)
    source_sinks_match = all(
        selected(reset_sources.bits, shifted(c452.RESET_SINK_SITES, trial))
        == selected(reference.bits, shifted(c452.VISIBLE_SITES, trial))
        and not any(selected(reset_sources.bits, shifted(c452.VISIBLE_SITES, trial)))
        for trial in range(reference.trials)
    )
    source_reset_restored = reset_trials_to_their_sinks(reset_sources, reverse=True)
    visible_before = selected(reference.bits, VISIBLE_SITES)
    reset = apply_reset(reference)
    sink_after = selected(reset.bits, RESET_SINK)
    restored = apply_reset(reset, reverse=True)
    populated_lane = next(
        lane for lane, site in enumerate(VISIBLE_SITES) if reference.bits[site]
    )
    partial = apply_reset(reference, delete_label=f"reset:{populated_lane}")
    dirty_bits = list(reference.bits)
    dirty_bits[RESET_SINK[0]] = 1
    dirty_refused = False
    try:
        apply_reset(replace(reference, bits=tuple(dirty_bits)))
    except ValueError:
        dirty_refused = True
    check(
        "ratchet-source resets preserve the copied corpus and complete visible reset exports bit-for-bit to an explicit sink with exact inverse",
        before is not None
        and after_source_reset == before
        and source_sinks_match
        and source_reset_restored == reference
        and not any(selected(reset.bits, VISIBLE_SITES))
        and sink_after == visible_before
        and restored == reference
        and any(selected(partial.bits, VISIBLE_SITES))
        and dirty_refused,
        {
            "corpus_survives_individual_ratchet_resets": after_source_reset == before,
            "source_sinks_match_committed_views": source_sinks_match,
            "source_reset_inverse_exact": source_reset_restored == reference,
            "visible_bits_exported": len(VISIBLE_SITES),
            "visible_support_before": len(set((visible_before, (0,) * len(visible_before)))),
            "visible_support_after": 1,
            "sink_support_after": len(set((sink_after, (0,) * len(sink_after)))),
            "inverse_exact": restored == reference,
            "deleted_populated_reset_lane": populated_lane,
            "incomplete_reset_detected": any(selected(partial.bits, VISIBLE_SITES)),
            "dirty_sink_refused": dirty_refused,
            "interpretation": "finite bit/support accounting only; not heat or thermodynamic cost",
        },
    )


def routed_and_covariance_controls() -> dict[str, object]:
    print("\nNEAREST-NEIGHBOUR COMPOSITION / ALL-24 COVARIANCE")
    initial = prepare_sequence("held_L6", "migrating", HELD_WORD)
    logical_trials = initial
    for trial in range(initial.trials):
        block = c452.State(selected(logical_trials.bits, trial_sites(trial)))
        logical_trials = replace_trial(logical_trials, trial, c452.joined_forward(block, initial.calls))
    logical = apply_schedule(logical_trials, corpus_schedule(initial.trials))
    routed = apply_nearest_neighbor(logical_trials, corpus_schedule(initial.trials))
    trace = compiled_trace(initial.trials)
    frames = proper_cubic_frames()
    base_line = tuple((index, 0, 0) for index in range(TOTAL_M2))
    frame_rows = []
    for frame in frames:
        mapped = tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in base_line)
        frame_rows.append(
            round(np.linalg.det(frame)) == 1
            and len({tuple(frame.flatten())}) == 1
            and connected(mapped)
            and decode_corpus(logical) == decode_corpus(routed)
        )
    c449_trace = c452.c449.nn_trace()
    c452_trace = c452.compiled_trace()
    total_logical = initial.trials * (c449_trace.logical_gates + c452_trace.logical_gates) + trace.logical_gates
    total_primitives = initial.trials * (
        c449_trace.nearest_neighbor_primitives + c452_trace.nearest_neighbor_primitives
    ) + trace.nearest_neighbor_primitives
    check(
        "the corpus circuit executes exactly under restored-placement NN routing and the complete composed line is covariant in all 24 proper-cubic frames",
        routed == logical
        and trace.maximum_support <= 3
        and trace.connected_failures == 0
        and len(frames) == 24
        and len({tuple(frame.flatten()) for frame in frames}) == 24
        and all(frame_rows),
        {
            "Cycle455_aggregation_trace": trace,
            "composed_held_logical_gates": total_logical,
            "composed_held_NN_primitives": total_primitives,
            "inherited_Cycle449_trace": c449_trace,
            "inherited_Cycle452_trace": c452_trace,
            "frames": len(frames),
            "frame_failures": len(frame_rows) - sum(frame_rows),
        },
    )
    return {
        "trace": trace,
        "composed_logical": total_logical,
        "composed_primitives": total_primitives,
    }


def semantic_firewall_controls(reference: State) -> None:
    print("\nACTUALITY / RECORD / PROBABILITY FIREWALL")
    view = decode_corpus(reference)

    def qualification(
        *,
        occurrence: bool,
        record_typing: bool,
        permanence: bool,
        selected_law: bool,
        history_actual: bool,
        probability_law: bool,
    ) -> object | None:
        if not (
            view is not None
            and occurrence
            and record_typing
            and permanence
            and selected_law
            and history_actual
            and probability_law
        ):
            return None
        return "separately qualified history/statistics object"

    baseline = qualification(
        occurrence=True,
        record_typing=True,
        permanence=True,
        selected_law=True,
        history_actual=True,
        probability_law=True,
    )
    deletions = {
        name: qualification(
            occurrence=name != "occurrence",
            record_typing=name != "Record typing",
            permanence=name != "permanence",
            selected_law=name != "law selection",
            history_actual=name != "actual history",
            probability_law=name != "probability law",
        )
        for name in (
            "occurrence",
            "Record typing",
            "permanence",
            "law selection",
            "actual history",
            "probability law",
        )
    }
    check(
        "the physical corpus and count exist while every occurrence/Record/history/law/probability promotion remains separately load-bearing",
        view is not None
        and baseline is not None
        and all(value is None for value in deletions.values()),
        {
            "physical_candidate_corpus": view,
            "semantic_baseline_is_explicitly_supplied": baseline,
            "semantic_deletions": deletions,
            "sampler": None,
            "selected_law": None,
            "actual_member": None,
            "frequency_theorem": None,
        },
    )


def inventory_controls(trace: dict[str, object]) -> None:
    print("\nPHYSICAL / SUPPLIED INVENTORY")
    ratchet_sites = MAX_TRIALS * c452.TOTAL_M2
    source_headers = MAX_TRIALS * (ID_BITS + ORDER_BITS)
    corpus_sites = MAX_TRIALS * ENTRY_BITS
    counter_sites = MAX_TRIALS + 1
    reset_sites = len(VISIBLE_SITES)
    expected_total = ratchet_sites + source_headers + corpus_sites + counter_sites + reset_sites
    check(
        "the held construction inventories every M2, bounded support, finite overhead, and supplied fixture structure",
        TOTAL_M2 == expected_total
        and len(VISIBLE_SITES) == corpus_sites + counter_sites
        and len(RESET_SINK) == len(VISIBLE_SITES)
        and trace["composed_logical"] > 0
        and trace["composed_primitives"] > trace["composed_logical"],
        {
            "independent_actual_Cycle452_blocks": ratchet_sites,
            "source_identity_order": source_headers,
            "protected_corpus": corpus_sites,
            "unary_counter": counter_sites,
            "explicit_corpus_reset_sink": reset_sites,
            "total_M2": TOTAL_M2,
            "maximum_primitive_support": 3,
            "supplied": (
                "finite trial count and train/held fixture sequence",
                "independent Cycle452 blocks, fresh-token envelopes, and route programs",
                "route-specific ready/dark Cycle443 packets",
                "trial identities, order labels, blank corpus/counter/sink resources",
                "fixed update order, restored-placement line, frame maps, and readout codec",
            ),
            "derived": (
                "ratchet fragment word",
                "copied protected corpus",
                "reversible unary count and finite ratio",
                "exact inverse, deletion responses, and reset export",
            ),
        },
    )


def main() -> int:
    print("Cycle 455 physical precommit-ratchet corpus/count bridge")
    print("authority=none audit=unset")
    note_contract()
    results = exact_bridge_controls()
    dark_and_refusal_controls()
    deletion_controls()
    reset_and_sink_controls(results["held_reference"])
    trace = routed_and_covariance_controls()
    semantic_firewall_controls(results["held_reference"])
    inventory_controls(trace)
    print(f"\nFINAL: {PASS} passed, {FAIL} failed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
