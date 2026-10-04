"""A53 library (supplied toys; nothing adopted).  Exact cluster tools for A51's short rules, dual (Klein) frame.
Rule = sum_c J_c O_c + sum_k c_k F_k : O_c = dual Heisenberg class sums (each lattice pair once), F_k = A49's star
four-spin operators (normalized as in A49 four_basis).  On a finite periodic cluster the infinite-lattice operator is
WRAPPED (sum over anchors x of the anchored terms, sites taken mod the superlattice), as in A49/A51 fwd16.
Configuration bit = 1 means dual s^z = -1 (A49 convention, z = 1 - 2 bit).
  s_i.s_j = z_i z_j + 2 X_ij  (X flips i, j when they differ)
  (s_a.s_b)(s_c.s_d) = z_a z_b z_c z_d + 2 z_c z_d X_ab + 2 z_a z_b X_cd + 4 X_ab X_cd    (disjoint pairs)
Star four-spin terms are regrouped by star centre (every T/C/Dm/Y four-set lies in exactly one star) and applied with
per-pattern (7-bit) tables.  Spin-flip reduction: for N = 0 mod 4 every singlet is even under global flip
(prod sigma^x = (-i)^N exp(i pi S^x)), so the even sector (top bit 0 representatives) holds all S-even states."""
import sys, itertools, time, numpy as np
D53 = __file__.rsplit('/', 1)[0]
sys.path.insert(0, D53.rsplit('/', 1)[0] + "/A51")
from a51lib import *          # noqa: a49lib (four_basis, PAIRINGS, mf_state, ...), a46lib (Cluster, cube, ...)
import numba as nb

F4 = four_basis()             # T0 T2 C0 Dm0 Dm1 Y0 Y1 Y2 P0 P1
F4N = [f[0] for f in F4]
STAR = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
SLOC = {s: l for l, s in enumerate(STAR)}
LPAIRS = [(a, b) for a in range(7) for b in range(a + 1, 7)]
LPIDX = {p: n for n, p in enumerate(LPAIRS)}


def load_rule(L, key):
    R = np.load(f"{D53}/../A51/rules51_{L}.npz"); ks = [tuple(int(c) for c in k) for k in R["ks"]]; v = R[key]; nc = len(ks)
    return ks, v[:nc].astype(float).copy(), v[nc:].astype(float).copy()


def class_vectors(k):
    out = set()
    for perm in itertools.permutations(k):
        for sg in itertools.product((1, -1), repeat=3):
            d = tuple(int(sg[i] * perm[i]) for i in range(3))
            if d != (0, 0, 0):
                out.add(max(d, tuple(-c for c in d)))
    return sorted(out)


def periodic_index(cl):
    return lambda x: cl.idx[tuple(int(c) for c in cl.canon(np.array(x))[0])]


def open_index(sites):
    d = {tuple(int(c) for c in s): i for i, s in enumerate(sites)}
    return lambda x: d.get(tuple(int(c) for c in x))


def bilinear_pairs(X, f, ks, J, tol=1e-14):
    """{(i,j): coef} of sum_c J_c O_c, anchors X (wrapped if f is periodic; open: pairs inside only)."""
    pairs = {}
    for kc, Jc in zip(ks, J):
        if abs(Jc) < tol: continue
        V = class_vectors(kc)
        for x in X:
            i = f(x)
            for d in V:
                j = f(np.array(x) + np.array(d))
                if j is None: continue
                assert j != i, "pair wraps onto itself"
                key = (min(i, j), max(i, j)); pairs[key] = pairs.get(key, 0.) + Jc
    return pairs


def bilinear_pairs_once(X, f, ks, J, tol=1e-14):
    """'pair-once' convention (A51's torus convention): every cluster pair carries the coupling of the SHORTEST
    displacement (within the rule's classes) connecting it, counted once; no wrap multiplicities."""
    best = {}
    for kc, Jc in zip(ks, J):
        if abs(Jc) < tol: continue
        n2 = sum(c * c for c in kc)
        for d in class_vectors(kc):
            for x in X:
                i = f(x); j = f(np.array(x) + np.array(d)); key = (min(i, j), max(i, j))
                if key not in best or n2 < best[key][0]: best[key] = (n2, Jc)
                elif n2 == best[key][0]: assert abs(best[key][1] - Jc) < 1e-12
    return {k: v[1] for k, v in best.items()}


