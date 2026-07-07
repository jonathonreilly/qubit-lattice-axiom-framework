#!/usr/bin/env python3
"""Free-field domain-wall chiral edge check from an achiral Cl(3,0) bulk.

This runner tests four finite-matrix claims:

1. The native three-dimensional Pauli/Cl(3,0) lattice Weyl operator
       D(p) = i sum_i sigma_i sin(p_i)
   has the Nielsen-Ninomiya eight-corner doubling pattern, with net
   Brillouin-zone chirality zero.

2. A direct Wilson mass W(p) = r sum_i (1 - cos p_i) lifts seven corners
   but breaks the chiral anticommutation in the four-component chiral
   embedding. This is a consistency check with the foreclosed direct
   Wilson-removal route, not a re-attack on that route.

3. A record-time domain-wall Hamiltonian, using the standard Kaplan
   higher-dimensional Wilson-Dirac diagnostic, has one two-component Weyl
   species localized on the wall and the opposite species on the anti-wall.
   The modes are extracted from the actual low eigenspace and then localized
   by diagonalizing a wall-window operator inside that computed eigenspace.

4. The torus has one chiral species per wall and zero net chirality.

The calculation is deterministic and uses only numpy.
"""

from __future__ import annotations

import itertools
import math

import numpy as np

np.set_printoptions(precision=12, suppress=True, linewidth=140)

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"{tag} - {name}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def norm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A))


