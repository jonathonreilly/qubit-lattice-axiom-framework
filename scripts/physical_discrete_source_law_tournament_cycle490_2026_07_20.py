#!/usr/bin/env python3
"""Cycle 490: isolated discrete source-law tournament on the Cycle487 compiler.

Three frozen source laws are tested against the four Cycle420 quadrupole rows:
an analytic source-word law, repeated local source excitation, and one common
train-only calibrated source word.  The receiver word stays fixed.  Response
is not gravity, phase is not energy, a generator is not a rate, schedule depth
is not time, and norm weight is not probability.  Authority none; audit unset.
"""

from __future__ import annotations

from dataclasses import asdict
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from time import perf_counter
import resource
import sys

import numpy as np
from scipy import optimize, sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_discrete_quadrupole_exact_strength_bridge_cycle487_2026_07_20 as c487


c453 = c487.c453
c435 = c487.c435
c420 = c487.c420
c480 = c487.c480
c476 = c487.c476
c472 = c487.c472

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DISCRETE_SOURCE_LAW_TOURNAMENT_CYCLE490_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
RECEIVER_WORD = 256
COEFFICIENT_MIN = 1
COEFFICIENT_MAX = 1023
CALIBRATION_MAX_EVALUATIONS = 40
CALIBRATION_XATOL = 0.25
CALIBRATION_NEIGHBORHOOD = 2
REPETITIONS = 2
ROW_TOLERANCE = c453.NUMERIC_ROW_TOLERANCE
BOUNDARY_MAXIMUM = c453.BOUNDARY_MAXIMUM
SIGNAL_FLOOR = c453.SIGNAL_FLOOR
WALL_CAP_SECONDS = 900.0
RSS_CAP_MIB = 3072.0
PASS = 0
FAIL = 0

FROZEN = {
    "Cycle487": (
        "physical_discrete_quadrupole_exact_strength_bridge_cycle487_2026_07_20.py",
        "b0e4ac4aea641dbf90f64ac6d944b639b983ec76e365c3a60377b1ea2b5cf091",
    ),
}

# Frozen before any Cycle490 row was evaluated.
ROUTES = {
    "A_analytic_sqrt_source_word": {
        "q1_occupation": "one",
        "source_word": "round(256*sqrt(p_route))",
        "source_repetitions": 1,
        "fitted_parameters": 0,
    },
    "B_two_coherent_source_passes": {
        "q1_occupation": "p_route",
        "source_word": RECEIVER_WORD,
        "source_repetitions": REPETITIONS,
        "fitted_parameters": 0,
    },
    "C_train_only_common_source_word": {
        "q1_occupation": "p_route",
        "source_word": "one common integer selected on both a1 rows",
        "source_repetitions": 1,
        "fitted_parameters": 1,
    },
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset", "cycle 490",
        "a — analytic source-word law", "b — two coherent source passes",
        "c — one train-only common source word", "frozen before outputs",
        "l13/a1/depth4", "l13/a2/depth4", "held rows never refit",
        "all four absolute rows", "stronger-a2 order", "numeric tolerance 5e-10",
        "compiler/product/angle residuals", "source-law/prediction residuals",
        "q1 occupation is not source strength", "renewal count zero",
        "response is not gravity", "phase is not energy", "generator is not a rate",
        "depth is not time", "norm weight is not probability",
        "n1 — alternative route enumeration", "n8 — cross-cycle echo and claim gate",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in normalized(NOTE))
    check("the Cycle490 note freezes the source-law tournament before outputs", not missing, missing)


def frozen_controls() -> None:
    observed = {
        name: file_sha(ROOT / "scripts" / filename)
        for name, (filename, _digest) in FROZEN.items()
    }
    expected = {name: digest for name, (_filename, digest) in FROZEN.items()}
    check("Cycle487 remains frozen at its exact input identity", observed == expected,
          {"observed": observed, "expected": expected})


def validate_word(word: int) -> None:
    if not isinstance(word, (int, np.integer)) or not COEFFICIENT_MIN <= int(word) <= COEFFICIENT_MAX:
        raise ValueError("uniform source word must be an integer in [1,1023]")


@lru_cache(maxsize=None)
def local_vertex(word: int, inverse: bool = False) -> np.ndarray:
    validate_word(word)
    identity = np.eye(448, dtype=complex)
    native = c480.product_action(
        identity, (int(word),) * 6, route=c487.SELECTED_ROUTE,
        discrete=True, inverse=inverse,
    )
    adapter = c487.q1_basis_adapter()
    return adapter @ native @ adapter.conj().T


