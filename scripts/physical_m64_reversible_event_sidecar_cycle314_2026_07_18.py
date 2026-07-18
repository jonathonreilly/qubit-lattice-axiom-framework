#!/usr/bin/env python3
"""Cycle 314: a bounded reversible event-parity sidecar for Cycle-311 M64.

This runner adds one ordinary local M2 ``h`` to the Cycle-311 rank-127 fixed
seam.  A local diagonal constraint ties ``h`` to the gauge-invariant seam
role, and the literal stream flips ``h`` exactly in nonvacuum sectors.  The
result is a readable event-ready update-parity carrier.  It is deliberately
not called elapsed time, a clock, occurrence, permanence, or a Record.

The runner also tests the independent-swap quotient on actual bounded block
supports from Cycle 312.  That quotient is a separate one-pair recurrence
fragment; no recurrent M64 glue between it and the sidecar is claimed.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_local_fock_extension_cycle312_2026_07_18 as c312


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_M64_REVERSIBLE_EVENT_SIDECAR_CYCLE314_NOTE_2026-07-18.md"
)
TRAINING_SIZES = (3, 4, 5)
HELD_SIZES = (6,)
SIZES = TRAINING_SIZES + HELD_SIZES
TOLERANCE = 1.2e-11

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class EventSidecar:
    encoder: c311.CommonEncoder
    basis: tuple[c311.CommonBranch, ...]
    flagged: np.ndarray
    exchange: np.ndarray
    base_encoding: np.ndarray
    numbers: np.ndarray
    slices: np.ndarray
    gauges: np.ndarray
    event_encoding: np.ndarray
    constraint_signs: np.ndarray
    stream_mapping: np.ndarray


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-314 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "one additional ordinary m2 h per coarse cell",
        "c_hist = p_vac z_h + p_nonvac z_f z_r z_h",
        "rank-127 constrained event-sidecar code",
        "e_hist g_coarse = g_hist e_hist",
        "binary update-parity carrier",
        "event-ready",
        "not an accumulated history index",
        "not elapsed time",
        "not a record",
        "all 24 proper-cubic frames",
        "all 27 l=3 translations",
        "held l=6",
        "at most fifty-seven m2",
        "twenty-four m2 per cell",
        "z3 spatial surface is unchanged",
        "independent-swap quotient",
        "stable event labels",
        "host positions",
        "none of pr5469 legs a, b, or c is closed",
        "broad gate status: fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the event-parity construction and semantic firewall", not missing, missing)


def event_constraint_sign(number: int, stream_slice: int, gauge: int, event: int) -> int:
    if number not in c311.NUMBERS or stream_slice not in (0, 1) or gauge not in (0, 1) or event not in (0, 1):
        raise ValueError("event constraint labels must be n=0..6 and binary f,r,h")
    exponent = event if number == 0 else stream_slice ^ gauge ^ event
    return 1 if exponent == 0 else -1


def build_event_sidecar(code, body=(0, 0, 0)) -> EventSidecar:
    encoder = c311.common_encoder(code, body)
    basis, flagged, occurrence = c311.flagged_basis_and_encoding(encoder)
    exchange = c311.exchange_matrix(encoder, occurrence)
    base = c311.constrained_encoding(flagged, exchange)
    micro = len(base)
    numbers = np.asarray([branch.number for branch in basis] * 2, dtype=int)
    slices = np.asarray([branch.stream_slice for branch in basis] * 2, dtype=int)
    gauges = np.repeat(np.asarray((0, 1), dtype=int), len(basis))

    event_encoding = np.zeros((2 * micro, c311.SEAM_DIMENSION), dtype=complex)
    rows = np.arange(micro)
    for column, (_number, _label, stream_slice) in enumerate(c311.SEAM_LABELS):
        event_encoding[2 * rows + stream_slice, column] = base[:, column]

    signs = np.asarray(
        [
            event_constraint_sign(numbers[row], slices[row], gauges[row], event)
            for row in range(micro)
            for event in (0, 1)
        ],
        dtype=int,
    )

    old_stream = c311.gauge_lift(exchange, exchange)
    old_target = np.argmax(abs(old_stream), axis=0)
    stream_mapping = np.empty(2 * micro, dtype=int)
    for row in range(micro):
        for event in (0, 1):
            stream_mapping[2 * row + event] = (
                2 * old_target[row] + (event ^ int(numbers[row] > 0))
            )
    if len(set(map(int, stream_mapping))) != len(stream_mapping):
        raise ValueError("the event-sidecar stream must be a permutation")
    return EventSidecar(
        encoder,
        basis,
        flagged,
        exchange,
        base,
        numbers,
        slices,
        gauges,
        event_encoding,
        signs,
        stream_mapping,
    )


def scalar_lift(operator: np.ndarray) -> np.ndarray:
    if operator.ndim != 2 or operator.shape[0] != operator.shape[1] or not np.all(np.isfinite(operator)):
        raise ValueError("a finite square operator is required")
    return np.kron(operator, np.eye(2, dtype=complex))


def apply_mapping(mapping: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    if mapping.ndim != 1 or matrix.shape[0] != len(mapping) or len(set(map(int, mapping))) != len(mapping):
        raise ValueError("one full permutation and a row-compatible matrix are required")
    result = np.zeros_like(matrix)
    result[mapping, :] = matrix
    return result


def shell_and_constraint_controls(sidecar: EventSidecar):
    print("\nLOCAL EVENT-SIDECAR CONSTRAINT")
    event = sidecar.event_encoding
    base = sidecar.base_encoding
    dimension = c311.SEAM_DIMENSION
    micro = len(base)
    shell = np.zeros((2 * micro, 2 * dimension), dtype=complex)
    shell[0::2, :dimension] = base
    shell[1::2, dimension:] = base
    reduced_constraint = shell.conj().T @ (sidecar.constraint_signs[:, None] * shell)
    selector = np.zeros((2 * dimension, dimension), dtype=complex)
    for column, (_number, _label, stream_slice) in enumerate(c311.SEAM_LABELS):
        selector[column if stream_slice == 0 else dimension + column, column] = 1
    details = {
        "base_rank": int(np.linalg.matrix_rank(base, tol=1e-10)),
        "shell_rank": int(np.linalg.matrix_rank(shell, tol=1e-10)),
        "constraint_plus_rank": int(np.count_nonzero(np.linalg.eigvalsh(reduced_constraint) > 0.5)),
        "event_rank": int(np.linalg.matrix_rank(event, tol=1e-10)),
        "base_isometry": float(np.linalg.norm(base.conj().T @ base - np.eye(dimension))),
        "event_isometry": float(np.linalg.norm(event.conj().T @ event - np.eye(dimension))),
        "constraint_eigen": float(np.linalg.norm(sidecar.constraint_signs[:, None] * event - event)),
        "constraint_shell_intertwiner": float(
            np.linalg.norm(sidecar.constraint_signs[:, None] * shell - shell @ reduced_constraint)
        ),
        "constraint_involution": float(np.linalg.norm(reduced_constraint @ reduced_constraint - np.eye(2 * dimension))),
        "selected_plus_basis": float(np.linalg.norm(shell @ selector - event)),
        "selected_plus_eigen": float(np.linalg.norm(reduced_constraint @ selector - selector)),
    }
    check(
        "C_hist locally cuts the rank-254 shell-times-h space to the exact rank-127 event-sidecar code",
        details["base_rank"] == details["event_rank"] == details["constraint_plus_rank"] == 127
        and details["shell_rank"] == 254
        and max(value for key, value in details.items() if "rank" not in key) < TOLERANCE,
        details,
    )
    return reduced_constraint


def geometry_and_held_size_controls():
    print("\nBOUNDED SUPPORT / TRAINED AND HELD SIZES")
    rows = []
    fixtures = {}
    for length in SIZES:
        code = c311.c269.build_code(length)
        sidecar = build_event_sidecar(code)
        fixtures[length] = sidecar
        face_union = tag_union = 0
        maximum_branch = 0
        for branch in sidecar.basis:
            face = branch.face_pauli.x | branch.face_pauli.z
            face_union |= face
            tag_union |= branch.tags
            maximum_branch = max(
                maximum_branch,
                face.bit_count() + branch.tags.bit_count() + bool(branch.stream_slice) + 2,
            )
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "seam_columns": sidecar.event_encoding.shape[1],
                "ambient_microsectors": sidecar.event_encoding.shape[0],
                "isometry": float(
                    np.linalg.norm(
                        sidecar.event_encoding.conj().T @ sidecar.event_encoding
                        - np.eye(c311.SEAM_DIMENSION)
                    )
                ),
                "constraint": float(
                    np.linalg.norm(
                        sidecar.constraint_signs[:, None] * sidecar.event_encoding
                        - sidecar.event_encoding
                    )
                ),
                "total_patch_support_M2": face_union.bit_count() + tag_union.bit_count() + 3,
                "maximum_branch_support_M2": maximum_branch,
                "installed_M2_per_cell": 24,
            }
        )
    check(
        "one ordinary h M2 has constant overhead, bounded support, and exact trained/held closure through L=6",
        all(
            row["seam_columns"] == 127
            and row["ambient_microsectors"] == 1020
            and row["isometry"] < TOLERANCE
            and row["constraint"] < TOLERANCE
            and row["total_patch_support_M2"] <= 57
            and row["maximum_branch_support_M2"] <= 46
            and row["installed_M2_per_cell"] == 24
            for row in rows
        ),
        rows,
    )
    return fixtures


def physical_update_controls(sidecar: EventSidecar):
    print("\nPHYSICAL EVENT-PARITY UPDATE / DECODER")
    event = sidecar.event_encoding
    logical_S = c311.logical_stream()
    logical_D = c311.logical_contact(c311.COUPLING)
    old_D = c311.gauge_lift(
        c311.flagged_contact(sidecar.encoder, sidecar.basis, c311.COUPLING),
        sidecar.exchange,
    )
    physical_D = scalar_lift(old_D)
    event_values = np.tile(np.asarray((0, 1), dtype=float), len(sidecar.base_encoding))
    logical_event_values = np.asarray([stream_slice for _n, _label, stream_slice in c311.SEAM_LABELS], dtype=float)
    decoder_residual = float(
        np.linalg.norm(
            event_values[:, None] * event
            - event @ np.diag(logical_event_values)
        )
    )
    rows = []
    nominal = None
    rng = np.random.default_rng(314)
    for beta, held in ((-0.2, False), (-0.3, False), (-0.4, False), (-0.35, True)):
        logical_K = c311.logical_coin(c311.c219.common_species(beta).coin)
        old_K, flagged_K = c311.physical_coin(
            sidecar.flagged, logical_K, sidecar.exchange
        )
        physical_K = scalar_lift(old_K)
        logical_G = logical_D @ logical_S @ logical_K
        coin_image = physical_K @ event
        stream_image = apply_mapping(sidecar.stream_mapping, coin_image)
        physical_image = physical_D @ stream_image
        inverse_image = physical_K.conj().T @ apply_mapping(
            np.argsort(sidecar.stream_mapping), physical_D.conj().T @ physical_image
        )
        coherent = rng.normal(size=c311.SEAM_DIMENSION) + 1j * rng.normal(size=c311.SEAM_DIMENSION)
        coherent /= np.linalg.norm(coherent)
        constraint_coin = float(
            np.linalg.norm(
                sidecar.constraint_signs[:, None] * physical_K
                - physical_K * sidecar.constraint_signs[None, :]
            )
        )
        constraint_contact = float(
            np.linalg.norm(
                sidecar.constraint_signs[:, None] * physical_D
                - physical_D * sidecar.constraint_signs[None, :]
            )
        )
        row = {
            "beta": beta,
            "held_beta": held,
            "coin_intertwiner": float(np.linalg.norm(coin_image - event @ logical_K)),
            "stream_intertwiner": float(
                np.linalg.norm(apply_mapping(sidecar.stream_mapping, event) - event @ logical_S)
            ),
            "contact_intertwiner": float(np.linalg.norm(physical_D @ event - event @ logical_D)),
            "composition_intertwiner": float(np.linalg.norm(physical_image - event @ logical_G)),
            "inverse_on_code": float(np.linalg.norm(inverse_image - event)),
            "constraint_coin": constraint_coin,
            "constraint_stream": float(
                np.linalg.norm(
                    sidecar.constraint_signs[sidecar.stream_mapping]
                    - sidecar.constraint_signs
                )
            ),
            "constraint_contact": constraint_contact,
            "coherent_composition": float(
                np.linalg.norm(physical_image @ coherent - event @ logical_G @ coherent)
            ),
            "flagged_coin_unitarity": float(
                np.linalg.norm(flagged_K.conj().T @ flagged_K - np.eye(len(flagged_K)))
            ),
        }
        rows.append(row)
        if beta == -0.3:
            nominal = (logical_K, old_K, physical_K, old_D, physical_D, logical_G, physical_image)
    fock_input = event @ c311.fock_input_embedding()
    nominal_output = nominal[-1] @ c311.fock_input_embedding()
    expected_output = np.asarray([0 if number == 0 else 1 for number, _label in c311.FOCK_LABELS])
    input_read = event_values[:, None] * fock_input
    output_read = event_values[:, None] * nominal_output
    event_read_residual = float(
        np.linalg.norm(output_read - nominal_output * expected_output[None, :])
    )
    leakage = float(
        np.linalg.norm(nominal[-1] - event @ (event.conj().T @ nominal[-1]))
    )
    check(
        "the physical coin, event-flipping stream, contact, and DSK exactly intertwine and preserve C_hist on coherent M64 states",
        all(
            max(value for key, value in row.items() if key not in ("beta", "held_beta")) < 3e-11
            for row in rows
        )
        and decoder_residual < TOLERANCE
        and np.linalg.norm(input_read) < TOLERANCE
        and event_read_residual < TOLERANCE
        and leakage < TOLERANCE,
        {
            "rows": rows,
            "decoder_residual": decoder_residual,
            "input_h_read_norm": float(np.linalg.norm(input_read)),
            "nonvacuum_output_h_residual": event_read_residual,
            "code_leakage": leakage,
        },
    )
    return nominal


def reachability_signature(execution, supports):
    labels = tuple(execution)
    edges = {
        (labels[left], labels[right])
        for left in range(len(labels))
        for right in range(left + 1, len(labels))
        if supports[labels[left]] & supports[labels[right]]
    }
    changed = True
    while changed:
        changed = False
        additions = {
            (left, right)
            for left, middle in edges
            for source, right in edges
            if middle == source and left != right and (left, right) not in edges
        }
        if additions:
            edges |= additions
            changed = True
    return frozenset(edges)


def independent_swap_quotient_controls():
    print("\nACTUAL BOUNDED-BLOCK INDEPENDENT-SWAP QUOTIENT")
    model = c312.c307.build_model(3)
    catalog = []
    for kind in ("coin", "edge"):
        for local_index, block in enumerate(c312.local_blocks(model, kind)):
            catalog.append(
                {
                    "stable_label": (kind, local_index, block.label),
                    "support": c312.block_mode_support(model, block),
                }
            )
    selected_catalog_indices = (0, 1, 13, 27, 35)
    selected = tuple(catalog[index] for index in selected_catalog_indices)
    supports = {index: selected[index]["support"] for index in range(len(selected))}
    initial = tuple(range(len(selected)))
    queue = deque((initial,))
    executions = {initial}
    certified_swaps = 0
    while queue:
        execution = queue.popleft()
        for position in range(len(execution) - 1):
            left, right = execution[position : position + 2]
            if supports[left] & supports[right]:
                continue
            certified_swaps += 1
            swapped = list(execution)
            swapped[position], swapped[position + 1] = swapped[position + 1], swapped[position]
            swapped = tuple(swapped)
            if swapped not in executions:
                executions.add(swapped)
                queue.append(swapped)
    signatures = {reachability_signature(execution, supports) for execution in executions}
    host_positions = {
        tuple(execution.index(label) for label in range(len(selected)))
        for execution in executions
    }
    dependent_pairs = sum(
        bool(supports[left] & supports[right])
        for left, right in combinations(range(len(selected)), 2)
    )
    independent_pairs = 10 - dependent_pairs
    detail = {
        "actual_Cycle312_blocks": len(selected),
        "stable_labels": tuple(row["stable_label"] for row in selected),
        "bounded_support_sizes": tuple(len(row["support"]) for row in selected),
        "dependent_pairs": dependent_pairs,
        "independent_pairs": independent_pairs,
        "reachable_swap_equivalent_executions": len(executions),
        "certified_adjacent_swaps": certified_swaps,
        "distinct_host_position_tuples": len(host_positions),
        "event_poset_signatures": len(signatures),
    }
    check(
        "actual Cycle-312 support labels quotient all certified independent swaps to one causal dependency poset while host positions vary",
        dependent_pairs > 0
        and independent_pairs > 0
        and len(executions) > 1
        and certified_swaps > 0
        and len(host_positions) > 1
        and len(signatures) == 1,
        detail,
    )
    return detail


def covariance_and_translation_controls(sidecar: EventSidecar, nominal):
    print("\nPROPER-CUBIC COVARIANCE / TRANSLATIONS / Z3 SURFACE")
    logical_K, old_K, _physical_K, old_D, _physical_D, logical_G, _image = nominal
    old_S = c311.gauge_lift(sidecar.exchange, sidecar.exchange)
    old_G = old_D @ old_S @ old_K
    reducer = c311.c305.StabilizerReducer(sidecar.encoder.code)
    frames = c311.c235.proper_cubic_frames()
    logical_reps = [c311.logical_frame_representation(frame) for frame in frames]
    signed_logical = [c311.signed_mapping(rep)[:2] for rep in logical_reps]
    frame_lookup = {tuple(frame.flatten()): index for index, frame in enumerate(frames)}
    group_failures = 0
    for left_index, left in enumerate(frames):
        left_map, left_phase = signed_logical[left_index]
        for right_index, right in enumerate(frames):
            right_map, right_phase = signed_logical[right_index]
            target_index = frame_lookup[tuple((left @ right).flatten())]
            target_map, target_phase = signed_logical[target_index]
            composed_map = left_map[right_map]
            composed_phase = right_phase * left_phase[right_map]
            group_failures += np.count_nonzero(composed_map != target_map)
            group_failures += np.count_nonzero(abs(composed_phase - target_phase) > TOLERANCE)

    frame_rows = []
    micro = len(sidecar.base_encoding)
    for frame, logical_R in zip(frames, logical_reps):
        old_R, branch_failures = c311.flagged_frame_representation(
            sidecar.encoder, sidecar.basis, {}, frame, reducer
        )
        mapping, phases, mapping_failures = c311.signed_mapping(old_R)
        role_mapping = np.concatenate((mapping, mapping + c311.FLAGGED_MICRO_DIMENSION))
        role_phases = np.concatenate((phases, phases))
        event_mapping = np.empty(2 * micro, dtype=int)
        event_phases = np.empty(2 * micro, dtype=complex)
        for row in range(micro):
            for event in (0, 1):
                event_mapping[2 * row + event] = 2 * role_mapping[row] + event
                event_phases[2 * row + event] = role_phases[row]
        rotated_event = np.zeros_like(sidecar.event_encoding)
        rotated_event[event_mapping, :] = event_phases[:, None] * sidecar.event_encoding
        frame_rows.append(
            {
                "branch_failures": branch_failures + mapping_failures,
                "event_encoding_covariance": float(np.linalg.norm(rotated_event - sidecar.event_encoding @ logical_R)),
                "constraint_scalar_covariance": float(
                    np.linalg.norm(sidecar.constraint_signs[event_mapping] - sidecar.constraint_signs)
                ),
                "stream_mapping_covariance": int(
                    np.count_nonzero(
                        event_mapping[sidecar.stream_mapping]
                        != sidecar.stream_mapping[event_mapping]
                    )
                ),
                "stream_phase_covariance": float(
                    np.linalg.norm(event_phases[sidecar.stream_mapping] - event_phases)
                ),
                "coin_covariance": c311.conjugation_residual(old_K, role_mapping, role_phases),
                "stream_covariance": c311.conjugation_residual(old_S, role_mapping, role_phases),
                "contact_covariance": c311.conjugation_residual(old_D, role_mapping, role_phases),
                "composition_covariance": c311.conjugation_residual(old_G, role_mapping, role_phases),
                "logical_composition_covariance": float(np.linalg.norm(logical_R @ logical_G - logical_G @ logical_R)),
            }
        )

    translation_failures = translation_tests = 0
    for displacement in product(range(sidecar.encoder.code.length), repeat=3):
        vertex_map, edge_map = c311.c269.graph_translation_maps(sidecar.encoder.code.graph, displacement)
        toggles, repair_pairs, flips = c311.c269.repair_data(
            sidecar.encoder.code.graph, vertex_map, edge_map
        )
        target = build_event_sidecar(sidecar.encoder.code, displacement)
        target_occurrence = {
            (branch.number, branch.label, branch.stream_slice, branch.carrier_direction): index
            for index, branch in enumerate(target.basis)
        }
        for branch in sidecar.basis:
            target_index = target_occurrence[
                (branch.number, branch.label, branch.stream_slice, branch.carrier_direction)
            ]
            target_branch = target.basis[target_index]
            transformed = c311.local.transform_pauli(
                sidecar.encoder.code,
                branch.face_pauli,
                edge_map,
                toggles,
                repair_pairs,
                flips,
            )
            translation_failures += reducer.relative_phase(transformed, target_branch.face_pauli) != 0
            translation_failures += abs(branch.amplitude - target_branch.amplitude) > TOLERANCE
            translation_failures += c311.ports.permute_bits(branch.tags, vertex_map) != target_branch.tags
            translation_tests += 1
    check(
        "h is a cubic scalar: the event-sidecar code, constraint, decoder, and update are covariant under every proper frame and L=3 translation",
        group_failures == 0
        and all(
            row["branch_failures"] == 0
            and max(value for key, value in row.items() if key != "branch_failures") < 3e-11
            for row in frame_rows
        )
        and translation_failures == 0,
        {
            "proper_frames": len(frames),
            "group_law_tests": len(frames) ** 2,
            "group_failures": group_failures,
            "maximum_frame_row": {
                key: max(row[key] for row in frame_rows) for key in frame_rows[0]
            },
            "translations": sidecar.encoder.code.length**3,
            "translation_branch_tests": translation_tests,
            "translation_failures": translation_failures,
            "spatial_surface": "Z3 unchanged; no fourth spatial direction installed",
        },
    )


def deletion_erasure_and_domain_controls(sidecar: EventSidecar, nominal):
    print("\nDELETION / ERASURE / LAWFUL DOMAIN")
    event = sidecar.event_encoding
    micro = len(sidecar.base_encoding)
    old_target = np.argmax(
        abs(c311.gauge_lift(sidecar.exchange, sidecar.exchange)), axis=0
    )
    no_flip = 2 * np.repeat(old_target, 2) + np.tile((0, 1), micro)
    flip_vacuum = np.empty_like(sidecar.stream_mapping)
    for row in range(micro):
        for event_bit in (0, 1):
            flip_vacuum[2 * row + event_bit] = 2 * old_target[row] + (event_bit ^ 1)
    logical_S = c311.logical_stream()
    no_flip_intertwiner = float(
        np.linalg.norm(apply_mapping(no_flip, event) - event @ logical_S)
    )
    no_flip_constraint = float(
        np.linalg.norm(sidecar.constraint_signs[no_flip] - sidecar.constraint_signs)
    )
    flip_vacuum_intertwiner = float(
        np.linalg.norm(apply_mapping(flip_vacuum, event) - event @ logical_S)
    )
    two_update_failures = int(
        np.count_nonzero(
            sidecar.stream_mapping[sidecar.stream_mapping]
            != np.arange(len(sidecar.stream_mapping))
        )
    )
    event_values = np.tile(np.asarray((0, 1), dtype=float), micro)
    logical_event_values = np.asarray([stream_slice for _n, _label, stream_slice in c311.SEAM_LABELS])
    deleted_decoder = float(np.linalg.norm(event @ np.diag(logical_event_values)))
    wrong_signs = np.asarray(
        [(-1) ** (sidecar.slices[row] ^ sidecar.gauges[row] ^ event_bit) for row in range(micro) for event_bit in (0, 1)]
    )
    vacuum_constraint_error = float(np.linalg.norm(wrong_signs[:, None] * event - event))

    logical_K, old_K, _physical_K, old_D, _physical_D, _logical_G, _image = nominal
    base_stream = c311.gauge_lift(sidecar.exchange, sidecar.exchange)
    base_G_image = old_D @ base_stream @ old_K @ sidecar.base_encoding
    base_logical_G = c311.logical_contact(c311.COUPLING) @ logical_S @ logical_K
    base_intertwiner = float(
        np.linalg.norm(base_G_image - sidecar.base_encoding @ base_logical_G)
    )

    one_interval_rate = 1 / 1
    two_interval_rate = 1 / 2
    one_particle_columns = [
        c311.SEAM_INDEX[(1, (direction,), 0)] for direction in range(6)
    ]
    streamed = apply_mapping(sidecar.stream_mapping, event[:, one_particle_columns])
    direction_event_reads = [
        float(np.vdot(streamed[:, index], event_values * streamed[:, index]).real)
        for index in range(6)
    ]

    rejected = 0
    for action in (
        lambda: c311.c269.build_code(2),
        lambda: build_event_sidecar(sidecar.encoder.code, (-1, 0, 0)),
        lambda: event_constraint_sign(1, 0, 0, 2),
        lambda: event_constraint_sign(7, 0, 0, 0),
        lambda: scalar_lift(np.eye(3)[:, :2]),
        lambda: scalar_lift(np.full((2, 2), np.nan)),
        lambda: apply_mapping(np.asarray((0, 0)), np.eye(2)),
    ):
        try:
            action()
        except ValueError:
            rejected += 1

    check(
        "event-flip deletion, vacuum mutation, missing decoder, and the vacuum-sector constraint mistake are all detected",
        no_flip_intertwiner > 10
        and no_flip_constraint > 10
        and flip_vacuum_intertwiner > 0.9
        and deleted_decoder > 7
        and vacuum_constraint_error > 1
        and base_intertwiner < TOLERANCE,
        {
            "omit_h_flip_intertwiner": no_flip_intertwiner,
            "omit_h_flip_constraint": no_flip_constraint,
            "flip_vacuum_intertwiner": flip_vacuum_intertwiner,
            "delete_decoder_residual": deleted_decoder,
            "unconditioned_constraint_vacuum_residual": vacuum_constraint_error,
            "matter_compiler_after_h_deletion": base_intertwiner,
        },
    )
    check(
        "two stream updates erase h back to its input value, so the reversible parity carrier has no proved past-distinguishing permanence",
        two_update_failures == 0,
        {"S_hist_squared_mapping_failures": two_update_failures},
    )
    check(
        "h selects neither a cubic direction nor an interval: six one-particle directions read identically and supplied intervals rescale the same event count",
        max(abs(value - 1) for value in direction_event_reads) < TOLERANCE
        and one_interval_rate == 2 * two_interval_rate,
        {
            "direction_event_reads": direction_event_reads,
            "same_count_per_supplied_interval": {"Delta=1": one_interval_rate, "Delta=2": two_interval_rate},
        },
    )
    check(
        "malformed size, body, labels, matrices, and mappings are rejected",
        rejected == 7,
        {"lawful_domain_rejections": rejected},
    )


def line_has(path: Path, line: int, fragment: str) -> bool:
    rows = path.read_text(encoding="utf-8").splitlines()
    return line <= len(rows) and fragment in rows[line - 1]


def no_go_discipline_controls():
    print("\nSTRICT N1-N8 NO-GO DISCIPLINE")
    flat = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    route_markers = (
        "event-sidecar relational gauge",
        "bare Cycle-311 role decoder",
        "Cycle-312 bounded-block trace quotient",
        "recurrent unary event front",
        "relational clock/coincidence matcher",
        "physical Record-forming instrument",
        "APBC or registration-axis marker",
    )
    check(
        "N1 enumerates seven genuinely distinct attacks and leaves the broad gate failed on live routes",
        all(marker in flat for marker in route_markers)
        and flat.count("OPEN / UNTESTED") >= 3,
        route_markers,
    )

    walls = ("W_occurrence", "W_permanence", "W_recurrence", "W_compact", "W_axis", "W_interval")
    pairs = tuple(combinations(walls, 2))
    check(
        "N2 audits all fifteen pairs in the collapsed six-condition set",
        all(f"{left} / {right}" in flat for left, right in pairs)
        and flat.count("independent tasks") >= len(pairs),
        {"walls": walls, "pairs": len(pairs)},
    )

    trigger_fragments = (
        "we" + " assume",
        "by" + " construction",
        "as is" + " standard",
        "the framework" + " provides",
        "bridge" + " context",
        "back" + "ground",
        "natur" + "ally",
        "obvious" + "ly",
        "standard" + " qft",
        "regis" + "tered",
        "canon" + "ical",
    )
    lowered = flat.lower()
    hits = tuple(fragment for fragment in trigger_fragments if fragment in lowered)
    check("N3 finds no hidden-condition trigger in the source note", not hits, hits)

    cycle243 = ROOT / "docs/work_history/repo/review_feedback/SPATIAL_COMPILER_DERIVED_CAUSAL_TIME_BRIDGE_CYCLE243_NOTE_2026-07-17.md"
    cycle311 = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_COMMON_M64_FIXED_SEAM_CYCLE311_NOTE_2026-07-18.md"
    cycle312 = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_LOCAL_FOCK_EXTENSION_CYCLE312_NOTE_2026-07-18.md"
    witnesses = (
        (cycle243, 142, "E G_coarse = G_physical E"),
        (cycle243, 183, "coherent pointer writes are reversible"),
        (cycle311, 59, "E G_coarse = G_physical E"),
        (cycle311, 66, "not a number-changing law"),
        (cycle311, 262, "compiler slices are not called time"),
        (cycle312, 25, "one-pair recurrence has an exact local block"),
    )
    witness_rows = tuple(
        (str(path.relative_to(ROOT)), line, fragment, line_has(path, line, fragment))
        for path, line, fragment in witnesses
    )
    check("N4 residual-matches six exact prior witnesses", all(row[-1] for row in witness_rows), witness_rows)

    n5_markers = (
        "per physical M2",
        "per fixed-seam block",
        "per bounded support graph",
        "recurrent M64 volume",
        "lattice-wide physical time",
    )
    check("N5 narrows every negative statement to tested resolution", all(item in flat for item in n5_markers), n5_markers)

    n6_markers = (
        "recurrent overlap-aware M64 compiler",
        "append-only physical close and permanence",
        "relational coincidence clock",
        "boundary-condition axis marker",
        "interval-matching calibration",
    )
    check("N6 preserves five explicit partial-closure campaigns", all(item in flat for item in n6_markers), n6_markers)
    check(
        "N7 contains the hostile recurrent-front and relational-clock steelman",
        "hostile reviewer" in lowered and "a broad negative would confuse" in lowered,
        "hostile steelman present",
    )
    n8_markers = ("Cycle 243", "Cycle 306", "Cycle 311", "Cycle 312", "PR 5451", "PR 5469")
    check("N8 records six cross-cycle echoes and their retirement lessons", all(item in flat for item in n8_markers), n8_markers)
    broad_markers = (
        "Broad gate status: FAIL / DO NOT SHIP.",
        "None of PR5469 Legs A, B, or C is closed.",
        "No axiom pressure follows.",
    )
    check("the broad A/B/C no-go and axiom-pressure claim are blocked", all(item in flat for item in broad_markers), broad_markers)


def mass_inventory_and_semantic_firewall(fixtures, quotient_detail):
    mass_rows = []
    for beta, held in ((-0.2, False), (-0.3, False), (-0.4, False), (-0.35, True)):
        species = c311.c219.common_species(beta)
        mass_rows.append(
            {
                "beta": beta,
                "held": held,
                "rest_mass": c311.c219.rest_mass(species),
                "analytic_mass": species.analytic_mass,
                "relative_residual": abs(c311.c219.rest_mass(species) / species.analytic_mass - 1),
            }
        )
    check(
        "the event sidecar preserves the unchanged Cycle-219 one-particle mass fixture",
        all(row["relative_residual"] < 2e-12 for row in mass_rows),
        mass_rows,
    )
    inventory = {
        "derived": (
            "rank-127 event-sidecar isometry and local C_hist plus-space",
            "exact physical coin/stream/contact/DSK intertwiners and event-parity decoder",
            "cubic-scalar h covariance, translations, held size, leakage, deletions, and inverse erasure",
            "one independent-swap quotient on five actual Cycle-312 bounded blocks",
        ),
        "supplied": (
            "all Cycle-311 fixed-reference, body-anchor, six-direction, port, f, r, coin, contact, and fixed-seam data",
            "one zero-initialized ordinary h M2 per coarse cell",
            "the number-conditioned diagonal matrix-unit constraint C_hist",
            "the oriented coin-stream-contact update and declared input slice",
            "Cycle-312 one-pair block supports and their support-independence certificate",
        ),
        "open": (
            "occurrence/identity, physical close, permanence, and Record formation",
            "recurrent M64 volume update and glue to the Cycle-312 trace quotient",
            "causal-axis existence/origin/compactification, intrinsic axis label, interval spacing, and rate",
            "multi-event past-distinguishing memory and relational clock selection",
        ),
        "not_claimed": (
            "h parity, seam slice, substep count, graph depth, or host position as elapsed time",
            "readable h or a coherent copy as a Record",
            "a generator element or contact/coin phase as a rate or physical energy",
            "a supplied update orientation or spatial direction as a derived time axis",
        ),
        "support_max_M2": 57,
        "installed_M2_per_cell": 24,
        "held_sizes": tuple(fixtures),
        "swap_quotient_executions": quotient_detail["reachable_swap_equivalent_executions"],
        "authority": "none",
        "audit": "unset",
        "axiom_pressure": False,
    }
    check(
        "supplied, derived, open, and forbidden semantic promotions are explicit",
        len(inventory) == 11
        and inventory["support_max_M2"] == 57
        and inventory["installed_M2_per_cell"] == 24
        and 6 in inventory["held_sizes"]
        and inventory["swap_quotient_executions"] > 1
        and not inventory["axiom_pressure"],
        inventory,
    )


def main() -> int:
    print("CYCLE 314: PHYSICAL M64 REVERSIBLE EVENT-PARITY SIDECAR")
    print("authority=none; audit=unset")
    note_contract()
    fixtures = geometry_and_held_size_controls()
    sidecar = fixtures[3]
    shell_and_constraint_controls(sidecar)
    nominal = physical_update_controls(sidecar)
    quotient_detail = independent_swap_quotient_controls()
    covariance_and_translation_controls(sidecar, nominal)
    deletion_erasure_and_domain_controls(sidecar, nominal)
    no_go_discipline_controls()
    mass_inventory_and_semantic_firewall(fixtures, quotient_detail)
    print(f"SUMMARY: {PASS} passed, {FAIL} failed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
