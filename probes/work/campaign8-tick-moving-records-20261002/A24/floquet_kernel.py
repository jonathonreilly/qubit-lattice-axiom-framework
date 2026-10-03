#!/usr/bin/env python3
"""A24 S6: reach of the ticked toy's conserved one-excitation energy E = W(K), cos W = cos m cos K.
W(K + pi) = pi - W(K), so only odd Fourier coefficients c_r (r in cells) are nonzero besides c_0 = pi/2.
They decay as r^-3/2 exp(-kappa r) with kappa = arccosh(1/cos m) ~ m: the energy terms touching a site reach about
one Compton length 1/m (EXACT for the symbol's branch points; CHECKED here)."""
import numpy as np
N = 1 << 16
K = 2 * np.pi * np.arange(N) / N
for m in (0.05, 0.1, 0.2, 0.6):
    W = np.arccos(np.cos(m) * np.cos(K))
    c = np.fft.fft(W).real / N
    even = np.abs(c[2:400:2]).max()
    r = np.arange(N)
    lo, hi = int(2 / m) | 1, int(8 / m) | 1
    rr = r[lo:hi:2]
    sl = np.polyfit(rr, np.log(np.abs(c[rr]) * rr ** 1.5), 1)[0]
    print(f"m={m}: c_0={c[0]:.6f}; max |even c_r| (r>0) = {even:.1e}; |c_1|={abs(c[1]):.3e}, |c_11|={abs(c[11]):.3e}, "
          f"|c_101|={abs(c[101]):.3e}; decay rate of |c_r| r^1.5 (odd r in [{lo},{hi}]) = {-sl:.5f}; arccosh(1/cos m) = "
          f"{np.arccosh(1/np.cos(m)):.5f}")
