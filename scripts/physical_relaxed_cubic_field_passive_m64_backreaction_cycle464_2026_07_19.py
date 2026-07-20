#!/usr/bin/env python3
"""Cycle 464: relaxed cubic field / passive M64 backreaction probe.

Generate the finite train/held cubic word field with the Cycle-463 reversible
six-neighbour rule, normalize it once into a Q1 M2 source preparation, derive
six directional amplitudes from local neighbour-word differences, and couple
that field reciprocally to a repeated physical M64 one-particle matter code.
Every cell uses the same 42-dimensional local field/matter vertex.  The field
is never refreshed or queried during the update and no host force is applied.

The word-to-amplitude normalization and preparation compiler, mass law,
coupling, packet, boundary, and readout are supplied.  This is not derived
gravity, energy, time, probability, an occurrence, or a Record.  Authority is
none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_dressed_source_corridor_trajectory_cycle447_2026_07_19 as c447
import physical_mass_passive_trajectory_tournament_cycle442_2026_07_19 as c442
import physical_reversible_cubic_relaxation_clock_compiler_cycle463_2026_07_19 as c463
import physical_cubic_shell_relational_interval_field_cycle461_2026_07_19 as c461


c435 = c447.c435
c319 = c447.c319
c210 = c447.c210
c219 = c447.c219

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RELAXED_CUBIC_FIELD_PASSIVE_M64_BACKREACTION_CYCLE464_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

TOLERANCE = 2.0e-10
LOCAL_TOLERANCE = 8.0e-12
SIGNAL_FLOOR = 1.0e-6
BACKREACTION_FLOOR = 1.0e-6
SCHMIDT_TAIL_FLOOR = 1.0e-5
DELETION_VISIBILITY = 1.0e-6
BOUNDARY_MAXIMUM = 0.75
WALL_CAP_SECONDS = 600.0
RSS_CAP_BYTES = 4 * 1024**3
MASS_BETA = float(c442.c441.TARGET_BETAS[1])
MASS_COORDINATE = float(-3 * np.tan(MASS_BETA / 2))
DIRECTIONS = np.asarray(c210.DIRECTIONS, dtype=int)


@dataclass(frozen=True)
class Geometry:
    name: str
    field_radius: int
    matter_radius: int
    depth: int
    held: bool


TRAIN = Geometry("train-R1-padR2-D4", 1, 2, 4, False)
HELD = Geometry("held-R2-padR3-D6", 2, 3, 6, True)
GEOMETRIES = (TRAIN, HELD)


class WallCapExceeded(RuntimeError):
    pass


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


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "cycle463 locally relaxed word field",
        "cycle461 is comparator only",
        "train r1/padr2/depth4",
        "held r2/padr3/depth6",
        "same 42-dimensional local vertex",
        "actual repeated physical m64",
        "no host per-step force or control",
        "no source refresh",
        "neighbor-word positive differences",
        "word-to-q1 normalization and amplitude-preparation compiler are supplied",
        "supplied force-like control",
        "not derived gravity",
        "physical -delta response",
        "rho_psi=|psi|^2/local mass source",
        "bounded passive response/backreaction",
        "all 24 proper-cubic frames",
        "600-second wall cap",
        "4 gib rss cap",
        "partial-attempt-with-named-untested-routes",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
        "no gravity, no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle464 note freezes the passive-response/backreaction contract", not missing, missing)


def validate_geometry(geometry: Geometry) -> None:
    if geometry not in GEOMETRIES:
        raise ValueError("geometry leaves the frozen train/held family")
    if geometry.matter_radius != geometry.field_radius + 1:
        raise ValueError("geometry lacks the frozen one-shell padding")
    if geometry.depth != 2 * geometry.field_radius + 2:
        raise ValueError("geometry lacks its frozen trajectory depth")


def generated_word_field(geometry: Geometry) -> dict[str, object]:
    """Consume Cycle463 by its executable map, never by copied result rows."""

    validate_geometry(geometry)
    item = c463.domain(geometry.field_radius)
    initial = c463.encode(c463.initial_coarse(item), item)
    physical = c463.physical_forward(initial, item)
    restored = c463.physical_forward(physical, item, reverse=True)
    values = c463.history_values(physical, c463.ITERATIONS)
    profile = {
        coord: Fraction(values[index], c463.DENOMINATOR)
        for index, coord in enumerate(item.active)
    }
    summary = c463.residual_summary(values, item)
    digest = sha256(
        "\n".join(f"{coord}:{values[index]}" for index, coord in enumerate(item.active)).encode()
    ).hexdigest()
    return {
        "domain": item,
        "initial": initial,
        "physical": physical,
        "restored": restored,
        "values": values,
        "profile": profile,
        "summary": summary,
        "digest": digest,
        "total_word_field": sum(profile.values(), Fraction()),
    }


def local_direction_weights(profile: dict[tuple[int, int, int], Fraction], coord):
    """Cubic-covariant inward lift derived from six local word differences."""

    center = profile[coord]
    differences = []
    for direction in DIRECTIONS:
        neighbor = tuple(int(value) for value in np.asarray(coord) + direction)
        differences.append(max(profile.get(neighbor, Fraction()) - center, Fraction()))
    total = sum(differences, Fraction())
    if total == 0:
        return np.full(6, 1 / 6, dtype=float), tuple(differences), "zero-gradient uniform"
    return (
        np.asarray([float(value / total) for value in differences]),
        tuple(differences),
        "positive-neighbor differences",
    )


def cubic_layout(geometry: Geometry) -> dict[str, object]:
    word = generated_word_field(geometry)
    coordinates = tuple(c463.cube(geometry.matter_radius))
    index = {coord: position for position, coord in enumerate(coordinates)}
    sites = len(coordinates)
    field_dimension = 1 + 7 * sites
    matter_dimension = 6 * sites
    total = word["total_word_field"]
    if total <= 0:
        raise ValueError("relaxed word field has no positive Q1 normalization")
    field = np.zeros(field_dimension, dtype=complex)
    direction_rows = {}
    for coord, value in word["profile"].items():
        direction_weight, differences, rule = local_direction_weights(word["profile"], coord)
        site_weight = float(value / total)
        start = 1 + 7 * index[coord]
        field[start + 1 : start + 7] = np.sqrt(site_weight * direction_weight)
        direction_rows[coord] = {
            "word": value,
            "site_Q1_weight": site_weight,
            "neighbor_positive_differences": differences,
            "direction_weights": tuple(float(value) for value in direction_weight),
            "rule": rule,
        }

    matter = np.zeros(matter_dimension, dtype=complex)
    initial_cell = (geometry.field_radius, 0, 0)
    inward_direction = int(np.where(np.all(DIRECTIONS == np.asarray((-1, 0, 0)), axis=1))[0][0])
    matter[6 * index[initial_cell] + inward_direction] = 1

    stream = np.empty(matter_dimension, dtype=int)
    for coord, source_index in index.items():
        for direction_index, direction in enumerate(DIRECTIONS):
            target = tuple(int(value) for value in np.asarray(coord) + direction)
            target_direction = direction_index
            if target not in index:
                target = coord
                target_direction = direction_index ^ 1
            stream[6 * source_index + direction_index] = 6 * index[target] + target_direction
    if len(set(int(value) for value in stream)) != matter_dimension:
        raise RuntimeError("reflecting matter stream is not a permutation")
    return {
        "geometry": geometry,
        "word": word,
        "coordinates": coordinates,
        "index": index,
        "sites": sites,
        "field_dimension": field_dimension,
        "matter_dimension": matter_dimension,
        "field": field,
        "matter": matter,
        "stream": stream,
        "inverse_stream": np.argsort(stream),
        "direction_rows": direction_rows,
        "initial_cell": initial_cell,
        "inward_direction": inward_direction,
        "physical_M2": 13 * sites,
    }


def field_matter_vertex() -> np.ndarray:
    return c447.local_test_vertex(round(MASS_COORDINATE, 13))


def apply_matter_coin(state: np.ndarray, layout, *, inverse: bool = False) -> np.ndarray:
    coin = c219.common_species(MASS_BETA).coin
    if inverse:
        coin = coin.conj().T
    return np.einsum(
        "fnd,ed->fne",
        state.reshape(layout["field_dimension"], layout["sites"], 6),
        coin,
        optimize=True,
    ).reshape(state.shape)


def apply_vertices(
    state: np.ndarray,
    layout,
    *,
    inverse: bool = False,
    enabled: bool = True,
    deleted_cell: tuple[int, int, int] | None = None,
) -> np.ndarray:
    if not enabled:
        return state.copy()
    output = state.copy()
    operator = field_matter_vertex()
    if inverse:
        operator = operator.conj().T
    cells = reversed(layout["coordinates"]) if inverse else layout["coordinates"]
    for coord in cells:
        if coord == deleted_cell:
            continue
        cell = layout["index"][coord]
        field_indices = tuple(range(1 + 7 * cell, 1 + 7 * cell + 7))
        matter_indices = tuple(range(6 * cell, 6 * cell + 6))
        packed = output[np.ix_(field_indices, matter_indices)].T.reshape(-1)
        output[np.ix_(field_indices, matter_indices)] = (operator @ packed).reshape(6, 7).T
    return output


def apply_stream(state: np.ndarray, layout, *, inverse: bool = False) -> np.ndarray:
    permutation = layout["inverse_stream"] if inverse else layout["stream"]
    output = np.empty_like(state)
    output[:, permutation] = state
    return output


def apply_free_matter(matter: np.ndarray, layout, *, coin_enabled=True, stream_enabled=True):
    output = matter.copy()
    if coin_enabled:
        output = np.einsum(
            "nd,ed->ne",
            output.reshape(layout["sites"], 6),
            c219.common_species(MASS_BETA).coin,
            optimize=True,
        ).reshape(-1)
    if stream_enabled:
        streamed = np.empty_like(output)
        streamed[layout["stream"]] = output
        output = streamed
    return output


def joint_step(
    state: np.ndarray,
    layout,
    *,
    coupling_enabled=True,
    coin_enabled=True,
    stream_enabled=True,
    deleted_cell=None,
) -> np.ndarray:
    output = apply_matter_coin(state, layout) if coin_enabled else state.copy()
    output = apply_vertices(output, layout, enabled=coupling_enabled, deleted_cell=deleted_cell)
    return apply_stream(output, layout) if stream_enabled else output


def joint_inverse(state: np.ndarray, layout) -> np.ndarray:
    output = apply_stream(state, layout, inverse=True)
    output = apply_vertices(output, layout, inverse=True)
    return apply_matter_coin(output, layout, inverse=True)


def matter_observables(state: np.ndarray, layout) -> dict[str, float]:
    weights = np.sum(np.abs(state) ** 2, axis=0)
    coordinate_x = np.repeat([coord[0] for coord in layout["coordinates"]], 6)
    radial_second = np.repeat([sum(value * value for value in coord) for coord in layout["coordinates"]], 6)
    boundary = np.repeat(
        [int(any(abs(value) == layout["geometry"].matter_radius for value in coord)) for coord in layout["coordinates"]],
        6,
    )
    return {
        "norm": float(np.sum(weights)),
        "centroid_x": float(weights @ coordinate_x),
        "radial_second": float(weights @ radial_second),
        "boundary_weight": float(weights @ boundary),
    }


def leading_schmidt_tail(state: np.ndarray, seed: np.ndarray, iterations: int = 12) -> float:
    vector = seed / np.linalg.norm(seed)
    for _ in range(iterations):
        field_vector = state @ vector
        vector = state.conj().T @ field_vector
        norm = np.linalg.norm(vector)
        if norm == 0:
            return 0.0
        vector /= norm
    largest_squared = float(np.linalg.norm(state @ vector) ** 2)
    return math.sqrt(max(0.0, 1 - min(1.0, largest_squared)))


def run_trace(
    layout,
    *,
    field_override: np.ndarray | None = None,
    coupling_enabled=True,
    coin_enabled=True,
    stream_enabled=True,
    deleted_cell=None,
) -> dict[str, object]:
    field = layout["field"] if field_override is None else field_override
    state = np.outer(field, layout["matter"])
    initial = state.copy()
    free = layout["matter"].copy()
    initial_field_weights = np.sum(np.abs(state) ** 2, axis=1)
    rows = []
    for tick in range(layout["geometry"].depth + 1):
        interacting = matter_observables(state, layout)
        free_state = np.outer(np.asarray((1.0,), dtype=complex), free)
        free_observable = matter_observables(free_state, layout)
        rows.append(
            {
                "tick": tick,
                "delta_centroid_x": interacting["centroid_x"] - free_observable["centroid_x"],
                "delta_radial_second": interacting["radial_second"] - free_observable["radial_second"],
                "joint_norm_error": abs(interacting["norm"] - 1),
                "boundary_weight": interacting["boundary_weight"],
            }
        )
        if tick < layout["geometry"].depth:
            state = joint_step(
                state,
                layout,
                coupling_enabled=coupling_enabled,
                coin_enabled=coin_enabled,
                stream_enabled=stream_enabled,
                deleted_cell=deleted_cell,
            )
            free = apply_free_matter(
                free, layout, coin_enabled=coin_enabled, stream_enabled=stream_enabled
            )
    final_field_weights = np.sum(np.abs(state) ** 2, axis=1)
    uncoupled_product = np.outer(field, free)
    first = joint_step(initial, layout)
    restored = joint_inverse(first, layout)
    return {
        "rows": rows,
        "final_state": state,
        "free_matter": free,
        "maximum_abs_centroid_response": max(abs(row["delta_centroid_x"]) for row in rows),
        "maximum_abs_radial_response": max(abs(row["delta_radial_second"]) for row in rows),
        "maximum_norm_error": max(row["joint_norm_error"] for row in rows),
        "maximum_boundary_weight_after_initial": max(row["boundary_weight"] for row in rows[1:]),
        "field_weight_backreaction": float(np.linalg.norm(final_field_weights - initial_field_weights)),
        "joint_product_residual": float(np.linalg.norm(state - uncoupled_product)),
        "Schmidt_tail": leading_schmidt_tail(state, free),
        "one_step_inverse_residual": float(np.linalg.norm(restored - initial)),
        "source_refresh_count": 0,
        "host_per_step_force_or_control_count": 0,
        "expectation_feedback_count": 0,
    }


def generation_and_direction_controls() -> dict[int, dict[str, object]]:
    print("\nCYCLE463 GENERATED WORD FIELD / LOCAL DIRECTION LIFT")
    layouts = {geometry.field_radius: cubic_layout(geometry) for geometry in GEOMETRIES}
    rows = []
    for geometry in GEOMETRIES:
        layout = layouts[geometry.field_radius]
        word = layout["word"]
        profile_norm = float(np.linalg.norm(layout["field"]))
        maximum_direction_sum = max(
            abs(sum(row["direction_weights"]) - 1) for row in layout["direction_rows"].values()
        )
        rows.append(
            {
                "geometry": geometry.name,
                "word_digest": word["digest"],
                "active_sites": len(word["profile"]),
                "matter_sites": layout["sites"],
                "total_word_field": float(word["total_word_field"]),
                "max_nonsource_residual": float(word["summary"]["max_nonsource"]),
                "source_defect_residual": float(word["summary"]["source_defect_residual"]),
                "upstream_inverse_exact": word["restored"] == word["initial"],
                "Q1_norm_error": abs(profile_norm - 1),
                "maximum_direction_sum_residual": maximum_direction_sum,
                "zero_gradient_sites": sum(
                    row["rule"] == "zero-gradient uniform" for row in layout["direction_rows"].values()
                ),
            }
        )
    check(
        "the frozen Cycle463 local rule generates train/held words and the neighbor-word rule gives normalized Q1 directions without a profile table",
        all(
            row["upstream_inverse_exact"]
            and row["max_nonsource_residual"] < float(c463.RESIDUAL_THRESHOLD)
            and row["source_defect_residual"] < float(c463.RESIDUAL_THRESHOLD)
            and row["Q1_norm_error"] < TOLERANCE
            and row["maximum_direction_sum_residual"] < TOLERANCE
            for row in rows
        ),
        {
            "rows": rows,
            "direction_rule": "positive differences of six final local neighbor words; uniform only at exact zero gradient",
            "Cycle461_role": "comparator only; its supplied orbit table is not consumed by the update",
            "word_to_Q1_normalization_supplied": True,
            "amplitude_preparation_compiler_supplied": True,
        },
    )
    return layouts


def local_physical_compiler_controls() -> dict[str, float]:
    print("\nLOCAL M2 / M64 COMPILER")
    field_encoding = np.zeros((2**7, 7), dtype=complex)
    field_encoding[0, 0] = 1
    for direction in range(6):
        field_encoding[1 << direction, direction + 1] = 1
    matter_encoding = np.zeros((2**6, 6), dtype=complex)
    for direction in range(6):
        matter_encoding[1 << direction, direction] = 1
    encoding = np.kron(matter_encoding, field_encoding)
    logical = field_matter_vertex()
    sample = np.arange(1, 43, dtype=complex) + 1j * np.arange(42, 0, -1, dtype=complex)
    sample /= np.linalg.norm(sample)
    physical_sample = encoding @ sample

    def physical_action(vector, *, inverse=False):
        compressed = encoding.conj().T @ vector
        projected = encoding @ compressed
        operator = logical.conj().T if inverse else logical
        return encoding @ (operator @ compressed) + vector - projected

    output = physical_action(physical_sample)
    expected = encoding @ (logical @ sample)
    restored = physical_action(output, inverse=True)
    projector_coefficients = encoding.conj().T @ output
    rows = {
        "field_Gram": float(np.linalg.norm(field_encoding.conj().T @ field_encoding - np.eye(7))),
        "matter_Gram": float(np.linalg.norm(matter_encoding.conj().T @ matter_encoding - np.eye(6))),
        "joint_Gram": float(np.linalg.norm(encoding.conj().T @ encoding - np.eye(42))),
        "EG": float(np.linalg.norm(output - expected)),
        "inverse": float(np.linalg.norm(restored - physical_sample)),
        "leakage": float(np.linalg.norm(output - encoding @ projector_coefficients)),
        "logical_unitarity": float(np.linalg.norm(logical.conj().T @ logical - np.eye(42))),
    }
    check(
        "one identical 13-M2 field/M64 vertex has exact E/G, inverse, Gram, leakage, and identity completion",
        max(rows.values()) < LOCAL_TOLERANCE,
        {
            **rows,
            "field_M2_per_cell": 7,
            "matter_M2_per_cell": 6,
            "maximum_local_support_M2": 13,
            "matter_code": "one-particle sector of one repeated physical M64 cell",
        },
    )
    return rows


def passive_response_controls(layouts) -> dict[int, dict[str, object]]:
    print("\nPASSIVE M64 RESPONSE / RECIPROCAL BACKREACTION")
    results = {}
    rows = []
    for geometry in GEOMETRIES:
        layout = layouts[geometry.field_radius]
        result = run_trace(layout)
        results[geometry.field_radius] = result
        row = {
            "geometry": geometry.name,
            "held": geometry.held,
            "physical_M2": layout["physical_M2"],
            "final": result["rows"][-1],
            "maximum_abs_centroid_response": result["maximum_abs_centroid_response"],
            "maximum_abs_radial_response": result["maximum_abs_radial_response"],
            "field_weight_backreaction": result["field_weight_backreaction"],
            "joint_product_residual": result["joint_product_residual"],
            "Schmidt_tail": result["Schmidt_tail"],
            "one_step_inverse_residual": result["one_step_inverse_residual"],
            "maximum_norm_error": result["maximum_norm_error"],
            "maximum_boundary_weight_after_initial": result["maximum_boundary_weight_after_initial"],
            "source_refresh_count": result["source_refresh_count"],
            "host_per_step_force_or_control_count": result["host_per_step_force_or_control_count"],
            "expectation_feedback_count": result["expectation_feedback_count"],
            "trace": result["rows"],
        }
        rows.append(row)
    check(
        "the same reciprocal local law gives visible train and no-refit held passive response/backreaction with norm, inverse, boundary, and no-control closure",
        all(
            max(row["maximum_abs_centroid_response"], row["maximum_abs_radial_response"]) > SIGNAL_FLOOR
            and row["field_weight_backreaction"] > BACKREACTION_FLOOR
            and row["joint_product_residual"] > SCHMIDT_TAIL_FLOOR
            and row["Schmidt_tail"] > SCHMIDT_TAIL_FLOOR
            and row["one_step_inverse_residual"] < TOLERANCE
            and row["maximum_norm_error"] < TOLERANCE
            and row["maximum_boundary_weight_after_initial"] < BOUNDARY_MAXIMUM
            and row["source_refresh_count"] == 0
            and row["host_per_step_force_or_control_count"] == 0
            and row["expectation_feedback_count"] == 0
            for row in rows
        ),
        {
            "rows": rows,
            "fit_parameters": 0,
            "held_refits": 0,
            "same_mass_beta": MASS_BETA,
            "same_mass_coordinate": MASS_COORDINATE,
            "same_local_vertex": True,
        },
    )
    return results


def uniform_direction_field(layout) -> np.ndarray:
    field = np.zeros_like(layout["field"])
    total = layout["word"]["total_word_field"]
    for coord, value in layout["word"]["profile"].items():
        start = 1 + 7 * layout["index"][coord]
        field[start + 1 : start + 7] = math.sqrt(float(value / total) / 6)
    return field


def deletion_controls(layouts, intact) -> None:
    print("\nDELETIONS")
    layout = layouts[TRAIN.field_radius]
    vacuum = np.zeros_like(layout["field"])
    vacuum[0] = 1
    source_deleted = run_trace(layout, field_override=vacuum)
    coupling_deleted = run_trace(layout, coupling_enabled=False)
    direction_deleted = run_trace(layout, field_override=uniform_direction_field(layout))
    coin_deleted = run_trace(layout, coin_enabled=False)
    stream_deleted = run_trace(layout, stream_enabled=False)
    vertex_deleted = run_trace(layout, deleted_cell=layout["initial_cell"])
    baseline = intact[TRAIN.field_radius]
    baseline_trace = np.asarray(
        [(row["delta_centroid_x"], row["delta_radial_second"]) for row in baseline["rows"]]
    )

    def trace_residual(candidate):
        values = np.asarray(
            [(row["delta_centroid_x"], row["delta_radial_second"]) for row in candidate["rows"]]
        )
        return float(np.linalg.norm(values - baseline_trace))

    rows = {
        "source": {
            "max_response": max(source_deleted["maximum_abs_centroid_response"], source_deleted["maximum_abs_radial_response"]),
            "backreaction": source_deleted["field_weight_backreaction"],
        },
        "coupling": {
            "max_response": max(coupling_deleted["maximum_abs_centroid_response"], coupling_deleted["maximum_abs_radial_response"]),
            "backreaction": coupling_deleted["field_weight_backreaction"],
        },
        "direction_lift_trace_residual": trace_residual(direction_deleted),
        "mass_coin_trace_residual": trace_residual(coin_deleted),
        "matter_stream_trace_residual": trace_residual(stream_deleted),
        "initial_cell_vertex_trace_residual": trace_residual(vertex_deleted),
    }
    check(
        "source/profile, reciprocal coupling, local direction lift, mass coin, matter stream, and one local vertex deletions have distinct effects",
        rows["source"]["max_response"] < TOLERANCE
        and rows["coupling"]["max_response"] < TOLERANCE
        and rows["source"]["backreaction"] < TOLERANCE
        and rows["coupling"]["backreaction"] < TOLERANCE
        and rows["direction_lift_trace_residual"] > DELETION_VISIBILITY
        and rows["mass_coin_trace_residual"] > DELETION_VISIBILITY
        and rows["matter_stream_trace_residual"] > DELETION_VISIBILITY
        and rows["initial_cell_vertex_trace_residual"] > DELETION_VISIBILITY,
        rows,
    )


def covariance_mass_contact_controls(layouts) -> None:
    print("\nALL-24 / MASS / CONTACT")
    frames = c463.proper_cubic_frames()
    maximum_profile_residual = 0.0
    maximum_direction_residual = 0.0
    maximum_stream_residual = 0.0
    for layout in layouts.values():
        profile = layout["word"]["profile"]
        for frame in frames:
            matrix = np.asarray(frame, dtype=int).T
            direction_map = []
            for direction in DIRECTIONS:
                mapped = matrix @ direction
                direction_map.append(int(np.where(np.all(DIRECTIONS == mapped, axis=1))[0][0]))
            for coord, value in profile.items():
                mapped_coord = tuple(int(item) for item in matrix @ np.asarray(coord))
                maximum_profile_residual = max(
                    maximum_profile_residual, abs(float(value - profile[mapped_coord]))
                )
                source_weights = layout["direction_rows"][coord]["direction_weights"]
                target_weights = layout["direction_rows"][mapped_coord]["direction_weights"]
                maximum_direction_residual = max(
                    maximum_direction_residual,
                    max(abs(source_weights[index] - target_weights[direction_map[index]]) for index in range(6)),
                )
            for source, target in enumerate(layout["stream"]):
                source_cell, _source_direction = divmod(source, 6)
                target_cell, _target_direction = divmod(int(target), 6)
                left = np.asarray(layout["coordinates"][source_cell])
                right = np.asarray(layout["coordinates"][target_cell])
                distance = int(np.sum(np.abs(matrix @ (right - left))))
                maximum_stream_residual = max(maximum_stream_residual, max(0, distance - 1))
    check(
        "the generated profile, neighbor-derived directional lift, reflecting NN stream, and identical vertex transport through all 24 proper-cubic frames",
        len(frames) == 24
        and maximum_profile_residual < TOLERANCE
        and maximum_direction_residual < TOLERANCE
        and maximum_stream_residual == 0,
        {
            "proper_cubic_frames": len(frames),
            "maximum_profile_residual": maximum_profile_residual,
            "maximum_direction_residual": maximum_direction_residual,
            "nonlocal_stream_supports": maximum_stream_residual,
        },
    )

    c435.PASS = c435.FAIL = 0
    c435.covariance_controls()
    update_rows = c435.restricted_factors()[0]
    contact = c319.triple_contact(c435.LABELS)
    two_particle = np.zeros(c435.MATTER_DIM, dtype=complex)
    two_particle[c435.LABEL_INDEX[(2, (0, 1), 0, (), 0, ())]] = 1
    contact_residual = float(np.linalg.norm(contact @ two_particle - two_particle))
    check(
        "the cubic passive-response route preserves the distinct Cycle442 common mass coordinate, inherited Cycle219 rest-mass fixture, all-24 family, and Cycle230 contact",
        c435.PASS == 1
        and c435.FAIL == 0
        and abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]) < TOLERANCE
        and abs(MASS_COORDINATE - float(-3 * np.tan(c442.c441.TARGET_BETAS[1] / 2))) < TOLERANCE
        and update_rows["uniform_one_particle_eigen_residual"] < TOLERANCE
        and update_rows["contact_nontrivial_columns"] == 645
        and contact_residual > 1e-6,
        {
            "Cycle219_three_cell_rest_mass_fixture": update_rows["Cycle219_mass_fixture"],
            "Cycle442_selected_common_mass_coordinate": MASS_COORDINATE,
            "fixtures_intentionally_not_identified": True,
            "mass_eigen_residual": update_rows["uniform_one_particle_eigen_residual"],
            "contact_nontrivial_columns": update_rows["contact_nontrivial_columns"],
            "two_particle_contact_residual": contact_residual,
        },
    )


def domain_resource_ledger_controls(started, layouts, results) -> None:
    print("\nDOMAIN / RESOURCES / WEAK-FIELD LEDGER")
    rejected = 0
    for probe in (
        lambda: validate_geometry(Geometry("bad", 1, 3, 4, False)),
        lambda: validate_geometry(Geometry("bad", 3, 4, 8, True)),
        lambda: c463.domain(3),
        lambda: c447.local_test_vertex(float("nan")),
    ):
        try:
            probe()
        except ValueError:
            rejected += 1
    check("geometry, radius, source, and mass domains reject malformed inputs", rejected == 4, rejected)
    elapsed = time.monotonic() - started
    maxrss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    maximum_state_bytes = max(
        result["final_state"].nbytes for result in results.values()
    )
    check(
        "the imported generation plus passive evolution stay below explicit wall, RSS, state, and support caps",
        elapsed < WALL_CAP_SECONDS
        and maxrss < RSS_CAP_BYTES
        and maximum_state_bytes < RSS_CAP_BYTES
        and max(layout["physical_M2"] for layout in layouts.values()) == 4459,
        {
            "elapsed_seconds_including_Cycle463_generation": elapsed,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "raw_maxrss_Darwin_bytes": maxrss,
            "RSS_cap_bytes": RSS_CAP_BYTES,
            "maximum_dense_joint_state_bytes": maximum_state_bytes,
            "maximum_physical_M2": max(layout["physical_M2"] for layout in layouts.values()),
            "maximum_local_vertex_support_M2": 13,
        },
    )
    check(
        "the three-part weak-field boundary closes only a bounded passive-response/backreaction fixture",
        all(result["field_weight_backreaction"] > BACKREACTION_FLOOR for result in results.values()),
        {
            "physical_minus_Delta_response": "finite reversible word-block response/profile-table import closes on declared domains; physical -Delta law and primitive arithmetic trace remain supplied/open",
            "rho_psi_equals_abs_psi_squared_local_mass_source": "not constructed; central source is a supplied bit and Q1 normalization is supplied",
            "passive_test_matter_response": "bounded train/held M64 response and reciprocal field-weight change close for this supplied coupling",
            "Cycle442_comparison": "does not repeat its sustained-acceleration claim; Cycle464 tests a short cubic response/backreaction fixture",
            "source_profile": "Cycle463 96-layer local word rule",
            "Q1_normalization": "supplied global word-to-amplitude normalization",
            "direction_control": "derived local positive neighbor-word differences; preparation circuit supplied",
            "receiver": "M64 one-particle centroid/radial-second and field-weight diagnostics",
            "calibration": "Cycle442 common passive mass coordinate and SOURCE_SCALE=0.05 supplied; Cycle219 three-cell rest fixture retained separately",
            "refresh": 0,
            "trajectory": "supplied initial cell, inward direction, reflecting shell, depth, coordinates",
            "force_like_control": "compiled directional Q1 preparation; supplied candidate, not derived gravity",
            "C_ref": "open: normalization, preparation, mass/coupling, packet, boundary, and readout supplied",
            "C_num": "bounded train/held response and reciprocal backreaction positive",
            "C_wrap": "open: phase is not energy and update count is not time",
            "C_int": "partial: identical reciprocal vertex executes; law selection/calibration open",
            "C_local": "bounded 13-M2 vertex and repeated M64/Q1 sectors; scalable preparation open",
            "C_source": "open: no rho_psi/mass/energy-stress source law or recurrence",
        },
    )


def _wall_alarm(_signum, _frame):
    raise WallCapExceeded(f"Cycle464 exceeded its {WALL_CAP_SECONDS:g}-second wall cap")


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    signal.signal(signal.SIGALRM, _wall_alarm)
    signal.setitimer(signal.ITIMER_REAL, WALL_CAP_SECONDS)
    print("=" * 96)
    print("CYCLE 464 — RELAXED CUBIC FIELD / PASSIVE M64 BACKREACTION")
    print("=" * 96)
    print(
        {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "RSS_cap_bytes": RSS_CAP_BYTES,
            "signal_floor": SIGNAL_FLOOR,
            "backreaction_floor": BACKREACTION_FLOOR,
            "Schmidt_tail_floor": SCHMIDT_TAIL_FLOOR,
            "boundary_maximum": BOUNDARY_MAXIMUM,
        }
    )
    try:
        note_contract()
        layouts = generation_and_direction_controls()
        local_physical_compiler_controls()
        results = passive_response_controls(layouts)
        deletion_controls(layouts, results)
        covariance_mass_contact_controls(layouts)
        domain_resource_ledger_controls(started, layouts, results)
    except WallCapExceeded as error:
        check("the Cycle464 runner remains inside its predeclared wall cap", False, str(error))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL:
        print("RESULT PHYSICAL_RELAXED_CUBIC_FIELD_PASSIVE_M64_BACKREACTION_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_RELAXED_CUBIC_FIELD_PASSIVE_M64_BACKREACTION_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
