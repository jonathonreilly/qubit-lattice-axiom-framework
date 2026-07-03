#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/LP_IDENTIFICATION_FAILS_OFF_M0_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_lp_identification_fails_off_m0_2026_06_12.py
"""
import sys
from dataclasses import dataclass

import numpy as np
from numpy.polynomial.legendre import leggauss


T_HOP = 1.0
MASSES = (0.2, 0.5)
TEMPERATURES = (0.2, 0.4)

Q_HARPER = 24
LX = Q_HARPER
LY = 2
N_SITE = LX * LY
B_FIELD = 2.0 * np.pi / Q_HARPER

GL_LOW = 160
GL_HIGH = 224
GL_ORDERS = (GL_LOW, GL_HIGH)
BISECTION_STEPS = 80
FULL_BRACKET = (0.0, 4.0)
LP_BRACKET = (0.0, 4.0)

FULL_GL_DOUBLING_ABS = 1.0e-6
LP_GL_DOUBLING_ABS = 1.0e-6
HARPER_ANCHOR_MU = 1.7086
HARPER_ANCHOR_TOL = 5.0e-3
IDENTIFICATION_ABS = 2.0e-2

M0_LIMIT_MASS = 1.0e-8
M0_KERNEL_TOL = 1.0e-10
RANDOM_SEED = 20260612

FAR_BELOW_MU = -20.0
FAR_BELOW_FULL_ABS = 1.0e-12
FAR_BELOW_LP_ABS = 1.0e-12

WRAP_PHASE_TOL = 1.0e-12
HERMITICITY_TOL = 1.0e-12
SPECTRAL_WRAP_TOL = 1.0e-10
B0_FOLDING_TOL = 1.0e-10

MEASURED_DEVIATION_TABLE_TOL = 5.0e-4
MEASURED_DEVIATIONS = {
    (0.2, 0.2): 0.0424013805,
    (0.2, 0.4): 0.0461600062,
    (0.5, 0.2): 0.2010378416,
    (0.5, 0.4): 0.1994054030,
}

SITE_SIGNS = np.array(
    [1.0 if (x + y) % 2 == 0 else -1.0 for x in range(LX) for y in range(LY)]
)


@dataclass(frozen=True)
class SpectrumTable:
    eigvals: np.ndarray
    weights_per_site: np.ndarray


@dataclass(frozen=True)
class ZeroBandTable:
    radius: np.ndarray
    weights: np.ndarray


@dataclass(frozen=True)
class LPTable:
    radius: np.ndarray
    det_hessian: np.ndarray
    weights: np.ndarray


class Checks:
    def __init__(self):
        self.pass_count = 0
        self.fail_count = 0

    def check(self, condition, label, detail):
        if bool(condition):
            self.pass_count += 1
            print(f"PASS: {label} :: {detail}")
        else:
            self.fail_count += 1
            print(f"FAIL: {label} :: {detail}")

    def finish(self):
        print(f"TOTAL: PASS={self.pass_count} FAIL={self.fail_count}")
        if self.fail_count:
            sys.exit(1)


def site_index(x, y):
    return x * LY + y


def gl_average_nodes_weights(n):
    x, w = leggauss(n)
    return np.pi * x, 0.5 * w


def harper_matrix(kx, ky, b_field, mass):
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


def harper_spectrum_table(mass, n):
    nodes, weights = gl_average_nodes_weights(n)
    eigvals = np.empty((n * n, N_SITE), dtype=np.float64)
    weights_per_site = np.empty(n * n, dtype=np.float64)

    row = 0
    for ix, kx in enumerate(nodes):
        wx = weights[ix]
        for iy, ky in enumerate(nodes):
            wy = weights[iy]
            eigvals[row] = np.linalg.eigvalsh(harper_matrix(kx, ky, B_FIELD, mass))
            weights_per_site[row] = wx * wy / N_SITE
            row += 1

    return SpectrumTable(eigvals=eigvals, weights_per_site=weights_per_site)


def zero_band_table(mass, n):
    nodes, weights = gl_average_nodes_weights(n)
    kx, ky = np.meshgrid(nodes, nodes, indexing="ij")
    wxwy = np.outer(weights, weights)
    eps = -2.0 * T_HOP * (np.cos(kx) + np.cos(ky))
    radius = np.sqrt(mass * mass + eps * eps)
    return ZeroBandTable(radius=radius, weights=wxwy)


def grand_kernel(energy, mu, temp):
    return -temp * np.logaddexp(0.0, -(energy - mu) / temp)


def harper_omega(table, mu, temp):
    return np.sum(table.weights_per_site[:, None] * grand_kernel(table.eigvals, mu, temp))


def zero_omega(table, mu, temp):
    return 0.5 * np.sum(
        table.weights
        * (grand_kernel(table.radius, mu, temp) + grand_kernel(-table.radius, mu, temp))
    )


def finite_field_delta(mu, temp, spectrum, zero_table):
    return harper_omega(spectrum, mu, temp) - zero_omega(zero_table, mu, temp)


def fermi_prime(energy_minus_mu, temp):
    z = np.clip(energy_minus_mu / (2.0 * temp), -60.0, 60.0)
    sech2 = 1.0 / (np.cosh(z) * np.cosh(z))
    return -0.25 * sech2 / temp


def det_hessian_staggered(kx, ky, mass):
    cx = np.cos(kx)
    cy = np.cos(ky)
    sx = np.sin(kx)
    sy = np.sin(ky)
    eps = -2.0 * T_HOP * (cx + cy)
    radius = np.sqrt(mass * mass + eps * eps)

    det_eps_hessian = 4.0 * T_HOP * T_HOP * cx * cy
    adj_contract = 8.0 * T_HOP**3 * (sx * sx * cy + sy * sy * cx)

    # E_s = s sqrt(m^2 + eps^2).  With g'=s eps/R and g''=s m^2/R^3,
    # det(g'' grad eps grad eps^T + g' Hess eps)
    # = (g')^2 det(Hess eps) + g'g'' grad eps^T adj(Hess eps) grad eps.
    return (
        (eps * eps / (radius * radius)) * det_eps_hessian
        + (eps * mass * mass / (radius**4)) * adj_contract
    )


def lp_table(mass, n):
    nodes, weights = gl_average_nodes_weights(n)
    kx, ky = np.meshgrid(nodes, nodes, indexing="ij")
    wxwy = np.outer(weights, weights)
    eps = -2.0 * T_HOP * (np.cos(kx) + np.cos(ky))
    radius = np.sqrt(mass * mass + eps * eps)
    det_hess = det_hessian_staggered(kx, ky, mass)
    return LPTable(radius=radius, det_hessian=det_hess, weights=wxwy)


def lp_value(mu, temp, table):
    kernel = fermi_prime(table.radius - mu, temp) + fermi_prime(-table.radius - mu, temp)
    return np.sum(table.weights * kernel * table.det_hessian)


def bisection_root(value_fn, bracket):
    lo, hi = bracket
    flo = value_fn(lo)
    fhi = value_fn(hi)
    start_flo = flo
    start_fhi = fhi
    if (not np.isfinite(flo)) or (not np.isfinite(fhi)) or flo * fhi > 0.0:
        return np.nan, np.nan, start_flo, start_fhi

    for _ in range(BISECTION_STEPS):
        mid = 0.5 * (lo + hi)
        fmid = value_fn(mid)
        if flo * fmid <= 0.0:
            hi = mid
            fhi = fmid
        else:
            lo = mid
            flo = fmid

    root = 0.5 * (lo + hi)
    return root, value_fn(root), start_flo, start_fhi


def folded_zero_spectrum(kx, ky, mass):
    vals = []
    py = ky / LY
    for nx in range(Q_HARPER):
        px = (kx + 2.0 * np.pi * nx) / Q_HARPER
        eps = -2.0 * T_HOP * (np.cos(px) + np.cos(py))
        radius = np.sqrt(mass * mass + eps * eps)
        vals.extend((-radius, radius))
    return np.sort(np.array(vals, dtype=np.float64))


def wraparound_and_size_probes():
    probe_mass = 0.2
    kx = 0.37
    ky = -0.91
    h = harper_matrix(kx, ky, B_FIELD, probe_mass)
    hermiticity = np.max(np.abs(h - h.conjugate().T))

    eig = np.linalg.eigvalsh(h)
    eig_kx_wrap = np.linalg.eigvalsh(harper_matrix(kx + 2.0 * np.pi, ky, B_FIELD, probe_mass))
    eig_ky_wrap = np.linalg.eigvalsh(harper_matrix(kx, ky + 2.0 * np.pi, B_FIELD, probe_mass))
    spectral_kx = np.max(np.abs(np.sort(eig) - np.sort(eig_kx_wrap)))
    spectral_ky = np.max(np.abs(np.sort(eig) - np.sort(eig_ky_wrap)))

    phase_period = max(
        abs(np.exp(1j * B_FIELD * (x + Q_HARPER)) - np.exp(1j * B_FIELD * x))
        for x in range(Q_HARPER)
    )

    h0 = harper_matrix(kx, ky, 0.0, probe_mass)
    folded = folded_zero_spectrum(kx, ky, probe_mass)
    b0_folding = np.max(np.abs(np.sort(np.linalg.eigvalsh(h0)) - folded))

    return {
        "cell_contains_staggered_period": (Q_HARPER % 2 == 0) and (LY == 2),
        "hermiticity": hermiticity,
        "spectral_kx": spectral_kx,
        "spectral_ky": spectral_ky,
        "phase_period": phase_period,
        "b0_folding": b0_folding,
    }


def kernel_m0_limit_error():
    rng = np.random.default_rng(RANDOM_SEED)
    points = rng.uniform(-np.pi, np.pi, size=(3, 2))
    errors = []
    for kx, ky in points:
        massive = det_hessian_staggered(kx, ky, M0_LIMIT_MASS)
        massless = 4.0 * T_HOP * T_HOP * np.cos(kx) * np.cos(ky)
        errors.append(abs(massive - massless))
    return max(errors)


def compute_results():
    spectra = {}
    zero_tables = {}
    lp_tables = {}
    results = []

    for mass in MASSES:
        for n in GL_ORDERS:
            spectra[(mass, n)] = harper_spectrum_table(mass, n)
            zero_tables[(mass, n)] = zero_band_table(mass, n)
            lp_tables[(mass, n)] = lp_table(mass, n)

        for temp in TEMPERATURES:
            full_roots = {}
            lp_roots = {}
            full_brackets = {}
            lp_brackets = {}
            full_residuals = {}
            lp_residuals = {}

            for n in GL_ORDERS:
                full_fn = lambda mu, m=mass, tt=temp, nn=n: finite_field_delta(
                    mu, tt, spectra[(m, nn)], zero_tables[(m, nn)]
                )
                root, residual, flo, fhi = bisection_root(full_fn, FULL_BRACKET)
                full_roots[n] = root
                full_residuals[n] = residual
                full_brackets[n] = (flo, fhi)

                lp_fn = lambda mu, tt=temp, nn=n: lp_value(mu, tt, lp_tables[(mass, nn)])
                root, residual, flo, fhi = bisection_root(lp_fn, LP_BRACKET)
                lp_roots[n] = root
                lp_residuals[n] = residual
                lp_brackets[n] = (flo, fhi)

            full_high_fn = lambda mu, m=mass, tt=temp: finite_field_delta(
                mu, tt, spectra[(m, GL_HIGH)], zero_tables[(m, GL_HIGH)]
            )
            lp_high_fn = lambda mu, tt=temp: lp_value(mu, tt, lp_tables[(mass, GL_HIGH)])

            deviation = abs(lp_roots[GL_HIGH] - full_roots[GL_HIGH])
            results.append(
                {
                    "mass": mass,
                    "temp": temp,
                    "full_roots": full_roots,
                    "lp_roots": lp_roots,
                    "full_brackets": full_brackets,
                    "lp_brackets": lp_brackets,
                    "full_residuals": full_residuals,
                    "lp_residuals": lp_residuals,
                    "deviation": deviation,
                    "within_identification": deviation <= IDENTIFICATION_ABS,
                    "full_far_below": abs(full_high_fn(FAR_BELOW_MU)),
                    "lp_far_below": abs(lp_high_fn(FAR_BELOW_MU)),
                }
            )

    return results


def print_results(results):
    print("# S3 staggered d=2 LP-vs-Harper boundary check")
    print(f"SCOPE: Harper q={Q_HARPER}, finite B=2*pi/{Q_HARPER}; LP is the B->0 candidate.")
    print(
        "MOTIVATION ONLY: with the in-review collapse relation, the LP formula is an analytic "
        "candidate for the boundary surface; finite-B deviations below are diagnostic."
    )
    print(
        "m      T      mu_full_224    mu_LP_224      abs_dev       comparison_gate"
    )
    for row in results:
        gate = "within_2e-2" if row["within_identification"] else "measured_deviation"
        print(
            f"{row['mass']:<6.3g} {row['temp']:<6.3g} "
            f"{row['full_roots'][GL_HIGH]:<14.10f} "
            f"{row['lp_roots'][GL_HIGH]:<14.10f} "
            f"{row['deviation']:<13.10f} {gate}"
        )


def main():
    probes = wraparound_and_size_probes()
    m0_error = kernel_m0_limit_error()
    results = compute_results()
    print_results(results)

    checks = Checks()
    checks.check(
        probes["cell_contains_staggered_period"],
        "finite cell contains staggered period",
        f"Q={Q_HARPER}, Ly={LY}",
    )
    checks.check(
        probes["phase_period"] <= WRAP_PHASE_TOL,
        "magnetic wraparound phase periodicity",
        f"max phase error={probes['phase_period']:.3e}, tol={WRAP_PHASE_TOL:.1e}",
    )
    checks.check(
        probes["hermiticity"] <= HERMITICITY_TOL,
        "Harper matrix Hermiticity",
        f"max |H-H^dag|={probes['hermiticity']:.3e}, tol={HERMITICITY_TOL:.1e}",
    )
    checks.check(
        probes["spectral_kx"] <= SPECTRAL_WRAP_TOL,
        "kx spectral wraparound",
        f"max eig drift={probes['spectral_kx']:.3e}, tol={SPECTRAL_WRAP_TOL:.1e}",
    )
    checks.check(
        probes["spectral_ky"] <= SPECTRAL_WRAP_TOL,
        "ky spectral wraparound",
        f"max eig drift={probes['spectral_ky']:.3e}, tol={SPECTRAL_WRAP_TOL:.1e}",
    )
    checks.check(
        probes["b0_folding"] <= B0_FOLDING_TOL,
        "B=0 Harper folding anti-fabrication anchor",
        f"max folded-spectrum error={probes['b0_folding']:.3e}, tol={B0_FOLDING_TOL:.1e}",
    )
    checks.check(
        m0_error <= M0_KERNEL_TOL,
        "m->0 LP kernel reduction",
        f"max error at 3 seeded random k points={m0_error:.3e}, tol={M0_KERNEL_TOL:.1e}",
    )

    for row in results:
        mass = row["mass"]
        temp = row["temp"]
        key = (mass, temp)

        for n in GL_ORDERS:
            flo, fhi = row["full_brackets"][n]
            checks.check(
                flo < 0.0 and fhi > 0.0,
                f"full Harper bisection bracket m={mass} T={temp} GL={n}",
                f"f({FULL_BRACKET[0]})={flo:.3e}, f({FULL_BRACKET[1]})={fhi:.3e}",
            )

            flo, fhi = row["lp_brackets"][n]
            checks.check(
                flo > 0.0 and fhi < 0.0,
                f"LP bisection bracket m={mass} T={temp} GL={n}",
                f"f({LP_BRACKET[0]})={flo:.3e}, f({LP_BRACKET[1]})={fhi:.3e}",
            )

        full_double = abs(row["full_roots"][GL_HIGH] - row["full_roots"][GL_LOW])
        checks.check(
            full_double <= FULL_GL_DOUBLING_ABS,
            f"full Harper GL {GL_LOW}/{GL_HIGH} doubling m={mass} T={temp}",
            f"|delta mu|={full_double:.3e}, tol={FULL_GL_DOUBLING_ABS:.1e}",
        )

        lp_double = abs(row["lp_roots"][GL_HIGH] - row["lp_roots"][GL_LOW])
        checks.check(
            lp_double <= LP_GL_DOUBLING_ABS,
            f"LP GL {GL_LOW}/{GL_HIGH} doubling m={mass} T={temp}",
            f"|delta mu|={lp_double:.3e}, tol={LP_GL_DOUBLING_ABS:.1e}",
        )

        checks.check(
            row["full_far_below"] <= FAR_BELOW_FULL_ABS,
            f"full Harper far-below-band control m={mass} T={temp}",
            f"|delta Omega(mu={FAR_BELOW_MU})|={row['full_far_below']:.3e}, tol={FAR_BELOW_FULL_ABS:.1e}",
        )

        checks.check(
            row["lp_far_below"] <= FAR_BELOW_LP_ABS,
            f"LP far-below-band control m={mass} T={temp}",
            f"|LP(mu={FAR_BELOW_MU})|={row['lp_far_below']:.3e}, tol={FAR_BELOW_LP_ABS:.1e}",
        )

        expected_dev = MEASURED_DEVIATIONS[key]
        checks.check(
            abs(row["deviation"] - expected_dev) <= MEASURED_DEVIATION_TABLE_TOL,
            f"measured deviation table m={mass} T={temp}",
            f"dev={row['deviation']:.10f}, expected={expected_dev:.10f}, tol={MEASURED_DEVIATION_TABLE_TOL:.1e}",
        )

    anchor_row = next(row for row in results if row["mass"] == 0.2 and row["temp"] == 0.2)
    anchor_mu = anchor_row["full_roots"][GL_HIGH]
    checks.check(
        abs(anchor_mu - HARPER_ANCHOR_MU) <= HARPER_ANCHOR_TOL,
        "Harper finite-field anchor mu*(0.2,0.2)",
        f"mu={anchor_mu:.10f}, anchor={HARPER_ANCHOR_MU:.4f}, tol={HARPER_ANCHOR_TOL:.1e}",
    )

    checks.finish()


if __name__ == "__main__":
    main()
