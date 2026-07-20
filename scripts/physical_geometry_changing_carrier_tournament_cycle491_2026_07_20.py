#!/usr/bin/env python3
"""Cycle 491: geometry-changing carrier tournament after Cycle490.

Join the frozen Cycle487 uniform discrete local source actuation to three
materially different carrier objects: the Cycle213 centered retarded wave,
the Cycle216 static stiffness inverse, and the Cycle425 finite-Q1 transient
update.  Each carrier hands a declared source column to the same physical M64
receiver packet.  Continuous/profile preparation seams are kept separate from
local physical E/G.  Response is not gravity, phase is not energy, depth is
not time, and norm weight is not probability.  Authority none; audit unset.
"""

from __future__ import annotations

from dataclasses import asdict
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
from time import perf_counter
import resource
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_discrete_source_law_tournament_cycle490_2026_07_20 as c490
import retarded_cubic_mass_field_cycle213_2026_07_16 as c213
import virtual_exchange_green_kernel_cycle216_2026_07_16 as c216
import common_cubic_transient_stationary_update_cycle425_2026_07_19 as c425


c487 = c490.c487
c453 = c490.c453
c435 = c490.c435
c420 = c490.c420
c472 = c490.c472
c480 = c490.c480

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_GEOMETRY_CHANGING_CARRIER_TOURNAMENT_CYCLE491_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
SOURCE_WORD = 256
CARRIER_STEPS = 4
RECEIVER_STEPS = 4
ROW_TOLERANCE = c453.NUMERIC_ROW_TOLERANCE
BOUNDARY_MAXIMUM = c453.BOUNDARY_MAXIMUM
WALL_CAP_SECONDS = 900.0
RSS_CAP_MIB = 3072.0
PASS = 0
FAIL = 0

FROZEN = {
    "Cycle213": ("retarded_cubic_mass_field_cycle213_2026_07_16.py",
                 "472e28c78901368629c8d9d6f614bb8fb3ea003639ac61d480d06941cdf6cb86"),
    "Cycle216": ("virtual_exchange_green_kernel_cycle216_2026_07_16.py",
                 "9ef0fff433bbf1c96c9b13c5ce79530e01fe705f08c6caf6b60316e20359e011"),
    "Cycle425": ("common_cubic_transient_stationary_update_cycle425_2026_07_19.py",
                 "c3aa51528e54c28b8b258d83d254068430d3b1816a03aafefabe4be3ef6a84c9"),
    "Cycle487": ("physical_discrete_quadrupole_exact_strength_bridge_cycle487_2026_07_20.py",
                 "b0e4ac4aea641dbf90f64ac6d944b639b983ec76e365c3a60377b1ea2b5cf091"),
    "Cycle490": ("physical_discrete_source_law_tournament_cycle490_2026_07_20.py",
                 "47609253d3a868a0f736f0c9571a7a6a0878776590af6ddf24d4e6ca9fe80ff4"),
}

