"""
T215 - locate lambda_c for the consistent record field of R136, and check the
two Binder limits as controls.

  disordered: m is a 3-component Gaussian  => <m^4>/<m^2>^2 = 5/3 => U = 4/9 = 0.4444
  ordered   : m^4 = (m^2)^2                                      => U = 2/3 = 0.6667
Both limits must be reproduced by the simulation or the measurement is worthless.
"""
import numpy as np, time
from opus_t214 import run

print("controls: disordered U -> 4/9 = 0.44444 ; ordered U -> 2/3 = 0.66667")
print("\n  lam    " + "".join(f"    L={L:2d}  U        " for L in (8,12,16)))
res = {}
for lam in (0.62, 0.66, 0.70, 0.72, 0.74, 0.78):
    row = f"  {lam:4.2f}  "
    for L in (8, 12, 16):
        t0 = time.time()
        m2, U = run(L, lam, nwarm=4000, nmeas=20000, seed=777+L)
        res[(lam, L)] = U
        row += f"  {U:7.4f} ({time.time()-t0:4.0f}s)"
    print(row)

print("\n  sign of dU/dL  (negative = disordered, positive = ordered):")
for lam in (0.62, 0.66, 0.70, 0.72, 0.74, 0.78):
    d1 = res[(lam,12)] - res[(lam,8)]
    d2 = res[(lam,16)] - res[(lam,12)]
    print(f"   lam={lam:4.2f}:  U(12)-U(8) = {d1:+.4f}   U(16)-U(12) = {d2:+.4f}   "
          f"{'ORDERED' if d2 > 0.002 else ('disordered' if d2 < -0.002 else 'CRITICAL (flat)')}")
