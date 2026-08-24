#!/usr/bin/env python3
"""Derive the half-space Weyl form and test reflection-completion radicals.

The scope is one supplied reflected-curvature action, the odd y/z sector, and
spatial momentum (pi/2,0,0).  Equal-boundary Feshbach positivity is separated
from OS positivity.  The negative result concerns the declared link/site
cross-action forms and fixed on-site action-covariant intertwiners only.
"""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
import sys
import time

import numpy as np
from scipy import linalg
from scipy.optimize import linear_sum_assignment


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_2026_08_24 as block182  # noqa: E402


AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_WEYL_FESHBACH_REFLECTION_RADICAL_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_WEYL_FESHBACH_REFLECTION_RADICAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_DESCRIPTOR_HALFSPACE_SOURCE_FAITHFUL_METRIC_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_CANONICAL_REDUCTION_SCHUR_POLE_TT_SPECTRAL_WEIGHT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_reflected_curvature_weyl_feshbach_reflection_radical_boundary_2026_08_24.py",
    "scripts/admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_2026_08_24.py",
    "scripts/admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_2026_08_23.py",
    "scripts/admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14.py",
    "scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py",
    "scripts/admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py",
    "scripts/admissibility_cycle713_record_stress_block44_ir_reflected_carrier_boundary_2026_08_13.py",
    "scripts/admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11.py",
)

