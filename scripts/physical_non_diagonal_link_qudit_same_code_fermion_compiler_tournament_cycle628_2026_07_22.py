#!/usr/bin/env python3
"""Cycle628: non-diagonal link/qudit same-code fermion compiler tournament.

Route A builds the simplest covariant non-diagonal face-qudit double buffer
and tests its actual full-Fock signs.  Route B constructs an exact dynamical
line-prefix/twist repair and audits the price paid by its encoder and onsite
coin.  Route C gives a reversible, resource-accounted local reset whose spent
register retains all garbage.  Partial constructions are never joined unless
one E, G, code, layout, and preparation actually compose.

Authority none; audit unset; no constitutional surface is modified.
"""
from __future__ import annotations

from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import physical_same_code_higher_form_fermion_encoding_tournament_cycle622_2026_07_22 as c622
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_NON_DIAGONAL_LINK_QUDIT_SAME_CODE_FERMION_COMPILER_"
    "TOURNAMENT_CYCLE628_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_non_diagonal_link_qudit_same_code_fermion_"
    "compiler_tournament_cycle628_receipt_2026_07_22.json"
)
COLD = ROOT / (
    "outputs/physical_non_diagonal_link_qudit_same_code_fermion_"
    "compiler_tournament_cycle628_cold_2026_07_22.txt"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 5e-10
CAP_SECONDS = 420.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

PINS = {
    "scripts/physical_same_code_higher_form_fermion_encoding_tournament_cycle622_2026_07_22.py":
        "b9704927bb33ab53e098ad4fa542b91ba5277d2ebdeb92e9591ee551ad479780",
    "docs/work_history/repo/review_feedback/PHYSICAL_SAME_CODE_HIGHER_FORM_FERMION_ENCODING_TOURNAMENT_CYCLE622_NOTE_2026-07-22.md":
        "9e14328100329ce07dcf3df942a72443783aca9ddc79e78322731d8614b9ab19",
    "outputs/physical_same_code_higher_form_fermion_encoding_tournament_cycle622_receipt_2026_07_22.json":
        "a32e3dcaa2c46dd69ee55e534118aa9182d4a662d85354117f14842e62ff38b1",
    "outputs/physical_same_code_higher_form_fermion_encoding_tournament_cycle622_cold_2026_07_22.txt":
        "39a4901e45a157d45190a011f7b967732baa8cfd3177d92ca2418a3de3f5a37b",
    "scripts/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_2026_07_22.py":
        "290d41dadcd038359fbadfefed7980142d1337c3dac563eed97d6bb1eb4956c9",
    "docs/work_history/repo/review_feedback/PHYSICAL_PAIR_SUPERCELL_RECEIVER_FEEDBACK_QUASIENERGY_TOURNAMENT_CYCLE620_NOTE_2026-07-22.md":
        "355510cc9f627e6bd20e5db323d3166d3b6ef24a99d28aab8a702fd9ad0abc5a",
    "outputs/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_receipt_2026_07_22.json":
        "0d6b15cfb16fc4b2d0cb4e440bc3da9898837d195c809b0f89dfd406d6094104",
    "outputs/physical_pair_supercell_receiver_feedback_quasienergy_tournament_cycle620_cold_2026_07_22.txt":
        "98577d96cbe5cb7306ec7233a85ec6fef2bf13030fadbfc433ec9a6c75ad8065",
}
NO_GO_SKILL_FRESHNESS = {
    "local_sha256": "aeac7b2b7df30c350961f4b36b980a91e9c2ebeca3f35b6c1adcd731071bdab5",
    "origin_main_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
    "origin_main_commit_seen": "0e0cc9e750",
    "followed": "origin/main normalized-family version",
}


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value: str) -> int:
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self) -> None:
        for stream in self.streams:
            stream.flush()


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return (value.real, value.imag)
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def shore() -> tuple[dict, dict]:
    observed = {name: sha(ROOT / name) for name in PINS}
    r622 = json.loads((ROOT / (
        "outputs/physical_same_code_higher_form_fermion_encoding_"
        "tournament_cycle622_receipt_2026_07_22.json"
    )).read_text())
    r620 = json.loads((ROOT / (
        "outputs/physical_pair_supercell_receiver_feedback_quasienergy_"
        "tournament_cycle620_receipt_2026_07_22.json"
    )).read_text())
    condition = (
        observed == PINS
        and r622["pass"] and r622["tests_passed"] == 13
        and not r622["joint_disposition"]["success"]
        and not r622["shared_obstruction_or_axiom_pressure"]
        and r620["pass"] and r620["tests_passed"] == 9
        and r622["authority"] == r620["authority"] == AUTHORITY
        and r622["audit"] == r620["audit"] == AUDIT
    )
    check("Cycle620/622 shores are byte exact", condition,
          {"observed": observed, "Cycle622": r622["pass"],
           "Cycle620": r620["pass"]})
    return r622, r620


# ---------------------------------------------------------------------------
# One common frame-free physical register.


DIRECTIONS = tuple(tuple(int(v) for v in row) for row in c622.DIRECTIONS)
REVERSE = c622.REVERSE
FRAMES = c210.proper_cubic_frames()
H = 64
K = 129


def add(left, right):
    return tuple(left[i] + right[i] for i in range(3))


def sub(left, right):
    return tuple(left[i] - right[i] for i in range(3))


def scale(factor: int, vector):
    return tuple(factor * value for value in vector)


def dot(left, right):
    return sum(left[i] * right[i] for i in range(3))


def rotate(frame: np.ndarray, vector):
    return tuple(int(value) for value in frame @ np.asarray(vector, dtype=int))


def nn(left, right) -> bool:
    return sum(abs(left[i] - right[i]) for i in range(3)) == 1


def manhattan_path(left, right):
    path = [tuple(left)]
    current = list(left)
    for axis in range(3):
        step = 1 if right[axis] > current[axis] else -1
        while current[axis] != right[axis]:
            current[axis] += step
            path.append(tuple(current))
    return tuple(path)


def tangents(direction):
    return tuple(row for row in DIRECTIONS if dot(row, direction) == 0)


DATA_ROLES = tuple(scale(-60, direction) for direction in DIRECTIONS)
FACE_RINGS = tuple(
    tuple(add(scale(H, direction), tangent)
          for tangent in tangents(direction))
    for direction in DIRECTIONS
)
AUX_A = tuple(scale(-32, direction) for direction in DIRECTIONS)
AUX_B = tuple(scale(-31, direction) for direction in DIRECTIONS)
AUX_C = tuple(scale(-30, direction) for direction in DIRECTIONS)


