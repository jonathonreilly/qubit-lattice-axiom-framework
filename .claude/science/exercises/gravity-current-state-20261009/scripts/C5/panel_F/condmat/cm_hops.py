"""Hop amplitudes (Fourier coefficients) of the root D1 symbols s(k), W(k); only odd harmonics survive by the mirror identities."""
import sys, numpy as np
sys.path.insert(0, sys.argv[1])
from dirac import D1
law = D1(0.909103708, 0.555604226)
N = 1 << 15; k = 2*np.pi*np.arange(N)/N
s = law.S(k); W = law.W(k)
cs = np.fft.rfft(s)/N*2; cw = np.fft.rfft(W)/N*2
print("r   |s_r|        |W_r|")
for r in (1,3,5,7,9,11,15,21,31,41,63,101,201):
    print(f"{r:4d} {abs(cs[r]):.3e}  {abs(cw[r]):.3e}")
print("W(0..pi) at b, pi/2, pi-b, pi:", [round(float(law.W(x)),6) for x in (0.909103708, np.pi/2, np.pi-0.909103708, np.pi)])
