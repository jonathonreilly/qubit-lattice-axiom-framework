"""K2c PG-odd (PREREG.md): pure-gauge hard-indicator kernel for one crossing plane with Lx plaquettes, beta_g = 0, no fermions:
K(W_a, W_b) = g_Lx(W_b - W_a), g_Lx = Lx-fold circular self-convolution of f = 1(|theta| < delta). Computed by FFT on a fine grid
(two grid sizes for the convergence change) and by Fourier coefficients c_n = sin(n delta)/(n pi) (closed form); circulant
matrix on N = 64 equally spaced Wilson-line values; also N = 12 random values (descriptive)."""
import numpy as np
delta = 0.6
def g_grid(Lx, M):
    th = 2 * np.pi * np.arange(M) / M; th = np.where(th > np.pi, th - 2 * np.pi, th)
    f = (np.abs(th) < delta).astype(float); f[np.isclose(np.abs(th), delta)] = 0.5
    F = np.fft.fft(f) * (2 * np.pi / M)                  # = 2 pi c_n
    gk = F ** Lx / (2 * np.pi) ** (Lx - 1)              # Fourier coefficients of the Lx-fold convolution (times 2pi)
    return np.real(np.fft.ifft(gk)) * M / (2 * np.pi), th
for Lx in (1, 2, 3, 4):
    n = np.arange(1, 41); cn = np.sin(n * delta) / (n * np.pi); c0 = delta / np.pi
    coef = np.concatenate([[c0 ** Lx], cn ** Lx]); neg = [int(i) for i in np.nonzero(coef < 0)[0]]
    N = 64; out = []
    for M in (2 ** 16, 2 ** 18):
        g, th = g_grid(Lx, M); idx = (np.arange(N) * (M // N)) % M
        Kc = np.array([[g[(idx[j] - idx[i]) % M] for j in range(N)] for i in range(N)])
        ev = np.linalg.eigvalsh(0.5 * (Kc + Kc.T)); out.append(ev)
    ch = np.abs(out[1] - out[0]).max(); ev = out[1]
    print(f"Lx={Lx}: Fourier coeffs of K_PG negative at n = {neg[:12]}{' ...' if len(neg) > 12 else ''} | circulant N=64: lam_min {ev.min():+.4e} "
          f"lam_max {ev.max():.4e} min/max {ev.min()/ev.max():+.3e} | grid change {ch:.1e} | certified-negative {ev.min() < -1e3 * ch} PSD {ev.min() > -1e3 * ch}")
