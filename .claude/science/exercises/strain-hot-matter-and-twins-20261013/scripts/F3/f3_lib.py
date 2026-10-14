"""F3 library: F1's one-loop additive mass (f1_lib.dm_sf formula, Psym vertex, Feynman gauge, P = 0, critical m = 0) for a GENERAL
Dirac-form operator D(k) = i g.c(k) + M(k) supplied as a callable at the 8 cube corners, plus the dressing used in F3:

  D-H dressing (Hamiltonian conjugation H -> V H V^dag, V = exp(i eps G), H = g0 D):  for the fully symmetric generators
  G_f = sum_j i beta alpha_j f_j(k) = -sum_j g_j f_j(k)  the dressed operator stays Dirac-form and is an exact k-dependent rotation
  of the 4-vector (c, M):  u = fhat.c,  (u, M) -> (u cos th + M sin th, M cos th - u sin th),  th = 2 eps |f|,  c_perp fixed
  (generator: d/d eps (c, M) = 2 (f M, -f.c); checked against expm in f3_mat.py).
  Symmetric generators by range (f3_sym.out):  G1: f_j = sin k_j (NN);  G2: f_j = sin k_j (cos k_l + cos k_m) (NNN);
  G3: sin k_j cos k_l cos k_m (cube corner, beyond NNN);  G4: sin 2k_j (distance 2, beyond NNN).
Formula (f1_lib.py:17-18; reduced form proved/checked by F1 against explicit gammas, rechecked here in f3_mat.py):
  dm/e^2 = < sum_j T_j /(2 Om) > + < [ M + sum_j ( (a_j.a_j - b_j^2) M - 2 b_j (a_j.c) ) ] / (2 E Om (E + Om)) >,
  T_j = ([M(q_j e_j) + M(-q_j e_j)]/2 - M(0)) / d_j^2 ,  V_j(0,q) = i g.a_j + b_j  (Psym, hermitian: a' = a, b' = b).
"""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'arch'))
from f1_lib import Ferm, Phot, flowF, flowG1, Grid, ROOT, ROOT0, CPH, hess
from r1934_lib import panels


def fvec(name, kx, ky, kz):
    """symmetric generator vector fields f(k) (T1u, odd)."""
    if name == 'G1':
        return np.sin(kx) + 0*ky + 0*kz, np.sin(ky) + 0*kx + 0*kz, np.sin(kz) + 0*kx + 0*ky
    if name == 'G2':
        cx, cy, cz = np.cos(kx), np.cos(ky), np.cos(kz)
        return np.sin(kx)*(cy + cz), np.sin(ky)*(cz + cx), np.sin(kz)*(cx + cy)
    if name == 'G3':
        cx, cy, cz = np.cos(kx), np.cos(ky), np.cos(kz)
        return np.sin(kx)*cy*cz, np.sin(ky)*cz*cx, np.sin(kz)*cx*cy
    if name == 'G4':
        return np.sin(2*kx) + 0*ky + 0*kz, np.sin(2*ky) + 0*kx + 0*kz, np.sin(2*kz) + 0*kx + 0*ky
    raise ValueError(name)


def rotate(c, M, f, eps):
    """exact D-H dressing by V = exp(i eps G_f): rotation of (c, M) by th = 2 eps |f| in the (fhat, M) plane."""
    if eps == 0.0:
        return c, M
    fn = np.sqrt(f[0]**2 + f[1]**2 + f[2]**2)
    safe = np.where(fn > 0, fn, 1.0)
    fh = [fj/safe for fj in f]
    u = fh[0]*c[0] + fh[1]*c[1] + fh[2]*c[2]
    th = 2*eps*fn
    ct, st = np.cos(th), np.sin(th)
    u2 = u*ct + M*st; M2 = M*ct - u*st
    c2 = tuple(c[j] + (u2 - u)*fh[j] for j in range(3))
    return c2, M2


def make_cM(F, t=0.0, dress=None, a=0.0, nrk=2, eps=None):
    """cM(kx, ky, kz) -> (cx, cy, cz, M) for the SF-strained root Dirac operator D(Phi_t k) (F1's flow; M without m_prop),
    then the D-H dressing V_t = exp(i t^2 a G_f(k)) (f at the unflowed k).  eps overrides t^2 a (t = 0 linear-response runs)."""
    def cM(kx, ky, kz):
        kx = kx + 0*ky + 0*kz; ky = ky + 0*kx + 0*kz; kz = kz + 0*kx + 0*ky
        Wz = F.W(kz)
        if t != 0.0:
            fx_, fy_ = flowF(F, kx, ky, Wz, t, nrk)
        else:
            fx_, fy_ = kx, ky
        c = (F.s(fx_), F.s(fy_), F.s(kz))
        M = F.W(fx_) + F.W(fy_) + Wz
        e = (t*t*a) if eps is None else eps
        if dress is not None and e != 0.0:
            c, M = rotate(c, M, fvec(dress, kx, ky, kz), e)
        return c[0], c[1], c[2], M
    return cM


