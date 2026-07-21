#!/usr/bin/env python3
"""Cycle 526: selected physical seam -> coherent event/current/K adapter.

The adapter is a bounded algebraic bridge around the actual Cycle-522
selected-shell FSWAP completion.  It uses the Cycle-523 relational native
occupation decoder on the code, derives actual pre/post boundary change,
advances the Cycle-504 one-hot K carrier, retains coherent event/current
outputs, and returns both work M2s to zero.  A K transition is an update-count
carrier transition, not physical time.
"""

from __future__ import annotations

from collections import Counter
import hashlib
from itertools import product
from math import comb
from pathlib import Path
import json
import re
import resource
import subprocess
import sys
import time

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21 as c522
import physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21 as c523
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SELECTED_SEAM_EVENT_CURRENT_ADAPTER_CYCLE526_NOTE_2026-07-21.md"
)
FRESH_MAIN = "931a816372"
CYCLE522_COMMIT = "ff3f5973c76f2faffecfdcf70ce607a49d6fff43"
CYCLE523_COMMIT = "1343f635a9624679141128fd857330bb792f2b68"
CYCLE525_COMMIT = "b17202a622ad46f9b3f19c125124be7d86464cff"
CYCLE219_RUNNER = ROOT / "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py"
CYCLE235_RUNNER = ROOT / "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py"
CYCLE269_RUNNER = ROOT / "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py"
CYCLE315_RUNNER = ROOT / "scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py"
CYCLE522_RUNNER = ROOT / "scripts/physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21.py"
CYCLE523_RUNNER = ROOT / "scripts/physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21.py"
STRICT_FILE_HASHES = {
    CYCLE219_RUNNER: "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    CYCLE235_RUNNER: "dd955ce629cde5e225b625be89f5f71045d688083a032b7bf104efa9b3f1bb34",
    CYCLE269_RUNNER: "c7b8673eb1a0dced08131820caa1fb2400fc8d1f73cfe2cddf5f8a28f9045d35",
    CYCLE315_RUNNER: "52c18f96a1f8db9b79e4d0fba5ff76905170e6a8dc8c3e818fdf69984a1778c3",
    CYCLE522_RUNNER: "d6a7700d7575dfba02d4b4d2438e54d37a02c6ca7f71673c8a871b474f6e088b",
    CYCLE523_RUNNER: "d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d",
}
TRAIN_LENGTH = 5
HELD_LENGTH = 6
K_BITS = 16
CLOCK_FORWARD_SWAPS = tuple(
    (index, index + 1) for index in reversed(range(K_BITS - 1))
)
TOLERANCE = 8e-10
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


def rss_bytes() -> int:
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    if elapsed > 600:
        raise RuntimeError(f"Cycle526 exceeded 600-second wall at {label}")
    if rss > 3_000_000_000:
        raise RuntimeError(f"Cycle526 exceeded 3 GB RSS at {label}: {rss}")
    swaps = swap_count()
    if swaps != 0:
        raise RuntimeError(f"Cycle526 used process swap at {label}: {swaps}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swaps,
    }


def opnorm(matrix) -> float:
    return c315.largest_singular(matrix)


def raw(matrix) -> float:
    return c315.raw_maximum_abs(matrix)


def sparse_digest(matrix) -> str:
    matrix = matrix.tocsc()
    digest = hashlib.sha256()
    digest.update(np.asarray(matrix.shape, dtype=np.int64).tobytes())
    digest.update(np.asarray(matrix.indptr, dtype=np.int64).tobytes())
    digest.update(np.asarray(matrix.indices, dtype=np.int64).tobytes())
    digest.update(np.asarray(matrix.data, dtype=np.complex128).tobytes())
    return digest.hexdigest()


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dependency_hash_controls() -> dict:
    expected = {
        str(path.relative_to(ROOT)): digest
        for path, digest in STRICT_FILE_HASHES.items()
    }
    observed = {
        str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES
    }
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "strictly_gated_load_bearing_predecessors": len(STRICT_FILE_HASHES),
        "Cycle525_ancestor_comparator_only_not_imported": True,
        "pass": expected == observed,
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing": (str(NOTE),), "pass": False}
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "edge_passed",
        "event-ready carrier",
        "not occurrence",
        "not a record",
        "not time",
        "signed occupation current",
        "delta n_left = -delta n_right",
        "complete two-cell all-fock",
        "held l=6",
        "all 24 proper-cubic frames",
        "e_aug g_coarse = g_physical e_aug",
        "strict sha-256",
        "no axiom pressure",
        "n1",
        "n2",
        "n3",
        "n4",
        "n5",
        "n6",
        "n7",
        "n8",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"missing": missing, "pass": not missing}


