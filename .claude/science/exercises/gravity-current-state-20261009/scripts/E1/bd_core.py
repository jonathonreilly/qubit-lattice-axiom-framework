"""Core numerics for E1: Poisson sprinklings of 1+1 and 3+1 Minkowski diamonds and the
Benincasa-Dowker (smeared) d'Alembertian evaluated on them.

Units: rho_k = eps * rho = 1 (non-locality scale l_k = 1). eps = 1 is the local operator.
For a target x only past elements y with rho_k V(x,y) < SMAX are kept (the 'shell');
every z in the interval I(y,x) has V(x,z) <= V(x,y), so n(x,y) is computed exactly
inside the shell. Truncation error: |weights| ~ e^{-SMAX} SMAX^3 (SMAX=24: ~4e-7).
"""
import numpy as np
from numba import njit, prange
from math import pi, sqrt

SMAX = 24.0


@njit(cache=True)
def f2(n, e):
    if e >= 1.0:  # local layer weights 1,-2,1
        if n == 0: return 1.0
        if n == 1: return -2.0
        if n == 2: return 1.0
        return 0.0
    q = 1.0 - e
    return q**n * (1.0 - 2.0*e*n/q + e*e*n*(n-1)/(2.0*q*q))


@njit(cache=True)
def f4(n, e):
    if e >= 1.0:  # local layer weights 1,-9,16,-8
        if n == 0: return 1.0
        if n == 1: return -9.0
        if n == 2: return 16.0
        if n == 3: return -8.0
        return 0.0
    q = 1.0 - e
    return q**n * (1.0 - 9.0*e*n/q + 8.0*e*e*n*(n-1)/(q*q)
                   - (4.0/3.0)*e**3*n*(n-1)*(n-2)/(q**3))


# ------------------------------------------------------------------ 2D
def sprinkle2d(rho, U, rng):
    """Diamond u,v in [0,U] (u=(t+x)/sqrt2, v=(t-x)/sqrt2; dt dx = du dv)."""
    N = rng.poisson(rho * U * U)
    return rng.uniform(0, U, N), rng.uniform(0, U, N)


@njit(cache=True)
def _shell2d(u, v, ix, smax_over_rhok):
    ux, vx = u[ix], v[ix]
    idx = np.empty(u.shape[0], np.int64)
    m = 0
    for j in range(u.shape[0]):
        du = ux - u[j]; dv = vx - v[j]
        if du > 0 and dv > 0 and du*dv < smax_over_rhok:
            idx[m] = j; m += 1
    return idx[:m]


@njit(cache=True)
def _counts2d(us, vs):
    """n_j = #{k : us[k] > us[j] and vs[k] > vs[j]} via BIT (exact, O(M log M))."""
    M = us.shape[0]
    order = np.argsort(-us)
    vr = np.argsort(np.argsort(vs))  # rank 0..M-1
    tree = np.zeros(M + 1, np.int64)
    n = np.zeros(M, np.int64)
    inserted = 0
    for k in range(M):
        j = order[k]
        r = vr[j] + 1
        # count inserted with rank <= r
        s = 0; i = r
        while i > 0:
            s += tree[i]; i -= i & (-i)
        n[j] = inserted - s
        i = r
        while i <= M:
            tree[i] += 1; i += i & (-i)
        inserted += 1
    return n


@njit(parallel=True, cache=True)
def bd2d_targets(u, v, targets, eps, phis_y, phis_x):
    """For each target x returns:
       out[:,k] = eps*sum_y f2(n,eps) phi_k(y) - 1/2 phi_k(x)   (B phi / (4 rho_k))
       gain[:]  = eps^2 sum_y f2^2  (white-noise gain A^2)
       nsh[:]   = shell size.  phis_y: (K, N) test fields at all elements."""
    K = phis_y.shape[0]
    T = targets.shape[0]
    out = np.zeros((T, K)); gain = np.zeros(T); nsh = np.zeros(T, np.int64)
    smr = SMAX  # rho_k = 1
    for a in prange(T):
        ix = targets[a]
        idx = _shell2d(u, v, ix, smr)
        n = _counts2d(u[idx], v[idx])
        acc = np.zeros(K); g = 0.0
        for j in range(idx.shape[0]):
            w = f2(n[j], eps)
            g += w*w
            for k in range(K):
                acc[k] += w * phis_y[k, idx[j]]
        for k in range(K):
            out[a, k] = eps*acc[k] - 0.5*phis_x[k, a]
        gain[a] = eps*eps*g; nsh[a] = idx.shape[0]
    return out, gain, nsh


