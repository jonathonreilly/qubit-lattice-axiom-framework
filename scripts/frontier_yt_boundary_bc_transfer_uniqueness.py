#!/usr/bin/env python3
"""Bounded finite-grid diagnostic runner for
`YT_BOUNDARY_BC_TRANSFER_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-17`.

Verifies the bounded numerical diagnostic that the backward-RGE map
`Phi : y_t(v) -> y_t(M_Pl)` used in claim (iv) of `YT_BOUNDARY_THEOREM.md`
is finite on sampled trajectories, increasing on the runner's finite X-grid,
has finite observed grid slopes, and has a stable bracketed root of the
runner's imported Ward boundary target

    Phi(X*) = g_lattice / sqrt(6) = 0.43577

near `X* = 0.97267`.

The scan interval is below the empirically observed Yukawa blow-up-like onset
at X_pole ~ 1.27 in Section 6 (T5).

This is not a continuum strict-monotonicity proof and not an exact unique-root
theorem over every point in [0.5, 1.2]. It does NOT claim that the SM EFT is
physical at M_Pl. It does NOT claim that the lattice Ward identity holds in
the SM. It does NOT close the parent yt_boundary_theorem row.

The runner uses the SAME 2-loop SM RGE (`beta_2loop`) and threshold
machinery (`run_with_thresholds`) as `frontier_yt_boundary_consistency.py`.
The two runners are independent: the parent runner finds the root and
exhibits Options A / B / C; this runner verifies finite-grid root stability
and sampled well-behavior (grid monotonicity, finite-difference slopes,
no-blow-up) on the working scan interval.

CHECKS:
  Section 0: source-boundary checks
  Section 1: setup + imported numeric inputs
  Section 2: (T1) globalness / max|y_t| bounded on [0.5, 1.2]
  Section 3: (T2) finite-grid monotonicity on 33-point grid
  Section 4: (T3) Lipschitz constant L from finite differences
  Section 5: (T4) bracketed root stability via sign-change + brentq
  Section 6: (T5) Yukawa-Landau onset at X_pole ~ 1.27
  Section 7: stability of X* under integrator step size
  Section 8: SCORECARD

Self-contained: numpy + scipy only.
"""

from __future__ import annotations

import math
import sys
import time
from pathlib import Path

import numpy as np
from canonical_plaquette_surface import (
    CANONICAL_ALPHA_BARE,
    CANONICAL_ALPHA_LM,
    CANONICAL_ALPHA_S_V,
    CANONICAL_PLAQUETTE,
    CANONICAL_U0,
)

try:
    from scipy.integrate import solve_ivp
    from scipy.optimize import brentq
except ImportError:
    print("ERROR: scipy required. pip install scipy")
    sys.exit(1)

np.set_printoptions(precision=10, linewidth=120)
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/YT_BOUNDARY_BC_TRANSFER_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-17.md"

# ── Physical constants (same as parent runner; only used as RGE seeds) ─────

PI = np.pi
N_C = 3
M_PL = 1.2209e19           # GeV, unreduced Planck mass
M_Z = 91.1876               # GeV
M_T_POLE = 172.69           # GeV (PDG 2024); used ONLY as threshold scale, not as fit target
M_B_MSBAR = 4.18            # GeV
M_C_MSBAR = 1.27            # GeV

# Imported implementation constants for the bounded diagnostic.
PLAQ = CANONICAL_PLAQUETTE
U0 = CANONICAL_U0
ALPHA_BARE = CANONICAL_ALPHA_BARE
ALPHA_LM = CANONICAL_ALPHA_LM
ALPHA_S_V = ALPHA_BARE / U0**2
C_APBC = (7.0 / 8.0) ** 0.25
V_DERIVED = M_PL * C_APBC * ALPHA_LM ** 16

# Lattice couplings
G_LATTICE = np.sqrt(4 * PI * ALPHA_LM)
G_S_V = np.sqrt(4 * PI * ALPHA_S_V)