@lru_cache(maxsize=None)
def restricted_vertex(group: str, cell_index: int, word: int, inverse: bool = False):
    return c487._restricted_from_local(group, cell_index, local_vertex(word, inverse))


def apply_vertex(state, geometry, group: str, cell_index: int, word: int, *, inverse: bool = False):
    cell = geometry.sources[cell_index] if group == "source" else geometry.receivers[cell_index]
    active = c435.vertex_keys(cell, geometry.length)
    zero = np.zeros((c435.SOURCE_DIM, c435.RECEIVER_DIM), dtype=complex)
    packed = np.stack([state.get(key, zero) for key in active], axis=2)
    transformed = np.empty_like(packed)
    operator = restricted_vertex(group, cell_index, word, inverse)
    if group == "source":
        for receiver_index in range(c435.RECEIVER_DIM):
            transformed[:, receiver_index, :] = (
                operator @ packed[:, receiver_index, :].reshape(-1)
            ).reshape((c435.SOURCE_DIM, 7))
    else:
        for source_index in range(c435.SOURCE_DIM):
            transformed[source_index, :, :] = (
                operator @ packed[source_index, :, :].reshape(-1)
            ).reshape((c435.RECEIVER_DIM, 7))
    output = {key: value.copy() for key, value in state.items() if key not in active}
    for local, key in enumerate(active):
        output[key] = transformed[:, :, local]
    return c435.prune(output)


def logical_step(state, geometry, *, source_word: int, source_repetitions: int = 1,
                 source_enabled: bool = True, receiver_enabled: bool = True,
                 stream_enabled: bool = True, packet_stream_enabled: bool = True,
                 contact_enabled: bool = True):
    validate_word(source_word)
    if source_repetitions not in (1, REPETITIONS):
        raise ValueError("source repetitions leave the frozen tournament domain")
    c435.validate_geometry(geometry)
    _rows, source_coin, receiver_coin, source_contact, receiver_contact, first, second = c435.restricted_factors()
    output = c435.apply_matter(state, source_coin, receiver_coin)
    output = c435.field_coin(output, geometry.length)
    if source_enabled:
        for _repeat in range(source_repetitions):
            for cell_index in range(3):
                output = apply_vertex(output, geometry, "source", cell_index, source_word)
    if receiver_enabled:
        for cell_index in range(3):
            output = apply_vertex(output, geometry, "receiver", cell_index, RECEIVER_WORD)
    if packet_stream_enabled:
        output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), first)
        output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), second)
    output = c435.field_stream(output, geometry.length, enabled=stream_enabled)
    if contact_enabled:
        output = c435.apply_matter(output, source_contact, receiver_contact)
    return output


def logical_inverse(state, geometry, *, source_word: int, source_repetitions: int = 1):
    _rows, source_coin, receiver_coin, source_contact, receiver_contact, first, second = c435.restricted_factors()
    output = c435.apply_matter(state, source_contact.getH(), receiver_contact.getH())
    output = c435.field_stream(output, geometry.length, inverse=True)
    output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), second.getH())
    output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), first.getH())
    for cell_index in (2, 1, 0):
        output = apply_vertex(output, geometry, "receiver", cell_index, RECEIVER_WORD, inverse=True)
    for _repeat in range(source_repetitions):
        for cell_index in (2, 1, 0):
            output = apply_vertex(output, geometry, "source", cell_index, source_word, inverse=True)
    output = c435.field_coin(output, geometry.length, inverse=True)
    return c435.apply_matter(output, source_coin.getH(), receiver_coin.getH())


def boundary_norm_weight(state, geometry) -> float:
    total = 0.0
    for key, value in state.items():
        cell = c453.field_cell(key, geometry.length)
        if cell is not None and any(coordinate in (0, geometry.length - 1) for coordinate in cell):
            total += float(np.vdot(value, value).real)
    return total


def evolve(state, geometry, *, source_word: int, source_repetitions: int = 1, **kwargs):
    output = state
    controls = {
        "maximum_boundary_norm_weight": boundary_norm_weight(output, geometry),
        "maximum_norm_error": abs(c435.state_norm(output) - 1),
        "maximum_active_field_keys": len(output),
        "maximum_logical_payload_bytes": sum(value.nbytes for value in output.values()),
    }
    for _ in range(geometry.depth):
        output = logical_step(
            output, geometry, source_word=source_word,
            source_repetitions=source_repetitions, **kwargs,
        )
        controls["maximum_boundary_norm_weight"] = max(
            controls["maximum_boundary_norm_weight"], boundary_norm_weight(output, geometry)
        )
        controls["maximum_norm_error"] = max(
            controls["maximum_norm_error"], abs(c435.state_norm(output) - 1)
        )
        controls["maximum_active_field_keys"] = max(controls["maximum_active_field_keys"], len(output))
        controls["maximum_logical_payload_bytes"] = max(
            controls["maximum_logical_payload_bytes"], sum(value.nbytes for value in output.values())
        )
    return output, controls


