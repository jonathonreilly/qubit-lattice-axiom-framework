"""Pair test for every (code, C2) pair, using an R-invariant corner-dressed flux convention with local clean hops."""
import sys, itertools, time
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17 as rb
bk = rb.bk; c1 = rb.c1
from collections import Counter, defaultdict
Lp = 6
rb.L = Lp; rb.N = 3 * Lp ** 3
N = rb.N; E = bk.E; O = c1.O
orders = list(itertools.permutations(range(6)))
H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
classes = defaultdict(list)
for o in orders: classes[H[o]].append(o)
V = list(itertools.product(range(Lp), repeat=3))
def vec(op):
    P = rb.from_op(op); return np.concatenate([P[0], P[1]])
def rref(R):
    A = (np.array(R, np.uint8) % 2).copy(); m, n = A.shape; r = 0
    for c in range(n):
        nz = np.flatnonzero(A[r:, c])
        if nz.size == 0: continue
        p = r + nz[0]
        if p != r: A[[r, p]] = A[[p, r]]
        rows = np.flatnonzero(A[:, c]); rows = rows[rows != r]
        if rows.size: A[rows] ^= A[r]
        r += 1
        if r == m: break
    return r, A[:r]
def gf2_solve(A, b):
    M = np.concatenate([A, b[:, None]], 1).astype(np.uint8) % 2; m, nn = A.shape; piv = []; r = 0
    for c in range(nn):
        nz = np.flatnonzero(M[r:, c])
        if nz.size == 0: continue
        p = r + nz[0]; M[[r, p]] = M[[p, r]]
        rows = np.flatnonzero(M[:, c]); rows = rows[rows != r]; M[rows] ^= M[r]; piv.append(c); r += 1
        if r == m: break
    if M[r:, -1].any(): return None
    x = np.zeros(nn, np.uint8)
    for i, c in enumerate(piv): x[c] = M[i, -1]
    return x
SH = {}
for v in V:
    perm = np.zeros(N, int)
    for u in V:
        for a in range(3):
            k = 3 * ((u[0] * Lp + u[1]) * Lp + u[2]) + a; w = tuple((u[i] + v[i]) % Lp for i in range(3))
            perm[k] = 3 * ((w[0] * Lp + w[1]) * Lp + w[2]) + a
    SH[v] = perm
def shiftv(x, v):
    y = np.zeros_like(x); p = SH[tuple(c % Lp for c in v)]; y[p] = x[:N]; y[N + p] = x[N:]; return y
def torus(gs):
    base = [vec(g) for g in gs]
    return np.array([shiftv(b, v) for v in V for b in base])
def rot_op(M, op):
    out = {}
    for (p, a), l in op.items():
        w = tuple(int(x) for x in M @ np.array(p)); d = M @ np.array(E[a]); b = int(np.nonzero(d)[0][0])
        q = w if d[b] == 1 else tuple(w[t] - (1 if t == b else 0) for t in range(3))
        out[(q, b)] = l
    return out
def corners(c):
    a, b = [t for t in range(3) if t != c]
    return [(0, 0, 0), tuple(E[a]), tuple(E[b]), tuple(np.add(E[a], E[b]))]
Brows = torus([bk.B((0, 0, 0))])
win = [(p, a) for p in itertools.product(range(-1, 3), repeat=3) for a in range(3)]
cols = np.array(sorted({3 * (((p[0] % Lp) * Lp + (p[1] % Lp)) * Lp + (p[2] % Lp)) + a for p, a in win}))
def symm(R): return np.concatenate([R[:, N + cols], R[:, cols]], 1)
subsets = [list(s) for k in range(5) for s in itertools.combinations(range(4), k)]
def Fg(o, bs):
    gs = []
    for c in range(3):
        g = bk.plaq((0, 0, 0), c, o)
        for i in bs[c]: g = bk.prod(g, bk.B(corners(c)[i]))
        gs.append(g)
    return gs
def screen4(o, M):
    out = []
    for bs in itertools.product(subsets, repeat=3):
        gs = Fg(o, bs)
        R0 = bk.torus_rows(gs, 4); r0, b0 = rref(R0)
        if r0 != 126: continue
        if rref(np.vstack([b0, bk.torus_rows([rot_op(M, g) for g in gs], 4)]))[0] == r0: out.append(bs)
    return out
def find_convention(o, M):
    """Corner-dressed flux convention invariant under M (screened at L = 4, confirmed at L = 6), with local clean hops."""
    for bs in screen4(o, M):
        gs = Fg(o, bs)
        Fr = torus(gs); rF, bF = rref(Fr)
        if rF != 430: continue
        if rref(np.vstack([bF, torus([rot_op(M, g) for g in gs])]))[0] != rF: continue
        print('  candidate', bs, flush=True)
        hops = []
        for a in range(3):
            Aa = vec(bk.A((0, 0, 0), a, o))
            rhs = (Fr[:, :N].astype(int) @ Aa[N:].astype(int) + Fr[:, N:].astype(int) @ Aa[:N].astype(int)) % 2
            d = gf2_solve(np.vstack([symm(Fr), symm(Brows)]), np.concatenate([rhs, np.zeros(len(Brows), int)]).astype(np.uint8))
            if d is None: break
            dv = np.zeros(2 * N, np.uint8); dv[cols] = d[:len(cols)]; dv[N + cols] = d[len(cols):]
            hops.append(Aa ^ dv)
        if len(hops) == 3: return bs, hops
    return None, None
def pauli_of(v):   # vector -> [x, z, k] Hermitian
    x = v[:N].copy(); z = v[N:].copy(); return [x, z, int(x.astype(int) @ z.astype(int)) % 4]
def shiftP(P, s):
    p = SH[tuple(c % Lp for c in s)]; x = np.zeros(N, np.uint8); z = np.zeros(N, np.uint8); x[p] = P[0]; z[p] = P[1]; return [x, z, P[2]]
def pair_lambda(hops, G, M, x):
    Rx = tuple(int(c) for c in M @ np.array(x))
    S = rb.one()
    for (v, a) in rb.path(x, Rx):
        S = rb.mulp(S, shiftP(pauli_of(hops[a]), v))
    f = rb.phase_in_group(G, rb.mulp(rb.dag(S), rb.apply_perm(S, rb.perm_of(M))))
    return None if f is None else {0: 1, 2: -1}.get(f, 'imag')
xs = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (-1, 0, 0), (1, -1, 0)]
res = Counter(); per = []
t0 = time.time()
mode = sys.argv[1] if len(sys.argv) > 1 else 'uncovered'
for h, ords in classes.items():
    o = ords[0]
    stab = [M for M in O if H[bk.rot_order(M, o)] == h]
    print("class", o, len(stab), round(time.time() - t0), flush=True)
    for M in stab:
        if bk.kind(M) not in ('C2edge', 'C2axis'): continue
        covered = any(rb.plaq_span(oo) == rb.plaq_span(bk.rot_order(M, oo)) for oo in ords)
        if mode == 'uncovered' and covered: continue
        bs, hops = find_convention(o, M)
        if hops is None:
            res[(24 // len(stab), bk.kind(M), 'no convention')] += 1; continue
        for sec in ((0, 0, 0), (1, 1, 1)):
            G, lab = rb.gens(o, sec)
            lam = Counter(pair_lambda(hops, G, M, x) for x in xs if tuple(int(c) for c in M @ np.array(x)) != x)
            res[(24 // len(stab), bk.kind(M), sec, tuple(sorted(lam.items(), key=str)))] += 1
        print(len(res), dict(res), round(time.time() - t0), flush=True)
print('FINAL', dict(res))
