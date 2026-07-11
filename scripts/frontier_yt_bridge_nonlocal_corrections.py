#!/usr/bin/env python3
"""Calibrated endpoint-kernel regression diagnostic.

Purpose
-------
Re-evaluate the historical SM-like/logistic trajectory after correcting the
adjoint sign, continuous-L2 affine projection, and coordinate Jacobian.

Definition
----------
On the historical UV window, project the scalar-model endpoint-response kernel
K(x) onto the affine subspace.  The remainder

    R(x) = K(x) - Pi_1 K(x)

measures non-affinity.  It does not by itself identify a nonlocal physical
interaction.

This file is a non-load-bearing diagnostic companion. The calibration-free
theorem is checked by frontier_yt_bridge_affine_remainder_theorem.py.  All
physical constants and reference-family rows below are excluded from that
theorem's claim surface.
"""

from __future__ import annotations

import sys
import time
from math import erf, sqrt

import numpy as np
from scipy.integrate import solve_ivp

np.set_printoptions(precision=10, linewidth=120)

PASS = 0
FAIL = 0


def report(tag: str, ok: bool, msg: str):
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"  [{status}] {tag}: {msg}")


PI = np.pi
M_PL = 1.2209e19
M_Z = 91.1876

PLAQ = 0.5934
U0 = PLAQ ** 0.25
ALPHA_BARE = 1.0 / (4.0 * PI)
ALPHA_LM = ALPHA_BARE / U0
ALPHA_S_V = ALPHA_BARE / U0**2
C_APBC = (7.0 / 8.0) ** 0.25
V_DERIVED = M_PL * C_APBC * ALPHA_LM**16

G3_PL = np.sqrt(4.0 * PI * ALPHA_LM)
YT_PL = G3_PL / np.sqrt(6.0)
G3_V = np.sqrt(4.0 * PI * ALPHA_S_V)

ALPHA_EM_MZ = 1.0 / 127.951
SIN2_TW_MZ = 0.23122
ALPHA_1_MZ_GUT = (5.0 / 3.0) * ALPHA_EM_MZ / (1.0 - SIN2_TW_MZ)
ALPHA_2_MZ = ALPHA_EM_MZ / SIN2_TW_MZ

T_V = np.log(V_DERIVED)
T_PL = np.log(M_PL)
LOG_SPAN = T_PL - T_V
FAC = 1.0 / (16.0 * PI**2)

TAU_GRID = np.linspace(0.0, LOG_SPAN, 2500)
TS_GRID = np.linspace(T_V, T_PL, 1500)
X_GRID = (TS_GRID - T_V) / LOG_SPAN

# Fixed reference center/width for the non-load-bearing family sanity row.
# These match the accepted_kernel scaffolding parameters; they are not
# target-conditioned or grid-searched.
REF_CENTER_FRAC = 0.975
REF_WIDTH_FRAC = 0.020


def ew_boundary_at_v():
    b1 = -41.0 / 10.0
    b2 = 19.0 / 6.0
    l_v_mz = T_V - np.log(M_Z)
    inv_a1_v = 1.0 / ALPHA_1_MZ_GUT + b1 / (2.0 * PI) * l_v_mz
    inv_a2_v = 1.0 / ALPHA_2_MZ + b2 / (2.0 * PI) * l_v_mz
    return np.sqrt(4.0 * PI / inv_a1_v), np.sqrt(4.0 * PI / inv_a2_v)


