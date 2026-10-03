"""C5: recording efficiency of a windowed formation rule (massless 1D Dirac step, R movers).
A T-tick window at site x sees exactly the R content on the T sites x-T+1..x (U^{-t} e_x^R = e_{x-t}^R).
Multi-mode rule: F = projector Q onto the window modes whose vacuum occupation nu_i < delta
(eigenvectors of the restricted sea projector A_-; nu = leakage into the filled half-circle).
Vacuum chance per window = 1 - prod(1 - nu_i). Efficiency for a one-particle excitation psi above the sea
(psi = P_+ of a Gaussian packet, mean quasi-energy k0, width sigma, centred in the window) = <psi|Q|psi>."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import numpy as np
from scipy.linalg import toeplitz

PI = np.pi
Nline = 8192
for T in (32, 64, 128):
    d = np.arange(T)
    col = np.where(d == 0, 0.5, 1j * (1 - (-1.0) ** d) / (2 * PI * np.maximum(d, 1)))   # a_-(d)
    A = toeplitz(col, col.conj())
    nu, V = np.linalg.eigh(A)
    for delta in (1e-6, 1e-10):
        sel = nu < delta
        Q = V[:, sel] @ V[:, sel].conj().T
        pvac = 1 - np.prod(1 - nu[sel])
        effs = []
        for k0, sig in ((PI / 2, T / 16), (PI / 2, T / 8), (PI / 4, T / 8), (3 * PI / 4, T / 8),
                        (0.6, T / 8), (0.3, T / 8), (0.1, T / 8)):
            xs = np.arange(Nline) - Nline // 2
            g = np.exp(1j * k0 * xs - (xs + T / 2) ** 2 / (2 * sig ** 2))     # centred in the window [-T+1, 0]
            G = np.fft.fft(g); kk = 2 * PI * np.fft.fftfreq(Nline)
            psi = np.fft.ifft(np.where((kk > 0) & (kk < PI), G, 0))            # upper band: k in (0, pi)
            psi /= np.linalg.norm(psi)
            win = psi[Nline // 2 - np.arange(T)]                                # sites x - t, t = 0..T-1
            effs.append((np.vdot(win, Q @ win)).real)
        print(f"T={T:4d} delta={delta:.0e}: {sel.sum():3d} quiet modes; vacuum chance/window {pvac:.2e}; "
              f"efficiency k0=pi/2 (sig T/16, T/8) {effs[0]:.4f} {effs[1]:.4f}; k0=pi/4 {effs[2]:.4f}; "
              f"3pi/4 {effs[3]:.4f}; k0=0.6 {effs[4]:.4f}; 0.3 {effs[5]:.4f}; 0.1 {effs[6]:.4f}")
