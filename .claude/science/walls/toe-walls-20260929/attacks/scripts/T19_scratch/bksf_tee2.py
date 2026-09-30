"""Test B2: calibrated topological-entropy check for the BKSF vacuum.
(1) Local-stabilizer degeneracy on the torus (definition of topological quantum order for stabilizer codes).
(2) Kitaev-Preskill gamma with regions built from whole plaquettes (edge set of a plaquette patch), calibrated on the toric code.
"""
import numpy as np, math, sys
from bksf_tee import *

def plaq_edges(T, i, j):
    return {T.e(i, j, 0), T.e(i + 1, j, 1), T.e(i, j + 1, 0), T.e(i, j, 1)}

def patch_sectors(T, cx, cy, rad, nsec=3, rot=0.3):
    L = T.L
    sec = [set() for _ in range(nsec)]
    for i in range(L):
        for j in range(L):
            x, y = i + .5, j + .5
            if (x - cx) ** 2 + (y - cy) ** 2 <= rad * rad:
                ang = (math.atan2(y - cy, x - cx) + rot) % (2 * math.pi)
                sec[int(ang // (2 * math.pi / nsec))] |= plaq_edges(T, i, j)
    return sec

def kp_sets(G, n, sec):
    # regions are edge sets; sectors may share boundary edges -> make disjoint by assigning shared edge to the lowest sector
    seen = set(); out = []
    for s in sec:
        s2 = set(s) - seen; out.append(s2); seen |= s2
    return kp(G, n, out), [len(s) for s in out]

def local_generators_bksf(L):
    T, G = bksf(L)
    return T, G[:-2]          # B_v and plaquette loops only

if __name__ == '__main__':
    for L in (6, 8):
        print(f"=== torus L={L}")
        for name, f, loc in (('BKSF vacuum', bksf, local_generators_bksf), ('toric code', toric, toric), ('product', product, product)):
            T, G = f(L); n = T.n
            _, Gl = loc(L)
            rl = gf2_rank(Gl); rf = gf2_rank(G)
            print(f"{name}: rank(local gens)={rl}, rank(all gens)={rf}, n={n} -> local-stabilizer ground space dim 2^{n-rl}")
            vals = []
            for (cx, cy, rad) in [(L / 2, L / 2, 2.0), (L / 2, L / 2, 2.6), (L / 2, L / 2, 3.0), (L / 2 + .5, L / 2 + .5, 2.4)]:
                for rot in (0.0, 0.7):
                    g, sz = kp_sets(G, n, patch_sectors(T, cx, cy, rad, 3, rot))
                    vals.append(g)
            print("   KP values (bits):", vals)