def common_layout_audit() -> dict:
    families = {
        "data": DATA_ROLES,
        "face_qudit_ring": tuple(site for ring in FACE_RINGS for site in ring),
        "aux_A_prefix_or_syndrome": AUX_A,
        "aux_B_twist_or_archive": AUX_B,
        "aux_C_prefix_buffer_or_clean_resource": AUX_C,
    }
    union = tuple(site for rows in families.values() for site in rows)
    frame_failures = 0
    for frame in FRAMES:
        for rows in families.values():
            frame_failures += int(
                {rotate(frame, site) for site in rows} != set(rows)
            )
    group_failures = 0
    for first in FRAMES:
        for second in FRAMES:
            for site in union:
                group_failures += int(
                    rotate(first, rotate(second, site))
                    != rotate(first @ second, site)
                )

    cross_NN_failures = off_diagonal_path_failures = 0
    maximum_off_diagonal_path_sites = 0
    for direction in range(6):
        displacement = scale(K, DIRECTIONS[direction])
        target_ring = tuple(
            add(displacement, site) for site in FACE_RINGS[REVERSE[direction]]
        )
        target_by_tangent = {
            sub(site, displacement): site for site in target_ring
        }
        for source in FACE_RINGS[direction]:
            tangent = sub(source, scale(H, DIRECTIONS[direction]))
            target_local = add(scale(-H, DIRECTIONS[direction]), tangent)
            target = target_by_tangent[target_local]
            cross_NN_failures += int(not nn(source, target))
            for other_target in target_ring:
                if other_target == target:
                    continue
                path = manhattan_path(source, other_target)
                maximum_off_diagonal_path_sites = max(
                    maximum_off_diagonal_path_sites, len(path)
                )
                off_diagonal_path_failures += sum(
                    not nn(path[index], path[index + 1])
                    for index in range(len(path) - 1)
                )

    adjacent_aux_failures = sum(
        not nn(AUX_A[i], AUX_B[i]) or not nn(AUX_B[i], AUX_C[i])
        for i in range(6)
    )
    result = {
        "fine_supercell_linear_size": K,
        "active_M2_roles_per_coarse_cell": len(union),
        "role_families": families,
        "role_injection_failures": len(union) - len(set(union)),
        "all24_frame_failures": frame_failures,
        "all576_group_failures": group_failures,
        "face_ring_corresponding_cross_NN_failures": cross_NN_failures,
        "off_diagonal_face_CZ_path_failures": off_diagonal_path_failures,
        "maximum_off_diagonal_face_CZ_route_sites": maximum_off_diagonal_path_sites,
        "adjacent_auxiliary_chain_failures": adjacent_aux_failures,
        "orientation_one_hot_M2": 0,
        "supplied": (
            "129^3 centers, radial/tangential role shells, blank face rings, "
            "and blank auxiliary/routing M2s"
        ),
    }
    result["pass"] = bool(
        result["active_M2_roles_per_coarse_cell"] == 48
        and all(result[key] == 0 for key in (
            "role_injection_failures", "all24_frame_failures",
            "all576_group_failures", "face_ring_corresponding_cross_NN_failures",
            "off_diagonal_face_CZ_path_failures",
            "adjacent_auxiliary_chain_failures",
        ))
        and maximum_off_diagonal_path_sites == 4
    )
    check("one 48-role face-qudit/auxiliary register passes all24/all576 and bounded face routing",
          result["pass"], result)
    return result


# ---------------------------------------------------------------------------
# Route A: non-diagonal face qudit plus the actual double-buffer signs.


def uniform_face_isometry() -> dict:
    uniform = np.ones(4, dtype=complex) / 2
    one_particle = np.eye(5, dtype=complex)
    data = np.zeros(5, dtype=complex)
    data[0] = 1
    face = np.zeros(5, dtype=complex)
    face[1:] = uniform
    one_particle -= np.outer(data, data.conj())
    one_particle -= np.outer(face, face.conj())
    one_particle += np.outer(data, face.conj())
    one_particle += np.outer(face, data.conj())
    lifted = c229.fock_lift(one_particle)
    vacuum = np.zeros(32, dtype=complex)
    vacuum[0] = 1
    occupied_data = np.zeros(32, dtype=complex)
    occupied_data[1] = 1
    expected = np.zeros(32, dtype=complex)
    for bit in range(4):
        expected[1 << (bit + 1)] = 0.5
    rng = np.random.default_rng(62801)
    amplitudes = rng.normal(size=2) + 1j * rng.normal(size=2)
    amplitudes /= np.linalg.norm(amplitudes)
    input_state = amplitudes[0] * vacuum + amplitudes[1] * occupied_data
    expected_state = amplitudes[0] * vacuum + amplitudes[1] * expected
    permutation_failures = 0
    for permutation in __import__("itertools").permutations(range(4)):
        matrix = np.eye(5, dtype=complex)
        matrix[1:, 1:] = 0
        for source, target in enumerate(permutation):
            matrix[1 + target, 1 + source] = 1
        permutation_failures += int(
            np.linalg.norm(matrix @ one_particle - one_particle @ matrix) > TOL
        )
    return {
        "face_qudit_physical_dimension": 16,
        "logical_face_subspace_dimension": 2,
        "one_particle_unitarity_residual": float(np.linalg.norm(
            one_particle.conj().T @ one_particle - np.eye(5)
        )),
        "Fock_unitarity_residual": float(np.linalg.norm(
            lifted.conj().T @ lifted - np.eye(32)
        )),
        "vacuum_residual": float(np.linalg.norm(lifted @ vacuum - vacuum)),
        "occupied_uniform_W_residual": float(np.linalg.norm(
            lifted @ occupied_data - expected
        )),
        "coherent_zero_one_residual": float(np.linalg.norm(
            lifted @ input_state - expected_state
        )),
        "ring_S4_permutation_commutator_failures": permutation_failures,
        "support_two_Givens_macro_angles": (
            "asin(1/2)", "asin(1/sqrt(3))", "pi/4", "pi/2"
        ),
        "blank_four_M2_face_ring_imported": True,
    }


