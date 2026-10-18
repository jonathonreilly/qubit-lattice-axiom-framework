import sys, time, numpy as np
sys.path.insert(0, '.')
import canon_tri as CT
for which in [(4,), ()]:
    t0 = time.time()
    OFF, base, vol, ncell, sizes = CT.build(which)
    print(f"orbits {which}: {ncell} Delaunay cell classes, sizes {sorted(set(sizes))}; {len(base)} simplices; {len(OFF)} vertex types; volume {vol:.6f}; {time.time()-t0:.1f}s")
