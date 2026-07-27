#!/usr/bin/env python3
"""Cycle 711 - run the continuum extrapolation that self_consistency_forces_poisson_note
invokes in its own caveat but never performed, for every operator rather than for
Poisson alone.

Parent row: docs/audit/data/ledger/se/self_consistency_forces_poisson_note.json
  criticality: critical, deps: [] (root), direct_in_degree: 17,
  transitive_descendants: 727, load_bearing_score: 18.092.

The parent note's first caveat reads:

  "**Finite-size beta**: The measured beta ~ 1.28 exceeds the target 1.0 due to
   Dirichlet BC on small lattices (N=20). The distance-law closure script
   demonstrates beta -> 1.0 in the continuum limit via extrapolation from larger
   lattices (up to 96^3)."

That caveat is the sole defence of the parent note's Bounded Claim 1 against the
observation that its measured exponent is 1.28 rather than the Newtonian 1.0.
Cycle 710 (PR #5656) showed the note's two operator discriminators are empty and
declared this extrapolation the highest-value open follow-up, because the note
ran its continuum argument for Poisson alone and never for the rivals.

This runner performs it. The field operator is fixed across the self-consistent
iterations and only the right-hand side changes, so each operator is factorized
once per lattice size with splu and reused, which is what makes N = 48 reachable.

Scope: the tested 3D Dirichlet cubic-lattice transfer-propagator construction of
the parent runner at the parent note's parameters (k = 5.0, G = 0.5, sigma = 2.0,
mixing = 0.3, tol = 1e-4, max_iter = 30), at the lattice sizes stated per row.
"""

from __future__ import annotations

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
    return lambda rho_full: G_COUPLING * rho_full


def fundamental_sign(N, solve):
    """Per-operator source sign, as established in cycle 710 R10."""
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
            return None
        pm = (1 - MIXING) * phi + MIXING * pn
        res = float(np.max(np.abs(pm - phi)))
        phi = pm
        if res < TOL and it > 0:
            return phi
    return phi


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
print("=" * 78)
print("PART A - the extrapolation the parent note's caveat invokes")
print("=" * 78)