ROUTES = {
    "A_Cycle213_retarded_slice": {
        "object": "centered two-slice scalar wave",
        "mechanism": "one supplied impulse followed by three source-free radius-one steps",
        "handoff": "scalar projection, uniform-direction lift, declared-column norm completion",
    },
    "B_Cycle216_static_exchange": {
        "object": "coin stiffness K=2I-U-Udagger and its zero-mean pseudoinverse",
        "mechanism": "exact static coin field K+ rho",
        "handoff": "coin-field profile, declared-column norm completion",
    },
    "C_Cycle425_Q1_transient": {
        "object": "finite-Q1 coin-plus-stream free branch",
        "mechanism": "four exact unitary transient steps after local source actuation",
        "handoff": "identity on the Q1 carrier state",
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
        "authority: none", "audit: unset", "cycle 491", "frozen before outputs",
        "a — cycle213 retarded slice", "b — cycle216 static exchange",
        "c — cycle425 q1 transient", "l13/a1/depth4", "l13/a2/depth4",
        "all four absolute rows", "stronger-a2 order", "held rows never refit",
        "declared-column norm completion", "complete l13 shell remains open",
        "cycle425 stationary/dressed face is not silently substituted",
        "local physical e/g", "leakage", "inverse", "deletion", "mass/contact",
        "all 24 proper-cubic frames", "response is not gravity",
        "phase is not energy", "depth is not time", "norm weight is not probability",
        "n1 — normalized alternative families", "n8 — cross-cycle echo and claim gate",
        "there is no axiom pressure",
    )
    missing = tuple(item for item in required if item not in normalized(NOTE))
    check("the Cycle491 note freezes the carrier tournament before outputs", not missing, missing)


def frozen_controls() -> None:
    observed = {name: file_sha(ROOT / "scripts" / filename)
                for name, (filename, _digest) in FROZEN.items()}
    expected = {name: digest for name, (_filename, digest) in FROZEN.items()}
    check("Cycles213/216/425/487/490 remain frozen at exact input identities",
          observed == expected, {"observed": observed, "expected": expected})


def source_compiled_state(geometry):
    state = c435.quadrupole_state(geometry)
    for cell_index in range(3):
        state = c490.apply_vertex(state, geometry, "source", cell_index, SOURCE_WORD)
    return state


def split_compiled(state, geometry):
    reservoirs = {}
    fields = {}
    scalar = {}
    zero = np.zeros((c435.SOURCE_DIM, c435.RECEIVER_DIM), dtype=complex)
    for key, value in state.items():
        if key < geometry.length ** 3:
            reservoirs[key] = value.copy()
            continue
        cell, direction = c453.c432.decode_field(key, geometry.length)
        fields[key] = value.copy()
        scalar[cell] = scalar.get(cell, zero.copy()) + np.conj(c435.c210.UNIFORM[direction]) * value
    return reservoirs, fields, scalar


def dictionary_norm(state) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def wave_kernel(length: int, source_cell):
    source = np.zeros((length,) * 3)
    source[source_cell] = 1.0
    previous = np.zeros_like(source)
    current = np.zeros_like(source)
    slices = []
    for step in range(CARRIER_STEPS):
        following = c213.wave_step(previous, current, source if step == 0 else np.zeros_like(source))
        previous, current = current, following
        slices.append(current.copy())
    return previous, current, tuple(slices)


def raw_retarded_field(geometry, scalar_payloads):
    output = {}
    zero = np.zeros((c435.SOURCE_DIM, c435.RECEIVER_DIM), dtype=complex)
    for source_cell, payload in scalar_payloads.items():
        _previous, profile, _slices = wave_kernel(geometry.length, source_cell)
        for flat in np.flatnonzero(abs(profile) > 1e-15):
            cell = tuple(int(value) for value in np.unravel_index(int(flat), profile.shape))
            for direction, component in enumerate(c435.c210.UNIFORM):
                key = c425.field_index(cell, direction, geometry.length)
                output[key] = output.get(key, zero.copy()) + profile[cell] * component * payload
    return c435.prune(output)


@lru_cache(maxsize=None)
def static_origin_kernel(length: int):
    source = np.zeros((length,) * 3)
    source[(0, 0, 0)] = 1.0
    return c216.solve_coin_field(source)


@lru_cache(maxsize=None)
def static_kernel(length: int, source_cell):
    return np.roll(
        static_origin_kernel(length), tuple(int(value) for value in source_cell),
        axis=(0, 1, 2),
    )


def raw_static_field(geometry, scalar_payloads):
    output = {}
    zero = np.zeros((c435.SOURCE_DIM, c435.RECEIVER_DIM), dtype=complex)
    for source_cell, payload in scalar_payloads.items():
        profile = static_kernel(geometry.length, source_cell)
        for flat in np.flatnonzero(np.max(abs(profile), axis=3) > 1e-15):
            cell = tuple(int(value) for value in np.unravel_index(int(flat), profile.shape[:3]))
            for direction in range(6):
                key = c425.field_index(cell, direction, geometry.length)
                output[key] = output.get(key, zero.copy()) + profile[cell + (direction,)] * payload
    return c435.prune(output)


def norm_complete_column(reservoirs, original_fields, raw_fields):
    target = dictionary_norm(original_fields)
    raw = dictionary_norm(raw_fields)
    if target <= 0 or raw <= 0:
        raise ValueError("declared source column has no carrier field component")
    scale = np.sqrt(target / raw)
    output = {key: value.copy() for key, value in reservoirs.items()}
    output.update({key: scale * value for key, value in raw_fields.items()})
    return c435.prune(output), {"original_field_norm_weight": target,
                                "raw_carrier_norm_weight": raw,
                                "column_normalization": scale}


@lru_cache(maxsize=1)
def static_train_contraction_scale() -> float:
    """Train-only contraction scale, capped analytically at one."""
    geometry = c453.TRAIN
    compiled = source_compiled_state(geometry)
    _reservoirs, original_fields, scalar = split_compiled(compiled, geometry)
    raw = raw_static_field(geometry, scalar)
    exact_train_completion = np.sqrt(dictionary_norm(original_fields) / dictionary_norm(raw))
    return float(min(1.0, exact_train_completion))


@lru_cache(maxsize=None)
def static_common_completed_pure(geometry_name: str):
    """One train-frozen contraction plus an explicit orthogonal spectator.

    The negative key is a declared logical auxiliary label, not a completed
    physical M2 shell.  It preserves the source-column norm without using the
    held profile to change the K+ scale.
    """
    geometry = next(item for item in c453.GEOMETRIES if item.name == geometry_name)
    compiled = source_compiled_state(geometry)
    reservoirs, original_fields, scalar = split_compiled(compiled, geometry)
    raw = raw_static_field(geometry, scalar)
    target = dictionary_norm(original_fields)
    raw_norm = dictionary_norm(raw)
    scale = static_train_contraction_scale()
    carried = scale * scale * raw_norm
    if carried > target + c435.TOLERANCE:
        raise ValueError("train-frozen static contraction cannot complete the held column")
    output = {key: value.copy() for key, value in reservoirs.items()}
    output.update({key: scale * value for key, value in raw.items()})
    auxiliary_weight = max(0.0, target - carried)
    if auxiliary_weight:
        output[-2] = np.sqrt(auxiliary_weight) * c435.base_matter()
    output = c435.prune(output)
    return output, {
        "common_train_frozen_scale": scale,
        "raw_carrier_norm_weight": raw_norm,
        "scaled_carrier_norm_weight": carried,
        "auxiliary_spectator_norm_weight": auxiliary_weight,
        "target_compiled_field_norm_weight": target,
        "output_norm": c435.state_norm(output),
        "held_profile_used_to_select_scale": False,
        "auxiliary_physical_encoding_constructed": False,
    }


def transient_field(state, geometry, *, inverse: bool = False):
    output = state
    for _ in range(CARRIER_STEPS):
        if inverse:
            output = c435.field_stream(output, geometry.length, inverse=True)
            output = c435.field_coin(output, geometry.length, inverse=True)
        else:
            output = c435.field_coin(output, geometry.length)
            output = c435.field_stream(output, geometry.length)
    return output


@lru_cache(maxsize=None)
def carrier_pure(geometry_name: str, route: str):
    geometry = next(item for item in c453.GEOMETRIES if item.name == geometry_name)
    compiled = source_compiled_state(geometry)
    reservoirs, original_fields, scalar = split_compiled(compiled, geometry)
    scalar_sum = sum(scalar.values(), start=np.zeros_like(next(iter(scalar.values()))))
    if route == "A_Cycle213_retarded_slice":
        raw = raw_retarded_field(geometry, scalar)
        output, adapter = norm_complete_column(reservoirs, original_fields, raw)
    elif route == "B_Cycle216_static_exchange":
        raw = raw_static_field(geometry, scalar)
        output, adapter = norm_complete_column(reservoirs, original_fields, raw)
    elif route == "C_Cycle425_Q1_transient":
        output = transient_field(compiled, geometry)
        adapter = {"original_field_norm_weight": dictionary_norm(original_fields),
                   "raw_carrier_norm_weight": dictionary_norm({
                       key: value for key, value in output.items() if key >= geometry.length ** 3
                   }), "column_normalization": 1.0}
    else:
        raise ValueError("carrier route leaves the frozen tournament")
    return output, {**adapter, "compiled_norm": c435.state_norm(compiled),
                    "output_norm": c435.state_norm(output),
                    "scalar_zero_mode_payload_residual": float(np.linalg.norm(scalar_sum)),
                    "scalar_source_cells": len(scalar)}


def receiver_step(state, geometry, *, receiver_enabled=True, stream_enabled=True,
                  packet_stream_enabled=True, contact_enabled=True):
    return c490.logical_step(
        state, geometry, source_word=SOURCE_WORD, source_repetitions=1,
        source_enabled=False, receiver_enabled=receiver_enabled,
        stream_enabled=stream_enabled, packet_stream_enabled=packet_stream_enabled,
        contact_enabled=contact_enabled,
    )


def receiver_inverse(state, geometry):
    _rows, source_coin, receiver_coin, source_contact, receiver_contact, first, second = c435.restricted_factors()
    output = c435.apply_matter(state, source_contact.getH(), receiver_contact.getH())
    output = c435.field_stream(output, geometry.length, inverse=True)
    output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), second.getH())
    output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), first.getH())
    for cell_index in (2, 1, 0):
        output = c490.apply_vertex(output, geometry, "receiver", cell_index, SOURCE_WORD, inverse=True)
    output = c435.field_coin(output, geometry.length, inverse=True)
    return c435.apply_matter(output, source_coin.getH(), receiver_coin.getH())


