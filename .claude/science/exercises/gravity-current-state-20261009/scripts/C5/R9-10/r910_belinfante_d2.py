"""C5 R9-10 (d = 2): a symmetric (Belinfante) stress for R8-1's interacting two-body box law, checked in
R8-1's canonical chart (box sector, c = 1), plus the fall of bound doublet states with spin, and the spin couplings.

Representation (R8-1 r81_d2_chart_algebra.py, refereed CWC): psi(P, q) on a spectral P-grid (NP^2, window +-WIN)
x polar q-grid (Gauss-Legendre Nr x Nf), X_NW = i grad_P (FFT), S = -i d/dphi_q (FFT), M = M0 + V (p-wave doublet),
H = sqrt(M^2 + P^2), J = X x P + S, K_a = (1/2){H, X_a} + eps_ab P_b S/(M + H).   [independent of the stress below]

Stress (box sector; T(Q) raises total momentum by Q; [H, T^{0nu}(Q)] = Q_j T^{j nu}(Q) since D(Q) = Q for |Q_i| <= 1):
  T00(Q)  = e^{iQX/2} Tc(Pbar,Q) e^{iQX/2},        Tc = H(Pbar) + i Q_a B_a(Pbar),  B_a = eps_ab Pbar_b S f,  f = 1/(M+H)
  T^{b0}(Q) = e^{iQX/2} [Tc Delta_b + c Sig eps_bk Q_k] e^{iQX/2},  c = -i,  Sig = S M/(2H)   (Belinfante curl)
  T^{ij}(Q) = e^{iQX/2} [Tc Delta_i Delta_j + c Sig (Delta_i eps_jk Q_k + Delta_j eps_ik Q_k)] e^{iQX/2}   (symmetric)
  Delta_b(Pbar, Q): staircase-symmetrised divided differences of h(P) = sqrt(mu^2 + P^2) per M-eigenvalue mu,
  sum_b Q_b Delta_b = h(Pbar + Q/2) - h(Pbar - Q/2)  (telescoping).
Checks:
 (A) moments by 8th-order finite differences in Q, against R8-1's independent generators:
     T00(0) = H ; -i d/dQ_a T00 |0 = K_a ; T^{b0}(0) = P_b ; J_T := eps_ab (-i d/dQ_a) T^{b0}|0 = J.
     Comparator: dust current (no curl, c = 0): J_T = X x P + S (1 - M/H).
 (B) Ward identities at finite Q (nu = 0 and nu = x, y), Hermiticity T(Q)^dag = T(-Q), symmetry.
 (C) fall in a uniform lapse H_g = H + g D1 (g along x), D1 = first moment of T00 (= K, checked in A):
     O(g) acceleration of the centre of energy X_E = <K>/<H>, from exact nested commutators, for bound doublet
     states S = +1 / -1, binding fractions 0.05, 0.15, 0.30 (M_b = 0.95, 0.85, 0.70), at rest and moving with a
     COMMON velocity (P0 = M_b u).  Prediction (box Poincare algebra): Xdd_E/g = -e_x + 2 V_x V.
     Comparators: D1 = (1/2){H, X} (spin term omitted from the energy dipole), D1 = K0 (binding does not gravitate).
 (D) spin couplings: lapse spin-orbit energy <g.D1>(S=+1) - <g.D1>(S=-1) vs the Thomas/BT value
     2 g_a eps_ab <P_b f>; gravitomagnetic: <J_T>(S=+-1) vs <J>.
"""
import numpy as np, time, sys
from r81_common import BTKernel, lam_for_mass

m, KAP = 0.5, 0.8
NP, WIN = 64, 1.0
Nr, Nf, QR = 40, 16, 1.8
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)

