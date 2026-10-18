"""K2b helpers on top of K2's lat2d.py (copied, unchanged): kernel entries for several fermion measures,
pool kernels with certified error, admissible candidate generators, Shamir DWF (dense 3D operator)."""
import numpy as np
from lat2d import Geom, nodes, rand_half, wrap, tri

M0, MF = 1.0, 0.05


def admissible(G, u, delta):
    T, Lx = G.T, G.Lx
    for t in range(T - 1):
        for x in range(Lx):
            if abs(wrap(u['x'][t, x] + u['t'][t, (x + 1) % Lx] - u['x'][t + 1, x] - u['t'][t, x])) >= delta:
                return False
    return True


def perturb(rng, G, u, sig, delta, maxtry=2000):
    for _ in range(maxtry):
        v = {'x': u['x'] + rng.normal(0, sig, u['x'].shape), 't': u['t'] + rng.normal(0, sig, u['t'].shape)}
        if admissible(G, v, delta): return v
    return None


def holonomy_shift(rng, u, cmax=0.3):
    c = rng.uniform(-cmax, cmax)
    return {'x': u['x'] + c, 't': u['t'].copy()}


def D_batch(G, D0, Fs, Bs, phis):
    e = np.exp(1j * phis)
    return D0[None] + np.einsum('pj,jab->pab', e, Fs) + np.einsum('pj,jab->pab', np.conj(e), Bs)


def logdet_op(G, Db, op, Ls=None):
    """Db: batch of 2D Wilson operators (massless, r=1). Returns complex logdet per point, min|eig H_W| (overlap ops)."""
    N = G.N; Id = np.eye(N); g5 = G.g5d; P = Db.shape[0]
    gap = np.full(P, np.nan)
    if op == 'W':
        A = Db + MF * Id[None]
    elif op == 'O':                          # Neuberger overlap (K2 convention)
        H = g5[None, :, None] * (Db - M0 * Id[None]); w, V = np.linalg.eigh(H); gap = np.abs(w).min(1)
        S = (V * np.sign(w)[:, None, :]) @ np.conj(np.swapaxes(V, 1, 2))
        A = (1 - MF / 2) * (Id[None] + g5[None, :, None] * S) + MF * Id[None]
    elif op == 'SH':                         # Shamir-kernel overlap = L_s -> infinity limit of (b)
        Am = Db - M0 * Id[None]
        H = g5[None, :, None] * (Am @ np.linalg.inv(2 * Id[None] + Am)); H = 0.5 * (H + np.conj(np.swapaxes(H, 1, 2)))
        w, V = np.linalg.eigh(H); gap = np.abs(w).min(1)
        S = (V * np.sign(w)[:, None, :]) @ np.conj(np.swapaxes(V, 1, 2))
        A = 0.5 * (1 + MF) * Id[None] + 0.5 * (1 - MF) * g5[None, :, None] * S
    elif op in ('D5', 'D5PV', 'D5ONE'):               # dense Shamir 3D operator; D5 = bare det D5(mf); D5PV = log det D5(mf) - log det D5(1)
        def build(mf):
            NN = Ls * N; X = np.zeros((P, NN, NN), complex)
            Pm = np.diag(0.5 * (1 - g5)); Pp = np.diag(0.5 * (1 + g5))
            for s in range(Ls):
                X[:, s*N:(s+1)*N, s*N:(s+1)*N] = Db - M0 * Id[None] + Id[None]
                if s + 1 < Ls: X[:, s*N:(s+1)*N, (s+1)*N:(s+2)*N] = -Pm[None]
                if s - 1 >= 0: X[:, s*N:(s+1)*N, (s-1)*N:s*N] = -Pp[None]
            X[:, (Ls-1)*N:Ls*N, 0:N] += mf * Pm[None]; X[:, 0:N, (Ls-1)*N:Ls*N] += mf * Pp[None]
            return X
        if op == 'D5ONE':
            sg1, ld1 = np.linalg.slogdet(build(1.0)); return ld1 + np.log(sg1.astype(complex)), gap
        sg, ld = np.linalg.slogdet(build(MF)); out = ld + np.log(sg.astype(complex))
        if op == 'D5PV':
            sg1, ld1 = np.linalg.slogdet(build(1.0)); out = out - (ld1 + np.log(sg1.astype(complex)))
        return out, gap
    else:
        raise ValueError(op)
    sg, ld = np.linalg.slogdet(A)
    return ld + np.log(sg.astype(complex)), gap