def star_local(c4):
    """Star-centred local four-spin operator: {(l0<l1<l2<l3): w[3]} (pairing index as in PAIRINGS over sorted key)."""
    assert len(c4) < 9 or np.allclose(c4[8:], 0), "plaquette four-spin terms not in a star"
    out = {}
    for k in range(min(8, len(c4))):
        if c4[k] == 0: continue
        for (Ps, pi), w in F4[k][2].items():
            P = [np.array(p) for p in Ps]; cen = None
            for cand in set(tuple(p + e) for p in P for e in [np.zeros(3, int)] + [np.array(s) for s in STAR[1:]]):
                if all(tuple(int(v) for v in p - np.array(cand)) in SLOC for p in P):
                    assert cen is None or cen == cand; cen = cand
            assert cen is not None
            ls = [SLOC[tuple(int(v) for v in p - np.array(cen))] for p in P]
            order = sorted(range(4), key=lambda q: ls[q]); S = tuple(ls[q] for q in order)
            inv = {order[q]: q for q in range(4)}
            pr = tuple(sorted(tuple(sorted((inv[u], inv[v]))) for u, v in PAIRINGS[pi]))
            out.setdefault(S, np.zeros(3))[PAIRINGS.index(pr)] += c4[k] * w
    return out


def star_tables(sl):
    """Per 7-bit pattern: diagonal DG, single-flip increments (local pair idx, value), double flips (four-set idx, value)."""
    fsl = sorted(sl); DG = np.zeros(128); SF = [[] for _ in range(128)]; DF = [[] for _ in range(128)]
    for P in range(128):
        b = [(P >> l) & 1 for l in range(7)]; z = [1 - 2 * v for v in b]; inc = {}
        for q, S in enumerate(fsl):
            w = sl[S]; DG[P] += w.sum() * z[S[0]] * z[S[1]] * z[S[2]] * z[S[3]]; dfc = 0.
            for pi, ((u, v), (x, y)) in enumerate(PAIRINGS):
                a, bb, c, d = S[u], S[v], S[x], S[y]
                if b[a] != b[bb]: inc[LPIDX[(a, bb)]] = inc.get(LPIDX[(a, bb)], 0.) + 2 * w[pi] * z[c] * z[d]
                if b[c] != b[d]: inc[LPIDX[(c, d)]] = inc.get(LPIDX[(c, d)], 0.) + 2 * w[pi] * z[a] * z[bb]
                if b[a] != b[bb] and b[c] != b[d]: dfc += 4 * w[pi]
            if dfc != 0.: DF[P].append((q, dfc))
        SF[P] = sorted(inc.items())
    ptr = lambda L: np.cumsum([0] + [len(x) for x in L]).astype(np.int64)
    SFp, DFp = ptr(SF), ptr(DF)
    SFl = np.array([e[0] for x in SF for e in x], np.int64); SFv = np.array([e[1] for x in SF for e in x])
    DFl = np.array([e[0] for x in DF for e in x], np.int64); DFv = np.array([e[1] for x in DF for e in x])
    return fsl, DG, SFp, SFl, SFv, DFp, DFl, DFv


