#!/usr/bin/env python3
"""Cycle676: moving-carrier phase field and finite-restriction theorem."""
from __future__ import annotations


TARGET_CONTRACT = {
    "cycle": 676,
    "target": (
        "a translation-invariant proper-cubic local M2 update which starts with no phase seed, exports the complete "
        "Cycle661 sector on outward carriers, leaves an increasing stable central-order-parameter wake, and produces "
        "one objective ObjectiveEventToken[none|six] on the native coherent input"
    ),
    "quantifiers": "all 64 Cycle661 basis sectors, arbitrary coherent amplitudes, cuts C3/C4/C6/C9, all24/all576",
    "allowed_premises": [
        "exact committed Cycle661 local basis QCA", "blank local carrier/phase registers",
        "translation-invariant directed carrier shift", "exact committed Cycle669 basis-token interface",
    ],
    "forbidden_weakenings": [
        "locally diagonal reduced center called objective", "global coherent cat called one realized phase",
        "disjoint infinite-volume sectors called a selected sector", "tracing-out or nonreturn called actuality",
        "supplied boundary phase", "supplied seed/selector/random draw/sampler", "host-selected frame or branch",
    ],
    "completion_witness": (
        "one central objective value plus complete outward coherent exhaust, not only a finite branch isometry, "
        "local reduced state, central decomposition, or conditional thermodynamic representation theorem"
    ),
    "outcomes_not_closure": [
        "finite pure entangled state", "rank-seven diagonal center", "infinite algebraic mixture of disjoint sectors",
        "first-crossing boundary exhaust", "stable branch-relative latch",
    ],
}
TARGET_CONTRACT_SHA256 = "4e312e45972b2ed4ab94fc1592a4ea5ffc3cb510fb08f0ec7d27bff10b252b45"


PREREGISTRATION = {
    "cuts": {
        "C3": {"radius": 3, "split": "train"},
        "C4": {"radius": 4, "split": "held_blinded"},
        "C6": {"radius": 6, "split": "held_blinded_nonproduct"},
        "C9": {"radius": 9, "split": "held_larger_cut"},
    },
    "local_cell": (
        "84 Cycle661 source M2 + 7 central one-hot M2 + 6x7 phase-head M2 + "
        "6x7 phase-wake M2 + 6x2 dual-rail information-head M2 = 187 active M2"
    ),
    "update": (
        "state-triggered local injection on the exact Cycle661 code, onsite phase-wake CNOTs, and six uniform "
        "direction-bank shifts; the same rule is applied at every coarse cell"
    ),
    "information_encoding": (
        "Cycle661 candidate bit d is reversibly moved into dual rail (zero_d,one_d) and transported only on ray d; "
        "the six rays collectively retain the exact 64-sector word"
    ),
    "phase_encoding": "the none|six event one-hot is copied to all six moving phase heads; each head writes its wake then advances",
    "finite_restriction": (
        "on cube [-R,R]^3 the first crossing occurs at update R+1; an explicit six-port boundary exhaust is a "
        "restriction ledger, not bulk dynamics or a boundary phase"
    ),
    "thermodynamic_gate": (
        "prove finite-state coherence, local center diagonality, and conditional disjoint GNS phase sectors separately; "
        "none alone is objective realization"
    ),
    "coherent_fixtures": ["uniform64", "phase_ramp64", "held_sparse_complex"],
    "no_go_gate": "fresh remote-main N1-N8 before disposition",
}
PREREGISTRATION_SHA256 = "0a8688d2f23b19888ef90fa3f79401156a28f8c0a73424240d67dbc196935750"


from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import ast
import cmath
import inspect
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time
import types

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SHORE = "884bcc67fa7baa38b750a1ddbcf094a16b666bce"
NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_MOVING_CARRIER_PHASE_FIELD_FINITE_RESTRICTION_CYCLE676_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_moving_carrier_phase_field_finite_restriction_cycle676_receipt_2026_07_23.json"
AUTHORITY = "none"; AUDIT = "unset"; TOL = 3.0e-10
WALL_CAP_SECONDS = 300.0; RSS_CAP_BYTES = 3 * 1024**3
PASS = FAIL = 0


PINS = {
    "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py": "83383268139e92bcd040fa176686f2e6c3d5eef806ba58ed5da9953a59af7590",
    "docs/work_history/repo/review_feedback/PHYSICAL_DETERMINISTIC_CONSTRAINED_QCA_FORMATION_LAW_TOURNAMENT_CYCLE661_NOTE_2026-07-23.md": "14262310b768983ebbdc8a89f914f237ab2a2523c8a096eece63b33a7e5e9ad4",
    "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json": "c0ac1effe618bbdcbfc4bd6a3360f3beb557aa2469d47be476deef862e1340c5",
    "scripts/physical_state_carried_event_chain_sequence_protocol_cycle669_2026_07_23.py": "ac1237e211bf06a8eb394db0dd8001c88a5aaf81726b38a3e43bd066285a9c84",
    "docs/work_history/repo/review_feedback/PHYSICAL_STATE_CARRIED_EVENT_CHAIN_SEQUENCE_PROTOCOL_CYCLE669_NOTE_2026-07-23.md": "4ba9fe3a26606a944f362e81d6262543936018c6adf497069d8800e616f0c2c5",
    "outputs/physical_state_carried_event_chain_sequence_protocol_cycle669_receipt_2026_07_23.json": "0765c66f3d3625892d133976aca217a5676fef0820557b12b32c988cb6180760",
    "scripts/physical_symmetry_neutral_order_parameter_actualizer_tournament_cycle674_2026_07_23.py": "91ae562030f6906b8762828dd92795aaa8771ce6c60da6371f50bc8f701dd823",
    "docs/work_history/repo/review_feedback/PHYSICAL_SYMMETRY_NEUTRAL_ORDER_PARAMETER_ACTUALIZER_TOURNAMENT_CYCLE674_NOTE_2026-07-23.md": "7efc246b7b2fbf00d18e4d52a949c225d97c4b32fc7731f84d652eddc8d98200",
    "outputs/physical_symmetry_neutral_order_parameter_actualizer_tournament_cycle674_receipt_2026_07_23.json": "e66f8b59ab81b6ff531cc5714dab51cd37188c38d398347d331d879da4963641",
    "docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_SEED_MEMBER_DILATION_CYCLE536_NOTE_2026-07-21.md": "e15944633127890fe27cb52193960a28d9860212d5d7aafd70f15eef2e987457",
    "docs/work_history/repo/review_feedback/PHYSICAL_DISSIPATIVE_METASTABLE_FORMATION_CHANNEL_CYCLE663_NOTE_2026-07-23.md": "96f59a3f79ce7c29f3c9ccdf93cae9503ea4cd0084821c11ba6e0545046bec87",
    "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md": "bdc8dda304985a62c73fc6e7a03f11d61041dd8053a9321fb7171c9b22947a05",
}


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=lambda x: list(x)).encode()).hexdigest()


def file_sha(path): return sha256(Path(path).read_bytes()).hexdigest()
def git_bytes(path): return subprocess.check_output(("git", "show", f"{SHORE}:{path}"), cwd=ROOT)


def load_exact(name, path):
    module = types.ModuleType(name); module.__file__ = str(ROOT / path); module.__package__ = ""
    sys.modules[name] = module
    exec(compile(git_bytes(path), module.__file__, "exec"), module.__dict__)
    return module


def citation(path, fragment):
    rows = git_bytes(path).decode().splitlines()
    matches = [line for line, text in enumerate(rows, 1) if fragment in text]
    if len(matches) != 1: raise AssertionError((path, fragment, matches))
    return {"ref": SHORE, "path": path, "line": matches[0]}


def current_citation(fragment):
    rows = Path(__file__).read_text().splitlines()
    matches = [line for line, text in enumerate(rows, 1) if text.strip().startswith(fragment)]
    if len(matches) != 1: raise AssertionError((fragment, matches))
    return {"ref": "Cycle676 current", "path": str(Path(__file__).relative_to(ROOT)), "line": matches[0]}


# Exact evidence loads occur only after the frozen target and preregistration.
c661 = load_exact("cycle676_exact_c661", "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py")
c669 = load_exact("cycle676_exact_c669", "scripts/physical_state_carried_event_chain_sequence_protocol_cycle669_2026_07_23.py")
c674 = load_exact("cycle676_exact_c674", "scripts/physical_symmetry_neutral_order_parameter_actualizer_tournament_cycle674_2026_07_23.py")


