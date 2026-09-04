#!/usr/bin/env python3
"""Actual full two-slice Wilson compression test on the L_s=3 torus.

The primary test is deliberately forward: a four-chain Monte Carlo estimate
of the full marked-face character matrix is compared, on the shared B_1
sector, with

    C_model = s M_beta D_beta^loc diag(rho_static) M_beta,

where ``s`` is fixed only by the trivial matrix entry.  ``rho_static`` comes
from independent, disjoint-seed marked-factor-deletion chains.  Both Monte
Carlo inputs are transformed inside their own leave-one-block jackknives and
their covariance contributions are added by independence.

The production character sampler uses B_2.  B_1 is its literal shared block;
it is not a separately sampled data set.  Auxiliary B_N forward models for
N=1,2,3,4 expose finite-box projection drift.  Direct algebraic stripping is
reported only as an ill-conditioned diagnostic and is never a physics gate.

``--pilot`` executes every sampler, transform, covariance, synthetic control,
and diagnostic with cheap statistics.  It is non-certifying: only a default
production run applies the forward physics gate.
"""

from __future__ import annotations

import argparse
import math
import time
from dataclasses import dataclass

import numpy as np
from scipy.linalg import expm
from scipy.stats import beta as beta_distribution
from scipy.stats import chi2

from frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization import (
    build_numeric_recurrence,
    symmetric_exponential,
    weights_box,
)
from frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_actual_l3 import (
    BETA,
    FACES,
    L,
    LINK_TO_FACES,
    all_face_traces,
    dim_su3,
    face_matrix,
    integrated_autocorrelation_time,
    metropolis_sweep,
    random_haar_su3,
    random_su2_subgroup_step,
    su3_character_from_trace,
    wilson_character_coefficient,
)


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_actual_l3.py",
    "scripts/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.py",
)

PRODUCTION_NMAX = 2
SHARED_NMAX = 1
AUXILIARY_NMAX = 4
CHAINS = 4
FULL_SEEDS = (82421, 82457, 82471, 82483)
STATIC_SEEDS = (83423, 83431, 83437, 83449)
PRIMARY_P_FLOOR = 1.0e-3
BOOTSTRAP_REPLICATES = 4096
BOOTSTRAP_SEED = 92507

Weight = tuple[int, int]


@dataclass(frozen=True)
class Config:
    pilot: bool
    nmax: int
    therm: int
    full_measure: int
    static_measure: int
    sample_every: int
    blocks_per_chain: int


@dataclass
class TwoSliceChain:
    seed: int
    initial: str
    acceptance: float
    epsilon: float
    samples: np.ndarray
    spatial_plaquettes: np.ndarray
    mixed_plaquettes: np.ndarray


@dataclass
class StaticChain:
    seed: int
    initial: str
    acceptance: float
    epsilon: float
    samples: np.ndarray
    plaquettes: np.ndarray


@dataclass(frozen=True)
class SectorOperators:
    nmax: int
    weights: tuple[Weight, ...]
    multiplier: np.ndarray
    inverse_multiplier: np.ndarray
    diagonal: np.ndarray
    multiplier_condition: float
    diagonal_condition: float


@dataclass(frozen=True)
class CovarianceMetric:
    rank: int
    dimension: int
    minimum_eigenvalue: float
    chi_square: float
    p_value: float
    max_studentized: float
    null_residual: float
    psd: bool


@dataclass(frozen=True)
class ForwardAnalysis:
    measured: np.ndarray
    rho: np.ndarray
    modeled: np.ndarray
    residual: np.ndarray
    covariance: np.ndarray
    coordinate_covariance: np.ndarray
    metric: CovarianceMetric
    full_leave: np.ndarray
    static_leave: np.ndarray


class Reporter:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f"; {detail}" if detail else ""
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}{suffix}")


def spatial_real_trace(slice_links: np.ndarray, face_id: int) -> float:
    return float(np.trace(face_matrix(slice_links, FACES[face_id])).real)


def mixed_real_trace(two_slice_links: np.ndarray, link_id: int) -> float:
    return float(
        np.trace(
            two_slice_links[1, link_id]
            @ two_slice_links[0, link_id].conj().T
        ).real
    )


def two_slice_log_weight(two_slice_links: np.ndarray, beta: float) -> float:
    spatial = sum(
        spatial_real_trace(two_slice_links[tau], face_id)
        for tau in range(2)
        for face_id in range(len(FACES))
    )
    mixed = sum(
        mixed_real_trace(two_slice_links, link_id)
        for link_id in range(3 * L**3)
    )
    return float((beta / 6.0) * spatial + (beta / 3.0) * mixed)


def two_slice_local_log_weight(
    two_slice_links: np.ndarray,
    tau: int,
    link_id: int,
    beta: float,
) -> float:
    """All action terms changed by one spatial-link proposal."""
    spatial = sum(
        spatial_real_trace(two_slice_links[tau], face_id)
        for face_id in LINK_TO_FACES[link_id]
    )
    return float(
        (beta / 6.0) * spatial
        + (beta / 3.0) * mixed_real_trace(two_slice_links, link_id)
    )


def two_slice_sweep(
    links: np.ndarray,
    rng: np.random.Generator,
    epsilon: float,
    beta: float,
) -> float:
    """One Metropolis sweep over all 81+81 spatial links."""
    nlinks = 3 * L**3
    accepted = 0
    for flat in rng.permutation(2 * nlinks):
        tau, link_id = divmod(int(flat), nlinks)
        old = links[tau, link_id].copy()
        old_local = two_slice_local_log_weight(links, tau, link_id, beta)

        links[tau, link_id] = random_su2_subgroup_step(rng, epsilon) @ old
        new_local = two_slice_local_log_weight(links, tau, link_id, beta)
        delta = float(new_local - old_local)
        if delta >= 0.0 or rng.random() < math.exp(delta):
            accepted += 1
        else:
            links[tau, link_id] = old
    return accepted / (2 * nlinks)


def character_table(traces: np.ndarray, weights: tuple[Weight, ...]) -> np.ndarray:
    return np.array(
        [
            [su3_character_from_trace(trace, p, q) for p, q in weights]
            for trace in traces
        ],
        dtype=complex,
    )


def character_cross_moment(
    incoming: np.ndarray, outgoing: np.ndarray
) -> np.ndarray:
    """Outgoing-conjugate cross moment used by the production sampler."""
    if incoming.shape != outgoing.shape or len(incoming) == 0:
        raise ValueError("incoming and outgoing character tables must align")
    return outgoing.conj().T @ incoming / len(incoming)


def two_slice_character_matrix(
    links: np.ndarray, weights: tuple[Weight, ...]
) -> np.ndarray:
    incoming = character_table(all_face_traces(links[0]), weights)
    outgoing = character_table(all_face_traces(links[1]), weights)
    return character_cross_moment(incoming, outgoing)


def static_marked_deletion_observable(
    traces: np.ndarray, weights: tuple[Weight, ...], beta: float
) -> np.ndarray:
    inverse_marked_weight = np.exp(-(beta / 3.0) * traces.real)
    characters = character_table(traces, weights)
    dimensions = np.array([dim_su3(p, q) for p, q in weights], dtype=float)
    return np.mean(inverse_marked_weight[:, None] * characters.conj(), axis=0) / dimensions


def initial_links(
    rng: np.random.Generator, initial: str, slices: int
) -> np.ndarray:
    nlinks = 3 * L**3
    if initial == "cold":
        if slices == 1:
            return np.tile(np.eye(3, dtype=complex), (nlinks, 1, 1))
        return np.tile(np.eye(3, dtype=complex), (slices, nlinks, 1, 1))
    if slices == 1:
        return np.array([random_haar_su3(rng) for _ in range(nlinks)])
    return np.array(
        [[random_haar_su3(rng) for _ in range(nlinks)] for _ in range(slices)]
    )