# Ward target
WARD_TARGET = G_LATTICE / np.sqrt(6.0)

# EW couplings at v (1-loop from M_Z; subdominant, treated as fixed
# initial-condition surface)
ALPHA_EM_MZ = 1.0 / 127.951
SIN2_TW_MZ = 0.23122
ALPHA_1_MZ_GUT = (5.0 / 3.0) * ALPHA_EM_MZ / (1.0 - SIN2_TW_MZ)
ALPHA_2_MZ = ALPHA_EM_MZ / SIN2_TW_MZ

b1_ew_dn = -41.0 / 10.0
b2_ew_dn = 19.0 / 6.0
L_v_MZ = np.log(V_DERIVED / M_Z)
inv_a1_v = 1.0 / ALPHA_1_MZ_GUT + b1_ew_dn / (2.0 * PI) * L_v_MZ
inv_a2_v = 1.0 / ALPHA_2_MZ + b2_ew_dn / (2.0 * PI) * L_v_MZ
G1_V = np.sqrt(4 * PI / inv_a1_v)
G2_V = np.sqrt(4 * PI / inv_a2_v)
LAMBDA_V = 0.129

# Working scan interval, below the sampled Yukawa blow-up-like onset.
X_LOW = 0.5
X_HIGH = 1.2

# Extension scan (for T5: locate Yukawa-Landau onset)
X_EXT_LOW = 1.20
X_EXT_HIGH = 1.30

# Lipschitz upper-bound claim
L_BOUND_GLOBAL = 10.0
L_BOUND_NEAR_ROOT = 1.5

# ── Logging ────────────────────────────────────────────────────────────

results_log = []
COUNTS = {"PASS": 0, "FAIL": 0}


def log(msg=""):
    results_log.append(msg)
    print(msg)


def check(name, condition, detail="", cls="D"):
    status = "PASS" if condition else "FAIL"
    COUNTS[status] += 1
    log(f"  [{status} ({cls})] {name}")
    if detail:
        log(f"         {detail}")


# =====================================================================
# 2-LOOP SM BETA FUNCTIONS (verbatim from frontier_yt_boundary_consistency.py)
# =====================================================================

def beta_2loop(t, y, n_f=6):
    """Full 2-loop SM RGEs for (g1, g2, g3, yt, lambda)."""
    g1, g2, g3, yt, lam = y
    fac = 1.0 / (16.0 * PI**2)
    fac2 = fac**2

    g1sq, g2sq, g3sq, ytsq = g1**2, g2**2, g3**2, yt**2

    # 1-loop gauge
    b1_1 = 41.0 / 10.0
    b2_1 = -(19.0 / 6.0)
    b3_1 = -(11.0 - 2.0 * n_f / 3.0)

    beta_g1_1 = b1_1 * g1**3
    beta_g2_1 = b2_1 * g2**3
    beta_g3_1 = b3_1 * g3**3

    # 1-loop Yukawa
    beta_yt_1 = yt * (9.0/2.0 * ytsq
                      - 17.0/20.0 * g1sq
                      - 9.0/4.0 * g2sq
                      - 8.0 * g3sq)

    # 1-loop Higgs quartic
    lamsq = lam**2
    beta_lam_1 = (24.0 * lamsq
                  + 12.0 * lam * ytsq - 6.0 * ytsq**2
                  - 3.0 * lam * (3.0 * g2sq + g1sq)
                  + 3.0/8.0 * (2.0 * g2sq**2 + (g2sq + g1sq)**2))

    # 2-loop gauge
    beta_g1_2 = g1**3 * (199.0/50.0 * g1sq + 27.0/10.0 * g2sq
                         + 44.0/5.0 * g3sq - 17.0/10.0 * ytsq)
    beta_g2_2 = g2**3 * (9.0/10.0 * g1sq + 35.0/6.0 * g2sq
                         + 12.0 * g3sq - 3.0/2.0 * ytsq)
    beta_g3_2 = g3**3 * (11.0/10.0 * g1sq + 9.0/2.0 * g2sq
                         - 26.0 * g3sq - 2.0 * ytsq)

    # 2-loop Yukawa
    beta_yt_2 = yt * (
        -12.0 * ytsq**2
        + ytsq * (36.0 * g3sq + 225.0/16.0 * g2sq + 131.0/80.0 * g1sq)
        + 1187.0/216.0 * g1sq**2
        - 23.0/4.0 * g2sq**2
        - 108.0 * g3sq**2
        + 19.0/15.0 * g1sq * g3sq
        + 9.0/4.0 * g2sq * g3sq
        + 6.0 * lamsq - 6.0 * lam * ytsq
    )

    dg1 = fac * beta_g1_1 + fac2 * beta_g1_2
    dg2 = fac * beta_g2_1 + fac2 * beta_g2_2
    dg3 = fac * beta_g3_1 + fac2 * beta_g3_2
    dyt = fac * beta_yt_1 + fac2 * beta_yt_2
    dlam = fac * beta_lam_1

    return [dg1, dg2, dg3, dyt, dlam]


