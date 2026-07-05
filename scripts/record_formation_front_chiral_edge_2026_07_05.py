#!/usr/bin/env python3
"""Record-formation front as a free-field domain-wall diagnostic.

Step 1 imposed m(s) = M sign(s-s0). This runner replaces that by

    m(s) = M * (2 theta(s) - 1),

where theta(s) is an explicit monotone record-occupancy profile. On a finite
periodic record-time circle a rising formation front is accompanied by a
falling anti-front. The checks below focus on the rising front and use the
anti-front as an opposite-chirality contrast.

All physical claims are measured from diagonalizing the finite operator.
No randomness; numpy only.
"""

from __future__ import annotations

import sys

import numpy as np


np.set_printoptions(precision=12, suppress=True, linewidth=120)

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
    print(f"{tag}: {name}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def fro_norm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, ord="fro"))


I2 = np.eye(2, dtype=complex)
SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)
SIGMA = (SIGMA_X, SIGMA_Y, SIGMA_Z)

TAU_X = SIGMA_X.copy()
TAU_Y = SIGMA_Y.copy()
TAU_Z = SIGMA_Z.copy()


def anticommutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b + b @ a


def expit(z: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-z))


def smooth_step_a(x: np.ndarray, width: float) -> np.ndarray:
    return 0.5 * (1.0 + np.tanh(x / width))


def smooth_step_b(x: np.ndarray, width: float) -> np.ndarray:
    # Algebraically equivalent to smooth_step_a, but coded independently.
    return expit(2.0 * x / width)


def occupancy_profile_a(
    length: int,
    front: int,
    anti_front: int,
    width: float,
    *,
    reverse: bool = False,
) -> np.ndarray:
    s = np.arange(length, dtype=float)
    theta = smooth_step_a(s - front, width) - smooth_step_a(s - anti_front, width)
    theta = np.clip(theta, 0.0, 1.0)
    return 1.0 - theta if reverse else theta


def occupancy_profile_b(
    length: int,
    front: int,
    anti_front: int,
    width: float,
    *,
    reverse: bool = False,
) -> np.ndarray:
    s = np.arange(length, dtype=float)
    theta = smooth_step_b(s - front, width) - smooth_step_b(s - anti_front, width)
    theta = np.maximum(0.0, np.minimum(1.0, theta))
    return 1.0 - theta if reverse else theta


def shift_operators(length: int) -> tuple[np.ndarray, np.ndarray]:
    shift = np.zeros((length, length), dtype=complex)
    for s in range(length):
        shift[(s + 1) % length, s] = 1.0
    momentum = (shift - shift.conj().T) / (2j)
    wilson_laplacian = np.eye(length, dtype=complex) - 0.5 * (shift + shift.conj().T)
    return momentum, wilson_laplacian


def hamiltonian_a(
    theta: np.ndarray,
    p: tuple[float, float, float] = (0.0, 0.0, 0.0),
    *,
    mass: float = 1.0,
) -> np.ndarray:
    length = len(theta)
    ps, ws = shift_operators(length)
    mass_profile = mass * (2.0 * theta - 1.0)
    sigma_dot_p = sum(np.sin(p[i]) * SIGMA[i] for i in range(3))
    spatial_wilson = sum(1.0 - np.cos(pi) for pi in p)

    h = np.kron(np.eye(length, dtype=complex), np.kron(TAU_Z, sigma_dot_p))
    h += np.kron(ps, np.kron(TAU_Y, I2))
    h += np.kron(
        np.diag(mass_profile) + ws + spatial_wilson * np.eye(length, dtype=complex),
        np.kron(TAU_X, I2),
    )
    return h


