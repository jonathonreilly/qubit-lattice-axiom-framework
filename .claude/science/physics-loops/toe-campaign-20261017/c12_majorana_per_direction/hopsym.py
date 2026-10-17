import sys, itertools, pickle
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
from collections import Counter
O = c1.O; DIRS = bk.DIRS
chosen = pickle.load(open('valid_group_choices.pkl', 'rb'))
def mat(M, eps):
    P = np.zeros((6, 6), int)
    for d in range(6): P[bk.rotdir(M, d), d] = eps[d]
    return P
C4 = next(M for M in O if bk.kind(M) == 'C4'); C3 = next(M for M in O if bk.kind(M) == 'C3')
key = lambda P: tuple(P.flatten())
res = Counter()
for e4, e3 in chosen:
    gens_ = [mat(C4, e4), mat(C3, e3)]
    el = {key(np.eye(6, dtype=int)): np.eye(6, dtype=int)}; fr = [np.eye(6, dtype=int)]
    while fr:
        nf = []
        for A in fr:
            for g in gens_:
                B = g @ A
                if key(B) not in el: el[key(B)] = B; nf.append(B)
        fr = nf
    # symmetric hopping signs t in {+-1}^3: t_{|Ra|} = sigma_R(a) t_a, sigma_R(a) = eps(+a) eps(-a)
    sols = []
    for t in itertools.product((1, -1), repeat=3):
        ok = True
        for B in el.values():
            perm = [int(np.flatnonzero(B[:, d])[0]) for d in range(6)]
            for a in range(3):
                dp, dm = DIRS.index((a, 1)), DIRS.index((a, -1))
                sig = B[perm[dp], dp] * B[perm[dm], dm]
                b = DIRS[perm[dp]][0]
                if t[b] != sig * t[a]: ok = False; break
            if not ok: break
        if ok: sols.append(t)
    res[len(sols)] += 1
print('number of symmetric translation-invariant Majorana hopping sign patterns per consistent group action:', dict(res))
