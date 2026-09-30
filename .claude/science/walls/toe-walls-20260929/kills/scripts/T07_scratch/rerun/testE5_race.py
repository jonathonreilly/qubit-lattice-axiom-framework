"""Test E5 (exploratory): does the noise rate needed scale with the branching time?  Ring L=48, centre 24.
Packet amplitude width w in {1.5, 3.0}; shifted product start (shift = 2 * w/1.5 sites); gamma in {0.3, 1, 3}."""
import numpy as np, json
from common import *
L = 48; C = 24
ring = Ring(L); x = np.arange(L)
SETS = [(0.0, np.pi/4), (0.0, -np.pi/4), (np.pi/2, np.pi/4), (np.pi/2, -np.pi/4)]
side = np.where(x >= C, 1.0, -1.0)
TE = np.arange(0, 9.0)
out = []
for w in (1.5, 3.0):
    models = {s: Bell2(L, s[0], s[1], ring, width=w, centre=C) for s in SETS}
    for m in models.values(): m.cap = 1e5
    Pb = models[SETS[0]].P(0.0); ma = Pb.sum(1); mb = Pb.sum(0)
    sh = int(round(2 * w / 1.5))
    rho0 = np.outer(np.roll(ma, sh), np.roll(mb, sh)); rho0 /= rho0.sum()
    for g in (0.3, 1.0, 3.0):
        runs = {s: models[s].evolve(rho0, TE, gamma=g) for s in SETS}
        Ps = {s: models[s].P(8.0) for s in SETS}
        D = np.mean([kl(runs[s][-1], Ps[s]) for s in SETS]); D0 = np.mean([kl(rho0, models[s].P(0.0)) for s in SETS])
        pB = {s: (runs[s][-1].sum(0) * (side > 0)).sum() for s in SETS}
        pA = {s: (runs[s][-1].sum(1) * (side > 0)).sum() for s in SETS}
        S = max(max(abs(pB[(0.0, tb)] - pB[(np.pi/2, tb)]) for tb in (np.pi/4, -np.pi/4)),
                max(abs(pA[(ta, np.pi/4)] - pA[(ta, -np.pi/4)]) for ta in (0.0, np.pi/2)))
        E = {s: float((runs[s][-1] * np.outer(side, side)).sum()) for s in SETS}
        ch = abs(E[SETS[0]] + E[SETS[1]] + E[SETS[2]] - E[SETS[3]])
        r = dict(width=w, shift=sh, gamma=g, D0=D0, D8=D, ratio=D/D0, S8=S, chsh=ch)
        out.append(r); print(r, flush=True)
json.dump(out, open('testE5_results.json', 'w'), indent=1)
