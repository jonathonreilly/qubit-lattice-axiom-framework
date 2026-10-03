"""Check 9: for U = exp(-i H tau), J_MH / tau -> 2 Im[psi(y)^* H_yx psi(x)] (the comparator
continuous-time current) as tau -> 0; non-nearest-neighbour parts of J_MH are O(tau^2)."""
import numpy as np
from scipy.linalg import expm
from common import rand_state, mh_split
rng = np.random.default_rng(12)
N = 8
H = np.zeros((N, N), complex)
for x in range(N):
    h = rng.normal() + 1j * rng.normal()
    H[(x + 1) % N, x] = h; H[x, (x + 1) % N] = np.conj(h)
H += np.diag(rng.normal(size=N))
psi = rand_state(N, rng)
Jc = np.array([[2 * np.imag(np.conj(psi[y]) * H[y, x] * psi[x]) for y in range(N)] for x in range(N)])
for tau in (1e-1, 1e-2, 1e-3):
    pi, K, _ = mh_split(expm(-1j * H * tau), psi, N, 1)
    J = pi - pi.T
    nn = np.zeros((N, N), bool)
    for x in range(N):
        nn[x, (x + 1) % N] = nn[(x + 1) % N, x] = True
    far = ~nn & ~np.eye(N, dtype=bool)
    print(f"tau={tau:.0e}: max|J_MH/tau - J_cont| on bonds = {np.abs(J[nn]/tau - Jc[nn]).max():.2e}; "
          f"max|J_MH| beyond nearest neighbours = {np.abs(J[far]).max():.2e}")
