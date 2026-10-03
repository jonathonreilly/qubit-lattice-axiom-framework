"""A8 check 2: contact capture under exclusion (Q1 reading: carriers never enter recorded sites), 31^3 box.

Dilute single-carrier mean dynamics matching the MC rule (lane G g3): each tick a carrier attempts a hop with
prob 1/2 to one of 6 neighbours (1/12 each); a hop into a held record fails (carrier stays).  A carrier that
ARRIVES on a contact site (free site face-adjacent to a held record) is captured with odds q per arrival.
Reservoir: boundary layer held at u = 1 (stands in for the far gas).  Steady state:
    deg_f(x) u_x = (1 - q [x in S]) * sum_{y~x free} u_y        (x interior free)
  symmetrized:  [diag(deg_f/(1 - q 1_S)) - Adj_f] u = 0.
Charge Q = 12 * J, J = captures per tick (so Q -> Cap_box for q = 1).
Additivity ratio A = Q(lump) / (N * Q(single record, same q)).
"""
import os
for k in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[k] = "1"
import time
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import cg

t0 = time.time()
L, C = 31, 15
NS = L ** 3
idx = np.arange(NS).reshape(L, L, L)
I, J, K = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
res = ((I == 0) | (I == L - 1) | (J == 0) | (J == L - 1) | (K == 0) | (K == L - 1)).ravel()
rows, cols = [], []
for d in range(3):
    a = [slice(None)] * 3; b = [slice(None)] * 3
    a[d] = slice(0, L - 1); b[d] = slice(1, L)
    p = idx[tuple(a)].ravel(); q_ = idx[tuple(b)].ravel()
    rows += [p, q_]; cols += [q_, p]
rows = np.concatenate(rows); cols = np.concatenate(cols)
ADJ = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(NS, NS))


def mask_of(points):
    m = np.zeros(NS, dtype=bool)
    for (x, y, z) in points:
        m[idx[C + x, C + y, C + z]] = True
    return m


def solve(lump, q):
    free = ~lump
    adjf = ADJ.multiply(free[None, :]).tocsr()          # only free targets count
    deg = np.asarray(adjf.sum(1)).ravel()
    S = free & (np.asarray(ADJ @ lump.astype(float)).ravel() > 0)
    unk = free & ~res
    if q >= 1.0:
        unk = unk & ~S                                  # Dirichlet u = 0 on S
    fixed_val = np.where(res, 1.0, 0.0)
    ui = np.flatnonzero(unk)
    diag = deg[ui] / np.where(S[ui], 1.0 - min(q, 0.999999), 1.0)
    Aii = adjf[ui][:, ui]
    M = sp.diags(diag) - Aii
    b = adjf[ui] @ fixed_val
    x, info = cg(M, b, rtol=1e-11, maxiter=50000)
    u = fixed_val.copy(); u[ui] = x
    resid = np.linalg.norm(M @ x - b) / np.linalg.norm(b)
    inflow = adjf @ u                                   # sum over free neighbours of u_y
    Jcap = (q * inflow[S]).sum() / 12.0 if q < 1.0 else inflow[S].sum() / 12.0
    return 12.0 * Jcap, int(S.sum()), info, resid


def cube_c(s):
    o = -(s // 2)
    return [(o + i, o + j, o + k) for i in range(s) for j in range(s) for k in range(s)]


def sub_ball(R, d):
    m = int(np.ceil(R / d)); out = []
    for i in range(-m, m + 1):
        for j in range(-m, m + 1):
            for k in range(-m, m + 1):
                if (d * i) ** 2 + (d * j) ** 2 + (d * k) ** 2 <= R * R + 1e-9:
                    out.append((d * i, d * j, d * k))
    return out


qs = [1.0, 0.3, 0.1, 0.01, 0.001]
single = {}
lump1 = mask_of([(0, 0, 0)])
for q in qs:
    single[q] = solve(lump1, q)[0]
print("single record (box): Q(q) = " + "  ".join(f"q={q}: {single[q]:.4f} (Q/q={single[q]/q:.3f})" for q in qs))

print("\n lump              N   contacts | A = Q/(N*Q1) at q = " + "  ".join(f"{q:>7}" for q in qs) + " |  Q(q=1)")
worst = 0.0
for name, pts in [("cube3 (jammed)", cube_c(3)), ("cube5 (jammed)", cube_c(5)), ("cube7 (jammed)", cube_c(7)),
                  ("sparse d=3,R=3", sub_ball(3.0, 3)), ("sparse d=3,R=6", sub_ball(6.0, 3)),
                  ("sparse d=3,R=9", sub_ball(9.0, 3)), ("sparse d=4,R=8", sub_ball(8.0, 4))]:
    lump = mask_of(pts)
    N = len(pts)
    row = []
    for q in qs:
        Q, nS, info, resid = solve(lump, q)
        worst = max(worst, resid)
        row.append(Q / (N * single[q]))
        if q == 1.0:
            Q1 = Q
    print(f" {name:16s} {N:4d}  {nS:5d}   |                       " + "  ".join(f"{a:7.4f}" for a in row) + f" | {Q1:8.3f}")
print("\n collapse test: defect 1-A vs continuum-ball 1-F(t), t = N*Q1(q)/Q(lump, q=1)  (sparse lumps)")


def F(t):
    x = np.sqrt(3 * t)
    return (1 - np.tanh(x) / x) / t


for name, pts in [("sparse d=3,R=6", sub_ball(6.0, 3)), ("sparse d=3,R=9", sub_ball(9.0, 3)), ("sparse d=4,R=8", sub_ball(8.0, 4))]:
    lump = mask_of(pts); N = len(pts)
    Qcap = solve(lump, 1.0)[0]
    out = f" {name:16s}"
    for q in [0.1, 0.01, 0.001]:
        t = N * single[q] / Qcap
        A = solve(lump, q)[0] / (N * single[q])
        out += f" | q={q}: t={t:6.3f} 1-A={1-A:.4f} 1-F={1-F(t):.4f}"
    print(out)
print(f"\nmax CG relative residual {worst:.1e}; elapsed {time.time()-t0:.1f} s")
