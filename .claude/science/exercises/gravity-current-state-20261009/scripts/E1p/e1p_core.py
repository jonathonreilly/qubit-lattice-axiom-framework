"""E1' core numerics: Poisson sprinklings of M^{1,3} (and M^{1,1}), link matrices, Johnston path sums.

Units: rho = 1 (ell = rho^{-1/4} = 1 in 4D; ell = rho^{-1/2} = 1 in 2D).
4D Johnston (arXiv:0909.0944 eq.17): K_R = a L (I - a b L)^{-1}, a = sqrt(rho)/(2 pi sqrt 6), b = -m^2/rho.
2D Johnston (eq.16):                 K_R = a C (I - a b C)^{-1}, a = 1/2,                b = -m^2/rho.
Field from a source: phi(x) = (1/rho) sum_y K(x,y) J(y)  (so that phi -> int G_R J d^dy).
Recursions used (exact identities K = aL + ab L K):
  K(x,y)  = a L(x,y) + a b sum_{z <. x} K(z,y)
  (KJ)(x) = (a/rho) sum_{z <. x} J(z) + a b sum_{z <. x} (KJ)(z)
"""
import numpy as np
from numba import njit, prange
from math import pi, sqrt

A4 = 1.0 / (2.0 * pi * sqrt(6.0))   # a at rho = 1


# ------------------------------------------------------------------ 4D diamond sprinkling
def sprinkle4d_diamond(T, rng, rho=1.0):
    """Poisson sprinkling of the causal diamond with bottom tip (0,0,0,0) and top tip (T,0,0,0).
    Returns points sorted by time WITH the two tips added: index 0 = bottom tip, index -1 = top tip."""
    vol = pi / 24.0 * T**4
    N = rng.poisson(rho * vol)
    out = []
    got = 0
    while got < N:
        m = int((N - got) * 1.7) + 100
        t = rng.uniform(0, T, m)
        xyz = rng.uniform(-T / 2, T / 2, (m, 3))
        r = np.sqrt((xyz**2).sum(1))
        ok = r < np.minimum(t, T - t)
        c = np.column_stack([t[ok], xyz[ok]])
        out.append(c)
        got += c.shape[0]
    P = np.vstack(out)[:N] if N > 0 else np.empty((0, 4))
    P = P[np.argsort(P[:, 0])]
    P = np.vstack([np.zeros((1, 4)), P, np.array([[T, 0, 0, 0]])])
    return P


@njit(cache=True)
def _prec(P, i, j):
    """True iff P[i] strictly precedes P[j] (timelike past)."""
    dt = P[j, 0] - P[i, 0]
    if dt <= 0.0:
        return False
    dx = P[j, 1] - P[i, 1]; dy = P[j, 2] - P[i, 2]; dz = P[j, 3] - P[i, 3]
    return dt * dt > dx * dx + dy * dy + dz * dz


@njit(cache=True)
def _maximal_past(P, x, buf_past, buf_max):
    """Past links of element x = maximal elements of {z : z < x}. P time-sorted.
    Fills buf_max[:k] with link indices (descending time). Returns k."""
    npast = 0
    for j in range(x - 1, -1, -1):  # descending time
        if _prec(P, j, x):
            buf_past[npast] = j
            npast += 1
    k = 0
    for q in range(npast):
        z = buf_past[q]
        dominated = False
        for r in range(k - 1, -1, -1):  # most recent (earliest-time) maximal first
            if _prec(P, z, buf_max[r]):
                dominated = True
                break
        if not dominated:
            buf_max[k] = z
            k += 1
    return k


@njit(parallel=True, cache=True)
def _count_links(P):
    N = P.shape[0]
    cnt = np.zeros(N, np.int64)
    for x in prange(N):
        bp = np.empty(x + 1, np.int64)
        bm = np.empty(x + 1, np.int64)
        cnt[x] = _maximal_past(P, x, bp, bm)
    return cnt


@njit(parallel=True, cache=True)
def _fill_links(P, indptr, indices):
    N = P.shape[0]
    for x in prange(N):
        bp = np.empty(x + 1, np.int64)
        bm = np.empty(x + 1, np.int64)
        k = _maximal_past(P, x, bp, bm)
        s0 = indptr[x]
        for q in range(k):
            indices[s0 + q] = bm[q]


