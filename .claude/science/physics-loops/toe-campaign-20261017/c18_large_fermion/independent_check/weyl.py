"""Item 5 follow-up: O x T invariant, I*K-breaking second-neighbour hops. Verify O invariance,
then locate the band minimum of the perturbed model."""
import numpy as np
from scipy.optimize import minimize
from perturb import *
rng = np.random.default_rng(5)
res = candidates(rng)
p = (-1.0, 0.1, -0.5)
inv_m = 0.043224
for pick in (0, 24, 26):
    kinds, c2, sh, zn, nrm, ikb, hops = res[pick]
    print(f"term: path {kinds} 0->{CORN[c2]}@{sh} amp {zn}; breaks I*K: {ikb>1e-9}")
    err = 0
    for R, eta, s, S in PS:
        W = Wmat(R, eta)
        for k in rng.uniform(-np.pi, np.pi, (3, 3)):
            err = max(err, np.abs(Xsym(hops, R @ k + np.pi * S) - W @ Xsym(hops, k) @ W.T).max())
    herm = max(np.abs(Xsym(hops, k) - Xsym(hops, k).conj().T).max() for k in rng.uniform(-np.pi, np.pi, (3, 3)))
    # translation invariance is built in (Bloch form); gauge covariance: amplitudes carry the u-string
    print(f"   O-invariance residual {err:.1e}, hermiticity residual {herm:.1e}")
    for delta in (0.005, 0.02):
        H = lambda k: bloch(u, k, *p) + delta * Xsym(hops, k)
        e0 = lambda k: np.linalg.eigvalsh(H(k))[0]
        a = e0(KP); b = e0(-KP); ks = KP if a < b else -KP
        q = 1e-4; ed = [np.linalg.eigvalsh(H(ks + q * d)) for d in (np.array([1., 0, 0]), np.ones(3) / 3**.5)]
        alpha = [(e[1] - e[0]) / (2 * q) for e in ed]
        Ek = e0(ks)
        best = None
        for k0 in list(ks + rng.normal(0, 0.3, (30, 3))) + list(rng.uniform(-np.pi, np.pi, (20, 3))):
            r = minimize(e0, k0, method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-13, maxiter=20000))
            if best is None or r.fun < best.fun: best = r
        dk = np.linalg.norm(((best.x - ks + np.pi) % (2*np.pi)) - np.pi)
        print(f"   delta={delta}: deg at k* {np.linalg.eigvalsh(H(ks))[1]-Ek:.1e}; alpha([100],[111]) = {np.round(alpha,5)};"
              f" band min at |k-k*|={dk:.4f} (m* alpha = {alpha[0]/inv_m:.4f}), E(k*)-Emin = {Ek-best.fun:.2e}"
              f" (m* alpha^2/2 = {alpha[0]**2/inv_m/2:.2e})")
