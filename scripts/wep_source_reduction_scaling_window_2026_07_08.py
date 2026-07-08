#!/usr/bin/env python3
"""Source-side reduction identities and witnesses.

Companion runner for
WEP_SOURCE_REDUCTION_FINITE_SPACING_BOUNDARY_SCALING_WINDOW_BOUNDED_NOTE_2026-07-08.md.

This runner exhibits IDENTITIES and WITNESSES for the source-side reduction;
it derives no gravitational coupling and sets no audit status.
"""

from __future__ import annotations

import math

import numpy as np
import sympy as sp

# Read-only companion convention source:
# scripts/composite_mass_additivity_binding_defect_2026_07_08.py.
# Reuses its P-block construction, finite-ring momentum conventions,
# E(p)=arcsinh(sqrt(m^2+sin^2 p)), M_I=m*sqrt(1+m^2),
# F(x)=sinh(2x)/2, and even quartic/sextic curvature extraction.
from composite_mass_additivity_binding_defect_2026_07_08 import (  # noqa: E402
    fit_even_quartic,
    inertial_mass,
    lowest_pblock_energy,
    near_zero_indices,
    signed_momentum_value,
    universal_function,
)


PASS_COUNT = 0
FAIL_COUNT = 0
FLAGS: list[str] = []


def record(ok: bool, flag: str) -> bool:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
        FLAGS.append(flag)
    return ok


def rest_gap(m: float) -> float:
    return float(np.arcsinh(m))


def continuum_edge(m: float) -> float:
    return float(2.0 * rest_gap(m))


def fit_mass_at(L: int, m: float, U: float) -> tuple[float, float, float, float]:
    ks = near_zero_indices(L, 3)
    xs = np.array([signed_momentum_value(K, L) for K in ks], dtype=float)
    ys = np.array([lowest_pblock_energy(L, m, m, U, K) for K in ks], dtype=float)
    fit = fit_even_quartic(xs, ys, sextic=True)
    E0 = lowest_pblock_energy(L, m, m, U, 0)
    EB = continuum_edge(m) - E0
    return E0, EB, fit.mass, fit.residual


def bisection_to_rest_energy(L: int, m: float, E_star: float) -> tuple[float, float]:
    low = 0.0
    high = 1.0

    def energy(U: float) -> float:
        return lowest_pblock_energy(L, m, m, U, 0)

    while energy(high) > E_star:
        high *= 2.0
        if high > 64.0:
            raise RuntimeError(f"failed to bracket target energy for m={m}")

    mid = 0.5 * (low + high)
    E_mid = energy(mid)
    for _ in range(200):
        mid = 0.5 * (low + high)
        E_mid = energy(mid)
        if abs(E_mid - E_star) <= 1e-12:
            return mid, E_mid
        if E_mid > E_star:
            low = mid
        else:
            high = mid
    return mid, E_mid


def kappa_L(m: float, EB: float, L: int) -> float:
    """Bound-state size diagnostic: kappa = sqrt(2 mu E_B) with reduced
    inertial mass mu = M_I/2, so kappa_L = sqrt(M_I * E_B) * L. A composite
    extraction is SIZE-VALID only when the bound state fits the ring,
    kappa_L >= 8; below that the level mixes with the continuum and the
    fitted M_comp is a finite-size artifact (the failure mode of the first
    version of this runner's CHECK-05/06)."""
    if EB <= 0.0:
        return 0.0
    return float(np.sqrt(inertial_mass(m) * EB) * L)


def slope_loglog(xs: list[float], ys: list[float]) -> float:
    if any(x <= 0.0 for x in xs) or any(y <= 0.0 for y in ys):
        return float("nan")
    coeff = np.polyfit(np.log(np.array(xs, dtype=float)), np.log(np.array(ys, dtype=float)), 1)
    return float(coeff[0])


def strictly_increases_with_u(values_by_u: list[tuple[float, float]]) -> bool:
    ordered = [v for _, v in sorted(values_by_u)]
    return all(a < b for a, b in zip(ordered, ordered[1:]))