measured: dict[str, list[tuple[int, float, float]]] = {}
for name, which in OPS.items():
    rows = []
    for N in SIZES:
        solve = local_solver(N) if which is None else matrix_solver(N, which)
        eps = fundamental_sign(N, solve)
        phi = converge(N, solve, eps)
        if phi is None:
            continue
        p = F.check_field_physics(N, phi, (N // 2, N // 2, N // 2))
        rows.append((N, float(p["beta"]), float(p["beta_r2"])))
    measured[name] = rows

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
    "S1  Poisson's self-consistent beta does NOT extrapolate to the Newtonian "
    "target 1.0",
    abs(p1 - 1.0) > 0.05 and abs(p2 - 1.0) > 0.05,
    f"beta at the largest size N=48: {measured['poisson'][-1][1]:.4f}\n"
    f"extrapolation beta = b_inf + c/N        : b_inf = {p1:.4f} +/- {e1:.4f}\n"
    f"extrapolation beta = b_inf + c/N + d/N^2: b_inf = {p2:.4f} +/- {e2:.4f}\n"
    f"target asserted by the parent note's caveat: 1.0\n"
    "neither extrapolation family lands near 1.0. Over the doubling from N=24 to\n"
    f"N=48 beta moves only "
    f"{measured['poisson'][2][1] - measured['poisson'][-1][1]:+.4f}.\n"
    "falsifier: either family landing within 0.05 of 1.0, which would support the\n"
    "parent note's caveat.",
)

# --- S2 ---------------------------------------------------------------------
bih = measured["biharmonic"]
dev = [abs(b - 1.0) for _, b, _ in bih]
mono_away = all(dev[i] < dev[i + 1] for i in range(len(dev) - 1))
check(
    "S2  the biharmonic rival's exponent moves monotonically AWAY from 1.0 as "
    "the lattice grows",
    mono_away,
    "\n".join(f"    N={N:3d}  beta={b:.4f}  abs(beta-1)={abs(b-1.0):.4f}"
              for N, b, _ in bih) + "\n"
    "so the biharmonic advantage that cycle 710 measured at N=20 and N=24 is a\n"
    "finite-size effect that dissolves as the lattice grows.\n"
    "falsifier: a monotone approach to 1.0, which would make the rival genuinely\n"
    "better in the continuum.",
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
    "S3  the continuum ranking is INDETERMINATE: the two extrapolation families "
    "disagree on which operator ends up closer to 1.0",
    (fam1 > 0) != (fam2 > 0),
    "gap = abs(beta_poisson - 1) - abs(beta_biharmonic - 1), positive means "
    "biharmonic is closer:\n"
    + "\n".join(f"    N={N:3d}  gap={g:+.4f}" for N, g in gaps) + "\n"
    f"extrapolated gap, family b_inf + c/N        : {fam1:+.4f}  "
    f"({'biharmonic' if fam1 > 0 else 'poisson'} closer)\n"
    f"extrapolated gap, family b_inf + c/N + d/N^2: {fam2:+.4f}  "
    f"({'biharmonic' if fam2 > 0 else 'poisson'} closer)\n"
    "the two families disagree on the SIGN, so this evidence does not determine a\n"
    "continuum ranking either way. This independently confirms cycle 710 R16,\n"
    "which refused to claim any rival is the better operator.\n"
    "falsifier: both families agreeing on the sign, which would determine the\n"
    "ranking and make one of the two readings correct.",
)

# --- S4 ---------------------------------------------------------------------
degrade = {}
for name in ("poisson", "biharmonic"):
    r2s = [r2 for _, _, r2 in measured[name]]
    degrade[name] = (r2s[0], r2s[-1],
                     all(r2s[i] > r2s[i + 1] for i in range(len(r2s) - 1)))
check(
    "S4  the power-law fit quality degrades monotonically with lattice size for "
    "both operators, so the fitted exponent means less at larger N, not more",
    all(v[2] for v in degrade.values()),
    "\n".join(f"    {n:11s} fit R^2: {a:.4f} at N=16 -> {b:.4f} at N=48  "
              f"(monotonically decreasing: {m})" for n, (a, b, m) in degrade.items())
    + "\nthe parent note's caveat assumes larger lattices give a cleaner reading of\n"
      "the same power law. The fit gets worse instead, for both operators.\n"
      "falsifier: R^2 improving with N, which would support extrapolating the "
      "exponent.",
)

print()
print("=" * 78)
print("PART B - why: the source is scale-locked to the box")
print("=" * 78)

src_rows = []
for N in SIZES:
    s = (N // 2, N // 2, N // 2)
    rho = F.propagate_wavepacket_fast(N, np.zeros((N, N, N)), K_WAVE, s, sigma=SIGMA)
    g = np.mgrid[0:N, 0:N, 0:N].astype(float)
    rad = np.sqrt((g[0] - s[0]) ** 2 + (g[1] - s[1]) ** 2 + (g[2] - s[2]) ** 2)
    rms = float(np.sqrt((rho * rad ** 2).sum() / rho.sum()))
    r_fit_max = N // 2 - 3
    enclosed = float(rho[rad <= r_fit_max].sum() / rho.sum())
    src_rows.append((N, float(rho.sum()), rms, rms / N, r_fit_max, enclosed))

# --- S5 ---------------------------------------------------------------------
ratios = [r[3] for r in src_rows]
check(
    "S5  the source never localizes: total mass is pinned to 1 and its RMS "
    "radius is a fixed fraction of the box",
    all(abs(m - 1.0) < 1e-12 for _, m, _, _, _, _ in src_rows)
    and (max(ratios) - min(ratios)) < 0.05,
    "\n".join(f"    N={N:3d}  total mass={m:.9f}  RMS radius={rms:7.3f}  "
              f"RMS/N={ratio:.4f}" for N, m, rms, ratio, _, _ in src_rows) + "\n"
    f"RMS/N stays within [{min(ratios):.4f}, {max(ratios):.4f}]\n"
    "the parent propagator normalizes total density to 1 and every layer to "
    "exactly\n1/N (cycle 710 R7), so the self-consistent source is a box-filling\n"
    "distribution rather than a localized mass. There is therefore no limit in "
    "which\nit becomes a point source and a 1/r far field could appear.\n"
    "falsifier: the RMS radius saturating at a fixed value as N grows, which "
    "would\nmake the source a fixed physical object and the extrapolation "
    "meaningful.",
)

# --- S6 ---------------------------------------------------------------------
encl = [r[5] for r in src_rows]
check(
    "S6  the beta fit window lies inside the source, and the enclosed mass "
    "fraction INCREASES with lattice size",
    all(encl[i] < encl[i + 1] for i in range(len(encl) - 1)) and encl[-1] > 0.8,
    "\n".join(f"    N={N:3d}  max fit radius={rf:3d}  source RMS={rms:7.3f}  "
              f"mass enclosed within the fit window={e:.4f}"
              for N, _, rms, _, rf, e in src_rows) + "\n"
    "check_field_physics fits radii 2..N//2-3 (its lines 387 and 405). A 1/r far\n"
    "field can only be read outside the source, but the fraction of source mass\n"
    f"inside the fit window rises from {encl[0]:.4f} at N=16 to {encl[-1]:.4f} "
    f"at N=48.\n"
    "so enlarging the lattice moves this diagnostic FURTHER from a far-field\n"
    "measurement, which inverts the parent note's caveat, and it explains S4:\n"
    "the profile inside a spreading cloud is progressively less power-law-like.\n"
    "falsifier: the enclosed fraction decreasing with N, which would mean larger\n"
    "lattices do approach a far-field reading.",
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
    measures_deflection and prescribed_source and not touches_self_consistent,
    f"file: scripts/{cited.name}\n"
    f"  contains 'deflection delta(b) ~ 1/b^alpha' : {measures_deflection}\n"
    f"  contains 'point source f = s/r'            : {prescribed_source}\n"
    f"  references the self-consistent construction: {touches_self_consistent}\n"
    "its stated convention is 'deflection delta(b) ~ 1/b^alpha => alpha = -1.0 "
    "for\nNewtonian gravity', and its analytic cross-check is for a prescribed "
    "point-source\nfield f = s/r. Those are a different observable and a "
    "different field from the\nself-consistent beta the caveat is defending, and "
    "the script never touches the\nself-consistent construction.\n"
    "falsifier: the script fitting the self-consistent field's beta, which would\n"
    "make the caveat's citation apposite.",
)

# --- S8 ---------------------------------------------------------------------
loc = measured["local"]
l1 = extrapolate([r[0] for r in loc], [r[1] for r in loc], 1)[0]
l2 = extrapolate([r[0] for r in loc], [r[1] for r in loc], 2)[0]
check(
    "S8  the 'local' operator diverges under the same scaling, so its exclusion "
    "does not depend on any of the above",
    l1 > 20.0 and l2 > 20.0,
    "\n".join(f"    N={N:3d}  beta={b:9.4f}" for N, b, _ in loc) + "\n"
    f"extrapolated b_inf: {l1:.2f} (1/N family), {l2:.2f} (1/N + 1/N^2 family)\n"
    "cycle 710 found 'local' excluded on the decay exponent alone rather than by "
    "the\nsign convention. That conclusion survives this scaling analysis.\n"
    "falsifier: a finite extrapolated exponent near 1.0.",
)

print()
print("=" * 78)
print(f"TOTAL: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL")
print("=" * 78)
sys.exit(0 if FAIL_COUNT == 0 else 1)