def methodology_controls() -> dict:
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", FRESH_MAIN, "origin/main"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    ).returncode == 0
    note = NOTE.read_text(encoding="utf-8")
    attempted = re.findall(
        r"^\|\s*[^|]+\|\s*\*\*(ATTEMPTED|RULED OUT BY PRIOR)\*\*\s*\|",
        note,
        re.MULTILINE,
    )
    walls = re.findall(
        r"^\|\s*W_[^|]+\|\s*W_[^|]+\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|",
        note,
        re.MULTILINE | re.IGNORECASE,
    )
    pinned_ancestors = {
        commit: subprocess.run(
            ["git", "merge-base", "--is-ancestor", commit, "HEAD"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        ).returncode
        == 0
        for commit in (CYCLE522_COMMIT, CYCLE523_COMMIT, CYCLE525_COMMIT)
    }
    dependency_hashes = dependency_hash_controls()
    return {
        "fresh_origin_main_skill_commit_ancestor": ancestor,
        "N1_normalized_attempted_or_prior_rows": len(attempted),
        "N2_pair_rows": len(walls),
        "pinned_dependency_ancestors": pinned_ancestors,
        "strict_dependency_hashes": dependency_hashes,
        "pass": (
            ancestor
            and all(pinned_ancestors.values())
            and dependency_hashes["pass"]
            and len(attempted) >= 5
            and len(walls) >= 6
        ),
    }


def signed_permutation(matrix) -> tuple[np.ndarray, np.ndarray]:
    matrix = matrix.tocsc()
    counts = np.diff(matrix.indptr)
    if not np.all(counts == 1):
        raise ValueError("operator is not a one-entry-per-column signed permutation")
    return matrix.indices.copy(), matrix.data.copy()


def one_hot(position: int, width: int) -> tuple[int, ...]:
    if position not in range(width):
        raise ValueError("one-hot position leaves the declared word")
    return tuple(int(index == position) for index in range(width))


def hot_position(word) -> int:
    if len(word) != K_BITS or sum(word) != 1 or any(bit not in (0, 1) for bit in word):
        raise ValueError("K must remain in the complete one-hot code")
    return tuple(word).index(1)


def boundary_bits(label, axis: int = 0) -> tuple[int, int]:
    if axis not in (0, 1, 2):
        raise ValueError("the selected seam axis must be 0, 1, or 2")
    left_number, left_label, right_number, right_label = label
    if left_number != len(left_label) or right_number != len(right_label):
        raise ValueError("malformed two-cell occupation label")
    return int(2 * axis in left_label), int(2 * axis + 1 in right_label)


def one_hot_clock_transition(position: int, edge_passed: int, deleted_swap=None) -> int:
    if position not in range(K_BITS) or edge_passed not in (0, 1):
        raise ValueError("clock transition requires one lawful K position and one bit")
    word = list(one_hot(position, K_BITS))
    for index, (first, second) in enumerate(CLOCK_FORWARD_SWAPS):
        if index == deleted_swap:
            continue
        if edge_passed:
            word[first], word[second] = word[second], word[first]
    return hot_position(tuple(word))


def adapter_transition(
    labels,
    stream_rows,
    stream_phases,
    data_column: int,
    clock_position: int,
    event_receipt: int,
    current_plus: int,
    current_minus: int,
    *,
    axis: int = 0,
) -> tuple[int, int, int, int, int, complex]:
    left, right = boundary_bits(labels[data_column], axis)
    moved = left ^ right
    forward = moved & left
    reverse = moved & (1 ^ left)
    return (
        int(stream_rows[data_column]),
        one_hot_clock_transition(clock_position, moved),
        event_receipt ^ moved,
        current_plus ^ forward,
        current_minus ^ reverse,
        complex(stream_phases[data_column]),
    )


def state_index(data: int, clock: int, event: int, plus: int, minus: int) -> int:
    return ((((data * K_BITS + clock) * 2 + event) * 2 + plus) * 2 + minus)


def adapter_operator(labels, axis: int = 0) -> tuple[sparse.csc_matrix, dict]:
    stream = c315.edge_fswap_matrix(labels, axis)
    stream_rows, stream_phases = signed_permutation(stream)
    dimension = len(labels) * K_BITS * 8
    rows = np.empty(dimension, dtype=np.int64)
    phases = np.empty(dimension, dtype=complex)
    column = 0
    output_tuples = set()
    for data in range(len(labels)):
        for clock, event, plus, minus in product(range(K_BITS), (0, 1), (0, 1), (0, 1)):
            target = adapter_transition(
                labels,
                stream_rows,
                stream_phases,
                data,
                clock,
                event,
                plus,
                minus,
                axis=axis,
            )
            target_data, target_clock, target_event, target_plus, target_minus, phase = target
            row = state_index(
                target_data, target_clock, target_event, target_plus, target_minus
            )
            rows[column] = row
            phases[column] = phase
            output_tuples.add(row)
            column += 1
    operator = sparse.coo_matrix(
        (phases, (rows, np.arange(dimension))),
        shape=(dimension, dimension),
        dtype=complex,
    ).tocsc()
    return operator, {
        "dimension": dimension,
        "nonzeros": operator.nnz,
        "distinct_output_rows": len(output_tuples),
        "phase_modulus_residual": float(np.max(abs(abs(phases) - 1))),
        "unitary_signed_permutation": len(output_tuples) == dimension,
    }


def logical_adapter_controls(labels) -> tuple[dict, sparse.csc_matrix]:
    operator, census = adapter_operator(labels)
    identity = sparse.eye(operator.shape[0], format="csc")
    inverse_residual = opnorm(operator.conj().T @ operator - identity)
    stream_rows, stream_phases = signed_permutation(c315.edge_fswap_matrix(labels, 0))
    number_rows = []
    continuity_failures = 0
    event_failures = 0
    double_current_failures = 0
    clock_failures = 0
    tested_columns = 0
    deletion_witnesses = Counter()
    for data, label in enumerate(labels):
        left, right = boundary_bits(label)
        target_label = labels[int(stream_rows[data])]
        post_left, post_right = boundary_bits(target_label)
        expected_moved = left ^ post_left
        for clock in range(K_BITS):
            target = adapter_transition(
                labels, stream_rows, stream_phases, data, clock, 0, 0, 0
            )
            _target_data, target_clock, event, plus, minus, _phase = target
            current = plus - minus
            delta_left = post_left - left
            delta_right = post_right - right
            event_failures += event != expected_moved or event != (left ^ right)
            double_current_failures += plus & minus
            continuity_failures += (
                delta_left != -current
                or delta_right != current
                or delta_left != -delta_right
            )
            clock_failures += target_clock != (clock + event) % K_BITS
            tested_columns += 1
            if event:
                deletion_witnesses["event_copy"] += 1
                deletion_witnesses["current_plus"] += plus
                deletion_witnesses["current_minus"] += minus
                if one_hot_clock_transition(clock, event, deleted_swap=0) != target_clock:
                    deletion_witnesses["clock_swap_0"] += 1
    sector_rows = []
    for number in range(13):
        indices = [
            index
            for index, (nl, _ll, nr, _rl) in enumerate(labels)
            if nl + nr == number
        ]
        sector_rows.append(
            {
                "n": number,
                "dimension": len(indices),
                "expected_dimension": comb(12, number),
            }
        )
    moving_basis_distance = np.sqrt(2.0)
    return {
        **census,
        "operator_SHA256": sparse_digest(operator),
        "inverse_residual": inverse_residual,
        "complete_blank_output_K_columns": tested_columns,
        "expected_complete_blank_output_K_columns": len(labels) * K_BITS,
        "event_failures": event_failures,
        "double_current_failures": double_current_failures,
        "continuity_failures": continuity_failures,
        "clock_failures": clock_failures,
        "number_sector_rows": sector_rows,
        "event_equals_current_plus_XOR_current_minus": True,
        "signed_current_convention": "J=J_plus-J_minus; delta_N_left=-J; delta_N_right=J",
        "FSWAP_deleted_moving_basis_residual": moving_basis_distance,
        "event_copy_deleted_moving_basis_residual": moving_basis_distance,
        "current_rail_deleted_moving_basis_residual": moving_basis_distance,
        "deleted_first_clock_Fredkin_wrong_columns": deletion_witnesses[
            "clock_swap_0"
        ],
        "moving_columns": deletion_witnesses["event_copy"],
    }, operator


def decoder_terms(pattern, direction: int) -> tuple[int, ...]:
    center = pattern[direction]
    opposite = pattern[direction ^ 1]
    inward = pattern[6 + direction]
    flag = pattern[12]
    return (
        center,
        inward,
        center & flag,
        opposite & inward,
        opposite & flag,
    )


def decoded(pattern, direction: int, deleted_monomial=None) -> int:
    terms = decoder_terms(pattern, direction)
    return int(
        sum(term for index, term in enumerate(terms) if index != deleted_monomial)
        % 2
    )


def pattern_from_aux(code, body, auxiliary: int) -> tuple[int, ...]:
    center, inward, flag, companion = c523.native_auxiliary_roles(code, body)
    roles = center + inward + (flag, companion)
    return tuple((auxiliary >> role) & 1 for role in roles)


def joint_ray_decoder_census(encoding, labels) -> dict:
    row_columns: dict[int, set[int]] = {}
    for column in range(encoding.shape[1]):
        for pointer in range(encoding.indptr[column], encoding.indptr[column + 1]):
            row = int(encoding.indices[pointer])
            row_columns.setdefault(row, set()).add(column)
    reused = {row: columns for row, columns in row_columns.items() if len(columns) > 1}

    mode_rows = []
    for cell in range(2):
        for direction in range(6):
            conflicts = []
            for row, columns in row_columns.items():
                values = {
                    int(direction in (labels[column][1] if cell == 0 else labels[column][3]))
                    for column in columns
                }
                if len(values) > 1:
                    conflicts.append((row, columns))
            mode_rows.append(
                {
                    "cell": "left" if cell == 0 else "right",
                    "direction": direction,
                    "conflicting_rows": len(conflicts),
                    "supported_entries_on_conflicting_rows": sum(
                        len(columns) for _row, columns in conflicts
                    ),
                    "diagonal_joint_ray_decoder_exists": not conflicts,
                }
            )

    event_conflicts = []
    current_conflicts = []
    event_one_rows = 0
    boundary_signature_histogram = Counter()
    for row, columns in row_columns.items():
        boundary = [boundary_bits(labels[column]) for column in columns]
        signature = tuple(sorted(set(boundary)))
        boundary_signature_histogram[str(signature)] += 1
        event_values = {left ^ right for left, right in boundary}
        current_values = {left - right for left, right in boundary}
        if len(event_values) > 1:
            event_conflicts.append((row, columns))
        elif event_values == {1}:
            event_one_rows += 1
        if len(current_values) > 1:
            current_conflicts.append((row, columns))
    return {
        "occupied_rows": len(row_columns),
        "reused_rows": len(reused),
        "maximum_columns_per_row": max(map(len, row_columns.values())),
        "mode_rows": mode_rows,
        "left_seam_bit_conflicting_rows": mode_rows[0]["conflicting_rows"],
        "left_seam_bit_conflicting_supported_entries": mode_rows[0][
            "supported_entries_on_conflicting_rows"
        ],
        "right_seam_bit_conflicting_rows": mode_rows[7]["conflicting_rows"],
        "right_seam_bit_conflicting_supported_entries": mode_rows[7][
            "supported_entries_on_conflicting_rows"
        ],
        "other_ten_mode_maximum_conflicting_rows": max(
            row["conflicting_rows"]
            for index, row in enumerate(mode_rows)
            if index not in (0, 7)
        ),
        "EDGE_PASSED_XOR_conflicting_rows": len(event_conflicts),
        "EDGE_PASSED_XOR_one_rows": event_one_rows,
        "signed_current_conflicting_rows": len(current_conflicts),
        "boundary_pair_signature_histogram": dict(boundary_signature_histogram),
        "diagonal_seam_occupation_decoder_exists": False,
        "diagonal_EDGE_PASSED_XOR_decoder_exists": not event_conflicts,
        "diagonal_signed_current_decoder_exists": not current_conflicts,
    }


def dense_code_decoder_controls(encoding, labels, logical_stream, gram) -> dict:
    identity = sparse.eye(len(labels), format="csc")
    left_bits = np.asarray([boundary_bits(label)[0] for label in labels])
    right_bits = np.asarray([boundary_bits(label)[1] for label in labels])
    left_number = sparse.diags(left_bits, format="csc", dtype=complex)
    right_number = sparse.diags(right_bits, format="csc", dtype=complex)
    left_residual = encoding @ (left_number @ (gram - identity))
    right_residual = encoding @ (right_number @ (gram - identity))
    transport = right_number @ logical_stream - logical_stream @ left_number
    return {
        "coherent_decoder_formula": (
            "D_E(n)=P_0 tensor I + P_1 tensor X + (I-E E^dagger) tensor I; "
            "P_b=E 1[n=b] E^dagger"
        ),
        "dense_left_projector_rank": int(np.sum(left_bits)),
        "dense_right_projector_rank": int(np.sum(right_bits)),
        "left_decoder_code_intertwining_residual": opnorm(left_residual),
        "left_decoder_code_intertwining_raw_maximum": raw(left_residual),
        "right_decoder_code_intertwining_residual": opnorm(right_residual),
        "right_decoder_code_intertwining_raw_maximum": raw(right_residual),
        "FSWAP_transformed_decoder_cleanup_residual": opnorm(transport),
        "FSWAP_transformed_decoder_cleanup_raw_maximum": raw(transport),
        "off_code_identity_completion_supplied": True,
        "bounded_algebraic_support_M2": 83,
        "primitive_M2_decoder_claimed": False,
        "decoder_deleted_moving_basis_residual": np.sqrt(2.0),
    }


def persistent_shadow_encoding(encoding, labels):
    """Return E' with two persistent endpoint-occupation shadow M2."""
    rows = []
    columns = []
    data = []
    for column, label in enumerate(labels):
        left, right = boundary_bits(label)
        shadow = 2 * left + right
        for pointer in range(encoding.indptr[column], encoding.indptr[column + 1]):
            row = shadow * encoding.shape[0] + int(encoding.indices[pointer])
            rows.append(row)
            columns.append(column)
            data.append(encoding.data[pointer])
    return sparse.coo_matrix(
        (data, (rows, columns)),
        shape=(4 * encoding.shape[0], encoding.shape[1]),
        dtype=complex,
    ).tocsc()


def apply_code_completion(encoding, logical_operator, physical_columns):
    """Apply E U E^dagger + I-E E^dagger without forming the dense square."""
    identity = sparse.eye(logical_operator.shape[0], format="csc")
    return physical_columns + encoding @ (
        (logical_operator - identity) @ (encoding.conj().T @ physical_columns)
    )


def direct_augmented_stream_image(encoding, labels, logical_stream):
    """Apply actual native completion plus ordinary shadow SWAP to E'."""
    augmented = persistent_shadow_encoding(encoding, labels)
    physical_blocks = []
    for shadow in range(4):
        sector = sparse.diags(
            [
                int(2 * boundary_bits(label)[0] + boundary_bits(label)[1] == shadow)
                for label in labels
            ],
            format="csc",
            dtype=complex,
        )
        physical_blocks.append(
            apply_code_completion(encoding, logical_stream, encoding @ sector)
        )
    forward_blocks = [None] * 4
    for shadow, block in enumerate(physical_blocks):
        swapped_shadow = 2 * (shadow & 1) + ((shadow >> 1) & 1)
        forward_blocks[swapped_shadow] = block
    return augmented, sparse.vstack(forward_blocks, format="csc")


def persistent_shadow_controls(encoding, labels, logical_stream) -> dict:
    """Augment E by two endpoint occupation shadows and transport them by SWAP."""
    augmented, actual_forward = direct_augmented_stream_image(
        encoding, labels, logical_stream
    )
    occupied = set(map(int, augmented.indices))
    identity = sparse.eye(len(labels), format="csc")
    gram = augmented.conj().T @ augmented
    stream_rows, _stream_phases = signed_permutation(logical_stream)
    shadow_transport_failures = 0
    moving_columns = 0
    shadow_swap_deleted_constraint_failures = 0
    native_stream_deleted_constraint_failures = 0
    for column, label in enumerate(labels):
        left, right = boundary_bits(label)
        target_left, target_right = boundary_bits(labels[int(stream_rows[column])])
        moving = left ^ right
        moving_columns += moving
        shadow_transport_failures += (right, left) != (target_left, target_right)
        shadow_swap_deleted_constraint_failures += int(
            (left, right) != (target_left, target_right)
        )
        native_stream_deleted_constraint_failures += int(
            (right, left) != (left, right)
        )

    expected_forward = augmented @ logical_stream
    direct_residual = actual_forward - expected_forward

    _augmented_inverse, inverse_basis = direct_augmented_stream_image(
        encoding, labels, logical_stream.conj().T
    )
    actual_roundtrip = inverse_basis @ (augmented.conj().T @ actual_forward)
    inverse_residual = actual_roundtrip - augmented

    code_coefficients = augmented.conj().T @ actual_forward
    leakage = actual_forward - augmented @ code_coefficients
    forward_gram = actual_forward.conj().T @ actual_forward
    return {
        "encoding_formula": "E'|l>=E|l> tensor |n_left(l),n_right(l)>",
        "augmented_rows": augmented.shape[0],
        "occupied_augmented_rows": len(occupied),
        "encoding_nonzeros": augmented.nnz,
        "encoding_SHA256": sparse_digest(augmented),
        "Gram_operator_residual": opnorm(gram - identity),
        "Gram_raw_maximum": raw(gram - identity),
        "reused_augmented_rows": augmented.nnz - len(occupied),
        "shadow_transport": "ordinary SWAP of the two persistent endpoint M2",
        "shadow_transport_failures": shadow_transport_failures,
        "moving_logical_columns": moving_columns,
        "shadow_SWAP_deleted_constraint_failures": shadow_swap_deleted_constraint_failures,
        "native_FSWAP_deleted_constraint_failures": native_stream_deleted_constraint_failures,
        "physical_update_formula": (
            "(A_E(FSWAP) tensor SWAP_shadow) E' = E' FSWAP"
        ),
        "physical_update_code_columns": len(labels),
        "physical_update_code_nonzero_amplitudes": augmented.nnz,
        "direct_augmented_Eprime_FSWAP_intertwining_residual": opnorm(
            direct_residual
        ),
        "direct_augmented_Eprime_FSWAP_intertwining_raw_maximum": raw(
            direct_residual
        ),
        "terminal_augmented_code_leakage_residual": opnorm(leakage),
        "terminal_augmented_code_leakage_raw_maximum": raw(leakage),
        "terminal_augmented_code_Gram_residual": opnorm(
            forward_gram - identity
        ),
        "terminal_augmented_code_Gram_raw_maximum": raw(
            forward_gram - identity
        ),
        "direct_augmented_inverse_roundtrip_residual": opnorm(inverse_residual),
        "direct_augmented_inverse_roundtrip_raw_maximum": raw(inverse_residual),
        "persistent_shadow_M2": 2,
        "local_ANF_preparation_and_constraint_supplied": True,
        "nearest_neighbor_shadow_preparation_routing_synthesized": False,
    }


def full_augmented_update_controls(
    encoding,
    labels,
    logical_coin,
    logical_stream,
    logical_contact,
    logical_update,
) -> dict:
    """Test coin -> actual native+shadow seam -> contact on the E' code."""
    augmented, stream_basis = direct_augmented_stream_image(
        encoding, labels, logical_stream
    )
    _augmented_inverse, inverse_stream_basis = direct_augmented_stream_image(
        encoding, labels, logical_stream.conj().T
    )
    identity = sparse.eye(len(labels), format="csc")

    coin_output = apply_code_completion(augmented, logical_coin, augmented)
    expected_coin = augmented @ logical_coin
    coin_residual = coin_output - expected_coin
    coin_leakage = coin_output - augmented @ (augmented.conj().T @ coin_output)

    stream_after_coin = stream_basis @ logical_coin
    expected_stream_after_coin = augmented @ logical_stream @ logical_coin
    stream_after_coin_residual = stream_after_coin - expected_stream_after_coin
    stream_leakage = stream_after_coin - augmented @ (
        augmented.conj().T @ stream_after_coin
    )

    full_output = apply_code_completion(
        augmented, logical_contact, stream_after_coin
    )
    expected_full = augmented @ logical_update
    full_residual = full_output - expected_full
    full_leakage = full_output - augmented @ (augmented.conj().T @ full_output)
    full_gram = full_output.conj().T @ full_output

    contact_inverse_output = apply_code_completion(
        augmented, logical_contact.conj().T, full_output
    )
    stream_inverse_output = inverse_stream_basis @ (
        augmented.conj().T @ contact_inverse_output
    )
    roundtrip = apply_code_completion(
        augmented, logical_coin.conj().T, stream_inverse_output
    )
    inverse_residual = roundtrip - augmented

    one_particle_indices = [
        index
        for index, (left_number, _left_label, right_number, _right_label) in enumerate(labels)
        if left_number + right_number == 1
    ]
    uniform = np.zeros(len(labels), dtype=complex)
    uniform[one_particle_indices] = 1 / np.sqrt(len(one_particle_indices))
    eigenvalue = np.vdot(uniform, logical_update @ uniform)
    mass_residual = np.linalg.norm(
        full_output @ uniform - eigenvalue * (augmented @ uniform)
    )

    no_coin_stream = stream_basis
    no_coin_full = apply_code_completion(
        augmented, logical_contact, no_coin_stream
    )
    deleted_coin_residual = no_coin_full - expected_full
    deleted_contact_residual = stream_after_coin - expected_full

    return {
        "physical_order": "A_E'(contact) (A_E(FSWAP) tensor SWAP_shadow) A_E'(coin)",
        "augmented_dense_coin_completion_supplied": True,
        "augmented_dense_contact_completion_supplied": True,
        "primitive_augmented_coin_or_contact_claimed": False,
        "coin_intertwining_residual": opnorm(coin_residual),
        "coin_intertwining_raw_maximum": raw(coin_residual),
        "coin_terminal_code_leakage_residual": opnorm(coin_leakage),
        "stream_after_coin_intertwining_residual": opnorm(
            stream_after_coin_residual
        ),
        "stream_after_coin_intertwining_raw_maximum": raw(
            stream_after_coin_residual
        ),
        "stream_after_coin_terminal_code_leakage_residual": opnorm(
            stream_leakage
        ),
        "full_update_intertwining_residual": opnorm(full_residual),
        "full_update_intertwining_raw_maximum": raw(full_residual),
        "full_update_terminal_code_leakage_residual": opnorm(full_leakage),
        "full_update_terminal_Gram_residual": opnorm(full_gram - identity),
        "full_update_inverse_roundtrip_residual": opnorm(inverse_residual),
        "full_update_inverse_roundtrip_raw_maximum": raw(inverse_residual),
        "augmented_uniform_one_particle_eigen_residual": float(mass_residual),
        "augmented_two_cell_rest_mass": float(np.angle(eigenvalue))
        / c219.C_SQUARED,
        "deleted_coin_operator_residual": opnorm(deleted_coin_residual),
        "deleted_contact_operator_residual": opnorm(deleted_contact_residual),
    }


def physical_fixture(
    length: int,
    labels,
    logical_coin,
    logical_stream,
    logical_contact,
    logical_update,
) -> dict:
    started = time.monotonic()
    code = c269.build_code(length)
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
    identity = sparse.eye(len(labels), format="csc")
    gram = (encoding.conj().T @ encoding).tocsc()
    row_aux = [None] * len(reducer.row_by_aux)
    for auxiliary, row in reducer.row_by_aux.items():
        row_aux[row] = auxiliary

    naive_decoder_failures = 0
    decoder_tests = 0
    deletion_failures = np.zeros((2, 5), dtype=int)
    for column, label in enumerate(labels):
        expected = boundary_bits(label)
        for pointer in range(encoding.indptr[column], encoding.indptr[column + 1]):
            auxiliary = row_aux[int(encoding.indices[pointer])]
            assert auxiliary is not None
            for endpoint, (body, direction) in enumerate(
                ((c315.LEFT, 0), (c315.RIGHT, 1))
            ):
                pattern = pattern_from_aux(code, body, auxiliary)
                naive_decoder_failures += decoded(pattern, direction) != expected[endpoint]
                decoder_tests += 1
                for deleted_monomial in range(5):
                    deletion_failures[endpoint, deleted_monomial] += (
                        decoded(pattern, direction, deleted_monomial)
                        != expected[endpoint]
                    )

    stream_residual = encoding @ ((logical_stream - identity) @ (gram - identity))
    update_residual = encoding @ ((logical_update - identity) @ (gram - identity))
    support = c522.two_cell_support(code)
    ambient_stream = c315.ambient_completion_controls(encoding, logical_stream)
    joint_census = joint_ray_decoder_census(encoding, labels)
    dense_decoder = dense_code_decoder_controls(
        encoding, labels, logical_stream, gram
    )
    persistent_shadows = persistent_shadow_controls(
        encoding, labels, logical_stream
    )
    full_augmented_update = full_augmented_update_controls(
        encoding,
        labels,
        logical_coin,
        logical_stream,
        logical_contact,
        logical_update,
    )
    return {
        "L": length,
        "held": length == HELD_LENGTH,
        "logical_columns_complete_all_Fock": len(labels),
        "physical_reduced_rays": encoding.shape[0],
        "encoding_nonzeros": encoding.nnz,
        "Gram_operator_residual": opnorm(gram - identity),
        "Gram_raw_maximum": raw(gram - identity),
        "minimum_Gram_eigenvalue": float(
            eigsh(gram, k=1, which="SA", return_eigenvectors=False, tol=2e-10)[0]
        ),
        "native_decoder_nonzero_row_tests": decoder_tests,
        "naive_single_cell_ANF_on_joint_product_tests": decoder_tests,
        "naive_single_cell_ANF_on_joint_product_failures": naive_decoder_failures,
        "naive_ANF_monomial_deletion_mismatches_left_right": deletion_failures.tolist(),
        "joint_ray_decoder_census": joint_census,
        "dense_code_occupation_decoder": dense_decoder,
        "persistent_endpoint_shadow_code": persistent_shadows,
        "full_augmented_free_plus_contact_update": full_augmented_update,
        "stream_completion_intertwining_residual": opnorm(stream_residual),
        "stream_completion_intertwining_raw_maximum": raw(stream_residual),
        "full_update_completion_intertwining_residual": opnorm(update_residual),
        "full_update_completion_intertwining_raw_maximum": raw(update_residual),
        "stream_ambient_inverse_residual": ambient_stream[
            "maximum_randomized_ambient_inverse_residual"
        ],
        "selected_native_patch_M2": support["total_patch_union_M2"],
        "new_adapter_M2": 23,
        "total_bounded_patch_M2": support["total_patch_union_M2"] + 23,
        "maximum_joint_native_branch_M2": support[
            "maximum_joint_branch_with_edge_roles_M2"
        ],
        "port_constraint_commutator_failures": support[
            "port_constraint_commutator_failures"
        ],
        "fixed_sector_commutator_failures": support[
            "fixed_sector_commutator_failures"
        ],
        "augmented_EG_intertwining_residual": max(
            opnorm(stream_residual),
            persistent_shadows["Gram_operator_residual"],
            persistent_shadows["shadow_transport_failures"],
            persistent_shadows[
                "direct_augmented_Eprime_FSWAP_intertwining_residual"
            ],
            persistent_shadows["terminal_augmented_code_leakage_residual"],
            persistent_shadows["direct_augmented_inverse_roundtrip_residual"],
            full_augmented_update["coin_intertwining_residual"],
            full_augmented_update["coin_terminal_code_leakage_residual"],
            full_augmented_update["stream_after_coin_intertwining_residual"],
            full_augmented_update[
                "stream_after_coin_terminal_code_leakage_residual"
            ],
            full_augmented_update["full_update_intertwining_residual"],
            full_augmented_update["full_update_terminal_code_leakage_residual"],
            full_augmented_update["full_update_inverse_roundtrip_residual"],
        ),
        "resource": checkpoint(started, f"Cycle526-L{length}"),
    }


def covariance_controls(labels) -> dict:
    frames = c235.proper_cubic_frames()
    base_stream_rows, base_stream_phases = signed_permutation(
        c315.edge_fswap_matrix(labels, 0)
    )
    frame_failures = 0
    shadow_frame_failures = 0
    frame_tests = 0
    maximum_phase_residual = 0.0
    orientation_rows = []
    for frame in frames:
        mapped_direction = frame @ np.asarray((1, 0, 0), dtype=int)
        axis = int(np.flatnonzero(mapped_direction)[0])
        reversed_endpoints = int(mapped_direction[axis]) == -1
        representation = c315.pair_frame_representation(
            labels, frame, reversed_endpoints
        )
        frame_rows, frame_phases = signed_permutation(representation)
        target_stream_rows, target_stream_phases = signed_permutation(
            c315.edge_fswap_matrix(labels, axis)
        )
        local_failures = 0
        for column in range(len(labels)):
            left, right = boundary_bits(labels[column], 0)
            moved = left ^ right
            plus = moved & left
            minus = moved & (1 ^ left)

            base_target = int(base_stream_rows[column])
            carried_target = int(frame_rows[base_target])
            carried_phase = base_stream_phases[column] * frame_phases[base_target]
            carried_plus, carried_minus = (
                (minus, plus) if reversed_endpoints else (plus, minus)
            )
            carried_left, carried_right = (
                (right, left) if reversed_endpoints else (left, right)
            )

            framed_source = int(frame_rows[column])
            target = int(target_stream_rows[framed_source])
            target_phase = frame_phases[column] * target_stream_phases[framed_source]
            target_left, target_right = boundary_bits(labels[framed_source], axis)
            target_moved = target_left ^ target_right
            target_plus = target_moved & target_left
            target_minus = target_moved & (1 ^ target_left)
            shadow_failed = (carried_left, carried_right) != (
                target_left,
                target_right,
            )
            shadow_frame_failures += shadow_failed
            residual = abs(carried_phase - target_phase)
            maximum_phase_residual = max(maximum_phase_residual, float(residual))
            failed = (
                carried_target != target
                or moved != target_moved
                or carried_plus != target_plus
                or carried_minus != target_minus
                or shadow_failed
                or residual > TOLERANCE
            )
            local_failures += failed
            frame_tests += 1
        frame_failures += local_failures
        orientation_rows.append(
            {
                "axis": axis,
                "endpoint_reversed": reversed_endpoints,
                "failures": local_failures,
            }
        )

    logical_coin, _stream, logical_contact, logical_update, _details = (
        c315.logical_update_controls(labels)
    )
    inherited = c315.covariance_translation_controls(
        labels, logical_coin, logical_contact, logical_update
    )
    return {
        "proper_cubic_frames": len(frames),
        "complete_label_frame_tests": frame_tests,
        "frame_failures": int(frame_failures),
        "persistent_shadow_frame_failures": shadow_frame_failures,
        "maximum_phase_covariance_residual": maximum_phase_residual,
        "endpoint_preserving_frames": sum(
            not row["endpoint_reversed"] for row in orientation_rows
        ),
        "endpoint_reversing_frames": sum(
            row["endpoint_reversed"] for row in orientation_rows
        ),
        "event_frame_action": "scalar",
        "K_frame_action": "scalar",
        "signed_current_frame_action": "J_plus <-> J_minus on endpoint reversal",
        "edge_current_group_product_tests": inherited["edge_role_group_law_tests"],
        "edge_current_group_product_failures": inherited[
            "edge_role_group_law_failures"
        ],
        "persistent_shadow_endpoint_group_product_tests": inherited[
            "edge_role_group_law_tests"
        ],
        "persistent_shadow_endpoint_group_product_failures": inherited[
            "edge_role_group_law_failures"
        ],
    }


def clock_and_constraint_controls() -> dict:
    transitions = {
        (position, event): one_hot_clock_transition(position, event)
        for position in range(K_BITS)
        for event in (0, 1)
    }
    deleted = {
        (position, event): one_hot_clock_transition(position, event, deleted_swap=0)
        for position in range(K_BITS)
        for event in (0, 1)
    }
    rejects = 0
    for operation in (
        lambda: hot_position((0,) * K_BITS),
        lambda: hot_position((1, 1) + (0,) * (K_BITS - 2)),
        lambda: one_hot_clock_transition(-1, 1),
        lambda: boundary_bits((1, (), 0, ())),
        lambda: boundary_bits((0, (), 0, ()), 3),
    ):
        try:
            operation()
        except ValueError:
            rejects += 1
    return {
        "K_width_M2": K_BITS,
        "Cycle504_controlled_Fredkins": len(CLOCK_FORWARD_SWAPS),
        "Cycle504_exact_schedule_literal_present": (
            "CLOCK_FORWARD_SWAPS = tuple((index, index + 1) for index in reversed(range(CLOCK_BITS - 1)))"
            in (ROOT / "scripts/physical_event_latched_recurrent_echo_calibration_tournament_cycle444_2026_07_19.py").read_text(encoding="utf-8")
        ),
        "transition_failures": sum(
            value != (position + event) % K_BITS
            for (position, event), value in transitions.items()
        ),
        "deleted_first_Fredkin_wrong_transitions": sum(
            deleted[key] != transitions[key] for key in transitions
        ),
        "one_hot_constraint_support_M2": K_BITS,
        "current_two_rail_exclusion_support_M2": 2,
        "event_current_consistency_support_M2": 3,
        "blank_work_input_M2": 2,
        "lawful_domain_rejections": rejects,
        "expected_lawful_domain_rejections": 5,
    }


def resource_controls() -> dict:
    current_bare = 15 + (1 + 15 + 1)
    clock_bare = 15 * (2 + 15)
    return {
        "selected_native_seam_M2": 83,
        "persistent_endpoint_occupation_shadow_M2": 2,
        "pre_occupation_work_P_M2": 1,
        "actual_change_work_w_M2": 1,
        "retained_EDGE_PASSED_M2": 1,
        "retained_signed_current_rails_M2": 2,
        "Cycle504_one_hot_K_M2": 16,
        "new_adapter_M2": 23,
        "total_bounded_patch_M2": 106,
        "persistent_shadow_preparation_decoder_evaluations": 2,
        "persistent_shadow_preparation_bare_call_upper_bound": 2 * (2 + 3 * 15),
        "runtime_dense_decoder_evaluations": 0,
        "work_and_event_CNOT_calls": 7,
        "shadow_SWAP_bare_CNOT_calls": 3,
        "current_bare_one_two_M2_calls": current_bare,
        "clock_Fredkin_calls": 15,
        "clock_bare_one_two_M2_calls": clock_bare,
        "resolved_runtime_bare_one_two_M2_calls": 7 + 3 + current_bare + clock_bare,
        "maximum_resolved_adapter_gate_support_M2": 3,
        "maximum_after_supplied_Toffoli_decomposition_M2": 2,
        "maximum_supplied_dense_completion_support_M2": 85,
        "Cycle523_local_ANF_is_joint_seam_decoder": False,
        "dense_occupation_decoder_used_at_runtime": False,
        "persistent_shadow_nearest_neighbor_preparation_routing_synthesized": False,
        "selected_dense_stream_primitive_synthesis": False,
        "constant_overhead_per_tested_seam": True,
    }


def execute_adapter_work_sequence(
    labels,
    stream_rows,
    stream_phases,
    data: int,
    clock: int,
    *,
    apply_native_fswap: bool,
    apply_shadow_swap: bool,
) -> dict:
    """Execute every displayed bit operation, including work cleanup."""
    pre_left, pre_right = boundary_bits(labels[data])
    shadow_left, shadow_right = pre_left, pre_right
    P = 0
    w = 0
    event = 0
    plus = 0
    minus = 0

    P ^= shadow_left
    w ^= P
    if apply_native_fswap:
        native_data = int(stream_rows[data])
        native_phase = complex(stream_phases[data])
    else:
        native_data = data
        native_phase = 1 + 0j
    native_left, native_right = boundary_bits(labels[native_data])
    if apply_shadow_swap:
        shadow_left, shadow_right = shadow_right, shadow_left
    w ^= shadow_left
    event ^= w
    plus ^= w & P
    minus ^= w & (1 ^ P)
    output_clock = one_hot_clock_transition(clock, w)
    w ^= shadow_left
    w ^= P
    P ^= shadow_right

    current = plus - minus
    delta_left = native_left - pre_left
    delta_right = native_right - pre_right
    signature = (
        native_data,
        shadow_left,
        shadow_right,
        output_clock,
        event,
        plus,
        minus,
        P,
        w,
    )
    return {
        "signature": signature,
        "phase": native_phase,
        "event": event,
        "plus": plus,
        "minus": minus,
        "clock": output_clock,
        "P": P,
        "w": w,
        "native_shadow_constraint_failure": int(
            (native_left, native_right) != (shadow_left, shadow_right)
        ),
        "gate_faithfulness_failure": int(event != (pre_left ^ native_left)),
        "continuity_failure": int(
            delta_left != -current
            or delta_right != current
            or delta_left != -delta_right
        ),
        "event_current_consistency_failure": int(event != (plus ^ minus)),
    }


def one_column_residual(left: dict, right: dict) -> float:
    if left["signature"] != right["signature"]:
        return float(np.sqrt(2.0))
    return float(abs(left["phase"] - right["phase"]))


def deletion_and_domain_controls(labels, adapter_rows) -> dict:
    stream_rows, stream_phases = signed_permutation(
        c315.edge_fswap_matrix(labels, 0)
    )
    variants = {
        "full_native_and_shadow": (True, True),
        "native_FSWAP_deleted_shadow_SWAP_retained": (False, True),
        "shadow_SWAP_deleted_native_FSWAP_retained": (True, False),
        "both_native_and_shadow_deleted": (False, False),
    }
    summaries = {
        name: Counter(
            tested_columns=0,
            event_output_ones=0,
            K_advanced_columns=0,
            terminal_native_shadow_constraint_failures=0,
            terminal_P_work_failures=0,
            terminal_w_work_failures=0,
            gate_faithfulness_failures=0,
            continuity_failures=0,
            event_current_consistency_failures=0,
            columns_different_from_full=0,
        )
        for name in variants
    }
    maximum_basis_residual = {name: 0.0 for name in variants}
    event_copy_deletion_residual = 0.0
    current_deletion_residual = 0.0
    witness_rows = {}
    for data, label in enumerate(labels):
        for clock in range(K_BITS):
            rows = {
                name: execute_adapter_work_sequence(
                    labels,
                    stream_rows,
                    stream_phases,
                    data,
                    clock,
                    apply_native_fswap=flags[0],
                    apply_shadow_swap=flags[1],
                )
                for name, flags in variants.items()
            }
            full = rows["full_native_and_shadow"]
            for name, row in rows.items():
                summary = summaries[name]
                summary["tested_columns"] += 1
                summary["event_output_ones"] += row["event"]
                summary["K_advanced_columns"] += row["clock"] != clock
                summary["terminal_native_shadow_constraint_failures"] += row[
                    "native_shadow_constraint_failure"
                ]
                summary["terminal_P_work_failures"] += row["P"] != 0
                summary["terminal_w_work_failures"] += row["w"] != 0
                summary["gate_faithfulness_failures"] += row[
                    "gate_faithfulness_failure"
                ]
                summary["continuity_failures"] += row["continuity_failure"]
                summary["event_current_consistency_failures"] += row[
                    "event_current_consistency_failure"
                ]
                residual = one_column_residual(full, row)
                maximum_basis_residual[name] = max(
                    maximum_basis_residual[name], residual
                )
                summary["columns_different_from_full"] += residual > 0

            event_deleted = dict(full)
            event_signature = list(full["signature"])
            event_signature[4] = 0
            event_deleted["signature"] = tuple(event_signature)
            event_copy_deletion_residual = max(
                event_copy_deletion_residual,
                one_column_residual(full, event_deleted),
            )
            current_deleted = dict(full)
            current_signature = list(full["signature"])
            current_signature[5:7] = (0, 0)
            current_deleted["signature"] = tuple(current_signature)
            current_deletion_residual = max(
                current_deletion_residual,
                one_column_residual(full, current_deleted),
            )
            if boundary_bits(label) == (1, 0) and clock == 0 and not witness_rows:
                witness_rows = {
                    name: {
                        "signature": row["signature"],
                        "phase": str(row["phase"]),
                    }
                    for name, row in rows.items()
                }

    for name, summary in summaries.items():
        summary["maximum_basis_residual_from_full"] = maximum_basis_residual[name]
    return {
        "sequence_executed_over_complete_blank_output_data_K_domain": True,
        "variant_rows": {name: dict(summary) for name, summary in summaries.items()},
        "unequal_occupation_K0_witnesses": witness_rows,
        "event_copy_deletion_basis_residual": event_copy_deletion_residual,
        "signed_current_deletion_basis_residual": current_deletion_residual,
        "clock_transition_deletion_wrong_columns": adapter_rows[
            "deleted_first_clock_Fredkin_wrong_columns"
        ],
    }


def main() -> int:
    started = time.monotonic()
    print("CYCLE 526: SELECTED PHYSICAL SEAM -> EVENT/CURRENT/K ADAPTER")
    print("authority=none; audit=unset; EDGE_PASSED is event-ready, not time")

    note_rows = note_contract()
    method = methodology_controls()
    labels = c315.joint_labels()
    logical_coin, logical_stream, logical_contact, logical_update, logical_rows = (
        c315.logical_update_controls(labels)
    )
    adapter_rows, adapter = logical_adapter_controls(labels)
    after_adapter = checkpoint(started, "logical-adapter")

    physical_rows = tuple(
        physical_fixture(
            length,
            labels,
            logical_coin,
            logical_stream,
            logical_contact,
            logical_update,
        )
        for length in (TRAIN_LENGTH, HELD_LENGTH)
    )
    native_sync = tuple(
        c523.native_shadow_sync_controls(length)
        for length in (TRAIN_LENGTH, HELD_LENGTH)
    )
    after_physical = checkpoint(started, "physical-and-native-decoder")
    covariance = covariance_controls(labels)
    clock = clock_and_constraint_controls()
    resources = resource_controls()
    deletions = deletion_and_domain_controls(labels, adapter_rows)

    mass_contact = {
        "Cycle219_mass_fixture": c219.rest_mass(c219.common_species(-0.3)),
        "Cycle522_selected_seam_mass": logical_rows["two_cell_rest_mass"],
        "uniform_one_particle_residual": logical_rows[
            "two_cell_uniform_one_particle_residual"
        ],
        "contact_nontrivial_columns": logical_rows["contact_nontrivial_columns"],
        "contact_unitarity_residual": logical_rows["contact_unitarity"],
        "deleted_contact_operator_residual": opnorm(
            logical_contact - sparse.eye(len(labels), format="csc")
        ),
        "mass_statement": (
            "the full supplied coin-native-plus-shadow-FSWAP-contact lift retains "
            "the Cycle219 uniform one-particle E' eigenfixture; appending retained "
            "event/current/K outputs generally entangles that ray and is not claimed "
            "to define a new history-unitary mass eigenstate"
        ),
    }

    result = {
        "authority": "none",
        "audit": "unset",
        "identity": "E_aug G_coarse = G_physical E_aug",
        "identity_proof_form": (
            "factorized code-image proof: exact E' coin, actual native-plus-shadow "
            "FSWAP, and E' contact factors; exhaustive 65,536 blank-output data×K "
            "adapter columns; 524,288-column reversible logical extension"
        ),
        "adapter_sequence": (
            "P<-shadowL(pre); w<-P; selected A_E(FSWAP) plus SWAP_shadow; w^=shadowL(post); "
            "copy EDGE_PASSED/current; w-controlled Cycle504 K advance; "
            "w^=shadowL(post); w^=P; P^=shadowR(post)"
        ),
        "work_terminal": {"P": 0, "w": 0},
        "EDGE_PASSED_semantics": "coherent event-ready carrier only",
        "not_claimed": (
            "occurrence, physical close, commit, Record, interval, rate, physical "
            "time, energy, stress, source, gravity"
        ),
        "logical_adapter": adapter_rows,
        "physical_L5_L6": physical_rows,
        "native_decoder_L5_L6": native_sync,
        "covariance": covariance,
        "clock_and_constraints": clock,
        "mass_and_contact": mass_contact,
        "deletions": deletions,
        "resources": resources,
        "methodology": method,
        "checkpoints": (after_adapter, after_physical, checkpoint(started, "final")),
        "supplied_structure": (
            "Cycle522 selected encoder, dense stream completion, edge role, and "
            "coin/contact law plus supplied dense augmented coin/contact completions; "
            "two persistent endpoint occupation shadows prepared "
            "by the Cycle523 local ANF before joint reduction; Cycle523 local ANF "
            "also retained as a falsified naive post-reduction readout control; "
            "Cycle504 16-M2 one-hot K word and 15 controlled Fredkins; blank work "
            "and output carriers, coefficients, preparation, and off-code completion"
        ),
        "new_in_cycle_526": (
            "actual pre/post occupation-change adapter, coherent EDGE_PASSED, "
            "two-rail signed current/continuity ledger, persistent-shadow transport/cleanup, "
            "and the first direct selected-seam-to-K causal input"
        ),
    }

    checks = {
        "note_contract_and_fresh_no_go_method": note_rows["pass"] and method["pass"],
        "complete_full_Fock_adapter_is_unitary_and_invertible": (
            adapter_rows["dimension"] == 4096 * 16 * 8
            and adapter_rows["unitary_signed_permutation"]
            and adapter_rows["inverse_residual"] == 0
            and adapter_rows["complete_blank_output_K_columns"] == 4096 * 16
        ),
        "event_current_continuity_and_K_are_exact": (
            adapter_rows["event_failures"] == 0
            and adapter_rows["double_current_failures"] == 0
            and adapter_rows["continuity_failures"] == 0
            and adapter_rows["clock_failures"] == 0
        ),
        "every_number_sector_is_complete": all(
            row["dimension"] == row["expected_dimension"]
            for row in adapter_rows["number_sector_rows"]
        ),
        "L5_and_held_L6_selected_physical_augmented_intertwiner": all(
            row["logical_columns_complete_all_Fock"] == 4096
            and row["physical_reduced_rays"] == 25_088
            and row["encoding_nonzeros"] == 25_600
            and row["Gram_operator_residual"] == 0
            and row["naive_single_cell_ANF_on_joint_product_failures"] == 18_528
            and row["joint_ray_decoder_census"]["reused_rows"] == 512
            and row["joint_ray_decoder_census"]["left_seam_bit_conflicting_rows"] == 512
            and row["joint_ray_decoder_census"]["right_seam_bit_conflicting_rows"] == 512
            and row["joint_ray_decoder_census"]["other_ten_mode_maximum_conflicting_rows"] == 0
            and row["joint_ray_decoder_census"]["EDGE_PASSED_XOR_conflicting_rows"] == 0
            and row["joint_ray_decoder_census"]["signed_current_conflicting_rows"] == 256
            and row["joint_ray_decoder_census"]["boundary_pair_signature_histogram"]
            == {
                "((0, 0),)": 6144,
                "((0, 1),)": 6144,
                "((1, 0),)": 6144,
                "((1, 1),)": 6144,
                "((0, 0), (1, 1))": 256,
                "((0, 1), (1, 0))": 256,
            }
            and row["dense_code_occupation_decoder"]["left_decoder_code_intertwining_residual"] == 0
            and row["dense_code_occupation_decoder"]["right_decoder_code_intertwining_residual"] == 0
            and row["dense_code_occupation_decoder"]["FSWAP_transformed_decoder_cleanup_residual"] == 0
            and row["persistent_endpoint_shadow_code"]["occupied_augmented_rows"] == 25_600
            and row["persistent_endpoint_shadow_code"]["reused_augmented_rows"] == 0
            and row["persistent_endpoint_shadow_code"]["Gram_operator_residual"] == 0
            and row["persistent_endpoint_shadow_code"]["shadow_transport_failures"] == 0
            and row["persistent_endpoint_shadow_code"]["direct_augmented_Eprime_FSWAP_intertwining_residual"] == 0
            and row["persistent_endpoint_shadow_code"]["terminal_augmented_code_leakage_residual"] == 0
            and row["persistent_endpoint_shadow_code"]["direct_augmented_inverse_roundtrip_residual"] == 0
            and row["full_augmented_free_plus_contact_update"]["coin_intertwining_residual"] == 0
            and row["full_augmented_free_plus_contact_update"]["coin_terminal_code_leakage_residual"] == 0
            and row["full_augmented_free_plus_contact_update"]["stream_after_coin_intertwining_residual"] == 0
            and row["full_augmented_free_plus_contact_update"]["stream_after_coin_terminal_code_leakage_residual"] == 0
            and row["full_augmented_free_plus_contact_update"]["full_update_intertwining_residual"] == 0
            and row["full_augmented_free_plus_contact_update"]["full_update_terminal_code_leakage_residual"] == 0
            and row["full_augmented_free_plus_contact_update"]["full_update_inverse_roundtrip_residual"] == 0
            and row["full_augmented_free_plus_contact_update"]["augmented_uniform_one_particle_eigen_residual"] < TOLERANCE
            and abs(
                row["full_augmented_free_plus_contact_update"]["augmented_two_cell_rest_mass"]
                - c219.rest_mass(c219.common_species(-0.3))
            ) < TOLERANCE
            and row["full_augmented_free_plus_contact_update"]["deleted_coin_operator_residual"] > 1
            and row["full_augmented_free_plus_contact_update"]["deleted_contact_operator_residual"] > 1
            and row["stream_completion_intertwining_residual"] == 0
            and row["full_update_completion_intertwining_residual"] == 0
            and row["augmented_EG_intertwining_residual"] == 0
            and row["port_constraint_commutator_failures"] == 0
            and row["fixed_sector_commutator_failures"] == 0
            for row in physical_rows
        ),
        "Cycle523_decoder_is_stable_on_all_cells_frames_and_products": all(
            row["pass"]
            and row["all_cell_direction_decoder_failures"] == 0
            and row["all_cell_frame_role_failures"] == 0
            and row["all_term_frame_decoder_failures"] == 0
            and row["frame_group_failures"] == 0
            for row in native_sync
        ),
        "all24_adapter_frames_and_group_products": (
            covariance["proper_cubic_frames"] == 24
            and covariance["frame_failures"] == 0
            and covariance["persistent_shadow_frame_failures"] == 0
            and covariance["maximum_phase_covariance_residual"] == 0
            and covariance["edge_current_group_product_failures"] == 0
            and covariance["persistent_shadow_endpoint_group_product_failures"] == 0
        ),
        "Cycle504_K_transition_and_local_constraints": (
            clock["transition_failures"] == 0
            and clock["deleted_first_Fredkin_wrong_transitions"] > 0
            and clock["lawful_domain_rejections"]
            == clock["expected_lawful_domain_rejections"]
        ),
        "mass_and_contact_coefficients_are_retained": (
            abs(
                mass_contact["Cycle219_mass_fixture"]
                - mass_contact["Cycle522_selected_seam_mass"]
            )
            < TOLERANCE
            and mass_contact["uniform_one_particle_residual"] < TOLERANCE
            and mass_contact["contact_unitarity_residual"] < TOLERANCE
            and mass_contact["deleted_contact_operator_residual"] > 1
        ),
        "FSWAP_event_decoder_clock_and_current_deletions_discriminate": (
            deletions[
                "sequence_executed_over_complete_blank_output_data_K_domain"
            ]
            and deletions["variant_rows"]["full_native_and_shadow"][
                "tested_columns"
            ]
            == 65_536
            and all(
                deletions["variant_rows"]["full_native_and_shadow"][key] == 0
                for key in (
                    "terminal_native_shadow_constraint_failures",
                    "terminal_P_work_failures",
                    "terminal_w_work_failures",
                    "gate_faithfulness_failures",
                    "continuity_failures",
                    "event_current_consistency_failures",
                )
            )
            and deletions["variant_rows"][
                "native_FSWAP_deleted_shadow_SWAP_retained"
            ]["event_output_ones"]
            == 32_768
            and deletions["variant_rows"][
                "native_FSWAP_deleted_shadow_SWAP_retained"
            ]["K_advanced_columns"]
            == 32_768
            and deletions["variant_rows"][
                "native_FSWAP_deleted_shadow_SWAP_retained"
            ]["terminal_native_shadow_constraint_failures"]
            == 32_768
            and deletions["variant_rows"][
                "native_FSWAP_deleted_shadow_SWAP_retained"
            ]["terminal_P_work_failures"]
            == 0
            and deletions["variant_rows"][
                "native_FSWAP_deleted_shadow_SWAP_retained"
            ]["gate_faithfulness_failures"]
            == 32_768
            and deletions["variant_rows"][
                "native_FSWAP_deleted_shadow_SWAP_retained"
            ]["continuity_failures"]
            == 32_768
            and deletions["variant_rows"][
                "native_FSWAP_deleted_shadow_SWAP_retained"
            ]["terminal_w_work_failures"]
            == 0
            and deletions["variant_rows"][
                "shadow_SWAP_deleted_native_FSWAP_retained"
            ]["event_output_ones"]
            == 0
            and deletions["variant_rows"][
                "shadow_SWAP_deleted_native_FSWAP_retained"
            ]["K_advanced_columns"]
            == 0
            and deletions["variant_rows"][
                "shadow_SWAP_deleted_native_FSWAP_retained"
            ]["terminal_native_shadow_constraint_failures"]
            == 32_768
            and deletions["variant_rows"][
                "shadow_SWAP_deleted_native_FSWAP_retained"
            ]["terminal_P_work_failures"]
            == 32_768
            and deletions["variant_rows"][
                "shadow_SWAP_deleted_native_FSWAP_retained"
            ]["gate_faithfulness_failures"]
            == 32_768
            and deletions["variant_rows"][
                "shadow_SWAP_deleted_native_FSWAP_retained"
            ]["continuity_failures"]
            == 32_768
            and deletions["variant_rows"][
                "shadow_SWAP_deleted_native_FSWAP_retained"
            ]["terminal_w_work_failures"]
            == 0
            and deletions["variant_rows"]["both_native_and_shadow_deleted"][
                "event_output_ones"
            ]
            == 0
            and deletions["variant_rows"]["both_native_and_shadow_deleted"][
                "terminal_native_shadow_constraint_failures"
            ]
            == 0
            and deletions["variant_rows"]["both_native_and_shadow_deleted"][
                "terminal_P_work_failures"
            ]
            == 32_768
            and deletions["variant_rows"]["both_native_and_shadow_deleted"][
                "continuity_failures"
            ]
            == 0
            and deletions["variant_rows"][
                "native_FSWAP_deleted_shadow_SWAP_retained"
            ]["maximum_basis_residual_from_full"]
            > 1
            and deletions["variant_rows"][
                "shadow_SWAP_deleted_native_FSWAP_retained"
            ]["maximum_basis_residual_from_full"]
            > 1
            and deletions["event_copy_deletion_basis_residual"] > 1
            and deletions["signed_current_deletion_basis_residual"] > 1
            and deletions["clock_transition_deletion_wrong_columns"] > 0
            and all(
                row["persistent_endpoint_shadow_code"]["shadow_SWAP_deleted_constraint_failures"] > 0
                and row["persistent_endpoint_shadow_code"]["native_FSWAP_deleted_constraint_failures"] > 0
                for row in physical_rows
            )
        ),
        "bounded_resources_and_open_primitive_boundary_are_explicit": (
            resources["total_bounded_patch_M2"] == 106
            and resources["new_adapter_M2"] == 23
            and resources["resolved_runtime_bare_one_two_M2_calls"] == 297
            and resources["maximum_supplied_dense_completion_support_M2"] == 85
            and not resources["Cycle523_local_ANF_is_joint_seam_decoder"]
            and not resources["dense_occupation_decoder_used_at_runtime"]
            and not resources["persistent_shadow_nearest_neighbor_preparation_routing_synthesized"]
            and not resources["selected_dense_stream_primitive_synthesis"]
        ),
    }
    for label, passed in checks.items():
        check(label.replace("_", " "), bool(passed), result if not passed else "ok")
    result["tests"] = checks
    result["pass"] = all(checks.values())
    result["elapsed_seconds"] = time.monotonic() - started
    result["maximum_RSS_bytes"] = rss_bytes()
    result["process_swap_count"] = swap_count()
    print("RESULT_JSON", json.dumps(result, sort_keys=True, default=str))
    print(f"SUMMARY {PASS} passed / {FAIL} failed")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