def adapted_epsilon(epsilon: float, acceptance: float) -> float:
    if acceptance > 0.62:
        epsilon *= 1.05
    elif acceptance < 0.42:
        epsilon *= 0.95
    return float(np.clip(epsilon, 0.06, 1.2))


def run_two_slice_chain(
    seed: int,
    initial: str,
    therm: int,
    measure: int,
    sample_every: int,
    weights: tuple[Weight, ...],
) -> TwoSliceChain:
    rng = np.random.default_rng(seed)
    links = initial_links(rng, initial, slices=2)
    epsilon = 0.32
    for sweep in range(therm):
        acceptance = two_slice_sweep(links, rng, epsilon, BETA)
        if (sweep + 1) % 25 == 0:
            epsilon = adapted_epsilon(epsilon, acceptance)

    samples: list[np.ndarray] = []
    spatial_plaquettes: list[float] = []
    mixed_plaquettes: list[float] = []
    acceptances: list[float] = []
    for sweep in range(measure):
        acceptances.append(two_slice_sweep(links, rng, epsilon, BETA))
        if (sweep + 1) % sample_every == 0:
            traces0 = all_face_traces(links[0])
            traces1 = all_face_traces(links[1])
            incoming = character_table(traces0, weights)
            outgoing = character_table(traces1, weights)
            samples.append(character_cross_moment(incoming, outgoing))
            spatial_plaquettes.append(
                float(np.mean(np.concatenate((traces0.real, traces1.real))) / 3.0)
            )
            mixed_plaquettes.append(
                float(
                    np.mean(
                        [mixed_real_trace(links, link_id) for link_id in range(3 * L**3)]
                    )
                    / 3.0
                )
            )
    return TwoSliceChain(
        seed=seed,
        initial=initial,
        acceptance=float(np.mean(acceptances)),
        epsilon=epsilon,
        samples=np.array(samples),
        spatial_plaquettes=np.array(spatial_plaquettes),
        mixed_plaquettes=np.array(mixed_plaquettes),
    )


def run_static_chain(
    seed: int,
    initial: str,
    therm: int,
    measure: int,
    sample_every: int,
    weights: tuple[Weight, ...],
) -> StaticChain:
    rng = np.random.default_rng(seed)
    links = initial_links(rng, initial, slices=1)
    epsilon = 0.32
    for sweep in range(therm):
        acceptance = metropolis_sweep(links, rng, epsilon, BETA)
        if (sweep + 1) % 25 == 0:
            epsilon = adapted_epsilon(epsilon, acceptance)

    samples: list[np.ndarray] = []
    plaquettes: list[float] = []
    acceptances: list[float] = []
    for sweep in range(measure):
        acceptances.append(metropolis_sweep(links, rng, epsilon, BETA))
        if (sweep + 1) % sample_every == 0:
            traces = all_face_traces(links)
            samples.append(static_marked_deletion_observable(traces, weights, BETA))
            plaquettes.append(float(np.mean(traces.real) / 3.0))
    return StaticChain(
        seed=seed,
        initial=initial,
        acceptance=float(np.mean(acceptances)),
        epsilon=epsilon,
        samples=np.array(samples),
        plaquettes=np.array(plaquettes),
    )


def block_means(sample_arrays: list[np.ndarray], blocks_per_chain: int) -> np.ndarray:
    blocks: list[np.ndarray] = []
    for samples in sample_arrays:
        block_size = len(samples) // blocks_per_chain
        if block_size < 2:
            raise ValueError("each chain needs at least two samples per block")
        for block in range(blocks_per_chain):
            lo = block * block_size
            hi = len(samples) if block == blocks_per_chain - 1 else (block + 1) * block_size
            blocks.append(np.mean(samples[lo:hi], axis=0))
    return np.array(blocks)


def leave_one_means(blocks: np.ndarray) -> np.ndarray:
    if len(blocks) < 3:
        raise ValueError("at least three blocks are required")
    total = np.sum(blocks, axis=0)
    return np.array([(total - block) / (len(blocks) - 1) for block in blocks])


def normalize_matrix(matrix: np.ndarray) -> np.ndarray:
    if abs(matrix[0, 0]) < 1.0e-14:
        raise ValueError("trivial matrix entry is numerically zero")
    return matrix / matrix[0, 0]


def normalize_rho(vector: np.ndarray) -> np.ndarray:
    if abs(vector[0]) < 1.0e-14:
        raise ValueError("trivial static channel is numerically zero")
    return vector / vector[0]


def charge_conjugation_project_rho(
    vector: np.ndarray, weights: tuple[Weight, ...]
) -> np.ndarray:
    """Project the static estimate onto its exact real conjugation symmetry."""
    index = {weight: i for i, weight in enumerate(weights)}
    projected = np.zeros(len(weights), dtype=complex)
    for i, (p, q) in enumerate(weights):
        j = index[(q, p)]
        value = 0.5 * (vector[i].real + vector[j].real)
        projected[i] = value
        projected[j] = value
    return projected


def subvector(
    vector: np.ndarray,
    source_weights: tuple[Weight, ...],
    target_weights: tuple[Weight, ...],
) -> np.ndarray:
    index = {weight: i for i, weight in enumerate(source_weights)}
    return vector[[index[weight] for weight in target_weights]]


def submatrix(
    matrix: np.ndarray,
    source_weights: tuple[Weight, ...],
    target_weights: tuple[Weight, ...],
) -> np.ndarray:
    index = {weight: i for i, weight in enumerate(source_weights)}
    positions = [index[weight] for weight in target_weights]
    return matrix[np.ix_(positions, positions)]


def build_operators(
    nmax: int, coefficient_lookup: dict[Weight, float]
) -> SectorOperators:
    recurrence, weights_list, _ = build_numeric_recurrence(nmax)
    weights = tuple(weights_list)
    multiplier = symmetric_exponential(recurrence, BETA / 2.0)
    inverse_multiplier = symmetric_exponential(recurrence, -BETA / 2.0)
    c00 = coefficient_lookup[(0, 0)]
    link_eigenvalues = np.array(
        [
            coefficient_lookup[(p, q)] / (dim_su3(p, q) * c00)
            for p, q in weights
        ],
        dtype=float,
    )
    diagonal = np.diag(link_eigenvalues**4)
    return SectorOperators(
        nmax=nmax,
        weights=weights,
        multiplier=multiplier,
        inverse_multiplier=inverse_multiplier,
        diagonal=diagonal,
        multiplier_condition=float(np.linalg.cond(multiplier)),
        diagonal_condition=float(np.linalg.cond(diagonal)),
    )


def forward_model(rho: np.ndarray, operators: SectorOperators) -> np.ndarray:
    raw = (
        operators.multiplier
        @ operators.diagonal
        @ np.diag(rho)
        @ operators.multiplier
    )
    return normalize_matrix(raw)


def direct_strip(matrix: np.ndarray, operators: SectorOperators) -> np.ndarray:
    """Numerically fragile inverse, used only in explicit diagnostics."""
    inverse_diagonal = np.diag(1.0 / np.diag(operators.diagonal))
    stripped = (
        inverse_diagonal
        @ operators.inverse_multiplier
        @ matrix
        @ operators.inverse_multiplier
    )
    return normalize_matrix(stripped)


def matrix_vector(matrix: np.ndarray) -> np.ndarray:
    return np.concatenate((matrix.real.ravel(), matrix.imag.ravel()))


def symmetry_vector(matrix: np.ndarray, weights: tuple[Weight, ...]) -> np.ndarray:
    """Independent real coordinates for C_bar(lambda),bar(mu)=conj(C_lambda,mu)."""
    index = {weight: i for i, weight in enumerate(weights)}
    values: list[float] = []
    size = len(weights)
    for row, (p_row, q_row) in enumerate(weights):
        for column, (p_column, q_column) in enumerate(weights):
            partner_row = index[(q_row, p_row)]
            partner_column = index[(q_column, p_column)]
            flat = row * size + column
            partner_flat = partner_row * size + partner_column
            if flat > partner_flat:
                continue
            if flat == partner_flat:
                if row != 0 or column != 0:
                    values.append(float(matrix[row, column].real))
            else:
                values.extend(
                    (float(matrix[row, column].real), float(matrix[row, column].imag))
                )
    return np.array(values, dtype=float)


