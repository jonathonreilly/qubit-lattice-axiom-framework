import sys, itertools
import numpy as np
exec(open('framed.py').read().split("cands = [()]")[0])
def as_vec(g):   # dict pos -> labs  ->  dict (pos, a) -> label
    return {(p, a): l for p, labs in g.items() for a, l in enumerate(labs) if l}
def prod(*ops):
    out = {}
    for op in ops:
        for k, l in op.items():
            c = out.get(k, 0)
            out[k] = l if c == 0 else (0 if c == l else 6 - c - l)
    return {k: l for k, l in out.items() if l}
def anti(o1, o2): return sum(1 for k, l in o1.items() if o2.get(k, 0) not in (0, l)) % 2
def shift(op, s): return {(tuple(p[i] + s[i] for i in range(3)), a): l for (p, a), l in op.items()}
def leg(S, d, n):
    """straight path from origin along signed axis direction d (0..5) with n steps: product of U_e"""
    a, sg = d % 3, (1 if d < 3 else -1); ops = []; v = (0,0,0)
    for _ in range(n):
        if sg == 1: base = v; v = tuple(v[i] + E[a][i] for i in range(3))
        else: v = tuple(v[i] - E[a][i] for i in range(3)); base = v
        ops.append(as_vec(U(base, a, S)))
    return prod(*ops), v
def check(S, name):
    P = [as_vec(plaq(c, S)) for c in range(3)]; Av = as_vec(A)
    # does U_e commute with every plaquette translate and anticommute with exactly the two endpoint vertices?
    ok = True
    for a in range(3):
        u = as_vec(U((0,0,0), a, S))
        for c in range(3):
            for s in itertools.product(range(-3, 4), repeat=3):
                if anti(u, shift(P[c], s)): ok = False
        hits = [s for s in itertools.product(range(-3, 4), repeat=3) if anti(u, shift(Av, s))]
        ok &= sorted(hits) == sorted([(0,0,0), E[a]])
    print(name, 'U_e are pure hopping operators (commute with all plaquettes, flip only endpoint vertices):', ok)
    if not ok: return
    res = {}
    for trip in itertools.combinations(range(6), 3):
        if len({d % 3 for d in trip}) < 2 and False: continue
        L = [leg(S, d, 3)[0] for d in trip]
        sgn = (-1) ** (anti(L[0], L[1]) + anti(L[1], L[2]) + anti(L[0], L[2]))
        res[trip] = sgn
    from collections import Counter
    print('  straight-leg T-junction signs over all triples of the 6 axis directions:', Counter(res.values()))
    print('  e.g.', {k: v for k, v in list(res.items())[:8]})
T = [(((0,-1,0),0),((0,1,0),0)), (((0,0,-1),1),((0,0,1),1)), (((-1,0,0),2),((1,0,0),2))]
check([(), (), ()], 'plain toric code')
check(T, 'T-framed')
