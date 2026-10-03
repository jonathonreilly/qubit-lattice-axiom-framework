"""Polish the search with Levenberg-Marquardt on the residual vector (UU^+ - 1 on the exact
4r+2 grid). Many random seeds; tabulate final unitarity defect vs W3 (GL formula).
"""
import sys
import time
import numpy as np
from scipy.optimize import least_squares, minimize
from wlib import grid, w3_from

t0 = time.time()
r = int(sys.argv[1]) if len(sys.argv) > 1 else 1
nseed = int(sys.argv[2]) if len(sys.argv) > 2 else 12
rng = np.random.default_rng(7)
vs = np.array([(a, b, c) for a in range(-r, r + 1) for b in range(-r, r + 1) for c in range(-r, r + 1)], float)
nv = len(vs)
Ph = np.exp(1j * grid(4 * r + 2) @ vs.T)
Kf = grid(24)
Pf = np.exp(1j * Kf @ vs.T)
iu = np.triu_indices(2)


def unpack(x):
    return (x[: 4 * nv] + 1j * x[4 * nv:]).reshape(nv, 4)


def resid(x):
    U = (Ph @ unpack(x)).reshape(-1, 2, 2)
    E = U @ U.conj().transpose(0, 2, 1) - np.eye(2)
    e = E[:, iu[0], iu[1]]
    return np.concatenate([e.real.ravel(), e[:, 1].imag.ravel()])


def jacfun(x):
    """Analytic Jacobian of resid, vectorized. dE_ab = c d_ai conj(U_bj) + conj(c) U_aj d_bi."""
    U = (Ph @ unpack(x)).reshape(-1, 2, 2)
    I2 = np.eye(2)
    blocks = []
    for part in (1.0, 1j):
        c = part * Ph  # (M, nv)
        # T1[m,v,i,j,a,b] = c[m,v] d_ai conj(U[m,b,j]);  T2 = conj(c) U[m,a,j] d_bi
        T1 = np.einsum("mv,ai,mbj->mvijab", c, I2, U.conj())
        T2 = np.einsum("mv,maj,bi->mvijab", c.conj(), U, I2)
        dE = (T1 + T2).reshape(len(U), 4 * nv, 2, 2)
        e = dE[:, :, iu[0], iu[1]]  # (M, 4nv, 3)
        blocks.append(np.concatenate([e.real.transpose(0, 2, 1).reshape(-1, 4 * nv),
                                      e[:, :, 1].imag], axis=0))
    return np.concatenate(blocks, axis=1)


def F_and_grad(x):
    A = unpack(x)
    U = (Ph @ A).reshape(-1, 2, 2)
    Ud = U.conj().transpose(0, 2, 1)
    E = U @ Ud - np.eye(2)
    F = np.einsum("mij,mji->", E, E).real
    G = (Ph.T @ (Ud @ E).reshape(-1, 4)).reshape(nv, 2, 2).transpose(0, 2, 1).reshape(nv, 4)
    return F, np.concatenate([4 * G.real.ravel(), -4 * G.imag.ravel()])


def measure(x):
    A = unpack(x)
    U = (Pf @ A).reshape(-1, 2, 2)
    dU = np.stack([((1j * vs[:, j][None, :] * Pf) @ A).reshape(-1, 2, 2) for j in range(3)])
    smin = np.linalg.svd(U, compute_uv=False).min()
    defect = np.abs(U @ U.conj().transpose(0, 2, 1) - np.eye(2)).max()
    w = w3_from(U, dU)[0] if smin > 1e-8 else np.nan
    return defect, smin, w


rows = []
for s in range(nseed):
    x = np.concatenate([rng.normal(size=4 * nv), rng.normal(size=4 * nv)]) / np.sqrt(2 * nv)
    x = minimize(F_and_grad, x, jac=True, method="L-BFGS-B",
                 options={"maxiter": 3000, "ftol": 1e-30, "gtol": 1e-14}).x
    sol = least_squares(resid, x, jac=jacfun, method="lm", xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=300)
    d, sm, w = measure(sol.x)
    rows.append((s, d, sm, w))
    print(f"  seed {s:2d}: sup|UU^+-1| = {d:.2e}  min sing.val = {sm:.3e}  W3_GL = {w:+.4f}", flush=True)
    if time.time() - t0 > 45:
        break
print(f"time {time.time()-t0:.1f}s")
