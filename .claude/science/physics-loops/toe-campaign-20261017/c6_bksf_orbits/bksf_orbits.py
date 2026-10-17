import itertools, sys, time
from collections import Counter, defaultdict
import numpy as np
sys.path.insert(0, '.')
from bksf import *
O = c1.O
def leg(order, d, n):
    a, s = DIRS[d]; ops = []; v = (0,0,0)
    for _ in range(n):
        if s == 1: base = v; v = tuple(v[i] + E[a][i] for i in range(3))
        else: v = tuple(v[i] - E[a][i] for i in range(3)); base = v
        ops.append(A(base, a, order))
    return prod(*ops)
def stats(order):
    signs = Counter()
    for trip in itertools.combinations(range(6), 3):
        Ls = [leg(order, d, 3) for d in trip]
        signs[(-1) ** (anti(Ls[0], Ls[1]) + anti(Ls[1], Ls[2]) + anti(Ls[0], Ls[2]))] += 1
    return dict(signs)
print('order (+x,+y,+z,-x,-y,-z): straight-leg T-junction signs over 20 triples:', stats(list(range(6))), flush=True)
# distinct codes over all 720 orderings
t0 = time.time(); H = {}; classes = defaultdict(list)
for order in itertools.permutations(range(6)):
    h, r = rref_hash(torus_rows(gens_at_origin(list(order)), 4))
    H[order] = h; classes[h].append(order)
print(f'distinct codes over 720 orderings: {len(classes)}  [{time.time()-t0:.0f}s]', flush=True)
# rotation action on orderings: R maps direction d to direction R(d)
def rotdir(M, d):
    a, s = DIRS[d]; v = M @ (s * np.array(E[a])); b = int(np.nonzero(v)[0][0]); return DIRS.index((b, int(v[b])))
def rot_order(M, order):
    # rotated code uses at vertex Rv the ordering of rotated directions
    return tuple(rotdir(M, d) for d in order)
reps = list(classes)
orbit_sizes = Counter()
for h in reps:
    o = classes[h][0]
    images = {H[rot_order(M, o)] for M in O}
    orbit_sizes[len(images)] += 1
print('orbit sizes of distinct codes under O (size: number of codes):', dict(orbit_sizes), flush=True)
print('statistics per class (first 10 classes):', [stats(list(classes[h][0])) for h in reps[:10]], flush=True)