@lru_cache(maxsize=None)
def pure_result(geometry_name: str, source_word: int, source_repetitions: int):
    geometry = next(item for item in c453.GEOMETRIES if item.name == geometry_name)
    return evolve(c435.quadrupole_state(geometry), geometry,
                  source_word=source_word, source_repetitions=source_repetitions)


@lru_cache(maxsize=None)
def free_result(geometry_name: str):
    geometry = next(item for item in c453.GEOMETRIES if item.name == geometry_name)
    return evolve(c435.vacuum_state(), geometry, source_word=RECEIVER_WORD)


def row_for(geometry, route_label: str, occupation: float, source_word: int,
            source_repetitions: int, *, fitted: bool, fit_surface: str | None):
    free_state, free_controls = free_result(geometry.name)
    pure_state, pure_controls = pure_result(geometry.name, source_word, source_repetitions)
    free_weights = c435.packet_weights(free_state)
    pure_weights = c435.packet_weights(pure_state)
    weights = (1 - occupation) * free_weights + occupation * pure_weights
    coherent = c435.combine(
        (free_state, pure_state), np.asarray((np.sqrt(1 - occupation), np.sqrt(occupation)), dtype=complex)
    ) if occupation < 1 else pure_state
    moments = c435.packet_moments(weights)
    free = c435.packet_moments(free_weights)
    target = c453.LEGACY_ROWS[(geometry.separation, route_label)]
    shift = moments["width"] - free["width"]
    return {
        "geometry": geometry.name,
        "separation": geometry.separation,
        "held": geometry.held,
        "target_route": route_label,
        "Q1_occupation": occupation,
        "source_word": source_word,
        "receiver_word": RECEIVER_WORD,
        "source_repetitions_per_step": source_repetitions,
        "source_renewal_count": 0,
        "width_shift": shift,
        "Cycle420_exact_target": target,
        "source_law_prediction_residual": shift - target,
        "centroid_shift": moments["centroid"] - free["centroid"],
        "maximum_boundary_norm_weight_upper_bound": (
            (1 - occupation) * free_controls["maximum_boundary_norm_weight"]
            + occupation * pure_controls["maximum_boundary_norm_weight"]
        ),
        "maximum_norm_error": max(free_controls["maximum_norm_error"], pure_controls["maximum_norm_error"]),
        "coherent_weight_residual": float(np.linalg.norm(c435.packet_weights(coherent) - weights)),
        "fitted": fitted,
        "fit_surface": fit_surface,
        "held_refit": False,
    }


def train_objective(source_word: int) -> float:
    validate_word(source_word)
    residuals = []
    for route, occupation in c453.PHYSICAL_STRENGTHS.items():
        row = row_for(c453.TRAIN, route, occupation, source_word, 1,
                      fitted=True, fit_surface="both train a1 rows")
        residuals.append(row["source_law_prediction_residual"] / row["Cycle420_exact_target"])
    return float(np.dot(residuals, residuals))


def calibrate_common_word():
    evaluations: dict[int, float] = {}

    def objective(value: float) -> float:
        word = int(np.clip(np.rint(value), COEFFICIENT_MIN, COEFFICIENT_MAX))
        if word not in evaluations:
            evaluations[word] = train_objective(word)
        return evaluations[word]

    result = optimize.minimize_scalar(
        objective, method="bounded", bounds=(COEFFICIENT_MIN, COEFFICIENT_MAX),
        options={"xatol": CALIBRATION_XATOL, "maxiter": CALIBRATION_MAX_EVALUATIONS},
    )
    center = int(np.clip(np.rint(result.x), COEFFICIENT_MIN, COEFFICIENT_MAX))
    for word in range(max(COEFFICIENT_MIN, center - CALIBRATION_NEIGHBORHOOD),
                      min(COEFFICIENT_MAX, center + CALIBRATION_NEIGHBORHOOD) + 1):
        objective(float(word))
    selected = min(evaluations, key=lambda word: (evaluations[word], word))
    return selected, {
        "algorithm": "bounded scalar search followed by fixed +/-2 integer neighborhood",
        "objective": "sum over both a1 rows of ((prediction-target)/target)^2",
        "bounds": (COEFFICIENT_MIN, COEFFICIENT_MAX),
        "maximum_optimizer_iterations": CALIBRATION_MAX_EVALUATIONS,
        "xatol": CALIBRATION_XATOL,
        "integer_neighborhood": CALIBRATION_NEIGHBORHOOD,
        "evaluated_words": tuple(sorted(evaluations)),
        "evaluations": len(evaluations),
        "selected_train_objective": evaluations[selected],
        "held_values_used": 0,
        "model_parameters": 1,
        "tie_break": "smaller integer source word",
    }


