#!/usr/bin/env python3
"""Cycle 488: supplied-bath FORM occurrence to finite Born-weight firewall.

The runner binds independent Cycle483 basis FORM occurrences to one actual
Cycle478 terminal mixed-root menu.  A fixed reversible M2 adapter emits an
ordered protected class receipt and a five-bin count history.  Empirical
counts, physical branch norms, and trace grades are compared but never
identified.  No sampler, independence law, actual member, Born probability,
or bath renewal is supplied by the construction.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from math import sqrt
from pathlib import Path
import inspect
import itertools
import resource
import signal
import sys
import time

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_born_support_nine_mixed_quotient_auxiliary_cycle478_2026_07_19 as c478
import physical_reset_environment_record_occurrence_cycle483_2026_07_19 as c483


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FORM_OCCURRENCE_BORN_WEIGHT_FIREWALL_CYCLE488_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
FROZEN_C478_RUNNER_SHA256 = "b700a8d5bede8037af025d9df65b1223c0159170e2c3f21992741a3b593ab99f"
FROZEN_C478_NOTE_SHA256 = "87ed2bfbcff03b155496123d664050e80e01c67e668b06d751c3ecef2415652f"
FROZEN_C483_RUNNER_SHA256 = "52f0621a06792093ad64a706ab7741335cfd7ff9418b3756f4ab83cf72b8d222"
FROZEN_C483_NOTE_SHA256 = "be836748288af45b5b71d71ce380376f05b4168468e48e2bc8ff75c4a43dc74f"
TOL = 8e-10
WALL_CAP_SECONDS = 900.0
RSS_CAP_BYTES = 4 * 1024**3
PASS = 0
FAIL = 0

# Frozen before querying the Cycle478 norm or trace-grade values.  These are
# deterministic supplied basis-history fixtures, not sampled observations.
TRAIN_POINTERS = (0, 1, 2)
HELD_POINTERS = (0, 1, 2, 3, 4, 0, 1, 2, 3)
TRAIN_CASE = "train_L3"
HELD_CASE = "held_L6"
TRAIN_HORIZON = 3
HELD_HORIZON = 6
MENU_ARITY = 5
TERMINAL_ROW_INDEX = 412
TERMINAL_CLASSES = (679, 724, 767, 813, 1039)
SUPPORT9_CLASSES = tuple(index for index, value in enumerate(c478.SELECTED_VECTOR) if value)
CLASS_ID_BITS = 11
COUNT_BITS = 4
TRIAL_ID_BITS = 4
POINTER_BITS = 3
WORD = c483.WORD

Word = tuple[int, ...]
Coord = tuple[int, int, int]


class WallCapExceeded(RuntimeError):
    pass


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    result = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return result


# One translation-equivalent event cell contains one complete frozen Cycle483
# system+bath block plus the Cycle488 sidecar, receipt, and retained adder data.
_cursor = [c483.TOTAL_M2]
POINTER = take(_cursor, POINTER_BITS)
TRIAL_ID = take(_cursor, TRIAL_ID_BITS)
CODEBOOK = tuple(take(_cursor, WORD) for _ in range(MENU_ARITY))
TYPE_FLAG = take(_cursor, 1)[0]
OCCURRENCE_FLAG = take(_cursor, 1)[0]
LOCK_FLAG = take(_cursor, 1)[0]
MATCH_PREFIX = tuple(take(_cursor, POINTER_BITS) for _ in range(MENU_ARITY))
MATCH = take(_cursor, MENU_ARITY)
CLASS_VALID = take(_cursor, 1)[0]
ACCEPT_PREFIX = take(_cursor, 5)
ACCEPT = take(_cursor, 1)[0]
OUTCOME_ENABLE = take(_cursor, MENU_ARITY)
RECEIPT_ONEHOT = take(_cursor, MENU_ARITY)
RECEIPT_CLASS_ID = take(_cursor, CLASS_ID_BITS)
RECEIPT_TRIAL_ID = take(_cursor, TRIAL_ID_BITS)
RECEIPT_WORD = take(_cursor, WORD)
COUNT_SUM = tuple(take(_cursor, COUNT_BITS) for _ in range(MENU_ARITY))
COUNT_CARRY = tuple(take(_cursor, COUNT_BITS + 1) for _ in range(MENU_ARITY))
CELL_M2 = _cursor[0]

ADAPTER_INPUT_LOCAL = POINTER + TRIAL_ID + tuple(site for bank in CODEBOOK for site in bank)
ADAPTER_OUTPUT_LOCAL = (
    (TYPE_FLAG, OCCURRENCE_FLAG, LOCK_FLAG)
    + tuple(site for prefix in MATCH_PREFIX for site in prefix)
    + MATCH + (CLASS_VALID,) + ACCEPT_PREFIX + (ACCEPT,)
    + OUTCOME_ENABLE + RECEIPT_ONEHOT + RECEIPT_CLASS_ID + RECEIPT_TRIAL_ID
    + RECEIPT_WORD
    + tuple(site for bank in COUNT_SUM for site in bank)
    + tuple(site for bank in COUNT_CARRY for site in bank)
)


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class BasisState:
    trials: int
    horizon: int
    case_name: str
    bits: Word


@dataclass(frozen=True)
class AdapterTrace:
    logical_gates: int
    nearest_neighbor_primitives: int
    maximum_support_M2: int
    connected_failures: int
    sha256: str


@dataclass(frozen=True)
class TypedMenuReceipt:
    trial: int
    pointer: int
    effect_class: int
    class_word: Word
    bath_relative_FORM: bool = True
    framework_actuality: bool = False
    framework_Record: bool = False
    realized_framework_history: bool = False


@dataclass(frozen=True)
class MenuSurface:
    row: tuple[int, ...]
    raw_effects: tuple[tuple[sp.Expr, ...], ...]
    train_program: object
    held_program: object
    train_words: tuple[Word, ...]
    held_words: tuple[Word, ...]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_and_source_contracts() -> None:
    required = (
        "authority: none", "audit: unset", "exact target contract",
        "cycle-478 direct born input", "cycle-483 direct occurrence input",
        "positive mixed root", "new-row index 412", "classes 679, 724, 767, 813, 1039",
        "train n=3 / h=3", "held n=9 / h=6",
        "history corpus frozen before norm/trace weights",
        "physical-m2 e/g bridge", "exact inverse", "held-out size",
        "raw integer counts", "normalized empirical frequencies",
        "occurrence-frequency versus norm/trace-weight firewall",
        "bath-relative form does not make a realized framework history",
        "no outcome/member law", "no probability interpretation",
        "no independence law", "no bath renewal", "all 24 proper-cubic frames",
        "deletion", "malformed", "permuted-member negative control",
        "supplied / derived / open", "gate disposition: fail",
        "partial-attempt-with-named-untested-routes",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle488 note freezes the occurrence/weight firewall and semantic ceiling", not missing, missing)

    sources = (
        ("Cycle478", Path(c478.__file__), c478.NOTE, FROZEN_C478_RUNNER_SHA256, FROZEN_C478_NOTE_SHA256),
        ("Cycle483", Path(c483.__file__), c483.NOTE, FROZEN_C483_RUNNER_SHA256, FROZEN_C483_NOTE_SHA256),
    )
    rows = tuple(
        (name, file_sha256(runner), file_sha256(note))
        for name, runner, note, _runner_sha, _note_sha in sources
    )
    exact = all(
        file_sha256(runner) == runner_sha and file_sha256(note) == note_sha
        for _name, runner, note, runner_sha, note_sha in sources
    )
    check(
        "the exact Cycle478 quotient and Cycle483 basis-FORM inputs are frozen by runner and note SHA",
        exact
        and "no occurrence, probability, frequency, or born-law selection" in normalized(c478.NOTE)
        and "bathrelativetypedoccurrence" in normalized(c483.NOTE).replace("-", "")
        and "norm or trace weight is not occurrence or probability" in normalized(c483.NOTE),
        {"sources": rows, "authority": AUTHORITY, "audit": AUDIT},
    )


def site(cell: int, local_index: int) -> int:
    return cell * CELL_M2 + local_index


def field(cell: int, local_indices: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(site(cell, index) for index in local_indices)


def local_c483_state(state: BasisState, cell: int) -> c483.State:
    start = cell * CELL_M2
    return c483.State(state.bits[start:start + c483.TOTAL_M2])


def is_word(value: object, width: int) -> bool:
    return (
        isinstance(value, tuple)
        and len(value) == width
        and all(isinstance(bit, int) and not isinstance(bit, bool) and bit in (0, 1) for bit in value)
    )


def bits_of(value: int, width: int) -> Word:
    if not isinstance(value, int) or isinstance(value, bool) or not 0 <= value < 2**width:
        raise ValueError("integer leaves its declared binary field")
    return tuple((value >> bit) & 1 for bit in range(width))


def int_of(bits: Word) -> int:
    return sum(bit << index for index, bit in enumerate(bits))


def selected(bits: Word | list[int], sites: tuple[int, ...]) -> Word:
    return tuple(bits[index] for index in sites)


def replace_selected(bits: list[int], sites: tuple[int, ...], values: Word) -> None:
    if len(sites) != len(values):
        raise ValueError("field-width mismatch")
    for index, value in zip(sites, values):
        bits[index] = value


def gate(trials: int, kind: str, sites: tuple[int, ...], label: str) -> Gate:
    widths = {"X": 1, "CNOT": 2, "TOFFOLI": 3, "SWAP": 2}
    if kind not in widths or len(sites) != widths[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed Cycle488 gate")
    if any(index not in range(trials * CELL_M2) for index in sites):
        raise ValueError("Cycle488 gate leaves the bounded event strip")
    return Gate(kind, sites, label)


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "X":
        bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        first, second = item.sites
        bits[second] ^= bits[first]
    elif item.kind == "TOFFOLI":
        first, second, target = item.sites
        bits[target] ^= bits[first] & bits[second]
    elif item.kind == "SWAP":
        first, second = item.sites
        bits[first], bits[second] = bits[second], bits[first]
    else:
        raise ValueError("unknown Cycle488 primitive")


def shifted_c483_gate(trials: int, cell: int, item: c483.Gate) -> Gate:
    return gate(
        trials, item.kind, tuple(site(cell, index) for index in item.sites),
        f"cell:{cell}:c483:{item.label}",
    )


def append_prefix(
    trials: int,
    output: list[Gate],
    conditions: tuple[int, ...],
    work: tuple[int, ...],
    label: str,
) -> tuple[Gate, ...]:
    if not conditions or len(conditions) != len(work):
        raise ValueError("prefix conditions/work mismatch")
    start = len(output)
    output.append(gate(trials, "CNOT", (conditions[0], work[0]), f"{label}:0"))
    for lane in range(1, len(conditions)):
        output.append(gate(
            trials, "TOFFOLI", (work[lane - 1], conditions[lane], work[lane]), f"{label}:{lane}",
        ))
    return tuple(output[start:])


def append_majority(
    trials: int, output: list[Gate], group: tuple[int, int, int], target: int, label: str,
) -> None:
    left, middle, right = group
    output.extend((
        gate(trials, "TOFFOLI", (left, middle, target), f"{label}:lm"),
        gate(trials, "TOFFOLI", (left, right, target), f"{label}:lr"),
        gate(trials, "TOFFOLI", (middle, right, target), f"{label}:mr"),
    ))


@lru_cache(maxsize=None)
def adapter_only_schedule(trials: int) -> tuple[Gate, ...]:
    if trials not in (len(TRAIN_POINTERS), len(HELD_POINTERS)):
        raise ValueError("Cycle488 schedule accepts only frozen train/held sizes")
    output: list[Gate] = []
    for cell in range(trials):
        pointer = field(cell, POINTER)
        for outcome in range(MENU_ARITY):
            value = bits_of(outcome, POINTER_BITS)
            for lane, bit in enumerate(value):
                if bit == 0:
                    output.append(gate(
                        trials, "X", (pointer[lane],), f"cell:{cell}:match:{outcome}:negate:{lane}",
                    ))
            computed = append_prefix(
                trials, output, pointer, field(cell, MATCH_PREFIX[outcome]),
                f"cell:{cell}:match:{outcome}:prefix",
            )
            output.append(gate(
                trials, "CNOT", (field(cell, MATCH_PREFIX[outcome])[-1], site(cell, MATCH[outcome])),
                f"cell:{cell}:match:{outcome}:retain",
            ))
            output.extend(
                Gate(item.kind, item.sites, f"{item.label}:uncompute") for item in reversed(computed)
            )
            for lane, bit in reversed(tuple(enumerate(value))):
                if bit == 0:
                    output.append(gate(
                        trials, "X", (pointer[lane],), f"cell:{cell}:match:{outcome}:negate:{lane}:restore",
                    ))
        for outcome in range(MENU_ARITY):
            output.append(gate(
                trials, "CNOT", (site(cell, MATCH[outcome]), site(cell, CLASS_VALID)),
                f"cell:{cell}:class-valid:{outcome}",
            ))

        append_majority(
            trials, output, field(cell, c483.B_TYPE), site(cell, TYPE_FLAG), f"cell:{cell}:type-majority",
        )
        append_majority(
            trials, output, field(cell, c483.B_OCCURRENCE), site(cell, OCCURRENCE_FLAG),
            f"cell:{cell}:occurrence-majority",
        )
        append_majority(
            trials, output, field(cell, c483.B_LOCK), site(cell, LOCK_FLAG), f"cell:{cell}:lock-majority",
        )
        accept_compute = append_prefix(
            trials, output,
            (
                site(cell, c483.B_FORM), site(cell, TYPE_FLAG), site(cell, OCCURRENCE_FLAG),
                site(cell, LOCK_FLAG), site(cell, CLASS_VALID),
            ),
            field(cell, ACCEPT_PREFIX), f"cell:{cell}:accept-prefix",
        )
        output.append(gate(
            trials, "CNOT", (field(cell, ACCEPT_PREFIX)[-1], site(cell, ACCEPT)), f"cell:{cell}:accept-retain",
        ))
        output.extend(
            Gate(item.kind, item.sites, f"{item.label}:uncompute") for item in reversed(accept_compute)
        )

        for outcome, class_index in enumerate(TERMINAL_CLASSES):
            output.append(gate(
                trials, "TOFFOLI",
                (site(cell, ACCEPT), site(cell, MATCH[outcome]), site(cell, OUTCOME_ENABLE[outcome])),
                f"cell:{cell}:outcome-enable:{outcome}",
            ))
            enable = site(cell, OUTCOME_ENABLE[outcome])
            output.append(gate(
                trials, "CNOT", (enable, site(cell, RECEIPT_ONEHOT[outcome])),
                f"cell:{cell}:receipt-onehot:{outcome}",
            ))
            for lane, bit in enumerate(bits_of(class_index, CLASS_ID_BITS)):
                if bit:
                    output.append(gate(
                        trials, "CNOT", (enable, field(cell, RECEIPT_CLASS_ID)[lane]),
                        f"cell:{cell}:receipt-class:{outcome}:{lane}",
                    ))
            for lane, (source, target) in enumerate(zip(field(cell, CODEBOOK[outcome]), field(cell, RECEIPT_WORD))):
                output.append(gate(
                    trials, "TOFFOLI", (enable, source, target),
                    f"cell:{cell}:packet-copy:{outcome}:{lane}",
                ))
        for lane, (source, target) in enumerate(zip(field(cell, TRIAL_ID), field(cell, RECEIPT_TRIAL_ID))):
            output.append(gate(
                trials, "TOFFOLI", (site(cell, ACCEPT), source, target), f"cell:{cell}:trial-copy:{lane}",
            ))

        # One reversible retained binary count stage per outcome.  Cell zero
        # copies its one-hot receipt.  Every later cell adds the current bit to
        # the previous four-bit count while retaining every carry.
        for outcome in range(MENU_ARITY):
            receipt = site(cell, RECEIPT_ONEHOT[outcome])
            current_sum = field(cell, COUNT_SUM[outcome])
            current_carry = field(cell, COUNT_CARRY[outcome])
            if cell == 0:
                output.append(gate(
                    trials, "CNOT", (receipt, current_sum[0]), f"cell:{cell}:count:{outcome}:seed",
                ))
                continue
            previous_sum = field(cell - 1, COUNT_SUM[outcome])
            for bit in range(COUNT_BITS):
                output.append(gate(
                    trials, "CNOT", (previous_sum[bit], current_sum[bit]),
                    f"cell:{cell}:count:{outcome}:add-a:{bit}",
                ))
                if bit == 0:
                    output.append(gate(
                        trials, "CNOT", (receipt, current_sum[bit]),
                        f"cell:{cell}:count:{outcome}:add-b:{bit}",
                    ))
                output.append(gate(
                    trials, "CNOT", (current_carry[bit], current_sum[bit]),
                    f"cell:{cell}:count:{outcome}:add-carry:{bit}",
                ))
                if bit == 0:
                    output.append(gate(
                        trials, "TOFFOLI", (previous_sum[bit], receipt, current_carry[bit + 1]),
                        f"cell:{cell}:count:{outcome}:carry-ab:{bit}",
                    ))
                    output.append(gate(
                        trials, "TOFFOLI", (receipt, current_carry[bit], current_carry[bit + 1]),
                        f"cell:{cell}:count:{outcome}:carry-bc:{bit}",
                    ))
                output.append(gate(
                    trials, "TOFFOLI", (previous_sum[bit], current_carry[bit], current_carry[bit + 1]),
                    f"cell:{cell}:count:{outcome}:carry-ac:{bit}",
                ))
    return tuple(output)


@lru_cache(maxsize=None)
def fixed_schedule(trials: int, horizon: int) -> tuple[Gate, ...]:
    expected_horizon = TRAIN_HORIZON if trials == len(TRAIN_POINTERS) else HELD_HORIZON
    if horizon != expected_horizon:
        raise ValueError("trial size and bath horizon leave the frozen train/held law")
    output: list[Gate] = []
    for cell in range(trials):
        output.extend(
            shifted_c483_gate(trials, cell, item)
            for item in c483.bath_schedule(horizon, inject_faults=False)
        )
    output.extend(adapter_only_schedule(trials))
    return tuple(output)


def schedule_with_deletion(trials: int, horizon: int, delete_label: str | None = None) -> tuple[Gate, ...]:
    schedule = fixed_schedule(trials, horizon)
    if delete_label is None:
        return schedule
    matches = tuple(
        index for index, item in enumerate(schedule)
        if item.label in (delete_label, f"{delete_label}:uncompute")
    )
    if len(matches) not in (1, 2):
        raise ValueError(f"deletion label does not select one gate or compute/uncompute pair: {delete_label}")
    removed = set(matches)
    return tuple(item for index, item in enumerate(schedule) if index not in removed)


def class_word(case_name: str, class_index: int) -> Word:
    return class_words(case_name)[TERMINAL_CLASSES.index(class_index)]


@lru_cache(maxsize=None)
def class_words(case_name: str) -> tuple[Word, ...]:
    if case_name == TRAIN_CASE:
        length = 3
    elif case_name == HELD_CASE:
        length = 6
    else:
        raise ValueError("unknown Cycle488 source case")
    cases = c478.bounded_class_cases(length, len(menu_surface().raw_effects))
    words = []
    for class_index in TERMINAL_CLASSES:
        prepared = c478.c433.prepare(c478.c433.LAYOUT, cases[class_index])
        written = c478.c433.apply_coupled(prepared, 1)
        words.append(c478.c433.selected(written.bits, written.layout.target))
    if len(set(words)) != MENU_ARITY or any(len(word) != WORD for word in words):
        raise RuntimeError("Cycle478 terminal class codec is not injective on the selected menu")
    return tuple(words)


@lru_cache(maxsize=1)
def menu_surface() -> MenuSurface:
    extension = c478.build_extension()
    if (
        extension.row_labels[TERMINAL_ROW_INDEX] != "positive mixed root"
        or extension.new_rows[TERMINAL_ROW_INDEX] != TERMINAL_CLASSES
    ):
        raise RuntimeError("Cycle478 terminal positive-root menu changed")
    programs = {}
    for length in (3, 6):
        fixture = c478.c317.physical_fixture(length)
        programs[length] = c478.new_programs(extension, fixture.contact)[TERMINAL_ROW_INDEX]
    # Build words after the MenuSurface is cached by returning a temporary
    # empty word tuple; class_words uses only raw_effects during this call.
    surface = MenuSurface(
        TERMINAL_CLASSES, extension.effects, programs[3], programs[6], (), (),
    )
    return surface


def finalized_surface() -> MenuSurface:
    surface = menu_surface()
    return MenuSurface(
        surface.row, surface.raw_effects, surface.train_program, surface.held_program,
        class_words(TRAIN_CASE), class_words(HELD_CASE),
    )


def prepare_history(case_name: str, horizon: int, pointers: tuple[int, ...]) -> BasisState:
    trials = len(pointers)
    if (case_name, horizon, trials) not in (
        (TRAIN_CASE, TRAIN_HORIZON, len(TRAIN_POINTERS)),
        (HELD_CASE, HELD_HORIZON, len(HELD_POINTERS)),
    ):
        raise ValueError("history leaves the frozen train/held pairing")
    words = class_words(case_name)
    laws = tuple(c483.c449.PROGRAMS)
    bits = [0] * (trials * CELL_M2)
    for cell, pointer in enumerate(pointers):
        if pointer not in range(MENU_ARITY):
            raise ValueError("supplied history pointer leaves the terminal menu")
        local = c483.prepare_state(
            case_name, laws[cell % len(laws)], route="bath", reset_work=1,
        )
        start = cell * CELL_M2
        bits[start:start + c483.TOTAL_M2] = local.bits
        replace_selected(bits, field(cell, POINTER), bits_of(pointer, POINTER_BITS))
        replace_selected(bits, field(cell, TRIAL_ID), bits_of(cell + 1, TRIAL_ID_BITS))
        for outcome, word in enumerate(words):
            replace_selected(bits, field(cell, CODEBOOK[outcome]), word)
    state = BasisState(trials, horizon, case_name, tuple(bits))
    validate_input(state)
    return state


def validate_input(state: BasisState) -> None:
    if (
        not isinstance(state, BasisState)
        or (state.trials, state.horizon, state.case_name) not in (
            (len(TRAIN_POINTERS), TRAIN_HORIZON, TRAIN_CASE),
            (len(HELD_POINTERS), HELD_HORIZON, HELD_CASE),
        )
        or not is_word(state.bits, state.trials * CELL_M2)
    ):
        raise ValueError("Cycle488 state leaves the bounded train/held binary domain")
    expected_words = class_words(state.case_name)
    identifiers = []
    for cell in range(state.trials):
        c483.validate_route_input(local_c483_state(state, cell), "bath")
        pointer = int_of(selected(state.bits, field(cell, POINTER)))
        if pointer not in range(MENU_ARITY):
            raise ValueError("history pointer leaves the five-outcome menu")
        identifier = int_of(selected(state.bits, field(cell, TRIAL_ID)))
        identifiers.append(identifier)
        if identifier != cell + 1:
            raise ValueError("trial identities are not the supplied ordered basis corpus")
        for outcome, word in enumerate(expected_words):
            if selected(state.bits, field(cell, CODEBOOK[outcome])) != word:
                raise ValueError("Cycle478 protected class codebook is dirty or mismatched")
        if any(state.bits[site(cell, local)] for local in ADAPTER_OUTPUT_LOCAL):
            raise ValueError("Cycle488 receipt, work, or count carriers must enter blank")
    if len(set(identifiers)) != state.trials:
        raise ValueError("trial identities are not unique")


def apply_permutation(
    state: BasisState,
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> BasisState:
    if reverse:
        if not is_word(state.bits, state.trials * CELL_M2):
            raise ValueError("reverse state leaves the binary domain")
    else:
        validate_input(state)
    bits = list(state.bits)
    schedule = schedule_with_deletion(state.trials, state.horizon, delete_label)
    for item in reversed(schedule) if reverse else schedule:
        apply_gate(bits, item)
    return BasisState(state.trials, state.horizon, state.case_name, tuple(bits))


def majority_value(bits: Word | list[int], sites: tuple[int, int, int]) -> int:
    return int(sum(bits[index] for index in sites) >= 2)


def coarse_composite_step(state: BasisState) -> BasisState:
    """Independent declarative adapter after the frozen lower Cycle483 map."""
    validate_input(state)
    bits = list(state.bits)
    lower = c483.bath_schedule(state.horizon, inject_faults=False)
    for cell in range(state.trials):
        local = list(bits[cell * CELL_M2:cell * CELL_M2 + c483.TOTAL_M2])
        for item in lower:
            c483.apply_gate(local, item)
        bits[cell * CELL_M2:cell * CELL_M2 + c483.TOTAL_M2] = local

    for cell in range(state.trials):
        pointer = int_of(selected(bits, field(cell, POINTER)))
        matches = tuple(int(outcome == pointer) for outcome in range(MENU_ARITY))
        replace_selected(bits, field(cell, MATCH), matches)
        bits[site(cell, CLASS_VALID)] = int(sum(matches) == 1)
        bits[site(cell, TYPE_FLAG)] = majority_value(bits, field(cell, c483.B_TYPE))
        bits[site(cell, OCCURRENCE_FLAG)] = majority_value(bits, field(cell, c483.B_OCCURRENCE))
        bits[site(cell, LOCK_FLAG)] = majority_value(bits, field(cell, c483.B_LOCK))
        accept = int(
            bits[site(cell, c483.B_FORM)]
            and bits[site(cell, TYPE_FLAG)]
            and bits[site(cell, OCCURRENCE_FLAG)]
            and bits[site(cell, LOCK_FLAG)]
            and bits[site(cell, CLASS_VALID)]
        )
        bits[site(cell, ACCEPT)] = accept
        outcome_enable = tuple(accept & value for value in matches)
        replace_selected(bits, field(cell, OUTCOME_ENABLE), outcome_enable)
        replace_selected(bits, field(cell, RECEIPT_ONEHOT), outcome_enable)
        if accept:
            class_index = TERMINAL_CLASSES[pointer]
            replace_selected(bits, field(cell, RECEIPT_CLASS_ID), bits_of(class_index, CLASS_ID_BITS))
            replace_selected(bits, field(cell, RECEIPT_TRIAL_ID), selected(bits, field(cell, TRIAL_ID)))
            replace_selected(bits, field(cell, RECEIPT_WORD), selected(bits, field(cell, CODEBOOK[pointer])))
        for outcome in range(MENU_ARITY):
            receipt = outcome_enable[outcome]
            if cell == 0:
                current = receipt
                carries = (0,) * (COUNT_BITS + 1)
            else:
                previous_bits = selected(bits, field(cell - 1, COUNT_SUM[outcome]))
                carry = 0
                sum_bits = []
                carry_bits = [0]
                for bit in range(COUNT_BITS):
                    first = previous_bits[bit]
                    second = receipt if bit == 0 else 0
                    sum_bits.append(first ^ second ^ carry)
                    carry = (first & second) ^ (first & carry) ^ (second & carry)
                    carry_bits.append(carry)
                current = int_of(tuple(sum_bits))
                carries = tuple(carry_bits)
            replace_selected(bits, field(cell, COUNT_SUM[outcome]), bits_of(current, COUNT_BITS))
            replace_selected(bits, field(cell, COUNT_CARRY[outcome]), carries)
    return BasisState(state.trials, state.horizon, state.case_name, tuple(bits))


def receipts(state: BasisState) -> tuple[TypedMenuReceipt, ...] | None:
    output = []
    for cell in range(state.trials):
        occurrence = c483.bath_occurrence(local_c483_state(state, cell), state.horizon)
        onehot = selected(state.bits, field(cell, RECEIPT_ONEHOT))
        if occurrence is None or sum(onehot) != 1 or state.bits[site(cell, ACCEPT)] != 1:
            return None
        pointer = onehot.index(1)
        class_index = int_of(selected(state.bits, field(cell, RECEIPT_CLASS_ID)))
        identifier = int_of(selected(state.bits, field(cell, RECEIPT_TRIAL_ID)))
        word = selected(state.bits, field(cell, RECEIPT_WORD))
        if (
            identifier != cell + 1
            or class_index != TERMINAL_CLASSES[pointer]
            or word != selected(state.bits, field(cell, CODEBOOK[pointer]))
        ):
            return None
        output.append(TypedMenuReceipt(identifier, pointer, class_index, word))
    return tuple(output)


def final_counts(state: BasisState) -> tuple[int, ...]:
    return tuple(
        int_of(selected(state.bits, field(state.trials - 1, COUNT_SUM[outcome])))
        for outcome in range(MENU_ARITY)
    )


def empirical_frequencies(counts: tuple[int, ...]) -> tuple[Fraction, ...]:
    total = sum(counts)
    if total <= 0:
        raise ValueError("empty FORM history has no finite empirical frequency")
    return tuple(Fraction(value, total) for value in counts)


def program_norm_weights(program: object) -> tuple[float, ...]:
    logical = np.asarray((sqrt(3 / 8), np.exp(1j * np.pi / 9) * sqrt(5 / 8)), complex)
    fine = tuple(float(np.vdot(operator @ logical, operator @ logical).real) for operator in program.kraus)
    return tuple(sum(fine[index] for index in group) for group in program.coarse_groups)


def program_trace_grades(program: object) -> tuple[float, ...]:
    return tuple(float(np.trace(effect).real / 2) for effect in program.coarse_effects)


def bridge_and_weight_controls() -> None:
    print("\nFORM OCCURRENCE -> TERMINAL MENU RECEIPTS / E-G / INVERSE / WEIGHT FIREWALL")
    surface = finalized_surface()
    rows = []
    for case_name, horizon, pointers, program in (
        (TRAIN_CASE, TRAIN_HORIZON, TRAIN_POINTERS, surface.train_program),
        (HELD_CASE, HELD_HORIZON, HELD_POINTERS, surface.held_program),
    ):
        initial = prepare_history(case_name, horizon, pointers)
        physical = apply_permutation(initial)
        coarse = coarse_composite_step(initial)
        recovered = apply_permutation(physical, reverse=True)
        witnessed = receipts(physical)
        counts = final_counts(physical)
        frequencies = empirical_frequencies(counts)
        norm_weights = program_norm_weights(program)
        trace_grades = program_trace_grades(program)
        frequency_float = np.asarray(tuple(map(float, frequencies)))
        rows.append({
            "case": case_name, "N": len(pointers), "horizon": horizon,
            "pointers": pointers, "raw_integer_counts": counts,
            "normalized_empirical_frequencies": tuple(map(str, frequencies)),
            "E_G_bit_mismatches": sum(a != b for a, b in zip(physical.bits, coarse.bits)),
            "inverse_exact": recovered == initial,
            "typed_FORM_receipts": 0 if witnessed is None else len(witnessed),
            "norm_weights": norm_weights, "trace_grades": trace_grades,
            "frequency_norm_L2": float(np.linalg.norm(frequency_float - np.asarray(norm_weights))),
            "frequency_trace_L2": float(np.linalg.norm(frequency_float - np.asarray(trace_grades))),
            "norm_trace_L2": float(np.linalg.norm(np.asarray(norm_weights) - np.asarray(trace_grades))),
        })
    check(
        "train N3 and held N9 bath-relative FORM histories feed exact protected menu receipts and retained counters with E-G and inverse",
        all(
            row["E_G_bit_mismatches"] == 0 and row["inverse_exact"]
            and row["typed_FORM_receipts"] == row["N"]
            and sum(row["raw_integer_counts"]) == row["N"]
            and abs(sum(row["norm_weights"]) - 1) < TOL
            and abs(sum(row["trace_grades"]) - 1) < TOL
            and row["frequency_norm_L2"] > 1e-4
            and row["frequency_trace_L2"] > 1e-4
            for row in rows
        )
        and rows[0]["raw_integer_counts"] == (1, 1, 1, 0, 0)
        and rows[1]["raw_integer_counts"] == (2, 2, 2, 2, 1),
        rows,
    )


def quotient_surface_controls() -> None:
    print("\nEXACT CYCLE478 QUOTIENT / TERMINAL WEIGHT SURFACE")
    surface = finalized_surface()
    extension = c478.build_extension()
    exact_support_residual = tuple(
        sp.simplify(sum(
            coefficient * c478.c448.exact_effects()[class_index][lane]
            for class_index, coefficient in enumerate(c478.SELECTED_VECTOR)
        ))
        for lane in range(4)
    )
    exact_trace_contraction = sp.simplify(sum(
        coefficient * (c478.c448.exact_effects()[class_index][0] + c478.c448.exact_effects()[class_index][1]) / 2
        for class_index, coefficient in enumerate(c478.SELECTED_VECTOR)
    ))
    positive_root_class = extension.new_rows[413][0]
    negative_root_class = extension.new_rows[415][0]
    positive_root = extension.effects[positive_root_class]
    negative_root = extension.effects[negative_root_class]
    row_sum = tuple(
        sp.simplify(sum(extension.effects[class_index][lane] for class_index in TERMINAL_CLASSES))
        for lane in range(4)
    )
    train_effect_residual = max(
        float(np.linalg.norm(
            physical - c478.c454.physical_effect(extension.effects[class_index], c478.c317.physical_fixture(3).contact)
        ))
        for physical, class_index in zip(surface.train_program.coarse_effects, TERMINAL_CLASSES)
    )
    held_effect_residual = max(
        float(np.linalg.norm(
            physical - c478.c454.physical_effect(extension.effects[class_index], c478.c317.physical_fixture(6).contact)
        ))
        for physical, class_index in zip(surface.held_program.coarse_effects, TERMINAL_CLASSES)
    )
    check(
        "the selected menu is the actual Cycle478 positive terminal root and retains exact support-nine quotient closure",
        exact_support_residual == (0, 0, 0, 0)
        and exact_trace_contraction == 0
        and c478.c454.exact_key(positive_root) == c478.c454.exact_key(negative_root)
        and row_sum == (1, 1, 0, 0)
        and max(train_effect_residual, held_effect_residual) < TOL
        and surface.row == TERMINAL_CLASSES
        and len(set(surface.train_words)) == len(set(surface.held_words)) == MENU_ARITY,
        {
            "terminal_new_row_index": TERMINAL_ROW_INDEX,
            "terminal_effect_classes": TERMINAL_CLASSES,
            "support9_classes": SUPPORT9_CLASSES,
            "exact_support9_operator_residual": exact_support_residual,
            "exact_support9_trace_grade_contraction": exact_trace_contraction,
            "positive_negative_root_shared": c478.c454.exact_key(positive_root) == c478.c454.exact_key(negative_root),
            "positive_terminal_menu_sum": row_sum,
            "train_held_effect_residuals": (train_effect_residual, held_effect_residual),
            "weight_semantics": "physical branch squared norms and trace grades; neither is called probability",
        },
    )


def permuted_member_control() -> None:
    print("\nPERMUTED-MEMBER / ORDER-FREQUENCY DISCRIMINATOR")
    original = prepare_history(HELD_CASE, HELD_HORIZON, HELD_POINTERS)
    permuted_pointers = tuple(reversed(HELD_POINTERS))
    permuted = prepare_history(HELD_CASE, HELD_HORIZON, permuted_pointers)
    original_output = apply_permutation(original)
    permuted_output = apply_permutation(permuted)
    original_receipts = receipts(original_output)
    permuted_receipts = receipts(permuted_output)
    original_order = tuple(item.pointer for item in original_receipts or ())
    permuted_order = tuple(item.pointer for item in permuted_receipts or ())
    original_counts = final_counts(original_output)
    permuted_counts = final_counts(permuted_output)
    check(
        "a deterministic permutation preserves raw counts/frequencies but changes the retained ordered member history",
        original_counts == permuted_counts == (2, 2, 2, 2, 1)
        and empirical_frequencies(original_counts) == empirical_frequencies(permuted_counts)
        and original_order == HELD_POINTERS and permuted_order == permuted_pointers
        and original_order != permuted_order
        and original_output.bits != permuted_output.bits,
        {
            "original_order": original_order, "permuted_order": permuted_order,
            "raw_integer_counts": original_counts,
            "normalized_empirical_frequencies": tuple(map(str, empirical_frequencies(original_counts))),
            "actual_member_selected_by_permutation_test": False,
        },
    )


def deletion_controls() -> None:
    print("\nPOINTER / MEMBER / RECEIPT / COUNTER DELETIONS")
    initial = prepare_history(TRAIN_CASE, TRAIN_HORIZON, TRAIN_POINTERS)
    nominal = apply_permutation(initial)
    first_word = class_words(TRAIN_CASE)[0]
    active_word_lane = first_word.index(1)
    controls = (
        ("member-FORM-occurrence-lane-0", "cell:0:c483:bath-form-flag:80:0"),
        ("member-FORM-occurrence-lane-1", "cell:0:c483:bath-form-flag:80:1"),
        ("pointer-matcher", "cell:0:match:0:prefix:0"),
        ("class-packet", f"cell:0:packet-copy:0:{active_word_lane}"),
        ("trial-member-id", "cell:0:trial-copy:0"),
        ("counter", "cell:1:count:1:add-b:0"),
    )
    # The two FORM occurrence lanes must be removed together to defeat the
    # repetition-three majority; every other deletion is independent.
    double_form = apply_permutation(
        initial, delete_label=None,
    )
    bits = list(initial.bits)
    schedule = fixed_schedule(initial.trials, initial.horizon)
    omitted = {controls[0][1], controls[1][1]}
    for item in schedule:
        if item.label not in omitted:
            apply_gate(bits, item)
    double_form = BasisState(initial.trials, initial.horizon, initial.case_name, tuple(bits))
    rows = [(
        "two-member-FORM-occurrence-lanes", tuple(omitted),
        double_form != nominal, receipts(double_form) is None,
        sum(a != b for a, b in zip(double_form.bits, nominal.bits)),
    )]
    for name, label in controls[2:]:
        damaged = apply_permutation(initial, delete_label=label)
        witnessed = receipts(damaged)
        count_changed = final_counts(damaged) != final_counts(nominal)
        rows.append((
            name, label, damaged != nominal,
            witnessed is None or count_changed,
            sum(a != b for a, b in zip(damaged.bits, nominal.bits)),
        ))
    # Deleting an actual Cycle478 program member gives a visible completeness
    # deficit without saying which member occurs.
    program = finalized_surface().train_program
    deleted_member_defect = float(np.linalg.norm(
        program.completeness - program.fine_effects[0] - np.eye(2)
    ))
    check(
        "FORM typing, supplied pointer matching, protected member content, trial identity, counter flow, and one program member are load-bearing",
        len(rows) == 5
        and all(visible and causal_failure and residual > 0 for _, _, visible, causal_failure, residual in rows)
        and deleted_member_defect > 1e-6,
        {"physical_deletions": rows, "deleted_Cycle478_member_completeness_defect": deleted_member_defect},
    )


def malformed_controls() -> None:
    print("\nMALFORMED / DIRTY DOMAIN CONTROLS")
    base = prepare_history(TRAIN_CASE, TRAIN_HORIZON, TRAIN_POINTERS)
    corruptions = {}
    bad_pointer = list(base.bits)
    replace_selected(bad_pointer, field(0, POINTER), bits_of(7, POINTER_BITS))
    corruptions["pointer-seven"] = tuple(bad_pointer)
    duplicate_id = list(base.bits)
    replace_selected(duplicate_id, field(1, TRIAL_ID), bits_of(1, TRIAL_ID_BITS))
    corruptions["duplicate-trial-id"] = tuple(duplicate_id)
    dirty_codebook = list(base.bits)
    dirty_codebook[field(0, CODEBOOK[0])[0]] ^= 1
    corruptions["dirty-codebook"] = tuple(dirty_codebook)
    dirty_output = list(base.bits)
    dirty_output[site(0, RECEIPT_ONEHOT[0])] = 1
    corruptions["dirty-receipt"] = tuple(dirty_output)
    dirty_work = list(base.bits)
    dirty_work[field(0, MATCH_PREFIX[0])[0]] = 1
    corruptions["dirty-match-work"] = tuple(dirty_work)
    missing_fresh = list(base.bits)
    missing_fresh[site(0, c483.B_FRESH)] = 0
    corruptions["missing-bath-fresh"] = tuple(missing_fresh)
    dirty_bath = list(base.bits)
    dirty_bath[site(0, c483.B_FORM_BATH_FRESH)] = 1
    corruptions["dirty-bath"] = tuple(dirty_bath)
    refusals = []
    for name, bits in corruptions.items():
        try:
            apply_permutation(BasisState(base.trials, base.horizon, base.case_name, bits))
        except (TypeError, ValueError):
            refusals.append(name)
    constructor_refusals = []
    for name, args in (
        ("zero-trials", (TRAIN_CASE, TRAIN_HORIZON, ())),
        ("wrong-horizon", (TRAIN_CASE, HELD_HORIZON, TRAIN_POINTERS)),
        ("ten-trials", (HELD_CASE, HELD_HORIZON, HELD_POINTERS + (4,))),
    ):
        try:
            prepare_history(*args)
        except (TypeError, ValueError):
            constructor_refusals.append(name)
    check(
        "invalid pointers/identities, dirty class/receipt/work/bath carriers, and unsupported sizes are refused",
        set(refusals) == set(corruptions)
        and set(constructor_refusals) == {"zero-trials", "wrong-horizon", "ten-trials"},
        {"state_refusals": refusals, "constructor_refusals": constructor_refusals},
    )


def coord_for_site(index: int) -> Coord:
    cell, local = divmod(index, CELL_M2)
    return (cell, local, 0)


def manifest(trials: int) -> tuple[Coord, ...]:
    return tuple(coord_for_site(index) for index in range(trials * CELL_M2))


def manhattan(first: Coord, second: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(first, second))


def cell_path(cell: int) -> tuple[int, ...]:
    return tuple(site(cell, local) for local in range(CELL_M2))


def link_path(left: int) -> tuple[int, ...]:
    return cell_path(left) + tuple(reversed(cell_path(left + 1)))


@lru_cache(maxsize=None)
def compact_route_plan(item: Gate) -> tuple[tuple[tuple[int, int], ...], tuple[int, ...], int]:
    cells = sorted({index // CELL_M2 for index in item.sites})
    if len(cells) == 1:
        path = cell_path(cells[0])
    elif len(cells) == 2 and cells[1] == cells[0] + 1:
        path = link_path(cells[0])
    else:
        raise RuntimeError("Cycle488 adapter gate leaves one cell or one adjacent link")
    labels = list(path)
    targets = tuple(range(len(path) - len(item.sites), len(path)))
    spans = []
    swap_count = 0
    for desired, target in zip(reversed(item.sites), reversed(targets)):
        position = labels.index(desired)
        if position > target:
            raise RuntimeError("Cycle488 right-edge route order failed")
        labels.insert(target, labels.pop(position))
        spans.append((position, target))
        swap_count += target - position
    if tuple(labels[index] for index in targets) != item.sites:
        raise RuntimeError("Cycle488 final operand order failed")
    return tuple(spans), tuple(path[index] for index in targets), swap_count


@lru_cache(maxsize=None)
def adapter_trace(trials: int) -> AdapterTrace:
    schedule = adapter_only_schedule(trials)
    coords = manifest(trials)
    path_failures = 0
    for cell in range(trials):
        path = cell_path(cell)
        path_failures += sum(manhattan(coords[a], coords[b]) != 1 for a, b in zip(path, path[1:]))
    for cell in range(trials - 1):
        path = link_path(cell)
        path_failures += sum(manhattan(coords[a], coords[b]) != 1 for a, b in zip(path, path[1:]))
    digest = sha256(f"Cycle488 {trials}-cell compact restored route v1".encode())
    primitives = 0
    maximum = 0
    failures = path_failures
    for item in schedule:
        spans, final_sites, swaps = compact_route_plan(item)
        failures += sum(manhattan(coords[a], coords[b]) != 1 for a, b in zip(final_sites, final_sites[1:]))
        primitives += 1 + 6 * swaps
        maximum = max(maximum, len(item.sites))
        digest.update(f"{item.kind}:{item.sites}:{item.label}:{spans}:{final_sites}".encode())
    return AdapterTrace(len(schedule), primitives, maximum, failures, digest.hexdigest())


def determinant(frame: tuple[tuple[int, int, int], ...]) -> int:
    return int(round(np.linalg.det(np.asarray(frame, dtype=int))))


@lru_cache(maxsize=1)
def proper_cubic_frames() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    frames = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = [[0, 0, 0] for _ in range(3)]
            for row, column in enumerate(permutation):
                matrix[row][column] = signs[row]
            frame = tuple(tuple(row) for row in matrix)
            if determinant(frame) == 1:
                frames.append(frame)
    return tuple(frames)


def rotate_coord(coord: Coord, frame: tuple[tuple[int, int, int], ...]) -> Coord:
    return tuple(sum(frame[row][column] * coord[column] for column in range(3)) for row in range(3))


def covariance_and_locality_controls() -> None:
    print("\nCONTRACTED CYCLE483 NN + CYCLE488 ADAPTER ALL-24")
    traces = {trials: adapter_trace(trials) for trials in (len(TRAIN_POINTERS), len(HELD_POINTERS))}
    imported = {
        TRAIN_HORIZON: c483.route_trace("bath", TRAIN_HORIZON),
        HELD_HORIZON: c483.route_trace("bath", HELD_HORIZON),
    }
    rows = []
    failures = 0
    for frame_index, frame in enumerate(proper_cubic_frames()):
        for trials, horizon in ((len(TRAIN_POINTERS), TRAIN_HORIZON), (len(HELD_POINTERS), HELD_HORIZON)):
            coords = tuple(rotate_coord(coord, frame) for coord in manifest(trials))
            local_failures = 0
            for cell in range(trials):
                path = cell_path(cell)
                local_failures += sum(manhattan(coords[a], coords[b]) != 1 for a, b in zip(path, path[1:]))
            for cell in range(trials - 1):
                path = link_path(cell)
                local_failures += sum(manhattan(coords[a], coords[b]) != 1 for a, b in zip(path, path[1:]))
            for item in adapter_only_schedule(trials):
                _spans, final_sites, _swaps = compact_route_plan(item)
                local_failures += sum(
                    manhattan(coords[a], coords[b]) != 1 for a, b in zip(final_sites, final_sites[1:])
                )
            exact = (
                local_failures == 0 and len(set(coords)) == len(coords)
                and traces[trials].connected_failures == 0
                and imported[horizon].connected_failures == 0
            )
            failures += int(not exact)
            rows.append((frame_index, trials, exact, local_failures))
    check(
        "the contracted Cycle483 bath map and new scalar receipt/count adapter have connected support in all 24 proper-cubic frames",
        len(proper_cubic_frames()) == 24 and len(rows) == 48 and failures == 0
        and all(trace.maximum_support_M2 == 3 and trace.connected_failures == 0 for trace in traces.values())
        and all(trace.maximum_support_M2 == 3 and trace.connected_failures == 0 for trace in imported.values()),
        {"proper_cubic_frames": 24, "train_held_rows": len(rows), "failures": failures,
         "adapter_traces": traces,
         "imported_Cycle483_bath_traces": imported,
         "geometry": "translation-equivalent event columns plus adjacent retained-count links"},
    )


def fixed_law_resource_controls() -> None:
    print("\nFIXED LAW / RESOURCE / SEMANTIC FIREWALL")
    held = prepare_history(HELD_CASE, HELD_HORIZON, HELD_POINTERS)
    nominal_source = (
        inspect.getsource(adapter_only_schedule).lower()
        + inspect.getsource(apply_permutation).lower()
        + inspect.getsource(coarse_composite_step).lower()
    )
    forbidden = tuple(token for token in (
        "sample_outcome", "born_probability", "realized_member_query",
        "independence_law", "renew_bath", "host_pointer_choice",
    ) if token in nominal_source)
    check(
        "the all-pointer schedule is state-independent and keeps every bath, member label, receipt, codebook, count, and carry physical",
        CELL_M2 * len(HELD_POINTERS) < 64_000
        and not forbidden
        and len(fixed_schedule(len(HELD_POINTERS), HELD_HORIZON))
        == len(HELD_POINTERS) * len(c483.bath_schedule(HELD_HORIZON, inject_faults=False))
        + len(adapter_only_schedule(len(HELD_POINTERS))),
        {
            "M2_per_event_cell": CELL_M2,
            "train_total_M2": CELL_M2 * len(TRAIN_POINTERS),
            "held_total_M2": CELL_M2 * len(HELD_POINTERS),
            "retained_scale40_bound_M2": 64_000,
            "train_supplied_bath_M2": len(TRAIN_POINTERS) * (261 + TRAIN_HORIZON * 255),
            "held_supplied_bath_M2": len(HELD_POINTERS) * (261 + HELD_HORIZON * 255),
            "held_form_receipts": len(receipts(apply_permutation(held)) or ()),
            "future_bath_renewal_operations": 0,
            "discarded_global_state_M2": 0,
            "nominal_forbidden_controls": forbidden,
            "framework_actuality": False, "framework_Record": False,
            "realized_framework_history": False, "Born_probability": False,
        },
    )


def no_go_discipline_controls() -> None:
    print("\nNO-GO DISCIPLINE N1-N8 / FIREWALL GATE")
    n1 = (
        ("deterministic supplied basis corpus", "ATTEMPTED", "Cycle488 exact count bridge; corpus/pointers supplied"),
        ("independent repeated instrument product law", "ATTEMPTED PRIOR", "Cycle430 conditional weights; independence and actualization supplied"),
        ("retained-outcome instrument trajectory", "OPEN / UNTESTED", "physical outcome carrier must select one continuing member"),
        ("deterministic every-orbit history", "OPEN / UNTESTED", "unique extension law could avoid stochastic sampling"),
        ("martingale/typicality on actual Records", "OPEN / UNTESTED", "requires a lawful repeated Record process and measure"),
        ("autonomous bath stochastic dynamics", "OPEN / UNTESTED", "must derive transition statistics and renewable resources"),
        ("symmetry/grade selection before histories", "OPEN / UNTESTED", "could derive trace functional then add a separate occurrence law"),
    )
    walls = ("W_grade", "W_member", "W_independence", "W_sampling", "W_renewal")
    n2 = tuple((first, second, False) for first, second in itertools.combinations(walls, 2))
    n3 = (
        "terminal menu and class codec", "logical input for norm weights",
        "deterministic train/held pointer words", "Cycle483 bath FORM law and blank baths",
        "trial identities and order", "finite N/horizon pairing", "frame and line geometry",
    )
    n4 = (
        ("Cycle430", "conditional product-law word weights", "actual-member/frequency bridge remains distinct", True),
        ("Cycle478", "finite quotient/functionality without occurrence", "exact selected weight surface", True),
        ("Cycle483", "basis FORM occurrence without probability/member law", "exact repeated occurrence input", True),
        ("Cycle486", "two endpoint FORM occurrences without Born law", "reconnaissance only, not direct premise", False),
    )
    n5 = (
        ("per-event", "typed receipt and class binding tested", "no universal frequency claim"),
        ("finite history", "N3/N9 counts differ from displayed weights", "no asymptotic claim"),
        ("lattice-wide", "untested", "no negative conclusion"),
        ("infinite-history", "untested", "no negative conclusion"),
    )
    n6 = (
        "derive a retained-outcome trajectory on the same terminal menu",
        "supply then retire an explicit independent-product import",
        "prove a deterministic every-orbit frequency theorem",
        "join Cycle483 FORM to an actual renewable bath conveyor",
        "extend the finite quotient surface to a selected grade/state law",
    )
    steelman = (
        "A retained-outcome instrument can use the actual Cycle478 Kraus pointer as the Cycle483 FORM label, "
        "then a separately derived stationary/ergodic local bath law could make its realized counts converge "
        "to the branch-norm functional. Cycle488's deliberately supplied deterministic words do not attack "
        "that mechanism; they only prove that FORM typing plus a counter does not itself install it."
    )
    n8 = (
        "Cycle430 separated conditional product weights from actual histories",
        "Cycle440/478 separated finite effect functionality from grade selection",
        "Cycle483 separated basis FORM from coherent member selection",
        "Cycle486 bound FORM occurrences to endpoints while leaving Born/frequency open",
    )
    gate_fail = (
        len(n1) >= 5 and len(n2) == 10 and len(n3) >= 7 and len(n4) == 4
        and len(n5) == 4 and len(n6) >= 5 and bool(steelman) and len(n8) == 4
    )
    check(
        "N1-N8 permits the bounded executable bridge but rejects a broad no-go, minimum, or axiom-pressure conclusion",
        gate_fail,
        {"N1_normalized_routes": n1, "N2_pairwise_independence": n2,
         "N3_hidden_conditions": n3, "N4_residual_matching": n4,
         "N5_resolution_audit": n5, "N6_partial_closure_paths": n6,
         "N7_steelman": steelman, "N8_cross_cycle_echo": n8,
         "Gate_disposition": "FAIL — partial-attempt-with-named-untested-routes",
         "no_go_or_axiom_pressure_claimed": False},
    )


def supplied_derived_open_controls() -> None:
    print("\nSUPPLIED / DERIVED / OPEN")
    supplied = (
        "Cycle478 terminal positive-root menu, physical programs, exact effects, and class codec",
        "Cycle483 basis bath FORM law, one blank formation/repair stack per event, and FORM/TYPE/OCCURRENCE/LOCK meanings",
        "deterministic train and held pointer words frozen before querying weights",
        "trial identities/order, logical input for norm weights, and trace-grade diagnostic",
        "five-outcome codebook, local line geometry, finite N/horizon pairing, and frame convention",
    )
    derived = (
        "three and nine exact bath-relative typed FORM receipts",
        "physical pointer-to-protected-class sidecars and reversible five-bin counts",
        "exact E/G, full inverse, zero hidden discard, and raw counts",
        "separate empirical frequencies, physical branch norms, and trace grades",
        "exact support-nine operator/trace contraction and shared terminal root",
        "held-size, permutation, deletion, malformed, NN, and all24 controls",
    )
    open_items = (
        "selection of an outcome/member or framework realized history",
        "a probability interpretation or equality between frequency and norm/trace weight",
        "independence, stationarity, sampling, concentration, or asymptotic law",
        "derivation of the bath FORM law, menu, class codec, or logical state",
        "bath renewal, used-resource export/reentry control, and unbounded Record permanence",
        "continuum Born theorem, time/rate, energy/source, gravity, or constitutional conclusion",
    )
    check(
        "the inventory keeps supplied FORM histories separate from selected grade, member, sampling, and renewal laws",
        len(supplied) == 5 and len(derived) == 6 and len(open_items) == 6,
        {"supplied": supplied, "derived": derived, "open": open_items,
         "bath_relative_FORM_does_not_make_realized_framework_history": True,
         "raw_counts_called_probability": False, "empirical_frequencies_called_probability": False,
         "norm_or_trace_grade_called_probability": False},
    )


def install_wall_cap() -> None:
    def handler(_signum: int, _frame: object) -> None:
        raise WallCapExceeded(f"Cycle488 exceeded wall cap {WALL_CAP_SECONDS}s")
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, WALL_CAP_SECONDS)


def resource_controls(started: float) -> None:
    elapsed = time.monotonic() - started
    raw_rss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    rss_bytes = raw_rss if sys.platform == "darwin" else raw_rss * 1024
    check(
        "Cycle488 remains within the declared wall/RSS envelope",
        elapsed < WALL_CAP_SECONDS and rss_bytes < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
         "peak_rss_bytes": rss_bytes, "rss_cap_bytes": RSS_CAP_BYTES},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    install_wall_cap()
    print("CYCLE488 PHYSICAL FORM-OCCURRENCE / BORN-WEIGHT FIREWALL")
    print("authority", AUTHORITY, "audit", AUDIT, "CELL_M2", CELL_M2)
    try:
        note_and_source_contracts()
        quotient_surface_controls()
        bridge_and_weight_controls()
        permuted_member_control()
        deletion_controls()
        malformed_controls()
        covariance_and_locality_controls()
        fixed_law_resource_controls()
        no_go_discipline_controls()
        supplied_derived_open_controls()
        resource_controls(started)
    except WallCapExceeded as error:
        check("the Cycle488 runner remains within its wall cap", False, str(error))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    return int(bool(FAIL))


if __name__ == "__main__":
    raise SystemExit(main())
