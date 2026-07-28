#!/usr/bin/env python3
"""Bounded diagnostics for the finite-size ``beta`` caveat in
``SELF_CONSISTENCY_FORCES_POISSON_NOTE.md``.

The parent note's first caveat reads:

  "**Finite-size beta**: The measured beta ~ 1.28 exceeds the target 1.0 due to
   Dirichlet BC on small lattices (N=20). The distance-law closure script
   demonstrates beta -> 1.0 in the continuum limit via extrapolation from larger
   lattices (up to 96^3)."

This runner checks the exact parent implementation rather than accepting that
citation as a continuum bridge. It reports two selected finite-data fits,
verifies convergence, proves the propagator's uniform x-layer marginal on the
computed fixed points, and checks that the cited script studies a different
observable in a prescribed field.

Scope: the tested 3D Dirichlet cubic-lattice transfer-propagator construction of
the parent runner at the parent note's parameters (k = 5.0, G = 0.5, sigma = 2.0,
mixing = 0.3, tol = 1e-4, max_iter = 30), at the lattice sizes stated per row.
No infinite-volume limit, exhaustive extrapolation result, or
operator-selection theorem is claimed.
"""

from __future__ import annotations

import hashlib
import math
import sys
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import splu

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import frontier_self_consistent_field_equation as F  # noqa: E402

K_WAVE = 5.0
G_COUPLING = 0.5
SIGMA = 2.0
MIXING = 0.3
TOL = 1e-4
MAX_ITER = 30
EXPECTED_PARENT_RUNNER_SHA256 = (
    "9714bfc547816059745b009ddba47db626444270e34e00aae08319cd2b5d1da2"
)

# N = 12 is excluded: check_field_physics fits radii 2..N//2-3, which is fewer
# than the three points its own mask requires, so it returns beta = nan.
SIZES = (16, 20, 24, 28, 32, 40, 48)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] {label}")
    if detail:
        for line in detail.splitlines():
            print(f"         {line}")
    return condition


def matrix_solver(N: int, which: str):
    """splu-factorized solve, built once per (operator, N) and reused across the
    self-consistent iterations. Uses the parent runner's own Laplacian."""
    A, M = F.build_laplacian_sparse(N)
    Op = A if which == "poisson" else (A @ A)
    lu = splu(Op.tocsc())

    def solve(rho_full):
        rhs = rho_full[1:N - 1, 1:N - 1, 1:N - 1].ravel()
        out = np.zeros((N, N, N))
        out[1:N - 1, 1:N - 1, 1:N - 1] = lu.solve(rhs).reshape((M, M, M))
        return out
    return solve


def local_solver(N: int):
    del N
    return lambda rho_full: rho_full