# ------------------------------------------------------------------ 4D
def sprinkle4d(rho, T, rng, center=None):
    """Causal diamond with bottom (0,0,0,0), top (T,0,0,0)."""
    vol = pi/24*T**4
    N = rng.poisson(rho*vol)
    pts = np.empty((0, 4))
    out = []
    got = 0
    while got < N:
        m = int((N - got)*1.6) + 100
        t = rng.uniform(0, T, m)
        xyz = rng.uniform(-T/2, T/2, (m, 3))
        r = np.sqrt((xyz**2).sum(1))
        ok = r < np.minimum(t, T - t)
        c = np.column_stack([t[ok], xyz[ok]])
        out.append(c); got += c.shape[0]
    P = np.vstack(out)[:N]
    P = P[np.argsort(P[:, 0])]
    return P


@njit(cache=True)
def _shell4d(P, ix, smax_over_rhok):
    tx, xx, yx, zx = P[ix, 0], P[ix, 1], P[ix, 2], P[ix, 3]
    c = 24.0/pi*smax_over_rhok
    idx = np.empty(ix, np.int64)
    m = 0
    for j in range(ix):  # P sorted by time; past candidates have j < ix
        dt = tx - P[j, 0]
        if dt <= 0: continue
        dx = xx - P[j, 1]; dy = yx - P[j, 2]; dz = zx - P[j, 3]
        tau2 = dt*dt - dx*dx - dy*dy - dz*dz
        if tau2 > 0 and tau2*tau2 < c:
            idx[m] = j; m += 1
    return idx[:m]


@njit(cache=True)
def _counts4d(Q):
    """Q sorted by time. n_j = #{k > j : Q[j] < Q[k] causally}. O(M^2)."""
    M = Q.shape[0]
    n = np.zeros(M, np.int64)
    for j in range(M):
        tj, xj, yj, zj = Q[j, 0], Q[j, 1], Q[j, 2], Q[j, 3]
        cnt = 0
        for k in range(j+1, M):
            dt = Q[k, 0] - tj
            if dt <= 0: continue
            dx = Q[k, 1] - xj; dy = Q[k, 2] - yj; dz = Q[k, 3] - zj
            if dt*dt > dx*dx + dy*dy + dz*dz:
                cnt += 1
        n[j] = cnt
    return n


@njit(parallel=True, cache=True)
def bd4d_targets(P, targets, eps, phis_y, phis_x):
    """out[:,k] = eps*sum_y f4 phi_k(y) - phi_k(x)  (= B phi / P, P = (4/sqrt6) rho_k^{1/2})."""
    K = phis_y.shape[0]
    T = targets.shape[0]
    out = np.zeros((T, K)); gain = np.zeros(T); nsh = np.zeros(T, np.int64)
    for a in prange(T):
        ix = targets[a]
        idx = _shell4d(P, ix, SMAX)
        Q = P[idx]
        n = _counts4d(Q)
        acc = np.zeros(K); g = 0.0
        for j in range(idx.shape[0]):
            w = f4(n[j], eps)
            g += w*w
            for k in range(K):
                acc[k] += w*phis_y[k, idx[j]]
        for k in range(K):
            out[a, k] = eps*acc[k] - phis_x[k, a]
        gain[a] = eps*eps*g; nsh[a] = idx.shape[0]
    return out, gain, nsh


# ------------------------------------------------------------------ 2D with cell index
def build_cells2d(u, v, U, h):
    nc = int(np.ceil(U/h)) + 1
    cu = np.minimum((u/h).astype(np.int64), nc-1); cv = np.minimum((v/h).astype(np.int64), nc-1)
    key = cu*nc + cv
    order = np.argsort(key, kind="stable")
    counts = np.bincount(key, minlength=nc*nc)
    start = np.zeros(nc*nc+1, np.int64); start[1:] = np.cumsum(counts)
    return order, start, nc


@njit(cache=True)
def _shell2d_cells(u, v, ix, smr, order, start, nc, h):
    ux, vx = u[ix], v[ix]
    cux = min(int(ux/h), nc-1); cvx = min(int(vx/h), nc-1)
    buf = np.empty(4096, np.int64); m = 0
    for iu in range(cux, -1, -1):
        du_min = ux - (iu+1)*h
        if du_min < 0: du_min = 0.0
        for iv in range(cvx, -1, -1):
            dv_min = vx - (iv+1)*h
            if dv_min < 0: dv_min = 0.0
            if du_min*dv_min >= smr:
                break
            c = iu*nc + iv
            for p in range(start[c], start[c+1]):
                j = order[p]
                du = ux - u[j]; dv = vx - v[j]
                if du > 0 and dv > 0 and du*dv < smr:
                    if m == buf.shape[0]:
                        nb = np.empty(2*m, np.int64); nb[:m] = buf; buf = nb
                    buf[m] = j; m += 1
    return buf[:m]


