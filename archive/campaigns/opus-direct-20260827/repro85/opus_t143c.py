"""T143c - a control that actually bites, and the threshold read with its resolution floor.

T143b's second sanity check ('all l^2 = 1 must give p > 0') returned 0 -- and my
EXPECTATION was wrong, not the code: all edges equal IS a valid regular 4-simplex.
A control that fails to fail is worthless, so here is one that must bite: violate
the triangle inequality outright by making one edge longer than the path around."""
import numpy as np, itertools, sys
sys.path.insert(0,".")
from opus_t143b import prep, bad_fraction
l2,IJ,NT=prep(3)
print(f"T143c  controls, {NT} simplices")
print(f"   flat lattice                          p = {bad_fraction(l2,IJ):.6f}   (must be 0)")
v=l2.copy(); v[0]=100.0
print(f"   ONE edge blown up to l^2=100          p = {bad_fraction(v,IJ):.6f}   (must be > 0)")
v=l2.copy(); v[:]=1.0; v[::7]=25.0
print(f"   triangle inequality violated broadly  p = {bad_fraction(v,IJ):.6f}   (must be large)")
print(f"   all l^2 = 1 (regular simplices)       p = {bad_fraction(np.ones_like(l2),IJ):.6f}   (correctly 0 -- valid geometry)")
print()
rng=np.random.default_rng(7)
print("   fine scan under the PHYSICAL snapping model (uniform +-q/2), 200 trials")
print(f"   {'q (a^2)':>9} {'l_0/a':>8} {'p':>12} {'95% upper bnd':>15}")
for q in (0.195,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.70):
    ps=[bad_fraction(l2+rng.uniform(-q/2,q/2,size=len(l2)),IJ) for _ in range(200)]
    m=np.mean(ps); tot=int(round(m*NT*200))
    ub=(tot+2.0)/(NT*200)
    mk=" <-- l_P^2 range" if q in (0.195,0.25) else ""
    print(f"   {q:9.3f} {np.sqrt(q):8.4f} {m:12.6f} {ub:15.2e}{mk}")
print()
print(f"   resolution floor at L=3: one bad simplex in 200 trials = {1.0/(NT*200):.2e}")
