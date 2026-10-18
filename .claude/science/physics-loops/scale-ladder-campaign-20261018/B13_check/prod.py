"""usage: python prod.py L V N eta seed init nblocks block_t [dt]
init: 'tiled' (2-periodic tiling of the max-N_f state of the 2^3 vacuum component, own BFS) or 'simple'.
eta > 0: twisted run (harmonic orientation-0 source); eta = 0: forward walking for 3 harmonic sources.
Saves results/L{L}_V{V}_N{N}_e{eta}_{init}_dt{dt}_s{seed}.npz.  Independent checker code; no claim."""
import os, sys, time
os.environ.setdefault("NUMBA_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import chk
L, V, N, eta, sd, init, nb_, bt = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), sys.argv[6], int(sys.argv[7]), float(sys.argv[8])
dt = float(sys.argv[9]) if len(sys.argv) > 9 else 0.1
lat = chk.Lat((L, L, L))
if init == "simple":
    s0 = chk.simple_ice(lat)
else:
    l2 = chk.Lat((2, 2, 2)); S2, nf2, _ = chk.component(l2, chk.simple_ice(l2))
    best = S2[np.argmax(nf2)]
    s0 = np.zeros(lat.nl, np.int64)
    for v in lat.verts:
        for a in range(3):
            s0[lat.link(v, a)] = best[l2.link(tuple(x % 2 for x in v), a)]
    assert np.abs(lat.div @ s0).max() == 0
assert lat.winding(s0) == (0, 0, 0)
Cm = np.array([lat.harm(o) for o in range(3)]) if eta == 0 else np.zeros((0, lat.np_))
t0 = time.time()
r = chk.run(lat, s0, V, N=N, dt=dt, ttherm=max(20.0, bt), nblocks=nb_, block_t=bt, ctw=lat.harm(0), eta=eta, Cm=Cm, seed=sd)
os.makedirs("results", exist_ok=True)
fn = f"results/L{L}_V{V:+.2f}_N{N}_e{eta:.2f}_{init}_dt{dt}_s{sd}.npz"
np.savez_compressed(fn, **{k: v for k, v in r.items()}, L=L, V=V, eta=eta, nf0=int((lat.circ(s0) != 0).sum()), secs=time.time() - t0)
e = r["EM"][~np.isnan(r["EM"])]
print(f"{fn}: Emix/plaq={e.mean()/lat.np_:.6f} nf0/plaq={(lat.circ(s0)!=0).mean():.3f} mean N/ESS={r['IESS'].mean():.2f} ({time.time()-t0:.0f}s)", flush=True)
