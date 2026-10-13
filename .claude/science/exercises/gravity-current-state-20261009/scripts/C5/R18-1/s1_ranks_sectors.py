"""R18-1 s1 (written before running). (a) Move-set checks.
- every pattern (cube, 3 mu8 orientations) is F2-invariant (G v = 0 mod 2) on the torus;
- dim ker_F2 G vs dim span(move translates): codim = sectors the local moves cannot connect;
- the integer charges a single cube / mu8 flip creates from n = 0 (cost at bU = infinity)."""
import numpy as np, sys
from common import *
print("patterns:", len(PATTERNS), "(cube copies: %d, mu8 copies: %d)" % (len(orbit(CUBE)), len(orbit(MU8))))
for L in [2, 3, 4, 5, 6]:
    G = G_matrix(L); V = L**3; P = pattern_vectors(L)
    inv = np.all((G @ P.T) % 2 == 0)
    rG = f2_rank(G); kerG = 6*V - rG; rP = f2_rank(P)
    print("L=%d: slots %d, edges %d, rank_F2 G = %d, dim ker = %d, dim span(moves) = %d, codim = %d, all moves invariant: %s"
          % (L, 6*V, 3*V, rG, kerG, rP, kerG - rP, inv), flush=True)
    if L == 4:
        for name, p in [("cube", PATTERNS[0]), ("mu8", PATTERNS[1])]:
            v = pattern_vectors(L)[[0, V][0 if name == "cube" else 1]]
            g = G @ v; gam = g // 2
            print("   %s flip from n=0: charged edges = %d, sum gamma^2 = %d, integer Gn values %s" %
                  (name, np.count_nonzero(g), int((gam**2).sum()), sorted(set(g[g != 0].tolist()))))
