#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/D2_SIGN_BOUNDARY_TRACKS_LANDAU_PEIERLS_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_lp_boundary_identification_2026_06_12.py
"""
import math
import sys
from dataclasses import dataclass

import numpy as np


T_HOP = 1.0
Q = 24
FLUX_B = 2.0 * math.pi / Q
FIELD_B = FLUX_B

TEMPERATURES = (0.2, 0.3, 0.4)

FULL_GL_LOW = 160
FULL_GL_HIGH = 224
FULL_GL_DOUBLING_TOL = 1.0e-6

LP_GL_LOW = 128
LP_GL_HIGH = 256
LP_GL_DOUBLING_TOL = 1.0e-6

ROOT_WIDTH = 2.0e-3
COMPARISON_TOL = 2.0e-2

ANCHOR_TOL = 1.0e-12
GAUGE_TOL = 1.0e-11
WRAP_TOL = 1.0e-12
ANTI_FAB_MIN_ABS_CHI = 1.0e-7
T50_FULL_TOL = 1.0e-4
T50_LP_TOL = 1.0e-4
LP_FAR_TOL = 1.0e-12
FPRIME_TOL = 1.0e-14

FULL_ROOT_BRACKETS = {
    0.2: (-3.2, -0.2),
    0.3: (-3.2, -0.2),
    0.4: (-3.2, -0.2),
}

LP_ROOT_BRACKETS = {
    0.2: (-3.2, -0.2),
    0.3: (-3.2, -0.2),
    0.4: (-3.2, -0.2),
}

ANCHOR_K_POINTS = (
    (-1.25, -0.75),
    (-0.10, 0.30),
    (0.80, 1.70),
    (2.10, -2.40),
)

GAUGE_PROBE_KX = 0.137 / Q
GAUGE_PROBE_KY = -0.421
ANTI_FAB_MU = 0.0
ANTI_FAB_T = 0.3
T50_MU = 0.0
FAR_BELOW_MU = -20.0
FPRIME_PROBE_T = 0.3


PASS_COUNT = 0
FAIL_COUNT = 0


def check(label, condition):
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
        print(f"PASS: {label}")
    else:
        FAIL_COUNT += 1
        print(f"FAIL: {label}")
    return ok


def finish():
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        sys.exit(1)


@dataclass
class WeightedSpectrum:
    energies: np.ndarray
    weights: np.ndarray


@dataclass
class RootResult:
    root: float
    initial_lo: float
    initial_hi: float
    final_lo: float
    final_hi: float
    initial_flo: float
    initial_fhi: float
    final_flo: float
    final_fhi: float
    steps: int


def normalized_legendre(n):
    nodes, weights = np.polynomial.legendre.leggauss(n)
    return nodes, 0.5 * weights


def square_band(kx, ky):
    return -2.0 * T_HOP * (np.cos(kx) + np.cos(ky))


def fermi_prime(x, temp):
    y = np.abs(np.asarray(x, dtype=np.float64)) / (2.0 * temp)
    e = np.exp(-2.0 * y)
    sech2 = 4.0 * e / ((1.0 + e) * (1.0 + e))
    return -0.25 * sech2 / temp


def grand_potential_from_spectrum(spec, mu, temp):
    z = (mu - spec.energies) / temp
    return -temp * np.sum(spec.weights * np.logaddexp(0.0, z))


def zero_field_spectrum(gl_n):
    x, wx = normalized_legendre(gl_n)
    y, wy = normalized_legendre(gl_n)
    kx = math.pi * x
    ky = math.pi * y
    energies = square_band(kx[:, None], ky[None, :]).ravel()
    weights = (wx[:, None] * wy[None, :]).ravel()
    return WeightedSpectrum(energies=energies, weights=weights)


def hofstadter_stack(kx, ky_values, gauge):
    ky_values = np.asarray(ky_values, dtype=np.float64)
    count = ky_values.size
    h = np.zeros((count, Q, Q), dtype=np.complex128)
    sites = np.arange(Q)
    diag = -2.0 * T_HOP * np.cos(ky_values[:, None] + FLUX_B * sites[None, :])
    h[:, sites, sites] = diag

    if gauge == "boundary":
        for r in range(Q - 1):
            h[:, r, r + 1] = -T_HOP
            h[:, r + 1, r] = -T_HOP
        phase = np.exp(1j * Q * kx)
        h[:, Q - 1, 0] = -T_HOP * phase
        h[:, 0, Q - 1] = -T_HOP * np.conj(phase)
        return h

    if gauge == "uniform":
        phase = np.exp(1j * kx)
        for r in range(Q):
            rp = (r + 1) % Q
            h[:, r, rp] = -T_HOP * phase
            h[:, rp, r] = -T_HOP * np.conj(phase)
        return h

    raise ValueError(f"unknown gauge {gauge!r}")


def finite_field_spectrum(gl_n):
    x, wx = normalized_legendre(gl_n)
    y, wy = normalized_legendre(gl_n)
    kx_values = (math.pi / Q) * x
    ky_values = math.pi * y

    total = gl_n * gl_n * Q
    energies = np.empty(total, dtype=np.float64)
    weights = np.empty(total, dtype=np.float64)
    repeated_wy = np.repeat(wy, Q)

    offset = 0
    for kx, wx_i in zip(kx_values, wx):
        vals = np.linalg.eigvalsh(hofstadter_stack(kx, ky_values, "boundary"))
        block = vals.size
        energies[offset : offset + block] = vals.ravel()
        weights[offset : offset + block] = (wx_i / Q) * repeated_wy
        offset += block

    return WeightedSpectrum(energies=energies, weights=weights)


def full_chi(mu, temp, finite_spec, zero_spec):
    omega_b = grand_potential_from_spectrum(finite_spec, mu, temp)
    omega_0 = grand_potential_from_spectrum(zero_spec, mu, temp)
    return 2.0 * (omega_b - omega_0) / (FIELD_B * FIELD_B)


def lp_quadrature(gl_n):
    x, wx = normalized_legendre(gl_n)
    y, wy = normalized_legendre(gl_n)
    kx = math.pi * x
    ky = math.pi * y
    cosx = np.cos(kx)[:, None]
    cosy = np.cos(ky)[None, :]
    eps = -2.0 * T_HOP * (cosx + cosy)
    determinant = 4.0 * T_HOP * T_HOP * cosx * cosy
    weights = wx[:, None] * wy[None, :]
    return eps.ravel(), determinant.ravel(), weights.ravel()


def lp_chi(mu, temp, lp_data):
    eps, determinant, weights = lp_data
    return -np.sum(weights * fermi_prime(eps - mu, temp) * determinant)


def bisection_root(func, lo, hi, width):
    flo = float(func(lo))
    fhi = float(func(hi))
    initial_lo = float(lo)
    initial_hi = float(hi)
    initial_flo = flo
    initial_fhi = fhi

    if not (np.isfinite(flo) and np.isfinite(fhi) and flo * fhi < 0.0):
        return RootResult(
            root=float("nan"),
            initial_lo=initial_lo,
            initial_hi=initial_hi,
            final_lo=float(lo),
            final_hi=float(hi),
            initial_flo=initial_flo,
            initial_fhi=initial_fhi,
            final_flo=flo,
            final_fhi=fhi,
            steps=0,
        )

    steps = int(math.ceil(math.log2((hi - lo) / width)))
    for _ in range(steps):
        mid = 0.5 * (lo + hi)
        fmid = float(func(mid))
        if flo * fmid <= 0.0:
            hi = mid
            fhi = fmid
        else:
            lo = mid
            flo = fmid

    return RootResult(
        root=0.5 * (lo + hi),
        initial_lo=initial_lo,
        initial_hi=initial_hi,
        final_lo=float(lo),
        final_hi=float(hi),
        initial_flo=initial_flo,
        initial_fhi=initial_fhi,
        final_flo=flo,
        final_fhi=fhi,
        steps=steps,
    )


def bracket_claim(result):
    return (
        np.isfinite(result.root)
        and result.initial_lo <= result.root <= result.initial_hi
        and result.initial_flo * result.initial_fhi < 0.0
        and result.final_flo * result.final_fhi <= 0.0
        and (result.final_hi - result.final_lo) <= ROOT_WIDTH
    )


def max_abs_full_delta(mu_values, temp, finite_low, zero_low, finite_high, zero_high):
    deltas = []
    for mu in mu_values:
        low = full_chi(mu, temp, finite_low, zero_low)
        high = full_chi(mu, temp, finite_high, zero_high)
        deltas.append(abs(high - low))
    return float(np.max(deltas))


def max_abs_lp_delta(mu_values, temp, lp_low, lp_high):
    deltas = []
    for mu in mu_values:
        low = lp_chi(mu, temp, lp_low)
        high = lp_chi(mu, temp, lp_high)
        deltas.append(abs(high - low))
    return float(np.max(deltas))


def anchor_reproduction_check():
    computed = []
    expected = []
    for kx, ky in ANCHOR_K_POINTS:
        computed.append(square_band(kx, ky))
        expected.append(-2.0 * T_HOP * (math.cos(kx) + math.cos(ky)))
    return float(np.max(np.abs(np.asarray(computed) - np.asarray(expected))))


def gauge_delta():
    boundary = np.linalg.eigvalsh(
        hofstadter_stack(GAUGE_PROBE_KX, np.array([GAUGE_PROBE_KY]), "boundary")[0]
    )
    uniform = np.linalg.eigvalsh(
        hofstadter_stack(GAUGE_PROBE_KX, np.array([GAUGE_PROBE_KY]), "uniform")[0]
    )
    return float(np.max(np.abs(boundary - uniform)))


def wraparound_matrix_probe():
    h = hofstadter_stack(GAUGE_PROBE_KX, np.array([GAUGE_PROBE_KY]), "boundary")[0]
    return (
        h.shape == (Q, Q)
        and abs(abs(h[Q - 1, 0]) - T_HOP) <= WRAP_TOL
        and abs(abs(h[0, Q - 1]) - T_HOP) <= WRAP_TOL
        and abs(Q * FIELD_B - 2.0 * math.pi) <= WRAP_TOL
    )


def main():
    anchor_error = anchor_reproduction_check()
    check(
        "ANCHOR reproduction: m=0 square band is eps(k)=-2t(cos kx+cos ky)",
        anchor_error <= ANCHOR_TOL,
    )

    check(
        "finite-lattice wraparound/size probe: q=24 cyclic Hamiltonian carries B=2*pi/24",
        wraparound_matrix_probe(),
    )

    gd = gauge_delta()
    check(
        f"gauge invariance: boundary and uniform twist spectra agree within {GAUGE_TOL:.1e}",
        gd <= GAUGE_TOL,
    )

    print("Building quadrature data: full GL 160/224 and LP GL 128/256.")
    zero_low = zero_field_spectrum(FULL_GL_LOW)
    zero_high = zero_field_spectrum(FULL_GL_HIGH)
    finite_low = finite_field_spectrum(FULL_GL_LOW)
    finite_high = finite_field_spectrum(FULL_GL_HIGH)
    lp_low = lp_quadrature(LP_GL_LOW)
    lp_high = lp_quadrature(LP_GL_HIGH)

    anti_fab = full_chi(ANTI_FAB_MU, ANTI_FAB_T, finite_high, zero_high)
    check(
        f"anti-fabrication nonzero: chi_full(mu={ANTI_FAB_MU}, T={ANTI_FAB_T}) is nonzero",
        abs(anti_fab) >= ANTI_FAB_MIN_ABS_CHI,
    )

    full_t50 = full_chi(T50_MU, 50.0, finite_high, zero_high)
    lp_t50 = lp_chi(T50_MU, 50.0, lp_high)
    check(
        f"T=50 kill: finite-field chi at mu={T50_MU} is below {T50_FULL_TOL:.1e}",
        abs(full_t50) <= T50_FULL_TOL,
    )
    check(
        f"T=50 kill: LP chi at mu={T50_MU} is below {T50_LP_TOL:.1e}",
        abs(lp_t50) <= T50_LP_TOL,
    )

    fprime_zero = float(fermi_prime(np.array([0.0]), FPRIME_PROBE_T)[0])
    fprime_expected = -1.0 / (4.0 * FPRIME_PROBE_T)
    lp_far = lp_chi(FAR_BELOW_MU, FPRIME_PROBE_T, lp_high)
    check(
        "f' sign convention: f'(0,T) is the negative Fermi slope",
        abs(fprime_zero - fprime_expected) <= FPRIME_TOL,
    )
    check(
        f"f' known limit: LP chi(mu={FAR_BELOW_MU}, T={FPRIME_PROBE_T}) tends to zero below the band",
        abs(lp_far) <= LP_FAR_TOL,
    )

    results = []
    for temp in TEMPERATURES:
        full_lo, full_hi = FULL_ROOT_BRACKETS[temp]
        lp_lo, lp_hi = LP_ROOT_BRACKETS[temp]

        full_func = lambda mu, tt=temp: full_chi(mu, tt, finite_high, zero_high)
        lp_func = lambda mu, tt=temp: lp_chi(mu, tt, lp_high)

        full_result = bisection_root(full_func, full_lo, full_hi, ROOT_WIDTH)
        lp_result = bisection_root(lp_func, lp_lo, lp_hi, ROOT_WIDTH)

        check(
            f"full boundary bracket invariant at T={temp}",
            bracket_claim(full_result),
        )
        check(
            f"LP boundary bracket invariant at T={temp}",
            bracket_claim(lp_result),
        )

        full_probe_mus = (full_result.initial_lo, full_result.root, full_result.initial_hi)
        lp_probe_mus = (lp_result.initial_lo, lp_result.root, lp_result.initial_hi)
        full_delta = max_abs_full_delta(
            full_probe_mus, temp, finite_low, zero_low, finite_high, zero_high
        )
        lp_delta = max_abs_lp_delta(lp_probe_mus, temp, lp_low, lp_high)

        check(
            f"full GL 160/224 doubling at T={temp}: max |delta chi| <= {FULL_GL_DOUBLING_TOL:.1e}",
            np.isfinite(full_delta) and full_delta <= FULL_GL_DOUBLING_TOL,
        )
        check(
            f"LP GL 128/256 doubling at T={temp}: max |delta chi| <= {LP_GL_DOUBLING_TOL:.1e}",
            np.isfinite(lp_delta) and lp_delta <= LP_GL_DOUBLING_TOL,
        )

        deviation = abs(full_result.root - lp_result.root)
        results.append((temp, full_result.root, lp_result.root, deviation))
        print(
            "T={:.1f} eps_star={:.9f} mu_LP={:.9f} |eps_star-mu_LP|={:.9f}".format(
                temp, full_result.root, lp_result.root, deviation
            )
        )

    deviations = np.asarray([row[3] for row in results], dtype=np.float64)
    max_deviation = float(np.max(deviations))

    print("Deviation table:")
    for temp, eps_star, mu_lp, deviation in results:
        print(
            "  T={:.1f}: eps_star={:.9f}, mu_LP={:.9f}, abs_diff={:.9f}".format(
                temp, eps_star, mu_lp, deviation
            )
        )

    if max_deviation <= COMPARISON_TOL:
        check(
            f"comparison datum: full-field boundary tracks LP sign change within {COMPARISON_TOL:.2e}",
            np.all(np.isfinite(deviations)) and max_deviation <= COMPARISON_TOL,
        )
        print("Datum: finite-field boundary tracking accepted at the requested tolerance.")
    else:
        check(
            f"comparison datum: measured deviation table exceeds {COMPARISON_TOL:.2e}; full response is not LP at this finite field",
            np.all(np.isfinite(deviations)) and max_deviation > COMPARISON_TOL,
        )
        print("Datum: deviation accepted; the full finite-field response is not LP at these fields.")

    print(
        "Scope caveat: m=0 square lattice; full boundary uses finite B=2*pi/24, "
        "whereas LP is the B->0 band-curvature candidate."
    )
    finish()


if __name__ == "__main__":
    main()
