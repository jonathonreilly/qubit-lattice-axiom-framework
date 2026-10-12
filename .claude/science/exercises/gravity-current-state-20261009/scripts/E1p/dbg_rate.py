import numpy as np
from E1p_5_mean4d import conv_nodes, A
def run(m, taumax, h):
    taus = np.unique(np.concatenate([np.arange(0, 8, 0.02), np.arange(8, taumax + h, h)]))
    K = np.zeros_like(taus); W = np.zeros_like(taus); b = -m * m
    for i, tau in enumerate(taus):
        P1 = np.exp(-np.pi * tau**4 / 24)
        if i == 0:
            K[i] = A; W[i] = A * A; continue
        t1, w = conv_nodes(tau)
        K[i] = A * P1 + A * b * np.sum(w * np.interp(t1, taus[:i], K[:i]))
        K2 = K[i] - A * P1
        S = A * A * P1 + K2 * K2
        W[i] = S + b * b * A * A * np.sum(w * np.interp(t1, taus[:i], W[:i]))
    return taus, K, W
ref = np.load("../out/mean4d_ml0.1.npz")
for h in [1.0, 0.25, 0.05]:
    taus, K, W = run(0.1, 200.0, h)
    V = W - K**2
    for t in [20, 50, 100, 150, 200]:
        i = np.argmin(abs(taus - t)); j = np.argmin(abs(ref['taus'] - t))
        print(f"h={h} tau={taus[i]:.0f}: K={K[i]:+.4e} ref={ref['K'][j]:+.4e}  W={W[i]:.4e} V={V[i]:.4e}")
