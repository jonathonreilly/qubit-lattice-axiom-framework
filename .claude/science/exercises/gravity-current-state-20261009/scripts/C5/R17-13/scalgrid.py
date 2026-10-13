"""R17-13 scalgrid: U-vertex scalar G_w(b_s, fr*(pi-b_s)) rows (Xi_T2g, Xi_Eg, mu_E) at m=0.01 (archived content4.scalw), saved."""
import sys, numpy as np
sys.path.insert(0, sys.argv[1])
from content4 import scalw
out = []
for bs in (0.5, 1.0, 1.5, 2.0, 2.2, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.05, 3.1):
    for fr in (0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0):
        v = scalw(bs, fr, 0.01, vert='U')[0]; out.append([bs, fr, *v[:3]])
np.save('scalgrid.npy', np.array(out)); print('saved', len(out))
