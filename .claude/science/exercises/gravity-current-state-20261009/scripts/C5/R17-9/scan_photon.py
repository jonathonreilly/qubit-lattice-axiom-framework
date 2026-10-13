"""R17-9 (b): per-vector Xi_T2g, Xi_Eg (VU = site-averaged Maxwell stress, product of legs; E1 = form factors at relative momentum),
mu_E, mu_T2 (SF: 2 polarizations x scalar strain formula on omega, regulator m_g), whole-zone v_max (= max d' for separable omega)."""
import numpy as np, time, sys
from photon import *
from zz import mu_E
N = int(sys.argv[1]) if len(sys.argv) > 1 else 48
t0 = time.time()
laws = [photonNN()] + [photonG(b) for b in (0.3, 0.6, 1.0, 1.4, 1.8, 2.2, 2.6, 2.9, 3.05)] + \
       [photonGw(b, w) for b in (0.6, 1.0, 1.4, 2.0) for w in (0.15, 0.4, 0.8) if b + w <= np.pi]
for law in laws:
    out = []
    for cm in ('VU', 'E1'):
        out += [photon_xi(law, N, p, cmode=cm)[0] for p in ('T2g', 'Eg')]
    g, f = law.samples(1 << 14)
    mus = [2*mu_E(g, f, mg) for mg in (1e-3, 1e-4)]
    print('%-22s VU: T2g %+.4e Eg %+.4e | E1: T2g %+.4e Eg %+.4e | mu_E(SF) %+.4e (m_g 1e-3) %+.4e (1e-4) mu_T2 0 | max d\' %.6f min d\' %.3f d(pi) %.3f' %
          (law.name, *out, *mus, law.maxdp, law.mindp, law.dpi), flush=True)
print('N=%d elapsed %.1fs' % (N, time.time()-t0))
