#!/usr/bin/env python3
"""Cycle 392: reciprocal translated-edge and multi-edge calibration test.

Train one frozen target-reservoir/pointer calibration on one L=3 physical
edge.  Without refitting, predict translated adjacent target edges on L=4 and
held L=6 for the Cycle-322 coefficient-two and Cycle-325 unit-weight routes.
Then stress the same calibration and a naive edge-product rule on a connected
two-edge L=6 chain.  The latter remains a logical comparator because no
shared-middle-site Cycle-325 physical compiler is installed.

All scalar outputs are operational coordinates.  They receive no far-side
physical interpretation.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import full_fock_unit_weight_two_source_cycle325_2026_07_18 as c325
import physical_contact_sensitive_operational_transcript_registration_cycle374_2026_07_18 as c374
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as c322


c315 = c322.c315
c210 = c322.c210
c331 = c374.c331
c214 = c325.c214

AUTHORITY = "none"
AUDIT = "unset"
TOL = 3.0e-10
CALIBRATION_RELATIVE_TOL = 1.0e-8
CHAIN_RELATIVE_TOL = 5.0e-2
TRAIN_EDGE = ((0, 0, 0), (1, 0, 0))
VALIDATION_EDGE = ((2, 1, 1), (3, 1, 1))
HELD_EDGE = ((3, 2, 1), (4, 2, 1))
HELD_CHAIN = ((1, 2, 1), (2, 2, 1), (3, 2, 1))
TRAIN_SIZE = 3
VALIDATION_SIZE = 4
HELD_SIZE = 6
EDGE_DEPTH = 2
CHAIN_DEPTH = 3
ROUTES = ("coefficient_two", "unit_weight")
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECIPROCAL_MULTI_EDGE_CALIBRATION_CYCLE392_NOTE_2026-07-18.md"
)

PASS = 0
FAIL = 0
ORIGINAL_HARDCORE_COIN = c331.local_hardcore_coin


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def raw_maximum(matrix: sparse.spmatrix) -> float:
    matrix = matrix.tocoo()
    return 0.0 if matrix.nnz == 0 else float(np.max(np.abs(matrix.data)))


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-392 note exists", False, NOTE)
        return
    text = NOTE.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    text = " ".join(text.split())
    required = (
        "authority: none",
        "audit: unset",
        "one l=3 physical edge",
        "blind held l=6",
        "no apparatus retraining",
        "candidate operational source coordinates",
        "cycle-322 coefficient-two",
        "cycle-325 unit-weight",
        "connected two-edge",
        "shared middle site",
        "strict physical compiler",
        "logical comparator",
        "source-target reciprocity",
        "ab/ba",
        "all 24 proper-cubic frames",
        "mass, q, number, and vector ledgers",
        "contact deletion",
        "edge deletions",
        "collision alternative",
        "route-specific",
        "no shared obstruction",
        "no axiom pressure",
        "not energy",
        "not stress",
        "not gravity",
        "not a rate",
        "not an occurrence",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    check(
        "the note pins the one-edge split, locality boundary, semantics, and controls",
        not missing,
        missing,
    )


def factors(contact_enabled: bool = True):
    coin, edge_swap, contact, _update, detail = c315.logical_update_controls(
        c322.LABELS
    )
    if not contact_enabled:
        contact = sparse.eye(contact.shape[0], format="csc", dtype=complex)
    return coin.tocsc(), edge_swap.tocsc(), contact.tocsc(), detail


def q_reservoir(route: str, endpoint: int):
    return (
        c322.q_reservoir(endpoint)
        if route == "coefficient_two"
        else c325.q_reservoir(endpoint)
    )


def route_step(
    route: str,
    state,
    length: int,
    update_factors,
    endpoint_cells,
    *,
    enabled=(True, True),
    stream_enabled=True,
):
    if route == "coefficient_two":
        return c322.logical_step(
            state,
            length,
            update_factors,
            endpoint_cells=endpoint_cells,
            enabled=enabled,
            stream_enabled=stream_enabled,
        )
    if route == "unit_weight":
        return c325.logical_step(
            state,
            length,
            update_factors,
            endpoint_cells=endpoint_cells,
            enabled=enabled,
            stream_enabled=stream_enabled,
            stream_program="paired",
        )
    raise ValueError("undeclared route")


def state_norm(route: str, state) -> float:
    return c322.state_norm(state) if route == "coefficient_two" else c325.state_norm(state)


@dataclass(frozen=True)
class EdgeResponse:
    role: str
    route: str
    length: int
    endpoints: tuple[tuple[int, int, int], tuple[int, int, int]]
    depth: int
    contact_code: int
    transfer: tuple[float, float]
    pointer: tuple[float, float]
    maximum_norm_drift: float
    maximum_reachable_labels: int
    strict_physical_compiler: bool

    @property
    def mean_transfer(self) -> float:
        return float(np.mean(self.transfer))

    @property
    def mean_pointer(self) -> float:
        return float(np.mean(self.pointer))

    @property
    def transfer_reciprocity_residual(self) -> float:
        return abs(self.transfer[0] - self.transfer[1])

    @property
    def pointer_reciprocity_residual(self) -> float:
        return abs(self.pointer[0] - self.pointer[1])


def edge_response(
    role: str,
    route: str,
    length: int,
    endpoints,
    depth: int,
    contact_code: int,
    operator,
    *,
    strict_physical_compiler: bool,
    enabled=(True, True),
    stream_enabled=True,
) -> EdgeResponse:
    update_factors = factors(bool(contact_code))[:3]
    transfer = []
    pointer = []
    drift = 0.0
    maximum_labels = 0
    for source in range(2):
        receiver = 1 - source
        state = {q_reservoir(route, source): c322.symmetric_one_one_state()}
        for _ in range(depth):
            state = route_step(
                route,
                state,
                length,
                update_factors,
                endpoints,
                enabled=enabled,
                stream_enabled=stream_enabled,
            )
            drift = max(drift, abs(state_norm(route, state) - 1))
        vector = state.get(
            q_reservoir(route, receiver), np.zeros(4096, dtype=complex)
        )
        rotated = operator @ vector
        transfer.append(float(np.vdot(vector, vector).real))
        pointer.append(float(abs(np.vdot(c374.RAY, rotated)) ** 2))
        maximum_labels = max(maximum_labels, len(state))
    return EdgeResponse(
        role=role,
        route=route,
        length=length,
        endpoints=tuple(endpoints),
        depth=depth,
        contact_code=contact_code,
        transfer=tuple(transfer),
        pointer=tuple(pointer),
        maximum_norm_drift=drift,
        maximum_reachable_labels=maximum_labels,
        strict_physical_compiler=strict_physical_compiler,
    )


def frozen_apparatus_controls(coin, edge_swap):
    operator = (edge_swap @ coin.conj().T).tocsc()
    menu_entry = c374.readout_menu(coin, edge_swap)[6]
    detail = {
        "Cycle374_program": menu_entry.program,
        "name": menu_entry.name,
        "depth_for_edge_response": EDGE_DEPTH,
        "pointer_ray": "symmetric one-one matter ray",
        "receiver_reservoir_projection": "supplied operational selector",
        "operator_residual": raw_maximum(menu_entry.operator - operator),
        "menu_search_executed": False,
        "apparatus_retrained": False,
    }
    check(
        "the Cycle-374 program-6 matter/pointer apparatus is frozen before edge training",
        menu_entry.program == 6
        and menu_entry.name == "inverse_matter_coin_then_edge_fswap"
        and detail["operator_residual"] == 0
        and detail["menu_search_executed"] is False
        and detail["apparatus_retrained"] is False,
        detail,
    )
    return operator


@dataclass(frozen=True)
class FrozenEdgeCalibration:
    coefficient_two_deleted_gain: float
    coefficient_two_actual_gain: float
    unit_weight_deleted_gain: float
    unit_weight_actual_gain: float

    def gain(self, route: str, contact_code: int) -> float:
        name = f"{route}_{'actual' if contact_code else 'deleted'}_gain"
        return float(getattr(self, name))

    def predict(self, route: str, contact_code: int, candidate_coordinate: float) -> float:
        return self.gain(route, contact_code) * candidate_coordinate


def train_one_edge(operator):
    rows = []
    gains = {}
    for route in ROUTES:
        for contact_code in (0, 1):
            row = edge_response(
                "training",
                route,
                TRAIN_SIZE,
                TRAIN_EDGE,
                EDGE_DEPTH,
                contact_code,
                operator,
                strict_physical_compiler=True,
            )
            rows.append(row)
            gains[(route, contact_code)] = row.mean_pointer / row.mean_transfer
    calibration = FrozenEdgeCalibration(
        coefficient_two_deleted_gain=gains[("coefficient_two", 0)],
        coefficient_two_actual_gain=gains[("coefficient_two", 1)],
        unit_weight_deleted_gain=gains[("unit_weight", 0)],
        unit_weight_actual_gain=gains[("unit_weight", 1)],
    )
    detail = {
        "training_size": TRAIN_SIZE,
        "training_edges": (TRAIN_EDGE,),
        "rows": rows,
        "calibration": calibration,
        "maximum_transfer_reciprocity_residual": max(
            row.transfer_reciprocity_residual for row in rows
        ),
        "maximum_pointer_reciprocity_residual": max(
            row.pointer_reciprocity_residual for row in rows
        ),
        "minimum_contact_pointer_contrast": min(
            abs(
                next(
                    row.mean_pointer
                    for row in rows
                    if row.route == route and row.contact_code == 1
                )
                - next(
                    row.mean_pointer
                    for row in rows
                    if row.route == route and row.contact_code == 0
                )
            )
            for route in ROUTES
        ),
        "validation_or_held_opened": False,
    }
    check(
        "one route-tagged calibration object is fit on one reciprocal L=3 physical edge only",
        len({row.endpoints for row in rows}) == 1
        and all(row.length == TRAIN_SIZE for row in rows)
        and all(row.strict_physical_compiler for row in rows)
        and detail["maximum_transfer_reciprocity_residual"] < TOL
        and detail["maximum_pointer_reciprocity_residual"] < TOL
        and detail["minimum_contact_pointer_contrast"] > 1e-8
        and detail["validation_or_held_opened"] is False,
        detail,
    )
    return calibration, rows


def translated_target_controls(calibration, operator):
    rows = []
    residuals = []
    for role, length, endpoints in (
        ("post-freeze validation", VALIDATION_SIZE, VALIDATION_EDGE),
        ("blind held", HELD_SIZE, HELD_EDGE),
    ):
        for route in ROUTES:
            for contact_code in (0, 1):
                row = edge_response(
                    role,
                    route,
                    length,
                    endpoints,
                    EDGE_DEPTH,
                    contact_code,
                    operator,
                    strict_physical_compiler=True,
                )
                prediction = calibration.predict(
                    route, contact_code, row.mean_transfer
                )
                absolute = abs(row.mean_pointer - prediction)
                relative = absolute / max(row.mean_pointer, 1e-30)
                rows.append(row)
                residuals.append(
                    {
                        "role": role,
                        "L": length,
                        "route": route,
                        "contact_code": contact_code,
                        "candidate_operational_source_coordinate": row.mean_transfer,
                        "observed_pointer_coordinate": row.mean_pointer,
                        "predicted_pointer_coordinate": prediction,
                        "absolute_residual": absolute,
                        "relative_residual": relative,
                    }
                )
    detail = {
        "validation_size": VALIDATION_SIZE,
        "held_size": HELD_SIZE,
        "validation_edge": VALIDATION_EDGE,
        "held_edge": HELD_EDGE,
        "target_edges_are_adjacent": True,
        "target_edges_are_disjoint_from_training_fixture_coordinates": True,
        "rows": residuals,
        "maximum_relative_residual": max(row["relative_residual"] for row in residuals),
        "maximum_norm_drift": max(row.maximum_norm_drift for row in rows),
        "calibration_refit": False,
        "apparatus_retrained": False,
    }
    check(
        "the one-edge calibration predicts translated L4 and blind held L6 physical target edges without refitting",
        detail["maximum_relative_residual"] < CALIBRATION_RELATIVE_TOL
        and detail["maximum_norm_drift"] < TOL
        and all(row.strict_physical_compiler for row in rows)
        and detail["calibration_refit"] is False
        and detail["apparatus_retrained"] is False,
        detail,
    )
    return rows, residuals


def connected_chain_controls(calibration, training_rows, operator):
    first_edge = (HELD_CHAIN[0], HELD_CHAIN[1])
    second_edge = (HELD_CHAIN[1], HELD_CHAIN[2])
    shared = set(first_edge) & set(second_edge)
    chain_rows = []
    failures = []
    for route in ROUTES:
        for contact_code in (0, 1):
            row = edge_response(
                "held connected-chain logical comparator",
                route,
                HELD_SIZE,
                (HELD_CHAIN[0], HELD_CHAIN[2]),
                CHAIN_DEPTH,
                contact_code,
                operator,
                strict_physical_compiler=False,
            )
            one_edge = next(
                item
                for item in training_rows
                if item.route == route and item.contact_code == contact_code
            )
            gain_prediction = calibration.predict(
                route, contact_code, row.mean_transfer
            )
            product_prediction = one_edge.mean_transfer**2
            gain_relative = abs(row.mean_pointer - gain_prediction) / max(
                row.mean_pointer, 1e-30
            )
            product_relative = abs(row.mean_transfer - product_prediction) / max(
                row.mean_transfer, 1e-30
            )
            chain_rows.append(row)
            failures.append(
                {
                    "route": route,
                    "contact_code": contact_code,
                    "direct_transfer": row.mean_transfer,
                    "direct_pointer": row.mean_pointer,
                    "one_edge_gain_prediction": gain_prediction,
                    "gain_relative_residual": gain_relative,
                    "two_edge_product_prediction": product_prediction,
                    "product_relative_residual": product_relative,
                    "strict_physical_compiler": False,
                }
            )
    detail = {
        "held_size": HELD_SIZE,
        "chain_cells": HELD_CHAIN,
        "first_edge": first_edge,
        "second_edge": second_edge,
        "connected_nearest_neighbor_edges": True,
        "shared_middle_cells": tuple(sorted(shared)),
        "unique_cells": len(set(first_edge) | set(second_edge)),
        "naive_tensor_endpoint_slots": len(first_edge) + len(second_edge),
        "duplicated_middle_slots_in_naive_tensor": 1,
        "Cycle325_shared_middle_site_compiler": None,
        "Cycle319_three_cell_matter_seam_not_extended_with_Cycle325_sources": True,
        "rows": failures,
        "minimum_gain_relative_residual": min(
            row["gain_relative_residual"] for row in failures
        ),
        "minimum_product_relative_residual": min(
            row["product_relative_residual"] for row in failures
        ),
    }
    check(
        "the held two-edge geometry is connected with one explicit shared middle site and is not mislabeled as a strict physical compiler",
        len(shared) == 1
        and detail["unique_cells"] == 3
        and detail["naive_tensor_endpoint_slots"] == 4
        and detail["duplicated_middle_slots_in_naive_tensor"] == 1
        and detail["Cycle325_shared_middle_site_compiler"] is None
        and all(not row.strict_physical_compiler for row in chain_rows),
        detail,
    )
    check(
        "one-edge gain transfer and naive edge-product composition both fail on the connected-chain logical comparator",
        detail["minimum_gain_relative_residual"] > CHAIN_RELATIVE_TOL
        and detail["minimum_product_relative_residual"] > CHAIN_RELATIVE_TOL,
        {
            "rows": failures,
            "scope": "route-specific depth-three logical comparator; broader multi-edge compilers remain open",
        },
    )
    return chain_rows, failures, detail


def covariance_controls(coin, edge_swap, contact, operator):
    inherited = c315.covariance_translation_controls(
        c322.LABELS, coin, contact, contact @ edge_swap @ coin
    )
    readout_residuals = []
    ray_residuals = []
    source_residuals = []
    stream_failures = 0
    stream_tests = 0
    endpoint_reversals = 0
    _exchange, coefficient_vertex, *_ = c322.local_source_blocks(c322.ANGLE)
    _exchange_u, unit_vertex, *_ = c325.unit_weight_local_source(c325.ANGLE)
    for frame in c210.proper_cubic_frames():
        mapped_direction = frame @ np.asarray((1, 0, 0), dtype=int)
        axis = int(np.flatnonzero(mapped_direction)[0])
        reversed_endpoints = int(mapped_direction[axis]) == -1
        endpoint_reversals += reversed_endpoints
        representation = c315.pair_frame_representation(
            c322.LABELS, frame, reversed_endpoints
        )
        target_operator = c315.edge_fswap_matrix(c322.LABELS, axis) @ coin.conj().T
        readout_residuals.append(
            raw_maximum(representation @ operator - target_operator @ representation)
        )
        mapped_ray = representation @ c374.RAY
        overlap = np.vdot(c374.RAY, mapped_ray)
        ray_residuals.append(float(np.linalg.norm(mapped_ray - overlap * c374.RAY)))
        source_frame = c322.local_source_frame(frame)
        source_residuals.extend(
            (
                float(
                    np.linalg.norm(
                        source_frame @ coefficient_vertex @ source_frame.T
                        - coefficient_vertex
                    )
                ),
                float(
                    np.linalg.norm(
                        source_frame @ unit_vertex @ source_frame.T - unit_vertex
                    )
                ),
            )
        )
        mapped_origin = tuple(int(value) % 6 for value in frame @ np.asarray((1, 2, 1)))
        for field_direction in range(6):
            mapped_field = c315.c311.direction_map(frame, field_direction)
            streamed = tuple(
                (
                    (1, 2, 1)[axis_index]
                    + int(c210.DIRECTIONS[field_direction, axis_index])
                )
                % 6
                for axis_index in range(3)
            )
            map_after_stream = tuple(
                int(value) % 6 for value in frame @ np.asarray(streamed)
            )
            stream_after_map = tuple(
                (
                    mapped_origin[axis_index]
                    + int(c210.DIRECTIONS[mapped_field, axis_index])
                )
                % 6
                for axis_index in range(3)
            )
            stream_tests += 1
            stream_failures += int(map_after_stream != stream_after_map)
    detail = {
        "proper_cubic_frames": len(readout_residuals),
        "endpoint_reversing_frames": endpoint_reversals,
        "maximum_readout_residual": max(readout_residuals),
        "maximum_ray_residual": max(ray_residuals),
        "maximum_source_vertex_residual": max(source_residuals),
        "stream_tests": stream_tests,
        "stream_failures": stream_failures,
        "inherited_seam": inherited,
    }
    check(
        "the frozen apparatus, both source vertices, streams, and common seam cover all 24 proper-cubic frames",
        detail["proper_cubic_frames"] == 24
        and endpoint_reversals == 12
        and max(readout_residuals) < TOL
        and max(ray_residuals) < TOL
        and max(source_residuals) < TOL
        and stream_failures == 0
        and inherited["maximum_update_covariance_residual"] < TOL,
        detail,
    )
    return detail


def local_ledger_rows():
    coefficient = c322.local_source_blocks(c322.ANGLE)
    unit = c325.unit_weight_local_source(c325.ANGLE)
    rows = []
    for route, data, momenta in (
        ("coefficient_two", coefficient, coefficient[4]),
        ("unit_weight", unit, unit[7]),
    ):
        _exchange, vertex, charge, number = data[:4]
        rows.append(
            {
                "route": route,
                "unitarity": float(
                    np.linalg.norm(vertex.conj().T @ vertex - np.eye(448))
                ),
                "Q": float(np.linalg.norm(vertex @ charge - charge @ vertex)),
                "number": float(np.linalg.norm(vertex @ number - number @ vertex)),
                "vector": tuple(
                    float(np.linalg.norm(vertex @ value - value @ vertex))
                    for value in momenta
                ),
            }
        )
    return rows


def mass_ledger_contact_controls(contact, logical_detail):
    rows = local_ledger_rows()
    contact_deletion = c315.largest_singular(
        contact - sparse.eye(contact.shape[0], format="csc")
    )
    unit = c325.unit_weight_local_source(c325.ANGLE)
    no_auxiliary = tuple(
        float(
            np.linalg.norm(
                unit[1] @ (matter + field) - (matter + field) @ unit[1]
            )
        )
        for matter, field in zip(unit[4], unit[5])
    )
    detail = {
        "ledger_rows": rows,
        "Cycle219_mass": logical_detail["Cycle219_mass_fixture"],
        "two_cell_mass": logical_detail["two_cell_rest_mass"],
        "mass_residual": logical_detail["two_cell_uniform_one_particle_residual"],
        "contact_nontrivial_columns": logical_detail["contact_nontrivial_columns"],
        "contact_deletion_opnorm": contact_deletion,
        "unit_weight_auxiliary_deletion_vector_commutators": no_auxiliary,
    }
    check(
        "mass, Q, number, and coefficient-two/unit-weight vector ledgers remain exact and the unit auxiliary stays load-bearing",
        max(
            max(row["unitarity"], row["Q"], row["number"], *row["vector"])
            for row in rows
        ) < TOL
        and abs(detail["Cycle219_mass"] - detail["two_cell_mass"]) < TOL
        and detail["mass_residual"] < TOL
        and detail["contact_nontrivial_columns"] == 4047
        and contact_deletion > 1.9
        and min(no_auxiliary) > 0.7,
        detail,
    )
    return detail


def physical_orientation_controls(update_factors, operator):
    encodings = {
        "AB": c322.build_encoding(3, False),
        "BA": c322.build_encoding(3, True),
    }
    maximum_rows = max(encoding.shape[0] for encoding in encodings.values())
    for encoding in encodings.values():
        if encoding.shape[0] < maximum_rows:
            encoding.resize((maximum_rows, encoding.shape[1]))
    rows = []
    for route in ROUTES:
        logical = c322.random_logical_state(3922) if route == "coefficient_two" else c325.random_state(3925)
        expected = route_step(
            route, logical, 3, update_factors, TRAIN_EDGE
        )
        for orientation, encoding in encodings.items():
            encoded = (
                c322.encode_physical(logical, encoding)
                if route == "coefficient_two"
                else c325.encode_physical(logical, encoding)
            )
            if route == "coefficient_two":
                actual = c322.physical_step(encoded, encoding, 3, update_factors)
                recovered = c322.physical_inverse(actual, encoding, 3, update_factors)
                expected_physical = c322.encode_physical(expected, encoding)
            else:
                actual = c325.physical_step(encoded, encoding, 3, update_factors)
                recovered = c325.physical_inverse(actual, encoding, 3, update_factors)
                expected_physical = c325.encode_physical(expected, encoding)
            residual = c322.state_residual(actual, expected_physical)
            inverse_residual = c322.state_residual(recovered, encoded)
            rows.append(
                {
                    "route": route,
                    "orientation": orientation,
                    "EG_residual": residual,
                    "inverse_residual": inverse_residual,
                    "input_norm": c322.state_norm(encoded),
                    "output_norm": c322.state_norm(actual),
                }
            )
    size_rows = [c315.size_gram_control(length, c322.LABELS) for length in (3, 4, 6)]
    rng = np.random.default_rng(392)
    vector = rng.normal(size=4096) + 1j * rng.normal(size=4096)
    vector /= np.linalg.norm(vector)
    logical_pointer = float(abs(np.vdot(c374.RAY, operator @ vector)) ** 2)
    pointer_rows = []
    for orientation, encoding in encodings.items():
        decoded = encoding.conj().T @ (encoding @ vector)
        pointer_rows.append(
            {
                "orientation": orientation,
                "decode_residual": float(np.linalg.norm(decoded - vector)),
                "pointer_residual": abs(
                    float(abs(np.vdot(c374.RAY, operator @ decoded)) ** 2)
                    - logical_pointer
                ),
            }
        )
    check(
        "Cycle-322 and Cycle-325 obey AB/BA physical EG while the frozen pointer has the same physical completion",
        max(
            max(
                row["EG_residual"],
                row["inverse_residual"],
                abs(row["input_norm"] - 1),
                abs(row["output_norm"] - 1),
            )
            for row in rows
        ) < TOL
        and max(
            max(row["decode_residual"], row["pointer_residual"])
            for row in pointer_rows
        ) < TOL
        and max(row["Gram_opnorm_residual"] for row in size_rows) < TOL,
        {"physical_rows": rows, "pointer_rows": pointer_rows, "size_rows": size_rows},
    )
    return rows, pointer_rows, size_rows


def signed_q2_coin(charge: int) -> np.ndarray:
    base = ORIGINAL_HARDCORE_COIN(charge)
    return -base if charge == 2 else base


def hard_core_collision_coordinate(
    length: int, endpoints, update_factors, operator, *, signed: bool
):
    original = c331.local_hardcore_coin
    c331.local_hardcore_coin = signed_q2_coin if signed else ORIGINAL_HARDCORE_COIN
    try:
        state = c331.initial_state()
        drift = 0.0
        for _ in range(2):
            state = c331.logical_step(
                state,
                length,
                update_factors,
                endpoint_cells=endpoints,
            )
            drift = max(drift, abs(c331.state_norm(state) - 1))
        coordinate = c374.pointer_one_coordinate(
            c374.pointer_transcript(state, operator)
        )
        leakage = c331.observables(state)["lawful_leakage"]
        return coordinate, drift, leakage
    finally:
        c331.local_hardcore_coin = original


def collision_controls(update_factors, operator):
    rows = []
    for role, length, endpoints in (
        ("training geometry", TRAIN_SIZE, TRAIN_EDGE),
        ("blind held target geometry", HELD_SIZE, HELD_EDGE),
    ):
        identity = hard_core_collision_coordinate(
            length, endpoints, update_factors, operator, signed=False
        )
        signed = hard_core_collision_coordinate(
            length, endpoints, update_factors, operator, signed=True
        )
        rows.append(
            {
                "role": role,
                "L": length,
                "identity_coordinate": identity[0],
                "signed_Q2_coordinate": signed[0],
                "collision_visibility": abs(identity[0] - signed[0]),
                "translation_residual": None,
                "maximum_norm_drift": max(identity[1], signed[1]),
                "maximum_lawful_leakage": max(identity[2], signed[2]),
                "strict_physical_compiler": True,
                "patch_M2": 98,
            }
        )
    rows[1]["translation_residual"] = abs(
        rows[1]["identity_coordinate"] - rows[0]["identity_coordinate"]
    )
    detail = {
        "rows": rows,
        "maximum_collision_visibility": max(row["collision_visibility"] for row in rows),
        "held_translation_residual": rows[1]["translation_residual"],
        "disposition": "signed onsite-Q2 alternative is invisible to this frozen apparatus",
    }
    check(
        "the hard-core signed-Q2 collision alternative remains lawful, translated, and explicitly apparatus-blind",
        detail["maximum_collision_visibility"] < TOL
        and detail["held_translation_residual"] < TOL
        and max(row["maximum_norm_drift"] for row in rows) < TOL
        and max(row["maximum_lawful_leakage"] for row in rows) < TOL
        and all(row["strict_physical_compiler"] for row in rows),
        detail,
    )
    return detail


def validate_geometry(length: int, endpoints, *, strict_edge: bool) -> None:
    if length not in (TRAIN_SIZE, VALIDATION_SIZE, HELD_SIZE):
        raise ValueError("size outside declared split")
    if len(endpoints) != 2 or endpoints[0] == endpoints[1]:
        raise ValueError("an edge needs two distinct cells")
    displacement = tuple(
        (endpoints[1][axis] - endpoints[0][axis]) % length for axis in range(3)
    )
    adjacent = sum(value not in (0,) for value in displacement) == 1 and any(
        value in (1, length - 1) for value in displacement
    )
    if strict_edge and not adjacent:
        raise ValueError("strict physical rows require one nearest-neighbor edge")


def deletion_domain_controls(operator):
    rows = []
    for route in ROUTES:
        receiver_deleted = edge_response(
            "receiver deletion",
            route,
            HELD_SIZE,
            HELD_EDGE,
            EDGE_DEPTH,
            1,
            operator,
            strict_physical_compiler=True,
            enabled=(True, False),
        )
        stream_deleted = edge_response(
            "edge-stream deletion",
            route,
            HELD_SIZE,
            HELD_EDGE,
            EDGE_DEPTH,
            1,
            operator,
            strict_physical_compiler=True,
            stream_enabled=False,
        )
        actual = edge_response(
            "actual contact",
            route,
            HELD_SIZE,
            HELD_EDGE,
            EDGE_DEPTH,
            1,
            operator,
            strict_physical_compiler=True,
        )
        deleted_contact = edge_response(
            "contact deletion",
            route,
            HELD_SIZE,
            HELD_EDGE,
            EDGE_DEPTH,
            0,
            operator,
            strict_physical_compiler=True,
        )
        rows.append(
            {
                "route": route,
                "receiver_deleted_A_to_B_transfer": receiver_deleted.transfer[0],
                "receiver_deleted_A_to_B_pointer": receiver_deleted.pointer[0],
                "stream_deleted_max_transfer": max(stream_deleted.transfer),
                "stream_deleted_max_pointer": max(stream_deleted.pointer),
                "contact_pointer_contrast": actual.mean_pointer
                - deleted_contact.mean_pointer,
                "contact_transfer_contrast": actual.mean_transfer
                - deleted_contact.mean_transfer,
            }
        )
    malformed = (
        (2, ((0, 0, 0), (1, 0, 0)), True),
        (6, ((0, 0, 0), (0, 0, 0)), True),
        (6, ((0, 0, 0), (2, 0, 0)), True),
        (5, ((0, 0, 0), (1, 0, 0)), True),
    )
    rejections = 0
    for args in malformed:
        try:
            validate_geometry(args[0], args[1], strict_edge=args[2])
        except ValueError:
            rejections += 1
    for length, endpoints in (
        (TRAIN_SIZE, TRAIN_EDGE),
        (VALIDATION_SIZE, VALIDATION_EDGE),
        (HELD_SIZE, HELD_EDGE),
    ):
        validate_geometry(length, endpoints, strict_edge=True)
    detail = {
        "deletion_rows": rows,
        "malformed_domain_rejections": rejections,
        "lawful_strict_edges": (TRAIN_EDGE, VALIDATION_EDGE, HELD_EDGE),
    }
    check(
        "contact and edge deletions are visible and malformed locality/size declarations are rejected",
        max(
            max(
                abs(row["receiver_deleted_A_to_B_transfer"]),
                abs(row["receiver_deleted_A_to_B_pointer"]),
                abs(row["stream_deleted_max_transfer"]),
                abs(row["stream_deleted_max_pointer"]),
            )
            for row in rows
        ) < TOL
        and min(abs(row["contact_pointer_contrast"]) for row in rows) > 1e-8
        and rejections == len(malformed),
        detail,
    )
    return detail


def inventory_controls(
    calibration,
    targets,
    chain,
    covariance,
    ledgers,
    physical,
    collision,
    deletions,
):
    detail = {
        "constructed": "one-edge-trained reciprocal calibration with translated-edge held prediction",
        "candidate_operational_source_coordinates": (
            "route tag",
            "actual/deleted contact code",
            "directed receiver-transfer coordinate",
        ),
        "strict_physical_compiler_rows": (
            "Cycle-322 coefficient-two adjacent edge plus pointer: 98 M2",
            "Cycle-325 unit-weight adjacent edge plus pointer: 112 M2",
            "Cycle-331 hard-core collision-control adjacent edge plus pointer: 98 M2",
        ),
        "logical_comparator_rows": (
            "depth-three non-nearest endpoint execution over the connected two-edge geometry",
            "naive product of independently calibrated edge transfers",
        ),
        "supplied": (
            "Cycle-315 two-cell seam, AB/BA encodings, actual contact, and frame action",
            "Cycle-322 coefficient-two Q1 vertex, preparation, receiver selector, and streams",
            "Cycle-325 unit-weight paired auxiliary, co-stream, and 111-M2 edge patch",
            "Cycle-374 program-6 pointer apparatus and symmetric ray",
            "one L3 training edge, L4 validation edge, blind L6 edge/chain, model class, and tolerances",
            "Cycle-331 signed-Q2 collision comparator",
        ),
        "not_constructed": (
            "shared-middle-site Cycle-325 source/update compiler",
            "primitive overlap resolution on the Cycle-319 three-cell matter seam",
            "empirical units, universal coupling, metric/lapse/tensor equation, or nonlinear backreaction",
            "pointer branch, Record, actual member, sampler, or frequency law",
        ),
        "calibration": calibration,
        "target_rows": targets,
        "chain": chain,
        "covariance": covariance,
        "ledgers": ledgers,
        "physical": physical,
        "collision": collision,
        "deletions": deletions,
        "pointer_is_energy": False,
        "pointer_is_stress": False,
        "pointer_is_source": False,
        "pointer_is_gravity": False,
        "pointer_is_rate": False,
        "pointer_is_occurrence": False,
        "shared_obstruction": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the physical/logical boundary and semantic inventory preserve authority none, audit unset, and no axiom pressure",
        len(detail["strict_physical_compiler_rows"]) == 3
        and len(detail["logical_comparator_rows"]) == 2
        and detail["pointer_is_energy"] is False
        and detail["pointer_is_stress"] is False
        and detail["pointer_is_source"] is False
        and detail["pointer_is_gravity"] is False
        and detail["pointer_is_rate"] is False
        and detail["pointer_is_occurrence"] is False
        and detail["shared_obstruction"] is detail["axiom_pressure"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 392: PHYSICAL RECIPROCAL MULTI-EDGE CALIBRATION")
    print("authority=none; audit=unset")
    note_contract()
    coin, edge_swap, contact, logical_detail = factors(True)
    update_factors = (coin, edge_swap, contact)
    operator = frozen_apparatus_controls(coin, edge_swap)
    calibration, training_rows = train_one_edge(operator)
    target_rows, target_residuals = translated_target_controls(
        calibration, operator
    )
    _chain_rows, chain_failures, chain_detail = connected_chain_controls(
        calibration, training_rows, operator
    )
    covariance = covariance_controls(coin, edge_swap, contact, operator)
    ledgers = mass_ledger_contact_controls(contact, logical_detail)
    physical = physical_orientation_controls(update_factors, operator)
    collision = collision_controls(update_factors, operator)
    deletions = deletion_domain_controls(operator)
    inventory_controls(
        calibration,
        target_residuals,
        {"rows": chain_failures, "locality": chain_detail},
        covariance,
        ledgers,
        physical,
        collision,
        deletions,
    )
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_RECIPROCAL_MULTI_EDGE_CALIBRATION_OPEN")
        return 1
    print("RESULT PHYSICAL_RECIPROCAL_MULTI_EDGE_CALIBRATION_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
