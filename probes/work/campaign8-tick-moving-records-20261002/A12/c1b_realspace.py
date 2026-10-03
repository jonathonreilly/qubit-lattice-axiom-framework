"""C1b: independent real-space check of C1 (massive 1D Dirac step, m = 0.3, Hann window, carrier pi/2).
Ring of N sites x 2 components, dense single-particle step U; sea correlation C = projector onto the
eigenvectors of U with quasi-energy in (-pi, 0); w_hat = sum_t f(t) U^{-t} e_x^R; eps = <w|C|w>/<w|w>."""
import numpy as np
N, m, T, Om = 400, 0.3, 64, np.pi / 2
cm, sm = np.cos(m), np.sin(m)
S = np.zeros((2 * N, 2 * N), complex)                      # index 2*site + comp (0 = R, 1 = L)
for xx in range(N):
    S[2 * ((xx + 1) % N), 2 * xx] = 1                       # R moves right
    S[2 * ((xx - 1) % N) + 1, 2 * xx + 1] = 1               # L moves left
Cm = np.kron(np.eye(N), np.array([[cm, -1j * sm], [-1j * sm, cm]]))
U = Cm @ S
lam, V = np.linalg.eig(U)
V, _ = np.linalg.qr(V)                                      # U normal: orthonormalise (no degeneracy across bands)
th = -np.angle(lam)
Vl = V[:, th < 0]
print(f"unitarity err {np.abs(U.conj().T @ U - np.eye(2*N)).max():.1e}; filled modes {Vl.shape[1]} of {2*N}")
t = np.arange(T); w = np.sin(np.pi * (t + 1) / (T + 1)) ** 2 * np.exp(-1j * Om * t)
x = N // 2
v = np.zeros(2 * N, complex); v[2 * x] = 1
Ui = U.conj().T
wh = np.zeros(2 * N, complex); cur = v.copy()
for tt in range(T):
    wh += w[tt] * cur
    cur = Ui @ cur
ov = Vl.conj().T @ wh
print(f"real-space eps (Hann, T={T}, m={m}) = {np.vdot(ov, ov).real / np.vdot(wh, wh).real:.4e}  (C1 k-space: 6.149e-09)")
supp = np.nonzero(np.abs(wh) > 1e-14)[0] // 2 - x
print(f"support of w_hat: sites {supp.min():+d}..{supp.max():+d} (strict cone: within T-1 = {T-1})")
