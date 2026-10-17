import sys, itertools
import numpy as np
sys.argv = [sys.argv[0], '4']
exec(open('spin.py').read())
from collections import Counter, defaultdict
orders = list(itertools.permutations(range(6)))
H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
classes = defaultdict(list)
for o in orders: classes[H[o]].append(o)
def Aop(v, a, o): return from_op(bk.A(v, a, o))
res = Counter()
for h, ords in classes.items():
    o = ords[0]
    stab = [Mr for Mr in O if H[bk.rot_order(Mr, o)] == h]
    for s in ((0, 0, 0), (1, 1, 1)):
        G, lab = gens(o, s)
        Sgen = {l[2]: g for g, l in zip(G, lab) if l[0] == 'S' and l[1] == (1, 1, 1)}
        v = (1, 1, 1); fl = []
        for c in range(3):
            a, b = [t for t in range(3) if t != c]
            va = tuple(v[i] + E[a][i] for i in range(3)); vb = tuple(v[i] + E[b][i] for i in range(3))
            Lp = [np.zeros(n, np.uint8), np.zeros(n, np.uint8), 0]
            for P in (Aop(v, b, o), Aop(vb, a, o), Aop(va, b, o), Aop(v, a, o)):
                Lp = mulp(Lp, P)     # L = A(v,b) A(vb,a) A(va,b) A(v,a): first hop v->va acts first
            Sg = Sgen[c]
            assert (Lp[0] == Sg[0]).all() and (Lp[1] == Sg[1]).all()
            fl.append((Lp[2] - Sg[2]) % 4)    # L = i^fl * S  => flux phase i^fl
        res[(24 // len(stab), s, tuple(fl))] += 1
for k in sorted(res): print(k, res[k])
