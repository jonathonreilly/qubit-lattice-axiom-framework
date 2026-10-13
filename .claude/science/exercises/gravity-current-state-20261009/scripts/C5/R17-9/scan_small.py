"""R17-9: small-box corners for the VU sign (photon) and for D1's T2g row."""
import numpy as np, time
from photon import *
from content3 import ferm
t0 = time.time()
for b in (0.1, 0.15, 0.2, 0.3):
    for w in (0.25, 0.5, 1.0, 2.0):
        law = photonGw(b, w); N = 96
        vu = [photon_xi(law, N, p)[0] for p in ('T2g', 'Eg')]
        print('%-22s N=%d VU Xi_T2g %+.4e Xi_Eg %+.4e' % (law.name, N, *vu), flush=True)
for bf in (0.1, 0.15, 0.2, 0.25):
    for r in (0.02, 0.3, 0.5773):
        v = ferm(bf, r, 0.01)[0]
        print('D1(%.2f,%.4f) m=0.01: Xi_T2g %+.4e Xi_Eg %+.4e mu_E %+.4e mu_T2 %+.3e' % (bf, r, *v), flush=True)
print('elapsed %.1fs' % (time.time()-t0))
