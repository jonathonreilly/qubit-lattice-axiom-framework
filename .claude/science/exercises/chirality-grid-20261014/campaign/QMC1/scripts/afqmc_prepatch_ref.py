"""QMC-1 engine: sign-free auxiliary-field QMC for the X2 lambda1 = 0 Hamiltonian in the Kramers d-frame.

Model (PREREG section 1):  H = sum_k psi^dag (sum_a sigma_a sin k_a) psi + W sum_x Q_x,
Q_x = sum_e c_e O_e(x)^2,  O_e(x) = d_S(x)^dag O_e d_S(x),  d_S(x) = sum_t w_t d(x + r_t)   (filter taps, real, symmetric).

Discretisation.  Z = Tr prod_l [ prod_x prod_e e^{-dtau W c_e O_e(x)^2} ] e^{-dtau H_W}.  Every square is decoupled
EXACTLY by its own Gaussian field: e^{-dtau W c O^2} = E_phi exp(a phi O), a = sqrt(2 dtau W |c|) (x i if c > 0).
The only systematic error is therefore the Trotter splitting between non-commuting factors; the factor order is
reversed on alternate slices.  Each channel squares to s_e^2 * 1 (checked), so exp(z O_e) = cosh(z s) + sinh(z s)/s O_e.

Vertex factor.  With F_x the D x (N D) filter map (F_x F_x^T = rho 1),
  prod_e exp(F_x^T a_e phi_e O_e F_x) = 1 + F_x^T [(core - 1)/rho] F_x,   core = prod_e exp(rho a_e phi_e O_e)  (D x D).
So a vertex is a rank-D modification; Green's-function wraps through it cost O(taps * D * N_d) and an update is a
rank-D Sherman-Morrison-Woodbury step (D x D determinant for the ratio).

Weight.  w = e^{-sum phi^2/2} det(1 + B_{L_tau} ... B_1) (d-frame; all one-body matrices traceless so the referee's
1/sqrt(det M_d) is a constant).  Kramers (T2 = (i sigma_y x 1) K, T^2 = -1) makes det(1 + M) >= 0; every ratio's phase
is monitored (gate ii).

Updates: per-vertex preconditioned Crank-Nicolson moves of all fields at the vertex (prior-reversible).
Stabilisation: pivoted-QR UDV stacks every n_s slices; upward sweeps, the left stack is rebuilt after each sweep.
"""
import time
import numpy as np
from scipy.linalg import qr as sp_qr, lu_factor, lu_solve

from x2model import FlavourModel, SX, SY, SZ


# ============================================================================================== lattice and filter
class Lattice:
    def __init__(self, dims, filt):
        self.dims = tuple(dims)
        self.d = len(dims)
        self.N = int(np.prod(dims))
        self.coords = np.array(list(np.ndindex(*self.dims)))
        if filt == "one":
            taps = [((0,) * self.d, 1.0)]
        elif filt == "f1":                      # 1D: (1 + cos p)/2
            assert self.d == 1
            taps = [((0,), 0.5), ((1,), 0.25), ((-1,), 0.25)]
        elif filt == "f2":                      # 2D: (1 + cos px cos py)/2
            assert self.d == 2
            taps = [((0, 0), 0.5)] + [((sx, sy), 0.125) for sx in (1, -1) for sy in (1, -1)]
        else:
            raise ValueError(filt)
        self.filt = filt
        self.taps = taps
        # merged taps per site (offsets that coincide on small tori are added)
        self.nbr, self.wts = [], []
        for x in range(self.N):
            acc = {}
            for off, w in taps:
                y = self.site(self.coords[x] + np.array(off))
                acc[y] = acc.get(y, 0.0) + w
            ys = sorted(acc)
            self.nbr.append(np.array(ys)); self.wts.append(np.array([acc[y] for y in ys]))
        self.rho = float(np.sum(self.wts[0] ** 2))
        for x in range(self.N):
            assert abs(np.sum(self.wts[x] ** 2) - self.rho) < 1e-14
        ks = np.array(list(np.ndindex(*self.dims))) * (2 * np.pi / np.array(self.dims))
        self.kvecs = ks                                            # in np.fft order
        self.fk = np.array([self.filter_symbol(k) for k in ks])
        # dense spatial filter matrix Fs[x, y] = weight of y in d_S(x)
        self.Fs = np.zeros((self.N, self.N))
        for x in range(self.N):
            self.Fs[x, self.nbr[x]] = self.wts[x]

    def site(self, c):
        return int(np.ravel_multi_index(tuple(np.mod(c, self.dims)), self.dims))

    def filter_symbol(self, k):
        return sum(w * np.cos(np.dot(off, k)) for off, w in self.taps)

    def kindex(self, kvec):
        n = tuple(int(round(kv * L / (2 * np.pi))) % L for kv, L in zip(kvec, self.dims))
        return int(np.ravel_multi_index(n, self.dims))

    def corners(self):
        """(mirror momenta, light momenta) for the filtered geometries."""
        pi = np.pi
        if self.d == 1:
            return [(0.0,)], [(pi,)]
        return [(0.0, 0.0), (pi, pi)], [(pi, 0.0), (0.0, pi)]


