# N-d: moving ONE point by delta (a local 'gauge' move of the embedding) flips relations with partners
# spread over its whole light cone: count ~ rho * delta * T^3 ; report also partner distances.
import numpy as np
rng = np.random.default_rng(11)
src = open("nb_orbit.py").read().split("def vol_diamond")[0]
exec(src)
delta = 0.05
for T in [6, 9, 13, 19]:
    from math import pi
    n = rng.poisson(pi * T**4 / 24)
    counts, dists = [], []
    for rep in range(40):
        P = sample_diamond(n, T, 4)
        x0 = np.array([T/2, 0, 0, 0.0]); x1 = x0 + np.array([0, delta, 0, 0])
        def rel(p):
            dt = P[:, 0] - p[0]; dx2 = ((P[:, 1:] - p[1:])**2).sum(1)
            return np.sign(dt) * (dt*dt - dx2 > 0)
        f = rel(x0) != rel(x1)
        counts.append(f.sum())
        dd = np.abs(P[f, 0] - x0[0]); dists.extend(dd.tolist())
    dists = np.array(dists) if dists else np.array([0.0])
    print(f"T={T:3d} n~{n:6d}: flipped relations per move = {np.mean(counts):8.2f} +- {np.std(counts)/np.sqrt(40):.2f}"
          f" | median |dt| of flipped partners = {np.median(dists):.2f} (T/2 = {T/2})")
