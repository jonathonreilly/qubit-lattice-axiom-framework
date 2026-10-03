"""A44 star_vmc: soldered state's correlations on the star-local pairs beyond nearest neighbours
(face diagonals x, x+e_a+-e_b and axis pairs x, x+2e_a), full 3x3 per family; Klein-dual combinations.
Usage: star_vmc.py L NSWEEP"""
import sys, time, signal, numpy as np
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a44lib import *
from vmc import vmc, binerr
L, nsw = int(sys.argv[1]), int(sys.argv[2])
cl = cube(L); X = cl.X
fams = {"fd(1,1,0)": (1, 1, 0), "fd(1,-1,0)": (1, -1, 0), "fd(1,0,1)": (1, 0, 1), "fd(1,0,-1)": (1, 0, -1),
        "fd(0,1,1)": (0, 1, 1), "fd(0,1,-1)": (0, 1, -1), "ax(2,0,0)": (2, 0, 0), "ax(0,2,0)": (0, 2, 0), "ax(0,0,2)": (0, 0, 2)}
extra = []
for nm, d in fams.items():
    pj = np.array([cl.idx[tuple(cl.canon(np.array(x) + np.array(d))[0])] for x in cl.sites])
    extra.append((np.arange(cl.N), pj))
r = vmc(cl, 0.0, 1.0, "sold", nsw, ntherm=max(50, nsw // 10), seed=4477, tlimit=240, extra=extra)
S = r["S"]; base = 6 + 27
np.save(f"star_vmc_{L}.npy", S)
print(f"L={L} soldered: sweeps {r['nsw']} in {r['secs']:.0f}s; drift {r['drift']:.1e}")
mJ, eJ, _ = binerr(S[:, 0].real); mK, eK, _ = binerr(S[:, 1].real)
print(f"  NN: e_J = {mJ:+.5f} +- {eJ:.5f}, e_K = {mK:+.5f} +- {eK:.5f}")
dual_fd, dual_ax, sold_fd = [], [], []
for f, (nm, d) in enumerate(fams.items()):
    C = S[:, base + 9 * f: base + 9 * f + 9].real.reshape(-1, 3, 3)
    Cm = C.mean(0)
    Rx = np.array([1, 1, 1.]); d = np.array(d)
    # Klein: R_x R_{x+d} = diag((-1)^(d2+d3), (-1)^(d1+d3), (-1)^(d1+d2))  (x-independent)
    sg = np.array([(-1.) ** (abs(d[1]) + abs(d[2])), (-1.) ** (abs(d[0]) + abs(d[2])), (-1.) ** (abs(d[0]) + abs(d[1]))])
    dual = (C * sg[None, :, None] * np.eye(3)[None]).sum(axis=(1, 2))   # sum_a sg_a C_aa = dual-frame s.s
    md, ed, _ = binerr(dual)
    ms_, es_, _ = binerr(np.trace(C, axis1=1, axis2=2))
    print(f"  {nm:10s}: <s.s> = {ms_:+.5f} +- {es_:.5f}; diag (xx,yy,zz) {np.round(np.diag(Cm), 4)}; offdiag max {np.abs(Cm - np.diag(np.diag(Cm))).max():.1e}; "
          f"dual-frame <s.s> = {md:+.5f} +- {ed:.5f}")
    (dual_ax if nm.startswith("ax") else dual_fd).append(md)
print(f"  dual-frame (pi-flux singlet) second-neighbour <s.s>: face diagonals {np.mean(dual_fd):+.5f}, axis pairs {np.mean(dual_ax):+.5f}")
np.save(f"star_vmc_{L}.npy", S)
