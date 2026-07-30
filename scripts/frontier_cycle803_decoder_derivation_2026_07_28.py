#!/usr/bin/env python3
"""Cycle 803: bounded derivation attempt for the W7 Choi-to-LinkState decoder.

The runner deliberately stops at the first semantic failure.  A signature is
not treated as a construction: the landed Cycle-720 object must determine the
six complex LinkState amplitudes before a decoder is allowed to return one.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import time
from typing import NoReturn

import numpy as np

import frontier_cycle720_companion_fixed_sector_live_input_teleportation_2026_07_27 as L720
import frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27 as P720
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S322
import unit_weight_carried_link_recoil_cycle320_2026_07_18 as U320


ROOT = Path(__file__).resolve().parents[1]
ORIGIN = (0, 0, 0)
AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024

AUDIT_INPUT_PATHS = (
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27.py",
    "scripts/frontier_cycle720_companion_fixed_sector_live_input_teleportation_2026_07_27.py",
    "scripts/frontier_cycle803_decoder_derivation_2026_07_28.py",
)

EXPECTED_SHA256 = {
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py":
        "71fb02658569174b7f6f989efe311951713026ead36ece8866dca1e96878d706",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py":
        "4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py":
        "108568254546e1f64e4454b455f4aa866fe9abfbd4a6ca3a82f65b6a29e28974",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py":
        "f2fc664a1d14a2d62562ff58395840a0174d4cc75239ef2c1589c6e0f65ed982",
    "scripts/frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27.py":
        "ee7d6c6d442bac4fe646535ed46369a649fc8b80eb661044242392058c139628",
    "scripts/frontier_cycle720_companion_fixed_sector_live_input_teleportation_2026_07_27.py":
        "6877d532aaa1c9a97358ce2dfa2e26b1264c1f5a8ef477c217e9cc5a16c8d205",
}


class DecoderSemanticGap(RuntimeError):
    """The landed object does not determine a unique LinkState."""

    def __init__(self, detail: dict[str, object]):
        super().__init__(str(detail["exact_gap"]))
        self.detail = detail


@dataclass(frozen=True)
class PreparedCompanionChoi:
    """Literal Cycle-720 preparation data used by the derivation attempt."""

    fixture: object
    rows: tuple[object, ...]
    tags: tuple[tuple, ...]


def gf2_rank(vectors: tuple[int, ...]) -> int:
    """Exact rank over GF(2), independent of numerical tolerances."""
    pivots: dict[int, int] = {}
    for original in vectors:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return len(pivots)


def bit_columns(bits: int) -> tuple[int, ...]:
    return tuple(index for index in range(bits.bit_length()) if (bits >> index) & 1)


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def decode_companion_choi_to_linkstate(
    prepared: PreparedCompanionChoi,
) -> U320.LinkState:
    """Attempt the only permitted forced reconstruction.

    The Cycle-720 rows define a normalized stabilizer density operator

        rho_J = 2^(-Q) product_j (I + S_j).

    A pure ket exists up to global phase only when the independent commuting
    signed rows have rank Q.  The landed candidate fails that premise before
    any phase convention or U320 position convention can be applied.
    """
    total_qubits = prepared.fixture.qubits + prepared.fixture.matter_qubits
    vectors = tuple(row.symplectic(total_qubits) for row in prepared.rows)
    rank = gf2_rank(vectors)
    support_dimension = 1 << (total_qubits - rank)
    if rank != total_qubits:
        raise DecoderSemanticGap({
            "stage": "exact_stabilizer_reconstruction",
            "forced_formula": "rho_J=2^(-Q)*product_j(I+S_j)",
            "Q": total_qubits,
            "independent_stabilizer_rank": rank,
            "density_operator_rank": support_dimension,
            "nonzero_eigenvalue": f"1/{support_dimension}",
            "purity": f"1/{support_dimension}",
            "unstabilized_logical_M2": total_qubits - rank,
            "exact_gap": (
                "the tableau determines a mixed Choi projector, not a ket; "
                "it contains no landed live-input contraction coefficients "
                "(c_0,...,c_5), no exact-one-occupation projection, and no "
                "pure companion-gauge/LinkState-branch selection"
            ),
            "missing_tableau_datum_with_no_LinkState_image": (
                "the normalized six-component live-input amplitude ray "
                "[c_0:...:c_5] (including all relative phases)"
            ),
        })
    raise AssertionError(
        "unexpected full-rank tableau still requires a Choi-input contraction audit"
    )


def source_anchors() -> dict[str, object]:
    rows = []
    for relative, expected in EXPECTED_SHA256.items():
        path = ROOT / relative
        actual = file_sha256(path)
        rows.append({
            "path": relative,
            "expected_sha256": expected,
            "actual_sha256": actual,
            "match": actual == expected,
        })
    candidate = (
        "scripts/"
        "frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py"
    )
    tracked = subprocess.run(
        ("git", "ls-files", "--error-unmatch", candidate),
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0
    return {
        "rows": rows,
        "all_match": all(row["match"] for row in rows),
        "cycle720_candidate_tracked_on_lineage": tracked,
    }


def exact_direction_inventory() -> dict[str, object]:
    u320_directions = tuple(
        tuple(int(value) for value in row)
        for row in np.asarray(U320.c210.DIRECTIONS)
    )
    s322_directions = tuple(
        tuple(int(value) for value in row)
        for row in np.asarray(S322.c210.DIRECTIONS)
    )
    p720_directions = tuple(
        tuple(int(value) for value in row) for row in P720.R.DIRECTIONS
    )
    direction_rows = tuple({
        "d": direction,
        "Cycle720_R_DIRECTIONS": p720_directions[direction],
        "U320_c210_DIRECTIONS": u320_directions[direction],
        "S322_c210_DIRECTIONS": s322_directions[direction],
        "fixed_relabeling": direction,
        "name": ("+x", "-x", "+y", "-y", "+z", "-z")[direction],
    } for direction in range(6))

    fixture = P720.M.CompanionFixture.build((2, 2, 2))
    edge_rows = []
    edge_failures = 0
    for edge, (left, right, owner, axis, left_mode, right_mode) in enumerate(
        fixture.edges
    ):
        delta = tuple(
            fixture.cells[right][item] - fixture.cells[left][item]
            for item in range(3)
        )
        expected_delta = tuple(int(item == axis) for item in range(3))
        left_local = left_mode % 6
        right_local = right_mode % 6
        valid = (
            delta == expected_delta
            and left_local == 2 * axis + 1
            and right_local == 2 * axis
            and p720_directions[right_local] == delta
            and p720_directions[left_local] == tuple(-item for item in delta)
        )
        edge_failures += not valid
        edge_rows.append({
            "edge": edge,
            "left_cell": fixture.cells[left],
            "right_cell": fixture.cells[right],
            "owner": owner,
            "axis": axis,
            "geometric_delta": delta,
            "left_endpoint_mode": left_local,
            "left_endpoint_direction": p720_directions[left_local],
            "right_endpoint_mode": right_local,
            "right_endpoint_direction": p720_directions[right_local],
            "assignment": (
                "the lower-coordinate endpoint carries the inward -axis port; "
                "the upper-coordinate endpoint carries the inward +axis port"
            ),
            "exact": valid,
        })

    # These are the literal Pauli/tableau columns for cell zero.  X and Z are
    # binary halves over the same Q columns; they are not amplitude columns.
    n_cells = 1
    output_qubits = 9 * n_cells
    column_rows = tuple({
        "direction_d": direction,
        "direction": p720_directions[direction],
        "output_matter_tableau_column": 6 * 0 + direction,
        "output_companion_tableau_column": (
            6 * n_cells + 3 * 0 + direction // 2
        ),
        "companion_Majorana_parity_bit": direction & 1,
        "Choi_input_matter_tableau_column": output_qubits + 6 * 0 + direction,
        "U320_LinkState_excited_column": direction,
    } for direction in range(6))
    return {
        "identification_kind": (
            "literal equality of the two modules' ordered integer direction "
            "tables; fixed relabeling is the identity permutation"
        ),
        "direction_rows": direction_rows,
        "identity_relabeling": p720_directions == u320_directions == s322_directions,
        "reverse_tables": {
            "U320": U320.REVERSE,
            "S322": S322.REVERSE,
            "derived_from_direction_negation": tuple(
                p720_directions.index(tuple(-value for value in row))
                for row in p720_directions
            ),
        },
        "column_correspondence_cell_0": column_rows,
        "edge_assignment_rows_2x2x2": tuple(edge_rows),
        "edge_assignment_failures": edge_failures,
        "semantic_warning": (
            "the exact column identification maps six fermionic mode labels "
            "to six cubic directions; it does not map Pauli bits to six "
            "complex wavefunction amplitudes"
        ),
    }


def prepared_one_cell() -> PreparedCompanionChoi:
    fixture = P720.M.CompanionFixture.build((1, 1, 1))
    rows, tags = P720.direct_graph_basis(fixture)
    return PreparedCompanionChoi(fixture, rows, tags)


def tableau_inventory(
    prepared: PreparedCompanionChoi,
) -> dict[str, object]:
    fixture = prepared.fixture
    total_qubits = fixture.qubits + fixture.matter_qubits
    vectors = tuple(row.symplectic(total_qubits) for row in prepared.rows)
    rank = gf2_rank(vectors)
    commutator_failures = sum(
        P720.M.symplectic(vectors[left], vectors[right], total_qubits)
        for left in range(len(vectors))
        for right in range(left)
    )
    row_rows = tuple({
        "row": index,
        "tag": tag,
        "phase_i_power": row.phase,
        "X_tableau_columns": bit_columns(row.x),
        "Z_tableau_columns": bit_columns(row.z),
        "direction_content": (
            (tag[2],)
            if tag[0] == "onsite_Z"
            else (tag[2], tag[2] + 1)
        ),
    } for index, (row, tag) in enumerate(zip(prepared.rows, prepared.tags)))

    companion_columns = tuple(
        range(fixture.matter_qubits, fixture.qubits)
    )
    used_bits = 0
    for row in prepared.rows:
        used_bits |= row.x | row.z
    unused_companion_columns = tuple(
        column for column in companion_columns
        if not ((used_bits >> column) & 1)
    )

    input_parity = P720.Pauli(
        z=((1 << fixture.matter_qubits) - 1) << fixture.qubits
    )
    augmented = prepared.rows + (input_parity,)
    fixed_rank = gf2_rank(tuple(
        row.symplectic(total_qubits) for row in augmented
    ))
    sector = L720.sector_resource_certificate(fixture)
    pump = P720.pump_algebra_certificate()
    return {
        "fixture": {
            "shape": fixture.shape,
            "cells": fixture.cells,
            "matter_qubits_6N": fixture.matter_qubits,
            "physical_output_qubits_9N": fixture.qubits,
            "Choi_total_qubits_Q_15N": total_qubits,
            "edges": len(fixture.edges),
        },
        "literal_direct_graph_rows": row_rows,
        "row_semantics": {
            "onsite_Z": (
                "Z on output matter mode d times Z on Choi-input matter mode d"
            ),
            "onsite_XX": (
                "X on adjacent output modes d,d+1 times X on adjacent "
                "Choi-input modes d,d+1"
            ),
            "edge": (
                "absent in the one-cell witness; on boxes it is a channel "
                "correlation built from the endpoint-port assignment above"
            ),
        },
        "commuting_Hermitian_failures": (
            commutator_failures
            + sum(row.phase & 1 for row in prepared.rows)
        ),
        "independent_rank": rank,
        "exact_density_reconstruction": {
            "formula": "rho_J=2^(-15)*product_(j=1)^11(I+S_j)",
            "projector_support_dimension": 1 << (total_qubits - rank),
            "normalized_nonzero_eigenvalue": (
                f"1/{1 << (total_qubits - rank)}"
            ),
            "purity": f"1/{1 << (total_qubits - rank)}",
            "pure_up_to_global_phase": rank == total_qubits,
        },
        "unstabilized_output_companion_columns": unused_companion_columns,
        "fixed_parity_augmentation": {
            "rank": fixed_rank,
            "support_dimension": 1 << (total_qubits - fixed_rank),
            "rank_increment": fixed_rank - rank,
            "still_pure": fixed_rank == total_qubits,
            "lineage_certificate": {
                "logical_qubits_in_fixed_parity_sector":
                    sector["logical_qubits_in_fixed_parity_sector"],
                "mixed_gauge_M2": sector["mixed_gauge_M2"],
                "normalized_fixed_sector_input_marginal":
                    sector["normalized_fixed_sector_input_marginal"],
                "input_marginal_stabilizer_kernel_rank":
                    sector["input_marginal_stabilizer_kernel_rank"],
                "Choi_graph_rank_equals_2L_plus_C":
                    sector["Choi_graph_rank_equals_2L_plus_C"],
            },
        },
        "candidate_scope_rerun": {
            "direct_rows_exact": len(prepared.rows) == 11,
            "direct_rank_exact": rank == 11,
            "pump_output_plus_failures":
                pump["canonical_output_plus_failures"],
            "pump_trace_preservation_failures":
                pump["canonical_trace_preservation_failures"],
        },
    }


def identity_link_state(direction: int) -> U320.LinkState:
    vector = np.zeros(6, dtype=complex)
    vector[direction] = 1
    return U320.LinkState({ORIGIN: vector}, {})


def linkstate_validity(state: U320.LinkState) -> dict[str, object]:
    excited_shapes = tuple(
        (position, tuple(value.shape)) for position, value in state.excited.items()
    )
    pair_shapes = tuple(
        (positions, tuple(value.shape)) for positions, value in state.pair.items()
    )
    finite = all(
        np.all(np.isfinite(value))
        for value in tuple(state.excited.values()) + tuple(state.pair.values())
    )
    shape_valid = (
        all(shape == (6,) for _key, shape in excited_shapes)
        and all(shape == (6, 6, 6) for _key, shape in pair_shapes)
    )
    norm = U320.state_norm(state)
    return {
        "is_U320_LinkState": isinstance(state, U320.LinkState),
        "excited_shapes": excited_shapes,
        "pair_shapes": pair_shapes,
        "finite_complex_amplitudes": bool(finite),
        "state_norm": norm,
        "normalized": norm == 1.0,
        "domain_shapes_valid": shape_valid,
        "constructor_enforcement": (
            "U320.LinkState is a dataclass with no __post_init__; validity is "
            "therefore reproduced with U320.state_norm plus literal 6 and "
            "6x6x6 domain shapes"
        ),
    }


def u320_defining_rows() -> dict[str, object]:
    exchange, vertex, _charge, _momenta = U320.link_recoil_vertex(U320.ANGLE)
    directions = np.asarray(U320.c210.DIRECTIONS, dtype=int)
    maximum_column_residual = 0.0
    response_rows = []
    source_rows = []
    for direction in range(6):
        pair_coordinate = (U320.REVERSE[direction], direction, direction)
        pair_flat = (
            6
            + 36 * pair_coordinate[0]
            + 6 * pair_coordinate[1]
            + pair_coordinate[2]
        )
        nonzero_exchange_rows = tuple(
            int(row) for row in np.flatnonzero(exchange[:, direction])
        )
        expected_exchange_rows = (pair_flat,)
        initial = np.zeros(222, dtype=complex)
        initial[direction] = 1
        expected = np.zeros(222, dtype=complex)
        expected[direction] = np.cos(U320.ANGLE)
        expected[pair_flat] = 1j * np.sin(U320.ANGLE)
        actual = vertex @ initial
        residual = float(np.linalg.norm(actual - expected))
        maximum_column_residual = max(maximum_column_residual, residual)
        source_rows.append({
            "direction": direction,
            "direction_vector": tuple(int(value) for value in directions[direction]),
            "exchange_law": (
                f"E_{direction} <-> "
                f"G_{U320.REVERSE[direction]},F_{direction},A_{direction}"
            ),
            "pair_tensor_coordinate": pair_coordinate,
            "vertex_flat_row": pair_flat,
            "literal_exchange_nonzero_rows": nonzero_exchange_rows,
            "expected_exchange_nonzero_rows": expected_exchange_rows,
            "vertex_column_formula": (
                f"cos(ANGLE) E_{direction} + i sin(ANGLE) "
                f"P_{pair_coordinate}"
            ),
            "column_residual": residual,
        })

        excited, pair = U320.local_vertex(
            identity_link_state(direction).excited[ORIGIN],
            U320.zero_tensor(),
            U320.ANGLE,
        )
        probabilities = abs(pair) ** 2
        matter_weights = abs(excited) ** 2 + np.sum(probabilities, axis=(1, 2))
        field_weights = np.sum(probabilities, axis=(0, 2))
        auxiliary_weights = np.sum(probabilities, axis=(0, 1))
        initial_vector = directions[direction].astype(float)
        final_matter = matter_weights @ directions
        mediator_flux = field_weights @ directions
        auxiliary_flux = auxiliary_weights @ directions
        response_rows.append({
            "direction": direction,
            "input_identity_column": direction,
            "matter_recoil": tuple(
                float(value) for value in final_matter - initial_vector
            ),
            "mediator_flux": tuple(float(value) for value in mediator_flux),
            "auxiliary_flux": tuple(float(value) for value in auxiliary_flux),
            "additive_kernel_formula": {
                "matter_recoil": "-2*sin(ANGLE)^2*DIRECTIONS[d]",
                "mediator_flux": "sin(ANGLE)^2*DIRECTIONS[d]",
                "auxiliary_flux": "sin(ANGLE)^2*DIRECTIONS[d]",
            },
            "balance_residual": float(np.linalg.norm(
                final_matter + mediator_flux + auxiliary_flux - initial_vector
            )),
        })
    validity_rows = tuple(
        linkstate_validity(identity_link_state(direction))
        for direction in range(6)
    )
    return {
        "ANGLE": U320.ANGLE,
        "REVERSE": U320.REVERSE,
        "local_active_dimension": 222,
        "source_rows": tuple(source_rows),
        "identity_column_response_rows": tuple(response_rows),
        "maximum_vertex_column_residual": maximum_column_residual,
        "maximum_balance_residual": max(
            row["balance_residual"] for row in response_rows
        ),
        "identity_LinkState_validity": validity_rows,
        "all_defining_rows_reproduced": (
            maximum_column_residual < U320.TOLERANCE
            and max(row["balance_residual"] for row in response_rows)
            < U320.TOLERANCE
            and all(
                row["is_U320_LinkState"]
                and row["normalized"]
                and row["domain_shapes_valid"]
                and row["finite_complex_amplitudes"]
                for row in validity_rows
            )
        ),
    }


def attempt_decoder(
    prepared: PreparedCompanionChoi,
) -> dict[str, object]:
    forced_steps = (
        {
            "step": 1,
            "status": "FORCED",
            "operation": (
                "read the signed commuting Pauli rows and reconstruct "
                "rho_J=2^(-Q) product_j(I+S_j)"
            ),
        },
        {
            "step": 2,
            "status": "FORCED",
            "operation": (
                "identify matter-mode d with cubic direction d by equality "
                "of the landed ordered direction tables"
            ),
        },
        {
            "step": 3,
            "status": "FORCED",
            "operation": (
                "test exact GF(2) stabilizer rank before choosing a ket or "
                "global phase"
            ),
        },
    )
    try:
        state = decode_companion_choi_to_linkstate(prepared)
    except DecoderSemanticGap as error:
        return {
            "constructed": False,
            "forced_steps": forced_steps,
            "obstruction": error.detail,
            "supplies_not_taken": (
                {
                    "datum": "live input / Choi-input contraction",
                    "reason": (
                        "would select the physical output state rather than "
                        "decode a datum already in the Choi resource"
                    ),
                },
                {
                    "datum": "exact-one-occupation projection on six modes",
                    "reason": (
                        "fixed fermion parity admits 32 basis states at one "
                        "cell, while U320's excited sector is C^6"
                    ),
                },
                {
                    "datum": "pure value of the three companion gauge M2",
                    "reason": "the fixed-sector lineage explicitly keeps it mixed",
                },
                {
                    "datum": "U320 excited/pair branch and position selection",
                    "reason": (
                        "the Choi tableau has physical/input Pauli columns, "
                        "not LinkState dictionary keys or branch tensors"
                    ),
                },
                {
                    "datum": "global phase convention",
                    "reason": (
                        "a harmless possible supply, but it cannot repair "
                        "mixedness or create the missing relative amplitudes"
                    ),
                },
            ),
            "return_value": None,
            "U320_input_validity_reached": False,
        }
    return {
        "constructed": True,
        "forced_steps": forced_steps,
        "obstruction": None,
        "return_value": linkstate_validity(state),
        "U320_input_validity_reached": True,
    }


def calibration_counterexample(
    decoder_attempt: dict[str, object],
) -> dict[str, object]:
    column_zero = identity_link_state(0)
    column_one = identity_link_state(1)
    difference = (
        column_zero.excited[ORIGIN] - column_one.excited[ORIGIN]
    )
    squared_residual = int(np.vdot(difference, difference).real)
    return {
        "status": "FAIL_NOT_WELL_DEFINED",
        "lineage_fact": (
            "the fixed-sector live-input sibling proves corrected-channel "
            "identity for every supplied live input while the gauge remains "
            "mixed; it does not store that live input in the Choi tableau"
        ),
        "two_inputs_admitted_by_the_same_odd_sector_resource": (
            "|100000> (direction 0)",
            "|010000> (direction 1)",
        ),
        "required_U320_outputs": ("e_0", "e_1"),
        "same_resource_equations_that_a_resource_only_decoder_would_need": (
            "D(T_odd)=e_0",
            "D(T_odd)=e_1",
        ),
        "exact_squared_LinkState_residual_between_required_outputs":
            squared_residual,
        "LinkState_residual": U320.state_residual(column_zero, column_one),
        "exact_mismatch": (
            "e_0 != e_1 (squared distance 2), so one function of the "
            "unchanged tableau cannot satisfy both identity columns"
        ),
        "candidate_prepares_recognizable_basis_state": False,
        "candidate_accepts_separately_supplied_basis_state": True,
        "decoder_constructed": decoder_attempt["constructed"],
        "stop_rule": (
            "calibration failure means stop before the composite test"
        ),
    }


def derive_report() -> dict[str, object]:
    prepared = prepared_one_cell()
    anchors = source_anchors()
    directions = exact_direction_inventory()
    inventory = tableau_inventory(prepared)
    decoder = attempt_decoder(prepared)
    calibration = calibration_counterexample(decoder)
    defining_rows = u320_defining_rows()
    certificate_a = (
        anchors["all_match"]
        and anchors["cycle720_candidate_tracked_on_lineage"]
        and directions["identity_relabeling"]
        and directions["edge_assignment_failures"] == 0
        and inventory["commuting_Hermitian_failures"] == 0
        and inventory["candidate_scope_rerun"]["direct_rows_exact"]
        and inventory["candidate_scope_rerun"]["direct_rank_exact"]
        and inventory["candidate_scope_rerun"]["pump_output_plus_failures"] == 0
        and inventory["candidate_scope_rerun"][
            "pump_trace_preservation_failures"
        ] == 0
    )
    certificate_b = decoder["constructed"]
    certificate_c = calibration["status"] == "PASS"
    certificate_d = (
        not decoder["constructed"]
        and calibration["status"] == "FAIL_NOT_WELL_DEFINED"
        and calibration[
            "exact_squared_LinkState_residual_between_required_outputs"
        ] == 2
    )
    return {
        "outcome": "OBSTRUCTED_DEEPER",
        "anchors": anchors,
        "semantic_inventory": {
            "directions_and_columns": directions,
            "tableau_and_state_content": inventory,
        },
        "decoder_construction": decoder,
        "calibration_identity": calibration,
        "composite_test": {
            "reached": False,
            "cross_term_census": "NOT_RUN_BY_FROZEN_CALIBRATION_STOP_RULE",
            "response_rows_vs_kernel_additive_prediction":
                "NOT_RUN_BY_FROZEN_CALIBRATION_STOP_RULE",
            "law_claim": "NONE",
            "honest_obstruction": decoder["obstruction"]["exact_gap"],
        },
        "U320_defining_rows_control": defining_rows,
        "certificates": {
            "A": certificate_a,
            "B": certificate_b,
            "C": certificate_c,
            "D": certificate_d,
        },
    }


def json_block(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True)


def report_lines(report: dict[str, object]) -> list[str]:
    cert = report["certificates"]
    lines = [
        "CYCLE 803: DERIVE THE DECODER BETWEEN W7 AND ITS SCOPE",
        "authority=none; audit=unset; claim=bounded derivation attempt",
        "",
        "CONTROL: LITERAL AUDIT INPUT PATHS",
        "AUDIT_INPUT_PATHS = " + repr(AUDIT_INPUT_PATHS),
        "",
        "A. SHA ANCHORS AND SEMANTIC INVENTORY",
        json_block(report["anchors"]),
        json_block(report["semantic_inventory"]),
        (
            ("PASS" if cert["A"] else "FAIL")
            + " CERTIFICATE A: anchors, exact direction identification, "
            "tableau rows, and candidate-scope checks"
        ),
        "",
        "B. DECODER CONSTRUCTION ATTEMPT",
        json_block(report["decoder_construction"]),
        (
            ("PASS" if cert["B"] else "FAIL")
            + " CERTIFICATE B: decode_companion_choi_to_linkstate construction"
        ),
        "",
        "C. CALIBRATION IDENTITY",
        json_block(report["calibration_identity"]),
        (
            ("PASS" if cert["C"] else "FAIL")
            + " CERTIFICATE C: calibration identity"
        ),
        "",
        "D. COMPOSITE TEST OR HONEST OBSTRUCTION",
        json_block(report["composite_test"]),
        (
            ("PASS" if cert["D"] else "FAIL")
            + " CERTIFICATE D: honest obstruction and frozen stop before "
            "composite execution"
        ),
        "",
        "CONTROL: U320 DEFINING SOURCE AND RESPONSE ROWS REPRODUCED",
        json_block(report["U320_defining_rows_control"]),
        "",
        "OUTCOME ARGUMENT",
        (
            "The geometry is identified exactly, but geometry labels do not "
            "supply amplitudes.  On one cell the landed 11-row tableau has "
            "Q=15 and exact rank 11, hence rho_J has rank 16 and purity 1/16. "
            "Fixing parity adds one row but leaves rank 8 because the companion "
            "gauge is mixed.  The live-input sibling makes the missing datum "
            "explicit: a separate fixed-sector live ket is Bell-coupled to the "
            "resource.  Since the same resource accepts e_0 and e_1 and those "
            "required U320 outputs have exact squared distance 2, no function "
            "of the prepared Choi/tableau alone can satisfy the calibration. "
            "Supplying that ket would choose the answer, not decode it."
        ),
    ]
    return lines


def render_with_certificate_e(
    prefix: list[str],
    *,
    e_base: bool,
    deterministic: bool,
    elapsed_seconds: float,
    stdout_bytes: int,
) -> str:
    e_pass = e_base and stdout_bytes < STDOUT_LIMIT_BYTES
    lines = prefix + [
        "",
        (
            ("PASS" if e_pass else "FAIL")
            + " CERTIFICATE E: controls; "
            + f"deterministic={deterministic}; "
            + f"runtime_seconds={elapsed_seconds:.6f}; "
            + f"runtime_limit_seconds={AUDIT_TIMEOUT_SEC}; "
            + f"stdout_bytes={stdout_bytes}; "
            + f"stdout_limit_bytes={STDOUT_LIMIT_BYTES}"
        ),
        "RESULT OBSTRUCTED_DEEPER",
        (
            "EXACT_SEMANTIC_GAP: no landed tableau datum contains the "
            "normalized six-component live-input amplitude ray "
            "[c_0:...:c_5] or its LinkState branch/position image"
        ),
        f"RUNTIME_SECONDS {elapsed_seconds:.6f}",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    started = time.monotonic()
    first = derive_report()
    second = derive_report()
    deterministic = (
        json.dumps(first, sort_keys=True, separators=(",", ":"))
        == json.dumps(second, sort_keys=True, separators=(",", ":"))
    )
    elapsed = time.monotonic() - started
    paths_exist = all((ROOT / relative).is_file() for relative in AUDIT_INPUT_PATHS)
    certificates = first["certificates"]
    e_base = (
        deterministic
        and paths_exist
        and elapsed < AUDIT_TIMEOUT_SEC
        and first["anchors"]["all_match"]
        and first["anchors"]["cycle720_candidate_tracked_on_lineage"]
        and certificates["A"]
        and certificates["D"]
        and first["U320_defining_rows_control"]["all_defining_rows_reproduced"]
    )
    prefix = report_lines(first)

    byte_count = 0
    for _iteration in range(8):
        rendered = render_with_certificate_e(
            prefix,
            e_base=e_base,
            deterministic=deterministic,
            elapsed_seconds=elapsed,
            stdout_bytes=byte_count,
        )
        next_count = len(rendered.encode("utf-8"))
        if next_count == byte_count:
            break
        byte_count = next_count
    rendered = render_with_certificate_e(
        prefix,
        e_base=e_base,
        deterministic=deterministic,
        elapsed_seconds=elapsed,
        stdout_bytes=byte_count,
    )
    final_count = len(rendered.encode("utf-8"))
    if final_count != byte_count:
        raise AssertionError((byte_count, final_count))
    print(rendered, end="")
    return 0 if e_base and final_count < STDOUT_LIMIT_BYTES else 1


if __name__ == "__main__":
    raise SystemExit(main())
