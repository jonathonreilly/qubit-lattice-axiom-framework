"""NT-1' library: chiral (Weyl) overlap measure for 2D U(1) on an open-time strip, general Lx, antiperiodic x (fermions).
Conventions as K2's lat2d.py (copied unchanged) and NT-1's nt1_lib.py (refereed): gamma_x = s1, gamma_t = s2, gamma5 = s3,
Wilson r = 1, M = 1, H_W = g5 (D - M), S = sign H_W, D_ov = 1 + g5 S.  L Weyl <-> positive subspace of H_W(U^e), rows g5 = +1;
R Weyl <-> negative subspace, rows g5 = -1.
Measure (PREREG section 4): W[A] = W0[A] + i s_k sum_l A_l kbb_l[A], evaluated on the canonical theta-covariant gauge rep A_c.
kbb = int_0^1 k[tA] dt with k = k_loc + Q(Anom - div k_loc), k_loc = sum_p F_p int_0^1 du kappa_p[uB] (local Poincare lemma of the
gauge-invariant plaquette derivative of the anomaly, monopole defect m_p removed at the plaquette corners)."""
import numpy as np

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1.]).astype(complex)
I2 = np.eye(2); M0 = 1.0

MODELS = {'11112': [(1, 'L', 4), (2, 'R', 1)], '345': [(3, 'L', 1), (4, 'L', 1), (5, 'R', 1)],
          'L1': [(1, 'L', 1)], 'L2': [(2, 'L', 1)], 'vec1': [(1, 'L', 1), (1, 'R', 1)]}


