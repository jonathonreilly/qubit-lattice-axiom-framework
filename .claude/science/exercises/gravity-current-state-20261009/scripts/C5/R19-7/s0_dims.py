"""R19-7 s0: (i) gcommon reproduces common at cubic L=2,3; (ii) coset (move-span) dimension d for candidate tori."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from gcommon import *
for L in [2, 3]:
    print("L=%d cubic: G equal %s, P equal %s" % (L, np.array_equal(G_matrix(L), G_matrix_a((L, L, L))),
          np.array_equal(pattern_vectors(L) % 2, pattern_vectors_a((L, L, L)) % 2)))
for Ls in [(2,2,2), (2,2,3), (2,2,4), (2,2,5), (2,2,6), (2,2,8), (1,2,4), (2,3,3), (3,3,3)]:
    P = pattern_vectors_a(Ls) % 2; G = G_matrix_a(Ls)
    d = f2_rank(P); dk = 6*np.prod(Ls) - f2_rank(G % 2)
    ok = np.all((G @ P.T) % 2 == 0)
    print("Ls=%s slots=%d moves=%d span dim d=%d  ker_F2(G) dim=%d  all moves Gn even: %s" % (Ls, 6*np.prod(Ls), len(P), d, dk, ok))
