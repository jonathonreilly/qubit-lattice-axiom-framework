"""R17-10 polish: re-optimize from stored points of ANY mode/cell (warm starts + perturbations), to test whether the
local maxima reported per cell are robust (nested problems must satisfy ge >= eq).  Copy of relaxK6.py otherwise.
Usage: python3 polish.py MODE m smin npert seed b dhi start1.npy start2.npy ...
OUTER relaxation for the K6 row (U vertex, E1): Lemma R_U extended by the sixth slope moment.
Per level bin j of the edge: M = int dk, P = int s^2 dk, Q = int s^4 dk, R = int s^6 dk  (u = s^2 in [0,1]).
Necessary per bin (truncated Hausdorff moment conditions for (M,P,Q,R) of a measure on u in [0,1], plus R16-9's coarea-CS):
  [[P,Q],[Q,R]] >= 0,  [[M-P, P-Q],[P-Q, Q-R]] >= 0,  [[M,P],[P,Q]] >= 0,  0 <= R <= Q <= P <= M,
  M*P >= |bin|^2 on visited bins [lo,hi] (coarea + Cauchy-Schwarz), M = 0 outside, sum_{l>=j} M_l <= pi - h_j (sigma <= k), sum M = pi - b.
Zone moments: E0 <- M, F2 <- P g, F4 <- Q g^2, F6 <- R g^3 (bin total placed at the bin node: NOT outward-rounded).
Mode 'ge':  maximize face1 subject to Eg >= 0, T2g >= 0.
Mode 'eq':  maximize -K/128 (= face1 at the zeros) subject to Eg = 0, T2g = 0.
If the maximum is >= 0 in some cell, this relaxation cannot certify the K6 conflict (relaxation gap exceeds the margin).
Usage: python3 relaxK6.py MODE m smin nstarts seed b dhi1 dhi2 ..."""
import numpy as np, sys, time
from math import gamma
from scipy.optimize import minimize
MODE = sys.argv[1]; m = float(sys.argv[2]); smin = float(sys.argv[3]); NS = int(sys.argv[4]); seed = int(sys.argv[5]); b = float(sys.argv[6]); DH = [float(sys.argv[7])]; STARTS = sys.argv[8:]
import os
CO = 0.0 if os.environ.get('NOCOAREA') else 1.0; NOSK = bool(os.environ.get('NOSK'))
L = int(os.environ.get('RLEV', '50')); lev = np.linspace(smin, np.pi, L); g = lev**2; DL = lev[1]-lev[0]; NV = 4*L
NU = 700; umax = np.log(80.0/min(m*m, 1.0)) + 2; u = np.linspace(-16.0, umax, NU); t = np.exp(u); du = u[1]-u[0]
w7 = t*du*t**2.5*np.exp(-t*m*m)/gamma(3.5); w5 = t*du*t**1.5*np.exp(-t*m*m)/gamma(2.5); w3 = t*du*t**0.5*np.exp(-t*m*m)/(12*gamma(1.5))
xg, wg = np.polynomial.legendre.leggauss(400)
El = np.exp(-np.outer(t, g))/np.pi; Z = np.zeros_like(El)
D = dict(E0=np.hstack([El, Z, Z, Z]), F2=np.hstack([Z, El*g, Z, Z]), F4=np.hstack([Z, Z, El*g**2, Z]), F6=np.hstack([Z, Z, Z, El*g**3]))
kb = 0.5*b*(xg+1); wb = 0.5*b*wg; Eb = np.exp(-np.outer(t, kb*kb))
Bx = {kk: Eb@(wb*kb**p)/np.pi for kk, p in [('E0', 0), ('F2', 2), ('F4', 4), ('F6', 6)]}
COEF = {'Eg': dict(a42=5/16, a222=-5/16, b4=-1/16, b22=1/16), 'T2g': dict(a222=5/8, b22=-1/8),
        'face1': dict(a6=-1/128, a42=45/128, a222=-5/16, b4=-3/64, b22=1/64), 'K6row': dict(a6=-1/128, a42=15/128, a222=-30/128)}
