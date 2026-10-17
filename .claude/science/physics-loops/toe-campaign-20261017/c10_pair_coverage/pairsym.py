"""General pair test: solve for S creating fermions at x and Rx (no other excitations away from x, Rx) such that
S and P_R S P_R^-1 create the same excitations; lambda = sign of S^dag S^R in the signed group."""
import sys, itertools, time
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17 as rb
bk = rb.bk; c1 = rb.c1
from collections import Counter, defaultdict
Lp = int(sys.argv[2]) if len(sys.argv) > 2 else 8
rb.L = Lp; rb.N = 3 * Lp ** 3
N = rb.N; E = bk.E; O = c1.O
orders = list(itertools.permutations(range(6)))
H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
classes = defaultdict(list)
for o in orders: classes[H[o]].append(o)
def wrap(p): return tuple(((c + Lp // 2) % Lp) - Lp // 2 for c in p)   # coordinates in [-L/2, L/2)
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
def qidx(p, a): return 3 * (((p[0] % Lp) * Lp + (p[1] % Lp)) * Lp + (p[2] % Lp)) + a
def support_vertices(P):
    qs = np.flatnonzero(P[0] | P[1]); out = set()
    for q in qs:
        e = q // 3; a = q % 3; p = (e // (Lp * Lp), (e // Lp) % Lp, e % Lp)
        out.add(wrap(p)); out.add(wrap(tuple(p[i] + E[a][i] for i in range(3))))
    return out
def linf(p, q): return max(abs(p[i] - q[i]) for i in range(3))
def run_pair(o, M, sec, x, G, lab, gsup):
    Rx = tuple(int(c) for c in M @ np.array(x))
    lo = tuple(min(x[i], Rx[i]) - 1 for i in range(3)); hi = tuple(max(x[i], Rx[i]) + 1 for i in range(3))
    W = [(p, a) for p in itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)]) for a in range(3)
         if all(lo[i] <= p[i] + E[a][i] <= hi[i] for i in range(3))]
    cols = np.array(sorted({qidx(p, a) for p, a in W}))
    perm = rb.perm_of(M)
    # generators touching W or R(W)
    rel = [i for i, s in enumerate(gsup) if any(lo[k] - 1 <= v[k] <= hi[k] + 1 for k in range(3) for v in [None] if False) or
           any(all(lo[k] - 1 <= v[k] <= hi[k] + 1 for k in range(3)) for v in s)]
    rows, rhs = [], []
    inv = np.argsort(perm)
    for i in rel:
        g = G[i]
        cg = np.concatenate([g[1][cols], g[0][cols]])                    # coef of S in sym(S, g)
        # sym(R S, g) = sym(S, R^-1 g): R^-1 g has bits g[perm[q]] at q
        gR = [g[0][perm], g[1][perm]]
        cgR = np.concatenate([gR[1][cols], gR[0][cols]])
        rows.append(cg ^ cgR); rhs.append(0)                              # S and R(S) have the same syndrome
        near = any(linf(v, x) <= 1 or linf(v, Rx) <= 1 for v in gsup[i])
        if lab[i][0] == 'B':
            v = wrap(lab[i][1]); rows.append(cg); rhs.append(1 if v in (wrap(x), wrap(Rx)) else 0)
        elif not near:
            rows.append(cg); rhs.append(0)                                # no excitations away from x, Rx
    s = gf2_solve(np.array(rows, np.uint8), np.array(rhs, np.uint8))
    if s is None: return 'no S'
    Sx = np.zeros(N, np.uint8); Sz = np.zeros(N, np.uint8); Sx[cols] = s[:len(cols)]; Sz[cols] = s[len(cols):]
    S = [Sx, Sz, int(Sx.astype(int) @ Sz.astype(int)) % 4]
    T = rb.mulp(rb.dag(S), rb.apply_perm(S, perm))
    # restrict the group solve to generators near the support of T
    tv = support_vertices(T)
    loc = [i for i, s_ in enumerate(gsup) if s_ and all(min(linf(v, u) for u in tv) <= 2 for v in s_)] if tv else []
    if not tv: return 1 if T[2] % 4 == 0 else ('-1' if T[2] % 4 == 2 else 'imag')
    f = rb.phase_in_group([G[i] for i in loc], T)
    return None if f is None else {0: 1, 2: -1}.get(f, 'imag')
mode = sys.argv[1] if len(sys.argv) > 1 else 'uncovered'
xs_by_kind = {}
res = Counter(); t0 = time.time()
for h, ords in classes.items():
    o = ords[0]
    stab = [M for M in O if H[bk.rot_order(M, o)] == h]
    todo = []
    for M in stab:
        if bk.kind(M) not in ('C2edge', 'C2axis'): continue
        covered = any(rb.plaq_span(oo) == rb.plaq_span(bk.rot_order(M, oo)) for oo in ords)
        if (mode == 'uncovered') == covered: continue
        todo.append(M)
    if not todo: continue
    for sec in ((0, 0, 0), (1, 1, 1)):
        G, lab = rb.gens(o, sec)
        gsup = [support_vertices(g) for g in G]
        for M in todo:
            # off-axis x with x and Rx separated by >= 3 (L-infinity)
            cand = [x for x in itertools.product(range(-2, 3), repeat=3) if linf(x, tuple(int(c) for c in M @ np.array(x))) >= 3]
            out = Counter(run_pair(o, M, sec, x, G, lab, gsup) for x in cand[:2])
            res[(24 // len(stab), bk.kind(M), sec, tuple(sorted(out.items(), key=str)))] += 1
            print(len(res), round(time.time() - t0), dict(res), flush=True)
print('FINAL', dict(res))
