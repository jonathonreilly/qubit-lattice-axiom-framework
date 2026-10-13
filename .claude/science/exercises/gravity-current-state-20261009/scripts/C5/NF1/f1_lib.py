"""F1 library: one-loop U(1) ADDITIVE mass of the root's Wilson-type D1 Dirac edge under the registered SF strain flow.

SF (R9-2 / R19-15 Lemma H / R16-13 / R18-5): each band is strained by its OWN momentum-space flow
    Phi_t = time-1 map of  v = (t/2) h.p ,  p = grad(E^2/2),  unit E_g strain h = diag(1, -1, 0)   (SF units: t).
  Dirac D1(b, r):  E^2 = sum s(k_j)^2 + M^2,  M = m_flow + sum W(k_j)  ->  p_j = s s' + M W'   (non-separable through M).
  photon Gph(c):   w^2 = sum d(q_j)^2,  d = SymG(c).h  ->  p_j = d d'   (separable; per-axis 1D flows).
Strained kinetic operator (the operator lift of SF; UD = its generator at t -> 0, rR18-5 sec. 0 item 3):
    D_t(k) = D(Phi^F_t(k)) = sum_j i g_j s([Phi^F_t k]_j) + m + sum_j W([Phi^F_t k]_j)
    photon symbols  d_{t,j}(q) = d([Phi^g_t q]_j)  (Feynman gauge propagator delta_mu nu /(Q0^2 + sum_j d_{t,j}^2 + lam^2)).
Minimal coupling of the NON-separable D_t w.r.t. the strained photon's gauge symmetry (a_j -> a_j + d_{t,j} chi):
    generalized-link (divided-difference) Wilson lines along axis-ordered paths (R8-5/R13-7/R19-34 per-axis convention),
    averaged uniformly over the 6 axis orderings ('Psym': the unique cubic-covariant, hermitian choice in that family).
    At P = 0 the x-vertex is V_x(0,q) = [2 D_x(0) + D_x(y) + D_x(z) + 2 D_x(yz)] / (6 d_{t,x}),  D_x(B) = D(B + q_x e_x) - D(B),
    B in {0, q_y e_y, q_z e_z, q_y e_y + q_z e_z}; cyclic for y, z.  Ward: sum_j d_{t,j} V_j(0,q) = D_t(q) - D_t(0) (telescoping).
    The diagonal seagull at photon momenta (q, -q) is path-INDEPENDENT (start phases cancel): T_jj = [D(q_j e_j) + D(-q_j e_j) - 2 D(0)]/(2 d_j^2).
Mass part (Euclidean, P = 0, critical m = 0 in the propagator):
    dm/e^2 = < sum_j W(phi_j(q_j))/d_j^2 /(2 Om) > + < [ M + sum_j ( (sum_l a_jl a'_jl - b_j b'_j) M - b_j (a'_j.c) - b'_j (a_j.c) ) ] /(2 E Om (E+Om)) >
    with V_j(0,q) = i g.a_j + b_j (left), V_j(q,0) = i g.a'_j + b'_j (right); Psym: a' = a, b' = b  (reduces to r1934_lib at t = 0).
Integration over [0, pi]^3 (integrand even in each q_j; the flows preserve the positive octant) with R19-34's composite GL panels.
"""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'flat'))
from dirac import D1
from sublum import SymG, SymS
from r1934_lib import panels


class Ferm:
    def __init__(self, b, r, mflow=0.01):
        self.L = D1(b, r); self.b, self.r, self.mflow = b, r, mflow
    def s(self, k): return self.L.S(k)
    def ds(self, k): return self.L.dS(k)
    def W(self, k): return self.L.W(k)
    def dW(self, k): return self.L.dW(k)
    def p2(self, kx, ky, Wz):
        """(p_x, p_y) of the 4-comp band at (kx, ky, kz) given W(kz)."""
        M = self.mflow + self.W(kx) + self.W(ky) + Wz
        return self.s(kx)*self.ds(kx) + M*self.dW(kx), self.s(ky)*self.ds(ky) + M*self.dW(ky)


class Phot:
    def __init__(self, c):
        self.G = SymG(c); self.c = c
    def d(self, q): return self.G.h(q)
    def p1(self, q): return self.G.h(q)*self.G.dh(q)


def rk4(f, y, n):
    """time-1 map of dy/dtau = f(y), n RK4 steps; y tuple of arrays."""
    h = 1.0/n
    for _ in range(n):
        k1 = f(y)
        k2 = f(tuple(a + 0.5*h*b for a, b in zip(y, k1)))
        k3 = f(tuple(a + 0.5*h*b for a, b in zip(y, k2)))
        k4 = f(tuple(a + h*b for a, b in zip(y, k3)))
        y = tuple(a + h/6*(b1 + 2*b2 + 2*b3 + b4) for a, b1, b2, b3, b4 in zip(y, k1, k2, k3, k4))
    return y


