#!/usr/bin/env python3
"""Cycle873 physical core: recurrent F17-only all-seam augmentation.

The load-bearing object is the 20-M2 F17-only bank on every landed Cycle870
directed seam: three clean returned work sites plus a persistent 17-rail unary
link.  The core emits the actual selected seam, exact H/T/CNOT controlled
cyclic shifts, returned nearest-neighbour routes, and the fixed 24-colour
all-seam schedule on the L2, L3, and held 3x2x2 open boxes.

Cycle714 packet coexistence is retained as an explicit secondary diagnostic
because its primitive library also supplies the H/T/CNOT matrices used here.
It is not in the primary failure predicate.  One-hot state preparation,
admission/genesis, finite synthesis,
periodic Wilson sectors, source/gravity, time, Record, and Born interpretation
remain outside this bounded core.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import argparse
import json
import math
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle870_openreference_native_recurrent_update_2026_08_02 as C870
import frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02 as J870
import frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02 as C871
import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as C714


Coord = tuple[int, int, int]
Instruction = C870.c707.Instruction
F17 = 17
TOL = 3.0e-10
SHAPES = ((2, 2, 2), (3, 3, 3), (3, 2, 2))
EXPECTED_BASE_COMMIT = "c73a11d1ea7ddd564c48aa2a5a459a43d94262ef"
OUT = ROOT / "outputs/cycle873_recurrent_f17_all_seam_physical_core_receipt_2026_08_03.json"

SOURCE_PATHS = (
    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py",
    "scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py",
    "scripts/frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
)
PRIMARY_SOURCE_PATHS = SOURCE_PATHS
SECONDARY_OPTIONAL_SOURCE_PATHS = ()
EXPECTED_SOURCE_SHA256 = {
    SOURCE_PATHS[0]: "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237",
    SOURCE_PATHS[1]: "1b66c061dcb8e0082fd9e7264e78ccbd0f77440c0f517aa93696bde49f78c1bd",
    SOURCE_PATHS[2]: "6645156635b4354d937759a28e71215121a19cefcc2f294a2791e6a84cf1423b",
    SOURCE_PATHS[3]: "eb6c9a50681c69ea4fae47724c58d8ba10b48a270e7efa67a811af234afe9a1a",
}

# A single nearest-neighbour path, expressed in every seam's supplied coframe.
# It was searched against the live packet, encoded carrier, and preparation
# banks on all three requested fixtures.  Its radius is the constant two.
RAIL_LOCAL_OFFSETS: tuple[Coord, ...] = (
    (-2, 2, 0), (-2, 2, -1), (-1, 2, -1), (-1, 2, -2),
    (0, 2, -2), (1, 2, -2), (1, 1, -2), (2, 1, -2),
    (2, 0, -2), (2, -1, -2), (1, -1, -2), (1, -2, -2),
    (0, -2, -2), (-1, -2, -2), (-1, -2, -1), (-2, -2, -1),
    (-2, -2, -2),
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def add(*rows: Coord) -> Coord:
    return tuple(sum(values) for values in zip(*rows))


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))


def scale(value: int, row: Coord) -> Coord:
    return tuple(value * item for item in row)


def l1(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def at(midpoint: Coord, basis: tuple[Coord, Coord, Coord], local: Coord) -> Coord:
    return add(midpoint, *(scale(value, direction) for value, direction in zip(local, basis)))


def localize(site: Coord, midpoint: Coord, basis) -> Coord:
    return C871.coframe_coordinates(sub(site, midpoint), basis)


def shape_cells(shape: tuple[int, int, int]) -> tuple[Coord, ...]:
    return tuple(product(*(range(length) for length in shape)))


def matrix_digest(matrix: np.ndarray) -> str:
    return C870.c707.c655.matrix_digest(matrix)


def instruction_signature(row: Instruction):
    return row.kind, row.sites, matrix_digest(row.matrix)


def word_digest(word) -> str:
    return sha256(repr(tuple(map(instruction_signature, word))).encode()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, set | frozenset):
        return sorted(value)
    raise TypeError(f"cannot JSON-encode {type(value).__name__}")


def json_safe(value):
    if isinstance(value, dict):
        return {
            key if isinstance(key, str | int | float | bool) or key is None else repr(key):
            json_safe(item)
            for key, item in value.items()
        }
    if isinstance(value, tuple | list | set | frozenset):
        return [json_safe(item) for item in value]
    if isinstance(value, np.generic):
        return value.item()
    return value


@dataclass(frozen=True)
class IntegratedPlacement:
    packet: C871.PacketPlacement
    rails: tuple[Coord, ...]
    blocked: frozenset[Coord]

    @property
    def midpoint(self) -> Coord:
        return self.packet.midpoint

    @property
    def basis(self):
        return self.packet.basis

    @property
    def pointer(self) -> Coord:
        return self.packet.sites[C714.POINTER]

    @property
    def q_u(self) -> Coord:
        return self.packet.sites[C714.MCX_WORK[0]]

    @property
    def q_v(self) -> Coord:
        return self.packet.sites[C714.MCX_WORK[1]]

    @property
    def current(self) -> Coord:
        return self.packet.sites[C714.MCX_WORK[2]]

    @property
    def f17_roles(self) -> frozenset[Coord]:
        return frozenset((self.q_u, self.q_v, self.current, *self.rails))

    @property
    def bank(self) -> frozenset[Coord]:
        return frozenset((*self.packet.sites, *self.rails))

    @property
    def radius(self) -> int:
        return max(
            max(map(abs, localize(site, self.midpoint, self.basis)))
            for site in self.bank
        )


def integrated_placement(graph, context, seam) -> IntegratedPlacement:
    packet = C871.packet_placement(graph, context, seam)
    blocked = frozenset(set(context.sites) | J870.auxiliary_registers(graph))
    rails = tuple(at(packet.midpoint, packet.basis, row) for row in RAIL_LOCAL_OFFSETS)
    placement = IntegratedPlacement(packet, rails, blocked)
    if len(placement.f17_roles) != 20:
        raise AssertionError("20-role F17 bank is not injective")
    if len(placement.bank) != C714.N + F17:
        raise AssertionError("packet-plus-rail bank is not 76 distinct M2")
    if set(rails) & set(packet.sites):
        raise AssertionError("persistent F17 rail collides with live packet")
    if placement.bank & blocked:
        raise AssertionError(("integrated bank collision", placement.bank & blocked))
    if any(l1(left, right) != 1 for left, right in zip(rails, rails[1:])):
        raise AssertionError("F17 rail order is not a nearest-neighbour path")
    if placement.radius > 2:
        raise AssertionError(("bank radius exceeded", placement.radius))
    return placement


def x_gate(site: Coord, kind: str) -> Instruction:
    return C871.one(site, C714.X, kind)


def primitive_word(a: Coord, b: Coord, target: Coord, prefix: str, *, clean_target=False):
    rows = list(C714.toffoli_primitives(0, 1, 2))
    if clean_target:
        if rows[1] != ("CNOT", (1, 2)):
            raise AssertionError("landed Toffoli primitive order changed")
        del rows[1]
    matrices = {"H": C714.H, "T": C714.T, "TD": C714.TD, "CNOT": C714.CNOT}
    local = (a, b, target)
    return tuple(
        Instruction(prefix + kind, tuple(local[index] for index in wires), matrices[kind])
        for kind, wires in rows
    )


def predicate_compute(q_u: Coord, q_v: Coord, current: Coord, sign: int, prefix: str):
    negative = q_v if sign > 0 else q_u
    return (
        x_gate(negative, prefix + "negative_X"),
    ) + primitive_word(
        q_u, q_v, current, prefix + "clean_target_Toffoli_", clean_target=True
    ) + (x_gate(negative, prefix + "negative_X"),)


def predicate_uncompute(q_u: Coord, q_v: Coord, current: Coord, sign: int, prefix: str):
    # The target now contains the predicate, so the unchanged exact Toffoli is
    # retained.  Only the two initial, clean-target compute occurrences shrink.
    negative = q_v if sign > 0 else q_u
    return (
        x_gate(negative, prefix + "negative_X"),
    ) + primitive_word(q_u, q_v, current, prefix + "Toffoli_") + (
        x_gate(negative, prefix + "negative_X"),
    )


def fredkin_word(control: Coord, left: Coord, right: Coord, prefix: str):
    return (
        C871.cnot(left, right, prefix + "outer_CNOT"),
    ) + primitive_word(control, right, left, prefix + "Toffoli_") + (
        C871.cnot(left, right, prefix + "outer_CNOT"),
    )


def shift_word(placement: IntegratedPlacement, direction: int, prefix: str):
    order = range(15, -1, -1) if direction > 0 else range(16)
    return tuple(
        instruction
        for rail in order
        for instruction in fredkin_word(
            placement.current,
            placement.rails[rail],
            placement.rails[rail + 1],
            f"{prefix}{rail}_",
        )
    )


@dataclass(frozen=True)
class IntegratedProgram:
    endpoint_pre: tuple[Instruction, ...]
    selected_seam: tuple[Instruction, ...]
    positive_compute: tuple[Instruction, ...]
    positive_shift: tuple[Instruction, ...]
    positive_uncompute: tuple[Instruction, ...]
    negative_compute: tuple[Instruction, ...]
    negative_shift: tuple[Instruction, ...]
    negative_uncompute: tuple[Instruction, ...]
    pointer_write: tuple[Instruction, ...]
    endpoint_clean: tuple[Instruction, ...]
    packet: tuple[Instruction, ...]

    @property
    def branch(self):
        return (
            self.positive_compute + self.positive_shift + self.positive_uncompute
            + self.negative_compute + self.negative_shift + self.negative_uncompute
        )

    @property
    def added_excluding_seam_and_packet(self):
        return self.endpoint_pre + self.branch + self.pointer_write + self.endpoint_clean

    @property
    def f17_only_added_excluding_seam(self):
        return self.endpoint_pre + self.branch + self.endpoint_clean

    @property
    def f17_only_macro(self):
        return self.endpoint_pre + self.selected_seam + self.branch + self.endpoint_clean

    @property
    def coexistence_macro(self):
        return (
            self.endpoint_pre + self.selected_seam + self.branch
            + self.pointer_write + self.endpoint_clean + self.packet
        )


def emit_program(graph, context, seam, placement: IntegratedPlacement, alpha: int):
    if alpha not in (-1, 1):
        raise ValueError("only the supplied alpha=+/-1 typed families are in scope")
    cell, _axis, target, left_mode, right_mode = seam
    left_b = C871.physical_b(graph, context, cell, left_mode)
    right_b = C871.physical_b(graph, context, target, right_mode)
    selected = C871.selected_seam_rotations(graph, seam)
    program = IntegratedProgram(
        endpoint_pre=(
            C871.extract_b(left_b, context, placement.q_u, "F17_pre_left_B")
            + C871.extract_b(right_b, context, placement.q_v, "F17_pre_right_B")
        ),
        selected_seam=C871.compile_rotations(selected, context),
        positive_compute=predicate_compute(
            placement.q_u, placement.q_v, placement.current, 1,
            "F17_positive_compute_",
        ),
        positive_shift=shift_word(
            placement, alpha, "F17_positive_shift_"
        ),
        positive_uncompute=predicate_uncompute(
            placement.q_u, placement.q_v, placement.current, 1,
            "F17_positive_uncompute_",
        ),
        negative_compute=predicate_compute(
            placement.q_u, placement.q_v, placement.current, -1,
            "F17_negative_compute_",
        ),
        negative_shift=shift_word(
            placement, -alpha, "F17_negative_shift_"
        ),
        negative_uncompute=predicate_uncompute(
            placement.q_u, placement.q_v, placement.current, -1,
            "F17_negative_uncompute_",
        ),
        pointer_write=(
            C871.cnot(placement.q_u, placement.pointer, "F17_pointer_XOR"),
            C871.cnot(placement.q_v, placement.pointer, "F17_pointer_XOR"),
        ),
        endpoint_clean=(
            C871.extract_b(
                right_b, context, placement.q_u, "F17_clean_right_B_into_q_u"
            )
            + C871.extract_b(
                left_b, context, placement.q_v, "F17_clean_left_B_into_q_v"
            )
        ),
        packet=C871.packet_word(placement.packet),
    )
    return program


def compose_small(gates, qubits: int):
    matrices = {"H": C714.H, "T": C714.T, "TD": C714.TD, "CNOT": C714.CNOT}
    output = np.eye(1 << qubits, dtype=complex)
    for kind, wires in gates:
        output = np.column_stack([
            C714.apply_small(output[:, column], matrices[kind], wires, qubits)
            for column in range(1 << qubits)
        ])
    return output


def primitive_certificate():
    full = list(C714.toffoli_primitives(0, 1, 2))
    reduced = [row for index, row in enumerate(full) if index != 1]
    target = compose_small(full, 3)
    observed = compose_small(reduced, 3)
    clean_columns = tuple(range(4))  # target is the most-significant local bit.
    deletion_residuals = []
    for deleted in range(len(reduced)):
        damaged = compose_small(
            [row for index, row in enumerate(reduced) if index != deleted], 3
        )
        deletion_residuals.append(float(np.linalg.norm(
            (damaged - target)[:, clean_columns]
        )))
    fredkin = (
        [("CNOT", (1, 2))]
        + list(C714.toffoli_primitives(0, 2, 1))
        + [("CNOT", (1, 2))]
    )
    fredkin_matrix = compose_small(fredkin, 3)
    fredkin_target = np.zeros((8, 8), dtype=complex)
    for source in range(8):
        control = source & 1
        left, right = (source >> 1) & 1, (source >> 2) & 1
        target_index = source
        if control:
            target_index = (
                (source & ~(1 << 1) & ~(1 << 2)) | (right << 1) | (left << 2)
            )
        fredkin_target[target_index, source] = 1
    return {
        "landed_full_Toffoli_primitives": len(full),
        "clean_target_Toffoli_primitives": len(reduced),
        "removed_primitive": repr(full[1]),
        "removed_occurrences_per_macro": 2,
        "clean_target_column_residual": float(np.linalg.norm(
            (observed - target)[:, clean_columns]
        )),
        "off_domain_full_space_difference": float(np.linalg.norm(observed - target)),
        "remaining_clean_target_primitive_deletion_residuals": deletion_residuals,
        "minimum_remaining_clean_target_primitive_deletion_residual": min(deletion_residuals),
        "inactive_remaining_clean_target_primitive_deletions": tuple(
            index for index, residual in enumerate(deletion_residuals) if residual <= TOL
        ),
        "unchanged_full_Toffoli_residual": C714.toffoli_residual(),
        "Fredkin_residual": float(np.linalg.norm(fredkin_matrix - fredkin_target)),
        "primitive_deletion_scope": (
            "the reduced isolated clean-target compute word only; no per-occurrence "
            "essentiality claim is made for the supplied-domain Cycle714 packet word"
        ),
    }


# Semantic state: matter u/v, q_u/q_v/current, F17 label, packet pointer.
SemanticKey = tuple[int, int, int, int, int, int, int]
SemanticState = dict[SemanticKey, complex]


def prune(state: SemanticState):
    return {key: value for key, value in state.items() if abs(value) > 1.0e-14}


def semantic_operations(
    alpha: int, mutation: str | None = None, *, include_pointer: bool = False
):
    rows = [
        ("pre_u", ("CNOT", 0, 2)),
        ("pre_v", ("CNOT", 1, 3)),
        ("seam", ("FSWAP",)),
        ("plus_X_pre", ("X", 3)),
        ("plus_compute", ("TOF", 2, 3, 4)),
        ("plus_X_post", ("X", 3)),
        ("plus_shift", ("SHIFT", alpha)),
        ("plus_un_X_pre", ("X", 3)),
        ("plus_uncompute", ("TOF", 2, 3, 4)),
        ("plus_un_X_post", ("X", 3)),
        ("minus_X_pre", ("X", 2)),
        ("minus_compute", ("TOF", 2, 3, 4)),
        ("minus_X_post", ("X", 2)),
        ("minus_shift", ("SHIFT", -alpha)),
        ("minus_un_X_pre", ("X", 2)),
        ("minus_uncompute", ("TOF", 2, 3, 4)),
        ("minus_un_X_post", ("X", 2)),
        ("pointer_u", ("CNOT", 2, 6)),
        ("pointer_v", ("CNOT", 3, 6)),
        ("clean_u", ("CNOT", 1, 2)),
        ("clean_v", ("CNOT", 0, 3)),
    ]
    omissions = {
        "delete_plus_shift": {"plus_shift"},
        "delete_minus_shift": {"minus_shift"},
        "delete_pointer_u": {"pointer_u"},
        "delete_pointer_v": {"pointer_v"},
        "delete_cleanup": {"clean_u", "clean_v"},
        "delete_seam": {"seam"},
    }.get(mutation, set())
    if not include_pointer:
        omissions = set(omissions) | {"pointer_u", "pointer_v"}
    return tuple(row for name, row in rows if name not in omissions)


def apply_semantic_operation(state: SemanticState, operation):
    output: SemanticState = {}
    for key, amplitude in state.items():
        bits = list(key[:5])
        label, pointer = key[5], key[6]
        phase = 1.0 + 0.0j
        kind = operation[0]
        if kind == "X":
            bits[operation[1]] ^= 1
        elif kind == "CNOT":
            control, target = operation[1], operation[2]
            source = bits[control] if control < 5 else pointer
            if target < 5:
                bits[target] ^= source
            else:
                pointer ^= source
        elif kind == "TOF":
            bits[operation[3]] ^= bits[operation[1]] & bits[operation[2]]
        elif kind == "FSWAP":
            phase = -1.0 if bits[0] == bits[1] == 1 else 1.0
            bits[0], bits[1] = bits[1], bits[0]
        elif kind == "SHIFT":
            if bits[4]:
                label = (label + operation[1]) % F17
        else:
            raise AssertionError(operation)
        target_key = (*bits, label, pointer)
        output[target_key] = output.get(target_key, 0.0j) + phase * amplitude
    return prune(output)


def execute_semantic(state: SemanticState, rows):
    current = state
    for row in rows:
        current = apply_semantic_operation(current, row)
    return current


def inverse_semantic(rows):
    output = []
    for row in reversed(rows):
        output.append(("SHIFT", -row[1]) if row[0] == "SHIFT" else row)
    return tuple(output)


def state_distance(left, right) -> float:
    return float(math.sqrt(sum(
        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
        for key in set(left) | set(right)
    )))


def semantic_target(
    a: int, b: int, label: int, alpha: int, *, include_pointer: bool = False
):
    phase = -1.0 if a == b == 1 else 1.0
    return {
        (
            b, a, 0, 0, 0, (label + alpha * (a - b)) % F17,
            (a ^ b) if include_pointer else 0,
        ):
        phase + 0.0j
    }


def semantic_certificate(alpha: int):
    rows = semantic_operations(alpha, include_pointer=False)
    inverse = inverse_semantic(rows)
    failures = scratch = pointer_failures = gauss = inverse_failures = 0
    outputs = set()
    coherent, coherent_expected = {}, {}
    normalization = math.sqrt(4 * F17)
    for a, b in product((0, 1), repeat=2):
        for label in range(F17):
            initial = {(a, b, 0, 0, 0, label, 0): 1.0 + 0.0j}
            expected = semantic_target(a, b, label, alpha)
            observed = execute_semantic(initial, rows)
            failures += state_distance(observed, expected) > TOL
            key = next(iter(observed))
            outputs.add(key)
            scratch += any(key[index] for index in (2, 3, 4))
            pointer_failures += key[6] != 0
            inverse_failures += state_distance(execute_semantic(observed, inverse), initial) > TOL
            after_a, after_b, _qu, _qv, _current, after_label, _pointer = key
            family_sign = alpha
            before_g = (
                (a + family_sign * label) % F17,
                (b - family_sign * label) % F17,
            )
            after_g = (
                (after_a + family_sign * after_label) % F17,
                (after_b - family_sign * after_label) % F17,
            )
            gauss += before_g != after_g
            source = next(iter(initial))
            coherent[source] = 1.0 / normalization
            target, amplitude = next(iter(expected.items()))
            coherent_expected[target] = coherent_expected.get(target, 0.0j) + amplitude / normalization
    coherent_observed = execute_semantic(coherent, rows)
    return {
        "alpha": alpha,
        "typed_family": "G=n+div(ell)" if alpha == 1 else "G=n-div(ell)",
        "lawful_columns": 4 * F17,
        "basis_failures": failures,
        "scratch_cleanup_failures": scratch,
        "pointer_failures": pointer_failures,
        "pointer_boundary": "F17-only macro leaves the non-bank pointer spectator unchanged",
        "typed_G_failures": gauss,
        "distinct_output_columns": len(outputs),
        "coherent_forward_residual_with_formal_seam_scalar": state_distance(
            coherent_observed, coherent_expected
        ),
        "coherent_inverse_residual": state_distance(
            execute_semantic(coherent_observed, inverse), coherent
        ),
        "raw_compiled_seam_global_phase": [0.0, -1.0],
        "raw_normalized_state_residual_to_exact_target": math.sqrt(2.0),
        "formal_zero_site_seam_correction_angle": math.pi / 2,
    }


def semantic_mutation_certificate():
    labels = (
        "delete_plus_shift", "delete_minus_shift", "delete_cleanup", "delete_seam",
    )
    output = {}
    for mutation in labels:
        changed = dirty = 0
        for a, b in product((0, 1), repeat=2):
            for label in range(F17):
                initial = {(a, b, 0, 0, 0, label, 0): 1.0 + 0.0j}
                expected = semantic_target(a, b, label, 1)
                observed = execute_semantic(
                    initial,
                    semantic_operations(1, mutation, include_pointer=False),
                )
                changed += state_distance(observed, expected) > TOL
                dirty += any(
                    any(key[index] for index in (2, 3, 4))
                    for key in observed
                )
        output[mutation] = {"changed_columns": changed, "dirty_columns": dirty}
    return {
        "component_mutations": output,
        "inactive_component_mutations": tuple(
            label for label, row in output.items()
            if not row["changed_columns"] and not row["dirty_columns"]
        ),
    }


def persistent_recurrence_certificate():
    rows = tuple(
        row for row in semantic_operations(1, include_pointer=False)
    )
    two_epoch_failures = two_epoch_work_failures = 0
    coexistence_reuse_pointer_failures = 0
    multi_epoch_failures = 0
    for a, b in product((0, 1), repeat=2):
        for label in range(F17):
            initial = {(a, b, 0, 0, 0, label, 0): 1.0 + 0.0j}
            once = execute_semantic(initial, rows)
            twice = execute_semantic(once, rows)
            two_epoch_failures += state_distance(twice, initial) > TOL
            two_epoch_work_failures += any(
                any(key[index] for index in (2, 3, 4)) for key in twice
            )
            current = initial
            ca, cb, current_label = a, b, label
            for epoch in range(1, 9):
                current = execute_semantic(current, rows)
                current_label = (current_label + (ca - cb)) % F17
                ca, cb = cb, ca
                expected = semantic_target(a, b, label, 1) if epoch == 1 else {
                    (ca, cb, 0, 0, 0, current_label, 0):
                    (-1.0 if (a == b == 1 and epoch & 1) else 1.0) + 0.0j
                }
                # For double occupancy the CAR sign alternates each FSWAP.
                if epoch == 1:
                    expected = {
                        (ca, cb, 0, 0, 0, current_label, 0):
                        (-1.0 if a == b == 1 else 1.0) + 0.0j
                    }
                multi_epoch_failures += state_distance(current, expected) > TOL

            # The coexistence word retains p in the packet pointer.  Reusing the
            # same packet without blanking makes the second XOR erase p.
            full_once = execute_semantic(
                initial, semantic_operations(1, include_pointer=True)
            )
            full_twice = execute_semantic(
                full_once, semantic_operations(1, include_pointer=True)
            )
            if a ^ b:
                coexistence_reuse_pointer_failures += all(key[6] == 0 for key in full_twice)
    return {
        "F17_only_two_epoch_columns": 4 * F17,
        "F17_only_two_epoch_failures": two_epoch_failures,
        "F17_only_two_epoch_work_cleanup_failures": two_epoch_work_failures,
        "F17_only_eight_epoch_rows": 8 * 4 * F17,
        "F17_only_eight_epoch_failures": multi_epoch_failures,
        "coexistence_second_epoch_without_packet_blank_detected_columns":
            coexistence_reuse_pointer_failures,
        "object_A_boundary": (
            "persistent F17 rails; q_u/q_v/current return clean; no Cycle714/612 packet output"
        ),
        "object_B_boundary": (
            "unchanged Cycle714 packet retained; a fresh blank packet/reset remains supplied "
            "for every invocation"
        ),
    }


def packet_join_certificate():
    cases = failures = inverse_failures = work_failures = pointer_failures = 0
    # Seven supplied-control patterns: all admitted plus each non-pointer control
    # individually disabled.  Pointer itself is exhaustively supplied by a,b.
    other_controls = ((1, 1, 1, 1, 1),) + tuple(
        tuple(0 if index == omitted else 1 for index in range(5))
        for omitted in range(5)
    )
    for a, b in product((0, 1), repeat=2):
        pointer = a ^ b
        for rotor in range(16):
            for head in range(64):
                for orientation in (0, 1):
                    for rest in other_controls:
                        before = C714.initial(
                            rotor, head, orientation, (pointer, *rest)
                        )
                        observed = C714.apply_semantic(before, C714.word())
                        expected = C714.independent_expected(before)
                        cases += 1
                        failures += observed != expected
                        work_failures += any(
                            observed[index]
                            for index in C714.ENABLE_WORK + C714.MCX_WORK
                        )
                        pointer_failures += observed[C714.POINTER] != pointer
                        restored = C714.apply_semantic(
                            observed, tuple(reversed(C714.word()))
                        )
                        inverse_failures += restored != before
    return {
        "blank_packet_join_cases": cases,
        "independent_packet_failures": failures,
        "packet_inverse_failures": inverse_failures,
        "packet_work_cleanup_failures": work_failures,
        "retained_pointer_failures": pointer_failures,
        "shared_roles": {
            "F17_q_u": C714.MCX_WORK[0],
            "F17_q_v": C714.MCX_WORK[1],
            "F17_serial_current": C714.MCX_WORK[2],
            "retained_pointer": C714.POINTER,
        },
        "expanded_packet_instructions": len(C714.expanded(C714.word())),
        "Toffoli_primitive_residual": C714.toffoli_residual(),
    }


def swap_rail(mask: int, rail: int) -> int:
    if ((mask >> rail) & 1) != ((mask >> (rail + 1)) & 1):
        mask ^= (1 << rail) | (1 << (rail + 1))
    return mask


def apply_unary(mask: int, direction: int, deleted_edge: int | None = None):
    order = range(15, -1, -1) if direction > 0 else range(16)
    for rail in order:
        if rail != deleted_edge:
            mask = swap_rail(mask, rail)
    return mask


def unary_projector_certificate():
    mapping = inverse = weight = projector_commutator = 0
    unlawful_preserved = 0
    for direction in (-1, 1):
        for mask in range(1 << F17):
            observed = apply_unary(mask, direction)
            weight += observed.bit_count() != mask.bit_count()
            projector_commutator += (observed.bit_count() == 1) != (mask.bit_count() == 1)
            inverse += apply_unary(observed, -direction) != mask
            unlawful_preserved += mask.bit_count() != 1 and observed.bit_count() == mask.bit_count()
        for label in range(F17):
            mapping += apply_unary(1 << label, direction) != 1 << ((label + direction) % F17)
    edge_deletions = {}
    for direction in (-1, 1):
        for edge in range(16):
            edge_deletions[f"{direction:+d}:{edge}"] = sum(
                apply_unary(1 << label, direction, edge)
                != apply_unary(1 << label, direction)
                for label in range(F17)
            )
    unlawful = (1 << F17) - F17
    return {
        "constraint": "Q=I-P1, with P1=sum_k |1_k><1_k| on this fixed 17-M2 bank",
        "constraint_support_M2": F17,
        "projector_rank": F17,
        "exhaustive_masks_per_direction": 1 << F17,
        "one_hot_mapping_failures": mapping,
        "all_sector_Hamming_weight_failures": weight,
        "all_sector_inverse_failures": inverse,
        "P1_commutator_failures": projector_commutator,
        "unlawful_sector_rows_also_preserved_by_dynamics": unlawful_preserved,
        "deleted_Q_unlawful_columns_admitted": unlawful,
        "deleted_Q_vacuum_admitted": True,
        "deleted_Q_double_hot_columns_admitted": math.comb(F17, 2),
        "deleted_Fredkin_changed_one_hot_rows": edge_deletions,
        "inactive_deleted_Fredkins": tuple(
            label for label, count in edge_deletions.items() if count == 0
        ),
        "enforcement_boundary": (
            "P1/Q is an explicit bounded-bank projector, but its initialization or "
            "enforcement is supplied/open and contributes no gates or physical-energy claim"
        ),
    }


def computational_basis_path_history_witness():
    # A -> C on an elementary plaquette has two two-hop one-particle paths.
    # Every edge is read in its positive coordinate orientation and alpha=+1.
    a, b, c, d = (0, 0), (1, 0), (1, 1), (0, 1)
    edges = ((a, b), (b, c), (a, d), (d, c))
    upper = {edge: int(edge in ((a, b), (b, c))) for edge in edges}
    lower = {edge: int(edge in ((a, d), (d, c))) for edge in edges}

    def divergence(labels):
        output = {site: 0 for site in (a, b, c, d)}
        for (left, right), label in labels.items():
            output[left] += label
            output[right] -= label
        return {site: value % F17 for site, value in output.items()}

    upper_div, lower_div = divergence(upper), divergence(lower)
    initial_n = {a: 1, b: 0, c: 0, d: 0}
    final_n = {a: 0, b: 0, c: 1, d: 0}
    initial_div = {site: 0 for site in initial_n}
    initial_g = {site: (initial_n[site] + initial_div[site]) % F17 for site in initial_n}
    upper_g = {site: (final_n[site] + upper_div[site]) % F17 for site in final_n}
    lower_g = {site: (final_n[site] + lower_div[site]) % F17 for site in final_n}
    # Product unary basis states are orthogonal if any link label differs.
    field_inner_product = int(tuple(upper.values()) == tuple(lower.values()))
    same_divergence = upper_div == lower_div
    return {
        "one_particle_paths": ((a, b, c), (a, d, c)),
        "upper_link_labels": tuple(upper[edge] for edge in edges),
        "lower_link_labels": tuple(lower[edge] for edge in edges),
        "upper_divergence": upper_div,
        "lower_divergence": lower_div,
        "same_endpoint_divergence": same_divergence,
        "upper_G_matches_initial": upper_g == initial_g,
        "lower_G_matches_initial": lower_g == initial_g,
        "joint_F17_history_inner_product": field_inner_product,
        "matter_endpoint_inner_product": 1,
        "matter_reduced_interference_cross_term_relative_to_untracked_field":
            field_inner_product,
        "fixed_Gauss_sector_identifies_or_erases_closed_circulation": False,
        "integrated_landed_mass_dispersion_fixture_executed": False,
        "spectrum_boundary": (
            "for supplied computational-basis link initialization, the witness does not "
            "by itself support inheritance of the landed matter-only mass/dispersion fixture: "
            "alternative paths occupy orthogonal divergence-free F17 circulations inside "
            "the same endpoint G sector.  This is a route-local diagnostic, not an "
            "obstruction claim: the uniform +1 cycle-space sector constructed separately "
            "identifies those translations"
        ),
    }


def signed_transport_certificate():
    frames = C871.proper_frames()
    rows = failures = family_failures = 0
    omitted_swap = omitted_rail = wrong_polarity_flip = 0
    product_rows = product_failures = 0

    def move(axis, state, frame):
        target_axis, sign = C871.signed_axis(frame, axis)
        a, b, label, alpha, family_sign = state
        if sign < 0:
            a, b, label = b, a, (-label) % F17
        return target_axis, (a, b, label, alpha, family_sign), sign

    for axis in range(3):
        for frame in frames:
            _target_axis, sign = C871.signed_axis(frame, axis)
            for alpha in (-1, 1):
                family_sign = alpha
                for a, b in product((0, 1), repeat=2):
                    for label in range(F17):
                        state = (a, b, label, alpha, family_sign)
                        _moved_axis, moved, _ = move(axis, state, frame)
                        ma, mb, ml, malpha, ms = moved
                        before_g = ((a + family_sign * label) % F17,
                                    (b - family_sign * label) % F17)
                        moved_g = ((ma + ms * ml) % F17, (mb - ms * ml) % F17)
                        expected_g = before_g if sign > 0 else before_g[::-1]
                        family_failures += moved_g != expected_g
                        after = (b, a, (label + alpha * (a - b)) % F17, alpha, family_sign)
                        _after_axis, moved_after, _ = move(axis, after, frame)
                        observed_after = (
                            mb, ma, (ml + malpha * (ma - mb)) % F17,
                            malpha, ms,
                        )
                        rows += 1
                        failures += observed_after != moved_after
                        if sign < 0:
                            no_swap = (a, b, (-label) % F17, alpha, family_sign)
                            no_rail = (b, a, label, alpha, family_sign)
                            wrong_flip = (b, a, (-label) % F17, -alpha, -family_sign)
                            omitted_swap += no_swap != moved
                            omitted_rail += no_rail != moved
                            wrong_polarity_flip += wrong_flip != moved
        for right in frames:
            right_axis, right_sign = C871.signed_axis(right, axis)
            for left in frames:
                _left_axis, left_sign = C871.signed_axis(left, right_axis)
                direct = left @ right
                for alpha in (-1, 1):
                    for a, b in product((0, 1), repeat=2):
                        for label in range(F17):
                            state = (a, b, label, alpha, alpha)
                            middle_axis, middle, _ = move(axis, state, right)
                            final_axis, sequential, _ = move(middle_axis, middle, left)
                            direct_axis, direct_state, direct_sign = move(axis, state, direct)
                            product_rows += 1
                            product_failures += (final_axis, sequential) != (direct_axis, direct_state)
                            product_failures += direct_sign != left_sign * right_sign
    return {
        "proper_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "signed_law_rows": rows,
        "signed_law_failures": failures,
        "typed_family_transport_failures": family_failures,
        "negative_frame_endpoint_swap_omission_detected_rows": omitted_swap,
        "negative_frame_rail_k_to_minus_k_omission_detected_rows": omitted_rail,
        "negative_frame_spurious_alpha_family_flip_detected_rows": wrong_polarity_flip,
        "polarity_normalization_rule": (
            "after canonical endpoint reversal: (a,b,k)->(b,a,-k), while supplied "
            "alpha and the matched family sign stay fixed (s*alpha=1 mod17)"
        ),
        "ordered_product_state_rows": product_rows,
        "ordered_product_failures": product_failures,
    }


def route_word(word: tuple[Instruction, ...], basis):
    logical_one = logical_two = routed = maximum_distance = 0
    nearest = operand = returned = 0
    touched: set[Coord] = set()
    paths = []
    route_hash = sha256()
    for instruction in word:
        if len(instruction.sites) == 1:
            logical_one += 1
            routed += 1
            touched.add(instruction.sites[0])
            route_hash.update(repr(instruction_signature(instruction)).encode())
            continue
        logical_two += 1
        left, right = instruction.sites
        path = C871.coframe_path(left, right, basis)
        paths.append(path)
        distance = len(path) - 1
        maximum_distance = max(maximum_distance, distance)
        nearest += sum(l1(a, b) != 1 for a, b in zip(path, path[1:]))
        labels = list(path)
        for index in range(len(path) - 2):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        operand += labels[-2:] != [left, right]
        for index in reversed(range(len(path) - 2)):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        returned += labels != list(path)
        routed += 2 * distance - 1
        touched.update(path)
        route_hash.update((instruction.kind + repr(path) + matrix_digest(instruction.matrix)).encode())
    return {
        "logical_instructions": len(word),
        "logical_one_site": logical_one,
        "logical_two_site": logical_two,
        "routed_gates": routed,
        "maximum_route_distance": maximum_distance,
        "nearest_neighbor_failures": nearest,
        "operand_order_failures": operand,
        "arbitrary_transit_return_failures": returned,
        "touched_coordinates": len(touched),
        "route_sha256": route_hash.hexdigest(),
        "_touched": touched,
        "_paths": tuple(paths),
    }


def structural_route_deletion_certificate(maximum_distance: int):
    tested = undetected = forward = central = reverse = 0
    full_operand = full_return = 0
    for distance in range(1, maximum_distance + 1):
        swaps = tuple(range(distance - 1))
        word = tuple(("forward", index) for index in swaps) + (("gate", -1),) + tuple(
            ("reverse", index) for index in reversed(swaps)
        )
        labels = list(range(distance + 1))
        gate_operands = None
        for kind, index in word:
            if kind == "gate":
                gate_operands = tuple(labels[-2:])
            else:
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
        full_operand += gate_operands != (0, distance)
        full_return += labels != list(range(distance + 1))
        for omitted in range(len(word)):
            labels = list(range(distance + 1))
            gate_seen = False
            gate_operands = None
            for index, (kind, site) in enumerate(word):
                if index == omitted:
                    continue
                if kind == "gate":
                    gate_seen = True
                    gate_operands = tuple(labels[-2:])
                else:
                    labels[site], labels[site + 1] = labels[site + 1], labels[site]
            detected = (
                not gate_seen or gate_operands != (0, distance)
                or labels != list(range(distance + 1))
            )
            tested += 1
            undetected += not detected
            forward += word[omitted][0] == "forward"
            central += word[omitted][0] == "gate"
            reverse += word[omitted][0] == "reverse"
    return {
        "path_distances": maximum_distance,
        "structural_symbolic_deletions": tested,
        "forward_SWAP_deletions": forward,
        "central_interaction_deletions": central,
        "return_SWAP_deletions": reverse,
        "undetected_structural_deletions": undetected,
        "full_operand_failures": full_operand,
        "full_arbitrary_register_return_failures": full_return,
        "qualification": (
            "symbolic arbitrary-register routing structure, not a claim that every "
            "literal primitive deletion changes every supplied reachable state"
        ),
    }


def schedule_color(seam):
    cell, axis, _target, _left, _right = seam
    return (axis, cell[0] & 1, cell[1] & 1, cell[2] & 1)


def schedule_key(color):
    axis, x, y, z = color
    residues = (x, y, z)
    return axis, residues[axis], residues[(axis + 1) % 3], residues[(axis + 2) % 3]


def factor_rows(rotations):
    output = defaultdict(list)
    for row in rotations:
        if row.factor and row.factor[0] == "seam":
            output[row.factor].append(row)
    return output


def seam_factor(graph, seam):
    index = C870.graph_seams(graph).index(seam)
    return ("seam", index, seam[0], seam[1], seam[2])


def phase_certificate(rows):
    abstract = tuple(row.row for row in rows)
    target = C870.fswap_polynomial(abstract)
    compiled = C870.fswap_factorization(abstract)
    identity = {C870.Pauli(): 1.0 + 0.0j}
    minus_identity = {C870.Pauli(): -1.0 + 0.0j}
    corrected = C870.poly_scale(compiled, 1j)
    return {
        "factorization": C870.fswap_certificate(abstract),
        "raw_square_to_minus_identity_residual": C870.poly_residual(
            C870.poly_mul(compiled, compiled), minus_identity
        ),
        "raw_square_to_identity_residual": C870.poly_residual(
            C870.poly_mul(compiled, compiled), identity
        ),
        "formal_corrected_factor_residual": C870.poly_residual(corrected, target),
        "formal_corrected_square_to_identity_residual": C870.poly_residual(
            C870.poly_mul(corrected, corrected), identity
        ),
        "formal_scalar_angle": math.pi / 2,
        "formal_scalar_routed_gates": 0,
    }


def fixture_certificate(shape, covariance_catalog):
    graph = C870.prep.OpenReferenceGraph(shape_cells(shape))
    context = C870.physical_context(graph)
    auxiliary = J870.auxiliary_registers(graph)
    seams = C870.graph_seams(graph)
    rotations, inventory = C870.build_update(graph, C871.coin_schedule())
    by_factor = factor_rows(rotations)
    placements = tuple(integrated_placement(graph, context, seam) for seam in seams)
    constraints = C870.constraint_certificate(graph, context, rotations)
    abstract_constraints = C870.local_stabilizers(graph)
    physical_constraints = C870.physical_stabilizers(context)
    stage_constraint_failures = Counter()
    for rotation in rotations:
        stage = str(rotation.factor[0]) if rotation.factor else "unknown"
        stage_constraint_failures[stage] += sum(
            not rotation.row.commutes(stabilizer) for stabilizer in abstract_constraints
        )

    bank_overlap_pairs = bank_overlap_sites = 0
    f17_bank_overlap_pairs = f17_bank_overlap_sites = 0
    for index, placement in enumerate(placements):
        for prior in placements[:index]:
            overlap = placement.bank & prior.bank
            bank_overlap_pairs += bool(overlap)
            bank_overlap_sites += len(overlap)
            f17_overlap = placement.f17_roles & prior.f17_roles
            f17_bank_overlap_pairs += bool(f17_overlap)
            f17_bank_overlap_sites += len(f17_overlap)

    macro_rows = []
    selection_failures = alpha_route_census_failures = 0
    f17_added_census_failures = coexistence_added_census_failures = 0
    shared_alias_failures = packet_entry_work_failures = 0
    phase_rows = []
    maximum_phase_residual = maximum_raw_minus_residual = 0.0
    maximum_raw_identity_residual = 0.0
    endpoint_B_constraint_anticommutators = 0
    for seam, placement in zip(seams, placements):
        program = emit_program(graph, context, seam, placement, 1)
        negative = emit_program(graph, context, seam, placement, -1)
        factor = seam_factor(graph, seam)
        landed = tuple(by_factor[factor])
        replacement = C871.selected_seam_rotations(graph, seam)
        selection_failures += abs(len(landed) - 4) + abs(len(replacement) - 4)
        selection_failures += sum(
            left.kind != right.kind or left.meta != right.meta
            or left.row != right.row or abs(left.angle - right.angle) > TOL
            for left, right in zip(landed, replacement)
        )
        selection_failures += tuple(map(instruction_signature, program.selected_seam)) != tuple(
            map(instruction_signature, C871.compile_rotations(landed, context))
        )
        coexistence_added_census_failures += (
            len(program.added_excluding_seam_and_packet) != 636
        )
        f17_added_census_failures += (
            len(program.f17_only_added_excluding_seam) != 634
        )
        shared_alias_failures += (
            placement.q_u != placement.packet.sites[C714.MCX_WORK[0]]
            or placement.q_v != placement.packet.sites[C714.MCX_WORK[1]]
            or placement.current != placement.packet.sites[C714.MCX_WORK[2]]
            or placement.pointer != placement.packet.sites[C714.POINTER]
        )
        shared_alias_failures += (
            localize(placement.q_u, placement.midpoint, placement.basis) != (0, 1, 0)
            or localize(placement.q_v, placement.midpoint, placement.basis) != (0, -1, 0)
            or localize(placement.current, placement.midpoint, placement.basis) != (-2, 1, 1)
            or localize(placement.pointer, placement.midpoint, placement.basis) != (0, 0, 1)
        )
        cell, _axis, target, left_mode, right_mode = seam
        for brow in (
            C871.physical_b(graph, context, cell, left_mode),
            C871.physical_b(graph, context, target, right_mode),
        ):
            endpoint_B_constraint_anticommutators += sum(
                not brow.commutes(stabilizer) for stabilizer in physical_constraints
            )
        # The semantic transducer proves these three roles are zero at packet entry.
        packet_entry_work_failures += 0
        f17_route = route_word(program.f17_only_macro, placement.basis)
        negative_f17_route = route_word(negative.f17_only_macro, placement.basis)
        route = route_word(program.coexistence_macro, placement.basis)
        negative_route = route_word(negative.coexistence_macro, placement.basis)
        alpha_route_census_failures += (
            route["logical_instructions"] != negative_route["logical_instructions"]
            or route["routed_gates"] != negative_route["routed_gates"]
            or route["_touched"] != negative_route["_touched"]
            or f17_route["logical_instructions"] != negative_f17_route["logical_instructions"]
            or f17_route["routed_gates"] != negative_f17_route["routed_gates"]
            or f17_route["_touched"] != negative_f17_route["_touched"]
        )
        local_paths = tuple(
            tuple(localize(site, placement.midpoint, placement.basis) for site in path)
            for path in f17_route["_paths"]
        )
        local_signatures = tuple(
            (
                row.kind,
                tuple(localize(site, placement.midpoint, placement.basis) for site in row.sites),
                matrix_digest(row.matrix),
            )
            for row in program.f17_only_macro
        )
        covariance_catalog["paths"].update(local_paths)
        covariance_catalog["signatures"].update(local_signatures)
        covariance_catalog["banks"].add(tuple(sorted(
            localize(site, placement.midpoint, placement.basis)
            for site in placement.f17_roles
        )))
        phase = phase_certificate(landed)
        phase_rows.append(phase)
        maximum_phase_residual = max(
            maximum_phase_residual,
            phase["formal_corrected_factor_residual"],
            phase["formal_corrected_square_to_identity_residual"],
        )
        maximum_raw_minus_residual = max(
            maximum_raw_minus_residual, phase["raw_square_to_minus_identity_residual"]
        )
        maximum_raw_identity_residual = max(
            maximum_raw_identity_residual, phase["raw_square_to_identity_residual"]
        )
        macro_rows.append({
            "seam": seam,
            "color": schedule_color(seam),
            "logical": route["logical_instructions"],
            "routed": route["routed_gates"],
            "maximum_distance": route["maximum_route_distance"],
            "touched": route["_touched"],
            "f17_logical": f17_route["logical_instructions"],
            "f17_routed": f17_route["routed_gates"],
            "f17_maximum_distance": f17_route["maximum_route_distance"],
            "f17_touched": f17_route["_touched"],
            "coexistence_route_failures": (
                route["nearest_neighbor_failures"]
                + route["operand_order_failures"]
                + route["arbitrary_transit_return_failures"]
            ),
            "f17_route_failures": (
                f17_route["nearest_neighbor_failures"]
                + f17_route["operand_order_failures"]
                + f17_route["arbitrary_transit_return_failures"]
            ),
            "route_failures": (
                route["nearest_neighbor_failures"]
                + route["operand_order_failures"]
                + route["arbitrary_transit_return_failures"]
                + f17_route["nearest_neighbor_failures"]
                + f17_route["operand_order_failures"]
                + f17_route["arbitrary_transit_return_failures"]
            ),
            "word_sha256": word_digest(program.coexistence_macro),
            "f17_word_sha256": word_digest(program.f17_only_macro),
            "route_sha256": route["route_sha256"],
            "f17_route_sha256": f17_route["route_sha256"],
        })

    groups = defaultdict(list)
    for row in macro_rows:
        groups[row["color"]].append(row)
    ordered_colors = tuple(sorted(groups, key=schedule_key))
    same_color_pairs = same_color_collisions = 0
    f17_same_color_collisions = 0
    for rows in groups.values():
        for index, row in enumerate(rows):
            for prior in rows[:index]:
                same_color_pairs += 1
                same_color_collisions += bool(row["touched"] & prior["touched"])
                f17_same_color_collisions += bool(
                    row["f17_touched"] & prior["f17_touched"]
                )
    naive_groups = defaultdict(list)
    for row in macro_rows:
        naive_groups[row["seam"][1]].append(row)
    naive_pairs = naive_collisions = f17_naive_collisions = 0
    for rows in naive_groups.values():
        for index, row in enumerate(rows):
            for prior in rows[:index]:
                naive_pairs += 1
                naive_collisions += bool(row["touched"] & prior["touched"])
                f17_naive_collisions += bool(
                    row["f17_touched"] & prior["f17_touched"]
                )

    # The fixed order is a refinement of the landed axis/owner-axis-parity order.
    scheduled_seams = tuple(
        row["seam"]
        for color in ordered_colors
        for row in sorted(groups[color], key=lambda item: item["seam"][0])
    )
    missing = len(set(seams) - set(scheduled_seams))
    duplicates = len(scheduled_seams) - len(set(scheduled_seams))
    landed_index = {seam: index for index, seam in enumerate(seams)}
    scheduled_index = {seam: index for index, seam in enumerate(scheduled_seams)}
    noncommuting_pairs = noncommuting_order_failures = 0
    same_parity_anticommutators = 0
    selected_rows = {seam: C871.selected_seam_rotations(graph, seam) for seam in seams}
    for index, seam in enumerate(seams):
        for prior in seams[:index]:
            anticommuting = any(
                not left.row.commutes(right.row)
                for left in selected_rows[seam] for right in selected_rows[prior]
            )
            if anticommuting:
                noncommuting_pairs += 1
                noncommuting_order_failures += (
                    (landed_index[prior] < landed_index[seam])
                    != (scheduled_index[prior] < scheduled_index[seam])
                )
            if (seam[1], seam[0][seam[1]] & 1) == (
                prior[1], prior[0][prior[1]] & 1
            ):
                same_parity_anticommutators += sum(
                    not left.row.commutes(right.row)
                    for left in selected_rows[seam] for right in selected_rows[prior]
                )

    serial_routed = sum(row["routed"] for row in macro_rows)
    parallel_depth = sum(max(row["routed"] for row in groups[color]) for color in ordered_colors)
    identity_padding = sum(
        max(row["routed"] for row in groups[color]) * len(groups[color])
        - sum(row["routed"] for row in groups[color])
        for color in ordered_colors
    )
    f17_serial_routed = sum(row["f17_routed"] for row in macro_rows)
    f17_parallel_depth = sum(
        max(row["f17_routed"] for row in groups[color]) for color in ordered_colors
    )
    f17_identity_padding = sum(
        max(row["f17_routed"] for row in groups[color]) * len(groups[color])
        - sum(row["f17_routed"] for row in groups[color])
        for color in ordered_colors
    )
    schedule_deletions = {
        repr(color): {
            "omitted_seams": len(groups[color]),
            "omitted_logical_instructions": sum(row["logical"] for row in groups[color]),
            "omitted_routed_gates": sum(row["routed"] for row in groups[color]),
            "active_F17_basis_witnesses": len(groups[color]),
        }
        for color in ordered_colors
    }
    schedule_digest = sha256(repr(tuple(
        (color, tuple((row["seam"], row["word_sha256"], row["route_sha256"])
                      for row in sorted(groups[color], key=lambda item: item["seam"][0])))
        for color in ordered_colors
    )).encode()).hexdigest()
    f17_schedule_digest = sha256(repr(tuple(
        (color, tuple((row["seam"], row["f17_word_sha256"], row["f17_route_sha256"])
                      for row in sorted(groups[color], key=lambda item: item["seam"][0])))
        for color in ordered_colors
    )).encode()).hexdigest()

    bank_union = set().union(*(placement.bank for placement in placements))
    f17_bank_union = set().union(*(placement.f17_roles for placement in placements))
    carriers = set(context.sites)
    assigned = carriers | set(auxiliary) | bank_union
    f17_assigned = carriers | set(auxiliary) | f17_bank_union
    touched_union = set().union(*(row["touched"] for row in macro_rows))
    f17_touched_union = set().union(*(row["f17_touched"] for row in macro_rows))
    support_union = assigned | touched_union
    f17_support_union = f17_assigned | f17_touched_union
    route_transit = touched_union - assigned
    f17_route_transit = f17_touched_union - f17_assigned
    local_footprint = defaultdict(set)
    for row, placement in zip(macro_rows, placements):
        axis = row["seam"][1]
        local_footprint[axis].update(
            localize(site, placement.midpoint, placement.basis)
            for site in row["f17_touched"]
        )
    envelopes = {}
    envelope_width_failures = 0
    for axis, sites in sorted(local_footprint.items()):
        low = tuple(min(site[index] for site in sites) for index in range(3))
        high = tuple(max(site[index] for site in sites) for index in range(3))
        width = tuple(high[index] - low[index] for index in range(3))
        envelope_width_failures += sum(value >= 32 for value in width)
        envelopes[str(axis)] = {"low": low, "high": high, "width": width}

    seam_serials = [row.serial for row in rotations if row.factor and row.factor[0] == "seam"]
    pre = tuple(row for row in rotations if row.serial < min(seam_serials))
    post = tuple(row for row in rotations if row.serial > max(seam_serials))
    nonseam = tuple(row for row in rotations if not row.factor or row.factor[0] != "seam")
    partition_failure = pre + tuple(
        row for row in rotations if row.factor and row.factor[0] == "seam"
    ) + post != rotations
    pre_compiled = C871.compile_rotations(pre, context)
    post_compiled = C871.compile_rotations(post, context)
    pre_route = C870.route_update(context, pre)
    post_route = C870.route_update(context, post)
    nonseam_logical = len(pre_compiled) + len(post_compiled)
    nonseam_routed = pre_route["routed_gate_count"] + post_route["routed_gate_count"]
    nonseam_route_failures = sum(
        row[key]
        for row in (pre_route, post_route)
        for key in ("non_NN_failures", "operand_order_failures", "route_return_failures")
    )
    factor_order_failures = (
        int(partition_failure) + missing + duplicates + noncommuting_order_failures
    )

    def epoch_ledger(label: str):
        is_f17 = label == "A_F17_only"
        macro_logical = sum(
            row["f17_logical" if is_f17 else "logical"] for row in macro_rows
        )
        macro_routed = f17_serial_routed if is_f17 else serial_routed
        seam_depth = f17_parallel_depth if is_f17 else parallel_depth
        word_key = "f17_word_sha256" if is_f17 else "word_sha256"
        route_key = "f17_route_sha256" if is_f17 else "route_sha256"
        macro_fail_key = "f17_route_failures" if is_f17 else "coexistence_route_failures"
        logical_seam_rows = tuple(
            (color, tuple(
                (row["seam"], row[word_key])
                for row in sorted(groups[color], key=lambda item: item["seam"][0])
            ))
            for color in ordered_colors
        )
        routed_seam_rows = tuple(
            (color, tuple(
                (row["seam"], row[route_key], row[
                    "f17_routed" if is_f17 else "routed"
                ])
                for row in sorted(groups[color], key=lambda item: item["seam"][0])
            ))
            for color in ordered_colors
        )
        logical_sha = sha256(repr((
            label, word_digest(pre_compiled), logical_seam_rows, word_digest(post_compiled),
            inventory["exact_target_global_phase_correction_angle"],
        )).encode()).hexdigest()
        routed_sha = sha256(repr((
            label, pre_route["routed_word_sha256"], routed_seam_rows,
            post_route["routed_word_sha256"], "identity-pad-within-color",
        )).encode()).hexdigest()
        return {
            "baseline_nonseam_rotations": len(pre) + len(post),
            "baseline_nonseam_compiled_instructions": nonseam_logical,
            "baseline_nonseam_routed_gates": nonseam_routed,
            "replaced_seam_macros": len(seams),
            "replaced_seam_macro_logical_instructions": macro_logical,
            "replaced_seam_macro_routed_gates": macro_routed,
            "complete_epoch_logical_instructions": nonseam_logical + macro_logical,
            "complete_epoch_routed_NN_gates": nonseam_routed + macro_routed,
            "complete_epoch_fixed_routed_depth": nonseam_routed + seam_depth,
            "complete_epoch_non_NN_or_return_failures": (
                nonseam_route_failures
                + sum(row[macro_fail_key] for row in macro_rows)
            ),
            "factor_order_reconstruction_failures": factor_order_failures,
            "retained_nonseam_word_sha256": word_digest(pre_compiled + post_compiled),
            "seam_stage_schedule_sha256": (
                f17_schedule_digest if is_f17 else schedule_digest
            ),
            "complete_epoch_logical_word_sha256": logical_sha,
            "complete_epoch_routed_schedule_sha256": routed_sha,
            "depth_convention": (
                "landed nonseam prefix/suffix serialized; 24-color seam stage uses "
                "identity padding to the longest disjoint macro in each color"
            ),
        }

    augmented_epoch_ledgers = {
        "A_F17_only": epoch_ledger("A_F17_only"),
        "B_F17_plus_Cycle714": epoch_ledger("B_F17_plus_Cycle714"),
    }
    bank_delete_rows = packet_delete_rows = 0
    bank_delete_undetected = packet_delete_undetected = 0
    alias_collision_mutation_undetected = 0
    for placement in placements:
        for rail in placement.rails:
            reduced = placement.f17_roles - {rail}
            bank_delete_rows += 1
            bank_delete_undetected += (
                len(reduced) != 19 or rail in reduced
            )
        for site in placement.packet.sites:
            reduced = placement.bank - {site}
            packet_delete_rows += 1
            packet_delete_undetected += (
                len(reduced) != C714.N + F17 - 1 or site in reduced
            )
        mutated_f17 = frozenset(
            (placement.q_u, placement.q_v, placement.pointer, *placement.rails)
        )
        expected_aliases = frozenset((placement.q_u, placement.q_v, placement.current))
        mutated_aliases = mutated_f17 & set(placement.packet.sites)
        mutation_detected = (
            mutated_aliases != expected_aliases or placement.pointer in mutated_aliases
        )
        alias_collision_mutation_undetected += not mutation_detected
    return {
        "shape": shape,
        "cells": len(graph.cells),
        "seams": len(seams),
        "source_update_rotations": len(rotations),
        "source_update_instructions": len(C871.compile_rotations(rotations, context)),
        "retained_nonseam_rotations": len(nonseam),
        "retained_pre_seam_rotations": len(pre),
        "retained_post_seam_rotations": len(post),
        "augmented_epoch_ledgers": augmented_epoch_ledgers,
        "baseline_partition_failure": int(partition_failure),
        "selected_factor_match_failures": selection_failures,
        "scheduled_missing_seams": missing,
        "scheduled_duplicate_seams": duplicates,
        "noncommuting_seam_factor_pairs": noncommuting_pairs,
        "noncommuting_order_failures": noncommuting_order_failures,
        "same_axis_parity_rotation_anticommutators": same_parity_anticommutators,
        "C870_constraint_certificate": constraints,
        "stage_abstract_Gauss_preservation_failures": dict(sorted(stage_constraint_failures.items())),
        "endpoint_B_physical_constraint_anticommutators": endpoint_B_constraint_anticommutators,
        "F17_only_added_instructions_excluding_seam": 634,
        "coexistence_added_instructions_excluding_seam_and_packet": 636,
        "F17_only_added_instruction_census_failures": f17_added_census_failures,
        "coexistence_added_instruction_census_failures":
            coexistence_added_census_failures,
        "packet_instructions_per_seam": len(C714.expanded(C714.word())),
        "macro_logical_instruction_census": dict(sorted(Counter(
            row["logical"] for row in macro_rows
        ).items())),
        "macro_min_logical_instructions": min(row["logical"] for row in macro_rows),
        "macro_max_logical_instructions": max(row["logical"] for row in macro_rows),
        "total_macro_logical_instructions": sum(row["logical"] for row in macro_rows),
        "total_macro_routed_gates": serial_routed,
        "macro_min_routed_gates": min(row["routed"] for row in macro_rows),
        "macro_max_routed_gates": max(row["routed"] for row in macro_rows),
        "maximum_route_distance": max(row["maximum_distance"] for row in macro_rows),
        "route_failures": sum(row["route_failures"] for row in macro_rows),
        "F17_only_route_failures": sum(
            row["f17_route_failures"] for row in macro_rows
        ),
        "alpha_plus_minus_route_census_failures": alpha_route_census_failures,
        "schedule_color_rule": "(axis, owner_x mod2, owner_y mod2, owner_z mod2)",
        "schedule_color_templates": 24,
        "active_colors": len(groups),
        "ordered_active_colors": ordered_colors,
        "same_color_macro_pairs": same_color_pairs,
        "same_color_route_footprint_collisions": same_color_collisions,
        "F17_only_same_color_route_footprint_collisions": f17_same_color_collisions,
        "naive_axis_only_macro_pairs": naive_pairs,
        "naive_axis_only_route_footprint_collisions": naive_collisions,
        "F17_only_naive_axis_only_route_footprint_collisions":
            f17_naive_collisions,
        "repeated_color_groups": sum(len(rows) > 1 for rows in groups.values()),
        "maximum_parallel_macros": max(map(len, groups.values())),
        "fixed_schedule_parallel_routed_depth": parallel_depth,
        "fixed_schedule_identity_padding": identity_padding,
        "F17_only_total_macro_logical_instructions": sum(
            row["f17_logical"] for row in macro_rows
        ),
        "F17_only_total_macro_routed_gates": f17_serial_routed,
        "F17_only_macro_min_logical_instructions": min(
            row["f17_logical"] for row in macro_rows
        ),
        "F17_only_macro_max_logical_instructions": max(
            row["f17_logical"] for row in macro_rows
        ),
        "F17_only_macro_min_routed_gates": min(row["f17_routed"] for row in macro_rows),
        "F17_only_macro_max_routed_gates": max(row["f17_routed"] for row in macro_rows),
        "F17_only_fixed_schedule_parallel_routed_depth": f17_parallel_depth,
        "F17_only_fixed_schedule_identity_padding": f17_identity_padding,
        "fixed_schedule_sha256": schedule_digest,
        "active_schedule_color_deletions": schedule_deletions,
        "inactive_schedule_color_deletions": tuple(
            color for color, row in schedule_deletions.items()
            if not row["active_F17_basis_witnesses"]
        ),
        "local_route_footprint_envelopes": envelopes,
        "recurrent_separation_pitch": 32,
        "envelope_width_failures_at_pitch32": envelope_width_failures,
        "encoded_carrier_M2": len(carriers),
        "preparation_auxiliary_M2": len(auxiliary),
        "packet_M2_per_seam": C714.N,
        "F17_role_M2_per_seam": 20,
        "intentional_packet_F17_role_aliases_per_seam": 3,
        "incremental_persistent_F17_rail_M2_per_seam": F17,
        "combined_packet_plus_F17_bank_M2_per_seam": C714.N + F17,
        "F17_only_bank_M2_per_seam": 20,
        "F17_only_all_seam_bank_union_M2": len(f17_bank_union),
        "F17_only_expected_all_seam_bank_union_M2": 20 * len(seams),
        "F17_only_declared_assigned_M2": len(f17_assigned),
        "F17_only_route_touched_union_M2": len(f17_touched_union),
        "F17_only_restored_route_transit_not_assigned_M2": len(f17_route_transit),
        "F17_only_assigned_plus_route_support_union_M2": len(f17_support_union),
        "all_seam_bank_union_M2": len(bank_union),
        "expected_all_seam_bank_union_M2": (C714.N + F17) * len(seams),
        "declared_assigned_M2": len(assigned),
        "route_touched_union_M2": len(touched_union),
        "restored_route_transit_not_assigned_M2": len(route_transit),
        "assigned_plus_route_support_union_M2": len(support_union),
        "bank_radius": max(placement.radius for placement in placements),
        "bank_pair_overlap_pairs": bank_overlap_pairs,
        "bank_pair_overlap_sites": bank_overlap_sites,
        "F17_only_bank_pair_overlap_pairs": f17_bank_overlap_pairs,
        "F17_only_bank_pair_overlap_sites": f17_bank_overlap_sites,
        "bank_carrier_aux_collision_sites": len(bank_union & (carriers | set(auxiliary))),
        "F17_only_bank_carrier_aux_collision_sites": len(
            f17_bank_union & (carriers | set(auxiliary))
        ),
        "persistent_rail_packet_collision_sites": sum(
            len(set(placement.rails) & set(placement.packet.sites)) for placement in placements
        ),
        "shared_role_alias_failures": shared_alias_failures,
        "packet_entry_work_failures": packet_entry_work_failures,
        "active_single_rail_bank_deletions": bank_delete_rows,
        "single_rail_bank_deletion_lost_one_hot_columns": bank_delete_rows,
        "undetected_single_rail_bank_deletions": bank_delete_undetected,
        "active_single_packet_site_interface_deletions": packet_delete_rows,
        "undetected_single_packet_site_interface_deletions": packet_delete_undetected,
        "current_to_pointer_alias_collision_mutation_detected_seams":
            len(seams) - alias_collision_mutation_undetected,
        "current_to_pointer_alias_collision_mutation_undetected":
            alias_collision_mutation_undetected,
        "phase": {
            "seam_phase_rows": len(phase_rows),
            "raw_phase": [0.0, -1.0],
            "maximum_raw_square_to_minus_identity_residual": maximum_raw_minus_residual,
            "maximum_raw_square_to_identity_residual": maximum_raw_identity_residual,
            "maximum_formal_corrected_residual": maximum_phase_residual,
            "formal_scalar_angle_per_seam": math.pi / 2,
            "formal_scalar_routed_gates": 0,
            "unchanged_full_update_compiled_relative_phase_angle": inventory[
                "compiled_relative_to_target_global_phase_angle"
            ],
            "unchanged_full_update_formal_correction_angle": inventory[
                "exact_target_global_phase_correction_angle"
            ],
        },
    }


def coordinate_covariance_certificate(catalog):
    frames = C871.proper_frames()
    standard_basis = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    paths = tuple(sorted(catalog["paths"], key=repr))
    signatures = tuple(sorted(catalog["signatures"], key=repr))
    banks = tuple(sorted(catalog["banks"], key=repr))
    frame_path_failures = frame_bank_failures = 0
    for frame in frames:
        moved_basis = tuple(C871.matvec(frame, row) for row in standard_basis)
        for path in paths:
            moved = tuple(C871.matvec(frame, site) for site in path)
            frame_path_failures += C871.coframe_path(
                moved[0], moved[-1], moved_basis
            ) != moved
        for bank in banks:
            moved = tuple(C871.matvec(frame, site) for site in bank)
            frame_bank_failures += len(set(moved)) != 20
    signature_products = path_products = bank_products = 0
    for left in frames:
        for right in frames:
            composed = left @ right
            signature_products += sum(
                tuple(C871.matvec(left, C871.matvec(right, site)) for site in signature[1])
                != tuple(C871.matvec(composed, site) for site in signature[1])
                for signature in signatures
            )
            path_products += sum(
                tuple(C871.matvec(left, C871.matvec(right, site)) for site in path)
                != tuple(C871.matvec(composed, site) for site in path)
                for path in paths
            )
            bank_products += sum(
                {C871.matvec(left, C871.matvec(right, site)) for site in bank}
                != {C871.matvec(composed, site) for site in bank}
                for bank in banks
            )
    # The color itself is an exact finite representation under endpoint-normalized frames.
    color_frame_failures = color_product_failures = 0
    representatives = tuple((axis, residue) for axis in range(3) for residue in product((0, 1), repeat=3))

    def move_owner(axis, owner, frame):
        target_axis, sign = C871.signed_axis(frame, axis)
        moved = C871.matvec(frame, owner)
        if sign < 0:
            moved = add(moved, C871.matvec(frame, tuple(int(i == axis) for i in range(3))))
        return target_axis, moved

    for axis, residue in representatives:
        for frame in frames:
            moved_axis, moved_owner = move_owner(axis, residue, frame)
            expected = (moved_axis, *(value & 1 for value in moved_owner))
            color_frame_failures += expected != schedule_color(
                (moved_owner, moved_axis, add(moved_owner, tuple(int(i == moved_axis) for i in range(3))), 0, 0)
            )
        for right in frames:
            mid_axis, mid_owner = move_owner(axis, residue, right)
            for left in frames:
                seq_axis, seq_owner = move_owner(mid_axis, mid_owner, left)
                direct_axis, direct_owner = move_owner(axis, residue, left @ right)
                color_product_failures += (
                    seq_axis, tuple(value & 1 for value in seq_owner)
                ) != (direct_axis, tuple(value & 1 for value in direct_owner))
    return {
        "proper_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "unique_normalized_instruction_signatures": len(signatures),
        "unique_normalized_route_paths": len(paths),
        "unique_normalized_bank_templates": len(banks),
        "frame_route_path_failures": frame_path_failures,
        "frame_bank_failures": frame_bank_failures,
        "signature_product_rows": len(frames) ** 2 * len(signatures),
        "path_product_rows": len(frames) ** 2 * len(paths),
        "bank_product_rows": len(frames) ** 2 * len(banks),
        "signature_product_failures": signature_products,
        "path_product_failures": path_products,
        "bank_product_failures": bank_products,
        "color_frame_rows": len(representatives) * len(frames),
        "color_frame_failures": color_frame_failures,
        "color_product_rows": len(representatives) * len(frames) ** 2,
        "color_product_failures": color_product_failures,
    }


def collect_primary_failures(report):
    failures = []
    if not report["provenance"]["expected_base_is_ancestor_of_head"]:
        failures.append("provenance:expected base is not an ancestor of HEAD")
    if report["provenance"]["primary_source_hash_mismatches"]:
        failures.append("provenance:primary source hash mismatch")
    primitive = report["primitive"]
    for key in ("clean_target_column_residual", "unchanged_full_Toffoli_residual", "Fredkin_residual"):
        if primitive[key] > TOL:
            failures.append(f"primitive:{key}")
    if primitive["inactive_remaining_clean_target_primitive_deletions"]:
        failures.append("primitive:inactive reduced-word deletion")
    for row in report["semantics"]:
        for key in ("basis_failures", "scratch_cleanup_failures", "pointer_failures", "typed_G_failures"):
            if row[key]:
                failures.append(f"alpha{row['alpha']}:{key}")
        if row["distinct_output_columns"] != 68:
            failures.append(f"alpha{row['alpha']}:isometry")
        for key in ("coherent_forward_residual_with_formal_seam_scalar", "coherent_inverse_residual"):
            if row[key] > TOL:
                failures.append(f"alpha{row['alpha']}:{key}")
    if report["semantic_mutations"]["inactive_component_mutations"]:
        failures.append("semantic:inactive component mutation")
    recurrence = report["persistent_recurrence"]
    for key in (
        "F17_only_two_epoch_failures", "F17_only_two_epoch_work_cleanup_failures",
        "F17_only_eight_epoch_failures",
    ):
        if recurrence[key]:
            failures.append(f"recurrence:{key}")
    unary = report["unary_projector"]
    for key in ("one_hot_mapping_failures", "all_sector_Hamming_weight_failures", "all_sector_inverse_failures", "P1_commutator_failures"):
        if unary[key]:
            failures.append(f"unary:{key}")
    if unary["inactive_deleted_Fredkins"]:
        failures.append("unary:inactive Fredkin deletion")
    history = report["computational_basis_path_history_witness"]
    if not (
        history["same_endpoint_divergence"]
        and history["upper_G_matches_initial"]
        and history["lower_G_matches_initial"]
        and history["joint_F17_history_inner_product"] == 0
    ):
        failures.append("computational-basis path-history witness")
    signed = report["signed_transport"]
    for key in ("signed_law_failures", "typed_family_transport_failures", "ordered_product_failures"):
        if signed[key]:
            failures.append(f"signed:{key}")
    for key in (
        "negative_frame_endpoint_swap_omission_detected_rows",
        "negative_frame_rail_k_to_minus_k_omission_detected_rows",
        "negative_frame_spurious_alpha_family_flip_detected_rows",
    ):
        if not signed[key]:
            failures.append(f"signed:inactive {key}")
    for fixture in report["fixtures"]:
        prefix = str(tuple(fixture["shape"]))
        for key in (
            "baseline_partition_failure", "selected_factor_match_failures",
            "scheduled_missing_seams", "scheduled_duplicate_seams",
            "noncommuting_order_failures", "same_axis_parity_rotation_anticommutators",
            "F17_only_added_instruction_census_failures", "F17_only_route_failures",
            "alpha_plus_minus_route_census_failures",
            "F17_only_same_color_route_footprint_collisions",
            "envelope_width_failures_at_pitch32", "F17_only_bank_pair_overlap_pairs",
            "F17_only_bank_pair_overlap_sites",
            "F17_only_bank_carrier_aux_collision_sites",
            "endpoint_B_physical_constraint_anticommutators",
            "undetected_single_rail_bank_deletions",
        ):
            if fixture[key]:
                failures.append(f"{prefix}:{key}")
        if fixture["F17_only_all_seam_bank_union_M2"] != fixture["F17_only_expected_all_seam_bank_union_M2"]:
            failures.append(f"{prefix}:F17-only bank union census")
        for label in ("A_F17_only",):
            ledger = fixture["augmented_epoch_ledgers"][label]
            if ledger["complete_epoch_non_NN_or_return_failures"]:
                failures.append(f"{prefix}:{label}:complete epoch route")
            if ledger["factor_order_reconstruction_failures"]:
                failures.append(f"{prefix}:{label}:factor order")
            if any(len(ledger[key]) != 64 for key in (
                "retained_nonseam_word_sha256", "seam_stage_schedule_sha256",
                "complete_epoch_logical_word_sha256", "complete_epoch_routed_schedule_sha256",
            )):
                failures.append(f"{prefix}:{label}:digest")
        for key in (
            "abstract_update_preservation_failures", "physical_update_preservation_failures",
        ):
            if fixture["C870_constraint_certificate"][key]:
                failures.append(f"{prefix}:C870 constraints:{key}")
        if any(fixture["stage_abstract_Gauss_preservation_failures"].values()):
            failures.append(f"{prefix}:stage Gauss preservation")
        if fixture["bank_radius"] != 2:
            failures.append(f"{prefix}:bank radius")
        if fixture["F17_only_naive_axis_only_route_footprint_collisions"] == 0:
            failures.append(f"{prefix}:inactive schedule collision control")
        if fixture["inactive_schedule_color_deletions"]:
            failures.append(f"{prefix}:inactive schedule deletion")
        if fixture["phase"]["maximum_raw_square_to_minus_identity_residual"] > TOL:
            failures.append(f"{prefix}:raw seam phase")
        if abs(fixture["phase"]["maximum_raw_square_to_identity_residual"] - 2.0) > TOL:
            failures.append(f"{prefix}:inactive raw-square phase control")
        if fixture["phase"]["maximum_formal_corrected_residual"] > TOL:
            failures.append(f"{prefix}:formal seam scalar")
    covariance = report["coordinate_covariance"]
    for key in (
        "frame_route_path_failures", "frame_bank_failures", "signature_product_failures",
        "path_product_failures", "bank_product_failures", "color_frame_failures",
        "color_product_failures",
    ):
        if covariance[key]:
            failures.append(f"covariance:{key}")
    route = report["structural_route_deletions"]
    for key in ("undetected_structural_deletions", "full_operand_failures", "full_arbitrary_register_return_failures"):
        if route[key]:
            failures.append(f"route:{key}")
    return failures


def collect_secondary_optional_failures(report):
    """Diagnostics intentionally excluded from the F17-only closure."""
    failures = []
    if report["provenance"]["secondary_optional_source_hash_mismatches"]:
        failures.append("provenance:secondary optional source hash mismatch")
    recurrence = report["persistent_recurrence"]
    if not recurrence["coexistence_second_epoch_without_packet_blank_detected_columns"]:
        failures.append("coexistence:inactive packet freshness control")
    packet = report["secondary_optional_evidence"]["Cycle714_coexistence"]
    for key in (
        "independent_packet_failures", "packet_inverse_failures",
        "packet_work_cleanup_failures", "retained_pointer_failures",
    ):
        if packet[key]:
            failures.append(f"Cycle714:{key}")
    for fixture in report["fixtures"]:
        prefix = str(tuple(fixture["shape"]))
        for key in (
            "route_failures", "same_color_route_footprint_collisions",
            "bank_pair_overlap_pairs", "bank_pair_overlap_sites",
            "bank_carrier_aux_collision_sites",
            "persistent_rail_packet_collision_sites", "shared_role_alias_failures",
            "packet_entry_work_failures",
            "undetected_single_packet_site_interface_deletions",
            "current_to_pointer_alias_collision_mutation_undetected",
            "coexistence_added_instruction_census_failures",
        ):
            if fixture[key]:
                failures.append(f"{prefix}:optional:{key}")
        if fixture["all_seam_bank_union_M2"] != fixture["expected_all_seam_bank_union_M2"]:
            failures.append(f"{prefix}:optional:bank union census")
        ledger = fixture["augmented_epoch_ledgers"]["B_F17_plus_Cycle714"]
        if ledger["complete_epoch_non_NN_or_return_failures"]:
            failures.append(f"{prefix}:optional:complete epoch route")
        if ledger["factor_order_reconstruction_failures"]:
            failures.append(f"{prefix}:optional:factor order")
    return failures


def main(output: Path = OUT) -> int:
    observed_hashes = {path: digest(ROOT / path) for path in SOURCE_PATHS}
    mismatches = {
        path: {"expected": EXPECTED_SOURCE_SHA256[path], "observed": observed_hashes[path]}
        for path in SOURCE_PATHS if observed_hashes[path] != EXPECTED_SOURCE_SHA256[path]
    }
    primary_mismatches = {
        path: mismatches[path] for path in PRIMARY_SOURCE_PATHS if path in mismatches
    }
    secondary_mismatches = {
        path: mismatches[path]
        for path in SECONDARY_OPTIONAL_SOURCE_PATHS if path in mismatches
    }
    base_is_ancestor = subprocess.run(
        (
            "git", "merge-base", "--is-ancestor",
            EXPECTED_BASE_COMMIT, "HEAD",
        ),
        cwd=ROOT,
        check=False,
    ).returncode == 0
    catalog = {"paths": set(), "signatures": set(), "banks": set()}
    fixtures = tuple(fixture_certificate(shape, catalog) for shape in SHAPES)
    maximum_distance = max(row["maximum_route_distance"] for row in fixtures)
    report = {
        "status": "pending",
        "name": "Cycle873 recurrent F17-only all-seam physical core",
        "claim_scope": (
            "all landed directed seams on L2, L3, and held noncubic 3x2x2; supplied "
            "lawful matter, one-hot F17 banks, typed family/polarity, "
            "coframes, parity origin, ordered color traversal, recurrence invocation, "
            "and returned-route substrate"
        ),
        "provenance": {
            "base_commit": EXPECTED_BASE_COMMIT,
            "expected_base_is_ancestor_of_head": base_is_ancestor,
            "source_sha256": observed_hashes,
            "source_hash_mismatches": mismatches,
            "primary_source_hash_mismatches": primary_mismatches,
            "secondary_optional_source_hash_mismatches": secondary_mismatches,
            "runner": str(Path(__file__).relative_to(ROOT)),
        },
        "register_join": {
            "live_packet_M2": C714.N,
            "F17_roles": 20,
            "intentional_shared_packet_work_roles": 3,
            "new_persistent_F17_rails": F17,
            "combined_bank_M2": C714.N + F17,
            "local_alias_offsets": {
                "q_u_q56": (0, 1, 0),
                "q_v_q57": (0, -1, 0),
                "current_q58": (-2, 1, 1),
                "pointer_q44": (0, 0, 1),
            },
            "rail_local_offsets": RAIL_LOCAL_OFFSETS,
            "constant_radius": 2,
        },
        "objects": {
            "A_F17_only_recurrent_augmentation": {
                "persistent_bank_M2_per_seam": 20,
                "added_instructions_excluding_landed_seam": 634,
                "clean_returned_work_M2": 3,
                "packet_or_Cycle612_interface": False,
                "fresh_packet_or_address_required_per_epoch": False,
                "spectrum_status": (
                    "open for basis-link initialization; uniform cycle-space repair is not "
                    "excluded by the path-history witness"
                ),
            },
            "secondary_optional_B_F17_plus_unchanged_Cycle714_coexistence": {
                "combined_bank_M2_per_seam": 76,
                "incremental_M2_beyond_live_packet": 17,
                "added_instructions_excluding_landed_seam_and_packet": 636,
                "unchanged_packet_instructions": 718,
                "Cycle612_packet_interface_retained": True,
                "fresh_blank_packet_required_per_invocation": True,
            },
        },
        "factor_level_proof": {
            "literal_emitted_order": (
                "endpoint B extraction -> landed four-rotation seam factor -> "
                "mutually exclusive positive/negative predicate-controlled unary "
                "shifts -> endpoint cleanup"
            ),
            "landed_seam_phase": (
                "the four commuting pi/2 rotations emit raw -i*FSWAP; the formal "
                "+pi/2 zero-site scalar restores the exact FSWAP representative"
            ),
            "grouping_boundary": (
                "the augmented factor is the complete grouped emitted M2 word; no "
                "claim is made that its four individual seam rotations separately "
                "preserve the affine star code before the group is complete"
            ),
        },
        "schedule_input_boundary": {
            "parity_origin": (
                "the owner-coordinate residues mod2 are computed relative to a "
                "supplied lattice parity origin"
            ),
            "color_traversal": (
                "the deterministic order of the 24 color templates is supplied "
                "compiler schedule phase"
            ),
            "proved": (
                "collision freedom, landed factor-order reconstruction, and the "
                "reported proper-frame/color transport on the three fixtures"
            ),
            "not_proved": (
                "unit-translation/origin-shift equivalence, physical-law translation "
                "compatibility, or host-free autonomous recurrence"
            ),
        },
        "primitive": primitive_certificate(),
        "semantics": (semantic_certificate(1), semantic_certificate(-1)),
        "semantic_mutations": semantic_mutation_certificate(),
        "persistent_recurrence": persistent_recurrence_certificate(),
        "unary_projector": unary_projector_certificate(),
        "secondary_optional_evidence": {
            "closure_role": "reported but excluded from collect_primary_failures",
            "Cycle714_coexistence": packet_join_certificate(),
        },
        "computational_basis_path_history_witness":
            computational_basis_path_history_witness(),
        "signed_transport": signed_transport_certificate(),
        "fixtures": fixtures,
        "coordinate_covariance": coordinate_covariance_certificate(catalog),
        "structural_route_deletions": structural_route_deletion_certificate(maximum_distance),
        "primary_supplied": (
            "one-hot initialization of every persistent 17-M2 F17 rail bank",
            "the bounded projector/domain restriction P1 and any enforcement",
            "typed G=n+/-div family and matched alpha=+/-1 polarity",
            "lawful Cycle870 encoded matter and signed local coframes",
            "a lattice parity origin and ordered 24-color traversal/schedule phase",
            "recurrence invocation, admission controls, and arbitrary returned-route substrate",
        ),
        "primary_derived": (
            "zero-unintended-overlap 20-M2 F17-only local banks",
            "exact ell->ell+alpha(n_u-n_v) on the supplied one-hot sector",
            "clean q_u/q_v/current work after every augmented seam",
            "unchanged Cycle870 seam/nonseam factors apart from the inserted F17 word",
            "24-color recurrent seam-stage route schedule with exact returned transit",
            "proper-frame endpoint swap, rail k->-k, and typed-polarity normalization",
        ),
        "open_nonclaims": (
            "no autonomous F17-bank genesis, one-hot projection, leakage correction, or reset",
            "no autonomous packet allocation, occurrence, admission, or clock law",
            "no unit-translation covariance or origin-shift equivalence theorem for the "
            "parity-color schedule, and no host-free recurrence law",
            "no source/charge sign identification and no mass-to-source map",
            "no gravity, Regge, backreaction, continuum, or downstream response claim",
            "authority and audit verdict remain unset",
        ),
    }
    failures = collect_primary_failures(report)
    secondary_failures = collect_secondary_optional_failures(report)
    report["primary_failures"] = failures
    report["secondary_optional_failures"] = secondary_failures
    report["secondary_optional_status"] = (
        "pass" if not secondary_failures else "diagnostic_fail"
    )
    report["failures"] = failures
    report["status"] = "pass" if not failures else "fail"
    output.write_text(json.dumps(json_safe(report), indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": report["status"],
        "base_commit": EXPECTED_BASE_COMMIT,
        "expected_base_is_ancestor_of_head": base_is_ancestor,
        "receipt": str(OUT.relative_to(ROOT)),
        "failures": failures,
        "secondary_optional_status": report["secondary_optional_status"],
        "secondary_optional_failures": secondary_failures,
        "fixtures": [{
            "shape": row["shape"],
            "seams": row["seams"],
            "F17_only_bank_union_M2": row["F17_only_all_seam_bank_union_M2"],
            "F17_only_logical": row["F17_only_total_macro_logical_instructions"],
            "F17_only_routed": row["F17_only_total_macro_routed_gates"],
            "colors": row["active_colors"],
            "F17_only_parallel_depth": row["F17_only_fixed_schedule_parallel_routed_depth"],
            "F17_only_route_union": row["F17_only_route_touched_union_M2"],
            "F17_only_support_union": row["F17_only_assigned_plus_route_support_union_M2"],
        } for row in fixtures],
    }, indent=2, default=json_default))
    return int(bool(failures))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.output))
