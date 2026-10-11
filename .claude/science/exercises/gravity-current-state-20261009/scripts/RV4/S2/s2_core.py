"""S2 core (lane RV4).  Jacobian formula (V3 refereed, P1 integration by parts):
    E_vac(eps) = < J_eps(k) e_vac(k) >_BZ ,   mu = < e_vac J''(0) > = -< grad(e_vac) . v  div v >_BZ
RN-L1 normalisation: v = (1/2) hhat p(k).
  E   : hhat = diag(1,-1,0)      v = 1/2 (p_x, -p_y, 0)
  T2  : hhat = offdiag_xy (1,1)  v = 1/2 (p_y,  p_x, 0)
  tr  : hhat = identity          v = 1/2 p
Momentum symbols are cubic-covariant trig polynomials, built from terms of p_x:
  d=2: t=(n,m):    p_x = sin(n kx) cos(m ky)                        p_y(kx,ky) = p_x(ky,kx)
  d=3: t=(n,m,l):  p_x = 1/2[sin(n kx)cos(m ky)cos(l kz) + (m<->l)]  p_y, p_z by cyclic relabelling
p = sum_t a_t p^(t);  slope condition p_x ~ kx  <=>  sum_t a_t n_t = 1.
With e_vac fixed, mu is a quadratic form in a:  mu = a^T Q a.
"""
import numpy as np

def terms(d, r):
    if d == 2:
        return [(n, m) for n in range(1, r+1) for m in range(0, r+1)]
    return [(n, m, l) for n in range(1, r+1) for m in range(0, r+1) for l in range(m, r+1)]

def _px_and_grad(t, K):
    """p_x^(t) and its gradient (d/dkx, d/dky[, d/dkz]) at K = (kx, ky[, kz]) arrays."""
    if len(t) == 2:
        n, m = t; kx, ky = K
        s, c = np.sin(n*kx), np.cos(n*kx); cm, sm = np.cos(m*ky), np.sin(m*ky)
        return s*cm, (n*c*cm, -m*s*sm)
    n, m, l = t; kx, ky, kz = K
    s, c = np.sin(n*kx), np.cos(n*kx)
    def one(m, l):
        cy, sy, cz, sz = np.cos(m*ky), np.sin(m*ky), np.cos(l*kz), np.sin(l*kz)
        return s*cy*cz, (n*c*cy*cz, -m*s*sy*cz, -l*s*cy*sz)
    a, ga = one(m, l); b, gb = one(l, m)
    return 0.5*(a+b), tuple(0.5*(x+y) for x, y in zip(ga, gb))

def p_and_dp(t, K):
    """full vector p^(t)_i and matrix dp[i][j] = d p_i / d k_j (cubic covariant extension)."""
    d = len(K)
    P = [None]*d; D = [[None]*d for _ in range(d)]
    for i in range(d):
        perm = [i] + [j for j in range(d) if j != i]          # (i, others) ; for d=3 others in increasing order
        Kp = tuple(K[j] for j in perm)
        val, g = _px_and_grad(t, Kp)
        P[i] = val
        for a, j in enumerate(perm):
            D[i][j] = g[a]
    return P, D

def channel_fields(P, D, G, ch):
    """returns (grad e . v, div v) for channel ch, given p, dp, grad e."""
    if ch == 'E':
        return 0.5*(G[0]*P[0] - G[1]*P[1]), 0.5*(D[0][0] - D[1][1])
    if ch == 'T2':
        return 0.5*(G[0]*P[1] + G[1]*P[0]), 0.5*(D[1][0] + D[0][1])
    if ch == 'tr':
        d = len(P)
        return 0.5*sum(G[i]*P[i] for i in range(d)), 0.5*sum(D[i][i] for i in range(d))
    raise ValueError

def grid(d, L, sl=None):
    k = 2*np.pi*(np.arange(L)+0.5)/L
    if d == 2:
        return np.meshgrid(k, k, indexing='ij')
    if sl is None:
        return np.meshgrid(k, k, k, indexing='ij')
    return np.meshgrid(k, k, k[sl], indexing='ij')

def kg_vac(K, M):
    """KG nearest neighbour: e_vac = omega/2, omega^2 = M^2 + sum 4 sin^2(k/2); returns e, grad e."""
    A = sum(4*np.sin(k/2)**2 for k in K)
    w = np.sqrt(M*M + A)
    return 0.5*w, [0.5*np.sin(k)/w for k in K]   # d(omega/2)/dk = sin k /(2 omega)

def quad_forms(d, L, tlist, vac, chans=('E', 'T2', 'tr'), nchunk=None):
    """Q[ch] (T x T) with mu_ch = a^T Q a, for vacuum function vac(K) -> (e, grad e)."""
    T = len(tlist)
    Q = {ch: np.zeros((T, T)) for ch in chans}
    N = L**d
    if d == 2:
        chunks = [None]
    else:
        nchunk = nchunk or max(1, L//8)
        idx = np.array_split(np.arange(L), nchunk)
        chunks = idx
    for sl in chunks:
        K = grid(d, L, sl)
        e, G = vac(K)
        A = {ch: [] for ch in chans}; B = {ch: [] for ch in chans}
        for t in tlist:
            P, D = p_and_dp(t, K)
            for ch in chans:
                a, b = channel_fields(P, D, G, ch)
                A[ch].append(a.ravel()); B[ch].append(b.ravel())
        for ch in chans:
            Am = np.array(A[ch]); Bm = np.array(B[ch])
            X = Am @ Bm.T
            Q[ch] += -(X + X.T)/2/N
    return Q

def slope_vec(tlist):
    return np.array([t[0] for t in tlist], float)
