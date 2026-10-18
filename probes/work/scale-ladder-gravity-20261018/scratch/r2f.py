import sys, numpy as np
sys.path.insert(0, '.')
from r2 import R2
from r2c import comp_inv, K, HC, itt, ixx
D15 = [K.evec[c] for c in range(K.E)]
l = np.array([np.linalg.norm(v) for v in D15])
for lam in (-0.1, -1.0):
    row = []
    for kk in [np.array([0, 0.04, 0, 0.0]), np.array([0, 0.02, 0, 0.0]), np.array([0, 0.01, 0, 0.0]), np.array([0, 0.012, 0.009, 0.0])]:
        k2 = kk @ kk; Qk = K.Q(kk) + lam*R2(K, kk); M = K.line_map(kk)
        W = np.eye(len(l))
        L = np.linalg.pinv(W @ M) @ W
        T = np.zeros(10); T[itt] = 1.0
        x = comp_inv(Qk, K.gauge(kk), L.conj().T @ T); h = L @ x
        row.append(f"{h[itt].real*k2:+.4f}/{(h[ixx]/h[itt]).real:+.3f}")
    print(f"Kuhn lambda={lam:+.1f}: h_tt k^2 / (h_xx/h_tt) at |k| = 0.04, 0.02, 0.01, 0.015(off-axis): " + "  ".join(row))
