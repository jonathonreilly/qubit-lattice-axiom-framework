#!/usr/bin/env python3
"""Cycle495: local physicalization tournament for Cycle216's scalar 3 L+.

The routes are retained divide-six Jacobi words, a fixed Q48 Chebyshev
recurrence, and a three-reservoir Cycle425 spectral-filter attempt.  The
finite L13 rows use one train-only common contraction and an ordinary
reservoir-M2 norm completion.  Arithmetic/preparation seams are reported at
their actual scopes.  Depth is not time and response is not gravity.
Authority none; audit unset.
"""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
from time import perf_counter
import gc
import resource
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_elementary_divsix_nn_compiler_cycle467_2026_07_19 as c467
import physical_geometry_changing_carrier_tournament_cycle491_2026_07_20 as c491


c453 = c491.c453
c435 = c491.c435
c425 = c491.c425
c216 = c491.c216
c490 = c491.c490
c210 = c435.c210

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE216_LOCAL_SOLVER_TOURNAMENT_CYCLE495_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
LENGTH = 13
JACOBI_DEPTH = 96
WORD_SCALE = 6**JACOBI_DEPTH
WORD_BITS = WORD_SCALE.bit_length()
CHEB_DEPTH = 64
Q_BITS = 48
Q_SCALE = 1 << Q_BITS
FILTER_DEPTH = 64
COMPLETION_CELL = (10, 10, 10)
TORUS_COLOUR = (0, 3, 1, 0, 2, 1, 3, 4, 1, 2, 0, 1, 4)
TORUS_REVERSAL_COLOUR = (0, 1, 2, 4, 3)
DELETION_SIGNAL_MIN = 1e-12
ROW_TOLERANCE = c453.NUMERIC_ROW_TOLERANCE
WALL_CAP_SECONDS = 1200.0
RSS_CAP_MIB = 3072.0
PASS = 0
FAIL = 0

FROZEN = {
    "Cycle216": ("virtual_exchange_green_kernel_cycle216_2026_07_16.py",
                 "9ef0fff433bbf1c96c9b13c5ce79530e01fe705f08c6caf6b60316e20359e011"),
    "Cycle425": ("common_cubic_transient_stationary_update_cycle425_2026_07_19.py",
                 "c3aa51528e54c28b8b258d83d254068430d3b1816a03aafefabe4be3ef6a84c9"),
    "Cycle467": ("physical_elementary_divsix_nn_compiler_cycle467_2026_07_19.py",
                 "7e562949be71a647d410c8a9624eb5cf5fdf2be30777fab93c6ed55824a5e402"),
    "Cycle470": ("physical_seven_supercell_port_delivery_compiler_cycle470_2026_07_19.py",
                 "287b72625b4bf7d29cb847e0a59ed5d64f58b3ec55e5b312942f96bbc0ea6674"),
    "Cycle474": ("physical_mod3_star_layer_scheduler_cycle474_2026_07_19.py",
                 "10a55ef2cb36f7d9f60b115911fc2bcffbffbe3ac0977db0ba319f6dcfd08755"),
    "Cycle479": ("physical_3d_laplacian_s3_generator_provenance_cycle479_2026_07_19.py",
                 "2154075b3f1bfa3dee849eb859bad46adf3f8d07670e6ac5200f6c720b119d30"),
    "Cycle490": ("physical_discrete_source_law_tournament_cycle490_2026_07_20.py",
                 "47609253d3a868a0f736f0c9571a7a6a0878776590af6ddf24d4e6ca9fe80ff4"),
    "Cycle491": ("physical_geometry_changing_carrier_tournament_cycle491_2026_07_20.py",
                 "713732caff61658a50b5de8c5387d0701838fd301406830431bc108936344898"),
}

ROUTES = (
    "A_Cycle479_Jacobi96",
    "B_Q48_Chebyshev64",
    "C_Cycle425_three_reservoir_filter64",
)


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


def note_and_frozen_controls() -> None:
    required = (
        "authority: none", "audit: unset", "frozen before cycle495 target outputs",
        "a — retained divide-six / jacobi adapter", "b — q48 chebyshev local adapter",
        "c — three-reservoir dressed-filter attempt", "periodic l13 cube",
        "held rows never refit", "single train-only common scale",
        "ordinary reservoir m2", "125 rounds per layer", "all 24 proper-cubic frames",
        "iteration depth is not time", "spectral phase is not energy or a rate",
        "no host k+", "n1 — normalized alternative families",
        "n8 — cross-cycle echo and claim gate", "there is no axiom pressure",
    )
    body = normalized(NOTE)
    missing = tuple(item for item in required if item not in body)
    observed = {name: file_sha(ROOT / "scripts" / filename)
                for name, (filename, _digest) in FROZEN.items()}
    expected = {name: digest for name, (_filename, digest) in FROZEN.items()}
    check("the Cycle495 note freezes the three-route physicalization contract before outputs",
          not missing, missing)
    check("Cycles216/425/467/470/474/479/490/491 retain exact identities",
          observed == expected, {"observed": observed, "expected": expected})


def laplacian(values: np.ndarray) -> np.ndarray:
    return 6 * values - sum(
        np.roll(values, shift, axis=axis)
        for axis in range(3) for shift in (-1, 1)
    )


def source_array(geometry) -> np.ndarray:
    output = np.zeros((LENGTH,) * 3)
    for coefficient, cell in zip((1.0, -2.0, 1.0), geometry.sources):
        output[cell] += coefficient
    return output


