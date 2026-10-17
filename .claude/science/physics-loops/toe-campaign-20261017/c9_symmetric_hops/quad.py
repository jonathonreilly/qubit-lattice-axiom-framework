"""Quad-condensed O-covariant 4-copy stack: O-invariance, code dims, charge statistics."""
import sys, itertools, time
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
E = bk.E; O = c1.O
orders = list(itertools.permutations(range(6)))
H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
o0 = next(o for o in orders if sum(1 for M in O if H[bk.rot_order(M, o)] == H[o]) == 6)
cops = []
for M in O:
    o = bk.rot_order(M, o0)
    if H[o] not in [H[c] for c in cops]: cops.append(o)
hidx = {H[c]: i for i, c in enumerate(cops)}

def rref_rank(R):
    A = (np.array(R, np.uint8) % 2).copy(); m, n = A.shape; r = 0
    for c in range(n):
        col = A[r:, c]
        nz = np.flatnonzero(col)
        if nz.size == 0: continue
        p = r + nz[0]
        if p != r: A[[r, p]] = A[[p, r]]
        rows = np.flatnonzero(A[:, c]); rows = rows[rows != r]
        if rows.size: A[rows] ^= A[r]
        r += 1
        if r == m: break
    return r, A[:r]

def build(L, K, cops=cops):
    nq = 4 * 3 * L**3
    def q(i, p, a): return 4 * (3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a) + i
    def vec(ops):
        x = np.zeros(2 * nq, np.uint8)
        for i, op in ops:
            for (p, a), l in op.items():
                k = q(i, p, a)
                if l in (1, 2): x[k] ^= 1
                if l in (2, 3): x[nq + k] ^= 1
        return x
    V = list(itertools.product(range(L), repeat=3))
    rows = [vec([(i, bk.plaq(v, c, cops[i]))]) for i in range(4) for v in V for c in range(3)]
    W = [w for w in itertools.product((0, 1), repeat=4) if any(w) and all(sum(a * b for a, b in zip(w, k)) % 2 == 0 for k in K)]
    # independent B-products: a basis of W
    Wb = []
    for w in W:
        if rref_rank(np.array(Wb + [w]))[0] > len(Wb): Wb.append(w)
    for v in V:
        for w in Wb: rows.append(vec([(i, bk.B(v)) for i in range(4) if w[i]]))
    for k in K:
        for v in V:
            for a in range(3): rows.append(vec([(i, bk.A(v, a, cops[i])) for i in range(4) if k[i]]))
    return np.array(rows), nq, q, vec

def rot_perm(M, L, nq, q):
    # qubit (i, v, a) -> (pi(i), R edge)
    pi = [hidx[H[bk.rot_order(M, c)]] for c in cops]
    perm = np.zeros(nq, int)
    for v in itertools.product(range(L), repeat=3):
        w = tuple(int(x) for x in M @ np.array(v))
        for a in range(3):
            d = M @ np.array(E[a]); b = int(np.nonzero(d)[0][0])
            p = w if d[b] == 1 else tuple(w[t] - (1 if t == b else 0) for t in range(3))
            for i in range(4): perm[q(i, v, a)] = q(pi[i], p, b)
    return perm, pi

if __name__ == '__main__':
    K = [(1, 1, 1, 1)]
    for L in (4,):
        t = time.time()
        R, nq, q, vec = build(L, K)
        Sy = (R[:, :nq].astype(np.int32) @ R[:, nq:].T.astype(np.int32) + R[:, nq:].astype(np.int32) @ R[:, :nq].T.astype(np.int32)) % 2
        r, basis = rref_rank(R)
        print('L', L, 'commuting', not Sy.any(), 'log2 dim', nq - r, round(time.time() - t), flush=True)
        inv = []
        for M in O:
            perm, pi = rot_perm(M, L, nq, q)
            Rr = np.zeros_like(R); Rr[:, perm] = R[:, :nq]; Rr[:, nq + perm] = R[:, nq:]
            inv.append((bk.kind(M), tuple(pi), rref_rank(np.vstack([basis, Rr]))[0] == r))
        print('rotation invariance of unsigned group:', inv, flush=True)
