"""Narrow no-go for the lensing detector-centroid observable.

The exact first-order Kubo centroid observable has the edge form

    alpha(b) = sum_e c_e / (sqrt((x_e - x_src)^2 + (z_e - b)^2) + eps).

For any finite edge list, this has a large-impact-parameter multipole
expansion

    alpha(b) = M0 / b + M1 / b^2 + O(b^-3),

where M0 = sum_e c_e and M1 = sum_e c_e * (z_e - eps).  The lensing
centroid kernel has an almost cancelled monopole and a nonzero signed
dipole, so its asymptotic falloff is b^-2.  A nonzero nonnegative scalar
potential layer/path sum has M0 > 0 and therefore cannot be the same
centroid observable; it has b^-1 asymptotics.

This prunes the positive scalar-potential / path-weighted reduction route.
It does not claim standard ray lensing is impossible, and it does not replace
the full adjoint wave response with a retained continuum lensing theorem.
"""

from __future__ import annotations

import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from kubo_continuum_limit import BETA, K_PER_H, PW_PHYS, SRC_LAYER_FRAC, grow
from lensing_adjoint_kernel_probe import build_free_and_adjoint
from lensing_adjoint_kernel_reduced_model import (
    exact_edge_sum,
    log_slope,
    signed_edge_coefficients,
)


EPS = 0.1
H = 0.6
T_PHYS = 15.0
ASYM_B = [60.0, 90.0, 135.0, 200.0]
DIPOLE_B = [30.0, 45.0, 60.0, 80.0]
CONTROL_B = [45.0, 70.0, 105.0, 160.0]


checks: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    checks.append((name, bool(ok)))


def reciprocal_asymptotic_coeffs(edges, x_src: float) -> tuple[float, float, float]:
    m0 = 0.0
    m1 = 0.0
    m2 = 0.0
    for _layer, coeff, mx, mz in edges:
        dx = mx - x_src
        m0 += coeff
        m1 += coeff * (mz - EPS)
        m2 += coeff * ((mz - EPS) ** 2 - 0.5 * dx * dx)
    return m0, m1, m2


def asymptotic_sum(b: float, m0: float, m1: float, m2: float) -> float:
    return m0 / b + m1 / (b * b) + m2 / (b * b * b)


def positive_scalar_sum(edges, x_src: float, b: float) -> float:
    total = 0.0
    for _layer, coeff, mx, mz in edges:
        r = math.sqrt((mx - x_src) ** 2 + (mz - b) ** 2) + EPS
        total += abs(coeff) / r
    return total


def centered_gradient_surrogate(b: float, length: float = 10.0) -> float:
    return length / (b * math.sqrt((length / 2.0) ** 2 + b * b))


