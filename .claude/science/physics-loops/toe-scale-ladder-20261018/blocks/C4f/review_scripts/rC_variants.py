"""Phase C falsification probe: is the full N1 (F_w cap S_u OR F_u cap S_w) needed for L2^2 = id?
Variants of N1 for the controlled tetra layer; count involution failures on packed stress configs."""
import sys, os, itertools, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rlib
from rlib import templates, add, Layer
def ntemp(T, mode):
    F = lambda t: T[t]['S'] + (T[t]['G'] or [])
    def N1(t):
        Su = set(T[t]['S']); Fu = set(F(t)); out = set()
        for t2 in range(len(T)):
            for q in itertools.product(range(-3, 4), repeat=3):
                if (t2, q) == (t, (0,0,0)): continue
                Sw = {add(q, o) for o in T[t2]['S']}; Fw = {add(q, o) for o in F(t2)}
                a = bool(Fw & Su); b = bool(Fu & Sw); s = bool(Su & Sw)
                if {'full': a or b, 'FwSu': a, 'FuSw': b, 'SS': s}[mode]: out.add((t2, q))
        return out
    n1 = {t: N1(t) for t in range(len(T))}
    n2 = {}
    for t in range(len(T)):
        acc = set()
        for (t2, q) in n1[t]:
            for (t3, r) in n1[t2]: acc.add((t3, add(q, r)))
        n2[t] = acc - n1[t] - {(t, (0,0,0))}
    return n1, n2
L = 8; V = L**3; _, T2 = templates()
rng = np.random.default_rng(11)
pts = np.array(list(itertools.product(range(L), repeat=3)))
lays = {m: Layer(T2, *ntemp(T2, m), L) for m in ('full', 'FwSu', 'FuSw', 'SS')}
ref = lays['full']
configs = []
for rep in range(400):
    bg = rep % 4
    c = [np.zeros(V, np.uint8), np.ones(V, np.uint8), (pts[:, 2] < L//2).astype(np.uint8),
         (rng.random(V) < rng.random()).astype(np.uint8)][bg]
    for _ in range(int(rng.integers(5, 40))):
        u = int(rng.integers(len(ref.units)))
        c[ref.S[u]] = ref.pat[u] if rng.random() < .5 else 1 - ref.pat[u]
        if ref.ctrl[u] == 1: c[ref.G[u]] = 0
        if ref.ctrl[u] == 2: c[ref.G[u]] = 1
    configs.append(c)
for m, lay in lays.items():
    fails = 0; nonsym = 0
    for c in configs:
        try:
            d = lay.apply(c); fails += not np.array_equal(lay.apply(d), c)
        except AssertionError: fails += 1
    print(f'N1 variant {m}: N1 size {list(lay.n1size.values())[0]}, N2 size {list(lay.n2size.values())[0]}; '
          f'involution failures {fails}/{len(configs)}')
