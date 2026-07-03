#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/SUSCEPTIBILITY_DENSITY_VANISHES_IDENTICALLY_1D_IBP_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_susceptibility_density_identity_zero_2026_06_12.py
"""
import math
import sys

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
import sympy as sp


K_LEFT = -0.5 * math.pi
K_RIGHT = 0.5 * math.pi
T_HOP = 1.0

QUAD_TOL = 1.0e-12
QUAD_AGREE_TOL = 1.0e-10
ZERO_TOL = 5.0e-13
CONV_TOL = 1.0e-3
TAIL_N_MIN = 20

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name, condition, detail):
    global PASS_COUNT, FAIL_COUNT
    if bool(condition):
        PASS_COUNT += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL_COUNT += 1
        print(f"FAIL {name}: {detail}")


def fermi(E, mu_ch, temperature):
    x = np.asarray((E - mu_ch) / temperature, dtype=float)
    out = np.empty_like(x, dtype=float)
    nonnegative = x >= 0.0
    z = np.exp(-x[nonnegative])
    out[nonnegative] = z / (1.0 + z)
    z = np.exp(x[~nonnegative])
    out[~nonnegative] = 1.0 / (1.0 + z)
    if np.ndim(E) == 0:
        return float(out)
    return out


def fermi_prime(E, mu_ch, temperature):
    f = fermi(E, mu_ch, temperature)
    return -f * (1.0 - f) / temperature


def band_radius_and_derivatives(k, mass):
    c = np.cos(k)
    s = np.sin(k)
    r = np.sqrt(mass * mass + 4.0 * T_HOP * T_HOP * c * c)
    rp = -4.0 * T_HOP * T_HOP * s * c / r
    rpp = (
        -4.0 * T_HOP * T_HOP * np.cos(2.0 * k) / r
        - 16.0 * T_HOP**4 * s * s * c * c / (r * r * r)
    )
    return r, rp, rpp


def susceptibility_integrand(k, mass, mu_ch, temperature):
    r, rp, rpp = band_radius_and_derivatives(k, mass)
    total = np.zeros_like(np.asarray(k, dtype=float), dtype=float)
    for band_sign in (-1.0, 1.0):
        energy = band_sign * r
        energy_k = band_sign * rp
        energy_kk = band_sign * rpp
        total = total + fermi(energy, mu_ch, temperature) * energy_kk
        total = total + fermi_prime(energy, mu_ch, temperature) * energy_k * energy_k
    if np.ndim(k) == 0:
        return float(total)
    return total


def chi_inf_quad(mass, mu_ch, temperature):
    value, error = quad(
        lambda kk: susceptibility_integrand(kk, mass, mu_ch, temperature),
        K_LEFT,
        K_RIGHT,
        epsabs=QUAD_TOL,
        epsrel=QUAD_TOL,
        limit=300,
    )
    return value / (2.0 * math.pi), error / (2.0 * math.pi)


def chi_inf_gauss(mass, mu_ch, temperature, order=800):
    nodes, weights = leggauss(order)
    midpoint = 0.5 * (K_LEFT + K_RIGHT)
    half_width = 0.5 * (K_RIGHT - K_LEFT)
    ks = midpoint + half_width * nodes
    values = susceptibility_integrand(ks, mass, mu_ch, temperature)
    return half_width * float(np.dot(weights, values)) / (2.0 * math.pi)


def chi_finite_N(site_count, mass, mu_ch, temperature):
    if site_count % 2:
        raise ValueError("site_count must be even for the staggered two-site cell")
    cell_count = site_count // 2
    spacing = 2.0 * math.pi / site_count
    ks = K_LEFT + spacing * np.arange(cell_count, dtype=float)
    values = susceptibility_integrand(ks, mass, mu_ch, temperature)
    return float(np.sum(values) / site_count)


def sign_label(value):
    if value > ZERO_TOL:
        return "POS"
    if value < -ZERO_TOL:
        return "NEG"
    return "ZERO"


def decreasing(values):
    return all(values[i] > values[i + 1] for i in range(len(values) - 1))


def fmt(value):
    return f"{value:+.16e}"


def run_y2_symbolic_ibp_identity():
    print("Y2 symbolic integration-by-parts identity")
    k = sp.symbols("k", real=True)
    energy = sp.Function("E")(k)
    occupation = sp.Function("f")
    total_derivative = sp.diff(occupation(energy) * sp.diff(energy, k), k)
    integrand = occupation(energy) * sp.diff(energy, k, 2)
    integrand += sp.diff(occupation(energy), k) * sp.diff(energy, k)
    residual = sp.simplify(total_derivative - integrand)
    check(
        "Y2 symbolic total-derivative residual vanishes",
        residual == 0,
        f"residual={residual}",
    )


def run_y2a():
    print("Y2a finite-N convergence")
    mass = 0.4
    temperature = 0.3
    site_counts = list(range(8, 42, 2))
    for mu_ch in (0.0, 0.5, 1.0):
        chi_limit, quad_error = chi_inf_quad(mass, mu_ch, temperature)
        print(
            f"Y2a mu_ch={mu_ch:.2f} m={mass:.2f} T={temperature:.2f} "
            f"chi_inf={fmt(chi_limit)} quad_err={quad_error:.3e}"
        )
        rows = []
        for site_count in site_counts:
            chi_n = chi_finite_N(site_count, mass, mu_ch, temperature)
            error = abs(chi_n - chi_limit)
            rows.append((site_count, chi_n, error))
            print(
                f"  N={site_count:2d} chi_N={fmt(chi_n)} "
                f"abs_err={error:.16e}"
            )

        endpoint_error = rows[-1][2]
        check(
            f"Y2a mu={mu_ch:.2f} N=40 endpoint below 1e-3",
            endpoint_error < CONV_TOL,
            f"abs_err(N=40)={endpoint_error:.3e}, chi_inf={fmt(chi_limit)}",
        )

        for cell_parity in (0, 1):
            label = "N/2 even" if cell_parity == 0 else "N/2 odd"
            subsequence = [
                row
                for row in rows
                if row[0] >= TAIL_N_MIN and (row[0] // 2) % 2 == cell_parity
            ]
            errors = [row[2] for row in subsequence]
            ns = [row[0] for row in subsequence]
            check(
                f"Y2a mu={mu_ch:.2f} {label} tail error decreasing",
                decreasing(errors),
                f"N={ns}, abs_err={[f'{err:.3e}' for err in errors]}",
            )
            check(
                f"Y2a mu={mu_ch:.2f} {label} endpoint below 1e-3",
                errors[-1] < CONV_TOL,
                f"N={ns[-1]}, abs_err={errors[-1]:.3e}",
            )


def run_y2b_y2c():
    print("Y2b sign table of the density-limit object")
    mu_values = (0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5)
    mass_values = (0.2, 0.4, 1.0)
    temperature_values = (0.15, 0.3, 0.6)
    table = []
    particle_hole_values = []

    for mass in mass_values:
        for temperature in temperature_values:
            print(f"Y2b row m={mass:.2f} T={temperature:.2f}")
            for mu_ch in mu_values:
                chi_limit, quad_error = chi_inf_quad(mass, mu_ch, temperature)
                label = sign_label(chi_limit)
                table.append((mass, temperature, mu_ch, chi_limit, label))
                if mu_ch == 0.0:
                    particle_hole_values.append((mass, temperature, chi_limit, label))
                print(
                    f"  mu_ch={mu_ch:.2f} chi_inf={fmt(chi_limit)} "
                    f"sign={label} quad_err={quad_error:.3e}"
                )

    max_abs = max(abs(row[3]) for row in table)
    observed_labels = sorted({row[4] for row in table})
    check(
        "Y2b full table uniformly ZERO to stated precision",
        max_abs < ZERO_TOL,
        f"max_abs={max_abs:.3e}, tol={ZERO_TOL:.1e}, observed_labels={observed_labels}",
    )
    check(
        "Y2b no positive density-limit entries above tolerance",
        not any(row[3] > ZERO_TOL for row in table),
        f"largest={max(row[3] for row in table):.3e}, tol={ZERO_TOL:.1e}",
    )
    check(
        "Y2b no negative density-limit entries below tolerance",
        not any(row[3] < -ZERO_TOL for row in table),
        f"smallest={min(row[3] for row in table):.3e}, tol={ZERO_TOL:.1e}",
    )

    print("Y2c particle-hole point mu_ch=0")
    for mass, temperature, chi_limit, label in particle_hole_values:
        print(
            f"  m={mass:.2f} T={temperature:.2f} "
            f"chi_inf(mu=0)={fmt(chi_limit)} sign={label}"
        )
    ph_max_abs = max(abs(row[2]) for row in particle_hole_values)
    check(
        "Y2c particle-hole envelope limit is ZERO to stated precision",
        ph_max_abs < ZERO_TOL,
        f"max_abs_mu0={ph_max_abs:.3e}, tol={ZERO_TOL:.1e}",
    )


def run_y2d():
    print("Y2d independent quadrature validation")
    instances = (
        (0.4, 0.0, 0.3),
        (0.2, 1.25, 0.15),
        (1.0, 0.75, 0.6),
    )
    for mass, mu_ch, temperature in instances:
        chi_quad, quad_error = chi_inf_quad(mass, mu_ch, temperature)
        chi_gauss = chi_inf_gauss(mass, mu_ch, temperature)
        diff = abs(chi_quad - chi_gauss)
        print(
            f"  m={mass:.2f} mu_ch={mu_ch:.2f} T={temperature:.2f} "
            f"quad={fmt(chi_quad)} gauss={fmt(chi_gauss)} "
            f"diff={diff:.3e} quad_err={quad_error:.3e}"
        )
        check(
            f"Y2d quad-vs-gauss agreement m={mass:.2f} mu={mu_ch:.2f} T={temperature:.2f}",
            diff < QUAD_AGREE_TOL,
            f"diff={diff:.3e}, tol={QUAD_AGREE_TOL:.1e}",
        )


def main():
    print("Y2 susceptibility density runner")
    print(
        "Bands E_pm(k)=pm sqrt(m^2 + 4 cos^2(k)); "
        "k in [-pi/2, pi/2]; chi_inf=(1/2pi) integral sum_pm."
    )
    run_y2_symbolic_ibp_identity()
    run_y2a()
    run_y2b_y2c()
    run_y2d()
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        sys.exit(1)


if __name__ == "__main__":
    main()
