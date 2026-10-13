"""R19-7 s7: the v -> +infinity and v -> -infinity limits. H/v -> D(C) = sum_m exp(-bU Delta_m(C)/2) (diagonal).
Count classical minimisers (v>0) and maximisers (v<0) of D on each cluster at bU = 1, 2, 3; report their E = sum gamma^2,
label totals, and min over moves of Delta_m. Degeneracy growth with V decides 'crystal' (finite) vs 'extensive'."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from ed import *
for h in [(2, 2, 2, 0, 0, 0), (2, 1, 3, 1, 0, 0), (2, 1, 4, 1, 0, 0), (2, 1, 2, 1, 0, 0)]:
    mod = Model(Torus(*h)); V = mod.V
    print("torus %s V=%d N=%d  #gamma=0 states in coset: %d" % (h, V, mod.N, int((mod.E == 0).sum())))
    for bU in [1.0, 2.0, 3.0]:
        D = mod.Dsum(bU)
        for sgn, nm in [(1, "min (v>0)"), (-1, "max (v<0)")]:
            x = sgn*D; best = x.min(); deg = np.nonzero(x <= best + 1e-9*abs(best) + 1e-12)[0]
            bits = mod.bits(0, mod.N)[deg]
            tot = bits.reshape(len(deg), 6, V).sum(2)
            mind = mod.dE[:, deg].min(0)
            print("   bU=%.0f %s: D=%.6g  degeneracy %d  E of minimisers %s  min_m Delta %s  label totals (xx yy zz xy yz xz) %s" %
                  (bU, nm, sgn*best, len(deg), sorted(set(mod.E[deg].astype(int).tolist())), sorted(set(mind.astype(int).tolist())),
                   [tuple(int(a) for a in r) for r in tot[:4]]))
