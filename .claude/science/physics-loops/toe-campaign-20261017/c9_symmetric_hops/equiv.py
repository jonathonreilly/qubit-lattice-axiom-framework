exec(open('hoptypes.py').read().split("for k, v in act.items()")[0])
import time
exec(open('quad.py').read().split("if __name__")[0].split("orders = list")[0])
from quad import rref_rank, rot_perm, hidx
fixed = []
for t in itertools.product(range(6), repeat=3):
    if all(all(act[(bk.kind(M), id(M), a)][t[a]] == (redge(M, a)[0], t[redge(M, a)[0]]) for a in range(3)) for M in stab):
        fixed.append(t)
print('fixed', fixed)
# coset reps R_j with R_j o0 in class hs[j]
hs = []; reps = []
for M in O:
    h = H[bk.rot_order(M, o0)]
    if h not in hs: hs.append(h); reps.append(M)
def copy_orders(t):
    O0 = [types[a][t[a]][0] for a in range(3)]
    Oj = []
    for j, Rj in enumerate(reps):
        d = [None] * 3
        for a in range(3):
            b, _ = redge(Rj, a); d[b] = bk.rot_order(Rj, O0[a])
        Oj.append(d)
    return Oj
def build_cond(L, Oj, cond=(1, 1, 1, 1)):
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
    Vv = list(itertools.product(range(L), repeat=3))
    G = [vec([(i, bk.plaq(v, c, classes[hs[i]][0]))]) for i in range(4) for v in Vv for c in range(3)] + \
        [vec([(i, bk.B(v))]) for i in range(4) for v in Vv]
    Q = [vec([(i, bk.A(v, a, Oj[i][a])) for i in range(4) if cond[i]]) for v in Vv for a in range(3)]
    G = np.array(G); Q = np.array(Q)
    sym = lambda X, Y: (X[:, :nq].astype(np.int32) @ Y[:, nq:].T.astype(np.int32) + X[:, nq:].astype(np.int32) @ Y[:, :nq].T.astype(np.int32)) % 2
    qq = sym(Q, Q).any()
    Cm = sym(G, Q)  # rows: G gens, cols: quads
    r, N = c1.f2_rank_and_null(Cm)
    keep = (N.astype(np.int32) @ G.astype(np.int32)) % 2
    Gp = np.vstack([keep, Q]).astype(np.uint8)
    return Gp, nq, q, not qq
if __name__ == '__main__':
    for t in fixed:
        Oj = copy_orders(t)
        # sanity: each copy's hops commute with its own code's plaquettes? (they should be hops of class hs[j])
        Gp, nq, q, qcomm = build_cond(4, Oj)
        r, basis = rref_rank(Gp)
        print('assignment', t, 'quads commute:', qcomm, 'log2 dim', nq - r, flush=True)
        bad = []
        for M in O:
            perm, pi = rot_perm(M, 4, nq, q)
            Rr = np.zeros_like(Gp); Rr[:, perm] = Gp[:, :nq]; Rr[:, nq + perm] = Gp[:, nq:]
            if rref_rank(np.vstack([basis, Rr]))[0] != r: bad.append(bk.kind(M))
        print('  rotations not preserving the condensed group:', bad, flush=True)
