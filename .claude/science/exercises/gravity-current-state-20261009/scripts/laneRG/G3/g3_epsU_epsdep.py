"""Strain-amplitude dependence of the sawtooth-flow T2 split (is the normal-class response analytic, ~eps^2, or cusped, ~|eps|?).
Prints raw I_N(eps)-I_N(0), I_U(eps)-I_U(0) and their ratios to eps^2 and |eps|."""
import numpy as np, time
from g3_epsU_mu import classes
t0 = time.time()
L, m = 15, 1.0
base = classes(L, m, 0.0, 'T2', 'saw')
for kind in ['saw', 'sin']:
    b0 = classes(L, m, 0.0, 'T2', kind)
    for e in [0.01, 0.02, 0.04, 0.08]:
        vp = classes(L, m, e, 'T2', kind); vm = classes(L, m, -e, 'T2', kind)
        d = 0.5*(vp + vm) - b0
        print(f"flow {kind} L={L} eps={e:.2f}: dI_N={d[0]:+.4e} dI_U={d[1]:+.4e} | dI/eps^2 = [{d[0]/e**2:+.4e}, {d[1]/e**2:+.4e}]  "
              f"dI/|eps| = [{d[0]/e:+.4e}, {d[1]/e:+.4e}]  [{time.time()-t0:.0f}s]", flush=True)
