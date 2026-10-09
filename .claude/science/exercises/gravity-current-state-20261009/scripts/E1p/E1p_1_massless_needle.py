"""E1' (b): per-realization noise of the massless link field phi(x) = (a/rho) sum_{y <. x} j(y), 4D, rho = 1.

Exact dependence region (EXACT): phi(x) depends only on the sprinkling inside S = supp j  union  U_{y in supp j} I(y,x).
We keep only source points with rho V(y,x) < SMAX (dropped link mass <= e^-SMAX per point, SMAX = 24) and sprinkle
R = {z < x : tau_xz^2 < tau_max^2, transverse distance from the x-source axis < s + tau_max, -tau_max < xi < D+s+tau_max},
xi = -X1 = distance from x toward the source. Every interval I(y,x), y in the kept source set, lies inside R
(subset of the shell since V(z,x) < V(y,x); within tau/2 <= tau_max/2 of the segment x-y, which lies in the cylinder).
Hence the computed link set is exact for the truncated functional.

x = origin. Source: ball of radius s centred at X = (-D,0,0), time window |t + D| < Ts/2 (Ts = inf: whole ball).
Profiles: 'flat' j = 1; 'gauss' j = exp(-d^2/(2 (s/2)^2)) truncated at the ball.
Output per realization: N_flat (link count), F_gauss = sum_links j, and the sigma = tau^2 of every link (pooled).
"""
import sys, time, os, json
import numpy as np
from numba import njit, prange
from math import pi, sqrt

SMAX = 24.0
TAU2 = sqrt(24.0 * SMAX / pi)   # tau_max^2 = 13.54 (rho=1): pi tau^4/24 < SMAX
TAU = sqrt(TAU2)


def hstab(X, tau2=TAU2):
    """(X+tau2)^1.5 - X^1.5 without cancellation."""
    return tau2 * (3 * X * X + 3 * X * tau2 + tau2 * tau2) / ((X + tau2)**1.5 + X**1.5)


def Axs(xi, Rp, tau2=TAU2):
    """cross-section 3-volume integral: int_{|perp|<Rp} Delta t(r) d^2perp, Delta t = sqrt(r^2+tau2) - r.
    = (2pi/3)[h(xi^2+Rp^2) - h(xi^2)], h(X) = (X+tau2)^1.5 - X^1.5; the difference is formed stably."""
    X0 = xi * xi; X1 = X0 + Rp * Rp
    # h(X1) - h(X0) = int_{X0}^{X1} h'(X) dX,  h'(X) = 1.5 (sqrt(X+tau2) - sqrt X) = 1.5 tau2/(sqrt(X+tau2)+sqrt X)
    # exact antiderivative difference via stable h is fine once h itself is stable:
    return (2 * pi / 3) * (hstab(X1, tau2) - hstab(X0, tau2))


def region_table(D, s):
    Rp = s + TAU
    lo, hi = -TAU, D + s + TAU
    # fine grid, denser near 0
    g1 = np.linspace(lo, min(hi, 4 * Rp), 4000)
    g2 = np.geomspace(4 * Rp, hi, 6000) if hi > 4 * Rp else np.array([])
    g = np.unique(np.concatenate([g1, g2]))
    A = Axs(g, Rp)
    cum = np.concatenate([[0.0], np.cumsum(0.5 * (A[1:] + A[:-1]) * np.diff(g))])
    return g, A, cum, Rp


def sample_region(D, s, rng, tab):
    g, A, cum, Rp = tab
    V = cum[-1]
    N = rng.poisson(V)
    # xi: inverse CDF with linear A inside each cell
    q = rng.uniform(0, V, N)
    k = np.searchsorted(cum, q, side="right") - 1
    k = np.clip(k, 0, len(g) - 2)
    dq = q - cum[k]
    a0 = A[k]; a1 = A[k + 1]; h = g[k + 1] - g[k]
    slope = (a1 - a0) / h
    # solve a0*u + slope*u^2/2 = dq
    with np.errstate(invalid="ignore", divide="ignore"):
        u = np.where(np.abs(slope) > 1e-14 * np.maximum(a0, 1e-300),
                     (-a0 + np.sqrt(np.maximum(a0 * a0 + 2 * slope * dq, 0))) / slope, dq / a0)
    xi = g[k] + np.clip(u, 0, h)
    # r given xi: density r*Dt(r) on [|xi|, sqrt(xi^2+Rp^2)], CDF F(r) = ((r^2+tau2)^1.5 - r^3)/3
    F = lambda r: hstab(r * r) / 3.0
    r0 = np.abs(xi); r1 = np.sqrt(xi * xi + Rp * Rp)
    target = F(r0) + rng.uniform(0, 1, N) * (F(r1) - F(r0))
    a_, b_ = r0.copy(), r1.copy()
    for _ in range(60):
        mid = 0.5 * (a_ + b_)
        lt = F(mid) < target
        a_ = np.where(lt, mid, a_); b_ = np.where(lt, b_, mid)
    r = 0.5 * (a_ + b_)
    perp = np.sqrt(np.maximum(r * r - xi * xi, 0))
    ph = rng.uniform(0, 2 * pi, N)
    t = -rng.uniform(r, np.sqrt(r * r + TAU2))
    P = np.column_stack([t, -xi, perp * np.cos(ph), perp * np.sin(ph)])
    return P


