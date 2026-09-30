"""Kill check K5: try to calibrate the attacker's Kitaev-Preskill test (Test B).  The pre-registered PASS was
'gamma = 1 bit'; the attacker's toric-code control returns -3 bits, so the regions are not a clean KP disc.
Here: regions = edges owned (by tail vertex) by three vertex-wedges of a disc; also a Levin-Wen annulus check
(gamma = (S_annulus-inner-region...) not needed).  Report KP for toric code, BKSF, product."""
import math, sys
import numpy as np
from bksf_tee import bksf, toric, product, kp, entropy

def wedge_regions(T, cx, cy, rad, rot):
    L = T.L; sec = [set(), set(), set()]
    for i in range(L):
        for j in range(L):
            if (i-cx)**2 + (j-cy)**2 <= rad*rad:
                ang = (math.atan2(j-cy+1e-3, i-cx+2e-3) + rot) % (2*math.pi)
                k = int(ang // (2*math.pi/3))
                for d in (0, 1): sec[k].add(T.e(i, j, d))       # edges owned by tail vertex
                sec[k].add(T.e(i-1, j, 0)); sec[k].add(T.e(i, j-1, 1))  # and edges pointing INTO the vertex
    seen = set(); out = []
    for s in sec:
        s2 = s - seen; out.append(s2); seen |= s2
    return out

if __name__ == '__main__':
    L = 10
    for name, f in (('toric', toric), ('BKSF', bksf), ('product', product)):
        T, G = f(L); n = T.n
        vals = []
        for (cx, cy, rad) in [(4.5, 4.5, 2.0), (5, 5, 2.5), (5, 5, 3.0), (4.6, 5.2, 3.3)]:
            for rot in (0.0, 0.5, 1.1):
                vals.append(kp(G, n, wedge_regions(T, cx, cy, rad, rot)))
        print(name, 'KP (bits):', vals, flush=True)
