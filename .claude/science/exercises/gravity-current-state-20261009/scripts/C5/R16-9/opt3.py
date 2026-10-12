"""R16-9 (a), gravity side on one scalar edge: minimize mu_E subject to Xi_Eg >= 0 and Xi_T2g >= 0 (vertex VTX) at mass m,
over the free-segment family P(N): sigma' = 1 on [0,b]; N equal segments on [b, pi-e] with values v_j in [-1,1];
flat (0) on [pi-e, pi]; C^inf steps of width wt (convex blends => |sigma'| <= 1 exactly). Constraint sigma >= smin on the edge
(no extra zero of g, i.e. no light doubler). If min mu_E < 0 is reached with both Xi >= 0, a triple zero follows by mixing
(done in triple.py). Usage: python3 opt3.py VTX m N b wt nstarts seed"""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import *
from scipy.optimize import minimize
VTX = sys.argv[1]; m = float(sys.argv[2]); N = int(sys.argv[3]); b = float(sys.argv[4]); wt = float(sys.argv[5])
NS = int(sys.argv[6]); seed = int(sys.argv[7]); e = 0.08; smin = 0.15
NF = 1 << 14; NN = 1 << 12; NU = 400
edges = np.linspace(b, np.pi - e, N + 1)
def law(v, nf=NF):
    vals = [1.0] + list(v) + [0.0]; bks = list(edges) 
    return ZLaw(vals, bks, wt, 'P', nf=nf)
def ev(v, nn=NN, nu=NU, nf=NF):
    L = law(v, nf); g, f = L.samples(nn); X = xi_all(g, f, m, nu=nu); mu = mu_E(g, f, m, nu=nu)
    return X[VTX+',Eg'], X[VTX+',T2g'], mu, L
cache = {}
def get(v):
    key = tuple(np.round(v, 12))
    if key not in cache: cache[key] = ev(v)
    return cache[key]
obj = lambda v: 1e2*get(v)[2]
cons = [{'type': 'ineq', 'fun': lambda v: 1e3*get(v)[0]}, {'type': 'ineq', 'fun': lambda v: 1e3*get(v)[1]},
        {'type': 'ineq', 'fun': lambda v: (get(v)[3].sig[get(v)[3].k >= b] - smin)[::256]}]
rng = np.random.default_rng(seed); T0 = time.time(); best = None
for s in range(NS):
    if s == 0: v0 = np.array([(-1.0)**(j+1) for j in range(N)])        # pure zigzag start
    elif s == 1: v0 = np.array([-1.0]*2 + [(-1.0)**(j+1) for j in range(N-2)])
    else: v0 = rng.uniform(-1, 1, N)
    # repair start to satisfy sigma >= smin roughly
    for it in range(50):
        L = law(v0); 
        if (L.sig[L.k >= b] >= smin).all(): break
        v0 = np.clip(v0 + 0.2, -1, 1)
    cache.clear()
    try:
        r = minimize(obj, v0, method='SLSQP', bounds=[(-1, 1)]*N, constraints=cons, options=dict(maxiter=80, ftol=1e-7))
    except Exception as ex:
        print('start %d failed: %s' % (s, ex)); continue
    Eg, T2, mu, L = get(r.x)
    feas = Eg >= -1e-7 and T2 >= -1e-7 and (L.sig[L.k >= b] >= smin - 1e-6).all()
    print('start %d: mu_E %+.4e  %s,Eg %+.3e %s,T2g %+.3e feas=%s  nit=%d  v=%s  (%.0fs)' % (s, mu, VTX, Eg, VTX, T2, feas, r.nit, np.round(r.x, 3).tolist(), time.time()-T0), flush=True)
    if feas and (best is None or mu < best[0]): best = (mu, r.x.copy())
if best is not None:
    mu, v = best; Eg, T2, mu2, L = ev(v, nn=1 << 15, nu=2000, nf=1 << 17)
    print('BEST (refined nf=2^17,nn=2^15,nu=2000): mu_E %+.5e %s,Eg %+.4e %s,T2g %+.4e vmax %.6f max|sp| %.9f min edge g %.4f v=%s' % (mu2, VTX, Eg, VTX, T2, L.vmax(m), np.abs(L.sp).max(), (L.sig[L.k >= b]**2).min(), np.round(v, 6).tolist()))
print('runtime %.0fs' % (time.time()-T0))
