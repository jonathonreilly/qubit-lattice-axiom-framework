"""QMC-1b engineering: memory and wrap check of one up + one down sweep at L6 (fG, W = 4, dtau 0.05, n_s 8). No observable read."""
import sys, os, time, resource
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from x2model import FlavourModel
from afqmc import Lattice, AFQMC
fm = FlavourModel("spin10"); lat = Lattice((6, 6), "fG")
sim = AFQMC(fm, {"sing:8v": 1.5, "trip:8v": -0.5, "sing:56v": 0.0, "trip:56v": 0.0}, lat, W=4.0, beta=4.0, dtau=0.05, n_s=8, seed=8, step=0.4)
sim.alternate = True; sim.build_left_stack()
for i in range(2):
    t = time.time(); sim.sweep()
    print(f"sweep {i} ({'up' if i == 0 else 'down'}): {time.time() - t:.1f}s acc {sim.nacc/sim.nprop:.2f} maxdev {sim.maxdev:.1e} "
          f"maxdev_down {getattr(sim, 'maxdev_down', float('nan')):.1e} rss {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20:.0f}MB", flush=True)
