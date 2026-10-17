"""TOR-1 W-matched random pool on the Lx = 4 torus (K2c V2 method): rand_half (sigma 0.3), holonomy shift W(slice 1) = 0, one
x-link sets W(slice T) = 0, bulk plaquettes <= 0.55.  usage: python3 tor1_pool.py Lt k seed"""
import sys
import numpy as np
from lat2d import Geom, rand_half, wrap
Lt, k, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); T = Lt // 2; G = Geom(4, T, True, -1); rng = np.random.default_rng(seed)
UX, UT = [], []
while len(UX) < k:
    u = rand_half(rng, G, 0.3, 0.55)
    ux = u['x'] - u['x'][0].sum() / 4                       # W(slice 1) = 0, plaquettes unchanged
    ux[T - 1, 0] -= ux[T - 1].sum()                          # W(slice T) = 0 by one x-link
    ok = True
    for t in range(T - 1):
        for x in range(4):
            if abs(wrap(ux[t, x] + u['t'][t, (x + 1) % 4] - ux[t + 1, x] - u['t'][t, x])) > 0.55: ok = False
    if ok: UX.append(ux); UT.append(u['t'])
UX, UT = np.array(UX), np.array(UT)
print(f"pool Lt={Lt} k={k} seed={seed}: max |W(slice 1)| {np.abs(UX[:, 0].sum(1)).max():.1e}, max |W(slice T)| {np.abs(UX[:, T-1].sum(1)).max():.1e}")
np.savez(f"pool_TOR1_Lt{Lt}_k{k}_s{seed}.npz", ux=UX, ut=UT)