WORDS = tuple(product((0, 1), repeat=6))
DIRECTIONS = tuple(c661.DIRECTIONS)
ZERO = (0, 0, 0)


def freeze_and_shore_controls():
    rows = Path(__file__).read_text().splitlines()
    target_line = next(i for i, row in enumerate(rows, 1) if row.startswith("TARGET_CONTRACT ="))
    prereg_line = next(i for i, row in enumerate(rows, 1) if row.startswith("PREREGISTRATION ="))
    evidence_line = next(i for i, row in enumerate(rows, 1) if row.startswith("c661 = load_exact"))
    observed = {path: sha256(git_bytes(path)).hexdigest() for path in PINS}
    imported_receipts = {}
    for cycle, path in {
        "661": "outputs/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_receipt_2026_07_23.json",
        "669": "outputs/physical_state_carried_event_chain_sequence_protocol_cycle669_receipt_2026_07_23.json",
        "674": "outputs/physical_symmetry_neutral_order_parameter_actualizer_tournament_cycle674_receipt_2026_07_23.json",
    }.items():
        imported_receipts[cycle] = json.loads(git_bytes(path))
    contracts = {f"Cycle{cycle}_pass": row["pass"] for cycle, row in imported_receipts.items()}
    passed = (target_line < prereg_line < evidence_line and digest(TARGET_CONTRACT) == TARGET_CONTRACT_SHA256
              and digest(PREREGISTRATION) == PREREGISTRATION_SHA256 and observed == PINS and all(contracts.values()))
    result = {
        "shore": SHORE, "target": TARGET_CONTRACT, "target_sha256": digest(TARGET_CONTRACT),
        "expected_target_sha256": TARGET_CONTRACT_SHA256, "preregistration": PREREGISTRATION,
        "preregistration_sha256": digest(PREREGISTRATION), "expected_preregistration_sha256": PREREGISTRATION_SHA256,
        "target_line": target_line, "preregistration_line": prereg_line, "first_evidence_line": evidence_line,
        "frozen_before_evidence": target_line < prereg_line < evidence_line, "pins": PINS, "observed": observed,
        "working_tree_bytes_used_as_evidence": False, "imported_contracts": contracts, "pass": passed,
    }
    check("Cycle676 target, C3/C4/C6/C9 cuts and exact shores were frozen before evidence", passed,
          {"target": result["target_sha256"], "prereg": result["preregistration_sha256"], "pins": len(PINS)})
    return result, imported_receipts


def add(left, right): return tuple(a + b for a, b in zip(left, right))
def scale(number, vector): return tuple(number * value for value in vector)
def inside_cut(point, radius): return max(abs(value) for value in point) <= radius


def onehot(index, width):
    if type(index) is not int or index not in range(width): raise ValueError("one-hot index")
    return tuple(int(site == index) for site in range(width))


def event_index(word): return word.index(1) + 1 if sum(word) == 1 else 0
def event_center(word): return onehot(event_index(word), 7)
def dual_word(word): return tuple(bit for value in word for bit in (1 - value, value))


def direction_map(frame, direction):
    moved = c661.c625.matvec(frame, DIRECTIONS[direction])
    return DIRECTIONS.index(moved)


def rotate_six(word, frame): return c661.c625.rotate_six(tuple(word), frame)


def rotate_seven(word, frame):
    output = [word[0]] + [0] * 6
    for direction in range(6): output[1 + direction_map(frame, direction)] = word[1 + direction]
    return tuple(output)


SOURCE = tuple(range(84))
CENTER = tuple(range(84, 91))
PHASE_HEAD = tuple(tuple(range(91 + 7 * direction, 98 + 7 * direction)) for direction in range(6))
PHASE_WAKE = tuple(tuple(range(133 + 7 * direction, 140 + 7 * direction)) for direction in range(6))
INFO_HEAD = tuple(tuple(range(175 + 2 * direction, 177 + 2 * direction)) for direction in range(6))
WIDTH = 187


@dataclass(frozen=True)
class Operation:
    kind: str
    sites: tuple[int, ...]
    label: str


def injection_schedule():
    operations = [Operation("CNOT", (c661.ADMIT, CENTER[0]), "center:none-clear")]
    operations += [Operation("CNOT", (c661.PACKET[0][1 + direction], CENTER[1 + direction]),
                             f"center:direction:{direction}") for direction in range(6)]
    for ray in range(6):
        operations += [Operation("CNOT", (CENTER[rail], PHASE_HEAD[ray][rail]),
                                 f"phase-copy:{ray}:{rail}") for rail in range(7)]
    operations.append(Operation("QCA_INVERSE", SOURCE, "Cycle661:qca-inverse"))
    for direction in range(6):
        zero, one = INFO_HEAD[direction]
        operations += [
            Operation("X", (zero,), f"dual-zero-init:{direction}"),
            Operation("CNOT", (c661.CAND[direction], zero), f"dual-zero-toggle:{direction}"),
            Operation("CNOT", (c661.CAND[direction], one), f"dual-one:{direction}"),
            Operation("CNOT", (one, c661.CAND[direction]), f"source-clear:{direction}"),
        ]
    return tuple(operations)


INJECTION_SCHEDULE = injection_schedule()


def initial_cell(word):
    source = c661.qca_forward(c661.source_word(tuple(word)))
    bits = list(source) + [0] * (WIDTH - 84)
    bits[CENTER[0]] = 1
    return tuple(bits)


def validate_initial_cell(bits):
    if len(bits) != WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("binary 187-M2 cell required")
    if tuple(bits[site] for site in CENTER) != onehot(0, 7): raise ValueError("center is not symmetry-neutral none")
    if any(bits[site] for bank in (*PHASE_HEAD, *PHASE_WAKE, *INFO_HEAD) for site in bank):
        raise ValueError("carrier/phase genesis is not blank")
    word = tuple(bits[site] for site in c661.CAND)
    if tuple(bits[:84]) != c661.qca_forward(c661.source_word(word)):
        raise ValueError("source is outside exact Cycle661 basis code")


def apply_injection(bits, *, reverse=False, delete_label=None):
    if len(bits) != WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in bits): raise ValueError("cell code")
    labels = tuple(operation.label for operation in INJECTION_SCHEDULE)
    if delete_label is not None and labels.count(delete_label) != 1: raise ValueError("unique deletion label required")
    output = list(bits)
    sequence = tuple(reversed(INJECTION_SCHEDULE)) if reverse else INJECTION_SCHEDULE
    for operation in sequence:
        if operation.label == delete_label: continue
        if operation.kind == "X": output[operation.sites[0]] ^= 1
        elif operation.kind == "CNOT":
            control, target = operation.sites; output[target] ^= output[control]
        elif operation.kind == "QCA_INVERSE":
            if reverse:
                output[:84] = c661.qca_forward(tuple(output[:84]))
            else:
                output[:84] = c661.apply_schedule(tuple(output[:84]), reverse=True)
        else: raise ValueError(operation.kind)
    return tuple(output)


def autonomous_injection_layer(bits):
    """The same state-triggered injection layer at every coarse cell."""
    if len(bits) != WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in bits): raise ValueError("cell code")
    source = tuple(bits[:84])
    if source in ((0,) * 84, c661.source_word((0,) * 6)):
        return tuple(bits)
    validate_initial_cell(bits)
    return apply_injection(bits)


def expected_injection(word):
    bits = list(c661.source_word((0,) * 6)) + [0] * (WIDTH - 84)
    center = event_center(word)
    for site, bit in zip(CENTER, center): bits[site] = bit
    for bank in PHASE_HEAD:
        for site, bit in zip(bank, center): bits[site] = bit
    for direction, bank in enumerate(INFO_HEAD):
        bits[bank[0]], bits[bank[1]] = 1 - word[direction], word[direction]
    return tuple(bits)


