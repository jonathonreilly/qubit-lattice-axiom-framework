"""QMC-1b: the speed-changed engine (this folder) against the unmodified QMC-1 engine (../../QMC1/scripts/afqmc.py),
same seed, same Lattice object, 2 sweeps with updates. PASS: identical accept counts, max |phi_new - phi_old| = 0,
max |G_new - G_old| <= 1e-9 at the end, both filters (f2, fG), L = 4, W = 2, beta = 4, dtau = 0.05, n_s = 8."""
import sys, os, importlib.util, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
OLD = os.path.join(HERE, "..", "..", "QMC1", "scripts")
sys.path.insert(0, HERE)
from x2model import FlavourModel
import afqmc as new
spec = importlib.util.spec_from_file_location("afqmc_old", os.path.join(OLD, "afqmc.py"))
old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
KAP = {"sing:8v": 1.5, "trip:8v": -0.5, "sing:56v": 0.0, "trip:56v": 0.0}
fm = FlavourModel("spin10")
ok = True
for filt in ("f2", "fG"):
    lat = new.Lattice((4, 4), filt)
    out = {}
    for name, mod in (("old", old), ("new", new)):
        t = time.time()
        sim = mod.AFQMC(fm, KAP, lat, W=2.0, beta=4.0, dtau=0.05, n_s=8, seed=2024, step=0.6)
        for _ in range(2):
            G = sim.sweep()
        out[name] = (sim.nacc, sim.nprop, sim.phi.copy(), G.copy(), time.time() - t, sim.maxdev)
    (ao, po, fo, Go, to, mo), (an, pn, fn, Gn, tn, mn) = out["old"], out["new"]
    dphi, dG = np.abs(fo - fn).max(), np.abs(Go - Gn).max()
    p = (ao == an) and (po == pn) and dphi == 0 and dG <= 1e-9
    ok &= p
    print(f"{filt}: acc old {ao}/{po} new {an}/{pn}; max|dphi| {dphi:.1e}; max|dG| {dG:.1e}; wrap-dev old {mo:.1e} new {mn:.1e}; "
          f"time old {to:.1f}s new {tn:.1f}s; PASS {p}", flush=True)
print("EQUIV PASS" if ok else "EQUIV FAIL")
