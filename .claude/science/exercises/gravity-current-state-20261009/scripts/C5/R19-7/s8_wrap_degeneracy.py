"""R19-7 s8: wrap degeneracy of each ED cluster. Per slot type (xx yy zz xy yz xz): how many (nonzero, XOR-deduped) moves touch
one slot of that type, and the max number of gamma-charged edges a single move creates from n = 0 (non-wrapping value: s3b of R19-1 = 12
edges touched). Moves that touch no slot of a type freeze that label (its variance is 0 in the trivial coset)."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from tcommon import *
for h in [(2, 2, 2, 0, 0, 0), (2, 1, 3, 1, 0, 0), (2, 1, 4, 1, 0, 0), (1, 1, 4, 0, 0, 0), (4, 4, 4, 0, 0, 0)]:
    T = Torus(*h); P = T.P() % 2; G = T.G(); V = T.V
    nz = P[P.sum(1) > 0]
    touch = [int((nz[:, t*V:(t+1)*V].sum(1) > 0).sum()) for t in range(6)]
    per_slot = [nz[:, t*V].sum() for t in range(6)]
    ch = (np.abs(G @ nz.T) > 0).sum(0)   # edges with nonzero Gn after one move from n = 0 (all-plus lift)
    print("torus %-20s V=%3d moves(nonzero)=%3d  moves touching each slot (type xx yy zz xy yz xz): %s  charged edges from n=0: %s" %
          (h, V, len(nz), per_slot, sorted(set(ch.tolist()))))
