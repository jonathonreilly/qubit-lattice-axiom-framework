#!/usr/bin/env python3
"""Cycle-789 discriminator for the companion-bank input register.

The landed epoch calls [q,2q) the live companion bank, but stage A initializes
the Choi system on [0,q)+[q,q+matter).  This probe inspects that overlap and
then uses the one-mode Bell-character analogue to distinguish self-comparison
of the two Choi halves from a repaired three-register teleportation channel.

The dense analogue uses the same two commuting Bell characters ZZ and XX,
coherent syndrome ancillas, and private-dual X/Z corrections.  It is a
semantic discriminator, not a dense execution of the full 9N/cell circuit.
"""

from __future__ import annotations

from hashlib import sha256
import json

import numpy as np

import frontier_companion_bank_epoch_liveness_2026_07_28 as L
import frontier_companion_bank_bell_character_dilation_2026_07_28 as B


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_"
    "BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_companion_bank_epoch_liveness_2026_07_28.py",
    "scripts/frontier_companion_bank_bell_character_dilation_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
ZERO = np.array([1, 0], dtype=complex)
ONE = np.array([0, 1], dtype=complex)


def apply_one(state: np.ndarray, gate: np.ndarray, target: int, width: int) -> np.ndarray:
    tensor = state.reshape((2,) * width)
    moved = np.moveaxis(tensor, target, 0).reshape(2, -1)
    moved = gate @ moved
    return np.moveaxis(moved.reshape((2,) + (2,) * (width - 1)), 0, target).reshape(-1)


def apply_controlled_pauli(
    state: np.ndarray,
    control: int,
    targets: tuple[tuple[int, np.ndarray], ...],
    width: int,
) -> np.ndarray:
    output = state.copy()
    for basis in range(1 << width):
        # np.reshape uses big-endian tensor axes: qubit axis q is bit width-1-q.
        if ((basis >> (width - 1 - control)) & 1) == 0:
            continue
        amplitude = state[basis]
        if abs(amplitude) == 0:
            continue
        output[basis] -= amplitude
        column = np.zeros(1 << width, dtype=complex)
        column[basis] = amplitude
        for target, gate in targets:
            column = apply_one(column, gate, target, width)
        output += column
    return output


def kron_states(rows: tuple[np.ndarray, ...]) -> np.ndarray:
    output = np.array([1.0 + 0.0j])
    for row in rows:
        output = np.kron(output, row)
    return output


def reduced_one(state: np.ndarray, target: int, width: int) -> np.ndarray:
    tensor = state.reshape((2,) * width)
    moved = np.moveaxis(tensor, target, 0).reshape(2, -1)
    return moved @ moved.conj().T


def bell_measure_character(
    state: np.ndarray,
    ancilla: int,
    targets: tuple[tuple[int, np.ndarray], ...],
    width: int,
) -> np.ndarray:
    state = apply_one(state, H, ancilla, width)
    state = apply_controlled_pauli(state, ancilla, targets, width)
    return apply_one(state, H, ancilla, width)


def prepare_bell_oi(live: np.ndarray) -> np.ndarray:
    # Registers O,I,L,aZ,aX.  O-I is the Choi Bell pair and L is external.
    state = kron_states((ZERO, ZERO, live, ZERO, ZERO))
    state = apply_one(state, H, 0, 5)
    return apply_controlled_pauli(state, 0, ((1, X),), 5)


def character_channel(live: np.ndarray, *, repaired: bool) -> np.ndarray:
    state = prepare_bell_oi(live)
    # Existing two-bank semantics compares O with I.  The repaired semantics
    # compares Choi input I with independent live bank L.
    left, right = ((1, 2) if repaired else (0, 1))
    state = bell_measure_character(state, 3, ((left, Z), (right, Z)), 5)
    state = bell_measure_character(state, 4, ((left, X), (right, X)), 5)
    # Private duals on Choi output O.
    state = apply_controlled_pauli(state, 3, ((0, X),), 5)
    state = apply_controlled_pauli(state, 4, ((0, Z),), 5)
    return reduced_one(state, 0, 5)


