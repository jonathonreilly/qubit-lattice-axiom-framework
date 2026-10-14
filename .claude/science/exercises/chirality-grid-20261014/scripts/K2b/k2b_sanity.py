"""K2b code sanity (registered in PREREG T2 (c) check; plus reproduction of K2's G1p set-1 value)."""
import numpy as np, time
from lat2d import Geom, rand_half
from k2b_lib import *
G = Geom(2, 6, False, -1); delta = 0.6; k = 8
rng = np.random.default_rng(262); sets = [[rand_half(rng, G, 0.25, delta) for _ in range(k)] for _ in range(3)]
t0 = time.time()
Z, g = full_kernel(G, sets[1], delta, 32, None, 'O'); a, b, _ = lam(Z)
print(f"reproduce K2 G1p d0.6 set1 overlap: lam_min {a:+.4e} min/max {a/b:+.4e} (K2: -7.4055e-6) min|H_W| {g:.3f} {time.time()-t0:.1f}s", flush=True)
# (c) check: Shamir overlap vs PV-subtracted dense DWF at large L_s, on single gauge points
Fs, Bs = G.crossing_mats(); D0 = G.D0(sets[1][0], sets[1][3])
ph = np.array([[0.0, 0.1], [0.0, -0.2]])
Db = D_batch(G, D0, Fs, Bs, ph)
sh, gs = logdet_op(G, Db, 'SH')
for Ls in [8, 16, 24, 40]:
    t0 = time.time(); pv, _ = logdet_op(G, Db, 'D5PV', Ls)
    print(f"Ls={Ls}: logdet D5PV - logdet SH = {np.abs(pv - sh).max():.2e}  ({time.time()-t0:.2f}s for 2 points)  min|H_T| {gs.min():.3f}", flush=True)
