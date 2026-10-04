#!/usr/bin/env python3
"""Radial-Schroedinger check of the Sommerfeld argument used by the DM thermal lane.

Evidence for the 2026-09-30 corrigendum to the DM same-surface thermal notes.

Claim under test
  Two particles of mass m (reduced mass mu = m/2) with RELATIVE speed v feel
  V(r) = -alpha/r.  The s-wave contact enhancement is

      S = 2 pi eta / (1 - exp(-2 pi eta)),   eta = alpha / v      (attractive)

  (eta -> -eta for the repulsive channel).  The lane's thermal helpers used
  pi * zeta / (1 - exp(-pi * zeta)), zeta = alpha / v, together with the
  relative-speed weight v^2 exp(-x_f v^2 / 4).  That is the textbook formula
  written for the per-particle CM speed v/2, i.e. half the correct argument at
  fixed relative speed; it equals the correct S at alpha / 2.

Independent of the lane helpers:
  Part 1 integrates the radial Schroedinger equation numerically (no closed
         form) and compares with mpmath's Coulomb wave function and both
         closed forms.
  Part 2 checks from Gaussian velocity moments that v^2 exp(-x_f v^2 / 4) is
         the distribution of the relative speed.
  Part 3 recomputes the thermal averages (scipy quadrature, closed form) and
         compares them with the repaired lane helper; it reproduces the
         archived half-argument numbers as the corrected numbers at alpha / 2
         and prints the corrected pins.

This is a same-family check by its author, not an independent referee.
"""

from __future__ import annotations

import math
import sys

AUDIT_TIMEOUT_SEC = 300

import mpmath as mp
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

from dm_full_closure_minimal_reduced_cycle_extension_map_common import omega_b_from_eta
from dm_full_closure_same_surface_thermal_support_common import (
    ALPHA_HI,
    ALPHA_LO,
    OMEGA_DM_OBS,
    converged_same_surface_ratio,
)
from dm_leptogenesis_exact_common import ETA_OBS

PASS_COUNT = 0
FAIL_COUNT = 0

X_F = 25.0
A_MB = X_F / 4.0
R_BASE = 31.0 / 9.0

# Endpoint ratios quoted by the archived (half-argument) notes.
ARCHIVED_R_LO = 5.442019867867
ARCHIVED_R_HI = 5.482855571890
ARCHIVED_PI_FORM_ROOT_ALPHA = 0.090899546858439


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


# ---------------------------------------------------------------------------
# closed forms
# ---------------------------------------------------------------------------
def s_closed(alpha: float, v: float, factor: float) -> float:
    """y/(1-exp(-y)) with y = factor * alpha / v (factor = 2 pi correct, pi archived)."""
    y = factor * alpha / v
    if abs(y) < 1.0e-12:
        return 1.0
    if y < -700.0:
        return 0.0  # repulsive tunnelling suppression below double range
    return y / (-math.expm1(-y))


def s_correct(alpha: float, v: float) -> float:
    return s_closed(alpha, v, 2.0 * math.pi)


def s_archived(alpha: float, v: float) -> float:
    return s_closed(alpha, v, math.pi)


# ---------------------------------------------------------------------------
# radial Schroedinger equation, integrated directly
# ---------------------------------------------------------------------------
def s_radial(alpha: float, v_rel: float, mu: float) -> float:
    """S = |psi(0)|^2 / |psi_free(0)|^2 from u'' + (k^2 + 2 mu alpha / r) u = 0.

    Physical wave number k = mu * v_rel (hbar = c = 1).  alpha > 0 attractive,
    alpha < 0 repulsive.  u(0) = 0, u'(0) = 1; the asymptotic amplitude A is
    read from the WKB invariant (u^2 kappa + u'^2 / kappa) / k with
    kappa = sqrt(k^2 + 2 mu alpha / r).  Free solution: u = sin(kr) / k, so
    S = 1 / (A k)^2.
    """
    k = mu * v_rel
    r0 = 1.0e-8 / k
    r_max = (4000.0 + 40.0 * abs(mu * alpha / k)) / k

    def rhs(r: float, y: list[float]) -> list[float]:
        return [y[1], -(k * k + 2.0 * mu * alpha / r) * y[0]]

    eta = mu * alpha / k
    u0 = r0 * (1.0 - eta * k * r0)
    up0 = 1.0 - 2.0 * eta * k * r0
    sol = solve_ivp(rhs, [r0, r_max], [u0, up0], method="DOP853", rtol=1.0e-13, atol=1.0e-15)
    if sol.status != 0:
        raise RuntimeError("radial integration failed")
    r = sol.t[-1]
    u, up = sol.y[0, -1], sol.y[1, -1]
    kappa = math.sqrt(k * k + 2.0 * mu * alpha / r)
    amp2 = (u * u * kappa + up * up / kappa) / k
    return 1.0 / (amp2 * k * k)