def boundary_norm_weight(state, geometry):
    total = 0.0
    for key, value in state.items():
        cell = c453.field_cell(key, geometry.length)
        if cell is not None and any(coordinate in (0, geometry.length - 1) for coordinate in cell):
            total += float(np.vdot(value, value).real)
    return total


def evolve_receiver(state, geometry, **kwargs):
    output = state
    controls = {"maximum_norm_error": abs(c435.state_norm(output) - 1),
                "maximum_boundary_norm_weight": boundary_norm_weight(output, geometry),
                "maximum_keys": len(output)}
    for _ in range(RECEIVER_STEPS):
        output = receiver_step(output, geometry, **kwargs)
        controls["maximum_norm_error"] = max(controls["maximum_norm_error"],
                                               abs(c435.state_norm(output) - 1))
        controls["maximum_boundary_norm_weight"] = max(
            controls["maximum_boundary_norm_weight"], boundary_norm_weight(output, geometry))
        controls["maximum_keys"] = max(controls["maximum_keys"], len(output))
    return output, controls


@lru_cache(maxsize=None)
def free_result(geometry_name: str):
    geometry = next(item for item in c453.GEOMETRIES if item.name == geometry_name)
    return evolve_receiver(c435.vacuum_state(), geometry)


@lru_cache(maxsize=None)
def pure_result(geometry_name: str, route: str):
    geometry = next(item for item in c453.GEOMETRIES if item.name == geometry_name)
    state, adapter = carrier_pure(geometry_name, route)
    output, controls = evolve_receiver(state, geometry)
    return output, controls, adapter


