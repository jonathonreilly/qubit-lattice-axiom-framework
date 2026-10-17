"""4-copy O-covariant stack of D3 BKSF codes; condense the quad boson f0f1f2f3; code dimension and charges."""
import sys, itertools
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
E = bk.E; O = c1.O
orders = list(itertools.permutations(range(6)))
H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
o0 = next(o for o in orders if sum(1 for M in O if H[bk.rot_order(M, o)] == H[o]) == 6)
cops = []
for M in O:
    o = bk.rot_order(M, o0)
    if H[o] not in [H[c] for c in cops]: cops.append(o)
assert len(cops) == 4
nq = 4 * 3 * L**3
def q(i, p, a): return 4 * (3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a) + i
def vec(ops):  # list of (copy, dictop)
    x = np.zeros(2 * nq, np.uint8)
    for i, op in ops:
        for (p, a), l in op.items():
            k = q(i, p, a)
            if l in (1, 2): x[k] ^= 1
            if l in (2, 3): x[nq + k] ^= 1
    return x
V = list(itertools.product(range(L), repeat=3))
def plaqs(i):
    return [vec([(i, bk.plaq(v, c, cops[i]))]) for v in V for c in range(3)]
def Bv(i, v): return (i, bk.B(v))
def hop(u, v, a): return vec([(i, bk.A(v, a, cops[i])) for i in u])
def rank(rows): return c1.f2_rank_and_null(np.array(rows))[0]
base_S = [r for i in range(4) for r in plaqs(i)]
G = base_S + [vec([Bv(i, v)]) for i in range(4) for v in V]
print('stack log2 dim', nq - rank(G))
# condense K: add hops of K-charges, keep B-products commuting with them
def condensed(K):
    rows = list(base_S)
    # B products: charge-measurement B^w = prod_{i in w} B^i_v for w with w.k = 0 for all k in K
    W = [w for w in itertools.product((0, 1), repeat=4) if any(w) and all(sum(a * b for a, b in zip(w, k)) % 2 == 0 for k in K)]
    for v in V:
        for w in W: rows.append(vec([Bv(i, v) for i in range(4) if w[i]]))
    for k in K:
        u = [i for i in range(4) if k[i]]
        for v in V:
            for a in range(3): rows.append(hop(u, v, a))
    return rows
def comm_ok(rows):
    R = np.array(rows); n = nq
    Sy = (R[:, :n].astype(int) @ R[:, n:].T.astype(int) + R[:, n:].astype(int) @ R[:, :n].T.astype(int)) % 2
    return not Sy.any()
for name, K in [('quad 1111', [(1, 1, 1, 1)]), ('pairing 01|23', [(1, 1, 0, 0), (0, 0, 1, 1)]), ('all pairs (01, 02)', [(1, 1, 0, 0), (1, 0, 1, 0)])]:
    rows = condensed(K)
    print(name, 'commuting:', comm_ok(rows), 'log2 dim', nq - rank(rows))