class Ham:
    """Wrapped rule on a periodic cluster (or open site set with f returning None outside).  Star terms need all 7 star
    sites present: for open clusters star four-sets are taken directly (slow path, small clusters only)."""
    def __init__(self, X, f, ks, J, c4, periodic=True, once=False):
        self.N = N = len(X); X = [np.array(x) for x in X]
        pairs = bilinear_pairs_once(X, f, ks, J) if once else bilinear_pairs(X, f, ks, J)
        sl = star_local(c4) if np.any(np.asarray(c4)[:8] != 0) else {}
        self.fsl, self.DG, self.SFp, self.SFl, self.SFv, self.DFp, self.DFl, self.DFv = star_tables(sl)
        if periodic:
            glob = np.array([[f(x + np.array(s)) for s in STAR] for x in X], np.int64)
            assert all(len(set(g)) == 7 for g in glob), "star sites coincide"
        else:
            raise NotImplementedError("open clusters: use dense_open()")
        for g in glob:
            for (a, b) in LPAIRS:
                key = (min(g[a], g[b]), max(g[a], g[b])); pairs.setdefault(key, 0.)
        self.pairs = pairs; pk = sorted(pairs)
        self.pidx = {p: n for n, p in enumerate(pk)}
        self.pm = np.array([(1 << i) | (1 << j) for i, j in pk], np.int64); self.pJ = np.array([pairs[p] for p in pk])
        self.pi = np.array([p[0] for p in pk], np.int64); self.pj = np.array([p[1] for p in pk], np.int64)
        self.glob = glob
        self.fpg = np.array([[self.pidx[(min(g[a], g[b]), max(g[a], g[b]))] for (a, b) in LPAIRS] for g in glob], np.int64)
        self.fsm = np.array([[sum(1 << int(g[l]) for l in S) for S in self.fsl] for g in glob], np.int64).reshape(len(glob), -1)
        if self.fsm.shape[1] == 0: self.fsm = np.zeros((len(glob), 1), np.int64)


# ------------------------------------------------------------------ S^z = 0 sector, Lin two-table ranking
@nb.njit(cache=True)
def _enum(N, nd, flip):
    cnt = 0; top = N - 1
    for c in range(1 << N):
        if flip and (c >> top) & 1: continue
        x = c; k = 0
        while x:
            x &= x - 1; k += 1
        if k == nd: cnt += 1
    out = np.empty(cnt, np.int64); n = 0
    for c in range(1 << N):
        if flip and (c >> top) & 1: continue
        x = c; k = 0
        while x:
            x &= x - 1; k += 1
        if k == nd:
            out[n] = c; n += 1
    return out