def s_coulomb_function(alpha: float, v_rel: float) -> float:
    """C_0(eta)^2 from mpmath's regular Coulomb function (its eta > 0 is repulsive)."""
    old = mp.mp.dps
    mp.mp.dps = 30
    try:
        eta_mp = -mp.mpf(alpha) / mp.mpf(v_rel)
        z = mp.mpf("1e-10")
        val = (mp.coulombf(0, eta_mp, z) / z) ** 2
        return float(val)
    finally:
        mp.mp.dps = old


def part1_radial_equation() -> None:
    print("\n" + "=" * 88)
    print("PART 1: s-WAVE COULOMB FACTOR FROM THE RADIAL SCHROEDINGER EQUATION")
    print("=" * 88)

    # (alpha, v_rel): attractive and repulsive, thermal range at x_f = 25
    pairs = [
        (0.02, 0.5), (0.05, 0.4), (0.090667836017286, 0.4), (0.090667836017286, 0.2),
        (0.121, 0.1), (0.3, 0.6), (0.5, 0.25), (1.0, 0.5),
        (-0.015, 0.4), (-0.05, 0.4), (-0.0151, 0.1), (-0.1, 0.3), (-0.3, 0.5),
    ]
    worst_radial = 0.0
    worst_mass = 0.0
    worst_cf = 0.0
    worst_archived = 0.0
    rows = []
    for alpha, v in pairs:
        s_num = s_radial(alpha, v, mu=0.5)
        s_num_heavy = s_radial(alpha, v, mu=3.0)
        s2 = s_correct(alpha, v)
        s1 = s_archived(alpha, v)
        s_cf = s_coulomb_function(alpha, v)
        worst_radial = max(worst_radial, abs(s_num / s2 - 1.0))
        worst_mass = max(worst_mass, abs(s_num_heavy / s_num - 1.0))
        worst_cf = max(worst_cf, abs(s_cf / s2 - 1.0))
        worst_archived = max(worst_archived, abs(s1 / s_num - 1.0))
        rows.append((alpha, v, s_num, s2, s1))

    for alpha, v, s_num, s2, s1 in rows:
        print(
            f"  alpha={alpha:+.6f} v_rel={v:.2f}  radial={s_num:.7f}  2pi-form={s2:.7f}  "
            f"pi-form={s1:.7f} ({100.0 * (s1 / s_num - 1.0):+6.1f}%)"
        )
    print()

    check(
        "Radial equation reproduces S = 2 pi eta/(1 - exp(-2 pi eta)), eta = alpha/v_rel, on all 13 attractive/repulsive points",
        worst_radial < 2.0e-6,
        f"max relative deviation {worst_radial:.2e}",
    )
    check(
        "Result is independent of the reduced mass (mu = 0.5 vs 3): only eta = alpha/v_rel enters",
        worst_mass < 2.0e-6,
        f"max relative deviation {worst_mass:.2e}",
    )
    check(
        "mpmath's regular Coulomb function C_0(eta)^2 agrees with the 2 pi form",
        worst_cf < 1.0e-9,
        f"max relative deviation {worst_cf:.2e}",
    )
    check(
        "The archived pi-form is wrong by more than 5% somewhere on the thermal range",
        worst_archived > 0.05,
        f"max relative deviation {worst_archived:.2%}",
    )

    # archived pi-form at alpha equals the radial result at alpha / 2
    worst_half = 0.0
    for alpha, v in pairs[:8]:
        worst_half = max(worst_half, abs(s_archived(alpha, v) / s_radial(alpha / 2.0, v, mu=0.5) - 1.0))
    check(
        "The archived pi-form at alpha equals the radial-equation result at alpha/2 (half the argument)",
        worst_half < 2.0e-6,
        f"max relative deviation {worst_half:.2e}",
    )
    check(
        "Textbook form pi*alpha/v_cm with v_cm = v_rel/2 is the 2 pi form in v_rel",
        all(
            abs(s_closed(alpha, v / 2.0, math.pi) - s_correct(alpha, v)) < 1.0e-12
            for alpha, v in pairs
        ),
        "S_pi(alpha, v_cm = v_rel/2) == S_2pi(alpha, v_rel)",
    )


