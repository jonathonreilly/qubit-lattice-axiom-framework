#!/usr/bin/env python3
"""Cycle 329: derive Cycle-326 matcher/readiness controls from physical support.

Three fixed reversible Boolean routes consume the actual Cycle-314/Cycle-312
stable block labels, bounded physical-support incidence flags, and individual
predecessor-closed flags.  They output the Cycle-326 identity-match and
predecessor-readiness bits without a host-side conjunction.  Occurrence,
close, freshness, Record typing, permanence, and clock calibration remain
separate.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import product
from math import ceil, log2
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_event_to_append_commit_candidate_cycle326_2026_07_18 as c326


c314 = c326.c314
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SUPPORT_MATCHER_PREDECESSOR_CONTROLS_CYCLE329_NOTE_2026-07-18.md"
)
TOL = 1.2e-11
MAX_LENGTH = 6
MODE_BITS = ceil(log2(6 * MAX_LENGTH**3))
INDEX_BITS = ceil(log2(3 * MAX_LENGTH**3))
LABEL_BITS = 1 + INDEX_BITS + 2 * MODE_BITS
MAX_SUPPORT_FLAGS = 102
WORD_WIDTH = LABEL_BITS + MAX_SUPPORT_FLAGS
SOURCE_PATCH_M2 = 45

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


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-329 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "physical support matcher and predecessor controls",
        "direct bounded comparator",
        "relational hash/syndrome comparator",
        "local causal-certificate propagation",
        "no host conjunction",
        "anti-splicing false positives",
        "anti-splicing false negatives",
        "support corruption",
        "missing predecessor",
        "schedule quotient",
        "held l=6",
        "all 24 proper-cubic frames",
        "occurrence remains separate",
        "close law remains separate",
        "fresh capacity remains separate",
        "typing remains separate",
        "permanence remains separate",
        "matcher-to-clock remains separate",
        "calibration remains separate",
        "derived match is not occurrence",
        "commit candidate is not a record",
        "broad gate status: fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the three support-derived routes and semantic firewall",
        not missing,
        missing,
    )


def integer_bits(value: int, width: int) -> tuple[int, ...]:
    if not 0 <= value < 2**width:
        raise ValueError((value, width))
    return tuple((value >> shift) & 1 for shift in reversed(range(width)))


@dataclass(frozen=True)
class Gate:
    kind: str
    controls: tuple[int, ...]
    target: int


def apply_gate(state: list[int], gate: Gate) -> None:
    if gate.kind == "X":
        state[gate.target] ^= 1
    elif gate.kind == "CNOT":
        if state[gate.controls[0]]:
            state[gate.target] ^= 1
    elif gate.kind == "TOFFOLI":
        if state[gate.controls[0]] and state[gate.controls[1]]:
            state[gate.target] ^= 1
    else:
        raise ValueError(gate.kind)


def execute(
    state: list[int],
    gates: tuple[Gate, ...],
    deleted_gate: int | None = None,
) -> list[int]:
    output = list(state)
    for index, gate in enumerate(gates):
        if index != deleted_gate:
            apply_gate(output, gate)
    return output


def equality_circuit(
    word: tuple[int, ...],
    expected: tuple[int, ...],
    *,
    delete_copy: bool = False,
) -> tuple[int, int, int]:
    """Fixed X/CNOT/Toffoli equality, with compute-copy-uncompute."""

    if len(word) != len(expected) or not word:
        raise ValueError("equality words must have equal nonzero width")
    if set(word) - {0, 1} or set(expected) - {0, 1}:
        raise ValueError("equality words must be binary")
    width = len(word)
    chain = tuple(range(width, width + max(0, width - 1)))
    output = width + max(0, width - 1)
    state = list(word) + [0] * max(0, width - 1) + [0]
    gates: list[Gate] = []
    for index, value in enumerate(expected):
        if value == 0:
            gates.append(Gate("X", (), index))
    if width == 1:
        copy_gate = len(gates)
        gates.append(Gate("CNOT", (0,), output))
    else:
        forward = [Gate("TOFFOLI", (0, 1), chain[0])]
        forward.extend(
            Gate("TOFFOLI", (chain[index - 2], index), chain[index - 1])
            for index in range(2, width)
        )
        gates.extend(forward)
        copy_gate = len(gates)
        gates.append(Gate("CNOT", (chain[-1],), output))
        gates.extend(reversed(forward))
    for index in reversed(range(width)):
        if expected[index] == 0:
            gates.append(Gate("X", (), index))
    result = execute(state, tuple(gates), copy_gate if delete_copy else None)
    return result[output], len(state) - width, len(gates)


def syndrome_circuit(word: tuple[int, ...]) -> tuple[tuple[int, ...], int]:
    if not word or set(word) - {0, 1}:
        raise ValueError("syndrome word must be nonempty and binary")
    address_bits = ceil(log2(len(word) + 1))
    width = address_bits + 1
    state = list(word) + [0] * width
    base = len(word)
    gates = []
    for index in range(len(word)):
        gates.append(Gate("CNOT", (index,), base))
        address = index + 1
        for bit in range(address_bits):
            if (address >> bit) & 1:
                gates.append(Gate("CNOT", (index,), base + 1 + bit))
    output = execute(state, tuple(gates))
    return tuple(output[base:]), len(gates)


def syndrome_compare(
    word: tuple[int, ...],
    expected_word: tuple[int, ...],
    *,
    delete_copy: bool = False,
) -> tuple[int, int, int]:
    syndrome, syndrome_gates = syndrome_circuit(word)
    expected, _ = syndrome_circuit(expected_word)
    match, workspace, equality_gates = equality_circuit(
        syndrome,
        expected,
        delete_copy=delete_copy,
    )
    return match, len(syndrome) + workspace, syndrome_gates + equality_gates


def causal_certificate(
    word: tuple[int, ...],
    expected: tuple[int, ...],
    *,
    deleted_stage: int | None = None,
) -> tuple[int, int, int]:
    """Fresh-stage certificate: q_(i+1) ^= q_i AND [word_i=expected_i]."""

    if len(word) != len(expected) or not word:
        raise ValueError("certificate words must have equal nonzero width")
    if set(word) - {0, 1} or set(expected) - {0, 1}:
        raise ValueError("certificate words must be binary")
    width = len(word)
    base = width
    state = list(word) + [1] + [0] * width
    gates: list[Gate] = []
    stage_gate_indices = []
    for index, value in enumerate(expected):
        if value == 0:
            gates.append(Gate("X", (), index))
        stage_gate_indices.append(len(gates))
        gates.append(Gate("TOFFOLI", (base + index, index), base + index + 1))
        if value == 0:
            gates.append(Gate("X", (), index))
    deletion = (
        stage_gate_indices[deleted_stage]
        if deleted_stage is not None
        else None
    )
    output = execute(state, tuple(gates), deletion)
    return output[base + width], width + 1, len(gates)


@dataclass(frozen=True)
class IdentityWord:
    stable_label: tuple[object, ...]
    label_bits: tuple[int, ...]
    support_bits: tuple[int, ...]
    word: tuple[int, ...]


@dataclass(frozen=True)
class SupportFixture:
    length: int
    words: tuple[IdentityWord, ...]
    supports: tuple[frozenset[int], ...]
    executions: tuple[tuple[int, ...], ...]
    signatures: tuple[frozenset[tuple[int, int]], ...]
    predecessors: tuple[int, ...]
    union_size: int
    covariance_failures: int


def selected_blocks(model) -> tuple[object, ...]:
    length = model.length
    coins = c314.c312.local_blocks(model, "coin")
    edges = c314.c312.local_blocks(model, "edge")
    blocks = [
        next(block for block in coins if block.label == cell)
        for cell in ((0, 0, 0), (0, 0, 1), (1, 1, 1))
    ]
    endpoint_pairs = (
        (((0, 0, 0), 0), ((length - 1, 0, 0), 1)),
        (((0, 0, 1), 2), ((0, length - 1, 1), 3)),
    )
    for endpoints in endpoint_pairs:
        label = tuple(
            sorted(
                index
                for index, vertex in enumerate(model.code.graph.vertices)
                if vertex in endpoints
            )
        )
        blocks.append(next(block for block in edges if block.label == label))
    return tuple(blocks)


def mode_map(model, frame: np.ndarray, mode: int) -> int:
    cell, direction = model.code.graph.vertices[mode]
    rotated_cell = tuple(int(value) % model.length for value in frame @ np.asarray(cell))
    dmap = c314.c311.c235.direction_map(frame)
    return model.code.graph.vertex_index[(rotated_cell, dmap[direction])]


def transformed_block(model, block, frame: np.ndarray):
    coins = c314.c312.local_blocks(model, "coin")
    edges = c314.c312.local_blocks(model, "edge")
    if block.kind == "coin":
        label = tuple(int(value) % model.length for value in frame @ np.asarray(block.label))
        return next(candidate for candidate in coins if candidate.label == label)
    label = tuple(sorted(mode_map(model, frame, mode) for mode in block.label))
    return next(candidate for candidate in edges if candidate.label == label)


def stable_label_bits(model, block) -> tuple[tuple[object, ...], tuple[int, ...]]:
    catalog = c314.c312.local_blocks(model, block.kind)
    local_index = next(
        index for index, candidate in enumerate(catalog) if candidate.label == block.label
    )
    kind = int(block.kind == "edge")
    if block.kind == "edge":
        payload = integer_bits(block.label[0], MODE_BITS) + integer_bits(
            block.label[1], MODE_BITS
        )
    else:
        cell_index = sum(
            block.label[axis] * model.length ** (2 - axis)
            for axis in range(3)
        )
        payload = integer_bits(cell_index, MODE_BITS) + (0,) * MODE_BITS
    label = (block.kind, local_index, block.label)
    return label, (kind,) + integer_bits(local_index, INDEX_BITS) + payload


def build_fixture(
    length: int,
    frame: np.ndarray | None = None,
) -> SupportFixture:
    if length not in (3, 6):
        raise ValueError("Cycle-329 fixture is declared only at L=3 and held L=6")
    model = c314.c312.c307.build_model(length)
    blocks = selected_blocks(model)
    covariance_failures = 0
    if frame is not None:
        original = blocks
        blocks = tuple(transformed_block(model, block, frame) for block in original)
    supports = tuple(
        frozenset(c314.c312.block_mode_support(model, block))
        for block in blocks
    )
    if frame is not None:
        for original, support in zip(selected_blocks(model), supports):
            mapped = frozenset(mode_map(model, frame, mode) for mode in c314.c312.block_mode_support(model, original))
            covariance_failures += mapped != support
    universe = tuple(sorted(set().union(*supports)))
    if len(universe) > MAX_SUPPORT_FLAGS:
        raise ValueError("bounded local support alphabet exceeded")
    position = {mode: index for index, mode in enumerate(universe)}
    words = []
    for block, support in zip(blocks, supports):
        label, label_bits = stable_label_bits(model, block)
        support_bits = tuple(int(mode in support) for mode in universe) + (
            0,
        ) * (MAX_SUPPORT_FLAGS - len(universe))
        words.append(
            IdentityWord(
                label,
                label_bits,
                support_bits,
                label_bits + support_bits,
            )
        )
    support_map = {index: supports[index] for index in range(len(supports))}
    initial = tuple(range(len(supports)))
    executions = {initial}
    queue = deque((initial,))
    while queue:
        execution = queue.popleft()
        for location in range(len(execution) - 1):
            left, right = execution[location : location + 2]
            if supports[left] & supports[right]:
                continue
            swapped = list(execution)
            swapped[location], swapped[location + 1] = swapped[location + 1], swapped[location]
            swapped = tuple(swapped)
            if swapped not in executions:
                executions.add(swapped)
                queue.append(swapped)
    ordered = tuple(sorted(executions))
    signatures = tuple(c314.reachability_signature(row, support_map) for row in ordered)
    target = 4
    predecessors = tuple(
        left for left, right in sorted(signatures[0]) if right == target
    )
    return SupportFixture(
        length,
        tuple(words),
        supports,
        ordered,
        signatures,
        predecessors,
        len(universe),
        covariance_failures,
    )


def route_outputs(
    fixture: SupportFixture,
    route: str,
    target_word: tuple[int, ...] | None = None,
    predecessor_words: tuple[tuple[int, ...], ...] | None = None,
    closed: tuple[int, ...] = (1, 1, 1),
    delete_target: bool = False,
    delete_readiness: bool = False,
) -> tuple[int, int]:
    target_expected = fixture.words[4].word
    target_word = target_word or target_expected
    predecessor_expected = tuple(fixture.words[index].word for index in fixture.predecessors)
    predecessor_words = predecessor_words or predecessor_expected
    if len(predecessor_words) != 3 or len(closed) != 3:
        raise ValueError("Cycle-329 target has exactly three predecessor slots")
    if route == "direct":
        matcher = equality_circuit(
            target_word,
            target_expected,
            delete_copy=delete_target,
        )[0]
        matches = tuple(
            equality_circuit(observed, expected)[0]
            for observed, expected in zip(predecessor_words, predecessor_expected)
        )
        readiness_word = tuple(
            value
            for pair in zip(matches, closed)
            for value in pair
        )
        readiness = equality_circuit(
            readiness_word,
            (1,) * 6,
            delete_copy=delete_readiness,
        )[0]
    elif route == "syndrome":
        matcher = syndrome_compare(
            target_word,
            target_expected,
            delete_copy=delete_target,
        )[0]
        matches = tuple(
            syndrome_compare(observed, expected)[0]
            for observed, expected in zip(predecessor_words, predecessor_expected)
        )
        readiness_word = tuple(
            value
            for pair in zip(matches, closed)
            for value in pair
        )
        readiness = equality_circuit(
            readiness_word,
            (1,) * 6,
            delete_copy=delete_readiness,
        )[0]
    elif route == "certificate":
        matcher = causal_certificate(
            target_word,
            target_expected,
            deleted_stage=0 if delete_target else None,
        )[0]
        matches = tuple(
            causal_certificate(observed, expected)[0]
            for observed, expected in zip(predecessor_words, predecessor_expected)
        )
        readiness_word = tuple(
            value
            for pair in zip(matches, closed)
            for value in pair
        )
        readiness = causal_certificate(
            readiness_word,
            (1,) * 6,
            deleted_stage=0 if delete_readiness else None,
        )[0]
    else:
        raise ValueError(route)
    return matcher, readiness


def source_and_fixture_controls() -> dict[int, SupportFixture]:
    rows = []
    fixtures = {}
    for length in (3, 6):
        fixture = build_fixture(length)
        fixtures[length] = fixture
        sidecar = c314.build_event_sidecar(c314.c311.c269.build_code(length))
        fock = sidecar.event_encoding @ c314.c311.fock_input_embedding()
        streamed = c314.apply_mapping(sidecar.stream_mapping, fock)
        h_values = np.tile(np.asarray((0, 1), dtype=float), len(sidecar.base_encoding))
        reads = np.asarray(
            [
                np.vdot(streamed[:, column], h_values * streamed[:, column]).real
                for column in range(streamed.shape[1])
            ]
        )
        expected = np.asarray(
            [0 if number == 0 else 1 for number, _label in c314.c311.FOCK_LABELS]
        )
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "event_residual": float(np.linalg.norm(reads - expected)),
                "union_support_flags": fixture.union_size,
                "word_width": len(fixture.words[0].word),
                "executions": len(fixture.executions),
                "signatures": len(set(fixture.signatures)),
                "predecessors": fixture.predecessors,
                "target_support": len(fixture.supports[4]),
            }
        )
    check(
        "the exact Cycle-314 event source and common-support dependency fixture close at trained L=3 and held L=6",
        all(
            row["event_residual"] < TOL
            and row["union_support_flags"] <= MAX_SUPPORT_FLAGS
            and row["word_width"] == WORD_WIDTH
            and row["executions"] == 3
            and row["signatures"] == 1
            and row["predecessors"] == (0, 1, 2)
            for row in rows
        ),
        rows,
    )
    return fixtures


def direct_route_controls(fixtures: dict[int, SupportFixture]) -> dict[str, object]:
    false_positives = false_negatives = corruption_false_positives = 0
    predecessor_splice_survivors = predecessor_corruption_survivors = 0
    missing_rows = []
    for fixture in fixtures.values():
        lawful = route_outputs(fixture, "direct")
        false_negatives += lawful != (1, 1)
        for index in range(4):
            false_positives += route_outputs(
                fixture,
                "direct",
                target_word=fixture.words[index].word,
            )[0]
        target = fixture.words[4]
        for label_index, support_index in product(range(5), repeat=2):
            if (label_index, support_index) == (4, 4):
                continue
            splice = (
                fixture.words[label_index].label_bits
                + fixture.words[support_index].support_bits
            )
            false_positives += route_outputs(
                fixture,
                "direct",
                target_word=splice,
            )[0]
        for bit in range(LABEL_BITS, WORD_WIDTH):
            corrupted = list(target.word)
            corrupted[bit] ^= 1
            corruption_false_positives += route_outputs(
                fixture,
                "direct",
                target_word=tuple(corrupted),
            )[0]
        lawful_predecessors = tuple(
            fixture.words[index].word for index in fixture.predecessors
        )
        for slot, expected_index in enumerate(fixture.predecessors):
            for other_index in range(5):
                if other_index == expected_index:
                    continue
                spliced = list(lawful_predecessors)
                spliced[slot] = fixture.words[other_index].word
                predecessor_splice_survivors += route_outputs(
                    fixture,
                    "direct",
                    predecessor_words=tuple(spliced),
                )[1]
            for bit in range(LABEL_BITS, WORD_WIDTH):
                corrupted_word = list(lawful_predecessors[slot])
                corrupted_word[bit] ^= 1
                corrupted = list(lawful_predecessors)
                corrupted[slot] = tuple(corrupted_word)
                predecessor_corruption_survivors += route_outputs(
                    fixture,
                    "direct",
                    predecessor_words=tuple(corrupted),
                )[1]
        for missing in range(3):
            closed = tuple(int(index != missing) for index in range(3))
            output = route_outputs(fixture, "direct", closed=closed)
            missing_rows.append((fixture.length, missing, output))
    deleted = {
        "matcher_copy": route_outputs(fixtures[3], "direct", delete_target=True),
        "readiness_copy": route_outputs(fixtures[3], "direct", delete_readiness=True),
    }
    direct_overhead = 4 * WORD_WIDTH + 4 * WORD_WIDTH + 3 + 6
    detail = {
        "word_width": WORD_WIDTH,
        "false_positives": false_positives,
        "false_negatives": false_negatives,
        "support_corruption_false_positives": corruption_false_positives,
        "predecessor_splice_readiness_survivors": predecessor_splice_survivors,
        "predecessor_corruption_readiness_survivors": predecessor_corruption_survivors,
        "missing_predecessors": missing_rows,
        "deletions": deleted,
        "comparator_receiver_M2": direct_overhead,
        "integrated_Cycle326_M2": direct_overhead + 4,
        "conservative_source_plus_receiver_M2": SOURCE_PATCH_M2 + direct_overhead + 4,
        "maximum_primitive_gate_support_M2": 3,
    }
    check(
        "route 1 directly compares stable labels and bounded support flags and derives three-predecessor readiness with no host conjunction",
        false_positives == 0
        and false_negatives == 0
        and corruption_false_positives == 0
        and predecessor_splice_survivors == 0
        and predecessor_corruption_survivors == 0
        and all(output == (1, 0) for _length, _missing, output in missing_rows)
        and deleted["matcher_copy"] == (0, 1)
        and deleted["readiness_copy"] == (1, 0)
        and direct_overhead == 1089,
        detail,
    )
    return detail


def syndrome_route_controls(fixtures: dict[int, SupportFixture]) -> dict[str, object]:
    false_positives = false_negatives = single_faults = swap_faults = 0
    predecessor_splice_survivors = predecessor_corruption_survivors = 0
    signature_rows = []
    for fixture in fixtures.values():
        false_negatives += route_outputs(fixture, "syndrome") != (1, 1)
        signatures = tuple(syndrome_circuit(word.word)[0] for word in fixture.words)
        signature_rows.append((fixture.length, len(signatures[0]), len(set(signatures))))
        target = fixture.words[4]
        expected_signature = signatures[4]
        for label_index, support_index in product(range(5), repeat=2):
            if (label_index, support_index) == (4, 4):
                continue
            splice = fixture.words[label_index].label_bits + fixture.words[support_index].support_bits
            false_positives += syndrome_circuit(splice)[0] == expected_signature
        for bit in range(LABEL_BITS, WORD_WIDTH):
            corrupted = list(target.word)
            corrupted[bit] ^= 1
            single_faults += syndrome_circuit(tuple(corrupted))[0] == expected_signature
        occupied = [
            LABEL_BITS + index
            for index, value in enumerate(target.support_bits)
            if value
        ]
        blank = [
            LABEL_BITS + index
            for index, value in enumerate(target.support_bits)
            if not value
        ]
        for left, right in product(occupied, blank):
            corrupted = list(target.word)
            corrupted[left] ^= 1
            corrupted[right] ^= 1
            swap_faults += syndrome_circuit(tuple(corrupted))[0] == expected_signature
        lawful_predecessors = tuple(
            fixture.words[index].word for index in fixture.predecessors
        )
        for slot, expected_index in enumerate(fixture.predecessors):
            for other_index in range(5):
                if other_index == expected_index:
                    continue
                spliced = list(lawful_predecessors)
                spliced[slot] = fixture.words[other_index].word
                predecessor_splice_survivors += route_outputs(
                    fixture,
                    "syndrome",
                    predecessor_words=tuple(spliced),
                )[1]
            for bit in range(LABEL_BITS, WORD_WIDTH):
                corrupted_word = list(lawful_predecessors[slot])
                corrupted_word[bit] ^= 1
                corrupted = list(lawful_predecessors)
                corrupted[slot] = tuple(corrupted_word)
                predecessor_corruption_survivors += route_outputs(
                    fixture,
                    "syndrome",
                    predecessor_words=tuple(corrupted),
                )[1]
    missing = tuple(
        route_outputs(fixtures[6], "syndrome", closed=tuple(int(i != miss) for i in range(3)))
        for miss in range(3)
    )
    deleted = {
        "matcher_copy": route_outputs(fixtures[3], "syndrome", delete_target=True),
        "readiness_copy": route_outputs(fixtures[3], "syndrome", delete_readiness=True),
    }
    syndrome_width = len(syndrome_circuit(fixtures[3].words[4].word)[0])
    overhead = 4 * WORD_WIDTH + 8 * syndrome_width + 3 + 6
    detail = {
        "signature_rows": signature_rows,
        "mixed_splice_false_positives": false_positives,
        "false_negatives": false_negatives,
        "single_support_fault_false_positives": single_faults,
        "support_delete_insert_false_positives": swap_faults,
        "predecessor_splice_readiness_survivors": predecessor_splice_survivors,
        "predecessor_corruption_readiness_survivors": predecessor_corruption_survivors,
        "missing_predecessors": missing,
        "deletions": deleted,
        "comparator_receiver_M2": overhead,
        "integrated_Cycle326_M2": overhead + 4,
        "conservative_source_plus_receiver_M2": SOURCE_PATCH_M2 + overhead + 4,
        "maximum_primitive_gate_support_M2": 3,
    }
    check(
        "route 2 uses a nine-bit relational Hamming syndrome to reject actual anti-splices and support faults and derive readiness",
        signature_rows == [(3, 9, 5), (6, 9, 5)]
        and false_positives == false_negatives == single_faults == swap_faults == 0
        and predecessor_splice_survivors == 0
        and predecessor_corruption_survivors == 0
        and missing == ((1, 0),) * 3
        and deleted["matcher_copy"] == (0, 1)
        and deleted["readiness_copy"] == (1, 0)
        and overhead == 621,
        detail,
    )
    return detail


def certificate_route_controls(fixtures: dict[int, SupportFixture]) -> dict[str, object]:
    false_positives = false_negatives = deleted_stage_survivors = 0
    support_corruption_survivors = predecessor_splice_survivors = 0
    stage_rows = []
    for fixture in fixtures.values():
        false_negatives += route_outputs(fixture, "certificate") != (1, 1)
        target = fixture.words[4]
        for index in range(4):
            false_positives += route_outputs(
                fixture,
                "certificate",
                target_word=fixture.words[index].word,
            )[0]
        for bit in range(LABEL_BITS, WORD_WIDTH):
            corrupted = list(target.word)
            corrupted[bit] ^= 1
            support_corruption_survivors += route_outputs(
                fixture,
                "certificate",
                target_word=tuple(corrupted),
            )[0]
        lawful_predecessors = tuple(
            fixture.words[index].word for index in fixture.predecessors
        )
        for slot, expected_index in enumerate(fixture.predecessors):
            for other_index in range(5):
                if other_index == expected_index:
                    continue
                spliced = list(lawful_predecessors)
                spliced[slot] = fixture.words[other_index].word
                predecessor_splice_survivors += route_outputs(
                    fixture,
                    "certificate",
                    predecessor_words=tuple(spliced),
                )[1]
        for stage in range(WORD_WIDTH):
            output = causal_certificate(target.word, target.word, deleted_stage=stage)[0]
            deleted_stage_survivors += output
        stage_rows.append((fixture.length, WORD_WIDTH, deleted_stage_survivors))
    missing = tuple(
        route_outputs(fixtures[6], "certificate", closed=tuple(int(i != miss) for i in range(3)))
        for miss in range(3)
    )
    deleted = {
        "target_stage": route_outputs(fixtures[3], "certificate", delete_target=True),
        "readiness_stage": route_outputs(fixtures[3], "certificate", delete_readiness=True),
    }
    overhead = 4 * WORD_WIDTH + 4 * (WORD_WIDTH + 1) + 3 + 7
    detail = {
        "stage_rows": stage_rows,
        "anti_splice_false_positives": false_positives,
        "false_negatives": false_negatives,
        "support_corruption_survivors": support_corruption_survivors,
        "predecessor_splice_readiness_survivors": predecessor_splice_survivors,
        "deleted_stage_survivors": deleted_stage_survivors,
        "missing_predecessors": missing,
        "deletions": deleted,
        "comparator_receiver_M2": overhead,
        "integrated_Cycle326_M2": overhead + 4,
        "conservative_source_plus_receiver_M2": SOURCE_PATCH_M2 + overhead + 4,
        "maximum_primitive_gate_support_M2": 3,
    }
    check(
        "route 3 propagates fresh local causal certificates through every identity bit and into the Cycle-326 receiver",
        false_positives == false_negatives == deleted_stage_survivors == 0
        and support_corruption_survivors == predecessor_splice_survivors == 0
        and missing == ((1, 0),) * 3
        and deleted["target_stage"] == (0, 1)
        and deleted["readiness_stage"] == (1, 0)
        and overhead == 1094,
        detail,
    )
    return detail


def schedule_frame_and_receiver_controls() -> dict[str, object]:
    schedule_rows = []
    for length in (3, 6):
        fixture = build_fixture(length)
        outputs = {
            route: {
                (
                    fixture.words[4].stable_label,
                    fixture.predecessors,
                    route_outputs(fixture, route),
                    signature,
                )
                for signature in fixture.signatures
            }
            for route in ("direct", "syndrome", "certificate")
        }
        schedule_rows.append(
            {
                "L": length,
                "executions": len(fixture.executions),
                "positions": tuple(sorted({row.index(4) for row in fixture.executions})),
                "route_outputs": {key: len(value) for key, value in outputs.items()},
            }
        )
    frame_failures = covariance_failures = 0
    frame_rows = []
    for length in (3, 6):
        for frame in c314.c311.c235.proper_cubic_frames():
            fixture = build_fixture(length, frame)
            covariance_failures += fixture.covariance_failures
            outputs = tuple(
                route_outputs(fixture, route)
                for route in ("direct", "syndrome", "certificate")
            )
            frame_failures += outputs != ((1, 1),) * 3
            frame_rows.append((length, fixture.union_size, outputs))
    receiver = {}
    fixture = build_fixture(3)
    for route in ("direct", "syndrome", "certificate"):
        match, ready = route_outputs(fixture, route)
        lawful = c326.run_local_close(
            event_ready=1,
            identity_match=match,
            dependencies_ready=ready,
            occurrence=1,
            close_law=1,
        )
        no_occurrence = c326.run_local_close(
            event_ready=1,
            identity_match=match,
            dependencies_ready=ready,
            occurrence=0,
            close_law=1,
        )
        no_close = c326.run_local_close(
            event_ready=1,
            identity_match=match,
            dependencies_ready=ready,
            occurrence=1,
            close_law=0,
        )
        receiver[route] = (lawful, no_occurrence, no_close)
    detail = {
        "schedule_rows": schedule_rows,
        "frame_cases": len(frame_rows),
        "frame_failures": frame_failures,
        "support_covariance_failures": covariance_failures,
        "Cycle326_receiver": receiver,
    }
    check(
        "all routes respect the schedule quotient, held size, 24 frames, and the separation of match/readiness from occurrence and close",
        all(
            row["executions"] == 3
            and row["positions"] == (3, 4)
            and set(row["route_outputs"].values()) == {1}
            for row in schedule_rows
        )
        and len(frame_rows) == 48
        and frame_failures == covariance_failures == 0
        and all(
            lawful == (0, 1)
            and no_occurrence == no_close == (1, 0)
            for lawful, no_occurrence, no_close in receiver.values()
        ),
        detail,
    )
    return detail


def domain_and_inventory_controls() -> None:
    rejected = 0
    invalid = (
        lambda: build_fixture(2),
        lambda: build_fixture(7),
        lambda: equality_circuit((), ()),
        lambda: equality_circuit((0,), (0, 1)),
        lambda: equality_circuit((2,), (1,)),
        lambda: syndrome_circuit(()),
        lambda: causal_certificate((0,), (0, 1)),
        lambda: route_outputs(build_fixture(3), "host-conjunction"),
        lambda: route_outputs(build_fixture(3), "direct", closed=(1, 1)),
    )
    for call in invalid:
        try:
            call()
        except ValueError:
            rejected += 1
    inventory = {
        "derived": (
            "stable-label/support match bit",
            "three-predecessor readiness bit",
            "bounded anti-splice certificate",
        ),
        "supplied_separate": (
            "event-ready h",
            "individual predecessor-closed flags",
            "fixed comparator program and placement",
            "occurrence",
            "close law",
            "fresh capacity",
            "Record typing",
            "permanence",
            "matcher-to-clock",
            "calibration",
        ),
    }
    text = normalized(NOTE)
    check(
        "lawful domains and the supplied-versus-derived inventory remain explicit",
        rejected == len(invalid)
        and "derived match is not occurrence" in text
        and "commit candidate is not a record" in text
        and "occurrence remains separate" in text
        and "permanence remains separate" in text,
        {"rejected": rejected, "attempted": len(invalid), "inventory": inventory},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    fixtures = source_and_fixture_controls()
    direct = direct_route_controls(fixtures)
    syndrome = syndrome_route_controls(fixtures)
    certificate = certificate_route_controls(fixtures)
    schedule_frame_and_receiver_controls()
    domain_and_inventory_controls()
    check(
        "Cycle 329 derives physical matcher and readiness controls by three bounded routes without promoting them to occurrence or Record",
        direct["false_positives"] == 0
        and syndrome["mixed_splice_false_positives"] == 0
        and certificate["anti_splice_false_positives"] == 0
        and "broad gate status: fail / do not ship" in normalized(NOTE)
        and "no axiom pressure" in normalized(NOTE),
        {
            "direct": "positive",
            "syndrome": "positive",
            "certificate": "positive",
        },
    )
    print("DATA direct", direct)
    print("DATA syndrome", syndrome)
    print("DATA certificate", certificate)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE329_PHYSICAL_MATCHER_READINESS_GREEN"
        if FAIL == 0
        else "CYCLE329_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
