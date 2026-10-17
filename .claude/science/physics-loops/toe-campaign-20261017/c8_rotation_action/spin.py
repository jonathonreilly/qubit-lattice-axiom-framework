"""Rotation fractionalization of the BKSF fermion under a C3 (and C2) of its D3 stabilizer.
Paulis with phases: P = i^k X^x Z^z (qubitwise X^x Z^z). Torus L, qubits = edges."""
import itertools, sys
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotation_orbits_2026_10_17 as bk
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
L = int(sys.argv[1]) if len(sys.argv) > 1 else 6
O = c1.O; E = bk.E
n = 3 * L**3
def idx(p, a): return 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a
def from_op(op):   # dict ((p,a)->label) with Hermitian labels X=1,Y=2,Z=3 -> (x, z, k)
    x = np.zeros(n, np.uint8); z = np.zeros(n, np.uint8); k = 0
    for (p, a), l in op.items():
        q = idx(p, a)
        if l in (1, 2): x[q] ^= 1
        if l in (2, 3): z[q] ^= 1
        if l == 2: k += 1          # Y = i X Z
    return [x, z, k % 4]
def mulp(P, Q):
    x1, z1, k1 = P; x2, z2, k2 = Q
    s = int(z1 @ x2) % 2           # (X^x1 Z^z1)(X^x2 Z^z2) = (-1)^{z1.x2} X^{x1+x2} Z^{z1+z2}
    return [x1 ^ x2, z1 ^ z2, (k1 + k2 + 2 * s) % 4]
def omega(P, Q): return int((P[0] @ Q[1] + P[1] @ Q[0]) % 2)
def gens(order, signs=(0, 0, 0)):
    G, lab = [], []
    for v in itertools.product(range(L), repeat=3):
        G.append(from_op(bk.B(v))); lab.append(('B', v))
        for c in range(3):
            a, b = [t for t in range(3) if t != c]
            va = tuple(v[i] + E[a][i] for i in range(3)); vb = tuple(v[i] + E[b][i] for i in range(3))
            P = from_op(bk.A(v, a, order))
            for Q in (from_op(bk.A(va, b, order)), from_op(bk.A(vb, a, order)), from_op(bk.A(v, b, order))): P = mulp(P, Q)
            # make Hermitian: P^2 = i^{2k}... a Pauli i^k X^x Z^z is Hermitian iff k == (x.z) mod 2 (mod 4 sign aside)
            if (P[2] - int(P[0] @ P[1])) % 2: P[2] = (P[2] + 1) % 4
            P[2] = (P[2] + 2 * signs[c]) % 4
            G.append(P); lab.append(('S', v, c))
    return G, lab
def gf2_solve(M, t):
    A = np.concatenate([M, t[:, None]], axis=1).astype(np.uint8) % 2; m, nn = M.shape; piv = []; r = 0
    for c in range(nn):
        p = next((i for i in range(r, m) if A[i, c]), None)
        if p is None: continue
        A[[r, p]] = A[[p, r]]; rows = np.nonzero(A[:, c])[0]; rows = rows[rows != r]; A[rows] ^= A[r]; piv.append(c); r += 1
        if r == m: break
    if any(A[i, -1] for i in range(r, m)): return None
    w = np.zeros(nn, np.uint8)
    for i, c in enumerate(piv): w[c] = A[i, -1]
    return w
def express(G, Pt):
    """Find a product of generators equal to Pt up to phase; return the phase-correct product or None."""
    M = np.array([np.concatenate([g[0], g[1]]) for g in G]).T   # columns = generators
    w = gf2_solve(M, np.concatenate([Pt[0], Pt[1]]))
    if w is None: return None
    R_ = [np.zeros(n, np.uint8), np.zeros(n, np.uint8), 0]
    for i in np.nonzero(w)[0]: R_ = mulp(R_, G[i])
    return R_
def perm_of(M):
    perm = np.zeros(n, int)
    for v in itertools.product(range(L), repeat=3):
        for a in range(3):
            p, b = bk_rot_edge(M, v, a); perm[idx(v, a)] = idx(p, b)
    return perm
def bk_rot_edge(M, v, a):
    w = tuple(int(x) for x in M @ np.array(v)); d = M @ np.array(E[a]); b = int(np.nonzero(d)[0][0])
    return (w if d[b] == 1 else tuple(w[i] - (1 if i == b else 0) for i in range(3))), b
def apply_perm(P, perm):
    x = np.zeros(n, np.uint8); z = np.zeros(n, np.uint8); x[perm] = P[0]; z[perm] = P[1]; return [x, z, P[2]]