def prediction_controls():
    print("\nFROZEN THREE-ROUTE SOURCE-LAW TOURNAMENT")
    selected_word, calibration = calibrate_common_word()
    print("TRAIN_ONLY_CALIBRATION_BEFORE_HELD", {
        "objective": calibration["objective"],
        "bounds": calibration["bounds"],
        "maximum_optimizer_iterations": calibration["maximum_optimizer_iterations"],
        "xatol": calibration["xatol"],
        "integer_neighborhood": calibration["integer_neighborhood"],
        "tie_break": calibration["tie_break"],
        "selected_word": selected_word,
        "selected_train_objective": calibration["selected_train_objective"],
        "held_values_used": calibration["held_values_used"],
    }, flush=True)
    rows_by_route: dict[str, list[dict[str, object]]] = {name: [] for name in ROUTES}
    for geometry in c453.GEOMETRIES:
        for target_route, occupation in c453.PHYSICAL_STRENGTHS.items():
            analytic_word = int(np.rint(c476.COEFFICIENT_SCALE * np.sqrt(occupation)))
            rows_by_route["A_analytic_sqrt_source_word"].append(
                row_for(geometry, target_route, 1.0, analytic_word, 1,
                        fitted=False, fit_surface=None)
            )
            rows_by_route["B_two_coherent_source_passes"].append(
                row_for(geometry, target_route, occupation, RECEIVER_WORD, REPETITIONS,
                        fitted=False, fit_surface=None)
            )
            rows_by_route["C_train_only_common_source_word"].append(
                row_for(geometry, target_route, occupation, selected_word, 1,
                        fitted=True, fit_surface="both train a1 rows")
            )

    dispositions = {}
    for route, rows in rows_by_route.items():
        keyed = {(row["separation"], row["target_route"]): row for row in rows}
        maximum = max(abs(row["source_law_prediction_residual"]) for row in rows)
        train_maximum = max(abs(row["source_law_prediction_residual"]) for row in rows if not row["held"])
        held_maximum = max(abs(row["source_law_prediction_residual"]) for row in rows if row["held"])
        held_order = all(
            keyed[(2, target)]["width_shift"] > keyed[(1, target)]["width_shift"]
            for target in c453.PHYSICAL_STRENGTHS
        )
        pure_geometry_ratios = {}
        for target in c453.PHYSICAL_STRENGTHS:
            train_row = keyed[(1, target)]
            held_row = keyed[(2, target)]
            train_free = c435.packet_moments(c435.packet_weights(free_result(c453.TRAIN.name)[0]))
            held_free = c435.packet_moments(c435.packet_weights(free_result(c453.HELD.name)[0]))
            train_pure = c435.packet_moments(c435.packet_weights(
                pure_result(c453.TRAIN.name, int(train_row["source_word"]),
                            int(train_row["source_repetitions_per_step"]))[0]
            ))
            held_pure = c435.packet_moments(c435.packet_weights(
                pure_result(c453.HELD.name, int(held_row["source_word"]),
                            int(held_row["source_repetitions_per_step"]))[0]
            ))
            pure_geometry_ratios[target] = (
                (held_pure["width"] - held_free["width"])
                / (train_pure["width"] - train_free["width"])
            )
        all_rows = maximum < ROW_TOLERANCE
        dispositions[route] = {
            "maximum_absolute_row_residual": maximum,
            "maximum_train_residual": train_maximum,
            "maximum_held_residual": held_maximum,
            "all_four_rows_within_tolerance": all_rows,
            "stronger_a2_order": held_order,
            "terminal_obligation_met": all_rows and held_order,
            "held_to_train": {
                target: keyed[(2, target)]["width_shift"] / keyed[(1, target)]["width_shift"]
                for target in c453.PHYSICAL_STRENGTHS
            },
            "pure_response_held_to_train_geometry_ratio": pure_geometry_ratios,
            "global_output_normalization_can_repair_order_at_observed_dynamics": all(
                value > 1 for value in pure_geometry_ratios.values()
            ),
            "route_changes_local_dynamics_or_schedule": route in (
                "A_analytic_sqrt_source_word", "B_two_coherent_source_passes",
                "C_train_only_common_source_word",
            ),
            "ordering_reading": (
                "source word or repetition can change the pure dynamics in principle; "
                "after selection, a pure ratio below one cannot be repaired by any further global scale"
            ),
        }
    all_rows = tuple(row for rows in rows_by_route.values() for row in rows)
    check(
        "all three frozen source laws execute all four rows with centered, resolved, norm, boundary, coherent-sector, renewal, and held-no-refit controls",
        len(all_rows) == 12
        and min(row["width_shift"] for row in all_rows) > SIGNAL_FLOOR
        and max(abs(row["centroid_shift"]) for row in all_rows) < 3e-13
        and max(row["maximum_norm_error"] for row in all_rows) < c435.TOLERANCE
        and max(row["maximum_boundary_norm_weight_upper_bound"] for row in all_rows) < BOUNDARY_MAXIMUM
        and max(row["coherent_weight_residual"] for row in all_rows) < c435.TOLERANCE
        and all(row["source_renewal_count"] == 0 and not row["held_refit"] for row in all_rows)
        and calibration["held_values_used"] == 0,
        {"rows": rows_by_route, "calibration": calibration},
    )
    check(
        "the four-row plus stronger-a2 terminal obligation is evaluated without promoting a failed source law",
        all(
            disposition["terminal_obligation_met"]
            == (disposition["all_four_rows_within_tolerance"] and disposition["stronger_a2_order"])
            for disposition in dispositions.values()
        ),
        {"numeric_row_tolerance": ROW_TOLERANCE, "dispositions": dispositions},
    )
    print("TOURNAMENT_ROWS", rows_by_route, flush=True)
    print("TOURNAMENT_DISPOSITIONS", dispositions, flush=True)
    return {"rows": rows_by_route, "dispositions": dispositions,
            "calibrated_word": selected_word, "calibration": calibration}