def entry_log(G, ua, ub, delta, n, nw, op, Fs, Bs, Ls=None, chunk=32):
    """log Z_ab (complex) for the gauge-invariant kernel, and min|eig H| over the evaluated points."""
    ph, w = nodes(G, ua, ub, delta, n, 'tri', nw)
    if len(w) == 0 or w.sum() <= 0: return -np.inf + 0j, np.inf
    D0 = G.D0(ua, ub); ls = []; gm = np.inf
    ck = chunk if op not in ('D5', 'D5PV') else max(1, 4096 // (Ls * G.N) )
    for c in range(0, len(w), ck):
        l, g = logdet_op(G, D_batch(G, D0, Fs, Bs, ph[c:c+ck]), op, Ls)
        ls.append(l)
        if np.any(np.isfinite(g)): gm = min(gm, np.nanmin(g))
    l = np.concatenate(ls); lm = l.real.max()
    return lm + np.log(np.sum(w * np.exp(l - lm)) + 0j), gm


class Pool:
    """unnormalized log-kernel storage for a growing pool; entries computed lazily (upper triangle, Hermitian fill)."""
    def __init__(self, G, delta, n, nw, op, Ls=None):
        self.G, self.delta, self.n, self.nw, self.op, self.Ls = G, delta, n, nw, op, Ls
        self.Fs, self.Bs = G.crossing_mats(); self.U = []; self.L = np.zeros((0, 0), complex); self.gmin = np.inf

    def row(self, u):
        r = [entry_log(self.G, a, u, self.delta, self.n, self.nw, self.op, self.Fs, self.Bs, self.Ls) for a in self.U]
        r.append(entry_log(self.G, u, u, self.delta, self.n, self.nw, self.op, self.Fs, self.Bs, self.Ls))
        return np.array([x[0] for x in r], complex), min(x[1] for x in r)

    def bordered(self, logs):
        k = len(self.U); L = np.full((k + 1, k + 1), -np.inf + 0j); L[:k, :k] = self.L
        L[:k, k] = logs[:k]; L[k, :k] = np.conj(logs[:k]); L[k, k] = logs[k].real
        return L

    def add(self, u, logs, g):
        self.L = self.bordered(logs); self.U.append(u); self.gmin = min(self.gmin, g)


def normalized(L):
    d = L.diagonal().real
    with np.errstate(invalid='ignore', over='ignore', under='ignore'):
        Z = np.where(np.isfinite(L.real), np.exp(L - 0.5 * (d[:, None] + d[None, :])), 0)
    return 0.5 * (Z + Z.conj().T)


def lam(Z):
    ev = np.linalg.eigvalsh(Z); return ev[0], ev[-1], ev


def full_kernel(G, U, delta, n, nw, op, Ls=None):
    P = Pool(G, delta, n, nw, op, Ls)
    for u in U:
        logs, g = P.row(u); P.add(u, logs, g)
    return normalized(P.L), P.gmin


def gen_ratio(Zo, Zw, rel=1e-8):
    """min generalized eigenvalue of (Zo, Zw) on Zw's numerical range (diagnostic only)."""
    w, V = np.linalg.eigh(Zw); keep = w > rel * w[-1]; Vk = V[:, keep] / np.sqrt(w[keep])
    return np.linalg.eigvalsh(Vk.conj().T @ Zo @ Vk).min()