def main() -> None:
    atlas = B.P.build_private_atlases()
    bundle = L.build_epoch((1, 1, 1), "primary", atlas)
    q = bundle.fixture.qubits
    matter = bundle.fixture.matter_qubits
    claimed_live = frozenset(range(q, 2 * q))
    stage_a_written = frozenset(
        register
        for slot in bundle.slots
        if slot.stage == "A"
        for word in slot.words
        for register, (_role, mode) in word.accesses.items()
        if mode == "write"
    )
    overlap = claimed_live & stage_a_written
    untouched_live = claimed_live - stage_a_written

    states = {
        "zero": ZERO,
        "one": ONE,
        "plus": (ZERO + ONE) / np.sqrt(2),
        "plus_i": (ZERO + 1j * ONE) / np.sqrt(2),
    }
    existing = {name: character_channel(state, repaired=False) for name, state in states.items()}
    repaired = {name: character_channel(state, repaired=True) for name, state in states.items()}
    targets = {name: np.outer(state, state.conj()) for name, state in states.items()}
    existing_pairwise = max(
        np.linalg.norm(existing[left] - existing[right])
        for left in states for right in states
    )
    existing_identity_residual = max(
        np.linalg.norm(existing[name] - targets[name]) for name in states
    )
    repaired_identity_residual = max(
        np.linalg.norm(repaired[name] - targets[name]) for name in states
    )
    report = {
        "status": "PASS",
        "authority": "none",
        "audit": "unset",
        "fixture": {
            "cells": 1,
            "q": q,
            "matter": matter,
            "claimed_live_bank": [q, 2 * q],
            "stage_A_written_overlap": sorted(overlap),
            "stage_A_written_overlap_count": len(overlap),
            "claimed_live_registers_not_written_by_A": sorted(untouched_live),
            "overlap_equals_entire_claimed_live_bank": overlap == claimed_live,
            "Choi_input_half_overlap": sorted(overlap & frozenset(range(q, q + matter))),
            "encoded_bank_supply_overlap": sorted(overlap & frozenset(range(q + matter, 2 * q))),
        },
        "dense_one_mode_discriminator": {
            "registers": "O,I,L,aZ,aX",
            "tested_input_states": tuple(states),
            "existing_two-bank_output_pairwise_residual": float(existing_pairwise),
            "existing_two-bank_identity_channel_residual": float(existing_identity_residual),
            "repaired_three-bank_identity_channel_residual": float(repaired_identity_residual),
        },
        "checks": {
            "claimed_live_bank_is_written_before_B": bool(len(overlap) > 0),
            "exact_overlap_is_entire_claimed_live_bank": bool(overlap == claimed_live),
            "existing_two_bank_output_is_input_independent": bool(existing_pairwise < 1e-12),
            "existing_two_bank_is_not_identity_channel": bool(existing_identity_residual > 0.5),
            "third_live_bank_repairs_dense_identity_channel": bool(repaired_identity_residual < 1e-12),
        },
        "verdict": (
            "The landed two-register epoch has no independent live-input register: stage A writes all of "
            "[q,2q) before B (Choi initialization on its matter part and encoded-bank supply on the rest). "
            "Its Bell-character leg is therefore a self-comparison "
            "of the Choi halves, not arbitrary input injection.  A third independent live bank repairs the "
            "one-mode character channel exactly; the separate fixed-schedule "
            "runner in this package tests the conditional 9N/cell construction."
        ),
        "claim_boundary": (
            "Route-specific semantic collision and constructive one-mode repair, "
            "not a no-go or, by itself, a full compiler."
        ),
    }
    report["status"] = "PASS" if all(report["checks"].values()) else "FAIL"
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