def main() -> None:
    nl = max(3, round(T_PHYS / H))
    k_phase = K_PER_H / H
    x_src = round(nl * SRC_LAYER_FRAC) * H

    pos, adj, _ = grow(0, 0.20, 0.70, nl, PW_PHYS, 3, H)
    amp, lam, cz_free, t0, _ = build_free_and_adjoint(
        pos, adj, nl, PW_PHYS, H, k_phase, BETA
    )
    edges = signed_edge_coefficients(pos, adj, H, k_phase, BETA, amp, lam)
    coeffs = np.array([edge[1] for edge in edges])

    m0, m1, m2 = reciprocal_asymptotic_coeffs(edges, x_src)
    abs_mass = float(np.sum(np.abs(coeffs)))
    mono_ratio = abs(m0) / abs_mass
    dipole_ratio = abs(m1) / abs_mass
    pos_abs = float(np.sum(np.abs(coeffs[coeffs > 0.0]))) / abs_mass
    neg_abs = float(np.sum(np.abs(coeffs[coeffs < 0.0]))) / abs_mass

    exact_asym_values = [exact_edge_sum(edges, x_src, b) for b in ASYM_B]
    asym3_values = [asymptotic_sum(b, m0, m1, m2) for b in ASYM_B]
    rel_errors = [
        abs(a - e) / abs(e) for a, e in zip(asym3_values, exact_asym_values)
    ]
    dipole_values = [exact_edge_sum(edges, x_src, b) for b in DIPOLE_B]
    slope_dipole_window = log_slope(DIPOLE_B, dipole_values)[0]

    control_values = [positive_scalar_sum(edges, x_src, b) for b in CONTROL_B]
    control_slope = log_slope(CONTROL_B, control_values)[0]

    centered_small_slope = log_slope(
        [3.0, 4.0, 5.0, 6.0],
        [centered_gradient_surrogate(b) for b in [3.0, 4.0, 5.0, 6.0]],
    )[0]

    check("finite edge list is nonempty", len(edges) > 100)
    check("centroid kernel has mixed signs", pos_abs > 0.15 and neg_abs > 0.15)
    check(
        "monopole cancellation: |M0|/sum|c| < 0.01",
        mono_ratio < 0.01,
    )
    check(
        "nonzero dipole: |M1|/sum|c| > 0.1",
        dipole_ratio > 0.1,
    )
    check(
        "three-term finite-edge asymptotic tracks exact sum at large b",
        max(rel_errors) < 0.02,
    )
    check(
        "exact centroid dipole window has slope near -2",
        abs(slope_dipole_window + 2.0) < 0.15,
    )
    check(
        "positive scalar-potential control keeps monopole slope",
        abs(control_slope + 1.0) < 0.08,
    )
    check(
        "old centered gradient surrogate is a different primitive",
        abs(centered_small_slope - slope_dipole_window) > 0.25,
    )

    print("=" * 88)
    print("LENSING CENTROID MULTIPOLE NO-GO")
    print("=" * 88)
    print(
        f"T_phys={T_PHYS:g} H={H:g} NL={nl} k_phase={k_phase:.6g} "
        f"x_src={x_src:.6g} cz_free={cz_free:+.6g} T0={t0:.6e}"
    )
    print(f"edges={len(edges)} eps={EPS}")
    print()
    print("Exact finite-edge expansion for alpha(b)=sum c_e/r_e(b):")
    print("  alpha(b) = M0/b + M1/b^2 + M2/b^3 + O(b^-4)")
    print(f"  M0=sum c_e                      = {m0:+.12e}")
    print(f"  M1=sum c_e*(z_e-eps)            = {m1:+.12e}")
    print(f"  M2=sum c_e*((z_e-eps)^2-dx^2/2) = {m2:+.12e}")
    print(f"  |M0|/sum|c| = {mono_ratio:.6e}")
    print(f"  |M1|/sum|c| = {dipole_ratio:.6e}")
    print(f"  sign split |c| positive/negative = {pos_abs:.3f}/{neg_abs:.3f}")
    print()
    print("Large-b exact vs three-term asymptotic:")
    print(f"{'b':>8s} {'exact':>16s} {'asym3':>16s} {'rel_err':>12s}")
    for b, exact, asym, rel in zip(ASYM_B, exact_asym_values, asym3_values, rel_errors):
        print(f"{b:8.1f} {exact:+16.8e} {asym:+16.8e} {rel:12.4%}")
    print(f"  dipole-window b={DIPOLE_B} slope = {slope_dipole_window:+.6f}")
    print()
    print("No-go control:")
    print(
        "  Replacing the signed centroid coefficients by nonnegative |c_e| gives "
        f"slope {control_slope:+.6f}, i.e. the uncancelled scalar-potential "
        "monopole."
    )
    print(
        "  The old centered finite-path gradient surrogate on b={3,4,5,6} has "
        f"slope {centered_small_slope:+.6f}; it is a separate b/r^3 ray-gradient "
        "primitive, not the code's adjoint centroid functional."
    )
    print()
    for name, ok in checks:
        print(("PASS" if ok else "FAIL"), name)
    print()
    n_pass = sum(1 for _, ok in checks if ok)
    n_fail = len(checks) - n_pass
    print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
    if n_fail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
