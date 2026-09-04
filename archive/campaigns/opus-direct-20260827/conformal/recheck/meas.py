"""meas.py -- the bridge measurement:

    ratio(s) = [ (4 pi s)^2 (K_pert(s) - K_flat(s)) - dVol ] / ( s dS_Regge / 3 )

K(s) = Tr exp(-s Delta_imp), Delta_imp = Delta + Delta C Delta / 24, C = diag(tr g / 4).
Both K's come from the identical Bloch pipeline; eigenvalues are paired by rank inside
each Bloch block before subtracting, so the cancellation is done in the small numbers.
"""
import math, itertools, time
import numpy as np
from kuhn import build, _bands, bloch_eigs, all_momenta
import cont


def heat_diff(L, eps, P, n, svals, chunk=1024, cpoint='vertex', cov=True, improve=True,
              verbose=False):
    kk = 2 * math.pi * n / L
    rp = build(L, eps, P, kk, cpoint=cpoint)
    rf = build(L, 0.0, P, kk, cpoint=cpoint)
    bp, bf = _bands(L, rp['stencil']), _bands(L, rf['stencil'])
    Cp = rp['C'] if cov else None
    Cf = rf['C'] if cov else None
    qs = all_momenta(L)
    sv = np.asarray(svals, dtype=float)
    acc = np.zeros(len(sv))
    t0 = time.time()
    for i in range(0, len(qs), chunk):
        q = qs[i:i + chunk]
        ep, h1 = bloch_eigs(L, bp, rp['mass'], q, C=Cp, improve=improve)
        ef, h2 = bloch_eigs(L, bf, rf['mass'], q, C=Cf, improve=improve)
        ep = np.sort(ep, axis=1)
        ef = np.sort(ef, axis=1)
        for j, s in enumerate(sv):
            acc[j] += float(np.sum(np.exp(-s * ep) - np.exp(-s * ef)))
        if verbose and i == 0:
            print(f"      [{(time.time()-t0):.1f}s/chunk -> ~{(time.time()-t0)*len(qs)/chunk:.0f}s]",
                  flush=True)
    return acc, rp, rf, time.time() - t0


def lda(L, eps, P, n, svals):
    """Local-density (zero-gradient) lattice artifact.  For a UNIFORM diagonal metric f
    the Kuhn symbol is exactly D_f(k) = sum_mu 2(1-cos k_mu)/f_mu (verified in T2c) and
    the improved symbol is D_f + (sum f)/96 D_f^2.  Its heat trace per site differs from
    the continuum sqrt(det f)/(4 pi s)^2 by a pure lattice error delta(s;f) that contains
    no curvature.  Summing delta(s;f(x0)) - delta(s;1) over x0 removes the zero-gradient
    part of the discretisation error and cannot touch the O(s) Regge term."""
    kk = 2 * math.pi * n / L
    sv = np.asarray(svals, float)
    nn = np.arange(L)
    d1 = 2 * (1 - np.cos(2 * np.pi * nn / L))
    v, inv = np.unique(np.round(d1, 13), return_inverse=True)
    w = np.bincount(inv).astype(float)
    Wt = (w[:, None, None, None] * w[None, :, None, None]
          * w[None, None, :, None] * w[None, None, None, :]).ravel()

    def delta(f):
        D = (v[:, None, None, None] / f[0] + v[None, :, None, None] / f[1]
             + v[None, None, :, None] / f[2] + v[None, None, None, :] / f[3]).ravel()
        X = D + (float(np.sum(f)) / 96.0) * D * D
        sd = math.sqrt(float(np.prod(f)))
        return np.array([(4 * math.pi * s) ** 2 * float(Wt @ np.exp(-s * X)) / L ** 4 - sd
                         for s in sv])

    from kuhn import gdiag
    d0 = delta(np.ones(4))
    tot = np.zeros(len(sv))
    cache = {}
    for x0 in range(L):
        f = np.array([0.5 * (gdiag(x0 - 0.5, eps, P, kk)[0] + gdiag(x0 + 0.5, eps, P, kk)[0])]
                     + [gdiag(x0, eps, P, kk)[m] for m in (1, 2, 3)])
        key = tuple(np.round(f, 12))
        if key not in cache:
            cache[key] = delta(f)
        tot += cache[key] - d0
    return tot * L ** 3