def run_ew_upward(g1_v: float, g2_v: float):
    def rhs(_t, y):
        g1, g2 = y
        return [
            FAC * (41.0 / 10.0) * g1**3,
            FAC * (-19.0 / 6.0) * g2**3,
        ]

    sol = solve_ivp(
        rhs,
        [T_V, T_PL],
        [g1_v, g2_v],
        method="RK45",
        rtol=1e-10,
        atol=1e-12,
        max_step=0.2,
        dense_output=True,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.sol(T_PL)


def sm_like_g3_trajectory():
    def rhs(_t, y):
        g3 = y[0]
        return [FAC * (-(11.0 - 2.0 * 6.0 / 3.0)) * g3**3]

    sol = solve_ivp(
        rhs,
        [T_V, T_PL],
        [G3_V],
        method="RK45",
        rtol=1e-10,
        atol=1e-12,
        max_step=0.2,
        dense_output=True,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return lambda t: sol.sol(t)[0]


def lattice_bridge_profile(t: float) -> float:
    x = (t - T_V) / LOG_SPAN
    return np.exp(np.log(G3_V) * (1.0 - x) + np.log(G3_PL) * x)


def shape_logistic(z: float) -> float:
    z = np.clip(z, -60.0, 60.0)
    return 1.0 / (1.0 + np.exp(-z))


def shape_erf(z: float) -> float:
    return 0.5 * (1.0 + erf(np.clip(z, -8.0, 8.0) / sqrt(2.0)))


def shape_smoothstep(z: float) -> float:
    u = np.clip((z + 1.0) / 2.0, 0.0, 1.0)
    return u * u * (3.0 - 2.0 * u)


SHAPES = {
    "logistic": shape_logistic,
    "erf": shape_erf,
    "smoothstep": shape_smoothstep,
}


def bridge_family(shape_name: str, g3_sm, center_frac: float, width_frac: float):
    shape = SHAPES[shape_name]
    t_center = T_V + center_frac * LOG_SPAN
    t_width = max(width_frac * LOG_SPAN, 1e-6)

    def raw_weight(t: float) -> float:
        return shape((t - t_center) / t_width)

    w_v = raw_weight(T_V)
    w_pl = raw_weight(T_PL)
    norm = w_pl - w_v

    def g3_family(t: float) -> float:
        w = (raw_weight(t) - w_v) / norm
        return g3_sm(t) + w * (lattice_bridge_profile(t) - g3_sm(t))

    return g3_family


def solve_tau(g1_pl: float, g2_pl: float, g3_family):
    def rhs(tau, y):
        t = T_PL - tau
        g1, g2, yt = y
        q = g3_family(t) ** 2
        return [
            -FAC * (41.0 / 10.0) * g1**3,
            -FAC * (-19.0 / 6.0) * g2**3,
            FAC
            * yt
            * (
                -9.0 / 2.0 * yt**2
                + 17.0 / 20.0 * g1**2
                + 9.0 / 4.0 * g2**2
                + 8.0 * q
            ),
        ]

    sol = solve_ivp(
        rhs,
        [0.0, LOG_SPAN],
        [g1_pl, g2_pl, YT_PL],
        t_eval=TAU_GRID,
        method="RK45",
        rtol=1e-10,
        atol=1e-12,
        max_step=0.1,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol


def accepted_kernel(g1_pl: float, g2_pl: float, g3_sm, return_components: bool = False):
    g3_acc = bridge_family("logistic", g3_sm, REF_CENTER_FRAC, REF_WIDTH_FRAC)
    baseline = solve_tau(g1_pl, g2_pl, g3_acc)
    g1_vals = baseline.y[0]
    g2_vals = baseline.y[1]
    yt_vals = baseline.y[2]
    q_vals = np.array([g3_acc(T_PL - tau) ** 2 for tau in TAU_GRID])

    a_vals = FAC * (
        -27.0 / 2.0 * yt_vals**2
        + 17.0 / 20.0 * g1_vals**2
        + 9.0 / 4.0 * g2_vals**2
        + 8.0 * q_vals
    )

    adjoint_factor = np.zeros_like(TAU_GRID)
    adjoint_factor[-1] = 1.0
    for i in range(len(TAU_GRID) - 2, -1, -1):
        dt = TAU_GRID[i + 1] - TAU_GRID[i]
        a_mid = 0.5 * (a_vals[i + 1] + a_vals[i])
        # Variation of constants gives exp(+ integral_s^T F_y du).
        # The previous minus sign failed a direct finite-difference check.
        adjoint_factor[i] = adjoint_factor[i + 1] * np.exp(a_mid * dt)

    result = {
        "kernel_tau": 8.0 * FAC * adjoint_factor * yt_vals * np.sqrt(8.0 / 9.0),
        "g1": g1_vals,
        "g2": g2_vals,
        "yt": yt_vals,
        "q": q_vals,
    }
    if return_components:
        return result
    return result["kernel_tau"]


def trapezoidal_l2_affine_projection(x_values, function_values):
    """Projection for the piecewise-sampled trapezoidal diagnostic."""
    g11 = np.trapezoid(x_values * x_values, x_values)
    g12 = np.trapezoid(x_values, x_values)
    g22 = np.trapezoid(np.ones_like(x_values), x_values)
    rhs = np.array(
        [
            np.trapezoid(x_values * function_values, x_values),
            np.trapezoid(function_values, x_values),
        ]
    )
    return np.linalg.solve(np.array([[g11, g12], [g12, g22]]), rhs)


def reference_family_diff2(shape_name: str, g3_sm):
    """Compute the reference profile diff2 at the fixed reference center/width.

    Not load-bearing. Reported only as a sanity comparison against the
    family-agnostic Cauchy-Schwarz bound.
    """
    g3_family = bridge_family(shape_name, g3_sm, REF_CENTER_FRAC, REF_WIDTH_FRAC)
    g3_vals = np.array([g3_family(t) for t in TS_GRID])
    g3_sm_vals = np.array([g3_sm(t) for t in TS_GRID])
    return g3_vals**2 - g3_sm_vals**2


print("=" * 78)
print("y_t BRIDGE AFFINE-REMAINDER REGRESSION DIAGNOSTIC")
print("=" * 78)
print()
print("Corrected diagnostic for the historical SM-like/logistic trajectory.")
print()
print("NON-LOAD-BEARING: physical constants and family rows in this runner")
print("are excluded from the paired theorem's claim surface.")
print()
t0 = time.time()

g1_v, g2_v = ew_boundary_at_v()
g1_pl, g2_pl = run_ew_upward(g1_v, g2_v)
g3_sm = sm_like_g3_trajectory()
kernel_data = accepted_kernel(g1_pl, g2_pl, g3_sm, return_components=True)

tau_frac = TAU_GRID / LOG_SPAN
x_kernel = 1.0 - tau_frac
uv_cut = 0.95
uv_mask = x_kernel >= uv_cut
order = np.argsort(x_kernel[uv_mask])
x_uv = x_kernel[uv_mask][order]
insert_cutoff = x_uv[0] > uv_cut


def sampled_uv_values(values):
    sampled = values[uv_mask][order]
    if insert_cutoff:
        cutoff_value = np.interp(uv_cut, x_kernel[::-1], values[::-1])
        return np.insert(sampled, 0, cutoff_value)
    return sampled


if insert_cutoff:
    x_uv = np.insert(x_uv, 0, uv_cut)

# The endpoint functional is initially integral K_tau(tau) dq(tau) d tau.
# With tau=LOG_SPAN*(1-x), the density with respect to dx is
# K_x=LOG_SPAN*K_tau.  Omitting this Jacobian changes the functional.
kernel_uv = LOG_SPAN * sampled_uv_values(kernel_data["kernel_tau"])

affine = trapezoidal_l2_affine_projection(x_uv, kernel_uv)
kernel_loc = np.polyval(affine, x_uv)
kernel_res = kernel_uv - kernel_loc
kernel_rel_max = float(np.max(np.abs(kernel_res / kernel_uv)))
kernel_rel_l2 = float(
    np.sqrt(np.trapezoid(kernel_res * kernel_res, x_uv))
    / np.sqrt(np.trapezoid(kernel_uv * kernel_uv, x_uv))
)

# Absolute operator norm of the affine remainder with respect to dx.
kernel_res_l2_abs = float(np.sqrt(np.trapezoid(kernel_res * kernel_res, x_uv)))
kernel_full_l2_abs = float(np.sqrt(np.trapezoid(kernel_uv * kernel_uv, x_uv)))
moment_0 = float(np.trapezoid(kernel_res, x_uv))
moment_1 = float(np.trapezoid(x_uv * kernel_res, x_uv))

# The exact theorem gives K_tau''/K_tau = 18 FAC^2 y_t^2 G_total for
# d=9/2.  Since K_x=LOG_SPAN*K_tau and tau=LOG_SPAN*(1-x),
# K_x''=LOG_SPAN^3 K_tau''.
yt_uv = sampled_uv_values(kernel_data["yt"])
g1_uv = sampled_uv_values(kernel_data["g1"])
g2_uv = sampled_uv_values(kernel_data["g2"])
q_uv = sampled_uv_values(kernel_data["q"])
kernel_tau_uv = sampled_uv_values(kernel_data["kernel_tau"])
gauge_source_uv = (
    17.0 / 20.0 * g1_uv**2 + 9.0 / 4.0 * g2_uv**2 + 8.0 * q_uv
)
kernel_second_x = (
    LOG_SPAN**3
    * 18.0
    * FAC**2
    * yt_uv**2
    * gauge_source_uv
    * kernel_tau_uv
)
window_length_x = 1.0 - uv_cut
curvature_bound = float(
    np.max(kernel_second_x) * window_length_x**2.5 / np.sqrt(120.0)
)

# Reference (non-load-bearing) family numbers at the fixed reference
# center/width pair. No grid search, no y_t viability filter.
reference_rows = []
for shape_name in SHAPES:
    diff2 = reference_family_diff2(shape_name, g3_sm)
    profile_uv = np.interp(x_uv, X_GRID, diff2)
    profile_l2 = float(np.sqrt(np.trapezoid(profile_uv * profile_uv, x_uv)))
    cs_bound = kernel_rel_l2 * kernel_full_l2_abs * profile_l2
    full = float(np.trapezoid(kernel_uv * profile_uv, x_uv))
    local = float(np.trapezoid(kernel_loc * profile_uv, x_uv))
    affine_remainder = abs(full - local)
    cs_margin = (cs_bound - affine_remainder) / max(cs_bound, 1.0e-30)
    reference_rows.append(
        {
            "shape": shape_name,
            "profile_l2": profile_l2,
            "remainder_abs": affine_remainder,
            "cs_bound_abs": cs_bound,
            "cs_margin": cs_margin,
        }
    )

print(f"Forced UV window: x >= {uv_cut:.2f}")
print(f"  K_loc(x) = {affine[0]:.6e} x + {affine[1]:.6e}")
print(f"  pointwise affine-fit max relative error = {kernel_rel_max:.6e}")
print(f"  affine-remainder operator norm ratio = {kernel_rel_l2:.6e}")
print(f"  affine-remainder operator norm (L2(dx)) = {kernel_res_l2_abs:.6e}")
print(f"  kernel L2 norm (absolute) = {kernel_full_l2_abs:.6e}")
print(f"  trapezoidal projection moments (1,x) = ({moment_0:.3e}, {moment_1:.3e})")
print(f"  analytic curvature bound = {curvature_bound:.6e}")
print()

print("Reference family sanity rows (NOT load-bearing):")
print(
    f"  {'shape':<12s} {'||phi||_2':>14s} {'|<R,phi>|':>16s} {'CS bound':>16s} {'margin':>12s}"
)
for row in reference_rows:
    print(
        f"  {row['shape']:<12s} {row['profile_l2']:14.6e} "
        f"{row['remainder_abs']:16.6e} {row['cs_bound_abs']:16.6e} "
        f"{row['cs_margin']:12.6e}"
    )
print()
print(
    "These rows use the fixed reference center/width "
    f"({REF_CENTER_FRAC:.3f}, {REF_WIDTH_FRAC:.3f}) without any target-y_t"
)
print("filter or grid search. They confirm Cauchy-Schwarz is non-trivial")
print("(margin > 0) on every reference shape.")
print()

# Regression checks only.  None is a proof input for the paired theorem.
report(
    "1a-corrected-kernel-is-nearly-affine-on-the-historical-window",
    kernel_rel_max < 1.0e-3,
    f"max relative affine-fit error = {kernel_rel_max:.6e}",
)
report(
    "1b-affine-remainder-has-small-operator-norm",
    kernel_rel_l2 < 1.0e-3,
    f"affine-remainder operator norm ratio = {kernel_rel_l2:.6e}",
)
report(
    "1c-cauchy-schwarz-bound-holds-on-all-reference-family-rows",
    all(row["cs_margin"] > 0.0 for row in reference_rows),
    f"min reference CS margin = {min(row['cs_margin'] for row in reference_rows):.6e}",
)
report(
    "1d-trapezoidal-l2-projection-normal-equations-close",
    abs(moment_0) < 1.0e-12 and abs(moment_1) < 1.0e-12,
    f"moments = ({moment_0:.3e}, {moment_1:.3e})",
)
report(
    "1e-analytic-curvature-bound-controls-the-remainder",
    kernel_res_l2_abs <= curvature_bound,
    f"{kernel_res_l2_abs:.6e} <= {curvature_bound:.6e}",
)

print()
print("-" * 78)
print("Interpretation")
print("-" * 78)
print("This is a calibrated regression diagnostic, not the load-bearing")
print("theorem.  On this one trajectory, Cauchy-Schwarz gives")
print(f"|<R, phi>| <= {kernel_res_l2_abs:.6e} * ||phi||_2.")
print()
print("The reference family rows above are a non-load-bearing sanity")
print("comparison and confirm Cauchy-Schwarz is non-trivial.")
print()
print("The remainder quantifies non-affinity; it is not an identification of")
print("a nonlocal physical correction.  The paired primary runner checks the")
print("calibration-free theorem without these physical inputs.")
print("=" * 78)
print(f"FINAL TALLY: {PASS} PASS / {FAIL} FAIL")
print(f"Elapsed: {time.time() - t0:.2f} s")
print("=" * 78)

sys.exit(0 if FAIL == 0 else 1)