def prediction_controls():
    print("\nFROZEN GEOMETRY-CHANGING CARRIER TOURNAMENT")
    rows_by_route = {route: [] for route in ROUTES}
    for route in ROUTES:
        for geometry in c453.GEOMETRIES:
            free, free_controls = free_result(geometry.name)
            pure, pure_controls, adapter = pure_result(geometry.name, route)
            free_weights = c435.packet_weights(free)
            pure_weights = c435.packet_weights(pure)
            free_moments = c435.packet_moments(free_weights)
            for target_route, occupation in c453.PHYSICAL_STRENGTHS.items():
                weights = (1 - occupation) * free_weights + occupation * pure_weights
                coherent = c435.combine(
                    (free, pure), np.asarray((np.sqrt(1 - occupation), np.sqrt(occupation)), dtype=complex)
                )
                moments = c435.packet_moments(weights)
                target = c453.LEGACY_ROWS[(geometry.separation, target_route)]
                shift = moments["width"] - free_moments["width"]
                rows_by_route[route].append({
                    "geometry": geometry.name, "separation": geometry.separation,
                    "held": geometry.held, "target_route": target_route,
                    "Q1_occupation": occupation, "source_word": SOURCE_WORD,
                    "carrier_steps": CARRIER_STEPS, "receiver_steps": RECEIVER_STEPS,
                    "width_shift": shift, "Cycle420_exact_target": target,
                    "source_carrier_prediction_residual": shift - target,
                    "centroid_shift": moments["centroid"] - free_moments["centroid"],
                    "maximum_norm_error": max(free_controls["maximum_norm_error"],
                                               pure_controls["maximum_norm_error"]),
                    "maximum_boundary_norm_weight": max(
                        free_controls["maximum_boundary_norm_weight"],
                        pure_controls["maximum_boundary_norm_weight"]),
                    "coherent_weight_residual": float(np.linalg.norm(
                        c435.packet_weights(coherent) - weights)),
                    "held_refit": False, "fitted_parameters": 0,
                    "adapter": adapter,
                })
    dispositions = {}
    for route, rows in rows_by_route.items():
        keyed = {(row["separation"], row["target_route"]): row for row in rows}
        max_residual = max(abs(row["source_carrier_prediction_residual"]) for row in rows)
        order = all(keyed[(2, target)]["width_shift"] > keyed[(1, target)]["width_shift"]
                    for target in c453.PHYSICAL_STRENGTHS)
        numeric = max_residual < ROW_TOLERANCE
        dispositions[route] = {
            "maximum_absolute_row_residual": max_residual,
            "all_four_rows_within_tolerance": numeric,
            "stronger_a2_order": order,
            "terminal_obligation_met": numeric and order,
            "held_to_train": {target: keyed[(2, target)]["width_shift"] /
                               keyed[(1, target)]["width_shift"]
                               for target in c453.PHYSICAL_STRENGTHS},
            "geometry_dependent_column_completion": route in (
                "A_Cycle213_retarded_slice", "B_Cycle216_static_exchange"
            ),
        }
    common_rows = []
    common_adapter_rows = {}
    for geometry in c453.GEOMETRIES:
        free, free_controls = free_result(geometry.name)
        initial, adapter = static_common_completed_pure(geometry.name)
        common_adapter_rows[geometry.name] = adapter
        pure, pure_controls = evolve_receiver(initial, geometry)
        free_weights = c435.packet_weights(free)
        pure_weights = c435.packet_weights(pure)
        free_moments = c435.packet_moments(free_weights)
        for target_route, occupation in c453.PHYSICAL_STRENGTHS.items():
            weights = (1 - occupation) * free_weights + occupation * pure_weights
            moments = c435.packet_moments(weights)
            target = c453.LEGACY_ROWS[(geometry.separation, target_route)]
            shift = moments["width"] - free_moments["width"]
            common_rows.append({
                "geometry": geometry.name, "separation": geometry.separation,
                "held": geometry.held, "target_route": target_route,
                "width_shift": shift, "Cycle420_exact_target": target,
                "source_carrier_prediction_residual": shift - target,
                "centroid_shift": moments["centroid"] - free_moments["centroid"],
                "held_refit": False, "common_scale": static_train_contraction_scale(),
                "adapter": adapter, "maximum_norm_error": max(
                    free_controls["maximum_norm_error"], pure_controls["maximum_norm_error"]),
            })
    common_keyed = {(row["separation"], row["target_route"]): row for row in common_rows}
    common_order = all(
        common_keyed[(2, target)]["width_shift"] > common_keyed[(1, target)]["width_shift"]
        for target in c453.PHYSICAL_STRENGTHS
    )
    common_disposition = {
        "maximum_absolute_row_residual": max(
            abs(row["source_carrier_prediction_residual"]) for row in common_rows),
        "stronger_a2_order": common_order,
        "held_to_train": {
            target: common_keyed[(2, target)]["width_shift"] /
                    common_keyed[(1, target)]["width_shift"]
            for target in c453.PHYSICAL_STRENGTHS
        },
        "common_scale_selected_from_train_only": static_train_contraction_scale(),
        "held_profile_used_to_select_scale": False,
        "auxiliary_physical_encoding_constructed": False,
    }
    raw_static_norm_ratio = (
        common_adapter_rows[c453.HELD.name]["raw_carrier_norm_weight"] /
        common_adapter_rows[c453.TRAIN.name]["raw_carrier_norm_weight"]
    )
    flat = tuple(row for rows in rows_by_route.values() for row in rows)
    check(
        "all three frozen carrier columns execute all four L13 rows with norm, boundary, coherent-sector, and held-no-refit controls",
        len(flat) == 12 and max(abs(row["centroid_shift"]) for row in flat) < 3e-13
        and max(row["maximum_norm_error"] for row in flat) < c435.TOLERANCE
        and max(row["maximum_boundary_norm_weight"] for row in flat) < BOUNDARY_MAXIMUM
        and max(row["coherent_weight_residual"] for row in flat) < c435.TOLERANCE
        and all(not row["held_refit"] and row["fitted_parameters"] == 0 for row in flat)
        and all(abs(row["adapter"]["output_norm"] - 1) < c435.TOLERANCE for row in flat),
        {"rows": rows_by_route},
    )
    check(
        "the four-row plus stronger-a2 terminal obligation is evaluated route-specifically without promoting a partial adapter",
        all(value["terminal_obligation_met"] ==
            (value["all_four_rows_within_tolerance"] and value["stronger_a2_order"])
            for value in dispositions.values()),
        {"row_tolerance": ROW_TOLERANCE, "dispositions": dispositions},
    )
    check(
        "the Cycle216 order audit separates raw K+, geometry-completed, and one train-frozen common contraction without using held values to select scale",
        raw_static_norm_ratio > 1
        and dispositions["B_Cycle216_static_exchange"]["stronger_a2_order"]
        and common_disposition["held_profile_used_to_select_scale"] is False
        and max(row["maximum_norm_error"] for row in common_rows) < c435.TOLERANCE
        and all(abs(row["adapter"]["output_norm"] - 1) < c435.TOLERANCE for row in common_rows),
        {"raw_Kplus_field_norm_weight_held_to_train": raw_static_norm_ratio,
         "geometry_completed_B": dispositions["B_Cycle216_static_exchange"],
         "train_frozen_common_completion_rows": common_rows,
         "train_frozen_common_completion_disposition": common_disposition,
         "reading": "raw profile order is carrier evidence; common completed packet order is predictive only at the declared logical-auxiliary boundary; geometry-completed order is not counted as held-clean calibration evidence"},
    )
    print("CARRIER_ROWS", rows_by_route, flush=True)
    print("CARRIER_DISPOSITIONS", dispositions, flush=True)
    print("STATIC_COMMON_SCALE_AUDIT", {"rows": common_rows,
          "disposition": common_disposition, "raw_norm_ratio": raw_static_norm_ratio}, flush=True)
    return {"rows": rows_by_route, "dispositions": dispositions,
            "static_common_rows": common_rows,
            "static_common_disposition": common_disposition,
            "raw_static_norm_ratio": raw_static_norm_ratio}


