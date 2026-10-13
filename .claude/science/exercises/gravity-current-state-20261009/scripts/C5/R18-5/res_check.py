"""R18-5: grid check of the photon part (and GL check of the Dirac/scalar parts) at a solver end point."""
import numpy as np, sys, time
from smud_lib import dirac, phot, scal, NS, ND, NV
z = np.load(sys.argv[1]); t0 = time.time()
bg, fwg, bf, r, bs, frs, a = z; wg = fwg*(np.pi - bg); ws = frs*(np.pi - bs)
s = NS*scal(bs, ws); F = ND*dirac(bf, r); F2 = ND*dirac(bf, r, q=(4, 10))
print('knobs', z, 'w_g %.6f w_s %.6f' % (wg, ws))
print('Dirac GL(3,8) vs (4,10):', F, F2 - F)
for N in (48, 64, 96, 128):
    V = NV*phot(bg, wg, N, 'VWa', a)
    t = s + F + V
    print('photon N=%d: 12 vectors %s | TOTAL T2g %+.3e Eg %+.3e muE %+.3e  [%.0fs]' % (N, V, t[0], t[1], t[2], time.time()-t0), flush=True)
