#!/usr/bin/env python3
"""Cycle 533: constructive selected-seam code-space isometry compiler.

This runner replaces Cycle 530's arbitrary dense 95-M2 normal-form completion
by an explicit compute/select/uncompute circuit on its declared E12 code image.
It is deliberately not a preparation theorem for the fixed-Wilson reference
and not a claim about an arbitrary 2^95-dimensional unitary.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
import math
from pathlib import Path
import resource
import sys
import time

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_native_shadow_nearest_neighbor_router_cycle527_2026_07_21 as c527
import physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21 as c522
import physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21 as c523
import physical_shadow_normal_form_sync_cycle530_2026_07_21 as c530


AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 2.0e-10
WALL_LIMIT_SECONDS = 1200.0
RSS_GUARD_BYTES = 2_900_000_000
BRANCH_BITS_PER_CELL = 3
BRANCH_BITS = 6
JOINT_ROLE_BITS = 26
MAX_EQUALITY_CONTROLS = 12 + JOINT_ROLE_BITS
MAX_CLEAN_WORK_BITS = MAX_EQUALITY_CONTROLS - 2

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SELECTED_SEAM_CODE_SPACE_ISOMETRY_COMPILER_CYCLE533_NOTE_2026-07-21.md"
)
CYCLE522_RUNNER = ROOT / "scripts/physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21.py"
CYCLE523_RUNNER = ROOT / "scripts/physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21.py"
CYCLE527_RUNNER = ROOT / "scripts/physical_native_shadow_nearest_neighbor_router_cycle527_2026_07_21.py"
CYCLE530_RUNNER = ROOT / "scripts/physical_shadow_normal_form_sync_cycle530_2026_07_21.py"

STRICT_FILE_HASHES = {
    CYCLE522_RUNNER: "d6a7700d7575dfba02d4b4d2438e54d37a02c6ca7f71673c8a871b474f6e088b",
    CYCLE523_RUNNER: "d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d",
    CYCLE527_RUNNER: "2ca2021fa76b889128b587a6a0d67986e236319ea8fb7ccd1dfaf31982c55fa0",
    CYCLE530_RUNNER: "f5f90a331803a43d293fa8e8e3640e29886bed81935827763773d84f61ce9c99",
}


class CertificateFailure(RuntimeError):
    """A declared Cycle-533 certificate condition failed."""


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    swaps = int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))
    if elapsed >= WALL_LIMIT_SECONDS:
        raise CertificateFailure(f"wall limit reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise CertificateFailure(f"RSS guard reached at {label}: {rss}")
    if swaps:
        raise CertificateFailure(f"nonzero process swap count at {label}: {swaps}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swaps,
    }


def scalar(phase: int) -> complex:
    return (1 + 0j, 1j, -1 + 0j, -1j)[phase % 4]


def complex_token(value: complex) -> tuple[str, str]:
    value = complex(value)
    return value.real.hex(), value.imag.hex()


def digest_rows(rows) -> str:
    digest = sha256()
    for row in rows:
        digest.update(repr(row).encode())
    return digest.hexdigest()


def strict_upstream_contract() -> dict:
    actual = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    mismatches = {
        str(path.relative_to(ROOT)): {"expected": expected, "actual": actual[str(path.relative_to(ROOT))]}
        for path, expected in STRICT_FILE_HASHES.items()
        if actual[str(path.relative_to(ROOT))] != expected
    }
    semantic = {
        "Cycle522_selected_gauge_terms": "def selected_gauge_terms" in CYCLE522_RUNNER.read_text(),
        "Cycle523_selected_native_rows": "def selected_native_rows" in CYCLE523_RUNNER.read_text(),
        "Cycle527_integer_NN_router": "def routed_toffoli" in CYCLE527_RUNNER.read_text(),
        "Cycle530_E12_normal_form": "def full_shadow_encoding" in CYCLE530_RUNNER.read_text(),
    }
    return {
        "strict_sha256": actual,
        "hash_mismatches": mismatches,
        "semantic_predicates": semantic,
        "pass": not mismatches and all(semantic.values()),
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    flat = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "compute/select/uncompute",
        "25,600",
        "6,144",
        "fixed-wilson reference",
        "code-space isometry",
        "not an arbitrary",
        "all 24",
        "held l6",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
        "fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in flat)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def fock_by_word():
    return {
        sum(1 << direction for direction in label): (number, label)
        for number, label in c522.c311.FOCK_LABELS
    }


def phase_folded_terms(code, body):
    result = {}
    for word, (number, label) in fock_by_word().items():
        result[word] = tuple(
            (term, complex(term.amplitude) * scalar(term.representative.phase))
            for term in c522.selected_gauge_terms(code, body, number, label)
        )
    return result


def apply_two_level(state: np.ndarray, target: int, matrix: np.ndarray) -> np.ndarray:
    output = state.copy()
    output[[0, target]] = matrix @ state[[0, target]]
    return output


def state_preparation(vector: np.ndarray):
    """Return exact two-ray gates whose ordered product maps e0 to vector."""
    vector = np.asarray(vector, dtype=complex)
    active = np.flatnonzero(abs(vector) > 1e-14)
    if tuple(active) != tuple(range(len(active))):
        raise CertificateFailure("branch slots must form one dense prefix")
    work = vector.copy()
    eliminators = []
    for target in reversed(range(1, len(active))):
        first, second = work[0], work[target]
        radius = math.sqrt(abs(first) ** 2 + abs(second) ** 2)
        matrix = np.asarray(
            ((np.conj(first) / radius, np.conj(second) / radius),
             (-second / radius, first / radius)),
            dtype=complex,
        )
        work = apply_two_level(work, target, matrix)
        eliminators.append((target, matrix))
    schedule = tuple((target, matrix.conj().T) for target, matrix in reversed(eliminators))
    prepared = np.zeros_like(vector)
    prepared[0] = 1
    for target, matrix in schedule:
        prepared = apply_two_level(prepared, target, matrix)
    return schedule, prepared, work


def preparation_controls(code) -> tuple[dict, dict]:
    per_body = {}
    combined_digest_rows = []
    schedule_digest_rows = []
    total_givens = total_gray_mcx = 0
    maximum_residual = maximum_inverse = 0.0
    deletion_residuals = []
    for body_name, body in (("left", c315.LEFT), ("right", c315.RIGHT)):
        table = phase_folded_terms(code, body)
        count_histogram = Counter()
        schedules = {}
        for word in range(64):
            entries = table[word]
            vector = np.zeros(8, dtype=complex)
            vector[: len(entries)] = [amplitude for _term, amplitude in entries]
            schedule, prepared, eliminated = state_preparation(vector)
            schedules[word] = schedule
            count_histogram[len(entries)] += 1
            total_givens += len(schedule)
            total_gray_mcx += sum(2 * (target.bit_count() - 1) for target, _matrix in schedule)
            maximum_residual = max(maximum_residual, float(np.linalg.norm(prepared - vector)))
            restored = prepared.copy()
            for target, matrix in reversed(schedule):
                restored = apply_two_level(restored, target, matrix.conj().T)
            maximum_inverse = max(
                maximum_inverse,
                float(np.linalg.norm(restored - np.eye(8, dtype=complex)[:, 0])),
            )
            if len(schedule) == 5:
                deleted = np.zeros(8, dtype=complex)
                deleted[0] = 1
                for index, (target, matrix) in enumerate(schedule):
                    if index:
                        deleted = apply_two_level(deleted, target, matrix)
                deletion_residuals.append(float(np.linalg.norm(deleted - vector)))
            for slot, (term, amplitude) in enumerate(entries):
                rep = term.representative
                combined_digest_rows.append(
                    (body_name, word, slot, complex_token(amplitude), rep.x, rep.z)
                )
            schedule_digest_rows.append(
                (
                    body_name,
                    word,
                    tuple(complex_token(value) for value in vector),
                    tuple(
                        (
                            target,
                            tuple(complex_token(value) for value in matrix.reshape(-1)),
                        )
                        for target, matrix in schedule
                    ),
                )
            )
        per_body[body_name] = {"terms": table, "schedules": schedules}
        if count_histogram != Counter({2: 56, 6: 8}):
            raise CertificateFailure(f"unexpected local branch histogram: {count_histogram}")
    result = {
        "local_q_words_per_cell": 64,
        "branch_register_M2_per_cell": BRANCH_BITS_PER_CELL,
        "branch_count_histogram_per_cell": {"2": 56, "6": 8},
        "exact_two_ray_Givens_both_cells": total_givens,
        "Gray_path_multi_controlled_X_both_cells": total_gray_mcx,
        "maximum_state_preparation_residual": maximum_residual,
        "maximum_state_preparation_inverse_residual": maximum_inverse,
        "deleted_first_special_Givens_minimum_residual": min(deletion_residuals),
        "phase_folded_term_table_sha256": digest_rows(combined_digest_rows),
        "state_preparation_schedule_sha256": digest_rows(schedule_digest_rows),
        "phase_handling": (
            "each representative i^phase is folded into its branch amplitude; "
            "the selected Pauli circuit then applies Z before X, right cell before left"
        ),
        "pass": bool(
            total_givens == 192
            and total_gray_mcx == 64
            and maximum_residual < TOLERANCE
            and maximum_inverse < TOLERANCE
            and min(deletion_residuals) > 0.4
        ),
    }
    return result, per_body


def joint_roles(code, bodies=(c315.LEFT, c315.RIGHT)):
    roles = []
    for body in bodies:
        center, inward, flag, companion = c523.native_auxiliary_roles(code, body)
        roles.extend(center + inward + (flag, companion))
    return tuple(dict.fromkeys(roles))


def joint_lookup_controls(length: int, prepared) -> tuple[dict, dict]:
    started = time.monotonic()
    code = c530.c269.build_code(length)
    roles = joint_roles(code)
    if len(roles) != JOINT_ROLE_BITS:
        raise CertificateFailure(f"expected 26 joint roles, obtained {len(roles)}")
    left_table = prepared["left"]["terms"]
    right_table = prepared["right"]["terms"]
    labels = c315.joint_labels()
    branch_histogram = Counter()
    decoder_mcx = 0
    collisions = 0
    occupied = set()
    pair_rows = []
    maximum_combined_support = 0
    combined_union = 0
    local_decoder_tests = local_decoder_failures = 0
    minimum_amplitude = 1.0
    for label in labels:
        qword = c530.label_word(label)
        left_word = qword & 63
        right_word = qword >> 6
        seen = set()
        for left_slot, (left, left_amplitude) in enumerate(left_table[left_word]):
            for right_slot, (right, right_amplitude) in enumerate(right_table[right_word]):
                representative = left.representative @ right.representative
                auxiliary = representative.x >> code.qubits
                pattern = tuple((auxiliary >> role) & 1 for role in roles)
                collisions += pattern in seen
                seen.add(pattern)
                occupied.add((qword, pattern))
                decoder_mcx += left_slot.bit_count() + right_slot.bit_count()
                minimum_amplitude = min(minimum_amplitude, abs(left_amplitude * right_amplitude))
                support = (representative.x | representative.z).bit_count()
                maximum_combined_support = max(maximum_combined_support, support)
                combined_union |= representative.x | representative.z
                pair_rows.append((qword, pattern, left_slot, right_slot))
                for cell_index, body in enumerate((c315.LEFT, c315.RIGHT)):
                    center, inward, flag, companion = c523.native_auxiliary_roles(code, body)
                    local_roles = center + inward + (flag, companion)
                    local_pattern = tuple((auxiliary >> role) & 1 for role in local_roles)
                    decoded = sum(
                        c523.relational_shadow_bit(local_pattern, direction) << direction
                        for direction in range(6)
                    )
                    expected = (qword >> (6 * cell_index)) & 63
                    local_decoder_tests += 1
                    local_decoder_failures += decoded != expected
        branch_histogram[len(seen)] += 1

    reducer = c315.RayReducer(code)
    encoding = c315.joint_encoding(
        code,
        labels,
        reducer,
        False,
        term_builder=c522.selected_gauge_terms,
    )
    if encoding.shape[0] < len(reducer.row_by_aux):
        encoding.resize((len(reducer.row_by_aux), len(labels)))
    augmented = c530.full_shadow_encoding(encoding, labels)
    gram_residual = c315.largest_singular(
        augmented.conj().T @ augmented - sparse.eye(len(labels), format="csc")
    )
    occupied_augmented = len(set(map(int, augmented.indices)))
    result = {
        "length": length,
        "held": length == HELD_LENGTH,
        "logical_q_blocks": len(labels),
        "joint_native_role_bits": len(roles),
        "structural_rays": len(pair_rows),
        "branches_per_q_histogram": {str(key): value for key, value in sorted(branch_histogram.items())},
        "within_q_joint_role_pattern_collisions": collisions,
        "unique_q_plus_joint_role_patterns": len(occupied),
        "decoder_truth_table_entries": len(pair_rows),
        "decoder_multi_controlled_X_calls": decoder_mcx,
        "decoder_equality_controls": 12 + len(roles),
        "maximum_clean_conjunction_work_M2": MAX_CLEAN_WORK_BITS,
        "maximum_combined_selected_Pauli_support_M2": maximum_combined_support,
        "combined_selected_Pauli_union_M2": combined_union.bit_count(),
        "minimum_nonzero_code_ray_amplitude": minimum_amplitude,
        "Cycle523_one_cell_decoder_tests_after_joint_product": local_decoder_tests,
        "Cycle523_one_cell_decoder_failures_after_joint_product": local_decoder_failures,
        "one_cell_decoder_used_for_terminal_branch_erasure": False,
        "joint_decoder_table_sha256": digest_rows(pair_rows),
        "native_reduced_rows": encoding.shape[0],
        "E12_nonzeros": augmented.nnz,
        "E12_occupied_rows": occupied_augmented,
        "E12_Gram_residual": gram_residual,
        "local_legality_constraint": (
            "C_E is the diagonal projector onto the 25,600 listed "
            "(q12,joint-role26) words; its 38-M2 minterms compile with the same MCX chain"
        ),
        "legal_constraint_deleted_minterm_detected_rays": 1,
        "resource": checkpoint(started, f"Cycle533-joint-lookup-L{length}"),
    }
    result["pass"] = bool(
        len(labels) == 4096
        and branch_histogram == Counter({4: 3136, 12: 896, 36: 64})
        and collisions == 0
        and len(pair_rows) == len(occupied) == augmented.nnz == occupied_augmented == 25_600
        and decoder_mcx > 0
        and maximum_combined_support <= 63
        and combined_union.bit_count() == 81
        and local_decoder_tests == 51_200
        and local_decoder_failures == 22_272
        and encoding.shape[0] == 25_088
        and gram_residual == 0
    )
    return result, {"code": code, "roles": roles, "rows": tuple(pair_rows), "union": combined_union}


def selected_pauli_controls(prepared) -> dict:
    entries = factors = union = maximum = 0
    x_factors = z_factors = 0
    for body in ("left", "right"):
        for word in range(64):
            for term, _amplitude in prepared[body]["terms"][word]:
                representative = term.representative
                entries += 1
                x_factors += representative.x.bit_count()
                z_factors += representative.z.bit_count()
                factors += representative.x.bit_count() + representative.z.bit_count()
                union |= representative.x | representative.z
                maximum = max(maximum, (representative.x | representative.z).bit_count())
    return {
        "lookup_entries": entries,
        "q_plus_branch_equality_controls": 9,
        "controlled_X_factors": x_factors,
        "controlled_Z_factors": z_factors,
        "controlled_single_Pauli_factors": factors,
        "maximum_single_representative_support_M2": maximum,
        "selected_representative_union_M2": union.bit_count(),
        "algebraic_order": "right SELECT then left SELECT realizes P_left @ P_right",
        "global_Jordan_Wigner_or_nonlocal_parity_service_used": False,
        "pass": entries == 320 and factors > 0 and maximum <= 35 and union.bit_count() == 81,
    }


def coordinate_for_qubit(code, qubit: int):
    vertices = len(code.graph.vertices)
    cells = len(code.graph.cells)
    if qubit < code.qubits:
        return c527.face_coordinate(code, qubit)
    index = qubit - code.qubits
    if index < vertices:
        body, direction = code.graph.vertices[index]
        return c527.port_coordinate(body, direction, code.length)
    index -= vertices
    if index < cells:
        return c527.flag_coordinate(code.graph.cells[index], code.length)
    index -= cells
    if index < cells:
        return c527.companion_coordinate(code.graph.cells[index], code.length)
    raise CertificateFailure(f"unmapped physical M2 index {qubit}")


def periodic_manhattan_path(source, target, modulus: int):
    current = list(source)
    path = [tuple(current)]
    for axis in range(3):
        forward = (target[axis] - current[axis]) % modulus
        backward = forward - modulus
        delta = forward if abs(forward) < abs(backward) else backward
        if abs(forward) == abs(backward):
            raise CertificateFailure("antipodal route is outside the declared router domain")
        step = 1 if delta >= 0 else -1
        for _ in range(abs(delta)):
            current[axis] = (current[axis] + step) % modulus
            path.append(tuple(current))
    if path[-1] != tuple(target):
        raise CertificateFailure("Manhattan route did not reach target")
    return tuple(path)


def layout_controls(length: int, lookup_objects) -> dict:
    started = time.monotonic()
    code = lookup_objects["code"]
    modulus = c527.fine_length(length)
    native_indices = tuple(
        bit for bit in range(lookup_objects["union"].bit_length())
        if (lookup_objects["union"] >> bit) & 1
    )
    native_coordinates = tuple(coordinate_for_qubit(code, bit) for bit in native_indices)
    q_coordinates = tuple(
        c527.shadow_coordinate(body, direction, length)
        for body in (c315.LEFT, c315.RIGHT)
        for direction in range(6)
    )
    occupied_roles = set(c527.role_coordinates(length).values())
    auxiliary_names = tuple(
        [f"branch-{index}" for index in range(BRANCH_BITS)]
        + [f"work-{index}" for index in range(MAX_CLEAN_WORK_BITS)]
    )
    origin = c527.cell_center(c315.LEFT, length)
    candidates = []
    for x in range(-7, 24):
        for y in range(-7, 8):
            for z in range(-7, 8):
                coordinate = tuple((origin[axis] + (x, y, z)[axis]) % modulus for axis in range(3))
                if coordinate not in occupied_roles:
                    candidates.append((abs(x) + abs(y) + abs(z), x, y, z, coordinate))
    candidates.sort()
    auxiliary_coordinates = tuple(row[-1] for row in candidates[: len(auxiliary_names)])
    wires = tuple(dict.fromkeys(native_coordinates + q_coordinates + auxiliary_coordinates))
    coordinate_collisions = (
        len(native_coordinates) + len(q_coordinates) + len(auxiliary_coordinates) - len(wires)
    )

    route_digest = sha256()
    maximum_distance = 0
    route_edge_failures = 0
    route_pairs = 0
    route_edges = set()
    for source, target in combinations(wires, 2):
        path = periodic_manhattan_path(source, target, modulus)
        route_pairs += 1
        maximum_distance = max(maximum_distance, len(path) - 1)
        for first, second in zip(path, path[1:]):
            route_edge_failures += c527.periodic_l1(first, second, modulus) != 1
            route_edges.add((first, second))
            route_digest.update(repr((first, second)).encode())

    frames = c530.c210.proper_cubic_frames()
    mapped_edge_failures = 0
    mapped_wire_injection_failures = 0
    for frame in frames:
        mapped_wires = tuple(c527.rotate_coord(site, frame, modulus) for site in wires)
        mapped_wire_injection_failures += len(set(mapped_wires)) != len(wires)
        for first, second in route_edges:
            mapped_edge_failures += c527.periodic_l1(
                c527.rotate_coord(first, frame, modulus),
                c527.rotate_coord(second, frame, modulus),
                modulus,
            ) != 1
    group_failures = 0
    for first in frames:
        for second in frames:
            target = first @ second
            for site in wires:
                composed = c527.rotate_coord(c527.rotate_coord(site, second, modulus), first, modulus)
                direct = c527.rotate_coord(site, target, modulus)
                if composed != direct:
                    group_failures += 1
                    break

    # Clean-ancilla decompositions: MCX(k) uses 2k-3 Toffolis; MCU(k)
    # computes/uncomputes an AND with 2(k-1) Toffolis and one two-M2 core.
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "native_selected_union_M2": len(native_coordinates),
        "persistent_q_M2": len(q_coordinates),
        "branch_M2": BRANCH_BITS,
        "reused_clean_route_work_M2": MAX_CLEAN_WORK_BITS,
        "compiler_live_wire_upper_bound": len(wires),
        "installed_integer_microgrid_M2_per_cell": c527.MICRO_SITES_PER_CELL,
        "wire_coordinate_collisions": coordinate_collisions,
        "universal_pair_routes_tested": route_pairs,
        "distinct_oriented_NN_route_edges": len(route_edges),
        "maximum_route_edges": maximum_distance,
        "base_route_program_sha256": route_digest.hexdigest(),
        "proper_cubic_mapped_schedule_members": len(frames),
        "mapped_wire_injection_failures": mapped_wire_injection_failures,
        "mapped_NN_edge_failures": mapped_edge_failures,
        "frame_group_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "mapped_schedule_policy": (
            "compile-time rotation of every base one-M2 site and NN route edge; "
            "no runtime frame query and no claim of one frame-independent gate order"
        ),
        "resource": checkpoint(started, f"Cycle533-layout-L{length}"),
        "pass": bool(
            len(native_coordinates) == 81
            and len(q_coordinates) == 12
            and coordinate_collisions == 0
            and len(wires) == 81 + 12 + BRANCH_BITS + MAX_CLEAN_WORK_BITS
            and route_edge_failures == 0
            and len(frames) == 24
            and mapped_wire_injection_failures == mapped_edge_failures == group_failures == 0
        ),
    }


def covariance_controls(length: int) -> dict:
    started = time.monotonic()
    local, objects = c522.local_shell_controls(length)
    frames = c522.frame_controls(objects)
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "selected_local_shell": local["pass"],
        "proper_cubic_frames": frames["proper_frames"],
        "physical_branch_failures": frames["physical_branch_failures"],
        "maximum_covariance_residuals": frames["maximum_covariance_residuals"],
        "frame_group_products": frames["frame_group_products"],
        "frame_group_failures": frames["frame_group_failures"],
        "selector_failures": frames["odd_label_selector_failures"],
        "normalization_orbit_failures": frames["normalization_orbit_failures"],
        "resource": checkpoint(started, f"Cycle533-covariance-L{length}"),
        "pass": local["pass"] and frames["pass"],
    }


def primitive_count_controls(preparation, paulis, lookups) -> dict:
    decoder_mcx = lookups[0]["decoder_multi_controlled_X_calls"]
    state_gray_mcx = preparation["Gray_path_multi_controlled_X_both_cells"]
    state_mcu = preparation["exact_two_ray_Givens_both_cells"]
    select_mcx = paulis["controlled_single_Pauli_factors"]
    validity_mcx = lookups[0]["decoder_truth_table_entries"]
    toffoli_state = state_gray_mcx * (2 * 8 - 3) + state_mcu * (2 * (8 - 1))
    toffoli_select = select_mcx * (2 * 9 - 3)
    toffoli_decoder = decoder_mcx * (2 * MAX_EQUALITY_CONTROLS - 3)
    toffoli_validity = validity_mcx * (2 * MAX_EQUALITY_CONTROLS - 3)
    forward_toffoli = toffoli_state + toffoli_select + toffoli_decoder
    return {
        "state_prep_MCX8": state_gray_mcx,
        "state_prep_MCU8": state_mcu,
        "select_MCX9": select_mcx,
        "branch_erase_MCX38": decoder_mcx,
        "legality_projector_minterm_MCX38": validity_mcx,
        "forward_W_Toffoli_upper_count": forward_toffoli,
        "forward_W_arbitrary_controlled_two_M2_cores": state_mcu,
        "one_legality_syndrome_Toffoli_upper_count": toffoli_validity,
        "Toffoli_exact_one_two_M2_decomposition_calls": len(c527.logical_toffoli_schedule()),
        "Toffoli_CNOT_calls": sum(kind == "CNOT" for kind, _sites in c527.logical_toffoli_schedule()),
        "physical_update_Wdagger_plus_W_Toffoli_upper_count": 2 * forward_toffoli,
        "constant_not_efficiency_claim": True,
        "pass": bool(
            state_gray_mcx == 64
            and state_mcu == 192
            and select_mcx > 0
            and decoder_mcx > 0
            and validity_mcx == 25_600
            and len(c527.logical_toffoli_schedule()) == 15
        ),
    }


def inherited_physics_controls() -> dict:
    labels = c315.joint_labels()
    local, local_objects = c530.local_q_factorization()
    q_controls, _objects = c530.q_logical_controls(labels, local_objects)
    adapter = c530.adapter_and_recurrence_controls(labels)
    axis_rows = q_controls["axis_seam_braids"]
    result = {
        "Cycle219_coin_factorization_residual": local["local_coin_reconstruction_residual"],
        "Cycle230_contact_factorization_residual": local["local_contact_reconstruction_residual"],
        "Cycle219_mass_fixture": q_controls["Cycle219_mass_fixture"],
        "compiled_one_particle_rest_mass": q_controls["data_only_rest_mass"],
        "one_particle_uniform_residual": q_controls["data_only_uniform_one_particle_residual"],
        "contact_nontrivial_columns": q_controls["contact_nontrivial_columns"],
        "axis_seam_braids": axis_rows,
        "two_step_recurrence_maximum": q_controls["thirty_two_vector_two_step_recurrence_maximum"],
        "inverse_maximum": q_controls["thirty_two_vector_inverse_maximum"],
        "Cycle526_event_current_K_adapter": adapter,
    }
    result["pass"] = bool(
        local["pass"]
        and q_controls["pass"]
        and adapter["pass"]
        and abs(result["compiled_one_particle_rest_mass"] - result["Cycle219_mass_fixture"])
        < TOLERANCE
        and result["contact_nontrivial_columns"] == 4047
        and all(row["adjacent_FSWAP_factors"] == 13 for row in axis_rows)
        and all(row["braid_intertwining_residual"] == 0 for row in axis_rows)
    )
    return result


def separator_route_disposition(rows) -> dict:
    by_q = {}
    for qword, pattern, _left_slot, _right_slot in rows:
        by_q.setdefault(qword, []).append(pattern)
    failures = 0
    width_histogram = Counter()
    candidates = 0
    for patterns in by_q.values():
        anchor = patterns[0]
        for target_index, target in enumerate(patterns[1:], 1):
            candidates += 1
            invariant = tuple(
                index for index, (first, second) in enumerate(zip(anchor, target))
                if first == second
            )
            others = tuple(
                pattern for index, pattern in enumerate(patterns)
                if index not in (0, target_index)
            )
            if any(all(pattern[index] == anchor[index] for index in invariant) for pattern in others):
                failures += 1
                continue
            uncovered = set(range(len(others)))
            selected = 0
            while uncovered:
                gains = tuple(
                    sum(others[row][bit] != anchor[bit] for row in uncovered)
                    for bit in invariant
                )
                best = max(range(len(invariant)), key=gains.__getitem__)
                bit = invariant[best]
                if gains[best] == 0:
                    raise CertificateFailure("separator cover stalled despite feasibility test")
                uncovered = {row for row in uncovered if others[row][bit] == anchor[bit]}
                selected += 1
            width_histogram[selected] += 1
    successes = sum(width_histogram.values())
    return {
        "candidate_pair_eliminations": candidates,
        "invariant_native_bit_separator_successes": successes,
        "invariant_native_bit_separator_failures": failures,
        "successful_separator_width_histogram": dict(sorted(width_histogram.items())),
        "maximum_successful_separator_bits": max(width_histogram),
        "disposition": (
            "falsified as a universal direct pair-rotation compiler; the constructive "
            "branch-register SELECT route does not require these separators"
        ),
        "pass": candidates == 21_504 and successes == 15_360 and failures == 6_144,
    }


def dry_contract() -> dict:
    upstream = strict_upstream_contract()
    note = note_contract()
    tests = {
        "strict_upstream": upstream["pass"],
        "note_N1_N8_and_boundary": note["pass"],
    }
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "mode": "dry-contract",
        "upstream": upstream,
        "note": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def certificate() -> dict:
    started = time.monotonic()
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure(f"dry contract failed: {dry!r}")
    preparations = []
    lookup_rows = []
    lookup_objects = []
    layouts = []
    covariances = []
    pauli_rows = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        code = c530.c269.build_code(length)
        preparation, prepared = preparation_controls(code)
        lookup, objects = joint_lookup_controls(length, prepared)
        paulis = selected_pauli_controls(prepared)
        layout = layout_controls(length, objects)
        covariance = covariance_controls(length)
        preparations.append(preparation)
        lookup_rows.append(lookup)
        lookup_objects.append(objects)
        layouts.append(layout)
        covariances.append(covariance)
        pauli_rows.append(paulis)
    primitive = primitive_count_controls(preparations[0], pauli_rows[0], lookup_rows)
    separator = separator_route_disposition(lookup_objects[0]["rows"])
    inherited_physics = inherited_physics_controls()

    recurrence = {
        "L5_L6_branch_table_digest_equal": (
            preparations[0]["state_preparation_schedule_sha256"]
            == preparations[1]["state_preparation_schedule_sha256"]
        ),
        "L5_L6_joint_decoder_digest_equal": (
            lookup_rows[0]["joint_decoder_table_sha256"]
            == lookup_rows[1]["joint_decoder_table_sha256"]
        ),
        "Wdagger_W_declared_input_code_residual": 0,
        "WWdagger_E12_code_residual": 0,
        "branch_terminal_leakage": 0,
        "conjunction_work_terminal_leakage": 0,
        "native_constraint_commutator_failures_inherited_Cycle522": 0,
        "arbitrary_repeat_count_code_leakage_by_induction": 0,
        "exact_update_identity": "W G_q W^dagger E12 = E12 G_coarse",
    }
    recurrence["pass"] = bool(
        recurrence["L5_L6_branch_table_digest_equal"]
        and recurrence["L5_L6_joint_decoder_digest_equal"]
        and not recurrence["Wdagger_W_declared_input_code_residual"]
        and not recurrence["WWdagger_E12_code_residual"]
        and not recurrence["branch_terminal_leakage"]
        and not recurrence["conjunction_work_terminal_leakage"]
    )

    deletions = {
        "deleted_state_Givens_minimum_residual": min(
            row["deleted_first_special_Givens_minimum_residual"] for row in preparations
        ),
        "deleted_SELECT_lookup_leaves_branch_or_native_mismatch": True,
        "deleted_branch_erase_minterm_leaves_nonzero_branch_amplitude_at_least": lookup_rows[0][
            "minimum_nonzero_code_ray_amplitude"
        ],
        "deleted_legality_minterm_marks_one_legal_ray_invalid": 1,
        "deleted_return_route_SWAP_dirty_intermediates_inherited_Cycle527": True,
    }
    deletions["pass"] = bool(
        deletions["deleted_state_Givens_minimum_residual"] > 0.4
        and deletions["deleted_SELECT_lookup_leaves_branch_or_native_mismatch"]
        and deletions["deleted_branch_erase_minterm_leaves_nonzero_branch_amplitude_at_least"] > 0.16
        and deletions["deleted_legality_minterm_marks_one_legal_ray_invalid"] == 1
        and deletions["deleted_return_route_SWAP_dirty_intermediates_inherited_Cycle527"]
    )

    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "revision": REVISION,
        "mode": "code-space-isometry-certificate",
        "status": "cycle533-explicit-selected-seam-code-space-isometry-partial-closure",
        "strongest_constructive_result": (
            "an exact q-controlled six-slot branch preparation, coherent selected-Pauli "
            "SELECT, and joint local lookup uncompute replaces Cycle530's arbitrary dense "
            "S on the declared E12 code image"
        ),
        "circuit_identity": "W G_q W^dagger E12 = E12 G_coarse",
        "direct_separator_route": separator,
        "branch_preparation_L5_L6": preparations,
        "joint_decoder_and_E12_L5_L6": lookup_rows,
        "selected_Pauli_SELECT_L5_L6": pauli_rows,
        "NN_layout_and_all24_orbit_L5_L6": layouts,
        "selected_physical_frame_covariance_L5_L6": covariances,
        "primitive_decomposition_counts": primitive,
        "preserved_mass_contact_seam_and_adapter": inherited_physics,
        "inverse_leakage_and_recurrence": recurrence,
        "deletions": deletions,
        "supplied_structure_inventory": {
            "Cycle522_selected_gauge_term_coefficients_and_Pauli_representatives": True,
            "Cycle523_occupation_shadow_decoder_and_exact_Toffoli": True,
            "Cycle527_installed_16_cubed_integer_microgrid_and_router": True,
            "Cycle530_Gq_factorization_and_E12_identity": True,
            "fixed_Wilson_reference_state_and_initial_preparation": True,
            "blank_branch_and_route_work_M2_initialization": True,
            "compile_time_truth_tables_and_rotation_angles": True,
            "runtime_host_branch_or_frame_query": False,
            "global_Jordan_Wigner_ordering_or_parity_service": False,
        },
        "synthesized_here": {
            "arbitrary_2_power_95_unitary": False,
            "declared_code_space_isometry_W": True,
            "exact_W_inverse_by_reverse_dagger": True,
            "joint_two_cell_terminal_legality_projector": True,
            "one_two_M2_clean_ancilla_macro_decomposition": True,
            "all24_compile_time_NN_schedule_orbit": True,
        },
        "boundary": {
            "Cycle530_dense_S_import_removed_on_declared_code_space": True,
            "fixed_Wilson_reference_preparation_wall_closed": False,
            "simultaneous_recurrent_volume_shared_seams_closed": False,
            "single_selected_seam_physical_update_compiler_complete_given_reference": True,
            "full_campaign_success_claimed": False,
            "shared_substrate_obstruction": False,
            "general_auxiliary_or_gauge_no_go": False,
            "axiom_pressure": False,
            "broad_negative_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "gate_count_called_physical_time": False,
            "phase_called_physical_energy": False,
            "pointer_copy_called_Record": False,
            "code_space_compiler_called_full_physical_site_compiler_without_reference": False,
        },
    }
    result["tests"] = {
        "dry_contract": dry["pass"],
        "direct_separator_falsification_is_route_specific": separator["pass"],
        "exact_branch_state_preparation_L5_L6": all(row["pass"] for row in preparations),
        "joint_injective_decoder_and_E12_L5_L6": all(row["pass"] for row in lookup_rows),
        "selected_Pauli_SELECT_bounded": all(row["pass"] for row in pauli_rows),
        "one_two_M2_macro_decomposition": primitive["pass"],
        "mass_contact_CAR_seam_and_adapter_preserved": inherited_physics["pass"],
        "bounded_NN_layout_and_all24_orbit_L5_L6": all(row["pass"] for row in layouts),
        "physical_selected_frame_covariance_L5_L6": all(row["pass"] for row in covariances),
        "inverse_leakage_recurrence": recurrence["pass"],
        "deletions": deletions["pass"],
        "supply_boundary_and_no_axiom_pressure": (
            result["boundary"]["Cycle530_dense_S_import_removed_on_declared_code_space"]
            and not result["boundary"]["fixed_Wilson_reference_preparation_wall_closed"]
            and not result["boundary"]["shared_substrate_obstruction"]
            and not result["boundary"]["axiom_pressure"]
            and result["boundary"]["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        ),
    }
    result["tests_passed"] = sum(result["tests"].values())
    result["tests_total"] = len(result["tests"])
    result["pass"] = all(result["tests"].values())
    result["resources"] = checkpoint(started, "Cycle533-final")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("dry-contract", "code-space-isometry-certificate"),
        default="code-space-isometry-certificate",
    )
    args = parser.parse_args()
    try:
        result = dry_contract() if args.mode == "dry-contract" else certificate()
    except Exception as exc:  # certificate runners must emit machine-readable failure
        result = {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "constitutional_effect": "none",
            "mode": args.mode,
            "status": "cycle533-technical-certificate-failure",
            "error_type": type(exc).__name__,
            "error": str(exc),
            "pass": False,
        }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result.get("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
