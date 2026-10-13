"""R19-29: the A_1 face-block identities for one vector field with R18-13's VWa-geo vertex (root a, root own-direction data),
time components by P1 (R19-5), on R18-13's grid convention: pair (k, q - k), q = 2 pi shift / N exactly on the grid.
Gram(A, B) = tr(P1 N_A P2 N_B^T) (vwface.pair_W generalized to A != B; N linear in the polarization tensor);
Pi_AB(omega) = -(1/2) < Gram(A_a, B_a)/(E - omega) + Gram(A_b, B_b)/(E + omega) >  (vwface: Pi(0) = -<W/E>, beta = -<W/E^3>).
A_a, A_b = e_sp +- sym(q x w)/E + e_00 q x q / E^2.  usage: python r1929_photon.py N n1,n2,...  (shifts n*(1,1,0))"""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'arch18'))
from photon import kgrid, crossmat, photonGw
import vwface_copy as V
from a1lib import emb, E1F, n3, gauge
t0 = time.time()
N = int(sys.argv[1]); shifts = [int(v) for v in sys.argv[2].split(',')]
root = np.load(os.path.join(HERE, 'root_refR18-9.npy')); bg, fw, a = root[5], root[6], root[3]
wd, wo = (float(sys.argv[3]), float(sys.argv[4])) if len(sys.argv) > 4 else (-1.171554, -0.195418)
law = photonGw(bg, fw*(np.pi - bg))
print('photon gammaGw(%.4f, fw=%g), VWa-geo a=%+.6f, own-direction (w_d, w_o) = (%+.6f, %+.6f), N=%d' % (bg, fw, a, wd, wo, N))
k = kgrid(N); sg = law.sig(k); cc = law.c(k); j = np.arange(N)
def gram_block(shift, omega, pols):
    qv = 2*np.pi*np.array(shift, float)/N
    j2 = [(shift[d] - j - 1) % N for d in range(3)]
    Y, Z = np.meshgrid(j, j, indexing='ij')
    base = {}
    sym = lambda A: 0.5*(A + A.T)
    tens = {'qq': np.outer(qv, qv)}
    for i, e in enumerate(pols):
        tens['sp%d' % i] = e[1:, 1:].copy()
        w = np.array([e[0, 1+jj] + e[1+jj, 0] for jj in range(3)])
        tens['qw%d' % i] = sym(np.outer(qv, w))
    n = len(pols); P = np.zeros((n, n))
    for ix in range(N):
        X_ = np.full_like(Y, ix)
        I1 = [X_, Y, Z]; I2 = [j2[0][X_], j2[1][Y], j2[2][Z]]
        s1 = np.stack([sg[I] for I in I1], -1); s2 = np.stack([sg[I] for I in I2], -1)
        c1 = np.stack([cc[I] for I in I1], -1); c2 = np.stack([cc[I] for I in I2], -1)
        ssum = np.stack([k[I1[d]] + k[I2[d]] for d in range(3)], -1)
        w1 = np.sqrt((s1*s1).sum(-1)); w2 = np.sqrt((s2*s2).sum(-1)); rw = np.sqrt(w1*w2); E = w1 + w2
        X1 = crossmat(s1); X2 = crossmat(s2)
        P1 = np.eye(3) - s1[..., :, None]*s1[..., None, :]/(w1*w1)[..., None, None]
        P2 = np.eye(3) - s2[..., :, None]*s2[..., None, :]/(w2*w2)[..., None, None]
        Nm = {}
        for key, e in tens.items():
            if not np.any(e): Nm[key] = 0.0; continue
            ME, MB = V.vertex_geo(e, c1, c2, ssum, a, wd, wo)
            Bp = np.einsum('...ji,...jk,...kl->...il', X1, MB, X2)/rw[..., None, None]
            Nm[key] = 0.5*(rw[..., None, None]*ME + Bp)
        Na, Nb = [], []
        for i, e in enumerate(pols):
            base_ = Nm['sp%d' % i] + (Nm['qq']*(e[0, 0]/E**2)[..., None, None] if e[0, 0] != 0 else 0.0)
            qw = Nm['qw%d' % i]
            qwE = qw/E[..., None, None] if not np.isscalar(qw) else 0.0
            Na.append(base_ + qwE); Nb.append(base_ - qwE)
        def gram(A, B):
            if np.isscalar(A) or np.isscalar(B): return 0.0
            return np.einsum('...ij,...jk,...kl,...il->...', P1, A, P2, B)
        for i in range(n):
            for jj in range(i, n):
                val = -0.5*np.sum(gram(Na[i], Na[jj])/(E - omega) + gram(Nb[i], Nb[jj])/(E + omega))/N**3
                P[i, jj] += val
                if jj != i: P[jj, i] += val
    return P, qv
t4 = np.array([1., 0, 0, 0]); nx = np.r_[0., n3]
for n in shifts:
    sh = (n, n, 0); qv = 2*np.pi*np.array(sh, float)/N; s = np.linalg.norm(qv)
    print('\nshift %s, s = %.5f' % (sh, s))
    for w in (0.0, s, 2*s):
        P, _ = gram_block(sh, w, [E1F, gauge(t4, w, qv), gauge(nx, w, qv)])
        print('   omega=%.4f e1.Pi.g0 = %+.2e  e1.Pi.gn = %+.10e  g0.Pi.g0 = %+.10e  g0.Pi.gn = %+.6e  gn.Pi.gn = %+.10e' % (w, P[0, 1], P[0, 2], P[1, 1], P[1, 2], P[2, 2]), flush=True)
    P0, _ = gram_block((0, 0, 0), 0.0, [emb(np.outer(n3, n3))])
    print('   degree-0 bubble nn.Pi.nn (q=0) = %+.6e' % P0[0, 0])
print('runtime %.1f s' % (time.time() - t0))
