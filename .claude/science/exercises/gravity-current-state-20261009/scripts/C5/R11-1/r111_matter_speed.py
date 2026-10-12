"""C5 R11-1 (b): one-loop dressed speed of box scalar matter under box-graviton loops.

PRESCRIPTION (stated; "dD-M"):
 matter  : real scalar, Euclidean S = 1/2 [ (d0 phi)^2 + sum_j (D_j phi)^2 + m^2 phi^2 ],  D_j symbol i s(k_j), s odd, s^2 = u
           profiles L (s = s_L, R7-1 literal) and G (s = sign(k) sqrt(u_G), R8-2 gapped) from R9-9 (r99_profiles, B = 2.0).
 coupling: minimal metric coupling sqrt(g) g^{mu nu} D_mu phi D_nu phi with g = delta + kappa h (R9-9's member M extended to
           every component).  phi(p) -> phi(p') + h(q), p' = p - q:
             V^{mu nu} = ph_mu ph'_nu + ph_nu ph'_mu - delta_{mu nu} (ph.ph' + m^2),   ph = (p0, s(p_j)),  ph' = (r, s(p'_j)).
           In the matter box this is the continuum vertex.  The O(h^2) seagull is ultralocal in h: its tadpole is
           P_{abcd} * int D, an O(4)-covariant tensor contracted with ph.ph -> no Lorentz violation (proved in report).
 graviton: R9-9's box graviton symbol d(q) = rho q + (1-rho) 2 sin(q/2) (C1 = 1.0, C2 = 2.5), de Donder-type propagator
           P_{mu nu rho sigma} / (q0^2 + |d(q)|^2 + lam^2),  P = (dd + dd - dd)/2, lam = IR regulator (extrapolated -> 0).
 exchange: Pi(p0, p) = -(kappa^2/4) int_q int dr/2pi  V.P.V / ((q0^2 + a^2)(r^2 + b^2)),  r = p0 - q0,
           a^2 = |d(q)|^2 + lam^2, b^2 = eps(p - q)^2.  r-integrals in closed form (r111_q0int.py).
 dispersion: Gamma = p0^2 + eps^2(p) + Pi;  on shell (first order)  omega^2 = eps^2(p) + Pi(i E_p, p),
           so  c_m^2 - 1 = d Pi_on / d p_x^2 at p = 0  (E_p = sqrt(m^2 + p^2) in the box).  kappa^2 = 32 pi G = 4 kappa_lat.
 Ward diagnostic: the pure-gauge propagator direction zeta * (d_mu d_rho delta_{nu sigma} + 3 perms)/D^2 adds
           Pi_zeta = -(kappa^2/4) * 4 zeta int W.W / (D^2 (r^2 + b^2)),  W^nu = d_mu V^{mu nu}, d = (q0, d(q)).
           With an exact Ward identity its on-shell LV coefficient vanishes (continuum: W = -p^nu (p'^2+m^2) on shell);
           a nonzero value measures the gauge dependence of the dD-M number.
 Also printed: the off-shell Euclidean dimension-4 coefficient (alpha_E - beta_E at p = 0), for comparison.
Output: J = dPi_on/dp^2 per kappa^2 = 1 (so c_m^2 - 1 = 4 kappa_lat J).
"""
import numpy as np, sys, time, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from r99_profiles_copy import profile, plateau, wrap, s_L, B as MBOX
from r111_q0int import get_funcs
F, _ = get_funcs()
WANTZ = bool(int(os.environ.get('R111_ZETA', '0')))
C1, C2 = 1.0, 2.5
T0 = time.time()

def dsym(q):
    q = wrap(q); rr = plateau(q, C1, C2)
    return rr * q + (1 - rr) * 2 * np.sin(q / 2)

def s_of(name, k):
    if name == 'L':
        return s_L(k)
    if name == 'G':
        u = profile('G', k)[0]
        return np.sign(wrap(k)) * np.sqrt(np.maximum(u, 0))
    if name == 'NN':
        return 2 * np.sin(wrap(k) / 2)
    raise ValueError

def poly_coeffs(fun, deg):
    """coefficients c_n of a polynomial in r of degree deg, from exact evaluation at deg+1 nodes."""
    nodes = np.arange(deg + 1) - deg // 2
    vals = [fun(float(t)) for t in nodes]
    Vm = np.vander(nodes.astype(float), deg + 1, increasing=True)
    Vi = np.linalg.inv(Vm)
    return [sum(Vi[n, i] * vals[i] for i in range(deg + 1)) for n in range(deg + 1)]

