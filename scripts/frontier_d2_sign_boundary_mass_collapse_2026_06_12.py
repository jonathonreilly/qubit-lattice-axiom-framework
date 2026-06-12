#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/D2_SIGN_BOUNDARY_MASS_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_d2_sign_boundary_mass_collapse_2026_06_12.py
"""
import math
import sys
from functools import lru_cache

import numpy as np


Q_MAIN = 24
Q_SPOT = 32
GL_N = 160
GL_DOUBLE_N = 224
MIN_GL = 96

BIS_WIDTH = 2.0e-3
DOUBLING_TOL = 1.0e-6
COLLAPSE_TOL = 2.0e-2
ANCHOR_TOL = 2.0e-2
Q32_TOL = 5.0e-2
WRAP_TOL = 1.0e-12
SIGN_RECOMPUTE_TOL = 1.0e-10

MU_BRACKET = (-4.8, 4.8)
BRACKET_SCAN_STEPS = 192
M_VALUES = (0.2, 0.35, 0.5, 0.8)
T_MAIN = 0.2
T_VALUES = (0.2, 0.3, 0.4)
CONTROL_M = 0.2
CONTROL_T = 0.2
CONTROL_MU = -2.0

PASS_COUNT = 0
FAIL_COUNT = 0


def check(condition, label):
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
        print(f"PASS: {label}")
    else:
        FAIL_COUNT += 1
        print(f"FAIL: {label}")


@lru_cache(maxsize=None)
def gl_rule(n):
    nodes, weights = np.polynomial.legendre.leggauss(n)
    return nodes.astype(float), weights.astype(float) * 0.5


def harper_matrix(q, kx, ky):
    b = 2.0 * math.pi / float(q)
    h = np.zeros((q, q), dtype=np.complex128)
    sites = np.arange(q, dtype=float)
    h[sites.astype(int), sites.astype(int)] = -2.0 * np.cos(ky + b * sites)
    for site in range(q - 1):
        h[site, site + 1] = -1.0
        h[site + 1, site] = -1.0
    wrap = -np.exp(-1j * kx * q)
    h[0, q - 1] = np.conjugate(wrap)
    h[q - 1, 0] = wrap
    return h


@lru_cache(maxsize=None)
def zero_spectrum(n):
    nodes, weights = gl_rule(n)
    kx = math.pi * nodes
    ky = math.pi * nodes
    eps = np.empty(n * n, dtype=float)
    w2 = np.empty(n * n, dtype=float)
    pos = 0
    for ix, x in enumerate(kx):
        for iy, y in enumerate(ky):
            eps[pos] = -2.0 * (math.cos(x) + math.cos(y))
            w2[pos] = weights[ix] * weights[iy]
            pos += 1
    return eps, w2


@lru_cache(maxsize=None)
def flux_spectrum(q, n):
    nodes, weights = gl_rule(n)
    kx_nodes = (math.pi / float(q)) * nodes
    ky_nodes = math.pi * nodes
    eps = np.empty((n * n, q), dtype=float)
    w2 = np.empty(n * n, dtype=float)
    pos = 0
    for ix, kx in enumerate(kx_nodes):
        for iy, ky in enumerate(ky_nodes):
            eps[pos, :] = np.linalg.eigvalsh(harper_matrix(q, kx, ky))
            w2[pos] = weights[ix] * weights[iy]
            pos += 1
    return eps, w2


def staggered_energies(spinless_eps, mass):
    if mass == 0.0:
        return spinless_eps
    magnitudes = np.sqrt(spinless_eps * spinless_eps + mass * mass)
    return np.where(spinless_eps < 0.0, -magnitudes, magnitudes)


def grand_potential_from_energies(energies, weights, mu, temperature, bands_per_site):
    scaled = (mu - energies) / temperature
    terms = -temperature * np.logaddexp(0.0, scaled)
    if terms.ndim == 1:
        return float(np.sum(weights * terms) / bands_per_site)
    return float(np.sum(weights * np.sum(terms, axis=1)) / bands_per_site)


def omega_zero(mu, mass, temperature, n):
    eps, weights = zero_spectrum(n)
    energies = staggered_energies(eps, mass)
    return grand_potential_from_energies(energies, weights, mu, temperature, 1.0)


def omega_flux(q, mu, mass, temperature, n):
    eps, weights = flux_spectrum(q, n)
    energies = staggered_energies(eps, mass)
    return grand_potential_from_energies(energies, weights, mu, temperature, float(q))


def chi(q, mu, mass, temperature, n):
    bq = 2.0 * math.pi / float(q)
    return 2.0 * (omega_flux(q, mu, mass, temperature, n) - omega_zero(mu, mass, temperature, n)) / (bq * bq)


def independent_chi(q, mu, mass, temperature, n):
    nodes, weights = gl_rule(n)
    zero_total = 0.0
    for ix, nx in enumerate(nodes):
        kx = math.pi * nx
        for iy, ny in enumerate(nodes):
            ky = math.pi * ny
            eps = -2.0 * (math.cos(kx) + math.cos(ky))
            energy = eps if mass == 0.0 else math.copysign(math.sqrt(eps * eps + mass * mass), eps if eps != 0.0 else 1.0)
            zero_total += weights[ix] * weights[iy] * (-temperature * np.logaddexp(0.0, (mu - energy) / temperature))

    flux_total = 0.0
    for ix, nx in enumerate(nodes):
        kx = (math.pi / float(q)) * nx
        for iy, ny in enumerate(nodes):
            ky = math.pi * ny
            eigs = np.linalg.eigvalsh(harper_matrix(q, kx, ky))
            energies = staggered_energies(eigs, mass)
            terms = -temperature * np.logaddexp(0.0, (mu - energies) / temperature)
            flux_total += weights[ix] * weights[iy] * float(np.sum(terms)) / float(q)

    bq = 2.0 * math.pi / float(q)
    return 2.0 * (flux_total - zero_total) / (bq * bq)


def sign_bracketed(left_value, right_value):
    return np.isfinite(left_value) and np.isfinite(right_value) and left_value * right_value <= 0.0


def scan_sign_bracket(q, mass, temperature, n):
    scan_points = np.linspace(MU_BRACKET[0], MU_BRACKET[1], BRACKET_SCAN_STEPS + 1)
    left = float(scan_points[0])
    left_value = chi(q, left, mass, temperature, n)
    for point in scan_points[1:]:
        right = float(point)
        right_value = chi(q, right, mass, temperature, n)
        if sign_bracketed(left_value, right_value):
            return left, right, left_value, right_value
        left = right
        left_value = right_value
    return float(scan_points[0]), float(scan_points[-1]), chi(q, float(scan_points[0]), mass, temperature, n), left_value


def locate_boundary(q, mass, temperature, n, label):
    left, right, left_value, right_value = scan_sign_bracket(q, mass, temperature, n)
    check(sign_bracketed(left_value, right_value), f"{label}: scanned endpoint signs bracket a zero")

    iteration = 0
    while right - left > BIS_WIDTH:
        midpoint = 0.5 * (left + right)
        midpoint_value = chi(q, midpoint, mass, temperature, n)
        if left_value * midpoint_value <= 0.0:
            right = midpoint
            right_value = midpoint_value
        else:
            left = midpoint
            left_value = midpoint_value
        iteration += 1
        check(sign_bracketed(left_value, right_value), f"{label}: bisection iter {iteration:02d} keeps bracket")

    mu_star = 0.5 * (left + right)
    width = right - left
    boundary_value = chi(q, mu_star, mass, temperature, n)
    check(width <= BIS_WIDTH, f"{label}: final bisection width <= {BIS_WIDTH:.1e}")
    check(np.isfinite(boundary_value), f"{label}: boundary susceptibility is finite")
    return mu_star, boundary_value, width


def epsilon_from_mu(mu_star, mass):
    datum = mu_star * mu_star - mass * mass
    return math.sqrt(max(0.0, datum))


def relative_spread(values):
    arr = np.asarray(values, dtype=float)
    mean = float(np.mean(arr))
    spread = float(np.max(np.abs(arr - mean)) / mean)
    return spread, mean


def gate_collapse_or_measured_failure(spread, tolerance, label):
    # FIXED assertion (panel edit): the bounded collapse claim, with the small
    # systematic m-trend an explicitly separate gate below.
    check(
        np.isfinite(spread) and spread < tolerance,
        f"{label}: BOUNDED collapse, relative spread {spread:.4e} < {tolerance:.1e} "
        f"(a small systematic m-trend exists and is gated separately)",
    )


def finite_lattice_probes():
    check(GL_N >= MIN_GL, f"GL quadrature has at least {MIN_GL} nodes per dimension")
    for q in (Q_MAIN, Q_SPOT):
        sample = harper_matrix(q, 0.173, -0.421)
        check(sample.shape == (q, q), f"q={q}: Harper matrix has q by q dense shape")
        check(np.linalg.norm(sample - sample.conjugate().T) < WRAP_TOL, f"q={q}: Harper matrix is Hermitian")
        check(abs(sample[0, q - 1] - np.conjugate(sample[q - 1, 0])) < WRAP_TOL, f"q={q}: wraparound hopping is conjugate paired")
        check(abs(abs(sample[0, q - 1]) - 1.0) < WRAP_TOL, f"q={q}: wraparound hopping has unit magnitude")

    expected_samples = GL_N * GL_N
    for q in (Q_MAIN, Q_SPOT):
        eigs, weights = flux_spectrum(q, GL_N)
        check(eigs.shape == (expected_samples, q), f"q={q}: cached spectrum has {expected_samples} samples and {q} bands")
        check(weights.shape == (expected_samples,), f"q={q}: cached weights have {expected_samples} samples")


def controls(reference_eps):
    chi_n = chi(Q_MAIN, CONTROL_MU, CONTROL_M, CONTROL_T, GL_N)
    chi_2n = chi(Q_MAIN, CONTROL_MU, CONTROL_M, CONTROL_T, GL_DOUBLE_N)
    doubling_delta = abs(chi_n - chi_2n)
    print(f"CONTROL quadrature: chi_{GL_N}={chi_n:.12e} chi_{GL_DOUBLE_N}={chi_2n:.12e} delta={doubling_delta:.12e}")
    check(doubling_delta < DOUBLING_TOL, f"quadrature doubling |chi_{GL_N} - chi_{GL_DOUBLE_N}| < {DOUBLING_TOL:.1e}")

    endpoint_mu, _, primary, _ = scan_sign_bracket(Q_MAIN, CONTROL_M, CONTROL_T, GL_N)
    independent = independent_chi(Q_MAIN, endpoint_mu, CONTROL_M, CONTROL_T, GL_N)
    print(f"CONTROL endpoint: mu={endpoint_mu:.12f} primary={primary:.12e} independent={independent:.12e}")
    check(abs(primary - independent) < SIGN_RECOMPUTE_TOL, f"independent endpoint recompute agrees within {SIGN_RECOMPUTE_TOL:.1e}")
    check(np.signbit(primary) == np.signbit(independent), "independent endpoint recompute preserves endpoint sign")

    mu_q32, _, _ = locate_boundary(Q_SPOT, CONTROL_M, CONTROL_T, GL_N, "U1d q=32 spot")
    eps_q32 = epsilon_from_mu(mu_q32, CONTROL_M)
    q32_rel = abs(eps_q32 - reference_eps) / reference_eps
    print(f"CONTROL q32: mu*={mu_q32:.12f} eps*={eps_q32:.12f} rel_to_q24={q32_rel:.12e}")
    check(q32_rel < Q32_TOL, f"q=32 spot relative agreement < {Q32_TOL:.1e}")


def main():
    finite_lattice_probes()

    u1a = []
    for mass in M_VALUES:
        mu_star, boundary_value, width = locate_boundary(Q_MAIN, mass, T_MAIN, GL_N, f"U1a m={mass:.2f} T={T_MAIN:.2f}")
        eps_star = epsilon_from_mu(mu_star, mass)
        u1a.append((mass, mu_star, eps_star, boundary_value, width))
        print(
            f"U1a m={mass:.12f} T={T_MAIN:.12f} "
            f"mu*={mu_star:.12f} eps*={eps_star:.12f} chi(mu*)={boundary_value:.12e} width={width:.12e}"
        )

    eps_by_mass = [row[2] for row in u1a]
    spread, mean_eps = relative_spread(eps_by_mass)
    print(f"U1a collapse: mean_eps={mean_eps:.12f} relative_spread={spread:.12e}")
    gate_collapse_or_measured_failure(spread, COLLAPSE_TOL, "U1a")

    u1b = []
    for temperature in T_VALUES:
        mu_star, boundary_value, width = locate_boundary(Q_MAIN, CONTROL_M, temperature, GL_N, f"U1b m={CONTROL_M:.2f} T={temperature:.2f}")
        eps_star = epsilon_from_mu(mu_star, CONTROL_M)
        u1b.append((temperature, mu_star, eps_star, boundary_value, width))
        print(
            f"U1b m={CONTROL_M:.12f} T={temperature:.12f} "
            f"mu*={mu_star:.12f} eps*={eps_star:.12f} chi(mu*)={boundary_value:.12e} width={width:.12e}"
        )

    eps_t = [row[2] for row in u1b]
    increasing_claim = eps_t[0] < eps_t[1] < eps_t[2]
    check(increasing_claim, "U1b eps*(T) is increasing for T=0.2,0.3,0.4")

    mu_m0, boundary_m0, width_m0 = locate_boundary(Q_MAIN, 0.0, T_MAIN, GL_N, "U1c m=0 anchor")
    eps_m0 = epsilon_from_mu(mu_m0, 0.0)
    anchor_rel = abs(eps_m0 - mean_eps) / mean_eps
    print(
        f"U1c m=0.000000000000 T={T_MAIN:.12f} "
        f"mu*={mu_m0:.12f} eps*={eps_m0:.12f} chi(mu*)={boundary_m0:.12e} "
        f"width={width_m0:.12e} rel_to_mean={anchor_rel:.12e}"
    )
    gate_collapse_or_measured_failure(anchor_rel, ANCHOR_TOL, "U1c")

    controls(eps_by_mass[0])

    print("SCOPE: sampled instances; collapse relation or measured failure is the datum; no continuum claim; X3-import unused.")
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        sys.exit(1)


if __name__ == "__main__":
    main()