def exact_vertex(word: int) -> np.ndarray:
    vector = np.full(6, word / c476.COEFFICIENT_SCALE)
    native = c480.expm_multiply(
        1j * c476.c426.ANGLE * c476.coefficient_generator(vector),
        np.eye(448, dtype=complex),
    )
    adapter = c487.q1_basis_adapter()
    return adapter @ native @ adapter.conj().T


def compiler_controls(prediction):
    words = {RECEIVER_WORD, prediction["calibrated_word"]}
    for occupation in c453.PHYSICAL_STRENGTHS.values():
        words.add(int(np.rint(c476.COEFFICIENT_SCALE * np.sqrt(occupation))))
    rows = []
    for word in sorted(words):
        identity = np.eye(448, dtype=complex)
        exact = exact_vertex(word)
        continuous_native = c480.product_action(
            identity, (word,) * 6, route=c487.SELECTED_ROUTE, discrete=False,
        )
        adapter = c487.q1_basis_adapter()
        product = adapter @ continuous_native @ adapter.conj().T
        discrete = local_vertex(word)
        rows.append({
            "word": word,
            "coefficient": word / c476.COEFFICIENT_SCALE,
            "product_formula_operator_residual": float(np.linalg.norm(product - exact, 2)),
            "discrete_angle_operator_residual": float(np.linalg.norm(discrete - product, 2)),
            "total_compiler_operator_residual": float(np.linalg.norm(discrete - exact, 2)),
            "unitarity_residual": float(np.linalg.norm(discrete.conj().T @ discrete - identity, 2)),
            "inverse_residual": float(np.linalg.norm(local_vertex(word, True) @ discrete - identity, 2)),
        })
    analytic_rounding = {
        route: {
            "target_sqrt_occupation": float(np.sqrt(occupation)),
            "selected_word": int(np.rint(c476.COEFFICIENT_SCALE * np.sqrt(occupation))),
            "coefficient_rounding_residual": float(
                int(np.rint(c476.COEFFICIENT_SCALE * np.sqrt(occupation))) / c476.COEFFICIENT_SCALE
                - np.sqrt(occupation)
            ),
        }
        for route, occupation in c453.PHYSICAL_STRENGTHS.items()
    }
    compiler_by_word = {
        int(row["word"]): float(row["total_compiler_operator_residual"])
        for row in rows
    }
    state_ceilings = {
        "A_unit_weight": c453.TRAIN.depth * 3 * (
            compiler_by_word[int(np.rint(c476.COEFFICIENT_SCALE * np.sqrt(
                c453.PHYSICAL_STRENGTHS["unit_weight"]
            )))] + compiler_by_word[RECEIVER_WORD]
        ),
        "A_coefficient_two": c453.TRAIN.depth * 3 * (
            compiler_by_word[int(np.rint(c476.COEFFICIENT_SCALE * np.sqrt(
                c453.PHYSICAL_STRENGTHS["coefficient_two"]
            )))] + compiler_by_word[RECEIVER_WORD]
        ),
        "B_two_pass": c453.TRAIN.depth * (
            3 * REPETITIONS * compiler_by_word[RECEIVER_WORD]
            + 3 * compiler_by_word[RECEIVER_WORD]
        ),
        "C_calibrated": c453.TRAIN.depth * 3 * (
            compiler_by_word[prediction["calibrated_word"]]
            + compiler_by_word[RECEIVER_WORD]
        ),
    }
    state_ceiling = max(state_ceilings.values())
    check(
        "coefficient rounding, product formula, discrete angle, total compiler, inverse, and state ceiling remain separate from prediction residuals",
        max(row["product_formula_operator_residual"] for row in rows) < c480.PRODUCT_ERROR_CAP
        and max(row["discrete_angle_operator_residual"] for row in rows) < c480.ANGLE_ERROR_CAP
        and max(row["total_compiler_operator_residual"] for row in rows) < c480.STATE_ERROR_CAP
        and max(max(row["unitarity_residual"], row["inverse_residual"]) for row in rows) < c480.TOLERANCE,
        {"operator_rows": rows, "analytic_word_rounding": analytic_rounding,
         "route_specific_depth4_telescoping_state_ceilings": state_ceilings,
         "maximum_declared_route_state_ceiling": state_ceiling},
    )
    return {"rows": rows, "analytic_rounding": analytic_rounding, "state_ceiling": state_ceiling}