Pg = np.linspace(-WIN, WIN, NP, endpoint=False); dP = Pg[1] - Pg[0]
kP = 2*np.pi*np.fft.fftfreq(NP, d=dP)
PX, PY = np.meshgrid(Pg, Pg, indexing='ij'); P2 = PX**2 + PY**2
xr, wr = np.polynomial.legendre.leggauss(Nr); r = 0.5*QR*(xr + 1); wr = 0.5*QR*wr
ph = 2*np.pi*np.arange(Nf)/Nf
R, PH = np.meshgrid(r, ph, indexing='ij'); qx, qy = (R*np.cos(PH)).ravel(), (R*np.sin(PH)).ravel()
wq = (wr[:, None]*r[:, None]*np.full((1, Nf), 2*np.pi/Nf)).ravel(); Rr = R.ravel()
sw = np.sqrt(wq); Nq = Nr*Nf
M0q = 2*np.sqrt(m*m + Rr**2)
lf = np.fft.fftfreq(Nf, d=1.0/Nf)
n_ = np.linalg.norm

# ---- joint (M, S) eigenbasis: state c[Px, Py, n, l]; n = radial eigen-index of M_l, l = angular momentum ----
lf = np.fft.fftfreq(Nf, d=1.0/Nf)            # l labels (S eigenvalues), as R8-1's Sop
LL = lf[None, None, None, :]
def Sop(v): return LL*v
def Xop(v, a):
    kk = kP[:, None, None, None] if a == 0 else kP[None, :, None, None]
    return 1j*np.fft.ifft(1j*kk*np.fft.fft(v, axis=a), axis=a)
def shift(v, Qx, Qy):
    """(e^{i Q.X} v)(P) = v(P - Q): band-limited shift on the periodic P-grid."""
    f = np.fft.fft2(v, axes=(0, 1))
    f = f*np.exp(-1j*(kP[:, None, None, None]*Qx + kP[None, :, None, None]*Qy))
    return np.fft.ifft2(f, axes=(0, 1))
Pop = lambda v, a: (PX if a == 0 else PY)[:, :, None, None]*v
P2b = P2[:, :, None, None]; PXb = PX[:, :, None, None]; PYb = PY[:, :, None, None]
M0r = 2*np.sqrt(m*m + r**2)

