import sys, itertools
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/c9')
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
from quad import rref_rank
from collections import defaultdict
O = c1.O; E = bk.E
orders = list(itertools.permutations(range(6)))
H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
classes = defaultdict(list)
for o in orders: classes[H[o]].append(o)
def rot_op(M, op):
    out = {}
    for (p, a), l in op.items():
        w = tuple(int(x) for x in M @ np.array(p)); d = M @ np.array(E[a]); b = int(np.nonzero(d)[0][0])
        q = w if d[b] == 1 else tuple(w[t] - (1 if t == b else 0) for t in range(3))
        out[(q, b)] = l
    return out
def corners(c):
    a, b = [t for t in range(3) if t != c]
    return [(0, 0, 0), tuple(E[a]), tuple(E[b]), tuple(np.add(E[a], E[b]))]
subsets = [list(s) for k in range(5) for s in itertools.combinations(range(4), k)]
found_total = 0
for h, ords in classes.items():
    stab = [M for M in O if H[bk.rot_order(M, ords[0])] == h]
    if len(stab) != 4: continue
    gensR = [M for M in stab if bk.kind(M) != 'E']
    for o in ords:
        ref = rref_rank(bk.torus_rows([bk.plaq((0, 0, 0), c, o) for c in range(3)], 4))[0]
        hits = []
        for bs in itertools.product(subsets, repeat=3):
            gs = []
            for c in range(3):
                g = bk.plaq((0, 0, 0), c, o)
                for i in bs[c]: g = bk.prod(g, bk.B(corners(c)[i]))
                gs.append(g)
            R0 = bk.torus_rows(gs, 4); r0, b0 = rref_rank(R0)
            if r0 != ref: continue
            if all(rref_rank(np.vstack([b0, bk.torus_rows([rot_op(M, g) for g in gs], 4)]))[0] == r0 for M in gensR):
                hits.append(bs)
        print('order-4 code', ords[0], 'ordering', o, 'D2-invariant corner-dressed conventions (rank-preserving):', len(hits), flush=True)
        found_total += len(hits)
    break
print('total', found_total)