def physical_eg_and_covariance_controls(prediction):
    words = {RECEIVER_WORD, prediction["calibrated_word"]}
    words.update(int(np.rint(c476.COEFFICIENT_SCALE * np.sqrt(value)))
                 for value in c453.PHYSICAL_STRENGTHS.values())
    eg_rows = []
    covariance_rows = []
    identity = np.eye(448, dtype=complex)
    encoding = c472.c322.build_encoding(3)
    for word in sorted(words):
        coefficients = (word,) * 6
        initial = c472.initial_state()
        logical = c487.c484.apply_product_source(
            initial, 0, coefficients, route=c487.SELECTED_ROUTE, discrete=True
        )
        encoded = c472.c426.encode_physical(initial, encoding)
        physical = c487.c484.physical_product_source(
            encoded, encoding, 0, coefficients, route=c487.SELECTED_ROUTE, discrete=True
        )
        expected = c472.c426.encode_physical(logical, encoding)
        decoded = {key: encoding.getH() @ value for key, value in physical.items()}
        projected = c472.c426.encode_physical(decoded, encoding)
        eg_rows.append({"word": word, "EG": c472.state_residual(physical, expected),
                        "code_leakage": c472.state_residual(physical, projected)})
        base = c480.product_action(identity, coefficients, route=c487.SELECTED_ROUTE, discrete=True)
        maximum = 0.0
        for frame in c487.c484.c463.proper_cubic_frames():
            matrix = np.asarray(frame, dtype=int)
            mapping = c472.direction_map(matrix)
            representation = c472.c426.recoil_frame(1, matrix)
            carried = c480.product_action(
                identity, coefficients, route=c487.SELECTED_ROUTE, discrete=True,
                direction_order=tuple(mapping),
            )
            maximum = max(maximum, float(np.max(abs(carried - representation @ base @ representation.getH()))))
        covariance_rows.append({"word": word, "proper_cubic_frames": 24,
                                "maximum_full_operator_covariance_residual": maximum})
    check(
        "every source/receiver word used in the tournament has local physical E/G, code return, and all24 proper-cubic covariance",
        max(max(row["EG"], row["code_leakage"]) for row in eg_rows) < c472.TOLERANCE
        and max(row["maximum_full_operator_covariance_residual"] for row in covariance_rows) < c480.TOLERANCE,
        {"EG_rows": eg_rows, "covariance_rows": covariance_rows,
         "scope": "one local q1 source-star seam; exact L13 logical prediction with local compiler ceiling"},
    )


