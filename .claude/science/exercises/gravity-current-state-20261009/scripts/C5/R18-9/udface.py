"""R18-9 (c), Dirac part: brute-force finite-q Xi for the UD vertex with q along ANY lattice direction and ANY TT polarization,
on a uniform midpoint grid (generalizes R18-5's xiud.brute, which is q || z only). Midpoint prescription G(k) (as R18-5).
UD: T_ij = (1/2)(p_j d_i h + p_i d_j h), d_i h = s'_i alpha_i + W'_i beta, p_i = s_i s'_i + M W'_i.
Polarization e (symmetric 3x3, normalized as R18-5: T2g <-> e:T = T_xy, Eg <-> (T_xx - T_yy)/2).
Pair term t = (Nc/4)[|G|^2 (1 + ca.cb/(Ea Eb)) - 2 (ca.G)(cb.G)/(Ea Eb)], Pi(q) = <2t/(Ea+Eb)>, alpha = -dPi/d|q|^2 (Richardson),
beta = -<t0/(4E^3)>, t0 = (Nc/2)(|G|^2 - (c.G)^2/E^2).  Xi = alpha + beta."""
import sys, numpy as np
sys.path.insert(0, '../arch18')
from content3 import D1q
r2 = np.sqrt(2.0)
POL = {}
e = np.zeros((3, 3)); e[0, 1] = e[1, 0] = 0.5; POL['T2g'] = e
e = np.zeros((3, 3)); e[0, 0] = 0.5; e[1, 1] = -0.5; POL['Eg'] = e
a = np.array([1, -1, 0])/r2; b = np.array([0, 0, 1.0])
POL['face2'] = 0.5*(np.outer(a, b) + np.outer(b, a)); POL['face1'] = 0.5*(np.outer(a, a) - np.outer(b, b))
e = np.zeros((3, 3)); e[0, 2] = e[2, 0] = 0.5; POL['xz'] = e          # q || y control (C4 image of T2g)
def tables3(law, N, m):
    kk = (np.arange(N) + 0.5)*2*np.pi/N - np.pi
    S, Sp, Spp, W, Wp, Wpp = law.tables(kk)
    return S, Sp, W, Wp
def fields(S, Sp, W, Wp, m, sh):
    """c (4 comps) on the grid shifted by integer vector sh (np.roll), plus s', W' arrays per axis."""
    ax = []
    for d in range(3):
        shape = [1, 1, 1]; shape[d] = -1
        ax.append([np.roll(A, sh[d]).reshape(shape) for A in (S, Sp, W, Wp)])
    M = m + ax[0][2] + ax[1][2] + ax[2][2]
    c = [ax[0][0] + 0*M, ax[1][0] + 0*M, ax[2][0] + 0*M, M]
    return c, ax, M
def Gface(e, ax, M):
    s = [ax[d][0] for d in range(3)]; sp = [ax[d][1] for d in range(3)]; wp = [ax[d][3] for d in range(3)]
    p = [s[d]*sp[d] + M*wp[d] for d in range(3)]
    G = [0*M, 0*M, 0*M, 0*M]
    for i in range(3):
        for j in range(3):
            if e[i, j] == 0: continue
            # T_ij = 1/2 (p_j d_i h + p_i d_j h)
            G[i] = G[i] + e[i, j]*0.5*p[j]*sp[i]; G[3] = G[3] + e[i, j]*0.5*p[j]*wp[i]
            G[j] = G[j] + e[i, j]*0.5*p[i]*sp[j]; G[3] = G[3] + e[i, j]*0.5*p[i]*wp[j]
    return G
def xi(law, m, pol, qdir, N, shifts=(1, 2, 4), Nc=4):
    S, Sp, W, Wp = tables3(law, N, m); e = POL[pol]; qdir = np.array(qdir)
    c0, ax0, M0 = fields(S, Sp, W, Wp, m, (0, 0, 0)); G = Gface(e, ax0, M0)
    G2 = sum(x*x for x in G); E2 = sum(x*x for x in c0); g = sum(x*y for x, y in zip(c0, G))
    beta = -np.mean((Nc/2)*(G2 - g*g/E2)/(4*E2**1.5))
    vals = []
    for n in (0,) + tuple(shifts):
        ca, _, _ = fields(S, Sp, W, Wp, m, tuple(n*qdir)); cb, _, _ = fields(S, Sp, W, Wp, m, tuple(-n*qdir))
        Ea = np.sqrt(sum(x*x for x in ca)); Eb = np.sqrt(sum(x*x for x in cb))
        caG = sum(x*y for x, y in zip(ca, G)); cbG = sum(x*y for x, y in zip(cb, G)); cab = sum(x*y for x, y in zip(ca, cb))
        t = (Nc/4)*(G2*(1 + cab/(Ea*Eb)) - 2*caG*cbG/(Ea*Eb))
        vals.append(np.mean(2*t/(Ea + Eb)))
    q2 = lambda n: (4*np.pi*n/N)**2*float(qdir @ qdir)
    d = [-(v - vals[0])/q2(n) for n, v in zip(shifts, vals[1:])]
    r1 = (4*d[0] - d[1])/3; r2_ = (4*d[1] - d[2])/3; alpha = (16*r1 - r2_)/15
    return alpha + beta, alpha, beta
if __name__ == '__main__':
    bf, r, m = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]); law = D1q(bf, r)
    for N in [int(v) for v in sys.argv[4].split(',')]:
        out = {}
        for pol, qd in (('T2g', (0, 0, 1)), ('Eg', (0, 0, 1)), ('xz', (0, 1, 0)), ('face1', (1, 1, 0)), ('face2', (1, 1, 0))):
            out[pol] = xi(law, m, pol, qd, N)[0]
        print('D1(%.6f, %.6f) m=%g N=%d UD per field: T2g %+.6e Eg %+.6e | C4 control xz(q||y) %+.6e | face1 %+.6e face2 %+.6e | face2-T2g %+.3e | face1-(3Eg+T2g)/4 %+.3e'
              % (bf, r, m, N, out['T2g'], out['Eg'], out['xz'], out['face1'], out['face2'], out['face2'] - out['T2g'], out['face1'] - (3*out['Eg'] + out['T2g'])/4), flush=True)
