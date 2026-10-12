"""F2: IR-resolved anisotropy scan (m = lam = 0.3, so L*m >= 10) of f2_aniso.py, with the continuous-time
reference at the same (m, lam) from f2_ir.py's formulas. Probe momenta for Pi scaled to m/10, m/5.
Usage: python f2_aniso_resolved.py"""
import numpy as np, sys, time
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from f2_aniso import fermion as f4, photon as p4
from f2_ir import fermion as f3, photon as p3
u = 16 * np.pi ** 2
m = lam = 0.3
t0 = time.time()
a0, a1, _ = f3(160, m, lam); aE, aB = p3(160, m, kxs=(m / 10, m / 5))
print(f"continuous time (xi=inf), L=160: dc_f={u*(a1-a0):+.4f}  dc_gamma per Dirac={u*(aB-aE)/16:+.5f}  "
      f"Delta(3D stag, 2 tastes)={u*(a1-a0)-u*(aB-aE)/4:+.4f}  Delta per-Dirac-photon={u*(a1-a0)-u*(aB-aE)/16:+.4f}", flush=True)
for L in (40, 56):
    for xi in (1.0, 1.5, 2.0, 4.0, 8.0):
        b0, bx, _ = f4(L, xi, m, lam); cE, cB = p4(L, xi, m, ks=(m / 10, m / 5))
        dcf = u * (bx - b0); dcgD = u * (cB - cE) / 32
        print(f"L={L} xi={xi:4.1f}: dc_f={dcf:+.4f}  dc_gamma per Dirac={dcgD:+.5f}  Delta(4D stag, 4 tastes)={dcf-4*dcgD:+.4f}  "
              f"Delta per-Dirac-photon={dcf-dcgD:+.4f}  [{time.time()-t0:.0f}s]", flush=True)
