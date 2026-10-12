#!/usr/bin/env python3
"""R7-2: Rule C (unit-cube XOR = 0) on larger lattice balls; compare log2 N_adm with
(1/2) * sum over boundary of (|n_x|+|n_y|+|n_z|) dA -> 0.75 * 4 pi R^2 for a sphere (suggested asymptote).
Also an exact combinatorial identity: for any finite region, cube constraints fully inside are independent iff
their rank equals their number; we print both."""
import math, sys, time
sys.path.insert(0, '.')
from r72_cube_rule import count_region
for R in [6, 8, 10, 12, 14]:
    t = time.time()
    rng = range(-R - 1, R + 2)
    sites = [(x, y, z) for x in rng for y in rng for z in rng if x*x + y*y + z*z <= R*R]
    n, ncon, rk, k = count_region(sites)
    print(f"R={R}: sites={n}, cubes={ncon}, rank={rk} (independent: {rk==ncon}), log2 N_adm={k}, "
          f"k/(4 pi R^2)={k/(4*math.pi*R*R):.4f}, k/(4 pi (R+0.5)^2)={k/(4*math.pi*(R+0.5)**2):.4f}, t={time.time()-t:.1f}s", flush=True)
