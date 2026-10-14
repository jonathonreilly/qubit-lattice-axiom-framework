"""F1 (b): additive-mass E_g Hessian on the SF-strained root law (main branch B1: Dirac flow at the rows' m = 0.01, photon own flow,
Psym minimal coupling, Feynman gauge, critical m = 0 at h = 0). Convergence in grid (n, hmax, photon-edge panels mph) and FD step d.
Evenness dm(-t) = dm(t) is exact (C2 about [110], checked in f1_timing.out), so Hess = 2[dm(d) - dm(0)]/d^2, Richardson over d, 2d.
SF units t (v = (t/2) diag(1,-1,0).p).  H-cov-equivalent (R19-34's h; t = -2h on soft modes, rR19-31 sec. 1): Hess_h = 4 Hess_t."""
import numpy as np, time, sys
from f1_lib import *
t00 = time.time()
def mkgrid(b, n, hm, mph):
    br = [b, np.pi - b] + [CPH + i*(np.pi - CPH)/mph for i in range(mph)]
    return Grid(br, n, hm)
def H(F, G, g, d, **kw):
    f0 = dm_sf(F, G, g, 0.0, **kw); f1 = dm_sf(F, G, g, d, **kw); f2 = dm_sf(F, G, g, 2*d, **kw)
    h1 = 2*(f1 - f0)/d**2; h2 = 2*(f2 - f0)/(2*d)**2
    return f0, h1, h2, (4*h1 - h2)/3
which = sys.argv[1] if len(sys.argv) > 1 else 'conv'
GRIDS = ((6, 0.25, 6, 0.003), (8, 0.25, 10, 0.003), (8, 0.15, 16, 0.003), (8, 0.15, 16, 0.0015))
if which == 'conv2':
    GRIDS = ((8, 0.15, 16, 0.003), (8, 0.15, 16, 0.0015)); which = 'conv'
if which == 'conv':
    F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH)
    print('R18-9 root D1(0.909103708, 0.555604226) + Gph(2.9435); branch B1 (mflow 0.01, Psym); per e^2, SF units')
    for (n, hm, mph, d) in GRIDS:
        g = mkgrid(ROOT[0], n, hm, mph); t0 = time.time()
        f0, h1, h2, hr = H(F, G, g, d, nrk=2)
        print('  n=%2d hmax=%.2f mph=%2d nodes=%3d d=%.4f: dm %+.9f  Hess_t (d) %+.7e (2d) %+.7e Rich %+.7e  [x4 = %+.6e]  (%.0fs)'
              % (n, hm, mph, len(g.x), d, f0, h1, h2, hr, 4*hr, time.time() - t0), flush=True)
print('time %.0f s' % (time.time() - t00))