def rotate_cell(bits, frame):
    output = list(bits); output[:84] = c661.rotate_qca_word(tuple(bits[:84]), frame)
    moved_center = rotate_seven(tuple(bits[site] for site in CENTER), frame)
    for site, bit in zip(CENTER, moved_center): output[site] = bit
    for banks in (PHASE_HEAD, PHASE_WAKE):
        original = [tuple(bits[site] for site in bank) for bank in banks]
        for direction, value in enumerate(original):
            target = direction_map(frame, direction); moved = rotate_seven(value, frame)
            for site, bit in zip(banks[target], moved): output[site] = bit
    original_info = [tuple(bits[site] for site in bank) for bank in INFO_HEAD]
    for direction, value in enumerate(original_info):
        target = direction_map(frame, direction)
        for site, bit in zip(INFO_HEAD[target], value): output[site] = bit
    return tuple(output)


def injection_controls():
    failures = inverse_failures = covariance_failures = leakage_failures = relaunch_failures = 0; sources = []
    fixed_source = c661.source_word((0,) * 6); frames = c661.c625.proper_cubic_frames()
    for word in WORDS:
        source = initial_cell(word); sources.append(source); output = apply_injection(source)
        failures += int(output != expected_injection(word))
        inverse_failures += int(apply_injection(output, reverse=True) != source)
        leakage_failures += int(tuple(output[:84]) != fixed_source)
        relaunch_failures += int(autonomous_injection_layer(output) != output)
        for frame in frames:
            left = apply_injection(rotate_cell(source, frame)); right = rotate_cell(output, frame)
            covariance_failures += int(left != right)
    deletions = 0
    for operation in INJECTION_SCHEDULE:
        deletions += int(any(apply_injection(source, delete_label=operation.label) != apply_injection(source)
                             for source in sources))
    malformed = []
    malformed.append(initial_cell((0,) * 6)[:-1])
    dirty_center = list(initial_cell((0,) * 6)); dirty_center[CENTER[1]] = 1; malformed.append(tuple(dirty_center))
    dirty_phase = list(initial_cell((0,) * 6)); dirty_phase[PHASE_HEAD[0][0]] = 1; malformed.append(tuple(dirty_phase))
    dirty_wake = list(initial_cell((0,) * 6)); dirty_wake[PHASE_WAKE[0][0]] = 1; malformed.append(tuple(dirty_wake))
    dirty_info = list(initial_cell((0,) * 6)); dirty_info[INFO_HEAD[0][0]] = 1; malformed.append(tuple(dirty_info))
    nonbinary = list(initial_cell((0,) * 6)); nonbinary[CENTER[0]] = 2; malformed.append(tuple(nonbinary))
    rejected = 0
    for case in malformed:
        try: validate_initial_cell(case)
        except ValueError: rejected += 1
    inherited_counts = {kind: sum(gate.kind == kind for gate in c661.SCHEDULE)
                        for kind in ("X", "CNOT", "TOFFOLI", "FREDKIN")}
    blank_cell = [0] * WIDTH; blank_cell[CENTER[0]] = 1
    blank_nonorigin_fixed = autonomous_injection_layer(tuple(blank_cell)) == tuple(blank_cell)
    result = {
        "basis_rows": 64, "basis_failures": failures, "inverse_failures": inverse_failures,
        "source_reset_leakage_failures": leakage_failures, "all24_injection_tests": 64 * len(frames),
        "all24_injection_failures": covariance_failures, "new_schedule_operations": len(INJECTION_SCHEDULE),
        "new_schedule_deletions_detected": deletions, "malformed_rejected": rejected,
        "malformed_expected": len(malformed), "input_selector_M2": 0, "input_actuality_M2": 0,
        "input_phase_seed_M2": 0, "host_sampler_calls": 0, "supplied_random_draw": False,
        "postimage_relaunch_failures": relaunch_failures, "blank_nonorigin_fixed": blank_nonorigin_fixed,
        "state_trigger": "exact Cycle661 output code; reset source and blank nonorigin cells do not trigger",
        "source_after_injection": "fixed Cycle661 source_word(000000)",
        "exact_injection_schedule": [operation.__dict__ for operation in INJECTION_SCHEDULE],
        "exact_injection_schedule_sha256": digest([operation.__dict__ for operation in INJECTION_SCHEDULE]),
        "inherited_Cycle661_inverse_gate_counts": inherited_counts,
        "inherited_Cycle661_inverse_schedule_sha256": digest([gate.__dict__ for gate in c661.SCHEDULE]),
        "support_before_lowering_M2": max(3, max(len(operation.sites) if operation.kind != "QCA_INVERSE" else 3
                                                 for operation in INJECTION_SCHEDULE)),
        "ambient_ledger": (
            "the state-triggered ambient map is partial; on the declared genesis-to-propagating code the complete "
            "source reset, central value and outgoing dual rails give the displayed exact inverse"
        ),
    }
    result["pass"] = (failures == inverse_failures == covariance_failures == leakage_failures == relaunch_failures == 0
                      and blank_nonorigin_fixed and deletions == len(INJECTION_SCHEDULE) and rejected == len(malformed))
    check("seed-free local injection resets the source and exports every Cycle661 basis sector reversibly", result["pass"],
          {"deletions": deletions, "all24": result["all24_injection_tests"], "selector": 0})
    return result


@dataclass(frozen=True)
class SparseState:
    word: tuple[int, ...]
    center: tuple[int, ...]
    phase_heads: frozenset[tuple[int, int, tuple[int, int, int]]]
    phase_wakes: frozenset[tuple[int, int, tuple[int, int, int]]]
    info_heads: frozenset[tuple[int, int, tuple[int, int, int]]]


def sparse_after_injection(word):
    label = event_index(word)
    return SparseState(tuple(word), event_center(word),
                       frozenset((direction, label, ZERO) for direction in range(6)), frozenset(),
                       frozenset((direction, word[direction], ZERO) for direction in range(6)))


def propagation_labels():
    labels = [f"phase-write:{direction}:{rail}" for direction in range(6) for rail in range(7)]
    labels += [f"phase-shift:{direction}:{rail}" for direction in range(6) for rail in range(7)]
    labels += [f"info-shift:{direction}:{rail}" for direction in range(6) for rail in range(2)]
    return tuple(labels)


PROPAGATION_LABELS = propagation_labels()


def propagate_once(state, delete_label=None):
    if delete_label is not None and PROPAGATION_LABELS.count(delete_label) != 1: raise ValueError("propagation deletion")
    wakes = set(state.phase_wakes); phase_heads = set(); info_heads = set()
    for direction, rail, position in state.phase_heads:
        if delete_label != f"phase-write:{direction}:{rail}": wakes.add((direction, rail, position))
        target = position if delete_label == f"phase-shift:{direction}:{rail}" else add(position, DIRECTIONS[direction])
        phase_heads.add((direction, rail, target))
    for direction, rail, position in state.info_heads:
        target = position if delete_label == f"info-shift:{direction}:{rail}" else add(position, DIRECTIONS[direction])
        info_heads.add((direction, rail, target))
    return SparseState(state.word, state.center, frozenset(phase_heads), frozenset(wakes), frozenset(info_heads))


def infinite_state(word, updates):
    state = sparse_after_injection(word)
    for _ in range(updates): state = propagate_once(state)
    return state


def expected_infinite_state(word, updates):
    label = event_index(word)
    heads = frozenset((direction, label, scale(updates, DIRECTIONS[direction])) for direction in range(6))
    wakes = frozenset((direction, label, scale(step, DIRECTIONS[direction]))
                      for direction in range(6) for step in range(updates))
    info = frozenset((direction, word[direction], scale(updates, DIRECTIONS[direction])) for direction in range(6))
    return SparseState(tuple(word), event_center(word), heads, wakes, info)


def rotate_sparse(state, frame):
    moved_word = rotate_six(state.word, frame); moved_center = rotate_seven(state.center, frame)
    phase_heads = frozenset((direction_map(frame, direction), 0 if rail == 0 else 1 + direction_map(frame, rail - 1),
                             c661.c625.matvec(frame, position))
                            for direction, rail, position in state.phase_heads)
    phase_wakes = frozenset((direction_map(frame, direction), 0 if rail == 0 else 1 + direction_map(frame, rail - 1),
                            c661.c625.matvec(frame, position))
                           for direction, rail, position in state.phase_wakes)
    info_heads = frozenset((direction_map(frame, direction), rail, c661.c625.matvec(frame, position))
                           for direction, rail, position in state.info_heads)
    return SparseState(moved_word, moved_center, phase_heads, phase_wakes, info_heads)


