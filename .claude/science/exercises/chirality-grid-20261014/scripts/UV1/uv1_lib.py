"""UV-1 helpers on top of K2's lat2d.py and K2b's k2b_lib.py (copied unchanged).
Shared-determinant kernels: quadrature nodes carry the union of both arms' kinks, determinants are computed once per node,
and every (arm, beta_g) weight is applied afterwards.  Arms: 'tri' (primary, positive-type triangle profile) and 'hard'.
Plaquette weight w(p) = f_arm(p) * exp(beta (cos p - 1)), delta = 0.6.
Depth 1: K2c layout (crossing links only).  Depth 2 (open time): buffer slice 1 (and mirror) integrated; temporal gauge on
the buffer t-link; buffer x-links from the gap plaquettes q: u_1(x) = u_2(x) + q(x).  Nested kink-aligned Gauss rule."""
import numpy as np
from lat2d import Geom, wrap, GX, I2
from k2b_lib import logdet_op, normalized

DELTA = 0.6; DB = 0.55
BETAS = (0.0, 1.0, 4.0, 8.0)
ARMS = [(a, b) for a in ('tri', 'hard') for b in BETAS]


def wfun(p, arm, beta):
    f = np.clip(1 - np.abs(p) / DELTA, 0, None) if arm == 'tri' else (np.abs(p) < DELTA).astype(float)
    return f * np.exp(beta * (np.cos(p) - 1.0))


def pieces_nodes(lo, hi, bps, n):
    pts = [lo] + sorted(b for b in bps if lo < b < hi) + [hi]
    xg, wg = np.polynomial.legendre.leggauss(n); X = []; W = []
    for a, b in zip(pts[:-1], pts[1:]):
        if b - a > 1e-14:
            X.append(0.5 * (b - a) * xg + 0.5 * (a + b)); W.append(0.5 * (b - a) * wg)
    return (np.concatenate(X), np.concatenate(W)) if X else (np.zeros(0), np.zeros(0))


def cross_nodes(Phi, n):
    """Lx = 2 crossing gap: plaquettes (d0, Phi - d0); support pieces split at {0, Phi} (union of both arms' kinks)."""
    lo = max(-DELTA, Phi - DELTA); hi = min(DELTA, Phi + DELTA)
    if hi <= lo: return np.zeros(0), np.zeros(0)
    return pieces_nodes(lo, hi, [0.0, Phi], n)


# ---------------------------------------------------------------- depth 1 (K2c layout) -------------------------------------
def nodes_d1(G, ua, ub, n, nw):
    """returns phis (P, ncross), base weights (P,), plaquettes (P, nplaq) for the crossing gap(s)."""
    A = ub['x'][0] - ua['x'][0]; PhiA = wrap(A.sum())
    dA, wA = cross_nodes(PhiA, n)
    if not G.torus:
        ph = np.stack([np.zeros_like(dA), dA - A[0]], 1)
        return ph, wA, np.stack([dA, PhiA - dA], 1)
    Bo = ua['x'][G.T - 1] - ub['x'][G.T - 1]; PhiB = wrap(Bo.sum())
    dB, wB = cross_nodes(PhiB, n)
    if len(wA) == 0 or len(wB) == 0: return np.zeros((0, 4)), np.zeros(0), np.zeros((0, 4))
    ws = 2 * np.pi * np.arange(nw) / nw; ww = 2 * np.pi / nw
    iA, iB, iW = [x.ravel() for x in np.meshgrid(np.arange(len(wA)), np.arange(len(wB)), np.arange(nw), indexing='ij')]
    chi0 = ws[iW]; chi1 = chi0 + (dB[iB] - Bo[0])
    ph = np.stack([np.zeros(len(iA)), dA[iA] - A[0], chi0, chi1], 1)
    pl = np.stack([dA[iA], PhiA - dA[iA], dB[iB], PhiB - dB[iB]], 1)
    return ph, wA[iA] * wB[iB] * ww, pl


def D_links(Dfix, Fs, Bs, th):
    e = np.exp(1j * th)
    return Dfix[None] + np.einsum('pj,jab->pab', e, Fs) + np.einsum('pj,jab->pab', np.conj(e), Bs)


def point_logs(G, Db, op):
    if op == 'PG':
        return np.zeros(Db.shape[0], complex), np.full(Db.shape[0], np.nan)
    return logdet_op(G, Db, op)


def entry_logs_all(logs, base_w, plaqs, arms=ARMS):
    """dict (arm, beta) -> complex log of sum_i base_w g_arm,beta(plaqs_i) exp(logs_i)."""
    out = {}
    if len(base_w) == 0:
        for k in arms: out[k] = -np.inf + 0j
        return out
    lm = logs.real.max(); e = np.exp(logs - lm)
    for (arm, beta) in arms:
        g = np.prod(wfun(plaqs, arm, beta), axis=1)
        s = np.sum(base_w * g * e)
        out[(arm, beta)] = (lm + np.log(s + 0j)) if s != 0 else -np.inf + 0j
    return out


def entry_d1(G, ua, ub, n, nw, op, Fs, Bs, chunk=32):
    ph, w, pl = nodes_d1(G, ua, ub, n, nw)
    if len(w) == 0: return entry_logs_all(np.zeros(0), w, pl), np.inf
    D0 = G.D0(ua, ub); ls = []; gm = np.inf
    for c in range(0, len(w), chunk):
        l, g = point_logs(G, D_links(D0, Fs, Bs, ph[c:c+chunk]), op); ls.append(l)
        if np.any(np.isfinite(g)): gm = min(gm, np.nanmin(g))
    return entry_logs_all(np.concatenate(ls), w, pl), gm


