"""Half-edge BKSF code with an on-site Majorana-permutation Clifford (in-site JW in the code's own ordering)."""
import sys, itertools
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17 as rb
bk, c1 = rb.bk, rb.c1
from collections import Counter, defaultdict
E, DIRS, O = bk.E, bk.DIRS, c1.O
L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
n = 6 * L ** 3
rb.L, rb.N = L, n
V = list(itertools.product(range(L), repeat=3))
def s_(v): return ((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)
def q(v, d): return 6 * s_(v) + d
one = lambda: [np.zeros(n, np.uint8), np.zeros(n, np.uint8), 0]
def single(qq, lab):   # lab 'X','Y','Z' Hermitian
    P = one()
    if lab in 'XY': P[0][qq] = 1
    if lab in 'YZ': P[1][qq] = 1
    if lab == 'Y': P[2] = 1
    return P
def mul(*Ps):
    R = one()
    for P in Ps: R = rb.mulp(R, P)
    return R
def maj(v, d, kind, order):
    """mu (kind 0) = X_d prod Z_{before d}; nu (kind 1) = Y_d prod Z_{before d}; JW order = position in `order`."""
    pos = {dd: i for i, dd in enumerate(order)}
    P = single(q(v, d), 'X' if kind == 0 else 'Y')
    for dd in range(6):
        if pos[dd] < pos[d]: P = mul(single(q(v, dd), 'Z'), P)
    return P
def A_half(v, a, order):
    w = tuple(v[i] + E[a][i] for i in range(3))
    return mul(maj(v, DIRS.index((a, 1)), 0, order), maj(w, DIRS.index((a, -1)), 0, order))
def herm(P):
    if (P[2] - int(P[0].astype(int) @ P[1].astype(int))) % 2: P = [P[0], P[1], (P[2] + 1) % 4]
    return P
def gens(order, signs):
    G = []
    for v in V:
        G.append(mul(*[single(q(v, d), 'Z') for d in range(6)]))
        for a in range(3):
            w = tuple(v[i] + E[a][i] for i in range(3))
            G.append(mul(single(q(v, DIRS.index((a, 1))), 'Z'), single(q(w, DIRS.index((a, -1))), 'Z')))
        for c in range(3):
            a, b = [t for t in range(3) if t != c]
            va = tuple(v[i] + E[a][i] for i in range(3)); vb = tuple(v[i] + E[b][i] for i in range(3))
            P = herm(mul(A_half(v, a, order), A_half(va, b, order), A_half(vb, a, order), A_half(v, b, order)))
            P[2] = (P[2] + 2 * signs[c]) % 4
            G.append(P)
    return G
# site decomposition: any 6-qubit Pauli on a site = i^k * ordered product of Majoranas (mu_0..5, nu_0..5 in a fixed list order)
def site_table(order):
    mlist = [(d, k) for d in range(6) for k in (0, 1)]
    tab = {}
    v0 = (0, 0, 0)
    base = [maj(v0, d, k, order) for d, k in mlist]
    for mask in range(1 << 12):
        P = one()
        for i in range(12):
            if mask >> i & 1: P = rb.mulp(P, base[i])
        key = (tuple(P[0][:6]), tuple(P[1][:6]))
        if key not in tab: tab[key] = (mask, P[2])
    return mlist, tab
def map_pauli(P, M, eps, order, mlist, tab):
    out = [np.zeros(n, np.uint8), np.zeros(n, np.uint8), P[2]]
    for s in sorted(set((np.flatnonzero(P[0] | P[1]) // 6).tolist())):
        v = (s // (L * L), (s // L) % L, s % L)
        mask, k = tab[(tuple(P[0][6 * s:6 * s + 6]), tuple(P[1][6 * s:6 * s + 6]))]
        w = tuple(int(x) for x in M @ np.array(v))
        W = one(); sgn = 1
        for i in range(12):
            if mask >> i & 1:
                d, kk = mlist[i]; sgn *= eps[i]
                W = rb.mulp(W, maj(w, bk.rotdir(M, d), kk, order))
        add = [W[0], W[1], (W[2] - k + (0 if sgn == 1 else 2)) % 4]
        sg = int(out[1].astype(int) @ add[0].astype(int)) % 2
        out = [out[0] ^ add[0], out[1] ^ add[1], (out[2] + add[2] + 2 * sg) % 4]
    return out
if __name__ == '__main__':
    orders = list(itertools.permutations(range(6)))
    H = {o: bk.span_hash(bk.torus_rows(bk.gens(o), 4)) for o in orders}
    classes = defaultdict(list)
    for o in orders: classes[H[o]].append(o)
    res = Counter()
    for h, ords in list(classes.items())[: int(sys.argv[2]) if len(sys.argv) > 2 else 60]:
        o = ords[0]
        mlist, tab = site_table(o)
        for sec in ((0, 0, 0), (1, 1, 1)):
            G = gens(o, sec)
            Mg = np.array([np.concatenate([g[0], g[1]]) for g in G]).T
            near = [g for g in G if (g[0][:6] | g[1][:6]).any()]     # generators touching site 0
            for M in O:
                ok_any = False
                # sign choices: eps per (direction, kind); search the 4096 choices for one preserving all near generators
                for eps in itertools.product((1, -1), repeat=12):
                    good = True
                    for g in near:
                        im = map_pauli(g, M, eps, o, mlist, tab)
                        f = rb.phase_in_group(G, im) if False else None
                        W, okk = rb.solve_multi(Mg, np.concatenate([im[0], im[1]])[:, None])
                        if not okk[0]: good = False; break
                        R = rb.one()
                        for i in np.nonzero(W[:, 0])[0]: R = rb.mulp(R, G[i])
                        if R[2] != im[2]: good = False; break
                    if good: ok_any = True; break
                res[(sec, bk.kind(M), ok_any)] += 1
        print(len(res), dict(res), flush=True)
    print('FINAL', dict(res))
