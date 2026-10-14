"""K2c quadrature/cost probe ONLY (no kernel matrix, no eigenvalue): log Z of one off-diagonal entry, HARD crossing weight,
for the overlap (O) and Wilson (W), as the GL node count n (per crossing plaquette) and Polyakov trapezoid nw vary."""
import numpy as np, time
from lat2d import *
for (torus, T, cfgs) in [(False, 6, [(8,None),(12,None),(16,None),(24,None),(32,None)]), (False, 10, [(8,None),(16,None),(32,None)]),
                         (True, 6, [(4,4),(6,4),(8,4),(8,6),(10,6),(12,8)]), (True, 8, [(4,4),(6,4),(8,6),(10,6),(12,8)])]:
    G = Geom(2, T, torus, 1 if torus else -1); rng = np.random.default_rng(7); Fs, Bs = G.crossing_mats()
    U = [rand_half(rng, G, 0.25, 0.55) for _ in range(2)]
    for op in ['O', 'W']:
        for (n, nw) in cfgs:
            t0 = time.time(); ph, w = nodes(G, U[0], U[1], 0.6, n, 'hard', nw)
            l, g = logdet_batch(G, G.D0(U[0], U[1]), Fs, Bs, ph, op, chunk=32)
            lm = l.real.max(); v = np.sum(w * np.exp(l - lm))
            print('torus' if torus else 'open', G.Lt, op, n, nw, len(w), f"{(np.log(v)+lm).real:.15f}", f"{(np.log(v)+lm).imag:+.2e}", f"{time.time()-t0:.2f}s", flush=True)
