"""R19-34 (c): is the additive-mass strain Hessian sign-definite on Wilson-type box laws, or can a law datum zero it?
(i) D1(b, r) family x photons (naive, Gph(2.9435) = root photon, Gph(1.0)); H-cov.  (ii) Wilson-term strain placement W_j = W/l_j^kappa on the
root edge (kappa = 1 is R19-31's H-cov; kappa is a law datum of the strained law, R19-31 sec. 1 'a law datum and a stated choice').
Per e^2; E_g strain (e^h, e^-h, 1); Hessian by Richardson (d = 0.02, 0.04). Grid n = 6, hmax = 0.25 (converged to <=1e-8 in r1934_root.out)."""
import numpy as np, time
from r1934_lib import Grid, dm_mass, d1_law, photon, strain_l, hessian
t0 = time.time()
print('(i) D1(b, r) family, H-cov: dm, d2dm/dh2, ratio')
for phk in (('Gph', 2.9435), ('naive',), ('Gph', 1.0)):
    d = photon(*phk)
    for b in (0.6, 0.838, 0.909103708, 1.2, 1.4):
        for r in (0.1, 0.3, 0.555604226):
            s, W, L = d1_law(b, r)
            g = Grid([b, np.pi - b] + ([phk[1]] if phk[0] == 'Gph' else []), 6, 0.25)
            f0, _, _, _, hr = hessian(lambda h: dm_mass(s, W, d, g, strain_l(h)), 0.02)
            print('  photon %-14s b=%.4f r=%.4f: dm %+.6f  Hess %+.6f  ratio %+.4f' % (str(phk), b, r, f0, hr, hr/f0), flush=True)
print('(ii) root edge D1(0.909103708, 0.555604226) + Gph(2.9435): Wilson strain placement kappa')
s, W, L = d1_law(0.909103708, 0.555604226); d = photon('Gph', 2.9435)
g = Grid([0.909103708, np.pi - 0.909103708, 2.9435], 6, 0.25)
res = []
for kap in (0.0, 0.5, 1.0, 1.5, 2.0, 3.0):
    f0, _, _, _, hr = hessian(lambda h: dm_mass(s, W, d, g, strain_l(h), wexp=kap), 0.02)
    res.append((kap, hr)); print('  kappa=%.2f: dm %+.6f  Hess %+.6f' % (kap, f0, hr), flush=True)
k = np.array([r[0] for r in res]); hh = np.array([r[1] for r in res])
for i in range(len(k) - 1):
    if hh[i]*hh[i + 1] < 0:
        a, b_ = k[i], k[i + 1]
        fa = hh[i]
        for _ in range(40):
            c = 0.5*(a + b_)
            fc = hessian(lambda h: dm_mass(s, W, d, g, strain_l(h), wexp=c), 0.02)[4]
            if fc*fa > 0: a, fa = c, fc
            else: b_ = c
        print('  zero of the Hessian at kappa* = %.6f (Hess %+.2e)' % (0.5*(a + b_), fc))
print('time %.0f s' % (time.time() - t0))