def check_01_singles_force_f() -> tuple[bool, str]:
    x = sp.symbols("x", real=True)
    residual = sp.simplify(sp.sinh(x) * sp.sqrt(1 + sp.sinh(x) ** 2) - sp.sinh(2 * x) / 2)
    ok = residual == 0
    record(ok, f"CHECK-01 singles uniqueness residual={residual}")
    return ok, f"CHECK-01 {'PASS' if ok else 'FAIL'} uniqueness_residual={residual}"


def check_02_convexity_breaks_free_composites() -> tuple[bool, str]:
    x = sp.symbols("x", positive=True, real=True)
    F = lambda z: sp.sinh(2 * z) / 2
    ratio_residual = sp.simplify(F(2 * x) / (2 * F(x)) - sp.cosh(2 * x))
    positive_witness = sp.simplify(sp.cosh(2 * x) - 1 - 2 * sp.sinh(x) ** 2)
    sinh_positive = sp.ask(sp.Q.positive(sp.sinh(x)))
    series = sp.series(sp.cosh(2 * x) - 1, x, 0, 4)
    coeff_x2 = sp.expand(series.removeO()).coeff(x, 2)
    assert coeff_x2 == 2
    ok = ratio_residual == 0 and positive_witness == 0 and sinh_positive is True and coeff_x2 == 2
    record(
        ok,
        f"CHECK-02 ratio_residual={ratio_residual} positive_witness={positive_witness} coeff_x2={coeff_x2}",
    )
    return ok, (
        "CHECK-02 {} F(2x)/(2F(x))-cosh(2x)={} "
        "positive_witness=cosh(2x)-1-2sinh(x)^2:{} sinh_positive={} "
        "free_violation_series={} coeff_x2={}"
    ).format("PASS" if ok else "FAIL", ratio_residual, positive_witness, sinh_positive, series, coeff_x2)


def check_03_same_rest_energy_different_inertia() -> tuple[bool, str]:
    L = 64
    m_a = 0.5
    m_b = 0.6
    edge_a = continuum_edge(m_a)
    edge_b = continuum_edge(m_b)
    E_star = 0.90 * edge_a
    adjusted = False
    if E_star >= edge_b - 1e-10:
        E_star = 0.90 * min(edge_a, edge_b - 1e-10)
        adjusted = True

    rows = []
    for m in (m_a, m_b):
        U, E0 = bisection_to_rest_energy(L, m, E_star)
        _, EB, M_comp, fit_residual = fit_mass_at(L, m, U)
        rows.append(
            {
                "m": m,
                "U": U,
                "E0": E0,
                "M": M_comp,
                "EB": EB,
                "fit_residual": fit_residual,
            }
        )

    equal_E = abs(rows[0]["E0"] - rows[1]["E0"])
    rel_M_diff = abs(rows[0]["M"] - rows[1]["M"]) / max(rows[0]["M"], rows[1]["M"])
    ok = equal_E <= 1e-10 and rel_M_diff >= 0.05
    record(ok, f"CHECK-03 equal_E={equal_E:.3e} rel_M_diff={rel_M_diff:.3e}")
    row_text = "; ".join(
        "m={m:.1f},U={U:.12e},E2_0={E0:.12e},M_comp={M:.12e},E_B={EB:.12e}".format(**row)
        for row in rows
    )
    return ok, (
        f"CHECK-03 {'PASS' if ok else 'FAIL'} E_star={E_star:.12e} "
        f"adjusted={adjusted} edge_A={edge_a:.12e} edge_B={edge_b:.12e} "
        f"equal_E={equal_E:.3e} rel_M_diff={rel_M_diff:.3e} rows=[{row_text}]"
    )


