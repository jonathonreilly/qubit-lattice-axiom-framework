"""R16-9 Lemma R_U: a relaxation for BOTH vertices (U and M) that contains every law in S.
Per level bin j of the edge: M_j = int dk, P_j = int s^2 dk, Q_j = int s^4 dk (s = |sigma'|). Every law satisfies
  0 <= Q_j <= P_j <= M_j,  P_j^2 <= Q_j M_j (Cauchy-Schwarz),  M_j P_j >= (bin width)^2 on the visited interval [lo,hi] (coarea:
  int |sigma'| dk over the level band >= its width, and int s dk <= sqrt(M P)),  M_j = 0 outside [lo,hi],  sum_{l>=j} M_l <= pi - h_j (sigma<=k),
and the zone moments are E0,G1,G2 <- M, F2 <- P g, F4 <- Q g^2. Xi_v and mu_E are functions of these moments only, so
  min{mu_E : Xi_v,Eg >= 0, Xi_v,T2g >= 0} over this set <= the same over S (level discretization aside). Two-phase SLSQP, exact gradients.
Usage: python3 relaxed_UV.py VTX m smin nstarts seed b hi_offsets..."""
import numpy as np, sys, time
from math import gamma
from scipy.optimize import minimize
VTX = sys.argv[1]; m = float(sys.argv[2]); smin = float(sys.argv[3]); NS = int(sys.argv[4]); seed = int(sys.argv[5]); b = float(sys.argv[6]); HIS = [float(x) for x in sys.argv[7:]]
L = 50; lev = np.linspace(smin, np.pi, L); g = lev**2; DL = lev[1]-lev[0]
NU = 700; umax = np.log(80.0/min(m*m, 1.0)) + 2; u = np.linspace(-16.0, umax, NU); t = np.exp(u); du = u[1]-u[0]
cX = t*du*t**1.5*np.exp(-t*m*m)/(32*gamma(2.5)); cM = t*du*t**0.5*np.exp(-t*m*m)/(12*gamma(1.5))
xg, wg = np.polynomial.legendre.leggauss(400)
El = np.exp(-np.outer(t, g))/np.pi; Z = np.zeros_like(El)
D = dict(E0=np.hstack([El, Z, Z]), F2=np.hstack([Z, El*g, Z]), F4=np.hstack([Z, Z, El*g*g]), G1=np.hstack([El*g, Z, Z]), G2=np.hstack([El*g*g, Z, Z]))
k = 0.5*b*(xg+1); w = 0.5*b*wg; Eb = np.exp(-np.outer(t, k*k)); B0, B2, B4 = (Eb@(w*k**p)/np.pi for p in (0, 2, 4))
Bx = dict(E0=B0, F2=B2, F4=B4, G1=B2, G2=B4); E = np.pi - b; NV = 3*L
def full(x):
    Mo = {kk: Bx[kk] + D[kk]@x for kk in Bx}; E0, F2, F4, G1, G2 = (Mo[kk] for kk in ['E0', 'F2', 'F4', 'G1', 'G2'])
    J = 2*t*F2 - E0; dJ = 2*t[:, None]*D['F2'] - D['E0']
    if VTX == 'M':
        WE, WT = 2*(G2*E0 - G1**2), 4*G1**2
        dWE = 2*(D['G2']*E0[:, None] + G2[:, None]*D['E0'] - 2*G1[:, None]*D['G1']); dWT = 8*G1[:, None]*D['G1']
    else:
        WE, WT = 2*(F4*E0 - F2**2), 4*F2**2
        dWE = 2*(D['F4']*E0[:, None] + F4[:, None]*D['E0'] - 2*F2[:, None]*D['F2']); dWT = 8*F2[:, None]*D['F2']
    Q = E0*(3*F2**2 - F4*E0)
    dQ = D['E0']*(3*F2**2 - F4*E0)[:, None] + E0[:, None]*(6*F2[:, None]*D['F2'] - D['F4']*E0[:, None] - F4[:, None]*D['E0'])
    return (cX@(WE*J), cX@(WT*J), cM@Q), (cX@(dWE*J[:, None] + WE[:, None]*dJ), cX@(dWT*J[:, None] + WT[:, None]*dJ), cM@dQ)
