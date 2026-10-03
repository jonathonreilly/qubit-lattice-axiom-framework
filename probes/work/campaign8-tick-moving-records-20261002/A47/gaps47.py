"""A47 gaps47: mean-field gap of the lp:<x> trial (NN soldered + face-diagonal i x s.d) at L = 6, 8 (APBC)."""
import sys, signal, numpy as np
signal.alarm(120)
sys.path.insert(0, __file__.rsplit('/', 2)[0] + "/A46")
from a46lib import *
for L in (6, 8):
    cl = cube(L)
    print(f"L={L}: " + "; ".join(f"x={x:.3f}: gap {mf_dual(cl, 0., 1., lam2=x)[1]:.3f}" for x in np.arange(0, 0.3001, 0.025)), flush=True)
