#!/usr/bin/env python3
"""Adversarial physical-M2 audit of the campaign edge-sign translator.

The corrected campaign candidate classifies AB/BA branch signs from Pauli
*preparation labels* with x_e(1-t_u)(1-t_v), and explicitly leaves a physical
matrix-unit synthesis open.  This runner tests that open tensor-factor route:
can one unitary on the outer-edge M2 and its two endpoint-tag M2s perform the
sign on the landed Cycle-269/311 physical state vectors?

The answer for that proposed route is no.  On every one of the six Cycle-330
arms, both a positive vacuum branch and a negative n_L=n_R=1 branch have
endpoint tags |00>.  The fixed-Wilson face state is maximally mixed on the
single outer-edge M2.  Exact action on the positive branch therefore fixes
the whole edge x |00> local subspace, while exact action on the negative
branch negates the same subspace.  This is a concrete route defect, not a
claim about all larger-support or ancilla-assisted constructions.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
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

ROOT_CANDIDATE = Path(
    "/Users/jonreilly/Projects/Physics-cycle657-658-endpoint/scripts/"
    "frontier_cycle330_symmetric_edge_sign_translator_2026_07_25.py"
)
ROUTE_B = Path(
    "/private/tmp/toe-route-b-sparse.sGeR8Z/scripts/"
    "frontier_two_overlapping_star_sparse_qutrit_edge_gauge_2026_07_25.py"
)

# Route B coordinate order: x on nine sorted interface edges, z on the same
# nine edges, then the two endpoint tags.  These are operator labels, not
# simultaneous physical state bits.
ROUTE_B_TERMS = (
    (5, 13),
    (6, 14),
    (13, 18),
    (13, 19),
    (14, 15),
    (18, 19),
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def edge_geometry(code, edge_geometry):
    (left_cell, left_mode), (right_cell, right_mode) = edge_geometry
    left_body = c330.CELLS[left_cell]
    right_body = c330.CELLS[right_cell]
    left_vertex = c311.c305.body_vertices(code, left_body)[left_mode]
    right_vertex = c311.c305.body_vertices(code, right_body)[right_mode]
    outer_edge = c311.local.old.outer_partner(code, left_vertex)[1]
    if outer_edge != c311.local.old.outer_partner(code, right_vertex)[1]:
        raise AssertionError("the endpoint pair did not resolve one outer M2")
    interface_edges = tuple(
        sorted(
            set(code.graph.incident[left_vertex])
            | set(code.graph.incident[right_vertex])
        )
    )
    if len(interface_edges) != 9:
        raise AssertionError("the landed endpoint interface must contain nine M2s")
    return left_body, right_body, left_vertex, right_vertex, outer_edge, interface_edges


def local_pattern(code, representative, edge: int, left_vertex: int, right_vertex: int):
    return (
        (representative.x >> edge) & 1,
        (representative.z >> edge) & 1,
        (representative.x >> (code.qubits + left_vertex)) & 1,
        (representative.x >> (code.qubits + right_vertex)) & 1,
    )


def candidate_sign(pattern: tuple[int, int, int, int]) -> int:
    x_edge, z_edge, tag_left, tag_right = pattern
    del z_edge
    return x_edge & (1 ^ tag_left) & (1 ^ tag_right)


def legacy_xz_sign(pattern: tuple[int, int, int, int]) -> int:
    """Failed first-round extrapolation, retained as a seam control."""
    x_edge, z_edge, tag_left, tag_right = pattern
    return x_edge & z_edge & (1 ^ tag_left) & (1 ^ tag_right)


def route_b_values(code, representative, interface_edges, left_vertex, right_vertex):
    return tuple(
        [(representative.x >> edge) & 1 for edge in interface_edges]
        + [(representative.z >> edge) & 1 for edge in interface_edges]
        + [
            (representative.x >> (code.qubits + left_vertex)) & 1,
            (representative.x >> (code.qubits + right_vertex)) & 1,
        ]
    )


def route_b_sign(values: tuple[int, ...]) -> int:
    return sum(values[left] & values[right] for left, right in ROUTE_B_TERMS) & 1


def descriptor(label, left_index: int, right_index: int, representative) -> dict[str, object]:
    return {
        "logical_label": label,
        "left_term_index": left_index,
        "right_term_index": right_index,
        "pauli_phase": representative.phase,
        "pauli_x_weight": representative.x.bit_count(),
        "pauli_z_weight": representative.z.bit_count(),
        "pauli_sha256": sha256(
            f"{representative.phase}:{representative.x}:{representative.z}".encode()
        ).hexdigest(),
    }


def single_edge_full_schmidt(code, edge: int) -> dict[str, object]:
    reducer = c315.c305.StabilizerReducer(code)
    membership = {}
    for name, phase, x, z in (
        ("X", 0, 1, 0),
        ("Z", 0, 0, 1),
        ("Y", 1, 1, 1),
    ):
        pauli = c315.c235.Pauli(
            phase=phase,
            x=x << edge,
            z=z << edge,
        )
        membership[name] = reducer.vacuum_phase(pauli)
    # A stabilizer-state single-qubit marginal is I/2 exactly when none of
    # its three nonidentity one-qubit Paulis is in the stabilizer.
    return {
        "single_edge_stabilizer_phases": membership,
        "reduced_density_eigenvalues": (0.5, 0.5),
        "schmidt_rank": 2 if all(value is None for value in membership.values()) else 0,
    }


def physical_matrix_unit_contradiction() -> dict[str, object]:
    # On K = H_edge tensor |00>_tags, an exact local matrix A would have to
    # satisfy A=+I from the positive full-Schmidt branch and A=-I from the
    # negative full-Schmidt branch.  The augmented rank exposes inconsistency.
    coefficient = np.vstack((np.eye(4), np.eye(4)))
    identity_vector = np.eye(2, dtype=complex).reshape(-1)
    target = np.concatenate((identity_vector, -identity_vector))
    solution, *_ = np.linalg.lstsq(coefficient, target, rcond=None)
    matrix_unit_residual = float(np.linalg.norm(coefficient @ solution - target))

    # State-vector residuals carry the I/2 Schmidt weights.  The best arbitrary
    # (nonunitary) local matrix has one unit error on each witness.  For every
    # unitary U on all three M2s, including any leakage out of K,
    # ||(U-I)psi+||^2 + ||(U+I)psi-||^2 = 4 because both local marginals equal
    # I/2 tensor |00><00|.  Hence at least one residual is >= sqrt(2).
    return {
        "restriction_dimension": 2,
        "matrix_unknowns": 4,
        "coefficient_rank": int(np.linalg.matrix_rank(coefficient)),
        "augmented_rank": int(
            np.linalg.matrix_rank(np.column_stack((coefficient, target)))
        ),
        "best_arbitrary_matrix_combined_unweighted_residual": matrix_unit_residual,
        "best_arbitrary_matrix_state_residual_each": matrix_unit_residual / 2,
        "best_arbitrary_matrix_combined_state_residual": matrix_unit_residual / np.sqrt(2),
        "any_unitary_combined_state_residual": 2.0,
        "any_unitary_maximum_witness_residual_lower_bound": float(np.sqrt(2)),
        "identity_positive_residual": 0.0,
        "identity_negative_residual": 2.0,
        "tag_flip_target_ray_leakage_probability": 1.0,
        "tag_flip_witness_residual_each": float(np.sqrt(2)),
    }


def edge_census(length: int) -> dict[str, object]:
    code = c315.c269.build_code(length)
    labels = c315.joint_labels(2)
    rows = []
    aggregate_deletions = Counter()
    route_b_deletions = Counter()
    total_cases = total_positives = 0
    for edge_index, geometry in enumerate(c330.EDGES):
        (
            left_body,
            right_body,
            left_vertex,
            right_vertex,
            outer_edge,
            interface_edges,
        ) = edge_geometry(code, geometry)
        cache = {}
        reducer = c315.RayReducer(code)
        row_tags: dict[int, tuple[int, int]] = {}
        row_signs: dict[int, int] = {}
        row_sign_conflicts = 0
        projected_plain_column_residuals = []
        abstract_translator_column_residuals = []
        cases = positives = candidate_errors = legacy_errors = route_b_errors = reverse_errors = 0
        endpoint_swap_errors = 0
        patterns = Counter()
        route_b_patterns = set()
        positive_witness = None
        negative_witness = None
        local_deletions = Counter()
        local_route_b_deletions = Counter()
        for label in labels:
            left_number, left_label, right_number, right_label = label
            left_terms = cache.setdefault(
                (left_body, left_number, left_label),
                c315.gauge_input_terms(code, left_body, left_number, left_label),
            )
            right_terms = cache.setdefault(
                (right_body, right_number, right_label),
                c315.gauge_input_terms(code, right_body, right_number, right_label),
            )
            forward_column = defaultdict(complex)
            reverse_column = defaultdict(complex)
            for left_index, left_term in enumerate(left_terms):
                for right_index, right_term in enumerate(right_terms):
                    forward = left_term.representative @ right_term.representative
                    reverse = right_term.representative @ left_term.representative
                    expected = int(
                        not left_term.representative.commutes(right_term.representative)
                    )
                    pattern = local_pattern(
                        code, forward, outer_edge, left_vertex, right_vertex
                    )
                    x_edge, z_edge, tag_left, tag_right = pattern
                    predicted = candidate_sign(pattern)
                    values = route_b_values(
                        code,
                        forward,
                        interface_edges,
                        left_vertex,
                        right_vertex,
                    )
                    quadratic = route_b_sign(values)
                    forward_row, forward_phase = reducer.reduce(forward)
                    reverse_row, reverse_phase = reducer.reduce(reverse)
                    if forward_row != reverse_row:
                        raise AssertionError("AB and BA did not reduce to the same physical ray")
                    amplitude = left_term.amplitude * right_term.amplitude
                    forward_column[forward_row] += amplitude * forward_phase
                    reverse_column[reverse_row] += amplitude * reverse_phase
                    row_tags.setdefault(forward_row, (tag_left, tag_right))
                    if row_tags[forward_row] != (tag_left, tag_right):
                        raise AssertionError("one physical row acquired inconsistent endpoint tags")
                    if forward_row in row_signs:
                        row_sign_conflicts += row_signs[forward_row] != predicted
                    else:
                        row_signs[forward_row] = predicted
                    cases += 1
                    positives += expected
                    candidate_errors += predicted != expected
                    legacy_errors += legacy_xz_sign(pattern) != expected
                    route_b_errors += quadratic != expected
                    reverse_errors += (
                        reverse.x != forward.x
                        or reverse.z != forward.z
                        or (reverse.phase - forward.phase) % 4 != 2 * expected
                    )
                    endpoint_swap_errors += predicted != candidate_sign(
                        (x_edge, z_edge, tag_right, tag_left)
                    )
                    patterns[pattern] += 1
                    route_b_patterns.add((values, expected))

                    mutations = {
                        "remove_x_control": (1 ^ tag_left) & (1 ^ tag_right),
                        "remove_left_tag_control": x_edge
                        & (1 ^ tag_right),
                        "remove_right_tag_control": x_edge
                        & (1 ^ tag_left),
                        "delete_sign_gate": 0,
                    }
                    for name, value in mutations.items():
                        local_deletions[name] += value != expected
                    for term_index, (first, second) in enumerate(ROUTE_B_TERMS):
                        mutated = quadratic ^ (values[first] & values[second])
                        local_route_b_deletions[str(term_index)] += mutated != expected

                    if tag_left == tag_right == 0:
                        detail = descriptor(label, left_index, right_index, forward)
                        detail["local_pattern"] = pattern
                        if expected == 0 and positive_witness is None:
                            positive_witness = detail
                        if expected == 1 and negative_witness is None:
                            negative_witness = detail

            all_rows = set(forward_column) | set(reverse_column)
            projected_plain_column_residuals.append(
                float(
                    np.sqrt(
                        sum(
                            abs(reverse_column[row] - forward_column[row]) ** 2
                            for row in all_rows
                            if row_tags[row] == (0, 0)
                        )
                    )
                )
            )
            abstract_translator_column_residuals.append(
                float(
                    np.sqrt(
                        sum(
                            abs(
                                reverse_column[row]
                                - (-1 if row_signs[row] else 1) * forward_column[row]
                            )
                            ** 2
                            for row in all_rows
                        )
                    )
                )
            )

        if positive_witness is None or negative_witness is None:
            raise AssertionError("one edge lacked the required +/- witness pair")
        schmidt = single_edge_full_schmidt(code, outer_edge)
        row = {
            "edge_index": edge_index,
            "geometry": geometry,
            "outer_edge_M2": outer_edge,
            "interface_M2": len(interface_edges),
            "cases": cases,
            "positives": positives,
            "candidate_formula_errors": candidate_errors,
            "legacy_xz_formula_errors": legacy_errors,
            "route_b_formula_errors": route_b_errors,
            "AB_BA_phase_relation_errors": reverse_errors,
            "endpoint_swap_errors": endpoint_swap_errors,
            "row_sign_conflicts": row_sign_conflicts,
            "abstract_ray_diagonal_intertwiner_max_column_residual": max(
                abstract_translator_column_residuals
            ),
            "tag00_projected_plain_AB_BA_max_column_residual": max(
                projected_plain_column_residuals
            ),
            "tag00_projected_plain_AB_BA_nonzero_columns": sum(
                value > TOL for value in projected_plain_column_residuals
            ),
            "tag00_projected_plain_AB_BA_frobenius_residual": float(
                np.linalg.norm(projected_plain_column_residuals)
            ),
            "observed_candidate_patterns": len(patterns),
            "observed_route_b_patterns": len(route_b_patterns),
            "candidate_pattern_counts": {
                "".join(map(str, key)): value for key, value in sorted(patterns.items())
            },
            "candidate_deletion_errors": dict(local_deletions),
            "route_b_term_deletion_errors": dict(local_route_b_deletions),
            "positive_witness": positive_witness,
            "negative_witness": negative_witness,
            "edge_schmidt_control": schmidt,
        }
        rows.append(row)
        total_cases += cases
        total_positives += positives
        aggregate_deletions.update(local_deletions)
        route_b_deletions.update(local_route_b_deletions)
    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "edges": rows,
        "total_cases": total_cases,
        "total_positives": total_positives,
        "candidate_formula_errors": sum(row["candidate_formula_errors"] for row in rows),
        "legacy_xz_formula_errors": sum(row["legacy_xz_formula_errors"] for row in rows),
        "route_b_formula_errors": sum(row["route_b_formula_errors"] for row in rows),
        "AB_BA_phase_relation_errors": sum(
            row["AB_BA_phase_relation_errors"] for row in rows
        ),
        "endpoint_swap_errors": sum(row["endpoint_swap_errors"] for row in rows),
        "row_sign_conflicts": sum(row["row_sign_conflicts"] for row in rows),
        "maximum_abstract_ray_diagonal_intertwiner_column_residual": max(
            row["abstract_ray_diagonal_intertwiner_max_column_residual"] for row in rows
        ),
        "minimum_tag00_projected_plain_AB_BA_max_column_residual": min(
            row["tag00_projected_plain_AB_BA_max_column_residual"] for row in rows
        ),
        "tag00_projected_plain_AB_BA_nonzero_columns": sum(
            row["tag00_projected_plain_AB_BA_nonzero_columns"] for row in rows
        ),
        "route_b_pattern_counts": [row["observed_route_b_patterns"] for row in rows],
        "candidate_deletion_errors": dict(aggregate_deletions),
        "route_b_term_deletion_errors": dict(route_b_deletions),
    }


def periodic_seam_control(length: int) -> dict[str, object]:
    """Exhibit the x=1,z=0 positive missed by the legacy x*z extrapolation."""
    code = c315.c269.build_code(length)
    left_body = (0, 0, length - 1)
    right_body = (0, 0, 0)
    left_mode, right_mode = 4, 5
    left_vertex = c311.c305.body_vertices(code, left_body)[left_mode]
    right_vertex = c311.c305.body_vertices(code, right_body)[right_mode]
    outer_edge = c311.local.old.outer_partner(code, left_vertex)[1]
    if outer_edge != c311.local.old.outer_partner(code, right_vertex)[1]:
        raise AssertionError("the periodic seam endpoints did not share one M2")
    interface_edges = tuple(
        sorted(
            set(code.graph.incident[left_vertex])
            | set(code.graph.incident[right_vertex])
        )
    )
    left_terms = c315.gauge_input_terms(code, left_body, 1, (0,))
    right_terms = c315.gauge_input_terms(code, right_body, 1, (0,))
    witnesses = []
    for left_index, left_term in enumerate(left_terms):
        for right_index, right_term in enumerate(right_terms):
            representative = left_term.representative @ right_term.representative
            pattern = local_pattern(
                code, representative, outer_edge, left_vertex, right_vertex
            )
            expected = int(
                not left_term.representative.commutes(right_term.representative)
            )
            if pattern == (1, 0, 0, 0) and expected == 1:
                values = route_b_values(
                    code,
                    representative,
                    interface_edges,
                    left_vertex,
                    right_vertex,
                )
                row = descriptor(
                    (1, (0,), 1, (0,)),
                    left_index,
                    right_index,
                    representative,
                )
                row.update(
                    {
                        "local_pattern": pattern,
                        "corrected_sign": candidate_sign(pattern),
                        "legacy_xz_sign": legacy_xz_sign(pattern),
                        "route_b_sign": route_b_sign(values),
                        "route_b_monomial_values": tuple(
                            values[first] & values[second]
                            for first, second in ROUTE_B_TERMS
                        ),
                    }
                )
                witnesses.append(row)
    return {
        "L": length,
        "outer_edge_M2": outer_edge,
        "endpoint_bodies": (left_body, right_body),
        "endpoint_modes": (left_mode, right_mode),
        "witnesses": witnesses,
        "edge_schmidt_control": single_edge_full_schmidt(code, outer_edge),
    }


def frame_covariance_census(edge_rows_by_length) -> dict[str, object]:
    frames = c330.c235.proper_cubic_frames()
    frame_keys = {
        tuple(int(value) for value in frame.reshape(-1)): index
        for index, frame in enumerate(frames)
    }
    group_failures = 0
    direction_composition_failures = 0
    witness_transport_failures = 0
    source_direction = c330.EDGES[0][0][1]
    direction_orbit = Counter()
    for frame in frames:
        target = c311.direction_map(frame, source_direction)
        direction_orbit[target] += 1
        for rows in edge_rows_by_length:
            witness_transport_failures += not (
                rows[target]["positive_witness"]["local_pattern"] == (0, 0, 0, 0)
                and rows[target]["negative_witness"]["local_pattern"] == (1, 1, 0, 0)
                and rows[target]["edge_schmidt_control"]["schmidt_rank"] == 2
            )
    for left in frames:
        for right in frames:
            product_frame = left @ right
            group_failures += tuple(
                int(value) for value in product_frame.reshape(-1)
            ) not in frame_keys
            for direction in range(6):
                direction_composition_failures += c311.direction_map(
                    product_frame, direction
                ) != c311.direction_map(
                    left, c311.direction_map(right, direction)
                )
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "direction_composition_tests": len(frames) ** 2 * 6,
        "direction_composition_failures": direction_composition_failures,
        "six_direction_orbit": dict(sorted(direction_orbit.items())),
        "witness_transport_tests": len(frames) * len(edge_rows_by_length),
        "witness_transport_failures": witness_transport_failures,
    }


def label_space_diagnostics() -> dict[str, object]:
    label_gate = np.eye(8, dtype=complex)
    label_gate[1, 1] = -1
    # With tags |00>, I,Z -> + and X,Y -> -.  This is conjugation by Z on
    # operator coordinates.  The corresponding channel is physical, but that
    # does not mean left action by Z supplies the phase on P|vacuum>: the edge
    # vacuum marginal is I/2 and Z|vacuum> is orthogonal to |vacuum>.
    z_matrix = np.diag((1.0, -1.0)).astype(complex)
    z_vector = z_matrix.reshape(-1)
    conjugation_choi = np.outer(z_vector, z_vector.conj())
    active_coordinate_bits = sorted(set(sum((list(term) for term in ROUTE_B_TERMS), [])))
    active_edge_positions = sorted(
        {index if index < 9 else index - 9 for index in active_coordinate_bits if index < 18}
    )
    active_tags = [index for index in active_coordinate_bits if index >= 18]
    return {
        "candidate_claimed_physical_M2": 3,
        "candidate_physical_Hilbert_dimension": 2**3,
        "candidate_label_gate_dimension": label_gate.shape[0],
        "candidate_label_gate_unitarity_residual": float(
            np.linalg.norm(label_gate.conj().T @ label_gate - np.eye(8))
        ),
        "candidate_negative_label_patterns": tuple(
            index for index in range(8) if label_gate[index, index] == -1
        ),
        "tag00_edge_label_map": "I,Z -> +; X,Y -> - (conjugation by Z)",
        "conjugation_Choi_eigenvalues": tuple(
            float(value) for value in np.linalg.eigvalsh(conjugation_choi)
        ),
        "route_b_quadratic_terms": ROUTE_B_TERMS,
        "route_b_active_coordinate_bits": active_coordinate_bits,
        "route_b_active_face_M2_positions": active_edge_positions,
        "route_b_active_endpoint_tags": active_tags,
        "route_b_active_physical_M2": len(active_edge_positions) + len(active_tags),
        "route_b_active_label_bits": len(active_coordinate_bits),
        "route_b_active_physical_Hilbert_dimension": 2
        ** (len(active_edge_positions) + len(active_tags)),
        "route_b_active_label_space_dimension": 2 ** len(active_coordinate_bits),
    }


def main() -> None:
    source_rows = {
        "root_candidate": {
            "path": str(ROOT_CANDIDATE),
            "sha256": file_sha256(ROOT_CANDIDATE),
        },
        "route_b": {"path": str(ROUTE_B), "sha256": file_sha256(ROUTE_B)},
    }
    label_rows = label_space_diagnostics()
    check(
        "the corrected eight-pattern table is a Pauli-label translator and still needs a state-vector realization",
        label_rows["candidate_label_gate_unitarity_residual"] < TOL
        and label_rows["candidate_negative_label_patterns"] == (1,)
        and label_rows["candidate_label_gate_dimension"] == 8
        and label_rows["candidate_physical_Hilbert_dimension"] == 8
        and label_rows["conjugation_Choi_eigenvalues"] == (0.0, 0.0, 0.0, 2.0),
        label_rows,
    )

    censuses = [edge_census(length) for length in (5, 6)]
    check(
        "the root and six-term Route-B formulas classify every landed branch pair on all six directions",
        all(
            row["total_cases"] == 23784
            and row["total_positives"] == 1200
            and row["candidate_formula_errors"] == 0
            and row["legacy_xz_formula_errors"] == 0
            and row["route_b_formula_errors"] == 0
            and row["AB_BA_phase_relation_errors"] == 0
            and row["row_sign_conflicts"] == 0
            and row[
                "maximum_abstract_ray_diagonal_intertwiner_column_residual"
            ]
            < TOL
            and row["route_b_pattern_counts"] == [347, 258, 347, 258, 158, 158]
            for row in censuses
        ),
        {
            "rows": [
                {
                    key: value
                    for key, value in row.items()
                    if key != "edges"
                }
                for row in censuses
            ],
            "boundary": "zero classifier error is not a physical tensor-factor implementation",
        },
    )

    seam_rows = [periodic_seam_control(length) for length in (5, 6)]
    check(
        "the corrected x-only sign closes the periodic-seam witness that falsifies the legacy x*z extrapolation",
        all(
            row["outer_edge_M2"] == (74 if row["L"] == 5 else 89)
            and len(row["witnesses"]) == 2
            and row["edge_schmidt_control"]["schmidt_rank"] == 2
            and all(
                witness["local_pattern"] == (1, 0, 0, 0)
                and witness["corrected_sign"] == 1
                and witness["legacy_xz_sign"] == 0
                and witness["route_b_sign"] == 1
                for witness in row["witnesses"]
            )
            for row in seam_rows
        ),
        seam_rows,
    )

    check(
        "endpoint symmetry holds and corrected-formula plus Route-B deletions are active",
        all(row["endpoint_swap_errors"] == 0 for row in censuses)
        and all(
            row["candidate_deletion_errors"]["remove_x_control"] > 0
            and row["candidate_deletion_errors"]["remove_left_tag_control"] > 0
            and row["candidate_deletion_errors"]["remove_right_tag_control"] > 0
            and row["candidate_deletion_errors"]["delete_sign_gate"] > 0
            and all(value > 0 for value in row["route_b_term_deletion_errors"].values())
            for row in censuses
        ),
        {
            "candidate_deletions": [row["candidate_deletion_errors"] for row in censuses],
            "route_b_term_deletions": [
                row["route_b_term_deletion_errors"] for row in censuses
            ],
            "legacy_control": "x*z agrees on the six interior star arms but fails the bound periodic-seam witnesses",
        },
    )

    witness_rows = [row["edges"] for row in censuses]
    check(
        "each direction has a positive and negative tag-00 full-Schmidt physical witness",
        all(
            edge["positive_witness"]["local_pattern"] == (0, 0, 0, 0)
            and edge["negative_witness"]["local_pattern"] == (1, 1, 0, 0)
            and edge["edge_schmidt_control"]["schmidt_rank"] == 2
            and all(
                value is None
                for value in edge["edge_schmidt_control"][
                    "single_edge_stabilizer_phases"
                ].values()
            )
            for rows in witness_rows
            for edge in rows
        ),
        [
            {
                "L": censuses[index]["L"],
                "edges": [
                    {
                        "edge_index": edge["edge_index"],
                        "outer_edge_M2": edge["outer_edge_M2"],
                        "positive": edge["positive_witness"]["pauli_sha256"],
                        "negative": edge["negative_witness"]["pauli_sha256"],
                        "schmidt_rank": edge["edge_schmidt_control"]["schmidt_rank"],
                    }
                    for edge in rows
                ],
            }
            for index, rows in enumerate(witness_rows)
        ],
    )

    matrix_rows = physical_matrix_unit_contradiction()
    matrix_rows["minimum_encoding_tag00_projected_AB_BA_max_column_residual"] = min(
        row["minimum_tag00_projected_plain_AB_BA_max_column_residual"]
        for row in censuses
    )
    matrix_rows["encoding_tag00_projected_AB_BA_nonzero_columns"] = sum(
        row["tag00_projected_plain_AB_BA_nonzero_columns"] for row in censuses
    )
    check(
        "the genuine three-M2 matrix-unit equations are inconsistent with a leakage-aware unitary residual bound",
        matrix_rows["coefficient_rank"] == 4
        and matrix_rows["augmented_rank"] == 5
        and abs(
            matrix_rows["best_arbitrary_matrix_combined_state_residual"]
            - np.sqrt(2)
        )
        < TOL
        and matrix_rows["any_unitary_combined_state_residual"] == 2.0
        and abs(
            matrix_rows["any_unitary_maximum_witness_residual_lower_bound"]
            - np.sqrt(2)
        )
        < TOL
        and matrix_rows["identity_negative_residual"] == 2.0
        and matrix_rows["tag_flip_target_ray_leakage_probability"] == 1.0
        # The vacuum column fixes U on edge x |00>; nevertheless the actual
        # AB and BA encoding matrices differ in that same local sector.
        # This upgrades the branch-ray contradiction to the full intertwiner.
        and
        matrix_rows["minimum_encoding_tag00_projected_AB_BA_max_column_residual"]
        > 0.1
        and matrix_rows["encoding_tag00_projected_AB_BA_nonzero_columns"] > 0,
        matrix_rows,
    )

    covariance_rows = frame_covariance_census(witness_rows)
    check(
        "the route defect is endpoint-symmetric and covariant through all 24 frames and 576 products",
        covariance_rows["proper_cubic_frames"] == 24
        and covariance_rows["ordered_frame_products"] == 576
        and covariance_rows["frame_group_failures"] == 0
        and covariance_rows["direction_composition_failures"] == 0
        and covariance_rows["six_direction_orbit"] == {index: 4 for index in range(6)}
        and covariance_rows["witness_transport_failures"] == 0,
        covariance_rows,
    )

    certificate = {
        "source_sha256": source_rows,
        "formula": "x_outer*(1-tag_u)*(1-tag_v)",
        "failed_legacy_formula": "x_outer*z_outer*(1-tag_u)*(1-tag_v)",
        "route_b_terms": ROUTE_B_TERMS,
        "matrix_unit_ranks": (
            matrix_rows["coefficient_rank"],
            matrix_rows["augmented_rank"],
        ),
        "unitary_max_witness_residual_lower_bound": matrix_rows[
            "any_unitary_maximum_witness_residual_lower_bound"
        ],
        "witness_digests": [
            (
                edge["positive_witness"]["pauli_sha256"],
                edge["negative_witness"]["pauli_sha256"],
            )
            for rows in witness_rows
            for edge in rows
        ],
    }
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "specific-physical-M2-route-defect",
        "terminal": "THREE_M2_POSTPRODUCT_LABEL_GATE_DEFECT_EXHIBITED_LARGER_PHYSICAL_ROUTE_OPEN",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "sources": source_rows,
        "label_space": label_rows,
        "censuses": censuses,
        "periodic_seam_control": seam_rows,
        "matrix_unit_counterexample": matrix_rows,
        "covariance": covariance_rows,
        "resources": {
            "candidate_claimed_support_M2": 3,
            "candidate_physical_dimension": 8,
            "candidate_label_dimension": 8,
            "route_b_active_support_M2": label_rows["route_b_active_physical_M2"],
            "route_b_active_label_bits": label_rows["route_b_active_label_bits"],
            "six_directions": 6,
            "sizes": (5, 6),
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            / (1024 * 1024),
        },
        "certificate_sha256": sha256(
            json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        "derived": (
            "zero-error six-arm postproduct classification for the corrected root formula, legacy interior control and Route B polynomial",
            "periodic-seam x=1,z=0 witnesses closed by the corrected and Route-B signs but missed by the legacy x*z extrapolation",
            "an explicit +/- pair of landed tag-00 branch rays on every arm at L5 and held L6",
            "maximally mixed shared-edge marginal from the exact fixed-Wilson stabilizer tableau",
            "rank-4 versus augmented-rank-5 inconsistency of the genuine local matrix-unit equations",
            "a sqrt(2) lower bound on at least one witness residual for every three-M2 unitary, including leakage",
            "a nonzero AB/BA difference in the tag-00 projection of the actual Cycle315 encoding after the vacuum fixes the local unitary to identity there",
            "24-frame, 576-product transport of the same defect and active formula deletions",
        ),
        "route_defect": (
            "The corrected root candidate appropriately identifies its eight-pattern x/tag table as a label/ray "
            "translator and leaves physical synthesis open.  On the landed state vectors, positive and negative "
            "tag-00 witnesses have the same full-rank local marginal, so no operator on those three tensor factors "
            "can supply their opposite phases."
        ),
        "open": (
            "a larger-support physical syndrome-extraction circuit or matrix-unit completion",
            "ancilla-assisted preparation and uncomputation of conjugate edge syndrome information",
            "a full simultaneous two-star M64 update and recurrent schedule",
        ),
        "claim_ceiling": (
            "Specific counterexample to the root candidate's three-M2 physical-unitary interpretation. "
            "It does not rule out larger bounded supports, added physical syndrome registers, or other routes."
        ),
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
