"""Check: under the pure HS mean field, are ALL realised vacua at the edge (admissibility edge or the rho=1.5 cap)?
Also: sign census of the fermion-determinant quadratic a2 (concavity => a2 <= 0) and min over rho of the angular class."""
import numpy as np
from t3_landau import *
S, C = bz_axis(16)
lams = fib_sphere(120)
for wilson in (False, True):
    nint = 0; ncap = 0; nadm = 0; a2pos = 0; nfirst = []
    for eta in (1/3, 1/2, 1.0, 2.0, 3.0):
        for lam in lams:
            R = run_coupling_A(eta, lam, S, C, wilson)
            real = R['real']
            nint += any(j < len(R['rr']) - 1 for j in real)
            if R['re'] >= 1.5 - 1e-12: ncap += 1
            else: nadm += 1
            a2pos += R['q'][1] > 0
    print(f'{"A-W" if wilson else "A-N"}: couplings with ANY interior realised vacuum {nint}/600; edge = cap(1.5) {ncap}, edge = velocity floor {nadm}; a2>0: {a2pos}/600')
