#!/usr/bin/env python3
"""Cycle 480: discrete-angle and product-law compiler for Cycle 476.

Freeze the finite Cycle-476 angle family, select one finite dyadic physical
gate basis, compile every onsite rotation into repeated fixed phase quanta,
and compare the retained eight-step symmetric schedule with a predeclared
fourth-order Suzuki composition.  Coefficient quantization, product-formula
error, and discrete-angle synthesis error remain separate.

This is one bounded q1 local response compiler.  Authority is none and audit
is unset.  No axiom, foundation, primitive registry, policy, queue, or audit
surface is changed.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
import math
from pathlib import Path
import resource
import sys
import time

import numpy as np
from scipy.sparse.linalg import expm_multiply


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_word_weight_control_compiler_cycle476_2026_07_19 as c476


c426 = c476.c426
c322 = c476.c322
c463 = c476.c463
c472 = c476.c472

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DISCRETE_ANGLE_PRODUCT_COMPILER_CYCLE480_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

COEFFICIENT_BITS = c476.COEFFICIENT_BITS
COEFFICIENT_SCALE = c476.COEFFICIENT_SCALE
PHASE_EXPONENT = 20
PHASE_QUANTUM = 2.0 * math.pi / (1 << PHASE_EXPONENT)
SUZUKI_P = 1.0 / (4.0 - 4.0 ** (1.0 / 3.0))
SUZUKI_Q = 1.0 - 4.0 * SUZUKI_P
ROUTE_SCALES = {
    "direct-strang8": (1.0 / 8.0,) * 8,
    "suzuki4": (SUZUKI_P, SUZUKI_P, SUZUKI_Q, SUZUKI_P, SUZUKI_P),
}
ROUTE_ORDER = ("direct-strang8", "suzuki4")
TOLERANCE = 3.0e-10
STATE_ERROR_CAP = 1.0e-2
PRODUCT_ERROR_CAP = 2.0e-3
ANGLE_ERROR_CAP = 2.0e-3
OPERATOR_ERROR_CAP = 2.0e-2
SIGNAL_FLOOR = 1.0e-9
WALL_CAP_SECONDS = 900.0
RSS_CAP_BYTES = 4 * 1024**3
FROZEN_C476_SHA = "2cb747b912ed92d6d19e067de9780e0a5899d3659d8defc2135612346cfd0963"

# These targets and the basis precision are module constants: they are frozen
# before word_rows() exposes any train or held fixture.
FROZEN_CYCLE476_ANGLES = tuple(
    c426.ANGLE * (1 << bit) / (16 * COEFFICIENT_SCALE)
    for bit in range(COEFFICIENT_BITS)
)
FROZEN_SUZUKI_ANGLES = tuple(
    scale * c426.ANGLE * (1 << bit) / (2 * COEFFICIENT_SCALE)
    for scale in (SUZUKI_P, SUZUKI_Q)
    for bit in range(COEFFICIENT_BITS)
)


@dataclass(frozen=True)
class RowResult:
    name: str
    held: bool
    coefficients: tuple[int, ...]
    coefficient_residual: float
    direct_product_residual: float
    direct_angle_residual: float
    direct_intrinsic_residual: float
    direct_total_residual: float
    suzuki_product_residual: float
    suzuki_angle_residual: float
    suzuki_intrinsic_residual: float
    suzuki_total_residual: float


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
        "frozen before held-row evaluation",
        "finite dyadic physical gate basis",
        "coefficient quantization, product-formula error, and discrete-angle synthesis error",
        "exact inverse convention",
        "held word rows",
        "all 24 proper-cubic frames",
        "26-m2 support",
        "no runtime angle oracle",
        "basis is supplied",
        "phase is not physical energy",
        "n1 —",
        "n8 —",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in normalized(NOTE))
    source_sha = sha256(Path(c476.__file__).read_bytes()).hexdigest()
    check(
        "the Cycle480 note freezes the discrete-angle/product boundary and exact Cycle476 source",
        not missing and source_sha == FROZEN_C476_SHA,
        {"missing_note_contract": missing, "Cycle476_runner_SHA256": source_sha},
    )


def nearest_steps(angle: float) -> int:
    """Symmetric nearest-integer phase-quantum count; no half ties occur."""

    magnitude = math.floor(abs(angle) / PHASE_QUANTUM + 0.5)
    return -magnitude if angle < 0 else magnitude


def synthesized_angle(angle: float) -> float:
    return nearest_steps(angle) * PHASE_QUANTUM


def frozen_angle_manifest() -> dict[str, object]:
    digest = sha256()
    rows = []
    for family, angles in (
        ("Cycle476-Strang8", FROZEN_CYCLE476_ANGLES),
        ("Suzuki4-comparison", FROZEN_SUZUKI_ANGLES),
    ):
        for index, angle in enumerate(angles):
            steps = nearest_steps(angle)
            compiled = steps * PHASE_QUANTUM
            error = compiled - angle
            digest.update(
                f"{family}|{index}|{angle:.17g}|{steps}|{compiled:.17g}|{error:.17g}\n".encode()
            )
            rows.append(
                {
                    "family": family,
                    "index": index,
                    "target": angle,
                    "phase_steps": steps,
                    "compiled": compiled,
                    "signed_error": error,
                    "pair_rotation_operator_error": 2.0 * math.sin(abs(error) / 2.0),
                    "onsite_Rz_operator_error": 2.0 * math.sin(abs(error) / 4.0),
                }
            )
    return {
        "basis": (
            "{NOT, CNOT, Toffoli, H, Z20, Z20^-1}; "
            "Z20=Rz(2*pi/2^20)"
        ),
        "basis_supplied": True,
        "phase_exponent": PHASE_EXPONENT,
        "phase_quantum": PHASE_QUANTUM,
        "rounding": "symmetric nearest integer, with no half ties in the frozen set",
        "frozen_targets": rows,
        "frozen_manifest_digest": digest.hexdigest(),
    }


@lru_cache(maxsize=8)
def direction_pairs(direction: int) -> tuple[tuple[int, int, float], ...]:
    generator = c476.direction_generator(direction).tocoo()
    pairs = tuple(
        (int(row), int(column), float(np.real(value)))
        for row, column, value in zip(generator.row, generator.col, generator.data)
        if row > column
    )
    if len(pairs) != 16:
        raise RuntimeError("direction generator left its sixteen disjoint physical pairs")
    occupied = [wire for pair in pairs for wire in pair[:2]]
    if len(set(occupied)) != len(occupied):
        raise RuntimeError("one directional exponential ceased to be disjoint")
    return pairs


def apply_direction(state: np.ndarray, direction: int, angle: float) -> np.ndarray:
    """Apply exp(i angle H_d) exactly through its disjoint signed X blocks."""

    output = np.asarray(state, dtype=complex).copy()
    cosine = math.cos(angle)
    sine = 1j * math.sin(angle)
    for left, right, sign in direction_pairs(direction):
        left_value = output[left].copy()
        right_value = output[right].copy()
        output[left] = cosine * left_value + sine * sign * right_value
        output[right] = cosine * right_value + sine * sign * left_value
    return output


def validate_compiler_domain(
    coefficients: tuple[int, ...],
    route: str,
    direction_order: tuple[int, ...],
    phase_exponent: int,
) -> None:
    if route not in ROUTE_SCALES:
        raise ValueError("unknown product route")
    if len(coefficients) != 6 or any(
        not isinstance(value, (int, np.integer)) or value < 0 or value >= (1 << COEFFICIENT_BITS)
        for value in coefficients
    ):
        raise ValueError("coefficient word leaves the six ten-bit code")
    if tuple(sorted(direction_order)) != tuple(range(6)):
        raise ValueError("direction order must carry exactly six lanes")
    if phase_exponent != PHASE_EXPONENT:
        raise ValueError("phase precision differs from the frozen physical basis")


def factor_list(route: str, direction_order: tuple[int, ...]) -> tuple[tuple[float, int], ...]:
    return tuple(
        (scale, direction)
        for scale in ROUTE_SCALES[route]
        for direction in direction_order + tuple(reversed(direction_order))
    )


def product_action(
    state: np.ndarray,
    coefficients: tuple[int, ...],
    *,
    route: str,
    discrete: bool,
    direction_order: tuple[int, ...] = tuple(range(6)),
    inverse: bool = False,
    omit_bit: tuple[int, int] | None = None,
    omit_factor: int | None = None,
    delete_one_quantum: tuple[int, int] | None = None,
    phase_exponent: int = PHASE_EXPONENT,
) -> np.ndarray:
    """Apply one frozen product schedule, optionally through the dyadic basis."""

    validate_compiler_domain(coefficients, route, direction_order, phase_exponent)
    factors = factor_list(route, direction_order)
    enumerated = tuple(enumerate(factors))
    if inverse:
        enumerated = tuple(reversed(enumerated))
    output = np.asarray(state, dtype=complex).copy()
    inverse_sign = -1 if inverse else 1
    for factor_index, (scale, direction) in enumerated:
        if factor_index == omit_factor:
            continue
        target_by_bit = tuple(
            scale * c426.ANGLE * (1 << bit) / (2 * COEFFICIENT_SCALE)
            for bit in range(COEFFICIENT_BITS)
        )
        active_bits = tuple(
            bit
            for bit in range(COEFFICIENT_BITS)
            if (coefficients[direction] >> bit) & 1
            and omit_bit != (direction, bit)
        )
        if discrete:
            steps = sum(nearest_steps(target_by_bit[bit]) for bit in active_bits)
            if delete_one_quantum == (factor_index, direction) and steps:
                steps -= 1 if steps > 0 else -1
            angle = inverse_sign * steps * PHASE_QUANTUM
        else:
            angle = inverse_sign * sum(target_by_bit[bit] for bit in active_bits)
        if angle:
            output = apply_direction(output, direction, angle)
    return output


def route_gate_manifest(route: str) -> dict[str, object]:
    scales = ROUTE_SCALES[route]
    half_passes = 2 * len(scales)
    rotations = 96 * COEFFICIENT_BITS * half_passes
    counts = Counter(
        {
            "Toffoli": rotations * 150,
            "CNOT": rotations * 2,
            "NOT": 1_889_280 * half_passes // 16,
            "H": rotations * 2,
        }
    )
    # For every scale and bit: 96 pairs, two directional passes per S2,
    # and two onsite Rz occurrences in the controlled-X decomposition.
    phase_steps = sum(
        abs(nearest_steps(scale * c426.ANGLE * (1 << bit) / (2 * COEFFICIENT_SCALE)))
        for scale in scales
        for bit in range(COEFFICIENT_BITS)
    )
    counts["Z20_or_inverse"] = 96 * 2 * 2 * phase_steps
    digest = sha256()
    for scale_index, scale in enumerate(scales):
        for direction in range(6):
            for bit in range(COEFFICIENT_BITS):
                target = scale * c426.ANGLE * (1 << bit) / (2 * COEFFICIENT_SCALE)
                digest.update(
                    f"{route}|{scale_index}|{direction}|{bit}|{nearest_steps(target)}\n".encode()
                )
    return {
        "route": route,
        "symmetric_S2_blocks": len(scales),
        "directional_half_passes": half_passes,
        "coefficient_controlled_pair_rotations": rotations,
        "counts": dict(counts),
        "total_discrete_gates": sum(counts.values()),
        "maximum_local_support_M2": 26,
        "clean_rotation_auxiliary_M2": 12,
        "new_angle_auxiliary_M2": 0,
        "manifest_digest": digest.hexdigest(),
    }


def probe_state() -> np.ndarray:
    rng = np.random.default_rng(480)
    state = rng.normal(size=(448, 3)) + 1j * rng.normal(size=(448, 3))
    state /= np.linalg.norm(state, axis=0)
    return state


def row_result(row: c476.WordRow, state: np.ndarray) -> RowResult:
    integers = c476.expected_coefficients(row.words)
    quantized = np.asarray(integers, dtype=float) / COEFFICIENT_SCALE
    exact = c476.exact_coefficients(row.words)
    quantized_target = expm_multiply(
        1j * c426.ANGLE * c476.coefficient_generator(quantized), state
    )
    exact_target = expm_multiply(
        1j * c426.ANGLE * c476.coefficient_generator(exact), state
    )
    outputs = {}
    for route in ROUTE_ORDER:
        continuous = product_action(state, integers, route=route, discrete=False)
        discrete = product_action(state, integers, route=route, discrete=True)
        outputs[route] = {
            "product": float(np.linalg.norm(continuous - quantized_target)),
            "angle": float(np.linalg.norm(discrete - continuous)),
            "intrinsic": float(np.linalg.norm(discrete - quantized_target)),
            "total": float(np.linalg.norm(discrete - exact_target)),
        }
    return RowResult(
        row.name,
        row.held,
        integers,
        float(np.linalg.norm(quantized_target - exact_target)),
        outputs["direct-strang8"]["product"],
        outputs["direct-strang8"]["angle"],
        outputs["direct-strang8"]["intrinsic"],
        outputs["direct-strang8"]["total"],
        outputs["suzuki4"]["product"],
        outputs["suzuki4"]["angle"],
        outputs["suzuki4"]["intrinsic"],
        outputs["suzuki4"]["total"],
    )


def state_residual_controls(rows: tuple[c476.WordRow, ...]) -> dict[str, object]:
    print("\nFROZEN TRAIN SELECTION / HELD WORD ROWS")
    state = probe_state()
    train_rows = tuple(row for row in rows if not row.held)
    held_rows = tuple(row for row in rows if row.held)
    if not train_rows or not held_rows:
        raise RuntimeError("Cycle472 train/held partition disappeared")

    # This rule and route order are fixed in code.  Only training intrinsic
    # residuals select a route; held residuals are evaluated afterward and
    # cannot change the selection.
    train = tuple(row_result(row, state) for row in train_rows)
    training_score = {
        "direct-strang8": max(item.direct_intrinsic_residual for item in train),
        "suzuki4": max(item.suzuki_intrinsic_residual for item in train),
    }
    selected = min(ROUTE_ORDER, key=lambda route: (training_score[route], ROUTE_ORDER.index(route)))
    held = tuple(row_result(row, state) for row in held_rows)
    results = train + held

    direct_product = max(item.direct_product_residual for item in results)
    direct_angle = max(item.direct_angle_residual for item in results)
    direct_total = max(item.direct_total_residual for item in results)
    suzuki_product = max(item.suzuki_product_residual for item in results)
    suzuki_angle = max(item.suzuki_angle_residual for item in results)
    suzuki_total = max(item.suzuki_total_residual for item in results)
    coefficient = max(item.coefficient_residual for item in results)

    inverse_residuals = {}
    leakage = {}
    sample = next(item for item in rows if item.held and len(set(item.words)) > 2)
    sample_coefficients = c476.expected_coefficients(sample.words)
    for route in ROUTE_ORDER:
        forward = product_action(state, sample_coefficients, route=route, discrete=True)
        restored = product_action(
            forward, sample_coefficients, route=route, discrete=True, inverse=True
        )
        inverse_residuals[route] = float(np.linalg.norm(restored - state))
        leakage[route] = abs(float(np.linalg.norm(forward) - np.linalg.norm(state)))

    result_dicts = tuple(result.__dict__ for result in results)
    check(
        "the frozen dyadic synthesis keeps coefficient, product, and angle errors separate on every train and held row",
        len(results) == 14
        and direct_product < PRODUCT_ERROR_CAP
        and suzuki_product < PRODUCT_ERROR_CAP
        and direct_angle < ANGLE_ERROR_CAP
        and suzuki_angle < ANGLE_ERROR_CAP
        and max(direct_total, suzuki_total) < STATE_ERROR_CAP
        and max(inverse_residuals.values()) < TOLERANCE
        and max(leakage.values()) < TOLERANCE,
        {
            "frozen_before_rows": True,
            "training_rows": len(train),
            "held_rows": len(held),
            "training_only_route_scores": training_score,
            "training_selected_route_locked_before_held_readout": selected,
            "maximum_coefficient_quantization_state_residual": coefficient,
            "maximum_direct_product_formula_state_residual": direct_product,
            "maximum_direct_discrete_angle_state_residual": direct_angle,
            "maximum_direct_total_state_residual": direct_total,
            "maximum_suzuki_product_formula_state_residual": suzuki_product,
            "maximum_suzuki_discrete_angle_state_residual": suzuki_angle,
            "maximum_suzuki_total_state_residual": suzuki_total,
            "inverse_residuals": inverse_residuals,
            "q1_norm_leakage": leakage,
            "rows": result_dicts,
        },
    )
    return {
        "selected": selected,
        "results": results,
        "state": state,
        "training_score": training_score,
        "inverse": inverse_residuals,
        "leakage": leakage,
    }


def spectral_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


def operator_controls(
    rows: tuple[c476.WordRow, ...], state_result: dict[str, object]
) -> dict[str, object]:
    print("\nLOCAL OPERATOR ERROR")
    representatives = (
        next(row for row in rows if not row.held),
        next(row for row in rows if row.held and len(set(row.words)) > 2),
    )
    identity = np.eye(448, dtype=complex)
    results = []
    maximum = 0.0
    for row in representatives:
        integers = c476.expected_coefficients(row.words)
        quantized = np.asarray(integers, dtype=float) / COEFFICIENT_SCALE
        exact = c476.exact_coefficients(row.words)
        quantized_target = expm_multiply(
            1j * c426.ANGLE * c476.coefficient_generator(quantized), identity
        )
        exact_target = expm_multiply(
            1j * c426.ANGLE * c476.coefficient_generator(exact), identity
        )
        item = {"name": row.name, "held": row.held}
        item["coefficient_quantization_operator_residual"] = spectral_norm(
            quantized_target - exact_target
        )
        for route in ROUTE_ORDER:
            continuous = product_action(identity, integers, route=route, discrete=False)
            discrete = product_action(identity, integers, route=route, discrete=True)
            product_error = spectral_norm(continuous - quantized_target)
            angle_error = spectral_norm(discrete - continuous)
            intrinsic = spectral_norm(discrete - quantized_target)
            total = spectral_norm(discrete - exact_target)
            unitarity = spectral_norm(discrete.conj().T @ discrete - identity)
            maximum = max(maximum, product_error, angle_error, intrinsic, total)
            item[route] = {
                "product_formula_operator_residual": product_error,
                "discrete_angle_operator_residual": angle_error,
                "intrinsic_operator_residual": intrinsic,
                "total_operator_residual": total,
                "unitarity_residual": unitarity,
            }
        results.append(item)

    angle_manifest = frozen_angle_manifest()
    maximum_pair_error = max(
        item["pair_rotation_operator_error"]
        for item in angle_manifest["frozen_targets"]
    )
    maximum_onsite_error = max(
        item["onsite_Rz_operator_error"]
        for item in angle_manifest["frozen_targets"]
    )
    check(
        "literal 448-dimensional train and held operators expose product, angle, coefficient, and total residuals",
        maximum < OPERATOR_ERROR_CAP
        and maximum_pair_error <= 2.0 * math.sin(PHASE_QUANTUM / 4.0) + TOLERANCE
        and all(
            item[route]["unitarity_residual"] < TOLERANCE
            for item in results
            for route in ROUTE_ORDER
        ),
        {
            "operator_norm": "spectral 2-norm on the complete 448-dimensional q1 block",
            "rows": results,
            "maximum_route_operator_residual": maximum,
            "maximum_frozen_pair_rotation_operator_error": maximum_pair_error,
            "maximum_frozen_onsite_Rz_operator_error": maximum_onsite_error,
            "declared_operator_error_cap": OPERATOR_ERROR_CAP,
        },
    )
    return {"rows": results, "maximum": maximum, "angle_manifest": angle_manifest}


def covariance_capacity_controls(
    rows: tuple[c476.WordRow, ...], selected: str
) -> dict[str, object]:
    print("\nALL24 CARRIED SCHEDULE / CAPACITY / GATE ACCOUNTING")
    sample = next(row for row in rows if row.held and len(set(row.words)) > 2)
    coefficients = c476.expected_coefficients(sample.words)
    state = probe_state()[:, 0]
    base_output = product_action(state, coefficients, route=selected, discrete=True)
    maximum_covariance = 0.0
    carried_digests = []
    for frame in c463.proper_cubic_frames():
        matrix = np.asarray(frame, dtype=int)
        mapping = c472.direction_map(matrix)
        carried_coefficients = [0] * 6
        for source, target in enumerate(mapping):
            carried_coefficients[target] = coefficients[source]
        representation = c426.recoil_frame(1, matrix)
        carried = product_action(
            representation @ state,
            tuple(carried_coefficients),
            route=selected,
            discrete=True,
            direction_order=tuple(mapping),
        )
        maximum_covariance = max(
            maximum_covariance,
            float(np.linalg.norm(carried - representation @ base_output)),
        )
        digest = sha256()
        digest.update(selected.encode())
        digest.update(str(tuple(mapping)).encode())
        digest.update(frozen_angle_manifest()["frozen_manifest_digest"].encode())
        carried_digests.append(digest.hexdigest())

    manifests = {route: route_gate_manifest(route) for route in ROUTE_ORDER}
    composed_occupied = 48_357
    check(
        "both bounded discrete schedules fit the Cycle476 physical block and the selected schedule carries through all24 frames",
        len(c463.proper_cubic_frames()) == 24
        and maximum_covariance < TOLERANCE
        and all(item["maximum_local_support_M2"] == 26 for item in manifests.values())
        and all(item["new_angle_auxiliary_M2"] == 0 for item in manifests.values())
        and composed_occupied < c463.SUPERCELL_M2,
        {
            "selected_route": selected,
            "proper_cubic_frames": 24,
            "maximum_all24_carried_discrete_schedule_residual": maximum_covariance,
            "frame_manifest_digests": carried_digests,
            "route_gate_manifests": manifests,
            "Cycle476_composed_occupied_M2": composed_occupied,
            "supercell_capacity_M2": c463.SUPERCELL_M2,
            "additional_angle_work_M2": 0,
            "maximum_rotation_support_M2": 26,
            "whole_layer_composed": False,
        },
    )
    return {"manifests": manifests, "maximum_covariance": maximum_covariance}


def deletion_domain_inventory_controls(
    rows: tuple[c476.WordRow, ...], selected: str
) -> None:
    print("\nDELETIONS / LAWFUL DOMAIN / INVENTORY / N1-N8")
    selected_row = next(row for row in rows if row.held and len(set(row.words)) > 2)
    coefficients = c476.expected_coefficients(selected_row.words)
    state = probe_state()[:, 0]
    intact = product_action(state, coefficients, route=selected, discrete=True)
    direction = next(index for index, value in enumerate(coefficients) if value)
    active_bit = next(bit for bit in range(COEFFICIENT_BITS) if (coefficients[direction] >> bit) & 1)
    quantum_deleted = product_action(
        state,
        coefficients,
        route=selected,
        discrete=True,
        delete_one_quantum=(0, 0),
    )
    # Factor zero is direction zero in the declared order.  If lane zero is
    # empty on this held row, choose its first nonempty occurrence instead.
    factor_direction = 0
    if not coefficients[0]:
        factor_direction = direction
    factor_index = next(
        index
        for index, (_scale, lane) in enumerate(factor_list(selected, tuple(range(6))))
        if lane == factor_direction
    )
    quantum_deleted = product_action(
        state,
        coefficients,
        route=selected,
        discrete=True,
        delete_one_quantum=(factor_index, factor_direction),
    )
    bit_deleted = product_action(
        state,
        coefficients,
        route=selected,
        discrete=True,
        omit_bit=(direction, active_bit),
    )
    factor_deleted = product_action(
        state,
        coefficients,
        route=selected,
        discrete=True,
        omit_factor=factor_index,
    )
    deletions = {
        "one_Z20_quantum": float(np.linalg.norm(intact - quantum_deleted)),
        "one_active_coefficient_bit_family": float(np.linalg.norm(intact - bit_deleted)),
        "one_symmetric_direction_factor": float(np.linalg.norm(intact - factor_deleted)),
    }

    zero = np.zeros(448, dtype=complex)
    zero[0] = 1.0
    allzero_residuals = {
        route: float(
            np.linalg.norm(
                product_action(zero, (0,) * 6, route=route, discrete=True) - zero
            )
        )
        for route in ROUTE_ORDER
    }
    rejected = 0
    malformed = (
        lambda: product_action(state, (0,) * 5, route=selected, discrete=True),
        lambda: product_action(state, (0, 0, 0, 0, 0, -1), route=selected, discrete=True),
        lambda: product_action(state, (0, 0, 0, 0, 0, 1 << COEFFICIENT_BITS), route=selected, discrete=True),
        lambda: product_action(state, (0,) * 6, route="unknown", discrete=True),
        lambda: product_action(state, (0,) * 6, route=selected, discrete=True, direction_order=(0, 1, 2, 3, 4, 4)),
        lambda: product_action(state, (0,) * 6, route=selected, discrete=True, phase_exponent=19),
    )
    for action in malformed:
        try:
            action()
        except ValueError:
            rejected += 1

    inventory = {
        "supplied": [
            "Cycle476 P=8 ten-bit coefficient words and q1 signed source-pair law",
            "Cycle426 dimensionless response angle and fermion convention",
            "finite basis {NOT,CNOT,Toffoli,H,Z20,Z20^-1}",
            "Z20=Rz(2*pi/2^20), exact H/NCT gates, and primitive calibration",
            "nearest-integer angle rounding, target-relative direction order, and train/held fixtures",
        ],
        "derived": [
            "ten frozen Cycle476 angles and twenty predeclared Suzuki comparison angles",
            "integer repeated-Z20 sequences with exact inverse convention and no runtime angle oracle",
            "direct Strang8 and fourth-order Suzuki state/operator residual separation",
            "complete structural/phase gate counts, no added angle work M2, and 26-M2 support",
            "held-row, deletion, domain, capacity, and all24 carried-schedule controls",
        ],
        "open": [
            "physical selection or calibration of the supplied dyadic basis and exponent 20",
            "fault/noise thresholds and optimal discrete synthesis",
            "uniform analytic error theorem over every lawful 249-bit word tuple",
            "coherent exact-small-block/Givens, phase-kickback, Clifford-plus-T, and qubitization alternatives",
            "q>1 response and Cycle476/Cycle477 augmented whole-layer composition",
            "autonomous law selection, recurrent source/matter behavior, operational occurrence, and continuum calibration",
        ],
        "N1": "direct dyadic Strang8 and dyadic fourth-order Suzuki are attempted and succeed; Clifford-plus-T, phase-gradient kickback, exact controlled Givens, qubitization/QSP, randomized formulas, and alternative finite bases remain materially distinct open families",
        "N2": "coefficient quantization, product order, primitive angle synthesis, whole-layer composition, q-sector extension, recurrence, calibration, and occurrence remain independent walls",
        "N3": "P=8, theta, fermion signs, H/NCT exactness, Z20 calibration, phase exponent, nearest rounding, serial carried order, clean controls, fixture split, and omitted fault model are explicit supplied structure",
        "N4": "this matches Cycle476's named primitive onsite angle and product-law residual; it does not match Cycle477's augmented whole-layer, q>1, recurrence, calibration, or occurrence residuals",
        "N5": "claims are restricted to frozen local q1 schedules, 448-dimensional operators, fourteen finite word rows, and one-supercell support; no wider physical interpretation is inferred",
        "N6": "higher-order composition closes part of the product wall constructively, while exact Givens, phase kickback, Clifford-plus-T, whole-layer coloring, and q-sector routes stay live",
        "N7": "a hostile reviewer can demand a basis-selection law, physical fault model, analytic uniform bound, shorter phase words, coherent exact-small-block arithmetic, and literal augmented-layer execution",
        "N8": "Cycles467, 470, 474, 476, and 477 repeatedly retire compiler and transport imports constructively; the surviving angle selection and composition surfaces do not echo a route-independent obstruction",
        "gate": "broad no-go FAIL; minimum-content FAIL; shared-obstruction FAIL; axiom-pressure FAIL; no axiom pressure",
    }
    check(
        "phase, bit-family, and product-factor deletions are visible while all-zero and malformed domains are controlled",
        min(deletions.values()) > SIGNAL_FLOOR
        and max(allzero_residuals.values()) < TOLERANCE
        and rejected == len(malformed),
        {
            "selected_held_row": selected_row.name,
            "selected_route": selected,
            "deletion_residuals": deletions,
            "allzero_identity_residuals": allzero_residuals,
            "malformed_domains_rejected": rejected,
            **inventory,
        },
    )


def resource_controls(started: float) -> None:
    elapsed = time.perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(raw if sys.platform == "darwin" else raw * 1024)
    check(
        "the bounded runner stays inside its wall/RSS caps",
        elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES,
        {
            "elapsed_seconds": elapsed,
            "peak_RSS_MiB": rss / 1024**2,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "RSS_cap_GiB": RSS_CAP_BYTES / 1024**3,
        },
    )


def main() -> int:
    started = time.perf_counter()
    note_contract()
    angle_manifest = frozen_angle_manifest()
    check(
        "one supplied finite dyadic basis compiles every predeclared angle by bounded integer repetition",
        len(angle_manifest["frozen_targets"]) == 30
        and max(abs(item["signed_error"]) for item in angle_manifest["frozen_targets"]) <= PHASE_QUANTUM / 2.0
        and all(abs(item["phase_steps"]) > 0 for item in angle_manifest["frozen_targets"]),
        angle_manifest,
    )
    rows = c476.word_rows()
    state_result = state_residual_controls(rows)
    operator_controls(rows, state_result)
    covariance_capacity_controls(rows, state_result["selected"])
    deletion_domain_inventory_controls(rows, state_result["selected"])
    resource_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    if FAIL:
        return 1
    print("RESULT PHYSICAL_DISCRETE_ANGLE_PRODUCT_COMPILER_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
