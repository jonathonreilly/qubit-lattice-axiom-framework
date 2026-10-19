import numpy as np
from cone1 import run, L, c
rng_reps = 2
print(" p     axis speed  body speed   (stable light-speed cap 1/sqrt3 = 0.577)")
for p in (0.25, 0.3, 0.35, 0.4):
    T = 70; ax, bd = [], []
    for rep in range(rng_reps):
        R = run(p, T); X, Y, Z = np.nonzero(R); P = np.stack([X - c, Y - c, Z - c], 1).astype(float); r = np.linalg.norm(P, axis=1) + 1e-9
        for u, lst in ((np.array([1, 0, 0.]), ax), (np.array([1, 1, 1.])/np.sqrt(3), bd)):
            sel = (P @ u)/r > 0.995; lst.append(r[sel].max()/T)
    print(f" {p:.2f}  {np.mean(ax):.3f}       {np.mean(bd):.3f}")
