import itertools, sys
from collections import defaultdict, Counter
import numpy as np
sys.path.insert(0, '.')
from bksf import *
O = c1.O
def rotdir(M, d):
    a, s_ = DIRS[d]; v = M @ (s_ * np.array(E[a])); b = int(np.nonzero(v)[0][0]); return DIRS.index((b, int(v[b])))
def rot_order(M, order): return tuple(rotdir(M, d) for d in order)
H = {}; classes = defaultdict(list)
for order in itertools.permutations(range(6)):
    h, r = rref_hash(torus_rows(gens_at_origin(list(order)), 4)); H[order] = h; classes[h].append(order)
def describe(M):
    w, v = np.linalg.eig(M.astype(float)); tr = int(round(np.trace(M)))
    kind = {3: 'E', -1: 'C2', 0: 'C3', 1: 'C4'}[tr]
    if kind == 'C2':   # axis vs edge type
        ax = np.real(v[:, np.argmin(abs(w - 1))]); nz = sum(abs(ax) > 1e-9); kind = 'C2axis' if nz == 1 else 'C2edge'
    axis = np.real(v[:, np.argmin(abs(w - 1))]); axis = tuple(int(round(x / max(abs(axis)))) for x in axis)
    return kind, axis
seen = set()
for h, orders in classes.items():
    o = orders[0]
    stab = [M for M in c1.O if H[rot_order(M, o)] == h]
    key = len(stab)
    if key in seen: continue
    seen.add(key)
    kinds = Counter(describe(M)[0] for M in stab)
    axes = sorted({describe(M)[1] for M in stab if describe(M)[0] in ('C3',)})
    print(f'orbit size {24 // len(stab)}: stabilizer order {len(stab)}, elements {dict(kinds)}, C3 axes {axes}, example ordering {o}', flush=True)
    for L in (4, 6):
        M_ = torus_rows(gens_at_origin(list(o)), L); r = c1.f2_rank_and_null(M_)[0]
        print(f'   torus L={L}: log2 code dim {3 * L**3 - r}', flush=True)
