"""C3c: is A9's eps(R) ~ R^-3 (truncated P_+ e_0) the spectral weight of soft states, |E| < a/R?
Single-site measure of the staggered sea (infinite volume, triple convolution of the sin^2 k law).
Small-E law: weight(|E| < Ec) = 8 cones * (4/3) pi Ec^3 / (2 pi)^3 = (4 / (3 pi^2)) Ec^3."""
import numpy as np
B, N1 = 2 ** 16, 2 ** 21
k = 2 * np.pi * (np.arange(N1) + 0.5) / N1
h = np.bincount(np.minimum((np.sin(k) ** 2 * B).astype(np.int64), B - 1), minlength=B) / N1
hs = np.clip(np.fft.irfft(np.fft.rfft(h, 4 * B) ** 3, 4 * B)[: 3 * B - 2], 0, None); hs /= hs.sum()
E = np.sqrt((np.arange(3 * B - 2) + 1.5) / B)
cum = np.cumsum(hs)
A9 = {6: 3.750e-4, 8: 1.738e-4, 12: 4.920e-5, 16: 2.054e-5}          # A9 sea_radius.out, L = 64
for Ec in (0.05, 0.1, 0.2):
    print(f"weight(|E|<{Ec}) = {np.interp(Ec, E, cum):.3e}  vs (4/(3 pi^2)) Ec^3 = {4/(3*np.pi**2)*Ec**3:.3e}")
for R, e in A9.items():
    Ec = np.interp(e, cum, E)
    print(f"R={R:2d}: eps_A9 = {e:.3e} equals the weight of states with |E| < {Ec:.4f} = {Ec*R:.3f}/R")
