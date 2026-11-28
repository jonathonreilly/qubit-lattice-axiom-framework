#!/usr/bin/env python3
"""K1 of CRITERIA.md: the lift kernel K(y, x') at U = 1, d = 4. Args: L Np [ell_inner]. ell_inner = 1: fine = level k; 3: composite, fine three
per level-k side, L must then be 3 and the block side of the top step is L * ell_inner on the fine lattice."""
import json, resource, sys, time
import numpy as np, scipy.fft as sf

def guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024**3 > 2:
        raise SystemExit("RSS above 2 GB")

def dl(q, l):
    s = np.sin(q / 2)
    out = np.full(q.shape, float(l), dtype=q.dtype)
    m = np.abs(s) > 1e-7
    out[m] = np.sin(l * q[m] / 2) / s[m]
    return out

def fourier_lift(L, Np, inner, dtype=np.float32):
    """Returns K fields: dict mu' -> array (d, n..) of the level-k bond angles on level-k sites, in the fine FFT convention."""
    ell = L * inner
    n = Np * ell
    d = 4
    q1 = (2 * np.pi * sf.fftfreq(n, 1.0 / n) / n).astype(dtype)  # fine momenta
    idx = np.arange(n)
    nint = np.round(q1 * n / (2 * np.pi)).astype(int)
    qh1 = 2 * np.sin(q1 / 2)
    dq = dl(q1, ell)
    # alias sign (-1)^{m_mu}, m := (index of alias), with q = q0 + 2 pi m / ell, q0 := representative in the coarse zone
    p0 = ((nint + Np // 2) % Np) - Np // 2
    m1 = (nint - p0) // Np
    sg = np.where(m1 % 2 == 0, 1.0, -1.0).astype(dtype)
    def bc(a, ax):
        sh = [1] * d; sh[ax] = -1
        return a.reshape(sh)
    Pi = np.ones((n,) * d, dtype=dtype)
    for ax in range(d):
        Pi = Pi * bc(dq / ell, ax)
    s = [Pi * bc(sg * dq, ax) for ax in range(d)]
    qh2 = sum(bc(qh1**2, ax) for ax in range(d))
    qh2[(0,) * d] = 1.0
    gi = 1.0 / qh2
    guard()
    # coarse index
    pidx = nint % Np
    flat = np.zeros((n,) * d, dtype=np.int32)
    for ax in range(d):
        flat = flat * Np + bc(pidx, ax).astype(np.int32)
    S = []
    for mu in range(d):
        w = (s[mu] ** 2 * gi).ravel().astype(np.float64)
        w[0] = 0.0  # drop q = 0
        S.append(np.bincount(flat.ravel(), weights=w, minlength=Np**d).reshape((Np,) * d))
    del w
    ph = 2 * np.sin(np.pi * np.arange(Np) * 0 + 2 * np.pi * sf.fftfreq(Np, 1.0 / Np) / Np / 2)  # coarse p-hat, 2 sin(p/2), p in coarse units
    def pc(ax):
        sh = [1] * d; sh[ax] = -1
        return ph.reshape(sh)
    out = {}
    for mup in range(d):
        Y = [np.ones((Np,) * d) * (1.0 if mu == mup else 0.0) for mu in range(d)]  # unit bond at the origin, midpoint phase convention below
        # transform of the unit bond with midpoint phases: sum_y e^{-i p (y + e_mu/2)} delta -> e^{-i p_mu / 2}
        pm = 2 * np.pi * sf.fftfreq(Np, 1.0 / Np) / Np
        shape = [1] * d; shape[mup] = -1
        Yh = [Y[mu] * (np.exp(-1j * pm).reshape(shape) if False else 1.0) for mu in range(d)]
        Yh[mup] = Yh[mup] * np.exp(-1j * pm / 2).reshape(shape)
        Yh = [y / Np**d for y in Yh]
        with np.errstate(divide="ignore", invalid="ignore"):
            num = sum(pc(mu) * Yh[mu] / S[mu] for mu in range(d))
            den = sum(pc(mu) ** 2 / S[mu] for mu in range(d))
            alpha = -num / den
            lam = [(Yh[mu] + pc(mu) * alpha) / S[mu] for mu in range(d)]
        for mu in range(d):
            lam[mu] = np.nan_to_num(lam[mu])
            lam[mu][(0,) * d] = 0.0
        H = []
        for mu in range(d):
            Ht = (s[mu] * gi).astype(np.complex64 if dtype == np.float32 else np.complex128) * lam[mu].ravel()[flat].astype(np.complex64 if dtype == np.float32 else np.complex128)
            Ht[(0,) * d] = 0
            guard()
            H.append(Ht)
        yield mup, H, q1, n, ell, s, gi, flat
    return

def to_position(Ht, q1, mu, n, extra=None):
    """H_mu(x) with midpoint convention: sum_q e^{i q (x + e_mu/2)} Ht. extra: symbol multiplying Ht."""
    d = 4
    sh = [1] * d; sh[mu] = -1
    ph = np.exp(1j * q1 / 2).astype(np.complex64 if q1.dtype == np.float32 else np.complex128).reshape(sh)
    X = Ht * ph if extra is None else Ht * ph * extra
    return sf.ifftn(X, norm="forward", workers=1).real

def analyse(L, Np, inner, R, dtype=np.float32):
    d = 4
    t0 = time.time()
    Scol = 0.0
    prow = None
    for mup, H, q1, n, ell, s, gi, flat in fourier_lift(L, Np, inner, dtype):
        col = 0.0
        for mu in range(d):
            if inner == 1:
                x = to_position(H[mu], q1, mu, n)
                K = x
                sites = n
                step = 1
            else:
                def bc(a, ax):
                    sh = [1] * d; sh[ax] = -1
                    return a.reshape(sh)
                dq = dl(q1, inner)
                sym = np.ones((n,) * d, dtype=q1.dtype)
                for ax in range(d):
                    sym = sym * bc(dq / inner, ax)
                sym = sym * bc(dq, mu)
                x = to_position(H[mu], q1, mu, n, extra=sym)
                # level-k bond from y: value sits at fine site y + (inner - 1)/2 e_mu by the midpoint convention
                K = np.roll(x, -(inner - 1) // 2, axis=mu)
                K = K[(slice(None, None, inner),) * d]
                sites = n // inner
                step = inner
            # bond distance from x' (parent bond at origin along mup) in parent cells, Chebyshev, torus
            nk = sites
            c = np.arange(nk)
            c = np.minimum(c, nk - c) / L
            sh = lambda ax: [-1 if i == ax else 1 for i in range(d)]
            dist = np.zeros(K.shape, dtype=np.float32)
            for ax in range(d):
                dist = np.maximum(dist, c.reshape(sh(ax)))
            A = np.abs(K) * (dist <= R)
            col += float(A.sum())
            # periodise on the block lattice for the row sum
            B = A
            for ax in range(d):
                B = np.add.reduce(np.stack(np.split(B, Np, axis=ax), 0), axis=0)
            if prow is None:
                prow = np.zeros((d,) + B.shape)
            prow[mu] += B
            guard()
        Scol = max(Scol, col)
    Srow = float(prow.max())
    return Srow, Scol, time.time() - t0

if __name__ == "__main__":
    L, Np = int(sys.argv[1]), int(sys.argv[2])
    inner = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    res = {}
    for R in (1, 2, 3):
        if R > Np / 2:
            continue
        Srow, Scol, t = analyse(L, Np, inner, R)
        res[R] = dict(Srow=Srow, Scol=Scol, LSrow=L * Srow, ScolL3=Scol / L**3, k5=Scol * Srow**4, k6=Scol * Srow**5, t=t)
        print(json.dumps(dict(L=L, Np=Np, inner=inner, R=R, **res[R])), flush=True)
    json.dump(res, open(f"k1_{L}_{Np}_{inner}.json", "w"))
    print("rss", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024**3)
