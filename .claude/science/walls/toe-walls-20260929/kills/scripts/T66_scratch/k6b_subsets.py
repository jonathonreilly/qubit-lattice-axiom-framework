import sys
sys.argv = ['k6', '1']
exec(open('k6_bbox_R1_2d.py').read().split("t0 = time.time()")[0])
import time
t0 = time.time()
cols = S.build_sym(1, verbose=False)
import numpy as np
def run(match):
    rows, entries, b, nr0 = S.assemble(cols, match, 1)
    nr, nc = len(rows), len(cols)
    p = PRIMES[0]
    M = np.zeros((nr, nc + 1), dtype=np.int64)
    for i, j, c in entries:
        M[i, j] = (M[i, j] + (c.numerator % p) * pow(c.denominator % p, -1, p)) % p
    for i, c in b.items():
        M[i, nc] = (c.numerator % p) * pow(c.denominator % p, -1, p) % p
    rk, cons, piv, Mred = rref_mod(M, p, nc)
    return nr, nc, rk, cons
for name, match in [('all', ('V2','T3','G2','xi1','chi')), ('no G2 match', ('V2','T3','xi1','chi')), ('no V2 match', ('T3','G2','xi1','chi')),
                    ('no T3 match', ('V2','G2','xi1','chi')), ('no xi1 match', ('V2','T3','G2','chi')), ('no chi match', ('V2','T3','G2','xi1')),
                    ('G2 only', ('G2',)), ('V2 only', ('V2',)), ('T3 only', ('T3',)), ('xi1 only', ('xi1',))]:
    print(name, run(match), round(time.time()-t0,1), flush=True)