# ---------------------------------------------------------------------------
# thermal weight
# ---------------------------------------------------------------------------
def part2_relative_speed_weight() -> None:
    print("\n" + "=" * 88)
    print("PART 2: v^2 exp(-x_f v^2 / 4) IS THE RELATIVE-SPEED DISTRIBUTION")
    print("=" * 88)

    old = mp.mp.dps
    mp.mp.dps = 30
    try:
        a = mp.mpf(A_MB)

        def moment(power: int) -> mp.mpf:
            num = mp.quad(lambda v: v ** (2 + power) * mp.e ** (-a * v * v), [0, 1, mp.inf])
            den = mp.quad(lambda v: v * v * mp.e ** (-a * v * v), [0, 1, mp.inf])
            return num / den

        m2 = float(moment(2))
        m4 = float(moment(4))
    finally:
        mp.mp.dps = old

    # Two independent Maxwell-Boltzmann particles of mass m: each velocity
    # component has variance T/m = 1/x_f, so each component of v1 - v2 has
    # variance sigma2 = 2/x_f.  For a 3D Gaussian vector <v^2> = 3 sigma2 and
    # <v^4> = 15 sigma2^2.
    sigma2 = 2.0 / X_F
    check(
        "<v^2> of the weight equals 3 * (2 T/m) for the difference of two Maxwell velocities",
        abs(m2 - 3.0 * sigma2) < 1.0e-12,
        f"weight {m2:.12f}, Gaussian {3.0 * sigma2:.12f}",
    )
    check(
        "<v^4> of the weight equals 15 * (2 T/m)^2 for the difference of two Maxwell velocities",
        abs(m4 - 15.0 * sigma2 * sigma2) < 1.0e-12,
        f"weight {m4:.12f}, Gaussian {15.0 * sigma2 * sigma2:.12f}",
    )
    # A single-particle speed would give exp(-x_f v^2 / 2): <v^2> = 3/x_f, half of the relative one.
    check(
        "The single-particle weight exp(-x_f v^2/2) would give <v^2> = 3/x_f, half the relative-speed value",
        abs(3.0 / X_F - 0.5 * m2) < 1.0e-12,
        f"single-particle {3.0 / X_F:.12f}, half relative {0.5 * m2:.12f}",
    )


# ---------------------------------------------------------------------------
# lane numbers
# ---------------------------------------------------------------------------
def thermal_avg(alpha: float, attractive: bool, factor: float) -> float:
    sgn = 1.0 if attractive else -1.0

    def num(v: float) -> float:
        return s_closed(sgn * alpha, v, factor) * v * v * math.exp(-A_MB * v * v)

    def den(v: float) -> float:
        return v * v * math.exp(-A_MB * v * v)

    n = quad(num, 0.0, 1.0, epsabs=0.0, epsrel=1.0e-13, limit=400)[0] + quad(
        num, 1.0, 12.0, epsabs=0.0, epsrel=1.0e-13, limit=400
    )[0]
    d = quad(den, 0.0, 1.0, epsabs=0.0, epsrel=1.0e-13, limit=400)[0] + quad(
        den, 1.0, 12.0, epsabs=0.0, epsrel=1.0e-13, limit=400
    )[0]
    return n / d


def ratio(alpha_s: float, factor: float) -> float:
    """R = R_base * S_vis with the lane's 8:1 channel weights (singlet alpha*4/3, octet alpha/6)."""
    s1 = thermal_avg(4.0 / 3.0 * alpha_s, True, factor)
    s8 = thermal_avg(alpha_s / 6.0, False, factor)
    return R_BASE * (8.0 * s1 + s8) / 9.0


