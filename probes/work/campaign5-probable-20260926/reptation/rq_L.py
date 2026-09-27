"""Two population-free curvature estimators on L^3 by reptation: window fluctuations of the transverse modes (zero field, m = 1, 2)
and the three-point energy curvature at m = 1 (E(0), E(H1), E(2 H1), common guide 0.5 H1). usage: rq_L.py L Mseg dur window nm0 nmh therm"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rq2_lib as R
L, Mseg = int(sys.argv[1]), int(sys.argv[2]); dur = float(sys.argv[3]); window = int(sys.argv[4])
nm0, nmh, therm = int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
H1, NSUB = 0.15, 8
ice = R.Ice(L); T = R.QTables(ice)
tail = np.array([ice.verts[l // 3] for l in range(ice.nl)])
modes, tags = [], []
for m in (1, 2):
    k = 2 * np.pi * m / L
    for a in range(3):
        for b in range(3):
            if a != b:
                for f in (np.cos, np.sin):
                    modes.append(f(k * tail[np.arange(ice.nl), b]) * (ice.axis == a)); tags.append(m)
xm = np.array(modes); tags = np.array(tags)
hv = np.cos(2 * np.pi / L * tail[np.arange(ice.nl), (ice.axis + 1) % 3])
rr = np.random.default_rng(21)
init = R.loop_vmc(ice, 0.2, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)[-1]
T0 = time.time()
out, st, bad, prof, J = R.reptation(ice, T, init, 0.0, 1.0, 2.0, Mseg, dur, nm0, therm, max(100, Mseg // 4), window, 31, xm=xm, nsub=NSUB,
                                    bguide=0.5 * H1 * hv, profile=False)
acc = st[0] / (st[0] + st[1])
el = 0.5 * (out[:, 2] + out[:, 3])
Tw = window * dur
nb = 20
def blk(x):
    b = np.array([c.mean() for c in np.array_split(x, nb)]); return x.mean(), b.std(ddof=1) / np.sqrt(nb)
print(f"L{L} path {Mseg * dur:g} window {Tw:g}: acc {acc:.3f}, renewals ~{(nm0 + therm) / (Mseg ** 2 * (1 - acc)):.0f}, {len(out)} meas, "
      f"{time.time() - T0:.0f} s", flush=True)
e0, e0e = blk(el)
print(f"   E(0) {e0:.4f}+-{e0e:.4f}  u {-e0 / ice.np_:.5f}; E by quarter: " + " ".join(f"{c.mean() / ice.np_:.5f}" for c in np.array_split(el, 4)), flush=True)
np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"rqJ8_L{L}_M{Mseg}.npy"), J)
for m in (1, 2):
    Jm = J[:, tags == m, :]
    If = Jm.sum(axis=2); Ih = Jm[:, :, NSUB // 4:3 * NSUB // 4].sum(axis=2)
    vf = (If ** 2).mean(axis=1) / Tw; vh = (Ih ** 2).mean(axis=1) / (Tw / 2)      # per measurement, mode-averaged
    ext = vf - vh / 2
    a_f, a_fe = blk(vf / 2); a_x, a_xe = blk(ext)
    print(f"   m={m} (k = 2 pi {m}/{L}): a_m(Tw) {a_f:.4f}+-{a_fe:.4f}, a_m(Tw/2) {(vh / 2).mean():.4f}, extrapolated {a_x:.4f}+-{a_xe:.4f}; "
          f"chi {4 * a_x / ice.nv:.4f}+-{4 * a_xe / ice.nv:.4f} (Tw only: {4 * a_f / ice.nv:.4f})", flush=True)
Es = {0.0: (e0, e0e)}
for j, h in enumerate((H1, 2 * H1)):
    out, st, bad, prof, _ = R.reptation(ice, T, init, 0.0, 1.0, 2.0, Mseg, dur, nmh, therm, 100, window, 41 + j, hfield=h * hv, bguide=0.5 * H1 * hv,
                                        profile=False)
    el = 0.5 * (out[:, 2] + out[:, 3]); Es[h] = blk(el)
    print(f"   E({h}) {Es[h][0]:.4f}+-{Es[h][1]:.4f}; by quarter: " + " ".join(f"{c.mean() / ice.np_:.5f}" for c in np.array_split(el, 4)) +
          f"  acc {st[0] / (st[0] + st[1]):.3f}  {time.time() - T0:.0f} s", flush=True)
(E0, s0), (E1, s1), (E2, s2) = Es[0.0], Es[H1], Es[2 * H1]
a = (15 * E0 - 16 * E1 + E2) / (12 * H1 ** 2); sa = np.sqrt(225 * s0 ** 2 + 256 * s1 ** 2 + s2 ** 2) / (12 * H1 ** 2)
print(f"   three-point chi (m=1) {4 * a / (3 * ice.nv):.4f}+-{4 * sa / (3 * ice.nv):.4f}", flush=True)
