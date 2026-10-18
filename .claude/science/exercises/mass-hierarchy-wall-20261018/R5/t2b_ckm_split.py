#!/usr/bin/env python3
"""R5 T2b (added after T2 output was seen; disclosed): CKM in the left-right symmetric split.
Mass exponent = a_L + a_R with a_L = a_R = p/2 (code pattern shared by doublet and singlet), so V_ij ~ eps^{(p_i-p_j)/2}
at the SAME eps that fits the masses under model A."""
import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location('t2', 't2_data.py')
src = open('t2_data.py').read().split("rng = np.random.default_rng")[0]
ns = {}; exec(src, ns)
SETS, SECT, PAT, S, sector_err, CKM = ns['SETS'], ns['SECT'], ns['PAT'], ns['S'], ns['sector_err'], ns['CKM']
t = np.log([CKM['us'], CKM['cb'], CKM['ub']])
for name, m in SETS.items():
    X = np.log(np.array([[m[k] for k in sec] for sec in SECT]))
    row = []
    for pn, p in PAT.items():
        e = np.stack([sector_err(X[f], p, S) for f in range(3)], -1).max(-1)
        k = e.argmin(); s = S[k]
        a = 0.5 * np.array([p[0]-p[1], p[1]-p[2], p[0]-p[2]], float)
        V = np.exp(a * s)
        fac = np.exp(np.abs(a * s - t))
        row.append(f"{pn}: mass x{np.exp(e[k]):.2f}; V(us,cb,ub)=({V[0]:.3f},{V[1]:.3f},{V[2]:.4f}) worst x{fac.max():.2f}")
    print(name, ' | '.join(row))
