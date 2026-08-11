#!/usr/bin/env python3
"""Certify a bounded ten-ray coframe/link local-frame Ward fixture.

The ten signed-cubic rays from Block 35 are used as metric probes.  They are
not asked to carry a continuous group action.  Two supplied GL+(4) coframes
and one SO(4) link carry an exact SO(4) x SO(4) local-frame redundancy.  A
finite Record free energy, geometry wells, the link constraint, and its
multiplier are differentiated from one master functional.

The runner keeps connected covariance, microscopic contact, mixed
source/geometry response, multiplier curvature, and generator derivatives
separate.  At the exact nonuniform KKT background the sector generator terms
are nonzero and cancel, while the total stationary generator-connection term
vanishes as it must.  Intrinsic quotient checks prevent ambient KKT
bookkeeping from being misidentified as a physical gravity contact.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import expm
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TEN_RAY_COFRAME_LINK_LOCAL_FRAME_WARD_STATIONARITY_"
    "CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_LOCAL_GEOMETRY_RECORD_BOND_TRANSFER_REFLECTION_RESPONSE_"
    "CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
WARD_PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_SOURCED_REGGE_JOINT_WARD_SCHUR_COMPLETION_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_TEN_RAY_COFRAME_LINK_LOCAL_FRAME_WARD_STATIONARITY_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_LOCAL_GEOMETRY_RECORD_BOND_TRANSFER_REFLECTION_RESPONSE_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_SOURCED_REGGE_JOINT_WARD_SCHUR_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

DIMENSION = 4
COFRAME_COORDINATES = DIMENSION * DIMENSION
GEOMETRY_COORDINATES = 3 * COFRAME_COORDINATES
SOURCE_COORDINATES = 20
MULTIPLIER_COORDINATES = 10
EXTENDED_COORDINATES = GEOMETRY_COORDINATES + MULTIPLIER_COORDINATES
ALPHA = 4.0
REDUCED_STEP = 2.0e-4

HCOMPS = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 3),
    (2, 3),
)

RAYS = np.asarray(
    (
        (1, 1, 1, 0),
        (1, 1, -1, 0),
        (1, -1, 1, 0),
        (1, -1, -1, 0),
        (1, 0, 0, 1),
        (-1, 0, 0, 1),
        (0, 1, 0, 1),
        (0, -1, 0, 1),
        (0, 0, 1, 1),
        (0, 0, -1, 1),
    ),
    dtype=float,
)

RECORD_WEIGHTS = (
    np.asarray((3, 3, 3, 3, 4, 4, 4, 4, 4, 4), dtype=float),
    np.asarray((6, 6, 6, 6, 2, 2, 2, 2, 2, 2), dtype=float),
)

MATRIX_BASIS = tuple(
    np.eye(DIMENSION, dtype=float)[[row]].T
    @ np.eye(DIMENSION, dtype=float)[[column]]
    for row in range(DIMENSION)
    for column in range(DIMENSION)
)


def exact_metric_map() -> sp.Matrix:
    return sp.Matrix(
        [
            [
                int(direction[left])
                * int(direction[right])
                * (1 if left == right else 2)
                for left, right in HCOMPS
            ]
            for direction in RAYS.astype(int)
        ]
    )


EXACT_METRIC_MAP = exact_metric_map()


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


@dataclass
class RecordData:
    value: float
    gradient: np.ndarray
    hessian: np.ndarray
    contact: np.ndarray
    covariance: np.ndarray
    mixed: np.ndarray
    source_gradient: np.ndarray
    source_hessian: np.ndarray
    probabilities: np.ndarray
    score_matrix: np.ndarray


@dataclass
class EffectiveData:
    value: float
    gradient: np.ndarray
    hessian: np.ndarray
    mixed: np.ndarray
    source_hessian: np.ndarray
    records: tuple[RecordData, RecordData]


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def split_geometry(vector: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return (
        vector[:16].reshape(4, 4),
        vector[16:32].reshape(4, 4),
        vector[32:48].reshape(4, 4),
    )


def join_geometry(e0: np.ndarray, e1: np.ndarray, link: np.ndarray) -> np.ndarray:
    return np.concatenate((e0.reshape(-1), e1.reshape(-1), link.reshape(-1)))


def symmetric_to_vector(matrix: np.ndarray) -> np.ndarray:
    return np.asarray([matrix[left, right] for left, right in HCOMPS])


def vector_to_symmetric(vector: np.ndarray) -> np.ndarray:
    matrix = np.zeros((4, 4), dtype=float)
    for value, (left, right) in zip(vector, HCOMPS):
        matrix[left, right] = value
        matrix[right, left] = value
    return matrix


def skew_generators() -> tuple[np.ndarray, ...]:
    generators: list[np.ndarray] = []
    for left, right in combinations(range(4), 2):
        generator = np.zeros((4, 4), dtype=float)
        generator[left, right] = -1.0
        generator[right, left] = 1.0
        generators.append(generator)
    return tuple(generators)


SKEW_GENERATORS = skew_generators()


def branch_contact(direction: np.ndarray) -> np.ndarray:
    projector = np.outer(direction, direction)
    result = np.zeros((16, 16), dtype=float)
    for column, variation in enumerate(MATRIX_BASIS):
        result[:, column] = (variation @ projector).reshape(-1)
    return result


BRANCH_CONTACTS = tuple(branch_contact(direction) for direction in RAYS)


def record_data(
    coframe: np.ndarray,
    weights: np.ndarray,
    sources: np.ndarray | None = None,
) -> RecordData:
    if sources is None:
        sources = np.zeros(10, dtype=float)
    images = (coframe @ RAYS.T).T
    scores = np.einsum("ri,ri->r", images, images)
    activities = weights * np.exp(sources - 0.5 * scores) / 60.0
    partition = 1.0 + float(np.sum(activities))
    probabilities = activities / partition

    branch_gradients = np.asarray(
        [np.outer(image, direction).reshape(-1) for image, direction in zip(images, RAYS)]
    )
    gradient = probabilities @ branch_gradients
    contact = sum(
        probabilities[index] * BRANCH_CONTACTS[index] for index in range(10)
    )
    second_moment = branch_gradients.T @ (
        probabilities[:, None] * branch_gradients
    )
    covariance = second_moment - np.outer(gradient, gradient)
    hessian = contact - covariance

    mixed = np.column_stack(
        [
            probabilities[index] * (branch_gradients[index] - gradient)
            for index in range(10)
        ]
    )
    source_gradient = -probabilities
    source_hessian = -(
        np.diag(probabilities) - np.outer(probabilities, probabilities)
    )
    score_matrix = sum(
        probabilities[index] * np.outer(RAYS[index], RAYS[index])
        for index in range(10)
    )
    return RecordData(
        value=-float(np.log(partition)),
        gradient=gradient,
        hessian=hessian,
        contact=contact,
        covariance=covariance,
        mixed=mixed,
        source_gradient=source_gradient,
        source_hessian=source_hessian,
        probabilities=probabilities,
        score_matrix=score_matrix,
    )


E0_STAR = np.eye(4, dtype=float)
E1_STAR = np.diag((2.0, 2.0, 2.0, 2.5))
U_STAR = np.eye(4, dtype=float)
RECORD0_STAR = record_data(E0_STAR, RECORD_WEIGHTS[0])
RECORD1_STAR = record_data(E1_STAR, RECORD_WEIGHTS[1])
STAR_MISMATCH = E0_STAR - U_STAR @ E1_STAR
STAR_LINK_GRADIENT_E0 = STAR_MISMATCH
STAR_LINK_GRADIENT_E1 = -U_STAR.T @ STAR_MISMATCH
STAR_LINK_GRADIENT_U = -STAR_MISMATCH @ E1_STAR.T
Q0 = (
    E0_STAR.T @ E0_STAR
    + np.linalg.solve(E0_STAR, STAR_LINK_GRADIENT_E0) / ALPHA
    + RECORD0_STAR.score_matrix / ALPHA
)
Q1 = (
    E1_STAR.T @ E1_STAR
    + np.linalg.solve(E1_STAR, STAR_LINK_GRADIENT_E1) / ALPHA
    + RECORD1_STAR.score_matrix / ALPHA
)
MULTIPLIER_STAR = -U_STAR.T @ STAR_LINK_GRADIENT_U


def link_data(
    e0: np.ndarray, e1: np.ndarray, link: np.ndarray
) -> tuple[float, np.ndarray, np.ndarray]:
    mismatch = e0 - link @ e1
    gradient = join_geometry(
        mismatch,
        -link.T @ mismatch,
        -mismatch @ e1.T,
    )
    hessian = np.zeros((48, 48), dtype=float)
    for column in range(48):
        perturbation = np.zeros(48, dtype=float)
        perturbation[column] = 1.0
        de0, de1, dlink = split_geometry(perturbation)
        dmismatch = de0 - dlink @ e1 - link @ de1
        dg0 = dmismatch
        dg1 = -dlink.T @ mismatch - link.T @ dmismatch
        dgu = -dmismatch @ e1.T - mismatch @ de1.T
        hessian[:, column] = join_geometry(dg0, dg1, dgu)
    return 0.5 * float(np.sum(mismatch * mismatch)), gradient, hessian


def well_data(coframe: np.ndarray, target: np.ndarray) -> tuple[float, np.ndarray, np.ndarray]:
    gram_residual = coframe.T @ coframe - target
    gradient = ALPHA * coframe @ gram_residual
    hessian = np.zeros((16, 16), dtype=float)
    for column, variation in enumerate(MATRIX_BASIS):
        dgram = variation.T @ coframe + coframe.T @ variation
        dgradient = ALPHA * (
            variation @ gram_residual + coframe @ dgram
        )
        hessian[:, column] = dgradient.reshape(-1)
    value = (ALPHA / 4.0) * float(np.sum(gram_residual * gram_residual))
    return value, gradient.reshape(-1), hessian


def effective_data(
    e0: np.ndarray,
    e1: np.ndarray,
    link: np.ndarray,
    sources0: np.ndarray | None = None,
    sources1: np.ndarray | None = None,
) -> EffectiveData:
    record0 = record_data(e0, RECORD_WEIGHTS[0], sources0)
    record1 = record_data(e1, RECORD_WEIGHTS[1], sources1)
    link_value, link_gradient, link_hessian = link_data(e0, e1, link)
    well0_value, well0_gradient, well0_hessian = well_data(e0, Q0)
    well1_value, well1_gradient, well1_hessian = well_data(e1, Q1)

    gradient = link_gradient.copy()
    gradient[:16] += well0_gradient + record0.gradient
    gradient[16:32] += well1_gradient + record1.gradient

    hessian = link_hessian.copy()
    hessian[:16, :16] += well0_hessian + record0.hessian
    hessian[16:32, 16:32] += well1_hessian + record1.hessian

    mixed = np.zeros((48, 20), dtype=float)
    mixed[:16, :10] = record0.mixed
    mixed[16:32, 10:] = record1.mixed
    source_hessian = np.zeros((20, 20), dtype=float)
    source_hessian[:10, :10] = record0.source_hessian
    source_hessian[10:, 10:] = record1.source_hessian

    return EffectiveData(
        value=link_value + well0_value + well1_value + record0.value + record1.value,
        gradient=gradient,
        hessian=hessian,
        mixed=mixed,
        source_hessian=source_hessian,
        records=(record0, record1),
    )


def constraint_vector(link: np.ndarray) -> np.ndarray:
    gram_residual = link.T @ link - np.eye(4)
    values = []
    for left, right in HCOMPS:
        values.append(
            0.5 * gram_residual[left, right]
            if left == right
            else gram_residual[left, right]
        )
    return np.asarray(values)


def constraint_jacobian(link: np.ndarray) -> np.ndarray:
    jacobian = np.zeros((10, 48), dtype=float)
    for column, variation in enumerate(MATRIX_BASIS):
        dgram = variation.T @ link + link.T @ variation
        for row, (left, right) in enumerate(HCOMPS):
            jacobian[row, 32 + column] = (
                0.5 * dgram[left, right]
                if left == right
                else dgram[left, right]
            )
    return jacobian


def multiplier_sector(
    link: np.ndarray, multiplier: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    gradient = np.zeros(EXTENDED_COORDINATES, dtype=float)
    gradient[32:48] = (link @ multiplier).reshape(-1)
    gradient[48:] = constraint_vector(link)

    hessian = np.zeros((EXTENDED_COORDINATES, EXTENDED_COORDINATES), dtype=float)
    for column, variation in enumerate(MATRIX_BASIS):
        hessian[32:48, 32 + column] = (variation @ multiplier).reshape(-1)
    jacobian = constraint_jacobian(link)
    hessian[:48, 48:] = jacobian.T
    hessian[48:, :48] = jacobian
    return gradient, hessian


def extended_data(
    effective: EffectiveData, link: np.ndarray, multiplier: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    effective_gradient = np.zeros(EXTENDED_COORDINATES, dtype=float)
    effective_gradient[:48] = effective.gradient
    effective_hessian = np.zeros((EXTENDED_COORDINATES, EXTENDED_COORDINATES), dtype=float)
    effective_hessian[:48, :48] = effective.hessian
    multiplier_gradient, multiplier_hessian = multiplier_sector(link, multiplier)
    return (
        effective_gradient + multiplier_gradient,
        effective_hessian + multiplier_hessian,
        effective_gradient,
        effective_hessian,
    )


def generator(
    site: int,
    tangent: np.ndarray,
    e0: np.ndarray,
    e1: np.ndarray,
    link: np.ndarray,
    multiplier: np.ndarray,
) -> np.ndarray:
    if site == 0:
        geometry = join_geometry(tangent @ e0, np.zeros((4, 4)), tangent @ link)
        multiplier_part = np.zeros(10, dtype=float)
    else:
        geometry = join_geometry(
            np.zeros((4, 4)), tangent @ e1, -link @ tangent
        )
        multiplier_part = symmetric_to_vector(
            tangent @ multiplier - multiplier @ tangent
        )
    return np.concatenate((geometry, multiplier_part))


def generator_connection(
    gradient: np.ndarray,
    site: int,
    tangent: np.ndarray,
) -> np.ndarray:
    ge0, ge1, gu = split_geometry(gradient[:48])
    connection = np.zeros(EXTENDED_COORDINATES, dtype=float)
    if site == 0:
        connection[:16] = (tangent.T @ ge0).reshape(-1)
        connection[32:48] = (tangent.T @ gu).reshape(-1)
    else:
        connection[16:32] = (tangent.T @ ge1).reshape(-1)
        connection[32:48] = (-gu @ tangent.T).reshape(-1)
        # The multiplier-gradient contribution vanishes on the constraint
        # surface used below.  Keeping this assertion explicit prevents a
        # silent off-surface use of this reduced adjoint formula.
        if np.linalg.norm(gradient[48:]) > 1.0e-13:
            raise ValueError("site-1 multiplier connection requested off constraint")
    return connection


def full_value(
    e0: np.ndarray,
    e1: np.ndarray,
    link: np.ndarray,
    multiplier: np.ndarray | None = None,
) -> float:
    value = effective_data(e0, e1, link).value
    if multiplier is not None:
        value += 0.5 * float(
            np.trace(multiplier @ (link.T @ link - np.eye(4)))
        )
    return value


def central_hessian(function, dimension: int, step: float) -> np.ndarray:
    origin = np.zeros(dimension, dtype=float)
    baseline = float(function(origin))
    hessian = np.zeros((dimension, dimension), dtype=float)
    unit = np.eye(dimension) * step
    for left in range(dimension):
        hessian[left, left] = (
            float(function(unit[left]))
            - 2.0 * baseline
            + float(function(-unit[left]))
        ) / (step * step)
        for right in range(left + 1, dimension):
            value = (
                float(function(unit[left] + unit[right]))
                - float(function(unit[left] - unit[right]))
                - float(function(-unit[left] + unit[right]))
                + float(function(-unit[left] - unit[right]))
            ) / (4.0 * step * step)
            hessian[left, right] = value
            hessian[right, left] = value
    return hessian


def reduced_value(coordinates: np.ndarray) -> float:
    e0 = E0_STAR + vector_to_symmetric(coordinates[:10])
    e1 = E1_STAR + vector_to_symmetric(coordinates[10:20])
    algebra = sum(
        coordinates[20 + index] * generator
        for index, generator in enumerate(SKEW_GENERATORS)
    )
    link = expm(algebra)
    return full_value(e0, e1, link)


def redundant_value(coordinates: np.ndarray) -> float:
    e0 = E0_STAR + coordinates[:16].reshape(4, 4)
    e1 = E1_STAR + coordinates[16:32].reshape(4, 4)
    algebra = sum(
        coordinates[32 + index] * generator
        for index, generator in enumerate(SKEW_GENERATORS)
    )
    return full_value(e0, e1, expm(algebra))


def finite_frame_invariance() -> tuple[float, float]:
    tangent0 = SKEW_GENERATORS[0] + 0.37 * SKEW_GENERATORS[4]
    tangent1 = -0.41 * SKEW_GENERATORS[2] + 0.23 * SKEW_GENERATORS[5]
    rotation0 = expm(0.31 * tangent0)
    rotation1 = expm(-0.27 * tangent1)
    e0 = np.diag((1.1, 0.9, 1.2, 0.8)) + 0.03 * np.ones((4, 4))
    e1 = np.diag((1.7, 1.4, 1.9, 1.3)) - 0.02 * np.ones((4, 4))
    link = np.eye(4) + 0.07 * np.arange(16, dtype=float).reshape(4, 4) / 16.0
    multiplier = np.diag((-1.2, -0.8, -1.4, -1.0))
    before_effective = full_value(e0, e1, link)
    before_full = full_value(e0, e1, link, multiplier)
    transformed_effective = full_value(
        rotation0 @ e0,
        rotation1 @ e1,
        rotation0 @ link @ rotation1.T,
    )
    transformed_full = full_value(
        rotation0 @ e0,
        rotation1 @ e1,
        rotation0 @ link @ rotation1.T,
        rotation1 @ multiplier @ rotation1.T,
    )
    return (
        abs(transformed_effective - before_effective),
        abs(transformed_full - before_full),
    )


def transported_ray_bond(
    e0: np.ndarray, e1: np.ndarray, link: np.ndarray
) -> np.ndarray:
    left_images = (e0 @ RAYS.T).T
    right_images = (link @ e1 @ RAYS.T).T
    differences = left_images[:, None, :] - right_images[None, :, :]
    return np.exp(-0.07 * np.einsum("rsi,rsi->rs", differences, differences))


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    parent = flat(PARENT_PATH)
    ward_parent = flat(WARD_PARENT_PATH)

    checks.check(
        "premise-and-scope-binding",
        "the runner binds the current four-axiom surface and both local-law/Ward parents without importing a coframe, link, action, or audit verdict",
        all(path.exists() for path in (AXIOM_PATH, PARENT_PATH, WARD_PARENT_PATH, PREMISE_REGISTRY_PATH))
        and "lattice / physical locality" in axiom
        and "admissibility / local constraint" in axiom
        and "the result is the exact chain rule, not yet a ward identity" in parent
        and "h_{ba} r^a" in ward_parent
        and "audit-status authority" in note,
    )

    determinant = EXACT_METRIC_MAP.det()
    rotation45 = np.asarray(
        (
            (2.0**-0.5, -2.0**-0.5, 0.0, 0.0),
            (2.0**-0.5, 2.0**-0.5, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
        )
    )
    rotated = rotation45 @ RAYS[0]
    ray_match = max(
        abs(float(np.dot(rotated, direction)))
        / (float(np.linalg.norm(rotated)) * float(np.linalg.norm(direction)))
        for direction in RAYS
    )
    checks.check(
        "ten-ray-basis-not-continuous-label-orbit",
        "the ten rays are an exact Sym(4) metric basis, while a connected 45-degree frame rotation leaves their finite label set",
        determinant == -24576 and ray_match < 1.0 - 1.0e-6,
        f"det={determinant}; best ray overlap={ray_match:.9f}",
    )

    rotated_metric_map = np.asarray(
        [
            [
                direction[left]
                * direction[right]
                * (1.0 if left == right else 2.0)
                for left, right in HCOMPS
            ]
            for direction in (rotation45 @ RAYS.T).T
        ]
    )
    score_lift = rotated_metric_map @ np.linalg.inv(
        np.asarray(EXACT_METRIC_MAP, dtype=float)
    )
    score_lift_error = float(
        np.max(
            np.abs(
                score_lift @ np.asarray(EXACT_METRIC_MAP, dtype=float)
                - rotated_metric_map
            )
        )
    )
    negative_lift_entries = int(np.count_nonzero(score_lift < -1.0e-12))
    checks.check(
        "continuous-score-lift-not-positive-label-mixing",
        "the rank-ten score basis carries the induced continuous Sym(4) action, but its 45-degree matrix has negative entries and is not a stochastic microscopic-label law",
        score_lift_error < 2.0e-15 and negative_lift_entries == 32,
        f"intertwiner error={score_lift_error:.3e}; negative entries={negative_lift_entries}; minimum={np.min(score_lift):.6f}",
    )

    simplex_tangent_constraints = np.zeros((100, 100), dtype=float)
    constraint_row = 0
    for row in range(10):
        for column in range(10):
            if row != column:
                simplex_tangent_constraints[constraint_row, 10 * row + column] = 1.0
                constraint_row += 1
    for row in range(10):
        simplex_tangent_constraints[constraint_row, 10 * row : 10 * (row + 1)] = 1.0
        constraint_row += 1
    simplex_tangent_rank = int(np.linalg.matrix_rank(simplex_tangent_constraints))
    checks.check(
        "continuous-simplex-automorphism-tangent-is-trivial",
        "positivity of a stochastic one-parameter map and its inverse kills every off-diagonal generator entry, while normalization kills the diagonal",
        constraint_row == 100 and simplex_tangent_rank == 100,
        f"constraint rank={simplex_tangent_rank}; tangent dimension={100-simplex_tangent_rank}",
    )

    escape_rotation0 = expm(0.29 * SKEW_GENERATORS[1])
    escape_rotation1 = expm(-0.37 * SKEW_GENERATORS[4])
    escape_e0 = np.diag((1.0, 1.1, 0.9, 1.2))
    escape_e1 = np.diag((1.6, 1.4, 1.8, 1.3))
    escape_link = expm(0.23 * SKEW_GENERATORS[2])
    base_ray_bond = transported_ray_bond(escape_e0, escape_e1, escape_link)
    transformed_ray_bond = transported_ray_bond(
        escape_rotation0 @ escape_e0,
        escape_rotation1 @ escape_e1,
        escape_rotation0 @ escape_link @ escape_rotation1.T,
    )
    ray_bond_error = float(np.max(np.abs(base_ray_bond - transformed_ray_bond)))
    uncompensated_ray_bond = transported_ray_bond(
        escape_rotation0 @ escape_e0, escape_e1, escape_link
    )
    uncompensated_change = float(
        np.max(np.abs(base_ray_bond - uncompensated_ray_bond))
    )
    checks.check(
        "ray-resolved-transport-escape",
        "a positive ray-resolved bond can be exactly frame invariant once coframes and a transforming link are added, so the finite-label boundary is not a gravity no-go",
        ray_bond_error < 2.0e-15 and uncompensated_change > 0.05,
        f"covariance error={ray_bond_error:.3e}; fixed-link mutation={uncompensated_change:.6f}",
    )

    effective = effective_data(E0_STAR, E1_STAR, U_STAR)
    multiplier = MULTIPLIER_STAR
    total_gradient, total_hessian, effective_gradient, effective_hessian = extended_data(
        effective, U_STAR, multiplier
    )
    multiplier_gradient, multiplier_hessian = multiplier_sector(U_STAR, multiplier)
    stationarity_error = float(np.max(np.abs(total_gradient)))
    constraint_error = float(np.max(np.abs(constraint_vector(U_STAR))))
    metric_difference = float(
        np.linalg.norm(E1_STAR.T @ E1_STAR - E0_STAR.T @ E0_STAR)
    )
    checks.check(
        "exact-nonuniform-kkt-background",
        "the supplied wells and link-orthogonality multiplier give an exact stationary representative whose metric nonuniformity is gauge invariant",
        stationarity_error < 5.0e-14
        and constraint_error < 1.0e-14
        and metric_difference > 7.0
        and abs(float(np.trace(E1_STAR.T @ E1_STAR)) - 18.25) < 1.0e-14
        and abs(float(np.linalg.det(E1_STAR.T @ E1_STAR)) - 400.0) < 1.0e-12,
        f"stationarity={stationarity_error:.3e}; constraint={constraint_error:.3e}; ||g1-g0||={metric_difference:.6f}",
    )

    finite_effective_error, finite_full_error = finite_frame_invariance()
    first_ward_error = 0.0
    for site in (0, 1):
        for tangent in SKEW_GENERATORS:
            frame_generator = generator(
                site, tangent, E0_STAR, E1_STAR, U_STAR, multiplier
            )
            first_ward_error = max(
                first_ward_error,
                abs(float(np.dot(effective_gradient, frame_generator))),
                abs(float(np.dot(multiplier_gradient, frame_generator))),
            )
    checks.check(
        "exact-sitewise-local-frame-invariance",
        "independent endpoint rotations leave the off-shell effective and multiplier sectors invariant and satisfy both infinitesimal first Ward identities",
        finite_effective_error < 2.0e-13
        and finite_full_error < 2.0e-13
        and first_ward_error < 2.0e-13,
        f"finite effective/full={finite_effective_error:.3e}/{finite_full_error:.3e}; first Ward={first_ward_error:.3e}",
    )

    record0 = effective.records[0]
    probe_index = 0
    local_contact = float(record0.contact[probe_index, probe_index])
    local_covariance = float(record0.covariance[probe_index, probe_index])
    local_hessian = float(record0.hessian[probe_index, probe_index])
    checks.check(
        "record-connected-contact-decomposition",
        "one Record free energy independently assembles a nonzero microscopic q-contact minus connected covariance, with neither term optional",
        local_contact > 0.05
        and local_covariance > 0.05
        and abs(local_hessian - (local_contact - local_covariance)) < 1.0e-14
        and local_hessian > 0.0
        and -local_covariance < 0.0,
        f"contact={local_contact:.12f}; covariance={local_covariance:.12f}; complete={local_hessian:.12f}",
    )

    mixed_rank = int(np.linalg.matrix_rank(effective.mixed, tol=1.0e-10))
    mixed_singular = np.linalg.svd(effective.mixed, compute_uv=False)
    mixed_ward_error = 0.0
    for site in (0, 1):
        for tangent in SKEW_GENERATORS:
            frame_generator = generator(
                site, tangent, E0_STAR, E1_STAR, U_STAR, multiplier
            )[:48]
            mixed_ward_error = max(
                mixed_ward_error,
                float(np.linalg.norm(effective.mixed.T @ frame_generator)),
            )
    checks.check(
        "ten-source-mixed-geometry-block",
        "the same two Record sums give a rank-twenty source/coframe Hessian whose twenty scalar-source rows annihilate every local-frame gauge tangent",
        mixed_rank == 20
        and float(mixed_singular[-1]) > 5.0e-4
        and mixed_ward_error < 2.0e-15,
        f"rank={mixed_rank}; minimum singular={mixed_singular[-1]:.9f}; Ward={mixed_ward_error:.3e}",
    )

    derivative_step = 1.0e-5
    star_geometry = join_geometry(E0_STAR, E1_STAR, U_STAR)
    numerical_hessian = np.zeros((48, 48), dtype=float)
    for column in range(48):
        displacement = np.zeros(48, dtype=float)
        displacement[column] = derivative_step
        plus = split_geometry(star_geometry + displacement)
        minus = split_geometry(star_geometry - displacement)
        numerical_hessian[:, column] = (
            effective_data(*plus).gradient - effective_data(*minus).gradient
        ) / (2.0 * derivative_step)
    numerical_mixed = np.zeros((48, 20), dtype=float)
    for column in range(20):
        plus0 = np.zeros(10, dtype=float)
        minus0 = np.zeros(10, dtype=float)
        plus1 = np.zeros(10, dtype=float)
        minus1 = np.zeros(10, dtype=float)
        if column < 10:
            plus0[column] = derivative_step
            minus0[column] = -derivative_step
        else:
            plus1[column - 10] = derivative_step
            minus1[column - 10] = -derivative_step
        numerical_mixed[:, column] = (
            effective_data(E0_STAR, E1_STAR, U_STAR, plus0, plus1).gradient
            - effective_data(E0_STAR, E1_STAR, U_STAR, minus0, minus1).gradient
        ) / (2.0 * derivative_step)
    hessian_difference = float(np.linalg.norm(numerical_hessian - effective.hessian, 2))
    mixed_difference = float(np.linalg.norm(numerical_mixed - effective.mixed, 2))
    checks.check(
        "independent-effective-hessian-differences",
        "centered differences of the complete effective gradient reproduce the separately assembled geometry and mixed-source Hessian blocks",
        hessian_difference < 2.0e-8 and mixed_difference < 2.0e-10,
        f"geometry={hessian_difference:.3e}; mixed={mixed_difference:.3e}",
    )

    effective_ward_error = 0.0
    multiplier_ward_error = 0.0
    total_ward_error = 0.0
    connection_norms: list[float] = []
    for site in (0, 1):
        for tangent in SKEW_GENERATORS:
            frame_generator = generator(
                site, tangent, E0_STAR, E1_STAR, U_STAR, multiplier
            )
            effective_connection = generator_connection(
                effective_gradient, site, tangent
            )
            multiplier_connection = generator_connection(
                multiplier_gradient, site, tangent
            )
            effective_ward_error = max(
                effective_ward_error,
                float(
                    np.linalg.norm(
                        effective_hessian @ frame_generator + effective_connection
                    )
                ),
            )
            multiplier_ward_error = max(
                multiplier_ward_error,
                float(
                    np.linalg.norm(
                        multiplier_hessian @ frame_generator
                        + multiplier_connection
                    )
                ),
            )
            total_ward_error = max(
                total_ward_error,
                float(np.linalg.norm(total_hessian @ frame_generator)),
            )
            connection_norms.append(float(np.linalg.norm(effective_connection)))
    checks.check(
        "differentiated-sector-and-kkt-ward-identities",
        "effective and multiplier sectors each need their generator derivative, while their nonzero connections cancel in the fully stationary KKT identity",
        effective_ward_error < 2.0e-12
        and multiplier_ward_error < 2.0e-12
        and total_ward_error < 2.0e-12
        and min(connection_norms) > 2.0,
        f"sector errors={effective_ward_error:.3e}/{multiplier_ward_error:.3e}; total={total_ward_error:.3e}; min connection={min(connection_norms):.6f}",
    )

    no_record_covariance = effective_hessian.copy()
    no_record_covariance[:16, :16] += effective.records[0].covariance
    no_record_covariance[16:32, 16:32] += effective.records[1].covariance
    no_record_contact = effective_hessian.copy()
    no_record_contact[:16, :16] -= effective.records[0].contact
    no_record_contact[16:32, 16:32] -= effective.records[1].contact
    no_covariance_ward_error = 0.0
    no_contact_ward_error = [0.0, 0.0]
    for site in (0, 1):
        for tangent in SKEW_GENERATORS:
            frame_generator = generator(
                site, tangent, E0_STAR, E1_STAR, U_STAR, multiplier
            )
            effective_connection = generator_connection(
                effective_gradient, site, tangent
            )
            no_covariance_ward_error = max(
                no_covariance_ward_error,
                float(
                    np.linalg.norm(
                        no_record_covariance @ frame_generator
                        + effective_connection
                    )
                ),
            )
            no_contact_ward_error[site] = max(
                no_contact_ward_error[site],
                float(
                    np.linalg.norm(
                        no_record_contact @ frame_generator
                        + effective_connection
                    )
                ),
            )
    checks.check(
        "record-ward-role-classification",
        "Record covariance and mixed sources are transverse to every gauge tangent, whereas the microscopic contact is the Record term load-bearing in the differentiated frame identity",
        no_covariance_ward_error < 2.0e-12
        and mixed_ward_error < 2.0e-15
        and no_contact_ward_error[0] > 0.1
        and no_contact_ward_error[1] > 0.003,
        f"drop covariance={no_covariance_ward_error:.3e}; drop contact endpoints={no_contact_ward_error[0]:.6f}/{no_contact_ward_error[1]:.6f}",
    )

    transforming_tangent = SKEW_GENERATORS[2]
    transforming_generator = generator(
        1,
        transforming_tangent,
        E0_STAR,
        E1_STAR,
        U_STAR,
        multiplier,
    )
    transforming_connection = generator_connection(
        multiplier_gradient, 1, transforming_tangent
    )
    no_mixed_multiplier = multiplier_hessian.copy()
    no_mixed_multiplier[:48, 48:] = 0.0
    no_mixed_multiplier[48:, :48] = 0.0
    no_constraint_curvature = multiplier_hessian.copy()
    no_constraint_curvature[32:48, 32:48] = 0.0
    missing_mixed_error = float(
        np.linalg.norm(
            no_mixed_multiplier @ transforming_generator
            + transforming_connection
        )
    )
    missing_curvature_error = float(
        np.linalg.norm(
            no_constraint_curvature @ transforming_generator
            + transforming_connection
        )
    )
    checks.check(
        "transforming-multiplier-blocks",
        "an anisotropic stationary multiplier transforms nontrivially at the second endpoint, making both constraint curvature and mixed multiplier blocks load-bearing",
        abs(np.linalg.norm(transforming_generator[48:]) - 7.0 / 4.0) < 2.0e-13
        and abs(missing_mixed_error - 7.0 * 2.0**0.5 / 4.0) < 2.0e-13
        and abs(missing_curvature_error - 4.25) < 2.0e-13,
        f"multiplier generator={np.linalg.norm(transforming_generator[48:]):.6f}; drop mixed/curvature={missing_mixed_error:.6f}/{missing_curvature_error:.6f}",
    )

    tangent = SKEW_GENERATORS[0]
    named_generator = generator(0, tangent, E0_STAR, E1_STAR, U_STAR, multiplier)
    named_connection = generator_connection(effective_gradient, 0, tangent)
    named_raw = float(named_generator @ effective_hessian @ named_generator)
    named_curve = float(
        np.sum(effective.gradient[32:48].reshape(4, 4) * (tangent @ tangent))
    )
    multiplier_raw = float(named_generator @ multiplier_hessian @ named_generator)
    multiplier_curve = float(
        np.sum(multiplier_gradient[32:48].reshape(4, 4) * (tangent @ tangent))
    )
    checks.check(
        "intrinsic-gauge-orbit-curvature",
        "raw ambient curvature is canceled by the exponential-chart second fundamental form in each sector and vanishes intrinsically on the gauge orbit",
        abs(named_raw - 4.0) < 2.0e-12
        and abs(named_curve + 4.0) < 2.0e-12
        and abs(named_raw + named_curve) < 2.0e-12
        and abs(multiplier_raw + multiplier_curve) < 2.0e-12,
        f"effective raw/chart={named_raw:.6f}/{named_curve:.6f}; multiplier raw/chart={multiplier_raw:.6f}/{multiplier_curve:.6f}",
    )

    reduced_hessian = central_hessian(reduced_value, 26, REDUCED_STEP)
    reduced_eigenvalues = np.linalg.eigvalsh(reduced_hessian)
    redundant_hessian = central_hessian(redundant_value, 38, REDUCED_STEP)
    redundant_eigenvalues = np.linalg.eigvalsh(redundant_hessian)
    gauge_zero_count = int(np.count_nonzero(np.abs(redundant_eigenvalues) < 2.0e-6))
    next_redundant = float(redundant_eigenvalues[gauge_zero_count])
    checks.check(
        "gauge-fixed-and-redundant-hessian-control",
        "the supplied Euclidean witness is positive on its polar/exponential gauge slice and the redundant chart exposes exactly twelve local-frame null directions",
        float(np.min(reduced_eigenvalues)) > 3.5
        and gauge_zero_count == 12
        and next_redundant > 5.5,
        f"reduced minimum={np.min(reduced_eigenvalues):.9f}; gauge zeros={gauge_zero_count}; next={next_redundant:.9f}",
    )

    angle = np.pi / 4.0
    rotated_e0 = expm(angle * tangent) @ E0_STAR
    held_link_delta = full_value(rotated_e0, E1_STAR, U_STAR) - full_value(
        E0_STAR, E1_STAR, U_STAR
    )
    omitted_connection = float(np.linalg.norm(effective_hessian @ named_generator))
    no_multiplier_stationarity = float(np.linalg.norm(effective.gradient[32:48]))
    checks.check(
        "load-bearing-term-mutations",
        "holding the link fixed, dropping the generator derivative, dropping the multiplier, or dropping the microscopic contact each breaks a different certified statement",
        abs(held_link_delta - 4.0 * (1.0 - 2.0**-0.5)) < 2.0e-12
        and abs(omitted_connection - 2.0 * 2.0**0.5) < 2.0e-12
        and abs(no_multiplier_stationarity - 417.0**0.5 / 4.0) < 2.0e-12
        and abs(local_contact) > 0.05
        and local_hessian * (-local_covariance) < 0.0,
        f"fixed-link delta={held_link_delta:.12f}; omitted connection={omitted_connection:.6f}; no-multiplier residual={no_multiplier_stationarity:.6f}",
    )

    extension_coefficient = 3.0
    shifted_gradient = effective_gradient.copy()
    shifted_gradient[32:48] += (2.0 * extension_coefficient * U_STAR).reshape(-1)
    shifted_multiplier = multiplier - 2.0 * extension_coefficient * np.eye(4)
    shifted_total, _, _, _ = extended_data(effective, U_STAR, shifted_multiplier)
    shifted_total[32:48] += (2.0 * extension_coefficient * U_STAR).reshape(-1)
    shifted_connection = generator_connection(shifted_gradient, 0, tangent)
    intrinsic_extension = extension_coefficient * float(
        np.trace(U_STAR.T @ U_STAR - np.eye(4))
    )
    checks.check(
        "ambient-extension-ambiguity",
        "an invariant constraint multiple vanishes intrinsically yet tunes the ambient sector connection and is absorbed by an opposite multiplier shift",
        abs(intrinsic_extension) < 1.0e-15
        and float(np.max(np.abs(shifted_total))) < 5.0e-14
        and abs(float(np.linalg.norm(shifted_connection)) - 8.0 * 2.0**0.5) < 2.0e-12,
        f"intrinsic shift={intrinsic_extension:.3e}; shifted KKT={np.max(np.abs(shifted_total)):.3e}; connection norm={np.linalg.norm(shifted_connection):.6f}",
    )

    pure_rotation = expm(0.37 * tangent)
    pure_gauge_e1 = pure_rotation @ E0_STAR
    pure_gauge_link = pure_rotation.T
    pure_metric_difference = float(
        np.linalg.norm(pure_gauge_e1.T @ pure_gauge_e1 - E0_STAR.T @ E0_STAR)
    )
    checks.check(
        "nonuniformity-not-pure-gauge",
        "metric invariants distinguish the anisotropic witness from a coordinate-nonuniform pure-gauge coframe/link control",
        pure_metric_difference < 2.0e-15 and metric_difference > 5.0,
        f"pure-gauge metric difference={pure_metric_difference:.3e}; witness={metric_difference:.6f}",
    )

    checks.check(
        "stationarity-target-correction-and-scope",
        "the note replaces the inconsistent nonzero-total-connection target by sector cancellation and keeps coframe/link selection, curvature, phase, diffeomorphism, Einstein, and Lorentzian content open",
        "total generator-connection term is zero" in note
        and "sector-resolved" in note
        and "metric probes" in note
        and "not a lattice-diffeomorphism" in note
        and "no fifth ontology axiom" in note,
    )

    print("N5_CERTIFICATE: all ten Record rays, twenty sources, two coframes, one link, and twelve local-frame generators were executed")
    print("N5_CERTIFICATE: covariance, microscopic contact, mixed source, multiplier, generator, and intrinsic-chart terms were assembled separately")
    print("per_element: checked one null plus ten actual-ray Record terms and exact rank-ten metric spanning")
    print("per_site: checked both endpoints and all six SO(4) generators at each endpoint")
    print("per_mode: checked twenty source directions, twelve gauge tangents, and twenty-six gauge-fixed directions")
    print("per_block: checked one supplied two-vertex/one-link Euclidean KKT functional and its off-shell frame orbit")
    print("lattice_wide: checked and not executed — no plaquette, six-incidence star, full-Z3 phase, diffeomorphism, or Lorentzian dynamics is certified")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
