"""R16-9 relaxed (Young-measure) problem for the scalar edge, vertex M (and U on an s-grid).
A law in S (R14-3/R16-3 class) induces a measure on (sigma, s=|sigma'|) of total mass pi: box sigma=k on [0,b] (s=1) plus an edge
of mass pi-b on levels sigma in [smin, pi]. For vertex M, Xi_M depends on the measure only through E0, F2 (f^2 = s^2 g), G1, G2,
so replacing each (g, s) by the mixture p = s^2 at (g, s=1) and 1-p at (g, s=0) keeps Xi_M,Eg and Xi_M,T2g and lowers mu_E
(F4: p g^2 >= s^4 g^2; mu_E integrand E0(3F2^2 - F4 E0)). Dropping the path (connectivity) constraint only enlarges the set.
So   min{ mu_E : Xi_M,Eg >= 0, Xi_M,T2g >= 0 } over the relaxed set  <=  the same min over S (at fixed m, b-range, smin).
Variables: b, masses a_l (s=1) and c_l (s=0) at L levels. Usage: python3 relaxed.py VTX m smin bmin nstarts seed"""
import numpy as np, sys, time
from math import gamma
from scipy.optimize import minimize
VTX = sys.argv[1]; m = float(sys.argv[2]); smin = float(sys.argv[3]); bmin = float(sys.argv[4]); NS = int(sys.argv[5]); seed = int(sys.argv[6])
SGRID = [0.0, 1.0] if VTX == 'M' else [0.0, 0.5, 0.75, 1.0]
L = 48; lev = np.linspace(smin, np.pi, L); NSG = len(SGRID)
xg, wg = np.polynomial.legendre.leggauss(400)
NU = 700; umax = np.log(80.0/min(m*m, 1.0)) + 2; u = np.linspace(-16.0, umax, NU); t = np.exp(u); du = u[1]-u[0]
def moments(b, A):            # A: (NSG, L) masses
    k = 0.5*b*(xg+1); w = 0.5*b*wg
    Eb = np.exp(-np.outer(t, k*k))
    g = lev*lev
    El = np.exp(-np.outer(t, g))          # (NU, L)
    mass = A.sum(0); s2 = (np.array(SGRID)[:, None]**2*A).sum(0); s4 = (np.array(SGRID)[:, None]**4*A).sum(0)
    E0 = (Eb@w + El@mass)/np.pi
    F2 = (Eb@(w*k**2) + El@(s2*g))/np.pi
    F4 = (Eb@(w*k**4) + El@(s4*g*g))/np.pi
    G1 = (Eb@(w*k**2) + El@(mass*g))/np.pi
    G2 = (Eb@(w*k**4) + El@(mass*g*g))/np.pi
    return E0, F2, F4, G1, G2
_C = {}
def evalq(x):
    key = x.tobytes()
    if key in _C: return _C[key]
    if len(_C) > 5000: _C.clear()
    _C[key] = _evalq(x); return _C[key]
def _evalq(x):
    b = x[0]; A = np.abs(x[1:]).reshape(NSG, L)
    A = A*(np.pi - b)/A.sum()
    E0, F2, F4, G1, G2 = moments(b, A)
    J = 2*t*F2 - E0; base = t*du*t**1.5*np.exp(-t*m*m)*J/(32*gamma(2.5))
    if VTX == 'M': We, Wt = 2*(G2*E0 - G1**2), 4*G1**2
    else: We, Wt = 2*(F4*E0 - F2**2), 4*F2**2
    mu = np.sum(t*du*t**0.5*np.exp(-t*m*m)*E0*(3*F2**2 - F4*E0))/(12*gamma(1.5))
    return float(np.sum(base*We)), float(np.sum(base*Wt)), float(mu), b, A
rng = np.random.default_rng(seed); T0 = time.time(); best = None
obj = lambda x: 1e2*evalq(x)[2]
cons = [{'type': 'ineq', 'fun': lambda x: 1e3*evalq(x)[0]}, {'type': 'ineq', 'fun': lambda x: 1e3*evalq(x)[1]}]
bnds = [(bmin, np.pi-0.05)] + [(1e-9, None)]*(NSG*L)
for s in range(NS):
    x0 = np.concatenate([[rng.uniform(bmin, 1.6)], rng.exponential(1.0, NSG*L)*(rng.uniform(size=NSG*L) < 0.3) + 1e-6])
    r = minimize(obj, x0, method='SLSQP', bounds=bnds, constraints=cons, options=dict(maxiter=200, ftol=1e-10))
    Eg, T2, mu, b, A = evalq(r.x)
    feas = Eg > -1e-9 and T2 > -1e-9
    top = np.argsort(-A.ravel())[:5]
    desc = ', '.join('s=%.2f lev=%.2f mass=%.3f' % (SGRID[i // L], lev[i % L], A.ravel()[i]) for i in top)
    print('start %2d: mu_E %+.4e Eg %+.2e T2g %+.2e feas=%s b=%.3f nit=%d | top atoms: %s' % (s, mu, Eg, T2, feas, b, r.nit, desc), flush=True)
    if feas and (best is None or mu < best[0]): best = (mu, Eg, T2, b, A)
if best: print('BEST relaxed: mu_E %+.5e Eg %+.2e T2g %+.2e b %.3f' % best[:4])
print('runtime %.0fs' % (time.time()-T0))
