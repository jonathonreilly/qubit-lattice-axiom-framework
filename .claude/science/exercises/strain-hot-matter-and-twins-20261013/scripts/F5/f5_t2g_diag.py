"""F5 diagnostic: F1's frame-component photon (d_{t,j}(q) = d([Phi^g_t q]_j)) does not extend to an off-diagonal (T2g) strain.
For h = e_x e_y + e_y e_x the photon flow moves q_y by (t/2) p^g(q_x), so d_{t,y}(q) vanishes on the surface
q_y* = -(t/2) p^g(q_x) + O(t^2), where the link difference L_y = D_t(B + q_y e_y) - D_t(B) does NOT vanish (it vanishes only at q_y = 0).
The generalized-link vertex V_y = L_y/d_{t,y} then diverges like 1/(q_y - q_y*), and |V_y|^2 is not integrable across the surface.
Printed: along a line at fixed (q_x, q_z), |a_y|^2 = |L_y^c|^2/d_{t,y}^2 approaching q_y* from both sides; and the E_g control (no zero
off q_y = 0).  Then the quadrature value of dm at t = 0.003 for T2g on three grids (no convergence) vs E_g."""
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f5_lib import *
F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH)
t = 0.003
for lab, h in (('T2g', H_T2), ('E_g control', H_EG)):
    qx, qz = 1.3, 0.7
    # locate the zero of d_{t,y} along q_y by bisection on the flowed y component
    def fy(qy):
        return flow3(G, h, np.array([qx]), np.array([qy]), np.array([qz]), t, 4)[1][0]
    lo, hi = -0.5, 0.5
    if fy(lo)*fy(hi) > 0:
        print('%s: d_{t,y} has no zero on q_y in [-0.5, 0.5] at (q_x, q_z) = (%.1f, %.1f)' % (lab, qx, qz)); continue
    for _ in range(80):
        mid = 0.5*(lo + hi)
        if fy(lo)*fy(mid) <= 0: hi = mid
        else: lo = mid
    qys = 0.5*(lo + hi)
    print('%s: d_{t,y} = 0 at q_y* = %+.6e (t/2 p^g(q_x) = %+.6e)' % (lab, qys, 0.5*t*0.5*float(G.G.dg(qx))))
    for eps in (1e-2, 1e-3, 1e-4, 1e-5, -1e-5, -1e-4):
        qy = qys + eps
        X, Y, Z = np.array([qx]), np.array([qy]), np.array([qz])
        def DF(a, b, c):
            u, v, w = flow3(F, h, a, b, c, t, 4)
            return np.array([F.s(u), F.s(v), F.s(w)])
        Ly = DF(X, Y, 0*Z) - DF(X, 0*Y, 0*Z)            # one leg (base q_x e_x) of the Psym average
        dty = G.d(flow3(G, h, X, Y, Z, t, 4)[1])
        print('   q_y - q_y* = %+.0e : |L_y^c| = %.3e  d_{t,y} = %.3e  |L_y^c|^2/d^2 = %.3e' % (eps, np.linalg.norm(Ly), dty[0], (np.linalg.norm(Ly)/dty[0])**2))
print('quadrature (T2g, t = 0.003) on three grids; E_g at the same t for comparison:', flush=True)
for (n, hm, mph) in ((4, 0.35, 3), (5, 0.30, 4), (6, 0.25, 6)):
    br = mkbreaks(ROOT[0], CPH, mph); xo = panels(br, n, hm); xs = panels_sym(br, n, hm)
    a = dm_gen(F, G, H_T2, xs, xo, xo, t); b = dm_gen(F, G, H_EG, xo, xo, xo, t)
    print('   %3d nodes/half-axis: T2g dm %+.6e   E_g dm %+.10e' % (len(xo[0]), a, b), flush=True)
