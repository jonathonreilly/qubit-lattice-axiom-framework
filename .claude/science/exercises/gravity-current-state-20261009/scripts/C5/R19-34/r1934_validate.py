"""R19-34 (validation): the generalized additive-mass formula reproduces R19-31's naive-Wilson numbers (r1931_wilson_mass.out:2-7),
and r = 0 gives 0 (chiral control). Grid convergence n = 6, 8 GL nodes per panel."""
import numpy as np, time
from r1934_lib import Grid, dm_mass, naive_wilson, strain_l, hessian
t0 = time.time()
s, W, d = naive_wilson(1.0)
for n in (6, 8):
    g = Grid([], n)
    f = lambda h: dm_mass(s, W, d, g, strain_l(h))
    f0, g1, h1, h2, hr = hessian(f, 0.02)
    print('naive Wilson r=1, naive photon, n=%d (%d nodes/half-axis): dm/e^2 = %+.9f (R19-31 +0.374347473)  d/dh %+.1e  d2/dh2 = %+.5e (d=0.02) %+.5e (2d) Richardson %+.5e (R19-31 -6.21578e-02 / -6.20847e-02)'
          % (n, len(g.x), f0, g1, h1, h2, hr), flush=True)
s0, W0, d0 = naive_wilson(0.0)
print('r = 0 control: dm = %+.2e' % dm_mass(s0, W0, d0, Grid([], 6)))
print('time %.0f s' % (time.time() - t0))
