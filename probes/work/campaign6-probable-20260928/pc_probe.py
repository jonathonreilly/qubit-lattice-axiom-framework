"""Population-control-corrected energy per plaquette at h = 0 versus the correction window Lc."""
import sys, time
from fw_lib import *

L, NW, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
NGEN = int(sys.argv[4]) if len(sys.argv) > 4 else 2000
LCS = (0, 10, 20, 40, 80, 160, 320, 640)
t0 = time.time()
ice = Ice(L)
rr = np.random.default_rng(SEED * 100 + L + NW)
init = loop_vmc(ice, ALPHA, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
pr = Projector(ice, np.ones(ice.np_, bool), ALPHA, 0.0, np.zeros((1, ice.nl), complex), SEED)
z = np.zeros(ice.nl)
out, res = energy_run(pr, init, NW, NGEN, DTAU, NGEN // 4, rr, z, z, Lcs=LCS)
nplaq = 3 * ice.nv
lw = res["lwbar"][NGEN // 4:]
print(f"L {L} NW {NW} seed {SEED}: sd(log mean weight) per generation {lw.std():.4f}; {time.time() - t0:.0f} s")
print("  " + "; ".join(f"Lc {Lc} ({Lc * DTAU:.2f}): u {-out[Lc][0] / nplaq:.5f}+-{out[Lc][1] / nplaq:.5f}" for Lc in LCS), flush=True)
