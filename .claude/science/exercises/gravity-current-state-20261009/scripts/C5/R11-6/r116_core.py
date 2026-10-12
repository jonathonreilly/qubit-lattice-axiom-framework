"""R11-6 core: assembled Sokolov-packed three-body BT law, d = 1, fixed total momentum P,
free rest-frame chart (FC prescription), dense matrices.

Prescription (stated, the registration's 'P != 0 ring' prescription):
  * The P-fibre of a ring of size L is represented by the free boost of the P = 0 rest-frame fibre
    (Lambda_P is a relabelling): every fibre uses the same internal grid.
  * Internal (rest-frame, sum p = 0) plane: master chart = channel a Jacobi chart (p3, q12), uniform
    cell-centred grid of spacing h = 2 pi / L on |p3| < PA, |q12| < QA; half-density in (p3, q12).
  * Channel c in {a, b, c} (pairs 12, 23, 31; spectators 3, 1, 2) uses its own Jacobi chart (s, q) with the same
    spacing; chart changes are 2D cubic-spline (not-a-knot) interpolation with exact half-density Jacobians.
  * Pair law (R7-6/R8-1, d = 1 fermion pair): M_pair = M0(q) + lam h g g^T, g odd, C^inf, supp |q| < kappa;
    m = 0.3, kappa = 0.25, lam = -3 (dimer 0.51528).  Plateau c(P_ij) = 1 (R7-6's plateau covers |P_ij| <= 0.8).
  * Packing unitaries in FC: B_c = R_M R_0^dag  (lab-chart B_c = R_0^dag R_M conjugated by the free boost).
  * Sokolov packing (choice S3): A = 1 + sum_c (B_c - 1), B = A (A^dag A)^(-1/2) (polar part, via SVD).
  * BT: M_BT = M0 + sum_c (M_(c) - M0); H_BT(P) = sqrt(M_BT^2 + P^2); H_S = B^dag H_BT B.
  * Channel-a cluster law in FC: H_a = B_a^dag sqrt(M_(a)^2 + P^2) B_a.
"""
import numpy as np
from scipy.interpolate import CubicSpline

m, KAP, LAM = 0.3, 0.25, -3.0

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
def g(q): return q*sstep(1.0 - (q/KAP)**2)/KAP
def eps(k): return np.sqrt(m*m + k*k)
def M0p(q): return 2*np.sqrt(m*m + q*q)

def pair_momenta(Pp, q):
    v = np.arcsinh(q/m); Y = np.arcsinh(Pp/(2*m*np.cosh(v)))
    return m*np.sinh(Y+v), m*np.sinh(Y-v)
def q_of(kf, ks): return m*np.sinh(0.5*(np.arcsinh(kf/m) - np.arcsinh(ks/m)))
def jac(Pp, q):
    """|d k_f / d q| at fixed pair momentum = Lebesgue(p_spec, p_f) per d(p_spec) dq."""
    kf, ks = pair_momenta(Pp, q); v = np.arcsinh(q/m)
    return 1.0/(0.5*m*np.cosh(v)*(1/eps(kf) + 1/eps(ks)))

def cgrid(A, h):
    n = int(np.floor(A/h)); return (np.arange(-n, n) + 0.5)*h

def card(x, xt):
    """cubic-spline cardinal weights: (len(xt), len(x)); zero outside [x0, x-1]."""
    W = CubicSpline(x, np.eye(len(x)))(xt)
    out = (xt < x[0] - 1e-12) | (xt > x[-1] + 1e-12)
    W[out] = 0.0
    return W

# lab <-> rest-frame spectator maps at total P (spectator lab k, cluster mass mu)
def phi(k, mu, P):          # lab k -> rest-frame u
    E = np.sqrt(mu*mu + (P-k)**2) + eps(k); Th = np.arctanh(P/E)
    return m*np.sinh(np.arcsinh(k/m) - Th)
def dphi(k, mu, P):
    Ep = np.sqrt(mu*mu + (P-k)**2); E = Ep + eps(k); Th = np.arctanh(P/E)
    dE = -(P-k)/Ep + k/eps(k); dTh = -P*dE/(E*E - P*P)
    return m*np.cosh(np.arcsinh(k/m) - Th)*(1/eps(k) - dTh)