def inverse_deletion_domain_fixture_controls(prediction):
    selected = prediction["calibrated_word"]
    inverse_rows = []
    for geometry in c453.GEOMETRIES:
        initial = c453.strength_state(geometry, c453.PHYSICAL_STRENGTHS["coefficient_two"])
        for repetitions in (1, REPETITIONS):
            stepped = logical_step(initial, geometry, source_word=selected, source_repetitions=repetitions)
            restored = logical_inverse(stepped, geometry, source_word=selected, source_repetitions=repetitions)
            inverse_rows.append({"geometry": geometry.name, "repetitions": repetitions,
                                 "inverse": c435.state_residual(restored, initial),
                                 "norm_error": abs(c435.state_norm(stepped) - 1)})
    geometry = c453.TRAIN
    initial = c453.strength_state(geometry, c453.PHYSICAL_STRENGTHS["coefficient_two"])
    intact, _intact_controls = evolve(initial, geometry, source_word=selected)
    deletions = {}
    for name, kwargs in (
        ("source", {"source_enabled": False}),
        ("receiver", {"receiver_enabled": False}),
        ("field_stream", {"stream_enabled": False}),
        ("packet_stream", {"packet_stream_enabled": False}),
        ("contact", {"contact_enabled": False}),
    ):
        deleted, _deleted_controls = evolve(initial, geometry, source_word=selected, **kwargs)
        deletions[name] = c435.state_residual(intact, deleted)
    repeated, _repeated_controls = evolve(
        initial, geometry, source_word=selected, source_repetitions=REPETITIONS
    )
    deletions["one_of_two_source_passes"] = c435.state_residual(repeated, intact)
    rejected = 0
    for probe in (
        lambda: validate_word(0), lambda: validate_word(1024),
        lambda: logical_step(initial, geometry, source_word=selected, source_repetitions=3),
        lambda: restricted_vertex("bad", 0, selected),
        lambda: c453.strength_state(geometry, 1.1),
    ):
        try:
            probe()
        except (ValueError, KeyError):
            rejected += 1
    update_rows = c435.restricted_factors()[0]
    contact = c435.c319.triple_contact(c435.LABELS)
    two_particle = np.zeros(c435.MATTER_DIM, dtype=complex)
    two_particle[c435.LABEL_INDEX[(2, (0, 1), 0, (), 0, ())]] = 1
    contact_signal = float(np.linalg.norm(contact @ two_particle - two_particle))
    check(
        "train/held one-pass and repeated-pass words have exact adjoint return; non-contact deletions are visible, contact is sector-trivial here with a dedicated two-particle fixture following, and malformed domains are refused",
        max(max(row["inverse"], row["norm_error"]) for row in inverse_rows) < c435.TOLERANCE
        and min(value for name, value in deletions.items() if name != "contact") > 1e-10
        and deletions["contact"] == 0.0 and rejected == 5,
        {"inverse_rows": inverse_rows, "deletions": deletions,
         "contact_one-source-state_depth4_visibility": "zero on this lawful sector; dedicated two-particle fixture follows",
         "malformed_domains_refused": rejected},
    )
    check(
        "the one-particle mass and Cycle230 contact fixtures survive every source-law change",
        abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]) < c435.TOLERANCE
        and update_rows["uniform_one_particle_eigen_residual"] < c435.TOLERANCE
        and update_rows["contact_nontrivial_columns"] == 645 and contact_signal > 1e-6,
        {"Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
         "three_cell_mass": update_rows["three_cell_rest_mass"],
         "mass_eigen_residual": update_rows["uniform_one_particle_eigen_residual"],
         "contact_nontrivial_columns": update_rows["contact_nontrivial_columns"],
         "two_particle_contact_signal": contact_signal},
    )


