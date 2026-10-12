"""R16-9 path-constrained scan for vertex U (and M as a cross-check): atoms at (level h_j, slope s_i), s_i in SG.
Not a strict relaxation for U (Xi_U depends on F4); it is a search over slope-quantized measures with the same
necessary path constraints as relaxed_path.py (occupation density >= 1 on the visited interval [lo,hi] ni b; sigma <= k).
Usage: python3 relaxed_pathU.py VTX m smin nstarts seed b1 b2 ..."""
import numpy as np, sys, time
from math import gamma
from scipy.optimize import minimize
VTX = sys.argv[1]; m = float(sys.argv[2]); smin = float(sys.argv[3]); NS = int(sys.argv[4]); seed = int(sys.argv[5]); BS = [float(x) for x in sys.argv[6:]]
SG = np.array([0.0, 0.4, 0.7, 0.85, 1.0]); NSG = len(SG)
L = 50; lev = np.linspace(smin, np.pi, L); g = lev**2; DL = lev[1]-lev[0]; NV = NSG*L
NU = 700; umax = np.log(80.0/min(m*m, 1.0)) + 2; u = np.linspace(-16.0, umax, NU); t = np.exp(u); du = u[1]-u[0]
cX = t*du*t**1.5*np.exp(-t*m*m)/(32*gamma(2.5)); cM = t*du*t**0.5*np.exp(-t*m*m)/(12*gamma(1.5))
xg, wg = np.polynomial.legendre.leggauss(400)
El = np.exp(-np.outer(t, g))/np.pi
D = dict(E0=np.hstack([El]*NSG), F2=np.hstack([El*g*s**2 for s in SG]), F4=np.hstack([El*g*g*s**4 for s in SG]),
         G1=np.hstack([El*g]*NSG), G2=np.hstack([El*g*g]*NSG))
lvl = np.tile(np.arange(L), NSG)
def setup(b):
    k = 0.5*b*(xg+1); w = 0.5*b*wg; Eb = np.exp(-np.outer(t, k*k))
    B0, B2, B4 = (Eb@(w*k**p)/np.pi for p in (0, 2, 4))
    return dict(E0=B0, F2=B2, F4=B4, G1=B2, G2=B4)
def full(x, Bx):
    Mo = {kk: Bx[kk] + D[kk]@x for kk in Bx}
    E0, F2, F4, G1, G2 = (Mo[kk] for kk in ['E0', 'F2', 'F4', 'G1', 'G2'])
    J = 2*t*F2 - E0
    if VTX == 'M': WE, WT = 2*(G2*E0 - G1**2), 4*G1**2
    else: WE, WT = 2*(F4*E0 - F2**2), 4*F2**2
    Q = E0*(3*F2**2 - F4*E0)
    dJ = 2*t[:, None]*D['F2'] - D['E0']
    if VTX == 'M':
        dWE = 2*(D['G2']*E0[:, None] + G2[:, None]*D['E0'] - 2*G1[:, None]*D['G1']); dWT = 8*G1[:, None]*D['G1']
    else:
        dWE = 2*(D['F4']*E0[:, None] + F4[:, None]*D['E0'] - 2*F2[:, None]*D['F2']); dWT = 8*F2[:, None]*D['F2']
    dQ = D['E0']*(3*F2**2 - F4*E0)[:, None] + E0[:, None]*(6*F2[:, None]*D['F2'] - D['F4']*E0[:, None] - F4[:, None]*D['E0'])
    return (cX@(WE*J), cX@(WT*J), cM@Q), (cX@(dWE*J[:, None] + WE[:, None]*dJ), cX@(dWT*J[:, None] + WT[:, None]*dJ), cM@dQ)
rng = np.random.default_rng(seed); T0 = time.time(); allbest = None
combos = []
for b in BS:
    los = sorted(set([smin] + [x for x in [0.3] if smin <= x <= b + 1e-9]))
    his = [b + d for d in [0.5, 0.75, 1.0, 1.5, 2.0] if b + d <= np.pi - 0.05]
    combos += [(b, lo, hi) for lo in los for hi in his if (b - lo) + (hi - b) <= np.pi - b - 0.02]
for (b, lo, hi) in combos:
    Bx = setup(b); E = np.pi - b; best = None
    inside = (lev >= lo - 1e-9) & (lev <= hi + 1e-9); ins = inside[lvl]
    bnds = [(0, None) if ins[j] else (0, 0) for j in range(NV)]
    Min = np.zeros((inside.sum(), NV))
    for r_, j in enumerate(np.where(inside)[0]): Min[r_, lvl == j] = 1
    cache = {}
    def F(x):
        kk = x.tobytes()
        if kk not in cache: cache.clear(); cache[kk] = full(x, Bx)
        return cache[kk]
    cons = [{'type': 'ineq', 'fun': lambda x: 1e3*F(x)[0][0], 'jac': lambda x: 1e3*F(x)[1][0]},
            {'type': 'ineq', 'fun': lambda x: 1e3*F(x)[0][1], 'jac': lambda x: 1e3*F(x)[1][1]},
            {'type': 'eq', 'fun': lambda x: x.sum() - E, 'jac': lambda x: np.ones_like(x)},
            {'type': 'ineq', 'fun': lambda x, M=Min: M@x - DL*0.999, 'jac': lambda x, M=Min: M}]
    hix = [j for j in range(L) if lev[j] > b]
    if hix:
        Mt = np.zeros((len(hix), NV))
        for r_, j in enumerate(hix): Mt[r_, lvl >= j] = 1
        cons.append({'type': 'ineq', 'fun': lambda x, M=Mt, r=np.pi - lev[hix]: r - M@x, 'jac': lambda x, M=Mt: -M})
    for s in range(NS):
        x0 = (rng.exponential(1.0, NV)*(rng.uniform(size=NV) < rng.uniform(0.05, 0.6)) + DL/NSG)*ins; x0 *= E/x0.sum()
        r = minimize(lambda x: 1e2*F(x)[0][2], x0, jac=lambda x: 1e2*F(x)[1][2], method='SLSQP', bounds=bnds, constraints=cons, options=dict(maxiter=400, ftol=1e-12))
        (Eg, T2, mu), _ = full(r.x, Bx)
        feas = Eg > -1e-10 and T2 > -1e-10 and abs(r.x.sum()-E) < 1e-8 and (Min@r.x >= DL*0.998).all()
        if feas and (best is None or mu < best[0]): best = (mu, Eg, T2, r.x.copy(), r.status)
    if best is None: print('b=%.2f lo=%.2f hi=%.2f: no feasible point found' % (b, lo, hi), flush=True); continue
    mu, Eg, T2, x, st = best
    smass = [x[i*L:(i+1)*L].sum() for i in range(NSG)]
    print('%s b=%.2f lo=%.2f hi=%.2f m=%g: MIN mu_E %+.5e (Eg %+.1e T2g %+.1e st %d) | mass by slope %s (%.0fs)' % (VTX, b, lo, hi, m, mu, Eg, T2, st, ' '.join('%.2f:%.3f' % (s_, ms) for s_, ms in zip(SG, smass)), time.time()-T0), flush=True)
    if allbest is None or mu < allbest[0]: allbest = (mu, (b, lo, hi))
print('OVERALL %s min mu_E %+.5e at (b,lo,hi)=%s; runtime %.0fs' % (VTX, allbest[0], str(allbest[1]), time.time()-T0))
