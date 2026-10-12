"""(b) Simultaneous zeros. Family F2(t, w): sigma' = (1-t) sigma'_{G(1.0)} + t sigma'_{Z1(w)}  (convex: |sigma'| <= 1).
Solve Xi_Eg = Xi_T2g = 0 (vertex M, then U) at m = 0.3, 0.1, 0.01.
Family F3(t, u, w): sigma' = (1-t-u) sigma'_{Gw(1.0,0.05)} + t sigma'_{Z1(w)} + u sigma'_{G(1.0)}; add mu_E = 0 (P62)."""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import *; from laws import *
from scipy.optimize import fsolve
T0 = time.time()
n = 1 << 14
G10 = G(1.0)
Z1cache = {}
def Z1w(w):
    w = float(w)
    if w not in Z1cache: Z1cache[w] = Z1(w)
    return Z1cache[w]
def fam2(t, w): return Mix([G10, Z1w(w)], [1-t, t], 'F2(t=%.6f,w=%.6f)' % (t, w))
def Gw(b, w): return ZLaw([1.0, 0.0], [b + w/2], w, 'Gw(%.2f,%.2f)' % (b, w))
Gw10 = Gw(1.0, 0.05)
def fam3(t, u, w): return Mix([Gw10, Z1w(w), G10], [1-t-u, t, u], 'F3(t=%.6f,u=%.6f,w=%.6f)' % (t, u, w))
def ev(L, m, nn=n, nu=1500):
    g, f = L.samples(nn); X = xi_all(g, f, m, nu=nu); X['mu_E'] = mu_E(g, f, m, nu=nu); return X
# scan F2 to see sign structure at m = 0.3
for m in [0.3]:
    for w in [0.06, 0.1]:
        print('F2 scan m=%.1f w=%.2f: ' % (m, w) + ' '.join('t=%.1f:(Eg %+.1e,T2g %+.1e)' % (t, *(lambda X: (X['M,Eg'], X['M,T2g']))(ev(fam2(t, w), m))) for t in [0.5, 0.7, 0.8, 0.9, 1.0]), flush=True)
sols = {}
for vtx in ['M', 'U']:
    for m in [0.3, 0.1, 0.01]:
        def F(p):
            t, w = p
            if not (0 < t <= 1 and 0.03 <= w <= 0.4): return [1.0, 1.0]
            X = ev(fam2(t, round(w, 6)), m); return [X[vtx + ',Eg']*1e4, X[vtx + ',T2g']*1e4]
        best = None
        for t0, w0 in [(0.9, 0.08), (0.95, 0.07), (0.85, 0.06), (0.97, 0.1), (0.8, 0.05)]:
            p, info, ier, msg = fsolve(F, [t0, w0], full_output=True, epsfcn=1e-6)
            r = np.abs(F(p)).max()
            if best is None or r < best[1]: best = (p, r)
        p = best[0]; L = fam2(p[0], round(p[1], 6)); X = ev(L, m, nn=1 << 16, nu=4000)
        sols[(vtx, m)] = p
        print('F2 zero vertex %s m=%.2f: t=%.6f w=%.6f | refined: Eg %+.2e T2g %+.2e (other vertex Eg %+.2e T2g %+.2e) mu_E %+.3e v_max %.6f max|s\'| %.6f'
              % (vtx, m, p[0], round(p[1], 6), X[vtx+',Eg'], X[vtx+',T2g'], X[('U' if vtx == 'M' else 'M')+',Eg'], X[('U' if vtx == 'M' else 'M')+',T2g'], X['mu_E'], L.vmax(m), np.abs(L.sp).max()), flush=True)
# mass dependence of the m=0.01 M solution
p = sols[('M', 0.01)]; L = fam2(p[0], round(p[1], 6))
print('M-zero tuned at m=0.01, evaluated at other m: ' + ' '.join('m=%g: Eg %+.3e T2g %+.3e' % (m, *(lambda X: (X['M,Eg'], X['M,T2g']))(ev(L, m, nn=1 << 15, nu=3000))) for m in [0.003, 0.01, 0.03, 0.1, 0.3]), flush=True)
# F3 with shear
for m in [0.3, 0.01]:
    print('Gw(1.0,0.05) mu_E m=%.2f: %+.3e' % (m, ev(Gw10, m)['mu_E']))
    def F3(p):
        t, u, w = p
        if not (0 < t and 0 <= u and t + u <= 1 and 0.03 <= w <= 0.4): return [1.0, 1.0, 1.0]
        X = ev(fam3(t, u, round(w, 6)), m); return [X['M,Eg']*1e4, X['M,T2g']*1e4, X['mu_E']*1e4]
    best = None
    for t0, u0, w0 in [(0.5, 0.1, 0.06), (0.6, 0.2, 0.07), (0.4, 0.3, 0.05), (0.7, 0.1, 0.08), (0.5, 0.4, 0.06)]:
        p, info, ier, msg = fsolve(F3, [t0, u0, w0], full_output=True, epsfcn=1e-6)
        r = np.abs(F3(p)).max()
        if best is None or r < best[1]: best = (p, r)
    p = best[0]; L = fam3(p[0], p[1], round(p[2], 6)); X = ev(L, m, nn=1 << 16, nu=4000)
    print('F3 zero (M, + shear) m=%.2f: t=%.6f u=%.6f w=%.6f resid %.1e | refined Eg %+.2e T2g %+.2e mu_E %+.2e | U: Eg %+.2e T2g %+.2e | v_max %.6f'
          % (m, p[0], p[1], round(p[2], 6), best[1], X['M,Eg'], X['M,T2g'], X['mu_E'], X['U,Eg'], X['U,T2g'], L.vmax(m)), flush=True)
print('runtime %.1fs' % (time.time()-T0))
