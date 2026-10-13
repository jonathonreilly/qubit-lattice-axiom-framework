"""R17-4 (b): U-vertex off-axis rows (E1) on R16-3's axis-zero laws (A, C2, C simplex; Newton re-solved here) and on corners."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import ZLaw, Mix, xi_all, mu_E
from floor_scan import Zz
from laws import Z1
from offaxis import xi_off, relation
T0 = time.time(); NF = 1 << 16
A = ZLaw([1.0, 0.0], [1.0 + (np.pi-1.0)/2], np.pi-1.0, 'G(1.0)', nf=NF)
C2 = Zz(1.0, 0.35, 0.47, 0.03); C = Zz(1.0, 0.35, 0.43, 0.03); B = ZLaw([1, -1, 1, -1, 1, -1, 0], [1.0, 1.4, 1.8, 2.2, 2.6, 3.0], 0.06, 'Z1', nf=NF)
def law(p, corners): return Mix(corners, [1 - sum(p)] + list(p))
def axisU(p, m, corners, nn=1 << 13, nu=800):
    g, f = law(p, corners).samples(nn); X = xi_all(g, f, m, nu=nu); return np.array([X['U,Eg'], X['U,T2g']])
def newton(fun, p, it=15, h=1e-5):
    for _ in range(it):
        r = fun(p); J = np.array([(fun(p + h*e) - r)/h for e in np.eye(len(p))]).T
        p = p - np.linalg.solve(J, r)
        if np.abs(r).max() < 1e-13: break
    return p, r
for nm, L in [('A=G(1.0)', A), ('C2', C2), ('C', C), ('Z1', B)]:
    X, _ = xi_off(L, 0.1, 'U')
    print('corner %-9s m=0.1 U: Eg %+.4e T2g %+.4e face1 %+.4e face2 %+.4e body %+.4e (face2-T2g %.1e, Oh resid %.1e)' % (nm, X['Eg'], X['T2g'], X['face1'], X['face2'], X['body'], X['face2']-X['T2g'], relation(X)), flush=True)
for m, p0 in [(0.1, (0.964879, 0.007410)), (0.03, (0.955996, 0.015995)), (0.01, (0.955208, 0.016763))]:
    p, r = newton(lambda p: axisU(p, m, [A, C2, C]), np.array(p0))
    L = law(p, [A, C2, C]); X, _ = xi_off(L, m, 'U', n1=1 << 15, nu=2500, umin=-20)
    print('U axis zero (A,C2,C) m=%.2f (u,v)=(%.6f,%.6f) in-simplex=%s | U rows: Eg %+.2e T2g %+.2e face1 %+.5e face2 %+.2e body %+.5e | v_max %.6f max|s\'| %.9f'
          % (m, p[0], p[1], p.min() >= 0 and p.sum() <= 1, X['Eg'], X['T2g'], X['face1'], X['face2'], X['body'], L.vmax(m), np.abs(L.sp).max()), flush=True)
print('runtime %.1fs' % (time.time()-T0))