# ============================================================================================== walker in the d-frame
def walker_symbol(fm, k):
    """d-frame one-body kinetic matrix at momentum k (D x D): s block sum_a sin k_a sigma_a, c block sigma_a^T."""
    sig = [SX, SY, SZ][:len(k)]
    hs = sum(np.sin(ka) * s for ka, s in zip(k, sig))
    hc = sum(np.sin(ka) * s.T for ka, s in zip(k, sig))
    Ps = np.diag(fm.Smask[:fm.nfl].astype(float))       # flavour projector on the s block
    Pc = np.eye(fm.nfl) - Ps
    return np.kron(hs, Ps) + np.kron(hc, Pc)            # index m = s * nfl + alpha


# ============================================================================================== the simulation
class AFQMC:
    def __init__(self, fm, kappa, lat, W, beta, dtau, n_s=4, seed=1, chans=None, step=0.3, n_hit=1):
        self.fm, self.lat, self.W, self.beta = fm, lat, W, beta
        self.Lt = int(round(beta / dtau))
        assert abs(self.Lt * dtau - beta) < 1e-9
        self.dtau = dtau
        assert self.Lt % n_s == 0
        self.n_s, self.nst = n_s, self.Lt // n_s
        self.D, self.N = fm.D, lat.N
        self.Nd = self.D * self.N
        self.rng = np.random.default_rng(seed)
        self.step, self.n_hit = step, n_hit
        # HS channels
        self.chans = fm.hs_channels(kappa) if chans is None else chans
        self.nch = len(self.chans)
        self.c = np.array([c for c, _ in self.chans])
        self.O = np.array([O for _, O in self.chans])                        # (nch, D, D)
        s2 = np.array([np.trace(O @ O).real / self.D for O in self.O])
        for O, s in zip(self.O, s2):
            assert np.abs(O @ O - s * np.eye(self.D)).max() < 1e-12, "channel does not square to a multiple of 1"
        self.s = np.sqrt(s2)
        self.a = np.sqrt(2 * dtau * W * np.abs(self.c)) * np.where(self.c < 0, 1.0, 1j)   # HS couplings
        # kinetic symbols for left multiplication by e^{-+dtau K} and for right multiplication (transposed, k -> -k)
        Kk = np.array([walker_symbol(fm, k) for k in lat.kvecs])                         # (N, D, D)
        self.Kk = Kk
        ev, V = np.linalg.eigh(Kk)
        self.Ufw = np.einsum("kij,kj,klj->kil", V, np.exp(-dtau * ev), V.conj())         # e^{-dtau K(k)}
        self.Ubw = np.einsum("kij,kj,klj->kil", V, np.exp(+dtau * ev), V.conj())
        minus = np.array([lat.kindex(-k) for k in lat.kvecs])
        self.Ufw_R = np.transpose(self.Ufw[minus], (0, 2, 1))                            # for X @ e^{-dtau K}
        self.Ubw_R = np.transpose(self.Ubw[minus], (0, 2, 1))
        # fields and vertex cores
        self.phi = self.rng.normal(size=(self.Lt, self.N, self.nch))
        self.core = np.zeros((self.Lt, self.N, self.D, self.D), complex)
        self.icore = np.zeros_like(self.core)
        for l in range(self.Lt):
            for x in range(self.N):
                self.core[l, x], self.icore[l, x] = self.vertex_core(l, self.phi[l, x])
        self.maxphase = 0.0                 # max |arg ratio| over all proposals (gate ii)
        self.nprop = self.nacc = 0
        self.maxdev = 0.0                   # max |G_wrapped - G_fresh| at stabilisation points
        self.light_dev = 0.0                # max per-configuration deviation of the light-corner G from 1/2 (gate iv)

    # ------------------------------------------------------------------------------------------ vertex algebra
    def channel_exps(self, phi, sign=+1):
        """exp(sign * rho a_e phi_e O_e) for all channels, (nch, D, D)."""
        z = sign * self.lat.rho * self.a * phi * self.s
        ch, sh = np.cosh(z), np.sinh(z) / self.s
        return ch[:, None, None] * np.eye(self.D)[None] + sh[:, None, None] * self.O

    def vertex_core(self, l, phi):
        """core = ordered product of the channel exponentials; order reversed on odd slices. Returns (core, core^-1)."""
        Xp = self.channel_exps(phi, +1)
        Xm = self.channel_exps(phi, -1)
        order = range(self.nch) if l % 2 == 0 else range(self.nch - 1, -1, -1)
        core = np.eye(self.D, dtype=complex); icore = np.eye(self.D, dtype=complex)
        for e in order:                      # core = X_{e_last} ... X_{e_first} acting on the left
            core = Xp[e] @ core
            icore = icore @ Xm[e]
        return core, icore

    # ------------------------------------------------------------------------------------------ one-body application
    def kin_left(self, X, U):
        """U(k)-symbol translation-invariant operator applied from the left to X (Nd x m)."""
        m = X.shape[1]
        Xr = X.reshape(self.lat.dims + (self.D, m))
        ax = tuple(range(self.lat.d))
        Xk = np.fft.fftn(Xr, axes=ax).reshape(self.N, self.D, m)
        Xk = np.einsum("kij,kjm->kim", U, Xk)
        return np.fft.ifftn(Xk.reshape(self.lat.dims + (self.D, m)), axes=ax).reshape(self.Nd, m)

    def kin_right(self, X, U_R):
        return np.ascontiguousarray(self.kin_left(np.ascontiguousarray(X.T), U_R).T)

    def vert_left(self, X, x, M):
        """(1 + F_x^T M F_x) X, in place on X (Nd x m, C-contiguous)."""
        assert X.flags.c_contiguous
        X3 = X.reshape(self.N, self.D, -1)
        ys, ws = self.lat.nbr[x], self.lat.wts[x]
        FX = np.tensordot(ws, X3[ys], axes=(0, 0))          # D x m
        Y = M @ FX
        for y, w in zip(ys, ws):
            X3[y] += w * Y
        return X

    def vert_right(self, X, x, M):
        """X (1 + F_x^T M F_x), in place (C-contiguous X)."""
        assert X.flags.c_contiguous
        X3 = X.reshape(-1, self.N, self.D)
        ys, ws = self.lat.nbr[x], self.lat.wts[x]
        XF = np.tensordot(X3[:, ys, :], ws, axes=(1, 0))     # m x D
        Z = XF @ M
        for y, w in zip(ys, ws):
            X3[:, y, :] += w * Z
        return X

    def apply_B(self, l, X):
        """X <- B_l X,  B_l = E_{l,N-1} ... E_{l,0} e^{-dtau K}."""
        X = self.kin_left(X, self.Ufw)
        rho = self.lat.rho
        for x in range(self.N):
            self.vert_left(X, x, (self.core[l, x] - np.eye(self.D)) / rho)
        return X

    def apply_Bdag(self, l, X):
        """X <- B_l^dag X = e^{-dtau K} E_{l,0}^dag ... E_{l,N-1}^dag X."""
        rho = self.lat.rho
        for x in range(self.N - 1, -1, -1):
            self.vert_left(X, x, (self.core[l, x].conj().T - np.eye(self.D)) / rho)
        return self.kin_left(X, self.Ufw)          # K Hermitian

    # ------------------------------------------------------------------------------------------ UDV stacks
    @staticmethod
    def udv_step(Y, V):
        """Y = (B U) * D  ->  new (U, D, V) with V_new = R~ P^T V."""
        Q, R, piv = sp_qr(Y, pivoting=True, mode="economic", check_finite=False)
        r = np.diag(R).copy()
        dabs = np.abs(r)
        Rt = R / r[:, None]
        Pt = np.zeros((len(piv), len(piv))); Pt[piv, np.arange(len(piv))] = 1.0
        return Q * (r / dabs)[None, :], dabs, (Rt @ Pt.T) @ V

    def identity_udv(self):
        I = np.eye(self.Nd, dtype=complex)
        return I.copy(), np.ones(self.Nd), I.copy()

    def build_left_stack(self):
        self.Lst = [None] * (self.nst + 1)
        self.Lst[self.nst] = self.identity_udv()
        for n in range(self.nst - 1, -1, -1):
            U, D, V = self.Lst[n + 1]
            Y = U.copy()
            for l in range((n + 1) * self.n_s - 1, n * self.n_s - 1, -1):
                Y = self.apply_Bdag(l, Y)
            self.Lst[n] = self.udv_step(Y * D[None, :], V)

    def green(self, R, L, timed=False):
        """equal-time G(tau) = (1 + B(tau,0) B(beta,tau))^{-1} and, if timed, G(tau,0) = B(tau,0) G(0)."""
        UR, DR, VR = R
        UL, DL, VL = L
        DRb, DRs = np.maximum(DR, 1.0), np.minimum(DR, 1.0)
        DLb, DLs = np.maximum(DL, 1.0), np.minimum(DL, 1.0)
        Mid = (UR.conj().T @ UL) / DRb[:, None] / DLb[None, :] + (DRs[:, None] * (VR @ VL.conj().T)) * DLs[None, :]
        lu = lu_factor(Mid, check_finite=False)
        G = (UL / DLb[None, :]) @ lu_solve(lu, (UR.conj().T) / DRb[:, None], check_finite=False)
        if not timed:
            return G, None
        Gt = (UL / DLb[None, :]) @ lu_solve(lu, DRs[:, None] * VR, check_finite=False)
        return G, Gt

    # ------------------------------------------------------------------------------------------ local updates
    def update_vertex(self, l, x, G):
        lat, D, rho = self.lat, self.D, self.lat.rho
        ys, ws = lat.nbr[x], lat.wts[x]
        G4 = G.reshape(self.N, D, self.N, D)
        Gs = np.einsum("t,u,tiuj->ij", ws, ws, G4[np.ix_(ys, np.arange(D), ys, np.arange(D))])
        g0 = rho * np.eye(D) - Gs
        g = g0.copy()
        core0, icore0 = self.core[l, x], self.icore[l, x]
        core, icore, phi = core0, icore0, self.phi[l, x]
        cstep = np.sqrt(1 - self.step ** 2)
        accepted = False
        for _ in range(self.n_hit):
            phin = cstep * phi + self.step * self.rng.normal(size=self.nch)
            corn, icorn = self.vertex_core(l, phin)
            delta = (corn @ icore - np.eye(D)) / rho
            M1 = np.eye(D) + delta @ g
            r = np.linalg.det(M1)
            self.nprop += 1
            if r != 0:
                self.maxphase = max(self.maxphase, abs(np.angle(r)))
            if self.rng.random() < r.real:
                self.nacc += 1
                accepted = True
                # local update of g (vertex block of 1 - G in smeared basis)
                g = g + (rho * np.eye(D) - g) @ delta @ np.linalg.solve(np.eye(D) + g @ delta, g)
                core, icore, phi = corn, icorn, phin
        if accepted:
            dtot = (core @ icore0 - np.eye(D)) / rho
            GFt = np.tensordot(G4[:, :, ys, :], ws, axes=(2, 0)).reshape(self.Nd, D)         # G F^T
            FG = np.tensordot(ws, G4[ys], axes=(0, 0)).reshape(D, self.Nd)                    # F G
            F1G = -FG
            F1G4 = F1G.reshape(D, self.N, D)
            for y, w in zip(ys, ws):
                F1G4[:, y, :] += w * np.eye(D)                                                  # F (1 - G)
            Kmat = dtot @ np.linalg.inv(np.eye(D) + g0 @ dtot)
            G -= GFt @ (Kmat @ F1G)
            self.core[l, x], self.icore[l, x], self.phi[l, x] = core, icore, phi
        return G

    # ------------------------------------------------------------------------------------------ sweep
    def sweep(self, measure=None, update=True):
        """One upward sweep. measure(n, G, Gt, sim) is called at every stabilisation point tau_n (n = 1..nst),
        and at n = 0 with G(0) (Gt = G(0,0) = G(0))."""
        if not hasattr(self, "Lst"):
            self.build_left_stack()
        R = self.identity_udv()
        G, _ = self.green(R, self.Lst[0])
        if measure is not None:
            measure(0, G, G, self)
        D, rho = self.D, self.lat.rho
        for n in range(self.nst):
            for l in range(n * self.n_s, (n + 1) * self.n_s):
                G = self.kin_left(G, self.Ufw)
                G = self.kin_right(G, self.Ubw_R)
                for x in range(self.N):
                    self.vert_left(G, x, (self.core[l, x] - np.eye(D)) / rho)
                    self.vert_right(G, x, (self.icore[l, x] - np.eye(D)) / rho)
                    if update and self.W != 0:
                        G = self.update_vertex(l, x, G)
            U, Dd, V = R
            Y = U.copy()
            for l in range(n * self.n_s, (n + 1) * self.n_s):
                Y = self.apply_B(l, Y)
            R = self.udv_step(Y * Dd[None, :], V)
            Gf, Gt = self.green(R, self.Lst[n + 1], timed=True)
            self.maxdev = max(self.maxdev, np.abs(Gf - G).max())
            G = Gf
            if measure is not None:
                measure(n + 1, G, Gt, self)
        self.build_left_stack()
        return G

    # ------------------------------------------------------------------------------------------ full weight
    def log_weight(self):
        """log det(1 + B(beta, 0)) from the right stack; returns complex log (phase check, gate ii)."""
        R = self.identity_udv()
        for l in range(self.Lt):
            U, Dd, V = R
            R = self.udv_step(self.apply_B(l, U.copy()) * Dd[None, :], V)
        U, Dd, V = R
        Db, Ds = np.maximum(Dd, 1.0), np.minimum(Dd, 1.0)
        # 1 + U D V = U Db (Db^-1 U^dag V^-1 + Ds) V
        inner = (U.conj().T @ np.linalg.inv(V)) / Db[:, None] + np.diag(Ds)
        out = 0j
        for Z in (U, inner, V):
            s, ld = np.linalg.slogdet(Z)
            out += np.log(s) + ld
        return out + np.sum(np.log(Db))