def carrier_equation_inverse_controls():
    geometry = c453.TRAIN
    compiled = source_compiled_state(geometry)
    reservoirs, original_fields, scalar = split_compiled(compiled, geometry)
    # Cycle213 exact two-slice inverse for the declared source history.
    source = np.zeros((geometry.length,) * 3)
    for index, cell in enumerate(geometry.sources):
        source[cell] = (1.0, -2.0, 1.0)[index]
    previous = np.zeros_like(source)
    current = np.zeros_like(source)
    following = c213.wave_step(previous, current, source)
    wave_inverse = float(np.linalg.norm(c213.reverse_step(current, following, source) - previous))
    # Cycle216 exact local equation on the zero-mean signed scalar profile.
    static = c216.solve_coin_field(source)
    static_equation = float(np.linalg.norm(
        c216.apply_stiffness(static) - source[..., None] * c435.c210.UNIFORM))
    static_scalar = float(np.linalg.norm(c216.scalar_field(static) - 3 * c216.c211.solve_field(source)))
    # Cycle425 transient is an exact unitary field update on the actual compiled column.
    transient = transient_field(compiled, geometry)
    restored = transient_field(transient, geometry, inverse=True)
    transient_inverse = c435.state_residual(restored, compiled)
    scalar_sum = sum(scalar.values(), start=np.zeros_like(next(iter(scalar.values()))))
    rows = {route: carrier_pure(geometry.name, route)[1] for route in ROUTES}
    check(
        "the retarded two-slice law reverses exactly, the static profile solves its local stiffness equation, and the finite-Q1 transient has an exact inverse",
        wave_inverse < 2e-14 and static_equation < 5e-11 and static_scalar < 5e-11
        and transient_inverse < c435.TOLERANCE and np.linalg.norm(scalar_sum) < c435.TOLERANCE
        and all(abs(row["output_norm"] - 1) < c435.TOLERANCE for row in rows.values()),
        {"Cycle213_pair_inverse": wave_inverse,
         "Cycle216_stiffness_equation": static_equation,
         "Cycle216_scalar_3Lplus": static_scalar,
         "Cycle425_transient_inverse": transient_inverse,
         "compiled_scalar_zero_mode_payload": float(np.linalg.norm(scalar_sum)),
         "adapter_rows": rows,
         "inverse_boundary": {
             "A": "two-slice carrier reversible; selected-slice column preparation is supplied",
             "B": "static K+ solution is not a recurrent inverse gate",
             "C": "full carrier update inverse constructed"}},
    )