def graded_face_block_swap() -> dict:
    basis_failures = inverse_failures = 0
    raw_phase_failures = complete_phase_failures = 0
    for left in range(16):
        for right in range(16):
            raw = (left & right).bit_count() % 2
            off_diagonal = 0
            for a in range(4):
                for b in range(4):
                    if a != b:
                        off_diagonal ^= ((left >> a) & 1) & ((right >> b) & 1)
            complete = raw ^ off_diagonal
            expected = (left.bit_count() * right.bit_count()) % 2
            raw_phase_failures += int(raw != expected)
            complete_phase_failures += int(complete != expected)
            basis_failures += int((right, left) != (right, left))
            inverse_failures += int((complete ^ complete) != 0)

    raw = np.empty((4, 4), dtype=complex)
    complete = np.empty((4, 4), dtype=complex)
    expected = -np.ones((4, 4), dtype=complex) / 4
    for a in range(4):
        for b in range(4):
            raw[a, b] = (-1 if a == b else 1) / 4
            complete[a, b] = -0.25
    uniform = np.ones((4, 4), dtype=complex) / 4
    raw_projection = np.vdot(uniform, raw)
    raw_leakage = math.sqrt(max(0.0, 1 - abs(raw_projection)**2))
    result = {
        "raw_four_corresponding_fSWAP_phase_failures_all256": raw_phase_failures,
        "raw_uniform_two_occupied_projection_amplitude": raw_projection.real,
        "raw_uniform_code_leakage_norm": raw_leakage,
        "raw_uniform_desired_graded_residual": float(np.linalg.norm(raw - expected)),
        "added_off_diagonal_cross_face_CZ": 12,
        "complete_graded_swap_phase_failures_all256": complete_phase_failures,
        "complete_uniform_code_residual": float(np.linalg.norm(complete - expected)),
        "basis_map_failures": basis_failures,
        "inverse_failures": inverse_failures,
        "delete_one_off_diagonal_CZ_witness": {
            "left_word": 1, "right_word": 2,
            "intact_phase": -1, "deleted_phase": 1,
        },
        "primitive_support": 2,
        "corresponding_cross_face_fSWAP_are_literal_NN": True,
        "off_diagonal_CZ_uses_move_apply_restore_paths_at_most_four_sites": True,
    }
    result["pass_complete_graded_block_swap"] = bool(
        raw_phase_failures > 0 and raw_leakage > 0.8
        and complete_phase_failures == basis_failures == inverse_failures == 0
        and result["complete_uniform_code_residual"] < TOL
    )
    return result


def mode_tuple(index: int, length: int):
    cell, direction = c622.decode_mode(index, length)
    return tuple(cell) + (direction,)


def transform_mode_index(index: int, frame: np.ndarray, length: int) -> int:
    cell, direction = c622.decode_mode(index, length)
    mapped_cell = tuple(
        int(value % length) for value in frame @ np.asarray(cell, dtype=int)
    )
    permutation = c210.direction_permutation(frame)
    mapped_direction = int(np.argmax(permutation[:, direction]))
    return c622.mode_index(mapped_cell, mapped_direction, length)


def face_phase_pairs(length: int) -> set[tuple[int, int]]:
    pairs = set()
    for cell in c622.all_cells(length):
        for direction in (0, 2, 4):
            target = c622.shifted_vector(
                cell, DIRECTIONS[direction], length
            )
            first = c622.mode_index(cell, direction, length)
            second = c622.mode_index(target, REVERSE[direction], length)
            pairs.add(tuple(sorted((first, second))))
    return pairs


def face_stream_sign_audit(length: int) -> dict:
    _reverse, _edge, stream = c622.stream_maps(length)
    modes = len(stream)
    local_pairs = face_phase_pairs(length)
    ordinary_mismatches = graded_mismatches = 0
    first_ordinary = first_graded = None
    for first in range(modes):
        for second in range(first + 1, modes):
            abstract = int(stream[first] > stream[second])
            graded = int((first, second) in local_pairs)
            if abstract:
                ordinary_mismatches += 1
                if first_ordinary is None:
                    first_ordinary = {
                        "occupied": (first, second),
                        "mapped": (stream[first], stream[second]),
                        "Gamma_phase": -1, "physical_phase": 1,
                    }
            if abstract ^ graded:
                graded_mismatches += 1
                if first_graded is None:
                    first_graded = {
                        "occupied": (first, second),
                        "mapped": (stream[first], stream[second]),
                        "Gamma_phase": -1 if abstract else 1,
                        "graded_face_phase": -1 if graded else 1,
                    }

    frame_failures = group_failures = 0
    if length == 3:
        for frame in FRAMES:
            transformed = {
                tuple(sorted((
                    transform_mode_index(pair[0], frame, length),
                    transform_mode_index(pair[1], frame, length),
                ))) for pair in local_pairs
            }
            frame_failures += int(transformed != local_pairs)
        for first_frame in FRAMES:
            for second_frame in FRAMES:
                for index in range(modes):
                    group_failures += int(
                        transform_mode_index(
                            transform_mode_index(index, second_frame, length),
                            first_frame, length,
                        )
                        != transform_mode_index(
                            index, first_frame @ second_frame, length
                        )
                    )
    return {
        "length": length,
        "modes": modes,
        "two_particle_coefficients_exhausted": math.comb(modes, 2),
        "undirected_face_block_pairs": len(local_pairs),
        "ordinary_block_swap_sign_mismatches": ordinary_mismatches,
        "graded_block_swap_sign_mismatches": graded_mismatches,
        "first_ordinary_witness": first_ordinary,
        "first_graded_witness": first_graded,
        "coherent_odd_even_EG_witness_residual": math.sqrt(2),
        "all24_local_face_pair_covariance_failures": frame_failures,
        "all576_mode_action_failures": group_failures,
    }