def run_rge(y0, t_start, t_end, n_f=6, max_step=0.5):
    def rhs(t, y):
        return beta_2loop(t, y, n_f=n_f)
    sol = solve_ivp(
        rhs, [t_start, t_end], y0,
        method='RK45', rtol=1e-9, atol=1e-11,
        max_step=max_step, dense_output=False
    )
    if not sol.success:
        raise RuntimeError(f"RGE failed: {sol.message}")
    return sol


def run_with_thresholds(y0, t_start, t_end, max_step=0.5):
    """Backward (or forward) run with SM threshold matching."""
    running_down = t_start > t_end

    thresholds = [
        (np.log(M_T_POLE), 6, 5),
        (np.log(M_B_MSBAR), 5, 4),
        (np.log(M_C_MSBAR), 4, 3),
    ]
    if running_down:
        thresholds.sort(key=lambda x: -x[0])
    else:
        thresholds.sort(key=lambda x: x[0])

    active_thresholds = []
    for t_th, nf_above, nf_below in thresholds:
        if running_down:
            if t_end < t_th < t_start:
                active_thresholds.append((t_th, nf_above, nf_below))
        else:
            if t_start < t_th < t_end:
                active_thresholds.append((t_th, nf_above, nf_below))

    mu_start = np.exp(t_start)
    if mu_start > M_T_POLE:
        nf_current = 6
    elif mu_start > M_B_MSBAR:
        nf_current = 5
    elif mu_start > M_C_MSBAR:
        nf_current = 4
    else:
        nf_current = 3

    segments = []
    current_t = t_start
    for t_th, nf_above, nf_below in active_thresholds:
        segments.append((current_t, t_th, nf_current))
        current_t = t_th
        nf_current = nf_below if running_down else nf_above
    segments.append((current_t, t_end, nf_current))

    y_current = list(y0)
    for t_s, t_e, nf in segments:
        if abs(t_s - t_e) < 1e-10:
            continue
        sol = run_rge(y_current, t_s, t_e, n_f=nf, max_step=max_step)
        y_current = list(sol.y[:, -1])
    return np.array(y_current)


# =====================================================================
# The map Phi : X -> y_t(M_Pl) (backward run from t_v to t_Pl)
# =====================================================================

t_v = np.log(V_DERIVED)
t_Pl = np.log(M_PL)


def Phi(X, max_step=1.0):
    """Backward-RGE map y_t(v) = X -> y_t(M_Pl)."""
    y0 = [G1_V, G2_V, G_S_V, float(X), LAMBDA_V]
    y_Pl = run_with_thresholds(y0, t_v, t_Pl, max_step=max_step)
    return float(y_Pl[3])