def jackknife_covariance(vectors: np.ndarray) -> np.ndarray:
    center = np.mean(vectors, axis=0)
    deviations = vectors - center
    return (len(vectors) - 1) / len(vectors) * deviations.T @ deviations


def covariance_metric(vector: np.ndarray, covariance: np.ndarray) -> CovarianceMetric:
    symmetric_covariance = 0.5 * (covariance + covariance.T)
    eigenvalues, eigenvectors = np.linalg.eigh(symmetric_covariance)
    max_eigenvalue = max(float(np.max(eigenvalues)), 0.0)
    tolerance = max(1.0e-18, max_eigenvalue * 1.0e-10)
    supported = eigenvalues > tolerance
    rank = int(np.count_nonzero(supported))
    if rank:
        projections = eigenvectors[:, supported].T @ vector
        statistic = float(np.sum(projections**2 / eigenvalues[supported]))
        p_value = float(chi2.sf(statistic, rank))
    else:
        statistic = math.inf
        p_value = 0.0
    null_projection = eigenvectors[:, ~supported].T @ vector
    null_residual = float(np.linalg.norm(null_projection))
    errors = np.sqrt(np.clip(np.diag(symmetric_covariance), 0.0, None))
    usable = errors > math.sqrt(tolerance)
    max_studentized = (
        float(np.max(np.abs(vector[usable]) / errors[usable]))
        if np.any(usable)
        else math.inf
    )
    psd_tolerance = max(1.0e-16, max_eigenvalue * 1.0e-9)
    return CovarianceMetric(
        rank=rank,
        dimension=len(vector),
        minimum_eigenvalue=float(np.min(eigenvalues)),
        chi_square=statistic,
        p_value=p_value,
        max_studentized=max_studentized,
        null_residual=null_residual,
        psd=bool(np.min(eigenvalues) >= -psd_tolerance),
    )


def forward_analysis(
    full_blocks: np.ndarray,
    full_weights: tuple[Weight, ...],
    static_blocks: np.ndarray,
    static_weights: tuple[Weight, ...],
    operators: SectorOperators,
    measurement_weights: tuple[Weight, ...] | None = None,
) -> ForwardAnalysis:
    model_weights = operators.weights
    target_weights = model_weights if measurement_weights is None else measurement_weights
    measured = normalize_matrix(
        submatrix(np.mean(full_blocks, axis=0), full_weights, target_weights)
    )
    rho = charge_conjugation_project_rho(
        normalize_rho(
            subvector(np.mean(static_blocks, axis=0), static_weights, model_weights)
        ),
        model_weights,
    )
    modeled = submatrix(
        forward_model(rho, operators), model_weights, target_weights
    )
    residual = measured - modeled

    full_leave = np.array(
        [
            normalize_matrix(submatrix(mean, full_weights, target_weights))
            - modeled
            for mean in leave_one_means(full_blocks)
        ]
    )
    static_leave = np.array(
        [
            measured
            - submatrix(
                forward_model(
                    charge_conjugation_project_rho(
                        normalize_rho(subvector(mean, static_weights, model_weights)),
                        model_weights,
                    ),
                    operators,
                ),
                model_weights,
                target_weights,
            )
            for mean in leave_one_means(static_blocks)
        ]
    )
    full_coordinate_covariance = jackknife_covariance(
        np.array([matrix_vector(value) for value in full_leave])
    )
    static_coordinate_covariance = jackknife_covariance(
        np.array([matrix_vector(value) for value in static_leave])
    )
    coordinate_covariance = (
        full_coordinate_covariance + static_coordinate_covariance
    )
    full_covariance = jackknife_covariance(
        np.array([symmetry_vector(value, target_weights) for value in full_leave])
    )
    static_covariance = jackknife_covariance(
        np.array([symmetry_vector(value, target_weights) for value in static_leave])
    )
    covariance = full_covariance + static_covariance
    return ForwardAnalysis(
        measured=measured,
        rho=rho,
        modeled=modeled,
        residual=residual,
        covariance=covariance,
        coordinate_covariance=coordinate_covariance,
        metric=covariance_metric(symmetry_vector(residual, target_weights), covariance),
        full_leave=full_leave,
        static_leave=static_leave,
    )


def max_coordinate_z(matrix: np.ndarray, covariance: np.ndarray) -> float:
    errors = np.sqrt(np.clip(np.diag(covariance), 0.0, None))
    vector = matrix_vector(matrix)
    usable = errors > 1.0e-14
    return (
        float(np.max(np.abs(vector[usable]) / errors[usable]))
        if np.any(usable)
        else math.inf
    )


def maximum_chain_deviation(
    chain_matrices: list[np.ndarray],
    center: np.ndarray,
    covariance: np.ndarray,
) -> float:
    errors = np.sqrt(np.clip(np.diag(covariance), 0.0, None))
    usable = errors > 1.0e-14
    if not np.any(usable):
        return math.inf
    return max(
        float(
            np.max(
                np.abs(matrix_vector(matrix - center)[usable]) / errors[usable]
            )
        )
        for matrix in chain_matrices
    )


def largest_coordinate_discrepancy(
    analysis: ForwardAnalysis,
    weights: tuple[Weight, ...],
) -> str:
    vector = matrix_vector(analysis.residual)
    errors = np.sqrt(
        np.clip(np.diag(analysis.coordinate_covariance), 0.0, None)
    )
    usable = errors > 1.0e-14
    ratios = np.full(len(vector), -math.inf)
    ratios[usable] = np.abs(vector[usable]) / errors[usable]
    position = int(np.argmax(ratios))
    size = len(weights)
    component = "Re" if position < size * size else "Im"
    flat = position % (size * size)
    row, column = divmod(flat, size)
    measured_value = (
        analysis.measured[row, column].real
        if component == "Re"
        else analysis.measured[row, column].imag
    )
    modeled_value = (
        analysis.modeled[row, column].real
        if component == "Re"
        else analysis.modeled[row, column].imag
    )
    return (
        f"{component} C[{weights[row]},{weights[column]}]: "
        f"measured/model={measured_value:+.6f}/{modeled_value:+.6f}; "
        f"SE={errors[position]:.2e}; z={ratios[position]:.2f}"
    )


def maximum_ratio_autocorrelation(
    sample_arrays: list[np.ndarray],
    source_weights: tuple[Weight, ...],
    target_weights: tuple[Weight, ...],
) -> float:
    """Conservative tau_int over every resolved normalized target coordinate."""
    index = {weight: i for i, weight in enumerate(source_weights)}
    positions = [index[weight] for weight in target_weights]
    maximum = 0.5
    for samples in sample_arrays:
        if samples.ndim == 3:
            selected = samples[:, positions][:, :, positions]
            center = normalize_matrix(np.mean(selected, axis=0))
            denominator = selected[:, 0, 0]
            residuals = selected - denominator[:, None, None] * center[None, :, :]
        elif samples.ndim == 2:
            selected = samples[:, positions]
            center = normalize_rho(np.mean(selected, axis=0))
            denominator = selected[:, 0]
            residuals = selected - denominator[:, None] * center[None, :]
        else:
            raise ValueError("ratio autocorrelation expects vector or matrix samples")
        flattened = residuals.reshape(len(residuals), -1)
        for column in range(flattened.shape[1]):
            for values in (flattened[:, column].real, flattened[:, column].imag):
                if float(np.var(values)) > 1.0e-20:
                    maximum = max(
                        maximum,
                        integrated_autocorrelation_time(values),
                    )
    return maximum


