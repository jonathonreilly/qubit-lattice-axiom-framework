"""F5 library: F1's SF-strained one-loop additive mass, generalized to an ARBITRARY uniform symmetric strain h (3x3).

Same law as F1 (f1_lib.py docstring; unmodified F1 copy alongside), only the strain direction is general:
  SF flow of every band: Phi_t = time-1 map of v = (t/2) h.p, p = grad(E^2/2)  (t in SF units; h = diag(1,-1,0) is F1's E_g,
  h = e_x e_y + e_y e_x is the unit T2g strain with the same Frobenius norm, h = e_z e_z is the rank-one 'nn' strain).
  Dirac D1(b, r):  p_j = s s'(k_j) + M W'(k_j),  M = mflow + sum W(k_j)   (3D ODE; non-separable through M)
  photon Gph(c):   p_j = d d'(q_j)  (3D ODE; separable only for diagonal h)
  D_t(k) = D(Phi^F_t k);  photon symbols d_{t,j}(q) = d([Phi^g_t q]_j);  Feynman gauge.
  Psym generalized links (axis-ordered, 6 orderings averaged) -> V_x(0,q) = [2 L_x(0) + L_x(y) + L_x(z) + 2 L_x(yz)]/(6 d_{t,x}(q)),
  L_x(B) = D_t(B + q_x e_x) - D_t(B), B in {0, q_y e_y, q_z e_z, q_y e_y + q_z e_z}; cyclic.  V(q,0) = V(0,q) for any odd
  flow (path-reversal symmetry of Psym; d_{t,j} odd).  Diagonal seagull M-part: M_t(q_j e_j) (M_t even, flow odd).
  dm/e^2 = < sum_j M_t(q_j e_j)/d_{t,j}^2/(2 Om) > + < [M + sum_j ((a_j.a_j - b_j^2) M - 2 b_j (a_j.c))]/(2 E Om (E+Om)) >
  (F1's reduced formula with a' = a, b' = b; M includes the propagator mass mprop).
Quadrature: per-axis composite GL node sets, each normalized to an AVERAGE over its interval; the caller chooses the
  interval per axis consistent with the symmetry of h (octant for diagonal h; x in [-pi, pi] for T2g, see f5_t2g.py).
"""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arch'))
sys.path.insert(0, HERE)
from dirac import D1
from sublum import SymG
from r1934_lib import panels


def panels_sym(breaks, n, hmax=0.25):
    """nodes on [-pi, pi] = mirror of r1934_lib.panels on [0, pi]; weights average over [-pi, pi]."""
    x, w = panels(breaks, n, hmax)
    return np.concatenate([-x[::-1], x]), np.concatenate([w[::-1], w])/2.0


class Ferm:
    def __init__(self, b, r, mflow=0.01):
        self.L = D1(b, r); self.b, self.r, self.mflow = b, r, mflow
    def s(self, k): return self.L.S(k)
    def ds(self, k): return self.L.dS(k)
    def W(self, k): return self.L.W(k)
    def dW(self, k): return self.L.dW(k)
    def p3(self, kx, ky, kz):
        M = self.mflow + self.W(kx) + self.W(ky) + self.W(kz)
        return (self.s(kx)*self.ds(kx) + M*self.dW(kx), self.s(ky)*self.ds(ky) + M*self.dW(ky),
                self.s(kz)*self.ds(kz) + M*self.dW(kz))


class Phot:
    def __init__(self, c):
        self.G = SymG(c); self.c = c
    def d(self, q): return self.G.h(q)      # even in q; only d^2 and (vertex/d)^2 products enter the P = 0 formula
    def p3(self, qx, qy, qz):
        G = self.G   # p_j = d d'(q_j) as an ODD function: SymG.h is h(|q|) (even), so use dg/2 = sign(q) h dh
        return 0.5*G.dg(qx), 0.5*G.dg(qy), 0.5*G.dg(qz)


def rk4(f, y, n):
    hh = 1.0/n
    for _ in range(n):
        k1 = f(y)
        k2 = f(tuple(a + 0.5*hh*b for a, b in zip(y, k1)))
        k3 = f(tuple(a + 0.5*hh*b for a, b in zip(y, k2)))
        k4 = f(tuple(a + hh*b for a, b in zip(y, k3)))
        y = tuple(a + hh/6*(b1 + 2*b2 + 2*b3 + b4) for a, b1, b2, b3, b4 in zip(y, k1, k2, k3, k4))
    return y


