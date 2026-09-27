import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rq_lib as R
L = int(sys.argv[1]); t = float(sys.argv[2]); gam = float(sys.argv[3]); nmoves = int(sys.argv[4])
Mseg = int(sys.argv[5]) if len(sys.argv) > 5 else 400
EX = {(2, 0.35): (0.1600, -9.631658548), (2, 0.5): (0.2978, -10.430531975)}
ice = R.Ice(L); T = R.QTables(ice)
dur = 0.05; window = Mseg // 4
T0 = time.time()
vals = []
for sd in range(int(os.environ.get("NCH", "3"))):
    rr = np.random.default_rng(10 + sd)
    init = R.loop_vmc(ice, R.ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
    out, st, bad, prof = R.reptation(ice, T, init[-1], t, gam, 2.0, Mseg, dur, nmoves, nmoves // 5, 50, window, 100 + sd)
    sx = out[:, 0] / (t * window * dur * ice.nl); up = out[:, 1] / (window * dur * ice.np_); el = 0.5 * (out[:, 2] + out[:, 3])
    nb_ = 10
    be = lambda x: np.array([c.mean() for c in np.array_split(x, nb_)]).std(ddof=1) / np.sqrt(nb_)
    vals.append((sx.mean(), be(sx), up.mean(), el.mean(), be(el)))
    pr = prof / (len(out) * t * dur * ice.nl)
    q = Mseg // 8
    print("   profile of <sx> along the path (eighths): " + " ".join(f"{pr[i * q:(i + 1) * q].mean():.3f}" for i in range(8)), flush=True)
    acc = st[0] / max(1, st[0] + st[1])
    print(f"L{L} t{t} gam{gam} seed{sd}: <sx> {sx.mean():.4f}+-{be(sx):.4f}  <U+U+> {up.mean():.4f}  E(ends) {el.mean():.4f}+-{be(el):.4f}  "
          f"acceptance {acc:.3f} overflow {st[2]} build-overflow {bad}  {len(out)} meas  {time.time() - T0:.0f} s", flush=True)
v = np.array(vals)
ex = EX.get((L, t))
print(f"mean <sx> {v[:, 0].mean():.4f} (seed scatter {v[:, 0].std(ddof=1):.4f})" + (f"; exact {ex[0]:.4f}; E ends {v[:, 3].mean():.4f} vs exact {ex[1]:.4f}" if ex else ""))
