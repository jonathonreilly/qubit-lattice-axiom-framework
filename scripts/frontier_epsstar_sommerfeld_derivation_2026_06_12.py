#!/usr/bin/env python3
"""Class-A finite-dimensional eps* T=0/Sommerfeld boundary verifier.

Companion draft:
    docs/EPSSTAR_SOMMERFELD_T0_BOUNDARY_DERIVATION_BOUNDED_NOTE_2026-06-12.md

Run:
    python3 scripts/frontier_epsstar_sommerfeld_derivation_2026_06_12.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from functools import lru_cache

import numpy as np
from numpy.polynomial.legendre import leggauss


# Landed finite-flux boundary anchor from PR #3797.
LANDED_Q = 24
LANDED_GL_ORDER = 160
LANDED_ROOT_M0_T02_FROZEN = 1.7086
LANDED_ROOT_ABS_TOL = 1.5e-2

# Mirrored two-band Harper/PT constants.
T_HOP = 1.0
Q_HARPER = 24
LX = Q_HARPER
LY = 2
N_SITE = LX * LY
PT_GL_ORDER = 20

MASSES = (0.0, 0.2, 0.3, 0.5)
EPS_TEMPERATURES = (0.15, 0.2, 0.3, 0.4)
LOW_T_TEMPERATURES = (0.1, 0.15, 0.2)
MU2_FIT_TEMPERATURES = (0.1, 0.15, 0.2, 0.25)
BISECTION_LO = 1.2
BISECTION_HI = 2.4
BISECTION_STEPS = 60

# Frozen anchors/tolerances selected after the fixed GL=20 calibration pass.
PT_ROOT_M0_T02_FROZEN = 1.631150561591
PT_ROOT_M0_T02_TOL = 1.0e-9
EPS_T02_FROZEN = 1.6247
EPS_T02_ABS_TOL = 1.0e-3
ANTI_FAB_INTERBAND_MIN = 1.0e-1

# T=0 Fermi-surface quadrature: fixed GL=20 table and fixed Gaussian surface
# delta.  The window [1.48, 1.56] is the predeclared branch connected to the
# low-T roots, avoiding unrelated finite-grid surface roots.
SURFACE_DELTA_ETA = 5.0e-2
T0_BRANCH_LO = 1.48
T0_BRANCH_HI = 1.56
D1_EXTRAP_ABS_TOL = 1.5e-2

# Fixed native Sommerfeld finite-difference controls.
SOMMERFELD_DERIV_H = 2.0e-2
D2_NEGATIVE_REL_MISMATCH_MIN = 2.0
D2_OPPOSITE_SIGN_MARGIN = 1.0
D3_NEGATIVE_REL_MISMATCH_MIN = 4.0

SITE_SIGNS = np.array(
    [1.0 if (x + y) % 2 == 0 else -1.0 for x in range(LX) for y in range(LY)]
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    """Gate a computed quantity against a fixed labeled tolerance or threshold."""

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


@lru_cache(maxsize=None)
def landed_gl_rule(n: int) -> tuple[np.ndarray, np.ndarray]:
    nodes, weights = leggauss(n)
    return nodes.astype(float), weights.astype(float) * 0.5


def landed_harper_matrix(q: int, kx: float, ky: float) -> np.ndarray:
    b_field = 2.0 * math.pi / float(q)
    h = np.zeros((q, q), dtype=np.complex128)
    sites = np.arange(q, dtype=float)
    h[sites.astype(int), sites.astype(int)] = -2.0 * np.cos(ky + b_field * sites)
    for site in range(q - 1):
        h[site, site + 1] = -1.0
        h[site + 1, site] = -1.0
    wrap = -np.exp(-1j * kx * q)
    h[0, q - 1] = np.conjugate(wrap)
    h[q - 1, 0] = wrap
    return h


@lru_cache(maxsize=None)
def landed_zero_spectrum(n: int) -> tuple[np.ndarray, np.ndarray]:
    nodes, weights = landed_gl_rule(n)
    kx_nodes = math.pi * nodes
    ky_nodes = math.pi * nodes
    eps = np.empty(n * n, dtype=float)
    weights_2d = np.empty(n * n, dtype=float)
    pos = 0
    for ix, kx in enumerate(kx_nodes):
        for iy, ky in enumerate(ky_nodes):
            eps[pos] = -2.0 * (math.cos(float(kx)) + math.cos(float(ky)))
            weights_2d[pos] = weights[ix] * weights[iy]
            pos += 1
    return eps, weights_2d


@lru_cache(maxsize=None)
def landed_flux_spectrum(q: int, n: int) -> tuple[np.ndarray, np.ndarray]:
    nodes, weights = landed_gl_rule(n)
    kx_nodes = (math.pi / float(q)) * nodes
    ky_nodes = math.pi * nodes
    eps = np.empty((n * n, q), dtype=float)
    weights_2d = np.empty(n * n, dtype=float)
    pos = 0
    for ix, kx in enumerate(kx_nodes):
        for iy, ky in enumerate(ky_nodes):
            eps[pos, :] = np.linalg.eigvalsh(
                landed_harper_matrix(q, float(kx), float(ky))
            )
            weights_2d[pos] = weights[ix] * weights[iy]
            pos += 1
    return eps, weights_2d


def landed_staggered_energies(spinless_eps: np.ndarray, mass: float) -> np.ndarray:
    if mass == 0.0:
        return spinless_eps
    magnitudes = np.sqrt(spinless_eps * spinless_eps + mass * mass)
    return np.where(spinless_eps < 0.0, -magnitudes, magnitudes)


def landed_grand_potential(
    energies: np.ndarray,
    weights: np.ndarray,
    mu: float,
    temperature: float,
    bands_per_site: float,
) -> float:
    scaled = (mu - energies) / temperature
    terms = -temperature * np.logaddexp(0.0, scaled)
    if terms.ndim == 1:
        return float(np.sum(weights * terms) / bands_per_site)
    return float(np.sum(weights * np.sum(terms, axis=1)) / bands_per_site)


def landed_omega_zero(mu: float, mass: float, temperature: float, n: int) -> float:
    eps, weights = landed_zero_spectrum(n)
    energies = landed_staggered_energies(eps, mass)
    return landed_grand_potential(energies, weights, mu, temperature, 1.0)


def landed_omega_flux(
    q: int, mu: float, mass: float, temperature: float, n: int
) -> float:
    eps, weights = landed_flux_spectrum(q, n)
    energies = landed_staggered_energies(eps, mass)
    return landed_grand_potential(energies, weights, mu, temperature, float(q))


def landed_chi(q: int, mu: float, mass: float, temperature: float, n: int) -> float:
    b_field = 2.0 * math.pi / float(q)
    return 2.0 * (
        landed_omega_flux(q, mu, mass, temperature, n)
        - landed_omega_zero(mu, mass, temperature, n)
    ) / (b_field * b_field)


def landed_positive_boundary_root() -> float:
    left = BISECTION_LO
    right = BISECTION_HI
    left_value = landed_chi(LANDED_Q, left, 0.0, 0.2, LANDED_GL_ORDER)
    for _ in range(BISECTION_STEPS):
        midpoint = 0.5 * (left + right)
        midpoint_value = landed_chi(
            LANDED_Q, midpoint, 0.0, 0.2, LANDED_GL_ORDER
        )
        if left_value * midpoint_value <= 0.0:
            right = midpoint
        else:
            left = midpoint
            left_value = midpoint_value
    return 0.5 * (left + right)


def site_index(x: int, y: int) -> int:
    return (x % LX) * LY + (y % LY)


def gl_average_nodes_weights(n: int) -> tuple[np.ndarray, np.ndarray]:
    x, w = leggauss(n)
    return np.pi * x, 0.5 * w


def fermi_occupation(energy: np.ndarray, mu: float, temp: float) -> np.ndarray:
    z = np.clip((energy - mu) / temp, -60.0, 60.0)
    return 1.0 / (1.0 + np.exp(z))


def grand_kernel_second_derivative(
    energy: np.ndarray, mu: float, temp: float
) -> np.ndarray:
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


def harper_h0_h1_h2(
    kx: float, ky: float, mass: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
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
class PTPoint:
    weight_per_site: float
    eig: np.ndarray
    h2_diag: np.ndarray
    h1_abs2: np.ndarray
    interband_mask: np.ndarray


@dataclass(frozen=True)
class MassTables:
    mass: float
    pt_points: tuple[PTPoint, ...]


@dataclass(frozen=True)
class PTValue:
    full: float
    intraband: float
    interband: float


@dataclass(frozen=True)
class RootRow:
    mass: float
    temperature: float
    root: float
    chi_at_root: float
    interband_at_root: float


@dataclass(frozen=True)
class SurfaceTable:
    weight: np.ndarray
    eig: np.ndarray
    curvature_kernel: np.ndarray
    h1_diag_abs2: np.ndarray


def build_mass_tables(mass: float, gl_order: int) -> MassTables:
    nodes, weights = gl_average_nodes_weights(gl_order)
    pt_points: list[PTPoint] = []

    for ix, kx in enumerate(nodes):
        for iy, ky in enumerate(nodes):
            weight_per_site = float(weights[ix] * weights[iy] / N_SITE)
            h0, h1, h2 = harper_h0_h1_h2(float(kx), float(ky), mass)
            eig, vec = np.linalg.eigh(h0)
            h1_eig = vec.conjugate().T @ h1 @ vec
            h2_eig = vec.conjugate().T @ h2 @ vec
            signs = np.sign(eig)
            interband_mask = (signs[:, None] * signs[None, :]) < 0.0
            pt_points.append(
                PTPoint(
                    weight_per_site=weight_per_site,
                    eig=eig,
                    h2_diag=np.real(np.diag(h2_eig)),
                    h1_abs2=np.abs(h1_eig) ** 2,
                    interband_mask=interband_mask,
                )
            )

    return MassTables(mass=mass, pt_points=tuple(pt_points))


def build_surface_table(table: MassTables) -> SurfaceTable:
    weights: list[float] = []
    eig_rows: list[np.ndarray] = []
    kernel_rows: list[np.ndarray] = []
    diag_rows: list[np.ndarray] = []

    for point in table.pt_points:
        eig = point.eig
        diff = eig[:, None] - eig[None, :]
        offdiag = np.abs(diff) > 1.0e-10
        denom = np.where(offdiag, diff, 1.0)
        curvature_kernel = 2.0 * point.h2_diag + 2.0 * np.sum(
            np.where(offdiag, point.h1_abs2 / denom, 0.0), axis=1
        )
        weights.append(point.weight_per_site)
        eig_rows.append(eig)
        kernel_rows.append(curvature_kernel)
        diag_rows.append(np.diag(point.h1_abs2))

    return SurfaceTable(
        weight=np.array(weights, dtype=float)[:, None],
        eig=np.array(eig_rows, dtype=float),
        curvature_kernel=np.array(kernel_rows, dtype=float),
        h1_diag_abs2=np.array(diag_rows, dtype=float),
    )


def pt_chi(mu: float, temp: float, points: tuple[PTPoint, ...]) -> PTValue:
    full_total = 0.0
    intra_total = 0.0
    inter_total = 0.0

    for point in points:
        eig = point.eig
        fp = fermi_occupation(eig, mu, temp)
        fpp = grand_kernel_second_derivative(eig, mu, temp)
        diff = eig[:, None] - eig[None, :]
        fp_diff = fp[:, None] - fp[None, :]

        kernel = np.empty_like(diff)
        offdiag = np.abs(diff) > 1.0e-10
        kernel[offdiag] = fp_diff[offdiag] / diff[offdiag]
        degenerate_limit = 0.5 * (fpp[:, None] + fpp[None, :])
        kernel[~offdiag] = degenerate_limit[~offdiag]

        h1_term_matrix = kernel * point.h1_abs2
        h1_term = float(np.sum(h1_term_matrix))
        inter_term = float(np.sum(h1_term_matrix[point.interband_mask]))
        seagull = float(2.0 * np.sum(fp * point.h2_diag))

        full = seagull + h1_term
        full_total += point.weight_per_site * full
        inter_total += point.weight_per_site * inter_term
        intra_total += point.weight_per_site * (full - inter_term)

    return PTValue(full=full_total, intraband=intra_total, interband=inter_total)


def sign_bracketed(left_value: float, right_value: float) -> bool:
    return (
        np.isfinite(left_value)
        and np.isfinite(right_value)
        and left_value * right_value <= 0.0
    )


def pt_boundary_root(table: MassTables, temperature: float) -> RootRow:
    left = BISECTION_LO
    right = BISECTION_HI
    left_value = pt_chi(left, temperature, table.pt_points).full
    right_value = pt_chi(right, temperature, table.pt_points).full
    if not sign_bracketed(left_value, right_value):
        return RootRow(table.mass, temperature, math.nan, math.nan, math.nan)

    for _ in range(BISECTION_STEPS):
        midpoint = 0.5 * (left + right)
        midpoint_value = pt_chi(midpoint, temperature, table.pt_points).full
        if left_value * midpoint_value <= 0.0:
            right = midpoint
            right_value = midpoint_value
        else:
            left = midpoint
            left_value = midpoint_value

    root = 0.5 * (left + right)
    value = pt_chi(root, temperature, table.pt_points)
    return RootRow(table.mass, temperature, root, value.full, value.interband)


def fit_max_relative_residual(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, float]:
    coeffs = np.linalg.lstsq(x, y, rcond=None)[0]
    predicted = x @ coeffs
    residual = float(np.max(np.abs(y - predicted) / np.maximum(np.abs(y), 1.0e-15)))
    return coeffs, residual


def surface_delta(surface: SurfaceTable, mu: float) -> np.ndarray:
    eta = SURFACE_DELTA_ETA
    return (1.0 / (eta * math.sqrt(math.pi))) * np.exp(
        -((surface.eig - mu) / eta) ** 2
    )


def surface_phi(surface: SurfaceTable, mu: float) -> float:
    return float(
        np.sum(surface.weight * surface_delta(surface, mu) * surface.curvature_kernel)
    )


def surface_psi(surface: SurfaceTable, mu: float) -> float:
    return float(
        np.sum(surface.weight * surface_delta(surface, mu) * surface.h1_diag_abs2)
    )


def t0_response(surface: SurfaceTable, mu: float) -> float:
    occupied = surface.eig < mu
    bulk = float(np.sum(surface.weight * occupied * surface.curvature_kernel))
    return bulk - surface_psi(surface, mu)


def scalar_derivative(fn, x: float, h: float) -> float:
    return (fn(x + h) - fn(x - h)) / (2.0 * h)


def scalar_second_derivative(fn, x: float, h: float) -> float:
    return (fn(x + h) - 2.0 * fn(x) + fn(x - h)) / (h * h)


def t0_branch_root(surface: SurfaceTable) -> tuple[float, float, float, float, float]:
    left = T0_BRANCH_LO
    right = T0_BRANCH_HI
    left_value = t0_response(surface, left)
    right_value = t0_response(surface, right)
    branch_left_value = left_value
    branch_right_value = right_value
    if not sign_bracketed(left_value, right_value):
        return math.nan, branch_left_value, branch_right_value, left_value, right_value

    for _ in range(BISECTION_STEPS):
        midpoint = 0.5 * (left + right)
        midpoint_value = t0_response(surface, midpoint)
        if left_value * midpoint_value <= 0.0:
            right = midpoint
            right_value = midpoint_value
        else:
            left = midpoint
            left_value = midpoint_value

    return (
        0.5 * (left + right),
        branch_left_value,
        branch_right_value,
        left_value,
        right_value,
    )


def sommerfeld_alpha(surface: SurfaceTable, mu0: float) -> tuple[float, float, float]:
    h = SOMMERFELD_DERIV_H
    phi_prime = scalar_derivative(lambda mu: surface_phi(surface, mu), mu0, h)
    psi_prime = scalar_derivative(lambda mu: surface_psi(surface, mu), mu0, h)
    psi_second = scalar_second_derivative(lambda mu: surface_psi(surface, mu), mu0, h)
    response_prime = surface_phi(surface, mu0) - psi_prime
    response_t2_coeff = (math.pi * math.pi / 6.0) * (phi_prime - psi_second)
    beta_mu = -response_t2_coeff / response_prime
    alpha_mu2 = 2.0 * mu0 * beta_mu
    return alpha_mu2, response_prime, response_t2_coeff


def run() -> int:
    print("eps* T=0/Sommerfeld boundary verifier")
    print(
        f"landed anchor: q={LANDED_Q}, GL={LANDED_GL_ORDER}; "
        f"PT cell: Q={Q_HARPER}, Ly={LY}, N={N_SITE}, GL={PT_GL_ORDER}; "
        f"T0 surface eta={SURFACE_DELTA_ETA}"
    )

    print("\nS0 ANCHOR GATES")
    landed_root = landed_positive_boundary_root()
    landed_delta = abs(landed_root - LANDED_ROOT_M0_T02_FROZEN)
    print(
        f"LANDED_ROOT m=0.000 T=0.200 mu={landed_root:.12f} "
        f"frozen={LANDED_ROOT_M0_T02_FROZEN:.12f} "
        f"abs_delta={landed_delta:.12e}"
    )
    check(
        "S0 landed 1.7086-adjacent finite-flux root",
        landed_delta <= LANDED_ROOT_ABS_TOL,
        f"abs_delta={landed_delta:.3e}, tol={LANDED_ROOT_ABS_TOL:.1e}",
    )

    tables: dict[float, MassTables] = {
        mass: build_mass_tables(mass, PT_GL_ORDER) for mass in MASSES
    }
    anchor_row = pt_boundary_root(tables[0.0], 0.2)
    pt_anchor_delta = abs(anchor_row.root - PT_ROOT_M0_T02_FROZEN)
    print(
        f"PT_ROOT m=0.000 T=0.200 mu={anchor_row.root:.12f} "
        f"frozen={PT_ROOT_M0_T02_FROZEN:.12f} "
        f"abs_delta={pt_anchor_delta:.12e} "
        f"interband={anchor_row.interband_at_root:+.12e}"
    )
    check(
        "S0 PT m=0,T=0.2 root reproduces the fixed GL=20 anchor",
        pt_anchor_delta <= PT_ROOT_M0_T02_TOL,
        f"abs_delta={pt_anchor_delta:.3e}, tol={PT_ROOT_M0_T02_TOL:.1e}",
    )
    check(
        "S0 anti-fabrication: PT interband term is nonzero at the root",
        abs(anchor_row.interband_at_root) >= ANTI_FAB_INTERBAND_MIN,
        f"|interband|={abs(anchor_row.interband_at_root):.3e}, "
        f"min={ANTI_FAB_INTERBAND_MIN:.1e}",
    )

    rows: list[RootRow] = []
    for temperature in EPS_TEMPERATURES:
        for mass in MASSES:
            row = pt_boundary_root(tables[mass], temperature)
            rows.append(row)
            print(
                f"ROOT_GRID m={mass:.3f} T={temperature:.3f} "
                f"mu*_PT={row.root:.12f} chi={row.chi_at_root:+.3e} "
                f"interband={row.interband_at_root:+.3e}"
            )

    eps_rows: list[tuple[float, float, float]] = []
    for temperature in EPS_TEMPERATURES:
        subset = [row for row in rows if row.temperature == temperature]
        collapse_values = np.array(
            [row.root * row.root - row.mass * row.mass for row in subset],
            dtype=float,
        )
        eps2 = float(np.mean(collapse_values))
        spread = float(np.max(np.abs(collapse_values - eps2)) / eps2)
        eps_rows.append((temperature, math.sqrt(eps2), spread))

    eps_t02 = next(eps for temperature, eps, _spread in eps_rows if temperature == 0.2)
    eps_t02_delta = abs(eps_t02 - EPS_T02_FROZEN)
    print(
        f"EPS_ANCHOR T=0.200 eps*={eps_t02:.12f} "
        f"frozen={EPS_T02_FROZEN:.12f} abs_delta={eps_t02_delta:.12e}"
    )
    check(
        "S0 landed eps*(0.2)=1.6247 anchor",
        eps_t02_delta <= EPS_T02_ABS_TOL,
        f"abs_delta={eps_t02_delta:.3e}, tol={EPS_T02_ABS_TOL:.1e}",
    )

    print("\nS1 T=0 FERMI-SURFACE BRANCH")
    surface = build_surface_table(tables[0.0])
    mu0_surface, t0_branch_lo, t0_branch_hi, t0_left, t0_right = t0_branch_root(
        surface
    )
    print(
        f"T0_BRANCH interval=[{T0_BRANCH_LO:.2f},{T0_BRANCH_HI:.2f}] "
        f"R(lo)={t0_branch_lo:+.12e} R(hi)={t0_branch_hi:+.12e} "
        f"final_bracket=({t0_left:+.12e},{t0_right:+.12e}) "
        f"mu0_surface={mu0_surface:.12f} "
        f"R(mu0)={t0_response(surface, mu0_surface):+.12e}"
    )
    check(
        "D1 fixed T=0 surface branch contains a response sign change",
        np.isfinite(mu0_surface)
        and T0_BRANCH_LO <= mu0_surface <= T0_BRANCH_HI,
        f"mu0={mu0_surface:.12f}, branch=[{T0_BRANCH_LO:.2f},{T0_BRANCH_HI:.2f}]",
    )

    low_t_rows = [
        pt_boundary_root(tables[0.0], temperature)
        for temperature in LOW_T_TEMPERATURES
    ]
    low_t_values = np.array([row.temperature for row in low_t_rows], dtype=float)
    low_t_roots = np.array([row.root for row in low_t_rows], dtype=float)
    quadratic_design = np.vstack(
        [np.ones_like(low_t_values), low_t_values**2, low_t_values**4]
    ).T
    quadratic_coeffs = np.linalg.solve(quadratic_design, low_t_roots)
    mu_extrap = float(quadratic_coeffs[0])
    linear_t2_design = np.vstack([np.ones_like(low_t_values), low_t_values**2]).T
    linear_t2_coeffs = np.linalg.lstsq(linear_t2_design, low_t_roots, rcond=None)[0]
    linear_t2_residual = float(
        np.max(np.abs(low_t_roots - linear_t2_design @ linear_t2_coeffs))
    )
    d1_delta = abs(mu_extrap - mu0_surface)
    print(
        "D1_LOW_T_ROOTS "
        + " ".join(
            f"T={row.temperature:.3f}:mu={row.root:.12f}" for row in low_t_rows
        )
    )
    print(
        f"D1_EXTRAP mu(T)=a+bT^2+cT^4: a={mu_extrap:.12f} "
        f"b={quadratic_coeffs[1]:.12f} c={quadratic_coeffs[2]:.12f}; "
        f"linear_T2_residual_scale={linear_t2_residual:.12e}; "
        f"|a-mu0_surface|={d1_delta:.12e}"
    )
    check(
        "D1 T->0 quadratic extrapolation matches the fixed T=0 surface branch",
        d1_delta <= D1_EXTRAP_ABS_TOL,
        f"delta={d1_delta:.3e}, tol={D1_EXTRAP_ABS_TOL:.1e}",
    )

    print("\nS2 SOMMERFELD COEFFICIENT")
    mu2_fit_rows = [
        pt_boundary_root(tables[0.0], temperature)
        for temperature in MU2_FIT_TEMPERATURES
    ]
    fit_t = np.array([row.temperature for row in mu2_fit_rows], dtype=float)
    fit_mu2 = np.array([row.root * row.root for row in mu2_fit_rows], dtype=float)
    mu2_design = np.vstack([np.ones_like(fit_t), fit_t * fit_t]).T
    mu2_coeffs, mu2_residual = fit_max_relative_residual(mu2_design, fit_mu2)
    measured_d_m0 = float(mu2_coeffs[1])

    alpha_analytic, response_prime, response_t2_coeff = sommerfeld_alpha(
        surface, mu0_surface
    )
    d2_rel_mismatch = abs(measured_d_m0 - alpha_analytic) / abs(measured_d_m0)
    print(
        "D2_MU2_FIT "
        + " ".join(
            f"T={row.temperature:.3f}:mu={row.root:.12f}" for row in mu2_fit_rows
        )
    )
    print(
        f"D2_COEFF measured_d_m0={measured_d_m0:.12f} "
        f"fit_c={mu2_coeffs[0]:.12f} max_rel_residual={mu2_residual:.12e}; "
        f"alpha_analytic={alpha_analytic:.12f} "
        f"R0_prime={response_prime:.12e} C_T2={response_t2_coeff:.12e} "
        f"rel_mismatch={d2_rel_mismatch:.12e}"
    )
    check(
        "D2 NEGATIVE: fixed Sommerfeld alpha has opposite sign from measured d",
        measured_d_m0 >= D2_OPPOSITE_SIGN_MARGIN
        and alpha_analytic <= -D2_OPPOSITE_SIGN_MARGIN,
        f"measured_d={measured_d_m0:.3e}, alpha={alpha_analytic:.3e}, "
        f"margin={D2_OPPOSITE_SIGN_MARGIN:.1e}",
    )
    check(
        "D2 NEGATIVE: analytic-vs-measured mismatch exceeds fixed 200% floor",
        d2_rel_mismatch >= D2_NEGATIVE_REL_MISMATCH_MIN,
        f"rel_mismatch={d2_rel_mismatch:.3e}, "
        f"floor={D2_NEGATIVE_REL_MISMATCH_MIN:.1e}",
    )

    print("\nS3 WAVE-10 REGRESSION CROSS-CHECK")
    eps_t = np.array([row[0] for row in eps_rows], dtype=float)
    eps_values = np.array([row[1] for row in eps_rows], dtype=float)
    eps2_design = np.vstack([np.ones_like(eps_t), eps_t * eps_t]).T
    eps2_coeffs, eps2_residual = fit_max_relative_residual(
        eps2_design, eps_values * eps_values
    )
    wave10_d = float(eps2_coeffs[1])
    d3_rel_mismatch = abs(wave10_d - alpha_analytic) / abs(wave10_d)
    m0_vs_wave_rel = abs(measured_d_m0 - wave10_d) / measured_d_m0
    for temperature, eps, spread in eps_rows:
        print(
            f"EPS_TABLE T={temperature:.3f} eps*={eps:.12f} "
            f"collapse_spread={spread:.12e}"
        )
    print(
        f"D3_COEFF wave10_d={wave10_d:.12f} "
        f"eps2_fit_c={eps2_coeffs[0]:.12f} "
        f"eps2_max_rel_residual={eps2_residual:.12e}; "
        f"alpha_analytic={alpha_analytic:.12f} "
        f"wave_vs_alpha_rel_mismatch={d3_rel_mismatch:.12e}; "
        f"m0_d_vs_wave10_d_rel={m0_vs_wave_rel:.12e}"
    )
    check(
        "D3 NEGATIVE: wave-10 d is not consistent with fixed alpha",
        d3_rel_mismatch >= D3_NEGATIVE_REL_MISMATCH_MIN,
        f"rel_mismatch={d3_rel_mismatch:.3e}, "
        f"floor={D3_NEGATIVE_REL_MISMATCH_MIN:.1e}",
    )

    print(f"\nTOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(run())