def stratified_block_resample(
    blocks: np.ndarray,
    blocks_per_chain: int,
    rng: np.random.Generator,
) -> np.ndarray:
    """Resample within each chain without mixing chain strata."""
    by_chain = blocks.reshape(CHAINS, blocks_per_chain, *blocks.shape[1:])
    indices = rng.integers(
        0, blocks_per_chain, size=(CHAINS, blocks_per_chain)
    )
    chain_index = np.arange(CHAINS)[:, None]
    return by_chain[chain_index, indices].reshape(-1, *blocks.shape[1:])


def null_centered_residual(
    resampled_residual: np.ndarray, observed_residual: np.ndarray
) -> np.ndarray:
    return resampled_residual - observed_residual


def bootstrap_tail_summary(
    exceeded: int, replicates: int
) -> tuple[float, float]:
    p_value = (exceeded + 1.0) / (replicates + 1.0)
    upper_95 = (
        float(beta_distribution.ppf(0.95, exceeded + 1, replicates - exceeded))
        if exceeded < replicates
        else 1.0
    )
    return p_value, upper_95


def rejection_certificate(
    certifying_protocol: bool,
    chain_health: bool,
    covariance_health: bool,
    auxiliary_shift_z: float,
    bootstrap_exceeded: int,
    bootstrap_rank_failures: int,
    bootstrap_upper_95: float,
) -> bool:
    return bool(
        certifying_protocol
        and chain_health
        and covariance_health
        and auxiliary_shift_z < 2.0
        and bootstrap_exceeded == 0
        and bootstrap_rank_failures == 0
        and bootstrap_upper_95 < PRIMARY_P_FLOOR
    )


def blocked_sampling_health(
    finite_samples: bool,
    full_block_count: int,
    static_block_count: int,
    full_acceptance: np.ndarray,
    static_acceptance: np.ndarray,
    full_block_size: int,
    static_block_size: int,
    full_tau: float,
    static_tau: float,
    config: Config,
) -> bool:
    return bool(
        finite_samples
        and full_block_count == CHAINS * config.blocks_per_chain
        and static_block_count == CHAINS * config.blocks_per_chain
        and np.all((full_acceptance > 0.25) & (full_acceptance < 0.80))
        and np.all((static_acceptance > 0.25) & (static_acceptance < 0.80))
        and (
            config.pilot
            or (
                full_block_size > 10.0 * full_tau
                and static_block_size > 10.0 * static_tau
            )
        )
    )


def chain_agreement_health(full_chain_z: float, static_chain_z: float) -> bool:
    return bool(full_chain_z < 5.0 and static_chain_z < 5.0)


def cutoff_stabilized(auxiliary_shift_z: float) -> bool:
    return bool(auxiliary_shift_z < 2.0)


def covariance_resolved(metric: CovarianceMetric, expected_dimension: int) -> bool:
    return bool(
        metric.psd
        and metric.dimension == expected_dimension
        and metric.rank == expected_dimension
        and metric.null_residual < 1.0e-8
    )


def null_centered_block_bootstrap(
    full_blocks: np.ndarray,
    full_weights: tuple[Weight, ...],
    static_blocks: np.ndarray,
    static_weights: tuple[Weight, ...],
    operators: SectorOperators,
    target_weights: tuple[Weight, ...],
    analysis: ForwardAnalysis,
    blocks_per_chain: int,
    replicates: int,
) -> tuple[int, int, float, float]:
    """Null-centered, replicate-studentized stratified two-ensemble bootstrap."""
    observed = symmetry_vector(analysis.residual, target_weights)
    observed_statistic = analysis.metric.chi_square
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    exceeded = 0
    rank_failures = 0
    for _ in range(replicates):
        full_resample = stratified_block_resample(
            full_blocks, blocks_per_chain, rng
        )
        static_resample = stratified_block_resample(
            static_blocks, blocks_per_chain, rng
        )
        replicate = forward_analysis(
            full_resample,
            full_weights,
            static_resample,
            static_weights,
            operators,
            measurement_weights=target_weights,
        )
        resampled = symmetry_vector(replicate.residual, target_weights)
        null_residual = null_centered_residual(resampled, observed)
        null_metric = covariance_metric(null_residual, replicate.covariance)
        if (
            not null_metric.psd
            or null_metric.rank != len(null_residual)
            or not math.isfinite(null_metric.chi_square)
        ):
            rank_failures += 1
            exceeded += 1
        else:
            exceeded += int(null_metric.chi_square >= observed_statistic)
    p_value, upper_95 = bootstrap_tail_summary(exceeded, replicates)
    return exceeded, rank_failures, p_value, upper_95


def local_delta_control() -> tuple[float, float]:
    rng = np.random.default_rng(91873)
    links = initial_links(rng, "hot", slices=2)
    before = two_slice_log_weight(links, BETA)
    tau, link_id = 1, 17
    old = links[tau, link_id].copy()
    old_local = two_slice_local_log_weight(links, tau, link_id, BETA)
    old_spatial = sum(
        spatial_real_trace(links[tau], face_id)
        for face_id in LINK_TO_FACES[link_id]
    )
    old_mixed = mixed_real_trace(links, link_id)
    links[tau, link_id] = random_su2_subgroup_step(rng, 0.27) @ old
    new_spatial = sum(
        spatial_real_trace(links[tau], face_id)
        for face_id in LINK_TO_FACES[link_id]
    )
    new_mixed = mixed_real_trace(links, link_id)
    after = two_slice_log_weight(links, BETA)
    new_local = two_slice_local_log_weight(links, tau, link_id, BETA)
    correct = (BETA / 6.0) * (new_spatial - old_spatial) + (BETA / 3.0) * (
        new_mixed - old_mixed
    )
    mutated = (BETA / 3.0) * (new_spatial - old_spatial) + (BETA / 3.0) * (
        new_mixed - old_mixed
    )
    implementation_error = max(
        abs((after - before) - correct),
        abs((new_local - old_local) - correct),
    )
    return implementation_error, abs(correct - mutated)


def orientation_control(weights: tuple[Weight, ...]) -> tuple[float, float]:
    rng = np.random.default_rng(91909)
    links = initial_links(rng, "hot", slices=1)
    trace = np.trace(face_matrix(links, FACES[0]))
    vector = np.array(
        [su3_character_from_trace(trace, p, q) for p, q in weights], dtype=complex
    )
    actual = character_cross_moment(vector[None, :], vector[None, :])
    expected = np.outer(np.conjugate(vector), vector)
    mutated = np.outer(vector, vector)
    return (
        float(np.max(np.abs(actual - expected))),
        float(np.max(np.abs(mutated - expected))),
    )


def operator_formula_controls(
    operators: dict[int, SectorOperators],
    coefficient_lookup: dict[Weight, float],
) -> tuple[float, float, float, float, float]:
    """Cross-check the declared multiplier and local-factor formulas."""
    multiplier_error = 0.0
    inverse_error = 0.0
    diagonal_error = 0.0
    wrong_tau_gap = math.inf
    wrong_power_gap = math.inf
    c00 = coefficient_lookup[(0, 0)]
    for nmax, sector in operators.items():
        recurrence, weights_list, _ = build_numeric_recurrence(nmax)
        weights = tuple(weights_list)
        if weights != sector.weights:
            return math.inf, math.inf, math.inf, 0.0, 0.0
        expected_multiplier = expm((BETA / 2.0) * recurrence)
        expected_inverse = expm((-BETA / 2.0) * recurrence)
        multiplier_scale = max(float(np.linalg.norm(expected_multiplier)), 1.0)
        inverse_scale = max(float(np.linalg.norm(expected_inverse)), 1.0)
        multiplier_error = max(
            multiplier_error,
            float(np.linalg.norm(sector.multiplier - expected_multiplier))
            / multiplier_scale,
        )
        inverse_error = max(
            inverse_error,
            float(np.linalg.norm(sector.inverse_multiplier - expected_inverse))
            / inverse_scale,
        )
        link_eigenvalues = np.array(
            [
                coefficient_lookup[weight] / (dim_su3(*weight) * c00)
                for weight in weights
            ],
            dtype=float,
        )
        expected_diagonal = np.diag(link_eigenvalues**4)
        diagonal_error = max(
            diagonal_error,
            float(np.max(np.abs(sector.diagonal - expected_diagonal))),
        )
        wrong_tau = expm((BETA / 3.0) * recurrence)
        wrong_tau_gap = min(
            wrong_tau_gap,
            float(np.linalg.norm(expected_multiplier - wrong_tau))
            / multiplier_scale,
        )
        wrong_power_gap = min(
            wrong_power_gap,
            float(
                np.max(
                    np.abs(expected_diagonal - np.diag(link_eigenvalues**3))
                )
            ),
        )
    return (
        multiplier_error,
        inverse_error,
        diagonal_error,
        wrong_tau_gap,
        wrong_power_gap,
    )


