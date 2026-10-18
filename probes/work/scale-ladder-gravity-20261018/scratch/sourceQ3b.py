import sys, pickle, numpy as np
sys.path.insert(0, '.')
from sourceQ3 import C, reading, Tvec, HC
for kk in [np.array([0.02, -0.01, 0.015, 0.01j]), np.array([0.01, 0.0, 0.0, 0.02j]), np.array([0.004, 0.003, -0.002, 0.005j])]:
    L = reading(kk); G = C.gauge(kk); nt = len(C.types)
    Ga = sum(G[:, 4*t:4*t+4] for t in range(nt))          # uniform displacement (lattice diffeo)
    LG = L @ Ga                                            # 10 x 4: metric change from a uniform displacement
    T = np.zeros((4, 4), complex); T[3, 3] = 1.0
    ks = kk[:3]; kt = kk[3]; Tq = T.copy(); ti = -(kt*T[3, 3])*ks/np.dot(ks, ks)
    for i in range(3): Tq[i, 3] = Tq[3, i] = ti[i]
    kn = np.linalg.norm(kk)
    Wc = np.abs(Tvec(T) @ LG); Wq = np.abs(Tvec(Tq) @ LG)
    print(f"|k|={kn:.4f}: Ward residual |W|/(|k||T|): count {np.linalg.norm(Wc)/(kn*np.linalg.norm(Tvec(T))):.3e}   content {np.linalg.norm(Wq)/(kn*np.linalg.norm(Tvec(Tq))):.3e}")
