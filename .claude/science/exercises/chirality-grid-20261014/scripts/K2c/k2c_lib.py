"""K2c helpers on top of K2's lat2d.py and K2b's k2b_lib.py (both copied unchanged): weight-selectable (hard | tri) kernel
entries, pure-gauge (PG) kernel, PV-subtracted DWF via the transfer-matrix formula, margin-admissible generators."""
import numpy as np
from lat2d import Geom, nodes, rand_half, wrap
from k2b_lib import D_batch, logdet_op, normalized, lam, gen_ratio, admissible, perturb, holonomy_shift, M0, MF

DELTA = 0.6; DB = 0.55          # measure support delta; pool margin: bulk plaquettes <= DB


def max_bulk(G, u):
    T, Lx = G.T, G.Lx; m = 0.0
    for t in range(T - 1):
        for x in range(Lx):
            m = max(m, abs(wrap(u['x'][t, x] + u['t'][t, (x + 1) % Lx] - u['x'][t + 1, x] - u['t'][t, x])))
    return m


def dwf_formula_logs(G, Db, Ls_list):
    """K2b V3 formula: det D5(mf)/det D5(1) = det[(1+mf)/2 + (1-mf)/2 g5 (1-T^Ls)/(1+T^Ls)], T = (1-H_T)/(1+H_T)."""
    N = G.N; Id = np.eye(N); g5 = G.g5d
    Am = Db - M0 * Id[None]
    H = g5[None, :, None] * (Am @ np.linalg.inv(2 * Id[None] + Am)); H = 0.5 * (H + np.conj(np.swapaxes(H, 1, 2)))
    w, V = np.linalg.eigh(H); t = (1 - w) / (1 + w); out = {}
    for Ls in Ls_list:
        if Ls == 'inf':
            eps = np.sign(w)
        else:
            with np.errstate(over='ignore', divide='ignore', invalid='ignore'):
                small = np.abs(t) <= 1; ti = np.where(small, 1.0, 1.0 / np.where(t == 0, 1.0, t))
                eps = np.where(small, (1 - t ** Ls) / (1 + t ** Ls), (ti ** Ls - 1) / (ti ** Ls + 1))
        S = (V * eps[:, None, :]) @ np.conj(np.swapaxes(V, 1, 2))
        A = 0.5 * (1 + MF) * Id[None] + 0.5 * (1 - MF) * g5[None, :, None] * S
        sg, ld = np.linalg.slogdet(A); out[Ls] = ld + np.log(sg.astype(complex))
    return out, np.abs(w).min(1)


def point_logs(G, Db, op):
    """log det per point for op in PG, W, O, SH, DWF4, DWF8; returns (logs, min gap)."""
    if op == 'PG':
        return np.zeros(Db.shape[0], complex), np.full(Db.shape[0], np.nan)
    if op in ('DWF4', 'DWF8'):
        o, g = dwf_formula_logs(G, Db, [int(op[3:])]); return o[int(op[3:])], g
    return logdet_op(G, Db, op)


def entry_log(G, ua, ub, n, nw, op, Fs, Bs, weight, chunk=32):
    ph, w = nodes(G, ua, ub, DELTA, n, weight, nw)
    if len(w) == 0 or w.sum() <= 0: return -np.inf + 0j, np.inf
    D0 = G.D0(ua, ub); ls = []; gm = np.inf
    for c in range(0, len(w), chunk):
        l, g = point_logs(G, D_batch(G, D0, Fs, Bs, ph[c:c+chunk]), op); ls.append(l)
        if np.any(np.isfinite(g)): gm = min(gm, np.nanmin(g))
    l = np.concatenate(ls); lm = l.real.max()
    return lm + np.log(np.sum(w * np.exp(l - lm)) + 0j), gm


class Pool:
    def __init__(self, G, n, nw, op, weight):
        self.G, self.n, self.nw, self.op, self.weight = G, n, nw, op, weight
        self.Fs, self.Bs = G.crossing_mats(); self.U = []; self.L = np.zeros((0, 0), complex); self.gmin = np.inf

    def row(self, u):
        r = [entry_log(self.G, a, u, self.n, self.nw, self.op, self.Fs, self.Bs, self.weight) for a in self.U]
        r.append(entry_log(self.G, u, u, self.n, self.nw, self.op, self.Fs, self.Bs, self.weight))
        return np.array([x[0] for x in r], complex), min(x[1] for x in r)

    def bordered(self, logs):
        k = len(self.U); L = np.full((k + 1, k + 1), -np.inf + 0j); L[:k, :k] = self.L
        L[:k, k] = logs[:k]; L[k, :k] = np.conj(logs[:k]); L[k, k] = logs[k].real
        return L

    def add(self, u, logs, g):
        self.L = self.bordered(logs); self.U.append(u); self.gmin = min(self.gmin, g)


def full_kernel(G, U, n, nw, op, weight):
    P = Pool(G, n, nw, op, weight)
    for u in U:
        logs, g = P.row(u); P.add(u, logs, g)
    return normalized(P.L), P.gmin


def subset_change(G, U, Zref, n, nw, op, weight, pairs):
    """max |Zn(n,nw) - Zref| over the given pairs (needs the diagonal at (n,nw) for normalization)."""
    Fs, Bs = G.crossing_mats(); k = len(U)
    d = np.array([entry_log(G, U[i], U[i], n, nw, op, Fs, Bs, weight)[0].real for i in range(k)])
    out = 0.0
    for (a, b) in pairs:
        v, _ = entry_log(G, U[a], U[b], n, nw, op, Fs, Bs, weight)
        z = np.exp(v - 0.5 * (d[a] + d[b])) if np.isfinite(v.real) else 0.0
        out = max(out, abs(z - Zref[a, b]))
    return out