def flow3(band, h, kx, ky, kz, t, n=2):
    """time-1 map of dk/dtau = (t/2) h.p(k) for a band with p3(); broadcasts kx, ky, kz."""
    kx, ky, kz = np.broadcast_arrays(np.asarray(kx, float), np.asarray(ky, float), np.asarray(kz, float))
    kx, ky, kz = kx.copy(), ky.copy(), kz.copy()
    if t == 0.0:
        return kx, ky, kz
    H = np.asarray(h, float)
    def f(y):
        p = band.p3(*y)
        return tuple(0.5*t*(H[i, 0]*p[0] + H[i, 1]*p[1] + H[i, 2]*p[2]) for i in range(3))
    return rk4(f, (kx, ky, kz), n)


def dm_gen(F, G, h, xs, ys, zs, t, mprop=0.0, lam=0.0, nrk=2, parts=False, chunk=None, ferm_on=True, phot_on=True):
    """one-loop additive mass dm/e^2 at P = 0 on the SF-strained law with strain direction h (see module doc).
    xs, ys, zs: (nodes, weights) per axis; weights average over the chosen interval."""
    x, wx = xs; y, wy = ys; z, wz = zs
    Nx, Ny = len(x), len(y)
    if chunk is None:
        chunk = max(1, int(1.2e5/(Nx*Ny)))
    tf = t if ferm_on else 0.0
    tg = t if phot_on else 0.0
    s, W = F.s, F.W
    def DF(kx, ky, kz):
        a, b, c = flow3(F, h, kx, ky, kz, tf, nrk)
        return (s(a), s(b), s(c), W(a) + W(b) + W(c))
    # axis corners (1D) and the xy plane (2D)
    Dx = DF(x, 0*x, 0*x); Dy = DF(0*y, y, 0*y)
    Dxy = DF(x[:, None], y[None, :], 0.0)
    tad = 0.0; loop = 0.0
    for i0 in range(0, len(z), chunk):
        iz = np.arange(i0, min(len(z), i0 + chunk))
        Zc = z[iz]
        X = x[:, None, None]; Y = y[None, :, None]; Z = Zc[None, None, :]
        Dz = DF(0*Zc, 0*Zc, Zc)
        Dz = tuple(c[None, None, :] for c in Dz)
        Dxz = DF(X, 0*Y, Z); Dyz = DF(0*X, Y, Z); Dq = DF(X, Y, Z)
        D0 = (0.0, 0.0, 0.0, 0.0)
        Dx3 = tuple(c[:, None, None] for c in Dx); Dy3 = tuple(c[None, :, None] for c in Dy)
        Dxy3 = tuple(c[:, :, None] for c in Dxy)
        def diff(A, B):
            return tuple(a - b for a, b in zip(A, B))
        def avg4(A, B, C, Dd):   # (2 A + B + C + 2 Dd)/6
            return tuple((2*a + b + c + 2*d)/6.0 for a, b, c, d in zip(A, B, C, Dd))
        Vx = avg4(diff(Dx3, D0), diff(Dxy3, Dy3), diff(Dxz, Dz), diff(Dq, Dyz))
        Vy = avg4(diff(Dy3, D0), diff(Dxy3, Dx3), diff(Dyz, Dz), diff(Dq, Dxz))
        Vz = avg4(diff(Dz, D0), diff(Dxz, Dx3), diff(Dyz, Dy3), diff(Dq, Dxy3))
        gx, gy, gz = flow3(G, h, X, Y, Z, tg, nrk)
        dd = [G.d(gx), G.d(gy), G.d(gz)]
        Om = np.sqrt(dd[0]**2 + dd[1]**2 + dd[2]**2 + lam*lam)
        c = Dq[:3]; M = mprop + Dq[3]
        E = np.sqrt(c[0]**2 + c[1]**2 + c[2]**2 + M*M)
        num = M
        for j, V in enumerate((Vx, Vy, Vz)):
            a = [V[l]/dd[j] for l in range(3)]; b = V[3]/dd[j]
            num = num + (a[0]*a[0] + a[1]*a[1] + a[2]*a[2] - b*b)*M - 2*b*(a[0]*c[0] + a[1]*c[1] + a[2]*c[2])
        ww = wx[:, None, None]*wy[None, :, None]*wz[iz][None, None, :]
        tadj = Dx3[3]/dd[0]**2 + Dy3[3]/dd[1]**2 + Dz[3]/dd[2]**2
        tad += float((ww*tadj/(2*Om)).sum())
        loop += float((ww*num/(2*E*Om*(E + Om))).sum())
    if parts:
        return tad + loop, tad, loop
    return tad + loop


def mkbreaks(b, cph, mph):
    return [b, np.pi - b] + [cph + i*(np.pi - cph)/mph for i in range(mph)]


H_EG = np.diag([1.0, -1.0, 0.0])
H_T2 = np.array([[0, 1.0, 0], [1.0, 0, 0], [0, 0, 0]])
H_NN = np.diag([0.0, 0.0, 1.0])
H_ISO = np.eye(3)
ROOT = (0.909103708, 0.555604226)
ROOT0 = (0.915438682, 0.568280847)
CPH = 2.9435
