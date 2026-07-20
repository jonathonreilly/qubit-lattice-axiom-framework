#!/usr/bin/env python3
"""Cycle 487: discrete full-layer quadrupole exact-strength bridge.

Replace Cycle453's continuous coefficient-two source/receiver vertex by the
Cycle484 training-selected P8/Suzuki4/B20 physical update.  The fixed local
reservoir/direction basis adapter is explicit.  Prediction residuals remain
separate from coefficient, product-formula, angle, routing, and compiler E/G
residuals.  Response is not gravity, phase is not energy, a generator is not
a rate, and schedule depth is not time.  Authority none; audit unset.
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
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_exact_strength_quadrupole_prediction_bridge_cycle453_2026_07_19 as c453
import physical_full_layer_discrete_response_composition_cycle484_2026_07_19 as c484


c435 = c453.c435
c420 = c453.c420
c480 = c484.c480
c476 = c484.c476
c472 = c484.c472

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DISCRETE_QUADRUPOLE_EXACT_STRENGTH_BRIDGE_CYCLE487_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
SELECTED_ROUTE = "suzuki4"
RETAINED_ROUTE = "direct-strang8"
UNIFORM_WORDS = (1, 1, 1, 1, 1, 1)
UNIFORM_COEFFICIENTS = (256, 256, 256, 256, 256, 256)
PREDICTION_TOLERANCE = c453.NUMERIC_ROW_TOLERANCE
RATIO_TOLERANCE = c453.STRENGTH_RATIO_RELATIVE_TOLERANCE
SIGNAL_FLOOR = c453.SIGNAL_FLOOR
WALL_CAP_SECONDS = 700.0
RSS_CAP_MIB = 3072.0
PASS = 0
FAIL = 0

FROZEN = {
    "Cycle420": (
        "physical_source_prediction_bridge_contract_cycle420_2026_07_19.py",
        "79eca68ca217277fa237d2420888b64ef7bfba801e8745925a8dfb14b7576d5c",
    ),
    "Cycle435": (
        "physical_quadrupole_packet_width_bridge_cycle435_2026_07_19.py",
        "d0682c388411e3f2c4547e4703214ce70831382e12fe154da9a5349944a07ff7",
    ),
    "Cycle453": (
        "physical_exact_strength_quadrupole_prediction_bridge_cycle453_2026_07_19.py",
        "dd3004fe92203651fd7fe732d1253d49379b52075bd88159fa7712154c0f8557",
    ),
    "Cycle480": (
        "physical_discrete_angle_product_compiler_cycle480_2026_07_19.py",
        "39f2fb1c9d3e10bf8741b6f426bc0a7dbbd75dea7c4c66aedc75b8d8275fb743",
    ),
    "Cycle481": (
        "physical_full_layer_fixed_p_response_composition_cycle481_2026_07_19.py",
        "7155a82ca672f36f11791cd771515e5039970dec400293dd4e1c4e30e6e3ee13",
    ),
    "Cycle484": (
        "physical_full_layer_discrete_response_composition_cycle484_2026_07_19.py",
        "7551a61dd61292cbeab685b55475e6d63c5223a9185891b4605fc7bcf151a86f",
    ),
}

# Cycle453's frozen continuous-vertex outputs, not fit by this cycle.
CYCLE453_OBSERVED = {
    (1, "unit_weight"): 4.846405339820059e-7,
    (1, "coefficient_two"): 2.4438685030658824e-6,
    (2, "unit_weight"): 4.3751148665061024e-7,
    (2, "coefficient_two"): 2.20621558276457e-6,
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
        "authority: none", "audit: unset", "cycle 487",
        "cycle453 exact targets", "cycle484 p8/suzuki4/b20",
        "fixed reservoir/direction basis adapter", "no observable adapter",
        "train l13/a1/depth4", "held l13/a2/depth4", "held rows do not refit",
        "coefficient quantization", "product-formula", "discrete-angle",
        "compiler e/g", "source-law/prediction residual", "quadrupole strength ratio",
        "stronger a=2 order", "l13 physical-shell resource boundary",
        "all 24 proper-cubic frames", "one-particle mass", "cycle-230 contact",
        "response is not gravity", "phase is not energy", "generator is not a rate",
        "depth is not time", "partial-attempt-with-named-untested-routes",
        "n1 — alternative route enumeration", "n8 — cross-cycle echo and claim gate",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in normalized(NOTE))
    check("the Cycle487 note freezes the discrete exact-strength bridge and N1-N8 scope", not missing, missing)


def frozen_controls() -> None:
    observed = {
        name: file_sha(ROOT / "scripts" / filename)
        for name, (filename, _expected) in FROZEN.items()
    }
    expected = {name: digest for name, (_filename, digest) in FROZEN.items()}
    check(
        "Cycles420/435/453/480/481/484 remain frozen at exact input identities",
        observed == expected,
        {"observed": observed, "expected": expected},
    )


@lru_cache(maxsize=1)
def q1_basis_adapter() -> np.ndarray:
    """Map Cycle484 order (d0..d5,R) to Cycle453 order (R,d0..d5)."""

    adapter = np.zeros((448, 448), dtype=complex)
    q1_index = c476.c426.LOCAL_STATE_INDEX[1]
    for matter in range(64):
        adapter[7 * matter, 7 * matter + q1_index[64]] = 1
        for direction in range(6):
            adapter[7 * matter + 1 + direction, 7 * matter + q1_index[1 << direction]] = 1
    return adapter


@lru_cache(maxsize=None)
def local_vertex(route: str, discrete: bool, inverse: bool = False) -> np.ndarray:
    identity = np.eye(448, dtype=complex)
    native = c480.product_action(
        identity, UNIFORM_COEFFICIENTS, route=route, discrete=discrete,
        inverse=inverse,
    )
    adapter = q1_basis_adapter()
    return adapter @ native @ adapter.conj().T


def exact_p8_vertex() -> np.ndarray:
    vector = np.asarray(UNIFORM_COEFFICIENTS, dtype=float) / c476.COEFFICIENT_SCALE
    native = c480.expm_multiply(
        1j * c476.c426.ANGLE * c476.coefficient_generator(vector),
        np.eye(448, dtype=complex),
    )
    adapter = q1_basis_adapter()
    return adapter @ native @ adapter.conj().T


def compiler_residual_controls() -> dict[str, float]:
    print("\nFIXED BASIS ADAPTER / P8 / SUZUKI4 / B20")
    adapter = q1_basis_adapter()
    exact = c435.c322.local_source_blocks(c435.c322.ANGLE)[1]
    p8 = exact_p8_vertex()
    product = local_vertex(SELECTED_ROUTE, False)
    discrete = local_vertex(SELECTED_ROUTE, True)
    identity = np.eye(448, dtype=complex)
    residuals = {
        "adapter_unitarity": float(np.linalg.norm(adapter.conj().T @ adapter - identity, 2)),
        "coefficient_quantization": float(np.linalg.norm(p8 - exact, 2)),
        "product_formula": float(np.linalg.norm(product - p8, 2)),
        "discrete_angle": float(np.linalg.norm(discrete - product, 2)),
        "compiler_total": float(np.linalg.norm(discrete - exact, 2)),
        "inverse": float(np.linalg.norm(local_vertex(SELECTED_ROUTE, True, True) @ discrete - identity, 2)),
        "unitarity": float(np.linalg.norm(discrete.conj().T @ discrete - identity, 2)),
    }
    check(
        "the fixed local adapter makes uniform P8 exact and keeps product, B20 angle, total, inverse, and unitarity residuals separate",
        c476.expected_coefficients(UNIFORM_WORDS) == UNIFORM_COEFFICIENTS
        and residuals["adapter_unitarity"] < c480.TOLERANCE
        and residuals["coefficient_quantization"] < c480.TOLERANCE
        and residuals["product_formula"] < c480.PRODUCT_ERROR_CAP
        and residuals["discrete_angle"] < c480.ANGLE_ERROR_CAP
        and residuals["compiler_total"] < c480.STATE_ERROR_CAP
        and residuals["inverse"] < c480.TOLERANCE
        and residuals["unitarity"] < c480.TOLERANCE,
        {
            "uniform_words": UNIFORM_WORDS,
            "P8_coefficients": UNIFORM_COEFFICIENTS,
            "Cycle453_exact_angle": c435.c322.ANGLE,
            "basis_order_Cycle484": "direction0..direction5,reservoir",
            "basis_order_Cycle453": "reservoir,direction0..direction5",
            "observable_adapter_required": False,
            "residuals": residuals,
        },
    )
    return residuals


def _restricted_from_local(group: str, cell_index: int, vertex: np.ndarray) -> sparse.csc_matrix:
    if group not in ("source", "receiver") or cell_index not in range(3):
        raise ValueError("vertex group/cell leaves the Cycle453 block")
    global_indices = c435.SOURCE_INDICES if group == "source" else c435.RECEIVER_INDICES
    labels = c435.SOURCE_LABELS if group == "source" else c435.RECEIVER_LABELS
    restricted_index = {global_index: local for local, global_index in enumerate(global_indices)}
    rows: list[int] = []
    columns: list[int] = []
    data: list[complex] = []
    for matter_source, label in enumerate(labels):
        specs = list(c435.c396.c319.label_specs(label))
        local_source = c435.c396.LOCAL_SPEC_INDEX[specs[cell_index]]
        for q_source in range(7):
            vertex_column = 7 * local_source + q_source
            for target in np.flatnonzero(abs(vertex[:, vertex_column]) > 2e-14):
                local_target, q_target = divmod(int(target), 7)
                target_specs = list(specs)
                target_specs[cell_index] = c435.c322.LOCAL_LABELS[local_target]
                target_label = tuple(item for spec in target_specs for item in spec)
                global_target = c435.LABEL_INDEX[target_label]
                rows.append(7 * restricted_index[global_target] + q_target)
                columns.append(7 * matter_source + q_source)
                data.append(vertex[target, vertex_column])
    dimension = 7 * len(labels)
    return sparse.coo_matrix(
        (data, (rows, columns)), shape=(dimension, dimension), dtype=complex
    ).tocsc()


@lru_cache(maxsize=None)
def restricted_discrete_vertex(group: str, cell_index: int, inverse: bool = False):
    return _restricted_from_local(
        group, cell_index, local_vertex(SELECTED_ROUTE, True, inverse)
    )


def embedding_controls() -> None:
    rows = []
    for group in ("source", "receiver"):
        for cell_index in range(3):
            inherited = c435.restricted_vertex(group, cell_index)
            rebuilt = _restricted_from_local(
                group, cell_index, c435.c322.local_source_blocks(c435.c322.ANGLE)[1]
            )
            difference = rebuilt - inherited
            rows.append({
                "group": group,
                "cell": cell_index,
                "continuous_embedding_max_abs": (
                    float(max(abs(difference.data))) if difference.nnz else 0.0
                ),
                "discrete_shape": restricted_discrete_vertex(group, cell_index).shape,
            })
    check(
        "the adapter embeds the discrete vertex into all six actual Cycle453 source/receiver factors without an observable remap",
        max(row["continuous_embedding_max_abs"] for row in rows) < 2e-14,
        {"rows": rows, "packet_observable": "unchanged Cycle435 packet_weights/packet_moments"},
    )


def apply_discrete_vertex(
    state: c435.MatterState, geometry: c435.Geometry, group: str, cell_index: int,
    *, inverse: bool = False, enabled: bool = True,
) -> c435.MatterState:
    if not enabled:
        return {key: value.copy() for key, value in state.items()}
    cell = geometry.sources[cell_index] if group == "source" else geometry.receivers[cell_index]
    active = c435.vertex_keys(cell, geometry.length)
    zero = np.zeros((c435.SOURCE_DIM, c435.RECEIVER_DIM), dtype=complex)
    packed = np.stack([state.get(key, zero) for key in active], axis=2)
    transformed = np.empty_like(packed)
    operator = restricted_discrete_vertex(group, cell_index, inverse)
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


def discrete_logical_step(
    state: c435.MatterState, geometry: c435.Geometry, *,
    source_enabled: bool = True, receiver_enabled: bool = True,
    stream_enabled: bool = True, packet_stream_enabled: bool = True,
    contact_enabled: bool = True,
) -> c435.MatterState:
    c435.validate_geometry(geometry)
    _rows, source_coin, receiver_coin, source_contact, receiver_contact, first, second = c435.restricted_factors()
    output = c435.apply_matter(state, source_coin, receiver_coin)
    output = c435.field_coin(output, geometry.length)
    for cell_index in range(3):
        output = apply_discrete_vertex(output, geometry, "source", cell_index, enabled=source_enabled)
    for cell_index in range(3):
        output = apply_discrete_vertex(output, geometry, "receiver", cell_index, enabled=receiver_enabled)
    if packet_stream_enabled:
        output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), first)
        output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), second)
    output = c435.field_stream(output, geometry.length, enabled=stream_enabled)
    if contact_enabled:
        output = c435.apply_matter(output, source_contact, receiver_contact)
    return output


def discrete_logical_inverse(state: c435.MatterState, geometry: c435.Geometry) -> c435.MatterState:
    _rows, source_coin, receiver_coin, source_contact, receiver_contact, first, second = c435.restricted_factors()
    output = c435.apply_matter(state, source_contact.getH(), receiver_contact.getH())
    output = c435.field_stream(output, geometry.length, inverse=True)
    output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), second.getH())
    output = c435.apply_matter(output, sparse.eye(c435.SOURCE_DIM, format="csc"), first.getH())
    for cell_index in (2, 1, 0):
        output = apply_discrete_vertex(output, geometry, "receiver", cell_index, inverse=True)
    for cell_index in (2, 1, 0):
        output = apply_discrete_vertex(output, geometry, "source", cell_index, inverse=True)
    output = c435.field_coin(output, geometry.length, inverse=True)
    return c435.apply_matter(output, source_coin.getH(), receiver_coin.getH())


def boundary_norm_weight(state: c435.MatterState, geometry: c435.Geometry) -> float:
    total = 0.0
    for key, value in state.items():
        cell = c453.field_cell(key, geometry.length)
        if cell is not None and any(coord in (0, geometry.length - 1) for coord in cell):
            total += float(np.vdot(value, value).real)
    return total


def evolve_trace(state: c435.MatterState, geometry: c435.Geometry, **kwargs):
    output = state
    maximum_boundary_norm_weight = boundary_norm_weight(output, geometry)
    maximum_norm_error = abs(c435.state_norm(output) - 1)
    maximum_keys = len(output)
    maximum_bytes = sum(value.nbytes for value in output.values())
    for _ in range(geometry.depth):
        output = discrete_logical_step(output, geometry, **kwargs)
        maximum_boundary_norm_weight = max(
            maximum_boundary_norm_weight, boundary_norm_weight(output, geometry)
        )
        maximum_norm_error = max(maximum_norm_error, abs(c435.state_norm(output) - 1))
        maximum_keys = max(maximum_keys, len(output))
        maximum_bytes = max(maximum_bytes, sum(value.nbytes for value in output.values()))
    return output, {
        "maximum_boundary_norm_weight": maximum_boundary_norm_weight,
        "maximum_norm_error": maximum_norm_error,
        "maximum_active_field_keys": maximum_keys,
        "maximum_logical_payload_bytes": maximum_bytes,
    }


def prediction_controls(compiler_residuals: dict[str, float]) -> dict[str, object]:
    print("\nACTUAL CYCLE453 DISCRETE L13 PREDICTIONS")
    summaries = []
    states = {}
    for geometry in c453.GEOMETRIES:
        free_state, free_controls = evolve_trace(c435.vacuum_state(), geometry)
        pure_state, pure_controls = evolve_trace(c435.quadrupole_state(geometry), geometry)
        free_weights = c435.packet_weights(free_state)
        pure_weights = c435.packet_weights(pure_state)
        sector_key_overlap = len(set(free_state) & set(pure_state))
        free = c435.packet_moments(free_weights)
        pure = c435.packet_moments(pure_weights)
        rows = []
        for route, occupation in c453.PHYSICAL_STRENGTHS.items():
            weights = (1 - occupation) * free_weights + occupation * pure_weights
            coherent_output = c435.combine(
                (free_state, pure_state),
                np.asarray((np.sqrt(1 - occupation), np.sqrt(occupation)), dtype=complex),
            )
            coherent_output_weights = c435.packet_weights(coherent_output)
            moments = c435.packet_moments(weights)
            target = c453.LEGACY_ROWS[(geometry.separation, route)]
            prior = CYCLE453_OBSERVED[(geometry.separation, route)]
            shift = moments["width"] - free["width"]
            rows.append({
                "route": route,
                "held": geometry.held,
                "Q1_occupation": occupation,
                "width_shift": shift,
                "Cycle453_continuous_width_shift": prior,
                "compiler_induced_width_delta": shift - prior,
                "Cycle420_exact_target": target,
                "source_law_prediction_residual": shift - target,
                "centroid_shift": moments["centroid"] - free["centroid"],
                "boundary_norm_weight_upper_bound": (
                    (1 - occupation) * free_controls["maximum_boundary_norm_weight"]
                    + occupation * pure_controls["maximum_boundary_norm_weight"]
                ),
                "refit": False,
                "coherent_output_weight_residual": float(
                    np.linalg.norm(coherent_output_weights - weights)
                ),
            })
        summaries.append({
            "geometry": asdict(geometry), "free": free, "pure": pure,
            "free_controls": free_controls, "pure_controls": pure_controls,
            "Q0_Q1_output_key_overlap": sector_key_overlap,
            "rows": rows,
        })
        states[geometry.name] = {"free": free_state, "pure": pure_state}

    by_key = {
        (summary["geometry"]["separation"], row["route"]): row
        for summary in summaries for row in summary["rows"]
    }
    ratio_target = c420.ROUTE_STRENGTHS["coefficient_two"] / c420.ROUTE_STRENGTHS["unit_weight"]
    ratios = {
        separation: by_key[(separation, "coefficient_two")]["width_shift"]
        / by_key[(separation, "unit_weight")]["width_shift"]
        for separation in (1, 2)
    }
    held_to_train = {
        route: by_key[(2, route)]["width_shift"] / by_key[(1, route)]["width_shift"]
        for route in c453.PHYSICAL_STRENGTHS
    }
    maximum_row_residual = max(abs(row["source_law_prediction_residual"]) for row in by_key.values())
    maximum_compiler_delta = max(abs(row["compiler_induced_width_delta"]) for row in by_key.values())
    telescoping_state_bound = 6 * c453.TRAIN.depth * compiler_residuals["compiler_total"]
    check(
        "the discrete update preserves centered resolved train/held rows, exact strength-ratio scaling, norm, boundary, and no-refit controls",
        min(row["width_shift"] for row in by_key.values()) > SIGNAL_FLOOR
        and max(abs(row["centroid_shift"]) for row in by_key.values()) < 3e-13
        and max(abs(value / ratio_target - 1) for value in ratios.values()) < RATIO_TOLERANCE
        and max(summary["pure_controls"]["maximum_norm_error"] for summary in summaries) < c435.TOLERANCE
        and max(row["boundary_norm_weight_upper_bound"] for row in by_key.values()) < c453.BOUNDARY_MAXIMUM
        and max(row["coherent_output_weight_residual"] for row in by_key.values()) < c435.TOLERANCE
        and all(summary["Q0_Q1_output_key_overlap"] == 0 for summary in summaries)
        and all(not row["refit"] for row in by_key.values()),
        {"rows": by_key, "strength_ratio_target": ratio_target,
         "discrete_strength_ratios": ratios, "held_to_train": held_to_train},
    )
    check(
        "the compiler perturbation is bounded separately and does not repair the four absolute Cycle420 rows or stronger-a2 order",
        maximum_compiler_delta < telescoping_state_bound
        and maximum_row_residual > PREDICTION_TOLERANCE
        and all(held_to_train[route] < 1 for route in held_to_train),
        {"maximum_compiler_induced_width_delta": maximum_compiler_delta,
         "telescoping_state_bound": telescoping_state_bound,
         "maximum_source_law_prediction_residual": maximum_row_residual,
         "numeric_row_tolerance": PREDICTION_TOLERANCE,
         "stronger_a2_reproduced": False, "held_to_train": held_to_train,
         "classification": "law/calibration/finite-domain evidence; not compiler obstruction"},
    )
    print("PREDICTION ROWS", summaries, flush=True)
    return {"summaries": summaries, "states": states, "by_key": by_key,
            "ratios": ratios, "held_to_train": held_to_train,
            "maximum_compiler_delta": maximum_compiler_delta}


def inverse_controls() -> None:
    rows = []
    for geometry in c453.GEOMETRIES:
        initial = c453.strength_state(
            geometry, c453.PHYSICAL_STRENGTHS["coefficient_two"]
        )
        stepped = discrete_logical_step(initial, geometry)
        restored = discrete_logical_inverse(stepped, geometry)
        rows.append({
            "geometry": geometry.name,
            "inverse": c435.state_residual(restored, initial),
            "norm_error": abs(c435.state_norm(stepped) - 1),
        })
    check(
        "the actual Cycle453 discrete train/held logical factors have exact adjoint return and no norm leakage",
        max(max(row["inverse"], row["norm_error"]) for row in rows) < c435.TOLERANCE,
        rows,
    )


def physical_eg_controls() -> None:
    coefficients = UNIFORM_COEFFICIENTS
    initial = c472.initial_state()
    logical = c484.apply_product_source(
        initial, 0, coefficients, route=SELECTED_ROUTE, discrete=True
    )
    encoding = c472.c322.build_encoding(3)
    encoded = c472.c426.encode_physical(initial, encoding)
    physical = c484.physical_product_source(
        encoded, encoding, 0, coefficients, route=SELECTED_ROUTE, discrete=True
    )
    expected = c472.c426.encode_physical(logical, encoding)
    decoded = {key: encoding.getH() @ value for key, value in physical.items()}
    projected = c472.c426.encode_physical(decoded, encoding)
    eg = c472.state_residual(physical, expected)
    leakage = c472.state_residual(physical, projected)
    check(
        "the uniform P8/Suzuki4/B20 actuation satisfies physical E/G and code return before prediction interpretation",
        eg < c472.TOLERANCE and leakage < c472.TOLERANCE,
        {"EG": eg, "code_leakage": leakage, "encoding_columns": encoding.shape[1],
         "off_code_completion": "identity", "scope": "one local q1 source-star actuation"},
    )


def covariance_controls() -> None:
    identity = np.eye(448, dtype=complex)
    base_native = c480.product_action(
        identity, UNIFORM_COEFFICIENTS, route=SELECTED_ROUTE, discrete=True
    )
    maximum = 0.0
    digests = []
    for frame in c484.c463.proper_cubic_frames():
        matrix = np.asarray(frame, dtype=int)
        mapping = c472.direction_map(matrix)
        representation = c472.c426.recoil_frame(1, matrix)
        carried = c480.product_action(
            identity, UNIFORM_COEFFICIENTS, route=SELECTED_ROUTE, discrete=True,
            direction_order=tuple(mapping),
        )
        maximum = max(maximum, float(np.max(abs(carried - representation @ base_native @ representation.getH()))))
        digest = sha256()
        digest.update(repr(frame).encode())
        digest.update(f"{mapping}|uniform-P8|S4|B20|no-resort".encode())
        digests.append(digest.hexdigest())
    check(
        "the full local discrete operator and structural schedule carry through all 24 proper-cubic frames without resort",
        len(digests) == 24 and len(set(digests)) == 24 and maximum < c480.TOLERANCE,
        {"proper_cubic_frames": 24, "maximum_full_operator_covariance_residual": maximum,
         "scope": "full 448-dimensional local operator; L13 rotated width rows are inherited, not rerun",
         "frame_manifests": digests},
    )


def deletion_domain_mass_contact_controls() -> None:
    identity = np.eye(448, dtype=complex)
    intact = c480.product_action(
        identity, UNIFORM_COEFFICIENTS, route=SELECTED_ROUTE, discrete=True
    )
    factors = c480.factor_list(SELECTED_ROUTE, tuple(range(6)))
    quantum = c480.product_action(
        identity, UNIFORM_COEFFICIENTS, route=SELECTED_ROUTE, discrete=True,
        delete_one_quantum=(0, factors[0][1]),
    )
    bit = c480.product_action(
        identity, UNIFORM_COEFFICIENTS, route=SELECTED_ROUTE, discrete=True,
        omit_bit=(0, 8),
    )
    factor = c480.product_action(
        identity, UNIFORM_COEFFICIENTS, route=SELECTED_ROUTE, discrete=True,
        omit_factor=0,
    )
    deletions = {
        "local_source_flag": float(np.linalg.norm(intact - identity)),
        "one_Z20_quantum": float(np.linalg.norm(intact - quantum)),
        "one_coefficient_bit_family": float(np.linalg.norm(intact - bit)),
        "one_Suzuki_factor": float(np.linalg.norm(intact - factor)),
        "quadrupole_sign_column": float(np.linalg.norm(
            c435.QUADRUPOLE - np.asarray((1, 2, 1), dtype=complex) / np.sqrt(6)
        )),
    }
    rejected = 0
    probes = (
        lambda: _restricted_from_local("bad", 0, intact),
        lambda: _restricted_from_local("source", 3, intact),
        lambda: c480.product_action(identity, (256,) * 5, route=SELECTED_ROUTE, discrete=True),
        lambda: c480.product_action(identity, (256,) * 6, route="bad", discrete=True),
        lambda: c480.product_action(identity, (256,) * 6, route=SELECTED_ROUTE, discrete=True,
                                    direction_order=(0, 1, 2, 3, 4, 4)),
        lambda: c435.validate_geometry(c435.Geometry("bad", 6, 1, c453.TRAIN.sources,
                                                     c453.TRAIN.receivers, 4, False)),
        lambda: c453.strength_state(c453.TRAIN, 1.1),
    )
    for probe in probes:
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
        "source-flag, Z20, coefficient, Suzuki-factor, and sign deletions remain visible and malformed domains are refused",
        min(deletions.values()) > 1e-9 and rejected == len(probes),
        {"deletions": deletions, "malformed_domains_refused": rejected,
         "unchanged_prediction_factors": ["field stream", "packet FSWAP", "contact"]},
    )
    check(
        "the one-particle mass and Cycle-230 contact fixtures survive the discrete actuation replacement",
        abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]) < c435.TOLERANCE
        and update_rows["uniform_one_particle_eigen_residual"] < c435.TOLERANCE
        and update_rows["contact_nontrivial_columns"] == 645
        and contact_signal > 1e-6,
        {"Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"],
         "three_cell_mass": update_rows["three_cell_rest_mass"],
         "mass_eigen_residual": update_rows["uniform_one_particle_eigen_residual"],
         "contact_nontrivial_columns": update_rows["contact_nontrivial_columns"],
         "two_particle_contact_deletion": contact_signal},
    )


def resource_inventory_no_go_controls(prediction: dict[str, object]) -> None:
    manifest = c484.flagged_discrete_manifest(SELECTED_ROUTE)
    cells = c453.TRAIN.length**3
    depth = c453.TRAIN.depth
    per_cell = 35_082_887_764
    full_layer_events = per_cell * cells
    depth_events = full_layer_events * depth
    physical_capacity = cells * c484.c463.SUPERCELL_M2
    used = cells * c484.c481.COMPOSED_USED
    reserve = cells * c484.c481.COMPOSED_RESERVE
    check(
        "the L13 discrete response sublayer has a bounded uniform M2/event schedule while the full Cycle453 shell/effect resource boundary remains open",
        cells == 2197 and physical_capacity == 140_608_000
        and used + reserve == physical_capacity
        and manifest["total_discrete_gates"] == 110_239_872
        and depth_events == 308_308_417_670_032,
        {"L13_cells": cells, "depth": depth,
         "per_cell_layout_M2": c484.c463.SUPERCELL_M2,
         "L13_capacity_M2": physical_capacity, "L13_used_M2": used,
         "L13_reserve_M2": reserve, "per_cell_pipeline_events": per_cell,
         "one_full_layer_events": full_layer_events, "depth4_events": depth_events,
         "depth4_actuation_only_active_flag_events": manifest["total_discrete_gates"] * 6 * depth,
         "host_active_cell_selection": False,
         "disposition": "response actuation schedule bounded; Cycle453 size-dependent three-M64 shell/effect encoding not supplied by Cycle484",
         "L13_full_physical_shell_closed": False,
         "Cycle453_prior_resource_refusal": {
             "seconds": c453.L13_SHELL_ABORT_SECONDS,
             "max_rss_bytes": c453.L13_SHELL_MAX_RSS_BYTES,
             "peak_footprint_bytes": c453.L13_SHELL_PEAK_FOOTPRINT_BYTES,
         }},
    )
    check(
        "the supplied/derived/open inventory separates compiler closure from prediction and shell residuals",
        AUTHORITY == "none" and AUDIT == "unset",
        {"supplied": [
             "Cycle453 exact strengths, L13 geometries, source state, factor order, packet width observable and Cycle420 targets",
             "Cycle484 B20 basis, P8 floor rule, Suzuki coefficients/order, source flag and full-layer route",
             "fixed q1 basis adapter convention, primitive gate calibration, finite norms/tolerances"],
         "derived": [
             "uniform P8 exact coefficient word and adapted six-vertex discrete Cycle453 update",
             "actual train/held discrete width rows and compiler-induced deltas",
             "local physical E/G, inverse, leakage, all24 operator covariance, deletions and L13 response resource ledger"],
         "open": [
             "absolute four-row law/calibration/finite-domain match and stronger-a2 order",
             "complete L13 three-M64 physical shell/effect encoding and emitted total schedule",
             "basis/angle calibration, fault model, optimized phase words, recurrence and autonomous preparation",
             "energy-stress/source identification, physical time, gravity, Records, Born/occurrence and realized history"],
         "firewall": {"response_called_gravity": False, "phase_called_energy": False,
                      "generator_called_rate": False, "depth_called_time": False}},
    )
    check(
        "full N1-N8 demotes the bounded negative to a partial attempt and rejects compiler no-go or axiom pressure",
        AUTHORITY == "none" and AUDIT == "unset",
        {"N1": {
             "adapted uniform P8/S4/B20 occupation route": "ATTEMPTED",
             "retained adapted P8/Strang8 route": "ATTEMPTED locally; prediction rerun remains open",
             "source-angle strength encoding": "UNTESTED",
             "many-Q coherent occupation encoding": "UNTESTED",
             "Cycle213 retarded-field packet join": "UNTESTED",
             "Cycle216 reversible static-field packet join": "UNTESTED",
             "held-out calibrated coupling map": "UNTESTED",
             "larger-depth/nonperiodic packet family": "UNTESTED"},
         "N2": "collapsed independent conditions are normalization/calibration, propagation/geometry, L13 shell/effect compilation, and operational readout",
         "N3": "P8, B20, exact H/NCT, Suzuki order, uniform words, basis permutation, state preparation, factor order, geometry, targets, tolerances and missing fault model are explicit",
         "N4": "Cycle453 four rows/order match exactly; Cycle484 compiler residuals match only the local actuation seam; L13 shell and prediction residuals are not conflated",
         "N5": "negative evidence is only four finite L13/depth4 rows, held order, and the still-unbuilt full shell; no lattice-wide or gravity negative",
         "N6": "Strang8 prediction, source-angle, many-Q, retarded/static field, calibrated held-out coupling, cached/local shell and larger-domain paths remain live",
         "N7": "a hostile reviewer can recover scale/order by changing the source normalization map or finite packet law while retaining the exact discrete compiler",
         "N8": "Cycles432->435 and 447->450 retired similar finite residuals by enlarging or composing constructions; the same mechanisms remain available; no axiom pressure",
         "gate": "partial-attempt-with-named-untested-routes; broad no-go FAIL; shared obstruction FAIL; axiom pressure FAIL"},
    )


def resource_cap_controls(started: float) -> None:
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    check(
        "the complete Cycle487 cold run stays below explicit wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
        {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
         "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB},
    )


def main() -> int:
    started = perf_counter()
    print("Cycle487 discrete quadrupole exact-strength bridge")
    print("authority", AUTHORITY, "audit", AUDIT)
    note_contract()
    frozen_controls()
    compiler = compiler_residual_controls()
    embedding_controls()
    prediction = prediction_controls(compiler)
    inverse_controls()
    physical_eg_controls()
    covariance_controls()
    deletion_domain_mass_contact_controls()
    resource_inventory_no_go_controls(prediction)
    resource_cap_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
