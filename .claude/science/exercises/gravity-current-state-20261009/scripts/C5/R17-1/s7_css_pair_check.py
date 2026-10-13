"""R17-1 s7 (written before running). CSS model with Z-stabilizers = all translates of the cube (mu6) and the
three mu8 orientations. For every pair s != t inside one stabilizer pattern, find a Z-stabilizer containing
exactly one of s, t (then X_s X_t anticommutes with it and <X_s X_t> = 0 in EVERY ground state), so the
exact flat k^0 formula m1 = K sum_patterns sum_{s in p}|c_s|^2 holds for every ground state.
"""
import numpy as np, itertools
src = open("s2_exact_symbols.py").read().split("# (A) X_s X_t in X-stabilizer group?")[0]
ns = {}; exec(src, ns)
rotate, Rs, canon = ns['rotate'], ns['Rs'], ns['canon']
mu8 = [((0,1,1),5,1),((0,1,2),2,1),((0,1,2),5,1),((1,1,1),0,1),((1,1,1),5,1),((1,1,2),5,1),((1,1,3),0,1),((2,1,2),2,1)]
mu8 = [((x, t), v) for x, t, v in mu8]
pats = {}
for base in [ns['mu6'], mu8]:
    for R in Rs:
        r = rotate(base, R); pats.setdefault(canon(r), r)
pats = [[(tuple(x), t) for x, t in key] for key in pats.keys()]   # canonical (translation-normalized) supports
print("pattern orientations:", len(pats), "weights:", [len(p) for p in pats])
def translates(p, shift): return set(((tuple(np.array(x) + shift), t) for x, t in p))
stabs = []
for p in pats:
    for sh in itertools.product(range(-4, 5), repeat=3):
        stabs.append(translates(p, np.array(sh)))
bad = 0; tot = 0
for p in pats:
    P = translates(p, np.array([0,0,0]))
    for s, t in itertools.combinations(sorted(P), 2):
        tot += 1
        if not any(((s in S) != (t in S)) for S in stabs): bad += 1
print("pairs tested %d ; pairs with NO separating Z-stabilizer: %d" % (tot, bad))
