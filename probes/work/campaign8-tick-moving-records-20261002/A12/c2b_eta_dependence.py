"""C2b: exponent c in eps* ~ exp(-c E T) versus required efficiency eta0 (E = 0.2 and 0.1, flat 1D massless)."""
import numpy as np
from c2lib import pareto
for eta0 in (0.1, 0.5, 0.9, 0.99):
    out = []
    for E in (0.1, 0.2):
        lns = []
        for ET in (4, 8, 12):
            eps, eta = pareto(int(round(ET / E)), E, eta0)
            lns.append(np.log(eps))
        c = -(lns[2] - lns[0]) / 8
        out.append(f"E={E}: ln eps* at ET=4,8,12 = {lns[0]:7.2f} {lns[1]:7.2f} {lns[2]:7.2f}; c = {c:.2f}")
    print(f"eta0={eta0}: " + " | ".join(out))
