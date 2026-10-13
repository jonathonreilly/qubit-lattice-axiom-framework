"""R17-4 (b): search for one subluminal law in S with U-vertex Xi_Eg = Xi_T2g = Xi_face1 = 0 (then face2 = T2g = 0 and
body = 0 by the identities), at mass m. Free-segment family P(N) as R16-9's opt3: sigma' = 1 on [0,b]; N equal segments on
[b, pi-e] with values v_j in [-1,1]; flat on [pi-e, pi]; C^inf steps width wt (|sigma'| <= 1 exactly); sigma >= smin on the edge.
Phase 1: maximize min(Eg, T2g, face1) (SLSQP, epigraph). Phase 2: least-squares Newton on (Eg, T2g, face1) from the best points.
Usage: python3 opt4.py m N b wt nstarts seed"""
import numpy as np, sys, time; sys.path.insert(0, '.')
from zz import ZLaw
from fastU import rowsU
from scipy.optimize import minimize, least_squares
m = float(sys.argv[1]); N = int(sys.argv[2]); b = float(sys.argv[3]); wt = float(sys.argv[4]); NS = int(sys.argv[5]); seed = int(sys.argv[6])
e = 0.08; smin = 0.15; NF = 1 << 14; NN = 1 << 12; NU = 400
edges = np.linspace(b, np.pi - e, N + 1)
def law(v, nf=NF): return ZLaw([1.0] + list(v) + [0.0], list(edges), wt, 'P', nf=nf)
cache = {}
def get(v, nn=NN, nu=NU, nf=NF):
    key = (tuple(np.round(v, 12)), nn, nu, nf)
    if key not in cache:
        L = law(v, nf); g, f = L.samples(nn); R = rowsU(g, f, m, nu=nu, shear=True)
        cache[key] = (np.array([R['Eg'], R['T2g'], R['face1']]), R, L)
    return cache[key]
def sigfloor(v): L = get(v)[2]; return (L.sig[L.k >= b] - smin)[::128]
rng = np.random.default_rng(seed); T0 = time.time(); found = []
for s in range(NS):
    if s == 0: v0 = np.array([(-1.0)**(j+1) for j in range(N)])
    elif s == 1: v0 = np.array([[-1.0, 0.0, 1.0, 0.0][j % 4] for j in range(N)])   # zigzag with flats at turns
    elif s == 2: v0 = np.array([[-1.0, 0.0, 0.0, 1.0, 0.0, 0.0][j % 6] for j in range(N)])
    else: v0 = rng.choice([-1.0, 0.0, 1.0], N)*rng.uniform(0.5, 1, N)
    for it in range(60):
        if (sigfloor(v0) >= 0).all(): break
        v0 = np.clip(v0 + 0.15, -1, 1)
    x0 = np.append(v0, 1e4*get(v0)[0].min())
    cons = [{'type': 'ineq', 'fun': lambda x: 1e4*get(x[:-1])[0] - x[-1]}, {'type': 'ineq', 'fun': lambda x: sigfloor(x[:-1])}]
    try:
        r = minimize(lambda x: -x[-1], x0, method='SLSQP', bounds=[(-1, 1)]*N + [(-1e3, 1e3)], constraints=cons, options=dict(maxiter=100, ftol=1e-9))
    except Exception as ex:
        print('start %d failed: %s' % (s, ex)); continue
    v = r.x[:-1]; X, R, L = get(v)
    ok = (sigfloor(v) >= -1e-6).all()
    print('start %d: max-min phase: Eg %+.3e T2g %+.3e face1 %+.3e (K6row %+.3e, mu_E %+.3e) floor-ok=%s nit=%d v=%s (%.0fs)'
          % (s, *X, R['K6row'], R['mu_E'], ok, r.nit, np.round(v, 3).tolist(), time.time()-T0), flush=True)
    if ok and X.min() > -1e-9: found.append(v.copy())
print('starts with min(Eg,T2g,face1) >= 0: %d' % len(found))
for v in found[:3]:
    # phase 2: drive all three to zero (move toward the boundary), keeping the floor
    res = least_squares(lambda v: np.concatenate([1e4*get(v)[0], 10*np.minimum(sigfloor(v), 0)]), v, bounds=(-1, 1), xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=400)
    vz = res.x; X, R, L = get(vz, nn=1 << 15, nu=2000, nf=1 << 17)
    print('ZERO candidate (refined): Eg %+.3e T2g %+.3e face1 %+.3e body(=8face1/9+..) | mu_E %+.4e | vmax(m) %.6f max|sp| %.9f min edge g %.4f | v=%s'
          % (*X, R['mu_E'], L.vmax(m), np.abs(L.sp).max(), (L.sig[L.k >= b]**2).min(), np.round(vz, 6).tolist()), flush=True)
print('runtime %.0fs' % (time.time()-T0))