class Sector:
    def __init__(self, N, flip=True):
        assert N % 4 == 0 or not flip
        self.N = N; self.flip = flip; self.h = h = N // 2
        self.confs = _enum(N, N // 2, flip); self.D = len(self.confs)
        pc = np.array([bin(v).count("1") for v in range(1 << h)])
        self.idxlo = np.zeros(1 << h, np.int64); seen = np.zeros(h + 1, np.int64)
        for v in range(1 << h):
            self.idxlo[v] = seen[pc[v]]; seen[pc[v]] += 1
        hi = self.confs >> h
        self.offset = -np.ones(1 << (N - h), np.int64)
        first = np.r_[True, hi[1:] != hi[:-1]]
        self.offset[hi[first]] = np.flatnonzero(first)
        self.lomask = (1 << h) - 1; self.full = (1 << N) - 1; self.top = N - 1
        assert np.all(self.offset[hi] + self.idxlo[self.confs & self.lomask] == np.arange(self.D))


@nb.njit(cache=True)
def _rank(c, offset, idxlo, h, lomask, flip, top, full):
    if flip and (c >> top) & 1:
        c = (~c) & full
    return offset[c >> h] + idxlo[c & lomask]


@nb.njit(cache=True)
def _matvec(x, y, confs, offset, idxlo, h, lomask, flip, top, full,
            pm, pJ, glob, DG, SFp, SFl, SFv, DFp, DFl, DFv, fpg, fsm, use4):
    npair = len(pm); nst = glob.shape[0]; coef = np.empty(npair); Jsum = 0.
    for p in range(npair): Jsum += pJ[p]
    for k in range(len(confs)):
        c = confs[k]
        for p in range(npair): coef[p] = 2. * pJ[p]
        acc = 0.; dg = Jsum
        if use4:
            for s in range(nst):
                pat = 0
                for l in range(7): pat |= ((c >> glob[s, l]) & 1) << l
                dg += DG[pat]
                for e in range(SFp[pat], SFp[pat + 1]): coef[fpg[s, SFl[e]]] += SFv[e]
                for e in range(DFp[pat], DFp[pat + 1]):
                    c2 = c ^ fsm[s, DFl[e]]
                    acc += DFv[e] * x[_rank(c2, offset, idxlo, h, lomask, flip, top, full)]
        for p in range(npair):
            m = pm[p]; cm = c & m
            if cm != 0 and cm != m:
                dg -= 2. * pJ[p]
                acc += coef[p] * x[_rank(c ^ m, offset, idxlo, h, lomask, flip, top, full)]
        y[k] = acc + dg * x[k]


def make_mv(H, S):
    use4 = len(H.fsl) > 0
    def mv(x):
        x = np.ascontiguousarray(np.asarray(x, dtype=np.float64).ravel()); y = np.empty_like(x)
        _matvec(x, y, S.confs, S.offset, S.idxlo, S.h, S.lomask, S.flip, S.top, S.full, H.pm, H.pJ, H.glob, H.DG,
                H.SFp, H.SFl, H.SFv, H.DFp, H.DFl, H.DFv, H.fpg, H.fsm, use4)
        return y
    return mv


@nb.njit(cache=True)
def _paircorr(x, confs, offset, idxlo, h, lomask, flip, top, full, N):
    """<s_i.s_j> for all i<j (unnormalized sums; divide by sum x^2)."""
    out = np.zeros((N, N))
    for k in range(len(confs)):
        c = confs[k]; xk = x[k]; w = xk * xk
        for i in range(N):
            bi = (c >> i) & 1
            for j in range(i + 1, N):
                bj = (c >> j) & 1
                if bi == bj:
                    out[i, j] += w
                else:
                    out[i, j] -= w
                    out[i, j] += 2. * xk * x[_rank(c ^ ((1 << i) | (1 << j)), offset, idxlo, h, lomask, flip, top, full)]
    return out


def paircorr(x, S):
    C = _paircorr(np.ascontiguousarray(x, dtype=np.float64), S.confs, S.offset, S.idxlo, S.h, S.lomask, S.flip, S.top, S.full, S.N)
    C = C / np.dot(x, x); C = C + C.T; np.fill_diagonal(C, 3.); return C


def full_vector(x, S):
    """Embed a sector vector into 2^N (spin-flip partner filled when flip=True); normalized."""
    v = np.zeros(1 << S.N); v[S.confs] = x
    if S.flip: v[(~S.confs) & S.full] = x
    return v / np.linalg.norm(v)


def rdm(v, N, sites):
    """Reduced density matrix of `sites` (bit order: sites[0] = least significant of the subsystem index)."""
    T = v.reshape((2,) * N)                          # axis a <-> bit N-1-a
    ax = [N - 1 - s for s in sites][::-1]
    rest = [a for a in range(N) if a not in ax]
    M = np.transpose(T, ax + rest).reshape(1 << len(sites), -1)
    return M @ M.T


def spin_projectors(n):
    """Projectors onto total spin S of n spins-1/2 (dense 2^n)."""
    sx = np.array([[0, 1], [1, 0]]) / 2.; sy = np.array([[0, -1j], [1j, 0]]) / 2.; sz = np.diag([0.5, -0.5])
    def op(o, i):
        out = np.array([[1.]]);
        for k in range(n - 1, -1, -1):
            out = np.kron(out, o if k == i else np.eye(2))
        return out
    Stot = [sum(op(o, i) for i in range(n)) for o in (sx, sy, sz)]
    C = sum(s @ s for s in Stot).real
    w, U = np.linalg.eigh(C); out = {}
    for Sv in np.arange(n % 2 / 2, n / 2 + 0.1, 1.):
        sel = np.abs(w - Sv * (Sv + 1)) < 1e-6; out[Sv] = U[:, sel] @ U[:, sel].T
    return out


def parton_vector(cl, S, Phi=None, chunk=8192):
    """Projected parton amplitudes on the sector (real up to a global phase, which is removed)."""
    if Phi is None: Phi, _ = mf_state(cl)
    N = S.N; rows0 = 2 * np.arange(N); out = np.empty(S.D, complex)
    for s0 in range(0, S.D, chunk):
        bits = ((S.confs[s0:s0 + chunk, None] >> np.arange(N)[None, :]) & 1)
        out[s0:s0 + chunk] = np.linalg.det(Phi[rows0[None, :] + bits])
    k = np.argmax(np.abs(out)); out = out * np.exp(-1j * np.angle(out[k]))
    return out


# ------------------------------------------------------------------ generic (slow) path: explicit four-sets, any site set
def four_sets(X, f, c4, tol=1e-14):
    """{(a<b<c<d): w[3]} of sum_k c4_k F_k (all ten A49 four-spin ops), anchors X; open f -> sets inside only."""
    out = {}
    for k, ck in enumerate(c4):
        if abs(ck) < tol: continue
        for x in X:
            for (Ps, pi), w in F4[k][2].items():
                cs = [f(np.array(x) + np.array(p)) for p in Ps]
                if any(c is None for c in cs): continue
                assert len(set(cs)) == 4
                order = sorted(range(4), key=lambda q: cs[q]); S = tuple(cs[q] for q in order)
                inv = {order[q]: q for q in range(4)}
                pr = tuple(sorted(tuple(sorted((inv[u], inv[v]))) for u, v in PAIRINGS[pi]))
                out.setdefault(S, np.zeros(3))[PAIRINGS.index(pr)] += ck * w
    return out


@nb.njit(cache=True)
def _matvec_gen(x, y, confs, offset, idxlo, h, lomask, flip, top, full, pm, pJ, fs, fw):
    npair = len(pm); nf = fs.shape[0]
    PA = np.array([[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2]])
    z = np.empty(4); b = np.empty(4, np.int64)
    for k in range(len(confs)):
        c = confs[k]; acc = 0.; dg = 0.
        for p in range(npair):
            m = pm[p]; cm = c & m
            if cm != 0 and cm != m:
                dg -= pJ[p]; acc += 2. * pJ[p] * x[_rank(c ^ m, offset, idxlo, h, lomask, flip, top, full)]
            else:
                dg += pJ[p]
        for q in range(nf):
            for t in range(4):
                b[t] = (c >> fs[q, t]) & 1; z[t] = 1. - 2. * b[t]
            dg += (fw[q, 0] + fw[q, 1] + fw[q, 2]) * z[0] * z[1] * z[2] * z[3]
            for pi in range(3):
                u = PA[pi, 0]; v = PA[pi, 1]; xx = PA[pi, 2]; yy = PA[pi, 3]; w = fw[q, pi]
                muv = (1 << fs[q, u]) | (1 << fs[q, v]); mxy = (1 << fs[q, xx]) | (1 << fs[q, yy])
                d1 = b[u] != b[v]; d2 = b[xx] != b[yy]
                if d1: acc += 2. * w * z[xx] * z[yy] * x[_rank(c ^ muv, offset, idxlo, h, lomask, flip, top, full)]
                if d2: acc += 2. * w * z[u] * z[v] * x[_rank(c ^ mxy, offset, idxlo, h, lomask, flip, top, full)]
                if d1 and d2: acc += 4. * w * x[_rank(c ^ muv ^ mxy, offset, idxlo, h, lomask, flip, top, full)]
        y[k] = acc + dg * x[k]


class GenHam:
    def __init__(self, pairs, fours, N):
        self.N = N; pk = sorted(pairs); self.pairs = pairs; self.fours = fours
        self.pm = np.array([(1 << i) | (1 << j) for i, j in pk], np.int64).reshape(-1)
        self.pJ = np.array([pairs[p] for p in pk], float).reshape(-1)
        fk = sorted(fours)
        self.fs = np.array(fk, np.int64).reshape(-1, 4); self.fw = np.array([fours[q] for q in fk], float).reshape(-1, 3)


def make_mv_gen(H, S):
    def mv(x):
        x = np.ascontiguousarray(np.asarray(x, dtype=np.float64).ravel()); y = np.empty_like(x)
        _matvec_gen(x, y, S.confs, S.offset, S.idxlo, S.h, S.lomask, S.flip, S.top, S.full, H.pm, H.pJ, H.fs, H.fw)
        return y
    return mv


def dense_matrix(mv, D):
    M = np.zeros((D, D))
    for k in range(D):
        e = np.zeros(D); e[k] = 1.; M[:, k] = mv(e)
    return M
