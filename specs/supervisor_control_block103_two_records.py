"""Supervisor control for block 103: NONLINEAR lattice control (not run by the workers). Sphere menu at beta, odds
pi_x(s) on a product grid of S^2 at every site of an L^3 box; boundary layer held at the uniform ordered sea (lean
along z); one record held at the centre with content s0. Self-consistent map log pi_x = sum_y log g_y - norm, g_y =
K1 pi_y (record: e^(b s.s0)/Z; boundary: K1 F). Red-black SOR in the log domain.
Measures: transverse lean T_x = <s.e_x>, lean M_x = <t>; compares T with the box hitting probability h of the record
site (massless channel) and dM with the box Green function of mass mL^2 (massive channel)."""
import sys
import time
import numpy as np
from numpy.polynomial.legendre import leggauss

beta = float(sys.argv[1]) if len(sys.argv) > 1 else 0.6
L = int(sys.argv[2]) if len(sys.argv) > 2 else 17
omega = float(sys.argv[3]) if len(sys.argv) > 3 else 1.6
nt, nph = 20, 24
tq, wt = leggauss(nt)
ph = 2 * np.pi * np.arange(nph) / nph
T, PH = np.meshgrid(tq, ph, indexing="ij")
T, PH = T.ravel(), PH.ravel()
W = (np.repeat(wt / 2, nph) / nph)
R = np.sqrt(1 - T * T)
S = np.stack([R * np.cos(PH), R * np.sin(PH), T], axis=1)
Z = np.sinh(beta) / beta
K = np.exp(beta * S @ S.T) * W[None, :] / Z
print(f"beta={beta} L={L} grid {len(W)} points; K1 1 - 1 max {np.abs(K.sum(1) - 1).max():.1e}")

F = 1 + 0.4 * T
for _ in range(20000):
    G = K @ F
    Fn = G ** 6
    Fn /= W @ Fn
    if np.abs(Fn - F).max() < 1e-14:
        F = Fn
        break
    F = Fn
GF = K @ F
MF = W @ (F * T)
print(f"uniform ordered sea: M = {MF:.6f}")

# the uniform sea's longitudinal mass on this grid (m = 0 sector): top eigenvalue of eta -> K(F eta)/G - <.>_F
A = K * F[None, :] / GF[:, None]
Q = A - np.outer(np.ones(len(W)), (W * F) @ A)
ev = np.linalg.eigvals(Q)
ev = np.sort(ev.real)[::-1]
print("top per-neighbour eigenvalues x6 (all sectors on the grid):", " ".join(f"{6 * e:.6f}" for e in ev[:6]))


def run(s0, tol=1e-11, maxit=4000, sites=None):
    c = L // 2
    sites = sites or [(c, c, c)]
    logP = np.tile(np.log(F), (L, L, L, 1))
    held = np.zeros((L, L, L), bool)
    held[0, :, :] = held[-1, :, :] = held[:, 0, :] = held[:, -1, :] = held[:, :, 0] = held[:, :, -1] = True
    rec = np.zeros((L, L, L), bool)
    for p in sites:
        rec[p] = True
    grec = np.exp(beta * S @ s0) / Z
    ii, jj, kk = np.indices((L, L, L))
    color = (ii + jj + kk) % 2
    upd = [(~held) & (~rec) & (color == q) for q in (0, 1)]
    t0 = time.time()
    for it in range(maxit):
        delta = 0.0
        for q in (0, 1):
            Pn = np.exp(logP)
            Pn /= (Pn * W).sum(-1, keepdims=True)
            g = Pn @ K.T
            g[held] = GF
            g[rec] = grec
            lg = np.log(g)
            acc = np.zeros_like(lg)
            acc[1:] += lg[:-1]; acc[:-1] += lg[1:]
            acc[:, 1:] += lg[:, :-1]; acc[:, :-1] += lg[:, 1:]
            acc[:, :, 1:] += lg[:, :, :-1]; acc[:, :, :-1] += lg[:, :, 1:]
            m = upd[q]
            new = acc[m]
            new -= np.log((np.exp(new - new.max(-1, keepdims=True)) * W).sum(-1, keepdims=True)) + new.max(-1, keepdims=True)
            old = logP[m]
            logP[m] = (1 - omega) * old + omega * new
            delta = max(delta, np.abs(new - old).max())
        if delta < tol:
            break
    Pn = np.exp(logP)
    Pn /= (Pn * W).sum(-1, keepdims=True)
    Tx = Pn @ (W * S[:, 0])
    Mx = Pn @ (W * T)
    print(f"  s0={np.round(s0, 4)}: {it + 1} iterations, residual {delta:.1e}, {time.time() - t0:.0f} s")
    return Tx, Mx


