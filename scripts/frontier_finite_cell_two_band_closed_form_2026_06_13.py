#!/usr/bin/env python3
"""Finite-cell two-band Peierls closed-form verifier.

Companion draft:
    docs/FINITE_CELL_TWO_BAND_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-13.md

This runner keeps the supplied finite Harper cell fixed at Q=24, Ly=2 and
computes the B^2 grand-potential response as an explicit finite momentum sum.

Run:
    python3 scripts/frontier_finite_cell_two_band_closed_form_2026_06_13.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np
from numpy.polynomial.legendre import leggauss


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "FINITE_CELL_TWO_BAND_CLOSED_FORM_BOUNDED_THEOREM_NOTE_2026-06-13.md"

T_HOP = 1.0
CELL_Q = 24
LY = 2
N_SITE = CELL_Q * LY
MU = 1.7086
TEMP = 0.2
GL_ORDER = 12
MASSES = (0.0, 0.2, 0.3, 0.5)

# Frozen before running any result gates.
CLOSED_FORM_TOL = 1.0e-10
FINITE_DIFF_FINE_ABS = 3.0e-5
FINITE_DIFF_RATIO_MIN = 3.5
INTERBAND_MIN = 1.0e-6
MOYAL_MONOTONE_MIN_RATE = 3.0
MOYAL_RATE_DENOM_FLOOR = 1.0e-15

PASS_COUNT = 0
FAIL_COUNT = 0


@dataclass(frozen=True)
class ResponseParts:
    full: float
    intraband: float
    interband: float


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def gl_average_nodes_weights(n: int) -> tuple[np.ndarray, np.ndarray]:
    nodes, weights = leggauss(n)
    return math.pi * nodes, 0.5 * weights


def grand_kernel(energy: np.ndarray, mu: float = MU, temp: float = TEMP) -> np.ndarray:
    return -temp * np.logaddexp(0.0, -(energy - mu) / temp)


def fermi_occupation(energy: np.ndarray, mu: float = MU, temp: float = TEMP) -> np.ndarray:
    z = np.clip((energy - mu) / temp, -60.0, 60.0)
    return 1.0 / (1.0 + np.exp(z))


def grand_kernel_second_derivative(
    energy: np.ndarray, mu: float = MU, temp: float = TEMP
) -> np.ndarray:
    f = fermi_occupation(energy, mu, temp)
    return -f * (1.0 - f) / temp


def finite_position_sums(q: int) -> tuple[np.ndarray, float]:
    """Return exact finite Fourier sums for x and the diagonal x^2 sum.

    X[n,m] = Q^{-1} sum_x x exp(i 2 pi (m-n) x/Q).  The x^2 diagonal is
    Q^{-1} sum_x x^2, independent of the momentum label.
    """

    r = np.arange(q, dtype=np.float64)
    delta = np.arange(q, dtype=np.float64)
    phases = np.exp(2.0j * math.pi * np.outer(delta, r) / q)
    s1 = (phases @ r) / q
    s2 = (phases @ (r * r)) / q
    index_delta = (np.arange(q)[None, :] - np.arange(q)[:, None]) % q
    return s1[index_delta], float(np.real(s2[0]))


def block_eigensystem(epsilon: np.ndarray, mass: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Diagonalize the Q two-band blocks [[eps,m],[m,-eps]]."""

    q = epsilon.size
    energies = np.empty((q, 2), dtype=np.float64)
    avec = np.empty((q, 2), dtype=np.float64)
    bvec = np.empty((q, 2), dtype=np.float64)
    for i, eps in enumerate(epsilon):
        vals, vec = np.linalg.eigh(np.array([[eps, mass], [mass, -eps]], dtype=np.float64))
        energies[i] = vals
        avec[i] = vec[0]
        bvec[i] = vec[1]
    return energies, avec, bvec


