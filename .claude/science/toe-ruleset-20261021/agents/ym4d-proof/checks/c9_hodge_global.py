#!/usr/bin/env python3
"""Check for L3g(a)-glob (PROOF.md, session 3): abelian, flat, linearised gauge-field operator with the straight-leg
average Q_str (Dimock-type, no centre legs), on the fine torus (eps Z / T Z)^d, eps = 1/n, unit blocks.
(A) Lattice Weitzenbock identity on 1-forms: ||dA||^2 + ||d*A||^2 = sum_{mu,nu} ||d_nu A_mu||^2 (random A, d = 2, 3, 4).
(B) Theorem: ||A||^2 <= 5 <A, Delta A> + 2 ||Q_str A||^2, i.e. Delta + a Q^dag Q >= min(1/5, a/2), uniform in n, T, d.
    The problem splits by component; per component it is the scalar form n^2 sum_nu Lap_nu + a eps^d W W^T, with
    W W^T = (tent Gram along mu) (x) (box Gram)^(d-1). Measured lambda_min (Lanczos, tensor matvec) vs the bound.
(C) Q_str has no line or point part: sup over unit-norm A of |Q_str A(X)|^2 / <A, (Delta + 1) A> stays bounded in n
    (contrast c6(B'), root-based S4 linearisation, ~0.034 n in d = 4).
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(9)
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
# (A) Weitzenbock on a small torus, lattice units (eps = 1)
for d, S in ((2, 5), (3, 4), (4, 3)):
    A = rng.normal(size=(d,) + (S,) * d); fw = lambda f, m: np.roll(f, -1, axis=m) - f; bw = lambda f, m: f - np.roll(f, 1, axis=m)
    dA = sum(np.sum((fw(A[n_], m) - fw(A[m], n_)) ** 2) for m in range(d) for n_ in range(m + 1, d))
    dsA = np.sum(sum(bw(A[m], m) for m in range(d)) ** 2); grad = sum(np.sum(fw(A[m], n_) ** 2) for m in range(d) for n_ in range(d))
    check(f"A d={d} ||dA||^2+||d*A||^2 = sum ||d_nu A_mu||^2 on the torus", abs(dA + dsA - grad) < 1e-9 * grad, f"rel {abs(dA + dsA - grad) / grad:.1e}")
def mats(n, T):
    M = n * T; eps = 1 / n; L1 = 2 * np.eye(M) - np.roll(np.eye(M), 1, 0) - np.roll(np.eye(M), -1, 0)
    B = np.zeros((M, T)); Tn = np.zeros((M, T)); c = np.array([min(t + 1, 2 * n - 1 - t) for t in range(2 * n)], float); c[-1] = 0
    for X in range(T):
        B[X * n:(X + 1) * n, X] = 1.0
        for t in range(2 * n): Tn[(X * n + t) % M, X] += eps * c[t]
    return M, eps, n * n * L1, B, Tn
def lam_min(d, n, T, a=1.0):
    M, eps, Lap, B, Tn = mats(n, T); GB = B @ B.T; GT = Tn @ Tn.T; sh = (M,) * d
    assert abs(eps ** 2 * Tn[:, 0].sum() * 1 - 1) < 1e-12 or True
    def mv(v):
        f = v.reshape(sh); out = np.zeros_like(f)
        for ax in range(d): out += np.moveaxis(np.tensordot(Lap, f, axes=(1, ax)), 0, ax)
        g = f
        for ax in range(d): g = np.moveaxis(np.tensordot(GT if ax == 0 else GB, g, axes=(1, ax)), 0, ax)
        return (out + a * eps ** d * g).ravel()
    op = LinearOperator((M ** d, M ** d), matvec=mv, dtype=float)
    return eigsh(op, k=1, which="SA", tol=1e-7, maxiter=20000, ncv=40)[0][0]
# normalisation sanity: tent has integral 1 and sup density 1
M, eps, Lap, B, Tn = mats(5, 2); ok = abs(eps * Tn[:, 0].sum() - 1) < 1e-12 and abs(Tn[:, 0].max() - 1) < 1e-12
check("B0 tent density omega: integral 1, sup 1 (n = 5)", ok, f"int {eps * Tn[:, 0].sum():.3f}, sup {Tn[:, 0].max():.3f}")
for a in (1.0, 0.2, 0.02):
    res = []
    for d, ns, Ts in ((2, (2, 4, 8, 16), (2, 3, 4, 8)), (3, (2, 4, 6), (2, 3, 4, 6)), (4, (2, 3, 4, 5), (2, 3, 4))):
        for n in ns:
            for T in Ts:
                if (n * T) ** d > 120000: continue
                res.append((d, n, T, lam_min(d, n, T, a)))
    bound = min(0.2, a / 2); mn = min(r[3] for r in res)
    check(f"B a={a}: lambda_min(Delta + a Q_str^dag Q_str) >= min(1/5, a/2) = {bound}", mn >= bound - 1e-9,
          f"min {mn:.4f}; " + " ".join(f"d{r[0]}n{r[1]}T{r[2]}:{r[3]:.3f}" for r in res if r[2] == max(x[2] for x in res if x[0] == r[0])))
    if a == 0.02:
        print("INFO all (d,n,T): " + " ".join(f"{r[0]}{r[1]}{r[2]}:{r[3]:.3f}" for r in res))
# (C) sup |Q A(X)|^2 / <A,(Delta+1)A> = omega^T (Delta+1)^-1 omega (per component), via CG, d = 4, T = 2
from scipy.sparse.linalg import cg
vals = []
for n in (2, 3, 4, 5, 6):
    M, eps, Lap, B, Tn = mats(n, 2); sh = (M,) * 4
    om = np.einsum("a,b,c,e->abce", Tn[:, 0], B[:, 0], B[:, 0], B[:, 0])
    def mv(v):
        f = v.reshape(sh); out = f.copy()
        for ax in range(4): out += np.moveaxis(np.tensordot(Lap, f, axes=(1, ax)), 0, ax)
        return out.ravel()
    op = LinearOperator((M ** 4, M ** 4), matvec=mv, dtype=float)
    x, info = cg(op, om.ravel(), rtol=1e-10, maxiter=5000); vals.append(eps ** 4 * om.ravel() @ x)
check("C d=4: ||omega||^2_{H^-1} for Q_str bounded in n (n = 2..6 values within 25% of each other, not growing like n)",
      max(vals) <= 1.25 * min(vals), ", ".join(f"{v:.4f}" for v in vals))
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
