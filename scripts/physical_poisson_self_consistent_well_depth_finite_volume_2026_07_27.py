#!/usr/bin/env python3
"""Finite-volume self-consistent localization and well-depth model comparisons
on a supplied four-operator family.

Context.  `docs/SELF_CONSISTENCY_FORCES_POISSON_NOTE.md` claims that demanding
self-consistency between a propagator and the field it sources selects the
unscreened Poisson operator.  Its ledger row asks, verbatim, to "normalize
alternative-operator source signs consistently" and records that "a
response-kernel bridge is still missing". Later review work also challenges
whether its fitted `beta` window probes a far field.

The source here is the density of the lowest eigenstate of `H = -t A + V`,
with `V` the self-consistent field of that same density.  The source sign is
fixed per operator so that every operator produces a non-positive well.  This
is an explicit comparison convention, not a derived physical sign rule.

Two finite-volume diagnostics are measured at fixed coupling as the box grows:

  (1) the RMS extent of rho;
  (2) the absolute well depth D_N = -min(V), with the Dirichlet boundary
      fixing V = 0.

The runner compares the finite sequences with two equal-parameter descriptive
models, `a + c/M` and `a + b M`.  It does not prove an infinite-volume limit
and it does not identify `D_N` with a physical binding energy.

Every number is computed here.  No observed value, fitted selector, literature
constant, or empirical comparator enters any row.  No new axiom and no new
framework primitive is used.

Usage:
  python3 scripts/physical_poisson_self_consistent_well_depth_finite_volume_2026_07_27.py
"""
from __future__ import annotations

import functools
import os
import subprocess
import sys
import time

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh, splu

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import frontier_self_consistent_field_equation as F  # noqa: E402

T_HOP = 1.0
FIX_LO, FIX_HI = 4.0, 10.0        # fixed exterior comparison window
MU2 = 0.25                        # the parent runner's own screening value
MATCHED_TOL = 2e-9                # odd-centred matched solves reach this floor

RESULTS: list[tuple[str, bool, str]] = []


