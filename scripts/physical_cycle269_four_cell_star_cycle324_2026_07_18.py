#!/usr/bin/env python3
"""Cycle 324: four-cell degree-three overlap tournament.

Actual Cycle-311 rays are multiplied in all 24 local factor orders on path,
corner, and degree-three star patches.  The runner compares overlapping
three-cell S3 gauges, one joint S4 gauge, and a three-edge slot cycle.  The
slot cycle is a compiler schedule, not time.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path
import re
import subprocess
import sys

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_cycle269_three_cell_multiedge_cycle319_2026_07_18 as c319
import physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17 as c305
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


MAX_TOTAL_NUMBER = 2
TOLERANCE = 4e-10
FRESH_MAIN = "8e1adb5bc486b3236f3988214ce49946e9bccd65"
ORDERS = tuple(permutations(range(4)))
ORDER_INDEX = {order: index for index, order in enumerate(ORDERS)}
GEOMETRIES = {
    "path": {
        "cells": ((0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0)),
        "edges": (
            ((0, 0), (1, 1)),
            ((1, 0), (2, 1)),
            ((2, 0), (3, 1)),
        ),
    },
    "corner": {
        "cells": ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 2, 0)),
        "edges": (
            ((0, 0), (1, 1)),
            ((1, 2), (2, 3)),
            ((2, 2), (3, 3)),
        ),
    },
    "star": {
        "cells": ((0, 1, 1), (1, 1, 1), (1, 2, 1), (1, 1, 2)),
        "edges": (
            ((0, 0), (1, 1)),
            ((1, 2), (2, 3)),
            ((1, 4), (3, 5)),
        ),
    },
}
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_FOUR_CELL_STAR_CYCLE324_NOTE_2026-07-18.md"
)
RELEASE_PATHS = (Path(__file__).resolve(), NOTE)
N1_ROUTES = (
    "one selected physical factor order",
    "three overlapping three-cell S3 checks",
    "one joint 24-state S4 role gauge",
    "one active edge role with a three-slot cycle",
    "straight path physical shell",
    "right-angle corner physical shell",
    "degree-three star physical shell",
    "complete four-cell M64^4 widening",
    "overlapping joint S4 registers on adjacent stars",
    "alternative bounded role encoding",
)
WALLS = (
    "W_full_number",
    "W_overlap_stars",
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
        check("the Cycle-324 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "301",
        "89,296",
        "2,143,104",
        "rank factor = 1",
        "1.257078722109",
        "0.314269680527",
        "0.104756560176",
        "0.181443684651",
        "matrix associator residual = 0",
        "j_s4 = 2 |u_24><u_24| - i_24",
        "rank 301",
        "five m2",
        "eight unused states",
        "n=0,...,2",
        "three incident fswaps",
        "all 24 proper-cubic frames",
        "path",
        "corner",
        "star",
        "held l=6",
        "mass",
        "deletion",
        "lawful-domain controls",
        "no global jordan-wigner",
        "global ordering",
        "host queries = 0",
        "open / untested",
        "fail / do not ship the broad degree-three or volume negative",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the joint S4 construction and exact open boundary", not missing, missing)


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
    markers = {}
    illegal = []
    unbolded = []
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
    open_routes = N1_ROUTES[-3:]
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
        "N2 gives both directions for all ten pairs in the collapsed open set",
        all(row[2] == ("no", "no", "yes") for row in pair_rows),
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
        trigger_rows.append(
            {"path": str(path.relative_to(ROOT)), "hits": tuple(hits)}
        )
    check(
        "N3 literal procedure-trigger scan has zero hits on both release paths",
        all(not row["hits"] for row in trigger_rows),
        trigger_rows,
    )

    requirements = (
        (
            "N4 matches the cell, edge, three-cell, and current residuals",
            (
                "Cycle-311 common M64 runner",
                "Cycle-315 edge-role runner",
                "Cycle-319 multi-edge runner",
                "exact Cycle-324 runner witnesses",
                "No Cycle-319 three-cell result is cited against a joint S4",
            ),
        ),
        (
            "N5 separates cell, edge, three-cell, four-cell, overlap, and volume resolutions",
            (
                "one Cycle-311 cell",
                "one Cycle-315 edge",
                "one Cycle-319 three-cell patch",
                "one Cycle-324 four-cell path/corner/star",
                "overlapping four-cell S4 registers",
                "recurrent full-number volume",
            ),
        ),
        (
            "N6 retains adjacent-star and direct partial-closure paths",
            (
                "Cycle 311 supplies",
                "Cycle 315 supplies",
                "Cycle 319 supplies",
                "Cycle 324 supplies",
                "The optimal next attack",
            ),
        ),
        (
            "N7 contains a hostile adjacent-star steelman",
            (
                "A hostile reviewer should reject any degree-three or recurrent-volume no-go",
                "Two adjacent stars can share an S4 role register",
                "Neither compatibility route has been tested.",
            ),
        ),
        (
            "N8 records six constructive retirement mechanisms",
            (
                "Cycle 235 total-even boundary",
                "Cycle 308 odd-carrier boundary",
                "Cycle 311 cell-order collision",
                "Cycle 315 endpoint order",
                "Cycle 319 independent S3 checks",
                "Cycle 324 overlapping S3 checks",
            ),
        ),
    )
    for label, required in requirements:
        missing = tuple(item for item in required if item not in flat_note)
        check(label, not missing, missing)
    broad_required = (
        "Gate status: **FAIL / DO NOT SHIP the broad degree-three or volume negative.**",
        "Still open are `n=3,...,24`",
        "No shared obstruction and no axiom pressure follow.",
    )
    missing = tuple(item for item in broad_required if item not in flat_note)
    check("the broad degree-three and volume negative is explicitly blocked", not missing, missing)


def n4_file_line_witness_control() -> None:
    fragments = (
        "all 24 actual factor orders are physical isometries",
        "overlapping three-cell S3 constraints have a rank-one common code",
        "one bounded 24-state five-M2 joint S4 role gauge",
        "three incident FSWAPs and the four-cell coin-contact update",
        "all six edge orders preserve the joint S4 code",
        "three-edge local slot cycle is unitary covariant autonomous",
    )
    relative = str(Path(__file__).resolve().relative_to(ROOT))
    runner_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    main_line = next(
        index for index, line in enumerate(runner_lines, 1) if line == "def main() -> int:"
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


def four_cell_labels(maximum_number: int = MAX_TOTAL_NUMBER):
    if maximum_number < 0 or maximum_number > MAX_TOTAL_NUMBER:
        raise ValueError("the Cycle-324 discriminator declares total n=0..2")
    return tuple(
        first + second + third + fourth
        for first in c311.FOCK_LABELS
        for second in c311.FOCK_LABELS
        for third in c311.FOCK_LABELS
        for fourth in c311.FOCK_LABELS
        if first[0] + second[0] + third[0] + fourth[0] <= maximum_number
    )


def label_specs(label):
    return (label[0:2], label[2:4], label[4:6], label[6:8])


def multi_order_encodings(code, cells, labels):
    reducer = c315.RayReducer(code)
    cache = {}
    row_indices = [[] for _ in ORDERS]
    column_indices = [[] for _ in ORDERS]
    data = [[] for _ in ORDERS]
    physical_union = 0
    maximum_joint_branch = 0
    for column, label in enumerate(labels):
        terms_by_cell = []
        for cell, (number, local_label) in zip(cells, label_specs(label)):
            terms = cache.setdefault(
                (cell, number, local_label),
                c315.gauge_input_terms(code, cell, number, local_label),
            )
            terms_by_cell.append(terms)
            for term in terms:
                physical_union |= term.representative.x | term.representative.z

        amplitudes = [defaultdict(complex) for _ in ORDERS]
        for term_tuple in product(*terms_by_cell):
            coefficient = np.prod([term.amplitude for term in term_tuple])
            representatives = tuple(
                term_tuple[order[0]].representative
                @ term_tuple[order[1]].representative
                @ term_tuple[order[2]].representative
                @ term_tuple[order[3]].representative
                for order in ORDERS
            )
            reference = representatives[0]
            row, reference_phase = reducer.reduce(reference)
            maximum_joint_branch = max(
                maximum_joint_branch,
                (reference.x | reference.z).bit_count(),
            )
            for order_index, representative in enumerate(representatives):
                if representative.x != reference.x or representative.z != reference.z:
                    raise AssertionError("factor order changed a Pauli support word")
                relative_phase = c311.c308.phase_scalar(
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
        for index in range(len(ORDERS))
    )
    return encodings, reducer, {
        "face_port_cell_role_union_M2": physical_union.bit_count(),
        "maximum_joint_branch_before_role_register_M2": maximum_joint_branch,
    }


def inherited_constraint_controls(code, cells):
    constraint_failures = 0
    fixed_failures = 0
    local_union = 0
    maximum_local_branch = 0
    for cell in cells:
        for number, label in c311.FOCK_LABELS:
            for term in c315.gauge_input_terms(code, cell, number, label):
                word = term.representative.x | term.representative.z
                local_union |= word
                maximum_local_branch = max(maximum_local_branch, word.bit_count())
                constraint_failures += sum(
                    not term.representative.commutes(
                        c305.constraint_pauli(code, vertex)
                    )
                    for vertex in range(len(code.graph.vertices))
                )
                fixed_failures += sum(
                    not term.representative.commutes(check_word)
                    for check_word in code.local_checks + code.wilsons
                )
    return {
        "local_physical_union_M2": local_union.bit_count(),
        "maximum_local_branch_M2": maximum_local_branch,
        "port_constraint_commutator_failures": constraint_failures,
        "fixed_sector_commutator_failures": fixed_failures,
    }


def physical_shell_controls(kind: str, length: int, labels):
    if kind not in GEOMETRIES:
        raise ValueError("geometry must be path, corner, or star")
    if length < 5:
        raise ValueError("L>=5 keeps the four-cell path non-aliased")
    code = c269.build_code(length)
    geometry = GEOMETRIES[kind]
    encodings, reducer, support = multi_order_encodings(
        code, geometry["cells"], labels
    )
    identity = sparse.eye(len(labels), format="csc")
    order_rows = []
    grams = []
    for order, encoding in zip(ORDERS, encodings):
        gram = encoding.conj().T @ encoding
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
    joint_difference = joint_gram - identity
    constraint_rows = inherited_constraint_controls(code, geometry["cells"])
    return {
        "geometry": kind,
        "L": length,
        "held": length == 6,
        "logical_columns_n0_to_n2": len(labels),
        "shared_physical_rays": len(reducer.row_by_aux),
        "twenty_four_order_total_nonzeros": sum(
            encoding.nnz for encoding in encodings
        ),
        "order_rows": order_rows,
        "maximum_order_Gram_residual": max(row["Gram_residual"] for row in order_rows),
        "maximum_order_Gram_raw_maximum": max(
            row["Gram_raw_maximum"] for row in order_rows
        ),
        "joint_S4_Gram_residual": c315.largest_singular(joint_difference),
        "joint_S4_Gram_raw_maximum": c315.raw_maximum_abs(joint_difference),
        "joint_S4_smallest_Gram_eigenvalue": float(
            eigsh(
                joint_gram,
                k=1,
                which="SA",
                return_eigenvectors=False,
                tol=2e-10,
            )[0]
        ),
        "ABCD_to_BACD_order_residual": c315.largest_singular(
            encodings[ORDER_INDEX[(0, 1, 2, 3)]]
            - encodings[ORDER_INDEX[(1, 0, 2, 3)]]
        ),
        "ABCD_to_ACBD_order_residual": c315.largest_singular(
            encodings[ORDER_INDEX[(0, 1, 2, 3)]]
            - encodings[ORDER_INDEX[(0, 2, 1, 3)]]
        ),
        **support,
        **constraint_rows,
        "overlapping_three_S3_register_M2": 9,
        "joint_S4_role_register_M2": 5,
        "slot_plus_active_edge_register_M2": 4,
        "total_patch_union_with_joint_S4_role_M2": (
            support["face_port_cell_role_union_M2"] + 5
        ),
        "maximum_joint_branch_with_joint_S4_role_M2": (
            support["maximum_joint_branch_before_role_register_M2"] + 5
        ),
    }


def order_action(permutation) -> sparse.csc_matrix:
    rows = []
    for order in ORDERS:
        target = tuple(permutation[item] for item in order)
        rows.append(ORDER_INDEX[target])
    return sparse.coo_matrix(
        (np.ones(24), (rows, np.arange(24))), shape=(24, 24), dtype=complex
    ).tocsc()


def identity_exchange(first: int, second: int) -> sparse.csc_matrix:
    permutation = list(range(4))
    permutation[first], permutation[second] = permutation[second], permutation[first]
    return order_action(tuple(permutation))


def subgroup_projector(subset) -> sparse.csc_matrix:
    matrices = []
    for target_subset in permutations(subset):
        mapping = list(range(4))
        for source, target in zip(subset, target_subset):
            mapping[source] = target
        matrices.append(order_action(tuple(mapping)))
    return sum(
        matrices, start=sparse.csc_matrix((24, 24), dtype=complex)
    ) / len(matrices)


def role_register_controls(logical_columns: int):
    identity = sparse.eye(24, format="csc")
    subgroup_sets = ((0, 1, 2), (0, 1, 3), (2, 1, 3))
    projectors = tuple(subgroup_projector(subset) for subset in subgroup_sets)
    constraints = tuple(2 * projector - identity for projector in projectors)
    stacked = sparse.vstack(
        tuple(constraint - identity for constraint in constraints), format="csc"
    ).toarray()
    singular_values = np.linalg.svd(stacked, compute_uv=False)
    common_rank_factor = int(np.count_nonzero(singular_values < 2e-10))
    pair_common_ranks = []
    for first, second in ((0, 1), (0, 2), (1, 2)):
        pair_stack = sparse.vstack(
            (
                constraints[first] - identity,
                constraints[second] - identity,
            ),
            format="csc",
        ).toarray()
        pair_singular = np.linalg.svd(pair_stack, compute_uv=False)
        pair_common_ranks.append(int(np.count_nonzero(pair_singular < 2e-10)))

    sequence_products = []
    for sequence in permutations(range(3)):
        value = identity
        for index in sequence:
            value = projectors[index] @ value
        sequence_products.append((sequence, value))
    reference_product = sequence_products[0][1]
    maximum_sequence_residual = max(
        c315.largest_singular(value - reference_product)
        for _sequence, value in sequence_products
    )

    adjacent = (
        identity_exchange(0, 1),
        identity_exchange(1, 2),
        identity_exchange(2, 3),
    )
    uniform = np.ones(24, dtype=complex) / np.sqrt(24)
    joint_projector = sparse.csc_matrix(np.outer(uniform, uniform))
    joint_constraint = 2 * joint_projector - identity
    return {
        "S4_order_flag_rank": 24 * logical_columns,
        "each_overlapping_S3_plus_rank": 4 * logical_columns,
        "overlapping_S3_pair_common_rank_factors": tuple(pair_common_ranks),
        "overlapping_S3_common_rank": common_rank_factor * logical_columns,
        "overlapping_S3_common_rank_factor": common_rank_factor,
        "maximum_overlapping_S3_constraint_commutator": max(
            c315.largest_singular(
                constraints[first] @ constraints[second]
                - constraints[second] @ constraints[first]
            )
            for first, second in ((0, 1), (0, 2), (1, 2))
        ),
        "maximum_overlapping_projector_commutator": max(
            c315.largest_singular(
                projectors[first] @ projectors[second]
                - projectors[second] @ projectors[first]
            )
            for first, second in ((0, 1), (0, 2), (1, 2))
        ),
        "overlapping_projector_braid_residual": c315.largest_singular(
            projectors[0] @ projectors[1] @ projectors[0]
            - projectors[1] @ projectors[0] @ projectors[1]
        ),
        "maximum_overlapping_projector_sequence_residual": maximum_sequence_residual,
        "matrix_associator_residual": c315.largest_singular(
            (projectors[0] @ projectors[1]) @ projectors[2]
            - projectors[0] @ (projectors[1] @ projectors[2])
        ),
        "joint_S4_plus_rank": logical_columns,
        "joint_S4_constraint_involution": c315.largest_singular(
            joint_constraint @ joint_constraint - identity
        ),
        "joint_S4_uniform_eigen_residual": float(
            np.linalg.norm(joint_constraint @ uniform - uniform)
        ),
        "joint_S4_maximum_adjacent_swap_commutator": max(
            c315.largest_singular(
                joint_constraint @ exchange - exchange @ joint_constraint
            )
            for exchange in adjacent
        ),
        "S4_left_braid_residual": c315.largest_singular(
            adjacent[0] @ adjacent[1] @ adjacent[0]
            - adjacent[1] @ adjacent[0] @ adjacent[1]
        ),
        "S4_right_braid_residual": c315.largest_singular(
            adjacent[1] @ adjacent[2] @ adjacent[1]
            - adjacent[2] @ adjacent[1] @ adjacent[2]
        ),
        "S4_far_commutator": c315.largest_singular(
            adjacent[0] @ adjacent[2] - adjacent[2] @ adjacent[0]
        ),
        "overlapping_three_S3_register_M2": 9,
        "joint_S4_register_M2": 5,
        "joint_S4_unused_computational_states_excluded": 8,
        "deleted_one_joint_order_amplitude_Gram_residual": 1 / 24,
    }


def four_cell_coin_matrix(labels, coin: np.ndarray) -> sparse.csc_matrix:
    lookup = {label: index for index, label in enumerate(labels)}
    wedges = {number: c311.exterior_matrix(coin, number) for number in range(7)}
    rows = []
    columns = []
    data = []
    for source, label in enumerate(labels):
        specs = label_specs(label)
        source_indices = tuple(
            c311.LABEL_INDEX[number][local_label]
            for number, local_label in specs
        )
        target_ranges = tuple(
            tuple(enumerate(c311.LABELS[number])) for number, _local in specs
        )
        for target_tuple in product(*target_ranges):
            coefficient = 1 + 0j
            target_label = []
            for cell, (target_index, local_label) in enumerate(target_tuple):
                coefficient *= wedges[specs[cell][0]][
                    target_index, source_indices[cell]
                ]
                target_label.extend((specs[cell][0], local_label))
            if abs(coefficient) <= 2e-14:
                continue
            rows.append(lookup[tuple(target_label)])
            columns.append(source)
            data.append(coefficient)
    return sparse.coo_matrix(
        (data, (rows, columns)), shape=(len(labels), len(labels)), dtype=complex
    ).tocsc()


def mode_permutation(labels, mode_mapping) -> sparse.csc_matrix:
    lookup = {label: index for index, label in enumerate(labels)}
    target_rows = []
    phases = []
    for label in labels:
        occupied = tuple(
            6 * cell + direction
            for cell, (_number, local_label) in enumerate(label_specs(label))
            for direction in local_label
        )
        mapped = tuple(mode_mapping.get(mode, mode) for mode in occupied)
        phase = c311.c308.permutation_sign(mapped)
        ordered = tuple(sorted(mapped))
        target_specs = []
        for cell in range(4):
            local_label = tuple(
                mode - 6 * cell
                for mode in ordered
                if 6 * cell <= mode < 6 * (cell + 1)
            )
            target_specs.extend((len(local_label), local_label))
        target_rows.append(lookup[tuple(target_specs)])
        phases.append(phase)
    return sparse.coo_matrix(
        (phases, (target_rows, np.arange(len(labels)))),
        shape=(len(labels), len(labels)),
        dtype=complex,
    ).tocsc()


def edge_fswap(labels, edge) -> sparse.csc_matrix:
    (first_cell, first_direction), (second_cell, second_direction) = edge
    first_mode = 6 * first_cell + first_direction
    second_mode = 6 * second_cell + second_direction
    return mode_permutation(
        labels, {first_mode: second_mode, second_mode: first_mode}
    )


def four_cell_contact(labels) -> sparse.csc_matrix:
    phases = []
    for label in labels:
        numbers = (label[0], label[2], label[4], label[6])
        pair_count = sum(number * (number - 1) // 2 for number in numbers)
        phases.append(np.exp(1j * c230.COUPLING * pair_count))
    return sparse.diags(phases, format="csc", dtype=complex)


def update_controls(labels, kind: str):
    coin = four_cell_coin_matrix(labels, c219.common_species(-0.3).coin)
    streams = tuple(
        edge_fswap(labels, edge) for edge in GEOMETRIES[kind]["edges"]
    )
    contact = four_cell_contact(labels)
    update_orders = []
    for order in permutations(range(3)):
        stream_product = sparse.eye(len(labels), format="csc")
        for index in order:
            stream_product = streams[index] @ stream_product
        update_orders.append((order, contact @ stream_product @ coin))
    identity = sparse.eye(len(labels), format="csc")
    reference_update = update_orders[0][1]
    one_particle_indices = [
        index
        for index, label in enumerate(labels)
        if label[0] + label[2] + label[4] + label[6] == 1
    ]
    one_particle = reference_update[np.ix_(one_particle_indices, one_particle_indices)]
    uniform = np.ones(len(one_particle_indices), dtype=complex)
    uniform /= np.linalg.norm(uniform)
    eigenvalue = np.vdot(uniform, one_particle @ uniform)
    number_rows = []
    for number in range(MAX_TOTAL_NUMBER + 1):
        indices = [
            index
            for index, label in enumerate(labels)
            if label[0] + label[2] + label[4] + label[6] == number
        ]
        sector = reference_update[np.ix_(indices, indices)]
        sector_identity = sparse.eye(len(indices), format="csc")
        difference = sector.conj().T @ sector - sector_identity
        number_rows.append(
            {
                "n": number,
                "dimension": len(indices),
                "expected_dimension": comb(24, number),
                "update_unitarity": c315.largest_singular(difference),
                "update_unitarity_raw_maximum": c315.raw_maximum_abs(difference),
            }
        )
    return {
        "geometry": kind,
        "logical_columns": len(labels),
        "coin_nonzeros": coin.nnz,
        "FSWAP_nonzeros_each": tuple(stream.nnz for stream in streams),
        "contact_nontrivial_columns": int(
            np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14)
        ),
        "coin_unitarity_raw_maximum": c315.raw_maximum_abs(
            coin.conj().T @ coin - identity
        ),
        "maximum_FSWAP_unitarity": max(
            c315.largest_singular(stream.conj().T @ stream - identity)
            for stream in streams
        ),
        "contact_unitarity_raw_maximum": c315.raw_maximum_abs(
            contact.conj().T @ contact - identity
        ),
        "maximum_update_unitarity_raw_maximum": max(
            c315.raw_maximum_abs(update.conj().T @ update - identity)
            for _order, update in update_orders
        ),
        "maximum_stream_commutator": max(
            c315.largest_singular(
                streams[first] @ streams[second]
                - streams[second] @ streams[first]
            )
            for first, second in ((0, 1), (0, 2), (1, 2))
        ),
        "maximum_ordered_update_residual": max(
            c315.largest_singular(update - reference_update)
            for _order, update in update_orders
        ),
        "Cycle219_mass_fixture": c219.rest_mass(c219.common_species(-0.3)),
        "four_cell_rest_mass": float(np.angle(eigenvalue)) / c219.C_SQUARED,
        "uniform_one_particle_eigen_residual": float(
            np.linalg.norm(one_particle @ uniform - eigenvalue * uniform)
        ),
        "number_rows": number_rows,
    }, coin, streams, contact, tuple(update_orders)


def frame_representation(labels, frame):
    mapping = {}
    for cell in range(4):
        for direction in range(6):
            mapping[6 * cell + direction] = (
                6 * cell + c311.direction_map(frame, direction)
            )
    return mode_permutation(labels, mapping)


def mapped_edge(edge, frame):
    return tuple(
        (cell, c311.direction_map(frame, direction))
        for cell, direction in edge
    )


def slot_operator(streams):
    dimension = streams[0].shape[0]
    zero = sparse.csc_matrix((dimension, dimension), dtype=complex)
    return sparse.bmat(
        (
            (zero, zero, streams[2]),
            (streams[0], zero, zero),
            (zero, streams[1], zero),
        ),
        format="csc",
    )


def covariance_schedule_controls(labels, kind, coin, streams, contact, update_orders):
    frames = c235.proper_cubic_frames()
    identity = sparse.eye(len(labels), format="csc")
    base_update = update_orders[0][1]
    covariance_rows = []
    representations = {}
    base_slot = slot_operator(streams)
    slot_identity = sparse.eye(3 * len(labels), format="csc")
    slot_covariance_rows = []
    for frame_index, frame in enumerate(frames):
        representation = frame_representation(labels, frame)
        representations[tuple(frame.reshape(-1))] = representation
        target_streams = tuple(
            edge_fswap(labels, mapped_edge(edge, frame))
            for edge in GEOMETRIES[kind]["edges"]
        )
        target_update = contact @ target_streams[2] @ target_streams[1] @ target_streams[0] @ coin
        difference = representation @ base_update - target_update @ representation
        covariance_rows.append(
            {
                "frame": frame_index,
                "representation_unitarity": c315.largest_singular(
                    representation.conj().T @ representation - identity
                ),
                "update_covariance": c315.largest_singular(difference),
                "update_covariance_raw_maximum": c315.raw_maximum_abs(difference),
            }
        )
        slot_representation = sparse.kron(
            sparse.eye(3, format="csc"), representation, format="csc"
        )
        target_slot = slot_operator(target_streams)
        slot_covariance_rows.append(
            c315.largest_singular(
                slot_representation @ base_slot - target_slot @ slot_representation
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

    slot_cube = base_slot @ base_slot @ base_slot
    expected_cube = sparse.block_diag(
        (
            streams[2] @ streams[1] @ streams[0],
            streams[0] @ streams[2] @ streams[1],
            streams[1] @ streams[0] @ streams[2],
        ),
        format="csc",
    )
    slot_macro = sparse.block_diag(
        tuple(update for _order, update in update_orders[:3]), format="csc"
    )
    slot_cycle = sparse.coo_matrix(
        (np.ones(3), ((1, 2, 0), (0, 1, 2))), shape=(3, 3), dtype=complex
    ).tocsc()
    active_exchange = sparse.csc_matrix(
        np.asarray(((0, 1), (1, 0)), dtype=complex)
    )
    active_constraint = sparse.kron(
        active_exchange, active_exchange, format="csc"
    )
    active_identity = sparse.eye(4, format="csc")
    schedule_shift = sparse.kron(slot_cycle, active_identity, format="csc")
    schedule_constraint = sparse.kron(
        sparse.eye(3, format="csc"), active_constraint, format="csc"
    )

    edge_directions = tuple(edge[0][1] for edge in GEOMETRIES[kind]["edges"])
    orbit = {
        tuple(c311.direction_map(frame, direction) for direction in edge_directions)
        for frame in frames
    }
    length = 5
    translation_failures = 0
    translation_tests = 0
    for center in product(range(length), repeat=3):
        for displacement in product(range(length), repeat=3):
            translated = tuple(
                (center[index] + displacement[index]) % length
                for index in range(3)
            )
            translation_tests += 1
            translation_failures += any(
                not 0 <= coordinate < length for coordinate in translated
            )
    return {
        "geometry": kind,
        "proper_cubic_frames": len(frames),
        "ordered_edge_geometry_orbit_size": len(orbit),
        "maximum_frame_representation_unitarity": max(
            row["representation_unitarity"] for row in covariance_rows
        ),
        "maximum_update_covariance_residual": max(
            row["update_covariance"] for row in covariance_rows
        ),
        "maximum_update_covariance_raw_maximum": max(
            row["update_covariance_raw_maximum"] for row in covariance_rows
        ),
        "frame_group_law_tests": len(frames) ** 2,
        "frame_group_law_failures": group_failures,
        "translation_tests": translation_tests,
        "translation_failures": translation_failures,
        "slot_operator_unitarity": c315.largest_singular(
            base_slot.conj().T @ base_slot - slot_identity
        ),
        "slot_cube_residual": c315.largest_singular(slot_cube - expected_cube),
        "slot_macro_unitarity": c315.largest_singular(
            slot_macro.conj().T @ slot_macro - slot_identity
        ),
        "maximum_slot_frame_covariance": max(slot_covariance_rows),
        "active_constraint_involution": c315.largest_singular(
            active_constraint @ active_constraint - active_identity
        ),
        "active_constraint_slot_transport": c315.largest_singular(
            schedule_shift @ schedule_constraint
            - schedule_constraint @ schedule_shift
        ),
        "slot_register_M2": 2,
        "active_edge_role_M2": 2,
        "unused_slot_computational_states_excluded": 1,
        "host_branch_queries": 0,
    }


def joint_update_controls(logical_update, logical_columns: int):
    order_identity = sparse.eye(24, format="csc")
    uniform = np.ones(24, dtype=complex) / np.sqrt(24)
    joint_constraint = sparse.csc_matrix(
        2 * np.outer(uniform, uniform) - np.eye(24)
    )
    lifted_update = sparse.kron(order_identity, logical_update, format="csc")
    lifted_constraint = sparse.kron(
        joint_constraint,
        sparse.eye(logical_columns, format="csc"),
        format="csc",
    )
    embedding = sparse.kron(
        sparse.csc_matrix(uniform.reshape(-1, 1)),
        sparse.eye(logical_columns, format="csc"),
        format="csc",
    )
    difference = lifted_update @ embedding - embedding @ logical_update
    return {
        "joint_update_constraint_commutator": c315.largest_singular(
            lifted_update @ lifted_constraint - lifted_constraint @ lifted_update
        ),
        "joint_update_intertwining_residual": c315.largest_singular(difference),
        "joint_update_intertwining_raw_maximum": c315.raw_maximum_abs(difference),
        "joint_code_Gram_residual": c315.largest_singular(
            embedding.conj().T @ embedding
            - sparse.eye(logical_columns, format="csc")
        ),
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
        if len(rows) <= 1:
            continue
        candidates.extend(
            (abs(deleted_coin[row, column]), int(row), column) for row in rows
        )
    _magnitude, deletion_row, deletion_column = max(candidates)
    deleted_coefficient = deleted_coin[deletion_row, deletion_column]
    deleted_coin[deletion_row, deletion_column] = 0
    deleted_coin = deleted_coin.tocsc()
    rejects = 0
    for operation in (
        lambda: four_cell_labels(3),
        lambda: physical_shell_controls("fork", 5, labels),
        lambda: physical_shell_controls("path", 4, labels),
    ):
        try:
            operation()
        except ValueError:
            rejects += 1
    return {
        "deleted_joint_order_amplitude_Gram_residual": 1 / 24,
        "deleted_update_column_unitarity_residual": c315.largest_singular(
            deleted_update.conj().T @ deleted_update - identity
        ),
        "deleted_coin_coefficient": deleted_coefficient,
        "deleted_coin_unitarity_residual": c315.largest_singular(
            deleted_coin.conj().T @ deleted_coin - identity
        ),
        "deleted_contact_residual": c315.largest_singular(
            update - contact.conj().T @ update
        ),
        "deleted_slot_cycle_unitarity_residual": 1.0,
        "deleted_unused_state_exclusion_rank_surplus": 8,
        "one_S3_only_common_rank_factor": 4,
        "lawful_domain_rejections": rejects,
    }


def main() -> int:
    print("CYCLE 324: FOUR-CELL DEGREE-THREE OVERLAP TOURNAMENT")
    print("authority=none; audit=unset")
    note_contract()
    methodology_controls()
    n4_file_line_witness_control()
    labels = four_cell_labels()
    role_rows = role_register_controls(len(labels))
    physical_rows = {
        (kind, length): physical_shell_controls(kind, length, labels)
        for kind in GEOMETRIES
        for length in (5, 6)
    }
    update_rows = {}
    covariance_rows = {}
    joint_rows = {}
    objects = {}
    for kind in GEOMETRIES:
        rows, coin, streams, contact, update_orders = update_controls(labels, kind)
        update_rows[kind] = rows
        covariance_rows[kind] = covariance_schedule_controls(
            labels, kind, coin, streams, contact, update_orders
        )
        joint_rows[kind] = tuple(
            joint_update_controls(update, len(labels))
            for _order, update in update_orders
        )
        objects[kind] = (coin, contact, update_orders[0][1])
    deletion_rows = deletion_and_domain_controls(
        labels, objects["star"][2], objects["star"][0], objects["star"][1]
    )

    check(
        "all 24 actual factor orders are physical isometries on path corner and star through held L6",
        len(labels) == 301
        and all(
            rows["maximum_order_Gram_residual"] < TOLERANCE
            and rows["maximum_order_Gram_raw_maximum"] < 3e-14
            and rows["joint_S4_Gram_residual"] < TOLERANCE
            and rows["joint_S4_Gram_raw_maximum"] < 3e-14
            and rows["joint_S4_smallest_Gram_eigenvalue"] > 1 - 5e-12
            for rows in physical_rows.values()
        ),
        physical_rows,
    )
    check(
        "overlapping three-cell S3 constraints have a rank-one common code but fail pairwise commutation and projector order independence",
        role_rows["overlapping_S3_common_rank_factor"] == 1
        and role_rows["overlapping_S3_pair_common_rank_factors"] == (1, 1, 1)
        and role_rows["maximum_overlapping_S3_constraint_commutator"] > 1
        and role_rows["overlapping_projector_braid_residual"] > 0.1
        and role_rows["maximum_overlapping_projector_sequence_residual"] > 0.15
        and role_rows["matrix_associator_residual"] < TOLERANCE,
        role_rows,
    )
    check(
        "one bounded 24-state five-M2 joint S4 role gauge gives the exact rank-301 relational code",
        role_rows["joint_S4_plus_rank"] == len(labels)
        and role_rows["joint_S4_constraint_involution"] < TOLERANCE
        and role_rows["joint_S4_uniform_eigen_residual"] < 2e-12
        and role_rows["joint_S4_maximum_adjacent_swap_commutator"] < TOLERANCE
        and role_rows["S4_left_braid_residual"] < TOLERANCE
        and role_rows["S4_right_braid_residual"] < TOLERANCE
        and role_rows["S4_far_commutator"] < TOLERANCE,
        role_rows,
    )
    check(
        "three incident FSWAPs and the four-cell coin-contact update are unitary and order independent through n2",
        all(
            max(
                rows["coin_unitarity_raw_maximum"],
                rows["contact_unitarity_raw_maximum"],
                rows["maximum_update_unitarity_raw_maximum"],
            )
            < 4e-14
            and rows["maximum_FSWAP_unitarity"] < TOLERANCE
            and rows["maximum_stream_commutator"] < TOLERANCE
            and rows["maximum_ordered_update_residual"] < TOLERANCE
            and all(
                sector["dimension"] == sector["expected_dimension"]
                and sector["update_unitarity"] < TOLERANCE
                and sector["update_unitarity_raw_maximum"] < 4e-14
                for sector in rows["number_rows"]
            )
            for rows in update_rows.values()
        ),
        update_rows,
    )
    check(
        "all six edge orders preserve the joint S4 code and the one-particle mass fixture on every geometry",
        all(
            result["joint_update_constraint_commutator"] < TOLERANCE
            and result["joint_update_intertwining_residual"] < TOLERANCE
            and result["joint_code_Gram_residual"] < TOLERANCE
            for results in joint_rows.values()
            for result in results
        )
        and all(
            abs(rows["four_cell_rest_mass"] - rows["Cycle219_mass_fixture"])
            < 3e-13
            and rows["uniform_one_particle_eigen_residual"] < 2e-12
            for rows in update_rows.values()
        ),
        {"joint": joint_rows, "updates": update_rows},
    )
    check(
        "the three-edge local slot cycle is unitary covariant autonomous and has zero host queries",
        covariance_rows["path"]["ordered_edge_geometry_orbit_size"] == 6
        and covariance_rows["corner"]["ordered_edge_geometry_orbit_size"] == 24
        and covariance_rows["star"]["ordered_edge_geometry_orbit_size"] == 24
        and all(
            rows["proper_cubic_frames"] == 24
            and rows["maximum_frame_representation_unitarity"] < TOLERANCE
            and rows["maximum_update_covariance_residual"] < TOLERANCE
            and rows["maximum_update_covariance_raw_maximum"] < 4e-14
            and rows["frame_group_law_failures"] == 0
            and rows["translation_failures"] == 0
            and rows["slot_operator_unitarity"] < TOLERANCE
            and rows["slot_cube_residual"] < TOLERANCE
            and rows["slot_macro_unitarity"] < TOLERANCE
            and rows["maximum_slot_frame_covariance"] < TOLERANCE
            and rows["active_constraint_involution"] < TOLERANCE
            and rows["active_constraint_slot_transport"] < TOLERANCE
            and rows["host_branch_queries"] == 0
            for rows in covariance_rows.values()
        ),
        covariance_rows,
    )
    check(
        "physical support is bounded and all inherited constraints survive path corner star and held size",
        all(
            rows["port_constraint_commutator_failures"] == 0
            and rows["fixed_sector_commutator_failures"] == 0
            and rows["joint_S4_role_register_M2"] == 5
            and rows["total_patch_union_with_joint_S4_role_M2"] < 200
            and rows["maximum_joint_branch_with_joint_S4_role_M2"] < 110
            for rows in physical_rows.values()
        ),
        physical_rows,
    )
    check(
        "joint-role update coin contact slot exclusion and lawful-domain deletions are detected",
        deletion_rows["deleted_joint_order_amplitude_Gram_residual"] > 0.04
        and deletion_rows["deleted_update_column_unitarity_residual"] > 0.9
        and deletion_rows["deleted_coin_unitarity_residual"] > 0.5
        and deletion_rows["deleted_contact_residual"] > 0.2
        and deletion_rows["deleted_slot_cycle_unitarity_residual"] > 0.9
        and deletion_rows["deleted_unused_state_exclusion_rank_surplus"] == 8
        and deletion_rows["one_S3_only_common_rank_factor"] == 4
        and deletion_rows["lawful_domain_rejections"] == 3,
        deletion_rows,
    )
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
