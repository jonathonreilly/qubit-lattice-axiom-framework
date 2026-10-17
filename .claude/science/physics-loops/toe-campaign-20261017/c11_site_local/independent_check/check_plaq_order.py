"""Sign of the plaquette generator: cyclic hop product is independent of start point and direction
(equals the companion note's order A(v,b)A(v+b,a)A(v+a,b)A(v,a)); all 720 orderings, half-edge L=4."""
import itertools
from ilib import *
H = HalfModel(4); bad = 0; herm = 0
for o in itertools.permutations(range(6)):
    for (a, b) in PLANES:
        v = (1, 1, 1)
        hs = [H.A(o, w, c) for (w, c) in plaq_hops(H, v, a, b)]
        prods = set()
        for k in range(4):
            for seq in (hs[k:] + hs[:k], (hs[k:] + hs[:k])[::-1]):
                P = (0, 0, 0)
                for h in seq: P = pmul(P, h)
                prods.add(P)
        if len(prods) != 1: bad += 1
        P = prods.pop()
        if pdag(P) != P: herm += 1
print('orderings x planes with start/direction-dependent sign:', bad, '; non-Hermitian:', herm)