MUTATIONS = (
    "reflection_input",
    "stable_graph_input",
    "feshbach_input",
    "link_reflection_input",
    "site_reflection_input",
    "commutant_input",
    "scalar_sign_input",
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
            clipped = detail if len(detail) <= 170 else detail[:167] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


@dataclass(frozen=True)
class StableData:
    transfer: np.ndarray
    weyl: np.ndarray
    selected_count: int
    endpoint_count: int
    boundary_condition: float
    root_match: float
    spectral_radius: float
    complex_count: int
    hermiticity: float
    subspace_angle: float
    graph_residual: float
    qz_transfer_error: float


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def inertia(matrix: np.ndarray, tolerance: float = 1.0e-10) -> tuple[int, int, int]:
    values = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    return (
        int(np.sum(values < -tolerance)),
        int(np.sum(values > tolerance)),
        int(np.sum(np.abs(values) <= tolerance)),
    )


def geometric_reflection(union, edge_basis: np.ndarray, mutation: str = "") -> np.ndarray:
    momentum = np.asarray(
        (block182.block181.SPATIAL_WAVE_NUMBER, 0.0, 0.0, 0.0), dtype=complex
    )
    edge = (
        edge_basis.T
        @ block182.block181.block74.block48.union_time_reflection_matrix(
            union, momentum
        )
        @ edge_basis
    )
    reflection = np.zeros((7, 7), dtype=complex)
    reflection[:6, :6] = edge
    reflection[6, 6] = 1.0
    if mutation == "reflection_input":
        reflection[0, 0] += 1.0e-2
    return reflection


def projective_match(values: np.ndarray, expected: np.ndarray) -> float:
    cost = np.asarray(
        [
            [
                abs(value - target)
                / (
                    np.sqrt(1.0 + abs(value) ** 2)
                    * np.sqrt(1.0 + abs(target) ** 2)
                )
                for target in expected
            ]
            for value in values
        ]
    )
    rows, columns = linear_sum_assignment(cost)
    return float(np.max(cost[rows, columns]))


def stable_weyl(
    coefficients: tuple[np.ndarray, ...],
    finite_inside: np.ndarray,
    mutation: str = "",
) -> StableData:
    local = tuple(value.copy() for value in coefficients)
    if mutation == "stable_graph_input":
        changed = list(local)
        changed[2] = changed[2] + 2.0e-2 * np.eye(7)
        local = tuple(changed)

    left, right = block182.strong_companion(local)

    def select(alpha, beta):
        scale = np.maximum(np.abs(alpha), np.abs(beta))
        finite = np.abs(beta) > 1.0e-10 * scale
        return finite & (np.abs(alpha) < (1.0 - 1.0e-8) * np.abs(beta))

    _, _, alpha, beta, _, vectors = linalg.ordqz(
        left, right, sort=select, output="complex"
    )
    selected = int(np.sum(select(alpha, beta)))
    if selected != 14:
        return StableData(
            transfer=np.full((14, 14), np.nan),
            weyl=np.full((14, 14), np.nan),
            selected_count=selected,
            endpoint_count=-1,
            boundary_condition=np.inf,
            root_match=np.inf,
            spectral_radius=np.inf,
            complex_count=-1,
            hermiticity=np.inf,
            subspace_angle=np.inf,
            graph_residual=np.inf,
            qz_transfer_error=np.inf,
        )

    qz_stable = vectors[:, :selected]

    endpoint_toeplitz = np.block(
        [
            [local[0], np.zeros((7, 7)), np.zeros((7, 7))],
            [local[1], local[0], np.zeros((7, 7))],
            [local[2], local[1], local[0]],
        ]
    )
    endpoint = linalg.null_space(endpoint_toeplitz, rcond=1.0e-12)
    endpoint_columns = []
    for column in range(endpoint.shape[1]):
        chain = endpoint[:, column]
        endpoint_columns.append(
            np.concatenate((chain[14:21], chain[7:14], chain[:7], np.zeros(7)))
        )

    laurent = {index - 2: value for index, value in enumerate(local)}
    finite_columns = []
    for root in finite_inside:
        matrix = block182.block181.evaluate_laurent(laurent, root)
        _, _, right_h = np.linalg.svd(matrix)
        vector = right_h.conj().T[:, -1]
        finite_columns.append(
            np.concatenate((vector, root * vector, root**2 * vector, root**3 * vector))
        )
    explicit_columns = np.column_stack(endpoint_columns + finite_columns)
    explicit_stable, _ = np.linalg.qr(explicit_columns)
    boundary = explicit_stable[:14, :]
    future = explicit_stable[14:, :]
    singular = np.linalg.svd(boundary, compute_uv=False)
    explicit_transfer = future @ np.linalg.inv(boundary)
    qz_transfer = qz_stable[14:, :] @ np.linalg.inv(qz_stable[:14, :])
    transfer = qz_transfer
    transfer_values = np.linalg.eigvals(transfer)
    expected = np.concatenate((np.zeros(7), finite_inside**2))
    match = projective_match(transfer_values, expected)

    minus_two, minus_one, zero, plus_one, plus_two = local
    boundary_operator = np.block([[zero, plus_one], [minus_one, zero]])
    tail_operator = np.block(
        [[plus_two, np.zeros((7, 7))], [plus_one, plus_two]]
    )
    backward_operator = np.block(
        [[minus_two, minus_one], [np.zeros((7, 7)), minus_two]]
    )
    weyl = boundary_operator + tail_operator @ transfer
    graph_residual = float(
        np.linalg.norm(
            backward_operator
            + boundary_operator @ transfer
            + tail_operator @ transfer @ transfer
        )
        / (
            np.linalg.norm(backward_operator)
            + np.linalg.norm(boundary_operator @ transfer)
            + np.linalg.norm(tail_operator @ transfer @ transfer)
        )
    )
    selected_values = alpha[:selected] / beta[:selected]
    return StableData(
        transfer=transfer,
        weyl=weyl,
        selected_count=selected,
        endpoint_count=int(np.sum(np.abs(selected_values) < 1.0e-6)),
        boundary_condition=float(singular[0] / singular[-1]),
        root_match=match,
        spectral_radius=float(np.max(np.abs(transfer_values))),
        complex_count=int(np.sum(np.abs(transfer_values.imag) > 1.0e-7)),
        hermiticity=float(np.linalg.norm(weyl - weyl.conj().T)),
        subspace_angle=float(
            np.max(linalg.subspace_angles(explicit_stable, qz_stable))
        ),
        graph_residual=graph_residual,
        qz_transfer_error=float(
            np.linalg.norm(explicit_transfer - qz_transfer)
            / np.linalg.norm(qz_transfer)
        ),
    )


def finite_toeplitz(
    coefficients: tuple[np.ndarray, ...], depth: int
) -> np.ndarray:
    matrix = np.zeros((7 * depth, 7 * depth), dtype=complex)
    by_offset = {offset - 2: value for offset, value in enumerate(coefficients)}
    for row in range(depth):
        for offset, value in by_offset.items():
            column = row + offset
            if 0 <= column < depth:
                matrix[
                    7 * row : 7 * (row + 1),
                    7 * column : 7 * (column + 1),
                ] = value
    return matrix


def feshbach_data(
    coefficients: tuple[np.ndarray, ...],
    weyl: np.ndarray,
    source: np.ndarray,
    mutation: str = "",
) -> tuple[tuple[float, ...], tuple[int, int, int], float, float]:
    local = tuple(value.copy() for value in coefficients)
    if mutation == "feshbach_input":
        changed = list(local)
        changed[2] = changed[2] + 1.0e-2 * np.eye(7)
        local = tuple(changed)

    differences = []
    for depth in (4, 8, 16, 32):
        matrix = finite_toeplitz(local, depth)
        boundary = matrix[:14, :14]
        coupling = matrix[:14, 14:]
        interior = matrix[14:, 14:]
        finite_weyl = boundary - coupling @ np.linalg.solve(
            interior, coupling.conj().T
        )
        differences.append(
            float(np.linalg.norm(weyl - finite_weyl) / np.linalg.norm(finite_weyl))
        )

    covariance = np.linalg.inv(weyl)
    edge_indices = np.asarray(list(range(6)) + list(range(7, 13)))
    edge_covariance = covariance[np.ix_(edge_indices, edge_indices)]
    source_state = np.concatenate((source, np.zeros(7)))
    response = float((source_state.conj() @ covariance @ source_state).real)
    return (
        tuple(differences),
        inertia(edge_covariance),
        response,
        float(np.linalg.norm(edge_covariance - edge_covariance.conj().T)),
    )


def completion_data(
    kernel: np.ndarray, transfer: np.ndarray
) -> tuple[tuple[int, int, int], tuple[int, int, int], float, float, float]:
    values, vectors = np.linalg.eigh(0.5 * (kernel + kernel.conj().T))
    negative = values < -1.0e-10
    positive = values > 1.0e-10
    radical = ~(negative | positive)
    fundamental = (vectors * np.where(negative, -1.0, 1.0)) @ vectors.conj().T
    completed = fundamental @ kernel
    null_vectors = vectors[:, radical]
    range_vectors = vectors[:, ~radical]
    shifted_null = transfer @ null_vectors
    radical_leakage = float(
        np.linalg.norm(range_vectors.conj().T @ shifted_null)
        / max(float(np.linalg.norm(shifted_null)), 1.0e-300)
    )
    adjoint_residual = float(
        np.linalg.norm(completed @ transfer - transfer.conj().T @ completed)
        / max(float(np.linalg.norm(completed)), 1.0e-300)
    )
    return (
        inertia(kernel),
        inertia(completed),
        float(np.linalg.norm(fundamental @ fundamental - np.eye(len(kernel)))),
        radical_leakage,
        adjoint_residual,
    )


def finite_mode_transfer(
    coefficients: tuple[np.ndarray, ...], roots: np.ndarray
) -> tuple[np.ndarray, float]:
    laurent = {index - 2: value for index, value in enumerate(coefficients)}
    vectors = []
    for root in roots:
        matrix = block182.block181.evaluate_laurent(laurent, root)
        _, _, right_h = np.linalg.svd(matrix)
        vectors.append(right_h.conj().T[:, -1])
    modes = np.column_stack(vectors)
    singular = np.linalg.svd(modes, compute_uv=False)
    transfer = modes @ np.diag(roots) @ np.linalg.inv(modes)
    return transfer, float(singular[0] / singular[-1])


def commutant_data(
    coefficients: tuple[np.ndarray, ...], mutation: str = ""
) -> tuple[int, float]:
    family = coefficients if mutation != "commutant_input" else (coefficients[-1],)
    dimension = coefficients[0].shape[0]
    system = np.vstack(
        [
            np.kron(value.T, np.eye(dimension))
            - np.kron(np.eye(dimension), value)
            for value in family
        ]
    )
    singular = np.linalg.svd(system, compute_uv=False)
    rank = int(np.sum(singular > 1.0e-10 * singular[0]))
    gap = float(
        singular[-2] / max(float(singular[-1]), np.finfo(float).tiny)
    )
    return dimension**2 - rank, gap


def one_layer_commutant_data(
    coefficients: tuple[np.ndarray, ...], mutation: str = ""
) -> tuple[int, float, float]:
    local = coefficients
    if mutation == "commutant_input":
        zero = np.zeros_like(coefficients[0])
        local = (zero, zero, coefficients[-1], zero, zero)
    dimension = coefficients[0].shape[0]

    def commutator_map(value: np.ndarray) -> np.ndarray:
        return np.kron(value.T, np.eye(dimension)) - np.kron(
            np.eye(dimension), value
        )

    by_power = {power - 2: value for power, value in enumerate(local)}
    zero_map = np.zeros((dimension**2, dimension**2), dtype=complex)
    system = np.vstack(
        [
            np.hstack(
                (
                    commutator_map(by_power.get(power, np.zeros_like(local[0]))),
                    commutator_map(
                        by_power.get(power - 1, np.zeros_like(local[0]))
                    ),
                )
            )
            for power in range(-2, 4)
        ]
    )
    singular = np.linalg.svd(system, compute_uv=False)
    rank = int(np.sum(singular > 1.0e-10 * singular[0]))
    nullity = 2 * dimension**2 - rank
    _, _, right_h = np.linalg.svd(system, full_matrices=True)
    null_space = right_h.conj().T[:, rank:]
    identity = np.eye(dimension).reshape(-1, order="F")
    scalar_monomials = np.column_stack(
        (np.concatenate((identity, np.zeros_like(identity))),
         np.concatenate((np.zeros_like(identity), identity)))
    )
    scalar_monomials, _ = np.linalg.qr(scalar_monomials)
    distance = (
        float(np.max(linalg.subspace_angles(null_space, scalar_monomials)))
        if nullity == 2
        else np.inf
    )
    smallest_nonzero = float(singular[rank - 1]) if rank else 0.0
    return nullity, smallest_nonzero, distance


def scalar_escape(
    roots: np.ndarray, weights: np.ndarray, mutation: str = ""
) -> tuple[
    tuple[int, int, int],
    tuple[int, int, int],
    float,
    float,
    float,
    float,
    float,
    float,
    float,
    float,
]:
    local_weights = weights.copy()
    if mutation == "scalar_sign_input":
        local_weights = np.abs(local_weights)

    transfer = np.diag(roots)
    original = np.diag(local_weights)
    fundamental = np.diag(np.sign(local_weights))
    positive = original @ fundamental
    adjoint = float(np.linalg.norm(positive @ transfer - transfer.T @ positive))

    source = np.ones(3)
    source_adjoint_change = float(
        np.linalg.norm(positive @ source - original @ source)
    )
    positive_restriction_change = float(
        abs(np.sum(local_weights[local_weights < 0.0]))
    )

    vandermonde = np.vander(roots, 3, increasing=True)
    coefficients = np.linalg.solve(vandermonde, np.sign(local_weights))

    change = np.asarray([[1.0, 0.3, 0.0], [0.0, 1.0, 0.2], [0.1, 0.0, 1.0]])
    inverse = np.linalg.inv(change)
    changed_transfer = change @ transfer @ inverse
    changed_metric = inverse.T @ original @ inverse
    transported_sign = change @ fundamental @ inverse
    changed_positive = inverse.T @ positive @ inverse
    covariance_residual = float(
        max(
            np.linalg.norm(changed_metric @ transported_sign - changed_positive),
            np.linalg.norm(transported_sign @ transported_sign - np.eye(3)),
            np.linalg.norm(
                changed_transfer @ transported_sign
                - transported_sign @ changed_transfer
            ),
            np.linalg.norm(
                changed_positive @ changed_transfer
                - changed_transfer.T @ changed_positive
            ),
        )
    )

    moments = np.asarray(
        [np.sum(local_weights * roots**power) for power in range(9)]
    )
    hankel = np.asarray(
        [[moments[row + column] for column in range(3)] for row in range(3)]
    )
    even_hankel = np.asarray(
        [
            [moments[2 * (row + column)] for column in range(3)]
            for row in range(3)
        ]
    )
    return (
        inertia(original),
        inertia(positive),
        adjoint,
        source_adjoint_change,
        positive_restriction_change,
        float(np.max(np.abs(coefficients))),
        float(np.linalg.cond(vandermonde)),
        covariance_residual,
        float(np.linalg.det(hankel)),
        float(np.linalg.det(even_hankel)),
    )


def main() -> int:
    started = time.perf_counter()
    mutation = os.environ.get("TOE_MUTATION", "")
    if mutation and mutation not in MUTATIONS:
        raise ValueError(f"unknown TOE_MUTATION={mutation!r}")

    checks = Checks()
    union = block182.block181.block74.block48.build_reflection_union()
    border = block182.odd_border_data(union)
    coefficients = border.coefficients
    directions = np.asarray(union.directions, dtype=float)
    edge_basis = block182.block181.sign_basis(
        block182.block181.swap_matrix(directions, 1, 2), -1
    )
    baseline_reflection = geometric_reflection(union, edge_basis)
    tested_reflection = geometric_reflection(union, edge_basis, mutation)
    reflection_error = max(
        float(
            np.linalg.norm(
                tested_reflection.T @ coefficients[2 - exponent] @ tested_reflection
                - coefficients[2 + exponent]
            )
        )
        for exponent in (0, 1, 2)
    )
    reflection_gate = (
        reflection_error < 1.0e-12
        and np.linalg.norm(tested_reflection @ tested_reflection - np.eye(7))
        < 1.0e-12
        and np.linalg.norm(tested_reflection @ border.rhs - border.rhs) < 1.0e-12
        and border.ward_relative < 1.0e-12
        and border.gauge_ranks == (4, 4, 4, 4)
        and border.action_ranks == (18, 18, 18, 18)
    )
    checks.check(
        "action-geometric-reflection-and-source-binding",
        "the supplied action, Ward border, geometric reflection, and local TT source are mutually covariant",
        reflection_gate,
        f"reflection={reflection_error:.2e}; Ward={border.ward_relative:.2e}; ranks={border.action_ranks}",
    )

    laurent = block182.block181.laurent_certificate(union, "")
    branches = tuple(branch for branch in laurent.branches if branch.coupled)
    finite_inside = np.asarray([branch.root for branch in laurent.branches])
    baseline_stable = stable_weyl(coefficients, finite_inside)
    stable = (
        stable_weyl(coefficients, finite_inside, mutation)
        if mutation == "stable_graph_input"
        else baseline_stable
    )
    stable_gate = (
        stable.selected_count == 14
        and stable.endpoint_count == 7
        and stable.boundary_condition < 2.0
        and stable.root_match < 1.0e-6
        and stable.spectral_radius < 0.31
        and stable.complex_count == 4
        and stable.hermiticity < 1.0e-12
        and stable.subspace_angle < 1.0e-8
        and stable.graph_residual < 1.0e-12
        and stable.qz_transfer_error < 1.0e-8
        and inertia(stable.weyl) == (2, 12, 0)
    )
    checks.check(
        "stable-deflating-subspace-and-hermitian-weyl-form",
        "the full endpoint-plus-finite stable descriptor is a conditioned graph defining a Hermitian Weyl form",
        stable_gate,
        f"selected/end={stable.selected_count}/{stable.endpoint_count}; cond={stable.boundary_condition:.2f}; angle={stable.subspace_angle:.2e}; graph={stable.graph_residual:.2e}; qz={stable.qz_transfer_error:.2e}; rho={stable.spectral_radius:.6f}",
    )

    differences, edge_inertia, response, edge_hermiticity = feshbach_data(
        coefficients, baseline_stable.weyl, border.rhs, mutation
    )
    feshbach_gate = (
        all(later < earlier for earlier, later in zip(differences, differences[1:]))
        and differences[-1] < 1.0e-11
        and edge_inertia == (0, 11, 1)
        and response > 0.4
        and edge_hermiticity < 1.0e-12
    )
    checks.check(
        "finite-depth-feshbach-and-positive-edge-covariance",
        "independent open-depth elimination converges to the Weyl form and its constrained edge covariance is positive semidefinite",
        feshbach_gate,
        f"depth rel={','.join(f'{value:.1e}' for value in differences)}; edge={edge_inertia}; TT={response:.12f}",
    )

    link_reflection = baseline_reflection.copy()
    if mutation == "link_reflection_input":
        link_reflection[0, 0] += 1.0e-2
    link_cross = -link_reflection @ coefficients[4]
    link_kernel = np.block(
        [
            [
                -link_reflection @ coefficients[3],
                link_cross,
            ],
            [
                link_cross.conj().T,
                np.zeros((7, 7)),
            ],
        ]
    )
    link = completion_data(link_kernel, baseline_stable.transfer)
    link_source = np.concatenate((border.rhs, np.zeros(7)))
    link_values, link_vectors = np.linalg.eigh(
        0.5 * (link_kernel + link_kernel.conj().T)
    )
    link_sign = (
        link_vectors * np.where(link_values < -1.0e-10, -1.0, 1.0)
    ) @ link_vectors.conj().T
    link_source_change = float(
        np.linalg.norm(link_sign @ link_source - link_source)
        / np.linalg.norm(link_source)
    )
    link_y = np.linalg.lstsq(link_cross, border.rhs, rcond=1.0e-12)[0]
    link_preimage = np.concatenate((np.zeros(7), link_y))
    link_preimage_residual = float(
        np.linalg.norm(link_kernel @ link_preimage - link_source)
        / np.linalg.norm(link_source)
    )
    link_zero_energy = float(
        abs(np.vdot(link_preimage, link_source))
        / (np.linalg.norm(link_preimage) * np.linalg.norm(link_source))
    )
    link_gate = (
        np.linalg.norm(link_kernel - link_kernel.conj().T) < 1.0e-12
        and link[0] == (4, 4, 6)
        and link[1] == (0, 8, 6)
        and link[2] < 1.0e-12
        and link[3] > 0.8
        and link[4] > 0.8
        and link_source_change > 0.5
        and link_preimage_residual < 1.0e-12
        and link_zero_energy < 1.0e-12
    )
    checks.check(
        "link-reflection-positive-completion-radical-wall",
        "the canonical sign makes the link crossing positive but its fixed radical is not shift invariant and the TT source is changed",
        link_gate,
        f"K/H={link[0]}/{link[1]}; radical leak={link[3]:.3f}; adjoint={link[4]:.3f}; source={link_source_change:.3f}; preimage={link_preimage_residual:.1e}/{link_zero_energy:.1e}",
    )

    site_reflection = baseline_reflection.copy()
    if mutation == "site_reflection_input":
        site_reflection[0, 0] += 1.0e-2
    site_kernel = -site_reflection @ coefficients[4]
    finite_roots = np.asarray([branch.root for branch in laurent.branches])
    site_transfer, mode_condition = finite_mode_transfer(coefficients, finite_roots)
    site = completion_data(site_kernel, site_transfer)
    site_values, site_vectors = np.linalg.eigh(
        0.5 * (site_kernel + site_kernel.conj().T)
    )
    site_sign = (
        site_vectors * np.where(site_values < -1.0e-10, -1.0, 1.0)
    ) @ site_vectors.conj().T
    site_source_change = float(
        np.linalg.norm(site_sign @ border.rhs - border.rhs)
        / np.linalg.norm(border.rhs)
    )
    site_y = np.linalg.lstsq(site_kernel, border.rhs, rcond=1.0e-12)[0]
    site_preimage_residual = float(
        np.linalg.norm(site_kernel @ site_y - border.rhs)
        / np.linalg.norm(border.rhs)
    )
    site_zero_energy = float(
        abs(np.vdot(site_y, border.rhs))
        / (np.linalg.norm(site_y) * np.linalg.norm(border.rhs))
    )
    site_gate = (
        np.linalg.norm(site_kernel - site_kernel.conj().T) < 1.0e-12
        and site[0] == (1, 1, 5)
        and site[1] == (0, 2, 5)
        and site[2] < 1.0e-12
        and site[3] > 0.7
        and site[4] > 1.0
        and site_source_change > 1.0
        and mode_condition < 5.0e3
        and site_preimage_residual < 1.0e-12
        and site_zero_energy < 1.0e-12
    )
    checks.check(
        "site-reflection-positive-completion-radical-wall",
        "the site crossing has the same structural failure: sign positivity leaves a non-invariant radical and changes the TT source",
        site_gate,
        f"K/H={site[0]}/{site[1]}; radical leak={site[3]:.3f}; adjoint={site[4]:.3f}; source={site_source_change:.3f}; preimage={site_preimage_residual:.1e}/{site_zero_energy:.1e}",
    )

    commutant_nullity, commutant_gap = commutant_data(coefficients, mutation)
    one_layer_nullity, one_layer_separation, one_layer_distance = (
        one_layer_commutant_data(coefficients, mutation)
    )
    commutant_gate = (
        commutant_nullity == 1
        and commutant_gap > 1.0e12
        and one_layer_nullity == 2
        and one_layer_separation > 0.7
        and one_layer_distance < 1.0e-12
    )
    checks.check(
        "fixed-local-action-covariant-intertwiner-exhaustion",
        "the constant and nearest-layer coefficient commutants contain only scalar monomials, so local action symmetries reduce to translated site/link planes",
        commutant_gate,
        f"constant={commutant_nullity}; one-layer={one_layer_nullity}; separation={one_layer_separation:.3f}; angle={one_layer_distance:.2e}",
    )

    coupled_roots = np.asarray([branch.root.real for branch in branches])
    coupled_weights = np.asarray([branch.moment_weight.real for branch in branches])
    scalar = scalar_escape(coupled_roots, coupled_weights, mutation)
    scalar_gate = (
        len(branches) == 3
        and scalar[0] == (1, 2, 0)
        and scalar[1] == (0, 3, 0)
        and scalar[2] < 1.0e-12
        and scalar[3] > 4.0e-4
        and scalar[4] > 2.0e-4
        and scalar[5] > 1.0e4
        and scalar[6] > 1.0e4
        and scalar[7] < 1.0e-12
        and scalar[8] < -1.0e-18
        and scalar[9] < -1.0e-28
    )
    checks.check(
        "minimal-tt-canonical-krein-escape-and-source-boundary",
        "the minimal TT modes admit a canonical covariant positive Krein metric, but it changes the source-adjoint response",
        scalar_gate,
        f"H/G={scalar[0]}/{scalar[1]}; source={scalar[3]:.2e}; restrict={scalar[4]:.2e}; filter={scalar[5]:.2e}; covariance={scalar[7]:.2e}; det={scalar[8]:.2e}/{scalar[9]:.2e}",
    )

    note = flat(NOTE_PATH)
    if mutation == "note_boundary":
        note = note.replace("gravity_verdict: open", "gravity_verdict: failed")
    axiom = flat(AXIOM_PATH)
    scope_gate = (
        "weyl_feshbach_verdict: positive_boundary_object" in note
        and "declared_reflection_completion_verdict: bounded_infeasible" in note
        and "minimal_tt_krein_escape: nonterminal" in note
        and "gravity_verdict: open" in note
        and "no axiom is amended" in note
        and all(f"### n{index}" in note for index in range(1, 9))
        and "n1--n8 status: pass" in note
        and "choose a hamiltonian or transfer operator" in axiom
    )
    checks.check(
        "scope-no-go-discipline-and-axiom-boundary",
        "the note lands N1-N8 for the declared reflection family while preserving the Weyl and scalar escapes and leaving gravity open",
        scope_gate,
    )

    print(
        "WEYL_CERTIFICATE: stable dimension=14, endpoint=7, finite-inside=7; "
        f"W Hermitian residual={baseline_stable.hermiticity:.2e}; Feshbach depth32={differences[-1]:.2e}"
    )
    print(
        "BOUNDARY_COVARIANCE: physical edge inertia=0/11/1 and the same unrefitted local TT covector gives boundary response="
        f"{response:.12f}; this is equal-boundary positivity, not an OS transfer theorem"
    )
    print(
        "RADICAL_CERTIFICATE: link/site positive sign completions exist, but their fixed radicals leak under the stable shift by "
        f"{link[3]:.3f}/{site[3]:.3f}"
    )
    print(
        "LOCALITY_CERTIFICATE: constant and one-forward-layer coefficient commutants contain only scalar monomials; fixed or nearest-layer action-covariant completions reduce to site/link translations"
    )
    print(
        "KREIN_ESCAPE: the three-mode TT quotient has a unique similarity-covariant spectral fundamental symmetry and positive metric, but it changes the original source-adjoint response and does not derive a local Record reflection"
    )
    print(
        "N5_CERTIFICATE: the execution resolutions below state exactly what this runner did and did not resolve"
    )
    print(
        "per_element: checked the twenty-two-edge action through its odd six-edge plus one-Ward bordered coefficients and geometric reflection"
    )
    print(
        "per_site: checked one link- and one site-centered reflection cut on the translation-invariant temporal recurrence; no inhomogeneous site family"
    )
    print(
        "per_mode: checked all seven endpoint and seven finite stable descriptor modes at spatial momentum pi over two, plus the three-mode TT minimal quotient"
    )
    print(
        "per_block: checked the 14-dimensional stable graph, infinite Weyl form, four finite-depth Feshbach eliminations, two crossing Grams, and coefficient commutant"
    )
    print(
        "lattice_wide: checked and not executed — no Brillouin-zone, Newtonian-IR, nonlinear-background, refinement, or all-lattice theorem is claimed"
    )
    print(
        "WEYL_FESHBACH_VERDICT: POSITIVE_BOUNDARY_OBJECT; DECLARED_REFLECTION_COMPLETION_VERDICT: BOUNDED_INFEASIBLE; MINIMAL_TT_KREIN_ESCAPE: NONTERMINAL; GRAVITY_VERDICT: OPEN"
    )
    print("TOE_MOVEMENT: obligations=0 percentages=0 axioms_amended=0")
    print(f"elapsed_sec={time.perf_counter() - started:.2f}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
