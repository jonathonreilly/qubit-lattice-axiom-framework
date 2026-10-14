"""NF-1 (b), direct staggered check: the FULL 8x8 one-loop U(1) self-energy Sigma(P = 0) of the staggered field at reduced momentum 0
(all 8 offsets = the 2 tastes), computed with explicit 8x8 reduced-zone matrices (nf1_alg.py's Gamma_j, Gamma_eps), eigh per point,
on a full-BZ midpoint grid (photon momentum q in the full BZ; unfolded symbols H(p) = sum_A f_A(p) M_A with the incoming-momentum
convention, consistent with the folding P_m H(k') P_m = H(k' + pi m) for every operator used here; nf1_alg.py checks).
Formula (H-form; f3_mat.py docstring, F1's Psym vertex, Feynman gauge, A_0 exchange, critical m = 0):
  Sigma = < X(q) - sum_j V_j(0,q) X(q) V_j(q,0) + sum_j T_j(q)/(2 Om) >,  X = sum_n P_n sgn(E_n)/(2 Om (|E_n| + Om)),
  V_j Psym divided differences of H between cube corners, T_j = [H(q_j e_j) + H(-q_j e_j) - 2 H(0)]/(2 d_j^2).
Reported: m_eps = tr(Gamma_eps Sigma)/8 (the staggered additive mass, normalized like F1's tr(beta Sigma)/4), the norm of the rest,
the taste-breaking part ||U Sigma U^dag - Sigma_4 x 1_2|| (U from nf1_alg.py), and F3's reduced 4x4 dm_gen on the SAME grid.
Cases:
  A  staggered (r = 0), SF strain t (photon own flow, staggered band's own separable flow);
  B  control: F3's G1 dressing in staggered form, V = exp(i eps G1), G1 = sum_j sin k_j i Gamma_eps Gamma_j  (t = 0);
  C  control: explicit eps-breaking 'eps-Wilson' term  r_c sum_j sin^2(k_j) Gamma_eps  (pi-periodic: a legal staggered operator,
     same-sublattice, vanishes at all 8 corners), SF flow of its non-separable band (F1's flowF).
argv: N"""
import numpy as np, sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'flat'))
from f1_lib import Phot, flowG1, flowF, CPH
from f3_lib import dm_gen, rotate, fvec
from f3_dirac import herm_basis
from sublum import SymS

t00 = time.time()
N = int(sys.argv[1]) if len(sys.argv) > 1 else 24
BF = 0.909103708
A = SymS(BF); G = Phot(CPH)
G4 = np.load(os.path.join(HERE, 'nf1_gammas.npy')); Ud = np.load(os.path.join(HERE, 'nf1_dict.npy'))
Gam, Geps = G4[:3], G4[3]
IG = [1j*Geps @ Gam[j] for j in range(3)]


class FermC:
    """duck-typed for f1_lib.flowF / dm_sf: s = root odd box symbol (r = 0), 'W' = r_c sin^2 k (pi-periodic eps-Wilson)."""
    def __init__(self, rc, mflow=0.01):
        self.rc, self.mflow = rc, mflow
    def s(self, k): return A.s(k)
    def ds(self, k): return A.ds(k)
    def W(self, k): return self.rc*np.sin(k)**2
    def dW(self, k): return self.rc*np.sin(2*k)
    def p2(self, kx, ky, Wz):
        M = self.mflow + self.W(kx) + self.W(ky) + Wz
        return self.s(kx)*self.ds(kx) + M*self.dW(kx), self.s(ky)*self.ds(ky) + M*self.dW(ky)


def make_cM(F, t, eps=0.0):
    """(cx, cy, cz, M) of the staggered law at unfolded momentum k: SF flow (F1's flowF; separable when rc = 0), then G1 dressing."""
    def cM(kx, ky, kz):
        kx = kx + 0*ky + 0*kz; ky = ky + 0*kx + 0*kz; kz = kz + 0*kx + 0*ky
        Wz = F.W(kz)
        fx, fy = flowF(F, kx, ky, Wz, t, 4) if t != 0.0 else (kx, ky)
        c = (F.s(fx), F.s(fy), F.s(kz)); M = F.W(fx) + F.W(fy) + Wz
        if eps != 0.0:
            c, M = rotate(c, M, fvec('G1', kx, ky, kz), eps)
        return c[0], c[1], c[2], M
    return cM


