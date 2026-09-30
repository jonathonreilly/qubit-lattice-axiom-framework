import numpy as np, warnings
from test_C3_winding import *
coef = fourier_coeffs(); M = hop_matrices(coef); Qs = build_Q_nz(M)
ks = 2*np.pi*np.arange(201)/200
smin = []
for kz in ks:
    Q = sum(np.exp(1j*kz*nz)*Qn for nz, Qn in Qs.items())
    s = np.linalg.svd(Q, compute_uv=False)
    smin.append(s.min())
print("min over kz of smallest singular value of dressed Q:", min(smin), " max of largest:", None)
# where do warnings come from
with warnings.catch_warnings():
    warnings.simplefilter("error")
    for i, kz in enumerate(ks):
        Q = sum(np.exp(1j*kz*nz)*Qn for nz, Qn in Qs.items())
        try:
            np.linalg.slogdet(Q)
        except Exception as e:
            print("warning at index", i, "kz =", kz, "->", e); break
    else:
        print("no warnings in slogdet loop")