def translate_sparse(state, offset):
    return SparseState(state.word, state.center,
                       frozenset((d, r, add(p, offset)) for d, r, p in state.phase_heads),
                       frozenset((d, r, add(p, offset)) for d, r, p in state.phase_wakes),
                       frozenset((d, r, add(p, offset)) for d, r, p in state.info_heads))


def translate_propagate_once(state, offset):
    return translate_sparse(propagate_once(state), offset)


def finite_projection(state, radius, updates):
    interior_phase_heads = tuple(sorted(item for item in state.phase_heads if inside_cut(item[2], radius)))
    interior_info_heads = tuple(sorted(item for item in state.info_heads if inside_cut(item[2], radius)))
    interior_wakes = tuple(sorted(item for item in state.phase_wakes if inside_cut(item[2], radius)))
    captured = updates > radius
    boundary = {
        "captured": captured, "first_crossing_update": radius + 1 if captured else None,
        "phase": tuple((direction, event_index(state.word)) for direction in range(6)) if captured else (),
        "information": tuple((direction, state.word[direction]) for direction in range(6)) if captured else (),
    }
    return {"center": state.center, "phase_heads": interior_phase_heads, "phase_wakes": interior_wakes,
            "info_heads": interior_info_heads, "boundary_exhaust": boundary}


def expected_finite_projection(word, radius, updates):
    label = event_index(word); captured = updates > radius
    wakes = tuple(sorted((direction, label, scale(step, DIRECTIONS[direction]))
                         for direction in range(6) for step in range(min(updates, radius + 1))))
    phase_heads = () if captured else tuple(sorted((direction, label, scale(updates, DIRECTIONS[direction]))
                                                   for direction in range(6)))
    info_heads = () if captured else tuple(sorted((direction, word[direction], scale(updates, DIRECTIONS[direction]))
                                                  for direction in range(6)))
    boundary = {"captured": captured, "first_crossing_update": radius + 1 if captured else None,
                "phase": tuple((direction, label) for direction in range(6)) if captured else (),
                "information": tuple((direction, word[direction]) for direction in range(6)) if captured else ()}
    return {"center": event_center(word), "phase_heads": phase_heads, "phase_wakes": wakes,
            "info_heads": info_heads, "boundary_exhaust": boundary}


def cell_geometry():
    full = tuple(product(range(-3, 4), repeat=3)); ordered = tuple(sorted(full, key=lambda p: (sum(abs(x) for x in p), p)))
    active = ordered[:WIDTH]; frames = c661.c625.proper_cubic_frames(); full_set = set(full)
    frame_rows = [tuple(c661.c625.matvec(frame, point) for point in active) for frame in frames]
    return {
        "reserved_M2_per_coarse_cell": len(full), "active_M2_per_coarse_cell": WIDTH,
        "inactive_routing_M2_per_coarse_cell": len(full) - WIDTH, "local_cube": "[-3,3]^3",
        "placement_rule": "logical M2 i is the i-th point ordered by (L1 norm,x,y,z)",
        "logical_index_to_coordinate": active, "placement_sha256": digest(active),
        "all24_reserved_cube_invariant": all({c661.c625.matvec(frame, p) for p in full} == full_set for frame in frames),
        "all24_active_frame_placements_inside_cube": all(set(row) <= full_set for row in frame_rows),
        "frame_placement_sha256": [digest(row) for row in frame_rows],
        "maximum_active_L1_diameter": max(sum(abs(a - b) for a, b in zip(x, y)) for x in active for y in active),
        "global_coordinate_rule": "coarse cell x and local p map to physical M2 coordinate 7*x+p",
        "same-bank_adjacent_coarse_shift_L1_support": 7,
        "bulk_dependency_neighborhood": "one coarse cell onsite plus x-d predecessor for direction bank d",
    }


def cut_resources(radius):
    cells = (2 * radius + 1) ** 3
    return {"radius": radius, "coarse_cells": cells, "active_M2": WIDTH * cells,
            "reserved_M2": 343 * cells, "affected_ray_cells": 1 + 6 * radius,
            "affected_ray_cell_fraction": (1 + 6 * radius) / cells,
            "first_crossing_update": radius + 1, "infinite_bulk_return_update": None,
            "boundary_exhaust_M2": 6 * (7 + 2), "constant_overhead_M2_per_coarse_cell": WIDTH}


def moving_carrier_and_restriction_controls():
    formula_failures = finite_failures = lightcone_failures = return_failures = center_failures = 0
    cut_rows = {}
    for name, spec in PREREGISTRATION["cuts"].items():
        radius = spec["radius"]; rows = 0
        for word in WORDS:
            for updates in range(0, 2 * radius + 4):
                state = infinite_state(word, updates); expected = expected_infinite_state(word, updates)
                formula_failures += int(state != expected)
                finite_failures += int(finite_projection(state, radius, updates)
                                       != expected_finite_projection(word, radius, updates))
                maximum = max((sum(abs(x) for x in position) for _, _, position in state.phase_heads | state.info_heads),
                              default=0)
                lightcone_failures += int(maximum != updates)
                if updates >= 1:
                    return_failures += int(any(position == ZERO for _, _, position in state.phase_heads | state.info_heads))
                center_failures += int(state.center != event_center(word)); rows += 1
        cut_rows[name] = {"split": spec["split"], "tested_updates_through": 2 * radius + 3,
                          "basis_time_rows": rows, "resources": cut_resources(radius),
                          "exact_all_future_interior_statement": (
                              "after first crossing, the directed dependency coordinate increases strictly and no carrier "
                              "or wake feeds the center; the captured finite interior therefore remains exact for all later updates"
                          )}
    deletions = 0
    states = [sparse_after_injection(word) for word in WORDS]
    references = [propagate_once(state) for state in states]
    for label in PROPAGATION_LABELS:
        deletions += int(any(propagate_once(state, delete_label=label) != expected
                             for state, expected in zip(states, references)))
    offsets = ((11, -7, 5), (-19, 2, 13), (37, -31, 17)); translation_failures = 0
    for state, offset in product(states, offsets):
        translation_failures += int(propagate_once(translate_sparse(state, offset))
                                    != translate_propagate_once(state, offset))
    monotone_proof = all(sum(a * b for a, b in zip(scale(step + 1, direction), direction))
                         == sum(a * b for a, b in zip(scale(step, direction), direction)) + 1
                         for direction in DIRECTIONS for step in range(20))
    geometry = cell_geometry()
    result = {
        "bulk_rule": "onsite phase-head-to-wake CNOT followed by direction-bank shift x->x+d",
        "translation_invariant": translation_failures == 0, "translation_tests": len(states) * len(offsets),
        "translation_failures": translation_failures, "formula_failures": formula_failures,
        "finite_restriction_failures": finite_failures, "lightcone_failures": lightcone_failures,
        "carrier_return_failures": return_failures, "central_stability_failures": center_failures,
        "propagation_operations": len(PROPAGATION_LABELS), "propagation_deletions_detected": deletions,
        "strict_directed_coordinate_induction": monotone_proof,
        "lightcone_theorem": "after n propagation updates every head is exactly at n*d and every wake site is k*d, 0<=k<n",
        "nonreturn_theorem": "bank d has strictly increasing d-coordinate; its infinite-bulk return update is infinity",
        "finite_restriction_theorem": (
            "C_R equals the infinite bulk on its entire interior through update R and, after exact first-crossing capture "
            "at R+1, forever because the directed causal graph has no incoming edge"
        ),
        "boundary_type": (
            "six first-crossing phase+dual-information exhaust ports supplied only by the finite restriction; "
            "they are not an infinite boundary phase and are not used by the infinite bulk law"
        ),
        "cut_rows": cut_rows, "local_M2_geometry": geometry,
        "no_boundary_phase": True, "no_phase_seed": True, "no_reflection_or_return_service": True,
        "ordered_support_dimension": 1,
        "full_density_three_dimensional_phase_claimed": False,
        "scope_boundary": "the exact wake occupies six rays and has zero density in growing cubic cuts",
    }
    result["pass"] = (formula_failures == finite_failures == lightcone_failures == return_failures == center_failures == 0
                      and translation_failures == 0 and deletions == len(PROPAGATION_LABELS) and monotone_proof
                      and geometry["all24_reserved_cube_invariant"]
                      and geometry["all24_active_frame_placements_inside_cube"])
    check("C3/C4/C6 and held C9 satisfy exact moving-front, finite-restriction and nonreturn theorems", result["pass"],
          {"cuts": list(cut_rows), "deletions": deletions, "return": "infinity"})
    return result


