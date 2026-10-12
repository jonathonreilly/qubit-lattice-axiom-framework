"""RL1 (F4b; left contour edge sampled densely near Im z = 0 to resolve the fast phase winding next to the double zero at z = 0):
RL1 (F4): stability re-scan with a RESOLVED quadrature (1500 Gauss nodes on tau in [0,10]) and the contour [0.003,20] x [-12,12].
Zeros with |z| > 12 are excluded analytically: for large |z| in Re z >= 0, ftilde(z) ~ 8 pi f(0)/z^4 (small-tau expansion,
f(0) = C_0), so |S + 1| << 1 there (ARGUED, asymptotic).  The 500-node runs (RL1_E/F/F3) under-resolve K_1 oscillations at
|Im z| > ~30, which produced spurious odd counts.  Exact in-script coefficients; normalised at z = 1e-3 (artificial real zero
at ~1e-3 lies left of the contour)."""
import numpy as np
from scipy.special import kv, gammaln
xg, wg = np.polynomial.legendre.leggauss(1500)
TAU = 5.0*(xg+1); WT = 5.0*wg; M = np.pi*TAU**4/24
def basis(L): return np.array([np.exp(-M + n*np.log(np.maximum(M, 1e-300)) - gammaln(n+1)) for n in range(L)])
def trans(Fb, z):
    z = np.asarray(z, complex); out = np.zeros(z.shape + (Fb.shape[0],), complex)
    for i0 in range(0, z.size, 2000):
        zz = z.ravel()[i0:i0+2000]; x = zz[:, None]*TAU
        out.reshape(-1, Fb.shape[0])[i0:i0+2000] = 4*np.pi*((kv(1, x)/x)*(WT*TAU**3)) @ Fb.T
    return out
def cont(x0, x1, y0, y1, n):
    s = np.linspace(-1, 1, 8*n); yl = y1*np.sign(s)*np.abs(s)**4          # left edge: dense near Im z = 0 (double zero at z = 0)
    return np.concatenate([x0+1j*yl, np.linspace(x0, x1, n)+1j*y1,
                           x1+1j*np.linspace(y1, y0, n), np.linspace(x1, x0, n)+1j*y0])
boxes = {"main [0.03,20]x[-12,12]": cont(0.03, 20, -12, 12, 2500), "near-axis [0.003,0.03]x[-12,12]": cont(0.003, 0.03, -12, 12, 2500)}
for L in [4, 5, 6]:
    Fb = basis(L)
    A_ = np.array([[np.exp(gammaln(n+(k+1)/2) - gammaln(n+1)) for n in range(L)] for k in range(3)])
    null = np.linalg.svd(A_)[2][3:]
    Tb = {k: trans(Fb, p) for k, p in boxes.items()}; T0 = trans(Fb, np.array([1e-3]))[0]
    if L == 4: params = [np.array([1.0])]
    elif L == 5: params = [np.array([np.cos(t), np.sin(t)]) for t in np.linspace(0, np.pi, 361)[:-1]]
    else: params = [np.array([np.cos(t), np.sin(t)*np.cos(p), np.sin(t)*np.sin(p)])
                    for t in np.linspace(0, np.pi, 61) for p in np.linspace(0, 2*np.pi, 121)[:-1]]
    hist = {}; stable = []
    for q in params:
        C = q @ null; f0 = (T0 @ C).real
        if abs(f0) < 1e-6: continue
        C = C/f0
        ns = []
        for k, T in Tb.items():
            ph = np.unwrap(np.angle(T @ C - 1.0)); ns.append(-int(round((ph[-1]-ph[0])/(2*np.pi))))
        hist[tuple(ns)] = hist.get(tuple(ns), 0) + 1
        if sum(ns) == 0: stable.append(C)
    print("L=%d: members=%d  {(#zeros main box, #zeros near-axis strip): count} = %s  -> stable: %d"
          % (L, sum(hist.values()), dict(sorted(hist.items())), len(stable)))
    for C in stable[:3]: print("    stable C =", np.array2string(C, precision=5))
    if stable: np.save("RL1_F4b_stable_L%d.npy" % L, np.array(stable))
