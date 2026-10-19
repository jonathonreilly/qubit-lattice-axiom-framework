"""B13: sign-free projector stochastic-series-expansion QMC for the supplied spin-1/2 ring model.

Model (supplied, same conventions as B6 ringlib.py and the ring-model notes):
  sigma_l = +-1 on positive-coordinate links of an Lx x Ly x Lz periodic cubic torus, exact Gauss law;
  H = V N_f - J sum_{flippable p} |flip_p><.|, J = 1.  Off-diagonal elements are all -J <= 0 (stoquastic).
Algorithm: projector SSE  Z = <psi_T| T^m |psi_T>,  T = Lambda - H = sum_p [w_d(p) + flip_p],
  w_d(p, s) = Cd - V F_p(s) > 0, Lambda = N_p Cd, psi_T = uniform on the flip component (exact RK state).
  Moves: diagonal re-plaquetting; pair toggles of consecutive same-plaquette operators with only neighbour
  diagonal operators in between; boundary toggles of the first/last operator on a plaquette (open ends).
  Open ends make every path reducible to the empty one, so the chain is ergodic on the flip component and,
  unlike periodic (finite-T) local SSE, the magnetic "flux winding" M is not frozen.
Magnetic (source) curvature estimator: for a plaquette source vector c (unit norm), with
  M_c(window) = sum over flip operators in the window of c_p * circ_sign(state before op),
  <M_c(d)^2> = A + chi_c d / (Lambda - E0)  for long windows of d operators, where chi_c = d^2 E0/db^2 along c
  (generating-function argument: T(i eta) has Perron eigenvalue Lambda - E0 + chi eta^2/2).
Exploratory worker code; no claim.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import itertools
import numpy as np
import numba as nb

ORI = [(0, 1), (1, 2), (2, 0)]


class Lattice:
    """Same link/plaquette ordering as B6 ringlib.Torus (asserted in the validation runner)."""

    def __init__(self, dims):
        self.dims = tuple(dims)
        Lx, Ly, Lz = self.dims
        self.verts = list(itertools.product(range(Lx), range(Ly), range(Lz)))
        self.vid = {v: k for k, v in enumerate(self.verts)}
        self.nv = len(self.verts)
        self.nl = 3 * self.nv
        self.axis = np.repeat(np.arange(3)[None, :], self.nv, 0).ravel()
        self.coord = np.repeat(np.array(self.verts), 3, axis=0)
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
        self.nw = (self.nl + 63) // 64
        self.pmaskw = np.zeros((self.np_, self.nw), np.uint64)
        for p in range(self.np_):
            for l in self.plaq[p]:
                self.pmaskw[p, l >> 6] ^= np.uint64(1) << np.uint64(l & 63)
        # neighbours: plaquettes sharing at least one link (excluding self)
        by_link = [[] for _ in range(self.nl)]
        for p in range(self.np_):
            for l in self.plaq[p]:
                by_link[l].append(p)
        nbr = [sorted(set(q for l in self.plaq[p] for q in by_link[l]) - {p}) for p in range(self.np_)]
        self.nbr_ptr = np.zeros(self.np_ + 1, np.int64)
        self.nbr_ptr[1:] = np.cumsum([len(x) for x in nbr])
        self.nbr_idx = np.array([q for x in nbr for q in x], np.int64)
        self.d1 = np.zeros((self.np_, self.nl))
        for p in range(self.np_):
            for l, s in zip(self.plaq[p], (1, 1, -1, -1)):
                self.d1[p, l] += s
        # Gauss incidence (out - in)
        self.div = np.zeros((self.nv, self.nl))
        for v in self.verts:
            for a in range(3):
                l = self.link(v, a)
                self.div[self.vid[v], l] += 1
                self.div[self.vid[self.add(v, a)], l] -= 1

    def add(self, v, a, s=1):
        w = list(v)
        w[a] = (w[a] + s) % self.dims[a]
        return tuple(w)

    def link(self, v, a):
        return 3 * self.vid[v] + a

    def words_of_sigma(self, sigma):
        w = np.zeros(self.nw, np.uint64)
        for l in range(self.nl):
            if sigma[l] > 0:
                w[l >> 6] |= np.uint64(1) << np.uint64(l & 63)
        return w

    def sigma_of_words(self, w):
        return np.array([1 if (int(w[l >> 6]) >> (l & 63)) & 1 else -1 for l in range(self.nl)], np.int64)

    def winding(self, sigma):
        return tuple(int(sigma[(self.axis == a) & (self.coord[:, a] == 0)].sum()) for a in range(3))

    def nflip(self, sigma):
        s = sigma[self.plaq] * np.array([1, 1, -1, -1])
        return int((np.abs(s.sum(1)) == 4).sum())

    # ---------------- source vectors --------------------------------------------------
    def fourier_dirs(self, q, o):
        ph = (self.proot * np.array(q)[None, :]).sum(1)
        out = []
        for f in (np.cos(ph), np.sin(ph)):
            v = np.where(self.pori == o, f, 0.0)
            v[np.abs(v) < 1e-12] = 0.0
            n = np.linalg.norm(v)
            if n > 1e-9:
                out.append(v / n)
        return out

    def coexact_dirs(self, q):
        B = np.array([v for o in range(3) for v in self.fourier_dirs(q, o)])
        M = B @ self.d1
        u, s, vt = np.linalg.svd(M)
        rank = int((s > 1e-9 * max(s.max(), 1e-300)).sum()) if s.size else 0
        N = u[:, rank:]
        return [B.T @ N[:, i] for i in range(N.shape[1])]


def loop_randomize(lat, sigma, nloops, rng, keep_winding=True):
    """Classical directed-loop moves on ice (Gauss law preserved); reject loops changing the winding."""
    sigma = sigma.copy()
    out_links = [[] for _ in range(lat.nv)]  # (link, head-if-+1, tail)
    for v in lat.verts:
        for a in range(3):
            l = lat.link(v, a)
            out_links[lat.vid[v]].append((l, lat.vid[lat.add(v, a)], +1))
            out_links[lat.vid[lat.add(v, a)]].append((l, lat.vid[v], -1))
    W0 = lat.winding(sigma)
    for _ in range(nloops):
        v0 = int(rng.integers(lat.nv))
        path_v, path_l, seen = [v0], [], {v0: 0}
        v = v0
        while True:
            outs = [(l, w) for (l, w, d) in out_links[v] if sigma[l] == d]  # field pointing out of v
            l, w = outs[int(rng.integers(len(outs)))]
            path_l.append(l)
            if w in seen:
                loop = path_l[seen[w]:]
                break
            seen[w] = len(path_v)
            path_v.append(w)
            v = w
        trial = sigma.copy()
        trial[loop] *= -1
        if (not keep_winding) or lat.winding(trial) == W0:
            sigma = trial
    return sigma


# ===================================================================================
@nb.njit(cache=True)
def _bit(S, k, l):
    return (S[k, l >> 6] >> np.uint64(l & 63)) & np.uint64(1)


@nb.njit(cache=True)
def _circ(S, k, plaq, q):
    b0 = _bit(S, k, plaq[q, 0]); b1 = _bit(S, k, plaq[q, 1])
    b2 = _bit(S, k, plaq[q, 2]); b3 = _bit(S, k, plaq[q, 3])
    if b0 == b1 and b2 == b3 and b0 != b2:
        return 1 if b0 == 1 else -1
    return 0


@nb.njit(cache=True)
def _circ_x(S, k, plaq, pmaskw, q, p):
    """circulation of q in state S[k] with plaquette p's links flipped."""
    bs = np.empty(4, np.uint64)
    for t in range(4):
        l = plaq[q, t]
        b = _bit(S, k, l)
        if (pmaskw[p, l >> 6] >> np.uint64(l & 63)) & np.uint64(1):
            b ^= np.uint64(1)
        bs[t] = b
    if bs[0] == bs[1] and bs[2] == bs[3] and bs[0] != bs[2]:
        return 1 if bs[0] == 1 else -1
    return 0


