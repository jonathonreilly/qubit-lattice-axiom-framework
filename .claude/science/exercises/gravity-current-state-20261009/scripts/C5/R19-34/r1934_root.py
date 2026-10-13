"""R19-34 (b): one-loop additive mass dm and its strain gradient/Hessian on the ROOT's Dirac edges (H-cov E_g strain, per e^2).
Root edges (identified in the report, section 1):
  R18-9 refined root  D1(b_f, r) = (0.909103708, 0.555604226), photon gamma G_w(2.9435) = Gph(2.9435)   (vR18-9:11; rR19-12:21,72-74)
  R19-11 0+ root      D1(0.915438682, 0.568280847), same photon                                         (rR19-11:167; vR19-11:14)
Comparators: same D1 with the naive photon; D1(1.4, 1/sqrt3) (R16-1 member); naive Wilson r = 1 and r = 0.5556; r = 0.
Checks: (i) grid n = 6 / 8 GL nodes per panel and hmax 0.25 / 0.15; (ii) cubic invariance: Hessian along (h,h,-2h) = 3 x along (h,-h,0);
(iii) isotropic dilation: dm(l) = dm(1)/l exactly -> d2/dh2 = dm(0)."""
import numpy as np, time, sys
from r1934_lib import Grid, dm_mass, naive_wilson, d1_law, photon, strain_l, hessian
t0 = time.time()
cases = []
bf, rf = 0.909103708, 0.555604226
b0, r0 = 0.915438682, 0.568280847
for lab, b, r, ph in (('R18-9 root D1(0.909103708,0.555604226)+Gph(2.9435)', bf, rf, ('Gph', 2.9435)),
                      ('R19-11 0+ root D1(0.915438682,0.568280847)+Gph(2.9435)', b0, r0, ('Gph', 2.9435)),
                      ('R18-9 root Dirac edge + naive photon', bf, rf, ('naive',)),
                      ('D1(1.4,1/sqrt3) + naive photon (R16-1 member)', 1.4, 1/np.sqrt(3), ('naive',)),
                      ('R18-9 root D1, r -> 0 (chiral control) + Gph', bf, 0.0, ('Gph', 2.9435))):
    if r > 0:
        s, W, L = d1_law(b, r)
        Wpi = L.Wpi
    else:
        from sublum import SymS
        A = SymS(b); s = A.s; W = lambda k: 0.0*np.asarray(k, float); Wpi = 0.0
    d = photon(*ph)
    brk = [b, np.pi - b] + ([ph[1]] if ph[0] == 'Gph' else [])
    print('%s  [W_pi = %.6f]' % (lab, Wpi), flush=True)
    for n, hm in ((6, 0.25), (8, 0.25), (8, 0.15)):
        g = Grid(brk, n, hm)
        f = lambda h: dm_mass(s, W, d, g, strain_l(h, 'Eg'))
        f0, g1, h1, h2, hr = hessian(f, 0.02)
        print('   n=%d hmax=%.2f (%3d nodes/half-axis): dm/e^2 = %+.9f   d/dh = %+.1e   d2dm/dh2 [Eg (h,-h,0)] = %+.6e (d) %+.6e (2d) Rich %+.6e'
              % (n, hm, len(g.x), f0, g1, h1, h2, hr), flush=True)
    if r > 0:
        f2 = lambda h: dm_mass(s, W, d, g, strain_l(h, 'Eg2'))
        _, _, a1, a2, ar = hessian(f2, 0.02)
        fi = lambda h: dm_mass(s, W, d, g, strain_l(h, 'iso'))
        i0, ig, i1, i2, ir = hessian(fi, 0.02)
        print('   cubic check: Hessian along (h,h,-2h) = %+.6e Rich; ratio to Eg = %.6f (expect 3)' % (ar, ar/hr))
        print('   dilation check: dm(iso) d/dh = %+.6e (expect -dm = %+.6e), d2/dh2 Rich = %+.6e (expect +dm)' % (ig, -i0, ir), flush=True)
        _, tad, loop = dm_mass(s, W, d, g, strain_l(0.0), parts=True)
        print('   parts at h=0: tadpole %+.6f  exchange %+.6f' % (tad, loop))
for r in (1.0, 0.555604226):
    s, W, d = naive_wilson(r)
    g = Grid([], 8)
    f = lambda h: dm_mass(s, W, d, g, strain_l(h, 'Eg'))
    f0, g1, h1, h2, hr = hessian(f, 0.02)
    print('naive Wilson r=%.6f, naive photon: dm/e^2 = %+.9f  d2dm/dh2 Rich = %+.6e  ratio Hess/dm = %+.5f' % (r, f0, hr, hr/f0), flush=True)
print('time %.0f s' % (time.time() - t0))
