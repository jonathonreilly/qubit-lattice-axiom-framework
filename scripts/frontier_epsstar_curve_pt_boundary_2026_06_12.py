#!/usr/bin/env python3
"""Class-A finite-dimensional PT boundary eps*(T) curve verifier.

Companion note:
    docs/EPSSTAR_CURVE_PT_BOUNDARY_QUADRATURE_COLLAPSE_BOUNDED_NOTE_2026-06-12.md

Run:
    python3 scripts/frontier_epsstar_curve_pt_boundary_2026_06_12.py
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from functools import lru_cache

import numpy as np
from numpy.polynomial.legendre import leggauss


# Landed finite-flux boundary anchor from the d=2 mass-collapse runner.
LANDED_Q = 24
LANDED_GL_ORDER = 160
LANDED_ROOT_M0_T02 = 1.708
LANDED_ROOT_ABS_TOL = 2.0e-2

# Fixed two-band Harper/PT constants used by the parent surface note.
T_HOP = 1.0
Q_HARPER = 24
LX = Q_HARPER
LY = 2
N_SITE = LX * LY
PT_GL_ORDER = 20

MASSES = (0.0, 0.2, 0.3, 0.5)
TEMPERATURES = (0.15, 0.2, 0.3, 0.4)
BISECTION_LO = 1.2
BISECTION_HI = 2.4
BISECTION_STEPS = 60

# Frozen gates, fixed after the GL=20 calibration pass:
# measured max collapse spread 1.5312%; measured best regression residual 0.0959%.
COLLAPSE_SPREAD_TOL = 2.0e-2
REGRESSION_MAX_REL_TOL = 2.0e-3
ANTI_FAB_INTERBAND_MIN = 1.0e-1

SITE_SIGNS = np.array(
    [1.0 if (x + y) % 2 == 0 else -1.0 for x in range(LX) for y in range(LY)]
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    """Gate a computed quantity against a fixed labeled tolerance or claim."""

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
    right_value = landed_chi(LANDED_Q, right, 0.0, 0.2, LANDED_GL_ORDER)
    for _ in range(BISECTION_STEPS):
        midpoint = 0.5 * (left + right)
        midpoint_value = landed_chi(
            LANDED_Q, midpoint, 0.0, 0.2, LANDED_GL_ORDER
        )
        if left_value * midpoint_value <= 0.0:
            right = midpoint
            right_value = midpoint_value
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

            # -t exp(i B x) = -t [1 + iBx - (B^2 x^2)/2 + O(B^3)].
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


def pt_boundary_root(table: MassTables, temperature: float, label: str) -> RootRow:
    left = BISECTION_LO
    right = BISECTION_HI
    left_value = pt_chi(left, temperature, table.pt_points).full
    right_value = pt_chi(right, temperature, table.pt_points).full
    bracket_ok = sign_bracketed(left_value, right_value)
    check(
        f"{label}: fixed bracket [{BISECTION_LO:.1f},{BISECTION_HI:.1f}] contains a PT zero",
        bracket_ok,
        f"chi_lo={left_value:+.6e}, chi_hi={right_value:+.6e}",
    )
    if not bracket_ok:
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


def run() -> int:
    print("PT epsstar boundary curve verifier")
    print(
        f"landed anchor: q={LANDED_Q}, GL={LANDED_GL_ORDER}; "
        f"PT cell: Q={Q_HARPER}, Ly={LY}, N={N_SITE}, GL={PT_GL_ORDER}"
    )

    print("\nS0 ANCHORS")
    landed_root = landed_positive_boundary_root()
    landed_delta = abs(landed_root - LANDED_ROOT_M0_T02)
    print(
        f"LANDED_ANCHOR m=0.000 T=0.200 mu*={landed_root:.12f} "
        f"frozen={LANDED_ROOT_M0_T02:.12f} abs_delta={landed_delta:.12e}"
    )
    check(
        "S0 landed finite-flux boundary root matches frozen 1.708 within 2e-2",
        landed_delta <= LANDED_ROOT_ABS_TOL,
        f"abs_delta={landed_delta:.3e}, tol={LANDED_ROOT_ABS_TOL:.1e}",
    )

    tables: dict[float, MassTables] = {
        0.0: build_mass_tables(0.0, PT_GL_ORDER),
    }
    anchor_row = pt_boundary_root(tables[0.0], 0.2, "S0 PT anchor m=0.00 T=0.20")
    print(
        f"PT_ANCHOR m=0.000 T=0.200 mu*_PT={anchor_row.root:.12f} "
        f"chi_PT={anchor_row.chi_at_root:+.6e} "
        f"interband={anchor_row.interband_at_root:+.6e}"
    )
    check(
        "S0 anti-fabrication: PT interband term is nontrivial at the m=0,T=0.2 root",
        abs(anchor_row.interband_at_root) >= ANTI_FAB_INTERBAND_MIN,
        f"|interband|={abs(anchor_row.interband_at_root):.3e}, "
        f"min={ANTI_FAB_INTERBAND_MIN:.1e}",
    )

    print("\nS1 PT BOUNDARY GRID")
    for mass in MASSES:
        if mass not in tables:
            tables[mass] = build_mass_tables(mass, PT_GL_ORDER)

    rows: list[RootRow] = []
    for temperature in TEMPERATURES:
        for mass in MASSES:
            row = pt_boundary_root(
                tables[mass], temperature, f"S1 m={mass:.2f} T={temperature:.2f}"
            )
            rows.append(row)
            print(
                f"ROOT m={mass:.3f} T={temperature:.3f} "
                f"mu*_PT={row.root:.12f} chi_PT={row.chi_at_root:+.6e} "
                f"interband={row.interband_at_root:+.6e}"
            )

    print("\nS2 QUADRATURE COLLAPSE")
    eps_rows: list[tuple[float, float, float]] = []
    max_spread = 0.0
    for temperature in TEMPERATURES:
        subset = [row for row in rows if row.temperature == temperature]
        collapse_values = np.array(
            [row.root * row.root - row.mass * row.mass for row in subset],
            dtype=float,
        )
        eps2 = float(np.mean(collapse_values))
        spread = float(np.max(np.abs(collapse_values - eps2)) / eps2)
        eps = math.sqrt(eps2)
        max_spread = max(max_spread, spread)
        eps_rows.append((temperature, eps, spread))
        print(
            f"COLLAPSE T={temperature:.3f} eps*(T)^2={eps2:.12f} "
            f"eps*(T)={eps:.12f} rel_spread={spread:.12e}"
        )
        check(
            f"S2 collapse spread at T={temperature:.2f} is below frozen 2%",
            np.isfinite(spread) and spread <= COLLAPSE_SPREAD_TOL,
            f"spread={spread:.3e}, tol={COLLAPSE_SPREAD_TOL:.1e}",
        )
    print(
        f"S2 measured max per-T spread={max_spread:.12e}; "
        f"frozen bound={COLLAPSE_SPREAD_TOL:.1e}"
    )

    print("\nS3 EPSSTAR CURVE CHARACTERIZATION")
    temperatures = np.array([row[0] for row in eps_rows], dtype=float)
    eps_values = np.array([row[1] for row in eps_rows], dtype=float)
    for temperature, eps, spread in eps_rows:
        print(
            f"EPS_TABLE T={temperature:.3f} eps*(T)={eps:.12f} "
            f"collapse_spread={spread:.12e}"
        )

    monotone = bool(np.all(np.diff(eps_values) > 0.0))
    check(
        "S3 eps*(T) is strictly increasing on T={0.15,0.2,0.3,0.4}",
        monotone,
        "eps*(T)=" + ", ".join(f"{value:.12f}" for value in eps_values),
    )

    linear_design = np.vstack([np.ones_like(temperatures), temperatures]).T
    linear_coeffs, linear_residual = fit_max_relative_residual(
        linear_design, eps_values
    )
    eps2_values = eps_values * eps_values
    eps2_design = np.vstack([np.ones_like(temperatures), temperatures * temperatures]).T
    eps2_coeffs, eps2_residual = fit_max_relative_residual(eps2_design, eps2_values)

    if eps2_residual <= linear_residual:
        better_label = "eps*(T)^2 = c + d*T^2"
        better_residual = eps2_residual
    else:
        better_label = "eps*(T) = a + b*T"
        better_residual = linear_residual

    print(
        "REGRESSION linear_eps: "
        f"a={linear_coeffs[0]:.12f} b={linear_coeffs[1]:.12f} "
        f"max_rel_residual={linear_residual:.12e}"
    )
    print(
        "REGRESSION eps2_T2: "
        f"c={eps2_coeffs[0]:.12f} d={eps2_coeffs[1]:.12f} "
        f"max_rel_residual={eps2_residual:.12e}"
    )
    print(f"REGRESSION better_characterization={better_label}")
    check(
        "S3 better fixed-form regression characterization has max relative residual below 2e-3",
        better_residual <= REGRESSION_MAX_REL_TOL,
        f"better={better_label}, best_residual={better_residual:.3e}, "
        f"linear_residual={linear_residual:.3e}, eps2_T2_residual={eps2_residual:.3e}, "
        f"tol={REGRESSION_MAX_REL_TOL:.1e}",
    )

    print(f"\nTOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(run())