def part3_lane_numbers() -> None:
    print("\n" + "=" * 88)
    print("PART 3: LANE NUMBERS (SAME-SURFACE ENDPOINTS AND COUPLING PINS)")
    print("=" * 88)

    two_pi = 2.0 * math.pi
    r_lo = ratio(ALPHA_LO, two_pi)
    r_hi = ratio(ALPHA_HI, two_pi)
    lane_lo = converged_same_surface_ratio(ALPHA_LO)
    lane_hi = converged_same_surface_ratio(ALPHA_HI)
    check(
        "Independent quadrature agrees with the repaired lane helper at alpha_lo and alpha_hi",
        abs(r_lo - lane_lo) < 1.0e-9 and abs(r_hi - lane_hi) < 1.0e-9,
        f"R(alpha_lo)={r_lo:.9f} vs {lane_lo:.9f}; R(alpha_hi)={r_hi:.9f} vs {lane_hi:.9f}",
    )

    old_lo = ratio(ALPHA_LO, math.pi)
    old_hi = ratio(ALPHA_HI, math.pi)
    check(
        "The archived endpoint ratios 5.442019868 / 5.482855572 are reproduced by the pi-form",
        abs(old_lo - ARCHIVED_R_LO) < 1.0e-8 and abs(old_hi - ARCHIVED_R_HI) < 1.0e-8,
        f"pi-form R(alpha_lo)={old_lo:.9f}, R(alpha_hi)={old_hi:.9f}",
    )
    half_lo = ratio(ALPHA_LO / 2.0, two_pi)
    half_hi = ratio(ALPHA_HI / 2.0, two_pi)
    check(
        "...and equal the corrected ratios at half the coupling",
        abs(half_lo - old_lo) < 1.0e-9 and abs(half_hi - old_hi) < 1.0e-9,
        f"R_corrected(alpha_lo/2)={half_lo:.9f}, R_corrected(alpha_hi/2)={half_hi:.9f}",
    )

    omega_b = float(omega_b_from_eta(ETA_OBS))
    target = OMEGA_DM_OBS / omega_b
    check(
        "Corrected endpoint ratios both exceed the lane comparator ratio Omega_DM/Omega_b (0.268 / BBN Omega_b)",
        r_lo > target and r_hi > target,
        f"R_target={target:.9f}",
    )

    pin = brentq(lambda a: ratio(a, two_pi) - target, 0.02, 0.09, xtol=1.0e-13)
    check(
        "The corrected coupling that reproduces the comparator is half the archived pi-form root",
        abs(2.0 * pin - ARCHIVED_PI_FORM_ROOT_ALPHA) < 1.0e-9,
        f"corrected pin {pin:.10f}; 2 x pin {2.0 * pin:.10f}; archived root {ARCHIVED_PI_FORM_ROOT_ALPHA:.10f}",
    )

    print()
    print(f"  R(alpha_lo = {ALPHA_LO:.9f}): archived pi-form {old_lo:.6f}  corrected {r_lo:.6f}")
    print(f"  R(alpha_hi = {ALPHA_HI:.9f}): archived pi-form {old_hi:.6f}  corrected {r_hi:.6f}")
    print(f"  S_vis/S_dark at alpha_lo: archived {old_lo / R_BASE:.4f}  corrected {r_lo / R_BASE:.4f}")
    print()
    print("  Coupling that gives R = target (single coupling in both places):")
    print(f"  {'target':>30s}  {'archived pi-form':>18s}  {'corrected':>10s}")
    targets = [
        ("lane comparator", target),
        ("Planck-2018 central 5.3643", 0.1200 / 0.02237),
        ("rounded 0.268/0.049 = 5.469", 0.268 / 0.049),
        ("cosmology-note 5.48", 5.48),
    ]
    for label, t in targets:
        p_old = brentq(lambda a: ratio(a, math.pi) - t, 0.02, 0.2, xtol=1.0e-12)
        p_new = brentq(lambda a: ratio(a, two_pi) - t, 0.02, 0.2, xtol=1.0e-12)
        print(f"  {label:>30s}  {p_old:18.6f}  {p_new:10.6f}")
    print()
    print("  S_vis/S_dark over alpha in [0.03, 0.05] (notes quote 1.4 - 1.7):")
    for a in (0.03, 0.04, 0.048, 0.05):
        print(
            f"    alpha={a:.3f}: archived pi-form {ratio(a, math.pi) / R_BASE:.4f}   "
            f"corrected {ratio(a, two_pi) / R_BASE:.4f}"
        )


def main() -> int:
    print("=" * 88)
    print("DM SOMMERFELD ARGUMENT: RADIAL-SCHROEDINGER VERIFICATION")
    print("=" * 88)
    print("Same-family check by its author; not an independent referee.")

    part1_radial_equation()
    part2_relative_speed_weight()
    part3_lane_numbers()

    print("\n" + "=" * 88)
    print("BOTTOM LINE")
    print("=" * 88)
    print("  S = 2 pi eta/(1 - exp(-2 pi eta)) with eta = alpha / v_rel is the s-wave result for")
    print("  the relative-speed weight used by the lane.  The archived pi-form is the same")
    print("  function at half the coupling.  With the corrected kernel R(alpha_lo) and")
    print("  R(alpha_hi) are about 8, not 5.4-5.5, and the comparator ratio is reproduced at")
    print("  alpha near 0.045, outside the admitted same-surface family.")

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
