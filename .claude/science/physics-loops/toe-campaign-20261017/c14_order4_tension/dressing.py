"""For each stabilizing C2 of a code: P_R(A^o_e) * A^o_{Re} = (B-product) * (plaquettes). Report the B-dressing set."""
import sys, itertools
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
from collections import defaultdict, Counter
O = c1.O; E = bk.E; L = 6
orders = list(itertools.permutations(range(6)))
H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
classes = defaultdict(list)
for o in orders: classes[H[o]].append(o)
V = list(itertools.product(range(L), repeat=3)); n = 3 * L ** 3
def vec(op):
    x = np.zeros(2 * n, np.uint8)
    for (p, a), l in op.items():
        k = 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a
        if l in (1, 2): x[k] ^= 1
        if l in (2, 3): x[n + k] ^= 1
    return x
def rot_op(M, op):
    out = {}
    for (p, a), l in op.items():
        w = tuple(int(x) for x in M @ np.array(p)); d = M @ np.array(E[a]); b = int(np.nonzero(d)[0][0])
        q = w if d[b] == 1 else tuple(w[t] - (1 if t == b else 0) for t in range(3))
        out[(q, b)] = l
    return out
def solve(Mt, t):
    A = np.concatenate([Mt, t[:, None]], 1) % 2; m, nn = Mt.shape; piv = []; r = 0
    for c in range(nn):
        nz = np.flatnonzero(A[r:, c])
        if nz.size == 0: continue
        p = r + nz[0]; A[[r, p]] = A[[p, r]]; rows = np.flatnonzero(A[:, c]); rows = rows[rows != r]; A[rows] ^= A[r]; piv.append(c); r += 1
        if r == m: break
    if A[r:, -1].any(): return None
    w = np.zeros(nn, np.uint8)
    for i, c in enumerate(piv): w[c] = A[i, -1]
    return w
wrap = lambda p: tuple(((c + L // 2) % L) - L // 2 for c in p)
def dressing(o, M):
    cols = [vec(bk.B(v)) for v in V] + [vec(bk.plaq(v, c, o)) for v in V for c in range(3)]
    Mt = np.array(cols).T.astype(np.uint8)
    out = []
    for d in range(6):
        a, s = bk.DIRS[d]
        base = (0, 0, 0) if s == 1 else tuple(-E[a][i] for i in range(3))
        img = rot_op(M, bk.A(base, a, o))
        dv = M @ np.array(E[a]); b = int(np.nonzero(dv)[0][0])
        tail = tuple(int(x) for x in M @ np.array(base)); head = tuple(int(x) for x in M @ np.add(base, E[a]))
        rbase = tail if dv[b] == 1 else head
        T = vec(img) ^ vec(bk.A(rbase, b, o))
        w = solve(Mt, T)
        if w is None: out.append('not in G'); continue
        bset = [wrap(V[i]) for i in np.flatnonzero(w[:len(V)])]
        if len(bset) > len(V) // 2: bset = sorted(set(wrap(v) for v in V) - set(bset))
        ends = {wrap(tail), wrap(head)}
        out.append('BtBh' if set(bset) == ends else ('none' if not bset else ('one end' if len(bset) == 1 and set(bset) <= ends else 'other:' + str(sorted(bset)))))
    return out
for h, ords in classes.items():
    o = ords[0]
    stab = [M for M in O if H[bk.rot_order(M, o)] == h]
    if len(stab) != 4: continue
    print('order-4 code', o)
    for M in stab:
        if bk.kind(M) == 'E': continue
        print('  ', bk.kind(M), M.tolist(), dressing(o, M), flush=True)
    break
