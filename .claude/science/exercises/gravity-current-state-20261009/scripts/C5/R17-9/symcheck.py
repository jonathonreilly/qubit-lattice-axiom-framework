"""R17-9 independent check of the photon alpha: symmetric pair (k+q/2, -k+q/2) on a midpoint grid with off-grid interpolation
(different quadrature from the exact grid shift), plus E-only / B-only diagnostics and shift-pair (1,2) vs (2,4) at fixed N."""
import numpy as np, time
from photon import *
def W_sym(law, N, q, pol, parts='EB'):
    k = kgrid(N); e = EPOL[pol]
    sx, cx = law.sig(k), law.c(k)
    zp, zm = k + q/2, -k + q/2
    def rep(z): return (z + np.pi) % (2*np.pi) - np.pi
    szp, czp = law.sig(rep(zp)), law.c(rep(zp)); szm, czm = law.sig(rep(zm)), law.c(rep(zm))
    tot = 0.0; totb = 0.0
    j = np.arange(N); Y, Z = np.meshgrid(j, j, indexing='ij')
    for ix in range(N):
        X_ = np.full_like(Y, ix)
        s1 = np.stack([sx[X_], sx[Y], szp[Z]], -1); s2 = np.stack([-sx[X_], -sx[Y], szm[Z]], -1)
        c1 = np.stack([cx[X_], cx[Y], czp[Z]], -1); c2 = np.stack([cx[X_], cx[Y], czm[Z]], -1)
        ct1 = np.stack([c1[..., 1]*c1[..., 2], c1[..., 0]*c1[..., 2], c1[..., 0]*c1[..., 1]], -1)
        ct2 = np.stack([c2[..., 1]*c2[..., 2], c2[..., 0]*c2[..., 2], c2[..., 0]*c2[..., 1]], -1)
        w1 = np.sqrt((s1*s1).sum(-1)); w2 = np.sqrt((s2*s2).sum(-1)); rw = np.sqrt(w1*w2)
        Ae = rw[..., None, None]*c1[..., :, None]*e*c2[..., None, :] if 'E' in parts else 0
        Mid = ct1[..., :, None]*e*ct2[..., None, :]
        Bp = np.einsum('...ji,...jk,...kl->...il', crossmat(s1), Mid, crossmat(s2))/rw[..., None, None] if 'B' in parts else 0
        Nm = 0.5*(Ae + Bp)
        P1 = np.eye(3) - s1[..., :, None]*s1[..., None, :]/(w1*w1)[..., None, None]
        P2 = np.eye(3) - s2[..., :, None]*s2[..., None, :]/(w2*w2)[..., None, None]
        Wv = np.einsum('...ij,...jk,...kl,...il->...', P1, Nm, P2, Nm); E = w1 + w2
        tot += np.sum(Wv/E); totb += np.sum(Wv/E**3)
    return -tot/N**3, -totb/N**3
t0 = time.time()
for law in (photonNN(), photonG(1.4)):
    for pol in ('T2g', 'Eg'):
        for parts in ('EB', 'E', 'B'):
            N = 64; P0, beta = W_sym(law, N, 0.0, pol, parts)
            q1 = 0.08; D1 = W_sym(law, N, q1, pol, parts)[0] - P0; D2 = W_sym(law, N, 2*q1, pol, parts)[0] - P0
            alpha = (16*D1 - D2)/(12*q1*q1)
            print('%s %s parts=%s  symmetric-pair N=64 q=0.08,0.16: alpha %+.5e beta %+.5e Xi %+.5e' % (law.name, pol, parts, alpha, beta, alpha+beta), flush=True)
        a = photon_xi(law, 64, pol, shifts=(2, 4)); print('   grid-shift N=64 shifts (2,4): Xi %+.5e' % a[0])
        a = photon_xi(law, 96, pol); print('   grid-shift N=96 shifts (1,2): Xi %+.5e (alpha %+.5e beta %+.5e)' % a, flush=True)
print('elapsed %.1fs' % (time.time()-t0))
