#!/usr/bin/env python3
"""A19 core (supplied toy): one unrecorded excitation (the mover) on the 1D single-track Dirac round,
registered now and then by a linear local formation instrument (A9 Theorems 1-2).

Chain: sites s = 0..N-1 on a ring, N = 2M.  Cell j holds site 2j (amplitude a_j) and site 2j+1 (b_j).
One tick = even layer (bonds (2j,2j+1)) partial swap at theta_e = pi/2, then odd layer (bonds (2j+1,2j+2))
at theta_o = pi/2 - m.  One-excitation block of exp(-i theta SWAP) relative to the emptiness:
cos(theta) - i sin(theta) sigma_x  (A10 S1, A13 M5).  Combined (derived, checked in check_core):
    a'_j = -cos m a_{j-1} - i sin m b_j ,   b'_j = -i sin m a_j - cos m b_{j+1}
so a = right-moving sublattice, b = left-moving sublattice.  Bloch (a_j = A e^{iKj}, b_j = B e^{iKj}):
    U(K) = [[-cos m e^{-iK}, -i sin m], [-i sin m, -cos m e^{iK}]] = -(cos W - i sin W n.sigma)... (see report)
with cos W = cos m cos K  (A5 T2 dispersion up to the overall sign), band velocities +-v(K),
    v(K) = cos m sin K / sqrt(sin^2 m + cos^2 m sin^2 K)   [cells per tick; light speed = 1 cell/tick].
Positions are reported in cells: site 2j -> j, site 2j+1 -> j + 1/2.

Registration (formation) instrument per tick, joint over sites (one excitation => at most one record per tick):
    K_y = sqrt(g w(x - y)) (diagonal in the mover's site x),  K_null = sqrt(1 - g)  (sum_y w = 1)
    sharp site cut: w = delta;  Gaussian (unsharp) cut: w(z) ~ exp(-z^2/(2 sig^2)), z in sites;
    block cut: projector onto an aligned block of s sites (s = 2 is the cell = A5's two-component 'site').
The record's readable content is its place y; the tick t is bookkeeping (what a co-moving record clock registers).
"""
import numpy as np

PI = np.pi


# ---------------------------------------------------------------- dynamics
def step(a, b, m):
    """One tick of the single-track Dirac round on a batch (rows = trajectories, cols = cells)."""
    cm, sm = np.cos(m), np.sin(m)
    an = -cm * np.roll(a, 1, axis=-1) - 1j * sm * b
    bn = -1j * sm * a - cm * np.roll(b, -1, axis=-1)
    return an, bn


def step_layers_sites(psi, m):
    """Reference implementation: explicit pair gates on the site array (one trajectory)."""
    N = psi.shape[0]
    out = psi.copy()
    # even layer, theta_e = pi/2
    th = PI / 2
    c, s = np.cos(th), np.sin(th)
    for j in range(0, N, 2):
        x, y = out[j], out[j + 1]
        out[j], out[j + 1] = c * x - 1j * s * y, c * y - 1j * s * x
    th = PI / 2 - m
    c, s = np.cos(th), np.sin(th)
    for j in range(1, N, 2):
        k = (j + 1) % N
        x, y = out[j], out[k]
        out[j], out[k] = c * x - 1j * s * y, c * y - 1j * s * x
    return out


def bloch_U(K, m):
    cm, sm = np.cos(m), np.sin(m)
    return np.array([[-cm * np.exp(-1j * K), -1j * sm], [-1j * sm, -cm * np.exp(1j * K)]])


def vgroup(K, m):
    cm, sm = np.cos(m), np.sin(m)
    return cm * np.sin(K) / np.sqrt(sm ** 2 + cm ** 2 * np.sin(K) ** 2)


def plus_band(K, m):
    """Eigenvector (uA, uB) of the band with velocity +v(K):  n = (-sin m, 0, cos m sin K)/sin W."""
    cm, sm = np.cos(m), np.sin(m)
    K = np.asarray(K, float)
    sW = np.sqrt(sm ** 2 + cm ** 2 * np.sin(K) ** 2)
    safe = sW > 0                                   # m = 0 and sin K = 0: degenerate Dirac point, pick n = (-1,0,0)
    sWs = np.where(safe, sW, 1.0)
    nx = np.where(safe, -sm / sWs, -1.0)
    nz = np.where(safe, cm * np.sin(K) / sWs, 0.0)
    al = np.arctan2(nx, nz)
    return np.cos(al / 2), np.sin(al / 2)


