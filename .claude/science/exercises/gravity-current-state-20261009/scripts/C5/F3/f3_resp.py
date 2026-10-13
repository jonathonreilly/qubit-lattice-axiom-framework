"""F3 (b): linear response L_G = d dm/d eps (t = 0, unstrained root law) to the D-H dressing V = exp(i eps G_f), per symmetric
generator, converged on F1's octant GL grids; evenness check of the dressed integrand; parts (tadpole / exchange).
Hessian with dressing a*G (V_t = exp(i t^2 a G)):  Hess = Hess_F1 + 2 a L_G  (proved, report sec. 2);  zero at a* = -Hess_F1/(2 L_G)."""
import numpy as np, time, sys
from f3_lib import *
t00 = time.time()
G = Phot(CPH)
which = sys.argv[1] if len(sys.argv) > 1 else 'main'

if which == 'even':
    F = Ferm(*ROOT)
    print('(A) evenness of the dressed integrand in each q_j: octant midpoint N vs full-BZ midpoint 2N (same |q| node set)')
    for N in (12, 20):
        xo = (np.arange(N) + 0.5)*np.pi/N; wo = np.full(N, 1.0/N)
        xf = -np.pi + (np.arange(2*N) + 0.5)*np.pi/N; wf = np.full(2*N, 1.0/(2*N))
        for nm in ('G1', 'G2', 'G3', 'G4'):
            a = dm_gen(make_cM(F, 0.0, nm, eps=0.05), G.d(xo), G.d(xo), G.d(xo), xo, wo)
            b = dm_gen(make_cM(F, 0.0, nm, eps=0.05), G.d(xf), G.d(xf), G.d(xf), xf, wf)
            print('   N=%2d %s eps=0.05: octant %+.15e  full %+.15e  diff %.1e' % (N, nm, a, b, a - b), flush=True)

GRIDS = ((6, 0.25, 6), (8, 0.25, 10), (8, 0.15, 16))
if which == 'main':
    F = Ferm(*ROOT)
    print('(B) R18-9 root D1(0.909103708, 0.555604226) + Gph(2.9435): L_G per e^2 (per unit eps), central d = 1e-3 and 2e-3, Richardson')
    for (n, hm, mph) in GRIDS:
        g = mkgrid(ROOT[0], n, hm, mph)
        for nm in ('G1', 'G2', 'G3', 'G4'):
            t0 = time.time()
            L1, L2, Lr, f0 = lin_resp(F, G, g, nm)
            print('   n=%d hmax=%.2f mph=%2d nodes=%3d %s: dm0 %+.9f  L(d) %+.9e  L(2d) %+.9e  L_rich %+.9e  (%.0fs)'
                  % (n, hm, mph, len(g.x), nm, f0, L1, L2, Lr, time.time() - t0), flush=True)
if which == 'root0':
    F = Ferm(*ROOT0)
    print('(C) 0+ root D1(0.915438682, 0.568280847) + Gph(2.9435)')
    for (n, hm, mph) in GRIDS[1:]:
        g = mkgrid(ROOT0[0], n, hm, mph)
        for nm in ('G1', 'G2'):
            t0 = time.time()
            L1, L2, Lr, f0 = lin_resp(F, G, g, nm)
            print('   n=%d hmax=%.2f mph=%2d nodes=%3d %s: dm0 %+.9f  L(d) %+.9e  L(2d) %+.9e  L_rich %+.9e  (%.0fs)'
                  % (n, hm, mph, len(g.x), nm, f0, L1, L2, Lr, time.time() - t0), flush=True)
if which == 'parts':
    F = Ferm(*ROOT)
    g = mkgrid(ROOT[0], 8, 0.25, 10)
    dx, dy, dz = photon_syms(G, g.x)
    print('(D) parts (tadpole / exchange) of L, 240 nodes, central d = 1e-3')
    for nm in ('G1', 'G2'):
        p = dm_gen(make_cM(F, 0.0, nm, eps=1e-3), dx, dy, dz, g.x, g.w, parts=True)
        m = dm_gen(make_cM(F, 0.0, nm, eps=-1e-3), dx, dy, dz, g.x, g.w, parts=True)
        print('   %s: L_total %+.6e  L_tadpole %+.6e  L_exchange %+.6e' % (nm, (p[0] - m[0])/2e-3, (p[1] - m[1])/2e-3, (p[2] - m[2])/2e-3), flush=True)
print('time %.0f s' % (time.time() - t00))