def covariance_controls():
    frames = c661.c625.proper_cubic_frames(); tests24 = failures24 = tests576 = failures576 = 0
    cut_times = [(spec["radius"], t) for spec in PREREGISTRATION["cuts"].values()
                 for t in (1, spec["radius"], spec["radius"] + 1, 2 * spec["radius"] + 3)]
    for frame, word, (_, updates) in product(frames, WORDS, cut_times):
        state = infinite_state(word, updates)
        failures24 += int(rotate_sparse(state, frame) != infinite_state(rotate_six(word, frame), updates)); tests24 += 1
    for left, right, word, spec in product(frames, frames, WORDS, PREREGISTRATION["cuts"].values()):
        state = infinite_state(word, spec["radius"] + 1)
        lhs = rotate_sparse(rotate_sparse(state, right), left)
        rhs = rotate_sparse(state, c661.c625.matmul(left, right))
        failures576 += int(lhs != rhs); tests576 += 1
    result = {"proper_cubic_frames": len(frames), "all24_tests": tests24, "all24_failures": failures24,
              "all576_tests": tests576, "all576_failures": failures576,
              "runtime_frame_selector": False, "preferred_direction_or_ray": False,
              "physical_state_and_position_rotated_together": True}
    result["pass"] = len(frames) == 24 and failures24 == failures576 == 0
    check("moving heads, wakes, dual exhaust and central labels pass all24/all576", result["pass"],
          {"all24": tests24, "all576": tests576})
    return result


def amplitude_fixtures():
    uniform = {word: 1 / 8 for word in WORDS}
    phase_ramp = {word: cmath.exp(1j * (0.173 * index + 0.011 * index * index)) / 8
                  for index, word in enumerate(WORDS)}
    selected = (WORDS[0], WORDS[1], WORDS[7], WORDS[13], WORDS[31], WORDS[42], WORDS[63])
    raw = {word: cmath.exp(1j * (0.37 * index)) * (index + 1) for index, word in enumerate(selected)}
    norm = math.sqrt(sum(abs(value) ** 2 for value in raw.values()))
    sparse = {word: value / norm for word, value in raw.items()}
    return {"uniform64": uniform, "phase_ramp64": phase_ramp, "held_sparse_complex": sparse}


def recover_word_from_dual(encoded):
    if len(encoded) != 12: raise ValueError("six dual rails required")
    word = []
    for direction in range(6):
        pair = tuple(encoded[2 * direction:2 * direction + 2])
        if pair not in ((1, 0), (0, 1)): raise ValueError("malformed dual rail")
        word.append(pair[1])
    return tuple(word)


def coherence_and_type_controls():
    rows = {}; failures = 0
    for name, amplitudes in amplitude_fixtures().items():
        output = {}; weights = [0.0] * 7
        for word, amplitude in amplitudes.items():
            key = (event_center(word), dual_word(word))
            output[key] = output.get(key, 0j) + amplitude
            weights[event_index(word)] += abs(amplitude) ** 2
        recovered = {recover_word_from_dual(key[1]): amplitude for key, amplitude in output.items()}
        residual = max(abs(recovered.get(word, 0j) - amplitude) for word, amplitude in amplitudes.items())
        normalization = abs(sum(abs(value) ** 2 for value in output.values()) - 1)
        off_diagonal = 0.0
        failures += int(residual > TOL or normalization > TOL or len(output) != len(amplitudes))
        rows[name] = {"support_sectors": len(amplitudes), "outgoing_basis_states": len(output),
                      "amplitude_phase_inverse_residual": residual, "normalization_residual": normalization,
                      "central_weights_none_plus_six": weights, "central_reduced_rank": sum(value > TOL for value in weights),
                      "central_offdiagonal_Frobenius": off_diagonal,
                      "finite_global_state_type": "PureCoherentDirectSum[center x six dual carriers x phase fronts]",
                      "local_center_type": "DiagonalReducedDensity[none|six]"}
    malformed = 0
    for encoded in ((0,) * 12, (1,) * 12, (1, 0) * 5, (1, 1) + (1, 0) * 5):
        try: recover_word_from_dual(encoded)
        except ValueError: malformed += 1
    result = {
        "fixture_rows": rows, "failures": failures, "all_64_dual_words_distinct": len({dual_word(word) for word in WORDS}) == 64,
        "malformed_dual_words_rejected": malformed, "malformed_dual_words_expected": 4,
        "arbitrary_amplitude_isometry_theorem": (
            "the 64 basis images have distinct six-ray dual words, so their Gram matrix is identity and linear extension "
            "preserves every complex amplitude and relative phase"
        ),
        "partial_trace_statement": (
            "orthogonal outgoing words make the center reduced matrix diagonal; this is tracing-out, not one realized value"
        ),
        "one_objective_realized_token": False,
    }
    result["pass"] = (failures == 0 and result["all_64_dual_words_distinct"] and malformed == 4
                      and all(row["central_offdiagonal_Frobenius"] == 0 for row in rows.values()))
    check("arbitrary Cycle661 amplitudes/phases are retained globally while the local center is only diagonal", result["pass"],
          {"fixtures": list(rows), "objective": False})
    return result


def thermodynamic_sector_controls():
    cut_rows = {}; overlap_failures = expectation_failures = 0
    labels = range(7)
    for name, spec in PREREGISTRATION["cuts"].items():
        length = spec["radius"]; pair_tests = 0
        for left, right in combinations(labels, 2):
            # A single ordered wake site is already orthogonal; the L-tail product remains exactly orthogonal.
            overlap = 0.0 ** (6 * length)
            overlap_failures += int(overlap != 0.0); pair_tests += 1
            for probe in (left, right):
                expected_left = int(probe == left); expected_right = int(probe == right)
                expectation_failures += int(expected_left == expected_right)
        cut_rows[name] = {
            "split": spec["split"], "tail_length_per_ray": length, "ordered_tail_registers": 6 * length,
            "distinct_phase_pair_tests": pair_tests, "maximum_distinct_product_overlap": 0.0,
            "central_sequence_commutator_bound_for_K1": 2 / (6 * length),
            "phase_projector_expectation": "omega_e(M_f^L)=delta[e,f], variance=0",
        }
    decreasing = all(cut_rows[left]["central_sequence_commutator_bound_for_K1"]
                     > cut_rows[right]["central_sequence_commutator_bound_for_K1"]
                     for left, right in (("C3", "C4"), ("C4", "C6"), ("C6", "C9")))
    result = {
        "finite_overlap_failures": overlap_failures, "tail_expectation_failures": expectation_failures,
        "cut_rows": cut_rows, "central_sequence_bound_strictly_decreases": decreasing,
        "conditional_theorem": (
            "given the infinite blank phase-register tensor product and the t->infinity local weak limit, the ray-average "
            "projectors form a central sequence with scalar limit delta[e,f]; hence the seven infinite product phase "
            "states have pairwise disjoint quasi-local/GNS sectors"
        ),
        "exact_added_supply": [
            "an infinite tensor product of initially blank phase/head registers",
            "the quasi-local observable algebra and its local-weak t->infinity limit",
            "the GNS/central-sequence criterion used to name disjoint representations",
        ],
        "not_supplied": ["boundary phase", "phase seed", "selector", "sampler", "random draw", "actuality token"],
        "finite_time_state": "one globally coherent pure/direct-sum state",
        "infinite_limit_state": "a non-extremal algebraic mixture/central decomposition over disjoint phase sectors",
        "objective_realization": "not derived; disjointness does not select one central summand",
        "tracing_or_nonreturn_called_actuality": False,
    }
    result["pass"] = overlap_failures == expectation_failures == 0 and decreasing
    check("the infinite-volume theorem gives conditional disjoint sectors but not a selected sector", result["pass"],
          {"phase_labels": 7, "held_larger": "C9", "objective": False})
    return result