def dm_gen(cM, dx, dy, dz, x, w, parts=False, chunk=None, lam=0.0):
    """F1's mass formula for a general Dirac-form D given by cM at the cube corners; photon symbols dx, dy, dz on the node set x
    (already strained if wanted).  x, w: 1D nodes and BZ-average weights per axis (octant [0,pi] with panels, or full-BZ midpoint)."""
    N = len(x)
    if chunk is None:
        chunk = max(1, int(6e4/(N*N)))
    Z = np.zeros(1)
    D0 = np.array(cM(Z, Z, Z)).reshape(4)
    # axis points (and their negatives for the seagull)
    Ax = np.array(cM(x, 0*x, 0*x)); Ay = np.array(cM(0*x, x, 0*x)); Az = np.array(cM(0*x, 0*x, x))
    Mxm = cM(-x, 0*x, 0*x)[3]; Mym = cM(0*x, -x, 0*x)[3]; Mzm = cM(0*x, 0*x, -x)[3]
    Pxy = np.array(cM(x[:, None], x[None, :], 0.0*x[:, None]))           # (4, N, N)
    Tx = ((Ax[3] + Mxm)/2 - D0[3])/dx**2; Ty = ((Ay[3] + Mym)/2 - D0[3])/dy**2; Tz = ((Az[3] + Mzm)/2 - D0[3])/dz**2
    tad = 0.0; loop = 0.0
    for i0 in range(0, N, chunk):
        iz = np.arange(i0, min(N, i0 + chunk))
        X = x[:, None, None]; Y = x[None, :, None]; Zs = x[iz][None, None, :]
        Cq = np.array(cM(X, Y, Zs))                                      # (4, N, N, c)
        Cxz = np.array(cM(X, 0*Y, Zs))                                   # (4, N, 1, c)
        Cyz = np.array(cM(0*X, Y, Zs))                                   # (4, 1, N, c)
        Cx = Ax[:, :, None, None]; Cy = Ay[:, None, :, None]; Cz = Az[:, iz][:, None, None, :]
        Cxy = Pxy[:, :, :, None]; C0 = D0[:, None, None, None]
        Vx = (2*(Cx - C0) + (Cxy - Cy) + (Cxz - Cz) + 2*(Cq - Cyz))/6/dx[None, :, None, None]
        Vy = (2*(Cy - C0) + (Cxy - Cx) + (Cyz - Cz) + 2*(Cq - Cxz))/6/dy[None, None, :, None]
        Vz = (2*(Cz - C0) + (Cxz - Cx) + (Cyz - Cy) + 2*(Cq - Cxy))/6/dz[iz][None, None, None, :]
        Om = np.sqrt(dx[:, None, None]**2 + dy[None, :, None]**2 + dz[iz][None, None, :]**2 + lam*lam)
        c = Cq[:3]; M = Cq[3]
        E = np.sqrt(c[0]**2 + c[1]**2 + c[2]**2 + M*M)
        num = M.copy()
        for V in (Vx, Vy, Vz):
            a = V[:3]; b = V[3]
            num += (a[0]**2 + a[1]**2 + a[2]**2 - b*b)*M - 2*b*(a[0]*c[0] + a[1]*c[1] + a[2]*c[2])
        ww = w[:, None, None]*w[None, :, None]*w[iz][None, None, :]
        tadj = Tx[:, None, None] + Ty[None, :, None] + Tz[iz][None, None, :]
        tad += float((ww*tadj/(2*Om)).sum())
        loop += float((ww*num/(2*E*Om*(E + Om))).sum())
        del Cq, Cxz, Cyz, Vx, Vy, Vz, Om, c, M, E, num, ww, tadj
    if parts:
        return tad + loop, tad, loop
    return tad + loop


def photon_syms(G, x, t=0.0, nrk=2):
    if t == 0.0:
        d = G.d(x); return d, d, d
    return G.d(flowG1(G, x, +1, t, nrk)), G.d(flowG1(G, x, -1, t, nrk)), G.d(x)


def mkgrid(b, n, hm, mph):
    """F1's grid (f1_root.py:9-11)."""
    br = [b, np.pi - b] + [CPH + i*(np.pi - CPH)/mph for i in range(mph)]
    return Grid(br, n, hm)


def lin_resp(F, G, grid, name, d=1e-3, **kw):
    """L = d/d eps dm[ Rot(eps f) D ] at eps = 0, t = 0 (central differences d, 2d + Richardson); returns (L_d, L_2d, L_rich, dm0)."""
    dx, dy, dz = photon_syms(G, grid.x)
    f = lambda e: dm_gen(make_cM(F, 0.0, name, eps=e), dx, dy, dz, grid.x, grid.w, **kw)
    f0 = f(0.0); p1, m1, p2, m2 = f(d), f(-d), f(2*d), f(-2*d)
    L1 = (p1 - m1)/(2*d); L2 = (p2 - m2)/(4*d)
    return L1, L2, (4*L1 - L2)/3, f0
