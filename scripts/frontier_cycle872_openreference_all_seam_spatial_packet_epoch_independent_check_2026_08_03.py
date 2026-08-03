#!/usr/bin/env python3
"""Independent Cycle 872 checker.

This file does not import the primary runner.  It reconstructs every macro
from the actual Cycle870 factor inventory and checks a compact independent
acceptance surface with alternative enumeration code.
"""

from __future__ import annotations

import argparse
import ast
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import groupby, product
import json
import math
import os
from pathlib import Path
import sys

import numpy as np


PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def discover_source_root():
    supplied = os.environ.get("CYCLE872_SOURCE_ROOT")
    candidates = [Path(supplied)] if supplied else []
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


PRIMARY_MODULE = "frontier_cycle872_openreference_all_seam_spatial_packet_epoch_2026_08_03"
NOTE = "docs/OPENREFERENCE_ALL_SEAM_SPATIAL_DIRECTION_PACKET_EPOCH_CYCLE872_BOUNDED_THEOREM_NOTE_2026-08-03.md"
DEFAULT_RECEIPT = PACKAGE_ROOT / "outputs/cycle872_openreference_all_seam_spatial_packet_epoch_independent_check_receipt_2026_08_03.json"
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
EXPECTED_FIXTURES = {
    2: {
        "cells": 8, "seams": 12, "rotations": 1392, "factors": 324,
        "instructions": 10920, "schedule_depth": 74912,
        "six_collisions": 12, "fine_collisions": 0,
        "packet_union": 708, "resource_union": 720,
        "route_differences": 540, "dirty_pairs": 46,
    },
    3: {
        "cells": 27, "seams": 54, "rotations": 4752, "factors": 1107,
        "instructions": 49644, "schedule_depth": 173040,
        "six_collisions": 72, "fine_collisions": 0,
        "packet_union": 3186, "resource_union": 3240,
        "route_differences": 2752, "dirty_pairs": 281,
    },
    4: {
        "cells": 64, "seams": 144, "schedule_depth": 184848,
        "six_collisions": 216, "fine_collisions": 0,
        "packet_union": 8496, "resource_union": 8640,
    },
    5: {
        "cells": 125, "seams": 300, "schedule_depth": 186816,
        "six_collisions": 480, "fine_collisions": 0,
        "packet_union": 17700, "resource_union": 18000,
    },
}
EXPECTED_PHYSICAL_STREAM = {
    "length": 2,
    "native_rotations": 1392,
    "native_factors": 324,
    "unrouted_bound_instructions": 26768,
    "physical_local_gates": 220920,
    "matrix_registry_entries": 77,
    "first_forward_swap_deletion_detections": 18440,
    "factor_manifest_sha256": "653f27706716823d46d8c9395aed8cd55ab4c1750bf8ee12285fcd85771b2878",
    "label_insensitive_instruction_binding_sha256": "c03fbd9503bcfda2cabb319f48ccb83d93db9b53f8c5aa7dd51859bdc1fff629",
    "normalized_physical_gate_sha256": "a178a1f221afd8fe8ad8aacac1cd61024f94c11eb5fe58eb75defa4d674e97b1",
    "matrix_registry_sha256": "e2f7cf72a9bb1288db9f3d89f4677d4f77625cc23c4f6790c22cb268cfebf091",
}
SPATIAL_CURRENT_LOCAL = (0, 0, 3)


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def cells(length):
    return tuple(product(range(length), repeat=3))


def fine(seam):
    owner, axis = seam[0], seam[1]
    return (
        axis, owner[axis] & 1,
        *(owner[index] & 1 for index in range(3) if index != axis),
    )


def coarse(seam):
    return seam[1], seam[0][seam[1]] & 1


def spatial_current_site(placement):
    site = placement.midpoint
    for coefficient, direction in zip(SPATIAL_CURRENT_LOCAL, placement.basis):
        site = tuple(
            site[index] + coefficient * direction[index] for index in range(3)
        )
    return site


def resource_bank(placement):
    return frozenset((*placement.sites, spatial_current_site(placement)))


def independent_import_certificate():
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imported = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.append(node.module)
    return {
        "imported_modules": tuple(sorted(imported)),
        "primary_imported": any(PRIMARY_MODULE in row for row in imported),
    }


