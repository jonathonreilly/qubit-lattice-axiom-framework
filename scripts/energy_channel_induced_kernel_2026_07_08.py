#!/usr/bin/env python3
"""Check background energy-density susceptibility under uniform rescaling.

The implemented object is a nondynamical modulation of the full local energy
density of a free one-dimensional staggered-fermion comparator.  The runner
checks the zero-momentum Lehmann susceptibility, direct Hamiltonian-rescaling
linearity, a finite-momentum q^2+q^4 fit, and a lattice continuity identity.
It makes no field, particle, gauge, lapse, source, or gravity claim.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import sys
import time

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp


sys.dont_write_bytecode = True

N_SITES = 256
MASS_VALUES = (0.0, 0.05, 0.2, 0.5)
Q_FIT = (1, 2, 3, 4)
CONTINUITY_MASSES = (0.2, 0.5)
CONTINUITY_Q = (1, 2)
RESCALE_EPS = (1.0e-4, 2.0e-4)
DENOM_TOL = 1.0e-11
MATRIX_TOL = 1.0e-9
CHI0_TOL = 1.0e-20
RESCALE_REL_TOL = 1.0e-12
FIT_RESID_TOL = 5.0e-2
CONTINUITY_REL_TOL = 1.0e-8


def fmt(value: float, digits: int = 6) -> str:
    if math.isinf(value):
        return "inf" if value > 0 else "-inf"
    if math.isnan(value):
        return "nan"
    return f"{value:.{digits}g}"


def rel_error(left: float, right: float) -> float:
    return abs(left - right) / max(abs(left), abs(right), 1.0e-30)


def one_body_hamiltonian(n_sites: int, mass: float) -> np.ndarray:
    matrix = np.zeros((n_sites, n_sites), dtype=np.float64)
    for site in range(n_sites):
        matrix[site, site] += mass * (1.0 if site % 2 == 0 else -1.0)
        right = (site + 1) % n_sites
        matrix[site, right] += -0.5
        matrix[right, site] += -0.5
    return matrix


def lattice_momentum(n_sites: int, q_index: int) -> float:
    """Momentum grid for the two-site translation cell."""
    return 2.0 * np.pi * q_index / (n_sites // 2)


def local_energy_block(
    eigvecs: np.ndarray,
    empty: np.ndarray,
    occupied: np.ndarray,
    site: int,
    mass: float,
) -> np.ndarray:
    """Occupied-to-empty block of one bond plus half each endpoint site term."""
    right = (site + 1) % eigvecs.shape[0]
    stagger_site = 1.0 if site % 2 == 0 else -1.0
    stagger_right = 1.0 if right % 2 == 0 else -1.0
    bond = -0.5 * (
        np.conj(eigvecs[site, empty])[:, None] * eigvecs[right, occupied][None, :]
        + np.conj(eigvecs[right, empty])[:, None] * eigvecs[site, occupied][None, :]
    )
    endpoint_sites = 0.5 * mass * (
        stagger_site * np.conj(eigvecs[site, empty])[:, None] * eigvecs[site, occupied][None, :]
        + stagger_right * np.conj(eigvecs[right, empty])[:, None] * eigvecs[right, occupied][None, :]
    )
    return bond + endpoint_sites


def local_energy_blocks(
    eigvecs: np.ndarray,
    empty: np.ndarray,
    occupied: np.ndarray,
    mass: float,
) -> np.ndarray:
    return np.stack(
        [local_energy_block(eigvecs, empty, occupied, site, mass) for site in range(eigvecs.shape[0])],
        axis=0,
    )


def local_energy_matrix(n_sites: int, mass: float, site: int) -> sp.csr_matrix:
    right = (site + 1) % n_sites
    rows = [site, right, site, right]
    cols = [right, site, site, right]
    data = [
        -0.5 + 0.0j,
        -0.5 + 0.0j,
        0.5 * mass * (1.0 if site % 2 == 0 else -1.0),
        0.5 * mass * (1.0 if right % 2 == 0 else -1.0),
    ]
    matrix = sp.coo_matrix((data, (rows, cols)), shape=(n_sites, n_sites), dtype=np.complex128)
    matrix.sum_duplicates()
    return matrix.tocsr()


@dataclass(frozen=True)
class ResponseValue:
    chi: float
    singular_weight: float
    singular_count: int


def response_from_block(block: np.ndarray, denominators: np.ndarray) -> ResponseValue:
    zero_mask = denominators <= DENOM_TOL
    singular_weight = float(np.sum(np.abs(block[zero_mask]) ** 2)) if np.any(zero_mask) else 0.0
    singular_count = int(np.count_nonzero(np.abs(block[zero_mask]) > MATRIX_TOL)) if np.any(zero_mask) else 0
    if singular_count:
        return ResponseValue(math.inf, singular_weight, singular_count)
    finite = ~zero_mask
    chi = 2.0 * float(np.sum((np.abs(block[finite]) ** 2) / denominators[finite]))
    return ResponseValue(chi, singular_weight, singular_count)


def fourier_block(blocks: np.ndarray, q_index: int) -> np.ndarray:
    n_sites = blocks.shape[0]
    q = lattice_momentum(n_sites, q_index)
    phases = np.exp(-1.0j * q * np.arange(n_sites))
    transformed = phases @ blocks.reshape(n_sites, -1)
    return transformed.reshape(blocks.shape[1], blocks.shape[2])


def rescaling_linearity_error(hamiltonian: np.ndarray, ground_energy: float) -> float:
    errors: list[float] = []
    for epsilon in RESCALE_EPS:
        plus = float(np.sum(sla.eigvalsh((1.0 + epsilon) * hamiltonian, check_finite=False)[: N_SITES // 2]))
        minus = float(np.sum(sla.eigvalsh((1.0 - epsilon) * hamiltonian, check_finite=False)[: N_SITES // 2]))
        errors.append(abs(plus + minus - 2.0 * ground_energy) / max(abs(ground_energy), 1.0e-30))
    return max(errors)


def fit_small_momentum(q_values: dict[int, float]) -> tuple[float, float, float]:
    momenta = np.array([lattice_momentum(N_SITES, q_index) for q_index in Q_FIT], dtype=np.float64)
    values = np.array([q_values[q_index] for q_index in Q_FIT], dtype=np.float64)
    if not np.all(np.isfinite(values)):
        return math.nan, math.nan, math.inf
    design = np.column_stack([momenta**2, momenta**4])
    (coefficient_a, coefficient_b), *_ = np.linalg.lstsq(design, values, rcond=None)
    fitted = design @ np.array([coefficient_a, coefficient_b])
    residual = float(np.linalg.norm(values - fitted) / max(float(np.linalg.norm(values)), 1.0e-30))
    return float(coefficient_a), float(coefficient_b), residual


def energy_current_fourier_matrix(n_sites: int, mass: float, q_index: int) -> np.ndarray:
    densities = [local_energy_matrix(n_sites, mass, site) for site in range(n_sites)]
    q = lattice_momentum(n_sites, q_index)
    phases = np.exp(-1.0j * q * np.arange(n_sites))
    current = sp.csr_matrix((n_sites, n_sites), dtype=np.complex128)
    for site in range(n_sites):
        density = densities[site]
        next_density = densities[(site + 1) % n_sites]
        cut_current = 1.0j * (density @ next_density - next_density @ density)
        current = current + phases[site] * cut_current
    # This convention makes DeltaE*h(q)=(1-exp(-iq))*j_E(q).
    return (1.0j * current).toarray()


@dataclass(frozen=True)
class BackgroundResult:
    mass: float
    chi0: float
    rescaling_rel: float
    coefficient_a: float
    coefficient_b: float
    fit_residual: float
    zero_mode_ok: bool
    fit_ok: bool


@dataclass(frozen=True)
class ContinuityResult:
    mass: float
    q_index: int
    pair_rel: float
    kernel_rel: float
    ok: bool


def continuity_checks(
    mass: float,
    eigvecs: np.ndarray,
    empty: np.ndarray,
    occupied: np.ndarray,
    denominators: np.ndarray,
    blocks: np.ndarray,
) -> list[ContinuityResult]:
    empty_vectors = eigvecs[:, empty]
    occupied_vectors = eigvecs[:, occupied]
    results: list[ContinuityResult] = []
    for q_index in CONTINUITY_Q:
        q = lattice_momentum(N_SITES, q_index)
        factor = 1.0 - np.exp(-1.0j * q)
        h_block = fourier_block(blocks, q_index)
        current = energy_current_fourier_matrix(N_SITES, mass, q_index)
        j_block = empty_vectors.conj().T @ current @ occupied_vectors
        left = denominators * h_block
        right = factor * j_block
        scale = np.maximum(np.abs(left), np.abs(right))
        mask = scale > 1.0e-12
        pair_rel = float(np.max(np.abs(left[mask] - right[mask]) / scale[mask])) if np.any(mask) else 0.0

        response = response_from_block(h_block, denominators)
        finite = denominators > DENOM_TOL
        current_kernel = abs(factor) ** 2 * 2.0 * float(
            np.sum((np.abs(j_block[finite]) ** 2) / (denominators[finite] ** 3))
        )
        kernel_rel = rel_error(response.chi, current_kernel)
        ok = pair_rel <= CONTINUITY_REL_TOL and kernel_rel <= CONTINUITY_REL_TOL
        results.append(ContinuityResult(mass, q_index, pair_rel, kernel_rel, ok))
    return results


def run_background_checks() -> tuple[list[BackgroundResult], list[ContinuityResult]]:
    backgrounds: list[BackgroundResult] = []
    continuity: list[ContinuityResult] = []
    for mass in MASS_VALUES:
        hamiltonian = one_body_hamiltonian(N_SITES, mass)
        eigvals, eigvecs = sla.eigh(hamiltonian)
        order = np.argsort(eigvals.real)
        eigvals = eigvals[order].real
        eigvecs = eigvecs[:, order]
        occupied = np.arange(N_SITES // 2)
        empty = np.arange(N_SITES // 2, N_SITES)
        denominators = eigvals[empty][:, None] - eigvals[occupied][None, :]
        blocks = local_energy_blocks(eigvecs, empty, occupied, mass)
        q_values = {
            q_index: response_from_block(fourier_block(blocks, q_index), denominators).chi
            for q_index in (0, *Q_FIT)
        }
        ground_energy = float(np.sum(eigvals[: N_SITES // 2]))
        rescaling_rel = rescaling_linearity_error(hamiltonian, ground_energy)
        coefficient_a, coefficient_b, fit_residual = fit_small_momentum(q_values)
        zero_mode_ok = (
            math.isfinite(q_values[0])
            and abs(q_values[0]) <= CHI0_TOL
            and rescaling_rel <= RESCALE_REL_TOL
        )
        fit_ok = (
            math.isfinite(coefficient_a)
            and coefficient_a > 0.0
            and fit_residual <= FIT_RESID_TOL
        )
        backgrounds.append(
            BackgroundResult(
                mass,
                q_values[0],
                rescaling_rel,
                coefficient_a,
                coefficient_b,
                fit_residual,
                zero_mode_ok,
                fit_ok,
            )
        )
        if mass in CONTINUITY_MASSES:
            continuity.extend(continuity_checks(mass, eigvecs, empty, occupied, denominators, blocks))
    return backgrounds, continuity


def main() -> int:
    started = time.time()
    backgrounds, continuity = run_background_checks()
    zero_mode_ok = all(result.zero_mode_ok for result in backgrounds)
    fit_ok = all(result.fit_ok for result in backgrounds)
    continuity_ok = bool(continuity) and all(result.ok for result in continuity)
    passed = zero_mode_ok and fit_ok and continuity_ok

    background_text = ";".join(
        f"m={fmt(result.mass,3)}:chi0={fmt(result.chi0,3)},rescale={fmt(result.rescaling_rel,2)},"
        f"A={fmt(result.coefficient_a,6)},B={fmt(result.coefficient_b,6)},"
        f"fit_res={fmt(result.fit_residual,3)},"
        f"valid=zero:{'Y' if result.zero_mode_ok else 'N'}+fit:{'Y' if result.fit_ok else 'N'}"
        for result in backgrounds
    )
    continuity_text = ";".join(
        f"m={fmt(result.mass,3)},q={result.q_index}:pair={fmt(result.pair_rel,2)},"
        f"kernel={fmt(result.kernel_rel,2)},valid={'Y' if result.ok else 'N'}"
        for result in continuity
    )
    checks = (
        f"CHECK-01-zero-mode={'ok' if zero_mode_ok else 'FAIL'};"
        f"CHECK-02-small-q-fit={'ok' if fit_ok else 'FAIL'};"
        f"CHECK-03-continuity={'ok' if continuity_ok else 'FAIL'}"
    )
    print("SPEC-NOTE background-only;sum_hn=H;chi-positive-Lehmann;q=2pi*k/(N/2);no-dynamical-field")
    print(f"BACKGROUND {background_text}")
    print(f"CONTINUITY {continuity_text}")
    print(f"CHECKS {checks}")
    print(f"TOTAL {'PASS' if passed else 'MACHINERY-FAIL'} elapsed={time.time()-started:.2f}s")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