def phiinv(u, mu, P):       # rest-frame u -> lab k  (free boost by rapidity of the (mu, u) system)
    Mr = np.sqrt(mu*mu + u*u) + eps(u); Th = np.arcsinh(P/Mr)
    return m*np.sinh(np.arcsinh(u/m) + Th)

class Fibre:
    def __init__(self, L, P, PA=0.5, QA=0.5, qpad=4, PIN=0.38, POUT=0.48):
        self.L, self.P = L, P; h = 2*np.pi/L; self.h = h; self.PIN, self.POUT = PIN, POUT
        self.p = cgrid(PA, h); self.q = cgrid(QA, h)
        self.Np, self.Nq = len(self.p), len(self.q); self.N = self.Np*self.Nq
        P3, Q12 = np.meshgrid(self.p, self.q, indexing='ij')
        self.P3, self.Q12 = P3.ravel(), Q12.ravel()
        # momenta of master points
        p1, p2 = pair_momenta(-self.P3, self.Q12)
        self.mom = np.stack([p1, p2, self.P3])         # (3, N)
        self.Ja = jac(-self.P3, self.Q12)
        # chart q-grid for channel operators: odd sector, q in (0, kappa + qpad h)
        nq = int(np.ceil(KAP/h)) + qpad
        self.qc = (np.arange(nq) + 0.5)*h
        self.sc = self.p.copy()
        # free 3-body mass on master
        self.M0 = np.sqrt(M0p(self.Q12)**2 + self.P3**2) + eps(self.P3)
        # pair spectral data on the odd chart grid (quadrature weight 2h, as R9-3)
        Mo = np.diag(M0p(self.qc)) + LAM*2*h*np.outer(g(self.qc), g(self.qc))
        self.mu, self.chi = np.linalg.eigh(Mo)
        self.nu = M0p(self.qc)
        self._ops = {}

    # channel c: 0 = a (pair 12, spec 3), 1 = b (pair 23, spec 1), 2 = c (pair 31, spec 2)
    def chart_to_mom(self, c, s, q):
        kf, ks = pair_momenta(-s, q)
        if c == 0: return kf, ks, s
        if c == 1: return s, kf, ks
        return ks, s, kf
    def mom_to_chart(self, c, p1, p2, p3):
        if c == 0: return p3, q_of(p1, p2)
        if c == 1: return p1, q_of(p2, p3)
        return p2, q_of(p3, p1)

    def interp_master_to_chart(self, c):
        """matrix (Ns*Nqc, N): odd part of a master half-density, as a chart-c half-density on (s, q>0)."""
        S, Q = np.meshgrid(self.sc, self.qc, indexing='ij'); S, Q = S.ravel(), Q.ravel()
        rows = []
        for sg in (+1, -1):
            p1, p2, p3 = self.chart_to_mom(c, S, sg*Q)
            p3m, q12 = p3, q_of(p1, p2)
            w = np.sqrt(jac(-S, sg*Q)/jac(-p3m, q12))
            Wp = card(self.p, p3m); Wq = card(self.q, q12)
            R = (Wp[:, :, None]*Wq[:, None, :]).reshape(len(S), self.N)*w[:, None]
            rows.append(R)
        return (rows[0] - rows[1])/np.sqrt(2)

    def interp_chart_to_master(self, c):
        """matrix (N, Ns*Nqc): odd chart function (s, q>0) -> master half-density."""
        s, qq = self.mom_to_chart(c, *self.mom)
        sg = np.sign(qq); aq = np.abs(qq)
        w = np.sqrt(self.Ja/jac(-s, qq))
        # odd extension in q: f(s, -q) = -f(s, q); the odd basis vector carries 1/sqrt(2)
        Ws = card(self.sc, s)
        qext = np.concatenate([-self.qc[::-1], self.qc])
        Wq_ext = card(qext, qq)                       # (N, 2 nq)
        nq = len(self.qc)
        Wq = Wq_ext[:, nq:] - Wq_ext[:, :nq][:, ::-1]  # odd combination
        # beyond chart q range -> zero (operator - 1 vanishes there)
        Wq[aq > self.qc[-1] + 0.5*self.h] = 0.0
        R = (Ws[:, :, None]*Wq[:, None, :]).reshape(self.N, len(self.sc)*nq)*w[:, None]/np.sqrt(2)
        return R

    def chart_Bm1(self, adj=False):
        """(B_c - 1) on the chart grid (Ns*nq)^2, FC form B = R_M R_0^dag; identical for every channel."""
        P = self.P; s = self.sc; Ns = len(s); nq = len(self.qc)
        X = np.zeros((Ns, nq, Ns, nq))
        for n in range(nq):
            for j in range(nq):
                # (R_mu R_nu^dag h)(u) = h(u') sqrt(du'/du),  u' = phi_nu(phiinv_mu(u))
                k = phiinv(s, self.mu[n], P)
                up = phi(k, self.nu[j], P)
                # du'/du = dphi_nu(k) / dphi_mu(k)
                d = dphi(k, self.nu[j], P)/dphi(k, self.mu[n], P)
                T = card(s, up)*np.sqrt(np.abs(d))[:, None]       # (Ns_out, Ns_in)
                X[:, :, :, j] += self.chi[:, n][None, :, None]*self.chi[j, n]*T[:, None, :]
        for j in range(nq): X[:, j, :, j] -= np.eye(Ns)
        X = X.reshape(Ns*nq, Ns*nq)
        return X.conj().T if adj else X

    def chart_dM(self):
        """(M_(c) - M0) on the chart grid: block diagonal in s: sqrt(M_pair^2+s^2) - sqrt(M0^2+s^2)."""
        s = self.sc; Ns = len(s); nq = len(self.qc)
        X = np.zeros((Ns, nq, Ns, nq))
        for i, si in enumerate(s):
            f = (self.chi*np.sqrt(self.mu**2 + si*si))@self.chi.T - np.diag(np.sqrt(self.nu**2 + si*si))
            X[i, :, i, :] = f
        return X.reshape(Ns*nq, Ns*nq)

    def build(self):
        N = self.N
        Bm1c = self.chart_Bm1(); dMc = self.chart_dM()
        self.Bm1 = []; self.dM = []
        # edge taper (box-edge artefact control): W = prod_i w(p_i), w = 1 on |p| < PIN, smooth to 0 at POUT
        PIN, POUT = self.PIN, self.POUT
        wv = np.prod(sstep((POUT - np.abs(self.mom))/(POUT - PIN)), axis=0)
        self.W = wv
        for c in range(3):
            I = self.interp_master_to_chart(c); E = self.interp_chart_to_master(c)
            self.Bm1.append(wv[:, None]*(E@Bm1c@I)*wv[None, :])
            dm = E@dMc@I; self.dM.append(0.5*(dm + dm.T))
        Id = np.eye(N)
        self.Bc = [Id + X for X in self.Bm1]
        A = Id + sum(self.Bm1)
        U, S, Vh = np.linalg.svd(A)
        self.smin, self.smax = S.min(), S.max()
        self.B = U@Vh
        self.MBT = np.diag(self.M0) + sum(self.dM)
        w, V = np.linalg.eigh(self.MBT); self.mbt_w, self.mbt_V = w, V
        self.HBT = (V*np.sqrt(w**2 + self.P**2))@V.T
        self.HS = self.B.conj().T@self.HBT@self.B
        Ma = np.diag(self.M0) + self.dM[0]
        wa, Va = np.linalg.eigh(Ma)
        Hpa = (Va*np.sqrt(wa**2 + self.P**2))@Va.T
        self.Ha = self.Bc[0].conj().T@Hpa@self.Bc[0]
        return self

    def unitarity(self):
        Id = np.eye(self.N)
        return [np.linalg.norm(Bc.conj().T@Bc - Id, 2) for Bc in self.Bc], np.linalg.norm(self.B.conj().T@self.B - Id, 2)

    def state(self, r, kind='dimer', p3c=-0.10, sig=0.08, qc0=0.08, sq=0.06):
        if kind == 'dimer':
            # odd bound state of the pair on the master q grid: chi_b(q) ~ g(q)/(M0(q) - mu_b)
            mub = self.mu[0]
            f = g(self.q)/(M0p(self.q) - mub)
        else:
            f = np.exp(-(self.q - qc0)**2/(4*sq*sq)) - np.exp(-(self.q + qc0)**2/(4*sq*sq))
        G = np.exp(-(self.p - p3c)**2/(4*sig*sig))*np.exp(-1j*self.p*r)
        psi = (G[:, None]*f[None, :]).ravel().astype(complex)
        return psi/np.linalg.norm(psi)