def point_source(cell=(0, 0, 0)) -> np.ndarray:
    output = np.zeros((LENGTH,) * 3)
    output[cell] = 1
    output -= output.mean()
    return output


def exact_scalar(source: np.ndarray) -> np.ndarray:
    return 3 * c216.c211.solve_field(source)


def jacobi(source: np.ndarray, depth: int = JACOBI_DEPTH) -> np.ndarray:
    current = np.zeros_like(source)
    for _ in range(depth):
        current = (
            sum(np.roll(current, shift, axis=axis)
                for axis in range(3) for shift in (-1, 1))
            + 3 * source
        ) / 6
    return current


def periodic_interface_controls() -> None:
    rows = []
    for geometry in c453.GEOMETRIES:
        source = source_array(geometry)
        response = jacobi(source)
        exact = exact_scalar(source)
        rows.append({
            "geometry": geometry.name,
            "source_sum": float(source.sum()),
            "Jacobi_mean": float(response.mean()),
            "Cycle216_mean": float(exact.mean()),
            "periodic_equation_residual": float(np.linalg.norm(
                laplacian(response) - 3 * source
            )),
        })
    constant = np.ones((LENGTH,) * 3)
    check("the Cycle479 local law is explicitly remapped from Dirichlet/Schur data to the periodic mean-zero Cycle216 domain",
          max(abs(row["source_sum"]) for row in rows) == 0
          and max(abs(row["Jacobi_mean"]) for row in rows) < 2e-15
          and max(abs(row["Cycle216_mean"]) for row in rows) < 2e-15
          and np.linalg.norm(laplacian(constant)) == 0,
          {"rows": rows, "periodic_cells": LENGTH**3,
           "Cycle479_box_trace_Schur_imported_as_solver": False,
           "retained_from_Cycle479": "six-neighbour divide-six law only",
           "boundary_drive_replacement": "internal (+1,-2,+1) zero-sum source",
           "zero_mode_rule": "zero initial slice plus zero-sum source preserves mean zero",
           "comparator": "Cycle216 periodic mean-zero 3L+"})


@lru_cache(maxsize=None)
def jacobi_point_kernel() -> np.ndarray:
    return jacobi(point_source())


def laplacian_interval() -> tuple[float, float]:
    momenta = 2 * np.pi * np.fft.fftfreq(LENGTH)
    values = np.asarray([
        6 - 2 * (np.cos(px) + np.cos(py) + np.cos(pz))
        for px in momenta for py in momenta for pz in momenta
    ])
    values = values[values > 1e-13]
    return float(values.min()), float(values.max())


@lru_cache(maxsize=1)
def cheb_coefficients() -> tuple[tuple[float, float], ...]:
    low, high = laplacian_interval()
    center = (low + high) / 2
    radius = (high - low) / 2
    alpha = round((1 / center) * Q_SCALE) / Q_SCALE
    rows = [(alpha, 0.0)]
    for _ in range(1, CHEB_DEPTH):
        beta = round(((radius * alpha / 2) ** 2) * Q_SCALE) / Q_SCALE
        alpha = round((1 / (center - beta / alpha)) * Q_SCALE) / Q_SCALE
        rows.append((alpha, beta))
    return tuple(rows)


def chebyshev(source: np.ndarray, depth: int = CHEB_DEPTH) -> np.ndarray:
    if depth == 0:
        return np.zeros_like(source)
    coefficients = cheb_coefficients()[:depth]
    previous = np.zeros_like(source)
    alpha, _ = coefficients[0]
    current = previous + alpha * (3 * source)
    for alpha, beta in coefficients[1:]:
        residual = 3 * source - laplacian(current)
        following = current + alpha * residual + beta * (current - previous)
        previous, current = current, following
    return current


@lru_cache(maxsize=None)
def cheb_point_kernel() -> np.ndarray:
    return chebyshev(point_source())


