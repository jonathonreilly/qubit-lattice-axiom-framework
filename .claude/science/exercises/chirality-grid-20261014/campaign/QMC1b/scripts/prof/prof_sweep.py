"""QMC-1b engineering: timing profile of one sweep (no physics output used)."""
import sys, os, time, cProfile, pstats
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import numpy as np
from x2model import FlavourModel
from afqmc import Lattice, AFQMC
L, filt, W, ns = int(sys.argv[1]), sys.argv[2], float(sys.argv[3]), int(sys.argv[4])
fm = FlavourModel("spin10"); lat = Lattice((L, L), filt)
t0 = time.time()
sim = AFQMC(fm, {"sing:8v": 1.5, "trip:8v": -0.5, "sing:56v": 0.0, "trip:56v": 0.0}, lat, W=W, beta=4.0, dtau=0.05, n_s=ns, seed=99, step=0.6)
sim.build_left_stack(); print(f"init+stack {time.time()-t0:.1f}s", flush=True)
pr = cProfile.Profile(); pr.enable(); t1 = time.time(); sim.sweep(); pr.disable()
print(f"one sweep {time.time()-t1:.1f}s acc {sim.nacc/max(1,sim.nprop):.2f}", flush=True)
pstats.Stats(pr).sort_stats("tottime").print_stats(14)