class Law:
    def __init__(self, MU_B):
        Kk = BTKernel(m, KAP, -1.0, 2, nq=3001)
        bq = Kk.b(Rr**2)
        self.lam = lam_for_mass(m, KAP, 2, MU_B, nq=3001)
        Vm = self.lam*(np.outer(qx*bq*sw, qx*bq*sw) + np.outer(qy*bq*sw, qy*bq*sw))
        Mfull = np.diag(M0q) + Vm                                  # grid basis (r-major, phi-minor), as R8-1
        Fp = np.exp(-1j*np.outer(lf, ph))/np.sqrt(Nf)              # unitary DFT along phi: (l, j)
        T = np.kron(np.eye(Nr), Fp)
        Mt = T @ Mfull @ T.conj().T
        Mt4 = Mt.reshape(Nr, Nf, Nr, Nf)
        blk = np.array([Mt4[:, l, :, l] for l in range(Nf)])        # (Nf, Nr, Nr)
        off = np.abs(Mt4).copy()
        for l in range(Nf): off[:, l, :, l] = 0
        self.offblock = off.max()
        self.mu = np.zeros((Nr, Nf)); self.U = np.zeros((Nf, Nr, Nr), complex)
        for l in range(Nf):
            w_, U_ = np.linalg.eigh(blk[l]); self.mu[:, l] = w_; self.U[l] = U_
        self.mub = self.mu[None, None, :, :]
        self.Hd = np.sqrt(self.mub**2 + P2b)
    def g0(self, v, fun):
        """apply fun(M0, P) (M0 diagonal on the radial grid) to an eigenbasis state."""
        vt = np.transpose(v, (3, 0, 1, 2)).reshape(Nf, NP*NP, Nr)          # (l, P, n)
        vg = vt @ np.transpose(self.U, (0, 2, 1))                            # sum_n U[l, r, n] v[n]
        vg = vg.reshape(Nf, NP, NP, Nr)*np.transpose(fun(M0r[None, None, :, None])*np.ones((NP, NP, Nr, 1)), (3, 0, 1, 2))
        vb = vg.reshape(Nf, NP*NP, Nr) @ self.U.conj()                       # sum_r conj(U[l, r, n]) vg[r]
        return np.transpose(vb.reshape(Nf, NP, NP, Nr), (1, 2, 3, 0))
    def H(self, v):  return self.Hd*v
    def F(self, v):  return v/(self.mub + self.Hd)
    def Sig(self, v): return LL*(self.mub/(2*self.Hd))*v
    def Kfull(self, v, a):
        base = 0.5*(self.H(Xop(v, a)) + Xop(self.H(v), a))
        sp = Sop(self.F(v))
        return base + (Pop(sp, 1) if a == 0 else -Pop(sp, 0))
    def Knospin(self, v, a):
        return 0.5*(self.H(Xop(v, a)) + Xop(self.H(v), a))
    def H0(self, v): return self.g0(v, lambda M0: np.sqrt(M0**2 + P2b))
    def K0(self, v, a):
        base = 0.5*(self.H0(Xop(v, a)) + Xop(self.H0(v), a))
        sp = Sop(self.g0(v, lambda M0: 1.0/(M0 + np.sqrt(M0**2 + P2b))))
        return base + (Pop(sp, 1) if a == 0 else -Pop(sp, 0))
    def J(self, v): return Xop(Pop(v, 1), 0) - Xop(Pop(v, 0), 1) + Sop(v)
    def Delta(self, v, b, Qx, Qy):
        """staircase-symmetrised divided difference of h = sqrt(mu^2+P^2) along b, at the grid P (= Pbar)."""
        mu = self.mub
        h = lambda dx, dy: np.sqrt(mu**2 + (PXb + dx)**2 + (PYb + dy)**2)
        Pm = (-Qx/2, -Qy/2)
        if b == 0:
            if abs(Qx) < 1e-14:
                hx = lambda y0: PXb/np.sqrt(mu**2 + PXb**2 + (PYb + y0)**2)
                return 0.5*(hx(Pm[1]) + hx(Pm[1] + Qy))*v
            num = 0.5*((h(Pm[0] + Qx, Pm[1]) - h(*Pm)) + (h(Qx/2, Qy/2) - h(Pm[0], Pm[1] + Qy)))
            return (num/Qx)*v
        else:
            if abs(Qy) < 1e-14:
                hy = lambda x0: PYb/np.sqrt(mu**2 + (PXb + x0)**2 + PYb**2)
                return 0.5*(hy(Pm[0]) + hy(Pm[0] + Qx))*v
            num = 0.5*((h(Qx/2, Qy/2) - h(Pm[0] + Qx, Pm[1])) + (h(Pm[0], Pm[1] + Qy) - h(*Pm)))
            return (num/Qy)*v
    # ---- the stress, applied to a vector ----
    def Tc(self, v, Qx, Qy):
        sp = Sop(self.F(v))
        return self.H(v) + 1j*(Qx*PYb*sp - Qy*PXb*sp)
    def T00(self, v, Qx, Qy):
        w = shift(v, Qx/2, Qy/2); w = self.Tc(w, Qx, Qy); return shift(w, Qx/2, Qy/2)
    def T0b(self, v, b, Qx, Qy, curl=True):
        w = shift(v, Qx/2, Qy/2)
        o = self.Tc(self.Delta(w, b, Qx, Qy), Qx, Qy)
        if curl:                                       # c Sig eps_bk Q_k, c = -i ; eps_xy = +1
            ek = Qy if b == 0 else -Qx
            o = o + (-1j)*ek*self.Sig(w)
        return shift(o, Qx/2, Qy/2)
    def Tij(self, v, i, j, Qx, Qy):
        w = shift(v, Qx/2, Qy/2)
        o = self.Tc(self.Delta(self.Delta(w, j, Qx, Qy), i, Qx, Qy), Qx, Qy)
        ek = lambda b: (Qy if b == 0 else -Qx)
        sg = self.Sig(w)
        o = o + (-1j)*(self.Delta(ek(j)*sg, i, Qx, Qy) + self.Delta(ek(i)*sg, j, Qx, Qy))
        return shift(o, Qx/2, Qy/2)

c8 = np.array([1/280, -4/105, 1/5, -4/5, 0, 4/5, -1/5, 4/105, -1/280])
def dQ(fun, a, h=4e-3):
    acc = 0
    for i, c in enumerate(c8):
        if c == 0: continue
        s = (i - 4)*h
        acc = acc + c*(fun(s, 0.0) if a == 0 else fun(0.0, s))
    return acc/h