def hamiltonian_b(
    theta: np.ndarray,
    p: tuple[float, float, float] = (0.0, 0.0, 0.0),
    *,
    mass: float = 1.0,
) -> np.ndarray:
    """Independent block assembly of the same finite operator."""
    length = len(theta)
    dim = 4 * length
    h = np.zeros((dim, dim), dtype=complex)
    mass_profile = mass * (2.0 * theta - 1.0)
    sigma_dot_p = sum(np.sin(p[i]) * SIGMA[i] for i in range(3))
    spatial_wilson = sum(1.0 - np.cos(pi) for pi in p)

    spatial_block = np.kron(TAU_Z, sigma_dot_p)
    record_momentum_block = np.kron(TAU_Y, I2)
    mass_block = np.kron(TAU_X, I2)

    for s in range(length):
        sl = slice(4 * s, 4 * (s + 1))
        h[sl, sl] += spatial_block
        h[sl, sl] += (mass_profile[s] + 1.0 + spatial_wilson) * mass_block

        sp = (s + 1) % length
        sm = (s - 1) % length
        slp = slice(4 * sp, 4 * (sp + 1))
        slm = slice(4 * sm, 4 * (sm + 1))
        h[slp, sl] += (1.0 / (2j)) * record_momentum_block - 0.5 * mass_block
        h[slm, sl] += (-1.0 / (2j)) * record_momentum_block - 0.5 * mass_block
    return h


def site_projector(length: int, sites: list[int]) -> np.ndarray:
    proj = np.zeros((4 * length, 4 * length), dtype=complex)
    for site in sites:
        s = site % length
        proj[4 * s : 4 * (s + 1), 4 * s : 4 * (s + 1)] = np.eye(4, dtype=complex)
    return proj


def site_profile(vec: np.ndarray, length: int) -> np.ndarray:
    return np.array([np.linalg.norm(vec[4 * s : 4 * (s + 1)]) ** 2 for s in range(length)])


def midpoint_near(theta: np.ndarray, center: int, radius: int) -> int:
    sites = [(center + d) % len(theta) for d in range(-radius, radius + 1)]
    return min(sites, key=lambda s: abs(float(theta[s]) - 0.5))


def localize_in_low_subspace(
    eigenvectors: np.ndarray,
    low_indices: np.ndarray,
    sites: list[int],
    n_states: int = 2,
) -> list[tuple[float, np.ndarray]]:
    length = eigenvectors.shape[0] // 4
    low_basis = eigenvectors[:, low_indices]
    projected = low_basis.conj().T @ site_projector(length, sites) @ low_basis
    weights, rotations = np.linalg.eigh(projected)
    order = np.argsort(weights)[::-1]
    out = []
    for idx in order[:n_states]:
        psi = low_basis @ rotations[:, idx]
        psi = psi / np.linalg.norm(psi)
        out.append((float(weights[idx].real), psi))
    return out


def fit_tail(profile: np.ndarray, peak: int, max_steps: int) -> tuple[float, float, float, int]:
    best = None
    length = len(profile)
    for direction in (+1, -1):
        xs = []
        ys = []
        for d in range(0, max_steps + 1):
            value = float(profile[(peak + direction * d) % length])
            if value > 1e-14:
                xs.append(float(d))
                ys.append(np.log(value))
        if len(xs) < 6:
            continue
        slope, intercept = np.polyfit(xs, ys, 1)
        fitted = slope * np.array(xs) + intercept
        denom = float(np.sum((np.array(ys) - np.mean(ys)) ** 2))
        r2 = 1.0 if denom < 1e-30 else 1.0 - float(np.sum((np.array(ys) - fitted) ** 2)) / denom
        candidate = (r2, len(xs), slope, direction)
        if best is None or candidate[0] > best[0]:
            best = candidate
    if best is None:
        return float("nan"), float("nan"), float("nan"), 0
    r2, _count, slope, direction = best
    probability_xi = -1.0 / slope if slope < 0.0 else float("inf")
    amplitude_xi = 2.0 * probability_xi
    return probability_xi, amplitude_xi, r2, direction


