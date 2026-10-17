"""TOR-1 library: Luscher's finite-volume chiral (Weyl) overlap measure for 2D U(1) on an Lx x Lt TORUS (PREREG section 2).
Conventions as NT-1' (nt1p_lib.py, copied unchanged and imported for dq_dA / q_of): gamma_x = s1, gamma_t = s2, gamma5 = s3,
Wilson r = 1, M = 1, H_W = g5 (D - M), D_ov = 1 + g5 sign H.  L Weyl <-> positive subspace of H(U^e), rows g5 = +1;
R Weyl <-> negative subspace, rows g5 = -1.
Fermions antiperiodic in x (sign on x-links x = Lx-1 -> 0) and in t (sign on the plane-B crossing t-links (x,T)->(x,T+1)).
Measure (Luscher hep-lat/9811032 sects. 7-11): on the canonical decomposition U ~ U[w] e^{i A^T} (Lemma 7.4),
  log rho = sum_f m_f log det(v_f[rows_f])   (basis: toron-torus transport (momentum space) along 0 -> (wx,0) -> (wx,wt),
                                               then transverse straight curve U[w] e^{i s A^T}, polar/SVD steps, Richardson)
            - i wt (Gam_t(wx) - Gam_t(0)) / 2pi   (Lemma 9.2 connection S on the toron torus; Gam_t = lifted arg of the
                                               multiplet Berry holonomy around the wt-cycle at fixed wx)
            + i s_k sum_l A^T_l kbb_l          (eq. 5.8 measure-term phase; kbb = int_0^1 (1-s) kappa[s] ds, local Poincare
                                               current of the multiplet anomaly's plaquette derivative).
Single-valuedness algebra (why the S sign is what it is): continuing wt -> wt + 2pi multiplies the transported det by the
holonomy h_t(wx) = exp(i Gam_t(wx)) and the S factor by exp(-i (Gam_t(wx) - Gam_t(0))), net h_t(0); continuing wx -> wx + 2pi
gives h_x(0) * exp(-i wt * winding(Gam_t)).  So rho is single-valued iff h_x(0) = h_t(0) = 1 and the winding is 0."""
import numpy as np
from nt1p_lib import dq_dA, q_of, MODELS, s1, s2, s3, I2

M0 = 1.0