def max_yt_on_trajectory(X, max_step=1.0):
    """Return max |y_t| on the trajectory from t_v to t_Pl."""
    y0 = [G1_V, G2_V, G_S_V, float(X), LAMBDA_V]
    def rhs(t, y):
        return beta_2loop(t, y, n_f=6)
    sol = solve_ivp(
        rhs, [t_v, t_Pl], y0,
        method='RK45', rtol=1e-9, atol=1e-11,
        max_step=max_step, dense_output=False
    )
    if not sol.success:
        return float('inf')
    return float(np.max(np.abs(sol.y[3])))


# =====================================================================
print("=" * 78)
print("BOUNDARY BC-TRANSFER FINITE-GRID DIAGNOSTIC")
print("=" * 78)
print()
t0 = time.time()

# =====================================================================
log("=" * 78)
log("SECTION 0: Source-boundary checks")
log("=" * 78)
log()
note_text = NOTE.read_text(encoding="utf-8")
note_flat = " ".join(note_text.split())
check(
    "section0_2026_06_07_boundary_present",
    "2026-06-07 Implementation-Input Boundary Retargeting" in note_text,
    "source note carries the implementation-input retargeting section",
)
check(
    "section0_source_status_is_conditional_support",
    "**Claim type:** bounded_theorem" in note_text
    and "**Type:** bounded_theorem" in note_text
    and "conditional finite-grid implementation diagnostic only" in note_flat
    and "not a continuum uniqueness theorem, physical BC-transfer theorem" in note_flat
    and "No new axiom, retained bridge, downstream status, ledger tag, or publication" in note_flat,
    "source type/status matches the finite-grid implementation boundary",
)
check(
    "section0_imports_are_implementation_inputs",
    "visible" in note_text
    and "declared implementation inputs" in note_text
    and "declared/admitted implementation inputs for this bounded" in note_text,
    "canonical plaquette and Ward target are not proof authorities for this row",
)
check(
    "section0_continuum_claims_excluded",
    "does not assert continuum" in note_text
    and "unique-root closure" in note_text
    and "does not claim continuum monotonicity, exact continuum uniqueness" in note_text,
    "finite grid diagnostic only",
)
check(
    "section0_declared_inputs_enumerated",
    all(token in note_text for token in ("**I1:**", "**I2:**", "**I3:**", "**I4:**", "**I5:**")),
    "plaquette, Ward target, RGE, thresholds, and EW initial conditions are enumerated",
)
check(
    "section0_inputs_admitted_not_retained",
    "2026-06-20 Source-Boundary Repair" in note_text
    and "None of `I1`–`I5` carries a retained-grade dependency edge" in note_flat
    and "supplied/" in note_flat and "admitted inputs" in note_flat
    and "finite-grid numerical diagnostic conditional on `I1`–`I5`" in note_flat
    and "not a retained-grade theorem" in note_flat,
    "I1-I5 are admitted (not retained-grade, not self-contained-derived); result is conditional finite-grid diagnostic",
)
check(
    "section0_runner_count_updated",
    "Counts: 31 PASS, 0 FAIL" in note_text,
    "note scorecard matches source-boundary runner",
)
check(
    "section0_no_retained_input_overclaim",
    "cited as retained inputs" not in note_text,
    "old retained-input wording removed",
)
log()

# =====================================================================
log("=" * 78)
log("SECTION 1: Imported numeric inputs")
log("=" * 78)
log()
log(f"  alpha_LM             = {ALPHA_LM:.6f}     (imported from canonical_plaquette_surface)")
log(f"  alpha_s(v) = CMT     = {ALPHA_S_V:.6f}     (block 10 narrow, alpha_bare/u_0^2)")
log(f"  g_lattice(M_Pl)      = {G_LATTICE:.6f}     (sqrt(4 pi alpha_LM))")
log(f"  Ward target y_t(M_Pl) = g_lattice/sqrt(6)  = {WARD_TARGET:.6f}")
log(f"  v_derived             = {V_DERIVED:.4e} GeV (hierarchy theorem)")
log(f"  ln(M_Pl / v_derived)  = {t_Pl - t_v:.3f}   (17-decade segment)")
log()
log(f"  Scan interval X = y_t(v) in [{X_LOW}, {X_HIGH}]")
log(f"  Chosen below Yukawa-Landau-like onset at X_pole ~ 1.27 (see (T5))")
log()

