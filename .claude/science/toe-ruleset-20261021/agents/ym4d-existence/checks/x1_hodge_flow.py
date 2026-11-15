"""Check x1 (criteria in x1_criteria.md, written before this script).

Cubical-lattice cochain complex on the periodic 4D lattice Z_n^4, forward-difference d.
A1: d d = 0.  A2/A3: Hodge Laplacians on 1- and 2-forms are componentwise scalar Laplacians.
B1: strict positivity of the scalar heat kernel.  B2: far-link response of a flowed plaquette is non-zero.
Reads no external files.
"""
import itertools
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply

D = 4


def site_index(x, n):
    i = 0
    for c in x:
        i = i * n + (c % n)
    return i


def forms(k):
    return list(itertools.combinations(range(D), k))


def dmat(k, n):
    """d: k-forms -> (k+1)-forms. Basis: (site, sorted direction tuple)."""
    Ik, Ik1 = forms(k), forms(k + 1)
    pos_k = {I: a for a, I in enumerate(Ik)}
    N = n ** D
    rows, cols, vals = [], [], []
    for x in itertools.product(range(n), repeat=D):
        sx = site_index(x, n)
        for b, J in enumerate(Ik1):
            r = b * N + sx
            for j, mu in enumerate(J):
                I = tuple(v for v in J if v != mu)
                a = pos_k[I]
                sign = (-1) ** j
                xp = list(x)
                xp[mu] += 1
                rows += [r, r]
                cols += [a * N + site_index(xp, n), a * N + sx]
                vals += [sign, -sign]
    return sp.csr_matrix((vals, (rows, cols)), shape=(len(Ik1) * N, len(Ik) * N))


def scalar_lap(n):
    N = n ** D
    rows, cols, vals = [], [], []
    for x in itertools.product(range(n), repeat=D):
        sx = site_index(x, n)
        rows.append(sx); cols.append(sx); vals.append(2.0 * D)
        for mu in range(D):
            for s in (1, -1):
                xp = list(x); xp[mu] += s
                rows.append(sx); cols.append(site_index(xp, n)); vals.append(-1.0)
    return sp.csr_matrix((vals, (rows, cols)), shape=(N, N))


def maxabs(M):
    M = M.tocoo()
    return 0.0 if M.nnz == 0 else float(np.max(np.abs(M.data)))


results = {}
for n in (4, 5):
    d0, d1, d2 = dmat(0, n), dmat(1, n), dmat(2, n)
    a1 = max(maxabs(d1 @ d0), maxabs(d2 @ d1))
    Ls = scalar_lap(n)
    L1 = d0 @ d0.T + d1.T @ d1
    L2 = d1 @ d1.T + d2.T @ d2
    a3 = maxabs(L1 - sp.block_diag([Ls] * len(forms(1))))
    a2 = maxabs(L2 - sp.block_diag([Ls] * len(forms(2))))
    results[n] = (a1, a2, a3)
    print(f"n={n}: A1 max|dd|={a1:.2e}  A2 max|D2-diag|={a2:.2e}  A3 max|D1-diag|={a3:.2e}")

A_ok = all(v <= 1e-10 for t in results.values() for v in t)

n = 5
N = n ** D
Ls = scalar_lap(n).tocsc()
d1 = dmat(1, n)
F2 = forms(2)
p12 = F2.index((0, 1)) * N + site_index((0, 0, 0, 0), n)
B_ok = True
for tau in (0.5, 2.0):
    # B1: the smallest entry of exp(-tau Ls) over all columns equals (translation invariance) the smallest
    # entry of the column of the origin.
    e0 = np.zeros(N); e0[0] = 1.0
    col = expm_multiply(-tau * Ls, e0)
    mn = float(col.min())
    # B2: response of F_12(tau, origin) to a unit perturbation of the link (x=(2,2,2,2), direction 2) [0-based dir 1].
    a = np.zeros(len(forms(1)) * N)
    a[forms(1).index((1,)) * N + site_index((2, 2, 2, 2), n)] = 1.0
    F0 = d1 @ a
    # flow componentwise with the scalar heat kernel (justified by A2)
    Ft = np.zeros_like(F0)
    for c in range(len(F2)):
        Ft[c * N:(c + 1) * N] = expm_multiply(-tau * Ls, F0[c * N:(c + 1) * N])
    resp = float(Ft[p12])
    print(f"tau={tau}: B1 min heat-kernel entry={mn:.3e}  B2 response F12(origin)={resp:.3e}")
    B_ok = B_ok and (mn > 0.0) and (abs(resp) > 1e-12)

print("PASS" if (A_ok and B_ok) else "FAIL", "A_ok=", A_ok, "B_ok=", B_ok)
