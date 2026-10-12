"""R16-9 relaxed problem, vertex M, with exact gradients (b fixed per run). Measure: box [0,b] (s=1) + masses a_l (s=1, f^2=g)
and c_l (s=0, f=0) at L levels in [smin, pi], sum = pi - b. By the mixture argument (relaxed.py docstring) this set lower-bounds
mu_E at given (Xi_M,Eg, Xi_M,T2g) over every law in S with that box and valley floor >= smin (path constraint dropped).
Minimize mu_E s.t. Xi_M,Eg >= 0, Xi_M,T2g >= 0. Usage: python3 relaxed_path.py m smin nstarts seed b1 b2 ...
PATH VERSION: also imposes the necessary occupation constraint: the edge visits a level interval [lo, hi] containing b
(continuity), total mass density >= 1 per unit level on it (each crossing at |slope| <= 1), and no mass outside it."""
import numpy as np, sys, time
from math import gamma
from scipy.optimize import minimize
m = float(sys.argv[1]); smin = float(sys.argv[2]); NS = int(sys.argv[3]); seed = int(sys.argv[4]); BS = [float(x) for x in sys.argv[5:]]
L = 60; lev = np.linspace(smin, np.pi, L); g = lev**2
NU = 700; umax = np.log(80.0/min(m*m, 1.0)) + 2; u = np.linspace(-16.0, umax, NU); t = np.exp(u); du = u[1]-u[0]
cX = t*du*t**1.5*np.exp(-t*m*m)/(32*gamma(2.5)); cM = t*du*t**0.5*np.exp(-t*m*m)/(12*gamma(1.5))
xg, wg = np.polynomial.legendre.leggauss(400)
El = np.exp(-np.outer(t, g))/np.pi                     # (NU, L)
# d(moment)/d(a_l), d(moment)/d(c_l): columns
dA = dict(E0=El, F2=El*g, F4=El*g*g, G1=El*g, G2=El*g*g)
dC = dict(E0=El, F2=0*El, F4=0*El, G1=El*g, G2=El*g*g)
def setup(b):
    k = 0.5*b*(xg+1); w = 0.5*b*wg; Eb = np.exp(-np.outer(t, k*k))
    B0, B2, B4 = (Eb@(w*k**p)/np.pi for p in (0, 2, 4))
    return dict(E0=B0, F2=B2, F4=B4, G1=B2, G2=B4)
def full(x, Bx):
    a, c = x[:L], x[L:]
    M = {kk: Bx[kk] + dA[kk]@a + dC[kk]@c for kk in Bx}
    E0, F2, F4, G1, G2 = M['E0'], M['F2'], M['F4'], M['G1'], M['G2']
    J = 2*t*F2 - E0; WE = 2*(G2*E0 - G1**2); WT = 4*G1**2; Q = E0*(3*F2**2 - F4*E0)
    vals = (cX@(WE*J), cX@(WT*J), cM@Q)
    grads = []
    for D in (dA, dC):
        dJ = 2*t[:, None]*D['F2'] - D['E0']
        dWE = 2*(D['G2']*E0[:, None] + G2[:, None]*D['E0'] - 2*G1[:, None]*D['G1']); dWT = 8*G1[:, None]*D['G1']
        dQ = D['E0']*(3*F2**2 - F4*E0)[:, None] + E0[:, None]*(6*F2[:, None]*D['F2'] - D['F4']*E0[:, None] - F4[:, None]*D['E0'])
        grads.append((cX@(dWE*J[:, None] + WE[:, None]*dJ), cX@(dWT*J[:, None] + WT[:, None]*dJ), cM@dQ))
    gE = np.concatenate([grads[0][0], grads[1][0]]); gT = np.concatenate([grads[0][1], grads[1][1]]); gM = np.concatenate([grads[0][2], grads[1][2]])
    return vals, (gE, gT, gM)
rng = np.random.default_rng(seed); T0 = time.time(); allbest = None
DL = lev[1]-lev[0]
combos = []
for b in BS:
    los = [smin]
    his = [b + d for d in [0.0, 0.25] if b + d <= np.pi - 0.05]
    combos += [(b, lo, hi) for lo in los for hi in his if (b - lo) + (hi - b) <= np.pi - b - 0.02]