def Pi(name, m, N, lam, p0, px, chunk=8, want_zeta=True):
    k1 = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    QY, QZ = np.meshgrid(k1, k1, indexing='ij')
    dy, dz = dsym(QY), dsym(QZ)
    sy, sz = s_of(name, -QY), s_of(name, -QZ)              # s(p'_j) with p'_j = -q_j  (p_y = p_z = 0)
    uy, uz = sy ** 2, sz ** 2
    spx = s_of(name, np.array(px))
    tot, totz = 0.0 + 0j, 0.0 + 0j
    for i0 in range(0, N, chunk):
        qx = k1[i0:i0 + chunk][:, None, None]
        dx = dsym(qx)
        sxp = s_of(name, px - qx)                       # s(p'_x)
        a = np.sqrt(dx ** 2 + dy[None] ** 2 + dz[None] ** 2 + lam ** 2)
        b = np.sqrt(m * m + sxp ** 2 + uy[None] + uz[None])
        S1 = sxp + 0 * a; S2 = sy[None] + 0 * a; S3 = sz[None] + 0 * a
        def Vmat(rv):
            ph = [p0, spx, 0.0, 0.0]
            pp = [rv, S1, S2, S3]
            Q = p0 * rv + spx * S1 + m * m
            V = [[ph[mu] * pp[nu] + ph[nu] * pp[mu] - (Q if mu == nu else 0) for nu in range(4)] for mu in range(4)]
            return V
        def VPV(rv):
            V = Vmat(rv)
            s2 = sum(V[mu][nu] * V[mu][nu] for mu in range(4) for nu in range(4))
            tr = sum(V[mu][mu] for mu in range(4))
            return s2 - 0.5 * tr * tr
        c = poly_coeffs(VPV, 2)
        val = sum(c[n] * F[(1, n)](p0, a, b) for n in range(3))
        tot += np.sum(val)
        if want_zeta:
            def WW(rv):
                V = Vmat(rv)
                dvec = [p0 - rv, dx + 0 * a, dy[None] + 0 * a, dz[None] + 0 * a]
                W = [sum(dvec[mu] * V[mu][nu] for mu in range(4)) for nu in range(4)]
                return sum(w * w for w in W)
            w = poly_coeffs(WW, 4)
            totz += np.sum(sum(w[n] * F[(2, n)](p0, a, b) for n in range(5)))
    V3 = N ** 3
    return -0.25 * tot / V3, -1.0 * totz / V3

def Eon(name, m, px):
    u = profile(name, np.array([px]))[0][0]
    return np.sqrt(m * m + u)

def lv_onshell(name, m, N, lam):
    h = 2 * np.pi / N
    f = {}; fz = {}
    for n in (0, 1, 2, 4):
        px = n * h
        P, Pz = Pi(name, m, N, lam, 1j * Eon(name, m, px), px, want_zeta=WANTZ)
        f[n], fz[n] = P, Pz
    def rich(g):
        d = {n: (g[n] - g[0]) / (n * h) ** 2 for n in (1, 2, 4)}
        r1 = (4 * d[1] - d[2]) / 3; r2 = (4 * d[2] - d[4]) / 3
        return (16 * r1 - r2) / 15
    return rich(f), rich(fz), f[0]

def lv_offshell(name, m, N, lam):
    h = 2 * np.pi / N
    g = {}; gt = {}
    for n in (0, 1, 2, 4):
        g[n] = Pi(name, m, N, lam, 0.0, n * h, want_zeta=False)[0]
        gt[n] = Pi(name, m, N, lam, n * h, 0.0, want_zeta=False)[0]
    def rich(G):
        d = {n: (G[n] - G[0]) / (n * h) ** 2 for n in (1, 2, 4)}
        r1 = (4 * d[1] - d[2]) / 3; r2 = (4 * d[2] - d[4]) / 3
        return (16 * r1 - r2) / 15
    return rich(g) - rich(gt)

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'main'
    U = 16 * np.pi ** 2
    if mode == 'main':
        names = sys.argv[2].split(',') if len(sys.argv) > 2 else ['G', 'L']
        masses = [float(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else [1.0, 0.3]
        Ns = [int(x) for x in sys.argv[4].split(',')] if len(sys.argv) > 4 else [48, 64]
        lams = [float(x) for x in sys.argv[5].split(',')] if len(sys.argv) > 5 else [0.4, 0.2]
        print('profile m N lam | J_on = dPi_on/dp^2 (kappa^2=1) [imag] | J_zeta (Ward diag, per zeta) | Pi_on(0) | J_off(Euclid alpha-beta)')
        for name in names:
            for m in masses:
                for N in Ns:
                    for lam in lams:
                        J, Jz, P0v = lv_onshell(name, m, N, lam)
                        Joff = lv_offshell(name, m, N, lam) if N <= 64 else np.nan
                        print('%s m=%.2f N=%3d lam=%.3f | J_on=%+.6e [%.0e] | J_zeta=%+.6e | Pi_on(0)=%+.5e | J_off=%+.6e   (%.0fs)'
                              % (name, m, N, lam, J.real, abs(J.imag), Jz.real, P0v.real, np.real(Joff), time.time() - T0), flush=True)
