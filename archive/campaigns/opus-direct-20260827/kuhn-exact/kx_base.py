"""kx_base.py -- shared plumbing for the Kuhn-exact instrument (R132 applied to the
simplicial operator).

Everything the lattice side needs comes from `conformal/recheck/kuhn.py`, used as a
black box:  build() -> stencil/mass/C,  _bands()/bloch_eigs() -> spectrum.
Everything the continuum side needs comes from opus_t205 (analytic b1,b2) and
opus_t206 (exact continuum heat trace by plane-wave diagonalisation).

Channels, in the P-vector convention of kuhn.py  (g_mu mu = 1 + eps P_mu cos(kk x0)):
    CONFORMAL     P = (1, 1, 1, 1)      <-> opus_t206 chan {0:1,1:1,2:1,3:1}
    TRACELESS-TT  P = (0, 1,-1, 0)      <-> opus_t206 chan {1:1,2:-1}
"""
import os, sys, math, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # .../opus-direct-20260827
RECHECK = os.path.join(ROOT, "conformal", "recheck")
for p in (RECHECK, ROOT):
    if p not in sys.path:
        sys.path.insert(0, p)

import kuhn                                        # noqa: E402
from kuhn import build, _bands, bloch_eigs, dense_eigs, gdiag   # noqa: E402
from kuhn import flat_lattice_trace, flat_exact_trace           # noqa: E402

CH_P = {"CONFORMAL":    np.array([1.0, 1.0, 1.0, 1.0]),
        "TRACELESS-TT": np.array([0.0, 1.0, -1.0, 0.0])}
CH_T206 = {"CONFORMAL":    {0: 1, 1: 1, 2: 1, 3: 1},
           "TRACELESS-TT": {1: 1, 2: -1}}

N_MODE = 2
H_EPS = 0.05
XS = np.array([0.4, 0.6, 0.8, 1.0, 1.4, 2.0])


# ------------------------------------------------------------------ momentum orbits
import itertools as _it


def momentum_orbits(L, full_perm):
    """Transverse momenta (2 pi/L)*(j1,j2,j3) reduced by the symmetries VERIFIED
    numerically in c2_symmetry.py:

        j -> -j   (mod L)                     always  (K real => K^{-q} = conj K^q)
        permutations of (j1,j2,j3)            only when P_1 = P_2 = P_3 (conformal)
        transposition (j1 j2) only            for TRACELESS-TT  (the 1<->2 coordinate
                                              swap sends eps -> -eps, itself a shift)

    The single-axis reflection j_i -> -j_i is NOT a symmetry of the Kuhn complex
    (c2_symmetry.py measures a 1e-2 spectral mismatch); it is deliberately not used.
    Returns (qs (m,3), mult (m,)) with sum(mult) = L^3.
    """
    j = np.arange(L, dtype=np.int64)
    J = np.stack(np.meshgrid(j, j, j, indexing='ij'), axis=-1).reshape(-1, 3)
    perms = list(_it.permutations(range(3))) if full_perm else [(0, 1, 2), (1, 0, 2)]
    code = None
    for pm in perms:
        for sgn in (1, -1):
            Y = (sgn * J[:, list(pm)]) % L
            c = (Y[:, 0] * L + Y[:, 1]) * L + Y[:, 2]
            code = c if code is None else np.minimum(code, c)
    reps, mult = np.unique(code, return_counts=True)
    q = np.stack([reps // (L * L), (reps // L) % L, reps % L], axis=-1).astype(float)
    return q * (2 * np.pi / L), mult.astype(float)


# ------------------------------------------------------------------ lattice trace
def lat_trace(L, P, eps, n, svals, improve, chunk=None, use_sym=True, verbose=False):
    """Tr exp(-s Delta) for the Kuhn operator, both improved and plain.
    Returns array over svals."""
    if chunk is None:                 # cap the (chunk, L, L) complex batch at ~128 MB
        chunk = max(32, int(8.0e6 / (L * L)))
    kk = 2 * math.pi * n / L
    r = build(L, eps, P, kk, cpoint='vertex')
    bands = _bands(L, r['stencil'])
    C = r['C']
    if use_sym:
        full_perm = (abs(P[1] - P[2]) < 1e-15 and abs(P[2] - P[3]) < 1e-15)
        if not full_perm:
            # the (1 2) swap is a symmetry only because it is equivalent to eps -> -eps,
            # i.e. the shift x0 -> x0 + L/(2n), which must be an integer number of sites.
            # (c2_symmetry: at L=10, n=2 the reduction is wrong by 2e-9.)
            assert L % (2 * n) == 0, f"swap12 reduction invalid for L={L}, n={n}"
        qs, mult = momentum_orbits(L, full_perm)
    else:
        qs = kuhn.all_momenta(L)
        mult = np.ones(len(qs))
    sv = np.asarray(svals, float)
    acc = np.zeros(len(sv))
    hmax = 0.0
    t0 = time.time()
    for i in range(0, len(qs), chunk):
        q = qs[i:i + chunk]
        w = mult[i:i + chunk]
        ev, herm = bloch_eigs(L, bands, r['mass'], q, C=(C if improve else None),
                              improve=improve)
        hmax = max(hmax, herm)
        for jj, s in enumerate(sv):
            acc[jj] += float(w @ np.exp(-s * ev).sum(axis=1))
        if verbose and i == 0:
            el = time.time() - t0
            print(f"      [chunk {el:.1f}s -> ~{el*len(qs)/len(q):.0f}s total]", flush=True)
    return acc, dict(vol=r['vol'], mass=r['mass'], herm=hmax, nq=len(qs),
                     wt=float(mult.sum()), sec=time.time() - t0)


def e2_sym(fn, h=H_EPS):
    """eps^2 Taylor coefficient by the 5-point central difference, using the EXACT
    parity f(-e) = f(e) that holds for both channels (verified in c3_parity.py):
    only e = 0, h, 2h are evaluated."""
    v0, v1, v2 = fn(0.0), fn(h), fn(2 * h)
    d2 = (-2 * v2 + 32 * v1 - 30 * v0) / (12 * h * h)
    return 0.5 * d2


def e2_full(fn, h=H_EPS):
    v = {e: fn(e * h) for e in (-2, -1, 0, 1, 2)}
    return 0.5 * (-v[2] + 16 * v[1] - 30 * v[0] + 16 * v[-1] - v[-2]) / (12 * h * h)


def fmt(a, w=9, p=5):
    return " ".join(f"{q:{w}.{p}f}" for q in np.atleast_1d(a))


def fmte(a, w=10, p=3):
    return " ".join(f"{q:{w}.{p}e}" for q in np.atleast_1d(a))