def packet(law, P0, sgn, sig=0.07, mix=False):
    """bound doublet state with S = sgn (lowest M eigenstate in the l = sgn block), Gaussian in P at P0;
    mix=True adds continuum (scattering) states in l = 0, +-1, +-2 with complex weights."""
    l_idx = int(np.where(lf == sgn)[0][0])
    chi = np.zeros((Nr, Nf), complex); chi[0, l_idx] = 1.0
    if mix:
        for l, wgt in ((0, 0.5), (1, 0.4j), (-1, 0.3), (2, 0.25 - 0.2j), (-2, 0.2)):
            li = int(np.where(lf == l)[0][0]); chi[3:9, li] += wgt*np.linspace(1, 0.4, 6)
    A = np.exp(-((PX - P0[0])**2 + (PY - P0[1])**2)/(4*sig**2))
    v = A[:, :, None, None]*chi[None, None, :, :]
    return v/n_(v), law.mu[0, l_idx]

ip = lambda a, b: np.vdot(a, b)
def comm_exp(A, B, psi):          # <i[A,B]> = -2 Im <A psi|B psi>
    return -2*np.imag(ip(A(psi), B(psi)))
def dcomm_exp(A, B, C, psi):      # <i[A, i[B,C]]> = -2 Re <A psi|(BC - CB) psi>
    return -2*np.real(ip(A(psi), B(C(psi)) - C(B(psi))))

t0 = time.time()
pr('R9-10 d = 2 chart run: NP = %d, window +-%.1f, q-grid %d x %d, m = %.2f, kappa = %.2f' % (NP, WIN, Nr, Nf, m, KAP))
laws = {}
for MB in (0.95, 0.85, 0.70):
    laws[MB] = Law(MB)
    pr('  M_b target %.2f: lam = %.6f, lowest M eigenvalues (l=0,+1,-1) = %.10f %.10f %.10f ; max off-block |M_ll\'| = %.1e' % (MB, laws[MB].lam, laws[MB].mu[0,0], laws[MB].mu[0,1], laws[MB].mu[0,-1], laws[MB].offblock))