@njit(parallel=True, cache=True)
def bd2d_targets_c(u, v, targets, eps, phis_y, phis_x, order, start, nc, h):
    K = phis_y.shape[0]; T = targets.shape[0]
    out = np.zeros((T, K)); gain = np.zeros(T); nsh = np.zeros(T, np.int64)
    for a in prange(T):
        ix = targets[a]
        idx = _shell2d_cells(u, v, ix, SMAX, order, start, nc, h)
        n = _counts2d(u[idx], v[idx])
        acc = np.zeros(K); g = 0.0
        for j in range(idx.shape[0]):
            w = f2(n[j], eps); g += w*w
            for k in range(K):
                acc[k] += w*phis_y[k, idx[j]]
        for k in range(K):
            out[a, k] = eps*acc[k] - 0.5*phis_x[k, a]
        gain[a] = eps*eps*g; nsh[a] = idx.shape[0]
    return out, gain, nsh


def bd2d(u, v, U, targets, eps, phis_y, phis_x, h=0.5):
    order, start, nc = build_cells2d(u, v, U, h)
    return bd2d_targets_c(u, v, targets, eps, phis_y, phis_x, order, start, nc, h)


# ------------------------------------------------------------------ 4D CSR weights
@njit(parallel=True, cache=True)
def _shell_sizes4d(P, targets):
    T = targets.shape[0]
    sz = np.zeros(T, np.int64)
    for a in prange(T):
        sz[a] = _shell4d(P, targets[a], SMAX).shape[0]
    return sz


@njit(parallel=True, cache=True)
def _fill4d(P, targets, eps, indptr, indices, weights):
    T = targets.shape[0]
    for a in prange(T):
        idx = _shell4d(P, targets[a], SMAX)
        Q = P[idx]
        n = _counts4d(Q)
        s0 = indptr[a]
        for j in range(idx.shape[0]):
            indices[s0 + j] = idx[j]
            weights[s0 + j] = eps*f4(n[j], eps)


def bd4d_weights(P, targets, eps):
    """CSR rows: (eps * f4(n(x,y))) for y in the shell of each target x.
    B phi(x)/P_pref = sum_row w*phi(y) - phi(x)."""
    sz = _shell_sizes4d(P, targets)
    indptr = np.zeros(len(targets)+1, np.int64); indptr[1:] = np.cumsum(sz)
    indices = np.empty(indptr[-1], np.int64); weights = np.empty(indptr[-1])
    _fill4d(P, targets, eps, indptr, indices, weights)
    return indptr, indices, weights


@njit(cache=True)
def csr_apply(indptr, indices, weights, phi):
    T = indptr.shape[0]-1
    out = np.zeros(T)
    for a in range(T):
        s = 0.0
        for p in range(indptr[a], indptr[a+1]):
            s += weights[p]*phi[indices[p]]
        out[a] = s
    return out


@njit(cache=True)
def evolve(indptr, indices, weights, targets, phi0, is_init):
    """Retarded explicit evolution phi(x) = sum_y w(x,y) phi(y) for non-initial targets,
    processed in time order (targets sorted by time, P time-sorted).  phi0: initial values
    for all elements (used where is_init)."""
    phi = phi0.copy()
    for a in range(targets.shape[0]):
        x = targets[a]
        if is_init[x]:
            continue
        s = 0.0
        for p in range(indptr[a], indptr[a+1]):
            s += weights[p]*phi[indices[p]]
        phi[x] = s
    return phi


# ------------------------------------------------------------------ 2D CSR weights
@njit(parallel=True, cache=True)
def _shell_sizes2d(u, v, targets, order, start, nc, h):
    T = targets.shape[0]; sz = np.zeros(T, np.int64)
    for a in prange(T):
        sz[a] = _shell2d_cells(u, v, targets[a], SMAX, order, start, nc, h).shape[0]
    return sz


@njit(parallel=True, cache=True)
def _fill2d(u, v, targets, eps, indptr, indices, weights, order, start, nc, h):
    T = targets.shape[0]
    for a in prange(T):
        idx = _shell2d_cells(u, v, targets[a], SMAX, order, start, nc, h)
        n = _counts2d(u[idx], v[idx])
        s0 = indptr[a]
        for j in range(idx.shape[0]):
            indices[s0+j] = idx[j]; weights[s0+j] = eps*f2(n[j], eps)


def bd2d_weights(u, v, U, targets, eps, h=0.5):
    """CSR rows eps*f2(n). B phi/(4 rho_k) = sum_row w phi(y) - phi(x)/2."""
    order, start, nc = build_cells2d(u, v, U, h)
    sz = _shell_sizes2d(u, v, targets, order, start, nc, h)
    indptr = np.zeros(len(targets)+1, np.int64); indptr[1:] = np.cumsum(sz)
    indices = np.empty(indptr[-1], np.int64); weights = np.empty(indptr[-1])
    _fill2d(u, v, targets, eps, indptr, indices, weights, order, start, nc, h)
    return indptr, indices, weights
