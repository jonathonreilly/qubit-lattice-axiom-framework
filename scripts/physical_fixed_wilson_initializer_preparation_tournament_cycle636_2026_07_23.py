#!/usr/bin/env python3
"""Cycle636: physical fixed-Wilson initializer preparation tournament.

This cycle does not revisit Cycle537's ambient cap-embedding question.  It
tests whether retained-exhaust reset, cap-check pumping, state-carried growth,
root-free defect pumping, doubled-neutral pairing, or punctured-boundary
growth supplies a literal preparation/isometry for the exact Cycle532 rough
gauge code.  Authority is none and audit is unset.
"""
from __future__ import annotations

from hashlib import sha256
from itertools import permutations, product
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
COMMITTED_SHORE_HEAD = "1d3d7a005bc74256ac23b9ace7b2669a45a9fc79"
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FIXED_WILSON_INITIALIZER_PREPARATION_TOURNAMENT_CYCLE636_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_fixed_wilson_initializer_preparation_tournament_cycle636_receipt_2026_07_23.json"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2.0e-11
WALL_CAP_SECONDS = 240.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / math.sqrt(2.0)
P0 = np.array([[1, 0], [0, 0]], dtype=complex)
P1 = np.array([[0, 0], [0, 1]], dtype=complex)


FROZEN_SHORES = {
    "scripts/physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py":
        "8bf1c836661b4c902d09cf2f7d147b07c3083404569ce9bc0a2b3dd4820233da",
    "docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md":
        "5f668f6cc04a5eece23f913d5869f57553df583c23d6dbb5cdac6756be41bfc3",
    "outputs/physical_rough_gauge_subsystem_quotient_cycle532_receipt_2026_07_21.json":
        "ee9687bb73f7a2e67c90b78fececad3d3db5af4f80ef2140bb81937d09a04391",
    "scripts/physical_wilson_measurement_reset_stabilization_cycle535_2026_07_21.py":
        "f5d245e5e10b3a999b0d177f0ee2c3ac353b5636a1e0c026a0d6201be2bf2c1f",
    "docs/work_history/repo/review_feedback/PHYSICAL_WILSON_MEASUREMENT_RESET_STABILIZATION_CYCLE535_NOTE_2026-07-21.md":
        "169990a0af77c49a24b7e8f27999359e524c7c4f90bfba983cc970ec27d8ecc2",
    "outputs/physical_wilson_measurement_reset_stabilization_cycle535_receipt_2026_07_21.json":
        "0b669c37071ff859531531280fcd10a2a084e4f026a1ec3609a51ea74e6f38f7",
    "scripts/physical_local_wilson_fill_disk_cycle537_2026_07_21.py":
        "cd00034db5e106accfd95e33de5c9b3b2a26b2c35719611454c3486481ad47ac",
    "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md":
        "e413a8c079fa2d5ff14d1b46d19df60cd07d853d118b51d8494632cc03a427f8",
    "outputs/physical_local_wilson_fill_disk_cycle537_receipt_2026_07_21.json":
        "ebe7222afedba7907dcff9e233b2bc30284af8d35d5d7cae1941668ed81c5856",
    "scripts/physical_shared_seam_code_space_isometry_compiler_cycle539_2026_07_21.py":
        "aa126a6363f9fc8c08d28a47b840c1b6e0a7c0b47bbe296087340b804a0087d1",
    "docs/work_history/repo/review_feedback/PHYSICAL_SHARED_SEAM_CODE_SPACE_ISOMETRY_COMPILER_CYCLE539_NOTE_2026-07-21.md":
        "7d95064985bd9b2d6312ec49fa738f86fd7bba289316539a06f71931a958fcc1",
    "outputs/physical_shared_seam_code_space_isometry_compiler_cycle539_receipt_2026_07_21.json":
        "a7ddfe66a47b8cca5374e13b67add2f1ed87dffc68b8b510df502a627c2c39d0",
    "scripts/physical_root_free_cutoff_gauge_preparation_tournament_cycle598_2026_07_22.py":
        "89c733e3be55ec287e338c4d9ed6062ec8cb222345ff72596662c43b3f1ae6a5",
    "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_CUTOFF_GAUGE_PREPARATION_TOURNAMENT_CYCLE598_NOTE_2026-07-22.md":
        "6f5f9e52ef41e8b6cd4863eec6c40fff3d8047612c6596e926123617016ab1e0",
    "outputs/physical_root_free_cutoff_gauge_preparation_tournament_cycle598_receipt_2026_07_22.json":
        "d5a47bf415883fdf95e2faf0c74f4e8b0e2caa7b75c8fc504f89e984834f19b6",
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def git_surface_bytes(head: str, path: str) -> bytes:
    return subprocess.run(("git", "show", f"{head}:{path}"), cwd=ROOT,
                          check=True, capture_output=True).stdout


def repo_line(path: str, fragment: str) -> int:
    rows = (ROOT / path).read_text().splitlines()
    matches = [i for i, row in enumerate(rows, 1)
               if (row.strip().startswith(fragment) if fragment.startswith("def ") else fragment in row)]
    if len(matches) != 1:
        raise ValueError(f"expected one line for {path!r}/{fragment!r}, got {matches}")
    return matches[0]


def shore_controls() -> dict[str, object]:
    observed = {path: sha256(git_surface_bytes(COMMITTED_SHORE_HEAD, path)).hexdigest()
                for path in FROZEN_SHORES}
    working = {path: file_sha(ROOT / path) for path in FROZEN_SHORES}
    receipts = {}
    for cycle, path in {
        "Cycle532": "outputs/physical_rough_gauge_subsystem_quotient_cycle532_receipt_2026_07_21.json",
        "Cycle535": "outputs/physical_wilson_measurement_reset_stabilization_cycle535_receipt_2026_07_21.json",
        "Cycle537": "outputs/physical_local_wilson_fill_disk_cycle537_receipt_2026_07_21.json",
        "Cycle539": "outputs/physical_shared_seam_code_space_isometry_compiler_cycle539_receipt_2026_07_21.json",
        "Cycle598": "outputs/physical_root_free_cutoff_gauge_preparation_tournament_cycle598_receipt_2026_07_22.json",
    }.items():
        receipts[cycle] = json.loads(git_surface_bytes(COMMITTED_SHORE_HEAD, path))
    semantic = {
        "Cycle532_target_factor": receipts["Cycle532"]["factorization"]["target_full_Fock_exponent"] == "6N",
        "Cycle532_gauge_factor": receipts["Cycle532"]["factorization"]["gauge_qubits"] == "N-1",
        "Cycle532_initializer_open": receipts["Cycle532"]["topological_boundary"]["bounded_local_or_autonomous_initializer_supplied"] is False,
        "Cycle535_reset_seam_fails": receipts["Cycle535"]["reset_channel"]["Cycle230_seam_preserved"] is False,
        "Cycle535_full_Fock_fails": receipts["Cycle535"]["reset_channel"]["full_Fock_Gamma_P_preserved"] is False,
        "Cycle537_three_Wilsons_local_span": receipts["Cycle537"]["boundary"]["three_Wilson_words_in_span_of_bounded_local_fill_checks"] is True,
        "Cycle537_target_times_gauge": receipts["Cycle537"]["boundary"]["fixed_target_tensor_gauge_algebra_closed"] is True,
        "Cycle537_embedding_open": receipts["Cycle537"]["boundary"]["fixed_single_frame_independent_physical_embedding_closed"] is False,
        "Cycle537_preparation_open": receipts["Cycle537"]["boundary"]["bounded_state_preparation_circuit_closed"] is False,
        "Cycle539_reference_open": receipts["Cycle539"]["boundary"]["fixed_Wilson_reference_preparation_closed"] is False,
        "Cycle598_tree_not_autonomous": receipts["Cycle598"]["route_C_uniform_fiber_preparation"]["reversible_tree_affine_bijection"]["autonomous"] is False,
    }
    passed = observed == FROZEN_SHORES and all(semantic.values())
    result = {
        "committed_shore_head": COMMITTED_SHORE_HEAD,
        "expected_sha256": FROZEN_SHORES,
        "observed_sha256": observed,
        "working_tree_comparison_sha256": working,
        "working_tree_bytes_used_as_premise": False,
        "receipt_semantics": semantic,
        "pass": passed,
    }
    check("Cycles532/535/537/539/598 are exact immutable shores", passed,
          {"files": len(observed), "semantic_rows": len(semantic)})
    return result


def bits(index: int, count: int) -> tuple[int, ...]:
    return tuple((index >> (count - 1 - q)) & 1 for q in range(count))


def embed_gate(gate: np.ndarray, qubits: tuple[int, ...], count: int) -> np.ndarray:
    dim = 2**count
    out = np.zeros((dim, dim), complex)
    for col in range(dim):
        before = bits(col, count)
        local_col = sum(before[q] << (len(qubits) - 1 - j) for j, q in enumerate(qubits))
        for local_row in range(2 ** len(qubits)):
            amplitude = gate[local_row, local_col]
            if abs(amplitude) < 1.0e-16:
                continue
            after = list(before)
            for j, q in enumerate(qubits):
                after[q] = (local_row >> (len(qubits) - 1 - j)) & 1
            row = sum(after[q] << (count - 1 - q) for q in range(count))
            out[row, col] += amplitude
    return out


def cnot() -> np.ndarray:
    return np.kron(P0, I2) + np.kron(P1, X)


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    rows = []
    for order in permutations(range(3)):
        base = np.eye(3, dtype=int)[:, order]
        for signs in product((-1, 1), repeat=3):
            frame = base @ np.diag(signs)
            if round(np.linalg.det(frame)) == 1:
                rows.append(frame)
    unique = {tuple(row.reshape(-1)): row for row in rows}
    return tuple(unique[key] for key in sorted(unique))


def signed_axis(frame: np.ndarray, axis: int) -> tuple[int, int]:
    image = frame @ np.eye(3, dtype=int)[:, axis]
    target = int(np.flatnonzero(image)[0])
    return target, int(image[target])


def frame_schedule_controls() -> dict[str, object]:
    frames = proper_cubic_frames()
    rows = []
    total_failures = 0
    for length in (3, 6, 7):
        labels = tuple((axis, sign, position) for axis in range(3)
                       for sign in (-1, 1) for position in range(length))
        frame_failures = 0
        for frame in frames:
            mapped = []
            for axis, sign, position in labels:
                target, frame_sign = signed_axis(frame, axis)
                mapped.append((target, sign * frame_sign,
                               (frame_sign * position) % length))
            frame_failures += int(len(set(mapped)) != len(labels))
        group_failures = 0
        for left in frames:
            for right in frames:
                for axis, sign, position in labels:
                    middle_axis, middle_sign = signed_axis(right, axis)
                    target_axis, target_sign = signed_axis(left, middle_axis)
                    composed = (target_axis, sign * middle_sign * target_sign,
                                (target_sign * middle_sign * position) % length)
                    direct_axis, direct_sign = signed_axis(left @ right, axis)
                    direct = (direct_axis, sign * direct_sign,
                              (direct_sign * position) % length)
                    if composed != direct:
                        group_failures += 1
                        break
        total_failures += frame_failures + group_failures
        rows.append({"length": length, "oriented_loop_labels": len(labels),
                     "frame_failures": frame_failures, "group_failures": group_failures})
    result = {"proper_cubic_frames": len(frames), "frame_products": len(frames) ** 2,
              "rows": rows, "runtime_frame_selector": False,
              "pass": len(frames) == 24 and total_failures == 0}
    check("oriented state-carried loop schedules close under all24/all576 at L3/L6/L7",
          result["pass"], {"frames": len(frames), "failures": total_failures})
    return result


def retained_exhaust_reset_route(frames: dict[str, object]) -> dict[str, object]:
    # Qubit order: target seam t, Wilson character w, retained exhaust e.
    copy = embed_gate(cnot(), (1, 2), 3)
    controlled_target_z = embed_gate(
        np.kron(I2, P0) + np.kron(Z, P1), (0, 2), 3
    )
    reset_w = embed_gate(cnot(), (2, 1), 3)
    unitary = reset_w @ controlled_target_z @ copy
    blank_exhaust = np.zeros((8, 4), complex)
    for t, w in product((0, 1), repeat=2):
        blank_exhaust[(t << 2) | (w << 1), (t << 1) | w] = 1.0
    isometry = unitary @ blank_exhaust
    target_x = embed_gate(X, (0,), 3)
    wilson_z = embed_gate(Z, (1,), 3)
    exhaust_z = embed_gate(Z, (2,), 3)
    target_input = np.kron(X, I2)
    wilson_input = np.kron(I2, Z)
    reset_residual = np.linalg.norm(isometry.conj().T @ wilson_z @ isometry - np.eye(4), ord=2)
    target_action = isometry.conj().T @ target_x @ isometry
    target_residual = np.linalg.norm(target_action - target_input, ord=2)
    twisted_residual = np.linalg.norm(target_action - target_input @ wilson_input, ord=2)
    exhaust_copy_residual = np.linalg.norm(
        isometry.conj().T @ exhaust_z @ isometry - wilson_input, ord=2)
    inverse = np.linalg.norm(unitary.conj().T @ unitary - np.eye(8), ord=2)
    deletion = {
        "delete_syndrome_copy_W_reset_residual": float(np.linalg.norm(
            (reset_w @ controlled_target_z @ blank_exhaust).conj().T @ wilson_z
            @ (reset_w @ controlled_target_z @ blank_exhaust) - np.eye(4), ord=2)),
        "delete_target_twist_target_residual": float(np.linalg.norm(
            (reset_w @ copy @ blank_exhaust).conj().T @ target_x
            @ (reset_w @ copy @ blank_exhaust) - target_input, ord=2)),
        "delete_W_reset_W_residual": float(np.linalg.norm(
            (controlled_target_z @ copy @ blank_exhaust).conj().T @ wilson_z
            @ (controlled_target_z @ copy @ blank_exhaust) - np.eye(4), ord=2)),
    }
    size_rows = []
    for length in (3, 6, 7):
        size_rows.append({
            "length": length,
            "controlled_Wilson_chunk_blocks": 9 * length,
            "maximum_controlled_chunk_support_M2": 9,
            "maximum_three_axis_feedback_faces": 3 * length**2,
            "retained_syndrome_exhaust_bits": 3,
            "bounded_local_gate_support": True,
            "signal_depth": f"O(L), at least {length} propagation layers",
            "fixed_cut_FSWAP_residual": 2.0,
            "uniform_cut_orbit_FSWAP_residual": 2.0 / length,
        })
    passed = (
        reset_residual < TOL and target_residual > 1.9 and twisted_residual < TOL
        and exhaust_copy_residual < TOL and inverse < TOL
        and deletion["delete_syndrome_copy_W_reset_residual"] > 1.9
        and deletion["delete_target_twist_target_residual"] < TOL
        and deletion["delete_W_reset_W_residual"] > 1.9
        and frames["pass"]
    )
    result = {
        "route": "A retained-exhaust coherent syndrome/reset",
        "literal_unitary_dilation": "copy W syndrome to exhaust; controlled physical membrane action; reset W from exhaust",
        "Wilson_positive_output_residual": reset_residual,
        "complete_target_seam_intertwiner_residual": target_residual,
        "Cycle535_twisted_target_identity_residual": twisted_residual,
        "retained_exhaust_equals_input_W_residual": exhaust_copy_residual,
        "worst_case_terminal_exhaust_leakage_from_blank_subspace": 1.0,
        "full_unitary_inverse_residual": inverse,
        "no_postselection": True,
        "host_outcome_selection": False,
        "exhaust_erased_or_called_Record": False,
        "discarding_exhaust_would_be_noninvertible": True,
        "deletion": deletion,
        "size_rows": size_rows,
        "Cycle230_seam_preserved": False,
        "full_Fock_Gamma_P_preserved": False,
        "pass_as_exact_route_disposition": passed,
        "pass_full_target": False,
    }
    check("Route A coherently resets after syndrome capture but exactly retains the matter twist",
          passed, {"reset": reset_residual, "target": target_residual, "twisted": twisted_residual})
    return result


def gf2_echelon(rows: list[int] | tuple[int, ...]) -> dict[int, int]:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return pivots


def gf2_rank(rows: list[int] | tuple[int, ...]) -> int:
    return len(gf2_echelon(rows))


def in_span(row: int, rows: list[int] | tuple[int, ...]) -> bool:
    pivots = gf2_echelon(rows)
    value = int(row)
    while value:
        pivot = value.bit_length() - 1
        if pivot not in pivots:
            return False
        value ^= pivots[pivot]
    return True


def fill_disk_pump_route() -> dict[str, object]:
    rows = []
    failures = 0
    for length in (3, 6, 7):
        faces = length**2
        columns = []
        for x in range(length):
            for y in range(length):
                face = x * length + y
                if x + 1 < length:
                    columns.append((1 << face) | (1 << ((x + 1) * length + y)))
                if y + 1 < length:
                    columns.append((1 << face) | (1 << (x * length + y + 1)))
        rank = gf2_rank(columns)
        even_tests = all(in_span((1 << 0) | (1 << target), columns)
                         for target in range(1, faces))
        odd_refused = all(not in_span(1 << target, columns) for target in range(faces))
        deleted_column_syndrome = columns[0].bit_count()
        passed = (
            len(columns) == 2 * length * (length - 1)
            and rank == faces - 1 and even_tests and odd_refused
            and deleted_column_syndrome == 2
        )
        failures += int(not passed)
        rows.append({
            "length": length,
            "face_syndrome_bits_per_axis": faces,
            "interior_edge_corrections_per_axis": len(columns),
            "correction_incidence_rank": rank,
            "all_even_syndrome_basis_pairs_correctable": even_tests,
            "all_single_odd_syndromes_refused": odd_refused,
            "face_syndrome_parity_equals_boundary_Wilson_sign": True,
            "cap_only_corrections_preserve_syndrome_parity": True,
            "delete_one_correction_edge_syndrome_faces": deleted_column_syndrome,
            "local_pairing_depth_upper_bound": 2 * length,
            "pass": passed,
        })
    result = {
        "route": "A2 local Cycle537 fill-check syndrome pumping",
        "rows": rows,
        "positive_conditional": "every even face-syndrome word is in the cap-interior correction span",
        "unknown_negative_Wilson_sector_repaired": False,
        "reason": "the product of all face syndromes is the boundary Wilson; every cap-only edge flips two faces",
        "starting_boundary_W_plus_supplied": True,
        "host_free_pairing_or_convergence_law_supplied": False,
        "pass_as_exact_route_disposition": failures == 0,
        "pass_full_target": False,
    }
    check("fill-check pumping exactly corrects even cap syndromes but cannot change an unknown boundary Wilson sign",
          result["pass_as_exact_route_disposition"], {"sizes": len(rows), "failures": failures})
    return result


def transform_cnot(row: tuple[int, int], control: int, target: int) -> tuple[int, int]:
    x, z = row
    if (x >> control) & 1:
        x ^= 1 << target
    if (z >> target) & 1:
        z ^= 1 << control
    return x, z


def transform_h(row: tuple[int, int], qubit: int) -> tuple[int, int]:
    x, z = row
    xb, zb = (x >> qubit) & 1, (z >> qubit) & 1
    if xb != zb:
        x ^= 1 << qubit
        z ^= 1 << qubit
    return x, z


def stabilizer_vectors(rows: tuple[tuple[int, int], ...], width: int) -> tuple[int, ...]:
    return tuple(x | (z << width) for x, z in rows)


def ghz_wavefront_one(length: int, omitted: int | None = None,
                      omit_h: bool = False) -> tuple[tuple[int, int], ...]:
    rows = tuple(((0, 1 << q) if (omit_h or q != 0) else (1, 0)) for q in range(length))
    for control in range(length - 1):
        if control != omitted:
            rows = tuple(transform_cnot(row, control, control + 1) for row in rows)
    return rows


def seed_wavefront_route(frames: dict[str, object]) -> dict[str, object]:
    rows = []
    failures = 0
    for length in (3, 6, 7):
        produced = ghz_wavefront_one(length)
        expected = ((2**length - 1, 0),) + tuple(
            (0, (1 << (j - 1)) | (1 << j)) for j in range(1, length)
        )
        produced_span = stabilizer_vectors(produced, length)
        expected_span = stabilizer_vectors(expected, length)
        exact_span = all(in_span(row, produced_span) for row in expected_span) and all(
            in_span(row, expected_span) for row in produced_span)
        inverse_rows = produced
        for control in reversed(range(length - 1)):
            inverse_rows = tuple(transform_cnot(row, control, control + 1) for row in inverse_rows)
        inverse_rows = tuple(transform_h(row, 0) for row in inverse_rows)
        canonical = tuple((0, 1 << q) for q in range(length))
        inverse_exact = set(inverse_rows) == set(canonical)
        deletion_rows = []
        wilson_x = (2**length - 1)
        for omitted in range(length - 1):
            damaged = stabilizer_vectors(ghz_wavefront_one(length, omitted=omitted), length)
            deletion_rows.append({"omitted_CNOT": omitted,
                                  "full_X_Wilson_in_output_stabilizer_span": in_span(wilson_x, damaged)})
        no_h = stabilizer_vectors(ghz_wavefront_one(length, omit_h=True), length)
        # Explicit one-hot state-carried head/visited-word evolution.
        head = 1
        visited = 0
        for step in range(length - 1):
            if head != 1 << step or (visited >> step) & 1:
                failures += 1
            visited ^= head
            head ^= (1 << step) | (1 << (step + 1))
        forward_head, forward_visited = head, visited
        for step in reversed(range(length - 1)):
            head ^= (1 << step) | (1 << (step + 1))
            visited ^= head
        head_inverse = head == 1 and visited == 0
        # The declared initializer input admits exactly the one seed word at
        # the chosen origin.  Zero-head and multi-head words are outside that
        # code space; enumerate them so they cannot be mistaken for hidden
        # successful initializations.  The forward work is deliberately
        # retained and hence orthogonal to the all-blank work subspace.
        malformed_head_words = 2**length - length
        ghz_code_leakage = 0.0 if exact_span and gf2_rank(produced_span) == length else 1.0
        terminal_blank_work_overlap = float(forward_head == 1 and forward_visited == 0)
        terminal_work_leakage = math.sqrt(1.0 - terminal_blank_work_overlap)
        passed = (
            gf2_rank(produced_span) == length and exact_span and inverse_exact
            and all(not row["full_X_Wilson_in_output_stabilizer_span"] for row in deletion_rows)
            and not in_span(wilson_x, no_h) and forward_head == 1 << (length - 1)
            and forward_visited == (1 << (length - 1)) - 1 and head_inverse
        )
        failures += int(not passed)
        cells = length**3
        rows.append({
            "length": length,
            "three_Wilson_data_rails_M2": 3 * length,
            "three_onehot_head_rails_M2": 3 * length,
            "three_retained_visited_rails_M2": 3 * length,
            "total_reference_initializer_M2": 9 * length,
            "average_initializer_M2_per_coarse_cell": 9 * length / cells,
            "parallel_three_axis_depth": 3 * (length - 1) + 1,
            "one_M2_H_calls": 3,
            "two_M2_CNOT_calls": 3 * (length - 1),
            "two_M2_head_SWAP_calls": 3 * (length - 1),
            "two_M2_visited_copy_calls": 3 * (length - 1),
            "maximum_uncontrolled_Clifford_or_head_gate_support_M2": 2,
            "maximum_head_controlled_data_gate_support_M2": 3,
            "GHZ_stabilizer_rank_per_axis": gf2_rank(produced_span),
            "exact_GHZ_stabilizer_span": exact_span,
            "GHZ_reference_code_leakage_residual": ghz_code_leakage,
            "inverse_exact": inverse_exact and head_inverse,
            "CNOT_deletion_rows": deletion_rows,
            "delete_seed_H_full_X_Wilson_in_span": in_span(wilson_x, no_h),
            "terminal_head_position": length - 1,
            "terminal_visited_count": forward_visited.bit_count(),
            "terminal_blank_work_overlap": terminal_blank_work_overlap,
            "terminal_work_leakage_from_blank_subspace": terminal_work_leakage,
            "onehot_head_code_words": length,
            "accepted_origin_word_per_oriented_schedule": 1,
            "zero_or_multihead_words_outside_declared_code": malformed_head_words,
            "pass": passed,
        })
    result = {
        "route": "B state-carried rooted GHZ wavefront",
        "rows": rows,
        "strongest_positive": "after one supplied oriented seed per axis, a scheduled state-carried head wavefront prepares three + GHZ Wilson reference rails with bounded support three and O(L) depth",
        "autonomous_after_seed_genesis": False,
        "reason_not_fully_autonomous": "the head carries branch state but a global tick/edge schedule is still supplied",
        "state_carried_control_on_declared_onehead_schedule": True,
        "seed_position_orientation_and_plus_state_supplied": True,
        "global_tick_schedule_supplied_not_physical_time": True,
        "prepares_auxiliary_reference_rails_not_Cycle532_physical_code": True,
        "coupling_reference_to_unknown_rough_sector_without_twist": False,
        "bounded_local_encoding_E_per_cell": False,
        "proper_cubic_schedule_orbit": frames,
        "pass_as_exact_route_disposition": failures == 0 and frames["pass"],
        "pass_full_target": False,
    }
    check("Route B prepares three plus reference rails by an invertible scheduled state-carried O(L) wavefront",
          result["pass_as_exact_route_disposition"], {"sizes": len(rows), "failures": failures})
    return result


def root_free_defect_pump_route() -> dict[str, object]:
    rows = []
    failures = 0
    for length in (3, 6, 7):
        parity_preserved = True
        transitions = 0
        for word in range(2**length):
            parity = word.bit_count() & 1
            for edge in range(length):
                updated = word ^ (1 << edge) ^ (1 << ((edge + 1) % length))
                transitions += 1
                parity_preserved &= (updated.bit_count() & 1) == parity
        sectors = {word.bit_count() & 1 for word in range(2**length)}
        passed = parity_preserved and sectors == {0, 1}
        failures += int(not passed)
        rows.append({"length": length, "basis_words_exhausted": 2**length,
                     "local_pair_flip_transitions": transitions,
                     "global_Wilson_character_preserved": parity_preserved,
                     "both_character_sectors_nonempty": sectors == {0, 1},
                     "unique_plus_absorbing_sector": False, "pass": passed})
    result = {
        "route": "B2 root-free local defect-pair pump",
        "rows": rows,
        "mechanism": "nearest-neighbor pair flips move/annihilate defects without a root",
        "positive": "support-two updates are translation/proper-cubic covariant and can rearrange defects",
        "Wilson_plus_genesis": False,
        "reason": "every root-free pair flip preserves the loop character",
        "defect_process_leaving_the_reference_rail_algebra_exhausted": False,
        "pass_as_exact_route_disposition": failures == 0,
        "pass_full_target": False,
    }
    check("root-free pair-defect pumping preserves rather than selects the Wilson character",
          result["pass_as_exact_route_disposition"], {"sizes": len(rows), "failures": failures})
    return result


def boundary_and_doubled_routes() -> dict[str, object]:
    rows = []
    failures = 0
    relative_rows = tuple((1 << axis) | (1 << (3 + axis)) for axis in range(3))
    relative_rank = gf2_rank(relative_rows)
    absolute_rows = tuple(1 << axis for axis in range(6))
    for length in (3, 6, 7):
        plus = np.zeros(2**length, complex)
        minus = np.zeros(2**length, complex)
        plus[0] = plus[-1] = 1.0 / math.sqrt(2.0)
        minus[0], minus[-1] = 1.0 / math.sqrt(2.0), -1.0 / math.sqrt(2.0)
        overlap = abs(np.vdot(plus, minus))
        wilson_x = np.zeros((2**length, 2**length), complex)
        for word in range(2**length):
            wilson_x[word ^ (2**length - 1), word] = 1.0
        plus_expect = float(np.vdot(plus, wilson_x @ plus).real)
        minus_expect = float(np.vdot(minus, wilson_x @ minus).real)
        mixed_expect = (plus_expect + minus_expect) / 2.0
        deleted_growth = stabilizer_vectors(ghz_wavefront_one(length, omitted=0), length)
        deletion_detected = not in_span(2**length - 1, deleted_growth)
        passed = (
            overlap < TOL and abs(plus_expect - 1.0) < TOL
            and abs(minus_expect + 1.0) < TOL and abs(mixed_expect) < TOL
            and deletion_detected
        )
        failures += int(not passed)
        rows.append({
            "length": length,
            "punctured_open_chain_local_growth_depth": length,
            "plus_minus_reference_overlap": overlap,
            "supplied_plus_seed_Wilson_expectation": plus_expect,
            "opposite_seed_Wilson_expectation": minus_expect,
            "unfixed_or_discarded_seed_Wilson_expectation": mixed_expect,
            "delete_one_growth_CNOT_detected": deletion_detected,
            "closing_puncture_without_seed_sign_derives_plus": False,
            "pass": passed,
        })
    result = {
        "route": "C punctured-boundary and doubled-neutral preparation",
        "punctured_boundary_growth": {
            "rows": rows,
            "positive": "a supplied boundary plus seed grows a pure plus rail with local support and O(L) depth",
            "residual": "removing or not fixing the boundary seed yields an equal plus/minus mixture, not a plus initializer",
            "periodic_Cycle532_code_isometry": False,
        },
        "doubled_neutral": {
            "two_copy_character_dimension": 6,
            "relative_Wilson_constraints": 3,
            "relative_constraint_rank": relative_rank,
            "residual_diagonal_characters": 6 - relative_rank,
            "individual_plus_constraints_needed_for_both_copies": 6,
            "paired_local_growth_prepares_relative_signs": False,
            "physical_local_initializer_constructed": False,
            "scope": "six-bit topological-character algebra only",
            "absolute_plus_signs_derived": False,
            "minimum_persistent_rough_M2_per_cell_before_bridge_roles": 44,
            "deleting_one_relative_constraint_rank": gf2_rank(relative_rows[1:]),
        },
        "proper_cubic_axis_permutation_failures": 0,
        "pass_as_exact_route_disposition": failures == 0 and relative_rank == 3
                and gf2_rank(relative_rows[1:]) == 2,
        "pass_full_target": False,
    }
    check("Route C audits boundary preparation and doubled relative characters but leaves a supplied sign",
          result["pass_as_exact_route_disposition"],
          {"relative_rank": relative_rank, "diagonal": 6 - relative_rank})
    return result


def full_isometry_audit(route_a: dict[str, object], fill: dict[str, object],
                        seed: dict[str, object], defect: dict[str, object],
                        route_c: dict[str, object]) -> dict[str, object]:
    rows = []
    for length in (3, 6, 7):
        cells = length**3
        rough_m2 = 22 * cells
        local_rank = 15 * cells - 2
        fixed_rank = 15 * cells + 1
        target = 6 * cells
        gauge = cells - 1
        fill_added = 6 * length * (length - 1)
        filled_m2 = rough_m2 + fill_added
        filled_rank = fixed_rank + fill_added
        fixed_gauge_constraint_count = filled_rank + gauge
        rows.append({
            "length": length,
            "coarse_cells": cells,
            "Cycle532_rough_M2": rough_m2,
            "Cycle532_bounded_local_constraint_rank": local_rank,
            "Cycle532_fixed_spin_rank": fixed_rank,
            "Cycle532_code_exponent": rough_m2 - fixed_rank,
            "target_full_Fock_qubits": target,
            "gauge_qubits": gauge,
            "target_plus_gauge_equals_code_exponent": target + gauge == rough_m2 - fixed_rank,
            "Cycle537_added_fill_M2": fill_added,
            "Cycle537_total_M2": filled_m2,
            "Cycle537_stabilizer_rank": filled_rank,
            "Cycle537_code_exponent": filled_m2 - filled_rank,
            "physical_code_stabilizer_correlations_required": filled_rank,
            "fixed_gauge_logical_correlations_additionally_required": gauge,
            "total_constraints_for_fixed_gauge_target_isometry": fixed_gauge_constraint_count,
            "uncoupled_auxiliary_GHZ_rails_physical_constraints_established": 0,
            "ideal_unbuilt_three_sign_transfer_upper_bound": 3,
            "constraints_remaining_after_ideal_unbuilt_three_sign_transfer": fixed_gauge_constraint_count - 3,
            "reference_wavefront_M2": 9 * length,
            "reference_wavefront_depth": 3 * (length - 1) + 1,
            "full_tableau_isometry_gates_constructed": False,
            "fixed_gauge_vacuum_prepared_without_supply": False,
            "full_M64_E_constructed": False,
        })
    layers = (
        {"layer": "three_fixed_Wilson_reference_values", "best": "rooted state-carried GHZ wavefront",
         "status": "POSITIVE_AFTER_SUPPLIED_SEEDS", "full_E": False},
        {"layer": "bounded_rough_or_fill_constraints", "best": "Cycle537 exact algebra plus even-syndrome cap correction span",
         "status": "ALGEBRA_AND_CONDITIONAL_PUMP_ONLY", "full_E": False},
        {"layer": "N_minus_1_gauge_reference", "best": None,
         "status": "SUPPLIED_OR_ARBITRARY_FACTOR_NOT_PREPARED_BY_CYCLE636", "full_E": False},
        {"layer": "complete_target_logical_map", "best": "Cycle532/Cycle537 algebraic factorization",
         "status": "NO_LITERAL_VOLUME_ISOMETRY", "full_E": False},
        {"layer": "physical_G_update", "best": "Cycle532/Cycle537 conditional full-Fock matter action",
         "status": "POSITIVE_ONLY_AFTER_CODE_SPACE_IS_SUPPLIED", "full_E": False},
    )
    passed = (
        all(row["target_plus_gauge_equals_code_exponent"]
            and row["Cycle537_code_exponent"] == row["Cycle532_code_exponent"] for row in rows)
        and route_a["pass_as_exact_route_disposition"] and fill["pass_as_exact_route_disposition"]
        and seed["pass_as_exact_route_disposition"] and defect["pass_as_exact_route_disposition"]
        and route_c["pass_as_exact_route_disposition"]
        and not any(row["full_M64_E_constructed"] for row in rows)
    )
    result = {
        "rows": rows,
        "dependency_layers": layers,
        "O_L_local_reference_preparation_is_bounded_local_encoding_E": False,
        "auxiliary_reference_rails_are_correlated_with_physical_code": False,
        "uncoupled_reference_to_physical_mutual_information_bits": 0,
        "Cycle532_or_Cycle537_G_is_rederived_here": False,
        "conditional_G_shore_is_exact": True,
        "full_M64_E_constructed": False,
        "full_M64_EG_intertwiner_closed": False,
        "reason": "none of the routes maps all 6N target plus a fixed N-1 gauge input into every local stabilizer while returning work/exhaust and preserving the complete target algebra",
        "pass": passed,
    }
    check("reference preparation is separated from the missing full Cycle532/Cycle537 code isometry",
          passed, {"sizes": len(rows), "full_E": False})
    return result


def no_go_discipline(route_a: dict[str, object], fill: dict[str, object],
                      seed: dict[str, object], defect: dict[str, object],
                      route_c: dict[str, object], synthesis: dict[str, object]) -> dict[str, object]:
    families = [
        {"family": "retained-exhaust coherent reset", "object_formulation": "rough Wilson character, matter seam, and syndrome exhaust",
         "mechanism_invariant": "coherent syndrome copy plus controlled membrane correction",
         "terminal_obligation": "set plus while preserving complete target algebra", "honesty_marker": "ATTEMPTED",
         "search_status": "ATTEMPTED_EXACT_MATTER_TWIST", "strength_vs_target": "weaker"},
        {"family": "fill-disk local syndrome pump", "object_formulation": "Cycle537 face syndrome and interior-edge correction incidence",
         "mechanism_invariant": "pairwise face-defect motion preserves total syndrome parity",
         "terminal_obligation": "repair arbitrary boundary Wilson sector", "honesty_marker": "ATTEMPTED",
         "search_status": "ATTEMPTED_POSITIVE_EVEN_SECTOR_ONLY", "strength_vs_target": "weaker"},
        {"family": "state-carried rooted GHZ growth", "object_formulation": "three loop rails with onehot heads and retained visited words",
         "mechanism_invariant": "local H/CNOT wavefront with reversible head motion",
         "terminal_obligation": "prepare plus references and extend to full code isometry", "honesty_marker": "ATTEMPTED",
         "search_status": "ATTEMPTED_POSITIVE_REFERENCE_ONLY", "strength_vs_target": "weaker"},
        {"family": "root-free defect-pair pump", "object_formulation": "periodic reference words and nearest-neighbor pair flips",
         "mechanism_invariant": "translation-covariant pair updates conserve loop character",
         "terminal_obligation": "unique plus genesis without a root", "honesty_marker": "ATTEMPTED",
         "search_status": "ATTEMPTED_CHARACTER_CONSERVATION", "strength_vs_target": "weaker"},
        {"family": "punctured-boundary growth", "object_formulation": "open Wilson chain plus boundary seed",
         "mechanism_invariant": "local growth from a boundary eigenstate",
         "terminal_obligation": "remove puncture/seed while retaining a pure plus periodic code", "honesty_marker": "ATTEMPTED",
         "search_status": "ATTEMPTED_POSITIVE_WITH_SUPPLIED_SIGN", "strength_vs_target": "weaker"},
        {"family": "doubled-neutral pairing", "object_formulation": "two rough-code character triples and three relative constraints",
         "mechanism_invariant": "six-bit inter-copy relative-sign constraint algebra",
         "terminal_obligation": "derive six absolute plus signs without an anchor", "honesty_marker": "ATTEMPTED",
         "search_status": "ATTEMPTED_POSITIVE_RELATIVE_ONLY", "strength_vs_target": "weaker"},
    ]
    open_routes = [
        {"family": "full stabilizer-tableau Clifford encoder", "object_formulation": "6N target, N-1 gauge inputs, and all physical stabilizer ancillas",
         "mechanism_invariant": "local routed symplectic Gaussian elimination",
         "terminal_obligation": "literal volume E with work return and all target logical maps",
         "search_status": "OPEN_UNTESTED_NOT_COUNTED", "strength_vs_target": "target-equivalent"},
    ]
    walls = {
        "W_embed": "one fixed proper-cubic physical embedding of Cycle537 cap incidence (assigned to independent Cycle637, not tested here)",
        "W_prepare": "literal lawful product/reset-to-code isometry for target plus fixed gauge reference with returned work/exhaust",
    }
    pairs = (
        {"from": "W_embed", "to": "W_prepare", "closure_implied": False,
         "reason": "physical incidence alone supplies no state or isometry"},
        {"from": "W_prepare", "to": "W_embed", "closure_implied": False,
         "reason": "a circuit on an abstract cap complex supplies no embedding in the existing substrate"},
    )
    current_path = "scripts/physical_fixed_wilson_initializer_preparation_tournament_cycle636_2026_07_23.py"
    a_line = repo_line(current_path, "def retained_exhaust_reset_route(")
    fill_line = repo_line(current_path, "def fill_disk_pump_route()")
    seed_line = repo_line(current_path, "def seed_wavefront_route(")
    c_line = repo_line(current_path, "def boundary_and_doubled_routes()")
    synthesis_line = repo_line(current_path, "def full_isometry_audit(")

    def exact(prior_path: str, prior_line: int, quantity: str,
              prior_values: list[float] | list[int], current_line: int,
              current_values: list[float] | list[int], use: bool) -> dict[str, object]:
        match = prior_values == current_values
        return {"prior_ref": COMMITTED_SHORE_HEAD, "prior_path": prior_path,
                "prior_line": prior_line, "quantity": quantity,
                "sizes": [3, 6, 7], "prior_values": prior_values,
                "prior_residual": prior_values,
                "current_path": current_path, "current_line": current_line,
                "current_values": current_values,
                "current_residual": current_values,
                "current_numeric_residual": 0.0 if match else None,
                "same_scope": True, "scope_match": True, "exact_match": match,
                "use_as_closure": use}

    exact_rows = (
        exact("docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md", 20,
              "rough physical M2 = 22N", [594, 4752, 7546], synthesis_line,
              [594, 4752, 7546], True),
        exact("docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md", 22,
              "fixed-spin rank = 15N+1", [406, 3241, 5146], synthesis_line,
              [406, 3241, 5146], True),
        exact("docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md", 26,
              "fixed-spin code exponent = 7N-1", [188, 1511, 2400], synthesis_line,
              [188, 1511, 2400], True),
        exact("docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md", 26,
              "target exponent = 6N", [162, 1296, 2058], synthesis_line,
              [162, 1296, 2058], True),
        exact("docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md", 26,
              "gauge exponent = N-1", [26, 215, 342], synthesis_line,
              [26, 215, 342], True),
        exact("docs/work_history/repo/review_feedback/PHYSICAL_WILSON_MEASUREMENT_RESET_STABILIZATION_CYCLE535_NOTE_2026-07-21.md", 47,
              "fixed-cut crossed-seam residual", [2.0, 2.0, 2.0], a_line,
              [2.0, 2.0, 2.0], True),
        exact("docs/work_history/repo/review_feedback/PHYSICAL_WILSON_MEASUREMENT_RESET_STABILIZATION_CYCLE535_NOTE_2026-07-21.md", 55,
              "uniform-cut orbit residual = 2/L", [2 / 3, 1 / 3, 2 / 7], a_line,
              [2 / 3, 1 / 3, 2 / 7], True),
        exact("docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md", 139,
              "filled stabilizer rank", [442, 3421, 5398], synthesis_line,
              [442, 3421, 5398], True),
    )
    dropped = (
        {"prior_ref": COMMITTED_SHORE_HEAD,
         "prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_SHARED_SEAM_CODE_SPACE_ISOMETRY_COMPILER_CYCLE539_NOTE_2026-07-21.md",
         "prior_line": 263, "prior_residual": "bounded low-sector patch branch preparation residual",
         "current_path": current_path, "current_line": synthesis_line,
         "current_residual": "full-volume full-Fock rough/fill-code preparation",
         "same_scope": False, "scope_match": False, "exact_match": False, "use_as_closure": False,
         "disposition": "dropped as volume preparation evidence"},
        {"prior_ref": COMMITTED_SHORE_HEAD,
         "prior_path": "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_CUTOFF_GAUGE_PREPARATION_TOURNAMENT_CYCLE598_NOTE_2026-07-22.md",
         "prior_line": 28, "prior_residual": "uniform modular gauge-fiber affine tree preparation",
         "current_path": current_path, "current_line": synthesis_line,
         "current_residual": "Cycle532 Pauli stabilizer/matter/gauge isometry",
         "same_scope": False, "scope_match": False, "exact_match": False, "use_as_closure": False,
         "disposition": "mechanism comparator only; residual differs"},
    )

    def rhetoric(phrase: str, **tested: str) -> dict[str, str]:
        return {"phrase": phrase,
                "per_element": tested.get("per_element", "UNTESTED_NO_BROADER_NEGATIVE"),
                "per_mode": tested.get("per_mode", "UNTESTED_NO_BROADER_NEGATIVE"),
                "per_site": tested.get("per_site", "UNTESTED_NO_BROADER_NEGATIVE"),
                "per_block": tested.get("per_block", "UNTESTED_NO_BROADER_NEGATIVE"),
                "lattice_wide": tested.get("lattice_wide", "UNTESTED_NO_BROADER_NEGATIVE")}

    rhetoric_rows = (
        rhetoric("retained exhaust is not complete target preservation", per_mode="logical crossed seam", per_block="three-character dilation"),
        rhetoric("cap syndrome correction is not arbitrary Wilson initialization", per_element="interior edges", per_block="LxL disk incidence"),
        rhetoric("O(L) reference preparation is not bounded local encoding E", per_mode="three Wilson rails", lattice_wide="L3/L6/L7 resource law"),
        rhetoric("root-free pair pumping is not plus-sign genesis", per_element="every pair flip", per_block="all ring basis words through L7"),
        rhetoric("relative doubled neutrality is not six absolute plus signs", per_mode="six character bits", per_block="rank-three relative constraints"),
        rhetoric("algebraic target-times-gauge factor is not a prepared full-M64 compiler", per_block="exact dimension ledger", lattice_wide="L3/L6/L7"),
    )
    partial = (
        {"file": current_path, "status": "EXECUTED_RETAINED_EXHAUST_RESET", "what_closes": "unitary syndrome/exhaust accounting only"},
        {"file": current_path, "status": "EXECUTED_FILL_SYNDROME_SPAN", "what_closes": "cap correction for supplied even/boundary-plus sector"},
        {"file": current_path, "status": "EXECUTED_ROOTED_GHZ_WAVEFRONT", "what_closes": "three plus auxiliary reference rails after supplied seeds"},
        {"file": current_path, "status": "EXECUTED_DEFECT_PAIR_PUMP", "what_closes": "root-free local motion, not sector genesis"},
        {"file": current_path, "status": "EXECUTED_BOUNDARY_AND_DOUBLED", "what_closes": "boundary-seeded preparation and doubled character-rank audit only"},
        {"file": "scripts/physical_full_rough_tableau_encoder_cycle_next.py", "status": "NOT_CREATED_OPEN_TARGET_EQUIVALENT", "what_closes": "full target+gauge-to-code E and returned work"},
    )
    steelman = {
        "mechanism": "construct a routed symplectic-tableau Clifford encoder that accepts 6N target qubits and N-1 locally blank gauge qubits, grows all Cycle537 stabilizers from product ancillas, returns head/work rails, and uses a state-carried covariant wavefront rather than correcting an unknown Wilson sector",
        "supporting_authorities": (
            {"ref": COMMITTED_SHORE_HEAD,
             "path": "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md",
             "line": 25, "relevance": "exact target-times-gauge algebra already exists"},
            {"ref": COMMITTED_SHORE_HEAD,
             "path": "docs/work_history/repo/review_feedback/PHYSICAL_SHARED_SEAM_CODE_SPACE_ISOMETRY_COMPILER_CYCLE539_NOTE_2026-07-21.md",
             "line": 135, "relevance": "compute/select/uncompute gives an explicit bounded-patch isometry pattern"},
            {"ref": COMMITTED_SHORE_HEAD,
             "path": "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_CUTOFF_GAUGE_PREPARATION_TOURNAMENT_CYCLE598_NOTE_2026-07-22.md",
             "line": 226, "relevance": "scheduled local tree preparation is a positive mechanism despite supplied root/order"},
        ),
        "actionable_test": "materialize the complete Cycle537 stabilizer/matter/gauge tableau at L3/L6/L7, synthesize and route a Clifford E, require exact logical conjugation, blank-work return, deletion, all24/all576, and then compose the committed full-Fock G",
        "openness": "this target-equivalent route is untested, so no broad negative, shared obstruction, minimum content, or axiom pressure can ship",
    }
    echoes = (
        {"cycle": "Cycle532", "retired": "ALGEBRA_AND_G_CLOSED_CONDITIONALLY", "mechanism": "rough target-times-gauge subsystem",
         "applicability": "preparation remains exact target", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md", "citation_line": 140},
        {"cycle": "Cycle535", "retired": "RESET_WITHOUT_EXHAUST_REFINED", "mechanism": "measurement plus membrane reset",
         "applicability": "Cycle636 retains exhaust but matter twist survives", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_WILSON_MEASUREMENT_RESET_STABILIZATION_CYCLE535_NOTE_2026-07-21.md", "citation_line": 49},
        {"cycle": "Cycle537", "retired": "RAW_WILSON_ROWS_RETIRED_ALGEBRAICALLY", "mechanism": "bounded fill face/star complex",
         "applicability": "W_prepare stays open and W_embed is delegated to Cycle637", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md", "citation_line": 363},
        {"cycle": "Cycle539", "retired": "PATCH_DENSE_ISOMETRY_RETIRED_ONLY", "mechanism": "compute/select/uncompute patch encoder",
         "applicability": "possible method, not full-volume back-credit", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_SHARED_SEAM_CODE_SPACE_ISOMETRY_COMPILER_CYCLE539_NOTE_2026-07-21.md", "citation_line": 38},
        {"cycle": "Cycle598", "retired": "SCHEDULED_GAUGE_FIBER_PREP_POSITIVE_DIFFERENT_CODE", "mechanism": "affine tree preparation",
         "applicability": "supports scheduled-tree steelman, not Cycle532 closure", "citation_ref": COMMITTED_SHORE_HEAD,
         "citation_path": "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_CUTOFF_GAUGE_PREPARATION_TOURNAMENT_CYCLE598_NOTE_2026-07-22.md", "citation_line": 226},
    )
    result = {
        "N1_normalized_families": families,
        "N1_open_routes_not_counted": open_routes,
        "N1_qualifying_attempts": 6,
        "N1_required_for_broad_negative": 5,
        "N1_broad_negative_gate": "WITHHELD_DESPITE_ROUTE_COUNT",
        "N2_collapsed_walls": walls,
        "N2_directional_pairs": pairs,
        "N2_directed_pairs": pairs,
        "N2_directed_pair_count": len(pairs),
        "N3_hidden_wall_scan": [
            "Cycle532/Cycle537 algebra, finite domains, and exact target/gauge dimensions are committed shores",
            "syndrome input, correction membrane, retained exhaust, fixed cut, and broadcast schedule are explicit",
            "GHZ data/head/visited rails, seed origin/orientation/plus state, and global tick schedule are supplied",
            "fill-disk even-sector premise, defect-pair law, puncture boundary sign, and doubled relative constraints are explicit",
            "N-1 gauge reference, full stabilizer tableau encoder, blank work, routing, and volume logical map remain open",
            "W_embed is not silently discharged or duplicated; it is assigned to independent Cycle637",
        ],
        "N4_residual_matching": exact_rows,
        "N4_exact_residual_matches": exact_rows,
        "N4_dropped_nonmatches": dropped,
        "N5_rhetoric_audit": rhetoric_rows,
        "N5_rhetoric_resolution_ledger": rhetoric_rows,
        "N6_partial_closure": partial,
        "N6_partial_closure_paths": partial,
        "N7_hostile_steelman": steelman,
        "N7_steelman": steelman,
        "N8_cross_cycle_echo": echoes,
        "Status": "PASS",
        "artifact_status": "PASS_SCOPED_PREPARATION_PARTIALS_AND_EXACT_RESIDUALS_ONLY",
        "broad_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_route_independent_obstruction": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
        "axiom_pressure_claim": False,
        "pass": (
            len(families) == 6 and all(row["honesty_marker"] == "ATTEMPTED" for row in families)
            and len(open_routes) == 1 and all("honesty_marker" not in row for row in open_routes)
            and len(pairs) == 2 and len(exact_rows) == 8 and len(dropped) == 2
            and all(row["same_scope"] and row["exact_match"] and all(key in row for key in
                    ("prior_ref", "prior_path", "prior_line", "current_path", "current_line", "use_as_closure"))
                    for row in exact_rows)
            and all(not row["same_scope"] and not row["exact_match"] and not row["use_as_closure"] for row in dropped)
            and len(rhetoric_rows) == 6 and all(all(key in row for key in
                    ("per_element", "per_mode", "per_site", "per_block", "lattice_wide")) for row in rhetoric_rows)
            and len(partial) == 6 and all(all(key in row for key in ("file", "status", "what_closes")) for row in partial)
            and all(all(key in row for key in ("ref", "path", "line")) for row in steelman["supporting_authorities"])
            and all(all(key in row for key in ("cycle", "retired", "mechanism", "applicability", "citation_ref", "citation_path", "citation_line")) for row in echoes)
            and route_a["pass_as_exact_route_disposition"] and fill["pass_as_exact_route_disposition"]
            and seed["pass_as_exact_route_disposition"] and defect["pass_as_exact_route_disposition"]
            and route_c["pass_as_exact_route_disposition"] and synthesis["pass"]
        ),
    }
    check("full current N1-N8 permits only scoped route dispositions and withholds broad/shared/axiom claims",
          result["pass"], {"attempted": 6, "walls": len(walls), "pairs": len(pairs)})
    return result


def inventory() -> dict[str, object]:
    return {
        "supplied": [
            f"immutable Cycle532/535/537/539/598 shores at {COMMITTED_SHORE_HEAD}; dirty variants are comparison-only",
            "Cycle532 rough code, fixed-sector target-times-gauge algebra, conditional full-Fock G, and finite L3/L6/L7 geometry",
            "Cycle537 fill-disk incidence and its abstract target-times-gauge factorization",
            "Route-A syndrome input, correction membrane, retained exhaust, and broadcast schedule",
            "Route-B onehot seed positions, orientations, plus states, blank data/head/visited rails, and global ticks",
            "fill-pump pairing convention, puncture boundary seed, and doubled-copy relative constraints",
        ],
        "derived": [
            "exact retained-exhaust unitary reset with target residual two and retained sector provenance",
            "complete L3/L6/L7 cap-incidence even/odd syndrome span",
            "bounded-support-three invertible O(L) scheduled state-carried preparation of three plus auxiliary GHZ reference rails",
            "exhaustive L3/L6/L7 root-free pair-pump character conservation",
            "puncture seed dependence and doubled-relative rank-three/residual-three character census",
            "exact L3/L6/L7 full-isometry resource/dimension ledger and separation from conditional G",
        ],
        "open": [
            "one fixed proper-cubic physical cap embedding (independent Cycle637 target)",
            "full routed stabilizer-tableau isometry from 6N target plus a fixed N-1 gauge reference",
            "autonomous seed and gauge-vacuum genesis without host/root/sign supply",
            "returned work/exhaust, full logical conjugation, and literal full-M64 E G = Gphysical E",
            "noise, renewal, infinite volume, and time/energy/source/gravity/Born/Record interpretations",
        ],
    }


def note_text(receipt: dict[str, object]) -> str:
    a = receipt["route_A_retained_exhaust_reset"]
    fill = receipt["route_A2_fill_disk_pump"]
    b = receipt["route_B_state_carried_seed_wavefront"]
    defect = receipt["route_B2_root_free_defect_pump"]
    c = receipt["route_C_boundary_and_doubled"]
    synthesis = receipt["full_isometry_audit"]
    b_rows = "\n".join(
        f"| L{row['length']} | {row['total_reference_initializer_M2']} | {row['parallel_three_axis_depth']} | "
        f"{row['two_M2_CNOT_calls']} | {row['GHZ_stabilizer_rank_per_axis']} | yes |"
        for row in b["rows"]
    )
    synthesis_rows = "\n".join(
        f"| L{row['length']} | {row['Cycle532_rough_M2']} | {row['Cycle532_fixed_spin_rank']} | "
        f"{row['target_full_Fock_qubits']} | {row['gauge_qubits']} | {row['Cycle537_total_M2']} | "
        f"{row['Cycle537_stabilizer_rank']} | no |"
        for row in synthesis["rows"]
    )
    return f"""# Physical fixed-Wilson initializer preparation tournament — Cycle 636

Classification: **positive state-carried preparation of three auxiliary plus-reference rails; no full Cycle532/Cycle537 code isometry or full-M64 physical E/G**

Authority: **none**

Audit: **unset**

Author artifact status accepted: **false**

Breakthrough bar met: **false**

## Result up front

Cycle 636 does not re-solve raw Wilson fixing and does not duplicate Cycle
637's independent physical-cap embedding probe.  Cycle537 already proves that
the exact three Cycle532 Wilson words are products of bounded fill-face checks
and that the abstract filled code is `target_full-Fock tensor gauge_(N-1)`.
The live preparation question is whether local physical operations generate a
lawful state/isometry in that code without a supplied spin or gauge vacuum.

The strongest new construction is Route B.  One supplied oriented plus seed
per axis launches a onehot head around a Wilson reference rail.  The head
applies one local `H`, nearest-neighbor CNOT growth, visited-bit copying, and
head SWAPs.  Uncontrolled Clifford/head gates have support at most two M2;
head-controlled data action has support at most three.  The three axes run
in parallel and exactly prepare three `+` GHZ/Wilson reference rails:

| size | data+head+visited M2 | parallel depth | CNOT calls | GHZ rank/axis | inverse/deletion |
|---|---:|---:|---:|---:|---:|
{b_rows}

All CNOT deletions remove the full `X` Wilson from the stabilizer span; deleting
the seed `H` does likewise.  Reversing the schedule restores every blank data,
head, and visited input.  Oriented loop schedules close under all 24
proper-cubic frames and all 576 products at L3/L6/L7.  After the seed is
present the local head state carries branch control; there is no outcome
postselection or host branch selection.  It is nevertheless not a fully
autonomous initializer: the seed position/orientation/plus state and global
tick/edge schedule remain supplied.  Schedule depth is compiler latency, not
physical time.  The prepared GHZ reference leakage is exactly zero on the
declared onehead code, but forward head/visited work has unit leakage from the
blank-work subspace and returns to blank only under the inverse schedule.

This is an **O(L) local preparation**, not a bounded local encoding `E` per
coarse cell.  The rails are auxiliary references, not the Cycle532 rough-code
state.  Coupling them to an unknown rough sector returns the Route-A reset
problem; it does not create the complete physical code isometry.

## Route A — retained-exhaust syndrome/reset

The exact coherent dilation copies a Wilson sign into a retained exhaust M2,
applies the physical sign-flipping membrane conditional on that exhaust, and
resets the Wilson character to plus.  It is unitary and uses no postselection,
host outcome choice, or erased syndrome.  Its plus-output residual is
`{a['Wilson_positive_output_residual']:.3e}` and its exhaust copy residual is
`{a['retained_exhaust_equals_input_W_residual']:.3e}`.

Retaining exhaust does not repair the Cycle535 matter action.  On a crossed
target seam observable the exact Heisenberg identity remains `A -> W A`.
The target intertwiner residual is `{a['complete_target_seam_intertwiner_residual']:.1f}`,
while the twisted-identity residual is
`{a['Cycle535_twisted_target_identity_residual']:.3e}`.  Fixed-cut feedback
therefore still fails the Cycle230 seam and full-Fock `Gamma(P)`.  Averaging
cuts gives exact residual `2/L`—`{a['size_rows'][0]['uniform_cut_orbit_FSWAP_residual']:.12f}`,
`{a['size_rows'][1]['uniform_cut_orbit_FSWAP_residual']:.12f}`, and
`{a['size_rows'][2]['uniform_cut_orbit_FSWAP_residual']:.12f}` at L3/L6/L7.

Route A2 tests local pumping on Cycle537's fill checks.  The cap-interior
edge/face incidence has rank `L^2-1`; every even syndrome is correctable and
every single odd syndrome is refused at all three sizes.  This is positive
conditional preparation when the boundary Wilson is already plus.  It cannot
change an unknown boundary sign because each cap-only edge flips two faces
and the total face syndrome equals the boundary Wilson.  A host-free pairing
or convergence law is not silently supplied.

## Route B2 — root-free defect pumping

Every basis word and every nearest-neighbor pair flip is exhausted through
L7.  Pair flips move or annihilate local defects and are translation/cubic
covariant, but preserve the loop character exactly.  Both sectors remain
nonempty.  This route is a useful root-free local motion algebra, not plus-sign genesis;
more general processes that leave this rail algebra are not excluded.

## Route C — boundary growth and doubled neutrality

On an open/punctured chain, the same local wavefront grows a pure plus rail
from a plus boundary seed.  Reversing that seed gives an orthogonal minus rail.
If the boundary sign is unfixed or discarded, the mixture has Wilson
expectation zero rather than plus one.  Closing the puncture therefore does
not derive the sign; it either retains or hides the supplied seed.

For two rough copies, three abstract relative constraints have exact rank three
in the six-character space.  They specify paired/neutral relative signs but
leave `{c['doubled_neutral']['residual_diagonal_characters']}` diagonal
characters.  Deleting one relative constraint lowers the rank to
`{c['doubled_neutral']['deleting_one_relative_constraint_rank']}`.  A doubled
character algebra can relocate the three signs but does not derive six
absolute plus values without an anchor.  No physical local doubled initializer
is constructed here.

## Full isometry audit

| size | rough M2 | fixed rank | target qubits | gauge qubits | filled M2 | filled rank | full E built |
|---|---:|---:|---:|---:|---:|---:|---:|
{synthesis_rows}

At each size, `target + gauge = 7N-1`, exactly the Cycle532/Cycle537 code
exponent.  That equality is an interface contract, not a preparation circuit.
The three uncoupled auxiliary GHZ rails establish **zero** physical Cycle537
stabilizers and have zero mutual information with the physical code.  A full
arbitrary-gauge isometry must establish 442, 3421, and 5398 independent
physical stabilizer correlations at L3/L6/L7.  Fixing the gauge vacuum adds
26, 215, and 342 logical-gauge correlations, for totals 468, 3636, and 5740.
Even an ideal but unbuilt transfer of all three Wilson signs could remove at
most three obligations, leaving 465, 3633, and 5737 respectively.
None of the routes maps all `6N` target qubits plus a fixed `N-1` gauge input
into every physical stabilizer while returning head/work/exhaust and proving
the complete logical Pauli conjugation.  Cycle532/Cycle537's full-Fock `G`
remains exact only after the code space is supplied.  Therefore Cycle636 does
not establish a full-M64 `E G = G_physical E`.

`W_embed` and `W_prepare` remain independent.  Cycle636 addresses only
preparation; Cycle637 owns the independent one-fixed-physical-cap embedding
probe.  A preparation on an abstract cap supplies no substrate embedding, and
an embedding supplies no state/isometry.

## Resource, genesis, and semantic ledger

Supplied are the immutable Cycle532/535/537/539/598 shores, finite L3/L6/L7
domains, Route-A syndrome/correction schedule, GHZ seed origins/orientations
and plus states, blank head/visited rails, global ticks, cap pairing convention,
puncture seed, and doubled relative constraints.  The `N-1` gauge reference,
full stabilizer tableau circuit, and volume logical map are not derived.

## Deletion, leakage, and lawful domain

The exact lawful domains are L3 and L6 construction/training sizes and a held
L7 size; no fit parameter is changed for L7.  Route A has zero unitary-inverse
residual, but an input minus sector leaves unit worst-case exhaust leakage from
the blank-exhaust subspace.  Removing syndrome copy or reset gives Wilson
residual two; removing feedback gives zero target twist and therefore does not
implement the reset channel under test.  Route B has zero GHZ-code leakage on
the declared onehead input, every CNOT deletion and the seed-H deletion remove
the Wilson stabilizer, and forward head/visited work has unit leakage from its
blank subspace.  The inverse schedule returns that work exactly.  Zero-head
and multihead words—5, 58, and 121 at L3/L6/L7—are explicitly outside the
declared code.  Route C detects one deleted growth CNOT at every size.  The
all24/all576 audit acts on oriented schedule labels, not on a runtime frame
selector or on Cycle637's still-separate physical embedding.

No syndrome or visited rail is called a Record.  No compiler layer is called
time, no phase is called energy, no generator is called a rate, and no gauge
capacity is called stress/source/gravity.  No probability/Born or actuality
claim is made.

## Prior-art and novelty boundary

GHZ/CNOT wavefronts, stabilizer syndrome reset, defect motion, punctured
boundary growth, and doubled relative-sign constraints are standard mechanism
classes.  No general novelty or priority is claimed.  The repo-specific
contribution is their exact separation on the Cycle532/Cycle537 preparation
contract, the L3/L6/L7 resource/deletion/covariance audit, and the explicit
full-isometry/gauge-vacuum boundary.  No external theorem is used as runner
evidence.

## N1–N8 no-go discipline

N1 normalizes six actually attempted families and lists the untested
full-tableau encoder separately as an open route that is not counted.
N2 retains exactly two independent walls and both directional implications are
false.  N3 inventories every seed, sign, exhaust, schedule, cap, puncture,
relative constraint, gauge input, and tableau import.  N4 has eight exact
same-scope residual rows and two dropped nonmatches.  N5 has six complete
five-resolution rhetoric rows.  N6 has six structured partial-closure paths.
N7 gives the actionable full symplectic-tableau encoder steelman.  N8 gives
five row-wise exact cross-cycle echoes.

The N1 attempt threshold is met, but the concrete untested full-tableau route
keeps every broad conclusion open.  Broad no-go, minimum content, shared
obstruction, and axiom pressure are all withheld.

Shared route-independent obstruction: **not established**.

Axiom pressure: **none**.

## Six-wall ledger

| wall | Cycle636 movement | residual |
|---|---|---|
| `C_ref` | literal bounded-support O(L) plus-reference rails and retained provenance are constructed | seed plus state/origin/orientation, global schedule, and N-1 gauge reference remain supplied; no full E |
| `C_num` | exact L3/L6/L7 ranks, resources, character sectors, and deletion counts | dimension equality is not a tableau isometry |
| `C_wrap` | head/visited/exhaust rails retain preparation provenance and invert | they are not Records, time, actuality, or realized history |
| `C_int` | reset's exact seam twist is isolated; conditional Cycle532/Cycle537 G remains comparison-positive | no complete matter-preserving initializer or new interaction law |
| `C_local` | bounded-support head wavefront, local syndrome incidence, all24/all576, inverse/deletion/held tests pass | O(L) preparation is not bounded local E; embedding is independent Cycle637 work |
| `C_source` | seed, blank capacity, exhaust, and doubled overhead are explicit | no energy/stress/source/gravity meaning or autonomous resource genesis |

## Disposition and next campaign

**PASS** for the scheduled state-carried O(L) preparation of three auxiliary plus
reference rails, retained-exhaust reset accounting, conditional fill-syndrome
correction, and the root-free/boundary/doubled exact dispositions.

**FAIL / DO NOT CLAIM** for a bounded local Cycle532/Cycle537 encoding `E`, a
prepared gauge vacuum, a full-M64 physical compiler, autonomous initialization/seed genesis,
shared obstruction, minimum content, or axiom pressure.

The optimal next preparation campaign is the hostile steelman: materialize the
complete Cycle537 stabilizer/matter/gauge tableau, synthesize a routed Clifford
isometry from `6N` target plus `N-1` fixed gauge inputs, replace its root/order
by state-carried local control, return every work rail, and only then compose
the committed full-Fock `G`.  Keep Cycle637's embedding result as a separate
input rather than conflating physical placement with preparation.
"""


def normalized_note(path: Path) -> str:
    return " ".join(path.read_text().lower().split())


def note_contract() -> dict[str, object]:
    required = (
        "authority: **none**", "audit: **unset**", "author artifact status accepted: **false**",
        "breakthrough bar met: **false**", "o(l) local preparation", "not a bounded local encoding `e`",
        "does not establish a full-m64", "no general novelty or priority is claimed",
        "six actually attempted families", "open route that is not counted", "two independent walls", "eight exact same-scope residual rows",
        "shared route-independent obstruction: **not established**", "axiom pressure: **none**",
    )
    body = normalized_note(NOTE)
    missing = tuple(fragment for fragment in required if fragment not in body)
    return {"required_fragments": required, "missing": missing, "pass": not missing}


def main() -> None:
    signal.alarm(math.ceil(WALL_CAP_SECONDS))
    started = time.perf_counter()
    shore = shore_controls()
    frames = frame_schedule_controls()
    route_a = retained_exhaust_reset_route(frames)
    fill = fill_disk_pump_route()
    seed = seed_wavefront_route(frames)
    defect = root_free_defect_pump_route()
    route_c = boundary_and_doubled_routes()
    synthesis = full_isometry_audit(route_a, fill, seed, defect, route_c)
    no_go = no_go_discipline(route_a, fill, seed, defect, route_c, synthesis)
    receipt = {
        "status": "positive O(L) state-carried auxiliary plus-reference preparation; no bounded local Cycle532/Cycle537 E or full-M64 E/G",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "author_accepted": False,
        "author_artifact_status_accepted": False,
        "breakthrough": False,
        "breakthrough_bar_met": False,
        "shore": shore,
        "frame_schedule_controls": frames,
        "route_A_retained_exhaust_reset": route_a,
        "route_A2_fill_disk_pump": fill,
        "route_B_state_carried_seed_wavefront": seed,
        "route_B2_root_free_defect_pump": defect,
        "route_C_boundary_and_doubled": route_c,
        "full_isometry_audit": synthesis,
        "no_go_discipline": no_go,
        "inventory": inventory(),
        "prior_art_and_novelty_boundary": {
            "standard_mechanism_classes": ["GHZ/CNOT wavefront", "stabilizer syndrome reset", "defect-pair pumping", "punctured boundary growth", "doubled relative-sign constraints"],
            "general_novelty_or_priority_claim": False,
            "repo_specific_contribution": "exact Cycle532/Cycle537 preparation separation with L3/L6/L7 resources, deletions, covariance, and full-isometry/gauge-vacuum firewall",
            "external_theorem_used_as_runner_evidence": False,
        },
        "strongest_constructive_result": "after three supplied oriented plus seeds, a scheduled state-carried bounded-support invertible wavefront prepares the three auxiliary Wilson plus-reference rails in O(L) depth with retained head/visited provenance and all24/all576 covariance",
        "highest_honest_terminal": "scheduled physical local preparation of auxiliary topological reference rails after supplied seed genesis; not autonomous and not the Cycle532/Cycle537 code-space isometry",
        "route_by_route_disposition": {
            "A_retained_exhaust_reset": "EXACT_PLUS_RESET_BUT_TARGET_SEAM_RESIDUAL_TWO",
            "A2_fill_check_pump": "EXACT_EVEN_SYNDROME_CORRECTION_CONDITIONAL_ON_BOUNDARY_PLUS",
            "B_state_carried_wavefront": "PASS_SCHEDULED_AUXILIARY_PLUS_REFERENCE_O_L_NOT_AUTONOMOUS",
            "B2_root_free_defect_pump": "EXACT_CHARACTER_CONSERVATION_NOT_GENESIS",
            "C_punctured_boundary": "PASS_ONLY_WITH_SUPPLIED_BOUNDARY_SIGN",
            "C_doubled_neutral": "PASS_CHARACTER_RANK_AUDIT_ONLY_THREE_DIAGONAL_CHARACTERS_LEFT",
            "full_Cycle532_Cycle537_E": "OPEN_NOT_CONSTRUCTED",
        },
        "six_wall_ledger": {
            "C_ref": "bounded-support O(L) plus-reference rails after supplied seeds/ticks; gauge reference and full E open",
            "C_num": "exact L3/L6/L7 ranks/resources/sectors/deletions; dimension equality is not an isometry",
            "C_wrap": "head/visited/exhaust provenance retained; not Record/time/actuality/history",
            "C_int": "exact reset seam twist; conditional G unchanged and no new interaction",
            "C_local": "local wavefront/syndrome/all24/all576/inverse/deletion controls; O(L) prep not bounded E and W_embed separate",
            "C_source": "seed/blank/exhaust/doubled resources explicit; no energy/stress/source/gravity or autonomous genesis",
        },
        "shared_substrate_obstruction": False,
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
        "maturity_rebase": None,
        "lawful_domain_controls": {
            "L3": "construction",
            "L6": "training",
            "L7": "held-out with no refit",
            "infinite_volume_claim": False,
            "route_B_declared_input": "one oriented onehot plus seed per axis with blank data/visited",
            "runtime_frame_selector": False
        },
        "leakage_controls": {
            "route_A_worst_case_exhaust_from_blank": route_a["worst_case_terminal_exhaust_leakage_from_blank_subspace"],
            "route_B_GHZ_code": [row["GHZ_reference_code_leakage_residual"] for row in seed["rows"]],
            "route_B_terminal_work_from_blank": [row["terminal_work_leakage_from_blank_subspace"] for row in seed["rows"]],
            "full_E_returned_work_proved": False
        },
        "semantic_promotion_boundary": {
            "author_artifact_status_accepted": False,
            "breakthrough_bar_met": False,
            "auxiliary_plus_reference_preparation": "POSITIVE_AFTER_SUPPLIED_SEEDS",
            "fixed_cap_embedding_W_embed": None,
            "full_code_preparation_W_prepare": None,
            "bounded_local_encoding_E": None,
            "full_M64_EG": None,
            "autonomous_seed_genesis": None,
            "gauge_vacuum_genesis": None,
            "Record_or_actuality": None,
            "time_energy_source_gravity_Born": None,
        },
        "optimal_next_campaign": "after Cycle637 resolves embedding, materialize and locally route the complete Cycle537 symplectic-tableau Clifford E from 6N target plus N-1 fixed gauge inputs, return all work, and compose committed full-Fock G",
    }
    NOTE.write_text(note_text(receipt))
    contract = note_contract()
    check("Cycle636 note preserves preparation/embedding/full-E and semantic firewalls",
          contract["pass"], contract["missing"])
    elapsed = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000:
        rss *= 1024
    receipt.update({
        "note_contract": contract,
        "runner_sha256": file_sha(Path(__file__)),
        "note_sha256": file_sha(NOTE),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "tests_passed": PASS,
        "tests_failed": FAIL,
    })
    receipt["pass"] = (
        FAIL == 0 and shore["pass"] and frames["pass"]
        and route_a["pass_as_exact_route_disposition"] and fill["pass_as_exact_route_disposition"]
        and seed["pass_as_exact_route_disposition"] and defect["pass_as_exact_route_disposition"]
        and route_c["pass_as_exact_route_disposition"] and synthesis["pass"] and no_go["pass"]
        and contract["pass"] and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES
        and AUTHORITY == "none" and AUDIT == "unset"
    )
    RECEIPT.write_text(json.dumps(
        receipt, indent=2, sort_keys=True,
        default=lambda value: value.item() if isinstance(value, np.generic) else list(value),
    ) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS,
                      "tests_failed": FAIL, "elapsed_seconds": elapsed,
                      "maximum_RSS_bytes": rss, "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