# ============================================================================================== observables (Wick)
class Observables:
    """Equal-time Wick contractions for operators O = sum (R_sp x A) etc., in the d-frame.
    An operator is (Rsp, A, P, Qm): O = d^dag (Rsp x A) d + d^T (Rsp x P) d + d^dag (Rsp x Qm) d^dag^T."""

    def __init__(self, sim):
        self.sim = sim
        fm, lat = sim.fm, sim.lat
        self.vec = fm.vector_ops()                      # list over a of (re, im), each (A, P, Qm) local
        Fs = lat.Fs
        self.R0 = Fs.T @ Fs                              # sum_x F_x^T F_x  (Q = 0)
        if lat.d == 1:
            sgn = np.array([(-1.0) ** c[0] for c in lat.coords])
        else:
            sgn = np.array([(-1.0) ** (c[0] + c[1]) for c in lat.coords])
        self.Rpi = Fs.T @ (sgn[:, None] * Fs)           # Q = pi or (pi, pi)
        # plane waves for G(tau, k)
        mir, lig = lat.corners()
        self.kset = {"mirror": mir, "light": lig}
        self.ph = {}
        for nm, ks in self.kset.items():
            self.ph[nm] = [np.exp(1j * lat.coords @ np.array(k)) / np.sqrt(lat.N) for k in ks]

    # ---- kron helpers on G4 (N, D, N, D)
    @staticmethod
    def kl(Rsp, A, X4):
        t = np.tensordot(A, X4, axes=([1], [1]))           # (i, y, z, k)
        return np.tensordot(Rsp, t, axes=([1], [1]))       # (x, i, z, k)

    @staticmethod
    def kr(X4, Rsp, A):
        t = np.tensordot(X4, Rsp, axes=([2], [0]))         # (x, i, k, w)
        return np.transpose(np.tensordot(t, A, axes=([2], [0])), (0, 1, 2, 3))   # (x, i, w, l)

    def corr(self, op, G, Rsp):
        """< O O > for one Hermitian operator O = Rsp x (A, P, Qm) (global), given equal-time G."""
        A, P, Qm = op
        N, D = self.sim.N, self.sim.D
        G4 = G.reshape(N, D, N, D)
        C4 = (np.eye(self.sim.Nd) - G.T).reshape(N, D, N, D)
        out = 0j
        if np.abs(A).max() > 0:
            # <O> = sum A_full * C ; conn = sum C * (A G A)
            mean = np.einsum("xy,ij,xiyj->", Rsp, A, C4)
            AGA = self.kr(self.kl(Rsp, A, G4), Rsp, A)
            out += mean ** 2 + np.sum(C4 * AGA)
        if np.abs(P).max() > 0 and np.abs(Qm).max() > 0:
            PGQ = self.kr(self.kl(Rsp, P, G4), Rsp, Qm)
            QCP = self.kr(self.kl(Rsp, Qm, C4), Rsp, P)
            out += 2 * np.sum(PGQ * G4) + 2 * np.sum(QCP * C4)
        return out

    def structure(self, G, which="Q0"):
        """per component a: (1/N) <X_a X_a>, (1/N) <Y_a Y_a> at Q = 0 ('Q0') or Q = pi ('Qpi')."""
        Rsp = self.R0 if which == "Q0" else self.Rpi
        N = self.sim.N
        SX = np.array([self.corr(re, G, Rsp).real for re, im in self.vec]) / N
        SY = np.array([self.corr(im, G, Rsp).real for re, im in self.vec]) / N
        return SX, SY

    def local_terms(self, G):
        """<Q_x> summed over x, two ways: (a) from Bh^a directly, (b) from the HS channels (Fierz check)."""
        sim, lat = self.sim, self.sim.lat
        N, D, rho = sim.N, sim.D, lat.rho
        G4 = G.reshape(N, D, N, D)
        qa = qb = 0.0
        for x in range(N):
            ys, ws = lat.nbr[x], lat.wts[x]
            Gs = np.einsum("t,u,tiuj->ij", ws, ws, G4[np.ix_(ys, np.arange(D), ys, np.arange(D))])
            Cs = rho * np.eye(D) - Gs.T
            def loc(op):
                A, P, Qm = op
                v = np.sum(A * Cs) ** 2 + np.sum(Cs * (A @ Gs @ A))
                v += 2 * np.sum((P @ Gs @ Qm) * Gs) + 2 * np.sum((Qm @ Cs @ P) * Cs)
                return v
            for re, im in self.vec:
                qa += -0.5 * (loc(re) - loc(im))
            for c, O in sim.chans:
                qb += c * (np.sum(O * Cs) ** 2 + np.sum(Cs * (O @ Gs @ O)))
        return qa, qb

    def kinetic(self, G):
        """<H_W> = sum_k tr[K(k) C(k)] with C = <d^dag d> (d-frame; c-block constant tr h = 0)."""
        sim = self.sim
        N, D = sim.N, sim.D
        C = np.eye(sim.Nd) - G.T
        tot = 0j
        for ik, k in enumerate(sim.lat.kvecs):
            v = np.exp(1j * sim.lat.coords @ k) / np.sqrt(N)
            Ck = np.einsum("x,xiyj,y->ij", v, C.reshape(N, D, N, D), v.conj())   # <d_k,i^dag d_k,j>
            tot += np.sum(sim.Kk[ik] * Ck)
        return tot

    def gk(self, Gt, name):
        """mode-resolved D x D matrices v_k^dag G(tau,0) v_k for each corner k in the set (G(tau,0)_{k,k})."""
        N, D = self.sim.N, self.sim.D
        Gt4 = Gt.reshape(N, D, N, D)
        return [np.einsum("x,xiyj,y->ij", v.conj(), Gt4, v) for v in self.ph[name]]
