"""K2 own 2D U(1) lattice code (Wilson r=1 and Neuberger overlap) for the gauge-invariant RP kernel.
Written from scratch for K2 (X3 scripts not imported). Basis: gamma_x = s1, gamma_t = s2, gamma5 = s3.
Sites (x,t), x in Z_Lx, t in {-T+1..T}; reflection theta: t -> 1-t; Lambda+ = {1..T}.
Open time ends (torus=False) or torus in t with antiperiodic fermions (torus=True).
"""
import numpy as np
from scipy.spatial import Delaunay

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1.]).astype(complex)
GX, GT, G5 = s1, s2, s3
I2 = np.eye(2)

def wrap(a): return (a + np.pi) % (2 * np.pi) - np.pi


class Geom:
    def __init__(self, Lx, T, torus=False, xbc=-1):
        self.Lx, self.T, self.torus, self.xbc = Lx, T, torus, xbc
        self.Lt = 2 * T; self.N = 2 * Lx * self.Lt
        self.g5d = np.tile([1., -1.], self.N // 2)

    def idx(self, x, t): return 2 * ((t + self.T - 1) * self.Lx + (x % self.Lx))

    def hop(self, D, x0, t0, x1, t1, g, ph, sign=1.0):
        a = self.idx(x0, t0); b = self.idx(x1, t1); u = sign * np.exp(1j * ph)
        D[a:a+2, b:b+2] += -0.5 * (I2 - g) * u
        D[b:b+2, a:a+2] += -0.5 * (I2 + g) * np.conj(u)

    def links(self, ua, ub):
        """non-crossing link angles: ax[(x,t)], at[(x,t)] (t -> t+1)."""
        T, Lx = self.T, self.Lx; ax = {}; at = {}
        for t in range(1, T + 1):
            for x in range(Lx):
                ax[(x, t)] = ua['x'][t-1, x]; ax[(x, 1 - t)] = ub['x'][t-1, x]
        for t in range(1, T):
            for x in range(Lx):
                at[(x, t)] = ua['t'][t-1, x]; at[(x, -t)] = -ub['t'][t-1, x]
        return ax, at

    def D0(self, ua, ub):
        N, Lx, T = self.N, self.Lx, self.T
        D = 2.0 * np.eye(N, dtype=complex)
        ax, at = self.links(ua, ub)
        for (x, t), ph in ax.items():
            self.hop(D, x, t, x + 1, t, GX, ph, self.xbc if x == Lx - 1 else 1.0)
        for (x, t), ph in at.items():
            self.hop(D, x, t, x, t + 1, GT, ph)
        return D

    def crossing_mats(self):
        """F_j, B_j for crossing links j: plane A (x,0)->(x,1), x=0..Lx-1; torus plane B (x,T)->(x,-T+1), antiperiodic."""
        N, Lx, T = self.N, self.Lx, self.T
        Fs, Bs = [], []
        planes = [(0, 1, 1.0)] + ([(T, -T + 1, -1.0)] if self.torus else [])
        for (t0, t1, sg) in planes:
            for x in range(Lx):
                F = np.zeros((N, N), complex); B = np.zeros((N, N), complex)
                a = self.idx(x, t0); b = self.idx(x, t1)
                F[a:a+2, b:b+2] = -0.5 * (I2 - GT) * sg
                B[b:b+2, a:a+2] = -0.5 * (I2 + GT) * sg
                Fs.append(F); Bs.append(B)
        return np.array(Fs), np.array(Bs)

    def full_D(self, ua, ub, phis):
        D = self.D0(ua, ub); Fs, Bs = self.crossing_mats()
        e = np.exp(1j * np.asarray(phis))
        return D + np.einsum('j,jab->ab', e, Fs) + np.einsum('j,jab->ab', np.conj(e), Bs)


def logdet_batch(geom, D0, Fs, Bs, phis, op, M=1.0, m=0.05, chunk=48):
    """returns logdet (complex) and min|eig H_W| per point (nan for Wilson)."""
    N = geom.N; Id = np.eye(N)
    out = []; gaps = []
    for c in range(0, len(phis), chunk):
        e = np.exp(1j * phis[c:c+chunk])
        D = D0[None] + np.einsum('pj,jab->pab', e, Fs) + np.einsum('pj,jab->pab', np.conj(e), Bs)
        if op == 'W':
            Dm = D + m * Id[None]; gaps.append(np.full(len(e), np.nan))
        else:
            H = geom.g5d[None, :, None] * (D - M * Id[None])
            w, V = np.linalg.eigh(H)
            gaps.append(np.abs(w).min(axis=1))
            S = (V * np.sign(w)[:, None, :]) @ np.conj(np.swapaxes(V, 1, 2))   # memory fix (was a 3-operand einsum with a p*N^3 intermediate)
            Dov = Id[None] + geom.g5d[None, :, None] * S
            Dm = (1 - m / 2) * Dov + m * Id[None]
            del H, V, S, Dov
        sg, ld = np.linalg.slogdet(Dm)
        out.append(ld + np.log(sg.astype(complex)))
        del D, Dm
    return np.concatenate(out), np.concatenate(gaps)


def tri(d, delta): return np.clip(1 - np.abs(d) / delta, 0, None)


def interval_pieces(lo, hi, kinks):
    pts = [lo] + sorted(k for k in kinks if lo < k < hi) + [hi]
    return [(pts[i], pts[i+1]) for i in range(len(pts) - 1) if pts[i+1] - pts[i] > 1e-14]


def gl_interval(pieces, n):
    xg, wg = np.polynomial.legendre.leggauss(n); X = []; W = []
    for (a, b) in pieces:
        X.append(0.5 * (b - a) * xg + 0.5 * (b + a)); W.append(0.5 * (b - a) * wg)
    return (np.concatenate(X), np.concatenate(W)) if X else (np.zeros(0), np.zeros(0))


def plane_offsets(geom, ua, ub):
    """A_x (plane A) and, for torus, B_x (plane B): crossing plaquette = offset_x + phi_{x+1} - phi_x."""
    A = ub['x'][0] - ua['x'][0]
    Bo = ua['x'][geom.T - 1] - ub['x'][geom.T - 1] if geom.torus else None
    return A, Bo


def nodes_1plaq(Aoff, delta, n, weight):
    """Lx = 2 plane: d0 free, d1 = Phi - d0. Returns d0 nodes, weights (incl. gauge weight), phi_1(d0)."""
    Phi = wrap(Aoff.sum())
    lo = max(-delta, Phi - delta); hi = min(delta, Phi + delta)
    if hi <= lo: return np.zeros(0), np.zeros(0), np.zeros(0)
    kinks = [0.0, Phi] if weight == 'tri' else []
    d0, w = gl_interval(interval_pieces(lo, hi, kinks), n)
    if weight == 'tri': w = w * tri(d0, delta) * tri(Phi - d0, delta)
    return d0, w, d0 - Aoff[0]


def cells_Lx4(Phi, delta, weight):
    """convex cells covering {|d_i|<delta (i=0,1,2), |Phi - s| < delta}, s = d0+d1+d2; split at kinks if tri."""
    cells = []
    sig = [(1,), (-1,)] if False else None
    if weight == 'tri':
        pats = [(a, b, c, e) for a in (1, -1) for b in (1, -1) for c in (1, -1) for e in (1, -1)]
    else:
        pats = [None]
    for p in pats:
        # half-spaces as rows (n, c): n.d <= c
        H = []
        for i in range(3):
            ni = np.zeros(3); ni[i] = 1.0
            if p is None:
                H += [(ni, delta), (-ni, delta)]
            else:
                H += [(-p[i] * ni, 0.0), (p[i] * ni, delta)]      # 0 <= p_i d_i <= delta
        one = np.ones(3)
        if p is None:
            H += [(one, Phi + delta), (-one, -(Phi - delta))]
        else:  # 0 <= e (Phi - s) <= delta
            e = p[3]; H += [(e * one, e * Phi), (-e * one, delta - e * Phi)]
        Nn = np.array([h[0] for h in H]); Cc = np.array([h[1] for h in H])
        V = []
        from itertools import combinations
        for (i, j, k) in combinations(range(len(H)), 3):
            A = Nn[[i, j, k]]
            if abs(np.linalg.det(A)) < 1e-12: continue
            v = np.linalg.solve(A, Cc[[i, j, k]])
            if np.all(Nn @ v <= Cc + 1e-12): V.append(v)
        if len(V) < 4: continue
        V = np.unique(np.round(np.array(V), 13), axis=0)
        if len(V) < 4: continue
        try:
            tr = Delaunay(V)
        except Exception:
            continue
        for s in tr.simplices:
            P = V[s]; vol = abs(np.linalg.det((P[1:] - P[0]).T)) / 6
            if vol > 1e-15: cells.append(P)
    return cells


def duffy_tet(P, n):
    xg, wg = np.polynomial.legendre.leggauss(n); xg = 0.5 * (xg + 1); wg = 0.5 * wg
    u, v, w = np.meshgrid(xg, xg, xg, indexing='ij'); Wt = np.einsum('i,j,k->ijk', wg, wg, wg)
    u, v, w, Wt = u.ravel(), v.ravel(), w.ravel(), Wt.ravel()
    x1 = u; x2 = v * (1 - u); x3 = w * (1 - u) * (1 - v)
    J = abs(np.linalg.det((P[1:] - P[0]).T))
    pts = P[0][None] + x1[:, None] * (P[1] - P[0]) + x2[:, None] * (P[2] - P[0]) + x3[:, None] * (P[3] - P[0])
    return pts, Wt * J * (1 - u) ** 2 * (1 - v)


def nodes(geom, ua, ub, delta, n, weight, nw=None):
    """crossing-link angle nodes (P, n_cross) and weights for the gauge-invariant kernel entry (a=ua, b=ub)."""
    Lx = geom.Lx
    A, Bo = plane_offsets(geom, ua, ub)
    if not geom.torus and Lx == 2:
        d0, w, ph1 = nodes_1plaq(A, delta, n, weight)
        return np.stack([np.zeros_like(ph1), ph1], 1), w
    if not geom.torus and Lx == 4:
        Phi = wrap(A.sum())
        if abs(Phi) >= 4 * delta: return np.zeros((0, 4)), np.zeros(0)
        Pts = []; Ws = []
        for P in cells_Lx4(Phi, delta, weight):
            pts, wt = duffy_tet(P, n); Pts.append(pts); Ws.append(wt)
        if not Pts: return np.zeros((0, 4)), np.zeros(0)
        d = np.concatenate(Pts); w = np.concatenate(Ws)
        if weight == 'tri':
            w = w * tri(d[:, 0], delta) * tri(d[:, 1], delta) * tri(d[:, 2], delta) * tri(Phi - d.sum(1), delta)
        ph1 = d[:, 0] - A[0]; ph2 = ph1 + d[:, 1] - A[1]; ph3 = ph2 + d[:, 2] - A[2]
        return np.stack([np.zeros_like(ph1), ph1, ph2, ph3], 1), w
    if geom.torus and Lx == 2:
        dA, wA, pA = nodes_1plaq(A, delta, n, weight)
        dB, wB, pB = nodes_1plaq(Bo, delta, n, weight)
        if len(wA) == 0 or len(wB) == 0: return np.zeros((0, 4)), np.zeros(0)
        ws = 2 * np.pi * np.arange(nw) / nw; ww = np.full(nw, 2 * np.pi / nw)
        iA, iB, iW = np.meshgrid(np.arange(len(wA)), np.arange(len(wB)), np.arange(nw), indexing='ij')
        iA, iB, iW = iA.ravel(), iB.ravel(), iW.ravel()
        chi0 = ws[iW]; chi1 = chi0 + pB[iB]          # chi_1 = w + d^B_0 - B_0
        phis = np.stack([np.zeros(len(iA)), pA[iA], chi0, chi1], 1)
        return phis, wA[iA] * wB[iB] * ww[iW]
    raise ValueError('geometry not supported')


def rand_half(rng, geom, s, delta, maxtry=100000):
    T, Lx = geom.T, geom.Lx
    for _ in range(maxtry):
        ux = rng.normal(0, s, (T, Lx)); ut = rng.normal(0, s, (T - 1, Lx))
        ok = True
        for t in range(T - 1):
            for x in range(Lx):
                p = ux[t, x] + ut[t, (x + 1) % Lx] - ux[t + 1, x] - ut[t, x]
                if abs(wrap(p)) >= delta: ok = False
        if ok: return {'x': ux, 't': ut}
    raise RuntimeError('no admissible config')


def kernel(geom, U, delta, n, weight, op, nw=None, M=1.0, m=0.05, sym=True):
    """normalized kernel Zn (k x k), min|H_W| over all points, symmetry defect, raw log-scale info."""
    k = len(U); Fs, Bs = geom.crossing_mats()
    Lg = np.full((k, k), -np.inf); Mt = np.zeros((k, k), complex); gmin = np.inf; imag_max = 0.0
    pairs = [(a, b) for a in range(k) for b in range(k) if (b >= a or not sym)]
    for (a, b) in pairs:
        ph, w = nodes(geom, U[a], U[b], delta, n, weight, nw)
        if len(w) == 0 or w.sum() == 0: continue
        l, g = logdet_batch(geom, geom.D0(U[a], U[b]), Fs, Bs, ph, op, M, m)
        if op == 'O': gmin = min(gmin, np.nanmin(g))
        lm = l.real.max(); val = np.sum(w * np.exp(l - lm))
        imag_max = max(imag_max, abs(val.imag) / max(abs(val.real), 1e-300))
        Lg[a, b] = lm; Mt[a, b] = val
        if sym and a != b: Lg[b, a] = lm; Mt[b, a] = np.conj(val)
    d = Lg.diagonal(); md = Mt.diagonal().real
    with np.errstate(invalid='ignore', over='ignore'):
        Zn = np.where(np.isfinite(Lg), Mt * np.exp(Lg - 0.5 * (d[:, None] + d[None, :])), 0) / np.sqrt(np.outer(md, md))
    return Zn, gmin, imag_max


def mineig(Z):
    ev = np.linalg.eigvalsh(0.5 * (Z + Z.conj().T)); return ev.min() / np.abs(ev).max()
