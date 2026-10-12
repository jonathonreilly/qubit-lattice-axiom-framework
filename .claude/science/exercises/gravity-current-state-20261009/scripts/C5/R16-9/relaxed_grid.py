"""R16-9: global grid scan of the relaxed (Young-measure) problem, vertex M, few-atom measures:
box [0,b] (s=1) + fast atoms (s=1) at levels l1, l2 with masses (1-x)(1-y)E, (1-x)y E + flat atom (s=0) at level l3 with mass xE,
E = pi - b. Reports min mu_E subject to Xi_M,Eg >= 0 and Xi_M,T2g >= 0 (and the max of min(Eg,T2g) subject to mu_E <= 0).
Usage: python3 relaxed_grid.py m"""
import numpy as np, sys, time, itertools
from math import gamma
m = float(sys.argv[1]); T0 = time.time()
NU = 700; umax = np.log(80.0/min(m*m, 1.0)) + 2; u = np.linspace(-16.0, umax, NU); t = np.exp(u); du = u[1]-u[0]
xg, wg = np.polynomial.legendre.leggauss(400)
cXi = t*du*t**1.5*np.exp(-t*m*m)/(32*gamma(2.5)); cMu = t*du*t**0.5*np.exp(-t*m*m)/(12*gamma(1.5))
bs = [0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.6, 2.0]
lf = np.concatenate([np.arange(0.15, 1.0, 0.05), np.arange(1.0, 3.15, 0.15)])     # fast levels
ll = np.arange(0.3, 3.15, 0.15)                                                       # flat levels
xs = np.linspace(0, 0.95, 20); ys = np.linspace(0, 1, 6)
best = None; bestd = None; nfeas = 0; ntot = 0
for b in bs:
    k = 0.5*b*(xg+1); w = 0.5*b*wg; Eb = np.exp(-np.outer(t, k*k))
    B = [Eb@(w*k**p)/np.pi for p in (0, 2, 4)]          # E0b, (F2b=G1b), (F4b=G2b)
    E = np.pi - b
    ef = np.exp(-np.outer(t, lf*lf))/np.pi; el = np.exp(-np.outer(t, ll*ll))/np.pi
    gf = lf*lf; gl = ll*ll
    # enumerate i1 <= i2 fast levels, y split, flat level j, flat fraction x
    for i1 in range(len(lf)):
        for i2 in range(i1, len(lf)):
            for y in (ys if i2 > i1 else [0.0]):
                # fast atom contributions per unit fast mass: (E0, F2, F4, G1, G2)
                a1, a2 = (1-y), y
                fe = a1*ef[:, i1] + a2*ef[:, i2]; f2 = a1*gf[i1]*ef[:, i1] + a2*gf[i2]*ef[:, i2]; f4 = a1*gf[i1]**2*ef[:, i1] + a2*gf[i2]**2*ef[:, i2]
                # arrays over (flat level j, x): shape (NU, J, X)
                X = xs[None, None, :]; Jl = el[:, :, None]
                fm = (1-X)*E; lm = X*E
                E0 = B[0][:, None, None] + fm*fe[:, None, None] + lm*Jl
                F2 = B[1][:, None, None] + fm*f2[:, None, None]
                F4 = B[2][:, None, None] + fm*f4[:, None, None]
                G1 = F2 + lm*gl[None, :, None]*Jl
                G2 = F4 + lm*(gl**2)[None, :, None]*Jl
                Jt = 2*t[:, None, None]*F2 - E0
                Eg = np.einsum('t,tjx->jx', cXi, Jt*2*(G2*E0 - G1**2)); T2 = np.einsum('t,tjx->jx', cXi, Jt*4*G1**2)
                mu = np.einsum('t,tjx->jx', cMu, E0*(3*F2**2 - F4*E0))
                ntot += mu.size
                ok = (Eg >= 0) & (T2 >= 0)
                if ok.any():
                    nfeas += ok.sum(); idx = np.unravel_index(np.where(ok, mu, np.inf).argmin(), mu.shape)
                    if best is None or mu[idx] < best[0]:
                        best = (mu[idx], Eg[idx], T2[idx], b, lf[i1], lf[i2], y, ll[idx[0]], xs[idx[1]])
                okd = mu <= 0
                if okd.any():
                    q = np.where(okd, np.minimum(Eg, T2), -np.inf); idx = np.unravel_index(q.argmax(), q.shape)
                    if bestd is None or q[idx] > bestd[0]:
                        bestd = (q[idx], Eg[idx], T2[idx], mu[idx], b, lf[i1], lf[i2], y, ll[idx[0]], xs[idx[1]])
    print('b=%.1f done (%.0fs): best so far %s' % (b, time.time()-T0, None if best is None else 'mu_E %+.4e' % best[0]), flush=True)
print('m=%g: %d measures, %d with Xi_M,Eg>=0 and Xi_M,T2g>=0' % (m, ntot, nfeas))
print('MIN mu_E s.t. both Xi>=0: mu_E %+.4e (Eg %+.2e T2g %+.2e) at b=%.2f fast l1=%.2f l2=%.2f y=%.2f flat l3=%.2f x=%.2f' % best)
print('MAX min(Eg,T2g) s.t. mu_E<=0: %+.4e (Eg %+.2e T2g %+.2e mu %+.2e) at b=%.2f l1=%.2f l2=%.2f y=%.2f l3=%.2f x=%.2f' % bestd)
print('runtime %.0fs' % (time.time()-T0))