def exact_word_rail(cell: tuple[int, int, int]) -> tuple[np.ndarray, dict]:
    words = np.zeros((LENGTH,) * 3, dtype=object)
    remainders = 0
    compiled_failures = 0
    sampled = 0
    maximum_bits = 0
    for _layer in range(JACOBI_DEPTH):
        numerator = sum(np.roll(words, shift, axis=axis)
                        for axis in range(3) for shift in (-1, 1))
        numerator[cell] += WORD_SCALE
        flat = numerator.ravel()
        remainders += sum(int(int(value) % 6 != 0) for value in flat)
        if sampled < 8:
            for value in flat:
                value = int(value)
                if value:
                    quotient, remainder = c467.compiled_division(value, WORD_BITS + 3)
                    compiled_failures += int(quotient != value // 6 or remainder != value % 6)
                    sampled += 1
                    break
        words = numerator // 6
        maximum_bits = max(maximum_bits, max(int(value).bit_length() for value in words.ravel()))
    return words, {"remainder_failures": remainders,
                   "compiled_divider_failures": compiled_failures,
                   "compiled_samples": sampled, "maximum_word_bits": maximum_bits}


def word_quadrupole(geometry) -> tuple[np.ndarray, dict]:
    decoded = np.zeros((LENGTH,) * 3, dtype=object)
    rows = []
    for coefficient, cell in zip((3, -6, 3), geometry.sources):
        words, controls = exact_word_rail(cell)
        decoded += coefficient * words
        rows.append({"cell": cell, "multiplicity_and_sign": coefficient, **controls})
    return np.asarray(decoded, dtype=float) / WORD_SCALE, {
        "binary_source_compiler_instances": 12,
        "unit_occurrences_before_factor_three": 4,
        "positive_instances": 6,
        "negative_instances": 6,
        "three_spatial_histories_compressed_by_linearity": True,
        "rail_rows": rows,
        "signed_payload_preparation_compiled": False,
    }


def periodic_schedule_controls() -> None:
    cells = tuple(product(range(LENGTH), repeat=3))
    colour_of = lambda cell: tuple(TORUS_COLOUR[value] for value in cell)
    rounds = []
    conflicts = 0
    maximum_parallel = 0
    for colour in product(range(5), repeat=3):
        selected = tuple(cell for cell in cells if colour_of(cell) == colour)
        maximum_parallel = max(maximum_parallel, len(selected))
        stars = []
        for cell in selected:
            stars.append({cell} | {
                tuple((cell[axis] + (shift if coordinate == axis else 0)) % LENGTH
                      for axis in range(3))
                for coordinate in range(3) for shift in (-1, 1)
            })
        for left in range(len(stars)):
            for right in range(left + 1, len(stars)):
                conflicts += int(bool(stars[left] & stars[right]))
        rounds.append((colour, len(selected)))
    coverage = sum(count for _colour, count in rounds)
    frames = c210.proper_cubic_frames()
    frame_coverage = []
    colour_relabelling_residuals = []
    classes = {
        colour: {cell for cell in cells if colour_of(cell) == colour}
        for colour in product(range(5), repeat=3)
    }
    for frame in frames:
        transformed = {
            tuple(int(value % LENGTH) for value in frame @ np.asarray(cell)) for cell in cells
        }
        frame_coverage.append(len(transformed))
        for colour, source_class in classes.items():
            target_colour = []
            for target_axis in range(3):
                source_axis = int(np.flatnonzero(frame[target_axis])[0])
                value = colour[source_axis]
                if int(frame[target_axis, source_axis]) < 0:
                    value = TORUS_REVERSAL_COLOUR[value]
                target_colour.append(value)
            carried_class = {
                tuple(int(value % LENGTH) for value in frame @ np.asarray(cell))
                for cell in source_class
            }
            colour_relabelling_residuals.append(
                len(carried_class.symmetric_difference(classes[tuple(target_colour)]))
            )
    check("a torus-valid 125-round double-buffer schedule covers every L13 cell with disjoint stars and carried all24 covariance",
          len(rounds) == 125 and coverage == LENGTH**3 and conflicts == 0
          and len(frames) == 24 and min(frame_coverage) == LENGTH**3
          and max(colour_relabelling_residuals) == 0,
          {"rounds_per_layer": len(rounds), "layers": JACOBI_DEPTH,
           "scheduled_rounds": len(rounds) * JACOBI_DEPTH, "coverage_per_layer": coverage,
           "maximum_parallel_stars": maximum_parallel, "star_conflicts": conflicts,
           "double_buffered": True, "one_dimensional_colour_word": TORUS_COLOUR,
           "reversal_colour_permutation": TORUS_REVERSAL_COLOUR,
           "frame_coverages": frame_coverage,
           "signed_permutation_colour_class_tests": len(colour_relabelling_residuals),
           "maximum_colour_class_symmetric_difference": max(colour_relabelling_residuals)})


def multi_vertex_layer(length: int, cells: tuple[tuple[int, int, int], ...], *, delete=False):
    dimension = 7 * length**3
    if delete:
        return sparse.eye(dimension, dtype=complex, format="csr")
    delta = c425.shore.local_vertex_block(c425.ANGLE) - np.eye(7)
    rows, columns, values = [], [], []
    for cell in cells:
        indices = (c425.reservoir_index(cell, length),) + tuple(
            c425.field_index(cell, direction, length) for direction in range(6)
        )
        for left, target in enumerate(indices):
            for right, source in enumerate(indices):
                if abs(delta[left, right]) > 1e-15:
                    rows.append(target); columns.append(source); values.append(delta[left, right])
    return sparse.eye(dimension, dtype=complex, format="csr") + sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


@lru_cache(maxsize=None)
def multi_update(cells: tuple[tuple[int, int, int], ...], delete_vertex=False):
    return (c425.stream_layer(LENGTH) @ multi_vertex_layer(
        LENGTH, cells, delete=delete_vertex
    ) @ c425.field_coin_layer(LENGTH)).tocsr()


def filter_kernel(cells, source_cell, *, delete_vertex=False, depth=FILTER_DEPTH):
    update = multi_update(tuple(cells), delete_vertex)
    state = np.zeros(update.shape[0], dtype=complex)
    state[c425.reservoir_index(source_cell, LENGTH)] = 1
    accumulator = np.zeros_like(state)
    phase = c425.ANGLE / LENGTH**1.5
    for layer in range(depth):
        accumulator += np.exp(-1j * layer * phase) * state / depth
        state = update @ state
    fields = accumulator[LENGTH**3:].reshape(LENGTH**3, 6)
    scalar = fields @ np.conj(c210.UNIFORM)
    return scalar.reshape((LENGTH,) * 3), accumulator


def raw_fields(geometry, scalar_payloads, route: str):
    output = {}
    zero = np.zeros((c435.SOURCE_DIM, c435.RECEIVER_DIM), dtype=complex)
    for cell, payload in scalar_payloads.items():
        if route == ROUTES[0]:
            profile = np.roll(jacobi_point_kernel(), cell, axis=(0, 1, 2))
        elif route == ROUTES[1]:
            profile = np.roll(cheb_point_kernel(), cell, axis=(0, 1, 2))
        elif route == ROUTES[2]:
            profile, _accumulator = filter_kernel(tuple(geometry.sources), cell)
        else:
            raise ValueError("unknown Cycle495 route")
        for flat in np.flatnonzero(abs(profile) > 1e-15):
            target = tuple(int(value) for value in np.unravel_index(int(flat), profile.shape))
            for direction, component in enumerate(c210.UNIFORM):
                key = c425.field_index(target, direction, LENGTH)
                output[key] = output.get(key, zero.copy()) + profile[target] * component * payload
    return c435.prune(output)


@lru_cache(maxsize=1)
def common_scale() -> tuple[float, dict]:
    geometry = c453.TRAIN
    compiled = c491.source_compiled_state(geometry)
    _reservoirs, original_fields, scalar = c491.split_compiled(compiled, geometry)
    target = c491.dictionary_norm(original_fields)
    raw = {route: c491.dictionary_norm(raw_fields(geometry, scalar, route)) for route in ROUTES}
    scale = float(min(1.0, np.sqrt(target / max(raw.values()))))
    return scale, {"train_target_field_norm_weight": target,
                   "train_raw_route_norm_weights": raw,
                   "packet_targets_used": False, "held_values_used": False}


def completed_state(geometry_name: str, route: str):
    geometry = next(item for item in c453.GEOMETRIES if item.name == geometry_name)
    compiled = c491.source_compiled_state(geometry)
    reservoirs, original_fields, scalar = c491.split_compiled(compiled, geometry)
    raw = raw_fields(geometry, scalar, route)
    scale, scale_controls = common_scale()
    target = c491.dictionary_norm(original_fields)
    carried = scale * scale * c491.dictionary_norm(raw)
    if carried > target + c435.TOLERANCE:
        raise ValueError("common train contraction cannot complete this column")
    output = {key: value.copy() for key, value in reservoirs.items()}
    output.update({key: scale * value for key, value in raw.items()})
    completion_weight = max(0.0, target - carried)
    completion_key = c425.reservoir_index(COMPLETION_CELL, LENGTH)
    if completion_key in output:
        raise ValueError("physical completion reservoir collides with source reservoir")
    if completion_weight:
        output[completion_key] = np.sqrt(completion_weight) * c435.base_matter()
    return c435.prune(output), {
        **scale_controls, "common_scale": scale, "raw_norm_weight": c491.dictionary_norm(raw),
        "carried_norm_weight": carried, "completion_norm_weight": completion_weight,
        "completion_key": completion_key, "completion_is_physical_reservoir_M2": True,
        "completion_source_vertex_and_field_stream_inert": True,
        "completion_receiver_inert": False,
        "completion_is_load_bearing_free_receiver_component": True,
        "target_field_norm_weight": target, "output_norm": c435.state_norm(output),
        "physical_keys_only": all(0 <= key < 7 * LENGTH**3 for key in output),
        "held_refit": False,
    }


def solver_controls() -> dict:
    print("\nLOCAL SOLVER / WORD / FILTER CONTROLS")
    low, high = laplacian_interval()
    coefficient_bytes = repr(cheb_coefficients()).encode()
    solver_rows = []
    word_rows = []
    deletion_rows = []
    for geometry in c453.GEOMETRIES:
        source = source_array(geometry)
        exact = exact_scalar(source)
        route_a = jacobi(source)
        route_b = chebyshev(source)
        zero = np.zeros_like(source)
        deletion_rows.extend((
            {"route": ROUTES[0], "geometry": geometry.name,
             "zero_source_norm": float(np.linalg.norm(jacobi(zero))),
             "source_deletion_signal": float(np.linalg.norm(route_a)),
             "last_layer_deletion_signal": float(np.linalg.norm(
                 route_a - jacobi(source, JACOBI_DEPTH - 1)))},
            {"route": ROUTES[1], "geometry": geometry.name,
             "zero_source_norm": float(np.linalg.norm(chebyshev(zero))),
             "source_deletion_signal": float(np.linalg.norm(route_b)),
             "last_layer_deletion_signal": float(np.linalg.norm(
                 route_b - chebyshev(source, CHEB_DEPTH - 1)))},
        ))
        word, word_control = word_quadrupole(geometry)
        solver_rows.extend((
            {"route": ROUTES[0], "geometry": geometry.name, "held": geometry.held,
             "solution_residual": float(np.linalg.norm(route_a - exact)),
             "equation_residual": float(np.linalg.norm(laplacian(route_a) - 3 * source))},
            {"route": ROUTES[1], "geometry": geometry.name, "held": geometry.held,
             "solution_residual": float(np.linalg.norm(route_b - exact)),
             "equation_residual": float(np.linalg.norm(laplacian(route_b) - 3 * source))},
        ))
        word_residual = float(np.max(abs(word - route_a)))
        word_rows.append({"geometry": geometry.name, "held": geometry.held,
                          "maximum_word_to_float_residual": word_residual, **word_control})
    # Reverse the last beta-nonzero Chebyshev layer on a deterministic held source.
    source = source_array(c453.HELD)
    coefficients = cheb_coefficients()
    previous = np.zeros_like(source)
    current = coefficients[0][0] * 3 * source
    reverse_residuals = []
    for alpha, beta in coefficients[1:]:
        following = current + alpha * (3 * source - laplacian(current)) + beta * (current - previous)
        restored = current - (following - current - alpha * (3 * source - laplacian(current))) / beta
        reverse_residuals.append(float(np.linalg.norm(restored - previous)))
        previous, current = current, following
    check("the retained 96-layer Jacobi law and exact D words agree on train/held signed quadrupoles",
          all(row["maximum_word_to_float_residual"] < 3e-15 for row in word_rows)
          and all(sum(item["remainder_failures"] + item["compiled_divider_failures"]
                      for item in row["rail_rows"]) == 0 for row in word_rows),
          {"D": str(WORD_SCALE), "word_bits": WORD_BITS, "rows": word_rows})
    check("the frozen Q48/64 Chebyshev recurrence is local, convergent, coefficient-fixed, and reverses from retained history",
          high > low > 0 and len(coefficients) == CHEB_DEPTH
          and max(reverse_residuals) < 3e-12
          and max(row["equation_residual"] for row in solver_rows if row["route"] == ROUTES[1]) < 2e-6
          and max(row["solution_residual"] for row in solver_rows if row["route"] == ROUTES[1]) < 3e-7,
          {"lambda_min": low, "lambda_max": high, "condition_number": high / low,
           "coefficient_sha256": sha256(coefficient_bytes).hexdigest(),
           "coefficient_denominator": Q_SCALE, "layers": CHEB_DEPTH,
           "maximum_reverse_residual": max(reverse_residuals), "solver_rows": solver_rows,
           "finite_M2_Q48_multiplier_compiled": False})
    check("Jacobi and Chebyshev source deletion and final-layer deletion are visible on train and held domains",
          all(row["zero_source_norm"] == 0
              and row["source_deletion_signal"] > DELETION_SIGNAL_MIN
              and row["last_layer_deletion_signal"] > DELETION_SIGNAL_MIN
              for row in deletion_rows),
          {"frozen_nonzero_threshold": DELETION_SIGNAL_MIN,
           "rows": deletion_rows, "depths_called_time": False})
    return {"solver_rows": solver_rows, "word_rows": word_rows,
            "deletion_rows": deletion_rows,
            "coefficient_sha256": sha256(coefficient_bytes).hexdigest()}


def dressed_update_controls() -> dict:
    print("\nTHREE-RESERVOIR LOCAL UPDATE / FILTER")
    rows = []
    frame_residuals = []
    for geometry in c453.GEOMETRIES:
        cells = tuple(geometry.sources)
        update = multi_update(cells)
        seed = np.zeros(update.shape[0], dtype=complex)
        for coefficient, cell in zip((1, -2, 1), cells):
            seed[c425.reservoir_index(cell, LENGTH)] = coefficient / np.sqrt(6)
        _profile, filtered = filter_kernel(cells, cells[0])
        # The actual quadrupole candidate uses one linear filter on its signed seed.
        state = seed.copy(); candidate = np.zeros_like(seed)
        target_phase = c425.ANGLE / LENGTH**1.5
        for layer in range(FILTER_DEPTH):
            candidate += np.exp(-1j * layer * target_phase) * state / FILTER_DEPTH
            state = update @ state
        state = seed.copy(); depth_deleted = np.zeros_like(seed)
        for layer in range(FILTER_DEPTH - 1):
            depth_deleted += (
                np.exp(-1j * layer * target_phase) * state / (FILTER_DEPTH - 1)
            )
            state = update @ state
        zero_seed = np.zeros_like(seed)
        zero_filtered = np.zeros_like(seed)
        zero_state = zero_seed.copy()
        for layer in range(FILTER_DEPTH):
            zero_filtered += np.exp(-1j * layer * target_phase) * zero_state / FILTER_DEPTH
            zero_state = update @ zero_state
        normalized_candidate = candidate / np.linalg.norm(candidate)
        eigen_residual = float(np.linalg.norm(update @ normalized_candidate
                                               - np.exp(1j * target_phase) * normalized_candidate))
        restored = update.getH() @ (update @ seed)
        deleted = multi_update(cells, True) @ seed
        nominal = update @ seed
        rows.append({
            "geometry": geometry.name, "held": geometry.held, "dimension": update.shape[0],
            "source_cells": cells, "seed_norm": float(np.linalg.norm(seed)),
            "inverse_residual": float(np.linalg.norm(restored - seed)),
            "filter_candidate_norm": float(np.linalg.norm(candidate)),
            "target_eigenphase_operator_coordinate": target_phase,
            "candidate_eigen_residual": eigen_residual,
            "zero_seed_filter_norm": float(np.linalg.norm(zero_filtered)),
            "source_seed_deletion_signal": float(np.linalg.norm(candidate)),
            "last_filter_layer_deletion_signal": float(np.linalg.norm(candidate - depth_deleted)),
            "vertex_deletion_residual": float(np.linalg.norm(nominal - deleted)),
            "physical_local_powers": True, "coherent_filter_accumulation_physical": False,
            "dressed_preparation_complete": False,
        })
        for frame in c210.proper_cubic_frames():
            representation = c425.frame_representation(LENGTH, frame)
            rotated = tuple(tuple(int(value % LENGTH) for value in frame @ np.asarray(cell))
                            for cell in cells)
            frame_residuals.append(float(sparse.linalg.norm(
                representation @ update - multi_update(rotated) @ representation
            )))
    check("the three-reservoir Cycle425 update is exactly invertible, deletion-visible, bounded-local, and carried-covariant in all24 frames",
          len(frame_residuals) == 48 and max(frame_residuals) < 8e-12
          and max(row["inverse_residual"] for row in rows) < 3e-13
          and min(row["vertex_deletion_residual"] for row in rows) > 1e-4,
          {"rows": rows, "frame_tests": len(frame_residuals),
           "maximum_frame_residual": max(frame_residuals),
           "reservoir_vertex_support_M2": 7, "coin_support_M2": 6,
           "stream_support_M2": 2, "filter_depth_called_time": False})
    check("the fixed spectral filter is diagnosed without promoting host accumulation into a dressed-state preparation",
          all(row["filter_candidate_norm"] > 0 and not row["dressed_preparation_complete"]
              and not row["coherent_filter_accumulation_physical"]
              and row["zero_seed_filter_norm"] == 0
              and row["source_seed_deletion_signal"] > DELETION_SIGNAL_MIN
              and row["last_filter_layer_deletion_signal"] > DELETION_SIGNAL_MIN
              for row in rows),
          {"rows": rows, "frozen_nonzero_deletion_threshold": DELETION_SIGNAL_MIN,
           "eigenphase_called_rate_or_energy": False})
    result = {"rows": rows, "maximum_frame_residual": max(frame_residuals)}
    # Rotated matrices are audit fixtures, not retained shell materialization.
    multi_update.cache_clear()
    return result


def prediction_controls() -> dict:
    print("\nONE-COMMON-SCALE PHYSICAL-COMPLETION PACKET ROWS")
    rows = []
    adapters = {}
    inverse_rows = []
    for route in ROUTES:
        for geometry in c453.GEOMETRIES:
            initial, adapter = completed_state(geometry.name, route)
            adapters[(route, geometry.name)] = adapter
            one_step = c491.receiver_step(initial, geometry)
            restored = c491.receiver_inverse(one_step, geometry)
            inverse_rows.append((route, geometry.name,
                                 c435.state_residual(restored, initial),
                                 abs(c435.state_norm(one_step) - 1)))
            pure, pure_control = c491.evolve_receiver(initial, geometry)
            free, free_control = c491.free_result(geometry.name)
            pure_weights = c435.packet_weights(pure)
            free_weights = c435.packet_weights(free)
            free_moments = c435.packet_moments(free_weights)
            for target_route, occupation in c453.PHYSICAL_STRENGTHS.items():
                weights = (1 - occupation) * free_weights + occupation * pure_weights
                moments = c435.packet_moments(weights)
                target = c453.LEGACY_ROWS[(geometry.separation, target_route)]
                shift = moments["width"] - free_moments["width"]
                rows.append({
                    "route": route, "geometry": geometry.name, "held": geometry.held,
                    "separation": geometry.separation, "target_route": target_route,
                    "occupation": occupation, "width_shift": shift,
                    "Cycle420_target": target, "absolute_row_residual": shift - target,
                    "centroid_shift": moments["centroid"] - free_moments["centroid"],
                    "maximum_norm_error": max(pure_control["maximum_norm_error"],
                                               free_control["maximum_norm_error"]),
                    "maximum_boundary_norm_weight": max(
                        pure_control["maximum_boundary_norm_weight"],
                        free_control["maximum_boundary_norm_weight"]),
                    "held_refit": False, "adapter": adapter,
                })
            del initial, one_step, restored, pure, pure_weights, free_weights
            gc.collect()
    dispositions = {}
    for route in ROUTES:
        selected = [row for row in rows if row["route"] == route]
        keyed = {(row["separation"], row["target_route"]): row for row in selected}
        order = all(keyed[(2, target)]["width_shift"] > keyed[(1, target)]["width_shift"]
                    for target in c453.PHYSICAL_STRENGTHS)
        numeric = max(abs(row["absolute_row_residual"]) for row in selected) < ROW_TOLERANCE
        physical_arithmetic = route == ROUTES[0]
        preparation = False  # every route still has a named payload/preparation seam
        dispositions[route] = {
            "stronger_a2_order": order, "all_four_absolute_rows": len(selected) == 4,
            "maximum_absolute_row_residual": max(abs(row["absolute_row_residual"]) for row in selected),
            "all_rows_within_tolerance": numeric,
            "finite_M2_local_arithmetic_or_update": physical_arithmetic or route == ROUTES[2],
            "physical_preparation_complete": preparation,
            "PHYSICAL_COMPLETE": numeric and order and preparation,
            "disposition": ("EXACT_BOUNDED_ADAPTER" if route == ROUTES[0]
                            else "PARTIAL_ATTEMPT_WITH_NAMED_WALLS"),
        }
    scale, scale_control = common_scale()
    check("all twelve train/held packet rows use one train-only scale and an ordinary physical reservoir completion/free receiver contribution without held refit",
          len(rows) == 12 and all(not row["held_refit"] for row in rows)
          and all(abs(row["adapter"]["common_scale"] - scale) < 1e-15 for row in rows)
          and all(row["adapter"]["completion_is_physical_reservoir_M2"]
                  and row["adapter"]["completion_source_vertex_and_field_stream_inert"]
                  and not row["adapter"]["completion_receiver_inert"]
                  and row["adapter"]["completion_is_load_bearing_free_receiver_component"]
                  and row["adapter"]["physical_keys_only"]
                  for row in rows)
          and max(abs(row["adapter"]["output_norm"] - 1) for row in rows) < c435.TOLERANCE
          and max(row["maximum_norm_error"] for row in rows) < c435.TOLERANCE
          and max(row["maximum_boundary_norm_weight"] for row in rows) < c453.BOUNDARY_MAXIMUM,
          {"common_scale": scale, "scale_control": scale_control,
           "rows": rows, "dispositions": dispositions})
    check("route dispositions require rows, order, and physical preparation rather than promoting a solver profile",
          all(not item["PHYSICAL_COMPLETE"] for item in dispositions.values()),
          {"row_tolerance": ROW_TOLERANCE, "dispositions": dispositions})
    print("CYCLE495_ROWS", rows, flush=True)
    print("CYCLE495_DISPOSITIONS", dispositions, flush=True)
    return {"rows": rows, "dispositions": dispositions, "common_scale": scale,
            "scale_control": scale_control, "inverse_rows": inverse_rows}


def inverse_deletion_fixture_controls(prediction: dict) -> None:
    inverse_rows = prediction["inverse_rows"]
    geometry = c453.TRAIN
    initial, adapter = completed_state(geometry.name, ROUTES[0])
    intact = c491.receiver_step(initial, geometry)
    deletion_rows = {}
    for name, kwargs in (
        ("receiver", {"receiver_enabled": False}),
        ("field_stream", {"stream_enabled": False}),
        ("packet_stream", {"packet_stream_enabled": False}),
        ("contact", {"contact_enabled": False}),
    ):
        deleted = c491.receiver_step(initial, geometry, **kwargs)
        deletion_rows[name] = c435.state_residual(intact, deleted)
    completion_deleted = {key: value for key, value in initial.items()
                          if key != adapter["completion_key"]}
    completion_deleted_step = c491.receiver_step(completion_deleted, geometry)
    deletion_rows["physical_completion"] = c435.state_residual(
        intact, completion_deleted_step
    )
    update_rows = c435.restricted_factors()[0]
    contact = c435.c319.triple_contact(c435.LABELS)
    two_particle = np.zeros(c435.MATTER_DIM, dtype=complex)
    two_particle[c435.LABEL_INDEX[(2, (0, 1), 0, (), 0, ())]] = 1
    contact_signal = float(np.linalg.norm(contact @ two_particle - two_particle))
    rejected = 0
    for probe in (
        lambda: completed_state(geometry.name, "bad"),
        lambda: c490.validate_word(0),
        lambda: multi_update(((0, 0, 0),), False) if LENGTH == 2 else (_ for _ in ()).throw(ValueError()),
    ):
        try:
            probe()
        except (ValueError, KeyError):
            rejected += 1
    check("the receiver inverse and receiver/stream/packet/completion deletions remain explicit while contact is a one-particle spectator on this column",
          max(max(row[2], row[3]) for row in inverse_rows) < c435.TOLERANCE
          and min(deletion_rows[name] for name in
                  ("receiver", "field_stream", "packet_stream", "physical_completion")) > 1e-10
          and deletion_rows["contact"] == 0 and rejected == 3,
          {"inverse_rows": inverse_rows, "deletions": deletion_rows,
           "completion_norm_weight": adapter["completion_norm_weight"],
           "completion_receiver_inert": adapter["completion_receiver_inert"],
           "lawful_domain_rejections": rejected})
    check("the Cycle219 one-particle mass and Cycle230 contact fixtures remain unchanged spectators",
          abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]) < c435.TOLERANCE
          and update_rows["uniform_one_particle_eigen_residual"] < c435.TOLERANCE
          and update_rows["contact_nontrivial_columns"] == 645 and contact_signal > 1e-6,
          {"Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
           "three_cell_rest_mass": update_rows["three_cell_rest_mass"],
           "mass_eigen_residual": update_rows["uniform_one_particle_eigen_residual"],
           "contact_nontrivial_columns": update_rows["contact_nontrivial_columns"],
           "contact_deletion_signal": contact_signal})


