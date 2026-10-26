"""SU(3) Wilson gauge + Ns staggered fields (even-odd pseudofermion), HMC. Own code, numpy only."""
import numpy as np

class Lat:
    def __init__(self, dims):
        self.dims = tuple(dims)            # (Lt, Lx, Ly, Lz); direction 0 = time (APBC for fermions)
        self.V = int(np.prod(dims))
        idx = np.arange(self.V).reshape(self.dims)
        coords = np.stack(np.unravel_index(np.arange(self.V), self.dims), axis=1)  # (V,4)
        self.coords = coords
        self.fwd = np.empty((4, self.V), dtype=np.int64)
        self.bwd = np.empty((4, self.V), dtype=np.int64)
        for mu in range(4):
            self.fwd[mu] = np.roll(idx, -1, axis=mu).reshape(-1)   # site s+mu
            self.bwd[mu] = np.roll(idx, +1, axis=mu).reshape(-1)   # site s-mu
        # staggered phases eta_mu(x) = (-1)^{sum_{nu<mu} x_nu}
        self.eta = np.ones((4, self.V))
        for mu in range(4):
            self.eta[mu] = (-1.0) ** (coords[:, :mu].sum(axis=1))
        # APBC in direction 0: the forward hop from t=Lt-1 and the backward hop from t=0 carry -1
        self.sgnf = np.ones((4, self.V))
        self.sgnb = np.ones((4, self.V))
        self.sgnf[0, coords[:, 0] == dims[0] - 1] = -1.0
        self.sgnb[0, coords[:, 0] == 0] = -1.0
        self.ef = (self.eta * self.sgnf)[:, :, None]   # (4,V,1)
        self.eb = (self.eta * self.sgnb)[:, :, None]
        self.even = (coords.sum(axis=1) % 2 == 0)
        self.evenf = self.even.astype(float)[:, None]
        self.oddf = 1.0 - self.evenf


def dag(a):
    return np.conj(np.swapaxes(a, -1, -2))


def random_su3(rng, shape, eps=None):
    """Haar-ish random SU(3) (eps=None) or exp(i eps*H) near identity."""
    if eps is None:
        A = rng.normal(size=shape + (3, 3)) + 1j * rng.normal(size=shape + (3, 3))
        Q, R = np.linalg.qr(A)
        d = np.diagonal(R, axis1=-2, axis2=-1)
        Q = Q * (d / np.abs(d))[..., None, :]
        det = np.linalg.det(Q)
        Q = Q / (det ** (1.0 / 3.0))[..., None, None]
        return Q
    H = herm_traceless_gauss(rng, shape) * eps
    return expm_ih(H)


def herm_traceless_gauss(rng, shape):
    """P with density exp(-tr P^2 / 2) over traceless hermitian 3x3."""
    # basis lambda_a/2 ... use P = sum p_a T_a, tr(T_a T_b)=delta/2 -> weight exp(-sum p_a^2/2 *(1/2)*2)?? handle explicitly:
    # tr P^2 = sum_a p_a^2 /2 ; exp(-tr P^2/2) = exp(-sum p_a^2/4)  => p_a ~ N(0, 2)
    lam = _gellmann()
    p = rng.normal(size=shape + (8,)) * np.sqrt(2.0)
    return np.einsum('...a,aij->...ij', p, lam / 2.0)


_GM = None
def _gellmann():
    global _GM
    if _GM is None:
        l = np.zeros((8, 3, 3), dtype=complex)
        l[0][0, 1] = l[0][1, 0] = 1
        l[1][0, 1] = -1j; l[1][1, 0] = 1j
        l[2][0, 0] = 1; l[2][1, 1] = -1
        l[3][0, 2] = l[3][2, 0] = 1
        l[4][0, 2] = -1j; l[4][2, 0] = 1j
        l[5][1, 2] = l[5][2, 1] = 1
        l[6][1, 2] = -1j; l[6][2, 1] = 1j
        l[7][0, 0] = l[7][1, 1] = 1 / np.sqrt(3); l[7][2, 2] = -2 / np.sqrt(3)
        _GM = l
    return _GM


def expm_ih(H):
    """exp(i H) for hermitian traceless H (batched) via eigendecomposition."""
    w, v = np.linalg.eigh(H)
    return np.einsum('...ik,...k,...jk->...ij', v, np.exp(1j * w), np.conj(v))