def static_deletion_control(weights: tuple[Weight, ...]) -> tuple[float, float]:
    """Compare the production deletion observable with a scalar-loop formula."""
    rng = np.random.default_rng(91931)
    links = initial_links(rng, "hot", slices=1)
    traces = all_face_traces(links)[:5]
    actual = static_marked_deletion_observable(traces, weights, BETA)
    expected = np.array(
        [
            sum(
                math.exp(-(BETA / 3.0) * float(trace.real))
                * np.conjugate(su3_character_from_trace(trace, *weight))
                for trace in traces
            )
            / (len(traces) * dim_su3(*weight))
            for weight in weights
        ],
        dtype=complex,
    )
    characters = character_table(traces, weights)
    dimensions = np.array([dim_su3(*weight) for weight in weights], dtype=float)
    mutated = (
        np.mean(
            np.exp(-(BETA / 2.0) * traces.real)[:, None] * characters.conj(),
            axis=0,
        )
        / dimensions
    )
    return (
        float(np.max(np.abs(actual - expected))),
        float(np.max(np.abs(actual - mutated))),
    )


def algebraic_coordinate_controls(
    weights: tuple[Weight, ...],
) -> tuple[float, float]:
    """Pin normalization, charge projection, and B_1 coordinate ordering."""
    matrix = (
        np.arange(1.0, 17.0).reshape(4, 4)
        + 1j * np.arange(21.0, 37.0).reshape(4, 4)
    )
    matrix[0, 0] = 2.0 + 0.0j
    vector = np.array([2.0 + 0.0j, 3.0 + 1.0j, 5.0 - 2.0j, 7.0 + 3.0j])
    normalization_error = max(
        float(np.max(np.abs(normalize_matrix(matrix) - matrix / matrix[0, 0]))),
        float(np.max(np.abs(normalize_rho(vector) - vector / vector[0]))),
    )
    wrong_normalization_gap = max(
        float(np.max(np.abs(matrix / matrix[1, 1] - matrix / matrix[0, 0]))),
        float(np.max(np.abs(vector / vector[1] - vector / vector[0]))),
    )

    projected = charge_conjugation_project_rho(vector, weights)
    expected_projection = np.array([2.0, 4.0, 4.0, 7.0], dtype=complex)
    projection_error = float(np.max(np.abs(projected - expected_projection)))

    expected_coordinates = np.array(
        [
            matrix[0, 1].real,
            matrix[0, 1].imag,
            matrix[0, 3].real,
            matrix[1, 0].real,
            matrix[1, 0].imag,
            matrix[1, 1].real,
            matrix[1, 1].imag,
            matrix[1, 2].real,
            matrix[1, 2].imag,
            matrix[1, 3].real,
            matrix[1, 3].imag,
            matrix[3, 0].real,
            matrix[3, 1].real,
            matrix[3, 1].imag,
            matrix[3, 3].real,
        ]
    )
    coordinate_error = float(
        np.max(np.abs(symmetry_vector(matrix, weights) - expected_coordinates))
    )
    return (
        max(normalization_error, projection_error, coordinate_error),
        wrong_normalization_gap,
    )


def statistical_controls() -> tuple[float, float, float, float, float, float, bool]:
    """Independent small-array controls for every statistical gate family."""
    vectors = np.array(
        [[1.0, -2.0, 0.5], [2.0, 1.0, -0.5], [-1.0, 0.0, 1.5], [0.5, 2.5, 0.0]]
    )
    center = np.mean(vectors, axis=0)
    deviations = vectors - center
    expected_covariance = (len(vectors) - 1.0) / len(vectors) * sum(
        np.outer(deviation, deviation) for deviation in deviations
    )
    covariance_error = float(
        np.max(np.abs(jackknife_covariance(vectors) - expected_covariance))
    )

    sample_arrays = [
        np.arange(12.0).reshape(6, 2),
        np.arange(12.0, 24.0).reshape(6, 2),
    ]
    expected_blocks = np.array(
        [
            [1.0, 2.0],
            [5.0, 6.0],
            [9.0, 10.0],
            [13.0, 14.0],
            [17.0, 18.0],
            [21.0, 22.0],
        ]
    )
    actual_blocks = block_means(sample_arrays, 3)
    expected_leave = np.array(
        [
            (np.sum(expected_blocks, axis=0) - block)
            / (len(expected_blocks) - 1)
            for block in expected_blocks
        ]
    )
    blocking_error = max(
        float(np.max(np.abs(actual_blocks - expected_blocks))),
        float(
            np.max(
                np.abs(leave_one_means(actual_blocks) - expected_leave)
            )
        ),
    )
    covariance_error = max(covariance_error, blocking_error)

    metric = covariance_metric(
        np.array([1.0, 2.0]), np.diag(np.array([4.0, 9.0]))
    )
    metric_error = abs(metric.chi_square - (1.0 / 4.0 + 4.0 / 9.0))

    blocks_per_chain = 3
    blocks = np.arange(CHAINS * blocks_per_chain * 2, dtype=float).reshape(-1, 2)
    actual_rng = np.random.default_rng(91943)
    actual_resample = stratified_block_resample(
        blocks, blocks_per_chain, actual_rng
    )
    reference_rng = np.random.default_rng(91943)
    indices = reference_rng.integers(
        0, blocks_per_chain, size=(CHAINS, blocks_per_chain)
    )
    by_chain = blocks.reshape(CHAINS, blocks_per_chain, 2)
    expected_resample = np.array(
        [
            by_chain[chain, index]
            for chain, row in enumerate(indices)
            for index in row
        ]
    )
    resample_error = float(np.max(np.abs(actual_resample - expected_resample)))

    observed = np.array([0.3, -0.4, 0.2])
    resampled = np.array([0.5, -0.1, -0.2])
    centered = null_centered_residual(resampled, observed)
    center_error = float(np.max(np.abs(centered - (resampled - observed))))
    uncentered_gap = float(np.max(np.abs(resampled - centered)))

    p_value, upper_95 = bootstrap_tail_summary(0, BOOTSTRAP_REPLICATES)
    expected_upper = 1.0 - 0.05 ** (1.0 / BOOTSTRAP_REPLICATES)
    tail_error = max(
        abs(p_value - 1.0 / (BOOTSTRAP_REPLICATES + 1.0)),
        abs(upper_95 - expected_upper),
    )
    production_config = Config(False, 2, 900, 2400, 2400, 4, 12)
    acceptances = np.full(CHAINS, 0.5)
    boundary_acceptances = acceptances.copy()
    boundary_acceptances[0] = 0.25
    health_boundaries = (
        blocked_sampling_health(
            True,
            48,
            48,
            acceptances,
            acceptances,
            50,
            50,
            4.9,
            4.9,
            production_config,
        )
        and not blocked_sampling_health(
            True,
            48,
            48,
            acceptances,
            acceptances,
            50,
            50,
            5.0,
            4.9,
            production_config,
        )
        and not blocked_sampling_health(
            True,
            48,
            48,
            boundary_acceptances,
            acceptances,
            50,
            50,
            4.9,
            4.9,
            production_config,
        )
        and not blocked_sampling_health(
            False,
            48,
            48,
            acceptances,
            acceptances,
            50,
            50,
            4.9,
            4.9,
            production_config,
        )
        and chain_agreement_health(4.9, 4.9)
        and not chain_agreement_health(5.0, 4.9)
        and cutoff_stabilized(1.9)
        and not cutoff_stabilized(2.0)
        and covariance_resolved(metric, 2)
        and not covariance_resolved(metric, 3)
    )
    gate_control = health_boundaries and (
        rejection_certificate(True, True, True, 0.5, 0, 0, PRIMARY_P_FLOOR / 2.0)
        and not rejection_certificate(True, True, True, 0.5, 1, 0, PRIMARY_P_FLOOR / 2.0)
        and not rejection_certificate(True, True, True, 0.5, 0, 1, PRIMARY_P_FLOOR / 2.0)
        and not rejection_certificate(True, True, True, 2.0, 0, 0, PRIMARY_P_FLOOR / 2.0)
        and not rejection_certificate(True, True, True, 0.5, 0, 0, PRIMARY_P_FLOOR)
        and not rejection_certificate(False, True, True, 0.5, 0, 0, PRIMARY_P_FLOOR / 2.0)
        and not rejection_certificate(True, False, True, 0.5, 0, 0, PRIMARY_P_FLOOR / 2.0)
        and not rejection_certificate(True, True, False, 0.5, 0, 0, PRIMARY_P_FLOOR / 2.0)
    )
    return (
        covariance_error,
        metric_error,
        resample_error,
        center_error,
        uncentered_gap,
        tail_error,
        gate_control,
    )