# ---------------- (A) moments, (B) Ward identities ----------------
law = laws[0.85]
for P0 in ((0.0, 0.0), (0.22, -0.09)):
    for sgn in (+1, -1):
        psi, evS = packet(law, P0, sgn, mix=True)
        Hv = law.H(psi)
        r0 = n_(law.T00(psi, 0.0, 0.0) - Hv)/n_(Hv)
        res = []
        for a in (0, 1):
            fm = dQ(lambda qx_, qy_: law.T00(psi, qx_, qy_), a)
            K = law.Kfull(psi, a)
            res.append(n_(-1j*fm - K)/n_(K))
        Kns = law.Knospin(psi, 0)
        fm0 = -1j*dQ(lambda qx_, qy_: law.T00(psi, qx_, qy_), 0)
        dsp = n_(law.Kfull(psi, 0) - Kns)
        rP = [n_(law.T0b(psi, b, 0.0, 0.0) - Pop(psi, b))/max(n_(Pop(psi, b)), 1e-300) for b in (0, 1)]
        # angular moment, Belinfante and dust
        JT = (-1j)*(dQ(lambda qx_, qy_: law.T0b(psi, 1, qx_, qy_), 0) - dQ(lambda qx_, qy_: law.T0b(psi, 0, qx_, qy_), 1))
        JTd = (-1j)*(dQ(lambda qx_, qy_: law.T0b(psi, 1, qx_, qy_, curl=False), 0) - dQ(lambda qx_, qy_: law.T0b(psi, 0, qx_, qy_, curl=False), 1))
        Jv = law.J(psi)
        pr('(A) P0 = %s, bound S = %+d (mu_b = %.10f) + continuum mix: |T00(0)-H|/|H| = %.1e ; |FD 1st moment - K_x|/|K_x| = %.1e, K_y: %.1e'
           % (P0, sgn, evS, r0, res[0], res[1]))
        pr('    spin-term share |K_x - K_x(no spin)|/|K_x| = %.3e (so the check resolves the spin term); |T^{b0}(0) - P_b|/|P_b| = %.1e, %.1e'
           % (dsp/n_(law.Kfull(psi, 0)), rP[0], rP[1]))
        pr('    J_T (Belinfante) vs J: |J_T psi - J psi|/|J psi| = %.1e ; <J_T> = %.12f, <J> = %.12f ; dust (no curl): <J_T> = %.6f'
           % (n_(JT - Jv)/n_(Jv), np.real(ip(psi, JT)), np.real(ip(psi, Jv)), np.real(ip(psi, JTd))))
        # Ward identities at finite Q, Hermiticity, symmetry
        for (Qx, Qy) in ((0.13, -0.07), (-0.21, 0.17)):
            T00v = law.T00(psi, Qx, Qy)
            lhs0 = law.H(T00v) - law.T00(Hv, Qx, Qy)
            rhs0 = Qx*law.T0b(psi, 0, Qx, Qy) + Qy*law.T0b(psi, 1, Qx, Qy)
            w1 = [n_(law.H(law.T0b(psi, i, Qx, Qy)) - law.T0b(Hv, i, Qx, Qy)
                     - (Qx*law.Tij(psi, 0, i, Qx, Qy) + Qy*law.Tij(psi, 1, i, Qx, Qy))) for i in (0, 1)]
            sc = n_(lhs0)
            sym = n_(law.Tij(psi, 0, 1, Qx, Qy) - law.Tij(psi, 1, 0, Qx, Qy))/n_(law.Tij(psi, 0, 1, Qx, Qy))
            # Hermiticity: <phi|T(Q) psi> = <T(-Q) phi|psi>
            phi, _ = packet(law, (P0[0] + Qx, P0[1] + Qy), -sgn, mix=True)
            herm = [abs(ip(phi, law.T00(psi, Qx, Qy)) - ip(law.T00(phi, -Qx, -Qy), psi)),
                    abs(ip(phi, law.T0b(psi, 0, Qx, Qy)) - ip(law.T0b(phi, 0, -Qx, -Qy), psi)),
                    abs(ip(phi, law.Tij(psi, 0, 1, Qx, Qy)) - ip(law.Tij(phi, 0, 1, -Qx, -Qy), psi))]
            pr('(B)   Q = (%+.2f,%+.2f): nu=0 |[H,T00]-Q.T^{.0}|/|[H,T00]| = %.1e ; nu=x,y abs = %.1e, %.1e (scale %.2e) ; '
               'sym %.1e ; herm (T00,T0x,Txy) = %.1e %.1e %.1e (scale %.2e)'
               % (Qx, Qy, n_(lhs0 - rhs0)/sc, w1[0], w1[1], sc, sym, herm[0], herm[1], herm[2], abs(ip(phi, T00v))))
pr('(A,B) time %.1fs' % (time.time() - t0))

