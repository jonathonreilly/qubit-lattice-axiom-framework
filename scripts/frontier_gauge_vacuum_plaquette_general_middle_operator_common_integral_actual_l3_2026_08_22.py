#!/usr/bin/env python3
"""Cross-fitted common-integral estimator for the two-slice middle operator.

For a marked spatial face let

    m(W) = exp[(beta/6) Re Tr W]

be its spatial half-weight.  If ``C`` is the normalized full two-slice
character matrix and ``Q`` is the same Wilson integral with only the two
marked boundary half-weights removed, then on the complete character space

    C = s M Q M,

where ``M`` is multiplication by ``m`` and the scalar ``s`` is removed by
normalizing the trivial entry.  The important estimator is forward and
positive-measure based:

    Q_ab proportional to E_full[
        exp(-(beta/6)(Re Tr W_0 + Re Tr W_1))
        conj(chi_a(W_1)) chi_b(W_0)
    ].

It does not invert ``M`` and it does not import the rejected static-rho
identification.  Four training chains estimate ``Q``; four disjoint validation
chains estimate ``C``.  The swapped assignment is a role-reversal diagnostic,
not an independent replication.  Auxiliary B_1,...,B_5 forward models expose
character-cutoff drift before the shared B_1 prediction is assessed.

This runner is deliberately diagnostic-only.  Its burned-seed pilot exercises
the common-integral estimator and exact polynomial controls, but never emits a
physics certificate.  An independent power audit found that the former fresh
``2400``-measurement protocol could not decide the diagonal submodel, so that
protocol is disabled rather than spending fresh seeds on an inconclusive run.
"""

from __future__ import annotations

import argparse
import functools
import math
import time
from dataclasses import dataclass

import numpy as np

import frontier_gauge_vacuum_plaquette_full_two_slice_compression_actual_l3_2026_08_22 as base


AUDIT_TIMEOUT_SEC = 1200
AUDIT_INPUT_PATHS = (
    "scripts/frontier_gauge_vacuum_plaquette_full_two_slice_compression_actual_l3_2026_08_22.py",
    "scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_actual_l3.py",
    "scripts/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.py",
)

AUXILIARY_NMAX = 5
TARGET_NMAX = 1
CHAINS_PER_ROLE = 4
TRAIN_SEEDS = (97213, 97231, 97241, 97259)
VALIDATION_SEEDS = (98207, 98213, 98221, 98251)
PILOT_TRAIN_SEEDS = (94201, 94219, 94229, 94253)
PILOT_VALIDATION_SEEDS = (95203, 95213, 95231, 95233)
DEFORMATION_PARAMETERS = (-9.0 / 10.0, 9.0 / 5.0)
BOOTSTRAP_REPLICATES = 4096
PILOT_BOOTSTRAP_REPLICATES = 8
BOOTSTRAP_SEED = 99223
GENERAL_COMPATIBILITY_FLOOR = 1.0e-2
SYMMETRY_COMPATIBILITY_FLOOR = 1.0e-3
DIAGONAL_REJECTION_CEILING = 1.0e-3
MAX_AUXILIARY_SHIFT_SE = 1.0
MAX_CHAIN_DEVIATION_SE = 5.0
MAX_DENOMINATOR_RELATIVE_SE = 0.10

Weight = tuple[int, int]


@dataclass(frozen=True)
class Config:
    pilot: bool
    therm: int
    measure: int
    sample_every: int
    blocks_per_chain: int


@dataclass
class CommonIntegralChain:
    seed: int
    initial: str
    acceptance: float
    epsilon: float
    full_samples: np.ndarray
    middle_samples: np.ndarray
    deformed_samples: np.ndarray
    spatial_plaquettes: np.ndarray
    mixed_plaquettes: np.ndarray
    inverse_pair_weights: np.ndarray


@dataclass(frozen=True)
class PredictiveAnalysis:
    measured: np.ndarray
    middle: np.ndarray
    modeled: np.ndarray
    residual: np.ndarray
    covariance: np.ndarray
    coordinate_covariance: np.ndarray
    metric: base.CovarianceMetric
    validation_leave: np.ndarray
    training_leave: np.ndarray


@dataclass(frozen=True)
class JointAnalysis:
    residual_vector: np.ndarray
    covariance: np.ndarray
    metric: base.CovarianceMetric
    validation_leave_vectors: np.ndarray
    training_leave_vectors: np.ndarray


@dataclass(frozen=True)
class SymmetryJointAnalysis:
    residual_vector: np.ndarray
    covariance: np.ndarray
    metric: base.CovarianceMetric


@dataclass(frozen=True)
class PolynomialNullAnalysis:
    residual_vector: np.ndarray
    covariance: np.ndarray
    metric: base.CovarianceMetric
    block_vectors: np.ndarray


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pilot",
        action="store_true",
        help="retained for command compatibility; this runner is always non-certifying",
    )
    parser.add_argument("--therm", type=int)
    parser.add_argument("--measure", type=int)
    parser.add_argument("--sample-every", type=int)
    parser.add_argument("--blocks-per-chain", type=int)
    return parser.parse_args()