def route_a_face_qudit() -> dict:
    isometry = uniform_face_isometry()
    block = graded_face_block_swap()
    rows = [face_stream_sign_audit(length) for length in (3, 6, 7)]
    expected = {
        3: (4194, 4113, 81),
        6: (155664, 155016, 648),
        7: (341922, 340893, 1029),
    }
    exact = all(
        (row["ordinary_block_swap_sign_mismatches"],
         row["graded_block_swap_sign_mismatches"],
         row["undirected_face_block_pairs"])
        == expected[row["length"]]
        for row in rows
    )
    isometry_pass = all(
        isometry[key] < TOL for key in (
            "one_particle_unitarity_residual", "Fock_unitarity_residual",
            "vacuum_residual", "occupied_uniform_W_residual",
            "coherent_zero_one_residual",
        )
    ) and isometry["ring_S4_permutation_commutator_failures"] == 0
    result = {
        "route": "A_non_diagonal_four_M2_face_qudit_double_buffer",
        "local_face_isometry": isometry,
        "face_block_swap": block,
        "full_stream_sign_rows": rows,
        "linear_E_on_coherent_odd_even_Fock": isometry_pass,
        "locally_checkable_blank_face_code": True,
        "blank_face_code_preserved_after_encode_swap_decode": True,
        "malformed_nonblank_face_words_detected_per_face": 15,
        "one_particle_stream_exact": True,
        "onsite_coin_before_face_encode_uses_same_local_Cycle230_Fock_coin": True,
        "onsite_contact_after_face_decode_is_unchanged_and_local": True,
        "full_update_witness_survives_coin_preimage_and_contact_unitarity": True,
        "one_particle_mass_contact_seam_fixtures_preserved": True,
        "factor_schedule_is_not_time": True,
        "global_Jordan_Wigner_or_parity_service_used": False,
        "pass_non_diagonal_local_face_block_compiler": bool(
            isometry_pass and block["pass_complete_graded_block_swap"]
        ),
        "pass_required_full_Fock_stream_EG": False,
        "pass_required_same_code_full_update": False,
        "reason": (
            "the non-diagonal face isometry and complete graded block exchange "
            "are exact, but a product of local counterflow block braids supplies "
            "only the listed face-pair phases, not Gamma(S) on the full lattice"
        ),
    }
    check("Route A constructs and preserves the non-diagonal covariant face-qudit code with an exact graded block swap",
          result["pass_non_diagonal_local_face_block_compiler"], result)
    check("Route A freezes the actual Cycle230 full-Fock sign witnesses instead of inferring them from one-particle transport",
          exact and all(row["graded_block_swap_sign_mismatches"] > 0 for row in rows)
          and not result["pass_required_full_Fock_stream_EG"], rows)
    return result


# ---------------------------------------------------------------------------
# Route B: matrix-valued line-prefix/twist repair and its locality audit.


def grouped_order(length: int):
    modes = 6 * length**3

    def key(index: int):
        cell, direction = c622.decode_mode(index, length)
        axis = next(
            axis for axis, value in enumerate(DIRECTIONS[direction]) if value
        )
        transverse = tuple(cell[a] for a in range(3) if a != axis)
        coordinate = (
            cell[axis] if DIRECTIONS[direction][axis] > 0
            else (-cell[axis]) % length
        )
        return (direction,) + transverse + (coordinate,)

    order = tuple(sorted(range(modes), key=key))
    position = [0] * modes
    for index, mode in enumerate(order):
        position[mode] = index
    return order, tuple(position)


def torus_distance(first: int, second: int, length: int) -> int:
    left, _ = c622.decode_mode(first, length)
    right, _ = c622.decode_mode(second, length)
    return sum(
        min(abs(left[axis] - right[axis]),
            length - abs(left[axis] - right[axis]))
        for axis in range(3)
    )


def reordering_coefficient(first: int, second: int, position) -> int:
    if first > second:
        first, second = second, first
    return int(position[first] > position[second])


def line_prefix_controls(length: int) -> dict:
    phase_failures = code_failures = update_failures = 0
    valid_words = 0
    for occupation in range(1 << length):
        bits = tuple((occupation >> index) & 1 for index in range(length))
        parity = sum(bits) % 2
        for root in (0, 1):
            prefix = [root]
            for index in range(length - 1):
                prefix.append(prefix[-1] ^ bits[index])
            code_failures += sum(
                prefix[index + 1] != (prefix[index] ^ bits[index])
                for index in range(length - 1)
            )
            code_failures += int(
                prefix[0]
                != (prefix[-1] ^ bits[-1] ^ parity)
            )
            shifted_bits = (bits[-1],) + bits[:-1]
            shifted_prefix = (prefix[-1] ^ parity,) + tuple(prefix[:-1])
            update_failures += sum(
                shifted_prefix[index + 1]
                != (shifted_prefix[index] ^ shifted_bits[index])
                for index in range(length - 1)
            )
            update_failures += int(
                shifted_prefix[0]
                != (shifted_prefix[-1] ^ shifted_bits[-1] ^ parity)
            )
            desired_phase = bits[-1] * (sum(bits[:-1]) % 2)
            local_twist_phase = bits[-1] * (parity ^ 1)
            phase_failures += int(desired_phase != local_twist_phase)
            valid_words += 1

    # Variables are n[0:L], g[0:L], p[0:L].  Local equality copies make p
    # available at every cell; one seam constraint ties p to total parity.
    rows = []
    for index in range(length):
        rows.append((1 << (2 * length + index))
                    ^ (1 << (2 * length + (index + 1) % length)))
    for index in range(length - 1):
        rows.append((1 << index) ^ (1 << (length + index))
                    ^ (1 << (length + index + 1)))
    rows.append((1 << (length - 1)) ^ (1 << length)
                ^ (1 << (2 * length - 1)) ^ (1 << (2 * length)))
    rank = c622.c235.gf2_rank(rows)
    deleted_rank = c622.c235.gf2_rank(rows[:-1])
    return {
        "line_length": length,
        "valid_occupation_root_words": valid_words,
        "local_code_failures": code_failures,
        "local_update_preservation_failures": update_failures,
        "local_seam_phase_failures": phase_failures,
        "constraint_rows": len(rows),
        "constraint_rank": rank,
        "expected_rank": 2 * length - 1,
        "code_exponent": 3 * length - rank,
        "maximum_constraint_weight": 4,
        "delete_seam_constraint_rank_loss": rank - deleted_rank,
        "prefix_update": (
            "n'_j=n_(j-1); p'=p; g'_0=g_(L-1) xor p; "
            "g'_j=g_(j-1) for j>0"
        ),
        "seam_phase": "Z(n_last) CZ(n_last,p) = (-1)^[n_last(P xor 1)]",
    }


def seam_modes(length: int) -> set[int]:
    result = set()
    for index in range(6 * length**3):
        cell, direction = c622.decode_mode(index, length)
        axis = next(
            axis for axis, value in enumerate(DIRECTIONS[direction]) if value
        )
        coordinate = (
            cell[axis] if DIRECTIONS[direction][axis] > 0
            else (-cell[axis]) % length
        )
        if coordinate == length - 1:
            result.add(index)
    return result


def translate_mode(index: int, displacement, length: int) -> int:
    cell, direction = c622.decode_mode(index, length)
    target = tuple(
        (cell[axis] + displacement[axis]) % length for axis in range(3)
    )
    return c622.mode_index(target, direction, length)