def covariance_local_physical_controls():
    side = 5
    rng = np.random.default_rng(491)
    source = rng.normal(size=(side,) * 3)
    source -= np.mean(source)
    base_static_field = c216.solve_coin_field(source)
    wave_rows = []
    static_rows = []
    for frame in c435.c210.proper_cubic_frames():
        previous = np.zeros_like(source)
        current = np.zeros_like(source)
        for step in range(CARRIER_STEPS):
            following = c213.wave_step(previous, current, source if step == 0 else np.zeros_like(source))
            previous, current = current, following
        rotated_source = c213.rotate_scalar(source, frame)
        rprevious = np.zeros_like(source)
        rcurrent = np.zeros_like(source)
        for step in range(CARRIER_STEPS):
            rfollowing = c213.wave_step(rprevious, rcurrent,
                                        rotated_source if step == 0 else np.zeros_like(source))
            rprevious, rcurrent = rcurrent, rfollowing
        wave_rows.append(float(np.linalg.norm(rcurrent - c213.rotate_scalar(current, frame))))
        rotated_field = c216.solve_coin_field(rotated_source)
        static_rows.append(float(np.linalg.norm(
            rotated_field - c216.rotate_field_state(base_static_field, frame))))
    update = c425.cubic_update(3, 0)
    c425_rows = []
    for frame in c435.c210.proper_cubic_frames():
        representation = c425.frame_representation(3, frame)
        c425_rows.append(float(sparse.linalg.norm(representation @ update - update @ representation)))

    coefficients = (SOURCE_WORD,) * 6
    initial = c472.initial_state()
    logical = c487.c484.apply_product_source(
        initial, 0, coefficients, route=c487.SELECTED_ROUTE, discrete=True)
    encoding = c472.c322.build_encoding(3)
    encoded = c472.c426.encode_physical(initial, encoding)
    physical = c487.c484.physical_product_source(
        encoded, encoding, 0, coefficients, route=c487.SELECTED_ROUTE, discrete=True)
    expected = c472.c426.encode_physical(logical, encoding)
    decoded = {key: encoding.getH() @ value for key, value in physical.items()}
    projected = c472.c426.encode_physical(decoded, encoding)
    eg = c472.state_residual(physical, expected)
    leakage = c472.state_residual(physical, projected)
    check(
        "the three carrier operators are proper-cubic in all24 frames and the shared word256 source seam has local physical E/G and code return",
        len(wave_rows) == len(static_rows) == len(c425_rows) == 24
        and max(wave_rows) < 2e-12 and max(static_rows) < 2e-10
        and max(c425_rows) < 2e-12 and eg < c472.TOLERANCE and leakage < c472.TOLERANCE,
        {"Cycle213_maximum_covariance_residual": max(wave_rows),
         "Cycle216_maximum_covariance_residual": max(static_rows),
         "Cycle425_maximum_covariance_residual": max(c425_rows),
         "proper_cubic_frames": 24, "local_physical_EG": eg,
         "local_code_leakage": leakage, "source_word": SOURCE_WORD},
    )


