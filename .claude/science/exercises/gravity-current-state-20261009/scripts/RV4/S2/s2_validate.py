"""Validate the S2 core against refereed numbers: F(1)=1.970388642e-3 (3D KG, p=sin k, E), T2 = 0, F(0.5)=2.467156e-3."""
import numpy as np, time
from s2_core import *
for d, L in [(3, 48), (3, 64)]:
    for M in [1.0, 0.5, 0.3]:
        t0 = time.time()
        Q = quad_forms(d, L, [(1, 0, 0)], lambda K: kg_vac(K, M))
        print(f"d={d} L={L} M={M}: mu_E={Q['E'][0,0]:+.10e} mu_T2={Q['T2'][0,0]:+.3e} mu_tr={Q['tr'][0,0]:+.10e}  ({time.time()-t0:.1f}s)")
print("refs: F(1)=1.970388642e-3, F(0.5)=2.467156e-3")
for L in [128, 256]:
    for M in [1.0, 0.3]:
        Q = quad_forms(2, L, [(1, 0)], lambda K: kg_vac(K, M))
        print(f"d=2 L={L} M={M}: mu_E={Q['E'][0,0]:+.10e} mu_T2={Q['T2'][0,0]:+.3e} mu_tr={Q['tr'][0,0]:+.10e}")
