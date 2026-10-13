"""R18-13: off-axis extension of R17-12's VWa photon TT vertex (stated here), and its Xi(n, e) for any lattice direction.

Base: R17-12's index-placed Maxwell stress T_ij = c_i c_j [E_iE_j + B_iB_j - delta_ij (E^2 + B^2)/2] in the rotated frame,
per-leg symbols c(k_l) = d'(|k_l|), pair (k1, k2), k1 + k2 = q on R17-9's grid (representatives in (-pi, pi)).
GEOMETRIC EXTENSION (VWa-geo; stated): each bilinear term keeps the half-integer offsets of its two (averaged) fields, read
from the lattice geometry (E_a at a/2, B_a at the two other half-axes; averaging along an index moves a field to the
site along that index only). Every half-integer offset along axis l is placed by the SAME two-offset stencil as on the
axis, P(s_l) = (1-a) cos(s_l/2) + a cos(3 s_l/2), s_l = k1_l + k2_l (R17-12 convention). Integer offsets: no stencil.
  i != j:  E_i(1)E_j(2): c1_i c2_j            (both fields averaged along their own index -> site)
           B_i(1)B_j(2): c1_j c2_i P(s_k)     (k = third axis)
  i == j:  E_i^2: +1/2 c1_i c2_i ;  E_a^2 (a != i): -1/2 c1_i c2_i P(s_a)
           B_i^2: +1/2 c1_i c2_i P(s_j) P(s_k) ;  B_a^2 (a != i): -1/2 c1_i c2_i P(s_third(a,i))
  On q || z this reproduces r1712_lib.vertex('VWa') term by term (checked numerically below).
OWN-DIRECTION PLACEMENT DATA (new law data, stated): component T_ii multiplied by u_d(s_i), T_ij (i != j) by u_o(s_i) u_o(s_j),
  u(s) = (1 - w) + w cos(s) (symmetric integer-offset stencil, weights 1-w at 0 and w/2 at +-1; u(0) = 1, so the forward
  (Lemma F) value is unchanged; O(s^2) coefficient -w/2). On an axis q || z the TT components (xx, yy, xy) see u(0) = 1:
  these data do not enter the axial rows."""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
from photon import kgrid, crossmat, photonGw

r2, r6 = np.sqrt(2.0), np.sqrt(6.0)
def _pol():   # R17-4 / R9-9 normalization e:e = 2 (the photon pair matrix carries the 1/2)
    P = {}
    P['T2g'] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], float)
    P['Eg'] = np.diag([1.0, -1.0, 0.0])
    a = np.array([1, -1, 0])/r2; b = np.array([0, 0, 1.0])
    P['face1'] = np.outer(a, a) - np.outer(b, b); P['face2'] = np.outer(a, b) + np.outer(b, a)
    b2 = np.array([1, 1, -2])/r6
    P['body'] = np.outer(a, a) - np.outer(b2, b2)
    P['xz'] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], float)
    return P
POL = _pol()
DIRS = {'T2g': (0, 0, 1), 'Eg': (0, 0, 1), 'xz': (0, 1, 0), 'face1': (1, 1, 0), 'face2': (1, 1, 0), 'body': (1, 1, 1)}

def vertex_geo(e, c1, c2, s, a, wd=0.0, wo=0.0):
    """e: 3x3 symmetric; c1, c2: (..., 3); s: (..., 3) leg sums. returns ME, MB (..., 3, 3)."""
    P = (1.0 - a)*np.cos(0.5*s) + a*np.cos(1.5*s)            # (..., 3) half-integer placement per axis
    ud = (1.0 - wd) + wd*np.cos(s); uo = (1.0 - wo) + wo*np.cos(s)
    sh = c1.shape[:-1]
    ME = np.zeros(sh + (3, 3)); MB = np.zeros(sh + (3, 3))
    for i in range(3):
        for j in range(3):
            if e[i, j] == 0: continue
            if i != j:
                k = 3 - i - j
                U = e[i, j]*uo[..., i]*uo[..., j]
                ME[..., i, j] += U*c1[..., i]*c2[..., j]
                MB[..., i, j] += U*c1[..., j]*c2[..., i]*P[..., k]
            else:
                U = e[i, i]*ud[..., i]
                cc = c1[..., i]*c2[..., i]
                oth = [x for x in range(3) if x != i]
                ME[..., i, i] += 0.5*U*cc
                MB[..., i, i] += 0.5*U*cc*P[..., oth[0]]*P[..., oth[1]]
                for aa in oth:
                    third = 3 - aa - i
                    ME[..., aa, aa] += -0.5*U*cc*P[..., aa]
                    MB[..., aa, aa] += -0.5*U*cc*P[..., third]
    return ME, MB

