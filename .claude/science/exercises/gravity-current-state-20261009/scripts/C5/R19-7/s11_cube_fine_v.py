"""R19-7 s11: L=2 cube, fine v scan through the RK point: E0(v), first gap, second derivative of E0 (finite differences),
the face (pi,pi,0) TT2 main pole and the axis T2 main pole. A sharp peak in -d2E0/dv2 with a gap minimum marks the
finite-size precursor of a transition; its location relative to v = t is the reading."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from ed import *
mod = Model(Torus(2, 2, 2))
pf = channel_pols(np.array([1, 1, 0.0])/np.sqrt(2)); pa = channel_pols(np.array([0, 0, 1.0]))
for bU in [1.0, 2.0, 3.0]:
    vs = np.round(np.arange(0.5, 1.505, 0.02), 3); E = []; rows = []
    for v in vs:
        E0, g, w, dense = ground(mod, v, bU)
        om, wt = spectral(mod, v, bU, np.array([np.pi, np.pi, 0]), pf["TT"][1], E0, g, dense=dense); df = diagnose(om, wt)
        om, wt = spectral(mod, v, bU, np.array([0, 0, np.pi]), pa["TT"][1], E0, g, dense=dense); da = diagnose(om, wt)
        E.append(E0); rows.append((v, E0, w[1] - w[0], df["main"], df["S"], da["main"]))
    E = np.array(E); d2 = np.full(len(E), np.nan); d2[1:-1] = (E[2:] - 2*E[1:-1] + E[:-2])/0.02**2
    i = np.nanargmin(d2)
    print("bU=%.0f: min d2E0/dv2 = %.3f at v = %.2f ; min gap %.3g at v = %.2f" % (bU, d2[i], vs[i], min(r[2] for r in rows), rows[int(np.argmin([r[2] for r in rows]))][0]))
    for (v, E0, gp, fm, fS, am), dd in zip(rows, d2):
        if abs(v*50 - round(v*50)) < 1e-9 and (round(v*100) % 10 == 0 or 0.9 <= v <= 1.1):
            print("   v=%.2f E0=%9.4f gap=%.4g d2E0=%8.3f face-TT2 main=%.4g (S=%.3f) axis-T2 main=%.4g" % (v, E0, gp, dd, fm, fS, am))