def report(L, P, name, eps=0.05, n=1, svals=None, chunk=1024, cpoint='vertex',
           cov=True, improve=True, verbose=False, do_lda=True):
    kk = 2 * math.pi * n / L
    acc, rp, rf, el = heat_diff(L, eps, P, n, svals, chunk=chunk, cpoint=cpoint,
                                cov=cov, improve=improve, verbose=verbose)
    sv = np.asarray(svals, float)
    F = (4 * math.pi * sv) ** 2 * acc
    dV = rp['vol'] - rf['vol']
    dS = rp['S'] - rf['S']
    Vc, Sc, Ia2 = cont.integrals(L, eps, P, kk)
    Vc0, Sc0, _ = cont.integrals(L, 0.0, P, kk)
    dVc = Vc - Vc0
    A = lda(L, eps, P, n, sv) if do_lda else np.zeros(len(sv))
    print(f"=== L={L} n={n} eps={eps} c={'tr g/96' if cov else '1/24'} "
          f"{'improved' if improve else 'UNimproved'}   {name}   [{el:.0f}s]")
    print(f"    dVol_simplicial = {dV:.5f}   dVol_continuum = {dVc:.5f}  "
          f"(rel diff {dV/dVc-1:+.3e})")
    print(f"    dS_Regge        = {dS:.5f}   S_continuum    = {Sc-Sc0:.5f}  "
          f"(rel diff {dS/(Sc-Sc0)-1:+.3e})     Int a2 = {Ia2:.5f}")
    print("       s    (4pi s)^2 dK        raw ratio    -a2      -LDA    -a2-LDA   "
          "raw w/ cont.dVol")
    for j, s in enumerate(sv):
        den = s * dS / 3.0
        print(f"   {s:6.1f} {F[j]:16.5f}   {(F[j]-dV)/den:10.5f} {(F[j]-dV-s*s*Ia2)/den:9.5f} "
              f"{(F[j]-dV-A[j])/den:9.5f} {(F[j]-dV-A[j]-s*s*Ia2)/den:9.5f} "
              f"{(F[j]-dVc)/den:12.5f}")
    return dict(s=sv, F=F, dV=dV, dS=dS, dVc=dVc, Ia2=Ia2, lda=A, dSc=Sc - Sc0)


def fits(r, lo, hi, label=""):
    s, F, dV, dS = r['s'], r['F'], r['dV'], r['dS']
    m = (s >= lo) & (s <= hi)
    out = {}
    X = np.vstack([s[m], s[m] ** 2]).T
    c, *_ = np.linalg.lstsq(X, (F - dV)[m], rcond=None)
    out['fixed_dV'] = 3 * c[0] / dS
    X = np.vstack([np.ones(m.sum()), s[m], s[m] ** 2]).T
    c, *_ = np.linalg.lstsq(X, F[m], rcond=None)
    out['free_A'] = 3 * c[1] / dS
    out['A/dV'] = c[0] / dV
    out['A/dVc'] = c[0] / r['dVc']
    X = np.vstack([np.ones(m.sum()), s[m], s[m] ** 2, 1.0 / s[m]]).T
    c, *_ = np.linalg.lstsq(X, F[m], rcond=None)
    out['free_A_1os'] = 3 * c[1] / dS
    print(f"    fit s in [{lo:g},{hi:g}] {label}: 3B/dS  fixed-dVol {out['fixed_dV']:.4f} | "
          f"free-A {out['free_A']:.4f} (A/dVol_simp {out['A/dV']:.6f}, A/dVol_cont "
          f"{out['A/dVc']:.6f}) | free-A+1/s {out['free_A_1os']:.4f}")
    return out