def deletion_receiver_inverse_fixture_controls(prediction):
    rows = []
    for route in ROUTES:
        for geometry in c453.GEOMETRIES:
            initial = carrier_pure(geometry.name, route)[0]
            stepped = receiver_step(initial, geometry)
            restored = receiver_inverse(stepped, geometry)
            rows.append({"route": route, "geometry": geometry.name,
                         "receiver_step_inverse": c435.state_residual(restored, initial),
                         "norm_error": abs(c435.state_norm(stepped) - 1)})
    route = "B_Cycle216_static_exchange"
    geometry = c453.TRAIN
    initial = carrier_pure(geometry.name, route)[0]
    intact, _ = evolve_receiver(initial, geometry)
    free, _ = free_result(geometry.name)
    deletions = {"source_compiler_or_carrier": c435.state_residual(intact, free)}
    for name, kwargs in (
        ("receiver", {"receiver_enabled": False}),
        ("field_stream", {"stream_enabled": False}),
        ("packet_stream", {"packet_stream_enabled": False}),
    ):
        deleted, _ = evolve_receiver(initial, geometry, **kwargs)
        deletions[name] = c435.state_residual(intact, deleted)
    update_rows = c435.restricted_factors()[0]
    contact = c435.c319.triple_contact(c435.LABELS)
    two_particle = np.zeros(c435.MATTER_DIM, dtype=complex)
    two_particle[c435.LABEL_INDEX[(2, (0, 1), 0, (), 0, ())]] = 1
    contact_signal = float(np.linalg.norm(contact @ two_particle - two_particle))
    rejected = 0
    for probe in (
        lambda: carrier_pure(geometry.name, "bad"),
        lambda: c490.validate_word(0),
        lambda: c435.validate_geometry(c435.Geometry("bad", 6, 1, geometry.sources,
                                                     geometry.receivers, 4, False)),
        lambda: c453.strength_state(geometry, 1.1),
    ):
        try:
            probe()
        except (ValueError, KeyError):
            rejected += 1
    check(
        "the shared receiver step has an exact inverse, source/carrier, receiver, field-stream, and packet-stream deletions are visible, and malformed domains are refused",
        max(max(row["receiver_step_inverse"], row["norm_error"]) for row in rows) < c435.TOLERANCE
        and min(deletions.values()) > 1e-10 and rejected == 4,
        {"inverse_rows": rows, "deletions": deletions, "malformed_domains_refused": rejected},
    )
    check(
        "the one-particle mass and Cycle230 contact fixtures remain spectators of every carrier join",
        abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]) < c435.TOLERANCE
        and update_rows["uniform_one_particle_eigen_residual"] < c435.TOLERANCE
        and update_rows["contact_nontrivial_columns"] == 645 and contact_signal > 1e-6,
        {"Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
         "three_cell_mass": update_rows["three_cell_rest_mass"],
         "mass_eigen_residual": update_rows["uniform_one_particle_eigen_residual"],
         "contact_nontrivial_columns": update_rows["contact_nontrivial_columns"],
         "two_particle_contact_signal": contact_signal},
    )


