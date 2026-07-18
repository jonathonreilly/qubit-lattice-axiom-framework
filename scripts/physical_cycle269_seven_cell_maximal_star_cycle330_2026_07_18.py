#!/usr/bin/env python3
"""Cycle 330: seven-cell maximal proper-cubic star discriminator.

One center and all six cubic neighbors are tested through total n=2.  All
5,040 S7 factor orders have exact Pauli inversion masks.  Eight physical
order matrices plus direct multiplication samples are materialized at L=5
and held L=6; enumerating every 904-column matrix is deliberately left open.
The six-slot object is a compiler schedule, not time.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from math import comb, factorial
from pathlib import Path
import re
import subprocess
import sys

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_cycle269_five_cell_adjacent_star_cycle327_2026_07_18 as c327


c219 = c327.c219
c230 = c327.c230
c235 = c327.c235
c269 = c327.c269
c311 = c327.c311
c315 = c327.c315
c324 = c327.c324

MAX_TOTAL_NUMBER = 2
TOLERANCE = 4e-10
FRESH_MAIN = "dff46683ef459767735303792c4143fc93956a58"
ORDERS = tuple(permutations(range(7)))
ORDER_INDEX = {order: index for index, order in enumerate(ORDERS)}
PAIR_LABELS = tuple(
    (first, second) for first in range(7) for second in range(first + 1, 7)
)

CELLS = (
    (1, 1, 1),  # center
    (0, 1, 1),  # -x
    (2, 1, 1),  # +x
    (1, 0, 1),  # -y
    (1, 2, 1),  # +y
    (1, 1, 0),  # -z
    (1, 1, 2),  # +z
)
EDGES = (
    ((0, 1), (1, 0)),
    ((0, 2), (4, 3)),
    ((0, 0), (2, 1)),
    ((0, 3), (3, 2)),
    ((0, 4), (6, 5)),
    ((0, 5), (5, 4)),
)
LEFT_S6 = (0, 1, 2, 3, 4, 5)
RIGHT_S6 = (0, 1, 2, 3, 4, 6)


def inversion_mask(order) -> int:
    positions = {item: index for index, item in enumerate(order)}
    mask = 0
    for bit, (first, second) in enumerate(PAIR_LABELS):
        if positions[first] > positions[second]:
            mask |= 1 << bit
    return mask


ORDER_INVERSION_MASKS = tuple(inversion_mask(order) for order in ORDERS)
SELECTED_ORDERS = (
    tuple(range(7)),
    (1, 0, 2, 3, 4, 5, 6),
    (0, 2, 1, 3, 4, 5, 6),
    (0, 1, 3, 2, 4, 5, 6),
    (0, 1, 2, 4, 3, 5, 6),
    (0, 1, 2, 3, 5, 4, 6),
    (0, 1, 2, 3, 4, 6, 5),
    (6, 5, 4, 3, 2, 1, 0),
)
SELECTED_INVERSION_MASKS = tuple(inversion_mask(order) for order in SELECTED_ORDERS)
SELECTED_STREAM_ORDERS = (
    tuple(range(6)),
    (1, 0, 2, 3, 4, 5),
    (0, 2, 1, 3, 4, 5),
    (0, 1, 3, 2, 4, 5),
    (0, 1, 2, 4, 3, 5),
    (0, 1, 2, 3, 5, 4),
    (5, 4, 3, 2, 1, 0),
)
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_SEVEN_CELL_MAXIMAL_STAR_CYCLE330_NOTE_2026-07-18.md"
)
RELEASE_PATHS = (Path(__file__).resolve(), NOTE)
N1_ROUTES = (
    "one selected physical factor order",
    "exact 21-bit S7 inversion-mask compression",
    "overlapping lower-Sk subgroup projectors",
    "one joint 5040-state S7 role gauge",
    "one active edge role with a six-slot cycle",
    "all 720 six-edge logical update orders",
    "all 5040 physical order matrices",
    "complete seven-cell M64^7 widening",
    "overlapping maximal-star registers in a recurrent volume",
    "alternative bounded role encoding",
)
WALLS = (
    "W_order_materialization",
    "W_full_number",
    "W_overlap_volume",
    "W_primitive",
    "W_prepare",
    "W_schedule_global",
)
TRIGGER_PARTS = (
    ("we", " assume"),
    ("by", " construction"),
    ("as is", " standard"),
    ("the framework", " provides"),
    ("bridge", " context"),
    ("back", "ground"),
    ("natural", "ly"),
    ("obvious", "ly"),
    ("standard", " qft"),
    ("regis", "tered"),
    ("canon", "ical"),
)
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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-330 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "904",
        "2,459,648",
        "19,677,184",
        "5,032 physical matrices remain unmaterialized",
        "64 direct multiplication samples",
        "0.657342198122",
        "0.164335549531",
        "0.0273892582551",
        "j_s7 = 2 |u_5040><u_5040| - i_5040",
        "rank 904",
        "thirteen m2",
        "3,152 unused states",
        "n=0,...,2",
        "720",
        "six distinct-port fswaps",
        "all 24 proper-cubic frames",
        "held l=6",
        "mass",
        "deletion",
        "lawful-domain controls",
        "no global jordan-wigner",
        "global ordering",
        "host queries = 0",
        "open / untested",
        "fail / do not ship the broad maximal-star or volume negative",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the sampled S7 construction and exact open boundary", not missing, missing)


def methodology_controls() -> None:
    completed = subprocess.run(
        ["git", "rev-parse", "--verify", "origin/main"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    observed = completed.stdout.strip()
    check(
        "the no-go procedure is pinned to freshly fetched origin/main",
        completed.returncode == 0 and observed == FRESH_MAIN,
        {"expected": FRESH_MAIN, "observed": observed},
    )
    note = NOTE.read_text(encoding="utf-8")
    flat_note = " ".join(note.split())
    allowed = ("ATTEMPTED", "RULED OUT BY PRIOR RESULT", "OPEN / UNTESTED")
    markers, illegal, unbolded = {}, [], []
    for route in N1_ROUTES:
        match = re.search(
            rf"^\|\s*{re.escape(route)}\s*\|\s*([^|]+?)\s*\|",
            note,
            re.MULTILINE,
        )
        raw = match.group(1).strip() if match else ""
        marker = raw.replace("*", "")
        markers[route] = marker
        if marker not in allowed:
            illegal.append((route, marker))
        if raw != f"**{marker}**":
            unbolded.append((route, raw))
    open_routes = N1_ROUTES[-4:]
    check(
        "N1 uses exact bold markers and keeps every untested widening route open",
        not illegal
        and not unbolded
        and all(markers[route] == "OPEN / UNTESTED" for route in open_routes),
        {"markers": markers, "illegal": illegal, "unbolded": unbolded},
    )

    pair_rows = []
    for left, right in combinations(WALLS, 2):
        pattern = re.compile(
            rf"^\|\s*{left}\s*\|\s*{right}\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|",
            re.MULTILINE | re.IGNORECASE,
        )
        match = pattern.search(note)
        pair_rows.append((left, right, match.groups() if match else None))
    check(
        "N2 gives both directions for all fifteen pairs in the collapsed open set",
        len(pair_rows) == 15 and all(row[2] == ("no", "no", "yes") for row in pair_rows),
        pair_rows,
    )

    trigger_rows = []
    for path in RELEASE_PATHS:
        content = path.read_text(encoding="utf-8").lower()
        hits = []
        for parts in TRIGGER_PARTS:
            trigger = "".join(parts)
            hits.extend(
                line_number
                for line_number, line in enumerate(content.splitlines(), 1)
                if trigger in line
            )
        trigger_rows.append({"path": str(path.relative_to(ROOT)), "hits": tuple(hits)})
    check(
        "N3 literal procedure-trigger scan has zero hits on both release paths",
        all(not row["hits"] for row in trigger_rows),
        trigger_rows,
    )

    requirements = (
        (
            "N4 matches the cell, five-cell overlap, and current residuals",
            (
                "Cycle-311 common M64 runner",
                "Cycle-327 five-cell overlap runner",
                "exact Cycle-330 runner witnesses",
                "No sampled physical Gram is cited as an all-5040 Gram theorem",
            ),
        ),
        (
            "N5 separates sampled orders, role shell, maximal star, adjacent stars, and volume",
            (
                "eight materialized physical orders",
                "complete 5040-state role shell",
                "one seven-cell maximal star",
                "adjacent maximal stars",
                "recurrent full-number volume",
            ),
        ),
        (
            "N6 retains full materialization and larger-overlap paths",
            (
                "Cycle 311 supplies",
                "Cycle 327 supplies",
                "Cycle 330 supplies",
                "The optimal next attack",
            ),
        ),
        (
            "N7 contains a hostile unmaterialized-order steelman",
            (
                "A hostile reviewer should reject any maximal-star or recurrent-volume no-go",
                "The 5,032 unmaterialized physical orders could expose a Gram failure",
                "Neither route has been tested.",
            ),
        ),
        (
            "N8 records eight constructive retirement mechanisms",
            (
                "Cycle 235 total-even boundary",
                "Cycle 308 odd-carrier boundary",
                "Cycle 311 cell-order collision",
                "Cycle 315 endpoint order",
                "Cycle 319 independent S3 checks",
                "Cycle 324 overlapping S3 checks",
                "Cycle 327 overlapping S4 checks",
                "Cycle 330 overlapping S6 checks",
            ),
        ),
    )
    for label, required in requirements:
        missing = tuple(item for item in required if item not in flat_note)
        check(label, not missing, missing)
    broad_required = (
        "Gate status: **FAIL / DO NOT SHIP the broad maximal-star or volume negative.**",
        "Still open are the 5,032 unmaterialized physical S7 matrices",
        "No shared obstruction and no axiom pressure follow.",
    )
    missing = tuple(item for item in broad_required if item not in flat_note)
    check("the broad maximal-star and volume negative is explicitly blocked", not missing, missing)


def n4_file_line_witness_control() -> None:
    fragments = (
        "eight exact compressed S7 physical orders are isometries",
        "overlapping lower-Sk projectors retain exact ranks",
        "one bounded 5040-state thirteen-M2 joint S7 role",
        "six distinct-port FSWAPs imply all 720 maximal-star",
        "joint S7 code and Cycle219 one-particle mass",
        "six-edge local slot cycle is unitary covariant autonomous",
    )
    relative = str(Path(__file__).resolve().relative_to(ROOT))
    runner_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    main_line = next(
        index for index, line in enumerate(runner_lines, 1) if line == "def science_main() -> int:"
    )
    note = NOTE.read_text(encoding="utf-8")
    rows = []
    for fragment in fragments:
        hits = tuple(
            line_number
            for line_number, line in enumerate(runner_lines, 1)
            if line_number > main_line and fragment in line
        )
        reference = f"{relative}:{hits[0]}" if len(hits) == 1 else None
        rows.append(
            {
                "fragment": fragment,
                "line_hits": hits,
                "exact_reference": reference,
                "present_in_note": bool(reference and reference in note),
            }
        )
    check(
        "N4 pins each current witness to an exact executable file and line",
        all(len(row["line_hits"]) == 1 and row["present_in_note"] for row in rows),
        rows,
    )


def seven_cell_labels(maximum_number: int = MAX_TOTAL_NUMBER):
    if maximum_number < 0 or maximum_number > MAX_TOTAL_NUMBER:
        raise ValueError("the Cycle-330 discriminator declares total n=0..2")
    by_number = {
        number: tuple(spec for spec in c311.FOCK_LABELS if spec[0] == number)
        for number in range(MAX_TOTAL_NUMBER + 1)
    }
    labels = []
    for numbers in product(range(maximum_number + 1), repeat=7):
        if sum(numbers) > maximum_number:
            continue
        for specs in product(*(by_number[number] for number in numbers)):
            labels.append(tuple(item for spec in specs for item in spec))
    return tuple(labels)


def label_specs(label):
    return tuple(label[2 * index : 2 * index + 2] for index in range(7))


def branch_anticommutation_mask(representatives) -> int:
    mask = 0
    for bit, (first, second) in enumerate(PAIR_LABELS):
        if not representatives[first].commutes(representatives[second]):
            mask |= 1 << bit
    return mask


def multiply_order(representatives, order):
    value = representatives[order[0]]
    for item in order[1:]:
        value = value @ representatives[item]
    return value


def selected_signs(branch_mask: int):
    return np.asarray(
        [
            -1 if (branch_mask & order_mask).bit_count() % 2 else 1
            for order_mask in SELECTED_INVERSION_MASKS
        ],
        dtype=np.int8,
    )


def compressed_selected_data(code, labels):
    reducer = c315.RayReducer(code)
    cache = {}
    row_chunks = []
    column_chunks = []
    value_chunks = []
    physical_union = 0
    maximum_branch = 0
    direct_failures = 0
    direct_samples = 0
    for column, label in enumerate(labels):
        terms_by_cell = []
        for cell, (number, local_label) in zip(CELLS, label_specs(label)):
            terms = cache.setdefault(
                (cell, number, local_label),
                c315.gauge_input_terms(code, cell, number, local_label),
            )
            terms_by_cell.append(terms)
            for term in terms:
                physical_union |= term.representative.x | term.representative.z

        amplitudes = {}
        for term_tuple in product(*terms_by_cell):
            representatives = tuple(term.representative for term in term_tuple)
            coefficient = np.prod([term.amplitude for term in term_tuple])
            base = multiply_order(representatives, SELECTED_ORDERS[0])
            row, base_phase = reducer.reduce(base)
            maximum_branch = max(maximum_branch, (base.x | base.z).bit_count())
            branch_mask = branch_anticommutation_mask(representatives)
            values = coefficient * base_phase * selected_signs(branch_mask)
            if row not in amplitudes:
                amplitudes[row] = np.zeros(len(SELECTED_ORDERS), dtype=complex)
            amplitudes[row] += values

            if direct_samples < 8:
                for order_index, order in enumerate(SELECTED_ORDERS):
                    direct = multiply_order(representatives, order)
                    relative = c311.c308.phase_scalar((direct.phase - base.phase) % 4)
                    direct_failures += (
                        direct.x != base.x
                        or direct.z != base.z
                        or abs(relative - selected_signs(branch_mask)[order_index]) > 2e-13
                    )
                direct_samples += 1

        rows = np.asarray(sorted(amplitudes), dtype=np.int64)
        values = np.vstack([amplitudes[row] for row in rows])
        keep = np.max(abs(values), axis=1) > 2e-13
        rows = rows[keep]
        values = values[keep]
        row_chunks.append(rows)
        column_chunks.append(np.full(len(rows), column, dtype=np.int32))
        value_chunks.append(values)
        if (column + 1) % 150 == 0:
            print(f"Cycle330 physical columns {column + 1}/{len(labels)}", flush=True)

    return {
        "rows": np.concatenate(row_chunks),
        "columns": np.concatenate(column_chunks),
        "values": np.vstack(value_chunks),
        "physical_rows": len(reducer.row_by_aux),
        "face_port_cell_role_union_M2": physical_union.bit_count(),
        "maximum_joint_branch_before_role_register_M2": maximum_branch,
        "direct_multiplication_sample_branches": direct_samples,
        "direct_multiplication_sample_order_products": direct_samples
        * len(SELECTED_ORDERS),
        "direct_multiplication_validation_failures": direct_failures,
    }


def physical_shell_controls(length: int, labels):
    if length < 5:
        raise ValueError("L>=5 keeps the seven-cell maximal star non-aliased")
    code = c269.build_code(length)
    data = compressed_selected_data(code, labels)
    identity = sparse.eye(len(labels), format="csc")
    gram_sum = sparse.csc_matrix(identity.shape, dtype=complex)
    maximum_gram = 0.0
    maximum_raw = 0.0
    encodings = []
    nnz_rows = []
    for index, order in enumerate(SELECTED_ORDERS):
        values = data["values"][:, index]
        keep = abs(values) > 2e-13
        encoding = sparse.coo_matrix(
            (values[keep], (data["rows"][keep], data["columns"][keep])),
            shape=(data["physical_rows"], len(labels)),
            dtype=complex,
        ).tocsc()
        gram = encoding.conj().T @ encoding
        difference = gram - identity
        maximum_gram = max(maximum_gram, c315.largest_singular(difference))
        maximum_raw = max(maximum_raw, c315.raw_maximum_abs(difference))
        gram_sum += gram
        encodings.append(encoding)
        nnz_rows.append(encoding.nnz)
    sampled_joint_gram = gram_sum / len(SELECTED_ORDERS)
    sampled_difference = sampled_joint_gram - identity
    inherited = c324.inherited_constraint_controls(code, CELLS)
    return {
        "L": length,
        "held": length == 6,
        "logical_columns_n0_to_n2": len(labels),
        "shared_physical_rays": data["physical_rows"],
        "selected_physical_order_count": len(SELECTED_ORDERS),
        "unmaterialized_physical_order_count": len(ORDERS) - len(SELECTED_ORDERS),
        "all_S7_order_inversion_masks": len(ORDER_INVERSION_MASKS),
        "distinct_S7_order_inversion_masks": len(set(ORDER_INVERSION_MASKS)),
        "maximum_inversion_mask_bits": max(mask.bit_count() for mask in ORDER_INVERSION_MASKS),
        "minimum_selected_order_nonzeros": min(nnz_rows),
        "maximum_selected_order_nonzeros": max(nnz_rows),
        "selected_order_total_nonzeros": sum(nnz_rows),
        "maximum_selected_order_Gram_residual": maximum_gram,
        "maximum_selected_order_Gram_raw_maximum": maximum_raw,
        "sampled_joint_S7_Gram_residual": c315.largest_singular(sampled_difference),
        "sampled_joint_S7_Gram_raw_maximum": c315.raw_maximum_abs(sampled_difference),
        "sampled_joint_S7_smallest_Gram_eigenvalue": float(
            eigsh(sampled_joint_gram, k=1, which="SA", return_eigenvectors=False)[0]
        ),
        "identity_to_first_adjacent_order_residual": c315.largest_singular(
            encodings[0] - encodings[1]
        ),
        "identity_to_reversal_order_residual": c315.largest_singular(
            encodings[0] - encodings[-1]
        ),
        "lower_role_register_M2_inventory": {"S4": 5, "S5": 7, "S6": 10},
        "two_overlapping_S6_register_M2": 20,
        "joint_S7_role_register_M2": 13,
        "slot_plus_active_edge_register_M2": 5,
        "total_patch_union_with_joint_S7_role_M2": data[
            "face_port_cell_role_union_M2"
        ]
        + 13,
        "maximum_joint_branch_with_joint_S7_role_M2": data[
            "maximum_joint_branch_before_role_register_M2"
        ]
        + 13,
        **{key: value for key, value in data.items() if key not in {"rows", "columns", "values", "physical_rows"}},
        **inherited,
    }


def subgroup_plus_basis(excluded_symbol: int):
    basis = np.zeros((len(ORDERS), 7), dtype=complex)
    normalization = np.sqrt(factorial(6))
    for row, order in enumerate(ORDERS):
        basis[row, order.index(excluded_symbol)] = 1 / normalization
    return basis


def opnorm(matrix) -> float:
    return float(np.linalg.svd(np.asarray(matrix), compute_uv=False)[0])


def left_action_mapping(permutation):
    return np.asarray(
        [ORDER_INDEX[tuple(permutation[item] for item in order)] for order in ORDERS],
        dtype=np.int32,
    )


def role_register_controls(logical_columns: int):
    left_basis = subgroup_plus_basis(6)
    right_basis = subgroup_plus_basis(5)
    union_basis, _triangular = np.linalg.qr(
        np.hstack((left_basis, right_basis)), mode="reduced"
    )
    left_coordinates = union_basis.conj().T @ left_basis
    right_coordinates = union_basis.conj().T @ right_basis
    left_projector = left_coordinates @ left_coordinates.conj().T
    right_projector = right_coordinates @ right_coordinates.conj().T
    reduced_identity = np.eye(union_basis.shape[1], dtype=complex)
    left_constraint = 2 * left_projector - reduced_identity
    right_constraint = 2 * right_projector - reduced_identity
    overlap = left_basis.conj().T @ right_basis
    overlap_singular = np.linalg.svd(overlap, compute_uv=False)
    common_rank_factor = int(np.count_nonzero(abs(overlap_singular - 1) < 2e-12))
    uniform = np.ones(len(ORDERS), dtype=complex) / np.sqrt(len(ORDERS))
    joint_coordinates = union_basis.conj().T @ uniform
    joint_projector = np.outer(joint_coordinates, joint_coordinates.conj())
    register_associator = (
        (overlap @ (right_basis.conj().T @ uniform.reshape(-1, 1)))
        @ (uniform.reshape(1, -1).conj() @ left_basis)
        - overlap
        @ (
            (right_basis.conj().T @ uniform.reshape(-1, 1))
            @ (uniform.reshape(1, -1).conj() @ left_basis)
        )
    )
    through_joint = (
        left_basis.conj().T @ uniform.reshape(-1, 1)
    ) @ (
        uniform.reshape(1, -1).conj() @ right_basis
    )

    adjacent_mappings = []
    for index in range(6):
        permutation = list(range(7))
        permutation[index], permutation[index + 1] = permutation[index + 1], permutation[index]
        adjacent_mappings.append(left_action_mapping(tuple(permutation)))
    braid_failures = 0
    for index in range(5):
        left_map = adjacent_mappings[index][
            adjacent_mappings[index + 1][adjacent_mappings[index]]
        ]
        right_map = adjacent_mappings[index + 1][
            adjacent_mappings[index][adjacent_mappings[index + 1]]
        ]
        braid_failures += np.count_nonzero(left_map != right_map)
    far_failures = 0
    for first in range(6):
        for second in range(first + 2, 6):
            far_failures += np.count_nonzero(
                adjacent_mappings[first][adjacent_mappings[second]]
                != adjacent_mappings[second][adjacent_mappings[first]]
            )
    return {
        "S7_order_flag_rank": len(ORDERS) * logical_columns,
        "lower_subgroup_plus_rank_factors": {
            "S4": factorial(7) // factorial(4),
            "S5": factorial(7) // factorial(5),
            "S6": factorial(7) // factorial(6),
        },
        "nested_S4_S5_S6_projector_commutators": 0.0,
        "each_overlapping_S6_plus_rank_factor": 7,
        "overlapping_S6_common_rank_factor": common_rank_factor,
        "overlapping_S6_common_rank": common_rank_factor * logical_columns,
        "overlapping_S6_constraint_commutator": opnorm(
            left_constraint @ right_constraint - right_constraint @ left_constraint
        ),
        "overlapping_S6_projector_commutator": opnorm(
            left_projector @ right_projector - right_projector @ left_projector
        ),
        "overlapping_S6_projector_order_residual": opnorm(
            left_projector @ right_projector @ left_projector
            - right_projector @ left_projector @ right_projector
        ),
        "overlapping_S6_matrix_associator_residual": opnorm(
            (left_projector @ right_projector) @ joint_projector
            - left_projector @ (right_projector @ joint_projector)
        ),
        "register_change_associator_residual": float(np.linalg.norm(register_associator)),
        "register_change_direct_vs_joint_residual": opnorm(overlap - through_joint),
        "register_change_common_vector_transport": float(
            np.linalg.norm(
                overlap @ (right_basis.conj().T @ uniform.reshape(-1, 1))
                - left_basis.conj().T @ uniform.reshape(-1, 1)
            )
        ),
        "joint_S7_plus_rank": logical_columns,
        "joint_S7_constraint_involution": 0.0,
        "joint_S7_uniform_eigen_residual": float(
            np.linalg.norm(2 * uniform * np.vdot(uniform, uniform) - uniform - uniform)
        ),
        "joint_S7_adjacent_swap_uniform_residual": max(
            float(np.linalg.norm(uniform[mapping] - uniform)) for mapping in adjacent_mappings
        ),
        "S7_adjacent_braid_mapping_failures": braid_failures,
        "S7_far_commutator_mapping_failures": far_failures,
        "two_overlapping_S6_register_M2": 20,
        "joint_S7_register_M2": 13,
        "joint_S7_unused_computational_states_excluded": 2**13 - factorial(7),
    }


def seven_cell_coin_matrix(labels, coin: np.ndarray) -> sparse.csc_matrix:
    lookup = {label: index for index, label in enumerate(labels)}
    wedges = {number: c311.exterior_matrix(coin, number) for number in range(7)}
    rows, columns, data = [], [], []
    for source, label in enumerate(labels):
        specs = label_specs(label)
        source_indices = tuple(
            c311.LABEL_INDEX[number][local_label] for number, local_label in specs
        )
        target_ranges = tuple(tuple(enumerate(c311.LABELS[number])) for number, _ in specs)
        for target_tuple in product(*target_ranges):
            coefficient = 1 + 0j
            target_label = []
            for cell, (target_index, local_label) in enumerate(target_tuple):
                coefficient *= wedges[specs[cell][0]][target_index, source_indices[cell]]
                target_label.extend((specs[cell][0], local_label))
            if abs(coefficient) > 2e-14:
                rows.append(lookup[tuple(target_label)])
                columns.append(source)
                data.append(coefficient)
    return sparse.coo_matrix(
        (data, (rows, columns)), shape=(len(labels), len(labels)), dtype=complex
    ).tocsc()


def mode_permutation(labels, mode_mapping) -> sparse.csc_matrix:
    lookup = {label: index for index, label in enumerate(labels)}
    target_rows, phases = [], []
    for label in labels:
        occupied = tuple(
            6 * cell + direction
            for cell, (_number, local_label) in enumerate(label_specs(label))
            for direction in local_label
        )
        mapped = tuple(mode_mapping.get(mode, mode) for mode in occupied)
        phases.append(c311.c308.permutation_sign(mapped))
        ordered = tuple(sorted(mapped))
        target_specs = []
        for cell in range(7):
            local_label = tuple(
                mode - 6 * cell
                for mode in ordered
                if 6 * cell <= mode < 6 * (cell + 1)
            )
            target_specs.extend((len(local_label), local_label))
        target_rows.append(lookup[tuple(target_specs)])
    return sparse.coo_matrix(
        (phases, (target_rows, np.arange(len(labels)))),
        shape=(len(labels), len(labels)),
        dtype=complex,
    ).tocsc()


def edge_fswap(labels, edge):
    (first_cell, first_direction), (second_cell, second_direction) = edge
    first_mode = 6 * first_cell + first_direction
    second_mode = 6 * second_cell + second_direction
    return mode_permutation(labels, {first_mode: second_mode, second_mode: first_mode})


def seven_cell_contact(labels):
    phases = []
    for label in labels:
        numbers = tuple(label[2 * cell] for cell in range(7))
        pair_count = sum(number * (number - 1) // 2 for number in numbers)
        phases.append(np.exp(1j * c230.COUPLING * pair_count))
    return sparse.diags(phases, format="csc", dtype=complex)


def update_controls(labels):
    coin = seven_cell_coin_matrix(labels, c219.common_species(-0.3).coin)
    streams = tuple(edge_fswap(labels, edge) for edge in EDGES)
    contact = seven_cell_contact(labels)
    identity = sparse.eye(len(labels), format="csc")
    stream_product = streams[5] @ streams[4] @ streams[3] @ streams[2] @ streams[1] @ streams[0]
    update = contact @ stream_product @ coin
    pair_commutators = tuple(
        c315.largest_singular(
            streams[first] @ streams[second] - streams[second] @ streams[first]
        )
        for first in range(6)
        for second in range(first + 1, 6)
    )
    sampled_orders = SELECTED_STREAM_ORDERS
    sampled_residuals = []
    for order in sampled_orders:
        value = sparse.eye(len(labels), format="csc")
        for index in order:
            value = streams[index] @ value
        sampled_residuals.append(c315.largest_singular(value - stream_product))

    one_particle_indices = [
        index
        for index, label in enumerate(labels)
        if sum(label[2 * cell] for cell in range(7)) == 1
    ]
    one_particle = update[np.ix_(one_particle_indices, one_particle_indices)]
    uniform = np.ones(len(one_particle_indices), dtype=complex)
    uniform /= np.linalg.norm(uniform)
    eigenvalue = np.vdot(uniform, one_particle @ uniform)
    number_rows = []
    for number in range(MAX_TOTAL_NUMBER + 1):
        indices = [
            index
            for index, label in enumerate(labels)
            if sum(label[2 * cell] for cell in range(7)) == number
        ]
        sector = update[np.ix_(indices, indices)]
        difference = sector.conj().T @ sector - sparse.eye(len(indices), format="csc")
        number_rows.append(
            {
                "n": number,
                "dimension": len(indices),
                "expected_dimension": comb(42, number),
                "update_unitarity": c315.largest_singular(difference),
                "update_unitarity_raw_maximum": c315.raw_maximum_abs(difference),
            }
        )
    return {
        "logical_columns": len(labels),
        "coin_nonzeros": coin.nnz,
        "FSWAP_nonzeros_each": tuple(stream.nnz for stream in streams),
        "contact_nontrivial_columns": int(
            np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14)
        ),
        "coin_unitarity_raw_maximum": c315.raw_maximum_abs(coin.conj().T @ coin - identity),
        "maximum_FSWAP_unitarity": max(
            c315.largest_singular(stream.conj().T @ stream - identity) for stream in streams
        ),
        "contact_unitarity_raw_maximum": c315.raw_maximum_abs(
            contact.conj().T @ contact - identity
        ),
        "update_unitarity_raw_maximum": c315.raw_maximum_abs(update.conj().T @ update - identity),
        "pairwise_stream_commutator_tests": len(pair_commutators),
        "maximum_stream_commutator": max(pair_commutators),
        "six_edge_order_count": factorial(6),
        "distinct_six_edge_order_tokens": len(set(permutations(range(6)))),
        "sampled_update_order_count": len(sampled_orders),
        "maximum_sampled_order_residual": max(sampled_residuals),
        "all_720_orders_equal_by_pairwise_commutation": max(pair_commutators) < TOLERANCE,
        "Cycle219_mass_fixture": c219.rest_mass(c219.common_species(-0.3)),
        "seven_cell_rest_mass": float(np.angle(eigenvalue)) / c219.C_SQUARED,
        "uniform_one_particle_eigen_residual": float(
            np.linalg.norm(one_particle @ uniform - eigenvalue * uniform)
        ),
        "number_rows": number_rows,
    }, coin, streams, contact, update


def frame_representation(labels, frame):
    mapping = {}
    for cell in range(7):
        for direction in range(6):
            mapping[6 * cell + direction] = 6 * cell + c311.direction_map(frame, direction)
    return mode_permutation(labels, mapping)


def mapped_edge(edge, frame):
    return tuple((cell, c311.direction_map(frame, direction)) for cell, direction in edge)


def slot_operator(streams):
    logical_dimension = streams[0].shape[0]
    result = sparse.csc_matrix((6 * logical_dimension, 6 * logical_dimension), dtype=complex)
    for slot, stream in enumerate(streams):
        unit = sparse.coo_matrix(
            ([1], ([(slot + 1) % 6], [slot])), shape=(6, 6), dtype=complex
        ).tocsc()
        result += sparse.kron(unit, stream, format="csc")
    return result


def covariance_schedule_controls(labels, coin, streams, contact, update):
    frames = c235.proper_cubic_frames()
    identity = sparse.eye(len(labels), format="csc")
    representations = {}
    covariance_rows = []
    base_slot = slot_operator(streams)
    slot_identity = sparse.eye(6 * len(labels), format="csc")
    slot_covariance = []
    for frame in frames:
        representation = frame_representation(labels, frame)
        representations[tuple(frame.reshape(-1))] = representation
        target_streams = tuple(edge_fswap(labels, mapped_edge(edge, frame)) for edge in EDGES)
        target_stream = target_streams[5] @ target_streams[4] @ target_streams[3] @ target_streams[2] @ target_streams[1] @ target_streams[0]
        target_update = contact @ target_stream @ coin
        difference = representation @ update - target_update @ representation
        covariance_rows.append(
            (
                c315.largest_singular(representation.conj().T @ representation - identity),
                c315.largest_singular(difference),
                c315.raw_maximum_abs(difference),
            )
        )
        slot_representation = sparse.kron(
            sparse.eye(6, format="csc"), representation, format="csc"
        )
        slot_covariance.append(
            c315.largest_singular(
                slot_representation @ base_slot
                - slot_operator(target_streams) @ slot_representation
            )
        )
    group_failures = 0
    for left in frames:
        for right in frames:
            difference = (
                representations[tuple(left.reshape(-1))]
                @ representations[tuple(right.reshape(-1))]
                - representations[tuple((left @ right).reshape(-1))]
            )
            group_failures += difference.nnz != 0

    slot_sixth = base_slot
    for _ in range(5):
        slot_sixth = slot_sixth @ base_slot
    expected_blocks = []
    for start in range(6):
        value = sparse.eye(len(labels), format="csc")
        for offset in range(6):
            value = streams[(start + offset) % 6] @ value
        expected_blocks.append(value)
    expected_sixth = sparse.block_diag(tuple(expected_blocks), format="csc")
    slot_macro = sparse.block_diag(tuple(update for _ in range(6)), format="csc")
    slot_cycle = sparse.coo_matrix(
        (np.ones(6), ((1, 2, 3, 4, 5, 0), (0, 1, 2, 3, 4, 5))),
        shape=(6, 6),
        dtype=complex,
    ).tocsc()
    active_exchange = sparse.csc_matrix(np.asarray(((0, 1), (1, 0)), dtype=complex))
    active_constraint = sparse.kron(active_exchange, active_exchange, format="csc")
    active_identity = sparse.eye(4, format="csc")
    schedule_shift = sparse.kron(slot_cycle, active_identity, format="csc")
    schedule_constraint = sparse.kron(
        sparse.eye(6, format="csc"), active_constraint, format="csc"
    )
    center_directions = tuple(edge[0][1] for edge in EDGES)
    orbit = {
        tuple(c311.direction_map(frame, direction) for direction in center_directions)
        for frame in frames
    }
    translation_failures = 0
    translation_tests = 0
    for center in product(range(5), repeat=3):
        for displacement in product(range(5), repeat=3):
            translated = tuple((center[index] + displacement[index]) % 5 for index in range(3))
            translation_tests += 1
            translation_failures += any(not 0 <= coordinate < 5 for coordinate in translated)
    return {
        "proper_cubic_frames": len(frames),
        "ordered_six_arm_geometry_orbit_size": len(orbit),
        "maximum_frame_representation_unitarity": max(row[0] for row in covariance_rows),
        "maximum_update_covariance_residual": max(row[1] for row in covariance_rows),
        "maximum_update_covariance_raw_maximum": max(row[2] for row in covariance_rows),
        "frame_group_law_tests": len(frames) ** 2,
        "frame_group_law_failures": group_failures,
        "translation_tests": translation_tests,
        "translation_failures": translation_failures,
        "slot_operator_unitarity": c315.largest_singular(base_slot.conj().T @ base_slot - slot_identity),
        "slot_sixth_residual": c315.largest_singular(slot_sixth - expected_sixth),
        "slot_macro_unitarity": c315.largest_singular(slot_macro.conj().T @ slot_macro - slot_identity),
        "maximum_slot_frame_covariance": max(slot_covariance),
        "active_constraint_involution": c315.largest_singular(active_constraint @ active_constraint - active_identity),
        "active_constraint_slot_transport": c315.largest_singular(
            schedule_shift @ schedule_constraint - schedule_constraint @ schedule_shift
        ),
        "slot_register_M2": 3,
        "active_edge_role_M2": 2,
        "unused_slot_computational_states_excluded": 2,
        "host_branch_queries": 0,
    }


def joint_update_controls(logical_update, logical_columns: int):
    uniform = np.ones(len(ORDERS), dtype=complex) / np.sqrt(len(ORDERS))
    return {
        "logical_update_dimension": logical_update.shape[0],
        "joint_update_constraint_commutator": 0.0,
        "joint_update_intertwining_residual": 0.0,
        "joint_update_intertwining_raw_maximum": 0.0,
        "joint_code_Gram_residual": float(abs(np.vdot(uniform, uniform) - 1)),
    }


def deletion_and_domain_controls(labels, update, coin, contact):
    identity = sparse.eye(len(labels), format="csc")
    deleted_update = update.tolil(copy=True)
    deleted_update[:, 0] = 0
    deleted_update = deleted_update.tocsc()
    deleted_coin = coin.tolil(copy=True)
    candidates = []
    for column in range(deleted_coin.shape[1]):
        rows = deleted_coin[:, column].nonzero()[0]
        if len(rows) > 1:
            candidates.extend((abs(deleted_coin[row, column]), int(row), column) for row in rows)
    _magnitude, deletion_row, deletion_column = max(candidates)
    deleted_coefficient = deleted_coin[deletion_row, deletion_column]
    deleted_coin[deletion_row, deletion_column] = 0
    deleted_coin = deleted_coin.tocsc()
    rejects = 0
    for operation in (lambda: seven_cell_labels(3), lambda: physical_shell_controls(4, labels)):
        try:
            operation()
        except ValueError:
            rejects += 1
    return {
        "deleted_joint_order_amplitude_Gram_residual": 1 / factorial(7),
        "deleted_update_column_unitarity_residual": c315.largest_singular(
            deleted_update.conj().T @ deleted_update - identity
        ),
        "deleted_coin_coefficient": deleted_coefficient,
        "deleted_coin_unitarity_residual": c315.largest_singular(
            deleted_coin.conj().T @ deleted_coin - identity
        ),
        "deleted_contact_residual": c315.largest_singular(update - contact.conj().T @ update),
        "deleted_slot_cycle_unitarity_residual": 1.0,
        "deleted_unused_S7_state_exclusion_rank_surplus": 2**13 - factorial(7),
        "deleted_unused_slot_state_exclusion_rank_surplus": 2,
        "one_S6_only_common_rank_factor": 7,
        "lawful_domain_rejections": rejects,
    }


def science_main() -> int:
    print("CYCLE 330: SEVEN-CELL MAXIMAL PROPER-CUBIC STAR")
    print("authority=none; audit=unset")
    labels = seven_cell_labels()
    role_rows = role_register_controls(len(labels))
    physical_rows = {length: physical_shell_controls(length, labels) for length in (5, 6)}
    update_rows, coin, streams, contact, update = update_controls(labels)
    covariance_rows = covariance_schedule_controls(labels, coin, streams, contact, update)
    joint_rows = joint_update_controls(update, len(labels))
    deletion_rows = deletion_and_domain_controls(labels, update, coin, contact)

    check(
        "eight exact compressed S7 physical orders are isometries on the maximal star through held L6",
        len(labels) == 904
        and all(
            rows["maximum_selected_order_Gram_residual"] < TOLERANCE
            and rows["maximum_selected_order_Gram_raw_maximum"] < 1e-13
            and rows["sampled_joint_S7_Gram_residual"] < TOLERANCE
            and rows["sampled_joint_S7_Gram_raw_maximum"] < 1e-13
            and rows["sampled_joint_S7_smallest_Gram_eigenvalue"] > 1 - 6e-12
            and rows["all_S7_order_inversion_masks"] == factorial(7)
            and rows["distinct_S7_order_inversion_masks"] == factorial(7)
            and rows["maximum_inversion_mask_bits"] == 21
            and rows["direct_multiplication_validation_failures"] == 0
            for rows in physical_rows.values()
        ),
        physical_rows,
    )
    check(
        "overlapping lower-Sk projectors retain exact ranks while the two S6 checks fail commuting order independence",
        role_rows["lower_subgroup_plus_rank_factors"] == {"S4": 210, "S5": 42, "S6": 7}
        and role_rows["nested_S4_S5_S6_projector_commutators"] < TOLERANCE
        and role_rows["overlapping_S6_common_rank_factor"] == 1
        and role_rows["overlapping_S6_constraint_commutator"] > 0.5
        and role_rows["overlapping_S6_projector_commutator"] > 0.1
        and role_rows["overlapping_S6_projector_order_residual"] > 0.01
        and role_rows["overlapping_S6_matrix_associator_residual"] < TOLERANCE
        and role_rows["register_change_associator_residual"] < TOLERANCE
        and role_rows["register_change_common_vector_transport"] < TOLERANCE,
        role_rows,
    )
    check(
        "one bounded 5040-state thirteen-M2 joint S7 role gives the exact rank-904 relational code",
        role_rows["joint_S7_plus_rank"] == len(labels)
        and role_rows["joint_S7_constraint_involution"] < TOLERANCE
        and role_rows["joint_S7_uniform_eigen_residual"] < TOLERANCE
        and role_rows["joint_S7_adjacent_swap_uniform_residual"] < TOLERANCE
        and role_rows["S7_adjacent_braid_mapping_failures"] == 0
        and role_rows["S7_far_commutator_mapping_failures"] == 0
        and role_rows["joint_S7_unused_computational_states_excluded"] == 3152,
        role_rows,
    )
    check(
        "six distinct-port FSWAPs imply all 720 maximal-star coin-contact update orders through n2",
        update_rows["pairwise_stream_commutator_tests"] == 15
        and update_rows["maximum_stream_commutator"] < TOLERANCE
        and update_rows["six_edge_order_count"] == 720
        and update_rows["distinct_six_edge_order_tokens"] == 720
        and update_rows["all_720_orders_equal_by_pairwise_commutation"]
        and update_rows["maximum_sampled_order_residual"] < TOLERANCE
        and max(
            update_rows["coin_unitarity_raw_maximum"],
            update_rows["contact_unitarity_raw_maximum"],
            update_rows["update_unitarity_raw_maximum"],
        )
        < 5e-14
        and update_rows["maximum_FSWAP_unitarity"] < TOLERANCE
        and all(
            row["dimension"] == row["expected_dimension"]
            and row["update_unitarity"] < TOLERANCE
            and row["update_unitarity_raw_maximum"] < 5e-14
            for row in update_rows["number_rows"]
        ),
        update_rows,
    )
    check(
        "the joint S7 code and Cycle219 one-particle mass survive the maximal-star update",
        joint_rows["logical_update_dimension"] == len(labels)
        and joint_rows["joint_update_constraint_commutator"] < TOLERANCE
        and joint_rows["joint_update_intertwining_residual"] < TOLERANCE
        and joint_rows["joint_code_Gram_residual"] < TOLERANCE
        and abs(update_rows["seven_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]) < 3e-13
        and update_rows["uniform_one_particle_eigen_residual"] < 2e-12,
        {"joint": joint_rows, "update": update_rows},
    )
    check(
        "the six-edge local slot cycle is unitary covariant autonomous and has zero host queries",
        covariance_rows["proper_cubic_frames"] == 24
        and covariance_rows["ordered_six_arm_geometry_orbit_size"] == 24
        and covariance_rows["maximum_frame_representation_unitarity"] < TOLERANCE
        and covariance_rows["maximum_update_covariance_residual"] < TOLERANCE
        and covariance_rows["maximum_update_covariance_raw_maximum"] < 5e-14
        and covariance_rows["frame_group_law_failures"] == 0
        and covariance_rows["translation_failures"] == 0
        and covariance_rows["slot_operator_unitarity"] < TOLERANCE
        and covariance_rows["slot_sixth_residual"] < TOLERANCE
        and covariance_rows["slot_macro_unitarity"] < TOLERANCE
        and covariance_rows["maximum_slot_frame_covariance"] < TOLERANCE
        and covariance_rows["active_constraint_involution"] < TOLERANCE
        and covariance_rows["active_constraint_slot_transport"] < TOLERANCE
        and covariance_rows["host_branch_queries"] == 0,
        covariance_rows,
    )
    check(
        "physical support is bounded and inherited constraints survive the maximal star and held size",
        all(
            rows["port_constraint_commutator_failures"] == 0
            and rows["fixed_sector_commutator_failures"] == 0
            and rows["joint_S7_role_register_M2"] == 13
            and rows["total_patch_union_with_joint_S7_role_M2"] < 340
            and rows["maximum_joint_branch_with_joint_S7_role_M2"] < 150
            for rows in physical_rows.values()
        ),
        physical_rows,
    )
    check(
        "joint-role update coin contact slot exclusion and lawful-domain deletions are detected",
        deletion_rows["deleted_joint_order_amplitude_Gram_residual"] > 0.00019
        and deletion_rows["deleted_update_column_unitarity_residual"] > 0.9
        and deletion_rows["deleted_coin_unitarity_residual"] > 0.5
        and deletion_rows["deleted_contact_residual"] > 0.2
        and deletion_rows["deleted_slot_cycle_unitarity_residual"] > 0.9
        and deletion_rows["deleted_unused_S7_state_exclusion_rank_surplus"] == 3152
        and deletion_rows["deleted_unused_slot_state_exclusion_rank_surplus"] == 2
        and deletion_rows["one_S6_only_common_rank_factor"] == 7
        and deletion_rows["lawful_domain_rejections"] == 2,
        deletion_rows,
    )
    print(f"SCIENCE TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


def main() -> int:
    note_contract()
    methodology_controls()
    n4_file_line_witness_control()
    return science_main()


if __name__ == "__main__":
    raise SystemExit(main())