def synthetic_controls(
    operators: SectorOperators,
) -> tuple[float, float, float]:
    rho = np.array(
        [1.0 / (1.0 + p + q + p * q) for p, q in operators.weights], dtype=float
    )
    synthetic = normalize_matrix(
        operators.multiplier
        @ operators.diagonal
        @ np.diag(rho)
        @ operators.multiplier
    )
    residual = float(np.max(np.abs(synthetic - forward_model(rho, operators))))
    recovered = direct_strip(synthetic, operators)
    strip_error = float(np.max(np.abs(recovered - np.diag(rho / rho[0]))))

    hostile_residual = np.diag(rho).astype(complex)
    hostile_residual[0, 1] = 0.125
    hostile_compression = normalize_matrix(
        operators.multiplier
        @ operators.diagonal
        @ hostile_residual
        @ operators.multiplier
    )
    diagonal_projection = forward_model(np.diag(hostile_residual), operators)
    hostile_gap = float(np.max(np.abs(hostile_compression - diagonal_projection)))
    return residual, strip_error, hostile_gap


def projected_auxiliary_models(
    static_blocks: np.ndarray,
    static_weights: tuple[Weight, ...],
    operators: dict[int, SectorOperators],
) -> dict[int, np.ndarray]:
    static_center = np.mean(static_blocks, axis=0)
    shared_weights = operators[SHARED_NMAX].weights
    output: dict[int, np.ndarray] = {}
    for nmax, sector in operators.items():
        rho = charge_conjugation_project_rho(
            normalize_rho(subvector(static_center, static_weights, sector.weights)),
            sector.weights,
        )
        model = forward_model(rho, sector)
        output[nmax] = submatrix(model, sector.weights, shared_weights)
    return output


def direct_inverse_diagnostics(
    full_blocks: np.ndarray,
    full_weights: tuple[Weight, ...],
    operators1: SectorOperators,
    operators2: SectorOperators,
) -> tuple[float, float, int]:
    center = np.mean(full_blocks, axis=0)
    c1 = normalize_matrix(submatrix(center, full_weights, operators1.weights))
    c2 = normalize_matrix(submatrix(center, full_weights, operators2.weights))
    stripped1 = direct_strip(c1, operators1)
    stripped2 = submatrix(
        direct_strip(c2, operators2), operators2.weights, operators1.weights
    )
    difference = stripped2 - stripped1

    differences: list[np.ndarray] = []
    for mean in leave_one_means(full_blocks):
        leave1 = direct_strip(
            normalize_matrix(submatrix(mean, full_weights, operators1.weights)),
            operators1,
        )
        leave2 = submatrix(
            direct_strip(
                normalize_matrix(submatrix(mean, full_weights, operators2.weights)),
                operators2,
            ),
            operators2.weights,
            operators1.weights,
        )
        differences.append(leave2 - leave1)
    vectors = np.array([matrix_vector(value) for value in differences])
    covariance = jackknife_covariance(vectors)
    metric = covariance_metric(matrix_vector(difference), covariance)
    amplification = (
        operators2.diagonal_condition * operators2.multiplier_condition**2
    )
    return amplification, metric.max_studentized, metric.rank


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pilot", action="store_true")
    parser.add_argument("--nmax", type=int, default=PRODUCTION_NMAX, choices=(1, 2))
    parser.add_argument("--therm", type=int)
    parser.add_argument("--full-measure", type=int)
    parser.add_argument("--static-measure", type=int)
    parser.add_argument("--sample-every", type=int)
    parser.add_argument("--blocks-per-chain", type=int)
    return parser.parse_args()