def check_04_scaling_window_exponents() -> tuple[bool, str]:
    m = sp.symbols("m", real=True)
    x = sp.symbols("x", real=True)
    F = lambda z: sp.sinh(2 * z) / 2

    mass_weight = 1 - 1 / sp.sqrt(1 + m**2)
    linear_rest = F(x) / x - 1
    free_comp = sp.cosh(2 * x) - 1

    coeff_a = sp.series(mass_weight, m, 0, 4).removeO().coeff(m, 2)
    coeff_b = sp.series(linear_rest, x, 0, 4).removeO().coeff(x, 2)
    coeff_c = sp.series(free_comp, x, 0, 4).removeO().coeff(x, 2)
    assert coeff_a == sp.Rational(1, 2)
    assert coeff_b == sp.Rational(2, 3)
    assert coeff_c == 2

    max_relerr = 0.0
    samples = []
    for m_val in (0.02, 0.05, 0.1):
        x_val = rest_gap(m_val)
        vals = (
            (1.0 - 1.0 / math.sqrt(1.0 + m_val * m_val), 0.5 * m_val * m_val),
            (universal_function(x_val) / x_val - 1.0, (2.0 / 3.0) * x_val * x_val),
            (math.cosh(2.0 * x_val) - 1.0, 2.0 * x_val * x_val),
        )
        rels = [abs(value / leading - 1.0) for value, leading in vals]
        max_relerr = max(max_relerr, max(rels))
        samples.append(f"m={m_val:.2f}:relerr_max={max(rels):.3e}")

    ok = max_relerr <= 0.20
    record(ok, f"CHECK-04 max_numeric_relerr={max_relerr:.3e}")
    return ok, (
        f"CHECK-04 {'PASS' if ok else 'FAIL'} coeffs=({coeff_a},{coeff_b},{coeff_c}) "
        f"numeric_20pct_max_relerr={max_relerr:.3e} samples=[{'; '.join(samples)}]"
    )


def check_05_binding_trend() -> tuple[bool, str]:
    """Binding trend at L = 256 with SIZE-VALID points only.

    Gates: (i) every point has kappa_L >= 8; (ii) the Q-coupling composite
    violation strictly increases with U for both masses; (iii) the
    F-coupling violation at the smallest binding is within 35% of its
    nonzero U -> 0 convexity baseline. The F-violation is NOT monotone:
    F(E_2)/M_comp crosses 1 at a fine-tuned, mass-dependent U (an
    accidental single-configuration WEP point, not species-blind
    universality) — the crossing is detected and reported."""
    L = 256
    pieces = []
    ok_all = True
    crossing_us = []
    for m in (0.5, 1.0):
        q_by_u: list[tuple[float, float]] = []
        eb_by_u: list[tuple[float, float]] = []
        baseline = abs(universal_function(continuum_edge(m)) / (2.0 * inertial_mass(m)) - 1.0)
        rows = []
        signed_f = []
        f_smallest_eb = None
        min_kappa = float("inf")
        for U in (0.1, 0.2, 0.4):
            E0, EB, M_comp, _ = fit_mass_at(L, m, U)
            kl = kappa_L(m, EB, L)
            min_kappa = min(min_kappa, kl)
            f_signed = universal_function(E0) / M_comp - 1.0
            f_violation = abs(f_signed)
            q_violation = abs(2.0 * inertial_mass(m) / M_comp - 1.0)
            signed_f.append((U, f_signed))
            q_by_u.append((U, q_violation))
            eb_by_u.append((U, EB))
            if f_smallest_eb is None:
                f_smallest_eb = f_violation
            rows.append(
                f"U={U:.1f},E_B={EB:.6e},kappaL={kl:.1f},Fv={f_violation:.6e},"
                f"Qv={q_violation:.6e},F_signed={f_signed:.6e}"
            )

        crossing = None
        ordered_signed = sorted(signed_f)
        for (u1, s1), (u2, s2) in zip(ordered_signed, ordered_signed[1:]):
            if s1 > 0.0 > s2 or s1 < 0.0 < s2:
                crossing = (u1, u2)
        crossing_us.append((m, crossing))

        q_mono = strictly_increases_with_u(q_by_u)
        eb_mono = strictly_increases_with_u(eb_by_u)
        base_consistency = abs(f_smallest_eb - baseline) / baseline
        size_ok = min_kappa >= 8.0
        ok_all = ok_all and q_mono and eb_mono and size_ok and base_consistency <= 0.35

        ordered_eb = [v for _, v in sorted(eb_by_u)]
        ordered_q = [v for _, v in sorted(q_by_u)]
        q_slope = slope_loglog(ordered_eb, ordered_q)
        pieces.append(
            f"m={m:.1f},baseline={baseline:.6e},min_kappaL={min_kappa:.1f},"
            f"Q_slope={q_slope:.6e},monotone(Q={q_mono},EB={eb_mono}),"
            f"F_base_consistency={base_consistency:.3e},"
            f"F_crossing_between_U={crossing},rows=[{'; '.join(rows)}]"
        )

    crossings_differ = (
        crossing_us[0][1] is not None
        and crossing_us[1][1] is not None
        and crossing_us[0][1] != crossing_us[1][1]
    )
    pieces.append(
        f"accidental_WEP_crossings_by_mass={crossing_us} differ={crossings_differ} "
        "(mass-dependent crossing cannot be species-blind)"
    )
    record(ok_all, "CHECK-05 size-valid binding trend gates failed")
    return ok_all, f"CHECK-05 {'PASS' if ok_all else 'FAIL'} {' | '.join(pieces)}"


