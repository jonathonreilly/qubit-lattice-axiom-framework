import numpy as np, time
from f1_lib import *
F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH)
def mkgrid(n, hm, mph):
    br = [ROOT[0], np.pi - ROOT[0]] + [CPH + i*(np.pi - CPH)/mph for i in range(mph)]
    return Grid(br, n, hm)
for n, hm, mph in ((6, 0.25, 1), (6, 0.25, 6)):
    g = mkgrid(n, hm, mph)
    t0 = time.time(); v0 = dm_sf(F, G, g, 0.0); t1 = time.time()
    v = dm_sf(F, G, g, 0.003, nrk=2); t2 = time.time()
    vm = dm_sf(F, G, g, -0.003, nrk=2); t3 = time.time()
    print('n=%d hmax=%.2f mph=%d nodes=%d: dm0 %+.10f (%.1fs)  dm(+0.003) %+.12e (%.1fs) dm(-0.003) %+.12e  2nd diff/d^2 %+.6e' % (n, hm, mph, len(g.x), v0, t1-t0, v, t2-t1, vm, (v + vm - 2*v0)/0.003**2), flush=True)