def H8(cM, kx, ky, kz):
    cx, cy, cz, M = cM(np.asarray(kx, float), np.asarray(ky, float), np.asarray(kz, float))
    return (np.multiply.outer(cx, Gam[0]) + np.multiply.outer(cy, Gam[1]) + np.multiply.outer(cz, Gam[2])
            + np.multiply.outer(M, Geps))


def sigma8(cM, dx, dy, dz, x, Hf=None):
    n = len(x); w = 1.0/n
    z = 0*x
    H8_ = H8
    if Hf is not None:
        H8_ = lambda c_, a_, b_, d_: Hf(a_, b_, d_)
    H0 = H8_(cM, 0.0, 0.0, 0.0)
    Hx, Hy, Hz = H8_(cM, x, z, z), H8_(cM, z, x, z), H8_(cM, z, z, x)
    Hxm, Hym, Hzm = H8_(cM, -x, z, z), H8_(cM, z, -x, z), H8_(cM, z, z, -x)
    T = [(Hx + Hxm - 2*H0)/(2*dx[:, None, None]**2), (Hy + Hym - 2*H0)/(2*dy[:, None, None]**2), (Hz + Hzm - 2*H0)/(2*dz[:, None, None]**2)]
    Hxy = H8_(cM, x[:, None], x[None, :], 0*x[:, None])
    tot = np.zeros((8, 8), complex)
    for iz in range(n):
        zz = x[iz]
        Hq = H8_(cM, x[:, None], x[None, :], zz + 0*x[:, None])
        Hxz = H8_(cM, x, z, zz + z)[:, None]; Hyz = H8_(cM, z, x, zz + z)[None, :]
        Hz1 = H8_(cM, 0.0, 0.0, zz)
        Cx = Hx[:, None]; Cy = Hy[None, :]
        dX = dx[:, None, None, None]; dY = dy[None, :, None, None]; dZ = dz[iz]
        Vx = (2*(Cx - H0) + (Hxy - Cy) + (Hxz - Hz1) + 2*(Hq - Hyz))/6/dX
        Vy = (2*(Cy - H0) + (Hxy - Cx) + (Hyz - Hz1) + 2*(Hq - Hxz))/6/dY
        Vz = (2*(Hz1 - H0) + (Hxz - Cx) + (Hyz - Cy) + 2*(Hq - Hxy))/6/dZ
        Om = np.sqrt(dx[:, None]**2 + dy[None, :]**2 + dz[iz]**2)
        E, U = np.linalg.eigh(Hq)
        X = U @ ((np.sign(E)/(2*Om[..., None]*(np.abs(E) + Om[..., None])))[..., None]*U.conj().swapaxes(-1, -2))
        val = X - sum(V @ X @ V for V in (Vx, Vy, Vz))
        tad = (T[0][:, None] + T[1][None, :] + T[2][iz])/(2*Om[..., None, None])
        tot += (val + tad).sum(axis=(0, 1))*w**3
    return tot


def report(lab, S, red):
    meps = np.real(np.trace(Geps @ S))/8
    rest = S - meps*Geps
    St = Ud @ S @ Ud.conj().T
    S4 = 0.5*(St[0::2, 0::2] + St[1::2, 1::2])          # partial trace over the taste factor (kron(A, 1_2) layout)
    tb = np.linalg.norm(St - np.kron(S4, np.eye(2)))
    comps = {nm: np.real(np.trace(B @ S4))/4 for nm, B in herm_basis()}
    big = sorted(comps.items(), key=lambda kv: -abs(kv[1]))[:3]
    print('  %-34s m_eps %+.12e | 4x4 reduced (same grid) %+.12e | diff %.1e | ||rest|| %.1e | taste-breaking %.1e | top: %s'
          % (lab, meps, red, meps - red, np.linalg.norm(rest), tb, ', '.join('%s %+.1e' % kv for kv in big)), flush=True)
    return meps


