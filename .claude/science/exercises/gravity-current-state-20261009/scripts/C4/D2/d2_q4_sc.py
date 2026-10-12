"""D2: self-consistent one-loop check of the degenerate-Cherenkov face cusp (band (1-cos k)^2,
c = 1.0, a = 0.5).  Grid N = 2048 (delta >= 3.1e-3).  Reports Z(pi), gap to lowest pole, face
chord slopes s(j dk) for j = 1, 4, 16, 64 and the SLAC-fit deviation on windows."""
import numpy as np, time
from d2_common import *
N = 2048
for g2 in [0.1, 0.03, 0.01]:
    t = time.time()
    r = dressed_band_1d('Q4', N, 1.0, g2, 0.5, sc=True, maxsc=300, mix=0.5)
    k, E = r['k'], r['E']; dk = k[1] - k[0]; n = len(k) - 1
    s = [(E[-1] - E[n - j])/(j*dk) for j in (1, 4, 16, 64)]
    fits = [slac_fit(k, E, w) for w in (np.pi/8, np.pi/4, np.pi/2)]
    print(f"Q4 SC c=1.0 g2={g2} N={N} | E(pi)={E[-1]:.6f} Z(pi)={r['Z'][-1]:.3e} gap={r['gap'][-1]:.2e} | s(1,4,16,64 dk)="
          + " ".join(f"{x:.4f}" for x in s) + " | SLAC dev/bw w=pi/8,pi/4,pi/2: " + " ".join(f"{f[2]:.4f}" for f in fits)
          + f" | Z(k=pi-0.2)={r['Z'][n-int(0.2/dk)]:.3e} | it={r['it']} res={r['res']:.1e} t={time.time()-t:.0f}s", flush=True)
