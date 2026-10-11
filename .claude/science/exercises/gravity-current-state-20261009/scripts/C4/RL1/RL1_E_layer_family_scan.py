"""RL1 (E): generalized 4D layer operators  B = alpha(-I + N),  N(x,y) = C[n(y,x)], n = 0..L-1  (BD: L=4, C ~ (1,-9,16,-8)).
Locality in the mean (no far-cone leakage, any nu): cone moments k=0,1,2 vanish:  sum_n C_n Gamma(n+(k+1)/2)/n! = 0.
Normalisation: ftilde_C(0) = 1 (cancels the -I).  Stability of the retarded MEAN inverse: no zero of S(z) = ftilde_C(z) - 1 in Re z > 0.
Also the diagonal-ladder (shared-path) VARIANCE growth rate z*: largest real root of rtilde(z) = 1, r = E[N^2] = e^{-m} sum C_n^2 m^n/n!.
rho = 1 (ell = 1).  Reports, per family member: #unstable zeros, max Re of mean zeros, ladder rate z*.
"""
import numpy as np
from scipy.special import kv, gammaln, gamma
from scipy.optimize import brentq
xg, wg = np.polynomial.legendre.leggauss(500)
TAU = 5.0*(xg+1); WT = 5.0*wg
M = np.pi*TAU**4/24

def basis(L):
    return np.array([np.exp(-M + n*np.log(np.maximum(M, 1e-300)) - gammaln(n+1)) for n in range(L)])  # e^-m m^n/n!

def trans(fvals, z):
    z = np.asarray(z, complex); x = z[..., None]*TAU
    K = kv(1, x)/x
    return 4*np.pi*np.tensordot(K*(WT*TAU**3), fvals.T, axes=([-1], [0]))   # shape z.shape + (L,)

def contour(x0=0.03, x1=8.0, y=12.0, n=1500):
    return np.concatenate([x0+1j*np.linspace(-y, y, n), np.linspace(x0, x1, n)+1j*y,
                           x1+1j*np.linspace(y, -y, n), np.linspace(x1, x0, n)-1j*y])

def analyse(C, Fb, Tc, path, Tsmall):
    C = np.asarray(C, float)
    f0 = (Tsmall @ C).real
    if abs(f0) < 1e-8: return None
    C = C/f0
    v = Tc @ C - 1.0
    ph = np.unwrap(np.angle(v)); nz = -round((ph[-1]-ph[0])/(2*np.pi))
    # z^2 coefficient
    c2 = -((Tz01 @ C).real - 1.0)/1e-4
    # ladder rate
    r = (Fb.T @ (C**2))
    rt = lambda z: 4*np.pi*np.sum(WT*TAU**3*r*kv(1, z*TAU)/(z*TAU)) - 1.0
    try: zs = brentq(rt, 1e-3, 40.0)
    except ValueError: zs = np.nan
    return nz, c2, zs, C

if __name__ == "__main__":
    path = contour()
    for L in [4, 5, 6]:
        Fb = basis(L)
        A = np.array([[np.exp(gammaln(n+(k+1)/2) - gammaln(n+1)) for n in range(L)] for k in range(3)])
        _, s, Vt = np.linalg.svd(A); null = Vt[3:]          # (L-3) x L
        Tc = trans(Fb, path); Tsmall = trans(Fb, np.array([1e-3]))[0]; Tz01 = trans(Fb, np.array([1e-2]))[0]
        globals()['Tz01'] = Tz01
        if L == 4:
            res = analyse(null[0], Fb, Tc, path, Tsmall)
            print("L=4 (BD): C = %s  unstable zeros=%d  c2=%.4f (sqrt6/4=%.4f)  ladder var rate z*=%.3f" %
                  (np.array2string(res[3]/res[3][0], precision=3), res[0], res[1], np.sqrt(6)/4, res[2]))
            continue
        stable = []; tot = 0
        if L == 5:
            params = [np.array([np.cos(t), np.sin(t)]) for t in np.linspace(0, np.pi, 721)[:-1]]
        else:
            params = [np.array([np.cos(t), np.sin(t)*np.cos(p), np.sin(t)*np.sin(p)])
                      for t in np.linspace(0, np.pi, 91) for p in np.linspace(0, 2*np.pi, 181)[:-1]]
        for q in params:
            res = analyse(q @ null, Fb, Tc, path, Tsmall)
            if res is None: continue
            tot += 1
            if res[0] == 0 and res[1] > 0: stable.append(res)
        print("L=%d: family members scanned=%d, stable (no zero in Re z>=0.03, |Im z|<=12, Re z<=8) with c2>0: %d" % (L, tot, len(stable)))
        for res in sorted(stable, key=lambda r: r[2])[:6]:
            print("   C = %s  c2=%.4f  ladder var rate z*=%.3f" % (np.array2string(res[3], precision=3), res[1], res[2]))