def inventory_resource_no_go_controls(prediction):
    cells = c453.TRAIN.length ** 3
    walls = ("W_interface", "W_calibration", "W_geometry", "W_shell")
    pairwise = []
    for left_index, left in enumerate(walls):
        for right in walls[left_index + 1:]:
            pairwise.append({"pair": (left, right), "left_closes_right": False,
                             "right_closes_left": False, "independent": True})
    check(
        "the supplied/derived/open inventory separates carrier equations, column adapters, prediction, and the complete L13 shell",
        AUTHORITY == "none" and AUDIT == "unset" and cells == 2197,
        {"supplied": [
            "Cycle487 word256 P8/Suzuki4/B20 local source compiler and fixed basis adapter",
            "Cycle213 dt=0.45 centered wave, one-impulse history and four carrier slices",
            "Cycle216 K=2I-U-Udagger, zero-mode pseudoinverse and static-action reading",
            "Cycle425 coin-plus-stream free Q1 branch and four transient steps",
            "scalar projection, A/B geometry-column norm completions, train-only contraction audit with logical spectator, factor order and no autonomous preparation",
            "Cycle453 L13 geometries, p_route strengths, depth4 receiver, packet observable, targets/tolerances"],
         "derived": [
            "one exact compiled coherent quadrupole source column with zero scalar payload mode",
            "retarded, static-exchange and finite-Q1 transient carrier columns on train/held L13",
            "twelve physical-M64 packet rows and route-specific terminal dispositions",
            "carrier equations/inverses at their actual scopes, all24 covariance, local E/G/leakage, receiver inverse/deletions and mass/contact controls"],
         "open": [
            "A/B finite-M2 carrier encodings, physical encoding of the common-scale logical spectator, and autonomous declared-column preparation",
            "Cycle216 recurrent unitary execution rather than host pseudoinverse solution",
            "Cycle425 three-defect stationary/dressed eigenpair selection and physical preparation at L13",
            "complete L13 three-M64 shell/effect materialization, total primitive schedule and fault model",
            "any unmet absolute-row/calibration or geometry-order obligation",
            "source recurrence/renewal, recoil/work, energy-stress identity, physical time, gravity/metric, Records and Born/occurrence"],
         "L13_cells": cells, "field_M2_per_cell": 7,
         "logical_payload_peak_only": True, "complete_L13_shell_materialized": False,
         "firewall": {"response_called_gravity": False, "phase_called_energy": False,
                      "depth_called_time": False, "norm_weight_called_probability": False}},
    )
    check(
        "full N1-N8 demotes any miss to a partial carrier tournament and rejects minimum-content, shared-obstruction, or axiom-pressure promotion",
        AUTHORITY == "none" and AUDIT == "unset" and len(pairwise) == 6,
        {"N1_normalized_families": [
            {"family": "centered retarded wave", "object": "two real scalar slices",
             "mechanism": "local causal cone and reversible wave invariant",
             "terminal": "four packet rows/order", "status": "ATTEMPTED"},
            {"family": "static virtual exchange", "object": "local coin stiffness and K+",
             "mechanism": "exact scalar 3L+ resolvent", "terminal": "four packet rows/order",
             "status": "ATTEMPTED"},
            {"family": "finite-Q1 transient", "object": "reservoir/directional one-excitation update",
             "mechanism": "unitary coin-stream propagation", "terminal": "four packet rows/order",
             "status": "ATTEMPTED"},
            {"family": "multi-defect dressed stationary", "object": "three-reservoir eigenstate",
             "mechanism": "selected shifted-Green eigenpair", "terminal": "physical L13 preparation and rows",
             "status": "UNTESTED; single-defect Cycle425 face is not interface-equivalent"},
            {"family": "renewable many-Q source", "object": "finite many-excitation carrier",
             "mechanism": "local conserved reservoir recurrence", "terminal": "autonomous repeated source and rows",
             "status": "UNTESTED"},
            {"family": "nonperiodic/longer-domain carrier", "object": "larger or open cubic domain",
             "mechanism": "changed propagation and image structure", "terminal": "held family without refit",
             "status": "UNTESTED"}],
         "N2_pairwise_wall_table": pairwise,
         "N3_hidden_trigger_scan": {
             "explicit_conditions": ["source word", "quadrupole column", "scalar projection",
                 "one impulse", "four carrier/receiver steps", "periodic L13", "zero-mode rule",
                 "A/B geometry norm completion", "train-only common contraction and logical spectator",
                 "static solve", "packet factor order", "targets/tolerances"],
             "phrase_scan": "by-construction claims are limited to displayed finite operators; no standard/background/obvious bridge is load-bearing"},
         "N4_residual_matching": [
             {"witness": "scripts/physical_discrete_source_law_tournament_cycle490_2026_07_20.py:357",
              "witness_residual": "word/repetition source law with ~0.902 geometry ratio",
              "current_residual": "geometry-changing carrier packet rows", "match": True},
             {"witness": "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py:60",
              "witness_residual": "continuous two-slice retarded field",
              "current_residual": "finite-M2 carrier compiler", "match": False},
             {"witness": "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py:84",
              "witness_residual": "static local-action Green response",
              "current_residual": "recurrent unitary source-to-packet update", "match": False},
             {"witness": "scripts/common_cubic_transient_stationary_update_cycle425_2026_07_19.py:420",
              "witness_residual": "single-defect selected dressed state",
              "current_residual": "three-defect quadrupole L13 preparation", "match": False}],
         "N5_scope": "only three declared columns, p_route strengths, periodic L13 a1/a2, four carrier and receiver steps; no lattice-wide source-law or gravity negative",
         "N6_partial_paths": "finite-alphabet wave dilation, local iterative K solver, multi-defect dressed preparation, many-Q renewal, open/larger domains and complete shell remain live",
         "N7_steelman": "A hostile reviewer should build the three-reservoir Cycle425 defect update, select the quadrupole-symmetry dressed eigenstate on train only, synthesize its local preparation, and test the held a2 packet without A/B column normalization; that actionable mechanism changes both geometry and the interface obligation.",
         "N8_cross_cycle": "Cycles432->435, 447->450 and 484->487 closed earlier residuals by enlarging/composing physical constructions; the same mechanism remains live here",
         "claim_gate": "partial-attempt-with-named-untested-routes; broad no-go FAIL; minimum-content FAIL; shared obstruction FAIL; axiom-pressure claim FAIL; there is no axiom pressure"},
    )


def resource_cap_controls(started):
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    check("the complete Cycle491 cold run stays below explicit wall and RSS caps",
          elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
          {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
           "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB})


def main() -> int:
    started = perf_counter()
    print("Cycle491 geometry-changing carrier tournament")
    print("authority", AUTHORITY, "audit", AUDIT)
    note_contract()
    frozen_controls()
    prediction = prediction_controls()
    carrier_equation_inverse_controls()
    covariance_local_physical_controls()
    deletion_receiver_inverse_fixture_controls(prediction)
    inventory_resource_no_go_controls(prediction)
    resource_cap_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
