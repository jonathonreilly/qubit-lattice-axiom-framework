"""Comparator: SLAC-fit deviation of the bare flat-bottom band (1-cos k)^2 and of its
c = 1.0 one-phonon threshold th(K) = min_q[eps(K-q) + 2c|sin(q/2)|] on windows [pi - w, pi]
(grid N = 2048 as in d2_q4_sc.py), plus SLAC face slope for each fit."""
import numpy as np
from d2_common import slac_fit
N = 2048; k = 2*np.pi*np.arange(N//2 + 1)/N
eps = (1 - np.cos(k))**2
qq = 2*np.pi*np.arange(1, 65536)/65536
th = np.array([np.min((1 - np.cos(K - qq))**2 + 2.0*np.abs(np.sin(qq/2))) for K in k])
for name, E in [('bare Q4', eps), ('threshold c=1', th)]:
    print(name, " ".join(f"w={w:.3f}: dev/bw={slac_fit(k, E, w)[2]:.4f} slope_ratio={slac_fit(k, E, w)[4]:.3f};" for w in (np.pi/8, np.pi/4, np.pi/2)))
