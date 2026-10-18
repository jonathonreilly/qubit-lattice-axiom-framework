from common import *
from wsym import Wcont
from ward2 import PR
d = np.array([0.3, -0.5, 0.6, 0.55]); d /= np.linalg.norm(d)
for s in (0.1, 0.05, 0.025):
    q = s * d; W = strain_metric(Dc, q) @ Dc.gauge(q)[:, :4]; Wm = np.exp(1j * PR @ q)[:, None] * Wcont(q)
    D = W - Wm; mask = np.abs(Wcont(q)) > 0
    print(f"s={s}: |W - e^(iqp) Wc|/|W| {np.linalg.norm(D)/np.linalg.norm(W):.2e}; on-support part {np.linalg.norm(D[mask])/np.linalg.norm(W):.2e}; off-support part {np.linalg.norm(D[~mask])/np.linalg.norm(W):.2e}")
    print("   off-support entries row (0,1):", np.round(W[HC.index((0,1))]/s**2, 3))