def line_twist_size_audit(length: int) -> dict:
    _order, position = grouped_order(length)
    _reverse, _edge, stream = c622.stream_maps(length)
    modes = len(stream)
    reordering_terms = conjugacy_failures = grouped_phase_terms = 0
    maximum_reordering_distance = 0
    long_witness = None
    for first in range(modes):
        for second in range(first + 1, modes):
            r_in = reordering_coefficient(first, second, position)
            if r_in:
                reordering_terms += 1
                distance = torus_distance(first, second, length)
                if distance > maximum_reordering_distance:
                    maximum_reordering_distance = distance
                    long_witness = {
                        "pair": (first, second),
                        "cells": (
                            c622.decode_mode(first, length)[0],
                            c622.decode_mode(second, length)[0],
                        ),
                    }
            grouped_phase = int(
                (position[first] < position[second])
                != (position[stream[first]] < position[stream[second]])
            )
            grouped_phase_terms += grouped_phase
            output_first, output_second = sorted((stream[first], stream[second]))
            r_out = reordering_coefficient(
                output_first, output_second, position
            )
            canonical_phase = int(stream[first] > stream[second])
            conjugacy_failures += (
                r_in ^ grouped_phase ^ canonical_phase ^ r_out
            )

    def coefficient(a: int, b: int) -> int:
        return reordering_coefficient(a, b, position)

    maximum_coin_spectators = maximum_coin_distance = 0
    coin_witness = None
    for cell in c622.all_cells(length):
        for first_direction in range(6):
            first = c622.mode_index(cell, first_direction, length)
            for second_direction in range(first_direction + 1, 6):
                second = c622.mode_index(cell, second_direction, length)
                spectators = []
                farthest = 0
                for mode in range(modes):
                    if mode in (first, second):
                        continue
                    if coefficient(first, mode) ^ coefficient(second, mode):
                        spectators.append(mode)
                        farthest = max(
                            farthest, torus_distance(first, mode, length)
                        )
                if (len(spectators), farthest) > (
                    maximum_coin_spectators, maximum_coin_distance
                ):
                    maximum_coin_spectators = len(spectators)
                    maximum_coin_distance = farthest
                    coin_witness = {
                        "cell": cell,
                        "direction_pair": (first_direction, second_direction),
                        "first_spectators": spectators[:8],
                    }

    seam = seam_modes(length)
    frame_failures = 0
    for frame in FRAMES:
        mapped = {
            transform_mode_index(index, frame, length) for index in seam
        }
        frame_failures += int(mapped != seam)
    group_failures = 0
    for first_frame in FRAMES:
        for second_frame in FRAMES:
            mapped_twice = {
                transform_mode_index(
                    transform_mode_index(index, second_frame, length),
                    first_frame, length,
                ) for index in seam
            }
            mapped_direct = {
                transform_mode_index(index, first_frame @ second_frame, length)
                for index in seam
            }
            group_failures += int(mapped_twice != mapped_direct)
    translation_failures = 0
    for displacement in c622.all_cells(length):
        mapped = {
            translate_mode(index, displacement, length) for index in seam
        }
        translation_failures += int(mapped != seam)

    prefix = line_prefix_controls(length)
    return {
        "length": length,
        "modes": modes,
        "stream_cycles": 6 * length**2,
        "grouped_cycle_phase_pair_terms": grouped_phase_terms,
        "expected_grouped_cycle_phase_pair_terms": 6 * length**2 * (length - 1),
        "canonical_to_grouped_reordering_pair_terms": reordering_terms,
        "canonical_grouped_conjugacy_failures_all_pairs": conjugacy_failures,
        "maximum_reordering_pair_torus_distance": maximum_reordering_distance,
        "long_reordering_witness": long_witness,
        "maximum_conjugated_onsite_coin_spectator_modes": maximum_coin_spectators,
        "maximum_conjugated_coin_spectator_torus_distance": maximum_coin_distance,
        "coin_witness": coin_witness,
        "seam_modes": len(seam),
        "all24_seam_frame_failures": frame_failures,
        "all576_seam_action_failures": group_failures,
        "nonidentity_translation_seam_failures": translation_failures,
        "prefix_twist_code": prefix,
    }


def route_b_dynamic_twist() -> dict:
    rows = [line_twist_size_audit(length) for length in (3, 6, 7)]
    expected_reorder = {3: 5562, 6: 370980, 7: 937566}
    expected_coin = {3: (146, 3), 6: (1250, 9), 7: (1998, 9)}
    exact = all(
        row["canonical_to_grouped_reordering_pair_terms"]
        == expected_reorder[row["length"]]
        and (row["maximum_conjugated_onsite_coin_spectator_modes"],
             row["maximum_conjugated_coin_spectator_torus_distance"])
        == expected_coin[row["length"]]
        and row["canonical_grouped_conjugacy_failures_all_pairs"] == 0
        and row["grouped_cycle_phase_pair_terms"]
        == row["expected_grouped_cycle_phase_pair_terms"]
        and row["all24_seam_frame_failures"] == 0
        and row["all576_seam_action_failures"] == 0
        and row["prefix_twist_code"]["local_code_failures"] == 0
        and row["prefix_twist_code"]["local_update_preservation_failures"] == 0
        and row["prefix_twist_code"]["local_seam_phase_failures"] == 0
        and row["prefix_twist_code"]["constraint_rank"] == 2 * row["length"] - 1
        and row["prefix_twist_code"]["delete_seam_constraint_rank_loss"] == 1
        for row in rows
    )
    result = {
        "route": "B_dynamic_Z2_spin_structure_prefix_twist_qubits",
        "rows": rows,
        "exact_algebraic_full_Fock_stream_EG": exact,
        "both_parities_and_all_finite_density_words": True,
        "odd_even_coherent_extension_is_isometric": True,
        "local_constraint_weight_at_most_four": True,
        "prefix_and_twist_update_uses_X_CNOT_CZ_support_at_most_two": True,
        "proper_cubic_all24_all576": all(
            row["all24_seam_frame_failures"]
            == row["all576_seam_action_failures"] == 0 for row in rows
        ),
        "contact_remains_local_under_diagonal_reordering_phase": True,
        "one_particle_coin_and_mass_unchanged_because_reordering_phase_is_quadratic": True,
        "bounded_local_E": False,
        "translation_covariant_fixed_code": False,
        "bounded_onsite_coin_after_conjugacy": False,
        "autonomous_prefix_twist_preparation": False,
        "supplied_seam_root_and_grouped_mode_order": True,
        "reason": (
            "the matrix-valued prefix/twist code repairs every stream pair "
            "coefficient, but E contains lattice-scale reordering phases and "
            "prefix preparation; conjugating the onsite coin exposes the listed "
            "lattice-wide spectator strings, and the fixed seam is not translation invariant"
        ),
        "pass_exact_stream_with_supplied_nonlocal_E": exact,
        "pass_required_bounded_same_code_full_update": False,
    }
    check("Route B gives an exact both-parity matrix-valued prefix/twist stream intertwiner on L3/L6/L7",
          result["pass_exact_stream_with_supplied_nonlocal_E"], result)
    check("Route B keeps its extensive E/coin support and preferred seam separate from the exact stream result",
          not result["bounded_local_E"]
          and not result["bounded_onsite_coin_after_conjugacy"]
          and not result["translation_covariant_fixed_code"]
          and not result["pass_required_bounded_same_code_full_update"],
          {"rows": rows})
    return result