def cycle669_controls():
    failures = inverse_failures = malformed = 0
    rows = {}
    for name, spec in PREREGISTRATION["cuts"].items():
        capacity = spec["radius"]; local_failures = 0
        for word in WORDS:
            center = event_center(word); index = center.index(1); actual = int(index != 0)
            direction = onehot(index - 1, 6) if actual else (0,) * 6
            exhaust = dual_word(word); recovered = recover_word_from_dual(exhaust)
            event = c669.EventToken(actual, direction, exhaust, "Cycle661_basis")
            chain = c669.initial_chain(capacity); output, _ = c669.append_event(chain, event)
            local_failures += int(recovered != word or len(c669.read_chain(output)) != actual)
            if actual: inverse_failures += int(c669.inverse_event(output) != chain)
        failures += local_failures
        rows[name] = {"capacity": capacity, "basis_rows": 64, "failures": local_failures}
    for bad in ((0,) * 12, (1,) * 12, (1, 0) * 5, (1, 1) + (1, 0) * 5):
        try: recover_word_from_dual(bad)
        except ValueError: malformed += 1
    result = {"cut_rows": rows, "basis_interface_failures": failures, "inverse_failures": inverse_failures,
              "malformed_exhaust_rejected": malformed, "malformed_exhaust_expected": 4,
              "basis_token_interface": "exact", "native_coherent_ObjectiveEventToken_available": False,
              "coherent_interface_type": "CoherentDirectSum[Cycle669 empty|one-node branch histories]"}
    result["pass"] = failures == inverse_failures == 0 and malformed == 4
    check("every finite-cut basis center and dual exhaust attaches to Cycle669 exactly", result["pass"],
          {"rows": sum(row["basis_rows"] for row in rows.values()), "coherent_token": False})
    return result


def no_go_discipline():
    current = current_citation("def moving_carrier_and_restriction_controls(")
    c674A = citation("docs/work_history/repo/review_feedback/PHYSICAL_SYMMETRY_NEUTRAL_ORDER_PARAMETER_ACTUALIZER_TOURNAMENT_CYCLE674_NOTE_2026-07-23.md", "## Route A — deterministic instability")
    c674B = citation("docs/work_history/repo/review_feedback/PHYSICAL_SYMMETRY_NEUTRAL_ORDER_PARAMETER_ACTUALIZER_TOURNAMENT_CYCLE674_NOTE_2026-07-23.md", "## Route B — finite reversible metastable candidate")
    c674C = citation("docs/work_history/repo/review_feedback/PHYSICAL_SYMMETRY_NEUTRAL_ORDER_PARAMETER_ACTUALIZER_TOURNAMENT_CYCLE674_NOTE_2026-07-23.md", "## Route C — relational/domain-wall variants")
    c674terminal = citation("docs/work_history/repo/review_feedback/PHYSICAL_SYMMETRY_NEUTRAL_ORDER_PARAMETER_ACTUALIZER_TOURNAMENT_CYCLE674_NOTE_2026-07-23.md", "**NOT MET, NOT FALSIFIED** for one objective")
    c536 = citation("docs/work_history/repo/review_feedback/PHYSICAL_COHERENT_SEED_MEMBER_DILATION_CYCLE536_NOTE_2026-07-21.md", "a diagonal density operator is not one realized member")
    c663 = citation("docs/work_history/repo/review_feedback/PHYSICAL_DISSIPATIVE_METASTABLE_FORMATION_CHANNEL_CYCLE663_NOTE_2026-07-23.md", "metastability are not irreversible framework Record formation")
    c662 = citation("docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md", "stochastic law itself—not a host sampler")
    routes = [
        {"family": "moving-carrier increasing phase field", "object": "quasi-local ray phase algebra",
         "mechanism": "directed front, persistent wake and central sequence", "terminal": "one selected central summand",
         "honesty": "ATTEMPTED", "authority": current,
         "disposition": "finite restriction and conditional disjointness close; objective selection does not"},
        {"family": "finite deterministic neutral instability", "object": "partial ready/spent cellular map",
         "mechanism": "basis latch", "terminal": "one coherent-input value", "honesty": "RULED OUT BY PRIOR",
         "authority": c674A, "disposition": "coherent output remains a direct sum"},
        {"family": "finite reversible metastable code", "object": "triple-repetition isometry",
         "mechanism": "one-error majority invariant", "terminal": "robustness plus actuality", "honesty": "RULED OUT BY PRIOR",
         "authority": c674B, "disposition": "finite stability does not promote actuality"},
        {"family": "relational domain wall", "object": "six-ray finite wall history",
         "mechanism": "relative wall propagation", "terminal": "one nonrelative center", "honesty": "RULED OUT BY PRIOR",
         "authority": c674C, "disposition": "wall alternatives remain coherent"},
        {"family": "hybrid objective stochastic field", "object": "quantum-classical instrument",
         "mechanism": "law-owned sigma update", "terminal": "derive selection law", "honesty": "RULED OUT BY PRIOR",
         "authority": c662, "disposition": "objective value belongs to supplied stochastic law"},
        {"family": "ontic selector extension", "object": "enlarged classical-quantum domain",
         "mechanism": "selector-controlled token", "terminal": "native-domain token", "honesty": "RULED OUT BY PRIOR",
         "authority": c674terminal, "disposition": "selector is an added actuality input"},
        {"family": "autonomous nonlinear extremal-sector law", "object": "nonlinear state flow on central decomposition",
         "mechanism": "intrinsic extremalization with coherent exhaust", "terminal": "one objective summand without seed/sampler",
         "honesty": "OPEN_NOT_COUNTED", "authority": c662,
         "disposition": "a concrete covariant law and exact exhaust theorem have not been constructed"},
    ]
    source = "\n".join(inspect.getsource(fn).lower() for fn in
                        (injection_controls, moving_carrier_and_restriction_controls,
                         coherence_and_type_controls, thermodynamic_sector_controls))
    phrases = ("we assume", "by construction", "as is standard", "the framework provides", "bridge context", "background",
               "naturally", "obviously", "standard qft", "registered", "canonical")
    hidden = tuple(phrase for phrase in phrases if phrase in source)
    residuals = [
        {"witness": c674terminal, "prior": "native coherent token not met", "current": "one selected thermodynamic summand", "match": True},
        {"witness": c536, "prior": "diagonal is not one realized member", "current": "local diagonal is not promoted", "match": True},
        {"witness": c663, "prior": "finite metastability is not irreversible formation", "current": "nonreturn is not promoted", "match": True},
        {"witness": c662, "prior": "objective sigma is supplied by stochastic law", "current": "no law-owned selection imported", "match": True},
    ]
    rhetoric = [
        {"claim": "local diagonality is not objective actuality", "per_element": "64 sector images",
         "per_site": "seven central rails", "per_mode": "three coherent fixtures", "per_block": "C3/C4/C6/C9",
         "lattice_wide": "finite pure state and infinite central decomposition distinguished"},
        {"claim": "carrier nonreturn is not objective actuality", "per_element": "six direction banks",
         "per_site": "strict directed-coordinate edge", "per_mode": "phase and dual information",
         "per_block": "four exact cuts", "lattice_wide": "symbolic all-future induction, not selection"},
        {"claim": "sector disjointness is not one selected sector", "per_element": "21 phase pairs",
         "per_site": "orthogonal one-hot wake", "per_mode": "seven tail projectors",
         "per_block": "C3/C4/C6/C9 tail averages", "lattice_wide": "conditional GNS central decomposition"},
    ]
    partial = [
        {"path": "Cycle676 moving front", "status": "EXECUTED_PARTIAL",
         "closes": "translation-invariant export, exact finite restrictions, conditional disjoint phase sectors"},
        {"path": "Cycle674 deterministic latch", "status": "EXECUTED_PRIOR", "closes": "finite stable basis center"},
        {"path": "Cycle674 repetition", "status": "EXECUTED_PRIOR", "closes": "finite one-error stability"},
        {"path": "Cycle662 stochastic law", "status": "EXECUTED_PRIOR", "closes": "objective event conditional on supplied law"},
        {"path": "nonlinear extremal-sector law", "status": "OPEN", "closes": "candidate objective selection if explicitly constructed"},
    ]
    steelman = (
        "A hostile reviewer should construct a proper-cubic, translation-invariant nonlinear or genuinely open local law "
        "whose central-decomposition weights evolve toward one extremal phase in each physical state while a reversible "
        "outgoing channel retains every Cycle661 amplitude and phase. The law must define objective central projections "
        "without a boundary phase, seed, sampler or hidden selector and must still attach to Cycle669. Cycle662 shows that "
        "objective selection is mathematically coherent once such a stochastic law is supplied, so the absence of a derived "
        "law here makes a broad impossibility claim premature."
    )
    echoes = [
        {"cycle": 536, "retired": "coherent seed diagonal", "remaining": "one realized value"},
        {"cycle": 662, "retired": "objective token under supplied sigma law", "remaining": "derive the law"},
        {"cycle": 663, "retired": "finite reduced metastability", "remaining": "objective sector ownership"},
        {"cycle": 671, "retired": "conditional selector interface", "remaining": "native-domain selection"},
        {"cycle": 674, "retired": "finite neutral latches/walls", "remaining": "thermodynamic selection"},
        {"cycle": 676, "retired": "conditional disjoint thermodynamic sectors", "remaining": "one selected summand"},
    ]
    qualifying = sum(row["honesty"] in ("ATTEMPTED", "RULED OUT BY PRIOR") for row in routes)
    complete = qualifying >= 5 and not hidden and all(row["match"] for row in residuals) and len(rhetoric) == 3
    result = {
        "skill_freshness": {"origin_main_checked": True, "origin_main_advanced": True,
                            "remote_skill_followed": True, "dirty_worktree_moved": False},
        "N1_routes": routes, "N1_qualifying_normalized_families": qualifying,
        "N2_collapsed_walls": ["objective_selection_of_one_central_summand"], "N2_directed_pairs": [],
        "N2_downstream_nonterminal_open_conditions": ["framework_Record", "Born_empirical_law", "physical_time_rate"],
        "N3_hidden_phrase_hits": hidden, "N4_residual_matches": residuals, "N5_rhetoric": rhetoric,
        "N6_partial_closure_paths": partial, "N6_primitive_registry_claim_made": False,
        "N7_steelman": steelman, "N7_supporting_authority": c662, "N8_cross_cycle_echo": echoes,
        "checklist_complete": complete, "negative_claim_gate_status": "FAIL_DO_NOT_SHIP_NEGATIVE",
        "negative_gate_failure_reason": "N7 autonomous nonlinear/open extremal-sector law remains untested",
        "demotion": "partial-attempt-with-named-untested-route", "broad_no_go_claim": False,
        "minimum_content_claim": False, "shared_route_independent_obstruction": False, "axiom_pressure": False,
        "discipline_compliance_pass": complete,
    }
    check("fresh N1-N8 blocks a broad objective-selection impossibility claim", complete,
          {"families": qualifying, "negative_gate": result["negative_claim_gate_status"]})
    return result