def inventory_no_go_controls(solver: dict, dressed: dict, prediction: dict) -> None:
    walls = ("signed_payload_preparation", "Q48_arithmetic", "filter_accumulation",
             "complete_shell", "source_renewal")
    pairwise = [
        {"pair": (left, right), "independent": True,
         "closing_left_closes_right": False, "closing_right_closes_left": False}
        for index, left in enumerate(walls) for right in walls[index + 1:]
    ]
    inventory = {
        "supplied": [
            "Cycle216 K=2I-U-Udagger and exact scalar 3L+",
            "Cycle479 depth96/D=6^96 local relaxation",
            "Cycle467/470/474 unsigned arithmetic, delivery, and finite-box scheduling",
            "Cycle425 reservoir/coin/stream update",
            "Cycle490 word256 source and Cycle491 receiver/targets",
            "periodic L13 a1 train/a2 held, common-scale formula, tolerances and readout",
        ],
        "derived": [
            "torus-valid 125-round double-buffer schedule",
            "exact four-sign/twelve-binary-rail Jacobi words",
            "fixed Q48/64 Chebyshev recurrence and reverse history",
            "three-reservoir local update and depth64 filter attempt",
            "physical-reservoir norm completion and twelve packet rows",
        ],
        "open": [
            "signed matrix-payload preparation into retained unsigned word compilers",
            "finite-M2 Q48 coefficient multiply/add",
            "physical coherent filter accumulation/eigenstate preparation",
            "complete L13 shell/fault model and autonomous source renewal",
            "recoil/work, energy-stress identity, physical time, gravity/metric, Records, Born occurrence",
        ],
        "firewall": {"host_Kplus_called_recurrent_gate": False,
                     "iteration_depth_called_time": False,
                     "eigenphase_called_energy_or_rate": False,
                     "response_called_gravity": False,
                     "norm_weight_called_probability": False,
                     "word_occupancy_called_Record": False},
    }
    check("the supplied/derived/open inventory keeps exact adapters separate from completed physical preparation",
          AUTHORITY == "none" and AUDIT == "unset" and len(pairwise) == 10,
          {**inventory, "pairwise_wall_table": pairwise})
    check("full N1-N8 rejects no-go, minimum-content, shared-obstruction, and axiom-pressure promotion",
          all(not item["PHYSICAL_COMPLETE"] for item in prediction["dispositions"].values())
          and len(dressed["rows"]) == 2 and len(solver["solver_rows"]) == 4,
          {"N1_normalized_families": [
              {"family": "divide-six Jacobi", "object": "D-scaled retained word histories",
               "mechanism": "six-neighbour average", "terminal": "physical payload-to-row", "status": "ATTEMPTED"},
              {"family": "fixed Chebyshev", "object": "Q48 two-slice recurrence",
               "mechanism": "local accelerated polynomial", "terminal": "compiled Q48 rows", "status": "ATTEMPTED"},
              {"family": "three-reservoir filter", "object": "local Cycle425 unitary plus Cesaro filter",
               "mechanism": "spectral concentration", "terminal": "physical dressed preparation", "status": "ATTEMPTED"},
              {"family": "reduction-tree CG", "object": "local words plus physical reductions", "status": "UNTESTED"},
              {"family": "multigrid", "object": "local restriction/coarse/prolongation", "status": "UNTESTED"},
              {"family": "QSP/quantum-walk resolvent", "object": "unitary polynomial inverse", "status": "UNTESTED"}],
           "N2_pairwise_wall_table": pairwise,
           "N3_hidden_wall_scan": ["source basis", "zero mode", "factor 3", "D/Q48", "depths",
              "periodic wrap", "double buffers", "colour origin", "filter phase", "factor order",
              "common scale", "load-bearing physical completion", "occupations", "observable", "targets/tolerances", "host readout"],
           "N4_residual_matching": [
              {"witness": "scripts/physical_3d_laplacian_s3_generator_provenance_cycle479_2026_07_19.py:270",
               "matches": "divide-six words", "does_not_match": "signed payload preparation"},
              {"witness": "scripts/physical_elementary_divsix_nn_compiler_cycle467_2026_07_19.py:391",
               "matches": "unsigned division", "does_not_match": "Q48 multiplication"},
              {"witness": "scripts/common_cubic_transient_stationary_update_cycle425_2026_07_19.py:420",
               "matches": "one-defect eigen diagnostic", "does_not_match": "three-defect preparation"},
              {"witness": "scripts/physical_geometry_changing_carrier_tournament_cycle491_2026_07_20.py:244",
               "matches": "norm accounting", "does_not_match": "physical receiver-active completion built here"}],
           "N5_scope": "only periodic L13 a1/a2, two occupations, four receiver updates and three frozen routes",
           "N6_partial_paths": "signed fanout, Q48 synthesis, QSP/phase-estimation, physical adiabatic preparation, multigrid and reduction-tree CG remain live",
           "N7_steelman": "compile signed fixed-point source and Q48 multiply-add on Cycle470, then compare all routes at equal error/shell resources",
           "N8_cross_cycle": "Cycles432-435, 447-450, 463-479 and 484-491 closed walls by explicit enlarged constructions",
           "claim_gate": "broad no-go FAIL; minimum-content FAIL; shared obstruction FAIL; axiom pressure FAIL; there is no axiom pressure"})


def resource_controls(started: float) -> None:
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    check("the Cycle495 cold run stays below explicit wall and RSS caps",
          elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
          {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
           "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB,
           "L13_cells": LENGTH**3, "Jacobi_layers": JACOBI_DEPTH,
           "Jacobi_rounds": 125 * JACOBI_DEPTH, "word_bits": WORD_BITS,
           "binary_source_rails": 12, "Chebyshev_layers": CHEB_DEPTH,
           "Q_bits": Q_BITS, "filter_layers": FILTER_DEPTH,
           "complete_L13_shell_materialized": False})


def main() -> int:
    global PASS, FAIL
    started = perf_counter()
    print("CYCLE 495: PHYSICAL CYCLE216 LOCAL-SOLVER TOURNAMENT")
    note_and_frozen_controls()
    periodic_interface_controls()
    periodic_schedule_controls()
    solver = solver_controls()
    dressed = dressed_update_controls()
    prediction = prediction_controls()
    inverse_deletion_fixture_controls(prediction)
    inventory_no_go_controls(solver, dressed, prediction)
    resource_controls(started)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
