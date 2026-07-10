#!/usr/bin/env python3
"""Check a local spectral-norm activity bound and finite toy witnesses.

For H=sum_X h_X and normalized rho,

    ||Tr_(R^c)(-i[H,rho])||_1 <= 2 sum_(X intersects R) ||h_X||.

The dense three-site check is independent of the analytic proof in the paired
note. One-particle chain checks provide finite toy witnesses only. Interpreting
activity as record-formation opportunity remains conditional on the separately
explicitly supplied activity-to-opportunity premise `AO`.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass

import numpy as np
import scipy.linalg as sla


RNG_SEED = 20260708
BOUND_TOL = 1.0e-12
WITNESS_TOL = 1.0e-11


def trace_norm_hermitian(matrix: np.ndarray) -> float:
    hermitian = 0.5 * (matrix + matrix.conj().T)
    return float(np.sum(np.abs(np.linalg.eigvalsh(hermitian))))


def normalize(vector: np.ndarray) -> np.ndarray:
    norm = float(np.linalg.norm(vector))
    if norm == 0.0:
        raise ValueError("zero vector")
    return np.asarray(vector, dtype=np.complex128) / norm


def partial_trace(matrix: np.ndarray, keep: tuple[int, ...], n_sites: int) -> np.ndarray:
    traced = tuple(site for site in range(n_sites) if site not in keep)
    tensor = np.asarray(matrix, dtype=np.complex128).reshape((2,) * (2 * n_sites))
    permutation = keep + traced + tuple(site + n_sites for site in keep) + tuple(
        site + n_sites for site in traced
    )
    d_keep = 2 ** len(keep)
    d_trace = 2 ** len(traced)
    arranged = tensor.transpose(permutation).reshape(d_keep, d_trace, d_keep, d_trace)
    return np.trace(arranged, axis1=1, axis2=3)


def kron_sites(operators: dict[int, np.ndarray], n_sites: int) -> np.ndarray:
    identity = np.eye(2, dtype=np.complex128)
    out = np.array([[1.0]], dtype=np.complex128)
    for site in range(n_sites):
        out = np.kron(out, operators.get(site, identity))
    return out


@dataclass(frozen=True)
class LocalTerm:
    support: frozenset[int]
    matrix: np.ndarray


def dense_local_model() -> tuple[np.ndarray, tuple[LocalTerm, ...]]:
    x = np.array(((0.0, 1.0), (1.0, 0.0)), dtype=np.complex128)
    y = np.array(((0.0, -1.0j), (1.0j, 0.0)), dtype=np.complex128)
    z = np.array(((1.0, 0.0), (0.0, -1.0)), dtype=np.complex128)
    terms = (
        LocalTerm(frozenset((0, 1)), 0.7 * kron_sites({0: x, 1: x}, 3)),
        LocalTerm(frozenset((1, 2)), 0.4 * kron_sites({1: y, 2: y}, 3)),
        LocalTerm(frozenset((0,)), 0.3 * kron_sites({0: z}, 3)),
        LocalTerm(frozenset((2,)), -0.2 * kron_sites({2: z}, 3)),
    )
    return sum((term.matrix for term in terms), np.zeros((8, 8), dtype=np.complex128)), terms


def check_bound() -> tuple[bool, float, float]:
    hamiltonian, terms = dense_local_model()
    region = frozenset((1,))
    local_scale = sum(
        float(np.linalg.norm(term.matrix, ord=2))
        for term in terms
        if term.support & region
    )
    bound = 2.0 * local_scale
    rng = np.random.default_rng(RNG_SEED)
    maximum_ratio = 0.0
    for _ in range(40):
        psi = normalize(rng.normal(size=8) + 1.0j * rng.normal(size=8))
        rho = np.outer(psi, psi.conj())
        derivative = -1.0j * (hamiltonian @ rho - rho @ hamiltonian)
        activity = trace_norm_hermitian(partial_trace(derivative, (1,), 3))
        maximum_ratio = max(maximum_ratio, activity / bound)
        if activity > bound + BOUND_TOL:
            return False, maximum_ratio, bound
    return True, maximum_ratio, bound


def check_stationary_witness() -> tuple[bool, float, float]:
    hamiltonian, terms = dense_local_model()
    touching = sum(
        (term.matrix for term in terms if 1 in term.support),
        np.zeros_like(hamiltonian),
    )
    _, eigenvectors = sla.eigh(hamiltonian)
    best_activity = math.inf
    best_local_energy = 0.0
    for column in range(eigenvectors.shape[1]):
        psi = eigenvectors[:, column]
        rho = np.outer(psi, psi.conj())
        derivative = -1.0j * (hamiltonian @ rho - rho @ hamiltonian)
        activity = trace_norm_hermitian(partial_trace(derivative, (1,), 3))
        local_energy = float(np.vdot(psi, touching @ psi).real)
        if abs(local_energy) > abs(best_local_energy):
            best_activity = activity
            best_local_energy = local_energy
    ok = best_activity <= WITNESS_TOL and abs(best_local_energy) > 1.0e-6
    return ok, best_activity, best_local_energy


def one_body_hamiltonian(n_sites: int, mass: float) -> np.ndarray:
    hamiltonian = np.zeros((n_sites, n_sites), dtype=np.complex128)
    signs = np.where(np.arange(n_sites) % 2 == 0, 1.0, -1.0)
    hamiltonian[np.arange(n_sites), np.arange(n_sites)] = mass * signs
    for site in range(n_sites - 1):
        hamiltonian[site, site + 1] = -0.5
        hamiltonian[site + 1, site] = -0.5
    return hamiltonian


def bond_activity(psi: np.ndarray, hamiltonian: np.ndarray) -> np.ndarray:
    derivative = -1.0j * hamiltonian @ psi
    out = np.empty(psi.size - 1, dtype=np.float64)
    for site in range(psi.size - 1):
        right = site + 1
        dp_left = 2.0 * float(np.real(np.conj(psi[site]) * derivative[site]))
        dp_right = 2.0 * float(np.real(np.conj(psi[right]) * derivative[right]))
        d_coherence = (
            derivative[site] * np.conj(psi[right])
            + psi[site] * np.conj(derivative[right])
        )
        d_rho = np.zeros((4, 4), dtype=np.complex128)
        d_rho[0, 0] = -(dp_left + dp_right)
        d_rho[1, 1] = dp_left
        d_rho[2, 2] = dp_right
        d_rho[1, 2] = d_coherence
        d_rho[2, 1] = np.conj(d_coherence)
        out[site] = trace_norm_hermitian(d_rho)
    return out


def bond_energy_density(psi: np.ndarray, mass: float) -> np.ndarray:
    probabilities = np.abs(psi) ** 2
    n_sites = psi.size
    signs = np.where(np.arange(n_sites) % 2 == 0, 1.0, -1.0)
    site_mass = mass * signs * probabilities
    degrees = np.ones(n_sites, dtype=np.float64)
    degrees[1:-1] = 2.0
    out = np.empty(n_sites - 1, dtype=np.float64)
    for site in range(n_sites - 1):
        right = site + 1
        hopping = float(
            (-0.5 * (np.conj(psi[site]) * psi[right] + np.conj(psi[right]) * psi[site])).real
        )
        out[site] = (
            site_mass[site] / degrees[site]
            + site_mass[right] / degrees[right]
            + hopping
        )
    return out


def overlap(left: np.ndarray, right: np.ndarray) -> float:
    x = np.asarray(left, dtype=np.float64)
    y = np.asarray(right, dtype=np.float64)
    if x.sum() <= 0.0 or y.sum() <= 0.0:
        return 0.0
    return float(np.sum(np.sqrt((x / x.sum()) * (y / y.sum()))))


def centroid(weights: np.ndarray) -> float:
    values = np.asarray(weights, dtype=np.float64)
    return float(np.dot(np.arange(values.size), values) / values.sum())


def check_empty_and_packet() -> tuple[bool, float, list[float], list[float]]:
    n_sites = 40
    mass = 0.3
    hamiltonian = one_body_hamiltonian(n_sites, mass)

    localized = np.zeros(n_sites, dtype=np.complex128)
    localized[2] = 1.0
    initial_activity = bond_activity(localized, hamiltonian)
    far_initial = float(np.max(initial_activity[8:]))

    eigenvalues, eigenvectors = sla.eigh(hamiltonian)
    positions = np.arange(n_sites, dtype=np.float64)
    packet = np.exp(-0.5 * ((positions - 12.0) / 3.0) ** 2).astype(np.complex128)
    packet *= np.exp(1.0j * (np.pi / 4.0) * positions)
    packet = normalize(packet)
    coefficients = eigenvectors.conj().T @ packet

    overlaps: list[float] = []
    centroid_deltas: list[float] = []
    for time_value in (0.0, 5.0, 10.0, 15.0):
        psi = eigenvectors @ (np.exp(-1.0j * eigenvalues * time_value) * coefficients)
        activity = bond_activity(psi, hamiltonian)
        energy = np.abs(bond_energy_density(psi, mass))
        overlaps.append(overlap(activity, energy))
        centroid_deltas.append(abs(centroid(activity) - centroid(energy)))

    ok = (
        far_initial <= WITNESS_TOL
        and min(overlaps) >= 0.6
        and max(centroid_deltas) <= 2.0
    )
    return ok, far_initial, overlaps, centroid_deltas


def run() -> tuple[list[str], int]:
    bound_ok, max_ratio, bound = check_bound()
    stationary_ok, stationary_activity, local_energy = check_stationary_witness()
    toy_ok, far_initial, overlaps, centroid_deltas = check_empty_and_packet()
    passed = bound_ok and stationary_ok and toy_ok

    lines = [
        (
            f"BOUND: pass={bound_ok} samples=40 max_activity_over_bound={max_ratio:.6g} "
            f"bound={bound:.6g}"
        ),
        (
            f"STATIONARY-WITNESS: pass={stationary_ok} activity={stationary_activity:.3e} "
            f"touching-term-energy={local_energy:.6g}"
        ),
        (
            f"FINITE-TOY-WITNESSES: pass={toy_ok} far_initial_activity={far_initial:.3e} "
            f"overlaps={[round(value, 6) for value in overlaps]} "
            f"centroid_deltas={[round(value, 6) for value in centroid_deltas]}"
        ),
        (
            "TOTAL: BOUNDED-TOY-SUPPORT-VALIDATED "
            "AO-bridge=supplied-premise finite-window-only"
            if passed
            else "TOTAL: MACHINERY-FAIL"
        ),
    ]
    return lines, 0 if passed else 1


def main() -> int:
    try:
        lines, exit_code = run()
    except Exception as exc:  # noqa: BLE001
        print(f"TOTAL: MACHINERY-FAIL {type(exc).__name__}: {exc}")
        return 1
    for line in lines:
        print(line)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
