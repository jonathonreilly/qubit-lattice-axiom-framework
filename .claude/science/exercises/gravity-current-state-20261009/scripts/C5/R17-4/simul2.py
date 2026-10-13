"""(b) Simultaneous Xi_Eg = Xi_T2g = 0 at a common mass, in the convex 2-simplex of three subluminal laws:
 A = G(1.0) (in U_0: both < 0), B = Z1 (wt 0.06: both > 0 at m <= 0.3), C = Zz(1.0, 0.35, 0.43, 0.03) (Eg < 0 < T2g at m = 0.1).
 sigma' = sigma'_A + u (sigma'_B - sigma'_A) + v (sigma'_C - sigma'_A), u, v >= 0, u + v <= 1  (|sigma'| <= 1 throughout).
Then (P62) add D = Gw(1.0, 0.05) (mu_E < 0) and solve Eg = T2g = mu_E = 0 in the 3-simplex."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import *; from floor_scan import Zz
T0 = time.time(); NF = 1 << 16
A = ZLaw([1.0, 0.0], [1.0 + (np.pi-1.0)/2], np.pi-1.0, 'G(1.0)', nf=NF)
B = ZLaw([1, -1, 1, -1, 1, -1, 0], [1.0, 1.4, 1.8, 2.2, 2.6, 3.0], 0.06, 'Z1', nf=NF)
C = Zz(1.0, 0.35, 0.43, 0.03)
D = ZLaw([1.0, 0.0], [1.0 + 0.025], 0.05, 'Gw(1.0,0.05)', nf=NF)
assert len(C.k) == len(B.k) == NF+1
def law(p, corners):
    w = [1 - sum(p)] + list(p); return Mix(corners, w)
def F(p, m, vtx, corners, nn=1 << 13, nu=800, shear=False):
    L = law(p, corners); g, f = L.samples(nn); X = xi_all(g, f, m, nu=nu)
    out = [X[vtx+',Eg'], X[vtx+',T2g']]
    if shear: out.append(mu_E(g, f, m, nu=nu))
    return np.array(out)
def newton(p, m, vtx, corners, shear=False, it=12, h=1e-4):
    for _ in range(it):
        r = F(p, m, vtx, corners, shear=shear)
        Jm = np.array([(F(p + h*e, m, vtx, corners, shear=shear) - r)/h for e in np.eye(len(p))]).T
        p = p - np.linalg.solve(Jm, r)
        if np.abs(r).max() < 1e-12: break
    return p, r
if __name__ == '__main__':
    sols = {}
    for vtx in ['M', 'U']:
        for m in [0.1, 0.03, 0.01]:
            # coarse grid
            best = None
            for u in np.arange(0, 1.0001, 0.05):
                for v in np.arange(0, 1.0001 - u, 0.05):
                    r = F(np.array([u, v]), m, vtx, [A, B, C], nn=1 << 12, nu=500)
                    s = np.abs(r).sum()
                    if best is None or s < best[0]: best = (s, u, v, r)
            p, r = newton(np.array([best[1], best[2]]), m, vtx, [A, B, C])
            L = law(p, [A, B, C]); g, f = L.samples(1 << 16); X = xi_all(g, f, m, nu=4000, umin=-22)
            ok = (p.min() >= 0) and (p.sum() <= 1)
            sols[(vtx, m)] = p
            print('%s m=%.2f: coarse (u,v)=(%.2f,%.2f); Newton (u,v)=(%.6f,%.6f) in-simplex=%s | refined Xi: %s | mu_E %+.3e | v_max %.6f max|s\'| %.6f min edge g %.4f'
                  % (vtx, m, best[1], best[2], p[0], p[1], ok, ' '.join('%s %+.2e' % kv for kv in X.items()), mu_E(g, f, m, nu=3000), L.vmax(m), np.abs(L.sp).max(), (L.sig[L.k >= 1.0]**2).min()), flush=True)
    # mass transfer: the M zero tuned at m = 0.01 evaluated at other masses
    p = sols[('M', 0.01)]; L = law(p, [A, B, C]); g, f = L.samples(1 << 15)
    print('M zero tuned at m=0.01, at other m: ' + ' | '.join('m=%g Eg %+.3e T2g %+.3e' % (m, *(lambda X: (X['M,Eg'], X['M,T2g']))(xi_all(g, f, m, nu=3000, umin=-20))) for m in [0.001, 0.003, 0.01, 0.03, 0.1, 0.3]), flush=True)
    # with shear (P62): 3-simplex A,B,C,D
    for m in [0.1, 0.01]:
        p0 = np.append(sols[('M', m)], 0.0)
        best = None
        for dd in [0.05, 0.1, 0.2, 0.3, 0.4, 0.5]:
            q = np.array([p0[0]*(1-dd), p0[1]*(1-dd), dd])
            r = F(q, m, 'M', [A, B, C, D], shear=True)
            print('   m=%.2f D-weight %.2f: Eg %+.2e T2g %+.2e mu_E %+.2e' % (m, dd, *r), flush=True)
    print('runtime %.1fs' % (time.time()-T0))
