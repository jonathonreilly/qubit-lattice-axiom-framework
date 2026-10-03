#!/usr/bin/env python3
"""Coordinator pre-derivation check: 1D tight-binding (hopping t=1) wave packet hitting a recorded wall (hard edge)
with a capture channel at the surface site (no-jump evolution, on-site -i Gamma/2). Reflected norm vs formula
|r|^2 = (1 + G^2/4 - G sin k)/(1 + G^2/4 + G sin k)."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply
L = 1600
x = np.arange(L)            # site L-1 is the surface site next to the wall
def run(k, G, sig=60.0):
    H = diags([-np.ones(L - 1), -np.ones(L - 1)], [-1, 1], dtype=complex).tolil()
    H[L - 1, L - 1] = -0.5j * G
    H = H.tocsc()
    x0 = L // 2 - 250
    psi = np.exp(-(x - x0) ** 2 / (4 * sig ** 2) + 1j * k * x); psi /= np.linalg.norm(psi)
    v = 2 * np.sin(k)
    T = 2 * (L - 1 - x0) / v
    psi = expm_multiply(-1j * H * T, psi)
    return np.linalg.norm(psi) ** 2
for k in (np.pi / 2, np.pi / 3, np.pi / 6):
    for G in (0.2, 1.0, 2.0, 4.0, 20.0):
        R_num = run(k, G)
        R_th = (1 + G * G / 4 - G * np.sin(k)) / (1 + G * G / 4 + G * np.sin(k))
        print("k=%.3f G=%5.1f  reflected %.4f  formula %.4f" % (k, G, R_num, R_th))