def record(tag: str, ok: bool, detail: str) -> None:
    RESULTS.append((tag, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {detail}")


def passed(*tags: str) -> bool:
    """Return whether every named result has already recorded PASS."""
    state = {tag: ok for tag, ok, _ in RESULTS}
    return all(state.get(tag, False) for tag in tags)


# --------------------------------------------------------------- construction
def make_operator(N: int, which: str):
    """Factorize `Op` for `Op phi = rho` on the Dirichlet interior."""
    A, M = F.build_laplacian_sparse(N)
    if which == "poisson":
        Op = A
    elif which == "biharmonic":
        Op = (A @ A).tocsc()
    elif which == "screened":
        Op = A - MU2 * sparse.eye(A.shape[0])
    elif which == "local":
        Op = -sparse.eye(A.shape[0])
    else:
        raise ValueError(which)
    return A, M, splu(Op.tocsc())


@functools.lru_cache(maxsize=None)
def self_consistent(N: int, which: str, g: float, n_iter: int = 300,
                    mixing: float = 0.4, tol: float = 1e-10):
    """Ground state of `H = -t A + V` with `Op phi = s g rho`, `V = phi <= 0`.

    `s` is chosen once, from the sign of `sum(phi)` on the first iterate, so
    that every operator -- whatever its definiteness -- produces an attractive
    well.  The parent runner instead used one fixed negative source for
    operators of opposite definiteness, which is the convention-dependence the
    ledger row names.
    """
    A, M, lu = make_operator(N, which)
    H_kin = (-T_HOP * A).tocsc()
    ax = np.arange(M)
    coords = np.stack(np.meshgrid(ax, ax, ax, indexing="ij"), -1)
    coords = coords.reshape(-1, 3).astype(float)

    V = np.zeros(M ** 3)
    sign = None
    change = np.inf
    v0 = np.ones(M ** 3, dtype=float)
    v0 /= np.linalg.norm(v0)
    for it in range(n_iter):
        eps, vec = eigsh((H_kin + sparse.diags(V)).tocsc(), k=1, which="SA",
                         tol=1e-11, v0=v0)
        v0 = vec[:, 0]
        rho = np.abs(vec[:, 0]) ** 2
        phi = lu.solve(rho)
        if sign is None:
            sign = -1.0 if phi.sum() > 0 else 1.0
        V_new = g * sign * phi
        change = float(np.max(np.abs(V_new - V)))
        V = (1 - mixing) * V + mixing * V_new
        if change < tol:
            break

    com = (coords * rho[:, None]).sum(0) / rho.sum()
    r = np.sqrt(((coords - com) ** 2).sum(1))
    rms = float(np.sqrt(((r ** 2) * rho).sum() / rho.sum()))
    return dict(M=M, V=V, rho=rho, r=r, com=com, coords=coords, lu=lu,
                sign=sign, g=g, rms=rms, depth=float(-V.min()),
                Vmax=float(V.max()), E0=float(eps[0]), it=it + 1,
                change=change, conv=bool(change < tol))


def fit_models(Ms, ys):
    """Least squares for `a + c/M` (bounded) and `a + b*M` (linear).

    Returns (bounded_intercept_a, rss_bounded, slope_b, rss_linear).
    """
    Ms = np.asarray(Ms, float)
    ys = np.asarray(ys, float)
    ab = np.linalg.lstsq(np.c_[np.ones_like(Ms), 1.0 / Ms], ys, rcond=None)[0]
    rb = float(np.sum((ys - (ab[0] + ab[1] / Ms)) ** 2))
    al = np.linalg.lstsq(np.c_[np.ones_like(Ms), Ms], ys, rcond=None)[0]
    rl = float(np.sum((ys - (al[0] + al[1] * Ms)) ** 2))
    return float(ab[0]), rb, float(al[1]), rl


def gaussian_source(M: int, width: float = 1.0) -> np.ndarray:
    """Unit total mass, fixed extent, independent of the box."""
    ax = np.arange(M)
    c = np.stack(np.meshgrid(ax, ax, ax, indexing="ij"), -1).reshape(-1, 3)
    rho = np.exp(-((c - (M - 1) / 2.0) ** 2).sum(1) / (2 * width ** 2))
    return rho / rho.sum()


def symbol(N: int) -> np.ndarray:
    k = 2 * np.pi * np.fft.fftfreq(N)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    return 2 * (np.cos(kx) + np.cos(ky) + np.cos(kz)) - 6.0


# ---------------------------------------------------------------------- rows
def row_P0():
    """The imported parent modules are the committed ones, not local edits."""
    print("\nP0  provenance")
    try:
        det = []
        ok = True
        for rel in ("scripts/frontier_self_consistent_field_equation.py",):
            blob = subprocess.run(
                ["git", "-C", HERE, "rev-parse", f"HEAD:{rel}"],
                capture_output=True, text=True, check=True).stdout.strip()
            live = subprocess.run(
                ["git", "-C", HERE, "hash-object",
                 os.path.join(os.path.dirname(HERE), rel)],
                capture_output=True, text=True, check=True).stdout.strip()
            ok = ok and blob == live and len(blob) == 40
            det.append(f"{os.path.basename(rel)} {blob[:12]}"
                       f"{'' if blob == live else f' != working {live[:12]}'}")
        record("P0", ok,
               "the imported parent module matches its committed blob, so "
               "every row below is measured against the tree as landed: "
               + "; ".join(det))
    except Exception as exc:  # noqa: BLE001
        record("P0", False, f"could not verify the committed blobs: {exc}")


def row_R0():
    """Sign normalization: every operator is handed an attractive well."""
    print("\nR0  source-sign normalization")
    bad = []
    for which, g in (("poisson", 50.0), ("biharmonic", 10.0),
                     ("screened", 100.0), ("local", 100.0)):
        s = self_consistent(16, which, g)
        if not s["conv"]:
            bad.append(f"{which} did not converge")
        if s["Vmax"] > 1e-12:
            bad.append(f"{which} max(V)={s['Vmax']:.3e}")
    record("R0", not bad,
           "all four operators produce V <= 0 everywhere on the interior"
           if not bad else "; ".join(bad))

def row_R3_R4():
    """Poisson: report finite-volume extent and absolute-depth trends."""
    print("\nR3/R4  Poisson -- extent and well depth against the box")
    out = {}
    all_conv = True
    for g, sizes in ((20.0, (12, 20, 28, 36, 44, 52)),
                     (50.0, (12, 16, 20, 24, 32, 40, 48))):
        Ms, rms, dep = [], [], []
        for N in sizes:
            s = self_consistent(N, "poisson", g)
            Ms.append(float(s["M"]))
            rms.append(s["rms"])
            dep.append(s["depth"])
            all_conv = all_conv and s["conv"]
            print(f"      g={g:5.1f} N={N:3d}  rms={s['rms']:8.4f}  "
                  f"depth={s['depth']:8.4f}  iters={s['it']:3d}")
        out[g] = (Ms, rms, dep)

    # convergence is a statement about the increments, not about the spread
    # across a sequence that is still moving at its small-box end
    det, ok = [], True
    for g in (20.0, 50.0):
        s = out[g][1]
        incs = [abs(s[i + 1] - s[i]) / s[i + 1] for i in range(len(s) - 1)]
        ok = (ok and all_conv and incs[-1] < 1e-3
              and incs[-1] < incs[0] / 100.0)
        det.append(f"g={g:.0f}: {s[0]:.4f} -> {s[-1]:.4f}, relative step "
                   f"{incs[0]:.2e} -> {incs[-1]:.2e}")
    record("R3", ok,
           "the finite-size extent increments fall by "
           "more than two orders of magnitude and end below 1e-3 -- "
           + "; ".join(det) + "; no infinite-volume limit is claimed")

    Ms20, _, dep20 = out[20.0]
    intercept20, rb20, _, rl20 = fit_models(Ms20, dep20)
    _, rb20_tail, _, rl20_tail = fit_models(Ms20[-4:], dep20[-4:])
    Ms50, _, dep50 = out[50.0]
    intercept50, rb50, _, rl50 = fit_models(Ms50, dep50)
    ok = (all_conv and rb50 < rl50 and intercept50 > 0
          and rb20 < rl20 and rl20_tail < rb20_tail)
    record("R4", ok,
           f"for g=50 the full finite-size depth sequence prefers a+c/M "
           f"(a={intercept50:.4f}, rss {rb50:.2e}) over a+b*M "
           f"(rss {rl50:.2e}); "
           f"g=20 is explicitly inconclusive because its full sequence prefers "
           f"a+c/M (a={intercept20:.4f}, rss {rb20:.2e} vs {rl20:.2e}) "
           f"but its last "
           f"four sizes prefer the linear model ({rl20_tail:.2e} vs "
           f"{rb20_tail:.2e}); no limit is inferred")


def row_R5():
    """Biharmonic: finite-volume extent and absolute-depth trends."""
    print("\nR5  biharmonic -- finite-volume extent and depth trends")
    Ms, rms, dep = [], [], []
    all_conv = True
    for N in (12, 16, 20, 24, 28, 32):
        s = self_consistent(N, "biharmonic", 10.0)
        Ms.append(float(s["M"]))
        rms.append(s["rms"])
        dep.append(s["depth"])
        all_conv = all_conv and s["conv"]
        print(f"      N={N:3d}  rms={s['rms']:8.4f}  depth={s['depth']:8.4f}  "
              f"iters={s['it']:3d}")
    _, rb, slope, rl = fit_models(Ms, dep)
    record("R5", all_conv and rl < rb and slope > 0.05,
           f"the extent stays in the narrow range "
           f"{min(rms):.4f}-{max(rms):.4f} over the tested boxes, while the "
           f"absolute depth runs "
           f"{dep[0]:.4f} -> {dep[-1]:.4f} and fits a + b*M with "
           f"b = {slope:.4f} per interior site (linear rss {rl:.2e} beats "
           f"a+c/M rss {rb:.2e}); this is a finite-range model comparison, "
           f"not a proof of divergence")


def row_R6_R7():
    """Isolate the kernel: prescribed source, no self-consistency."""
    print("\nR6/R7  a PRESCRIBED unit source of fixed extent -- kernel only")
    sizes_d = (12, 20, 28, 36)
    rows = {}
    for which in ("poisson", "biharmonic", "screened", "local"):
        vals = []
        for N in sizes_d:
            _, M, lu = make_operator(N, which)
            vals.append(float(np.abs(lu.solve(gaussian_source(M))).max()))
        rows[which] = vals
        print(f"      Dirichlet {which:>11s}: " +
              " ".join(f"{v:9.5f}" for v in vals))
    Ms = [float(n - 2) for n in sizes_d]
    verdicts = {}
    for which, vals in rows.items():
        _, rb, slope, rl = fit_models(Ms, vals)
        verdicts[which] = (rl < rb and slope > 1e-4)
    record("R6", (verdicts["biharmonic"] and not verdicts["poisson"]
                  and not verdicts["screened"] and not verdicts["local"]),
           f"with self-consistency removed entirely, the same split appears: "
           f"biharmonic's peak |phi| runs "
           f"{rows['biharmonic'][0]:.4f} -> {rows['biharmonic'][-1]:.4f} and "
           f"is fit by the linear family, while poisson "
           f"({rows['poisson'][0]:.4f} -> {rows['poisson'][-1]:.4f}), screened "
           f"({rows['screened'][0]:.4f} -> {rows['screened'][-1]:.4f}) and "
           f"local ({rows['local'][0]:.4f} -> {rows['local'][-1]:.4f}) are fit "
           f"by a+c/M over these sizes -- the linear trend does not require "
           f"the nonlinear fixed point")

    sizes_t = (16, 24, 32, 48, 64, 96)
    tor = {}
    for which, p, mu2 in (("poisson", 1, 0.0), ("biharmonic", 2, 0.0),
                          ("screened", 1, MU2)):
        vals = []
        for N in sizes_t:
            sym = (symbol(N) - mu2) ** p
            rh = np.fft.fftn(gaussian_source(N).reshape(N, N, N))
            out = np.zeros_like(rh)
            nz = np.abs(sym) > 1e-13
            out[nz] = rh[nz] / sym[nz]
            phi = np.real(np.fft.ifftn(out))
            vals.append(float(np.abs(phi - phi.mean()).max()))
        tor[which] = vals
        print(f"      torus     {which:>11s}: " +
              " ".join(f"{v:9.5f}" for v in vals))
    Nt = [float(n) for n in sizes_t]
    _, rb_b, sl_b, rl_b = fit_models(Nt, tor["biharmonic"])
    intercept_p, rb_p, _, rl_p = fit_models(Nt, tor["poisson"])
    record("R7", rl_b < rb_b and sl_b > 1e-3 and rb_p < rl_p,
           f"on a boundary-free torus with the zero mode removed the same "
           f"holds -- biharmonic {tor['biharmonic'][0]:.4f} -> "
           f"{tor['biharmonic'][-1]:.4f}, linear in N (b = {sl_b:.4f}); "
           f"poisson {tor['poisson'][0]:.4f} -> {tor['poisson'][-1]:.4f}, "
           f"preferring a+c/N with fitted a={intercept_p:.4f}; the observed "
           f"biharmonic growth is therefore not specific to the Dirichlet wall")


def row_R8_R9():
    """Report the local zero-start discontinuity and screened finite trends."""
    print("\nR8/R9  the other two members of the parent note's family")
    loc = []
    local_conv = True
    for N in (12, 16, 20, 24, 28):
        s = self_consistent(N, "local", 100.0)
        loc.append(s["rms"])
        local_conv = local_conv and s["conv"]
        print(f"      local    g=100 N={N:3d}  rms={s['rms']:8.4f}  "
              f"depth={s['depth']:9.4f}")
    record("R8", local_conv and max(loc) / max(min(loc), 1e-12) > 10.0,
           f"the identical V=0-start protocol is discontinuous across the "
           f"finite-size sweep: the converged extent jumps {min(loc):.4f} -> "
           f"{max(loc):.4f}; this sampled sweep does not exhibit a smooth "
           f"local-operator continuation, without proving "
           f"fixed-N bistability")

    Ms, rms, dep = [], [], []
    screened_conv = True
    for N in (12, 16, 20, 24, 28):
        s = self_consistent(N, "screened", 100.0)
        Ms.append(float(s["M"]))
        rms.append(s["rms"])
        dep.append(s["depth"])
        screened_conv = screened_conv and s["conv"]
        print(f"      screened g=100 N={N:3d}  rms={s['rms']:8.4f}  "
              f"depth={s['depth']:9.4f}")
    intercept, rb, _, rl = fit_models(Ms, dep)
    record("R9", screened_conv and (max(rms) - min(rms) < 1e-4) and rb < rl,
           f"over the tested boxes screened Poisson has extent "
           f"{np.mean(rms):.4f} (spread {max(rms) - min(rms):.1e}), depth "
           f"{dep[0]:.4f} -> {dep[-1]:.4f}, and the depth sequence prefers "
           f"a+c/M with fitted a={intercept:.4f}; the finite well-depth "
           f"diagnostic "
           f"does not single out unscreened Poisson")


def row_R10_R11_R12():
    """Matched-source localization check under the already supplied solver."""
    print("\nR10/R11/R12  matched point-source kernel, same operator, same "
          f"boundary condition, window [{FIX_LO:.0f},{FIX_HI:.0f}]")

    def matched(which, g, N):
        s = self_consistent(N, which, g, tol=MATCHED_TOL)
        pt = np.zeros(s["M"] ** 3)
        j = int(np.argmin(np.sum((s["coords"] - s["com"]) ** 2, axis=1)))
        pt[j] = 1.0
        V_pt = s["g"] * s["sign"] * s["lu"].solve(pt)
        m = (s["r"] >= FIX_LO) & (s["r"] <= FIX_HI) & (np.abs(V_pt) > 1e-300)
        off = float(np.sqrt(((s["coords"][j] - s["com"]) ** 2).sum()))
        return s, s["V"][m] / V_pt[m], s["r"][m], off

    # An odd interior width M puts the centre of the box -- and so the centroid
    # of a centred state -- exactly ON a lattice site, so the comparison point
    # source sits where the mass actually is.  An even M leaves it half a
    # spacing off in each axis.  R11 measures what that costs.
    meds, convs = [], []
    for N in (25, 33, 41, 49):
        s, ratio, _, off = matched("poisson", 50.0, N)
        convs.append(s["conv"])
        meds.append(float(np.median(ratio)))
        print(f"      poisson    N={N:3d} M={s['M']:3d}  rms={s['rms']:7.4f}  "
              f"site offset={off:6.4f}  median ratio={meds[-1]:9.5f}  "
              f"scatter={np.std(ratio):8.2e}  residual={s['change']:.2e}")
    record("R10", all(convs) and all(abs(x - 1.0) < 1e-3 for x in meds),
           f"over the tested exterior window, the self-consistent Poisson "
           f"field's median ratio to the matched point-source field of the "
           f"same operator lies in {min(meds):.5f}-{max(meds):.5f} across "
           f"N=25..49 (maximum deviation "
           f"{max(abs(x - 1) for x in meds):.2e}); this finite localization "
           f"check uses the already chosen field solver and is not the parent "
           f"transfer propagator's susceptibility")

    print("      parity control -- the same comparison with the centroid "
          "between sites instead of on one:")
    par, par_conv = {}, []
    for N in (24, 25, 32, 33):
        s, ratio, rr, off = matched("poisson", 50.0, N)
        par_conv.append(s["conv"])
        par[N] = (off, float(np.median(ratio)), float(np.std(ratio)),
                  float(np.abs(ratio - 1).mean()))
        print(f"      poisson    N={N:3d} M={s['M']:3d} "
              f"({'odd ' if s['M'] % 2 else 'even'})  site offset={off:6.4f}  "
              f"median={par[N][1]:9.5f}  scatter={par[N][2]:8.2e}  "
              f"residual={s['change']:.2e}")
    gain = (par[24][3] / par[25][3], par[32][3] / par[33][3])
    # "on site" is limited by the eigensolver tolerance, not by exact symmetry,
    # so the bound is loose; it only has to separate 0 from sqrt(3)/2
    on_site = par[25][0] < 1e-3 and par[33][0] < 1e-3
    off_site = par[24][0] > 0.5 and par[32][0] > 0.5
    record("R11", all(par_conv) and min(gain) > 30.0 and on_site and off_site,
           f"the even-width residual is strongly reduced when the comparison "
           f"point source is aligned with the centroid: moving it from "
           f"half a spacing off in each axis (offset {par[24][0]:.4f}) to "
           f"exactly on a site (offset {par[25][0]:.4f}) shrinks the mean "
           f"absolute deviation by a factor {gain[0]:.0f} at N=24 vs 25 and "
           f"{gain[1]:.0f} at N=32 vs 33, and the median ratio moves "
           f"{par[24][1]:.5f} -> {par[25][1]:.5f} and "
           f"{par[32][1]:.5f} -> {par[33][1]:.5f}")

    det = []
    other_ok = True
    for which, g in (("biharmonic", 10.0), ("screened", 100.0)):
        matches = [matched(which, g, N) for N in (25, 33, 41)]
        ms = [float(np.median(item[1])) for item in matches]
        other_ok = (other_ok and all(item[0]["conv"] for item in matches)
                    and all(0.90 < value < 1.05 for value in ms))
        det.append(f"{which} {min(ms):.5f}-{max(ms):.5f}")
    record("R12", other_ok,
           "the same matched comparison for the other two operators that have "
           "an extended field: " + "; ".join(det) +
           " (scored only as a broad 0.90-1.05 localization check on converged "
           "fixed points; it is not the operator discriminator)")


def row_R14():
    """Test whether changing the potential reference changes the comparison.

    Referencing the potential to a fixed radius rather than to the well bottom
    tests whether the apparent separation survives a change of observable. A
    kernel growing like `r` has box-dependent values and box-independent
    differences, so the claim must distinguish absolute well depth from local
    field differences.
    """
    print("\nR14  reference the potential to a fixed radius instead of to the "
          "well bottom")
    verdict = {}
    all_conv = True
    for which, g, sizes in (("poisson", 50.0, (24, 32, 40)),
                            ("biharmonic", 10.0, (24, 32, 40)),
                            ("screened", 100.0, (24, 32, 40))):
        Ms, dv, depth = [], [], []
        for N in sizes:
            s = self_consistent(N, which, g)
            all_conv = all_conv and s["conv"]
            inner = s["V"][(s["r"] >= 4.0) & (s["r"] < 5.0)].mean()
            outer = s["V"][(s["r"] >= 9.0) & (s["r"] < 10.0)].mean()
            Ms.append(float(s["M"]))
            dv.append(float(outer - inner))
            depth.append(s["depth"])
        intercept, rb, slope, rl = fit_models(Ms, dv)
        _, rb_depth, depth_slope, rl_depth = fit_models(Ms, depth)
        verdict[which] = {
            "difference_prefers_bounded": rb < rl,
            "difference": dv,
            "depth": depth,
            "difference_bounded_intercept": intercept,
            "difference_slope": slope,
            "depth_prefers_linear": rl_depth < rb_depth,
            "depth_slope": depth_slope,
        }
        print(f"      {which:>11s}  C_N: " +
              " ".join(f"{v:9.5f}" for v in dv) +
              f"   depth: " + " ".join(f"{v:8.4f}" for v in depth))

    bi_bounded = verdict["biharmonic"]["difference_prefers_bounded"]
    other_bounded = all(
        verdict[name]["difference_prefers_bounded"]
        for name in ("poisson", "screened")
    )
    bi_depth_linear = verdict["biharmonic"]["depth_prefers_linear"]
    record("R14", all_conv and bi_bounded and other_bounded and bi_depth_linear,
           f"the observable choice matters: across the same boxes the "
           f"biharmonic shell contrast C_N over the fixed window runs "
           f"{verdict['biharmonic']['difference'][0]:.5f} -> "
           f"{verdict['biharmonic']['difference'][-1]:.5f} and is fit by the "
           f"{'bounded' if bi_bounded else 'linear'} family, while its well "
           f"depth runs {verdict['biharmonic']['depth'][0]:.4f} -> "
           f"{verdict['biharmonic']['depth'][-1]:.4f} and prefers the linear "
           f"model; the finite-volume separation is about absolute well depth "
           f"under the Dirichlet-zero reference, not the shell contrast "
           f"(poisson C_N {verdict['poisson']['difference'][0]:.5f} -> "
           f"{verdict['poisson']['difference'][-1]:.5f}, screened "
           f"{verdict['screened']['difference'][0]:.5f} -> "
           f"{verdict['screened']['difference'][-1]:.5f})")


def row_thesis():
    print("\nTHESIS")
    required = ("P0", "R0", "R3", "R4", "R5", "R6", "R7", "R8", "R9",
                "R10", "R11", "R12", "R14")
    record("T", passed(*required),
           "On the supplied four-operator family and Dirichlet lattice, with "
           "the source sign normalized so no operator is handed a repulsive "
           "well, the tested finite-volume sequences produce converged "
           "self-consistent states. At the scored couplings, Poisson g=50 and "
           "screened Poisson prefer a+c/M for absolute well depth, biharmonic "
           "prefers a+b*M, and the local V=0-start sweep is discontinuous. "
           "These are finite-range model preferences under an explicit "
           "potential reference, not proofs of limits, physical binding "
           "energies, operator uniqueness, or the parent susceptibility bridge.")


def main():
    t0 = time.time()
    print("=" * 78)
    print("FINITE-VOLUME SELF-CONSISTENT LOCALIZATION AND")
    print("ABSOLUTE-WELL-DEPTH MODEL COMPARISONS")
    print("=" * 78)
    row_P0()
    row_R0()
    row_R3_R4()
    row_R5()
    row_R6_R7()
    row_R8_R9()
    row_R10_R11_R12()
    row_R14()
    row_thesis()

    npass = sum(1 for _, ok, _ in RESULTS if ok)
    nfail = len(RESULTS) - npass
    print("\n" + "=" * 78)
    print(f"SUMMARY: SELF-CONSISTENT WELL DEPTH PASS={npass} FAIL={nfail}")
    print(f"elapsed {time.time() - t0:.1f}s")
    print("=" * 78)
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
