"""Part 1: enumerate all sign choices (s_a, s_b) for generators quarter-turn a and
threefold b such that the generated signed-permutation group G is a (projective)
representation of O: |G| in {24, 48}, kernel of G->O is {I} or {I,-I}.
Then extend to all 24 rotations (the full sign data is determined by the
generators up to the global +-1 on each element), classify by diagonal gauge
equivalence, detect spinoriality, and decompose under the binary octahedral group.
Exact integer arithmetic throughout (signed permutation matrices).
"""
import itertools, numpy as np, json
from common import *

Pa, Pb = Pmat(A_q).astype(int), Pmat(B_t).astype(int)
Pperm = {rkey(R): Pmat(R).astype(int) for R in ROTS}
permkey = {Pperm[k].astype(np.int8).tobytes(): k for k in Pperm}

signs = [np.array((1,) + t) for t in itertools.product([1, -1], repeat=7)]  # mod global sign
good = []
for sa in signs:
    Da = Pa @ np.diag(sa)
    for sb in signs:
        Db = Pb @ np.diag(sb)
        G = gen_group([Da, Db], maxsize=48)
        if G is None:
            continue
        # check kernel: elements with trivial permutation part
        ker = [g for g in G if (perm_part(g) == np.eye(8, dtype=int)).all()]
        okker = all((g == np.eye(8)).all() or (g == -np.eye(8)).all() for g in ker)
        if not okker:
            continue
        good.append((sa, sb, len(G)))
print("number of (s_a,s_b) mod global signs giving projective reps of O:", len(good))
from collections import Counter
print("group orders:", Counter(x[2] for x in good))

def full_data(sa, sb):
    """return dict rotation-key -> D (one of the +- lifts), and group G"""
    Da = Pa @ np.diag(sa); Db = Pb @ np.diag(sb)
    G = gen_group([Da, Db], maxsize=48)
    D = {}
    for g in G:
        k = permkey[perm_part(g).astype(np.int8).tobytes()]
        if k not in D:
            D[k] = g
    return D, G

def invariants(sa, sb):
    D, G = full_data(sa, sb)
    Dq = D[rkey(A_q)]
    q4 = np.linalg.matrix_power(Dq, 4)
    q4s = 1 if (q4 == np.eye(8)).all() else (-1 if (q4 == -np.eye(8)).all() else 0)
    # half-turn about z: D^2
    hz = np.linalg.matrix_power(Dq, 2)
    hz2 = np.linalg.matrix_power(hz, 2)
    hz2s = 1 if (hz2 == np.eye(8)).all() else -1
    # threefold: D^3
    t3 = np.linalg.matrix_power(D[rkey(B_t)], 3)
    t3s = 1 if (t3 == np.eye(8)).all() else -1
    # edge two-fold (x,y,z)->(y,x,-z)
    Re = np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])
    e2 = np.linalg.matrix_power(D[rkey(Re)], 2)
    e2s = 1 if (e2 == np.eye(8)).all() else -1
    ninv = sum(1 for g in G if (g @ g == np.eye(8)).all() and not (g == np.eye(8)).all())
    return dict(order=len(G), quarter4=q4s, half2=hz2s, three3=t3s, edge2=e2s, n_involutions=ninv)

# gauge classes: gauge g in {+-1}^8 acts D -> diag(g) D diag(g).  Canonical form:
# represent a choice by the set of signed matrices {+-D(R)} for all R; take the
# lexicographically minimal representation over all 128 gauges (mod global).
gauges = [np.array((1,) + t) for t in itertools.product([1, -1], repeat=7)]
def canon(sa, sb):
    D, G = full_data(sa, sb)
    best = None
    for g in gauges:
        Gg = np.diag(g)
        rep = []
        for k in sorted(D):
            M = Gg @ D[k] @ Gg
            # fix the projective sign: make the first nonzero entry of column 0 positive
            col = M[:, 0]
            sgn = col[np.nonzero(col)[0][0]]
            rep.append(tuple((sgn * M).flatten()))
        rep = tuple(rep)
        if best is None or rep < best:
            best = rep
    return best

classes = {}
for sa, sb, o in good:
    cf = canon(sa, sb)
    classes.setdefault(cf, []).append((sa, sb))
print("number of gauge classes:", len(classes))
cls_list = []
for i, (cf, members) in enumerate(classes.items()):
    sa, sb = members[0]
    inv = invariants(sa, sb)
    cls_list.append((sa, sb, inv, len(members)))
    print(i, "members", len(members), "rep s_a", sa, "s_b", sb, inv)

np.save("classes.npy", np.array([[x[0], x[1]] for x in cls_list]))
json.dump([dict(sa=x[0].tolist(), sb=x[1].tolist(), inv=x[2], nmembers=x[3]) for x in cls_list],
          open("classes.json", "w"), indent=1)
