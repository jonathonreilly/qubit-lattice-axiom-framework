"""BKSF codes read as three-axis-qubit site codes (site v owns edges (v,+a)); framework site rotation
(u, a) -> (M u, |M e_a|), optionally with Pauli-label soldering. Which codes are covariant?"""
import sys, itertools
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
from collections import Counter, defaultdict
O = c1.O; E = bk.E; L = 4
orders = list(itertools.permutations(range(6)))
rows = {o: bk.torus_rows(bk.gens(o), L) for o in orders}
H = {o: bk.span_hash(rows[o]) for o in orders}
classes = defaultdict(list)
for o in orders: classes[H[o]].append(o)
n = 3 * L ** 3
def idx(p, a): return 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a
def site_perm(M, shiftrev=False):
    perm = np.zeros(n, int)
    for v in itertools.product(range(L), repeat=3):
        w = tuple(int(x) for x in M @ np.array(v))
        for a in range(3):
            d = M @ np.array(E[a]); b = int(np.nonzero(d)[0][0])
            p = w if (d[b] == 1 or not shiftrev) else tuple(w[t] - (1 if t == b else 0) for t in range(3))
            perm[idx(v, a)] = idx(p, b)
    return perm
# Pauli label actions on X/Z bits: trivial; Hadamard-like swap X<->Z for odd rotations? keep: trivial only, and (X,Z)->(Z,X) for C4/C2 (test both)
def act(R, perm, swapXZ=False):
    out = np.zeros_like(R); out[:, perm] = R[:, :n]; out[:, n + perm] = R[:, n:]
    if swapXZ: out = np.concatenate([out[:, n:], out[:, :n]], 1)
    return out
res = Counter()
for h, ords in classes.items():
    R = rows[ords[0]]
    for shiftrev in (True, False):
        st = [M for M in O if bk.span_hash(act(R, site_perm(M, shiftrev))) == h]
        res[('edge rotation' if shiftrev else 'site rotation (framework)', len(st))] += 1
print('(action, |stabilizer in O|): number of codes', dict(res))
