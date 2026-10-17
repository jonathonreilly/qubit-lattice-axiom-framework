"""QMC-1b check (c1): alternating up/down sweeps keep wrapped-vs-fresh G <= 1e-6 in both directions (L4, W = 2,
dtau = 0.05, n_s = 8, f2 and fG); timing of 4 alternating sweeps vs 2 upward-only sweeps. No observable is read."""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from x2model import FlavourModel
from afqmc import Lattice, AFQMC
KAP = {"sing:8v": 1.5, "trip:8v": -0.5, "sing:56v": 0.0, "trip:56v": 0.0}
fm = FlavourModel("spin10"); ok = True
for filt in ("f2", "fG"):
    lat = Lattice((4, 4), filt)
    sim = AFQMC(fm, KAP, lat, W=2.0, beta=4.0, dtau=0.05, n_s=8, seed=7, step=0.6); sim.alternate = True
    sim.build_left_stack(); t = time.time()
    for _ in range(4):
        sim.sweep()
    ta = (time.time() - t) / 4
    p = sim.maxdev <= 1e-6 and sim.maxdev_down <= 1e-6
    ok &= p
    sim2 = AFQMC(fm, KAP, lat, W=2.0, beta=4.0, dtau=0.05, n_s=8, seed=7, step=0.6); sim2.build_left_stack(); t = time.time()
    for _ in range(2):
        sim2.sweep()
    tu = (time.time() - t) / 2
    print(f"{filt}: alternating maxdev {sim.maxdev:.1e} (down {sim.maxdev_down:.1e}); acc {sim.nacc/sim.nprop:.2f}; "
          f"{ta:.2f} s/sweep alternating vs {tu:.2f} s/sweep upward; PASS(c1) {p}", flush=True)
print("C1 PASS" if ok else "C1 FAIL")
