#!/usr/bin/env python3
"""Population-free transverse structure factor S(k = pi/4) on the 8^3 ring torus by reptation (no walker population).

Setting (supplied model, nothing here is a framework premise): spin-1/2 link fields sigma = +-1 on the cubic 8^3 torus, exact vertex Gauss law,
H = -g sum_p (U_p + U_p^dag), g = 1 (pure ring point, V = 0), the canonical zero-winding flip component, guide exp(0.2 N_flip) (the guide of the
landed forward-walking run).  S = <0| (1/3) sum_a O_a^dag O_a |0> with the cyclic triple O_a = N^-1/2 sum_{a-links l} e^{i k x_(a+1)(l)} sigma_l
(fw_lib.triple), k = 2 pi / 8.

Estimator.  One path of Mseg segments of imaginary time dur (path length Mseg*dur) is sampled by importance-sampled bounce reptation
(rq3_lib.rq_run_S: grow a segment at the leading end, delete one at the other end, accept min(1, exp(W_new - W_old)), bounce on rejection).
For a long path the configuration at the MIDDLE of the path is distributed as |phi|^2, phi = exp(-(path/2) H) psi_G -> psi_0 (pure); the two
ends give the mixed distribution psi_G phi.  Printed per chain and over chains:
  mid_cyc / mid_anti / mid_six : |O|^2 at the exact middle of the path (maintained incrementally; checked against a replay from the tail), for the cyclic
          triple (b = a + 1, the landed forward-walking observable), the anticyclic triple (b = a + 2) and all six modes (symmetry-equivalent; six = best)
  win_six : mean of |O|^2 (six modes) over the path boundaries j = JLO..JHI of 0..16 (default 4..12, the central half), each a pure sample if long enough
  ends_six: mean over the two end configurations (mixed estimate with the same guide as the projector's mixed estimate)
  u_ends  : energy per plaquette from the ends (mixed estimator of E0)
  shift range: (max - min of the signed shift of the path) / Mseg over the production run, i.e. how many path lengths of FRESH interior content were
          generated; the interior of the path is only replaced when the shift range exceeds Mseg (bounce reptation moves the path sub-diffusively: in the
          pilot D_eff fell from 0.5 seg^2/move at 1e4 moves to 0.03-0.15 at 1e6 moves; the old "renewals = moves / (Mseg^2 (1 - acc))" overstates the
          renewal rate by a factor 12-60 (4^3 ... 8^3 logs)).  Burn-in therefore runs until the shift range exceeds BURN_RANGE (default 2.5) path lengths.
Errors: per chain, 20 block errors (a LOWER bound: S_win has a slowly decaying autocorrelation); over chains, scatter of the chain means / sqrt(n).

START STATE.  Default: the canonical state sector_state(0), which is certainly in the canonical component.  With RS_INIT=loop the start is a loop-VMC
sample of |psi_G|^2 on the zero-winding Gauss sector (what the earlier projector/reptation runners used).  Pilot (8^3, one path shift range of ~1 path
length per chain): loop-start chains sat at chain-dependent cyclic-triple levels 0.38 ... 0.61 and canonical-start chains at 0.42 ... 0.48; on 6^3
(shift ranges ~1.2) loop and canonical starts agree (0.50 and 0.49).  The 8^3 spread is attributed to unflushed initial path content, not demonstrated
to be a separate flip component.

usage: rept8_S.py [nchains=4] [prod_moves=15000000] [burn_cap_moves=25000000] [seed0=100] [Mseg=800] [dur=0.025] [JLO=4] [JHI=12] [burn_range=2.5]
Defaults: path length 20 = 800 segments x 0.025, ~36 microseconds per move (8^3).  Measured at 8^3: a canonical-start chain of 2.5e6 moves (90 s) shifted its
path over a range of 1.64 path lengths (rms shift 0.57 path lengths at lag 1e6 moves); the same wall time with 1600 x 0.0125 gave ~1.0 and with
400 x 0.05 gave ~0.64.  Burn-in to 2.5 path lengths is expected to take ~5e6 - 1e7 moves (3 - 6 min), 1.5e7 production moves (9 min) give ~3 more path
lengths: ~12-15 min per chain, four chains ~ 1 hour.  Expected statistical error of win_six ~ +-0.02 (NOT +-0.01: that needs ~4x more, ~4 hours).
Memory: measured max RSS 321 MB for a 7e6-move chain at M = 1600 (rows kept in memory: 1.5e7/250 rows x 62 floats ~ 30 MB).
Run niced, single thread, one process:
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 /opt/homebrew/bin/python3 rept8_S.py
Saves data/rept8_<seed0>_c<chain>.npz (S rows [13 columns: 3 mid, 3 tail, 3 head, N_flip mid/tail/head, shift; then 6 mid amplitudes], E rows,
profile rows) for re-analysis (rept_S_analyze.py).
"""
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
import rq3_lib as R

AUDIT_TIMEOUT_SEC = 7200

