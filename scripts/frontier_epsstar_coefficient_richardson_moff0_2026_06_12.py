#!/usr/bin/env python3
"""Finite Harper/PT eps* coefficient Richardson and m != 0 sign-flip runner.

Companion draft:
    docs/EPSSTAR_COEFFICIENT_RICHARDSON_MOFF0_BOUNDED_NOTE_2026-06-12.md

Run:
    python3 scripts/frontier_epsstar_coefficient_richardson_moff0_2026_06_12.py
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from functools import lru_cache

import numpy as np
from numpy.polynomial.legendre import leggauss


T_HOP = 1.0
Q_HARPER = 24
LX = Q_HARPER
LY = 2
N_SITE = LX * LY
PT_GL_ORDER = 20
BISECTION_LO = 1.2
BISECTION_HI = 2.4
BISECTION_STEPS = 60

SURFACE_DELTA_ETA = 5.0e-2
T0_BRANCH_LO = 1.48
T0_BRANCH_HI = 1.56
SOMMERFELD_DERIV_H = 2.0e-2
DEGENERATE_PAIR_TOL = 1.0e-10
ONEPOINT_T = SURFACE_DELTA_ETA
RICHARDSON_ETAS = (0.08, 0.04, 0.02, 0.01)
LANDED_SLOPE_TEMPERATURES = (0.10, 0.15, 0.20, 0.25)

FROZEN_MU0 = 1.515550712171
FROZEN_MU0_ABS_TOL = 1.0e-9
FROZEN_ALPHA_SEAGULL = -9.266358431847
FROZEN_ALPHA_SEAGULL_ABS_TOL = 1.0e-9
FROZEN_ALPHA_ONEPOINT = 4.141818423703
FROZEN_ALPHA_ONEPOINT_ABS_TOL = 1.0e-9
FROZEN_D_MEASURED = 3.877078419950
FROZEN_D_MEASURED_ABS_TOL = 1.0e-9
INTERBAND_H1_MIN = 1.0e-2

# Frozen after the genuine eta^2 fit on the fixed GL=20, Q=24, Ly=2 cell.
FROZEN_ALPHA_FULL_EXTRAP = -16.688856113481
ALPHA_FULL_EXTRAP_ABS_TOL = 1.0e-9
RICHARDSON_ALPHA_FIT_RESIDUAL_BOUND = 8.6e1
MEASURED_REL_GAP_BOUND = 5.4

SITE_SIGNS = np.array(
    [1.0 if (x + y) % 2 == 0 else -1.0 for x in range(LX) for y in range(LY)]
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: str) -> None:
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    print(f"{tag}: {label} :: {detail}")


def site_index(x: int, y: int) -> int:
    return (x % LX) * LY + (y % LY)


@lru_cache(maxsize=None)
def gl_average_nodes_weights(n: int) -> tuple[np.ndarray, np.ndarray]:
    x, w = leggauss(n)
    return np.pi * x, 0.5 * w


def fermi_occupation(energy: np.ndarray, mu: float, temp: float) -> np.ndarray:
    z = np.clip((energy - mu) / temp, -60.0, 60.0)
    return 1.0 / (1.0 + np.exp(z))


def fermi_prime_energy(energy: np.ndarray, mu: float, temp: float) -> np.ndarray:
    f = fermi_occupation(energy, mu, temp)
    return -f * (1.0 - f) / temp


def harper_matrix(kx: float, ky: float, b_field: float, mass: float) -> np.ndarray:
    h = np.zeros((N_SITE, N_SITE), dtype=np.complex128)
    h[np.diag_indices(N_SITE)] = mass * SITE_SIGNS
    exp_kx = np.exp(1j * kx)
    exp_ky = np.exp(1j * ky)

    for x in range(LX):
        for y in range(LY):
            i = site_index(x, y)

            xp = (x + 1) % LX
            x_phase = exp_kx if x + 1 == LX else 1.0 + 0.0j
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

    for x in range(LX):
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


@dataclass(frozen=True)
class PTArrays:
    weights: np.ndarray
    eig: np.ndarray
    h2_diag: np.ndarray
    h1_abs2: np.ndarray
    diff: np.ndarray
    nondegenerate: np.ndarray
    degenerate: np.ndarray
    interband: np.ndarray


@dataclass(frozen=True)
class PTParts:
    full: float
    seagull: float
    kernel: float
    interband: float


@dataclass(frozen=True)
class RootRow:
    temperature: float
    root: float
    chi_at_root: float
    interband_at_root: float
    interband_h1_weight_at_root: float


@dataclass(frozen=True)
class SurfaceTable:
    weight: np.ndarray
    eig: np.ndarray
    curvature_kernel: np.ndarray
    h1_diag_abs2: np.ndarray
    h1_degenerate_abs2: np.ndarray


@dataclass(frozen=True)
class RichardsonFit:
    chi_over_eta2_extrap: float
    chi_over_eta2_slope: float
    alpha_full_extrap: float
    alpha_eta2_slope: float
    max_abs_alpha_residual: float
    rms_alpha_residual: float
    max_abs_chi_over_eta2_residual: float


def build_pt_arrays(mass: float, gl_order: int) -> PTArrays:
    nodes, gl_weights = gl_average_nodes_weights(gl_order)
    weights: list[float] = []
    eig_rows: list[np.ndarray] = []
    h2_rows: list[np.ndarray] = []
    h1_rows: list[np.ndarray] = []
    interband_rows: list[np.ndarray] = []

    for ix, kx in enumerate(nodes):
        for iy, ky in enumerate(nodes):
            h0, h1, h2 = harper_h0_h1_h2(float(kx), float(ky), mass)
            eig, vec = np.linalg.eigh(h0)
            h1_eig = vec.conjugate().T @ h1 @ vec
            h2_eig = vec.conjugate().T @ h2 @ vec
            signs = np.sign(eig)
            weights.append(float(gl_weights[ix] * gl_weights[iy] / N_SITE))
            eig_rows.append(eig)
            h2_rows.append(np.real(np.diag(h2_eig)))
            h1_rows.append(np.abs(h1_eig) ** 2)
            interband_rows.append((signs[:, None] * signs[None, :]) < 0.0)

    eig = np.array(eig_rows, dtype=float)
    h1_abs2 = np.array(h1_rows, dtype=float)
    diff = eig[:, :, None] - eig[:, None, :]
    nondegenerate = np.abs(diff) > DEGENERATE_PAIR_TOL
    return PTArrays(
        weights=np.array(weights, dtype=float)[:, None],
        eig=eig,
        h2_diag=np.array(h2_rows, dtype=float),
        h1_abs2=h1_abs2,
        diff=diff,
        nondegenerate=nondegenerate,
        degenerate=~nondegenerate,
        interband=np.array(interband_rows, dtype=bool),
    )


def pt_chi_parts(mu: float, temp: float, table: PTArrays) -> PTParts:
    fp = fermi_occupation(table.eig, mu, temp)
    fprime = fermi_prime_energy(table.eig, mu, temp)
    fp_diff = fp[:, :, None] - fp[:, None, :]

    denom = np.where(table.nondegenerate, table.diff, 1.0)
    kernel = np.where(
        table.nondegenerate,
        fp_diff / denom,
        0.5 * (fprime[:, :, None] + fprime[:, None, :]),
    )
    h1_matrix = kernel * table.h1_abs2

    seagull_point = 2.0 * np.sum(fp * table.h2_diag, axis=1)
    kernel_point = np.sum(h1_matrix, axis=(1, 2))
    interband_point = np.sum(np.where(table.interband, h1_matrix, 0.0), axis=(1, 2))

    seagull = float(np.sum(table.weights[:, 0] * seagull_point))
    kernel_total = float(np.sum(table.weights[:, 0] * kernel_point))
    interband = float(np.sum(table.weights[:, 0] * interband_point))
    return PTParts(
        full=seagull + kernel_total,
        seagull=seagull,
        kernel=kernel_total,
        interband=interband,
    )


def interband_h1_weight(mu: float, table: PTArrays) -> float:
    window = np.exp(-((table.eig - mu) / SURFACE_DELTA_ETA) ** 2)
    pair_window = 0.5 * (window[:, :, None] + window[:, None, :])
    weighted = np.where(table.interband, table.h1_abs2 * pair_window, 0.0)
    return float(np.sum(table.weights[:, 0] * np.sum(weighted, axis=(1, 2))))


def sign_bracketed(left_value: float, right_value: float) -> bool:
    return (
        np.isfinite(left_value)
        and np.isfinite(right_value)
        and left_value * right_value <= 0.0
    )


def pt_boundary_root(table: PTArrays, temperature: float) -> RootRow:
    left = BISECTION_LO
    right = BISECTION_HI
    left_value = pt_chi_parts(left, temperature, table).full
    right_value = pt_chi_parts(right, temperature, table).full
    if not sign_bracketed(left_value, right_value):
        return RootRow(temperature, math.nan, math.nan, math.nan, math.nan)

    for _ in range(BISECTION_STEPS):
        midpoint = 0.5 * (left + right)
        midpoint_value = pt_chi_parts(midpoint, temperature, table).full
        if left_value * midpoint_value <= 0.0:
            right = midpoint
            right_value = midpoint_value
        else:
            left = midpoint
            left_value = midpoint_value

    root = 0.5 * (left + right)
    value = pt_chi_parts(root, temperature, table)
    return RootRow(
        temperature=temperature,
        root=root,
        chi_at_root=value.full,
        interband_at_root=value.interband,
        interband_h1_weight_at_root=interband_h1_weight(root, table),
    )


def build_surface_table(table: PTArrays) -> SurfaceTable:
    denom = np.where(table.nondegenerate, table.diff, 1.0)
    offdiag_sum = np.sum(
        np.where(table.nondegenerate, table.h1_abs2 / denom, 0.0), axis=2
    )
    curvature_kernel = 2.0 * table.h2_diag + 2.0 * offdiag_sum
    return SurfaceTable(
        weight=table.weights,
        eig=table.eig,
        curvature_kernel=curvature_kernel,
        h1_diag_abs2=np.diagonal(table.h1_abs2, axis1=1, axis2=2),
        h1_degenerate_abs2=np.sum(np.where(table.degenerate, table.h1_abs2, 0.0), axis=2),
    )


def surface_delta(surface: SurfaceTable, mu: float) -> np.ndarray:
    eta = SURFACE_DELTA_ETA
    return (1.0 / (eta * math.sqrt(math.pi))) * np.exp(-((surface.eig - mu) / eta) ** 2)


def surface_phi(surface: SurfaceTable, mu: float) -> float:
    return float(np.sum(surface.weight * surface_delta(surface, mu) * surface.curvature_kernel))


def surface_gamma(surface: SurfaceTable, mu: float, full_degenerate: bool) -> float:
    h1_weight = surface.h1_degenerate_abs2 if full_degenerate else surface.h1_diag_abs2
    return float(np.sum(surface.weight * surface_delta(surface, mu) * h1_weight))


def t0_response(surface: SurfaceTable, mu: float, full_degenerate: bool = False) -> float:
    h1_weight = surface.h1_degenerate_abs2 if full_degenerate else surface.h1_diag_abs2
    occupied = surface.eig < mu
    bulk = float(np.sum(surface.weight * occupied * surface.curvature_kernel))
    contact = float(np.sum(surface.weight * surface_delta(surface, mu) * h1_weight))
    return bulk - contact


def scalar_derivative(fn, x: float, h: float) -> float:
    return (fn(x + h) - fn(x - h)) / (2.0 * h)


def scalar_second_derivative(fn, x: float, h: float) -> float:
    return (fn(x + h) - 2.0 * fn(x) + fn(x - h)) / (h * h)


def t0_branch_root(surface: SurfaceTable) -> tuple[float, float, float]:
    left = T0_BRANCH_LO
    right = T0_BRANCH_HI
    left_value = t0_response(surface, left, full_degenerate=False)
    right_value = t0_response(surface, right, full_degenerate=False)
    if not sign_bracketed(left_value, right_value):
        return math.nan, left_value, right_value

    for _ in range(BISECTION_STEPS):
        midpoint = 0.5 * (left + right)
        midpoint_value = t0_response(surface, midpoint, full_degenerate=False)
        if left_value * midpoint_value <= 0.0:
            right = midpoint
            right_value = midpoint_value
        else:
            left = midpoint
            left_value = midpoint_value

    return 0.5 * (left + right), left_value, right_value


def sommerfeld_alpha(surface: SurfaceTable, mu0: float, full_degenerate: bool) -> tuple[float, float, float]:
    h = SOMMERFELD_DERIV_H
    phi_prime = scalar_derivative(lambda x: surface_phi(surface, x), mu0, h)
    gamma_prime = scalar_derivative(lambda x: surface_gamma(surface, x, full_degenerate), mu0, h)
    gamma_second = scalar_second_derivative(lambda x: surface_gamma(surface, x, full_degenerate), mu0, h)
    response_prime = surface_phi(surface, mu0) - gamma_prime
    response_t2_coeff = (math.pi * math.pi / 6.0) * (phi_prime - gamma_second)
    beta_mu = -response_t2_coeff / response_prime
    return 2.0 * mu0 * beta_mu, response_prime, response_t2_coeff


def fit_mu2_slope(rows: list[RootRow]) -> tuple[float, float, float]:
    t = np.array([row.temperature for row in rows], dtype=float)
    mu2 = np.array([row.root * row.root for row in rows], dtype=float)
    design = np.vstack([np.ones_like(t), t * t]).T
    coeffs = np.linalg.lstsq(design, mu2, rcond=None)[0]
    predicted = design @ coeffs
    max_abs_residual = float(np.max(np.abs(mu2 - predicted)))
    return float(coeffs[1]), float(coeffs[0]), max_abs_residual


def alpha_from_parts(parts: PTParts, temp: float, mu0: float, response_prime: float) -> float:
    chi_t2_coeff = parts.full / (temp * temp)
    return -chi_t2_coeff / (response_prime / (2.0 * mu0))


def onepoint_alpha(table: PTArrays, mu0: float, response_prime: float) -> tuple[float, float, PTParts]:
    parts = pt_chi_parts(mu0, ONEPOINT_T, table)
    alpha = alpha_from_parts(parts, ONEPOINT_T, mu0, response_prime)
    return alpha, parts.full / (ONEPOINT_T * ONEPOINT_T), parts


def richardson_eta2_fit(
    eta_rows: list[tuple[float, float, float, float]],
    mu0: float,
    response_prime: float,
) -> RichardsonFit:
    """Extrapolate the finite-T response from the eta sequence only."""

    etas = np.array([row[0] for row in eta_rows], dtype=float)
    chi_over_eta2 = np.array([row[2] for row in eta_rows], dtype=float)
    eta2 = etas * etas
    design = np.vstack([np.ones_like(eta2), eta2]).T
    chi_coeffs = np.linalg.lstsq(design, chi_over_eta2, rcond=None)[0]
    fitted_chi_over_eta2 = design @ chi_coeffs

    alpha_scale = -1.0 / (response_prime / (2.0 * mu0))
    alpha_values = alpha_scale * chi_over_eta2
    fitted_alpha = alpha_scale * fitted_chi_over_eta2
    alpha_residuals = alpha_values - fitted_alpha
    chi_residuals = chi_over_eta2 - fitted_chi_over_eta2

    return RichardsonFit(
        chi_over_eta2_extrap=float(chi_coeffs[0]),
        chi_over_eta2_slope=float(chi_coeffs[1]),
        alpha_full_extrap=float(alpha_scale * chi_coeffs[0]),
        alpha_eta2_slope=float(alpha_scale * chi_coeffs[1]),
        max_abs_alpha_residual=float(np.max(np.abs(alpha_residuals))),
        rms_alpha_residual=float(np.sqrt(np.mean(alpha_residuals * alpha_residuals))),
        max_abs_chi_over_eta2_residual=float(np.max(np.abs(chi_residuals))),
    )


def analyze_mass(mass: float) -> dict[str, object]:
    table = build_pt_arrays(mass, PT_GL_ORDER)
    surface = build_surface_table(table)
    mu0, branch_left, branch_right = t0_branch_root(surface)
    alpha_seagull, response_prime, ct2_naive = sommerfeld_alpha(
        surface, mu0, full_degenerate=False
    )
    alpha_onepoint, ct2_full, onepoint_parts = onepoint_alpha(table, mu0, response_prime)
    alpha_kernel_onepoint = alpha_onepoint - alpha_seagull
    eta_rows = []
    for eta in RICHARDSON_ETAS:
        parts = pt_chi_parts(mu0, eta, table)
        eta_rows.append(
            (
                eta,
                parts.full,
                parts.full / (eta * eta),
                alpha_from_parts(parts, eta, mu0, response_prime),
            )
        )
    return {
        "table": table,
        "surface": surface,
        "mu0": mu0,
        "branch_left": branch_left,
        "branch_right": branch_right,
        "alpha_seagull": alpha_seagull,
        "response_prime": response_prime,
        "ct2_naive": ct2_naive,
        "alpha_onepoint": alpha_onepoint,
        "ct2_full": ct2_full,
        "onepoint_parts": onepoint_parts,
        "alpha_kernel_onepoint": alpha_kernel_onepoint,
        "eta_rows": eta_rows,
    }


def run() -> int:
    print("eps* coefficient Richardson/m!=0 finite Harper/PT verifier")
    print(
        f"PT cell: Q={Q_HARPER}, Ly={LY}, N={N_SITE}, GL={PT_GL_ORDER}; "
        f"surface_eta={SURFACE_DELTA_ETA:.3f}; richardson_etas={RICHARDSON_ETAS}"
    )

    print("\nS0 ANCHORS")
    m0 = analyze_mass(0.0)
    mu0 = float(m0["mu0"])
    alpha_seagull = float(m0["alpha_seagull"])
    response_prime = float(m0["response_prime"])
    anchor_row = pt_boundary_root(m0["table"], 0.20)  # type: ignore[arg-type]
    alpha_onepoint = float(m0["alpha_onepoint"])
    print(
        f"T0_BRANCH mu0={mu0:.12f} "
        f"branch_final=({float(m0['branch_left']):+.12e},{float(m0['branch_right']):+.12e}) "
        f"R0_prime={response_prime:+.12e} C_T2_naive={float(m0['ct2_naive']):+.12e}"
    )
    print(
        f"ANCHOR_COEFF alpha_seagull={alpha_seagull:+.12f} "
        f"alpha_full_onepoint={alpha_onepoint:+.12f}"
    )
    print(
        f"ANTI_FAB T=0.20 root={anchor_row.root:.12f} "
        f"interband_chi={anchor_row.interband_at_root:+.12e} "
        f"interband_H1_weight={anchor_row.interband_h1_weight_at_root:+.12e}"
    )
    check(
        "S0 T=0 branch root reproduces landed mu*_0 region",
        abs(mu0 - FROZEN_MU0) <= FROZEN_MU0_ABS_TOL,
        f"mu0={mu0:.12f}, frozen={FROZEN_MU0:.12f}, tol={FROZEN_MU0_ABS_TOL:.2e}",
    )
    check(
        "S0 landed seagull alpha is reproduced",
        abs(alpha_seagull - FROZEN_ALPHA_SEAGULL) <= FROZEN_ALPHA_SEAGULL_ABS_TOL,
        f"alpha_seagull={alpha_seagull:+.12f}, frozen={FROZEN_ALPHA_SEAGULL:+.12f}, "
        f"tol={FROZEN_ALPHA_SEAGULL_ABS_TOL:.2e}",
    )
    check(
        "S0 landed one-point full alpha is reproduced",
        abs(alpha_onepoint - FROZEN_ALPHA_ONEPOINT) <= FROZEN_ALPHA_ONEPOINT_ABS_TOL,
        f"alpha_onepoint={alpha_onepoint:+.12f}, frozen={FROZEN_ALPHA_ONEPOINT:+.12f}, "
        f"tol={FROZEN_ALPHA_ONEPOINT_ABS_TOL:.2e}",
    )
    check(
        "S0 anti-fabrication: interband |H1| weight is nontrivial at the PT root",
        anchor_row.interband_h1_weight_at_root >= INTERBAND_H1_MIN,
        f"interband_H1_weight={anchor_row.interband_h1_weight_at_root:.6e}, "
        f"min={INTERBAND_H1_MIN:.1e}",
    )

    print("\nS1 GENUINE RICHARDSON")
    for eta, chi, chi_t2, alpha_eta in m0["eta_rows"]:  # type: ignore[assignment]
        print(
            f"ETA_SEQUENCE eta={eta:.3f} chi={chi:+.12e} "
            f"chi_over_eta2={chi_t2:+.12e} alpha_eta={alpha_eta:+.12f}"
        )
    richardson = richardson_eta2_fit(
        m0["eta_rows"], mu0, response_prime  # type: ignore[arg-type]
    )
    alpha_extrap = richardson.alpha_full_extrap
    alpha_kernel_extrap = alpha_extrap - alpha_seagull
    print(
        f"RICHARDSON_FIT chi_over_eta2_extrap={richardson.chi_over_eta2_extrap:+.12e} "
        f"chi_over_eta2_slope={richardson.chi_over_eta2_slope:+.12e} "
        f"alpha_full_extrap={alpha_extrap:+.12f} "
        f"alpha_eta2_slope={richardson.alpha_eta2_slope:+.12e} "
        f"max_abs_alpha_fit_residual={richardson.max_abs_alpha_residual:.12e} "
        f"rms_alpha_fit_residual={richardson.rms_alpha_residual:.12e} "
        f"max_abs_chi_over_eta2_fit_residual={richardson.max_abs_chi_over_eta2_residual:.12e}"
    )
    check(
        "S1 Richardson uses the required fixed eta set",
        tuple(row[0] for row in m0["eta_rows"]) == RICHARDSON_ETAS,  # type: ignore[index]
        f"etas={tuple(row[0] for row in m0['eta_rows'])}",  # type: ignore[index]
    )
    check(
        "S1 genuine eta^2 extrapolated alpha is frozen",
        abs(alpha_extrap - FROZEN_ALPHA_FULL_EXTRAP) <= ALPHA_FULL_EXTRAP_ABS_TOL,
        f"alpha_extrap={alpha_extrap:+.12f}, frozen={FROZEN_ALPHA_FULL_EXTRAP:+.12f}, "
        f"tol={ALPHA_FULL_EXTRAP_ABS_TOL:.2e}",
    )
    check(
        "S1 eta^2 fit residual is below the frozen honest bound",
        richardson.max_abs_alpha_residual <= RICHARDSON_ALPHA_FIT_RESIDUAL_BOUND,
        f"max_abs_alpha_fit_residual={richardson.max_abs_alpha_residual:.6e}, "
        f"bound={RICHARDSON_ALPHA_FIT_RESIDUAL_BOUND:.1e}",
    )

    print("\nS2 HONEST COMPARISON")
    root_cache = {
        temp: pt_boundary_root(m0["table"], temp)  # type: ignore[arg-type]
        for temp in LANDED_SLOPE_TEMPERATURES
    }
    slope_rows = [root_cache[temp] for temp in LANDED_SLOPE_TEMPERATURES]
    d_measured, mu2_intercept, mu2_max_abs_residual = fit_mu2_slope(slope_rows)
    rel_gap = abs(alpha_extrap - d_measured) / max(abs(d_measured), 1.0e-15)
    onepoint_gap = abs(alpha_onepoint - d_measured)
    extrap_gap = abs(alpha_extrap - d_measured)
    print(
        "LANDED_SLOPE_GRID "
        + " ".join(
            f"T={row.temperature:.3f}:mu={row.root:.12f}:mu2={row.root * row.root:.12f}"
            for row in slope_rows
        )
    )
    print(
        f"TRUTH_FIT mu*(T)^2 = c + d*T^2: c={mu2_intercept:.12f} "
        f"d_measured={d_measured:+.12f} max_abs_residual={mu2_max_abs_residual:.12e}"
    )
    print(
        f"HONEST_COMPARISON alpha_full_extrap={alpha_extrap:+.12f} "
        f"alpha_kernel_extrap={alpha_kernel_extrap:+.12f} "
        f"onepoint_gap={onepoint_gap:.12e} extrap_gap={extrap_gap:.12e} "
        f"relative_gap={rel_gap:.12e}"
    )
    check(
        "S2 measured finite-T slope reproduces landed +3.877078419950",
        abs(d_measured - FROZEN_D_MEASURED) <= FROZEN_D_MEASURED_ABS_TOL,
        f"d_measured={d_measured:+.12f}, frozen={FROZEN_D_MEASURED:+.12f}, "
        f"tol={FROZEN_D_MEASURED_ABS_TOL:.2e}",
    )
    check(
        "S2 measured relative gap is inside the frozen honest bound",
        rel_gap <= MEASURED_REL_GAP_BOUND,
        f"relative_gap={rel_gap:.6e}, bound={MEASURED_REL_GAP_BOUND:.2e}",
    )
    check(
        "S2 genuine eta^2 Richardson does not improve on the one-point estimate",
        extrap_gap > onepoint_gap,
        f"extrap_gap={extrap_gap:.6e}, onepoint_gap={onepoint_gap:.6e}",
    )
    check(
        "S2 m=0 extrapolated split honestly does not satisfy sign-flip inequalities",
        not (
            alpha_seagull < 0.0
            and alpha_kernel_extrap > 0.0
            and abs(alpha_kernel_extrap) > abs(alpha_seagull)
        ),
        f"alpha_seagull={alpha_seagull:+.12f}, "
        f"alpha_kernel_extrap={alpha_kernel_extrap:+.12f}",
    )

    print("\nS3 m != 0 GENERALITY")
    m02 = analyze_mass(0.2)
    mu0_m02 = float(m02["mu0"])
    alpha_seagull_m02 = float(m02["alpha_seagull"])
    alpha_onepoint_m02 = float(m02["alpha_onepoint"])
    alpha_kernel_m02 = alpha_onepoint_m02 - alpha_seagull_m02
    print(
        f"MASS_OFF_ZERO m=0.200 mu0={mu0_m02:.12f} "
        f"alpha_seagull={alpha_seagull_m02:+.12f} "
        f"alpha_kernel={alpha_kernel_m02:+.12f} "
        f"alpha_full={alpha_onepoint_m02:+.12f}"
    )
    check(
        "S3 m=0.2 kernel still flips the seagull sign",
        alpha_seagull_m02 < 0.0
        and alpha_kernel_m02 > 0.0
        and abs(alpha_kernel_m02) > abs(alpha_seagull_m02),
        f"alpha_seagull(m=0.2)={alpha_seagull_m02:+.12f}, "
        f"alpha_kernel(m=0.2)={alpha_kernel_m02:+.12f}",
    )

    print(f"\nTOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(run())
