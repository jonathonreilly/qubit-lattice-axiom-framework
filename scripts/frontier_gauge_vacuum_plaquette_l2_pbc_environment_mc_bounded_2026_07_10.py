#!/usr/bin/env python3
"""Direct bounded Monte Carlo for actual L_s=2 PBC Wilson environment rho.

The marked plaquette Boltzmann factor is omitted.  All 24 spatial links are
sampled with the remaining 23-plaquette Wilson weight.  Character expectations
of the marked holonomy then give the actual finite-environment convolution
coefficients, not a single-link packet or injected positive witness.

This is stochastic bounded support, not a theorem-grade beta=6 evaluation.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

import frontier_gauge_vacuum_plaquette_environment_geometry_dependence_no_go_2026_07_10 as geometry_source
import frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute as single_link_source


BETA = 6.0
BURN_SWEEPS = 4000
SAMPLE_SWEEPS = 16000
THIN = 4
CHAINS = 4
STEP = 0.80
SEEDS = (71021, 71022, 71023, 71024)
CONTROL_SAMPLES = 12000


@dataclass
class ChainResult:
    samples: np.ndarray
    acceptance: float
    start: str


def haar_su3(rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    q = q @ np.diag(np.conj(phases) / np.abs(phases))
    det = np.linalg.det(q)
    q[:, 0] /= det
    return q


def su2_subgroup_proposal(rng: np.random.Generator, step: float) -> np.ndarray:
    pair = ((0, 1), (0, 2), (1, 2))[int(rng.integers(3))]
    axis = rng.normal(size=3)
    axis /= np.linalg.norm(axis)
    theta = rng.uniform(-step, step)
    a0 = np.cos(theta)
    a1, a2, a3 = np.sin(theta) * axis
    block = np.array(
        [[a0 + 1j * a3, a2 + 1j * a1], [-a2 + 1j * a1, a0 - 1j * a3]],
        dtype=complex,
    )
    out = np.eye(3, dtype=complex)
    i, j = pair
    out[np.ix_((i, j), (i, j))] = block
    return out


def plaquette_matrix(
    links: np.ndarray,
    link_index: dict[geometry_source.Link, int],
    plaquette: geometry_source.Plaquette,
    size: int,
) -> np.ndarray:
    out = np.eye(3, dtype=complex)
    for link, orientation in geometry_source.plaquette_boundary(plaquette, size):
        matrix = links[link_index[link]]
        out = out @ (matrix if orientation == 1 else matrix.conj().T)
    return out


def character_observables(marked_holonomy: np.ndarray) -> np.ndarray:
    trace = np.trace(marked_holonomy)
    chi_10 = trace
    chi_11 = abs(trace) ** 2 - 1.0
    chi_20 = trace**2 - np.conj(trace)
    return np.array([np.conj(chi_10) / 3.0, chi_11 / 8.0, np.conj(chi_20) / 6.0])


def run_chain(seed: int, hot_start: bool) -> ChainResult:
    rng = np.random.default_rng(seed)
    geometry = geometry_source.build_geometry(2)
    link_index = {link: index for index, link in enumerate(geometry.links)}
    active = [
        plaquette
        for index, plaquette in enumerate(geometry.plaquettes)
        if index != geometry.marked_index
    ]
    marked = geometry.plaquettes[geometry.marked_index]
    affected: dict[int, list[geometry_source.Plaquette]] = {i: [] for i in range(len(geometry.links))}
    for plaquette in active:
        for link, _ in geometry_source.plaquette_boundary(plaquette, 2):
            affected[link_index[link]].append(plaquette)

    if hot_start:
        links = np.array([haar_su3(rng) for _ in geometry.links])
        start = "hot"
    else:
        links = np.array([np.eye(3, dtype=complex) for _ in geometry.links])
        start = "cold"

    accepted = 0
    proposed = 0
    samples: list[np.ndarray] = []
    total_sweeps = BURN_SWEEPS + SAMPLE_SWEEPS
    for sweep in range(total_sweeps):
        for link_slot in rng.permutation(len(geometry.links)):
            local_plaquettes = affected[int(link_slot)]
            old_local = sum(
                float(np.trace(plaquette_matrix(links, link_index, plaquette, 2)).real)
                for plaquette in local_plaquettes
            )
            old_link = links[link_slot].copy()
            links[link_slot] = su2_subgroup_proposal(rng, STEP) @ old_link
            new_local = sum(
                float(np.trace(plaquette_matrix(links, link_index, plaquette, 2)).real)
                for plaquette in local_plaquettes
            )
            delta = (BETA / 3.0) * (new_local - old_local)
            proposed += 1
            if delta >= 0.0 or rng.random() < np.exp(delta):
                accepted += 1
            else:
                links[link_slot] = old_link
        if sweep >= BURN_SWEEPS and (sweep - BURN_SWEEPS) % THIN == 0:
            marked_holonomy = plaquette_matrix(links, link_index, marked, 2)
            samples.append(character_observables(marked_holonomy))
    return ChainResult(np.array(samples), accepted / proposed, start)


def batch_summary(results: list[ChainResult], batches_per_chain: int = 20) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    batch_means: list[np.ndarray] = []
    chain_means = np.array([np.mean(result.samples, axis=0) for result in results])
    for result in results:
        for batch in np.array_split(result.samples, batches_per_chain):
            batch_means.append(np.mean(batch, axis=0))
    batches = np.array(batch_means)
    mean = np.mean(batches, axis=0)
    real_error = np.std(batches.real, axis=0, ddof=1) / np.sqrt(len(batches))
    imag_error = np.std(batches.imag, axis=0, ddof=1) / np.sqrt(len(batches))
    error = real_error + 1j * imag_error
    return mean, error, chain_means


def haar_control(seed: int = 71020) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    values = []
    for _ in range(CONTROL_SAMPLES):
        holonomy = np.eye(3, dtype=complex)
        for _ in range(4):
            holonomy = holonomy @ haar_su3(rng)
        values.append(character_observables(holonomy))
    data = np.array(values)
    error = (
        np.std(data.real, axis=0, ddof=1)
        + 1j * np.std(data.imag, axis=0, ddof=1)
    ) / np.sqrt(len(data))
    return np.mean(data, axis=0), error


def main() -> int:
    print("=" * 78)
    print("L_s=2 PBC ACTUAL UNMARKED WILSON ENVIRONMENT: BOUNDED MC")
    print("=" * 78)
    print(
        f"beta={BETA:g}, chains={CHAINS}, burn={BURN_SWEEPS}, "
        f"sample_sweeps={SAMPLE_SWEEPS}, thin={THIN}, step={STEP}"
    )
    results = [run_chain(seed, hot_start=(index % 2 == 0)) for index, seed in enumerate(SEEDS)]
    mean, error, chain_means = batch_summary(results)
    control_mean, control_error = haar_control()
    c00 = single_link_source.wilson_character_coefficient_bessel(0, 0)
    single_link_rho_10 = single_link_source.rho_pq(1, 0, c00)

    labels = ("rho_(1,0)", "rho_(1,1)", "rho_(2,0)")
    for index, label in enumerate(labels):
        print(
            f"{label:12s} = {mean[index].real:+.9f} +/- {error[index].real:.9f} "
            f"  imag={mean[index].imag:+.3e} +/- {error[index].imag:.3e}"
        )
    print("acceptance by chain = " + ", ".join(f"{r.acceptance:.4f} ({r.start})" for r in results))
    print("chain rho_(1,0) means = " + ", ".join(f"{x[0].real:.7f}" for x in chain_means))
    print(f"single-link packet rho_(1,0) comparator = {single_link_rho_10:.9f}")
    print(
        "actual-environment minus single-link difference = "
        f"{mean[0].real - single_link_rho_10:+.9f} "
        f"({abs(mean[0].real - single_link_rho_10) / error[0].real:.1f} declared batch-diagnostic error units)"
    )
    print()
    print("beta=0 independent-Haar control")
    for index, label in enumerate(labels):
        print(
            f"{label:12s} = {control_mean[index].real:+.3e} +/- {control_error[index].real:.3e} "
            f"  imag={control_mean[index].imag:+.3e} +/- {control_error[index].imag:.3e}"
        )

    failures = 0
    acceptance_ok = all(0.25 < result.acceptance < 0.9 for result in results)
    control_ok = all(
        abs(control_mean[i].real) < 4.0 * max(control_error[i].real, 1.0e-12)
        and abs(control_mean[i].imag) < 4.0 * max(control_error[i].imag, 1.0e-12)
        for i in range(3)
    )
    imag_ok = all(abs(mean[i].imag) < 4.0 * max(error[i].imag, 1.0e-12) for i in range(3))
    chain_spread = float(np.max(chain_means[:, 0].real) - np.min(chain_means[:, 0].real))
    chain_ok = chain_spread < 8.0 * float(error[0].real)
    signal_ok = float(mean[0].real) > 5.0 * float(error[0].real)
    discrimination_ok = abs(float(mean[0].real) - single_link_rho_10) > 20.0 * float(error[0].real)
    for name, condition in (
        ("proposal acceptance is in the declared heuristic diagnostic window", acceptance_ok),
        ("beta=0 Haar controls are consistent with zero", control_ok),
        ("charge-conjugation imaginary parts are consistent with zero", imag_ok),
        ("independent hot/cold chain means agree within the bounded diagnostic", chain_ok),
        ("the actual L_s=2 PBC fundamental coefficient passes the declared nonzero-signal heuristic", signal_ok),
        ("the coupled environment is strongly distinguished from the single-link packet under the bounded diagnostic", discrimination_ok),
    ):
        status = "PASS" if condition else "FAIL"
        failures += 0 if condition else 1
        print(f"[{status}] {name}")
    print()
    print("BOUNDARY: stochastic finite-volume support; no all-weight, thermodynamic, or stripping closure")
    print(f"SUMMARY: PASS={6 - failures} FAIL={failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