def finite_cell_closed_form_point(
    q: int,
    kx_twist: float,
    ky_twist: float,
    mass: float,
    x_matrix: np.ndarray,
    x2_diag: float,
) -> ResponseParts:
    """Per-twist finite-cell closed form.

    The B=0 Hamiltonian is a direct sum of Q two-band blocks.  The Peierls
    first and second variations are exact finite Fourier sums of x and x^2.
    """

    n = np.arange(q)
    py = 0.5 * ky_twist
    px = (kx_twist + 2.0 * math.pi * n) / q
    epsilon = -2.0 * T_HOP * (np.cos(px) + np.cos(py))
    energies, avec, bvec = block_eigensystem(epsilon, mass)

    flat_e = energies.ravel()
    flat_a = avec.ravel()
    flat_b = bvec.ravel()
    flat_n = np.repeat(n, 2)

    y_first = 2.0 * math.sin(py)
    y_second = math.cos(py)
    h2_diag = y_second * x2_diag * (flat_a * flat_a - flat_b * flat_b)

    contrast = flat_a[:, None] * flat_a[None, :] - flat_b[:, None] * flat_b[None, :]
    h1_abs2 = (
        (y_first * y_first)
        * np.abs(x_matrix[flat_n[:, None], flat_n[None, :]]) ** 2
        * (contrast * contrast)
    )

    fprime = fermi_occupation(flat_e)
    fsecond = grand_kernel_second_derivative(flat_e)
    diff = flat_e[:, None] - flat_e[None, :]
    fprime_diff = fprime[:, None] - fprime[None, :]

    kernel = np.empty_like(diff)
    offdiag = np.abs(diff) > 1.0e-10
    kernel[offdiag] = fprime_diff[offdiag] / diff[offdiag]
    degenerate_limit = 0.5 * (fsecond[:, None] + fsecond[None, :])
    kernel[~offdiag] = degenerate_limit[~offdiag]

    h1_term = kernel * h1_abs2
    seagull = 2.0 * float(np.sum(fprime * h2_diag))
    full = seagull + float(np.sum(h1_term))
    interband_mask = (np.sign(flat_e)[:, None] * np.sign(flat_e)[None, :]) < 0.0
    interband = float(np.sum(h1_term[interband_mask]))
    return ResponseParts(full=full, intraband=full - interband, interband=interband)


def finite_cell_closed_form_response(q: int, mass: float, gl_order: int = GL_ORDER) -> ResponseParts:
    x_matrix, x2_diag = finite_position_sums(q)
    nodes, weights = gl_average_nodes_weights(gl_order)
    total = np.zeros(3, dtype=np.float64)
    for ix, kx in enumerate(nodes):
        for iy, ky in enumerate(nodes):
            weight = weights[ix] * weights[iy] / (q * LY)
            part = finite_cell_closed_form_point(q, kx, ky, mass, x_matrix, x2_diag)
            total += weight * np.array([part.full, part.intraband, part.interband])
    return ResponseParts(full=float(total[0]), intraband=float(total[1]), interband=float(total[2]))


SITE_SIGNS = np.array(
    [1.0 if (x + y) % 2 == 0 else -1.0 for x in range(CELL_Q) for y in range(LY)]
)


def site_index(x: int, y: int) -> int:
    return (x % CELL_Q) * LY + (y % LY)


def harper_matrix(kx: float, ky: float, b_field: float, mass: float) -> np.ndarray:
    h = np.zeros((N_SITE, N_SITE), dtype=np.complex128)
    h[np.diag_indices(N_SITE)] = mass * SITE_SIGNS
    exp_kx = np.exp(1j * kx)
    exp_ky = np.exp(1j * ky)

    for x in range(CELL_Q):
        for y in range(LY):
            i = site_index(x, y)

            xp = (x + 1) % CELL_Q
            x_phase = exp_kx if x + 1 == CELL_Q else 1.0 + 0.0j
            j = site_index(xp, y)
            amp = -T_HOP * x_phase
            h[i, j] += amp
            h[j, i] += np.conjugate(amp)

            yp = (y + 1) % LY
            y_phase = np.exp(1j * b_field * x)
            if y + 1 == LY:
                y_phase *= exp_ky
            j = site_index(x, yp)
            amp = -T_HOP * y_phase
            h[i, j] += amp
            h[j, i] += np.conjugate(amp)

    return h


