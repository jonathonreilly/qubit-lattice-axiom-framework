"""Exploratory (descriptive): does a rational SEGMENT pool (no ring) in (X0, R), P = Q = 0, Y0 = 0, give a negative
matrix? Kernel K ~ box4(dR/2; a, a, 2d, 2d), a = (2d - |dX0|)_+ (closed form, positive constant dropped)."""
import numpy as np
from t22lib import box4
d = 0.6
for (hx, Kx, nR) in [(0.1, 15, 12), (0.1, 25, 12), (0.05, 30, 12), (0.1, 15, 8), (0.1, 10, 6), (0.1, 12, 5), (0.1, 8, 4)]:
    X = np.arange(-Kx, Kx + 1) * hx
    R = np.linspace(-1.1, 1.1, nR)
    XX, RR = np.meshgrid(X, R, indexing='ij'); XX = XX.ravel(); RR = RR.ravel()
    a = np.maximum(2 * d - np.abs(XX[:, None] - XX[None, :]), 0)
    A = np.stack([a, a, 2 * d + 0 * a, 2 * d + 0 * a], -1)
    Km = box4((RR[:, None] - RR[None, :]) / 2, A)
    ev = np.linalg.eigvalsh(Km)
    print(f"hx={hx} X0 in [{X[0]:.2f},{X[-1]:.2f}] ({len(X)}), R points {nR}: n={len(XX)} lam_min {ev[0]:+.4e} lam_max {ev[-1]:.4e} rel {ev[0]/ev[-1]:+.3e} #neg {(ev < -1e-12*ev[-1]*len(XX)).sum()}")
