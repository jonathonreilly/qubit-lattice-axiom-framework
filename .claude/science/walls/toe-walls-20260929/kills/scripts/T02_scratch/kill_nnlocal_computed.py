"""T02 script A2: weak-reading test of Claim R (range follows from Admissibility locality).

Strong reading (proved by the injective monomial map): the compressed one-site generator
h_x(records) is a polynomial whose monomials are in 1-1 correspondence with Pauli strings;
it depends only on the six NN records iff every string of the generator lives on a clique.

Weak reading (this script): only the DIRECTION of h_x has to be independent of records
beyond nearest neighbours (the odds are (1 + lam p.h^)/2).  Could a fine-tuned covariant
star-range generator with non-clique terms have a direction that does not care about
far records?  We build the explicit covariant basis (possibility covariance = SU(2) x
proper cubic rotations, 24 real dimensions) and minimise a far-dependence functional
over the space, with the non-clique part normalised to 1.
Pre-registered: FAIL of the route if the minimum reaches ~0 (< 1e-6) at non-clique norm 1.
"""
import itertools, sys, json
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, ".")
from count_covariant_generators import (K_list, G, act, inv_basis, perm_matrix, is_clique)

rng = np.random.default_rng(20260929)

# ---- explicit covariant basis (unsoldered)
B, off, tot = {}, {}, 0
for K in K_list:
    n = len(K)
    B[K] = inv_basis(n)
    off[K] = tot
    tot += B[K].shape[1]
Rey = np.zeros((tot, tot))
for g in G:
    for K in K_list:
        n = len(K)
        Kp, pi = act(g, K)
        P = perm_matrix(n, pi)
        blk = B[Kp].T @ P @ B[K]
        Rey[off[Kp]:off[Kp]+blk.shape[0], off[K]:off[K]+blk.shape[1]] += blk/len(G)
w, V = np.linalg.eigh((Rey+Rey.T)/2)
sel = np.where(w > 0.5)[0]
print("covariant dimension", len(sel), "(expected 24)")
C = V[:, sel]                                   # coordinates in invariant bases
# coefficient tensors of each basis vector
basis = []
for m in range(C.shape[1]):
    a = {K: (B[K] @ C[off[K]:off[K]+B[K].shape[1], m]).reshape((3,)*len(K)) for K in K_list}
    basis.append(a)
clique_mask = np.zeros(len(basis))          # non-clique norm per basis vector (projector onto clique classes)
def clique_norm2(m):
    return sum(float(np.sum(basis[m][K]**2)) for K in K_list if is_clique(K))
def nonclique_norm2(m):
    return sum(float(np.sum(basis[m][K]**2)) for K in K_list if not is_clique(K))
# split the 24-dim space into clique (1) and non-clique (23) parts by projecting on clique classes
Pc = np.zeros((len(basis), len(basis)))
for i in range(len(basis)):
    for j in range(len(basis)):
        Pc[i,j] = sum(float(np.sum(basis[i][K]*basis[j][K])) for K in K_list if is_clique(K))
wc, Vc = np.linalg.eigh(Pc)
print("clique-part eigenvalues (should be one nonzero):", np.round(wc[-3:], 6))
# orthonormal basis of the non-clique subspace = vectors whose clique part is zero
Ncl = Vc[:, np.abs(wc) < 1e-9]
Cl = Vc[:, np.abs(wc) >= 1e-9]
print("non-clique subspace dim", Ncl.shape[1], " clique dim", Cl.shape[1])

# ---- field polynomial of each basis vector on configurations
NN = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
offsets = set()
for K in K_list:
    for i in range(len(K)):
        for j in range(len(K)):
            if i != j:
                offsets.add(tuple(a-b for a,b in zip(K[j], K[i])))
offsets = sorted(offsets)
far = [o for o in offsets if o not in NN]
print("offsets touching x:", len(offsets), "of which NN", len([o for o in offsets if o in NN]), "far", len(far))

def rand_unit(shape):
    v = rng.normal(size=shape + (3,))
    return v / np.linalg.norm(v, axis=-1, keepdims=True)

NNC, FC = 24, 12                    # NN configurations, far configurations per NN configuration
qNN = rand_unit((NNC, 6))
qFar = rand_unit((NNC, FC, len(far)))
# record vector at every offset, per (nn config, far config)
def record_array():
    Q = {}
    for k,o in enumerate(NN):
        Q[o] = np.repeat(qNN[:, None, k, :], FC, axis=1)
    for k,o in enumerate(far):
        Q[o] = qFar[:, :, k, :]
    return Q
