exec(open('equiv.py').read().split("if __name__ == '__main__':\n    for t in fixed")[0])
import sys
L = 6
t = fixed[int(sys.argv[1]) if len(sys.argv) > 1 else 0]
Oj = copy_orders(t)
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
def sym(X, Y):
    return (X[:, :nq].astype(np.int32) @ Y[:, nq:].T.astype(np.int32) + X[:, nq:].astype(np.int32) @ Y[:, :nq].T.astype(np.int32)) % 2
def shiftvec(x, s):
    # translate a vector by s
    y = np.zeros_like(x)
    idx = np.arange(nq)
    i = idx % 4; e = idx // 4; a = e % 3; c = e // 3
    p2 = (c // (L * L) + s[0]) % L, ((c // L) % L + s[1]) % L, (c % L + s[2]) % L
    new = 4 * (3 * ((p2[0] * L + p2[1]) * L + p2[2]) + a) + i
    y[new] = x[:nq]; y[nq + new] = x[nq:]
    return y
quad0 = [vec([(i, bk.A((0, 0, 0), a, Oj[i][a])) for i in range(4)]) for a in range(3)]
V = list(itertools.product(range(L), repeat=3))
Q = np.array([shiftvec(qv, v) for v in V for qv in quad0])
# local window candidates: B^j at the 8 cube vertices, S^j plaquettes based at those vertices
win = list(itertools.product((0, 1), repeat=3))
cand = [vec([(j, bk.B(v))]) for j in range(4) for v in win] + [vec([(j, bk.plaq(v, c, classes[hs[j]][0]))]) for j in range(4) for v in win for c in range(3)]
cand = np.array(cand)
Cm = sym(cand, Q)
r, N = c1.f2_rank_and_null(Cm)
loc = (N.astype(np.int32) @ cand.astype(np.int32)) % 2
loc = np.array([x for x in loc if x.any()], np.uint8)
lr, lb = rref_rank(loc)
# translation-reduce: keep generators, take all translates
gens0 = lb
Gp = np.vstack([np.array([shiftvec(g, v) for v in V for g in gens0]), Q]).astype(np.uint8)
print('local kept generators per cell (window rank)', lr, ' rows', Gp.shape, flush=True)
rG, bG = rref_rank(Gp)
print('L', L, 'log2 dim with local generators', nq - rG, 'commuting', not sym(Gp, Gp).any(), flush=True)
np.save('gp_L6.npy', Gp)