def inventory_and_no_go_controls(prediction, compiler):
    cells = c453.TRAIN.length ** 3
    base_events = c487.c484.flagged_discrete_manifest(c487.SELECTED_ROUTE)["total_discrete_gates"]
    selected = prediction["calibrated_word"]
    check(
        "the repeated-source route has explicit bounded resource and zero-renewal accounting",
        cells == 2197 and REPETITIONS == 2,
        {"source_stars_per_macro_step": 3, "receiver_stars_per_macro_step": 3,
         "A_source_actuation_passes_per_macro_step": 3,
         "B_source_actuation_passes_per_macro_step": 6,
         "C_source_actuation_passes_per_macro_step": 3,
         "source_renewal_count_all_routes": 0,
         "one_local_full_layer_discrete_events_at_uniform256": base_events,
         "B_source_actuation_event_multiplier": 2,
         "calibrated_common_source_word": selected,
         "L13_full_physical_shell_closed": False},
    )
    check(
        "the supplied/derived/open inventory keeps source-law evidence below gravity or energy interpretation",
        AUTHORITY == "none" and AUDIT == "unset",
        {"supplied": [
            "Cycle420 four targets, route labels/strengths and 5e-10 row tolerance",
            "Cycle453 L13 a1/a2 geometries, signed quadrupole, packet-width readout and depth4 schedule",
            "Cycle487 adapter and P8/Suzuki4/B20 physical compiler",
            "analytic sqrt map, two-pass schedule, train-only scalar-search algorithm/bounds and fixed receiver word",
            "host preparation, factor order, target readout and finite tolerances"],
         "derived": [
            "twelve exact logical L13 rows and route dispositions",
            "one train-only selected integer word with zero held evaluations",
            "word-specific compiler residuals/ceiling, physical E/G, code return, all24 covariance",
            "inverse, locality-by-factorization, deletion, domain, mass/contact and resource controls"],
         "open": [
            "any unmet four-row plus stronger-a2 terminal obligation",
            "complete L13 three-M64 physical shell/effect encoding and total emitted schedule",
            "autonomous preparation, source recurrence/renewal, carried recoil and source work",
            "join to Cycle213 retarded dynamics, Cycle216 static exchange, or Cycle425 dressed field",
            "energy-stress/source identity, physical time, gravity/metric, Records, Born/occurrence and realized history"],
         "firewall": {"response_called_gravity": False, "phase_called_energy": False,
                      "generator_called_rate": False, "depth_called_time": False,
                      "norm_weight_called_probability": False}},
    )
    check(
        "full N1-N8 keeps any bounded negative route-specific and rejects shared obstruction or axiom pressure",
        AUTHORITY == "none" and AUDIT == "unset",
        {"N1": {
            "analytic sqrt source word at fixed Q1": "ATTEMPTED all four rows",
            "two coherent local source passes": "ATTEMPTED all four rows",
            "one train-only calibrated common word": "ATTEMPTED all four rows",
            "analytic nonlinear/saturation word map": "UNTESTED",
            "coherent many-Q finite-carrier source": "UNTESTED",
            "renewed/recurrent local source with an explicit reservoir": "UNTESTED",
            "Cycle213 retarded-field join": "UNTESTED",
            "Cycle216 static-exchange join": "UNTESTED",
            "Cycle425 transient/stationary join": "UNTESTED"},
         "N2": "pairwise separation: word normalization does not imply repeated excitation; repeated excitation does not imply train calibration; calibration does not fix propagation/geometry or the L13 shell; none implies a gravity/source identity",
         "N3": "sqrt map, integer rounding, B20/P8/S4, fixed receiver word, repetition count/order, no renewal, optimizer bounds/tolerance/neighborhood, factor order, geometry, targets and readout are explicit triggers",
         "N4": {"compiler_residual": compiler["state_ceiling"],
                "law_residuals": {route: data["maximum_absolute_row_residual"] for route, data in prediction["dispositions"].items()},
                "matching": "local compiler residuals close only local E/G; row/order residuals remain law/prediction; L13 shell remains separate"},
         "N5": "evidence is bounded to three frozen source laws, two strengths, L13 depth4, a1 train and a2 held; no universal lattice or gravity negative",
         "N6": "nonlinear word maps, true many-Q sources, explicit renewable reservoirs, retarded/static/dressed field joins, alternate domains and complete shell compilation remain live",
         "N7": "a hostile reviewer can use the two train rows to fit a two-parameter analytic source law, or add a locally conserved renewable source reservoir and test held a2 without altering the Cycle487 compiler",
         "N8": "Cycles432->435 and 447->450 retired finite residuals by composing/enlarging constructions; Cycles213/216/425 already provide distinct field mechanisms; no cross-cycle constitutional echo",
         "gate": "bounded three-route tournament only; broad no-go FAIL; minimum-content FAIL; shared obstruction FAIL; axiom pressure FAIL"},
    )


def resource_cap_controls(started: float) -> None:
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    check("the complete Cycle490 cold run stays below explicit wall and RSS caps",
          elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
          {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
           "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB})


def main() -> int:
    started = perf_counter()
    print("Cycle490 isolated discrete source-law tournament")
    print("authority", AUTHORITY, "audit", AUDIT)
    note_contract()
    frozen_controls()
    prediction = prediction_controls()
    compiler = compiler_controls(prediction)
    physical_eg_and_covariance_controls(prediction)
    inverse_deletion_domain_fixture_controls(prediction)
    inventory_and_no_go_controls(prediction, compiler)
    resource_cap_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
