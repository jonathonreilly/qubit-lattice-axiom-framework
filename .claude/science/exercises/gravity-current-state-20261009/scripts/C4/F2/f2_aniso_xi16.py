"""F2: xi = 16 point and an exact-zero check at xi = 1 (prints raw magnitudes) for f2_aniso.py.
Usage: python f2_aniso_xi16.py"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from f2_aniso import fermion, photon
u = 16 * np.pi ** 2
m, lam = 0.1, 0.2
for (L, xi) in [(24, 1.0), (32, 16.0)]:
    a0, ax, A2 = fermion(L, xi, m, lam)
    aE, aB = photon(L, xi, m)
    print(f"L={L} xi={xi}: a0={u*a0:+.12f} ax={u*ax:+.12f} dc_f*16pi^2={u*(ax-a0):+.3e}  aE={u*aE:+.10f} aB={u*aB:+.10f} "
          f"dc_gamma per Dirac={u*(aB-aE)/32:+.6f}  Delta(4D stag)={u*(ax-a0)-u*(aB-aE)/8:+.4f}", flush=True)
print("continuous-time reference at m=0.1, lam=0.2 (f2_ir.out, f2_ir_photon.out): dc_f = -15.978, dc_gamma per Dirac = -0.6579")
