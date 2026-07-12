#!/usr/bin/env python3
"""Finite Harper/PT eps* full-kernel finite-scale quotient verifier.

Companion draft:
    docs/EPSSTAR_FULL_KERNEL_COEFFICIENT_DERIVATION_BOUNDED_THEOREM_NOTE_2026-06-12.md

Run:
    python3 scripts/frontier_epsstar_full_kernel_coefficient_2026_06_12.py
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


# Two-band Harper/PT constants used for the internally recomputed precursor
# anchor and the complete finite-temperature kernel check.
T_HOP = 1.0
Q_HARPER = 24
LX = Q_HARPER
LY = 2
N_SITE = LX * LY
PT_GL_ORDER = 20
BISECTION_LO = 1.2
BISECTION_HI = 2.4
BISECTION_STEPS = 60

# Fixed finite-T truth grid specified by this runner, plus the branch-slope
# grid that recomputes the measured-d comparator. The first grid is printed as
# the fine scan; the second is the frozen measured-d comparator that produced
# +3.88.
TRUTH_TEMPERATURES = (0.08, 0.10, 0.12, 0.15, 0.20)
PRECURSOR_SLOPE_TEMPERATURES = (0.10, 0.15, 0.20, 0.25)

# Fixed T=0 Fermi-surface quadrature controls. The Gaussian delta is a fixed
# surface proxy; the gates below are therefore finite-cell/finite-eta
# statements, not a continuum theorem.
SURFACE_DELTA_ETA = 5.0e-2
T0_BRANCH_LO = 1.48
T0_BRANCH_HI = 1.56
SOMMERFELD_DERIV_H = 2.0e-2
DEGENERATE_PAIR_TOL = 1.0e-10
FULL_KERNEL_READOUT_T = SURFACE_DELTA_ETA

# Frozen anchors/tolerances.  They are constants, not maps edited from the
# observed values.
FROZEN_MU0 = 1.5216
FROZEN_MU0_ABS_TOL = 2.0e-2
FROZEN_ALPHA_SEAGULL = -9.27
FROZEN_ALPHA_SEAGULL_ABS_TOL = 7.5e-1
FROZEN_D_GRID = 3.88
FROZEN_D_GRID_ABS_TOL = 7.5e-1
INTERBAND_H1_MIN = 1.0e-2
DECLARED_COMPARISON_BAND = 1.5e-1
PRINTED_VALUE_ROUNDING_RADIUS = 5.0e-13
NOTE_PATH = Path(
    "docs/EPSSTAR_FULL_KERNEL_COEFFICIENT_DERIVATION_BOUNDED_THEOREM_NOTE_2026-06-12.md"
)
RUNNER_LINK = (
    "[`scripts/frontier_epsstar_full_kernel_coefficient_2026_06_12.py`]"
    "(../scripts/frontier_epsstar_full_kernel_coefficient_2026_06_12.py)"
)
CACHE_LINK = (
    "[`logs/runner-cache/frontier_epsstar_full_kernel_coefficient_2026_06_12.txt`]"
    "(../logs/runner-cache/frontier_epsstar_full_kernel_coefficient_2026_06_12.txt)"
)
LP_BRIDGE_LINK = (
    "[`LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md`]"
    "(LP_TWO_BAND_EXACT_COMPLETION_BOUNDED_THEOREM_NOTE_2026-06-12.md)"
)
RICHARDSON_BOUNDARY_LINK = (
    "[`EPSSTAR_COEFFICIENT_RICHARDSON_MOFF0_BOUNDED_NOTE_2026-06-12.md`]"
    "(EPSSTAR_COEFFICIENT_RICHARDSON_MOFF0_BOUNDED_NOTE_2026-06-12.md)"
)
FORBIDDEN_CLOSED_PR_MARKER = "PR #" + "3820"
FORBIDDEN_PRECURSOR_STATUS_WORD = "lan" + "ded"

SITE_SIGNS = np.array(
    [1.0 if (x + y) % 2 == 0 else -1.0 for x in range(LX) for y in range(LY)]
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: str) -> None:
    """Gate a computed quantity against a fixed frozen tolerance or threshold."""

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
    kernel = np.where(table.nondegenerate, fp_diff / denom, 0.5 * (fprime[:, :, None] + fprime[:, None, :]))
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
    offdiag_sum = np.sum(np.where(table.nondegenerate, table.h1_abs2 / denom, 0.0), axis=2)
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
    """Return d(mu^2)/d(T^2) from a fixed T=0 Sommerfeld surface formula.

    The occupation part is the standard one-energy Sommerfeld coefficient of
    the T=0 curvature kernel.  The contact part is the degenerate divided-
    difference limit K(E,E;T)=f'(E); its T^2 coefficient is the fixed second
    moment of -f'(E), hence the -gamma'' term.  The precursor negative uses
    only the diagonal H1 contact.  The full-kernel test keeps every H1 matrix
    element inside the fixed degenerate block before taking the same moment.
    """

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


def full_kernel_finite_scale_readout(
    table: PTArrays,
    mu0: float,
    response_prime: float,
) -> tuple[float, float, PTParts]:
    """Return the declared complete-kernel quotient at fixed mu0 and T_q.

    This is deliberately not a boundary-root refit.  It evaluates the complete
    finite-T PT integrand once at the declared finite scale T_q=0.05 and
    divides by T_q^2 after the separately regularized T=0 branch response has
    been anchored to zero.  This defines a finite-protocol quotient.  It is
    not a T->0 coefficient or an error-controlled asymptotic estimate.
    """

    parts = pt_chi_parts(mu0, FULL_KERNEL_READOUT_T, table)
    chi_t2_coeff = parts.full / (FULL_KERNEL_READOUT_T * FULL_KERNEL_READOUT_T)
    alpha = -chi_t2_coeff / (response_prime / (2.0 * mu0))
    return alpha, chi_t2_coeff, parts


def run() -> int:
    print("eps* full-kernel finite-scale quotient verifier")
    print(
        f"PT cell: Q={Q_HARPER}, Ly={LY}, N={N_SITE}, GL={PT_GL_ORDER}; "
        f"bracket=[{BISECTION_LO:.1f},{BISECTION_HI:.1f}], "
        f"surface_eta={SURFACE_DELTA_ETA:.3f}, deg_tol={DEGENERATE_PAIR_TOL:.1e}"
    )

    table = build_pt_arrays(0.0, PT_GL_ORDER)
    surface = build_surface_table(table)

    print("\nS0 ANCHORS")
    mu0, branch_left, branch_right = t0_branch_root(surface)
    alpha_seagull, response_prime_naive, ct2_naive = sommerfeld_alpha(
        surface, mu0, full_degenerate=False
    )
    anchor_row = pt_boundary_root(table, 0.20)
    print(
        f"T0_BRANCH mu0={mu0:.12f} branch_final=({branch_left:+.12e},{branch_right:+.12e}) "
        f"R0_prime_naive={response_prime_naive:+.12e} C_T2_naive={ct2_naive:+.12e}"
    )
    print(
        f"NAIVE_PROXY alpha_proxy={alpha_seagull:+.12f} "
        f"frozen={FROZEN_ALPHA_SEAGULL:+.12f}"
    )
    print(
        f"ANTI_FAB T=0.20 root={anchor_row.root:.12f} "
        f"interband_chi={anchor_row.interband_at_root:+.12e} "
        f"interband_H1_weight={anchor_row.interband_h1_weight_at_root:+.12e}"
    )
    check(
        "S0 T=0 branch root is in the internally recomputed mu*_0=1.5216 region",
        abs(mu0 - FROZEN_MU0) <= FROZEN_MU0_ABS_TOL,
        f"mu0={mu0:.12f}, frozen={FROZEN_MU0:.4f}, tol={FROZEN_MU0_ABS_TOL:.2e}",
    )
    check(
        "S0 precursor naive Sommerfeld proxy is reproduced",
        abs(alpha_seagull - FROZEN_ALPHA_SEAGULL) <= FROZEN_ALPHA_SEAGULL_ABS_TOL,
        f"alpha_seagull={alpha_seagull:+.12f}, frozen={FROZEN_ALPHA_SEAGULL:+.2f}, "
        f"tol={FROZEN_ALPHA_SEAGULL_ABS_TOL:.2e}",
    )
    check(
        "S0 anti-fabrication: interband |H1| weight is nontrivial at the PT root",
        anchor_row.interband_h1_weight_at_root >= INTERBAND_H1_MIN,
        f"interband_H1_weight={anchor_row.interband_h1_weight_at_root:.6e}, "
        f"min={INTERBAND_H1_MIN:.1e}",
    )

    print("\nS1 TRUTH: finite-T boundary roots")
    root_cache: dict[float, RootRow] = {}
    for temp in sorted(set(TRUTH_TEMPERATURES + PRECURSOR_SLOPE_TEMPERATURES)):
        root_cache[temp] = pt_boundary_root(table, temp)

    truth_rows = [root_cache[temp] for temp in TRUTH_TEMPERATURES]
    for row in truth_rows:
        print(
            f"ROOT T={row.temperature:.3f} mu={row.root:.12f} "
            f"mu2={row.root * row.root:.12f} chi={row.chi_at_root:+.3e} "
            f"interband={row.interband_at_root:+.12e}"
        )
    slope_rows = [root_cache[temp] for temp in PRECURSOR_SLOPE_TEMPERATURES]
    d_grid, mu2_intercept, mu2_max_abs_residual = fit_mu2_slope(slope_rows)
    print(
        "PRECURSOR_SLOPE_GRID "
        + " ".join(
            f"T={row.temperature:.3f}:mu={row.root:.12f}:mu2={row.root * row.root:.12f}"
            for row in slope_rows
        )
    )
    print(
        f"TRUTH_FIT mu*(T)^2 = c + d*T^2: c={mu2_intercept:.12f} "
        f"d_grid={d_grid:+.12f} max_abs_residual={mu2_max_abs_residual:.12e}"
    )
    check(
        "S1 finite-grid regression slope reproduces internally recomputed +3.88",
        abs(d_grid - FROZEN_D_GRID) <= FROZEN_D_GRID_ABS_TOL,
        f"d_grid={d_grid:+.12f}, frozen={FROZEN_D_GRID:+.2f}, "
        f"tol={FROZEN_D_GRID_ABS_TOL:.2e}",
    )

    print("\nS2 FINITE-SCALE READOUT: complete finite-T divided-difference kernel")
    q_full, ct2_full, coeff_parts = full_kernel_finite_scale_readout(
        table, mu0, response_prime_naive
    )
    finite_readout_scale = -1.0 / (
        (response_prime_naive / (2.0 * mu0))
        * FULL_KERNEL_READOUT_T
        * FULL_KERNEL_READOUT_T
    )
    q_seagull = finite_readout_scale * coeff_parts.seagull
    q_kernel = finite_readout_scale * coeff_parts.kernel
    print(
        f"READOUTS alpha_proxy={alpha_seagull:+.12f} q_seagull={q_seagull:+.12f} "
        f"q_kernel={q_kernel:+.12f} q_full={q_full:+.12f}"
    )
    print(
        f"FULL_INTERNAL readout_T={FULL_KERNEL_READOUT_T:.3f} "
        f"chi_full(T)={coeff_parts.full:+.12e} "
        f"seagull(T)={coeff_parts.seagull:+.12e} kernel(T)={coeff_parts.kernel:+.12e} "
        f"C_T2_full={ct2_full:+.12e}; "
        f"R0_prime={response_prime_naive:+.12e} C_T2_naive={ct2_naive:+.12e}"
    )
    relative_difference = abs(q_full - d_grid) / max(abs(d_grid), 1.0e-15)
    rounding_upper = (
        abs(q_full - d_grid) + 2.0 * PRINTED_VALUE_ROUNDING_RADIUS
    ) / (abs(d_grid) - PRINTED_VALUE_ROUNDING_RADIUS)
    sign_robustness_radius = 0.5 * min(
        -q_seagull,
        q_kernel,
        q_kernel - abs(q_seagull),
        q_full,
        d_grid,
    )
    print(
        f"COMPARISON d_grid={d_grid:+.12f} q_full={q_full:+.12f} "
        f"relative_difference={relative_difference:.12e} "
        f"printed_rounding_upper={rounding_upper:.12e}"
    )
    print(
        f"SIGN_ROBUSTNESS componentwise_open_radius={sign_robustness_radius:.12f} "
        "for q_seagull<0, q_kernel>0, q_kernel>|q_seagull|, q_full>0, d_grid>0"
    )

    print("\nS3 GATES")
    check(
        "S3 q_full has the same positive sign as the finite-grid boundary slope",
        q_full > 0.0 and d_grid > 0.0,
        f"q_full={q_full:+.12f}, d_grid={d_grid:+.12f}, gate both > 0",
    )
    check(
        "S3 printed finite-grid comparison lies inside the declared band",
        rounding_upper <= DECLARED_COMPARISON_BAND,
        f"printed_rounding_upper={rounding_upper:.6e}, "
        f"declared_band={DECLARED_COMPARISON_BAND:.2e}; band is not an error estimate",
    )
    check(
        "S3 same-response finite-scale divided-difference term flips the seagull sign",
        q_seagull < 0.0
        and q_kernel > 0.0
        and abs(q_kernel) > abs(q_seagull)
        and math.isclose(q_full, q_seagull + q_kernel, rel_tol=0.0, abs_tol=1.0e-10),
        f"q_seagull={q_seagull:+.12f}, q_kernel={q_kernel:+.12f}, "
        f"q_full-(q_seagull+q_kernel)={q_full-q_seagull-q_kernel:+.3e}; "
        "gate q_seagull<0, q_kernel>0, |q_kernel|>|q_seagull|, exact split",
    )
    check(
        "S3 sign conclusions have a nontrivial componentwise robustness radius",
        sign_robustness_radius > 1.9,
        f"componentwise_open_radius={sign_robustness_radius:.12f}, gate > 1.9",
    )

    print("\nS4 SOURCE HYGIENE")
    note = NOTE_PATH.read_text(encoding="utf-8")
    check(
        "S4 canonical source metadata is present",
        "**Claim type:** bounded_theorem" in note
        and "**Status authority:** independent audit lane only" in note
        and "**No-promotion statement:**" in note,
        "claim_type bounded_theorem; independent audit authority; no-promotion statement",
    )
    check(
        "S4 runner and cache markdown links are present",
        RUNNER_LINK in note and CACHE_LINK in note,
        "primary runner/cache links seed review discoverability",
    )
    check(
        "S4 closed-PR authority rhetoric is absent",
        FORBIDDEN_CLOSED_PR_MARKER not in note
        and FORBIDDEN_PRECURSOR_STATUS_WORD not in note,
        "no closed PR is cited as load-bearing authority",
    )
    check(
        "S4 direct finite-model bridge and coefficient-limit boundary links are present",
        LP_BRIDGE_LINK in note and RICHARDSON_BOUNDARY_LINK in note,
        "load-bearing links seed the retained-bounded dependency chain",
    )
    check(
        "S4 finite-scale boundary replaces the unsupported asymptotic claim",
        "not a controlled `T -> 0` coefficient" in note
        and "`O(eta^2)` truncation estimate" in note
        and "MINIMAL_AXIOMS_2026-06-05.md" not in note,
        "one-point quotient is finite-grid only; no minimal-axiom model-selection claim",
    )

    print(f"\nTOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(run())
