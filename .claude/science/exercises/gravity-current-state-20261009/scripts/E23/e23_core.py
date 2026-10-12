"""E2/E3 core: vacuum TT stress and stiffness of a label-blind (or fixed-graph) free field on a point set.

Generalises R3's C2 toy (scripts/R3_c2_pointset_shear_modulus.py) and KF1a's K1 per-direction statistics.
Field: H = 1/2 sum pi^2 + 1/2 phi^T (L_g + m^2) phi on the PRESENT points only.
L_g = weighted graph Laplacian, weights w(d_g^2) with d_g^2 = dx^T g dx, g = exp(t h), h traceless, tr h^2 = 1.
Couplings:
  'pd' : proper-distance kernel, all pairs with d_g < R, w = (1 - d_g^2/R^2)^4  (R3/K1 exactly, R = 1.8)
  'nn' : fixed graph = unit-length Z^3 bonds among present sites (only for subsets of Z^3), w = 1/d_g^2
Spectral functionals (E = sum_n f(lam_n)):
  boson zero-point   f = 1/2 sqrt(lam + m2)
  fermion sea (spinless, smeared): single-particle H = L_g, grand potential f = -T log(1 + exp(-(lam-mu)/T))
Exact derivatives at t = 0 (eigen-perturbation):
  E'  = sum_n f'(l_n) A1_nn
  E'' = sum_n f'(l_n) A2_nn + sum_{nm} A1_nm^2 f'[l_n, l_m]    (divided difference of f')
TT directions: orthonormal E_g pair and T_2g triple (K1 convention).
"""
import numpy as np
import scipy.sparse as sps

R_PD = 1.8


def tt_dirs():
    E = [np.diag([1., -1, 0]) / np.sqrt(2), np.diag([1., 1, -2]) / np.sqrt(6)]
    T = []
    for (i, j) in [(0, 1), (1, 2), (0, 2)]:
        M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1 / np.sqrt(2); T.append(M)
    return E + T          # 5 directions: 0,1 = E_g ; 2,3,4 = T_2g


DIRS = tt_dirs()
CH = {'E_g': [0, 1], 'T_2g': [2, 3, 4]}


def kernel(mode, s):
    """weights and derivatives w.r.t. s = d_g^2."""
    if mode == 'pd':
        u = s / R_PD**2
        return (1 - u)**4, -4 * (1 - u)**3 / R_PD**2, 12 * (1 - u)**2 / R_PD**4
    if mode == 'nn':
        return 1 / s, -1 / s**2, 2 / s**3
    raise ValueError(mode)


def pairs(X, Lb, mode, G=None):
    """minimum-image pairs. G = metric (for FD checks); default identity. Returns I, J, D (label displacements)."""
    n = len(X)
    D = X[None, :, :] - X[:, None, :]
    if Lb is not None:
        D -= Lb * np.round(D / Lb)
    if G is None:
        d2 = np.einsum('ijk,ijk->ij', D, D)
    else:
        d2 = np.einsum('ijk,kl,ijl->ij', D, G, D)
    iu = np.triu_indices(n, 1)
    d2u = d2[iu]
    if mode == 'pd':
        msk = d2u < R_PD**2                       # label-blind: pairs chosen by CURRENT proper distance
    else:
        msk = np.abs(np.einsum('ijk,ijk->ij', D, D)[iu] - 1) < 1e-9   # fixed graph: unit Z^3 bonds
    return iu[0][msk], iu[1][msk], D[iu][msk]


def pairs_sparse(X, Lb, mode):
    """KD-tree version for large sets (periodic box via boxsize, or open)."""
    from scipy.spatial import cKDTree
    r = R_PD if mode == 'pd' else 1.0 + 1e-6
    if Lb is not None:
        tr = cKDTree(np.mod(X, Lb), boxsize=Lb)
        P = tr.query_pairs(r, output_type='ndarray')
        D = np.mod(X[P[:, 1]], Lb) - np.mod(X[P[:, 0]], Lb)
        D -= Lb * np.round(D / Lb)
    else:
        tr = cKDTree(X)
        P = tr.query_pairs(r, output_type='ndarray')
        D = X[P[:, 1]] - X[P[:, 0]]
    if mode == 'nn':
        keep = np.abs(np.einsum('pk,pk->p', D, D) - 1) < 1e-6
        P, D = P[keep], D[keep]
    return P[:, 0], P[:, 1], D


def lap_dense(n, I, J, w):
    Lm = np.zeros((n, n))
    np.add.at(Lm, (I, J), -w); np.add.at(Lm, (J, I), -w)
    deg = np.zeros(n); np.add.at(deg, I, w); np.add.at(deg, J, w)
    Lm[np.diag_indices(n)] += deg
    return Lm


def lap_sparse(n, I, J, w):
    deg = np.zeros(n); np.add.at(deg, I, w); np.add.at(deg, J, w)
    rows = np.concatenate([I, J, np.arange(n)]); cols = np.concatenate([J, I, np.arange(n)])
    return sps.csr_matrix((np.concatenate([-w, -w, deg]), (rows, cols)), shape=(n, n))


def boson_fns(m2):
    return (lambda l: 0.25 / np.sqrt(l + m2)), (lambda l: -0.125 / (l + m2)**1.5)


def fermion_fns(mu, T):
    def nf(l):
        return 0.5 * (1 - np.tanh((l - mu) / (2 * T)))
    return nf, (lambda l: -nf(l) * (1 - nf(l)) / T)


