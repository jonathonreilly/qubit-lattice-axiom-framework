"""Autocorrelation of the walker-level local energy E_L along a path (8^3, guide exp(0.2 N_flip) + beta modes), and growth of the variance of the
accumulated -int E_L dt without resampling. usage: python3 elcorr.py L NW SEED BETA
Population equilibrated for 500 generations with resampling, then 300 generations (4.5 time units) evolved WITHOUT resampling and without using the weights
(the unweighted guided jump process, a diagnostic of the memory of E_L along a path, not of the weighted ensemble)."""
import sys, time
from gguide_lib import *

L, NW, SEED, BETA = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
t0 = time.time()
ice = Ice(L)
PH = cyclic_modes(ice, [1]); beta = np.full(3, BETA)
rr = np.random.default_rng(SEED * 100 + L + NW)
init = loop_vmc_g(ice, ALPHA, PH, beta, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
pr = GProjector(ice, ALPHA, beta, PH, V=0.0, seed=SEED)
st = pr.make_state(init, NW, rr)
logw = np.zeros(NW); EL = np.zeros(NW)
for g in range(500):
    if g % 10 == 0 and g > 0:
        st["Om"] = np.ascontiguousarray(st["sig"].astype(np.float64) @ pr.PH)
    pr._walk(st, DTAU, logw, EL)
    mx = logw.max(); w = np.exp(logw - mx); wn = w / w.sum()
    cum = np.cumsum(wn)
    picks = np.minimum(np.searchsorted(cum, (np.arange(NW) + rr.random()) / NW), NW - 1)
    for key in ("sig", "C", "flp", "dN", "rate0", "cls", "nflp", "Om"):
        st[key] = st[key][picks]
NG = 300
E = np.zeros((NG + 1, NW))
pr._walk(st, 1e-9, logw, EL); E[0] = EL
lwacc = np.zeros(NW); acc_var = []
for g in range(1, NG + 1):
    pr._walk(st, DTAU, logw, EL)
    E[g] = EL; lwacc += logw
    acc_var.append(lwacc.var())
d = E - E.mean(axis=1, keepdims=True)           # remove the population mean per generation (keeps the within-population fluctuation)
var0 = (E[0] - E[0].mean()).var()
C = lambda k: float((d[0] * d[k]).mean() / var0)
print(f"L {L} NW {NW} seed {SEED} beta {BETA}: sd(E_L) at t=0 {np.sqrt(var0):.3f}; corr C(t) = <dE(0) dE(t)>/var: " +
      " ".join(f"t={k * DTAU:.2f}:{C(k):.3f}" for k in (1, 3, 7, 14, 33, 67, 133, 200, 300)) + "; sd of accumulated log weight (no resampling) after t = " +
      " ".join(f"{k * DTAU:.2f}:{np.sqrt(acc_var[k - 1]):.3f}" for k in (1, 7, 33, 67, 133, 300)) +
      f"; frozen-E_L prediction sd(E_L) t: {np.sqrt(var0) * DTAU:.3f} (t=0.015), {np.sqrt(var0) * 1.005:.2f} (t=1.0); {time.time() - t0:.0f} s", flush=True)