@nb.njit(cache=True)
def _flip_range(S, k0, k1, pmaskw, p):
    """flip p's links in S[k] for k0 <= k <= k1."""
    for k in range(k0, k1 + 1):
        for w in range(S.shape[1]):
            S[k, w] ^= pmaskw[p, w]


@nb.njit(cache=True)
def init_state(m, NP, s0):
    S = np.empty((m + 1, s0.shape[0]), np.uint64)
    for k in range(m + 1):
        S[k] = s0
    typ = np.zeros(m, np.int8)
    pq = np.random.randint(0, NP, m).astype(np.int64)
    return S, typ, pq


@nb.njit(cache=True)
def seed(s):
    np.random.seed(s)


@nb.njit(cache=True)
def sweep(S, typ, pq, plaq, pmaskw, nbr_ptr, nbr_idx, V, Cd, J):
    m = typ.shape[0]
    NP = plaq.shape[0]
    wfl = Cd - V  # diagonal weight of a flippable plaquette
    # ---- 1. diagonal update
    for k in range(m):
        if typ[k] == 0:
            q = pq[k]
            q2 = np.random.randint(NP)
            w_old = Cd - V * (1 if _circ(S, k, plaq, q) != 0 else 0)
            w_new = Cd - V * (1 if _circ(S, k, plaq, q2) != 0 else 0)
            if w_new >= w_old or np.random.random() * w_old < w_new:
                pq[k] = q2
    # ---- 2. relevant lists
    cnt = np.zeros(NP + 1, np.int64)
    for k in range(m):
        q = pq[k]
        cnt[q + 1] += 1
        for t in range(nbr_ptr[q], nbr_ptr[q + 1]):
            cnt[nbr_idx[t] + 1] += 1
    ptr = np.cumsum(cnt)
    fill = ptr[:-1].copy()
    rel = np.empty(ptr[-1], np.int64)
    for k in range(m):
        q = pq[k]
        rel[fill[q]] = k
        fill[q] += 1
        for t in range(nbr_ptr[q], nbr_ptr[q + 1]):
            r = nbr_idx[t]
            rel[fill[r]] = k
            fill[r] += 1
    # ---- 3. off-diagonal (pair and boundary) toggles
    nacc = 0
    order = np.random.permutation(NP)
    for ii in range(NP):
        p = order[ii]
        a0, a1 = ptr[p], ptr[p + 1]
        if a1 == a0:
            continue
        # left boundary
        nbw = 1.0
        blocked = False
        first = -1
        for t in range(a0, a1):
            k = rel[t]
            if pq[k] == p:
                first = t
                break
            if typ[k] == 1:
                blocked = True
                break
        if first >= 0 and not blocked:
            a = rel[first]
            c = _circ(S, a, plaq, p)
            if c != 0:
                ratio = (J / wfl) if typ[a] == 0 else (wfl / J)
                for t in range(a0, first):
                    k = rel[t]
                    q = pq[k]
                    wo = Cd - V * (1 if _circ(S, k, plaq, q) != 0 else 0)
                    wn = Cd - V * (1 if _circ_x(S, k, plaq, pmaskw, q, p) != 0 else 0)
                    ratio *= wn / wo
                if ratio >= 1.0 or np.random.random() < ratio:
                    typ[a] = 1 - typ[a]
                    _flip_range(S, 0, a, pmaskw, p)
                    nacc += 1
        # pairs
        prev = -1
        blocked = False
        for t in range(a0, a1):
            k = rel[t]
            if pq[k] == p:
                if prev >= 0 and not blocked:
                    a = rel[prev]
                    b = k
                    if _circ(S, a, plaq, p) != 0:
                        ratio = 1.0
                        ratio *= (J / wfl) if typ[a] == 0 else (wfl / J)
                        ratio *= (J / wfl) if typ[b] == 0 else (wfl / J)
                        for u in range(prev + 1, t):
                            kk = rel[u]
                            q = pq[kk]
                            wo = Cd - V * (1 if _circ(S, kk, plaq, q) != 0 else 0)
                            wn = Cd - V * (1 if _circ_x(S, kk, plaq, pmaskw, q, p) != 0 else 0)
                            ratio *= wn / wo
                        if ratio >= 1.0 or np.random.random() < ratio:
                            typ[a] = 1 - typ[a]
                            typ[b] = 1 - typ[b]
                            _flip_range(S, a + 1, b, pmaskw, p)
                            nacc += 1
                prev = t
                blocked = False
            elif typ[k] == 1:
                blocked = True
        # right boundary
        last = -1
        blocked = False
        for t in range(a1 - 1, a0 - 1, -1):
            k = rel[t]
            if pq[k] == p:
                last = t
                break
            if typ[k] == 1:
                blocked = True
                break
        if last >= 0 and not blocked:
            z = rel[last]
            if _circ(S, z, plaq, p) != 0:
                ratio = (J / wfl) if typ[z] == 0 else (wfl / J)
                for t in range(last + 1, a1):
                    k = rel[t]
                    q = pq[k]
                    wo = Cd - V * (1 if _circ(S, k, plaq, q) != 0 else 0)
                    wn = Cd - V * (1 if _circ_x(S, k, plaq, pmaskw, q, p) != 0 else 0)
                    ratio *= wn / wo
                if ratio >= 1.0 or np.random.random() < ratio:
                    typ[z] = 1 - typ[z]
                    _flip_range(S, z + 1, m, pmaskw, p)
                    nacc += 1
    return nacc