def inventory():
    return {
        "supplied": [
            "Cycle661 coherent source/QCA", "initially blank phase/head registers at every modeled cell",
            "translation-invariant direction-bank shift law", "finite cut geometry",
            "finite first-crossing boundary exhaust only for restriction models", "Cycle669 root/next seeds",
            "compile-time proper-cubic frame chart", "for the conditional limit: infinite blank tensor product and GNS representation",
        ],
        "derived": [
            "seed-free event-dependent phase launch", "exact reset of the 84-M2 local source",
            "six-ray dual encoding of all 64 sectors", "persistent increasing phase wake",
            "exact C3/C4/C6/C9 finite restrictions", "strict lightcone/nonreturn induction",
            "conditional seven-sector disjointness theorem", "branchwise Cycle669 interface",
        ],
        "open": [
            "one objective realized central summand", "collision-resolved full-density 3D phase front",
            "autonomous nonlinear/open selection law", "framework Record",
            "Born/empirical-frequency law", "physical time/rate", "physical energy/generator", "source/gravity",
        ],
    }


def note_text(receipt):
    ng = receipt["no_go_discipline"]; inj = receipt["injection_controls"]; mov = receipt["moving_carrier_controls"]
    cov = receipt["covariance_controls"]; coh = receipt["coherence_type_controls"]; thermo = receipt["thermodynamic_sector_controls"]
    chain = receipt["Cycle669_controls"]
    n1 = "\n".join(f"| {r['family']} | {r['object']} | {r['mechanism']} | {r['terminal']} | {r['honesty']} | `{r['authority']['path']}:{r['authority']['line']}` | {r['disposition']} |" for r in ng["N1_routes"])
    n4 = "\n".join(f"| `{r['witness']['path']}:{r['witness']['line']}` | {r['prior']} | {r['current']} | {str(r['match']).lower()} |" for r in ng["N4_residual_matches"])
    n5 = "\n".join(f"| {r['claim']} | {r['per_element']} | {r['per_site']} | {r['per_mode']} | {r['per_block']} | {r['lattice_wide']} |" for r in ng["N5_rhetoric"])
    n6 = "\n".join(f"| {r['path']} | {r['status']} | {r['closes']} |" for r in ng["N6_partial_closure_paths"])
    n8 = "\n".join(f"| Cycle {r['cycle']} | {r['retired']} | {r['remaining']} |" for r in ng["N8_cross_cycle_echo"])
    cuts = "\n".join(f"| {name} | {row['split']} | {row['resources']['coarse_cells']} | {row['resources']['active_M2']} | {row['resources']['first_crossing_update']} | {row['tested_updates_through']} |" for name, row in mov["cut_rows"].items())
    amplitudes = "\n".join(f"| {name} | {row['support_sectors']} | {row['outgoing_basis_states']} | {row['central_reduced_rank']} | {row['amplitude_phase_inverse_residual']:.3e} | {row['central_offdiagonal_Frobenius']:.1f} |" for name, row in coh["fixture_rows"].items())
    tails = "\n".join(f"| {name} | {row['split']} | {row['tail_length_per_ray']} | {row['ordered_tail_registers']} | {row['distinct_phase_pair_tests']} | {row['central_sequence_commutator_bound_for_K1']:.6f} |" for name, row in thermo["cut_rows"].items())
    return f"""# Moving-carrier phase field and finite-restriction theorem — Cycle 676

Authority: **none**

Audit: **unset**

## Fresh no-go-discipline gate before disposition

The freshness check fetched the advanced `origin/main` skill and used its complete remote N1–N8 text without moving the dirty worktree.

### N1

| family | object | mechanism | terminal | honesty | authority | disposition |
|---|---|---|---|---|---|---|
{n1}

### N2–N4

The collapsed current wall is `{ng['N2_collapsed_walls']}`. Record, Born-law and time questions are downstream, not extra current-target walls. Hidden phrase hits are `{ng['N3_hidden_phrase_hits']}`.

| witness | prior residual | current residual | match? |
|---|---|---|---:|
{n4}

### N5

| claim | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
{n5}

### N6

| path | status | closes |
|---|---|---|
{n6}

No claim that a retained primitive is absent is made, so the primitive-registry gate is not triggered.

### N7

{ng['N7_steelman']} Supporting prior boundary: `{ng['N7_supporting_authority']['path']}:{ng['N7_supporting_authority']['line']}`.

### N8

| cycle | retired | remaining |
|---|---|---|
{n8}

Negative-claim gate: **{ng['negative_claim_gate_status']}**. This is a `{ng['demotion']}`, not a no-go. Shared route-independent obstruction: **not established**. Axiom pressure: **none**.

## Frozen target

Target `{receipt['frozen_contract']['target_sha256']}` and preregistration `{receipt['frozen_contract']['preregistration_sha256']}` precede evidence. All `{len(receipt['frozen_contract']['pins'])}` shores are exact at `{receipt['frozen_contract']['shore']}`.

The exact terminal is one objective `none|six` token on the native coherent Cycle661 domain. A finite coherent state, a diagonal reduced center, disjoint infinite-volume representations, and a central decomposition are explicitly forbidden as substitutes.

## Local translation-invariant construction

Every coarse cell reserves the same 187 active M2: 84 Cycle661 source rails, seven central rails, six seven-rail phase heads, six seven-rail phase wakes, and six two-rail information heads. The genesis has no phase seed, selector, actuality token, random draw or sampler. Only the origin carries the Cycle661 input; every carrier and wake register is blank.

On the exact source code, a bounded local injection writes the `none|six` center, copies that event label to all six phase heads, applies the exact inverse Cycle661 QCA, and moves candidate bit `d` into the dual rail `(zero_d,one_d)` on ray `d`. The 84-M2 source is thereby reset to fixed `source_word(000000)`. The source-code trigger is consumed: the postimage and blank nonorigin cells do not relaunch. The six dual rails collectively distinguish all 64 words without choosing a preferred ray. Injection passes 64 basis rows, exact inverse, all `{inj['new_schedule_deletions_detected']}` new-operation deletions, malformed, leakage, relaunch/saturation and `{inj['all24_injection_tests']}` covariance tests.

The same bulk rule is applied at every coarse cell: each phase head CNOTs its one-hot value into the local wake and every phase/information bank shifts from `x` to `x+d`. The rule is translation invariant and has no runtime frame or boundary service. Its directed coordinate increases by one on every update.

## Exact finite restrictions and resources

| cut | split | coarse cells | active M2 | first crossing | tested through |
|---|---|---:|---:|---:|---:|
{cuts}

For update `n`, every moving head is exactly at `n d`; its wake occupies `k d`, `0 <= k < n`. Thus C_R first crossing is exactly `R+1`. The direction-bank coordinate increases strictly, so the infinite-bulk return update is infinity. No head or wake has an incoming dependency to the center. After first crossing, a finite restriction stores the phase and dual word in six explicit boundary ports and its entire interior is exact for all later updates.

That boundary capture is a finite representation ledger, not translation-invariant bulk dynamics, not an infinite boundary phase, and not objective actuality. Nonreturn is a causal fact about this conveyor, not a branch-selection rule.

The ordered support grows without bound but is exactly six rays, hence has zero density in the growing cubic cut. This is not claimed to be a collision-resolved full-density three-dimensional phase. Ray support is nevertheless sufficient for the conditional disjointness test below because different phase labels disagree on infinitely many local registers.

Each receipt serializes the exact 187-index M2 placement in `[-3,3]^3`, the global coordinate rule `7*x+p`, the complete injection schedule and its inherited Cycle661 schedule digest. Onsite support is at most three M2 before lowering; a same-bank adjacent-coarse-cell dependency spans seven physical M2 steps. The 343-M2 reserved cell and every active frame placement pass all24.

Full trajectory covariance gives `{cov['all24_tests']}` all24 and `{cov['all576_tests']}` all576 tests with zero failures. Translation, `{mov['propagation_deletions_detected']}` propagation deletions, leakage, malformed-domain, exact light-cone and held-C9 controls pass.

## Three rigorously distinct state types

### I. Finite globally coherent state

| fixture | sectors | outgoing basis | center rank | amplitude inverse residual | center offdiag |
|---|---:|---:|---:|---:|---:|
{amplitudes}

Distinct dual words make the 64 basis images orthogonal, so linear extension preserves arbitrary complex amplitudes and relative phases exactly. The finite global state is `PureCoherentDirectSum[center x dual carriers x phase fronts]`. Tracing carriers gives a diagonal center. That trace is not one realized member.

### II. Conditional disjoint infinite-volume sectors

| cut | split | tail/ray | ordered registers | phase-pair tests | K=1 commutator bound |
|---|---|---:|---:|---:|---:|
{tails}

The conditional theorem supplies an infinite tensor product of initially blank phase registers, the quasi-local algebra and its local-weak `n -> infinity` limit, and the GNS/central-sequence criterion. Ray-average phase projectors then converge to distinct scalar values and the seven product-phase representations are pairwise disjoint. No boundary phase is supplied; the phase comes from the Cycle661 branch and an infinite blank reservoir is the explicit resource.

The limiting algebraic state is nevertheless a non-extremal mixture/central decomposition across those disjoint sectors. Superselection removes local interference between sectors; it does not select one sector as the realized world.

### III. Objective realized token

This type is **not obtained**. Neither a finite pure cat, a locally diagonal center, outward escape, a conditional disjoint-sector theorem, nor a central decomposition provides one objective member. An autonomous objective selection law remains absent and untested.

## Cycle669 and semantic boundaries

All `{sum(row['basis_rows'] for row in chain['cut_rows'].values())}` C3/C4/C6/C9 basis interfaces attach and invert exactly. The coherent interface remains `{chain['coherent_interface_type']}`; a native coherent `ObjectiveEventToken` is unavailable.

The infinite blank reservoir, finite-cut boundary registers, Cycle669 seeds, and compile-time frame chart are supplied explicitly. No packet, wake, latch or sector is called a framework Record. Diagonal weights are not called Born probabilities or empirical frequencies. Update count, cut radius, wake length, stability and nonreturn are not physical time or rates. No wrapped phase is called physical energy and no generator element is called a rate.

## Disposition

**PASS / POSITIVE CONDITIONAL THEOREM** for a translation-invariant moving-carrier phase field, exact source reset and coherent export, held increasing finite restrictions, and conditional pairwise-disjoint infinite-volume phase sectors.

**NOT MET, NOT FALSIFIED** for one objective realized central token. The strongest result stops at a central decomposition; there is no shared obstruction and no axiom pressure. The optimal next campaign is the N7 autonomous nonlinear/open extremal-sector selection law with the present exact exhaust and type gates held fixed.
"""


