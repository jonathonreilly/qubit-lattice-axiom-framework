"""Element-order census of the combined group modulo the diagonal (-1_L)(-1_M) (= prod D, trivial on D=+1)."""
AUDIT_TIMEOUT_SEC = 1800
import numpy as np
from rot import *
import matter as MT
groups = consistent_link_groups()
Q = MT.quat_2O(); Ds = [MT.su2(q) for q in Q]
def qidx(D):
    for i, E in enumerate(Ds):
        if np.allclose(D, E): return i
def cm(a, b): return (sp_compose(a[0], b[0]), qidx(Ds[a[1]] @ Ds[b[1]]))
mneg = qidx(-np.eye(2))
for Gp in groups[:3]:
    gens = []
    for R in (C4z, C3):
        p = tuple(dir_perm(R)); ls = sorted(y for y in Gp if y[0] == p)[0]
        qi = [i for i, D in enumerate(Ds) if (np.rint(MT.so3(D)).astype(int) == R).all()][0]
        gens.append((ls, qi))
    idn = ((tuple(range(6)), (1,) * 6), qidx(np.eye(2)))
    both = ((tuple(range(6)), (-1,) * 6), mneg)
    Gc = {idn}; fr = [idn]
    while fr:
        nw = []
        for x in fr:
            for g in gens:
                y = cm(g, x)
                if y not in Gc: Gc.add(y); nw.append(y)
        fr = nw
    def order(x):
        y = x; n = 1
        while y != idn and y != both: y = cm(x, y); n += 1
        return n
    from collections import Counter
    print('quotient order', len(Gc) // 2, 'element orders:', sorted(Counter(order(x) for x in Gc).items()), '(each counted twice)')