def box_solve(diag, body=None):
    """solve diag*u_x - sum_y u_y = delta(centre) on the interior with u = 0 on the boundary layer (dense-free Jacobi-CG)."""
    from scipy.sparse import lil_matrix
    from scipy.sparse.linalg import spsolve
    n = L - 2
    idx = lambda a, b, cc: ((a - 1) * n + (b - 1)) * n + (cc - 1)
    A = lil_matrix((n ** 3, n ** 3))
    for a in range(1, L - 1):
        for b in range(1, L - 1):
            for cc in range(1, L - 1):
                i = idx(a, b, cc)
                A[i, i] = diag
                for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                    p = (a + d[0], b + d[1], cc + d[2])
                    if 1 <= p[0] <= L - 2 and 1 <= p[1] <= L - 2 and 1 <= p[2] <= L - 2:
                        A[i, idx(*p)] = -1
    rhs = np.zeros(n ** 3)
    c = L // 2
    if body is None:
        rhs[idx(c, c, c)] = 1
        u = spsolve(A.tocsr(), rhs)
    else:
        A = A.tolil()
        for p in body:
            i = idx(*p)
            A.rows[i] = [i]
            A.data[i] = [1.0]
            rhs[i] = 1
        u = spsolve(A.tocsr(), rhs)
    full = np.zeros((L, L, L))
    full[1:-1, 1:-1, 1:-1] = u.reshape(n, n, n)
    return full


c = L // 2
h = box_solve(6.0)
h /= h[c, c, c]  # hitting probability of the centre (harmonic off it, 1 on it, 0 on the boundary layer)


print("\ntwo misaligned records (content e_x) against one: far-field charge ratio vs the box capacity ratio")
s0 = np.array([1.0, 0.0, 0.0])
T1, _ = run(s0)
h1 = box_solve(6.0, body=[(c, c, c)])
cap = lambda hh, body: sum(hh[p] - (hh[p[0]+1,p[1],p[2]]+hh[p[0]-1,p[1],p[2]]+hh[p[0],p[1]+1,p[2]]+hh[p[0],p[1]-1,p[2]]+hh[p[0],p[1],p[2]+1]+hh[p[0],p[1],p[2]-1])/6 for p in body)
c1 = cap(h1, [(c, c, c)])
for name, body in (("adjacent along x", [(c, c, c), (c + 1, c, c)]), ("adjacent along z", [(c, c, c), (c, c, c + 1)]), ("two apart along y", [(c, c, c), (c, c + 2, c)])):
    T2, _ = run(s0, sites=body)
    h2 = box_solve(6.0, body=body)
    c2 = cap(h2, body)
    far = [(c - 6, c, c), (c, c - 6, c), (c, c, c - 6), (c - 5, c - 5, c), (c + 6, c + 1, c - 3)]
    rt = [T2[p] / T1[p] for p in far]
    rh = [h2[p] / h1[p] for p in far]
    flat = [T2[p] / h2[p] for p in far]
    print(f"  {name}: T2/T1 at far sites " + " ".join(f"{x:.4f}" for x in rt) + " | h2/h1 " + " ".join(f"{x:.4f}" for x in rh)
          + f" | box capacities c2/c1 = {c2 / c1:.4f} (c1 = {c1:.5f}) | T2/h2 far " + " ".join(f"{x:.4f}" for x in flat))
