"""R19-29 (c), lam_nn = 0 branch only: re-solve face1 with the Schur-completed row by moving w_d (face2 is an isolated A_2
pole, Lemma I of R19-23, so w_o stays at R18-13's value). Photon kappa, c4 depend on (w_d, w_o); scalar and Dirac do not.
Physical face1 total(w_d) = J11 (w_d - w_d0) - kappa_tot(w_d)^2 / (c4_tot(w_d) + 8 X_tot),  J11 = 1.67645 (R18-13, N = 224).
usage: python r1929_resolve.py Ng kappa_sd c4_sd X_sd  (scalar+Dirac totals from r1929_root.py at matching resolution)"""
import os, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'arch18'))
from a1lib import n3, E1F
from photon import kgrid, crossmat, photonGw
import vwface_copy as V
t0 = time.time()
Ng = int(sys.argv[1]); kap_sd, c4_sd, X_sd = (float(v) for v in sys.argv[2:5])
root = np.load(os.path.join(HERE, 'root_refR18-9.npy')); bs, bf, rr, a, fr, bg, fw, m = root
wd0, wo0 = -1.171554, -0.195418; J11 = 1.67645
NNs = np.outer(n3, n3); E13 = E1F[1:, 1:]
pl = photonGw(bg, fw*(np.pi - bg)); kg = kgrid(Ng); sg = pl.sig(kg); cg = pl.c(kg); jj = np.arange(Ng)
def phot_g(n, wd, wo):
    sh = (n, n, 0); j2 = [(sh[d] - jj - 1) % Ng for d in range(3)]
    Y, Z = np.meshgrid(jj, jj, indexing='ij'); acc = np.zeros(3)
    for ix in range(Ng):
        X_ = np.full_like(Y, ix); I1 = [X_, Y, Z]; I2 = [j2[0][X_], j2[1][Y], j2[2][Z]]
        s1 = np.stack([sg[I] for I in I1], -1); s2 = np.stack([sg[I] for I in I2], -1)
        c1 = np.stack([cg[I] for I in I1], -1); c2 = np.stack([cg[I] for I in I2], -1)
        ssum = np.stack([kg[I1[d]] + kg[I2[d]] for d in range(3)], -1)
        w1 = np.sqrt((s1*s1).sum(-1)); w2 = np.sqrt((s2*s2).sum(-1)); rw = np.sqrt(w1*w2); E = w1 + w2
        X1 = crossmat(s1); X2 = crossmat(s2)
        P1 = np.eye(3) - s1[..., :, None]*s1[..., None, :]/(w1*w1)[..., None, None]
        P2 = np.eye(3) - s2[..., :, None]*s2[..., None, :]/(w2*w2)[..., None, None]
        Nm = []
        for e in (E13, NNs):
            ME, MB = V.vertex_geo(e, c1, c2, ssum, a, wd, wo)
            Bp = np.einsum('...ji,...jk,...kl->...il', X1, MB, X2)/rw[..., None, None]
            Nm.append(0.5*(rw[..., None, None]*ME + Bp))
        g = lambda A, B: 0.5*np.einsum('...ij,...jk,...kl,...il->...', P1, A, P2, B)
        gen, gnn = g(Nm[0], Nm[1]), g(Nm[1], Nm[1])
        acc += [np.sum(-4*gen/E), np.sum(-8*gnn/E), np.sum(gnn/E**3)]
    return acc/Ng**3, 2*np.pi*np.sqrt(2)*n/Ng
def phot_kc(wd, wo):
    v0, _ = phot_g(0, wd, wo); v1, s1 = phot_g(1, wd, wo); v2, s2 = phot_g(2, wd, wo)
    k1 = (v1[0] - v0[0])/s1**2; k2 = (v2[0] - v0[0])/s2**2
    c1 = (v1[1] - v0[1])/s1**2; c2 = (v2[1] - v0[1])/s2**2
    return (4*k1 - k2)/3, (4*c1 - c2)/3, v0[2]
wds = [wd0, wd0 - 0.4, wd0 - 0.8]
rows = []
for wd in wds:
    kg_, cg_, Xg = phot_kc(wd, wo0)
    kt, ct, Xt = kap_sd + 12*kg_, c4_sd + 12*cg_, X_sd + 12*Xg
    sh = -kt**2/(ct + 8*Xt)
    rows.append((wd, kt, ct, Xt, sh))
    print('w_d=%+.6f: kappa_tot %+.6e c4_tot %+.6e X_tot %+.6e  Schur term -kappa^2/(c4+8X) %+.6e  phys face1 = %+.6e'
          % (wd, kt, ct, Xt, sh, J11*(wd - wd0) + sh), flush=True)
R = np.array(rows)
pk = np.polyfit(R[:, 0], R[:, 1], 2); pc = np.polyfit(R[:, 0], R[:, 2], 2); Xt = R[0, 3]
f = lambda w: J11*(w - wd0) - np.polyval(pk, w)**2/(np.polyval(pc, w) + 8*Xt)
from scipy.optimize import brentq
lo, hi = wd0 - 2.0, wd0 + 0.5
grid = np.linspace(lo, hi, 401); fv = [f(w) for w in grid]
roots = [brentq(f, grid[i], grid[i+1]) for i in range(len(grid)-1) if fv[i]*fv[i+1] < 0]
print('kappa(w_d) quad fit', pk, ' c4(w_d) quad fit', pc)
print('roots of the Schur-completed face1 total in w_d (w_o fixed at %+.6f): %s' % (wo0, ['%+.5f' % r for r in roots]))
for r in roots:
    dk = np.polyval(np.polyder(pk), r); dc = np.polyval(np.polyder(pc), r); kk = np.polyval(pk, r); cc = np.polyval(pc, r) + 8*Xt
    J = J11 - (2*kk*dk*cc - kk**2*dc)/cc**2
    print('   root w_d = %+.5f: d(face1_phys)/d w_d = %+.5f (raw 1.67645); 2x2 Jacobian det = %+.4f (raw 11.639)' % (r, J, J*6.94286))
print('runtime %.1f s' % (time.time() - t0))
