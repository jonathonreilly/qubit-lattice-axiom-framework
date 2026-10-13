"""F1 (b): branches the root does not fix, controls for the structural account, and parts.  Per e^2, SF units t; grid from argv.
Branches:  B1 main (Dirac flow at the rows' m = 0.01; Psym); B2 Dirac flow at m = 0 (the critical, massless propagator's own band);
           B3 single axis orderings (NOT hermitian, NOT cubic-covariant: path-sensitivity probe only; full +-t stencil);
           R19-11 0+ root under B1.
Controls (structural account):  photon unstrained; fermion unstrained; K1 = fermion carried by the PHOTON's separable flow (both flowed
           alike, separable: exact relabelling F_t(q) = F_0(Phi^g_t q)); K2 = photon symbols carried by the FERMION's flow (both alike,
           non-separable).  K1 is checked against the Jacobian formula <F_0 * d^2_t j_t> computed from the UNSTRAINED integrand only:
           j_t = j^x_t(k_x) j^y_t(k_y),  1D: j_t = 1 - t u' + (t^2/2)(u'^2 + u u''),  u = +-(1/2) p^g."""
import numpy as np, time, sys
from f1_lib import *
t00 = time.time()
n, hm, mph, d = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
which = sys.argv[5] if len(sys.argv) > 5 else 'all'
def mkgrid(b, n, hm, mph):
    br = [b, np.pi - b] + [CPH + i*(np.pi - CPH)/mph for i in range(mph)]
    return Grid(br, n, hm)
def Heven(F, G, g, d, **kw):
    f0 = dm_sf(F, G, g, 0.0, **kw); f1 = dm_sf(F, G, g, d, **kw); f2 = dm_sf(F, G, g, 2*d, **kw)
    h1 = 2*(f1 - f0)/d**2; h2 = 2*(f2 - f0)/(2*d)**2
    return f0, (4*h1 - h2)/3, h1
def Hfull(F, G, g, d, **kw):
    f0 = dm_sf(F, G, g, 0.0, **kw); fp, fm = dm_sf(F, G, g, d, **kw), dm_sf(F, G, g, -d, **kw)
    fp2, fm2 = dm_sf(F, G, g, 2*d, **kw), dm_sf(F, G, g, -2*d, **kw)
    h1 = (fp - 2*f0 + fm)/d**2; h2 = (fp2 - 2*f0 + fm2)/(2*d)**2
    return f0, (4*h1 - h2)/3, (fp - fm)/(2*d)
G = Phot(CPH)
F1 = Ferm(*ROOT, mflow=0.01)
g = mkgrid(ROOT[0], n, hm, mph)
print('grid n=%d hmax=%.2f mph=%d (%d nodes), d=%.4f' % (n, hm, mph, len(g.x), d), flush=True)
if which in ('all', 'branches'):
    f0, hr, _ = Heven(F1, G, g, d, nrk=2)
    print('B1 main (mflow 0.01, Psym)           : dm %+.9f  Hess_t %+.7e   [x4 %+.6e]' % (f0, hr, 4*hr), flush=True)
    _, tad, loop = dm_sf(F1, G, g, 0.0, parts=True)
    _, tadp, loopp = dm_sf(F1, G, g, d, parts=True, nrk=2)
    _, tadp2, loopp2 = dm_sf(F1, G, g, 2*d, parts=True, nrk=2)
    ht = (4*2*(tadp - tad)/d**2 - 2*(tadp2 - tad)/(2*d)**2)/3; hl = (4*2*(loopp - loop)/d**2 - 2*(loopp2 - loop)/(2*d)**2)/3
    print('   parts: tadpole dm %+.6f Hess %+.6e ; exchange dm %+.6f Hess %+.6e' % (tad, ht, loop, hl), flush=True)
    F2 = Ferm(*ROOT, mflow=0.0)
    f0, hr, _ = Heven(F2, G, g, d, nrk=2)
    print('B2 (Dirac flow at m = 0, Psym)       : dm %+.9f  Hess_t %+.7e   [x4 %+.6e]' % (f0, hr, 4*hr), flush=True)
    F0p = Ferm(*ROOT0, mflow=0.01)
    g0 = mkgrid(ROOT0[0], n, hm, mph)
    f0, hr, _ = Heven(F0p, G, g0, d, nrk=2)
    print('R19-11 0+ root, B1                    : dm %+.9f  Hess_t %+.7e   [x4 %+.6e]' % (f0, hr, 4*hr), flush=True)
if which in ('all', 'orders'):
    for o in (('x','y','z'), ('y','x','z'), ('x','z','y'), ('z','x','y'), ('y','z','x'), ('z','y','x')):
        f0, hr, gr = Hfull(F1, G, g, d, nrk=2, path=o)
        print('B3 single order %s (non-hermitian)   : dm %+.9f  Hess_t %+.7e  grad %+.2e' % (''.join(o), f0, hr, gr), flush=True)
if which in ('all', 'controls'):
    for lab, kw in (('photon unstrained (F own)', dict(photflow='none')), ('fermion unstrained (photon own)', dict(fermflow='none')),
                    ('K1 both on photon flow (separable)', dict(fermflow='phot')), ('K2 both on fermion flow (non-separable)', dict(photflow='ferm'))):
        f0, hr, _ = Heven(F1, G, g, d, nrk=2, **kw)
        print('%-40s: dm %+.9f  Hess_t %+.7e' % (lab, f0, hr), flush=True)
    # K1 Jacobian formula from the unstrained integrand
    def u1(k): return 0.5*G.p1(k)
    eps = 1e-5
    def du(k): return (u1(k + eps) - u1(k - eps))/(2*eps)
    def d2u(k): return (u1(k + eps) - 2*u1(k) + u1(k - eps))/eps**2
    def jac2(X, Y, Z):
        ux, uxp, uxpp = u1(X), du(X), d2u(X)
        uy, uyp, uypp = -u1(Y), -du(Y), -d2u(Y)
        return (uxp**2 + ux*uxpp) + (uyp**2 + uy*uypp) + 2*uxp*uyp
    print('K1 via Jacobian formula <F_0 j\'\'>     : Hess_t %+.7e' % dm_sf(F1, G, g, 0.0, extra=jac2), flush=True)
print('time %.0f s' % (time.time() - t00))