def harper_h0_h1_h2(kx: float, ky: float, mass: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    h0 = harper_matrix(kx, ky, 0.0, mass)
    h1 = np.zeros_like(h0)
    h2 = np.zeros_like(h0)
    exp_ky = np.exp(1j * ky)

    for x in range(CELL_Q):
        for y in range(LY):
            i = site_index(x, y)
            yp = (y + 1) % LY
            j = site_index(x, yp)
            y_boundary_phase = exp_ky if y + 1 == LY else 1.0 + 0.0j
            amp1 = -T_HOP * (1j * x) * y_boundary_phase
            amp2 = T_HOP * (x * x / 2.0) * y_boundary_phase
            h1[i, j] += amp1
            h1[j, i] += np.conjugate(amp1)
            h2[i, j] += amp2
            h2[j, i] += np.conjugate(amp2)
    return h0, h1, h2


def response_from_pt_matrices(eig: np.ndarray, h1_abs2: np.ndarray, h2_diag: np.ndarray) -> ResponseParts:
    fprime = fermi_occupation(eig)
    fsecond = grand_kernel_second_derivative(eig)
    diff = eig[:, None] - eig[None, :]
    fprime_diff = fprime[:, None] - fprime[None, :]

    kernel = np.empty_like(diff)
    offdiag = np.abs(diff) > 1.0e-10
    kernel[offdiag] = fprime_diff[offdiag] / diff[offdiag]
    degenerate_limit = 0.5 * (fsecond[:, None] + fsecond[None, :])
    kernel[~offdiag] = degenerate_limit[~offdiag]

    h1_term = kernel * h1_abs2
    full = 2.0 * float(np.sum(fprime * h2_diag)) + float(np.sum(h1_term))
    interband_mask = (np.sign(eig)[:, None] * np.sign(eig)[None, :]) < 0.0
    interband = float(np.sum(h1_term[interband_mask]))
    return ResponseParts(full=full, intraband=full - interband, interband=interband)


def direct_real_space_pt_response(mass: float, gl_order: int = GL_ORDER) -> ResponseParts:
    nodes, weights = gl_average_nodes_weights(gl_order)
    total = np.zeros(3, dtype=np.float64)
    for ix, kx in enumerate(nodes):
        for iy, ky in enumerate(nodes):
            h0, h1, h2 = harper_h0_h1_h2(kx, ky, mass)
            eig, vec = np.linalg.eigh(h0)
            h1_eig = vec.conjugate().T @ h1 @ vec
            h2_eig = vec.conjugate().T @ h2 @ vec
            part = response_from_pt_matrices(
                eig=eig,
                h1_abs2=np.abs(h1_eig) ** 2,
                h2_diag=np.real(np.diag(h2_eig)),
            )
            weight = weights[ix] * weights[iy] / N_SITE
            total += weight * np.array([part.full, part.intraband, part.interband])
    return ResponseParts(full=float(total[0]), intraband=float(total[1]), interband=float(total[2]))


def finite_difference_response(mass: float, b_field: float, gl_order: int = GL_ORDER) -> float:
    nodes, weights = gl_average_nodes_weights(gl_order)
    inv_b2 = 1.0 / (b_field * b_field)
    total = 0.0
    for ix, kx in enumerate(nodes):
        for iy, ky in enumerate(nodes):
            eig_plus = np.linalg.eigvalsh(harper_matrix(kx, ky, b_field, mass))
            eig_zero = np.linalg.eigvalsh(harper_matrix(kx, ky, 0.0, mass))
            eig_minus = np.linalg.eigvalsh(harper_matrix(kx, ky, -b_field, mass))
            total += weights[ix] * weights[iy] * inv_b2 * float(
                np.sum(
                    grand_kernel(eig_plus)
                    + grand_kernel(eig_minus)
                    - 2.0 * grand_kernel(eig_zero)
                )
            ) / N_SITE
    return total


def continuum_moyal_midpoint_sum(q: int, mass: float) -> float:
    """Vectorized finite-Q midpoint sum for the continuum B^2 comparator.

    This is the determinant-Hessian member of the continuum Moyal/LP B^2
    density for the two-band staggered Bloch Hamiltonian.  It is used only as a
    convergence discriminator for the discrete-Moyal quadrature.
    """

    k = -math.pi + (np.arange(q, dtype=np.float64) + 0.5) * (2.0 * math.pi / q)
    kx, ky = np.meshgrid(k, k, indexing="ij")
    cx = np.cos(kx)
    cy = np.cos(ky)
    sx = np.sin(kx)
    sy = np.sin(ky)
    eps = -2.0 * T_HOP * (cx + cy)
    radius = np.sqrt(mass * mass + eps * eps)
    det_eps_hessian = 4.0 * T_HOP * T_HOP * cx * cy
    if mass == 0.0:
        det_hessian = det_eps_hessian
    else:
        adj_contract = 8.0 * T_HOP**3 * (sx * sx * cy + sy * sy * cx)
        det_hessian = (
            (eps * eps / (radius * radius)) * det_eps_hessian
            + (eps * mass * mass / (radius**4)) * adj_contract
        )

    z_plus = np.clip((radius - MU) / (2.0 * TEMP), -60.0, 60.0)
    z_minus = np.clip((-radius - MU) / (2.0 * TEMP), -60.0, 60.0)
    fermi_prime_plus = -0.25 / (TEMP * np.cosh(z_plus) ** 2)
    fermi_prime_minus = -0.25 / (TEMP * np.cosh(z_minus) ** 2)
    return float(np.mean((fermi_prime_plus + fermi_prime_minus) * det_hessian))


def run() -> int:
    print("Finite-cell two-band closed-form verifier")
    print(
        f"cell: Q={CELL_Q}, Ly={LY}, N={N_SITE}, GL={GL_ORDER}, "
        f"mu={MU}, T={TEMP}"
    )
    print(f"frozen tolerance: closed_form={CLOSED_FORM_TOL:.1e}")

    closed: dict[float, ResponseParts] = {}
    direct: dict[float, ResponseParts] = {}
    print("\nS0 finite-cell responses")
    for mass in MASSES:
        closed[mass] = finite_cell_closed_form_response(CELL_Q, mass)
        direct[mass] = direct_real_space_pt_response(mass)
        print(
            "m={:.3g} closed={:.12f} parts(intra,inter)=({:+.6e},{:+.6e})".format(
                mass,
                closed[mass].full,
                closed[mass].intraband,
                closed[mass].interband,
            )
        )

    check(
        "anti-fabrication: off-m=0 interband term is nonzero at every massive case",
        all(abs(closed[m].interband) > INTERBAND_MIN for m in (0.2, 0.3, 0.5)),
        "interband magnitudes="
        + ", ".join(f"m={m}: {abs(closed[m].interband):.6e}" for m in (0.2, 0.3, 0.5)),
    )

    print("\nS1 closed form: finite momentum sum vs real-space Harper PT")
    for mass in MASSES:
        diff = closed[mass].full - direct[mass].full
        check(
            f"closed finite sum equals direct Harper PT at m={mass}",
            abs(diff) <= CLOSED_FORM_TOL,
            f"closed-direct={diff:+.3e}, tol={CLOSED_FORM_TOL:.1e}",
        )

    coarse_b = 5.0e-4
    fine_b = 2.5e-4
    fd_mass = 0.2
    fd_coarse = finite_difference_response(fd_mass, coarse_b)
    fd_fine = finite_difference_response(fd_mass, fine_b)
    err_coarse = abs(fd_coarse - closed[fd_mass].full)
    err_fine = abs(fd_fine - closed[fd_mass].full)
    ratio = err_coarse / max(err_fine, 1.0e-300)
    print(
        f"finite-difference discriminator m={fd_mass}: "
        f"B={coarse_b:.1e} err={err_coarse:.6e}, "
        f"B={fine_b:.1e} err={err_fine:.6e}, ratio={ratio:.3f}"
    )
    check(
        "finite-difference cross-check converges toward the closed form when B halves",
        err_fine <= FINITE_DIFF_FINE_ABS and ratio >= FINITE_DIFF_RATIO_MIN,
        f"fine_err={err_fine:.3e}, max={FINITE_DIFF_FINE_ABS:.1e}, "
        f"ratio={ratio:.3f}, min={FINITE_DIFF_RATIO_MIN:.1f}",
    )

    print("\nS2 convergence: finite-Q discrete Moyal midpoint sums")
    q_values = (24, 48, 96, 192)
    target_q = 384
    for mass in (0.2, 0.5):
        seq = [continuum_moyal_midpoint_sum(q, mass) for q in q_values]
        target = continuum_moyal_midpoint_sum(target_q, mass)
        diffs = [abs(value - target) for value in seq]
        rates = [
            diffs[i] / max(diffs[i + 1], MOYAL_RATE_DENOM_FLOOR)
            for i in range(len(diffs) - 1)
        ]
        print(
            "m={:.3g} Q-sequence: ".format(mass)
            + ", ".join(f"Q={q}: {value:+.12e}" for q, value in zip(q_values, seq))
            + f"; target Q={target_q}: {target:+.12e}; rates="
            + ", ".join(f"{rate:.3f}" for rate in rates)
        )
        check(
            f"discrete Moyal sum converges monotonically at m={mass}",
            all(diffs[i + 1] < diffs[i] for i in range(len(diffs) - 1))
            and min(rates) >= MOYAL_MONOTONE_MIN_RATE,
            "diffs_to_Q384=" + ", ".join(f"{d:.3e}" for d in diffs),
        )

    print("\nS3 note hygiene")
    note = NOTE.read_text(encoding="utf-8")
    check(
        "note has bounded theorem claim type and audit authority",
        "**Claim type:** bounded_theorem" in note
        and "**Status authority:** independent audit lane" in note,
    )
    check(
        "note names the supplied finite-cell scope",
        "Q = 24, Ly = 2" in note
        and "finite discrete momentum sum" in note,
    )
    check(
        "note discloses residuals and the Moyal comparator scope",
        "Residuals" in note and "Moyal comparator" in note,
    )

    print(f"\nTOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(run())
