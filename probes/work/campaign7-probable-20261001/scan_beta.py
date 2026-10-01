"""One guide-comparison run: python3 scan_beta.py L NW SEED NGEN BETA [MS] [ALPHA] -- prints one summary line.
Per-generation statistics after thermalisation (NGEN//4 generations): sd of log mean weight, effective sample fraction, sd of walker log weights,
hops per generation, fraction of distinct ancestors at lags of 1, 10, 33, 67 (=1.0), 133 (=2.0) generations (dtau = 0.015), energy per plaquette."""
import sys, time
from gguide_lib import *

L, NW, SEED, NGEN = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
BETA = sys.argv[5]                  # one number, or a comma list with one beta per momentum in MS (each applied to the triple)
MS = [int(x) for x in sys.argv[6].split(",")] if len(sys.argv) > 6 else [1]
ALPHA_ = float(sys.argv[7]) if len(sys.argv) > 7 else ALPHA
DT = float(sys.argv[8]) if len(sys.argv) > 8 else DTAU
LAGS = [1] + [max(1, int(round(t / DT))) for t in (0.15, 0.5, 1.0, 2.0)]    # generations; projection times 0.15, 0.5, 1.0, 2.0
t0 = time.time()
ice = Ice(L)
PH = cyclic_modes(ice, MS)
bl = [float(x) for x in BETA.split(",")]
beta = np.repeat(bl, 3) if len(bl) > 1 else np.full(PH.shape[1], bl[0])
assert len(beta) == PH.shape[1]
rr = np.random.default_rng(SEED * 100 + L + NW)
init = loop_vmc_g(ice, ALPHA_, PH, beta, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
t_init = time.time() - t0
pr = GProjector(ice, ALPHA_, beta, PH, V=0.0, seed=SEED)
THERM = NGEN // 4
res = pr.run(init, NW, NGEN, DT, THERM, LAGS, rr)
es = energy_summary(res, Lcs=(0, 40))
Np = ice.np_
lw = res["lwbar"][THERM:]
nd = res["nd"].mean(axis=0)
hops = res["hops"][THERM:].mean()
print(f"L {L} NW {NW} seed {SEED} NGEN {NGEN} beta {BETA} ms {MS} alpha {ALPHA_} dtau {DT}: sd(log mean wt) {lw.std():.5f}; ESS frac {res['ess'][THERM:].mean():.4f}; "
      f"sd(walker log wt) {res['lwsd'][THERM:].mean():.4f}; hops/gen {hops:.0f}; "
      f"distinct anc @lag(gens) " + " ".join(f"{l}g({l * DT:.2f}):{x:.4f}" for l, x in zip(LAGS, nd)) +
      f"; u(Lc=0) {-es[0][0] / Np:.5f}+-{es[0][1] / Np:.5f}; u(Lc=40) {-es[40][0] / Np:.5f}+-{es[40][1] / Np:.5f}; "
      f"<N_flip>/Np {res['nflp'].mean():.4f}; K {pr.K}; init {t_init:.0f} s; run {res['wall']:.0f} s; total {time.time() - t0:.0f} s", flush=True)