@nb.njit(cache=True)
def nflip_at(S, k, plaq):
    n = 0
    for q in range(plaq.shape[0]):
        if _circ(S, k, plaq, q) != 0:
            n += 1
    return n


@nb.njit(cache=True)
def cum_M(S, typ, pq, plaq, Csrc, grid):
    """cumulative source-weighted signed flip counts at grid positions (ops with k < grid[g])."""
    ns = Csrc.shape[0]
    out = np.zeros((grid.shape[0], ns))
    acc = np.zeros(ns)
    g = 0
    m = typ.shape[0]
    for k in range(m):
        while g < grid.shape[0] and grid[g] == k:
            out[g] = acc
            g += 1
        if typ[k] == 1:
            c = _circ(S, k, plaq, pq[k])
            for s in range(ns):
                acc[s] += Csrc[s, pq[k]] * c
    while g < grid.shape[0]:
        out[g] = acc
        g += 1
    return out


@nb.njit(cache=True)
def check_consistency(S, typ, pq, plaq, pmaskw):
    """every op valid: offdiag needs flippable p and S[k+1] = S[k]^p; diag needs S[k+1]=S[k]."""
    m = typ.shape[0]
    bad = 0
    for k in range(m):
        p = pq[k]
        for w in range(S.shape[1]):
            exp = S[k, w] ^ pmaskw[p, w] if typ[k] == 1 else S[k, w]
            if S[k + 1, w] != exp:
                bad += 1
        if typ[k] == 1 and _circ(S, k, plaq, p) == 0:
            bad += 1
    return bad


