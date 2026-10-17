"""Longer runs of the two validation points (contents (3,1,2) N=2 g=0.5; content-less N=4 g=0.3) on 4^3, 4 seeds."""
import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
import numpy as np, lock_mc as M
for s in range(4):
    r, _ = M.run_point(4, 2/64, 0.5, (3, 1, 2), "rand", 100+s, neq=500, nmeas=200000, every=2)
    r2, _ = M.run_point(4, 4/64, 0.3, None, "rand", 200+s, neq=500, nmeas=200000, every=2)
    print(f"seed {s}: contents P(bond)={2*r['bonds_per_rec']:.5f} (exact 0.05) | contentless bonds/rec={r2['bonds_per_rec']:.5f} (exact 0.04780)", flush=True)