for (b, lo, hi) in combos:
    Bx = setup(b); E = np.pi - b; best = None
    inside = (lev >= lo - 1e-9) & (lev <= hi + 1e-9)
    bnds = [(0, None) if inside[j % L] else (0, 0) for j in range(2*L)]
    Min = np.zeros((inside.sum(), 2*L)); 
    for r_, j in enumerate(np.where(inside)[0]): Min[r_, j] = 1; Min[r_, L+j] = 1
    # gradient check once
    x0 = rng.exponential(1.0, 2*L); x0 *= E/x0.sum(); v0, g0 = full(x0, Bx); h = 1e-6; e5 = np.zeros(2*L); e5[5] = h; e5[L+7] = h
    v1, _ = full(x0 + e5, Bx)
    if (b, lo, hi) == combos[0]: print('grad check: %s vs %s' % (np.round((np.array(v1)-np.array(v0))/h, 6), np.round([gg[5]+gg[L+7] for gg in g0], 6)))
    cache = {}
    def F(x):
        kk = x.tobytes()
        if kk not in cache: cache.clear(); cache[kk] = full(x, Bx)
        return cache[kk]
    cons = [{'type': 'ineq', 'fun': lambda x: 1e3*F(x)[0][0], 'jac': lambda x: 1e3*F(x)[1][0]},
            {'type': 'ineq', 'fun': lambda x: 1e3*F(x)[0][1], 'jac': lambda x: 1e3*F(x)[1][1]},
            {'type': 'eq', 'fun': lambda x: x.sum() - E, 'jac': lambda x: np.ones_like(x)}]
    # necessary path constraint sigma(k) <= k: edge mass at levels >= h is <= pi - h for every h > b
    hix = [j for j in range(L) if lev[j] > b]
    if hix:
        Mtail = np.zeros((len(hix), 2*L))
        for r_, j in enumerate(hix): Mtail[r_, j:L] = 1; Mtail[r_, L+j:2*L] = 1
        rhs = np.pi - lev[hix]
        cons.append({'type': 'ineq', 'fun': lambda x, M=Mtail, r=rhs: r - M@x, 'jac': lambda x, M=Mtail: -M})
    cons.append({'type': 'ineq', 'fun': lambda x, M=Min: M@x - DL*0.999, 'jac': lambda x, M=Min: M})
    for s in range(NS):
        x0 = rng.exponential(1.0, 2*L)*(rng.uniform(size=2*L) < rng.uniform(0.05, 0.6)) + 1e-4
        x0 = x0*inside[np.arange(2*L) % L] + DL*inside[np.arange(2*L) % L]; x0 *= E/x0.sum()
        r = minimize(lambda x: 1e2*F(x)[0][2], x0, jac=lambda x: 1e2*F(x)[1][2], method='SLSQP', bounds=bnds, constraints=cons, options=dict(maxiter=500, ftol=1e-12))
        (Eg, T2, mu), _ = full(r.x, Bx)
        feas = Eg > -1e-10 and T2 > -1e-10 and abs(r.x.sum()-E) < 1e-8 and (Min@r.x >= DL*0.998).all()
        if feas and (best is None or mu < best[0]): best = (mu, Eg, T2, r.x.copy(), r.nit, r.status)
    if best is None: print('b=%.2f lo=%.2f hi=%.2f: no feasible point found' % (b, lo, hi), flush=True); continue
    mu, Eg, T2, x, nit, st = best
    a, c = x[:L], x[L:]
    top = lambda v: ', '.join('%.2f:%.3f' % (lev[i], v[i]) for i in np.argsort(-v)[:4] if v[i] > 1e-3)
    print('b=%.2f lo=%.2f hi=%.2f m=%g smin=%.2f: MIN mu_E %+.5e (Eg %+.1e T2g %+.1e; status %d nit %d) | fast mass %.3f [%s] | flat mass %.3f [%s] (%.0fs)'
          % (b, lo, hi, m, smin, mu, Eg, T2, st, nit, a.sum(), top(a), c.sum(), top(c), time.time()-T0), flush=True)
    if allbest is None or mu < allbest[0]: allbest = (mu, (b, lo, hi))
print('OVERALL min mu_E %+.5e at (b,lo,hi)=%s; runtime %.0fs' % (allbest[0], str(allbest[1]), time.time()-T0))