def resolve_config(args: argparse.Namespace) -> Config:
    if args.pilot:
        defaults = (20, 64, 64, 4, 4)
    else:
        defaults = (900, 2400, 2400, 4, 12)
    therm = defaults[0] if args.therm is None else args.therm
    full_measure = defaults[1] if args.full_measure is None else args.full_measure
    static_measure = defaults[2] if args.static_measure is None else args.static_measure
    sample_every = defaults[3] if args.sample_every is None else args.sample_every
    blocks = defaults[4] if args.blocks_per_chain is None else args.blocks_per_chain
    if min(therm, full_measure, static_measure, sample_every, blocks) <= 0:
        raise ValueError("all sweep, cadence, and blocking arguments must be positive")
    if not args.pilot and args.nmax != PRODUCTION_NMAX:
        raise ValueError("a production run requires --nmax 2")
    if full_measure % sample_every or static_measure % sample_every:
        raise ValueError("measurement sweeps must be divisible by the sample cadence")
    if (full_measure // sample_every) % blocks:
        raise ValueError("full samples must divide evenly into equal blocks")
    if (static_measure // sample_every) % blocks:
        raise ValueError("static samples must divide evenly into equal blocks")
    if full_measure // sample_every < 2 * blocks:
        raise ValueError("full sampler needs at least two samples per block")
    if static_measure // sample_every < 2 * blocks:
        raise ValueError("static sampler needs at least two samples per block")
    return Config(
        pilot=bool(args.pilot),
        nmax=int(args.nmax),
        therm=int(therm),
        full_measure=int(full_measure),
        static_measure=int(static_measure),
        sample_every=int(sample_every),
        blocks_per_chain=int(blocks),
    )


def main() -> int:
    config = resolve_config(parse_args())
    reporter = Reporter()
    fixed_production = Config(
        pilot=False,
        nmax=PRODUCTION_NMAX,
        therm=900,
        full_measure=2400,
        static_measure=2400,
        sample_every=4,
        blocks_per_chain=12,
    )
    certifying_protocol = config == fixed_production
    mode = "PILOT / NON-CERTIFYING" if config.pilot else "PRODUCTION"
    full_weights = tuple(weights_box(config.nmax))
    static_weights = tuple(weights_box(AUXILIARY_NMAX))

    all_coefficient_weights = tuple(weights_box(AUXILIARY_NMAX))
    coefficient_lookup = {
        weight: wilson_character_coefficient(*weight, BETA)
        for weight in all_coefficient_weights
    }
    operators = {
        nmax: build_operators(nmax, coefficient_lookup)
        for nmax in range(SHARED_NMAX, AUXILIARY_NMAX + 1)
    }

    print("FULL TWO-SLICE WILSON COMPRESSION, ACTUAL L_s=3")
    print(
        f"mode={mode}; beta={BETA:g}; B_full=B_{config.nmax} ({len(full_weights)} states); "
        f"shared=B_1; static auxiliary=B_{AUXILIARY_NMAX}"
    )
    print(
        f"four chains/ensemble; therm={config.therm}; full/static measure="
        f"{config.full_measure}/{config.static_measure}; every={config.sample_every}; "
        f"blocks/chain={config.blocks_per_chain}"
    )
    print("Forward model has no fitted parameter beyond C_(0,0) normalization.")

    print("Implementation and synthetic controls")
    local_error, mutated_error = local_delta_control()
    reporter.check(
        "81+81+81 action census and local Metropolis delta",
        3 * L**3 == 81
        and len(FACES) == 81
        and all(len(value) == 4 for value in LINK_TO_FACES)
        and local_error < 1.0e-11,
        f"delta error={local_error:.2e}",
    )
    reporter.check(
        "wrong full-strength spatial half-action is rejected",
        mutated_error > 1.0e-6,
        f"mutated error={mutated_error:.2e}",
    )
    orientation_error, mutated_orientation_error = orientation_control(
        operators[SHARED_NMAX].weights
    )
    reporter.check(
        "outgoing-conjugate cross-moment orientation",
        orientation_error < 1.0e-12 and mutated_orientation_error > 1.0e-6,
        f"implementation error/mutated gap={orientation_error:.1e}/{mutated_orientation_error:.1e}",
    )
    (
        multiplier_error,
        inverse_error,
        diagonal_error,
        wrong_tau_gap,
        wrong_power_gap,
    ) = operator_formula_controls(operators, coefficient_lookup)
    reporter.check(
        "independent exp[(beta/2)J] and fourth-power local-factor formulas",
        max(multiplier_error, inverse_error) < 1.0e-12
        and diagonal_error < 1.0e-14
        and wrong_tau_gap > 1.0e-2
        and wrong_power_gap > 1.0e-3,
        f"M/Minv/D errors={multiplier_error:.1e}/{inverse_error:.1e}/{diagonal_error:.1e}; "
        f"mutation gaps={wrong_tau_gap:.2e}/{wrong_power_gap:.2e}",
    )
    deletion_error, mutated_deletion_gap = static_deletion_control(
        operators[SHARED_NMAX].weights
    )
    reporter.check(
        "independent marked-factor-deletion observable formula",
        deletion_error < 1.0e-12 and mutated_deletion_gap > 1.0e-3,
        f"implementation error/mutated gap={deletion_error:.1e}/{mutated_deletion_gap:.2e}",
    )
    algebraic_error, wrong_normalization_gap = algebraic_coordinate_controls(
        operators[SHARED_NMAX].weights
    )
    reporter.check(
        "trivial normalization, conjugation projection and 15-coordinate map",
        algebraic_error < 1.0e-12 and wrong_normalization_gap > 1.0e-3,
        f"implementation error/wrong-normalizer gap={algebraic_error:.1e}/{wrong_normalization_gap:.2e}",
    )
    synthetic_residual, strip_error, hostile_gap = synthetic_controls(
        operators[PRODUCTION_NMAX]
    )
    reporter.check(
        "exact synthetic forward factorization and normalized strip",
        synthetic_residual < 1.0e-13 and strip_error < 1.0e-6,
        f"forward/strip errors={synthetic_residual:.1e}/{strip_error:.1e}",
    )
    reporter.check(
        "off-diagonal residual defeats diagonal projection helper",
        hostile_gap > 1.0e-5,
        f"detected gap={hostile_gap:.2e}",
    )
    (
        covariance_error,
        metric_error,
        resample_error,
        center_error,
        uncentered_gap,
        tail_error,
        gate_control,
    ) = statistical_controls()
    reporter.check(
        "independent covariance, stratification, null-centering, tail and gate controls",
        max(
            covariance_error,
            metric_error,
            resample_error,
            center_error,
            tail_error,
        )
        < 1.0e-12
        and uncentered_gap > 1.0e-2
        and gate_control,
        f"max error={max(covariance_error, metric_error, resample_error, center_error, tail_error):.1e}; "
        f"uncentered gap={uncentered_gap:.1e}",
    )
    reporter.check(
        "independent ensembles have four disjoint deterministic seeds",
        len(FULL_SEEDS) == CHAINS
        and len(STATIC_SEEDS) == CHAINS
        and set(FULL_SEEDS).isdisjoint(STATIC_SEEDS),
    )
    reporter.check(
        "audit certificate uses the frozen production configuration",
        (config.pilot or certifying_protocol)
        and PRIMARY_P_FLOOR == 1.0e-3
        and BOOTSTRAP_REPLICATES == 4096
        and BOOTSTRAP_SEED == 92507,
        "overridden non-pilot configurations are non-certifying",
    )

    start = time.perf_counter()
    full_chains = [
        run_two_slice_chain(
            seed=seed,
            initial="cold" if chain % 2 == 0 else "hot",
            therm=config.therm,
            measure=config.full_measure,
            sample_every=config.sample_every,
            weights=full_weights,
        )
        for chain, seed in enumerate(FULL_SEEDS)
    ]
    full_elapsed = time.perf_counter() - start
    start = time.perf_counter()
    static_chains = [
        run_static_chain(
            seed=seed,
            initial="hot" if chain % 2 == 0 else "cold",
            therm=config.therm,
            measure=config.static_measure,
            sample_every=config.sample_every,
            weights=static_weights,
        )
        for chain, seed in enumerate(STATIC_SEEDS)
    ]
    static_elapsed = time.perf_counter() - start

    full_blocks = block_means(
        [chain.samples for chain in full_chains], config.blocks_per_chain
    )
    static_blocks = block_means(
        [chain.samples for chain in static_chains], config.blocks_per_chain
    )
    full_acceptance = np.array([chain.acceptance for chain in full_chains])
    static_acceptance = np.array([chain.acceptance for chain in static_chains])
    full_block_size = min(len(chain.samples) for chain in full_chains) // config.blocks_per_chain
    static_block_size = min(len(chain.samples) for chain in static_chains) // config.blocks_per_chain
    full_tau = maximum_ratio_autocorrelation(
        [chain.samples for chain in full_chains],
        full_weights,
        operators[SHARED_NMAX].weights,
    )
    static_tau = maximum_ratio_autocorrelation(
        [chain.samples for chain in static_chains],
        static_weights,
        operators[AUXILIARY_NMAX].weights,
    )
    finite_samples = bool(
        np.all(np.isfinite(full_blocks.real))
        and np.all(np.isfinite(full_blocks.imag))
        and np.all(np.isfinite(static_blocks.real))
        and np.all(np.isfinite(static_blocks.imag))
    )
    print("Sampling health")
    print(
        f"  full:   acceptance={full_acceptance.min():.3f}..{full_acceptance.max():.3f}; "
        f"<P_space>={np.mean([np.mean(c.spatial_plaquettes) for c in full_chains]):.5f}; "
        f"<P_mix>={np.mean([np.mean(c.mixed_plaquettes) for c in full_chains]):.5f}; "
        f"block/tau={full_block_size}/{full_tau:.2f}; elapsed={full_elapsed:.1f}s"
    )
    print(
        f"  static: acceptance={static_acceptance.min():.3f}..{static_acceptance.max():.3f}; "
        f"<P>={np.mean([np.mean(c.plaquettes) for c in static_chains]):.5f}; "
        f"block/tau={static_block_size}/{static_tau:.2f}; elapsed={static_elapsed:.1f}s"
    )
    reporter.check(
        "four-chain blocked samples are finite with nondegenerate acceptance",
        blocked_sampling_health(
            finite_samples,
            len(full_blocks),
            len(static_blocks),
            full_acceptance,
            static_acceptance,
            full_block_size,
            static_block_size,
            full_tau,
            static_tau,
            config,
        ),
        f"blocks={len(full_blocks)}/{len(static_blocks)}; "
        f"block/tau={full_block_size}/{full_tau:.2f},{static_block_size}/{static_tau:.2f}",
    )

    auxiliary = projected_auxiliary_models(static_blocks, static_weights, operators)
    auxiliary_deltas = {
        nmax: float(np.linalg.norm(auxiliary[nmax] - auxiliary[nmax - 1], ord="fro"))
        for nmax in range(SHARED_NMAX + 1, AUXILIARY_NMAX + 1)
    }
    shared_positions2 = [operators[2].weights.index(w) for w in operators[1].weights]
    projected_m2 = operators[2].multiplier[np.ix_(shared_positions2, shared_positions2)]
    multiplier_noncommutation = float(
        np.linalg.norm(projected_m2 - operators[1].multiplier, ord="fro")
    )

    shared = forward_analysis(
        full_blocks,
        full_weights,
        static_blocks,
        static_weights,
        operators[AUXILIARY_NMAX],
        measurement_weights=operators[SHARED_NMAX].weights,
    )
    metric = shared.metric
    shared_weights = operators[SHARED_NMAX].weights
    full_chain_matrices = [
        normalize_matrix(
            submatrix(np.mean(chain.samples, axis=0), full_weights, shared_weights)
        )
        for chain in full_chains
    ]
    static_chain_models = []
    for chain in static_chains:
        chain_rho = charge_conjugation_project_rho(
            normalize_rho(np.mean(chain.samples, axis=0)),
            operators[AUXILIARY_NMAX].weights,
        )
        static_chain_models.append(
            submatrix(
                forward_model(chain_rho, operators[AUXILIARY_NMAX]),
                operators[AUXILIARY_NMAX].weights,
                shared_weights,
            )
        )
    full_chain_z = maximum_chain_deviation(
        full_chain_matrices,
        shared.measured,
        jackknife_covariance(
            np.array([matrix_vector(value) for value in shared.full_leave])
        ),
    )
    static_chain_z = maximum_chain_deviation(
        static_chain_models,
        shared.modeled,
        jackknife_covariance(
            np.array([matrix_vector(value) for value in shared.static_leave])
        ),
    )
    chain_health = chain_agreement_health(full_chain_z, static_chain_z)
    reporter.check(
        "independent hot/cold chain observables agree within five grand-mean SE",
        config.pilot or chain_health,
        f"full/static max={full_chain_z:.2f}/{static_chain_z:.2f} SE",
    )
    auxiliary_shift_z = max_coordinate_z(
        auxiliary[AUXILIARY_NMAX] - auxiliary[AUXILIARY_NMAX - 1],
        shared.coordinate_covariance,
    )
    print("Auxiliary-box projection diagnostics")
    print(
        "  "
        + "; ".join(
            f"||P1 Cmodel_{nmax} P1-Cmodel_{nmax-1}||F={delta:.3e}"
            for nmax, delta in auxiliary_deltas.items()
        )
    )
    print(
        f"  B_{AUXILIARY_NMAX-1}->B_{AUXILIARY_NMAX} "
        f"max shift/primary-residual SE={auxiliary_shift_z:.2f}"
    )
    print(f"  ||P1 M_2 P1-M_1||F={multiplier_noncommutation:.3e}")
    reporter.check(
        f"shared forward model stabilizes from auxiliary B_{AUXILIARY_NMAX-1} "
        f"to B_{AUXILIARY_NMAX}",
        cutoff_stabilized(auxiliary_shift_z),
        f"max shift={auxiliary_shift_z:.2f} primary-residual SE",
    )

    print(
        f"Primary shared B_1 forward residual using auxiliary "
        f"B_{AUXILIARY_NMAX} model"
    )
    print(
        f"  cov rank={metric.rank}/{metric.dimension}; min_eig={metric.minimum_eigenvalue:.2e}; "
        f"chi2/rank={metric.chi_square:.2f}/{metric.rank}; "
        f"asymptotic p(diag only)={metric.p_value:.3g}; "
        f"max|coordinate|/SE={metric.max_studentized:.2f}; null={metric.null_residual:.1e}"
    )
    print(f"  largest discrepancy: {largest_coordinate_discrepancy(shared, shared_weights)}")
    covariance_health = covariance_resolved(
        metric, len(operators[SHARED_NMAX].weights) ** 2 - 1
    )
    reporter.check(
        "shared forward covariance resolves its symmetry-supported sector",
        covariance_health,
        f"rank={metric.rank}, PSD={metric.psd}",
    )
    if config.pilot:
        print(
            f"  [DIAG] pilot asymptotic p={metric.p_value:.3g}; bootstrap and "
            "physics PASS/FAIL are not assigned"
        )
    else:
        (
            bootstrap_exceeded,
            bootstrap_rank_failures,
            bootstrap_p,
            bootstrap_upper_95,
        ) = null_centered_block_bootstrap(
            full_blocks,
            full_weights,
            static_blocks,
            static_weights,
            operators[AUXILIARY_NMAX],
            shared_weights,
            shared,
            config.blocks_per_chain,
            BOOTSTRAP_REPLICATES,
        )
        print(
            f"  null-centered stratified block bootstrap: exceedances="
            f"{bootstrap_exceeded}/{BOOTSTRAP_REPLICATES}; "
            f"rank_failures={bootstrap_rank_failures}; p={bootstrap_p:.6g}; "
            f"one-sided 95% upper={bootstrap_upper_95:.6g}"
        )
        reporter.check(
            "predeclared static-rho forward identification is rejected",
            rejection_certificate(
                certifying_protocol,
                chain_health,
                covariance_health,
                auxiliary_shift_z,
                bootstrap_exceeded,
                bootstrap_rank_failures,
                bootstrap_upper_95,
            ),
            f"predeclared p floor={PRIMARY_P_FLOOR:g}",
        )

    if config.nmax >= PRODUCTION_NMAX:
        full_box = forward_analysis(
            full_blocks,
            full_weights,
            static_blocks,
            static_weights,
            operators[AUXILIARY_NMAX],
            measurement_weights=operators[PRODUCTION_NMAX].weights,
        )
        full_metric = full_box.metric
        print("B_2 forward residual (rank-limited diagnostic, not a gate)")
        print(
            f"  cov rank={full_metric.rank}/{full_metric.dimension}; "
            f"chi2/rank={full_metric.chi_square:.2f}/{full_metric.rank}; "
            f"p_support={full_metric.p_value:.3g}; max|coordinate|/SE="
            f"{full_metric.max_studentized:.2f}"
        )

    if config.nmax >= PRODUCTION_NMAX:
        amplification, stability_z, stability_rank = direct_inverse_diagnostics(
            full_blocks,
            full_weights,
            operators[SHARED_NMAX],
            operators[PRODUCTION_NMAX],
        )
        print("Direct inverse diagnostic only (never a gate)")
        print(
            f"  B_2 cond(D)cond(M)^2={amplification:.3e}; paired B_2->B_1 vs B_1 "
            f"max|difference|/JK-SE={stability_z:.2f}; cov rank={stability_rank}"
        )

    print(
        "per_element: checked and executed — the normalized shared 4x4 "
        "character matrix is tested coordinatewise and in its "
        "covariance-supported subspace"
    )
    print(
        "per_site: checked and not executed — all 81 translated/oriented "
        "plaquettes are symmetry-averaged, so no individual-face equality "
        "is tested or claimed"
    )
    print(
        "per_mode: checked and partially executed — B_1 is the physics "
        "surface, B_2 is sampled, and auxiliary models run through B_4; no "
        "B_5 or infinite-character claim is tested"
    )
    print(
        "per_block: checked and executed — 48 leave-one-block transforms per "
        "independent ensemble supply the combined covariance"
    )
    print(
        "lattice_wide: checked and partially executed — the result is only "
        "for the finite periodic L_s=3 Wilson lattice at beta=6; no volume "
        "sequence is tested"
    )
    print(f"TOTAL: PASS={reporter.passed} FAIL={reporter.failed}")
    return 0 if reporter.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
