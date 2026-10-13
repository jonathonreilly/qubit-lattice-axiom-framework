"""R18-13: UD Dirac graviton-cone shift Xi(n, e) for ANY unit direction n and ANY polarization e, pointwise form on
R16-13's composite Gauss-Legendre nodes (resolves m = 0.01, unlike R18-9's uniform brute grid).

Generalizes R18-5's xiud.pointwise (axial, ' = d/dk_z) by replacing ' with the directional derivative D = n.grad
(the derivation in xiud is a 1D Taylor expansion of the pair (k - q/2, k + q/2), q = s n, with G at the midpoint k,
so it is direction-agnostic). For the separable D1 law, c = (S(kx), S(ky), S(kz), M), M = m + sum W(k_l):
  Dc   = (n_x S'(kx), n_y S'(ky), n_z S'(kz), sum n_l W'(k_l)),  D^2 c = (n_x^2 S'', ..., sum n_l^2 W''(k_l)).
UD vertex (R18-5): T_ij = (1/2)(p_j d_i h + p_i d_j h), d_i h = S'_i alpha_i + W'_i beta, p_i = S_i S'_i + M W'_i.
Polarization normalization as R18-5 / udface.py: T2g <-> e_xy = e_yx = 1/2; Eg <-> diag(1/2, -1/2, 0);
face1 = (aa - bb)/2, face2 = (ab + ba)/2, a = (1,-1,0)/sqrt2, b = z;  body = (aa - bb)/2, a = (1,-1,0)/sqrt2, b = (1,1,-2)/sqrt6.
The midpoint prescription G(k) is the stated O(q^2) placement (P-R18-5c), applied to every direction."""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
import dfam
from content3 import D1q

r2, r6 = np.sqrt(2.0), np.sqrt(6.0)
def _pol():
    P = {}
    e = np.zeros((3, 3)); e[0, 1] = e[1, 0] = 0.5; P['T2g'] = e
    P['Eg'] = np.diag([0.5, -0.5, 0.0])
    a = np.array([1, -1, 0])/r2; b = np.array([0, 0, 1.0])
    P['face1'] = 0.5*(np.outer(a, a) - np.outer(b, b)); P['face2'] = 0.5*(np.outer(a, b) + np.outer(b, a))
    b2 = np.array([1, 1, -2])/r6
    P['body'] = 0.5*(np.outer(a, a) - np.outer(b2, b2))
    e = np.zeros((3, 3)); e[0, 2] = e[2, 0] = 0.5; P['xz'] = e
    return P
POL = _pol()
DIRS = {'T2g': (0, 0, 1), 'Eg': (0, 0, 1), 'xz': (0, 1, 0), 'face1': (1, 1, 0), 'face2': (1, 1, 0), 'body': (1, 1, 1)}

def xi_dirac(law, m, rows=('T2g', 'Eg', 'face1', 'face2', 'body', 'xz'), npan=3, ngl=8, Nc=4):
    k, wq = dfam.gl_nodes(law.breaks(), npan, ngl)
    S, Sp, Spp, W, Wp, Wpp = law.tables(k)
    out = {r: 0.0 for r in rows}
    ny = len(k)
    # (ky, kz) arrays
    Sy, Spy, Sppy, Wy, Wpy, Wppy = (A[:, None] + 0*k[None, :] for A in (S, Sp, Spp, W, Wp, Wpp))
    Sz, Spz, Sppz, Wz, Wpz, Wppz = (A[None, :] + 0*k[:, None] for A in (S, Sp, Spp, W, Wp, Wpp))
    wyz = wq[:, None]*wq[None, :]
    for ix in range(len(k)):
        Sx, Spx, Sppx, Wx, Wpx, Wppx = S[ix], Sp[ix], Spp[ix], W[ix], Wp[ix], Wpp[ix]
        M = m + Wx + Wy + Wz
        c = [Sx + 0*M, Sy, Sz, M]
        E2 = sum(x*x for x in c); E = np.sqrt(E2)
        s_ = [Sx + 0*M, Sy, Sz]; sp_ = [Spx + 0*M, Spy, Spz]; wp_ = [Wpx + 0*M, Wpy, Wpz]
        spp_ = [Sppx + 0*M, Sppy, Sppz]; wpp_ = [Wppx + 0*M, Wppy, Wppz]
        p = [s_[d]*sp_[d] + M*wp_[d] for d in range(3)]
        for row in rows:
            e = POL[row]; n = np.array(DIRS[row], float); n = n/np.linalg.norm(n)
            # vertex G (4 comps) at the midpoint k
            G = [0*M, 0*M, 0*M, 0*M]
            for i in range(3):
                for j in range(3):
                    if e[i, j] == 0: continue
                    G[i] = G[i] + e[i, j]*0.5*p[j]*sp_[i]; G[3] = G[3] + e[i, j]*0.5*p[j]*wp_[i]
                    G[j] = G[j] + e[i, j]*0.5*p[i]*sp_[j]; G[3] = G[3] + e[i, j]*0.5*p[i]*wp_[j]
            cp = [n[0]*sp_[0], n[1]*sp_[1], n[2]*sp_[2], n[0]*wp_[0] + n[1]*wp_[1] + n[2]*wp_[2]]
            cpp = [n[0]**2*spp_[0], n[1]**2*spp_[1], n[2]**2*spp_[2], n[0]**2*wpp_[0] + n[1]**2*wpp_[1] + n[2]**2*wpp_[2]]
            cc1 = sum(a*b for a, b in zip(c, cp)); c1c1 = sum(a*a for a in cp); cc2 = sum(a*b for a, b in zip(c, cpp))
            Ep = cc1/E; Epp = (c1c1 + cc2 - Ep**2)/E
            G2 = sum(a*a for a in G); g = sum(a*b for a, b in zip(c, G))
            g1 = sum(a*b for a, b in zip(cp, G)); g2 = sum(a*b for a, b in zip(cpp, G))
            t0 = (Nc/2)*(G2 - g*g/E2)
            al = 0.25*(t0*Epp/(2*E2) + (Nc/2)*(G2*(c1c1 - Ep**2) + g*g2 - g1**2 - g*g*(E*Epp - Ep**2)/E2)/E**3)
            be = -t0/(4*E**3)
            out[row] += wq[ix]*float(np.sum(wyz*(al + be)))
    return out

def relation(X):   # R17-4's O_h relation, body = (8 face1 + 4 face2 - 3 Eg)/9 (normalization-uniform)
    return X['body'] - (8*X['face1'] + 4*X['face2'] - 3*X['Eg'])/9

if __name__ == '__main__':
    bf, r, m = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    qs = [tuple(int(v) for v in s.split(',')) for s in sys.argv[4].split(';')]
    law = D1q(bf, r)
    for q in qs:
        X = xi_dirac(law, m, npan=q[0], ngl=q[1])
        print('D1(%.6f, %.6f) m=%g GL%s UD per field: ' % (bf, r, m, q) + ' '.join('%s %+.8e' % (kk, v) for kk, v in X.items()), flush=True)
        print('   face2-T2g %+.4e | face1-(3Eg+T2g)/4 %+.4e | C4 xz-T2g %+.2e | O_h relation resid %+.2e'
              % (X['face2'] - X['T2g'], X['face1'] - (3*X['Eg'] + X['T2g'])/4, X['xz'] - X['T2g'], relation(X)), flush=True)
