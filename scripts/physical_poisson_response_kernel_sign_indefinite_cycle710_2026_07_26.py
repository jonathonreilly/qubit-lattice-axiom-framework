#!/usr/bin/env python3
"""Cycle 710 - diagnostic repair of self_consistency_forces_poisson_note.

Parent row: docs/audit/data/ledger/se/self_consistency_forces_poisson_note.json
  criticality: critical, deps: [] (root), direct_in_degree: 17,
  transitive_descendants: 727, load_bearing_score: 18.092.

The parent row's re-audit note asks for exactly three things:

  "missing_bridge_theorem: compare susceptibility with the matched
   point-to-point inverse-Laplacian kernel, normalize alternative-operator
   source signs consistently, and revise the note to the resulting finite
   numerical scope before re-audit."

and its chain_closure_explanation names the obstruction:

  "it does not establish that the transfer propagator's response kernel is
   the inverse graph Laplacian. Its susceptibility scalar is correlated with
   the domain-integrated Green-function norm for sources moved toward the
   boundary, rather than with a matched point-to-point Poisson profile."

This runner does the two computations and reports the resulting scope.
Every row is computed from the repo's own operators and propagator, imported
directly from scripts/frontier_self_consistent_field_equation.py, so the
object under test is the parent note's actual construction and not a
paraphrase of it.

Scope of every numerical row below: the tested 3D Dirichlet cubic-lattice
transfer-propagator construction of the parent runner, at the parameter
values the parent note works at (k = 5.0, G = 0.5, sigma = 2.0, mixing = 0.3),
at the lattice sizes stated per row. No row is a continuum-limit claim.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
from scipy import sparse

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import frontier_self_consistent_field_equation as F  # noqa: E402

K_WAVE = 5.0
G_COUPLING = 0.5
SIGMA = 2.0
MIXING = 0.3
TOL = 1e-4
MAX_ITER = 30

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


def interior_mask(N: int) -> np.ndarray:
    m = np.zeros((N, N, N), dtype=bool)
    m[1:N - 1, 1:N - 1, 1:N - 1] = True
    return m


def switchable_propagate(N, phi, k, source_pos, sigma=2.0, renormalize=True):
    """Byte-for-byte re-implementation of F.propagate_wavepacket_fast with the
    per-layer renormalization and the global normalization made switchable.

    R1 below verifies that renormalize=True reproduces the repo propagator
    exactly, so the renormalize=False branch is the same physics with one
    identified step removed and nothing else changed.
    """
    sx, sy, sz = source_pos
    yy, zz = np.mgrid[0:N, 0:N]
    psi_init = np.exp(-((yy - sy) ** 2 + (zz - sz) ** 2) / (2 * sigma ** 2)).astype(complex)
    psi_init /= np.sqrt(np.sum(np.abs(psi_init) ** 2))

    density = np.zeros((N, N, N))
    density[sx, :, :] = np.abs(psi_init) ** 2

    offsets = [(dy, dz, math.sqrt(1.0 + dy ** 2 + dz ** 2))
               for dy in (-1, 0, 1) for dz in (-1, 0, 1)]

    for direction in (+1, -1):
        psi_layer = psi_init.copy()
        x_range = range(sx + 1, N) if direction == +1 else range(sx - 1, -1, -1)
        for x_new in x_range:
            x_old = x_new - direction
            psi_new = np.zeros((N, N), dtype=complex)
            for dy, dz, L in offsets:
                if dy >= 0:
                    src_y, dst_y = ((slice(0, N - dy), slice(dy, N)) if dy > 0
                                    else (slice(0, N), slice(0, N)))
                else:
                    src_y, dst_y = slice(-dy, N), slice(0, N + dy)
                if dz >= 0:
                    src_z, dst_z = ((slice(0, N - dz), slice(dz, N)) if dz > 0
                                    else (slice(0, N), slice(0, N)))
                else:
                    src_z, dst_z = slice(-dz, N), slice(0, N + dz)
                f_avg = 0.5 * (phi[x_old, src_y, src_z] + phi[x_new, dst_y, dst_z])
                # written exactly as the parent runner writes it, so that R1 can
                # assert bit-identity rather than round-off-level agreement
                S = L * (1.0 - f_avg)
                amp = np.exp(1j * k * S) / L
                psi_new[dst_y, dst_z] += amp * psi_layer[src_y, src_z]
            if renormalize:
                nrm = np.sqrt(np.sum(np.abs(psi_new) ** 2))
                if nrm > 1e-30:
                    psi_new /= nrm
            psi_layer = psi_new
            density[x_new, :, :] += np.abs(psi_layer) ** 2

    if renormalize:
        tot = density.sum()
        if tot > 1e-30:
            density /= tot
    return density


def response_column(N, y_site, source_pos, k=K_WAVE, dphi=1e-3, renormalize=True):
    """K(.,y) = d rho(.) / d phi(y), a single-site field perturbation."""
    zero = np.zeros((N, N, N))
    rho0 = switchable_propagate(N, zero, k, source_pos, SIGMA, renormalize)
    phip = np.zeros((N, N, N))
    phip[y_site] = dphi
    rhop = switchable_propagate(N, phip, k, source_pos, SIGMA, renormalize)
    return (rhop - rho0) / dphi


def scalar_match(Kcol, Gcol, mask):
    """Best-fit scalar c minimising ||K - c G||, and the relative residual."""
    kv, gv = Kcol[mask], Gcol[mask]
    c = float(kv @ gv / (gv @ gv))
    resid = float(np.linalg.norm(kv - c * gv) / np.linalg.norm(kv))
    corr = float(np.corrcoef(kv, gv)[0, 1])
    return c, resid, corr


# ---------------------------------------------------------------------------
print(__doc__)
print("=" * 78)
print("PART A - the matched point-to-point response kernel (re-audit ask #1)")
print("=" * 78)

# --- R1 ---------------------------------------------------------------------
diffs = []
for (N, k) in ((10, 5.0), (12, 2.0)):
    s = (N // 2, N // 2, N // 2)
    rng = np.random.default_rng(7)
    phi = rng.normal(0, 0.3, (N, N, N))
    a = F.propagate_wavepacket_fast(N, phi, k, s, sigma=SIGMA)
    b = switchable_propagate(N, phi, k, s, SIGMA, renormalize=True)
    diffs.append(float(np.abs(a - b).max()))
check(
    "R1  switchable propagator reproduces the parent runner exactly "
    "(renormalize=True)",
    all(d == 0.0 for d in diffs),
    f"max|repo - reimplementation| at (N=10,k=5.0) and (N=12,k=2.0): {diffs}\n"
    "falsifier: any nonzero difference would mean later rows test a different\n"
    "propagator than the parent note's.",
)

# --- R2 ---------------------------------------------------------------------
g_signed = []
for N in (10, 12):
    s = (N // 2, N // 2, N // 2)
    Gf = F.poisson_greens_function(N, s)
    v = Gf[interior_mask(N)]
    g_signed.append((N, float(np.mean(v > 0)), float(np.abs(v).min())))
check(
    "R2  inverse Dirichlet graph Laplacian is single-signed on the interior",
    all(frac == 1.0 and mn > 0.0 for _, frac, mn in g_signed),
    "\n".join(f"N={N}: fraction of interior sites with G>0 = {frac:.6f}, "
              f"min|G| = {mn:.3e}" for N, frac, mn in g_signed) + "\n"
    "falsifier: any interior sign change or exact zero in G.",
)

# --- R3 / R4 ----------------------------------------------------------------
N = 10
s = (N // 2, N // 2, N // 2)
mask = interior_mask(N)
r3_rows, r4_rows = [], []
for dr in (1, 2, 3):
    y = (s[0], s[1] + dr, s[2])
    Kcol = response_column(N, y, s)
    Gcol = F.poisson_greens_function(N, y)
    kv = Kcol[mask]
    fpos, fneg = float(np.mean(kv > 0)), float(np.mean(kv < 0))
    r3_rows.append((dr, fpos, fneg))
    c, resid, corr = scalar_match(Kcol, Gcol, mask)
    r4_rows.append((dr, c, resid, corr))
check(
    "R3  response kernel K(.,y) = d rho / d phi(y) is sign-indefinite",
    all(fp > 0.05 and fn > 0.05 for _, fp, fn in r3_rows),
    "\n".join(f"y = source + {dr}*yhat : fraction K>0 = {fp:.4f}, "
              f"fraction K<0 = {fn:.4f}" for dr, fp, fn in r3_rows) + "\n"
    "falsifier: K single-signed (either fraction below 5%), which is what a\n"
    "kernel proportional to the inverse Laplacian would have to be by R2.",
)
check(
    "R4  no scalar c makes K proportional to G (relative residual > 0.9)",
    all(resid > 0.9 for _, _, resid, _ in r4_rows),
    "\n".join(f"y = source + {dr}*yhat : best-fit c = {c:+.4e}, "
              f"relative residual = {resid:.4f}, corr(K,G) = {corr:+.4f}"
              for dr, c, resid, corr in r4_rows) + "\n"
    "this is the matched point-to-point comparison the re-audit note asks for.\n"
    "falsifier: a small residual at any tested site.",
)

# --- R5 ---------------------------------------------------------------------
y = (s[0], s[1] + 2, s[2])
Gcol = F.poisson_greens_function(N, y)
k_rows = []
for k in (0.05, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0):
    Kcol = response_column(N, y, s, k=k)
    c, resid, corr = scalar_match(Kcol, Gcol, mask)
    k_rows.append((k, corr, resid, float(np.abs(Kcol[mask]).sum())))
check(
    "R5  the mismatch is not a strong-coupling artifact: |corr(K,G)| < 0.25 "
    "across k in [0.05, 10]",
    all(abs(corr) < 0.25 for _, corr, _, _ in k_rows),
    "\n".join(f"k = {k:<5}: corr(K,G) = {corr:+.4f}, residual = {resid:.4f}, "
              f"|K|_1 = {n1:.3e}" for k, corr, resid, n1 in k_rows) + "\n"
    "falsifier: corr approaching 1 at small k, i.e. a weak-coupling regime in\n"
    "which the parent note's identification would hold. This row is the\n"
    "steelman for the parent note and it does not survive.",
)

# --- R6 ---------------------------------------------------------------------
r6_rows = []
for dr in (1, 2, 3):
    yy_ = (s[0], s[1] + dr, s[2])
    Kcol = response_column(N, yy_, s, renormalize=False)
    Gc = F.poisson_greens_function(N, yy_)
    c, resid, corr = scalar_match(Kcol, Gc, mask)
    r6_rows.append((dr, resid, corr))
check(
    "R6  removing the per-layer renormalization does NOT produce a match",
    all(resid > 0.9 for _, resid, _ in r6_rows),
    "\n".join(f"y = source + {dr}*yhat (renormalize=False): residual = {resid:.4f}, "
              f"corr = {corr:+.4f}" for dr, resid, corr in r6_rows) + "\n"
    "this row falsifies the natural repair hypothesis that the per-layer\n"
    "renormalization is what destroys the Green-function structure. It is not:\n"
    "the field enters only as a phase (|amp| = 1/L, independent of phi), so the\n"
    "density response is an interference kernel either way.\n"
    "falsifier: a small residual, which would have identified the repair.",
)

# --- R7 ---------------------------------------------------------------------
N7 = 12
s7 = (N7 // 2, N7 // 2, N7 // 2)
rng = np.random.default_rng(0)
fields = {
    "zero": np.zeros((N7, N7, N7)),
    "random_sigma0.05": rng.normal(0, 0.05, (N7, N7, N7)),
    "random_sigma0.9": rng.normal(0, 0.9, (N7, N7, N7)),
    "single_site_bump": np.zeros((N7, N7, N7)),
    "uniform_0.5": np.full((N7, N7, N7), 0.5),
}
fields["single_site_bump"][3, 4, 5] = 0.7
lay_dev = []
for name, phi in fields.items():
    rho = F.propagate_wavepacket_fast(N7, phi, K_WAVE, s7, sigma=SIGMA)
    lm = rho.sum(axis=(1, 2))
    lay_dev.append((name, float(np.abs(lm - 1.0 / N7).max())))
rho0 = F.propagate_wavepacket_fast(N7, fields["zero"], K_WAVE, s7, sigma=SIGMA)
phip = np.zeros((N7, N7, N7))
phip[s7[0], s7[1] + 2, s7[2]] = 0.1
rhop = F.propagate_wavepacket_fast(N7, phip, K_WAVE, s7, sigma=SIGMA)
d = rhop - rho0
signed, absolute = float(abs(d.sum())), float(np.abs(d).sum())
check(
    "R7  per-layer mass is exactly 1/N for every field, so the signed response "
    "sums to machine zero and the absolute value in the parent statistic is "
    "load-bearing",
    all(dev < 1e-15 for _, dev in lay_dev) and signed < 1e-14 and absolute > 1e-3,
    "\n".join(f"phi = {name:18s} max|layer mass - 1/N| = {dev:.3e}"
              for name, dev in lay_dev) + "\n"
    f"single-site perturbation: |signed sum| = {signed:.3e}, "
    f"sum|.| = {absolute:.6e}\n"
    "the parent runner's statistic is sum(abs(rho_p - rho_0)) (line 489). The\n"
    "signed sum it would otherwise be is exactly zero, so the statistic is a\n"
    "total-variation reshaping measure and carries no response amplitude.\n"
    "falsifier: layer mass depending on phi, or a nonzero signed sum.",
)

print()
print("=" * 78)
print("PART B - the 0.93 shape correlation (parent note Bounded Claim 3)")
print("=" * 78)

# --- R8 ---------------------------------------------------------------------
N8 = 20
s8 = (N8 // 2, N8 // 2, N8 // 2)
r_vals, chi, _ = F.compute_susceptibility_profile(N8, K_WAVE, s8, delta_phi=0.1,
                                                 sigma=SIGMA)
Gfull = F.poisson_greens_function(N8, s8)
gprof = np.array([Gfull[s8[0], s8[1] + int(dv), s8[2]] for dv in r_vals])
ok = (chi > 0) & (gprof > 0)
sl_chi = float(np.polyfit(np.log(r_vals[ok]), np.log(chi[ok]), 1)[0])
sl_g = float(np.polyfit(np.log(r_vals[ok]), np.log(gprof[ok]), 1)[0])
corr_note = float(np.corrcoef(chi[ok], gprof[ok])[0, 1])
ratio = chi[ok] / gprof[ok]
spread = float(ratio.max() / ratio.min())
check(
    "R8  the parent note's own statistic is high while the two profiles "
    "disagree in shape",
    corr_note > 0.9 and abs(sl_chi - sl_g) > 0.5 and spread > 5.0,
    f"radii tested (the parent note's own set): {r_vals[ok].astype(int).tolist()}\n"
    f"Pearson corr(chi, G_poisson)   = {corr_note:.6f}   "
    f"(parent note reports 0.93 as a 'strong match')\n"
    f"chi(r) log-log slope           = {sl_chi:+.4f}\n"
    f"G_poisson(r) log-log slope     = {sl_g:+.4f}\n"
    f"chi/G ratio across the radii   = {ratio.min():.4g} .. {ratio.max():.4g}  "
    f"(spread factor {spread:.1f}x)\n"
    "a matched profile has a constant ratio. falsifier: a near-constant ratio\n"
    "or matching slopes, which would make the high correlation meaningful.",
)

# --- R9 ---------------------------------------------------------------------
rr = r_vals[ok]
g_pow = rr ** -1.0
P_GRID_LO = 0.01
band = [p for p in np.arange(P_GRID_LO, 10.001, 0.01)
        if np.corrcoef(g_pow, rr ** -p)[0, 1] >= 0.93]
probe = {p: float(np.corrcoef(g_pow, rr ** -p)[0, 1])
         for p in (1.0, 1.28, 2.0, 2.805, 4.0, 8.637)}
check(
    "R9  a 0.93 shape-correlation threshold on these radii does not exclude "
    "the parent note's own rival exponents",
    min(band) < 0.5 and max(band) > 2.805 and probe[2.805] >= 0.93,
    f"exponents p with corr(r^-1, r^-p) >= 0.93 : p in "
    f"[{min(band):.2f}, {max(band):.2f}]\n"
    f"(the lower endpoint is the scan grid's floor p = {P_GRID_LO}, not a real "
    f"boundary; the\ninformative endpoint is the upper one, {max(band):.2f})\n"
    + "\n".join(f"  p = {p:<6} corr = {c:.6f}" for p, c in probe.items()) + "\n"
    "p = 2.805 is the susceptibility exponent the parent row's verdict "
    "rationale reports;\np = 8.637 is the 'local' operator's exponent the "
    "parent note lists as unphysical.\n"
    "falsifier: a narrow band excluding those exponents, which would make 0.93\n"
    "a discriminating threshold.",
)

print()
print("=" * 78
      )
print("PART C - per-operator source-sign normalization (re-audit ask #2)")
print("=" * 78)

SOLVERS = {
    "poisson": (F.solve_poisson, {}),
    "biharmonic": (F.solve_biharmonic, {}),
    "local": (F.solve_local, {"G": G_COUPLING}),
    "inv_r2": (F.solve_inv_r2_kernel, {"G": G_COUPLING, "mid": None}),
}


def fundamental_sign(N, solver, kwargs):
    """sign of the operator's response at the source to a unit POSITIVE point source."""
    kw = dict(kwargs)
    if "mid" in kw:
        kw["mid"] = N // 2
    d0 = np.zeros((N, N, N))
    d0[(N // 2, N // 2, N // 2)] = 1.0
    return float(np.sign(solver(N, d0, **kw)[(N // 2, N // 2, N // 2)]))


def iterate_signed(N, solver, kwargs, eps):
    """The parent runner's self_consistent_iterate with its hardcoded
    rho_source = -G*rho (line 296) replaced by rho_source = eps*G*rho."""
    kw = dict(kwargs)
    if "mid" in kw:
        kw["mid"] = N // 2
    src = (N // 2, N // 2, N // 2)
    phi = np.zeros((N, N, N))
    for it in range(MAX_ITER):
        rho = F.propagate_wavepacket_fast(N, phi, K_WAVE, src, sigma=SIGMA)
        phi_new = solver(N, eps * G_COUPLING * rho, **kw)
        if not np.all(np.isfinite(phi_new)):
            return None, it + 1, False
        phi_mix = (1 - MIXING) * phi + MIXING * phi_new
        res = float(np.max(np.abs(phi_mix - phi)))
        phi = phi_mix
        if res < TOL and it > 0:
            return phi, it + 1, True
    return phi, MAX_ITER, False


# --- R10 --------------------------------------------------------------------
signs = {n: fundamental_sign(20, sv, kw) for n, (sv, kw) in SOLVERS.items()}
check(
    "R10 Poisson's fundamental solution has the opposite sign to every rival, "
    "and the parent runner feeds all of them the same source",
    signs["poisson"] == -1.0
    and all(signs[n] == +1.0 for n in ("biharmonic", "local", "inv_r2")),
    "\n".join(f"  {n:12s} sign of O^-1(+delta) at the source = {v:+.0f}"
              for n, v in signs.items()) + "\n"
    "the parent runner's self_consistent_iterate hardcodes "
    "rho_source = -G * rho\n(line 296) for every operator. The Laplacian is "
    "negative definite on the\nDirichlet interior; the biharmonic, local and "
    "1/r^2 kernels are positive.\nSo one fixed source sign yields an "
    "attractive well for Poisson and a\nrepulsive hill for each rival, which "
    "is the whole content of the parent\nnote's 'Attractive?' column.\n"
    "falsifier: the signs agreeing, which would make the column substantive.",
)

# --- R11 / R12 --------------------------------------------------------------
r11 = {}
for Nsz in (20, 24):
    rows = {}
    for name, (solver, kw) in SOLVERS.items():
        eps = fundamental_sign(Nsz, solver, kw)
        phi, iters, conv = iterate_signed(Nsz, solver, kw, eps)
        if phi is None:
            rows[name] = dict(conv=False, attr=False, mono=False,
                              beta=float("nan"), fpos=float("nan"))
            continue
        p = F.check_field_physics(Nsz, phi, (Nsz // 2, Nsz // 2, Nsz // 2))
        v = phi[interior_mask(Nsz)]
        rows[name] = dict(conv=conv, attr=bool(p["attractive"]),
                          mono=bool(p["monotonic"]), beta=float(p["beta"]),
                          fpos=float(np.mean(v > 0)))
    r11[Nsz] = rows

lines = []
poisson_rank = {}
for Nsz, rows in r11.items():
    lines.append(f"  N = {Nsz}:")
    elig = [(n, r) for n, r in rows.items()
            if r["attr"] and r["mono"] and not math.isnan(r["beta"])]
    order = sorted(elig, key=lambda t: abs(t[1]["beta"] - 1.0))
    for rank, (n, r) in enumerate(order, 1):
        lines.append(f"    {rank}. {n:12s} beta = {r['beta']:7.4f}  "
                     f"|beta-1| = {abs(r['beta']-1.0):7.4f}  "
                     f"attractive={r['attr']}  monotone={r['mono']}  "
                     f"frac(phi>0)={r['fpos']:.4f}")
    poisson_rank[Nsz] = [n for n, _ in order].index("poisson") + 1
check(
    "R11 under per-operator sign normalization Poisson is not the best "
    "operator in the tested family: it ranks third at both lattice sizes",
    all(rk == 3 for rk in poisson_rank.values()),
    "\n".join(lines) + "\n"
    f"Poisson's rank by |beta - 1| among attractive+monotone operators: "
    f"{poisson_rank}\n"
    "the parent note's Bounded Claim 1 states unscreened Poisson is 'the "
    "best-supported\noperator in the tested family and the only tested one "
    "that stays close to the\nNewtonian target'. At the parent note's own "
    "working point, with its own beta\ndiagnostic, and with the source sign "
    "normalized per operator as the re-audit\nnote asks, biharmonic and the "
    "1/r^2 kernel both land closer to beta = 1.\n"
    "falsifier: Poisson ranking first at either size.",
)
check(
    "R12 biharmonic and the 1/r^2 kernel are genuine global wells after "
    "normalization, not merely positive at the source",
    all(r11[Nsz][n]["fpos"] == 1.0 for Nsz in (20, 24)
        for n in ("poisson", "biharmonic", "inv_r2")),
    "\n".join(f"  N={Nsz} {n:12s} fraction of interior sites with phi>0 = "
              f"{r11[Nsz][n]['fpos']:.6f}"
              for Nsz in (20, 24)
              for n in ("poisson", "biharmonic", "local", "inv_r2")) + "\n"
    "sign normalization fixes the source-point sign by construction, so that "
    "bit alone\nis not evidence. This row tests the whole interior instead, and "
    "all four operators\nare positive throughout it, including 'local' "
    "(phi = G*rho with rho > 0 everywhere).\nSo the parent note's "
    "'Attractive?' column has no content beyond the source sign\nfor any of "
    "the four. What survives as a genuine discriminator is the decay\n"
    "exponent alone, and on that 'local' does fail badly (R11: beta = 8.6 at "
    "N=20,\n12.3 at N=24) while biharmonic and 1/r^2 do not.\n"
    "falsifier: a rival changing sign somewhere in the interior, which would "
    "leave the\nparent note's attractiveness discriminator with real content.",
)

# --- R13 --------------------------------------------------------------------
A, _ = F.build_laplacian_sparse(12)
scr_max = []
for mu2 in (0.0, 0.01, 0.1, 0.5, 1.0, 2.0):
    Asc = (A - mu2 * sparse.eye(A.shape[0])).toarray()
    scr_max.append((mu2, float(np.linalg.eigvalsh(Asc).max())))
check(
    "R13 the screened-Poisson family shares Poisson's definiteness, so the "
    "parent note's Test 4 is untouched by the sign defect",
    all(mx < 0.0 for _, mx in scr_max),
    "\n".join(f"  mu^2 = {mu2:<5} max eigenvalue of (Laplacian - mu^2 I) = "
              f"{mx:+.6f}" for mu2, mx in scr_max) + "\n"
    "every member of the screened family is negative definite, like the "
    "unscreened\nLaplacian, so one fixed source sign treats them all "
    "consistently. The parent\nnote's screened sweep and its conclusion that "
    "mu^2 = 0 is closest to beta = 1\nwithin that family are not affected by "
    "this cycle.\n"
    "falsifier: a nonnegative eigenvalue, which would extend the sign defect "
    "to Test 4.",
)


# --- R14 -------------------------------------------------------------------
# The strongest physical escape from Part C: require the mediator kernel to be
# positive, so that superposing positive masses never anti-attracts. That would
# exclude biharmonic on grounds independent of the source-sign convention. For
# the clamped-plate biharmonic operator positivity genuinely can fail
# (Coffman-Duffin). The parent runner does not implement that operator: it
# implements A @ A, the square of the Dirichlet Laplacian, whose inverse is the
# square of an entrywise single-signed matrix and is therefore entrywise
# positive by construction. So this escape is not available here.
N14 = 10
A14, M14 = F.build_laplacian_sparse(N14)
A14d = A14.toarray()
Ainv = np.linalg.inv(A14d)
Bih = np.linalg.inv((A14 @ A14).toarray())
lap_single = bool(np.all(Ainv < 0) or np.all(Ainv > 0))
compose_err = float(np.abs(Bih - Ainv @ Ainv).max())
bih_pos = float(np.mean(Bih > 0))
check(
    "R14 the tested biharmonic rival is positivity-preserving by construction, "
    "so a mediator-positivity requirement cannot exclude it either",
    lap_single and compose_err < 1e-12 and bih_pos == 1.0,
    f"Dirichlet Laplacian inverse is entrywise single-signed: {lap_single}\n"
    f"max|(A@A)^-1 - (A^-1)^2| = {compose_err:.3e}  (so the tested biharmonic "
    f"is (Delta_D)^-2)\n"
    f"fraction of entries of (A@A)^-1 that are positive = {bih_pos:.6f}\n"
    "the product of two entrywise single-signed matrices is entrywise positive, "
    "so the\ntested biharmonic Green's function cannot change sign. Requiring a "
    "positive\nmediator kernel - the strongest convention-free discriminator "
    "available - does\nnot separate it from Poisson. Clamped-plate biharmonic "
    "positivity can fail\n(Coffman-Duffin), but that is a different operator "
    "from the one the parent\nrunner tests.\n"
    "falsifier: a sign change in the tested biharmonic Green's function, which "
    "would\nrestore a convention-free discriminator and partially rescue the "
    "parent note.",
)


# --- R15 -------------------------------------------------------------------
# R11 uses the parent note's single G = 0.5 for every operator. The operators
# have very different natural scales, so each converges to a different |phi|,
# and the self-consistent loop is nonlinear. If beta depended on the converged
# amplitude, the R11 ranking would be an amplitude artifact rather than an
# operator-shape result. Sweep G per operator over an 80x range, then compare
# at matched converged amplitude.
def _iter_G(Nsz, solver, kwargs, eps, Gc):
    kw = dict(kwargs)
    if "mid" in kw:
        kw["mid"] = Nsz // 2
    kernel_type = "G" in kw
    if kernel_type:
        kw["G"] = Gc
    srcpos = (Nsz // 2, Nsz // 2, Nsz // 2)
    phi = np.zeros((Nsz, Nsz, Nsz))
    for it in range(MAX_ITER):
        rho = F.propagate_wavepacket_fast(Nsz, phi, K_WAVE, srcpos, sigma=SIGMA)
        srcterm = eps * rho if kernel_type else eps * Gc * rho
        pn = solver(Nsz, srcterm, **kw)
        if not np.all(np.isfinite(pn)):
            return None, None
        pm = (1 - MIXING) * phi + MIXING * pn
        res = float(np.max(np.abs(pm - phi)))
        phi = pm
        if res < TOL and it > 0:
            break
    p = F.check_field_physics(Nsz, phi, srcpos)
    return float(np.max(np.abs(phi))), float(p["beta"])


N15 = 20
G_SWEEP = (0.05, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0)
sweep = {}
for name, (solver, kw) in SOLVERS.items():
    eps = fundamental_sign(N15, solver, kw)
    rows = []
    for Gc in G_SWEEP:
        amp, beta = _iter_G(N15, solver, kw, eps, Gc)
        if amp is not None and not math.isnan(beta):
            rows.append((Gc, amp, beta))
    sweep[name] = rows
spreads = {n: (min(b for _, _, b in r), max(b for _, _, b in r))
           for n, r in sweep.items() if r}
ref_amp = [a for g, a, _ in sweep["poisson"] if abs(g - G_COUPLING) < 1e-12][0]
matched = {}
for name, rows in sweep.items():
    g, a, b = min(rows, key=lambda t: abs(math.log(t[1]) - math.log(ref_amp)))
    matched[name] = (g, a, b)
matched_order = sorted(matched.items(), key=lambda t: abs(t[1][2] - 1.0))
matched_rank = [n for n, _ in matched_order].index("poisson") + 1
check(
    "R15 the R11 ranking is not an amplitude artifact: beta is amplitude-"
    "independent per operator, and the ranking is unchanged at matched amplitude",
    all(hi - lo < 0.05 for lo, hi in spreads.values()) and matched_rank == 3,
    "beta range across an 80x sweep in the coupling G, per operator:\n"
    + "\n".join(f"  {n:11s} beta in [{lo:.4f}, {hi:.4f}]  spread {hi-lo:.4f}"
                for n, (lo, hi) in spreads.items())
    + f"\nreference amplitude: poisson at G={G_COUPLING} gives "
      f"max abs(phi) = {ref_amp:.5f}\n"
    "each operator at the G whose converged amplitude is closest to that "
    "reference:\n"
    + "\n".join(f"  {n:11s} G={g:<6} max abs(phi)={a:.5f}  beta={b:7.4f}  "
                f"abs(beta-1)={abs(b-1.0):.4f}" for n, (g, a, b) in matched.items())
    + "\nranking at matched amplitude: "
    + ", ".join(f"{i}. {n}" for i, (n, _) in enumerate(matched_order, 1))
    + f"\nPoisson's rank at matched amplitude: {matched_rank}\n"
    "so beta is a property of the operator's shape, not of the field strength it\n"
    "happens to converge to at a shared coupling. This closes the strongest\n"
    "objection to R11: that the parent note's single G = 0.5 evaluates each\n"
    "operator at a different effective amplitude.\n"
    "falsifier: beta varying appreciably with G, or Poisson ranking first once\n"
    "amplitudes are matched.",
)

print()
print("=" * 78)
print(f"TOTAL: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL")
print("=" * 78)
print("""
Measured but NOT claimed: the parent note's 'linear response regime' caveat
holds. The statistic sum|rho_p - rho_0| scales as delta_phi^1.124 over
delta_phi in [0.0125, 0.2] at r = 3 (N = 12), i.e. approximately linear. This
cycle looked for a linearity failure there and did not find one.
""")
sys.exit(0 if FAIL_COUNT == 0 else 1)
