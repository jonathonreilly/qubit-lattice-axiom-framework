"""QMC-1b gate (iii) comparison: reduced-flavour QMC (runs/gate3_<filt>.npz) against psi-frame ED, 1D L = 3, W = 2,
beta = 2. PASS = |QMC - ED| <= 2 sigma (binning, 20 bins) for W<Q> (HS channels), sum_a(S_X + S_Y), E_kin."""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from x2model import FlavourModel
from afqmc import Lattice
from analysis import binned
import ed_exact
KAPRED = {"sing:1v": 1.0, "trip:1v": -1.0 / 3}
fr = FlavourModel("reduced"); ok = True
for filt in sys.argv[1:]:
    tag = filt
    filt = filt.split("_")[0]
    lat = Lattice((3,), filt)
    r = ed_exact.thermal(ed_exact.build(fr, KAPRED, lat, W=2.0), beta=2.0)
    z = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs", f"gate3_{tag}.npz"), allow_pickle=True)
    ed = {"WQc": 2.0 * r["Q"], "S": float(np.sum(r["SX"] + r["SY"]) / lat.N), "Ekin": r["Ekin"]}
    qm = {"WQc": z["WQc"], "S": z["SX0"].sum(1) + z["SY0"].sum(1), "Ekin": z["Ekin"]}
    for k in ("WQc", "S", "Ekin"):
        m, e, _ = binned(qm[k], 20)
        dev = abs(m - ed[k]) / e
        ok &= dev <= 2
        print(f"gate(iii) {tag} n={len(z['acc'])}: {k}: QMC {m:.6f} +- {e:.6f}  ED {ed[k]:.6f}  |dev| = {dev:.2f} sigma "
              f"(PASS {dev <= 2}); max phase {np.max(z['maxphase']):.1e}", flush=True)
print("GATE (iii) PASS" if ok else "GATE (iii) FAIL")
