import numpy as np, time
import testB_protocol as B
from common import kl, tv
for m in B.models.values(): m.cap = 1e3
r0 = B.starts['4 uniform']
runs = {}; t0 = time.time()
for s in B.SETS:
    runs[s] = B.models[s].evolve(r0, B.TE, rtol=1e-6, atol=1e-10)
    print('setting', np.round(s, 3), 'done', round(time.time() - t0, 1), flush=True)
Ps = {s: B.models[s].P(8.0) for s in B.SETS}
D = [kl(runs[s][-1], Ps[s]) for s in B.SETS]; D0 = [kl(r0, B.models[s].P(0.0)) for s in B.SETS]
pB = {s: (runs[s][-1].sum(0) * (B.side > 0)).sum() for s in B.SETS}
pA = {s: (runs[s][-1].sum(1) * (B.side > 0)).sum() for s in B.SETS}
sAB = max(abs(pB[(0.0, tb)] - pB[(np.pi/2, tb)]) for tb in (np.pi/4, -np.pi/4))
sBA = max(abs(pA[(ta, np.pi/4)] - pA[(ta, -np.pi/4)]) for ta in (0.0, np.pi/2))
E = {s: float((runs[s][-1] * np.outer(B.side, B.side)).sum()) for s in B.SETS}
ch = abs(E[B.SETS[0]] + E[B.SETS[1]] + E[B.SETS[2]] - E[B.SETS[3]])
print('uniform start (cap 1e3, rtol 1e-6): D0=%.3f D8=%.3f ratio=%.3f  TV8=%.3f  S8=%.4f  CHSH_rec=%.3f' % (np.mean(D0), np.mean(D), np.mean(D)/np.mean(D0), np.mean([tv(runs[s][-1], Ps[s]) for s in B.SETS]), max(sAB, sBA), ch))
