#!/usr/bin/env python3
"""Cycle 374: contact-sensitive operational-transcript registration.

The runner searches a finite depth/readout menu on L=3,4 only, freezes the
winner, and evaluates it on held L=6.  The retained apparatus applies a fixed
two-cell coherent recombination followed by a two-branch pointer isometry.
It registers only a grade-blind Cycle-351-compatible tag schema.  No pointer
branch is selected, no Record is formed, and Cycle-364 formation is not used.

All reported scalar coordinates are exact diagnostics of the finite pointer
instrument.  They are not promoted to a Born rule or to any far-side physical
interpretation.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from hashlib import sha256
from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import global_q2_simultaneous_two_source_cycle328_2026_07_18 as c328
import hardcore_global_q2_mediator_cycle331_2026_07_18 as c331


c315 = c331.c315
c322 = c331.c322
c210 = c331.c210
LABELS = c331.LABELS
TRAIN_SIZES = (3, 4)
HELD_SIZE = 6
DEPTHS = (1, 2)
TOL = 3.0e-10
AUTHORITY = "none"
AUDIT = "unset"
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CONTACT_SENSITIVE_OPERATIONAL_TRANSCRIPT_REGISTRATION_"
    "CYCLE374_NOTE_2026-07-18.md"
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


def raw_maximum(matrix: sparse.spmatrix) -> float:
    matrix = matrix.tocoo()
    return 0.0 if matrix.nnz == 0 else float(np.max(np.abs(matrix.data)))


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-374 note exists", False, NOTE)
        return
    text = NOTE.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    text = " ".join(text.split())
    required = (
        "authority: none",
        "audit: unset",
        "train-only selection",
        "held l=6",
        "inverse matter coin then mapped edge fswap",
        "actual cycle-230 contact",
        "all 24 proper-cubic frames",
        "cycle-351-compatible",
        "cycle-364 is not invoked",
        "formation remains supplied",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins selection, held test, registration boundary, and status", not missing, missing)


# Preserve the reviewed executors before installing the performance-only
# gather implementation below.  An exhaustive permutation/equivalence
# certificate runs before any scientific control.
ORIGINAL_MATTER_MATRIX = c328.matter_matrix
ORIGINAL_MATTER_VECTOR = c328.matter_vector


# The inherited source routines use a scalar loop to reshape the 4096-state
# two-cell matter vector.  These gather maps are the identical representation
# change, installed here only to keep the cold certificate bounded in wall time.
INDEX_BY_ENDPOINT = tuple(
    np.asarray(
        [
            [
                c322.JOINT_INDEX[(local, other)]
                if endpoint == 0
                else c322.JOINT_INDEX[(other, local)]
                for other in range(64)
            ]
            for local in range(64)
        ],
        dtype=int,
    )
    for endpoint in range(2)
)


def fast_matter_matrix(vector: np.ndarray, endpoint: int) -> np.ndarray:
    return np.asarray(vector)[INDEX_BY_ENDPOINT[endpoint]]


def fast_matter_vector(matrix: np.ndarray, endpoint: int) -> np.ndarray:
    vector = np.zeros(4096, dtype=complex)
    vector[INDEX_BY_ENDPOINT[endpoint].ravel()] = np.asarray(matrix).ravel()
    return vector


c328.matter_matrix = fast_matter_matrix
c328.matter_vector = fast_matter_vector


def executor_equivalence_controls() -> dict[str, object]:
    permutation_failures = 0
    formula_failures = 0
    spanning_matrix_residual = 0.0
    spanning_vector_residual = 0.0
    random_matrix_residual = 0.0
    random_vector_residual = 0.0
    random_roundtrip_residual = 0.0
    for endpoint in range(2):
        indices = INDEX_BY_ENDPOINT[endpoint]
        permutation_failures += int(
            len(np.unique(indices)) != 4096
            or int(indices.min()) != 0
            or int(indices.max()) != 4095
        )
        for local in range(64):
            for other in range(64):
                expected = (
                    c322.JOINT_INDEX[(local, other)]
                    if endpoint == 0
                    else c322.JOINT_INDEX[(other, local)]
                )
                formula_failures += int(indices[local, other] != expected)

        # Every input coordinate is distinct.  Equality of the two linear
        # permutation actions on this probe plus the exact formula/bijection
        # check is a basis-spanning certificate, not a sampled shortcut.
        spanning_vector = (
            np.arange(4096, dtype=float)
            + 1j * np.arange(4096, dtype=float)[::-1]
        )
        spanning_matrix = spanning_vector.reshape(64, 64)
        spanning_matrix_residual = max(
            spanning_matrix_residual,
            float(
                np.linalg.norm(
                    ORIGINAL_MATTER_MATRIX(spanning_vector, endpoint)
                    - fast_matter_matrix(spanning_vector, endpoint)
                )
            ),
        )
        spanning_vector_residual = max(
            spanning_vector_residual,
            float(
                np.linalg.norm(
                    ORIGINAL_MATTER_VECTOR(spanning_matrix, endpoint)
                    - fast_matter_vector(spanning_matrix, endpoint)
                )
            ),
        )
        for seed in (3740, 3741, 3742):
            rng = np.random.default_rng(seed + endpoint)
            vector = rng.normal(size=4096) + 1j * rng.normal(size=4096)
            matrix = rng.normal(size=(64, 64)) + 1j * rng.normal(size=(64, 64))
            random_matrix_residual = max(
                random_matrix_residual,
                float(
                    np.linalg.norm(
                        ORIGINAL_MATTER_MATRIX(vector, endpoint)
                        - fast_matter_matrix(vector, endpoint)
                    )
                ),
            )
            random_vector_residual = max(
                random_vector_residual,
                float(
                    np.linalg.norm(
                        ORIGINAL_MATTER_VECTOR(matrix, endpoint)
                        - fast_matter_vector(matrix, endpoint)
                    )
                ),
            )
            random_roundtrip_residual = max(
                random_roundtrip_residual,
                float(
                    np.linalg.norm(
                        fast_matter_vector(fast_matter_matrix(vector, endpoint), endpoint)
                        - vector
                    )
                ),
            )
    detail = {
        "endpoints": 2,
        "basis_coordinates_per_endpoint": 4096,
        "permutation_failures": permutation_failures,
        "exact_formula_failures": formula_failures,
        "basis_spanning_matrix_residual": spanning_matrix_residual,
        "basis_spanning_vector_residual": spanning_vector_residual,
        "random_complex_matrix_residual": random_matrix_residual,
        "random_complex_vector_residual": random_vector_residual,
        "random_complex_roundtrip_residual": random_roundtrip_residual,
        "executor_patch_scope": "performance-only representation gather",
        "semantic_residual": max(
            spanning_matrix_residual,
            spanning_vector_residual,
            random_matrix_residual,
            random_vector_residual,
            random_roundtrip_residual,
        ),
    }
    check(
        "the performance gather is basis-spanning equivalent to the reviewed Cycle-328 matter reshape before any response test",
        permutation_failures == formula_failures == 0
        and detail["semantic_residual"] == 0,
        detail,
    )
    return detail


@dataclass(frozen=True)
class MenuEntry:
    program: int
    name: str
    operator: sparse.csc_matrix


@dataclass(frozen=True)
class GradeBlindRegistrationSchema:
    preparation_width_M2: int
    program_width_M2: int
    fine_pointer_width_M2: int
    trial_width_M2: int
    use_width_M2: int
    preparation_label: int
    program_label: int
    trial_label: int
    use_label: int
    fine_pointer_domain: tuple[int, int]
    apparatus_hash: str
    numerical_grade: None = None
    occurrence: None = None
    commit: None = None
    typed_Record: None = None
    faithful_close: None = None
    provenance_acceptance: None = None
    predecessor_readiness: None = None

    @property
    def tag_width_M2(self) -> int:
        return (
            self.preparation_width_M2
            + self.program_width_M2
            + self.fine_pointer_width_M2
            + self.trial_width_M2
            + self.use_width_M2
        )


def factors():
    coin, fswap, contact, _update, detail = c315.logical_update_controls(LABELS)
    return coin.tocsc(), fswap.tocsc(), contact.tocsc(), detail


def readout_menu(coin: sparse.csc_matrix, edge_swap: sparse.csc_matrix) -> tuple[MenuEntry, ...]:
    identity = sparse.eye(coin.shape[0], format="csc", dtype=complex)
    operators = (
        ("identity", identity),
        ("matter_coin", coin),
        ("edge_fswap", edge_swap),
        ("edge_fswap_then_matter_coin", coin @ edge_swap),
        ("matter_coin_then_edge_fswap", edge_swap @ coin),
        ("edge_fswap_then_inverse_matter_coin", coin.conj().T @ edge_swap),
        ("inverse_matter_coin_then_edge_fswap", edge_swap @ coin.conj().T),
    )
    return tuple(MenuEntry(index, name, operator.tocsc()) for index, (name, operator) in enumerate(operators))


RAY = c322.symmetric_one_one_state()


def pointer_transcript(state: c331.State, operator: sparse.csc_matrix) -> dict[tuple[c331.Occupation, int], np.ndarray]:
    """Two-branch isometry with no actual-branch selector."""

    output: dict[tuple[c331.Occupation, int], np.ndarray] = {}
    for label, vector in state.items():
        rotated = operator @ vector
        branch_one = RAY * np.vdot(RAY, rotated)
        branch_zero = rotated - branch_one
        if np.linalg.norm(branch_zero) > 2e-13:
            output[(label, 0)] = branch_zero
        if np.linalg.norm(branch_one) > 2e-13:
            output[(label, 1)] = branch_one
    return output


def transcript_norm(transcript: dict[tuple[c331.Occupation, int], np.ndarray]) -> float:
    return float(sum(np.vdot(value, value).real for value in transcript.values()))


def pointer_one_coordinate(transcript: dict[tuple[c331.Occupation, int], np.ndarray]) -> float:
    return float(
        sum(
            np.vdot(value, value).real
            for (_label, branch), value in transcript.items()
            if branch == 1
        )
    )


def transcript_residual(left, right) -> float:
    keys = left.keys() | right.keys()
    zero = np.zeros(4096, dtype=complex)
    return float(np.sqrt(sum(np.vdot(left.get(key, zero) - right.get(key, zero), left.get(key, zero) - right.get(key, zero)).real for key in keys)))


def states_by_depth(
    length: int,
    update_factors,
    *,
    enabled=(True, True),
    contact_enabled: bool = True,
    q2_coin=None,
) -> tuple[dict[int, c331.State], float]:
    if length not in TRAIN_SIZES + (HELD_SIZE,):
        raise ValueError("length is outside the declared train/held domain")
    if q2_coin is None:
        q2_coin = c331.local_hardcore_coin
    original = c331.local_hardcore_coin
    c331.local_hardcore_coin = q2_coin
    try:
        state = c331.initial_state()
        rows = {}
        drift = 0.0
        for depth in DEPTHS:
            state = c331.logical_step(
                state,
                length,
                update_factors,
                enabled=enabled,
                contact_enabled=contact_enabled,
            )
            rows[depth] = state
            drift = max(drift, abs(c331.state_norm(state) - 1))
        return rows, drift
    finally:
        c331.local_hardcore_coin = original


def menu_scores(states: dict[int, c331.State], menu: tuple[MenuEntry, ...]) -> dict[tuple[int, int], float]:
    return {
        (depth, entry.program): pointer_one_coordinate(pointer_transcript(states[depth], entry.operator))
        for depth in DEPTHS
        for entry in menu
    }


def train_only_selection(update_factors, menu: tuple[MenuEntry, ...]):
    rows = []
    states = {}
    maximum_drift = 0.0
    for length in TRAIN_SIZES:
        actual, drift_actual = states_by_depth(length, update_factors)
        deleted, drift_deleted = states_by_depth(length, update_factors, contact_enabled=False)
        maximum_drift = max(maximum_drift, drift_actual, drift_deleted)
        states[(length, True)] = actual
        states[(length, False)] = deleted
        actual_scores = menu_scores(actual, menu)
        deleted_scores = menu_scores(deleted, menu)
        for depth in DEPTHS:
            for entry in menu:
                key = (depth, entry.program)
                rows.append(
                    {
                        "L": length,
                        "depth": depth,
                        "program": entry.program,
                        "name": entry.name,
                        "actual_contact": actual_scores[key],
                        "deleted_contact": deleted_scores[key],
                        "contrast": actual_scores[key] - deleted_scores[key],
                    }
                )
    candidates = []
    for depth in DEPTHS:
        for entry in menu:
            values = tuple(
                abs(row["contrast"])
                for row in rows
                if row["depth"] == depth and row["program"] == entry.program
            )
            candidates.append((min(values), depth, -entry.program, entry))
    minimum_contrast, selected_depth, _negative_program, selected = max(candidates)
    return selected_depth, selected, minimum_contrast, rows, states, maximum_drift


def selection_and_held_controls(update_factors, menu):
    selected_depth, selected, train_margin, train_rows, states, train_drift = train_only_selection(update_factors, menu)
    held_actual, held_actual_drift = states_by_depth(HELD_SIZE, update_factors)
    held_deleted, held_deleted_drift = states_by_depth(
        HELD_SIZE, update_factors, contact_enabled=False
    )
    actual_transcript = pointer_transcript(held_actual[selected_depth], selected.operator)
    deleted_transcript = pointer_transcript(held_deleted[selected_depth], selected.operator)
    actual_value = pointer_one_coordinate(actual_transcript)
    deleted_value = pointer_one_coordinate(deleted_transcript)
    actual_legacy = c331.observables(held_actual[selected_depth])
    deleted_legacy = c331.observables(held_deleted[selected_depth])
    detail = {
        "training_sizes": TRAIN_SIZES,
        "held_size": HELD_SIZE,
        "selection_inputs": TRAIN_SIZES,
        "menu_entries": len(menu) * len(DEPTHS),
        "selected_depth": selected_depth,
        "selected_program": selected.program,
        "selected_name": selected.name,
        "minimum_training_contact_contrast": train_margin,
        "held_actual_contact_coordinate": actual_value,
        "held_deleted_contact_coordinate": deleted_value,
        "held_contact_contrast": actual_value - deleted_value,
        "held_fine_transcript_residual": transcript_residual(actual_transcript, deleted_transcript),
        "held_legacy_joint_survival_actual": actual_legacy["R_A_R_B"],
        "held_legacy_joint_survival_deleted_contact": deleted_legacy["R_A_R_B"],
        "held_legacy_joint_survival_contact_contrast": (
            actual_legacy["R_A_R_B"] - deleted_legacy["R_A_R_B"]
        ),
        "held_lawful_leakage": max(
            actual_legacy["lawful_leakage"], deleted_legacy["lawful_leakage"]
        ),
        "maximum_update_norm_drift": max(train_drift, held_actual_drift, held_deleted_drift),
        "maximum_pointer_isometry_residual": max(
            abs(transcript_norm(actual_transcript) - c331.state_norm(held_actual[selected_depth])),
            abs(transcript_norm(deleted_transcript) - c331.state_norm(held_deleted[selected_depth])),
        ),
    }
    check(
        "the 14-entry train-only menu freezes a contact-sensitive readout before held L=6",
        HELD_SIZE not in detail["selection_inputs"]
        and selected_depth == 2
        and selected.name == "inverse_matter_coin_then_edge_fswap"
        and train_margin > 1e-3
        and abs(detail["held_contact_contrast"]) > 1e-3
        and abs(detail["held_legacy_joint_survival_contact_contrast"]) < TOL
        and detail["held_lawful_leakage"] == 0
        and detail["held_fine_transcript_residual"] > 1e-3
        and detail["maximum_update_norm_drift"] < TOL
        and detail["maximum_pointer_isometry_residual"] < TOL,
        detail,
    )
    return {
        "selected_depth": selected_depth,
        "selected": selected,
        "train_rows": train_rows,
        "states": states,
        "held_actual": held_actual,
        "held_deleted": held_deleted,
        "detail": detail,
    }


def frame_controls(result, coin):
    selected: MenuEntry = result["selected"]
    source_operator = selected.operator
    source_ray = RAY
    residuals = []
    ray_residuals = []
    coordinate_residuals = []
    endpoint_reversals = 0
    source_transcript = pointer_transcript(
        result["states"][(3, True)][result["selected_depth"]], source_operator
    )
    source_coordinate = pointer_one_coordinate(source_transcript)
    for frame in c210.proper_cubic_frames():
        mapped_direction = frame @ np.asarray((1, 0, 0), dtype=int)
        axis = int(np.flatnonzero(mapped_direction)[0])
        reversed_endpoints = int(mapped_direction[axis]) == -1
        endpoint_reversals += reversed_endpoints
        representation = c315.pair_frame_representation(LABELS, frame, reversed_endpoints)
        target_swap = c315.edge_fswap_matrix(LABELS, axis)
        target_operator = target_swap @ coin.conj().T
        residuals.append(raw_maximum(representation @ source_operator - target_operator @ representation))
        mapped_ray = representation @ source_ray
        overlap = np.vdot(source_ray, mapped_ray)
        ray_residuals.append(float(np.linalg.norm(mapped_ray - overlap * source_ray)))
        # The mediator labels only undergo a permutation, which disappears in
        # the coarse sum.  Matter covariance is checked directly on every
        # occupied label of the actual training state.
        transformed_coordinate = 0.0
        for vector in result["states"][(3, True)][result["selected_depth"]].values():
            transformed = representation @ vector
            branch = source_ray * np.vdot(source_ray, target_operator @ transformed)
            transformed_coordinate += float(np.vdot(branch, branch).real)
        coordinate_residuals.append(abs(transformed_coordinate - source_coordinate))
    detail = {
        "proper_cubic_frames": len(residuals),
        "endpoint_reversing_frames": endpoint_reversals,
        "maximum_readout_intertwiner_raw_residual": max(residuals),
        "maximum_projector_ray_residual": max(ray_residuals),
        "maximum_actual_output_coordinate_residual": max(coordinate_residuals),
    }
    check(
        "the selected readout and actual transcript coordinate transform in all 24 proper-cubic frames",
        len(residuals) == 24
        and endpoint_reversals == 12
        and max(residuals) < TOL
        and max(ray_residuals) < TOL
        and max(coordinate_residuals) < TOL,
        detail,
    )
    return detail


def source_deletion_and_alternative_controls(result, update_factors):
    depth = result["selected_depth"]
    selected: MenuEntry = result["selected"]
    deleted_source, source_drift = states_by_depth(
        HELD_SIZE, update_factors, enabled=(True, False)
    )
    deleted_source_value = pointer_one_coordinate(
        pointer_transcript(deleted_source[depth], selected.operator)
    )
    actual_value = result["detail"]["held_actual_contact_coordinate"]
    source_observed = c331.observables(deleted_source[depth])

    original_coin = c331.local_hardcore_coin

    def signed_q2_coin(charge: int) -> np.ndarray:
        base = original_coin(charge)
        return -base if charge == 2 else base

    signed_states, signed_drift = states_by_depth(
        3, update_factors, q2_coin=signed_q2_coin
    )
    signed_deleted, signed_deleted_drift = states_by_depth(
        3, update_factors, contact_enabled=False, q2_coin=signed_q2_coin
    )
    signed_contrast = pointer_one_coordinate(
        pointer_transcript(signed_states[depth], selected.operator)
    ) - pointer_one_coordinate(
        pointer_transcript(signed_deleted[depth], selected.operator)
    )

    statistics_rows = []
    for statistics in ("bosonic", "independent"):
        state, observed, drift = c328.run_response(
            3, update_factors, statistics, depths=depth
        )
        deleted, deleted_observed, deleted_drift = c328.run_response(
            3,
            update_factors,
            statistics,
            depths=depth,
            contact_enabled=False,
        )
        value = pointer_one_coordinate(pointer_transcript(state, selected.operator))
        deleted_value = pointer_one_coordinate(pointer_transcript(deleted, selected.operator))
        statistics_rows.append(
            {
                "statistics": statistics,
                "actual_contact_coordinate": value,
                "deleted_contact_coordinate": deleted_value,
                "contact_contrast": value - deleted_value,
                "norm_drift": max(drift, deleted_drift),
                "lawful_leakage": max(
                    observed["lawful_Q2_leakage"], deleted_observed["lawful_Q2_leakage"]
                ),
            }
        )
    detail = {
        "deleted_source_B_pointer_coordinate": deleted_source_value,
        "actual_minus_deleted_source_B": actual_value - deleted_source_value,
        "deleted_source_B_reservoir_fixture": source_observed["R_B"],
        "deleted_source_norm_drift": source_drift,
        "signed_Q2_collision_contact_contrast_L3": signed_contrast,
        "signed_Q2_collision_norm_drift": max(signed_drift, signed_deleted_drift),
        "statistics_alternatives_L3": statistics_rows,
        "statistics_or_collision_rule_selected": False,
    }
    check(
        "source deletion is visible while its untouched reservoir fixture remains fixed; collision/statistics alternatives stay explicit",
        abs(detail["actual_minus_deleted_source_B"]) > 1e-3
        and abs(detail["deleted_source_B_reservoir_fixture"] - 1) < TOL
        and detail["deleted_source_norm_drift"] < TOL
        and abs(signed_contrast) > 1e-4
        and detail["signed_Q2_collision_norm_drift"] < TOL
        and all(abs(row["contact_contrast"]) > 1e-4 for row in statistics_rows)
        and all(row["norm_drift"] < TOL and row["lawful_leakage"] < TOL for row in statistics_rows)
        and detail["statistics_or_collision_rule_selected"] is False,
        detail,
    )
    return detail


def physical_code_and_ledger_controls(result, coin, edge_swap, contact, logical_detail):
    depth = result["selected_depth"]
    selected: MenuEntry = result["selected"]
    rows = []
    rng = np.random.default_rng(374)
    vector = rng.normal(size=4096) + 1j * rng.normal(size=4096)
    vector /= np.linalg.norm(vector)
    for orientation, reverse in (("AB", False), ("BA", True)):
        encoding = c322.build_encoding(3, reverse)
        encoded = encoding @ vector
        decoded = encoding.conj().T @ encoded
        logical_transcript = pointer_transcript({(0, 1): vector}, selected.operator)
        decoded_transcript = pointer_transcript({(0, 1): decoded}, selected.operator)
        physical_transcript = {
            key: encoding @ value for key, value in decoded_transcript.items()
        }
        expected_physical = {
            key: encoding @ value for key, value in logical_transcript.items()
        }
        zero = np.zeros(encoding.shape[0], dtype=complex)
        residual = float(
            np.sqrt(
                sum(
                    np.vdot(
                        physical_transcript.get(key, zero) - expected_physical.get(key, zero),
                        physical_transcript.get(key, zero) - expected_physical.get(key, zero),
                    ).real
                    for key in physical_transcript.keys() | expected_physical.keys()
                )
            )
        )
        rows.append(
            {
                "orientation": orientation,
                "sampled_decode_residual": float(np.linalg.norm(decoded - vector)),
                "sampled_readout_intertwiner_residual": residual,
                "encoded_input_norm_residual": abs(float(np.vdot(encoded, encoded).real) - 1),
                "physical_pointer_isometry_residual": abs(
                    sum(float(np.vdot(value, value).real) for value in physical_transcript.values())
                    - 1
                ),
            }
        )

    source_rows = []
    for local_q in (1, 2):
        generator = c331.hardcore_source_generator(local_q)
        configurations = c331.hardcore_local_configurations(local_q)
        q_operator = sparse.eye(generator.shape[0], format="csc") * local_q
        matter_numbers = sparse.diags(
            [mask.bit_count() for _configuration in configurations for mask in c331.LOCAL_MASKS],
            format="csc",
            dtype=float,
        )
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
                for axis in range(3):
                    vector_values[axis].append(
                        float(matter_vector[axis] + 2 * field_vector[axis])
                    )
        vector_operators = tuple(
            sparse.diags(values, format="csc", dtype=float)
            for values in vector_values
        )
        source_rows.append(
            {
                "local_Q": local_q,
                "Hermiticity": raw_maximum(generator - generator.conj().T),
                "Q_ledger": raw_maximum(generator @ q_operator - q_operator @ generator),
                "matter_number_ledger": raw_maximum(
                    generator @ matter_numbers - matter_numbers @ generator
                ),
                "vector_ledgers": tuple(
                    raw_maximum(generator @ operator - operator @ generator)
                    for operator in vector_operators
                ),
            }
        )
    contact_deletion = c315.largest_singular(
        contact - sparse.eye(contact.shape[0], format="csc")
    )
    detail = {
        "physical_readout_rows": rows,
        "source_ledger_rows": source_rows,
        "one_particle_mass_fixture": logical_detail["Cycle219_mass_fixture"],
        "two_cell_mass_fixture": logical_detail["two_cell_rest_mass"],
        "one_particle_mass_residual": logical_detail["two_cell_uniform_one_particle_residual"],
        "actual_contact_nontrivial_columns": logical_detail["contact_nontrivial_columns"],
        "actual_contact_deletion_opnorm": contact_deletion,
        "inherited_common_seam_M2_per_cell": 36,
        "inherited_two_cell_patch_M2": 97,
        "pointer_M2": 1,
        "readout_patch_M2": 98,
        "readout_primitive_matrix_unit_synthesis": "supplied",
        "selected_update_depth": depth,
    }
    check(
        "the pointer isometry has a bounded AB/BA code completion and preserves the source, mass, contact, and code ledgers",
        max(
            value
            for row in rows
            for key, value in row.items()
            if key != "orientation"
        ) < TOL
        and max(
            max(value) if isinstance(value, tuple) else value
            for row in source_rows
            for key, value in row.items()
            if key != "local_Q"
        ) == 0
        and abs(detail["one_particle_mass_fixture"] - detail["two_cell_mass_fixture"]) < TOL
        and detail["one_particle_mass_residual"] < TOL
        and detail["actual_contact_nontrivial_columns"] == 4047
        and detail["actual_contact_deletion_opnorm"] > 1.9
        and detail["readout_patch_M2"] == 98,
        detail,
    )
    return detail


def registration_and_domain_controls(result):
    selected: MenuEntry = result["selected"]
    depth = result["selected_depth"]
    apparatus_payload = (
        f"Cycle331|depth={depth}|program={selected.program}|name={selected.name}|"
        "ray=symmetric-one-one|pointer=orthogonal-two-branch"
    ).encode("utf-8")
    schema = GradeBlindRegistrationSchema(
        preparation_width_M2=2,
        program_width_M2=3,
        fine_pointer_width_M2=3,
        trial_width_M2=4,
        use_width_M2=1,
        preparation_label=0,
        program_label=selected.program,
        trial_label=depth - 1,
        use_label=0,
        fine_pointer_domain=(0, 1),
        apparatus_hash=sha256(apparatus_payload).hexdigest(),
    )
    with_grade = replace(schema, numerical_grade=None)
    deleted_grade = replace(with_grade, numerical_grade=None)
    rejections = 0
    for call in (
        lambda: states_by_depth(5, (None, None, None)),
        lambda: pointer_transcript(c331.initial_state(), sparse.eye(16, format="csc")),
        lambda: GradeBlindRegistrationSchema(
            2, 2, 3, 4, 1, 0, selected.program, depth - 1, 0, (0, 1), "bad"
        ),
    ):
        try:
            value = call()
            if isinstance(value, GradeBlindRegistrationSchema) and value.program_width_M2 < 3:
                raise ValueError("program does not fit schema")
        except (TypeError, ValueError):
            rejections += 1
    detail = {
        "Cycle351_compatible_field_widths_M2": (2, 3, 3, 4, 1),
        "registered_tag_width_M2": schema.tag_width_M2,
        "schema": asdict(schema),
        "schema_unchanged_when_grade_absent": asdict(with_grade) == asdict(deleted_grade),
        "pointer_branch_selected": False,
        "actual_member_selector": None,
        "Cycle364_invoked": False,
        "faithful_close_available": False,
        "provenance_acceptance_available": False,
        "predecessor_readiness_available": False,
        "formation": "supplied/open",
        "lawful_domain_rejections": rejections,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the Cycle-351-compatible registration is grade-blind; Cycle-364 is unavailable without close, provenance, and readiness",
        schema.tag_width_M2 == 13
        and detail["schema_unchanged_when_grade_absent"]
        and detail["pointer_branch_selected"] is False
        and detail["actual_member_selector"] is None
        and detail["Cycle364_invoked"] is False
        and not detail["faithful_close_available"]
        and not detail["provenance_acceptance_available"]
        and not detail["predecessor_readiness_available"]
        and detail["formation"] == "supplied/open"
        and rejections == 3
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )
    return detail


def inventory_controls(result, alternative, physical, registration, frame, executor):
    detail = {
        "constructed": "bounded contact-sensitive two-branch operational transcript on the Cycle-331 common seam",
        "supplied": (
            "Cycle-315 complete matter seam, physical encodings, FSWAP, and actual Cycle-230 contact",
            "Cycle-331 hard-core mediator exclusion, source angle, coefficient-two ledger, Q1 coin, and Q2 collision block",
            "symmetric one-one matter preparation, both occupied reservoirs, and finite update depths",
            "finite seven-readout by two-depth train menu and maximin/lexicographic selection rule",
            "inverse matter coin, mapped edge FSWAP, symmetric one-one projector, pointer M2, and bounded matrix-unit completion",
            "finite periodic L3/L4 train and held L6 domains, tolerances, and frame action",
            "Cycle-351-compatible 13-M2 tag field widths",
        ),
        "not_selected": (
            "mediator statistics or collision law",
            "numerical grade",
            "pointer branch or actual member",
            "occurrence, commit, typing, close, provenance, readiness, or formation",
            "empirical calibration or far-side interpretation",
        ),
        "menu_selection_used_held_data": False,
        "global_ordering_or_parity_service": False,
        "state_dependent_host_readout_selection": False,
        "record_formed": False,
        "formation_supplied": True,
        "frame_cases": frame["proper_cubic_frames"],
        "readout_patch_M2": physical["readout_patch_M2"],
        "alternative_rows": alternative,
        "registration": registration,
        "performance_executor_equivalence": executor,
        "shared_obstruction": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the supplied-law and semantic inventory is explicit with no shared obstruction or axiom pressure",
        detail["menu_selection_used_held_data"] is False
        and detail["global_ordering_or_parity_service"] is False
        and detail["state_dependent_host_readout_selection"] is False
        and detail["record_formed"] is False
        and detail["formation_supplied"] is True
        and detail["frame_cases"] == 24
        and detail["readout_patch_M2"] == 98
        and detail["performance_executor_equivalence"]["semantic_residual"] == 0
        and detail["shared_obstruction"] is detail["axiom_pressure"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 374: PHYSICAL CONTACT-SENSITIVE OPERATIONAL TRANSCRIPT")
    print("authority=none; audit=unset")
    note_contract()
    executor = executor_equivalence_controls()
    coin, edge_swap, contact, logical_detail = factors()
    update_factors = (coin, edge_swap, contact)
    menu = readout_menu(coin, edge_swap)
    result = selection_and_held_controls(update_factors, menu)
    frame = frame_controls(result, coin)
    alternative = source_deletion_and_alternative_controls(result, update_factors)
    physical = physical_code_and_ledger_controls(
        result, coin, edge_swap, contact, logical_detail
    )
    registration = registration_and_domain_controls(result)
    inventory_controls(result, alternative, physical, registration, frame, executor)
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_CONTACT_SENSITIVE_OPERATIONAL_TRANSCRIPT_OPEN")
        return 1
    print("RESULT PHYSICAL_CONTACT_SENSITIVE_OPERATIONAL_TRANSCRIPT_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