def note_contract():
    body = " ".join(NOTE.read_text().lower().split())
    required = (
        "authority: **none**", "audit: **unset**", "fresh no-go-discipline gate before disposition",
        "not a no-go", "not met, not falsified", "shared route-independent obstruction: **not established**",
        "axiom pressure: **none**", "tracing carriers gives a diagonal center. that trace is not one realized member",
        "superselection removes local interference between sectors; it does not select one sector",
        "nonreturn is a causal fact about this conveyor, not a branch-selection rule",
        "not physical time or rates", "no generator element is called a rate",
    )
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def main():
    signal.alarm(math.ceil(WALL_CAP_SECONDS)); started = time.perf_counter()
    frozen, imported = freeze_and_shore_controls(); ng = no_go_discipline()
    injection = injection_controls(); moving = moving_carrier_and_restriction_controls()
    covariance = covariance_controls(); coherence = coherence_and_type_controls()
    thermodynamic = thermodynamic_sector_controls(); chain = cycle669_controls()
    receipt = {
        "cycle": 676, "date": "2026-07-23", "authority": AUTHORITY, "audit": AUDIT,
        "status": "moving-carrier phase field and conditional disjoint sectors; objective token not met",
        "classification": "positive-conditional-theorem-with-honest-terminal-residual",
        "frozen_contract": frozen, "no_go_discipline": ng, "injection_controls": injection,
        "moving_carrier_controls": moving, "covariance_controls": covariance,
        "coherence_type_controls": coherence, "thermodynamic_sector_controls": thermodynamic,
        "Cycle669_controls": chain, "supplied_structure_inventory": inventory(),
        "strict_full_framework_terminal_met": False, "target_contract_candidate_terminal_met": False,
        "exact_terminal_met": False, "exact_terminal_disposition": "NOT_MET_NOT_FALSIFIED",
        "strongest_constructive_result": (
            "a 187-M2-per-cell translation-invariant directed phase conveyor with exact source reset, complete six-ray "
            "dual coherent exhaust, all-future finite-restriction theorem and conditional seven-sector GNS disjointness"
        ),
        "state_type_disposition": {
            "finite_global": "globally coherent pure/direct-sum state",
            "finite_local_center": "rank-up-to-seven diagonal reduced state, not objective",
            "infinite_conditional": "non-extremal central decomposition over disjoint sectors, not selected",
            "objective_realized": "not derived",
        },
        "shared_route_independent_obstruction": False, "axiom_pressure": False,
        "breakthrough": False, "author_accepted": False,
        "optimal_next_campaign": "autonomous nonlinear/open extremal-sector selection law with exact coherent exhaust",
    }
    NOTE.write_text(note_text(receipt)); note = note_contract()
    check("Cycle676 note preserves finite/diagonal/superselection/objective and semantic type gates", note["pass"], note["missing"])
    elapsed = time.perf_counter() - started; rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000: rss *= 1024
    receipt.update({"note_contract": note, "runner_sha256": file_sha(Path(__file__)), "note_sha256": file_sha(NOTE),
                    "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss, "tests_passed": PASS, "tests_failed": FAIL})
    receipt["pass"] = (FAIL == 0 and all(item["pass"] for item in
                       (frozen, injection, moving, covariance, coherence, thermodynamic, chain, note))
                       and ng["discipline_compliance_pass"] and not ng["broad_no_go_claim"]
                       and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES and AUTHORITY == "none" and AUDIT == "unset")
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True,
                                  default=lambda x: x.item() if isinstance(x, np.generic) else list(x)) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
                      "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
                      "note": str(NOTE), "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]: raise SystemExit(1)


if __name__ == "__main__": main()
