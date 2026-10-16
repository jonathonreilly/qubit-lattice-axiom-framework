"""Numerical search for unitary covariant walks (evidence only)."""
import json, sys, itertools
import numpy as np, sympy as sp
from scipy.optimize import least_squares
m = json.load(open(sys.argv[1])); P = m['P']
c = sp.symbols('c1:%d' % (P+1))
offs = list(itertools.product([-1,0,1], repeat=3))
coef = {}  # n -> array (P,8,8)
for n in offs:
    M = sp.Matrix([[sp.sympify(e) for e in row] for row in m['A'][str(n)]])
    coef[n] = np.array([[[float(sp.diff(M[i,j], c[p])) for j in range(8)] for i in range(8)] for p in range(P)])
def mats(x):
    return {n: np.tensordot(x, coef[n], 1) for n in offs}
def resid(xr):
    x = xr[:P] + 1j*xr[P:]
    A = mats(x); r = []
    for mm in itertools.product(range(-2,3), repeat=3):
        S = np.zeros((8,8), complex)
        for n in offs:
            n2 = tuple(a+b for a,b in zip(n,mm))
            if n2 in A: S += A[n].conj().T @ A[n2]
        if mm == (0,0,0): S -= np.eye(8)
        r += [S.real.ravel(), S.imag.ravel()]
    return np.concatenate(r)
def Wk(x, k):
    A = mats(x)
    return sum(A[n]*np.exp(1j*np.dot(k,n)) for n in offs)
rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv)>2 else 0)
sols = []
for t in range(int(sys.argv[3]) if len(sys.argv)>3 else 200):
    x0 = rng.normal(size=2*P)*rng.uniform(0.1,1)
    r = least_squares(resid, x0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
    if np.linalg.norm(r.fun) < 1e-9:
        x = r.x[:P]+1j*r.x[P:]
        # flatness: sorted eigenphase sets at several k
        specs = []
        for _ in range(6):
            k = rng.uniform(-np.pi, np.pi, 3)
            ev = np.linalg.eigvals(Wk(x,k))
            specs.append(np.sort(np.angle(ev)))
        # compare char polys instead (robust)
        cps = [np.poly(np.linalg.eigvals(Wk(x, rng.uniform(-np.pi,np.pi,3)))) for _ in range(6)]
        var = max(np.max(np.abs(cp-cps[0])) for cp in cps)
        sols.append((x, var))
        print("sol", t, "charpoly k-variation %.2e" % var, "|c|:", np.round(np.abs(x),4).tolist(), flush=True)
print("found", len(sols), "solutions; max k-variation", max([v for _,v in sols], default=None))
np.save(sys.argv[1].replace('.json','_numsols.npy'), np.array([s for s,_ in sols]))
