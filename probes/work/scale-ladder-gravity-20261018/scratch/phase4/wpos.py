# effective registration point of each strain-metric entry: W[row, col] ~ e^{i q.p} Wcont[row, col]
from wsym import Wcont
from common import *
eps = 1e-4; Ws = {}
P = {}
for r in range(4):
    e = np.zeros(4); e[r] = eps
for i, (a, b) in enumerate(HC):
    for col in sorted({a, b}):
        p = []
        for m in range(4):
            dq = np.zeros(4); dq[m] = eps; base = np.array([0.013, 0.007, -0.011, 0.005])
            ph = lambda q: np.angle((strain_metric(Dc, q) @ Dc.gauge(q)[:, :4])[i, col] / Wcont(q)[i, col])
            p.append((ph(base + dq) - ph(base - dq)) / (2 * eps))
        P[(i, col)] = np.round(p, 4)
        print(HC[i], 'col', col, 'p =', P[(i, col)])
