import numpy as np, time
from solve2d_sym import *
from solve import rref_mod, PRIMES
def exact(R, match):
    cols = build_sym(R, verbose=False)
    rows, entries, b, nr0 = assemble(cols, match, R)
    nr, nc = len(rows), len(cols)
    out = []
    for p in PRIMES:
        M = np.zeros((nr, nc + 1), dtype=np.int64)
        for i, j, c in entries:
            M[i, j] = (M[i, j] + (c.numerator % p) * pow(c.denominator % p, -1, p)) % p
        for i, c in b.items():
            M[i, nc] = (c.numerator % p) * pow(c.denominator % p, -1, p) % p
        rk, cons, piv, Mred = rref_mod(M, p, nc)
        out.append((p, rk, cons))
    return nr, nc, out
t0=time.time()
print("2D R=1 identity-only (exact mod two primes):", exact(1, ()), round(time.time()-t0,1), flush=True)
print("2D R=1 ADM-matched  (exact mod two primes):", exact(1, ('V2','T3','G2','xi1','chi')), round(time.time()-t0,1), flush=True)
