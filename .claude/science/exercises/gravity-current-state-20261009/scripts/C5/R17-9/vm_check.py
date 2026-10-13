"""R17-9: VM vs VU per vector; VM continuum check (q=0 amplitude equals VU's when c=1 in box) via N-convergence."""
import numpy as np, time
from photon import *
t0 = time.time()
for law in (photonNN(), photonG(0.6), photonG(1.4), photonG(2.2), photonGw(1.0, 0.8)):
    for N in (48, 64):
        r = [photon_xi_VM(law, N, p) for p in ('T2g', 'Eg')]
        print('%-22s N=%d VM: Xi_T2g %+.5e (a %+.4e b %+.4e) Xi_Eg %+.5e (a %+.4e b %+.4e)' % (law.name, N, r[0][0], r[0][1], r[0][2], r[1][0], r[1][1], r[1][2]), flush=True)
print('elapsed %.1fs' % (time.time()-t0))