def full(x):
    E0, F2, F4, F6 = (Bx[k] + D[k]@x for k in ['E0', 'F2', 'F4', 'F6'])
    Q = dict(a6=(w7@(F6*E0*E0), dict(E0=2*w7*F6*E0, F6=w7*E0*E0)), a42=(w7@(F4*F2*E0), dict(E0=w7*F4*F2, F2=w7*F4*E0, F4=w7*F2*E0)),
             a222=(w7@F2**3, dict(F2=3*w7*F2**2)), b4=(w5@(F4*E0*E0), dict(E0=2*w5*F4*E0, F4=w5*E0*E0)), b22=(w5@(F2*F2*E0), dict(F2=2*w5*F2*E0, E0=w5*F2*F2)))
    val, grad = {}, {}
    for row, cf in COEF.items():
        val[row] = sum(c*Q[q][0] for q, c in cf.items())
        grad[row] = sum(c*sum(gv@D[k] for k, gv in Q[q][1].items()) for q, c in cf.items())
    val['mu'] = w3@(E0*(3*F2**2 - F4*E0))
    grad['mu'] = (w3*(3*F2**2 - 2*F4*E0))@D['E0'] + (w3*6*F2*E0)@D['F2'] - (w3*E0*E0)@D['F4']
    val['negmu'] = -val['mu']; grad['negmu'] = -grad['mu']
    return val, grad
I = np.eye(L); O = 0*I
Mv = lambda x: x[:L]; Pv = lambda x: x[L:2*L]; Qv = lambda x: x[2*L:3*L]; Rv = lambda x: x[3*L:]
A_lin = np.vstack([np.hstack([I, -I, O, O]), np.hstack([O, I, -I, O]), np.hstack([O, O, I, -I])])
def nl(x, ins):
    M, P, Q, R = Mv(x), Pv(x), Qv(x), Rv(x)
    c = np.concatenate([(P*R - Q*Q)[ins], ((M-P)*(Q-R) - (P-Q)**2)[ins], (M*Q - P*P)[ins], (M*P - CO*0.999*DL*DL)[ins]])
    dg = np.diag
    J = np.vstack([np.hstack([O, dg(R), dg(-2*Q), dg(P)])[ins],
                   np.hstack([dg(Q-R), dg(-(Q-R) - 2*(P-Q)), dg((M-P) + 2*(P-Q)), dg(-(M-P))])[ins],
                   np.hstack([dg(Q), dg(-2*P), dg(M), O])[ins],
                   np.hstack([dg(P), dg(M), O, O])[ins]])
    return c, J