def pair_W(law, N, shift, e, a, settings):
    """sum_pol |amp|^2 for each (wd, wo) in settings, and E = w1 + w2; pair (k, q - k), q = 2 pi shift / N."""
    k = kgrid(N); s = law.sig(k); c = law.c(k)
    j = np.arange(N)
    j2 = [(shift[d] - j - 1) % N for d in range(3)]
    Y, Z = np.meshgrid(j, j, indexing='ij')
    outW = [np.empty((N, N, N)) for _ in settings]; outE = np.empty((N, N, N))
    for ix in range(N):
        X_ = np.full_like(Y, ix)
        I1 = [X_, Y, Z]; I2 = [j2[0][X_], j2[1][Y], j2[2][Z]]
        s1 = np.stack([s[I] for I in I1], -1); s2 = np.stack([s[I] for I in I2], -1)
        c1 = np.stack([c[I] for I in I1], -1); c2 = np.stack([c[I] for I in I2], -1)
        ssum = np.stack([k[I1[d]] + k[I2[d]] for d in range(3)], -1)
        w1 = np.sqrt((s1*s1).sum(-1)); w2 = np.sqrt((s2*s2).sum(-1)); rw = np.sqrt(w1*w2)
        X1 = crossmat(s1); X2 = crossmat(s2)
        P1 = np.eye(3) - s1[..., :, None]*s1[..., None, :]/(w1*w1)[..., None, None]
        P2 = np.eye(3) - s2[..., :, None]*s2[..., None, :]/(w2*w2)[..., None, None]
        for t, (wd, wo) in enumerate(settings):
            ME, MB = vertex_geo(e, c1, c2, ssum, a, wd, wo)
            Bp = np.einsum('...ji,...jk,...kl->...il', X1, MB, X2)/rw[..., None, None]
            Nm = 0.5*(rw[..., None, None]*ME + Bp)
            outW[t][ix] = np.einsum('...ij,...jk,...kl,...il->...', P1, Nm, P2, Nm)
        outE[ix] = w1 + w2
    return outW, outE

def xi_geo(law, N, row, a, settings=((0.0, 0.0),), shifts=(1, 2)):
    e = POL[row]; d = np.array(DIRS[row])
    W0, E0 = pair_W(law, N, (0, 0, 0), e, a, settings)
    res = []
    D = {}
    for n in shifts:
        W, E = pair_W(law, N, tuple(n*d), e, a, settings); D[n] = W
        D[n] = (W, E)
    q1 = 2*np.pi*shifts[0]*np.sqrt(float(d @ d))/N; r = shifts[1]/shifts[0]
    for t in range(len(settings)):
        beta = -np.mean(W0[t]/E0**3); Pi0 = -np.mean(W0[t]/E0)
        Dn = {n: -np.mean(D[n][0][t]/D[n][1]) - Pi0 for n in shifts}
        alpha = (r**4*Dn[shifts[0]] - Dn[shifts[1]])/((r**4 - r**2)*q1**2)
        res.append(alpha + beta)
    return np.array(res)

if __name__ == '__main__':
    bg, fw, a = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    Ns = [int(v) for v in sys.argv[4].split(',')]
    rows = sys.argv[5].split(',') if len(sys.argv) > 5 else ['T2g', 'Eg', 'xz', 'face1', 'face2', 'body']
    law = photonGw(bg, fw*(np.pi - bg))
    sets = ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0))
    for N in Ns:
        out = {}
        for row in rows:
            v = xi_geo(law, N, row, a, sets)
            out[row] = v
            print('gammaGw(%.6f, fw=%.3f) a=%+.6f N=%d %s: Xi(0,0) %+.9e | dXi/dwd %+.9e | dXi/dwo %+.9e' % (bg, fw, a, N, row, v[0], v[1] - v[0], v[2] - v[0]), flush=True)
        if all(r in out for r in ('Eg', 'T2g', 'face1', 'face2')):
            X = {r: out[r][0] for r in out}
            print('   N=%d per vector: face2-T2g %+.6e | face1-(3Eg+T2g)/4 %+.6e' % (N, X['face2'] - X['T2g'], X['face1'] - (3*X['Eg'] + X['T2g'])/4), flush=True)
            if 'body' in out:
                for t in range(3):
                    Y = {r: out[r][t] for r in out}
                    print('   setting %d: O_h relation resid %+.2e' % (t, Y['body'] - (8*Y['face1'] + 4*Y['face2'] - 3*Y['Eg'])/9), flush=True)
            if 'xz' in out: print('   C4 control xz(q||y) - T2g(q||z) %+.2e' % (out['xz'][0] - out['T2g'][0]), flush=True)
