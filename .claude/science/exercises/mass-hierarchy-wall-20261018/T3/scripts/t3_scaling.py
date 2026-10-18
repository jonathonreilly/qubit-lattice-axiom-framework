"""Fraction of coupling directions whose angular minimum is D2h at FIXED absolute strain rho (angle-blind tree potential
assumed to hold rho there). Tests the expected law P(D2h | rho) ~ rho^3 (needs |b3| < 4 c6 rho^3)."""
import sys, numpy as np
from t3_landau import *
S, C = bz_axis(16)
lams = fib_sphere(2000)
for wilson in (False, True):
    for eta in (1.0, 2.0):
        res = {}
        edges = np.array([rho_edge_A(eta, l, 0.05 * min(1, eta)) for l in lams])
        for rho in (0.05, 0.1, 0.2, 0.4, 0.8):
            ok = edges > rho
            n = 0; nd = 0; tsd = []
            for l in lams[ok]:
                V = V_A(eta, l, np.full(TH.size, rho), TH, S, C, wilson)
                t = ang_min(V); n += 1
                if classify(t) == 'D2h': nd += 1; tsd.append(np.degrees(t))
            res[rho] = (nd, n)
            print(f'{"A-W" if wilson else "A-N"} eta={eta:g} rho={rho:<5g} admissible dirs {n:4d}  D2h {nd:4d}  frac {nd/max(n,1):.4f}  '
                  f'frac/rho^3 {nd/max(n,1)/rho**3:.3f}  t* sample {np.round(tsd[:6],1).tolist()}')
            sys.stdout.flush()
