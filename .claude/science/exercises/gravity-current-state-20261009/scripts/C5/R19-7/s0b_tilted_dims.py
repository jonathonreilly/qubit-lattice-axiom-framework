"""R19-7 s0b: coset dimension d for small (tilted) tori; cubic check against common."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from tcommon import *
for L in [2, 3]:
    T = Torus(L, L, L)
    print("cubic L=%d: G equal %s P equal %s" % (L, np.array_equal(T.G(), G_matrix(L)), np.array_equal(T.P() % 2, pattern_vectors(L) % 2)))
cands = [(2,2,2,0,0,0), (2,1,2,1,0,0), (2,1,3,1,0,0), (2,1,4,1,0,0), (2,1,5,1,0,0), (2,1,6,1,0,0), (2,1,8,1,0,0),
         (2,2,3,0,0,0), (2,2,4,1,0,0), (2,2,4,0,1,1), (2,2,2,1,1,1), (1,1,4,0,0,0), (1,1,8,0,0,0), (1,1,6,0,0,0), (1,2,4,0,0,0),
         (2,1,4,1,1,0), (2,1,6,1,1,0), (2,1,4,0,0,0), (2,1,6,0,0,0)]
for c in cands:
    T = Torus(*c); P = T.P() % 2; G = T.G()
    d = f2_rank(P); ok = np.all((G @ P.T) % 2 == 0)
    print("HNF %s V=%d moves=%d d=%d  moves Gn even %s  nonzero moves %d" % (c, T.V, len(P), d, ok, int((P.sum(1) > 0).sum())))