# ---------------- (C) fall, (D) spin couplings ----------------
t0 = time.time()
u = np.array([0.30, 0.12])        # common rapidity-like velocity parameter: P0 = M_b u (start)
VSTAR = np.array([0.28, 0.11])    # common target velocity <P>/<H> for moving bodies
rows = []
for MB, law in laws.items():
    for mov in (False, True):
        P0 = tuple(MB*u) if mov else (0.0, 0.0)
        for sgn in (+1, -1):
            psi, _ = packet(law, P0, sgn)
            if mov:   # tune P0 so that V = <P>/<H> equals the common target VSTAR exactly (equal-velocity Eotvos comparison)
                P0 = np.array(P0)
                for it in range(60):
                    hh = np.real(ip(psi, law.H(psi))); Vc = np.array([np.real(ip(psi, Pop(psi, 0))), np.real(ip(psi, Pop(psi, 1)))])/hh
                    if np.abs(Vc - VSTAR).max() < 2e-16: break
                    P0 = P0*(VSTAR/Vc); psi, _ = packet(law, tuple(P0), sgn)
                P0 = tuple(P0)
            H = law.H; Kx = lambda v: law.Kfull(v, 0); Ky = lambda v: law.Kfull(v, 1)
            h = np.real(ip(psi, H(psi))); k = [np.real(ip(psi, Kx(psi))), np.real(ip(psi, Ky(psi)))]
            Pm = [np.real(ip(psi, Pop(psi, 0))), np.real(ip(psi, Pop(psi, 1)))]
            V = np.array(Pm)/h
            K0x = lambda v: law.K0(v, 0)
            res = {}
            for lab, D in (('K (Belinfante dipole)', Kx), ('(1/2){H,X} (spin term omitted)', lambda v: law.Knospin(v, 0)),
                           ('K0 (binding not gravitating)', K0x)):
                a1 = comm_exp(D, H, psi)
                p = [comm_exp(H, Kx, psi), comm_exp(H, Ky, psi)]
                e = [comm_exp(D, Kx, psi), comm_exp(D, Ky, psi)]
                a2 = dcomm_exp(H, D, H, psi)
                z = [dcomm_exp(H, H, Kb, psi) for Kb in (Kx, Ky)]
                cd = [dcomm_exp(D, H, Kb, psi) + dcomm_exp(H, D, Kb, psi) for Kb in (Kx, Ky)]
                acc = np.array([cd[b]/h - 2*p[b]*a1/h**2 - k[b]*a2/h**2 for b in (0, 1)])
                pred = np.array([-1 + 2*V[0]*V[0], 2*V[0]*V[1]])
                wP = -comm_exp(D, lambda v: Pop(v, 0), psi)/h     # weight on the lattice momentum
                vel = np.array([e[b]/h - k[b]*a1/h**2 for b in (0, 1)])   # O(g) part of d X_E/dt
                Dexp = np.real(ip(psi, D(psi)))
                res[lab] = (acc, pred, wP, vel, Dexp, np.array(z)/h)
            Jexp = np.real(ip(psi, law.J(psi)))
            fexp = np.real(ip(psi, Pop(Sop(law.F(psi)), 1)))            # <P_y S f>  (g along x: eps_xy P_y S f)
            rows.append((MB, mov, sgn, V, h, res, Jexp, fexp))
            r_ = res['K (Belinfante dipole)']
            pr('(C) M_b %.2f f_B %.2f %s S=%+d: V = (%.4f,%.4f) | D1=K: Xdd/g = (%.15f, %.15f), minus prediction = (%.1e, %.1e), w_P-1 = %.1e, O(1) drift %.1e'
               % (MB, 1 - MB, 'moving' if mov else 'rest  ', sgn, V[0], V[1], r_[0][0], r_[0][1], r_[0][0] - r_[1][0], r_[0][1] - r_[1][1], r_[2] - 1, np.abs(r_[5]).max()))
            for lab in ('(1/2){H,X} (spin term omitted)', 'K0 (binding not gravitating)'):
                rr = res[lab]
                pr('      comparator D1 = %-32s Xdd/g = (%.9f, %.9f), minus prediction = (%.2e, %.2e), w_P = %.9f'
                   % (lab, rr[0][0], rr[0][1], rr[0][0] - rr[1][0], rr[0][1] - rr[1][1], rr[2]))
            vpred = np.array([k[0]*Pm[0]/h**2, Jexp/h + k[1]*Pm[0]/h**2])     # Poincare/elevator: eps_xb <J>/<H> + <K_b><P_x>/<H>^2
            rs = res['(1/2){H,X} (spin term omitted)']
            pr('      O(g) velocity of X_E: D1 = K: (%.9e, %.9e) ; elevator value (eps_xb <J> + <K_b><P_x>/<H>)/<H> = (%.9e, %.9e) ; '
               'comparator spin-omitted: (%.6e, %.6e) ; <J> = %.9f, <S> = %+d'
               % (r_[3][0], r_[3][1], vpred[0], vpred[1], rs[3][0], rs[3][1], Jexp, sgn))
pr('(C) time %.1fs' % (time.time() - t0))

# eta between bodies (same S, same motion state, common velocity), D1 = K
pr('(C) eta (D1 = K): |a_1 - a_2| / |a| between binding fractions, a = Xdd_E (vector), same S and common velocity:')
def acc_of(MB, mov, sgn, lab='K (Belinfante dipole)'):
    for row in rows:
        if row[0] == MB and row[1] == mov and row[2] == sgn: return row[5][lab][0], row[3]
