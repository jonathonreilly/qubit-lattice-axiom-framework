import numpy as np
from t_f4_3_folded_slab import G1, G3, G5, MU, Mt, My, S, lam
def H_spread(kx, kz, N, L, phi, spread=True):
    n = 4*N*L; H = np.zeros((n, n), complex)
    on = G1*np.sin(kx) + G3*np.sin(kz) + G5*(MU - np.cos(kx) - np.cos(kz))
    idx = lambda t, y: ((t-1)*N + (y % N))*4
    nb = 2*L - 1
    a = phi/nb if spread else 0.0
    ag = phi/nb if spread else phi
    active = lambda y: 1 <= (y % N) <= N//2 - 1          # segments {y,-y}, y in (0, N/2)
    for t in range(1, L+1):
        for y in range(N):
            i = idx(t, y); H[i:i+4, i:i+4] += on
            j = idx(t, y+1); H[i:i+4, j:j+4] += My; H[j:j+4, i:i+4] += My.conj().T
            if t < L:
                j = idx(t+1, y)
                ph = 1.0
                if active(y): ph = np.exp(1j*a)        # downward traversal (t+1 -> t) on the x side
                elif active(-y): ph = np.exp(-1j*a)    # upward traversal on the image side
                H[i:i+4, j:j+4] += Mt*ph; H[j:j+4, i:i+4] += (Mt*ph).conj().T
    A = (lam*S).conj().T @ Mt * np.exp(1j*kx*N/2)
    for y in range(N):
        ph = np.exp(1j*ag) if active(y) else (np.exp(-1j*ag) if active(-y) else 1.0)
        i = idx(1, -y); j = idx(1, y)
        H[i:i+4, j:j+4] += A*ph*0.5; H[j:j+4, i:i+4] += (A*ph*0.5).conj().T
    # (each unordered pair {y,-y} is visited twice in the loop above; the 0.5 keeps the bond strength equal to T-F4-3)
    assert np.allclose(H, H.conj().T)
    return H
N = 16; ks = 2*np.pi*np.arange(N)/N
# sanity: phi=0 reproduces T-F4-3 spectrum
from t_f4_3_folded_slab import H_quot
assert np.allclose(np.linalg.eigvalsh(H_spread(0.3, 0.7, N, 3, 0.0)), np.linalg.eigvalsh(H_quot(0.3, 0.7, N, 3, True)))
for spread in (False, True):
    print("spread" if spread else "concentrated")
    for L in (2, 3, 4, 6, 8):
        E = {}
        for phi in (0.0, np.pi/2):
            tot = 0.0
            for kx in ks:
                for kz in ks:
                    w = np.linalg.eigvalsh(H_spread(kx, kz, N, L, phi, spread)); tot += w[w < 0].sum()
            E[phi] = tot
        dE = (E[np.pi/2] - E[0.0]) / (N*N*N)
        print(f"  L={L}: DeltaE per face site = {dE:.4e};  DeltaE*(2L-1) = {dE*(2*L-1):.4e}")
