import numpy as np
from t_f4_3_folded_slab import H_quot, S, Mt, lam
def H_phase(kx, kz, N, L, phi):
    H = H_quot(kx, kz, N, L, glued=False)
    A = (lam*S).conj().T @ Mt * np.exp(1j*kx*N/2)
    idx = lambda t, y: ((t-1)*N + (y % N))*4
    for y in range(N):
        ph = np.exp(1j*phi) if (y % N) < N//2 else 1.0
        i = idx(1, -y); j = idx(1, y)
        H[i:i+4, j:j+4] += 0.5*A*ph; H[j:j+4, i:i+4] += (0.5*A*ph).conj().T
    return H
N = 16
ks = 2*np.pi*np.arange(N)/N
prev = None
for L in (2, 3, 4, 5, 6, 8):
    E = {}
    for phi in (0.0, np.pi/2):
        tot = 0.0
        for kx in ks:
            for kz in ks:
                w = np.linalg.eigvalsh(H_phase(kx, kz, N, L, phi)); tot += w[w < 0].sum()
        E[phi] = tot
    dE = (E[np.pi/2] - E[0.0]) / (N*N*N)   # per gluing bond (N^3 sites on the face, one bond per site)
    print(f"L={L}: DeltaE per gluing bond = {dE:.3e}" + (f"   ratio to previous = {dE/prev:.3e}" if prev else ""))
    prev = dE
