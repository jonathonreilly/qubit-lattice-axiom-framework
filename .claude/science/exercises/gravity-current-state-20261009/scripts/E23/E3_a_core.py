"""E3 (a) core: icosahedral cut-and-project point sets and the LOCAL vacuum stiffness density on open patches.

Local density (one choice; the total is unambiguous and S(0) does not depend on the choice up to divergences):
  e_i(t) = 1/2 [ sqrt(L_g(t) + m2) ]_ii ,  sum_i e_i = E (boson zero-point energy).
e_i', e_i'' by 5-point finite differences in t (pairs recomputed in proper distance at every t; kernel C^3 at R).
For m2 = 1 the matrix function is exponentially local, so interior sites (distance > buffer from the patch edge)
carry the bulk value.  Validated on a Z^3 ball against the exact crystal value (E2_0 / R3).
"""
import numpy as np
from scipy.spatial import cKDTree
import e23_core as c

TAU = (1 + 5**0.5) / 2


def ico_projectors():
    a = np.array([(1, TAU, 0), (-1, TAU, 0), (0, 1, TAU), (0, -1, TAU), (TAU, 0, 1), (-TAU, 0, 1)], float)
    tp = -1 / TAU                                                 # Galois conjugate of tau
    b = np.array([(1, tp, 0), (-1, tp, 0), (0, 1, tp), (0, -1, tp), (tp, 0, 1), (-tp, 0, 1)], float)
    P = (a / np.linalg.norm(a, axis=1)[:, None]).T / np.sqrt(2)   # 3 x 6
    Q = (b / np.linalg.norm(b, axis=1)[:, None]).T / np.sqrt(2)
    return P, Q


def ico_patch(Rp, gamma, rw=(3 / (4 * np.pi))**(1 / 3)):
    """all par-projections Pn, n in Z^6, with |Pn| < Rp and |Qn - gamma| < rw (spherical window, density 4 pi rw^3/3)."""
    P, Q = ico_projectors()
    nb = int(np.floor(np.sqrt(Rp**2 + (np.linalg.norm(gamma) + rw)**2)))
    r = np.arange(-nb, nb + 1)
    tail = np.stack(np.meshgrid(r, r, r, r, indexing='ij'), -1).reshape(-1, 4).astype(float)
    pts, perp = [], []
    for i in r:
        for j in r:
            n = np.concatenate([np.full((len(tail), 1), i), np.full((len(tail), 1), j), tail], 1)
            xp = n @ P.T; xq = n @ Q.T
            m = (np.einsum('ij,ij->i', xp, xp) < Rp**2) & (np.einsum('ij,ij->i', xq - gamma, xq - gamma) < rw**2)
            pts.append(xp[m]); perp.append(xq[m] - gamma)
    return np.concatenate(pts), np.concatenate(perp)


def local_energy(X, G, m2, cand):
    I, J, D = cand
    s = np.einsum('pi,ij,pj->p', D, G, D)
    u = np.clip(s / c.R_PD**2, 0, 1)
    w = (1 - u)**4
    lam, V = np.linalg.eigh(c.lap_dense(len(X), I, J, w))
    return 0.5 * (V**2) @ np.sqrt(np.clip(lam, 0, None) + m2)


def local_stiffness(X, m2=1.0, delta=4e-3):
    """returns e1 (N x 5), e2 (N x 5): per-site first/second t-derivative for the 5 TT directions."""
    tr = cKDTree(X)
    P = tr.query_pairs(c.R_PD + 0.1, output_type='ndarray')
    cand = (P[:, 0], P[:, 1], X[P[:, 1]] - X[P[:, 0]])
    e0 = local_energy(X, np.eye(3), m2, cand)
    e1 = np.zeros((len(X), 5)); e2 = np.zeros((len(X), 5))
    for d, h in enumerate(c.DIRS):
        e = {s: local_energy(X, c.expm_sym(h, s * delta), m2, cand) for s in (-2, -1, 1, 2)}
        e2[:, d] = (-e[-2] + 16 * e[-1] - 30 * e0 + 16 * e[1] - e[2]) / (12 * delta**2)
        e1[:, d] = (e[-2] - 8 * e[-1] + 8 * e[1] - e[2]) / (12 * delta)
    return e1, e2


def ico_patch_fast(Rp, gamma, rw=(3 / (4 * np.pi))**(1 / 3)):
    """same set as ico_patch, enumerated through the window: n = (na, nb), nb solved from the perp condition."""
    P, Q = ico_projectors()
    Qa, Qb = Q[:, :3], Q[:, 3:]; Qbi = np.linalg.inv(Qb)
    nbnd = int(np.floor(np.sqrt(Rp**2 + (np.linalg.norm(gamma) + rw)**2)))
    r = np.arange(-nbnd, nbnd + 1)
    na = np.stack(np.meshgrid(r, r, r, indexing='ij'), -1).reshape(-1, 3).astype(float)
    cen = (gamma[None, :] - na @ Qa.T) @ Qbi.T                 # nb centre for each na
    hw = rw * np.linalg.norm(Qbi, axis=1)                        # half-widths of the bounding box
    k = int(np.ceil(hw.max())) + 1
    o = np.arange(-k, k + 1); off = np.stack(np.meshgrid(o, o, o, indexing='ij'), -1).reshape(-1, 3).astype(float)
    pts, perp = [], []
    for s in range(0, len(na), 20000):
        A = na[s:s + 20000]; B = np.round(cen[s:s + 20000])[:, None, :] + off[None, :, :]   # m x K x 3
        A = np.broadcast_to(A[:, None, :], B.shape)
        n = np.concatenate([A, B], -1).reshape(-1, 6)
        xq = n @ Q.T - gamma; ok = np.einsum('ij,ij->i', xq, xq) < rw**2
        n, xq = n[ok], xq[ok]; xp = n @ P.T; ok = np.einsum('ij,ij->i', xp, xp) < Rp**2
        pts.append(xp[ok]); perp.append(xq[ok])
    return np.concatenate(pts), np.concatenate(perp)