def analyze_front(
    *,
    length: int,
    front: int,
    anti_front: int,
    width: float,
    reverse: bool,
    center: int,
) -> dict[str, object]:
    theta = occupancy_profile_a(length, front, anti_front, width, reverse=reverse)
    h = hamiltonian_a(theta)
    evals, evecs = np.linalg.eigh(h)
    low_indices = np.where(np.abs(evals) < 1e-6)[0]
    if len(low_indices) != 4:
        low_indices = np.argsort(np.abs(evals))[:4]
    radius = max(8, int(np.ceil(4.0 * width)))
    sites = [s for s in range(center - radius, center + radius + 1)]
    localized = localize_in_low_subspace(evecs, low_indices, sites, 2)
    chirality_operator = np.kron(np.eye(length, dtype=complex), np.kron(TAU_Z, I2))
    chiralities = [float(np.vdot(psi, chirality_operator @ psi).real) for _w, psi in localized]
    profiles = [site_profile(psi, length) for _w, psi in localized]
    peaks = [int(np.argmax(profile)) for profile in profiles]
    midpoint = midpoint_near(theta, center, radius)
    gradient = float(theta[(center + 1) % length] - theta[(center - 1) % length])
    probability_xi, amplitude_xi, r2, tail_dir = fit_tail(
        profiles[0], peaks[0], max(12, int(np.ceil(4.0 * width)))
    )
    return {
        "theta": theta,
        "evals": evals,
        "low_indices": low_indices,
        "low_max": float(np.max(np.abs(evals[low_indices]))),
        "support": [w for w, _psi in localized],
        "chiralities": chiralities,
        "peaks": peaks,
        "midpoint": midpoint,
        "gradient": gradient,
        "probability_xi": probability_xi,
        "amplitude_xi": amplitude_xi,
        "r2": r2,
        "tail_dir": tail_dir,
        "states": localized,
    }


def projected_velocity_errors(states: list[tuple[float, np.ndarray]], length: int) -> tuple[float, list[np.ndarray]]:
    basis = np.column_stack([psi for _w, psi in states])
    velocities = []
    for sigma in SIGMA:
        op = np.kron(np.eye(length, dtype=complex), np.kron(TAU_Z, sigma))
        velocities.append(basis.conj().T @ op @ basis)
    max_error = 0.0
    for i in range(3):
        for j in range(3):
            target = 2.0 * np.eye(2, dtype=complex) if i == j else np.zeros((2, 2), dtype=complex)
            max_error = max(max_error, fro_norm(velocities[i] @ velocities[j] + velocities[j] @ velocities[i] - target))
    return max_error, velocities


