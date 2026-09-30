import numpy as np, sys
sys.path.insert(0,'.')
from m2_torus import run
for L in (12,16):
    o=[(1,0,0),(2,1,0),(1,1,0),(2,1,1),(2,2,1),(3,1,0),(1,1,1),(3,2,1),(3,1,1)]
    r=run(L,0.0,o)
    print("L=%d m=0"%L, {k:round(float(v),4) for k,v in r.items()})
    # plaquette-count (l1) normalisation: eta_l1 = eta_euclid * |n|_2 / |n|_1
    print("   per-plaquette (l1) area:", {k:round(float(v*np.sqrt(sum(c*c for c in k))/sum(abs(c) for c in k)),4) for k,v in r.items()})
