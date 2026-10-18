"""K2b note N2 (descriptive check of a proved claim): the PV denominator det D5(1) is itself an RP kernel (L_s = 4, 8)
on the SH-search pool, where the ratio det D5(mf)/det D5(1) is certified negative."""
import numpy as np, sys, time
from lat2d import Geom
from k2b_lib import *
d = np.load('pool_search_open_Lt12_seed1201_SH.npz'); G = Geom(2, 6, False, -1)
U = [{'x': d['ux'][i], 't': d['ut'][i]} for i in range(len(d['ux']))]; k = len(U); t0 = time.time()
for Ls in (4, 8):
    Zl, _ = full_kernel(G, U, 0.6, 16, None, 'D5ONE', Ls); Zh, _ = full_kernel(G, U, 0.6, 32, None, 'D5ONE', Ls)
    q = np.abs(Zh - Zl).max(); E = k * q + 1e-13; a, b, ev = lam(Zh)
    print(f"det D5(1) kernel L_s={Ls}: lam_min {a:+.4e} min/max {a/b:+.4e} E {E:.1e} PSD-within-error {a > -10*E} [{time.time()-t0:.0f}s]", flush=True)
print("done")
