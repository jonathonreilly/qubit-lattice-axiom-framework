"""check: tree-product vertex_core (afqmc.py) == sequential loop (afqmc_prepatch_ref.py), both slice parities."""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from x2model import FlavourModel
import afqmc, afqmc_prepatch_ref as ref
fm = FlavourModel("spin10"); lat = afqmc.Lattice((4, 4), "f2")
K = {"sing:8v": 1.5, "trip:8v": -0.5, "sing:56v": 0.0, "trip:56v": 0.0}
s1 = afqmc.AFQMC(fm, K, lat, W=4.0, beta=0.4, dtau=0.1, n_s=4, seed=1)
s0 = ref.AFQMC(fm, K, lat, W=4.0, beta=0.4, dtau=0.1, n_s=4, seed=1)
dev = 0
for l in range(2):
    phi = np.random.default_rng(l).normal(size=s1.nch) * 2
    c1, i1 = s1.vertex_core(l, phi); c0, i0 = s0.vertex_core(l, phi)
    dev = max(dev, np.abs(c1 - c0).max() / np.abs(c0).max(), np.abs(i1 - i0).max() / np.abs(i0).max(), np.abs(c1 @ i1 - np.eye(32)).max())
t = time.time()
for _ in range(200): s1.vertex_core(0, phi)
t1 = (time.time() - t) / 200; t = time.time()
for _ in range(200): s0.vertex_core(0, phi)
t0 = (time.time() - t) / 200
print(f"tree vs loop max rel dev {dev:.1e}; time per core: tree {t1*1e3:.3f} ms, loop {t0*1e3:.3f} ms")