def proj_su3(U):
    """re-unitarise (Gram-Schmidt + det fix)"""
    a = U[..., 0, :]
    a = a / np.linalg.norm(a, axis=-1, keepdims=True)
    b = U[..., 1, :] - np.sum(np.conj(a) * U[..., 1, :], axis=-1, keepdims=True) * a
    b = b / np.linalg.norm(b, axis=-1, keepdims=True)
    c = np.conj(np.cross(a, b))
    return np.stack([a, b, c], axis=-2)


class Gauge:
    def __init__(self, lat, beta):
        self.lat = lat
        self.beta = beta

    def staples(self, U):
        """V[mu,s] such that the sum of the 6 plaquettes containing link (mu,s) is Re tr(U[mu,s] V[mu,s])."""
        lat = self.lat
        V = np.zeros_like(U)
        for mu in range(4):
            for nu in range(4):
                if nu == mu:
                    continue
                # forward staple: U_nu(s+mu) U_mu^dag(s+nu) U_nu^dag(s)
                a = U[nu][lat.fwd[mu]]
                b = dag(U[mu][lat.fwd[nu]])
                c = dag(U[nu])
                V[mu] += a @ b @ c
                # backward staple: U_nu^dag(s+mu-nu) U_mu^dag(s-nu) U_nu(s-nu)
                sm = lat.bwd[nu]
                a = dag(U[nu][lat.fwd[mu][sm]])
                b = dag(U[mu][sm])
                c = U[nu][sm]
                V[mu] += a @ b @ c
        return V

    def action(self, U):
        V = self.staples(U)
        # sum over links of Re tr(U V) counts each plaquette 4 times (once per link)... each plaquette has 4 links,
        # and the 6 plaquettes/link counted: sum_links Re tr(U V) = 4 * sum_p Re tr U_p
        s = np.einsum('msij,msji->', U, V).real
        sum_p = s / 4.0
        return -(self.beta / 3.0) * sum_p

    def plaq(self, U):
        V = self.staples(U)
        s = np.einsum('msij,msji->', U, V).real / 4.0
        return s / (3.0 * 6 * self.lat.V)

    def force(self, U):
        V = self.staples(U)
        W = U @ V
        N = -(self.beta / 6.0) * 1j * (W - dag(W))
        return N


def traceless_herm(N):
    F = 0.5 * (N + dag(N))
    tr = np.trace(F, axis1=-2, axis2=-1)
    return F - (tr / 3.0)[..., None, None] * np.eye(3)


class Fermion:
    """one staggered field = det(m+D); pseudofermion on even sites with A = m^2 - D^2."""
    def __init__(self, lat, m, tol=1e-10):
        self.lat = lat
        self.m = m
        self.tol = tol
        self.cg_iters = 0

    def prep(self, U):
        lat = self.lat
        self.U = U
        self.Ub = dag(U[np.arange(4)[:, None], lat.bwd])   # U_mu^dag(s - mu)
        self.Ur = [[np.ascontiguousarray(U[:, :, i, j]) for j in range(3)] for i in range(3)]
        self.Ubr = [[np.ascontiguousarray(self.Ub[:, :, i, j]) for j in range(3)] for i in range(3)]
        self.ef0 = lat.ef[..., 0]
        self.eb0 = lat.eb[..., 0]

    def D(self, psi):
        lat = self.lat
        pf = psi[lat.fwd]          # (4,V,3)
        pb = psi[lat.bwd]
        out = np.empty((lat.V, 3), dtype=complex)
        Ur, Ubr = self.Ur, self.Ubr
        for i in range(3):
            t1 = Ur[i][0] * pf[..., 0] + Ur[i][1] * pf[..., 1] + Ur[i][2] * pf[..., 2]
            t2 = Ubr[i][0] * pb[..., 0] + Ubr[i][1] * pb[..., 1] + Ubr[i][2] * pb[..., 2]
            out[:, i] = 0.5 * np.sum(self.ef0 * t1 - self.eb0 * t2, axis=0)
        return out

    def A(self, x):
        return self.m ** 2 * x - self.D(self.D(x))

    def cg(self, b, x0=None, tol=None):
        tol = self.tol if tol is None else tol
        A = self.A
        x = np.zeros_like(b) if x0 is None else x0.copy()
        r = b - A(x) if x0 is not None else b.copy()
        p = r.copy()
        rr = np.vdot(r, r).real
        bb = np.vdot(b, b).real
        it = 0
        while rr > tol ** 2 * bb and it < 5000:
            Ap = A(p)
            alpha = rr / np.vdot(p, Ap).real
            x += alpha * p
            r -= alpha * Ap
            rr2 = np.vdot(r, r).real
            p = r + (rr2 / rr) * p
            rr = rr2
            it += 1
        self.cg_iters += it
        return x

    def refresh(self, rng):
        lat = self.lat
        s = np.sqrt(0.5)
        ze = (rng.normal(size=(lat.V, 3)) + 1j * rng.normal(size=(lat.V, 3))) * s * lat.evenf
        zo = (rng.normal(size=(lat.V, 3)) + 1j * rng.normal(size=(lat.V, 3))) * s * lat.oddf
        # phi = m*ze + D^dag zo = m*ze - D zo
        return self.m * ze - self.D(zo)

    def action_force(self, phi, want_force=True, tol=None):
        chi = self.cg(phi, tol=tol)
        S = np.vdot(phi, chi).real
        if not want_force:
            return S, None
        lat = self.lat
        psi1 = self.D(chi)                     # odd-supported
        U = self.U
        def Fab(a, b):
            # Z1 = U b(s+mu) a(s)^dag ; Z2^dag = b(s) a(s+mu)^dag U^dag
            bf = b[lat.fwd]                    # (4,V,3)
            af = a[lat.fwd]
            Z1 = U @ (bf[..., :, None] * np.conj(a)[None, :, None, :])
            Z2d = (b[None, :, :, None] * np.conj(af)[..., None, :]) @ dag(U)
            return Z1 + Z2d
        Fx = Fab(chi, psi1) - Fab(psi1, chi)
        N = 0.5 * 1j * lat.ef[..., None] * Fx
        return S, N