check(
    "section1_v_derived_matches_canonical",
    abs(V_DERIVED - 246.28) / 246.28 < 0.01,
    f"v_derived = {V_DERIVED:.2f} GeV matches canonical 246.28 GeV",
)
check(
    "section1_ward_target_value",
    abs(WARD_TARGET - 0.43577) < 5e-4,
    f"WARD_TARGET = {WARD_TARGET:.6f} matches 0.43577 to 5e-4",
)
check(
    "section1_gv_ordering",
    G_S_V > G2_V > G1_V,
    f"g3(v)={G_S_V:.4f} > g2(v)={G2_V:.4f} > g1(v)={G1_V:.4f}  (expected SM ordering)",
)
log()


# =====================================================================
log("=" * 78)
log("SECTION 2: (T1) Globalness / max|y_t| bounded on [0.5, 1.2]")
log("=" * 78)
log()
log("  Sample max|y_t| on trajectory across X grid; verify bounded.")
log()

X_grid_coarse = np.linspace(X_LOW, X_HIGH, 8)
max_yt_arr = []
for X in X_grid_coarse:
    m_yt = max_yt_on_trajectory(X, max_step=1.0)
    max_yt_arr.append(m_yt)
    log(f"    X = {X:.3f}:  max|y_t on trajectory| = {m_yt:.4f}")

max_yt_arr = np.array(max_yt_arr)
log()
log(f"  Max-of-max|y_t| across grid: {max_yt_arr.max():.4f}")
log()

check(
    "T1_all_trajectories_finite",
    np.all(np.isfinite(max_yt_arr)),
    "All trajectories finite (no integrator blow-up) across the scan grid",
)
check(
    "T1_max_yt_bounded_by_X_HIGH_plus_eps",
    max_yt_arr.max() < X_HIGH + 0.05,
    f"max|y_t| = {max_yt_arr.max():.4f} < {X_HIGH + 0.05} across [0.5, 1.2] (no upward amplification)",
)
check(
    "T1_max_yt_no_amplification",
    bool(np.all(max_yt_arr <= np.array(X_grid_coarse) + 0.03)),
    f"max|y_t| on trajectory <= X + 0.03 across the grid (trajectory does NOT exceed initial value within tolerance)",
)
check(
    "T1_max_yt_starts_at_X",
    abs(max_yt_arr[0] - X_LOW) < 0.02 and abs(max_yt_arr[-1] - X_HIGH) < 0.04,
    f"max|y_t| at endpoints tracks X (no spurious amplification at low X)",
)
log()


# =====================================================================
log("=" * 78)
log("SECTION 3: (T2) Finite-grid monotonicity on 33-point grid")
log("=" * 78)
log()
log("  Compute Phi on a finite X-grid; verify all sampled forward differences are positive.")
log()

X_grid_fine = np.linspace(X_LOW, X_HIGH, 33)
Phi_vals = np.array([Phi(X, max_step=1.0) for X in X_grid_fine])

log(f"  Sample of (X, Phi(X)):")
for i in range(0, len(X_grid_fine), 4):
    log(f"    X = {X_grid_fine[i]:.4f}  ->  Phi = {Phi_vals[i]:.6f}")
log(f"    X = {X_grid_fine[-1]:.4f}  ->  Phi = {Phi_vals[-1]:.6f}")
log()

diffs = np.diff(Phi_vals)
n_increasing = int(np.sum(diffs > 0))
n_decreasing = int(np.sum(diffs <= 0))

log(f"  Of {len(diffs)} forward differences:")
log(f"    {n_increasing} positive forward differences")
log(f"    {n_decreasing} non-increasing")
log()