class Strip:
    """open time t = -T+1..T, x in Z_Lx (gauge periodic, fermion antiperiodic in x). Link order: all x-links (slice-major),
    then all t-links (x,t)->(x,t+1), t = -T+1..T-1 (crossing links are t = 0)."""
    def __init__(self, Lx, T, xbc=-1.0):
        self.Lx, self.T, self.Lt = Lx, T, 2 * T; self.ns = Lx * self.Lt; self.N = 2 * self.ns; self.xbc = xbc
        L = []
        for t in range(-T + 1, T + 1):
            for x in range(Lx):
                L.append((self.site(x, t), self.site(x + 1, t), 'x', xbc if x == Lx - 1 else 1.0, x, t))
        for t in range(-T + 1, T):
            for x in range(Lx):
                L.append((self.site(x, t), self.site(x, t + 1), 't', 1.0, x, t))
        self.L = L; self.nl = len(L); self.nx = Lx * self.Lt
        self.key = {(l[2], l[4], l[5]): i for i, l in enumerate(L)}
        self.frm = np.array([l[0] for l in L]); self.to = np.array([l[1] for l in L])
        self.g5 = np.tile([1., -1.], self.ns)
        self.site_t = np.array([s // Lx - T + 1 for s in range(self.ns)]); self.site_x = np.array([s % Lx for s in range(self.ns)])
        # hop blocks: D[a, b] += Fblk * e^{i th}, D[b, a] += Bblk * e^{-i th}
        self.Fb = np.zeros((self.nl, 2, 2), complex); self.Bb = np.zeros((self.nl, 2, 2), complex)
        N = self.N; Fi = []; Fj = []; Fv = []; Bi = []; Bj = []; Bv = []
        for i, (s0, s1_, d, bc, _, _) in enumerate(L):
            g = s1 if d == 'x' else s2; Fb = -0.5 * (I2 - g) * bc; Bb = -0.5 * (I2 + g) * bc
            self.Fb[i] = Fb; self.Bb[i] = Bb
            for al in range(2):
                for be in range(2):
                    if Fb[al, be] != 0: Fi.append((i, 2 * s0 + al, 2 * s1_ + be, Fb[al, be]))
                    if Bb[al, be] != 0: Bi.append((i, 2 * s1_ + al, 2 * s0 + be, Bb[al, be]))
        self.Fl = np.array([f[0] for f in Fi]); self.Fr = np.array([f[1] for f in Fi]); self.Fc = np.array([f[2] for f in Fi]); self.Fv = np.array([f[3] for f in Fi])
        self.Bl = np.array([f[0] for f in Bi]); self.Br = np.array([f[1] for f in Bi]); self.Bc = np.array([f[2] for f in Bi]); self.Bv = np.array([f[3] for f in Bi])
        # plaquettes p = (x, t), t = -T+1..T-1: F = A_x(x,t) + A_t(x+1,t) - A_x(x,t+1) - A_t(x,t)
        self.plaq = []; Pm = np.zeros((Lx * (self.Lt - 1), self.nl))
        for t in range(-T + 1, T):
            for x in range(Lx):
                ip = len(self.plaq); self.plaq.append((x, t))
                Pm[ip, self.key[('x', x, t)]] += 1; Pm[ip, self.key[('t', (x + 1) % Lx, t)]] += 1
                Pm[ip, self.key[('x', x, t + 1)]] -= 1; Pm[ip, self.key[('t', x, t)]] -= 1
        self.Pm = Pm; self.np_ = len(self.plaq)
        Wm = np.zeros((self.Lt, self.nl))
        for t in range(-T + 1, T + 1):
            for x in range(Lx): Wm[t + T - 1, self.key[('x', x, t)]] = 1.0
        self.Wm = Wm
        self.xl = np.array([[self.key[('x', x, t)] for x in range(Lx)] for t in range(-T + 1, T + 1)])   # (Lt, Lx)
        self.tl = np.array([[self.key[('t', x, t)] for x in range(Lx)] for t in range(-T + 1, T)])      # (Lt-1, Lx)
        self._paths()

    def site(self, x, t): return (t + self.T - 1) * self.Lx + (x % self.Lx)

    # ---------------- operators ----------------
    def D(self, th):
        """massless Wilson operator for link angles th (P, nl) (charge already applied)."""
        P = th.shape[0]; N = self.N; ns = self.ns
        out = np.zeros((P, ns, 2, ns, 2), complex)
        out[:, np.arange(ns), :, np.arange(ns), :] = 2.0 * I2
        e = np.exp(1j * th)
        for i in range(self.nl):
            a, b = self.frm[i], self.to[i]
            out[:, a, :, b, :] += e[:, i, None, None] * self.Fb[i][None]
            out[:, b, :, a, :] += np.conj(e[:, i])[:, None, None] * self.Bb[i][None]
        return out.reshape(P, N, N)

    def H(self, th):
        D = self.D(th); D[:, np.arange(self.N), np.arange(self.N)] -= M0
        return self.g5[None, :, None] * D

    def div(self, k):
        """outflow divergence of link currents k (..., nl) -> (..., ns)."""
        out = np.zeros(k.shape[:-1] + (self.ns,))
        for i in range(self.nl):
            out[..., self.frm[i]] += k[..., i]; out[..., self.to[i]] -= k[..., i]
        return out

    def gauge(self, A, om):
        """A_l -> A_l + om(from) - om(to)."""
        return A + om[..., self.frm] - om[..., self.to]

    # ---------------- gauge-invariant data, canonical gauge ----------------
    def FW(self, A):
        return A @ self.Pm.T, A @ self.Wm.T          # plaquettes (P, np), Wilson lines (P, Lt)

    def canon(self, A):
        """canonical theta-covariant representative: A_t = 0; A_x(x,0) + A_x(x,1) = (W_0 + W_1)/Lx."""
        F, W = self.FW(A); T, Lx = self.T, self.Lx; P = A.shape[0]
        F = F.reshape(P, self.Lt - 1, Lx)            # F[:, t + T - 1, x]
        Ax = np.zeros((P, self.Lt, Lx))
        i0, i1 = T - 1, T                            # slice indices of t = 0, 1
        Ax[:, i0] = 0.5 * ((W[:, i0] + W[:, i1])[:, None] / Lx + F[:, i0])
        for i in range(i0, self.Lt - 1): Ax[:, i + 1] = Ax[:, i] - F[:, i]
        for i in range(i0 - 1, -1, -1): Ax[:, i] = Ax[:, i + 1] + F[:, i]
        out = np.zeros((P, self.nl)); out[:, self.xl.reshape(-1)] = Ax.reshape(P, -1)
        return out

    def theta(self, A):
        """link reflection t -> 1 - t: x-link (x,t) <- (x,1-t); t-link (x,t)->(x,t+1) <- minus t-link (x,-t)."""
        out = np.zeros_like(A)
        for t in range(-self.T + 1, self.T + 1):
            out[:, self.xl[t + self.T - 1]] = A[:, self.xl[(1 - t) + self.T - 1]]
        for t in range(-self.T + 1, self.T):
            out[:, self.tl[t + self.T - 1]] = -A[:, self.tl[(-t) + self.T - 1]]
        return out

    def joined(self, ua, ub, phis):
        """lat2d convention: Lambda+ = ua (slices 1..T), Lambda- = mirror of ub, crossing t-links (x,0) = phis[:, x]."""
        T, Lx = self.T, self.Lx; A0 = np.zeros(self.nl)
        for t in range(1, T + 1):
            for x in range(Lx):
                A0[self.key[('x', x, t)]] = ua['x'][t - 1, x]; A0[self.key[('x', x, 1 - t)]] = ub['x'][t - 1, x]
        for t in range(1, T):
            for x in range(Lx):
                A0[self.key[('t', x, t)]] = ua['t'][t - 1, x]; A0[self.key[('t', x, -t)]] = -ub['t'][t - 1, x]
        A = np.repeat(A0[None], len(phis), 0)
        for x in range(Lx): A[:, self.key[('t', x, 0)]] = phis[:, x]
        return A

    # ---------------- fixed right inverse Q and Poincare paths ----------------
    def Q(self, f):
        """f (..., ns) with zero total sum -> link current k with div k = f (NT-1's construction generalized)."""
        T, Lx, Lt = self.T, self.Lx, self.Lt
        fs = f.reshape(f.shape[:-1] + (Lt, Lx)); fh = fs.sum(-1); K = np.cumsum(fh, -1)   # K[..., i] = sum_{slices <= i}
        k = np.zeros(f.shape[:-1] + (self.nl,))
        for i in range(Lt - 1): k[..., self.tl[i]] = (K[..., i] / Lx)[..., None]
        for i in range(Lt):
            g = fs[..., i, :] - fh[..., i, None] / Lx; c = np.cumsum(g, -1); c = c - c.mean(-1, keepdims=True)
            k[..., self.xl[i]] = c
        return k

    def _path_current(self, z, c):
        """symmetric unit current from site z to site c: average of t-first and x-first L-paths; both arcs at antipodal dx."""
        Lx, T = self.Lx, self.T
        xz, tz = z % Lx, z // Lx - T + 1; xc, tc = c % Lx, c // Lx - T + 1
        dx = (xc - xz) % Lx
        arcs = [+1] if 2 * dx < Lx else ([-1] if 2 * dx > Lx else [+1, -1])
        cur = np.zeros(self.nl); w = 1.0 / (2 * len(arcs)) if dx != 0 and tz != tc else (1.0 / len(arcs) if dx != 0 else 1.0)
        def tmove(x, t0, t1, cur, w):
            s = 1 if t1 > t0 else -1
            for t in range(t0, t1, s):
                tt = t if s > 0 else t - 1
                cur[self.key[('t', x, tt)]] += s * w
        def xmove(t, x0, nstep, d, cur, w):
            x = x0
            for _ in range(nstep):
                if d > 0: cur[self.key[('x', x, t)]] += w; x = (x + 1) % Lx
                else: x = (x - 1) % Lx; cur[self.key[('x', x, t)]] -= w
        if dx == 0:
            tmove(xz, tz, tc, cur, 1.0); return cur
        if tz == tc:
            for d in arcs: xmove(tz, xz, dx if d > 0 else Lx - dx, d, cur, w)
            return cur
        for d in arcs:
            n = dx if d > 0 else Lx - dx
            tmove(xz, tz, tc, cur, w); xmove(tc, xz, n, d, cur, w)          # t-first
            xmove(tz, xz, n, d, cur, w); tmove(xc, tz, tc, cur, w)          # x-first
        return cur

    def _paths(self):
        """Pi[c] (nl x ns): column z = unit current z -> c.  Corner-averaged operator per plaquette: PK[p] (nl x ns)."""
        ns = self.ns; Pi = np.zeros((ns, self.nl, ns))
        for c in range(ns):
            for z in range(ns):
                if z != c: Pi[c, :, z] = self._path_current(z, c)
        self.PK = np.zeros((self.np_, self.nl, ns)); self.corners = np.zeros((self.np_, ns))
        for ip, (x, t) in enumerate(self.plaq):
            cs = [self.site(x, t), self.site(x + 1, t), self.site(x + 1, t + 1), self.site(x, t + 1)]
            for c in cs: self.PK[ip] += 0.25 * Pi[c]; self.corners[ip, c] += 0.25
        # string matrices for plaquette derivatives: STR_up[p] = coefficient vector over x-links (len nl), STR_dn[p]
        self.Sup = np.zeros((self.np_, self.nl)); self.Sdn = np.zeros((self.np_, self.nl))
        for ip, (x, t) in enumerate(self.plaq):
            for tt in range(t + 1, self.T + 1): self.Sup[ip, self.key[('x', x, tt)]] = -1.0
            for tt in range(-self.T + 1, t + 1): self.Sdn[ip, self.key[('x', x, tt)]] = +1.0
        # selector: use up-string for sites with t_x <= t_p, down-string otherwise
        tp = np.array([t for (_, t) in self.plaq])
        self.use_up = (self.site_t[None, :] <= tp[:, None])          # (np, ns)
        self.Wunif = np.zeros(self.nl); self.Wunif[self.xl.reshape(-1)] = 1.0 / self.Lx


# ---------------- spectral pieces ----------------
def eig_H(S, th):
    w, V = np.linalg.eigh(S.H(th)); return w, V


def q_of(S, w, V):
    """q(x) = -1/2 tr_spin sign(H)(x,x) for a batch."""
    Sd = np.einsum('pak,pk->pa', np.abs(V) ** 2, np.sign(w))
    return -0.5 * (Sd[:, 0::2] + Sd[:, 1::2])


def dq_dA(S, th, w, V):
    """R_raw[p, x, l] = d q(x) / d th_l at the field th (charge-e angles), analytic spectral derivative:
    dS_aa = 2 Re sum_{i+, j-} C_ij Vp_ai conj(Vm_aj) X^l_ij, X^l = Vp^dag dH/dth_l Vm, C_ij = 2/(w_i - w_j)."""
    P, N = w.shape; n = N // 2
    assert np.all((w > 0).sum(1) == n)
    Vp = V[:, :, n:]; Vm = V[:, :, :n]; wp = w[:, n:]; wm = w[:, :n]           # eigh ascending
    C = 2.0 / (wp[:, :, None] - wm[:, None, :])                                 # (P, n, n)
    e = np.exp(1j * th)
    Vp5 = Vp.reshape(P, S.ns, 2, n); Vm5 = Vm.reshape(P, S.ns, 2, n)
    gF = s3[None] @ S.Fb; gB = s3[None] @ S.Bb                                  # g5 row scaling of the hop blocks
    cF = 1j * e[:, :, None, None] * gF[None]; cB = -1j * np.conj(e)[:, :, None, None] * gB[None]   # (P, nl, 2, 2)
    Phi = ((Vp[:, :, :, None] * np.conj(Vm)[:, :, None, :]) * C[:, None]).reshape(P, N, n * n)   # (P, N, n*n)
    Rr = np.zeros((P, N, S.nl)); LC = 64 if N <= 96 else 24                     # link chunks (memory)
    for l0 in range(0, S.nl, LC):
        sl = slice(l0, min(l0 + LC, S.nl)); fr = S.frm[sl]; to = S.to[sl]
        X = np.einsum('plai,plab,plbj->plij', np.conj(Vp5[:, fr]), cF[:, sl], Vm5[:, to], optimize=True)
        X += np.einsum('plai,plab,plbj->plij', np.conj(Vp5[:, to]), cB[:, sl], Vm5[:, fr], optimize=True)
        Rr[:, :, sl] = 2 * np.real(Phi @ np.swapaxes(X.reshape(P, -1, n * n), 1, 2)); del X
    return -0.5 * (Rr[:, 0::2] + Rr[:, 1::2])                                    # (P, ns, nl)


class Measure:
    def __init__(self, S, model, Ns=8, sk=+1, use_Q=True):
        self.S, self.model, self.Ns, self.sk, self.use_Q = S, MODELS[model], Ns, sk, use_Q
        self.charges = sorted(set(e for (e, _, _) in self.model))
        self.coef = {e: sum(m * e * (1 if c == 'L' else -1) for (ee, c, m) in self.model if ee == e) for e in self.charges}
        w0, V0 = eig_H(S, np.zeros((1, S.nl))); n = S.N // 2
        assert (w0 > 0).sum() == n
        self.V0 = {'L': V0[0][:, n:], 'R': V0[0][:, :n]}
        self.rows = {'L': np.where(S.g5 > 0)[0], 'R': np.where(S.g5 < 0)[0]}
        self.free = {e: (w0, V0) for e in self.charges}

    def ray(self, A, Ns, need_k=True):
        """A: (P, nl) canonical-gauge angles. Returns dict with W0 (plain transport at Ns and Ns/2), kbb, Abar, diagnostics."""
        S = self.S; P = A.shape[0]; n = S.N // 2; ts = np.arange(Ns + 1) / Ns
        V = {}; V2 = {}
        for (e, c, m) in self.model: V[(e, c)] = np.repeat(self.V0[c][None], P, 0); V2[(e, c)] = V[(e, c)].copy()
        sw = np.ones(Ns + 1); sw[1:-1:2] = 4; sw[2:-1:2] = 2; sw *= 1.0 / (3 * Ns)          # Simpson weights
        Abar = np.zeros((P, S.ns)); kap = np.zeros((P, S.np_, S.nl)); mbar = np.zeros((P, S.np_)); hbar = np.zeros((P, S.ns))
        gmin = np.inf; idx_ok = True; idchk = 0.0
        F, Wl = S.FW(A); Wx = Wl[:, S.site_t + S.T - 1]          # Wilson line of each site's slice
        for j, t in enumerate(ts):
            Rtot = np.zeros((P, S.ns, S.nl)); qtot = np.zeros((P, S.ns))
            for e in self.charges:
                th = t * e * A
                w, Vv = eig_H(S, th) if j > 0 else (np.repeat(self.free[e][0], P, 0), np.repeat(self.free[e][1], P, 0))
                gmin = min(gmin, np.abs(w).min()); idx_ok &= bool(np.all((w > 0).sum(1) == n))
                qtot += self.coef[e] * q_of(S, w, Vv)
                if need_k: Rtot += self.coef[e] * e * dq_dA(S, th, w, Vv)
                if j > 0:
                    for (ee, c, m) in self.model:
                        if ee != e: continue
                        Qs = Vv[:, :, n:] if c == 'L' else Vv[:, :, :n]
                        u_, s_, vh = np.linalg.svd(np.conj(np.swapaxes(Qs, 1, 2)) @ V[(e, c)]); V[(e, c)] = Qs @ (u_ @ vh)
                        if j % 2 == 0:
                            u_, s_, vh = np.linalg.svd(np.conj(np.swapaxes(Qs, 1, 2)) @ V2[(e, c)]); V2[(e, c)] = Qs @ (u_ @ vh)
            Abar += sw[j] * qtot
            if need_k:
                # gauge-invariant plaquette derivatives g'(x, p) and Wilson-line response h(x)
                gup = np.einsum('pxl,ql->pqx', Rtot, S.Sup); gdn = np.einsum('pxl,ql->pqx', Rtot, S.Sdn)
                g = np.where(S.use_up[None], gup, gdn)                          # (P, np, ns)
                h = Rtot @ S.Wunif                                              # (P, ns)
                lhs = np.einsum('pxl,pl->px', Rtot, A); rhs = np.einsum('pq,pqx->px', F, g) + Wx * h
                idchk = max(idchk, np.abs(lhs - rhs).max())
                m = g.sum(-1)                                                   # monopole defects (P, np)
                src = g - m[:, :, None] * S.corners[None]
                kp = np.einsum('qls,pqs->pql', S.PK, src)                       # kappa_p (P, np, nl)
                kap += sw[j] * (1 - t) * kp; mbar += sw[j] * m; hbar += sw[j] * h
        out = {}
        for nm, VV in (('W0', V), ('W0half', V2)):
            W0 = np.zeros(P, complex)
            for (e, c, m) in self.model:
                sg, ld = np.linalg.slogdet(VV[(e, c)][:, self.rows[c], :]); W0 += m * (ld + np.log(sg.astype(complex)))
            out[nm] = W0
        out.update(Abar=Abar, gmin=gmin, idx_ok=idx_ok, idchk=idchk, sumA=np.abs(Abar.sum(1)).max())
        if need_k:
            kloc = np.einsum('pq,pql->pl', F, kap)
            corr = S.Q(Abar - S.div(kloc)) if self.use_Q else 0.0 * kloc
            out.update(kbb=kloc + corr, kloc=kloc, kQ=corr, mbar=mbar, hbar=hbar)
        return out

    def logrho(self, A, Ns=None, canon=True, parts=False):
        """W = W0 (Richardson R(Ns/2) = (4 W(Ns) - W(Ns/2))/3) + i s_k sum A_c kbb."""
        Ns = Ns or self.Ns; S = self.S
        Ac = S.canon(A) if canon else A
        r = self.ray(Ac, Ns)
        Wa, Wb = r['W0half'], r['W0']
        Wa = Wa + 2j * np.pi * np.round((Wb - Wa).imag / (2 * np.pi))
        W0 = (4 * Wb - Wa) / 3
        W = W0 + 1j * self.sk * np.sum(Ac * r['kbb'], 1)
        if parts: return W, r, Ac
        return W, r['gmin'], r['idx_ok']


def vec_logdet(S, A, m=0.0, e=1):
    """vector-like Neuberger overlap logdet, K2 convention (1 - m/2) D_ov + m."""
    N = S.N; Id = np.eye(N); w, V = eig_H(S, e * A)
    Sg = (V * np.sign(w)[:, None, :]) @ np.conj(np.swapaxes(V, 1, 2))
    Dm = (1 - m / 2) * (Id[None] + S.g5[None, :, None] * Sg) + m * Id[None]
    sg, ld = np.linalg.slogdet(Dm); return ld + np.log(sg.astype(complex)), np.abs(w).min(1)
