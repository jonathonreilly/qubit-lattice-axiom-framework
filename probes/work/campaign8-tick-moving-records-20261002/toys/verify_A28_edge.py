#!/usr/bin/env python3
"""Coordinator's independent check of A28 Step 3c (edge floor): a half-filled free-fermion sea next to a hard wall
(the recorded site) is full rank on the unrecorded star of the empty site beside the wall.
1D: closed forms C11 = C22 = 1/2, C12 = 4/(3 pi) -> nu = 1/2 +- 4/(3 pi); bulk 3-site star nu = 1/2, 1/2 +- sqrt2/pi.
3D: planar wall (open in x, periodic y,z with a tiny twist), 6-site star next to the wall vs 7-site bulk star."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
def mb_min(nu):
    return float(np.prod(np.minimum(nu, 1 - nu)))
# 1D closed form
nu1 = np.array([0.5 - 4 / (3 * np.pi), 0.5 + 4 / (3 * np.pi)])
nub = np.array([0.5 - np.sqrt(2) / np.pi, 0.5, 0.5 + np.sqrt(2) / np.pi])
print("1D wall star nu =", np.round(nu1, 4), " min many-body eig = %.3e" % mb_min(nu1))
print("1D bulk star nu =", np.round(nub, 4), " min many-body eig = %.3e" % mb_min(nub))
# 1D finite check
for N in (200, 800):
    i = np.arange(1, N + 1); m = np.arange(1, N // 2 + 1)
    phi = np.sqrt(2 / (N + 1)) * np.sin(np.pi * np.outer(i, m) / (N + 1))
    C = phi[:2] @ phi[:2].T
    print("  N=%d wall-star nu = %s" % (N, np.round(np.linalg.eigvalsh(C), 5)))
# 3D planar wall
def star3d(Nx, L, x0, twist=0.013):
    xs = np.arange(1, Nx + 1); m = np.arange(1, Nx + 1)
    ex = -2 * np.cos(np.pi * m / (Nx + 1))
    ky = 2 * np.pi * (np.arange(L) + twist) / L; kz = 2 * np.pi * (np.arange(L) + 2 * twist) / L
    E = ex[:, None, None] - 2 * np.cos(ky)[None, :, None] - 2 * np.cos(kz)[None, None, :]
    occ = E < 0
    sites = [(x0, 0, 0), (x0 + 1, 0, 0), (x0, 1, 0), (x0, -1, 0), (x0, 0, 1), (x0, 0, -1)]
    if x0 > 1:
        sites.append((x0 - 1, 0, 0))
    n = len(sites); C = np.zeros((n, n), complex)
    sx = lambda x: np.sqrt(2 / (Nx + 1)) * np.sin(np.pi * m * x / (Nx + 1))
    for a, (xa, ya, za) in enumerate(sites):
        for b, (xb, yb, zb) in enumerate(sites):
            ph = np.exp(1j * (ky[None, :, None] * (yb - ya) + kz[None, None, :] * (zb - za)))
            C[a, b] = np.sum(occ * (sx(xa) * sx(xb))[:, None, None] * ph) / L ** 2
    nu = np.linalg.eigvalsh(C)
    return nu
for L in (16, 24):
    nu = star3d(64, L, 1)
    nb = star3d(64, L, 32)
    print("3D L=%d wall 6-star nu in [%.3f, %.3f], min many-body %.3e ; bulk 7-star min many-body %.3e" %
          (L, nu.min(), nu.max(), mb_min(nu), mb_min(nb)))