check(
    "T2_grid_monotonicity",
    n_decreasing == 0 and n_increasing == len(diffs),
    f"All {len(diffs)} sampled forward differences > 0 on the 33-point grid",
)
check(
    "T2_endpoint_ordering",
    Phi_vals[0] < Phi_vals[-1],
    f"Phi({X_LOW}) = {Phi_vals[0]:.6f} < Phi({X_HIGH}) = {Phi_vals[-1]:.6f}",
)
check(
    "T2_min_forward_diff_positive",
    diffs.min() > 0,
    f"min forward diff = {diffs.min():.6e} > 0",
)
log()


# =====================================================================
log("=" * 78)
log("SECTION 4: (T3) Lipschitz constant L from finite differences")
log("=" * 78)
log()
log("  L_observed = max |Phi(X1) - Phi(X2)| / |X1 - X2| over the working grid.")
log()

# Global Lipschitz on fine grid
dX = X_grid_fine[1] - X_grid_fine[0]
local_L_global = np.abs(diffs) / dX
L_observed_global = float(local_L_global.max())
L_observed_global_min = float(local_L_global.min())

log(f"  Global samples on [{X_LOW}, {X_HIGH}]:")
log(f"    max local L  = {L_observed_global:.4f}")
log(f"    min local L  = {L_observed_global_min:.4f}")
log(f"    mean local L = {local_L_global.mean():.4f}")
log()

# Near-root tight sample on [0.9, 1.0]
X_near = np.linspace(0.9, 1.0, 21)
Phi_near = np.array([Phi(X, max_step=1.0) for X in X_near])
local_L_near = np.diff(Phi_near) / np.diff(X_near)
L_observed_near = float(local_L_near.max())
L_observed_near_min = float(local_L_near.min())

log(f"  Near-root samples on [0.9, 1.0]:")
log(f"    max local L  = {L_observed_near:.4f}")
log(f"    min local L  = {L_observed_near_min:.4f}")
log(f"    mean local L = {local_L_near.mean():.4f}")
log()
log(f"  Interpretation: near the root, a 1% perturbation in y_t(M_Pl)")
log(f"                  corresponds to ~ 1/L_observed_near = {1.0/L_observed_near:.3f}")
log(f"                  sensitivity in y_t(v).")
log()

check(
    "T3_lipschitz_finite_global",
    np.isfinite(L_observed_global) and L_observed_global > 0,
    f"L_observed_global = {L_observed_global:.4f} (finite, positive)",
)
check(
    "T3_lipschitz_global_below_bound",
    L_observed_global < L_BOUND_GLOBAL,
    f"L_observed_global = {L_observed_global:.4f} < {L_BOUND_GLOBAL} (declared diagnostic bound)",
)
check(
    "T3_lipschitz_lower_bound_positive",
    L_observed_global_min > 0,
    f"min local L = {L_observed_global_min:.4f} > 0 (no zero-derivative points)",
)
check(
    "T3_lipschitz_near_root_below_bound",
    L_observed_near < L_BOUND_NEAR_ROOT,
    f"L_observed_near = {L_observed_near:.4f} < {L_BOUND_NEAR_ROOT} (declared near-root diagnostic bound)",
)
log()


# =====================================================================
log("=" * 78)
log("SECTION 5: (T4) Bracketed root stability via sign-change + brentq")
log("=" * 78)
log()
log("  Sign change: verify Phi(X_LOW) < WARD_TARGET < Phi(X_HIGH)")
log()
log(f"    Phi({X_LOW}) = {Phi_vals[0]:.6f}")
log(f"    WARD_TARGET = {WARD_TARGET:.6f}")
log(f"    Phi({X_HIGH}) = {Phi_vals[-1]:.6f}")
log()

sign_change = (Phi_vals[0] < WARD_TARGET < Phi_vals[-1])
check(
    "T4_sign_change_in_interval",
    sign_change,
    f"Sign change Phi(X_LOW)={Phi_vals[0]:.4f} < {WARD_TARGET:.4f} < Phi(X_HIGH)={Phi_vals[-1]:.4f}",
)

# Find root via brentq on full interval
def residual(X):
    return Phi(X) - WARD_TARGET