def provenance():
    observed = {label: sha(SOURCE_ROOT / label) for label in EXPECTED_INPUT_SHA256}
    return {
        "input_sha256": observed,
        "literal_dependency_pin_count": len(EXPECTED_INPUT_SHA256),
        "dependency_surface": (
            "complete local Python import closure plus dynamically loaded Cycle870 "
            "placement and Cycle610/611 modules"
        ),
        "pin_failures": {
            label: (expected, observed[label])
            for label, expected in EXPECTED_INPUT_SHA256.items()
            if observed[label] != expected
        },
        "note_sha256": sha(PACKAGE_ROOT / NOTE),
        "note_pin_failure": sha(PACKAGE_ROOT / NOTE) != EXPECTED_NOTE_SHA256,
        "checker_sha256": sha(Path(__file__)),
    }


def independent_segments(
    graph, context, seam, placement, actual_rows, *, wrong_side=False,
    delete_seam=False,
):
    cell, _axis, target, left_mode, right_mode = seam
    left = C871.physical_b(graph, context, cell, left_mode)
    right = C871.physical_b(graph, context, target, right_mode)
    du = placement.sites[C714.MCX_WORK[0]]
    dv = placement.sites[C714.MCX_WORK[1]]
    pointer = placement.sites[C714.POINTER]
    spatial = spatial_current_site(placement)
    pre = C871.extract_b(left, context, du, "check_pre_l") + C871.extract_b(
        right, context, dv, "check_pre_r"
    )
    seam_word = C871.compile_rotations(actual_rows, context)
    if delete_seam:
        seam_word = ()
    post = C871.extract_b(left, context, du, "check_post_l") + C871.extract_b(
        right, context, dv, "check_post_r"
    )
    endpoint_or = (
        C871.cnot(du, pointer, "check_or"), C871.cnot(dv, pointer, "check_or")
    ) + C871.toffoli_word(du, dv, pointer, "check_or_tof_")
    clean = (
        C871.extract_b(left, context, du, "check_clean_l")
        + C871.extract_b(right, context, du, "check_clean_r")
        + C871.extract_b(left, context, dv, "check_clean_l")
        + C871.extract_b(right, context, dv, "check_clean_r")
    )
    direction_b = left if wrong_side else right
    direction = (
        C871.extract_b(direction_b, context, du, "check_direction_load")
        + C871.toffoli_word(pointer, du, spatial, "check_direction_tof_")
        + C871.extract_b(direction_b, context, du, "check_direction_unload")
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


def independent_macro(graph, context, seam, placement, actual_rows):
    segments = independent_segments(graph, context, seam, placement, actual_rows)
    return tuple(
        instruction for word in segments.values() for instruction in word
    ), segments["seam"]


def canonical_json_bytes(value):
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), default=float)
        + "\n"
    ).encode()


def matrix_payload(matrix):
    array = np.asarray(matrix, dtype=complex)
    return {
        "shape": tuple(map(int, array.shape)),
        "row_major_complex_float_hex": tuple(
            (float(value.real).hex(), float(value.imag).hex())
            for value in array.reshape(-1)
        ),
        "cycle655_rounded_matrix_sha256": C870.c707.c655.matrix_digest(array),
    }


def matrix_key(matrix):
    return sha256(canonical_json_bytes(matrix_payload(matrix))).hexdigest()


