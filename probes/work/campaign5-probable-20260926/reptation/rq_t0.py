"""Pure ring (t = 0) reptation on L^3 with guide exp(alpha N_flip): E(ends) and <U+U+>/plaquette for several alpha and path lengths.
usage: rq_t0.py L nmoves dur spec... where spec = alpha:Mseg"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rq2_lib as R
L = int(sys.argv[1]); nmoves = int(sys.argv[2]); dur = float(sys.argv[3])
ice = R.Ice(L); T = R.QTables(ice)
T0 = time.time()
for spec in sys.argv[4:]:
    al, Mseg = spec.split(":"); al = float(al); Mseg = int(Mseg)
    rr = np.random.default_rng(10)
    init = R.loop_vmc(ice, al, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
    out, st, bad, prof, J = R.reptation(ice, T, init[-1], 0.0, 1.0, 2.0, Mseg, dur, nmoves, nmoves // 5, 100, Mseg // 4, 100, alpha=al)
    el = 0.5 * (out[:, 2] + out[:, 3]); up = out[:, 1] / (Mseg // 4 * dur * ice.np_)
    nb_ = 10
    be = lambda x: np.array([c.mean() for c in np.array_split(x, nb_)]).std(ddof=1) / np.sqrt(nb_)
    q = Mseg // 8
    pr = prof[1] / (len(out) * dur * ice.np_)
    nbin = 20; qq = Mseg // nbin
    prb = [pr[i * qq:(i + 1) * qq].mean() for i in range(nbin)]
    acc = st[0] / max(1, st[0] + st[1])
    print(f"L{L} alpha {al} Mseg {Mseg} (path {Mseg * dur:g}): E(ends) {el.mean():.4f}+-{be(el):.4f}  <U+U+>/plaq middle {up.mean():.5f}+-{be(up):.5f}  "
          f"-E/plaq {-el.mean() / ice.np_:.5f}  acc {acc:.3f}  {time.time() - T0:.0f} s\n   <U+U+>/plaq profile ({nbin} bins of {qq * dur:g}): " + " ".join(f"{x:.4f}" for x in prb), flush=True)
