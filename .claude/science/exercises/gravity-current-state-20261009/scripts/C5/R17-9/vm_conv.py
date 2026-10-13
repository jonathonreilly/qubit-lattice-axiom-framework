"""R17-9: N-convergence and shift-pair check of the VM photon on the negative-T2g laws."""
import numpy as np, time
from photon import *
t0 = time.time()
for law in (photonGw(0.3, 1.0), photonGw(0.3, 0.5)):
    for N, sh in ((48, (1, 2)), (64, (1, 2)), (96, (1, 2)), (128, (1, 2)), (128, (2, 4))):
        r = [photon_xi_VM(law, N, p, shifts=sh)[0] for p in ('T2g', 'Eg')]
        print('%-22s N=%3d shifts %s VM Xi_T2g %+.5e Xi_Eg %+.5e  (%.0fs)' % (law.name, N, sh, *r, time.time()-t0), flush=True)