X_star_full = brentq(residual, X_LOW, X_HIGH, xtol=1e-10)
log(f"  brentq on [{X_LOW}, {X_HIGH}]:  X* = {X_star_full:.10f}")
log(f"                                  Phi(X*) = {Phi(X_star_full):.10f}")
log(f"                                  residual = {Phi(X_star_full) - WARD_TARGET:.2e}")
log()

# Check root stability by also finding the bracketed root on three different
# sign-changing subintervals that each contain X*:
subintervals = [
    (X_LOW, 1.1),
    (0.7, X_HIGH),
    (0.85, 1.1),
]
sub_roots = []
log("  Independence-of-subinterval check:")
for lo, hi in subintervals:
    res_lo = Phi(lo) - WARD_TARGET
    res_hi = Phi(hi) - WARD_TARGET
    if res_lo * res_hi < 0:
        X_sub = brentq(residual, lo, hi, xtol=1e-10)
        sub_roots.append(X_sub)
        log(f"    [{lo}, {hi}]:  X* = {X_sub:.10f}")
    else:
        log(f"    [{lo}, {hi}]:  no sign change in subinterval (SKIPPED)")

sub_roots_arr = np.array(sub_roots)
max_root_spread = float(np.max(sub_roots_arr) - np.min(sub_roots_arr)) if len(sub_roots) > 1 else 0.0
log()
log(f"  Max spread across subinterval roots: {max_root_spread:.2e}")
log()

check(
    "T4_all_subintervals_with_signchange_agree",
    max_root_spread < 1e-7,
    f"All {len(sub_roots)} sub-roots agree to {max_root_spread:.2e}",
)

root_stability_claim = (n_decreasing == 0) and sign_change and max_root_spread < 1e-7
check(
    "T4_grid_root_bracketed_by_sampled_monotonicity",
    root_stability_claim,
    "Sampled monotonicity + sign change + subinterval agreement support a stable bracketed root; not a continuum uniqueness proof",
)

# Numerical value of X*
check(
    "T4_X_star_value_near_0p973",
    abs(X_star_full - 0.973) < 5e-3,
    f"X* = {X_star_full:.6f} matches parent runner value 0.973 (to 5e-3)",
)
log()


# =====================================================================
log("=" * 78)
log("SECTION 6: (T5) Yukawa-Landau onset at X_pole ~ 1.27")
log("=" * 78)
log()
log("  Extend the scan into [1.20, 1.30] and locate the Yukawa-Landau-like")
log("  onset to verify that the chosen scan interval [0.5, 1.2] lies below")
log("  the sampled blow-up-like region.")
log()

X_ext = np.arange(X_EXT_LOW, X_EXT_HIGH + 0.001, 0.01)
Phi_ext = np.array([Phi(X, max_step=1.0) for X in X_ext])
max_yt_ext = np.array([max_yt_on_trajectory(X, max_step=1.0) for X in X_ext])

log(f"  Extension scan in [{X_EXT_LOW}, {X_EXT_HIGH}]:")
for i, X in enumerate(X_ext):
    log(f"    X = {X:.3f}:  Phi = {Phi_ext[i]:8.3f}    max|y_t| = {max_yt_ext[i]:9.3f}")
log()

# Locate "pole" as the first X where Phi exceeds 5 (well above the working
# range and clearly into Landau-pole-like blow-up)
pole_idx = int(np.argmax(Phi_ext > 5.0))
if Phi_ext[pole_idx] > 5.0:
    X_pole = float(X_ext[pole_idx])
    log(f"  First X in extension with Phi > 5:  X_pole ~ {X_pole:.3f}")
    log(f"  Phi(X_pole)                          = {Phi_ext[pole_idx]:.3f}")
else:
    X_pole = float('inf')
    log(f"  No Phi > 5 in extension scan (no Landau onset detected up to {X_EXT_HIGH})")
log()

