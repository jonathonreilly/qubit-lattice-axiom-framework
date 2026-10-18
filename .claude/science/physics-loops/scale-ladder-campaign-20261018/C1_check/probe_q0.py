"""Probe: Q = 0 A1 on-site pairing -- where are the BdG zeros near each node, vs tau?  (grid in a ball + Nelder-Mead)"""
from cklib import *
from scipy.optimize import minimize
rng = np.random.default_rng(4242)
VA1 = onsite_channel(A1)
for trial in range(2):
    A1m = sum((rng.normal() + 1j * rng.normal()) * X for X in VA1); A1m /= np.linalg.norm(A1m)
    D = lambda ks: np.broadcast_to(A1m, (len(np.atleast_2d(ks)), 12, 12)).copy()
    for tau in (0.05, 0.2, 0.5):
        out = {}
        for n, K in NODES.items():
            g = np.linspace(-0.6, 0.6, 25); P = K + np.array(list(itertools.product(g, g, g)))
            v = gap0(P, D, tau, Q0); j = np.argmin(v)
            res = minimize(lambda k: gap0(k, D, tau, Q0)[0], P[j], method='Nelder-Mead', options=dict(xatol=1e-11, fatol=1e-15, maxiter=4000))
            out[n] = (res.fun, np.linalg.norm(res.x - K))
        print(f"trial {trial} tau={tau}: " + ", ".join(f"{NAME[n]}: min {v:.1e} at |dk|={d:.3f}" for n, (v, d) in out.items()), flush=True)
