#!/usr/bin/env python3
"""Sparse edge-local qutrit gauge on two overlapping maximal stars.

This is a constructive shared-edge probe, not a full two-star M64 compiler.
It extends each *factor* representative before multiplication by two M2 bits
per endpoint feature copy.  Thus the factor contributions that cancel on the
common physical outer-square M2 remain available in two star-private views.
Two local equality projectors identify the duplicate views on the common
edge.  A reversible five-M2 phase circuit plus one edge-role M2 then gives an
executed AB/BA chart-toggle intertwiner.

The full branch-ray copy projector is only a diagnostic.  This runner does
not claim a primitive Hamiltonian/projector synthesis or an end-to-end update
of two simultaneous maximal stars.
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
import frontier_two_overlapping_star_sparse_qutrit_edge_gauge_core_2026_07_25 as core


START = time.perf_counter()
TOL = 4.0e-10
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def q_word_from_representative(code, body, mode: int, representative) -> int:
    vertex = c311.c305.body_vertices(code, body)[mode]
    _arrival, outer_edge = c311.local.old.outer_partner(code, vertex)
    outer = (representative.x >> outer_edge) & 1
    tag = (representative.x >> (code.qubits + vertex)) & 1
    return core.qutrit_word(outer, tag)


@dataclass
class AugmentedTermBuilder:
    code: object

    def __post_init__(self) -> None:
        code = self.code
        self.base = code.qubits + len(code.graph.vertices) + 2 * code.length**3
        # Copy-block order is A-left, A-right, B-left, B-right.  On the common
        # edge B-left is the physical right factor and B-right the physical
        # left factor.
        self.blocks = {
            c315.LEFT: (0, 6),
            c315.RIGHT: (2, 4),
        }
        self.modes = {c315.LEFT: 0, c315.RIGHT: 1}
        self.invalid_factor_words = 0
        self.factor_term_rows = 0

    def __call__(self, code, body, number: int, label: tuple[int, ...]):
        rows = []
        for term in c315.gauge_input_terms(code, body, number, label):
            word = q_word_from_representative(
                code, body, self.modes[body], term.representative
            )
            outer, tag = core.qutrit_bits(word)
            x_word = term.representative.x
            for start in self.blocks[body]:
                x_word |= tag << (self.base + start)
                x_word |= outer << (self.base + start + 1)
            representative = c315.c235.Pauli(
                term.representative.phase, x_word, term.representative.z
            )
            rows.append(c315.GaugeTerm(term.number, representative, term.amplitude))
            self.factor_term_rows += 1
            self.invalid_factor_words += word not in core.LAWFUL_QUTRIT_WORDS
        return tuple(rows)

    def copy_words_from_aux(self, auxiliary: int) -> tuple[int, int, int, int]:
        offset = self.base - self.code.qubits
        return tuple((auxiliary >> (offset + 2 * block)) & 0b11 for block in range(4))


def aligned_encodings(length: int, labels) -> tuple[dict[str, object], object, object, object, object, object]:
    code = c315.c269.build_code(length)
    builder = AugmentedTermBuilder(code)
    reducer = c315.RayReducer(code)
    forward = c315.joint_encoding(code, labels, reducer, False, builder)
    reverse = c315.joint_encoding(code, labels, reducer, True, builder)
    rows = len(reducer.row_by_aux)
    forward, reverse = c315.align_rows(forward, reverse, rows)
    identity = sparse.eye(len(labels), format="csc")

    phases = np.ones(rows, dtype=float)
    copy_failures = invalid_copy_words = star_sign_disagreements = 0
    positive_rows = 0
    for auxiliary, row in reducer.row_by_aux.items():
        a_left, a_right, b_left, b_right = builder.copy_words_from_aux(auxiliary)
        invalid_copy_words += sum(
            word not in core.LAWFUL_QUTRIT_WORDS
            for word in (a_left, a_right, b_left, b_right)
        )
        copy_failures += a_left != b_right
        copy_failures += a_right != b_left
        a_sign = core.branch_sign_bit(a_left, a_right)
        b_sign = core.branch_sign_bit(b_left, b_right)
        star_sign_disagreements += a_sign != b_sign
        positive_rows += a_sign
        phases[row] = -1.0 if a_sign else 1.0

    sign = sparse.diags(phases, format="csc")
    aligned_difference = sign @ reverse - forward
    raw_difference = reverse - forward
    double_count_difference = sign @ sign @ reverse - forward

    encoding = sparse.block_diag((forward, reverse), format="csc")
    zero_rows = sparse.csc_matrix((rows, rows), dtype=complex)
    physical_toggle = sparse.bmat(((zero_rows, sign), (sign, zero_rows)), format="csc")
    zero_logical = sparse.csc_matrix((len(labels), len(labels)), dtype=complex)
    logical_identity = sparse.eye(len(labels), format="csc")
    coarse_toggle = sparse.bmat(
        ((zero_logical, logical_identity), (logical_identity, zero_logical)),
        format="csc",
    )
    intertwiner_difference = physical_toggle @ encoding - encoding @ coarse_toggle
    physical_identity = sparse.eye(2 * rows, format="csc")
    code_identity = sparse.eye(2 * len(labels), format="csc")
    details = {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "logical_columns_n0_to_n2": len(labels),
        "full_branch_rays": rows,
        "forward_nonzeros": forward.nnz,
        "reverse_nonzeros": reverse.nnz,
        "factor_term_rows_visited": builder.factor_term_rows,
        "invalid_factor_feature_words": builder.invalid_factor_words,
        "invalid_copy_words": invalid_copy_words,
        "shared_copy_equality_failures": copy_failures,
        "two_star_sign_disagreements": star_sign_disagreements,
        "negative_sign_branch_rays": positive_rows,
        "forward_Gram_residual": c315.largest_singular(
            forward.conj().T @ forward - identity
        ),
        "reverse_Gram_residual": c315.largest_singular(
            reverse.conj().T @ reverse - identity
        ),
        "two_role_code_Gram_residual": c315.largest_singular(
            encoding.conj().T @ encoding - code_identity
        ),
        "local_sign_alignment_residual": c315.largest_singular(aligned_difference),
        "local_sign_alignment_raw_maximum": c315.raw_maximum_abs(aligned_difference),
        "uncorrected_AB_BA_residual": c315.largest_singular(raw_difference),
        "uncorrected_AB_BA_raw_maximum": c315.raw_maximum_abs(raw_difference),
        "role_toggle_unitarity_residual": c315.largest_singular(
            physical_toggle.conj().T @ physical_toggle - physical_identity
        ),
        "role_toggle_intertwining_residual": c315.largest_singular(
            intertwiner_difference
        ),
        "role_toggle_intertwining_raw_maximum": c315.raw_maximum_abs(
            intertwiner_difference
        ),
        "delete_sign_gate_residual": c315.largest_singular(raw_difference),
        "double_count_shared_gate_residual": c315.largest_singular(
            double_count_difference
        ),
    }
    return details, code, builder, reducer, forward, reverse


def local_joint_ray_census(length: int) -> dict[str, object]:
    """Test what survives after the two factor contributions are multiplied."""
    code = c315.c269.build_code(length)
    # Use the interior +x edge of the actual Cycle-330 maximal star.  The
    # Cycle-315 encoding below is translation covariant, but its declared
    # representative seam begins at the periodic origin; using the interior
    # edge here avoids turning that reference seam into a local extractor.
    left_body = c330.CELLS[0]
    right_body = c330.CELLS[2]
    left_vertex = c311.c305.body_vertices(code, left_body)[0]
    right_vertex = c311.c305.body_vertices(code, right_body)[1]
    _arrival, outer_edge = c311.local.old.outer_partner(code, left_vertex)
    if outer_edge != c311.local.old.outer_partner(code, right_vertex)[1]:
        raise AssertionError("the two endpoints did not resolve one shared outer M2")
    interface_edges = tuple(
        sorted(set(code.graph.incident[left_vertex]) | set(code.graph.incident[right_vertex]))
    )
    local_groups = defaultdict(lambda: {"q": set(), "sign": set(), "cases": 0})
    reducer = c315.RayReducer(code)
    ray_q = defaultdict(set)
    ray_sign = defaultdict(set)
    feature_mismatches = positive_signs = 0
    naive_q_mismatches = naive_sign_mismatches = naive_invalid_words = 0
    cases = 0
    cache = {}
    for left_number, left_label, right_number, right_label in c315.joint_labels(2):
        left_terms = cache.setdefault(
            (left_body, left_number, left_label),
            c315.gauge_input_terms(code, left_body, left_number, left_label),
        )
        right_terms = cache.setdefault(
            (right_body, right_number, right_label),
            c315.gauge_input_terms(code, right_body, right_number, right_label),
        )
        for left_term, right_term in product(left_terms, right_terms):
            left_word = q_word_from_representative(
                code, left_body, 0, left_term.representative
            )
            right_word = q_word_from_representative(
                code, right_body, 1, right_term.representative
            )
            sign = core.branch_sign_bit(left_word, right_word)
            observed = int(
                not left_term.representative.commutes(right_term.representative)
            )
            feature_mismatches += sign != observed
            positive_signs += sign
            representative = left_term.representative @ right_term.representative
            row, _phase = reducer.reduce(representative)
            ray_q[row].add((left_word, right_word))
            ray_sign[row].add(sign)

            local_word = 0
            cursor = 0
            for edge in interface_edges:
                local_word |= ((representative.x >> edge) & 1) << cursor
                cursor += 1
            for edge in interface_edges:
                local_word |= ((representative.z >> edge) & 1) << cursor
                cursor += 1
            for vertex in (left_vertex, right_vertex):
                local_word |= (
                    (representative.x >> (code.qubits + vertex)) & 1
                ) << cursor
                cursor += 1
            group = local_groups[local_word]
            group["q"].add((left_word, right_word))
            group["sign"].add(sign)
            group["cases"] += 1

            outer_xor = (representative.x >> outer_edge) & 1
            left_tag = (representative.x >> (code.qubits + left_vertex)) & 1
            right_tag = (representative.x >> (code.qubits + right_vertex)) & 1
            naive_words = ((outer_xor << 1) | left_tag, (outer_xor << 1) | right_tag)
            if any(word not in core.LAWFUL_QUTRIT_WORDS for word in naive_words):
                naive_invalid_words += 1
            else:
                naive_q_mismatches += naive_words != (left_word, right_word)
                naive_sign_mismatches += (
                    core.branch_sign_bit(*naive_words) != sign
                )
            cases += 1

    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "factor_term_pair_cases": cases,
        "feature_sign_mismatches": feature_mismatches,
        "positive_signs": positive_signs,
        "interface_M2": len(interface_edges),
        "interface_edge_kinds": dict(
            sorted(Counter(code.graph.edges[edge][2] for edge in interface_edges).items())
        ),
        "full_joint_branch_rays": len(ray_q),
        "full_ray_qpair_ambiguities": sum(len(values) > 1 for values in ray_q.values()),
        "full_ray_sign_ambiguities": sum(
            len(values) > 1 for values in ray_sign.values()
        ),
        "local_interface_words": len(local_groups),
        "local_interface_qpair_ambiguities": sum(
            len(group["q"]) > 1 for group in local_groups.values()
        ),
        "local_interface_sign_ambiguities": sum(
            len(group["sign"]) > 1 for group in local_groups.values()
        ),
        "local_ambiguous_sign_cases": sum(
            group["cases"]
            for group in local_groups.values()
            if len(group["sign"]) > 1
        ),
        "naive_postproduct_invalid_qpair_cases": naive_invalid_words,
        "naive_postproduct_qpair_mismatches_on_lawful_outputs": naive_q_mismatches,
        "naive_postproduct_sign_mismatches_on_lawful_outputs": naive_sign_mismatches,
    }


def half_edge_chart_census(length: int) -> dict[str, int]:
    code = c315.c269.build_code(length)
    failures = invalid_words = cases = 0
    for edge in c330.EDGES:
        for cell_index, mode in edge:
            body = c330.CELLS[cell_index]
            for number, label in c311.FOCK_LABELS:
                if number > 2:
                    continue
                for branch in c311.common_branches(code, body, number, label, 0):
                    variants = ((branch, 0),)
                    if number:
                        target = next(
                            candidate
                            for candidate in c311.common_branches(
                                code, body, number, label, 1
                            )
                            if candidate.carrier_direction == branch.carrier_direction
                        )
                        variants += ((target, 1),)
                    else:
                        variants += ((branch, 1),)
                    for candidate, r_value in variants:
                        representative = c311.branch_representative(
                            code, body, candidate, r_value
                        )
                        word = q_word_from_representative(
                            code, body, mode, representative
                        )
                        incidence, tag = core.incidence_and_tag(word)
                        expected_incidence = int(
                            mode in label or candidate.carrier_direction == mode
                        )
                        vertex = c311.c305.body_vertices(code, body)[mode]
                        expected_tag = (
                            representative.x >> (code.qubits + vertex)
                        ) & 1
                        failures += (incidence, tag) != (
                            expected_incidence,
                            expected_tag,
                        )
                        invalid_words += word not in core.LAWFUL_QUTRIT_WORDS
                        cases += 1
    return {
        "L": length,
        "half_edge_branch_cases": cases,
        "feature_chart_failures": failures,
        "invalid_qutrit_words": invalid_words,
    }


QUADRATIC_LABEL_TERMS = (
    (5, 13),
    (6, 14),
    (13, 18),
    (13, 19),
    (14, 15),
    (18, 19),
)


def quadratic_label_sign(values: tuple[int, ...]) -> int:
    if len(values) != 20:
        raise ValueError("the interface label chart has x9,z9,tag2 coordinates")
    return sum(values[left] & values[right] for left, right in QUADRATIC_LABEL_TERMS) & 1


def quadratic_postproduct_census(length: int) -> dict[str, object]:
    """Check the sparse postproduct sign formula as a label diagnostic only."""
    code = c315.c269.build_code(length)
    errors = cases = 0
    pattern_counts = []
    for edge in c330.EDGES:
        (left_cell, left_mode), (right_cell, right_mode) = edge
        left_body = c330.CELLS[left_cell]
        right_body = c330.CELLS[right_cell]
        left_vertex = c311.c305.body_vertices(code, left_body)[left_mode]
        right_vertex = c311.c305.body_vertices(code, right_body)[right_mode]
        _arrival, outer_edge = c311.local.old.outer_partner(code, left_vertex)
        if outer_edge != c311.local.old.outer_partner(code, right_vertex)[1]:
            raise AssertionError("one center-arm pair did not share its outer M2")
        interface_edges = tuple(
            sorted(
                set(code.graph.incident[left_vertex])
                | set(code.graph.incident[right_vertex])
            )
        )
        patterns = set()
        cache = {}
        for left_number, left_label, right_number, right_label in c315.joint_labels(2):
            left_terms = cache.setdefault(
                (left_body, left_number, left_label),
                c315.gauge_input_terms(code, left_body, left_number, left_label),
            )
            right_terms = cache.setdefault(
                (right_body, right_number, right_label),
                c315.gauge_input_terms(code, right_body, right_number, right_label),
            )
            for left_term, right_term in product(left_terms, right_terms):
                representative = left_term.representative @ right_term.representative
                values = tuple(
                    [(representative.x >> item) & 1 for item in interface_edges]
                    + [(representative.z >> item) & 1 for item in interface_edges]
                    + [
                        (representative.x >> (code.qubits + vertex)) & 1
                        for vertex in (left_vertex, right_vertex)
                    ]
                )
                left_word = q_word_from_representative(
                    code, left_body, left_mode, left_term.representative
                )
                right_word = q_word_from_representative(
                    code, right_body, right_mode, right_term.representative
                )
                expected = core.branch_sign_bit(left_word, right_word)
                predicted = quadratic_label_sign(values)
                errors += predicted != expected
                patterns.add((values, expected))
                cases += 1
        pattern_counts.append(len(patterns))
    return {
        "L": length,
        "center_arm_term_pair_cases": cases,
        "quadratic_label_sign_errors": errors,
        "observed_patterns_per_edge": pattern_counts,
        "quadratic_terms": QUADRATIC_LABEL_TERMS,
        "term_count": len(QUADRATIC_LABEL_TERMS),
        "coordinate_order": "x on sorted interface M2, z on the same M2, left tag, right tag",
        "physical_unitary_claimed": False,
    }


def update_fixture(labels) -> dict[str, object]:
    logical_coin, logical_stream, logical_contact, update, details = (
        c315.logical_update_controls(labels)
    )
    zero = sparse.csc_matrix((len(labels), len(labels)), dtype=complex)
    role_toggle = sparse.bmat(
        (
            (zero, sparse.eye(len(labels), format="csc")),
            (sparse.eye(len(labels), format="csc"), zero),
        ),
        format="csc",
    )
    doubled_contact = sparse.block_diag((logical_contact, logical_contact), format="csc")
    doubled_update = sparse.block_diag((update, update), format="csc")
    return {
        **details,
        "role_toggle_contact_commutator": c315.largest_singular(
            role_toggle @ doubled_contact - doubled_contact @ role_toggle
        ),
        "role_toggle_full_logical_update_commutator": c315.largest_singular(
            role_toggle @ doubled_update - doubled_update @ role_toggle
        ),
        "seam_roles": 2,
    }


def deletion_domain_controls(projectors: dict[str, object]) -> dict[str, object]:
    invalid_rejections = 0
    for operation in (
        lambda: core.qutrit_bits(0b11),
        lambda: core.qutrit_word(2, 0),
        lambda: core.patch_geometry((1, 1, 0)),
        lambda: c315.joint_labels(13),
    ):
        try:
            operation()
        except ValueError:
            invalid_rejections += 1

    incompatible_lawful_rows = 0
    sign_disagreements = 0
    for a_left, a_right, b_left, b_right in product(
        core.LAWFUL_QUTRIT_WORDS, repeat=4
    ):
        compatible = a_left == b_right and a_right == b_left
        incompatible_lawful_rows += not compatible
        sign_disagreements += (
            not compatible
            and core.branch_sign_bit(a_left, a_right)
            != core.branch_sign_bit(b_left, b_right)
        )

    deleted_uncompute_scratch_failures = 0
    for left_word, right_word in product(core.LAWFUL_QUTRIT_WORDS, repeat=2):
        left_tag = left_word & 1
        right_tag = right_word & 1
        deleted_uncompute_scratch_failures += left_tag ^ right_tag
    return {
        "lawful_four_copy_rows": 3**4,
        "compatible_four_copy_rows": 3**2,
        "incompatible_lawful_rows_rejected": incompatible_lawful_rows,
        "incompatible_rows_with_star_sign_disagreement": sign_disagreements,
        "delete_one_equality_rank_surplus": projectors[
            "delete_one_equality_rank"
        ]
        - projectors["joint_equality_rank"],
        "deleted_scratch_uncompute_failures": deleted_uncompute_scratch_failures,
        "lawful_domain_rejections": invalid_rejections,
    }


def main() -> None:
    labels = c315.joint_labels(2)
    projector_rows = core.four_copy_projectors()
    circuit_rows = core.sign_circuit_census()
    covariance_rows = core.covariance_census()
    geometry = core.patch_geometry()

    check(
        "the two-star patch has one shared physical edge and a constant sparse feature inventory",
        len(geometry["incidences"]) == 12
        and len(geometry["edges"]) == 11
        and len(geometry["cells"]) == 12
        and len(geometry["shared_rows"]) == 2,
        {
            "maximal_stars": 2,
            "star_incidence_edges": len(geometry["incidences"]),
            "unique_physical_edges": len(geometry["edges"]),
            "distinct_coarse_cells": len(geometry["cells"]),
            "shared_edge_star_views": geometry["shared_rows"],
            "star_private_half_edge_qutrits": 24,
            "feature_copy_M2": 48,
            "unique_edge_role_M2": 11,
            "edge_local_scratch_M2": 11,
            "total_new_feature_role_scratch_M2": 70,
            "new_M2_per_coarse_cell_on_this_fixed_patch": 70 / 12,
            "maximum_constraint_support_M2": 4,
            "maximum_role_toggle_circuit_support_M2": 6,
            "global_ordering_M2": 0,
            "Jordan_Wigner_string_M2": 0,
            "host_branch_queries": 0,
        },
    )

    local_q = core.valid_qutrit_projector()
    local_eq = core.equality_projector()
    check(
        "explicit sparse qutrit validity and cross-star equality projectors have the exact shared-edge rank",
        np.linalg.matrix_rank(local_q) == 3
        and np.linalg.matrix_rank(local_eq) == 3
        and np.linalg.norm(local_q @ local_q - local_q) < 1e-14
        and np.linalg.norm(local_eq @ local_eq - local_eq) < 1e-14
        and projector_rows["ambient_dimension"] == 256
        and projector_rows["valid_rank"] == 81
        and projector_rows["joint_equality_rank"] == 9
        and projector_rows["delete_one_equality_rank"] == 27
        and max(
            projector_rows["valid_left_commutator"],
            projector_rows["valid_right_commutator"],
            projector_rows["equality_commutator"],
            projector_rows["joint_idempotence_residual"],
        )
        < 1e-14,
        {
            "single_qutrit_projector_rank": int(np.linalg.matrix_rank(local_q)),
            "single_copy_equality_projector_rank": int(
                np.linalg.matrix_rank(local_eq)
            ),
            **projector_rows,
            "full_patch_lawful_feature_rank_before_shared_equalities": 3**24,
            "full_patch_feature_constraint_rank_after_shared_equalities": 3**22,
            "full_patch_feature_rank_after_deleting_one_shared_equality": 3**23,
            "full_patch_copy_ambient_dimension": 2**48,
            "scope": "full branch-ray copy projector diagnostic only",
        },
    )

    check(
        "the five-M2 sign circuit is exact on the qutrit truth table and returns scratch",
        circuit_rows["lawful_truth_table_cases"] == 9
        and circuit_rows["phase_failures"] == 0
        and circuit_rows["returned_scratch_failures"] == 0,
        {
            **circuit_rows,
            "gate_word": (
                "CNOT(tagL,s) CNOT(tagR,s) CNOT(outerL,tagL) "
                "CNOT(outerR,tagR) CCZ(tagL,tagR,s) then exact reverse"
            ),
            "data_M2": 4,
            "scratch_M2": 1,
        },
    )

    alignment_rows = []
    joint_rows = []
    chart_rows = []
    quadratic_rows = []
    for length in (5, 6):
        aligned, _code, _builder, _reducer, _forward, _reverse = aligned_encodings(
            length, labels
        )
        alignment_rows.append(aligned)
        joint_rows.append(local_joint_ray_census(length))
        chart_rows.append(half_edge_chart_census(length))
        quadratic_rows.append(quadratic_postproduct_census(length))

    check(
        "factor-contribution qutrit copies align the full shared-edge AB/BA branch encodings through held L6",
        all(
            row["logical_columns_n0_to_n2"] == 79
            and row["full_branch_rays"] == 3964
            and row["forward_nonzeros"] == row["reverse_nonzeros"] == 3964
            and row["invalid_factor_feature_words"] == 0
            and row["invalid_copy_words"] == 0
            and row["shared_copy_equality_failures"] == 0
            and row["two_star_sign_disagreements"] == 0
            and row["forward_Gram_residual"] < TOL
            and row["reverse_Gram_residual"] < TOL
            and row["two_role_code_Gram_residual"] < TOL
            and row["local_sign_alignment_residual"] < TOL
            and row["local_sign_alignment_raw_maximum"] < 1e-14
            and row["uncorrected_AB_BA_residual"] > 1.4
            for row in alignment_rows
        ),
        alignment_rows,
    )

    check(
        "one edge-role M2 and the local sign circuit give an executed exact chart-toggle intertwiner",
        all(
            row["role_toggle_unitarity_residual"] < TOL
            and row["role_toggle_intertwining_residual"] < TOL
            and row["role_toggle_intertwining_raw_maximum"] < 1e-14
            for row in alignment_rows
        ),
        {
            "equation": "E G_coarse_role = G_physical_role E",
            "rows": alignment_rows,
            "physical_update": "one local edge-role X times the five-M2 qutrit sign circuit",
            "host_branch_queries": 0,
        },
    )

    check(
        "the actual half-edge qutrit chart and factor sign remain exact at L5 and held L6",
        all(
            row["half_edge_branch_cases"] == 1104
            and row["feature_chart_failures"] == 0
            and row["invalid_qutrit_words"] == 0
            for row in chart_rows
        )
        and all(
            row["factor_term_pair_cases"] == 3964
            and row["feature_sign_mismatches"] == 0
            and row["positive_signs"] == 200
            and row["interface_M2"] == 9
            and row["interface_edge_kinds"]
            == {"internal_triangle": 8, "outer_square": 1}
            and row["full_joint_branch_rays"] == 3964
            and row["full_ray_qpair_ambiguities"] == 0
            and row["full_ray_sign_ambiguities"] == 0
            for row in joint_rows
        ),
        {"half_edge_charts": chart_rows, "joint_rays": joint_rows},
    )

    check(
        "the postproduct local interface cannot reconstruct the factor-private qutrit copies",
        all(
            row["local_interface_words"] == 347
            and row["local_interface_qpair_ambiguities"] == 18
            and row["local_interface_sign_ambiguities"] == 0
            and row["local_ambiguous_sign_cases"] == 0
            and row["naive_postproduct_invalid_qpair_cases"] > 0
            and row["naive_postproduct_qpair_mismatches_on_lawful_outputs"] > 0
            and row["naive_postproduct_sign_mismatches_on_lawful_outputs"] > 0
            for row in joint_rows
        ),
        {
            "rows": joint_rows,
            "interpretation": (
                "the common outer-square contribution is XOR-combined by factor multiplication; "
                "the ordered qutrit pair is not recoverable from this interface even though its "
                "sign is; this runner uses pre-multiplication copies and does not claim a sparse "
                "postproduct sign circuit"
            ),
        },
    )

    check(
        "a six-term quadratic Pauli-label formula retains the postproduct sign on all six edges",
        all(
            row["center_arm_term_pair_cases"] == 23784
            and row["quadratic_label_sign_errors"] == 0
            and row["observed_patterns_per_edge"] == [347, 258, 347, 258, 158, 158]
            and row["term_count"] == 6
            and not row["physical_unitary_claimed"]
            for row in quadratic_rows
        ),
        {
            "rows": quadratic_rows,
            "boundary": (
                "x/z are Pauli-label coordinates; this is not yet a physical direct-sign "
                "unitary or a replacement for the qutrit-copy circuit"
            ),
        },
    )

    check(
        "the complete two-star feature gadget is covariant under all 24 frames and 576 products",
        covariance_rows["proper_cubic_frames"] == 24
        and covariance_rows["ordered_frame_products"] == 576
        and covariance_rows["frame_geometry_failures"] == 0
        and covariance_rows["frame_product_failures"] == 0
        and covariance_rows["shared_edge_transport_failures"] == 0
        and covariance_rows["feature_sign_covariance_failures"] == 0,
        covariance_rows,
    )

    fixture = update_fixture(labels)
    check(
        "the underlying free seam contact update and one-particle mass fixture are unchanged",
        fixture["coin_unitarity"] < TOL
        and fixture["FSWAP_unitarity"] < TOL
        and fixture["contact_unitarity"] < TOL
        and fixture["composed_unitarity"] < TOL
        and fixture["contact_nontrivial_columns"] > 0
        and abs(fixture["two_cell_rest_mass"] - fixture["Cycle219_mass_fixture"])
        < 3e-13
        and fixture["two_cell_uniform_one_particle_residual"] < 2e-12
        and fixture["role_toggle_contact_commutator"] < TOL
        and fixture["role_toggle_full_logical_update_commutator"] < TOL,
        fixture,
    )

    deletion_rows = deletion_domain_controls(projector_rows)
    check(
        "copy equality sign scratch double-count and lawful-domain deletions remain active",
        deletion_rows["incompatible_lawful_rows_rejected"] == 72
        and deletion_rows["incompatible_rows_with_star_sign_disagreement"] > 0
        and deletion_rows["delete_one_equality_rank_surplus"] == 18
        and deletion_rows["deleted_scratch_uncompute_failures"] == 4
        and deletion_rows["lawful_domain_rejections"] == 4
        and all(row["delete_sign_gate_residual"] > 1.4 for row in alignment_rows)
        and all(
            row["double_count_shared_gate_residual"] > 1.4
            for row in alignment_rows
        ),
        {
            **deletion_rows,
            "delete_sign_gate_residuals": [
                row["delete_sign_gate_residual"] for row in alignment_rows
            ],
            "double_count_shared_gate_residuals": [
                row["double_count_shared_gate_residual"] for row in alignment_rows
            ],
        },
    )

    certificate = {
        "lawful_qutrit_words": core.LAWFUL_QUTRIT_WORDS,
        "geometry_edges": sorted(geometry["edges"]),
        "projector_rows": projector_rows,
        "alignment_rows": alignment_rows,
        "joint_rows": joint_rows,
        "quadratic_rows": quadratic_rows,
        "covariance_rows": covariance_rows,
    }
    digest = sha256(
        json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "bounded-two-overlapping-star-sparse-qutrit-edge-gauge-probe",
        "terminal": "SHARED_EDGE_QUTRIT_ROLE_TOGGLE_CLOSED_FULL_TWO_STAR_M64_UPDATE_OPEN",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "route_disposition": (
            "constructive shared-edge order/sign compiler and exact local role-toggle update; "
            "partial for the tournament because the simultaneous twelve-cell physical M64 update "
            "and primitive projector enforcement remain open"
        ),
        "domains": {
            "logical_two_cell_columns_n0_to_n2": 79,
            "full_branch_rays_per_size": 3964,
            "training_size": 5,
            "held_size_no_refit": 6,
            "proper_cubic_frames": 24,
            "ordered_frame_products": 576,
        },
        "resources": {
            "maximal_stars": 2,
            "distinct_coarse_cells": 12,
            "unique_physical_edges": 11,
            "star_private_feature_qutrits": 24,
            "feature_copy_M2": 48,
            "unique_edge_role_M2": 11,
            "edge_local_scratch_M2": 11,
            "total_new_feature_role_scratch_M2": 70,
            "new_M2_per_coarse_cell_on_this_fixed_patch": 70 / 12,
            "global_ordering_M2": 0,
            "Jordan_Wigner_string_M2": 0,
            "host_branch_queries": 0,
            "maximum_projector_support_M2": 4,
            "maximum_update_support_M2": 6,
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            / (1024 * 1024),
        },
        "exact_residuals": {
            "alignment": [row["local_sign_alignment_residual"] for row in alignment_rows],
            "intertwiner": [
                row["role_toggle_intertwining_residual"] for row in alignment_rows
            ],
            "uncorrected": [row["uncorrected_AB_BA_residual"] for row in alignment_rows],
            "mass_difference": abs(
                fixture["two_cell_rest_mass"] - fixture["Cycle219_mass_fixture"]
            ),
        },
        "supplied": (
            "the landed Cycle-311 factor branch representatives, port tags, role gauge and fixed seam",
            "the landed Cycle-315 nearest-neighbor AB/BA physical-ray reducer and n<=2 update fixtures",
            "the landed Cycle-330 center-plus-six-arm geometry and proper-cubic action",
            "the Cycle-658 endpoint identity q=(outer-square factor X contribution, own endpoint-tag X contribution)",
            "one local edge-role M2, one scratch M2 per physical edge, and two M2 per star-private feature copy",
        ),
        "derived": (
            "the three lawful feature words 00,10,01 and exclusion of 11 on all 1104 half-edge branch cases per size",
            "two exact local equality projectors reduce the shared four-qutrit lawful rank from 81 to 9",
            "zero-residual AB/BA alignment on all 3964 physical branch rays at L5 and held L6",
            "an exact unitary chart-toggle intertwiner decomposed into local CNOT, CCZ and edge-role X gates with returned scratch",
            "one shared physical edge/sign gate rather than two silently independent star gates",
            "24-frame and 576-product covariance of the full two-star feature gadget",
            "stable postproduct qutrit-pair ambiguity showing why this copy construction attaches before factor multiplication, while the sign itself remains determined",
            "a stable six-term quadratic Pauli-label sign on all 23784 center-arm term pairs per size, retained strictly as a direct-route diagnostic",
        ),
        "open": (
            "whether the deterministic postproduct nine-M2 sign admits a sparse covariant direct circuit that removes the feature copies",
            "a simultaneous physical encoding of all twelve distinct M64 factors on the two overlapping maximal stars",
            "a local physical implementation of the complete free-plus-contact M64 update on that twelve-cell code",
            "primitive dynamical enforcement/preparation of the branch-ray copy projectors rather than this diagnostic",
            "a recurrence proof when more than two maximal stars share cells and ports",
            "n>2, full M64^12, autonomous collision scheduling, state genesis and volume scaling",
            "minimality, impossibility, shared obstruction, axiom pressure, time, source, Record and probability",
        ),
        "claim_ceiling": (
            "Positive bounded construction for the common edge of two overlapping maximal stars.  "
            "It is an executed physical M2 feature/order-role update and exact AB/BA encoding "
            "intertwiner, not an end-to-end two-star M64 update.  The copy projectors are only "
            "diagnosed, not promoted to a primitive law."
        ),
        "certificate_sha256": digest,
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
