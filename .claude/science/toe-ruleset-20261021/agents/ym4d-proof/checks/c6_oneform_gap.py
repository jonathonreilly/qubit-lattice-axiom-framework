#!/usr/bin/env python3
"""Check for L3g(a) (PROOF.md, session 2): 1-form (gauge-field) fluctuation operators, abelian/free part.
(A) Block Hodge-Poincare (Neumann/absolute): on the bonds of a unit block {0..n-1}^d, spacing 1/n,
    lambda_min(d_B^* d_B + d_B d_B^*) = 4 n^2 sin^2(pi/(2n)) >= 4 exactly (tensor-product proof in PROOF.md).
(B) Global torus operator, Feynman gauge:  M = d^*d + d d^* + a Q^dag Q,  Q = linearisation (L1c) of the S4
    complete-axial log-average from spacing 1/n to unit blocks:  (QA)(X,mu) = n^-d sum_y int_{Gamma_y} A.
    Mechanism (L3g-ob in PROOF.md): Q contains line functionals (the complete-axial legs funnel onto the coordinate-1
    line through each root), whose H^-1 norm^2 grows like n in d = 4, log n in d = 3, and stays bounded in d = 2.
    Diagnostics: constants are exact eigenvectors (eigenvalue a); ||Q_row||^2_{H^-1} versus n; straight-leg control.
(C) The same operator restricted to the complete-axial gauge inside blocks (A = 0 on intra-block tree bonds,
    no d d^* term), residual coarse gauge left unfixed: lambda_min ~ a/n from coarse pure-gauge modes living on the
    inter-block faces (||A||^2 ~ n, |QA|^2 ~ 1, dA = 0). Gauge artifact; it says nothing about axial-gauge coercivity.
All numbers are finite diagnostics except (A), which checks an exact formula.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, itertools as it, numpy as np, scipy.sparse as sp
from scipy.sparse.linalg import lobpcg, LinearOperator
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
def complex_ops(shape, periodic, eps):
    """d0: sites->bonds, d1: bonds->plaquettes on a box/torus grid; bonds indexed (mu, site), only existing ones kept."""
    d = len(shape); X = np.array(list(it.product(*[range(s) for s in shape]))); Vn = len(X)
    fl = lambda Y: np.ravel_multi_index(tuple((Y % np.array(shape)).T), shape)
    E = np.eye(d, dtype=int); bonds = []; bidx = {}
    for m in range(d):
        ok = np.ones(Vn, bool) if periodic else (X[:, m] + 1 < shape[m])
        for v in np.nonzero(ok)[0]: bidx[(m, v)] = len(bonds); bonds.append((m, v))
    r, c, w = [], [], []
    for i, (m, v) in enumerate(bonds):
        r += [i, i]; c += [fl(X[v] + E[m]), v]; w += [1 / eps, -1 / eps]
    d0 = sp.csr_matrix((w, (r, c)), shape=(len(bonds), Vn))
    r, c, w = [], [], []; k = 0
    for m in range(d):
        for nu in range(m + 1, d):
            for v in range(Vn):
                x = X[v]
                if not periodic and (x[m] + 1 >= shape[m] or x[nu] + 1 >= shape[nu]): continue
                for (mm, y, s) in ((m, x, 1), (nu, x + E[m], 1), (m, x + E[nu], -1), (nu, x, -1)):
                    r.append(k); c.append(bidx[(mm, fl(y))]); w.append(s / eps)
                k += 1
    d1 = sp.csr_matrix((w, (r, c)), shape=(k, len(bonds)))
    return X, fl, bonds, bidx, d0, d1
# (A) block Hodge-Poincare
for d, ns in ((2, (2, 3, 5, 8)), (3, (2, 3, 4)), (4, (2, 3, 4))):
    res = []
    for n in ns:
        _, _, _, _, d0, d1 = complex_ops((n,) * d, False, 1 / n)
        H = (d1.T @ d1 + d0 @ d0.T).toarray(); lam = np.linalg.eigvalsh(H)[0]; res.append((n, lam, 4 * n * n * np.sin(np.pi / (2 * n)) ** 2))
    check(f"(A) d={d} block Hodge-Poincare: lambda_min = 4n^2 sin^2(pi/2n) >= 4, no averaging term needed",
          all(abs(l - f) < 1e-8 * max(1, f) and l >= 4 - 1e-9 for _, l, f in res), " ".join(f"n={n}:{l:.4f}" for n, l, _ in res))
# (B), (C) torus operators
def Qmatrix(d, n, T, X, fl, bidx):
    S = n * T; r0 = (n - 1) // 2; eps = 1 / n; E = np.eye(d, dtype=int); rows, cols, vals = [], [], []; row = 0
    def addpath(acc, start, steps):
        cur = start.copy()
        for m, sg in steps:
            if sg > 0: acc[bidx[(m, fl(cur))]] = acc.get(bidx[(m, fl(cur))], 0) + 1
            else: acc[bidx[(m, fl(cur - E[m]))]] = acc.get(bidx[(m, fl(cur - E[m]))], 0) - 1
            cur = cur + sg * E[m]
    def ax(o):
        st = []
        for m in range(d): k = o[m] - r0; st += [(m, 1 if k > 0 else -1)] * abs(k)
        return st
    for Xc in it.product(range(T), repeat=d):
        c = np.array(Xc) * n + r0
        for mu in range(d):
            acc = {}
            for o in it.product(range(n), repeat=d):
                o = np.array(o); st = ax(o); addpath(acc, c, st); addpath(acc, c + o - r0, [(mu, 1)] * n)
                rev = {}; addpath(rev, c + n * E[mu], st)
                for k_, v_ in rev.items(): acc[k_] = acc.get(k_, 0) - v_
            for k_, v_ in acc.items():
                if v_ != 0: rows.append(row); cols.append(k_); vals.append(v_ * eps / n ** d)
            row += 1
    return sp.csr_matrix((vals, (rows, cols)), shape=(row, len(bidx)))
def lowest(Mop, N, seed=0, extra=None):
    r = np.random.default_rng(seed); X0 = r.normal(size=(N, 6))
    if extra is not None: X0[:, :extra.shape[1]] = extra
    w, v = lobpcg(Mop, X0, largest=False, tol=1e-7, maxiter=400)
    i = np.argmin(w); x = v[:, i]; return float(x @ (Mop @ x) / (x @ x))  # Rayleigh quotient: rigorous upper bound
import warnings; warnings.filterwarnings("ignore")
from scipy.sparse.linalg import cg
a = 1.0; T = 2; out = {}; hm = {}
for d, ns in ((2, (3, 7, 15, 31)), (3, (3, 5, 9, 15)), (4, (3, 5, 7))):
    for n in ns:
        if time.time() - T0 > 80: break
        X, fl, bonds, bidx, d0, d1 = complex_ops((n * T,) * d, True, 1 / n)
        Q = Qmatrix(d, n, T, X, fl, bidx); N = len(bonds); eps = 1 / n
        K1 = (d1.T @ d1).tocsr(); K0 = (d0 @ d0.T).tocsr(); cq = a / eps ** d
        const = np.zeros((N, d))
        for i_, (m, v) in enumerate(bonds): const[i_, m] = 1
        Mc = K1 @ const + K0 @ const + cq * (Q.T @ (Q @ const))
        cerr = np.abs(Mc - a * const).max()
        # H^-1 norm^2 of one averaging functional (X=0, mu=last direction != 1), and of its straight-leg part only
        row = d - 1; q = Q[row].toarray().ravel()
        qs = np.zeros(N); r0 = (n - 1) // 2; E = np.eye(d, dtype=int)
        for o in it.product(range(n), repeat=d):
            cur = np.array(o) + 0 * r0
            for _ in range(n): qs[bidx[(d - 1, fl(cur))]] += eps / n ** d; cur = cur + E[d - 1]
        A1 = (K1 + K0 + sp.identity(N)).tocsr()
        z, _ = cg(A1, q, rtol=1e-10, maxiter=5000); zs, _ = cg(A1, qs, rtol=1e-10, maxiter=5000)
        h, hs = q @ z / eps ** d, qs @ zs / eps ** d
        # axial-gauge restriction: drop intra-block tree bonds
        keep = []
        for i_, (m, v) in enumerate(bonds):
            loc = X[v] % n; intra = loc[m] + 1 < n
            if not (intra and all(loc[rho] == r0 for rho in range(m + 1, d))): keep.append(i_)
        keep = np.array(keep); Pk = sp.csr_matrix((np.ones(len(keep)), (np.arange(len(keep)), keep)), shape=(len(keep), N))
        lamR = None
        if len(keep) < 50000:
            K1r = (Pk @ K1 @ Pk.T).tocsr(); Qr = (Q @ Pk.T).tocsr(); Qrs = Qr.T.tocsr()
            Mr = LinearOperator((len(keep),) * 2, matvec=lambda v: K1r @ v + cq * (Qrs @ (Qr @ v)), dtype=float)
            lamR = lowest(Mr, len(keep), extra=const[keep])
        out[(d, n)] = (cerr, h, hs, lamR)
        print(f"INFO d={d} n={n} dof={N}: const-mode err {cerr:.1e}; ||Q_row||^2_H-1 = {h:.4f} (straight legs only {hs:.4f}); axial-restricted lambda_min <= {lamR if lamR is None else round(lamR, 4)} ({time.time() - T0:.0f}s)")
def ser(d, j): return [out[k][j] for k in sorted(out) if k[0] == d and out[k][j] is not None]
check("(B) constant 1-forms are exact eigenvectors of the Feynman-gauge operator with eigenvalue a (T = 2 torus)",
      all(v[0] < 1e-8 for v in out.values()), "max err %.1e" % max(v[0] for v in out.values()))
h2, h3, h4 = ser(2, 1), ser(3, 1), ser(4, 1)
check("(B') d=4: H^-1 norm^2 of the S4 averaging functional grows with n, roughly linearly (last/first >= 0.5 * n_last/n_first)",
      len(h4) >= 2 and all(x < y for x, y in zip(h4, h4[1:])) and h4[-1] / h4[0] >= 0.5 * 7 / 3, ", ".join(f"{x:.3f}" for x in h4))
check("(B') d=2 control: H^-1 norm^2 stays bounded (last/first < 2)", len(h2) >= 2 and h2[-1] / h2[0] < 2, ", ".join(f"{x:.3f}" for x in h2))
check("(B') straight-leg part alone stays bounded in every d (last/first < 2)", all(len(ser(dd, 2)) >= 2 and ser(dd, 2)[-1] / ser(dd, 2)[0] < 2 for dd in (2, 3, 4)),
      "; ".join(f"d={dd}: " + ",".join(f"{x:.3f}" for x in ser(dd, 2)) for dd in (2, 3, 4)))
print("INFO d=3 H^-1 norm^2: " + ", ".join(f"{x:.3f}" for x in h3))
for dd in (2, 4):
    lr = ser(dd, 3)
    check(f"(C) d={dd} complete-axial-gauge restriction (residual coarse gauge NOT fixed): lambda_min ~ a c/n, as predicted for coarse pure-gauge modes on inter-block faces (n*lambda in [0.5, 1.5]) -- a gauge artifact",
          len(lr) >= 2 and all(0.5 <= x * n_ <= 1.5 for x, n_ in zip(lr, [k[1] for k in sorted(out) if k[0] == dd])), ", ".join(f"{x:.4f}" for x in lr))
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