def kinetic(P):
    return 0.5 * np.einsum('msij,msji->', P, P).real


class HMC:
    def __init__(self, lat, beta, Ns=0, m=0.1, nmd=10, tau=1.0, tol_force=1e-7, tol_act=1e-11, seed=0):
        self.tol_force = tol_force
        self.tol_act = tol_act
        self.lat = lat
        self.g = Gauge(lat, beta)
        self.Ns = Ns
        self.f = Fermion(lat, m, tol_act) if Ns > 0 else None
        self.nmd = nmd
        self.tau = tau
        self.rng = np.random.default_rng(seed)
        self.U = random_su3(self.rng, (4, lat.V))   # hot start
        self.nacc = 0
        self.ntraj = 0
        self.dH = []

    def force_total(self, U, phis):
        N = self.g.force(U)
        if self.Ns > 0:
            self.f.prep(U)
            for phi in phis:
                _, Nf = self.f.action_force(phi, tol=self.tol_force)
                N = N + Nf
        return traceless_herm(N)

    def action(self, U, phis):
        S = self.g.action(U)
        if self.Ns > 0:
            self.f.prep(U)
            for phi in phis:
                Sf, _ = self.f.action_force(phi, want_force=False, tol=self.tol_act)
                S += Sf
        return S

    def trajectory(self, thermal=False):
        lat = self.lat
        rng = self.rng
        U0 = self.U.copy()
        P = herm_traceless_gauss(rng, (4, lat.V))
        phis = []
        if self.Ns > 0:
            self.f.prep(U0)
            phis = [self.f.refresh(rng) for _ in range(self.Ns)]
        H0 = kinetic(P) + self.action(U0, phis)
        # Omelyan 2MN
        lam = 0.1931833275037836
        dt = self.tau / self.nmd
        U = U0.copy()
        def upd_U(U, P, h):
            return expm_ih(h * P) @ U
        def upd_P(U, P, h):
            return P - h * self.force_total(U, phis)
        P = upd_P(U, P, lam * dt)
        for k in range(self.nmd):
            U = upd_U(U, P, 0.5 * dt)
            P = upd_P(U, P, (1 - 2 * lam) * dt)
            U = upd_U(U, P, 0.5 * dt)
            if k < self.nmd - 1:
                P = upd_P(U, P, 2 * lam * dt)
            else:
                P = upd_P(U, P, lam * dt)
        if self.ntraj % 20 == 0:
            U = proj_su3(U)
        H1 = kinetic(P) + self.action(U, phis)
        dH = H1 - H0
        self.dH.append(dH)
        self.ntraj += 1
        if thermal or rng.random() < np.exp(-dH):
            self.U = U
            self.nacc += 1
            acc = True
        else:
            acc = False
        return acc, dH
