#!/usr/bin/env python3
"""Cycle871 selected Cycle870 seam to Cycle714 packet bridge checker.

This checker selects directed OpenReference seams, surrounds the complete
signed FSWAP with a coherent XOR/OR endpoint instrument, and feeds the retained
pointer plus an independently supplied orientation into the landed 59-M2
Cycle714 fixed packet.  It checks the unchanged Cycle704/610/612 projections.

The checks are finite and basis-exhaustive on the declared two-cell occupation
domain.  Circuit order is not physical time.  The retained pointer is an
opportunity control, and the other Cycle714 admission controls remain supplied.

Authority: none.  Audit: unset.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict, dataclass
from hashlib import sha256
from itertools import permutations, product
import argparse
import json
import math
from pathlib import Path
import random
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle870_openreference_native_recurrent_update_2026_08_02 as C870
import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as C714
import frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25 as C704


RUNNER_PATH = (
    "scripts/frontier_cycle871_selected_openreference_seam_cycle714_"
    "packet_bridge_check_2026_08_02.py"
)
RECEIPT_PATH = (
    "outputs/cycle871_selected_openreference_seam_cycle714_packet_bridge_"
    "check_receipt_2026_08_02.json"
)
AUDIT_INPUT_PATHS = (
    RUNNER_PATH,
    RECEIPT_PATH,
    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py",
    "scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 300
EXPECTED_DIRECT_SHA256 = {
    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py": (
        "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237"
    ),
    "scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py": (
        "64b36432670f8a05179d0473e724afee1dfe6327cdd0233d3d788a6b8413c8a2"
    ),
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py": (
        "eb6c9a50681c69ea4fae47724c58d8ba10b48a270e7efa67a811af234afe9a1a"
    ),
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py": (
        "4d0049dbcb231301e0b0b110bc1933dfb2bda1aea2628e5e30bc5c1cee97d66a"
    ),
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py": (
        "36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac"
    ),
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py": (
        "6365d5aed1e70fb9b427ee6fb987879027cc30c818856a992b3fbf9d057e0c1b"
    ),
}

TOL = 3.0e-10
OCCUPATION_WIDTH = 12
OCCUPATION_ROWS = 1 << OCCUPATION_WIDTH
CANONICAL_DELTA_MASK = (1 << 1) | (1 << 6)
HEAD_NONE = C714.SENTINEL_NONE
ROTOR_BEFORE = 14
DIRECTIONS = tuple(tuple(int(value) for value in row) for row in C870.root_place.DIRECTIONS)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def add(left, right):
    return tuple(left[index] + right[index] for index in range(3))


def matvec(frame: np.ndarray, row):
    return tuple(int(value) for value in frame @ np.asarray(row, dtype=int))


def axis_endpoints(axis: int) -> tuple[int, int]:
    """Global two-cell mode indices for the landed directed seam."""

    return 2 * axis + 1, 6 + 2 * axis


def endpoint_cells(axis: int):
    left = (0, 0, 0)
    right = tuple(int(index == axis) for index in range(3))
    return left, right


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    """Independent reconstruction of the 24 determinant-one signed frames."""

    rows = {}
    for order in permutations(range(3)):
        permutation = np.eye(3, dtype=int)[list(order)]
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation
            if round(np.linalg.det(frame)) == 1:
                rows[tuple(int(value) for value in frame.flat)] = frame
    return tuple(rows[key] for key in sorted(rows))


FRAMES = proper_cubic_frames()


def frame_key(frame: np.ndarray):
    return tuple(int(value) for value in frame.flat)


def mode_map(frame: np.ndarray) -> tuple[int, ...]:
    return tuple(
        DIRECTIONS.index(matvec(frame, direction)) for direction in DIRECTIONS
    )


def inverse_mapping(mapping):
    output = [0] * len(mapping)
    for source, target in enumerate(mapping):
        output[target] = source
    return tuple(output)


def permute_mask(mask: int, mapping) -> int:
    return sum(
        ((mask >> source) & 1) << target
        for source, target in enumerate(mapping)
    )


def fock_permutation_action(mapping, state: int) -> tuple[int, int]:
    targets = [
        mapping[mode] for mode in range(len(mapping)) if (state >> mode) & 1
    ]
    inversions = sum(
        targets[left] > targets[right]
        for left in range(len(targets))
        for right in range(left + 1, len(targets))
    )
    return sum(1 << target for target in targets), (-1 if inversions & 1 else 1)


def transposition_action(state: int, first: int, second: int) -> tuple[int, int]:
    mapping = list(range(OCCUPATION_WIDTH))
    mapping[first], mapping[second] = mapping[second], mapping[first]
    return fock_permutation_action(mapping, state)


def logical_fswap_polynomial(first: int, second: int):
    """Signed Pauli polynomial for a non-adjacent fermionic transposition."""

    low, high = sorted((first, second))
    flip = (1 << first) | (1 << second)
    between = sum(1 << mode for mode in range(low + 1, high))
    endpoints = (1 << first) | (1 << second)
    return {
        (0, 1 << first): 0.5 + 0.0j,
        (0, 1 << second): 0.5 + 0.0j,
        (flip, between): 0.5 + 0.0j,
        (flip, between | endpoints): -0.5 + 0.0j,
    }


def apply_logical_polynomial(value, source: int):
    output = defaultdict(complex)
    for (xmask, zmask), coefficient in value.items():
        phase = -1 if ((zmask & source).bit_count() & 1) else 1
        output[source ^ xmask] += coefficient * phase
    return {
        target: amplitude
        for target, amplitude in output.items()
        if abs(amplitude) > 1.0e-13
    }


def sparse_residual(left, right) -> float:
    return float(math.sqrt(sum(
        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
        for key in set(left) | set(right)
    )))


class SignedStabilizerReducer:
    """Canonical signed reduction modulo the landed Cycle870 constraints."""

    def __init__(self, stabilizers, qubits: int):
        self.qubits = qubits
        self.basis = {}
        for source in stabilizers:
            row = source
            vector = row.symplectic(qubits)
            while vector:
                pivot = vector.bit_length() - 1
                if pivot in self.basis:
                    row = row @ self.basis[pivot]
                    vector = row.symplectic(qubits)
                else:
                    self.basis[pivot] = row
                    break
            if not vector and row != C870.Pauli():
                raise AssertionError(("inconsistent signed stabilizer", row))

    def reduce_pauli(self, source):
        row = source
        vector = row.symplectic(self.qubits)
        for pivot in sorted(self.basis, reverse=True):
            if (vector >> pivot) & 1:
                row = row @ self.basis[pivot]
                vector = row.symplectic(self.qubits)
        return row

    def reduce_polynomial(self, value):
        output = defaultdict(complex)
        for row, coefficient in value.items():
            reduced = self.reduce_pauli(row)
            key = C870.Pauli(0, reduced.x, reduced.z)
            output[key] += coefficient * (1j ** reduced.phase)
        return {
            row: coefficient
            for row, coefficient in output.items()
            if abs(coefficient) > 1.0e-12
        }


def graph_logical_fswap_target(graph, axis: int):
    left_cell, right_cell = endpoint_cells(axis)
    pairs = {
        (cell, mode): (xrow, zrow)
        for cell, mode, xrow, zrow in C870.root_place.logical_rows(graph)
    }
    first, second = axis_endpoints(axis)
    left_pair = pairs[(left_cell, first)]
    right_pair = pairs[(right_cell, second - 6)]
    xa, za = left_pair
    xb, zb = right_pair
    ya = C870.Pauli(1) @ xa @ za
    yb = C870.Pauli(1) @ xb @ zb
    ordered_modes = tuple(
        [(left_cell, mode) for mode in range(6)]
        + [(right_cell, mode) for mode in range(6)]
    )
    parity = C870.pauli_product(
        pairs[wire][1] for wire in ordered_modes[first + 1:second]
    )
    return C870.poly_clean({
        za: 0.5 + 0.0j,
        zb: 0.5 + 0.0j,
        xa @ parity @ xb: 0.5 + 0.0j,
        ya @ parity @ yb: 0.5 + 0.0j,
    })


def seam_code_certificate(axis: int):
    left_cell, right_cell = endpoint_cells(axis)
    graph = C870.prep.OpenReferenceGraph((left_cell, right_cell))
    first, second = axis_endpoints(axis)
    rows = (
        C870.semantic_row(graph, ("B", left_cell, first)),
        C870.semantic_row(graph, ("B", right_cell, second - 6)),
        *C870.seam_hop_rows(
            graph, left_cell, first, right_cell, second - 6
        ),
    )
    observed = C870.fswap_polynomial(rows)
    expected = graph_logical_fswap_target(graph, axis)
    reducer = SignedStabilizerReducer(
        C870.local_stabilizers(graph), len(graph.edges)
    )
    reduced_observed = reducer.reduce_polynomial(observed)
    reduced_expected = reducer.reduce_polynomial(expected)
    certificate = C870.fswap_certificate(rows)
    term_deletion_code_residuals = []
    for deleted in range(4):
        damaged = C870.fswap_polynomial(tuple(
            row for index, row in enumerate(rows) if index != deleted
        ))
        term_deletion_code_residuals.append(C870.poly_residual(
            reducer.reduce_polynomial(damaged), reduced_expected
        ))
    selected = (left_cell, axis, right_cell, first, second - 6)
    return {
        "axis": axis,
        "selected_seam": selected,
        "selected_seam_present_in_landed_graph_enumerator": (
            selected in C870.graph_seams(graph)
        ),
        "constraint_rank": len(reducer.basis),
        "code_target_residual": C870.poly_residual(
            reduced_observed, reduced_expected
        ),
        "full_space_involution_residual": certificate[
            "full_space_involution_residual"
        ],
        "four_rotation_residual_up_to_global_phase": certificate[
            "four_rotation_residual_up_to_global_phase"
        ],
        "four_rotation_global_phase": certificate["four_rotation_global_phase"],
        "term_deletion_code_residuals": tuple(term_deletion_code_residuals),
        "term_deletion_involution_residuals": tuple(certificate[
            "term_deletion_involution_residuals"
        ]),
        "rotation_deletion_residuals": tuple(certificate[
            "rotation_deletion_residuals"
        ]),
        "hermitian_term_failures": certificate["hermitian_term_failures"],
    }


# These proper rotations carry the canonical +x seam to +x, +y, and +z.
AXIS_FRAMES = (
    np.eye(3, dtype=int),
    np.asarray(((0, 0, 1), (1, 0, 0), (0, 1, 0)), dtype=int),
    np.asarray(((0, 1, 0), (0, 0, 1), (1, 0, 0)), dtype=int),
)


def raw_to_canonical_mapping(axis: int):
    canonical_to_raw_local = mode_map(AXIS_FRAMES[axis])
    raw_to_canonical_local = inverse_mapping(canonical_to_raw_local)
    return tuple(
        6 * cell + raw_to_canonical_local[mode]
        for cell in range(2)
        for mode in range(6)
    )


def raw_to_canonical_mask(mask: int, axis: int) -> int:
    return permute_mask(mask, raw_to_canonical_mapping(axis))


PACKET_WORD = C714.word()
PACKET_INVERSE = tuple(reversed(PACKET_WORD))


def packet_word_without(selector):
    index = next(
        index for index, gate in enumerate(PACKET_WORD) if selector(index, gate)
    )
    return PACKET_WORD[:index] + PACKET_WORD[index + 1:]


DAMAGED_PACKET_WORDS = {
    "delete_packet_enable": PACKET_WORD[1:],
    "delete_packet_delta": packet_word_without(
        lambda _index, gate: gate.q[-1] == C714.PDELTA[1]
    ),
    "delete_packet_orientation": packet_word_without(
        lambda _index, gate: gate.q[-1] == C714.PORIENT
    ),
    "delete_packet_predecessor": packet_word_without(
        lambda _index, gate: gate.q[-1] == C714.PRED[0]
    ),
}


def blank_packet(
    rotor: int = ROTOR_BEFORE,
    head: int = HEAD_NONE,
    orientation: int = 0,
    other_controls=(1, 1, 1, 1, 1),
):
    """Cycle714 register before the aliased endpoint instrument.

    The pointer is blank and then derived by the seam instrument.  The five
    remaining liveness controls and ORIENT are independent supplied inputs.
    """

    return C714.initial(
        rotor,
        head,
        orientation,
        controls=(0, *other_controls),
    )


@dataclass(frozen=True)
class BridgeOutput:
    matter: int
    phase: int
    packet: tuple[int, ...]
    pre_packet_work: tuple[int, int, int]

    @property
    def du(self) -> int:
        return self.packet[C714.MCX_WORK[0]]

    @property
    def dv(self) -> int:
        return self.packet[C714.MCX_WORK[1]]

    @property
    def pointer(self) -> int:
        return self.packet[C714.POINTER]

    @property
    def supplied_orientation(self) -> int:
        return self.packet[C714.ORIENT]


def output_key(row: BridgeOutput):
    return (
        row.matter,
        C714.bits_to_int(row.packet),
    )


def forward_case(
    source: int,
    axis: int,
    *,
    supplied_orientation: int = 0,
    rotor: int = ROTOR_BEFORE,
    head: int = HEAD_NONE,
    other_controls=(1, 1, 1, 1, 1),
    omission: str | None = None,
) -> BridgeOutput:
    first, second = axis_endpoints(axis)
    packet = list(blank_packet(
        rotor, head, supplied_orientation, other_controls
    ))
    du, dv = C714.MCX_WORK[:2]
    pointer = C714.POINTER
    if omission != "delete_pre_left":
        packet[du] ^= (source >> first) & 1
    if omission != "delete_pre_right":
        packet[dv] ^= (source >> second) & 1

    if omission == "delete_seam":
        target, phase = source, 1
    else:
        target, phase = transposition_action(source, first, second)
        if omission == "plain_SWAP_phase":
            phase = 1

    if omission != "delete_post_left":
        packet[du] ^= (target >> first) & 1
    if omission != "delete_post_right":
        packet[dv] ^= (target >> second) & 1
    if omission != "delete_OR_left_CNOT":
        packet[pointer] ^= packet[du]
    if omission != "delete_OR_right_CNOT":
        packet[pointer] ^= packet[dv]
    if omission != "delete_OR_Toffoli":
        packet[pointer] ^= packet[du] & packet[dv]
    if omission != "delete_cleanup_left":
        packet[du] ^= packet[pointer]
    if omission != "delete_cleanup_right":
        packet[dv] ^= packet[pointer]
    pre_packet_work = tuple(packet[wire] for wire in C714.MCX_WORK)
    if omission == "delete_pointer_handoff":
        packet[pointer] = 0
    packet_word = DAMAGED_PACKET_WORDS.get(omission, PACKET_WORD)
    if omission != "delete_packet_word":
        packet = list(C714.apply_semantic(tuple(packet), packet_word))

    if omission == "delete_raw_to_canonical":
        raw_delta = source ^ target
        for wire in C714.PDELTA:
            packet[wire] = 0
        if packet[C714.POINTER]:
            for bit, wire in enumerate(C714.PDELTA):
                packet[wire] = (raw_delta >> bit) & 1

    return BridgeOutput(target, phase, tuple(packet), pre_packet_work)


def independent_expected_case(
    source: int,
    axis: int,
    *,
    supplied_orientation: int = 0,
    rotor: int = ROTOR_BEFORE,
    head: int = HEAD_NONE,
    other_controls=(1, 1, 1, 1, 1),
) -> BridgeOutput:
    first, second = axis_endpoints(axis)
    target, phase = transposition_action(source, first, second)
    pointer = ((source >> first) ^ (source >> second)) & 1
    packet = list(blank_packet(
        rotor, head, supplied_orientation, other_controls
    ))
    packet[C714.POINTER] = pointer
    packet = list(C714.independent_expected(tuple(packet)))
    return BridgeOutput(target, phase, tuple(packet), (0, 0, 0))


def inverse_case(row: BridgeOutput, axis: int) -> BridgeOutput:
    first, second = axis_endpoints(axis)
    matter = row.matter
    packet = list(row.packet)
    packet = list(C714.apply_semantic(tuple(packet), PACKET_INVERSE))
    du, dv = C714.MCX_WORK[:2]
    pointer = C714.POINTER

    # Inverse clean, OR, postwrite, FSWAP, and prewrite on the same aliases.
    packet[dv] ^= packet[pointer]
    packet[du] ^= packet[pointer]
    packet[pointer] ^= packet[du] & packet[dv]
    packet[pointer] ^= packet[dv]
    packet[pointer] ^= packet[du]
    packet[dv] ^= (matter >> second) & 1
    packet[du] ^= (matter >> first) & 1
    matter, inverse_phase = transposition_action(matter, first, second)
    packet[dv] ^= (matter >> second) & 1
    packet[du] ^= (matter >> first) & 1
    return BridgeOutput(
        matter,
        row.phase * inverse_phase,
        tuple(packet),
        (0, 0, 0),
    )


def decode_packet(bits) -> C704.IntervalPacket:
    predecessor = C714.integer(bits, C714.PRED)
    return C704.IntervalPacket(
        identity=C714.FIXED_ADDRESS,
        predecessor=None if predecessor == HEAD_NONE else predecessor,
        rotor_before=C714.integer(bits, C714.RB),
        rotor=C714.integer(bits, C714.RA),
        carry=bits[C714.CARRY],
        delta_mask=C714.integer(bits, C714.PDELTA),
        endpoint=bits[C714.PEND],
        binder=bits[C714.PBIND],
        valid=bits[C714.PVALID],
        orientation=1 if bits[C714.PORIENT] else -1,
        actuality=bits[C714.PACT],
        admissibility=bits[C714.PADM],
        law_domain=bits[C714.PLAW],
    )


def expected_packet(supplied_orientation: int):
    return {
        "identity": C714.FIXED_ADDRESS,
        "predecessor": None,
        "rotor_before": ROTOR_BEFORE,
        "rotor": (ROTOR_BEFORE + 1) % 16,
        "carry": 0,
        "delta_mask": CANONICAL_DELTA_MASK,
        "endpoint": 1,
        "binder": 1,
        "valid": 1,
        "orientation": 1 if supplied_orientation else -1,
        "actuality": 1,
        "admissibility": 1,
        "law_domain": 1,
    }


def exhaustive_bridge_certificate():
    axis_rows = []
    total_cases = equation_failures = inverse_failures = 0
    scratch_failures = packet_failures = mask_failures = orientation_failures = 0
    pointer_true = pointer_false = signed_negative = phase_failures = 0
    maximum_column_residual = maximum_coherent_residual = 0.0
    plain_swap_witness_residuals = []
    coherent_rows = []

    for axis in range(3):
        first, second = axis_endpoints(axis)
        value = logical_fswap_polynomial(first, second)
        axis_equations = axis_inverse = axis_scratch = 0
        axis_packet = axis_mask = axis_orientation = axis_phase = 0
        axis_true = axis_false = axis_negative = 0
        axis_maximum = 0.0
        observed_coherent = defaultdict(complex)
        expected_coherent = defaultdict(complex)
        for supplied_orientation in (0, 1):
            for source in range(OCCUPATION_ROWS):
                observed = forward_case(
                    source, axis, supplied_orientation=supplied_orientation
                )
                expected = independent_expected_case(
                    source, axis, supplied_orientation=supplied_orientation
                )
                equation_failed = observed != expected
                axis_equations += equation_failed
                total_cases += 1

                target, phase = transposition_action(source, first, second)
                column = apply_logical_polynomial(value, source)
                column_residual = sparse_residual(column, {target: complex(phase)})
                axis_maximum = max(axis_maximum, column_residual)
                axis_phase += column_residual > TOL
                axis_negative += phase == -1

                restored = inverse_case(observed, axis)
                axis_inverse += restored != BridgeOutput(
                    source,
                    1,
                    blank_packet(orientation=supplied_orientation),
                    (0, 0, 0),
                )
                axis_scratch += (
                    any(observed.pre_packet_work)
                    or any(observed.packet[wire] for wire in (
                        *C714.ENABLE_WORK, *C714.MCX_WORK
                    ))
                )
                pointer = ((source >> first) ^ (source >> second)) & 1
                raw_delta = source ^ target
                canonical_delta = raw_to_canonical_mask(raw_delta, axis)
                axis_mask += canonical_delta != pointer * CANONICAL_DELTA_MASK
                axis_true += pointer
                axis_false += 1 - pointer
                if pointer:
                    packet = decode_packet(observed.packet)
                    axis_packet += asdict(packet) != expected_packet(
                        supplied_orientation
                    )
                    axis_orientation += packet.orientation != (
                        1 if supplied_orientation else -1
                    )
                else:
                    axis_packet += any(
                        observed.packet[wire] for wire in range(34)
                    )

                amplitude = (
                    np.exp(
                        2j * np.pi * ((source + 7 * supplied_orientation) % 17) / 17
                    )
                    / (64.0 * math.sqrt(2.0))
                )
                observed_coherent[output_key(observed)] += (
                    amplitude * observed.phase
                )
                expected_coherent[output_key(expected)] += (
                    amplitude * expected.phase
                )

        coherent_residual = sparse_residual(observed_coherent, expected_coherent)
        maximum_coherent_residual = max(
            maximum_coherent_residual, coherent_residual
        )
        coherent_rows.append({
            "axis": axis,
            "superposed_source_columns": 2 * OCCUPATION_ROWS,
            "independently_supplied_orientation_values": 2,
            "norm_residual": coherent_residual,
        })

        double = (1 << first) | (1 << second)
        signed = {
            output: amplitude
            for source, amplitude in ((0, 1 / math.sqrt(2)), (double, 1 / math.sqrt(2)))
            for output, sign in (transposition_action(source, first, second),)
            for amplitude in (amplitude * sign,)
        }
        plain = {0: 1 / math.sqrt(2), double: 1 / math.sqrt(2)}
        witness_residual = sparse_residual(signed, plain)
        plain_swap_witness_residuals.append(witness_residual)

        axis_rows.append({
            "axis": axis,
            "raw_endpoint_modes": (first, second),
            "occupation_rows_per_supplied_orientation": OCCUPATION_ROWS,
            "independently_supplied_orientation_values": 2,
            "composed_rows": 2 * OCCUPATION_ROWS,
            "pointer_true_rows": axis_true,
            "pointer_false_rows": axis_false,
            "signed_negative_rows": axis_negative,
            "FSWAP_polynomial_truth_failures": axis_phase,
            "maximum_FSWAP_column_residual": axis_maximum,
            "bridge_equation_failures": axis_equations,
            "inverse_failures": axis_inverse,
            "scratch_cleanup_failures": axis_scratch,
            "packet_schema_failures": axis_packet,
            "raw_to_canonical_mask_failures": axis_mask,
            "Cycle714_supplied_orientation_failures": axis_orientation,
            "plain_SWAP_coherent_phase_residual": witness_residual,
        })
        equation_failures += axis_equations
        inverse_failures += axis_inverse
        scratch_failures += axis_scratch
        packet_failures += axis_packet
        mask_failures += axis_mask
        orientation_failures += axis_orientation
        pointer_true += axis_true
        pointer_false += axis_false
        signed_negative += axis_negative
        phase_failures += axis_phase
        maximum_column_residual = max(maximum_column_residual, axis_maximum)

    return {
        "axes": tuple(axis_rows),
        "total_occupation_rows": total_cases,
        "pointer_true_rows": pointer_true,
        "pointer_false_rows": pointer_false,
        "signed_negative_rows": signed_negative,
        "FSWAP_polynomial_truth_failures": phase_failures,
        "maximum_FSWAP_column_residual": maximum_column_residual,
        "bridge_equation_failures": equation_failures,
        "inverse_failures": inverse_failures,
        "scratch_cleanup_failures": scratch_failures,
        "packet_schema_failures": packet_failures,
        "raw_to_canonical_mask_failures": mask_failures,
        "Cycle714_supplied_orientation_failures": orientation_failures,
        "coherent_full_4096_by_two_orientation_rows": tuple(coherent_rows),
        "maximum_coherent_composition_residual": maximum_coherent_residual,
        "plain_SWAP_coherent_phase_residuals": tuple(
            plain_swap_witness_residuals
        ),
    }


def deletion_certificate():
    omissions = (
        "delete_seam",
        "plain_SWAP_phase",
        "delete_pre_left",
        "delete_pre_right",
        "delete_post_left",
        "delete_post_right",
        "delete_OR_left_CNOT",
        "delete_OR_right_CNOT",
        "delete_OR_Toffoli",
        "delete_cleanup_left",
        "delete_cleanup_right",
        "delete_pointer_handoff",
        "delete_packet_enable",
        "delete_packet_delta",
        "delete_packet_orientation",
        "delete_packet_predecessor",
        "delete_packet_word",
        "delete_raw_to_canonical",
    )
    counts = {}
    for omission in omissions:
        differences = 0
        for axis in range(3):
            for supplied_orientation in (0, 1):
                for source in range(OCCUPATION_ROWS):
                    differences += (
                        forward_case(
                            source,
                            axis,
                            supplied_orientation=supplied_orientation,
                            omission=omission,
                        )
                        != independent_expected_case(
                            source,
                            axis,
                            supplied_orientation=supplied_orientation,
                        )
                    )
        counts[omission] = differences
    return {
        "trials_per_mutation": 3 * 2 * OCCUPATION_ROWS,
        "difference_counts": counts,
        "inactive_mutations": tuple(
            label for label, count in counts.items() if not count
        ),
    }


def exhaustive_liveness_certificate():
    """Primary 262,144-row endpoint/packet liveness domain."""

    axis = 0
    first, second = axis_endpoints(axis)
    cases = admitted = refused = 0
    equation_failures = inverse_failures = scratch_failures = 0
    pointer_alias_failures = orientation_failures = work_failures = 0
    for rotor in range(16):
        for head in range(64):
            for supplied_orientation in (0, 1):
                for left_occupation, right_occupation in product((0, 1), repeat=2):
                    source = (
                        (left_occupation << first)
                        | (right_occupation << second)
                    )
                    pointer = left_occupation ^ right_occupation
                    for pattern in range(32):
                        controls = tuple(
                            (pattern >> index) & 1 for index in range(5)
                        )
                        observed = forward_case(
                            source,
                            axis,
                            supplied_orientation=supplied_orientation,
                            rotor=rotor,
                            head=head,
                            other_controls=controls,
                        )
                        expected = independent_expected_case(
                            source,
                            axis,
                            supplied_orientation=supplied_orientation,
                            rotor=rotor,
                            head=head,
                            other_controls=controls,
                        )
                        cases += 1
                        enabled = bool(pointer and all(controls))
                        admitted += enabled
                        refused += not enabled
                        equation_failures += observed != expected
                        scratch_failures += any(observed.pre_packet_work)
                        work_failures += any(
                            observed.packet[wire]
                            for wire in (*C714.ENABLE_WORK, *C714.MCX_WORK)
                        )
                        pointer_alias_failures += (
                            observed.packet[C714.POINTER] != pointer
                        )
                        if enabled:
                            orientation_failures += (
                                observed.packet[C714.PORIENT]
                                != supplied_orientation
                            )
                        restored = inverse_case(observed, axis)
                        inverse_failures += restored != BridgeOutput(
                            source,
                            1,
                            blank_packet(
                                rotor,
                                head,
                                supplied_orientation,
                                controls,
                            ),
                            (0, 0, 0),
                        )
    return {
        "factorization": (
            "16 rotors * 64 heads * 2 supplied orientations * "
            "4 endpoint occupations * 32 other-control patterns"
        ),
        "cases": cases,
        "admitted_cases": admitted,
        "refused_cases": refused,
        "equation_failures": equation_failures,
        "inverse_failures": inverse_failures,
        "pre_packet_scratch_failures": scratch_failures,
        "post_packet_work_failures": work_failures,
        "pointer_q44_alias_failures": pointer_alias_failures,
        "supplied_orientation_failures": orientation_failures,
        "endpoint_scratch_aliases": C714.MCX_WORK[:2],
        "pointer_alias": C714.POINTER,
        "total_physical_M2": C714.N,
    }


def arbitrary_packet_inverse_certificate():
    generator = random.Random(871)
    failures = 0
    cases = 256
    for _ in range(cases):
        before = tuple(generator.randrange(2) for _ in range(C714.N))
        after = C714.apply_semantic(before, PACKET_WORD)
        failures += C714.apply_semantic(after, PACKET_INVERSE) != before
    return {
        "arbitrary_59_M2_rows": cases,
        "inverse_failures": failures,
        "semantic_gates": len(PACKET_WORD),
        "expanded_one_two_M2_gates": len(C714.expanded(PACKET_WORD)),
        "Toffoli_decomposition_residual": C714.toffoli_residual(),
    }


def generated_joint_order_controls(packet_a, packet_b, no_endpoint: int):
    opportunity_a = packet_a.endpoint
    opportunity_b = packet_b.endpoint
    joint = C704.C612.JointOrder()
    for index in range(3):
        if opportunity_a:
            joint.admit_local("A", 100 + index)
    for index in range(2):
        if opportunity_b:
            joint.admit_local("B", 200 + index)
    first_shared = (
        joint.admit_shared(900)
        if opportunity_a & opportunity_b
        else "no_opportunity"
    )
    if opportunity_a:
        joint.admit_local("A", 103)
    if opportunity_b:
        joint.admit_local("B", 202)
    second_shared = (
        joint.admit_shared(901)
        if opportunity_a & opportunity_b
        else "no_opportunity"
    )

    adversary = C704.C612.JointOrder()
    for index in range(4):
        adversary.admit_local("A", 300 + index)
        adversary.admit_local("B", 400 + index)
    inverted_first = adversary.admit_shared(910)
    adversary.force_shared(911, 1, 6)
    inverted_refusal = adversary.admit_shared(912)

    forced = C704.C612.JointOrder()
    for index in range(3):
        forced.admit_local("A", 500 + index)
        forced.admit_local("B", 600 + index)
    forced.force_shared(920, 0, 2)
    forced.force_shared(921, 2, 0)

    gated = C704.C612.JointOrder()
    no_endpoint_status = (
        gated.admit_shared(930) if no_endpoint else "no_opportunity"
    )
    return {
        "edge_qubit_opportunities": (opportunity_a, opportunity_b),
        "consistent_statuses": (first_shared, second_shared),
        "consistent_acyclic": joint.acyclic(),
        "inverted_first": inverted_first,
        "inverted_refusal": inverted_refusal,
        "forced_cycle_detected": not forced.acyclic(),
        "no_endpoint_status": no_endpoint_status,
        "JointOrder_class_module": C704.C612.JointOrder.__module__,
    }


def acceptance_certificate():
    first, second = axis_endpoints(0)
    source = 1 << first
    bridge_outputs = tuple(
        forward_case(source, 0, supplied_orientation=orientation)
        for orientation in (0, 1)
    )
    generated = [decode_packet(output.packet) for output in bridge_outputs]
    packet_statuses = []
    cycle610_statuses = []
    packet_projection_failures = cycle610_projection_failures = 0
    for packet in generated:
        bank = C704.ReversiblePacketBank(bank=C704.C610.BANK_SIZE)
        status = bank.append(
            packet.identity,
            packet.delta_mask,
            packet.endpoint,
            packet.orientation,
            packet.binder,
            packet.actuality,
            packet.admissibility,
            packet.law_domain,
        )
        packet_statuses.append(status)
        packet_projection_failures += (
            status != "admitted" or asdict(bank.cells[packet.identity]) != asdict(packet)
        )

        chain = C704.C610.EventChain(bank=C704.C610.BANK_SIZE)
        chain_status = chain.admit(
            tick_id=packet.identity,
            orientation=packet.orientation,
            certificate=packet.endpoint,
            binder=packet.binder,
            actuality=packet.actuality,
            admissibility=packet.admissibility,
            law_domain=packet.law_domain,
        )
        cycle610_statuses.append(chain_status)
        projected = C704.C610.EventCell(
            identity=packet.identity,
            rotor=packet.rotor,
            carry=packet.carry,
            predecessor=packet.predecessor,
            binder=packet.binder,
            valid=packet.valid,
            orientation=packet.orientation,
        )
        cycle610_projection_failures += (
            chain_status != "admitted"
            or asdict(projected) != asdict(chain.cells[-1])
        )

    no_pointer = forward_case(0, 0, supplied_orientation=0)
    no_packet = decode_packet(no_pointer.packet)
    no_bank = C704.ReversiblePacketBank(bank=C704.C610.BANK_SIZE)
    no_packet_status = no_bank.append(
        C714.FIXED_ADDRESS,
        no_packet.delta_mask,
        no_packet.endpoint,
        -1,
        1,
        1,
        1,
        1,
    )
    no_chain = C704.C610.EventChain(bank=C704.C610.BANK_SIZE)
    no_cycle610_status = no_chain.admit(
        tick_id=C714.FIXED_ADDRESS,
        orientation=-1,
        certificate=no_packet.endpoint,
        binder=1,
        actuality=1,
        admissibility=1,
        law_domain=1,
    )

    generated_joint = generated_joint_order_controls(
        generated[0], generated[1], no_packet.endpoint
    )
    landed_joint = C704.joint_order_controls()
    return {
        "generated_orientations": tuple(packet.orientation for packet in generated),
        "supplied_orientation_bits": (0, 1),
        "packet_orientation_bits": tuple(
            output.packet[C714.PORIENT] for output in bridge_outputs
        ),
        "Cycle704_packet_statuses": tuple(packet_statuses),
        "Cycle704_packet_projection_failures": packet_projection_failures,
        "Cycle610_statuses": tuple(cycle610_statuses),
        "Cycle610_EventCell_projection_failures": cycle610_projection_failures,
        "no_pointer_Cycle704_status": no_packet_status,
        "no_pointer_Cycle610_status": no_cycle610_status,
        "Cycle612_generated_harness": generated_joint,
        "Cycle612_landed_harness": landed_joint,
        "Cycle612_unchanged_harness_failures": generated_joint != landed_joint,
    }


def unit(axis: int):
    return tuple(int(index == axis) for index in range(3))


def scale_vector(value: int, row):
    return tuple(value * component for component in row)


@dataclass(frozen=True)
class SeamCoframe:
    midpoint: tuple[int, int, int]
    along: tuple[int, int, int]
    b: tuple[int, int, int]
    d: tuple[int, int, int]


def seam_coframe(seam) -> SeamCoframe:
    cell, axis, _target, _left_mode, _right_mode = seam
    along = unit(axis)
    b = unit((axis + 1) % 3)
    d = unit((axis + 2) % 3)
    midpoint = add(scale_vector(16, cell), scale_vector(8, along))
    return SeamCoframe(midpoint, along, b, d)


def transform_coframe(frame, coframe: SeamCoframe) -> SeamCoframe:
    return SeamCoframe(
        matvec(frame, coframe.midpoint),
        matvec(frame, coframe.along),
        matvec(frame, coframe.b),
        matvec(frame, coframe.d),
    )


def coframe_site(coframe: SeamCoframe, local):
    output = coframe.midpoint
    for coefficient, basis in zip(
        local, (coframe.along, coframe.b, coframe.d)
    ):
        output = add(output, scale_vector(coefficient, basis))
    return output


FIXED_ALIAS_LOCALS = {
    C714.POINTER: (0, 0, 1),
    C714.MCX_WORK[0]: (0, 1, 0),
    C714.MCX_WORK[1]: (0, -1, 0),
}


def radius_two_packet_sites(coframe: SeamCoframe, blocked):
    """Independent frozen primary coframe placement reconstruction."""

    fixed = {
        wire: coframe_site(coframe, local)
        for wire, local in FIXED_ALIAS_LOCALS.items()
    }
    fixed_sites = set(fixed.values())
    candidates = []
    for local in product(range(-2, 3), repeat=3):
        site = coframe_site(coframe, local)
        if site in blocked or site in fixed_sites:
            continue
        candidates.append((
            max(abs(value) for value in local),
            sum(abs(value) for value in local),
            local,
            site,
        ))
    candidates.sort(key=lambda row: row[:3])
    remaining_wires = tuple(
        wire for wire in range(C714.N) if wire not in fixed
    )
    if len(candidates) < len(remaining_wires):
        raise AssertionError(("radius-two packet palette deficit", len(candidates)))
    sites = dict(fixed)
    locals_by_wire = dict(FIXED_ALIAS_LOCALS)
    for wire, (_linf, _l1, local, site) in zip(remaining_wires, candidates):
        sites[wire] = site
        locals_by_wire[wire] = local
    return sites, locals_by_wire, {
        "fixed_alias_blocked_collisions": len(fixed_sites & set(blocked)),
        "available_radius_two_sites": len(candidates),
        "unused_radius_two_sites": len(candidates) - len(remaining_wires),
    }


def physical_support_sites(row, context):
    lifted = C870.physical_lift(row, context)
    return tuple(
        context.sites[index]
        for index in range(len(context.sites))
        if ((lifted.x | lifted.z) >> index) & 1
    )


MATRICES = {
    "H": C714.H,
    "T": C714.T,
    "TD": C714.TD,
    "CNOT": C714.CNOT,
}


def physical_bridge_instructions(packet_sites, left_support, right_support):
    du = packet_sites[C714.MCX_WORK[0]]
    dv = packet_sites[C714.MCX_WORK[1]]
    pointer = packet_sites[C714.POINTER]
    instructions = []

    def append_cnot(kind, control, target):
        instructions.append(C870.c707.Instruction(
            kind, (control, target), C714.CNOT
        ))

    for site in left_support:
        append_cnot("cycle871_pre_left_B_parity", site, du)
    for site in right_support:
        append_cnot("cycle871_pre_right_B_parity", site, dv)
    for site in left_support:
        append_cnot("cycle871_post_left_B_parity", site, du)
    for site in right_support:
        append_cnot("cycle871_post_right_B_parity", site, dv)
    append_cnot("cycle871_OR_left", du, pointer)
    append_cnot("cycle871_OR_right", dv, pointer)
    for kind, wires in C714.toffoli_primitives(0, 1, 2):
        local_sites = tuple((du, dv, pointer)[wire] for wire in wires)
        instructions.append(C870.c707.Instruction(
            "cycle871_OR_Toffoli_" + kind,
            local_sites,
            MATRICES[kind],
        ))
    append_cnot("cycle871_clean_left", pointer, du)
    append_cnot("cycle871_clean_right", pointer, dv)
    for kind, wires in C714.expanded(PACKET_WORD):
        instructions.append(C870.c707.Instruction(
            "cycle871_packet_" + kind,
            tuple(packet_sites[wire] for wire in wires),
            MATRICES[kind],
        ))
    return tuple(instructions)


def inverse_instructions(word):
    return tuple(
        C870.c707.Instruction(
            "inverse_" + instruction.kind,
            instruction.sites,
            instruction.matrix.conj().T,
        )
        for instruction in reversed(word)
    )


def route_summary(report):
    return {
        key: report[key]
        for key in (
            "routed_gate_count",
            "routed_one_site",
            "routed_two_site",
            "touched_sites",
            "maximum_route_distance",
            "non_NN_failures",
            "operand_order_failures",
            "route_return_failures",
            "delete_first_swap_detected_macros",
            "word_sha256",
        )
    }


def geometry_certificate():
    shapes = []
    total_frame_transport_failures = total_product_failures = 0
    total_layouts = 0
    for length in (2, 3):
        shape = (length, length, length)
        graph = C870.prep.OpenReferenceGraph(C870.box_cells(shape))
        context = C870.physical_context(graph)
        persistent = set(context.sites) | {
            C870.root_place.slot(cell, role, index)
            for cell in graph.cells
            for role, count in C870.root_place.ROLE_COUNTS.items()
            for index in range(count)
        }
        seam_rows = []
        layout_payload = []
        for seam_index, seam in enumerate(C870.graph_seams(graph)):
            left_cell, axis, right_cell, left_mode, right_mode = seam
            left_row = C870.semantic_row(
                graph, ("B", left_cell, left_mode)
            )
            right_row = C870.semantic_row(
                graph, ("B", right_cell, right_mode)
            )
            left_support = physical_support_sites(left_row, context)
            right_support = physical_support_sites(right_row, context)
            coframe = seam_coframe(seam)
            packet_sites, local_sites, placement = radius_two_packet_sites(
                coframe, persistent
            )
            word = physical_bridge_instructions(
                packet_sites, left_support, right_support
            )
            routed, route = C870.c707.route_word(word)
            inverse_word = inverse_instructions(word)
            inverse_routed, inverse_route = C870.c707.route_word(inverse_word)
            assigned = set(packet_sites.values())
            touched = set(route["touched_coordinates"])
            inverse_touched = set(inverse_route["touched_coordinates"])
            first_packet_index = next(
                index for index, instruction in enumerate(word)
                if instruction.kind.startswith("cycle871_packet_")
            )
            last_cleanup_index = max(
                index for index, instruction in enumerate(word)
                if instruction.kind.startswith("cycle871_clean_")
            )

            frame_transport_failures = 0
            for frame in FRAMES:
                transformed_blocked = {
                    matvec(frame, site) for site in persistent
                }
                transported, transported_locals, _row = radius_two_packet_sites(
                    transform_coframe(frame, coframe), transformed_blocked
                )
                frame_transport_failures += sum(
                    transported[wire] != matvec(frame, packet_sites[wire])
                    or transported_locals[wire] != local_sites[wire]
                    for wire in range(C714.N)
                )
            product_failures = 0
            for left in FRAMES:
                for right in FRAMES:
                    product_failures += sum(
                        matvec(left, matvec(right, site))
                        != matvec(left @ right, site)
                        for site in packet_sites.values()
                    )
            total_frame_transport_failures += frame_transport_failures
            total_product_failures += product_failures
            total_layouts += 1
            layout_payload.append(tuple(
                (wire, packet_sites[wire], local_sites[wire])
                for wire in range(C714.N)
            ))
            seam_rows.append({
                "seam_index": seam_index,
                "axis": axis,
                "selected_seam": seam,
                "selected_seam_present": seam in C870.graph_seams(graph),
                "left_B_support_weight": len(left_support),
                "right_B_support_weight": len(right_support),
                "left_B_support_L1_diameter": C870.support_diameter(
                    C870.physical_lift(left_row, context), context.sites
                ),
                "right_B_support_L1_diameter": C870.support_diameter(
                    C870.physical_lift(right_row, context), context.sites
                ),
                "bridge_and_packet_aliased_M2": len(assigned),
                "Cycle714_packet_interface_M2": C714.N,
                "endpoint_scratch_aliases": C714.MCX_WORK[:2],
                "pointer_alias": C714.POINTER,
                "assigned_palette_collisions": C714.N - len(assigned),
                "persistent_palette_collisions": len(assigned & persistent),
                "packet_site_collisions": C714.N - len(assigned),
                "fixed_alias_blocked_collisions": placement[
                    "fixed_alias_blocked_collisions"
                ],
                "available_radius_two_sites": placement[
                    "available_radius_two_sites"
                ],
                "maximum_local_L_infinity_radius": max(
                    max(abs(value) for value in local_sites[wire])
                    for wire in range(C714.N)
                ),
                "endpoint_cleanup_precedes_packet": (
                    last_cleanup_index < first_packet_index
                ),
                "extra_primitive_instructions": len(word),
                "forward_route": route_summary(route),
                "inverse_route": route_summary(inverse_route),
                "forward_inverse_routed_gate_count_match": (
                    len(routed) == len(inverse_routed)
                ),
                "returned_route_persistent_spectators": len(
                    (touched | inverse_touched) & persistent
                    - set(left_support) - set(right_support)
                ),
                "proper_frame_coframe_transport_failures": frame_transport_failures,
                "ordered_product_coordinate_failures": product_failures,
            })
        landed_covariance = C870.root_place.covariance_certificate(
            shape, graph, context.site_map
        )
        shapes.append({
            "name": f"open_L{length}",
            "shape": shape,
            "cells": len(graph.cells),
            "internal_seams": len(C870.graph_seams(graph)),
            "physical_carrier_M2": len(context.sites),
            "persistent_preparation_auxiliary_M2": len(persistent) - len(context.sites),
            "seam_layouts_checked": len(seam_rows),
            "seams": tuple(seam_rows),
            "all_seam_layout_sha256": sha256(
                repr(tuple(layout_payload)).encode()
            ).hexdigest(),
            "landed_coordinate_covariance": landed_covariance,
        })
    return {
        "shapes": tuple(shapes),
        "radius_two_rule": (
            "q44=m+d, q56=m+b, q57=m-b; remaining wires receive unblocked "
            "local [-2,2]^3 offsets in (Linf,L1,local tuple) order"
        ),
        "coframe_recomputed_from_unsigned_target_axis": False,
        "seam_layouts_checked": total_layouts,
        "proper_frame_coframe_transport_failures": (
            total_frame_transport_failures
        ),
        "ordered_product_coordinate_failures": total_product_failures,
    }


def covariance_certificate():
    landed_frames = tuple(C870.base.proper_cubic_frames())
    independent_keys = {frame_key(frame) for frame in FRAMES}
    landed_keys = {frame_key(frame) for frame in landed_frames}
    frame_lookup = {frame_key(frame): index for index, frame in enumerate(FRAMES)}
    semantic_rows = semantic_failures = endpoint_failures = 0
    pointer_failures = canonical_mask_failures = 0
    maximum_phase_residual = 0.0

    for axis in range(3):
        first, second = axis_endpoints(axis)
        source_mapping = list(range(OCCUPATION_WIDTH))
        source_mapping[first], source_mapping[second] = (
            source_mapping[second], source_mapping[first]
        )
        for frame in FRAMES:
            local = mode_map(frame)
            transformed_direction = matvec(frame, DIRECTIONS[2 * axis])
            transformed_index = DIRECTIONS.index(transformed_direction)
            target_axis = transformed_index // 2
            reverses_owner = transformed_index & 1
            cell_map = (1, 0) if reverses_owner else (0, 1)
            global_map = tuple(
                6 * cell_map[cell] + local[mode]
                for cell in range(2)
                for mode in range(6)
            )
            target_first, target_second = axis_endpoints(target_axis)
            endpoint_failures += {
                global_map[first], global_map[second]
            } != {target_first, target_second}
            for source in range(OCCUPATION_ROWS):
                target_input, input_phase = fock_permutation_action(
                    global_map, source
                )
                source_output, source_phase = fock_permutation_action(
                    source_mapping, source
                )
                transported_output, output_phase = fock_permutation_action(
                    global_map, source_output
                )
                expected_output, target_phase = transposition_action(
                    target_input, target_first, target_second
                )
                phase_residual = abs(
                    source_phase * output_phase - input_phase * target_phase
                )
                maximum_phase_residual = max(maximum_phase_residual, phase_residual)
                semantic_failures += (
                    transported_output != expected_output or phase_residual > TOL
                )
                source_pointer = ((source >> first) ^ (source >> second)) & 1
                target_pointer = (
                    (target_input >> target_first)
                    ^ (target_input >> target_second)
                ) & 1
                pointer_failures += source_pointer != target_pointer
                raw_target, _phase = transposition_action(
                    target_input, target_first, target_second
                )
                canonical_mask_failures += raw_to_canonical_mask(
                    target_input ^ raw_target, target_axis
                ) != target_pointer * CANONICAL_DELTA_MASK
                semantic_rows += 1

    # Precompute the signed six-mode frame action, doubled over two cells.
    signed_tables = []
    local_maps = []
    for frame in FRAMES:
        local = mode_map(frame)
        local_maps.append(local)
        global_map = tuple(
            6 * cell + local[mode]
            for cell in range(2)
            for mode in range(6)
        )
        signed_tables.append(tuple(
            fock_permutation_action(global_map, state)
            for state in range(OCCUPATION_ROWS)
        ))

    product_rows = mode_product_failures = signed_product_failures = 0
    coordinate_product_failures = 0
    canonical_coframe = SeamCoframe(
        (8, 0, 0), unit(0), unit(1), unit(2)
    )
    coordinate_sites = tuple(
        coframe_site(canonical_coframe, local)
        for local in product(range(-2, 3), repeat=3)
    )
    for left_index, left in enumerate(FRAMES):
        for right_index, right in enumerate(FRAMES):
            product_index = frame_lookup[frame_key(left @ right)]
            composed_modes = tuple(
                local_maps[left_index][local_maps[right_index][mode]]
                for mode in range(6)
            )
            mode_product_failures += composed_modes != local_maps[product_index]
            for state in range(OCCUPATION_ROWS):
                middle, right_phase = signed_tables[right_index][state]
                sequential, left_phase = signed_tables[left_index][middle]
                direct, direct_phase = signed_tables[product_index][state]
                signed_product_failures += (
                    sequential != direct
                    or left_phase * right_phase != direct_phase
                )
            coordinate_product_failures += sum(
                matvec(left, matvec(right, site))
                != matvec(left @ right, site)
                for site in coordinate_sites
            )
            product_rows += 1
    return {
        "proper_cubic_frames": len(FRAMES),
        "ordered_frame_products": product_rows,
        "independent_landed_frame_set_difference": len(
            independent_keys ^ landed_keys
        ),
        "signed_seam_occupation_rows": semantic_rows,
        "signed_seam_endpoint_mapping_failures": endpoint_failures,
        "signed_seam_semantic_failures": semantic_failures,
        "maximum_signed_seam_phase_residual": maximum_phase_residual,
        "pointer_covariance_failures": pointer_failures,
        "Cycle714_orientation_input_values_exhausted": 2,
        "canonical_mask_covariance_failures": canonical_mask_failures,
        "mode_product_failures": mode_product_failures,
        "signed_Fock_product_rows": product_rows * OCCUPATION_ROWS,
        "signed_Fock_product_failures": signed_product_failures,
        "bridge_coordinate_product_failures": coordinate_product_failures,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-receipt",
        action="store_true",
        help="write the deterministic JSON receipt after all checks pass",
    )
    args = parser.parse_args()
    started = time.perf_counter()
    observed_hashes = {
        path: digest(ROOT / path) for path in EXPECTED_DIRECT_SHA256
    }
    dependency_pin_failures = {
        path: {"expected": expected, "observed": observed_hashes[path]}
        for path, expected in EXPECTED_DIRECT_SHA256.items()
        if observed_hashes[path] != expected
    }
    seam = tuple(seam_code_certificate(axis) for axis in range(3))
    exhaustive = exhaustive_bridge_certificate()
    liveness = exhaustive_liveness_certificate()
    deletions = deletion_certificate()
    packet_inverse = arbitrary_packet_inverse_certificate()
    acceptance = acceptance_certificate()
    geometry = geometry_certificate()
    covariance = covariance_certificate()

    geometry_seams = tuple(
        seam_row
        for shape in geometry["shapes"]
        for seam_row in shape["seams"]
    )
    checks = {
        "direct_dependencies_are_byte_pinned": not dependency_pin_failures,
        "selected_landed_seams_equal_signed_logical_FSWAPs": all(
            row["selected_seam_present_in_landed_graph_enumerator"]
            and row["code_target_residual"] < TOL
            and row["full_space_involution_residual"] < TOL
            and row["four_rotation_residual_up_to_global_phase"] < TOL
            and row["hermitian_term_failures"] == 0
            for row in seam
        ),
        "seam_term_and_rotation_deletions_are_active": all(
            min(row["term_deletion_code_residuals"]) > 1.0e-3
            and min(row["term_deletion_involution_residuals"]) > 1.0e-3
            and min(row["rotation_deletion_residuals"]) > 1.0e-3
            for row in seam
        ),
        "all_4096_rows_on_all_three_axes_close_exactly": (
            exhaustive["total_occupation_rows"] == 3 * 2 * OCCUPATION_ROWS
            and exhaustive["FSWAP_polynomial_truth_failures"] == 0
            and exhaustive["maximum_FSWAP_column_residual"] < TOL
            and exhaustive["bridge_equation_failures"] == 0
            and exhaustive["packet_schema_failures"] == 0
            and exhaustive["raw_to_canonical_mask_failures"] == 0
            and exhaustive["Cycle714_supplied_orientation_failures"] == 0
        ),
        "both_declared_orientation_inputs_project_exactly": (
            acceptance["supplied_orientation_bits"] == (0, 1)
            and acceptance["packet_orientation_bits"] == (0, 1)
        ),
        "coherent_phase_pointer_and_scratch_are_exact": (
            exhaustive["maximum_coherent_composition_residual"] < TOL
            and exhaustive["scratch_cleanup_failures"] == 0
            and exhaustive["pointer_true_rows"] > 0
            and exhaustive["pointer_false_rows"] > 0
            and exhaustive["signed_negative_rows"] > 0
            and min(exhaustive["plain_SWAP_coherent_phase_residuals"]) > 1.0e-3
        ),
        "all_262144_primary_liveness_rows_close_exactly": (
            liveness["cases"] == 262144
            and liveness["admitted_cases"] == 4096
            and liveness["refused_cases"] == 258048
            and liveness["endpoint_scratch_aliases"] == (56, 57)
            and liveness["pointer_alias"] == 44
            and liveness["total_physical_M2"] == 59
            and all(
                liveness[key] == 0
                for key in (
                    "equation_failures",
                    "inverse_failures",
                    "pre_packet_scratch_failures",
                    "post_packet_work_failures",
                    "pointer_q44_alias_failures",
                    "supplied_orientation_failures",
                )
            )
        ),
        "composed_inverse_and_59_M2_packet_inverse_are_exact": (
            exhaustive["inverse_failures"] == 0
            and packet_inverse["inverse_failures"] == 0
            and packet_inverse["Toffoli_decomposition_residual"] < TOL
        ),
        "every_named_bridge_mutation_is_detected": not deletions[
            "inactive_mutations"
        ],
        "unchanged_Cycle704_610_612_acceptance_is_preserved": (
            acceptance["generated_orientations"] == (-1, 1)
            and set(acceptance["Cycle704_packet_statuses"]) == {"admitted"}
            and acceptance["Cycle704_packet_projection_failures"] == 0
            and set(acceptance["Cycle610_statuses"]) == {"admitted"}
            and acceptance["Cycle610_EventCell_projection_failures"] == 0
            and acceptance["no_pointer_Cycle704_status"] == "no_opportunity"
            and acceptance["no_pointer_Cycle610_status"] == "no_opportunity"
            and acceptance["Cycle612_unchanged_harness_failures"] == 0
        ),
        "L2_L3_bridge_geometry_and_returned_routes_close": (
            tuple(
                (shape["cells"], shape["internal_seams"])
                for shape in geometry["shapes"]
            ) == ((8, 12), (27, 54))
            and geometry["seam_layouts_checked"] == 66
            and geometry["proper_frame_coframe_transport_failures"] == 0
            and geometry["ordered_product_coordinate_failures"] == 0
            and not geometry["coframe_recomputed_from_unsigned_target_axis"]
            and all(
                shape["seam_layouts_checked"] == shape["internal_seams"]
                and shape["landed_coordinate_covariance"][
                    "proper_cubic_frames"
                ] == 24
                and shape["landed_coordinate_covariance"][
                    "ordered_products"
                ] == 576
                and shape["landed_coordinate_covariance"][
                    "frame_injectivity_failures"
                ] == 0
                and shape["landed_coordinate_covariance"][
                    "product_diagram_failures"
                ] == 0
                for shape in geometry["shapes"]
            )
            and all(
                seam_row["selected_seam_present"]
                and seam_row["bridge_and_packet_aliased_M2"] == 59
                and seam_row["endpoint_scratch_aliases"] == (56, 57)
                and seam_row["pointer_alias"] == 44
                and seam_row["assigned_palette_collisions"] == 0
                and seam_row["persistent_palette_collisions"] == 0
                and seam_row["packet_site_collisions"] == 0
                and seam_row["fixed_alias_blocked_collisions"] == 0
                and seam_row["maximum_local_L_infinity_radius"] <= 2
                and seam_row["endpoint_cleanup_precedes_packet"]
                and seam_row["proper_frame_coframe_transport_failures"] == 0
                and seam_row["ordered_product_coordinate_failures"] == 0
                and seam_row["forward_route"]["non_NN_failures"] == 0
                and seam_row["forward_route"]["operand_order_failures"] == 0
                and seam_row["forward_route"]["route_return_failures"] == 0
                and seam_row["inverse_route"]["non_NN_failures"] == 0
                and seam_row["inverse_route"]["operand_order_failures"] == 0
                and seam_row["inverse_route"]["route_return_failures"] == 0
                and seam_row["forward_inverse_routed_gate_count_match"]
                for seam_row in geometry_seams
            )
        ),
        "24_frame_576_product_bridge_covariance_is_exact": (
            covariance["proper_cubic_frames"] == 24
            and covariance["ordered_frame_products"] == 576
            and covariance["independent_landed_frame_set_difference"] == 0
            and covariance["signed_seam_occupation_rows"]
            == 3 * 24 * OCCUPATION_ROWS
            and all(
                covariance[key] == 0
                for key in (
                    "signed_seam_endpoint_mapping_failures",
                    "signed_seam_semantic_failures",
                    "pointer_covariance_failures",
                    "canonical_mask_covariance_failures",
                    "mode_product_failures",
                    "signed_Fock_product_failures",
                    "bridge_coordinate_product_failures",
                )
            )
            and covariance["maximum_signed_seam_phase_residual"] < TOL
        ),
    }
    report = {
        "cycle": 871,
        "status": (
            "cycle871-selected-openreference-seam-cycle714-packet-bridge-check-pass"
            if all(checks.values())
            else "cycle871-check-failed"
        ),
        "authority": "none",
        "audit": "unset",
        "claim_scope": (
            "bounded selected-seam checker: signed Cycle870 FSWAP -> coherent "
            "XOR/OR opportunity pointer -> independently supplied Cycle714 "
            "orientation -> landed packet -> unchanged Cycle704/610/612 acceptance"
        ),
        "declared_orientation_input": {
            "Cycle714_ORIENT": "independent input coordinate",
        },
        "selected_seam_code_algebra": seam,
        "exhaustive_two_cell_bridge": exhaustive,
        "exhaustive_primary_liveness": liveness,
        "deletions": deletions,
        "packet_inverse": packet_inverse,
        "unchanged_acceptance": acceptance,
        "L2_L3_geometry": geometry,
        "covariance_24_576": covariance,
        "checks": checks,
        "declared_inputs": AUDIT_INPUT_PATHS,
        "direct_dependency_sha256": observed_hashes,
        "dependency_pin_failures": dependency_pin_failures,
    }
    payload = json.dumps(
        report, indent=2, sort_keys=True, default=str
    ) + "\n"
    print(payload, end="")
    for label, passed in checks.items():
        print(f"CHECK {label}: {'PASS' if passed else 'FAIL'}")
    if not all(checks.values()):
        raise SystemExit(1)
    receipt = ROOT / RECEIPT_PATH
    if args.write_receipt:
        receipt.write_text(payload)
    receipt_matches = receipt.is_file() and receipt.read_text() == payload
    print(
        "CHECK deterministic_receipt_matches: "
        + ("PASS" if receipt_matches else "FAIL")
    )
    print("RECEIPT_SHA256", sha256(payload.encode()).hexdigest())
    print("RUNTIME_SECONDS", time.perf_counter() - started)
    if not receipt_matches:
        raise SystemExit(1)
    print("CYCLE871_SELECTED_OPENREFERENCE_SEAM_CYCLE714_PACKET_BRIDGE_CHECK_PASS")


if __name__ == "__main__":
    main()