for lab in ('K (Belinfante dipole)', '(1/2){H,X} (spin term omitted)', 'K0 (binding not gravitating)'):
    for mov in (False, True):
        for sgn in (+1, -1):
            for (A, B) in ((0.95, 0.85), (0.95, 0.70), (0.85, 0.70)):
                aA, VA = acc_of(A, mov, sgn, lab); aB, VB = acc_of(B, mov, sgn, lab)
                pr('    %-32s %s S=%+d f_B %.2f vs %.2f: eta = %.2e (|V_A - V_B| = %.1e)'
                   % (lab, 'moving' if mov else 'rest  ', sgn, 1 - A, 1 - B, n_(aA - aB)/n_(aA), n_(VA - VB)))
    for mov in (False, True):
        for MB in laws:
            aP, _ = acc_of(MB, mov, +1, lab); aM, _ = acc_of(MB, mov, -1, lab)
            pr('    %-32s %s f_B %.2f: spin eta S=+1 vs S=-1 = %.2e' % (lab, 'moving' if mov else 'rest  ', 1 - MB, n_(aP - aM)/n_(aP)))

# ---------------- (D) spin-orbit (lapse) and gravitomagnetic couplings ----------------
pr('(D) lapse spin-orbit: E_SO = <g.D1>(S=+1) - <g.D1>(S=-1), g = e_x, D1 = FD first moment of T00, bodies at X = 0 moving with P0 = M_b u;'
   ' elevator/BT value = <eps_xy P_y S f>(+) - (-) ; low-velocity form 2 * (1/2) eps_xy V_y:')
for MB, law in laws.items():
    P0 = tuple(MB*u)
    vals = {}
    for sgn in (+1, -1):
        psi, _ = packet(law, P0, sgn)
        D1 = -1j*dQ(lambda qx_, qy_: law.T00(psi, qx_, qy_), 0)
        vals[sgn] = (np.real(ip(psi, D1)), np.real(ip(psi, Pop(Sop(law.F(psi)), 1))), np.real(ip(psi, law.Knospin(psi, 0))),
                     np.real(ip(psi, Pop(psi, 1)))/np.real(ip(psi, law.H(psi))))
    dE = vals[1][0] - vals[-1][0]; pred = vals[1][1] - vals[-1][1]; dEns = vals[1][2] - vals[-1][2]
    pr('    M_b %.2f: E_SO(stress) = %.12e ; BT/elevator = %.12e ; ratio = %.12f ; low-velocity 2*(1/2)V_y = %.6e ; comparator (spin term omitted) E_SO = %.1e'
       % (MB, dE, pred, dE/pred, vals[1][3], dEns))
pr('(D) gravitomagnetic ratio (uniform rotation couples as -Omega J_T): <J_T> per unit <S> at rest, Belinfante vs dust:')
for MB, law in laws.items():
    for sgn in (+1, -1):
        psi, _ = packet(law, (0.0, 0.0), sgn)
        JT = (-1j)*(dQ(lambda qx_, qy_: law.T0b(psi, 1, qx_, qy_), 0) - dQ(lambda qx_, qy_: law.T0b(psi, 0, qx_, qy_), 1))
        JTd = (-1j)*(dQ(lambda qx_, qy_: law.T0b(psi, 1, qx_, qy_, curl=False), 0) - dQ(lambda qx_, qy_: law.T0b(psi, 0, qx_, qy_, curl=False), 1))
        Sx = np.real(ip(psi, Sop(psi)))
        pr('    M_b %.2f S=%+d: <S> = %.12f, <J> = %.12f, <J_T>_Belinfante = %.12f (ratio %.12f), <J_T>_dust = %.6f (ratio %.4f)'
           % (MB, sgn, Sx, np.real(ip(psi, law.J(psi))), np.real(ip(psi, JT)), np.real(ip(psi, JT))/Sx, np.real(ip(psi, JTd)), np.real(ip(psi, JTd))/Sx))
pr('total time %.1fs' % (time.time() - t0))
with open(__file__.replace('.py', '.out'), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