# ---------------------------------------------------------------- depth 2 (open time) --------------------------------------
def nested_nodes_d2(n, Phi0=0.0, signs=(-1, -1, +1, +1)):
    """nodes for variables q = (q+_0, q+_1, q-_0, q-_1) then d0; Phi_eff = Phi0 + sum s_i q_i.
    Each variable's interval [-delta, delta] is split at its own kinks {0} and where the residual hits j*delta,
    |j| <= (#inner plaquettes); pieces where the inner function vanishes are dropped.  Returns Q (P,4), d0 (P,), base w (P,)."""
    m = len(signs); Qs = []; Ds = []; Ws = []
    def rec(i, R, qs, wacc):
        if i == m:
            d, w = cross_nodes(R, n)
            if len(w):
                Qs.append(np.tile(qs, (len(d), 1))); Ds.append(d); Ws.append(wacc * w)
            return
        J = 2 + (m - 1 - i); s = signs[i]
        bps = [0.0] + [s * (j * DELTA - R) for j in range(-J, J + 1)]
        x, w = pieces_nodes(-DELTA, DELTA, bps, n)
        for xi, wi in zip(x, w):
            if abs(R + s * xi) < J * DELTA:
                rec(i + 1, R + s * xi, qs + [xi], wacc * wi)
    rec(0, Phi0, [], 1.0)
    return np.concatenate(Qs), np.concatenate(Ds), np.concatenate(Ws)


def deep_to_ext(ud, qrow):
    """depth-2 test config (slices 2..T: ux (T-1, Lx), ut (T-2, Lx)) + buffer gap plaquettes q (Lx,) -> K2 config (slices 1..T)."""
    ux = np.vstack([ud['x'][0] + qrow, ud['x']]); ut = np.vstack([np.zeros((1, ud['x'].shape[1])), ud['t']])
    return {'x': ux, 't': ut}


def buffer_xlink_mats(G):
    """hop matrices for the buffer x-links (x, t=1) [positive side] and (x, t=0) [mirror side], K2 hop convention."""
    N, Lx = G.N, G.Lx; Fs = []; Bs = []
    for t in (1, 0):
        for x in range(Lx):
            F = np.zeros((N, N), complex); B = np.zeros((N, N), complex)
            a = G.idx(x, t); b = G.idx(x + 1, t); sg = G.xbc if x == Lx - 1 else 1.0
            F[a:a+2, b:b+2] = -0.5 * (I2 - GX) * sg; B[b:b+2, a:a+2] = -0.5 * (I2 + GX) * sg
            Fs.append(F); Bs.append(B)
    return np.array(Fs), np.array(Bs)


def entry_d2(G, ua_d, ub_d, nodes, op, FsC, BsC, FsX, BsX, chunk=32):
    """depth-2 open-time entry: ua_d, ub_d deep configs (W-matched at slice 2).  nodes = nested_nodes_d2(n)."""
    Q, d0, w = nodes; Lx = G.Lx
    zero = np.zeros(Lx)
    ua0 = deep_to_ext(ua_d, zero); ub0 = deep_to_ext(ub_d, zero)
    D0 = G.D0(ua0, ub0)
    th0 = np.concatenate([ua0['x'][0], ub0['x'][0]]); e0 = np.exp(1j * th0)
    Dfix = D0 - np.einsum('j,jab->ab', e0, FsX) - np.einsum('j,jab->ab', np.conj(e0), BsX)   # remove the buffer x-link hops (their q = 0 angles)
    up = ua0['x'][0][None] + Q[:, 0:2]; um = ub0['x'][0][None] + Q[:, 2:4]
    A = um - up; Phi = wrap(A.sum(1))
    th = np.concatenate([up, um, np.zeros((len(d0), 1)), (d0 - A[:, 0])[:, None]], 1)   # [x-links +, x-links -, phi0, phi1]
    Fs = np.concatenate([FsX, FsC]); Bs = np.concatenate([BsX, BsC])
    pl = np.concatenate([Q, d0[:, None], (Phi - d0)[:, None]], 1)
    ls = []; gm = np.inf
    for c in range(0, len(w), chunk):
        l, g = point_logs(G, D_links(Dfix, Fs, Bs, th[c:c+chunk]), op); ls.append(l)
        if np.any(np.isfinite(g)): gm = min(gm, np.nanmin(g))
    return entry_logs_all(np.concatenate(ls), w, pl), gm, Phi


def explicit_plaquettes(G, ua, ub, phis):
    """all plaquettes of the open-time lattice from links (independent of the node bookkeeping), for validation."""
    ax, at = G.links(ua, ub); T, Lx = G.T, G.Lx
    at = dict(at); at[(0, 0)] = phis[0]; at[(1, 0)] = phis[1]
    out = {}
    for t in range(-T + 1, T):
        for x in range(Lx):
            out[(x, t)] = wrap(ax[(x, t)] + at[((x + 1) % Lx, t)] - ax[(x, t + 1)] - at[(x, t)])
    return out


# ---------------------------------------------------------------- kernels ---------------------------------------------------
def kernel_from_logs(Lmats, key):
    return normalized(Lmats[key])


def lam(Z):
    ev = np.linalg.eigvalsh(Z); return ev[0], ev[-1], ev
