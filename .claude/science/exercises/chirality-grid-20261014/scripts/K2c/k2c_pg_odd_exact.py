"""K2c follow-up V1 (PREREG.md): exact circulant eigenvalues of the pure-gauge hard-indicator kernel g_Lx(W_b - W_a) on
N = 64 equally spaced Wilson-line values: lam_j = N sum_{n = j mod N} c_n^Lx, c_n = sin(n delta)/(n pi), |n| <= Nmax,
with tail bound 2 / (pi^Lx (Lx-1) Nmax^(Lx-1))."""
import numpy as np
delta = 0.6; N = 64; Nmax = 10 ** 6
n = np.arange(-Nmax, Nmax + 1); c = np.where(n == 0, delta / np.pi, np.sin(n * delta) / (np.pi * np.where(n == 0, 1, n)))
for Lx in (2, 3, 4):
    cl = c ** Lx; lamj = N * np.array([cl[(n % N) == j].sum() for j in range(N)])
    tail = 2 / (np.pi ** Lx * (Lx - 1) * Nmax ** (Lx - 1)); bound = N * tail; jmin = int(np.argmin(lamj))
    print(f"Lx={Lx}: exact circulant N={N}: lam_min {lamj.min():+.6e} at j={jmin} (|j| = {min(jmin, N - jmin)}), lam_max {lamj.max():.6e}, "
          f"min/max {lamj.min()/lamj.max():+.3e} | N x tail bound {bound:.1e} | certified-negative {lamj.min() < -1e3 * bound} | PSD {lamj.min() > -bound}"
          f" | negative modes j: {[min(j, N - j) for j in np.nonzero(lamj < -bound)[0]][:12]}")
