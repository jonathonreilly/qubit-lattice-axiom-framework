"""B6 helper library: exact (sparse) diagonalisation of the supplied spin-1/2 ring model
on small periodic Lx x Ly x Lz tori, in the sigma=+-1 link language of the ring-model notes.

Supplied model (not a framework premise):
  link fields sigma_l = +-1 on positive-coordinate links, exact vertex Gauss law div sigma = 0
  (3 in / 3 out); H = V N_f - J sum_{flippable p} |flip_p><.|, J = 1.
  Plaquette source (SPIN_HALF_CARTESIAN_PLAQUETTE_SOURCE_NOTE_2026-09-07, uniform Cartesian
  convention): H_{n, n^p}(b) = -J exp(i c_p(n) b_p) with c_p(n) = C_p(n)/4 = +-1 the circulation
  sign of the flippable plaquette.  On even tori this equals eps(r) s_p(n) of the note
  (sigma_i(r) = eps(r)(2 n_i(r) - 1)); on tori with an odd extent only the sigma form is used.
Plaquettes: orientation o = 0,1,2 <-> (i,j) = (0,1),(1,2),(2,0) (normals z, x, y), links
  [(r,i), (r+i,j), (r+j,i), (r,j)] with signs (+,+,-,-), exactly as in the probe.
Exploratory worker code; no claim.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import itertools
import numpy as np
import numba as nb
import scipy.sparse as sp
import scipy.sparse.linalg as sla

ORI = [(0, 1), (1, 2), (2, 0)]


class Torus:
    def __init__(self, dims):
        self.dims = tuple(dims)
        Lx, Ly, Lz = self.dims
        self.verts = list(itertools.product(range(Lx), range(Ly), range(Lz)))
        self.vid = {v: k for k, v in enumerate(self.verts)}
        self.nv = len(self.verts)
        self.nl = 3 * self.nv
        self.tail = np.zeros(self.nl, np.int64)
        self.head = np.zeros(self.nl, np.int64)
        self.axis = np.zeros(self.nl, np.int64)
        self.coord = np.zeros((self.nl, 3), np.int64)
        for v in self.verts:
            for a in range(3):
                l = 3 * self.vid[v] + a
                self.tail[l] = self.vid[v]
                self.head[l] = self.vid[self.add(v, a)]
                self.axis[l] = a
                self.coord[l] = v
        plaq, proot, pori = [], [], []
        for v in self.verts:
            for o, (i, j) in enumerate(ORI):
                plaq.append([self.link(v, i), self.link(self.add(v, i), j), self.link(self.add(v, j), i), self.link(v, j)])
                proot.append(v)
                pori.append(o)
        self.plaq = np.array(plaq, np.int64)
        self.proot = np.array(proot, np.int64)
        self.pori = np.array(pori, np.int64)
        self.np_ = len(plaq)
        self.pmask = np.array([sum(1 << int(l) for l in ls) for ls in plaq], np.int64)
        # winding planes: links of axis a with coord_a == 0
        self.wmask = np.array([sum(1 << int(l) for l in np.flatnonzero((self.axis == a) & (self.coord[:, a] == 0)))
                               for a in range(3)], np.int64)
        self.wsize = np.array([int(((self.axis == a) & (self.coord[:, a] == 0)).sum()) for a in range(3)], np.int64)
        # incidence d0^T style: d1 (links -> plaquettes)
        self.d1 = np.zeros((self.np_, self.nl))
        for p, ls in enumerate(plaq):
            for l, s in zip(ls, (1, 1, -1, -1)):
                self.d1[p, l] += s

    def add(self, v, a, s=1):
        w = list(v)
        w[a] = (w[a] + s) % self.dims[a]
        return tuple(w)

    def link(self, v, a):
        return 3 * self.vid[v] + a

    def code_of(self, sigma):
        return int(sum(1 << l for l in range(self.nl) if sigma[l] > 0))

    def sigma_of(self, code):
        return np.array([1 if (code >> l) & 1 else -1 for l in range(self.nl)], np.int64)


@nb.njit(cache=True)
def _popc(x):
    n = 0
    while x:
        x &= x - 1
        n += 1
    return n


@nb.njit(cache=True)
def dfs_count_sectors(nl, nv, tail, head, rem0, wmask, wsize, maxw):
    """Exhaustive DFS over all Gauss states (div sigma = 0). Returns histogram over windings
    W_a = 2 popcount(code & wmask_a) - wsize_a, indexed by (W_a + maxw)//2."""
    nb_ = maxw + 1
    hist = np.zeros((nb_, nb_, nb_), np.int64)
    bal = np.zeros(nv, np.int64)
    rem = rem0.copy()
    choice = np.zeros(nl + 1, np.int64)
    code = np.int64(0)
    i = 0
    while i >= 0:
        if i == nl:
            w0 = 2 * _popc(code & wmask[0]) - wsize[0]
            w1 = 2 * _popc(code & wmask[1]) - wsize[1]
            w2 = 2 * _popc(code & wmask[2]) - wsize[2]
            hist[(w0 + maxw) // 2, (w1 + maxw) // 2, (w2 + maxw) // 2] += 1
            i -= 1
            continue
        t, h = tail[i], head[i]
        if choice[i] > 0:
            s = 1 if choice[i] == 1 else -1
            bal[t] -= s
            bal[h] += s
            rem[t] += 1
            rem[h] += 1
            if s == 1:
                code &= ~(np.int64(1) << i)
        if choice[i] == 2:
            choice[i] = 0
            i -= 1
            continue
        choice[i] += 1
        s = 1 if choice[i] == 1 else -1
        bal[t] += s
        bal[h] -= s
        rem[t] -= 1
        rem[h] -= 1
        if s == 1:
            code |= (np.int64(1) << i)
        if abs(bal[t]) <= rem[t] and abs(bal[h]) <= rem[h]:
            i += 1
            choice[i] = 0
    return hist


@nb.njit(cache=True)
def dfs_sector(nl, nv, tail, head, rem0, wmask, wneed, maxn):
    """All Gauss states with popcount(code & wmask_a) == wneed_a (a = 0,1,2)."""
    out = np.empty(maxn, np.int64)
    cnt = 0
    bal = np.zeros(nv, np.int64)
    rem = rem0.copy()
    choice = np.zeros(nl + 1, np.int64)
    code = np.int64(0)
    i = 0
    while i >= 0:
        if i == nl:
            if _popc(code & wmask[0]) == wneed[0] and _popc(code & wmask[1]) == wneed[1] and _popc(code & wmask[2]) == wneed[2]:
                if cnt < maxn:
                    out[cnt] = code
                cnt += 1
            i -= 1
            continue
        t, h = tail[i], head[i]
        if choice[i] > 0:
            s = 1 if choice[i] == 1 else -1
            bal[t] -= s
            bal[h] += s
            rem[t] += 1
            rem[h] += 1
            if s == 1:
                code &= ~(np.int64(1) << i)
        if choice[i] == 2:
            choice[i] = 0
            i -= 1
            continue
        choice[i] += 1
        s = 1 if choice[i] == 1 else -1
        bal[t] += s
        bal[h] -= s
        rem[t] -= 1
        rem[h] -= 1
        if s == 1:
            code |= (np.int64(1) << i)
        if abs(bal[t]) <= rem[t] and abs(bal[h]) <= rem[h]:
            i += 1
            choice[i] = 0
    return out[:min(cnt, maxn)], cnt


@nb.njit(cache=True)
def _circ(c, plaq, p):
    C = 0
    for k in range(4):
        sg = 2 * ((c >> plaq[p, k]) & 1) - 1
        C += sg if k < 2 else -sg
    return C


@nb.njit(cache=True)
def _bsearch(codes, x):
    lo, hi = 0, codes.shape[0] - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if codes[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo if codes[lo] == x else -1


@nb.njit(cache=True)
def count_moves(codes, plaq):
    n = codes.shape[0]
    nf = np.zeros(n, np.int64)
    for i in range(n):
        for p in range(plaq.shape[0]):
            C = _circ(codes[i], plaq, p)
            if C == 4 or C == -4:
                nf[i] += 1
    return nf


@nb.njit(cache=True)
def build_moves(codes, plaq, pmask, nf):
    """Directed moves: row i, col j (flipped state), plaquette p, circulation sign c of row state."""
    n = codes.shape[0]
    tot = nf.sum()
    rows = np.empty(tot, np.int64)
    cols = np.empty(tot, np.int64)
    ps = np.empty(tot, np.int64)
    cs = np.empty(tot, np.int64)
    k = 0
    bad = 0
    for i in range(n):
        for p in range(plaq.shape[0]):
            C = _circ(codes[i], plaq, p)
            if C == 4 or C == -4:
                j = _bsearch(codes, codes[i] ^ pmask[p])
                if j < 0:
                    bad += 1
                rows[k] = i
                cols[k] = j
                ps[k] = p
                cs[k] = 1 if C == 4 else -1
                k += 1
    return rows, cols, ps, cs, bad


@nb.njit(cache=True)
def _find(par, x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x


@nb.njit(cache=True)
def union_components(n, rows, cols):
    par = np.arange(n)
    for k in range(rows.shape[0]):
        a, b = _find(par, rows[k]), _find(par, cols[k])
        if a != b:
            par[a] = b
    for i in range(n):
        par[i] = _find(par, i)
    return par


class Component:
    """One flip component (sorted codes) with its move list."""

    def __init__(self, T, codes):
        self.T = T
        self.codes = np.sort(np.asarray(codes, np.int64))
        self.n = len(self.codes)
        self.nf = count_moves(self.codes, T.plaq)
        r, c, p, s, bad = build_moves(self.codes, T.plaq, T.pmask, self.nf)
        assert bad == 0, "flip left the supplied state set"
        self.rows, self.cols, self.ps, self.cs = r, c, p, s
        self.A = sp.csr_matrix((np.ones(len(r)), (r, c)), shape=(self.n, self.n))

    def H(self, V, J=1.0):
        return (sp.diags(V * self.nf.astype(float)) - J * self.A).tocsr()

    def ground(self, V, J=1.0, tol=1e-13):
        if self.n == 1:
            return float(V * self.nf[0]), np.ones(1), np.inf
        if self.n <= 800:
            w, U = np.linalg.eigh(self.H(V, J).toarray())
            g = U[:, 0]
            return float(w[0]), g * np.sign(g.sum()), float(w[1] - w[0])
        H = self.H(V, J)
        w, U = sla.eigsh(H, k=2, which="SA", tol=tol, v0=np.random.default_rng(1).random(self.n) + 0.5, ncv=40, maxiter=20000)
        o = np.argsort(w)
        g = U[:, o[0]]
        return float(w[o[0]]), g * np.sign(g.sum()), float(w[o[1]] - w[o[0]])

    # ---------------- source response -------------------------------------------------
    def w_vecs(self, g, C):
        """C: (k, NP) real source directions. w[:, m] = sum_moves C[m,p] c sign g_col (row index)."""
        k = C.shape[0]
        W = np.zeros((self.n, k))
        gc = g[self.cols] * self.cs
        for m in range(k):
            W[:, m] = np.bincount(self.rows, weights=C[m][self.ps] * gc, minlength=self.n)
        return W

    def direct(self, g, C):
        """J sum_moves C_p C'_p g_row g_col  (k x k), via per-plaquette sums."""
        gg = g[self.rows] * g[self.cols]
        perp = np.bincount(self.ps, weights=gg, minlength=self.T.np_)
        return (C * perp[None, :]) @ C.T

    def block_cg(self, H, E0, g, Bm, tol=1e-11, maxit=20000):
        """Solve (H - E0) X = Bm on the complement of g; independent CG per column, frozen when converged."""
        Bm = Bm - np.outer(g, g @ Bm)
        k = Bm.shape[1]
        X = np.zeros_like(Bm)
        bn = np.sqrt((Bm * Bm).sum(0))
        scale = max(bn.max(), 1e-300)
        act = np.flatnonzero(bn > 1e-14 * scale)
        R = Bm[:, act].copy()
        P = R.copy()
        rs = (R * R).sum(0)
        it = 0
        while len(act) and it < maxit:
            it += 1
            AP = H @ P - E0 * P
            AP -= np.outer(g, g @ AP)
            alpha = rs / (P * AP).sum(0)
            X[:, act] += P * alpha
            R -= AP * alpha
            rs_new = (R * R).sum(0)
            if it % 50 == 0:  # residual replacement against drift
                R = Bm[:, act] - (H @ X[:, act] - E0 * X[:, act])
                R -= np.outer(g, g @ R)
                rs_new = (R * R).sum(0)
            done = np.sqrt(rs_new) <= tol * bn[act]
            beta = rs_new / rs
            P = R + P * beta
            rs = rs_new
            if done.any():
                keep = ~done
                act, R, P, rs = act[keep], R[:, keep], P[:, keep], rs[keep]
        X -= np.outer(g, g @ X)
        res = np.abs(H @ X - E0 * X - Bm).max() / scale
        return X, it, res

    def hessian(self, V, C, J=1.0, ground=None):
        """R(c,c') = d^2 E0 / db db' along source directions (rows of C), J = 1."""
        E0, g, gap = ground if ground is not None else self.ground(V, J)
        H = self.H(V, J)
        W = self.w_vecs(g, C)
        k = C.shape[0]
        R = J * self.direct(g, C)
        its, res = 0, 0.0
        ch = 16
        for a in range(0, k, ch):
            X, it_, re_ = self.block_cg(H, E0, g, W[:, a:a + ch])
            R[:, a:a + ch] -= 2 * J * J * (W.T @ X)
            its, res = max(its, it_), max(res, re_)
            del X
        return 0.5 * (R + R.T), dict(E0=E0, gap=gap, cg_its=its, cg_res=res)

    def energy_with_source(self, V, b, J=1.0):
        """Lowest eigenvalue of the Hermitian sourced matrix H(b) (direct, for finite differences)."""
        ph = np.exp(1j * b[self.ps] * self.cs)
        Hb = sp.csr_matrix((-J * ph, (self.rows, self.cols)), shape=(self.n, self.n)) + sp.diags(V * self.nf.astype(float))
        if self.n <= 2500:
            return float(np.linalg.eigvalsh(Hb.toarray())[0])
        w = sla.eigsh(Hb, k=1, which="SA", tol=1e-14, v0=(np.random.default_rng(2).random(self.n) + 0.5).astype(complex), ncv=40, maxiter=20000)[0]
        return float(w.min())


def fourier_dirs(T, q, o):
    """Real unit source vectors on orientation o: cos(q.r) and (if nonzero) sin(q.r), r = plaquette root."""
    ph = (T.proot * np.array(q)[None, :]).sum(1)
    out = []
    for f in (np.cos(ph), np.sin(ph)):
        v = np.where(T.pori == o, f, 0.0)
        v[np.abs(v) < 1e-12] = 0.0
        nrm = np.linalg.norm(v)
        if nrm > 1e-9:
            out.append(v / nrm)
    return out


def sector_states(T, W, maxn=60_000_000):
    rem0 = np.full(T.nv, 6, np.int64)
    wneed = (T.wsize + np.array(W)) // 2
    codes, cnt = dfs_sector(T.nl, T.nv, T.tail, T.head, rem0, T.wmask, wneed.astype(np.int64), maxn)
    assert cnt <= maxn
    return np.sort(codes)


def split_components(T, codes):
    nf = count_moves(codes, T.plaq)
    r, c, p, s, bad = build_moves(codes, T.plaq, T.pmask, nf)
    assert bad == 0
    par = union_components(len(codes), r, c)
    roots, inv, sizes = np.unique(par, return_inverse=True, return_counts=True)
    return inv, sizes, nf