class Torus:
    def __init__(self, Lx, Lt, light=False):
        assert Lx >= 3 and Lt >= 4 and Lt % 2 == 0
        self.light = light
        self.Lx, self.Lt, self.T = Lx, Lt, Lt // 2
        self.ns = Lx * Lt; self.N = 2 * self.ns; self.V = self.ns
        T = self.T; L = []
        for t in range(Lt):
            for x in range(Lx):
                L.append((self.site(x, t), self.site(x + 1, t), 'x', -1.0 if x == Lx - 1 else 1.0, x, t))
        for t in range(Lt):
            for x in range(Lx):
                L.append((self.site(x, t), self.site(x, t + 1), 't', -1.0 if t == T else 1.0, x, t))
        self.L = L; self.nl = len(L)
        self.key = {(l[2], l[4], l[5]): i for i, l in enumerate(L)}
        self.frm = np.array([l[0] for l in L]); self.to = np.array([l[1] for l in L])
        self.isx = np.array([l[2] == 'x' for l in L])
        self.g5 = np.tile([1., -1.], self.ns)
        self.site_t = np.array([s // Lx for s in range(self.ns)]); self.site_x = np.array([s % Lx for s in range(self.ns)])
        self.Fb = np.zeros((self.nl, 2, 2), complex); self.Bb = np.zeros((self.nl, 2, 2), complex)
        N = self.N; self.Gsum = {k: np.zeros((N, N), complex) for k in ('fx', 'bx', 'ft', 'bt')}
        if not light: self.Fm = np.zeros((self.nl, N, N), complex); self.Bm = np.zeros((self.nl, N, N), complex)
        for i, (a, b, d, bc, _, _) in enumerate(L):
            g = s1 if d == 'x' else s2; Fb = -0.5 * (I2 - g) * bc; Bb = -0.5 * (I2 + g) * bc
            self.Fb[i] = Fb; self.Bb[i] = Bb
            self.Gsum['f' + d][2 * a:2 * a + 2, 2 * b:2 * b + 2] += Fb; self.Gsum['b' + d][2 * b:2 * b + 2, 2 * a:2 * a + 2] += Bb
            if not light:
                self.Fm[i, 2 * a:2 * a + 2, 2 * b:2 * b + 2] = Fb; self.Bm[i, 2 * b:2 * b + 2, 2 * a:2 * a + 2] = Bb
        # plaquettes p = (x, t): F = A_x(x,t) + A_t(x+1,t) - A_x(x,t+1) - A_t(x,t)
        self.plaq = []; Pm = np.zeros((self.ns, self.nl))
        for t in range(Lt):
            for x in range(Lx):
                ip = len(self.plaq); self.plaq.append((x, t))
                Pm[ip, self.key[('x', x, t)]] += 1; Pm[ip, self.key[('t', (x + 1) % Lx, t)]] += 1
                Pm[ip, self.key[('x', x, (t + 1) % Lt)]] -= 1; Pm[ip, self.key[('t', x, t)]] -= 1
        self.Pm = Pm; self.np_ = self.ns
        self.aP = np.linalg.pinv(Pm) if not light else None                      # (nl, np): transverse zero-mean potential of unit flux (compensated)
        self.xl = np.array([[self.key[('x', x, t)] for x in range(Lx)] for t in range(Lt)])   # (Lt, Lx)
        self.tl = np.array([[self.key[('t', x, t)] for x in range(Lx)] for t in range(Lt)])   # (Lt, Lx)
        self.Wx_ref = np.zeros(self.nl); self.Wx_ref[self.xl[1]] = 1.0      # x-Wilson line at slice t = 1
        self.Wt_ref = np.zeros(self.nl); self.Wt_ref[self.tl[:, 0]] = 1.0   # t-Wilson line at column x = 0
        self.Ux = np.zeros(self.nl); self.Ux[self.isx] = 1.0 / Lx         # uniform toron directions
        self.Ut = np.zeros(self.nl); self.Ut[~self.isx] = 1.0 / Lt
        if not light: self._paths()
        self._momenta()

    def site(self, x, t): return (t % self.Lt) * self.Lx + (x % self.Lx)

    # ---------------- operators ----------------
    def D(self, th):
        e = np.exp(1j * th)
        return 2.0 * np.eye(self.N)[None] + np.einsum('pl,lij->pij', e, self.Fm) + np.einsum('pl,lij->pij', np.conj(e), self.Bm)

    def H(self, th):
        D = self.D(th); D[:, np.arange(self.N), np.arange(self.N)] -= M0
        return self.g5[None, :, None] * D

    def div(self, k):
        out = np.zeros(k.shape[:-1] + (self.ns,))
        for i in range(self.nl):
            out[..., self.frm[i]] += k[..., i]; out[..., self.to[i]] -= k[..., i]
        return out

    def gauge(self, A, om):
        return A + om[..., self.frm] - om[..., self.to]

    # ---------------- canonical decomposition (Luscher Lemma 7.4) ----------------
    def decompose(self, th):
        """th (P, nl) link angles -> F (reduced), Q, A^T, w = (wx, wt) real lifts, canonical A_c."""
        Fr = th @ self.Pm.T; F = (Fr + np.pi) % (2 * np.pi) - np.pi
        Q = np.round(F.sum(1) / (2 * np.pi)).astype(int)
        AT = F @ self.aP.T
        wx = (th - AT) @ self.Wx_ref; wt = (th - AT) @ self.Wt_ref
        return F, Q, AT, np.stack([wx, wt], 1)

    def canon(self, AT, w):
        return AT + w[:, 0:1] * self.Ux[None] + w[:, 1:2] * self.Ut[None]

    def theta(self, A):
        """link reflection t -> 1 - t: x-link (x,t) <- (x,1-t); t-link (x,t)->(x,t+1) <- minus t-link (x,-t)."""
        out = np.zeros_like(A); Lt = self.Lt
        for t in range(Lt):
            out[:, self.xl[t]] = A[:, self.xl[(1 - t) % Lt]]
            out[:, self.tl[t]] = -A[:, self.tl[(-t) % Lt]]
        return out

    # ---------------- momentum space (zero-field toron fields) ----------------
    def _momenta(self):
        Lx, Lt, T = self.Lx, self.Lt, self.T
        kx = (2 * np.arange(Lx) + 1) * np.pi / Lx; kt = (2 * np.arange(Lt) + 1) * np.pi / Lt
        sig = np.where(self.site_t <= T, 1.0, -1.0)            # moves the t-sign from plane B to the wrap
        Ph = np.zeros((self.ns, len(kx) * len(kt)), complex); self.klist = []
        j = 0
        for a in kt:
            for b in kx:
                Ph[:, j] = np.exp(1j * (b * self.site_x + a * self.site_t)) * sig / np.sqrt(self.ns); self.klist.append((b, a)); j += 1
        self.Ph = Ph; self.nk = Ph.shape[1]
        # 2x2 blocks of the four hopping generators
        PhS = np.kron(Ph, np.eye(2))                              # (N, 2 nk): column 2j+al = Ph_j (x) e_al
        gens = {}
        for nm in ('fx', 'bx', 'ft', 'bt'):
            G = self.Gsum[nm]; Gk = np.conj(PhS.T) @ G @ PhS
            blk = np.array([Gk[2 * j:2 * j + 2, 2 * j:2 * j + 2] for j in range(self.nk)])
            off = Gk.copy()
            for j in range(self.nk): off[2 * j:2 * j + 2, 2 * j:2 * j + 2] = 0
            gens[nm] = blk; self.offblock = max(getattr(self, 'offblock', 0.0), np.abs(off).max())
        self.gk = gens; self.PhS = PhS

    def hk(self, wx, wt):
        """2x2 blocks h_k(w) of H at the uniform toron field with Wilson lines (wx, wt); wx, wt arrays (...)."""
        ex = np.exp(1j * np.asarray(wx) / self.Lx)[..., None, None, None]; et = np.exp(1j * np.asarray(wt) / self.Lt)[..., None, None, None]
        D = 2.0 * np.eye(2) + ex * self.gk['fx'] + np.conj(ex) * self.gk['bx'] + et * self.gk['ft'] + np.conj(et) * self.gk['bt']
        return s3 @ (D - M0 * np.eye(2))

    # ---------------- Poincare paths on the torus ----------------
    def _path_current(self, z, c):
        """symmetric unit current z -> c: average over (t-first, x-first) and over both arcs in x and in t at antipodes."""
        Lx, Lt = self.Lx, self.Lt
        xz, tz = z % Lx, z // Lx; xc, tc = c % Lx, c // Lx
        dx = (xc - xz) % Lx; dt = (tc - tz) % Lt
        ax = [0] if dx == 0 else ([+1] if 2 * dx < Lx else ([-1] if 2 * dx > Lx else [+1, -1]))
        at = [0] if dt == 0 else ([+1] if 2 * dt < Lt else ([-1] if 2 * dt > Lt else [+1, -1]))
        cur = np.zeros(self.nl)
        def xmove(t, x0, d, cur, w):
            n = dx if d > 0 else Lx - dx; x = x0
            for _ in range(n if d != 0 else 0):
                if d > 0: cur[self.key[('x', x, t)]] += w; x = (x + 1) % Lx
                else: x = (x - 1) % Lx; cur[self.key[('x', x, t)]] -= w
        def tmove(x, t0, d, cur, w):
            n = dt if d > 0 else Lt - dt; t = t0
            for _ in range(n if d != 0 else 0):
                if d > 0: cur[self.key[('t', x, t)]] += w; t = (t + 1) % Lt
                else: t = (t - 1) % Lt; cur[self.key[('t', x, t)]] -= w
        orders = [0] if (dx == 0 or dt == 0) else [0, 1]
        w = 1.0 / (len(ax) * len(at) * len(orders))
        for a in ax:
            for b in at:
                for o in orders:
                    if o == 0:   # t first, then x
                        tmove(xz, tz, b, cur, w); xmove(tc, xz, a, cur, w)
                    else:
                        xmove(tz, xz, a, cur, w); tmove(xc, tz, b, cur, w)
        return cur

    def _paths(self):
        ns = self.ns; Pi = np.zeros((ns, self.nl, ns))
        for c in range(ns):
            for z in range(ns):
                if z != c: Pi[c, :, z] = self._path_current(z, c)
        self.Pi = Pi
        self.PK = np.zeros((self.np_, self.nl, ns)); self.corners = np.zeros((self.np_, ns))
        for ip, (x, t) in enumerate(self.plaq):
            cs = [self.site(x, t), self.site(x + 1, t), self.site(x + 1, t + 1), self.site(x, t + 1)]
            for c in cs: self.PK[ip] += 0.25 * Pi[c]; self.corners[ip, c] += 0.25
        # torus distances
        dxs = np.minimum(np.abs(self.site_x[:, None] - self.site_x[None]), self.Lx - np.abs(self.site_x[:, None] - self.site_x[None]))
        dts = np.minimum(np.abs(self.site_t[:, None] - self.site_t[None]), self.Lt - np.abs(self.site_t[:, None] - self.site_t[None]))
        self.dist = dxs + dts

    def lapinv_current(self, f):
        """global right inverse of the outflow divergence on the torus: k = grad-type minimum-norm solution (logged diagnostic)."""
        if not hasattr(self, 'Dv'):
            Dv = np.zeros((self.ns, self.nl))
            for i in range(self.nl): Dv[self.frm[i], i] += 1; Dv[self.to[i], i] -= 1
            self.Dv = Dv; self.Dvp = np.linalg.pinv(Dv)
        return f @ self.Dvp.T


# ---------------- toron torus (momentum space) ----------------
class Toron:
    """Weyl lines per momentum over the toron torus for one model; parallel transport and holonomies."""
    def __init__(self, S, model):
        self.S = S; self.model = MODELS[model]
        self.flav = [(e, c, m) for (e, c, m) in self.model]

    def spinor(self, e, c, wx, wt):
        """unit spinor u_k of the L (positive) / R (negative) eigenspace of h_k(e w): shape (..., nk, 2)."""
        h = self.S.hk(e * np.asarray(wx), e * np.asarray(wt)); h = 0.5 * (h + np.conj(np.swapaxes(h, -1, -2)))
        w, V = np.linalg.eigh(h)
        assert np.all(w[..., 0] < 0) and np.all(w[..., 1] > 0)
        return V[..., :, 1] if c == 'L' else V[..., :, 0], np.abs(w).min()

    def transport(self, e, c, path):
        """path: (P, n+1, 2) w-points; returns transported spinors at the end (P, nk, 2), starting from the fixed gauge at path[:,0]."""
        u, g = self.spinor(e, c, path[..., 0], path[..., 1])        # (P, n+1, nk, 2)
        ov = np.einsum('pjka,pjka->pjk', np.conj(u[:, :-1]), u[:, 1:])   # <u_j | u_{j+1}>
        ph = np.cumprod(np.conj(ov / np.abs(ov)), axis=1)               # gauge factor making successive overlaps real positive
        return u[:, -1] * ph[:, -1][..., None], u[:, 0], g

    def perm(self, which):
        """label of the physical momentum k + 2pi/L_mu (the label k carries at w_mu = 2pi)."""
        S = self.S; Lx, Lt = S.Lx, S.Lt; p = np.zeros(S.nk, int)
        for j in range(S.nk):
            it, ix = j // Lx, j % Lx
            p[j] = ((it + 1) % Lt) * Lx + ix if which == 't' else it * Lx + (ix + 1) % Lx
        return p

    def berry_phase_loop(self, e, c, wx, nloop=256, which='t'):
        """log-phase (per momentum label) of the factor z_k by which the parallel-transported Weyl line of label k, carried once
        around the cycle (w_t: 0 -> 2pi at fixed w_x = wx if which='t'; w_x-cycle at fixed w_t = wx if which='x'), returns onto the
        start line of label perm(k) (same field up to the winding gauge transformation that relabels momenta)."""
        s = 2 * np.pi * np.arange(nloop + 1) / nloop; wx = np.atleast_1d(np.asarray(wx, float)); out = []
        pm = np.arange(self.S.nk)
        for _ in range(e): pm = self.perm(which)[pm]          # charge e: w -> w + 2pi shifts the momentum e steps
        for c0 in range(0, len(wx), 4):
            ww = wx[c0:c0 + 4]
            if which == 't': WX = np.repeat(ww[:, None], nloop + 1, 1); WT = np.repeat(s[None], len(ww), 0)
            else: WT = np.repeat(ww[:, None], nloop + 1, 1); WX = np.repeat(s[None], len(ww), 0)
            u, _ = self.spinor(e, c, WX, WT)
            ov = np.einsum('pjka,pjka->pjk', np.conj(u[:, :-1]), u[:, 1:])
            ut = u[:, -1] * np.prod(np.conj(ov / np.abs(ov)), axis=1)[..., None]       # transported end spinors (P, nk, 2)
            z = np.einsum('pka,pka->pk', np.conj(u[:, 0][:, pm]), ut)
            out.append(np.angle(z))
        return np.concatenate(out, 0)

    def holonomy(self, wx, nloop=256, which='t'):
        """multiplet log-phase h: the transported multiplet det(v[rows]) is multiplied by exp(i h) around the cycle."""
        tot = 0.0
        for (e, c, m) in self.flav:
            tot = tot + m * self.berry_phase_loop(e, c, wx, nloop, which).sum(-1)
        return tot


class TorusMeasure:
    def __init__(self, S, model, Ns=8, sk=-1, ntor=96, nloop=256, ngam=512):
        self.S, self.modelname, self.model = S, model, MODELS[model]
        self.Ns, self.sk, self.ntor, self.nloop = Ns, sk, ntor, nloop
        self.charges = sorted(set(e for (e, _, _) in self.model))
        self.coef = {e: sum(m * e * (1 if c == 'L' else -1) for (ee, c, m) in self.model if ee == e) for e in self.charges}
        self.rows = {'L': np.where(S.g5 > 0)[0], 'R': np.where(S.g5 < 0)[0]}
        self.tor = Toron(S, model)
        # Gamma_t(wx): lifted multiplet holonomy phase around the wt-cycle, on a fine grid over [0, 2pi] (+ winding)
        self.ggrid = 2 * np.pi * np.arange(ngam + 1) / ngam
        gam = np.unwrap(Richardson_loop(self.tor, self.ggrid, nloop))
        self.gam = gam; self.wind = (gam[-1] - gam[0]) / (2 * np.pi)
        self.hx0 = Richardson_loop(self.tor, np.array([0.0]), nloop, which='x')[0]

    def Gam_t(self, wx):
        if getattr(self, 'spline', None) is not None:
            wx = np.asarray(wx, float); return self.spline(np.mod(wx, 2 * np.pi)) + self.wind * wx
        return self.Gam_t_exact(wx)

    def use_spline(self):
        from scipy.interpolate import CubicSpline
        y = self.gam - self.wind * self.ggrid; y[-1] = y[0]
        self.spline = CubicSpline(self.ggrid, y, bc_type='periodic')

    def Gam_t_exact(self, wx):
        """continuous lift of the wt-cycle holonomy phase at wx (any real wx), anchored on the fine grid."""
        wx = np.asarray(wx, float); n = len(self.ggrid) - 1; twopi = 2 * np.pi
        cyc = np.floor(wx / twopi); r = wx - cyc * twopi
        i = np.clip(np.floor(r / twopi * n).astype(int), 0, n - 1)
        val = Richardson_loop(self.tor, r, self.nloop)
        base = self.gam[i]
        val = base + np.angle(np.exp(1j * (val - base)))
        return val + cyc * twopi * self.wind

    def toron_basis(self, w, n=None, n1=None):
        """position-space start bases at U[w] for each flavour (P, N, nk), transported 0 -> (wx,0) -> (wx,wt); returns dict and
        the log det contribution is computed later from the full transported basis.  Richardson n vs n/2 on the spinor phases."""
        S = self.S; n = n or self.ntor; n1 = n1 or getattr(self, 'ntor1', None) or n; P = len(w); out = {}; out2 = {}
        for (e, c, m) in self.model:
            res = []
            for (nn, mm) in ((n, n1), (n // 2, n1 // 2)):
                s = np.linspace(0, 1, nn + 1); s1 = np.linspace(0, 1, mm + 1)
                leg1 = np.stack([s1[None] * w[:, 0:1], 0 * s1[None] + 0 * w[:, 0:1]], -1)
                leg2 = np.stack([0 * s[None] + w[:, 0:1], s[None] * w[:, 1:2]], -1)
                path = np.concatenate([leg1, leg2[:, 1:]], 1)
                uend, u0, g = self.tor.transport(e, c, path)
                res.append((uend, u0))
            (ua, u0), (ub, _) = res
            # Richardson on the accumulated phase relative to the endpoint eigenvector
            uE, _ = self.tor.spinor(e, c, w[:, 0], w[:, 1])
            pa = np.angle(np.einsum('pka,pka->pk', np.conj(uE), ua)); pb = np.angle(np.einsum('pka,pka->pk', np.conj(uE), ub))
            pb = pa + np.angle(np.exp(1j * (pb - pa)))
            ph = (4 * pa - pb) / 3
            u = uE * np.exp(1j * ph)[..., None]
            V = np.einsum('sj,pja->psaj', S.Ph, u).reshape(P, S.N, S.nk)   # (P, N, nk), column j = Ph_j (x) u_j
            out[(e, c)] = V; out2[(e, c)] = np.abs(pa - pb).max()
        return out, out2

    def logrho(self, th, Ns=None, need_k=True, parts=False, w_override=None, dAT=None):
        """th (P, nl) link angles (any gauge). Canonical decomposition, then the three pieces."""
        S = self.S; Ns = Ns or self.Ns
        F, Q, AT, w = S.decompose(th)
        assert np.all(Q == 0), 'nonzero topological sector'
        if w_override is not None: w = w_override
        if dAT is not None: AT = AT + dAT                        # un-fixed (non-canonical) transverse endpoint, Ward test only
        V0, rich = self.toron_basis(w)
        r = self.ray(AT, w, V0, Ns, need_k)
        Wa, Wb = r['W0half'], r['W0']; Wa = Wa + 2j * np.pi * np.round((Wb - Wa).imag / (2 * np.pi))
        W0 = (4 * Wb - Wa) / 3
        Sph = -1j * w[:, 1] * (self.Gam_t(w[:, 0]) - self.gam[0]) / (2 * np.pi)
        W = W0 + Sph + (1j * self.sk * np.sum(AT * r['kbb'], 1) if need_k else 0.0)
        if parts: return W, dict(r, Sph=Sph, W0=W0, AT=AT, w=w, F=F, rich=rich)
        return W

    def ray(self, AT, w, V0, Ns, need_k=True):
        S = self.S; P = AT.shape[0]; n = S.N // 2; ts = np.arange(Ns + 1) / Ns
        Aw = w[:, 0:1] * S.Ux[None] + w[:, 1:2] * S.Ut[None]
        V = {k: v.copy() for k, v in V0.items()}; V2 = {k: v.copy() for k, v in V0.items()}
        sw = np.ones(Ns + 1); sw[1:-1:2] = 4; sw[2:-1:2] = 2; sw *= 1.0 / (3 * Ns)
        Abar = np.zeros((P, S.ns)); kap = np.zeros((P, S.np_, S.nl)); gmin = np.inf; idx_ok = True; idchk = 0.0; mmax = 0.0
        F = AT @ S.Pm.T; F = (F + np.pi) % (2 * np.pi) - np.pi
        for j, t in enumerate(ts):
            Rtot = np.zeros((P, S.ns, S.nl)); qtot = np.zeros((P, S.ns))
            for e in self.charges:
                th = e * (Aw + t * AT)
                wv, Vv = np.linalg.eigh(S.H(th))
                gmin = min(gmin, np.abs(wv).min()); idx_ok &= bool(np.all((wv > 0).sum(1) == n))
                qtot += self.coef[e] * q_of(S, wv, Vv)
                if need_k: Rtot += self.coef[e] * e * dq_dA(S, th, wv, Vv)
                for (ee, c, m) in self.model:
                    if ee != e: continue
                    Qs = Vv[:, :, n:] if c == 'L' else Vv[:, :, :n]
                    if j == 0:
                        # start basis must span this subspace (toron field): check
                        res = np.abs(V[(e, c)] - Qs @ (np.conj(np.swapaxes(Qs, 1, 2)) @ V[(e, c)])).max()
                        assert res < 1e-8, f'start basis not in subspace {res}'
                        continue
                    u_, s_, vh = np.linalg.svd(np.conj(np.swapaxes(Qs, 1, 2)) @ V[(e, c)]); V[(e, c)] = Qs @ (u_ @ vh)
                    if j % 2 == 0:
                        u_, s_, vh = np.linalg.svd(np.conj(np.swapaxes(Qs, 1, 2)) @ V2[(e, c)]); V2[(e, c)] = Qs @ (u_ @ vh)
            Abar += sw[j] * qtot
            if need_k:
                g = np.einsum('pxl,lq->pqx', Rtot, S.aP)                   # (P, np, ns) plaquette derivative at fixed toron
                lhs = np.einsum('pxl,pl->px', Rtot, AT); rhs = np.einsum('pq,pqx->px', F, g)
                idchk = max(idchk, np.abs(lhs - rhs).max())
                m = g.sum(-1); mmax = max(mmax, np.abs(m).max())
                src = g - m[:, :, None] * S.corners[None]
                kp = np.einsum('qls,pqs->pql', S.PK, src)
                kap += sw[j] * (1 - t) * kp
        out = {}
        for nm, VV in (('W0', V), ('W0half', V2)):
            W0 = np.zeros(P, complex)
            for (e, c, m) in self.model:
                sg, ld = np.linalg.slogdet(VV[(e, c)][:, self.rows[c], :]); W0 += m * (ld + np.log(sg.astype(complex)))
            out[nm] = W0
        out.update(Abar=Abar, gmin=gmin, idx_ok=idx_ok, idchk=idchk, mono=mmax, sumA=np.abs(Abar.sum(1)).max(), V=V)
        if need_k:
            kloc = np.einsum('pq,pql->pl', F, kap)
            resid = Abar - S.div(kloc)
            corr = S.lapinv_current(resid)
            out.update(kbb=kloc + corr, kloc=kloc, kQ=corr, resid=np.abs(resid).max())
        else:
            out.update(kbb=np.zeros_like(AT))
        return out


def Richardson_loop(tor, wx, nloop, which='t'):
    """multiplet holonomy log-phase around a cycle, Richardson nloop vs nloop/2 (O(1/n^2) discretisation)."""
    a = tor.holonomy(wx, nloop, which); b = tor.holonomy(wx, nloop // 2, which)
    b = a + np.angle(np.exp(1j * (b - a)))
    return (4 * a - b) / 3


def vec_logdet(S, A, m=0.0, e=1):
    """vector-like Neuberger overlap logdet, K2 convention (1 - m/2) D_ov + m; returns logdet and min gap."""
    N = S.N; Id = np.eye(N); w, V = np.linalg.eigh(S.H(e * A))
    Sg = (V * np.sign(w)[:, None, :]) @ np.conj(np.swapaxes(V, 1, 2))
    Dm = (1 - m / 2) * (Id[None] + S.g5[None, :, None] * Sg) + m * Id[None]
    sg, ld = np.linalg.slogdet(Dm); return ld + np.log(sg.astype(complex)), np.abs(w).min(1)


def wilson_logdet(S, A, m=0.05):
    Dm = S.D(A) + m * np.eye(S.N)[None]; sg, ld = np.linalg.slogdet(Dm); return ld + np.log(sg.astype(complex))


def kbb_only(M, th, Ns=8):
    """the ray-averaged cohomology current kbb (P, nl) of TorusMeasure M at fields th (canonical decomposition), no transport."""
    S = M.S; F, Q, AT, w = S.decompose(th); P = th.shape[0]; ts = np.arange(Ns + 1) / Ns
    Aw = w[:, 0:1] * S.Ux[None] + w[:, 1:2] * S.Ut[None]
    sw = np.ones(Ns + 1); sw[1:-1:2] = 4; sw[2:-1:2] = 2; sw *= 1.0 / (3 * Ns)
    kap = np.zeros((P, S.np_, S.nl)); gm = []
    for j, t in enumerate(ts):
        Rtot = np.zeros((P, S.ns, S.nl))
        for e in M.charges:
            thh = e * (Aw + t * AT); wv, Vv = np.linalg.eigh(S.H(thh))
            Rtot += M.coef[e] * e * dq_dA(S, thh, wv, Vv)
        g = np.einsum('pxl,lq->pqx', Rtot, S.aP); m = g.sum(-1)
        src = g - m[:, :, None] * S.corners[None]
        kap += sw[j] * (1 - t) * np.einsum('qls,pqs->pql', S.PK, src)
        if j == Ns // 2: gm = g
    return np.einsum('pq,pql->pl', F, kap), gm
