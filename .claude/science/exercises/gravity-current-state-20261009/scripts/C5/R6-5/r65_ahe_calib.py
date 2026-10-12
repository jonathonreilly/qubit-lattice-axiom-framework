"""Calibration of the current vertices and 1/N^3 normalisation used in r65_cme*.py:
omega->0 limit of the same Lindhard expression (TKNN/Kubo Berry-curvature form) for the spatial-b Weyl semimetal
h = alpha.sin k + beta*r*sum(1-cos k) + bz*Sigma_z (m=0); prediction sigma_xy = Delta_k/(4 pi^2), Delta_k = 4 arcsin(bz/2).
Grid offset by half a step in k_z so that no grid point sits on a node."""
import numpy as np
s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
Z2 = np.zeros((2, 2)); beta = np.block([[s0, Z2], [Z2, -s0]]).astype(complex)
alpha = [np.block([[Z2, s], [s, Z2]]) for s in (sx, sy, sz)]; SigZ = np.block([[sz, Z2], [Z2, sz]])
for N in (48, 64, 96):
    k = 2 * np.pi * np.arange(N) / N - np.pi
    K1, K2, K3 = np.meshgrid(k, k, k + np.pi / N, indexing='ij')
    r, bz = 1.0, 0.2
    H = (np.sin(K1)[..., None, None] * alpha[0] + np.sin(K2)[..., None, None] * alpha[1] + np.sin(K3)[..., None, None] * alpha[2]
         + (r * (3 - np.cos(K1) - np.cos(K2) - np.cos(K3)))[..., None, None] * beta + bz * SigZ)
    vx = np.cos(K1)[..., None, None] * alpha[0] + (r * np.sin(K1))[..., None, None] * beta
    vy = np.cos(K2)[..., None, None] * alpha[1] + (r * np.sin(K2))[..., None, None] * beta
    E, U = np.linalg.eigh(H); Ud = np.conj(np.swapaxes(U, -1, -2))
    X = Ud @ vx @ U; Y = Ud @ vy @ U
    occ = E < 0
    tot = 0.0
    for n in range(4):
        for mm in range(4):
            sel = occ[..., n] & ~occ[..., mm]
            d = (E[..., n] - E[..., mm])
            tot += np.sum(np.where(sel, 2 * np.imag(X[..., n, mm] * Y[..., mm, n]) / np.where(sel, d, 1) ** 2, 0))
    print("N=%d  |sigma_xy| = %.5f   Delta_k/(4pi^2) = %.5f" % (N, abs(tot) / N ** 3, 4 * np.arcsin(bz / 2) / (4 * np.pi ** 2)))
