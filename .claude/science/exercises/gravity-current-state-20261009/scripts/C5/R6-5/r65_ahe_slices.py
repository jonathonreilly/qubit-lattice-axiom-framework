"""Diagnose r65_ahe_calib: slice Chern numbers C(kz) = 2*pi * (slice Kubo sum)/N^2 for the spatial-b Weyl test model."""
import numpy as np
s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
Z2 = np.zeros((2, 2)); beta = np.block([[s0, Z2], [Z2, -s0]]).astype(complex)
alpha = [np.block([[Z2, s], [s, Z2]]) for s in (sx, sy, sz)]; SigZ = np.block([[sz, Z2], [Z2, sz]])
N = 96; r, bz = 1.0, 0.2
k = 2 * np.pi * np.arange(N) / N - np.pi
for kz in [0.0, 0.1, 0.19, 0.21, 0.3, 1.0, 3.0]:
    K1, K2 = np.meshgrid(k, k, indexing='ij'); K3 = np.full_like(K1, kz)
    H = (np.sin(K1)[..., None, None] * alpha[0] + np.sin(K2)[..., None, None] * alpha[1] + np.sin(K3)[..., None, None] * alpha[2]
         + (r * (3 - np.cos(K1) - np.cos(K2) - np.cos(K3)))[..., None, None] * beta + bz * SigZ)
    vx = np.cos(K1)[..., None, None] * alpha[0] + (r * np.sin(K1))[..., None, None] * beta
    vy = np.cos(K2)[..., None, None] * alpha[1] + (r * np.sin(K2))[..., None, None] * beta
    E, U = np.linalg.eigh(H); Ud = np.conj(np.swapaxes(U, -1, -2)); X = Ud @ vx @ U; Y = Ud @ vy @ U
    occ = E < 0; tot = 0.0
    for n in range(4):
        for mm in range(4):
            sel = occ[..., n] & ~occ[..., mm]; d = E[..., n] - E[..., mm]
            tot += np.sum(np.where(sel, 2 * np.imag(X[..., n, mm] * Y[..., mm, n]) / np.where(sel, d, 1) ** 2, 0))
    print("kz=%.2f  C = %.4f   gap=%.4f" % (kz, 2 * np.pi * tot / N ** 2 * (2 * np.pi) / (2 * np.pi), np.abs(E).min()))
