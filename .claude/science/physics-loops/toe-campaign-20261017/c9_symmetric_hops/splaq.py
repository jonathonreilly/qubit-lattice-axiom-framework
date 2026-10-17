import sys, itertools
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
from quad import rref_rank
from collections import Counter, defaultdict
O = c1.O
orders = list(itertools.permutations(range(6)))
H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
classes = defaultdict(list)
for o in orders: classes[H[o]].append(o)
res = Counter()
for h, os_ in classes.items():
    stab = [M for M in O if H[bk.rot_order(M, os_[0])] == h]
    for o in os_:
        rows = bk.torus_rows(bk.gens(o)[1:], 4)
        r0 = rref_rank(rows)[0]
        inv = sum(1 for M in stab if rref_rank(np.vstack([rows, bk.torus_rows(bk.gens(bk.rot_order(M, o))[1:], 4)]))[0] == r0)
        res[(24 // len(stab), len(stab), inv)] += 1
print('(orbit size, |stab|, #stabilizing rotations preserving span(S^o)): #orderings', dict(res))
