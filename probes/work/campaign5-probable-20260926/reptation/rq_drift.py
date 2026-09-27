"""E(ends) drift from the path build: one chain, therm 0, block means in time order. usage: rq_drift.py L Mseg dur nmoves h nblk"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rq3_lib as R
L = int(sys.argv[1]); Mseg = int(sys.argv[2]); dur = float(sys.argv[3]); nm = int(sys.argv[4]); h = float(sys.argv[5]); nb = int(sys.argv[6])
ice = R.Ice(L); T = R.QTables(ice)
k = 2 * np.pi / L
tail = np.array([ice.verts[l // 3] for l in range(ice.nl)])
hv = np.cos(k * tail[np.arange(ice.nl), (ice.axis + 1) % 3])
rr = np.random.default_rng(11)
init = R.loop_vmc(ice, 0.2, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
T0 = time.time()
out, st, bad, prof = R.reptation(ice, T, init[-1], 0.0, 1.0, 2.0, Mseg, dur, nm, 0, 100, Mseg // 4, 77, hfield=h * hv, bguide=0.5 * 0.15 * hv, profile=False)
el = 0.5 * (out[:, 2] + out[:, 3])
acc = st[0] / (st[0] + st[1])
ren = Mseg ** 2 * (1 - acc)
print(f"L{L} Mseg {Mseg} dur {dur} (path {Mseg * dur:g}) h {h}: acc {acc:.3f}, est. renewal {ren:.0f} moves, {nm / ren:.1f} renewals, "
      f"{(time.time() - T0) / nm * 1e6:.0f} us/move", flush=True)
bm = [c.mean() / ice.np_ for c in np.array_split(el, nb)]
print("   -E/plaq by block (time order): " + " ".join(f"{-x:.5f}" for x in bm), flush=True)
np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"rqdrift_L{L}_M{Mseg}_d{dur}_h{h}.npy"), el)
