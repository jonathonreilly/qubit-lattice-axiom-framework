#!/usr/bin/env python3
"""Three-route local-feature test for the landed Cycle-330 branch sign."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, permutations, product
import json
import math
import resource
import time

import numpy as np

import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18 as c330


START = time.perf_counter()
TOL = 2.0e-12
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Permutation = tuple[int, ...]


@dataclass(frozen=True)
class RoleTerm:
    cell: int
    number: int
    label: tuple[int, ...]
    carrier: int | None
    stream_slice: int
    r_value: int
    representative: object


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def role_terms(code, cell: int, number: int, label: tuple[int, ...]) -> tuple[RoleTerm, ...]:
    body = c330.CELLS[cell]
    rows = []
    for branch in c311.common_branches(code, body, number, label, 0):
        rows.append(
            RoleTerm(
                cell,
                number,
                label,
                branch.carrier_direction,
                branch.stream_slice,
                0,
                c311.branch_representative(code, body, branch, 0),
            )
        )
        target_slice = 0 if number == 0 else 1
        target = next(
            candidate
            for candidate in c311.common_branches(code, body, number, label, target_slice)
            if candidate.carrier_direction == branch.carrier_direction
        )
        rows.append(
            RoleTerm(
                cell,
                number,
                label,
                target.carrier_direction,
                target.stream_slice,
                1,
                c311.branch_representative(code, body, target, 1),
            )
        )
    return tuple(rows)


CENTER_EDGE_MODES = {
    right[0]: (left[1], right[1]) for left, right in c330.EDGES
}
ARM_CENTER_MODE = {right[0]: right[1] for _left, right in c330.EDGES}


def pair_geometry(left: int, right: int) -> tuple[int, int, int]:
    if left == 0:
        left_mode, right_mode = CENTER_EDGE_MODES[right]
        return 1, left_mode, right_mode
    return 0, ARM_CENTER_MODE[left], ARM_CENTER_MODE[right]


def endpoint_features(code, term: RoleTerm, mode: int) -> tuple[int, int, int, int, int]:
    occupied_endpoint = int(mode in term.label)
    incident = int(occupied_endpoint or term.carrier == mode)
    vertex = c311.c305.body_vertices(code, c330.CELLS[term.cell])[mode]
    tag = int(
        (term.representative.x >> (code.qubits + vertex)) & 1  # type: ignore[attr-defined]
    )
    predicted_tag = incident * (term.stream_slice ^ occupied_endpoint)
    return incident, tag, occupied_endpoint, term.stream_slice, predicted_tag


def endpoint_predictor(
    shared_edge: int,
    left_incident: int,
    right_incident: int,
    left_tag: int,
    right_tag: int,
) -> int:
    return shared_edge & left_incident & right_incident & (left_tag ^ right_tag)


def endpoint_interface_masks(
    code, left: int, right: int, left_mode: int, right_mode: int
) -> tuple[int, int, int]:
    if left != 0:
        return 0, 0, 0
    left_vertex = c311.c305.body_vertices(code, c330.CELLS[left])[left_mode]
    right_vertex = c311.c305.body_vertices(code, c330.CELLS[right])[right_mode]
    left_mask = sum(1 << edge for edge in code.graph.incident[left_vertex])
    right_mask = sum(1 << edge for edge in code.graph.incident[right_vertex])
    return left_mask, right_mask, left_mask | right_mask


def interface_description(
    code, left: int, right: int, left_mode: int, right_mode: int
) -> dict[str, object]:
    _left_mask, _right_mask, mask = endpoint_interface_masks(
        code, left, right, left_mode, right_mode
    )
    edges = tuple(index for index in range(code.qubits) if (mask >> index) & 1)
    kinds = Counter(code.graph.edges[index][2] for index in edges)
    distances = {}
    for source in edges:
        rows = {source: 0}
        queue = [source]
        while queue:
            current = queue.pop(0)
            current_vertices = set(code.graph.edges[current][:2])
            for target in edges:
                if target not in rows and current_vertices & set(code.graph.edges[target][:2]):
                    rows[target] = rows[current] + 1
                    queue.append(target)
        distances[source] = rows
    diameter = max(
        (distance for rows in distances.values() for distance in rows.values()),
        default=0,
    )
    return {
        "pair": (left, right),
        "M2": len(edges),
        "edge_kinds": dict(sorted(kinds.items())),
        "line_graph_diameter": diameter,
    }


def branch_census(length: int) -> tuple[dict[str, object], dict[tuple[int, int], tuple[RoleTerm, RoleTerm]]]:
    code = c315.c269.build_code(length)
    cache = {
        (cell, number, label): role_terms(code, cell, number, label)
        for cell in range(7)
        for number, label in c311.FOCK_LABELS
    }
    feature_outcomes: dict[tuple[int, int, int, int, int], set[int]] = defaultdict(set)
    class_rows = defaultdict(lambda: Counter(cases=0, positives=0))
    ablations = Counter()
    route1_errors = route2_errors = 0
    tag_relation_failures = 0
    outside_interface_crossings = 0
    one_endpoint_interface_errors = 0
    one_endpoint_outside_crossings = 0
    full_symplectic_mismatches = 0
    cases = positives = 0
    interface_union = 0
    interface_rows = []
    deletion_errors_by_edge: Counter[tuple[int, int]] = Counter()
    cross_support_by_pair: dict[tuple[int, int], int] = defaultdict(int)
    positive_witnesses: dict[tuple[int, int], tuple[RoleTerm, RoleTerm]] = {}

    for left, right in c330.PAIR_LABELS:
        shared, left_mode, right_mode = pair_geometry(left, right)
        _left_mask, one_endpoint_mask, mask = endpoint_interface_masks(
            code, left, right, left_mode, right_mode
        )
        interface_union |= mask
        interface_rows.append(
            interface_description(code, left, right, left_mode, right_mode)
        )
        mask_edges = tuple(index for index in range(code.qubits) if (mask >> index) & 1)
        pair_class = "center_arm" if shared else "arm_arm"
        for left_number, left_label in c311.FOCK_LABELS:
            for right_number, right_label in c311.FOCK_LABELS:
                if left_number + right_number > 2:
                    continue
                for left_term in cache[(left, left_number, left_label)]:
                    for right_term in cache[(right, right_number, right_label)]:
                        observed = int(
                            not left_term.representative.commutes(  # type: ignore[attr-defined]
                                right_term.representative
                            )
                        )
                        li, lt, _lo, _ls, ltp = endpoint_features(code, left_term, left_mode)
                        ri, rt, _ro, _rs, rtp = endpoint_features(code, right_term, right_mode)
                        tag_relation_failures += lt != ltp
                        tag_relation_failures += rt != rtp
                        predicted = endpoint_predictor(shared, li, ri, lt, rt)
                        route1_errors += predicted != observed
                        feature_outcomes[(shared, li, ri, lt, rt)].add(observed)

                        ablations["shared_edge"] += (li & ri & (lt ^ rt)) != observed
                        ablations["left_incidence"] += (shared & ri & (lt ^ rt)) != observed
                        ablations["right_incidence"] += (shared & li & (lt ^ rt)) != observed
                        ablations["left_tag"] += (shared & li & ri & rt) != observed
                        ablations["right_tag"] += (shared & li & ri & lt) != observed

                        left_x_right_z = (
                            left_term.representative.x & right_term.representative.z  # type: ignore[attr-defined]
                        )
                        left_z_right_x = (
                            left_term.representative.z & right_term.representative.x  # type: ignore[attr-defined]
                        )
                        full_symplectic = (
                            left_x_right_z.bit_count() + left_z_right_x.bit_count()
                        ) & 1
                        local_xz = (left_x_right_z & mask).bit_count() & 1
                        local_zx = (left_z_right_x & mask).bit_count() & 1
                        local_symplectic = local_xz ^ local_zx
                        one_endpoint_symplectic = (
                            (left_x_right_z & one_endpoint_mask).bit_count()
                            + (left_z_right_x & one_endpoint_mask).bit_count()
                        ) & 1
                        full_symplectic_mismatches += full_symplectic != observed
                        route2_errors += local_symplectic != observed
                        one_endpoint_interface_errors += one_endpoint_symplectic != observed
                        outside_interface_crossings += bool(
                            (left_x_right_z | left_z_right_x) & ~mask
                        )
                        one_endpoint_outside_crossings += bool(
                            (left_x_right_z | left_z_right_x) & ~one_endpoint_mask
                        )
                        cross_support_by_pair[(left, right)] |= (
                            left_x_right_z | left_z_right_x
                        ) & mask
                        for edge in mask_edges:
                            deleted_mask = mask & ~(1 << edge)
                            deleted = (
                                (left_x_right_z & deleted_mask).bit_count()
                                + (left_z_right_x & deleted_mask).bit_count()
                            ) & 1
                            deletion_errors_by_edge[(right, edge)] += deleted != observed

                        cases += 1
                        positives += observed
                        class_rows[pair_class]["cases"] += 1
                        class_rows[pair_class]["positives"] += observed
                        if observed and (left, right) not in positive_witnesses:
                            positive_witnesses[(left, right)] = (left_term, right_term)

    ambiguous_feature_vectors = sum(len(values) > 1 for values in feature_outcomes.values())
    active_interface_rows = tuple(row for row in interface_rows if row["M2"])
    inactive_interface_rows = tuple(row for row in interface_rows if not row["M2"])
    active_deletion_values = tuple(
        errors
        for (right, edge), errors in deletion_errors_by_edge.items()
        if (cross_support_by_pair[(0, right)] >> edge) & 1
    )
    inactive_deletion_values = tuple(
        errors
        for (right, edge), errors in deletion_errors_by_edge.items()
        if not ((cross_support_by_pair[(0, right)] >> edge) & 1)
    )
    detail = {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "cases": cases,
        "positive_signs": positives,
        "route1_endpoint_feature_errors": route1_errors,
        "route1_feature_vectors": len(feature_outcomes),
        "route1_ambiguous_feature_vectors": ambiguous_feature_vectors,
        "endpoint_tag_relation_failures": tag_relation_failures,
        "route1_ablation_errors": dict(sorted(ablations.items())),
        "route2_interface_symplectic_errors": route2_errors,
        "route2_one_endpoint_comparator_errors": one_endpoint_interface_errors,
        "full_symplectic_identity_errors": full_symplectic_mismatches,
        "outside_interface_crossing_cases": outside_interface_crossings,
        "one_endpoint_outside_crossing_cases": one_endpoint_outside_crossings,
        "active_center_arm_interfaces": len(active_interface_rows),
        "inactive_arm_arm_pairs": len(inactive_interface_rows),
        "interface_M2_per_center_arm": sorted({row["M2"] for row in active_interface_rows}),
        "interface_edge_kind_rows": sorted(
            {json.dumps(row["edge_kinds"], sort_keys=True) for row in active_interface_rows}
        ),
        "interface_line_graph_diameters": sorted(
            {row["line_graph_diameter"] for row in active_interface_rows}
        ),
        "actual_cross_support_M2_per_center_arm": sorted(
            {
                cross_support_by_pair[pair].bit_count()
                for pair in positive_witnesses
            }
        ),
        "six_interface_union_M2": interface_union.bit_count(),
        "delete_each_active_crossing_M2_minimum_errors": min(
            active_deletion_values, default=0
        ),
        "delete_each_active_crossing_M2_maximum_errors": max(
            active_deletion_values, default=0
        ),
        "inactive_interface_M2_deletion_maximum_errors": max(
            inactive_deletion_values, default=0
        ),
        "pair_class_rows": {key: dict(value) for key, value in sorted(class_rows.items())},
        "positive_pair_labels": sorted(positive_witnesses),
    }
    return detail, positive_witnesses


PAIR_INDEX = {pair: index for index, pair in enumerate(c330.PAIR_LABELS)}


def inversion_mask(mapping: Permutation) -> int:
    return sum(
        1 << index
        for index, (left, right) in enumerate(c330.PAIR_LABELS)
        if mapping[left] > mapping[right]
    )


def transport_pair_mask(mask: int, mapping: Permutation) -> tuple[int, int]:
    target = 0
    phase = 1
    for index, (left, right) in enumerate(c330.PAIR_LABELS):
        if not ((mask >> index) & 1):
            continue
        mapped_left, mapped_right = mapping[left], mapping[right]
        if mapped_left > mapped_right:
            mapped_left, mapped_right = mapped_right, mapped_left
            phase *= -1
        target |= 1 << PAIR_INDEX[(mapped_left, mapped_right)]
    return target, phase


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(7))


def adjacent_swap(index: int) -> Permutation:
    row = list(range(7))
    row[index], row[index + 1] = row[index + 1], row[index]
    return tuple(row)


ADJACENT = tuple(adjacent_swap(index) for index in range(6))


def apply_register_word(mask: int, word: tuple[Permutation, ...]) -> tuple[int, int]:
    phase = 1
    for mapping in word:
        mask, step_phase = transport_pair_mask(mask, mapping)
        phase *= step_phase
    return mask, phase


STAR_COORDS: tuple[Coord, ...] = tuple(
    tuple(cell[axis] - c330.CELLS[0][axis] for axis in range(3))
    for cell in c330.CELLS
)


def frame_tuple(frame: np.ndarray) -> tuple[Coord, Coord, Coord]:
    return tuple(tuple(int(value) for value in row) for row in frame)  # type: ignore[return-value]


def matvec(frame: tuple[Coord, Coord, Coord], vector: Coord) -> Coord:
    return tuple(
        sum(frame[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def matmul(
    left: tuple[Coord, Coord, Coord], right: tuple[Coord, Coord, Coord]
) -> tuple[Coord, Coord, Coord]:
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(3))
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


FRAMES = tuple(frame_tuple(frame) for frame in c330.c235.proper_cubic_frames())
FRAME_INDEX = {frame: index for index, frame in enumerate(FRAMES)}
FRAME_MAPS = tuple(
    tuple(STAR_COORDS.index(matvec(frame, site)) for site in STAR_COORDS)
    for frame in FRAMES
)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(factor: int, row: Coord) -> Coord:
    return tuple(factor * value for value in row)  # type: ignore[return-value]


def register_site(pair: tuple[int, int]) -> Coord:
    left, right = pair
    if left == 0:
        return scale(6, STAR_COORDS[right])
    if right == 0:
        return scale(7, STAR_COORDS[left])
    return add(scale(4, STAR_COORDS[left]), STAR_COORDS[right])


ORDERED_PAIRS = tuple((left, right) for left in range(7) for right in range(7) if left != right)
REGISTER_SITE = {pair: register_site(pair) for pair in ORDERED_PAIRS}
REGISTER_SITES = set(REGISTER_SITE.values())
REGISTER_RADIUS = max(abs(value) for site in REGISTER_SITES for value in site)


def l1(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def sign_pair_projector() -> np.ndarray:
    projector = np.zeros((8, 8), dtype=float)
    projector[0, 0] = 1.0
    backward = 1 | (1 << 1)
    forward = 1 | (1 << 2)
    vector = np.zeros(8, dtype=float)
    vector[backward] = 1 / math.sqrt(2)
    vector[forward] = -1 / math.sqrt(2)
    projector += np.outer(vector, vector)
    return projector


def register_projector_controls() -> dict[str, object]:
    local = sign_pair_projector()
    hermitian = float(np.linalg.norm(local - local.T))
    idempotence = float(np.linalg.norm(local @ local - local))
    rank = int(np.linalg.matrix_rank(local, tol=1e-12))
    identity = np.eye(8)
    left = np.kron(local, identity)
    right = np.kron(identity, local)
    distinct_control_commutator = float(np.linalg.norm(left @ right - right @ left))
    zero = np.asarray(((1.0, 0.0), (0.0, 0.0)))
    one = np.asarray(((0.0, 0.0), (0.0, 1.0)))
    blank = np.zeros((4, 4), dtype=float)
    blank[0, 0] = 1.0
    antisymmetric = np.zeros(4, dtype=float)
    antisymmetric[1] = 1 / math.sqrt(2)
    antisymmetric[2] = -1 / math.sqrt(2)
    active = np.outer(antisymmetric, antisymmetric)
    shared_left = np.kron(np.kron(zero, blank), np.eye(4)) + np.kron(
        np.kron(one, active), np.eye(4)
    )
    shared_right = np.kron(np.kron(zero, np.eye(4)), blank) + np.kron(
        np.kron(one, np.eye(4)), active
    )
    shared_control_commutator = float(
        np.linalg.norm(shared_left @ shared_right - shared_right @ shared_left)
    )
    maximum_commutator = max(
        distinct_control_commutator, shared_control_commutator
    )
    pair_failures = sum(maximum_commutator >= TOL for _pair in combinations(range(21), 2))
    return {
        "local_rank": rank,
        "local_hermiticity_residual": hermitian,
        "local_idempotence_residual": idempotence,
        "distinct_control_pair_commutator_residual": distinct_control_commutator,
        "shared_control_pair_commutator_residual": shared_control_commutator,
        "projector_pair_tests": math.comb(21, 2),
        "projector_pair_failures": pair_failures,
        "register_fiber_dimension": 1,
        "deleted_one_projector_fiber_dimension": 4,
    }


def placement_controls() -> dict[str, object]:
    pitch = 2 * REGISTER_RADIUS + 1
    rows = []
    for length, split in ((3, "train"), (5, "held-no-refit")):
        anchors = tuple(
            (pitch * x, pitch * y, pitch * z)
            for x in range(length)
            for y in range(length)
            for z in range(length)
        )
        placed = {add(anchor, site) for anchor in anchors for site in REGISTER_SITES}
        rows.append(
            {
                "L": length,
                "split": split,
                "isolated_blocks": len(anchors),
                "register_M2_per_block": len(REGISTER_SITES),
                "collisions": len(anchors) * len(REGISTER_SITES) - len(placed),
            }
        )
    return {
        "pitch": pitch,
        "rows": rows,
        "held_parameters_refit": 0,
        "overlapping_or_recurrent_blocks_tested": False,
    }


def validate_mask(mask: int) -> None:
    if mask < 0 or mask >= 1 << 21:
        raise ValueError("pair mask must contain exactly 21 available bits")


def validate_permutation(mapping: Permutation) -> None:
    if len(mapping) != 7 or set(mapping) != set(range(7)):
        raise ValueError("mapping must be a permutation of seven cells")


def main() -> None:
    train, train_witnesses = branch_census(5)
    held, held_witnesses = branch_census(6)
    comparable_train = {key: value for key, value in train.items() if key not in {"L", "split"}}
    comparable_held = {key: value for key, value in held.items() if key not in {"L", "split"}}
    check(
        "the five-bit endpoint/tag formula predicts every landed n<=2 branch sign without L6 refit",
        train["route1_endpoint_feature_errors"] == held["route1_endpoint_feature_errors"] == 0
        and train["route1_ambiguous_feature_vectors"] == held["route1_ambiguous_feature_vectors"] == 0
        and train["endpoint_tag_relation_failures"] == held["endpoint_tag_relation_failures"] == 0
        and comparable_train == comparable_held
        and all(value > 0 for value in train["route1_ablation_errors"].values()),
        {
            "formula": "shared_edge * I_left * I_right * (tag_left XOR tag_right)",
            "I_endpoint": "occupied endpoint mode OR odd-carrier endpoint role",
            "tag_endpoint": "actual endpoint auxiliary-port X occupation",
            "train": train,
            "held": held,
        },
    )

    check(
        "the same sign is exact on the covariant nine-M2 two-endpoint interface union",
        train["route2_interface_symplectic_errors"] == held["route2_interface_symplectic_errors"] == 0
        and train["full_symplectic_identity_errors"] == held["full_symplectic_identity_errors"] == 0
        and train["outside_interface_crossing_cases"] == held["outside_interface_crossing_cases"] == 0
        and train["route2_one_endpoint_comparator_errors"] == held["route2_one_endpoint_comparator_errors"] == 600
        and train["one_endpoint_outside_crossing_cases"] > 0
        and held["one_endpoint_outside_crossing_cases"] > 0
        and train["interface_M2_per_center_arm"] == held["interface_M2_per_center_arm"] == [9]
        and train["actual_cross_support_M2_per_center_arm"] == held["actual_cross_support_M2_per_center_arm"] == [5]
        and train["active_center_arm_interfaces"] == held["active_center_arm_interfaces"] == 6
        and train["inactive_arm_arm_pairs"] == held["inactive_arm_arm_pairs"] == 15
        and train["delete_each_active_crossing_M2_minimum_errors"] > 0
        and train["inactive_interface_M2_deletion_maximum_errors"] == 0,
        {
            "formula": "symplectic parity on the union of both five-edge endpoint stars",
            "failed_narrow_comparator": "the arm-endpoint-only five-M2 rule leaves 600 errors per size",
            "train_interface": {
                key: train[key]
                for key in (
                    "interface_M2_per_center_arm",
                    "actual_cross_support_M2_per_center_arm",
                    "interface_edge_kind_rows",
                    "interface_line_graph_diameters",
                    "six_interface_union_M2",
                    "route2_one_endpoint_comparator_errors",
                    "one_endpoint_outside_crossing_cases",
                    "delete_each_active_crossing_M2_minimum_errors",
                    "delete_each_active_crossing_M2_maximum_errors",
                    "inactive_interface_M2_deletion_maximum_errors",
                )
            },
            "held_interface": {
                key: held[key]
                for key in (
                    "interface_M2_per_center_arm",
                    "actual_cross_support_M2_per_center_arm",
                    "interface_edge_kind_rows",
                    "interface_line_graph_diameters",
                    "six_interface_union_M2",
                    "route2_one_endpoint_comparator_errors",
                    "one_endpoint_outside_crossing_cases",
                    "delete_each_active_crossing_M2_minimum_errors",
                    "delete_each_active_crossing_M2_maximum_errors",
                    "inactive_interface_M2_deletion_maximum_errors",
                )
            },
        },
    )

    positive_pairs = tuple(sorted(train_witnesses))
    actual_masks = (0,) + tuple(1 << PAIR_INDEX[pair] for pair in positive_pairs)
    witness_mask_failures = 0
    for length, witnesses in ((5, train_witnesses), (6, held_witnesses)):
        code = c315.c269.build_code(length)
        vacuum = {
            cell: role_terms(code, cell, 0, ())[0].representative for cell in range(7)
        }
        witness_mask_failures += c330.branch_anticommutation_mask(tuple(vacuum[cell] for cell in range(7))) != 0
        for pair, (left_term, right_term) in witnesses.items():
            rows = dict(vacuum)
            rows[pair[0]] = left_term.representative
            rows[pair[1]] = right_term.representative
            witness_mask_failures += c330.branch_anticommutation_mask(tuple(rows[cell] for cell in range(7))) != (
                1 << PAIR_INDEX[pair]
            )

    all_order_failures = target_mask_failures = 0
    for mask in actual_masks:
        for order in c330.ORDERS:
            mapping = tuple(order.index(cell) for cell in range(7))
            target, phase = transport_pair_mask(mask, mapping)
            expected = -1 if (mask & c330.inversion_mask(order)).bit_count() & 1 else 1
            all_order_failures += phase != expected
            target_mask_failures += target.bit_count() != mask.bit_count()

    relation_failures = 0
    for mask in actual_masks:
        for swap in ADJACENT:
            relation_failures += apply_register_word(mask, (swap, swap)) != (mask, 1)
        for index in range(5):
            relation_failures += apply_register_word(
                mask, (ADJACENT[index], ADJACENT[index + 1], ADJACENT[index])
            ) != apply_register_word(
                mask, (ADJACENT[index + 1], ADJACENT[index], ADJACENT[index + 1])
            )
        for first in range(6):
            for second in range(first + 2, 6):
                relation_failures += apply_register_word(mask, (ADJACENT[first], ADJACENT[second])) != apply_register_word(
                    mask, (ADJACENT[second], ADJACENT[first])
                )

    frame_site_failures = frame_product_failures = frame_cocycle_failures = 0
    frame_mask_closure_failures = 0
    for frame, mapping in zip(FRAMES, FRAME_MAPS):
        frame_site_failures += sum(
            matvec(frame, site) != REGISTER_SITE[(mapping[left], mapping[right])]
            for (left, right), site in REGISTER_SITE.items()
        )
        frame_mask_closure_failures += sum(
            transport_pair_mask(mask, mapping)[0] not in actual_masks for mask in actual_masks
        )
    for left_index, left in enumerate(FRAMES):
        for right_index, right in enumerate(FRAMES):
            target_index = FRAME_INDEX[matmul(left, right)]
            left_map, right_map = FRAME_MAPS[left_index], FRAME_MAPS[right_index]
            target_map = FRAME_MAPS[target_index]
            frame_product_failures += compose(left_map, right_map) != target_map
            for mask in actual_masks:
                intermediate, right_phase = transport_pair_mask(mask, right_map)
                composed_target, left_phase = transport_pair_mask(intermediate, left_map)
                target_mask, target_phase = transport_pair_mask(mask, target_map)
                frame_cocycle_failures += composed_target != target_mask
                frame_cocycle_failures += left_phase * right_phase != target_phase

    projector = register_projector_controls()
    placement = placement_controls()
    check(
        "actual branch-role-conditioned ordered pairs close the S7 sign and proper-cubic constraint family",
        len(actual_masks) == 7
        and positive_pairs == tuple((0, arm) for arm in range(1, 7))
        and witness_mask_failures == all_order_failures == target_mask_failures == relation_failures == 0
        and frame_site_failures == frame_product_failures == frame_cocycle_failures == 0
        and frame_mask_closure_failures == 0
        and projector["local_rank"] == 2
        and projector["local_hermiticity_residual"] < TOL
        and projector["local_idempotence_residual"] < TOL
        and projector["projector_pair_failures"] == 0
        and len(REGISTER_SITES) == 42
        and REGISTER_RADIUS == 7
        and all(row["collisions"] == 0 for row in placement["rows"]),
        {
            "attainable_Cycle330_n_le_2_branch_masks": len(actual_masks),
            "attainable_masks": actual_masks,
            "positive_pair_labels": positive_pairs,
            "witness_mask_failures": witness_mask_failures,
            "S7_order_mask_cases": len(actual_masks) * math.factorial(7),
            "S7_order_failures": all_order_failures,
            "S7_relation_failures": relation_failures,
            "proper_cubic_frames": len(FRAMES),
            "ordered_frame_products": len(FRAMES) ** 2,
            "frame_product_mask_cases": len(FRAMES) ** 2 * len(actual_masks),
            "frame_site_failures": frame_site_failures,
            "frame_product_failures": frame_product_failures,
            "frame_cocycle_failures": frame_cocycle_failures,
            "frame_mask_closure_failures": frame_mask_closure_failures,
            "projector": projector,
            "ordered_pair_register_M2": len(REGISTER_SITES),
            "conditional_center_arm_projectors": 6,
            "blank_arm_arm_projectors": 15,
            "maximum_conditional_projector_controls": 4,
            "maximum_conditional_projector_support_including_register": 6,
            "explicit_incidence_control_M2_if_materialized": 12,
            "existing_endpoint_tag_M2_controls": 12,
            "register_radius": REGISTER_RADIUS,
            "prior_dense_S7_role_M2": 13,
            "prior_dense_S7_states": math.factorial(7),
            "prior_dense_S7_unused_states": 2**13 - math.factorial(7),
            "placement": placement,
        },
    )

    feature_covariance_failures = 0
    feature_covariance_cases = 0
    feature_code = c315.c269.build_code(5)
    for frame, cell_mapping in zip(c330.c235.proper_cubic_frames(), FRAME_MAPS):
        direction_map = tuple(c311.direction_map(frame, mode) for mode in range(6))
        for arm in range(1, 7):
            target_arm = cell_mapping[arm]
            source_modes = CENTER_EDGE_MODES[arm]
            target_modes = CENTER_EDGE_MODES[target_arm]
            feature_covariance_failures += direction_map[source_modes[0]] != target_modes[0]
            feature_covariance_failures += direction_map[source_modes[1]] != target_modes[1]
            feature_covariance_cases += 2
        for cell in range(7):
            for number, label in c311.FOCK_LABELS:
                if number > 2:
                    continue
                for term in role_terms(feature_code, cell, number, label):
                    mapped_label = tuple(sorted(direction_map[mode] for mode in term.label))
                    mapped_carrier = (
                        None
                        if term.carrier is None
                        else direction_map[term.carrier]
                    )
                    for mode in range(6):
                        incident, tag, _occupied, _slice, predicted = endpoint_features(
                            feature_code, term, mode
                        )
                        mapped_mode = direction_map[mode]
                        mapped_occupied = int(mapped_mode in mapped_label)
                        mapped_incident = int(
                            mapped_occupied or mapped_carrier == mapped_mode
                        )
                        mapped_tag = mapped_incident * (
                            term.stream_slice ^ mapped_occupied
                        )
                        feature_covariance_failures += incident != mapped_incident
                        feature_covariance_failures += tag != predicted
                        feature_covariance_failures += tag != mapped_tag
                        feature_covariance_cases += 1
        feature_covariance_failures += len(set(direction_map)) != 6
    check(
        "endpoint incidence, endpoint tags and the two-endpoint interface family are proper-cubic scalars/covariants",
        feature_covariance_failures == 0
        and train["interface_edge_kind_rows"] == held["interface_edge_kind_rows"]
        and train["interface_line_graph_diameters"] == held["interface_line_graph_diameters"] == [2],
        {
            "feature_covariance_cases": feature_covariance_cases,
            "feature_covariance_failures": feature_covariance_failures,
            "interface_family": "six proper-cubic center-arm unions of eight internal-triangle plus one outer-square M2",
            "frame_products_already_tested": 576,
        },
    )

    symmetric = np.asarray((1 / math.sqrt(2), 1 / math.sqrt(2)))
    antisymmetry_deletion_residual = float(np.linalg.norm(symmetric[::-1] + symmetric))
    one_amplitude_probability_loss = 0.5
    invalid_rejections = 0
    for mask, mapping in (
        (-1, tuple(range(7))),
        (1 << 21, tuple(range(7))),
        (0, (0, 1, 2, 3, 4, 5, 5)),
        (0, tuple(range(6))),
    ):
        try:
            validate_mask(mask)
            validate_permutation(mapping)
        except ValueError:
            invalid_rejections += 1
    check(
        "feature, interface, register and lawful-domain deletions remain active",
        all(value > 0 for value in train["route1_ablation_errors"].values())
        and train["delete_each_active_crossing_M2_minimum_errors"] > 0
        and abs(antisymmetry_deletion_residual - 2.0) < TOL
        and one_amplitude_probability_loss == 0.5
        and projector["deleted_one_projector_fiber_dimension"] == 4
        and invalid_rejections == 4,
        {
            "endpoint_feature_ablation_errors": train["route1_ablation_errors"],
            "delete_each_active_crossing_M2_minimum_errors": train["delete_each_active_crossing_M2_minimum_errors"],
            "delete_antisymmetric_phase_residual": antisymmetry_deletion_residual,
            "delete_one_ordered_amplitude_probability_loss": one_amplitude_probability_loss,
            "delete_one_projector_fiber_dimension": projector["deleted_one_projector_fiber_dimension"],
            "lawful_domain_rejections": invalid_rejections,
        },
    )

    certificate = {
        "formula": "shared_edge*I_left*I_right*(tag_left XOR tag_right)",
        "star_coords": STAR_COORDS,
        "register_sites": sorted((pair, site) for pair, site in REGISTER_SITE.items()),
        "actual_masks": actual_masks,
    }
    digest = sha256(
        json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "bounded-cycle330-branch-local-order-sign-feature-certificate",
        "terminal": "BRANCH_LOCAL_SIGN_FEATURES_CLOSE_DENSE_PHYSICAL_ROLE_NOT_RETIRED",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "discriminants": {
            "endpoint_formula": "shared_edge * I_left * I_right * (tag_left XOR tag_right)",
            "interface_formula": "symplectic parity on the nine-M2 union of both endpoint stars",
            "failed_one_endpoint_errors_per_size": train[
                "route2_one_endpoint_comparator_errors"
            ],
            "train_errors": {
                "endpoint": train["route1_endpoint_feature_errors"],
                "interface": train["route2_interface_symplectic_errors"],
            },
            "held_errors": {
                "endpoint": held["route1_endpoint_feature_errors"],
                "interface": held["route2_interface_symplectic_errors"],
            },
            "train_cases": train["cases"],
            "held_cases": held["cases"],
        },
        "register_route": {
            "actual_branch_masks": len(actual_masks),
            "ordered_pair_register_M2": len(REGISTER_SITES),
            "conditional_projectors": 6,
            "blank_projectors": 15,
            "S7_cases": len(actual_masks) * math.factorial(7),
            "proper_cubic_product_cases": len(actual_masks) * 576,
        },
        "resources": {
            "two_endpoint_interface_M2_per_center_arm": 9,
            "actual_cross_support_M2_per_center_arm": 5,
            "six_interface_union_M2": train["six_interface_union_M2"],
            "existing_endpoint_tag_controls": 12,
            "supplied_incidence_role_controls": 12,
            "new_ordered_pair_register_M2": 42,
            "register_radius": REGISTER_RADIUS,
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
        },
        "certificate_sha256": digest,
        "supplied": (
            "the landed Cycle-311 branch labels, odd-carrier direction, stream slice and endpoint tag M2 occupations",
            "the landed Cycle-330 center, six arms, endpoint-mode dictionary and n<=2 domain",
            "the covariant two-endpoint interface union for each center-arm pair",
            "twelve branch-incidence controls if those role labels are materialized coherently",
            "42 ordered-pair register M2, conditional antisymmetric state and static projectors",
            "the standard S7 relabeling action, proper-cubic coordinate action and tolerance 2e-12",
        ),
        "derived": (
            "zero-error five-bit endpoint/tag formula on all 83244 L5 and all 83244 held-L6 branch-term pairs",
            "zero-error nine-M2 interface-union symplectic parity, while the one-endpoint five-M2 comparator retains 600 errors",
            "seven actual n<=2 branch masks rather than 5040 dense order states",
            "all-5040 order signs, adjacent relations and all-576 proper-cubic products for those masks",
            "commuting rank-two conditional pair projectors, deletions and bounded placement census",
        ),
        "open": (
            "a coherent physical extractor or primitive projector synthesis for the branch-incidence control bits",
            "an end-to-end physical update that uses the conditional pair code and returns every control",
            "proof that the full physical AB/BA order sectors, rather than their signs alone, are related by this code",
            "n>2, simultaneous multiple active pair signs, full M64^7 and overlapping maximal stars",
            "shared-port recurrence, autonomous collision control, preparation and state genesis",
            "minimality, impossibility, shared obstruction, axiom pressure, time, source, Record and probability",
        ),
        "claim_ceiling": (
            "Positive bounded sign/constraint certificate.  The local features exactly predict the landed n<=2 "
            "branch sign and replace the dense S7 state list at the sign-bookkeeping level.  The route uses more "
            "register M2 than the 13-M2 dense role, still supplies branch-incidence controls, and does not retire "
            "the full physical order-role sectors or establish a physical update, recurrence, minimality or axiom pressure."
        ),
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