def packet(M, m, K0, w, j0, band=+1):
    """Band packet: Gaussian in cell momentum around K0, position std w cells, centred at cell j0."""
    k = np.arange(M)
    K = 2 * PI * k / M
    dK = (K - K0 + PI) % (2 * PI) - PI
    phi = np.exp(-dK ** 2 * w ** 2)          # |phi|^2 has std 1/(2w) in K
    uA, uB = plus_band(K, m)
    if band < 0:                              # orthogonal band (velocity -v)
        uA, uB = -np.conj(uB), np.conj(uA)
    ph = np.exp(-1j * K * j0)
    a = np.fft.ifft(phi * uA * ph) * M
    b = np.fft.ifft(phi * uB * ph) * M
    nrm = np.sqrt(np.sum(np.abs(a) ** 2 + np.abs(b) ** 2))
    return a / nrm, b / nrm


def momentum_stats(a, b, m):
    """Per-trajectory <sin K>-free summary: circular mean K, + band weight (rows = trajectories)."""
    M = a.shape[-1]
    A = np.fft.fft(a, axis=-1) / np.sqrt(M)
    B = np.fft.fft(b, axis=-1) / np.sqrt(M)
    K = 2 * PI * np.arange(M) / M
    uA, uB = plus_band(K, m)
    cp = np.conj(uA) * A + np.conj(uB) * B
    wp = np.abs(cp) ** 2
    wt = np.abs(A) ** 2 + np.abs(B) ** 2
    zbar = np.sum(wt * np.exp(1j * K), axis=-1) / np.sum(wt, axis=-1)
    Kmean = np.angle(zbar)
    plus = np.sum(wp, axis=-1) / np.sum(wt, axis=-1)
    # K variance around the circular mean (wrapped)
    d = (K[None, :] - Kmean[:, None] + PI) % (2 * PI) - PI
    Kvar = np.sum(wt * d ** 2, axis=-1) / np.sum(wt, axis=-1)
    return Kmean, Kvar, plus


# ---------------------------------------------------------------- registration
def gauss_kernel(sig):
    """Discrete Gaussian on integer site offsets, normalised to sum 1; sig = 0 -> delta."""
    if sig <= 0:
        return np.array([0]), np.array([1.0])
    R = int(np.ceil(6 * sig))
    z = np.arange(-R, R + 1)
    wz = np.exp(-z ** 2 / (2.0 * sig ** 2))
    return z, wz / wz.sum()


class Registrar:
    """Applies the per-tick formation instrument to a batch; keeps the record tracks (cells, unwrapped)."""

    def __init__(self, B, M, g, kind="gauss", sig=0.0, s=2, x0_cells=None, rng=None, single_use=False):
        self.B, self.M, self.N = B, M, 2 * M
        self.g, self.kind, self.sig, self.s = g, kind, sig, s
        self.rng = rng if rng is not None else np.random.default_rng(0)
        self.z, self.wz = gauss_kernel(sig) if kind == "gauss" else (None, None)
        self.cw = None if self.wz is None else np.cumsum(self.wz)
        self.sqw = None if self.wz is None else np.sqrt(self.wz)
        x0 = 0.0 if x0_cells is None else x0_cells
        self.prev_raw = np.full(B, 2.0 * x0)       # in sites (may be fractional for block centres)
        self.prev_unw = np.full(B, 2.0 * x0)
        self.tracks = [[(0, x0)] for _ in range(B)]   # preparation point (t=0, packet centre) as bookkeeping
        self.single_use = single_use
        if single_use:
            self.used = np.zeros((B, self.N), bool)
        self.count = np.zeros(B, int)

    def _unwrap(self, i, y_sites):
        N = self.N
        d = ((y_sites - self.prev_raw[i] + N / 2) % N) - N / 2
        self.prev_unw[i] += d
        self.prev_raw[i] = y_sites
        return self.prev_unw[i] / 2.0

    def apply(self, a, b, t):
        B, N, M = self.B, self.N, self.M
        rng = self.rng
        if not self.single_use:
            fire = np.nonzero(rng.random(B) < self.g)[0]
        else:
            fire = []
            # sharp single-use: P(fire at y) = g P(y) [y unused]; null update sqrt(1-g) on unused sites
            for i in range(B):
                P = np.empty(N)
                P[0::2] = np.abs(a[i]) ** 2
                P[1::2] = np.abs(b[i]) ** 2
                Pf = P * (~self.used[i])
                pf = self.g * Pf.sum()
                if rng.random() < pf:
                    fire.append(i)
                else:
                    f = np.where(self.used[i], 1.0, np.sqrt(1 - self.g))
                    a[i] *= f[0::2]
                    b[i] *= f[1::2]
                    nrm = np.sqrt(np.sum(np.abs(a[i]) ** 2 + np.abs(b[i]) ** 2))
                    a[i] /= nrm
                    b[i] /= nrm
            fire = np.array(fire, int)
        for i in fire:
            P = np.empty(N)
            P[0::2] = np.abs(a[i]) ** 2
            P[1::2] = np.abs(b[i]) ** 2
            if self.single_use:
                P = P * (~self.used[i])
            P /= P.sum()
            if self.kind == "block":
                s = self.s
                PB = P.reshape(-1, s).sum(1)
                Bk = min(np.searchsorted(np.cumsum(PB), rng.random()), PB.size - 1)
                keep = np.zeros(N)
                keep[Bk * s:(Bk + 1) * s] = 1.0
                ysite = Bk * s + (s - 1) / 2.0
            else:
                x = min(np.searchsorted(np.cumsum(P), rng.random()), N - 1)
                xi = self.z[min(np.searchsorted(self.cw, rng.random()), self.z.size - 1)]
                y = (x + xi) % N
                keep = np.zeros(N)
                idx = (y + self.z) % N
                keep[idx] = self.sqw
                ysite = float(y)
                if self.single_use:
                    self.used[i, y] = True
            a[i] *= keep[0::2]
            b[i] *= keep[1::2]
            nrm = np.sqrt(np.sum(np.abs(a[i]) ** 2 + np.abs(b[i]) ** 2))
            a[i] /= nrm
            b[i] /= nrm
            yc = self._unwrap(i, ysite)
            self.tracks[i].append((t, yc))
            self.count[i] += 1
        return a, b


