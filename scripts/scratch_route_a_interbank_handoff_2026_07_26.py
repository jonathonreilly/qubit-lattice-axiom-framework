#!/usr/bin/env python3
"""Scratch Route-A extension: local reversible handoff between packet banks.

This probe attacks the finite two-cell exhaustion wall left by the recurrent
directional packet-bank construction.  A fixed local word transfers the
one-hot allocator token plus its head/rotor state from a full bank into a
neighboring blank bank.  The packet append then uses the unchanged Route-A
word.  No cycle, retention, Record, time, Born, source, or no-go claim is made.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import scratch_route_a_recurrent_directional_packet_bank_2026_07_26 as A


TOL = 4.0e-10
LEFT = 0
RIGHT = A.N
LATCH = 2 * A.N
# Complete bank-work and event hygiene raises the largest predicate to 184
# controls; 190 link-work bits leave a small explicit constant-size margin.
LINK_WORK = tuple(range(LATCH + 1, LATCH + 191))
N_LINK = LINK_WORK[-1] + 1


def off(gate: A.Gate, base: int) -> A.Gate:
    return A.Gate(gate.kind, tuple(base + wire for wire in gate.wires))


def q(base: int, wire: int) -> int:
    return base + wire


def controlled_latch(
    positives: tuple[int, ...], negatives: tuple[int, ...]
) -> tuple[A.Gate, ...]:
    word: list[A.Gate] = []
    word.extend(A.x(wire) for wire in negatives)
    word.extend(A.mcx(positives + negatives, LATCH, LINK_WORK))
    word.extend(A.x(wire) for wire in reversed(negatives))
    return tuple(word)


def fredkin(control: int, left: int, right: int) -> tuple[A.Gate, ...]:
    return (A.cn(right, left), A.tof(control, left, right), A.cn(right, left))


def handoff_word(left: int = LEFT, right: int = RIGHT) -> tuple[A.Gate, ...]:
    """Full-left/blank-right token+head+rotor transfer with clean latch."""
    left_full = (
        q(left, A.TOKEN[0]),
        q(left, A.FRESH[0]), q(left, A.FRESH[1]),
        q(left, int(A.CELLS[0]["valid"])),
        q(left, int(A.CELLS[1]["valid"])),
        q(left, A.POINTER), q(left, A.DIRECTION_OK),
        q(left, A.BINDER), q(left, A.ACTUAL),
        q(left, A.ADMISS), q(left, A.LAW),
        q(right, A.BINDER), q(right, A.ACTUAL),
        q(right, A.ADMISS), q(right, A.LAW),
    )
    right_blank = tuple(q(right, wire) for layout in A.CELLS for wire in layout["payload"])
    pre_negative = right_blank + tuple(q(right, wire) for wire in (
        *A.FRESH, *A.TOKEN, *A.HEAD, *A.ROTOR, *A.ZERO_WORK, A.TOKEN_OK,
        A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
    )) + tuple(q(left, wire) for wire in (
        A.TOKEN[1], *A.ZERO_WORK, A.TOKEN_OK,
    ))
    pre = controlled_latch(left_full, pre_negative)

    swaps: list[A.Gate] = []
    for left_wire, right_wire in (
        (q(left, A.TOKEN[0]), q(right, A.TOKEN[0])),
        *((q(left, wire), q(right, wire)) for wire in (*A.HEAD, *A.ROTOR)),
        *((q(left, wire), q(right, wire)) for wire in (
            A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
        )),
    ):
        swaps.extend(fredkin(LATCH, left_wire, right_wire))

    post_full = (
        q(right, A.TOKEN[0]),
        q(left, A.FRESH[0]), q(left, A.FRESH[1]),
        q(left, int(A.CELLS[0]["valid"])),
        q(left, int(A.CELLS[1]["valid"])),
        q(right, A.POINTER), q(right, A.DIRECTION_OK),
        q(left, A.BINDER), q(left, A.ACTUAL),
        q(left, A.ADMISS), q(left, A.LAW),
        q(right, A.BINDER), q(right, A.ACTUAL),
        q(right, A.ADMISS), q(right, A.LAW),
    )
    post_negative = right_blank + tuple(q(right, wire) for wire in (
        *A.FRESH, A.TOKEN[1], *A.ZERO_WORK, A.TOKEN_OK,
    )) + tuple(q(left, wire) for wire in (
        *A.TOKEN, *A.HEAD, *A.ROTOR, *A.ZERO_WORK,
        A.TOKEN_OK, A.DIRECTION_OK, A.POINTER, A.U_TO_V, A.V_TO_U,
    ))
    post = controlled_latch(post_full, post_negative)
    return pre + tuple(swaps) + post


def link_input(left_bank: tuple[int, ...], right_bank: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left_bank) + tuple(right_bank) + (0,) * (N_LINK - 2 * A.N)


def inactive_bank() -> tuple[int, ...]:
    return A.initial_bank(head=0, rotor=0, token=(0, 0))


def full_bank(rotor: int = 14) -> tuple[int, ...]:
    state = A.initial_bank(rotor=rotor)
    state = A.combined_step(state, (1, 0))
    state = A.combined_step(state, (0, 1))
    return state


def inactive_occupied_bank() -> tuple[int, ...]:
    state = list(A.combined_step(A.initial_bank(), (1, 0)))
    for wire in (*A.TOKEN, *A.HEAD, *A.ROTOR):
        state[wire] = 0
    return tuple(state)


def handoff_certificate() -> dict[str, object]:
    word = handoff_word()
    inverse = tuple(reversed(word))
    before = link_input(event_ready_bank(full_bank()), inactive_bank())
    after = A.apply_semantic(before, word)
    left = after[:A.N]
    right = after[A.N:2 * A.N]
    expected = {
        "left_token": (0, 0),
        "right_token": (1, 0),
        "left_head": 0,
        "right_head": 1,
        "left_rotor": 0,
        "right_rotor": 0,
    }
    observed = {
        "left_token": tuple(left[wire] for wire in A.TOKEN),
        "right_token": tuple(right[wire] for wire in A.TOKEN),
        "left_head": A.integer(left, A.HEAD),
        "right_head": A.integer(right, A.HEAD),
        "left_rotor": A.integer(left, A.ROTOR),
        "right_rotor": A.integer(right, A.ROTOR),
    }
    rng = np.random.default_rng(717)
    arbitrary_inverse_failures = 0
    for _ in range(256):
        row = tuple(int(value) for value in rng.integers(0, 2, size=N_LINK))
        arbitrary_inverse_failures += A.apply_semantic(A.apply_semantic(row, word), inverse) != row

    controls = {}
    mutations = {
        "left_not_full": A.combined_step(A.initial_bank(), (1, 0)),
        "right_occupied": inactive_occupied_bank(),
        "right_token_dirty": list(inactive_bank()),
        "right_payload_dirty": list(inactive_bank()),
        "left_token_dirty": list(full_bank()),
        "left_no_endpoint_event": full_bank(),
        "left_binder_zero": list(full_bank()),
        "left_actual_zero": list(full_bank()),
        "left_admiss_zero": list(full_bank()),
        "left_law_zero": list(full_bank()),
        "right_binder_zero": list(inactive_bank()),
        "right_actual_zero": list(inactive_bank()),
        "right_admiss_zero": list(inactive_bank()),
        "right_law_zero": list(inactive_bank()),
        "right_bank_work_dirty": list(inactive_bank()),
        "left_bank_work_dirty": list(full_bank()),
    }
    mutations["right_token_dirty"][A.TOKEN[1]] = 1
    mutations["right_payload_dirty"][0] = 1
    mutations["left_token_dirty"][A.TOKEN[1]] = 1
    mutations["left_binder_zero"][A.BINDER] = 0
    mutations["left_actual_zero"][A.ACTUAL] = 0
    mutations["left_admiss_zero"][A.ADMISS] = 0
    mutations["left_law_zero"][A.LAW] = 0
    mutations["right_binder_zero"][A.BINDER] = 0
    mutations["right_actual_zero"][A.ACTUAL] = 0
    mutations["right_admiss_zero"][A.ADMISS] = 0
    mutations["right_law_zero"][A.LAW] = 0
    mutations["right_bank_work_dirty"][A.ZERO_WORK[7]] = 1
    mutations["left_bank_work_dirty"][A.ZERO_WORK[9]] = 1
    for label, bank in mutations.items():
        if label.startswith("left_"):
            left = tuple(bank)
            if label != "left_no_endpoint_event":
                left = event_ready_bank(left)
            hostile = link_input(left, inactive_bank())
        else:
            hostile = link_input(event_ready_bank(full_bank()), tuple(bank))
        controls[label] = A.apply_semantic(hostile, word) == hostile

    deletion_word = tuple(gate for index, gate in enumerate(word) if index != 0)
    deletion_detected = A.apply_semantic(before, deletion_word) != after
    return {
        "semantic_matches": observed == expected,
        "observed": observed,
        "expected": expected,
        "clean_latch_and_work": not any(after[2 * A.N:]),
        "exact_inverse": A.apply_semantic(after, inverse) == before,
        "arbitrary_inverse_cases": 256,
        "arbitrary_inverse_failures": arbitrary_inverse_failures,
        "hostile_controls": controls,
        "logical_gates": len(word),
        "deletion_detected": deletion_detected,
    }


def composed_handoff_append_certificate() -> dict[str, object]:
    left = A.set_interface(full_bank(), 1, 1, 0)
    right = inactive_bank()
    before = link_input(left, right)
    direction_in = tuple(off(gate, LEFT) for gate in direction_witness_word())
    direction_out = tuple(off(gate, RIGHT) for gate in reversed(direction_witness_word()))
    combined = (
        direction_in
        + handoff_word()
        + tuple(off(gate, RIGHT) for gate in packet_word_for_bank(1))
        + direction_out
    )
    after = A.apply_semantic(before, combined)
    left_after = after[:A.N]
    right_after = after[A.N:2 * A.N]
    packet = A.packet_projection(right_after, 0)
    return {
        "left_token": tuple(left_after[wire] for wire in A.TOKEN),
        "right_token": tuple(right_after[wire] for wire in A.TOKEN),
        "packet": packet,
        "head": A.integer(right_after, A.HEAD),
        "rotor": A.integer(right_after, A.ROTOR),
        "clean_link_work": not any(after[2 * A.N:]),
        "exact_inverse": A.apply_semantic(after, tuple(reversed(combined))) == before,
        "pass": tuple(left_after[wire] for wire in A.TOKEN) == (0, 0)
        and tuple(right_after[wire] for wire in A.TOKEN) == (0, 1)
        and packet is not None
        and packet["predecessor"] == 1
        and packet["identity"] == 0
        and A.integer(right_after, A.HEAD) == 2
        and A.integer(right_after, A.ROTOR) == 1
        and not any(after[2 * A.N:])
        and A.apply_semantic(after, tuple(reversed(combined))) == before,
    }


def deletion_certificate() -> dict[str, dict[str, object]]:
    # Use a nonzero post-fill rotor so the rotor-transfer deletion is active.
    left = A.set_interface(full_bank(rotor=12), 1, 1, 0)
    right = inactive_bank()
    before = link_input(left, right)
    direction = tuple(off(gate, LEFT) for gate in direction_witness_word())
    handoff = handoff_word()
    packet = tuple(off(gate, RIGHT) for gate in safe_packet_body_word())
    prefix = tuple(off(gate, RIGHT) for gate in structural_prefix_word(1))
    cleanup = tuple(off(gate, RIGHT) for gate in reversed(direction_witness_word()))
    complete = direction + handoff + packet + prefix + cleanup
    expected = A.apply_semantic(before, complete)

    left_full = (
        q(LEFT, A.TOKEN[0]),
        q(LEFT, A.FRESH[0]), q(LEFT, A.FRESH[1]),
        q(LEFT, int(A.CELLS[0]["valid"])),
        q(LEFT, int(A.CELLS[1]["valid"])),
        q(LEFT, A.POINTER), q(LEFT, A.DIRECTION_OK),
        q(LEFT, A.BINDER), q(LEFT, A.ACTUAL),
        q(LEFT, A.ADMISS), q(LEFT, A.LAW),
        q(RIGHT, A.BINDER), q(RIGHT, A.ACTUAL),
        q(RIGHT, A.ADMISS), q(RIGHT, A.LAW),
    )
    right_blank = tuple(q(RIGHT, wire) for layout in A.CELLS for wire in layout["payload"])
    pre_negative = right_blank + tuple(q(RIGHT, wire) for wire in (
        *A.FRESH, *A.TOKEN, *A.HEAD, *A.ROTOR, *A.ZERO_WORK, A.TOKEN_OK,
        A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
    )) + tuple(q(LEFT, wire) for wire in (
        A.TOKEN[1], *A.ZERO_WORK, A.TOKEN_OK,
    ))
    pre_length = len(controlled_latch(left_full, pre_negative))
    variants = {
        "whole_handoff": direction + packet + prefix + cleanup,
        "token_transfer": direction + handoff[:pre_length] + handoff[pre_length + 3:] + packet + prefix + cleanup,
        "head_transfer": direction + handoff[:pre_length + 3] + handoff[pre_length + 6:] + packet + prefix + cleanup,
        "rotor_transfer": direction + handoff[:pre_length + 24] + handoff[pre_length + 27:] + packet + prefix + cleanup,
        "structural_address_prefix": direction + handoff + packet + cleanup,
        "next_bank_packet": direction + handoff + prefix + cleanup,
    }
    report = {}
    for label, variant in variants.items():
        observed = A.apply_semantic(before, variant)
        different = sum(left_bit != right_bit for left_bit, right_bit in zip(observed, expected))
        report[label] = {
            "different_bits": different,
            "basis_state_norm_residual": float(np.sqrt(2.0)) if different else 0.0,
        }
    return report


def apply_boundary(
    banks: tuple[tuple[int, ...], ...], left_index: int
) -> tuple[tuple[int, ...], ...]:
    before = link_input(banks[left_index], banks[left_index + 1])
    after = A.apply_semantic(before, handoff_word())
    output = list(banks)
    output[left_index] = tuple(after[:A.N])
    output[left_index + 1] = tuple(after[A.N:2 * A.N])
    if any(after[2 * A.N:]):
        raise RuntimeError("link work did not return clean")
    return tuple(output)


def direction_witness_word() -> tuple[A.Gate, ...]:
    return (
        A.cn(A.U_TO_V, A.DIRECTION_OK),
        A.cn(A.V_TO_U, A.DIRECTION_OK),
    )


def event_ready_bank(
    bank: tuple[int, ...], direction: tuple[int, int] = (1, 0)
) -> tuple[int, ...]:
    state = A.set_interface(bank, direction[0] ^ direction[1], *direction)
    return A.apply_semantic(state, direction_witness_word())


def safe_packet_body_word() -> tuple[A.Gate, ...]:
    """Route-A packet body with externally retained direction witness.

    The original seven-gate token mover keys only on the post-write VALID bit;
    on an already-full bank that can move a token without a new append.  The
    four latch computations are replaced by complete admitted-event controls.
    """
    base = list(A.packet_word())
    move = A.ZERO_WORK[0]
    valid0 = int(A.CELLS[0]["valid"])
    valid1 = int(A.CELLS[1]["valid"])
    original = [
        A.tof(A.TOKEN[0], valid0, move),
        A.tof(A.TOKEN[1], valid1, move),
        A.cn(A.TOKEN[1], A.TOKEN[0]),
        A.tof(move, A.TOKEN[0], A.TOKEN[1]),
        A.cn(A.TOKEN[1], A.TOKEN[0]),
        A.tof(A.TOKEN[1], valid0, move),
        A.tof(A.TOKEN[0], valid1, move),
    ]
    start = next(
        index for index in range(len(base) - len(original) + 1)
        if base[index:index + len(original)] == original
    )
    common = (
        A.POINTER, A.DIRECTION_OK, A.BINDER, A.ACTUAL, A.ADMISS, A.LAW,
    )
    replacement = (
        *A.mcx(common + (A.TOKEN[0], valid0), move, A.ZERO_WORK[1:]),
        *A.mcx(common + (A.TOKEN[1], valid1), move, A.ZERO_WORK[1:]),
        A.cn(A.TOKEN[1], A.TOKEN[0]),
        A.tof(move, A.TOKEN[0], A.TOKEN[1]),
        A.cn(A.TOKEN[1], A.TOKEN[0]),
        *A.mcx(common + (A.TOKEN[1], valid0), move, A.ZERO_WORK[1:]),
        *A.mcx(common + (A.TOKEN[0], valid1), move, A.ZERO_WORK[1:]),
    )
    base[start:start + len(original)] = replacement
    # The witness is computed before the boundary layer and removed after the
    # packet layer, so delete the packet word's internal compute/uncompute.
    base = [
        gate for gate in base
        if not (
            gate.kind == "CNOT"
            and gate.wires[1] == A.DIRECTION_OK
            and gate.wires[0] in (A.U_TO_V, A.V_TO_U)
        )
    ]
    return tuple(base)


def structural_prefix_word(bank_index: int) -> tuple[A.Gate, ...]:
    """Write the high five bits of address 2*bank+cell after an append."""
    if not 0 <= bank_index < 32:
        raise ValueError("six-bit packet address exhausted")
    word: list[A.Gate] = []
    valid0 = int(A.CELLS[0]["valid"])
    valid1 = int(A.CELLS[1]["valid"])
    admitted = (
        A.POINTER, A.DIRECTION_OK, A.BINDER, A.ACTUAL, A.ADMISS, A.LAW,
    )
    for head_bit in range(1, 6):
        if not ((bank_index >> (head_bit - 1)) & 1):
            continue
        # First append: token moved to rail 1 and cell 1 remains blank.
        word.append(A.x(valid1))
        word.extend(A.mcx(
            admitted + (A.TOKEN[1], A.FRESH[0], valid0, valid1),
            A.HEAD[head_bit], A.ZERO_WORK,
        ))
        word.append(A.x(valid1))
        # Second append: token returned to rail 0 and both cells are full.
        word.extend(A.mcx(
            admitted + (A.TOKEN[0], *A.FRESH, valid0, valid1),
            A.HEAD[head_bit], A.ZERO_WORK,
        ))
    return tuple(word)


def packet_word_for_bank(bank_index: int) -> tuple[A.Gate, ...]:
    return safe_packet_body_word() + structural_prefix_word(bank_index)


def fixed_event_step(
    banks: tuple[tuple[int, ...], ...], direction: tuple[int, int]
) -> tuple[tuple[int, ...], ...]:
    # Every boundary and every bank receives the same fixed layer.  An empty
    # destination prevents a token from cascading through two boundaries.
    state = []
    for bank in banks:
        if sum(bank[wire] for wire in A.TOKEN) == 1:
            prepared = A.set_interface(bank, direction[0] ^ direction[1], *direction)
            prepared = A.apply_semantic(prepared, direction_witness_word())
            state.append(prepared)
        else:
            state.append(bank)
    state = tuple(state)
    for left in range(len(state) - 1):
        state = apply_boundary(state, left)
    output = []
    for bank_index, bank in enumerate(state):
        after = A.apply_semantic(bank, packet_word_for_bank(bank_index))
        after = A.apply_semantic(after, tuple(reversed(direction_witness_word())))
        output.append(A.clear_interface(after))
    return tuple(output)


def chain_certificate(bank_count: int) -> dict[str, object]:
    banks = (A.initial_bank(),) + (inactive_bank(),) * (bank_count - 1)
    directions = ((1, 0), (0, 1)) * bank_count
    failures = token_failures = continuity_failures = predecessor_failures = 0
    for event, direction in enumerate(directions):
        banks = fixed_event_step(banks, direction)
        occupied = [
            index
            for index, bank in enumerate(banks)
            for layout in A.CELLS
            if bank[int(layout["valid"])]
        ]
        failures += len(occupied) != event + 1
        token_banks = [index for index, bank in enumerate(banks) if sum(bank[wire] for wire in A.TOKEN)]
        token_failures += token_banks != [event // 2]
        active = banks[event // 2]
        continuity_failures += A.integer(active, A.HEAD) != event
        continuity_failures += A.integer(active, A.ROTOR) != ((14 + event + 1) % 16)
        layout = A.CELLS[event % 2]
        predecessor = A.integer(active, layout["pred"])
        predecessor_failures += predecessor != (A.NONE_SENTINEL if event == 0 else event - 1)
    # A seventh event on the three-bank fixture is outside the declared
    # finite resource domain and must not be mistaken for lawful recurrence.
    hostile = fixed_event_step(banks, (1, 0))
    exhaustion_changes = hostile != banks
    packet_field_failures = 0
    for event, direction in enumerate(directions):
        bank = banks[event // 2]
        packet = A.packet_projection(bank, event % 2)
        rotor_before = (14 + event) % 16
        expected = {
            "identity": event % 2,
            "predecessor": None if event == 0 else event - 1,
            "rotor_before": rotor_before,
            "rotor": (rotor_before + 1) % 16,
            "carry": int(rotor_before == 15),
            "delta_mask": 66,
            "endpoint": 1,
            "binder": 1,
            "valid": 1,
            "orientation": 1 if direction == (1, 0) else -1,
            "actuality": 1,
            "admissibility": 1,
            "law_domain": 1,
        }
        packet_field_failures += packet != expected
    return {
        "banks": bank_count,
        "events": len(directions),
        "filled_packet_cells": sum(
            bank[int(layout["valid"])] for bank in banks for layout in A.CELLS
        ),
        "fill_failures": failures,
        "one_hot_token_failures": token_failures,
        "head_rotor_continuity_failures": continuity_failures,
        "global_predecessor_failures": predecessor_failures,
        "packet_field_failures": packet_field_failures,
        "exhausted_next_event_declared_outside_domain": True,
        "forced_exhausted_continuation_changes_state": exhaustion_changes,
    }


def refusal_and_token_domain_certificate() -> dict[str, object]:
    initial = (A.initial_bank(), inactive_bank())
    half = fixed_event_step(initial, (1, 0))
    full = fixed_event_step(half, (0, 1))
    no_event = full
    for _ in range(3):
        no_event = fixed_event_step(no_event, (0, 0))

    refusal_failures = 0
    refusal_rows = {}
    for wire, label in (
        (A.BINDER, "binder_zero"),
        (A.ACTUAL, "actual_zero"),
        (A.ADMISS, "admiss_zero"),
        (A.LAW, "law_zero"),
    ):
        for phase, banks in (("half", half), ("full", full)):
            hostile = [list(bank) for bank in banks]
            token_bank = next(
                index for index, bank in enumerate(hostile)
                if sum(bank[q] for q in A.TOKEN) == 1
            )
            hostile[token_bank][wire] = 0
            hostile = tuple(tuple(bank) for bank in hostile)
            observed = fixed_event_step(hostile, (1, 0))
            refused = observed == hostile
            refusal_failures += not refused
            refusal_rows[f"{phase}_{label}"] = refused

    # Two tokens are deliberately exposed as an unlawful supplied sector,
    # not misreported as locally rejected by the physical word.
    two = list(initial)
    extra = list(two[1])
    extra[A.TOKEN[0]] = 1
    two[1] = tuple(extra)
    two = tuple(two)
    two_after = fixed_event_step(two, (1, 0))
    two_writes = sum(
        bank[int(layout["valid"])] for bank in two_after for layout in A.CELLS
    )
    return {
        "three_no_event_updates_identity": no_event == full,
        "refusal_rows": refusal_rows,
        "refusal_failures": refusal_failures,
        "two_token_input_detected_outside_domain": sum(
            bank[wire] for bank in two for wire in A.TOKEN
        ) != 1,
        "two_token_literal_execution_packet_writes": two_writes,
        "global_one_token_genesis_remains_supplied": True,
    }


def recurrent_one_particle_chain_certificate() -> dict[str, object]:
    maximum_norm = maximum_number = maximum_bad_weight = 0.0
    maximum_support = append_terms = no_append_terms = history_failures = 0
    for source in (1 << mode for mode in range(12)):
        initial_banks = (A.initial_bank(), inactive_bank())
        state: dict[tuple[int, tuple[tuple[int, ...], ...], tuple[int, ...]], complex] = {
            (source, initial_banks, ()): 1.0 + 0.0j
        }
        for _step in range(4):
            updated: dict[tuple[int, tuple[tuple[int, ...], ...], tuple[int, ...]], complex] = {}
            for (matter, banks, history), outer_amplitude in state.items():
                for (target, pointer), amplitude in A.K714.decoded_cycle713_column(matter).items():
                    if pointer:
                        direction = (
                            int(bool((target >> 6) & 1) and not bool((target >> 1) & 1)),
                            int(bool((target >> 1) & 1) and not bool((target >> 6) & 1)),
                        )
                        append_terms += 1
                        next_history = history + (1 if direction == (1, 0) else -1,)
                    else:
                        direction = (0, 0)
                        no_append_terms += 1
                        next_history = history
                    target_banks = fixed_event_step(banks, direction)
                    key = (target, target_banks, next_history)
                    updated[key] = updated.get(key, 0.0j) + outer_amplitude * amplitude
            state = {key: value for key, value in updated.items() if abs(value) > 1.0e-13}
            maximum_support = max(maximum_support, len(state))
        maximum_norm = max(
            maximum_norm,
            abs(sum(abs(value) ** 2 for value in state.values()) - 1.0),
        )
        maximum_number = max(
            maximum_number,
            max(
                (abs(value) for (matter, _banks, _history), value in state.items() if matter.bit_count() != 1),
                default=0.0,
            ),
        )
        bad_weight = 0.0
        for (_matter, banks, history), amplitude in state.items():
            count = len(history)
            bad = sum(
                bank[int(layout["valid"])] for bank in banks for layout in A.CELLS
            ) != count
            token_banks = [
                index for index, bank in enumerate(banks)
                if sum(bank[wire] for wire in A.TOKEN)
            ]
            expected_token_bank = 0 if count == 0 else (count - 1) // 2
            bad |= token_banks != [expected_token_bank]
            active = banks[expected_token_bank]
            bad |= A.integer(active, A.HEAD) != (A.NONE_SENTINEL if count == 0 else count - 1)
            bad |= A.integer(active, A.ROTOR) != ((14 + count) % 16)
            for event in range(4):
                bank = banks[event // 2]
                packet = A.packet_projection(bank, event % 2)
                if event >= count:
                    bad |= packet is not None
                    continue
                rotor_before = (14 + event) % 16
                expected = {
                    "identity": event % 2,
                    "predecessor": None if event == 0 else event - 1,
                    "rotor_before": rotor_before,
                    "rotor": (rotor_before + 1) % 16,
                    "carry": int(rotor_before == 15),
                    "delta_mask": 66,
                    "endpoint": 1,
                    "binder": 1,
                    "valid": 1,
                    "orientation": history[event],
                    "actuality": 1,
                    "admissibility": 1,
                    "law_domain": 1,
                }
                bad |= packet != expected
            history_failures += bool(bad)
            if bad:
                bad_weight += abs(amplitude) ** 2
        maximum_bad_weight = max(maximum_bad_weight, bad_weight)
    return {
        "one_particle_sources": 12,
        "applications_per_source": 4,
        "maximum_sparse_support": maximum_support,
        "maximum_norm_residual": maximum_norm,
        "maximum_particle_number_leakage": maximum_number,
        "history_oracle_failures": history_failures,
        "maximum_bad_history_probability_weight": maximum_bad_weight,
        "append_branch_terms": append_terms,
        "no_append_branch_terms": no_append_terms,
    }


def route_certificate() -> dict[str, object]:
    direction_in = tuple(off(gate, LEFT) for gate in direction_witness_word())
    direction_out = tuple(off(gate, RIGHT) for gate in reversed(direction_witness_word()))
    word = (
        direction_in
        + handoff_word()
        + tuple(off(gate, RIGHT) for gate in packet_word_for_bank(1))
        + direction_out
    )
    primitives = A.expanded(word)
    matrices = {"X": A.X, "H": A.H, "T": A.T, "TD": A.TD, "CNOT": A.CNOT}
    instructions = tuple(
        A.C713.C712.c707.Instruction(
            "interbank_then_append_" + kind,
            tuple((0, wire, 0) for wire in wires),
            matrices[kind],
        )
        for kind, wires in primitives
    )
    routed, route = A.C713.C712.c707.route_word(instructions)
    translations = ((3, -2, 1), (-4, 1, 2))
    translation_failures = 0
    signature = tuple((gate.kind, gate.sites) for gate in instructions)
    for shift in translations:
        shifted = tuple(
            (
                gate.kind,
                tuple(tuple(site[axis] + shift[axis] for axis in range(3)) for site in gate.sites),
            )
            for gate in instructions
        )
        normalized = tuple(
            (
                kind,
                tuple(tuple(site[axis] - shift[axis] for axis in range(3)) for site in sites),
            )
            for kind, sites in shifted
        )
        translation_failures += normalized != signature
    frames = A.C713.C712.C709.G.c706.proper_cubic_frames()
    frame_failures = product_failures = 0
    for frame in frames:
        inverse = frame.T
        for gate in instructions:
            transformed = tuple(tuple(int(v) for v in frame @ np.asarray(site)) for site in gate.sites)
            restored = tuple(tuple(int(v) for v in inverse @ np.asarray(site)) for site in transformed)
            frame_failures += restored != gate.sites
            for left_index in range(len(gate.sites)):
                for right_index in range(left_index + 1, len(gate.sites)):
                    original_distance = sum(abs(a - b) for a, b in zip(
                        gate.sites[left_index], gate.sites[right_index]
                    ))
                    transformed_distance = sum(abs(a - b) for a, b in zip(
                        transformed[left_index], transformed[right_index]
                    ))
                    frame_failures += original_distance != transformed_distance
    for left in frames:
        for right in frames:
            product = left @ right
            product_failures += not any(np.array_equal(product, frame) for frame in frames)
    return {
        "assigned_M2": N_LINK,
        "primitive_one_two_M2_gates": len(instructions),
        "routed_nearest_neighbor_gates": len(routed),
        "maximum_route_distance": route["maximum_route_distance"],
        "non_NN_failures": route["non_NN_failures"],
        "operand_order_failures": route["operand_order_failures"],
        "route_return_failures": route["route_return_failures"],
        "route_deletion_detected_macros": route["delete_first_swap_detected_macros"],
        "routed_word_sha256": route["word_sha256"],
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "frame_failures": frame_failures,
        "product_failures": product_failures,
        "translation_failures": translation_failures,
    }


def main() -> int:
    handoff = handoff_certificate()
    composed = composed_handoff_append_certificate()
    deletions = deletion_certificate()
    trained = chain_certificate(2)
    held = chain_certificate(5)
    held32 = chain_certificate(32)
    domains = refusal_and_token_domain_certificate()
    mass_chain = recurrent_one_particle_chain_certificate()
    route = route_certificate()
    checks = {
        "literal_local_handoff": handoff["semantic_matches"]
        and handoff["clean_latch_and_work"]
        and handoff["exact_inverse"]
        and handoff["arbitrary_inverse_failures"] == 0,
        "hostile_controls": all(handoff["hostile_controls"].values()),
        "active_deletions": handoff["deletion_detected"]
        and all(row["basis_state_norm_residual"] > 1.0e-3 for row in deletions.values()),
        "composed_handoff_then_append": composed["pass"],
        "trained_chain": trained["fill_failures"] == 0
        and trained["one_hot_token_failures"] == 0
        and trained["head_rotor_continuity_failures"] == 0
        and trained["global_predecessor_failures"] == 0
        and trained["packet_field_failures"] == 0,
        "held_chain": held["fill_failures"] == 0
        and held["one_hot_token_failures"] == 0
        and held["head_rotor_continuity_failures"] == 0
        and held["global_predecessor_failures"] == 0
        and held["packet_field_failures"] == 0,
        "finite_exhaustion_exposed": trained["forced_exhausted_continuation_changes_state"]
        and held["forced_exhausted_continuation_changes_state"],
        "held_32_bank_chain": held32["events"] == 64
        and held32["fill_failures"] == 0
        and held32["one_hot_token_failures"] == 0
        and held32["head_rotor_continuity_failures"] == 0
        and held32["global_predecessor_failures"] == 0
        and held32["packet_field_failures"] == 0,
        "refusal_and_no_event_domains": domains["three_no_event_updates_identity"]
        and domains["refusal_failures"] == 0
        and domains["two_token_input_detected_outside_domain"]
        and domains["two_token_literal_execution_packet_writes"] == 2,
        "four_update_one_particle_chain": mass_chain["one_particle_sources"] == 12
        and mass_chain["applications_per_source"] == 4
        and mass_chain["maximum_norm_residual"] < TOL
        and mass_chain["maximum_particle_number_leakage"] < TOL
        and mass_chain["history_oracle_failures"] == 0
        and mass_chain["maximum_bad_history_probability_weight"] < TOL,
        "literal_M2_route": route["non_NN_failures"] == 0
        and route["operand_order_failures"] == 0
        and route["route_return_failures"] == 0
        and route["route_deletion_detected_macros"] > 0,
        "proper_cubic_translation": route["proper_cubic_frames"] == 24
        and route["ordered_frame_products"] == 576
        and route["frame_failures"] == 0
        and route["product_failures"] == 0
        and route["translation_failures"] == 0,
    }
    report = {
        "checks": checks,
        "pass": all(checks.values()),
        "handoff": handoff,
        "composed_handoff_append": composed,
        "deletions": deletions,
        "trained": trained,
        "held": held,
        "held_32_bank_ceiling": held32,
        "domain_controls": domains,
        "recurrent_one_particle_chain": mass_chain,
        "route": route,
        "supplied": [
            "Route-A two-cell physical bank and packet word",
            "finite translated chain of blank banks and link work genesis",
            "six-bit structural bank-address ROM (at most 32 two-cell banks)",
            "one initial token/head/rotor state",
            "BINDER, ACTUAL, ADMISS, LAW and endpoint-event inputs",
            "fixed boundary-handoff-then-append circuit order; not physical time",
        ],
        "derived": [
            "full-left/blank-right local handoff predicate",
            "reversible token/head/rotor transfer with returned-clean latch",
            "same fixed layer filling trained two-bank and held five-bank chains",
            "six-bit structural bank-address prefix and cross-bank predecessor continuity",
            "four Cycle-713 one-particle updates through the translated-bank allocator",
            "nearest-neighbor M2 route and passive proper-cubic/translation covariance",
        ],
        "open": [
            "genesis/enforcement of blank banks, link work, and initial token",
            "local enforcement of the globally supplied one-token sector",
            "ACTUAL and ADMISS laws and autonomous endpoint-event production",
            "resource growth or lawful boundary behavior after finite-chain exhaustion",
            "active coframes, time, permanent Record, Born history, source/gravity, and prediction bridges",
        ],
        "boundary": (
            "Positive local inter-bank allocator handoff on a finite supplied chain. "
            "It removes host address selection but does not derive event admission, genesis, "
            "unbounded resources, time, Record permanence, or Born realization."
        ),
    }
    report["report_sha256"] = sha256(json.dumps(report, sort_keys=True, default=str).encode()).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print("ROUTE_A_INTERBANK_HANDOFF_PASS" if report["pass"] else "ROUTE_A_INTERBANK_HANDOFF_INCOMPLETE")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
