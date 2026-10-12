"""Lane RD probe D2: shared helpers.

Dressed one-particle band from the one-loop (Brillouin-Wigner) self-energy
  E(k) = eps(k) + (1/N) sum_{q != 0} |M_q|^2 / (E(k) - Ed(k-q) - w(q)),
with Ed = eps (BW1, bare propagator) or Ed = E (self-consistent quasiparticle
propagator, 'SC').  Lowest root below the lowest pole, bracketed Newton.
Measures: face shape exponent, SLAC fit on windows including the face, Z.
"""
import numpy as np

TWO_PI = 2 * np.pi


def eps_band(kind, k, m=0.5):
    if kind == 'TB':          # tight binding, bandwidth 2, v_max = 1
        return 1.0 - np.cos(k)
    if kind == 'KG':          # nearest-neighbour lattice Klein-Gordon
        return np.sqrt(m * m + 4 * np.sin(k / 2) ** 2)
    if kind == 'Q4':          # flat-bottom NN-network band (trig degree 2)
        return (1.0 - np.cos(k)) ** 2
    if kind == 'SLAC':        # comparator: exact SLAC band (not NN)
        kk = (k + np.pi) % TWO_PI - np.pi
        return np.sqrt(m * m + kk ** 2)
    raise ValueError(kind)


def phonon(q, c):
    return 2 * c * np.abs(np.sin(q / 2))


def vertex2(q, g2, a):
    """|M_q|^2 = g2 * (2|sin q/2|)^(2a); a=1/2 is the NN strain vertex."""
    s = 2 * np.abs(np.sin(q / 2))
    out = np.zeros_like(q)
    nz = s > 1e-14
    out[nz] = g2 * s[nz] ** (2 * a)
    return out


def solve_root_1d(eps_k, Ed, w, M2, jk, N, tol=1e-13, maxit=80):
    """For k-indices jk solve lam = eps + Sigma(k, lam) below lowest pole.
    Ed: dressed band on the full grid (length N); w, M2 on q-grid l = 1..N-1.
    Returns lam, dSigma/dlam, lowest pole."""
    l = np.arange(1, N)
    out_l = np.empty(len(jk)); out_d = np.empty(len(jk)); out_p = np.empty(len(jk))
    chunk = max(1, int(4e6 // N))
    for s0 in range(0, len(jk), chunk):
        js = jk[s0:s0 + chunk]
        idx = (js[:, None] - l[None, :]) % N
        P = Ed[idx] + w[None, :]           # pole positions
        wts = M2[None, :] / N
        lp = P.min(axis=1)
        e0 = eps_k[s0:s0 + chunk]
        hi = lp.copy()
        lo = np.minimum(e0, lp) - 50.0
        lam = np.minimum(e0, lp - 1e-3)
        for it in range(maxit):
            den = lam[:, None] - P
            sig = (wts / den).sum(axis=1)
            dsig = -(wts / den ** 2).sum(axis=1)
            f = lam - e0 - sig
            fp = 1 - dsig
            lo = np.where(f < 0, lam, lo)
            hi = np.where(f > 0, lam, hi)
            new = lam - f / fp
            bad = (new <= lo) | (new >= hi) | ~np.isfinite(new)
            new = np.where(bad, 0.5 * (lo + hi), new)
            done = np.abs(new - lam) < tol
            lam = new
            if done.all():
                break
        den = lam[:, None] - P
        dsig = -(wts / den ** 2).sum(axis=1)
        out_l[s0:s0 + chunk] = lam; out_d[s0:s0 + chunk] = dsig; out_p[s0:s0 + chunk] = lp
    return out_l, out_d, out_p


def dressed_band_1d(kind, N, c, g2, a, sc=True, m=0.5, mix=0.6, maxsc=200,
                    tol=1e-12):
    k = TWO_PI * np.arange(N) / N
    eps = eps_band(kind, k, m)
    q = TWO_PI * np.arange(1, N) / N
    w = phonon(q, c)
    M2 = vertex2(q, g2, a)
    jk = np.arange(0, N // 2 + 1)        # use E(k) = E(-k)
    Ed = eps.copy()
    it_used = 0; res = np.nan
    for it in range(maxsc if sc else 1):
        lam, dsig, lp = solve_root_1d(eps[jk], Ed, w, M2, jk, N)
        full = np.empty(N); full[jk] = lam; full[N - jk[1:-1]] = lam[1:-1]
        res = np.max(np.abs(full - Ed)) if sc else np.nan
        Ed_new = mix * full + (1 - mix) * Ed if sc else full
        it_used = it + 1
        if sc:
            Ed = Ed_new
            if res < tol:
                break
    if sc:
        lam, dsig, lp = solve_root_1d(eps[jk], Ed, w, M2, jk, N)
        full = np.empty(N); full[jk] = lam; full[N - jk[1:-1]] = lam[1:-1]
    Z = 1.0 / (1.0 - dsig)
    return dict(k=k[jk], E=lam, Z=Z, gap=lp - lam, eps=eps[jk], it=it_used,
                res=res, full=full)


def face_measures(kh, Eh):
    """kh ascending on [0, pi] with last point at the face pi.  Returns
    local exponents of D(delta) = E(pi) - E(pi - delta) at delta = j*dk for
    j = 1, 2, 4, ..., and the kink indicator D/delta at smallest delta."""
    dk = kh[1] - kh[0]
    n = len(kh) - 1
    Ef = Eh[-1]
    js = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    js = [j for j in js if 2 * j <= n // 2]
    rows = []
    for j in js:
        D1 = Ef - Eh[n - j]; D2 = Ef - Eh[n - 2 * j]
        p = np.log(abs(D2) / abs(D1)) / np.log(2) if D1 != 0 and D2 != 0 else np.nan
        rows.append((j * dk, D1, D1 / (j * dk), p))
    return rows


def slac_fit(kh, Eh, w):
    """Fit E^2 = m0^2 + beta k^2 on k in [pi - w, pi].  Return m0^2, beta,
    max|E - E_fit| / bandwidth, rms/bandwidth, slope ratio
    (one-sided face slope)/(SLAC face slope beta*pi/E(pi))."""
    sel = kh >= np.pi - w - 1e-12
    x = kh[sel] ** 2; y = Eh[sel] ** 2
    A = np.vstack([np.ones_like(x), x]).T
    (m02, beta), *_ = np.linalg.lstsq(A, y, rcond=None)
    Ef = np.sqrt(np.clip(m02 + beta * x, 0, None))
    bw = Eh.max() - Eh.min()
    dev = np.max(np.abs(Ef - Eh[sel])) / bw
    rms = np.sqrt(np.mean((Ef - Eh[sel]) ** 2)) / bw
    dk = kh[1] - kh[0]
    slope_face = (Eh[-1] - Eh[-2]) / dk
    slac_slope = beta * np.pi / Eh[-1]
    return m02, beta, dev, rms, slope_face / slac_slope