def independent_physical_stream_check():
    """Reconstruct the L2 full factor/stage/routed-gate ledger independently."""
    graph = C870.prep.OpenReferenceGraph(cells(2))
    context = C870.physical_context(graph)
    seams = C870.graph_seams(graph)
    placements = tuple(C871.packet_placement(graph, context, seam) for seam in seams)
    rotations, _inventory = C870.build_update(graph, C871.coin_schedule())
    factors = tuple(
        (tuple(factor), tuple(group))
        for factor, group in groupby(rotations, key=lambda row: row.factor)
    )
    seam_lookup = {
        ("seam", index, seam[0], seam[1], seam[2]): (seam, placements[index])
        for index, seam in enumerate(seams)
    }
    failures = Counter()
    registry = {}
    instructions = []
    gates = []
    factor_manifest = []
    deletion_detections = 0

    def register(matrix):
        key = matrix_key(matrix)
        payload = matrix_payload(matrix)
        failures["matrix_digest_collision"] += key in registry and registry[key] != payload
        registry[key] = payload
        return key

    def emit(factor_index, factor, stage, segment, rotation_serial,
             instruction, route_policy, basis):
        nonlocal deletion_detections
        serial = len(instructions)
        if len(instruction.sites) == 1:
            path = tuple(instruction.sites)
        elif route_policy == "landed_global_axis_manhattan_returned":
            path = tuple(C870.c707.c655.manhattan_path(*instruction.sites))
        else:
            path = C871.coframe_path(*instruction.sites, basis)
        failures["arity"] += len(instruction.sites) not in (1, 2)
        failures["endpoints"] += (
            not path
            or path[0] != instruction.sites[0]
            or path[-1] != instruction.sites[-1]
        )
        gate_start = len(gates)
        source_matrix = register(instruction.matrix)
        if len(instruction.sites) == 1:
            gates.append({
                "serial": len(gates), "factor_index": factor_index,
                "instruction_serial": serial, "role": "active_one_site",
                "sites": instruction.sites, "matrix": source_matrix,
            })
        else:
            labels = list(path)
            swap_matrix = register(C870.c707.c655.SWAP)
            for route_index in range(len(path) - 2):
                sites = (path[route_index], path[route_index + 1])
                gates.append({
                    "serial": len(gates), "factor_index": factor_index,
                    "instruction_serial": serial, "role": "swap_forward",
                    "sites": sites, "matrix": swap_matrix,
                })
                labels[route_index], labels[route_index + 1] = (
                    labels[route_index + 1], labels[route_index]
                )
            failures["operands"] += tuple(labels[-2:]) != instruction.sites
            gates.append({
                "serial": len(gates), "factor_index": factor_index,
                "instruction_serial": serial, "role": "active_two_site",
                "sites": (path[-2], path[-1]), "matrix": source_matrix,
            })
            for route_index in reversed(range(len(path) - 2)):
                sites = (path[route_index], path[route_index + 1])
                gates.append({
                    "serial": len(gates), "factor_index": factor_index,
                    "instruction_serial": serial, "role": "swap_return",
                    "sites": sites, "matrix": swap_matrix,
                })
                labels[route_index], labels[route_index + 1] = (
                    labels[route_index + 1], labels[route_index]
                )
            failures["spectator_return"] += labels != list(path)
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
        failures["NN"] += sum(
            len(row["sites"]) == 2 and C870.c707.c655.l1(*row["sites"]) != 1
            for row in gates[gate_start:gate_stop]
        )
        failures["one_active"] += sum(
            row["role"].startswith("active") for row in gates[gate_start:gate_stop]
        ) != 1
        instructions.append({
            "serial": serial,
            "factor_index": factor_index,
            "factor": factor,
            "stage": stage,
            "segment": segment,
            "rotation_serial": rotation_serial,
            "kind": instruction.kind,
            "unrouted_sites": instruction.sites,
            "unrouted_matrix": source_matrix,
            "route_policy": route_policy,
            "path": path,
            "gate_serial_start": gate_start,
            "gate_serial_stop_exclusive": gate_stop,
        })

    for factor_index, (factor, factor_rotations) in enumerate(factors):
        stage = str(factor[0])
        instruction_start = len(instructions)
        gate_start = len(gates)
        route_policy = (
            "augmented_seam_local_coframe_returned"
            if stage == "seam" else "landed_global_axis_manhattan_returned"
        )
        if stage == "seam":
            seam, placement = seam_lookup[factor]
            segments = independent_segments(
                graph, context, seam, placement, factor_rotations
            )
            for segment, word in segments.items():
                if segment == "seam":
                    actual = []
                    for rotation in factor_rotations:
                        rotation_word = C870.c707.compile_pauli_rotation(
                            C870.physical_lift(rotation.row, context),
                            context.sites, rotation.angle,
                        )
                        actual.extend(rotation_word)
                        for instruction in rotation_word:
                            emit(
                                factor_index, factor, stage, segment, rotation.serial,
                                instruction, route_policy, placement.basis,
                            )
                    failures["seam_word"] += (
                        C871.word_sha256(tuple(actual)) != C871.word_sha256(word)
                    )
                else:
                    for instruction in word:
                        emit(
                            factor_index, factor, stage, segment, None,
                            instruction, route_policy, placement.basis,
                        )
        else:
            for rotation in factor_rotations:
                for instruction in C870.c707.compile_pauli_rotation(
                    C870.physical_lift(rotation.row, context),
                    context.sites, rotation.angle,
                ):
                    emit(
                        factor_index, factor, stage, "landed_factor", rotation.serial,
                        instruction, route_policy, None,
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

    failures["factor_sequence"] += tuple(
        row["factor"] for row in factor_manifest
    ) != tuple(factor for factor, _rows in factors)
    failures["rotation_coverage"] += tuple(
        serial for row in factor_manifest for serial in row["native_rotation_serials"]
    ) != tuple(row.serial for row in rotations)
    failures["gate_serial"] += any(
        row["serial"] != index for index, row in enumerate(gates)
    )
    failures["stage_order"] += tuple(dict.fromkeys(
        row["stage"] for row in factor_manifest
    )) != ("coin", "reverse", "seam", "contact")
    gate_stages = Counter(
        factor_manifest[row["factor_index"]]["stage"] for row in gates
    )
    result = {
        "length": 2,
        "native_rotations": len(rotations),
        "native_factors": len(factors),
        "unrouted_bound_instructions": len(instructions),
        "physical_local_gates": len(gates),
        "matrix_registry_entries": len(registry),
        "first_forward_swap_deletion_detections": deletion_detections,
        "deletion_control_scope": (
            "delete the first forward SWAP of every nontrivial returned route; "
            "not exhaustive over arbitrary SWAP positions"
        ),
        "factor_stage_census": dict(Counter(row["stage"] for row in factor_manifest)),
        "physical_gate_stage_census": dict(gate_stages),
        "factor_manifest_sha256": sha256(canonical_json_bytes(
            tuple(factor_manifest)
        )).hexdigest(),
        "instruction_binding_sha256": sha256(canonical_json_bytes(
            tuple(instructions)
        )).hexdigest(),
        "label_insensitive_instruction_binding_sha256": sha256(
            canonical_json_bytes(tuple(
                {key: value for key, value in row.items() if key != "kind"}
                for row in instructions
            ))
        ).hexdigest(),
        "instruction_label_scope": (
            "compiler kind strings intentionally excluded; all semantic binding fields retained"
        ),
        "normalized_physical_gate_sha256": sha256(canonical_json_bytes(
            tuple(gates)
        )).hexdigest(),
        "matrix_registry_sha256": sha256(canonical_json_bytes(
            dict(sorted(registry.items()))
        )).hexdigest(),
        "native_factor_sha256": C870.factor_digest(rotations),
        "failure_census": dict(failures),
    }
    result["expected_mismatches"] = {
        key: (expected, result.get(key))
        for key, expected in EXPECTED_PHYSICAL_STREAM.items()
        if result.get(key) != expected
    }
    return result


def path_metrics(word, basis):
    depth = deletion = returns = operands = 0
    footprint = set()
    for instruction in word:
        if len(instruction.sites) == 1:
            depth += 1
            footprint.update(instruction.sites)
            continue
        path = C871.coframe_path(*instruction.sites, basis)
        depth += 2 * len(path) - 3
        footprint.update(path)
        labels = list(range(len(path)))
        for index in range(len(path) - 2):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        operands += labels[-2:] != [0, len(path) - 1]
        for index in reversed(range(len(path) - 2)):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        returns += labels != list(range(len(path)))
        if len(path) > 2:
            damaged = list(range(len(path)))
            for index in range(1, len(path) - 2):
                damaged[index], damaged[index + 1] = damaged[index + 1], damaged[index]
            for index in reversed(range(len(path) - 2)):
                damaged[index], damaged[index + 1] = damaged[index + 1], damaged[index]
            deletion += damaged != list(range(len(path)))
    return depth, footprint, deletion, operands, returns


def independent_routed_macro_payload(word, basis):
    output = []
    for serial, instruction in enumerate(word):
        source_matrix = matrix_key(instruction.matrix)
        if len(instruction.sites) == 1:
            output.append({
                "instruction_serial": serial, "role": "active_one_site",
                "sites": instruction.sites, "matrix": source_matrix,
            })
            continue
        path = C871.coframe_path(*instruction.sites, basis)
        swap_matrix = matrix_key(C870.c707.c655.SWAP)
        for index in range(len(path) - 2):
            output.append({
                "instruction_serial": serial, "role": "swap_forward",
                "sites": (path[index], path[index + 1]), "matrix": swap_matrix,
            })
        output.append({
            "instruction_serial": serial, "role": "active_two_site",
            "sites": (path[-2], path[-1]), "matrix": source_matrix,
        })
        for index in reversed(range(len(path) - 2)):
            output.append({
                "instruction_serial": serial, "role": "swap_return",
                "sites": (path[index], path[index + 1]), "matrix": swap_matrix,
            })
    return tuple(output)


def independent_macro_mutations():
    graph = C870.prep.OpenReferenceGraph(cells(2))
    context = C870.physical_context(graph)
    seams = C870.graph_seams(graph)
    rotations, _inventory = C870.build_update(graph, C871.coin_schedule())
    factor_map = {
        factor: tuple(group)
        for factor, group in groupby(rotations, key=lambda row: row.factor)
        if factor[0] == "seam"
    }
    families = {"canonical": [], "wrong_side": [], "seam_deleted": []}
    for index, seam in enumerate(seams):
        placement = C871.packet_placement(graph, context, seam)
        factor = ("seam", index, seam[0], seam[1], seam[2])
        rows = factor_map[factor]
        for label, options in (
            ("canonical", {}),
            ("wrong_side", {"wrong_side": True}),
            ("seam_deleted", {"delete_seam": True}),
        ):
            segments = independent_segments(
                graph, context, seam, placement, rows, **options
            )
            word = tuple(
                instruction for segment in segments.values() for instruction in segment
            )
            families[label].append(independent_routed_macro_payload(word, placement.basis))
    return {
        "seams": len(seams),
        "canonical_routed_macro_sha256": sha256(canonical_json_bytes(
            tuple(families["canonical"])
        )).hexdigest(),
        "wrong_side_routed_macro_sha256": sha256(canonical_json_bytes(
            tuple(families["wrong_side"])
        )).hexdigest(),
        "seam_deleted_routed_macro_sha256": sha256(canonical_json_bytes(
            tuple(families["seam_deleted"])
        )).hexdigest(),
        "wrong_side_digest_detections": sum(
            left != right for left, right in zip(
                families["canonical"], families["wrong_side"]
            )
        ),
        "seam_deletion_digest_detections": sum(
            left != right for left, right in zip(
                families["canonical"], families["seam_deleted"]
            )
        ),
    }


def fixture(length, full):
    graph = C870.prep.OpenReferenceGraph(cells(length))
    context = C870.physical_context(graph)
    seams = C870.graph_seams(graph)
    placements = tuple(C871.packet_placement(graph, context, seam) for seam in seams)
    spatial_sites = tuple(spatial_current_site(placement) for placement in placements)
    resource_banks = tuple(resource_bank(placement) for placement in placements)
    blocked = set(context.sites) | J870.auxiliary_registers(graph)
    rotations, _inventory = C870.build_update(graph, C871.coin_schedule())
    factors = tuple(
        (factor, tuple(group))
        for factor, group in groupby(rotations, key=lambda row: row.factor)
    )
    factor_map = {
        factor: rows for factor, rows in factors if factor[0] == "seam"
    }
    words = []
    seam_words = []
    binding_failures = 0
    for index, (seam, placement) in enumerate(zip(seams, placements)):
        key = ("seam", index, seam[0], seam[1], seam[2])
        rows = factor_map.get(key, ())
        binding_failures += len(rows) != 4
        word, seam_word = independent_macro(graph, context, seam, placement, rows)
        words.append(word)
        seam_words.append(seam_word)

    metrics = [path_metrics(word, placement.basis) for word, placement in zip(words, placements)]
    depths = {seam: metrics[index][0] for index, seam in enumerate(seams)}
    footprints = {seam: metrics[index][1] for index, seam in enumerate(seams)}
    deletion = sum(row[2] for row in metrics)
    route_failures = sum(row[3] + row[4] for row in metrics)
    groups = defaultdict(list)
    for seam in seams:
        groups[fine(seam)].append(seam)
    schedule_depth = sum(max(depths[seam] for seam in members) for members in groups.values())
    fine_collisions = sum(
        bool(footprints[left] & footprints[right])
        for index, left in enumerate(seams) for right in seams[:index]
        if fine(left) == fine(right)
    )
    six_collisions = sum(
        bool(footprints[left] & footprints[right])
        for index, left in enumerate(seams) for right in seams[:index]
        if coarse(left) == coarse(right)
    )
    packet_union = set().union(*(set(row.sites) for row in placements))
    resource_union = set().union(*resource_banks)
    packet_overlaps = sum(
        bool(set(left.sites) & set(right.sites))
        for index, left in enumerate(placements) for right in placements[:index]
    )
    resource_overlaps = sum(
        bool(left & right)
        for index, left in enumerate(resource_banks) for right in resource_banks[:index]
    )
    spatial_geometry_failures = (
        len(spatial_sites) - len(set(spatial_sites))
        + sum(site in packet_union for site in spatial_sites)
        + sum(site in blocked for site in spatial_sites)
    )

    route_difference = reconcile_failures = 0
    for seam_word, placement in zip(seam_words, placements):
        for instruction in seam_word:
            if len(instruction.sites) != 2:
                continue
            replacement = C871.coframe_path(*instruction.sites, placement.basis)
            landed = tuple(C870.c707.c655.manhattan_path(*instruction.sites))
            route_difference += replacement != landed
            reconcile_failures += (
                replacement[0] != landed[0] or replacement[-1] != landed[-1]
            )

    bank_at = {
        site: bank for bank, resources in enumerate(resource_banks) for site in resources
    }
    dirty_pairs = set()
    dirty_failures = 0
    if full:
        for macro, (seam, placement, word) in enumerate(zip(seams, placements, words)):
            for instruction in word:
                if len(instruction.sites) != 2:
                    continue
                path = C871.coframe_path(*instruction.sites, placement.basis)
                for path_index, site in enumerate(path):
                    other = bank_at.get(site)
                    if other is None or other == macro:
                        continue
                    dirty_pairs.add((macro, other))
                    dirty_failures += path_index in (0, len(path) - 1)
                    dirty_failures += fine(seam) == fine(seams[other])

    result = {
        "length": length,
        "cells": len(graph.cells),
        "seams": len(seams),
        "rotations": len(rotations),
        "factors": len(factors),
        "instructions": sum(map(len, words)),
        "binding_failures": binding_failures,
        "schedule_depth": schedule_depth,
        "fine_collisions": fine_collisions,
        "six_collisions": six_collisions,
        "packet_union": len(packet_union),
        "resource_union": len(resource_union),
        "packet_overlaps": packet_overlaps,
        "resource_overlaps": resource_overlaps,
        "spatial_geometry_failures": spatial_geometry_failures,
        "first_forward_swap_deletion_detections": deletion,
        "route_failures": route_failures,
        "route_differences": route_difference,
        "route_reconciliation_failures": reconcile_failures,
        "dirty_pairs": len(dirty_pairs),
        "dirty_failures": dirty_failures,
        "used_packet_M2_per_seam": C714.N,
        "retained_spatial_current_M2_per_seam": 1,
        "total_resource_M2_per_seam": C714.N + 1,
        "spatial_output_local_coordinate": SPATIAL_CURRENT_LOCAL,
        "lockstep_schedule_key": (
            "nested coarse=(axis,owner[axis] mod 2), then fine=owner parities "
            "on remaining axes in ascending global-axis order"
        ),
        "route_policy": "coframe replacement in augmented seam stage",
    }
    expected = EXPECTED_FIXTURES[length]
    result["expected_mismatches"] = {
        key: (expected_value, result.get(key))
        for key, expected_value in expected.items()
        if result.get(key) != expected_value
    }
    return result


def direction_check():
    failures = Counter()
    counts = Counter()
    pairs = set()
    for pointer, binder, actuality, admissibility, law, fresh, causal in product(
        (0, 1), repeat=7
    ):
        controls = (pointer, binder, actuality, admissibility, law, fresh)
        after = C714.apply_semantic(
            C714.initial(9, 12, causal, controls), C714.word()
        )
        counts["exact_packet_equation_rows"] += 1
        failures["exact_packet_equation"] += after[C714.PORIENT] != (
            pointer & binder & actuality & admissibility & law & fresh & causal
        )
    for axis in range(3):
        left, right = 2 * axis + 1, 6 + 2 * axis
        for source in product((0, 1), repeat=12):
            target, _phase = C704.GAUSS.target_fswap_action(source, left, right)
            pointer = source[left] ^ source[right]
            uv = pointer & target[right]
            vu = pointer & target[left]
            failures["one_hot"] += (uv ^ vu) != pointer
            failures["current_decode"] += 2 * uv - pointer != uv - vu
            for causal in (0, 1):
                pairs.add((uv, causal))
                counts["rows"] += 1
                counts["moving"] += pointer
                counts["wrong_side"] += pointer and vu != uv
                counts["seam_deletion"] += (0, 0) != (pointer, uv)
                spatial = pointer & target[right]
                failures["spatial_output"] += spatial != uv
                counts["dirty_spatial"] += (1 ^ spatial) != uv
                before = C714.initial(
                    9, 12, causal, (pointer, 1, 1, 1, 1, 1)
                )
                after = C714.apply_semantic(before, C714.word())
                failures["causal_projection"] += (
                    after[C714.PORIENT] != pointer & causal
                )
                failures["causal_return"] += after[C714.ORIENT] != causal
                damaged = C714.initial(
                    9, 12, causal ^ uv, (pointer, 1, 1, 1, 1, 1)
                )
                damaged_after = C714.apply_semantic(damaged, C714.word())
                counts["ORIENT_overload"] += (
                    damaged_after[C714.PORIENT] != pointer & causal
                )
    once = C714.apply_semantic(C714.initial(9, 12, 1), C714.word())
    twice = C714.apply_semantic(once, C714.word())
    return {
        **dict(counts), "failure_census": dict(failures),
        "spatial_causal_pairs": tuple(sorted(pairs)),
        "reuse_changed_bits": sum(a != b for a, b in zip(once, twice)),
    }


def continuity_check():
    graph = C870.prep.OpenReferenceGraph(cells(2))
    seams = C870.graph_seams(graph)
    index = {cell: row for row, cell in enumerate(graph.cells)}
    failures = 0
    patterns = 0
    for currents in product((-1, 0, 1), repeat=len(seams)):
        direct = [0] * len(graph.cells)
        incidence = [0] * len(graph.cells)
        for seam, current in zip(seams, currents):
            pre_u, pre_v = (
                (1, 0) if current == 1 else (0, 1) if current == -1 else (0, 0)
            )
            post_u, post_v = pre_v, pre_u
            direct[index[seam[0]]] += post_u - pre_u
            direct[index[seam[2]]] += post_v - pre_v
            incidence[index[seam[0]]] -= current
            incidence[index[seam[2]]] += current
        failures += direct != incidence or sum(direct) != 0
        patterns += 1
    frame_failures = product_failures = 0
    frames = C871.proper_frames()
    for seam in seams:
        for frame in frames:
            _axis, sign = C871.signed_axis(frame, seam[1])
            for current in (-1, 0, 1):
                moved = sign * current
                frame_failures += abs(moved) != abs(current)
        for left in frames:
            for right in frames:
                intermediate, sr = C871.signed_axis(right, seam[1])
                _final, sl = C871.signed_axis(left, intermediate)
                _product, sp = C871.signed_axis(left @ right, seam[1])
                for current in (-1, 0, 1):
                    product_failures += sl * sr * current != sp * current
    return {
        "patterns": patterns,
        "covered_columns": 4 ** len(seams),
        "continuity_failures": failures,
        "frame_rows": len(seams) * len(frames) * 3,
        "frame_failures": frame_failures,
        "product_rows": len(seams) * len(frames) ** 2 * 3,
        "product_failures": product_failures,
    }


def allocator_check():
    graph = C870.prep.OpenReferenceGraph(cells(2))
    context = C870.physical_context(graph)
    seam = C870.graph_seams(graph)[0]
    midpoint = C871.seam_midpoint(seam[0], seam[1])
    basis = C871.local_coframe(seam[1])
    blocked = set(context.sites) | J870.auxiliary_registers(graph)
    def physical(local):
        output = midpoint
        for coefficient, direction in zip(local, basis):
            output = C871.add(output, C871.scale(coefficient, direction))
        return output
    available = {
        row for row in product(range(-3, 4), repeat=3) if physical(row) not in blocked
    }
    def rotate(row):
        a, b, c = row
        return a, -c, b
    seen = set()
    orbits = []
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
            orbits.append(orbit)
    reflect = lambda orbit: frozenset((-a, b, -c) for a, b, c in orbit)
    fixed = sorted((row for row in orbits if reflect(row) == row), key=repr)
    paired = []
    used = set(fixed)
    for orbit in sorted(orbits, key=repr):
        if orbit in used:
            continue
        partner = reflect(orbit)
        pair = tuple(sorted((orbit, partner), key=repr))
        paired.append(pair)
        used.update(pair)
    paired.sort(key=repr)
    selected = tuple(fixed[:5]) + tuple(row for pair in paired[:27] for row in pair)
    selected_set = set(selected)
    sites = frozenset(site for orbit in selected for site in orbit)
    failures = 0
    products = 0
    frames = C871.proper_frames()
    def matrix(axis, frame):
        target, _sign = C871.signed_axis(frame, axis)
        return target, np.asarray(
            np.column_stack(C871.local_coframe(target)).T
            @ frame @ np.column_stack(C871.local_coframe(axis)), dtype=int
        )
    for axis in range(3):
        for frame in frames:
            _target, transform = matrix(axis, frame)
            failures += frozenset(
                tuple(map(int, transform @ np.asarray(site))) for site in sites
            ) != sites
            failures += any(
                frozenset(tuple(map(int, transform @ np.asarray(site))) for site in orbit)
                not in selected_set for orbit in selected
            )
        for left in frames:
            for right in frames:
                intermediate, mr = matrix(axis, right)
                final, ml = matrix(intermediate, left)
                product_axis, mp = matrix(axis, left @ right)
                products += 1
                failures += final != product_axis or not np.array_equal(ml @ mr, mp)
    return {
        "status": "separate geometric candidate",
        "used_by_epoch": False,
        "available_orbits": len(orbits),
        "selected_registers": len(selected),
        "M2_per_seam": len(sites),
        "frames": len(frames),
        "products": products,
        "failures": failures,
    }


def mass_contact_check():
    inherited = C871.inherited_matter_certificate()
    return {
        "scope": (
            "inherited unchanged Cycle870/Cycle871 factor fixtures; not a new "
            "integrated-epoch spectrum"
        ),
        "mass": inherited["mass_fixture_pass"],
        "contact": inherited["contact_fixture_pass"],
        "mass_difference": abs(
            inherited["one_particle"]["analytic_mass"]
            - inherited["one_particle"]["rest_mass"]
        ),
        "contact_residual": inherited["contact"]["maximum_residual_up_to_global_phase"],
    }


def build_report():
    report = {
        "schema": "cycle872-all-seam-spatial-packet-independent-v1",
        "status": "pending",
        "independence": independent_import_certificate(),
        "provenance": provenance(),
        "physical_epoch_stream": independent_physical_stream_check(),
        "physical_macro_mutations": independent_macro_mutations(),
        "fixtures": [fixture(length, length in (2, 3)) for length in (2, 3, 4, 5)],
        "direction": direction_check(),
        "continuity": continuity_check(),
        "four_rail_candidate": allocator_check(),
        "mass_contact": mass_contact_check(),
        "scope": (
            "one clean-own-bank epoch using a 59-site packet plus separate retained spatial-current "
            "M2 per seam and a declared coframe replacement route; four-rail allocation is separate; "
            "causal ORIENT and later reset remain supplied"
        ),
    }
    failures = []
    if report["independence"]["primary_imported"]:
        failures.append("primary imported")
    if report["provenance"]["pin_failures"] or report["provenance"]["note_pin_failure"]:
        failures.append("provenance")
    stream = report["physical_epoch_stream"]
    if any(stream["failure_census"].values()) or stream["expected_mismatches"]:
        failures.append("physical epoch stream")
    if stream["first_forward_swap_deletion_detections"] <= 0:
        failures.append("physical stream deletion")
    mutations = report["physical_macro_mutations"]
    if any((
        mutations["wrong_side_digest_detections"] != mutations["seams"],
        mutations["seam_deletion_digest_detections"] != mutations["seams"],
    )):
        failures.append("physical macro mutations")
    for row in report["fixtures"]:
        if row["expected_mismatches"]:
            failures.append(f"L{row['length']} expected mismatch")
        if any(row[key] for key in (
            "binding_failures", "packet_overlaps", "resource_overlaps",
            "spatial_geometry_failures", "route_failures",
            "route_reconciliation_failures", "fine_collisions",
        )):
            failures.append(f"L{row['length']} fixture failure")
        if row["six_collisions"] <= 0 or row["first_forward_swap_deletion_detections"] <= 0:
            failures.append(f"L{row['length']} inactive control")
        if row["length"] in (2, 3) and row["dirty_failures"]:
            failures.append(f"L{row['length']} dirty")
    if any(report["direction"]["failure_census"].values()):
        failures.append("direction")
    if any((
        report["direction"]["wrong_side"] != 12288,
        report["direction"]["dirty_spatial"] != 24576,
        report["direction"]["ORIENT_overload"] != 6144,
        report["direction"]["seam_deletion"] != 12288,
        len(report["direction"]["spatial_causal_pairs"]) != 4,
    )):
        failures.append("direction controls")
    if report["direction"]["reuse_changed_bits"] <= 0:
        failures.append("reuse control")
    if any(report["continuity"][key] for key in (
        "continuity_failures", "frame_failures", "product_failures"
    )):
        failures.append("continuity")
    if report["four_rail_candidate"]["failures"]:
        failures.append("allocator")
    if not report["mass_contact"]["mass"] or not report["mass_contact"]["contact"]:
        failures.append("mass/contact")
    report["failures"] = failures
    report["status"] = "pass" if not failures else "fail"
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_RECEIPT)
    args = parser.parse_args()
    report = build_report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True, default=float) + "\n",
        encoding="utf-8",
    )
    print("CYCLE872_ALL_SEAM_SPATIAL_PACKET_INDEPENDENT_PASS" if report["status"] == "pass"
          else "CYCLE872_ALL_SEAM_SPATIAL_PACKET_INDEPENDENT_FAIL")
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
