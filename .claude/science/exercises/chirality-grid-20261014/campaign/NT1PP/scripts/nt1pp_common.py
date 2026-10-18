"""NT-1'' shared helpers (no physics changes to NT-1' nt1p_lib.py, which is imported unchanged)."""
import numpy as np
from nt1p_lib import Strip, Measure
from lat2d import Geom, rand_half


def midpoints(S):
    return np.array([((l[4] + 0.5, l[5]) if l[2] == 'x' else (l[4], l[5] + 0.5)) for l in S.L])


def uniformW(S, W0):
    """zero plaquettes, A_x = W0/Lx on every x-link, A_t = 0 (canonical form)."""
    A = np.zeros((1, S.nl)); A[0, S.xl.reshape(-1)] = W0 / S.Lx
    return A


def gen_config(S, rng, center=True):
    """NT-1' generator (nt1p_locality.py): two rand_half(0.25, 0.55), crossing N(0,0.25); canonical rep; optional W-centering."""
    G = Geom(S.Lx, S.T, False, -1)
    ua = rand_half(rng, G, 0.25, 0.55); ub = rand_half(rng, G, 0.25, 0.55); ph = rng.normal(0, 0.25, (1, S.Lx))
    A = S.canon(S.joined(ua, ub, ph))
    if center:
        _, W = S.FW(A); wc = 0.5 * (W[0, S.T - 1] + W[0, S.T])
        A = A.copy(); A[0, S.xl.reshape(-1)] -= wc / S.Lx
        A = S.canon(A)
    return A


def tail_stat(S, resp, ys):
    """resp: dict y -> (nl,) |d kQ / dA_y|. Returns (tau_mixed at s* = Lx/2-0.5, tau_same at s = Lx/2) maximised over ys,
    pairs with |dt_mid| <= 0.5 (NT-1' XPROFILE convention)."""
    mid = midpoints(S); Lx = S.Lx
    sstar = Lx / 2 - 0.5; out_m = 0.0; out_s = 0.0
    for y in ys:
        dx = np.abs(mid[:, 0] - mid[y, 0]); dx = np.minimum(dx, Lx - dx); dt = np.abs(mid[:, 1] - mid[y, 1])
        sel = dt <= 0.5 + 1e-9
        m = sel & (np.abs(dx - sstar) < 1e-9); s = sel & (np.abs(dx - Lx / 2) < 1e-9)
        if np.any(m): out_m = max(out_m, resp[y][m].max())
        if np.any(s): out_s = max(out_s, resp[y][s].max())
    return out_m, out_s


def fd_response(MS, A, ys, eps=1e-4, Ns=8, keys=('kbb', 'kloc', 'kQ'), chunk=2):
    """central differences of the ray currents w.r.t. single links ys; returns {key: {y: |dk/dA_y| (nl,)}}."""
    nl = A.shape[1]; Ap = np.repeat(A, 2 * len(ys), 0)
    for i, y in enumerate(ys): Ap[2 * i, y] += eps; Ap[2 * i + 1, y] -= eps
    out = {k: {} for k in keys}; gmin = np.inf; ok = True; store = {k: [] for k in keys}
    for c in range(0, len(Ap), chunk):
        r = MS.ray(Ap[c:c + chunk], Ns); gmin = min(gmin, r['gmin']); ok &= r['idx_ok']
        for k in keys: store[k].append(r[k])
    store = {k: np.concatenate(v, 0) for k, v in store.items()}
    for i, y in enumerate(ys):
        for k in keys: out[k][y] = np.abs(store[k][2 * i] - store[k][2 * i + 1]) / (2 * eps)
    return out, gmin, ok
