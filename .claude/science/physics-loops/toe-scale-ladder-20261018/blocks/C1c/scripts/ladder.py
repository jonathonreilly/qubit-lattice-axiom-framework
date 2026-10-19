#!/usr/bin/env python3
"""beta ladder: d ln(beta) = kappa / sigma(beta), sigma^2 = c Np beta^2/(1+beta) (model of Var(nF)).
usage: ladder.py L bmin bmax kappa [c] > file"""
import sys, numpy as np
L, bmin, bmax, kap = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
c = float(sys.argv[5]) if len(sys.argv) > 5 else 0.27
rmax = float(sys.argv[6]) if len(sys.argv) > 6 else 1.2
Np = 3 * L ** 3
b = [bmin]
while b[-1] < bmax:
    s = np.sqrt(c * Np * b[-1] ** 2 / (1 + b[-1]))
    b.append(b[-1] * min(rmax, np.exp(kap / max(s, 1e-9))))
b[-1] = bmax
if len(b) > 2 and b[-1] / b[-2] < 1.02:
    b.pop(-2)
# make sure beta = bmax/2 is on the ladder (replace nearest)
for extra in (bmax / 2,):
    i = int(np.argmin(np.abs(np.array(b) - extra)))
    b[i] = extra
print(" ".join(f"{x:.6g}" for x in sorted(set(b))))
