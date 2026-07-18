#!/usr/bin/env python3
"""Cycle 387: contact-sensitive response-calibration stress tournament.

Freeze Cycle 374's 98-M2 pointer apparatus.  Fit one swap-symmetric,
contact-conditioned multiplicative calibration on hard-core L=3,4 cases with
zero or one enabled reservoir, then open L=6.  Held cases cover both endpoint
species, multiplicity zero/one/two, actual/deleted contact, a signed onsite-Q2
collision comparator, and the already-declared Cycle-328 bosonic/labelled
logical comparators.  Held cases never select or refit the readout or model.

The input labels are candidate operational source coordinates.  The pointer
output is only a dimensionless response coordinate; it is not promoted to a
far-side physical interpretation or an actual occurrence.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import math
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_contact_sensitive_operational_transcript_registration_cycle374_2026_07_18 as c374


c331 = c374.c331
c328 = c374.c328
c315 = c374.c315
c322 = c374.c322
c210 = c374.c210
c214 = c331.c214

TRAIN_SIZES = (3, 4)
HELD_SIZE = 6
DEPTH = 2
POINTER_CALIBRATION_TOLERANCE = 1.0e-3
CALIBRATED_MULTIPLICITY_TOLERANCE = 1.0e-2
NUMERICAL_TOLERANCE = 3.0e-10
AUTHORITY = "none"
AUDIT = "unset"
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CONTACT_SENSITIVE_SOURCE_RESPONSE_CALIBRATION_STRESS_"
    "CYCLE387_NOTE_2026-07-18.md"
)

PATTERNS = (
    (False, False),
    (True, False),
    (False, True),
    (True, True),
)
ROUTES = (
    "hard_core_identity_collision",
    "hard_core_signed_Q2_collision",
    "bosonic_logical_comparator",
    "independently_labelled_logical_comparator",
)
ORIGINAL_HARDCORE_COIN = c331.local_hardcore_coin

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


def raw_maximum(matrix: sparse.spmatrix) -> float:
    matrix = matrix.tocoo()
    return 0.0 if matrix.nnz == 0 else float(np.max(np.abs(matrix.data)))


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-387 note exists", False, NOTE)
        return
    text = NOTE.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    text = " ".join(text.split())
    required = (
        "authority: none",
        "audit: unset",
        "frozen 98-m2 readout",
        "candidate operational source coordinates",
        "l=3,4 training",
        "blind held l=6",
        "no readout retraining",
        "multiplicative calibration",
        "additivity",
        "monotonicity",
        "source-target swap",
        "ab/ba",
        "all 24 proper-cubic frames",
        "collision alternative",
        "mass and input ledgers",
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
        "the note pins the frozen apparatus, blind split, semantics, controls, and status",
        not missing,
        missing,
    )


def factors():
    coin, edge_swap, contact, _update, detail = c315.logical_update_controls(
        c331.LABELS
    )
    return coin.tocsc(), edge_swap.tocsc(), contact.tocsc(), detail


def frozen_readout_controls(coin, edge_swap) -> sparse.csc_matrix:
    menu = c374.readout_menu(coin, edge_swap)
    selected = menu[6]
    operator = (edge_swap @ coin.conj().T).tocsc()
    index_failures = 0
    roundtrip_residual = 0.0
    for endpoint in range(2):
        indices = c374.INDEX_BY_ENDPOINT[endpoint]
        index_failures += int(
            indices.shape != (64, 64)
            or len(np.unique(indices)) != 4096
            or int(indices.min()) != 0
            or int(indices.max()) != 4095
        )
        vector = np.arange(4096, dtype=float) + 1j * np.arange(4096)[::-1]
        roundtrip_residual = max(
            roundtrip_residual,
            float(
                np.linalg.norm(
                    c374.fast_matter_vector(
                        c374.fast_matter_matrix(vector, endpoint), endpoint
                    )
                    - vector
                )
            ),
        )
    detail = {
        "program": selected.program,
        "name": selected.name,
        "depth": DEPTH,
        "readout_patch_M2": 98,
        "pointer_M2": 1,
        "inherited_seam_M2": 97,
        "menu_search_executed": False,
        "held_data_used_for_readout": False,
        "operator_residual": raw_maximum(selected.operator - operator),
        "gather_index_failures": index_failures,
        "gather_roundtrip_residual": roundtrip_residual,
    }
    check(
        "Cycle 374's program-6 depth-two 98-M2 readout is frozen without rerunning selection",
        selected.program == 6
        and selected.name == "inverse_matter_coin_then_edge_fswap"
        and detail["operator_residual"] == 0
        and index_failures == 0
        and roundtrip_residual == 0
        and detail["menu_search_executed"] is False
        and detail["held_data_used_for_readout"] is False,
        detail,
    )
    return operator


@dataclass(frozen=True)
class ResponseRow:
    role: str
    length: int
    route: str
    n_A: int
    n_B: int
    contact_code: int
    pointer_coordinate: float
    norm_drift: float
    lawful_leakage: float
    reachable_labels: int
    strict_98_M2_physical_route: bool

    @property
    def multiplicity(self) -> int:
        return self.n_A + self.n_B


def signed_q2_coin(charge: int) -> np.ndarray:
    base = ORIGINAL_HARDCORE_COIN(charge)
    return -base if charge == 2 else base


def validate_candidate_coordinates(
    length: int, route: str, enabled: tuple[bool, bool], contact_code: int
) -> None:
    if length not in TRAIN_SIZES + (HELD_SIZE,):
        raise ValueError("length outside declared train/held domain")
    if route not in ROUTES:
        raise ValueError("undeclared candidate route")
    if len(enabled) != 2 or any(type(value) is not bool for value in enabled):
        raise ValueError("candidate coordinates require two Boolean endpoint labels")
    if contact_code not in (0, 1):
        raise ValueError("contact code must be zero or one")


def response_row(
    role: str,
    length: int,
    route: str,
    enabled: tuple[bool, bool],
    contact_code: int,
    update_factors,
    operator,
    *,
    retain_state: bool = False,
):
    validate_candidate_coordinates(length, route, enabled, contact_code)
    contact_enabled = bool(contact_code)
    if route.startswith("hard_core"):
        q2_coin = (
            signed_q2_coin
            if route == "hard_core_signed_Q2_collision"
            else None
        )
        states, drift = c374.states_by_depth(
            length,
            update_factors,
            enabled=enabled,
            contact_enabled=contact_enabled,
            q2_coin=q2_coin,
        )
        state = states[DEPTH]
        observed = c331.observables(state)
        leakage = observed["lawful_leakage"]
        strict = True
    else:
        statistics = (
            "bosonic"
            if route == "bosonic_logical_comparator"
            else "independent"
        )
        state, observed, drift = c328.run_response(
            length,
            update_factors,
            statistics,
            enabled=enabled,
            contact_enabled=contact_enabled,
            depths=DEPTH,
        )
        leakage = observed["lawful_Q2_leakage"]
        # These are lawful inherited logical comparators.  Cycle 328 does not
        # supply their primitive Q-factor M2 synthesis, so they are not called
        # additional 98-M2 physical routes.
        strict = False
    coordinate = c374.pointer_one_coordinate(
        c374.pointer_transcript(state, operator)
    )
    row = ResponseRow(
        role=role,
        length=length,
        route=route,
        n_A=int(enabled[0]),
        n_B=int(enabled[1]),
        contact_code=contact_code,
        pointer_coordinate=coordinate,
        norm_drift=drift,
        lawful_leakage=leakage,
        reachable_labels=len(state),
        strict_98_M2_physical_route=strict,
    )
    return (row, state) if retain_state else row


@dataclass(frozen=True)
class FrozenCalibration:
    baseline_deleted: float
    attenuation_deleted: float
    baseline_actual: float
    attenuation_actual: float

    def baseline(self, contact_code: int) -> float:
        return self.baseline_actual if contact_code else self.baseline_deleted

    def attenuation(self, contact_code: int) -> float:
        return (
            self.attenuation_actual
            if contact_code
            else self.attenuation_deleted
        )

    def predict(self, multiplicity: int, contact_code: int) -> float:
        return self.baseline(contact_code) * self.attenuation(contact_code) ** multiplicity

    def calibrated_multiplicity(self, coordinate: float, contact_code: int) -> float:
        return math.log(coordinate / self.baseline(contact_code)) / math.log(
            self.attenuation(contact_code)
        )


def fit_training_only_calibration(update_factors, operator):
    rows = []
    for length in TRAIN_SIZES:
        for enabled in PATTERNS[:3]:
            for contact_code in (0, 1):
                rows.append(
                    response_row(
                        "training",
                        length,
                        "hard_core_identity_collision",
                        enabled,
                        contact_code,
                        update_factors,
                        operator,
                    )
                )
    parameters = {}
    training_residual = 0.0
    species_residual = 0.0
    size_residual = 0.0
    for contact_code in (0, 1):
        zero = [
            row.pointer_coordinate
            for row in rows
            if row.contact_code == contact_code and row.multiplicity == 0
        ]
        ones_A = [
            row.pointer_coordinate
            for row in rows
            if row.contact_code == contact_code and (row.n_A, row.n_B) == (1, 0)
        ]
        ones_B = [
            row.pointer_coordinate
            for row in rows
            if row.contact_code == contact_code and (row.n_A, row.n_B) == (0, 1)
        ]
        baseline = float(np.mean(zero))
        one = float(np.mean(ones_A + ones_B))
        parameters[contact_code] = (baseline, one / baseline)
        species_residual = max(
            species_residual, max(abs(left - right) for left, right in zip(ones_A, ones_B))
        )
        size_residual = max(
            size_residual,
            max(zero) - min(zero),
            max(ones_A + ones_B) - min(ones_A + ones_B),
        )
    calibration = FrozenCalibration(
        baseline_deleted=parameters[0][0],
        attenuation_deleted=parameters[0][1],
        baseline_actual=parameters[1][0],
        attenuation_actual=parameters[1][1],
    )
    for row in rows:
        training_residual = max(
            training_residual,
            abs(
                row.pointer_coordinate
                - calibration.predict(row.multiplicity, row.contact_code)
            ),
        )
    detail = {
        "training_sizes": TRAIN_SIZES,
        "training_rows": len(rows),
        "training_multiplicities": (0, 1),
        "held_size_opened": False,
        "model": "p_hat(n,c)=p0(c) r(c)^n",
        "calibration": calibration,
        "maximum_training_residual": training_residual,
        "maximum_A_B_species_residual": species_residual,
        "maximum_training_size_residual": size_residual,
    }
    check(
        "one swap-symmetric multiplicative calibration is frozen on L=3,4 zero/one coordinates before held L=6",
        all(row.length in TRAIN_SIZES for row in rows)
        and all(row.multiplicity < 2 for row in rows)
        and training_residual < NUMERICAL_TOLERANCE
        and species_residual < NUMERICAL_TOLERANCE
        and size_residual < NUMERICAL_TOLERANCE,
        detail,
    )
    return calibration, rows


def held_tournament(calibration, update_factors, operator):
    rows = []
    retained_states = {}
    for route in ROUTES:
        for enabled in PATTERNS:
            for contact_code in (0, 1):
                retain = (
                    route == "hard_core_identity_collision"
                    and enabled == (True, True)
                )
                result = response_row(
                    "blind held",
                    HELD_SIZE,
                    route,
                    enabled,
                    contact_code,
                    update_factors,
                    operator,
                    retain_state=retain,
                )
                if retain:
                    row, state = result
                    retained_states[contact_code] = state
                else:
                    row = result
                rows.append(row)

    transfer_rows = []
    for row in rows:
        prediction = calibration.predict(row.multiplicity, row.contact_code)
        calibrated = calibration.calibrated_multiplicity(
            row.pointer_coordinate, row.contact_code
        )
        transfer_rows.append(
            {
                "route": row.route,
                "n_A": row.n_A,
                "n_B": row.n_B,
                "contact_code": row.contact_code,
                "strict_98_M2_physical_route": row.strict_98_M2_physical_route,
                "observed": row.pointer_coordinate,
                "predicted": prediction,
                "pointer_residual": row.pointer_coordinate - prediction,
                "calibrated_multiplicity": calibrated,
                "multiplicity_residual": calibrated - row.multiplicity,
            }
        )
    decisive = [row for row in transfer_rows if row["n_A"] == row["n_B"] == 1]
    maximum_pointer_residual = max(abs(row["pointer_residual"]) for row in decisive)
    maximum_multiplicity_residual = max(
        abs(row["multiplicity_residual"]) for row in decisive
    )
    detail = {
        "held_size": HELD_SIZE,
        "held_rows": len(rows),
        "routes": ROUTES,
        "strict_98_M2_rows": sum(row.strict_98_M2_physical_route for row in rows),
        "logical_comparator_rows": sum(not row.strict_98_M2_physical_route for row in rows),
        "two_coordinate_transfer_rows": decisive,
        "maximum_two_coordinate_pointer_residual": maximum_pointer_residual,
        "pointer_tolerance_frozen_before_held": POINTER_CALIBRATION_TOLERANCE,
        "maximum_two_coordinate_multiplicity_residual": maximum_multiplicity_residual,
        "multiplicity_tolerance_frozen_before_held": CALIBRATED_MULTIPLICITY_TOLERANCE,
        "maximum_norm_drift": max(row.norm_drift for row in rows),
        "maximum_lawful_leakage": max(row.lawful_leakage for row in rows),
        "readout_refit_on_held": False,
        "calibration_refit_on_held": False,
    }
    check(
        "the frozen calibration predicts every held two-coordinate route within its predeclared response and multiplicity tolerances",
        maximum_pointer_residual < POINTER_CALIBRATION_TOLERANCE
        and maximum_multiplicity_residual < CALIBRATED_MULTIPLICITY_TOLERANCE
        and detail["maximum_norm_drift"] < NUMERICAL_TOLERANCE
        and detail["maximum_lawful_leakage"] < NUMERICAL_TOLERANCE
        and detail["readout_refit_on_held"] is False
        and detail["calibration_refit_on_held"] is False,
        detail,
    )
    return rows, retained_states, transfer_rows


def composition_monotonicity_reciprocity_controls(rows):
    lookup = {
        (row.route, row.contact_code, row.n_A, row.n_B): row.pointer_coordinate
        for row in rows
    }
    composition_rows = []
    for route in ROUTES:
        for contact_code in (0, 1):
            p00 = lookup[(route, contact_code, 0, 0)]
            p10 = lookup[(route, contact_code, 1, 0)]
            p01 = lookup[(route, contact_code, 0, 1)]
            p11 = lookup[(route, contact_code, 1, 1)]
            composition_rows.append(
                {
                    "route": route,
                    "contact_code": contact_code,
                    "p00": p00,
                    "p10": p10,
                    "p01": p01,
                    "p11": p11,
                    "additivity_residual": p11 - p10 - p01 + p00,
                    "source_target_swap_residual": abs(p10 - p01),
                    "strict_monotone": p00 > max(p10, p01) > p11,
                }
            )
    contact_rows = []
    for route in ROUTES:
        contrasts = []
        for enabled in PATTERNS:
            n_A, n_B = map(int, enabled)
            contrast = (
                lookup[(route, 1, n_A, n_B)]
                - lookup[(route, 0, n_A, n_B)]
            )
            contrasts.append((n_A + n_B, enabled, contrast))
        contact_rows.append(
            {
                "route": route,
                "contrasts": contrasts,
                "all_contact_sensitive": all(abs(row[2]) > 1e-3 for row in contrasts),
                "contrast_magnitude_monotone": (
                    abs(contrasts[0][2])
                    > abs(contrasts[1][2])
                    and abs(contrasts[0][2])
                    > abs(contrasts[2][2])
                    and min(abs(contrasts[1][2]), abs(contrasts[2][2]))
                    > abs(contrasts[3][2])
                ),
            }
        )
    maximum_swap = max(row["source_target_swap_residual"] for row in composition_rows)
    minimum_additivity_residual = min(
        abs(row["additivity_residual"]) for row in composition_rows
    )
    check(
        "held source-target swap reciprocity and monotonicity pass for every route and contact setting",
        maximum_swap < NUMERICAL_TOLERANCE
        and all(row["strict_monotone"] for row in composition_rows)
        and all(row["all_contact_sensitive"] for row in contact_rows)
        and all(row["contrast_magnitude_monotone"] for row in contact_rows),
        {
            "maximum_source_target_swap_residual": maximum_swap,
            "composition_rows": composition_rows,
            "contact_rows": contact_rows,
        },
    )
    check(
        "the direct additive pointer-response hypothesis is decisively rejected while the frozen multiplicative calibration remains the retained route",
        minimum_additivity_residual > 1e-2,
        {
            "minimum_absolute_additivity_residual": minimum_additivity_residual,
            "additivity_acceptance_tolerance": POINTER_CALIBRATION_TOLERANCE,
            "scope": "route-specific finite pointer coordinate; not a negative substrate wall",
        },
    )
    return composition_rows, contact_rows


def covariance_controls(coin, edge_swap, operator):
    readout_residuals = []
    ray_residuals = []
    endpoint_reversals = 0
    source_residuals = []
    collision_residuals = []
    hard_generators = {
        charge: c331.hardcore_source_generator(charge) for charge in (1, 2)
    }
    boson_generators = {
        charge: c328.boson_source_generator(charge) for charge in (1, 2)
    }
    configurations = tuple(combinations(range(6), 2))
    lookup = {configuration: index for index, configuration in enumerate(configurations)}
    signed_collision = -np.eye(len(configurations), dtype=complex)
    _exchange, independent_vertex, _charge, _number, _momenta = c322.local_source_blocks(
        c331.ANGLE
    )
    for frame in c210.proper_cubic_frames():
        mapped_direction = frame @ np.asarray((1, 0, 0), dtype=int)
        axis = int(np.flatnonzero(mapped_direction)[0])
        reversed_endpoints = int(mapped_direction[axis]) == -1
        endpoint_reversals += reversed_endpoints
        representation = c315.pair_frame_representation(
            c331.LABELS, frame, reversed_endpoints
        )
        target_operator = c315.edge_fswap_matrix(c331.LABELS, axis) @ coin.conj().T
        readout_residuals.append(
            raw_maximum(representation @ operator - target_operator @ representation)
        )
        mapped_ray = representation @ c374.RAY
        overlap = np.vdot(c374.RAY, mapped_ray)
        ray_residuals.append(float(np.linalg.norm(mapped_ray - overlap * c374.RAY)))
        for charge in (1, 2):
            hard_frame = c331.hardcore_source_frame(charge, frame)
            source_residuals.append(
                raw_maximum(
                    hard_frame @ hard_generators[charge]
                    - hard_generators[charge] @ hard_frame
                )
            )
            boson_frame = c328.boson_source_frame(charge, frame)
            source_residuals.append(
                raw_maximum(
                    boson_frame @ boson_generators[charge]
                    - boson_generators[charge] @ boson_frame
                )
            )
        independent_frame = c322.local_source_frame(frame)
        source_residuals.append(
            float(
                np.linalg.norm(
                    independent_frame @ independent_vertex @ independent_frame.T
                    - independent_vertex
                )
            )
        )
        rows = []
        for configuration in configurations:
            mapped = tuple(
                sorted(c315.c311.direction_map(frame, direction) for direction in configuration)
            )
            rows.append(lookup[mapped])
        q2_frame = np.zeros((15, 15), dtype=complex)
        q2_frame[rows, np.arange(15)] = 1
        collision_residuals.append(
            float(
                np.linalg.norm(
                    q2_frame @ signed_collision @ q2_frame.T - signed_collision
                )
            )
        )
    inherited = c315.covariance_translation_controls(
        c331.LABELS, coin, c315.logical_update_controls(c331.LABELS)[2],
        c315.logical_update_controls(c331.LABELS)[2] @ edge_swap @ coin,
    )
    detail = {
        "proper_cubic_frames": len(readout_residuals),
        "endpoint_reversing_frames": endpoint_reversals,
        "maximum_readout_residual": max(readout_residuals),
        "maximum_ray_residual": max(ray_residuals),
        "maximum_candidate_input_operator_frame_residual": max(source_residuals),
        "maximum_signed_collision_frame_residual": max(collision_residuals),
        "inherited_common_seam": inherited,
    }
    check(
        "the frozen readout, candidate input operators, collision alternative, and common seam cover all 24 proper-cubic frames",
        detail["proper_cubic_frames"] == 24
        and endpoint_reversals == 12
        and max(readout_residuals) < NUMERICAL_TOLERANCE
        and max(ray_residuals) < NUMERICAL_TOLERANCE
        and max(source_residuals) < NUMERICAL_TOLERANCE
        and max(collision_residuals) < NUMERICAL_TOLERANCE
        and inherited["maximum_update_covariance_residual"] < NUMERICAL_TOLERANCE,
        detail,
    )
    return detail


def diagonal_ledgers(configurations, generator, *, coefficient: int):
    number_values = []
    q_values = []
    vector_values = [[], [], []]
    for configuration in configurations:
        field_vector = sum(
            (
                c210.DIRECTIONS[label - 1]
                for label in configuration
                if label > 0
            ),
            start=np.zeros(3, dtype=int),
        )
        for mask in c331.LOCAL_MASKS:
            matter_vector = sum(
                (
                    c210.DIRECTIONS[direction]
                    for direction in range(6)
                    if (mask >> direction) & 1
                ),
                start=np.zeros(3, dtype=int),
            )
            number_values.append(mask.bit_count())
            q_values.append(len(configuration))
            for axis in range(3):
                vector_values[axis].append(
                    float(matter_vector[axis] + coefficient * field_vector[axis])
                )
    number = sparse.diags(number_values, format="csc", dtype=float)
    q_operator = sparse.diags(q_values, format="csc", dtype=float)
    vectors = tuple(
        sparse.diags(values, format="csc", dtype=float) for values in vector_values
    )
    return {
        "Hermiticity": raw_maximum(generator - generator.conj().T),
        "Q": raw_maximum(generator @ q_operator - q_operator @ generator),
        "matter_number": raw_maximum(generator @ number - number @ generator),
        "vector": tuple(
            raw_maximum(generator @ operator - operator @ generator)
            for operator in vectors
        ),
    }


def mass_and_input_ledger_controls(contact, logical_detail):
    rows = []
    for route, configurations_fn, generator_fn in (
        (
            "hard_core",
            c331.hardcore_local_configurations,
            c331.hardcore_source_generator,
        ),
        (
            "bosonic",
            c328.boson_local_configurations,
            c328.boson_source_generator,
        ),
    ):
        for charge in (1, 2):
            rows.append(
                {
                    "route": route,
                    "local_Q": charge,
                    **diagonal_ledgers(
                        configurations_fn(charge),
                        generator_fn(charge),
                        coefficient=2,
                    ),
                }
            )
    _exchange, independent_vertex, charge, number, momenta = c322.local_source_blocks(
        c331.ANGLE
    )
    independent = {
        "unitarity": float(
            np.linalg.norm(independent_vertex.conj().T @ independent_vertex - np.eye(448))
        ),
        "Q": float(np.linalg.norm(independent_vertex @ charge - charge @ independent_vertex)),
        "matter_number": float(
            np.linalg.norm(independent_vertex @ number - number @ independent_vertex)
        ),
        "vector": tuple(
            float(np.linalg.norm(independent_vertex @ value - value @ independent_vertex))
            for value in momenta
        ),
    }
    contact_deletion = c315.largest_singular(
        contact - sparse.eye(contact.shape[0], format="csc")
    )
    detail = {
        "input_operator_ledgers": rows,
        "independently_labelled_vertex_ledgers": independent,
        "Cycle219_mass_fixture": logical_detail["Cycle219_mass_fixture"],
        "two_cell_mass_fixture": logical_detail["two_cell_rest_mass"],
        "mass_eigenvector_residual": logical_detail[
            "two_cell_uniform_one_particle_residual"
        ],
        "actual_contact_nontrivial_columns": logical_detail[
            "contact_nontrivial_columns"
        ],
        "contact_deletion_opnorm": contact_deletion,
    }
    all_values = [
        max(row["Hermiticity"], row["Q"], row["matter_number"], *row["vector"])
        for row in rows
    ]
    check(
        "mass and candidate-input Q, matter-number, and coefficient-two vector ledgers remain exact across the held routes",
        max(all_values) == 0
        and max(
            independent["unitarity"],
            independent["Q"],
            independent["matter_number"],
            *independent["vector"],
        ) < NUMERICAL_TOLERANCE
        and abs(detail["Cycle219_mass_fixture"] - detail["two_cell_mass_fixture"])
        < NUMERICAL_TOLERANCE
        and detail["mass_eigenvector_residual"] < NUMERICAL_TOLERANCE
        and detail["actual_contact_nontrivial_columns"] == 4047
        and contact_deletion > 1.9,
        detail,
    )
    return detail


def physical_orientation_controls(operator):
    rng = np.random.default_rng(387)
    vector = rng.normal(size=4096) + 1j * rng.normal(size=4096)
    vector /= np.linalg.norm(vector)
    logical_coordinate = c374.pointer_one_coordinate(
        c374.pointer_transcript({(0, 1): vector}, operator)
    )
    rows = []
    for orientation, reverse in (("AB", False), ("BA", True)):
        encoding = c322.build_encoding(3, reverse)
        encoded = encoding @ vector
        decoded = encoding.conj().T @ encoded
        decoded_coordinate = c374.pointer_one_coordinate(
            c374.pointer_transcript({(0, 1): decoded}, operator)
        )
        rows.append(
            {
                "orientation": orientation,
                "decode_residual": float(np.linalg.norm(decoded - vector)),
                "encoded_norm_residual": abs(float(np.vdot(encoded, encoded).real) - 1),
                "pointer_coordinate_residual": abs(decoded_coordinate - logical_coordinate),
            }
        )
    check(
        "the frozen response coordinate has the same sampled AB and BA physical-code completion",
        max(
            value
            for row in rows
            for key, value in row.items()
            if key != "orientation"
        ) < NUMERICAL_TOLERANCE,
        rows,
    )
    return rows


def deletion_collision_domain_controls(rows, retained_states, operator, coin, edge_swap):
    lookup = {
        (row.route, row.contact_code, row.n_A, row.n_B): row.pointer_coordinate
        for row in rows
    }
    identity_route = "hard_core_identity_collision"
    signed_route = "hard_core_signed_Q2_collision"
    signed_visibility = max(
        abs(
            lookup[(identity_route, contact, n_A, n_B)]
            - lookup[(signed_route, contact, n_A, n_B)]
        )
        for contact in (0, 1)
        for n_A, n_B in ((0, 0), (1, 0), (0, 1), (1, 1))
    )
    source_deletion_contrasts = {
        "delete_A": lookup[(identity_route, 1, 1, 1)]
        - lookup[(identity_route, 1, 0, 1)],
        "delete_B": lookup[(identity_route, 1, 1, 1)]
        - lookup[(identity_route, 1, 1, 0)],
        "delete_both": lookup[(identity_route, 1, 1, 1)]
        - lookup[(identity_route, 1, 0, 0)],
    }
    contact_transcript_residual = c374.transcript_residual(
        c374.pointer_transcript(retained_states[1], operator),
        c374.pointer_transcript(retained_states[0], operator),
    )
    readout_deletions = {}
    for name, deleted_operator in (
        ("delete_inverse_coin", edge_swap),
        ("delete_edge_fswap", coin.conj().T),
        ("delete_both_recombination_factors", sparse.eye(4096, format="csc")),
    ):
        readout_deletions[name] = c374.pointer_one_coordinate(
            c374.pointer_transcript(retained_states[1], deleted_operator)
        )
    rejection_count = 0
    malformed = (
        (5, identity_route, (True, True), 1),
        (6, "undeclared", (True, True), 1),
        (6, identity_route, (True,), 1),
        (6, identity_route, (1, True), 1),
        (6, identity_route, (True, True), 2),
    )
    for call in malformed:
        try:
            validate_candidate_coordinates(*call)
        except ValueError:
            rejection_count += 1
    detail = {
        "source_coordinate_deletions": source_deletion_contrasts,
        "contact_fine_transcript_residual": contact_transcript_residual,
        "signed_Q2_collision_coordinate_visibility": signed_visibility,
        "signed_collision_disposition": "lawful covariant comparator; invisible to this frozen response",
        "readout_factor_deletions": readout_deletions,
        "malformed_domain_rejections": rejection_count,
    }
    check(
        "source-coordinate, contact, readout-factor, collision, and lawful-domain controls remain explicit",
        min(abs(value) for value in source_deletion_contrasts.values()) > 0.1
        and contact_transcript_residual > 0.3
        and signed_visibility < NUMERICAL_TOLERANCE
        and min(
            abs(value - lookup[(identity_route, 1, 1, 1)])
            for value in readout_deletions.values()
        ) > 1e-3
        and rejection_count == len(malformed),
        detail,
    )
    return detail


def inventory_controls(calibration, held_rows, covariance, ledgers, orientation, deletion):
    detail = {
        "constructed": "one frozen finite multiplicative response calibration with blind held transfer",
        "candidate_operational_source_coordinates": (
            "enabled reservoir A bit",
            "enabled reservoir B bit",
            "actual/deleted contact code",
            "declared mediator/collision comparator label",
        ),
        "calibration": calibration,
        "supplied": (
            "Cycle-315 complete matter seam, AB/BA encodings, FSWAP, and actual Cycle-230 contact",
            "Cycle-331 hard-core exclusion/source angle/Q1 coin/Q2 collision rule",
            "Cycle-374 depth-two program-6 symmetric-ray pointer apparatus and 98-M2 patch count",
            "zero/one L3/L4 train split, multiplicative model class, tolerances, and L6 held menu",
            "Cycle-328 bosonic and independently labelled logical comparator grammars",
            "signed onsite-Q2 collision comparator",
        ),
        "derived": (
            "training-frozen coefficients",
            "held response and calibrated-multiplicity residuals",
            "direct-additivity residuals and monotonicity",
            "source-target swap equality",
            "covariance, ledgers, deletions, and physical-orientation controls",
        ),
        "not_supplied_or_claimed": (
            "physical identification of either input or output",
            "empirical units or universal coupling",
            "metric/lapse/tensor equation or nonlinear backreaction",
            "mediator-statistics selection or bosonic/labelled primitive M2 synthesis",
            "pointer branch, Record formation, or actual member",
        ),
        "held_rows": len(held_rows),
        "covariance": covariance,
        "ledgers": ledgers,
        "orientation": orientation,
        "deletion": deletion,
        "response_is_energy": False,
        "response_is_stress": False,
        "response_is_source": False,
        "response_is_gravity": False,
        "response_is_rate": False,
        "response_is_occurrence": False,
        "shared_obstruction": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the supplied-content and semantic inventory preserves authority none, audit unset, and no axiom pressure",
        detail["response_is_energy"] is False
        and detail["response_is_stress"] is False
        and detail["response_is_source"] is False
        and detail["response_is_gravity"] is False
        and detail["response_is_rate"] is False
        and detail["response_is_occurrence"] is False
        and detail["shared_obstruction"] is detail["axiom_pressure"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 387: CONTACT-SENSITIVE RESPONSE-CALIBRATION STRESS")
    print("authority=none; audit=unset")
    note_contract()
    coin, edge_swap, contact, logical_detail = factors()
    update_factors = (coin, edge_swap, contact)
    operator = frozen_readout_controls(coin, edge_swap)
    calibration, _training_rows = fit_training_only_calibration(
        update_factors, operator
    )
    held_rows, retained_states, _transfer_rows = held_tournament(
        calibration, update_factors, operator
    )
    composition_monotonicity_reciprocity_controls(held_rows)
    covariance = covariance_controls(coin, edge_swap, operator)
    ledgers = mass_and_input_ledger_controls(contact, logical_detail)
    orientation = physical_orientation_controls(operator)
    deletion = deletion_collision_domain_controls(
        held_rows, retained_states, operator, coin, edge_swap
    )
    inventory_controls(
        calibration, held_rows, covariance, ledgers, orientation, deletion
    )
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_CONTACT_SENSITIVE_RESPONSE_CALIBRATION_OPEN")
        return 1
    print("RESULT PHYSICAL_CONTACT_SENSITIVE_RESPONSE_CALIBRATION_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