rng = np.random.default_rng(seed); T0 = time.time(); overall = None
for dh in DH:
    hi = b + dh; lo = smin
    if hi > np.pi - 0.05: continue
    E = np.pi - b; ins = (lev >= lo - 1e-9) & (lev <= hi + 1e-9)
    bnds = [(0, None) if ins[j % L] else (0, 0) for j in range(NV)]
    hix = [j for j in range(L) if lev[j] > b]; Mt = np.zeros((len(hix), NV))
    for r_, j in enumerate(hix): Mt[r_, j:L] = 1
    rr = np.pi - lev[hix]
    cache = {}
    def F(x):
        kk = x.tobytes()
        if kk not in cache: cache.clear(); cache[kk] = full(x)
        return cache[kk]
    base = [{'type': 'eq', 'fun': lambda x: Mv(x).sum() - E, 'jac': lambda x: np.concatenate([np.ones(L), np.zeros(3*L)])},
            {'type': 'ineq', 'fun': lambda x: A_lin@x, 'jac': lambda x: A_lin},
            {'type': 'ineq', 'fun': lambda x: nl(x, ins)[0], 'jac': lambda x: nl(x, ins)[1]}]
    if hix and not NOSK: base.append({'type': 'ineq', 'fun': lambda x: rr - Mt@x, 'jac': lambda x: -Mt})
    best = None; zb = -1
    for s in range(len(STARTS) + NS):
        st = np.load(STARTS[s % len(STARTS)]); x0 = st*(1 + (0.0 if s < len(STARTS) else 0.05)*rng.standard_normal(NV)); x0 = np.clip(x0, 0, None)
        x0[:L] *= ins; x0[L:] *= np.tile(ins, 3); x0[:L] *= E/max(x0[:L].sum(), 1e-12)
        pad = lambda gv, zc: np.concatenate([gv, [zc]])
        c1 = [{'type': 'ineq', 'fun': (lambda y, r=r: 1e3*(F(y[:NV])[0][r] - y[-1])), 'jac': (lambda y, r=r: 1e3*pad(F(y[:NV])[1][r], -1.0))} for r in ['Eg', 'T2g']]
        for c_ in base:
            c1.append({'type': c_['type'], 'fun': (lambda y, c_=c_: c_['fun'](y[:NV])), 'jac': (lambda y, c_=c_: np.hstack([np.atleast_2d(c_['jac'](y[:NV])), np.zeros((np.atleast_2d(c_['jac'](y[:NV])).shape[0], 1))]).squeeze())})
        r1 = minimize(lambda y: -1e3*y[-1], np.concatenate([x0, [-1e-3]]), jac=lambda y: pad(np.zeros(NV), -1e3), method='SLSQP', bounds=bnds + [(-1, 1)], constraints=c1, options=dict(maxiter=300, ftol=1e-12))
        v1 = F(r1.x[:NV])[0]; z = min(v1['Eg'], v1['T2g']); zb = max(zb, z)
        if z < 0 and MODE != 'free': continue
        ctype = 'eq' if MODE in ('eq', 'mueq') else 'ineq'; obj = {'eq': 'K6row', 'mu': 'negmu', 'mueq': 'negmu'}.get(MODE, 'face1')
        c2 = ([] if MODE == 'free' else [{'type': ctype, 'fun': (lambda x, r=r: 1e3*F(x)[0][r]), 'jac': (lambda x, r=r: 1e3*F(x)[1][r])} for r in ['Eg', 'T2g']]) + base
        r2 = minimize(lambda x: -1e3*F(x)[0][obj], r1.x[:NV], jac=lambda x: -1e3*F(x)[1][obj], method='SLSQP', bounds=bnds, constraints=c2, options=dict(maxiter=500, ftol=1e-13))
        tol = 1e-10
        for x in (r2.x, r1.x[:NV]):          # phase-1 point is a valid fallback for 'ge'/'free' (feasibility re-checked)
            val, _ = full(x); cn, _ = nl(x, ins)
            feas = ((MODE == 'free' or (val['Eg'] > -tol and val['T2g'] > -tol)) and (MODE not in ('eq', 'mueq') or (abs(val['Eg']) < 1e-9 and abs(val['T2g']) < 1e-9))
                    and abs(Mv(x).sum()-E) < 1e-8 and (A_lin@x > -1e-9).all() and (cn > -1e-9).all() and (NOSK or not hix or (rr - Mt@x > -1e-9).all()))
            if feas and (best is None or val[obj] > best[0]): best = (val[obj], val, x.copy())
    if best is None:
        print('%s b=%.2f hi=%.2f m=%g: no feasible point found (best min(Eg,T2g) %+.3e) (%.0fs)' % (MODE, b, hi, m, zb, time.time()-T0), flush=True); continue
    ob, val, x = best
    M, P, Q, R = Mv(x), Pv(x), Qv(x), Rv(x); nz = M > 1e-6
    print('%s b=%.2f hi=%.2f m=%g: MAX %s %+.4e | Eg %+.2e T2g %+.2e face1 %+.3e K6row %+.3e mu_E %+.3e | edge P/M %.3f Q/M %.3f R/M %.3f (%.0fs)'
          % (MODE, b, hi, m, {'eq': 'K6row', 'mu': '-mu_E', 'mueq': '-mu_E'}.get(MODE, 'face1'), ob, val['Eg'], val['T2g'], val['face1'], val['K6row'], val['mu'], P.sum()/M.sum(), Q.sum()/M.sum(), R.sum()/M.sum(), time.time()-T0), flush=True)
    np.save('polish_%s_m%g_b%.2f_hi%.2f.npy' % (MODE, m, b, hi), x)
    if overall is None or ob > overall[0]: overall = (ob, hi)
print('OVERALL %s b=%.2f m=%g smin=%g: %s; runtime %.0fs' % (MODE, b, m, smin, 'none' if overall is None else '%+.4e (hi=%.2f)' % overall, time.time()-T0))