def check_06_window_wep() -> tuple[bool, str]:
    """Scaling-window universality exhibit at a SIZE-VALID shallow bound
    state: m = 0.05, U tuned by bisection to E_B ~ 2e-3 (E_B/E_2(0) ~ 2%),
    L = 1024 so that kappa_L ~ 10. The first version of this leg used
    (U = 0.02, L = 64), where the pair's size ~ 180 sites cannot fit the
    ring and the extracted M_comp is a finite-size artifact."""
    m = 0.05
    L = 1024
    EB_target = 2.0e-3
    E_star = continuum_edge(m) - EB_target
    U, E0 = bisection_to_rest_energy(L, m, E_star)
    E0_fit, EB, M_comp, fit_residual = fit_mass_at(L, m, U)
    kl = kappa_L(m, EB, L)
    single_accel = inertial_mass(m) / inertial_mass(m)
    composite_accel = 2.0 * inertial_mass(m) / M_comp
    violation = abs(composite_accel - 1.0)
    gate = 5.0 * (2.0 * rest_gap(m) ** 2 + EB / E0)
    ok = EB > 0.0 and kl >= 8.0 and violation <= gate
    record(ok, f"CHECK-06 violation={violation:.3e} gate={gate:.3e} kappaL={kl:.1f} L={L}")
    return ok, (
        f"CHECK-06 {'PASS' if ok else 'FAIL'} L={L} m={m:.2f} U={U:.6e} "
        f"kappaL={kl:.1f} single_a/g={single_accel:.12e} composite_a/g={composite_accel:.12e} "
        f"E2_0={E0:.12e} continuum_edge={continuum_edge(m):.12e} separation=E_B={EB:.12e} "
        f"M_comp={M_comp:.12e} two_MI={2.0 * inertial_mass(m):.12e} "
        f"|a/g-1|={violation:.12e} gate={gate:.12e} fit_residual={fit_residual:.3e}"
    )


def main() -> int:
    print(
        "RUNNER WEP_SOURCE_REDUCTION scaling-window; "
        "E(p)=arcsinh(sqrt(m^2+sin^2 p)); M_I=m*sqrt(1+m^2); F=sinh(2x)/2; "
        "contact P-block from read-only companion"
    )
    c01_ok, c01 = check_01_singles_force_f()
    c02_ok, c02 = check_02_convexity_breaks_free_composites()
    print(f"{c01} | {c02}")
    _, c03 = check_03_same_rest_energy_different_inertia()
    print(c03)
    _, c04 = check_04_scaling_window_exponents()
    _, c05 = check_05_binding_trend()
    print(f"{c04} | {c05}")
    _, c06 = check_06_window_wep()
    flag_text = "none" if not FLAGS else " ; ".join(FLAGS)
    print(f"{c06} | TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT} FLAGS={flag_text}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