def anticommutator(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A @ B + B @ A


def periodic_distance(n: int, center: int) -> np.ndarray:
    x = np.arange(n)
    d = np.abs(x - center)
    return np.minimum(d, n - d)


def linear_fit_r2(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    slope, intercept = np.polyfit(x, y, 1)
    predicted = slope * x + intercept
    ss_res = float(np.sum((y - predicted) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0
    return float(slope), float(intercept), float(r2)


def fit_one_sided_localization_lengths(
    profile: np.ndarray,
    peak: int,
    max_distance: int = 8,
) -> tuple[float, float, float, float]:
    """Fit the two one-sided exponential tails around the measured peak."""
    n = len(profile)
    x = np.arange(1, max_distance + 1, dtype=float)
    right = np.array([profile[(peak + d) % n] for d in range(1, max_distance + 1)])
    left = np.array([profile[(peak - d) % n] for d in range(1, max_distance + 1)])
    left_slope, _, left_r2 = linear_fit_r2(x, np.log(left))
    right_slope, _, right_r2 = linear_fit_r2(x, np.log(right))
    left_xi = -2.0 / left_slope
    right_xi = -2.0 / right_slope
    return float(left_xi), float(right_xi), float(left_r2), float(right_r2)


# Pauli / Cl(3,0) generators.
I2 = np.eye(2, dtype=complex)
sigma_1 = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)
sigmas = [sigma_1, sigma_2, sigma_3]

# Four-component chiral extension used only to measure chiral breaking and
# to build the record-time domain-wall diagnostic.
tau_1 = sigma_1.copy()
tau_2 = sigma_2.copy()
tau_3 = sigma_3.copy()
I4 = np.eye(4, dtype=complex)
G_spatial = [np.kron(tau_1, s) for s in sigmas]
G_s = np.kron(tau_2, I2)
G_m = np.kron(tau_3, I2)
gamma_5 = G_m
edge_chirality = 1j * G_s @ G_m


def naive_cl3_operator(p: tuple[float, float, float]) -> np.ndarray:
    out = np.zeros((2, 2), dtype=complex)
    for i, p_i in enumerate(p):
        out += 1j * math.sin(p_i) * sigmas[i]
    return out


def chiral_embedded_naive_operator(p: tuple[float, float, float]) -> np.ndarray:
    out = np.zeros((4, 4), dtype=complex)
    for i, p_i in enumerate(p):
        out += 1j * math.sin(p_i) * G_spatial[i]
    return out


def wilson_weight(p: tuple[float, float, float], r: float = 1.0) -> float:
    return float(r * sum(1.0 - math.cos(p_i) for p_i in p))


def record_time_operators(n_s: int) -> tuple[np.ndarray, np.ndarray]:
    """Hermitian momentum K_s and Wilson Laplacian L_s on periodic record-time."""
    K = np.zeros((n_s, n_s), dtype=complex)
    L = np.zeros((n_s, n_s), dtype=complex)
    for s in range(n_s):
        K[s, (s + 1) % n_s] += -0.5j
        K[s, (s - 1) % n_s] += 0.5j
        L[s, s] += 1.0
        L[s, (s + 1) % n_s] += -0.5
        L[s, (s - 1) % n_s] += -0.5
    return K, L


def mass_profile(n_s: int, M: float) -> tuple[np.ndarray, int, int]:
    """Periodic wall/anti-wall profile: -M -> +M at wall, +M -> -M at anti-wall."""
    wall = n_s // 4
    anti_wall = wall + n_s // 2
    m = -M * np.ones(n_s, dtype=float)
    m[wall:anti_wall] = M
    return m, wall, anti_wall


def domain_wall_hamiltonian(
    p: tuple[float, float, float],
    n_s: int = 64,
    M: float = 0.8,
    r_space: float = 1.0,
    r_s: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, int, int]:
    """Finite Kaplan domain-wall Hamiltonian on T_s at fixed spatial momentum."""
    K, L = record_time_operators(n_s)
    m, wall, anti_wall = mass_profile(n_s, M)
    spatial_wilson_mass = wilson_weight(p, r_space)
    mass_matrix = np.diag(m + spatial_wilson_mass) + r_s * L

    H = np.kron(K, G_s) + np.kron(mass_matrix, G_m)
    for i, p_i in enumerate(p):
        H += np.kron(np.eye(n_s, dtype=complex), math.sin(p_i) * G_spatial[i])
    return H, m, wall, anti_wall


def localized_light_basis(
    H: np.ndarray,
    n_s: int,
    center: int,
    light_threshold: float = 1.0e-5,
    window_width: float = 2.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    evals, evecs = np.linalg.eigh(H)
    light = np.where(np.abs(evals) < light_threshold)[0]
    V = evecs[:, light]
    d = periodic_distance(n_s, center)
    window = np.exp(-((d / window_width) ** 2))
    W = np.kron(np.diag(window), I4)
    small = V.conj().T @ W @ V
    wvals, wvecs = np.linalg.eigh(small)
    order = np.argsort(wvals)[::-1]
    return evals, light, wvals[order], V @ wvecs[:, order]


def subspace_profile(U: np.ndarray, n_s: int, rank: int = 2) -> np.ndarray:
    profile = np.zeros(n_s, dtype=float)
    for k in range(rank):
        profile += np.sum(np.abs(U[:, k].reshape(n_s, 4)) ** 2, axis=1)
    return profile / rank


def subspace_chirality(U: np.ndarray, n_s: int, rank: int = 2) -> float:
    C = np.kron(np.eye(n_s, dtype=complex), edge_chirality)
    P = U[:, :rank]
    return float(np.real(np.trace(P.conj().T @ C @ P)) / rank)


def projected_velocity_data(U: np.ndarray, n_s: int, rank: int = 2) -> tuple[float, float, float]:
    P = U[:, :rank]
    velocities = [P.conj().T @ np.kron(np.eye(n_s, dtype=complex), G) @ P for G in G_spatial]
    square_error = max(norm(V @ V - np.eye(rank, dtype=complex)) for V in velocities)
    anticom_error = max(
        norm(velocities[i] @ velocities[j] + velocities[j] @ velocities[i])
        for i in range(3)
        for j in range(i + 1, 3)
    )
    handedness = float(np.real(np.trace(velocities[0] @ velocities[1] @ velocities[2]) / (2j)))
    return square_error, anticom_error, handedness


section("1. Naive Cl(3,0) operator has the Nielsen-Ninomiya eight-corner doubling")

N_SCAN = 16
grid = [2.0 * math.pi * k / N_SCAN for k in range(N_SCAN)]
zero_points: list[tuple[float, float, float]] = []
for p in itertools.product(grid, repeat=3):
    D = naive_cl3_operator(p)
    if max(abs(math.sin(x)) for x in p) < 1.0e-12 and norm(D) < 1.0e-12:
        zero_points.append(p)

expected_corners = list(itertools.product([0.0, math.pi], repeat=3))
corner_set = {tuple(round(x, 12) for x in p) for p in expected_corners}
found_set = {tuple(round(x, 12) for x in p) for p in zero_points}
chiralities = []
for p in zero_points:
    jac_det = math.prod(math.cos(p_i) for p_i in p)
    chiralities.append(1 if jac_det > 0 else -1)

check(
    "naive operator zeros occur exactly at p_i in {0, pi}",
    found_set == corner_set and len(zero_points) == 8,
    f"found={len(zero_points)} corners",
)
check(
    "naive BZ-corner chiralities sum to zero",
    sum(chiralities) == 0 and chiralities.count(1) == 4 and chiralities.count(-1) == 4,
    f"plus={chiralities.count(1)} minus={chiralities.count(-1)} sum={sum(chiralities)}",
)

section("2. Direct Wilson removal lifts doublers but breaks chiral anticommutation")

corner_singular_mins = []
for p in expected_corners:
    D4 = chiral_embedded_naive_operator(p)
    Dw = D4 + wilson_weight(p) * I4
    corner_singular_mins.append(float(np.min(np.linalg.svd(Dw, compute_uv=False))))

zero_after_wilson = sum(x < 1.0e-12 for x in corner_singular_mins)
p_test = (math.pi / 2.0, 0.0, 0.0)
D_test = chiral_embedded_naive_operator(p_test)
Dw_test = D_test + wilson_weight(p_test) * I4
naive_anticom_norm = norm(anticommutator(gamma_5, D_test))
wilson_anticom_norm = norm(anticommutator(gamma_5, Dw_test))

check(
    "Wilson scalar lifts seven of the eight naive corner zeros",
    zero_after_wilson == 1 and corner_singular_mins[0] < 1.0e-12 and min(corner_singular_mins[1:]) > 1.9,
    f"corner_min_singular={corner_singular_mins}",
)
check(
    "massless embedded operator anticommutes with gamma_5",
    naive_anticom_norm < 1.0e-12,
    f"||{{gamma_5,D}}||={naive_anticom_norm:.3e}",
)
check(
    "Wilson term breaks the gamma_5 anticommutation",
    wilson_anticom_norm > 1.0,
    f"||{{gamma_5,D+W}}||={wilson_anticom_norm:.6f}",
)

section("3. Record-time domain wall localizes one chiral Weyl species per wall")

N_S = 64
M = 0.8
H0, m, wall, anti_wall = domain_wall_hamiltonian((0.0, 0.0, 0.0), n_s=N_S, M=M)
evals, evecs = np.linalg.eigh(H0)
light = np.where(np.abs(evals) < 1.0e-5)[0]
next_gap = float(np.min(np.abs(evals[np.abs(evals) >= 1.0e-5])))

check("domain-wall Hamiltonian is Hermitian", norm(H0 - H0.conj().T) < 1.0e-12)
check(
    "periodic wall/anti-wall has four light spinor states at p=0",
    len(light) == 4 and next_gap > 0.5,
    f"light={len(light)} max|E_light|={np.max(np.abs(evals[light])):.3e} next_gap={next_gap:.6f}",
)

wall_evals, wall_light, wall_window, wall_basis = localized_light_basis(H0, N_S, wall)
anti_evals, anti_light, anti_window, anti_basis = localized_light_basis(H0, N_S, anti_wall)

check(
    "wall-localized light rank is two spin components, i.e. one Weyl species",
    wall_light.size == 4 and np.all(wall_window[:2] > 0.5) and np.all(wall_window[2:] < 1.0e-10),
    f"window_eigs={wall_window}",
)
check(
    "anti-wall-localized light rank is two spin components, i.e. one Weyl species",
    anti_light.size == 4 and np.all(anti_window[:2] > 0.5) and np.all(anti_window[2:] < 1.0e-10),
    f"window_eigs={anti_window}",
)

wall_profile = subspace_profile(wall_basis, N_S)
anti_profile = subspace_profile(anti_basis, N_S)
wall_peak = int(np.argmax(wall_profile))
anti_peak = int(np.argmax(anti_profile))
wall_left_xi, wall_right_xi, wall_left_r2, wall_right_r2 = fit_one_sided_localization_lengths(
    wall_profile, wall_peak
)
anti_left_xi, anti_right_xi, anti_left_r2, anti_right_r2 = fit_one_sided_localization_lengths(
    anti_profile, anti_peak
)
wall_leak = float(wall_profile[anti_wall] / np.max(wall_profile))
anti_leak = float(anti_profile[wall] / np.max(anti_profile))

check(
    "wall profile has exponential one-sided localization tails",
    wall_peak in {wall - 1, wall, wall + 1}
    and 0.2 < wall_left_xi < 2.5
    and 0.2 < wall_right_xi < 2.5
    and wall_left_r2 > 0.999999
    and wall_right_r2 > 0.999999
    and wall_leak < 1.0e-12,
    (
        f"peak={wall_peak} xi_left={wall_left_xi:.6f} xi_right={wall_right_xi:.6f} "
        f"r2=({wall_left_r2:.12f},{wall_right_r2:.12f}) antiwall_leak={wall_leak:.3e}"
    ),
)
check(
    "anti-wall profile has exponential one-sided localization tails",
    anti_peak in {anti_wall - 1, anti_wall, anti_wall + 1}
    and 0.2 < anti_left_xi < 2.5
    and 0.2 < anti_right_xi < 2.5
    and anti_left_r2 > 0.999999
    and anti_right_r2 > 0.999999
    and anti_leak < 1.0e-12,
    (
        f"peak={anti_peak} xi_left={anti_left_xi:.6f} xi_right={anti_right_xi:.6f} "
        f"r2=({anti_left_r2:.12f},{anti_right_r2:.12f}) wall_leak={anti_leak:.3e}"
    ),
)

wall_chi = subspace_chirality(wall_basis, N_S)
anti_chi = subspace_chirality(anti_basis, N_S)
wall_sqerr, wall_antierr, wall_hand = projected_velocity_data(wall_basis, N_S)
anti_sqerr, anti_antierr, anti_hand = projected_velocity_data(anti_basis, N_S)

check(
    "wall chirality is a definite eigenvalue fixed by sign(M)",
    abs(wall_chi - math.copysign(1.0, M)) < 1.0e-10,
    f"<chi_edge>={wall_chi:.12f}, sign(M)={math.copysign(1.0, M):.0f}",
)
check(
    "anti-wall chirality is opposite",
    abs(anti_chi + math.copysign(1.0, M)) < 1.0e-10,
    f"<chi_edge>={anti_chi:.12f}",
)
check(
    "wall projected spatial velocities form one Cl(3,0) Weyl cone",
    wall_sqerr < 1.0e-10 and wall_antierr < 1.0e-10 and abs(abs(wall_hand) - 1.0) < 1.0e-10,
    f"square_err={wall_sqerr:.3e} anticomm_err={wall_antierr:.3e} handedness={wall_hand:.0f}",
)
check(
    "anti-wall projected Weyl cone has opposite handedness",
    anti_sqerr < 1.0e-10
    and anti_antierr < 1.0e-10
    and abs(abs(anti_hand) - 1.0) < 1.0e-10
    and abs(wall_hand + anti_hand) < 1.0e-10,
    f"wall_hand={wall_hand:.0f} anti_hand={anti_hand:.0f}",
)

H_flip, _, wall_flip, anti_flip = domain_wall_hamiltonian((0.0, 0.0, 0.0), n_s=N_S, M=-M)
_, _, _, wall_flip_basis = localized_light_basis(H_flip, N_S, wall_flip)
_, _, _, anti_flip_basis = localized_light_basis(H_flip, N_S, anti_flip)
wall_flip_chi = subspace_chirality(wall_flip_basis, N_S)
anti_flip_chi = subspace_chirality(anti_flip_basis, N_S)
check(
    "flipping M flips wall and anti-wall chiralities",
    wall_flip_chi < -0.999999999 and anti_flip_chi > 0.999999999,
    f"M=-{M}: wall_chi={wall_flip_chi:.12f} anti_chi={anti_flip_chi:.12f}",
)

section("4. Bulk gap and index/count contrasts")

corner_light_counts = []
corner_min_gaps = []
for p in expected_corners:
    H_corner, _, _, _ = domain_wall_hamiltonian(p, n_s=N_S, M=M)
    e_corner = np.linalg.eigvalsh(H_corner)
    corner_light_counts.append(int(np.sum(np.abs(e_corner) < 1.0e-5)))
    corner_min_gaps.append(float(np.min(np.abs(e_corner))))

K_s, L_s = record_time_operators(N_S)
uniform_gaps = []
for sign in (-1.0, 1.0):
    uniform_mass = sign * M * np.ones(N_S)
    H_bulk = np.kron(K_s, G_s) + np.kron(np.diag(uniform_mass) + L_s, G_m)
    uniform_gaps.append(float(np.min(np.abs(np.linalg.eigvalsh(H_bulk)))))

check(
    "only the physical p=0 corner carries light domain-wall modes",
    corner_light_counts[0] == 4 and sum(corner_light_counts[1:]) == 0 and min(corner_min_gaps[1:]) > 0.7,
    f"light_counts={corner_light_counts} min_gaps={corner_min_gaps}",
)
check(
    "uniform record-time bulk is gapped by |M| with no edge light modes",
    min(uniform_gaps) > 0.7 and all(abs(g - abs(M)) < 1.0e-10 for g in uniform_gaps),
    f"uniform_gaps={uniform_gaps}",
)
check(
    "wall/anti-wall pair has one species per wall and net zero chirality on the torus",
    abs(wall_chi + anti_chi) < 1.0e-10 and abs(wall_hand + anti_hand) < 1.0e-10,
    f"species_count=2 walls=2 net_edge_chi={wall_chi + anti_chi:.3e} net_handedness={wall_hand + anti_hand:.3e}",
)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