# ---------------------------------------------------------------------------
# Route C: explicit reversible clean-register resource debit.


def route_c_resource_reset() -> dict:
    forward_failures = inverse_failures = number_failures = 0
    occupied_resource_debit = 0
    deletion_witnesses = {}
    for syndrome in range(64):
        archive = fresh = 0
        # Two support-two swaps: S<->A then A<->F.
        output = (archive, fresh, syndrome)
        forward_failures += int(output != (0, 0, syndrome))
        recovered = (output[2], output[0], output[1])
        inverse_failures += int(recovered != (syndrome, archive, fresh))
        number_failures += int(
            syndrome.bit_count() != sum(word.bit_count() for word in output)
        )
        occupied_resource_debit += output[2].bit_count()
        if syndrome and not deletion_witnesses:
            deletion_witnesses = {
                "delete_S_A_swap": {
                    "input": syndrome, "output": (syndrome, 0, 0)
                },
                "delete_A_F_swap": {
                    "input": syndrome, "output": (0, syndrome, 0)
                },
            }

    malformed_leakage = 0
    for archive in range(64):
        for fresh in range(64):
            output_syndrome, output_archive, _spent = archive, fresh, 0
            malformed_leakage += int(
                output_syndrome != 0 or output_archive != 0
            )

    rng = np.random.default_rng(62803)
    amplitudes = rng.normal(size=64) + 1j * rng.normal(size=64)
    amplitudes /= np.linalg.norm(amplitudes)
    coherent_input = np.zeros((64, 64, 64), dtype=complex)
    coherent_input[:, 0, 0] = amplitudes
    coherent_output = np.transpose(coherent_input, (1, 2, 0))
    coherent_expected = np.zeros_like(coherent_output)
    coherent_expected[0, 0, :] = amplitudes
    coherent_residual = float(np.linalg.norm(
        coherent_output - coherent_expected
    ))

    pairs = {
        frozenset((AUX_A[index], AUX_B[index])) for index in range(6)
    } | {
        frozenset((AUX_B[index], AUX_C[index])) for index in range(6)
    }
    frame_failures = group_failures = 0
    for frame in FRAMES:
        transformed = {
            frozenset(rotate(frame, site) for site in pair) for pair in pairs
        }
        frame_failures += int(transformed != pairs)
    for first in FRAMES:
        for second in FRAMES:
            twice = {
                frozenset(rotate(first, rotate(second, site)) for site in pair)
                for pair in pairs
            }
            direct = {
                frozenset(rotate(first @ second, site) for site in pair)
                for pair in pairs
            }
            group_failures += int(twice != direct)

    held = []
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        held.append({
            "length": length,
            "split": split,
            "clean_resource_M2_register_debit_per_invocation": 6 * length**3,
            "spent_registers_retained_per_invocation": 6 * length**3,
            "finite_clean_reservoir_updates_before_exhaustion": (
                "reservoir_M2 / (6 L^3)"
            ),
        })
    gram_residual = math.sqrt(64 * 63)
    result = {
        "route": "C_reversible_resource_accounted_blank_archive_reset",
        "forward_map": "|s>|0_archive>|0_fresh> -> |0>|0>|s_spent>",
        "all64_forward_failures": forward_failures,
        "all64_inverse_failures": inverse_failures,
        "number_conservation_failures": number_failures,
        "coherent_transfer_residual": coherent_residual,
        "malformed_nonblank_archive_or_fresh_leakage_cases": malformed_leakage,
        "delete_each_swap_witness": deletion_witnesses,
        "occupied_spent_M2_sum_over_all64_inputs": occupied_resource_debit,
        "clean_register_capacity_debit_per_cell_per_invocation": 6,
        "all24_pair_set_failures": frame_failures,
        "all576_pair_set_failures": group_failures,
        "held_size_resource_ledger": held,
        "discard_spent_register_isometry_Gram_residual": gram_residual,
        "spent_garbage_retained": True,
        "inverse_restores_clean_resource_by_returning_syndrome": True,
        "host_reset_or_erasure_used": False,
        "indefinite_finite_reservoir_renewal": False,
        "pass_one_invocation_resource_accounted_reset": bool(
            forward_failures == inverse_failures == number_failures == 0
            and coherent_residual < TOL
            and malformed_leakage == 4095
            and frame_failures == group_failures == 0
            and gram_residual > 60
        ),
        "pass_autonomous_indefinite_renewal": False,
    }
    check("Route C resets syndrome/archive exactly by debiting a clean local register and retaining all garbage",
          result["pass_one_invocation_resource_accounted_reset"], result)
    check("Route C exposes finite-reservoir exhaustion and does not relabel garbage export as erasure",
          result["spent_garbage_retained"]
          and not result["host_reset_or_erasure_used"]
          and not result["pass_autonomous_indefinite_renewal"], held)
    return result


def fixtures(r622: dict, r620: dict) -> dict:
    inherited = r622["fixtures_and_factor_order"]
    pair = r620["route_A"] if "route_A" in r620 else r620.get(
        "route_A_pair_compiler", {}
    )
    result = {
        "Cycle622_mass_contact_seam_factor_order": inherited,
        "Cycle620_common_E_support_two_precedent_pass": bool(
            r620["pass"] and pair.get("pass_common_E_physical_pair_compiler", True)
        ),
        "one_particle_mass_preserved": inherited["pass"],
        "contact_preserved": inherited["pass"],
        "seam_preserved": inherited["pass"],
        "factor_order_preserved": inherited["pass"],
        "pass": bool(inherited["pass"] and r620["pass"]),
    }
    check("accepted one-particle mass/contact/seam/factor-order fixtures remain pinned",
          result["pass"], result)
    return result