rng = np.random.default_rng(seed); T0 = time.time()
I = np.eye(L)
for hoff in HIS:
    hi = b + hoff; lo = smin
    if hi > np.pi - 0.05: continue
    ins = (lev >= lo - 1e-9) & (lev <= hi + 1e-9); nin = ins.sum()
    bnds = [(0, None) if ins[j % L] else (0, 0) for j in range(NV)]
    cache = {}
    def F(x):
        kk = x.tobytes()
        if kk not in cache: cache.clear(); cache[kk] = full(x)
        return cache[kk]
    Mv = lambda x: x[:L]; Pv = lambda x: x[L:2*L]; Qv = lambda x: x[2*L:]
    A_MP = np.hstack([I, -I, 0*I]); A_PQ = np.hstack([0*I, I, -I])
    hix = [j for j in range(L) if lev[j] > b]
    Mt = np.zeros((len(hix), NV))
    for r_, j in enumerate(hix): Mt[r_, j:L] = 1
    base = [{'type': 'eq', 'fun': lambda x: Mv(x).sum() - E, 'jac': lambda x: np.concatenate([np.ones(L), np.zeros(2*L)])},
            {'type': 'ineq', 'fun': lambda x: A_MP@x, 'jac': lambda x: A_MP},
            {'type': 'ineq', 'fun': lambda x: A_PQ@x, 'jac': lambda x: A_PQ},
            {'type': 'ineq', 'fun': lambda x: (Qv(x)*Mv(x) - Pv(x)**2)[ins], 'jac': lambda x: np.hstack([np.diag(Qv(x)), np.diag(-2*Pv(x)), np.diag(Mv(x))])[ins]},
            {'type': 'ineq', 'fun': lambda x: (Mv(x)*Pv(x) - 0.999*DL*DL)[ins], 'jac': lambda x: np.hstack([np.diag(Pv(x)), np.diag(Mv(x)), 0*I])[ins]}]
    if hix: base.append({'type': 'ineq', 'fun': lambda x: (np.pi - lev[hix]) - Mt@x, 'jac': lambda x: -Mt})
    best = None; zb = -1
    for s in range(NS):
        Mm = (DL + rng.exponential(1.0, L)*(rng.uniform(size=L) < rng.uniform(0.1, 0.7)))*ins; Mm *= E/Mm.sum()
        s2 = rng.uniform(0.3, 1.0, L); Pm = Mm*np.maximum(s2, (DL*DL/np.maximum(Mm, 1e-12))/np.maximum(Mm, 1e-12)).clip(0, 1); Qm = Pm*np.clip(Pm/np.maximum(Mm, 1e-12), 0, 1)*1.05
        Qm = np.minimum(Qm, Pm); x0 = np.concatenate([Mm, Pm, Qm])
        pad = lambda gv, zc: np.concatenate([gv, [zc]])
        cons1 = [{'type': 'ineq', 'fun': lambda y: 1e3*(F(y[:NV])[0][0] - y[-1]), 'jac': lambda y: 1e3*pad(F(y[:NV])[1][0], -1.0)},
                 {'type': 'ineq', 'fun': lambda y: 1e3*(F(y[:NV])[0][1] - y[-1]), 'jac': lambda y: 1e3*pad(F(y[:NV])[1][1], -1.0)}]
        for c_ in base:
            cons1.append({'type': c_['type'], 'fun': (lambda y, c_=c_: c_['fun'](y[:NV])), 'jac': (lambda y, c_=c_: np.hstack([np.atleast_2d(c_['jac'](y[:NV])), np.zeros((np.atleast_2d(c_['jac'](y[:NV])).shape[0], 1))]))})
        r1 = minimize(lambda y: -1e3*y[-1], np.concatenate([x0, [-1e-3]]), jac=lambda y: pad(np.zeros(NV), -1e3), method='SLSQP', bounds=bnds + [(-1, 1)], constraints=cons1, options=dict(maxiter=300, ftol=1e-12))
        x1 = r1.x[:NV]; zmax = min(full(x1)[0][:2]); zb = max(zb, zmax)
        if zmax < 0: continue
        cons = [{'type': 'ineq', 'fun': lambda x: 1e3*F(x)[0][0], 'jac': lambda x: 1e3*F(x)[1][0]},
                {'type': 'ineq', 'fun': lambda x: 1e3*F(x)[0][1], 'jac': lambda x: 1e3*F(x)[1][1]}] + base
        r = minimize(lambda x: 1e2*F(x)[0][2], x1, jac=lambda x: 1e2*F(x)[1][2], method='SLSQP', bounds=bnds, constraints=cons, options=dict(maxiter=400, ftol=1e-12))
        x = r.x; (Eg, T2, mu), _ = full(x)
        ok = Eg > -1e-10 and T2 > -1e-10 and abs(Mv(x).sum() - E) < 1e-7 and (A_MP@x > -1e-9).all() and (A_PQ@x > -1e-9).all() \
             and ((Qv(x)*Mv(x) - Pv(x)**2)[ins] > -1e-9).all() and ((Mv(x)*Pv(x))[ins] > 0.998*DL*DL).all()
        if ok and (best is None or mu < best[0]): best = (mu, Eg, T2, x.copy(), r.status)
    if best is None: print('%s b=%.2f lo=%.2f hi=%.2f m=%g: no point with both Xi >= 0 found; best min(Xi_Eg,Xi_T2g) = %+.3e (%.0fs)' % (VTX, b, lo, hi, m, zb, time.time()-T0), flush=True); continue
    mu, Eg, T2, x, st = best
    print('%s b=%.2f lo=%.2f hi=%.2f m=%g: MIN mu_E %+.5e (Eg %+.1e T2g %+.1e st %d) | edge M %.3f, P/M %.3f, Q/M %.3f (%.0fs)'
          % (VTX, b, lo, hi, m, mu, Eg, T2, st, Mv(x).sum(), Pv(x).sum()/Mv(x).sum(), Qv(x).sum()/Mv(x).sum(), time.time()-T0), flush=True)
