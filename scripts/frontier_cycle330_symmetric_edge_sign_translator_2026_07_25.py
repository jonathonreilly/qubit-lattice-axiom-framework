#!/usr/bin/env python3
"""Cycle 700 supporting diagnostic: symmetric edge-sign translator.

Cycle 658 showed that factor-private endpoint-incidence features predict the
Cycle-330 branch commutation sign.  This runner asks the stronger state-local
question: after the two endpoint representatives have already been multiplied,
is their order sign a function of a bounded undirected physical interface?

On the declared n<=2 Cycle-315 domain the answer tested here is yes.  If e is
the shared outer-square M2 and t_u,t_v are its two endpoint-tag M2 factors, the
joint Pauli word p=a b obeys

    [a,b]_2 = x_e(p) (1-x_tu(p)) (1-x_tv(p)).

The corresponding diagonal phase on the eight local x/tag label patterns is
an endpoint-symmetric, self-inverse coefficient/ray-space translator.  The
runner executes its intertwiner from the actual AB encoding to the actual BA
encoding.  The label table is not by itself a physical three-M2 unitary: a
physical matrix-unit or circuit synthesis remains open.  This is an edge-order
translator diagnostic, not yet a recurrent multi-star update.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import json
import resource
import time

import numpy as np
from scipy import sparse

import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18 as c330


START = time.perf_counter()
TOL = 2.0e-12
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class EndpointTerm:
    representative: object
    amplitude: complex


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def endpoint_terms(code, body, number: int, label: tuple[int, ...]) -> tuple[EndpointTerm, ...]:
    """The exact two-slice/r-role terms used by Cycle 315."""
    rows = []
    for branch in c311.common_branches(code, body, number, label, 0):
        rows.append(
            EndpointTerm(
                c311.branch_representative(code, body, branch, 0),
                branch.amplitude / np.sqrt(2),
            )
        )
        target_slice = 0 if number == 0 else 1
        target = next(
            candidate
            for candidate in c311.common_branches(
                code, body, number, label, target_slice
            )
            if candidate.carrier_direction == branch.carrier_direction
        )
        rows.append(
            EndpointTerm(
                c311.branch_representative(code, body, target, 1),
                branch.amplitude / np.sqrt(2),
            )
        )
    return tuple(rows)


def outer_edge(code, body, mode: int) -> int:
    vertex = c311.c305.body_vertices(code, body)[mode]
    _arrival, edge = c311.local.old.outer_partner(code, vertex)
    return edge


def symmetric_edge_sign(code, representative, edge: int) -> int:
    u, v, kind, _owner = code.graph.edges[edge]
    if kind != "outer_square":
        raise ValueError("the edge-sign translator requires one outer-square M2")
    x_edge = (representative.x >> edge) & 1
    tag_u = (representative.x >> (code.qubits + u)) & 1
    tag_v = (representative.x >> (code.qubits + v)) & 1
    return x_edge & (1 ^ tag_u) & (1 ^ tag_v)


def local_pattern(code, representative, edge: int) -> tuple[int, int, int, int]:
    u, v, _kind, _owner = code.graph.edges[edge]
    return (
        (representative.x >> edge) & 1,
        (representative.z >> edge) & 1,
        (representative.x >> (code.qubits + u)) & 1,
        (representative.x >> (code.qubits + v)) & 1,
    )


def local_phase_gate() -> np.ndarray:
    """Coefficient-label diagnostic, not a claimed physical Hilbert gate."""
    result = np.eye(8, dtype=complex)
    for bits in range(8):
        x_edge = bits & 1
        tag_u = (bits >> 1) & 1
        tag_v = (bits >> 2) & 1
        sign = x_edge & (1 ^ tag_u) & (1 ^ tag_v)
        result[bits, bits] = -1 if sign else 1
    return result


def edge_census(length: int) -> dict[str, object]:
    code = c315.c269.build_code(length)
    labels = c315.joint_labels(2)
    label_pairs = tuple(
        (left_number, left_label, right_number, right_label)
        for left_number, left_label, right_number, right_label in labels
    )
    cache: dict[tuple[tuple[int, int, int], int, tuple[int, ...]], tuple[EndpointTerm, ...]] = {}

    cases = errors = positives = 0
    pattern_signs: dict[tuple[int, int, int, int], set[int]] = defaultdict(set)
    delete_outer_x_errors = 0
    delete_tag_u_orbit_errors = delete_tag_v_orbit_errors = 0
    orientation_augmented_cases = 0
    per_edge = []

    outer_edges = tuple(
        index
        for index, (_u, _v, kind, _owner) in enumerate(code.graph.edges)
        if kind == "outer_square"
    )
    for edge in outer_edges:
        u, v, _kind, _owner = code.graph.edges[edge]
        left_body, left_mode = code.graph.vertices[u]
        right_body, right_mode = code.graph.vertices[v]
        local_cases = local_errors = local_positives = 0
        for left_number, left_label, right_number, right_label in label_pairs:
            left_terms = cache.setdefault(
                (left_body, left_number, left_label),
                endpoint_terms(code, left_body, left_number, left_label),
            )
            right_terms = cache.setdefault(
                (right_body, right_number, right_label),
                endpoint_terms(code, right_body, right_number, right_label),
            )
            for left, right in product(left_terms, right_terms):
                expected = int(
                    not left.representative.commutes(right.representative)
                )
                joint = left.representative @ right.representative
                observed = symmetric_edge_sign(code, joint, edge)
                pattern = local_pattern(code, joint, edge)
                pattern_signs[pattern].add(expected)
                errors += observed != expected
                local_errors += observed != expected
                positives += expected
                local_positives += expected
                cases += 1
                local_cases += 1

                x_edge, z_edge, tag_u, tag_v = pattern
                delete_outer_x_errors += expected != 0
                # Include the endpoint-reversed orbit explicitly.  This makes
                # both tag controls active without choosing an endpoint order.
                for first, second in ((tag_u, tag_v), (tag_v, tag_u)):
                    orientation_augmented_cases += 1
                    delete_tag_u_orbit_errors += expected != (
                        x_edge & z_edge & (1 ^ second)
                    )
                    delete_tag_v_orbit_errors += expected != (
                        x_edge & z_edge & (1 ^ first)
                    )
        per_edge.append(
            {
                "edge": edge,
                "endpoint_modes": ((left_body, left_mode), (right_body, right_mode)),
                "cases": local_cases,
                "positives": local_positives,
                "errors": local_errors,
            }
        )

    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "outer_edges": len(outer_edges),
        "cases": cases,
        "positives": positives,
        "errors": errors,
        "pattern_count": len(pattern_signs),
        "ambiguous_patterns": sum(len(values) > 1 for values in pattern_signs.values()),
        "truth_table": {
            "".join(map(str, key)): sorted(values)
            for key, values in sorted(pattern_signs.items())
        },
        "delete_outer_x_errors": delete_outer_x_errors,
        "endpoint_reversed_orbit_cases": orientation_augmented_cases,
        "delete_tag_u_orbit_errors": delete_tag_u_orbit_errors,
        "delete_tag_v_orbit_errors": delete_tag_v_orbit_errors,
        "per_edge_case_values": sorted({row["cases"] for row in per_edge}),
        "per_edge_positive_values": sorted({row["positives"] for row in per_edge}),
        "per_edge_error_values": sorted({row["errors"] for row in per_edge}),
    }


def encoding_translator(length: int, left_cell: int, right_cell: int) -> dict[str, object]:
    code = c315.c269.build_code(length)
    left_body = c330.CELLS[left_cell]
    right_body = c330.CELLS[right_cell]
    shared, left_mode, _right_mode = __import__(
        "frontier_cycle330_branch_local_order_sign_features_2026_07_24"
    ).pair_geometry(left_cell, right_cell)
    if not shared:
        raise ValueError("the translator test needs one center-arm edge")
    edge = outer_edge(code, left_body, left_mode)
    labels = c315.joint_labels(2)
    reducer = c315.RayReducer(code)
    cache = {}
    ab_columns = []
    ba_columns = []
    row_sign: dict[int, int] = {}
    row_pattern: dict[int, tuple[int, int, int, int]] = {}
    sign_conflicts = pattern_conflicts = row_mismatches = branch_residuals = 0
    one_particle_negative_terms = 0

    for left_number, left_label, right_number, right_label in labels:
        left_terms = cache.setdefault(
            (left_body, left_number, left_label),
            endpoint_terms(code, left_body, left_number, left_label),
        )
        right_terms = cache.setdefault(
            (right_body, right_number, right_label),
            endpoint_terms(code, right_body, right_number, right_label),
        )
        ab = defaultdict(complex)
        ba = defaultdict(complex)
        for left, right in product(left_terms, right_terms):
            forward = left.representative @ right.representative
            reverse = right.representative @ left.representative
            expected = int(not left.representative.commutes(right.representative))
            observed = symmetric_edge_sign(code, forward, edge)
            forward_row, forward_phase = reducer.reduce(forward)
            reverse_row, reverse_phase = reducer.reduce(reverse)
            row_mismatches += forward_row != reverse_row
            branch_residuals += abs(reverse_phase - (-1 if observed else 1) * forward_phase) > TOL
            if forward_row in row_sign:
                sign_conflicts += row_sign[forward_row] != observed
                pattern_conflicts += row_pattern[forward_row] != local_pattern(code, forward, edge)
            else:
                row_sign[forward_row] = observed
                row_pattern[forward_row] = local_pattern(code, forward, edge)
            amplitude = left.amplitude * right.amplitude
            ab[forward_row] += amplitude * forward_phase
            ba[reverse_row] += amplitude * reverse_phase
            if left_number + right_number <= 1:
                one_particle_negative_terms += expected
        ab_columns.append(ab)
        ba_columns.append(ba)

    rows = len(reducer.row_by_aux)

    def matrix(columns):
        rr = []
        cc = []
        vv = []
        for column, entries in enumerate(columns):
            for row, value in entries.items():
                if abs(value) > 2e-14:
                    rr.append(row)
                    cc.append(column)
                    vv.append(value)
        return sparse.coo_matrix(
            (vv, (rr, cc)), shape=(rows, len(labels)), dtype=complex
        ).tocsc()

    forward = matrix(ab_columns)
    reverse = matrix(ba_columns)
    diagonal = np.ones(rows, dtype=complex)
    for row, sign in row_sign.items():
        diagonal[row] = -1 if sign else 1
    translator = sparse.diags(diagonal, format="csc")
    identity = sparse.eye(len(labels), format="csc")
    gram_forward = c315.raw_maximum_abs(forward.conj().T @ forward - identity)
    gram_reverse = c315.raw_maximum_abs(reverse.conj().T @ reverse - identity)
    intertwiner = c315.raw_maximum_abs(translator @ forward - reverse)
    involution = c315.raw_maximum_abs(
        translator @ translator - sparse.eye(rows, format="csc")
    )

    logical_coin, logical_stream, logical_contact, update, update_details = (
        c315.logical_update_controls(labels)
    )
    block_residuals = {
        "coin": c315.raw_maximum_abs(translator @ forward @ logical_coin - reverse @ logical_coin),
        "FSWAP": c315.raw_maximum_abs(translator @ forward @ logical_stream - reverse @ logical_stream),
        "contact": c315.raw_maximum_abs(translator @ forward @ logical_contact - reverse @ logical_contact),
        "full_update": c315.raw_maximum_abs(translator @ forward @ update - reverse @ update),
    }
    return {
        "L": length,
        "edge_cells": (left_cell, right_cell),
        "logical_columns": len(labels),
        "physical_rows": rows,
        "forward_nonzeros": forward.nnz,
        "reverse_nonzeros": reverse.nnz,
        "row_sign_conflicts": sign_conflicts,
        "row_pattern_conflicts": pattern_conflicts,
        "forward_reverse_row_mismatches": row_mismatches,
        "branch_phase_residual_failures": branch_residuals,
        "one_particle_negative_terms": one_particle_negative_terms,
        "forward_gram_raw_maximum": gram_forward,
        "reverse_gram_raw_maximum": gram_reverse,
        "translator_intertwiner_raw_maximum": intertwiner,
        "translator_involution_raw_maximum": involution,
        "logical_block_intertwiner_raw_maxima": block_residuals,
        "mass": {
            "Cycle219": update_details["Cycle219_mass_fixture"],
            "two_cell": update_details["two_cell_rest_mass"],
            "one_particle_eigen_residual": update_details[
                "two_cell_uniform_one_particle_residual"
            ],
        },
    }


def frame_and_two_star_controls() -> dict[str, object]:
    frames = c330.c235.proper_cubic_frames()
    frame_keys = {tuple(int(value) for value in frame.reshape(-1)): index for index, frame in enumerate(frames)}
    frame_product_failures = 0
    for left in frames:
        for right in frames:
            frame_product_failures += tuple(
                int(value) for value in (left @ right).reshape(-1)
            ) not in frame_keys

    # The local gate uses an undirected outer edge and both endpoint tags.
    # Coordinate frames may reverse endpoints; the unordered support is exact.
    edge_orbit = set()
    endpoint_reversing_frames = 0
    source = np.asarray((1, 0, 0), dtype=int)
    for frame in frames:
        target = frame @ source
        axis = int(np.flatnonzero(target)[0])
        sign = int(target[axis])
        edge_orbit.add((axis, abs(sign)))
        endpoint_reversing_frames += sign < 0

    code = c315.c269.build_code(5)

    def neighbors(body):
        result = []
        for mode, vertex in enumerate(c311.c305.body_vertices(code, body)):
            _arrival, edge = c311.local.old.outer_partner(code, vertex)
            u, v, kind, _owner = code.graph.edges[edge]
            if kind != "outer_square":
                raise ValueError("one body direction did not reach an outer-square edge")
            other = v if u == vertex else u
            target_body, target_mode = code.graph.vertices[other]
            result.append((edge, (body, mode), (target_body, target_mode)))
        return tuple(result)

    first_center = c330.CELLS[0]
    second_center = c330.CELLS[1]
    two_star_edges = {row[0] for row in neighbors(first_center)} | {
        row[0] for row in neighbors(second_center)
    }
    supports = []
    for edge in sorted(two_star_edges):
        u, v, _kind, _owner = code.graph.edges[edge]
        supports.append({("edge", edge), ("tag", u), ("tag", v)})
    support_intersections = sum(
        bool(left & right)
        for index, left in enumerate(supports)
        for right in supports[index + 1 :]
    )
    cells = {first_center, second_center}
    for center in (first_center, second_center):
        for _edge, _source, (target, _mode) in neighbors(center):
            cells.add(target)
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "frame_product_failures": frame_product_failures,
        "axis_orbit": len(edge_orbit),
        "endpoint_reversing_frames": endpoint_reversing_frames,
        "two_overlapping_star_cells": len(cells),
        "two_overlapping_star_unique_edges": len(two_star_edges),
        "three_M2_gate_supports": len(supports),
        "pairwise_support_intersections": support_intersections,
        "support_M2_union": len(set().union(*supports)),
    }


def main() -> None:
    gate = local_phase_gate()
    gate_unitarity = float(np.linalg.norm(gate.conj().T @ gate - np.eye(8)))
    gate_involution = float(np.linalg.norm(gate @ gate - np.eye(8)))
    gate_hermiticity = float(np.linalg.norm(gate - gate.conj().T))
    negative_patterns = tuple(index for index in range(8) if gate[index, index] == -1)
    check(
        "the symmetric x/tag label phase is an exact one-pattern involutive ray-space translator",
        gate_unitarity < TOL
        and gate_involution < TOL
        and gate_hermiticity < TOL
        and negative_patterns == (1,),
        {
            "basis_order": "x_edge,tag_u,tag_v",
            "dimension": 8,
            "physical_unitary_claimed": False,
            "negative_patterns": negative_patterns,
            "unitarity_residual": gate_unitarity,
            "involution_residual": gate_involution,
            "hermiticity_residual": gate_hermiticity,
        },
    )

    censuses = [edge_census(length) for length in (5, 6)]
    check(
        "the symmetric local formula predicts every nearest-neighbor branch sign at L5 and held L6",
        all(row["errors"] == row["ambiguous_patterns"] == 0 for row in censuses)
        and all(row["outer_edges"] == 3 * row["L"] ** 3 for row in censuses)
        and all(row["per_edge_case_values"] == [3964] for row in censuses)
        and all(row["per_edge_positive_values"] == [200] for row in censuses)
        and all(row["per_edge_error_values"] == [0] for row in censuses)
        and all(row["delete_outer_x_errors"] > 0 for row in censuses)
        and all(row["delete_tag_u_orbit_errors"] > 0 for row in censuses)
        and all(row["delete_tag_v_orbit_errors"] > 0 for row in censuses),
        censuses,
    )

    translators = [
        encoding_translator(length, 0, arm)
        for length in (5, 6)
        for arm in range(1, 7)
    ]
    maximum_residual = max(
        max(
            row["forward_gram_raw_maximum"],
            row["reverse_gram_raw_maximum"],
            row["translator_intertwiner_raw_maximum"],
            row["translator_involution_raw_maximum"],
            *row["logical_block_intertwiner_raw_maxima"].values(),
        )
        for row in translators
    )
    check(
        "the local phase executes AB-to-BA on all six edge encodings and preserves the full Cycle315 block",
        all(
            row["row_sign_conflicts"]
            == row["row_pattern_conflicts"]
            == row["forward_reverse_row_mismatches"]
            == row["branch_phase_residual_failures"]
            == row["one_particle_negative_terms"]
            == 0
            for row in translators
        )
        and maximum_residual < TOL,
        {
            "translator_rows": translators,
            "maximum_raw_residual": maximum_residual,
        },
    )

    frame_overlap = frame_and_two_star_controls()
    check(
        "the undirected gate family is proper-cubic and collision-free on two overlapping maximal stars",
        frame_overlap["proper_cubic_frames"] == 24
        and frame_overlap["ordered_frame_products"] == 576
        and frame_overlap["frame_product_failures"] == 0
        and frame_overlap["axis_orbit"] == 3
        and frame_overlap["endpoint_reversing_frames"] == 12
        and frame_overlap["two_overlapping_star_cells"] == 12
        and frame_overlap["two_overlapping_star_unique_edges"] == 11
        and frame_overlap["three_M2_gate_supports"] == 11
        and frame_overlap["pairwise_support_intersections"] == 0
        and frame_overlap["support_M2_union"] == 33,
        frame_overlap,
    )

    certificate = {
        "formula": "x_outer*(1-tag_u)*(1-tag_v)",
        "truth_table": censuses[0]["truth_table"],
        "two_star": frame_overlap,
    }
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "bounded-symmetric-edge-order-translator-certificate",
        "terminal": "SYMMETRIC_LOCAL_RAY_SIGN_TRANSLATOR_CLOSES_ORDER_SIGN_PHYSICAL_SYNTHESIS_OPEN",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "formula": certificate["formula"],
        "censuses": censuses,
        "translator_rows": translators,
        "maximum_raw_residual": maximum_residual,
        "frame_and_two_star": frame_overlap,
        "resources": {
            "physical_M2_interface_per_edge": 3,
            "physical_unitary_claimed": False,
            "local_pattern_dimension": 8,
            "negative_local_patterns": 1,
            "two_star_edge_gates": 11,
            "two_star_support_M2": 33,
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            / (1024 * 1024),
        },
        "certificate_sha256": sha256(
            json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        "supplied": (
            "the landed Cycle311/315 physical branch grammar and n<=2 domain",
            "the square-pyramid outer-edge and endpoint-tag M2 identification",
            "the local eight-pattern coefficient/ray label phase table",
            "the Cycle315 coin/FSWAP/contact update and one-particle fixture",
            "standard translations, proper-cubic frames and tolerance 2e-12",
        ),
        "derived": (
            "an endpoint-symmetric state-local sign formula on every L5 and held-L6 outer edge",
            "an executed sparse AB-to-BA physical-ray intertwiner on all six star edges",
            "composition with free coin, seam FSWAP, contact and full Cycle315 update",
            "identity action on the full one-particle branch-term sector",
            "a disjoint 33-M2 placement for eleven edge gates on two overlapping maximal stars",
            "proper-cubic endpoint-reversal closure and all 576 frame products",
        ),
        "open": (
            "an executed complete two-star update rather than eleven local order translators",
            "a physical matrix-unit or nearest-neighbor synthesis of the ray-label translator in the landed Cycle655 coordinate carrier",
            "simultaneous n>2 and full M64^12 widening",
            "shared cell-update scratch, recurrent scheduling, preparation and genesis",
            "physical time, source, Record, Born, minimum, no-go or axiom pressure",
        ),
        "claim_ceiling": (
            "Positive bounded local edge-order translator.  It removes factor-private incidence copies "
            "from the tested n<=2 sign operation, but it does not by itself execute the complete "
            "two-star recurrent physical update or close the full M64 lattice compiler."
        ),
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
