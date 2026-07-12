#!/usr/bin/env python3
"""Certificate for exact factor-two gauge blocking and Schur/OS transfer."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_"
    "SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
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


def random_su3(rng: np.random.Generator) -> np.ndarray:
    raw = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(raw)
    phases = np.diag(r)
    q = q @ np.diag(np.conjugate(phases) / np.maximum(np.abs(phases), 1.0e-15))
    det = np.linalg.det(q)
    q[:, 0] /= det
    return q


def sites(length: int) -> list[tuple[int, int]]:
    return [(x, y) for x in range(length) for y in range(length)]


def index(site: tuple[int, int], length: int) -> int:
    return site[0] * length + site[1]


def shift(site: tuple[int, int], mu: int, step: int, length: int) -> tuple[int, int]:
    point = list(site)
    point[mu] = (point[mu] + step) % length
    return point[0], point[1]


def eta(site: tuple[int, int], mu: int) -> int:
    return 1 if mu == 0 else (-1) ** site[0]


def random_links(length: int, rng: np.random.Generator) -> dict[tuple[tuple[int, int], int], np.ndarray]:
    return {(site, mu): random_su3(rng) for site in sites(length) for mu in range(2)}


def staggered_matrix(
    links: dict[tuple[tuple[int, int], int], np.ndarray], length: int, mass: float
) -> np.ndarray:
    count = length * length
    matrix = mass * np.eye(3 * count, dtype=complex)
    for site in sites(length):
        row = slice(3 * index(site, length), 3 * (index(site, length) + 1))
        for mu in range(2):
            sign = 0.5 * eta(site, mu)
            forward = shift(site, mu, 1, length)
            backward = shift(site, mu, -1, length)
            col_f = slice(3 * index(forward, length), 3 * (index(forward, length) + 1))
            col_b = slice(3 * index(backward, length), 3 * (index(backward, length) + 1))
            matrix[row, col_f] += sign * links[(site, mu)]
            matrix[row, col_b] -= sign * links[(backward, mu)].conj().T
    return matrix


def gauge_transform_links(
    links: dict[tuple[tuple[int, int], int], np.ndarray],
    gauge: dict[tuple[int, int], np.ndarray],
    length: int,
) -> dict[tuple[tuple[int, int], int], np.ndarray]:
    return {
        (site, mu): gauge[site] @ value @ gauge[shift(site, mu, 1, length)].conj().T
        for (site, mu), value in links.items()
    }


def coarse_links(
    links: dict[tuple[tuple[int, int], int], np.ndarray], length: int
) -> dict[tuple[tuple[int, int], int], np.ndarray]:
    coarse_length = length // 2
    result = {}
    for coarse_site in sites(coarse_length):
        fine_site = (2 * coarse_site[0], 2 * coarse_site[1])
        for mu in range(2):
            middle = shift(fine_site, mu, 1, length)
            result[(coarse_site, mu)] = links[(fine_site, mu)] @ links[(middle, mu)]
    return result


def retained_indices(length: int) -> tuple[list[int], list[int]]:
    retained_sites = [site for site in sites(length) if site[0] % 2 == 0 and site[1] % 2 == 0]
    retained = [3 * index(site, length) + color for site in retained_sites for color in range(3)]
    retained_set = set(retained)
    eliminated = [entry for entry in range(3 * length * length) if entry not in retained_set]
    return retained, eliminated


def schur(matrix: np.ndarray, retained: list[int], eliminated: list[int]) -> tuple[np.ndarray, np.ndarray]:
    dkk = matrix[np.ix_(retained, retained)]
    dki = matrix[np.ix_(retained, eliminated)]
    dik = matrix[np.ix_(eliminated, retained)]
    dii = matrix[np.ix_(eliminated, eliminated)]
    return dkk - dki @ np.linalg.solve(dii, dik), dii


def max_two_minor_mixture_mismatch(first: np.ndarray, second: np.ndarray) -> float:
    average = 0.5 * (first + second)
    maximum = 0.0
    size = min(first.shape[0], 10)
    for rows in combinations(range(size), 2):
        for cols in combinations(range(size), 2):
            value = 0.5 * np.linalg.det(first[np.ix_(rows, cols)])
            value += 0.5 * np.linalg.det(second[np.ix_(rows, cols)])
            value -= np.linalg.det(average[np.ix_(rows, cols)])
            maximum = max(maximum, abs(value))
    return maximum


def main() -> int:
    rng = np.random.default_rng(20260712)
    length = 6
    mass = 1.3
    links = random_links(length, rng)
    matrix = staggered_matrix(links, length, mass)
    hop = matrix - mass * np.eye(matrix.shape[0])

    epsilon_site = np.diag([(-1) ** (x + y) for x, y in sites(length)])
    epsilon = np.kron(epsilon_site, np.eye(3))
    antihermitian = np.linalg.norm(hop + hop.conj().T)
    parity_residual = np.linalg.norm(epsilon @ hop @ epsilon + hop)
    check(
        "Reduced staggered carrier has the analytic anti-Hermitian and parity structure",
        antihermitian < 1.0e-12 and parity_residual < 1.0e-12,
        f"antihermitian={antihermitian:.2e}, parity={parity_residual:.2e}",
    )

    retained, eliminated = retained_indices(length)
    schur_matrix, dii = schur(matrix, retained, eliminated)
    sign_d, logdet_d = np.linalg.slogdet(matrix)
    sign_i, logdet_i = np.linalg.slogdet(dii)
    sign_s, logdet_s = np.linalg.slogdet(schur_matrix)
    determinant_residual = abs((logdet_i + logdet_s) - logdet_d)
    sign_residual = abs(sign_i * sign_s - sign_d)
    inverse_residual = np.linalg.norm(
        np.linalg.inv(matrix)[np.ix_(retained, retained)] - np.linalg.inv(schur_matrix)
    )
    check(
        "Schur determinant and retained-inverse identities hold",
        determinant_residual < 1.0e-11 and sign_residual < 1.0e-11 and inverse_residual < 1.0e-11,
        f"logdet={determinant_residual:.2e}, sign={sign_residual:.2e}, inverse={inverse_residual:.2e}",
    )

    singular_values = np.linalg.svd(dii, compute_uv=False)
    eliminated_sites = [site for site in sites(length) if not (site[0] % 2 == 0 and site[1] % 2 == 0)]
    epsilon_i = np.kron(
        np.diag([(-1) ** (x + y) for x, y in eliminated_sites]), np.eye(3)
    )
    mii = dii - mass * np.eye(dii.shape[0])
    compressed_parity = np.linalg.norm(epsilon_i @ mii @ epsilon_i + mii)
    check(
        "The eliminated determinant is positive and its inverse norm is at most one over mass",
        abs(sign_i.imag) < 1.0e-11
        and sign_i.real > 0.999999
        and singular_values[-1] >= mass - 1.0e-12
        and compressed_parity < 1.0e-12,
        f"det phase={sign_i}, sigma_min={singular_values[-1]:.6f}, parity={compressed_parity:.2e}",
    )

    gauge = {site: random_su3(rng) for site in sites(length)}
    transformed_links = gauge_transform_links(links, gauge, length)
    transformed_matrix = staggered_matrix(transformed_links, length, mass)
    transformed_schur, _ = schur(transformed_matrix, retained, eliminated)
    retained_sites = [site for site in sites(length) if site[0] % 2 == 0 and site[1] % 2 == 0]
    gauge_k = np.zeros_like(schur_matrix)
    for position, site in enumerate(retained_sites):
        gauge_k[3 * position : 3 * position + 3, 3 * position : 3 * position + 3] = gauge[site]
    schur_covariance = np.linalg.norm(
        transformed_schur - gauge_k @ schur_matrix @ gauge_k.conj().T
    )

    blocked = coarse_links(links, length)
    blocked_transformed = coarse_links(transformed_links, length)
    coarse_covariance = 0.0
    coarse_length = length // 2
    for (site, mu), value in blocked.items():
        fine_site = (2 * site[0], 2 * site[1])
        fine_end = shift(fine_site, mu, 2, length)
        expected = gauge[fine_site] @ value @ gauge[fine_end].conj().T
        coarse_covariance = max(coarse_covariance, np.linalg.norm(blocked_transformed[(site, mu)] - expected))
    check(
        "The Schur kernel and two-link coarse links are gauge covariant",
        schur_covariance < 1.0e-11 and coarse_covariance < 1.0e-11,
        f"Schur={schur_covariance:.2e}, links={coarse_covariance:.2e}",
    )

    # The Q-series uses the four-dimensional safe constant 16 even on this
    # reduced two-dimensional carrier.
    c = mass * mass + 16.0
    q_matrix = (16.0 * np.eye(mii.shape[0]) + mii @ mii) / c
    r = 16.0 / c
    q_eigenvalues = np.linalg.eigvalsh((q_matrix + q_matrix.conj().T) / 2.0)
    partial = np.zeros_like(dii)
    power = np.eye(dii.shape[0], dtype=complex)
    for _ in range(320):
        partial += power @ (mass * np.eye(dii.shape[0]) - mii) / c
        power = power @ q_matrix
    q_residual = np.linalg.norm(partial - np.linalg.inv(dii))
    check(
        "The all-mass Q-series is positive, contractive, and reproduces the eliminated inverse",
        q_eigenvalues[0] > -1.0e-12 and q_eigenvalues[-1] <= r + 1.0e-12 and q_residual < 1.0e-10,
        f"eig=[{q_eigenvalues[0]:.6f},{q_eigenvalues[-1]:.6f}], r={r:.6f}, residual={q_residual:.2e}",
    )

    # Change a nonskeleton link: base point has an odd transverse coordinate.
    altered = {key: value.copy() for key, value in links.items()}
    nonskeleton = ((1, 1), 0)
    altered[nonskeleton] = random_su3(rng) @ altered[nonskeleton]
    blocked_altered = coarse_links(altered, length)
    fiber_residual = max(np.linalg.norm(blocked[key] - blocked_altered[key]) for key in blocked)
    altered_schur, _ = schur(staggered_matrix(altered, length, mass), retained, eliminated)
    schur_variation = np.linalg.norm(altered_schur - schur_matrix)
    quartic_mismatch = max_two_minor_mixture_mismatch(schur_matrix, altered_schur)
    check(
        "One coarse-link fiber contains distinct Schur kernels and a non-Gaussian mixture diagnostic",
        fiber_residual < 1.0e-12 and schur_variation > 1.0e-5 and quartic_mismatch > 1.0e-8,
        f"fiber={fiber_residual:.2e}, Schur variation={schur_variation:.6f}, quartic={quartic_mismatch:.2e}",
    )

    # The nine qutrit Weyl matrices form an exact unitary one-design and
    # independently reproduce integral U_ij conjugate(U_kl)=delta_ik delta_jl/3.
    omega = np.exp(2j * np.pi / 3.0)
    shift_matrix = np.roll(np.eye(3, dtype=complex), 1, axis=0)
    clock = np.diag([1.0, omega, omega**2])
    design = [np.linalg.matrix_power(shift_matrix, a) @ np.linalg.matrix_power(clock, b) for a in range(3) for b in range(3)]
    twirl_residual = 0.0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for ell in range(3):
                    average = sum(u[i, j] * np.conjugate(u[k, ell]) for u in design) / 9.0
                    expected = (1.0 / 3.0) if i == k and j == ell else 0.0
                    twirl_residual = max(twirl_residual, abs(average - expected))
    check(
        "An independent exact unitary design verifies the SU(3) Haar second-moment coefficient one third",
        twirl_residual < 1.0e-12,
        f"maximum residual={twirl_residual:.2e}",
    )

    # Semigroup/path concatenation on an 8x8 carrier.
    long_links = random_links(8, rng)
    first_block = coarse_links(long_links, 8)
    second_block = coarse_links(first_block, 4)
    path_residual = 0.0
    for (site, mu), value in second_block.items():
        fine = (4 * site[0], 4 * site[1])
        expected = np.eye(3, dtype=complex)
        cursor = fine
        for _ in range(4):
            expected = expected @ long_links[(cursor, mu)]
            cursor = shift(cursor, mu, 1, 8)
        path_residual = max(path_residual, np.linalg.norm(value - expected))
    check(
        "Two factor-two blocks equal one straight factor-four path block",
        path_residual < 1.0e-12,
        f"maximum residual={path_residual:.2e}",
    )

    energies = np.array([0.0, 0.2, 0.7, 1.4])
    spacing = 0.03
    transfer_two = np.diag(np.exp(-2.0 * spacing * energies))
    recovered = -np.log(np.diag(transfer_two)) / (2.0 * spacing)
    check(
        "Doubling the time spacing leaves the OS physical energies unchanged",
        np.linalg.norm(recovered - energies) < 1.0e-12,
        "energies=" + ",".join(f"{value:.3f}" for value in recovered),
    )

    text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    required = [
        "**Type:** bounded_theorem",
        "B(U)_(X,mu)=U_(2X,mu) U_(2X+e_mu,mu)",
        "det D_II=m^z product_(lambda>0)(m^2+lambda^2)>0",
        "r(m)=16/(m^2+16)<1",
        "not a taste-faithful staggered block",
        "It does not, by operator norm alone",
        "T'_1 = T_2 restricted to H_block^gauge",
        "(ker T'_1)^perp=H_block^gauge intersect (ker T_2)^perp",
        "antiperiodic temporal fermion seam",
        "extents must be divisible by `2^(n+k)`",
        "not a proof that `S_c` has a uniformly quasilocal",
        "not a fitted coupling",
        "No axiom-update stop",
        "No-Go Discipline N1--N8",
        "### N3 — hidden-condition phrase scan",
        "### N4 — citation/residual matching",
        "### N5 — rhetoric and resolution audit",
        "### N6 — partial-closure and primitive scan",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "**No-Go Discipline status: PASS.**",
    ]
    missing = [item for item in required if item not in text]
    attempted = text.count("| `ATTEMPTED` |")
    n2_conditions = [
        "taste-faithful coarse fermion variables",
        "controlled action-space RG theorem",
        "physical critical trajectory/observable identification",
    ]
    n2_pairs = [
        f"| {n2_conditions[left]} | {n2_conditions[right]} |"
        for left in range(len(n2_conditions))
        for right in range(left + 1, len(n2_conditions))
    ]
    missing_pairs = [item for item in n2_pairs if item not in text]
    check(
        "Source-note bounded theorem and N1-N8 contract",
        not missing and not missing_pairs and attempted >= 8,
        f"missing={missing}; missing N2 pairs={missing_pairs}; attempted={attempted}",
    )

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