check(
    "T5_phi_at_X12_bounded",
    Phi_ext[0] < 2.0,
    f"Phi({X_EXT_LOW}) = {Phi_ext[0]:.4f} < 2.0 (chosen scan boundary still well-behaved)",
)
check(
    "T5_yukawa_landau_pole_exists_in_extension",
    np.isfinite(X_pole) and X_pole > X_HIGH,
    f"Yukawa-Landau onset detected at X_pole = {X_pole:.3f} > X_HIGH = {X_HIGH} (extension shows blow-up)",
)
check(
    "T5_scan_interval_strictly_below_pole",
    X_pole > X_HIGH,
    f"Scan interval [0.5, {X_HIGH}] strictly below X_pole = {X_pole:.3f}",
)
check(
    "T5_root_well_inside_well_defined_region",
    X_pole - X_star_full > 0.25,
    f"X_pole - X* = {X_pole - X_star_full:.3f} > 0.25 (root sits well inside well-defined region)",
)
log()


# =====================================================================
log("=" * 78)
log("SECTION 7: Stability of X* under integrator step size")
log("=" * 78)
log()
log("  Refine integrator max_step; X* should be stable to <= 1e-5.")
log()

X_star_by_step = []
for max_s in [2.0, 1.0, 0.5, 0.2]:
    def residual_s(X, ms=max_s):
        return Phi(X, max_step=ms) - WARD_TARGET
    X_s = brentq(residual_s, X_LOW, X_HIGH, xtol=1e-10)
    X_star_by_step.append((max_s, X_s))
    log(f"    max_step = {max_s:.2f}:  X* = {X_s:.10f}")

X_values = np.array([xs for _, xs in X_star_by_step])
X_spread = float(np.max(X_values) - np.min(X_values))
log()
log(f"  Spread across step sizes: {X_spread:.2e}")
log()

check(
    "step_size_stability",
    X_spread < 1e-5,
    f"X* stable to {X_spread:.2e} across integrator step sizes",
)


# =====================================================================
log()
log("=" * 78)
log("SECTION 8: SCORECARD")
log("=" * 78)
log()
log(f"  Backward-RGE map Phi : X = y_t(v) -> y_t(M_Pl)")
log(f"  on segment [ln v_derived, ln M_Pl] (Delta t = {t_Pl - t_v:.3f} natural-log units, ~17 decades).")
log()
log(f"  Verified properties on scan interval X in [{X_LOW}, {X_HIGH}]:")
log()
log(f"    (T1) Globalness:        YES  (max|y_t| <= {max_yt_arr.max():.4f})")
log(f"    (T2) Grid monotonicity: YES  (positive on 33-point grid; min diff > 0)")
log(f"    (T3) Lipschitz global:  L_observed = {L_observed_global:.4f}")
log(f"    (T3) Lipschitz near root: L_observed_near = {L_observed_near:.4f}")
log(f"    (T4) Root diagnostic:   X* = {X_star_full:.6f}")
log(f"                             Phi(X*) = {Phi(X_star_full):.6f}")
log(f"    (T5) Yukawa-Landau:     X_pole ~ {X_pole:.3f} (extension scan)")
log()
log(f"  This supports the bounded finite-grid diagnostic for the BC-transfer map.")
log(f"  It does NOT prove continuum uniqueness or close YT_BOUNDARY_THEOREM.md.")
log()
log(f"  Does NOT touch:")
log(f"    - parent claim (i)  domain separation        (interpretive)")
log(f"    - parent claim (iii) Ward-identity domain     (interpretive)")
log(f"    - parent claim (v)  non-perturbative bridge  (interpretive)")
log()

elapsed = time.time() - t0
log(f"  Elapsed: {elapsed:.1f}s")
log()

log(f"  Counts: {COUNTS['PASS']} PASS, {COUNTS['FAIL']} FAIL")
log()
if COUNTS["FAIL"] > 0:
    log(f"  *** {COUNTS['FAIL']} FAILURES ***")
    sys.exit(1)
else:
    log(f"  All {COUNTS['PASS']} checks passed.")
    sys.exit(0)