# ---------------------------------------------------------------- track metrics
def ls_slope(tt, yy):
    tt = np.asarray(tt, float)
    yy = np.asarray(yy, float)
    if tt.size < 2 or np.ptp(tt) == 0:
        return np.nan
    tc = tt - tt.mean()
    return np.dot(tc, yy - yy.mean()) / np.dot(tc, tc)


def track_metrics(tracks, T, v0, checkpoints):
    """Statistics of the record tracks.  Y(t) = place of the latest record at time t (preparation at t=0)."""
    out = {}
    Yc = np.zeros((len(tracks), len(checkpoints)))
    s_all, s1, s2, res = [], [], [], []
    for n, tr in enumerate(tracks):
        tt = np.array([p[0] for p in tr], float)
        yy = np.array([p[1] for p in tr], float)
        for c, tc in enumerate(checkpoints):
            k = np.searchsorted(tt, tc, side="right") - 1
            Yc[n, c] = yy[k] - yy[0]
        sl = ls_slope(tt, yy)
        s_all.append(sl)
        h = tt <= T / 2
        s1.append(ls_slope(tt[h], yy[h]))
        q = tt > T / 2
        s2.append(ls_slope(tt[q], yy[q]))
        if tt.size >= 3 and np.isfinite(sl):
            fit = yy.mean() + sl * (tt - tt.mean())
            res.append(np.sqrt(np.mean((yy - fit) ** 2)))
    s_all, s1, s2 = map(np.array, (s_all, s1, s2))
    ok = np.isfinite(s1) & np.isfinite(s2)
    out["meanY_over_t"] = Yc.mean(0) / np.array(checkpoints)
    out["varY"] = Yc.var(0)
    out["slope_mean"] = np.nanmean(s_all)
    out["slope_sd"] = np.nanstd(s_all)
    out["slope_rmse_v0"] = np.sqrt(np.nanmean((s_all - v0) ** 2))
    out["s1_mean"] = np.nanmean(s1)
    out["s2_mean"] = np.nanmean(s2)
    out["corr12"] = np.corrcoef(s1[ok], s2[ok])[0, 1] if ok.sum() > 3 and np.std(s1[ok]) > 0 and np.std(s2[ok]) > 0 else np.nan
    out["samesign12"] = np.mean(np.sign(s1[ok]) == np.sign(s2[ok])) if ok.sum() else np.nan
    out["resid_rms"] = np.mean(res) if res else np.nan
    out["n_ok"] = int(ok.sum())
    return out
