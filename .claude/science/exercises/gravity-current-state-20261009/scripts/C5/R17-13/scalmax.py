"""R17-13 scalmax: range of the U-vertex scalar G_w(b_s, w_s) rows at m = 0.01 (archived content4.scalw), esp. max mu_E^s."""
import sys, time, numpy as np
sys.path.insert(0, sys.argv[1])
from content4 import scalw
t0 = time.time(); best = None
for bs in (0.5, 1.0, 1.5, 2.0, 2.4, 2.6, 2.8, 2.9, 3.0, 3.05, 3.1):
    row = []
    for fr in (0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0):
        v = scalw(bs, fr, 0.01, vert='U')[0]; row.append(v[2])
        if best is None or v[2] > best[0]: best = (v[2], bs, fr, v[0], v[1])
    print('b_s=%.2f mu_E^s over fr=(.02,.05,.1,.2,.4,.6,.8,1): %s' % (bs, ' '.join('%+.2e' % x for x in row)), flush=True)
print('max mu_E^s = %+.4e at b_s=%.2f fr=%.2f (Xi_T2g %+.3e Xi_Eg %+.3e) [%.0fs]' % (*best, time.time()-t0))