def fundamental_sign(N, solve):
    """Choose the source sign so every point-source response uses one convention."""
    d = np.zeros((N, N, N))
    d[(N // 2, N // 2, N // 2)] = 1.0
    return float(np.sign(solve(d)[(N // 2, N // 2, N // 2)]))


def converge(N, solve, eps):
    src = (N // 2, N // 2, N // 2)
    phi = np.zeros((N, N, N))
    for it in range(MAX_ITER):
        rho = F.propagate_wavepacket_fast(N, phi, K_WAVE, src, sigma=SIGMA)
        pn = solve(eps * G_COUPLING * rho)
        if not np.all(np.isfinite(pn)):
            return {
                "converged": False,
                "iterations": it + 1,
                "residual": float("inf"),
                "phi": phi,
                "rho": rho,
            }
        pm = (1 - MIXING) * phi + MIXING * pn
        res = float(np.max(np.abs(pm - phi)))
        phi = pm
        if res < TOL and it > 0:
            return {
                "converged": True,
                "iterations": it + 1,
                "residual": res,
                "phi": phi,
                "rho": F.propagate_wavepacket_fast(
                    N, phi, K_WAVE, src, sigma=SIGMA
                ),
            }
    return {
        "converged": False,
        "iterations": MAX_ITER,
        "residual": res,
        "phi": phi,
        "rho": F.propagate_wavepacket_fast(N, phi, K_WAVE, src, sigma=SIGMA),
    }


def extrapolate(Ns, vals, order):
    """v(N) = v_inf + c/N (+ d/N^2). Returns v_inf and its standard error.

    Both families are reported because the repo's own distance-law script
    (frontier_distance_law_definitive.py) reports several extrapolation families
    rather than selecting one.
    """
    Ns = np.asarray(Ns, float)
    vals = np.asarray(vals, float)
    cols = [np.ones_like(Ns), 1.0 / Ns] + ([1.0 / Ns ** 2] if order == 2 else [])
    X = np.column_stack(cols)
    coef, res, *_ = np.linalg.lstsq(X, vals, rcond=None)
    dof = max(1, len(Ns) - X.shape[1])
    s2 = float(res[0] / dof) if len(res) else 0.0
    cov = s2 * np.linalg.inv(X.T @ X)
    return float(coef[0]), float(math.sqrt(max(cov[0, 0], 0.0)))


OPS = {"poisson": "poisson", "biharmonic": "biharmonic", "local": None}

print(__doc__)
parent_runner = REPO_ROOT / "scripts" / "frontier_self_consistent_field_equation.py"
observed_parent_hash = hashlib.sha256(parent_runner.read_bytes()).hexdigest()
check(
    "P0  the imported parent runner matches the reviewed source bytes",
    observed_parent_hash == EXPECTED_PARENT_RUNNER_SHA256,
    f"observed={observed_parent_hash}\nexpected={EXPECTED_PARENT_RUNNER_SHA256}",
)

print("=" * 78)
print("PART A - finite-data fits named by the parent caveat")
print("=" * 78)

measured: dict[str, list[tuple[int, float, float]]] = {}
states: dict[str, dict[int, dict[str, object]]] = {}
for name, which in OPS.items():
    rows = []
    states[name] = {}
    for N in SIZES:
        solve = local_solver(N) if which is None else matrix_solver(N, which)
        eps = fundamental_sign(N, solve)
        state = converge(N, solve, eps)
        states[name][N] = state
        p = F.check_field_physics(
            N, state["phi"], (N // 2, N // 2, N // 2)
        )
        rows.append((N, float(p["beta"]), float(p["beta_r2"])))
    measured[name] = rows

convergence_failures = [
    f"{name}/N={N}: iterations={state['iterations']}, "
    f"residual={state['residual']:.3e}"
    for name, by_size in states.items()
    for N, state in by_size.items()
    if not state["converged"]
]
check(
    "P1  every field used by the finite-size tables reaches the declared "
    "fixed-point tolerance",
    not convergence_failures,
    "all 21 runs converged"
    if not convergence_failures
    else "\n".join(convergence_failures),
)

print("measured beta and power-law fit quality:")
for name, rows in measured.items():
    print(f"  {name}:")
    for N, b, r2 in rows:
        print(f"    N={N:3d}  beta={b:9.4f}  fit R^2={r2:.4f}")

ext = {}
for name, rows in measured.items():
    Ns = [r[0] for r in rows]
    bs = [r[1] for r in rows]
    ext[name] = {1: extrapolate(Ns, bs, 1), 2: extrapolate(Ns, bs, 2)}

# --- S1 ---------------------------------------------------------------------
p1, e1 = ext["poisson"][1]
p2, e2 = ext["poisson"][2]
check(
    "S1  the two selected fits of Poisson's finite beta table both have "
    "intercepts above 1.1",
    p1 > 1.1 and p2 > 1.1,
    f"beta at the largest size N=48: {measured['poisson'][-1][1]:.4f}\n"
    f"extrapolation beta = b_inf + c/N        : b_inf = {p1:.4f} +/- {e1:.4f}\n"
    f"extrapolation beta = b_inf + c/N + d/N^2: b_inf = {p2:.4f} +/- {e2:.4f}\n"
    f"target asserted by the parent note's caveat: 1.0\n"
    "these selected finite-data models do not reproduce 1.0. Over the doubling\n"
    f"from N=24 to N=48 beta changes by "
    f"{measured['poisson'][-1][1] - measured['poisson'][2][1]:+.4f}.\n"
    "This is a statement about two declared models, not an exhaustive continuum\n"
    "extrapolation.",
)

# --- S2 ---------------------------------------------------------------------
bih = measured["biharmonic"]
dev = [abs(b - 1.0) for _, b, _ in bih]
mono_away = all(dev[i] < dev[i + 1] for i in range(len(dev) - 1))
check(
    "S2  across the tested sizes the biharmonic exponent moves monotonically "
    "farther from 1.0",
    mono_away,
    "\n".join(f"    N={N:3d}  beta={b:.4f}  abs(beta-1)={abs(b-1.0):.4f}"
              for N, b, _ in bih) + "\n"
    "the finite-grid gap to 1.0 grows across this table. No asymptotic ranking is\n"
    "inferred from that monotone finite trend.",
)

# --- S3 ---------------------------------------------------------------------
gaps = [(N, abs(measured["poisson"][i][1] - 1.0) - abs(bih[i][1] - 1.0))
        for i, (N, _, _) in enumerate(bih)]
dev_p = [abs(b - 1.0) for _, b, _ in measured["poisson"]]
dev_b = [abs(b - 1.0) for _, b, _ in bih]
Ns = [r[0] for r in bih]
fam1 = extrapolate(Ns, dev_p, 1)[0] - extrapolate(Ns, dev_b, 1)[0]
fam2 = extrapolate(Ns, dev_p, 2)[0] - extrapolate(Ns, dev_b, 2)[0]
check(
    "S3  the two selected extrapolation families do not determine one "
    "Poisson-versus-biharmonic ranking",
    (fam1 > 0) != (fam2 > 0),
    "gap = abs(beta_poisson - 1) - abs(beta_biharmonic - 1), positive means "
    "biharmonic is closer:\n"
    + "\n".join(f"    N={N:3d}  gap={g:+.4f}" for N, g in gaps) + "\n"
    f"extrapolated gap, family b_inf + c/N        : {fam1:+.4f}  "
    f"({'biharmonic' if fam1 > 0 else 'poisson'} closer)\n"
    f"extrapolated gap, family b_inf + c/N + d/N^2: {fam2:+.4f}  "
    f"({'biharmonic' if fam2 > 0 else 'poisson'} closer)\n"
    "the two selected families disagree on the sign, so these fits do not\n"
    "determine a ranking. No claim is made about untested fit families.",
)

# --- S4 ---------------------------------------------------------------------
degrade = {}
for name in ("poisson", "biharmonic"):
    r2s = [r2 for _, _, r2 in measured[name]]
    degrade[name] = (r2s[0], r2s[-1],
                     all(r2s[i] > r2s[i + 1] for i in range(len(r2s) - 1)))
check(
    "S4  the single-power-law fit R^2 decreases monotonically with lattice size "
    "for both matrix operators",
    all(v[2] for v in degrade.values()),
    "\n".join(f"    {n:11s} fit R^2: {a:.4f} at N=16 -> {b:.4f} at N=48  "
              f"(monotonically decreasing: {m})" for n, (a, b, m) in degrade.items())
    + "\nAcross this finite table a single power law explains less of the logged\n"
      "profile variance as N grows. This does not itself select an asymptotic\n"
      "model.",
)

print()
print("=" * 78)
print("PART B - exact layer normalization and the fitted window")
print("=" * 78)

src_rows = []
for N in SIZES:
    s = (N // 2, N // 2, N // 2)
    rho = states["poisson"][N]["rho"]
    g = np.mgrid[0:N, 0:N, 0:N].astype(float)
    rad = np.sqrt((g[0] - s[0]) ** 2 + (g[1] - s[1]) ** 2 + (g[2] - s[2]) ** 2)
    layer_mass = rho.sum(axis=(1, 2))
    layer_error = float(np.max(np.abs(layer_mass - 1.0 / N)))
    x_rms = float(
        np.sqrt(np.sum(layer_mass * (np.arange(N, dtype=float) - s[0]) ** 2))
    )
    expected_x_rms = math.sqrt((N * N + 2.0) / 12.0)
    rms = float(np.sqrt((rho * rad ** 2).sum() / rho.sum()))
    r_fit_max = N // 2 - 3
    enclosed = float(rho[rad <= r_fit_max].sum() / rho.sum())
    src_rows.append(
        (
            N,
            float(rho.sum()),
            layer_error,
            x_rms,
            expected_x_rms,
            rms,
            rms / N,
            r_fit_max,
            enclosed,
        )
    )

# --- S5 ---------------------------------------------------------------------
check(
    "S5  every converged Poisson density has the parent propagator's exact "
    "uniform x-layer marginal",
    all(
        abs(m - 1.0) < 1e-12
        and layer_error < 1e-12
        and abs(x_rms - expected_x_rms) < 1e-10
        for N, m, layer_error, x_rms, expected_x_rms, rms, ratio, rf, e
        in src_rows
    ),
    "\n".join(
        f"    N={N:3d}  max|layer mass-1/N|={layer_error:.2e}  "
        f"x-RMS={x_rms:7.3f}  expected={expected_x_rms:7.3f}  "
        f"full RMS/N={ratio:.4f}"
        for N, m, layer_error, x_rms, expected_x_rms, rms, ratio, rf, e
        in src_rows
    )
    + "\nThe code normalizes each propagated x-layer before normalizing the full\n"
      "density. Hence the x marginal is exactly 1/N and\n"
      "x-RMS=sqrt((N^2+2)/12) for the even sizes used here. The source in this\n"
      "specific propagator therefore spans the box in x; this is not a claim\n"
      "about a differently normalized or fixed localized source.",
)

# --- S6 ---------------------------------------------------------------------
encl = [r[8] for r in src_rows]
check(
    "S6  the parent beta fit is not source-exterior-only on the converged "
    "Poisson densities",
    all(
        1.0 - e >= 5.0 / N - 1e-12
        for N, m, layer_error, x_rms, expected_x_rms, rms, ratio, rf, e
        in src_rows
    ),
    "\n".join(
        f"    N={N:3d}  max fit radius={rf:3d}  source RMS={rms:7.3f}  "
        f"mass outside outer fit radius={1.0-e:.4f}  "
        f"exact layer lower bound={5.0/N:.4f}"
        for N, m, layer_error, x_rms, expected_x_rms, rms, ratio, rf, e
        in src_rows
    )
    + "\ncheck_field_physics fits every axis radius 2..N//2-3. Because the x-layer\n"
      "marginal is exactly 1/N, the five layers with |x-N/2| greater than the\n"
      "outer fit radius put at least 5/N of the source outside the entire fit\n"
      "window. This diagnostic is therefore not source-exterior-only; no claim\n"
      "is made that the field has no exterior.",
)

print()
print("=" * 78)
print("PART C - the observable the parent note's caveat actually cites")
print("=" * 78)

# --- S7 ---------------------------------------------------------------------
cited = REPO_ROOT / "scripts" / "frontier_distance_law_definitive.py"
text = cited.read_text()
measures_deflection = "deflection delta(b) ~ 1/b^alpha" in text
prescribed_source = "point source f = s/r" in text
touches_self_consistent = "self_consistent" in text
check(
    "S7  the script the caveat cites measures ray deflection in a PRESCRIBED "
    "f = s/r field, not the self-consistent field's decay exponent",
    measures_deflection
    and prescribed_source
    and not touches_self_consistent
    and "check_field_physics" not in text,
    f"file: scripts/{cited.name}\n"
    f"  contains 'deflection delta(b) ~ 1/b^alpha' : {measures_deflection}\n"
    f"  contains 'point source f = s/r'            : {prescribed_source}\n"
    f"  references the self-consistent construction: {touches_self_consistent}\n"
    "its stated convention is 'deflection delta(b) ~ 1/b^alpha => alpha = -1.0 "
    "for\nNewtonian gravity', and its analytic cross-check is for a prescribed "
    "point-source\nfield f = s/r. Those are a different observable and a "
    "different field from the\nself-consistent beta the caveat is defending, and "
    "the script never touches the\nself-consistent construction. A separate "
    "bridge could compare the two\nobservables, but the cited script is not such "
    "a bridge.",
)

# --- S8 ---------------------------------------------------------------------
loc = measured["local"]
check(
    "S8  the local-operator finite beta values stay far from 1.0 on every "
    "tested size",
    all(abs(b - 1.0) > 4.0 for _, b, _ in loc),
    "\n".join(f"    N={N:3d}  beta={b:9.4f}" for N, b, _ in loc)
    + "\nNo extrapolation or divergence claim is made for this sequence.",
)

print()
print("=" * 78)
print(f"TOTAL: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL")
print("=" * 78)
sys.exit(0 if FAIL_COUNT == 0 else 1)