def run(lat, sigma0, V, m, nsweep, ntherm, Csrc, ngrid=64, central=(0.25, 0.75), seed_=1, Cd=None, J=1.0,
        meas_every=1, check_every=0):
    """Returns dict with mixed energy samples, middle N_f, and per-measurement cumulative M grids."""
    if Cd is None:
        Cd = max(V, 0.0) + 0.5
    seed(seed_)
    s0 = lat.words_of_sigma(sigma0)
    S, typ, pq = init_state(m, lat.np_, s0)
    lo, hi = int(central[0] * m), int(central[1] * m)
    grid = np.linspace(lo, hi, ngrid).astype(np.int64)
    Emix, Nmid, Ms, acc = [], [], [], []
    bad = 0
    for it in range(ntherm + nsweep):
        a = sweep(S, typ, pq, lat.plaq, lat.pmaskw, lat.nbr_ptr, lat.nbr_idx, float(V), float(Cd), float(J))
        if check_every and it % check_every == 0:
            bad += check_consistency(S, typ, pq, lat.plaq, lat.pmaskw)
        if it >= ntherm and (it - ntherm) % meas_every == 0:
            nfL = nflip_at(S, 0, lat.plaq)
            nfR = nflip_at(S, m, lat.plaq)
            Emix.append(0.5 * (V - J) * (nfL + nfR))
            Nmid.append(nflip_at(S, m // 2, lat.plaq))
            Ms.append(cum_M(S, typ, pq, lat.plaq, Csrc, grid))
            acc.append(a)
    return dict(Emix=np.array(Emix), Nmid=np.array(Nmid), Ms=np.array(Ms), grid=grid, Cd=Cd, Lambda=lat.np_ * Cd,
                m=m, bad=bad, acc=np.array(acc), noff=int(typ.sum()), Sfinal=S[m // 2].copy())


def binned(x, nb_=20):
    x = np.asarray(x, float)
    n = len(x) // nb_ * nb_
    b = x[:n].reshape(nb_, -1).mean(1)
    return b.mean(), b.std(ddof=1) / np.sqrt(nb_)


def chi_from_M(res, E0, lag_min_frac=0.3, nb_=20):
    """Slope of <(M(x+d)-M(x))^2> vs d (in operators) over lags d >= lag_min_frac * window, times (Lambda-E0).
    Returns per-source (chi, err) using binning over measurements (jackknife-free: slope per bin)."""
    Ms, grid = res["Ms"], res["grid"]
    G = len(grid)
    nmeas, _, ns = Ms.shape
    lags = np.arange(1, G)
    dk = (grid[1:] - grid[0])  # operator lag for index lag
    # per measurement, mean over x of squared increment for each lag
    sq = np.zeros((nmeas, len(lags), ns))
    for i, L in enumerate(lags):
        d = Ms[:, L:, :] - Ms[:, :-L, :]
        sq[:, i, :] = (d * d).mean(1)
    sel = lags >= int(lag_min_frac * (G - 1))
    x = dk[sel].astype(float)
    n = nmeas // nb_ * nb_
    bins = sq[:n].reshape(nb_, -1, len(lags), ns).mean(1)
    fac = res["Lambda"] - E0
    out = []
    for s in range(ns):
        slopes = [np.polyfit(x, bins[b, sel, s], 1)[0] * fac for b in range(nb_)]
        tot = np.polyfit(x, sq[:n, sel, s].mean(0), 1)[0] * fac
        out.append((tot, np.std(slopes, ddof=1) / np.sqrt(nb_)))
    return out, sq[:n].mean(0), dk
