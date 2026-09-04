"""bridge_core.py -- Kuhn simplicial geometry on the L^4 torus in LATTICE UNITS (a=1),
element matrices, exact analytic gradients w.r.t. squared edge lengths, Regge action,
and the matter effective-action gradient.

Conventions (all fixed by the campaign spec, not re-derived here):
  * s_e = ell_e^2 is the variable.
  * Vol  = sum_sigma V_sigma,   V = sqrt(det G)/4!,  G_ab = (s_{0,a+1}+s_{0,b+1}-s_{a+1,b+1})/2
  * S_Regge = sum_h A_h delta_h,   dS/ds_e = sum_{h ni e} delta_h dA_h/ds_e   (NO 1/2)
  * matter: K v = lambda M v  (P1 FEM stiffness, lumped mass), operator spectrum lambda
  * improvement: mu(lambda) = lambda + lambda^2/24 (covariant Symanzik), plain: mu = lambda
  * W = -(1/2) sum_i E_1(tau0 (mu_i + m^2))
    dW/ds_e = (1/2) [ Tr(F(B) Yhat_e) - Tr(G(B) Zhat_e) ]
       F(l) = f(mu(l)) mu'(l),  G(l) = l F(l),  f(x) = exp(-tau0 (x+m^2))/(x+m^2)
       B = M^{-1/2} K M^{-1/2},  Yhat = M^{-1/2} dK M^{-1/2},  Zhat = M^{-1/2} dM M^{-1/2}
"""
import numpy as np, itertools

d = 4
NC = 5           # corners of a 4-simplex
PAIRS = [(i, j) for i in range(NC) for j in range(i + 1, NC)]   # 10 edges
PIDX = {p: k for k, p in enumerate(PAIRS)}

# ---------------------------------------------------------------- Kuhn combinatorics
PERMS = list(itertools.permutations(range(d)))          # 24
def corner_offsets():
    """CORN[p] = (5,4) int array of the corner offsets of Kuhn simplex type p."""
    out = []
    for perm in PERMS:
        a = np.zeros((NC, d), dtype=np.int64)
        cur = np.zeros(d, dtype=np.int64)
        for m, ax in enumerate(perm):
            cur = cur.copy(); cur[ax] += 1
            a[m + 1] = cur
        out.append(a)
    return np.array(out)                                 # (24,5,4)
CORN = corner_offsets()

# 15 nonzero 0/1 edge classes
ECLS = [np.array(v) for v in itertools.product((0, 1), repeat=d) if sum(v) > 0]
ECIDX = {tuple(v): i for i, v in enumerate(ECLS)}
NE = len(ECLS)                                           # 15

# for each simplex type and each of its 10 edges: (class index, x0-offset of the edge base)
SEC = np.zeros((24, 10), dtype=np.int64)
SEX = np.zeros((24, 10), dtype=np.int64)
for p in range(24):
    for k, (i, j) in enumerate(PAIRS):
        u = CORN[p][j] - CORN[p][i]
        SEC[p, k] = ECIDX[tuple(u)]
        SEX[p, k] = CORN[p][i][0]

# ---------------------------------------------------------------- configuration
def edge_s(L, amp, nk, alpha):
    """S[c, x0] = squared length of the class-c edge whose base vertex has x0-coord x0,
    for the diagonal metric g_mumu = 1 + alpha_mu * amp * sin(2 pi nk y / L),
    evaluated at the edge midpoint (y = x0 + u0/2)."""
    alpha = np.asarray(alpha, dtype=float)
    S = np.zeros((NE, L))
    for c, u in enumerate(ECLS):
        y = np.arange(L) + 0.5 * u[0]
        f = amp * np.sin(2.0 * np.pi * nk * y / L)
        S[c] = sum(u[mu] * (1.0 + alpha[mu] * f) for mu in range(d))
    return S

def simplex_s(S, L):
    """SS[p, x0b, k] = squared length of edge k of Kuhn simplex (type p, base x0b)."""
    x0b = np.arange(L)
    return S[SEC[:, None, :], (x0b[None, :, None] + SEX[:, None, :]) % L]

# ---------------------------------------------------------------- element quantities
_GA = np.zeros((10, d, d))      # dG/ds_k
for k, (i, j) in enumerate(PAIRS):
    if i == 0:
        c = j - 1
        _GA[k][c, :] += 0.5; _GA[k][:, c] += 0.5
    else:
        a, b = i - 1, j - 1
        _GA[k][a, b] -= 0.5; _GA[k][b, a] -= 0.5

def gram(ss):
    """ss: (...,10) -> G: (...,4,4)"""
    sh = ss.shape[:-1]
    G = np.zeros(sh + (d, d), dtype=ss.dtype)
    for a in range(d):
        for b in range(d):
            G[..., a, b] = 0.5 * (ss[..., PIDX[(0, a + 1)]] + ss[..., PIDX[(0, b + 1)]]
                                  - (ss[..., PIDX[(min(a, b) + 1, max(a, b) + 1)]] if a != b else 0.0))
    return G

def element(ss):
    """ss (...,10) -> V (...,), loc (...,5,5), dV (...,10), dloc (...,10,5,5)."""
    G = gram(ss)
    Gi = np.linalg.inv(G)
    det = np.linalg.det(G)
    V = np.sqrt(det) / 24.0
    # loc
    sh = ss.shape[:-1]
    loc = np.zeros(sh + (NC, NC))
    loc[..., 1:, 1:] = V[..., None, None] * Gi
    loc[..., 0, 1:] = -loc[..., 1:, 1:].sum(axis=-2)
    loc[..., 1:, 0] = loc[..., 0, 1:]
    loc[..., 0, 0] = -loc[..., 0, 1:].sum(axis=-1)
    # derivatives
    tr = np.einsum('...ab,kba->...k', Gi, _GA)                 # tr(G^-1 dG/ds_k)
    dV = 0.5 * V[..., None] * tr                                # (...,10)
    dGi = -np.einsum('...ac,kcd,...db->...kab', Gi, _GA, Gi)    # (...,10,4,4)
    dloc = np.zeros(sh + (10, NC, NC))
    dloc[..., :, 1:, 1:] = dV[..., :, None, None] * Gi[..., None, :, :] + V[..., None, None, None] * dGi
    dloc[..., :, 0, 1:] = -dloc[..., :, 1:, 1:].sum(axis=-2)
    dloc[..., :, 1:, 0] = dloc[..., :, 0, 1:]
    dloc[..., :, 0, 0] = -dloc[..., :, 0, 1:].sum(axis=-1)
    return V, loc, dV, dloc

# ---------------------------------------------------------------- triangles / Regge
# hinge of a 4-simplex = 2-face; the dihedral angle there is indexed by the two
# EXCLUDED corners (p,q):  cos theta_pq = - loc[p,q]/sqrt(loc[p,p] loc[q,q])
TRI = [(t, [x for x in range(NC) if x not in t]) for t in PAIRS]   # (excluded pair, the 3 corners)

def tri_key(p, ijk):
    """canonical key of the triangle {corners ijk} of Kuhn type p: (x0 offset of its
    lowest corner, the two increment vectors as tuples)."""
    i, j, k = ijk
    a = CORN[p]
    return (int(a[i][0]), tuple(a[j] - a[i]), tuple(a[k] - a[i]))

def heron(sab, sac, sbc):
    q = 2.0 * (sab * sac + sab * sbc + sac * sbc) - (sab ** 2 + sac ** 2 + sbc ** 2)
    return np.sqrt(np.maximum(q, 0.0)) / 4.0