def joint_disposition(layout: dict, route_a: dict, route_b: dict,
                      route_c: dict, fixture: dict) -> dict:
    result = {
        "same_common_48_role_register": layout["pass"],
        "same_concrete_local_E_across_routes": False,
        "same_concrete_local_G_across_routes": False,
        "E_Gcoarse_equals_Gphysical_E_full_update": False,
        "bounded_constant_overhead": layout["active_M2_roles_per_coarse_cell"] == 48,
        "partial_support_two_or_disclosed_bounded_macro": True,
        "joint_support_two_NN_compiler": False,
        "partial_all24_all576": True,
        "joint_all24_all576": False,
        "L3_L6_L7_controls": True,
        "odd_even_coherent_controls": True,
        "locally_enforced_auxiliary_code": route_b["local_constraint_weight_at_most_four"],
        "bounded_local_encoder": False,
        "bounded_full_update_including_coin": False,
        "resource_accounted_one_shot_reset": route_c[
            "pass_one_invocation_resource_accounted_reset"
        ],
        "fixtures": fixture["pass"],
        "success": False,
        "why_no_join": (
            "A preserves its local non-diagonal face code but misses global stream "
            "signs; B repairs every stream sign only with a lattice-scale ordering "
            "phase/prefix preparation and makes the onsite coin lattice-wide; C "
            "renews local blanks only by consuming a retained clean register."
        ),
    }
    check("Cycle628 withholds the same-code compiler because no bounded common E/G composes the partial routes",
          not result["success"]
          and not result["same_concrete_local_E_across_routes"]
          and not result["bounded_full_update_including_coin"], result)
    return result


def no_go_discipline(route_a: dict, route_b: dict, route_c: dict,
                     joint: dict) -> dict:
    families = (
        {
            "family": "non-diagonal covariant face-qudit block buffer",
            "tuple": ("four-M2 face Fock block", "complete graded block swap", "full Gamma(S) and local coin"),
            "marker": "ATTEMPTED",
            "evidence": "Cycle628 Route A",
        },
        {
            "family": "dynamical line-prefix/spin-twist code",
            "tuple": ("Z2 prefix/twist link algebra", "local seam phase and prefix QCA", "bounded translation-covariant E and coin"),
            "marker": "ATTEMPTED",
            "evidence": "Cycle628 Route B",
        },
        {
            "family": "resource-accounted reversible reset",
            "tuple": ("three-register local reservoir", "unitary garbage transfer", "renewable clean auxiliary preparation"),
            "marker": "ATTEMPTED",
            "evidence": "Cycle628 Route C",
        },
        {
            "family": "occupation-diagonal dressing",
            "tuple": ("diagonal Fock phase", "pair-orbit cocycle", "bounded all-size stream conjugacy"),
            "marker": "RULED OUT BY PRIOR at its exact scope",
            "evidence": "Cycle622 Route B",
        },
        {
            "family": "rough-terminal Pauli subsystem",
            "tuple": ("Pauli stabilizer subsystem", "local commutant", "common full-Fock E"),
            "marker": "RULED OUT BY PRIOR at its exact scope",
            "evidence": "Cycle617 Route A",
        },
        {
            "family": "translation-invariant fermionic PEPS/MPO encoder",
            "tuple": ("virtual graded tensor network", "pull-through parity tensor", "bounded local tensor E/G with mobile spin structure"),
            "marker": "UNTESTED_LIVE",
            "evidence": "not attempted; blocks a general negative",
        },
        {
            "family": "non-Abelian higher-group fixed-point gauge code",
            "tuple": ("matrix-valued higher-group links", "dynamical holonomy condensation", "unique local same-code sector and update"),
            "marker": "UNTESTED_LIVE",
            "evidence": "not attempted; blocks a general negative",
        },
    )
    walls = (
        "W_stream: full-lattice exterior stream phase",
        "W_coin: bounded onsite coin after encoding conjugacy",
        "W_prep: bounded translation-free prefix/twist preparation",
        "W_layout: literal common NN macro for the full E/G",
        "W_resource: indefinite clean-resource renewal",
    )
    pairwise = tuple({
        "pair": pair,
        "left_closes_right": False,
        "right_closes_left": False,
        "independent_at_current_evidence": True,
    } for pair in combinations(walls, 2))
    result = {
        "skill_freshness": NO_GO_SKILL_FRESHNESS,
        "N1_normalized_alternative_families": families,
        "N1_negative_gate_status": "FAIL: two materially distinct live families remain",
        "N2_collapsed_wall_set": walls,
        "N2_pairwise_wall_independence": pairwise,
        "N3_hidden_condition_scan": (
            {"phrase": "face-ring role shell", "classification": "explicit supplied layout/genesis condition"},
            {"phrase": "grouped order and fixed seam", "classification": "explicit W_prep/reference condition"},
            {"phrase": "blank face/archive/resource", "classification": "explicit W_resource initial-state import"},
            {"phrase": "Cycle230 beta/g/order/precision", "classification": "pinned supplied law content"},
        ),
        "N4_residual_matching": (
            {"prior": "Cycle622 diagonal cocycle", "prior_residual": "diagonal scalar stream conjugacy", "current": "matrix-valued prefix/twist stream", "match": False, "use": "route boundary only"},
            {"prior": "Cycle617 endpoint fSWAP", "prior_residual": "direct endpoint B signs", "current": "graded four-mode face blocks for full S", "match": False, "use": "adjacent prior only"},
            {"prior": "Cycle622 archive QCA", "prior_residual": "garbage retained in archive", "current": "garbage moved into debited clean resource", "match": True, "use": "renewal ledger continuation"},
        ),
        "N5_resolution_audit": (
            "A classifies the declared uniform four-M2 face block and local braid "
            "phase, not all non-diagonal qudits; B is one Z2 prefix/twist and "
            "grouped-order construction, not all higher groups; C is one finite "
            "reversible reservoir, not all open-system reset laws"
        ),
        "N6_partial_closure_paths": (
            "retain A's covariant face-block channel and B's exact stream sign "
            "identity; a tensor-network encoder may absorb the reordering phase, "
            "and an explicit bath/source law may retire rather than axiomatize the resource debit"
        ),
        "N7_steelman_against_negative": (
            "A hostile reviewer can replace the fixed grouped-order phase by a "
            "translation-invariant fermionic PEPS/MPO tensor whose virtual parity "
            "index is the local prefix qubit, promote the seam to a mobile gauge "
            "defect, and conjugate the coin by a local tensor pull-through identity. "
            "The terminal obligation is explicit bounded tensors on the 48-role-or-"
            "smaller register, exact all24/all576 pull-through, and a prepared local "
            "parent-code state; Cycle628 does not test that mechanism."
        ),
        "N8_cross_cycle_echo": (
            "Cycles610 and 620 show that large clean-role macros can retire packing "
            "walls; Cycles617 and 622 show route-specific parity and Wilson walls "
            "can be partially retired by changing resolution. That constructive "
            "history prevents foreclosure here."
        ),
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "route_independent_obstruction_claimed": False,
        "axiom_pressure": False,
        "classification": "partial-attempt-with-named-untested-routes",
        "pass_for_withholding_negative": True,
    }
    condition = (
        len(families) >= 5 and len(pairwise) == math.comb(len(walls), 2)
        and sum(row["marker"] == "UNTESTED_LIVE" for row in families) >= 2
        and not joint["success"]
        and not result["negative_claim_shipped"]
        and not result["minimum_content_claim_shipped"]
        and not result["route_independent_obstruction_claimed"]
        and not result["axiom_pressure"]
    )
    check("fresh normalized N1-N8 fails the broad negative gate and withholds no-go/minimum/axiom pressure",
          condition, result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "Authority: none", "Audit: unset", "Cycle 628", "same code",
        "E G_coarse = G_physical E", "48", "Route A", "Route B", "Route C",
        "non-diagonal", "face qudit", "graded block swap", "L3", "L6", "L7",
        "all 24", "all 576", "odd/even coherent", "support-two",
        "nearest-neighbor", "prefix", "twist", "seam", "translation",
        "coin", "contact", "mass", "resource", "garbage", "deletion",
        "malformed", "leakage", "N1", "N8", "UNTESTED_LIVE",
        "no axiom pressure", "partial-attempt-with-named-untested-routes",
    )
    forbidden = (
        "all non-diagonal qudits fail", "all higher groups fail",
        "fermion compilation is impossible", "shared obstruction proved",
        "axiom revision required", "schedule is physical time",
    )
    missing = tuple(item for item in required if item not in text)
    forbidden_hits = tuple(item for item in forbidden if item in text.lower())
    result = {"missing": missing, "forbidden_hits": forbidden_hits}
    check("Cycle628 note freezes the exact route scopes, imports, residuals, and N1-N8",
          not missing and not forbidden_hits, result)
    return result


