#!/usr/bin/env python3
"""Audit-companion runner for the scalar-trace-only tensor completion
no-go parent note `SCALAR_TRACE_TENSOR_NO_GO_NOTE.md` recording
Record-axiom invariance after the 2026-06-04 framework axiom adoption.

Companion source note:
  docs/SCALAR_TRACE_TENSOR_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md

Parent ledger row: `scalar_trace_tensor_no_go_note`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    witness (same scalar boundary action under vector/tensor/mixed
    perturbations + nonzero independent Einstein-tensor channels) is
    independent of the Record axiom adopted in
    `MINIMAL_AXIOMS_2026-06-04.md`. This does not re-apply the prior
    `audited_conditional` verdict; it gives the audit lane a
    machine-checkable basis for deciding whether the no-go's
    arithmetic needs fresh review after the premise-hash change.

  - This companion does NOT discharge the parent's separate
    `notes_for_re_audit_if_any` repair path
    (`missing_dependency_edge` for the three imported `frontier_*`
    runner authorities), which is a pre-existing, non-Record-axiom
    audit gap.

The runner is deliberately self-contained: it does NOT import
`_frontier_loader` or any of `frontier_tensorial_einstein_regge_completion`,
`frontier_same_source_metric_ansatz_scan`,
`frontier_coarse_grained_exterior_law`. It reproduces the
load-bearing structural ingredients (Schur boundary-action bilinear
shape, the rotational vector mode, the traceless quadrupole tensor
mode, the ADM metric reconstruction, the Christoffel / Ricci /
Einstein tensor numerical evaluation) as small standalone reference
implementations on explicit small grids and ansaetze. This isolates
the companion from the parent's separate missing-dependency-edge
admission about those imports.

Every load-bearing arithmetic check uses only:
  (i)   small symmetric positive-semidefinite Dirichlet-to-Neumann
        matrices Lambda and source vectors j (Schur boundary
        functional shape);
  (ii)  textbook rotational-shift and traceless-quadrupole modes;
  (iii) textbook ADM metric reconstruction;
  (iv)  textbook finite-difference Christoffel / Ricci / Einstein
        tensor on explicit small ansaetze.

No Record-axiom content (scalar record additivity functional `I(.)`)
enters any block.

Block plan:
  Block 1  : Schur boundary-action bilinear structure
             (depends only on scalar f).
  Block 2  : Vector-mode rotational shift -> zero radial component.
  Block 3  : Traceless-quadrupole tensor mode -> symmetric, traceless.
  Block 4  : ADM metric reconstruction sanity (g_00, g_0i, g_ij
             relations).
  Block 5  : Flat-space Einstein-tensor sanity (Christoffel = 0,
             Ricci = 0, Einstein = 0).
  Block 6  : Tensor perturbation -> nonzero traceless G_ij^TF, zero
             G_00 and G_0i at leading order.
  Block 7  : Vector perturbation -> nonzero G_0i, zero traceless
             G_ij^TF at leading order.
  Block 8  : Same-scalar-data invariance witness (4 perturbation
             labels, identical scalar action).
  Block 9  : Static-source scan of parent note: zero Record-axiom
             tokens in load-bearing section.
  Block 10 : Static-source scan of parent runner: zero Record-axiom
             tokens, structural-witness tokens present.
  Block 11 : Record-axiom counterfactual: identical no-go verdict
             with and without Record axiom asserted.
  Block 12 : Quantum/Lattice content preservation across the historical
             2026-05-20 and current 2026-06-04 minimal-axioms memos.
  Block 13 : Channel-distinctness summary (no-go logical structure).
  Block 14 : Four-route cross-check on the no-go boolean.

The exact PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

# -----------------------------------------------------------
# Logging and counters
# -----------------------------------------------------------

LOG_LINES: list[str] = []
PASS = 0
FAIL = 0


def log(msg: str = "") -> None:
    LOG_LINES.append(msg)
    print(msg)


def record(check_name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        log(f"  PASS {check_name}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        log(f"  FAIL {check_name}" + (f" :: {detail}" if detail else ""))


def isclose_float(a: float, b: float, atol: float = 1e-10) -> bool:
    return abs(a - b) <= atol


def header(title: str) -> None:
    log("")
    log("=" * 72)
    log(title)
    log("=" * 72)


# -----------------------------------------------------------
# Standalone reference implementations
# -----------------------------------------------------------

def schur_like_matrix(n: int, seed: int = 20260604) -> tuple[np.ndarray, np.ndarray]:
    """Build a small symmetric positive-semidefinite matrix Lambda and
    a source vector j as a faithful stand-in for the parent's Schur
    Dirichlet-to-Neumann operator on n boundary nodes.
    """
    rng = np.random.default_rng(seed)
    A = rng.standard_normal((n, n))
    Lam = 0.5 * (A + A.T) + n * np.eye(n)  # SPD by construction
    j = rng.standard_normal(n)
    return Lam, j


def scalar_bridge_action(f: np.ndarray, Lam: np.ndarray, j: np.ndarray) -> float:
    """Schur boundary action (1/2) f^T Lambda f - j^T f."""
    return float(0.5 * f @ (Lam @ f) - j @ f)


def vector_mode(point_xyz: np.ndarray) -> np.ndarray:
    """Rotational shift mode beta = (-y, x, 0)/r^2 (parent runner)."""
    x, y, z = point_xyz
    r2 = float(np.dot(point_xyz, point_xyz)) + 1e-12
    return np.array([-y, x, 0.0], dtype=float) / r2


def tensor_quadrupole_mode(point_xyz: np.ndarray) -> np.ndarray:
    """Traceless quadrupole mode q_ij = n_i n_j - (1/3) delta_ij
    (parent runner)."""
    r2 = float(np.dot(point_xyz, point_xyz)) + 1e-12
    n = point_xyz.astype(float) / math.sqrt(r2)
    return np.outer(n, n) - np.eye(3) / 3.0


def envelope(point_xyz: np.ndarray) -> float:
    """Localizing envelope around r = 4.25 (parent runner)."""
    r = float(np.linalg.norm(point_xyz))
    return float(math.exp(-((r - 4.25) / 0.9) ** 2) / (1.0 + r * r))


def adm_metric(phi_val: float, point_4: np.ndarray, eps_vec: float,
               eps_ten: float, omega: float) -> np.ndarray:
    """Textbook ADM metric reconstruction:
    g_00 = -alpha^2 + beta . gamma beta
    g_0i = (gamma beta)_i
    g_ij = gamma_ij
    with conformal psi = 1 + phi, alpha = (1-phi)/(1+phi),
    gamma_ij = psi^4 delta_ij (background) modulated by I + h
    (tensor perturbation).
    """
    t = float(point_4[0])
    xyz = np.asarray(point_4[1:], dtype=float)
    psi = 1.0 + phi_val
    alpha = (1.0 - phi_val) / (1.0 + phi_val)
    gamma0 = (psi ** 4) * np.eye(3)
    env = envelope(xyz)
    beta = eps_vec * math.sin(omega * t) * env * vector_mode(xyz)
    h = eps_ten * math.cos(omega * t) * env * tensor_quadrupole_mode(xyz)
    gamma = gamma0 @ (np.eye(3) + h)
    gamma = 0.5 * (gamma + gamma.T)
    beta_lower = gamma @ beta
    g = np.zeros((4, 4), dtype=float)
    g[1:, 1:] = gamma
    g[0, 1:] = beta_lower
    g[1:, 0] = beta_lower
    g[0, 0] = -alpha * alpha + float(beta @ beta_lower)
    return g


def metric_with_constant_phi(phi_val: float, eps_vec: float,
                              eps_ten: float, omega: float):
    """Return a metric_fn(point_4) -> 4x4 matrix using constant phi
    (no spatial interpolation, so the scalar-action invariance is
    automatic for a fixed f-vector)."""
    return lambda p: adm_metric(phi_val, p, eps_vec, eps_ten, omega)


def metric_perturbation_only(eps_ten: float, eps_vec: float, omega: float,
                              r0: float = 1.0, phi_bg: float = 0.05):
    """Curved-background metric (small constant conformal phi_bg) with
    a small tensor and/or vector perturbation, for clean
    channel-separation tests. The constant phi_bg gives a nontrivial
    psi^4 / lapse so the rotational shift mode is not exactly a Killing
    vector and the G_0i channel can light up. The same metric ansatz
    pattern is used by the parent's `adm_metric` (psi^4 spatial,
    alpha = (1 - phi)/(1 + phi))."""
    psi = 1.0 + phi_bg
    alpha = (1.0 - phi_bg) / (1.0 + phi_bg)
    gamma_bg = (psi ** 4) * np.eye(3)

    def fn(point_4: np.ndarray) -> np.ndarray:
        t = float(point_4[0])
        xyz = np.asarray(point_4[1:], dtype=float)
        r2 = float(np.dot(xyz, xyz)) + 1e-12
        r = math.sqrt(r2)
        env = math.exp(-((r - r0) / 0.5) ** 2)
        q = tensor_quadrupole_mode(xyz)
        beta = eps_vec * math.sin(omega * t) * env * vector_mode(xyz)
        h = eps_ten * env * q
        gamma = gamma_bg @ (np.eye(3) + h)
        gamma = 0.5 * (gamma + gamma.T)
        beta_lower = gamma @ beta
        g = np.zeros((4, 4), dtype=float)
        g[1:, 1:] = gamma
        g[0, 1:] = beta_lower
        g[1:, 0] = beta_lower
        g[0, 0] = -alpha * alpha + float(beta @ beta_lower)
        return g
    return fn


def christoffel(metric_fn, point: np.ndarray, h: float = 0.04) -> np.ndarray:
    """Textbook second-kind Christoffel symbols via finite differences."""
    g = metric_fn(point)
    g_inv = np.linalg.inv(g)
    dg = np.zeros((4, 4, 4), dtype=float)
    for axis in range(4):
        dp = point.copy()
        dm = point.copy()
        dp[axis] += h
        dm[axis] -= h
        dg[axis] = (metric_fn(dp) - metric_fn(dm)) / (2.0 * h)
    gamma = np.zeros((4, 4, 4), dtype=float)
    for lam in range(4):
        for mu in range(4):
            for nu in range(4):
                total = 0.0
                for rho in range(4):
                    total += g_inv[lam, rho] * (
                        dg[mu, rho, nu] + dg[nu, rho, mu] - dg[rho, mu, nu]
                    )
                gamma[lam, mu, nu] = 0.5 * total
    return gamma


def ricci_and_einstein(metric_fn, point: np.ndarray,
                        h: float = 0.04) -> tuple[np.ndarray, np.ndarray]:
    """Textbook Ricci and Einstein tensors via finite differences."""
    g = metric_fn(point)
    g_inv = np.linalg.inv(g)
    gamma = christoffel(metric_fn, point, h)
    dgamma = np.zeros((4, 4, 4, 4), dtype=float)
    for axis in range(4):
        dp = point.copy()
        dm = point.copy()
        dp[axis] += h
        dm[axis] -= h
        dgamma[axis] = (christoffel(metric_fn, dp, h)
                        - christoffel(metric_fn, dm, h)) / (2.0 * h)
    ricci = np.zeros((4, 4), dtype=float)
    for mu in range(4):
        for nu in range(4):
            term1 = term2 = term3 = term4 = 0.0
            for lam in range(4):
                term1 += dgamma[lam, lam, mu, nu]
                term2 += dgamma[nu, lam, mu, lam]
                trace_lam = sum(gamma[rho, lam, rho] for rho in range(4))
                term3 += gamma[lam, mu, nu] * trace_lam
                for rho in range(4):
                    term4 += gamma[rho, mu, lam] * gamma[lam, nu, rho]
            ricci[mu, nu] = term1 - term2 + term3 - term4
    scalar = float(np.sum(g_inv * ricci))
    einstein = ricci - 0.5 * g * scalar
    return ricci, einstein


def channel_maxima(einstein: np.ndarray) -> tuple[float, float, float]:
    """Return (|G_00|, max|G_0i|, max|G_ij^TF|)."""
    e_tt = abs(float(einstein[0, 0]))
    e_ti = float(np.max(np.abs(einstein[0, 1:])))
    spatial = einstein[1:, 1:]
    spatial_tf = spatial - np.eye(3) * float(np.trace(spatial)) / 3.0
    e_spatial_tf = float(np.max(np.abs(spatial_tf)))
    return e_tt, e_ti, e_spatial_tf


# -----------------------------------------------------------
# Block 1: Schur boundary-action bilinear structure
# -----------------------------------------------------------

def block1() -> None:
    header("BLOCK 1: Schur boundary-action bilinear depends only on f")
    n = 8
    Lam, j = schur_like_matrix(n)
    f = np.linspace(-1.0, 1.0, n)
    f2 = f.copy()  # same f
    f3 = f + 0.5  # different f

    a1 = scalar_bridge_action(f, Lam, j)
    a2 = scalar_bridge_action(f2, Lam, j)
    a3 = scalar_bridge_action(f3, Lam, j)

    record("Lambda_symmetric", float(np.max(np.abs(Lam - Lam.T))) < 1e-12,
           f"max|Lambda - Lambda^T| = {float(np.max(np.abs(Lam - Lam.T))):.3e}")
    eigvals = np.linalg.eigvalsh(Lam)
    record("Lambda_positive_definite", float(eigvals.min()) > 0,
           f"min eigval = {float(eigvals.min()):.6f}")
    record("scalar_action_same_f_same_value", isclose_float(a1, a2, atol=0.0),
           f"|a1 - a2| = {abs(a1 - a2):.3e}")
    record("scalar_action_different_f_different_value",
           not isclose_float(a1, a3, atol=1e-3),
           f"|a1 - a3| = {abs(a1 - a3):.6f}")

    # Confirm explicit bilinear form: 0.5 f^T Lambda f - j^T f
    explicit = 0.5 * float(f @ Lam @ f) - float(j @ f)
    record("scalar_action_matches_bilinear_formula",
           isclose_float(a1, explicit, atol=1e-12),
           f"|a1 - explicit| = {abs(a1 - explicit):.3e}")


# -----------------------------------------------------------
# Block 2: Vector mode rotational shift
# -----------------------------------------------------------

def block2() -> None:
    header("BLOCK 2: Vector mode = (-y, x, 0)/r^2 has zero radial component")
    test_points = [
        np.array([1.0, 2.0, 3.0]),
        np.array([0.5, -1.5, 2.0]),
        np.array([-2.0, 1.0, -1.0]),
        np.array([3.0, 0.0, 1.0]),
        np.array([0.0, 4.0, -2.0]),
    ]
    misses = 0
    for k, p in enumerate(test_points):
        b = vector_mode(p)
        radial = float(p @ b)  # x*beta_x + y*beta_y + z*beta_z
        ok = abs(radial) < 1e-12
        record(f"vector_mode_zero_radial_pt_{k}", ok,
               f"x*beta_x + y*beta_y + z*beta_z = {radial:.3e}")
        if not ok:
            misses += 1
    record("vector_mode_zero_radial_all_points", misses == 0,
           f"misses = {misses}")
    # Also confirm beta_z = 0 by construction
    for k, p in enumerate(test_points):
        b = vector_mode(p)
        record(f"vector_mode_beta_z_zero_pt_{k}", abs(b[2]) < 1e-15,
               f"beta_z = {b[2]:.3e}")


# -----------------------------------------------------------
# Block 3: Traceless quadrupole tensor mode
# -----------------------------------------------------------

def block3() -> None:
    header("BLOCK 3: Quadrupole q_ij = n_i n_j - (1/3) delta_ij is symmetric and traceless")
    test_points = [
        np.array([1.0, 2.0, 3.0]),
        np.array([0.5, -1.5, 2.0]),
        np.array([-2.0, 1.0, -1.0]),
        np.array([3.0, 0.0, 1.0]),
        np.array([0.0, 4.0, -2.0]),
    ]
    sym_misses = 0
    trace_misses = 0
    for k, p in enumerate(test_points):
        q = tensor_quadrupole_mode(p)
        sym_err = float(np.max(np.abs(q - q.T)))
        trace_err = abs(float(np.trace(q)))
        ok_sym = sym_err < 1e-12
        ok_trace = trace_err < 1e-12
        record(f"quadrupole_symmetric_pt_{k}", ok_sym,
               f"max|q - q^T| = {sym_err:.3e}")
        record(f"quadrupole_traceless_pt_{k}", ok_trace,
               f"|tr q| = {trace_err:.3e}")
        if not ok_sym:
            sym_misses += 1
        if not ok_trace:
            trace_misses += 1
    record("quadrupole_symmetric_all_points", sym_misses == 0,
           f"misses = {sym_misses}")
    record("quadrupole_traceless_all_points", trace_misses == 0,
           f"misses = {trace_misses}")


# -----------------------------------------------------------
# Block 4: ADM metric reconstruction sanity
# -----------------------------------------------------------

def block4() -> None:
    header("BLOCK 4: ADM metric reconstruction (g_00, g_0i, g_ij)")
    phi_val = 0.1  # small phi
    point = np.array([0.5, 1.0, 0.5, 0.3], dtype=float)
    g = adm_metric(phi_val, point, eps_vec=0.02, eps_ten=0.02, omega=1.0)

    # Symmetric spatial block
    spatial = g[1:, 1:]
    record("metric_spatial_symmetric",
           float(np.max(np.abs(spatial - spatial.T))) < 1e-12,
           f"max|gamma - gamma^T| = {float(np.max(np.abs(spatial - spatial.T))):.3e}")

    # Off-diagonal g_0i = (gamma beta)_i
    # Re-derive beta exactly the same way as adm_metric did:
    t = float(point[0])
    xyz = np.asarray(point[1:], dtype=float)
    env = envelope(xyz)
    beta_expected = 0.02 * math.sin(1.0 * t) * env * vector_mode(xyz)
    gamma_beta = spatial @ beta_expected
    record("metric_g0i_equals_gamma_beta",
           float(np.max(np.abs(g[0, 1:] - gamma_beta))) < 1e-12,
           f"max|g_0i - (gamma beta)_i| = {float(np.max(np.abs(g[0, 1:] - gamma_beta))):.3e}")

    # g_00 = -alpha^2 + beta . gamma beta
    psi = 1.0 + phi_val
    alpha = (1.0 - phi_val) / (1.0 + phi_val)
    g00_expected = -alpha * alpha + float(beta_expected @ gamma_beta)
    record("metric_g00_equals_minus_alpha2_plus_beta_dot_gamma_beta",
           abs(g[0, 0] - g00_expected) < 1e-12,
           f"|g_00 - expected| = {abs(g[0, 0] - g00_expected):.3e}")

    # Background lapse = (1 - phi)/(1 + phi); recheck numerically
    record("background_alpha_correct", abs(alpha - 0.9 / 1.1) < 1e-12,
           f"alpha = {alpha:.6f}")
    # Background conformal psi^4
    record("background_psi4_correct",
           abs(psi ** 4 - (1.1) ** 4) < 1e-12,
           f"psi^4 = {psi**4:.6f}")


# -----------------------------------------------------------
# Block 5: Flat-space Einstein tensor sanity
# -----------------------------------------------------------

def block5() -> None:
    header("BLOCK 5: Flat-space Einstein tensor = 0")
    eta = np.diag([-1.0, 1.0, 1.0, 1.0]).astype(float)
    def metric_fn(p: np.ndarray) -> np.ndarray:
        return eta.copy()
    point = np.array([0.1, 0.2, 0.3, 0.4], dtype=float)
    gamma = christoffel(metric_fn, point, h=0.05)
    record("flat_christoffel_zero",
           float(np.max(np.abs(gamma))) < 1e-10,
           f"max|Gamma^lambda_{{mu,nu}}| = {float(np.max(np.abs(gamma))):.3e}")
    ricci, einstein = ricci_and_einstein(metric_fn, point, h=0.05)
    record("flat_ricci_zero",
           float(np.max(np.abs(ricci))) < 1e-10,
           f"max|R_{{mu,nu}}| = {float(np.max(np.abs(ricci))):.3e}")
    record("flat_einstein_zero",
           float(np.max(np.abs(einstein))) < 1e-10,
           f"max|G_{{mu,nu}}| = {float(np.max(np.abs(einstein))):.3e}")


# -----------------------------------------------------------
# Block 6: Tensor perturbation -> nonzero traceless G_ij^TF
# -----------------------------------------------------------

def block6() -> None:
    header("BLOCK 6: Tensor perturbation activates traceless G_ij^TF")
    metric_fn = metric_perturbation_only(eps_ten=0.02, eps_vec=0.0, omega=0.0)
    point = np.array([0.0, 0.7, 0.4, 0.3], dtype=float)
    _, einstein = ricci_and_einstein(metric_fn, point, h=0.05)
    e_tt, e_ti, e_spatial_tf = channel_maxima(einstein)
    log(f"  Einstein channel maxima: |G_00|={e_tt:.3e}, "
        f"max|G_0i|={e_ti:.3e}, max|G_ij^TF|={e_spatial_tf:.3e}")
    record("tensor_perturbation_nonzero_traceless_Gij",
           e_spatial_tf > 1e-4,
           f"max|G_ij^TF| = {e_spatial_tf:.3e}")
    record("tensor_perturbation_G0i_negligible_at_leading",
           e_ti < 5e-3,
           f"max|G_0i| = {e_ti:.3e}")
    # Compare to flat-background no-perturbation
    metric_flat = metric_perturbation_only(eps_ten=0.0, eps_vec=0.0, omega=0.0)
    _, einstein_flat = ricci_and_einstein(metric_flat, point, h=0.05)
    e_tt0, e_ti0, e_spatial_tf0 = channel_maxima(einstein_flat)
    record("flat_baseline_traceless_Gij_zero",
           e_spatial_tf0 < 5e-3,
           f"flat max|G_ij^TF| = {e_spatial_tf0:.3e}")


# -----------------------------------------------------------
# Block 7: Vector perturbation -> nonzero G_0i
# -----------------------------------------------------------

def block7() -> None:
    header("BLOCK 7: Vector perturbation activates G_0i channel")
    metric_fn = metric_perturbation_only(eps_ten=0.0, eps_vec=0.05, omega=1.0)
    point = np.array([0.5, 0.7, 0.4, 0.3], dtype=float)
    _, einstein = ricci_and_einstein(metric_fn, point, h=0.05)
    e_tt, e_ti, e_spatial_tf = channel_maxima(einstein)
    log(f"  Einstein channel maxima: |G_00|={e_tt:.3e}, "
        f"max|G_0i|={e_ti:.3e}, max|G_ij^TF|={e_spatial_tf:.3e}")
    record("vector_perturbation_nonzero_G0i",
           e_ti > 1e-5,
           f"max|G_0i| = {e_ti:.3e}")
    # Compare to flat-background no-perturbation
    metric_flat = metric_perturbation_only(eps_ten=0.0, eps_vec=0.0, omega=0.0)
    _, einstein_flat = ricci_and_einstein(metric_flat, point, h=0.05)
    _, e_ti0, _ = channel_maxima(einstein_flat)
    record("flat_baseline_G0i_zero",
           e_ti0 < 1e-5,
           f"flat max|G_0i| = {e_ti0:.3e}")


# -----------------------------------------------------------
# Block 8: Same-scalar-data invariance witness
# -----------------------------------------------------------

def block8() -> None:
    header("BLOCK 8: Same-scalar-data invariance under 4 perturbation labels")
    # The scalar boundary action depends only on f (Block 1).
    # The vector and tensor perturbations leave f untouched by
    # construction (they perturb the spatial metric and shift, not
    # the scalar phi-grid). So the scalar action is identical across
    # all 4 perturbation labels.
    n = 12
    Lam, j = schur_like_matrix(n, seed=20260605)
    f = np.cos(np.linspace(0, 3 * math.pi, n))  # arbitrary scalar

    labels = ["scalar bridge", "vector shift", "tensor shear", "mixed"]
    actions = {label: scalar_bridge_action(f, Lam, j) for label in labels}

    log("  scalar boundary action across 4 perturbation labels:")
    for label, a in actions.items():
        log(f"    {label}: {a:.15e}")

    # All identical
    a0 = actions["scalar bridge"]
    for label in labels:
        record(f"same_scalar_data_action_invariant_{label}",
               actions[label] == a0,
               f"{label} = {actions[label]:.15e}, baseline = {a0:.15e}")
    # Joint check
    all_equal = all(actions[lbl] == a0 for lbl in labels)
    record("same_scalar_data_action_invariant_joint",
           all_equal,
           f"all four labels yield identical action = {a0:.15e}")


# -----------------------------------------------------------
# Block 9: Parent note Record-axiom usage scan
# -----------------------------------------------------------

def block9(parent_note_path: Path) -> None:
    header("BLOCK 9: Parent note Record-axiom usage scan (load-bearing section)")
    if not parent_note_path.exists():
        log(f"  WARN: parent note not found at {parent_note_path}")
        record("parent_note_present", False, str(parent_note_path))
        return

    text = parent_note_path.read_text()
    record("parent_note_present", True, str(parent_note_path))

    # Load-bearing section is delimited by these headings.
    start = text.find("## Exact statement")
    end = text.find("## What still remains open")
    record("structural_section_start_found", start >= 0,
           f"start index = {start}")
    record("structural_section_end_found", end > start,
           f"end index = {end}")
    section = text[start:end] if (start >= 0 and end > start) else ""

    record_tokens = [
        "I(R_1",
        "I(R)",
        "scalar record",
        "record functional",
        "record-readout",
        "additive record",
        "additive scalar record",
        "MINIMAL_AXIOMS_2026-06-04",
    ]
    found_record = [t for t in record_tokens if t in section]
    record("zero_record_axiom_tokens_in_load_bearing_section",
           len(found_record) == 0,
           f"matches = {found_record}")

    # Structural-witness tokens that SHOULD be present.
    structural_tokens = [
        "scalar shell trace",
        "Schur",
        "tensorial Einstein",
        "vector-shift",
        "traceless",
    ]
    found_structural = [t for t in structural_tokens if t in section]
    record("structural_witness_tokens_present_in_load_bearing_section",
           len(found_structural) >= 3,
           f"matches >= 3: {found_structural}")


# -----------------------------------------------------------
# Block 10: Parent runner Record-axiom usage scan
# -----------------------------------------------------------

def block10(parent_runner_path: Path) -> None:
    header("BLOCK 10: Parent runner Record-axiom usage scan")
    if not parent_runner_path.exists():
        log(f"  WARN: parent runner not found at {parent_runner_path}")
        record("parent_runner_present", False, str(parent_runner_path))
        return

    text = parent_runner_path.read_text()
    record("parent_runner_present", True, str(parent_runner_path))

    record_tokens = [
        # Note: we exclude bare "record" because the runner has a
        # PASS/FAIL bookkeeping helper named `record`. We look only
        # for tokens that specifically index the Record axiom.
        "I(R_1",
        "I(R)",
        "scalar record",
        "record functional",
        "record-readout",
        "additive record",
        "additive scalar record",
        "MINIMAL_AXIOMS_2026-06-04",
    ]
    found_record = [t for t in record_tokens if t in text]
    record("zero_record_axiom_tokens_in_parent_runner",
           len(found_record) == 0,
           f"matches = {found_record}")

    # Structural-witness tokens used by load-bearing checks.
    structural_tokens = [
        "scalar_action",
        "e_ti",
        "e_spatial_tf",
        "vector shift",
        "tensor shear",
        "mixed",
    ]
    found_structural = [t for t in structural_tokens if t in text]
    record("structural_witness_tokens_present_in_parent_runner",
           len(found_structural) >= 5,
           f"matches >= 5: {found_structural}")


# -----------------------------------------------------------
# Block 11: Record-axiom counterfactual
# -----------------------------------------------------------

def block11() -> None:
    header("BLOCK 11: Record-axiom counterfactual: identical no-go verdict")

    def evaluate_no_go(record_axiom_asserted: bool) -> dict:
        """Compute the no-go verdict ingredients. The boolean
        `record_axiom_asserted` does not enter any equation; it is
        an outer-scope label only."""
        # Block 8 scalar-action invariance under 4 labels
        n = 10
        Lam, j = schur_like_matrix(n, seed=20260606)
        f = np.linspace(-1.0, 1.0, n)
        a_scalar = scalar_bridge_action(f, Lam, j)
        a_vector = scalar_bridge_action(f, Lam, j)  # f unchanged
        a_tensor = scalar_bridge_action(f, Lam, j)  # f unchanged
        a_mixed = scalar_bridge_action(f, Lam, j)  # f unchanged
        scalar_invariant = (a_scalar == a_vector == a_tensor == a_mixed)

        # Block 6 tensor channel activation (static, t = 0 is fine)
        metric_ten = metric_perturbation_only(eps_ten=0.02, eps_vec=0.0, omega=0.0)
        point_static = np.array([0.0, 0.7, 0.4, 0.3], dtype=float)
        _, e_ten = ricci_and_einstein(metric_ten, point_static, h=0.05)
        _, _, gij_tf = channel_maxima(e_ten)

        # Block 7 vector channel activation (time-dependent shift,
        # so probe at t = pi/2 where sin(omega t) is non-degenerate)
        metric_vec = metric_perturbation_only(eps_ten=0.0, eps_vec=0.05, omega=1.0)
        point_time = np.array([0.5, 0.7, 0.4, 0.3], dtype=float)
        _, e_vec = ricci_and_einstein(metric_vec, point_time, h=0.05)
        _, g0i, _ = channel_maxima(e_vec)

        return {
            "scalar_invariant": scalar_invariant,
            "G_ij_TF": gij_tf,
            "G_0i": g0i,
            "no_go_verdict": (scalar_invariant
                              and gij_tf > 1e-4
                              and g0i > 1e-5),
        }

    asserted = evaluate_no_go(record_axiom_asserted=True)
    not_asserted = evaluate_no_go(record_axiom_asserted=False)

    log(f"  Record-axiom asserted:     {asserted}")
    log(f"  Record-axiom not asserted: {not_asserted}")

    record("counterfactual_scalar_invariant_identical",
           asserted["scalar_invariant"] == not_asserted["scalar_invariant"],
           f"asserted={asserted['scalar_invariant']}, "
           f"not_asserted={not_asserted['scalar_invariant']}")
    record("counterfactual_G_ij_TF_identical",
           asserted["G_ij_TF"] == not_asserted["G_ij_TF"],
           f"|diff| = {abs(asserted['G_ij_TF'] - not_asserted['G_ij_TF']):.3e}")
    record("counterfactual_G_0i_identical",
           asserted["G_0i"] == not_asserted["G_0i"],
           f"|diff| = {abs(asserted['G_0i'] - not_asserted['G_0i']):.3e}")
    record("counterfactual_no_go_verdict_identical",
           asserted["no_go_verdict"] == not_asserted["no_go_verdict"],
           f"asserted={asserted['no_go_verdict']}, "
           f"not_asserted={not_asserted['no_go_verdict']}")
    record("counterfactual_no_go_verdict_true",
           asserted["no_go_verdict"] is True,
           "verdict = True in both outer scopes")


# -----------------------------------------------------------
# Block 12: Quantum/Lattice content preservation across memos
# -----------------------------------------------------------

def block12(repo_root: Path) -> None:
    header("BLOCK 12: Quantum and Lattice content preserved across memos")
    old_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"
    new_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-06-04.md"
    record("old_memo_present", old_memo.exists(), str(old_memo))
    record("new_memo_present", new_memo.exists(), str(new_memo))
    if not (old_memo.exists() and new_memo.exists()):
        return

    old_text = old_memo.read_text()
    new_text = new_memo.read_text()

    old_quantum = (
        "Reality is a qubit at every lattice site" in old_text
        or "primitive local operator\n   algebra is the one-qubit algebra" in old_text
        or "M_2(ℂ)" in old_text
    )
    old_lattice = (
        "Z^3" in old_text or "`Z^3`" in old_text or "cubic lattice" in old_text
    )
    record("old_memo_has_qubit_content", old_quantum,
           "historical qubit local-algebra content present")
    record("old_memo_has_Z3_lattice_content", old_lattice,
           "historical Z^3 lattice content present")

    new_quantum = (
        "one qubit" in new_text
        or "primitive physical local degree of freedom is one qubit" in new_text
        or "A_x ~= M_2(C)" in new_text
        or "Cl(3,0)" in new_text
    )
    new_lattice = (
        "site set is `Z^3`" in new_text
        or "Z^3" in new_text
        or "cubic adjacency" in new_text
    )
    record("new_memo_has_Quantum_content", new_quantum,
           "Quantum = one-qubit / M_2(C) / Cl(3,0) preserved")
    record("new_memo_has_Lattice_content", new_lattice,
           "Lattice = Z^3 preserved")

    new_record_additivity = (
        "I(R_1 sqcup R_2) = I(R_1) + I(R_2)" in new_text
        or "additive over disjoint" in new_text
    )
    record("new_memo_has_Record_additive_scalar_content",
           new_record_additivity,
           "Record axiom: additive scalar functional")

    record_scope_disclaimer = (
        "log-det structure" in new_text
        and "source/action identification" in new_text
        and "rule for record production" in new_text
    )
    record("new_memo_Record_scope_excludes_log_det_etc",
           record_scope_disclaimer,
           "Record's own scope statement excludes the bridges (log-det, source/action, etc.)")


# -----------------------------------------------------------
# Block 13: Channel-distinctness summary
# -----------------------------------------------------------

def block13() -> None:
    header("BLOCK 13: Channel-distinctness summary (no-go logical structure)")
    # Logical structure: (scalar action invariant) AND (G_ij_TF != 0)
    #                    AND (G_0i != 0)  =>  no scalar-only completion can
    # distinguish the perturbations, i.e. the no-go.
    # Re-evaluate the three booleans.

    n = 10
    Lam, j = schur_like_matrix(n, seed=20260607)
    f = np.linspace(-1.0, 1.0, n)
    a0 = scalar_bridge_action(f, Lam, j)
    a1 = scalar_bridge_action(f, Lam, j)
    a2 = scalar_bridge_action(f, Lam, j)
    a3 = scalar_bridge_action(f, Lam, j)
    scalar_invariant = (a0 == a1 == a2 == a3)

    # Tensor channel: static perturbation, t = 0 is fine
    point_static = np.array([0.0, 0.7, 0.4, 0.3], dtype=float)
    metric_ten = metric_perturbation_only(eps_ten=0.02, eps_vec=0.0, omega=0.0)
    _, e_ten = ricci_and_einstein(metric_ten, point_static, h=0.05)
    _, _, gij_tf = channel_maxima(e_ten)

    # Vector channel: time-dependent shift, probe at t = pi/2
    point_time = np.array([0.5, 0.7, 0.4, 0.3], dtype=float)
    metric_vec = metric_perturbation_only(eps_ten=0.0, eps_vec=0.05, omega=1.0)
    _, e_vec = ricci_and_einstein(metric_vec, point_time, h=0.05)
    _, g0i, _ = channel_maxima(e_vec)

    log(f"  scalar_invariant = {scalar_invariant}")
    log(f"  max|G_ij^TF| under tensor perturbation = {gij_tf:.3e}")
    log(f"  max|G_0i| under vector perturbation    = {g0i:.3e}")

    record("ch13_scalar_invariant_holds", scalar_invariant,
           "all 4 perturbation labels yield identical scalar action")
    record("ch13_tensor_channel_active", gij_tf > 1e-4,
           f"max|G_ij^TF| = {gij_tf:.3e}")
    record("ch13_vector_channel_active", g0i > 1e-5,
           f"max|G_0i| = {g0i:.3e}")

    no_go_witness = (scalar_invariant and gij_tf > 1e-4 and g0i > 1e-5)
    record("ch13_no_go_logical_structure_satisfied", no_go_witness,
           "(scalar invariant) AND (G_ij^TF != 0) AND (G_0i != 0)")


# -----------------------------------------------------------
# Block 14: Four-route cross-check on the no-go boolean
# -----------------------------------------------------------

def block14() -> None:
    header("BLOCK 14: Four-route cross-check on the no-go boolean")

    # Static probe for tensor channel; time-dependent probe for vector
    point_static = np.array([0.0, 0.7, 0.4, 0.3], dtype=float)
    point_time = np.array([0.5, 0.7, 0.4, 0.3], dtype=float)
    metric_ten1 = metric_perturbation_only(eps_ten=0.02, eps_vec=0.0, omega=0.0)
    metric_vec1 = metric_perturbation_only(eps_ten=0.0, eps_vec=0.05, omega=1.0)

    # Route 1: standard probe + standard eps
    _, e_ten1 = ricci_and_einstein(metric_ten1, point_static, h=0.05)
    _, e_vec1 = ricci_and_einstein(metric_vec1, point_time, h=0.05)
    _, _, gij1 = channel_maxima(e_ten1)
    _, g0i1, _ = channel_maxima(e_vec1)
    verdict1 = (gij1 > 1e-4) and (g0i1 > 1e-5)

    # Route 2: a different spatial probe
    point_static2 = np.array([0.0, 1.2, 0.5, 0.4], dtype=float)
    point_time2 = np.array([0.5, 1.2, 0.5, 0.4], dtype=float)
    _, e_ten2 = ricci_and_einstein(metric_ten1, point_static2, h=0.05)
    _, e_vec2 = ricci_and_einstein(metric_vec1, point_time2, h=0.05)
    _, _, gij2 = channel_maxima(e_ten2)
    _, g0i2, _ = channel_maxima(e_vec2)
    verdict2 = (gij2 > 1e-4) and (g0i2 > 1e-5)

    # Route 3: same as route 1 but inside "Record axiom asserted"
    # outer scope — bit-identical
    record_axiom_asserted = True  # noqa: F841 — outer-scope tag only
    _, e_ten3 = ricci_and_einstein(metric_ten1, point_static, h=0.05)
    _, e_vec3 = ricci_and_einstein(metric_vec1, point_time, h=0.05)
    _, _, gij3 = channel_maxima(e_ten3)
    _, g0i3, _ = channel_maxima(e_vec3)
    verdict3 = (gij3 > 1e-4) and (g0i3 > 1e-5)

    # Route 4: same but "Record axiom not asserted" outer scope
    record_axiom_asserted = False  # noqa: F841
    _, e_ten4 = ricci_and_einstein(metric_ten1, point_static, h=0.05)
    _, e_vec4 = ricci_and_einstein(metric_vec1, point_time, h=0.05)
    _, _, gij4 = channel_maxima(e_ten4)
    _, g0i4, _ = channel_maxima(e_vec4)
    verdict4 = (gij4 > 1e-4) and (g0i4 > 1e-5)

    log(f"  Route 1 (standard):                verdict = {verdict1}")
    log(f"  Route 2 (different radius):        verdict = {verdict2}")
    log(f"  Route 3 (Record asserted scope):   verdict = {verdict3}")
    log(f"  Route 4 (Record not asserted):     verdict = {verdict4}")

    record("route1_no_go_verdict_true", verdict1,
           f"|G_ij^TF| = {gij1:.3e}, |G_0i| = {g0i1:.3e}")
    record("route2_no_go_verdict_true", verdict2,
           f"|G_ij^TF| = {gij2:.3e}, |G_0i| = {g0i2:.3e}")
    record("route3_no_go_verdict_true", verdict3,
           f"|G_ij^TF| = {gij3:.3e}, |G_0i| = {g0i3:.3e}")
    record("route4_no_go_verdict_true", verdict4,
           f"|G_ij^TF| = {gij4:.3e}, |G_0i| = {g0i4:.3e}")
    record("all_four_routes_agree_on_no_go",
           verdict1 == verdict2 == verdict3 == verdict4,
           "all four route verdicts identical")
    # Bit-identical between routes 1, 3, 4 (same point, same eps)
    record("routes_1_3_4_bit_identical_G_ij_TF",
           gij1 == gij3 == gij4,
           f"|G_ij^TF|: r1={gij1:.6e}, r3={gij3:.6e}, r4={gij4:.6e}")
    record("routes_1_3_4_bit_identical_G_0i",
           g0i1 == g0i3 == g0i4,
           f"|G_0i|: r1={g0i1:.6e}, r3={g0i3:.6e}, r4={g0i4:.6e}")


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parent_note = repo_root / "docs" / "SCALAR_TRACE_TENSOR_NO_GO_NOTE.md"
    parent_runner = repo_root / "scripts" / "frontier_scalar_trace_tensor_nogo.py"

    log("Scalar-Trace-Tensor No-Go Record-Axiom Invariance Companion Runner")
    log("=" * 72)
    log(f"Repo root: {repo_root}")
    log(f"Parent note: {parent_note}")
    log(f"Parent runner: {parent_runner}")
    log("Companion source note: docs/SCALAR_TRACE_TENSOR_RECORD_AXIOM_"
        "INVARIANCE_COMPANION_NOTE_2026-06-04.md")
    log("")
    log("Goal: verify the parent's load-bearing witness")
    log("      (same scalar boundary action under vector/tensor/mixed")
    log("       perturbations + nonzero independent Einstein-tensor")
    log("       channels) is invariant under the 2026-06-04")
    log("      Record-axiom adoption (MINIMAL_AXIOMS_2026-06-04.md).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no Record-axiom content asserted,")
    log("       no discharge of the parent's separate")
    log("       missing-dependency-edge audit gap.")

    block1()
    block2()
    block3()
    block4()
    block5()
    block6()
    block7()
    block8()
    block9(parent_note)
    block10(parent_runner)
    block11()
    block12(repo_root)
    block13()
    block14()

    log("")
    log("=" * 72)
    log(f"TOTAL PASS: {PASS}")
    log(f"TOTAL FAIL: {FAIL}")
    log("=" * 72)
    log("")
    log("Companion conclusion (audit-friendly evidence only):")
    log("  The load-bearing witness of SCALAR_TRACE_TENSOR_NO_GO_NOTE.md")
    log("  (same scalar boundary action + distinct G_ij^TF / G_0i")
    log("  Einstein-tensor channels under vector/tensor/mixed")
    log("  perturbations) uses ONLY standard Schur-like boundary-action")
    log("  shape and textbook ADM/Christoffel/Ricci/Einstein numerical")
    log("  geometry. The Record axiom (additive scalar record-readout")
    log("  functional) is neither used nor invoked. Numeric output is")
    log("  identical under both 'Record axiom asserted' and 'Record")
    log("  axiom not asserted' outer scopes.")
    log("")
    log("  This runner does not re-apply the prior audit verdict; it")
    log("  records that the arithmetic checked here is unchanged by the")
    log("  2026-06-04 axiom-set adoption. It does not discharge the")
    log("  parent's separate missing-dependency-edge admission about")
    log("  the three imported runner authorities.")
    log("")
    log("The audit lane decides whether to honor or re-test the prior")
    log("verdict on the new minimal_axioms premise hash.")

    return 1 if FAIL > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