x = -np.pi + (np.arange(N) + 0.5)*2*np.pi/N; wv = np.full(N, 1.0/N)
def phot(t):
    if t == 0.0:
        d = G.d(x); return d, d, d
    # Gph's archived h/dh are EVEN extensions (valid on q >= 0 only, as F1/F3 integrate over the octant); the SF flow of the odd
    # gauge symbol is odd, so flow |q| and use evenness of d^2 (only d^2 and d-quadratic vertex products enter).
    return G.d(flowG1(G, np.abs(x), +1, t, 4)), G.d(flowG1(G, np.abs(x), -1, t, 4)), G.d(x)

print('NF-1 direct 8x8 staggered self-energy at P = 0, full-BZ midpoint N = %d (%d points); per e^2' % (N, N**3), flush=True)
F0 = FermC(0.0)
print(' A: staggered (r = 0) under SF strain')
for t in (0.0, 0.1, -0.1, 0.2):
    cM = make_cM(F0, t); dx, dy, dz = phot(t)
    report('A t=%+.2f' % t, sigma8(cM, dx, dy, dz, x), dm_gen(cM, dx, dy, dz, x, wv))
print(' B: control, G1 dressing (t = 0), eps = t^2 a')
d0 = phot(0.0); vals = {}
for e in (1e-3, -1e-3, 0.05):
    cM = make_cM(F0, 0.0, eps=e)
    vals[e] = report('B eps=%+.3f' % e, sigma8(cM, *d0, x), dm_gen(cM, *d0, x, wv))
print('   L = d m_eps/d eps (central, eps = +-1e-3) = %+.6e per e^2  (Hess_t = 2 a L)' % ((vals[1e-3] - vals[-1e-3])/2e-3))
print(' C: control, eps-Wilson r_c sum sin^2 k_j Gamma_eps (critical mass fixed at t = 0)')
for rc in (0.1, 0.3):
    Fc = FermC(rc); out = {}
    for t in (0.0, 0.1, 0.2):
        cM = make_cM(Fc, t); dx, dy, dz = phot(t)
        out[t] = report('C rc=%.1f t=%+.2f' % (rc, t), sigma8(cM, dx, dy, dz, x), dm_gen(cM, dx, dy, dz, x, wv))
    h1 = 2*(out[0.1] - out[0.0])/0.1**2; h2 = 2*(out[0.2] - out[0.0])/0.2**2
    print('   rc=%.1f: coarse Hess_t (d=0.1) %+.4e (d=0.2) %+.4e  [coarse grid; converged values in nf1_conv]' % (rc, h1, h2))
print(' D: eps-RESPECTING dressing (check of the mechanism): G_c = sum_{j<k} i Gamma_j Gamma_k sin k_j sin k_k ([G_c, Gamma_eps] = 0, even in k)')
pairs = ((0, 1), (1, 2), (0, 2))
def Hdress(t, e):
    cM = make_cM(F0, t)
    def Hf(kx, ky, kz):
        kx = np.asarray(kx, float); ky = np.asarray(ky, float); kz = np.asarray(kz, float)
        kx, ky, kz = np.broadcast_arrays(kx, ky, kz)
        H = H8(cM, kx, ky, kz)
        kk = (kx, ky, kz)
        Gc = sum(np.multiply.outer(np.sin(kk[a])*np.sin(kk[b]), 1j*Gam[a] @ Gam[b]) for a, b in pairs)
        lam, U = np.linalg.eigh(Gc)
        V = U @ (np.exp(1j*e*lam)[..., None]*U.conj().swapaxes(-1, -2))
        return V @ H @ V.conj().swapaxes(-1, -2)
    return Hf
print('   max |[G_c, Gamma_eps]| = %.1e' % max(np.abs(1j*Gam[a] @ Gam[b] @ Geps - Geps @ (1j*Gam[a] @ Gam[b])).max() for a, b in pairs))
for t, e in ((0.0, 0.05), (0.1, 0.05), (0.2, 0.3)):
    dx, dy, dz = phot(t)
    S = sigma8(None, dx, dy, dz, x, Hf=Hdress(t, e))
    report('D t=%+.2f eps=%.2f' % (t, e), S, float('nan'))
print('time %.0f s' % (time.time() - t00))
