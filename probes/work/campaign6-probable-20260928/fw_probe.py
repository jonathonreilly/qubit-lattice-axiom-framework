"""Forward-walking transverse structure factor at h = 0 vs the Cauchy-Schwarz ceiling s sqrt(u chi)."""
import sys, time
from fw_lib import *

L, NW, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
NGEN = int(sys.argv[4]) if len(sys.argv) > 4 else 4000
LAGS = (0, 67, 133, 200, 267, 400, 533)
t0 = time.time()
ice = Ice(L); k = 2 * np.pi / L
hv, PH = triple(ice, k)
rr = np.random.default_rng(SEED * 100 + L + NW)
init = loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
pr = Projector(ice, np.ones(ice.np_, bool), ALPHA, 0.0, PH, SEED)
res = pr.run(init, NW, NGEN, DTAU, NGEN // 2, LAGS, rr)
e = res["e"][NGEN // 2:]
u = -float(e.mean()) / (3 * ice.nv)
fw = res["fw"]                                   # (n_post, nlags, nobs)
S = fw[:, :, :3].mean(axis=2)                    # triple-averaged |O|^2 per generation and lag
nb_ = 10
rows = []
for j, lag in enumerate(LAGS):
    x = S[:, j]; bins = np.array([c.mean() for c in np.array_split(x, nb_)])
    rows.append(f"lag {lag * DTAU:5.2f}: S {x.mean():.4f}+-{bins.std(ddof=1) / np.sqrt(nb_):.4f} distinct {res['nd'][:, j].mean():.3f}")
s = 2 * np.sin(k / 2)
print(f"L {L} NW {NW} seed {SEED}: u {u:.5f}; s {s:.4f}; ceiling s sqrt(u chi) at chi 1.00/1.05/1.10: "
      f"{s * np.sqrt(u * 1.0):.4f}/{s * np.sqrt(u * 1.05):.4f}/{s * np.sqrt(u * 1.10):.4f}; {time.time() - t0:.0f} s")
print("  " + "\n  ".join(rows), flush=True)
