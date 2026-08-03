#!/usr/bin/env python3
"""Cycle 872 bounded construction: one all-seam spatial packet epoch.

This runner writes one deterministic receipt.  It claims one bounded update
epoch on supplied clean own-bank inputs.  It does not derive causal
orientation or later-epoch bank renewal.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from hashlib import sha256
from itertools import groupby, product
import json
import math
import os
from pathlib import Path
import sys

import numpy as np


PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def discover_source_root() -> Path:
    supplied = os.environ.get("CYCLE872_SOURCE_ROOT")
    candidates = []
    if supplied:
        candidates.append(Path(supplied))
    for start in (Path.cwd(), PACKAGE_ROOT):
        candidates.extend((start, *start.parents))
    marker = "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py"
    for candidate in candidates:
        resolved = candidate.resolve()
        if (resolved / marker).is_file():
            return resolved
    raise RuntimeError(
        "Cycle872 upstream repository not found; run from its root or set "
        "CYCLE872_SOURCE_ROOT"
    )


SOURCE_ROOT = discover_source_root()
sys.path.insert(0, str(SOURCE_ROOT / "scripts"))

import frontier_cycle870_openreference_native_recurrent_update_2026_08_02 as C870
import frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02 as J870
import frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02 as C871
import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as C714
import frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25 as C704
import physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22 as C612


NOTE = "docs/OPENREFERENCE_ALL_SEAM_SPATIAL_DIRECTION_PACKET_EPOCH_CYCLE872_BOUNDED_THEOREM_NOTE_2026-08-03.md"
DEFAULT_RECEIPT = PACKAGE_ROOT / "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_receipt_2026_08_03.json"
EXPECTED_NOTE_SHA256 = "f8ef1a6951f9fdc62cfaa70c73b279d57ffd1e855d3c21c3cf1178270c1d2dd9"
EXPECTED_INPUT_SHA256 = {
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py": "717a60f45c7d7e9e354b50005fea6ace4bae7b63d74cebb48ded59546cc561f9",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py": "d5392152d322ea8f3850d0345d6caa426db22ae7f7694775b4bd6388704c18a6",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py": "a5e78e40cad0c43ee62ae887df7d84a0b895ab217ba4f3d521353e5d0b6bf95a",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py": "464e5928b7c1e46c23e4010363b6bd8ff3d0e2379c6e5ecb46891010ef47a5a4",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py": "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py": "3a977106389428d2281ea7e0e32b65fe57f6ce33d783742b80f264f78f4f2c17",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py": "fbf434a94c8dae57ffb6e68776642e4342a91f0d39f071ee1388fcb89ff846d7",
    "scripts/frontier_cycle703_local_cellular_plaquette_decoder_2026_07_25.py": "2d9618ab1c50448f4bd611826c3f265bb8985878a5d76d01d3b78d793d3635d0",
    "scripts/frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py": "eb0841f064bc840b1892a02ce1cf75e2c8275b6c21cc9b2952a5032cc03d4bb4",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py": "781823cf744be93de73f5e86e4e4cc988e0e7fe19c9c88a264b6f58169c07b0e",
    "scripts/frontier_cycle703_open_bksf_stabilizer_preparation_2026_07_25.py": "833ac9ee1d7f83185fdd66d89e2f3208e514c0b3b2cff660e7227dc28f506245",
    "scripts/frontier_cycle703_reversible_echo_ack_controller_2026_07_25.py": "5dab64cd17ead6cb5062eab9266b9206d74bb608dcc22f3a1132ee1f1af3e9a9",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py": "4d0049dbcb231301e0b0b110bc1933dfb2bda1aea2628e5e30bc5c1cee97d66a",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py": "71d073a95d089c13baf6fbaff4c3e3ebbd63650a3c152bba49f8de78ee377c69",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py": "b42ea07c1ed671b9cbab38bc38eba6f8166fe65be52295941a95e3ed75049abf",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py": "f5b604b714e8fbb33e2b6284cb38199e900859d710cd9e1411ee941a021235f3",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py": "3aa964a6eaca559048a53de580f39d9295a3e4b41ef9d4ff9dcdd4d3ff7444a7",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py": "5d49d85ddbc4daddfc0b24737dc569eaa9f32a050f5fccf48f048fe0fdd74b40",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py": "d74fb32e21879b2a843eae822c8e71b950729d9dc295eaf336911f174cceee3a",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py": "eb6c9a50681c69ea4fae47724c58d8ba10b48a270e7efa67a811af234afe9a1a",
    "scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py": "1b66c061dcb8e0082fd9e7264e78ccbd0f77440c0f517aa93696bde49f78c1bd",
    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py": "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237",
    "scripts/frontier_cycle870_openreference_physical_m2_placement_2026_08_02.py": "64b36432670f8a05179d0473e724afee1dfe6327cdd0233d3d788a6b8413c8a2",
    "scripts/frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02.py": "6645156635b4354d937759a28e71215121a19cefcc2f294a2791e6a84cf1423b",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py": "e79b733bd3b8e273a2094679e6175b5d1f253ebef1a33b96544519cbdf278e13",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py": "94f0fbd1212e210d0e073c3a80cdc2f92afa3c9807f981bd220625a67e8d94a0",
    "scripts/frontier_full128_code_projectors_2026_07_24.py": "f561714d036c8c7568b1772110303d6c0da11c6d73c9df3bdcbae2db632f5b44",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py": "ecae9048b4ee2d257315072cb7120335109f362fa7007573c46a82a1f0ed4195",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py": "17eca725b72943d8804147dd800be044ffaa80dc209588adb37ae6543d0fa935",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py": "b446ace0856b45108ae0ed4ed35614961ae3b69bf20d12132981f54809966afb",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py": "05cb2f6083cf6c4307c04284632e991b7fd7378cbd2a4eb08a52d5e3c7ae6b99",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py": "b418c74e82405a0511de81be0eef7080f98d5fe760ccac5d47783a6a751c2480",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py": "4ab857755b606d7ba7432179ed66de723ac31d3f66507cafa1168ab60d4965d6",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py": "97fdf54189d7da93099aeab4a9b1dd8501c7262d55493b9fa95bf1c2f5c97a9d",
    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py": "15db2200b08bc4a5d7669975806fe51e9b8a55049f0660969d427332602bf9e8",
    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py": "67aa2435d66fb34b6734cc564a82ac839525139fdc9e8c347dc1b2277d08b40b",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py": "ef6805e691a1ddd303a96f7cabd7000517e0cf33d5b1c577b20c2cbbf29aca23",
    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py": "4ef60441d31d62b1fc61c9b5e09ff3bc8f7f32d1b68bc3c548834431d24302f6",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py": "36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py": "a9786cf68a9c669e7e7fe310a00ab9912aa404689651682ccfe3045a06e357f1",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py": "6365d5aed1e70fb9b427ee6fb987879027cc30c818856a992b3fbf9d057e0c1b",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py": "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py": "472e28c78901368629c8d9d6f614bb8fb3ea003639ac61d480d06941cdf6cb86",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py": "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py": "9ef0fff433bbf1c96c9b13c5ce79530e01fe705f08c6caf6b60316e20359e011",
}

Coord = tuple[int, int, int]
SPATIAL_CURRENT_LOCAL = (0, 0, 3)


@dataclass(frozen=True)
class BoundInstruction:
    serial: int
    factor_index: int
    factor: tuple[object, ...]
    stage: str
    segment: str
    rotation_serial: int | None
    instruction: object = field(repr=False, compare=False)
    route_policy: str
    path: tuple[Coord, ...]
    gate_start: int
    gate_stop: int


@dataclass(frozen=True)
class ExecutablePhysicalGate:
    serial: int
    factor_index: int
    instruction_serial: int
    role: str
    sites: tuple[Coord, ...]
    matrix: np.ndarray = field(repr=False, compare=False)


@dataclass(frozen=True)
class PhysicalEpochStream:
    length: int
    native_rotations: tuple[object, ...]
    native_inventory: dict[str, object]
    native_factors: tuple[tuple[tuple[object, ...], tuple[object, ...]], ...]
    factor_manifest: tuple[dict[str, object], ...]
    instructions: tuple[BoundInstruction, ...]
    gates: tuple[ExecutablePhysicalGate, ...]
    matrix_registry: dict[str, dict[str, object]]
    construction_failures: dict[str, int]
    deletion_detections: int


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def cells(length: int) -> tuple[Coord, ...]:
    return tuple(product(range(length), repeat=3))


def color(seam) -> tuple[int, int, int, int]:
    owner, axis = seam[0], seam[1]
    remaining = tuple(owner[index] & 1 for index in range(3) if index != axis)
    return axis, owner[axis] & 1, *remaining


def coarse_color(seam) -> tuple[int, int]:
    return seam[1], seam[0][seam[1]] & 1


def spatial_current_site(placement) -> Coord:
    """The retained spatial-current output, separate from causal ORIENT."""
    site = placement.midpoint
    for coefficient, direction in zip(SPATIAL_CURRENT_LOCAL, placement.basis):
        site = C871.add(site, C871.scale(coefficient, direction))
    return site


def resource_bank(placement) -> frozenset[Coord]:
    return frozenset((*placement.sites, spatial_current_site(placement)))


def provenance_certificate():
    observed = {
        label: file_sha256(SOURCE_ROOT / label)
        for label in EXPECTED_INPUT_SHA256
        if (SOURCE_ROOT / label).is_file()
    }
    return {
        "declared_inputs": tuple(EXPECTED_INPUT_SHA256),
        "literal_dependency_pin_count": len(EXPECTED_INPUT_SHA256),
        "dependency_surface": (
            "complete local Python import closure plus dynamically loaded Cycle870 "
            "placement and Cycle610/611 modules"
        ),
        "input_sha256": observed,
        "missing_inputs": tuple(
            label for label in EXPECTED_INPUT_SHA256 if label not in observed
        ),
        "pin_failures": {
            label: {"expected": expected, "observed": observed.get(label)}
            for label, expected in EXPECTED_INPUT_SHA256.items()
            if observed.get(label) != expected
        },
        "theorem_note": NOTE,
        "theorem_note_sha256": file_sha256(PACKAGE_ROOT / NOTE),
        "theorem_note_pin_failure": (
            file_sha256(PACKAGE_ROOT / NOTE) != EXPECTED_NOTE_SHA256
        ),
        "runner_sha256": file_sha256(Path(__file__)),
    }


def candidate_segments(graph, context, seam, placement, *, wrong_side=False,
                       delete_seam=False, seam_rotations=None):
    cell, _axis, target, left_mode, right_mode = seam
    left_b = C871.physical_b(graph, context, cell, left_mode)
    right_b = C871.physical_b(graph, context, target, right_mode)
    du = placement.sites[C714.MCX_WORK[0]]
    dv = placement.sites[C714.MCX_WORK[1]]
    pointer = placement.sites[C714.POINTER]
    spatial = spatial_current_site(placement)
    pre = (
        C871.extract_b(left_b, context, du, "endpoint_pre_left_B")
        + C871.extract_b(right_b, context, dv, "endpoint_pre_right_B")
    )
    seam_word = C871.compile_rotations(
        C871.selected_seam_rotations(graph, seam)
        if seam_rotations is None else seam_rotations,
        context,
    )
    if delete_seam:
        seam_word = ()
    post = (
        C871.extract_b(left_b, context, du, "endpoint_post_left_B")
        + C871.extract_b(right_b, context, dv, "endpoint_post_right_B")
    )
    endpoint_or = (
        C871.cnot(du, pointer, "endpoint_OR_CNOT"),
        C871.cnot(dv, pointer, "endpoint_OR_CNOT"),
    ) + C871.toffoli_word(du, dv, pointer, "endpoint_OR_Toffoli_")
    clean = (
        C871.extract_b(left_b, context, du, "endpoint_clean_left_B")
        + C871.extract_b(right_b, context, du, "endpoint_clean_right_B")
        + C871.extract_b(left_b, context, dv, "endpoint_clean_left_B")
        + C871.extract_b(right_b, context, dv, "endpoint_clean_right_B")
    )
    direction_b = left_b if wrong_side else right_b
    direction = (
        C871.extract_b(direction_b, context, du, "spatial_direction_B_load")
        + C871.toffoli_word(pointer, du, spatial, "spatial_direction_Toffoli_")
        + C871.extract_b(direction_b, context, du, "spatial_direction_B_unload")
    )
    return {
        "pre": pre,
        "seam": seam_word,
        "post": post,
        "or": endpoint_or,
        "clean": clean,
        "spatial_direction_write": direction,
        "packet": C871.packet_word(placement),
    }


def flatten(segments):
    return tuple(row for segment in segments.values() for row in segment)


def canonical_json_bytes(value) -> bytes:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), default=float)
        + "\n"
    ).encode()


def matrix_payload(matrix: np.ndarray) -> dict[str, object]:
    array = np.asarray(matrix, dtype=complex)
    return {
        "shape": tuple(map(int, array.shape)),
        "row_major_complex_float_hex": tuple(
            (float(value.real).hex(), float(value.imag).hex())
            for value in array.reshape(-1)
        ),
        "cycle655_rounded_matrix_sha256": C870.c707.c655.matrix_digest(array),
    }


def matrix_key(matrix: np.ndarray) -> str:
    return sha256(canonical_json_bytes(matrix_payload(matrix))).hexdigest()


def serialize_bound_instruction(row: BoundInstruction) -> dict[str, object]:
    instruction = row.instruction
    return {
        "serial": row.serial,
        "factor_index": row.factor_index,
        "factor": row.factor,
        "stage": row.stage,
        "segment": row.segment,
        "rotation_serial": row.rotation_serial,
        "kind": instruction.kind,
        "unrouted_sites": instruction.sites,
        "unrouted_matrix": matrix_key(instruction.matrix),
        "route_policy": row.route_policy,
        "path": row.path,
        "gate_serial_start": row.gate_start,
        "gate_serial_stop_exclusive": row.gate_stop,
    }


def serialize_physical_gate(row: ExecutablePhysicalGate) -> dict[str, object]:
    return {
        "serial": row.serial,
        "factor_index": row.factor_index,
        "instruction_serial": row.instruction_serial,
        "role": row.role,
        "sites": row.sites,
        "matrix": matrix_key(row.matrix),
    }


def physical_stream_payload(stream: PhysicalEpochStream) -> dict[str, object]:
    return {
        "schema": "cycle872-executable-local-gate-stream-v1",
        "length": stream.length,
        "composition_order": (
            "ascending physical-gate serial; each listed local matrix left-multiplies "
            "the state after the preceding gate"
        ),
        "local_basis": (
            "one-site |0>,|1>; two-site little-endian |00>,|10>,|01>,|11> "
            "with first listed site as local bit zero"
        ),
        "semantic_scope": (
            "exact local matrices and global serial composition/order certificate; "
            "no global statevector or global matrix was constructed"
        ),
        "formal_zero_site_global_phase_correction_angle": stream.native_inventory[
            "exact_target_global_phase_correction_angle"
        ],
        "factor_manifest": stream.factor_manifest,
        "instruction_bindings": tuple(
            serialize_bound_instruction(row) for row in stream.instructions
        ),
        "physical_gates": tuple(serialize_physical_gate(row) for row in stream.gates),
        "matrix_registry": dict(sorted(stream.matrix_registry.items())),
    }


def build_physical_epoch_stream(length: int) -> PhysicalEpochStream:
    """Materialize one complete, serial, locally executable physical epoch."""
    graph = C870.prep.OpenReferenceGraph(cells(length))
    context = C870.physical_context(graph)
    seams = C870.graph_seams(graph)
    placements = tuple(C871.packet_placement(graph, context, seam) for seam in seams)
    rotations, inventory = C870.build_update(graph, C871.coin_schedule())
    factors = tuple(
        (tuple(factor), tuple(group))
        for factor, group in groupby(rotations, key=lambda row: row.factor)
    )
    seam_lookup = {
        ("seam", index, seam[0], seam[1], seam[2]): (seam, placements[index])
        for index, seam in enumerate(seams)
    }
    registry: dict[str, dict[str, object]] = {}
    instructions: list[BoundInstruction] = []
    gates: list[ExecutablePhysicalGate] = []
    factor_manifest: list[dict[str, object]] = []
    failures = Counter()
    deletion_detections = 0

    def register(matrix) -> str:
        key = matrix_key(matrix)
        payload = matrix_payload(matrix)
        failures["matrix_digest_collision"] += key in registry and registry[key] != payload
        registry[key] = payload
        return key

    def emit_instruction(
        factor_index: int,
        factor: tuple[object, ...],
        stage: str,
        segment: str,
        rotation_serial: int | None,
        instruction,
        route_policy: str,
        basis,
    ) -> None:
        nonlocal deletion_detections
        instruction_serial = len(instructions)
        failures["unsupported_instruction_arity"] += len(instruction.sites) not in (1, 2)
        if len(instruction.sites) == 1:
            path = tuple(instruction.sites)
        elif route_policy == "landed_global_axis_manhattan_returned":
            path = tuple(C870.c707.c655.manhattan_path(*instruction.sites))
        else:
            path = C871.coframe_path(*instruction.sites, basis)
        failures["route_endpoint"] += (
            not path
            or path[0] != instruction.sites[0]
            or path[-1] != instruction.sites[-1]
        )
        gate_start = len(gates)
        register(instruction.matrix)
        if len(instruction.sites) == 1:
            gates.append(ExecutablePhysicalGate(
                len(gates), factor_index, instruction_serial, "active_one_site",
                instruction.sites, instruction.matrix,
            ))
        elif len(instruction.sites) == 2:
            labels = list(path)
            for route_index in range(len(path) - 2):
                sites = (path[route_index], path[route_index + 1])
                gates.append(ExecutablePhysicalGate(
                    len(gates), factor_index, instruction_serial, "swap_forward",
                    sites, C870.c707.c655.SWAP,
                ))
                register(C870.c707.c655.SWAP)
                labels[route_index], labels[route_index + 1] = (
                    labels[route_index + 1], labels[route_index]
                )
            active_sites = (path[-2], path[-1])
            failures["active_operand_binding"] += tuple(labels[-2:]) != instruction.sites
            gates.append(ExecutablePhysicalGate(
                len(gates), factor_index, instruction_serial, "active_two_site",
                active_sites, instruction.matrix,
            ))
            for route_index in reversed(range(len(path) - 2)):
                sites = (path[route_index], path[route_index + 1])
                gates.append(ExecutablePhysicalGate(
                    len(gates), factor_index, instruction_serial, "swap_return",
                    sites, C870.c707.c655.SWAP,
                ))
                labels[route_index], labels[route_index + 1] = (
                    labels[route_index + 1], labels[route_index]
                )
            failures["spectator_permutation_return"] += labels != list(path)
            if len(path) > 2:
                damaged = list(path)
                for route_index in range(1, len(path) - 2):
                    damaged[route_index], damaged[route_index + 1] = (
                        damaged[route_index + 1], damaged[route_index]
                    )
                for route_index in reversed(range(len(path) - 2)):
                    damaged[route_index], damaged[route_index + 1] = (
                        damaged[route_index + 1], damaged[route_index]
                    )
                deletion_detections += damaged != list(path)
        gate_stop = len(gates)
        active = tuple(
            row for row in gates[gate_start:gate_stop] if row.role.startswith("active")
        )
        failures["active_gate_count"] += len(active) != 1
        if len(active) == 1:
            failures["active_matrix_binding"] += (
                matrix_key(active[0].matrix) != matrix_key(instruction.matrix)
            )
        instructions.append(BoundInstruction(
            instruction_serial, factor_index, factor, stage, segment,
            rotation_serial, instruction, route_policy, path, gate_start, gate_stop,
        ))

    for factor_index, (factor, factor_rotations) in enumerate(factors):
        stage = str(factor[0])
        instruction_start = len(instructions)
        gate_start = len(gates)
        route_policy = (
            "augmented_seam_local_coframe_returned"
            if stage == "seam" else "landed_global_axis_manhattan_returned"
        )
        if stage == "seam":
            seam_binding = seam_lookup.get(factor)
            failures["seam_factor_lookup"] += seam_binding is None
            if seam_binding is None:
                continue
            seam, placement = seam_binding
            candidate = candidate_segments(
                graph, context, seam, placement, seam_rotations=factor_rotations
            )
            for segment, segment_word in candidate.items():
                if segment == "seam":
                    actual = []
                    for rotation in factor_rotations:
                        rotation_word = C870.c707.compile_pauli_rotation(
                            C870.physical_lift(rotation.row, context),
                            context.sites,
                            rotation.angle,
                        )
                        actual.extend(rotation_word)
                        for instruction in rotation_word:
                            emit_instruction(
                                factor_index, factor, stage, segment, rotation.serial,
                                instruction, route_policy, placement.basis,
                            )
                    failures["seam_segment_actual_word"] += (
                        C871.word_sha256(tuple(actual)) != C871.word_sha256(segment_word)
                    )
                else:
                    for instruction in segment_word:
                        emit_instruction(
                            factor_index, factor, stage, segment, None,
                            instruction, route_policy, placement.basis,
                        )
        else:
            for rotation in factor_rotations:
                rotation_word = C870.c707.compile_pauli_rotation(
                    C870.physical_lift(rotation.row, context),
                    context.sites,
                    rotation.angle,
                )
                for instruction in rotation_word:
                    emit_instruction(
                        factor_index, factor, stage, "landed_factor",
                        rotation.serial, instruction, route_policy, None,
                    )
        factor_manifest.append({
            "factor_index": factor_index,
            "factor": factor,
            "stage": stage,
            "native_rotation_serials": tuple(row.serial for row in factor_rotations),
            "replacement": "augmented_seam_macro" if stage == "seam" else "identity",
            "route_policy": route_policy,
            "instruction_serial_start": instruction_start,
            "instruction_serial_stop_exclusive": len(instructions),
            "physical_gate_serial_start": gate_start,
            "physical_gate_serial_stop_exclusive": len(gates),
        })

    expected_factor_sequence = tuple(factor for factor, _rows in factors)
    observed_factor_sequence = tuple(row["factor"] for row in factor_manifest)
    failures["factor_sequence"] += observed_factor_sequence != expected_factor_sequence
    failures["factor_count"] += len(factor_manifest) != len(factors)
    failures["rotation_coverage"] += tuple(
        serial
        for row in factor_manifest
        for serial in row["native_rotation_serials"]
    ) != tuple(row.serial for row in rotations)
    failures["instruction_serial"] += any(
        row.serial != index for index, row in enumerate(instructions)
    )
    failures["physical_gate_serial"] += any(
        row.serial != index for index, row in enumerate(gates)
    )
    failures["factor_binding"] += sum(
        row.factor_index != instruction.factor_index
        for instruction in instructions
        for row in gates[instruction.gate_start:instruction.gate_stop]
    )
    failures["NN_support"] += sum(
        len(row.sites) == 2 and C870.c707.c655.l1(*row.sites) != 1
        for row in gates
    )
    failures["gate_arity"] += sum(len(row.sites) not in (1, 2) for row in gates)
    failures["stage_order"] += tuple(dict.fromkeys(
        row["stage"] for row in factor_manifest
    )) != ("coin", "reverse", "seam", "contact")
    failures["landed_nonseam_route_policy"] += sum(
        row["stage"] != "seam"
        and row["route_policy"] != "landed_global_axis_manhattan_returned"
        for row in factor_manifest
    )
    failures["seam_route_policy"] += sum(
        row["stage"] == "seam"
        and row["route_policy"] != "augmented_seam_local_coframe_returned"
        for row in factor_manifest
    )
    return PhysicalEpochStream(
        length, rotations, inventory, factors, tuple(factor_manifest),
        tuple(instructions), tuple(gates), registry, dict(failures),
        deletion_detections,
    )


def physical_stream_certificate(stream: PhysicalEpochStream) -> dict[str, object]:
    payload = physical_stream_payload(stream)
    payload_bytes = canonical_json_bytes(payload)
    gate_payload = tuple(serialize_physical_gate(row) for row in stream.gates)
    instruction_payload = tuple(
        serialize_bound_instruction(row) for row in stream.instructions
    )
    semantic_instruction_payload = tuple(
        {key: value for key, value in row.items() if key != "kind"}
        for row in instruction_payload
    )
    stage_factors = Counter(row["stage"] for row in stream.factor_manifest)
    stage_gates = Counter(
        stream.factor_manifest[row.factor_index]["stage"] for row in stream.gates
    )
    route_roles = Counter(row.role for row in stream.gates)
    return {
        "length": stream.length,
        "cells": stream.length ** 3,
        "native_rotations": len(stream.native_rotations),
        "native_factors": len(stream.native_factors),
        "augmented_seam_factors": stage_factors["seam"],
        "factor_stage_census": dict(stage_factors),
        "physical_gate_stage_census": dict(stage_gates),
        "unrouted_bound_instructions": len(stream.instructions),
        "physical_local_gates": len(stream.gates),
        "physical_gate_role_census": dict(route_roles),
        "matrix_registry_entries": len(stream.matrix_registry),
        "matrix_registry_sha256": sha256(canonical_json_bytes(
            dict(sorted(stream.matrix_registry.items()))
        )).hexdigest(),
        "factor_manifest_sha256": sha256(canonical_json_bytes(
            stream.factor_manifest
        )).hexdigest(),
        "instruction_binding_sha256": sha256(canonical_json_bytes(
            instruction_payload
        )).hexdigest(),
        "label_insensitive_instruction_binding_sha256": sha256(
            canonical_json_bytes(semantic_instruction_payload)
        ).hexdigest(),
        "instruction_label_scope": (
            "kind strings are diagnostic compiler labels; independent comparison "
            "uses the label-insensitive binding digest over factors, rotations, "
            "segments, sites, exact matrices, paths, and gate ranges"
        ),
        "normalized_physical_gate_sha256": sha256(canonical_json_bytes(
            gate_payload
        )).hexdigest(),
        "serialized_stream_sha256": sha256(payload_bytes).hexdigest(),
        "serialized_stream_bytes": len(payload_bytes),
        "construction_failure_census": stream.construction_failures,
        "first_forward_swap_deletion_detections": stream.deletion_detections,
        "deletion_control_scope": (
            "delete the first forward SWAP of every nontrivial returned route; "
            "not exhaustive over arbitrary SWAP positions"
        ),
        "native_factor_sha256": C870.factor_digest(stream.native_rotations),
        "factor_order": "exact Cycle870 serial factor order",
        "nonseam_route": "landed C707/C655 global-axis Manhattan returned route",
        "seam_route": "declared Cycle872 local-coframe returned replacement",
        "spectator_statement": (
            "identity label permutation with intended operands at every active gate; "
            "therefore exact on arbitrary dirty or entangled spectator states"
        ),
        "execution_scope": (
            "exact local gate matrices plus global serial composition/order; "
            "no global statevector or global matrix execution"
        ),
    }


def routed_macro_gate_payload(word, basis) -> tuple[dict[str, object], ...]:
    output = []
    for instruction_serial, instruction in enumerate(word):
        source_matrix = matrix_key(instruction.matrix)
        if len(instruction.sites) == 1:
            output.append({
                "instruction_serial": instruction_serial,
                "role": "active_one_site",
                "sites": instruction.sites,
                "matrix": source_matrix,
            })
            continue
        path = C871.coframe_path(*instruction.sites, basis)
        swap_matrix = matrix_key(C870.c707.c655.SWAP)
        for index in range(len(path) - 2):
            output.append({
                "instruction_serial": instruction_serial,
                "role": "swap_forward",
                "sites": (path[index], path[index + 1]),
                "matrix": swap_matrix,
            })
        output.append({
            "instruction_serial": instruction_serial,
            "role": "active_two_site",
            "sites": (path[-2], path[-1]),
            "matrix": source_matrix,
        })
        for index in reversed(range(len(path) - 2)):
            output.append({
                "instruction_serial": instruction_serial,
                "role": "swap_return",
                "sites": (path[index], path[index + 1]),
                "matrix": swap_matrix,
            })
    return tuple(output)


def physical_macro_mutation_certificate() -> dict[str, object]:
    """Digest actual coframe-routed canonical and damaged seam macros."""
    graph = C870.prep.OpenReferenceGraph(cells(2))
    context = C870.physical_context(graph)
    seams = C870.graph_seams(graph)
    canonical = []
    wrong_side = []
    seam_deleted = []
    for seam in seams:
        placement = C871.packet_placement(graph, context, seam)
        canonical.append(routed_macro_gate_payload(
            flatten(candidate_segments(graph, context, seam, placement)),
            placement.basis,
        ))
        wrong_side.append(routed_macro_gate_payload(
            flatten(candidate_segments(
                graph, context, seam, placement, wrong_side=True
            )),
            placement.basis,
        ))
        seam_deleted.append(routed_macro_gate_payload(
            flatten(candidate_segments(
                graph, context, seam, placement, delete_seam=True
            )),
            placement.basis,
        ))
    nn_failures = sum(
        len(gate["sites"]) == 2 and C870.c707.c655.l1(*gate["sites"]) != 1
        for family in (canonical, wrong_side, seam_deleted)
        for macro in family for gate in macro
    )
    return {
        "shape": (2, 2, 2),
        "seams": len(seams),
        "canonical_routed_macro_sha256": sha256(canonical_json_bytes(
            tuple(canonical)
        )).hexdigest(),
        "wrong_side_routed_macro_sha256": sha256(canonical_json_bytes(
            tuple(wrong_side)
        )).hexdigest(),
        "seam_deleted_routed_macro_sha256": sha256(canonical_json_bytes(
            tuple(seam_deleted)
        )).hexdigest(),
        "wrong_side_digest_detections": sum(
            left != right for left, right in zip(canonical, wrong_side)
        ),
        "seam_deletion_digest_detections": sum(
            left != right for left, right in zip(canonical, seam_deleted)
        ),
        "NN_failures": nn_failures,
        "semantic_supported_rows": "reported in spatial_direction",
    }


def route_word(word, basis):
    output = []
    deletion_detected = 0
    for instruction_index, instruction in enumerate(word):
        if len(instruction.sites) == 1:
            output.append(("ACTIVE:" + instruction.kind, instruction.sites, instruction_index))
            continue
        path = C871.coframe_path(*instruction.sites, basis)
        forward = [
            ("SWAP_FORWARD", (path[index], path[index + 1]), instruction_index)
            for index in range(len(path) - 2)
        ]
        active = [("ACTIVE:" + instruction.kind, (path[-2], path[-1]), instruction_index)]
        backward = [
            ("SWAP_RETURN", (path[index], path[index + 1]), instruction_index)
            for index in reversed(range(len(path) - 2))
        ]
        output.extend(forward + active + backward)
        if forward:
            labels = list(range(len(path)))
            # Delete the first forward SWAP but retain the gate and full return.
            for index in range(1, len(path) - 2):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            for index in reversed(range(len(path) - 2)):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            deletion_detected += labels != list(range(len(path)))
    return tuple(output), deletion_detected


def footprint(word, basis):
    output = set()
    for instruction in word:
        if len(instruction.sites) == 1:
            output.update(instruction.sites)
        else:
            output.update(C871.coframe_path(*instruction.sites, basis))
    return output


def returned_path_labels(path):
    labels = list(range(len(path)))
    for index in range(len(path) - 2):
        labels[index], labels[index + 1] = labels[index + 1], labels[index]
    operands = tuple(labels[-2:])
    for index in reversed(range(len(path) - 2)):
        labels[index], labels[index + 1] = labels[index + 1], labels[index]
    return operands, tuple(labels)


def schedule_order(seams):
    output = []
    for coarse in tuple(dict.fromkeys(map(coarse_color, seams))):
        members = tuple(seam for seam in seams if coarse_color(seam) == coarse)
        for fine in sorted(set(map(color, members))):
            output.extend(seam for seam in members if color(seam) == fine)
    return tuple(output)


def epoch_fixture(length: int):
    graph = C870.prep.OpenReferenceGraph(cells(length))
    context = C870.physical_context(graph)
    seams = C870.graph_seams(graph)
    placements = tuple(C871.packet_placement(graph, context, seam) for seam in seams)
    spatial_sites = tuple(spatial_current_site(placement) for placement in placements)
    resource_banks = tuple(resource_bank(placement) for placement in placements)
    blocked = set(context.sites) | J870.auxiliary_registers(graph)
    segments = tuple(
        candidate_segments(graph, context, seam, placement)
        for seam, placement in zip(seams, placements)
    )
    words = tuple(map(flatten, segments))
    used_packet_union = set().union(*(set(placement.sites) for placement in placements))
    used_resource_union = set().union(*resource_banks)
    packet_pair_overlaps = sum(
        bool(set(left.sites) & set(right.sites))
        for index, left in enumerate(placements) for right in placements[:index]
    )
    resource_pair_overlaps = sum(
        bool(left & right)
        for index, left in enumerate(resource_banks) for right in resource_banks[:index]
    )
    spatial_geometry = {
        "duplicate_output_sites": len(spatial_sites) - len(set(spatial_sites)),
        "packet_aliases": sum(site in used_packet_union for site in spatial_sites),
        "native_aux_collisions": sum(site in blocked for site in spatial_sites),
    }
    routes = {}
    deletions = 0
    footprints = {}
    for seam, placement, word in zip(seams, placements, words):
        routes[seam], detected = route_word(word, placement.basis)
        deletions += detected
        footprints[seam] = footprint(word, placement.basis)

    route_reconciliation = Counter()
    for placement, candidate in zip(placements, segments):
        for instruction in candidate["seam"]:
            if len(instruction.sites) != 2:
                continue
            replacement = C871.coframe_path(*instruction.sites, placement.basis)
            landed = tuple(C870.c707.c655.manhattan_path(*instruction.sites))
            replacement_operands, replacement_return = returned_path_labels(replacement)
            landed_operands, landed_return = returned_path_labels(landed)
            route_reconciliation["retained_two_site_instructions"] += 1
            route_reconciliation["path_differences"] += replacement != landed
            route_reconciliation["endpoint_failures"] += (
                replacement[0] != landed[0]
                or replacement[-1] != landed[-1]
                or replacement[0] != instruction.sites[0]
                or replacement[-1] != instruction.sites[1]
            )
            route_reconciliation["replacement_operand_failures"] += (
                replacement_operands != (0, len(replacement) - 1)
            )
            route_reconciliation["landed_operand_failures"] += (
                landed_operands != (0, len(landed) - 1)
            )
            route_reconciliation["replacement_return_failures"] += (
                replacement_return != tuple(range(len(replacement)))
            )
            route_reconciliation["landed_return_failures"] += (
                landed_return != tuple(range(len(landed)))
            )
            route_reconciliation["replacement_routed_gates"] += 2 * len(replacement) - 3
            route_reconciliation["landed_routed_gates"] += 2 * len(landed) - 3

    rotations, inventory = C870.build_update(graph, C871.coin_schedule())
    factors = tuple(
        (factor, tuple(group))
        for factor, group in groupby(rotations, key=lambda row: row.factor)
    )
    actual_seams = tuple((factor, rows) for factor, rows in factors if factor[0] == "seam")
    binding_failures = Counter()
    physical_rows = {}
    logical_polys = {}
    packet_sites = {}
    endpoint_modes = {}
    for seam_index, (seam, placement, candidate) in enumerate(zip(seams, placements, segments)):
        expected = ("seam", seam_index, seam[0], seam[1], seam[2])
        selected = tuple(rows for factor, rows in actual_seams if factor == expected)
        binding_failures["selection"] += len(selected) != 1
        if len(selected) == 1:
            binding_failures["four_rotations"] += len(selected[0]) != 4
            actual_word = C871.compile_rotations(selected[0], context)
            binding_failures["compiled_word"] += (
                C871.word_sha256(actual_word) != C871.word_sha256(candidate["seam"])
            )
        cell, _axis, target, left_mode, right_mode = seam
        u = graph.vertex_index[(cell, left_mode)]
        v = graph.vertex_index[(target, right_mode)]
        logical = (
            graph.B(u), graph.B(v),
            *C870.seam_hop_rows(graph, cell, left_mode, target, right_mode),
        )
        physical_rows[seam] = tuple(C870.physical_lift(row, context) for row in logical)
        logical_polys[seam] = C870.fswap_polynomial(logical)
        packet_sites[seam] = resource_bank(placement)
        endpoint_modes[seam] = {(cell, left_mode), (target, right_mode)}

    scheduled = schedule_order(seams)
    position = {seam: index for index, seam in enumerate(scheduled)}
    inversions = tuple(
        (left, right)
        for index, left in enumerate(seams) for right in seams[index + 1 :]
        if position[left] > position[right]
    )
    coarse_pairs = tuple(
        (left, right)
        for index, left in enumerate(seams) for right in seams[index + 1 :]
        if coarse_color(left) == coarse_color(right)
    )
    commute_failures = Counter()
    maximum_poly_residual = 0.0
    for left, right in coarse_pairs:
        commute_failures["endpoint_overlap"] += bool(endpoint_modes[left] & endpoint_modes[right])
        commute_failures["packet_overlap"] += bool(packet_sites[left] & packet_sites[right])
        commute_failures["physical_anticommutators"] += sum(
            not a.commutes(b) for a in physical_rows[left] for b in physical_rows[right]
        )
        residual = C870.poly_residual(
            C870.poly_mul(logical_polys[left], logical_polys[right]),
            C870.poly_mul(logical_polys[right], logical_polys[left]),
        )
        maximum_poly_residual = max(maximum_poly_residual, residual)
        commute_failures["polynomial"] += residual > C871.TOL
    commute_failures["inversion_outside_class"] = sum(
        coarse_color(left) != coarse_color(right) for left, right in inversions
    )

    grouped = defaultdict(list)
    for seam in seams:
        grouped[color(seam)].append(seam)
    padding = same_layer_pairs = same_layer_collisions = footprint_collisions = 0
    fixed_depth = 0
    for members in grouped.values():
        depth = max(len(routes[seam]) for seam in members)
        fixed_depth += depth
        padded = {
            seam: routes[seam] + (None,) * (depth - len(routes[seam]))
            for seam in members
        }
        padding += sum(depth - len(routes[seam]) for seam in members)
        for index, left in enumerate(members):
            footprint_collisions += sum(
                bool(footprints[left] & footprints[right]) for right in members[:index]
            )
        for layer in range(depth):
            active = [padded[seam][layer] for seam in members if padded[seam][layer] is not None]
            for index, gate in enumerate(active):
                for prior in active[:index]:
                    same_layer_pairs += 1
                    same_layer_collisions += bool(set(gate[1]) & set(prior[1]))

    bank_at = {}
    for bank_index, bank in enumerate(resource_banks):
        for site in bank:
            bank_at[site] = bank_index
    dirty = Counter()
    macro_bank_pairs = set()
    for macro_index, (seam, placement, word) in enumerate(zip(seams, placements, words)):
        for instruction in word:
            if len(instruction.sites) != 2:
                continue
            path = C871.coframe_path(*instruction.sites, placement.basis)
            labels = list(range(len(path)))
            for index in range(len(path) - 2):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            dirty["operand_failures"] += labels[-2:] != [0, len(path) - 1]
            for index in reversed(range(len(path) - 2)):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            dirty["path_return_failures"] += labels != list(range(len(path)))
            for path_index, site in enumerate(path):
                other = bank_at.get(site)
                if other is None or other == macro_index:
                    continue
                macro_bank_pairs.add((macro_index, other))
                dirty["site_incidences"] += 1
                dirty["endpoint_alias_failures"] += path_index in (0, len(path) - 1)
                dirty["same_color_failures"] += color(seam) == color(seams[other])
                dirty["label_return_failures"] += labels[path_index] != path_index
                dirty["dirty_basis_rows"] += 2
                dirty["dirty_basis_failures"] += 2 * (labels[path_index] != path_index)

    naive_pairs = fine_pairs = 0
    for index, left in enumerate(seams):
        for right in seams[:index]:
            if coarse_color(left) == coarse_color(right):
                naive_pairs += bool(footprints[left] & footprints[right])
            if color(left) == color(right):
                fine_pairs += bool(footprints[left] & footprints[right])

    tags = tuple(factor[0] for factor, _rows in factors)
    first_seam = tags.index("seam")
    last_seam = len(tags) - 1 - tuple(reversed(tags)).index("seam")
    expected_phase = -math.pi * len(seams) / 2
    return {
        "length": length,
        "cells": len(graph.cells),
        "seams": len(seams),
        "actual_update_rotations": len(rotations),
        "actual_factor_macros": len(factors),
        "actual_seam_factors": len(actual_seams),
        "actual_seam_rotations": sum(len(rows) for _factor, rows in actual_seams),
        "augmented_instructions": sum(map(len, words)),
        "augmented_instruction_range": (min(map(len, words)), max(map(len, words))),
        "used_packet_M2_per_seam": C714.N,
        "retained_spatial_current_M2_per_seam": 1,
        "total_resource_M2_per_seam": C714.N + 1,
        "packet_bank_radius": max(placement.radius for placement in placements),
        "total_resource_radius": max(
            max(placement.radius for placement in placements),
            max(map(abs, SPATIAL_CURRENT_LOCAL)),
        ),
        "used_packet_union_M2": len(used_packet_union),
        "used_resource_union_M2": len(used_resource_union),
        "packet_bank_pair_overlap_pairs": packet_pair_overlaps,
        "resource_bank_pair_overlap_pairs": resource_pair_overlaps,
        "spatial_output_local_coordinate": SPATIAL_CURRENT_LOCAL,
        "spatial_output_geometry_failures": spatial_geometry,
        "route_policy": (
            "declared coframe-returned replacement for the augmented seam stage; "
            "landed Manhattan route retained outside that stage"
        ),
        "retained_seam_route_reconciliation": dict(route_reconciliation),
        "binding_failures": dict(binding_failures),
        "commuting_transpositions": len(inversions),
        "certified_coarse_macro_pairs": len(coarse_pairs),
        "commutation_failures": dict(commute_failures),
        "maximum_polynomial_commutator_residual": maximum_poly_residual,
        "active_colors": len(grouped),
        "lockstep_schedule_key": (
            "nested coarse=(axis,owner[axis] mod 2), then fine=owner parities "
            "on remaining axes in ascending global-axis order"
        ),
        "emitted_physical_stream_order": "exact Cycle870 serial factor order",
        "identity_padding_slots": padding,
        "same_layer_gate_pairs": same_layer_pairs,
        "same_layer_support_collisions": same_layer_collisions,
        "same_color_footprint_collisions": footprint_collisions,
        "fixed_color_schedule_routed_depth": fixed_depth,
        "first_forward_swap_deletion_detections": deletions,
        "dirty_spectator": {
            **dict(dirty),
            "ordered_macro_bank_pairs": len(macro_bank_pairs),
        },
        "coarse_six_color_collision_control": naive_pairs,
        "fine_24_color_collision_count": fine_pairs,
        "seam_stage_contiguity_failure": any(
            tag != "seam" for tag in tags[first_seam:last_seam + 1]
        ),
        "stage_order_failure": (
            any(tag == "contact" for tag in tags[:first_seam])
            or any(tag in ("coin", "reverse") for tag in tags[last_seam + 1 :])
        ),
        "expected_seam_phase": expected_phase,
        "observed_seam_phase": inventory["compiled_relative_phase_breakdown"]["seam_FSWAP"],
        "seam_phase_failure": abs(
            inventory["compiled_relative_phase_breakdown"]["seam_FSWAP"] - expected_phase
        ) > C871.TOL,
        "full_update_relative_phase_unchanged": inventory[
            "compiled_relative_to_target_global_phase_angle"
        ],
    }


def held_schedule_fixture(length: int):
    """Held geometry/schedule stress for the declared coframe replacement."""
    graph = C870.prep.OpenReferenceGraph(cells(length))
    context = C870.physical_context(graph)
    seams = C870.graph_seams(graph)
    placements = tuple(C871.packet_placement(graph, context, seam) for seam in seams)
    spatial_sites = tuple(spatial_current_site(placement) for placement in placements)
    resource_banks = tuple(resource_bank(placement) for placement in placements)
    blocked = set(context.sites) | J870.auxiliary_registers(graph)
    words = tuple(
        flatten(candidate_segments(graph, context, seam, placement))
        for seam, placement in zip(seams, placements)
    )
    footprints = {
        seam: footprint(word, placement.basis)
        for seam, word, placement in zip(seams, words, placements)
    }
    routed_depth = {}
    for seam, word, placement in zip(seams, words, placements):
        depth = 0
        for instruction in word:
            if len(instruction.sites) == 1:
                depth += 1
            else:
                path = C871.coframe_path(*instruction.sites, placement.basis)
                depth += 2 * len(path) - 3
        routed_depth[seam] = depth
    grouped = defaultdict(list)
    for seam in seams:
        grouped[color(seam)].append(seam)
    fine_pairs = fine_collisions = 0
    for members in grouped.values():
        for index, left in enumerate(members):
            for right in members[:index]:
                fine_pairs += 1
                fine_collisions += bool(footprints[left] & footprints[right])
    coarse_collisions = sum(
        bool(footprints[left] & footprints[right])
        for index, left in enumerate(seams) for right in seams[:index]
        if coarse_color(left) == coarse_color(right)
    )
    packet_pair_overlaps = sum(
        bool(set(left.sites) & set(right.sites))
        for index, left in enumerate(placements) for right in placements[:index]
    )
    resource_pair_overlaps = sum(
        bool(left & right)
        for index, left in enumerate(resource_banks) for right in resource_banks[:index]
    )
    offset_min = [math.inf] * 3
    offset_max = [-math.inf] * 3
    for seam, placement in zip(seams, placements):
        for site in footprints[seam]:
            for axis in range(3):
                offset_min[axis] = min(offset_min[axis], site[axis] - placement.midpoint[axis])
                offset_max[axis] = max(offset_max[axis], site[axis] - placement.midpoint[axis])
    return {
        "length": length,
        "cells": len(graph.cells),
        "seams": len(seams),
        "used_packet_M2_per_seam": C714.N,
        "retained_spatial_current_M2_per_seam": 1,
        "total_resource_M2_per_seam": C714.N + 1,
        "used_packet_union_M2": len(set().union(*(set(row.sites) for row in placements))),
        "used_resource_union_M2": len(set().union(*resource_banks)),
        "packet_bank_pair_overlap_pairs": packet_pair_overlaps,
        "resource_bank_pair_overlap_pairs": resource_pair_overlaps,
        "spatial_output_local_coordinate": SPATIAL_CURRENT_LOCAL,
        "spatial_output_geometry_failures": {
            "duplicate_output_sites": len(spatial_sites) - len(set(spatial_sites)),
            "packet_aliases": sum(
                site in set().union(*(set(row.sites) for row in placements))
                for site in spatial_sites
            ),
            "native_aux_collisions": sum(site in blocked for site in spatial_sites),
        },
        "active_colors": len(grouped),
        "lockstep_schedule_key": (
            "nested coarse=(axis,owner[axis] mod 2), then fine=owner parities "
            "on remaining axes in ascending global-axis order"
        ),
        "same_color_macro_pairs": fine_pairs,
        "same_color_footprint_support_collisions": fine_collisions,
        "coarse_six_color_collision_control": coarse_collisions,
        "fixed_color_schedule_routed_depth": sum(
            max(routed_depth[seam] for seam in members) for members in grouped.values()
        ),
        "macro_routed_depth_range": (
            min(routed_depth.values()), max(routed_depth.values())
        ),
        "footprint_offset_min": offset_min,
        "footprint_offset_max": offset_max,
        "route_policy": "declared coframe-returned replacement",
    }


def semantic_direction_certificate():
    rows = tuple(product((0, 1), repeat=12))
    counts = Counter()
    failures = Counter()
    lawful_pairs = set()
    for pointer, binder, actuality, admissibility, law, fresh, causal in product(
        (0, 1), repeat=7
    ):
        controls = (pointer, binder, actuality, admissibility, law, fresh)
        after = C714.apply_semantic(
            C714.initial(9, 12, causal, controls), C714.word()
        )
        expected = (
            pointer & binder & actuality & admissibility & law & fresh & causal
        )
        counts["exact_packet_equation_rows"] += 1
        failures["exact_packet_equation"] += after[C714.PORIENT] != expected
        failures["exact_packet_ORIENT_return"] += after[C714.ORIENT] != causal
    for axis in range(3):
        left, right = 2 * axis + 1, 6 + 2 * axis
        for source in rows:
            target, _phase = C704.GAUSS.target_fswap_action(source, left, right)
            pre_left, pre_right = source[left], source[right]
            post_left, post_right = target[left], target[right]
            pointer = pre_left ^ pre_right
            u_to_v = pointer & post_right
            v_to_u = pointer & post_left
            wrong = pointer & post_left
            du = pre_left ^ post_left
            dv = pre_right ^ post_right
            failures["pointer"] += pointer != (du | dv)
            failures["one_hot"] += (u_to_v ^ v_to_u) != pointer or u_to_v + v_to_u > 1
            failures["scratch"] += (du ^ post_left ^ post_right) != 0
            failures["scratch"] += (dv ^ post_left ^ post_right) != 0
            failures["current_decode"] += (
                2 * u_to_v - pointer != u_to_v - v_to_u
                or u_to_v - v_to_u != post_right - pre_right
            )
            for causal in (0, 1):
                counts["rows"] += 1
                counts["moving"] += pointer
                counts["u_to_v"] += u_to_v
                counts["v_to_u"] += v_to_u
                counts["wrong_side_detected"] += pointer and wrong != u_to_v
                # Deleting the seam makes post=pre, hence du=dv=pointer=0
                # in the actual comparator grammar and spatial output zero.
                counts["seam_deletion_detected"] += (
                    (0, 0) != (pointer, u_to_v)
                )
                lawful_pairs.add((u_to_v, causal))

                # The added M2 site begins blank and retains the spatial bit.
                spatial_before = 0
                spatial_after = spatial_before ^ (pointer & post_right)
                failures["spatial_output"] += spatial_after != u_to_v
                counts["dirty_spatial_input_detected"] += (
                    (1 ^ (pointer & post_right)) != u_to_v
                )

                # Cycle714 ORIENT is a supplied causal coordinate.  The packet
                # emits its enabled causal projection and returns ORIENT.
                enabled_controls = (pointer, 1, 1, 1, 1, 1)
                before = C714.initial(9, 12, causal, enabled_controls)
                after = C714.apply_semantic(before, C714.word())
                failures["causal_packet_projection"] += (
                    after[C714.PORIENT] != pointer & causal
                )
                failures["causal_ORIENT_return"] += after[C714.ORIENT] != causal
                failures["work_return"] += any(
                    after[index] for index in C714.MCX_WORK + C714.ENABLE_WORK
                )

                # Mutation: XOR the spatial result into the supplied causal
                # ORIENT, reproducing the forbidden overloaded construction.
                damaged = C714.initial(
                    9, 12, causal ^ u_to_v, (pointer, 1, 1, 1, 1, 1)
                )
                damaged_after = C714.apply_semantic(damaged, C714.word())
                counts["ORIENT_overload_detected"] += (
                    damaged_after[C714.PORIENT] != pointer & causal
                )

    initial = C714.initial(9, 12, 1, (1, 1, 1, 1, 1, 1))
    first = C714.apply_semantic(initial, C714.word())
    reused = C714.apply_semantic(first, C714.word())
    reuse_difference = sum(a != b for a, b in zip(first, reused))
    return {
        **dict(counts),
        "failure_census": dict(failures),
        "packet_reuse_without_reset_changed_bits": reuse_difference,
        "packet_reuse_without_reset_detected": reuse_difference > 0,
        "spatial_causal_pairs": tuple(sorted(lawful_pairs)),
        "spatial_current_decode": "j_e = 2*r_u_to_v - pointer = r_u_to_v-r_v_to_u",
        "spatial_output_register": "one separate retained M2 per seam",
        "exact_packet_equation": (
            "PORIENT = POINTER AND BINDER AND ACTUAL AND ADMISS AND LAW AND FRESH AND ORIENT"
        ),
        "enabled_domain_simplification": (
            "with BINDER=ACTUAL=ADMISS=LAW=FRESH=1 only, PORIENT=POINTER AND ORIENT"
        ),
        "output_type": "spatial direction / unit-weight number-resource current",
        "causal_orientation": (
            "supplied and retained in ORIENT; PORIENT carries the fully enabled projection"
        ),
    }


def continuity_certificate():
    graph = C870.prep.OpenReferenceGraph(cells(2))
    seams = C870.graph_seams(graph)
    cell_rows = graph.cells
    cell_index = {cell: index for index, cell in enumerate(cell_rows)}
    endpoint_index = {}
    endpoint_cell = []
    for seam in seams:
        for key in ((seam[0], seam[3]), (seam[2], seam[4])):
            if key not in endpoint_index:
                endpoint_index[key] = len(endpoint_index)
                endpoint_cell.append(cell_index[key[0]])

    failures = Counter()
    patterns = 0
    for currents in product((-1, 0, 1), repeat=len(seams)):
        occupation = [0] * len(endpoint_index)
        for seam, current in zip(seams, currents):
            u = endpoint_index[(seam[0], seam[3])]
            v = endpoint_index[(seam[2], seam[4])]
            if current > 0:
                occupation[u] = 1
            elif current < 0:
                occupation[v] = 1
        before = [0] * len(cell_rows)
        for endpoint, bit in enumerate(occupation):
            before[endpoint_cell[endpoint]] += bit
        observed_current = []
        for seam in seams:
            u = endpoint_index[(seam[0], seam[3])]
            v = endpoint_index[(seam[2], seam[4])]
            pre_v = occupation[v]
            occupation[u], occupation[v] = occupation[v], occupation[u]
            observed_current.append(occupation[v] - pre_v)
        after = [0] * len(cell_rows)
        for endpoint, bit in enumerate(occupation):
            after[endpoint_cell[endpoint]] += bit
        divergence = [0] * len(cell_rows)
        for seam, current in zip(seams, observed_current):
            divergence[cell_index[seam[0]]] -= current
            divergence[cell_index[seam[2]]] += current
        failures["current_pattern"] += tuple(observed_current) != currents
        failures["cell_continuity"] += any(
            after[index] - before[index] != divergence[index]
            for index in range(len(cell_rows))
        )
        failures["global_number"] += sum(after) != sum(before)
        patterns += 1

    # Both stationary endpoint columns project to j=0 and zero occupation delta.
    stationary_rows = (((0, 0), (0, 0)), ((1, 1), (1, 1)))
    stationary_failures = sum(
        (post_v - pre_v) != 0 or (sum(post) - sum(pre)) != 0
        for pre, post in stationary_rows for pre_v, post_v in ((pre[1], post[1]),)
    )

    frames = C871.proper_frames()
    frame_rows = frame_failures = 0
    product_rows = product_failures = 0
    for seam in seams:
        owner, axis, target = seam[0], seam[1], seam[2]
        for frame in frames:
            target_axis, sign = C871.signed_axis(frame, axis)
            moved_owner = C871.matvec(frame, owner)
            moved_target = C871.matvec(frame, target)
            canonical_owner, canonical_target = (
                (moved_owner, moved_target) if sign > 0
                else (moved_target, moved_owner)
            )
            for current in (-1, 0, 1):
                transformed = sign * current
                observed = {
                    moved_owner: -current,
                    moved_target: current,
                }
                expected = {
                    canonical_owner: -transformed,
                    canonical_target: transformed,
                }
                frame_rows += 1
                frame_failures += observed != expected or target_axis not in range(3)
        for left in frames:
            for right in frames:
                intermediate_axis, sign_right = C871.signed_axis(right, axis)
                _final_axis, sign_left = C871.signed_axis(left, intermediate_axis)
                _product_axis, sign_product = C871.signed_axis(left @ right, axis)
                for current in (-1, 0, 1):
                    product_rows += 1
                    product_failures += sign_left * sign_right * current != sign_product * current
    return {
        "shape": (2, 2, 2),
        "seams": len(seams),
        "endpoint_modes": len(endpoint_index),
        "current_patterns": patterns,
        "covered_full_occupation_columns": 4 ** len(seams),
        "stationary_equivalence_rows": len(stationary_rows),
        "stationary_equivalence_failures": stationary_failures,
        "failure_census": dict(failures),
        "proper_frames": len(frames),
        "frame_rows": frame_rows,
        "frame_failures": frame_failures,
        "ordered_frame_products": len(frames) ** 2,
        "product_rows": product_rows,
        "product_failures": product_failures,
        "identity": "Delta N_x = sum_in j_e - sum_out j_e",
        "current": "j_e = n_v_post - n_v_pre = r_u_to_v - r_v_to_u",
        "type": "unit-weight conserved number/resource current",
        "not_claimed": (
            "energy", "mass", "source density", "occurrence", "gravity"
        ),
        "coupling_and_scale": "supplied",
    }


def color_covariance_certificate():
    def encode(axis, owner):
        return (
            axis, owner[axis] & 1,
            *(owner[index] & 1 for index in range(3) if index != axis),
        )

    def decode(row):
        axis, axial, *remaining = row
        iterator = iter(remaining)
        owner = tuple(axial if index == axis else next(iterator) for index in range(3))
        return axis, owner

    colors = tuple(
        encode(axis, owner)
        for axis in range(3) for owner in product((0, 1), repeat=3)
    )
    frames = C871.proper_frames()

    def action(row, frame):
        axis, owner = decode(row)
        target_axis, sign = C871.signed_axis(frame, axis)
        moved = C871.matvec(frame, owner)
        if sign < 0:
            moved = C871.add(moved, C871.matvec(frame, C871.unit(axis)))
        return encode(target_axis, moved)

    bijection_failures = 0
    for frame in frames:
        bijection_failures += len({action(row, frame) for row in colors}) != len(colors)
    product_failures = 0
    for left in frames:
        for right in frames:
            product_failures += sum(
                action(action(row, right), left) != action(row, left @ right)
                for row in colors
            )
    return {
        "colors": len(colors),
        "proper_frames": len(frames),
        "bijection_failures": bijection_failures,
        "ordered_frame_products": len(frames) ** 2,
        "product_rows": len(colors) * len(frames) ** 2,
        "product_failures": product_failures,
    }


def used_epoch_passive_covariance():
    """Passive representation law for the used 59+1-site words/routes."""
    graph = C870.prep.OpenReferenceGraph(cells(2))
    context = C870.physical_context(graph)
    seams = C870.graph_seams(graph)
    representatives = tuple(next(seam for seam in seams if seam[1] == axis) for axis in range(3))
    frames = C871.proper_frames()
    counts = Counter()
    for seam in representatives:
        placement = C871.packet_placement(graph, context, seam)
        word = flatten(candidate_segments(graph, context, seam, placement))
        signatures = tuple(sorted(
            set(map(C871.instruction_signature, word)), key=repr
        ))
        paths = tuple(sorted(set(
            C871.coframe_path(*instruction.sites, placement.basis)
            for instruction in word if len(instruction.sites) == 2
        ), key=repr))
        for frame in frames:
            moved_basis = tuple(C871.matvec(frame, row) for row in placement.basis)
            for path in paths:
                observed = C871.coframe_path(
                    C871.matvec(frame, path[0]), C871.matvec(frame, path[-1]), moved_basis
                )
                counts["frame_path_rows"] += 1
                counts["frame_path_failures"] += observed != C871.transform_path(path, frame)
        for left in frames:
            for right in frames:
                composed = left @ right
                for signature in signatures:
                    counts["signature_product_rows"] += 1
                    counts["signature_product_failures"] += (
                        C871.transform_signature(
                            C871.transform_signature(signature, right), left
                        ) != C871.transform_signature(signature, composed)
                    )
                for path in paths:
                    counts["path_product_rows"] += 1
                    counts["path_product_failures"] += (
                        C871.transform_path(C871.transform_path(path, right), left)
                        != C871.transform_path(path, composed)
                    )
    return {
        "used_packet_M2_per_seam": C714.N,
        "retained_spatial_current_M2_per_seam": 1,
        "total_resource_M2_per_seam": C714.N + 1,
        "representative_axes": 3,
        "proper_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        **dict(counts),
        "scope": (
            "passive coordinate/program/declared-coframe-route representation; "
            "not active covariance of the single-rail allocator"
        ),
    }


def c4_orbits(available):
    def rotate(row):
        a, b, c = row
        return a, -c, b
    seen = set()
    output = []
    for row in sorted(available):
        if row in seen:
            continue
        orbit = []
        current = row
        for _ in range(4):
            orbit.append(current)
            current = rotate(current)
        orbit = frozenset(orbit)
        seen.update(orbit)
        if len(orbit) == 4 and orbit <= available:
            output.append(orbit)
    return tuple(sorted(output, key=lambda row: repr(sorted(row))))


def reflected(orbit):
    return frozenset((-a, b, -c) for a, b, c in orbit)


def orbit_inventory(graph, context, seam):
    midpoint = C871.seam_midpoint(seam[0], seam[1])
    basis = C871.local_coframe(seam[1])
    blocked = set(context.sites) | J870.auxiliary_registers(graph)
    def physical(local):
        site = midpoint
        for coefficient, direction in zip(local, basis):
            site = C871.add(site, C871.scale(coefficient, direction))
        return site
    available = {
        local for local in product(range(-3, 4), repeat=3)
        if physical(local) not in blocked
    }
    return c4_orbits(available), physical


def four_rail_allocator_certificate():
    graph = C870.prep.OpenReferenceGraph(cells(2))
    context = C870.physical_context(graph)
    all_orbits, _physical = orbit_inventory(graph, context, C870.graph_seams(graph)[0])
    orbit_set = set(all_orbits)
    fixed = tuple(sorted(
        (orbit for orbit in all_orbits if reflected(orbit) == orbit),
        key=lambda row: repr(sorted(row)),
    ))
    pairs = []
    seen = set(fixed)
    for orbit in all_orbits:
        if orbit in seen:
            continue
        partner = reflected(orbit)
        if partner not in orbit_set:
            raise AssertionError("missing reflection partner")
        pair = tuple(sorted((orbit, partner), key=lambda row: repr(sorted(row))))
        pairs.append(pair)
        seen.update(pair)
    pairs.sort(key=repr)
    selected = tuple(fixed[:5]) + tuple(orbit for pair in pairs[:27] for orbit in pair)
    selected_set = set(selected)
    sites = frozenset(site for orbit in selected for site in orbit)
    frames = C871.proper_frames()

    def local_transform(axis, frame):
        target_axis, _sign = C871.signed_axis(frame, axis)
        source_basis = np.column_stack(C871.local_coframe(axis))
        target_basis = np.column_stack(C871.local_coframe(target_axis))
        return target_axis, np.asarray(target_basis.T @ frame @ source_basis, dtype=int)

    counts = Counter()
    identity_register_failures = 0
    half_action_failures = 0
    for axis in range(3):
        for frame in frames:
            _target_axis, matrix = local_transform(axis, frame)
            moved_orbits = tuple(
                frozenset(tuple(map(int, matrix @ np.asarray(site))) for site in orbit)
                for orbit in selected
            )
            counts["frame_site_rows"] += len(sites)
            counts["frame_orbit_rows"] += len(selected)
            counts["site_set_failures"] += frozenset(
                tuple(map(int, matrix @ np.asarray(site))) for site in sites
            ) != sites
            counts["orbit_membership_failures"] += sum(
                orbit not in selected_set for orbit in moved_orbits
            )
            counts["orbit_bijection_failures"] += len(set(moved_orbits)) != len(selected)
            identity_register_failures += sum(
                moved != original for moved, original in zip(moved_orbits, selected)
            )
            _moved_axis, sign = C871.signed_axis(frame, axis)
            if sign < 0:
                # Damage: keep only the axial C4 half-action and suppress the
                # reflection of the axial local coordinate.
                damaged = np.array(matrix, copy=True)
                damaged[0, :] *= -1
                half_action_failures += frozenset(
                    tuple(map(int, damaged @ np.asarray(site))) for site in sites
                ) != sites
        for left in frames:
            for right in frames:
                intermediate, right_matrix = local_transform(axis, right)
                final_axis, left_matrix = local_transform(intermediate, left)
                product_axis, product_matrix = local_transform(axis, left @ right)
                counts["products"] += 1
                counts["axis_product_failures"] += final_axis != product_axis
                counts["matrix_product_failures"] += not np.array_equal(
                    left_matrix @ right_matrix, product_matrix
                )
                for site in sites:
                    row = np.asarray(site)
                    counts["site_product_rows"] += 1
                    counts["site_product_failures"] += not np.array_equal(
                        left_matrix @ (right_matrix @ row), product_matrix @ row
                    )
                for orbit in selected:
                    twice = frozenset(
                        tuple(map(int, left_matrix @ (right_matrix @ np.asarray(site))))
                        for site in orbit
                    )
                    direct = frozenset(
                        tuple(map(int, product_matrix @ np.asarray(site))) for site in orbit
                    )
                    counts["orbit_product_rows"] += 1
                    counts["orbit_product_failures"] += twice != direct

    geometry = []
    reference_inventory = set(all_orbits)
    for length in (2, 3, 4, 5):
        local_graph = C870.prep.OpenReferenceGraph(cells(length))
        local_context = C870.physical_context(local_graph)
        blocked = set(local_context.sites) | J870.auxiliary_registers(local_graph)
        banks = []
        inventory_failures = 0
        for seam in C870.graph_seams(local_graph):
            inventory, physical = orbit_inventory(local_graph, local_context, seam)
            inventory_failures += set(inventory) != reference_inventory
            banks.append({physical(site) for orbit in selected for site in orbit})
        geometry.append({
            "length": length,
            "seams": len(banks),
            "M2_union": len(set().union(*banks)),
            "inventory_failures": inventory_failures,
            "native_aux_collisions": sum(len(bank & blocked) for bank in banks),
            "cross_seam_overlap_pairs": sum(
                bool(left & right)
                for index, left in enumerate(banks) for right in banks[:index]
            ),
        })
    return {
        "status": "separate geometric covariance candidate",
        "used_by_executable_epoch": False,
        "available_C4_orbits": len(all_orbits),
        "reflection_fixed_orbits": len(fixed),
        "reflection_paired_orbit_pairs": len(pairs),
        "selected_fixed_orbits": 5,
        "selected_reflected_pairs": 27,
        "register_orbits": len(selected),
        "rails_per_register": 4,
        "M2_per_seam": len(sites),
        **dict(counts),
        "geometry": geometry,
        "half_action_deletion_detections": half_action_failures,
        "register_permutation_deletion_detections": identity_register_failures,
        "missing_for_execution": (
            "a transported four-rail Cycle714 word implementing the induced register/rail permutation"
        ),
    }


def noncommuting_stage_reorder_control():
    graph = C870.prep.OpenReferenceGraph(cells(2))
    rotations, _inventory = C870.build_update(graph, C871.coin_schedule())
    factors = tuple(
        (factor, tuple(group))
        for factor, group in groupby(rotations, key=lambda row: row.factor)
    )
    seams = tuple(rows for factor, rows in factors if factor[0] == "seam")
    contacts = tuple(rows for factor, rows in factors if factor[0] == "contact")

    def polynomial(rows):
        output = {C870.Pauli(): 1.0 + 0.0j}
        for rotation in rows:
            output = C870.poly_mul(
                C870.rotation_polynomial(rotation.row, rotation.angle), output
            )
        return output

    best = 0.0
    witness = None
    for seam_index, seam_rows in enumerate(seams):
        left = polynomial(seam_rows)
        for contact_index, contact_rows in enumerate(contacts):
            if not any(
                not a.row.commutes(b.row) for a in seam_rows for b in contact_rows
            ):
                continue
            right = polynomial(contact_rows)
            residual = C870.poly_residual(
                C870.poly_mul(left, right), C870.poly_mul(right, left)
            )
            if residual > best:
                best = residual
                witness = (seam_index, contact_index)
    return {
        "mutation": "move a seam factor across a noncommuting contact factor",
        "witness": witness,
        "commutator_residual": best,
        "detected": best > 1.0e-3,
    }


def association_firewall():
    C610 = C704.C610
    pairs = []
    failures = 0
    for spatial in (0, 1):
        for causal in (-1, 1):
            packet = C704.ReversiblePacketBank(bank=1)
            chain = C610.EventChain(bank=1)
            left = packet.append(
                0, 66, 1, causal, binder=1,
                actuality=1, admissibility=1, law_domain=1,
            )
            right = chain.admit(
                0, causal, certificate=1, binder=1,
                actuality=1, admissibility=1, law_domain=1,
            )
            failures += left != "admitted" or right != "admitted"
            pairs.append((spatial, causal))
    return {
        "lawful_pairs": pairs,
        "acceptance_failures": failures,
        "spatial_to_causal_is_function": False,
        "causal_orientation": "supplied",
        "Cycle612_shared_order_reads_orientation": False,
        "missing_map": (
            "absent from these pinned interfaces: identity co-registration from seam "
            "opportunity to signed tick crossing, followed by EventCell.orientation = "
            "tick-crossing orientation; no global nonexistence claim"
        ),
    }


def failure_list(report):
    failures = []
    provenance = report["provenance"]
    if provenance["missing_inputs"] or provenance["pin_failures"]:
        failures.append("source provenance")
    if provenance["theorem_note_pin_failure"]:
        failures.append("theorem note pin")
    stream = report["physical_epoch_stream"]
    if any(stream["construction_failure_census"].values()):
        failures.append("physical epoch stream")
    if stream["first_forward_swap_deletion_detections"] <= 0:
        failures.append("inactive physical-stream first-forward-SWAP deletion")
    mutations = report["physical_macro_mutations"]
    if mutations["NN_failures"]:
        failures.append("physical macro mutation NN")
    if mutations["wrong_side_digest_detections"] != mutations["seams"]:
        failures.append("inactive physical wrong-side mutation")
    if mutations["seam_deletion_digest_detections"] != mutations["seams"]:
        failures.append("inactive physical seam-deletion mutation")
    for fixture in report["epoch_fixtures"]:
        prefix = f"L{fixture['length']}"
        if fixture["packet_bank_pair_overlap_pairs"] or fixture[
            "resource_bank_pair_overlap_pairs"
        ]:
            failures.append(prefix + " resource overlap")
        if any(fixture["spatial_output_geometry_failures"].values()):
            failures.append(prefix + " spatial output geometry")
        if any(fixture["binding_failures"].values()):
            failures.append(prefix + " binding")
        if any(fixture["commutation_failures"].values()):
            failures.append(prefix + " commutation")
        for key in (
            "same_layer_support_collisions", "same_color_footprint_collisions",
            "fine_24_color_collision_count", "seam_stage_contiguity_failure",
            "stage_order_failure", "seam_phase_failure",
        ):
            if fixture[key]:
                failures.append(prefix + " " + key)
        dirty = fixture["dirty_spectator"]
        if any(dirty.get(key, 0) for key in (
            "operand_failures", "path_return_failures", "endpoint_alias_failures",
            "same_color_failures", "label_return_failures", "dirty_basis_failures",
        )):
            failures.append(prefix + " dirty spectator")
        if fixture["coarse_six_color_collision_control"] <= 0:
            failures.append(prefix + " inactive six-color control")
        if fixture["first_forward_swap_deletion_detections"] <= 0:
            failures.append(prefix + " inactive first-forward-SWAP deletion")
        reconciliation = fixture["retained_seam_route_reconciliation"]
        if any(reconciliation.get(key, 0) for key in (
            "endpoint_failures", "replacement_operand_failures", "landed_operand_failures",
            "replacement_return_failures", "landed_return_failures",
        )):
            failures.append(prefix + " route reconciliation")
    for fixture in report["held_schedule_fixtures"]:
        prefix = f"held-L{fixture['length']}"
        if fixture["packet_bank_pair_overlap_pairs"] or fixture[
            "resource_bank_pair_overlap_pairs"
        ]:
            failures.append(prefix + " resource overlap")
        if any(fixture["spatial_output_geometry_failures"].values()):
            failures.append(prefix + " spatial output geometry")
        if fixture["same_color_footprint_support_collisions"]:
            failures.append(prefix + " support collision")
        if fixture["coarse_six_color_collision_control"] <= 0:
            failures.append(prefix + " inactive six-color control")
    direction = report["spatial_direction"]
    if any(direction["failure_census"].values()):
        failures.append("spatial direction")
    for key in (
        "wrong_side_detected", "seam_deletion_detected",
        "dirty_spatial_input_detected", "ORIENT_overload_detected",
    ):
        if direction.get(key, 0) <= 0:
            failures.append("inactive " + key)
    if len(direction["spatial_causal_pairs"]) != 4:
        failures.append("spatial/causal independence")
    if not direction["packet_reuse_without_reset_detected"]:
        failures.append("inactive packet reuse")
    continuity = report["continuity"]
    if any(continuity["failure_census"].values()) or any((
        continuity["stationary_equivalence_failures"], continuity["frame_failures"],
        continuity["product_failures"],
    )):
        failures.append("continuity")
    covariance = report["color_covariance"]
    if covariance["bijection_failures"] or covariance["product_failures"]:
        failures.append("color covariance")
    passive = report["used_epoch_passive_covariance"]
    if passive.get("frame_path_failures", 0) or passive.get(
        "signature_product_failures", 0
    ) or passive.get("path_product_failures", 0):
        failures.append("used-epoch passive covariance")
    allocator = report["four_rail_allocator_candidate"]
    for key in (
        "site_set_failures", "orbit_membership_failures", "orbit_bijection_failures",
        "axis_product_failures", "matrix_product_failures", "site_product_failures",
        "orbit_product_failures",
    ):
        if allocator.get(key, 0):
            failures.append("allocator " + key)
    if any(
        row[key]
        for row in allocator["geometry"]
        for key in ("inventory_failures", "native_aux_collisions", "cross_seam_overlap_pairs")
    ):
        failures.append("allocator geometry")
    if allocator["half_action_deletion_detections"] <= 0:
        failures.append("inactive allocator half-action")
    if allocator["register_permutation_deletion_detections"] <= 0:
        failures.append("inactive allocator permutation")
    if not report["noncommuting_stage_reorder_control"]["detected"]:
        failures.append("inactive stage reorder")
    if report["association_firewall"]["acceptance_failures"]:
        failures.append("orientation acceptance")
    mass = report["mass_contact"]
    if not mass["mass_fixture_pass"] or not mass["contact_fixture_pass"]:
        failures.append("mass/contact")
    return failures


def build_report(stream_output: Path | None = None):
    inherited = C871.inherited_matter_certificate()
    physical_stream = build_physical_epoch_stream(2)
    if stream_output is not None:
        stream_output.parent.mkdir(parents=True, exist_ok=True)
        stream_output.write_bytes(canonical_json_bytes(
            physical_stream_payload(physical_stream)
        ))
    report = {
        "schema": "cycle872-all-seam-spatial-packet-epoch-v1",
        "status": "pending",
        "claim_scope": (
            "one complete all-seam spatial-direction packet epoch on supplied clean "
            "own-bank inputs"
        ),
        "provenance": provenance_certificate(),
        "supplied_structures": (
            "pinned Cycle870 graph/carriers/factor stream/coin/contact/non-seam route/phase representative",
            "declared coframe-returned replacement route for augmented seam-stage instructions",
            "one clean 59-wire own packet bank plus one blank retained spatial-current M2 per seam",
            "blank packet payload and work; head; rotor; fixed address",
            "binder; actuality; admissibility; law-domain; fresh controls",
            "causal orientation supplied and retained in Cycle714 ORIENT; PORIENT obeys the full seven-factor enabled projection equation",
            "separate candidate D4-closed four-rail orbit subset and register/rail representation",
            "one declared update-epoch boundary",
        ),
        "physical_epoch_stream": physical_stream_certificate(physical_stream),
        "physical_macro_mutations": physical_macro_mutation_certificate(),
        "epoch_fixtures": [epoch_fixture(length) for length in (2, 3)],
        "held_schedule_fixtures": [held_schedule_fixture(length) for length in (4, 5)],
        "spatial_direction": semantic_direction_certificate(),
        "continuity": continuity_certificate(),
        "color_covariance": color_covariance_certificate(),
        "used_epoch_passive_covariance": used_epoch_passive_covariance(),
        "four_rail_allocator_candidate": four_rail_allocator_certificate(),
        "noncommuting_stage_reorder_control": noncommuting_stage_reorder_control(),
        "association_firewall": association_firewall(),
        "mass_contact": {
            "scope": (
                "inherited unchanged Cycle870/Cycle871 factor fixtures and phase ledger; "
                "not a new integrated-epoch spectrum"
            ),
            "mass_fixture_pass": inherited["mass_fixture_pass"],
            "contact_fixture_pass": inherited["contact_fixture_pass"],
            "QR_off_diagonal_residual": inherited["QR"]["QR_off_diagonal_residual"],
            "QR_reconstruction_residual": inherited["QR"]["reconstruction_residual"],
            "coin_unitarity_residual": inherited["one_particle"]["coin_unitarity_residual"],
            "mass_difference": abs(
                inherited["one_particle"]["analytic_mass"]
                - inherited["one_particle"]["rest_mass"]
            ),
            "contact_residual": inherited["contact"]["maximum_residual_up_to_global_phase"],
        },
        "open_boundaries": (
            "causal orientation remains supplied and is not derived from spatial direction",
            "later-epoch fresh address/reset/renewal/genesis remains supplied or open",
            "four-rail allocator is a separate geometric candidate; no transported packet word claimed",
            "every coupling and physical scale for the unit-weight current remains supplied",
        ),
        "interpretation_firewall": (
            "not autonomous recurrence; colors/factors/padding/routes/addresses are not time, "
            "ticks, occurrences, Events, Records, Born histories, sources, or gravity; "
            "unit occupation current is not energy, mass, calibrated source density, or gravity"
        ),
    }
    report["failures"] = failure_list(report)
    report["status"] = "pass" if not report["failures"] else "fail"
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_RECEIPT)
    parser.add_argument(
        "--stream-output", type=Path,
        help="optional full deterministic L2 executable local-gate stream JSON",
    )
    args = parser.parse_args()
    report = build_report(args.stream_output)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True, default=float) + "\n",
        encoding="utf-8",
    )
    print("CYCLE872_ALL_SEAM_SPATIAL_PACKET_EPOCH_PASS" if report["status"] == "pass"
          else "CYCLE872_ALL_SEAM_SPATIAL_PACKET_EPOCH_FAIL")
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
