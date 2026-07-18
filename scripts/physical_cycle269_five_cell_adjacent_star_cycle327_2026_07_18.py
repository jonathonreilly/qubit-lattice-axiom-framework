#!/usr/bin/env python3
"""Cycle 327: five-cell overlap of two degree-three star patches.

The patch is one cubic center with four arms.  The two four-cell stars share
the center and two arms, so their union has five cells.  Actual Cycle-311
rays are multiplied in all 120 S5 factor orders through total n=2.  Two S4
subgroup checks, one joint S5 role, and a transported four-edge slot are
compared.  The slot is a compiler schedule, not time.
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

import physical_cycle269_four_cell_star_cycle324_2026_07_18 as c324


c219 = c324.c219
c230 = c324.c230
c235 = c324.c235
c269 = c324.c269
c305 = c324.c305
c311 = c324.c311
c315 = c324.c315

MAX_TOTAL_NUMBER = 2
TOLERANCE = 4e-10
FRESH_MAIN = "689ae2c8018fb23ac0d9b92ea2d3324c9249938b"
ORDERS = tuple(permutations(range(5)))
ORDER_INDEX = {order: index for index, order in enumerate(ORDERS)}
CELLS = (
    (0, 1, 1),  # A: -x arm
    (1, 1, 1),  # B: shared center
    (2, 1, 1),  # C: +x arm
    (1, 2, 1),  # D: +y arm, first-star-only
    (1, 1, 2),  # E: +z arm, second-star-only
)
STARS = ((0, 1, 2, 3), (0, 1, 2, 4))
EDGES = (
    ((0, 0), (1, 1)),
    ((1, 2), (3, 3)),
    ((1, 0), (2, 1)),
    ((1, 4), (4, 5)),
)
PAIR_LABELS = tuple((first, second) for first in range(5) for second in range(first + 1, 5))
INVERSION_MASKS = []
for order in ORDERS:
    positions = {item: index for index, item in enumerate(order)}
    mask = 0
    for bit, (first, second) in enumerate(PAIR_LABELS):
        if positions[first] > positions[second]:
            mask |= 1 << bit
    INVERSION_MASKS.append(mask)
SIGN_TABLE = np.asarray(
    [
        [(-1 if (branch_mask & inversion_mask).bit_count() % 2 else 1) for inversion_mask in INVERSION_MASKS]
        for branch_mask in range(1 << len(PAIR_LABELS))
    ],
    dtype=np.int8,
)
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_FIVE_CELL_ADJACENT_STAR_CYCLE327_NOTE_2026-07-18.md"
)
RELEASE_PATHS = (Path(__file__).resolve(), NOTE)
N1_ROUTES = (
    "one selected physical factor order",
    "two overlapping four-cell S4 projectors",
    "one joint 120-state S5 role gauge",
    "one active edge role with a transported four-slot cycle",
    "five-cell adjacent-star physical shell",
    "all four incident FSWAP update orders",
    "complete five-cell M64^5 widening",
    "overlapping joint S5 registers in a recurrent volume",
    "alternative bounded role encoding",
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
        check("the Cycle-327 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "466",
        "295,232",
        "35,427,840",
        "rank factor = 1",
        "0.968245836552",
        "0.242061459138",
        "0.0605153647845",
        "register-change associator",
        "0.250000000000",
        "j_s5 = 2 |u_120><u_120| - i_120",
        "rank 466",
        "seven m2",
        "eight unused states",
        "n=0,...,2",
        "four literal fswaps",
        "all 24 proper-cubic frames",
        "held l=6",
        "mass",
        "deletion",
        "lawful-domain controls",
        "no global jordan-wigner",
        "global ordering",
        "host queries = 0",
        "open / untested",
        "fail / do not ship the broad adjacent-star or volume negative",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the joint S5 construction and exact open boundary", not missing, missing)


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
        trigger_rows.append({"path": str(path.relative_to(ROOT)), "hits": tuple(hits)})
    check(
        "N3 literal procedure-trigger scan has zero hits on both release paths",
        all(not row["hits"] for row in trigger_rows),
        trigger_rows,
    )

    requirements = (
        (
            "N4 matches the cell, star, and current residuals",
            (
                "Cycle-311 common M64 runner",
                "Cycle-324 four-cell star runner",
                "exact Cycle-327 runner witnesses",
                "No Cycle-324 single-star result is cited against a joint S5",
            ),
        ),
        (
            "N5 separates cell, edge, star, overlap, distinct centers, and volume resolutions",
            (
                "one Cycle-311 cell",
                "one Cycle-315 edge",
                "one Cycle-324 four-cell star",
                "one Cycle-327 five-cell overlap",
                "distinct adjacent cubic centers",
                "overlapping five-cell S5 registers",
                "recurrent full-number volume",
            ),
        ),
        (
            "N6 retains larger-overlap and direct partial-closure paths",
            (
                "Cycle 311 supplies",
                "Cycle 324 supplies",
                "Cycle 327 supplies",
                "The optimal next attack",
            ),
        ),
        (
            "N7 contains a hostile recurrent-overlap steelman",
            (
                "A hostile reviewer should reject any adjacent-star or recurrent-volume no-go",
                "Two five-cell crosses can share an S5 role register",
                "Neither volume-compatibility route has been tested.",
            ),
        ),
        (
            "N8 records seven constructive retirement mechanisms",
            (
                "Cycle 235 total-even boundary",
                "Cycle 308 odd-carrier boundary",
                "Cycle 311 cell-order collision",
                "Cycle 315 endpoint order",
                "Cycle 319 independent S3 checks",
                "Cycle 324 overlapping S3 checks",
                "Cycle 327 overlapping S4 checks",
            ),
        ),
    )
    for label, required in requirements:
        missing = tuple(item for item in required if item not in flat_note)
        check(label, not missing, missing)
    broad_required = (
        "Gate status: **FAIL / DO NOT SHIP the broad adjacent-star or volume negative.**",
        "Still open are `n=3,...,30`",
        "No shared obstruction and no axiom pressure follow.",
    )
    missing = tuple(item for item in broad_required if item not in flat_note)
    check("the broad adjacent-star and volume negative is explicitly blocked", not missing, missing)


def n4_file_line_witness_control() -> None:
    fragments = (
        "all 120 actual five-cell factor orders are physical isometries",
        "two overlapping four-cell S4 projectors have a rank-one common code",
        "one bounded 120-state seven-M2 joint S5 role",
        "four incident FSWAPs and all 24 five-cell coin-contact update orders",
        "all 24 update orders preserve the joint S5 code",
        "transported four-edge slot cycle is unitary covariant autonomous",
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


def five_cell_labels(maximum_number: int = MAX_TOTAL_NUMBER):
    if maximum_number < 0 or maximum_number > MAX_TOTAL_NUMBER:
        raise ValueError("the Cycle-327 discriminator declares total n=0..2")
    return tuple(
        first + second + third + fourth + fifth
        for first in c311.FOCK_LABELS
        for second in c311.FOCK_LABELS
        for third in c311.FOCK_LABELS
        for fourth in c311.FOCK_LABELS
        for fifth in c311.FOCK_LABELS
        if first[0] + second[0] + third[0] + fourth[0] + fifth[0]
        <= maximum_number
    )


def label_specs(label):
    return tuple(label[2 * index : 2 * index + 2] for index in range(5))


def branch_anticommutation_mask(representatives) -> int:
    mask = 0
    for bit, (first, second) in enumerate(PAIR_LABELS):
        if not representatives[first].commutes(representatives[second]):
            mask |= 1 << bit
    return mask


def multiply_base(representatives):
    value = representatives[0]
    for representative in representatives[1:]:
        value = value @ representative
    return value


def compressed_order_data(code, labels):
    reducer = c315.RayReducer(code)
    cache = {}
    row_chunks = []
    column_chunks = []
    value_chunks = []
    physical_union = 0
    maximum_branch = 0
    validation_failures = 0
    validated_branches = 0
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
            base = multiply_base(representatives)
            row, base_phase = reducer.reduce(base)
            maximum_branch = max(maximum_branch, (base.x | base.z).bit_count())
            branch_mask = branch_anticommutation_mask(representatives)
            values = coefficient * base_phase * SIGN_TABLE[branch_mask]
            if row not in amplitudes:
                amplitudes[row] = np.zeros(len(ORDERS), dtype=complex)
            amplitudes[row] += values

            if validated_branches < 4:
                for order_index, order in enumerate(ORDERS):
                    direct = representatives[order[0]]
                    for item in order[1:]:
                        direct = direct @ representatives[item]
                    relative = c311.c308.phase_scalar(
                        (direct.phase - base.phase) % 4
                    )
                    validation_failures += (
                        direct.x != base.x
                        or direct.z != base.z
                        or abs(relative - SIGN_TABLE[branch_mask, order_index])
                        > 2e-13
                    )
                validated_branches += 1

        rows = np.asarray(sorted(amplitudes), dtype=np.int64)
        values = np.vstack([amplitudes[row] for row in rows])
        keep = np.max(abs(values), axis=1) > 2e-13
        rows = rows[keep]
        values = values[keep]
        row_chunks.append(rows)
        column_chunks.append(np.full(len(rows), column, dtype=np.int32))
        value_chunks.append(values)

    return {
        "rows": np.concatenate(row_chunks),
        "columns": np.concatenate(column_chunks),
        "values": np.vstack(value_chunks),
        "physical_rows": len(reducer.row_by_aux),
        "face_port_cell_role_union_M2": physical_union.bit_count(),
        "maximum_joint_branch_before_role_register_M2": maximum_branch,
        "direct_order_phase_validation_branches": validated_branches,
        "direct_order_phase_validation_failures": validation_failures,
    }


def physical_shell_controls(length: int, labels):
    if length < 5:
        raise ValueError("L>=5 keeps the five-cell cross non-aliased")
    code = c269.build_code(length)
    data = compressed_order_data(code, labels)
    identity = sparse.eye(len(labels), format="csc")
    joint_gram = sparse.csc_matrix(identity.shape, dtype=complex)
    maximum_gram = 0.0
    maximum_raw = 0.0
    minimum_nnz = None
    maximum_nnz = 0
    selected = {}
    selected_indices = {
        ORDER_INDEX[(0, 1, 2, 3, 4)],
        ORDER_INDEX[(1, 0, 2, 3, 4)],
        ORDER_INDEX[(0, 1, 2, 4, 3)],
    }
    for order_index, order in enumerate(ORDERS):
        values = data["values"][:, order_index]
        keep = abs(values) > 2e-13
        encoding = sparse.coo_matrix(
            (
                values[keep],
                (data["rows"][keep], data["columns"][keep]),
            ),
            shape=(data["physical_rows"], len(labels)),
            dtype=complex,
        ).tocsc()
        gram = encoding.conj().T @ encoding
        difference = gram - identity
        maximum_gram = max(maximum_gram, c315.largest_singular(difference))
        maximum_raw = max(maximum_raw, c315.raw_maximum_abs(difference))
        joint_gram += gram
        minimum_nnz = encoding.nnz if minimum_nnz is None else min(minimum_nnz, encoding.nnz)
        maximum_nnz = max(maximum_nnz, encoding.nnz)
        if order_index in selected_indices:
            selected[order] = encoding
        if (order_index + 1) % 30 == 0:
            print(
                f"Cycle327 L={length} physical order {order_index + 1}/120",
                flush=True,
            )
    joint_gram /= len(ORDERS)
    joint_difference = joint_gram - identity
    inherited = c324.inherited_constraint_controls(code, CELLS)
    base = selected[(0, 1, 2, 3, 4)]
    return {
        "L": length,
        "held": length == 6,
        "logical_columns_n0_to_n2": len(labels),
        "shared_physical_rays": data["physical_rows"],
        "minimum_order_nonzeros": minimum_nnz,
        "maximum_order_nonzeros": maximum_nnz,
        "one_hundred_twenty_order_total_nonzeros": int(
            sum(np.count_nonzero(abs(data["values"][:, index]) > 2e-13) for index in range(len(ORDERS)))
        ),
        "maximum_order_Gram_residual": maximum_gram,
        "maximum_order_Gram_raw_maximum": maximum_raw,
        "joint_S5_Gram_residual": c315.largest_singular(joint_difference),
        "joint_S5_Gram_raw_maximum": c315.raw_maximum_abs(joint_difference),
        "joint_S5_smallest_Gram_eigenvalue": float(
            eigsh(joint_gram, k=1, which="SA", return_eigenvectors=False)[0]
        ),
        "ABCDE_to_BACDE_order_residual": c315.largest_singular(
            base - selected[(1, 0, 2, 3, 4)]
        ),
        "ABCDE_to_ABCED_order_residual": c315.largest_singular(
            base - selected[(0, 1, 2, 4, 3)]
        ),
        "overlapping_two_S4_register_M2": 10,
        "joint_S5_role_register_M2": 7,
        "slot_plus_active_edge_register_M2": 4,
        "total_patch_union_with_joint_S5_role_M2": data[
            "face_port_cell_role_union_M2"
        ]
        + 7,
        "maximum_joint_branch_with_joint_S5_role_M2": data[
            "maximum_joint_branch_before_role_register_M2"
        ]
        + 7,
        **{key: value for key, value in data.items() if key not in {"rows", "columns", "values", "physical_rows"}},
        **inherited,
    }


def order_action(permutation) -> sparse.csc_matrix:
    rows = []
    for order in ORDERS:
        target = tuple(permutation[item] for item in order)
        rows.append(ORDER_INDEX[target])
    return sparse.coo_matrix(
        (np.ones(120), (rows, np.arange(120))),
        shape=(120, 120),
        dtype=complex,
    ).tocsc()


def identity_exchange(first: int, second: int) -> sparse.csc_matrix:
    permutation = list(range(5))
    permutation[first], permutation[second] = permutation[second], permutation[first]
    return order_action(tuple(permutation))


def subgroup_projector(subset) -> sparse.csc_matrix:
    matrices = []
    for target_subset in permutations(subset):
        mapping = list(range(5))
        for source, target in zip(subset, target_subset):
            mapping[source] = target
        matrices.append(order_action(tuple(mapping)))
    return sum(matrices, start=sparse.csc_matrix((120, 120), dtype=complex)) / 24


def plus_basis(projector):
    eigenvalues, eigenvectors = np.linalg.eigh(projector.toarray())
    return eigenvectors[:, eigenvalues > 0.5]


def role_register_controls(logical_columns: int):
    identity = sparse.eye(120, format="csc")
    left, right = tuple(subgroup_projector(star) for star in STARS)
    constraints = (2 * left - identity, 2 * right - identity)
    stacked = sparse.vstack(
        (constraints[0] - identity, constraints[1] - identity), format="csc"
    ).toarray()
    singular_values = np.linalg.svd(stacked, compute_uv=False)
    common_rank_factor = int(np.count_nonzero(singular_values < 2e-10))
    uniform = np.ones(120, dtype=complex) / np.sqrt(120)
    joint_projector = sparse.csc_matrix(np.outer(uniform, uniform))
    joint_constraint = 2 * joint_projector - identity
    adjacent = tuple(identity_exchange(index, index + 1) for index in range(4))

    left_basis = plus_basis(left)
    right_basis = plus_basis(right)
    change_lr = left_basis.conj().T @ right_basis
    change_r5 = right_basis.conj().T @ uniform.reshape(-1, 1)
    change_5l = uniform.reshape(1, -1).conj() @ left_basis
    associator = (change_lr @ change_r5) @ change_5l - change_lr @ (change_r5 @ change_5l)
    direct_through_joint = (
        left_basis.conj().T @ uniform.reshape(-1, 1)
    ) @ (
        uniform.reshape(1, -1).conj() @ right_basis
    )
    return {
        "S5_order_flag_rank": 120 * logical_columns,
        "each_S4_plus_rank_factor": left_basis.shape[1],
        "overlapping_S4_common_rank_factor": common_rank_factor,
        "overlapping_S4_common_rank": common_rank_factor * logical_columns,
        "overlapping_S4_constraint_commutator": c315.largest_singular(
            constraints[0] @ constraints[1] - constraints[1] @ constraints[0]
        ),
        "overlapping_S4_projector_commutator": c315.largest_singular(
            left @ right - right @ left
        ),
        "overlapping_S4_projector_order_residual": c315.largest_singular(
            left @ right @ left - right @ left @ right
        ),
        "overlapping_S4_matrix_associator_residual": c315.largest_singular(
            (left @ right) @ joint_projector - left @ (right @ joint_projector)
        ),
        "register_change_associator_residual": float(np.linalg.norm(associator)),
        "register_change_direct_vs_joint_residual": float(
            np.linalg.svd(change_lr - direct_through_joint, compute_uv=False)[0]
        ),
        "register_change_common_vector_transport": float(
            np.linalg.norm(change_lr @ change_r5 - left_basis.conj().T @ uniform.reshape(-1, 1))
        ),
        "joint_S5_plus_rank": logical_columns,
        "joint_S5_constraint_involution": c315.largest_singular(
            joint_constraint @ joint_constraint - identity
        ),
        "joint_S5_uniform_eigen_residual": float(
            np.linalg.norm(joint_constraint @ uniform - uniform)
        ),
        "joint_S5_maximum_adjacent_swap_commutator": max(
            c315.largest_singular(
                joint_constraint @ exchange - exchange @ joint_constraint
            )
            for exchange in adjacent
        ),
        "S5_maximum_adjacent_braid_residual": max(
            c315.largest_singular(
                adjacent[index] @ adjacent[index + 1] @ adjacent[index]
                - adjacent[index + 1] @ adjacent[index] @ adjacent[index + 1]
            )
            for index in range(3)
        ),
        "S5_maximum_far_commutator": max(
            c315.largest_singular(
                adjacent[first] @ adjacent[second]
                - adjacent[second] @ adjacent[first]
            )
            for first, second in ((0, 2), (0, 3), (1, 3))
        ),
        "overlapping_two_S4_register_M2": 10,
        "joint_S5_register_M2": 7,
        "joint_S5_unused_computational_states_excluded": 8,
    }


def five_cell_coin_matrix(labels, coin: np.ndarray) -> sparse.csc_matrix:
    lookup = {label: index for index, label in enumerate(labels)}
    wedges = {number: c311.exterior_matrix(coin, number) for number in range(7)}
    rows, columns, data = [], [], []
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
                coefficient *= wedges[specs[cell][0]][target_index, source_indices[cell]]
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
        for cell in range(5):
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


def edge_fswap(labels, edge) -> sparse.csc_matrix:
    (first_cell, first_direction), (second_cell, second_direction) = edge
    first_mode = 6 * first_cell + first_direction
    second_mode = 6 * second_cell + second_direction
    return mode_permutation(labels, {first_mode: second_mode, second_mode: first_mode})


def five_cell_contact(labels) -> sparse.csc_matrix:
    phases = []
    for label in labels:
        numbers = tuple(label[2 * cell] for cell in range(5))
        pair_count = sum(number * (number - 1) // 2 for number in numbers)
        phases.append(np.exp(1j * c230.COUPLING * pair_count))
    return sparse.diags(phases, format="csc", dtype=complex)


def update_controls(labels):
    coin = five_cell_coin_matrix(labels, c219.common_species(-0.3).coin)
    streams = tuple(edge_fswap(labels, edge) for edge in EDGES)
    contact = five_cell_contact(labels)
    update_orders = []
    for order in permutations(range(4)):
        stream_product = sparse.eye(len(labels), format="csc")
        for index in order:
            stream_product = streams[index] @ stream_product
        update_orders.append((order, contact @ stream_product @ coin))
    identity = sparse.eye(len(labels), format="csc")
    reference_update = update_orders[0][1]
    one_particle_indices = [
        index
        for index, label in enumerate(labels)
        if sum(label[2 * cell] for cell in range(5)) == 1
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
            if sum(label[2 * cell] for cell in range(5)) == number
        ]
        sector = reference_update[np.ix_(indices, indices)]
        sector_identity = sparse.eye(len(indices), format="csc")
        difference = sector.conj().T @ sector - sector_identity
        number_rows.append(
            {
                "n": number,
                "dimension": len(indices),
                "expected_dimension": comb(30, number),
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
                streams[first] @ streams[second] - streams[second] @ streams[first]
            )
            for first in range(4)
            for second in range(first + 1, 4)
        ),
        "maximum_ordered_update_residual": max(
            c315.largest_singular(update - reference_update)
            for _order, update in update_orders
        ),
        "Cycle219_mass_fixture": c219.rest_mass(c219.common_species(-0.3)),
        "five_cell_rest_mass": float(np.angle(eigenvalue)) / c219.C_SQUARED,
        "uniform_one_particle_eigen_residual": float(
            np.linalg.norm(one_particle @ uniform - eigenvalue * uniform)
        ),
        "number_rows": number_rows,
    }, coin, streams, contact, tuple(update_orders)


def frame_representation(labels, frame):
    mapping = {}
    for cell in range(5):
        for direction in range(6):
            mapping[6 * cell + direction] = 6 * cell + c311.direction_map(frame, direction)
    return mode_permutation(labels, mapping)


def mapped_edge(edge, frame):
    return tuple((cell, c311.direction_map(frame, direction)) for cell, direction in edge)


def slot_operator(streams):
    slot_dimension = len(streams)
    logical_dimension = streams[0].shape[0]
    result = sparse.csc_matrix(
        (slot_dimension * logical_dimension, slot_dimension * logical_dimension),
        dtype=complex,
    )
    for slot, stream in enumerate(streams):
        matrix_unit = sparse.coo_matrix(
            ([1], ([(slot + 1) % slot_dimension], [slot])),
            shape=(slot_dimension, slot_dimension),
            dtype=complex,
        ).tocsc()
        result += sparse.kron(matrix_unit, stream, format="csc")
    return result


def covariance_schedule_controls(labels, coin, streams, contact, update_orders):
    frames = c235.proper_cubic_frames()
    identity = sparse.eye(len(labels), format="csc")
    base_update = update_orders[0][1]
    representations = {}
    covariance_rows = []
    base_slot = slot_operator(streams)
    slot_identity = sparse.eye(4 * len(labels), format="csc")
    slot_covariance = []
    for frame_index, frame in enumerate(frames):
        representation = frame_representation(labels, frame)
        representations[tuple(frame.reshape(-1))] = representation
        target_streams = tuple(edge_fswap(labels, mapped_edge(edge, frame)) for edge in EDGES)
        target_update = contact @ target_streams[3] @ target_streams[2] @ target_streams[1] @ target_streams[0] @ coin
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
            sparse.eye(4, format="csc"), representation, format="csc"
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

    slot_fourth = base_slot @ base_slot @ base_slot @ base_slot
    expected_blocks = []
    for start in range(4):
        value = sparse.eye(len(labels), format="csc")
        for offset in range(4):
            value = streams[(start + offset) % 4] @ value
        expected_blocks.append(value)
    expected_fourth = sparse.block_diag(tuple(expected_blocks), format="csc")
    slot_macro = sparse.block_diag(
        tuple(update for _order, update in update_orders[:4]), format="csc"
    )
    slot_cycle = sparse.coo_matrix(
        (np.ones(4), ((1, 2, 3, 0), (0, 1, 2, 3))),
        shape=(4, 4),
        dtype=complex,
    ).tocsc()
    active_exchange = sparse.csc_matrix(np.asarray(((0, 1), (1, 0)), dtype=complex))
    active_constraint = sparse.kron(active_exchange, active_exchange, format="csc")
    active_identity = sparse.eye(4, format="csc")
    schedule_shift = sparse.kron(slot_cycle, active_identity, format="csc")
    schedule_constraint = sparse.kron(
        sparse.eye(4, format="csc"), active_constraint, format="csc"
    )

    arm_directions = tuple(edge[0][1] if edge[0][0] == 1 else edge[1][1] for edge in EDGES)
    orbit = {
        tuple(c311.direction_map(frame, direction) for direction in arm_directions)
        for frame in frames
    }
    translation_failures = 0
    translation_tests = 0
    length = 5
    for center in product(range(length), repeat=3):
        for displacement in product(range(length), repeat=3):
            translated = tuple((center[index] + displacement[index]) % length for index in range(3))
            translation_tests += 1
            translation_failures += any(not 0 <= coordinate < length for coordinate in translated)
    return {
        "proper_cubic_frames": len(frames),
        "ordered_four_arm_geometry_orbit_size": len(orbit),
        "maximum_frame_representation_unitarity": max(row["representation_unitarity"] for row in covariance_rows),
        "maximum_update_covariance_residual": max(row["update_covariance"] for row in covariance_rows),
        "maximum_update_covariance_raw_maximum": max(row["update_covariance_raw_maximum"] for row in covariance_rows),
        "frame_group_law_tests": len(frames) ** 2,
        "frame_group_law_failures": group_failures,
        "translation_tests": translation_tests,
        "translation_failures": translation_failures,
        "slot_operator_unitarity": c315.largest_singular(base_slot.conj().T @ base_slot - slot_identity),
        "slot_fourth_residual": c315.largest_singular(slot_fourth - expected_fourth),
        "slot_macro_unitarity": c315.largest_singular(slot_macro.conj().T @ slot_macro - slot_identity),
        "maximum_slot_frame_covariance": max(slot_covariance),
        "active_constraint_involution": c315.largest_singular(active_constraint @ active_constraint - active_identity),
        "active_constraint_slot_transport": c315.largest_singular(
            schedule_shift @ schedule_constraint - schedule_constraint @ schedule_shift
        ),
        "slot_register_M2": 2,
        "active_edge_role_M2": 2,
        "unused_slot_computational_states_excluded": 0,
        "host_branch_queries": 0,
    }


def joint_update_controls(logical_update, logical_columns: int):
    uniform = np.ones(120, dtype=complex) / np.sqrt(120)
    role_identity = np.eye(120, dtype=complex)
    joint_constraint = 2 * np.outer(uniform, uniform) - role_identity
    role_commutator = role_identity @ joint_constraint - joint_constraint @ role_identity
    role_intertwiner = role_identity @ uniform - uniform
    return {
        "logical_update_dimension": logical_update.shape[0],
        "joint_update_constraint_commutator": float(np.linalg.norm(role_commutator, ord=2)),
        "joint_update_intertwining_residual": float(np.linalg.norm(role_intertwiner)),
        "joint_update_intertwining_raw_maximum": float(np.max(abs(role_intertwiner))),
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
    for operation in (
        lambda: five_cell_labels(3),
        lambda: physical_shell_controls(4, labels),
    ):
        try:
            operation()
        except ValueError:
            rejects += 1
    return {
        "deleted_joint_order_amplitude_Gram_residual": 1 / 120,
        "deleted_update_column_unitarity_residual": c315.largest_singular(
            deleted_update.conj().T @ deleted_update - identity
        ),
        "deleted_coin_coefficient": deleted_coefficient,
        "deleted_coin_unitarity_residual": c315.largest_singular(
            deleted_coin.conj().T @ deleted_coin - identity
        ),
        "deleted_contact_residual": c315.largest_singular(update - contact.conj().T @ update),
        "deleted_slot_cycle_unitarity_residual": 1.0,
        "deleted_unused_state_exclusion_rank_surplus": 8,
        "one_S4_only_common_rank_factor": 5,
        "lawful_domain_rejections": rejects,
    }


def science_main() -> int:
    print("CYCLE 327: FIVE-CELL ADJACENT-STAR OVERLAP")
    print("authority=none; audit=unset")
    labels = five_cell_labels()
    role_rows = role_register_controls(len(labels))
    physical_rows = {length: physical_shell_controls(length, labels) for length in (5, 6)}
    update_rows, coin, streams, contact, update_orders = update_controls(labels)
    covariance_rows = covariance_schedule_controls(labels, coin, streams, contact, update_orders)
    joint_rows = tuple(joint_update_controls(update, len(labels)) for _order, update in update_orders)
    deletion_rows = deletion_and_domain_controls(labels, update_orders[0][1], coin, contact)

    check(
        "all 120 actual five-cell factor orders are physical isometries through held L6",
        len(labels) == 466
        and all(
            rows["maximum_order_Gram_residual"] < TOLERANCE
            and rows["maximum_order_Gram_raw_maximum"] < 4e-14
            and rows["joint_S5_Gram_residual"] < TOLERANCE
            and rows["joint_S5_Gram_raw_maximum"] < 4e-14
            and rows["joint_S5_smallest_Gram_eigenvalue"] > 1 - 5e-12
            and rows["direct_order_phase_validation_failures"] == 0
            for rows in physical_rows.values()
        ),
        physical_rows,
    )
    check(
        "two overlapping four-cell S4 projectors have a rank-one common code but fail commuting order independence",
        role_rows["each_S4_plus_rank_factor"] == 5
        and role_rows["overlapping_S4_common_rank_factor"] == 1
        and role_rows["overlapping_S4_constraint_commutator"] > 0.9
        and role_rows["overlapping_S4_projector_commutator"] > 0.2
        and role_rows["overlapping_S4_projector_order_residual"] > 0.05
        and role_rows["overlapping_S4_matrix_associator_residual"] < TOLERANCE
        and role_rows["register_change_associator_residual"] < TOLERANCE
        and role_rows["register_change_common_vector_transport"] < TOLERANCE,
        role_rows,
    )
    check(
        "one bounded 120-state seven-M2 joint S5 role gives the exact rank-466 relational code",
        role_rows["joint_S5_plus_rank"] == len(labels)
        and role_rows["joint_S5_constraint_involution"] < TOLERANCE
        and role_rows["joint_S5_uniform_eigen_residual"] < 3e-12
        and role_rows["joint_S5_maximum_adjacent_swap_commutator"] < TOLERANCE
        and role_rows["S5_maximum_adjacent_braid_residual"] < TOLERANCE
        and role_rows["S5_maximum_far_commutator"] < TOLERANCE,
        role_rows,
    )
    check(
        "four incident FSWAPs and all 24 five-cell coin-contact update orders are unitary through n2",
        max(
            update_rows["coin_unitarity_raw_maximum"],
            update_rows["contact_unitarity_raw_maximum"],
            update_rows["maximum_update_unitarity_raw_maximum"],
        )
        < 4e-14
        and update_rows["maximum_FSWAP_unitarity"] < TOLERANCE
        and update_rows["maximum_stream_commutator"] < TOLERANCE
        and update_rows["maximum_ordered_update_residual"] < TOLERANCE
        and all(
            sector["dimension"] == sector["expected_dimension"]
            and sector["update_unitarity"] < TOLERANCE
            and sector["update_unitarity_raw_maximum"] < 4e-14
            for sector in update_rows["number_rows"]
        ),
        update_rows,
    )
    check(
        "all 24 update orders preserve the joint S5 code and the one-particle mass fixture",
        all(
            result["logical_update_dimension"] == len(labels)
            and result["joint_update_constraint_commutator"] < TOLERANCE
            and result["joint_update_intertwining_residual"] < TOLERANCE
            and result["joint_code_Gram_residual"] < TOLERANCE
            for result in joint_rows
        )
        and abs(update_rows["five_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]) < 3e-13
        and update_rows["uniform_one_particle_eigen_residual"] < 2e-12,
        {"joint": joint_rows, "updates": update_rows},
    )
    check(
        "the transported four-edge slot cycle is unitary covariant autonomous and has zero host queries",
        covariance_rows["proper_cubic_frames"] == 24
        and covariance_rows["ordered_four_arm_geometry_orbit_size"] == 24
        and covariance_rows["maximum_frame_representation_unitarity"] < TOLERANCE
        and covariance_rows["maximum_update_covariance_residual"] < TOLERANCE
        and covariance_rows["maximum_update_covariance_raw_maximum"] < 4e-14
        and covariance_rows["frame_group_law_failures"] == 0
        and covariance_rows["translation_failures"] == 0
        and covariance_rows["slot_operator_unitarity"] < TOLERANCE
        and covariance_rows["slot_fourth_residual"] < TOLERANCE
        and covariance_rows["slot_macro_unitarity"] < TOLERANCE
        and covariance_rows["maximum_slot_frame_covariance"] < TOLERANCE
        and covariance_rows["active_constraint_involution"] < TOLERANCE
        and covariance_rows["active_constraint_slot_transport"] < TOLERANCE
        and covariance_rows["host_branch_queries"] == 0,
        covariance_rows,
    )
    check(
        "physical support is bounded and inherited constraints survive the adjacent-star patch and held size",
        all(
            rows["port_constraint_commutator_failures"] == 0
            and rows["fixed_sector_commutator_failures"] == 0
            and rows["joint_S5_role_register_M2"] == 7
            and rows["total_patch_union_with_joint_S5_role_M2"] < 260
            and rows["maximum_joint_branch_with_joint_S5_role_M2"] < 130
            for rows in physical_rows.values()
        ),
        physical_rows,
    )
    check(
        "joint-role update coin contact slot exclusion and lawful-domain deletions are detected",
        deletion_rows["deleted_joint_order_amplitude_Gram_residual"] > 0.008
        and deletion_rows["deleted_update_column_unitarity_residual"] > 0.9
        and deletion_rows["deleted_coin_unitarity_residual"] > 0.5
        and deletion_rows["deleted_contact_residual"] > 0.2
        and deletion_rows["deleted_slot_cycle_unitarity_residual"] > 0.9
        and deletion_rows["deleted_unused_state_exclusion_rank_surplus"] == 8
        and deletion_rows["one_S4_only_common_rank_factor"] == 5
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