def main() -> int:
    length = 96
    front = 32
    anti_front = 80
    widths = [0.75, 1.5, 3.0, 5.0, 8.0]

    section("0. Cl(3,0) and independent construction cross-check")
    cl3_ok = True
    for i in range(3):
        cl3_ok = cl3_ok and np.allclose(SIGMA[i] @ SIGMA[i], I2, atol=1e-12)
        for j in range(i + 1, 3):
            cl3_ok = cl3_ok and np.allclose(anticommutator(SIGMA[i], SIGMA[j]), 0.0, atol=1e-12)
    check("Pauli generators realize the Cl(3,0) spatial algebra", cl3_ok)

    theta_a = occupancy_profile_a(length, front, anti_front, 3.0)
    theta_b = occupancy_profile_b(length, front, anti_front, 3.0)
    h_a = hamiltonian_a(theta_a, p=(0.17, 0.11, -0.07))
    h_b = hamiltonian_b(theta_b, p=(0.17, 0.11, -0.07))
    check(
        "two independent occupancy constructions agree",
        float(np.max(np.abs(theta_a - theta_b))) < 1e-14,
        f"max|theta_A-theta_B|={float(np.max(np.abs(theta_a - theta_b))):.3e}",
    )
    check(
        "two independent Hamiltonian constructions agree",
        fro_norm(h_a - h_b) < 1e-12,
        f"||H_A-H_B||_F={fro_norm(h_a - h_b):.3e}",
    )

    section("1. Formation front localizes a chiral edge across front widths")
    xi_table = []
    representative = None
    for width in widths:
        result = analyze_front(
            length=length,
            front=front,
            anti_front=anti_front,
            width=width,
            reverse=False,
            center=front,
        )
        expected_chi = -float(np.sign(result["gradient"]))
        support_ok = all(s > 0.999 for s in result["support"])
        chirality_ok = all(abs(c - expected_chi) < 1e-9 for c in result["chiralities"])
        peak_ok = all(abs(p - result["midpoint"]) <= 1 for p in result["peaks"])
        loc_ok = np.isfinite(result["probability_xi"]) and result["probability_xi"] > 0.0 and result["r2"] > 0.98
        light_ok = len(result["low_indices"]) == 4 and result["low_max"] < 1e-6
        check(
            f"front width w={width:g}: edge is light, localized at occupancy midpoint, and chiral",
            light_ok and support_ok and chirality_ok and peak_ok and loc_ok,
            "grad={:+.6f}, midpoint_s={}, peaks={}, chi={}, prob_xi={:.6f}, R2={:.6f}".format(
                result["gradient"],
                result["midpoint"],
                result["peaks"],
                [round(c, 12) for c in result["chiralities"]],
                result["probability_xi"],
                result["r2"],
            ),
        )
        xi_table.append((width, result["probability_xi"], result["amplitude_xi"]))
        if width == 3.0:
            representative = result
    check(
        "localization length is measured for a range of front widths",
        all(np.isfinite(x[1]) and x[1] > 0.0 for x in xi_table) and xi_table[-1][1] > xi_table[0][1],
        "xi_prob(w)=" + ", ".join(f"{w:g}:{xi:.6f}" for w, xi, _amp in xi_table),
    )

    section("2. Formation-arrow sign flip")
    forward = representative
    reverse = analyze_front(
        length=length,
        front=front,
        anti_front=anti_front,
        width=3.0,
        reverse=True,
        center=front,
    )
    forward_mean_chi = float(np.mean(forward["chiralities"]))
    reverse_mean_chi = float(np.mean(reverse["chiralities"]))
    check(
        "reversing occupancy gradient flips the edge chirality",
        forward["gradient"] * reverse["gradient"] < 0.0
        and abs(forward_mean_chi + reverse_mean_chi) < 1e-9
        and abs(abs(reverse_mean_chi) - 1.0) < 1e-9,
        "forward_grad={:+.6f}, forward_chi={:+.1f}; reverse_grad={:+.6f}, reverse_chi={:+.1f}".format(
            forward["gradient"], forward_mean_chi, reverse["gradient"], reverse_mean_chi
        ),
    )

    anti = analyze_front(
        length=length,
        front=front,
        anti_front=anti_front,
        width=3.0,
        reverse=False,
        center=anti_front,
    )
    anti_mean_chi = float(np.mean(anti["chiralities"]))
    check(
        "periodic anti-front has the opposite chirality",
        forward["gradient"] * anti["gradient"] < 0.0 and abs(forward_mean_chi + anti_mean_chi) < 1e-9,
        "front_grad={:+.6f}, anti_grad={:+.6f}, front_chi={:+.1f}, anti_chi={:+.1f}".format(
            forward["gradient"], anti["gradient"], forward_mean_chi, anti_mean_chi
        ),
    )

    section("3. Uniform occupancy contrast")
    theta_empty = np.zeros(length, dtype=float)
    theta_full = np.ones(length, dtype=float)
    evals_empty = np.linalg.eigvalsh(hamiltonian_a(theta_empty))
    evals_full = np.linalg.eigvalsh(hamiltonian_a(theta_full))
    gap_empty = float(np.min(np.abs(evals_empty)))
    gap_full = float(np.min(np.abs(evals_full)))
    check(
        "uniform empty/full occupancy has no light edge and stays gapped",
        gap_empty > 0.99 and gap_full > 0.99 and np.count_nonzero(np.abs(evals_empty) < 1e-6) == 0,
        f"gap_empty={gap_empty:.12f}, gap_full={gap_full:.12f}",
    )

    section("4. Projected Cl(3,0) Weyl cone at the front")
    max_velocity_error, velocities = projected_velocity_errors(forward["states"], length)
    velocity_eigs = [np.linalg.eigvalsh(v) for v in velocities]
    check(
        "projected edge velocities obey the Pauli Clifford algebra",
        max_velocity_error < 1e-10
        and all(np.allclose(eigs, [-1.0, 1.0], atol=1e-10) for eigs in velocity_eigs),
        f"max_anticommutator_error={max_velocity_error:.3e}, velocity_eigs={velocity_eigs}",
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
