#!/usr/bin/env python3
"""Block 185: axial momentum, source quotient, and action-sign boundary.

The runner extends Block 184's y/z-odd matrix GNS probe over axial spatial
momentum.  It certifies the infrared sign boundary, tests two Ward-conserved
edge representatives of the same common-metric TT stress, and challenges the
equal-magnitude action-sign flip in the complementary even sector.

This is a bounded numerical/algebraic result for the supplied quadratic
twenty-two-edge action family.  It does not claim gravity failure, select a
physical constraint reduction, amend an axiom, retire an obligation, or move
a TOE percentage.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import os
from pathlib import Path
import sys
import time

import numpy as np
from numpy.polynomial import Polynomial, chebyshev
from scipy.linalg import null_space
from scipy.optimize import brentq


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_2026_08_13 as block68  # noqa: E402
import admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14 as block74  # noqa: E402
import admissibility_reflected_curvature_action_glued_matrix_gns_unitary_boundary_2026_08_24 as block184  # noqa: E402


block48 = block74.block48
block49 = block74.block49
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_MOMENTUM_SOURCE_QUOTIENT_SIGN_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_GLUED_MATRIX_GNS_UNITARY_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
SOURCE_PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_MOMENTUM_SOURCE_QUOTIENT_SIGN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_GLUED_MATRIX_GNS_UNITARY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_reflected_curvature_momentum_source_quotient_sign_boundary_2026_08_24.py",
    "scripts/admissibility_reflected_curvature_action_glued_matrix_gns_unitary_boundary_2026_08_24.py",
    "scripts/admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14.py",
    "scripts/admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_2026_08_13.py",
)

MUTATIONS = (
    "action_input",
    "threshold_input",
    "periodic_input",
    "source_input",
    "tt_input",
    "reduction_input",
    "repair_input",
    "even_input",
    "note_boundary",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 190 else detail[:187] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


@dataclass(frozen=True)
class Sector:
    edge_basis: np.ndarray
    gauge_basis: np.ndarray


@dataclass(frozen=True)
class PhysicalFiber:
    operator: np.ndarray
    right: np.ndarray
    left: np.ndarray
    quotient: np.ndarray
    reduced: np.ndarray
    bordered: np.ndarray
    covariance: np.ndarray


@dataclass(frozen=True)
class AxialPolynomialCertificate:
    coefficients: np.ndarray
    bernstein_safe: np.ndarray
    relative_reconstruction: float
    k_zero: float
    k_global: float
    safe_grid_minimum: float
    rank_one_residual: float
    rank_one_ward: float
    rank_one_norm_range: tuple[float, float]


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def inertia_values(values: np.ndarray, tolerance: float = 1.0e-9) -> tuple[int, int, int]:
    values = np.asarray(values, dtype=float)
    return (
        int(np.sum(values < -tolerance)),
        int(np.sum(values > tolerance)),
        int(np.sum(np.abs(values) <= tolerance)),
    )


def sector(union, sign: int) -> Sector:
    edge_swap = block48.swap_matrix_for_directions(tuple(union.directions))
    edge_basis = block48.sign_basis(edge_swap, sign)
    gauge_swap = np.eye(4)
    gauge_swap[[1, 2]] = gauge_swap[[2, 1]]
    gauge_basis = block48.sign_basis(gauge_swap, sign)
    return Sector(edge_basis=edge_basis, gauge_basis=gauge_basis)


def physical_fiber(
    union,
    selected: Sector,
    momentum: np.ndarray,
    mu: float,
) -> PhysicalFiber:
    q = np.asarray(momentum, dtype=complex)
    edge = selected.edge_basis
    gauge = selected.gauge_basis
    operator = edge.T @ (-block74.cross_action_symbol(union, q, mu)) @ edge
    right = edge.T @ block48.union_gauge_map(union, q) @ gauge
    left = edge.T @ block48.union_gauge_map(union, -q) @ gauge
    quotient = null_space(right.conj().T, rcond=1.0e-11)
    reduced = quotient.conj().T @ operator @ quotient
    reduced = 0.5 * (reduced + reduced.conj().T)
    zero = np.zeros((gauge.shape[1], gauge.shape[1]), dtype=complex)
    bordered = np.block([[operator, left], [right.T, zero]])
    covariance = np.linalg.inv(bordered)[: edge.shape[1], : edge.shape[1]]
    covariance = 0.5 * (covariance + covariance.conj().T)
    return PhysicalFiber(
        operator=operator,
        right=right,
        left=left,
        quotient=quotient,
        reduced=reduced,
        bordered=bordered,
        covariance=covariance,
    )


def fifth_elementary(matrix: np.ndarray) -> float:
    value = sum(
        np.linalg.det(np.delete(np.delete(matrix, index, axis=0), index, axis=1))
        for index in range(matrix.shape[0])
    )
    return float(value.real)


def odd_e5(union, odd: Sector, wave_number: float, frequency: float, mu: float) -> float:
    q = np.asarray((wave_number, 0.0, 0.0, frequency), dtype=complex)
    operator = odd.edge_basis.T @ (-block74.cross_action_symbol(union, q, mu)) @ odd.edge_basis
    return fifth_elementary(operator)


def chebyshev_to_power(coefficients: np.ndarray) -> np.ndarray:
    degree_x, degree_y = np.asarray(coefficients.shape) - 1
    first = np.zeros_like(coefficients)
    for y_index in range(degree_y + 1):
        values = chebyshev.cheb2poly(coefficients[:, y_index])
        first[: len(values), y_index] = values
    power = np.zeros_like(coefficients)
    for x_index in range(degree_x + 1):
        values = chebyshev.cheb2poly(first[x_index, :])
        power[x_index, : len(values)] = values
    return power


def transform_rectangle(
    power: np.ndarray,
    x_low: float,
    x_high: float,
    y_low: float = -1.0,
    y_high: float = 1.0,
) -> np.ndarray:
    first = np.zeros_like(power)
    for y_index in range(power.shape[1]):
        transformed = Polynomial(power[:, y_index])(
            Polynomial((x_low, x_high - x_low))
        ).coef
        first[: len(transformed), y_index] = transformed
    result = np.zeros_like(power)
    for x_index in range(power.shape[0]):
        transformed = Polynomial(first[x_index, :])(
            Polynomial((y_low, y_high - y_low))
        ).coef
        result[x_index, : len(transformed)] = transformed
    return result


def power_to_bernstein(power: np.ndarray) -> np.ndarray:
    degree_x, degree_y = np.asarray(power.shape) - 1
    bernstein = np.zeros_like(power)
    for x_index in range(degree_x + 1):
        for y_index in range(degree_y + 1):
            bernstein[x_index, y_index] = sum(
                power[x_power, y_power]
                * math.comb(x_index, x_power)
                / math.comb(degree_x, x_power)
                * math.comb(y_index, y_power)
                / math.comb(degree_y, y_power)
                for x_power in range(x_index + 1)
                for y_power in range(y_index + 1)
            )
    return bernstein


def axial_polynomial_certificate(
    union, odd: Sector, mutation: str
) -> AxialPolynomialCertificate:
    count_x = 32
    count_y = 32
    degree_x = 5
    degree_y = 4
    sampled = np.asarray(
        [
            [
                odd_e5(
                    union,
                    odd,
                    2.0 * np.pi * x_index / count_x,
                    2.0 * np.pi * y_index / count_y,
                    block74.MU,
                )
                for y_index in range(count_y)
            ]
            for x_index in range(count_x)
        ]
    )
    fourier = np.fft.fft2(sampled) / (count_x * count_y)
    coefficients = np.zeros((degree_x + 1, degree_y + 1))
    for x_index in range(degree_x + 1):
        x_slots = (0,) if x_index == 0 else (x_index, (-x_index) % count_x)
        for y_index in range(degree_y + 1):
            y_slots = (0,) if y_index == 0 else (y_index, (-y_index) % count_y)
            coefficients[x_index, y_index] = float(
                sum(fourier[left, right] for left in x_slots for right in y_slots).real
            )

    controls = (
        (0.123, 0.456),
        (0.777, 2.222),
        (1.2, 3.1),
        (2.9, 1.7),
    )
    reconstruction = max(
        abs(
            chebyshev.chebval2d(np.cos(wave), np.cos(frequency), coefficients)
            - odd_e5(union, odd, wave, frequency, block74.MU)
        )
        for wave, frequency in controls
    )
    scale = max(float(np.max(np.abs(sampled))), np.finfo(float).tiny)

    k_zero = brentq(
        lambda wave: odd_e5(union, odd, wave, 0.0, block74.MU),
        0.08,
        0.10,
        xtol=1.0e-14,
    )
    k_global = brentq(
        lambda wave: odd_e5(union, odd, wave, np.pi, block74.MU),
        0.08,
        0.10,
        xtol=1.0e-14,
    )
    certified_boundary = k_global - (0.002 if mutation == "threshold_input" else 0.0)
    power = chebyshev_to_power(coefficients)
    rectangle = transform_rectangle(power, -1.0, np.cos(certified_boundary))
    bernstein_safe = power_to_bernstein(rectangle)

    safe_grid_minimum = np.inf
    for wave in np.linspace(k_global + 1.0e-5, np.pi, 19):
        for frequency in np.linspace(0.0, np.pi, 17):
            fiber = physical_fiber(
                union,
                odd,
                np.asarray((wave, 0.0, 0.0, frequency)),
                block74.MU,
            )
            safe_grid_minimum = min(
                safe_grid_minimum, float(np.linalg.eigvalsh(fiber.reduced)[0])
            )
    rank_one_residual = 0.0
    rank_one_ward = 0.0
    norm_values = []
    for frequency in (0.0, 0.7, np.pi):
        momentum = np.asarray((0.3, 0.0, 0.0, frequency), dtype=complex)
        baseline = (
            odd.edge_basis.T
            @ (-block74.cross_action_symbol(union, momentum, 0.0))
            @ odd.edge_basis
        )
        supplied = (
            odd.edge_basis.T
            @ (-block74.cross_action_symbol(union, momentum, block74.MU))
            @ odd.edge_basis
        )
        update = (baseline - supplied) / block74.MU
        vector = np.asarray(
            (
                1.0 + np.exp(-1.0j * frequency),
                np.sqrt(2.0),
                0.0,
                0.0,
                -np.sqrt(2.0) * np.exp(-1.0j * frequency),
                0.0,
            ),
            dtype=complex,
        )
        expected = np.outer(vector, vector.conj())
        rank_one_residual = max(
            rank_one_residual,
            float(np.linalg.norm(update - expected) / np.linalg.norm(expected)),
        )
        ward = (
            odd.edge_basis.T
            @ block48.union_gauge_map(union, momentum)
            @ odd.gauge_basis
        )
        rank_one_ward = max(
            rank_one_ward, float(np.linalg.norm(vector.conj() @ ward))
        )
        norm_values.append(float(np.vdot(vector, vector).real))

    return AxialPolynomialCertificate(
        coefficients=coefficients,
        bernstein_safe=bernstein_safe,
        relative_reconstruction=float(reconstruction / scale),
        k_zero=float(k_zero),
        k_global=float(k_global),
        safe_grid_minimum=float(safe_grid_minimum),
        rank_one_residual=rank_one_residual,
        rank_one_ward=rank_one_ward,
        rank_one_norm_range=(min(norm_values), max(norm_values)),
    )


def periodic_phase_data(union, odd: Sector, mutation: str) -> dict[str, float | tuple[int, int, int]]:
    hostile_length = 70 if mutation == "periodic_input" else 72
    hostile_k = 2.0 * np.pi / hostile_length
    safe_k = 2.0 * np.pi / 71.0
    hostile = physical_fiber(
        union, odd, np.asarray((hostile_k, 0.0, 0.0, 0.0)), block74.MU
    )
    safe_static = physical_fiber(
        union, odd, np.asarray((safe_k, 0.0, 0.0, 0.0)), block74.MU
    )

    transition_frequency = brentq(
        lambda frequency: float(
            np.linalg.eigvalsh(
                physical_fiber(
                    union,
                    odd,
                    np.asarray((safe_k, 0.0, 0.0, frequency)),
                    block74.MU,
                ).reduced
            )[0]
        ),
        0.0,
        np.pi,
        xtol=1.0e-14,
    )
    transition = physical_fiber(
        union,
        odd,
        np.asarray((safe_k, 0.0, 0.0, transition_frequency)),
        block74.MU,
    )
    hostile_values = np.linalg.eigvalsh(hostile.reduced)
    safe_values = np.linalg.eigvalsh(safe_static.reduced)
    transition_values = np.linalg.eigvalsh(transition.reduced)
    return {
        "hostile_length": float(hostile_length),
        "hostile_k": hostile_k,
        "safe_k": safe_k,
        "hostile_minimum": float(hostile_values[0]),
        "safe_minimum": float(safe_values[0]),
        "hostile_inertia": inertia_values(hostile_values),
        "safe_inertia": inertia_values(safe_values),
        "transition_frequency": float(transition_frequency),
        "transition_eigenvalue": float(transition_values[np.argmin(np.abs(transition_values))]),
        "transition_border_singular": float(
            np.linalg.svd(transition.bordered, compute_uv=False)[-1]
        ),
    }


def record_edge_source(union, direction: tuple[int, int, int]) -> np.ndarray:
    edge_index = {value: slot for slot, value in enumerate(union.directions)}
    carrier = block68.canonical_carrier(
        tuple(union.directions), np.asarray(direction, dtype=int)
    )
    if carrier is None:
        raise AssertionError("the reflected union must carry every signed Record ray")
    edge, _offset = carrier
    source = np.zeros(len(union.directions), dtype=complex)
    source[edge_index[edge]] = 2.0
    return source


def source_quotient_data(union, odd: Sector, mutation: str) -> dict[str, float]:
    local = block74.local_tt_observables(union, "")[0]
    record = (
        record_edge_source(union, (0, 1, 0))
        + record_edge_source(union, (0, -1, 0))
        - record_edge_source(union, (0, 0, 1))
        - record_edge_source(union, (0, 0, -1))
    ) / (2.0 * np.sqrt(2.0))
    if mutation == "source_input":
        record = record + 0.1 * local

    wave_number = 2.0 * np.pi / 72.0
    momentum = np.asarray((wave_number, 0.0, 0.0, 0.0), dtype=complex)
    fiber = physical_fiber(union, odd, momentum, block74.MU)
    local_odd = odd.edge_basis.T @ local
    record_odd = odd.edge_basis.T @ record
    difference = record - local
    difference_odd = record_odd - local_odd
    metric = block48.metric_coefficients(np.asarray(union.directions, dtype=float))
    gauge = block48.union_gauge_map(union, momentum)
    projector = odd.edge_basis @ odd.edge_basis.T
    multiplier = 72.0 * (1.0 - np.exp(1.0j * wave_number))

    def response(source: np.ndarray) -> float:
        return float(np.vdot(source, fiber.covariance @ source).real)

    return {
        "local_odd_residual": float(np.linalg.norm(local - projector @ local)),
        "record_odd_residual": float(np.linalg.norm(record - projector @ record)),
        "metric_match": float(np.linalg.norm(metric.T @ difference)),
        "local_ward": float(np.linalg.norm(local.conj() @ gauge)),
        "record_ward": float(np.linalg.norm(record.conj() @ gauge)),
        "line_multiplier": float(abs(multiplier)),
        "local_response": response(local_odd),
        "record_response": response(record_odd),
        "difference_response": response(difference_odd),
        "cross_response": float(
            np.vdot(local_odd, fiber.covariance @ record_odd).real
        ),
        "scaled_record_response": float(abs(multiplier) ** 2 * response(record_odd)),
    }


def tt_visibility_data(union, odd: Sector, mutation: str) -> dict[str, float]:
    source = odd.edge_basis.T @ block74.local_tt_observables(union, "")[0]
    if mutation == "tt_input":
        source = source + 0.01 * odd.edge_basis.T @ record_edge_source(
            union, (0, 1, 0)
        )
    wave_number = 2.0 * np.pi / 72.0
    densities = []
    for frequency in np.linspace(0.0, 2.0 * np.pi, 256, endpoint=False):
        fiber = physical_fiber(
            union,
            odd,
            np.asarray((wave_number, 0.0, 0.0, frequency)),
            block74.MU,
        )
        densities.append(float(np.vdot(source, fiber.covariance @ source).real))

    critical = brentq(
        lambda wave: float(
            np.linalg.eigvalsh(
                physical_fiber(
                    union,
                    odd,
                    np.asarray((wave, 0.0, 0.0, 0.0)),
                    block74.MU,
                ).reduced
            )[0]
        ),
        0.08,
        0.10,
        xtol=1.0e-14,
    )
    at_root = physical_fiber(
        union, odd, np.asarray((critical, 0.0, 0.0, 0.0)), block74.MU
    )
    root_values, root_vectors = np.linalg.eigh(at_root.reduced)
    root_slot = int(np.argmin(np.abs(root_values)))
    root_edge = at_root.quotient @ root_vectors[:, root_slot]
    overlap = float(abs(np.vdot(source, root_edge)))

    nearby = []
    for offset in (-3.0e-12, 3.0e-12):
        fiber = physical_fiber(
            union,
            odd,
            np.asarray((critical + offset, 0.0, 0.0, 0.0)),
            block74.MU,
        )
        nearby.append(float(np.vdot(source, fiber.covariance @ source).real))
    return {
        "density_minimum": min(densities),
        "density_maximum": max(densities),
        "static_residue": wave_number**2 * densities[0],
        "critical": float(critical),
        "critical_overlap": overlap,
        "below_response": nearby[0],
        "above_response": nearby[1],
    }


def odd_metric_basis() -> np.ndarray:
    basis = np.zeros((len(block48.HCOMPS), 3), dtype=float)
    root_two = np.sqrt(2.0)
    basis[block48.HCOMPS.index((1, 1)), 0] = 1.0 / root_two
    basis[block48.HCOMPS.index((2, 2)), 0] = -1.0 / root_two
    basis[block48.HCOMPS.index((0, 1)), 1] = 1.0 / root_two
    basis[block48.HCOMPS.index((0, 2)), 1] = -1.0 / root_two
    basis[block48.HCOMPS.index((1, 3)), 2] = 1.0 / root_two
    basis[block48.HCOMPS.index((2, 3)), 2] = -1.0 / root_two
    return basis


def metric_reduction_data(union, odd: Sector, mutation: str) -> dict[str, float]:
    metric_basis = odd_metric_basis()
    maximum_gauge_lift = 0.0
    minimum_reduced = np.inf
    for wave_number in np.linspace(0.001, np.pi, 41):
        for frequency in np.linspace(0.0, np.pi, 65):
            momentum = np.asarray(
                (wave_number, 0.0, 0.0, frequency), dtype=complex
            )
            metric = block49.union_line_metric_map(union, momentum) @ metric_basis
            gauge = block48.union_gauge_map(union, momentum) @ odd.gauge_basis
            metric_gauge = np.linalg.lstsq(metric, gauge, rcond=None)[0]
            maximum_gauge_lift = max(
                maximum_gauge_lift,
                float(np.linalg.norm(metric @ metric_gauge - gauge)),
            )
            quotient = null_space(metric_gauge.conj().T, rcond=1.0e-11)
            operator = -block74.cross_action_symbol(union, momentum, block74.MU)
            reduced = quotient.conj().T @ metric.conj().T @ operator @ metric @ quotient
            reduced = 0.5 * (reduced + reduced.conj().T)
            minimum_reduced = min(
                minimum_reduced, float(np.linalg.eigvalsh(reduced)[0])
            )

    wave_number = 2.0 * np.pi / 72.0
    momentum = np.asarray((wave_number, 0.0, 0.0, 0.0), dtype=complex)
    metric = block49.union_line_metric_map(union, momentum) @ metric_basis
    gauge = block48.union_gauge_map(union, momentum) @ odd.gauge_basis
    metric_gauge = np.linalg.lstsq(metric, gauge, rcond=None)[0]
    quotient = null_space(metric_gauge.conj().T, rcond=1.0e-11)
    operator = -block74.cross_action_symbol(union, momentum, block74.MU)
    reduced = quotient.conj().T @ metric.conj().T @ operator @ metric @ quotient
    reduced = 0.5 * (reduced + reduced.conj().T)

    local = block74.local_tt_observables(union, "")[0]
    record = (
        record_edge_source(union, (0, 1, 0))
        + record_edge_source(union, (0, -1, 0))
        - record_edge_source(union, (0, 0, 1))
        - record_edge_source(union, (0, 0, -1))
    ) / (2.0 * np.sqrt(2.0))
    local_stress = quotient.conj().T @ metric.conj().T @ local
    record_stress = quotient.conj().T @ metric.conj().T @ record
    local_response = float(
        np.vdot(local_stress, np.linalg.solve(reduced, local_stress)).real
    )
    record_response = float(
        np.vdot(record_stress, np.linalg.solve(reduced, record_stress)).real
    )

    raw = physical_fiber(union, odd, momentum, block74.MU)
    odd_metric = odd.edge_basis.T @ metric
    projector = odd_metric @ np.linalg.pinv(odd_metric, rcond=1.0e-11)
    projected_local = projector @ (odd.edge_basis.T @ local)
    projected_record = projector @ (odd.edge_basis.T @ record)
    post_inversion_response = float(
        np.vdot(projected_local, raw.covariance @ projected_local).real
    )
    if mutation == "reduction_input":
        local_response = post_inversion_response

    return {
        "maximum_gauge_lift": maximum_gauge_lift,
        "minimum_reduced": minimum_reduced,
        "stress_match": float(np.linalg.norm(local_stress - record_stress)),
        "local_response": local_response,
        "record_response": record_response,
        "projected_source_match": float(
            np.linalg.norm(projected_local - projected_record)
        ),
        "post_inversion_response": post_inversion_response,
        "l72_reduced_minimum": float(np.linalg.eigvalsh(reduced)[0]),
    }


def repair_data(union, odd: Sector, mutation: str) -> dict[str, object]:
    repair_mu = block74.MU if mutation == "repair_input" else -block74.MU
    structural = block74.structural_certificate(union, repair_mu, "")
    sources = block74.source_certificate(
        union, (repair_mu, 2.0 * repair_mu), False, ""
    )
    static = block74.static_source_certificate(union, repair_mu, "")
    wave_number = 2.0 * np.pi / 72.0
    fiber = physical_fiber(
        union,
        odd,
        np.asarray((wave_number, 0.0, 0.0, 0.0)),
        repair_mu,
    )
    local = odd.edge_basis.T @ block74.local_tt_observables(union, "")[0]
    record = odd.edge_basis.T @ (
        (
            record_edge_source(union, (0, 1, 0))
            + record_edge_source(union, (0, -1, 0))
            - record_edge_source(union, (0, 0, 1))
            - record_edge_source(union, (0, 0, -1))
        )
        / (2.0 * np.sqrt(2.0))
    )
    return {
        "mu": repair_mu,
        "zero_inertia": structural["zero_inertia"],
        "nullities": structural["nullities"],
        "ward": structural["ward"],
        "reflection": structural["reflection"],
        "hermiticity": structural["hermiticity"],
        "source_samples": sources.samples,
        "source_nullities": sources.nullities,
        "source_ward": sources.maximum_ward,
        "source_residuals": sources.maximum_relative_residual,
        "selection_ratio": sources.selection_ratio,
        "static_residues": static["residues"],
        "static_nonmetric": static["nonmetric"],
        "odd_minimum": float(np.linalg.eigvalsh(fiber.reduced)[0]),
        "local_response": float(np.vdot(local, fiber.covariance @ local).real),
        "record_response": float(np.vdot(record, fiber.covariance @ record).real),
    }


def even_counterexample_data(union, even: Sector, mutation: str) -> dict[str, object]:
    mu = -block74.MU

    def indexed_eigenvalue(frequency: float) -> float:
        fiber = physical_fiber(
            union,
            even,
            np.asarray((np.pi / 2.0, 0.0, 0.0, frequency)),
            mu,
        )
        return float(np.linalg.eigvalsh(fiber.reduced)[3])

    root = brentq(indexed_eigenvalue, 1.05, 1.07, xtol=1.0e-14)
    root_fiber = physical_fiber(
        union,
        even,
        np.asarray((np.pi / 2.0, 0.0, 0.0, root)),
        mu,
    )
    root_values, root_vectors = np.linalg.eigh(root_fiber.reduced)
    root_edge = root_fiber.quotient @ root_vectors[:, 3]
    source = even.edge_basis.T @ block74.local_tt_observables(union, "")[1]
    if mutation == "even_input":
        source = np.zeros_like(source)

    side_inertias = []
    responses = []
    for offset in (-1.0e-7, 1.0e-7):
        fiber = physical_fiber(
            union,
            even,
            np.asarray((np.pi / 2.0, 0.0, 0.0, root + offset)),
            mu,
        )
        side_inertias.append(
            inertia_values(np.linalg.eigvalsh(fiber.reduced), tolerance=1.0e-11)
        )
        responses.append(float(np.vdot(source, fiber.covariance @ source).real))

    curvature_null_inertias = []
    for frequency in (0.0, root, np.pi):
        q = np.asarray((np.pi / 2.0, 0.0, 0.0, frequency), dtype=complex)
        fiber = physical_fiber(union, even, q, 0.0)
        curvature = (
            block49.centered_curvature_intertwiner(union, q)
            @ even.edge_basis
            @ fiber.quotient
        )
        kernel = null_space(curvature, rcond=1.0e-11)
        restricted = kernel.conj().T @ fiber.reduced @ kernel
        restricted = 0.5 * (restricted + restricted.conj().T)
        curvature_null_inertias.append(inertia_values(np.linalg.eigvalsh(restricted)))

    return {
        "root": float(root),
        "root_eigenvalue": float(root_values[3]),
        "root_border_singular": float(
            np.linalg.svd(root_fiber.bordered, compute_uv=False)[-1]
        ),
        "root_inertia": inertia_values(root_values),
        "side_inertias": tuple(side_inertias),
        "source_overlap": float(abs(np.vdot(source, root_edge))),
        "responses": tuple(responses),
        "curvature_null_inertias": tuple(curvature_null_inertias),
    }


def main() -> int:
    started = time.perf_counter()
    mutation = os.environ.get("TOE_MUTATION", "")
    if mutation and mutation not in MUTATIONS:
        raise ValueError(f"unknown TOE_MUTATION={mutation!r}")

    checks = Checks()
    union = block48.build_reflection_union()
    odd = sector(union, -1)
    even = sector(union, +1)
    binding_mu = 2.0 * block74.MU if mutation == "action_input" else block74.MU
    binding_gate = (
        binding_mu == 1.0 / 1024.0
        and len(union.directions) == 22
        and odd.edge_basis.shape == (22, 6)
        and odd.gauge_basis.shape == (4, 1)
        and even.edge_basis.shape == (22, 16)
        and even.gauge_basis.shape == (4, 3)
        and NOTE_PATH.exists()
        and AXIOM_PATH.exists()
        and PARENT_PATH.exists()
        and SOURCE_PARENT_PATH.exists()
    )
    checks.check(
        "supplied-action-sector-source-binding",
        "the literal mu=1/1024 action, both y/z sectors, and supplied Record carriers are bound without fitting",
        binding_gate,
        f"edges={len(union.directions)}; odd={odd.edge_basis.shape}/{odd.gauge_basis.shape}; even={even.edge_basis.shape}/{even.gauge_basis.shape}",
    )

    polynomial = axial_polynomial_certificate(union, odd, mutation)
    polynomial_gate = (
        polynomial.relative_reconstruction < 1.0e-11
        and 0.08841 < polynomial.k_zero < 0.08843
        and 0.08908 < polynomial.k_global < 0.08910
        and polynomial.k_global > polynomial.k_zero
        and np.min(polynomial.bernstein_safe) > -1.0e-7
        and np.max(polynomial.bernstein_safe) > 700.0
        and polynomial.safe_grid_minimum > 1.0e-7
        and polynomial.rank_one_residual < 1.0e-12
        and polynomial.rank_one_ward < 1.0e-12
        and abs(polynomial.rank_one_norm_range[0] - 4.0) < 1.0e-12
        and abs(polynomial.rank_one_norm_range[1] - 8.0) < 1.0e-12
    )
    checks.check(
        "global-axial-odd-rank-five-phase-boundary",
        "a degree-(5,4) bivariate Bernstein certificate localizes the full-circle PSD boundary",
        polynomial_gate,
        f"k0={polynomial.k_zero:.15f}; k*={polynomial.k_global:.15f}; Bernstein min={np.min(polynomial.bernstein_safe):.2e}; rank1={polynomial.rank_one_residual:.1e}; heldout={polynomial.relative_reconstruction:.2e}",
    )

    periodic = periodic_phase_data(union, odd, mutation)
    periodic_gate = (
        periodic["hostile_length"] == 72.0
        and periodic["hostile_inertia"] == (1, 4, 0)
        and periodic["safe_inertia"] == (0, 5, 0)
        and periodic["hostile_minimum"] < -7.0e-5
        and periodic["safe_minimum"] > 5.0e-6
        and 0.6912 < periodic["transition_frequency"] < 0.6914
        and abs(periodic["transition_eigenvalue"]) < 1.0e-12
        and periodic["transition_border_singular"] < 1.0e-10
    )
    checks.check(
        "periodic-ir-negative-band-and-transition-pole",
        "L=72 lies in the all-frequency negative band while L=71 carries an exact temporal unit-circle pole",
        periodic_gate,
        f"L72 min={periodic['hostile_minimum']:.3e}; L71 static={periodic['safe_minimum']:.3e}; theta_pole={periodic['transition_frequency']:.12f}; sigma={periodic['transition_border_singular']:.2e}",
    )

    source = source_quotient_data(union, odd, mutation)
    source_gate = (
        source["local_odd_residual"] < 1.0e-12
        and source["record_odd_residual"] < 1.0e-12
        and source["metric_match"] < 1.0e-12
        and source["local_ward"] < 1.0e-12
        and source["record_ward"] < 1.0e-12
        and source["line_multiplier"] > 6.0
        and source["local_response"] > 250.0
        and source["record_response"] < -19000.0
        and source["difference_response"] < -19000.0
        and abs(source["cross_response"] - source["local_response"]) < 0.2
        and source["scaled_record_response"] < -7.0e5
    )
    checks.check(
        "same-metric-record-source-quotient-obstruction",
        "two Ward-conserved odd sources with identical metric stress have opposite-sign covariance responses",
        source_gate,
        f"M^T(r-o)={source['metric_match']:.2e}; oCo={source['local_response']:.6f}; rCr={source['record_response']:.6f}; dCd={source['difference_response']:.6f}",
    )

    tt = tt_visibility_data(union, odd, mutation)
    tt_gate = (
        tt["density_minimum"] > 0.50
        and tt["density_maximum"] > 260.0
        and 2.001 < tt["static_residue"] < 2.002
        and abs(tt["critical"] - polynomial.k_zero) < 1.0e-11
        and tt["critical_overlap"] > 8.0e-6
        and tt["below_response"] < -100.0
        and tt["above_response"] > 500.0
    )
    checks.check(
        "tt-newtonian-subchannel-hides-but-does-not-remove-pole",
        "the sampled local TT density stays positive with k^2 C near two, yet its tiny nonzero pole overlap is resolved",
        tt_gate,
        f"rho=[{tt['density_minimum']:.6f},{tt['density_maximum']:.6f}]; k2C={tt['static_residue']:.9f}; overlap={tt['critical_overlap']:.3e}; sides={tt['below_response']:.2f}/{tt['above_response']:.2f}",
    )

    reduction = metric_reduction_data(union, odd, mutation)
    reduction_gate = (
        reduction["maximum_gauge_lift"] < 3.0e-13
        and reduction["minimum_reduced"] > 2.0e-7
        and reduction["stress_match"] < 1.0e-12
        and 262.7 < reduction["local_response"] < 262.9
        and abs(reduction["local_response"] - reduction["record_response"]) < 1.0e-10
        and reduction["projected_source_match"] < 1.0e-12
        and reduction["post_inversion_response"] < -4600.0
        and reduction["l72_reduced_minimum"] > 0.0018
    )
    checks.check(
        "metric-first-reduction-constructive-escape",
        "restricting the action before inversion gives a positive source-faithful odd metric quotient on the declared atlas",
        reduction_gate,
        f"grid min={reduction['minimum_reduced']:.3e}; M-gauge={reduction['maximum_gauge_lift']:.2e}; reduced o/r={reduction['local_response']:.6f}/{reduction['record_response']:.6f}; P C P={reduction['post_inversion_response']:.3f}",
    )

    repair = repair_data(union, odd, mutation)
    repair_gate = (
        repair["mu"] == -1.0 / 1024.0
        and repair["zero_inertia"] == (10, 2, 10)
        and repair["nullities"] == (4,)
        and repair["ward"] < 2.0e-13
        and repair["reflection"] < 1.0e-13
        and repair["hermiticity"] < 1.0e-13
        and repair["source_samples"] == 6528
        and repair["source_nullities"] == (4,)
        and repair["source_ward"] < 1.0e-12
        and max(repair["source_residuals"]) < 1.2e-10
        and repair["selection_ratio"] < -0.6
        and max(abs(value - 2.0) for value in repair["static_residues"][:4]) < 0.002
        and repair["odd_minimum"] > 0.002
        and repair["local_response"] > 250.0
        and repair["record_response"] > 500.0
    )
    checks.check(
        "equal-magnitude-negative-sign-odd-repair-counterfactual",
        "mu=-1/1024 repairs the odd IR sign while preserving Ward, source solves, and the static residue",
        repair_gate,
        f"zero inertia={repair['zero_inertia']}; 6528 residual={max(repair['source_residuals']):.2e}; odd min={repair['odd_minimum']:.3e}; o/r={repair['local_response']:.3f}/{repair['record_response']:.3f}",
    )

    even = even_counterexample_data(union, even, mutation)
    even_gate = (
        1.0582 < even["root"] < 1.0584
        and abs(even["root_eigenvalue"]) < 1.0e-11
        and even["root_border_singular"] < 1.0e-10
        and even["root_inertia"] == (3, 9, 1)
        and even["side_inertias"] == ((3, 10, 0), (4, 9, 0))
        and even["source_overlap"] > 4.0e-4
        and even["responses"][0] > 500.0
        and even["responses"][1] < -500.0
        and even["curvature_null_inertias"] == ((3, 8, 0),) * 3
    )
    checks.check(
        "even-sector-sign-flip-and-curvature-null-wall",
        "the equal sign flip creates a cross-TT-visible even pole and cannot alter three curvature-null negative directions",
        even_gate,
        f"theta={even['root']:.15f}; sigma={even['root_border_singular']:.2e}; overlap={even['source_overlap']:.3e}; C sides={even['responses'][0]:.2f}/{even['responses'][1]:.2f}; kerD={even['curvature_null_inertias']}",
    )

    note = flat(NOTE_PATH)
    if mutation == "note_boundary":
        note = note.replace("gravity_verdict: open", "gravity_verdict: closed")
    axiom = flat(AXIOM_PATH)
    scope_gate = (
        "raw_full_source_matrix_gns_verdict: bounded_infeasible" in note
        and "equal_magnitude_sign_flip_verdict: bounded_infeasible" in note
        and "physical_reduction_verdict: open" in note
        and "gravity_verdict: open" in note
        and "no axiom is amended" in note
        and "zero obligation retirement" in note
        and all(f"### n{index}" in note for index in range(1, 9))
        and "n1--n8 status: pass" in note
        and "choose a hamiltonian or transfer operator" in axiom
    )
    checks.check(
        "no-go-discipline-axiom-and-toe-boundary",
        "the two route failures are bounded while physical reduction, changed action, gravity, and axioms remain open",
        scope_gate,
        "raw full-source GNS and the tested sign flip stop; selected TT/constraint sections, other actions, nonlinear gravity, and Record dynamics remain live",
    )

    print(
        "AXIAL_PHASE_CERTIFICATE: in the odd sector k>=0.0890875879243 is rank-five PSD on the full temporal circle; a transition shell and an infrared negative band lie below"
    )
    print(
        "SOURCE_QUOTIENT_CERTIFICATE: at L=72, M^T r=M^T o and both sources are Ward-conserved, but r^dag C r<0<o^dag C o, so the raw covariance does not descend to metric-source classes"
    )
    print(
        "METRIC_REDUCTION_CERTIFICATE: reducing the action to the common-metric image before inversion restores representative independence and a positive tested odd quotient; projecting sources after raw inversion does not"
    )
    print(
        "SIGN_COUNTERFACTUAL_CERTIFICATE: mu=-1/1024 repairs the tested odd infrared fiber and retains the inherited source/Newtonian gates, but creates a cross-TT-visible even-sector unit-circle pole"
    )
    print(
        "CURVATURE_NULL_CERTIFICATE: on the tested even fibers, ker D within the conserved quotient has inertia (3-,8+), so changing only the coefficient of D^dag D cannot make the raw full-source form positive"
    )
    print(
        "PHYSICAL_DECISION: derive a source/constraint section or a different action from independent physics before returning to quantum GNS and Record construction"
    )
    print(
        "N5_CERTIFICATE: the execution resolutions below state exactly what this runner did and did not resolve"
    )
    print(
        "per_element: checked all six odd edge coordinates, all sixteen even edge coordinates, their one/three Ward columns, and two equal-metric source representatives"
    )
    print(
        "per_site: checked closed neutral Record-line pairs on the exact L=71 and L=72 periodic witnesses; no arbitrary inhomogeneous lattice is claimed"
    )
    print(
        "per_mode: certified the full axial odd temporal circle above the global threshold and localized odd/even unit-circle poles below it"
    )
    print(
        "per_block: checked the supplied action, source quotient, equal-magnitude sign counterfactual, inherited 6528-source battery, and static residue"
    )
    print(
        "lattice_wide: checked and not executed — no off-axis full Brillouin zone, nonlinear background, canonical reduction, refinement, quantum Record, or gravity theorem is claimed"
    )
    print(
        "RAW_FULL_SOURCE_MATRIX_GNS_VERDICT: BOUNDED_INFEASIBLE; EQUAL_MAGNITUDE_SIGN_FLIP_VERDICT: BOUNDED_INFEASIBLE; PHYSICAL_REDUCTION_VERDICT: OPEN; GRAVITY_VERDICT: OPEN"
    )
    print("TOE_MOVEMENT: obligations=0 percentages=0 axioms_amended=0")
    print(f"elapsed_sec={time.perf_counter() - started:.2f}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