@njit(parallel=True, cache=True)
def links_to_origin(P, sig_order, src_idx):
    """For each source index y: 1 if y <. x (x = origin), i.e. no z in P with y < z (z < x automatic in R)
    and sigma_z < sigma_y. sig_order: indices of P sorted by sigma."""
    ns = src_idx.shape[0]
    out = np.zeros(ns, np.int8)
    N = P.shape[0]
    sig = np.empty(N)
    for i in range(N):
        sig[i] = P[i, 0]**2 - P[i, 1]**2 - P[i, 2]**2 - P[i, 3]**2
    for q in prange(ns):
        y = src_idx[q]
        sy = sig[y]
        ty, xy, yy, zy = P[y, 0], P[y, 1], P[y, 2], P[y, 3]
        linked = 1
        for p in range(N):
            z = sig_order[p]
            if sig[z] >= sy:
                break
            dt = P[z, 0] - ty
            if dt <= 0:
                continue
            dx = P[z, 1] - xy; dy = P[z, 2] - yy; dz = P[z, 3] - zy
            if dt * dt > dx * dx + dy * dy + dz * dz:
                linked = 0
                break
        out[q] = linked
    return out


def mean_quadrature(D, s, Ts, profile, power=1, nr=400, nth=200):
    """rho * int_src j^power e^{-rho V} d^4y  (V = pi tau^4/24), exact quadrature (no SMAX cut)."""
    # spherical coords about the source centre: d, cos(theta) relative to +X1 (toward x)
    dd = (np.arange(nr) + 0.5) / nr * s
    ct = np.linspace(-1, 1, nth + 1); ct = 0.5 * (ct[1:] + ct[:-1])
    Dd, Ct = np.meshgrid(dd, ct, indexing="ij")
    X1 = -D + Dd * Ct
    perp2 = (Dd * np.sqrt(1 - Ct**2))**2
    r = np.sqrt(X1**2 + perp2)
    j = np.ones_like(r) if profile == "flat" else np.exp(-Dd**2 / (2 * (s / 2)**2))
    # time integral over t in window, t < -r:  int e^{-pi (t^2-r^2)^2/24} dt
    # substitute sigma = t^2 - r^2, dt = dsigma / (2 sqrt(r^2+sigma)); window -> sigma range
    smax = 60.0
    ns = 3000
    sg = (np.arange(ns) + 0.5) / ns * smax  # sigma grid (pi sigma^2/24 up to ~470)
    out = 0.0
    for i in range(nr):
        for k in range(nth):
            rr = r[i, k]
            tt = -np.sqrt(rr * rr + sg)          # times for these sigma
            w = np.exp(-pi * sg**2 / 24.0) / (2 * np.sqrt(rr * rr + sg))
            if np.isfinite(Ts):
                w = w * (np.abs(tt + D) < Ts / 2)
            val = w.sum() * (smax / ns)
            out += (j[i, k]**power) * val * (Dd[i, k]**2) * (s / nr) * (2.0 / nth) * 2 * pi
    return out


def run(D, s, Ts, nreal, seed, verbose=True):
    rng = np.random.default_rng(seed)
    tab = region_table(D, s)
    NF = np.zeros(nreal); FG = np.zeros(nreal); NR = np.zeros(nreal, np.int64)
    sig_links = []
    t0 = time.time()
    for it in range(nreal):
        P = sample_region(D, s, rng, tab)
        d2 = (P[:, 1] + D)**2 + P[:, 2]**2 + P[:, 3]**2
        insrc = d2 < s * s
        if np.isfinite(Ts):
            insrc &= np.abs(P[:, 0] + D) < Ts / 2
        src = np.where(insrc)[0]
        sig = P[:, 0]**2 - (P[:, 1:]**2).sum(1)
        order = np.argsort(sig)
        lk = links_to_origin(P, order, src).astype(bool)
        jg = np.exp(-d2[src] / (2 * (s / 2)**2))
        NF[it] = lk.sum(); FG[it] = jg[lk].sum(); NR[it] = len(P)
        if it < 200:
            r_ = np.sqrt((P[src[lk], 1:]**2).sum(1))
            sig_links.append(np.column_stack([sig[src[lk]], r_]))
    sl = np.vstack(sig_links) if sig_links else np.zeros((0, 2))
    return dict(NF=NF, FG=FG, NR=NR, sig_links=sl, time=time.time() - t0)


if __name__ == "__main__":
    cfgs = json.loads(sys.argv[1])
    tag = sys.argv[2]
    res = {}
    os.makedirs("../out", exist_ok=True)
    for c in cfgs:
        D, s, Ts, nreal, seed = c["D"], c["s"], c.get("Ts", float("inf")), c["n"], c.get("seed", 1)
        r = run(D, s, Ts, nreal, seed)
        m1f = mean_quadrature(D, s, Ts, "flat", 1)
        m1g = mean_quadrature(D, s, Ts, "gauss", 1)
        m2g = mean_quadrature(D, s, Ts, "gauss", 2)
        key = f"D{D}_s{s}_Ts{Ts}"
        np.savez(f"../out/massless_{tag}_{key}.npz", **r, D=D, s=s, Ts=Ts, m1f=m1f, m1g=m1g, m2g=m2g)
        NF, FG = r["NF"], r["FG"]
        print(f"{key}: Nregion~{r['NR'].mean():.0f} | flat: mean {NF.mean():.3f} (quad {m1f:.3f}) var {NF.var(ddof=1):.3f} "
              f"Fano {NF.var(ddof=1)/m1f:.3f} | gauss: mean {FG.mean():.3f} (quad {m1g:.3f}) "
              f"var/diag {FG.var(ddof=1)/m2g:.3f} | n={nreal} t={r['time']:.1f}s", flush=True)