def resolve_config(args: argparse.Namespace) -> Config:
    defaults = (40, 128, 4, 4)
    therm = defaults[0] if args.therm is None else args.therm
    measure = defaults[1] if args.measure is None else args.measure
    sample_every = defaults[2] if args.sample_every is None else args.sample_every
    blocks = defaults[3] if args.blocks_per_chain is None else args.blocks_per_chain
    if min(therm, measure, sample_every, blocks) <= 0:
        raise ValueError("all sweep, cadence, and blocking arguments must be positive")
    if measure % sample_every:
        raise ValueError("measurement sweeps must be divisible by sample cadence")
    if (measure // sample_every) % blocks:
        raise ValueError("samples must divide evenly into equal blocks")
    if measure // sample_every < 2 * blocks:
        raise ValueError("each chain needs at least two samples per block")
    return Config(
        pilot=True,
        therm=int(therm),
        measure=int(measure),
        sample_every=int(sample_every),
        blocks_per_chain=int(blocks),
    )


def conjugation_permutation(weights: tuple[Weight, ...]) -> np.ndarray:
    index = {weight: i for i, weight in enumerate(weights)}
    return np.array([index[(q, p)] for p, q in weights], dtype=int)


def project_physical(matrix: np.ndarray, weights: tuple[Weight, ...]) -> np.ndarray:
    """Project onto the exact real, symmetric, irrep-swap-commuting surface."""
    symmetric = 0.5 * (matrix.real + matrix.real.T)
    permutation = conjugation_permutation(weights)
    swapped = symmetric[np.ix_(permutation, permutation)]
    return np.asarray(0.5 * (symmetric + swapped), dtype=complex)


def normalized_physical(matrix: np.ndarray, weights: tuple[Weight, ...]) -> np.ndarray:
    return base.normalize_matrix(project_physical(matrix, weights))


@functools.lru_cache(maxsize=None)
def physical_coordinate_basis(weights: tuple[Weight, ...]) -> np.ndarray:
    """Orthonormal real basis after exact symmetries and C_00 normalization."""
    size = len(weights)
    candidates: list[np.ndarray] = []
    for component in (1.0, 1.0j):
        for flat in range(size * size):
            matrix = np.zeros((size, size), dtype=complex)
            matrix.ravel()[flat] = component
            projected = project_physical(matrix, weights)
            projected[0, 0] = 0.0
            candidates.append(base.matrix_vector(projected))
    _, singular_values, right = np.linalg.svd(np.array(candidates), full_matrices=False)
    tolerance = max(singular_values[0] * 1.0e-12, 1.0e-14)
    rank = int(np.count_nonzero(singular_values > tolerance))
    return right[:rank]


def physical_vector(matrix: np.ndarray, basis: np.ndarray) -> np.ndarray:
    residual = np.array(matrix, copy=True)
    residual[0, 0] = 0.0
    return basis @ base.matrix_vector(residual)


@functools.lru_cache(maxsize=None)
def physical_unnormalized_basis(weights: tuple[Weight, ...]) -> np.ndarray:
    """Orthonormal real basis of the unnormalized exact physical surface."""
    size = len(weights)
    candidates: list[np.ndarray] = []
    for component in (1.0, 1.0j):
        for flat in range(size * size):
            matrix = np.zeros((size, size), dtype=complex)
            matrix.ravel()[flat] = component
            candidates.append(base.matrix_vector(project_physical(matrix, weights)))
    _, singular_values, right = np.linalg.svd(np.array(candidates), full_matrices=False)
    tolerance = max(singular_values[0] * 1.0e-12, 1.0e-14)
    rank = int(np.count_nonzero(singular_values > tolerance))
    return right[:rank]


def physical_unnormalized_vector(
    matrix: np.ndarray, basis: np.ndarray, weights: tuple[Weight, ...]
) -> np.ndarray:
    return basis @ base.matrix_vector(project_physical(matrix, weights))


def project_antiunitary(matrix: np.ndarray, weights: tuple[Weight, ...]) -> np.ndarray:
    """Project onto the pointwise S conjugate(A) S = A character identity."""
    permutation = conjugation_permutation(weights)
    transformed = matrix[np.ix_(permutation, permutation)].conj()
    return 0.5 * (matrix + transformed)


@functools.lru_cache(maxsize=None)
def symmetry_complement_basis(weights: tuple[Weight, ...]) -> np.ndarray:
    """Orthonormal complement to the physical surface after pointwise symmetry."""
    size = len(weights)
    candidates: list[np.ndarray] = []
    for component in (1.0, 1.0j):
        for flat in range(size * size):
            matrix = np.zeros((size, size), dtype=complex)
            matrix.ravel()[flat] = component
            antiunitary = project_antiunitary(matrix, weights)
            complement = antiunitary - project_physical(antiunitary, weights)
            candidates.append(base.matrix_vector(complement))
    _, singular_values, right = np.linalg.svd(np.array(candidates), full_matrices=False)
    tolerance = max(singular_values[0] * 1.0e-12, 1.0e-14)
    rank = int(np.count_nonzero(singular_values > tolerance))
    return right[:rank]


def symmetry_complement_vector(
    matrix: np.ndarray, weights: tuple[Weight, ...]
) -> np.ndarray:
    normalized = base.normalize_matrix(matrix)
    complement = normalized - normalized_physical(matrix, weights)
    return symmetry_complement_basis(weights) @ base.matrix_vector(complement)


def symmetry_complement_metric(
    blocks: np.ndarray,
    source_weights: tuple[Weight, ...],
    target_weights: tuple[Weight, ...],
) -> base.CovarianceMetric:
    def coordinates(matrix: np.ndarray) -> np.ndarray:
        target = base.submatrix(matrix, source_weights, target_weights)
        return symmetry_complement_vector(target, target_weights)

    center = coordinates(np.mean(blocks, axis=0))
    leaves = np.array([coordinates(mean) for mean in base.leave_one_means(blocks)])
    covariance = base.jackknife_covariance(leaves)
    return base.covariance_metric(center, covariance)


def antiunitary_sample_error(
    samples: np.ndarray,
    source_weights: tuple[Weight, ...],
    target_weights: tuple[Weight, ...],
) -> float:
    index = {weight: i for i, weight in enumerate(source_weights)}
    positions = [index[weight] for weight in target_weights]
    selected = samples[:, positions][:, :, positions]
    permutation = conjugation_permutation(target_weights)
    transformed = selected[:, permutation][:, :, permutation].conj()
    return float(np.max(np.abs(selected - transformed)))


def symmetry_role_analysis(
    middle_blocks: np.ndarray,
    full_blocks: np.ndarray,
    source_weights: tuple[Weight, ...],
    target_weights: tuple[Weight, ...],
) -> tuple[np.ndarray, np.ndarray]:
    def coordinates(matrix: np.ndarray) -> np.ndarray:
        target = base.submatrix(matrix, source_weights, target_weights)
        return symmetry_complement_vector(target, target_weights)

    center = np.concatenate(
        (
            coordinates(np.mean(middle_blocks, axis=0)),
            coordinates(np.mean(full_blocks, axis=0)),
        )
    )
    middle_leave = base.leave_one_means(middle_blocks)
    full_leave = base.leave_one_means(full_blocks)
    leaves = np.array(
        [
            np.concatenate((coordinates(middle), coordinates(full)))
            for middle, full in zip(middle_leave, full_leave)
        ]
    )
    return center, base.jackknife_covariance(leaves)


def symmetry_joint_analysis(
    train_middle_blocks: np.ndarray,
    train_full_blocks: np.ndarray,
    validation_middle_blocks: np.ndarray,
    validation_full_blocks: np.ndarray,
    source_weights: tuple[Weight, ...],
    target_weights: tuple[Weight, ...],
) -> SymmetryJointAnalysis:
    train_vector, train_covariance = symmetry_role_analysis(
        train_middle_blocks, train_full_blocks, source_weights, target_weights
    )
    validation_vector, validation_covariance = symmetry_role_analysis(
        validation_middle_blocks,
        validation_full_blocks,
        source_weights,
        target_weights,
    )
    dimension = len(train_vector) + len(validation_vector)
    covariance = np.zeros((dimension, dimension))
    split = len(train_vector)
    covariance[:split, :split] = train_covariance
    covariance[split:, split:] = validation_covariance
    residual = np.concatenate((train_vector, validation_vector))
    return SymmetryJointAnalysis(
        residual_vector=residual,
        covariance=covariance,
        metric=base.covariance_metric(residual, covariance),
    )


def heldout_minimum_direction(
    training_blocks: np.ndarray,
    validation_blocks: np.ndarray,
    source_weights: tuple[Weight, ...],
    target_weights: tuple[Weight, ...],
) -> tuple[float, float, float, float]:
    training = normalized_physical(
        base.submatrix(
            np.mean(training_blocks, axis=0), source_weights, target_weights
        ),
        target_weights,
    ).real
    training_eigenvalues, training_eigenvectors = np.linalg.eigh(training)
    direction = training_eigenvectors[:, 0]
    validation = normalized_physical(
        base.submatrix(
            np.mean(validation_blocks, axis=0), source_weights, target_weights
        ),
        target_weights,
    ).real
    value = float(direction @ validation @ direction)
    leave_values = np.array(
        [
            float(
                direction
                @ normalized_physical(
                    base.submatrix(mean, source_weights, target_weights),
                    target_weights,
                ).real
                @ direction
            )
            for mean in base.leave_one_means(validation_blocks)
        ]
    )
    covariance = base.jackknife_covariance(leave_values[:, None])
    error = math.sqrt(max(float(covariance[0, 0]), 0.0))
    z_value = value / error if error > 0.0 else -math.inf
    return float(training_eigenvalues[0]), value, error, z_value


def scalar_denominator_diagnostics(
    chain_values: list[np.ndarray], block_values: np.ndarray
) -> tuple[float, float, float]:
    """Return minimum block value, relative SE, and maximum chain deviation."""
    values = np.asarray(block_values, dtype=float)
    center = float(np.mean(values))
    leave_values = base.leave_one_means(values)
    covariance = base.jackknife_covariance(leave_values[:, None])
    error = math.sqrt(max(float(covariance[0, 0]), 0.0))
    chain_means = np.array(
        [float(np.mean(chain)) for chain in chain_values], dtype=float
    )
    maximum_chain_z = (
        float(np.max(np.abs(chain_means - center)) / error)
        if error > 0.0
        else math.inf
    )
    relative_error = error / abs(center) if center != 0.0 else math.inf
    return float(np.min(values)), relative_error, maximum_chain_z


def forward_influence_samples(
    chains: list[CommonIntegralChain],
    source_weights: tuple[Weight, ...],
    operator: base.SectorOperators,
    target_weights: tuple[Weight, ...],
    diagonal_only: bool,
) -> list[np.ndarray]:
    output: list[np.ndarray] = []
    operator_index = {weight: i for i, weight in enumerate(operator.weights)}
    source_index = {weight: i for i, weight in enumerate(source_weights)}
    source_positions = [source_index[weight] for weight in operator.weights]
    target_positions = [operator_index[weight] for weight in target_weights]
    boundary = operator.multiplier[
        np.ix_(target_positions, range(len(operator.weights)))
    ]
    for chain in chains:
        transformed: list[np.ndarray] = []
        for sample in chain.middle_samples:
            middle = sample[np.ix_(source_positions, source_positions)]
            middle = project_physical(middle, operator.weights)
            if diagonal_only:
                middle = np.diag(np.diag(middle))
            transformed.append(boundary @ middle @ boundary.T)
        output.append(np.array(transformed))
    return output


def run_common_integral_chain(
    seed: int,
    initial: str,
    therm: int,
    measure: int,
    sample_every: int,
    weights: tuple[Weight, ...],
) -> CommonIntegralChain:
    rng = np.random.default_rng(seed)
    links = base.initial_links(rng, initial, slices=2)
    epsilon = 0.32
    for sweep in range(therm):
        acceptance = base.two_slice_sweep(links, rng, epsilon, base.BETA)
        if (sweep + 1) % 25 == 0:
            epsilon = base.adapted_epsilon(epsilon, acceptance)

    full_samples: list[np.ndarray] = []
    middle_samples: list[np.ndarray] = []
    deformed_samples: list[np.ndarray] = []
    spatial_plaquettes: list[float] = []
    mixed_plaquettes: list[float] = []
    inverse_pair_weights: list[float] = []
    acceptances: list[float] = []
    for sweep in range(measure):
        acceptances.append(base.two_slice_sweep(links, rng, epsilon, base.BETA))
        if (sweep + 1) % sample_every:
            continue
        traces0 = base.all_face_traces(links[0])
        traces1 = base.all_face_traces(links[1])
        incoming = base.character_table(traces0, weights)
        outgoing = base.character_table(traces1, weights)
        inverse_pair = np.exp(
            -(base.BETA / 6.0) * (traces0.real + traces1.real)
        )
        full_samples.append(outgoing.conj().T @ incoming / len(base.FACES))
        middle_samples.append(
            np.einsum(
                "fi,fj,f->ij",
                outgoing.conj(),
                incoming,
                inverse_pair,
                optimize=True,
            )
            / len(base.FACES)
        )
        target_positions = [weights.index(weight) for weight in base.weights_box(1)]
        incoming_target = incoming[:, target_positions]
        outgoing_target = outgoing[:, target_positions]
        x0 = traces0.real / 3.0
        x1 = traces1.real / 3.0
        deformed_samples.append(
            np.array(
                [
                    np.einsum(
                        "fi,fj,f->ij",
                        outgoing_target.conj(),
                        incoming_target,
                        inverse_pair * (1.0 + parameter * x0) * (1.0 + parameter * x1),
                        optimize=True,
                    )
                    / len(base.FACES)
                    for parameter in DEFORMATION_PARAMETERS
                ]
            )
        )
        spatial_plaquettes.append(
            float(np.mean(np.concatenate((traces0.real, traces1.real))) / 3.0)
        )
        mixed_plaquettes.append(
            float(
                np.mean(
                    [
                        base.mixed_real_trace(links, link_id)
                        for link_id in range(3 * base.L**3)
                    ]
                )
                / 3.0
            )
        )
        inverse_pair_weights.append(float(np.mean(inverse_pair)))
    return CommonIntegralChain(
        seed=seed,
        initial=initial,
        acceptance=float(np.mean(acceptances)),
        epsilon=epsilon,
        full_samples=np.array(full_samples),
        middle_samples=np.array(middle_samples),
        deformed_samples=np.array(deformed_samples),
        spatial_plaquettes=np.array(spatial_plaquettes),
        mixed_plaquettes=np.array(mixed_plaquettes),
        inverse_pair_weights=np.array(inverse_pair_weights),
    )


def general_forward(middle: np.ndarray, operator: base.SectorOperators) -> np.ndarray:
    physical = project_physical(middle, operator.weights)
    raw = operator.multiplier @ physical @ operator.multiplier
    return normalized_physical(raw, operator.weights)


def diagonal_forward(middle: np.ndarray, operator: base.SectorOperators) -> np.ndarray:
    physical = project_physical(middle, operator.weights)
    diagonal = np.diag(np.diag(physical))
    raw = operator.multiplier @ diagonal @ operator.multiplier
    return normalized_physical(raw, operator.weights)


def forward_target(
    middle: np.ndarray,
    operator: base.SectorOperators,
    target_weights: tuple[Weight, ...],
    diagonal_only: bool = False,
) -> np.ndarray:
    """Compute only the target block of M Q M, without a full dense output."""
    physical = project_physical(middle, operator.weights)
    if diagonal_only:
        physical = np.diag(np.diag(physical))
    index = {weight: i for i, weight in enumerate(operator.weights)}
    positions = [index[weight] for weight in target_weights]
    boundary = operator.multiplier[np.ix_(positions, range(len(operator.weights)))]
    raw = boundary @ physical @ boundary.T
    return normalized_physical(raw, target_weights)


def predictive_analysis(
    training_blocks: np.ndarray,
    validation_blocks: np.ndarray,
    training_weights: tuple[Weight, ...],
    operator: base.SectorOperators,
    target_weights: tuple[Weight, ...],
    diagonal_only: bool = False,
    validation_weights: tuple[Weight, ...] | None = None,
) -> PredictiveAnalysis:
    measured_weights = training_weights if validation_weights is None else validation_weights
    measured = normalized_physical(
        base.submatrix(
            np.mean(validation_blocks, axis=0), measured_weights, target_weights
        ),
        target_weights,
    )
    middle = normalized_physical(
        base.submatrix(
            np.mean(training_blocks, axis=0), training_weights, operator.weights
        ),
        operator.weights,
    )
    modeled = forward_target(middle, operator, target_weights, diagonal_only)
    residual = project_physical(measured - modeled, target_weights)

    validation_leave = np.array(
        [
            project_physical(
                normalized_physical(
                    base.submatrix(mean, measured_weights, target_weights),
                    target_weights,
                )
                - modeled,
                target_weights,
            )
            for mean in base.leave_one_means(validation_blocks)
        ]
    )
    training_leave = np.array(
        [
            project_physical(
                measured
                - forward_target(
                    normalized_physical(
                        base.submatrix(
                            mean, training_weights, operator.weights
                        ),
                        operator.weights,
                    ),
                    operator,
                    target_weights,
                    diagonal_only,
                ),
                target_weights,
            )
            for mean in base.leave_one_means(training_blocks)
        ]
    )
    coordinate_covariance = base.jackknife_covariance(
        np.array([base.matrix_vector(value) for value in validation_leave])
    ) + base.jackknife_covariance(
        np.array([base.matrix_vector(value) for value in training_leave])
    )
    basis = physical_coordinate_basis(target_weights)
    covariance = base.jackknife_covariance(
        np.array([physical_vector(value, basis) for value in validation_leave])
    ) + base.jackknife_covariance(
        np.array([physical_vector(value, basis) for value in training_leave])
    )
    vector = physical_vector(residual, basis)
    return PredictiveAnalysis(
        measured=measured,
        middle=middle,
        modeled=modeled,
        residual=residual,
        covariance=covariance,
        coordinate_covariance=coordinate_covariance,
        metric=base.covariance_metric(vector, covariance),
        validation_leave=validation_leave,
        training_leave=training_leave,
    )


def polynomial_operator(parameter: float) -> base.SectorOperators:
    recurrence, weights_list, _ = base.build_numeric_recurrence(2)
    weights = tuple(weights_list)
    multiplier = np.eye(len(weights)) + parameter * recurrence
    inverse = np.linalg.inv(multiplier)
    identity = np.eye(len(weights))
    return base.SectorOperators(
        nmax=2,
        weights=weights,
        multiplier=multiplier,
        inverse_multiplier=inverse,
        diagonal=identity,
        multiplier_condition=float(np.linalg.cond(multiplier)),
        diagonal_condition=1.0,
    )


def diagonal_orbit_candidates(weights: tuple[Weight, ...]) -> tuple[np.ndarray, ...]:
    permutation = conjugation_permutation(weights)
    candidates: list[np.ndarray] = []
    visited: set[int] = set()
    for i, j in enumerate(permutation):
        if i in visited:
            continue
        matrix = np.zeros((len(weights), len(weights)))
        matrix[i, i] = 1.0
        matrix[j, j] = 1.0
        candidates.append(matrix)
        visited.update((i, int(j)))
    return tuple(candidates)


@functools.lru_cache(maxsize=None)
def polynomial_diagonal_design(
    parameter: float, target_weights: tuple[Weight, ...]
) -> np.ndarray:
    operator = polynomial_operator(parameter)
    index = {weight: i for i, weight in enumerate(operator.weights)}
    positions = [index[weight] for weight in target_weights]
    boundary = operator.multiplier[
        np.ix_(positions, range(len(operator.weights)))
    ]
    physical_basis = physical_unnormalized_basis(target_weights)
    columns = []
    for candidate in diagonal_orbit_candidates(operator.weights):
        raw = boundary @ candidate @ boundary.T
        columns.append(
            physical_unnormalized_vector(raw, physical_basis, target_weights)
        )
    return np.column_stack(columns)


@functools.lru_cache(maxsize=None)
def polynomial_diagonal_null_basis(
    parameter: float, target_weights: tuple[Weight, ...]
) -> np.ndarray:
    """Fixed two-dimensional left null of the unnormalized diagonal image."""
    design = polynomial_diagonal_design(parameter, target_weights)
    left, singular_values, _ = np.linalg.svd(design, full_matrices=True)
    tolerance = max(singular_values[0] * 1.0e-12, 1.0e-14)
    rank = int(np.count_nonzero(singular_values > tolerance))
    null_basis = left[:, rank:].T
    for row in null_basis:
        pivot = int(np.argmax(np.abs(row)))
        if row[pivot] < 0.0:
            row *= -1.0
    return null_basis


def polynomial_null_contrast_vector(
    deformed_matrices: np.ndarray,
    target_weights: tuple[Weight, ...],
) -> np.ndarray:
    physical_basis = physical_unnormalized_basis(target_weights)
    values = []
    for position, parameter in enumerate(DEFORMATION_PARAMETERS):
        coordinates = physical_unnormalized_vector(
            deformed_matrices[position], physical_basis, target_weights
        )
        values.extend(polynomial_diagonal_null_basis(parameter, target_weights) @ coordinates)
    return np.asarray(values, dtype=float)


def polynomial_null_analysis(
    deformed_blocks: np.ndarray,
    target_weights: tuple[Weight, ...],
) -> PolynomialNullAnalysis:
    block_vectors = np.array(
        [
            polynomial_null_contrast_vector(block, target_weights)
            for block in deformed_blocks
        ]
    )
    center = np.mean(block_vectors, axis=0)
    leave_vectors = base.leave_one_means(block_vectors)
    covariance = base.jackknife_covariance(leave_vectors)
    return PolynomialNullAnalysis(
        residual_vector=center,
        covariance=covariance,
        metric=base.covariance_metric(center, covariance),
        block_vectors=block_vectors,
    )


def maximum_vector_autocorrelation(sample_vectors: list[np.ndarray]) -> float:
    maximum = 0.5
    for samples in sample_vectors:
        for column in range(samples.shape[1]):
            values = samples[:, column]
            if float(np.var(values)) > 1.0e-20:
                maximum = max(
                    maximum,
                    base.integrated_autocorrelation_time(values),
                )
    return maximum


def maximum_vector_chain_deviation(
    chain_vectors: list[np.ndarray],
    center: np.ndarray,
    covariance: np.ndarray,
) -> float:
    errors = np.sqrt(np.clip(np.diag(covariance), 0.0, None))
    usable = errors > 1.0e-14
    if not np.any(usable):
        return math.inf
    return max(
        float(np.max(np.abs(vector - center)[usable] / errors[usable]))
        for vector in chain_vectors
    )


def forward_jacobian_rank(
    operator: base.SectorOperators,
    target_weights: tuple[Weight, ...],
    diagonal_only: bool,
) -> int:
    weights = operator.weights
    size = len(weights)
    candidates: list[np.ndarray] = []
    if diagonal_only:
        permutation = conjugation_permutation(weights)
        visited: set[int] = set()
        for i, j in enumerate(permutation):
            if i in visited:
                continue
            matrix = np.zeros((size, size))
            matrix[i, i] = 1.0
            matrix[j, j] = 1.0
            candidates.append(matrix)
            visited.update((i, int(j)))
    else:
        swap_basis, plus_size = swap_eigenbasis(weights)
        for lo, hi in ((0, plus_size), (plus_size, size)):
            for i in range(lo, hi):
                for j in range(i, hi):
                    blocked = np.zeros((size, size))
                    blocked[i, j] = 1.0
                    blocked[j, i] = 1.0
                    candidates.append(swap_basis @ blocked @ swap_basis.T)
    index = {weight: i for i, weight in enumerate(weights)}
    positions = [index[weight] for weight in target_weights]
    boundary = operator.multiplier[np.ix_(positions, range(size))]
    raw_center = boundary @ np.eye(size) @ boundary.T
    denominator = float(raw_center[0, 0])
    coordinate_basis = physical_coordinate_basis(target_weights)
    columns: list[np.ndarray] = []
    for candidate in candidates:
        derivative_raw = boundary @ candidate @ boundary.T
        derivative = (
            derivative_raw * denominator
            - raw_center * float(derivative_raw[0, 0])
        ) / denominator**2
        columns.append(physical_vector(derivative, coordinate_basis))
    jacobian = np.column_stack(columns)
    return int(np.linalg.matrix_rank(jacobian, tol=1.0e-10))


def swap_eigenbasis(weights: tuple[Weight, ...]) -> tuple[np.ndarray, int]:
    """Orthogonal basis with irrep-swap-even columns followed by odd columns."""
    index = {weight: i for i, weight in enumerate(weights)}
    plus: list[np.ndarray] = []
    minus: list[np.ndarray] = []
    visited: set[int] = set()
    for i, (p, q) in enumerate(weights):
        if i in visited:
            continue
        j = index[(q, p)]
        visited.update((i, j))
        if i == j:
            vector = np.zeros(len(weights))
            vector[i] = 1.0
            plus.append(vector)
        else:
            even = np.zeros(len(weights))
            odd = np.zeros(len(weights))
            even[i] = even[j] = 1.0 / math.sqrt(2.0)
            odd[i] = 1.0 / math.sqrt(2.0)
            odd[j] = -1.0 / math.sqrt(2.0)
            plus.append(even)
            minus.append(odd)
    return np.column_stack(plus + minus), len(plus)


def structural_middle_model(
    matrix: np.ndarray,
    weights: tuple[Weight, ...],
    family: str,
) -> np.ndarray:
    physical = normalized_physical(matrix, weights)
    if family == "general":
        return physical
    if family == "diagonal":
        return normalized_physical(np.diag(np.diag(physical)), weights)
    if family not in {"perron_plus", "perron_plus_minus"}:
        raise ValueError(f"unknown structural family: {family}")
    basis, plus_size = swap_eigenbasis(weights)
    blocked = basis.T @ physical.real @ basis
    plus_block = 0.5 * (blocked[:plus_size, :plus_size] + blocked[:plus_size, :plus_size].T)
    eigenvalues, eigenvectors = np.linalg.eigh(plus_block)
    leading = eigenvectors[:, -1]
    truncated = np.zeros_like(blocked)
    truncated[:plus_size, :plus_size] = eigenvalues[-1] * np.outer(leading, leading)
    if family == "perron_plus_minus":
        truncated[plus_size:, plus_size:] = blocked[plus_size:, plus_size:]
    reconstructed = basis @ truncated @ basis.T
    return normalized_physical(reconstructed, weights)


def structural_analysis(
    training_blocks: np.ndarray,
    validation_blocks: np.ndarray,
    source_weights: tuple[Weight, ...],
    target_weights: tuple[Weight, ...],
    family: str,
) -> PredictiveAnalysis:
    training_center = base.submatrix(
        np.mean(training_blocks, axis=0), source_weights, target_weights
    )
    validation_center = base.submatrix(
        np.mean(validation_blocks, axis=0), source_weights, target_weights
    )
    middle = normalized_physical(training_center, target_weights)
    measured = normalized_physical(validation_center, target_weights)
    modeled = structural_middle_model(middle, target_weights, family)
    residual = project_physical(measured - modeled, target_weights)
    validation_leave = np.array(
        [
            project_physical(
                normalized_physical(
                    base.submatrix(mean, source_weights, target_weights),
                    target_weights,
                )
                - modeled,
                target_weights,
            )
            for mean in base.leave_one_means(validation_blocks)
        ]
    )
    training_leave = np.array(
        [
            project_physical(
                measured
                - structural_middle_model(
                    base.submatrix(mean, source_weights, target_weights),
                    target_weights,
                    family,
                ),
                target_weights,
            )
            for mean in base.leave_one_means(training_blocks)
        ]
    )
    coordinate_covariance = base.jackknife_covariance(
        np.array([base.matrix_vector(value) for value in validation_leave])
    ) + base.jackknife_covariance(
        np.array([base.matrix_vector(value) for value in training_leave])
    )
    coordinate_basis = physical_coordinate_basis(target_weights)
    covariance = base.jackknife_covariance(
        np.array([physical_vector(value, coordinate_basis) for value in validation_leave])
    ) + base.jackknife_covariance(
        np.array([physical_vector(value, coordinate_basis) for value in training_leave])
    )
    return PredictiveAnalysis(
        measured=measured,
        middle=middle,
        modeled=modeled,
        residual=residual,
        covariance=covariance,
        coordinate_covariance=coordinate_covariance,
        metric=base.covariance_metric(
            physical_vector(residual, coordinate_basis), covariance
        ),
        validation_leave=validation_leave,
        training_leave=training_leave,
    )


def stack_predictive_analyses(
    analyses: tuple[PredictiveAnalysis, ...],
    target_weights: tuple[Weight, ...],
) -> JointAnalysis:
    basis = physical_coordinate_basis(target_weights)
    residual = np.concatenate(
        [physical_vector(analysis.residual, basis) for analysis in analyses]
    )
    validation_leave = np.array(
        [
            np.concatenate(
                [
                    physical_vector(analysis.validation_leave[index], basis)
                    for analysis in analyses
                ]
            )
            for index in range(len(analyses[0].validation_leave))
        ]
    )
    training_leave = np.array(
        [
            np.concatenate(
                [
                    physical_vector(analysis.training_leave[index], basis)
                    for analysis in analyses
                ]
            )
            for index in range(len(analyses[0].training_leave))
        ]
    )
    covariance = base.jackknife_covariance(
        validation_leave
    ) + base.jackknife_covariance(training_leave)
    return JointAnalysis(
        residual_vector=residual,
        covariance=covariance,
        metric=base.covariance_metric(residual, covariance),
        validation_leave_vectors=validation_leave,
        training_leave_vectors=training_leave,
    )


def build_joint_analysis(
    training_middle_blocks: np.ndarray,
    validation_full_blocks: np.ndarray,
    validation_deformed_blocks: np.ndarray,
    source_weights: tuple[Weight, ...],
    exponential_operator: base.SectorOperators,
    polynomial_operators: dict[float, base.SectorOperators],
    target_weights: tuple[Weight, ...],
    diagonal_only: bool,
) -> JointAnalysis:
    analyses: list[PredictiveAnalysis] = [
        predictive_analysis(
            training_middle_blocks,
            validation_full_blocks,
            source_weights,
            exponential_operator,
            target_weights,
            diagonal_only=diagonal_only,
        )
    ]
    for position, parameter in enumerate(DEFORMATION_PARAMETERS):
        analyses.append(
            predictive_analysis(
                training_middle_blocks,
                validation_deformed_blocks[:, position],
                source_weights,
                polynomial_operators[parameter],
                target_weights,
                diagonal_only=diagonal_only,
                validation_weights=target_weights,
            )
        )
    return stack_predictive_analyses(tuple(analyses), target_weights)


def joint_block_bootstrap(
    training_middle_blocks: np.ndarray,
    validation_full_blocks: np.ndarray,
    validation_deformed_blocks: np.ndarray,
    source_weights: tuple[Weight, ...],
    exponential_operator: base.SectorOperators,
    polynomial_operators: dict[float, base.SectorOperators],
    target_weights: tuple[Weight, ...],
    observed: JointAnalysis,
    blocks_per_chain: int,
    replicates: int,
    diagonal_only: bool,
    seed_offset: int,
) -> tuple[int, int, float, float, float]:
    """Null-centered, replicate-studentized joint train/validation bootstrap."""
    training_by_chain = training_middle_blocks.reshape(
        CHAINS_PER_ROLE,
        blocks_per_chain,
        *training_middle_blocks.shape[1:],
    )
    validation_full_by_chain = validation_full_blocks.reshape(
        CHAINS_PER_ROLE,
        blocks_per_chain,
        *validation_full_blocks.shape[1:],
    )
    validation_deformed_by_chain = validation_deformed_blocks.reshape(
        CHAINS_PER_ROLE,
        blocks_per_chain,
        *validation_deformed_blocks.shape[1:],
    )
    rng = np.random.default_rng(BOOTSTRAP_SEED + seed_offset)
    chain_index = np.arange(CHAINS_PER_ROLE)[:, None]
    exceeded = 0
    rank_failures = 0
    for _ in range(replicates):
        training_indices = rng.integers(
            0, blocks_per_chain, size=(CHAINS_PER_ROLE, blocks_per_chain)
        )
        validation_indices = rng.integers(
            0, blocks_per_chain, size=(CHAINS_PER_ROLE, blocks_per_chain)
        )
        training_resample = training_by_chain[
            chain_index, training_indices
        ].reshape(-1, *training_middle_blocks.shape[1:])
        validation_full_resample = validation_full_by_chain[
            chain_index, validation_indices
        ].reshape(-1, *validation_full_blocks.shape[1:])
        validation_deformed_resample = validation_deformed_by_chain[
            chain_index, validation_indices
        ].reshape(-1, *validation_deformed_blocks.shape[1:])
        replicate = build_joint_analysis(
            training_resample,
            validation_full_resample,
            validation_deformed_resample,
            source_weights,
            exponential_operator,
            polynomial_operators,
            target_weights,
            diagonal_only,
        )
        null_residual = replicate.residual_vector - observed.residual_vector
        metric = base.covariance_metric(null_residual, replicate.covariance)
        if (
            not metric.psd
            or metric.rank != len(null_residual)
            or not math.isfinite(metric.chi_square)
        ):
            rank_failures += 1
            exceeded += 1
        else:
            exceeded += int(metric.chi_square >= observed.metric.chi_square)
    p_value = (exceeded + 1.0) / (replicates + 1.0)
    lower_95 = (
        float(base.beta_distribution.ppf(0.05, exceeded, replicates - exceeded + 1))
        if exceeded > 0
        else 0.0
    )
    upper_95 = (
        float(base.beta_distribution.ppf(0.95, exceeded + 1, replicates - exceeded))
        if exceeded < replicates
        else 1.0
    )
    return exceeded, rank_failures, p_value, lower_95, upper_95


def symmetry_joint_block_bootstrap(
    train_middle_blocks: np.ndarray,
    train_full_blocks: np.ndarray,
    validation_middle_blocks: np.ndarray,
    validation_full_blocks: np.ndarray,
    source_weights: tuple[Weight, ...],
    target_weights: tuple[Weight, ...],
    observed: SymmetryJointAnalysis,
    blocks_per_chain: int,
    replicates: int,
) -> tuple[int, int, float, float, float]:
    """Null-centered joint bootstrap for four exact-symmetry complements."""
    arrays = (
        train_middle_blocks,
        train_full_blocks,
        validation_middle_blocks,
        validation_full_blocks,
    )
    by_chain = [
        array.reshape(
            CHAINS_PER_ROLE,
            blocks_per_chain,
            *array.shape[1:],
        )
        for array in arrays
    ]
    rng = np.random.default_rng(BOOTSTRAP_SEED + 3000)
    chain_index = np.arange(CHAINS_PER_ROLE)[:, None]
    exceeded = 0
    rank_failures = 0
    for _ in range(replicates):
        train_indices = rng.integers(
            0, blocks_per_chain, size=(CHAINS_PER_ROLE, blocks_per_chain)
        )
        validation_indices = rng.integers(
            0, blocks_per_chain, size=(CHAINS_PER_ROLE, blocks_per_chain)
        )
        resampled = []
        for position, array in enumerate(by_chain):
            indices = train_indices if position < 2 else validation_indices
            resampled.append(
                array[chain_index, indices].reshape(-1, *arrays[position].shape[1:])
            )
        replicate = symmetry_joint_analysis(
            *resampled, source_weights, target_weights
        )
        null_residual = replicate.residual_vector - observed.residual_vector
        metric = base.covariance_metric(null_residual, replicate.covariance)
        if (
            not metric.psd
            or metric.rank != len(null_residual)
            or not math.isfinite(metric.chi_square)
        ):
            rank_failures += 1
            exceeded += 1
        else:
            exceeded += int(metric.chi_square >= observed.metric.chi_square)
    p_value = (exceeded + 1.0) / (replicates + 1.0)
    lower_95 = (
        float(base.beta_distribution.ppf(0.05, exceeded, replicates - exceeded + 1))
        if exceeded > 0
        else 0.0
    )
    upper_95 = (
        float(base.beta_distribution.ppf(0.95, exceeded + 1, replicates - exceeded))
        if exceeded < replicates
        else 1.0
    )
    return exceeded, rank_failures, p_value, lower_95, upper_95


def polynomial_null_block_bootstrap(
    deformed_blocks: np.ndarray,
    target_weights: tuple[Weight, ...],
    observed: PolynomialNullAnalysis,
    blocks_per_chain: int,
    replicates: int,
) -> tuple[int, int, float, float, float]:
    """Null-centered stratified bootstrap of the exact diagonal-null contrasts."""
    chains = 2 * CHAINS_PER_ROLE
    by_chain = deformed_blocks.reshape(
        chains,
        blocks_per_chain,
        *deformed_blocks.shape[1:],
    )
    rng = np.random.default_rng(BOOTSTRAP_SEED + 4000)
    chain_index = np.arange(chains)[:, None]
    exceeded = 0
    rank_failures = 0
    for _ in range(replicates):
        indices = rng.integers(0, blocks_per_chain, size=(chains, blocks_per_chain))
        resampled = by_chain[chain_index, indices].reshape(
            -1, *deformed_blocks.shape[1:]
        )
        replicate = polynomial_null_analysis(resampled, target_weights)
        null_residual = replicate.residual_vector - observed.residual_vector
        metric = base.covariance_metric(null_residual, replicate.covariance)
        if (
            not metric.psd
            or metric.rank != len(null_residual)
            or not math.isfinite(metric.chi_square)
        ):
            rank_failures += 1
            exceeded += 1
        else:
            exceeded += int(metric.chi_square >= observed.metric.chi_square)
    p_value = (exceeded + 1.0) / (replicates + 1.0)
    lower_95 = (
        float(base.beta_distribution.ppf(0.05, exceeded, replicates - exceeded + 1))
        if exceeded > 0
        else 0.0
    )
    upper_95 = (
        float(base.beta_distribution.ppf(0.95, exceeded + 1, replicates - exceeded))
        if exceeded < replicates
        else 1.0
    )
    return exceeded, rank_failures, p_value, lower_95, upper_95


def improvement_block_bootstrap(
    training_middle_blocks: np.ndarray,
    validation_full_blocks: np.ndarray,
    validation_deformed_blocks: np.ndarray,
    source_weights: tuple[Weight, ...],
    exponential_operator: base.SectorOperators,
    polynomial_operators: dict[float, base.SectorOperators],
    target_weights: tuple[Weight, ...],
    blocks_per_chain: int,
    replicates: int,
) -> tuple[float, float, float]:
    """Paired bootstrap for the general-minus-diagonal predictive improvement."""
    training_by_chain = training_middle_blocks.reshape(
        CHAINS_PER_ROLE,
        blocks_per_chain,
        *training_middle_blocks.shape[1:],
    )
    validation_full_by_chain = validation_full_blocks.reshape(
        CHAINS_PER_ROLE,
        blocks_per_chain,
        *validation_full_blocks.shape[1:],
    )
    validation_deformed_by_chain = validation_deformed_blocks.reshape(
        CHAINS_PER_ROLE,
        blocks_per_chain,
        *validation_deformed_blocks.shape[1:],
    )
    rng = np.random.default_rng(BOOTSTRAP_SEED + 2000)
    chain_index = np.arange(CHAINS_PER_ROLE)[:, None]
    deltas = np.empty(replicates)
    for replicate_index in range(replicates):
        training_indices = rng.integers(
            0, blocks_per_chain, size=(CHAINS_PER_ROLE, blocks_per_chain)
        )
        validation_indices = rng.integers(
            0, blocks_per_chain, size=(CHAINS_PER_ROLE, blocks_per_chain)
        )
        training_resample = training_by_chain[
            chain_index, training_indices
        ].reshape(-1, *training_middle_blocks.shape[1:])
        validation_full_resample = validation_full_by_chain[
            chain_index, validation_indices
        ].reshape(-1, *validation_full_blocks.shape[1:])
        validation_deformed_resample = validation_deformed_by_chain[
            chain_index, validation_indices
        ].reshape(-1, *validation_deformed_blocks.shape[1:])
        general = build_joint_analysis(
            training_resample,
            validation_full_resample,
            validation_deformed_resample,
            source_weights,
            exponential_operator,
            polynomial_operators,
            target_weights,
            diagonal_only=False,
        )
        diagonal = build_joint_analysis(
            training_resample,
            validation_full_resample,
            validation_deformed_resample,
            source_weights,
            exponential_operator,
            polynomial_operators,
            target_weights,
            diagonal_only=True,
        )
        deltas[replicate_index] = float(
            np.dot(diagonal.residual_vector, diagonal.residual_vector)
            - np.dot(general.residual_vector, general.residual_vector)
        )
    return (
        float(np.quantile(deltas, 0.01)),
        float(np.median(deltas)),
        float(np.quantile(deltas, 0.99)),
    )


def paired_analysis(
    middle_blocks: np.ndarray,
    full_blocks: np.ndarray,
    source_weights: tuple[Weight, ...],
    operator: base.SectorOperators,
    target_weights: tuple[Weight, ...],
) -> PredictiveAnalysis:
    """Common-sample implementation/truncation check with paired covariance."""
    measured = normalized_physical(
        base.submatrix(np.mean(full_blocks, axis=0), source_weights, target_weights),
        target_weights,
    )
    middle = normalized_physical(
        base.submatrix(np.mean(middle_blocks, axis=0), source_weights, operator.weights),
        operator.weights,
    )
    modeled = normalized_physical(
        base.submatrix(
            general_forward(middle, operator), operator.weights, target_weights
        ),
        target_weights,
    )
    residual = project_physical(measured - modeled, target_weights)
    middle_leave = base.leave_one_means(middle_blocks)
    full_leave = base.leave_one_means(full_blocks)
    paired_leave = np.array(
        [
            project_physical(
                normalized_physical(
                    base.submatrix(c_mean, source_weights, target_weights),
                    target_weights,
                )
                - normalized_physical(
                    base.submatrix(
                        general_forward(
                            normalized_physical(
                                base.submatrix(q_mean, source_weights, operator.weights),
                                operator.weights,
                            ),
                            operator,
                        ),
                        operator.weights,
                        target_weights,
                    ),
                    target_weights,
                ),
                target_weights,
            )
            for q_mean, c_mean in zip(middle_leave, full_leave)
        ]
    )
    coordinate_covariance = base.jackknife_covariance(
        np.array([base.matrix_vector(value) for value in paired_leave])
    )
    basis = physical_coordinate_basis(target_weights)
    covariance = base.jackknife_covariance(
        np.array([physical_vector(value, basis) for value in paired_leave])
    )
    return PredictiveAnalysis(
        measured=measured,
        middle=middle,
        modeled=modeled,
        residual=residual,
        covariance=covariance,
        coordinate_covariance=coordinate_covariance,
        metric=base.covariance_metric(
            physical_vector(residual, basis), covariance
        ),
        validation_leave=paired_leave,
        training_leave=np.empty((0, *paired_leave.shape[1:]), dtype=complex),
    )


def projected_models(
    middle_blocks: np.ndarray,
    source_weights: tuple[Weight, ...],
    operators: dict[int, base.SectorOperators],
    target_weights: tuple[Weight, ...],
) -> dict[int, np.ndarray]:
    center = np.mean(middle_blocks, axis=0)
    models: dict[int, np.ndarray] = {}
    for nmax, operator in operators.items():
        middle = base.submatrix(center, source_weights, operator.weights)
        models[nmax] = normalized_physical(
            base.submatrix(
                general_forward(middle, operator), operator.weights, target_weights
            ),
            target_weights,
        )
    return models


def deletion_weight_control() -> tuple[float, float]:
    rng = np.random.default_rng(96211)
    links = base.initial_links(rng, "hot", slices=2)
    traces0 = base.all_face_traces(links[0])
    traces1 = base.all_face_traces(links[1])
    exponent = (base.BETA / 6.0) * (traces0.real + traces1.real)
    exact = float(np.max(np.abs(np.exp(exponent) * np.exp(-exponent) - 1.0)))
    mutated = float(
        np.max(np.abs(np.exp(exponent) * np.exp(-2.0 * exponent) - 1.0))
    )
    return exact, mutated


def synthetic_control(operator: base.SectorOperators) -> tuple[float, float]:
    rng = np.random.default_rng(96223)
    raw = rng.normal(size=(len(operator.weights), len(operator.weights))) + 1j * rng.normal(
        size=(len(operator.weights), len(operator.weights))
    )
    middle = project_physical(raw @ raw.conj().T, operator.weights)
    expected = general_forward(middle, operator)
    repeated = general_forward(middle, operator)
    diagonal = diagonal_forward(middle, operator)
    return float(np.max(np.abs(expected - repeated))), float(
        np.max(np.abs(expected - diagonal))
    )


def polynomial_pointwise_forward_control(
    parameter: float, target_weights: tuple[Weight, ...]
) -> tuple[float, float]:
    """Check ``C_g = G Q G`` before any Monte Carlo averaging.

    Degree-one multiplication closes B_1 into B_2 exactly.  A finite set of
    actual SU(3) plaquette holonomies can therefore test the forward identity
    point by point, with arbitrary positive sample weights, without a character
    cutoff or a statistical premise.
    """
    operator = polynomial_operator(parameter)
    rng = np.random.default_rng(96229 + int(round(10.0 * parameter)))
    links = base.initial_links(rng, "hot", slices=2)
    traces0 = base.all_face_traces(links[0])
    traces1 = base.all_face_traces(links[1])
    incoming = base.character_table(traces0, operator.weights)
    outgoing = base.character_table(traces1, operator.weights)
    target_positions = [operator.weights.index(weight) for weight in target_weights]
    incoming_target = incoming[:, target_positions]
    outgoing_target = outgoing[:, target_positions]
    sample_weights = np.exp(-0.17 * (traces0.real + traces1.real))
    x0 = traces0.real / 3.0
    x1 = traces1.real / 3.0
    middle = np.einsum(
        "fi,fj,f->ij", outgoing.conj(), incoming, sample_weights, optimize=True
    )
    measured = np.einsum(
        "fi,fj,f->ij",
        outgoing_target.conj(),
        incoming_target,
        sample_weights * (1.0 + parameter * x0) * (1.0 + parameter * x1),
        optimize=True,
    )
    boundary = operator.multiplier[np.ix_(target_positions, range(len(operator.weights)))]
    modeled = boundary @ middle @ boundary.T
    mutated = (
        np.eye(len(operator.weights)) + (parameter + 0.25) * base.build_numeric_recurrence(2)[0]
    )
    mutated_boundary = mutated[np.ix_(target_positions, range(len(operator.weights)))]
    wrong = mutated_boundary @ middle @ boundary.T
    return float(np.max(np.abs(measured - modeled))), float(
        np.max(np.abs(measured - wrong))
    )


def finite_class_convolution_control(
    weights: tuple[Weight, ...]
) -> tuple[float, float, float, float]:
    """Finite Peter-Weyl iff control and a symmetry-insufficiency witness."""
    dimensions = np.array([base.dim_su3(p, q) for p, q in weights], dtype=float)
    rho = np.array(
        [1.0 + 2.0 * (p + q) + float((p - q) ** 2) for p, q in weights]
    )
    central_coefficients = dimensions * rho
    schur_action = np.diag(central_coefficients / dimensions)
    diagonal_error = float(np.max(np.abs(schur_action - np.diag(rho))))

    index = {weight: position for position, weight in enumerate(weights)}
    vector = np.zeros(len(weights))
    vector[index[(0, 0)]] = 1.0
    vector[index[(1, 1)]] = 1.0
    witness = np.eye(len(weights)) + np.outer(vector, vector)
    permutation = conjugation_permutation(weights)
    swap = np.eye(len(weights))[permutation]
    symmetry_error = max(
        float(np.max(np.abs(witness - witness.T))),
        float(np.max(np.abs(witness @ swap - swap @ witness))),
    )
    off_diagonal = witness - np.diag(np.diag(witness))
    return (
        diagonal_error,
        float(np.min(np.linalg.eigvalsh(witness))),
        symmetry_error,
        float(np.linalg.norm(off_diagonal, ord="fro")),
    )


def casimir_labels(weights: tuple[Weight, ...]) -> tuple[np.ndarray, np.ndarray]:
    quadratic = np.array(
        [float(p * p + q * q + p * q + 3 * p + 3 * q) / 3.0 for p, q in weights]
    )
    cubic = np.array(
        [
            float((p - q) * (2 * p + q + 3) * (p + 2 * q + 3)) / 18.0
            for p, q in weights
        ]
    )
    return quadratic, cubic


def joint_casimir_defect(matrix: np.ndarray, weights: tuple[Weight, ...]) -> float:
    quadratic, cubic = casimir_labels(weights)
    delta_quadratic = quadratic[:, None] - quadratic[None, :]
    delta_cubic = cubic[:, None] - cubic[None, :]
    return float(
        np.sum((delta_quadratic**2 + delta_cubic**2) * np.abs(matrix) ** 2)
    )


def joint_casimir_control(weights: tuple[Weight, ...]) -> tuple[bool, float, float]:
    quadratic, cubic = casimir_labels(weights)
    labels = set(zip(quadratic.tolist(), cubic.tolist(), strict=True))
    diagonal = np.diag(np.arange(1.0, len(weights) + 1.0))
    witness = diagonal.copy()
    witness[0, -1] = witness[-1, 0] = 0.125
    return (
        len(labels) == len(weights),
        joint_casimir_defect(diagonal, weights),
        joint_casimir_defect(witness, weights),
    )


def largest_discrepancy(
    analysis: PredictiveAnalysis, weights: tuple[Weight, ...]
) -> str:
    vector = base.matrix_vector(analysis.residual)
    errors = np.sqrt(np.clip(np.diag(analysis.coordinate_covariance), 0.0, None))
    usable = errors > 1.0e-14
    ratios = np.full(len(vector), -math.inf)
    ratios[usable] = np.abs(vector[usable]) / errors[usable]
    position = int(np.argmax(ratios))
    size = len(weights)
    component = "Re" if position < size * size else "Im"
    flat = position % (size * size)
    row, column = divmod(flat, size)
    measured = (
        analysis.measured[row, column].real
        if component == "Re"
        else analysis.measured[row, column].imag
    )
    modeled = (
        analysis.modeled[row, column].real
        if component == "Re"
        else analysis.modeled[row, column].imag
    )
    return (
        f"{component} C[{weights[row]},{weights[column]}]: "
        f"measured/model={measured:+.6f}/{modeled:+.6f}; "
        f"SE={errors[position]:.2e}; z={ratios[position]:.2f}"
    )


def print_analysis(
    label: str,
    analysis: PredictiveAnalysis,
    weights: tuple[Weight, ...],
    *,
    detail: bool = False,
) -> None:
    metric = analysis.metric
    print(
        f"{label}: rank={metric.rank}/{metric.dimension}; "
        f"chi2={metric.chi_square:.2f}; p={metric.p_value:.3g}; "
        f"maxz={metric.max_studentized:.2f}"
    )
    if detail:
        print(f"  largest: {largest_discrepancy(analysis, weights)}")


def main() -> int:
    config = resolve_config(parse_args())
    reporter = base.Reporter()
    certifying_protocol = False
    mode = "BURNED-SEED DIAGNOSTIC / NON-CERTIFYING"
    source_weights = tuple(base.weights_box(AUXILIARY_NMAX))
    target_weights = tuple(base.weights_box(TARGET_NMAX))
    train_seeds = PILOT_TRAIN_SEEDS if config.pilot else TRAIN_SEEDS
    validation_seeds = (
        PILOT_VALIDATION_SEEDS if config.pilot else VALIDATION_SEEDS
    )
    coefficient_lookup = {
        weight: base.wilson_character_coefficient(*weight, base.BETA)
        for weight in source_weights
    }
    operators = {
        nmax: base.build_operators(nmax, coefficient_lookup)
        for nmax in range(TARGET_NMAX, AUXILIARY_NMAX + 1)
    }
    polynomial_operators = {
        parameter: polynomial_operator(parameter)
        for parameter in DEFORMATION_PARAMETERS
    }

    print("GENERAL TWO-SLICE MIDDLE OPERATOR FROM A COMMON WILSON INTEGRAL")
    print(
        f"mode={mode}; beta={base.BETA:g}; B_{AUXILIARY_NMAX}->B_{TARGET_NMAX}; "
        f"four train + four validation chains; therm={config.therm}; "
        f"measure={config.measure}; every={config.sample_every}; "
        f"blocks/chain={config.blocks_per_chain}"
    )

    print("Implementation controls")
    local_error, action_mutation = base.local_delta_control()
    reporter.check(
        "81+81+81 action and local Metropolis delta",
        local_error < 1.0e-11 and action_mutation > 1.0e-6,
        f"delta/mutation={local_error:.2e}/{action_mutation:.2e}",
    )
    deletion_error, deletion_mutation = deletion_weight_control()
    reporter.check(
        "two marked spatial half-weights are deleted with beta/6",
        deletion_error < 1.0e-14 and deletion_mutation > 1.0e-3,
        f"identity/mutation={deletion_error:.1e}/{deletion_mutation:.2e}",
    )
    orientation_error, orientation_mutation = base.orientation_control(target_weights)
    reporter.check(
        "outgoing character carries the conjugate orientation",
        orientation_error < 1.0e-12 and orientation_mutation > 1.0e-6,
        f"correct/mutated={orientation_error:.1e}/{orientation_mutation:.1e}",
    )
    synthetic_error, synthetic_diagonal_gap = synthetic_control(operators[2])
    reporter.check(
        "general forward map preserves an off-diagonal synthetic middle operator",
        synthetic_error < 1.0e-13 and synthetic_diagonal_gap > 1.0e-5,
        f"repeat/diagonal gap={synthetic_error:.1e}/{synthetic_diagonal_gap:.2e}",
    )
    polynomial_pointwise_controls = {
        parameter: polynomial_pointwise_forward_control(parameter, target_weights)
        for parameter in DEFORMATION_PARAMETERS
    }
    reporter.check(
        "degree-one common-integral forward identities hold pointwise",
        all(
            error < 1.0e-11 and mutation > 1.0e-5
            for error, mutation in polynomial_pointwise_controls.values()
        ),
        "controls="
        + ",".join(
            f"a={parameter:+.1f}:err={error:.1e},mutation={mutation:.2e}"
            for parameter, (error, mutation) in polynomial_pointwise_controls.items()
        ),
    )
    basis_dimension = len(physical_coordinate_basis(target_weights))
    complement_dimension = len(symmetry_complement_basis(target_weights))
    reporter.check(
        "exact B_1 physical/complement dimensions are 6/9",
        basis_dimension == 6 and complement_dimension == 9,
        f"dimensions={basis_dimension}/{complement_dimension}",
    )
    (
        convolution_error,
        witness_minimum,
        witness_symmetry_error,
        witness_off_diagonal,
    ) = finite_class_convolution_control(target_weights)
    reporter.check(
        "finite central convolution is exactly character-diagonal",
        convolution_error < 1.0e-14,
        f"Schur contraction error={convolution_error:.1e}",
    )
    reporter.check(
        "positivity, slice symmetry, and irrep swap do not force diagonality",
        witness_minimum > 0.0
        and witness_symmetry_error < 1.0e-14
        and witness_off_diagonal > 1.0,
        f"min eigenvalue/symmetry error/offdiag="
        f"{witness_minimum:.1f}/{witness_symmetry_error:.1e}/{witness_off_diagonal:.3f}",
    )
    casimir_separates, diagonal_defect, mutation_defect = joint_casimir_control(
        source_weights
    )
    reporter.check(
        "joint quadratic/cubic Casimir defect vanishes exactly only on B_5 diagonals",
        casimir_separates and diagonal_defect == 0.0 and mutation_defect > 0.0,
        f"labels={len(source_weights)}; diagonal/mutation="
        f"{diagonal_defect:.1e}/{mutation_defect:.3e}",
    )
    reporter.check(
        "training and validation seeds are disjoint",
        len(train_seeds) == len(validation_seeds) == CHAINS_PER_ROLE
        and set(train_seeds).isdisjoint(validation_seeds),
    )
    reporter.check(
        "underpowered fresh-production certificate is disabled",
        config.pilot and not certifying_protocol,
        "diagnostic mode uses burned seeds and cannot certify",
    )
    polynomial_conditions = {
        parameter: operator.multiplier_condition
        for parameter, operator in polynomial_operators.items()
    }
    polynomial_weight_minima = {
        parameter: min(1.0 - 0.5 * parameter, 1.0 + parameter)
        for parameter in DEFORMATION_PARAMETERS
    }
    reporter.check(
        "degree-one sources stay positive, close B_1 into B_2, and are conditioned",
        all(condition < 6.0 for condition in polynomial_conditions.values())
        and all(value >= 0.10 - 1.0e-12 for value in polynomial_weight_minima.values()),
        "conditions="
        + ",".join(
            f"a={parameter:+.1f}:{condition:.3f},gmin={polynomial_weight_minima[parameter]:.2f}"
            for parameter, condition in polynomial_conditions.items()
        ),
    )
    jacobian_ranks = {
        "exp_general": forward_jacobian_rank(
            operators[AUXILIARY_NMAX], target_weights, diagonal_only=False
        ),
        "exp_diagonal": forward_jacobian_rank(
            operators[AUXILIARY_NMAX], target_weights, diagonal_only=True
        ),
        "poly_general": forward_jacobian_rank(
            polynomial_operators[DEFORMATION_PARAMETERS[0]],
            target_weights,
            diagonal_only=False,
        ),
        "poly_diagonal": forward_jacobian_rank(
            polynomial_operators[DEFORMATION_PARAMETERS[0]],
            target_weights,
            diagonal_only=True,
        ),
    }
    reporter.check(
        "forward Jacobians have the declared B_1 image ranks",
        jacobian_ranks
        == {
            "exp_general": 6,
            "exp_diagonal": 6,
            "poly_general": 6,
            "poly_diagonal": 4,
        },
        f"ranks={jacobian_ranks}",
    )
    polynomial_null_controls = {}
    for parameter in DEFORMATION_PARAMETERS:
        design = polynomial_diagonal_design(parameter, target_weights)
        null_basis = polynomial_diagonal_null_basis(parameter, target_weights)
        polynomial_null_controls[parameter] = (
            int(np.linalg.matrix_rank(design, tol=1.0e-10)),
            null_basis.shape,
            float(np.max(np.abs(null_basis @ design))),
        )
    reporter.check(
        "each exact polynomial diagonal image has a fixed two-dimensional null",
        len(physical_unnormalized_basis(target_weights)) == 7
        and all(
            rank == 5 and shape == (2, 7) and error < 1.0e-12
            for rank, shape, error in polynomial_null_controls.values()
        ),
        "controls="
        + ",".join(
            f"a={parameter:+.1f}:rank={rank},null={shape[0]},err={error:.1e}"
            for parameter, (rank, shape, error) in polynomial_null_controls.items()
        ),
    )
    print(
        "Parameter scope: normalized B_5 Q general/diagonal=350/20; "
        "held-out B_1 image=6."
    )

    start = time.perf_counter()
    train_chains = [
        run_common_integral_chain(
            seed,
            "cold" if chain % 2 == 0 else "hot",
            config.therm,
            config.measure,
            config.sample_every,
            source_weights,
        )
        for chain, seed in enumerate(train_seeds)
    ]
    train_elapsed = time.perf_counter() - start
    start = time.perf_counter()
    validation_chains = [
        run_common_integral_chain(
            seed,
            "hot" if chain % 2 == 0 else "cold",
            config.therm,
            config.measure,
            config.sample_every,
            source_weights,
        )
        for chain, seed in enumerate(validation_seeds)
    ]
    validation_elapsed = time.perf_counter() - start

    train_middle_blocks = base.block_means(
        [chain.middle_samples for chain in train_chains], config.blocks_per_chain
    )
    train_full_blocks = base.block_means(
        [chain.full_samples for chain in train_chains], config.blocks_per_chain
    )
    validation_middle_blocks = base.block_means(
        [chain.middle_samples for chain in validation_chains], config.blocks_per_chain
    )
    validation_full_blocks = base.block_means(
        [chain.full_samples for chain in validation_chains], config.blocks_per_chain
    )
    train_deformed_blocks = base.block_means(
        [chain.deformed_samples for chain in train_chains], config.blocks_per_chain
    )
    validation_deformed_blocks = base.block_means(
        [chain.deformed_samples for chain in validation_chains],
        config.blocks_per_chain,
    )
    all_deformed_blocks = np.concatenate(
        (train_deformed_blocks, validation_deformed_blocks), axis=0
    )
    polynomial_null = polynomial_null_analysis(all_deformed_blocks, target_weights)

    all_chains = train_chains + validation_chains
    acceptance = np.array([chain.acceptance for chain in all_chains])
    block_size = min(len(chain.full_samples) for chain in all_chains) // config.blocks_per_chain
    full_tau = base.maximum_ratio_autocorrelation(
        [chain.full_samples for chain in all_chains], source_weights, target_weights
    )
    middle_tau = base.maximum_ratio_autocorrelation(
        [chain.middle_samples for chain in all_chains], source_weights, target_weights
    )
    general_influence_samples = forward_influence_samples(
        all_chains,
        source_weights,
        operators[AUXILIARY_NMAX],
        target_weights,
        diagonal_only=False,
    )
    diagonal_influence_samples = forward_influence_samples(
        all_chains,
        source_weights,
        operators[AUXILIARY_NMAX],
        target_weights,
        diagonal_only=True,
    )
    general_influence_tau = base.maximum_ratio_autocorrelation(
        general_influence_samples, target_weights, target_weights
    )
    diagonal_influence_tau = base.maximum_ratio_autocorrelation(
        diagonal_influence_samples, target_weights, target_weights
    )
    polynomial_null_samples = [
        np.array(
            [
                polynomial_null_contrast_vector(sample, target_weights)
                for sample in chain.deformed_samples
            ]
        )
        for chain in all_chains
    ]
    polynomial_null_tau = maximum_vector_autocorrelation(polynomial_null_samples)
    maximum_tau = max(
        full_tau,
        middle_tau,
        general_influence_tau,
        diagonal_influence_tau,
        polynomial_null_tau,
    )
    ess_fractions = []
    for chain in all_chains:
        weights = chain.inverse_pair_weights
        ess_fractions.append(float(np.sum(weights) ** 2 / np.sum(weights**2) / len(weights)))
    minimum_ess_fraction = min(ess_fractions)
    deformed_ess_fractions = {
        parameter: min(
            float(
                np.sum(chain.deformed_samples[:, position, 0, 0].real) ** 2
                / np.sum(chain.deformed_samples[:, position, 0, 0].real**2)
                / len(chain.deformed_samples)
            )
            for chain in all_chains
        )
        for position, parameter in enumerate(DEFORMATION_PARAMETERS)
    }
    minimum_deformed_ess_fraction = min(deformed_ess_fractions.values())
    denominator_diagnostics = {
        "train_Q": scalar_denominator_diagnostics(
            [chain.middle_samples[:, 0, 0].real for chain in train_chains],
            train_middle_blocks[:, 0, 0].real,
        ),
        "validation_Q": scalar_denominator_diagnostics(
            [chain.middle_samples[:, 0, 0].real for chain in validation_chains],
            validation_middle_blocks[:, 0, 0].real,
        ),
    }
    for position, parameter in enumerate(DEFORMATION_PARAMETERS):
        denominator_diagnostics[f"validation_g{parameter:+.1f}"] = (
            scalar_denominator_diagnostics(
                [
                    chain.deformed_samples[:, position, 0, 0].real
                    for chain in validation_chains
                ],
                validation_deformed_blocks[:, position, 0, 0].real,
            )
        )
    denominator_ok = all(
        minimum > 0.0
        and relative_error < MAX_DENOMINATOR_RELATIVE_SE
        and chain_z < MAX_CHAIN_DEVIATION_SE
        for minimum, relative_error, chain_z in denominator_diagnostics.values()
    )
    finite = all(
        np.all(np.isfinite(array.real)) and np.all(np.isfinite(array.imag))
        for array in (
            train_middle_blocks,
            train_full_blocks,
            train_deformed_blocks,
            validation_middle_blocks,
            validation_full_blocks,
            validation_deformed_blocks,
        )
    )
    print("Sampling health")
    print(
        f"  train/validation elapsed={train_elapsed:.1f}/{validation_elapsed:.1f}s; "
        f"acceptance={acceptance.min():.3f}..{acceptance.max():.3f}; "
        f"block/tau_full/tau_Q/tau_forward/tau_diag/tau_poly="
        f"{block_size}/{full_tau:.2f}/{middle_tau:.2f}/"
        f"{general_influence_tau:.2f}/{diagonal_influence_tau:.2f}/"
        f"{polynomial_null_tau:.2f}"
    )
    print(
        f"  <P_space>={np.mean([np.mean(c.spatial_plaquettes) for c in all_chains]):.5f}; "
        f"<P_mix>={np.mean([np.mean(c.mixed_plaquettes) for c in all_chains]):.5f}; "
        f"<inverse marked pair>="
        f"{np.mean([np.mean(c.inverse_pair_weights) for c in all_chains]):.5f}; "
        f"min ESS Q/poly={minimum_ess_fraction:.3f}/"
        f"{minimum_deformed_ess_fraction:.3f}"
    )
    reporter.check(
        "eight burned diagnostic chains are finite with nondegenerate acceptance",
        finite
        and np.all((acceptance > 0.25) & (acceptance < 0.80)),
        f"blocks={len(train_middle_blocks)}/{len(validation_full_blocks)}; "
        f"block/max_tau={block_size}/{maximum_tau:.2f}; "
        f"min ESS={minimum_ess_fraction:.3f}/"
        f"{minimum_deformed_ess_fraction:.3f}",
    )
    reporter.check(
        "all ratio normalizations are positive and statistically stable",
        denominator_ok,
    )

    pointwise_antiunitary_error = max(
        antiunitary_sample_error(samples, source_weights, target_weights)
        for samples in (
            *(chain.middle_samples for chain in all_chains),
            *(chain.full_samples for chain in all_chains),
        )
    )
    symmetry_metrics = {
        "train_Q": symmetry_complement_metric(
            train_middle_blocks, source_weights, target_weights
        ),
        "validation_Q": symmetry_complement_metric(
            validation_middle_blocks, source_weights, target_weights
        ),
        "train_C": symmetry_complement_metric(
            train_full_blocks, source_weights, target_weights
        ),
        "validation_C": symmetry_complement_metric(
            validation_full_blocks, source_weights, target_weights
        ),
    }
    symmetry_joint = symmetry_joint_analysis(
        train_middle_blocks,
        train_full_blocks,
        validation_middle_blocks,
        validation_full_blocks,
        source_weights,
        target_weights,
    )
    expected_symmetry_joint_rank = min(
        2 * complement_dimension, len(train_middle_blocks) - 1
    ) + min(2 * complement_dimension, len(validation_middle_blocks) - 1)
    symmetry_surface_ok = (
        pointwise_antiunitary_error < 1.0e-12
        and symmetry_joint.metric.psd
        and symmetry_joint.metric.rank == expected_symmetry_joint_rank
        and symmetry_joint.metric.dimension == 36
        and (config.pilot or symmetry_joint.metric.null_residual < 1.0e-8)
        and all(
            metric.psd
            and metric.rank == metric.dimension == complement_dimension
            and metric.null_residual < 1.0e-8
            and metric.max_studentized < MAX_CHAIN_DEVIATION_SE
            for metric in symmetry_metrics.values()
        )
    )
    reporter.check(
        "raw exact-symmetry complements have fixed rank and no five-SE excursion",
        symmetry_surface_ok,
    )
    symmetry_ok = symmetry_surface_ok

    fold_a = predictive_analysis(
        train_middle_blocks,
        validation_full_blocks,
        source_weights,
        operators[AUXILIARY_NMAX],
        target_weights,
    )
    fold_b = predictive_analysis(
        validation_middle_blocks,
        train_full_blocks,
        source_weights,
        operators[AUXILIARY_NMAX],
        target_weights,
    )
    diagonal_a = predictive_analysis(
        train_middle_blocks,
        validation_full_blocks,
        source_weights,
        operators[AUXILIARY_NMAX],
        target_weights,
        diagonal_only=True,
    )
    paired_a = paired_analysis(
        train_middle_blocks,
        train_full_blocks,
        source_weights,
        operators[AUXILIARY_NMAX],
        target_weights,
    )
    paired_b = paired_analysis(
        validation_middle_blocks,
        validation_full_blocks,
        source_weights,
        operators[AUXILIARY_NMAX],
        target_weights,
    )
    polynomial_analyses = {
        parameter: predictive_analysis(
            train_middle_blocks,
            validation_deformed_blocks[:, position],
            source_weights,
            polynomial_operators[parameter],
            target_weights,
            validation_weights=target_weights,
        )
        for position, parameter in enumerate(DEFORMATION_PARAMETERS)
    }
    polynomial_diagonal_analyses = {
        parameter: predictive_analysis(
            train_middle_blocks,
            validation_deformed_blocks[:, position],
            source_weights,
            polynomial_operators[parameter],
            target_weights,
            diagonal_only=True,
            validation_weights=target_weights,
        )
        for position, parameter in enumerate(DEFORMATION_PARAMETERS)
    }
    structural_families = (
        "general",
        "diagonal",
        "perron_plus",
        "perron_plus_minus",
    )
    structural_analyses = {
        family: structural_analysis(
            train_middle_blocks,
            validation_middle_blocks,
            source_weights,
            target_weights,
            family,
        )
        for family in structural_families
    }
    joint_general = stack_predictive_analyses(
        (fold_a, *tuple(polynomial_analyses.values())), target_weights
    )
    joint_diagonal = stack_predictive_analyses(
        (diagonal_a, *tuple(polynomial_diagonal_analyses.values())),
        target_weights,
    )

    train_general_chain_models = [
        forward_target(
            normalized_physical(
                base.submatrix(
                    np.mean(chain.middle_samples, axis=0),
                    source_weights,
                    operators[AUXILIARY_NMAX].weights,
                ),
                operators[AUXILIARY_NMAX].weights,
            ),
            operators[AUXILIARY_NMAX],
            target_weights,
        )
        for chain in train_chains
    ]
    train_diagonal_chain_models = [
        forward_target(
            normalized_physical(
                base.submatrix(
                    np.mean(chain.middle_samples, axis=0),
                    source_weights,
                    operators[AUXILIARY_NMAX].weights,
                ),
                operators[AUXILIARY_NMAX].weights,
            ),
            operators[AUXILIARY_NMAX],
            target_weights,
            diagonal_only=True,
        )
        for chain in train_chains
    ]
    validation_chain_matrices = [
        normalized_physical(
            base.submatrix(
                np.mean(chain.full_samples, axis=0), source_weights, target_weights
            ),
            target_weights,
        )
        for chain in validation_chains
    ]
    train_general_z = base.maximum_chain_deviation(
        train_general_chain_models,
        fold_a.modeled,
        base.jackknife_covariance(
            np.array(
                [base.matrix_vector(value) for value in fold_a.training_leave]
            )
        ),
    )
    train_diagonal_z = base.maximum_chain_deviation(
        train_diagonal_chain_models,
        diagonal_a.modeled,
        base.jackknife_covariance(
            np.array(
                [base.matrix_vector(value) for value in diagonal_a.training_leave]
            )
        ),
    )
    validation_z = base.maximum_chain_deviation(
        validation_chain_matrices,
        fold_a.measured,
        base.jackknife_covariance(
            np.array(
                [base.matrix_vector(value) for value in fold_a.validation_leave]
            )
        ),
    )
    polynomial_null_chain_z = maximum_vector_chain_deviation(
        [np.mean(samples, axis=0) for samples in polynomial_null_samples],
        polynomial_null.residual_vector,
        polynomial_null.covariance,
    )
    chain_health = (
        max(
            train_general_z,
            train_diagonal_z,
            validation_z,
            polynomial_null_chain_z,
        )
        < MAX_CHAIN_DEVIATION_SE
    )
    reporter.check(
        "hot/cold chain-deviation diagnostic is finite and non-gating",
        all(
            math.isfinite(value)
            for value in (
                train_general_z,
                train_diagonal_z,
                validation_z,
                polynomial_null_chain_z,
            )
        ),
        f"general/diagonal/validation={train_general_z:.2f}/"
        f"{train_diagonal_z:.2f}/{validation_z:.2f}; "
        f"poly={polynomial_null_chain_z:.2f} SE; "
        f"five-SE health={'PASS' if chain_health else 'WARN'}",
    )

    models_a = projected_models(
        train_middle_blocks, source_weights, operators, target_weights
    )
    models_b = projected_models(
        validation_middle_blocks, source_weights, operators, target_weights
    )
    drifts_a = {
        nmax: float(np.linalg.norm(models_a[nmax] - models_a[nmax - 1], ord="fro"))
        for nmax in range(2, AUXILIARY_NMAX + 1)
    }
    drifts_b = {
        nmax: float(np.linalg.norm(models_b[nmax] - models_b[nmax - 1], ord="fro"))
        for nmax in range(2, AUXILIARY_NMAX + 1)
    }
    last_shift_a = base.max_coordinate_z(
        models_a[AUXILIARY_NMAX] - models_a[AUXILIARY_NMAX - 1],
        fold_a.coordinate_covariance,
    )
    last_shift_b = base.max_coordinate_z(
        models_b[AUXILIARY_NMAX] - models_b[AUXILIARY_NMAX - 1],
        fold_b.coordinate_covariance,
    )
    print(
        f"Auxiliary B_{AUXILIARY_NMAX-1}->B_{AUXILIARY_NMAX} "
        f"shift/primary SE A/B={last_shift_a:.2f}/{last_shift_b:.2f}; "
        f"raw drift={drifts_a[AUXILIARY_NMAX]:.2e}/"
        f"{drifts_b[AUXILIARY_NMAX]:.2e}"
    )

    print_analysis(
        "Primary fold A: train Q -> held-out validation C",
        fold_a,
        target_weights,
        detail=True,
    )
    print_analysis("Role-swapped fold B: validation Q -> held-out train C", fold_b, target_weights)
    print_analysis(
        "Paired train-chain implementation/truncation control",
        paired_a,
        target_weights,
    )
    print_analysis(
        "Paired validation-chain implementation/truncation control",
        paired_b,
        target_weights,
    )
    print_analysis(
        "Diagonal-Q diagnostic on primary fold A",
        diagonal_a,
        target_weights,
        detail=True,
    )
    for parameter in DEFORMATION_PARAMETERS:
        print_analysis(
            f"Exact polynomial holdout a={parameter:+.1f}: general Q_B2",
            polynomial_analyses[parameter],
            target_weights,
        )
        print_analysis(
            f"Exact polynomial holdout a={parameter:+.1f}: diagonal Q_B2 diagnostic",
            polynomial_diagonal_analyses[parameter],
            target_weights,
        )
    print("Joint exponential plus two exact polynomial holdouts")
    for label, joint in (("general Q", joint_general), ("diagonal Q", joint_diagonal)):
        metric = joint.metric
        print(
            f"  {label}: rank={metric.rank}/{metric.dimension}; "
            f"chi2={metric.chi_square:.2f}; p_asym={metric.p_value:.3g}; "
            f"maxz={metric.max_studentized:.2f}"
        )
    observed_improvement = float(
        np.dot(joint_diagonal.residual_vector, joint_diagonal.residual_vector)
        - np.dot(joint_general.residual_vector, joint_general.residual_vector)
    )
    print(
        f"  orthonormal loss improvement ||r_diag||^2-||r_general||^2="
        f"{observed_improvement:.6g}"
    )
    polynomial_errors = np.sqrt(
        np.clip(np.diag(polynomial_null.covariance), 0.0, None)
    )
    print("Exact polynomial diagonal-null discriminator")
    print(
        f"  rank={polynomial_null.metric.rank}/4; "
        f"T2={polynomial_null.metric.chi_square:.2f}; "
        f"maxz={polynomial_null.metric.max_studentized:.2f}; "
        f"contrasts={np.array2string(polynomial_null.residual_vector, precision=5)}; "
        f"SE={np.array2string(polynomial_errors, precision=4)}"
    )
    if config.pilot:
        print(
            "  [DIAG] no power extrapolation from this short burned-seed run; "
            "the former fresh protocol is disabled"
        )
    print("Independent B_1 middle-operator structure tournament")
    print(
        "  "
        + "; ".join(
            f"{family}:p={structural_analyses[family].metric.p_value:.3g},"
            f"maxz={structural_analyses[family].metric.max_studentized:.2f}"
            for family in structural_families
        )
    )

    q1 = normalized_physical(
        base.submatrix(np.mean(train_middle_blocks, axis=0), source_weights, target_weights),
        target_weights,
    )
    off_diagonal = q1 - np.diag(np.diag(q1))
    print("Measured shared-B_1 middle operator from train chains")
    print(
        "  Q=[1,b,b,c;b,a,e,f;b,e,a,f;c,f,f,d] with "
        f"b={q1[0,1].real:.6f}, c={q1[0,3].real:.6f}, "
        f"a={q1[1,1].real:.6f}, e={q1[1,2].real:.6f}, "
        f"f={q1[1,3].real:.6f}, d={q1[3,3].real:.6f}"
    )
    print(
        f"  ||offdiag(Q)||F/||Q||F={np.linalg.norm(off_diagonal)/np.linalg.norm(q1):.6f}; "
        f"min eigenvalue={np.min(np.linalg.eigvalsh(q1)):.6g}"
    )
    train_minimum, heldout_quadratic, heldout_error, heldout_z = heldout_minimum_direction(
        train_middle_blocks,
        validation_middle_blocks,
        source_weights,
        target_weights,
    )
    print(
        f"  train-selected minimum direction: lambda_train={train_minimum:.6g}; "
        f"heldout quadratic={heldout_quadratic:.6g} +/- {heldout_error:.3g} "
        f"({heldout_z:.2f} SE from zero)"
    )
    positivity_compatibility = heldout_z > -3.5
    reporter.check(
        "independent B_1 quadratic-form check does not contradict analytic positivity",
        positivity_compatibility,
        f"heldout z={heldout_z:.2f}",
    )

    paired_budget_a = base.max_coordinate_z(
        paired_a.residual, fold_a.coordinate_covariance
    )
    paired_budget_b = base.max_coordinate_z(
        paired_b.residual, fold_b.coordinate_covariance
    )
    separation_z = base.max_coordinate_z(
        diagonal_a.modeled - fold_a.modeled, fold_a.coordinate_covariance
    )
    cutoff_budget_ok = (
        last_shift_a < MAX_AUXILIARY_SHIFT_SE
        and last_shift_b < MAX_AUXILIARY_SHIFT_SE
        and max(paired_budget_a, paired_budget_b) < 0.25
        and max(last_shift_a, last_shift_b) < 0.25 * separation_z
    )
    print(
        f"Finite-cutoff error budget: paired residual/primary SE A/B="
        f"{paired_budget_a:.3f}/{paired_budget_b:.3f}; "
        f"general-vs-diagonal separation={separation_z:.2f} SE"
    )
    reporter.check(
        "B_5 exponential cutoff is subdominant to prediction noise and model separation",
        cutoff_budget_ok,
    )

    covariance_ok = all(
        analysis.metric.psd
        and analysis.metric.rank == analysis.metric.dimension == basis_dimension
        and analysis.metric.null_residual < 1.0e-8
        for analysis in (
            fold_a,
            fold_b,
            *polynomial_analyses.values(),
            structural_analyses["general"],
        )
    ) and all(
        joint.metric.psd
        and joint.metric.rank == joint.metric.dimension == 3 * basis_dimension
        and joint.metric.null_residual < 1.0e-8
        for joint in (joint_general, joint_diagonal)
    )
    reporter.check(
        "both cross-fitted physical covariance surfaces are full rank",
        covariance_ok,
        f"rank A/B={fold_a.metric.rank}/{fold_b.metric.rank}; "
        f"polynomial={[a.metric.rank for a in polynomial_analyses.values()]}; "
        f"dimension={basis_dimension}",
    )
    if config.pilot:
        smoke_polynomial_null = polynomial_null_block_bootstrap(
            all_deformed_blocks,
            target_weights,
            polynomial_null,
            config.blocks_per_chain,
            PILOT_BOOTSTRAP_REPLICATES,
        )
        smoke_symmetry = symmetry_joint_block_bootstrap(
            train_middle_blocks,
            train_full_blocks,
            validation_middle_blocks,
            validation_full_blocks,
            source_weights,
            target_weights,
            symmetry_joint,
            config.blocks_per_chain,
            PILOT_BOOTSTRAP_REPLICATES,
        )
        smoke_general = joint_block_bootstrap(
            train_middle_blocks,
            validation_full_blocks,
            validation_deformed_blocks,
            source_weights,
            operators[AUXILIARY_NMAX],
            polynomial_operators,
            target_weights,
            joint_general,
            config.blocks_per_chain,
            PILOT_BOOTSTRAP_REPLICATES,
            diagonal_only=False,
            seed_offset=0,
        )
        smoke_diagonal = joint_block_bootstrap(
            train_middle_blocks,
            validation_full_blocks,
            validation_deformed_blocks,
            source_weights,
            operators[AUXILIARY_NMAX],
            polynomial_operators,
            target_weights,
            joint_diagonal,
            config.blocks_per_chain,
            PILOT_BOOTSTRAP_REPLICATES,
            diagonal_only=True,
            seed_offset=1000,
        )
        smoke_improvement = improvement_block_bootstrap(
            train_middle_blocks,
            validation_full_blocks,
            validation_deformed_blocks,
            source_weights,
            operators[AUXILIARY_NMAX],
            polynomial_operators,
            target_weights,
            config.blocks_per_chain,
            PILOT_BOOTSTRAP_REPLICATES,
        )
        smoke_ok = (
            all(
                0 <= result[0] <= PILOT_BOOTSTRAP_REPLICATES
                for result in (
                    smoke_polynomial_null,
                    smoke_symmetry,
                    smoke_general,
                    smoke_diagonal,
                )
            )
            and all(math.isfinite(value) for value in smoke_improvement)
        )
        reporter.check(
            "stratified joint-bootstrap and paired-improvement paths execute",
            smoke_ok,
            f"smoke replicates={PILOT_BOOTSTRAP_REPLICATES}",
        )
        print("  [DIAG] pilot assigns no positive-law or diagonal-no-go PASS/FAIL")
    else:
        polynomial_null_bootstrap = polynomial_null_block_bootstrap(
            all_deformed_blocks,
            target_weights,
            polynomial_null,
            config.blocks_per_chain,
            BOOTSTRAP_REPLICATES,
        )
        symmetry_bootstrap = symmetry_joint_block_bootstrap(
            train_middle_blocks,
            train_full_blocks,
            validation_middle_blocks,
            validation_full_blocks,
            source_weights,
            target_weights,
            symmetry_joint,
            config.blocks_per_chain,
            BOOTSTRAP_REPLICATES,
        )
        general_bootstrap = joint_block_bootstrap(
            train_middle_blocks,
            validation_full_blocks,
            validation_deformed_blocks,
            source_weights,
            operators[AUXILIARY_NMAX],
            polynomial_operators,
            target_weights,
            joint_general,
            config.blocks_per_chain,
            BOOTSTRAP_REPLICATES,
            diagonal_only=False,
            seed_offset=0,
        )
        diagonal_bootstrap = joint_block_bootstrap(
            train_middle_blocks,
            validation_full_blocks,
            validation_deformed_blocks,
            source_weights,
            operators[AUXILIARY_NMAX],
            polynomial_operators,
            target_weights,
            joint_diagonal,
            config.blocks_per_chain,
            BOOTSTRAP_REPLICATES,
            diagonal_only=True,
            seed_offset=1000,
        )
        improvement_interval = improvement_block_bootstrap(
            train_middle_blocks,
            validation_full_blocks,
            validation_deformed_blocks,
            source_weights,
            operators[AUXILIARY_NMAX],
            polynomial_operators,
            target_weights,
            config.blocks_per_chain,
            BOOTSTRAP_REPLICATES,
        )
        print("Joint null-centered stratified bootstrap")
        for label, result in (
            ("polynomial diagonal-null", polynomial_null_bootstrap),
            ("exact-symmetry complement", symmetry_bootstrap),
            ("general Q", general_bootstrap),
            ("diagonal Q", diagonal_bootstrap),
        ):
            exceeded, rank_failures, p_value, lower_95, upper_95 = result
            print(
                f"  {label}: exceedances={exceeded}/{BOOTSTRAP_REPLICATES}; "
                f"rank_failures={rank_failures}; p={p_value:.6g}; "
                f"one-sided 95% bounds=[{lower_95:.6g},{upper_95:.6g}]"
            )
        print(
            "  predictive-improvement central 98% interval="
            f"[{improvement_interval[0]:.6g},{improvement_interval[2]:.6g}]; "
            f"median={improvement_interval[1]:.6g}; q01 is one-sided 99% lower"
        )
        null_exceeded, null_rank_failures, _, _, null_upper = (
            polynomial_null_bootstrap
        )
        general_exceeded, general_rank_failures, _, general_lower, _ = general_bootstrap
        diagonal_exceeded, diagonal_rank_failures, _, _, diagonal_upper = diagonal_bootstrap
        symmetry_exceeded, symmetry_rank_failures, _, symmetry_lower, _ = (
            symmetry_bootstrap
        )
        symmetry_ok = (
            symmetry_surface_ok
            and symmetry_rank_failures == 0
            and symmetry_exceeded > 0
            and symmetry_lower > SYMMETRY_COMPATIBILITY_FLOOR
        )
        reporter.check(
            "joint raw exact-symmetry complement is bootstrap-compatible",
            certifying_protocol and symmetry_ok,
            f"bootstrap lower={symmetry_lower:.6g} > "
            f"{SYMMETRY_COMPATIBILITY_FLOOR:g}",
        )
        reporter.check(
            "common-integral general-Q forward image is compatible with all held-out sources",
            certifying_protocol
            and chain_health
            and denominator_ok
            and symmetry_ok
            and covariance_ok
            and cutoff_budget_ok
            and positivity_compatibility
            and general_rank_failures == 0
            and general_exceeded > 0
            and general_lower > GENERAL_COMPATIBILITY_FLOOR,
            f"bootstrap lower={general_lower:.6g} > {GENERAL_COMPATIBILITY_FLOOR:g}",
        )
        reporter.check(
            "character-diagonal common-integral Q is rejected by exact polynomial nulls",
            certifying_protocol
            and chain_health
            and denominator_ok
            and symmetry_ok
            and covariance_ok
            and cutoff_budget_ok
            and polynomial_null.metric.rank == polynomial_null.metric.dimension == 4
            and null_exceeded == 0
            and null_rank_failures == 0
            and null_upper < DIAGONAL_REJECTION_CEILING,
            f"bootstrap upper={null_upper:.6g} < {DIAGONAL_REJECTION_CEILING:g}",
        )
        print(
            "  [DIAG] 18D diagonal bootstrap and paired raw-loss improvement are "
            f"corroborating only: diagonal upper={diagonal_upper:.6g}; "
            f"rank failures={diagonal_rank_failures}; "
            f"paired q01={improvement_interval[0]:.6g}"
        )

    print(
        "per_element: checked and executed - pointwise marked-weight cancellation "
        "and degree-one forward identities"
    )
    print(
        "per_site: checked and not executed - the burned diagnostic averages 81 "
        "faces and makes no site-resolved claim"
    )
    print(
        "per_mode: checked and executed - exact B_1 class-sector classification "
        "plus a non-certifying B_5 diagnostic"
    )
    print(
        "per_block: checked and executed - blocked burned-seed calculations test "
        "implementation paths only"
    )
    print(
        "lattice_wide: checked and not executed - no beta transport, volume law, "
        "or thermodynamic-limit claim is made"
    )
    print(f"TOTAL: PASS={reporter.passed} FAIL={reporter.failed}")
    return 0 if reporter.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
