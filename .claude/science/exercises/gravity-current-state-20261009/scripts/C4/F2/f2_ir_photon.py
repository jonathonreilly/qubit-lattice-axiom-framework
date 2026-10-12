"""F2: photon speed (continuous-time Z^3 QED) with the B-term probe momentum scaled to the IR mass
(kx = m/10, m/5, Richardson), fixing the kx ~ m contamination of f2_ir.py's photon rows.
Usage: python f2_ir_photon.py"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from f2_ir import photon
u = 16 * np.pi ** 2
for m in (0.2, 0.1, 0.07, 0.05, 0.035, 0.025):
    L = int(np.ceil(20 / m / 8) * 8)
    aE, aB = photon(L, m, kxs=(m / 10, m / 5))
    aE2, aB2 = photon(L, m, kxs=(m / 20, m / 10))
    print(f"m={m:6.3f} L={L:4d}  per Dirac dc_gamma*16pi^2 = {u*(aB-aE)/16:+.6f}  (kx/2: {u*(aB2-aE2)/16:+.6f})  naive(8) {u*(aB-aE)/2:+.5f}", flush=True)
