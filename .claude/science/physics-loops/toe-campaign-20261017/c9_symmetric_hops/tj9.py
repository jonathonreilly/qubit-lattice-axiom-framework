"""T-junction statistics of charges in the quad-condensed O-covariant stack (L = 6, local solve)."""
src = open('stats9.py').read().split("lr, lb = rref_rank(loc)")[0]
exec(src)
from quad import rref_rank
lr, gens0 = rref_rank(loc)
def Bprod(js, v=(0, 0, 0)): return vec([(j, bk.B(v)) for j in js])
probes = [Bprod((0, 1)), Bprod((0, 2)), Bprod((0, 3))]
LG = np.vstack([gens0, np.array(quad0), np.array(probes)]).astype(np.uint8)
ng = len(LG)
P0 = ng - 3
print('local generators per vertex', ng, flush=True)
def box(lo, hi): return [tuple(c) for c in itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)])]
def edges_in(B):
    Bs = set(B); out = []
    for p in B:
        for a in range(3):
            w = tuple(p[i] + E[a][i] for i in range(3))
            if w in Bs: out.append((p, a))
    return out
def qubits_of(B):
    return sorted({q(i, p, a) for (p, a) in edges_in(B) for i in range(4)})
rowcache = {}
def row(u, g):
    key = (tuple(c % L for c in u), g)
    if key not in rowcache: rowcache[key] = shiftvec(LG[g], key[0])
    return rowcache[key]
def symrow(r, cols):
    # symplectic product of row r with unknown x on qubit set cols: returns coefficient vector over (x_X cols, x_Z cols)
    return np.concatenate([r[nq + np.array(cols)], r[np.array(cols)]])
def gf2_solve(A, b):
    M = np.concatenate([A, b[:, None]], 1).astype(np.uint8) % 2; m, n = A.shape; piv = []; r = 0
    for c in range(n):
        nz = np.flatnonzero(M[r:, c])
        if nz.size == 0: continue
        p = r + nz[0]; M[[r, p]] = M[[p, r]]
        rows = np.flatnonzero(M[:, c]); rows = rows[rows != r]; M[rows] ^= M[r]; piv.append(c); r += 1
        if r == m: break
    if M[r:, -1].any(): return None
    x = np.zeros(n, np.uint8)
    for i, c in enumerate(piv): x[c] = M[i, -1]
    return x
box0 = box((-1, -1, -1), (1, 1, 1))
def hop_system(d, sigma=None, probe_vals=None):
    a, s = bk.DIRS[d]; step = tuple(s * E[a][i] for i in range(3))
    lo = tuple(min(0, step[i]) - 1 for i in range(3)); hi = tuple(max(0, step[i]) + 1 for i in range(3))
    W = box(lo, hi); cols = qubits_of(W)
    rowbox = box(tuple(x - 2 for x in lo), tuple(x + 2 for x in hi))
    sidx = {(u, g): k for k, (u, g) in enumerate((u, g) for u in box0 for g in range(ng))}
    A, rhs, Sg = [], [], []
    for u in rowbox:
        for g in range(ng):
            A.append(symrow(row(u, g), cols))
            sv = np.zeros(len(sidx), np.uint8)
            if (u, g) in sidx: sv[sidx[(u, g)]] ^= 1
            ub = tuple(u[i] - step[i] for i in range(3))
            if (ub, g) in sidx: sv[sidx[(ub, g)]] ^= 1
            Sg.append(sv)
    A = np.array(A, np.uint8); Sg = np.array(Sg, np.uint8)
    if sigma is None:
        # unknowns (x, sigma): A x + Sg sigma = 0, with probe normalization
        Afull = np.concatenate([A, Sg], 1); b = np.zeros(len(A), np.uint8)
        extra = []
        for k, val in enumerate(probe_vals):
            e = np.zeros(Afull.shape[1], np.uint8); e[A.shape[1] + sidx[((0, 0, 0), P0 + k)]] = 1; extra.append((e, val))
        Afull = np.vstack([Afull] + [e for e, _ in extra]); b = np.concatenate([b, [v for _, v in extra]]).astype(np.uint8)
        sol = gf2_solve(Afull, b)
        if sol is None: return None, None, cols
        return sol[:A.shape[1]], sol[A.shape[1]:], cols
    sol = gf2_solve(A, (Sg.astype(np.int32) @ sigma.astype(np.int32)) % 2)
    return sol, sigma, cols
def to_full(x, cols):
    f = np.zeros(2 * nq, np.uint8); c = np.array(cols); f[c] = x[:len(cols)]; f[nq + c] = x[len(cols):]; return f
def run(probe_vals, name):
    x0, sigma, cols = hop_system(0, None, probe_vals)
    if x0 is None: print(name, ': no clean +x hop'); return
    hops = {}
    for d in range(6):
        x, _, cols = hop_system(d, sigma)
        if x is None: print(name, ': no clean hop in direction', d); return
        hops[d] = to_full(x, cols)
    def leg(d, n=2):
        a, s = bk.DIRS[d]; out = np.zeros(2 * nq, np.uint8)
        for k in range(n): out ^= shiftvec(hops[d], tuple(k * s * E[a][i] for i in range(3)))
        return out
    legs = {d: leg(d) for d in range(6)}
    def sy(x, y): return int((x[:nq].astype(int) @ y[nq:].astype(int) + x[nq:].astype(int) @ y[:nq].astype(int)) % 2)
    from collections import Counter
    cnt = Counter()
    for tr in itertools.combinations(range(6), 3):
        a, b, c = [legs[d] for d in tr]
        cnt[(-1) ** (sy(a, b) + sy(b, c) + sy(a, c))] += 1
    print(name, 'T-junction signs over 20 triples:', dict(cnt), flush=True)
run((1, 1, 1), 'f0')
run((0, 1, 1), 'b01')
run((1, 0, 1), 'b02')
