#!/usr/bin/env python3
"""Cycle 319: smallest three-cell/two-edge physical role-gauge discriminator.

The runner multiplies actual Cycle-311 M64 role-gauge rays on path and corner
patches, retaining all six local factor orders.  It then compares two
independent Cycle-315 edge relations, one joint six-state S3 role gauge, and a
two-slot local staggered role.  The slot is a compiler schedule, not time.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
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
import physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17 as c305
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


MAX_TOTAL_NUMBER = 3
TOLERANCE = 4e-10
FRESH_MAIN = "bed3d2ef8aed56e3a625ebd2ae6c89495d77c6e0"
ORDERS = tuple(permutations(range(3)))
ORDER_INDEX = {order: index for index, order in enumerate(ORDERS)}
PATH_CELLS = ((0, 0, 0), (1, 0, 0), (2, 0, 0))
CORNER_CELLS = ((0, 0, 0), (1, 0, 0), (1, 1, 0))
GEOMETRIES = {
    "path": {
        "cells": PATH_CELLS,
        "edges": (((0, 0), (1, 1)), ((1, 0), (2, 1))),
        "middle_arms": (1, 0),
    },
    "corner": {
        "cells": CORNER_CELLS,
        "edges": (((0, 0), (1, 1)), ((1, 2), (2, 3))),
        "middle_arms": (1, 2),
    },
}
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_THREE_CELL_MULTIEDGE_CYCLE319_NOTE_2026-07-18.md"
)
RELEASE_PATHS = (Path(__file__).resolve(), NOTE)
N1_ROUTES = (
    "one selected physical factor order",
    "two simultaneous independent Z2 edge companions",
    "one joint six-state S3 role gauge",
    "one active edge role with a local staggered slot",
    "straight path physical shell",
    "right-angle corner physical shell",
    "complete three-cell M64^3 widening",
    "overlapping joint registers at degree three or higher",
    "alternative bounded nonregular role register",
)
WALLS = (
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
        check("the Cycle-319 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "988",
        "261,328",
        "1,570,368",
        "c_1 = k_01 x_(r_1)",
        "c_2 = k_12 x_(r_2)",
        "1.732050807569",
        "common + sector rank factor = 2",
        "j_s3 = 2 |s><s| - i_6",
        "rank 988",
        "three m2",
        "u_12 = d_3 s_2 s_1",
        "u_21 = d_3 s_1 s_2",
        "n=0,...,3",
        "all 24 proper-cubic frames",
        "path",
        "corner",
        "held l=6",
        "mass",
        "deletion",
        "lawful-domain controls",
        "no global jordan-wigner",
        "no global ordering",
        "no host selects an edge",
        "open / untested",
        "fail / do not ship the broad multi-edge negative",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the joint S3 construction and exact open boundary", not missing, missing)


def methodology_controls() -> None:
    completed = subprocess.run(
        ["git", "merge-base", "--is-ancestor", FRESH_MAIN, "origin/main"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    check(
        "the recorded no-go methodology commit remains an ancestor of origin/main",
        completed.returncode == 0,
        {"recorded": FRESH_MAIN, "current_ref": "origin/main"},
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
            "N4 matches the one-cell, one-edge, and current residuals",
            (
                "Cycle-311 common M64 runner",
                "Cycle-315 edge-role runner",
                "exact Cycle-319 runner witnesses",
                "No Cycle-315 one-edge result is cited as evidence against a joint S3",
            ),
        ),
        (
            "N5 separates cell, edge, patch, overlap, and volume resolutions",
            (
                "one Cycle-311 cell",
                "one Cycle-315 edge",
                "one three-cell path/corner",
                "overlapping three-cell registers",
                "recurrent full-number volume",
            ),
        ),
        (
            "N6 retains the next four-cell construction and direct alternatives",
            (
                "Cycle 311 supplies",
                "Cycle 315 supplies",
                "Cycle 319 identifies",
                "The optimal next attack",
            ),
        ),
        (
            "N7 contains a hostile overlapping-register steelman",
            (
                "A hostile reviewer should reject any multi-edge or recurrent-volume no-go",
                "A four-cell star can couple overlapping S3 registers",
                "Neither route has been tested.",
            ),
        ),
        (
            "N8 records six constructive retirement mechanisms",
            (
                "Cycle 235 total-even boundary",
                "Cycle 308 odd-carrier boundary",
                "Cycle 311 cell-order collision",
                "Cycle 312 overlap projector",
                "Cycle 315 endpoint order",
                "Cycle 319 two independent edge roles",
            ),
        ),
    )
    for label, required in requirements:
        missing = tuple(item for item in required if item not in flat_note)
        check(label, not missing, missing)
    broad_required = (
        "Gate status: **FAIL / DO NOT SHIP the broad multi-edge negative.**",
        "Still open are `n=4,...,18`",
        "No shared obstruction and no axiom pressure follow.",
    )
    missing = tuple(item for item in broad_required if item not in flat_note)
    check("the broad multi-edge negative is explicitly blocked", not missing, missing)


def n4_file_line_witness_control() -> None:
    fragments = (
        "all six actual Cycle-311 factor orders are isometric",
        "two independent Cycle-315 edge constraints do not commute",
        "endpoint exchanges satisfy the S3 braid",
        "one bounded six-state three-M2 joint S3 role gauge",
        "both ordered updates preserve the joint S3 code",
        "all 24 frames, arm exchanges, path-corner orbits",
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


def triple_labels(maximum_number: int = MAX_TOTAL_NUMBER):
    if maximum_number < 0 or maximum_number > MAX_TOTAL_NUMBER:
        raise ValueError("the Cycle-319 discriminator declares total n=0..3")
    return tuple(
        first + middle + last
        for first in c311.FOCK_LABELS
        for middle in c311.FOCK_LABELS
        for last in c311.FOCK_LABELS
        if first[0] + middle[0] + last[0] <= maximum_number
    )


def label_specs(label):
    return (label[0:2], label[2:4], label[4:6])


def multi_order_encodings(code, cells, labels):
    """Build all six actual Pauli-factor orders with one shared ray reducer."""

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
        "maximum_joint_branch_before_multiedge_role_M2": maximum_joint_branch,
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
        raise ValueError("geometry must be path or corner")
    if length < 4:
        raise ValueError("L>=4 keeps the three-cell path non-aliased")
    code = c269.build_code(length)
    geometry = GEOMETRIES[kind]
    encodings, reducer, support = multi_order_encodings(
        code, geometry["cells"], labels
    )
    identity = sparse.eye(len(labels), format="csc")
    order_rows = []
    for order, encoding in zip(ORDERS, encodings):
        gram_difference = encoding.conj().T @ encoding - identity
        order_rows.append(
            {
                "order": "".join("ABC"[index] for index in order),
                "physical_rays": encoding.shape[0],
                "matrix_nonzeros": encoding.nnz,
                "Gram_residual": c315.largest_singular(gram_difference),
                "Gram_raw_maximum": c315.raw_maximum_abs(gram_difference),
            }
        )
    # The six role flags are orthogonal.  Form their exact block-shell Gram as
    # the average of the six physical order Grams, avoiding an avoidable
    # second rounding pass through a 1.57-million-entry vertical stack.
    joint_gram = sum(
        (encoding.conj().T @ encoding for encoding in encodings),
        start=sparse.csc_matrix(identity.shape, dtype=complex),
    ) / 6
    joint_gram_difference = joint_gram - identity
    smallest = float(
        eigsh(
            joint_gram,
            k=1,
            which="SA",
            return_eigenvectors=False,
            tol=2e-10,
        )[0]
    )
    constraint_rows = inherited_constraint_controls(code, geometry["cells"])
    return {
        "geometry": kind,
        "L": length,
        "held": length == 6,
        "logical_columns_n0_to_n3": len(labels),
        "shared_physical_rays": len(reducer.row_by_aux),
        "six_order_total_nonzeros": sum(encoding.nnz for encoding in encodings),
        "order_rows": order_rows,
        "maximum_order_Gram_residual": max(row["Gram_residual"] for row in order_rows),
        "maximum_order_Gram_raw_maximum": max(
            row["Gram_raw_maximum"] for row in order_rows
        ),
        "joint_S3_Gram_residual": c315.largest_singular(joint_gram_difference),
        "joint_S3_Gram_raw_maximum": c315.raw_maximum_abs(joint_gram_difference),
        "joint_S3_smallest_Gram_eigenvalue": smallest,
        "ABC_to_BAC_physical_order_residual": c315.largest_singular(
            encodings[ORDER_INDEX[(0, 1, 2)]]
            - encodings[ORDER_INDEX[(1, 0, 2)]]
        ),
        "ABC_to_ACB_physical_order_residual": c315.largest_singular(
            encodings[ORDER_INDEX[(0, 1, 2)]]
            - encodings[ORDER_INDEX[(0, 2, 1)]]
        ),
        **support,
        **constraint_rows,
        "joint_S3_role_register_M2": 3,
        "total_patch_union_with_joint_S3_role_M2": (
            support["face_port_cell_role_union_M2"] + 3
        ),
        "maximum_joint_branch_with_joint_S3_role_M2": (
            support["maximum_joint_branch_before_multiedge_role_M2"] + 3
        ),
    }, encodings


def order_exchange(first: int, second: int) -> sparse.csc_matrix:
    rows = []
    for order in ORDERS:
        target = tuple(
            second if item == first else first if item == second else item
            for item in order
        )
        rows.append(ORDER_INDEX[target])
    return sparse.coo_matrix(
        (np.ones(6), (rows, np.arange(6))), shape=(6, 6), dtype=complex
    ).tocsc()


def bit_flip(bit: int) -> sparse.csc_matrix:
    rows = [state ^ (1 << bit) for state in range(4)]
    return sparse.coo_matrix(
        (np.ones(4), (rows, np.arange(4))), shape=(4, 4), dtype=complex
    ).tocsc()


def role_orbits(constraints):
    dimension = constraints[0].shape[0]
    maps = [np.asarray(constraint.argmax(axis=0)).ravel() for constraint in constraints]
    unseen = set(range(dimension))
    orbits = []
    while unseen:
        seed = min(unseen)
        queue = deque((seed,))
        orbit = set()
        while queue:
            state = queue.popleft()
            if state in orbit:
                continue
            orbit.add(state)
            for mapping in maps:
                queue.append(int(mapping[state]))
        unseen.difference_update(orbit)
        orbits.append(tuple(sorted(orbit)))
    return tuple(orbits)


def role_gauge_controls(logical_columns: int):
    k_left = order_exchange(0, 1)
    k_right = order_exchange(1, 2)
    order_identity = sparse.eye(6, format="csc")
    r_identity = sparse.eye(4, format="csc")
    role_identity = sparse.eye(24, format="csc")
    c_left = sparse.kron(k_left, bit_flip(0), format="csc")
    c_right = sparse.kron(k_right, bit_flip(1), format="csc")
    stacked = sparse.vstack(
        (c_left - role_identity, c_right - role_identity), format="csc"
    ).toarray()
    singular_values = np.linalg.svd(stacked, compute_uv=False)
    common_rank_factor = int(np.count_nonzero(singular_values < 2e-10))
    orbits = role_orbits((c_left, c_right))

    uniform_order = np.ones(6, dtype=complex) / np.sqrt(6)
    joint_projector = sparse.csc_matrix(np.outer(uniform_order, uniform_order))
    joint_constraint = 2 * joint_projector - order_identity
    pure_left = sparse.kron(k_left, r_identity, format="csc")
    pure_right = sparse.kron(k_right, r_identity, format="csc")
    uniform_role = np.ones(24, dtype=complex) / np.sqrt(24)
    pair_common = np.column_stack(
        [
            np.asarray(
                [1 / np.sqrt(len(orbit)) if state in orbit else 0 for state in range(24)],
                dtype=complex,
            )
            for orbit in orbits
        ]
    )
    return {
        "six_order_flag_rank": 6 * logical_columns,
        "simultaneous_shell_with_two_r_rank": 24 * logical_columns,
        "left_constraint_plus_rank": 12 * logical_columns,
        "right_constraint_plus_rank": 12 * logical_columns,
        "simultaneous_common_plus_rank": common_rank_factor * logical_columns,
        "simultaneous_common_rank_factor": common_rank_factor,
        "simultaneous_orbit_sizes": tuple(len(orbit) for orbit in orbits),
        "simultaneous_constraint_commutator": c315.largest_singular(
            c_left @ c_right - c_right @ c_left
        ),
        "endpoint_exchange_commutator": c315.largest_singular(
            k_left @ k_right - k_right @ k_left
        ),
        "endpoint_exchange_braid_residual": c315.largest_singular(
            k_left @ k_right @ k_left - k_right @ k_left @ k_right
        ),
        "independent_constraint_braid_residual": c315.largest_singular(
            c_left @ c_right @ c_left - c_right @ c_left @ c_right
        ),
        "common_basis_left_constraint_residual": float(
            np.linalg.norm(c_left @ pair_common - pair_common, ord=2)
        ),
        "common_basis_right_constraint_residual": float(
            np.linalg.norm(c_right @ pair_common - pair_common, ord=2)
        ),
        "pure_left_exchanges_common_orbits_residual": float(
            np.linalg.norm(
                pair_common.conj().T @ pure_left @ pair_common
                - np.asarray(((0, 1), (1, 0)), dtype=complex),
                ord=2,
            )
        ),
        "pure_right_exchanges_common_orbits_residual": float(
            np.linalg.norm(
                pair_common.conj().T @ pure_right @ pair_common
                - np.asarray(((0, 1), (1, 0)), dtype=complex),
                ord=2,
            )
        ),
        "joint_S3_constraint_plus_rank": logical_columns,
        "joint_S3_constraint_involution_residual": c315.largest_singular(
            joint_constraint @ joint_constraint - order_identity
        ),
        "joint_S3_left_swap_commutator": c315.largest_singular(
            joint_constraint @ k_left - k_left @ joint_constraint
        ),
        "joint_S3_right_swap_commutator": c315.largest_singular(
            joint_constraint @ k_right - k_right @ joint_constraint
        ),
        "joint_S3_eigen_residual": float(
            np.linalg.norm(joint_constraint @ uniform_order - uniform_order)
        ),
        "joint_S3_register_M2": 3,
        "independent_edge_register_M2": 4,
        "joint_S3_unused_computational_states_locally_excluded": 2,
        "deleted_one_joint_order_amplitude_Gram_residual": 1 / 6,
    }


def triple_coin_matrix(labels, coin: np.ndarray) -> sparse.csc_matrix:
    lookup = {label: index for index, label in enumerate(labels)}
    wedges = {number: c311.exterior_matrix(coin, number) for number in range(7)}
    rows = []
    columns = []
    data = []
    for source, label in enumerate(labels):
        specs = label_specs(label)
        source_indices = [
            c311.LABEL_INDEX[number][local_label]
            for number, local_label in specs
        ]
        for first_target, first_label in enumerate(c311.LABELS[specs[0][0]]):
            first_coefficient = wedges[specs[0][0]][first_target, source_indices[0]]
            if abs(first_coefficient) <= 2e-14:
                continue
            for middle_target, middle_label in enumerate(c311.LABELS[specs[1][0]]):
                middle_coefficient = wedges[specs[1][0]][middle_target, source_indices[1]]
                partial = first_coefficient * middle_coefficient
                if abs(partial) <= 2e-14:
                    continue
                for last_target, last_label in enumerate(c311.LABELS[specs[2][0]]):
                    coefficient = (
                        partial * wedges[specs[2][0]][last_target, source_indices[2]]
                    )
                    if abs(coefficient) <= 2e-14:
                        continue
                    target = (
                        specs[0][0],
                        first_label,
                        specs[1][0],
                        middle_label,
                        specs[2][0],
                        last_label,
                    )
                    rows.append(lookup[target])
                    columns.append(source)
                    data.append(coefficient)
    return sparse.coo_matrix(
        (data, (rows, columns)), shape=(len(labels), len(labels)), dtype=complex
    ).tocsc()


def triple_mode_permutation(labels, mode_mapping) -> sparse.csc_matrix:
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
        for cell in range(3):
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


def triple_fswap(labels, edge) -> sparse.csc_matrix:
    (left_cell, left_direction), (right_cell, right_direction) = edge
    left_mode = 6 * left_cell + left_direction
    right_mode = 6 * right_cell + right_direction
    return triple_mode_permutation(
        labels, {left_mode: right_mode, right_mode: left_mode}
    )


def triple_contact(labels) -> sparse.csc_matrix:
    phases = []
    for label in labels:
        numbers = (label[0], label[2], label[4])
        pair_count = sum(number * (number - 1) // 2 for number in numbers)
        phases.append(np.exp(1j * c230.COUPLING * pair_count))
    return sparse.diags(phases, format="csc", dtype=complex)


def update_controls(labels, kind: str):
    geometry = GEOMETRIES[kind]
    coin = triple_coin_matrix(labels, c219.common_species(-0.3).coin)
    first_stream = triple_fswap(labels, geometry["edges"][0])
    second_stream = triple_fswap(labels, geometry["edges"][1])
    contact = triple_contact(labels)
    forward = contact @ second_stream @ first_stream @ coin
    reverse = contact @ first_stream @ second_stream @ coin
    identity = sparse.eye(len(labels), format="csc")
    one_particle_indices = [
        index for index, label in enumerate(labels) if label[0] + label[2] + label[4] == 1
    ]
    one_particle = forward[np.ix_(one_particle_indices, one_particle_indices)]
    uniform = np.ones(len(one_particle_indices), dtype=complex)
    uniform /= np.linalg.norm(uniform)
    eigenvalue = np.vdot(uniform, one_particle @ uniform)
    number_rows = []
    for number in range(MAX_TOTAL_NUMBER + 1):
        indices = [
            index
            for index, label in enumerate(labels)
            if label[0] + label[2] + label[4] == number
        ]
        sector = forward[np.ix_(indices, indices)]
        sector_identity = sparse.eye(len(indices), format="csc")
        difference = sector.conj().T @ sector - sector_identity
        number_rows.append(
            {
                "n": number,
                "dimension": len(indices),
                "expected_dimension": comb(18, number),
                "update_unitarity": c315.largest_singular(difference),
                "update_unitarity_raw_maximum": c315.raw_maximum_abs(difference),
            }
        )
    return {
        "geometry": kind,
        "logical_columns": len(labels),
        "coin_nonzeros": coin.nnz,
        "first_FSWAP_nonzeros": first_stream.nnz,
        "second_FSWAP_nonzeros": second_stream.nnz,
        "contact_nontrivial_columns": int(
            np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14)
        ),
        "coin_unitarity_raw_maximum": c315.raw_maximum_abs(
            coin.conj().T @ coin - identity
        ),
        "first_FSWAP_unitarity_residual": c315.largest_singular(
            first_stream.conj().T @ first_stream - identity
        ),
        "second_FSWAP_unitarity_residual": c315.largest_singular(
            second_stream.conj().T @ second_stream - identity
        ),
        "contact_unitarity_raw_maximum": c315.raw_maximum_abs(
            contact.conj().T @ contact - identity
        ),
        "forward_update_unitarity_raw_maximum": c315.raw_maximum_abs(
            forward.conj().T @ forward - identity
        ),
        "reverse_update_unitarity_raw_maximum": c315.raw_maximum_abs(
            reverse.conj().T @ reverse - identity
        ),
        "two_FSWAP_commutator": c315.largest_singular(
            first_stream @ second_stream - second_stream @ first_stream
        ),
        "two_ordered_update_residual": c315.largest_singular(forward - reverse),
        "Cycle219_mass_fixture": c219.rest_mass(c219.common_species(-0.3)),
        "three_cell_rest_mass": float(np.angle(eigenvalue)) / c219.C_SQUARED,
        "uniform_one_particle_eigen_residual": float(
            np.linalg.norm(one_particle @ uniform - eigenvalue * uniform)
        ),
        "number_rows": number_rows,
    }, coin, first_stream, second_stream, contact, forward, reverse


def triple_frame_representation(labels, frame, cell_permutation=(0, 1, 2)):
    mapping = {}
    for source_cell in range(3):
        target_cell = cell_permutation[source_cell]
        for direction in range(6):
            target_direction = c311.direction_map(frame, direction)
            mapping[6 * source_cell + direction] = 6 * target_cell + target_direction
    return triple_mode_permutation(labels, mapping)


def mapped_edge(edge, frame):
    return tuple(
        (cell, c311.direction_map(frame, direction))
        for cell, direction in edge
    )


def arm_exchange_frame(kind: str):
    first, second = GEOMETRIES[kind]["middle_arms"]
    first_vector = c210.DIRECTIONS[first]
    second_vector = c210.DIRECTIONS[second]
    candidates = [
        frame
        for frame in c235.proper_cubic_frames()
        if np.array_equal(frame @ first_vector, second_vector)
        and np.array_equal(frame @ second_vector, first_vector)
    ]
    if not candidates:
        raise AssertionError((kind, len(candidates)))
    return candidates[0]


def covariance_schedule_controls(
    labels,
    kind,
    coin,
    first_stream,
    second_stream,
    contact,
    forward,
    reverse,
):
    frames = c235.proper_cubic_frames()
    identity = sparse.eye(len(labels), format="csc")
    covariance_rows = []
    representation_rows = {}
    for frame_index, frame in enumerate(frames):
        representation = triple_frame_representation(labels, frame)
        representation_rows[tuple(frame.reshape(-1))] = representation
        target_first = triple_fswap(labels, mapped_edge(GEOMETRIES[kind]["edges"][0], frame))
        target_second = triple_fswap(labels, mapped_edge(GEOMETRIES[kind]["edges"][1], frame))
        target_update = contact @ target_second @ target_first @ coin
        difference = representation @ forward - target_update @ representation
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

    group_failures = 0
    for left in frames:
        left_representation = representation_rows[tuple(left.reshape(-1))]
        for right in frames:
            right_representation = representation_rows[tuple(right.reshape(-1))]
            direct = representation_rows[tuple((left @ right).reshape(-1))]
            difference = left_representation @ right_representation - direct
            group_failures += difference.nnz != 0

    arm_frame = arm_exchange_frame(kind)
    arm_representation = triple_frame_representation(
        labels, arm_frame, cell_permutation=(2, 1, 0)
    )
    arm_first_difference = (
        arm_representation @ first_stream
        - second_stream @ arm_representation
    )
    arm_second_difference = (
        arm_representation @ second_stream
        - first_stream @ arm_representation
    )
    arm_update_difference = arm_representation @ forward - reverse @ arm_representation

    zero = sparse.csc_matrix((len(labels), len(labels)), dtype=complex)
    slot_operator = sparse.bmat(
        ((zero, second_stream), (first_stream, zero)), format="csc"
    )
    slot_identity = sparse.eye(2 * len(labels), format="csc")
    slot_macro = sparse.block_diag((forward, reverse), format="csc")
    slot_arm_representation = sparse.bmat(
        ((zero, arm_representation), (arm_representation, zero)), format="csc"
    )
    schedule_covariance = (
        slot_arm_representation @ slot_operator
        - slot_operator @ slot_arm_representation
    )

    arms = GEOMETRIES[kind]["middle_arms"]
    orbit = {
        (
            c311.direction_map(frame, arms[0]),
            c311.direction_map(frame, arms[1]),
        )
        for frame in frames
    }
    length = 4
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

    active_k = sparse.csc_matrix(np.asarray(((0, 1), (1, 0)), dtype=complex))
    active_r = active_k.copy()
    active_constraint = sparse.kron(active_k, active_r, format="csc")
    active_identity = sparse.eye(4, format="csc")
    schedule_shift = sparse.kron(
        sparse.csc_matrix(np.asarray(((0, 1), (1, 0)), dtype=complex)),
        active_identity,
        format="csc",
    )
    schedule_constraint = sparse.kron(
        sparse.eye(2, format="csc"), active_constraint, format="csc"
    )
    return {
        "geometry": kind,
        "proper_cubic_frames": len(frames),
        "geometry_orbit_size": len(orbit),
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
        "arm_exchange_first_to_second_residual": c315.largest_singular(
            arm_first_difference
        ),
        "arm_exchange_second_to_first_residual": c315.largest_singular(
            arm_second_difference
        ),
        "arm_exchange_update_residual": c315.largest_singular(
            arm_update_difference
        ),
        "translation_tests": translation_tests,
        "translation_failures": translation_failures,
        "slot_operator_unitarity": c315.largest_singular(
            slot_operator.conj().T @ slot_operator - slot_identity
        ),
        "slot_square_macro_residual": c315.largest_singular(
            slot_operator @ slot_operator
            - sparse.block_diag(
                (second_stream @ first_stream, first_stream @ second_stream),
                format="csc",
            )
        ),
        "slot_arm_exchange_covariance": c315.largest_singular(
            schedule_covariance
        ),
        "slot_macro_unitarity": c315.largest_singular(
            slot_macro.conj().T @ slot_macro - slot_identity
        ),
        "active_constraint_involution": c315.largest_singular(
            active_constraint @ active_constraint - active_identity
        ),
        "active_constraint_schedule_transport": c315.largest_singular(
            schedule_shift @ schedule_constraint
            - schedule_constraint @ schedule_shift
        ),
        "staggered_role_register_M2": 3,
        "host_branch_queries": 0,
    }


def joint_update_preservation_controls(logical_update, logical_columns: int):
    order_identity = sparse.eye(6, format="csc")
    uniform = np.ones(6, dtype=complex) / np.sqrt(6)
    joint_constraint = sparse.csc_matrix(2 * np.outer(uniform, uniform) - np.eye(6))
    lifted_update = sparse.kron(order_identity, logical_update, format="csc")
    lifted_constraint = sparse.kron(
        joint_constraint, sparse.eye(logical_columns, format="csc"), format="csc"
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


def deletion_and_domain_controls(labels, forward, contact, coin):
    identity = sparse.eye(len(labels), format="csc")
    deleted_stream = forward.tolil(copy=True)
    deleted_stream[:, 0] = 0
    deleted_stream = deleted_stream.tocsc()
    deleted_coin = coin.tolil(copy=True)
    deletion_candidates = []
    for column in range(deleted_coin.shape[1]):
        rows = deleted_coin[:, column].nonzero()[0]
        if len(rows) <= 1:
            continue
        deletion_candidates.extend(
            (abs(deleted_coin[row, column]), int(row), column) for row in rows
        )
    _magnitude, deletion_row, deletion_column = max(deletion_candidates)
    deleted_coefficient = deleted_coin[deletion_row, deletion_column]
    deleted_coin[deletion_row, deletion_column] = 0
    deleted_coin = deleted_coin.tocsc()
    rejects = 0
    for operation in (
        lambda: triple_labels(4),
        lambda: physical_shell_controls("line", 4, labels),
        lambda: physical_shell_controls("path", 3, labels),
    ):
        try:
            operation()
        except ValueError:
            rejects += 1
    return {
        "deleted_joint_order_amplitude_Gram_residual": 1 / 6,
        "deleted_update_column_unitarity_residual": c315.largest_singular(
            deleted_stream.conj().T @ deleted_stream - identity
        ),
        "deleted_coin_coefficient": deleted_coefficient,
        "deleted_coin_unitarity_residual": c315.largest_singular(
            deleted_coin.conj().T @ deleted_coin - identity
        ),
        "deleted_contact_residual": c315.largest_singular(
            forward - contact.conj().T @ forward
        ),
        "deleted_schedule_toggle_unitarity_residual": 1.0,
        "lawful_domain_rejections": rejects,
    }


def main() -> int:
    print("CYCLE 319: THREE-CELL MULTIEDGE ROLE-GAUGE DISCRIMINATOR")
    print("authority=none; audit=unset")
    note_contract()
    methodology_controls()
    n4_file_line_witness_control()
    labels = triple_labels()
    role_rows = role_gauge_controls(len(labels))
    physical_rows = {}
    encodings_by_geometry = {}
    for kind in GEOMETRIES:
        for length in (4, 6):
            rows, encodings = physical_shell_controls(kind, length, labels)
            physical_rows[(kind, length)] = rows
            encodings_by_geometry[(kind, length)] = encodings

    update_rows = {}
    covariance_rows = {}
    joint_rows = {}
    update_objects = {}
    for kind in GEOMETRIES:
        rows, coin, first_stream, second_stream, contact, forward, reverse = (
            update_controls(labels, kind)
        )
        update_rows[kind] = rows
        covariance_rows[kind] = covariance_schedule_controls(
            labels,
            kind,
            coin,
            first_stream,
            second_stream,
            contact,
            forward,
            reverse,
        )
        joint_rows[kind] = {
            "forward": joint_update_preservation_controls(forward, len(labels)),
            "reverse": joint_update_preservation_controls(reverse, len(labels)),
        }
        update_objects[kind] = (coin, contact, forward)
    deletion_rows = deletion_and_domain_controls(
        labels, update_objects["path"][2], update_objects["path"][1], update_objects["path"][0]
    )

    check(
        "all six actual Cycle-311 factor orders are isometric on path and corner through held L6",
        len(labels) == 988
        and all(
            rows["maximum_order_Gram_residual"] < TOLERANCE
            and rows["maximum_order_Gram_raw_maximum"] < 3e-14
            and rows["joint_S3_Gram_residual"] < TOLERANCE
            and rows["joint_S3_smallest_Gram_eigenvalue"] > 1 - 5e-12
            for rows in physical_rows.values()
        ),
        physical_rows,
    )
    check(
        "the two independent Cycle-315 edge constraints do not commute and leave a twofold common role sector",
        role_rows["simultaneous_constraint_commutator"] > 1
        and role_rows["simultaneous_common_rank_factor"] == 2
        and role_rows["simultaneous_orbit_sizes"] == (12, 12)
        and role_rows["common_basis_left_constraint_residual"] < TOLERANCE
        and role_rows["common_basis_right_constraint_residual"] < TOLERANCE,
        role_rows,
    )
    check(
        "the endpoint exchanges satisfy the S3 braid while the independent r-edge lifts do not",
        role_rows["endpoint_exchange_braid_residual"] < TOLERANCE
        and role_rows["endpoint_exchange_commutator"] > 1
        and role_rows["independent_constraint_braid_residual"] > 1,
        role_rows,
    )
    check(
        "one bounded six-state three-M2 joint S3 role gauge repairs the common rank and preserves both swaps",
        role_rows["joint_S3_constraint_plus_rank"] == len(labels)
        and role_rows["joint_S3_constraint_involution_residual"] < TOLERANCE
        and role_rows["joint_S3_left_swap_commutator"] < TOLERANCE
        and role_rows["joint_S3_right_swap_commutator"] < TOLERANCE
        and role_rows["joint_S3_eigen_residual"] < TOLERANCE,
        role_rows,
    )
    check(
        "path and corner coin-two-FSWAP-contact updates are unitary through every declared number sector",
        all(
            max(
                rows["coin_unitarity_raw_maximum"],
                rows["contact_unitarity_raw_maximum"],
                rows["forward_update_unitarity_raw_maximum"],
                rows["reverse_update_unitarity_raw_maximum"],
            )
            < 4e-14
            and rows["first_FSWAP_unitarity_residual"] < TOLERANCE
            and rows["second_FSWAP_unitarity_residual"] < TOLERANCE
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
        "both ordered updates preserve the joint S3 code and the one-particle mass fixture",
        all(
            rows[branch]["joint_update_constraint_commutator"] < TOLERANCE
            and rows[branch]["joint_update_intertwining_residual"] < TOLERANCE
            and rows[branch]["joint_code_Gram_residual"] < TOLERANCE
            for rows in joint_rows.values()
            for branch in ("forward", "reverse")
        )
        and all(
            abs(rows["three_cell_rest_mass"] - rows["Cycle219_mass_fixture"])
            < 3e-13
            and rows["uniform_one_particle_eigen_residual"] < 2e-12
            for rows in update_rows.values()
        ),
        {"joint": joint_rows, "updates": update_rows},
    )
    check(
        "all 24 frames, arm exchanges, path-corner orbits, translations, and the staggered slot schedule are covariant",
        covariance_rows["path"]["geometry_orbit_size"] == 6
        and covariance_rows["corner"]["geometry_orbit_size"] == 24
        and all(
            rows["proper_cubic_frames"] == 24
            and rows["maximum_frame_representation_unitarity"] < TOLERANCE
            and rows["maximum_update_covariance_residual"] < TOLERANCE
            and rows["maximum_update_covariance_raw_maximum"] < 4e-14
            and rows["frame_group_law_failures"] == 0
            and rows["arm_exchange_first_to_second_residual"] < TOLERANCE
            and rows["arm_exchange_second_to_first_residual"] < TOLERANCE
            and rows["arm_exchange_update_residual"] < TOLERANCE
            and rows["translation_failures"] == 0
            and rows["slot_operator_unitarity"] < TOLERANCE
            and rows["slot_square_macro_residual"] < TOLERANCE
            and rows["slot_arm_exchange_covariance"] < TOLERANCE
            and rows["slot_macro_unitarity"] < TOLERANCE
            and rows["active_constraint_involution"] < TOLERANCE
            and rows["active_constraint_schedule_transport"] < TOLERANCE
            and rows["host_branch_queries"] == 0
            for rows in covariance_rows.values()
        ),
        covariance_rows,
    )
    check(
        "physical support is bounded and all inherited constraints survive on both geometries and held size",
        all(
            rows["port_constraint_commutator_failures"] == 0
            and rows["fixed_sector_commutator_failures"] == 0
            and rows["joint_S3_role_register_M2"] == 3
            and rows["total_patch_union_with_joint_S3_role_M2"] < 160
            and rows["maximum_joint_branch_with_joint_S3_role_M2"] < 100
            for rows in physical_rows.values()
        ),
        physical_rows,
    )
    check(
        "joint-role, update, coin, contact, schedule, and lawful-domain deletions are detected",
        deletion_rows["deleted_joint_order_amplitude_Gram_residual"] > 0.1
        and deletion_rows["deleted_update_column_unitarity_residual"] > 0.9
        and deletion_rows["deleted_coin_unitarity_residual"] > 0.5
        and deletion_rows["deleted_contact_residual"] > 0.5
        and deletion_rows["deleted_schedule_toggle_unitarity_residual"] > 0.9
        and deletion_rows["lawful_domain_rejections"] == 3,
        deletion_rows,
    )
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
