"""Pair test in the Majorana-per-direction code for the on-site signed-Majorana-permutation realizations."""
import pickle
exec(open('gse_sym.py').read().split("# (a) statistics")[0])
def perm_sign(p):
    p = list(p); s_ = 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; s_ = -s_
    return s_
exec("def image_word" + open('gse_sym.py').read().split("def image_word")[1].split("res = Counter(); good_eps = {}")[0])
MAJ = list(range(6))
# per-site decomposition table: bits (x3, z3) -> (subset of Majoranas, phase k) with X^x Z^z = i^k * prod_{d in subset, increasing} gamma_d
def site_word_pauli(sub):
    x = np.zeros(3, np.uint8); z = np.zeros(3, np.uint8); k = 0
    P = [x, z, 0]
    for d in sub:
        xb, zb, kk = JW[d]
        Q = [np.array(xb, np.uint8), np.array(zb, np.uint8), kk]
        s_ = int(P[1].astype(int) @ Q[0].astype(int)) % 2
        P = [P[0] ^ Q[0], P[1] ^ Q[1], (P[2] + Q[2] + 2 * s_) % 4]
    return P
TAB = {}
for r in range(7):
    for sub in itertools.combinations(range(6), r):
        P = site_word_pauli(sub); TAB[(tuple(P[0]), tuple(P[1]))] = (sub, P[2])
def map_pauli(P, M, eps):
    """Image of a Pauli under site rotation M and on-site gamma_d -> eps(d) gamma_{Rd} (MAJ = identity)."""
    out = [np.zeros(n, np.uint8), np.zeros(n, np.uint8), P[2]]
    for s in sorted(set((np.flatnonzero(P[0] | P[1]) // 3).tolist())):
        v = (s // (L * L), (s // L) % L, s % L)
        xb = tuple(P[0][3 * s:3 * s + 3]); zb = tuple(P[1][3 * s:3 * s + 3])
        sub, k = TAB[(xb, zb)]
        sgn, ws = image_word([(v, d) for d in sub], M, eps)
        W = word(ws)
        # X^x Z^z = i^k gamma_sub  =>  gamma_sub = i^{-k} X^x Z^z ; image of X^x Z^z = i^k * sgn * W
        add = [W[0], W[1], (W[2] + k + (0 if sgn == 1 else 2)) % 4]
        out = [out[0] ^ add[0], out[1] ^ add[1], (out[2] + add[2] + 2 * (int(out[1].astype(int) @ add[0].astype(int)) % 2)) % 4]
    return out
def bitmap(M, eps):
    """Linear map on (x|z) bits."""
    cols = []
    for j in range(2 * n):
        e = [np.zeros(n, np.uint8), np.zeros(n, np.uint8), 0]
        if j < n: e[0][j] = 1
        else: e[1][j - n] = 1
        im = map_pauli(e, M, eps); cols.append(np.concatenate([im[0], im[1]]))
    return np.array(cols).T   # (2n x 2n): new = Rmat @ old
def wrapv(p): return tuple(((c + L // 2) % L) - L // 2 for c in p)
def linf(p, q): return max(abs(p[i] - q[i]) for i in range(3))
def site_support(P):
    out = set()
    for q in np.flatnonzero(P[0] | P[1]):
        s = q // 3; out.add(wrapv((s // (L * L), (s // L) % L, s % L)))
    return out
def pair(G, lab, M, eps, x, Rmat):
    Rx = tuple(int(c) for c in M @ np.array(x))
    lo = tuple(min(x[i], Rx[i]) - 1 for i in range(3)); hi = tuple(max(x[i], Rx[i]) + 1 for i in range(3))
    sites = [p for p in itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)])]
    cols = np.array(sorted({3 * sidx(p) + t for p in sites for t in range(3)}))
    allc = np.concatenate([cols, n + cols])
    rows, rhs = [], []
    gs = [site_support(g) for g in G]
    for i, g in enumerate(G):
        if not any(all(lo[k] - 1 <= v[k] <= hi[k] + 1 for k in range(3)) for v in gs[i]): continue
        gv = np.concatenate([g[1], g[0]])                       # sym(S, g) = S . (gz | gx)
        cg = gv[allc]
        cgR = (gv.astype(np.int64) @ Rmat[:, allc].astype(np.int64)) % 2   # sym(R S, g)
        rows.append((cg ^ cgR.astype(np.uint8))); rhs.append(0)
        if lab[i][0] == 'B':
            rows.append(cg); rhs.append(1 if wrapv(lab[i][1]) in (wrapv(x), wrapv(Rx)) else 0)
        elif not any(linf(v, x) <= 1 or linf(v, Rx) <= 1 for v in gs[i]):
            rows.append(cg); rhs.append(0)
    A = np.concatenate([np.array(rows, np.uint8), np.array(rhs, np.uint8)[:, None]], 1); m, nn = len(rows), len(allc)
    piv, r = [], 0
    for c in range(nn):
        nz = np.flatnonzero(A[r:, c])
        if nz.size == 0: continue
        p = r + nz[0]; A[[r, p]] = A[[p, r]]; rr = np.flatnonzero(A[:, c]); rr = rr[rr != r]; A[rr] ^= A[r]; piv.append(c); r += 1
        if r == m: break
    if A[r:, -1].any(): return 'no S'
    sol = np.zeros(nn, np.uint8)
    for i, c in enumerate(piv): sol[c] = A[i, -1]
    Sx = np.zeros(n, np.uint8); Sz = np.zeros(n, np.uint8); Sx[cols] = sol[:len(cols)]; Sz[cols] = sol[len(cols):]
    S = [Sx, Sz, int(Sx.astype(int) @ Sz.astype(int)) % 4]
    T = rb.mulp(rb.dag(S), map_pauli(S, M, eps))
    tv = site_support(T)
    if not tv: return {0: 1, 2: -1}.get(T[2] % 4, 'imag')
    loc = [G[i] for i, sv in enumerate(gs) if sv and all(min(linf(v, u) for u in tv) <= 2 for v in sv)]
    f = rb.phase_in_group(loc, T)
    return None if f is None else {0: 1, 2: -1}.get(f, 'imag')
if __name__ == '__main__':
    out = Counter()
    for sec in ((0, 0, 0), (1, 1, 1)):
        G, lab, words = gens(sec)
        done = Counter()
        for k, M in enumerate(O):
            kd = bk.kind(M)
            if kd not in ('C2axis', 'C2edge') or done[kd] >= 2: continue
            done[kd] += 1
            pi = [bk.rotdir(M, d) for d in range(6)]
            # group-law-respecting sign choices: eps(d) eps(Rd) the same for all moved d (U^2 = 1 or (-1)^F)
            valid = []
            for eps in itertools.product((1, -1), repeat=6):
                if np.prod(eps) != perm_sign(pi): continue
                prods = {eps[d] * eps[pi[d]] for d in range(6) if pi[d] != d}
                fixed = [d for d in range(6) if pi[d] == d]
                if len(prods) == 1 and (prods == {1} or not fixed): valid.append((eps, prods.pop()))
            for eps, pr in valid[:2]:
                Rmat = bitmap(M, eps)
                xs = [x for x in itertools.product(range(-2, 3), repeat=3) if linf(x, tuple(int(c) for c in M @ np.array(x))) >= 3][:2]
                lam = tuple(pair(G, lab, M, eps, x, Rmat) for x in xs)
                out[(sec, kd, 'U^2 = ' + ('1' if pr == 1 else '(-1)^F'), lam)] += 1
                print(sec, kd, eps, pr, lam, flush=True)
    print('FINAL', dict(out))
