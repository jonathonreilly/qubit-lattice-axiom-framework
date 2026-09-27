"""Reptation sub-window integrals of the transverse probe modes for the pure ring clause (t = 0): 2^3 exact control, then larger L.
usage: rq_chi_test.py L nmoves Mseg window dur [nch] [meas_every]"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.sparse import coo_matrix
import rq2_lib as R
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "p24b_runner.py")).read()
exec(src[src.index("def exact_L2"):src.index("OFF = 16")])
L = int(sys.argv[1]); nmoves = int(sys.argv[2]); Mseg = int(sys.argv[3]); window = int(sys.argv[4]); dur = float(sys.argv[5])
nch = int(sys.argv[6]) if len(sys.argv) > 6 else 2
me = int(sys.argv[7]) if len(sys.argv) > 7 else max(50, Mseg // 4)
NSUB = 8
ice = R.Ice(L); T = R.QTables(ice)
k = 2 * np.pi / L
tail = np.array([ice.verts[l // 3] for l in range(ice.nl)])
modes, names = [], []
for a in range(3):
    for b in range(3):
        if a == b:
            continue
        xb = tail[np.arange(ice.nl), b]
        for f, fn in ((np.cos, "cos"), (np.sin, "sin")):
            v = f(k * xb) * (ice.axis == a)
            if np.abs(v).max() > 1e-9:
                modes.append(v); names.append(f"{'xyz'[a]}-links {fn}(k {'xyz'[b]})")
xm = np.array(modes)
T0 = time.time()
if L == 2:
    canon = ice.sector_state(0)
    codes, order, H2, sig_of = exact_L2(ice, canon)
    Sg = np.array([sig_of(c) for c in order]).astype(float)
    w, v = np.linalg.eigh(H2.toarray()); E0 = w[0]; psi = v[:, 0]
    D = w[1:] - E0
    cm = [(v.T @ ((Sg @ x) * psi))[1:] ** 2 for x in xm]
    a_ex = np.mean([np.sum(c / D) for c in cm])
    print(f"exact 2^3: n_c {len(order)}, E0 {E0:.6f}, gap {D[0]:.4f}, mode-mean a_m = {a_ex:.6f}", flush=True)
    def pred(Tw):
        return np.mean([np.sum(c * 2 * (Tw / D - (1 - np.exp(-D * Tw)) / D ** 2)) / Tw for c in cm])
allJ = []
for sd in range(nch):
    rr = np.random.default_rng(10 + sd)
    init = [ice.sector_state(0)] if L == 2 else R.loop_vmc(ice, R.ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
    out, st, bad, prof, J = R.reptation(ice, T, init[-1], 0.0, 1.0, 2.0, Mseg, dur, nmoves, nmoves // 5, me, window, 100 + sd, xm=xm, nsub=NSUB)
    el = 0.5 * (out[:, 2] + out[:, 3]); up = out[:, 1] / (window * dur * ice.np_)
    acc = st[0] / max(1, st[0] + st[1])
    allJ.append(J)
    Tw = window * dur
    def est(J):
        vf = (J.sum(axis=2) ** 2).mean(axis=0) / Tw                       # per mode, <I> = 0 by the sigma -> -sigma symmetry of the sector
        vh = (J[:, :, NSUB // 4:3 * NSUB // 4].sum(axis=2) ** 2).mean(axis=0) / (Tw / 2)
        return vf.mean() / 2, vh.mean() / 2, (vf - vh / 2).mean()
    nb_ = 10
    bl = np.array([est(c) for c in np.array_split(J, nb_)])
    e = est(J); er = bl.std(axis=0, ddof=1) / np.sqrt(nb_)
    msg = (f"L{L} seed{sd}: E(ends) {el.mean():.4f}  <U+U+>/plaq {up.mean():.4f}  a_m(Tw={Tw:g}) {e[0]:.4f}+-{er[0]:.4f}  a_m(Tw/2) {e[1]:.4f}+-{er[1]:.4f}  "
           f"extrapolated {e[2]:.4f}+-{er[2]:.4f}  chi {4 * e[2] / ice.nv:.4f}+-{4 * er[2] / ice.nv:.4f}  <I> mean {J.sum(axis=2).mean():.3f}  acc {acc:.3f} ovf {st[2]} "
           f"{len(out)} meas  {time.time() - T0:.0f} s")
    if L == 2:
        msg += f"\n   exact finite-window a_m: {pred(Tw) / 2:.5f} (Tw), {pred(Tw / 2) / 2:.5f} (Tw/2); exact a_m {a_ex:.5f}"
    print(msg, flush=True)
np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"rqJ_L{L}_M{Mseg}_w{window}_d{dur}.npy"), np.concatenate(allJ))
