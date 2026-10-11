"""Independent numerical checks for the RZ referee report.

This script only reads the worker's saved Monte Carlo arrays.  It uses a
separate implementation of the covariance integration and of the physical
translation, so that rerunning the worker's scripts is not the sole check.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
Z2 = ROOT.parent / "Z2"


def late_correlation(path: Path, carrier: float, lag_max: float):
    data = np.load(path)
    phi = data["phi"]
    time = data["tobs"]
    carriers = list(data["W0"])
    terminal_time = float(data["T"])
    index = carriers.index(carrier)
    values = phi[:, :, index]
    if carrier == 0:
        values = values.real
    mean = values.mean(axis=0)
    residual = values - mean
    variance = np.mean(np.abs(residual) ** 2, axis=0)
    late = np.flatnonzero(time >= max(float(data["d"]) + 1.5, terminal_time - 4.0))
    step = float(time[1] - time[0])
    count = int(round(lag_max / step))
    corr = np.empty(count + 1, dtype=complex)
    for lag in range(count + 1):
        usable = late[late + lag < len(time)]
        products = np.mean(
            residual[:, usable] * np.conj(residual[:, usable + lag]), axis=0
        )
        corr[lag] = np.mean(products / np.sqrt(variance[usable] * variance[usable + lag]))
    lags = step * np.arange(count + 1)
    spectral = 2 * np.real(np.trapezoid(corr * np.exp(1j * carrier * lags), lags))
    return spectral, corr, lags


def variance_fits(path: Path, carrier: float = 0.0):
    data = np.load(path)
    phi = data["phi"]
    time = data["tobs"]
    index = list(data["W0"]).index(carrier)
    values = phi[:, :, index]
    if carrier == 0:
        values = values.real
    residual = values - values.mean(axis=0)
    variance = np.mean(np.abs(residual) ** 2, axis=0)
    proper_time = np.sqrt(np.maximum(time**2 - float(data["d"]) ** 2, 1e-15))
    late = time >= max(float(data["d"]) + 1.5, float(data["T"]) - 4.0)
    y = np.log(variance[late])
    tau = proper_time[late]
    fixed = {}
    for power in (0.0, -1.5):
        matrix = np.column_stack([np.ones(len(tau)), tau])
        intercept, rate = np.linalg.lstsq(matrix, y - power * np.log(tau), rcond=None)[0]
        residual_sum = np.sum((y - (intercept + power * np.log(tau) + rate * tau)) ** 2)
        fixed[power] = (rate, intercept, residual_sum)
    free_matrix = np.column_stack([np.ones(len(tau)), np.log(tau), tau])
    intercept, power, rate = np.linalg.lstsq(free_matrix, y, rcond=None)[0]
    free_residual = np.sum((y - free_matrix @ np.array([intercept, power, rate])) ** 2)
    condition = np.linalg.cond(free_matrix)
    return fixed, (rate, intercept, power, free_residual, condition), (tau[0], tau[-1])


def physical_check():
    planck = 1.616255e-35
    lattice = 7.9e-20
    light = 2.99792458e8
    gpc = 3.0857e25
    sqrt_epsilon = (planck / lattice) ** 2
    c_low = 0.628
    c2 = 0.692180
    kh = 2.7348
    halfwidth = 0.5 * (2 * math.pi * light / 507e-9 - 2 * math.pi * light / 595e-9)
    dimensionless_halfwidth = halfwidth * lattice / light
    analytic_complex = sqrt_epsilon * dimensionless_halfwidth / (
        4 * math.pi**2 * c2**2 * kh
    )
    z2_real = 2 * analytic_complex
    duration = 1.0
    tau = math.sqrt(2 * gpc * light * duration + (light * duration) ** 2)
    boost_gamma = (gpc + light * duration) / tau
    rapidity = math.acosh(boost_gamma)
    boost = rapidity / math.sinh(rapidity)
    exponent = c_low * sqrt_epsilon * tau / lattice
    time_penalty = 1.5 * math.log(tau / lattice)
    radio_halfwidth = 2 * math.pi * 50e6 / light
    vlbi_halfwidth = 2 * math.pi * 500 / light
    spectral_length = math.pi * (1 / (2 * math.pi * c2)) ** 2 * sqrt_epsilon * lattice / kh
    radio_fraction = 2 * radio_halfwidth * spectral_length / math.pi * boost
    vlbi_fraction = 2 * vlbi_halfwidth * spectral_length / math.pi * boost
    return {
        "sqrt_epsilon": sqrt_epsilon,
        "tau_1s_1gpc": tau,
        "rate_exponent": exponent,
        "complex_growth_frame_fraction": analytic_complex,
        "real_growth_frame_fraction": z2_real,
        "boost_gamma": boost_gamma,
        "rapidity": rapidity,
        "boost_factor": boost,
        "real_observer_fraction": z2_real * boost,
        "observer_band_penalty": -math.log(z2_real * boost),
        "lclt_time_penalty": time_penalty,
        "budget_B1000_optical": exponent - time_penalty + math.log(z2_real * boost) - 1000,
        "budget_B1000_radio100MHz": exponent - time_penalty + math.log(radio_fraction) - 1000,
        "budget_B1000_vlbi1kHz": exponent - time_penalty + math.log(vlbi_fraction) - 1000,
    }


def gw_side_check(lattice: float):
    planck = 1.616255e-35
    light = 2.99792458e8
    gpc = 3.0857e25
    c_low = 0.628
    c2 = 0.692180
    kh = 2.7348
    sqrt_epsilon = (planck / lattice) ** 2
    source_extent = 1e4
    tau = math.sqrt(2 * gpc * source_extent + source_extent**2)
    boost_gamma = (gpc + source_extent) / tau
    rapidity = math.acosh(boost_gamma)
    boost = rapidity / math.sinh(rapidity)
    dimensionless_halfwidth = 2 * math.pi * 490 * lattice / light
    real_fraction = (
        sqrt_epsilon
        * dimensionless_halfwidth
        / (2 * math.pi**2 * c2**2 * kh)
        * boost
    )
    return {
        "c_low_exponent": c_low * sqrt_epsilon * tau / lattice,
        "band_penalty": -math.log(real_fraction),
        "c_low_net": c_low * sqrt_epsilon * tau / lattice + math.log(real_fraction),
        "node_net": kh * sqrt_epsilon * tau / lattice + math.log(real_fraction),
    }


def main():
    files = [
        Z2 / "z2_A_e1.npz",
        Z2 / "z2_A_e05.npz",
        Z2 / "z2_A_e025.npz",
        Z2 / "z2_A_e0125.npz",
    ]
    print("Independent covariance-integral check (S(omega0)/V):")
    for path in files:
        epsilon = float(np.load(path)["eps"])
        rows = []
        for carrier in (0.0, 1.0, 4.0):
            values = []
            for cutoff in (0.5, 1.0, 1.5, 2.0):
                spectral, _, _ = late_correlation(path, carrier, cutoff)
                values.append(spectral)
            rows.append((carrier, values))
        print(f"  eps={epsilon:g}: " + "; ".join(
            f"w0={carrier:g} " + "/".join(f"{value:.3f}" for value in values)
            for carrier, values in rows
        ))

    print("\nVariance fits (rate, lnA, RSS; free fit also gives p and condition number):")
    for path in files:
        epsilon = float(np.load(path)["eps"])
        fixed, free, window = variance_fits(path)
        print(
            f"  eps={epsilon:g}, tau={window[0]:.2f}..{window[1]:.2f}: "
            f"p=0 {fixed[0.0][0]:.3f},{fixed[0.0][1]:.2f},{fixed[0.0][2]:.3g}; "
            f"p=-1.5 {fixed[-1.5][0]:.3f},{fixed[-1.5][1]:.2f},{fixed[-1.5][2]:.3g}; "
            f"free gamma={free[0]:.3f},lnA={free[1]:.2f},p={free[2]:.2f},"
            f"RSS={free[3]:.3g},cond={free[4]:.2g}"
        )

    print("\nPhysical convention check:")
    for key, value in physical_check().items():
        print(f"  {key} = {value:.12g}")

    print("\nGW side check:")
    for lattice in (1e-19, 7.9e-20):
        values = gw_side_check(lattice)
        print(f"  l_k={lattice:.2g}: " + ", ".join(
            f"{key}={value:.6f}" for key, value in values.items()
        ))


if __name__ == "__main__":
    main()