def flowF(F, kx, ky, Wz, t, n=6):
    """SF flow of the Dirac band, E_g: dk_x = +(t/2) p_x, dk_y = -(t/2) p_y, k_z fixed."""
    if t == 0.0:
        return kx + 0*ky + 0*Wz, ky + 0*kx + 0*Wz
    def f(y):
        px, py = F.p2(y[0], y[1], Wz)
        return 0.5*t*px, -0.5*t*py
    return rk4(f, (kx + 0*ky + 0*Wz, ky + 0*kx + 0*Wz), n)


def flowG1(G, q, sgn, t, n=6):
    """1D SF flow of the separable photon along one axis (sgn = +1 for x, -1 for y, 0 for z)."""
    if t == 0.0 or sgn == 0:
        return np.array(q, float)
    def f(y):
        return (0.5*sgn*t*G.p1(y[0]),)
    return rk4(f, (np.array(q, float),), n)[0]


class Grid:
    def __init__(self, breaks, n, hmax=0.25):
        self.x, self.w = panels(breaks, n, hmax)


def dm_sf(F, G, grid, t, mprop=0.0, lam=0.0, path='Psym', photflow='own', fermflow='own', nrk=6, parts=False, chunk=None, extra=None):
    """one-loop additive mass dm/e^2 at P = 0 on the SF-strained law (see module doc).
    photflow: 'own' (photon's own separable flow), 'none' (photon unstrained), 'ferm' (photon symbols d([Phi^F q]_j): flowed like the fermion).
    fermflow: 'own' (Dirac band's own flow), 'phot' (fermion flowed by the photon's separable flow), 'none'.
    path: 'Psym' (6-ordering average, hermitian) or a tuple ordering like ('x','y','z') (single ordering; NOT hermitian: sensitivity only)."""
    x, w = grid.x, grid.w
    N = len(x)
    if chunk is None:                      # memory bound: ~750 B per (N^2 x chunk) point -> <= ~0.45 GB of temporaries
        chunk = max(1, int(2.5e5/(N*N)))
    s, W = F.s, F.W
    # ---- fermion flows ----
    def fflow(kx, ky, Wz):
        if fermflow == 'own':
            return flowF(F, kx, ky, Wz, t, nrk)
        if fermflow == 'phot':
            return flowG1(G, kx + 0*ky + 0*Wz, +1, t, nrk), flowG1(G, ky + 0*kx + 0*Wz, -1, t, nrk)
        if fermflow == 'none':
            return kx + 0*ky + 0*Wz, ky + 0*kx + 0*Wz
        raise ValueError(fermflow)
    W0 = 0.0
    ax, _ = fflow(x, 0*x, W0)              # (q_x,0,0) -> (ax,0,0)
    _, ay = fflow(0*x, x, W0)              # (0,q_y,0) -> (0,ay,0)
    PX0, PY0 = fflow(x[:, None], x[None, :], W0)   # (q_x,q_y,0) plane
    # ---- photon symbols ----
    if photflow == 'own':
        dxv = G.d(flowG1(G, x, +1, t, nrk)); dyv = G.d(flowG1(G, x, -1, t, nrk))
    elif photflow in ('none', 'ferm'):
        dxv = G.d(x); dyv = G.d(x)
    dzv = G.d(x)
    sx_ax, W_ax = s(ax), W(ax)
    sy_ay, W_ay = s(ay), W(ay)
    sz_all, Wz_all = s(x), W(x)
    s_PX0, s_PY0, W_PX0, W_PY0 = s(PX0), s(PY0), W(PX0), W(PY0)
    tad = 0.0; loop = 0.0
    for i0 in range(0, N, chunk):
        iz = np.arange(i0, min(N, i0 + chunk))
        z = x[iz][None, None, :]
        Wz = Wz_all[iz][None, None, :]; sz = sz_all[iz][None, None, :]
        X = x[:, None, None]; Y = x[None, :, None]
        FX, FY = fflow(X, Y, Wz)                      # full points q
        BX, _ = fflow(X, 0*X, Wz)                     # (q_x,0,q_z)
        _, BY = fflow(0*Y, Y, Wz)                     # (0,q_y,q_z)
        # D at corners: tuples (cx, cy, cz, M) with M excluding mprop (added below where needed)
        Z0 = 0.0
        D_0 = (Z0, Z0, Z0, Z0)
        D_x = (sx_ax[:, None, None], Z0, Z0, W_ax[:, None, None])
        D_y = (Z0, sy_ay[None, :, None], Z0, W_ay[None, :, None])
        D_z = (Z0, Z0, sz, Wz)
        D_xy = (s_PX0[:, :, None], s_PY0[:, :, None], Z0, (W_PX0 + W_PY0)[:, :, None])
        D_xz = (s(BX), Z0, sz, W(BX) + Wz)
        D_yz = (Z0, s(BY), sz, W(BY) + Wz)
        D_q = (s(FX), s(FY), sz, W(FX) + W(FY) + Wz)
        def diff(A, B):
            return tuple(a - b for a, b in zip(A, B))
        # leg differences (after - before) for each axis and base
        Lx = {'0': diff(D_x, D_0), 'y': diff(D_xy, D_y), 'z': diff(D_xz, D_z), 'yz': diff(D_q, D_yz)}
        Ly = {'0': diff(D_y, D_0), 'x': diff(D_xy, D_x), 'z': diff(D_yz, D_z), 'xz': diff(D_q, D_xz)}
        Lz = {'0': diff(D_z, D_0), 'x': diff(D_xz, D_x), 'y': diff(D_yz, D_y), 'xy': diff(D_q, D_xy)}
        def avg(dct, wts):
            tot = sum(wts.values())
            return tuple(sum(wts[k]*dct[k][c] for k in wts)/tot for c in range(4))
        if path == 'Psym':
            VL = [avg(Lx, {'0': 2, 'y': 1, 'z': 1, 'yz': 2}), avg(Ly, {'0': 2, 'x': 1, 'z': 1, 'xz': 2}),
                  avg(Lz, {'0': 2, 'x': 1, 'y': 1, 'xy': 2})]
            VR = VL
        else:
            def legs(order):
                done = ''
                out = {}
                for ax_ in order:
                    key = ''.join(sorted(done)) or '0'
                    out[ax_] = {'x': Lx, 'y': Ly, 'z': Lz}[ax_][key]
                    done += ax_
                return [out['x'], out['y'], out['z']]
            VL = legs(path); VR = legs(tuple(reversed(path)))
        dd = [dxv[:, None, None], dyv[None, :, None], dzv[iz][None, None, :]]
        if photflow == 'ferm':
            dd = [G.d(FX), G.d(FY), dzv[iz][None, None, :] + 0*FX]
        # strained photon dispersion
        Om = np.sqrt(dd[0]**2 + dd[1]**2 + dd[2]**2 + lam*lam)
        c = D_q[:3]; M = mprop + D_q[3]
        E = np.sqrt(c[0]**2 + c[1]**2 + c[2]**2 + M*M)
        num = M
        for j in range(3):
            a = [VL[j][l]/dd[j] for l in range(3)]; b = VL[j][3]/dd[j]
            a2 = [VR[j][l]/dd[j] for l in range(3)]; b2 = VR[j][3]/dd[j]
            num = num + (a[0]*a2[0] + a[1]*a2[1] + a[2]*a2[2] - b*b2)*M - b*(a2[0]*c[0] + a2[1]*c[1] + a2[2]*c[2]) \
                - b2*(a[0]*c[0] + a[1]*c[1] + a[2]*c[2])
        ww = w[:, None, None]*w[None, :, None]*w[iz][None, None, :]
        if extra is not None:
            ww = ww*extra(x[:, None, None], x[None, :, None], x[iz][None, None, :])
        tadj = D_x[3]/dd[0]**2 + D_y[3]/dd[1]**2 + D_z[3]/dd[2]**2
        tad += float((ww*tadj/(2*Om)).sum())
        loop += float((ww*num/(2*E*Om*(E + Om))).sum())
    if parts:
        return tad + loop, tad, loop
    return tad + loop


def hess(f, d):
    f0 = f(0.0); fp, fm = f(d), f(-d); fp2, fm2 = f(2*d), f(-2*d)
    h1 = (fp - 2*f0 + fm)/d**2; h2 = (fp2 - 2*f0 + fm2)/(2*d)**2
    return dict(f0=f0, grad=(fp - fm)/(2*d), odd=(fp - fm), h1=h1, h2=h2, rich=(4*h1 - h2)/3)


ROOT = (0.909103708, 0.555604226)      # R18-9 refined root Dirac edge (vR18-9 item 2)
ROOT0 = (0.915438682, 0.568280847)     # R19-11 0+ root
CPH = 2.9435                           # Gph(2.9435)