arg = lambda i, d, f: f(sys.argv[i]) if len(sys.argv) > i else d
NCH, PROD, BURN, SEED0 = arg(1, 4, int), arg(2, 15000000, int), arg(3, 25000000, int), arg(4, 100, int)
MSEG, DUR, JLO, JHI = arg(5, 800, int), arg(6, 0.025, float), arg(7, 4, int), arg(8, 12, int)
BURN_RANGE = arg(9, 2.5, float)
L, ME = 8, 250
k = 2 * np.pi / L
CANON = os.environ.get("RS_INIT", "canon") != "loop"
ice = R.Ice(L)
T = R.QTables(ice)
t0 = time.time()


def blk(x, nb=20):
    b = np.array([c.mean() for c in np.array_split(x, nb)])
    return x.mean(), b.std(ddof=1) / np.sqrt(nb)


print(f"8^3, k = pi/4, path {MSEG * DUR:g} = {MSEG} x {DUR:g}, start {'canonical state' if CANON else 'loop-VMC sample'}, {NCH} chains x (burn-in until the path has shifted over "
      f"{BURN_RANGE:g} path lengths, cap {BURN} moves; then {PROD} production moves), measure every {ME}; win = boundaries {JLO}..{JHI} of 0..16; "
      f"expected ~{NCH * (min(BURN, 8e6) + PROD) * 3.6e-5 / 60:.0f} min", flush=True)
os.makedirs(os.path.join(HERE, "data"), exist_ok=True)
res = []
for c in range(NCH):
    rr = np.random.default_rng(SEED0 + c)
    if CANON:
        init = ice.sector_state(0)
    else:
        init = R.loop_vmc(ice, R.ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)[-1]
    o = R.reptation_S(ice, T, init, k, MSEG, DUR, PROD, BURN, ME, 1000 * (SEED0 + c) + 7, prof_every=ME, nprof=16, burn_range=BURN_RANGE, progress=100)
    st = o["stats"]
    acc = st[0] / (st[0] + st[1])
    S, P = o["S"], o["prof"]
    assert len(S) == len(P)
    u = R.unpack(S, P, JLO, JHI)
    X = u["shift"]
    lag = max(1, 30000 // ME)
    Dm = float(((X[lag:] - X[:-lag]) ** 2).mean() / (lag * ME)) if len(X) > 2 * lag else float("nan")
    ren = o['prod_range']
    el = 0.5 * (o["E"][:, 0] + o["E"][:, 1])
    chk = float(np.abs(P.mean(axis=1)[:, 8] - u["mid_six"]).max())
    ok = o["mid_ok"] and o["head_ok"] and o["bad"] == 0 and st[2] == 0 and chk < 1e-9
    vals = {n: blk(u[n]) for n in ("mid_cyc", "mid_anti", "mid_six", "win_six", "ends_six")}
    EE, EEe = blk(el)
    res.append([vals[n][0] for n in ("mid_cyc", "mid_anti", "mid_six", "win_six", "ends_six")] + [-EE / ice.np_, ren])
    print(f"chain {c} (seed {SEED0 + c}): burn-in {o['burn'][0]:.2e} moves (range {o['burn'][1]:.2f} M), production shift range {o['prod_range']:.2f} M; acceptance {acc:.3f}, D(3e4) {Dm:.3f} seg^2/move, integrity {'OK' if ok else 'FAILED'} (overflow {st[2]}, "
          f"build-overflow {o['bad']}, mid replay diff {chk:.1e}) | " + "  ".join(f"{n} {v[0]:.4f}+-{v[1]:.4f}" for n, v in vals.items())
          + f" | u_ends {-EE / ice.np_:.5f}+-{EEe / ice.np_:.5f} | {time.time() - t0:.0f} s", flush=True)
    fifths = lambda x: " ".join(f"{q.mean():.3f}" for q in np.array_split(x, 5))
    print(f"   by fifth of the production: win_six {fifths(u['win_six'])} | mid_six {fifths(u['mid_six'])} | ends_six {fifths(u['ends_six'])}", flush=True)
    print("   profile (six-mode mean, tail -> head, 17 boundaries): " + " ".join(f"{x:.3f}" for x in u["prof_six"].mean(axis=0)), flush=True)
    np.savez_compressed(os.path.join(HERE, "data", f"rept8_{SEED0}_c{c}.npz"), S=S.astype(np.float32), E=o["E"], prof=P.astype(np.float32), stats=st,
                        meas_every=ME, Mseg=MSEG, dur=DUR)
r = np.array(res)
n = len(r)
names = ("mid_cyc", "mid_anti", "mid_six", "win_six", "ends_six", "u_ends")
print(f"\nTOTAL production shift range (path lengths) {r[:, 6].sum():.1f}, wall {time.time() - t0:.0f} s")
if n >= 3:
    for i, name in enumerate(names):
        print(f"  {name:8s} = {r[:, i].mean():.5f} +- {r[:, i].std(ddof=1) / np.sqrt(n):.5f}   (chain scatter sd {r[:, i].std(ddof=1):.4f}, n = {n})")
    print("  comparison: forward-walking S(pi/4) on 8^3 = 0.4084 +- 0.0144 (7680 walkers, supplied by the brief)")
else:
    print("  fewer than 3 chains: no chain-scatter error; the block errors above are lower bounds")
