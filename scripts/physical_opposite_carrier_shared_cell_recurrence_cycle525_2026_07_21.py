#!/usr/bin/env python3
"""Cycle 525: opposite-carrier shared-cell recurrence certificate.

This runner multiplies three actual selected Cycle-522 cell encoders on one
Cycle-269 physical patch.  It does not replace the shared middle cell by two
independent tensor factors.  Six physical cell-factor orders are coupled to
the inherited bounded S3 role register, and two incident seams are applied in
both orders through total three-cell number n<=3.

The physical updates are algebraic code-space completions.  Their matrix
coefficients, role preparation, schedule, and off-code identity action remain
supplied.  An update count or factor order is not physical time.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_cycle269_three_cell_multiedge_cycle319_2026_07_18 as c319
import physical_cycle269_four_cell_star_cycle324_2026_07_18 as c324
import physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21 as c522


AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
MAX_TOTAL_NUMBER = 3
TOLERANCE = 5.0e-11
WALL_LIMIT_SECONDS = 600.0
RSS_GUARD_BYTES = 3_000_000_000

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_OPPOSITE_CARRIER_SHARED_CELL_RECURRENCE_CYCLE525_NOTE_2026-07-21.md"
)
CYCLE315_RUNNER = ROOT / "scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py"
CYCLE319_RUNNER = ROOT / "scripts/physical_cycle269_three_cell_multiedge_cycle319_2026_07_18.py"
CYCLE324_RUNNER = ROOT / "scripts/physical_cycle269_four_cell_star_cycle324_2026_07_18.py"
CYCLE522_RUNNER = ROOT / "scripts/physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21.py"
STRICT_FILE_HASHES = {
    CYCLE315_RUNNER: "52c18f96a1f8db9b79e4d0fba5ff76905170e6a8dc8c3e818fdf69984a1778c3",
    CYCLE319_RUNNER: "faa05d97542efca7684f4acc6f9b7dfb8e32a02f3f9d16adeae16449f5b702fb",
    CYCLE324_RUNNER: "f2e07bf91e7a5b06c8037314798cb84cd6d747bc92fa6292c1759915fb91354d",
    CYCLE522_RUNNER: "d6a7700d7575dfba02d4b4d2438e54d37a02c6ca7f71673c8a871b474f6e088b",
}

PASS = 0
FAIL = 0


class ResourceWall(RuntimeError):
    """Technical execution ceiling, never a physical conclusion."""


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
        raise ResourceWall(f"wall limit reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard reached at {label}: {rss}")
    if swaps != 0:
        raise ResourceWall(f"nonzero process swap count at {label}: {swaps}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swaps,
    }


def alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard wall alarm reached")


def check(label: str, condition: bool, detail: object) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def semantic_upstream_contract() -> dict:
    cycle319 = CYCLE319_RUNNER.read_text(encoding="utf-8")
    cycle522 = CYCLE522_RUNNER.read_text(encoding="utf-8")
    cycle324 = CYCLE324_RUNNER.read_text(encoding="utf-8")
    predicates = {
        "Cycle319_six_orders": "ORDERS = tuple(permutations(range(3)))" in cycle319,
        "Cycle319_actual_shared_reducer": "one shared ray reducer" in cycle319,
        "Cycle319_joint_S3": "joint_S3_constraint_plus_rank" in cycle319,
        "Cycle319_two_incident_streams": "two_FSWAP_commutator" in cycle319,
        "Cycle522_opposite_selector": "(direction ^ 1) in label" in cycle522,
        "Cycle522_selected_normalization": (
            "math.sqrt((6 - number) / len(kept))" in cycle522
        ),
        "Cycle522_rebuilt_completion": "selected_projector" in cycle522,
        "Cycle324_twenty_four_orders": (
            "ORDERS = tuple(permutations(range(4)))" in cycle324
        ),
        "Cycle324_three_incident_streams": "maximum_stream_commutator" in cycle324,
    }
    expected_hashes = {
        str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()
    }
    observed_hashes = {
        str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES
    }
    return {
        "predicates": predicates,
        "expected_sha256": expected_hashes,
        "observed_sha256": observed_hashes,
        "pass": all(predicates.values()) and expected_hashes == observed_hashes,
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing": (str(NOTE),), "pass": False}
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "988",
        "301",
        "8,272",
        "8,288",
        "joint selected physical encoder",
        "shared middle",
        "rebuilt",
        "supplied schedule",
        "not physical time",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def triple_labels(maximum_number: int = MAX_TOTAL_NUMBER):
    if maximum_number < 0 or maximum_number > MAX_TOTAL_NUMBER:
        raise ValueError("the Cycle-525 recurrence domain is total n=0..3")
    return c319.triple_labels(maximum_number)


def label_specs(label):
    return c319.label_specs(label)


def selected_terms(code, cell, number, local_label, delete_cell_role: bool = False):
    terms = c522.selected_gauge_terms(code, cell, number, local_label)
    if delete_cell_role:
        # Every carrier contributes its input/r=0 term followed by its
        # exchanged/r=1 partner.  Removing the second member is a literal
        # deletion without renormalization.
        return terms[::2]
    return terms


def multi_order_encodings(
    code,
    cells,
    labels,
    deleted_role_cell=None,
):
    """Multiply all three actual physical cell factors on one shared code."""

    reducer = c315.RayReducer(code)
    cache = {}
    row_indices = [[] for _ in c319.ORDERS]
    column_indices = [[] for _ in c319.ORDERS]
    data = [[] for _ in c319.ORDERS]
    physical_union = 0
    maximum_joint_branch = 0
    branch_products = 0
    for column, label in enumerate(labels):
        terms_by_cell = []
        for cell, (number, local_label) in zip(cells, label_specs(label)):
            cache_key = (cell, number, local_label, cell == deleted_role_cell)
            terms = cache.setdefault(
                cache_key,
                selected_terms(
                    code,
                    cell,
                    number,
                    local_label,
                    delete_cell_role=cell == deleted_role_cell,
                ),
            )
            terms_by_cell.append(terms)
            for term in terms:
                physical_union |= term.representative.x | term.representative.z

        amplitudes = [defaultdict(complex) for _ in c319.ORDERS]
        for term_tuple in product(*terms_by_cell):
            branch_products += 1
            coefficient = np.prod([term.amplitude for term in term_tuple])
            representatives = tuple(
                term_tuple[order[0]].representative
                @ term_tuple[order[1]].representative
                @ term_tuple[order[2]].representative
                for order in c319.ORDERS
            )
            reference = representatives[0]
            row, reference_phase = reducer.reduce(reference)
            maximum_joint_branch = max(
                maximum_joint_branch,
                (reference.x | reference.z).bit_count(),
            )
            for order_index, representative in enumerate(representatives):
                if representative.x != reference.x or representative.z != reference.z:
                    raise AssertionError("cell-factor order changed physical support")
                relative_phase = c319.c311.c308.phase_scalar(
                    (representative.phase - reference.phase) % 4
                )
                amplitudes[order_index][row] += (
                    coefficient * reference_phase * relative_phase
                )

        for order_index, column_amplitudes in enumerate(amplitudes):
            for row, value in column_amplitudes.items():
                if abs(value) <= 2e-13:
                    continue
                row_indices[order_index].append(row)
                column_indices[order_index].append(column)
                data[order_index].append(value)

    rows = len(reducer.row_by_aux)
    encodings = tuple(
        sparse.coo_matrix(
            (data[index], (row_indices[index], column_indices[index])),
            shape=(rows, len(labels)),
            dtype=complex,
        ).tocsc()
        for index in range(len(c319.ORDERS))
    )
    return encodings, reducer, {
        "actual_three_cell_branch_products": branch_products,
        "face_port_cell_role_union_M2": physical_union.bit_count(),
        "maximum_joint_branch_before_multiedge_role_M2": maximum_joint_branch,
    }


def four_cell_multi_order_encodings(code, cells, labels):
    """Multiply all 24 actual four-cell orders for the selected S4 star."""

    reducer = c315.RayReducer(code)
    cache = {}
    row_indices = [[] for _ in c324.ORDERS]
    column_indices = [[] for _ in c324.ORDERS]
    data = [[] for _ in c324.ORDERS]
    physical_union = 0
    maximum_joint_branch = 0
    branch_products = 0
    for column, label in enumerate(labels):
        terms_by_cell = []
        for cell, (number, local_label) in zip(cells, c324.label_specs(label)):
            terms = cache.setdefault(
                (cell, number, local_label),
                selected_terms(code, cell, number, local_label),
            )
            terms_by_cell.append(terms)
            for term in terms:
                physical_union |= term.representative.x | term.representative.z

        amplitudes = [defaultdict(complex) for _ in c324.ORDERS]
        for term_tuple in product(*terms_by_cell):
            branch_products += 1
            coefficient = np.prod([term.amplitude for term in term_tuple])
            representatives = tuple(
                term_tuple[order[0]].representative
                @ term_tuple[order[1]].representative
                @ term_tuple[order[2]].representative
                @ term_tuple[order[3]].representative
                for order in c324.ORDERS
            )
            reference = representatives[0]
            row, reference_phase = reducer.reduce(reference)
            maximum_joint_branch = max(
                maximum_joint_branch,
                (reference.x | reference.z).bit_count(),
            )
            for order_index, representative in enumerate(representatives):
                if representative.x != reference.x or representative.z != reference.z:
                    raise AssertionError("four-cell order changed physical support")
                relative_phase = c319.c311.c308.phase_scalar(
                    (representative.phase - reference.phase) % 4
                )
                amplitudes[order_index][row] += (
                    coefficient * reference_phase * relative_phase
                )

        for order_index, column_amplitudes in enumerate(amplitudes):
            for row, value in column_amplitudes.items():
                if abs(value) <= 2e-13:
                    continue
                row_indices[order_index].append(row)
                column_indices[order_index].append(column)
                data[order_index].append(value)

    rows = len(reducer.row_by_aux)
    encodings = tuple(
        sparse.coo_matrix(
            (data[index], (row_indices[index], column_indices[index])),
            shape=(rows, len(labels)),
            dtype=complex,
        ).tocsc()
        for index in range(len(c324.ORDERS))
    )
    return encodings, reducer, {
        "actual_four_cell_branch_products": branch_products,
        "face_port_cell_role_union_M2": physical_union.bit_count(),
        "maximum_joint_branch_before_role_register_M2": maximum_joint_branch,
    }


def inherited_cell_constraint_controls(code, cells) -> dict:
    port_constraint_failures = 0
    fixed_sector_failures = 0
    role_pair_failures = 0
    role_pairs = 0
    local_union = 0
    maximum_local_branch = 0
    for cell in cells:
        for number, local_label in c319.c311.FOCK_LABELS:
            terms = selected_terms(code, cell, number, local_label)
            role_pair_failures += len(terms) % 2
            for first, second in zip(terms[::2], terms[1::2]):
                role_pairs += 1
                role_pair_failures += abs(first.amplitude - second.amplitude) > TOLERANCE
            for term in terms:
                word = term.representative.x | term.representative.z
                local_union |= word
                maximum_local_branch = max(maximum_local_branch, word.bit_count())
                port_constraint_failures += sum(
                    not term.representative.commutes(
                        c319.c305.constraint_pauli(code, vertex)
                    )
                    for vertex in range(len(code.graph.vertices))
                )
                fixed_sector_failures += sum(
                    not term.representative.commutes(check_word)
                    for check_word in code.local_checks + code.wilsons
                )
    return {
        "selected_cell_role_pairs": role_pairs,
        "cell_role_pairing_failures": role_pair_failures,
        "local_physical_union_M2": local_union.bit_count(),
        "maximum_local_branch_M2": maximum_local_branch,
        "port_constraint_commutator_failures": port_constraint_failures,
        "fixed_sector_commutator_failures": fixed_sector_failures,
    }


def joint_role_physical_controls(encodings, logical_update) -> dict:
    """Test a joint symmetric-group role and rebuilt actual-order update."""

    order_count = len(encodings)
    columns = encodings[0].shape[1]
    rows = encodings[0].shape[0]
    identity = sparse.eye(columns, format="csc")
    joint_encoder = sparse.vstack(encodings, format="csc") / math.sqrt(order_count)
    gram = (joint_encoder.conj().T @ joint_encoder).tocsc()

    uniform = np.ones(order_count, dtype=complex) / math.sqrt(order_count)
    joint_small = 2 * np.outer(uniform, uniform) - np.eye(order_count)
    joint_shell = sparse.kron(
        sparse.csc_matrix(joint_small), identity, format="csc"
    )

    def split(vector):
        return [
            vector[index * rows : (index + 1) * rows]
            for index in range(order_count)
        ]

    def apply_update(vector, operator):
        output = []
        for encoding, block in zip(encodings, split(vector)):
            coefficients = encoding.conj().T @ block
            output.append(
                block + encoding @ (operator @ coefficients - coefficients)
            )
        return np.concatenate(output)

    def apply_constraint(vector):
        blocks = split(vector)
        coefficients = np.concatenate(
            [encoding.conj().T @ block for encoding, block in zip(encodings, blocks)]
        )
        transformed = joint_shell @ coefficients
        output = []
        for index, (encoding, block) in enumerate(zip(encodings, blocks)):
            source = coefficients[index * columns : (index + 1) * columns]
            target = transformed[index * columns : (index + 1) * columns]
            output.append(block + encoding @ (target - source))
        return np.concatenate(output)

    encoded_blocks = [encoding / math.sqrt(order_count) for encoding in encodings]
    physical_eigen_blocks = []
    logical_coefficients = []
    for source in range(order_count):
        source_gram = encodings[source].conj().T @ encoded_blocks[source]
        logical_coefficients.append(source_gram)
    for target in range(order_count):
        transformed = sum(
            (
                joint_small[target, source] * logical_coefficients[source]
                for source in range(order_count)
            ),
            start=sparse.csc_matrix((columns, columns), dtype=complex),
        )
        source = logical_coefficients[target]
        physical_eigen_blocks.append(
            encoded_blocks[target] + encodings[target] @ (transformed - source)
            - encoded_blocks[target]
        )
    physical_eigen_difference = sparse.vstack(physical_eigen_blocks, format="csc")

    physical_image_blocks = []
    for encoding, encoded_block in zip(encodings, encoded_blocks):
        coefficients = encoding.conj().T @ encoded_block
        physical_image_blocks.append(
            encoded_block
            + encoding @ (logical_update @ coefficients - coefficients)
        )
    physical_image = sparse.vstack(physical_image_blocks, format="csc")
    intertwining = physical_image - joint_encoder @ logical_update
    leakage = physical_image - joint_encoder @ (
        joint_encoder.conj().T @ physical_image
    )

    rng = np.random.default_rng(525 + rows + order_count)
    inverse_residuals = []
    constraint_involution_residuals = []
    constraint_update_commutators = []
    for _ in range(3):
        vector = rng.normal(size=joint_encoder.shape[0]) + 1j * rng.normal(
            size=joint_encoder.shape[0]
        )
        vector /= np.linalg.norm(vector)
        forward = apply_update(vector, logical_update)
        backward = apply_update(forward, logical_update.conj().T)
        inverse_residuals.append(float(np.linalg.norm(backward - vector)))
        constrained_twice = apply_constraint(apply_constraint(vector))
        constraint_involution_residuals.append(
            float(np.linalg.norm(constrained_twice - vector))
        )
        left = apply_constraint(apply_update(vector, logical_update))
        right = apply_update(apply_constraint(vector), logical_update)
        constraint_update_commutators.append(float(np.linalg.norm(left - right)))

    return {
        "actual_joint_encoder_rows": joint_encoder.shape[0],
        "actual_joint_encoder_nonzeros": joint_encoder.nnz,
        "joint_encoder_Gram_residual": c315.largest_singular(gram - identity),
        "joint_encoder_Gram_raw_maximum": c315.raw_maximum_abs(gram - identity),
        "physical_joint_constraint_eigen_residual": c315.largest_singular(
            physical_eigen_difference
        ),
        "physical_joint_constraint_eigen_raw_maximum": c315.raw_maximum_abs(
            physical_eigen_difference
        ),
        "physical_update_intertwining_residual": c315.largest_singular(
            intertwining
        ),
        "physical_update_intertwining_raw_maximum": c315.raw_maximum_abs(
            intertwining
        ),
        "physical_update_terminal_leakage_residual": c315.largest_singular(leakage),
        "physical_update_terminal_leakage_raw_maximum": c315.raw_maximum_abs(leakage),
        "maximum_randomized_physical_inverse_residual": max(inverse_residuals),
        "maximum_randomized_joint_constraint_involution_residual": max(
            constraint_involution_residuals
        ),
        "maximum_randomized_constraint_update_commutator": max(
            constraint_update_commutators
        ),
        "rebuilt_formula": "E U E^dagger + I - E E^dagger, order-blockwise",
        "off_code_identity_completion_supplied": True,
    }


def physical_shell_controls(kind: str, length: int, labels, logical_update):
    if kind not in c319.GEOMETRIES:
        raise ValueError("geometry must be path or corner")
    if length < TRAIN_LENGTH:
        raise ValueError("the Cycle-525 declared domain is nonaliased L>=5")
    code = c319.c269.build_code(length)
    cells = c319.GEOMETRIES[kind]["cells"]
    encodings, reducer, support = multi_order_encodings(code, cells, labels)
    identity = sparse.eye(len(labels), format="csc")
    order_rows = []
    grams = []
    for order, encoding in zip(c319.ORDERS, encodings):
        gram = (encoding.conj().T @ encoding).tocsc()
        grams.append(gram)
        difference = gram - identity
        order_rows.append(
            {
                "order": "".join("ABC"[index] for index in order),
                "physical_rays": encoding.shape[0],
                "matrix_nonzeros": encoding.nnz,
                "Gram_residual": c315.largest_singular(difference),
                "Gram_raw_maximum": c315.raw_maximum_abs(difference),
            }
        )
    joint_gram = sum(
        grams, start=sparse.csc_matrix(identity.shape, dtype=complex)
    ) / 6
    joint_difference = joint_gram - identity
    deleted_order_gram = sum(
        grams[:5], start=sparse.csc_matrix(identity.shape, dtype=complex)
    ) / 6
    constraints = inherited_cell_constraint_controls(code, cells)
    physical = joint_role_physical_controls(encodings, logical_update)
    result = {
        "geometry": kind,
        "L": length,
        "held": length == HELD_LENGTH,
        "logical_columns_n0_to_n3": len(labels),
        "shared_physical_rays": len(reducer.row_by_aux),
        "six_order_total_nonzeros": sum(encoding.nnz for encoding in encodings),
        "order_rows": order_rows,
        "maximum_order_Gram_residual": max(row["Gram_residual"] for row in order_rows),
        "maximum_order_Gram_raw_maximum": max(
            row["Gram_raw_maximum"] for row in order_rows
        ),
        "joint_S3_Gram_residual": c315.largest_singular(joint_difference),
        "joint_S3_Gram_raw_maximum": c315.raw_maximum_abs(joint_difference),
        "joint_S3_minimum_Gram_eigenvalue": float(
            eigsh(
                joint_gram,
                k=1,
                which="SA",
                return_eigenvectors=False,
                tol=2e-10,
            )[0]
        ),
        "ABC_to_BAC_physical_order_residual": c315.largest_singular(
            encodings[c319.ORDER_INDEX[(0, 1, 2)]]
            - encodings[c319.ORDER_INDEX[(1, 0, 2)]]
        ),
        "ABC_to_ACB_physical_order_residual": c315.largest_singular(
            encodings[c319.ORDER_INDEX[(0, 1, 2)]]
            - encodings[c319.ORDER_INDEX[(0, 2, 1)]]
        ),
        "deleted_one_order_amplitude_Gram_residual": c315.largest_singular(
            deleted_order_gram - identity
        ),
        **support,
        **constraints,
        "joint_S3_role_register_M2": 3,
        "total_patch_union_with_joint_S3_role_M2": (
            support["face_port_cell_role_union_M2"] + 3
        ),
        "maximum_joint_branch_with_joint_S3_role_M2": (
            support["maximum_joint_branch_before_multiedge_role_M2"] + 3
        ),
        "physical_update": physical,
    }
    return result


def four_cell_star_update_controls(labels) -> tuple[dict, object]:
    update, coin, streams, contact, update_orders = c324.update_controls(
        labels, "star"
    )
    frames = c324.covariance_schedule_controls(
        labels, "star", coin, streams, contact, update_orders
    )
    role = c324.role_register_controls(len(labels))
    reference = update_orders[0][1]
    preservation = tuple(
        c324.joint_update_controls(candidate, len(labels))
        for _order, candidate in update_orders
    )
    missing_first = contact @ streams[2] @ streams[1] @ coin
    return {
        "logical_update": update,
        "proper_frames_and_three_slot_schedule": frames,
        "role_algebra": role,
        "six_order_joint_role_preservation": preservation,
        "shared_center_modes": tuple(
            endpoint[1]
            for edge in c324.GEOMETRIES["star"]["edges"]
            for endpoint in edge
            if endpoint[0] == 1
        ),
        "missing_first_seam_target_residual": c315.largest_singular(
            reference - missing_first
        ),
    }, reference


def four_cell_star_shell(length: int, labels, logical_update) -> dict:
    if length < TRAIN_LENGTH:
        raise ValueError("the selected four-cell star declares L>=5")
    code = c324.c269.build_code(length)
    cells = c324.GEOMETRIES["star"]["cells"]
    encodings, reducer, support = four_cell_multi_order_encodings(
        code, cells, labels
    )
    identity = sparse.eye(len(labels), format="csc")
    grams = []
    order_rows = []
    for order, encoding in zip(c324.ORDERS, encodings):
        gram = (encoding.conj().T @ encoding).tocsc()
        grams.append(gram)
        difference = gram - identity
        order_rows.append(
            {
                "order": "".join("ABCD"[index] for index in order),
                "physical_rays": encoding.shape[0],
                "matrix_nonzeros": encoding.nnz,
                "Gram_residual": c315.largest_singular(difference),
                "Gram_raw_maximum": c315.raw_maximum_abs(difference),
            }
        )
    joint_gram = sum(
        grams, start=sparse.csc_matrix(identity.shape, dtype=complex)
    ) / 24
    deleted_order_gram = sum(
        grams[:23], start=sparse.csc_matrix(identity.shape, dtype=complex)
    ) / 24
    constraints = inherited_cell_constraint_controls(code, cells)
    physical = joint_role_physical_controls(encodings, logical_update)
    return {
        "geometry": "star",
        "L": length,
        "held": length == HELD_LENGTH,
        "logical_columns_n0_to_n2": len(labels),
        "shared_physical_rays": len(reducer.row_by_aux),
        "twenty_four_order_total_nonzeros": sum(
            encoding.nnz for encoding in encodings
        ),
        "order_rows": order_rows,
        "maximum_order_Gram_residual": max(
            row["Gram_residual"] for row in order_rows
        ),
        "maximum_order_Gram_raw_maximum": max(
            row["Gram_raw_maximum"] for row in order_rows
        ),
        "joint_S4_Gram_residual": c315.largest_singular(joint_gram - identity),
        "joint_S4_Gram_raw_maximum": c315.raw_maximum_abs(joint_gram - identity),
        "joint_S4_minimum_Gram_eigenvalue": float(
            eigsh(
                joint_gram,
                k=1,
                which="SA",
                return_eigenvectors=False,
                tol=2e-10,
            )[0]
        ),
        "ABCD_to_BACD_physical_order_residual": c315.largest_singular(
            encodings[c324.ORDER_INDEX[(0, 1, 2, 3)]]
            - encodings[c324.ORDER_INDEX[(1, 0, 2, 3)]]
        ),
        "ABCD_to_ACBD_physical_order_residual": c315.largest_singular(
            encodings[c324.ORDER_INDEX[(0, 1, 2, 3)]]
            - encodings[c324.ORDER_INDEX[(0, 2, 1, 3)]]
        ),
        "deleted_one_order_amplitude_Gram_residual": c315.largest_singular(
            deleted_order_gram - identity
        ),
        **support,
        **constraints,
        "joint_S4_role_register_M2": 5,
        "total_patch_union_with_joint_S4_role_M2": (
            support["face_port_cell_role_union_M2"] + 5
        ),
        "maximum_joint_branch_with_joint_S4_role_M2": (
            support["maximum_joint_branch_before_role_register_M2"] + 5
        ),
        "physical_update": physical,
    }


def local_selected_frame_controls() -> dict:
    rows = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        local, objects = c522.local_shell_controls(length)
        frames = c522.frame_controls(objects)
        rows.append(
            {
                "L": length,
                "local_selected_Gram_residual": local["selected_Gram_residual"],
                "proper_cubic_frames": frames["proper_frames"],
                "branch_covariance_failures": frames["physical_branch_failures"],
                "encoder_covariance_residual": frames[
                    "maximum_covariance_residuals"
                ]["isometry"],
                "rebuilt_update_covariance_residual": frames[
                    "maximum_covariance_residuals"
                ]["composition"],
                "frame_group_law_failures": frames["frame_group_failures"],
                "selector_failures": frames["odd_label_selector_failures"],
            }
        )
    return {
        "rows": rows,
        "pass": all(
            row["proper_cubic_frames"] == 24
            and row["branch_covariance_failures"] == 0
            and row["encoder_covariance_residual"] < TOLERANCE
            and row["rebuilt_update_covariance_residual"] < TOLERANCE
            and row["frame_group_law_failures"] == 0
            and row["selector_failures"] == 0
            for row in rows
        ),
    }


def update_and_frame_controls(labels) -> tuple[dict, dict]:
    results = {}
    operators = {}
    for kind in c319.GEOMETRIES:
        update, coin, first, second, contact, forward, reverse = c319.update_controls(
            labels, kind
        )
        frames = c319.covariance_schedule_controls(
            labels,
            kind,
            coin,
            first,
            second,
            contact,
            forward,
            reverse,
        )
        forward_preservation = c319.joint_update_preservation_controls(
            forward, len(labels)
        )
        reverse_preservation = c319.joint_update_preservation_controls(
            reverse, len(labels)
        )
        missing_first = contact @ second @ coin
        deleted_first_column = first.tolil(copy=True)
        deleted_first_column[:, 0] = 0
        deleted_first_column = deleted_first_column.tocsc()
        identity = sparse.eye(len(labels), format="csc")
        results[kind] = {
            "logical_update": update,
            "proper_frames_and_schedule": frames,
            "forward_joint_role_preservation": forward_preservation,
            "reverse_joint_role_preservation": reverse_preservation,
            "shared_middle_modes": tuple(
                endpoint[1]
                for edge in c319.GEOMETRIES[kind]["edges"]
                for endpoint in edge
                if endpoint[0] == 1
            ),
            "missing_first_seam_target_residual": c315.largest_singular(
                forward - missing_first
            ),
            "deleted_first_FSWAP_column_unitarity_residual": c315.largest_singular(
                deleted_first_column.conj().T @ deleted_first_column - identity
            ),
        }
        operators[kind] = {"forward": forward, "reverse": reverse}
    return results, operators


def deletion_controls(labels) -> dict:
    code = c319.c269.build_code(TRAIN_LENGTH)
    middle = c319.GEOMETRIES["path"]["cells"][1]
    encodings, _reducer, _support = multi_order_encodings(
        code,
        c319.GEOMETRIES["path"]["cells"],
        labels,
        deleted_role_cell=middle,
    )
    identity = sparse.eye(len(labels), format="csc")
    residuals = [
        c315.largest_singular(encoding.conj().T @ encoding - identity)
        for encoding in encodings
    ]
    return {
        "deleted_middle_cell_role_Gram_residuals": residuals,
        "minimum_deleted_middle_cell_role_Gram_residual": min(residuals),
        "expected_exact_residual": 0.5,
    }


def role_gauge_pass(role: dict) -> bool:
    return (
        role["simultaneous_common_rank_factor"] == 2
        and role["simultaneous_constraint_commutator"] > 1
        and role["independent_constraint_braid_residual"] > 1
        and role["endpoint_exchange_braid_residual"] == 0
        and role["joint_S3_constraint_plus_rank"] == 988
        and role["joint_S3_constraint_involution_residual"] == 0
        and role["joint_S3_left_swap_commutator"] == 0
        and role["joint_S3_right_swap_commutator"] == 0
        and role["joint_S3_eigen_residual"] < TOLERANCE
    )


def update_pass(result: dict) -> bool:
    logical = result["logical_update"]
    frames = result["proper_frames_and_schedule"]
    return (
        logical["logical_columns"] == 988
        and logical["coin_nonzeros"] == 94_342
        and logical["two_FSWAP_commutator"] == 0
        and logical["two_ordered_update_residual"] == 0
        and logical["forward_update_unitarity_raw_maximum"] < TOLERANCE
        and logical["reverse_update_unitarity_raw_maximum"] < TOLERANCE
        and abs(logical["three_cell_rest_mass"] - logical["Cycle219_mass_fixture"])
        < TOLERANCE
        and logical["uniform_one_particle_eigen_residual"] < TOLERANCE
        and all(
            row["dimension"] == row["expected_dimension"]
            and row["update_unitarity_raw_maximum"] < TOLERANCE
            for row in logical["number_rows"]
        )
        and frames["proper_cubic_frames"] == 24
        and frames["maximum_update_covariance_residual"] == 0
        and frames["frame_group_law_failures"] == 0
        and frames["arm_exchange_update_residual"] == 0
        and frames["slot_operator_unitarity"] == 0
        and frames["slot_square_macro_residual"] == 0
        and frames["slot_arm_exchange_covariance"] == 0
        and frames["host_branch_queries"] == 0
        and result["shared_middle_modes"][0] != result["shared_middle_modes"][1]
        and result["missing_first_seam_target_residual"] > 1
        and result["deleted_first_FSWAP_column_unitarity_residual"] > 0.99
    )


def shell_pass(result: dict) -> bool:
    physical = result["physical_update"]
    return (
        result["logical_columns_n0_to_n3"] == 988
        and result["shared_physical_rays"] == 8_272
        and result["six_order_total_nonzeros"] == 49_728
        and all(row["matrix_nonzeros"] == 8_288 for row in result["order_rows"])
        and result["maximum_order_Gram_residual"] == 0
        and result["maximum_order_Gram_raw_maximum"] < TOLERANCE
        and result["joint_S3_Gram_residual"] == 0
        and abs(result["joint_S3_minimum_Gram_eigenvalue"] - 1) < TOLERANCE
        and result["ABC_to_BAC_physical_order_residual"] > 1.9
        and result["ABC_to_ACB_physical_order_residual"] > 1.9
        and abs(result["deleted_one_order_amplitude_Gram_residual"] - 1 / 6)
        < TOLERANCE
        and result["cell_role_pairing_failures"] == 0
        and result["port_constraint_commutator_failures"] == 0
        and result["fixed_sector_commutator_failures"] == 0
        and result["total_patch_union_with_joint_S3_role_M2"] == 121
        and result["maximum_joint_branch_with_joint_S3_role_M2"] == 45
        and physical["actual_joint_encoder_rows"] == 49_632
        and physical["actual_joint_encoder_nonzeros"] == 49_728
        and physical["joint_encoder_Gram_residual"] == 0
        and physical["physical_joint_constraint_eigen_residual"] == 0
        and physical["physical_update_intertwining_residual"] == 0
        and physical["physical_update_intertwining_raw_maximum"] < TOLERANCE
        and physical["physical_update_terminal_leakage_residual"] == 0
        and physical["physical_update_terminal_leakage_raw_maximum"] < TOLERANCE
        and physical["maximum_randomized_physical_inverse_residual"] < TOLERANCE
        and physical[
            "maximum_randomized_joint_constraint_involution_residual"
        ]
        < TOLERANCE
        and physical["maximum_randomized_constraint_update_commutator"]
        < TOLERANCE
    )


def four_cell_update_pass(result: dict) -> bool:
    logical = result["logical_update"]
    frames = result["proper_frames_and_three_slot_schedule"]
    role = result["role_algebra"]
    preservation = result["six_order_joint_role_preservation"]
    return (
        logical["logical_columns"] == 301
        and logical["coin_nonzeros"] == 8_701
        and logical["maximum_stream_commutator"] == 0
        and logical["maximum_ordered_update_residual"] == 0
        and logical["maximum_update_unitarity_raw_maximum"] < TOLERANCE
        and abs(logical["four_cell_rest_mass"] - logical["Cycle219_mass_fixture"])
        < TOLERANCE
        and logical["uniform_one_particle_eigen_residual"] < TOLERANCE
        and all(
            row["dimension"] == row["expected_dimension"]
            and row["update_unitarity_raw_maximum"] < TOLERANCE
            for row in logical["number_rows"]
        )
        and role["overlapping_S3_common_rank_factor"] == 1
        and role["maximum_overlapping_S3_constraint_commutator"] > 1
        and role["joint_S4_plus_rank"] == 301
        and role["joint_S4_constraint_involution"] == 0
        and role["joint_S4_maximum_adjacent_swap_commutator"] == 0
        and role["S4_left_braid_residual"] == 0
        and role["S4_right_braid_residual"] == 0
        and role["S4_far_commutator"] == 0
        and frames["proper_cubic_frames"] == 24
        and frames["maximum_update_covariance_residual"] == 0
        and frames["frame_group_law_failures"] == 0
        and frames["slot_operator_unitarity"] == 0
        and frames["slot_cube_residual"] == 0
        and frames["maximum_slot_frame_covariance"] == 0
        and frames["host_branch_queries"] == 0
        and len(set(result["shared_center_modes"])) == 3
        and result["missing_first_seam_target_residual"] > 1
        and all(
            row["joint_update_constraint_commutator"] == 0
            and row["joint_update_intertwining_residual"] == 0
            for row in preservation
        )
    )


def four_cell_shell_pass(result: dict) -> bool:
    physical = result["physical_update"]
    return (
        result["logical_columns_n0_to_n2"] == 301
        and result["shared_physical_rays"] == 4_816
        and result["twenty_four_order_total_nonzeros"] == 115_584
        and all(row["matrix_nonzeros"] == 4_816 for row in result["order_rows"])
        and result["maximum_order_Gram_residual"] == 0
        and result["maximum_order_Gram_raw_maximum"] < TOLERANCE
        and result["joint_S4_Gram_residual"] == 0
        and abs(result["joint_S4_minimum_Gram_eigenvalue"] - 1) < TOLERANCE
        and result["ABCD_to_BACD_physical_order_residual"] > 1.4
        and result["ABCD_to_ACBD_physical_order_residual"] > 1.4
        and abs(result["deleted_one_order_amplitude_Gram_residual"] - 1 / 24)
        < TOLERANCE
        and result["cell_role_pairing_failures"] == 0
        and result["port_constraint_commutator_failures"] == 0
        and result["fixed_sector_commutator_failures"] == 0
        and result["total_patch_union_with_joint_S4_role_M2"] == 160
        and result["maximum_joint_branch_with_joint_S4_role_M2"] == 32
        and physical["actual_joint_encoder_rows"] == 115_584
        and physical["actual_joint_encoder_nonzeros"] == 115_584
        and physical["joint_encoder_Gram_residual"] == 0
        and physical["physical_joint_constraint_eigen_residual"] == 0
        and physical["physical_update_intertwining_residual"] == 0
        and physical["physical_update_intertwining_raw_maximum"] < TOLERANCE
        and physical["physical_update_terminal_leakage_residual"] == 0
        and physical["physical_update_terminal_leakage_raw_maximum"] < TOLERANCE
        and physical["maximum_randomized_physical_inverse_residual"] < TOLERANCE
        and physical[
            "maximum_randomized_joint_constraint_involution_residual"
        ]
        < TOLERANCE
        and physical["maximum_randomized_constraint_update_commutator"]
        < TOLERANCE
    )


def domain_controls(labels) -> dict:
    rejects = 0
    for operation in (
        lambda: triple_labels(4),
        lambda: c324.four_cell_labels(3),
        lambda: physical_shell_controls("line", TRAIN_LENGTH, labels, sparse.eye(len(labels))),
        lambda: physical_shell_controls("path", 4, labels, sparse.eye(len(labels))),
        lambda: c522.selected_carriers(2, (0,)),
    ):
        try:
            operation()
        except (ValueError, KeyError):
            rejects += 1
    determinant_minus_one = np.diag((-1, 1, 1))
    lawful_frames = c319.c235.proper_cubic_frames()
    reflection_rejected = not any(
        np.array_equal(determinant_minus_one, frame) for frame in lawful_frames
    )
    return {
        "explicit_rejections": rejects,
        "reflection_rejected": reflection_rejected,
        "L5_train_L6_held_only": True,
        "global_number_cutoff": MAX_TOTAL_NUMBER,
        "pass": rejects == 5 and reflection_rejected,
    }


def dry_contract() -> dict:
    upstream = semantic_upstream_contract()
    note = note_contract()
    labels = triple_labels()
    four_labels = c324.four_cell_labels()
    sectors = {
        number: sum(
            label[0] + label[2] + label[4] == number for label in labels
        )
        for number in range(MAX_TOTAL_NUMBER + 1)
    }
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "upstream": upstream,
        "note": note,
        "logical_columns": len(labels),
        "sector_dimensions": sectors,
        "four_cell_star_columns": len(four_labels),
        "pass": upstream["pass"]
        and note["pass"]
        and len(labels) == 988
        and len(four_labels) == 301
        and sectors == {0: 1, 1: 18, 2: 153, 3: 816},
    }


def certificate() -> dict:
    started = time.monotonic()
    checkpoints = []
    labels = triple_labels()
    dry = dry_contract()
    check("semantic and note contracts", dry["pass"], dry)

    role = c319.role_gauge_controls(len(labels))
    check("joint S3 replaces incompatible independent edge roles", role_gauge_pass(role), role)
    checkpoints.append(checkpoint(started, "role-algebra"))

    local_frames = local_selected_frame_controls()
    check("selected local physical code is covariant in all 24 frames", local_frames["pass"], local_frames)
    checkpoints.append(checkpoint(started, "local-frames"))

    updates, operators = update_and_frame_controls(labels)
    for kind in c319.GEOMETRIES:
        check(
            f"{kind} two-seam logical update, both orders, frames, mass, and slot",
            update_pass(updates[kind]),
            updates[kind],
        )
    checkpoints.append(checkpoint(started, "logical-updates"))

    shells = {}
    for kind in c319.GEOMETRIES:
        shells[kind] = {}
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            shell = physical_shell_controls(
                kind,
                length,
                labels,
                operators[kind]["forward"],
            )
            shells[kind][str(length)] = shell
            check(
                f"{kind} L{length} actual joint selected physical recurrence",
                shell_pass(shell),
                shell,
            )
            checkpoints.append(checkpoint(started, f"{kind}-L{length}"))

    four_labels = c324.four_cell_labels()
    star_update, star_operator = four_cell_star_update_controls(four_labels)
    check(
        "selected four-cell three-seam update, joint S4, frames, and three-slot",
        four_cell_update_pass(star_update),
        star_update,
    )
    star_shells = {}
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        shell = four_cell_star_shell(length, four_labels, star_operator)
        star_shells[str(length)] = shell
        check(
            f"star L{length} actual joint selected three-seam recurrence",
            four_cell_shell_pass(shell),
            shell,
        )
        checkpoints.append(checkpoint(started, f"star-L{length}"))

    deletion = deletion_controls(labels)
    deletion_pass = (
        abs(deletion["minimum_deleted_middle_cell_role_Gram_residual"] - 0.5)
        < TOLERANCE
        and all(
            abs(value - 0.5) < TOLERANCE
            for value in deletion["deleted_middle_cell_role_Gram_residuals"]
        )
    )
    check("middle-cell role deletion is detected", deletion_pass, deletion)

    domain = domain_controls(labels)
    check("lawful domain rejects widened or malformed inputs", domain["pass"], domain)
    checkpoints.append(checkpoint(started, "deletions-domain"))

    supplied = (
        "fixed-Wilson reference and face/port dictionary",
        "Cycle-311 cell flag, cell companion, and preparation",
        "Cycle-522 opposite-carrier selector and normalization",
        "three addressed cells in a path or corner",
        "global n<=3 cutoff",
        "six-state joint S3 role encoded in three M2 and its preparation",
        "24-state joint S4 role encoded in five M2 and its preparation",
        "rebuilt dense code-space coefficients and off-code identity completion",
        "Cycle-219 beta=-0.3 coin and Cycle-230 g=0.37 contact",
        "coin then two sequential seam streams then contact",
        "L5/L6 periodic patches, reference preparation, and schedule",
    )
    not_claimed = (
        "primitive synthesis of the rebuilt dense operations",
        "physical phase controller or autonomous edge selection",
        "causal time, duration, rate, or physical energy",
        "overlapping S4 registers or recurrent volume",
        "three-cell sectors n=4..18, four-cell sectors n=3..24, or number-changing dynamics",
        "Records, Born probability, source/stress, gravity, or continuum limit",
        "minimality or uniqueness of the selector or role register",
        "global Jordan-Wigner order or nonlocal parity service",
        "axiom pressure",
    )

    final_resource = checkpoint(started, "complete")
    result = {
        "cycle": 525,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "revision": REVISION,
        "result": "bounded opposite-carrier two- and three-seam shared-cell algebraic recurrence",
        "dry_contract": dry,
        "joint_role_algebra": role,
        "local_physical_frames": local_frames,
        "updates": updates,
        "physical_shells": shells,
        "three_seam_star_update": star_update,
        "three_seam_star_shells": star_shells,
        "deletions": deletion,
        "domain": domain,
        "resources": checkpoints + [final_resource],
        "supplied": supplied,
        "not_claimed": not_claimed,
        "gate_summary": {"PASS": PASS, "FAIL": FAIL},
        "pass": FAIL == 0,
    }
    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode", choices=("dry-contract", "certificate"), default="certificate"
    )
    args = parser.parse_args()
    if args.mode == "dry-contract":
        result = dry_contract()
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
        return 0 if result["pass"] else 1

    previous = signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(int(WALL_LIMIT_SECONDS))
    try:
        result = certificate()
        return 0 if result["pass"] else 1
    except ResourceWall as error:
        print(json.dumps({"resource_wall": str(error), "pass": False}, indent=2))
        return 2
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous)


if __name__ == "__main__":
    raise SystemExit(main())
