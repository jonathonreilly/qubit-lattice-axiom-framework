import numpy as np, pickle
from walks import *
dat = pickle.load(open("nn_eqs_class0.pkl", "rb")); names, Bo = dat["names"], dat["B"].astype(float)
act = {"o00": 1, "o0i": 1j, "oi0": -1j, "oii": -1, "000": 1, "0ii": 1}
A = sum(v * Bo[names.index(k)] for k, v in act.items()) / 4
E = [idx(v) for v in corners if v[0] == 0]; O = [idx(v) for v in corners if v[0] == 1]
for kperp in [np.array([0., 0.]), np.array([0.7, -1.3]), np.array([np.pi, np.pi])]:
    InE = sum(A[i] * np.exp(1j * (n[1] * kperp[0] + n[2] * kperp[1])) for i, n in enumerate(OFFS) if n[0] == 0)[np.ix_(O, E)]
    OutE = sum(A[i] * np.exp(1j * (n[1] * kperp[0] + n[2] * kperp[1])) for i, n in enumerate(OFFS) if n[0] == 1)[np.ix_(O, E)]
    print(kperp, "rank In_E", np.linalg.matrix_rank(InE, 1e-9), "rank Out_E", np.linalg.matrix_rank(OutE, 1e-9),
          "sv In", np.round(np.linalg.svd(InE, compute_uv=False), 4), "sv Out", np.round(np.linalg.svd(OutE, compute_uv=False), 4))
