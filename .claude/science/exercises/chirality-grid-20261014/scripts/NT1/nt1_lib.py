"""NT-1: chiral (Weyl) overlap measure for 2D U(1), Lüscher-type abelian construction (PREREG.md section 2).
Geometry/conventions from K2's lat2d.py (copied unchanged): Lx = 2, open time, antiperiodic x, Wilson r = 1, M = 1.
A joined configuration is a vector of link angles (charge 1) in a fixed link order; D(theta) = 2 + sum_l e^{i th_l} F_l + e^{-i th_l} B_l.
Weyl dets: L -> positive spectral subspace of H_W(U^e) (P̂_-), rows g5 = +1; R -> negative subspace, rows g5 = -1.
Phase: straight-ray parallel transport (W0) + i s_k sum_l A_l kbar_l, div kbar = int_0^1 Anom(tA) dt."""
import numpy as np
from lat2d import Geom, nodes, wrap, GX, GT, I2

M0 = 1.0


class Links:
    def __init__(self, G):
        assert not G.torus and G.Lx == 2
        self.G = G; T, Lx, N = G.T, G.Lx, G.N
        L = []          # (from_site, to_site, dir, bc, key)
        for t in range(-T + 1, T + 1):
            for x in range(Lx):
                L.append((self.site(x, t), self.site(x + 1, t), 'x', G.xbc if x == Lx - 1 else 1.0, ('x', x, t)))
        for t in range(-T + 1, T):
            for x in range(Lx):
                L.append((self.site(x, t), self.site(x, t + 1), 't', 1.0, ('t', x, t)))
        self.L = L; self.nl = len(L); self.key = {l[4]: i for i, l in enumerate(L)}
        F = np.zeros((self.nl, N, N), complex); B = np.zeros((self.nl, N, N), complex)
        for i, (s0, s1, d, bc, _) in enumerate(L):
            g = GX if d == 'x' else GT; a, b = 2 * s0, 2 * s1
            F[i, a:a+2, b:b+2] = -0.5 * (I2 - g) * bc; B[i, b:b+2, a:a+2] = -0.5 * (I2 + g) * bc
        self.F, self.B = F, B
        # fast assembly: D_flat[:, nz] = E @ Fnz, E = [e^{i th}, e^{-i th}]  (same result as the einsum form, checked in gates)
        FB = np.concatenate([F, B]).reshape(2 * self.nl, N * N); self.nz = np.where(np.abs(FB).sum(0) > 0)[0]
        self.FBnz = FB[:, self.nz].copy(); self.D2 = 2.0 * np.eye(N).reshape(N * N)
        self.frm = np.array([l[0] for l in L]); self.to = np.array([l[1] for l in L])
        self.cross = [self.key[('t', x, 0)] for x in range(Lx)]
        self.g5 = G.g5d; self.nsite = N // 2
        # slice index of each site, t-link list per slice
        self.site_t = np.array([s // Lx for s in range(self.nsite)])          # 0..Lt-1  (t = -T+1 + slice)

    def site(self, x, t): return (t + self.G.T - 1) * self.G.Lx + (x % self.G.Lx)

    def base_angles(self, ua, ub):
        """link-angle vector of J(a, b, crossing = 0) (lat2d.links convention)."""
        G = self.G; T, Lx = G.T, G.Lx; A = np.zeros(self.nl)
        for t in range(1, T + 1):
            for x in range(Lx):
                A[self.key[('x', x, t)]] = ua['x'][t-1, x]; A[self.key[('x', x, 1 - t)]] = ub['x'][t-1, x]
        for t in range(1, T):
            for x in range(Lx):
                A[self.key[('t', x, t)]] = ua['t'][t-1, x]; A[self.key[('t', x, -t)]] = -ub['t'][t-1, x]
        return A

    def joined(self, ua, ub, phis):
        A0 = self.base_angles(ua, ub); P = len(phis); A = np.repeat(A0[None], P, 0)
        for x in range(self.G.Lx): A[:, self.cross[x]] = phis[:, x]
        return A

    def D_einsum(self, th):
        e = np.exp(1j * th)
        return 2.0 * np.eye(self.G.N)[None] + np.einsum('pl,lab->pab', e, self.F) + np.einsum('pl,lab->pab', np.conj(e), self.B)

    def D(self, th):
        e = np.exp(1j * th); E = np.concatenate([e, np.conj(e)], 1); N = self.G.N
        out = np.repeat(self.D2[None].astype(complex), th.shape[0], 0); out[:, self.nz] += E @ self.FBnz
        return out.reshape(th.shape[0], N, N)

    def gauge(self, A, om):
        """A_l -> A_l + om(from) - om(to)  (psi(x) -> e^{i om(x)} psi(x))."""
        return A + om[..., self.frm] - om[..., self.to]

    def div(self, k):
        """outflow divergence of a link current k (..., nl) -> (..., nsite)."""
        out = np.zeros(k.shape[:-1] + (self.nsite,))
        np.add.at(out.T, self.frm, k.T); np.add.at(out.T, self.to, -k.T)
        return out

    def current(self, An):
        """K(t)/2 on each t-link, +-(An(0,t) - An(1,t))/4 on the two x-links (PREREG 2(iii)); An: (P, nsite)."""
        G = self.G; Lx, Lt = G.Lx, G.Lt; P = An.shape[0]
        As = An.reshape(P, Lt, Lx); K = np.cumsum(As.sum(2), axis=1)       # K[:, s] = sum_{slices <= s}
        k = np.zeros((P, self.nl))
        for t in range(-G.T + 1, G.T + 1):
            s = t + G.T - 1; r = 0.5 * (As[:, s, 0] - As[:, s, 1])
            k[:, self.key[('x', 0, t)]] = 0.5 * r; k[:, self.key[('x', 1, t)]] = -0.5 * r
            if t < G.T:
                for x in range(Lx): k[:, self.key[('t', x, t)]] = 0.5 * K[:, s]
        return k, K


MODELS = {'11112': [(1, 'L', 4), (2, 'R', 1)], '345': [(3, 'L', 1), (4, 'L', 1), (5, 'R', 1)],
          'L1': [(1, 'L', 1)], 'vecW': [(1, 'L', 1), (1, 'R', 1)]}


class Chiral:
    def __init__(self, LK, model, Ns=32, sk=+1):
        self.LK, self.model, self.Ns, self.sk = LK, MODELS[model], Ns, sk
        self.charges = sorted(set(e for (e, _, _) in self.model))
        N = LK.G.N; self.n = N // 2
        H0 = LK.g5[:, None] * (LK.D(np.zeros((1, LK.nl)))[0] - M0 * np.eye(N))
        w, Q = np.linalg.eigh(H0); assert (w > 0).sum() == self.n, 'free index'
        self.V0 = {'L': Q[:, w > 0], 'R': Q[:, w < 0]}
        self.rows = {'L': np.where(LK.g5 > 0)[0], 'R': np.where(LK.g5 < 0)[0]}

    def logrho(self, A, Ns=None, parts=False):
        """A: (P, nl) charge-1 link angles. Returns W (P,) complex [= W0 + i sk sum A kbar], plus diagnostics."""
        LK = self.LK; Ns = Ns or self.Ns; P, N, n = A.shape[0], LK.G.N, self.n
        ts = np.linspace(0, 1, Ns + 1); wS = np.ones(Ns + 1); wS[1:-1:2] = 4; wS[2:-1:2] = 2; wS *= (1.0 / Ns) / 3  # Simpson
        assert Ns % 2 == 0
        Id = np.eye(N); W0 = np.zeros(P, complex); Abar = np.zeros((P, LK.nsite)); gmin = np.inf; idx_ok = True
        V = {(e, c): np.repeat(self.V0[c][None], P, 0) for (e, c, _) in self.model}
        coefA = {e: sum(m * e * (1 if c == 'L' else -1) for (ee, c, m) in self.model if ee == e) for e in self.charges}
        for j, t in enumerate(ts):
            for e in self.charges:
                H = LK.g5[None, :, None] * (LK.D(t * e * A) - M0 * Id[None])
                w, Q = np.linalg.eigh(H)
                gmin = min(gmin, np.abs(w).min())
                if not np.all((w > 0).sum(1) == n): idx_ok = False
                Sd = np.einsum('pik,pk->pi', np.abs(Q) ** 2, np.sign(w))          # diag of S = sign(H_W)
                q = -0.5 * (Sd[:, 0::2] + Sd[:, 1::2])                            # q_e(x) per site
                Abar += wS[j] * coefA[e] * q
                if j == 0: continue
                for (ee, c, m) in self.model:
                    if ee != e: continue
                    Qs = Q[:, :, n:] if c == 'L' else Q[:, :, :n]                 # eigh sorts ascending
                    X = np.conj(np.swapaxes(Qs, 1, 2)) @ V[(e, c)]
                    u, s, vh = np.linalg.svd(X)
                    V[(e, c)] = Qs @ (u @ vh)
        for (e, c, m) in self.model:
            Vr = V[(e, c)][:, self.rows[c], :]
            sg, ld = np.linalg.slogdet(Vr); W0 += m * (ld + np.log(sg.astype(complex)))
        k, K = LK.current(Abar)
        corr = 1j * self.sk * np.sum(A * k, 1)
        W = W0 + corr
        if parts:
            return W, dict(W0=W0, corr=corr, Abar=Abar, K=K, gmin=gmin, idx_ok=idx_ok, sumA=np.abs(Abar.sum(1)).max())
        return W, gmin, idx_ok


def vec_logdet(LK, A, m=0.0, e=1):
    """massless (m=0) or massive vector-like Neuberger overlap logdet, K2 convention (1 - m/2) D + m."""
    N = LK.G.N; Id = np.eye(N)
    H = LK.g5[None, :, None] * (LK.D(e * A) - M0 * Id[None]); w, V = np.linalg.eigh(H)
    S = (V * np.sign(w)[:, None, :]) @ np.conj(np.swapaxes(V, 1, 2))
    Dm = (1 - m / 2) * (Id[None] + LK.g5[None, :, None] * S) + m * Id[None]
    sg, ld = np.linalg.slogdet(Dm); return ld + np.log(sg.astype(complex)), np.abs(w).min(1)


def entry_chi(LK, CH, ua, ub, n, delta=0.6, weight='hard', chunk=16, Ns=None, op='chi'):
    """log K(a, b) for op in chi (complex chiral), mod (|rho_chi|), W0 (no current), vec0 (massless vector overlap)."""
    ph, w = nodes(LK.G, ua, ub, delta, n, weight)
    if len(w) == 0 or w.sum() <= 0: return -np.inf + 0j, np.inf
    A = LK.joined(ua, ub, ph); ls = []; gm = np.inf
    for c in range(0, len(w), chunk):
        if op == 'vec0':
            l, g = vec_logdet(LK, A[c:c+chunk]); g = g.min()
        else:
            l, g, ok = CH.logrho(A[c:c+chunk], Ns=Ns)
            if not ok: raise RuntimeError('index != 0 on a ray')
            if op == 'mod': l = l.real + 0j
        ls.append(l); gm = min(gm, g)
    l = np.concatenate(ls); lm = l.real.max()
    return lm + np.log(np.sum(w * np.exp(l - lm)) + 0j), gm


def kernel_full(LK, CH, U, n, delta=0.6, op='chi', Ns=None, cphase=0.0):
    """all ordered pairs (no Hermitian fill). cphase: global constant added to every log rho (Theta-reality convention)."""
    k = len(U); L = np.full((k, k), -np.inf + 0j); gm = np.inf
    for a in range(k):
        for b in range(k):
            v, g = entry_chi(LK, CH, U[a], U[b], n, delta, op=op, Ns=Ns); L[a, b] = v + cphase; gm = min(gm, g)
    return L, gm


def normalize_raw(L):
    """Zn without symmetrization; returns Zn, max |Im diag| of log, Hermiticity defect h."""
    d = L.diagonal(); dim = np.abs(np.angle(np.exp(1j * d.imag))).max()
    dr = d.real
    with np.errstate(invalid='ignore', over='ignore', under='ignore'):
        Z = np.where(np.isfinite(L.real), np.exp(L - 0.5 * (dr[:, None] + dr[None, :])), 0)
    h = np.abs(Z - Z.conj().T).max()
    return Z, dim, h
