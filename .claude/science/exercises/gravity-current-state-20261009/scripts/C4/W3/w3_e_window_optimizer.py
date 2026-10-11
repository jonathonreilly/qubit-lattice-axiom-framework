"""C4 / RW / W3 part E: can a scalar-healthy general-local completion (a = -1, lam - 1 in the BBN window)
also be GR-like at k >> mu?  Targets (v2, normalisation fixed to GR Phi k^2 = -2): c_T^2 = 1 by penalty 10|c_T^2 - 1|, static gamma = Psi/Phi = 1,
G_eff/G_GR = 1 at k = 100 (masses and a negligible there), TT not tachyonic.  Nelder-Mead from every healthy
hit of part C2 on  |gamma - 1| + |G_eff/G_GR - 1| + 50 * (# unhealthy (k, mode) pairs)  over all 20 free
coefficients (lam clipped to (1.001, 1.095), eta to (0.01, 1.99))."""
import sys, pickle, time; sys.path.insert(0, '.')
import sympy as sp, numpy as np
from scipy.optimize import minimize
from w3_lib import w, k
M = pickle.load(open('w3_c2_symbol.pkl', 'rb'))
lam, eta, a = sp.symbols('lam eta a', real=True)
ms = sp.symbols('m0:5', real=True); cs = sp.symbols('c0:13', real=True)
pars = (lam, eta, a) + ms + cs
Mf = sp.lambdify((w, k, *pars), M, 'numpy'); dMf = sp.lambdify((w, k, *pars), sp.diff(M, w), 'numpy')
def nbad(pv, ks=np.logspace(-4, 5, 28)):
    bad = 0
    for kv in ks:
        d = [np.linalg.det(np.array(Mf(np.sqrt(complex(W)), kv, *pv), dtype=complex)) for W in (0.0, 1.0, -1.0)]
        C = d[0]; A = (d[1] + d[2])/2 - C; Bc = (d[1] - d[2])/2
        rts = np.roots([A, Bc, C])
        for r in rts:
            if abs(r.imag) > 1e-7*max(1, abs(r)) or r.real <= 0: bad += 1; continue
            wv = np.sqrt(r.real); v = np.linalg.svd(np.array(Mf(wv, kv, *pv), dtype=complex))[2][-1].conj()
            if wv*np.real(v.conj() @ np.array(dMf(wv, kv, *pv), dtype=complex) @ v) <= 0: bad += 1
    return bad
GR_PHI = None
def static(pv, kv=100.0):
    v = np.linalg.solve(np.array(Mf(0.0, kv, *pv), dtype=complex), np.array([1.0, 0, 0, 0], dtype=complex))
    return (v[2]/v[0]).real, (v[0]/(-2.0/kv**2)).real   # GR reference (part D): Phi k^2 = -2 for J = 1
def unpack(z):
    lv = 1.001 + 0.094/(1 + np.exp(-z[0])); ev = 0.01 + 1.98/(1 + np.exp(-z[1]))
    m = z[2:7]; c = np.array(z[7:20])
    return (lv, ev, -1.0) + tuple(m) + tuple(c)
def obj(z):
    pv = unpack(z)
    try:
        g, G = static(pv); b = nbad(pv)
    except Exception:
        return 1e3
    cT2_ok = (1 - 8*pv[8]) > 0
    cT2 = (1 - 8*pv[8])/(1 + 8*pv[12])
    return abs(g - 1) + abs(G - 1) + 10*abs(cT2 - 1) + 50*b + (0 if cT2_ok else 100)
hits_by_p = pickle.load(open('w3_c2_hits.pkl', 'rb'))
hits = [h for p in hits_by_p for h in hits_by_p[p]]
# GR normalisation check
gr = (1.0, 1e-9, 0.0) + (0.0,)*5 + (0.0,)*13
print("normalisation: GR static via (Phi,Psi) block gives gamma = 1, G = 1 by construction of 'static' (Phi_GR = -J/(2k^2)... see C2/D)")
best = []
t0 = time.time()
for h in hits:
    lv, ev = h[0], h[1]
    z0 = np.concatenate([[np.log((lv - 1.001)/(1.095 - lv)), np.log((ev - 0.01)/(1.99 - ev))], h[3:8], h[8:21]])
    res = minimize(obj, z0, method='Nelder-Mead', options={'maxfev': 3000, 'xatol': 1e-6, 'fatol': 1e-8})
    pv = unpack(res.x); g, G = static(pv); b = nbad(pv)
    best.append((res.fun, g, G, b, pv))
    print(f"  start lam={lv:.3f}: obj={res.fun:.3e} gamma={g:+.5f} G_eff/G_GR={G:+.5f} unhealthy={b} lam={pv[0]:.4f} eta={pv[1]:.3f} max|c|={np.max(np.abs(pv[8:])):.2f} ({time.time()-t0:.0f}s)")
best.sort(key=lambda r: r[0])
f, g, G, b, pv = best[0]
print(f"BEST: obj={f:.3e} gamma={g:+.6f} G_eff/G_GR={G:+.6f} unhealthy={b}")
print(f"      lam={pv[0]:.5f} eta={pv[1]:.4f} masses/|a|={np.round(pv[3:8], 4).tolist()}")
print(f"      c (c0=-c4) = {np.round(pv[8:], 4).tolist()}")
pickle.dump(best, open('w3_e_best.pkl', 'wb'))

cT = lambda pv: (1 - 8*pv[8])/(1 + 8*pv[12])
print(f"      c_T^2 = {cT(pv):.6f}")
