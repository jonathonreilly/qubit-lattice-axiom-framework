"""Adversarial search: try to find a STRICTLY LOCAL 2x2 unitary step (support cube {-r..r}^3)
with W3 != 0, by minimizing F = sum_k ||U U^+ - 1||_F^2 (exact unitarity test on a grid of
4r+2 points/axis), seeded (a) at the truncated Fourier series of the W3=-1 map E3, (b) at random.
Prediction (theorem): unitarity (F -> 0) and W3 != 0 cannot coexist.
"""
import sys
import time
import numpy as np
from scipy.optimize import minimize
from wlib import grid, w3_from
from models import E3

t0 = time.time()
r = int(sys.argv[1]) if len(sys.argv) > 1 else 1
rng = np.random.default_rng(int(sys.argv[2]) if len(sys.argv) > 2 else 0)
vs = np.array([(a, b, c) for a in range(-r, r + 1) for b in range(-r, r + 1) for c in range(-r, r + 1)], float)
nv = len(vs)
Kres = grid(4 * r + 2)
Ph = np.exp(1j * Kres @ vs.T)  # (M, nv)


def unpack(x):
    return (x[: 4 * nv] + 1j * x[4 * nv:]).reshape(nv, 4)


def pack(A):
    A = A.reshape(nv, 4)
    return np.concatenate([A.real.ravel(), A.imag.ravel()])


def F_and_grad(x):
    A = unpack(x)
    U = (Ph @ A).reshape(-1, 2, 2)
    Ud = U.conj().transpose(0, 2, 1)
    E = U @ Ud - np.eye(2)
    F = np.einsum("mij,mji->", E, E).real
    UdE = (Ud @ E).reshape(-1, 4)
    G = (Ph.T @ UdE).reshape(nv, 2, 2)  # G_v = sum_k e^{ik.v} U^+ E
    g = G.transpose(0, 2, 1).reshape(nv, 4)
    grad = np.concatenate([4 * g.real.ravel(), -4 * g.imag.ravel()])
    return F, grad


def U_dU(A, K):
    P = np.exp(1j * K @ vs.T)
    U = (P @ A).reshape(-1, 2, 2)
    dU = np.stack([((1j * vs[:, j][None, :] * P) @ A).reshape(-1, 2, 2) for j in range(3)])
    return U, dU


def report(tag, x):
    A = unpack(x)
    Kf = grid(24)
    U, dU = U_dU(A, Kf)
    smin = np.linalg.svd(U, compute_uv=False).min()
    E = np.abs(U @ U.conj().transpose(0, 2, 1) - np.eye(2)).max()
    w, _ = w3_from(U, dU) if smin > 1e-6 else (np.nan, 0)
    print(f"  {tag}: F={F_and_grad(x)[0]:.3e}  sup|UU^+-1|(24^3)={E:.3e}  min sing.val={smin:.3e}  W3_GL={w:+.4f}")


# seed (a): truncated Fourier series of E3
Nf = 32
Kf = grid(Nf)
U3, _ = E3(Kf)
C = np.fft.fftn(U3.reshape(Nf, Nf, Nf, 2, 2), axes=(0, 1, 2)) / Nf ** 3  # A_v (coeff of e^{+ik.v}) at index v
A0 = np.array([C[int(v[0]) % Nf, int(v[1]) % Nf, int(v[2]) % Nf].reshape(4) for v in vs])
print(f"range r={r}: {nv} coefficient matrices, residual grid {4*r+2}^3")
x0 = pack(A0)
report("E3 truncated seed", x0)
res = minimize(F_and_grad, x0, jac=True, method="L-BFGS-B", options={"maxiter": 20000, "ftol": 1e-30, "gtol": 1e-14})
report(f"after L-BFGS ({res.nit} it)", res.x)
for t in range(3):
    xr = pack(rng.normal(size=(nv, 4)) + 1j * rng.normal(size=(nv, 4))) / np.sqrt(nv)
    res = minimize(F_and_grad, xr, jac=True, method="L-BFGS-B", options={"maxiter": 20000, "ftol": 1e-30, "gtol": 1e-14})
    report(f"random seed {t} ({res.nit} it)", res.x)
print(f"time {time.time()-t0:.1f}s")