def past_links(P):
    """CSR of past links for every element of a time-sorted point set."""
    cnt = _count_links(P)
    indptr = np.zeros(P.shape[0] + 1, np.int64)
    indptr[1:] = np.cumsum(cnt)
    indices = np.empty(indptr[-1], np.int64)
    _fill_links(P, indptr, indices)
    return indptr, indices


@njit(cache=True)
def path_sums(indptr, indices, src, J, avec, bvec):
    """For each (a,b) pair k: point-to-point column K[:,k] = K(., src) and smeared KJ[:,k] = (KJ)(.).
    Elements must be time-sorted (links point to lower indices)."""
    N = indptr.shape[0] - 1
    nk = avec.shape[0]
    K = np.zeros((N, nk))
    KJ = np.zeros((N, nk))
    for x in range(N):
        sJ = 0.0
        isl = 0.0
        sK = np.zeros(nk)
        sKJ = np.zeros(nk)
        for p in range(indptr[x], indptr[x + 1]):
            z = indices[p]
            if z == src:
                isl = 1.0
            sJ += J[z]
            for k in range(nk):
                sK[k] += K[z, k]
                sKJ[k] += KJ[z, k]
        for k in range(nk):
            K[x, k] = avec[k] * isl + avec[k] * bvec[k] * sK[k]
            KJ[x, k] = avec[k] * sJ + avec[k] * bvec[k] * sKJ[k]
    return K, KJ


@njit(cache=True)
def two_link_count(indptr, indices, x, y):
    """L^2(x,y) = #{z : y <. z <. x}."""
    c = 0
    for p in range(indptr[x], indptr[x + 1]):
        z = indices[p]
        for q in range(indptr[z], indptr[z + 1]):
            if indices[q] == y:
                c += 1
                break
    return c


# ------------------------------------------------------------------ 2D (Johnston causal-matrix form)
def sprinkle2d_diamond(U, rng, rho=1.0):
    """Light-cone coords u=(t+x)/sqrt2, v=(t-x)/sqrt2 in [0,U]^2 (dt dx = du dv). Bottom tip (0,0), top (U,U)."""
    N = rng.poisson(rho * U * U)
    u = rng.uniform(0, U, N); v = rng.uniform(0, U, N)
    return u, v


@njit(cache=True)
def chain_sums_2d(u, v, U, J, avec, bvec):
    """2D Johnston K = a C (I - a b C)^{-1}, source = bottom tip (0,0) [precedes every element],
    evaluated at the top tip (U,U), plus smeared (KJ)(top) with J on elements.
    K(x,0)  = a + a b sum_{z<x} K(z,0);   (KJ)(x) = a sum_{z<x} J(z) + a b sum_{z<x} (KJ)(z).
    BIT over v-ranks, elements processed in increasing u. Returns K_top[nk], KJ_top[nk]."""
    N = u.shape[0]
    nk = avec.shape[0]
    order = np.argsort(u)
    vrank = np.argsort(np.argsort(v)) + 1
    treeK = np.zeros((N + 1, nk)); treeKJ = np.zeros((N + 1, nk)); treeJ = np.zeros(N + 1)
    for idx in range(N):
        j = order[idx]
        r = vrank[j]
        sK = np.zeros(nk); sKJ = np.zeros(nk); sJ = 0.0
        i = r - 1
        while i > 0:
            for k in range(nk):
                sK[k] += treeK[i, k]; sKJ[k] += treeKJ[i, k]
            sJ += treeJ[i]
            i -= i & (-i)
        Kz = np.empty(nk); KJz = np.empty(nk)
        for k in range(nk):
            Kz[k] = avec[k] + avec[k] * bvec[k] * sK[k]
            KJz[k] = avec[k] * sJ + avec[k] * bvec[k] * sKJ[k]
        i = r
        while i <= N:
            for k in range(nk):
                treeK[i, k] += Kz[k]; treeKJ[i, k] += KJz[k]
            treeJ[i] += J[j]
            i += i & (-i)
    # top tip: all elements precede it
    sK = np.zeros(nk); sKJ = np.zeros(nk); sJ = 0.0
    i = N
    while i > 0:
        for k in range(nk):
            sK[k] += treeK[i, k]; sKJ[k] += treeKJ[i, k]
        sJ += treeJ[i]
        i -= i & (-i)
    Ktop = np.empty(nk); KJtop = np.empty(nk)
    for k in range(nk):
        Ktop[k] = avec[k] + avec[k] * bvec[k] * sK[k]
        KJtop[k] = avec[k] * sJ + avec[k] * bvec[k] * sKJ[k]
    return Ktop, KJtop