Q = record_array()

def field_of(a, far_zero=False):
    """h_x for coefficient dict a on all (NNC, FC) configs; returns (NNC,FC,3)"""
    h = np.zeros((NNC, FC, 3))
    for K in K_list:
        n = len(K)
        T = a[K]
        if np.abs(T).max() < 1e-13: continue
        for i in range(n):
            others = [j for j in range(n) if j != i]
            # contract T over the other slots with the record vectors at offsets K[j]-K[i]
            X = np.moveaxis(T, i, -1)          # slot i last
            for j_idx in range(len(others)):
                pass
            # sequentially contract slots (in original order, skipping i)
            cur = T
            # contract from the highest axis down so axis numbers stay valid
            axes_order = sorted(others, reverse=True)
            cur_t = cur
            res = None
            # build einsum string
            letters = "abcdefg"[:n]
            rec_letters = "".join("Nf" + "" for _ in [0])
            ops, subs = [T], [letters]
            for j in others:
                o = tuple(x-y for x,y in zip(K[j], K[i]))
                qv = Q[o]                        # (NNC,FC,3)
                ops.append(qv); subs.append("NF" + letters[j])
            expr = ",".join(subs) + "->NF" + letters[i]
            h += np.einsum(expr, *ops, optimize=True)
    return h

Hn = np.array([field_of(basis[m]) for m in range(len(basis))])   # (24,NNC,FC,3)
print("precomputed fields", Hn.shape)

def coeff_from(x):
    # x = [J (1 clique dir), y (23 non-clique) ] -> coordinates in the 24-basis
    return Cl[:, 0]*x[0] + Ncl @ x[1:]
def F(x, ncnorm=1.0):
    y = x[1:]
    y = y / (np.linalg.norm(y)+1e-30) * ncnorm
    c = coeff_from(np.concatenate([[x[0]], y]))
    h = np.tensordot(c, Hn, axes=(0,0))                           # (NNC,FC,3)
    hh = h / (np.linalg.norm(h, axis=-1, keepdims=True)+1e-30)
    mean = hh.mean(axis=1, keepdims=True)
    return float(np.mean(1 - np.sum(mean**2, axis=-1)))            # 1-|<h^>|^2 averaged: 0 iff direction constant over far configs


def Fr(y, rho, sgn):
    y = y/(np.linalg.norm(y)+1e-30)*np.sqrt(rho)
    J = sgn*np.sqrt(1-rho)
    c = Cl[:,0]*J + Ncl @ y
    h = np.tensordot(c, Hn, axes=(0,0))
    hh = h/(np.linalg.norm(h,axis=-1,keepdims=True)+1e-30)
    mean = hh.mean(axis=1,keepdims=True)
    return float(np.mean(1-np.sum(mean**2,axis=-1)))

# --- kill: compute (not define) the NN-local subspace of the 24-dim covariant space
# far-part map: c -> h(N,F) - mean_F h(N,F), stacked over all sampled (N,F)
Hvar = Hn - Hn.mean(axis=2, keepdims=True)                  # (24,NNC,FC,3)
M = Hvar.reshape(Hn.shape[0], -1)                           # rows = basis vectors
u,s,vt = np.linalg.svd(M, full_matrices=True)
print("singular values of the far-dependence map (24 covariant basis vectors):", np.round(s,4))
null_dim = int(np.sum(s < 1e-9)) + max(0, M.shape[0]-len(s))
print("computed dimension of the subspace with NO far-record dependence of h_x (sampled):", null_dim)
# is that null vector the clique vector?
Nspace = u[:, s < 1e-9] if null_dim>0 else np.zeros((24,0))
# u are left singular vectors (24x24): null of M^T ... need coefficient vectors c with c^T M = 0
uu, ss, vv = np.linalg.svd(M.T, full_matrices=False)
cnull = vv[ss < 1e-9].T if np.any(ss<1e-9) else np.zeros((24,0))
print("null coefficient vectors:", cnull.shape[1])
# overlap with clique direction Cl[:,0]
if cnull.shape[1]>0:
    ov = np.abs(cnull.T @ Cl[:,0])
    print("overlap of null space with clique (bond) direction:", np.round(ov,6))
# smallest nonzero singular value (linear-order strength of far dependence, per unit coefficient norm)
print("smallest nonzero singular value:", float(np.min(ss[ss>1e-9])))