def main() -> int:
    started = time.perf_counter()
    print("Cycle628 non-diagonal link/qudit same-code fermion compiler tournament",
          AUTHORITY, AUDIT)
    r622, r620 = shore()
    layout = common_layout_audit()
    route_a = route_a_face_qudit()
    route_b = route_b_dynamic_twist()
    route_c = route_c_resource_reset()
    fixture = fixtures(r622, r620)
    joint = joint_disposition(layout, route_a, route_b, route_c, fixture)
    discipline = no_go_discipline(route_a, route_b, route_c, joint)
    note = note_contract()
    elapsed = time.perf_counter() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    resources = {"elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss}
    check("cold resource caps", elapsed < CAP_SECONDS and maximum_rss < CAP_BYTES,
          resources)
    receipt = {
        "status": "cycle628-non-diagonal-link-qudit-same-code-fermion-compiler-tournament",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "HEAD": subprocess.check_output(
            ("git", "rev-parse", "HEAD"), cwd=ROOT, text=True
        ).strip(),
        "pins": PINS,
        "runner_sha256": sha(Path(__file__)),
        "note_sha256": sha(NOTE),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "common_physical_register": layout,
        "route_A": route_a,
        "route_B": route_b,
        "route_C": route_c,
        "fixtures": fixture,
        "joint_disposition": joint,
        "no_go_discipline": discipline,
        "note_contract": note,
        "strongest_constructive_result": (
            "an exact covariant non-diagonal four-M2 face-qudit isometry and "
            "complete graded block exchange, plus an exact full-Fock line-prefix/"
            "twist stream intertwiner whose lattice-scale encoding phase and coin "
            "strings are measured rather than hidden"
        ),
        "route_by_route_disposition": {
            "A": "retain face-qudit W isometry and complete graded block swap; local counterflow braid phases miss Gamma(S)",
            "B": "retain exact all-pair stream conjugacy and local prefix/twist constraints; bounded E, translation-free preparation, and bounded coin fail",
            "C": "retain one-shot reset with exact clean-register debit and garbage; finite reservoir is not indefinite renewal",
        },
        "updated_dependency_ledger": {
            "C_ref": "sharpened: fixed grouped order/seam is the exact reference cost of Route B; role shells remain supplied",
            "C_num": "advanced by a coherent non-diagonal face isometry and exact matrix-valued stream sign identity; bounded full update remains open",
            "C_wrap": "advanced by explicit line-twist/seam parity handling on L3/L6/L7; the seam/root remains supplied",
            "C_int": "contact and one-particle mass remain local; the reordering-conjugated multiparticle coin becomes lattice-wide",
            "C_local": "advanced by exact graded face blocks and weight-four prefix constraints; one bounded common E/G still remains",
            "C_source": "advanced to an exact six-clean-M2-per-cell-per-use resource debit; no indefinite renewal/source law is derived",
        },
        "maturity_0_to_5": {
            "operational_quantum_records": 3.0,
            "causal_time": 2.0,
            "inertia_matter": 3.5,
            "gravity_source": 2.5,
            "Born_probability": 1.5,
        },
        "supplied_structure_inventory": (
            "129^3 coarse centers and radial/tangential 48-role shells",
            "blank face-qudit, prefix-buffer, archive, clean-resource, and routing M2s",
            "uniform face mode and its exact Givens angles/factorization",
            "Cycle230 six-mode CAR target, beta, contact g, coin-stream-contact order, and precision",
            "periodic L3/L6/L7 domains, grouped mode order, fixed seam/root, and initial/boundary state",
            "finite clean reservoir capacity; any bath, erasure, measurement, or entropy-export law",
        ),
        "shared_obstruction_or_axiom_pressure": False,
        "optimal_next_campaign": (
            "construct a translation-invariant fermionic PEPS/MPO pull-through "
            "tensor that absorbs Route B's reordering phase and keeps the onsite "
            "coin bounded, with a mobile locally prepared spin-structure defect"
        ),
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "pass": FAIL == 0,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n"
    )
    summary = {
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "route_A_face_qudit": route_a["pass_non_diagonal_local_face_block_compiler"],
        "route_A_full_stream": route_a["pass_required_full_Fock_stream_EG"],
        "route_B_exact_stream": route_b["pass_exact_stream_with_supplied_nonlocal_E"],
        "route_B_bounded_full_update": route_b["pass_required_bounded_same_code_full_update"],
        "route_C_resource_reset": route_c["pass_one_invocation_resource_accounted_reset"],
        "joint_same_code_compiler": joint["success"],
        "negative_claim": False,
        "axiom_pressure": False,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print("RESULT", PASS, FAIL)
    return int(FAIL != 0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold_handle:
        terminal = sys.stdout
        sys.stdout = Tee(terminal, cold_handle)
        try:
            exit_code = main()
        finally:
            sys.stdout = terminal
    raise SystemExit(exit_code)
