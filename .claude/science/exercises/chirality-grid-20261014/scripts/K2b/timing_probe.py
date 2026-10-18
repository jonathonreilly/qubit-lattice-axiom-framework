"""timing/convergence probe only (no reading): torus entry cost vs quadrature."""
import numpy as np, time
from lat2d import *
for T in [6, 8, 10]:
    G = Geom(2, T, True, 1); rng = np.random.default_rng(1); Fs, Bs = G.crossing_mats()
    U = [rand_half(rng, G, 0.25, 0.6) for _ in range(2)]
    for (n, nw) in [(3, 4), (3, 6), (4, 6), (4, 8), (6, 12)]:
        t0 = time.time(); ph, w = nodes(G, U[0], U[1], 0.6, n, 'tri', nw)
        l, g = logdet_batch(G, G.D0(U[0], U[1]), Fs, Bs, ph, 'O', chunk=32)
        lm = l.real.max(); v = np.sum(w * np.exp(l - lm))
        print(T, n, nw, len(w), f"{(np.log(v)+lm).real:.15f}", f"{time.time()-t0:.2f}s", flush=True)
