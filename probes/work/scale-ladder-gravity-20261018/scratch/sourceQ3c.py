import sys, pickle, numpy as np
sys.path.insert(0, '.')
from sourceQ3 import C, reading, Tvec, HC
print("  |k|      count (T = e_t e_t)   conserved content (T = P e_t e_t P)   [Ward residual |W|/(|k||T|)]")
for kk in [np.array([0.02, -0.01, 0.015, 0.01j]), np.array([0.01, 0.0, 0.0, 0.02j]), np.array([0.004, 0.003, -0.002, 0.005j]), np.array([0.002, 0.0015, -0.001, 0.0025j])]:
    L = reading(kk); G = C.gauge(kk); Ga = sum(G[:, 4*t:4*t+4] for t in range(len(C.types))); LG = L @ Ga
    et = np.zeros(4); et[3] = 1.0; S = np.outer(et, et).astype(complex)
    Pi = np.eye(4) - np.outer(kk, kk)/(kk @ kk)         # bilinear transverse projector (complex k)
    Tq = Pi @ S @ Pi.T
    kn = np.linalg.norm(kk)
    r = lambda T: np.linalg.norm(Tvec(T) @ LG)/(kn*np.linalg.norm(Tvec(T)))
    print(f"  {kn:.4f}   {r(S):.3e}               {r(Tq):.3e}")
