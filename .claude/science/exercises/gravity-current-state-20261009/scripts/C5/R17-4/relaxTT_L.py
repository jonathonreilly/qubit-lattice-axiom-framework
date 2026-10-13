"""R17-4 (b): slope-resolved occupation-measure search (R16-9 relaxed_pathU4 constraints: coarea per visited level bin,
sigma <= k, edge mass pi - b; slopes {0,.2,.4,.6,.8,.9,1}; 40 levels on [smin, pi]) for the U vertex:
 phase 1: maximize min(Xi_Eg, Xi_T2g); phase 2: maximize Xi_face1 subject to Xi_Eg >= 0, Xi_T2g >= 0.
If max face1 < 0 in every cell, the off-axis row cannot be zeroed together with the axis rows in this search (not a relaxation).
Usage: python3 relaxTT.py m smin nstarts seed b dhi1 dhi2 ..."""
import numpy as np, sys, time
from math import gamma
from scipy.optimize import minimize
m = float(sys.argv[1]); smin = float(sys.argv[2]); NS = int(sys.argv[3]); seed = int(sys.argv[4]); b = float(sys.argv[5]); DH = [float(x) for x in sys.argv[6:]]
import os
SG = np.array([float(x) for x in os.environ.get("RSG", "0,0.2,0.4,0.6,0.8,0.9,1").split(",")]); NSG = len(SG)
L = int(os.environ.get("RLEV", "40")); lev = np.linspace(smin, np.pi, L); g = lev**2; DL = lev[1]-lev[0]; NV = NSG*L
NU = 600; umax = np.log(80.0/min(m*m, 1.0)) + 2; u = np.linspace(-16.0, umax, NU); t = np.exp(u); du = u[1]-u[0]
w7 = t*du*t**2.5*np.exp(-t*m*m)/gamma(3.5); w5 = t*du*t**1.5*np.exp(-t*m*m)/gamma(2.5)
xg, wg = np.polynomial.legendre.leggauss(400)
El = np.exp(-np.outer(t, g))/np.pi
D = dict(E0=np.hstack([El]*NSG), F2=np.hstack([El*g*s**2 for s in SG]), F4=np.hstack([El*g**2*s**4 for s in SG]), F6=np.hstack([El*g**3*s**6 for s in SG]))
lvl = np.tile(np.arange(L), NSG)
kb = 0.5*b*(xg+1); wb = 0.5*b*wg; Eb = np.exp(-np.outer(t, kb*kb))
Bx = {kk: Eb@(wb*kb**p)/np.pi for kk, p in [('E0', 0), ('F2', 2), ('F4', 4), ('F6', 6)]}
COEF = {'Eg': dict(a42=5/16, a222=-5/16, b4=-1/16, b22=1/16), 'T2g': dict(a222=5/8, b22=-1/8),
        'face1': dict(a6=-1/128, a42=45/128, a222=-5/16, b4=-3/64, b22=1/64)}
def full(x):
    E0, F2, F4, F6 = (Bx[k] + D[k]@x for k in ['E0', 'F2', 'F4', 'F6'])
    Q = dict(a6=(w7@(F6*E0*E0), dict(E0=2*w7*F6*E0, F6=w7*E0*E0)), a42=(w7@(F4*F2*E0), dict(E0=w7*F4*F2, F2=w7*F4*E0, F4=w7*F2*E0)),
             a222=(w7@F2**3, dict(F2=3*w7*F2**2)), b4=(w5@(F4*E0*E0), dict(E0=2*w5*F4*E0, F4=w5*E0*E0)), b22=(w5@(F2*F2*E0), dict(F2=2*w5*F2*E0, E0=w5*F2*F2)))
    val, grad = {}, {}
    for row, cf in COEF.items():
        val[row] = sum(c*Q[q][0] for q, c in cf.items())
        grad[row] = sum(c*sum(gv@D[k] for k, gv in Q[q][1].items()) for q, c in cf.items())
    mu = (t*du*t**0.5*np.exp(-t*m*m)/(12*gamma(1.5)))@(E0*(3*F2**2 - F4*E0))
    return val, grad, mu
