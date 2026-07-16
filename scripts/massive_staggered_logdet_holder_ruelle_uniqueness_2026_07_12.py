#!/usr/bin/env python3
"""Massive staggered log-det Hölder/Ruelle uniqueness certificate."""

from __future__ import annotations

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "MASSIVE_STAGGERED_LOGDET_HOLDER_RUELLE_INFINITE_TIME_UNIQUENESS_"
    "BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
TOL = 2.0e-10
PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


def haar_su3(rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    q = q @ np.diag(np.conj(phases) / np.abs(phases))
    return q / np.linalg.det(q) ** (1.0 / 3.0)


def identity_links(length_t: int, length_x: int) -> tuple[np.ndarray, np.ndarray]:
    shape = (length_t, length_x, 3, 3)
    temporal = np.broadcast_to(np.eye(3), shape).copy().astype(complex)
    spatial = temporal.copy()
    return temporal, spatial


def random_links(
    length_t: int, length_x: int, rng: np.random.Generator
) -> tuple[np.ndarray, np.ndarray]:
    temporal, spatial = identity_links(length_t, length_x)
    for time in range(length_t):
        for position in range(length_x):
            temporal[time, position] = haar_su3(rng)
            spatial[time, position] = haar_su3(rng)
    return temporal, spatial


def site_index(time: int, position: int, color: int, length_x: int) -> int:
    return (time * length_x + position) * 3 + color


def add_block(matrix: np.ndarray, left: int, right: int, block: np.ndarray) -> None:
    matrix[left : left + 3, right : right + 3] += block
    matrix[right : right + 3, left : left + 3] -= block.conj().T


def staggered_hop(
    temporal: np.ndarray,
    spatial: np.ndarray,
    *,
    antiperiodic: bool,
) -> np.ndarray:
    length_t, length_x = temporal.shape[:2]
    dimension = length_t * length_x * 3
    hop = np.zeros((dimension, dimension), dtype=complex)
    for time in range(length_t):
        for position in range(length_x):
            left = site_index(time, position, 0, length_x)

            next_time = (time + 1) % length_t
            right_t = site_index(next_time, position, 0, length_x)
            wrap_sign = -1.0 if antiperiodic and time == length_t - 1 else 1.0
            add_block(hop, left, right_t, 0.5 * wrap_sign * temporal[time, position])

            next_position = (position + 1) % length_x
            right_x = site_index(time, next_position, 0, length_x)
            eta_x = -1.0 if time % 2 else 1.0
            add_block(hop, left, right_x, 0.5 * eta_x * spatial[time, position])
    return hop


def epsilon_matrix(length_t: int, length_x: int) -> np.ndarray:
    values = []
    for time in range(length_t):
        for position in range(length_x):
            values.extend([(-1.0) ** (time + position)] * 3)
    return np.diag(values)


def matrix_function_hermitian(matrix: np.ndarray, function) -> np.ndarray:
    values, vectors = np.linalg.eigh((matrix + matrix.conj().T) / 2.0)
    return (vectors * function(values)) @ vectors.conj().T


def log_series(qmat: np.ndarray, degree: int, scale: float) -> np.ndarray:
    total = np.log(scale) * np.eye(qmat.shape[0], dtype=complex)
    power = np.eye(qmat.shape[0], dtype=complex)
    for order in range(1, degree + 1):
        power = power @ qmat
        total -= power / order
    return total


def inverse_series(qmat: np.ndarray, degree: int, scale: float) -> np.ndarray:
    total = np.eye(qmat.shape[0], dtype=complex)
    power = np.eye(qmat.shape[0], dtype=complex)
    for _ in range(1, degree + 1):
        power = power @ qmat
        total += power
    return total / scale


def time_block_trace(matrix: np.ndarray, time: int, length_x: int) -> float:
    start = time * length_x * 3
    stop = (time + 1) * length_x * 3
    return float(np.trace(matrix[start:stop, start:stop]).real)


def main() -> int:
    rng = np.random.default_rng(20260712)
    length_t, length_x = 8, 4
    temporal, spatial = random_links(length_t, length_x, rng)
    hop = staggered_hop(temporal, spatial, antiperiodic=True)
    epsilon = epsilon_matrix(length_t, length_x)
    hop_norm = float(np.linalg.norm(hop, 2))
    check(
        "Staggered hop is anti-Hermitian bipartite and obeys the four-dimensional norm envelope",
        np.linalg.norm(hop + hop.conj().T) < TOL
        and np.linalg.norm(epsilon @ hop + hop @ epsilon) < TOL
        and hop_norm <= 4.0 + TOL,
        f"anti-Hermitian={np.linalg.norm(hop + hop.conj().T):.3e}, "
        f"bipartite={np.linalg.norm(epsilon @ hop + hop @ epsilon):.3e}, ||M||={hop_norm:.6f}",
    )

    mass = 1.0
    dimension = hop.shape[0]
    dmat = mass * np.eye(dimension) + hop
    amat = dmat.conj().T @ dmat
    direct_a = mass**2 * np.eye(dimension) - hop @ hop
    scale = mass**2 + 16.0
    qmat = np.eye(dimension) - amat / scale
    qvalues = np.linalg.eigvalsh((qmat + qmat.conj().T) / 2.0)
    radius = 16.0 / scale
    check(
        "D dagger D has the exact massive range-two form and Q is a strict contraction",
        np.linalg.norm(amat - direct_a) < TOL
        and np.min(np.linalg.eigvalsh(amat)) >= mass**2 - TOL
        and np.max(np.linalg.eigvalsh(amat)) <= mass**2 + 16.0 + TOL
        and np.min(qvalues) >= -TOL
        and np.max(qvalues) <= radius + TOL
        and radius < 1.0,
        f"A identity={np.linalg.norm(amat-direct_a):.3e}, "
        f"spec(A)=[{np.min(np.linalg.eigvalsh(amat)):.6f},{np.max(np.linalg.eigvalsh(amat)):.6f}], "
        f"||Q||={np.max(qvalues):.6f}, universal r={radius:.6f}",
    )

    exact_log = matrix_function_hermitian(amat, np.log)
    log_errors = []
    for degree in (8, 32, 128, 512):
        approximate = log_series(qmat, degree, scale)
        log_errors.append(float(np.linalg.norm(approximate - exact_log, 2)))
    sign, direct_logdet = np.linalg.slogdet(dmat)
    spectral_logdet = 0.5 * float(np.trace(exact_log).real)
    check(
        "Positive determinant equals one half trace log and the exact Q series converges",
        abs(sign - 1.0) < TOL
        and abs(direct_logdet - spectral_logdet) < 2.0e-9
        and all(log_errors[index + 1] < log_errors[index] for index in range(3))
        and log_errors[-1] < 2.0e-10,
        f"logdet residual={abs(direct_logdet-spectral_logdet):.3e}, "
        f"series errors={','.join(f'{value:.3e}' for value in log_errors)}",
    )

    exact_inverse = np.linalg.inv(amat)
    inverse_errors = []
    for degree in (8, 32, 128, 512):
        approximate = inverse_series(qmat, degree, scale)
        inverse_errors.append(float(np.linalg.norm(approximate - exact_inverse, 2)))
    reconstructed_dirac_inverse = exact_inverse @ dmat.conj().T
    check(
        "The same strict-contraction series gives the quasilocal staggered inverse",
        all(
            inverse_errors[index + 1] < inverse_errors[index]
            for index in range(3)
        )
        and inverse_errors[-1] < 2.0e-10
        and np.linalg.norm(reconstructed_dirac_inverse - np.linalg.inv(dmat), 2)
        < 2.0e-10,
        f"A^-1 errors={','.join(f'{value:.3e}' for value in inverse_errors)}, "
        f"D^-1 residual={np.linalg.norm(reconstructed_dirac_inverse-np.linalg.inv(dmat),2):.3e}",
    )

    long_t = 24
    temporal_a, spatial_a = random_links(long_t, length_x, rng)
    temporal_b, spatial_b = random_links(long_t, length_x, rng)
    center = long_t // 2
    agreement_radius = 7
    for time in range(long_t):
        cyclic_distance = min((time - center) % long_t, (center - time) % long_t)
        if cyclic_distance <= agreement_radius:
            temporal_b[time] = temporal_a[time]
            spatial_b[time] = spatial_a[time]
    hop_a = staggered_hop(temporal_a, spatial_a, antiperiodic=True)
    hop_b = staggered_hop(temporal_b, spatial_b, antiperiodic=True)
    scale_local = mass**2 + 16.0
    qa = np.eye(hop_a.shape[0]) - (mass**2 * np.eye(hop_a.shape[0]) - hop_a @ hop_a) / scale_local
    qb = np.eye(hop_b.shape[0]) - (mass**2 * np.eye(hop_b.shape[0]) - hop_b @ hop_b) / scale_local
    local_polynomial_residuals = []
    power_a = np.eye(qa.shape[0], dtype=complex)
    power_b = np.eye(qb.shape[0], dtype=complex)
    for order in range(1, 4):
        power_a = power_a @ qa
        power_b = power_b @ qb
        local_polynomial_residuals.append(
            abs(
                time_block_trace(power_a, center, length_x)
                - time_block_trace(power_b, center, length_x)
            )
        )
    check(
        "Finite powers are exactly local before the agreement boundary",
        max(local_polynomial_residuals) < 2.0e-10,
        f"central block residuals Q^1..Q^3={','.join(f'{value:.3e}' for value in local_polynomial_residuals)}",
    )

    twist_differences = []
    inverse_differences = []
    for circumference in (8, 12, 16, 20):
        temporal_free, spatial_free = identity_links(circumference, length_x)
        hop_ap = staggered_hop(temporal_free, spatial_free, antiperiodic=True)
        hop_p = staggered_hop(temporal_free, spatial_free, antiperiodic=False)
        a_ap = mass**2 * np.eye(hop_ap.shape[0]) - hop_ap @ hop_ap
        a_p = mass**2 * np.eye(hop_p.shape[0]) - hop_p @ hop_p
        log_ap = matrix_function_hermitian(a_ap, np.log)
        log_p = matrix_function_hermitian(a_p, np.log)
        target = circumference // 2
        twist_differences.append(
            abs(
                time_block_trace(log_ap, target, length_x)
                - time_block_trace(log_p, target, length_x)
            )
        )
        d_ap = mass * np.eye(hop_ap.shape[0]) + hop_ap
        d_p = mass * np.eye(hop_p.shape[0]) + hop_p
        target_index = site_index(target, 0, 0, length_x)
        inverse_differences.append(
            abs(np.linalg.inv(d_ap)[target_index, target_index] - np.linalg.inv(d_p)[target_index, target_index])
        )
    check(
        "Antiperiodic seam influence decays away from the seam",
        twist_differences[-1] < twist_differences[0] * 0.02
        and inverse_differences[-1] < inverse_differences[0] * 0.02,
        f"log-density differences={','.join(f'{value:.3e}' for value in twist_differences)}, "
        f"inverse differences={','.join(f'{value:.3e}' for value in inverse_differences)}",
    )

    masses = (0.01, 0.1, 1.0, 10.0)
    radii = [16.0 / (value**2 + 16.0) for value in masses]
    check(
        "Every strictly positive mass gives an exponential Hölder radius below one",
        all(0.0 < value < 1.0 for value in radii),
        ", ".join(f"m={mass_value}:r={radius_value:.12f}" for mass_value, radius_value in zip(masses, radii)),
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    conditions = [
        "supplied Wilson-staggered dynamics",
        "strictly positive fermion mass",
        "fixed finite spatial volume",
        "unique infinite-time functional",
        "spatial thermodynamic limit",
        "controlled continuum, Standard Model, and GR limits",
    ]
    pairs = [
        f"| {conditions[left]} | {conditions[right]} |"
        for left in range(len(conditions))
        for right in range(left + 1, len(conditions))
    ]
    required = [
        "full-sequence infinite-time uniqueness",
        "log det D = (1/2) Tr log A",
        "Q=I-A/c",
        "compact two-slice gauge alphabet",
        "Ruelle--Perron--Frobenius",
        "antiperiodic seam",
        "does not derive the probability rule",
        "does not take the spatial thermodynamic limit",
        "No-Go Discipline N1--N8",
        "### N3 — hidden-condition phrase scan",
        "### N4 — citation/residual matching",
        "### N5 — rhetoric and resolution audit",
        "### N6 — partial-closure, convention, reframe, and primitive scan",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "Test and result",
        "Left closes right? | Right closes left? | Independent?",
        "| `we assume` |",
        "| `by construction` |",
        "| `as is standard` |",
        "| `the framework provides` |",
        "| `bridge context` |",
        "| `background` |",
        "| `naturally` |",
        "| `obviously` |",
        "| `standard QFT` |",
        "| `registered` |",
        "| `canonical` |",
        "Cited witness and location | Witness residual | Present residual | Match? | Disposition",
        "Statement / resolution | Tested? | Permitted conclusion",
        "Arbitrary nonlocal or degree-growing insertions | No",
        "Arbitrary boundary states with zero positive-eigenfunction overlap | No",
        "Spatial-volume-uniform family | No",
        "Retirement mechanism and applicability",
        "RPF theorem is external mathematical machinery",
        "no Ruelle spectral gap claimed",
        "trace-equivalent positive two-step spectral realization",
        "No observable-insertion intertwiner",
        "No axiom-update stop",
    ]
    missing = [item for item in required + pairs if item not in note_text]
    attempted = note_text.count("| `ATTEMPTED` |")
    directional_pairs = note_text.count("| No | No | Yes |")
    check(
        "Source-note boundary and N1-N8 contract",
        not missing and attempted >= 7 and directional_pairs >= 15,
        f"missing={missing}; attempted routes={attempted}; directional pairs={directional_pairs}",
    )

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
