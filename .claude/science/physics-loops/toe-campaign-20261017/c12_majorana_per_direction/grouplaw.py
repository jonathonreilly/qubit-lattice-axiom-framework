"""Can the per-rotation sign choices eps_R be chosen as a group action (up to the global sign -1 = fermion parity)?"""
import sys, itertools, pickle
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
O = c1.O
good = pickle.load(open('good_eps_L4.pkl', 'rb'))
def mat(k, eps):
    M = O[k]; P = np.zeros((6, 6), int)
    for d in range(6): P[bk.rotdir(M, d), d] = eps[d]
    return P
key = lambda P: (tuple(P.flatten()), )
def find_idx(M):
    return next(k for k, N in enumerate(O) if (N == M).all())
for sec in ((0, 0, 0), (1, 1, 1)):
    goodset = {k: {tuple(e) for e in good[(sec, k)]} for k in range(24)}
    c4 = next(k for k, M in enumerate(O) if bk.kind(M) == 'C4'); c3 = next(k for k, M in enumerate(O) if bk.kind(M) == 'C3')
    results = []
    for e4 in good[(sec, c4)]:
        for e3 in good[(sec, c3)]:
            gens = [mat(c4, e4), mat(c3, e3)]
            # generate group
            elems = {key(np.eye(6, dtype=int)): np.eye(6, dtype=int)}
            frontier = [np.eye(6, dtype=int)]
            while frontier and len(elems) <= 200:
                nf = []
                for A in frontier:
                    for g in gens:
                        B = g @ A
                        if key(B) not in elems: elems[key(B)] = B; nf.append(B)
                frontier = nf
            if len(elems) > 200: continue
            hasminus = key(-np.eye(6, dtype=int)) in elems
            # every element's eps must be good for its rotation
            ok = True
            for B in elems.values():
                Mrot = np.zeros((3, 3), int)
                perm = [int(np.flatnonzero(B[:, d])[0]) for d in range(6)]
                # recover rotation from the direction permutation of +x,+y,+z
                for a in range(3):
                    b, s = bk.DIRS[perm[a]]; Mrot[b, a] = s
                k = find_idx(Mrot); eps = tuple(int(B[perm[d], d]) for d in range(6))
                if eps not in goodset[k]: ok = False; break
            results.append((len(elems), hasminus, ok))
    from collections import Counter
    print(sec, Counter(results))
# extension class of the valid 48-element lifts: squares of lifts of C2axis and C2edge
for sec in ((0, 0, 0),):
    goodset = {k: {tuple(e) for e in good[(sec, k)]} for k in range(24)}
    c4 = next(k for k, M in enumerate(O) if bk.kind(M) == 'C4'); c3 = next(k for k, M in enumerate(O) if bk.kind(M) == 'C3')
    cls = Counter(); chosen = []
    for e4 in good[(sec, c4)]:
        for e3 in good[(sec, c3)]:
            gens = [mat(c4, e4), mat(c3, e3)]
            elems = {key(np.eye(6, dtype=int)): np.eye(6, dtype=int)}; frontier = [np.eye(6, dtype=int)]
            while frontier and len(elems) <= 200:
                nf = []
                for A in frontier:
                    for g in gens:
                        B = g @ A
                        if key(B) not in elems: elems[key(B)] = B; nf.append(B)
                frontier = nf
            if len(elems) != 48: continue
            sq = {}
            for B in elems.values():
                perm = [int(np.flatnonzero(B[:, d])[0]) for d in range(6)]
                Mrot = np.zeros((3, 3), int)
                for a in range(3):
                    b, s = bk.DIRS[perm[a]]; Mrot[b, a] = s
                kd = bk.kind(Mrot)
                if kd in ('C2axis', 'C2edge'):
                    S2 = B @ B
                    sq.setdefault(kd, set()).add('+' if (S2 == np.eye(6)).all() else ('-' if (S2 == -np.eye(6)).all() else 'mixed'))
            cls[tuple(sorted((k, tuple(sorted(v))) for k, v in sq.items()))] += 1
            chosen.append((e4, e3))
    print('on-site extension classes (squares of lifts):', dict(cls))
    pickle.dump(chosen, open('valid_group_choices.pkl', 'wb'))
