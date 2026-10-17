"""Gate (iii) exact side: ED of the reduced-flavour model (1 s + 1 c flavour), 1D ring L = 3, filter f1,
walker on, W = 2, beta = 2 (PREREG section 4 (iii)). Saves runs/ed_gate3.npz."""
import sys, os, time, resource
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from x2model import FlavourModel
from afqmc import Lattice
import ed_exact
KAPRED = {"sing:1v": 1.0, "trip:1v": -1.0 / 3}
fr = FlavourModel("reduced"); lat = Lattice((3,), "f1")
out = {}
for W in (2.0,):
    ops = ed_exact.build(fr, KAPRED, lat, W=W)
    r = ed_exact.thermal(ops, beta=2.0)
    print(f"ED W={W} beta=2 L=3: E={r['E']:.10f} Ekin={r['Ekin']:.10f} WQ={W * r['Q']:.10f} "
          f"S_X/N={np.round(r['SX'] / lat.N, 10).tolist()} S_Y/N={np.round(r['SY'] / lat.N, 10).tolist()} "
          f"E0={r['E0']:.6f} gap={r['gap']:.6f}")
    out.update({f"W{W}_{k}": v for k, v in r.items()})
np.savez("runs/ed_gate3.npz", **out)
print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20:.0f} MB")
