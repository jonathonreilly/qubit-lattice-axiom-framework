#!/usr/bin/env python3
"""Cycle871 selected-seam OpenReference endpoint-to-packet bridge.

This probe splices a coherent endpoint-opportunity instrument around one
selected Cycle870 physical seam factor, retains its pointer through the rest
of the unchanged recurrent update, and drives the landed Cycle714 59-M2
fixed-cell packet word.  The packet is then checked against the unchanged
Cycle704/Cycle610/Cycle612 software acceptance interfaces.

The selected seam, its signed local coframe, blank packet cell, head/rotor,
and admission controls are declared input coordinates.  Output types are a
coherent opportunity pointer, circuit-bookkeeping ordinals, and a reversible
packet.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle870_openreference_native_recurrent_update_2026_08_02 as C870
import frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02 as J870
import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as C714
import frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25 as C704


NOTE_PATH = (
    "docs/OPENREFERENCE_MATTER_ENDPOINT_CAUSAL_INTERVAL_PACKET_"
    "CYCLE871_BOUNDED_THEOREM_NOTE_2026-08-02.md"
)
RECEIPT_PATH = ROOT / "outputs" / (
    "cycle871_openreference_endpoint_packet_bridge_receipt_2026_08_02.json"
)
AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    NOTE_PATH,
    "scripts/frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02.py",
    "scripts/frontier_cycle871_selected_openreference_seam_cycle714_packet_bridge_check_2026_08_02.py",
    "outputs/cycle871_selected_openreference_seam_cycle714_packet_bridge_check_receipt_2026_08_02.json",
    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py",
    "scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py",
    "scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
EXPECTED_INPUT_SHA256 = {
    "scripts/frontier_cycle871_selected_openreference_seam_cycle714_packet_bridge_check_2026_08_02.py":
        "3d09072e53052724ff503a37a7df41b20de56f3aa62948850081531a5c9a4608",
    "outputs/cycle871_selected_openreference_seam_cycle714_packet_bridge_check_receipt_2026_08_02.json":
        "e8ceb57382957f08b523e96e617153ea9fd6807cc756bc6f5568ccdf67d52cdf",
    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py":
        "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237",
    "scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py":
        "1b66c061dcb8e0082fd9e7264e78ccbd0f77440c0f517aa93696bde49f78c1bd",
    "scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py":
        "64b36432670f8a05179d0473e724afee1dfe6327cdd0233d3d788a6b8413c8a2",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py":
        "eb6c9a50681c69ea4fae47724c58d8ba10b48a270e7efa67a811af234afe9a1a",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py":
        "4d0049dbcb231301e0b0b110bc1933dfb2bda1aea2628e5e30bc5c1cee97d66a",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py":
        "b61f98d0b44c1496883e8ab2ae1db065772ed053c77b6661a0153086acfd0e2f",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py":
        "36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py":
        "6365d5aed1e70fb9b427ee6fb987879027cc30c818856a992b3fbf9d057e0c1b",
}

Coord = tuple[int, int, int]
Instruction = C870.c707.Instruction
TOL = 3.0e-10
PRIMARY_SHAPE = (2, 2, 2)
HELD_SHAPE = (3, 3, 3)


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] + right[index] for index in range(3))


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] - right[index] for index in range(3))


def scale(value: int, row: Coord) -> Coord:
    return tuple(value * item for item in row)


def unit(axis: int) -> Coord:
    return tuple(int(index == axis) for index in range(3))


def matvec(frame: np.ndarray, row: Coord) -> Coord:
    return (
        int(frame[0, 0]) * row[0]
        + int(frame[0, 1]) * row[1]
        + int(frame[0, 2]) * row[2],
        int(frame[1, 0]) * row[0]
        + int(frame[1, 1]) * row[1]
        + int(frame[1, 2]) * row[2],
        int(frame[2, 0]) * row[0]
        + int(frame[2, 1]) * row[1]
        + int(frame[2, 2]) * row[2],
    )


def proper_frames() -> tuple[np.ndarray, ...]:
    return tuple(np.asarray(frame, dtype=int) for frame in C870.base.proper_cubic_frames())


def shape_cells(shape: tuple[int, int, int]) -> tuple[Coord, ...]:
    return tuple(product(*(range(length) for length in shape)))


def local_coframe(axis: int) -> tuple[Coord, Coord, Coord]:
    return unit(axis), unit((axis + 1) % 3), unit((axis + 2) % 3)


def seam_midpoint(cell: Coord, axis: int) -> Coord:
    return add(scale(16, cell), scale(8, unit(axis)))


def signed_axis(frame: np.ndarray, axis: int) -> tuple[int, int]:
    moved = matvec(frame, unit(axis))
    target_axis = next(index for index, value in enumerate(moved) if value)
    return target_axis, moved[target_axis]


def normalized_mode(axis: int, mode: int) -> int:
    return 2 * (((mode // 2) - axis) % 3) + (mode % 2)


def normalize_raw_mask(raw: int, target_axis: int, sign: int) -> int:
    left = tuple(index for index in range(6) if (raw >> index) & 1)
    right = tuple(index for index in range(6) if (raw >> (6 + index)) & 1)
    if sign < 0:
        left, right = right, left
    output = 0
    for mode in left:
        output |= 1 << normalized_mode(target_axis, mode)
    for mode in right:
        output |= 1 << (6 + normalized_mode(target_axis, mode))
    return output


def transported_raw_mask(axis: int, frame: np.ndarray) -> tuple[int, int, int]:
    target_axis, sign = signed_axis(frame, axis)
    if sign > 0:
        source_mode, target_mode = 2 * target_axis + 1, 2 * target_axis
    else:
        source_mode, target_mode = 2 * target_axis, 2 * target_axis + 1
    raw = (1 << source_mode) | (1 << (6 + target_mode))
    return raw, target_axis, sign


def provenance_certificate() -> dict[str, object]:
    pins = {}
    for label, expected in EXPECTED_INPUT_SHA256.items():
        observed = file_sha256(ROOT / label)
        if observed != expected:
            pins[label] = {"expected": expected, "observed": observed}
    missing = tuple(label for label in AUDIT_INPUT_PATHS if not (ROOT / label).is_file())
    own_runner = "scripts/frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02.py"
    pin_required = tuple(
        label for label in AUDIT_INPUT_PATHS
        if label.startswith("scripts/") and label != own_runner
    )
    unpinned = tuple(
        label for label in pin_required if label not in EXPECTED_INPUT_SHA256
    )
    return {
        "pinned_input_failures": pins,
        "pin_required_inputs": pin_required,
        "unpinned_declared_inputs": unpinned,
        "missing_declared_inputs": missing,
        "duplicate_declared_inputs": len(AUDIT_INPUT_PATHS) - len(set(AUDIT_INPUT_PATHS)),
        "input_sha256": {
            label: file_sha256(ROOT / label)
            for label in AUDIT_INPUT_PATHS
            if (ROOT / label).is_file()
        },
    }


@dataclass(frozen=True)
class PacketPlacement:
    sites: tuple[Coord, ...]
    midpoint: Coord
    basis: tuple[Coord, Coord, Coord]
    occupied: frozenset[Coord]
    radius: int


def packet_placement(graph, context, seam) -> PacketPlacement:
    cell, axis, _target, _left_mode, _right_mode = seam
    midpoint = seam_midpoint(cell, axis)
    basis = local_coframe(axis)
    blocked = set(context.sites) | J870.auxiliary_registers(graph)
    fixed = {
        C714.POINTER: add(midpoint, basis[2]),
        C714.MCX_WORK[0]: add(midpoint, basis[1]),
        C714.MCX_WORK[1]: sub(midpoint, basis[1]),
    }
    if len(set(fixed.values())) != len(fixed) or set(fixed.values()) & blocked:
        raise AssertionError(("fixed packet-site collision", fixed, set(fixed.values()) & blocked))
    candidates = []
    for local in product(range(-2, 3), repeat=3):
        site = midpoint
        for coefficient, direction in zip(local, basis):
            site = add(site, scale(coefficient, direction))
        if site in blocked or site in fixed.values():
            continue
        candidates.append((max(map(abs, local)), sum(map(abs, local)), local, site))
    candidates.sort()
    iterator = iter(row[-1] for row in candidates)
    allocated = []
    for wire in range(C714.N):
        allocated.append(fixed[wire] if wire in fixed else next(iterator))
    sites = tuple(allocated)
    if len(set(sites)) != C714.N:
        raise AssertionError("packet allocator reused a site")
    radius = max(
        max(abs(sum((site[i] - midpoint[i]) * basis[j][i] for i in range(3))) for j in range(3))
        for site in sites
    )
    return PacketPlacement(sites, midpoint, basis, frozenset(blocked), radius)


def cnot(control: Coord, target: Coord, kind: str) -> Instruction:
    return Instruction(kind, (control, target), C714.CNOT)


def one(site: Coord, matrix: np.ndarray, kind: str) -> Instruction:
    return Instruction(kind, (site,), matrix)


def toffoli_word(a: Coord, b: Coord, target: Coord, prefix: str) -> tuple[Instruction, ...]:
    local = (a, b, target)
    matrices = {"H": C714.H, "T": C714.T, "TD": C714.TD, "CNOT": C714.CNOT}
    return tuple(
        Instruction(prefix + kind, tuple(local[index] for index in wires), matrices[kind])
        for kind, wires in C714.toffoli_primitives(0, 1, 2)
    )


def packet_word(placement: PacketPlacement) -> tuple[Instruction, ...]:
    matrices = {"H": C714.H, "T": C714.T, "TD": C714.TD, "CNOT": C714.CNOT}
    return tuple(
        Instruction(
            "packet_" + kind,
            tuple(placement.sites[wire] for wire in wires),
            matrices[kind],
        )
        for kind, wires in C714.expanded(C714.word())
    )


def physical_b(graph, context, cell: Coord, mode: int):
    logical = graph.B(graph.vertex_index[(cell, mode)])
    physical = C870.physical_lift(logical, context)
    if physical.x or physical.phase % 4:
        raise AssertionError(("physical B is not a positive Z word", physical))
    return physical


def z_support(row, context) -> tuple[Coord, ...]:
    return tuple(
        site for index, site in enumerate(context.sites) if (row.z >> index) & 1
    )


def extract_b(row, context, target: Coord, kind: str) -> tuple[Instruction, ...]:
    return tuple(cnot(site, target, kind) for site in z_support(row, context))


def selected_seam_rotations(graph, seam):
    cell, axis, target, left_mode, right_mode = seam
    builder = C870.RotationBuilder(graph)
    C870.add_seam_fswap(
        builder, ("cycle871_selected_seam", cell, axis, target),
        cell, left_mode, target, right_mode,
    )
    return tuple(builder.rows)


def compile_rotations(rotations, context) -> tuple[Instruction, ...]:
    return tuple(
        instruction
        for rotation in rotations
        for instruction in C870.c707.compile_pauli_rotation(
            C870.physical_lift(rotation.row, context), context.sites, rotation.angle
        )
    )


@dataclass(frozen=True)
class EmittedProgram:
    update_prefix: tuple[Instruction, ...]
    endpoint_pre: tuple[Instruction, ...]
    selected_seam: tuple[Instruction, ...]
    endpoint_post: tuple[Instruction, ...]
    endpoint_or: tuple[Instruction, ...]
    endpoint_clean: tuple[Instruction, ...]
    update_suffix: tuple[Instruction, ...]
    packet: tuple[Instruction, ...]

    @property
    def endpoint(self) -> tuple[Instruction, ...]:
        return (
            self.endpoint_pre + self.selected_seam + self.endpoint_post
            + self.endpoint_or + self.endpoint_clean
        )

    @property
    def selected_packet(self) -> tuple[Instruction, ...]:
        return self.endpoint + self.packet

    @property
    def full(self) -> tuple[Instruction, ...]:
        return self.update_prefix + self.endpoint + self.update_suffix + self.packet


def emit_program(graph, context, seam, placement) -> EmittedProgram:
    cell, _axis, target, left_mode, right_mode = seam
    left_b = physical_b(graph, context, cell, left_mode)
    right_b = physical_b(graph, context, target, right_mode)
    du = placement.sites[C714.MCX_WORK[0]]
    dv = placement.sites[C714.MCX_WORK[1]]
    pointer = placement.sites[C714.POINTER]
    endpoint_pre = extract_b(left_b, context, du, "endpoint_pre_left_B") + extract_b(
        right_b, context, dv, "endpoint_pre_right_B"
    )
    rotations, _inventory = C870.build_update(graph, coin_schedule())
    requested_seam_index = C870.graph_seams(graph).index(seam)
    requested_factor = (
        "seam", requested_seam_index, cell, seam[1], target
    )
    selected = tuple(
        rotation for rotation in rotations
        if rotation.kind == "directed_seam_fswap"
        and rotation.factor == requested_factor
    )
    expected_meta = (
        ("B", cell, left_mode),
        ("B", target, right_mode),
        ("seam_h1", cell, left_mode, target, right_mode),
        ("seam_h2", cell, left_mode, target, right_mode),
    )
    requested_selection_failures = (
        abs(len(selected) - 4)
        + sum(
            left.meta != right
            for left, right in zip(selected, expected_meta)
        )
    )
    if not selected:
        raise AssertionError(("requested seam factor absent", requested_factor))
    selected_serials = tuple(rotation.serial for rotation in selected)
    contiguous_selection_failure = int(
        selected_serials
        != tuple(range(selected_serials[0], selected_serials[0] + len(selected_serials)))
    )
    before = tuple(
        rotation for rotation in rotations
        if rotation.serial < selected_serials[0]
    )
    after = tuple(
        rotation for rotation in rotations
        if rotation.serial > selected_serials[-1]
    )
    partition_reconstruction_failure = int(
        before + selected + after != rotations
    )
    if any((
        requested_selection_failures,
        contiguous_selection_failure,
        partition_reconstruction_failure,
    )):
        raise AssertionError((
            "candidate selected-seam partition failed",
            requested_factor,
            requested_selection_failures,
            contiguous_selection_failure,
            partition_reconstruction_failure,
        ))
    selected_seam = compile_rotations(selected, context)
    endpoint_post = extract_b(left_b, context, du, "endpoint_post_left_B") + extract_b(
        right_b, context, dv, "endpoint_post_right_B"
    )
    endpoint_or = (
        cnot(du, pointer, "endpoint_OR_CNOT"),
        cnot(dv, pointer, "endpoint_OR_CNOT"),
    ) + toffoli_word(du, dv, pointer, "endpoint_OR_Toffoli_")
    endpoint_clean = (
        extract_b(left_b, context, du, "endpoint_clean_left_B")
        + extract_b(right_b, context, du, "endpoint_clean_right_B")
        + extract_b(left_b, context, dv, "endpoint_clean_left_B")
        + extract_b(right_b, context, dv, "endpoint_clean_right_B")
    )
    return EmittedProgram(
        update_prefix=compile_rotations(before, context),
        endpoint_pre=endpoint_pre,
        selected_seam=selected_seam,
        endpoint_post=endpoint_post,
        endpoint_or=endpoint_or,
        endpoint_clean=endpoint_clean,
        update_suffix=compile_rotations(after, context),
        packet=packet_word(placement),
    )


def coin_schedule():
    species = C870.c219.common_species(float(C870.c230.BETA))
    return C870.qr_coin_schedule(np.asarray(species.coin, dtype=complex))[0]


def instruction_signature(instruction: Instruction):
    return (
        instruction.kind,
        instruction.sites,
        C870.c707.c655.matrix_digest(instruction.matrix),
    )


def word_sha256(word: tuple[Instruction, ...]) -> str:
    return sha256(repr(tuple(map(instruction_signature, word))).encode()).hexdigest()


def transform_signature(signature, frame: np.ndarray):
    kind, sites, matrix_digest = signature
    return kind, tuple(matvec(frame, site) for site in sites), matrix_digest


def transform_path(path: tuple[Coord, ...], frame: np.ndarray):
    return tuple(matvec(frame, site) for site in path)


def binding_certificate(
    graph,
    context,
    seam,
    placement,
    program: EmittedProgram,
    *,
    declared_endpoint=None,
    declared_selected_packet=None,
    declared_full=None,
):
    cell, _axis, target, left_mode, right_mode = seam
    left_b = C870.physical_lift(
        graph.B(graph.vertex_index[(cell, left_mode)]), context
    )
    right_b = C870.physical_lift(
        graph.B(graph.vertex_index[(target, right_mode)]), context
    )
    if any((left_b.x, left_b.phase % 4, right_b.x, right_b.phase % 4)):
        raise AssertionError("independent expected B lift is not positive Z")
    left_support = tuple(
        site for index, site in enumerate(context.sites)
        if (left_b.z >> index) & 1
    )
    right_support = tuple(
        site for index, site in enumerate(context.sites)
        if (right_b.z >> index) & 1
    )
    du = placement.sites[C714.MCX_WORK[0]]
    dv = placement.sites[C714.MCX_WORK[1]]
    pointer = placement.sites[C714.POINTER]
    expected_species = C870.c219.common_species(float(C870.c230.BETA))
    expected_coin_schedule = C870.qr_coin_schedule(
        np.asarray(expected_species.coin, dtype=complex)
    )[0]
    rotations, _inventory = C870.build_update(graph, expected_coin_schedule)
    requested_seam_index = C870.graph_seams(graph).index(seam)
    requested_factor = (
        "seam", requested_seam_index, cell, seam[1], target
    )
    selected = tuple(
        rotation for rotation in rotations
        if rotation.kind == "directed_seam_fswap"
        and rotation.factor == requested_factor
    )
    expected_meta = (
        ("B", cell, left_mode),
        ("B", target, right_mode),
        ("seam_h1", cell, left_mode, target, right_mode),
        ("seam_h2", cell, left_mode, target, right_mode),
    )
    requested_selection_failures = (
        abs(len(selected) - 4)
        + sum(
            left.meta != right
            for left, right in zip(selected, expected_meta)
        )
    )
    if not selected:
        raise AssertionError(("requested seam factor absent", requested_factor))
    selected_serials = tuple(rotation.serial for rotation in selected)
    contiguous_selection_failure = int(
        selected_serials
        != tuple(range(selected_serials[0], selected_serials[0] + len(selected_serials)))
    )
    before = tuple(
        rotation for rotation in rotations
        if rotation.serial < selected_serials[0]
    )
    after = tuple(
        rotation for rotation in rotations
        if rotation.serial > selected_serials[-1]
    )
    partition_reconstruction_failure = int(
        before + selected + after != rotations
    )
    expected_coin_signature = tuple(
        (
            gate.kind,
            gate.modes,
            C870.c707.c655.matrix_digest(np.asarray(gate.matrix, dtype=complex)),
        )
        for gate in expected_coin_schedule
    )
    candidate_coin = coin_schedule()
    candidate_coin_signature = tuple(
        (
            gate.kind,
            gate.modes,
            C870.c707.c655.matrix_digest(np.asarray(gate.matrix, dtype=complex)),
        )
        for gate in candidate_coin
    )
    coin_schedule_mismatch = int(
        candidate_coin_signature != expected_coin_signature
    )
    def independent_compile(rows):
        return tuple(
            instruction
            for rotation in rows
            for instruction in C870.c707.compile_pauli_rotation(
                C870.physical_lift(rotation.row, context),
                context.sites,
                rotation.angle,
            )
        )

    def independent_cnot(kind, control, destination):
        return Instruction(kind, (control, destination), C714.CNOT)

    primitive_matrices = {
        "H": C714.H,
        "T": C714.T,
        "TD": C714.TD,
        "CNOT": C714.CNOT,
    }
    expected_or_toffoli = tuple(
        Instruction(
            "endpoint_OR_Toffoli_" + kind,
            tuple((du, dv, pointer)[wire] for wire in wires),
            primitive_matrices[kind],
        )
        for kind, wires in C714.toffoli_primitives(0, 1, 2)
    )
    expected_packet = tuple(
        Instruction(
            "packet_" + kind,
            tuple(placement.sites[wire] for wire in wires),
            primitive_matrices[kind],
        )
        for kind, wires in C714.expanded(C714.word())
    )
    expected = EmittedProgram(
        update_prefix=independent_compile(before),
        endpoint_pre=(
            tuple(independent_cnot("endpoint_pre_left_B", site, du) for site in left_support)
            + tuple(independent_cnot("endpoint_pre_right_B", site, dv) for site in right_support)
        ),
        selected_seam=independent_compile(selected),
        endpoint_post=(
            tuple(independent_cnot("endpoint_post_left_B", site, du) for site in left_support)
            + tuple(independent_cnot("endpoint_post_right_B", site, dv) for site in right_support)
        ),
        endpoint_or=(
            independent_cnot("endpoint_OR_CNOT", du, pointer),
            independent_cnot("endpoint_OR_CNOT", dv, pointer),
        ) + expected_or_toffoli,
        endpoint_clean=(
            tuple(independent_cnot("endpoint_clean_left_B", site, du) for site in left_support)
            + tuple(independent_cnot("endpoint_clean_right_B", site, du) for site in right_support)
            + tuple(independent_cnot("endpoint_clean_left_B", site, dv) for site in left_support)
            + tuple(independent_cnot("endpoint_clean_right_B", site, dv) for site in right_support)
        ),
        update_suffix=independent_compile(after),
        packet=expected_packet,
    )
    labels = tuple(EmittedProgram.__dataclass_fields__)
    mismatches = {}
    for label in labels:
        observed_word = getattr(program, label)
        expected_word = getattr(expected, label)
        if tuple(map(instruction_signature, observed_word)) != tuple(
            map(instruction_signature, expected_word)
        ):
            mismatches[label] = {
                "observed_instructions": len(observed_word),
                "expected_instructions": len(expected_word),
                "observed_sha256": word_sha256(observed_word),
                "expected_sha256": word_sha256(expected_word),
            }
    baseline = independent_compile(before + selected + after)
    restored_baseline = (
        program.update_prefix + program.selected_seam + program.update_suffix
    )
    baseline_mismatch = tuple(map(instruction_signature, restored_baseline)) != tuple(
        map(instruction_signature, baseline)
    )
    observed_endpoint = program.endpoint if declared_endpoint is None else declared_endpoint
    observed_selected_packet = (
        program.selected_packet
        if declared_selected_packet is None
        else declared_selected_packet
    )
    observed_full = program.full if declared_full is None else declared_full
    explicit_program_endpoint = (
        program.endpoint_pre + program.selected_seam + program.endpoint_post
        + program.endpoint_or + program.endpoint_clean
    )
    explicit_program_selected_packet = explicit_program_endpoint + program.packet
    explicit_program_full = (
        program.update_prefix + explicit_program_endpoint
        + program.update_suffix + program.packet
    )
    explicit_expected_endpoint = (
        expected.endpoint_pre + expected.selected_seam + expected.endpoint_post
        + expected.endpoint_or + expected.endpoint_clean
    )
    explicit_expected_selected_packet = explicit_expected_endpoint + expected.packet
    explicit_expected_full = (
        expected.update_prefix + explicit_expected_endpoint
        + expected.update_suffix + expected.packet
    )

    def differs(left, right):
        return int(
            tuple(map(instruction_signature, left))
            != tuple(map(instruction_signature, right))
        )

    composition_mismatches = {
        "endpoint_vs_stored_segments": differs(
            observed_endpoint, explicit_program_endpoint
        ),
        "endpoint_vs_independent_expected": differs(
            observed_endpoint, explicit_expected_endpoint
        ),
        "selected_packet_vs_stored_segments": differs(
            observed_selected_packet, explicit_program_selected_packet
        ),
        "selected_packet_vs_independent_expected": differs(
            observed_selected_packet, explicit_expected_selected_packet
        ),
        "full_vs_stored_segments": differs(observed_full, explicit_program_full),
        "full_vs_independent_expected": differs(observed_full, explicit_expected_full),
    }
    return {
        "requested_factor": repr(requested_factor),
        "requested_selected_serials": selected_serials,
        "requested_selection_failures": requested_selection_failures,
        "contiguous_selection_failure": contiguous_selection_failure,
        "partition_reconstruction_failure": partition_reconstruction_failure,
        "expected_coin_schedule_gates": len(expected_coin_schedule),
        "candidate_coin_schedule_gates": len(candidate_coin),
        "expected_coin_schedule_sha256": sha256(
            repr(expected_coin_signature).encode()
        ).hexdigest(),
        "candidate_coin_schedule_sha256": sha256(
            repr(candidate_coin_signature).encode()
        ).hexdigest(),
        "coin_schedule_mismatch": coin_schedule_mismatch,
        "segment_signature_mismatches": mismatches,
        "baseline_update_reconstruction_failure": int(baseline_mismatch),
        "composite_surface_mismatches": composition_mismatches,
        "emitted_endpoint_sha256": word_sha256(observed_endpoint),
        "emitted_selected_packet_sha256": word_sha256(observed_selected_packet),
        "emitted_full_word_sha256": word_sha256(observed_full),
        "emitted_full_instructions": len(observed_full),
        "failure_count": (
            len(mismatches) + int(baseline_mismatch)
            + requested_selection_failures + contiguous_selection_failure
            + partition_reconstruction_failure + coin_schedule_mismatch
            + sum(composition_mismatches.values())
        ),
        "segment_instruction_counts": {
            label: len(getattr(program, label)) for label in labels
        },
    }


def phase_representative_certificate(graph, context, program: EmittedProgram):
    """Carry Cycle870's nontrivial projective phase into the augmented word.

    The endpoint comparator and packet consist of exact CNOT/Clifford+T
    primitives and add no declared scalar.  The native update segment is the
    byte-level compiled Cycle870 rotation word, so its landed phase ledger is
    the unique scalar needed for literal vector equality.
    """

    expected_species = C870.c219.common_species(float(C870.c230.BETA))
    expected_coin_schedule = C870.qr_coin_schedule(
        np.asarray(expected_species.coin, dtype=complex)
    )[0]
    rotations, inventory = C870.build_update(graph, expected_coin_schedule)
    expected_update = tuple(
        instruction
        for rotation in rotations
        for instruction in C870.c707.compile_pauli_rotation(
            C870.physical_lift(rotation.row, context),
            context.sites,
            rotation.angle,
        )
    )
    emitted_update = (
        program.update_prefix + program.selected_seam + program.update_suffix
    )
    update_signature_failures = int(
        tuple(map(instruction_signature, emitted_update))
        != tuple(map(instruction_signature, expected_update))
    )
    relative = inventory["compiled_relative_to_target_global_phase_angle"]
    correction = inventory["exact_target_global_phase_correction_angle"]
    phase_sum_residual = abs(
        math.atan2(math.sin(relative + correction), math.cos(relative + correction))
    )
    return {
        "projective_equation": (
            "U871_routed E871 = exp(i*phi870) E871 G871_logical"
        ),
        "exact_vector_representative": (
            "G871_physical_exact := exp(-i*phi870) U871_routed"
        ),
        "compiled_relative_phase_angle": relative,
        "formal_correction_angle": correction,
        "formal_scalar": [math.cos(correction), math.sin(correction)],
        "phase_breakdown": inventory["compiled_relative_phase_breakdown"],
        "phase_breakdown_sum_residual": inventory[
            "phase_breakdown_sum_residual"
        ],
        "phase_sum_residual_mod_2pi": phase_sum_residual,
        "formal_scalar_routed_gate_count": inventory[
            "global_phase_correction_routed_gate_count"
        ],
        "emitted_update_instructions": len(emitted_update),
        "landed_update_instructions": len(expected_update),
        "emitted_update_sha256": word_sha256(emitted_update),
        "landed_update_sha256": word_sha256(expected_update),
        "update_segment_signature_failures": update_signature_failures,
        "endpoint_packet_declared_scalar_angle": 0.0,
        "packet_Toffoli_decomposition_residual": C714.toffoli_residual(),
        "literal_vector_equality_uses_formal_unrouted_scalar": True,
        "circuit_and_route_ordinals": "circuit bookkeeping",
    }


def program_mutation_certificate(graph, context, seam, placement, program):
    mutations = {
        "delete_entire_endpoint_instrument": EmittedProgram(
            program.update_prefix, (), (), (), (), (), program.update_suffix, program.packet
        ),
        "delete_left_prewrite": EmittedProgram(
            program.update_prefix,
            tuple(row for row in program.endpoint_pre if row.kind != "endpoint_pre_left_B"),
            program.selected_seam, program.endpoint_post, program.endpoint_or,
            program.endpoint_clean, program.update_suffix, program.packet,
        ),
        "delete_selected_seam_primitive": EmittedProgram(
            program.update_prefix, program.endpoint_pre, program.selected_seam[1:],
            program.endpoint_post, program.endpoint_or, program.endpoint_clean,
            program.update_suffix, program.packet,
        ),
        "delete_OR_Toffoli": EmittedProgram(
            program.update_prefix, program.endpoint_pre, program.selected_seam,
            program.endpoint_post,
            tuple(row for row in program.endpoint_or if "Toffoli" not in row.kind),
            program.endpoint_clean, program.update_suffix, program.packet,
        ),
        "delete_endpoint_cleanup": EmittedProgram(
            program.update_prefix, program.endpoint_pre, program.selected_seam,
            program.endpoint_post, program.endpoint_or, (), program.update_suffix,
            program.packet,
        ),
        "delete_update_suffix": EmittedProgram(
            program.update_prefix, program.endpoint_pre, program.selected_seam,
            program.endpoint_post, program.endpoint_or, program.endpoint_clean, (),
            program.packet,
        ),
        "delete_packet_word": EmittedProgram(
            program.update_prefix, program.endpoint_pre, program.selected_seam,
            program.endpoint_post, program.endpoint_or, program.endpoint_clean,
            program.update_suffix, (),
        ),
        "delete_one_update_prefix_primitive": EmittedProgram(
            program.update_prefix[:-1], program.endpoint_pre, program.selected_seam,
            program.endpoint_post, program.endpoint_or, program.endpoint_clean,
            program.update_suffix, program.packet,
        ),
        "delete_one_selected_seam_primitive": EmittedProgram(
            program.update_prefix, program.endpoint_pre, program.selected_seam[:-1],
            program.endpoint_post, program.endpoint_or, program.endpoint_clean,
            program.update_suffix, program.packet,
        ),
        "delete_one_endpoint_post_primitive": EmittedProgram(
            program.update_prefix, program.endpoint_pre, program.selected_seam,
            program.endpoint_post[:-1], program.endpoint_or, program.endpoint_clean,
            program.update_suffix, program.packet,
        ),
        "delete_one_OR_Toffoli_primitive": EmittedProgram(
            program.update_prefix, program.endpoint_pre, program.selected_seam,
            program.endpoint_post, program.endpoint_or[:-1], program.endpoint_clean,
            program.update_suffix, program.packet,
        ),
        "delete_one_cleanup_primitive": EmittedProgram(
            program.update_prefix, program.endpoint_pre, program.selected_seam,
            program.endpoint_post, program.endpoint_or, program.endpoint_clean[:-1],
            program.update_suffix, program.packet,
        ),
        "delete_one_update_suffix_primitive": EmittedProgram(
            program.update_prefix, program.endpoint_pre, program.selected_seam,
            program.endpoint_post, program.endpoint_or, program.endpoint_clean,
            program.update_suffix[:-1], program.packet,
        ),
        "delete_one_packet_primitive": EmittedProgram(
            program.update_prefix, program.endpoint_pre, program.selected_seam,
            program.endpoint_post, program.endpoint_or, program.endpoint_clean,
            program.update_suffix, program.packet[:-1],
        ),
    }

    def independent_compile(rows):
        return tuple(
            instruction
            for rotation in rows
            for instruction in C870.c707.compile_pauli_rotation(
                C870.physical_lift(rotation.row, context),
                context.sites,
                rotation.angle,
            )
        )

    requested_index = C870.graph_seams(graph).index(seam)
    wrong_index = (requested_index + 1) % len(C870.graph_seams(graph))
    wrong_seam = C870.graph_seams(graph)[wrong_index]
    wrong_cell, wrong_axis, wrong_target, _wrong_left, _wrong_right = wrong_seam
    correct_species = C870.c219.common_species(float(C870.c230.BETA))
    correct_coin = C870.qr_coin_schedule(
        np.asarray(correct_species.coin, dtype=complex)
    )[0]
    correct_rotations, _inventory = C870.build_update(graph, correct_coin)
    wrong_factor = (
        "seam", wrong_index, wrong_cell, wrong_axis, wrong_target
    )
    wrong_selected = tuple(
        rotation for rotation in correct_rotations
        if rotation.kind == "directed_seam_fswap"
        and rotation.factor == wrong_factor
    )
    wrong_before = tuple(
        rotation for rotation in correct_rotations
        if rotation.serial < wrong_selected[0].serial
    )
    wrong_after = tuple(
        rotation for rotation in correct_rotations
        if rotation.serial > wrong_selected[-1].serial
    )
    mutations["wrong_selected_factor_partition"] = EmittedProgram(
        independent_compile(wrong_before),
        program.endpoint_pre,
        independent_compile(wrong_selected),
        program.endpoint_post,
        program.endpoint_or,
        program.endpoint_clean,
        independent_compile(wrong_after),
        program.packet,
    )

    empty_rotations, _empty_inventory = C870.build_update(graph, ())
    cell, axis, target, _left_mode, _right_mode = seam
    requested_factor = ("seam", requested_index, cell, axis, target)
    empty_selected = tuple(
        rotation for rotation in empty_rotations
        if rotation.kind == "directed_seam_fswap"
        and rotation.factor == requested_factor
    )
    empty_before = tuple(
        rotation for rotation in empty_rotations
        if rotation.serial < empty_selected[0].serial
    )
    empty_after = tuple(
        rotation for rotation in empty_rotations
        if rotation.serial > empty_selected[-1].serial
    )
    mutations["empty_coin_schedule_update"] = EmittedProgram(
        independent_compile(empty_before),
        program.endpoint_pre,
        independent_compile(empty_selected),
        program.endpoint_post,
        program.endpoint_or,
        program.endpoint_clean,
        independent_compile(empty_after),
        program.packet,
    )
    failure_counts = {
        label: binding_certificate(graph, context, seam, placement, damaged)[
            "failure_count"
        ]
        for label, damaged in mutations.items()
    }
    failure_counts.update({
        "hostile_endpoint_composition_omits_prewrite": binding_certificate(
            graph, context, seam, placement, program,
            declared_endpoint=(
                program.selected_seam + program.endpoint_post
                + program.endpoint_or + program.endpoint_clean
            ),
        )["failure_count"],
        "hostile_selected_packet_composition_omits_endpoint": binding_certificate(
            graph, context, seam, placement, program,
            declared_selected_packet=program.packet,
        )["failure_count"],
        "hostile_full_composition_omits_endpoint": binding_certificate(
            graph, context, seam, placement, program,
            declared_full=(
                program.update_prefix + program.selected_seam
                + program.update_suffix + program.packet
            ),
        )["failure_count"],
        "hostile_full_composition_moves_packet_before_suffix": binding_certificate(
            graph, context, seam, placement, program,
            declared_full=(
                program.update_prefix + program.endpoint + program.packet
                + program.update_suffix
            ),
        )["failure_count"],
    })
    return {
        "mutation_failure_counts": failure_counts,
        "inactive_mutations": tuple(
            label for label, count in failure_counts.items() if count == 0
        ),
    }


def splice_certificate(graph, seam) -> dict[str, object]:
    expected_species = C870.c219.common_species(float(C870.c230.BETA))
    expected_coin_schedule = C870.qr_coin_schedule(
        np.asarray(expected_species.coin, dtype=complex)
    )[0]
    rotations, inventory = C870.build_update(graph, expected_coin_schedule)
    cell, axis, target, _left_mode, _right_mode = seam
    seam_index = C870.graph_seams(graph).index(seam)
    factor = ("seam", seam_index, cell, axis, target)
    landed = tuple(rotation for rotation in rotations if rotation.factor == factor)
    replacement = selected_seam_rotations(graph, seam)
    match_failures = sum(
        left.kind != right.kind
        or left.meta != right.meta
        or left.row != right.row
        or abs(left.angle - right.angle) > TOL
        for left, right in zip(landed, replacement)
    ) + abs(len(landed) - len(replacement))
    return {
        "landed_update_rotations": len(rotations),
        "landed_factor_sha256": C870.factor_digest(rotations),
        "landed_kind_census": dict(sorted(Counter(row.kind for row in rotations).items())),
        "selected_factor": repr(factor),
        "selected_factor_rotation_count": len(landed),
        "replacement_rotation_count": len(replacement),
        "selected_rotation_match_failures": match_failures,
        "nonselected_rotation_count": len(rotations) - len(landed),
        "inventory": inventory,
    }


def coframe_coordinates(delta: Coord, basis: tuple[Coord, Coord, Coord]) -> tuple[int, int, int]:
    return tuple(sum(delta[i] * direction[i] for i in range(3)) for direction in basis)


def coframe_path(left: Coord, right: Coord, basis: tuple[Coord, Coord, Coord]) -> tuple[Coord, ...]:
    coefficients = coframe_coordinates(sub(right, left), basis)
    current = left
    path = [current]
    for coefficient, direction in zip(coefficients, basis):
        step = direction if coefficient >= 0 else scale(-1, direction)
        for _ in range(abs(coefficient)):
            current = add(current, step)
            path.append(current)
    if current != right:
        raise AssertionError(("coframe route missed endpoint", left, right, current))
    return tuple(path)


def route_certificate(word: tuple[Instruction, ...], basis) -> dict[str, object]:
    counts = Counter()
    routed = maximum_distance = nearest_neighbor_failures = 0
    operand_failures = return_failures = deletion_detected = 0
    touched = set()
    digest = sha256()
    for instruction in word:
        counts[instruction.kind] += 1
        if len(instruction.sites) == 1:
            routed += 1
            touched.update(instruction.sites)
            digest.update((instruction.kind + repr(instruction.sites)).encode())
            continue
        left, right = instruction.sites
        path = coframe_path(left, right, basis)
        distance = len(path) - 1
        maximum_distance = max(maximum_distance, distance)
        nearest_neighbor_failures += sum(
            sum(abs(a - b) for a, b in zip(x, y)) != 1
            for x, y in zip(path, path[1:])
        )
        labels = list(path)
        for index in range(len(path) - 2):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        operand_failures += labels[-2:] != [left, right]
        for index in reversed(range(len(path) - 2)):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        return_failures += labels != list(path)
        if len(path) > 2:
            damaged = list(path)
            # Omit the first forward route SWAP, retain the active gate and return.
            for index in range(1, len(path) - 2):
                damaged[index], damaged[index + 1] = damaged[index + 1], damaged[index]
            for index in reversed(range(len(path) - 2)):
                damaged[index], damaged[index + 1] = damaged[index + 1], damaged[index]
            deletion_detected += damaged != list(path)
        routed += 2 * distance - 1
        touched.update(path)
        digest.update((instruction.kind + repr(path)).encode())
    return {
        "logical_instructions": len(word),
        "routed_gates": routed,
        "maximum_route_distance": maximum_distance,
        "nearest_neighbor_failures": nearest_neighbor_failures,
        "operand_order_failures": operand_failures,
        "route_return_failures": return_failures,
        "route_return_deletion_detected_macros": deletion_detected,
        "touched_coordinates": len(touched),
        "logical_kind_census": dict(sorted(counts.items())),
        "route_schedule_sha256": digest.hexdigest(),
    }


def computed_fswap_plain_swap_residual(axis: int) -> float:
    left, right = 2 * axis + 1, 6 + 2 * axis
    vacuum = (0,) * 12
    double = tuple(int(index in (left, right)) for index in range(12))
    observed = {}
    plain = {}
    for source in (vacuum, double):
        target, phase = C704.GAUSS.target_fswap_action(source, left, right)
        observed[target] = observed.get(target, 0.0j) + phase / math.sqrt(2.0)
        plain[target] = plain.get(target, 0.0j) + 1.0 / math.sqrt(2.0)
    return float(math.sqrt(sum(
        abs(observed.get(key, 0.0j) - plain.get(key, 0.0j)) ** 2
        for key in set(observed) | set(plain)
    )))


def semantic_certificate() -> dict[str, object]:
    logical_rows = tuple(product((0, 1), repeat=12))
    cases = predicate_failures = scratch_failures = packet_failures = 0
    raw_mask_failures = normalized_mask_failures = phase_failures = 0
    deletion_pre_detected = deletion_toffoli_detected = 0
    contact_false_positives = inverse_failures = work_failures = 0
    raw_masks = set()
    for axis in range(3):
        left_mode, right_index = 2 * axis + 1, 6 + 2 * axis
        for logical in logical_rows:
            target, phase = C704.GAUSS.target_fswap_action(logical, left_mode, right_index)
            p = logical[left_mode] ^ logical[right_index]
            du = logical[left_mode] ^ target[left_mode]
            dv = logical[right_index] ^ target[right_index]
            pointer = du ^ dv ^ (du & dv)
            raw = C704.matter_delta_mask(logical, target)
            raw_masks.add(raw)
            normalized = 0
            for mode in range(6):
                if (raw >> mode) & 1:
                    normalized |= 1 << normalized_mode(axis, mode)
                if (raw >> (6 + mode)) & 1:
                    normalized |= 1 << (6 + normalized_mode(axis, mode))
            before = C714.initial(
                rotor=9, head=12, orientation=1,
                controls=(pointer, 1, 1, 1, 1, 1),
            )
            after = C714.apply_semantic(before, C714.word())
            cases += 1
            predicate_failures += pointer != p
            scratch_failures += (du ^ target[left_mode] ^ target[right_index]) != 0
            scratch_failures += (dv ^ target[left_mode] ^ target[right_index]) != 0
            raw_mask_failures += raw != (0 if not p else (1 << left_mode) | (1 << right_index))
            normalized_mask_failures += normalized != (0 if not p else 66)
            expected_delta = 66 if p else 0
            packet_failures += C714.integer(after, C714.PDELTA) != expected_delta
            packet_failures += after[C714.PEND] != p
            packet_failures += after[C714.PORIENT] != p
            work_failures += any(after[index] for index in C714.MCX_WORK + C714.ENABLE_WORK)
            restored = C714.apply_semantic(after, tuple(reversed(C714.word())))
            inverse_failures += restored != before
            # Omitting the left prewrite leaves dirty scratch on one moving
            # direction even when the OR output itself happens to agree.
            broken_du_after_clean = (
                target[left_mode] ^ target[left_mode] ^ target[right_index]
            )
            deletion_pre_detected += p and bool(broken_du_after_clean)
            # Without the OR Toffoli, du XOR dv is zero on every moving FSWAP.
            broken_or = du ^ dv
            deletion_toffoli_detected += p and broken_or != p
            # On the moving sector, compare the landed graph-local CAR action
            # with the independent globally ordered Fock target.  The phase is
            # not merely (-1)^(n_u n_v) for nonadjacent mode indices.
            if p:
                _observed, observed_phase = C704.GAUSS.corrected_fswap_action(
                    C704.GAUSS.extended_codeword(logical), left_mode, 2 * axis
                )
                phase_failures += abs(phase - observed_phase) > TOL
            contact_false_positives += C704.endpoint_from_b_change(logical, logical)

    frames = proper_frames()
    frame_rows = normalization_failures = unsigned_half_swap_failures = 0
    frame_orientation_failures = 0
    transported_masks = set()
    for axis in range(3):
        for frame in frames:
            raw, target_axis, sign = transported_raw_mask(axis, frame)
            transported_masks.add(raw)
            frame_rows += 1
            normalization_failures += normalize_raw_mask(raw, target_axis, sign) != 66
            unsigned_half_swap_failures += sign < 0 and normalize_raw_mask(raw, target_axis, 1) == 66
            orientation_bit = int(sign > 0)
            frame_orientation_failures += (1 if orientation_bit else -1) != sign

    # Positive CAR-phase witness: FSWAP and plain SWAP differ on the coherent
    # |00>+|11> superposition even though the endpoint pointer is zero.
    coherent_fswap_swap_residuals = tuple(
        computed_fswap_plain_swap_residual(axis) for axis in range(3)
    )
    # The existing orientation wire is independent of matter occupations.
    orientation_input_projection_bitset = 0
    for supplied in (0, 1):
        row = C714.initial(9, 12, supplied, (1, 1, 1, 1, 1, 1))
        out = C714.apply_semantic(row, C714.word())
        orientation_input_projection_bitset |= out[C714.PORIENT] << supplied

    return {
        "two_cell_columns": cases,
        "predicate_failures": predicate_failures,
        "scratch_cleanup_failures": scratch_failures,
        "packet_projection_failures": packet_failures,
        "raw_mask_failures": raw_mask_failures,
        "normalized_mask_failures": normalized_mask_failures,
        "FSWAP_phase_failures": phase_failures,
        "packet_work_return_failures": work_failures,
        "inverse_failures": inverse_failures,
        "contact_false_positives": contact_false_positives,
        "prewrite_deletion_detected_moving_cases": deletion_pre_detected,
        "OR_Toffoli_deletion_detected_moving_cases": deletion_toffoli_detected,
        "positive_axis_raw_masks": tuple(sorted(raw_masks)),
        "proper_frame_rows": frame_rows,
        "transported_nonzero_raw_masks": tuple(sorted(transported_masks)),
        "signed_normalization_failures": normalization_failures,
        "negative_frame_half_swap_deletion_undetected": unsigned_half_swap_failures,
        "signed_orientation_failures": frame_orientation_failures,
        "coherent_FSWAP_vs_SWAP_residuals": coherent_fswap_swap_residuals,
        "minimum_coherent_FSWAP_vs_SWAP_residual": min(
            coherent_fswap_swap_residuals
        ),
        "independent_orientation_outputs_bitset": orientation_input_projection_bitset,
    }


def geometry_fixture(shape: tuple[int, int, int], include_word: bool) -> dict[str, object]:
    graph = C870.prep.OpenReferenceGraph(shape_cells(shape))
    context = C870.physical_context(graph)
    seams = C870.graph_seams(graph)
    collision_failures = radius_failures = b_weight_failures = b_commutators = 0
    frame_coordinate_failures = coordinate_product_failures = 0
    program_signature_product_failures = route_path_product_failures = 0
    coframe_product_failures = 0
    placements = []
    for seam in seams:
        placement = packet_placement(graph, context, seam)
        placements.append(placement)
        collision_failures += len(set(placement.sites) & set(context.sites))
        collision_failures += len(set(placement.sites) & J870.auxiliary_registers(graph))
        radius_failures += placement.radius > 2
        cell, _axis, target, left_mode, right_mode = seam
        for row in (
            physical_b(graph, context, cell, left_mode),
            physical_b(graph, context, target, right_mode),
        ):
            b_weight_failures += len(z_support(row, context)) != 6
            b_commutators += sum(
                not row.commutes(stabilizer)
                for stabilizer in C870.physical_stabilizers(context)
            )

    selected = seams[0]
    placement = placements[0]
    program = emit_program(graph, context, selected, placement)
    selected_packet = program.selected_packet
    selected_route = route_certificate(selected_packet, placement.basis)
    full_route = None
    full_word = None
    if include_word:
        full_word = program.full
        full_route = route_certificate(full_word, placement.basis)

    frames = proper_frames()
    base_sites = set(placement.sites)
    covariance_words = (selected_packet,) + (() if full_word is None else (full_word,))
    path_rows = []
    program_signatures = []
    covariance_instruction_rows = 0
    for candidate_word in covariance_words:
        program_signatures.extend(map(instruction_signature, candidate_word))
        two_site = tuple(row for row in candidate_word if len(row.sites) == 2)
        candidate_paths = tuple(
            coframe_path(*instruction.sites, placement.basis)
            for instruction in two_site
        )
        covariance_instruction_rows += len(two_site)
        path_rows.extend(candidate_paths)
        for frame in frames:
            moved_basis = tuple(matvec(frame, direction) for direction in placement.basis)
            for instruction, path in zip(two_site, candidate_paths):
                moved_sites = tuple(matvec(frame, site) for site in instruction.sites)
                moved_path = coframe_path(*moved_sites, moved_basis)
                frame_coordinate_failures += moved_path != tuple(
                    matvec(frame, site) for site in path
                )
            moved_packet = {matvec(frame, site) for site in base_sites}
            frame_coordinate_failures += len(moved_packet) != len(base_sites)
    probe_sites = set(base_sites) | {site for path in path_rows for site in path}
    unique_program_signatures = tuple(sorted(set(program_signatures), key=repr))
    unique_paths = tuple(sorted(set(path_rows), key=repr))
    for left in frames:
        for right in frames:
            product_frame = left @ right
            coordinate_product_failures += sum(
                matvec(left, matvec(right, site)) != matvec(product_frame, site)
                for site in probe_sites
            )
            coframe_product_failures += sum(
                matvec(left, matvec(right, direction))
                != matvec(product_frame, direction)
                for direction in placement.basis
            )
            program_signature_product_failures += sum(
                transform_signature(transform_signature(signature, right), left)
                != transform_signature(signature, product_frame)
                for signature in unique_program_signatures
            )
            route_path_product_failures += sum(
                transform_path(transform_path(path, right), left)
                != transform_path(path, product_frame)
                for path in unique_paths
            )

    seam_rows = selected_seam_rotations(graph, selected)
    seam_semantics = C870.fswap_certificate(tuple(rotation.row for rotation in seam_rows))
    physical_semantics = C870.fswap_certificate(
        tuple(C870.physical_lift(rotation.row, context) for rotation in seam_rows)
    )
    return {
        "shape": shape,
        "cells": len(graph.cells),
        "seams": len(seams),
        "physical_carriers": len(context.sites),
        "packet_M2": C714.N,
        "packet_radius": max(row.radius for row in placements),
        "packet_carrier_or_aux_collisions": collision_failures,
        "packet_radius_failures": radius_failures,
        "physical_B_weight_failures": b_weight_failures,
        "physical_B_constraint_anticommutators": b_commutators,
        "splice": splice_certificate(graph, selected),
        "emitted_binding": binding_certificate(
            graph, context, selected, placement, program
        ),
        "emitted_mutations": program_mutation_certificate(
            graph, context, selected, placement, program
        ),
        "phase_representative": phase_representative_certificate(
            graph, context, program
        ),
        "selected_route": selected_route,
        "full_update_route": full_route,
        "proper_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "route_covariance_two_site_instructions": covariance_instruction_rows,
        "program_covariance_instructions": len(program_signatures),
        "unique_program_signatures": len(unique_program_signatures),
        "unique_route_paths": len(unique_paths),
        "ordered_program_signature_product_rows": (
            len(frames) ** 2 * len(unique_program_signatures)
        ),
        "ordered_route_path_product_rows": len(frames) ** 2 * len(unique_paths),
        "route_frame_coordinate_failures": frame_coordinate_failures,
        "coordinate_representation_product_failures": coordinate_product_failures,
        "coframe_product_failures": coframe_product_failures,
        "program_signature_product_failures": program_signature_product_failures,
        "route_path_product_failures": route_path_product_failures,
        "seam_maximum_four_rotation_residual": seam_semantics[
            "four_rotation_residual_up_to_global_phase"
        ],
        "physical_seam_maximum_four_rotation_residual": physical_semantics[
            "four_rotation_residual_up_to_global_phase"
        ],
    }


def downstream_certificate() -> dict[str, object]:
    packet = C704.packet_interface_controls()
    joint = C704.joint_order_controls()
    return {
        "packet_interface": packet,
        "joint_order": joint,
        "packet_interface_pass": all((
            packet["matching_statuses"] == C704.C610.BANK_SIZE + 1,
            packet["projection_failures"] == 0,
            packet["interval_failures"] == 0,
            packet["d_ab"] == 9,
            packet["d_bc"] == 12,
            packet["d_ac"] == 21,
            packet["additivity_closed"],
            packet["reversal_closed"],
            packet["inverse_returned_initial_state"],
            packet["forward_replay_exact"],
            packet["register_inverse_failures"] == 0,
            packet["carry_truth_failures"] == 0,
        )),
        "joint_order_pass": all((
            joint["consistent_statuses"] == ("admitted", "admitted"),
            joint["consistent_acyclic"],
            joint["inverted_refusal"] == "refused_inverted",
            joint["forced_cycle_detected"],
            joint["no_endpoint_status"] == "no_opportunity",
        )),
    }


def inherited_matter_certificate() -> dict[str, object]:
    species = C870.c219.common_species(float(C870.c230.BETA))
    coin = np.asarray(species.coin, dtype=complex)
    gates, qr = C870.qr_coin_schedule(coin)
    one_particle = C870.one_particle_semantics(coin, gates)
    contact = C870.contact_semantics()
    return {
        "QR": qr,
        "one_particle": one_particle,
        "contact": contact,
        "mass_fixture_pass": all((
            qr["QR_off_diagonal_residual"] < TOL,
            qr["reconstruction_residual"] < TOL,
            one_particle["coin_unitarity_residual"] < TOL,
            one_particle["maximum_coin_covariance_residual"] < TOL,
            one_particle["reverse_helper_permutation_residual"] < TOL,
            abs(one_particle["analytic_mass"] - one_particle["rest_mass"]) < TOL,
        )),
        "contact_fixture_pass": bool(
            contact["occupation_words"] == 64
            and contact["contact_pairs"] == 15
            and contact["maximum_residual_up_to_global_phase"] < TOL
        ),
        "interpretation": (
            "the endpoint/packet splice changes no Cycle219 coin or Cycle230 contact "
            "rotation; the retained pointer is an augmented logical output of the "
            "declared channel"
        ),
    }


def collect_failures(report: dict[str, object]) -> list[str]:
    failures = []
    provenance = report["provenance"]
    if provenance["pinned_input_failures"]:
        failures.append("pinned inputs")
    if provenance["unpinned_declared_inputs"]:
        failures.append("unpinned declared inputs")
    if provenance["missing_declared_inputs"]:
        failures.append("declared inputs")
    if provenance["duplicate_declared_inputs"]:
        failures.append("duplicate inputs")
    semantic = report["semantic"]
    exact_zero = (
        "predicate_failures", "scratch_cleanup_failures", "packet_projection_failures",
        "raw_mask_failures", "normalized_mask_failures", "FSWAP_phase_failures",
        "packet_work_return_failures", "inverse_failures", "contact_false_positives",
        "signed_normalization_failures",
        "negative_frame_half_swap_deletion_undetected", "signed_orientation_failures",
    )
    for key in exact_zero:
        if semantic[key] != 0:
            failures.append(f"semantic:{key}={semantic[key]}")
    if semantic["two_cell_columns"] != 3 * (1 << 12):
        failures.append("semantic column census")
    if semantic["transported_nonzero_raw_masks"] != (66, 129, 264, 516, 1056, 2064):
        failures.append("six transported raw masks")
    if semantic["minimum_coherent_FSWAP_vs_SWAP_residual"] < 1.0:
        failures.append("CAR phase control")
    if semantic["prewrite_deletion_detected_moving_cases"] == 0:
        failures.append("inactive prewrite deletion")
    if semantic["OR_Toffoli_deletion_detected_moving_cases"] == 0:
        failures.append("inactive OR-Toffoli deletion")
    if semantic["independent_orientation_outputs_bitset"] != 2:
        failures.append("orientation independence control")
    for fixture in report["fixtures"]:
        for key in (
            "packet_carrier_or_aux_collisions", "packet_radius_failures",
            "physical_B_weight_failures", "physical_B_constraint_anticommutators",
            "route_frame_coordinate_failures",
            "coordinate_representation_product_failures",
            "coframe_product_failures", "program_signature_product_failures",
            "route_path_product_failures",
        ):
            if fixture[key] != 0:
                failures.append(f"{fixture['shape']}:{key}={fixture[key]}")
        splice = fixture["splice"]
        if splice["selected_factor_rotation_count"] != 4:
            failures.append(f"{fixture['shape']}:selected factor census")
        if splice["replacement_rotation_count"] != 4:
            failures.append(f"{fixture['shape']}:replacement factor census")
        if splice["selected_rotation_match_failures"] != 0:
            failures.append(f"{fixture['shape']}:seam substitution mismatch")
        if splice["nonselected_rotation_count"] + 4 != splice["landed_update_rotations"]:
            failures.append(f"{fixture['shape']}:nonselected rotation conservation")
        binding = fixture["emitted_binding"]
        if binding["failure_count"] != 0:
            failures.append(f"{fixture['shape']}:emitted word not bound")
        if fixture["emitted_mutations"]["inactive_mutations"]:
            failures.append(f"{fixture['shape']}:inactive emitted mutation")
        phase = fixture["phase_representative"]
        if phase["update_segment_signature_failures"] != 0:
            failures.append(f"{fixture['shape']}:phase update segment mismatch")
        if phase["phase_breakdown_sum_residual"] > TOL:
            failures.append(f"{fixture['shape']}:phase breakdown")
        if phase["phase_sum_residual_mod_2pi"] > TOL:
            failures.append(f"{fixture['shape']}:formal phase correction")
        if phase["formal_scalar_routed_gate_count"] != 0:
            failures.append(f"{fixture['shape']}:formal scalar encoded as routed gate")
        if phase["packet_Toffoli_decomposition_residual"] > TOL:
            failures.append(f"{fixture['shape']}:packet Toffoli")
        for route_name in ("selected_route", "full_update_route"):
            route = fixture[route_name]
            if route is None:
                continue
            for key in (
                "nearest_neighbor_failures", "operand_order_failures", "route_return_failures"
            ):
                if route[key] != 0:
                    failures.append(f"{fixture['shape']}:{route_name}:{key}")
            if route["route_return_deletion_detected_macros"] == 0:
                failures.append(f"{fixture['shape']}:{route_name}:inactive route deletion")
        if fixture["seam_maximum_four_rotation_residual"] > TOL:
            failures.append(f"{fixture['shape']}:seam residual")
        if fixture["physical_seam_maximum_four_rotation_residual"] > TOL:
            failures.append(f"{fixture['shape']}:physical seam residual")
    if not report["downstream"]["packet_interface_pass"]:
        failures.append("unchanged packet interface")
    if not report["downstream"]["joint_order_pass"]:
        failures.append("unchanged JointOrder")
    if not report["inherited_matter"]["mass_fixture_pass"]:
        failures.append("one-particle mass fixture")
    if not report["inherited_matter"]["contact_fixture_pass"]:
        failures.append("contact fixture")
    return failures


def main() -> int:
    report = {
        "status": "pending",
        "claim_scope": (
            "selected-seam coherent Cycle870 physical endpoint opportunity -> fixed blank "
            "Cycle714 packet -> unchanged Cycle704/610/612 interface on the declared "
            "signed-coframe, blank-packet, head/rotor, control, and seam input domain"
        ),
        "provenance": provenance_certificate(),
        "semantic": semantic_certificate(),
        "fixtures": (
            geometry_fixture(PRIMARY_SHAPE, True),
            geometry_fixture(HELD_SHAPE, True),
        ),
        "inherited_matter": inherited_matter_certificate(),
        "downstream": downstream_certificate(),
        "declared_input_coordinates": (
            "selected seam and signed local coframe",
            "Cycle870 lawful codeword and clean bridge registers",
            "blank fixed-address packet cell 23 and clean packet work",
            "packet head, rotor, binder, actuality, admissibility, law-domain, and freshness inputs",
            "Cycle714 orientation input coordinate",
            "fixed serial circuit word and route-transit substrate",
            "Cycle219 coin and Cycle230 contact parameters",
        ),
        "constructed_outputs": (
            "physical endpoint B words and coherent XOR/OR opportunity pointer",
            "clean reuse of packet work M2 q56/q57 after endpoint extraction",
            "signed-frame half swap and local-port mask normalization to 66",
            "bounded radius-two 59-M2 placement and coframe-covariant returned routing",
            "fixed-cell packet projection into unchanged interval and JointOrder interfaces",
        ),
    }
    failures = collect_failures(report)
    report["validation_failures"] = failures
    report["status"] = "pass" if not failures else "fail"
    report["runner_sha256"] = file_sha256(Path(__file__))
    RECEIPT_PATH.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    print("CYCLE871_OPENREFERENCE_ENDPOINT_PACKET_PASS" if not failures else "CYCLE871_OPENREFERENCE_ENDPOINT_PACKET_FAIL")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