rng = np.random.default_rng(seed); T0 = time.time(); overall = None
for dh in DH:
    hi = b + dh; lo = smin
    if hi > np.pi - 0.05: continue
    E = np.pi - b; inside = (lev >= lo - 1e-9) & (lev <= hi + 1e-9); ins = inside[lvl]
    bnds = [(0, None) if ins[j] else (0, 0) for j in range(NV)]
    slp = np.repeat(SG, L); Min = np.zeros((inside.sum(), NV))
    for r_, j in enumerate(np.where(inside)[0]): Min[r_, lvl == j] = slp[lvl == j]
    hix = [j for j in range(L) if lev[j] > b]; Mt = np.zeros((len(hix), NV))
    for r_, j in enumerate(hix): Mt[r_, lvl >= j] = 1
    rr = np.pi - lev[hix]
    cache = {}
    def F(x):
        kk = x.tobytes()
        if kk not in cache: cache.clear(); cache[kk] = full(x)
        return cache[kk]
    base_cons = [{'type': 'eq', 'fun': lambda x: x.sum() - E, 'jac': lambda x: np.ones_like(x)},
                 {'type': 'ineq', 'fun': lambda x: Min@x - DL*0.999, 'jac': lambda x: Min},
                 {'type': 'ineq', 'fun': lambda x: rr - Mt@x, 'jac': lambda x: -Mt}]
    best = None; zb = -1
    for s in range(NS):
        base = np.zeros(NV); base[(NSG-1)*L:][inside] = DL
        extra = rng.exponential(1.0, NV)*(rng.uniform(size=NV) < rng.uniform(0.05, 0.6))*ins
        rem = E - base.sum()
        if rem < 0: break
        x0 = base + extra*rem/max(extra.sum(), 1e-12)
        pad = lambda gv, zc: np.concatenate([gv, [zc]])
        c1 = [{'type': 'ineq', 'fun': (lambda y, r=r: 1e3*(F(y[:NV])[0][r] - y[-1])), 'jac': (lambda y, r=r: 1e3*pad(F(y[:NV])[1][r], -1.0))} for r in ['Eg', 'T2g']]
        for c_ in base_cons:
            c1.append({'type': c_['type'], 'fun': (lambda y, c_=c_: c_['fun'](y[:NV])), 'jac': (lambda y, c_=c_: np.hstack([np.atleast_2d(c_['jac'](y[:NV])), np.zeros((np.atleast_2d(c_['jac'](y[:NV])).shape[0], 1))]).squeeze())})
        r1 = minimize(lambda y: -1e3*y[-1], np.concatenate([x0, [-1e-3]]), jac=lambda y: pad(np.zeros(NV), -1e3), method='SLSQP', bounds=bnds + [(-1, 1)], constraints=c1, options=dict(maxiter=300, ftol=1e-12))
        v1 = F(r1.x[:NV])[0]; z = min(v1['Eg'], v1['T2g']); zb = max(zb, z)
        if z < 0: continue
        c2 = [{'type': 'ineq', 'fun': (lambda x, r=r: 1e3*F(x)[0][r]), 'jac': (lambda x, r=r: 1e3*F(x)[1][r])} for r in ['Eg', 'T2g']] + base_cons
        r2 = minimize(lambda x: -1e3*F(x)[0]['face1'], r1.x[:NV], jac=lambda x: -1e3*F(x)[1]['face1'], method='SLSQP', bounds=bnds, constraints=c2, options=dict(maxiter=400, ftol=1e-13))
        x = r2.x; val, _, mu = full(x)
        feas = val['Eg'] > -1e-10 and val['T2g'] > -1e-10 and abs(x.sum()-E) < 1e-8 and (Min@x >= DL*0.998).all() and (rr - Mt@x >= -1e-9).all()
        if feas and (best is None or val['face1'] > best[0]): best = (val['face1'], val, mu, x.copy())
    if best is None:
        print('b=%.2f hi=%.2f m=%g: no point with Eg,T2g >= 0 found (best min %+.3e) (%.0fs)' % (b, hi, m, zb, time.time()-T0), flush=True); continue
    f1, val, mu, x = best
    sm = [x[i*L:(i+1)*L].sum() for i in range(NSG)]
    print('b=%.2f hi=%.2f m=%g: MAX face1 %+.4e at Eg %+.1e T2g %+.1e (mu_E %+.3e) | mass by slope %s (%.0fs)' % (b, hi, m, f1, val['Eg'], val['T2g'], mu, ' '.join('%.1f:%.3f' % (s_, q) for s_, q in zip(SG, sm)), time.time()-T0), flush=True)
    if overall is None or f1 > overall[0]: overall = (f1, hi)
print('OVERALL b=%.2f m=%g: max face1 at a graviton-axis-feasible point = %s; runtime %.0fs' % (b, m, 'none' if overall is None else '%+.4e (hi=%.2f)' % overall, time.time()-T0))