def derivs(n, I, J, D, mode, fnsets, dirs=DIRS):
    """Return array (len(fnsets), 5, 2): per-site E' and E'' for each functional and TT direction."""
    s0 = np.einsum('pk,pk->p', D, D)
    w, w1s, w2s = kernel(mode, s0)
    lam, V = np.linalg.eigh(lap_dense(n, I, J, w))
    lam = np.clip(lam, 0, None)
    dl = lam[:, None] - lam[None, :]
    deg = np.abs(dl) < 1e-9
    pre = []
    for (g1, g2) in fnsets:
        F1 = g1(lam)
        with np.errstate(divide='ignore', invalid='ignore'):
            F = (F1[:, None] - F1[None, :]) / dl
        F[deg] = g2(0.5 * (lam[:, None] + lam[None, :]))[deg]
        pre.append((F1, F))
    out = np.zeros((len(fnsets), len(dirs), 2))
    for d, h in enumerate(dirs):
        sp = np.einsum('pi,ij,pj->p', D, h, D)
        spp = np.einsum('pi,ij,pj->p', D, h @ h, D)
        L1 = lap_sparse(n, I, J, w1s * sp)
        L2 = lap_sparse(n, I, J, w2s * sp**2 + w1s * spp)
        A1 = V.T @ (L1 @ V)
        dA2 = np.sum(V * (L2 @ V), axis=0)
        dA1 = np.diag(A1)
        A1sq = A1**2
        for k, (F1, F) in enumerate(pre):
            out[k, d, 0] = np.sum(F1 * dA1) / n
            out[k, d, 1] = (np.sum(F1 * dA2) + np.sum(A1sq * F)) / n
    return out, lam


def energy_total(X, Lb, mode, G, m2):
    """total boson zero-point energy per site at metric G (pairs recomputed in proper distance for 'pd')."""
    n = len(X)
    I, J, D = pairs(X, Lb, mode, G=G)
    s = np.einsum('pi,ij,pj->p', D, G, D)
    w = kernel(mode, s)[0]
    lam = np.clip(np.linalg.eigvalsh(lap_dense(n, I, J, w)), 0, None)
    return np.sum(0.5 * np.sqrt(lam + m2)) / n


def expm_sym(h, t):
    ev, U = np.linalg.eigh(h)
    return U @ np.diag(np.exp(t * ev)) @ U.T


def kspace_Z3(mode, fns, M=64, extra=None):
    """infinite (M large) cubic crystal, density 1. Returns {E_g: (e1,e2), T_2g: (e1,e2)} per site."""
    rr = 2
    ns = np.array([(a, b, c) for a in range(-rr, rr + 1) for b in range(-rr, rr + 1) for c in range(-rr, rr + 1)
                   if (a, b, c) != (0, 0, 0)], float)
    s = np.einsum('pk,pk->p', ns, ns)
    keep = s < R_PD**2 if mode == 'pd' else np.abs(s - 1) < 1e-9
    ns, s = ns[keep], s[keep]
    w, w1s, w2s = kernel(mode, s)
    k = 2 * np.pi * np.arange(M) / M
    K = np.stack(np.meshgrid(k, k, k, indexing='ij'), -1).reshape(-1, 3)
    C = 1 - np.cos(K @ ns.T)           # lambda(k) = sum over all n (both signs) w_n (1 - cos k.n)  (R3 convention)
    lam = C @ w
    g1, g2 = fns
    res = {}
    for ch, idx in CH.items():
        v1, v2 = [], []
        for d in idx:
            h = DIRS[d]
            sp = np.einsum('pi,ij,pj->p', ns, h, ns)
            spp = np.einsum('pi,ij,pj->p', ns, h @ h, ns)
            l1 = C @ (w1s * sp)
            l2 = C @ (w2s * sp**2 + w1s * spp)
            v1.append(np.mean(g1(lam) * l1)); v2.append(np.mean(g1(lam) * l2 + g2(lam) * l1**2))
        res[ch] = (np.mean(v1), np.mean(v2))
    return res


def summarize(vals_by_box, ch_idx):
    """vals_by_box: {Lb: list of (nsites, array(5,2))}. Return per-box stats for stiffness (col 1) and stress (col 0)."""
    rows = []
    for Lb, lst in vals_by_box.items():
        Ns = np.array([x[0] for x in lst]); A = np.array([x[1] for x in lst])   # nr x 5 x 2
        out = {'Lb': Lb, 'nr': len(lst), 'Nmean': Ns.mean()}
        for ch, idx in ch_idx.items():
            st = A[:, idx, 1]; ss = A[:, idx, 0]
            out[ch + '_mean'] = st.mean(); out[ch + '_se'] = st.mean(axis=1).std(ddof=1) / np.sqrt(len(lst)) if len(lst) > 1 else 0
            # noise: per-direction sd (pooled over the channel's directions), times sqrt(N present)
            sd = st.std(ddof=1) if len(lst) > 1 else 0.0
            out[ch + '_sdrootN'] = sd * np.sqrt(Ns.mean())
            out[ch + '_sdrootN_se'] = sd * np.sqrt(Ns.mean()) / np.sqrt(2 * max(len(lst) - 1, 1))
            sds = ss.std(ddof=1) if len(lst) > 1 else 0.0
            out[ch + '_stress_sdrootN'] = sds * np.sqrt(Ns.mean())
        rows.append(out)
    return rows
