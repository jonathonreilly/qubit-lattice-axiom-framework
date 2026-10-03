"""For every surviving covariant Clifford candidate: trace of the symbol, order, support radius of powers."""
import itertools, sys
import numpy as np
from cliff_lines import affine_solutions
from cliff_enum import check
from cliff_poly import from_vecs, trace, orbit_stats

cases = [("oct", 2), ("cube", 2), ("oct", 3)]
if len(sys.argv) > 1:
    cases = [(sys.argv[1], int(sys.argv[2]))]
for shape, r in cases:
    pts, idx, Bs, L3, part, hom = affine_solutions(shape, r)
    L33 = (L3.astype(int) @ L3) % 2
    for s in itertools.product([0, 1], repeat=len(hom)):
        coeff = part.astype(int).copy()
        for si, hv in zip(s, hom):
            if si:
                coeff = (coeff + hv) % 2
        f = (coeff @ Bs.astype(int)) % 2
        h = (L33 @ f) % 2
        ok1, ok2 = check(f, h, pts, r)
        if not (ok1 and ok2):
            continue
        M = from_vecs(f, h, pts)
        tr = trace(M)
        order, radii = orbit_stats(M, 10)
        print(f"{shape} r={r} s={s}: |supp fx,fz,hx,hz|={[len(M[0][0]),len(M[1][0]),len(M[0][1]),len(M[1][1])]}"
              f" trace terms={len(tr)} order={order} radii(M^t)={radii}")
